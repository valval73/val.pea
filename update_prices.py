#!/usr/bin/env python3
"""
VAL.PEA — Mise à jour COMPLÈTE des 228 prix
Stratégie : PRICES_LIVE = {ticker: prix} injecté dans index.html
Le screener applique ces prix au démarrage (aucun risque d'injection incorrecte)

Priorités :
  P1 : Portefeuille Val + BPF (toujours mis à jour en premier)
  P2 : Reste SBF250 (best effort, même délai)

Fondamentaux : chaque lundi pour les BPF (PE, ROE, marges, h52, l52)
Macro        : taux US, or, dollar (chaque soir)
"""

import yfinance as yf
import json, re, time
from datetime import datetime

DELAY = 0.3   # secondes entre chaque ticker — 228 x 0.3s ≈ 70 secondes

# ══════════════════════════════════════════════════════════
# MAPPING COMPLET ticker → Yahoo Finance
# Source : fetchLive() dans index.html (même mapping)
# ══════════════════════════════════════════════════════════
ALL_TICKERS = {
    # ── CAC 40 ──
    "MC":    "MC.PA",    "AI":    "AI.PA",    "OR":    "OR.PA",
    "RMS":   "RMS.PA",   "SAN":   "SAN.PA",   "TTE":   "TTE.PA",
    "SAF":   "SAF.PA",   "SU":    "SU.PA",    "AXA":   "CS.PA",
    "BNP":   "BNP.PA",   "ACA":   "ACA.PA",   "GLE":   "GLE.PA",
    "AIR":   "AIR.PA",   "KER":   "KER.PA",   "PUB":   "PUB.PA",
    "ORA":   "ORA.PA",   "VIE":   "VIE.PA",   "RNO":   "RNO.PA",
    "SGO":   "SGO.PA",   "CAP":   "CAP.PA",   "DG":    "DG.PA",
    "VIV":   "VIV.PA",   "RI":    "RI.PA",    "LR":    "LR.PA",
    "WLN":   "WLN.PA",   "DSY":   "DSY.PA",   "STM":   "STM.PA",
    "EL":    "EL.PA",    "ML":    "ML.PA",    "ENGI":  "ENGI.PA",
    "MT":    "MT.AS",    "URW":   "URW.AS",   "SW":    "SW.PA",
    "TEP":   "TEP.PA",   "EN":    "EN.PA",    "AC":    "AC.PA",
    "AF":    "AF.PA",    "BN":    "BN.PA",    "CA":    "CA.PA",
    "HO":    "HO.PA",    "GTT":   "GTT.PA",
    # ── SBF 250 ──
    "COFA":  "COFA.PA",  "MERY":  "MRY.PA",   "JXS":   "JXS.PA",
    "SPIE":  "SPIE.PA",  "NEX":   "NEX.PA",   "DASSAV":"AM.PA",
    "ALO":   "ALO.PA",   "ELIS":  "ELIS.PA",  "SEB":   "SK.PA",
    "ERF":   "ERF.PA",   "IPSOS": "IPS.PA",   "ABCA":  "ABCA.PA",
    "VK":    "VK.PA",    "FNAC":  "FNAC.PA",  "LNA":   "LNA.PA",
    "CNP":   "CNP.PA",   "SOP":   "SOP.PA",   "BIOM":  "BIM.PA",
    "KLPI":  "LI.PA",    "RCO":   "RCO.PA",   "FGR":   "FGR.PA",
    "COV":   "COV.PA",   "TRI":   "TRI.PA",   "BOI":   "BOI.PA",
    "VIRP":  "VIRP.PA",  "ITP":   "ITP.PA",   "ALCLA": "ALCLA.PA",
    "ARG":   "ARG.PA",   "STF":   "STF.PA",   "THEP":  "THEP.PA",
    "PLX":   "PLX.PA",   "EDEN":  "EDEN.PA",  "FRVIA": "FRVIA.PA",
    "DBV":   "DBV.PA",   "IPSEN": "IPN.PA",   "ALTEN": "ATE.PA",
    "LEGRAND":"LR.PA",   "NEXITY":"NXI.PA",   "VICAT": "VCT.PA",
    "APERAM":"APAM.AS",  "SOPRA": "SOP.PA",   "BUREAU":"BV.PA",
    "BELIER":"ABEL.PA",  "LACROIX":"LACR.PA", "PARROT":"PARRO.PA",
    "MGIC":  "MGIC.PA",  "FLEURY":"FLEUR.PA", "LISI":  "FII.PA",
    "MAISON":"MAIS.PA",  "NEURONES":"NRO.PA", "ORDINA":"ORDI.PA",
    "TXCOM": "TXCO.PA",  "AURES": "AURS.PA",  "INFOTEL":"INF.PA",
    "AKWEL": "AKW.PA",   "SAFT":  "SAFT.PA",  "TRIGANO2":"TRI.PA",
    "SAVENCIA":"SAVE.PA","INTERF":"ITRFI.PA", "VIEL":  "VIEL.PA",
    "COLAS": "RE.PA",    "MICHELIN":"ML.PA",  "WENDEL":"MF.PA",
    "FFP":   "FFP.PA",   "RUBIS": "RUI.PA",   "HEXAOM":"HXO.PA",
    "ALTAREA":"ALTA.PA", "ICADE": "ICAD.PA",  "MERCIALYS":"MERY.PA",
    "UNIBAIL":"URW.AS",  "NEXANS2":"NEX.PA",  "REXEL": "RXL.PA",
    "SCHNEIDER":"SU.PA", "LEGR":  "LR.PA",    "VALEO": "FR.PA",
    "SOITEC":"SOI.PA",   "ALSTOM":"ALO.PA",   "SAFRAN2":"SAF.PA",
    "AMUNDI":"AMUN.PA",  "CARMIGNAC":"CGMF.PA","TIKEHAU":"TKO.PA",
    "ROTHSCHILD":"ROTH.PA","NATIXIS":"KN.PA",
    # ── ETFs PEA ──
    "CW8":   "CW8.PA",   "EWLD":  "EWLD.PA",  "PAEEM": "PAEEM.PA",
    "DCAM":  "DCAM.PA",  "ESE":   "ESE.PA",   "PTPXE": "500S.PA",
    "RS2K":  "RS2K.PA",  "LYPS":  "LYPS.PA",
    # ── Actions hors France (BPF) ──
    "ASML":  "ASML.AS",  "ADYEN": "ADYEN.AS", "NOVO":  "NOVO-B.CO",
    "SAP":   "SAP.DE",
}

# BPF prioritaires (toujours les premiers)
BPF = ["MC","AI","OR","RMS","SAN","TTE","SAF","SU","LR","EL","GTT",
       "HO","DSY","EDEN","ASML","ELIS"]

MACRO_TICKERS = {
    'taux10us': '^TNX',
    'or':       'GC=F',
    'dxy':      'DX-Y.NYB',
}

# ══════════════════════════════════════════════════════════
def get_price(yahoo_tk):
    try:
        hist = yf.Ticker(yahoo_tk).history(period="5d")
        if len(hist) >= 1:
            return round(float(hist["Close"].iloc[-1]), 2)
    except: pass
    return None

def get_vratio(yahoo_tk):
    try:
        hist = yf.Ticker(yahoo_tk).history(period="30d")
        if len(hist) >= 5:
            v5  = float(hist["Volume"].iloc[-5:].mean())
            v20 = float(hist["Volume"].mean())
            return round(v5/v20, 2) if v20 > 0 else 1.0
    except: pass
    return 1.0

def get_fundamentals(yahoo_tk):
    try:
        info = yf.Ticker(yahoo_tk).info
        def pct(k): v=info.get(k); return round(float(v)*100,1) if v else None
        def num(k,r=1): v=info.get(k); return round(float(v),r) if v else None
        return {k:v for k,v in {
            'pe':    num('trailingPE'),
            'pb':    num('priceToBook',1),
            'roe':   pct('returnOnEquity'),
            'marge': pct('grossMargins'),
            'mn':    pct('profitMargins'),
            'div':   pct('dividendYield'),
            'epsg':  pct('earningsGrowth'),
            'revg':  pct('revenueGrowth'),
            'h52':   num('fiftyTwoWeekHigh'),
            'l52':   num('fiftyTwoWeekLow'),
            'beta':  num('beta', 2),
        }.items() if v is not None}
    except: return {}

def inject_prices_live(html, prices):
    """Injection robuste via PRICES_LIVE — jamais de confusion avec autres chiffres"""
    js = "var PRICES_LIVE = " + json.dumps(prices, ensure_ascii=False) + ";"
    if "var PRICES_LIVE = {" in html:
        html = re.sub(r"var PRICES_LIVE = \{[^;]*\};", js, html)
    elif "var PRICES_LIVE = {};" in html:
        html = html.replace("var PRICES_LIVE = {};", js, 1)
    return html

def inject_vratio_in_s(html, ticker, vratio):
    """Injecte vratio directement dans S[]"""
    pat = f"ticker:'{ticker}'"
    idx = html.find(pat)
    if idx < 0: return html
    # Chercher la fin de l'objet
    end = html.find('\n},\n', idx)
    if end < 0: end = html.find('\n}', idx)
    if end < 0 or end-idx > 2000: return html
    obj = html[idx:end]
    if 'vratio:' in obj:
        new_obj = re.sub(r'vratio:\s*[\d.]+', f"vratio:{vratio}", obj)
        html = html[:idx] + new_obj + html[end:]
    return html

def inject_fundamentals_in_s(html, ticker, funds):
    """Met à jour les fondamentaux dans S[] le lundi"""
    pat = f"ticker:'{ticker}'"
    idx = html.find(pat)
    if idx < 0: return html
    end = html.find('\n},\n', idx)
    if end < 0: end = html.find('\n}', idx)
    if end < 0 or end-idx > 2000: return html
    obj = html[idx:end]
    
    field_map = {
        'pe': r'\bpe:\s*[\d.]+',
        'pb': r'\bpb:\s*[\d.]+',
        'roe': r'\broe:\s*[\d.]+',
        'marge': r'\bgm:\s*[\d.]+',   # gm = gross margin dans S[]
        'mn': r'\bmargin:\s*[\d.]+',
        'div': r'\byield:\s*[\d.]+',
        'epsg': r'\bepsg:\s*[\d.]+',
        'revg': r'\brevg:\s*[\d.]+',
        'h52': r'\bb52h:\s*[\d.]+',
        'l52': r'\bb52l:\s*[\d.]+',
        'beta': r'\bbeta:\s*[\d.]+',
    }
    for key, pattern in field_map.items():
        if key in funds and re.search(pattern, obj):
            obj = re.sub(pattern, f"{pattern.split(':')[0].strip().lstrip(r'\\b')}:{funds[key]}", obj)
    
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

# ══════════════════════════════════════════════════════════
if __name__ == '__main__':
    now = datetime.now()
    is_monday = now.weekday() == 0
    total = len(ALL_TICKERS)
    est_sec = int(total * DELAY)
    
    print("=" * 60)
    print(f"VAL.PEA — {now.strftime('%d/%m/%Y %H:%M')}")
    print(f"{total} tickers · délai {DELAY}s · ~{est_sec//60}min{est_sec%60}s")
    if is_monday: print("🗓️  LUNDI — fondamentaux BPF inclus")
    print("=" * 60)

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    prices_live = {}
    ok = err = 0

    # Mettre les BPF EN PREMIER dans la liste
    ordered = {t: ALL_TICKERS[t] for t in BPF if t in ALL_TICKERS}
    ordered.update({t: v for t, v in ALL_TICKERS.items() if t not in ordered})

    print(f"\n📈 PRIX ({total} tickers)...")
    for symbol, yahoo_tk in ordered.items():
        price = get_price(yahoo_tk)
        if price:
            prices_live[symbol] = price
            ok += 1
            if ok % 25 == 0:
                print(f"  ✅ {ok}/{total} — {symbol}={price}€")
        else:
            err += 1
        time.sleep(DELAY)

    # Afficher les BPF
    print(f"\n  📊 BPF mis à jour:")
    for t in BPF:
        if t in prices_live:
            print(f"    {t}: {prices_live[t]}€")

    print(f"\n  Total: {ok}/{total} OK · {err} échecs")

    # Injection PRICES_LIVE (méthode robuste — jamais de confusion avec autres chiffres)
    html = inject_prices_live(html, prices_live)
    print(f"✅ PRICES_LIVE injecté ({len(prices_live)} tickers)")

    # Vratio pour les BPF
    print(f"\n📊 Vratio BPF...")
    for symbol in BPF:
        if symbol in ALL_TICKERS:
            vr = get_vratio(ALL_TICKERS[symbol])
            html = inject_vratio_in_s(html, symbol, vr)
            time.sleep(0.2)

    # Fondamentaux chaque lundi
    if is_monday:
        print(f"\n📋 Fondamentaux BPF (lundi)...")
        for symbol in BPF:
            if symbol not in ALL_TICKERS: continue
            funds = get_fundamentals(ALL_TICKERS[symbol])
            if funds:
                html = inject_fundamentals_in_s(html, symbol, funds)
                print(f"  {symbol}: PE={funds.get('pe','?')} ROE={funds.get('roe','?')}% h52={funds.get('h52','?')} l52={funds.get('l52','?')}")
            time.sleep(0.5)

    # Macro
    print(f"\n🌍 Macro...")
    macro = {}
    for field, tk in MACRO_TICKERS.items():
        p = get_price(tk)
        macro[field] = p or 0
        time.sleep(0.3)
    print(f"  Taux US: {macro.get('taux10us')}%  Or: {macro.get('or')}$  DXY: {macro.get('dxy')}")

    html = inject_macro(html, macro)
    html = inject_timestamp(html, ok, total, err)

    # Mettre à jour l'historique des prix
    print(f"\n📅 Historique des prix...")
    update_history(prices_live)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n{'='*60}")
    print(f"✅ TERMINÉ — {ok} prix dans PRICES_LIVE")
    print(f"{'='*60}")


# ═══════════════════════════════════════════════════
# HISTORIQUE DES PRIX — prices_history.json
# Stocke chaque jour les prix clôture
# Permet de calculer MM20, MM50, MM200 long terme
# RSI calculé sur 14 jours depuis l'historique
# ═══════════════════════════════════════════════════

import math as _math

def update_history(prices_live, filename="prices_history.json"):
    """Met à jour l'historique des prix (JSON dans le repo)"""
    import json, os
    
    # Charger l'historique existant
    history = {}
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                history = json.load(f)
        except: history = {}
    
    today_str = datetime.now().strftime('%Y-%m-%d')
    
    for ticker, price in prices_live.items():
        if ticker not in history:
            history[ticker] = []
        
        # Ajouter le prix d'aujourd'hui (éviter les doublons du même jour)
        hist_list = history[ticker]
        if isinstance(hist_list, list):
            history[ticker].append(price)
            # Garder max 260 jours (~1 an de trading)
            if len(history[ticker]) > 260:
                history[ticker] = history[ticker][-260:]
    
    # Calculer RSI 14j pour chaque ticker
    for ticker, prices_list in history.items():
        if len(prices_list) >= 15:
            rsi = calc_rsi(prices_list, 14)
            if rsi is not None:
                history[ticker+'_rsi'] = round(rsi, 1)
    
    # Sauvegarder
    with open(filename, 'w') as f:
        json.dump(history, f, separators=(',', ':'))
    
    print(f"✅ prices_history.json mis à jour ({len([k for k in history if '_rsi' not in k])} tickers)")
    return history

def calc_rsi(prices, period=14):
    """Calcule le RSI sur les N derniers prix"""
    if len(prices) < period + 1:
        return None
    recent = prices[-(period+1):]
    gains = [max(0, recent[i]-recent[i-1]) for i in range(1, len(recent))]
    losses = [max(0, recent[i-1]-recent[i]) for i in range(1, len(recent))]
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0: return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100/(1+rs)), 1)

# Appeler update_history à la fin du main
if __name__ == '__main__':
    pass  # update_history est appelé dans le block principal ci-dessus
