#!/usr/bin/env python3
"""
portfolio_risk.py — VAL.PEA
Calcule la matrice de corrélation, VaR et métriques de risque
pour le portefeuille Val.

Usage :
  python portfolio_risk.py
  python portfolio_risk.py --period 2y   (1y, 2y, 5y)

Produit : portfolio_risk.html (rapport complet)
"""

import yfinance as yf
import pandas as pd
import numpy as np
import json, os, sys
from datetime import datetime, timedelta

# ─── PORTEFEUILLE VAL (synchronisé avec index.html) ───────────────
PORTFOLIO = [
    {'ticker':'ASML', 'qty':1,  'pru':653.60,  'yf':'ASML.AS'},
    {'ticker':'ELIS', 'qty':45, 'pru':18.9524, 'yf':'ELIS.PA'},
    {'ticker':'EL',   'qty':4,  'pru':205.78,  'yf':'EL.PA'},
    {'ticker':'GTT',  'qty':4,  'pru':196.7575,'yf':'GTT.PA'},
    {'ticker':'RMS',  'qty':2,  'pru':1795.95, 'yf':'RMS.PA'},
    {'ticker':'AI',   'qty':10, 'pru':159.308, 'yf':'AI.PA'},
    {'ticker':'LR',   'qty':5,  'pru':139.234, 'yf':'LR.PA'},
    {'ticker':'SU',   'qty':7,  'pru':240.7243,'yf':'SU.PA'},
    {'ticker':'HO',   'qty':3,  'pru':237.0767,'yf':'HO.PA'},
    {'ticker':'TTE',  'qty':10, 'pru':50.5205, 'yf':'TTE.PA'},
]

BENCHMARK = '^FCHI'  # CAC40

def run_risk_analysis(period='2y'):
    print("="*60)
    print("ANALYSE DE RISQUE PORTEFEUILLE — VAL.PEA")
    print(f"Période : {period} | {len(PORTFOLIO)} positions")
    print("="*60)
    
    # ── Télécharger les prix historiques ──────────────────────────
    print("\n[1/4] Téléchargement des prix...")
    tickers_yf = [p['yf'] for p in PORTFOLIO] + [BENCHMARK]
    
    try:
        prices = yf.download(tickers_yf, period=period, 
                            auto_adjust=True, progress=False)['Close']
        prices = prices.dropna(how='all')
        print(f"  → {len(prices)} jours de données, {prices.shape[1]} tickers")
    except Exception as e:
        print(f"  ERREUR: {e}")
        sys.exit(1)
    
    # Renommer les colonnes avec les tickers VAL.PEA
    rename = {p['yf']: p['ticker'] for p in PORTFOLIO}
    prices = prices.rename(columns=rename)
    
    # ── Calcul des poids actuels ──────────────────────────────────
    prices_latest = {}
    for pos in PORTFOLIO:
        if pos['ticker'] in prices.columns:
            prices_latest[pos['ticker']] = prices[pos['ticker']].dropna().iloc[-1]
    
    values = {p['ticker']: prices_latest.get(p['ticker'], p['pru']) * p['qty'] 
              for p in PORTFOLIO}
    total_value = sum(values.values())
    weights = {t: v/total_value for t,v in values.items()}
    
    print(f"\n  Valorisation totale : {total_value:.0f}€")
    for pos in PORTFOLIO:
        t = pos['ticker']
        pv = (prices_latest.get(t, pos['pru']) - pos['pru']) / pos['pru'] * 100
        print(f"  {t:6} {weights[t]*100:5.1f}%  PV={pv:+5.1f}%")
    
    # ── Rendements journaliers ────────────────────────────────────
    print("\n[2/4] Calcul des rendements et statistiques...")
    
    # Filtrer sur les colonnes disponibles
    available = [p['ticker'] for p in PORTFOLIO if p['ticker'] in prices.columns]
    returns = prices[available].pct_change().dropna()
    
    # Rendement du portefeuille pondéré
    port_weights = np.array([weights.get(t, 0) for t in available])
    port_weights = port_weights / port_weights.sum()  # Normaliser
    
    port_returns = returns[available].values @ port_weights
    port_returns_series = pd.Series(port_returns, index=returns.index)
    
    # Benchmark
    if BENCHMARK in prices.columns:
        bench_returns = prices[BENCHMARK].pct_change().dropna()
        common_idx = port_returns_series.index.intersection(bench_returns.index)
        bench_aligned = bench_returns[common_idx]
        port_aligned = port_returns_series[common_idx]
    
    # ── MÉTRIQUES DE RISQUE ───────────────────────────────────────
    print("\n[3/4] Calcul des métriques de risque...")
    
    # Rendement et volatilité
    ret_daily  = port_returns_series.mean()
    vol_daily  = port_returns_series.std()
    ret_annual = (1 + ret_daily)**252 - 1
    vol_annual = vol_daily * np.sqrt(252)
    
    # Sharpe (taux sans risque = 3%)
    rf = 0.03
    sharpe = (ret_annual - rf) / vol_annual if vol_annual > 0 else 0
    
    # Sortino (volatilité des pertes seulement)
    negative_returns = port_returns_series[port_returns_series < 0]
    downside_vol = negative_returns.std() * np.sqrt(252)
    sortino = (ret_annual - rf) / downside_vol if downside_vol > 0 else 0
    
    # Max Drawdown
    cumulative = (1 + port_returns_series).cumprod()
    rolling_max = cumulative.cummax()
    drawdown = (cumulative / rolling_max - 1)
    max_drawdown = drawdown.min()
    
    # Calmar ratio
    calmar = ret_annual / abs(max_drawdown) if max_drawdown != 0 else 0
    
    # Beta vs CAC40
    beta_port = 1.0
    if BENCHMARK in prices.columns:
        cov_matrix = np.cov(port_aligned.values, bench_aligned.values)
        beta_port = cov_matrix[0,1] / cov_matrix[1,1] if cov_matrix[1,1] > 0 else 1.0
        
        # Alpha de Jensen
        bench_ret_annual = (1 + bench_aligned.mean())**252 - 1
        alpha_jensen = ret_annual - (rf + beta_port * (bench_ret_annual - rf))
    else:
        bench_ret_annual = None
        alpha_jensen = None
    
    # ── VAR (Value at Risk) ───────────────────────────────────────
    # VaR historique à différents niveaux
    var_95_daily  = np.percentile(port_returns_series, 5)   # 5% worst days
    var_99_daily  = np.percentile(port_returns_series, 1)   # 1% worst days
    var_95_amount = var_95_daily * total_value
    var_99_amount = var_99_daily * total_value
    
    # VaR paramétrique (Gaussienne)
    from scipy import stats as scipy_stats
    var_95_param = scipy_stats.norm.ppf(0.05, ret_daily, vol_daily) * total_value
    
    # CVaR / Expected Shortfall (perte moyenne au-delà de VaR)
    cvar_95 = port_returns_series[port_returns_series <= var_95_daily].mean() * total_value
    
    print(f"\n  Rendement annualisé : {ret_annual*100:+.1f}%")
    print(f"  Volatilité annuelle  : {vol_annual*100:.1f}%")
    print(f"  Sharpe ratio         : {sharpe:.2f}")
    print(f"  Sortino ratio        : {sortino:.2f}")
    print(f"  Max Drawdown         : {max_drawdown*100:.1f}%")
    print(f"  Calmar ratio         : {calmar:.2f}")
    print(f"  Beta (CAC40)         : {beta_port:.2f}")
    if alpha_jensen is not None:
        print(f"  Alpha de Jensen      : {alpha_jensen*100:+.1f}%/an")
    
    print(f"\n  VaR 95% (1 jour)     : {var_95_amount:+.0f}€  ({var_95_daily*100:.2f}%)")
    print(f"  VaR 99% (1 jour)     : {var_99_amount:+.0f}€  ({var_99_daily*100:.2f}%)")
    print(f"  CVaR 95%             : {cvar_95:+.0f}€")
    
    # ── MATRICE DE CORRÉLATION ────────────────────────────────────
    print("\n[4/4] Matrice de corrélation...")
    
    corr_matrix = returns[available].corr()
    
    # Trouver les paires fortement corrélées
    high_corr_pairs = []
    for i, t1 in enumerate(available):
        for j, t2 in enumerate(available):
            if i < j:
                c = corr_matrix.loc[t1, t2]
                if abs(c) > 0.6:
                    high_corr_pairs.append((t1, t2, round(c, 3)))
    
    if high_corr_pairs:
        print(f"\n  Corrélations élevées (>0.6) :")
        for t1, t2, c in sorted(high_corr_pairs, key=lambda x: abs(x[2]), reverse=True):
            risk_flag = "⚠️ Risque doublon" if c > 0.75 else "📍 À surveiller"
            print(f"  {risk_flag} {t1} ↔ {t2} : {c:+.3f}")
    else:
        print("  ✅ Aucune corrélation > 0.6 — bonne diversification")
    
    # Corrélations avec le benchmark
    if BENCHMARK in prices.columns:
        print(f"\n  Corrélation avec le CAC40 :")
        for t in available:
            if t in returns.columns:
                c = returns[t].corr(bench_returns)
                print(f"    {t:6} : {c:+.3f}  {'haute' if abs(c)>0.7 else 'modérée' if abs(c)>0.4 else 'faible'}")
    
    # ── CONCENTRATION SECTORIELLE ─────────────────────────────────
    secteurs = {
        'ASML':'Semi-conducteurs', 'ELIS':'Services', 'EL':'Optique/Luxe',
        'GTT':'Énergie LNG', 'RMS':'Luxe', 'AI':'Gaz industriels',
        'LR':'Électrotechnique', 'SU':'Énergie/Industrie', 
        'HO':'Défense', 'TTE':'Énergie fossile',
    }
    
    sect_weights = {}
    for t, poids in weights.items():
        sect = secteurs.get(t, 'Autre')
        sect_weights[sect] = sect_weights.get(sect, 0) + poids
    
    print(f"\n  Répartition sectorielle :")
    for sect, poids in sorted(sect_weights.items(), key=lambda x: x[1], reverse=True):
        flag = "⚠️" if poids > 0.25 else "📍" if poids > 0.15 else "  "
        print(f"  {flag} {sect:25} : {poids*100:5.1f}%")
    
    # ── RAPPORT HTML ──────────────────────────────────────────────
    now = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    # Matrice corrélation HTML
    corr_html = "<table style='border-collapse:collapse;font-size:9px'><tr><th></th>"
    for t in available:
        corr_html += f"<th style='padding:3px;background:#0f2540;color:#fff'>{t}</th>"
    corr_html += "</tr>"
    
    for t1 in available:
        corr_html += f"<tr><th style='padding:3px;background:#0f2540;color:#fff'>{t1}</th>"
        for t2 in available:
            c = corr_matrix.loc[t1, t2]
            if t1 == t2:
                bg = '#16a34a'; col = '#fff'
            elif abs(c) > 0.75:
                bg = '#dc2626'; col = '#fff'
            elif abs(c) > 0.5:
                bg = '#d97706'; col = '#fff'
            elif c > 0:
                bg = '#dcfce7'; col = '#333'
            else:
                bg = '#fee2e2'; col = '#333'
            corr_html += f"<td style='padding:3px;background:{bg};color:{col};text-align:center'>{c:.2f}</td>"
        corr_html += "</tr>"
    corr_html += "</table>"
    
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>VAL.PEA — Analyse de Risque</title>
<style>
body{{font-family:Arial,sans-serif;font-size:11px;color:#1a1a1a;padding:20px;max-width:900px;margin:0 auto}}
.hd{{background:#0f2540;color:#fff;padding:16px 20px;border-radius:8px;margin-bottom:16px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:12px 0}}
.card{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:10px 12px}}
.card h3{{font-size:9px;text-transform:uppercase;color:#888;margin:0 0 6px}}
.big{{font-size:20px;font-weight:700;font-family:monospace}}
.green{{color:#16a34a}}.red{{color:#dc2626}}.orange{{color:#d97706}}
.row{{display:flex;justify-content:space-between;padding:3px 0;border-bottom:1px solid #f1f5f9}}
h2{{color:#0f2540;border-bottom:2px solid #f0d080;padding-bottom:4px;margin-top:20px}}
</style>
</head><body>

<div class="hd">
<div style="font-size:18px;font-weight:700">VAL.PEA — Analyse de Risque Portefeuille</div>
<div style="font-size:11px;color:rgba(255,255,255,.6)">
  {now} · {period} de données · {len(available)} positions · Valorisation {total_value:.0f}€
</div>
</div>

<h2>Performance & Risque</h2>
<div class="grid">
<div class="card"><h3>Rendement annualisé</h3>
<div class="big {'green' if ret_annual>0 else 'red'}">{ret_annual*100:+.1f}%</div></div>
<div class="card"><h3>Volatilité annuelle</h3>
<div class="big orange">{vol_annual*100:.1f}%</div></div>
<div class="card"><h3>Sharpe ratio</h3>
<div class="big {'green' if sharpe>1 else 'orange' if sharpe>0.5 else 'red'}">{sharpe:.2f}</div></div>
<div class="card"><h3>Max Drawdown</h3>
<div class="big red">{max_drawdown*100:.1f}%</div></div>
<div class="card"><h3>Sortino ratio</h3>
<div class="big {'green' if sortino>1.5 else 'orange'}">{sortino:.2f}</div></div>
<div class="card"><h3>Beta (CAC40)</h3>
<div class="big {'green' if 0.7<beta_port<1.2 else 'orange'}">{beta_port:.2f}</div></div>
</div>

<h2>Value at Risk (VaR)</h2>
<div class="card" style="margin-bottom:10px">
{''.join(f'<div class="row"><span>{k}</span><b style="color:#dc2626">{v}</b></div>' for k,v in [
    ('VaR 95% — 1 jour (histor.)', f'{var_95_amount:+.0f}€  ({var_95_daily*100:.2f}%)'),
    ('VaR 99% — 1 jour (histor.)', f'{var_99_amount:+.0f}€  ({var_99_daily*100:.2f}%)'),
    ('CVaR 95% (Expected Shortfall)', f'{cvar_95:+.0f}€'),
    ('Interprétation', f'1 jour sur 20, tu peux perdre plus de {abs(var_95_amount):.0f}€'),
])}
</div>

<h2>Matrice de Corrélation</h2>
<p style="color:#666;font-size:10px">
🟢 Corrélation identique · 🟠 Corrélation élevée (>0.75) · 
🔴 Corrélation très élevée (risque doublon) · Vert clair = corrélation positive modérée
</p>
{corr_html}

<h2>Concentration Sectorielle</h2>
<div class="card">
{''.join(f'<div class="row"><span>{sect}</span><b style="color:{"#dc2626" if w>0.25 else "#d97706" if w>0.15 else "#16a34a"}">{w*100:.1f}%</b></div>' 
for sect, w in sorted(sect_weights.items(), key=lambda x: x[1], reverse=True))}
</div>

<h2>Positions détaillées</h2>
<table width="100%" cellpadding="4" cellspacing="0" style="border-collapse:collapse;font-size:10px">
<tr style="background:#0f2540;color:#fff">
<th>Ticker</th><th>Qté</th><th>PRU</th><th>Cours</th><th>Valeur</th><th>Poids</th>
<th>PV/MV %</th><th>Volatilité</th><th>Corrél. CAC40</th></tr>
{''.join(f"""
<tr style="background:{'#f0fdf4' if (prices_latest.get(p['ticker'],p['pru'])-p['pru'])/p['pru']>0 else '#fff5f5'}">
<td><b>{p['ticker']}</b></td>
<td>{p['qty']}</td>
<td>{p['pru']:.2f}€</td>
<td>{prices_latest.get(p['ticker'],p['pru']):.2f}€</td>
<td>{values.get(p['ticker'],0):.0f}€</td>
<td>{weights.get(p['ticker'],0)*100:.1f}%</td>
<td style="color:{'#16a34a' if (prices_latest.get(p['ticker'],p['pru'])-p['pru'])/p['pru']>0 else '#dc2626'}">
{(prices_latest.get(p['ticker'],p['pru'])-p['pru'])/p['pru']*100:+.1f}%</td>
<td>{returns[p['ticker']].std()*np.sqrt(252)*100:.1f}% if '{p['ticker']}' in returns.columns else 'N/A'</td>
<td>{'N/A'}</td>
</tr>""" for p in PORTFOLIO if p['ticker'] in available)}
</table>

<p style="margin-top:20px;text-align:center;font-size:9px;color:#aaa">
VAL.PEA · Analyse de risque portefeuille · {now} · Non-conseil
</p>
</body></html>"""
    
    with open('portfolio_risk.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"\n✅ portfolio_risk.html sauvegardé")
    
    # Résultats JSON
    risk_summary = {
        'date': now,
        'total_value': round(total_value, 2),
        'ret_annual_pct': round(ret_annual*100, 2),
        'vol_annual_pct': round(vol_annual*100, 2),
        'sharpe': round(sharpe, 3),
        'sortino': round(sortino, 3),
        'max_drawdown_pct': round(max_drawdown*100, 2),
        'beta': round(beta_port, 3),
        'var_95_eur': round(var_95_amount, 0),
        'var_99_eur': round(var_99_amount, 0),
        'high_corr_pairs': high_corr_pairs,
        'weights': {t: round(w, 4) for t,w in weights.items()},
    }
    
    with open('portfolio_risk.json', 'w') as f:
        json.dump(risk_summary, f, indent=2)
    print("✅ portfolio_risk.json sauvegardé")
    
    return risk_summary

if __name__ == '__main__':
    period = '2y'
    if '--period' in sys.argv:
        idx = sys.argv.index('--period')
        period = sys.argv[idx+1]
    run_risk_analysis(period)
