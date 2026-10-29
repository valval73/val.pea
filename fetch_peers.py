"""VAL.PEA — comparatif chiffré avec les concurrents (29/10/2026).

Pour chaque action qui a une fiche, on va chercher chaque semaine chez Yahoo
les mêmes ratios pour l'action et pour 3 concurrents cotés, puis on calcule
la médiane des concurrents. Sert à COMPRENDRE (où se situe l'action, le
secteur est-il à la mode ?), jamais à décider : aucune règle d'achat ou de
vente n'utilise ces chiffres.

Sortie : peers.js (const PEERS = {...}), chargé par index.html.
"""
import json, statistics, time, datetime
import yfinance as yf
from tickers import YF_MAP

# Concurrents cotés retenus pour chaque fiche : [symbole Yahoo, nom affiché]
PEER_MAP = {
    'ASML': [['AMAT', 'Applied Materials'], ['LRCX', 'Lam Research'], ['KLAC', 'KLA']],
    'ELIS': [['RTO.L', 'Rentokil'], ['CTAS', 'Cintas'], ['UNF', 'UniFirst']],
    'EL': [['COO', 'Cooper Companies'], ['AFX.DE', 'Carl Zeiss Meditec'], ['SFL.MI', 'Safilo']],
    'GTT': [['TE.PA', 'Technip Energies'], ['WRT1V.HE', 'Wärtsilä'], ['SBMO.AS', 'SBM Offshore']],
    'RMS': [['MC.PA', 'LVMH'], ['CFR.SW', 'Richemont'], ['BC.MI', 'Brunello Cucinelli']],
    'INTERPARFUMS': [['PUIG.MC', 'Puig'], ['IPAR', 'Inter Parfums Inc.'], ['COTY', 'Coty']],
    'AI': [['LIN', 'Linde'], ['APD', 'Air Products'], ['4091.T', 'Nippon Sanso']],
    'LR': [['SU.PA', 'Schneider Electric'], ['HUBB', 'Hubbell'], ['ABBN.SW', 'ABB']],
    'SU': [['ABBN.SW', 'ABB'], ['SIE.DE', 'Siemens'], ['ETN', 'Eaton']],
    'HO': [['BA.L', 'BAE Systems'], ['LDO.MI', 'Leonardo'], ['SAAB-B.ST', 'Saab']],
    'TTE': [['SHEL.L', 'Shell'], ['BP.L', 'BP'], ['ENI.MI', 'Eni']],
    'WKL': [['REL.L', 'RELX'], ['TRI', 'Thomson Reuters'], ['EXPN.L', 'Experian']],
    'MA': [['V', 'Visa'], ['AXP', 'American Express'], ['ADYEN.AS', 'Adyen']],
    'KO': [['PEP', 'PepsiCo'], ['KDP', 'Keurig Dr Pepper'], ['MNST', 'Monster Beverage']],
    'ADBE': [['ADSK', 'Autodesk'], ['INTU', 'Intuit'], ['CRM', 'Salesforce']],
    'AMS': [['SABR', 'Sabre'], ['BKNG', 'Booking'], ['EXPE', 'Expedia']],
    'UMG': [['WMG', 'Warner Music'], ['6758.T', 'Sony'], ['SPOT', 'Spotify']],
    'GOOGL': [['MSFT', 'Microsoft'], ['META', 'Meta'], ['AMZN', 'Amazon']],
    'OR': [['EL', 'Estée Lauder'], ['BEI.DE', 'Beiersdorf'], ['ULVR.L', 'Unilever']],
    'SAF': [['GE', 'GE Aerospace'], ['RR.L', 'Rolls-Royce'], ['MTX.DE', 'MTU Aero']],
    'AIR': [['BA', 'Boeing'], ['ERJ', 'Embraer'], ['SAF.PA', 'Safran']],
    'DSY': [['ADSK', 'Autodesk'], ['PTC', 'PTC'], ['SNPS', 'Synopsys']],
    'IPSEN': [['UCB.BR', 'UCB'], ['REC.MI', 'Recordati'], ['NOVN.SW', 'Novartis']],
    'NRO': [['SOP.PA', 'Sopra Steria'], ['AUB.PA', 'Aubay'], ['CAP.PA', 'Capgemini']],
    'PLNW': [['PTC', 'PTC'], ['MNDY', 'monday.com'], ['DSY.PA', 'Dassault Systèmes']],
    'ITX': [['HM-B.ST', 'H&M'], ['9983.T', 'Fast Retailing'], ['NXT.L', 'Next']],
    'RAA': [['MIDD', 'Middleby'], ['ELUX-B.ST', 'Electrolux'], ['WHR', 'Whirlpool']],
    'NEM': [['ADSK', 'Autodesk'], ['BSY', 'Bentley Systems'], ['DSY.PA', 'Dassault Systèmes']],
    'MONC': [['BC.MI', 'Brunello Cucinelli'], ['CFR.SW', 'Richemont'], ['MC.PA', 'LVMH']],
    'RHM': [['LDO.MI', 'Leonardo'], ['BA.L', 'BAE Systems'], ['SAAB-B.ST', 'Saab']],
    'ATCO': [['IR', 'Ingersoll Rand'], ['SAND.ST', 'Sandvik'], ['6273.T', 'SMC']],
    'DG': [['FGR.PA', 'Eiffage'], ['ACS.MC', 'ACS'], ['EN.PA', 'Bouygues']],
}

FIELDS = ('pe', 'fpe', 'eveb', 'om', 'roe', 'revg', 'pfcf')
_cache = {}


def ratios(sym):
    if sym in _cache:
        return _cache[sym]
    out = {}
    try:
        i = yf.Ticker(sym).info or {}
        pct = lambda v: round(v * 100, 1) if isinstance(v, (int, float)) else None
        num = lambda v: round(v, 1) if isinstance(v, (int, float)) and 0 < v < 500 else None
        out = {
            'pe': num(i.get('trailingPE')),
            'fpe': num(i.get('forwardPE')),
            'eveb': num(i.get('enterpriseToEbitda')),
            'om': pct(i.get('operatingMargins')),
            'roe': pct(i.get('returnOnEquity')),
            'revg': pct(i.get('revenueGrowth')),
        }
        mc, fcf = i.get('marketCap'), i.get('freeCashflow')
        out['pfcf'] = round(mc / fcf, 1) if mc and fcf and fcf > 0 and mc / fcf < 500 else None
    except Exception as e:
        print('  erreur', sym, e)
    _cache[sym] = out
    time.sleep(0.4)
    return out


def median(vals):
    v = [x for x in vals if isinstance(x, (int, float))]
    return round(statistics.median(v), 1) if len(v) >= 2 else None


def main():
    res = {}
    for t, peers in PEER_MAP.items():
        sym = YF_MAP.get(t)
        if not sym:
            continue
        print(t, sym)
        rows = [dict(n=n, s=s, **ratios(s)) for s, n in peers]
        res[t] = {
            'self': ratios(sym),
            'peers': rows,
            'med': {f: median([r.get(f) for r in rows]) for f in FIELDS},
        }
    payload = {'date': datetime.date.today().isoformat(), 'groups': res}
    with open('peers.js', 'w', encoding='utf-8') as f:
        f.write('// Généré par fetch_peers.py — ne pas éditer à la main.\n')
        f.write('const PEERS = ' + json.dumps(payload, ensure_ascii=False) + ';\n')
    ok = sum(1 for g in res.values() if g['self'].get('pe') or g['self'].get('eveb'))
    print(f'{len(res)} fiches, {ok} avec ratios')


if __name__ == '__main__':
    main()
