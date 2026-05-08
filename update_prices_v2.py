#!/usr/bin/env python3
"""
update_prices_v2.py — VAL.PEA
Batch download Yahoo Finance + mémoire persistante.
Mise à jour chirurgicale : ne touche que price: et chg: du bon ticker.
v3 — Mai 2026 : force-sync HTML←mémoire, fix AXA/doublon, fallback individuel
"""

import re, json, sys, os, warnings
from datetime import datetime
warnings.filterwarnings("ignore")

try:
    import yfinance as yf
except ImportError:
    print("ERREUR: pip install yfinance")
    sys.exit(1)

MEMORY_FILE   = "prices_memory.json"
MIN_PRICE     = 0.50
NON_EUR       = {"NOVO": 7.46}
FORCE_RESET   = {"NOVO": 50, "WLN": 50, "ATO": 5}

# ── Mappings Yahoo Finance ──────────────────────────────────────────────────
# CORRECTIONS v3:
#   • AXA → AXA.PA  (CS.PA = Credit Suisse, liquidé 2023 !)
#   • DERICHEBOURG supprimé (doublon de DBG, même symbol DBG.PA)
#   • Ajout : ALSTOM, EDENRED, ALV, EMEIS, PLUXEE, FREY, LEGRAND, PERNOD
YF_MAP = {
    # ── CAC 40 ──
    "MC":"MC.PA","AI":"AI.PA","OR":"OR.PA","RMS":"RMS.PA","SAN":"SAN.PA",
    "TTE":"TTE.PA","SAF":"SAF.PA","SU":"SU.PA","AXA":"AXA.PA","BNP":"BNP.PA",
    "ACA":"ACA.PA","GLE":"GLE.PA","AIR":"AIR.PA","KER":"KER.PA","PUB":"PUB.PA",
    "ORA":"ORA.PA","VIE":"VIE.PA","RNO":"RNO.PA","SGO":"SGO.PA","CAP":"CAP.PA",
    "DG":"DG.PA","VIV":"VIV.PA","LR":"LR.PA","DSY":"DSY.PA",
    "EL":"EL.PA","ENGI":"ENGI.PA","HO":"HO.PA","EN":"EN.PA",
    "BN":"BN.PA","AC":"AC.PA","AF":"AF.PA","CA":"CA.PA","RI":"RI.PA",
    "URW":"URW.AS","TEP":"TEP.PA","DIOR":"CDI.PA","STM":"STM.PA",
    "ALSTOM":"ALO.PA","EDENRED":"EDEN.PA","PLUXEE":"PLX.PA",
    # ── SBF 120 / Mid caps ──
    "GTT":"GTT.PA","ELIS":"ELIS.PA","ERF":"ERF.PA","COFA":"COFA.PA",
    "SPIE":"SPIE.PA","BVI":"BVI.PA","FDJ":"FDJ.PA",
    "IPSEN":"IPN.PA","REXEL":"RXL.PA","SOP":"SOP.PA","LNA":"LNA.PA",
    "FNAC":"FNAC.PA","EIFFAGE":"FGR.PA","NEXANS":"NEX.PA","SOI":"SOI.PA",
    "FORVIA":"FRVIA.PA","IMERYS":"NK.PA","ALTEN":"ATE.PA","VK":"VK.PA",
    "SW":"SW.PA","WLN":"WLN.PA","SEB":"SK.PA","IPSOS":"IPS.PA","CNP":"CNP.PA",
    "DBG":"DBG.PA","TRIGANO":"TRI.PA","EMEIS":"EMEIS.PA",
    # ── Européens ──
    "ASML":"ASML.AS","PRX":"PRX.AS","ADYEN":"ADYEN.AS","HEIA":"HEIA.AS",
    "MT":"MT.AS","SAP":"SAP.DE","SIEMENS":"SIE.DE","ALV":"ALV.DE",
    # ── Small caps FR ──
    "NOVO":"NOVO-B.CO","BOIRON":"BOI.PA","VIRBAC":"VIRP.PA",
    "INTERPARFUMS":"ITP.PA","ARGAN":"ARG.PA","LECTRA":"LSS.PA",
    "LISI":"FII.PA","ELIOR":"ELIOR.PA","SAMSE":"SAMS.PA",
    "MANITOU":"MTU.PA","FIGEAC":"FGA.PA","ABIVAX":"ABVX.PA",
    "COVIVIO":"COV.PA","STEF":"STF.PA","THERMADOR":"THEP.PA",
    "LACROIX":"LACR.PA","WAGA":"WGAEN.PA","DASSAV":"AM.PA",
    "FREY":"FREY.PA","LEGRAND":"LR.PA","PERNOD":"RI.PA",
    # ── Autres ──
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
            print(f"  Reset {ticker}: {memory[ticker]['price']}")
            del memory[ticker]
    return memory

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def fetch_batch():
    """Téléchargement en lot Yahoo Finance."""
    symbols = list(set(YF_MAP.values()))
    try:
        data = yf.download(symbols, period="2d", auto_adjust=True,
                           progress=False, threads=True)
        if data.empty:
            return {}
        # Compat yfinance >=0.2 MultiIndex
        try:
            close = data["Close"]
        except Exception:
            close = data.xs("Close", axis=1, level=0)
        # Si Series (un seul ticker téléchargé)
        if not hasattr(close, "columns"):
            close = close.to_frame(name=symbols[0])

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
        print(f"  Batch erreur: {e}")
        return {}

def fetch_individual(tickers_needed):
    """Fallback : téléchargement individuel pour les tickers manquants."""
    results = {}
    for ticker in tickers_needed:
        yf_sym = YF_MAP.get(ticker)
        if not yf_sym:
            continue
        try:
            t_obj = yf.Ticker(yf_sym)
            hist = t_obj.history(period="2d", auto_adjust=True)
            if not hist.empty:
                p = round(float(hist["Close"].dropna().iloc[-1]), 2)
                if ticker in NON_EUR:
                    p = round(p / NON_EUR[ticker], 2)
                if p > MIN_PRICE:
                    results[ticker] = p
        except:
            pass
    return results

def update_price_in_content(content, ticker, new_price, mem_price):
    """
    Mise à jour chirurgicale.
    Cherche ticker:'TICKER' puis remplace price:X et chg:Y dans ce bloc uniquement.
    """
    search = f"ticker:'{ticker}'"
    pos = content.find(search)
    if pos < 0:
        return content, False

    next_ticker = content.find("ticker:'", pos + len(search))
    end_s = content.find("\n];", pos)
    block_end = min(next_ticker if next_ticker > 0 else 999999,
                    end_s if end_s > 0 else 999999)

    block = content[pos:block_end]
    new_block = re.sub(r'\bprice:[\d.]+', f'price:{new_price}', block, count=1)
    if new_block == block:
        return content, False

    chg = round((new_price - mem_price) / mem_price * 100, 2) if mem_price else 0
    new_block = re.sub(r'\bchg:[-\d.]+', f'chg:{chg}', new_block, count=1)

    return content[:pos] + new_block + content[block_end:], True


def sync_html_from_memory(content, memory):
    """
    Force-sync : corrige les prix HTML figés depuis la mémoire persistante.
    Garantit que l'HTML reflète toujours la mémoire, même si un commit
    précédent a échoué ou si l'HTML a été ré-uploadé avec des prix statiques.
    """
    synced = 0
    for ticker, entry in memory.items():
        mem_price = entry.get("price", 0)
        if not mem_price:
            continue
        search = f"ticker:'{ticker}'"
        pos = content.find(search)
        if pos < 0:
            continue
        end_blk_pos = content.find("ticker:'", pos + len(search))
        if end_blk_pos < 0:
            end_blk_pos = pos + 2000
        block = content[pos:end_blk_pos]
        m = re.search(r'\bprice:([\d.]+)', block[:400])
        if not m:
            continue
        html_price = float(m.group(1))
        # Sync si écart > 1%
        if mem_price and abs(html_price - mem_price) / mem_price > 0.01:
            content, changed = update_price_in_content(content, ticker, mem_price, html_price)
            if changed:
                synced += 1
    return content, synced


if __name__ == "__main__":
    if not os.path.exists("index.html"):
        print("ERREUR: index.html introuvable")
        sys.exit(1)

    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    is_friday = datetime.now().weekday() == 4
    now_str   = datetime.now().strftime("%d/%m à %H:%M")

    memory    = load_memory()
    init_mode = len(memory) < 80
    synced    = 0

    print("Source : Yahoo Finance (batch + fallback individuel)")
    print("Mode   : VENDREDI" if is_friday else "Mode   : Quotidien")
    print(f"Mémoire: {len(memory)} entrées" + (" (INIT)" if init_mode else ""))
    print("=" * 55)

    # ── ÉTAPE 1 : Force-sync HTML ← mémoire ─────────────────────────────
    if not init_mode:
        print("Force-sync HTML ← mémoire persistante...")
        content, synced = sync_html_from_memory(content, memory)
        print(f"  -> {synced} prix remis à jour depuis mémoire")
        print()

    # ── ÉTAPE 2 : Download prix live Yahoo Finance ───────────────────────
    print("Batch download...")
    live_prices = fetch_batch()
    print(f"  -> {len(live_prices)}/{len(YF_MAP)} prix reçus")

    # Fallback individuel si <70% couverts
    missing = [t for t in YF_MAP if t not in live_prices]
    if missing and len(missing) < len(YF_MAP) * 0.5:
        print(f"  Fallback individuel ({len(missing)} tickers)...")
        fallback = fetch_individual(missing)
        live_prices.update(fallback)
        print(f"  -> +{len(fallback)} prix récupérés")
    print(f"  -> Total live: {len(live_prices)}")
    print()

    # ── ÉTAPE 3 : Mise à jour chirurgicale ──────────────────────────────
    updated  = 0
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
                ok  = var <= 0.50   # seuil 50% (80% trop laxiste)

            if ok:
                content, changed = update_price_in_content(
                    content, ticker, yf_price, mem_price or yf_price
                )
                if changed:
                    memory[ticker] = {"price": yf_price, "date": now_str, "source": "yahoo"}
                    updated += 1
                else:
                    # Prix inchangé : refresh date mémoire seulement
                    if ticker in memory:
                        memory[ticker]["date"] = now_str
            else:
                pct = abs(yf_price - mem_price) / mem_price * 100
                print(f"  REJETÉ {ticker}: YF={yf_price} vs mém={mem_price} ({round(pct)}%)")
                aberrant += 1
        else:
            if mem_price:
                from_mem += 1

    save_memory(memory)

    # ── Mise à jour statut dans HTML ────────────────────────────────────
    status_new  = f"{updated} cours mis à jour le {now_str}"
    # Chercher pattern existant (unicode ou ascii)
    replaced = False
    for pat in [r'\d+ cours mis \u00e0 jour[^<"\')\]]*',
                r'\d+ cours mis a jour[^<"\')\]]*',
                r'\d+ prices? updated[^<"\')\]]*']:
        if re.search(pat, content):
            content  = re.sub(pat, status_new, content)
            replaced = True
            break

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

    total = updated + synced
    print(f"Mis à jour live  : {updated}")
    print(f"Sync depuis mém  : {synced}")
    print(f"Mémoire (fallback): {from_mem}")
    print(f"Rejetés (>50%)   : {aberrant}")
    print(f"Couverture totale: {round(total / len(YF_MAP) * 100)}% ({total}/{len(YF_MAP)})")
    if not replaced:
        print("⚠  Statut 'cours mis à jour' non trouvé dans HTML — ajouter manuellement")
