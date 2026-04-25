#!/usr/bin/env python3
"""
update_prices_v2.py - GitHub Actions script
Runs every weekday at 17:35 + every Friday at 18:00 (full recalibration)
1. Updates live prices for ALL 223 tickers from Yahoo Finance
2. On Friday: recalibrates el/eh/stop/o1/o2/dcfm when price drifts >15%
"""

import re, json, sys, os
from datetime import datetime
import urllib.request

def fetch_price(yf_ticker):
    """Fetch live price from Yahoo Finance v8"""
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

def recalibrate_zones(old_price, new_price, el, eh, stop, o1, o2, dcfb, dcfm, dcfu):
    """Scale all zones proportionally when price drifts >15%"""
    if old_price <= 0 or new_price <= 0:
        return el, eh, stop, o1, o2, dcfb, dcfm, dcfu
    ratio = new_price / old_price
    new_el   = round(el   * ratio, 1)
    new_eh   = round(eh   * ratio, 1)
    new_stop = round(stop * ratio, 1)
    new_o1   = round(o1   * ratio, 1)
    new_o2   = round(o2   * ratio, 1)
    new_dcfb = round(dcfb * ratio, 1)
    new_dcfm = round(dcfm * ratio, 1)
    new_dcfu = round(dcfu * ratio, 1)
    assert new_stop < new_price, f"stop {new_stop} >= price {new_price}"
    assert new_o1   > new_price, f"o1 {new_o1} <= price {new_price}"
    assert new_dcfm > new_price * 0.9, f"dcfm {new_dcfm} too low vs price {new_price}"
    return new_el, new_eh, new_stop, new_o1, new_o2, new_dcfb, new_dcfm, new_dcfu

# ─── MAPPING COMPLET 223 TICKERS → YAHOO FINANCE ─────────────────────────
YF_MAP = {
    # CAC 40
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA',
    'ORA':'ORA.PA','VIE':'VIE.PA','RNO':'RNO.PA','SGO':'SGO.PA','CAP':'CAP.PA',
    'DG':'DG.PA','VIV':'VIV.PA','LR':'LR.PA','WLN':'WLN.PA','DSY':'DSY.PA',
    'STM':'STM.PA','EL':'EL.PA','ML':'ML.PA','ENGI':'ENGI.PA','HO':'HO.PA',
    'AC':'AC.PA','AF':'AF.PA','BN':'BN.PA','EN':'EN.PA','SW':'SW.PA',
    'MT':'MT.AS','URW':'URW.AS','RI':'RI.PA',
    # SBF 120 / Grandes caps
    'GTT':'GTT.PA','ELIS':'ELIS.PA','SEB':'SK.PA','ERF':'ERF.PA',
    'COFA':'COFA.PA','SPIE':'SPIE.PA','ALO':'ALO.PA','EDENRED':'EDEN.PA',
    'BVI':'BVI.PA','FDJ':'FDJ.PA','NRO':'NRO.PA','PERNOD':'RI.PA',
    'IPSEN':'IPN.PA','REXEL':'RXL.PA','SOP':'SOP.PA',
    'LNA':'LNA.PA','ABCA':'ABCA.PA','VK':'VK.PA','FNAC':'FNAC.PA',
    'CNP':'CNP.PA','KLPI':'LI.PA','EIFFAGE':'FGR.PA','NEXANS':'NEX.PA',
    'PLUXEE':'PLX.PA','FORVIA':'FRVIA.PA',
    'DIOR':'CDI.PA','IMERYS':'NK.PA','IPSOS':'IPS.PA',
    # International
    'ASML':'ASML.AS','NOVO':'NOVO-B.CO','SAP':'SAP.DE',
    'ADYEN':'ADYEN.AS','HEIA':'HEIA.AS','SIEMENS':'SIE.DE','ALV':'ALV.DE',
    'SOLVB':'SOLB.BB','SYENSQO':'SYENS.BB','PRX':'PRX.AS',
    # Midcaps
    'LECTRA':'LSS.PA','ARGAN':'ARG.PA','FREY':'FREY.PA',
    'COVIVIO':'COV.PA','ALTAREA':'ALTA.PA','DERICHEBOURG':'DBG.PA','DBG':'DBG.PA',
    'CLASQUIN':'ALCLA.PA','ALCLF':'ALCLA.PA',
    'INTERPARFUMS':'ITP.PA','INTPRF':'ITP.PA',
    'STEF':'STF.PA','STEF2':'STF.PA',
    'THERMADOR':'THEP.PA','THERMD':'THEP.PA',
    'LISI':'FII.PA','MANITOU':'MTU.PA',
    'SAMSE':'SAMS.PA','ELIOR':'ELIOR.PA','BIOM':'BIM.PA',
    'LACROIX':'LACR.PA','LACBX':'LACR.PA',
    'DASSAV':'AM.PA','EMEIS':'EMEIS.PA','ORPEA':'ORP.PA',
    'MERCIALYS':'MRY.PA','MERY':'MRY.PA',
    'IDLG':'IDL.PA','EUFSCI':'ERF.PA',
    'LDLC':'LDLC.PA','LDLCG':'LDLC.PA',
    'PLFRY':'PLX.PA','RXLSA':'RXL.PA','PRNRD':'RI.PA',
    'VALO':'FR.PA','LEGRAND':'LR.PA',
    'TEP':'TEP.PA','TALY':'TEP.PA',
    'ALBIA':'ABIO.PA','ALIDS':'ALIDS.PA','ALFPC':'ALFPC.PA',
    'NAMR':'NAMR.PA','NAMREN':'NAMR.PA',
    'KZATM':'KZK.PA','ATO':'ATO.PA','ICAD':'ICA.PA',
    'SELENV':'SELER.PA','SIPH':'SIPH.PA',
    'ENVEA':'ENVEA.PA','JXS':'JXS.PA','JACMETL':'JXS.PA',
    'WAGA':'WGAEN.PA','WGAEN':'WGAEN.PA',
    'IPSNF':'IPN.PA','DALET':'DLT.PA',
    'ABIVAX':'ABVX.PA','ABIVXA':'ABVX.PA','NANOBT':'ABVX.PA','NBNTX':'ABVX.PA',
    'PLASTIC':'POM.PA','RCO':'RCO.PA',
    'SCBSM':'SCBSM.PA','SIIGRP':'SII.PA',
    'VRMTX':'VRM.PA','FIGEAC':'FGA.PA','FGAERO':'FGA.PA',
    'GLEVT':'GLE.PA','LVMHF':'MC.PA',
    'TRIGANO':'TRI.PA','TRGO':'TRI.PA',
    'BOIRON':'BOI.PA',
    'VIRBAC':'VIRP.PA','VIRB2':'VIRP.PA',
    'ALSTOM':'ALO.PA',
    # Nouveaux ajouts
    'AMF':'AMUN.PA','AK':'AKE.PA','RUI':'RUI.PA','SOI':'SOI.PA',
    'GFC':'GFC.PA','WLX':'WLN.PA','NXI':'NXI.PA',
    # Smallcaps ML*
    'MLJR':'JRS.PA','MLKAG':'KAG.PA','MLHRZ':'HRZ.PA',
    'MLHAG':'HAG.PA','MLHRT':'HRT.PA','MLINS':'INS.PA','MLAEP':'AEP.PA',
    'MLAFF':'AFF.PA','MLALW':'ALW.PA','MLARDK':'ARDK.PA',
    'MLBCF':'BCF.PA','MLBFF':'BFF.PA','MLBLT':'BLT.PA',
    'MLCFT':'CFT.PA','MLCHG':'CHG.PA','MLCOB':'COB.PA',
    'MLFNIV':'FNIV.PA','MLLBP':'LBP.PA','MLMCD':'MCD.PA',
    'MLNMG':'NMG.PA','MLNMX':'NMX.PA','MLNRD':'NRD.PA',
    'MLPFT':'PFT.PA','MLPHI':'PHI.PA','MLPSB':'PSB.PA',
    'MLPVR':'PVR.PA','MLRLV':'RLV.PA','MLSBS':'SBS.PA',
    'MLSMD':'SMD.PA','MLTPX':'TPX.PA','MLVAL':'VAL.PA',
    'MLVPN':'VPN.PA','MLVRB':'VRB.PA','MLXIV':'XIV.PA',
    'MLAERO':'AERO.PA','MLGOM':'GOM.PA',
    # Divers
    'CA':'CA.PA','CDRCK':'CDK.PA','CHSR':'CAS.PA',
    'COGEFI':'COFA.PA','DIOR':'CDI.PA','DIORCDI':'CDI.PA',
    'ELECOR':'ELEC.PA','ESCAP':'ESCAP.PA','GALIMMO':'GALIM.PA',
    'GENIE':'GENI.PA','HIPAY':'HPI.PA','HMSNW':'HMS.PA',
    'IDSF':'IDS.PA','ITRLN':'ITL.PA','BNENF':'BNF.PA',
    'LPE':'LPE.PA','NEXTY':'NEXO.PA','TIXEO':'TIXEO.PA',
    'SSYNQ':'SSYNQ.PA','WTRGP':'WTR.PA','SFCA':'WLN2.PA',
    'SODITECH':'SDT.PA','SEQENS':'SEQENS.PA','PRECIA':'PREC.PA',
    'RADIALL':'RAL.PA','LNSBN':'LNS.PA','ALMKT':'ALMKT.PA',
    'ALTGX':'ALTGX.PA','ALSEI':'ALSEI.PA','CSTEU':'CST.PA',
    'DBV':'DBV.PA','OPM':'VRLA.PA',
}

# ─── MAIN ──────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    html_file = 'index.html'
    if not os.path.exists(html_file):
        print(f"ERROR: {html_file} not found")
        sys.exit(1)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    is_friday = datetime.now().weekday() == 4
    is_full_recalibration = '--full' in sys.argv or is_friday

    print(f"Mode: {'VENDREDI — Recalibration complète' if is_full_recalibration else 'Mise à jour prix quotidienne'}")
    print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"Tickers avec mapping YF: {len(YF_MAP)}")
    print("="*50)

    updated = 0
    recalibrated = 0
    errors = []
    skipped = 0

    # Find S[] bounds
    s_start = content.find("const S=[")
    s_end_match = re.search(r'\n\];\s*\n\s*\n\s*// ═+\s*CALENDRIER', content[s_start:])
    if not s_end_match:
        # Fallback: chercher la fin de S[] autrement
        s_end_match = re.search(r'\n\];\s*\n', content[s_start:])
    if not s_end_match:
        print("ERROR: Could not find end of S[]")
        sys.exit(1)
    s_end = s_start + s_end_match.start()

    # Process each stock
    for m in re.finditer(r"(\{ticker:'([^']+)'.*?)(?=\n\n\{ticker:|\n\n\];)",
                          content[s_start:s_end], re.DOTALL):
        block = m.group(1)
        ticker = m.group(2)

        yf = YF_MAP.get(ticker)
        if not yf:
            skipped += 1
            continue

        def gn(key, text=block):
            mx = re.search(r'\b'+key+r':([\d.]+)', text)
            return float(mx.group(1)) if mx else None

        old_price = gn('price')
        if not old_price:
            continue

        new_price = fetch_price(yf)
        if not new_price:
            errors.append(f"{ticker}({yf}): no price")
            continue

        new_block = block
        chg = round((new_price - old_price) / old_price * 100, 2) if old_price else 0
        new_block = re.sub(r'\bprice:[\d.]+', f'price:{new_price}', new_block, count=1)
        new_block = re.sub(r'\bchg:[-\d.]+', f'chg:{chg}', new_block, count=1)
        updated += 1

        # Vendredi ou drift >15%: recalibrer les zones
        drift = abs(new_price - old_price) / old_price if old_price else 0
        if is_full_recalibration or drift > 0.15:
            el=gn('el'); eh=gn('eh'); stop=gn('stop')
            o1=gn('o1'); o2=gn('o2')
            dcfb=gn('dcfb'); dcfm=gn('dcfm'); dcfu=gn('dcfu')
            if all(v is not None for v in [el,eh,stop,o1,o2,dcfb,dcfm,dcfu]):
                try:
                    new_el,new_eh,new_stop,new_o1,new_o2,new_dcfb,new_dcfm,new_dcfu = \
                        recalibrate_zones(old_price,new_price,el,eh,stop,o1,o2,dcfb,dcfm,dcfu)
                    for key,val in [('el',new_el),('eh',new_eh),('stop',new_stop),
                                     ('o1',new_o1),('o2',new_o2),('dcfb',new_dcfb),
                                     ('dcfm',new_dcfm),('dcfu',new_dcfu)]:
                        new_block = re.sub(r'\b'+key+r':[\d.]+', key+':'+str(val), new_block, count=1)
                    recalibrated += 1
                    if drift > 0.05:
                        print(f"  RECALIBRÉ {ticker}: {old_price}€ → {new_price}€ ({drift*100:.1f}%)")
                except AssertionError as e:
                    errors.append(f"{ticker}: {e}")

        if new_block != block:
            block_start = s_start + m.start()
            block_end = block_start + len(block)
            content = content[:block_start] + new_block + content[block_end:]

    # Timestamp dans le header
    ts = datetime.now().strftime('%d/%m à %H:%M')
    content = re.sub(
        r'(\d+ cours mis à jour[^<"\)]*)',
        f'{updated} cours mis à jour le {ts} ({len(errors)} échecs)',
        content
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ {updated} prix mis à jour")
    print(f"✅ {recalibrated} zones recalibrées (vendredi={is_friday})")
    print(f"⏭  {skipped} tickers sans mapping YF")
    if errors:
        print(f"⚠️  {len(errors)} erreurs: {errors[:5]}")
    sys.exit(0)
