#!/usr/bin/env python3
"""
VAL.PEA Screener - Mise à jour prix, volumes et momentum
Données récupérées : prix, variation, volume, ratio volume vs moyenne 20j
"""
import re, time, sys
from datetime import datetime

try:
    import yfinance as yf
    import numpy as np
except:
    import subprocess
    subprocess.check_call([sys.executable,"-m","pip","install","yfinance","numpy","--quiet","--break-system-packages"])
    import yfinance as yf
    import numpy as np

YAHOO = {
    "ABCA": "ABCA.PA", "ABIVAX": "ABVX.PA", "AC": "AC.PA", "ACA": "ACA.PA",
    "ADYEN": "ADYEN.AS", "AF": "AF.PA", "AI": "AI.PA", "AIR": "AIR.PA",
    "ALBIA": "ALBIA.PA", "ALCLF": "ALCLA.PA", "ALIDS": "ALIDS.PA",
    "ALMKT": "ALMKT.PA", "ALO": "ALO.PA", "ALSEI": "ALSEI.PA",
    "ALTAREA": "ALTA.PA", "ALTGX": "ALTX.PA", "ALV": "ALV.DE",
    "ARGAN": "ARG.PA", "ASML": "ASML.AS", "ATO": "ATO.PA", "AXA": "CS.PA",
    "BIOM": "BIM.PA", "BN": "BN.PA", "BNP": "BNP.PA", "BOIRON": "BOI.PA",
    "CA": "CA.PA", "CAP": "CAP.PA", "CDRCK": "CDR.PA", "CHSR": "CAS.PA",
    "CLASQUIN": "ALCLA.PA", "CNP": "CNP.PA", "COFA": "COFA.PA",
    "COVIVIO": "COV.PA", "DALET": "DLT.PA", "DASSAV": "AM.PA",
    "DBG": "DBG.PA", "DBV": "DBV.PA", "DG": "DG.PA", "DIOR": "CDI.PA",
    "DSY": "DSY.PA", "EDENRED": "EDEN.PA", "EIFFAGE": "FGR.PA",
    "EL": "EL.PA", "ELIOR": "ELIOR.PA", "ELIS": "ELIS.PA",
    "EMEIS": "EMEIS.PA", "EN": "EN.PA", "ENGI": "ENGI.PA",
    "ENVEA": "ALENV.PA", "ERF": "ERF.PA", "ESKER": "ALESK.PA",
    "FREY": "FREY.PA", "FNAC": "FNAC.PA", "FORVIA": "FRVIA.PA",
    "ALFPC": "ALFPC.PA", "GALIMMO": "GALIM.PA", "GLE": "GLE.PA",
    "GTT": "GTT.PA", "HEIA": "HEIA.AS", "HIPAY": "HIP.PA", "HO": "HO.PA",
    "ICAD": "ICAD.PA", "IMERYS": "NK.PA", "INTERPARFUMS": "ITP.PA",
    "IPSEN": "IPN.PA", "IPSOS": "IPS.PA", "JXS": "JXS.PA",
    "KER": "KER.PA", "KLPI": "LI.PA", "LACROIX": "LACR.PA",
    "LDLC": "ALLDL.PA", "LECTRA": "LSS.PA", "LEGRAND": "LR.PA",
    "LISI": "FII.PA", "LNA": "LNA.PA", "LR": "LR.PA", "MC": "MC.PA",
    "MERCIALYS": "MERY.PA", "ML": "ML.PA", "MANITOU": "MTU.PA",
    "MT": "MT.AS", "NAMR": "ALNAM.PA", "NEXANS": "NEX.PA",
    "NEXTY": "NXI.PA", "NOVO": "NOVO-B.CO", "OR": "OR.PA", "ORA": "ORA.PA",
    "ORPEA": "ORP.PA", "PERNOD": "RI.PA", "PLASTIC": "POM.PA",
    "PLUXEE": "PLX.PA", "PRECIA": "PREC.PA", "PRX": "PRX.AS",
    "PUB": "PUB.PA", "RADIALL": "RAL.PA", "RCO": "RCO.PA",
    "REXEL": "RXL.PA", "RI": "RI.PA", "RMS": "RMS.PA", "RNO": "RNO.PA",
    "SAF": "SAF.PA", "SAMSE": "SAMS.PA", "SAN": "SAN.PA", "SAP": "SAP.DE",
    "SEB": "SK.PA", "SGO": "SGO.PA", "SIEMENS": "SIE.DE", "SIIGRP": "SII.PA",
    "SIPH": "SIPH.PA", "SOLVB": "SOLB.BR", "SOP": "SOP.PA",
    "SPIE": "SPIE.PA", "STEF": "STF.PA", "STM": "STM.PA", "SU": "SU.PA",
    "SW": "SW.PA", "SYENSQO": "SYENSQO.BR", "TEP": "TEP.PA",
    "THERMD": "THEP.PA", "TIXEO": "ALTXO.PA", "TRIGANO": "TRI.PA",
    "TTE": "TTE.PA", "URW": "URW.AS", "VALO": "FR.PA", "VIE": "VIE.PA",
    "VIRBAC": "VIRP.PA", "VIV": "VIV.PA", "VK": "VK.PA",
    "WAGA": "WAGA.PA", "WLN": "WLN.PA", "SFERACO": "SFR.PA",
    "SECTORIEL": "SEC.PA", "DISTRILABO": "DLAB.PA",
}

def get_data(yf_ticker):
    """Récupère prix, variation, volume et ratio volume vs moyenne 20j"""
    for tentative in range(2):
        try:
            t = yf.Ticker(yf_ticker)
            # Historique 30 jours pour calculer volume moyen
            hist = t.history(period="30d")
            if len(hist) >= 2:
                p     = round(float(hist["Close"].iloc[-1]), 2)
                prev  = round(float(hist["Close"].iloc[-2]), 2)
                chg   = round((p - prev) / prev * 100, 2) if prev else 0
                vol   = int(hist["Volume"].iloc[-1]) if "Volume" in hist else 0
                # Volume moyen 20 séances
                vol20 = int(hist["Volume"].tail(20).mean()) if len(hist) >= 5 else vol
                # Ratio : 1.0 = normal, >1.5 = accumulation, <0.5 = désintérêt
                vratio = round(vol / vol20, 2) if vol20 > 0 else 1.0
                if p > 0:
                    return p, chg, vol, vol20, vratio
        except:
            pass
        time.sleep(0.3)
    return None, None, None, None, None

def maj_html(resultats):
    """Met à jour prix, chg, volume et vratio dans index.html"""
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    mis_a_jour = 0
    for ticker, (p, chg, vol, vol20, vratio) in resultats.items():
        if not p or p <= 0:
            continue

        avant = "ticker:'" + ticker + "'"
        if avant not in html:
            continue

        # Mise à jour prix + chg (existant)
        pattern = "(" + re.escape(avant) + r"[^{]{0,200}?price:)[\d.]+?(,chg:)[-\d.]+"
        nouveau, n = re.subn(
            pattern,
            r"\g<1>" + str(p) + r"\g<2>" + str(chg),
            html, flags=re.DOTALL
        )
        if n > 0:
            html = nouveau
            mis_a_jour += 1

            # Mise à jour volume si le champ existe déjà
            if vratio is not None:
                pat_vol = "(" + re.escape(avant) + r"[^{]{0,300}?vratio:)[\d.]+"
                html, nv = re.subn(
                    pat_vol,
                    r"\g<1>" + str(vratio),
                    html, flags=re.DOTALL
                )

            print(f"  OK {ticker}: {p}€ ({chg:+.2f}%) vol×{vratio}")
        else:
            print(f"  ?? {ticker}: pattern non trouvé")

    # Timestamp
    ts = datetime.now().strftime("%d/%m/%Y %H:%M")
    html = re.sub(
        r"Données indicatives|Mis a jour [\d/]+ [\d:]+",
        "Mis a jour " + ts, html, count=1
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\nTotal: {mis_a_jour}/{len(resultats)} mis à jour — {ts}")
    return mis_a_jour

if __name__ == "__main__":
    print("=" * 55)
    print(f"VAL.PEA Prix + Volume — {len(YAHOO)} tickers")
    print(f"Début: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 55)

    resultats = {}
    erreurs = 0
    for i, (pea, yf_t) in enumerate(YAHOO.items(), 1):
        sys.stdout.write(f"[{i:3d}/{len(YAHOO)}] {pea:12s} ({yf_t:15s}) ")
        sys.stdout.flush()
        p, chg, vol, vol20, vratio = get_data(yf_t)
        if p:
            print(f"-> {p}€ ({chg:+.2f}%) vol×{vratio}")
        else:
            print("-> ECHEC")
            erreurs += 1
        resultats[pea] = (p, chg, vol, vol20, vratio)
        time.sleep(0.12)

    print(f"\nYahoo: {len(YAHOO)-erreurs}/{len(YAHOO)} OK")
    maj_html(resultats)
    print("Terminé!")
