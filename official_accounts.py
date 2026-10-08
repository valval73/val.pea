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
Resultat : official_check.json (lu par la fiche et le mail du samedi).
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
        g = lambda k: ((re.search(r'\b' + k + r":'((?:[^'\\]|\\.)*)'", b) or [None, None])[1] or '').replace("\\'", "'") or None
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


# Noms officiels quand le nom usuel ne suffit pas (verifies le 08/10/2026)
# Correspondance impossible a garantir (homonymes) : on n'affirme rien plutot que de se tromper
SKIP = {'RACE': 'homonyme Ferrari Group plc'}
# Ecarts de definition connus (pas des erreurs) : controle du CA desactive
NO_REV = {'TTE': 'CA officiel avec droits d accise, Yahoo sans'}
SEARCH_NAME = {'ITX': 'INDUSTRIA DE DISENO TEXTIL', 'OR': 'OREAL', 'AIR': 'AIRBUS', 'TTE': 'TOTALENERGIES',
               'RACE': 'FERRARI', 'NSIS': 'NOVONESIS', 'RBT': 'ROBERTET'}


def resolve(tk, name, country, cache):
    """Retrouve l'identifiant LEI. Tous les mots du nom doivent figurer dans le
    nom officiel (evite Brunel International pour ASM International, ou
    Dassault Systemes pour Dassault Aviation). Pas de filtre pays : Airbus ou
    Ferrari deposent aux Pays-Bas tout en etant cotees a Paris ou Milan."""
    if tk in cache and cache[tk]:
        return cache[tk]
    words = norm(SEARCH_NAME.get(tk) or name)
    if not words:
        return None
    key = max(words, key=len)
    d = get('/api/entities?page[size]=50&filter=' + json.dumps([{"name": "name", "op": "ilike", "val": f"%{key}%"}]))
    best = None
    for e in (d or {}).get('data', []):
        a = e.get('attributes', {})
        ew = norm(a.get('name'))
        if not ew or not all(w in ew for w in words):
            continue
        score = (ew[0] == words[0]) * 1.0 - len(ew) * 0.01   # nom court et qui commence pareil
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
    # du plus recent au plus ancien ; si un rapport est illisible, on prend le precedent
    for a in sorted(items, key=lambda x: (x['period_end'], x.get('date_added') or ''), reverse=True)[:3]:
        j = get(a['json_url'])
        if not j:
            continue
        facts = j.get('facts', {})
        o = {'period_end': a['period_end'], 'rev': year_values(facts, REV), 'ni': year_values(facts, NI)}
        if o['rev'] or o['ni']:
            return o
    return None


def main():
    S = load_stocks()
    scope = {tk for tk, s in S.items() if s['qok'] or s['near']} | (fiche_tickers() & set(S))
    try:
        cache = json.load(open(CACHE, encoding='utf-8'))
    except Exception:
        cache = {}
    res, n_ok, n_cmp = {}, 0, 0
    for tk in sorted(scope):
      try:
        y = YF_MAP.get(tk, '')
        country = COUNTRY.get(y.rsplit('.', 1)[-1]) if '.' in y else None
        if tk in SKIP:
            res[tk] = {'status': 'non controle : ' + SKIP[tk]}
            continue
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
        for lab, key, src in (('CA', 'revh', {} if tk in NO_REV else o['rev']), ('resultat net', 'nih', o['ni'])):
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
      except Exception as ex:
        res[tk] = {'status': 'erreur ' + str(ex)[:80]}
    json.dump(cache, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
    json.dump({'date': time.strftime('%Y-%m-%d'), 'scope': len(scope), 'compared': n_cmp, 'ok': n_ok, 'res': res},
              open('official_check.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'Comptes officiels : {len(scope)} valeurs, {n_cmp} comparees, {n_ok} concordantes')
    # 08/10/2026 : resultat dans official_check.json uniquement (lu par le site et
    # le mail) : pas d'ecriture concurrente de data.js avec la mise a jour Yahoo.


if __name__ == '__main__':
    main()
