#!/usr/bin/env python3
"""
update_prices_v2.py — VAL.PEA
Sources : Yahoo Finance (yfinance) + mémoire persistante

Twelve Data abandonné : plan gratuit = US uniquement, actions FR non couvertes.
Yahoo Finance via yfinance est gratuit et couvre l'ensemble du SBF250.

Cascade :
  1. Yahoo Finance via yfinance (principal)
  2. Mémoire persistante prices_memory.json (filet de sécurité)

Validation : variation > 40% vs mémoire = aberration, on garde le prix mémoire.
Premier run (mémoire vide) : pas de validation, on accepte Yahoo directement.
"""

import re, json, sys, os
from datetime import datetime

try:
    import yfinance as yf
    HAS_YF = True
except ImportError:
    HAS_YF = False
    print("ERREUR : yfinance non installé — pip install yfinance")
    sys.exit(1)

MEMORY_FILE   = 'prices_memory.json'
MAX_VARIATION = 0.80
MIN_PRICE     = 0.50

# Taux de change approximatifs pour les actions hors EUR
DKK_TO_EUR = 7.46  # Novo Nordisk (couronnes danoises)

# ─── MAPPING YAHOO FINANCE ────────────────────────────────────────
YF_MAP = {
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA',
    'SAN':'SAN.PA','TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA',
    'AXA':'CS.PA','BNP':'BNP.PA','ACA':'ACA.PA','GLE':'GLE.PA',
    'AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA','ORA':'ORA.PA',
    'VIE':'VIE.PA','RNO':'RNO.PA','SGO':'SGO.PA','CAP':'CAP.PA',
    'DG':'DG.PA','VIV':'VIV.PA','LR':'LR.PA','DSY':'DSY.PA',
    'EL':'EL.PA','ENGI':'ENGI.PA','HO':'HO.PA','EN':'EN.PA',
    'BN':'BN.PA','AC':'AC.PA','AF':'AF.PA','CA':'CA.PA',
    'RI':'RI.PA','URW':'URW.AS','TEP':'TEP.PA','DIOR':'CDI.PA',
    'EDENRED':'EDEN.PA','PLUXEE':'PLX.PA','ALSTOM':'ALO.PA','GTT':'GTT.PA',
    'ELIS':'ELIS.PA','ERF':'ERF.PA','COFA':'COFA.PA','SPIE':'SPIE.PA',
    'BVI':'BVI.PA','FDJ':'FDJ.PA','IPSEN':'IPN.PA','REXEL':'RXL.PA',
    'SOP':'SOP.PA','LNA':'LNA.PA','FNAC':'FNAC.PA','EIFFAGE':'FGR.PA',
    'NEXANS':'NEX.PA','SOI':'SOI.PA','FORVIA':'FRVIA.PA','IMERYS':'NK.PA',
    'ALTEN':'ATE.PA','VK':'VK.PA','STM':'STM.PA','NOVO':'NOVO-B.CO',
    'SW':'SW.PA','ASML':'ASML.AS','PRX':'PRX.AS','ADYEN':'ADYEN.AS',
    'HEIA':'HEIA.AS','MT':'MT.AS','WLN':'WLN.PA','SEB':'SK.PA',
    'IPSOS':'IPS.PA','CNP':'CNP.PA','DBG':'DBG.PA','TRIGANO':'TRI.PA',
    'BOIRON':'BOI.PA','VIRBAC':'VIRP.PA','INTERPARFUMS':'ITP.PA','ARGAN':'ARG.PA',
    'LECTRA':'LSS.PA','LISI':'FII.PA','ELIOR':'ELIOR.PA','SAMSE':'SAMS.PA',
    'MANITOU':'MTU.PA','FIGEAC':'FGA.PA','ABIVAX':'ABVX.PA','COVIVIO':'COV.PA',
    'STEF':'STF.PA','THERMADOR':'THEP.PA','LACROIX':'LACR.PA','SYENSQO':'SYENS.PA',
    'WAGA':'WGAEN.PA','ORPEA':'ORP.PA','EMEIS':'EMEIS.PA','ALTAREA':'ALTA.PA',
    'NRO':'NRO.PA','RUI':'RUI.PA','NXI':'NXI.PA','GFC':'GFC.PA',
    'DERICHEBOURG':'DBG.PA','DASSAV':'AM.PA','SAP':'SAP.DE','SIEMENS':'SIE.DE',
    'ALV':'ALV.DE','BIOM':'BIO.PA','ATO':'ATO.PA','AK':'AK.PA',
    'JXS':'JXS.PA','MERY':'MERY.PA','TALY':'TEP.PA',
}

# Tickers dont le prix Yahoo est dans une devise autre que EUR
NON_EUR = {
    'NOVO': DKK_TO_EUR,   # DKK → EUR
}

# Tickers à réinitialiser si la mémoire contient une valeur aberrante
FORCE_RESET = {
    'NOVO': 50,   # Si mémoire > 50 = était en DKK, reset
    'WLN':  50,   # Si mémoire > 50 = ancien prix pré-effondrement, reset
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
    # Reset entrées DKK mal converties (prix > 100 pour NOVO = était en DKK)
    for ticker, divisor in NON_EUR.items():
        if ticker in memory and memory[ticker].get('price', 0) > 100:
            print(f"  Reset {ticker}: {memory[ticker]['price']} (était en devise étrangère)")
            del memory[ticker]
    return memory

def save_memory(memory):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

# ─── VALIDATION ──────────────────────────────────────────────────
def is_valid(price, mem_price):
    if not price or price < MIN_PRICE:
        return False, f"prix trop bas ({price})"
    if mem_price and mem_price > 0:
        var = abs(price - mem_price) / mem_price
        if var > MAX_VARIATION:
            return False, f"variation {var*100:.0f}% vs mémoire {mem_price}"
    return True, ""

# ─── FETCH PRIX ──────────────────────────────────────────────────
def fetch_all_prices(tickers_yf):
    """Télécharge tous les prix en 1 seul appel batch — plus efficace et moins bloqué"""
    results = {}
    if not tickers_yf:
        return results

    # Batch download
    try:
        import pandas as pd
        symbols = list(set(tickers_yf.values()))
        data = yf.download(symbols, period='2d', auto_adjust=True,
                          progress=False, threads=True)

        if data.empty:
            return results

        # Extraire le dernier cours de clôture
        close = data['Close'] if 'Close' in data.columns else data.xs('Close', level=0, axis=1) if len(data.columns.names) > 1 else data

        for ticker, yf_sym in tickers_yf.items():
            try:
                if yf_sym in close.columns:
                    series = close[yf_sym].dropna()
                    if not series.empty:
                        price = round(float(series.iloc[-1]), 2)
                        if price > MIN_PRICE:
                            # Conversion devise
                            if ticker in NON_EUR:
                                price = round(price / NON_EUR[ticker], 2)
                            results[ticker] = price
            except:
                pass
    except Exception as e:
        print(f"  Batch download erreur: {e}")
        # Fallback individuel
        for ticker, yf_sym in tickers_yf.items():
            try:
                t = yf.Ticker(yf_sym)
                p = t.fast_info.last_price
                if p and p > MIN_PRICE:
                    price = round(float(p), 2)
                    if ticker in NON_EUR:
                        price = round(price / NON_EUR[ticker], 2)
                    results[ticker] = price
            except:
                pass

    return results

# ─── MAIN ─────────────────────────────────────────────────────────
import sys, io

# Supprimer les warnings yfinance sur les tickers non trouvés
class _SuppressYF:
    def write(self, msg):
        if 'possibly delisted' not in msg and 'No data found' not in msg:
            sys.__stderr__.write(msg)
    def flush(self): pass

sys.stderr = _SuppressYF()

if __name__ == '__main__':
    html_file = 'index.html'
    if not os.path.exists(html_file):
        print(f"ERREUR: {html_file} introuvable")
        sys.exit(1)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    is_friday = datetime.now().weekday() == 4
    now_str   = datetime.now().strftime('%d/%m à %H:%M')

    print(f"Source : Yahoo Finance (yfinance)")
    print(f"Mode   : {'VENDREDI — recalibration zones' if is_friday else 'Quotidien'}")
    print("=" * 50)

    memory    = load_memory()
    first_run = len(memory) == 0
    if first_run:
        print("⚠️  Premier run — pas de validation (mémoire vide)")
    print(f"Mémoire : {len(memory)} prix en cache")

    s_start = content.find("const S=[")
    if s_start < 0:
        print("ERREUR: const S=[ non trouvé")
        sys.exit(1)

    # Télécharger TOUS les prix en 1 appel batch
    print("Téléchargement des prix en batch...")
    all_prices = fetch_all_prices(YF_MAP)
    print(f"  → {len(all_prices)} prix reçus du batch")

    updated   = 0
    from_mem  = 0
    aberrant  = 0
    no_map    = 0

    for m in re.finditer(
        r"(\{ticker:'([^']+)'.*?)(?=\n\n\{ticker:|\n\n\];)",
        content[s_start:], re.DOTALL
    ):
        block  = m.group(1)
        ticker = m.group(2)

        pm         = re.search(r'\bprice:([\d.]+)', block)
        file_price = float(pm.group(1)) if pm else 0
        mem_price  = memory.get(ticker, {}).get('price', file_price)

        if ticker not in YF_MAP:
            no_map += 1
            continue

        yf_price = all_prices.get(ticker)

        if yf_price:
            # Phase d'initialisation : mémoire < 100 entrées = vieux prix S[]
            # Accepter tous les prix Yahoo > 0.50 sans validation
            init_phase = len(memory) < 100
            if first_run or init_phase:
                ok, reason = True, ""
            else:
                ok, reason = is_valid(yf_price, mem_price)

            if ok:
                best_price = yf_price
                memory[ticker] = {
                    'price':  yf_price,
                    'date':   datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'source': 'yahoo'
                }
                updated += 1
            else:
                # Aberration → garder mémoire
                best_price = mem_price
                aberrant  += 1
                print(f"  🚫 {ticker:8} Yahoo={yf_price} ABERRANT ({reason})")
        else:
            # Yahoo indisponible → mémoire
            best_price = mem_price
            from_mem  += 1

        # Appliquer dans le fichier
        if best_price and best_price != file_price:
            chg = round((best_price - mem_price) / mem_price * 100, 2) if mem_price else 0
            new_block = re.sub(r'\bprice:[\d.]+', f'price:{best_price}', block, count=1)
            new_block = re.sub(r'\bchg:[-\d.]+', f'chg:{chg}', new_block, count=1)
            if new_block != block:
                content = content[:s_start + m.start()] + new_block + content[s_start + m.end():]

        # Vendredi : recalibration zones si dérive > 15%
        if is_friday and yf_price and not first_run and mem_price and mem_price > 0:
            drift = abs(yf_price - mem_price) / mem_price
            if drift > 0.15:
                ratio = yf_price / mem_price
                for key in ['el','eh','stop','o1','o2','dcfb','dcfm','dcfu']:
                    km = re.search(r'\b' + key + r':([\d.]+)', block)
                    if km:
                        nv = round(float(km.group(1)) * ratio, 1)
                        content = content.replace(f'{key}:{km.group(1)}', f'{key}:{nv}', 1)
                print(f"  📐 {ticker:8} zones recalibrées ({drift*100:.0f}% dérive)")

    # Sauvegarder mémoire
    save_memory(memory)

    # Timestamp
    content = re.sub(
        r'\d+ cours mis à jour[^<"\')\]]*',
        f"{updated} cours mis à jour le {now_str}",
        content
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    total = updated + from_mem + no_map
    coverage = round(updated / total * 100) if total else 0

    print(f"\n✅ Yahoo Finance  : {updated} prix mis à jour")
    print(f"📦 Mémoire        : {from_mem} prix (Yahoo indispo)")
    print(f"🚫 Aberrations    : {aberrant} rejetées")
    print(f"⏭  Sans mapping   : {no_map} tickers")
    print(f"💾 Mémoire        : {len(memory)} entrées ({MEMORY_FILE})")
    print(f"📊 Couverture     : {coverage}% ({updated}/{total})")
