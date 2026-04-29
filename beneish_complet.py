#!/usr/bin/env python3
"""
beneish_complet.py — VAL.PEA
Calcule les 8 vrais ratios Beneish depuis les bilans Yahoo Finance
et met à jour index.html avec les M-Scores réels.

Usage :
  python beneish_complet.py [--ticker EL] [--all]
"""

import yfinance as yf
import re, sys, os, json
from datetime import datetime

YF_MAP = {
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA',
    'ORA':'ORA.PA','LR':'LR.PA','DSY':'DSY.PA','STM':'STM.PA','EL':'EL.PA',
    'ML':'ML.PA','ENGI':'ENGI.PA','HO':'HO.PA','DG':'DG.PA','CAP':'CAP.PA',
    'GTT':'GTT.PA','ELIS':'ELIS.PA','SPIE':'SPIE.PA','RNO':'RNO.PA',
    'SGO':'SGO.PA','ASML':'ASML.AS','ERF':'ERF.PA',
}

def safe_div(a, b, default=1.0):
    try:
        return float(a) / float(b) if b and float(b) != 0 else default
    except:
        return default

def calc_beneish_complet(ticker, yf_ticker):
    """
    Calcule les 8 ratios du modèle Beneish M-Score.
    
    Les 8 ratios :
    1. DSRI  : Days Sales in Receivables Index
    2. GMI   : Gross Margin Index
    3. AQI   : Asset Quality Index
    4. SGI   : Sales Growth Index
    5. DEPI  : Depreciation Index
    6. SGAI  : Sales General & Admin Expenses Index
    7. TATA  : Total Accruals to Total Assets
    8. LVGI  : Leverage Index
    """
    try:
        t = yf.Ticker(yf_ticker)
        
        # Récupérer 2 années de bilans
        bs  = t.balance_sheet    # Bilan
        inc = t.income_stmt      # Compte de résultats
        cf  = t.cashflow         # Flux de trésorerie
        
        if bs.empty or inc.empty:
            return None, "Données bilans insuffisantes"
        
        # Colonnes = années (plus récente en premier)
        cols = bs.columns.tolist()
        if len(cols) < 2:
            return None, "Pas assez d'années de données"
        
        y1 = cols[0]  # Année N (plus récente)
        y0 = cols[1]  # Année N-1
        
        def get(df, key, year):
            """Récupère une valeur de bilan par clé"""
            for k in df.index:
                if key.lower() in str(k).lower():
                    try:
                        val = df.loc[k, year]
                        if val is not None and str(val) != 'nan':
                            return float(val)
                    except:
                        pass
            return None
        
        # ── EXTRACTION DES DONNÉES BRUTES ──
        # Bilan
        receivables_t1 = get(bs, 'receivable', y1) or get(bs, 'net receivable', y1)
        receivables_t0 = get(bs, 'receivable', y0) or get(bs, 'net receivable', y0)
        total_assets_t1 = get(bs, 'total assets', y1) or get(bs, 'total asset', y1)
        total_assets_t0 = get(bs, 'total assets', y0) or get(bs, 'total asset', y0)
        ppe_net_t1 = get(bs, 'net ppe', y1) or get(bs, 'property plant equipment', y1)
        ppe_net_t0 = get(bs, 'net ppe', y0) or get(bs, 'property plant equipment', y0)
        total_debt_t1 = (get(bs, 'long term debt', y1) or 0) + (get(bs, 'current debt', y1) or 0)
        total_debt_t0 = (get(bs, 'long term debt', y0) or 0) + (get(bs, 'current debt', y0) or 0)
        
        # Compte de résultats
        revenue_t1 = get(inc, 'total revenue', y1)
        revenue_t0 = get(inc, 'total revenue', y0)
        gross_profit_t1 = get(inc, 'gross profit', y1)
        gross_profit_t0 = get(inc, 'gross profit', y0)
        cogs_t1 = get(inc, 'cost of revenue', y1) or get(inc, 'cost of goods', y1)
        cogs_t0 = get(inc, 'cost of revenue', y0) or get(inc, 'cost of goods', y0)
        sga_t1 = get(inc, 'selling general', y1) or get(inc, 'sga', y1)
        sga_t0 = get(inc, 'selling general', y0) or get(inc, 'sga', y0)
        
        # Flux
        depreciation_t1 = get(cf, 'depreciation', y1)
        depreciation_t0 = get(cf, 'depreciation', y0)
        operating_cf_t1 = get(cf, 'operating cash flow', y1) or get(cf, 'total cash from operating', y1)
        net_income_t1 = get(inc, 'net income', y1)
        
        # ── CALCUL DES 8 RATIOS BENEISH ──
        ratios = {}
        
        # 1. DSRI — jours de créances clients
        # DSRI = (Créances_t1 / CA_t1) / (Créances_t0 / CA_t0)
        if all(v for v in [receivables_t1, revenue_t1, receivables_t0, revenue_t0]):
            ratios['DSRI'] = safe_div(receivables_t1 / revenue_t1, 
                                       receivables_t0 / revenue_t0)
        
        # 2. GMI — indice de marge brute
        # GMI = Marge_brute_t0 / Marge_brute_t1 (>1 = dégradation)
        if all(v for v in [gross_profit_t1, revenue_t1, gross_profit_t0, revenue_t0]):
            gm_t1 = gross_profit_t1 / revenue_t1
            gm_t0 = gross_profit_t0 / revenue_t0
            ratios['GMI'] = safe_div(gm_t0, gm_t1)
        
        # 3. AQI — qualité des actifs
        # AQI = (1 - (ActifsCourants+PPE)_t1/TotalActifs_t1) / même_t0
        if all(v for v in [ppe_net_t1, total_assets_t1, ppe_net_t0, total_assets_t0]):
            aqi_t1 = 1 - safe_div(ppe_net_t1, total_assets_t1)
            aqi_t0 = 1 - safe_div(ppe_net_t0, total_assets_t0)
            ratios['AQI'] = safe_div(aqi_t1, aqi_t0)
        
        # 4. SGI — croissance du CA
        # SGI = CA_t1 / CA_t0
        if all(v for v in [revenue_t1, revenue_t0]):
            ratios['SGI'] = safe_div(revenue_t1, revenue_t0)
        
        # 5. DEPI — indice d'amortissement
        # DEPI = (Amort/(Amort+PPE))_t0 / même_t1 (>1 = ralentissement amortissement)
        if all(v for v in [depreciation_t1, ppe_net_t1, depreciation_t0, ppe_net_t0]):
            dep_rate_t1 = safe_div(depreciation_t1, depreciation_t1 + ppe_net_t1)
            dep_rate_t0 = safe_div(depreciation_t0, depreciation_t0 + ppe_net_t0)
            ratios['DEPI'] = safe_div(dep_rate_t0, dep_rate_t1)
        
        # 6. SGAI — charges générales et administratives
        # SGAI = (SGA/CA)_t1 / (SGA/CA)_t0
        if all(v for v in [sga_t1, revenue_t1, sga_t0, revenue_t0]):
            ratios['SGAI'] = safe_div(sga_t1 / revenue_t1, sga_t0 / revenue_t0)
        
        # 7. TATA — accruals totaux sur total actifs
        # TATA = (Résultat net - Flux opérationnels) / Total actifs
        if all(v for v in [net_income_t1, operating_cf_t1, total_assets_t1]):
            ratios['TATA'] = safe_div(net_income_t1 - operating_cf_t1, total_assets_t1)
        
        # 8. LVGI — indice de levier
        # LVGI = (Dettes LT / Total actifs)_t1 / même_t0
        if all(v for v in [total_debt_t1, total_assets_t1, total_debt_t0, total_assets_t0]):
            ratios['LVGI'] = safe_div(
                total_debt_t1 / total_assets_t1, 
                total_debt_t0 / total_assets_t0
            )
        
        if len(ratios) < 4:
            return None, f"Données insuffisantes ({len(ratios)}/8 ratios calculés)"
        
        # ── CALCUL DU M-SCORE ──
        # Coefficients Beneish originaux
        coefficients = {
            'DSRI':  0.920,
            'GMI':   0.528,
            'AQI':   0.404,
            'SGI':   0.892,
            'DEPI':  0.115,
            'SGAI': -0.172,
            'TATA':  4.679,
            'LVGI': -0.327,
        }
        
        m_score = -4.840  # constante
        for ratio_name, coeff in coefficients.items():
            if ratio_name in ratios:
                m_score += coeff * ratios[ratio_name]
        
        # Verdict
        if m_score > -1.49:
            verdict = "⚠️ ALERTE ÉLEVÉE — Risque de manipulation comptable"
            risk_level = "HIGH"
        elif m_score > -1.78:
            verdict = "⚠️ Zone grise — Surveiller les flux de trésorerie"
            risk_level = "MEDIUM"
        else:
            verdict = "✅ Normal — Pas de signal de manipulation"
            risk_level = "LOW"
        
        return {
            'ticker': ticker,
            'mscore': round(m_score, 3),
            'verdict': verdict,
            'risk_level': risk_level,
            'ratios': {k: round(v, 3) for k,v in ratios.items()},
            'ratios_count': len(ratios),
            'annee_n': str(y1.year if hasattr(y1,'year') else y1),
            'annee_n1': str(y0.year if hasattr(y0,'year') else y0),
        }, None
        
    except Exception as e:
        return None, str(e)[:100]


def update_html_beneish(html_path, beneish_results):
    """Met à jour les valeurs beneish dans index.html"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = 0
    for result in beneish_results:
        ticker = result['ticker']
        mscore = result['mscore']
        
        # Chercher le pattern beneish: dans le bloc S[]
        pattern = f"ticker:'{ticker}'"
        pos = content.find(pattern)
        if pos < 0:
            continue
        
        block_end = content.find('\n\n{ticker:', pos+1)
        if block_end < 0:
            block_end = pos + 2000
        block = content[pos:block_end]
        
        # Mettre à jour ou ajouter beneish
        if 'beneish:' in block:
            new_block = re.sub(r'beneish:[-\d.]+', f'beneish:{mscore}', block, count=1)
        else:
            # Ajouter après score:
            new_block = re.sub(r"(score:'[ABCD]')", f"\\1,beneish:{mscore}", block, count=1)
        
        if new_block != block:
            content = content[:pos] + new_block + content[pos+len(block):]
            updated += 1
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return updated


def main():
    args = sys.argv[1:]
    
    # Déterminer quels tickers traiter
    if '--ticker' in args:
        idx = args.index('--ticker')
        target_tickers = {args[idx+1]: YF_MAP[args[idx+1]]} if args[idx+1] in YF_MAP else {}
    elif '--all' in args:
        target_tickers = YF_MAP
    else:
        # Par défaut : les BPF (grandes caps + portefeuille Val)
        bpf = ['EL','ASML','RMS','AI','LR','SU','HO','TTE','GTT','ELIS',
               'MC','OR','SAN','SAF','DSY','KER','BNP','AXA','GLE']
        target_tickers = {t: YF_MAP[t] for t in bpf if t in YF_MAP}
    
    print(f"Calcul Beneish complet pour {len(target_tickers)} tickers...")
    print("="*60)
    
    results = []
    errors = []
    
    for ticker, yf_ticker in target_tickers.items():
        result, error = calc_beneish_complet(ticker, yf_ticker)
        if result:
            results.append(result)
            risk_icon = {'HIGH':'🔴','MEDIUM':'🟡','LOW':'✅'}.get(result['risk_level'],'⚪')
            print(f"{risk_icon} {ticker:6} M-Score = {result['mscore']:+.3f}  "
                  f"({result['ratios_count']}/8 ratios)  {result['verdict'][:30]}")
        else:
            errors.append(f"{ticker}: {error}")
            print(f"⚪ {ticker:6} Données insuffisantes: {error[:50]}")
    
    print(f"\n{'='*60}")
    print(f"Résultats : {len(results)} calculés, {len(errors)} erreurs")
    
    # Alertes
    high_risk = [r for r in results if r['risk_level'] == 'HIGH']
    if high_risk:
        print(f"\n🔴 ALERTES HAUTE PRIORITÉ ({len(high_risk)}):")
        for r in sorted(high_risk, key=lambda x: x['mscore'], reverse=True):
            print(f"  {r['ticker']} : M-Score = {r['mscore']:+.3f} — {r['verdict']}")
    else:
        print("\n✅ Aucune alerte haute priorité")
    
    # Sauvegarder JSON
    with open('beneish_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n✅ beneish_results.json sauvegardé")
    
    # Mettre à jour HTML si présent
    if os.path.exists('index.html') and results:
        n = update_html_beneish('index.html', results)
        print(f"✅ index.html mis à jour ({n} actions)")
    
    return results

if __name__ == '__main__':
    main()
