"""19/10/2026 : quelles lignes de flux de tresorerie Yahoo donne-t-il pour les loyers (IFRS 16) ?"""
import json, yfinance as yf
out = {}
for s in ['AXFO.ST', 'ITX.MC', 'LPP.WA', 'MC.PA', 'COST', 'WKL.AS', 'ELIS.PA']:
    try:
        cf = yf.Ticker(s).cashflow
        rows = {r: [None if v != v else round(float(v) / 1e6, 1) for v in cf.loc[r].values[:4]] for r in cf.index
                if any(k in r.lower() for k in ('lease', 'debt', 'free cash', 'operating cash', 'capital expenditure', 'financing'))}
        out[s] = {'years': [str(c)[:10] for c in cf.columns[:4]], 'rows': rows}
    except Exception as e:
        out[s] = str(e)
json.dump(out, open('probe_sources.json', 'w'), indent=1)
print(json.dumps(out, indent=1)[:6000])
