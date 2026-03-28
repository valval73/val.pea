#!/usr/bin/env python3
"""
VAL.PEA — Mise à jour automatique
- Prix de clôture (228 actions)
- Volume & vratio
- Indicateurs macro (taux, or, dollar)
- Ratios fondamentaux trimestriels (PE, marges, BPA)
- Commit dans index.html

GitHub Actions : 17h35 Paris, Lun-Ven
"""

import yfinance as yf
import json, re, time, os
from datetime import datetime

# ══════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════

# Délai entre chaque appel Yahoo Finance (évite le rate-limiting)
DELAY = 0.4  # secondes — 228 x 0.4s = ~90s total

# Tickers à mettre à jour (228 actions SBF250 + ETFs)
YAHOO = {
    "AI":    "AI.PA",    "SU":    "SU.PA",    "RMS":   "RMS.PA",
    "TTE":   "TTE.PA",   "ASML":  "ASML.AS",  "ELIS":  "ELIS.PA",
    "GTT":   "GTT.PA",   "HO":    "HO.PA",    "LR":    "LR.PA",
    "EL":    "EL.PA",    "MC":    "MC.PA",    "OR":    "OR.PA",
    "DSY":   "DSY.PA",   "SAF":   "SAF.PA",   "EDEN":  "EDEN.PA",
    "TTE":   "TTE.PA",   "BNP":   "BNP.PA",   "GLE":   "GLE.PA",
    "ACA":   "ACA.PA",   "AXA":   "CS.PA",    "SGO":   "SGO.PA",
    "VIE":   "VIE.PA",   "CAP":   "CAP.PA",   "STM":   "STM.PA",
    "SAN":   "SAN.PA",   "KER":   "KER.PA",   "RNO":   "RNO.PA",
    "PUB":   "PUB.PA",   "RI":    "RI.PA",    "BN":    "BN.PA",
    "DG":    "DG.PA",    "FP":    "FP.PA",    "ENI":   "ENI.MI",
    "AIR":   "AIR.PA",   "ALO":   "ALO.PA",   "MT":    "MT.AS",
    "NOKIA": "NOKIA.HE", "URW":   "URW.AS",   "SHL":   "SHL.DE",
    "ORA":   "ORA.PA",   "TEP":   "TEP.PA",   "VK":    "VK.PA",
    "ML":    "ML.PA",    "RXL":   "RXL.PA",   "NEXANS":"NEX.PA",
    "DBV":   "DBV.PA",   "MERY":  "MERY.PA",  "COFA":  "COFA.PA",
    "FI":    "FI.PA",    "ERF":   "ERF.PA",   "ABCA":  "ABCA.PA",
    "DASSAV":"DSY.PA",   "KZATM": "KAZ.PA",   "MLVRB": "ML.PA",
    "ALFPC": "AFP.PA",   "TRGO":  "TRI.PA",   "CLASQN":"CLAS.PA",
    "COGEFI":"CGF.PA",   "THERMD":"HMY.PA",   "MLCFT": "MLCFT.PA",
    "ALCLF": "ALCL.PA",  "RXLSA": "RXLSA.PA", "TRIGANO":"TRI.PA",
    "GBT":   "GBT.PA",   "IPSEN": "IPN.PA",   "STEF":  "STEF.PA",
    "SAFT":  "SAFT.PA",  "ESCAP": "ESCAP.PA", "THERM": "HMY.PA",
    "MLFP":  "MLFP.PA",  "INEA":  "INEA.PA",  "PRECIA":"PRECIA.PA",
    "AURES": "AURS.PA",  "METAP": "MTAP.PA",  "VRAP":  "VRAP.PA",
    "FDP":   "FDP.PA",   "MGIC":  "MGIC.PA",  "FBEL":  "FBEL.PA",
    "HCO":   "HCO.PA",   "TXNM":  "TXNM.PA",  "CROS":  "CROS.PA",
    # ETFs PEA
    "PAEEM": "PAEEM.PA", "DCAM":  "DCAM.PA",  "ESE":   "ESE.PA",
    "PTPXE": "500S.PA",  "CW8":   "CW8.PA",   "EWLD":  "EWLD.PA",
    # Macro proxies
    "GLD":   "GC=F",     "TNX":   "^TNX",
}

MACRO_TICKERS = {
    'taux10us': '^TNX',
    'or':       'GC=F',
    'dxy':      'DX-Y.NYB',
}

# Ratios à extraire automatiquement de yfinance
RATIOS_TO_UPDATE = [
    'trailingPE', 'forwardPE', 'priceToBook', 'priceToSalesTrailing12Months',
    'enterpriseToEbitda', 'returnOnEquity', 'returnOnAssets', 'profitMargins',
    'grossMargins', 'operatingMargins', 'revenueGrowth', 'earningsGrowth',
    'currentRatio', 'debtToEquity', 'dividendYield', 'trailingEps', 'forwardEps',
]

def get_price_and_volume(ticker_yahoo, symbol):
    """Récupère prix, volume et vratio"""
    try:
        t = yf.Ticker(ticker_yahoo)
        hist = t.history(period="30d")
        if len(hist) < 2:
            return None
        
        price  = round(float(hist["Close"].iloc[-1]), 2)
        vol5d  = float(hist["Volume"].iloc[-5:].mean()) if len(hist) >= 5 else 0
        vol20d = float(hist["Volume"].mean())
        vratio = round(vol5d / vol20d, 2) if vol20d > 0 else 1.0
        
        return {
            'price':  price,
            'vol5d':  int(vol5d),
            'vol20d': int(vol20d),
            'vratio': vratio,
        }
    except Exception as e:
        print(f"    ⚠️ {symbol}: {e}")
        return None

def get_fundamentals(ticker_yahoo, symbol):
    """Récupère les ratios fondamentaux mis à jour"""
    try:
        t = yf.Ticker(ticker_yahoo)
        info = t.info
        result = {}
        
        for ratio in RATIOS_TO_UPDATE:
            val = info.get(ratio)
            if val is not None and val != 0:
                # Convertir en format lisible
                if ratio in ['returnOnEquity', 'returnOnAssets', 'profitMargins',
                             'grossMargins', 'operatingMargins', 'revenueGrowth',
                             'earningsGrowth', 'dividendYield']:
                    result[ratio] = round(float(val) * 100, 1)  # En %
                else:
                    result[ratio] = round(float(val), 2)
        
        return result
    except:
        return {}

def get_macro():
    """Récupère les 3 indicateurs macro"""
    results = {}
    for field, ticker in MACRO_TICKERS.items():
        try:
            t = yf.Ticker(ticker)
            hist = t.history(period="2d")
            if len(hist) >= 1:
                results[field] = round(float(hist["Close"].iloc[-1]), 2)
        except:
            results[field] = 0
        time.sleep(0.3)
    return results

def inject_price(html, symbol, data):
    """Injecte le prix dans index.html"""
    patterns = [
        f"ticker:'{symbol}',",
        f'ticker:"{symbol}",'
    ]
    for pat in patterns:
        idx = html.find(pat)
        if idx < 0:
            continue
        
        # Injecter price
        price_pat = re.compile(r"price:\s*[\d.]+")
        end_obj = html.find('}', idx)
        obj_str = html[idx:end_obj]
        
        if 'price:' in obj_str:
            new_obj = price_pat.sub(f"price:{data['price']}", obj_str)
            html = html[:idx] + new_obj + html[end_obj:]
        
        # Injecter vratio
        vratio_pat = re.compile(r"vratio:\s*[\d.]+")
        end_obj2 = html.find('}', idx)
        obj_str2 = html[idx:end_obj2]
        
        if 'vratio:' in obj_str2:
            new_obj2 = vratio_pat.sub(f"vratio:{data['vratio']}", obj_str2)
            html = html[:idx] + new_obj2 + html[end_obj2:]
        
        return html
    
    return html

def inject_fundamentals(html, symbol, fundamentals):
    """Met à jour les ratios fondamentaux dans les données"""
    if not fundamentals:
        return html
    
    patterns = [f"ticker:'{symbol}',", f'ticker:"{symbol}",']
    for pat in patterns:
        idx = html.find(pat)
        if idx < 0:
            continue
        
        end_obj = html.find('\n}', idx)
        if end_obj < 0:
            end_obj = html.find('},', idx) + 1
        
        obj_str = html[idx:end_obj]
        
        # Mapping ratios → champs dans index.html
        mapping = {
            'trailingPE':    'pe',
            'priceToBook':   'pb',
            'returnOnEquity': 'roe',
            'grossMargins':  'marge',
            'dividendYield': 'div',
            'earningsGrowth': 'bpacroiss',
        }
        
        for ratio_key, field_name in mapping.items():
            if ratio_key in fundamentals:
                pat_field = re.compile(rf"{field_name}:\s*[\d.]+")
                if pat_field.search(obj_str):
                    new_obj = pat_field.sub(f"{field_name}:{fundamentals[ratio_key]}", obj_str)
                    html = html[:idx] + new_obj + html[end_obj:]
                    obj_str = new_obj  # Update for next iteration
        
        return html
    
    return html

def inject_macro(html, macro):
    """Injecte les données macro statiques"""
    macro_js = "var MACRO_STATIC = " + json.dumps(macro) + ";"
    if "var MACRO_STATIC" in html:
        html = re.sub(r"var MACRO_STATIC = \{[^;]*\};", macro_js, html)
    else:
        html = html.replace("var PTF_VAL_DEFAULT", macro_js + "\nvar PTF_VAL_DEFAULT", 1)
    return html

def inject_timestamp(html, nb_ok, nb_total, nb_errors):
    """Injecte le timestamp de mise à jour"""
    now = datetime.now().strftime('%d/%m %H:%M')
    ts = f"{nb_ok} cours mis à jour à {now} ({nb_errors} échecs)"
    
    if 'var UPDATE_TS=' in html:
        html = re.sub(r"var UPDATE_TS='[^']*'", f"var UPDATE_TS='{ts}'", html)
    else:
        html = html.replace("var MACRO_STATIC", f"var UPDATE_TS='{ts}';\nvar MACRO_STATIC", 1)
    
    return html

# ══════════════════════════════════════
# MAIN
# ══════════════════════════════════════
if __name__ == '__main__':
    print("=" * 60)
    print(f"VAL.PEA — Mise à jour {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"Tickers: {len(YAHOO)} | Délai: {DELAY}s | Durée estimée: ~{int(len(YAHOO)*DELAY/60)+1}min")
    print("=" * 60)

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    ok, errors, skipped = 0, 0, 0
    
    # Jour de la semaine — lundi = mise à jour des fondamentaux aussi
    is_monday = datetime.now().weekday() == 0

    print(f"\n📈 PRIX & VOLUMES ({len(YAHOO)} tickers)...")
    for symbol, ticker_yahoo in YAHOO.items():
        data = get_price_and_volume(ticker_yahoo, symbol)
        if data:
            html = inject_price(html, symbol, data)
            ok += 1
            if ok % 20 == 0:
                print(f"  ✅ {ok}/{len(YAHOO)} mis à jour...")
        else:
            errors += 1
        time.sleep(DELAY)
    
    print(f"\n✅ Prix: {ok} OK, {errors} échecs")

    # Mise à jour des fondamentaux chaque lundi (ou si < 50 prix OK)
    if is_monday:
        print(f"\n📊 RATIOS FONDAMENTAUX (lundi — mise à jour hebdo)...")
        # Mettre à jour uniquement les BPF pour commencer
        bpf_tickers = {
            'RMS': 'RMS.PA', 'AI': 'AI.PA', 'LR': 'LR.PA', 'HO': 'HO.PA',
            'SU': 'SU.PA', 'TTE': 'TTE.PA', 'EL': 'EL.PA', 'GTT': 'GTT.PA',
            'MC': 'MC.PA', 'OR': 'OR.PA', 'SAF': 'SAF.PA', 'ASML': 'ASML.AS',
            'EDEN': 'EDEN.PA', 'ELIS': 'ELIS.PA',
        }
        for symbol, ticker_yahoo in bpf_tickers.items():
            fundamentals = get_fundamentals(ticker_yahoo, symbol)
            if fundamentals:
                html = inject_fundamentals(html, symbol, fundamentals)
                print(f"  ✅ {symbol}: PE={fundamentals.get('trailingPE','?')}x, ROE={fundamentals.get('returnOnEquity','?')}%, Div={fundamentals.get('dividendYield','?')}%")
            time.sleep(0.5)

    print(f"\n🌍 INDICATEURS MACRO...")
    macro = get_macro()
    print(f"  Taux US: {macro.get('taux10us', '?')}%")
    print(f"  Or:      {macro.get('or', '?')}$")
    print(f"  Dollar:  {macro.get('dxy', '?')}")
    html = inject_macro(html, macro)
    html = inject_timestamp(html, ok, len(YAHOO), errors)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n{'='*60}")
    print(f"✅ Terminé — {ok}/{len(YAHOO)} prix, macro OK")
    if is_monday:
        print(f"✅ Ratios fondamentaux BPF mis à jour")
    print(f"{'='*60}")
