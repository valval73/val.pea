#!/usr/bin/env python3
"""
VAL.PEA -- Mise a jour automatique des donnees fondamentales
Declenche par GitHub Actions toutes les 4h + dimanche 20h UTC
Met a jour : PE, PB, ROE, dividende, bilan, prochains resultats
"""
import yfinance as yf
import re, json, sys, math
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
    'TEF':'TEF.MC','NN':'NN.AS','INGA':'INGA.AS','AD':'AD.AS'
}

def safe(v, d=0, dec=2):
    try:
        f = float(v)
        if math.isnan(f) or math.isinf(f): return d
        return round(f, dec)
    except: return d

def pct(v, d=0): return safe(v * 100 if v else 0, d, 1)

def fetch_one(ticker, yf_sym):
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
        # Prochaine publication resultats
        try:
            cal = t.calendar
            if cal is not None and not cal.empty:
                row = cal.iloc[0] if len(cal) > 0 else None
                if row is not None:
                    ed = row.get('Earnings Date') if hasattr(row, 'get') else None
                    if ed: result['next_earnings'] = str(ed)
        except: pass
        print(f"  OK {ticker}: PE={result['pe']} ROE={result['roe']}% Div={result['yield']}% Earnings={result.get('next_earnings','?')}")
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
               'revg':'revg','epsg':'epsg','yield':'yield','beta':'beta','b52h':'b52h','b52l':'b52l'}
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
    all_results = {}
    items = list(YF_MAP.items())
    import time
    for i in range(0, len(items), 5):
        for ticker, sym in items[i:i+5]:
            all_results[ticker] = fetch_one(ticker, sym)
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
