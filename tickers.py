"""
VAL.PEA -- Table UNIQUE ticker screener -> symbole Yahoo Finance.

Source de verite partagee par fetch_fundamentals.py et
refresh_intraday_prices.py. Avant le 04/10/2026, chaque script avait sa
propre copie, et 85 fiches de data.js sur 205 n'etaient dans aucune :
leurs prix et fondamentaux etaient figes depuis leur creation (ex. OPM
affiche 18 EUR pour 11,80 EUR reel). Chaque symbole ci-dessous a ete
verifie le 04/10/2026 sur l'API chart de Yahoo (cours < 5 jours).

Regle : toute nouvelle fiche dans data.js DOIT etre ajoutee ici, sinon
check_coverage() la signale a chaque run.
"""

YF_MAP = {
    'MC':'MC.PA', 'AI':'AI.PA', 'OR':'OR.PA', 'RMS':'RMS.PA', 'SAN':'SAN.PA',
    'TTE':'TTE.PA', 'SAF':'SAF.PA', 'SU':'SU.PA', 'AXA':'CS.PA', 'BNP':'BNP.PA',
    'ACA':'ACA.PA', 'GLE':'GLE.PA', 'AIR':'AIR.PA', 'KER':'KER.PA', 'PUB':'PUB.PA',
    'ORA':'ORA.PA', 'VIE':'VIE.PA', 'RNO':'RNO.PA', 'SGO':'SGO.PA', 'CAP':'CAP.PA',
    'DG':'DG.PA', 'VIV':'VIV.PA', 'RI':'RI.PA', 'LR':'LR.PA', 'WLN':'WLN.PA',
    'DSY':'DSY.PA', 'STM':'STMPA.PA', 'EL':'EL.PA', 'ML':'ML.PA', 'ENGI':'ENGI.PA',
    'MT':'MT.AS', 'URW':'URW.PA', 'SW':'SW.PA', 'TEP':'TEP.PA', 'EN':'EN.PA',
    'GTT':'GTT.PA', 'COFA':'COFA.PA', 'MERY':'MERY.PA', 'JXS':'JCQ.PA', 'SPIE':'SPIE.PA',
    'NEXANS':'NEX.PA', 'DASSAV':'AM.PA', 'ALO':'ALO.PA', 'ELIS':'ELIS.PA', 'SEB':'SK.PA',
    'ERF':'ERF.PA', 'IPSOS':'IPS.PA', 'ABCA':'ABCA.PA', 'VK':'VK.PA', 'FNAC':'FNAC.PA',
    'LNA':'LNA.PA', 'SOP':'SOP.PA', 'AC':'AC.PA', 'AF':'AF.PA', 'BN':'BN.PA',
    'CA':'CA.PA', 'HO':'HO.PA', 'ATO':'ATO.PA', 'DBG':'DBG.PA', 'LPE':'LPE.PA',
    'ASML':'ASML.AS', 'PRX':'PRX.AS', 'ADYEN':'ADYEN.AS', 'HEIA':'HEIA.AS', 'NOVO':'NOVO-B.CO',
    'RACE':'RACE.MI', 'SAP':'SAP.DE', 'SIEMENS':'SIE.DE', 'ALV':'ALV.DE', 'BIOM':'BIM.PA',
    'KLPI':'LI.PA', 'RCO':'RCO.PA', 'EIFFAGE':'FGR.PA', 'ALTAREA':'ALTA.PA', 'COVIVIO':'COV.PA',
    'FREY':'FREY.PA', 'CHSR':'CRI.PA', 'VALO':'FR.PA', 'FORVIA':'FRVIA.PA', 'PLUXEE':'PLX.PA',
    'EDENRED':'EDEN.PA', 'OPM':'OPM.PA', 'IMERYS':'NK.PA', 'THERMADOR':'THEP.PA', 'STEF':'STF.PA',
    'TRIGANO':'TRI.PA', 'VIRBAC':'VIRP.PA', 'INTERPARFUMS':'ITP.PA', 'ARGAN':'ARG.PA', 'BOIRON':'BOI.PA',
    'LECTRA':'LSS.PA', 'LACROIX':'LACR.PA', 'IDLG':'IDL.PA', 'ELIOR':'ELIOR.PA', 'WAGA':'WAGA.PA',
    'LDLC':'ALLDL.PA', 'DBV':'DBV.PA', 'HIPAY':'ALHYP.PA', 'LISI':'FII.PA', 'SYENSQO':'SYENS.BR',
    'IPSEN':'IPN.PA', 'REXEL':'RXL.PA', 'FIGEAC':'FGA.PA', 'DIOR':'CDI.PA', 'ABIVAX':'ABVX.PA',
    'NANOBT':'NANO.PA', 'ICAD':'ICAD.PA', 'GLEVT':'GLO.PA', 'VRMTX':'VMX.PA', 'SAMSE':'SAMS.PA',
    'MANITOU':'MTU.PA', 'NEXTY':'NXI.PA', 'SCBSM':'CBSM.PA', 'EMEIS':'EMEIS.PA', 'ALFPC':'ALFPC.PA',
    'SELENV':'SCHP.PA', 'LNSBN':'ALLAN.PA', 'ALTGX':'ALTOU.PA', 'SOLVB':'SOLB.BR', 'BNENF':'BEN.PA',
    'IDSF':'INF.PA', 'GENIE':'GNFT.PA', 'CDRCK':'CARM.PA', 'ADP':'ADP.PA', 'AKE':'AKE.PA',
    'LTA':'LTA.PA', 'BB':'BB.PA', 'ATE':'ATE.PA', 'ANTIN':'ANTIN.PA', 'ELEC':'ELEC.PA',
    'ERA':'ERA.PA', 'RF':'RF.PA', 'ETL':'ETL.PA', 'EXA':'EXA.PA', 'EXENS':'EXENS.PA',
    'FDJU':'FDJU.PA', 'GFC':'GFC.PA', 'GET':'GET.PA', 'DEC':'DEC.PA', 'MMB':'MMB.PA',
    'LOUP':'LOUP.PA', 'MMT':'MMT.PA', 'NRO':'NRO.PA', 'OVH':'OVH.PA', 'PLNW':'PLNW.PA',
    'GDS':'GDS.PA', 'RBT':'RBT.PA', 'RUI':'RUI.PA', 'DIM':'DIM.PA', 'SCR':'SCR.PA',
    'SESG':'SESG.PA', 'TE':'TE.PA', 'TFI':'TFI.PA', 'TKO':'TKO.PA', 'VCT':'VCT.PA',
    'VIL':'VIL.PA', 'WAVE':'WAVE.PA',
}

# Cotations hors euro : diviser par ce taux pour obtenir des EUR.
# (approximatif, a revoir si l'ecart de change devient significatif)
NON_EUR = {'NOVO-B.CO': 7.46}

ETF_TICKERS = {'CW8','PAEEM','PANX','PCEU','GOLDN','ESE','LYPS','RS2K','PINR','PTPXE','DCAM'}


# Fiches retirees de data.js le 04/10/2026 (doublons, societes retirees de
# la cote, introuvables ou hors PEA). Elles affichaient des chiffres ronds
# inventes, jamais mis a jour. purge_data_js() les supprime a chaque run
# (idempotent) -- ne pas les recreer sans symbole Yahoo verifie.
REMOVED = {
    'MERCIALYS': 'doublon MERY',
    'SFCA': 'doublon WLN (Worldline)',
    'PLASTIC': 'doublon OPM',
    'IPSNF': 'doublon IPSEN',
    'RXLSA': 'doublon REXEL',
    'TRGO': 'doublon TRIGANO',
    'THERMD': 'doublon THERMADOR',
    'GTTLNG': 'doublon GTT',
    'ORPEA': 'doublon EMEIS',
    'ELECOR': 'doublon ELEC',
    'LACBX': 'doublon LACROIX',
    'ESKER': 'retirée de la cote (OPA 2024)',
    'ESCAP': 'doublon + retirée',
    'NAMR': 'plus cotée (dernier cours > 1 an)',
    'NAMREN': 'doublon NAMR',
    'ALCLF': 'Clasquin retirée (OPA MSC)',
    'ALBIA': 'Albioma retirée (OPA KKR 2022)',
    'DALET': 'retirée (2022)',
    'GALIMMO': 'introuvable/retirée',
    'SIPH': 'introuvable/retirée',
    'PRECIA': 'introuvable/retirée',
    'RADIALL': 'introuvable/retirée',
    'SEQENS': 'non cotée',
    'TIXEO': 'non cotée',
    'ENVEA': 'introuvable',
    'KZATM': 'cotée Londres/Astana, non PEA',
    'ITRLN': 'Suisse, non éligible PEA',
    'HMSNW': 'cotée en SEK, hors périmètre',
    'ALIDS': 'société introuvable',
    'SODITECH': 'société introuvable',
    'WTRGP': 'non cotée',
    'CSTEU': 'société introuvable',
    'ALMKT': 'société introuvable',
    'PLFRY': 'société introuvable',
    'ALSEI': 'société introuvable',
    'SIIGRP': 'introuvable sur Yahoo (vérifier si toujours cotée)',
    'CNP': 'CNP Assurances retirée de la cote (2022)',
}

RENAMES = {
    "{ticker:'LVMHF',name:'Ferrari'": "{ticker:'RACE',name:'Ferrari'",
    "{ticker:'OPM',name:'Opco (Verallia)'": "{ticker:'OPM',name:'OPmobility (ex-Plastic Omnium)'",
    "{ticker:'CHSR',name:'Chargeurs'": "{ticker:'CHSR',name:'Belgrano (ex-Chargeurs)'",
}


# ═══ Elargissement aux leaders europeens eligibles PEA (05/10/2026) ═══
# Societes de l'UE/EEE (eligibles PEA). Objectif : plus de choix parmi les
# entreprises excellentes, pour trouver celles qui sont sous-evaluees.
# (ticker, symbole Yahoo, nom, secteur maison, taille, devise)
EU_LEADERS = [
    ('WKL',   'WKL.AS',    'Wolters Kluwer',      'Logiciel & information professionnelle', 'large', 'EUR'),
    ('ITX',   'ITX.MC',    'Inditex',             'Distribution habillement',              'large', 'EUR'),
    ('AMS',   'AMS.MC',    'Amadeus',             'Logiciel voyage',                       'large', 'EUR'),
    ('RAA',   'RAA.DE',    'Rational',            'Industrie equipements cuisine pro',     'mid',   'EUR'),
    ('NEM',   'NEM.DE',    'Nemetschek',          'Logiciel construction',                 'large', 'EUR'),
    ('BEI',   'BEI.DE',    'Beiersdorf',          'Cosmetique (Nivea)',                    'large', 'EUR'),
    ('SY1',   'SY1.DE',    'Symrise',             'Chimie aromes et parfums',              'large', 'EUR'),
    ('MONC',  'MONC.MI',   'Moncler',             'Luxe',                                  'large', 'EUR'),
    ('BC',    'BC.MI',     'Brunello Cucinelli',  'Luxe',                                  'mid',   'EUR'),
    ('REC',   'REC.MI',    'Recordati',           'Pharma specialites',                    'large', 'EUR'),
    ('AMP',   'AMP.MI',    'Amplifon',            'Sante materiel medical (audition)',     'mid',   'EUR'),
    ('KNEBV', 'KNEBV.HE',  'Kone',                'Industrie maintenance ascenseurs',      'large', 'EUR'),
    ('UMG',   'UMG.AS',    'Universal Music Group','Media musique',                        'large', 'EUR'),
    ('BESI',  'BESI.AS',   'BE Semiconductor',    'Semi-conducteurs equipements',          'mid',   'EUR'),
    ('ASM',   'ASM.AS',    'ASM International',   'Semi-conducteurs equipements',          'large', 'EUR'),
    ('MTX',   'MTX.DE',    'MTU Aero Engines',    'Aeronautique moteurs',                  'large', 'EUR'),
    ('RHM',   'RHM.DE',    'Rheinmetall',         'Defense',                               'large', 'EUR'),
    ('COLO',  'COLO-B.CO', 'Coloplast',           'Sante materiel medical',                'large', 'DKK'),
    ('DSV',   'DSV.CO',    'DSV',                 'Logistique transit international',      'large', 'DKK'),
    ('NSIS',  'NSIS-B.CO', 'Novonesis',           'Biotech enzymes',                       'large', 'DKK'),
    ('ATCO',  'ATCO-A.ST', 'Atlas Copco',         'Industrie compresseurs',                'large', 'SEK'),
    ('ASSA',  'ASSA-B.ST', 'Assa Abloy',          'Industrie serrures et acces',           'large', 'SEK'),
    ('EPI',   'EPI-A.ST',  'Epiroc',              'Industrie equipements miniers',         'large', 'SEK'),
    ('KOG',   'KOG.OL',    'Kongsberg Gruppen',   'Defense',                               'large', 'NOK'),
]
# Devise par symbole hors euro (le taux est lu en direct dans fetch_fundamentals ;
# NON_EUR ci-dessus sert de valeur de secours)
CURRENCY = {'NOVO-B.CO': 'DKK'}
_FX_FALLBACK = {'DKK': 7.46, 'SEK': 11.0, 'NOK': 11.6}
for _t, _sym, _n, _sec, _cap, _cur in EU_LEADERS:
    YF_MAP.setdefault(_t, _sym)
    if _cur != 'EUR':
        CURRENCY[_sym] = _cur
        NON_EUR.setdefault(_sym, _FX_FALLBACK[_cur])


def check_coverage(data_js_path='data.js'):
    """Renvoie la liste des fiches actions de data.js sans symbole Yahoo."""
    import re
    with open(data_js_path, encoding='utf-8') as f:
        tickers = re.findall(r"\{ticker:'([A-Z0-9]+)'", f.read())
    return [t for t in tickers if t not in YF_MAP and t not in ETF_TICKERS]


def purge_data_js(data_js_path='data.js'):
    """Supprime de data.js les fiches de REMOVED et applique RENAMES.
    Idempotent : ne fait rien si c'est deja fait. Les entrees du tableau
    S sont separees soit par '},' soit par une virgule en debut de ligne
    (',{ticker:...') -- les deux formats coexistent dans le fichier."""
    import re
    with open(data_js_path, encoding='utf-8') as f:
        d = f.read()
    before = d
    removed = []
    end_re = re.compile(r"\n,?\{ticker:|\n//|\n\];")
    for t in REMOVED:
        m = re.search(r"\{ticker:'" + t + "'", d)
        if not m:
            continue
        ls = d.rfind('\n', 0, m.start()) + 1
        e = end_re.search(d, m.start())
        if not e:
            continue
        d = d[:ls] + d[e.start() + 1:]
        removed.append(t)
    for a, b in RENAMES.items():
        d = d.replace(a, b)
    # Reparer les separateurs apres suppression
    d = re.sub(r"\}(\s*)\n\{ticker:", r"},\1\n{ticker:", d)
    d = re.sub(r"\},(\s*)\n,\{ticker:", r"}\1\n,{ticker:", d)
    if d != before:
        with open(data_js_path, 'w', encoding='utf-8') as f:
            f.write(d)
    return removed
