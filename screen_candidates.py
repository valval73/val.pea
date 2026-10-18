"""
VAL.PEA -- Passe la banque de candidats (candidats.json) dans le MEME filtre
qualite que le screener (compute_quality), sans les ajouter au site.
Sortie : candidats_resultats.json (qok, criteres en echec, chiffres cles).
Les chiffres viennent de Yahoo ; rien n'est repris d'un autre screener.
Lancement manuel (GitHub Actions > Candidats > Run workflow).
"""
import json, time, re, unicodedata
import yfinance as yf
from fetch_fundamentals import compute_quality, qarp_value, expected_return, implied_growth, QV_GMAX

# code de marche (MIC) -> suffixe Yahoo
SUFFIX = {'XPAR': '.PA', 'XETR': '.DE', 'XFRA': '.F', 'XMIL': '.MI', 'XMAD': '.MC',
          'XAMS': '.AS', 'XBRU': '.BR', 'XLIS': '.LS', 'XSTO': '.ST', 'XOSL': '.OL',
          'XHEL': '.HE', 'XCSE': '.CO', 'XWBO': '.VI', 'XWAR': '.WA', 'XBUD': '.BD',
          'XICE': '.IC', 'XDUB': '.IR', 'XBSE': '.RO', 'XNYS': '', 'XNGS': '',
          'XLON': '.L', 'XSWX': '.SW', 'XTSE': '.TO',
          'ASEX': '.AT', 'XSAT': '.ST', 'XDUS': '.DU', 'XPRA': '.PR'}


# 18/10/2026 : frais Bourse Direct par place (grille publique boursedirect.fr,
# consultee le 18/10/2026). 'autres' = 0,48 % min. 41,90 EUR, liste exacte des
# places a confirmer aupres du courtier.
COURTAGE = {'.PA': 'Euronext (0,99-3,80 EUR)', '.AS': 'Euronext (0,99-3,80 EUR)',
            '.BR': 'Euronext (0,99-3,80 EUR)', '.LS': 'Lisbonne (0,20 % min. 18 EUR)',
            '.DE': 'Xetra (0,15 % min. 15 EUR)', '.L': 'Londres (0,15 % min. 15 EUR)',
            '.MC': 'Madrid (0,20 % min. 18 EUR)', '.SW': 'Suisse (0,20 % min. 18 EUR)'}


def courtage(sym):
    if '.' not in sym:
        return 'New York (8,50 EUR jusqu a 10 000 EUR)'
    return COURTAGE.get('.' + sym.rsplit('.', 1)[1],
                        'autre place (0,48 % min. 41,90 EUR, acces a confirmer)')


# Paliers : meme regle que le screener (palier 1 = demi-position, palier 2 =
# position complete). Candidat sans evaluation du moat -> incertitude 'elevee'
# (marges 20 % / 30 %), la plus prudente de la grille.
MARGES_CANDIDAT = (0.30, 0.20)


# 18/10/2026 : le PEA exige un siege dans l'UE/EEE. Les places de Vienne,
# Francfort ou Varsovie cotent aussi des societes americaines ou asiatiques
# (Nvidia, Meta...) : on les ecarte sur le pays du siege donne par Yahoo.
PAYS_PEA = {'France', 'Germany', 'Italy', 'Spain', 'Netherlands', 'Belgium', 'Portugal', 'Austria',
            'Finland', 'Ireland', 'Greece', 'Estonia', 'Lithuania', 'Latvia', 'Sweden', 'Denmark',
            'Norway', 'Poland', 'Czech Republic', 'Czechia', 'Hungary', 'Romania', 'Iceland', 'Luxembourg',
            'Slovenia', 'Slovakia', 'Croatia', 'Bulgaria', 'Cyprus', 'Malta', 'Liechtenstein'}


# Industries cycliques (classement Yahoo) : un benefice de haut de cycle,
# prolonge 10 ans, gonfle la valeur. Pas de palier tant qu'il n'y a pas de
# grille dediee (meme logique que la regle du reinvestissement).
CYCLIQUES = ('Engineering & Construction', 'Residential Construction', 'Building Materials',
             'Oil & Gas', 'Marine Shipping', 'Steel', 'Aluminum', 'Copper', 'Other Industrial Metals',
             'Gold', 'Silver', 'Coal', 'Chemicals', 'Specialty Chemicals', 'Agricultural Inputs',
             'Auto Manufacturers', 'Auto Parts', 'Airlines', 'Semiconductors', 'Semiconductor Equipment',
             'Paper', 'Lumber', 'Trucking', 'Farm & Heavy Construction Machinery')


def norm_nom(n):
    n = re.sub(r'[^A-Z0-9 ]', ' ', unicodedata.normalize('NFKD', n or '').encode('ascii', 'ignore').decode().upper())
    mots = [m for m in n.split() if m not in ('SA', 'SE', 'NV', 'AG', 'SPA', 'S', 'P', 'A', 'AB', 'ASA', 'OYJ', 'PLC', 'KGAA',
                                              'CO', 'GROUP', 'GROUPE', 'HOLDING', 'INC', 'CORP', 'CORPORATION', 'LTD', 'THE',
                                              'SER', 'B', 'PUBL', 'NV', 'C', 'XWAR', 'PLN', 'INTERNATIONAL')]
    return ' '.join(mots[:3])


def _noms_screener():
    try:
        t = open('data.js', encoding='utf-8').read()
        return {norm_nom(m) for m in re.findall(r"[,{]name:'([^']*)'", t)} - {''}
    except Exception:
        return set()


NOMS_SCREENER = _noms_screener()
NOMS_UN_MOT = {n for n in NOMS_SCREENER if ' ' not in n and len(n) >= 5}
try:
    EXCLUS = json.load(open('univers_exclus_pea.json', encoding='utf-8'))
except Exception:
    EXCLUS = {}


def charger_listes():
    C = json.load(open('candidats.json', encoding='utf-8'))
    for f in ('univers_pea.json', 'univers_cto.json'):
        try:
            C.update(json.load(open(f, encoding='utf-8')))
        except FileNotFoundError:
            pass
    return C


def yahoo(code):
    mic, tk = code.split(':', 1)
    if mic == 'YF':  # 18/10/2026 : univers elargi, symbole Yahoo direct
        return tk
    if mic not in SUFFIX:
        return None
    if mic == 'XLON':
        tk = tk.rstrip('.')
    return tk + SUFFIX[mic]


def main():
    import sys
    # 18/10/2026 : deux passages separes (PEA le vendredi, compte-titres le jeudi)
    cto = len(sys.argv) > 1 and sys.argv[1] == 'cto'
    sortie = 'candidats_cto_resultats.json' if cto else 'candidats_resultats.json'
    C = charger_listes()
    out = {'genere': time.strftime('%Y-%m-%d %H:%M'), 'listes': {}}
    for liste, codes in C.items():
        if not isinstance(codes, list):
            continue
        if liste.startswith(('cto', 'univers_cto')) != cto:
            continue
        rows = []
        vus_noms = set(NOMS_SCREENER)  # une seule cotation par societe, hors screener
        pea_liste = liste.startswith(('univers_pea', 'pea'))
        for code in codes:
            sym = yahoo(code)
            if not sym:
                rows.append({'code': code, 'err': 'marche non couvert par Yahoo'})
                continue
            if pea_liste and sym in EXCLUS:
                rows.append({'code': code, 'yahoo': sym, 'err': EXCLUS[sym]})
                continue
            for essai in range(4):
              try:
                t = yf.Ticker(sym)
                info = t.info or {}
                if pea_liste:
                    pays = info.get('country')
                    nom_ = (info.get('longName') or info.get('shortName') or '').upper().strip()
                    if pays and pays not in PAYS_PEA:
                        EXCLUS[sym] = f'siege hors UE/EEE ({pays}) : non eligible PEA'
                        rows.append({'code': code, 'yahoo': sym, 'nom': nom_, 'err': EXCLUS[sym]})
                        break
                    cle_ = norm_nom(nom_)
                    if cle_ and (cle_ in vus_noms or cle_.split()[0] in NOMS_UN_MOT):
                        EXCLUS[sym] = 'doublon (autre cotation, ou deja dans le screener)'
                        rows.append({'code': code, 'yahoo': sym, 'nom': nom_, 'err': EXCLUS[sym]})
                        break
                    vus_noms.add(cle_)
                # 18/10/2026 : banques, assurances, foncieres -> grille dediee a venir
                # (la grille 'default' les jugerait mal : ROIC sans objet)
                if (info.get('sector') or '') in ('Financial Services', 'Real Estate'):
                    rows.append({'code': code, 'yahoo': sym, 'nom': info.get('shortName') or info.get('longName'),
                                 'secteur': info.get('sector'), 'qok': False,
                                 'echec': 'financiere/fonciere : grille dediee a venir'})
                    break
                q = compute_quality(t, 'default')
                if 'Too Many Requests' in (q.get('qwhy') or ''):
                    raise RuntimeError('Too Many Requests (bilans)')
                rows.append({'code': code, 'yahoo': sym, 'nom': info.get('shortName') or info.get('longName'),
                             'courtage': courtage(sym),
                             'secteur': info.get('sector'), 'devise': info.get('currency'),
                             'cap_Md': round((info.get('marketCap') or 0) / 1e9, 2),
                             'qok': bool(q.get('qok')), 'echec': q.get('qwhy', ''),
                             'roic': q.get('roic'), 'roicx': q.get('roicx'), 'cash': q.get('fcfc'),
                             'dette_ebitda': q.get('nde'), 'croissance': q.get('cagr')})
                # 13/10/2026 : meme valorisation que le screener, pour les seules valeurs qui passent
                r_ = rows[-1]
                px = info.get('currentPrice') or info.get('regularMarketPrice')
                same = not (info.get('financialCurrency') and info.get('currency')
                            and info.get('financialCurrency') != info.get('currency'))
                roic_v = q.get('roicx') or q.get('roic')
                if r_['qok'] and px and same and roic_v:
                    gs = [x for x in (q.get('cagr'), q.get('nig')) if x is not None]
                    g = max(0.0, min(sum(gs) / len(gs), QV_GMAX * 100)) if gs else 0.0
                    roic_c = min(roic_v, 60.0)
                    v = qarp_value(info.get('forwardEps'), info.get('trailingEps'), None, None, roic_c, g1_override=g / 100)
                    ind = info.get('industry') or ''
                    if any(ind.startswith(x) for x in CYCLIQUES):
                        r_['note'] = f'cyclique ({ind}) : pas de palier, grille dediee a venir'
                        v = None
                    if v:
                        r_['palier1'] = round(v * (1 - MARGES_CANDIDAT[1]), 2)
                        r_['palier2'] = round(v * (1 - MARGES_CANDIDAT[0]), 2)
                        r_['en_zone'] = bool(px <= r_['palier1'])
                    r_.update({'cours': px, 'valeur': round(v, 2) if v else None,
                               'ecart_pct': round((px / v - 1) * 100, 0) if v else None,
                               'rendement_attendu': expected_return(info.get('forwardEps'), info.get('trailingEps'), g, roic_c, px),
                               'croissance_supposee': implied_growth(info.get('forwardEps'), info.get('trailingEps'), roic_c, px),
                               'croissance_retenue': round(g, 1)})
                elif r_['qok'] and not same:
                    r_['note'] = 'comptes dans une autre devise que le cours : valorisation non calculee'
                break
              except Exception as e:
                if 'Too Many Requests' in str(e) and essai < 3:
                    time.sleep(60 * (essai + 1))  # 18/10/2026 : Yahoo limite le debit
                    continue
                rows.append({'code': code, 'yahoo': sym, 'err': str(e)[:120]})
                break
            time.sleep(0.8)
        ok = [r for r in rows if r.get('qok')]
        out['listes'][liste] = {'total': len(rows), 'passent': len(ok),
                                'sans_donnees': sum(1 for r in rows if r.get('err') and not r['err'].startswith(('siege', 'doublon'))),
                                'hors_pea_ou_doublon': sum(1 for r in rows if (r.get('err') or '').startswith(('siege', 'doublon'))),
                                'lignes': rows}
        print(liste, len(rows), 'candidats,', len(ok), 'passent le filtre')
    # 18/10/2026 : entrees / sorties de la grille depuis le passage precedent.
    # Une liste vue pour la premiere fois sert de point de depart (pas d'entrees).
    try:
        prev = json.load(open(sortie, encoding='utf-8')).get('listes', {})
    except Exception:
        prev = {}
    entrees, sorties = [], []
    for liste, bloc in out['listes'].items():
        if liste not in prev:
            continue
        avant = {r['code'] for r in prev[liste].get('lignes', []) if r.get('qok')}
        vus = {r['code'] for r in prev[liste].get('lignes', [])}
        for r in bloc['lignes']:
            cle = {k: r.get(k) for k in ('code', 'nom', 'roic', 'roicx', 'cash', 'croissance', 'ecart_pct', 'echec',
                                         'cours', 'palier1', 'palier2', 'en_zone', 'courtage')}
            cle['liste'] = liste
            if r.get('qok') and r['code'] not in avant:
                entrees.append(cle)
            elif not r.get('qok') and r['code'] in avant and r['code'] in vus and not r.get('err'):
                sorties.append(cle)
    out['entrees'], out['sorties'] = entrees, sorties
    # candidats qui passent la grille ET sont sous leur palier 1 : a etudier en priorite
    out['en_zone'] = [dict({k: r.get(k) for k in ('code', 'nom', 'cours', 'palier1', 'palier2', 'courtage', 'roic', 'cash')}, liste=l)
                      for l, b in out['listes'].items() for r in b['lignes'] if r.get('qok') and r.get('en_zone')]
    print(len(entrees), 'entree(s),', len(sorties), 'sortie(s) depuis le passage precedent')
    json.dump(out, open(sortie, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if not cto:
        json.dump(EXCLUS, open('univers_exclus_pea.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)


if __name__ == '__main__':
    main()
