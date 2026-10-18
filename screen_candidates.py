"""
VAL.PEA -- Passe la banque de candidats (candidats.json) dans le MEME filtre
qualite que le screener (compute_quality), sans les ajouter au site.
Sortie : candidats_resultats.json (qok, criteres en echec, chiffres cles).
Les chiffres viennent de Yahoo ; rien n'est repris d'un autre screener.
Lancement manuel (GitHub Actions > Candidats > Run workflow).
"""
import json, time
import yfinance as yf
from fetch_fundamentals import compute_quality, qarp_value, expected_return, implied_growth, QV_GMAX

# code de marche (MIC) -> suffixe Yahoo
SUFFIX = {'XPAR': '.PA', 'XETR': '.DE', 'XFRA': '.F', 'XMIL': '.MI', 'XMAD': '.MC',
          'XAMS': '.AS', 'XBRU': '.BR', 'XLIS': '.LS', 'XSTO': '.ST', 'XOSL': '.OL',
          'XHEL': '.HE', 'XCSE': '.CO', 'XWBO': '.VI', 'XWAR': '.WA', 'XBUD': '.BD',
          'XICE': '.IC', 'XDUB': '.IR', 'XBSE': '.RO', 'XNYS': '', 'XNGS': '',
          'XLON': '.L', 'XSWX': '.SW', 'XTSE': '.TO',
          'ASEX': '.AT', 'XSAT': '.ST', 'XDUS': '.DU', 'XPRA': '.PR'}


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
    C = json.load(open('candidats.json', encoding='utf-8'))
    out = {'genere': time.strftime('%Y-%m-%d %H:%M'), 'listes': {}}
    for liste, codes in C.items():
        if not isinstance(codes, list):
            continue
        rows = []
        for code in codes:
            sym = yahoo(code)
            if not sym:
                rows.append({'code': code, 'err': 'marche non couvert par Yahoo'})
                continue
            try:
                t = yf.Ticker(sym)
                info = t.info or {}
                # 18/10/2026 : banques, assurances, foncieres -> grille dediee a venir
                # (la grille 'default' les jugerait mal : ROIC sans objet)
                if (info.get('sector') or '') in ('Financial Services', 'Real Estate'):
                    rows.append({'code': code, 'yahoo': sym, 'nom': info.get('shortName') or info.get('longName'),
                                 'secteur': info.get('sector'), 'qok': False,
                                 'echec': 'financiere/fonciere : grille dediee a venir'})
                    continue
                q = compute_quality(t, 'default')
                rows.append({'code': code, 'yahoo': sym, 'nom': info.get('shortName') or info.get('longName'),
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
                    r_.update({'cours': px, 'valeur': round(v, 2) if v else None,
                               'ecart_pct': round((px / v - 1) * 100, 0) if v else None,
                               'rendement_attendu': expected_return(info.get('forwardEps'), info.get('trailingEps'), g, roic_c, px),
                               'croissance_supposee': implied_growth(info.get('forwardEps'), info.get('trailingEps'), roic_c, px),
                               'croissance_retenue': round(g, 1)})
                elif r_['qok'] and not same:
                    r_['note'] = 'comptes dans une autre devise que le cours : valorisation non calculee'
            except Exception as e:
                rows.append({'code': code, 'yahoo': sym, 'err': str(e)[:120]})
            time.sleep(0.4)
        ok = [r for r in rows if r.get('qok')]
        out['listes'][liste] = {'total': len(rows), 'passent': len(ok),
                                'sans_donnees': sum(1 for r in rows if r.get('err')), 'lignes': rows}
        print(liste, len(rows), 'candidats,', len(ok), 'passent le filtre')
    json.dump(out, open('candidats_resultats.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
