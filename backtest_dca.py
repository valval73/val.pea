"""
VAL.PEA -- Test du DCA action par action (17/11/2026).

Question : pour chaque action de l'univers, verser 100 EUR chaque mois sur
l'action fait-il mieux que verser 100 EUR chaque mois sur l'ETF Monde ?
Et renforcer quand l'action perd 30 % sous son prix de revient aide-t-il ?

Strategies (versement le 1er de chaque mois, cours ajustes des dividendes,
convertis en EUR, sans frais ni impots, aucune vente) :
  DCA_ACTION : 100 EUR/mois sur l'action
  DCA_ETF    : 100 EUR/mois sur l'ETF Monde (EUNL.DE)
  RENFORT    : DCA_ACTION + 100 EUR de plus chaque mois ou le cours est
               <= 70 % du prix de revient
Mesures : TRI (rendement annuel de l'argent verse), pire moins-value latente
(valeur / verse - 1) ; fenetre 10 ans et fenetres glissantes de 5 ans.

BIAIS : univers = actions suivies AUJOURD'HUI (biais du survivant, flatte
DCA_ACTION et RENFORT). Resultat : backtests/dca_univers.json
"""
import json, os
import numpy as np
import pandas as pd
import yfinance as yf
from tickers import YF_MAP

START, END = '2016-11-01', '2026-11-02'
ETF = 'EUNL.DE'
M = 100.0
FX = {'.ST': 'SEK', '.CO': 'DKK', '.OL': 'NOK', '.SW': 'CHF', '.L': 'GBP',
      '.WA': 'PLN', '.PR': 'CZK', '.BD': 'HUF'}


def ccy(t):
    for s, c in FX.items():
        if t.endswith(s):
            return c
    return 'USD' if '.' not in t else 'EUR'


def monthly(tks):
    d = yf.download(tks, start=START, end=END, interval='1mo', auto_adjust=True,
                    progress=False, group_by='column', threads=True)['Close']
    if isinstance(d, pd.Series):
        d = d.to_frame(tks[0])
    return d


def irr(flows):
    # flows mensuels, renvoie un taux annuel
    f = np.array(flows, dtype=float)
    lo, hi = -0.99, 1.0
    npv = lambda r: sum(x / (1 + r) ** i for i, x in enumerate(f))
    if npv(lo) * npv(hi) > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(lo) * npv(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return round(((1 + mid) ** 12 - 1) * 100, 1)


def run(p, extra=False):
    units = inv = 0.0
    flows, worst = [], 0.0
    for px in p:
        put = M
        if extra and units > 0 and px <= 0.7 * (inv / units):
            put += M
        units += put / px
        inv += put
        flows.append(-put)
        worst = min(worst, units * px / inv - 1)
    val = units * p[-1]
    flows[-1] += val
    return {'tri': irr(flows), 'verse': round(inv), 'valeur': round(val),
            'pire_moins_value': round(worst * 100, 1)}


def main():
    yfs = sorted({v for v in YF_MAP.values() if v})
    px = monthly(yfs + [ETF])
    need = sorted({ccy(t) for t in yfs} - {'EUR'})
    fx = monthly([f'EUR{c}=X' for c in need]) if need else pd.DataFrame()
    etf = px[ETF].dropna()
    res, wins10, diffs10, win5 = {}, 0, [], []
    for t in yfs:
        if t not in px:
            continue
        s = px[t]
        c = ccy(t)
        if c != 'EUR':
            r = fx.get(f'EUR{c}=X')
            if r is None:
                continue
            s = s / r.reindex(s.index).ffill()
            if c == 'GBP':
                s = s / 100.0
        df = pd.concat([s, etf], axis=1, keys=['a', 'e']).dropna()
        if len(df) < 60:
            continue
        a, e = df['a'].values, df['e'].values
        full = len(df) >= 118
        out = {'mois': len(df), 'fenetre_10_ans': full,
               'DCA_ACTION': run(a), 'DCA_ETF': run(e), 'RENFORT': run(a, True)}
        # fenetres glissantes de 5 ans (60 mois), depart chaque mois
        w = []
        for i in range(0, len(df) - 59, 3):
            ta, te = run(a[i:i + 60])['tri'], run(e[i:i + 60])['tri']
            if ta is not None and te is not None:
                w.append(ta > te)
        out['fenetres5_battent_etf_pct'] = round(100 * sum(w) / len(w)) if w else None
        res[t] = out
        if full and out['DCA_ACTION']['tri'] is not None:
            d = out['DCA_ACTION']['tri'] - out['DCA_ETF']['tri']
            diffs10.append(d)
            wins10 += d > 0
    n = len(diffs10)
    agg = {
        'periode': [START, END], 'versement_mensuel': M, 'etf': ETF,
        'actions_10_ans': n,
        'pct_dca_action_bat_etf_10_ans': round(100 * wins10 / n) if n else None,
        'ecart_tri_median_points': round(float(np.median(diffs10)), 1) if n else None,
        'biais': ["univers d'aujourd'hui (survivant)", 'sans frais ni impots',
                  'dividendes reinvestis (cours ajustes)'],
    }
    os.makedirs('backtests', exist_ok=True)
    json.dump({'synthese': agg, 'actions': res},
              open('backtests/dca_univers.json', 'w'), indent=1)
    print(json.dumps(agg, indent=1))


if __name__ == '__main__':
    main()
