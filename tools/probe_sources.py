"""Performances des ETF eligibles PEA (yfinance, cours ajustes, en euros) -> etf_perf.json"""
import json, yfinance as yf, pandas as pd
T = {'CW8.PA': 'Amundi MSCI World (CW8)', 'DCAM.PA': 'Amundi PEA Monde (DCAM)', 'WPEA.PA': 'iShares MSCI World PEA (WPEA)',
     'PSP5.PA': 'Amundi PEA S&P 500 (PSP5)', 'ESE.PA': 'BNP Easy S&P 500 (ESE)', 'PE500.PA': 'Amundi PEA S&P 500 ESG (PE500)',
     'PUST.PA': 'Amundi PEA Nasdaq-100 (PUST)', 'PCEU.PA': 'Amundi PEA MSCI Europe (PCEU)', 'MEUD.PA': 'Amundi Stoxx Europe 600 (MEUD)',
     'PAEEM.PA': 'Amundi PEA Emergents ESG (PAEEM)', 'PAASI.PA': 'Amundi PEA Asie emergente (PAASI)', 'GPEA.PA': 'Amundi PEA Global ACWI (GPEA)',
     'C40.PA': 'Amundi CAC 40 (C40)'}
out = {}
for s, n in T.items():
    try:
        h = yf.Ticker(s).history(period='max', interval='1d', auto_adjust=True)['Close'].dropna()
        h.index = h.index.tz_localize(None)
        last = h.index[-1]
        r = {'nom': n, 'debut': str(h.index[0].date()), 'dernier': round(float(h.iloc[-1]), 3)}
        for y in (1, 3, 5, 10):
            past = h[h.index <= last - pd.DateOffset(years=y)]
            if len(past):
                r[f'{y}a'] = round(((float(h.iloc[-1]) / float(past.iloc[-1])) ** (1 / y) - 1) * 100, 1)
        # pire baisse sur 5 ans
        h5 = h[h.index >= last - pd.DateOffset(years=5)]
        r['pire_baisse_5a'] = round(float((h5 / h5.cummax() - 1).min()) * 100, 1)
        out[s] = r
    except Exception as e:
        out[s] = {'nom': n, 'erreur': str(e)[:80]}
json.dump(out, open('probe_sources.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False))
