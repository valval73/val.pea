#!/usr/bin/env python3
"""
backtest_qarp.py — VAL.PEA
Backteste le score QARP sur le SBF250 de 2019 à 2024.
Valide que le scoring prédit vraiment la performance.

Usage Google Colab :
  !pip install yfinance pandas numpy matplotlib seaborn
  !python backtest_qarp.py

Résultat : backtest_results.csv + backtest_chart.png
"""

import yfinance as yf
import pandas as pd
import numpy as np
import json, re, os, sys
from datetime import datetime, timedelta

# ─── CONFIGURATION ────────────────────────────────────────────────
PERIODE_DEBUT = "2019-01-01"
PERIODE_FIN   = "2024-12-31"
HOLDING_MOIS  = 12        # On tient chaque position 12 mois
TOP_N         = 20        # On sélectionne les N meilleures actions par score
CAPITAL_INIT  = 10000     # Capital de départ simulé
BENCHMARK     = "^FCHI"   # CAC40 comme benchmark

# Tickers SBF250 avec leur équivalent Yahoo Finance
YF_MAP = {
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA',
    'ORA':'ORA.PA','LR':'LR.PA','DSY':'DSY.PA','STM':'STM.PA','EL':'EL.PA',
    'ML':'ML.PA','ENGI':'ENGI.PA','HO':'HO.PA','DG':'DG.PA','CAP':'CAP.PA',
    'GTT':'GTT.PA','ELIS':'ELIS.PA','BVI':'BVI.PA','SPIE':'SPIE.PA',
    'IPSEN':'IPN.PA','REXEL':'RXL.PA','ALO':'ALO.PA','RNO':'RNO.PA',
    'SGO':'SGO.PA','VIE':'VIE.PA','VIV':'VIV.PA','AF':'AF.PA',
    'ASML':'ASML.AS','ERF':'ERF.PA','FDJ':'FDJ.PA','EDEN':'EDEN.PA',
    'SEB':'SK.PA','AC':'AC.PA','EN':'EN.PA','BN':'BN.PA',
}

# ─── CALCUL DU SCORE QARP depuis les fondamentaux Yahoo Finance ───
def calc_qarp_from_yf(ticker_yf):
    """Calcule un score QARP simplifié depuis les données Yahoo Finance"""
    try:
        t = yf.Ticker(ticker_yf)
        info = t.info
        
        # Extraction des métriques
        roe       = (info.get('returnOnEquity') or 0) * 100
        margin    = (info.get('profitMargins') or 0) * 100
        fcf_yield = 0
        debt_ebitda = info.get('debtToEquity', 5) / 10  # proxy
        pe        = info.get('trailingPE') or 25
        pe_fwd    = info.get('forwardPE') or pe
        revg      = (info.get('revenueGrowth') or 0) * 100
        epsg      = (info.get('earningsGrowth') or 0) * 100
        beta      = info.get('beta') or 1.0
        
        # FCF yield proxy
        fcf       = info.get('freeCashflow') or 0
        mkt_cap   = info.get('marketCap') or 1
        fcf_yield = (fcf / mkt_cap * 100) if mkt_cap > 0 else 0
        
        score = 0
        
        # Q — Qualité (ROE)
        if roe >= 20:   score += 20
        elif roe >= 15: score += 15
        elif roe >= 10: score += 10
        elif roe >= 5:  score += 5
        
        # R — Rentabilité (Marge + FCF)
        if margin >= 15 and fcf_yield >= 8:   score += 20
        elif margin >= 10 and fcf_yield >= 5: score += 15
        elif margin >= 5:                      score += 10
        else:                                  score += 3
        
        # B — Bilan (dette proxy)
        if debt_ebitda < 1.5:   score += 20
        elif debt_ebitda < 2.5: score += 14
        elif debt_ebitda < 4:   score += 8
        else:                    score += 2
        
        # V — Valorisation (PE forward vs moyen sectoriel)
        if pe_fwd < 12:    score += 20
        elif pe_fwd < 18:  score += 16
        elif pe_fwd < 25:  score += 11
        elif pe_fwd < 35:  score += 6
        else:               score += 2
        
        # M — Momentum (croissance BPA)
        if epsg > 15:   score += 20
        elif epsg > 8:  score += 15
        elif epsg > 3:  score += 10
        elif epsg > 0:  score += 6
        else:            score += 2
        
        return min(100, score), {
            'roe':round(roe,1), 'margin':round(margin,1),
            'fcf_yield':round(fcf_yield,1), 'debt_ebitda':round(debt_ebitda,1),
            'pe_fwd':round(pe_fwd,1), 'epsg':round(epsg,1)
        }
    except Exception as e:
        return None, {}

# ─── BACKTEST PRINCIPAL ───────────────────────────────────────────
def run_backtest():
    print("="*60)
    print("BACKTEST QARP — VAL.PEA")
    print(f"Période : {PERIODE_DEBUT} → {PERIODE_FIN}")
    print(f"Top {TOP_N} actions par score, holding {HOLDING_MOIS} mois")
    print("="*60)
    
    # ── Étape 1 : calculer les scores QARP pour tous les tickers
    print(f"\n[1/4] Calcul des scores QARP pour {len(YF_MAP)} tickers...")
    scores = {}
    metrics_data = {}
    
    for i, (ticker, yf_ticker) in enumerate(YF_MAP.items()):
        score, metrics = calc_qarp_from_yf(yf_ticker)
        if score is not None:
            scores[ticker] = {'yf': yf_ticker, 'score': score, 'metrics': metrics}
        if (i+1) % 10 == 0:
            print(f"  {i+1}/{len(YF_MAP)} traités...")
    
    print(f"  → {len(scores)} tickers avec données valides")
    
    # ── Étape 2 : télécharger les prix historiques
    print(f"\n[2/4] Téléchargement des prix historiques...")
    
    # Télécharger tous les tickers en batch
    yf_tickers = [v['yf'] for v in scores.values()]
    
    try:
        prices_raw = yf.download(
            yf_tickers + [BENCHMARK],
            start=PERIODE_DEBUT,
            end=PERIODE_FIN,
            auto_adjust=True,
            progress=False
        )['Close']
        print(f"  → Prix téléchargés : {prices_raw.shape}")
    except Exception as e:
        print(f"  ERREUR download batch: {e}")
        print("  Essai en mode individuel...")
        prices_dict = {}
        for ticker, data in scores.items():
            try:
                hist = yf.download(data['yf'], start=PERIODE_DEBUT, end=PERIODE_FIN, 
                                   auto_adjust=True, progress=False)['Close']
                prices_dict[data['yf']] = hist
            except:
                pass
        prices_raw = pd.DataFrame(prices_dict)
    
    # Ajouter le benchmark séparément si absent
    if BENCHMARK not in prices_raw.columns:
        try:
            bench = yf.download(BENCHMARK, start=PERIODE_DEBUT, end=PERIODE_FIN, 
                               auto_adjust=True, progress=False)['Close']
            prices_raw[BENCHMARK] = bench
        except:
            print("  Benchmark non disponible")
    
    # ── Étape 3 : simuler la stratégie
    print(f"\n[3/4] Simulation de la stratégie...")
    
    # Trier par score QARP
    ranked = sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True)
    top_tickers = ranked[:TOP_N]
    bottom_tickers = ranked[-TOP_N:]
    
    print(f"\n  TOP {TOP_N} (scores les plus élevés):")
    for t, d in top_tickers[:5]:
        print(f"    {t:6} score={d['score']:3} | ROE={d['metrics'].get('roe',0):5.1f}% | "
              f"Marge={d['metrics'].get('margin',0):5.1f}% | PE={d['metrics'].get('pe_fwd',0):5.1f}x")
    
    print(f"\n  BOTTOM {TOP_N} (scores les plus bas):")
    for t, d in bottom_tickers[:5]:
        print(f"    {t:6} score={d['score']:3} | ROE={d['metrics'].get('roe',0):5.1f}% | "
              f"Marge={d['metrics'].get('margin',0):5.1f}%")
    
    # Calculer les rendements
    results = []
    
    for ticker, data in ranked:
        yf_t = data['yf']
        if yf_t not in prices_raw.columns:
            continue
        
        price_series = prices_raw[yf_t].dropna()
        if len(price_series) < 50:
            continue
        
        # Rendement total sur la période
        ret_total = (price_series.iloc[-1] / price_series.iloc[0] - 1) * 100
        
        # Rendement annualisé
        n_years = (pd.to_datetime(PERIODE_FIN) - pd.to_datetime(PERIODE_DEBUT)).days / 365.25
        ret_annual = ((price_series.iloc[-1] / price_series.iloc[0]) ** (1/n_years) - 1) * 100
        
        # Volatilité annualisée
        daily_ret = price_series.pct_change().dropna()
        vol = daily_ret.std() * np.sqrt(252) * 100
        
        # Max drawdown
        roll_max = price_series.cummax()
        drawdown = (price_series / roll_max - 1)
        max_dd = drawdown.min() * 100
        
        # Sharpe ratio (approx, taux sans risque = 2%)
        sharpe = (ret_annual - 2) / vol if vol > 0 else 0
        
        results.append({
            'ticker': ticker,
            'score_qarp': data['score'],
            'score_decile': 'TOP' if data in [d for _,d in top_tickers] else (
                            'BOTTOM' if data in [d for _,d in bottom_tickers] else 'MID'),
            'ret_total_pct': round(ret_total, 1),
            'ret_annual_pct': round(ret_annual, 1),
            'volatilite_pct': round(vol, 1),
            'max_drawdown_pct': round(max_dd, 1),
            'sharpe': round(sharpe, 2),
            **data['metrics']
        })
    
    df = pd.DataFrame(results).sort_values('score_qarp', ascending=False)
    
    # ── Étape 4 : analyse des résultats
    print(f"\n[4/4] Analyse des résultats...")
    
    # Benchmark
    if BENCHMARK in prices_raw.columns:
        bench_series = prices_raw[BENCHMARK].dropna()
        bench_ret = (bench_series.iloc[-1] / bench_series.iloc[0] - 1) * 100
        bench_annual = ((bench_series.iloc[-1] / bench_series.iloc[0]) ** (1/n_years) - 1) * 100
        print(f"\n  CAC40 (benchmark) : {bench_ret:.1f}% total, {bench_annual:.1f}%/an")
    
    # Corrélation Score QARP ↔ Performance
    corr = df['score_qarp'].corr(df['ret_total_pct'])
    print(f"\n  Corrélation Score QARP ↔ Performance totale : {corr:.3f}")
    print(f"  {'Bonne corrélation positive ✅' if corr > 0.3 else 'Corrélation faible ⚠️ — score à calibrer' if corr > 0 else 'Corrélation NÉGATIVE ❌ — score à revoir'}")
    
    # Performance par décile de score
    print(f"\n  Performance par tranche de score QARP :")
    df['score_bucket'] = pd.cut(df['score_qarp'], bins=[0,40,55,65,75,100], 
                                  labels=['<40','40-55','55-65','65-75','>75'])
    bucket_perf = df.groupby('score_bucket', observed=True)['ret_annual_pct'].agg(['mean','count'])
    for bucket, row in bucket_perf.iterrows():
        print(f"    Score {bucket:6} : {row['mean']:+5.1f}%/an  ({int(row['count'])} actions)")
    
    # Top 20 vs reste
    top20_perf = df[df['score_qarp'] >= df['score_qarp'].quantile(0.8)]['ret_annual_pct'].mean()
    rest_perf  = df[df['score_qarp'] < df['score_qarp'].quantile(0.8)]['ret_annual_pct'].mean()
    print(f"\n  TOP 20% (score élevé) : {top20_perf:+.1f}%/an")
    print(f"  Reste (score faible)  : {rest_perf:+.1f}%/an")
    print(f"  Alpha généré : {top20_perf - rest_perf:+.1f}%/an")
    
    # Pondérations optimales
    print(f"\n  Corrélations par dimension QARP :")
    for col in ['roe','margin','fcf_yield','debt_ebitda','pe_fwd','epsg']:
        if col in df.columns:
            c = df[col].corr(df['ret_annual_pct'])
            print(f"    {col:15} : {c:+.3f}")
    
    # ── Sauvegarder les résultats
    df.to_csv('backtest_results.csv', index=False)
    print(f"\n  ✅ backtest_results.csv sauvegardé ({len(df)} lignes)")
    
    # ── Graphique
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle(f'Backtest QARP VAL.PEA — {PERIODE_DEBUT} à {PERIODE_FIN}', 
                     fontsize=14, fontweight='bold')
        
        # 1. Score vs Performance
        ax = axes[0,0]
        colors = ['#16a34a' if s >= 65 else '#d97706' if s >= 50 else '#dc2626' 
                  for s in df['score_qarp']]
        ax.scatter(df['score_qarp'], df['ret_annual_pct'], c=colors, alpha=0.7, s=60)
        z = np.polyfit(df['score_qarp'].dropna(), df['ret_annual_pct'].dropna(), 1)
        p = np.poly1d(z)
        x_line = np.linspace(df['score_qarp'].min(), df['score_qarp'].max(), 100)
        ax.plot(x_line, p(x_line), 'k--', alpha=0.5, linewidth=1.5)
        ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
        ax.set_xlabel('Score QARP')
        ax.set_ylabel('Rendement annualisé (%)')
        ax.set_title(f'Score QARP vs Performance\nCorrélation : {corr:.3f}')
        ax.grid(True, alpha=0.3)
        
        # 2. Performance par bucket de score
        ax2 = axes[0,1]
        bucket_means = df.groupby('score_bucket', observed=True)['ret_annual_pct'].mean()
        bar_colors = ['#dc2626','#d97706','#d97706','#16a34a','#16a34a']
        bars = ax2.bar(range(len(bucket_means)), bucket_means.values, color=bar_colors[:len(bucket_means)])
        ax2.set_xticks(range(len(bucket_means)))
        ax2.set_xticklabels(bucket_means.index)
        ax2.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
        if BENCHMARK in prices_raw.columns:
            ax2.axhline(y=bench_annual, color='navy', linestyle='--', alpha=0.7, label=f'CAC40 {bench_annual:.1f}%/an')
            ax2.legend()
        ax2.set_title('Performance par tranche de score QARP')
        ax2.set_ylabel('Rendement annualisé moyen (%)')
        ax2.grid(True, alpha=0.3, axis='y')
        for bar, val in zip(bars, bucket_means.values):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    f'{val:+.1f}%', ha='center', va='bottom', fontsize=9)
        
        # 3. Top 5 vs Bottom 5 performance évolution
        ax3 = axes[1,0]
        top5 = df.nlargest(5, 'score_qarp')
        bot5 = df.nsmallest(5, 'score_qarp')
        
        for _, row in top5.iterrows():
            yf_t = YF_MAP.get(row['ticker'])
            if yf_t and yf_t in prices_raw.columns:
                series = prices_raw[yf_t].dropna()
                normalized = series / series.iloc[0] * 100
                ax3.plot(normalized.index, normalized.values, 'g-', alpha=0.5, linewidth=1)
        
        for _, row in bot5.iterrows():
            yf_t = YF_MAP.get(row['ticker'])
            if yf_t and yf_t in prices_raw.columns:
                series = prices_raw[yf_t].dropna()
                normalized = series / series.iloc[0] * 100
                ax3.plot(normalized.index, normalized.values, 'r-', alpha=0.5, linewidth=1)
        
        if BENCHMARK in prices_raw.columns:
            bench_norm = prices_raw[BENCHMARK].dropna() / prices_raw[BENCHMARK].dropna().iloc[0] * 100
            ax3.plot(bench_norm.index, bench_norm.values, 'b--', linewidth=2, label='CAC40')
        
        green_patch = mpatches.Patch(color='green', alpha=0.5, label=f'Top 5 score')
        red_patch = mpatches.Patch(color='red', alpha=0.5, label=f'Bottom 5 score')
        ax3.legend(handles=[green_patch, red_patch] + ([mpatches.Patch(color='blue', label='CAC40')] if BENCHMARK in prices_raw.columns else []))
        ax3.set_title('Évolution des Top 5 vs Bottom 5')
        ax3.set_ylabel('Base 100')
        ax3.grid(True, alpha=0.3)
        
        # 4. Distribution des rendements par score
        ax4 = axes[1,1]
        df_top    = df[df['score_qarp'] >= 65]['ret_annual_pct']
        df_mid    = df[(df['score_qarp'] >= 50) & (df['score_qarp'] < 65)]['ret_annual_pct']
        df_bottom = df[df['score_qarp'] < 50]['ret_annual_pct']
        
        ax4.hist(df_top, bins=10, alpha=0.6, color='#16a34a', label=f'Score ≥65 (n={len(df_top)})')
        ax4.hist(df_mid, bins=10, alpha=0.6, color='#d97706', label=f'Score 50-65 (n={len(df_mid)})')
        ax4.hist(df_bottom, bins=10, alpha=0.6, color='#dc2626', label=f'Score <50 (n={len(df_bottom)})')
        ax4.axvline(x=0, color='black', linestyle=':', alpha=0.5)
        ax4.set_xlabel('Rendement annualisé (%)')
        ax4.set_ylabel('Nombre d\'actions')
        ax4.set_title('Distribution des rendements par niveau de score')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('backtest_chart.png', dpi=150, bbox_inches='tight')
        print("  ✅ backtest_chart.png sauvegardé")
        plt.close()
        
    except ImportError:
        print("  matplotlib non installé, graphiques ignorés")
    
    # ── Recommandations de recalibration
    print(f"\n{'='*60}")
    print("RECOMMANDATIONS DE RECALIBRATION")
    print("="*60)
    
    if corr > 0.3:
        print("✅ Le score QARP a une bonne corrélation avec la performance.")
        print("   Le modèle est valide. Ajustements possibles sur les pondérations.")
    elif corr > 0.1:
        print("⚠️  Corrélation faible. Les pondérations actuelles (20×5) sont sous-optimales.")
        print("   Revoir la dimension Valorisation qui est souvent la moins prédictive.")
    else:
        print("❌ Corrélation insuffisante. Le modèle mérite une refonte.")
        print("   Piste : ajouter le momentum prix (performance à 12 mois) qui est")
        print("   l'un des facteurs les plus robustes empiriquement.")
    
    # Pondérations suggérées
    print(f"\nPondérations actuelles : Q=20 R=20 B=20 V=20 M=20")
    
    # Calculer les corrélations par dimension
    dim_corrs = {}
    for col, dim in [('roe','Qualité'),('margin','Rentabilité'),('debt_ebitda','Bilan'),
                      ('pe_fwd','Valorisation'),('epsg','Momentum')]:
        if col in df.columns:
            c = abs(df[col].corr(df['ret_annual_pct']))
            dim_corrs[dim] = c
    
    if dim_corrs:
        total_corr = sum(dim_corrs.values())
        print("Pondérations suggérées basées sur les données :")
        for dim, c in sorted(dim_corrs.items(), key=lambda x: x[1], reverse=True):
            suggested = round(c / total_corr * 100) if total_corr > 0 else 20
            print(f"  {dim:15} : {suggested:2}/100 (corrélation abs = {c:.3f})")
    
    print(f"\n✅ Backtest terminé. {len(df)} actions analysées.")
    return df

if __name__ == '__main__':
    df = run_backtest()
