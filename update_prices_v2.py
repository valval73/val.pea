#!/usr/bin/env python3
"""
update_prices_v2.py — VAL.PEA
Système de prix multi-sources avec mémoire persistante.

Cascade de fiabilité :
  1. Twelve Data (800 req/jour gratuit — meilleure couverture Euronext)
  2. Yahoo Finance via yfinance (fallback si Twelve Data échoue)
  3. Mémoire persistante (dernier prix valide connu)

Validation anti-aberration à chaque étape.
prices_memory.json = source de vérité des derniers prix valides.

Clés API requises (gratuites) :
  - TWELVE_DATA_KEY : twelvedata.com (800 req/jour)
  - FMP_KEY         : financialmodelingprep.com (250 req/jour — pour le PTF uniquement)
"""

import re, json, sys, os, time
from datetime import datetime
import urllib.request
import yfinance as yf

MEMORY_FILE   = 'prices_memory.json'
MAX_VARIATION = 0.40   # 40% max entre 2 runs
MIN_PRICE     = 0.50   # Prix minimum acceptable

# Clés API depuis les secrets GitHub
TWELVE_KEY = os.environ.get('TWELVE_DATA_KEY', '')
FMP_KEY    = os.environ.get('FMP_KEY', '')

# ─── MAPPING TWELVE DATA (symboles Euronext) ─────────────────────
# Twelve Data utilise le format "MC:EPA" pour les actions françaises
TWELVE_MAP = {
    'MC':'MC:EPA','AI':'AI:EPA','OR':'OR:EPA','RMS':'RMS:EPA','SAN':'SAN:EPA',
    'TTE':'TTE:EPA','SAF':'SAF:EPA','SU':'SU:EPA','AXA':'CS:EPA','BNP':'BNP:EPA',
    'ACA':'ACA:EPA','GLE':'GLE:EPA','AIR':'AIR:EPA','KER':'KER:EPA','PUB':'PUB:EPA',
    'ORA':'ORA:EPA','LR':'LR:EPA','DSY':'DSY:EPA','STM':'STM:EPA','EL':'EL:EPA',
    'ML':'ML:EPA','ENGI':'ENGI:EPA','HO':'HO:EPA','DG':'DG:EPA','CAP':'CAP:EPA',
    'GTT':'GTT:EPA','ELIS':'ELIS:EPA','ERF':'ERF:EPA','COFA':'COFA:EPA',
    'SPIE':'SPIE:EPA','ALO':'ALO:EPA','BVI':'BVI:EPA','FDJ':'FDJ:EPA',
    'IPSEN':'IPNP:EPA','REXEL':'RXL:EPA','SOI':'SOI:EPA',
    'ASML':'ASML:AMS','NOVO':'NOVO-B:CPH','PRX':'PRX:AMS',
    'NEXANS':'NEX:EPA','SGB':'SGO:EPA','RNO':'RNO:EPA',
    'FORVIA':'FRVIA:EPA','IMERYS':'NK:EPA','ALTEN':'ATE:EPA',
    'EIFFAGE':'FGR:EPA','VK':'VK:EPA','MT':'MT:AMS',
}

# Mapping Yahoo Finance (fallback)
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
    'FNAC':'FNAC.PA','EIFFAGE':'FGR.PA','NEXANS':'NEX.PA','SOI':'SOI.PA',
    'FORVIA':'FRVIA.PA','IMERYS':'NK.PA','ALTEN':'ATE.PA',
    'ASML':'ASML.AS','NOVO':'NOVO-B.CO','PRX':'PRX.AS','MT':'MT.AS',
    'HEIA':'HEIA.AS','ADYEN':'ADYEN.AS','VK':'VK.PA','RNO':'RNO.PA',
}

# ─── MÉMOIRE PERSISTANTE ─────────────────────────────────────────
def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

# ─── VALIDATION ANTI-ABERRATION ──────────────────────────────────
def is_valid(new_price, mem_price, b52h=None, b52l=None):
    """Retourne (True, "") si valide, (False, raison) si aberrant"""
    if not new_price or new_price < MIN_PRICE:
        return False, f"prix trop bas {new_price}"
    if mem_price and mem_price > 0:
        variation = abs(new_price - mem_price) / mem_price
        if variation > MAX_VARIATION:
            return False, f"variation {variation*100:.0f}% vs mémoire {mem_price}"
    if b52h and b52l and b52l > 0:
        if new_price < b52l * 0.50 or new_price > b52h * 1.50:
            return False, f"hors range [{b52l}-{b52h}]×1.5"
    return True, ""

# ─── SOURCE 1 : TWELVE DATA ──────────────────────────────────────
def fetch_twelve(ticker):
    """Twelve Data — 800 req/jour gratuit, meilleure couverture Euronext"""
    if not TWELVE_KEY:
        return None
    symbol = TWELVE_MAP.get(ticker)
    if not symbol:
        return None
    try:
        url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={TWELVE_KEY}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read())
        if 'price' in data:
            return round(float(data['price']), 2)
    except:
        pass
    return None

# ─── SOURCE 2 : YAHOO FINANCE (yfinance) ─────────────────────────
def fetch_yahoo(ticker):
    """Yahoo Finance via yfinance — fallback principal"""
    yf_ticker = YF_MAP.get(ticker)
    if not yf_ticker:
        return None
    try:
        t = yf.Ticker(yf_ticker)
        price = t.fast_info.last_price
        if price and price > 0:
            return round(float(price), 2)
    except:
        pass
    # Fallback v8 API
    try:
        url = f"https://query2.finance.yahoo.com/v8/finance/chart/{yf_ticker}?interval=1d&range=1d"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Referer': 'https://finance.yahoo.com/',
        })
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        meta = data['chart']['result'][0]['meta']
        price = meta.get('regularMarketPrice') or meta.get('previousClose')
        return round(float(price), 2) if price else None
    except:
        return None

# ─── SOURCE 3 : FMP (portefeuille uniquement) ────────────────────
def fetch_fmp(ticker):
    """FMP — 250 req/jour, utilisé uniquement pour valider le PTF"""
    if not FMP_KEY:
        return None
    try:
        url = f"https://financialmodelingprep.com/api/v3/quote-short/{ticker}.PA?apikey={FMP_KEY}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read())
        if data and isinstance(data, list):
            return round(float(data[0]['price']), 2)
    except:
        pass
    return None

# ─── FETCH AVEC CASCADE ──────────────────────────────────────────
def fetch_best_price(ticker, mem_price, b52h, b52l, is_portfolio=False):
    """
    Essaie les sources dans l'ordre et retourne le premier prix valide.
    Retourne (price, source, reason_if_fallback)
    """
    # 1. Twelve Data
    p1 = fetch_twelve(ticker)
    valid, reason = is_valid(p1, mem_price, b52h, b52l)
    if p1 and valid:
        return p1, 'twelve', ''

    # 2. Yahoo Finance
    p2 = fetch_yahoo(ticker)
    valid2, reason2 = is_valid(p2, mem_price, b52h, b52l)
    if p2 and valid2:
        return p2, 'yahoo', f"twelve={'aberrant: '+reason if p1 else 'indispo'}"

    # 3. FMP (si portefeuille)
    if is_portfolio and FMP_KEY:
        p3 = fetch_fmp(ticker)
        valid3, reason3 = is_valid(p3, mem_price, b52h, b52l)
        if p3 and valid3:
            return p3, 'fmp', f"twelve+yahoo indispos/aberrants"

    # 4. Mémoire (filet de sécurité)
    if mem_price and mem_price > 0:
        return mem_price, 'memory', f"toutes sources indisponibles/aberrantes"

    return None, 'none', 'aucune source disponible'

# ─── MAIN ─────────────────────────────────────────────────────────
if __name__ == '__main__':
    html_file = 'index.html'
    if not os.path.exists(html_file):
        print(f"ERROR: {html_file} not found")
        sys.exit(1)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    is_friday = datetime.now().weekday() == 4
    now_str   = datetime.now().strftime('%d/%m à %H:%M')

    # Afficher la configuration
    print(f"Sources actives :")
    print(f"  Twelve Data : {'OUI (' + TWELVE_KEY[:8] + '...)' if TWELVE_KEY else 'NON — ajouter TWELVE_DATA_KEY dans GitHub Secrets'}")
    print(f"  Yahoo Finance (yfinance) : OUI (fallback)")
    print(f"  FMP : {'OUI' if FMP_KEY else 'NON (optionnel)'}")
    print(f"  Mémoire persistante : OUI ({MEMORY_FILE})")
    print(f"Mode : {'VENDREDI — recalibration zones' if is_friday else 'Quotidien'}")
    print("=" * 60)

    memory = load_memory()
    print(f"Mémoire : {len(memory)} prix en cache")

    # Portefeuille Val (pour priorité FMP)
    ptf_tickers = ['ASML','ELIS','EL','GTT','RMS','AI','LR','SU','HO','TTE','DCAM','PAEEM']

    s_start = content.find("const S=[")
    stats = {'twelve':0, 'yahoo':0, 'fmp':0, 'memory':0, 'none':0, 'recalibrated':0}

    for m in re.finditer(
        r"(\{ticker:'([^']+)'.*?)(?=\n\n\{ticker:|\n\n\];)",
        content[s_start:], re.DOTALL
    ):
        block  = m.group(1)
        ticker = m.group(2)

        pm     = re.search(r'\bprice:([\d.]+)', block)
        b52h_m = re.search(r'\bb52h:([\d.]+)', block)
        b52l_m = re.search(r'\bb52l:([\d.]+)', block)

        file_price = float(pm.group(1)) if pm else 0
        mem_price  = memory.get(ticker, {}).get('price', file_price)
        b52h       = float(b52h_m.group(1)) if b52h_m else None
        b52l       = float(b52l_m.group(1)) if b52l_m else None
        is_ptf     = ticker in ptf_tickers

        # Récupérer le meilleur prix disponible
        best_price, source, fallback_reason = fetch_best_price(
            ticker, mem_price, b52h, b52l, is_portfolio=is_ptf
        )

        if not best_price:
            stats['none'] += 1
            continue

        # Logger les fallbacks
        if source == 'memory' and fallback_reason:
            print(f"  📦 {ticker:8} → mémoire {best_price} ({fallback_reason})")
        elif source == 'yahoo' and fallback_reason:
            pass  # silencieux pour ne pas polluer les logs

        # Mettre à jour la mémoire si source fiable
        if source in ('twelve', 'yahoo', 'fmp'):
            memory[ticker] = {
                'price':  best_price,
                'date':   datetime.now().strftime('%Y-%m-%d %H:%M'),
                'source': source
            }

        stats[source] = stats.get(source, 0) + 1

        # Appliquer dans index.html
        if best_price != file_price:
            chg = round((best_price - mem_price) / mem_price * 100, 2) if mem_price else 0
            new_block = re.sub(r'\bprice:[\d.]+', f'price:{best_price}', block, count=1)
            new_block = re.sub(r'\bchg:[-\d.]+', f'chg:{chg}', new_block, count=1)
            if new_block != block:
                content = content[:s_start + m.start()] + new_block + content[s_start + m.end():]

        # Recalibration zones le vendredi
        if is_friday and source != 'memory' and mem_price and mem_price > 0:
            drift = abs(best_price - mem_price) / mem_price
            if drift > 0.15:
                ratio = best_price / mem_price
                for key in ['el','eh','stop','o1','o2','dcfb','dcfm','dcfu']:
                    km = re.search(r'\b' + key + r':([\d.]+)', block)
                    if km:
                        new_val = round(float(km.group(1)) * ratio, 1)
                        content = content.replace(f'{key}:{km.group(1)}', f'{key}:{new_val}', 1)
                stats['recalibrated'] += 1
                print(f"  📐 {ticker:8} zones recalibrées ({drift*100:.0f}% dérive)")

    # Sauvegarder mémoire
    save_memory(memory)

    # Timestamp header
    total_updated = stats['twelve'] + stats['yahoo'] + stats['fmp']
    content = re.sub(
        r'\d+ cours mis à jour[^<"\')\]]*',
        f"{total_updated} cours mis à jour le {now_str} "
        f"(twelve:{stats['twelve']} yahoo:{stats['yahoo']} mémoire:{stats['memory']})",
        content
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ Twelve Data   : {stats['twelve']} prix")
    print(f"✅ Yahoo Finance : {stats['yahoo']} prix")
    print(f"✅ FMP           : {stats.get('fmp',0)} prix")
    print(f"📦 Mémoire       : {stats['memory']} prix (fallback)")
    print(f"📐 Recalibrés    : {stats['recalibrated']} zones (vendredi)")
    print(f"💾 Mémoire sauvegardée : {len(memory)} entrées")

    if stats.get('none', 0) > 10:
        print(f"⚠️  {stats['none']} actions sans aucune source — vérifier les secrets GitHub")
