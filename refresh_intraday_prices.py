#!/usr/bin/env python3
"""
VAL.PEA -- Rafraichissement rapide des prix en heures de marche.
Remplace l'ancien fetchLive() cote navigateur (proxies CORS publics
corsproxy.io / api.allorigins.win, morts depuis des mois -- 0 succes
sur 441 runs consecutifs, cf audit du 26/08/2026).

Ne touche que price + chg (pas les fondamentaux, deja geres par
fetch_fundamentals.py 2x/jour). Utilise yfinance.fast_info, beaucoup
plus rapide que .info pour juste un prix, avec repli sur history()
si un ticker donne echoue silencieusement (audit du 04/09/2026).

Declenche par GitHub Actions toutes les heures, Lun-Ven, heures de marche.
"""
import yfinance as yf
import re
from datetime import datetime
import pytz

PARIS = pytz.timezone('Europe/Paris')

# Mapping ticker interne -> symbole Yahoo Finance
# (porte depuis le YF_MAP cote JS de index.html, plus complet que
#  celui de fetch_fundamentals.py -- couvre aussi les mid/small caps)
YF_MAP = {
    "MC":"MC.PA","AI":"AI.PA","OR":"OR.PA","RMS":"RMS.PA","SAN":"SAN.PA",
    "TTE":"TTE.PA","SAF":"SAF.PA","SU":"SU.PA","AXA":"CS.PA","BNP":"BNP.PA",
    "ACA":"ACA.PA","GLE":"GLE.PA","AIR":"AIR.PA","KER":"KER.PA","PUB":"PUB.PA",
    "ORA":"ORA.PA","VIE":"VIE.PA","RNO":"RNO.PA","SGO":"SGO.PA","CAP":"CAP.PA",
    "DG":"DG.PA","VIV":"VIV.PA","LR":"LR.PA","DSY":"DSY.PA","EL":"EL.PA",
    "ENGI":"ENGI.PA","HO":"HO.PA","EN":"EN.PA","BN":"BN.PA","AC":"AC.PA",
    "AF":"AF.PA","CA":"CA.PA","RI":"RI.PA","URW":"URW.AS","TEP":"TEP.PA",
    "STM":"STM.MI","ML":"ML.PA","WLN":"WLN.PA","SEB":"SK.PA","IPSOS":"IPS.PA",
    "GTT":"GTT.PA","ELIS":"ELIS.PA","ERF":"ERF.PA","COFA":"COFA.PA",
    "SPIE":"SPIE.PA","FNAC":"FNAC.PA","LNA":"LNA.PA","SOP":"SOP.PA",
    "NEXANS":"NEX.PA","VK":"VK.PA","SW":"SW.PA","MERY":"MERY.PA",
    "IPSEN":"IPN.PA","REXEL":"RXL.PA","ALTEN":"ATE.PA","IMERYS":"NK.PA",
    "FORVIA":"FRVIA.PA","EIFFAGE":"FGR.PA","TRIGANO":"TRI.PA","DASSAV":"AM.PA",
    "ASML":"ASML.AS","PRX":"PRX.AS","ADYEN":"ADYEN.AS","MT":"MT.AS",
    "SAP":"SAP.DE","ALV":"ALV.DE","HEIA":"HEIA.AS","SIEMENS":"SIE.DE",
    "NOVO":"NOVO-B.CO","COVIVIO":"COV.PA","STEF":"STF.PA","ARGAN":"ARG.PA",
    "INTERPARFUMS":"ITP.PA","LECTRA":"LSS.PA","LISI":"FII.PA","VIRBAC":"VIRP.PA",
    "ABIVAX":"ABVX.PA","BOIRON":"BOI.PA","THERMADOR":"THEP.PA","WAGA":"WAGA.PA",
    "LACROIX":"LACR.PA","MANITOU":"MTU.PA","FIGEAC":"FGA.PA","SAMSE":"SAMS.PA",
    "ALTAREA":"ALTA.PA","DERICHEBOURG":"DBG.PA","NRO":"NRO.PA","RUI":"RUI.PA",
    "JXS":"JCQ.PA","CNP":"CNP.PA","ABCA":"ABCA.PA",
    "ATO":"ATO.PA","SYENSQO":"SYENSQO.BR","ICAD":"ICAD.PA","NXI":"NXI.PA",
    "GFC":"GFC.PA","EMEIS":"EMEIS.PA","ELIOR":"ELIOR.PA",
    "ALSTOM":"ALO.PA"
}
# Taux de conversion devise -> EUR (pour tickers hors zone euro)
NON_EUR = {"NOVO-B.CO": 7.46}


import time

def fetch_one_with_retry(sym, tks):
    """Essaie fast_info, retente une fois apres une pause, puis se
    rabat sur history() -- un endpoint Yahoo different, generalement
    plus fiable pour un simple cours de cloture -- si fast_info reste
    muet. Avant ce correctif, un ticker capricieux (ex: EL.PA) restait
    silencieusement fige indefiniment, sans aucune erreur visible
    (audit du 04/09/2026)."""
    for attempt in range(2):
        try:
            fi = tks.tickers[sym].fast_info
            price = fi.get('last_price') or fi.get('lastPrice')
            prev = fi.get('previous_close') or fi.get('previousClose')
            if price and price > 0.05:
                return price, prev
        except Exception:
            pass
        if attempt == 0:
            time.sleep(1.5)
    try:
        h = yf.Ticker(sym).history(period='2d')
        if not h.empty:
            price = float(h['Close'].iloc[-1])
            prev = float(h['Close'].iloc[-2]) if len(h) > 1 else price
            if price > 0.05:
                return price, prev
    except Exception:
        pass
    return None, None


def fetch_all():
    yf_syms = list(dict.fromkeys(YF_MAP.values()))  # dedupe (ALSTOM/ALO doublon)
    rev = {}
    for tk, sym in YF_MAP.items():
        rev.setdefault(sym, []).append(tk)

    out = {}
    failed = []
    tks = yf.Tickers(' '.join(yf_syms))
    for sym in yf_syms:
        price, prev = fetch_one_with_retry(sym, tks)
        if not price:
            failed.append(sym)
            continue
        fx = NON_EUR.get(sym, 1)
        price_eur = round(price / fx, 2)
        chg = round((price / prev - 1) * 100, 2) if prev else 0
        for tk in rev[sym]:
            out[tk] = (price_eur, chg)
    if failed:
        print(f"  ECHEC malgre repli pour {len(failed)} valeur(s) : {', '.join(failed)}")
    return out


def patch_data_js(quotes):
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    for ticker, (price, chg) in quotes.items():
        tp = content.find(f"ticker:'{ticker}'")
        if tp == -1:
            continue
        np = content.find("ticker:'", tp + 1)
        block_end = np if np > -1 else len(content)
        block = content[tp:block_end]
        nb = re.sub(r'price:[+-]?\d+\.?\d*', f'price:{price}', block, count=1)
        if nb != block:
            block = nb
            updated += 1
        nb2 = re.sub(r'chg:[+-]?\d+\.?\d*', f'chg:{chg}', block, count=1)
        if nb2 != block:
            block = nb2
        content = content[:tp] + block + content[block_end:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    return updated


def main():
    now = datetime.now(PARIS)
    print(f"VAL.PEA -- refresh intraday -- {now.strftime('%Y-%m-%d %H:%M')} Paris")
    quotes = fetch_all()
    print(f"{len(quotes)}/{len(YF_MAP)} cours recuperes")
    if not quotes:
        print("ECHEC total -- aucun commit, on ne veut pas ecraser data.js avec du vide")
        return
    updated = patch_data_js(quotes)
    print(f"data.js : {updated} tickers mis a jour")


if __name__ == '__main__':
    main()
