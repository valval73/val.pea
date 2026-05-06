#!/usr/bin/env python3
"""
update_prices_v2.py — VAL.PEA
Multi-sources avec mémoire persistante.

Cascade :
  1. Twelve Data (800 req/jour gratuit — clé dans secrets GitHub)
  2. Yahoo Finance via yfinance (fallback automatique)
  3. Mémoire persistante prices_memory.json (filet de sécurité)

Validation anti-aberration : variation > 40% = rejeté, mémoire utilisée.
"""

import re, json, sys, os
from datetime import datetime

# Imports optionnels — ne pas crasher si manquants
try:
    import yfinance as yf
    HAS_YF = True
except ImportError:
    HAS_YF = False
    print("⚠️  yfinance non installé — fallback urllib uniquement")

try:
    import urllib.request
    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False


DKK_TICKERS = {'NOVO'}  # Retournent des prix en DKK, pas en EUR
DKK_TO_EUR  = 7.46      # Taux approximatif EUR/DKK

MEMORY_FILE   = 'prices_memory.json'
MAX_VARIATION = 0.40
MIN_PRICE     = 0.50

TWELVE_KEY = os.environ.get('TWELVE_DATA_KEY', '')
FMP_KEY    = os.environ.get('FMP_KEY', '')

# ─── MAPPING TWELVE DATA ─────────────────────────────────────────
TWELVE_MAP = {
    # Format Twelve Data pour Euronext Paris : même format que Yahoo (.PA, .AS etc.)
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA',
    'ORA':'ORA.PA','LR':'LR.PA','DSY':'DSY.PA','STM':'STM.MI','EL':'EL.PA',
    'ML':'ML.PA','ENGI':'ENGI.PA','HO':'HO.PA','DG':'DG.PA','CAP':'CAP.PA',
    'GTT':'GTT.PA','ELIS':'ELIS.PA','SPIE':'SPIE.PA','ALO':'ALO.PA',
    'BVI':'BVI.PA','REXEL':'RXL.PA','SOI':'SOI.PA','NEXANS':'NEX.PA',
    'ASML':'ASML.AS','MT':'MT.AS','VK':'VK.PA','RNO':'RNO.PA',
    'FORVIA':'FRVIA.PA','IMERYS':'NK.PA','ALTEN':'ATE.PA','EIFFAGE':'FGR.PA',
    'SGO':'SGO.PA','ERF':'ERF.PA','BN':'BN.PA','EN':'EN.PA',
}

# ─── MAPPING YAHOO FINANCE ───────────────────────────────────────
YF_MAP = {
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA',
    'ORA':'ORA.PA','VIE':'VIE.PA','RNO':'RNO.PA','SGO':'SGO.PA','CAP':'CAP.PA',
    'DG':'DG.PA','VIV':'VIV.PA','LR':'LR.PA','WLN':'WLN.PA','DSY':'DSY.PA',
    'STM':'STM.MI','EL':'EL.PA','ML':'ML.PA','ENGI':'ENGI.PA','HO':'HO.PA',
    'AC':'AC.PA','AF':'AF.PA','BN':'BN.PA','EN':'EN.PA','SW':'SW.PA',
    'GTT':'GTT.PA','ELIS':'ELIS.PA','ERF':'ERF.PA','COFA':'COFA.PA',
    'SPIE':'SPIE.PA','ALO':'ALO.PA','BVI':'BVI.PA','FDJ':'FDJ.PA',
    'IPSEN':'IPN.PA','REXEL':'RXL.PA','SOP':'SOP.PA','LNA':'LNA.PA',
    'FNAC':'FNAC.PA','EIFFAGE':'FGR.PA','NEXANS':'NEX.PA','SOI':'SOI.PA',
    'FORVIA':'FRVIA.PA','IMERYS':'NK.PA','ALTEN':'ATE.PA','VK':'VK.PA',
    'ASML':'ASML.AS','NOVO':'NOVO-B.CO','MT':'MT.AS','HEIA':'HEIA.AS',
    'ADYEN':'ADYEN.AS','RNO':'RNO.PA','SGO':'SGO.PA',
}

# ─── MÉMOIRE ─────────────────────────────────────────────────────
def load_memory():
    memory = {}
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, 'r') as f:
                memory = json.load(f)
        except:
            pass
    # Réinitialiser les tickers DKK si leur prix mémoire > 100
    # (signifie qu'ils ont été enregistrés en DKK avant la conversion)
    for ticker in list(memory.keys()):
        if ticker in ('NOVO',) and memory[ticker].get('price', 0) > 100:
            print(f"  🔄 Reset mémoire {ticker}: {memory[ticker]['price']} (était en DKK)")
            del memory[ticker]
    return memory

def save_memory(memory):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

# ─── VALIDATION ──────────────────────────────────────────────────
def is_valid(price, mem_price, b52h=None, b52l=None):
    # Validation uniquement vs mémoire (les b52h/b52l dans S[] sont périmés)
    if not price or price < MIN_PRICE:
        return False, f"prix trop bas ({price})"
    if mem_price and mem_price > 0:
        var = abs(price - mem_price) / mem_price
        if var > MAX_VARIATION:
            return False, f"variation {var*100:.0f}% vs mémoire {mem_price}"
    return True, ""

# ─── SOURCES ─────────────────────────────────────────────────────
_twelve_error_logged = False  # Logger une seule fois

def fetch_twelve(ticker):
    global _twelve_error_logged
    if not TWELVE_KEY or not HAS_URLLIB:
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
            _twelve_error_logged = False
            return round(float(data['price']), 2)
        elif 'code' in data and not _twelve_error_logged:
            print(f"  ⚠️  Twelve Data erreur: {data.get('message','?')} (code {data.get('code','?')})")
            _twelve_error_logged = True
    except Exception as e:
        if not _twelve_error_logged:
            print(f"  ⚠️  Twelve Data exception: {str(e)[:80]}")
            _twelve_error_logged = True
    return None

def fetch_yahoo(ticker):
    yf_sym = YF_MAP.get(ticker)
    if not yf_sym:
        return None
    # Méthode 1 : yfinance library
    if HAS_YF:
        try:
            t = yf.Ticker(yf_sym)
            price = t.fast_info.last_price
            if price and price > 0:
                return round(float(price), 2)
        except:
            pass
    # Méthode 2 : API directe
    if HAS_URLLIB:
        try:
            url = f"https://query2.finance.yahoo.com/v8/finance/chart/{yf_sym}?interval=1d&range=1d"
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Accept': 'application/json',
                'Referer': 'https://finance.yahoo.com/',
            })
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read())
            meta = data['chart']['result'][0]['meta']
            price = meta.get('regularMarketPrice') or meta.get('previousClose')
            return round(float(price), 2) if price else None
        except:
            pass
    return None

# ─── MAIN ─────────────────────────────────────────────────────────
if __name__ == '__main__':
    html_file = 'index.html'
    if not os.path.exists(html_file):
        print(f"ERREUR: {html_file} introuvable")
        sys.exit(1)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    is_friday = datetime.now().weekday() == 4
    now_str   = datetime.now().strftime('%d/%m à %H:%M')

    print(f"Sources : Twelve={'OUI' if TWELVE_KEY else 'NON (ajouter TWELVE_DATA_KEY dans GitHub Secrets)'} | yfinance={'OUI' if HAS_YF else 'NON'}")
    print(f"Mode : {'VENDREDI — recalibration zones' if is_friday else 'Quotidien'}")
    print("=" * 55)

    memory = load_memory()
    print(f"Mémoire : {len(memory)} prix en cache")

    s_start = content.find("const S=[")
    if s_start < 0:
        print("ERREUR: const S=[ non trouvé")
        sys.exit(1)

    stats = {'twelve': 0, 'yahoo': 0, 'memory': 0, 'skipped': 0}

    # Trouver toutes les actions dans S[]
    pattern = re.compile(r"(\{ticker:'([^']+)'[^{}]*(?:\{[^{}]*\}[^{}]*)*\})", re.DOTALL)
    s_section = content[s_start:]

    for m in re.finditer(r"(\{ticker:'([^']+)'.*?)(?=\n\n\{ticker:|\n\n\];)", s_section, re.DOTALL):
        block  = m.group(1)
        ticker = m.group(2)

        pm     = re.search(r'\bprice:([\d.]+)', block)
        b52h_m = re.search(r'\bb52h:([\d.]+)', block)
        b52l_m = re.search(r'\bb52l:([\d.]+)', block)

        file_price = float(pm.group(1)) if pm else 0
        mem_entry  = memory.get(ticker, {})
        mem_price  = mem_entry.get('price', file_price)
        b52h       = float(b52h_m.group(1)) if b52h_m else None
        b52l       = float(b52l_m.group(1)) if b52l_m else None

        best_price = None
        source     = 'skipped'

        # Premier run : mémoire vide → accepter sans validation
        # Les prix dans S[] sont peut-être périmés — ne pas les utiliser comme référence
        first_run = (len(memory) == 0)

        # 1. Twelve Data
        p = fetch_twelve(ticker)
        if p and ticker in DKK_TICKERS:
            p = round(p / DKK_TO_EUR, 2)
        if p and p > MIN_PRICE:
            if first_run:
                ok, reason = True, ""
            else:
                ok, reason = is_valid(p, mem_price, b52h, b52l)
            if ok:
                best_price, source = p, 'twelve'

        # 2. Yahoo Finance (si Twelve échoue)
        if not best_price:
            p = fetch_yahoo(ticker)
            # Conversion DKK → EUR (Novo Nordisk)
            if p and ticker in DKK_TICKERS:
                p = round(p / DKK_TO_EUR, 2)
            if p and p > MIN_PRICE:
                if first_run:
                    ok, reason = True, ""
                else:
                    ok, reason = is_valid(p, mem_price, b52h, b52l)
                # Reset mémoire si le ticker DKK avait un ancien prix EUR incorrect
                if not ok and ticker in DKK_TICKERS:
                    ok, reason = True, "reset DKK ticker"
                if ok:
                    best_price, source = p, 'yahoo'
                elif not ok:
                    print(f"  🚫 {ticker:8} Yahoo={p} ABERRANT ({reason}) → mémoire {mem_price}")

        # 3. Mémoire (filet de sécurité)
        if not best_price:
            if mem_price and mem_price > 0:
                best_price, source = mem_price, 'memory'
            else:
                stats['skipped'] += 1
                continue

        # Mettre à jour la mémoire
        if source in ('twelve', 'yahoo'):
            memory[ticker] = {
                'price':  best_price,
                'date':   datetime.now().strftime('%Y-%m-%d %H:%M'),
                'source': source
            }

        stats[source] = stats.get(source, 0) + 1

        # Appliquer dans le fichier
        if best_price != file_price:
            chg = round((best_price - mem_price) / mem_price * 100, 2) if mem_price else 0
            new_block = re.sub(r'\bprice:[\d.]+', f'price:{best_price}', block, count=1)
            new_block = re.sub(r'\bchg:[-\d.]+', f'chg:{chg}', new_block, count=1)
            if new_block != block:
                content = content[:s_start + m.start()] + new_block + content[s_start + m.end():]

        # Recalibration zones le vendredi (dérive > 15%)
        if is_friday and source != 'memory' and mem_price and mem_price > 0:
            drift = abs(best_price - mem_price) / mem_price
            if drift > 0.15:
                ratio = best_price / mem_price
                for key in ['el','eh','stop','o1','o2','dcfb','dcfm','dcfu']:
                    km = re.search(r'\b' + key + r':([\d.]+)', block)
                    if km:
                        new_val = round(float(km.group(1)) * ratio, 1)
                        content = content.replace(f'{key}:{km.group(1)}', f'{key}:{new_val}', 1)
                print(f"  📐 {ticker:8} zones recalibrées ({drift*100:.0f}% dérive)")

    # Sauvegarder mémoire
    save_memory(memory)

    # Timestamp
    total = stats['twelve'] + stats['yahoo']
    content = re.sub(
        r'\d+ cours mis à jour[^<"\')\]]*',
        f"{total} cours mis à jour le {now_str} (twelve:{stats['twelve']} yahoo:{stats['yahoo']} mémoire:{stats['memory']})",
        content
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ Twelve Data   : {stats['twelve']}")
    print(f"✅ Yahoo Finance : {stats['yahoo']}")
    print(f"📦 Mémoire       : {stats['memory']} (fallback)")
    print(f"💾 {len(memory)} entrées sauvegardées dans {MEMORY_FILE}")

    total_live = stats['twelve'] + stats['yahoo']
    total_all  = total_live + stats['memory'] + stats.get('skipped',0)
    coverage   = round(total_live / total_all * 100) if total_all > 0 else 0
    print(f"📊 Couverture prix en temps réel : {coverage}% ({total_live}/{total_all})")

    if not TWELVE_KEY:
        print("\n⚠️  CONSEIL : Ajouter TWELVE_DATA_KEY dans GitHub Secrets")
        print("   → twelvedata.com (gratuit, 800 req/jour)")
    if stats['twelve'] == 0 and TWELVE_KEY:
        print("\n⚠️  Twelve Data actif mais 0 prix retournés — vérifier la clé API")
        print("   Test manuel : https://api.twelvedata.com/price?symbol=MC.PA&apikey=VOTRE_CLE")
