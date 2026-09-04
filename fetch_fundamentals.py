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
        dividend = info.get('dividendYield') or 0
        roe = info.get('returnOnEquity') or 0
        book_value = info.get('bookValue') or 0
        pe_ttm = info.get('trailingPE') or (price / eps_ttm if eps_ttm else 0)

        cat = classify_sector(sector)
        pe_normal = FAIR_PE.get(cat, FAIR_PE['default'])
        decote = DECOTE.get(cat, DECOTE['default'])

        eps_3y = eps_fwd * ((1 + eps_growth) ** 3) if eps_fwd and eps_fwd > 0 else 0
        dcf_pe = pe_normal * eps_3y if eps_3y > 0 else 0

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

def patch_data_js(all_results):
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    FIELDS = {'price':'price','chg':'chg','pe':'pe','pb':'pb','ev_ebitda':'ev_ebitda',
               'roe':'roe','margin':'margin','gm':'gm','debt':'debt','ic':'ic',
               'revg':'revg','epsg':'epsg','yield':'yield','beta':'beta','b52h':'b52h','b52l':'b52l',
               'dcfb':'dcfb','dcfm':'dcfm','dcfu':'dcfu',
               'el':'el','eh':'eh','stop':'stop','o1':'o1','o2':'o2'}
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
    calendar = build_earnings_calendar(all_results)
    log = {'generated': datetime.now(PARIS).isoformat(), 'updated_count': updated,
           'earnings': calendar, 'data': {k: {f:v for f,v in d.items() if f!='error'} for k,d in all_results.items()}}
    with open('fundamentals_log.json', 'w', encoding='utf-8') as f:
        json.dump(log, f, ensure_ascii=False, indent=2, default=str)
    print(f"\nfundamentals_log.json sauvegarde")

if __name__ == '__main__':
    main()

