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
# 19/10/2026 : bilan, pour recalculer le ROIC (cas KSB, Knorr-Bremse : ROIC Yahoo
# tres superieur a la realite). ROIC officiel = resultat operationnel x 0,75 /
# (capitaux propres + dettes financieres - tresorerie), dernier exercice depose.
EBIT_C = ('ifrs-full:ProfitLossFromOperatingActivities',)
EQ_C = ('ifrs-full:EquityAttributableToOwnersOfParent',)
DEBT_TOT = ('ifrs-full:Borrowings',)
DEBT_PARTS = ('ifrs-full:LongtermBorrowings', 'ifrs-full:ShorttermBorrowings',
              'ifrs-full:CurrentPortionOfLongtermBorrowings', 'ifrs-full:NoncurrentPortionOfNoncurrentBorrowings')
CASH_C = ('ifrs-full:CashAndCashEquivalents',)
# 19/10/2026 : cash libre APRES loyers (IFRS 16). Yahoo ne separe pas les loyers
# des remboursements de dette : son cash libre surestime celui des commerces.
CFO_C = ('ifrs-full:CashFlowsFromUsedInOperatingActivities',)
CAPEX_C = ('ifrs-full:PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities',
           'ifrs-full:PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities')
LEASE_C = ('ifrs-full:PaymentsOfLeaseLiabilitiesClassifiedAsFinancingActivities',)
LEASE_MIN = 0.10   # loyers > 10 % du flux d'exploitation : la correction compte
CASH_SEUIL = 80
ROIC_RATIO, ROIC_GAP = 1.5, 8.0   # alerte si Yahoo > 1,5 x l'officiel ET +8 points
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
        rm = re.search(r'[,{]roic:([0-9.]+)', b)
        out[tk] = {'name': g('name'), 'yrs': g('yrs'), 'revh': g('revh'), 'nih': g('nih'), 'fcur': g('fcur'),
                   'roic': float(rm.group(1)) if rm else None,
                   'qok': gb('qok'), 'near': gb('near'),
                   'fcfc': float(re.search(r'[,{]fcfc:([0-9.]+)', b).group(1)) if re.search(r'[,{]fcfc:([0-9.]+)', b) else None}
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
NO_REV = {'TTE': 'CA officiel avec droits d accise, Yahoo sans',
          'PLUXEE': 'CA Yahoo avec revenus financiers du float, officiel sans',
          'EDENRED': 'CA Yahoo avec revenus financiers du float, officiel sans'}
# Banques : Yahoo retire les coupons des obligations perpetuelles (AT1) du resultat
NO_NI = {'BNP': 'coupons AT1', 'ACA': 'coupons AT1', 'GLE': 'coupons AT1'}
MIN_ABS = 5e6   # ecart absolu minimal (les chiffres Yahoo sont arrondis au million)
SEARCH_NAME = {'AMS': 'AMADEUS IT GROUP', 'ITX': 'INDUSTRIA DE DISENO TEXTIL', 'OR': 'OREAL', 'AIR': 'AIRBUS', 'TTE': 'TOTALENERGIES',
               'RACE': 'FERRARI', 'NSIS': 'NOVONESIS', 'RBT': 'ROBERTET'}


# Novo Nordisk etait rattachee a la fondation (Novo Nordisk Fonden) : CA, resultat
# et ROIC compares a ceux de la fondation -> faux ecarts, achat bloque a tort.
LEI_FIXE = {'NOVO': ('549300DAQ1CVT6CXN342', 'NOVO NORDISK A/S')}


def resolve(tk, name, country, cache):
    """Retrouve l'identifiant LEI. Tous les mots du nom doivent figurer dans le
    nom officiel (evite Brunel International pour ASM International, ou
    Dassault Systemes pour Dassault Aviation). Pas de filtre pays : Airbus ou
    Ferrari deposent aux Pays-Bas tout en etant cotees a Paris ou Milan."""
    if tk in LEI_FIXE:   # 19/10/2026 : correspondance verifiee a la main
        cache[tk] = {'lei': LEI_FIXE[tk][0], 'name': LEI_FIXE[tk][1]}
        return cache[tk]
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


def instant_values(facts, concepts):
    """{annee: valeur} pour des soldes de bilan (date unique), sans axe."""
    out = {}
    for f in facts.values():
        dm = f.get('dimensions', {})
        if dm.get('concept') not in concepts or set(dm) != {'concept', 'entity', 'period', 'unit'}:
            continue
        p = dm.get('period', '')
        if '/' in p:
            continue
        try:
            v = float(f.get('value'))
        except Exception:
            continue
        yr = str(int(p[:4]) - (1 if p[5:10] <= '01-15' else 0))
        out[yr] = out.get(yr, 0.0) + v if len(concepts) > 1 else v
    return out


def official_roic(facts):
    eb = year_values(facts, EBIT_C)
    eq = instant_values(facts, EQ_C)
    if not eb or not eq:
        return None
    yr = max(set(eb) & set(eq), default=None)
    if not yr:
        return None
    debt = instant_values(facts, DEBT_TOT).get(yr)
    if debt is None:
        parts = {c: instant_values(facts, (c,)).get(yr) for c in DEBT_PARTS}
        if all(v is None for v in parts.values()):
            return None   # dette non lisible : on n'affirme rien
        debt = sum(v for v in parts.values() if v)
    cash = instant_values(facts, CASH_C).get(yr) or 0.0
    ic = eq[yr] + debt - cash
    if ic <= 0:
        ic = eq[yr] + debt   # tresorerie > capitaux (meme regle que le screener)
    if ic <= 0:
        return None
    return {'annee': yr, 'roic': round(eb[yr][0] * 0.75 / ic * 100, 1)}


def official_cash(facts):
    """Conversion du benefice en cash apres loyers, derniere annee publiee."""
    cfo, ni, ls = year_values(facts, CFO_C), year_values(facts, NI), year_values(facts, LEASE_C)
    yr = max(set(cfo) & set(ni) & set(ls), default=None)
    if not yr or ni[yr][0] <= 0:
        return None
    capex = sum(abs(year_values(facts, (c,)).get(yr, (0, ''))[0]) for c in CAPEX_C)
    lease = abs(ls[yr][0])
    if cfo[yr][0] <= 0 or lease < LEASE_MIN * cfo[yr][0]:
        return None
    return {'annee': yr, 'cash': round((cfo[yr][0] - capex - lease) / ni[yr][0] * 100),
            'loyers_pct_cfo': round(lease / cfo[yr][0] * 100)}


# ═══ 19/10/2026 : comptes officiels americains (SEC, data.sec.gov) pour le compte-titres ═══
# Gratuit, officiel, 10 ans et plus. La SEC exige un User-Agent identifiant l'usage.
SEC_UA = {'User-Agent': 'VAL.PEA screener personnel valpea@users.noreply.github.com'}
SEC_REV = ('Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet')
SEC_NI = ('NetIncomeLoss',)
_SEC_CIK = None


def sec_get(u):
    for i in range(3):
        try:
            r = requests.get(u, headers=SEC_UA, timeout=40)
            if r.status_code == 200:
                return r.json()
        except Exception:
            pass
        time.sleep(2 * (i + 1))
    return None


def sec_cik(sym):
    global _SEC_CIK
    if _SEC_CIK is None:
        j = sec_get('https://www.sec.gov/files/company_tickers.json') or {}
        _SEC_CIK = {v['ticker'].upper(): str(v['cik_str']).zfill(10) for v in j.values()}
    return _SEC_CIK.get(sym.upper().replace('-', '.')) or _SEC_CIK.get(sym.upper())


def sec_years(facts, concepts):
    """{annee: (valeur, 'USD')} depuis les 10-K (exercices d'environ un an)."""
    out = {}
    for c in concepts:
        for f in ((facts.get('us-gaap') or {}).get(c) or {}).get('units', {}).get('USD', []):
            if f.get('form') != '10-K' or f.get('fp') != 'FY' or not f.get('start') or not f.get('end'):
                continue
            try:
                days = (time.mktime(time.strptime(f['end'], '%Y-%m-%d')) - time.mktime(time.strptime(f['start'], '%Y-%m-%d'))) / 86400
            except Exception:
                continue
            if 350 <= days <= 380:
                b = f['end']
                yr = str(int(b[:4]) - (1 if b[5:10] <= '01-15' else 0))
                out.setdefault(yr, (float(f['val']), 'USD'))
        if out:
            return out
    return out


def sec_official(sym):
    cik = sec_cik(sym)
    if not cik:
        return None
    j = sec_get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json')
    if not j:
        return None
    fx = j.get('facts') or {}
    rev, ni = sec_years(fx, SEC_REV), sec_years(fx, SEC_NI)
    if not rev and not ni:
        return None
    ys = sorted(rev)
    h = {}
    if len(ys) >= 6:
        a, b = ys[max(0, len(ys) - 11)], ys[-1]
        n = int(b) - int(a)
        if n > 0 and rev[a][0] > 0 and rev[b][0] > 0:
            h['ca_croissance_an'] = round(((rev[b][0] / rev[a][0]) ** (1 / n) - 1) * 100, 1)
            h['annees'] = n + 1
        h['annees_en_perte'] = sum(1 for y in sorted(ni)[-10:] if ni[y][0] < 0)
    return {'period_end': (ys[-1] if ys else ''), 'rev': rev, 'ni': ni, 'roic': None, 'cash': None,
            'cik': cik, 'entity': j.get('entityName', ''), 'histo': h}


def official(lei):
    fl = get(f'/api/entities/{lei}/filings?page[size]=50')
    items = [x.get('attributes', {}) for x in (fl or {}).get('data', [])]
    items = [a for a in items if a.get('json_url') and a.get('period_end')]
    # du plus recent au plus ancien ; si un rapport est illisible, on prend le precedent
    for a in sorted(items, key=lambda x: (x['period_end'], x.get('date_added') or ''), reverse=True)[:6]:
        j = get(a['json_url'])
        if not j:
            continue
        facts = j.get('facts', {})
        o = {'period_end': a['period_end'], 'rev': year_values(facts, REV), 'ni': year_values(facts, NI),
             'roic': official_roic(facts), 'cash': official_cash(facts)}
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
        if y and '.' not in y:   # valeur americaine : SEC
            o = sec_official(y)
            if not o:
                # 19/10/2026 : la SEC refuse les serveurs de GitHub (403) : on le dit
                res[tk] = {'status': 'SEC inaccessible depuis GitHub' if not _SEC_CIK else 'SEC : societe introuvable'}
                continue
            ent = {'lei': 'CIK' + o['cik'], 'name': o['entity']}
            time.sleep(0.2)
        else:
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
        for lab, key, src in (('CA', 'revh', {} if tk in NO_REV else o['rev']), ('resultat net', 'nih', {} if tk in NO_NI else o['ni'])):
            ys = (S[tk][key] or '').split('|')
            for yr, (val, unit) in sorted(src.items(), reverse=True)[:2]:
                if yr not in yrs or unit != (S[tk]['fcur'] or unit):
                    continue
                try:
                    yv = float(ys[yrs.index(yr)]) * 1e6
                except Exception:
                    continue
                checked.append(f'{lab} {yr}')
                if val and abs(yv / val - 1) > TOL and abs(yv - val) > MIN_ABS:
                    issues.append(f'{lab} {yr} officiel {val / 1e6:,.0f} M contre Yahoo {yv / 1e6:,.0f} M'.replace(',', ' '))
        # 19/10/2026 : ROIC recalcule sur le bilan officiel ; seule une SURestimation
        # par Yahoo bloque l'achat (c'est elle qui cree de faux signaux)
        ro, ry = o.get('roic'), S[tk].get('roic')
        if ro and ry is not None and tk not in NO_NI:
            checked.append(f"ROIC {ro['annee']}")
            if ry > ro['roic'] * ROIC_RATIO and ry - ro['roic'] > ROIC_GAP:
                issues.append(f"ROIC officiel {ro['roic']} % ({ro['annee']}) contre {ry} % calcule avec Yahoo")
        oc, yc = o.get('cash'), S[tk].get('fcfc')
        if oc and yc is not None:
            checked.append(f"cash apres loyers {oc['annee']}")
            if yc >= CASH_SEUIL and oc['cash'] < CASH_SEUIL:
                issues.append(f"cash après loyers {oc['cash']} % ({oc['annee']}, loyers = {oc['loyers_pct_cfo']} % du flux d'exploitation) contre {yc:.0f} % selon Yahoo : sous le seuil de 80 %")
        if checked:
            n_cmp += 1
            n_ok += not issues
        res[tk] = {'status': 'compare' if checked else 'annees non comparables', 'lei': ent['lei'], 'entity': ent['name'],
                   'period_end': o['period_end'], 'checked': checked, 'issues': issues,
                   'roic_officiel': (o.get('roic') or {}).get('roic'), 'cash_apres_loyers': (o.get('cash') or {}).get('cash'),
                   'histo_10a': o.get('histo') or None}
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
