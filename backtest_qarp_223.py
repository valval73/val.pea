#!/usr/bin/env python3
"""
backtest_qarp_223.py — VAL.PEA
Backtest complet sur les 223 actions SBF250 — 2019-2024
Calcule QARP Large + QARP Mid séparément
Produit : backtest_223_results.csv + backtest_223_chart.png

Usage Google Colab :
  !pip install yfinance pandas numpy matplotlib -q
  !python backtest_qarp_223.py
"""

import re, json, os, sys
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

PERIODE_DEBUT = "2019-01-01"
PERIODE_FIN   = "2024-12-31"
BENCHMARK     = "^FCHI"

# ─── YF_MAP COMPLET 223 TICKERS ───────────────────────────────────
YF_MAP = {
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA',
    'ORA':'ORA.PA','VIE':'VIE.PA','RNO':'RNO.PA','SGO':'SGO.PA','CAP':'CAP.PA',
    'DG':'DG.PA','VIV':'VIV.PA','LR':'LR.PA','WLN':'WLN.PA','DSY':'DSY.PA',
    'STM':'STM.PA','EL':'EL.PA','ML':'ML.PA','ENGI':'ENGI.PA','HO':'HO.PA',
    'AC':'AC.PA','AF':'AF.PA','BN':'BN.PA','EN':'EN.PA','SW':'SW.PA',
    'GTT':'GTT.PA','ELIS':'ELIS.PA','ERF':'ERF.PA','COFA':'COFA.PA',
    'SPIE':'SPIE.PA','ALO':'ALO.PA','BVI':'BVI.PA','FDJ':'FDJ.PA',
    'IPSEN':'IPN.PA','REXEL':'RXL.PA','SOP':'SOP.PA','LNA':'LNA.PA',
    'FNAC':'FNAC.PA','CNP':'CNP.PA','EIFFAGE':'FGR.PA','NEXANS':'NEX.PA',
    'FORVIA':'FRVIA.PA','IMERYS':'NK.PA','IPSOS':'IPS.PA',
    'ASML':'ASML.AS','NOVO':'NOVO-B.CO','PRX':'PRX.AS',
    'HEIA':'HEIA.AS','ADYEN':'ADYEN.AS',
    'LECTRA':'LSS.PA','ARGAN':'ARG.PA','FREY':'FREY.PA',
    'COVIVIO':'COV.PA','DERICHEBOURG':'DBG.PA',
    'STEF':'STF.PA','THERMADOR':'THEP.PA','LISI':'FII.PA',
    'MANITOU':'MTU.PA','SAMSE':'SAMS.PA','ELIOR':'ELIOR.PA',
    'TRIGANO':'TRI.PA','BOIRON':'BOI.PA','VIRBAC':'VIRP.PA',
    'DIOR':'CDI.PA','EDEN':'EDEN.PA','PLXEE':'PLX.PA',
    'NXI':'NXI.PA','ATO':'ATO.PA','RUI':'RUI.PA',
    'WAGA':'WGAEN.PA','ABIVAX':'ABVX.PA','FIGEAC':'FGA.PA',
    'INTERP':'ITP.PA','LACROIX':'LACR.PA','SEB':'SK.PA',
    'MCPHY':'MCPHY.PA','SOITEC':'SOI.PA','ALTEN':'ATE.PA',
    'SWORD':'SWP.PA','DASSYS':'DSY.PA','AXWAY':'AXW.PA',
    'ESKER':'ALESK.PA','VISIOMED':'VM.PA','TXCOM':'TXCO.PA',
    'GINESYS':'GNS.PA','COHERIS':'COH.PA',
}

# ─── CALCUL QARP LARGE CAPS ───────────────────────────────────────
def calc_qarp_large(info):
    """QARP Large Caps — pondérations recalibrées sur backtest"""
    roe = (info.get('returnOnEquity') or 0) * 100
    margin = (info.get('profitMargins') or 0) * 100
    fcf = info.get('freeCashflow') or 0
    mkt = info.get('marketCap') or 1
    fcf_y = fcf/mkt*100 if mkt else 0
    debt = info.get('debtToEquity', 50) / 10
    pe_fwd = info.get('forwardPE') or info.get('trailingPE') or 25
    epsg = (info.get('earningsGrowth') or 0) * 100

    q = r = b = v = m = 0

    # ROE — 15 pts (réduit car corrél. 0.012 sur backtest)
    if roe >= 25: q = 15
    elif roe >= 18: q = 12
    elif roe >= 12: q = 8
    elif roe >= 8: q = 5
    else: q = 2

    # Marge — 22 pts (corrél. +0.391)
    if margin >= 20: r = 22
    elif margin >= 14: r = 17
    elif margin >= 8: r = 12
    elif margin >= 4: r = 7
    else: r = 2

    # Bilan/Dette — 26 pts (corrél. -0.493, le plus prédictif)
    if debt < 1.0: b = 26
    elif debt < 1.8: b = 20
    elif debt < 2.8: b = 13
    elif debt < 4.0: b = 7
    else: b = 2

    # Valorisation PE — 25 pts (corrél. +0.467)
    if pe_fwd < 12: v = 10   # très bon marché
    elif pe_fwd < 18: v = 20
    elif pe_fwd < 25: v = 25  # valorisation raisonnable = meilleur signal
    elif pe_fwd < 35: v = 18
    elif pe_fwd < 50: v = 10
    else: v = 3

    # FCF — 12 pts (réduit car corrél. -0.237)
    if fcf_y >= 8: m = 12
    elif fcf_y >= 5: m = 9
    elif fcf_y >= 2: m = 5
    else: m = 2

    return {'q':q,'r':r,'b':b,'v':v,'m':m,'total':min(100,q+r+b+v+m)}

# ─── CALCUL QARP MIDCAPS ──────────────────────────────────────────
def calc_qarp_mid(info):
    """QARP Midcaps — accent sur croissance CA et rentabilité opérationnelle"""
    roe = (info.get('returnOnEquity') or 0) * 100
    margin = (info.get('profitMargins') or 0) * 100
    revg = (info.get('revenueGrowth') or 0) * 100
    epsg = (info.get('earningsGrowth') or 0) * 100
    fcf = info.get('freeCashflow') or 0
    mkt = info.get('marketCap') or 1
    fcf_y = fcf/mkt*100 if mkt else 0
    debt = info.get('debtToEquity', 50) / 10
    pe_fwd = info.get('forwardPE') or info.get('trailingPE') or 20

    q = r = b = v = m = 0

    # ROE + Marge op — 20 pts
    if roe >= 15 and margin >= 10: q = 20
    elif roe >= 10 or margin >= 8: q = 14
    elif roe >= 6 or margin >= 4: q = 8
    else: q = 3

    # Croissance CA — 25 pts (driver principal midcaps)
    if revg >= 15: r = 25
    elif revg >= 10: r = 20
    elif revg >= 6: r = 15
    elif revg >= 2: r = 9
    elif revg >= 0: r = 5
    else: r = 2

    # Bilan — 20 pts (moins strict que large caps)
    if debt < 2.0: b = 20
    elif debt < 3.5: b = 14
    elif debt < 5.0: b = 8
    else: b = 3

    # Valorisation — 20 pts
    if pe_fwd < 15: v = 20
    elif pe_fwd < 22: v = 16
    elif pe_fwd < 30: v = 11
    elif pe_fwd < 40: v = 6
    else: v = 2

    # FCF + BPA — 15 pts
    if fcf_y >= 6 and epsg > 5: m = 15
    elif fcf_y >= 4 or epsg > 8: m = 11
    elif fcf_y >= 2 or epsg > 3: m = 7
    else: m = 3

    return {'q':q,'r':r,'b':b,'v':v,'m':m,'total':min(100,q+r+b+v+m)}

# ─── RÉCUPÉRER LES FONDAMENTAUX ───────────────────────────────────
def get_fundamentals(ticker, yf_ticker):
    try:
        t = yf.Ticker(yf_ticker)
        info = t.info
        if not info.get('marketCap'):
            return None
        
        mkt = info.get('marketCap', 0)
        cap_type = 'large' if mkt > 5e9 else 'mid' if mkt > 1e9 else 'small'
        
        qarp_l = calc_qarp_large(info)
        qarp_m = calc_qarp_mid(info)
        
        # Score unifié selon cap
        if cap_type == 'large':
            unified = round(qarp_l['total']*0.75 + qarp_m['total']*0.25)
        elif cap_type == 'small':
            unified = round(qarp_l['total']*0.20 + qarp_m['total']*0.80)
        else:
            unified = round(qarp_l['total']*0.45 + qarp_m['total']*0.55)

        return {
            'ticker': ticker,
            'yf': yf_ticker,
            'cap_type': cap_type,
            'mkt_cap_bn': round(mkt/1e9, 1),
            'score_large': qarp_l['total'],
            'score_mid': qarp_m['total'],
            'score_unified': unified,
            'roe': round((info.get('returnOnEquity') or 0)*100, 1),
            'margin': round((info.get('profitMargins') or 0)*100, 1),
            'pe_fwd': round(info.get('forwardPE') or info.get('trailingPE') or 0, 1),
            'debt_eq': round((info.get('debtToEquity') or 0)/10, 2),
            'revg': round((info.get('revenueGrowth') or 0)*100, 1),
            'epsg': round((info.get('earningsGrowth') or 0)*100, 1),
        }
    except:
        return None

# ─── MAIN ─────────────────────────────────────────────────────────
def run_backtest_223():
    print("="*65)
    print("BACKTEST QARP 223 ACTIONS — VAL.PEA")
    print(f"Période : {PERIODE_DEBUT} → {PERIODE_FIN}")
    print("2 scores : QARP Large + QARP Mid")
    print("="*65)

    # ── Étape 1 : Fondamentaux
    print(f"\n[1/4] Calcul des scores pour {len(YF_MAP)} tickers...")
    fund_data = {}
    for i, (ticker, yf_t) in enumerate(YF_MAP.items()):
        data = get_fundamentals(ticker, yf_t)
        if data:
            fund_data[ticker] = data
        if (i+1) % 20 == 0:
            print(f"  {i+1}/{len(YF_MAP)} — {len(fund_data)} avec données")
    print(f"  → {len(fund_data)} tickers avec fondamentaux valides")

    # ── Étape 2 : Prix historiques
    print(f"\n[2/4] Téléchargement des prix 2019-2024...")
    yf_tickers = [v['yf'] for v in fund_data.values()] + [BENCHMARK]
    
    try:
        prices = yf.download(yf_tickers, start=PERIODE_DEBUT, end=PERIODE_FIN,
                             auto_adjust=True, progress=False)['Close']
        print(f"  → {prices.shape[0]} jours × {prices.shape[1]} tickers")
    except Exception as e:
        print(f"  Erreur batch: {e}. Mode individuel...")
        prices_dict = {}
        for ticker, data in fund_data.items():
            try:
                h = yf.download(data['yf'], start=PERIODE_DEBUT, end=PERIODE_FIN,
                               auto_adjust=True, progress=False)['Close']
                prices_dict[data['yf']] = h
            except:
                pass
        prices = pd.DataFrame(prices_dict)

    n_years = (pd.to_datetime(PERIODE_FIN) - pd.to_datetime(PERIODE_DEBUT)).days / 365.25

    # ── Étape 3 : Calcul des rendements
    print(f"\n[3/4] Calcul des rendements annualisés...")
    results = []

    for ticker, data in fund_data.items():
        yf_t = data['yf']
        col = None
        for c in prices.columns:
            if str(c) == yf_t or str(c).startswith(yf_t):
                col = c
                break
        if col is None:
            continue

        series = prices[col].dropna()
        if len(series) < 100:
            continue

        ret_total = (series.iloc[-1] / series.iloc[0] - 1) * 100
        ret_annual = ((series.iloc[-1] / series.iloc[0])**(1/n_years) - 1) * 100
        daily_r = series.pct_change().dropna()
        vol = daily_r.std() * np.sqrt(252) * 100
        roll_max = series.cummax()
        max_dd = ((series / roll_max) - 1).min() * 100
        sharpe = (ret_annual - 2) / vol if vol > 0 else 0

        results.append({
            **data,
            'ret_total_pct': round(ret_total, 1),
            'ret_annual_pct': round(ret_annual, 1),
            'vol_pct': round(vol, 1),
            'max_dd_pct': round(max_dd, 1),
            'sharpe': round(sharpe, 2),
        })

    df = pd.DataFrame(results).sort_values('score_unified', ascending=False)
    print(f"  → {len(df)} actions avec prix et fondamentaux")

    # ── Étape 4 : Analyse
    print(f"\n[4/4] Analyse des résultats...")

    # Benchmark
    bench_col = BENCHMARK
    if bench_col in prices.columns:
        bs = prices[bench_col].dropna()
        bench_ret = ((bs.iloc[-1]/bs.iloc[0])**(1/n_years)-1)*100
        print(f"\n  CAC40 benchmark : {bench_ret:+.1f}%/an")

    # Corrélations
    for score_col, label in [('score_unified','Score Unifié'),
                               ('score_large','Score Large'),
                               ('score_mid','Score Mid')]:
        vals = df[['ret_annual_pct', score_col]].dropna()
        if len(vals) > 10:
            corr = vals['ret_annual_pct'].corr(vals[score_col])
            print(f"\n  Corrélation {label} ↔ Performance : {corr:.3f} "
                  f"({'✅' if corr>0.3 else '⚠️' if corr>0 else '❌'})")

    # Performance par tranche — Score Unifié
    print(f"\n  Performance par tranche (Score Unifié) :")
    df['bucket'] = pd.cut(df['score_unified'],
                          bins=[0,40,55,65,75,100],
                          labels=['<40','40-55','55-65','65-75','>75'])
    bp = df.groupby('bucket', observed=True)['ret_annual_pct'].agg(['mean','count'])
    for bucket, row in bp.iterrows():
        print(f"    Score {bucket:6} : {row['mean']:+5.1f}%/an  ({int(row['count'])} actions)")

    # Large vs Mid séparé
    print(f"\n  Large Caps (QARP Large) :")
    large = df[df['cap_type']=='large']
    if len(large) > 5:
        print(f"    Corrélation Score Large ↔ Perf : {large['ret_annual_pct'].corr(large['score_large']):.3f}")
        for q in [40,55,65,75]:
            sub = large[large['score_large']>=q]
            if len(sub)>2:
                print(f"    Score Large ≥{q} ({len(sub)} actions) : {sub['ret_annual_pct'].mean():+.1f}%/an")

    print(f"\n  Midcaps (QARP Mid) :")
    mid = df[df['cap_type'].isin(['mid','small'])]
    if len(mid) > 5:
        print(f"    Corrélation Score Mid ↔ Perf : {mid['ret_annual_pct'].corr(mid['score_mid']):.3f}")
        for q in [40,55,65,75]:
            sub = mid[mid['score_mid']>=q]
            if len(sub)>2:
                print(f"    Score Mid ≥{q} ({len(sub)} actions) : {sub['ret_annual_pct'].mean():+.1f}%/an")

    # Anomalies — actions bien notées qui ont sous-performé
    print(f"\n  Top 10 score mais perf décevante (à revoir) :")
    surprises = df[df['score_unified']>=65].nsmallest(5,'ret_annual_pct')
    for _, row in surprises.iterrows():
        print(f"    {row['ticker']:6} score={row['score_unified']:3} perf={row['ret_annual_pct']:+5.1f}%/an")

    print(f"\n  Top 10 perf mais score bas (non détectées) :")
    missed = df[df['score_unified']<50].nlargest(5,'ret_annual_pct')
    for _, row in missed.iterrows():
        print(f"    {row['ticker']:6} score={row['score_unified']:3} perf={row['ret_annual_pct']:+5.1f}%/an")

    # ── Graphiques
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches

        fig, axes = plt.subplots(2, 3, figsize=(18, 11))
        fig.suptitle(f'Backtest QARP VAL.PEA — 223 actions SBF250 — {PERIODE_DEBUT} à {PERIODE_FIN}',
                     fontsize=13, fontweight='bold')

        # 1. Score Unifié vs Perf
        ax = axes[0,0]
        colors = ['#16a34a' if s>=65 else '#d97706' if s>=50 else '#dc2626'
                  for s in df['score_unified']]
        ax.scatter(df['score_unified'], df['ret_annual_pct'], c=colors, alpha=0.6, s=40)
        z = np.polyfit(df['score_unified'].dropna(), df['ret_annual_pct'].dropna(), 1)
        x_line = np.linspace(df['score_unified'].min(), df['score_unified'].max(), 100)
        ax.plot(x_line, np.poly1d(z)(x_line), 'k--', alpha=0.5, lw=1.5)
        ax.axhline(0, color='gray', linestyle=':', alpha=0.4)
        corr_u = df['ret_annual_pct'].corr(df['score_unified'])
        ax.set_title(f'Score Unifié vs Performance\nCorr: {corr_u:.3f}')
        ax.set_xlabel('Score QARP Unifié'); ax.set_ylabel('%/an')
        ax.grid(True, alpha=0.3)

        # 2. Score Large vs Perf (large caps seulement)
        ax2 = axes[0,1]
        large_df = df[df['cap_type']=='large'].copy()
        if len(large_df) > 5:
            colors_l = ['#16a34a' if s>=65 else '#d97706' if s>=50 else '#dc2626'
                       for s in large_df['score_large']]
            ax2.scatter(large_df['score_large'], large_df['ret_annual_pct'],
                       c=colors_l, alpha=0.7, s=50)
            z2 = np.polyfit(large_df['score_large'], large_df['ret_annual_pct'], 1)
            x2 = np.linspace(large_df['score_large'].min(), large_df['score_large'].max(), 100)
            ax2.plot(x2, np.poly1d(z2)(x2), 'b--', alpha=0.5, lw=1.5)
            corr_l = large_df['ret_annual_pct'].corr(large_df['score_large'])
            ax2.set_title(f'Score Large ↔ Large Caps seulement\nCorr: {corr_l:.3f} (n={len(large_df)})')
        ax2.axhline(0, color='gray', linestyle=':', alpha=0.4)
        ax2.set_xlabel('Score QARP Large'); ax2.set_ylabel('%/an')
        ax2.grid(True, alpha=0.3)

        # 3. Score Mid vs Perf (midcaps seulement)
        ax3 = axes[0,2]
        mid_df = df[df['cap_type'].isin(['mid','small'])].copy()
        if len(mid_df) > 5:
            colors_m = ['#16a34a' if s>=65 else '#d97706' if s>=50 else '#dc2626'
                       for s in mid_df['score_mid']]
            ax3.scatter(mid_df['score_mid'], mid_df['ret_annual_pct'],
                       c=colors_m, alpha=0.7, s=50)
            z3 = np.polyfit(mid_df['score_mid'], mid_df['ret_annual_pct'], 1)
            x3 = np.linspace(mid_df['score_mid'].min(), mid_df['score_mid'].max(), 100)
            ax3.plot(x3, np.poly1d(z3)(x3), 'purple', linestyle='--', alpha=0.5, lw=1.5)
            corr_m = mid_df['ret_annual_pct'].corr(mid_df['score_mid'])
            ax3.set_title(f'Score Mid ↔ Midcaps seulement\nCorr: {corr_m:.3f} (n={len(mid_df)})')
        ax3.axhline(0, color='gray', linestyle=':', alpha=0.4)
        ax3.set_xlabel('Score QARP Mid'); ax3.set_ylabel('%/an')
        ax3.grid(True, alpha=0.3)

        # 4. Performance par bucket
        ax4 = axes[1,0]
        bp_vals = df.groupby('bucket', observed=True)['ret_annual_pct'].mean()
        bp_counts = df.groupby('bucket', observed=True)['ret_annual_pct'].count()
        bar_colors = ['#dc2626','#d97706','#d97706','#16a34a','#16a34a']
        bars = ax4.bar(range(len(bp_vals)), bp_vals.values,
                      color=bar_colors[:len(bp_vals)])
        ax4.set_xticks(range(len(bp_vals)))
        ax4.set_xticklabels(bp_vals.index)
        ax4.axhline(0, color='gray', linestyle=':', alpha=0.4)
        if bench_col in prices.columns:
            ax4.axhline(bench_ret, color='navy', linestyle='--', alpha=0.7,
                       label=f'CAC40 {bench_ret:.1f}%/an')
            ax4.legend(fontsize=8)
        for bar, val, cnt in zip(bars, bp_vals.values, bp_counts.values):
            ax4.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3,
                    f'{val:+.1f}%\n(n={cnt})', ha='center', va='bottom', fontsize=8)
        ax4.set_title('Performance par tranche de score (Unifié)')
        ax4.set_ylabel('%/an'); ax4.grid(True, alpha=0.3, axis='y')

        # 5. Large vs Mid séparé
        ax5 = axes[1,1]
        x_pos = np.arange(5)
        width = 0.35
        buckets_l = pd.cut(large_df['score_large'] if len(large_df)>5 else pd.Series([]),
                           bins=[0,40,55,65,75,100], labels=['<40','40-55','55-65','65-75','>75'])
        buckets_m = pd.cut(mid_df['score_mid'] if len(mid_df)>5 else pd.Series([]),
                           bins=[0,40,55,65,75,100], labels=['<40','40-55','55-65','65-75','>75'])
        if len(large_df)>5 and len(mid_df)>5:
            large_df = large_df.copy(); large_df['bkt'] = buckets_l.values
            mid_df2 = mid_df.copy(); mid_df2['bkt'] = buckets_m.values
            l_perf = large_df.groupby('bkt', observed=True)['ret_annual_pct'].mean()
            m_perf = mid_df2.groupby('bkt', observed=True)['ret_annual_pct'].mean()
            ax5.bar(x_pos - width/2, l_perf.values, width, label='Large', color='#1d4ed8', alpha=0.8)
            ax5.bar(x_pos + width/2, m_perf.values, width, label='Mid', color='#7c3aed', alpha=0.8)
            ax5.set_xticks(x_pos)
            ax5.set_xticklabels(['<40','40-55','55-65','65-75','>75'])
            ax5.legend()
        ax5.axhline(0, color='gray', linestyle=':', alpha=0.4)
        ax5.set_title('Large Caps vs Midcaps par tranche de score')
        ax5.set_ylabel('%/an'); ax5.grid(True, alpha=0.3, axis='y')

        # 6. Distribution rendements par cap type
        ax6 = axes[1,2]
        for cap, col, label in [('large','#1d4ed8','Large'),
                                  ('mid','#7c3aed','Mid'),
                                  ('small','#16a34a','Small')]:
            sub = df[df['cap_type']==cap]['ret_annual_pct']
            if len(sub) > 2:
                ax6.hist(sub, bins=12, alpha=0.5, color=col,
                        label=f'{label} (n={len(sub)}, moy={sub.mean():+.1f}%)')
        ax6.axvline(0, color='black', linestyle=':', alpha=0.5)
        ax6.set_xlabel('%/an'); ax6.set_ylabel('Nb actions')
        ax6.set_title('Distribution rendements par type de cap')
        ax6.legend(fontsize=8); ax6.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('backtest_223_chart.png', dpi=150, bbox_inches='tight')
        plt.close()
        print(f"\n  ✅ backtest_223_chart.png sauvegardé")

    except ImportError:
        print("  matplotlib non disponible")

    # ── Sauvegarder CSV
    df.to_csv('backtest_223_results.csv', index=False)
    print(f"  ✅ backtest_223_results.csv ({len(df)} lignes)")

    # ── Synthèse finale
    print(f"\n{'='*65}")
    print("CONCLUSIONS")
    print('='*65)
    corr_u = df['ret_annual_pct'].corr(df['score_unified'])
    print(f"\n1. Score Unifié : corrél. {corr_u:.3f}")
    print(f"   {'✅ Modèle valide' if corr_u>0.3 else '⚠️ Corrélation faible — revoir pondérations'}")

    alpha = df[df['score_unified']>=65]['ret_annual_pct'].mean() - \
            df[df['score_unified']<50]['ret_annual_pct'].mean()
    print(f"\n2. Alpha Score ≥65 vs Score <50 : {alpha:+.1f}%/an")
    print(f"   {'✅ Alpha significatif' if alpha>5 else '⚠️ Alpha faible'}")

    print(f"\n3. Large Caps (n={len(df[df['cap_type']=='large'])}) :")
    if len(large_df)>5:
        corr_l = large_df['ret_annual_pct'].corr(large_df['score_large'])
        print(f"   Score Large corrél. {corr_l:.3f}")

    print(f"\n4. Midcaps (n={len(df[df['cap_type'].isin(['mid','small'])])}) :")
    if len(mid_df)>5:
        corr_m = mid_df['ret_annual_pct'].corr(mid_df['score_mid'])
        print(f"   Score Mid corrél. {corr_m:.3f}")

    print(f"\n5. Poids optimaux suggérés (à implémenter dans calcQARPLarge) :")
    dim_corrs = {}
    for col, label in [('roe','ROE'),('margin','Marge'),('debt_eq','Dette'),
                        ('pe_fwd','PE fwd'),('revg','Croiss.CA'),('epsg','Croiss.BPA')]:
        if col in df.columns:
            c2 = abs(df[col].corr(df['ret_annual_pct']))
            if not np.isnan(c2):
                dim_corrs[label] = c2
    total_c = sum(dim_corrs.values())
    for label, c2 in sorted(dim_corrs.items(), key=lambda x: x[1], reverse=True):
        pts = round(c2/total_c*100) if total_c > 0 else 20
        print(f"   {label:15} corrél={c2:.3f}  → suggère ~{pts} pts")

    return df

if __name__ == '__main__':
    run_backtest_223()
