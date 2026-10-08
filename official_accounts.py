"""
VAL.PEA -- Comptes officiels (08/10/2026) : 2e source pour les chiffres d'entreprise.

Source : filings.xbrl.org (XBRL International), qui rassemble les rapports
annuels au format europeen ESEF que toutes les societes cotees de l'UE doivent
deposer depuis 2021. Gratuit, sans cle.

Pour chaque valeur suivie (qualite OK, proche, ou avec une fiche) :
  1. retrouve la societe (identifiant LEI) -- cache dans lei_map.json ;
  2. lit le dernier rapport annuel depose ;
  3. compare chiffre d'affaires et resultat net part du groupe aux chiffres
     Yahoo de la meme annee (revh / nih de data.js) ;
  4. ecart > 5 % -> champ x2 de la fiche ("donnee a verifier", achat bloque).
Champs ecrits : x2 (ecarts, texte), x2s (source + annee controlee).
Limites : rapports annuels seulement, deposes avec plusieurs mois de retard ;
toutes les societes ne sont pas presentes. Ne corrige jamais : signale.
"""
import json, re, time, unicodedata
import requests
from tickers import YF_MAP

B = 'https://filings.xbrl.org'
CACHE = 'lei_map.json'
TOL = 0.05
COUNTRY = {'PA': 'FR', 'AS': 'NL', 'DE': 'DE', 'MI': 'IT', 'CO': 'DK', 'ST': 'SE', 'BR': 'BE',
           'MC': 'ES', 'HE': 'FI', 'OL': 'NO', 'LS': 'PT', 'VI': 'AT', 'IR': 'IE'}
REV = ('ifrs-full:Revenue', 'ifrs-full:RevenueFromContractsWithCustomers')
NI = ('ifrs-full:ProfitLossAttributableToOwnersOfParent',)
STOP = {'SA', 'SE', 'NV', 'AG', 'SPA', 'GROUP', 'GROUPE', 'THE', 'HOLDING', 'CIE', 'ET', 'DE', 'LA', 'LE', 'AB', 'ASA', 'OYJ', 'PLC'}


def get(u, tries=3):
    for i in range(tries):
        try:
            r = requests.get(u if u.startswith('http') else B + u, timeout=40)
            if r.status_code == 200:
                return r.json()
        except Exception:
            pass
        time.sleep(2 * (i + 1))
    return None


def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().upper()
    return [w for w in re.findall(r'[A-Z0-9]+', s) if w not in STOP]


def load_stocks():
    t = open('data.js', encoding='utf-8').read().split('const ETF')[0]
    out = {}
    for b in re.split(r"\{ticker:'", t)[1:]:
        tk = b.split("'")[0]
        g = lambda k: (re.search(r'\b' + k + r":'([^']*)'", b) or [None, None])[1]
        gb = lambda k: (re.search(r'\b' + k + r":(true|false)", b) or [None, 'false'])[1] == 'true'
        out[tk] = {'name': g('name'), 'yrs': g('yrs'), 'revh': g('revh'), 'nih': g('nih'), 'fcur': g('fcur'),
                   'qok': gb('qok'), 'near': gb('near')}
    return out


def fiche_tickers():
    try:
        t = open('fiches.js', encoding='utf-8').read()
        return set(re.findall(r"^\s*'?([A-Z0-9]+)'?\s*:\s*\{", t, re.M))
    except Exception:
        return set()


def resolve(tk, name, country, cache):
    if tk in cache:
        return cache[tk]
    words = norm(name)
    if not words:
        return None
    key = max(words, key=len)
    d = get('/api/entities?page[size]=25&filter=' + json.dumps([{"name": "name", "op": "ilike", "val": f"%{key}%"}]))
    best = None
    for e in (d or {}).get('data', []):
        a = e.get('attributes', {})
        ew = norm(a.get('name'))
        score = sum(1 for w in words if w in ew) / len(words)
        if ew and ew[0] == words[0]:
            score += 0.5
        if score < 0.5:
            continue
        f = get(f"/api/entities/{a.get('identifier')}/filings?page[size]=1")
        c = ((f or {}).get('data') or [{}])[0].get('attributes', {}).get('country')
        if country and c and c != country:
            continue
        if not best or score > best[0]:
            best = (score, a.get('identifier'), a.get('name'))
    cache[tk] = {'lei': best[1], 'name': best[2]} if best else None
    return cache[tk]


def year_values(facts, concepts):
    """{annee de cloture: valeur} pour des faits sans axe, d'une duree ~1 an."""
    out = {}
    for f in facts.values():
        dm = f.get('dimensions', {})
        if dm.get('concept') not in concepts or set(dm) != {'concept', 'entity', 'period', 'unit'}:
            continue
        p = dm.get('period', '')
        if '/' not in p:
            continue
        a, b = p.split('/')
        try:
            days = (time.mktime(time.strptime(b[:10], '%Y-%m-%d')) - time.mktime(time.strptime(a[:10], '%Y-%m-%d'))) / 86400
            v = float(f.get('value'))
        except Exception:
            continue
        if 350 <= days <= 380:
            yr = str(int(b[:4]) - (1 if b[5:10] <= '01-15' else 0))
            out.setdefault(yr, (v, dm.get('unit', '').split(':')[-1]))
    return out


def official(lei):
    fl = get(f'/api/entities/{lei}/filings?page[size]=50')
    items = [x.get('attributes', {}) for x in (fl or {}).get('data', [])]
    items = [a for a in items if a.get('json_url') and a.get('period_end')]
    if not items:
        return None
    a = sorted(items, key=lambda x: (x['period_end'], x.get('date_added') or ''))[-1]
    j = get(a['json_url'])
    if not j:
        return None
    facts = j.get('facts', {})
    return {'period_end': a['period_end'], 'rev': year_values(facts, REV), 'ni': year_values(facts, NI)}


def main():
    S = load_stocks()
    scope = {tk for tk, s in S.items() if s['qok'] or s['near']} | (fiche_tickers() & set(S))
    try:
        cache = json.load(open(CACHE, encoding='utf-8'))
    except Exception:
        cache = {}
    res, n_ok, n_cmp = {}, 0, 0
    for tk in sorted(scope):
        y = YF_MAP.get(tk, '')
        country = COUNTRY.get(y.rsplit('.', 1)[-1]) if '.' in y else None
        ent = resolve(tk, S[tk]['name'], country, cache)
        if not ent:
            res[tk] = {'status': 'societe introuvable'}
            continue
        o = official(ent['lei'])
        if not o:
            res[tk] = {'status': 'aucun rapport lisible', 'lei': ent['lei']}
            continue
        yrs = (S[tk]['yrs'] or '').split('|')
        issues, checked = [], []
        for lab, key, src in (('CA', 'revh', o['rev']), ('resultat net', 'nih', o['ni'])):
            ys = (S[tk][key] or '').split('|')
            for yr, (val, unit) in sorted(src.items(), reverse=True)[:2]:
                if yr not in yrs or unit != (S[tk]['fcur'] or unit):
                    continue
                try:
                    yv = float(ys[yrs.index(yr)]) * 1e6
                except Exception:
                    continue
                checked.append(f'{lab} {yr}')
                if val and abs(yv / val - 1) > TOL:
                    issues.append(f'{lab} {yr} officiel {val / 1e6:,.0f} M contre Yahoo {yv / 1e6:,.0f} M'.replace(',', ' '))
        if checked:
            n_cmp += 1
            n_ok += not issues
        res[tk] = {'status': 'compare' if checked else 'annees non comparables', 'lei': ent['lei'], 'entity': ent['name'],
                   'period_end': o['period_end'], 'checked': checked, 'issues': issues}
        time.sleep(0.3)
    json.dump(cache, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
    json.dump({'date': time.strftime('%Y-%m-%d'), 'scope': len(scope), 'compared': n_cmp, 'ok': n_ok, 'res': res},
              open('official_check.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'Comptes officiels : {len(scope)} valeurs, {n_cmp} comparees, {n_ok} concordantes')
    # ecriture dans data.js : x2 / x2s (efface les anciennes valeurs)
    js = open('data.js', encoding='utf-8').read()
    head, sep, tail = js.partition('const ETF')

    def patch(m):
        tk = m.group(1)
        r = res.get(tk) or {}
        iss = ' · '.join(r.get('issues', [])).replace("'", ' ')
        src = ('comptes officiels ' + r['period_end'][:4]) if r.get('checked') else ''
        return "{ticker:'" + tk + "',x2:'" + iss + "',x2s:'" + src + "'"
    head = re.sub(r"\{ticker:'([^']+)'(?:,x2:'[^']*',x2s:'[^']*')?", patch, head)
    open('data.js', 'w', encoding='utf-8').write(head + sep + tail)


if __name__ == '__main__':
    main()
