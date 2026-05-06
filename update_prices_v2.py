#!/usr/bin/env python3
"""
update_prices_v2.py — VAL.PEA
Système de prix avec mémoire persistante.

Principe :
  - Chaque run lit prices_memory.json (dernier prix valide connu)
  - Si Yahoo Finance retourne un prix cohérent → on met à jour la mémoire ET index.html
  - Si Yahoo Finance retourne une aberration → on utilise le prix en mémoire
  - La mémoire s'enrichit run après run — jamais de régression

prices_memory.json = source de vérité des derniers prix valides
"""

import re, json, sys, os
from datetime import datetime
import urllib.request

MEMORY_FILE = 'prices_memory.json'
MAX_VARIATION = 0.40   # 40% max entre 2 runs consécutifs
MIN_PRICE     = 0.50   # Prix minimum acceptable (évite les centimes)

# ─── MAPPING YAHOO FINANCE ─────────────────────────────────────────
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
    'FNAC':'FNAC.PA','CNP':'CNP.PA','EIFFAGE':'FGR.PA','NEXANS':'NEX.PA',
    'FORVIA':'FRVIA.PA','IMERYS':'NK.PA','IPSOS':'IPS.PA',
    'ASML':'ASML.AS','NOVO':'NOVO-B.CO','PRX':'PRX.AS',
    'HEIA':'HEIA.AS','ADYEN':'ADYEN.AS',
    'LECTRA':'LSS.PA','ARGAN':'ARG.PA','FREY':'FREY.PA',
    'COVIVIO':'COV.PA','DERICHEBOURG':'DBG.PA',
    'STEF':'STF.PA','THERMADOR':'THEP.PA','LISI':'FII.PA',
    'MANITOU':'MTU.PA','SAMSE':'SAMS.PA','ELIOR':'ELIOR.PA',
    'TRIGANO':'TRI.PA','BOIRON':'BOI.PA','VIRBAC':'VIRP.PA',
    'DIOR':'CDI.PA','EDEN':'EDEN.PA','PLXEE':'PLX.PA',
    'NXI':'NXI.PA','ATO':'ATO.PA','RUI':'RUI.PA',
    'WAGA':'WGAEN.PA','ABIVAX':'ABVX.PA','FIGEAC':'FGA.PA',
    'SOI':'SOI.PA','ALTEN':'ATE.PA','SWORD':'SWP.PA',
    'SEB':'SK.PA','MT':'MT.AS','VK':'VK.PA','JXS':'JXS.PA',
    'NEXANS':'NEX.PA','REXEL':'RXL.PA',
}

# ─── MÉMOIRE PERSISTANTE ──────────────────────────────────────────
def load_memory():
    """Charge la mémoire des derniers prix valides"""
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {}

def save_memory(memory):
    """Sauvegarde la mémoire des prix valides"""
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

def is_aberrant(new_price, memory_price, b52h=None, b52l=None):
    """
    Détecte un prix aberrant en comparant avec la mémoire
    et le range 52 semaines.
    """
    if new_price < MIN_PRICE:
        return True, f"prix trop bas ({new_price})"

    if memory_price and memory_price > 0:
        variation = abs(new_price - memory_price) / memory_price
        if variation > MAX_VARIATION:
            return True, f"variation {variation*100:.0f}% vs mémoire {memory_price}"

    if b52h and b52l and b52l > 0:
        # Tolérance 50% au-delà du range (marché peut bouger fort)
        if new_price < b52l * 0.50 or new_price > b52h * 1.50:
            return True, f"hors range 52S [{b52l}-{b52h}] × 1.5"

    return False, ""

# ─── FETCH PRIX ───────────────────────────────────────────────────
def fetch_price(yf_ticker):
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{yf_ticker}?interval=1d&range=1d"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        meta = data['chart']['result'][0]['meta']
        price = meta.get('regularMarketPrice') or meta.get('previousClose')
        return round(float(price), 2) if price else None
    except:
        return None

# ─── MAIN ─────────────────────────────────────────────────────────
if __name__ == '__main__':
    html_file = 'index.html'
    if not os.path.exists(html_file):
        print(f"ERROR: {html_file} not found")
        sys.exit(1)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    is_friday = datetime.now().weekday() == 4
    now_str = datetime.now().strftime('%d/%m à %H:%M')

    # Charger la mémoire
    memory = load_memory()
    print(f"Mémoire chargée : {len(memory)} prix en mémoire")
    print(f"Mode : {'VENDREDI — recalibration complète' if is_friday else 'Mise à jour quotidienne'}")
    print("=" * 55)

    s_start = content.find("const S=[")
    if s_start < 0:
        print("ERROR: S[] non trouvé")
        sys.exit(1)

    updated     = 0
    from_memory = 0
    aberrant    = 0
    no_yf       = 0

    for m in re.finditer(
        r"(\{ticker:'([^']+)'.*?)(?=\n\n\{ticker:|\n\n\];)",
        content[s_start:], re.DOTALL
    ):
        block  = m.group(1)
        ticker = m.group(2)
        yf     = YF_MAP.get(ticker)

        # Prix actuel dans le fichier
        pm = re.search(r'\bprice:([\d.]+)', block)
        file_price = float(pm.group(1)) if pm else 0

        # Prix en mémoire (dernier prix valide connu)
        mem_price = memory.get(ticker, {}).get('price', file_price)

        # Range 52 semaines
        b52h_m = re.search(r'\bb52h:([\d.]+)', block)
        b52l_m = re.search(r'\bb52l:([\d.]+)', block)
        b52h = float(b52h_m.group(1)) if b52h_m else None
        b52l = float(b52l_m.group(1)) if b52l_m else None

        if not yf:
            no_yf += 1
            # Pas de mapping YF — utiliser la mémoire si disponible
            if mem_price and mem_price != file_price:
                # Mettre à jour depuis mémoire
                new_block = re.sub(r'\bprice:[\d.]+', f'price:{mem_price}', block, count=1)
                if new_block != block:
                    content = content[:s_start + m.start()] + new_block + content[s_start + m.end():]
            continue

        # Récupérer le prix Yahoo Finance
        yf_price = fetch_price(yf)

        if yf_price:
            # Valider le prix
            aberrant_flag, reason = is_aberrant(yf_price, mem_price, b52h, b52l)

            if aberrant_flag:
                # Prix aberrant → utiliser la mémoire
                best_price = mem_price if mem_price else file_price
                aberrant += 1
                print(f"  🚫 {ticker:8} Yahoo={yf_price} ABERRANT ({reason}) → mémoire {best_price}")
            else:
                # Prix valide → mettre à jour mémoire ET fichier
                best_price = yf_price
                memory[ticker] = {
                    'price': yf_price,
                    'date':  datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'source': 'yahoo'
                }
                updated += 1
        else:
            # Yahoo Finance indisponible → utiliser la mémoire
            best_price = mem_price if mem_price else file_price
            from_memory += 1

        # Appliquer le meilleur prix disponible
        if best_price and best_price != file_price:
            chg = round((best_price - mem_price) / mem_price * 100, 2) if mem_price else 0
            new_block = re.sub(r'\bprice:[\d.]+', f'price:{best_price}', block, count=1)
            new_block = re.sub(r'\bchg:[-\d.]+', f'chg:{chg}', new_block, count=1)
            if new_block != block:
                content = content[:s_start + m.start()] + new_block + content[s_start + m.end():]

        # Vendredi : recalibrer les zones si dérive > 15%
        if is_friday and yf_price and not aberrant_flag and mem_price and mem_price > 0:
            drift = abs(yf_price - mem_price) / mem_price
            if drift > 0.15:
                ratio = yf_price / mem_price
                for key in ['el','eh','stop','o1','o2','dcfb','dcfm','dcfu']:
                    km = re.search(r'\b' + key + r':([\d.]+)', block)
                    if km:
                        new_val = round(float(km.group(1)) * ratio, 1)
                        content = content.replace(f'{key}:{km.group(1)}', f'{key}:{new_val}', 1)
                print(f"  📐 {ticker:8} recalibré ({drift*100:.0f}% de dérive)")

    # Sauvegarder la mémoire mise à jour
    save_memory(memory)

    # Mettre à jour le timestamp dans le header
    content = re.sub(
        r'\d+ cours mis à jour[^<"\')\]]*',
        f'{updated} cours mis à jour le {now_str} ({aberrant} aberrants corrigés)',
        content
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ {updated} prix Yahoo Finance valides")
    print(f"📦 {from_memory} prix depuis la mémoire (Yahoo indispo)")
    print(f"🚫 {aberrant} aberrations corrigées automatiquement")
    print(f"⏭  {no_yf} tickers sans mapping YF")
    print(f"💾 Mémoire sauvegardée : {len(memory)} entrées ({MEMORY_FILE})")
