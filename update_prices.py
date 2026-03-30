#!/usr/bin/env python3
"""
VAL.PEA — Mise à jour prix via PRICES_LIVE
Injecte var PRICES_LIVE = {'AI':172.94, 'RMS':1620.5, ...}
dans index.html. Le screener applique ces prix au démarrage.
"""

import yfinance as yf
import json, re, time
from datetime import datetime

DELAY = 0.35

# ═══ PRIORITÉ 1 : Portefeuille Val + BPF ═══
P1 = {
    "AI":   "AI.PA",    "RMS":  "RMS.PA",   "SU":   "SU.PA",
    "TTE":  "TTE.PA",   "ASML": "ASML.AS",  "ELIS": "ELIS.PA",
    "GTT":  "GTT.PA",   "HO":   "HO.PA",    "LR":   "LR.PA",
    "EL":   "EL.PA",    "MC":   "MC.PA",    "OR":   "OR.PA",
    "DSY":  "DSY.PA",   "SAF":  "SAF.PA",   "EDEN": "EDEN.PA",
    "CW8":  "CW8.PA",   "EWLD": "EWLD.PA",
}

# ═══ PRIORITÉ 2 : Grade A fiables ═══
P2 = {
    "BN":   "BN.PA",    "DG":   "DG.PA",    "SGO":  "SGO.PA",
    "VIE":  "VIE.PA",   "CAP":  "CAP.PA",   "SAN":  "SAN.PA",
    "KER":  "KER.PA",   "RNO":  "RNO.PA",   "PUB":  "PUB.PA",
    "RI":   "RI.PA",    "AIR":  "AIR.PA",   "ORA":  "ORA.PA",
    "ML":   "ML.PA",    "RXL":  "RXL.PA",   "NEX":  "NEX.PA",
    "COFA": "COFA.PA",  "STM":  "STM.PA",   "BNP":  "BNP.PA",
    "GLE":  "GLE.PA",   "ACA":  "ACA.PA",   "AXA":  "CS.PA",
    "ERF":  "ERF.PA",   "FI":   "FI.PA",    "VK":   "VK.PA",
    "IPN":  "IPN.PA",   "STEF": "STEF.PA",  "ABCA": "ABCA.PA",
    "DBV":  "DBV.PA",   "MERY": "MERY.PA",  "MT":   "MT.AS",
    "NOVO": "NVO",      "TEP":  "TEP.PA",   "TECH": "TECH.PA",
}

# ═══ PRIORITÉ 3 : Reste SBF ═══
P3 = {
    "URW":  "URW.AS",  "FP":   "FP.PA",
    "ALO":  "ALO.PA",  "GBT":  "GBT.PA",
    "FDP":  "FDP.PA",  "HCO":  "HCO.PA",
}

MACRO_TICKERS = {
    'taux10us': '^TNX',
    'or':       'GC=F',
    'dxy':      'DX-Y.NYB',
}

def get_price(yahoo_tk):
    try:
        hist = yf.Ticker(yahoo_tk).history(period="5d")
        if len(hist) >= 1:
            return round(float(hist["Close"].iloc[-1]), 2)
    except:
        pass
    return None

def get_vratio(yahoo_tk):
    try:
        hist = yf.Ticker(yahoo_tk).history(period="30d")
        if len(hist) >= 5:
            v5  = float(hist["Volume"].iloc[-5:].mean())
            v20 = float(hist["Volume"].mean())
            return round(v5/v20, 2) if v20 > 0 else 1.0
    except:
        pass
    return 1.0

def get_fundamentals(yahoo_tk):
    try:
        info = yf.Ticker(yahoo_tk).info
        def pct(k): v=info.get(k); return round(float(v)*100,1) if v else None
        def num(k,r=1): v=info.get(k); return round(float(v),r) if v else None
        return {k:v for k,v in {
            'pe':    num('trailingPE'),
            'roe':   pct('returnOnEquity'),
            'marge': pct('grossMargins'),
            'div':   pct('dividendYield'),
            'h52':   num('fiftyTwoWeekHigh'),
            'l52':   num('fiftyTwoWeekLow'),
        }.items() if v is not None}
    except:
        return {}

def inject_prices_live(html, prices_dict):
    """Injecte PRICES_LIVE dans index.html de façon robuste"""
    js_obj = "var PRICES_LIVE = " + json.dumps(prices_dict, ensure_ascii=False) + ";"
    # Remplacer l'ancienne ligne PRICES_LIVE
    if "var PRICES_LIVE = {" in html:
        html = re.sub(r"var PRICES_LIVE = \{[^;]*\};", js_obj, html)
    elif "var PRICES_LIVE = {};" in html:
        html = html.replace("var PRICES_LIVE = {};", js_obj, 1)
    return html

def inject_vratio(html, ticker, vratio):
    """Injecte le vratio dans S[]"""
    pattern = f"ticker:'{ticker}'"
    idx = html.find(pattern)
    if idx < 0:
        return html
    end = html.find('\n},\n', idx)
    if end < 0: end = html.find('\n}', idx)
    if end < 0: return html
    obj = html[idx:end]
    if 'vratio:' in obj:
        new_obj = re.sub(r'vratio:\s*[\d.]+', f"vratio:{vratio}", obj)
        html = html[:idx] + new_obj + html[end:]
    return html

def inject_fundamentals(html, ticker, funds):
    """Injecte les fondamentaux dans S[]"""
    pattern = f"ticker:'{ticker}'"
    idx = html.find(pattern)
    if idx < 0:
        return html
    end = html.find('\n},\n', idx)
    if end < 0: end = html.find('\n}', idx)
    if end < 0: return html
    obj = html[idx:end]
    
    for field, val in funds.items():
        if field in ('h52', 'l52'):
            # Ces champs s'appellent b52h et b52l dans S[]
            fname = 'b52h' if field == 'h52' else 'b52l'
        else:
            fname = field
        pattern_f = re.compile(rf'\b{fname}:\s*[\d.]+')
        if pattern_f.search(obj):
            obj = pattern_f.sub(f"{fname}:{val}", obj)
    
    html = html[:idx] + obj + html[end:]
    return html

def inject_macro(html, macro):
    js = "var MACRO_STATIC = " + json.dumps(macro) + ";"
    if "var MACRO_STATIC" in html:
        html = re.sub(r"var MACRO_STATIC = \{[^;]*\};", js, html)
    else:
        html = html.replace("var PRICES_LIVE", js + "\nvar PRICES_LIVE", 1)
    return html

def inject_timestamp(html, ok, total, err):
    now = datetime.now().strftime('%d/%m %H:%M')
    ts = f"{ok} cours mis à jour à {now} ({err} échecs)"
    if "var UPDATE_TS=" in html:
        html = re.sub(r"var UPDATE_TS='[^']*'", f"var UPDATE_TS='{ts}'", html)
    else:
        html = html.replace("var PRICES_LIVE", f"var UPDATE_TS='{ts}';\nvar PRICES_LIVE", 1)
    return html

if __name__ == '__main__':
    print("=" * 60)
    print(f"VAL.PEA — {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    is_monday = datetime.now().weekday() == 0
    print(f"Mode: {'LUNDI (fondamentaux BPF inclus)' if is_monday else 'Standard'}")
    print("=" * 60)

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    prices_live = {}
    ok = err = 0

    for label, batch in [("P1 — Portefeuille+BPF", P1), 
                          ("P2 — Grade A", P2),
                          ("P3 — SBF reste", P3)]:
        print(f"\n📈 {label} ({len(batch)} tickers)...")
        for symbol, yahoo_tk in batch.items():
            price = get_price(yahoo_tk)
            if price:
                prices_live[symbol] = price
                ok += 1
                if ok % 10 == 0:
                    print(f"  ✅ {ok} OK — dernier: {symbol}={price}")
            else:
                err += 1
            time.sleep(DELAY)

    print(f"\n✅ {ok} prix récupérés, {err} échecs")

    # Injecter PRICES_LIVE (méthode robuste)
    html = inject_prices_live(html, prices_live)
    print(f"✅ PRICES_LIVE injecté ({len(prices_live)} tickers)")

    # Vratio pour les BPF (best effort)
    print(f"\n📊 Vratio BPF...")
    for symbol, yahoo_tk in list(P1.items())[:10]:
        vr = get_vratio(yahoo_tk)
        html = inject_vratio(html, symbol, vr)
        time.sleep(0.2)

    # Fondamentaux BPF chaque lundi
    if is_monday:
        print(f"\n📋 Fondamentaux BPF (lundi)...")
        for symbol, yahoo_tk in P1.items():
            funds = get_fundamentals(yahoo_tk)
            if funds:
                html = inject_fundamentals(html, symbol, funds)
                print(f"  {symbol}: h52={funds.get('h52','?')} l52={funds.get('l52','?')}")
            time.sleep(0.4)

    # Macro
    print(f"\n🌍 Macro...")
    macro = {}
    for field, tk in MACRO_TICKERS.items():
        p = get_price(tk)
        macro[field] = p or 0
        time.sleep(0.3)
    print(f"  Taux: {macro.get('taux10us')}% Or: {macro.get('or')}$ DXY: {macro.get('dxy')}")
    html = inject_macro(html, macro)
    html = inject_timestamp(html, ok, len(P1)+len(P2)+len(P3), err)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n{'='*60}")
    print(f"✅ TERMINÉ — {ok} prix dans PRICES_LIVE")
    print(f"{'='*60}")
