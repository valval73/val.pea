#!/usr/bin/env python3
"""
update_prices_v2.py — VAL.PEA
Batch download Yahoo Finance + mémoire persistante.
Mise à jour chirurgicale : ne touche que price: et chg: du bon ticker.
"""

import re, json, sys, os, warnings
from datetime import datetime
warnings.filterwarnings("ignore")

try:
    import yfinance as yf
except ImportError:
    print("ERREUR: pip install yfinance")
    sys.exit(1)

MEMORY_FILE = "prices_memory.json"
MIN_PRICE   = 0.50
NON_EUR     = {"NOVO": 7.46}
FORCE_RESET = {"NOVO": 50, "WLN": 50, "ATO": 5}

YF_MAP = {
    "MC":"MC.PA","AI":"AI.PA","OR":"OR.PA","RMS":"RMS.PA","SAN":"SAN.PA",
    "TTE":"TTE.PA","SAF":"SAF.PA","SU":"SU.PA","AXA":"CS.PA","BNP":"BNP.PA",
    "ACA":"ACA.PA","GLE":"GLE.PA","AIR":"AIR.PA","KER":"KER.PA","PUB":"PUB.PA",
    "ORA":"ORA.PA","VIE":"VIE.PA","RNO":"RNO.PA","SGO":"SGO.PA","CAP":"CAP.PA",
    "DG":"DG.PA","VIV":"VIV.PA","LR":"LR.PA","DSY":"DSY.PA",
    "EL":"EL.PA","ENGI":"ENGI.PA","HO":"HO.PA","EN":"EN.PA",
    "BN":"BN.PA","AC":"AC.PA","AF":"AF.PA","CA":"CA.PA","RI":"RI.PA",
    "URW":"URW.AS","TEP":"TEP.PA","DIOR":"CDI.PA",
    "GTT":"GTT.PA","ELIS":"ELIS.PA","ERF":"ERF.PA","COFA":"COFA.PA",
    "SPIE":"SPIE.PA","BVI":"BVI.PA","FDJ":"FDJ.PA",
    "IPSEN":"IPN.PA","REXEL":"RXL.PA","SOP":"SOP.PA","LNA":"LNA.PA",
    "FNAC":"FNAC.PA","EIFFAGE":"FGR.PA","NEXANS":"NEX.PA","SOI":"SOI.PA",
    "FORVIA":"FRVIA.PA","IMERYS":"NK.PA","ALTEN":"ATE.PA","VK":"VK.PA",
    "STM":"STM.PA","NOVO":"NOVO-B.CO","SW":"SW.PA","WLN":"WLN.PA",
    "ASML":"ASML.AS","PRX":"PRX.AS","ADYEN":"ADYEN.AS","HEIA":"HEIA.AS",
    "MT":"MT.AS","SEB":"SK.PA","IPSOS":"IPS.PA","CNP":"CNP.PA",
    "DBG":"DBG.PA","TRIGANO":"TRI.PA","BOIRON":"BOI.PA","VIRBAC":"VIRP.PA",
    "INTERPARFUMS":"ITP.PA","ARGAN":"ARG.PA","LECTRA":"LSS.PA",
    "LISI":"FII.PA","ELIOR":"ELIOR.PA","SAMSE":"SAMS.PA",
    "MANITOU":"MTU.PA","FIGEAC":"FGA.PA","ABIVAX":"ABVX.PA",
    "COVIVIO":"COV.PA","STEF":"STF.PA","THERMADOR":"THEP.PA",
    "LACROIX":"LACR.PA","WAGA":"WGAEN.PA","DASSAV":"AM.PA",
    "SAP":"SAP.DE","SIEMENS":"SIE.DE","DERICHEBOURG":"DBG.PA",
    "ATO":"ATO.PA","MERY":"MERY.PA","JXS":"JXS.PA","SYENSQO":"SYENS.PA",
}

def load_memory():
    memory = {}
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE) as f:
                memory = json.load(f)
        except:
            pass
    for ticker, threshold in FORCE_RESET.items():
        if ticker in memory and memory[ticker].get("price", 0) > threshold:
            print("  Reset " + ticker + ": " + str(memory[ticker]["price"]))
            del memory[ticker]
    return memory

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def fetch_all():
    symbols = list(set(YF_MAP.values()))
    try:
        data = yf.download(symbols, period="2d", auto_adjust=True,
                          progress=False, threads=True)
        close = data["Close"]
        results = {}
        for ticker, yf_sym in YF_MAP.items():
            try:
                if yf_sym in close.columns:
                    series = close[yf_sym].dropna()
                    if not series.empty:
                        p = round(float(series.iloc[-1]), 2)
                        if ticker in NON_EUR:
                            p = round(p / NON_EUR[ticker], 2)
                        if p > MIN_PRICE:
                            results[ticker] = p
            except:
                pass
        return results
    except Exception as e:
        print("  Batch erreur: " + str(e))
        return {}

def update_price_in_content(content, ticker, new_price, mem_price):
    """
    Mise à jour chirurgicale.
    Cherche la balise ticker:'TICKER' puis remplace UNIQUEMENT
    le premier 'price:X' qui suit sur les lignes suivantes.
    Utilise une approche position-based, pas regex globale.
    """
    search = "ticker:'" + ticker + "'"
    pos = content.find(search)
    if pos < 0:
        return content, False

    # Trouver la fin du bloc = prochain "ticker:" ou fin de S[]
    next_ticker = content.find("ticker:'", pos + len(search))
    end_s = content.find("\n];", pos)
    block_end = min(next_ticker if next_ticker > 0 else 999999,
                    end_s if end_s > 0 else 999999)

    block = content[pos:block_end]

    # Remplacer price:X dans ce bloc uniquement
    new_block = re.sub(r'\bprice:[\d.]+', 'price:' + str(new_price), block, count=1)
    if new_block == block:
        return content, False

    # Remplacer chg:X
    chg = round((new_price - mem_price) / mem_price * 100, 2) if mem_price else 0
    new_block = re.sub(r'\bchg:[-\d.]+', 'chg:' + str(chg), new_block, count=1)

    return content[:pos] + new_block + content[block_end:], True


if __name__ == "__main__":
    if not os.path.exists("index.html"):
        print("ERREUR: index.html introuvable")
        sys.exit(1)

    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    is_friday = datetime.now().weekday() == 4
    now_str   = datetime.now().strftime("%d/%m a %H:%M")

    memory    = load_memory()
    init_mode = len(memory) < 80

    print("Source : Yahoo Finance (batch)")
    print("Mode   : VENDREDI" if is_friday else "Mode   : Quotidien")
    print("Memoire: " + str(len(memory)) + " entrees" + (" (init)" if init_mode else ""))
    print("=" * 50)

    print("Batch download...")
    live_prices = fetch_all()
    print("  -> " + str(len(live_prices)) + " prix recus")

    updated = 0
    aberrant = 0
    from_mem = 0

    for ticker in YF_MAP:
        yf_price  = live_prices.get(ticker)
        mem_entry = memory.get(ticker, {})
        mem_price = mem_entry.get("price", 0)

        if yf_price:
            if init_mode or mem_price == 0:
                ok = True
            else:
                var = abs(yf_price - mem_price) / mem_price
                ok = var <= 0.80

            if ok:
                content, changed = update_price_in_content(content, ticker, yf_price, mem_price or yf_price)
                if changed:
                    memory[ticker] = {"price": yf_price, "date": now_str, "source": "yahoo"}
                    updated += 1
            else:
                pct = abs(yf_price - mem_price) / mem_price * 100 if mem_price else 0
                print("  Rejete " + ticker + ": " + str(yf_price) + " vs memoire " + str(mem_price) + " (" + str(round(pct)) + "%)")
                aberrant += 1
        else:
            if mem_price:
                from_mem += 1

    save_memory(memory)

    content = re.sub(
        r'\d+ cours mis \xE0 jour[^<"\')\]]*',
        str(updated) + " cours mis a jour le " + now_str,
        content
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("")
    print("OK Mis a jour : " + str(updated))
    print("Memoire       : " + str(from_mem))
    print("Rejetes       : " + str(aberrant))
    print("Couverture    : " + str(round(updated / len(YF_MAP) * 100)) + "% (" + str(updated) + "/" + str(len(YF_MAP)) + ")")
