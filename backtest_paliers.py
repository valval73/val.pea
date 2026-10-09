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
  - filtres du screener appliques (chute, regularite, moat d'aujourd'hui) ;
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
from fetch_fundamentals import qarp_value, QV_GMAX, effective_growth
from moat import UNCERTAINTY, MARGIN, MOAT, MOAT_MIN_BUY

ETF = 'EUNL.DE'           # iShares Core MSCI World (EUR)
EUR_IDX = 'MEUD.PA'       # Amundi Stoxx Europe 600 (capitalisant) : reference europeenne
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


def xbrl_history(tk):
    """Comptes officiels (filings.xbrl.org) : {annee: (BPA, chiffre d'affaires)}.
    Les rapports europeens existent depuis l'exercice 2020 : ils allongent le
    test d'environ 2 ans (dont la baisse de 2022) par rapport a Yahoo seul."""
    try:
        import official_accounts as OA
        lei = (json.load(open('lei_map.json', encoding='utf-8')).get(tk) or {}).get('lei')
        if not lei:
            return {}
        fl = OA.get(f'/api/entities/{lei}/filings?page[size]=50') or {}
        out = {}
        for a in sorted([x.get('attributes', {}) for x in fl.get('data', [])], key=lambda x: x.get('period_end') or ''):
            if not a.get('json_url'):
                continue
            j = OA.get(a['json_url'])
            if not j:
                continue
            facts = j.get('facts', {})
            rev = OA.year_values(facts, OA.REV)
            eps = OA.year_values(facts, ('ifrs-full:DilutedEarningsLossPerShare', 'ifrs-full:BasicEarningsLossPerShare'))
            for y in set(rev) & set(eps):
                out[int(y)] = (eps[y][0], rev[y][0])
        return out
    except Exception as ex:
        print('  XBRL', tk, str(ex)[:60])
        return {}


def valuations(tk, roic):
    """Serie (date de publication -> paliers, valeur) a partir des comptes publies :
    Yahoo (4-5 ans) complete par les comptes officiels plus anciens."""
    t = yf.Ticker(YF_MAP[tk])
    info = t.info or {}
    if info.get('financialCurrency') and info.get('currency') and info['financialCurrency'] != info['currency']:
        return None, 'devise des comptes differente du cours'
    fin = t.income_stmt
    eps = row(fin, 'Diluted EPS', 'Basic EPS')
    rev = row(fin, 'Total Revenue', 'Operating Revenue')
    data = {}   # annee -> (date de cloture, bpa, ca)
    for y, (e_, r_) in xbrl_history(tk).items():
        data[y] = (pd.Timestamp(year=y, month=12, day=31), e_, r_)
    if eps is not None and rev is not None:
        for c in fin.columns:
            if pd.notna(eps.get(c)) and pd.notna(rev.get(c)):
                d = pd.Timestamp(c).tz_localize(None)
                data[d.year] = (d, float(eps[c]), float(rev[c]))
    ys = sorted(data)
    if len(ys) < 2:
        return None, 'moins de 2 ans de comptes'
    unc = UNCERTAINTY.get(tk) or 'moyenne'
    hi = MARGIN.get(unc, (0.25, 0.15))[1]
    moat_s = (MOAT.get(tk) or (None,))[0]
    pts = []
    for i in range(1, len(ys)):
        d0, _, r0 = data[ys[0]]
        d1, e, r1 = data[ys[i]]
        n = (d1 - d0).days / 365.25
        g = ((r1 / r0) ** (1 / n) - 1) * 100 if r0 > 0 and r1 > 0 and n > 0 else 0.0
        g, _cap = effective_growth(max(0.0, g), roic, moat_s, False)
        if e <= 0:
            continue
        v = qarp_value(None, e, None, None, roic, g1_override=g / 100)
        rs = [data[y][2] for y in ys[:i + 1]]
        ups = sum(1 for a_, b_ in zip(rs, rs[1:]) if b_ > a_)
        regular = ups >= len(rs) - 2 if len(rs) >= 3 else True
        if v:
            pts.append((d1 + timedelta(days=LAG), v * (1 - hi), v * (1 - Z2M[unc]), v, round(g, 1), regular))
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
    try:
        eu = yf.Ticker(EUR_IDX).history(period='6y', interval='1mo', auto_adjust=True)['Close']
        eu.index = eu.index.tz_localize(None)
    except Exception:
        eu = None
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
    A, B, C_etf, C, D_ = 0.0, {}, 0.0, {}, 0.0
    events, invested, blocked = [], 0.0, {}
    for d in months:
        pe = float(etf[etf.index <= d].iloc[-1])
        invested += MONTHLY
        A += MONTHLY / pe
        if eu is not None and len(eu[eu.index <= d]):
            D_ += MONTHLY / float(eu[eu.index <= d].iloc[-1])
        live = [tk for tk in closes if px(tk, d) and cur_val(tk, d)]
        for tk in live:
            B[tk] = B.get(tk, 0.0) + MONTHLY / len(live) / px(tk, d)
        # valeur du portefeuille C avant versement
        tot = C_etf * pe + sum(q * px(tk, d) for tk, q in C.items()) + MONTHLY
        cash = MONTHLY
        cands = []
        for tk in live:
            p, v = px(tk, d), cur_val(tk, d)
            # memes filtres que le screener : chute > 35 % sur 12 mois, croissance
            # irreguliere, moat < 3 (moat = note d'aujourd'hui)
            hist12 = closes[tk][(closes[tk].index <= d) & (closes[tk].index > d - pd.Timedelta(days=366))]
            knife = len(hist12) and p < 0.65 * float(hist12.max())
            weak = (MOAT.get(tk, (0,))[0] or 0) < MOAT_MIN_BUY
            if knife or weak or not v[5]:
                blocked[tk] = blocked.get(tk, 0) + 1
                continue
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
    vD = D_ * float(eu.iloc[-1]) if eu is not None and D_ else None
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
        'D_europe_stoxx600': {'valeur': round(vD), 'rendement_annuel': irr(vD)} if vD else None,
        'B_actions_chaque_mois': {'valeur': round(vB), 'rendement_annuel': irr(vB)},
        'C_paliers_plus_etf': {'valeur': round(vC), 'rendement_annuel': irr(vC),
                               'part_actions_finale_pct': round((vC - C_etf * pe) / vC * 100, 1)},
        'achats': {'palier1': n1, 'palier2': n2, 'battent_etf': beat, 'total': len(events)},
        'bloques_par_filtres': blocked,
        'evenements': events[-60:],
        'biais': ['actions = celles de qualité aujourd’hui (biais du survivant, flatte les actions)',
                  'rentabilité, moat et incertitude d’aujourd’hui',
                  'comptes : Yahoo + rapports officiels européens (depuis 2020) ; pas de krach 2020 dans le test',
                  'sans frais ni impôts'],
    }
    json.dump(out, open('backtest_paliers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps({k: out[k] for k in ('periode', 'A_etf_seul', 'D_europe_stoxx600', 'B_actions_chaque_mois', 'C_paliers_plus_etf', 'achats')}, indent=1))


if __name__ == '__main__':
    main()
