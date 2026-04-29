#!/usr/bin/env python3
"""
zones_dynamiques.py — VAL.PEA
Recalcule les zones el/eh/stop/o1/dcf depuis les fondamentaux réels
au lieu du recalibrage proportionnel (crude).

Méthode :
  DCF médian = PE_forward × BPA_N+1 × (1 + g_5ans) — pondéré par secteur
  Zone basse  = DCF × décote sectorielle (15-25%)
  Zone haute  = DCF × prime faible (5%)
  Stop loss   = Zone basse × 0.88 (12% sous la zone)
  Objectif 1  = DCF × 1.10 à 1.20

Usage :
  python zones_dynamiques.py [--ticker EL] [--grade A] [--all]
"""

import yfinance as yf
import re, sys, os, json
from datetime import datetime

# Décotes sectorielles sur le DCF (zone basse = DCF × (1 - décote))
# Plus la décote est élevée, plus on demande un rabais important pour entrer
DECOTES_SECTEUR = {
    'Semi-conducteurs EUV':  0.28,  # Très volatile, on demande plus de marge
    'Luxe':                  0.22,
    'Optique':               0.18,
    'Défense':               0.15,
    'Énergie':               0.20,
    'Industrie':             0.16,
    'Technologie':           0.22,
    'Santé':                 0.18,
    'Financier':             0.20,
    'Immobilier':            0.22,
    'Consommation':          0.18,
    'Utilities':             0.15,
    'Telecom':               0.18,
    'default':               0.18,
}

# PE normalisés par secteur (PE "juste" long terme)
PE_SECTEUR = {
    'Semi-conducteurs EUV':  35,
    'Luxe':                  30,
    'Optique':               28,
    'Défense':               22,
    'Énergie':               12,
    'Industrie':             20,
    'Technologie':           28,
    'Santé':                 22,
    'Financier':             12,
    'Immobilier':            18,
    'Consommation':          20,
    'Utilities':             18,
    'Telecom':               15,
    'default':               20,
}

YF_MAP = {
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','KER':'KER.PA','EL':'EL.PA',
    'LR':'LR.PA','DSY':'DSY.PA','STM':'STM.PA','ML':'ML.PA','HO':'HO.PA',
    'CAP':'CAP.PA','GTT':'GTT.PA','ELIS':'ELIS.PA','ASML':'ASML.AS',
    'RNO':'RNO.PA','SGO':'SGO.PA','ENGI':'ENGI.PA','DG':'DG.PA',
}


def calc_zones_from_fundamentals(ticker, yf_ticker, sector='default'):
    """
    Calcule les zones d'achat dynamiques depuis les fondamentaux réels.
    
    Approche :
    1. DCF simplifié = PE_sectoriel × EPS_forward
    2. Confirmation par DDM (si dividende) et EV/EBITDA sectoriel
    3. Zone = autour du DCF avec décote sectorielle
    """
    try:
        t = yf.Ticker(yf_ticker)
        info = t.info
        
        price = info.get('regularMarketPrice') or info.get('previousClose')
        if not price:
            return None, "Prix non disponible"
        
        # ── DONNÉES CLÉS ──────────────────────────────────────────
        eps_ttm    = info.get('trailingEps') or 0
        eps_fwd    = info.get('forwardEps') or eps_ttm * 1.08  # +8% par défaut
        pe_ttm     = info.get('trailingPE') or (price / eps_ttm if eps_ttm else 20)
        pe_fwd     = info.get('forwardPE') or (price / eps_fwd if eps_fwd else 20)
        peg        = info.get('pegRatio') or 1.5
        beta       = info.get('beta') or 1.0
        rev_growth = (info.get('revenueGrowth') or 0.07)
        eps_growth = (info.get('earningsGrowth') or rev_growth)
        dividend   = info.get('dividendYield') or 0
        roe        = (info.get('returnOnEquity') or 0)
        book_value = info.get('bookValue') or 0
        
        # ── MÉTHODE 1 : DCF par PE normalisé ─────────────────────
        pe_normal = PE_SECTEUR.get(sector, PE_SECTEUR['default'])
        
        # EPS projeté à 3 ans
        eps_3y = eps_fwd * ((1 + eps_growth) ** 3) if eps_fwd > 0 else 0
        
        # DCF simplifié
        dcf_pe = pe_normal * eps_3y if eps_3y > 0 else 0
        
        # ── MÉTHODE 2 : Gordon Growth Model (si dividende) ───────
        dcf_gordon = 0
        if dividend > 0.01 and price > 0:
            div_amount = price * dividend
            ke = 0.08  # taux de rendement exigé 8%
            g = min(eps_growth, 0.07)  # taux de croissance long terme, max 7%
            if ke > g:
                dcf_gordon = div_amount * (1 + g) / (ke - g)
        
        # ── MÉTHODE 3 : Price-to-Book ajusté (si ROE élevé) ──────
        dcf_pb = 0
        if roe > 0.15 and book_value > 0:
            # PB justifié = ROE / ke
            ke = 0.09
            pb_justified = roe / ke
            dcf_pb = book_value * pb_justified
        
        # ── CONSOLIDATION ─────────────────────────────────────────
        dcfs = [d for d in [dcf_pe, dcf_gordon, dcf_pb] if d > price * 0.3]
        
        if not dcfs:
            # Fallback : utiliser le PE actuel comme base
            if pe_ttm and pe_ttm > 0:
                dcfs = [price * (pe_normal / pe_ttm)]
            else:
                return None, "Impossible de calculer le DCF"
        
        dcfm = round(sum(dcfs) / len(dcfs), 2)  # DCF médian
        dcfb = round(dcfm * 0.85, 2)             # DCF bear (-15%)
        dcfu = round(dcfm * 1.20, 2)             # DCF bull (+20%)
        
        # ── ZONES D'ACHAT ─────────────────────────────────────────
        decote = DECOTES_SECTEUR.get(sector, DECOTES_SECTEUR['default'])
        
        # Zone : autour de DCF × (1 - décote) à DCF × (1 - décote/2)
        el = round(dcfm * (1 - decote), 2)          # Zone basse
        eh = round(dcfm * (1 - decote * 0.4), 2)    # Zone haute
        
        # Stop loss : 12% sous la zone basse
        stop = round(el * 0.88, 2)
        
        # Objectifs
        o1 = round(dcfm * 1.05, 2)   # Objectif 1 = DCF médian + 5%
        o2 = round(dcfm * 1.20, 2)   # Objectif 2 = DCF bull
        
        # ── VALIDATION DE COHÉRENCE ───────────────────────────────
        assert stop < price * 1.5, f"Stop trop haut: {stop} vs prix {price}"
        assert el < eh, f"el >= eh: {el} >= {eh}"
        assert o1 > el, f"Obj1 {o1} < zone {el}"
        
        # ── QUALITÉ DU CALCUL ─────────────────────────────────────
        methods_used = []
        if dcf_pe > 0:   methods_used.append('PE×EPS')
        if dcf_gordon > 0: methods_used.append('Gordon')
        if dcf_pb > 0:   methods_used.append('P/B')
        
        return {
            'ticker':     ticker,
            'price':      round(price, 2),
            'el':         el,
            'eh':         eh,
            'stop':       stop,
            'o1':         o1,
            'o2':         o2,
            'dcfb':       dcfb,
            'dcfm':       dcfm,
            'dcfu':       dcfu,
            'upside_pct': round((dcfm - price) / price * 100, 1),
            'in_zone':    el <= price <= eh,
            'dcf_methods': '+'.join(methods_used),
            'eps_fwd':    round(eps_fwd, 2) if eps_fwd else 0,
            'eps_3y':     round(eps_3y, 2) if eps_3y else 0,
            'pe_used':    pe_normal,
            'sector':     sector,
        }, None
        
    except AssertionError as e:
        return None, f"Incohérence: {e}"
    except Exception as e:
        return None, str(e)[:100]


def update_html_zones(html_path, zones_results):
    """Met à jour les zones dans index.html"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    s_start = content.find("const S=[")
    updated = 0
    skipped = 0
    
    for result in zones_results:
        ticker = result['ticker']
        pos = content.find(f"ticker:'{ticker}',", s_start)
        if pos < 0:
            continue
        
        block_end = content.find('\n\n{ticker:', pos+1)
        if block_end < 0:
            block_end = pos + 2000
        block = content[pos:block_end]
        
        # Mise à jour des zones
        new_block = block
        for key in ['el','eh','stop','o1','o2','dcfb','dcfm','dcfu']:
            val = result.get(key)
            if val:
                new_block = re.sub(r'\b' + key + r':[\d.]+', f'{key}:{val}', new_block, count=1)
        
        if new_block != block:
            content = content[:pos] + new_block + content[pos+len(block):]
            updated += 1
        else:
            skipped += 1
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return updated, skipped


def main():
    # Lire le secteur depuis index.html si disponible
    sector_map = {}
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
        for m in re.finditer(r"ticker:'([^']+)'.*?sector:'([^']+)'", html, re.DOTALL):
            sector_map[m.group(1)] = m.group(2)
    
    args = sys.argv[1:]
    
    if '--ticker' in args:
        idx = args.index('--ticker')
        tk = args[idx+1]
        target = {tk: YF_MAP[tk]} if tk in YF_MAP else {}
    elif '--grade' in args:
        # Filtrer par grade depuis index.html
        grade = args[args.index('--grade')+1]
        if os.path.exists('index.html'):
            with open('index.html','r') as f:
                html = f.read()
            target_tickers = re.findall(r"ticker:'([^']+)'[^}]+score:'" + grade + r"'", html)
            target = {t: YF_MAP[t] for t in target_tickers if t in YF_MAP}
        else:
            target = YF_MAP
    else:
        # Par défaut : BPF + portefeuille
        bpf = ['EL','ASML','RMS','AI','LR','SU','HO','TTE','GTT','ELIS',
               'MC','OR','SAN','SAF','DSY','KER','BNP','SGO']
        target = {t: YF_MAP[t] for t in bpf if t in YF_MAP}
    
    print(f"Calcul zones dynamiques pour {len(target)} tickers...")
    print("="*60)
    
    results = []
    errors = []
    
    for ticker, yf_ticker in target.items():
        sector = sector_map.get(ticker, 'default')
        result, error = calc_zones_from_fundamentals(ticker, yf_ticker, sector)
        
        if result:
            results.append(result)
            zone_flag = "🟢 EN ZONE" if result['in_zone'] else "⚪ hors zone"
            print(f"{zone_flag} {ticker:6} DCF={result['dcfm']}€  "
                  f"Zone [{result['el']}-{result['eh']}]  "
                  f"Upside {result['upside_pct']:+.0f}%  "
                  f"({result['dcf_methods']})")
        else:
            errors.append(f"{ticker}: {error}")
            print(f"⚠️  {ticker:6} {error[:50]}")
    
    print(f"\n{'='*60}")
    print(f"{len(results)} zones calculées, {len(errors)} erreurs")
    
    # Sauvegarder
    with open('zones_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"✅ zones_results.json sauvegardé")
    
    # Mettre à jour HTML
    if os.path.exists('index.html') and results:
        upd, skip = update_html_zones('index.html', results)
        print(f"✅ index.html : {upd} actions mises à jour, {skip} inchangées")
    
    # Résumé des meilleures opportunités
    in_zone = [r for r in results if r['in_zone'] and r['upside_pct'] > 10]
    if in_zone:
        print(f"\n🎯 Opportunités en zone avec upside > 10% :")
        for r in sorted(in_zone, key=lambda x: x['upside_pct'], reverse=True):
            print(f"  {r['ticker']:6} cours={r['price']}€  DCF={r['dcfm']}€  "
                  f"upside={r['upside_pct']:+.0f}%")

if __name__ == '__main__':
    main()
