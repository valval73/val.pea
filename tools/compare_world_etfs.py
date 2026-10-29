"""Compare les ETF MSCI World eligibles au PEA sur la meme periode (sonde ponctuelle).
Resultat ecrit dans probe_sources.json (sortie des sondes)."""
import io, json, contextlib
_buf = io.StringIO()
_ctx = contextlib.redirect_stdout(_buf); _ctx.__enter__()
import yfinance as yf
import pandas as pd

T = {'CW8.PA': 'Amundi MSCI World (CW8)', 'DCAM.PA': 'Amundi PEA Monde (DCAM)', 'WPEA.PA': 'iShares MSCI World PEA (WPEA)'}
px = pd.DataFrame({k: yf.Ticker(k).history(period='5y', auto_adjust=True)['Close'] for k in T})
px.index = px.index.tz_localize(None).normalize()
px = px.groupby(level=0).last()
start = px['DCAM.PA'].first_valid_index()
c = px.loc[start:].dropna()
print('PERIODE COMMUNE', c.index[0].date(), '->', c.index[-1].date(), len(c), 'jours')
base = c / c.iloc[0] * 100
for k, n in T.items():
    print(f'{n:32s} cumul {base[k].iloc[-1]-100:7.2f} %')
def perf(since):
    s = c.loc[since:]
    return {k: round((s[k].iloc[-1] / s[k].iloc[0] - 1) * 100, 2) for k in T}
last = c.index[-1]
print('1 AN   ', perf(last - pd.DateOffset(years=1)))
print('DEPUIS 1/1', perf(pd.Timestamp(last.year, 1, 1)))
print('6 MOIS ', perf(last - pd.DateOffset(months=6)))
r = c.pct_change().dropna()
print('CORRELATION JOURNALIERE\n', r.corr().round(4))
gap = (base['DCAM.PA'] - base['CW8.PA'])
print('ECART DCAM-CW8 (points de base 100): min', round(gap.min(), 2), 'max', round(gap.max(), 2), 'fin', round(gap.iloc[-1], 2))
m = base.resample('ME').last()
print('COURBES MENSUELLES (base 100)\n', m.round(2).to_string())

_ctx.__exit__(None, None, None)
print(_buf.getvalue())
json.dump({'sonde': 'compare_world_etfs', 'texte': _buf.getvalue().splitlines()}, open('probe_sources.json', 'w'), ensure_ascii=False, indent=1)
