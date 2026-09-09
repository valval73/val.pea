#!/usr/bin/env python3
"""
VAL.PEA -- Mise a jour automatique des donnees fondamentales
Declenche par GitHub Actions 2x/jour (7h + 17h35 Paris)
Met a jour : PE, PB, ROE, dividende, bilan, prochains resultats,
ainsi que le DCF (dcfb/dcfm/dcfu) et les zones d'achat (el/eh/stop/o1/o2).

Le DCF etait fige depuis la creation de chaque fiche (jamais recalcule --
audit du 26/08/2026). Il est maintenant recalcule a chaque run, avec une
vraie classification sectorielle (18 categories couvrant les 193 secteurs
reels du screener, contre 4/193 avant).
"""
import yfinance as yf
import re, json, sys, math, unicodedata
from datetime import datetime
import pytz

PARIS = pytz.timezone('Europe/Paris')

YF_MAP = {
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','CAP':'CAP.PA','DSY':'DSY.PA',
    'LR':'LR.PA','PUB':'PUB.PA','RI':'RI.PA','SGO':'SGO.PA','VIE':'VIE.PA',
    'ORA':'ORA.PA','EL':'EL.PA','KER':'KER.PA','STM':'STM.PA','ENX':'ENX.PA',
    'ENGI':'ENGI.PA','DG':'DG.PA','HO':'HO.PA','BN':'BN.PA','CA':'CA.PA',
    'WLN':'WLN.PA','RNO':'RNO.PA','TEP':'TEP.PA','FTI':'FTI.PA','ALO':'ALO.PA',
    'EDEN':'EDEN.PA','SAM':'SAM.PA','GTT':'GTT.PA','SEB':'SK.PA','VK':'VK.PA',
    'MT':'MT.AS','STLA':'STLA.MI','SAP':'SAP.DE','ASML':'ASML.AS',
    'SIE':'SIE.DE','BAYN':'BAYN.DE','BMW':'BMW.DE','ALV':'ALV.DE',
    'ENEL':'ENEL.MI','ENI':'ENI.MI','UCG':'UCG.MI','RACE':'RACE.MI',
    'CABK':'CABK.MC','BBVA':'BBVA.MC','IBE':'IBE.MC','ITX':'ITX.MC',
    'TEF':'TEF.MC','NN':'NN.AS','INGA':'INGA.AS','AD':'AD.AS',
    # Elargissement de couverture (fusion avec le mapping cote client)
    'URW':'URW.AS','ELIS':'ELIS.PA','ERF':'ERF.PA','COFA':'COFA.PA',
    'SPIE':'SPIE.PA','FNAC':'FNAC.PA','LNA':'LNA.PA','SOP':'SOP.PA',
    'NEXANS':'NEX.PA','SW':'SW.PA','MERY':'MERY.PA','IPSEN':'IPN.PA',
    'REXEL':'RXL.PA','ALTEN':'ATE.PA','IMERYS':'NK.PA','FORVIA':'FRVIA.PA',
    'EIFFAGE':'FGR.PA','TRIGANO':'TRI.PA','DASSAV':'AM.PA','PRX':'PRX.AS',
    'ADYEN':'ADYEN.AS','NOVO':'NOVO-B.CO','COVIVIO':'COV.PA','STEF':'STF.PA',
    'ARGAN':'ARG.PA','INTERPARFUMS':'ITP.PA','LECTRA':'LSS.PA','LISI':'FII.PA',
    'VIRBAC':'VIRP.PA','ABIVAX':'ABVX.PA','BOIRON':'BOI.PA','THERMADOR':'THEP.PA',
    'WAGA':'WAGA.PA','LACROIX':'LACR.PA','MANITOU':'MTU.PA','FIGEAC':'FGA.PA',
    'SAMSE':'SAMS.PA','ALTAREA':'ALTA.PA','NRO':'NRO.PA',
    'DBG':'DBG.PA','RUI':'RUI.PA','JXS':'JCQ.PA','CNP':'CNP.PA','ABCA':'ABCA.PA','ATO':'ATO.PA',
    'SYENSQO':'SYENSQO.BR','ICAD':'ICAD.PA','NXI':'NXI.PA','GFC':'GFC.PA',
    'EMEIS':'EMEIS.PA','ELIOR':'ELIOR.PA','ALSTOM':'ALO.PA',
    # 34 valeurs SRD Classique ajoutees (audit Investir 24/07/2026)
    'ADP':'ADP.PA','AKE':'AKE.PA','LTA':'LTA.PA','BB':'BB.PA','ATE':'ATE.PA','ANTIN':'ANTIN.PA','ELEC':'ELEC.PA','ERA':'ERA.PA','RF':'RF.PA','ETL':'ETL.PA','EXA':'EXA.PA','EXENS':'EXENS.PA','FDJU':'FDJU.PA','GFC':'GFC.PA','GET':'GET.PA','DEC':'DEC.PA','MMB':'MMB.PA','LOUP':'LOUP.PA','MMT':'MMT.PA','NRO':'NRO.PA','OVH':'OVH.PA','PLNW':'PLNW.PA','GDS':'GDS.PA','RBT':'RBT.PA','RUI':'RUI.PA','DIM':'DIM.PA','SCR':'SCR.PA','SESG':'SESG.PA','TE':'TE.PA','TFI':'TFI.PA','TKO':'TKO.PA','VCT':'VCT.PA','VIL':'VIL.PA','WAVE':'WAVE.PA',
}

# ─── Classification sectorielle (mots-cles, couvre 193/193 secteurs reels
#      du screener -- audit du 26/08/2026 avait trouve 4/193 seulement) ───
def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

SECTOR_RULES = [
    ('luxe', 'Luxe'), ('maroquinerie', 'Luxe'), ('parfum', 'Luxe'),
    ('champagne', 'Luxe'), ('cosmetique', 'Luxe'), ('bijou', 'Luxe'),
    ('spiritueux', 'Luxe'), ('vins bordeaux', 'Luxe'), ('licences parfums', 'Luxe'),
    ('semi-conducteur', 'Semiconducteurs'), ('connecteurs rf', 'Semiconducteurs'),
    ('instruments mesure', 'Semiconducteurs'), ('instruments scientifiques', 'Semiconducteurs'),
    ('electronique embarquee', 'Semiconducteurs'), ('optique', 'Semiconducteurs'),
    ('saas', 'Logiciel'), ('erp cloud', 'Logiciel'), ('logiciel', 'Logiciel'),
    ('cybersecurite', 'Logiciel'), ('industrie digitale', 'Logiciel'),
    ('esn ', 'Logiciel'), ('services it', 'Logiciel'), ('services informatiques', 'Logiciel'),
    ('recrutement tech', 'Logiciel'), ('tech investissement', 'Logiciel'),
    ('visioconference', 'Logiciel'), ('diagnostic medical ia', 'Logiciel'),
    ('iot industriel', 'Logiciel'),
    ('biotech', 'Biotech'), ('pharma', 'Biotech'), ('homeopathie', 'Biotech'),
    ('radioenhancement', 'Biotech'), ('chimie pharmaceutique', 'Biotech'),
    ('laboratoires analyses', 'Biotech'), ('diagnostics medicaux', 'Biotech'),
    ('sante materiel medical', 'Biotech'), ('sante services', 'Biotech'),
    ('aviation', 'Defense'), ('aeronautique', 'Defense'), ('defense', 'Defense'),
    ('drones', 'Defense'), ('pyrotechnie', 'Defense'), ('simulation combat', 'Defense'),
    ('fixations aeronautiques', 'Defense'), ('usinage aeronautique', 'Defense'),
    ('ingenierie thermique spatial', 'Defense'), ('infrastructure aeroports', 'Defense'),
    ('transport aerien', 'Defense'),
    ('energie', 'Energie'), ('electrique', 'Energie'), ('electricite', 'Energie'), ('eolien', 'Energie'),
    ('solaire', 'Energie'), ('biogaz', 'Energie'), ('biomethane', 'Energie'),
    ('bienergie', 'Energie'), ('uranium', 'Energie'), ('gaz industriels', 'Energie'),
    ('lng technology', 'Energie'), ('membranes methaniers', 'Energie'),
    ('data energie', 'Energie'), ('data souterrain', 'Energie'), ('option achat gtt', 'Energie'),
    ('assurance', 'Financier'), ('banque', 'Financier'), ('paiements', 'Financier'),
    ('arbitrage', 'Financier'), ('holding', 'Financier'), ('avantages salariaux', 'Financier'),
    ('immobilier', 'Immobilier'), ('centres commerciaux', 'Immobilier'),
    ('entrepots logistiques', 'Immobilier'), ('retail parks', 'Immobilier'),
    ('promotion immobiliere', 'Immobilier'), ('tourisme residences', 'Immobilier'),
    ('ehpad', 'Immobilier'),
    ('dechets', 'Environnement'), ('recyclage', 'Environnement'),
    ('environnementaux', 'Environnement'), ('eau traitement', 'Environnement'),
    ('distribution eau', 'Environnement'), ('mesure pollution', 'Environnement'),
    ('eau & dechets', 'Environnement'),
    ('ferroviaire', 'Transport'), ('wagons fret', 'Transport'), ('logistique', 'Transport'),
    ('transit international', 'Transport'), ('ports logistique', 'Transport'),
    ('transport frigorifique', 'Transport'), ('commission fret', 'Transport'),
    ('bateaux', 'Transport'), ('catamarans', 'Transport'), ('propulsion velique', 'Transport'),
    ('camping-car', 'Transport'), ('vehicules loisirs', 'Transport'),
    ('telecom', 'Telecoms'), ('media', 'Telecoms'), ('communication', 'Telecoms'),
    ('publicite', 'Telecoms'), ('evenementiel', 'Telecoms'),
    ('distribution', 'Distribution'), ('ecommerce', 'Distribution'),
    ('agroalimentaire', 'Conso'), ('agriculture tropicale', 'Conso'),
    ('gastronomie', 'Conso'), ('brasseries', 'Conso'), ('restauration collective', 'Conso'),
    ('emballage', 'Conso'), ('electromenager', 'Conso'),
    ('bpo', 'Services'), ('services techniques', 'Services'), ('services collectifs', 'Services'),
    ('services location-entretien', 'Services'), ('tests & analyses', 'Services'),
    ('etudes de marche', 'Services'), ('construction & concessions', 'Services'),
    ('automobile', 'Automobile'), ('equipementier auto', 'Automobile'),
    ('plasturgie auto', 'Automobile'),
    ('hotellerie', 'Hotellerie'),
    ('industrie', 'Industrie'), ('engins manutention', 'Industrie'), ('fours industriels', 'Industrie'),
    ('isolation phonique', 'Industrie'), ('menuiserie', 'Industrie'), ('materiaux', 'Industrie'),
    ('plasturgie', 'Industrie'), ('pneumatiques', 'Industrie'), ('tubes acier', 'Industrie'),
    ('acier', 'Industrie'), ('tuyaux flexibles', 'Industrie'), ('films protection', 'Industrie'),
    ('cables', 'Industrie'), ('piscines acier', 'Industrie'), ('maintenance ascenseurs', 'Industrie'),
    ('materiel brasserie', 'Industrie'), ('chimie', 'Industrie'), ('conglomerat', 'Industrie'),
]
FAIR_PE = {
    'Luxe': 28, 'Semiconducteurs': 32, 'Logiciel': 26, 'Biotech': 24, 'Defense': 20,
    'Energie': 14, 'Financier': 12, 'Immobilier': 16, 'Environnement': 17, 'Transport': 15,
    'Telecoms': 14, 'Distribution': 16, 'Conso': 18, 'Services': 16, 'Automobile': 12,
    'Hotellerie': 18, 'Industrie': 18, 'default': 18,
}
DECOTE = {
    'Luxe': 0.22, 'Semiconducteurs': 0.28, 'Logiciel': 0.24, 'Biotech': 0.30, 'Defense': 0.16,
    'Energie': 0.20, 'Financier': 0.20, 'Immobilier': 0.20, 'Environnement': 0.17, 'Transport': 0.18,
    'Telecoms': 0.16, 'Distribution': 0.17, 'Conso': 0.16, 'Services': 0.16, 'Automobile': 0.20,
    'Hotellerie': 0.18, 'Industrie': 0.17, 'default': 0.18,
}

def classify_sector(sector):
    s = strip_accents(sector or '').lower().strip()
    if s == 'it':
        return 'Logiciel'
    for kw, cat in SECTOR_RULES:
        if kw in s:
            return cat
    return 'default'

def load_sectors_from_data_js():
    """Lit le secteur de chaque ticker directement depuis data.js (source
    de verite : la taxonomie maison, pas celle -- differente -- de Yahoo)."""
    sectors = {}
    try:
        with open('data.js', 'r', encoding='utf-8') as f:
            content = f.read()
        for m in re.finditer(r"ticker:'([A-Z0-9]+)'.*?sector:'([^']*)'", content):
            sectors[m.group(1)] = m.group(2)
    except Exception as e:
        print(f"  WARN lecture secteurs: {e}")
    return sectors

def compute_dcf_and_zones(ticker, sector, price, info):
    """Recalcule le DCF (3 methodes consolidees) et les zones d'achat.
    Repris de zones_dynamiques.py (jamais branche en prod -- audit du
    26/08/2026), avec la classification sectorielle complete ci-dessus."""
    try:
        eps_ttm = info.get('trailingEps') or 0
        eps_fwd = info.get('forwardEps') or (eps_ttm * 1.08 if eps_ttm else 0)
        eps_growth = info.get('earningsGrowth') or info.get('revenueGrowth') or 0.05
        # earningsGrowth de yfinance est un YoY brut, parfois extreme (ex-effet
        # de base sur creux/rebond) -- sans plafond, un exposant sur 3 ans
        # (1+g)^3 peut exploser et inverser dcfb/dcfu (ex: LVMH dcfb>dcfu
        # constate en prod). Plafonne a une croissance soutenable long terme.
        eps_growth_proj = max(min(eps_growth, 0.25), -0.15)
        dividend = info.get('dividendYield') or 0
        roe = info.get('returnOnEquity') or 0
        book_value = info.get('bookValue') or 0
        pe_ttm = info.get('trailingPE') or (price / eps_ttm if eps_ttm else 0)

        cat = classify_sector(sector)
        pe_normal = FAIR_PE.get(cat, FAIR_PE['default'])
        decote = DECOTE.get(cat, DECOTE['default'])

        # Fair PE x BPA prevu N+1 -- valeur d'aujourd'hui, pas une projection
        # a 3 ans traitee a tort comme un prix actuel (cause reelle des DCF a
        # 3-5x le cours meme avec la croissance plafonnee -- audit du
        # 07/09/2026). Le PE sectoriel "normal" est deja une hypothese
        # generuse ; l'appliquer a un profit a 3 ans double l'optimisme.
        dcf_pe = pe_normal * eps_fwd if eps_fwd and eps_fwd > 0 else 0

        dcf_gordon = 0
        if dividend and dividend > 0.01 and price > 0:
            div_amount = price * dividend
            ke = 0.08
            g = min(eps_growth, 0.07)
            if ke > g:
                dcf_gordon = div_amount * (1 + g) / (ke - g)

        dcf_pb = 0
        if roe and roe > 0.15 and book_value and book_value > 0:
            ke = 0.09
            dcf_pb = book_value * (roe / ke)

        # Garde-fou final : quelle que soit la cause (action decotee pour
        # raison specifique -- ex Air France, Atos, Worldline -- pas un
        # simple retard sectoriel), aucune methode individuelle ne doit
        # pousser le "juste prix" au-dela d'un multiple raisonnable du
        # cours actuel. Un DCF a 4-6x le cours n'est pas un signal
        # d'opportunite fiable, c'est un artefact de calcul -- audit du
        # 07/09/2026 (48/891 combinaisons testees hors [0.25x-2.5x]
        # avant ce garde-fou).
        def _clamp(v, lo=0.4, hi=2.2):
            if not v or v <= 0 or price <= 0: return v
            return max(min(v, price * hi), price * lo)
        dcf_pe = _clamp(dcf_pe)
        dcf_gordon = _clamp(dcf_gordon)
        dcf_pb = _clamp(dcf_pb)

        dcfs = [d for d in [dcf_pe, dcf_gordon, dcf_pb] if d > price * 0.3]
        if not dcfs:
            if pe_ttm and pe_ttm > 0:
                dcfs = [price * (pe_normal / pe_ttm)]
            else:
                return None

        dcfm = round(sum(dcfs) / len(dcfs), 2)
        dcfb = round(dcfm * 0.85, 2)
        dcfu = round(dcfm * 1.20, 2)

        el = round(dcfm * (1 - decote), 2)
        eh = round(dcfm * (1 - decote * 0.4), 2)
        stop = round(el * 0.88, 2)
        o1 = round(dcfm * 1.05, 2)
        o2 = round(dcfm * 1.20, 2)

        if not (el < eh and o1 > el):
            return None

        return {'dcfb': dcfb, 'dcfm': dcfm, 'dcfu': dcfu,
                'el': el, 'eh': eh, 'stop': stop, 'o1': o1, 'o2': o2,
                'sector_cat': cat}
    except Exception as e:
        print(f"  DCF SKIP {ticker}: {e}")
        return None

def compute_rsi(closes, period=14):
    """RSI (methode de Wilder), sans dependance pandas. closes = liste de
    cours de cloture du plus ancien au plus recent. Rend None si pas
    assez d'historique -- mieux vaut ne rien afficher qu'afficher un
    chiffre invente. Filtre les trous de cotation (NaN) en amont --
    trouve en verifiant ce meme risque apres l'incident Altman du
    08/09/2026 : un historique Yahoo troue peut sinon produire un NaN
    qui casse tout data.js."""
    closes = [c for c in closes if c is not None and not math.isnan(c)]
    if len(closes) < period + 1:
        return None
    deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    gains = [d if d > 0 else 0.0 for d in deltas]
    losses = [-d if d < 0 else 0.0 for d in deltas]
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    if avg_loss == 0:
        return 100.0 if avg_gain > 0 else 50.0
    rs = avg_gain / avg_loss
    val = round(100 - (100 / (1 + rs)), 1)
    return None if math.isnan(val) else val

def compute_ma(closes, window):
    closes = [c for c in closes if c is not None and not math.isnan(c)]
    if len(closes) < window:
        return None
    val = round(sum(closes[-window:]) / window, 2)
    return None if math.isnan(val) else val

def _get_row(df, *names):
    """Cherche une ligne de bilan/resultat en essayant plusieurs libelles
    possibles -- yfinance a change ses noms de champs selon les versions,
    et je n'ai pas d'acces reseau pour verifier en direct lesquels sont
    actifs. Renvoie la valeur la plus recente (1ere colonne) ou None.
    Traite NaN comme absent -- pandas utilise NaN (pas None) pour une
    case vide, et 'val is not None' laissait passer NaN, qui s'ecrivait
    ensuite tel quel dans data.js (litteral 'nan', invalide en JS) et
    cassait le chargement de tout le site -- incident du 08/09/2026."""
    if df is None or df.empty:
        return None
    for name in names:
        if name in df.index:
            try:
                val = df.loc[name].iloc[0]
                if val is None:
                    continue
                fval = float(val)
                if math.isnan(fval) or math.isinf(fval):
                    continue
                return fval
            except Exception:
                continue
    return None

def _get_row_prev(df, *names):
    """Meme chose mais pour l'annee precedente (2e colonne). Meme
    traitement NaN que _get_row (cf note ci-dessus)."""
    if df is None or df.empty or df.shape[1] < 2:
        return None
    for name in names:
        if name in df.index:
            try:
                val = df.loc[name].iloc[1]
                if val is None:
                    continue
                fval = float(val)
                if math.isnan(fval) or math.isinf(fval):
                    continue
                return fval
            except Exception:
                continue
    return None

def compute_piotroski(t, info):
    """F-Score de Piotroski (0-9). Echoue proprement (None) si le bilan
    n'a pas assez d'historique -- mieux vaut ne rien afficher qu'un faux
    chiffre. A verifier sur le premier run reel (cf note plus haut)."""
    try:
        bs = t.balance_sheet
        inc = t.financials
        cf = t.cashflow
        if bs is None or bs.empty or inc is None or inc.empty:
            return None

        total_assets = _get_row(bs, 'Total Assets')
        total_assets_prev = _get_row_prev(bs, 'Total Assets')
        net_income = _get_row(inc, 'Net Income', 'Net Income Common Stockholders')
        ocf = _get_row(cf, 'Operating Cash Flow', 'Total Cash From Operating Activities', 'Cash Flow From Continuing Operating Activities')
        ltd = _get_row(bs, 'Long Term Debt', 'Long Term Debt And Capital Lease Obligation')
        ltd_prev = _get_row_prev(bs, 'Long Term Debt', 'Long Term Debt And Capital Lease Obligation')
        cur_assets = _get_row(bs, 'Total Current Assets', 'Current Assets')
        cur_liab = _get_row(bs, 'Total Current Liabilities', 'Current Liabilities')
        cur_assets_prev = _get_row_prev(bs, 'Total Current Assets', 'Current Assets')
        cur_liab_prev = _get_row_prev(bs, 'Total Current Liabilities', 'Current Liabilities')
        shares = _get_row(bs, 'Share Issued', 'Ordinary Shares Number')
        shares_prev = _get_row_prev(bs, 'Share Issued', 'Ordinary Shares Number')
        gross_profit = _get_row(inc, 'Gross Profit')
        gross_profit_prev = _get_row_prev(inc, 'Gross Profit')
        revenue = _get_row(inc, 'Total Revenue')
        revenue_prev = _get_row_prev(inc, 'Total Revenue')
        net_income_prev = _get_row_prev(inc, 'Net Income', 'Net Income Common Stockholders')

        if total_assets is None or net_income is None or total_assets_prev is None:
            return None

        roa = net_income / total_assets if total_assets else None
        roa_prev = (net_income_prev / total_assets_prev) if (net_income_prev is not None and total_assets_prev) else None

        score = 0
        # Rentabilite (4 points)
        if roa is not None and roa > 0: score += 1
        if ocf is not None and ocf > 0: score += 1
        if roa is not None and roa_prev is not None and roa > roa_prev: score += 1
        if ocf is not None and net_income is not None and ocf > net_income: score += 1
        # Levier / liquidite (3 points)
        if ltd is not None and ltd_prev is not None and ltd <= ltd_prev: score += 1
        if cur_assets and cur_liab and cur_assets_prev and cur_liab_prev:
            if (cur_assets/cur_liab) > (cur_assets_prev/cur_liab_prev): score += 1
        if shares is not None and shares_prev is not None and shares <= shares_prev * 1.01: score += 1
        # Efficacite operationnelle (2 points)
        if gross_profit and revenue and gross_profit_prev and revenue_prev:
            if (gross_profit/revenue) > (gross_profit_prev/revenue_prev): score += 1
        if revenue and revenue_prev and total_assets_prev:
            if (revenue/total_assets) > (revenue_prev/total_assets_prev): score += 1
        return score
    except Exception as e:
        print(f"  Piotroski SKIP: {e}")
        return None

def compute_altman_z(t, info, price, shares_out):
    """Z-Score d'Altman. Meme reserve que Piotroski sur les noms de
    champs yfinance. Formule standard (entreprises industrielles cotees)."""
    try:
        bs = t.balance_sheet
        inc = t.financials
        if bs is None or bs.empty or inc is None or inc.empty:
            return None

        total_assets = _get_row(bs, 'Total Assets')
        cur_assets = _get_row(bs, 'Total Current Assets', 'Current Assets')
        cur_liab = _get_row(bs, 'Total Current Liabilities', 'Current Liabilities')
        total_liab = _get_row(bs, 'Total Liab', 'Total Liabilities Net Minority Interest')
        retained_earnings = _get_row(bs, 'Retained Earnings')
        ebit = _get_row(inc, 'EBIT', 'Operating Income')
        revenue = _get_row(inc, 'Total Revenue')

        if not total_assets or not total_liab:
            return None

        working_capital = (cur_assets - cur_liab) if (cur_assets is not None and cur_liab is not None) else 0
        market_cap = (price * shares_out) if (price and shares_out) else info.get('marketCap')

        A = working_capital / total_assets
        B = (retained_earnings or 0) / total_assets
        C = (ebit or 0) / total_assets
        D = (market_cap / total_liab) if (market_cap and total_liab) else 0
        E = (revenue or 0) / total_assets

        z = 1.2*A + 1.4*B + 3.3*C + 0.6*D + 1.0*E
        if math.isnan(z) or math.isinf(z):
            return None
        return round(z, 2)
    except Exception as e:
        print(f"  Altman SKIP: {e}")
        return None

def safe(v, d=0, dec=2):
    try:
        f = float(v)
        if math.isnan(f) or math.isinf(f): return d
        return round(f, dec)
    except: return d

def pct(v, d=0): return safe(v * 100 if v else 0, d, 1)

def fetch_one(ticker, yf_sym, sector):
    result = {'ticker': ticker, 'updated': datetime.now(PARIS).isoformat()}
    try:
        t = yf.Ticker(yf_sym)
        info = t.info
        result['price']   = safe(info.get('currentPrice') or info.get('regularMarketPrice'))
        if result['price'] <= 0:
            # Repli : .info peut revenir vide pour un ticker donne sans
            # lever d'erreur (cas reel observe sur EL.PA -- audit du
            # 04/09/2026). history() est un endpoint different, plus
            # fiable pour un simple cours de cloture.
            try:
                h = t.history(period='2d')
                if not h.empty:
                    result['price'] = safe(h['Close'].iloc[-1])
            except Exception:
                pass
        result['chg']     = pct(info.get('regularMarketChangePercent', 0))
        result['pe']      = safe(info.get('trailingPE') or info.get('forwardPE'))
        result['pe_fwd']  = safe(info.get('forwardPE'))
        result['pb']      = safe(info.get('priceToBook'))
        result['ps']      = safe(info.get('priceToSalesTrailing12Months'))
        result['ev_ebitda']= safe(info.get('enterpriseToEbitda'))
        result['roe']     = pct(info.get('returnOnEquity', 0))
        result['roic']    = pct(info.get('returnOnEquity', 0))
        result['margin']  = pct(info.get('profitMargins', 0))
        result['gm']      = pct(info.get('grossMargins', 0))
        result['debt']    = safe(info.get('debtToEquity', 0) / 100)
        result['ic']      = safe(info.get('currentRatio'))
        result['revg']    = pct(info.get('revenueGrowth', 0))
        result['epsg']    = pct(info.get('earningsGrowth', 0))
        result['yield']   = pct(info.get('dividendYield', 0))
        result['payout']  = pct(info.get('payoutRatio', 0))
        result['beta']    = safe(info.get('beta'))
        result['b52h']    = safe(info.get('fiftyTwoWeekHigh'))
        result['b52l']    = safe(info.get('fiftyTwoWeekLow'))
        result['nb_analysts'] = int(safe(info.get('numberOfAnalystOpinions', 0), 0, 0))
        result['target_price'] = safe(info.get('targetMeanPrice'))
        result['recommendation'] = info.get('recommendationKey', '')
        # DCF + zones d'achat (recalcule desormais a chaque run -- avant
        # ces valeurs etaient figees depuis la creation de la fiche)
        if result['price'] > 0:
            dcf = compute_dcf_and_zones(ticker, sector, result['price'], info)
            if dcf:
                result.update({k: v for k, v in dcf.items() if k != 'sector_cat'})
                print(f"  OK {ticker} [{dcf['sector_cat']}]: PE={result['pe']} ROE={result['roe']}% "
                      f"DCF={dcf['dcfm']}€ Zone={dcf['el']}-{dcf['eh']}€")
            else:
                print(f"  OK {ticker}: PE={result['pe']} ROE={result['roe']}% (DCF non calculable)")
        # RSI + moyennes mobiles (recalcules a chaque run -- avant geles
        # depuis la creation de chaque fiche, cf audit du 08/09/2026)
        try:
            hist = t.history(period='1y')
            if not hist.empty and len(hist) > 15:
                closes = hist['Close'].tolist()
                rsi = compute_rsi(closes)
                mm50 = compute_ma(closes, 50)
                mm200 = compute_ma(closes, 200)
                if rsi is not None: result['rsi'] = rsi
                if mm50 is not None: result['mm50'] = mm50
                if mm200 is not None: result['mm200'] = mm200
        except Exception as e:
            print(f"  RSI/MM SKIP {ticker}: {e}")
        # Piotroski + Altman Z (a verifier sur le premier run reel --
        # voir reserve dans compute_piotroski/compute_altman_z)
        pio = compute_piotroski(t, info)
        shares_out = info.get('sharesOutstanding')
        alt = compute_altman_z(t, info, result['price'], shares_out)
        if pio is not None: result['pio'] = pio
        if alt is not None: result['alt'] = alt
        # Prochaine publication resultats
        try:
            cal = t.calendar
            if cal is not None and not cal.empty:
                row = cal.iloc[0] if len(cal) > 0 else None
                if row is not None:
                    ed = row.get('Earnings Date') if hasattr(row, 'get') else None
                    if ed: result['next_earnings'] = str(ed)
        except: pass
    except Exception as e:
        print(f"  SKIP {ticker}: {e}")
        result['error'] = str(e)
    return result

def bam_score(price, dcfm, pio, alt, roe, epsg):
    """Score aligne methode BAM (Buffett-Ackman-Munger) : la marge de
    securite DCF et la solidite financiere pesent plus que le momentum
    ou la taille. Bareme continu (pas de paliers fixes) pour eviter les
    gros paquets d'ex-aequo qui gonflaient artificiellement le nombre
    de A -- corrige suite a une question directe du 09/09/2026."""
    score = 0
    if price > 0 and dcfm > 0:
        upside = (dcfm/price - 1) * 100
        score += min(35, max(0, upside * 0.7))
    score += (max(0, min(9, pio)) / 9) * 25
    score += min(15, max(0, alt * 4))
    score += min(15, max(0, roe * 0.7))
    score += min(10, max(0, epsg * 1.0))
    return round(min(100, score))

def compute_all_scores():
    """Relit data.js apres la mise a jour des fondamentaux et recalcule
    le score A/B/C/D de chaque action -- seuils calcules par categorie
    (large/mid/small), pas sur l'univers entier mele, pour comparer
    chaque valeur a ses pairs de taille comparable (cf audit du
    09/09/2026 : comparer Safran a des small caps n'a pas de sens).
    Extraction par blocs simples (meme methode que patch_data_js,
    deja eprouvee) plutot que par regex complexe -- suite a un echec
    silencieux en environnement reel non reproduit localement, on
    reduit le risque en reutilisant ce qui marche deja ailleurs."""
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    entries = []
    tickers_found = list(re.finditer(r"\{ticker:'([A-Z0-9]+)'", content))
    for i, m in enumerate(tickers_found):
        tk = m.group(1)
        start = m.start()
        end = tickers_found[i+1].start() if i+1 < len(tickers_found) else len(content)
        block = content[start:end]
        def g(field, d=0):
            mm = re.search(field + r":([\d.-]+)", block)
            return float(mm.group(1)) if mm else d
        cap_m = re.search(r"cap:'(\w+)'", block)
        cap = cap_m.group(1) if cap_m else 'mid'
        price = g('price')
        if price <= 0: continue
        cs = bam_score(price, g('dcfm'), g('pio'), g('alt'), g('roe'), g('epsg'))
        entries.append({'ticker': tk, 'cap': cap, 'score': cs})

    by_cap = {}
    for e in entries:
        by_cap.setdefault(e['cap'], []).append(e['score'])
    thresholds = {}
    for cap, vals in by_cap.items():
        vs = sorted(vals, reverse=True)
        n = len(vs)
        if n < 5:
            thresholds[cap] = (75, 60, 45)
            continue
        thresholds[cap] = (vs[max(0,int(n*0.10)-1)], vs[max(0,int(n*0.45)-1)], vs[max(0,int(n*0.80)-1)])

    grades = {}
    for e in entries:
        a, b, cc = thresholds.get(e['cap'], (75, 60, 45))
        if e['score'] >= a: g = 'A'
        elif e['score'] >= b: g = 'B'
        elif e['score'] >= cc: g = 'C'
        else: g = 'D'
        grades[e['ticker']] = g
    return grades

def patch_scores(grades):
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    for ticker, grade in grades.items():
        tp = content.find(f"ticker:'{ticker}'")
        if tp == -1: continue
        np_ = content.find("ticker:'", tp + 1)
        block_end = np_ if np_ > -1 else len(content)
        block = content[tp:block_end]
        nb = re.sub(r"score:'[ABCD]'", f"score:'{grade}'", block, count=1)
        if nb != block:
            block = nb; updated += 1
        content = content[:tp] + block + content[block_end:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Scores A/B/C/D recalcules : {updated} valeurs mises a jour")
    return updated

def patch_data_js(all_results):
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    FIELDS = {'price':'price','chg':'chg','pe':'pe','pb':'pb','ev_ebitda':'ev_ebitda',
               'roe':'roe','margin':'margin','gm':'gm','debt':'debt','ic':'ic',
               'revg':'revg','epsg':'epsg','yield':'yield','beta':'beta','b52h':'b52h','b52l':'b52l',
               'dcfb':'dcfb','dcfm':'dcfm','dcfu':'dcfu',
               'el':'el','eh':'eh','stop':'stop','o1':'o1','o2':'o2',
               'rsi':'rsi','mm50':'mm50','mm200':'mm200','pio':'pio','alt':'alt'}
    for ticker, data in all_results.items():
        if 'error' in data and 'price' not in data: continue
        tp = content.find(f"ticker:'{ticker}'")
        if tp == -1: continue
        np = content.find("ticker:'", tp + 1)
        block_end = np if np > -1 else len(content)
        block = content[tp:block_end]
        for dk, jk in FIELDS.items():
            val = data.get(dk)
            if val is None or val == 0: continue
            # Garde-fou universel : un NaN/Infinity ecrit tel quel (litteral
            # 'nan'/'inf') casse la syntaxe JS de tout data.js et rend le
            # site entier vide -- incident reel du 08/09/2026 (bug Altman
            # Z, mais cette protection couvre n'importe quel champ futur).
            if isinstance(val, float) and (math.isnan(val) or math.isinf(val)):
                print(f"  IGNORE {ticker}.{dk}: valeur invalide ({val})")
                continue
            nb = re.sub(jk + r':[+-]?\d+\.?\d*', jk + ':' + str(val), block, count=1)
            if nb != block: block = nb; updated += 1
        content = content[:tp] + block + content[block_end:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nMaj data.js: {updated} champs")
    return updated

def build_earnings_calendar(all_results):
    cal = []
    today = datetime.now(PARIS).date()
    for ticker, data in all_results.items():
        if 'next_earnings' not in data: continue
        try:
            from datetime import date
            d = datetime.fromisoformat(str(data['next_earnings']).split(' ')[0]).date()
            cal.append({'ticker':ticker,'date':str(d),'days_away':(d-today).days,
                        'type':'Resultats','confirmed':True,
                        'target_price':data.get('target_price'),
                        'recommendation':data.get('recommendation',''),
                        'nb_analysts':data.get('nb_analysts',0),
                        'revg':data.get('revg')})
        except: pass
    cal.sort(key=lambda x: x['days_away'])
    print(f"\nEarnings calendar: {len(cal)} dates")
    for e in cal[:10]:
        if e['days_away'] >= 0:
            print(f"  {'🔴' if e['days_away']<=7 else '🟠' if e['days_away']<=30 else '🟡'} {e['ticker']:6s}: {e['date']} (J+{e['days_away']})")
    return cal

def main():
    print(f"VAL.PEA Fundamentals -- {datetime.now(PARIS).strftime('%Y-%m-%d %H:%M')} Paris")
    print('='*50)
    sectors = load_sectors_from_data_js()
    print(f"Secteurs charges pour {len(sectors)} tickers")
    all_results = {}
    items = list(YF_MAP.items())
    import time
    for i in range(0, len(items), 5):
        for ticker, sym in items[i:i+5]:
            all_results[ticker] = fetch_one(ticker, sym, sectors.get(ticker, ''))
        time.sleep(2)
    updated = patch_data_js(all_results)
    if updated: bump_index_html_version()
    try:
        grades = compute_all_scores()
        patch_scores(grades)
    except Exception as e:
        import traceback
        print(f"❌ ECHEC recalcul des scores A/B/C/D : {e}")
        traceback.print_exc()
        print("(les scores existants restent inchanges pour ce run -- prix et fondamentaux, eux, sont bien a jour)")
    calendar = build_earnings_calendar(all_results)
    log = {'generated': datetime.now(PARIS).isoformat(), 'updated_count': updated,
           'earnings': calendar, 'data': {k: {f:v for f,v in d.items() if f!='error'} for k,d in all_results.items()}}
    with open('fundamentals_log.json', 'w', encoding='utf-8') as f:
        json.dump(log, f, ensure_ascii=False, indent=2, default=str)
    print(f"\nfundamentals_log.json sauvegarde")

if __name__ == '__main__':
    main()

def bump_index_html_version():
    """Casse le cache CDN de GitHub Pages en changeant l'URL de data.js a
    chaque ecriture reussie -- data.js etait fige depuis des semaines cote
    site public car son URL ne changeait jamais (audit du 08/09/2026)."""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(
            r'data\.js\?v=\d+',
            f'data.js?v={int(datetime.now(PARIS).timestamp())}',
            content, count=1
        )
        if new_content != content:
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("index.html : version data.js mise a jour (cache casse)")
    except Exception as e:
        print(f"  WARN bump version: {e}")
