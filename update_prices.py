#!/usr/bin/env python3
"""
VAL.PEA — Mise à jour COMPLÈTE des prix
Délai 0.8s · 3 vagues · Retry automatique
"""

import yfinance as yf
import json, re, time, os
from datetime import datetime

DELAY       = 0.8
DELAY_RETRY = 1.5

# ════════════════════════════════════════════════════
# VAGUE 1 — BPF + Portefeuille Val (garantis)
# ════════════════════════════════════════════════════
VAGUE_1 = {
    "AI":    "AI.PA",    "RMS":   "RMS.PA",   "SU":    "SU.PA",
    "TTE":   "TTE.PA",   "ASML":  "ASML.AS",  "ELIS":  "ELIS.PA",
    "GTT":   "GTT.PA",   "HO":    "HO.PA",    "LR":    "LR.PA",
    "EL":    "EL.PA",    "MC":    "MC.PA",    "OR":    "OR.PA",
    "DSY":   "DSY.PA",   "SAF":   "SAF.PA",   "EDEN":  "EDEN.PA",
    "CW8":   "CW8.PA",   "EWLD":  "EWLD.PA",  "DCAM":  "DCAM.PA",
    "PAEEM": "PAEEM.PA", "ESE":   "ESE.PA",   "RS2K":  "RS2K.PA",
}

# ════════════════════════════════════════════════════
# VAGUE 2 — CAC40 + Grade A/B (tickers vérifiés)
# ════════════════════════════════════════════════════
VAGUE_2 = {
    "SAN":   "SAN.PA",   "AXA":   "CS.PA",    "BNP":   "BNP.PA",
    "ACA":   "ACA.PA",   "GLE":   "GLE.PA",   "AIR":   "AIR.PA",
    "KER":   "KER.PA",   "PUB":   "PUB.PA",   "ORA":   "ORA.PA",
    "VIE":   "VIE.PA",   "RNO":   "RNO.PA",   "SGO":   "SGO.PA",
    "CAP":   "CAP.PA",   "DG":    "DG.PA",    "VIV":   "VIV.PA",
    "RI":    "RI.PA",    "WLN":   "WLN.PA",   "ML":    "ML.PA",
    "ENGI":  "ENGI.PA",  "MT":    "MT.AS",    "SW":    "SW.PA",
    "TEP":   "TEP.PA",   "EN":    "EN.PA",    "AC":    "AC.PA",
    "AF":    "AF.PA",    "BN":    "BN.PA",    "CA":    "CA.PA",
    "COFA":  "COFA.PA",  "SPIE":  "SPIE.PA",  "NEX":   "NEX.PA",
    "ALO":   "ALO.PA",   "ERF":   "ERF.PA",   "ABCA":  "ABCA.PA",
    "VK":    "VK.PA",    "IPN":   "IPN.PA",   "FGR":   "FGR.PA",
    "TRI":   "TRI.PA",   "PLX":   "PLX.PA",   "STF":   "STF.PA",
    "BOI":   "BOI.PA",   "ITP":   "ITP.PA",   "ARG":   "ARG.PA",
    "AMUN":  "AMUN.PA",  "TKO":   "TKO.PA",   "RXL":   "RXL.PA",
    "SOI":   "SOI.PA",   "DBV":   "DBV.PA",   "ATE":   "ATE.PA",
    "NXI":   "NXI.PA",   "FII":   "FII.PA",   "NRO":   "NRO.PA",
    "SAFT":  "SAFT.PA",  "SAVE":  "SAVE.PA",  "RUI":   "RUI.PA",
    "ICAD":  "ICAD.PA",  "VIRP":  "VIRP.PA",  "ALCLA": "ALCLA.PA",
    "IPS":   "IPS.PA",   "ADYEN": "ADYEN.AS", "NOVO":  "NOVO-B.CO",
    "SAP":   "SAP.DE",   "HEIA":  "HEIA.AS",  "ALV":   "ALV.DE",
    "PRX":   "PRX.AS",   "APAM":  "APAM.AS",  "NEX2":  "NEX.PA",
    "AM":    "AM.PA",    "LI":    "LI.PA",    "ALTA":  "ALTA.PA",
    "NK":    "NK.PA",    "ELIOR": "ELIOR.PA",
}

# ════════════════════════════════════════════════════
# VAGUE 3 — Reste SBF250 (codes vérifiés uniquement)
# Supprimés : ESKR, LDLC, POM, SIPH, FLEUR, MAIS,
# TXCO, AURS, MGIC, LPF, GALIM, NEOEN, PRECIA, JXS,
# ROTH, FFP, HXO, VIEL, MRY — codes invalides Yahoo
# ════════════════════════════════════════════════════
VAGUE_3 = {
    "LNA":   "LNA.PA",   "SOP":   "SOP.PA",
    "COV":   "COV.PA",   "FNAC":  "FNAC.PA",
    "BIOM":  "BIM.PA",   "RCO":   "RCO.PA",
    "SEB":   "SK.PA",    "STM":   "STM.PA",
    "FRVIA": "FRVIA.PA", "WLN3":  "WLN.PA",
    "EMEIS": "EMEIS.PA", "ATO":   "ATO.PA",
    "DBG":   "DBG.PA",   "FREY":  "FREY.PA",
    "WAGA":  "WAGA.PA",  "LSS":   "LSS.PA",
    "VRLA":  "VRLA.PA",  "LACR":  "LACR.PA",
}

BPF = ["AI","RMS","SU","TTE","ASML","ELIS","GTT","HO",
       "LR","EL","MC","OR","DSY","SAF","EDEN","CW8"]

MACRO_TICKERS = {
    'taux10us': '^TNX',
    'or':       'GC=F',
    'dxy':      'DX-Y.NYB',
}

# ════════════════════════════════════════════════════
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
            return round(v5 / v20, 2) if v20 > 0 else 1.0
    except: pass
    return 1.0

def get_fundamentals(yahoo_tk):
    try:
        info = yf.Ticker(yahoo_tk).info
        def pct(k):
            v = info.get(k)
            return round(float(v) * 100, 1) if v else None
        def num(k, r=1):
            v = info.get(k)
            return round(float(v), r) if v else None
        result = {
            'pe':     num('trailingPE'),
            'pb':     num('priceToBook', 1),
            'roe':    pct('returnOnEquity'),
            'gm':     pct('grossMargins'),
            'margin': pct('profitMargins'),
            'yield':  pct('dividendYield'),
            'epsg':   pct('earningsGrowth'),
            'revg':   pct('revenueGrowth'),
            'b52h':   num('fiftyTwoWeekHigh'),
            'b52l':   num('fiftyTwoWeekLow'),
            'beta':   num('beta', 2),
        }
        return {k: v for k, v in result.items() if v is not None}
    except: return {}

def get_fear_greed():
    try:
        import urllib.request
        url = 'https://api.alternative.me/fng/?limit=1&format=json'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            val = int(data['data'][0]['value'])
            label = data['data'][0]['value_classification']
            print("  Fear & Greed: " + str(val) + "/100 (" + label + ")")
            return val
    except Exception as e:
        print("  Fear & Greed indisponible: " + str(e)[:50])
        return None

def get_cac40_ytd():
    try:
        start_year = str(datetime.now().year) + '-01-01'
        hist = yf.Ticker('^FCHI').history(start=start_year)
        if len(hist) >= 2:
            ytd = round((float(hist['Close'].iloc[-1]) - float(hist['Close'].iloc[0])) /
                        float(hist['Close'].iloc[0]) * 100, 1)
            print("  CAC40 YTD: " + ('+' if ytd >= 0 else '') + str(ytd) + "%")
            return ytd
    except Exception as e:
        print("  CAC40 YTD indisponible: " + str(e)[:50])
    return None

def send_telegram(token, chat_id, message):
    if not token or not chat_id: return
    try:
        import urllib.request, urllib.parse
        url = 'https://api.telegram.org/bot' + token + '/sendMessage'
        data = urllib.parse.urlencode({
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }).encode()
        urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=10)
        print("  Telegram envoye")
    except Exception as e:
        print("  Telegram: " + str(e)[:50])

def fetch_vague(tickers_dict, label, delay, prices_live):
    ok = err = 0
    failed = {}
    total = len(tickers_dict)
    for symbol, yahoo_tk in tickers_dict.items():
        price = get_price(yahoo_tk)
        if price:
            prices_live[symbol] = price
            ok += 1
            if ok % 20 == 0:
                print("  " + label + " : " + str(ok) + "/" + str(total) +
                      " — " + symbol + "=" + str(price))
        else:
            failed[symbol] = yahoo_tk
            err += 1
        time.sleep(delay)
    print("  " + label + " : " + str(ok) + " OK · " + str(err) + " echecs")
    return failed

def retry_failed(failed_dict, prices_live):
    if not failed_dict: return
    print("  Retry " + str(len(failed_dict)) + " tickers...")
    ok = 0
    for symbol, yahoo_tk in failed_dict.items():
        price = get_price(yahoo_tk)
        if price:
            prices_live[symbol] = price
            ok += 1
        time.sleep(DELAY_RETRY)
    print("  Retry : " + str(ok) + "/" + str(len(failed_dict)) + " recuperes")

def inject_prices_live(html, prices):
    js = "var PRICES_LIVE = " + json.dumps(prices, ensure_ascii=False) + ";"
    if "var PRICES_LIVE = {" in html:
        html = re.sub(r"var PRICES_LIVE = \{[^;]*\};", js, html)
    elif "var PRICES_LIVE = {};" in html:
        html = html.replace("var PRICES_LIVE = {};", js, 1)
    return html

def inject_vratio_in_s(html, ticker, vratio):
    pat = "ticker:'" + ticker + "'"
    idx = html.find(pat)
    if idx < 0: return html
    end = html.find('\n},\n', idx)
    if end < 0: end = html.find('\n}', idx)
    if end < 0 or end - idx > 2000: return html
    obj = html[idx:end]
    if 'vratio:' in obj:
        new_obj = re.sub(r'vratio:\s*[\d.]+', 'vratio:' + str(vratio), obj)
        html = html[:idx] + new_obj + html[end:]
    return html

def inject_fundamentals_in_s(html, ticker, funds):
    pat = "ticker:'" + ticker + "'"
    idx = html.find(pat)
    if idx < 0: return html
    end = html.find('\n},\n', idx)
    if end < 0: end = html.find('\n}', idx)
    if end < 0 or end - idx > 2000: return html
    obj = html[idx:end]
    field_map = {
        'pe':'pe','pb':'pb','roe':'roe','gm':'gm',
        'margin':'margin','yield':'yield','epsg':'epsg',
        'revg':'revg','b52h':'b52h','b52l':'b52l','beta':'beta',
    }
    for yf_key, s_field in field_map.items():
        if yf_key not in funds: continue
        pattern = r'\b' + s_field + r':\s*[\d.]+'
        replacement = s_field + ':' + str(funds[yf_key])
        if re.search(pattern, obj):
            obj = re.sub(pattern, replacement, obj)
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
    ts = str(ok) + " cours mis a jour a " + now + " (" + str(err) + " echecs)"
    if "var UPDATE_TS=" in html:
        html = re.sub(r"var UPDATE_TS='[^']*'", "var UPDATE_TS='" + ts + "'", html)
    else:
        html = html.replace("var PRICES_LIVE",
                            "var UPDATE_TS='" + ts + "';\nvar PRICES_LIVE", 1)
    return html

def calc_rsi(prices, period=14):
    if len(prices) < period + 1: return None
    recent = prices[-(period + 1):]
    gains  = [max(0.0, recent[i] - recent[i-1]) for i in range(1, len(recent))]
    losses = [max(0.0, recent[i-1] - recent[i]) for i in range(1, len(recent))]
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0: return 100.0
    return round(100 - (100 / (1 + avg_gain / avg_loss)), 1)

def update_history(prices_live, filename="prices_history.json"):
    history = {}
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                history = json.load(f)
        except: history = {}
    for ticker, price in prices_live.items():
        key = str(ticker)
        if key not in history: history[key] = []
        history[key].append(float(price))
        if len(history[key]) > 260:
            history[key] = history[key][-260:]
    for ticker in list(history.keys()):
        if ticker.endswith('_rsi'): continue
        rsi = calc_rsi(history[ticker], 14)
        if rsi is not None:
            history[ticker + '_rsi'] = rsi
    with open(filename, 'w') as f:
        json.dump(history, f, separators=(',', ':'))
    nb = len([k for k in history if not k.endswith('_rsi')])
    print("  prices_history.json : " + str(nb) + " tickers")

# ════════════════════════════════════════════════════
if __name__ == '__main__':
    start = datetime.now()
    is_monday = start.weekday() == 0
    total = len(VAGUE_1) + len(VAGUE_2) + len(VAGUE_3)
    est = int(total * DELAY / 60)

    print("=" * 60)
    print("VAL.PEA — " + start.strftime('%d/%m/%Y %H:%M'))
    print(str(total) + " tickers · " + str(DELAY) + "s · ~" + str(est) + "min")
    if is_monday: print("LUNDI — fondamentaux BPF inclus")
    print("=" * 60)

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    prices_live = {}
    failed_all  = {}

    print("\nVAGUE 1 — BPF & Portefeuille (" + str(len(VAGUE_1)) + ")")
    failed_all.update(fetch_vague(VAGUE_1, "V1", DELAY, prices_live))

    print("\nVAGUE 2 — CAC40 & Grade A/B (" + str(len(VAGUE_2)) + ")")
    failed_all.update(fetch_vague(VAGUE_2, "V2", DELAY, prices_live))

    print("\nVAGUE 3 — SBF250 reste (" + str(len(VAGUE_3)) + ")")
    failed_all.update(fetch_vague(VAGUE_3, "V3", DELAY, prices_live))

    if failed_all:
        print("\nRETRY (" + str(len(failed_all)) + " tickers)")
        retry_failed(failed_all, prices_live)

    ok = len(prices_live)
    err = total - ok
    print("\nBPF :")
    for t in BPF:
        if t in prices_live:
            print("  " + t + " : " + str(prices_live[t]) + "€")

    print("\nTotal : " + str(ok) + "/" + str(total) + " · " + str(err) + " manquants")

    html = inject_prices_live(html, prices_live)
    print("PRICES_LIVE injecte (" + str(ok) + " tickers)")

    print("\nVratio BPF...")
    for symbol in BPF:
        if symbol in VAGUE_1:
            vr = get_vratio(VAGUE_1[symbol])
            html = inject_vratio_in_s(html, symbol, vr)
            time.sleep(0.3)

    if is_monday:
        print("\nFondamentaux BPF...")
        for symbol in BPF:
            if symbol not in VAGUE_1: continue
            funds = get_fundamentals(VAGUE_1[symbol])
            if funds:
                html = inject_fundamentals_in_s(html, symbol, funds)
                print("  " + symbol + " PE=" + str(funds.get('pe','?')) +
                      " b52h=" + str(funds.get('b52h','?')))
            time.sleep(0.5)

    print("\nMacro...")
    macro = {}
    for field, tk in MACRO_TICKERS.items():
        p = get_price(tk)
        macro[field] = p or 0
        time.sleep(0.4)
    print("  Taux " + str(macro.get('taux10us')) +
          "% · Or " + str(macro.get('or')) +
          "$ · DXY " + str(macro.get('dxy')))

    fng = get_fear_greed()
    if fng is not None:
        macro['fng'] = fng

    cac40_ytd = get_cac40_ytd()
    if cac40_ytd is not None:
        macro['cac40_ytd'] = cac40_ytd

    html = inject_macro(html, macro)
    html = inject_timestamp(html, ok, total, err)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("\nHistorique des prix...")
    update_history(prices_live)

    # Alertes Telegram
    TELEGRAM_TOKEN   = os.environ.get('TELEGRAM_TOKEN', '').strip()
    TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '').strip()
    print(f"  Telegram token present: {bool(TELEGRAM_TOKEN)} · chat_id present: {bool(TELEGRAM_CHAT_ID)}")
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        now_str = datetime.now().strftime('%d/%m a %Hh%M')
        fng_val = macro.get('fng')
        cac_val = macro.get('cac40_ytd')
        # Emoji Fear&Greed
        if fng_val is not None:
            fng_v = int(fng_val)
            fng_emoji = '😱' if fng_v<=20 else '😰' if fng_v<=40 else '😐' if fng_v<=60 else '😏' if fng_v<=80 else '🤑'
            fng_str = f'\n{fng_emoji} Fear&Greed: {fng_v}/100'
        else:
            fng_str = ''
        if cac_val is not None:
            cac_sign = '+' if float(cac_val) >= 0 else ''
            cac_str = f'\n📊 CAC40 YTD: {cac_sign}{cac_val}%'
        else:
            cac_str = ''
        msg = f'<b>🤖 VAL.PEA</b> — {now_str}\n'
        msg += f'✅ {ok}/{total} cours mis a jour\n'
        msg += fng_str + cac_str
        # Prix BPF clés
        bpf_tickers = ['AI','RMS','ASML','TTE','GTT','SU','LR','HO','ELIS','EL']
        bpf_lines = []
        for t in bpf_tickers:
            if t in prices_live:
                bpf_lines.append(f'{t}: {prices_live[t]}€')
        if bpf_lines:
            msg += '\n\n<b>Tes BPF:</b>\n' + '\n'.join(bpf_lines)
        # Signaux grade A en zone
        print("  Envoi Telegram...")
        send_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, msg)
        print(f"  Message envoye ({len(msg)} chars)")
    else:
        print("  ⚠️ Telegram NON configure — verifier secrets GitHub:")
        print("    Settings > Secrets > TELEGRAM_TOKEN et TELEGRAM_CHAT_ID")

    elapsed = int((datetime.now() - start).total_seconds())
    print("\n" + "=" * 60)
    print("TERMINE en " + str(elapsed // 60) + "min" + str(elapsed % 60) + "s")
    print(str(ok) + " prix · " + str(err) + " manquants")
    print("=" * 60)
