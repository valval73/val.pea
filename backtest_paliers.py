"""
VAL.PEA -- Test des deux paliers sur le passe (08/10/2026).

Question testee : pour les MEMES actions, attendre les paliers fait-il mieux
que (A) tout mettre chaque mois sur l'ETF Monde, ou (B) acheter ces actions
chaque mois sans regarder le prix ?

A chaque fin de mois, avec seulement les comptes deja publies a cette date
(publication supposee 75 jours apres la cloture) :
  valeur centrale = meme modele que le screener (qarp_value, 8,5 %/an),
  croissance = croissance du chiffre d'affaires publiee jusque-la (0-12 %) ;
  palier 1 = valeur x (1 - decote haute), palier 2 = valeur x (1 - 20/30/40 %).
Versement mensuel de 1 000 : palier 2 -> l'action monte jusqu'a 5 % du
portefeuille ; palier 1 -> jusqu'a 2,5 % ; le reste va sur l'ETF Monde.
Aucune vente (on garde tout jusqu'a la fin).

BIAIS CONNUS (a lire avant de conclure) :
  - univers = les valeurs de qualite D'AUJOURD'HUI (biais du survivant :
    flatte les strategies B et C) ;
  - rentabilite du capital et incertitude = valeurs d'aujourd'hui ;
  - Yahoo ne donne que ~4-5 comptes annuels : test court (depuis 2023 environ),
    sans le krach de 2020 ;
  - cours ajustes des dividendes (dividendes reinvestis), sans frais ni impots.
Resultat ecrit dans backtest_paliers.json.
"""
import json, math, sys
from datetime import timedelta
import pandas as pd
import yfinance as yf
from tickers import YF_MAP
from fetch_fundamentals import qarp_value, QV_GMAX
from moat import UNCERTAINTY, MARGIN

ETF = 'EUNL.DE'           # iShares Core MSCI World (EUR)
Z2M = {'faible': 0.20, 'moyenne': 0.30, 'elevee': 0.40}
LAG = 75                  # jours entre cloture et publication
MONTHLY = 1000.0


def universe():
    import re
    t = open('data.js', encoding='utf-8').read().split('const ETF')[0]
    out = {}
    for b in re.split(r"\{ticker:'", t)[1:]:
        tk = b.split("'")[0]
        q = re.search(r'\bqok:(true|false)', b)
        r = re.search(r'\broicx:([0-9.]+)', b) or re.search(r'\broic:([0-9.]+)', b)
        if q and q.group(1) == 'true' and r and tk in YF_MAP:
            out[tk] = float(r.group(1))
    return out


def row(df, *names):
    for n in names:
        if df is not None and n in df.index:
            return df.loc[n]
    return None


def valuations(tk, roic):
    """Serie mensuelle (date -> (palier1, palier2, valeur)) a partir des comptes publies."""
    t = yf.Ticker(YF_MAP[tk])
    info = t.info or {}
    if info.get('financialCurrency') and info.get('currency') and info['financialCurrency'] != info['currency']:
        return None, 'devise des comptes differente du cours'
    fin = t.income_stmt
    eps = row(fin, 'Diluted EPS', 'Basic EPS')
    rev = row(fin, 'Total Revenue', 'Operating Revenue')
    if eps is None or rev is None:
        return None, 'comptes incomplets'
    years = sorted([c for c in fin.columns if pd.notna(eps.get(c)) and pd.notna(rev.get(c))])
    if len(years) < 2:
        return None, 'moins de 2 ans de comptes'
    unc = UNCERTAINTY.get(tk) or 'moyenne'
    hi = MARGIN.get(unc, (0.25, 0.15))[1]
    pts = []
    for i in range(1, len(years)):
        y0, y1 = years[0], years[i]
        n = (y1 - y0).days / 365.25
        r0, r1 = float(rev[y0]), float(rev[y1])
        g = ((r1 / r0) ** (1 / n) - 1) * 100 if r0 > 0 and r1 > 0 and n > 0 else 0.0
        g = max(0.0, min(g, QV_GMAX * 100))
        e = float(eps[y1])
        if e <= 0:
            continue
        v = qarp_value(None, e, None, None, roic, g1_override=g / 100)
        if v:
            pts.append((pd.Timestamp(y1).tz_localize(None) + timedelta(days=LAG), v * (1 - hi), v * (1 - Z2M[unc]), v, round(g, 1)))
    return pts, None


def main():
    U = universe()
    print('Univers :', len(U), 'valeurs de qualite (aujourd hui)')
    closes, vals, skipped = {}, {}, {}
    for tk, roic in U.items():
        try:
            pts, why = valuations(tk, roic)
            if not pts:
                skipped[tk] = why or 'aucune valeur'
                continue
            h = yf.Ticker(YF_MAP[tk]).history(period='6y', interval='1mo', auto_adjust=True)['Close']
            h.index = h.index.tz_localize(None)
            closes[tk], vals[tk] = h, pts
        except Exception as ex:
            skipped[tk] = str(ex)[:80]
    etf = yf.Ticker(ETF).history(period='6y', interval='1mo', auto_adjust=True)['Close']
    etf.index = etf.index.tz_localize(None)
    start = min(p[0][0] for p in vals.values())
    months = [d for d in etf.index if d >= start]
    print('Periode :', months[0].date(), '->', months[-1].date(), len(months), 'mois')

    def px(tk, d):
        s = closes[tk][closes[tk].index <= d]
        return float(s.iloc[-1]) if len(s) else None

    def cur_val(tk, d):
        L = [p for p in vals[tk] if p[0] <= d]
        return L[-1] if L else None

    # A : ETF seul ; B : actions chaque mois (parts egales) ; C : paliers + ETF
    A, B, C_etf, C = 0.0, {}, 0.0, {}
    events, invested = [], 0.0
    for d in months:
        pe = float(etf[etf.index <= d].iloc[-1])
        invested += MONTHLY
        A += MONTHLY / pe
        live = [tk for tk in closes if px(tk, d) and cur_val(tk, d)]
        for tk in live:
            B[tk] = B.get(tk, 0.0) + MONTHLY / len(live) / px(tk, d)
        # valeur du portefeuille C avant versement
        tot = C_etf * pe + sum(q * px(tk, d) for tk, q in C.items()) + MONTHLY
        cash = MONTHLY
        cands = []
        for tk in live:
            p, v = px(tk, d), cur_val(tk, d)
            if p <= v[2]:
                cands.append((0, p / v[3], tk, 0.05, 2))
            elif p <= v[1]:
                cands.append((1, p / v[3], tk, 0.025, 1))
        for _, _, tk, cap, lvl in sorted(cands):
            p = px(tk, d)
            room = cap * tot - C.get(tk, 0.0) * p
            amt = min(cash, max(0.0, room))
            if amt > 1:
                C[tk] = C.get(tk, 0.0) + amt / p
                cash -= amt
                events.append({'date': str(d.date()), 'ticker': tk, 'palier': lvl, 'cours': round(p, 2),
                               'valeur': round(cur_val(tk, d)[3], 2), 'montant': round(amt)})
        C_etf += cash / pe
    dl = months[-1]
    pe = float(etf.iloc[-1])
    vA = A * pe
    vB = sum(q * px(tk, dl) for tk, q in B.items())
    vC = C_etf * pe + sum(q * px(tk, dl) for tk, q in C.items())

    def irr(final):
        # rendement annuel (taux interne) de versements mensuels constants
        n = len(months)
        lo, hi = -0.5, 1.0
        for _ in range(80):
            m = (lo + hi) / 2
            r = (1 + m) ** (1 / 12) - 1
            fv = sum(MONTHLY * (1 + r) ** (n - i) for i in range(n))
            lo, hi = (m, hi) if fv < final else (lo, m)
        return round((lo + hi) / 2 * 100, 1)

    # resultat de chaque achat au palier, a ce jour
    for e in events:
        e['perf_a_ce_jour'] = round((px(e['ticker'], dl) / e['cours'] - 1) * 100, 1)
        e['etf_meme_periode'] = round((pe / float(etf[etf.index <= pd.Timestamp(e['date'])].iloc[-1]) - 1) * 100, 1)
    n1 = sum(1 for e in events if e['palier'] == 1)
    n2 = sum(1 for e in events if e['palier'] == 2)
    beat = sum(1 for e in events if e['perf_a_ce_jour'] > e['etf_meme_periode'])
    out = {
        'periode': [str(months[0].date()), str(dl.date())], 'mois': len(months), 'verse': invested,
        'univers': sorted(closes), 'exclues': skipped,
        'A_etf_seul': {'valeur': round(vA), 'rendement_annuel': irr(vA)},
        'B_actions_chaque_mois': {'valeur': round(vB), 'rendement_annuel': irr(vB)},
        'C_paliers_plus_etf': {'valeur': round(vC), 'rendement_annuel': irr(vC),
                               'part_actions_finale_pct': round((vC - C_etf * pe) / vC * 100, 1)},
        'achats': {'palier1': n1, 'palier2': n2, 'battent_etf': beat, 'total': len(events)},
        'evenements': events[-60:],
        'biais': ['univers = qualite d aujourd hui (survivant)', 'ROIC et incertitude d aujourd hui',
                  'test court : comptes Yahoo limites a 4-5 ans', 'sans frais ni impots'],
    }
    json.dump(out, open('backtest_paliers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps({k: out[k] for k in ('periode', 'A_etf_seul', 'B_actions_chaque_mois', 'C_paliers_plus_etf', 'achats')}, indent=1))


if __name__ == '__main__':
    main()
