#!/usr/bin/env python3
"""
VAL.PEA — Mise à jour automatique
Priorité 1 : Portefeuille Val (14 positions) + BPF
Priorité 2 : Actions Grade A du screener  
Priorité 3 : Reste SBF250 (best effort)
Ratios fondamentaux : chaque lundi pour les BPF
"""

import yfinance as yf
import json, re, time, os
from datetime import datetime

DELAY_FAST  = 0.3   # Entre les prix (priorité 1 & 2)
DELAY_SLOW  = 0.5   # Entre les fondamentaux

# ═══════════════════════════════════════════
# PRIORITÉ 1 — Portefeuille Val + BPF
# Ces tickers sont TOUJOURS mis à jour en premier
# ═══════════════════════════════════════════
PRIORITY_1 = {
    # Portefeuille Val actuel
    "AI":    "AI.PA",
    "RMS":   "RMS.PA",
    "SU":    "SU.PA",
    "TTE":   "TTE.PA",
    "ASML":  "ASML.AS",
    "ELIS":  "ELIS.PA",
    "GTT":   "GTT.PA",
    "HO":    "HO.PA",
    "LR":    "LR.PA",
    "EL":    "EL.PA",
    "DCAM":  "0P0000X5MB.F",
    "PAEEM": "0P0000MATV.F",
    "ESE":   "0P0001FBMQ.F",
    "PTPXE": "0P0001LJQR.F",
    # BPF supplémentaires
    "MC":    "MC.PA",
    "OR":    "OR.PA",
    "DSY":   "DSY.PA",
    "SAF":   "SAF.PA",
    "EDEN":  "EDEN.PA",
    "CW8":   "CW8.PA",
}

# ═══════════════════════════════════════════
# PRIORITÉ 2 — Grade A fiables (tickers vérifiés)
# ═══════════════════════════════════════════
PRIORITY_2 = {
    "BN":    "BN.PA",
    "DG":    "DG.PA",
    "SGO":   "SGO.PA",
    "VIE":   "VIE.PA",
    "CAP":   "CAP.PA",
    "SAN":   "SAN.PA",
    "KER":   "KER.PA",
    "RNO":   "RNO.PA",
    "PUB":   "PUB.PA",
    "RI":    "RI.PA",
    "AIR":   "AIR.PA",
    "ORA":   "ORA.PA",
    "TEP":   "TEF.PA",
    "ML":    "ML.PA",
    "RXL":   "RXL.PA",
    "NEX":   "NEX.PA",
    "COFA":  "COFA.PA",
    "STM":   "STM.PA",
    "BNP":   "BNP.PA",
    "GLE":   "GLE.PA",
    "ACA":   "ACA.PA",
    "AXA":   "CS.PA",
    "MT":    "MT.AS",
    "ERF":   "ERF.PA",
    "FI":    "FI.PA",
    "VK":    "VK.PA",
    "NOKIA": "NOKIA.HE",
    "TRI":   "TRI.PA",
    "IPN":   "IPN.PA",
    "HMY":   "HMY.PA",
    "STEF":  "STEF.PA",
    "ABCA":  "ABCA.PA",
    "DBV":   "DBV.PA",
    "MERY":  "MERY.PA",
}

# ═══════════════════════════════════════════
# PRIORITÉ 3 — Reste SBF250 (best effort)
# ═══════════════════════════════════════════
PRIORITY_3 = {
    "URW":   "URW.AS",
    "FP":    "FP.PA",
    "ENI":   "ENI.MI",
    "SHL":   "SHL.DE",
    "ALO":   "ALO.PA",
    "SAFT":  "SAFT.PA",
    "GBT":   "GBT.PA",
    "INEA":  "INEA.PA",
    "CROS":  "CROS.PA",
    "FDP":   "FDP.PA",
    "HCO":   "HCO.PA",
}

# Macro
MACRO_TICKERS = {
    'taux10us': '^TNX',
    'or':       'GC=F',
    'dxy':      'DX-Y.NYB',
}

def get_price_and_vratio(ticker_yahoo, symbol):
    """Récupère prix + vratio. Retourne None si délisted."""
    try:
        t = yf.Ticker(ticker_yahoo)
        hist = t.history(period="30d")
        if len(hist) < 2:
            return None
        price  = round(float(hist["Close"].iloc[-1]), 2)
        vol5   = float(hist["Volume"].iloc[-5:].mean()) if len(hist) >= 5 else 0
        vol20  = float(hist["Volume"].mean())
        vratio = round(vol5 / vol20, 2) if vol20 > 0 else 1.0
        return {'price': price, 'vratio': vratio}
    except Exception as e:
        msg = str(e)
        if 'delisted' not in msg.lower():
            print(f"    ⚠️  {symbol}: {msg[:60]}")
        return None

def get_fundamentals(ticker_yahoo, symbol):
    """Ratios fondamentaux via yfinance.info"""
    try:
        info = yf.Ticker(ticker_yahoo).info
        def pct(k): 
            v = info.get(k)
            return round(float(v)*100, 1) if v else None
        def val(k, r=2):
            v = info.get(k)
            return round(float(v), r) if v else None
        result = {
            'pe':       val('trailingPE', 1),
            'pb':       val('priceToBook', 1),
            'roe':      pct('returnOnEquity'),
            'roa':      pct('returnOnAssets'),
            'marge':    pct('grossMargins'),
            'mn':       pct('profitMargins'),
            'div':      pct('dividendYield'),
            'bpacrois': pct('earningsGrowth'),
            'cacrois':  pct('revenueGrowth'),
            'eps':      val('trailingEps'),
            'epsf':     val('forwardEps'),
        }
        # Supprimer les None
        return {k: v for k, v in result.items() if v is not None}
    except Exception as e:
        print(f"    ⚠️  Fondamentaux {symbol}: {str(e)[:60]}")
        return {}

def inject_price(html, symbol, data):
    """Injecte price + vratio dans le JS."""
    for pat in [f"ticker:'{symbol}',", f'ticker:"{symbol}",']:
        idx = html.find(pat)
        if idx < 0: continue
        end = html.find('\n},', idx)
        if end < 0: end = html.find('\n}', idx)
        if end < 0: continue
        obj = html[idx:end]
        if 'price:' in obj:
            obj = re.sub(r'price:\s*[\d.]+', f"price:{data['price']}", obj)
        if 'vratio:' in obj:
            obj = re.sub(r'vratio:\s*[\d.]+', f"vratio:{data['vratio']}", obj)
        html = html[:idx] + obj + html[end:]
        return html
    return html

def inject_fundamentals(html, symbol, funds):
    """Met à jour PE, ROE, marges dans le JS."""
    if not funds: return html
    mapping = {
        'pe':    r'pe:\s*[\d.]+',
        'pb':    r'pb:\s*[\d.]+',
        'roe':   r'roe:\s*[\d.]+',
        'marge': r'marge:\s*[\d.]+',
        'div':   r'div:\s*[\d.]+',
    }
    for pat in [f"ticker:'{symbol}',", f'ticker:"{symbol}",']: 
        idx = html.find(pat)
        if idx < 0: continue
        end = html.find('\n},', idx)
        if end < 0: end = html.find('\n}', idx)
        if end < 0: continue
        obj = html[idx:end]
        for field, regex in mapping.items():
            if field in funds and re.search(regex, obj):
                obj = re.sub(regex, f"{field}:{funds[field]}", obj)
        html = html[:idx] + obj + html[end:]
        return html
    return html

def inject_macro(html, macro):
    js = "var MACRO_STATIC = " + json.dumps(macro) + ";"
    if "var MACRO_STATIC" in html:
        html = re.sub(r"var MACRO_STATIC = \{[^;]*\};", js, html)
    else:
        html = html.replace("var PTF_VAL_DEFAULT", js + "\nvar PTF_VAL_DEFAULT", 1)
    return html

def inject_timestamp(html, ok, total, err):
    now = datetime.now().strftime('%d/%m %H:%M')
    ts = f"{ok} cours mis à jour à {now} ({err} échecs)"
    if "var UPDATE_TS=" in html:
        html = re.sub(r"var UPDATE_TS='[^']*'", f"var UPDATE_TS='{ts}'", html)
    else:
        html = html.replace("var MACRO_STATIC", f"var UPDATE_TS='{ts}';\nvar MACRO_STATIC", 1)
    return html

def update_batch(html, tickers, label, delay, do_fundamentals=False):
    ok = err = 0
    for symbol, yahoo_tk in tickers.items():
        data = get_price_and_vratio(yahoo_tk, symbol)
        if data:
            html = inject_price(html, symbol, data)
            ok += 1
            if do_fundamentals:
                time.sleep(0.2)
                funds = get_fundamentals(yahoo_tk, symbol)
                if funds:
                    html = inject_fundamentals(html, symbol, funds)
                    roe = funds.get('roe', '?')
                    pe  = funds.get('pe', '?')
                    div = funds.get('div', '?')
                    print(f"  📊 {symbol}: PE={pe}x ROE={roe}% Div={div}%")
        else:
            err += 1
        time.sleep(delay)
    print(f"  {label}: {ok} OK, {err} échecs")
    return html, ok, err

# ══════════════════════════════════════
# MAIN
# ══════════════════════════════════════
if __name__ == '__main__':
    print("=" * 60)
    print(f"VAL.PEA — {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    is_monday = datetime.now().weekday() == 0
    total_tickers = len(PRIORITY_1) + len(PRIORITY_2) + len(PRIORITY_3)
    est_min = int(total_tickers * DELAY_FAST / 60) + 1
    print(f"Tickers: {total_tickers} | Estimé: ~{est_min} min")
    if is_monday:
        print("🗓️  LUNDI — Mise à jour des fondamentaux BPF incluse")
    print("=" * 60)

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    total_ok = total_err = 0

    # ── P1 : Portefeuille + BPF (fondamentaux si lundi) ──
    print(f"\n🎯 PRIORITÉ 1 — Portefeuille & BPF ({len(PRIORITY_1)} tickers)...")
    html, ok, err = update_batch(html, PRIORITY_1, "P1", DELAY_FAST, do_fundamentals=is_monday)
    total_ok += ok; total_err += err

    # ── P2 : Grade A ──
    print(f"\n📈 PRIORITÉ 2 — Grade A ({len(PRIORITY_2)} tickers)...")
    html, ok, err = update_batch(html, PRIORITY_2, "P2", DELAY_FAST)
    total_ok += ok; total_err += err

    # ── P3 : Reste SBF250 (best effort) ──
    print(f"\n📋 PRIORITÉ 3 — SBF250 reste ({len(PRIORITY_3)} tickers)...")
    html, ok, err = update_batch(html, PRIORITY_3, "P3", DELAY_FAST)
    total_ok += ok; total_err += err

    # ── MACRO ──
    print(f"\n🌍 MACRO...")
    macro = {}
    for field, tk in MACRO_TICKERS.items():
        try:
            hist = yf.Ticker(tk).history(period="2d")
            if len(hist) >= 1:
                macro[field] = round(float(hist["Close"].iloc[-1]), 2)
        except: macro[field] = 0
        time.sleep(0.3)
    print(f"  Taux US: {macro.get('taux10us','?')}%  Or: {macro.get('or','?')}$  DXY: {macro.get('dxy','?')}")
    html = inject_macro(html, macro)
    html = inject_timestamp(html, total_ok, total_tickers, total_err)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n{'='*60}")
    print(f"✅ TERMINÉ — {total_ok}/{total_tickers} prix · {total_err} échecs")
    print(f"{'='*60}")
