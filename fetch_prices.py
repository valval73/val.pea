import urllib.request, urllib.parse, json, time

PROXY = 'https://corsproxy.io/?'
YF_BASE = 'https://query1.finance.yahoo.com/v8/finance/chart/'

YF_MAP = {
  "MC":"MC.PA","AI":"AI.PA","OR":"OR.PA","RMS":"RMS.PA","SAN":"SAN.PA",
  "TTE":"TTE.PA","SAF":"SAF.PA","SU":"SU.PA","AXA":"CS.PA","BNP":"BNP.PA",
  "ACA":"ACA.PA","GLE":"GLE.PA","AIR":"AIR.PA","CAP":"CAP.PA","DSY":"DSY.PA",
  "LR":"LR.PA","PUB":"PUB.PA","RI":"RI.PA","SGO":"SGO.PA","VIE":"VIE.PA",
  "ORA":"ORA.PA","EL":"EL.PA","KER":"KER.PA","STM":"STM.PA","ENX":"ENX.PA",
  "ENGI":"ENGI.PA","DG":"DG.PA","HO":"HO.PA","BN":"BN.PA","CA":"CA.PA",
  "WLN":"WLN.PA","RNO":"RNO.PA","TEP":"TEP.PA","FTI":"FTI.PA","ALO":"ALO.PA",
  "EDEN":"EDEN.PA","SAM":"SAM.PA","GTT":"GTT.PA","SEB":"SK.PA","VK":"VK.PA",
  "MT":"MT.AS","STLA":"STLA.MI","SAP":"SAP.DE","ASML":"ASML.AS",
  "SIE":"SIE.DE","BAYN":"BAYN.DE","BMW":"BMW.DE","ALV":"ALV.DE",
  "ENEL":"ENEL.MI","ENI":"ENI.MI","UCG":"UCG.MI","RACE":"RACE.MI",
  "CABK":"CABK.MC","BBVA":"BBVA.MC","IBE":"IBE.MC","ITX":"ITX.MC",
  "TEF":"TEF.MC","NN":"NN.AS","INGA":"INGA.AS","AD":"AD.AS"
}

out = {}
rev = {v: k for k, v in YF_MAP.items()}
HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
  'Accept': 'application/json, */*',
}

def fetch_price(yf_sym):
    url = PROXY + urllib.parse.quote(YF_BASE + yf_sym + '?range=1d&interval=5m', safe='')
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=12) as resp:
        data = json.loads(resp.read())
    m = data['chart']['result'][0]['meta']
    p = m['regularMarketPrice']
    prev = m['chartPreviousClose']
    if not p or p <= 0: return None
    return {
        'p': round(float(p), 2),
        'c': round((float(p) - float(prev)) / float(prev) * 100, 2),
        'h52': round(float(m.get('fiftyTwoWeekHigh') or 0), 2),
        'l52': round(float(m.get('fiftyTwoWeekLow') or 0), 2)
    }

BATCH = 5
syms = list(YF_MAP.values())
for i in range(0, len(syms), BATCH):
    batch = syms[i:i+BATCH]
    for sym in batch:
        try:
            data = fetch_price(sym)
            if data:
                tk = rev.get(sym)
                if tk:
                    out[tk] = data
                    print(f"  {tk}: {data['p']}e ({'+' if data['c']>0 else ''}{data['c']}%)")
        except Exception as e:
            print(f"  ERR {sym}: {str(e)[:50]}")
        time.sleep(0.3)
    if i + BATCH < len(syms):
        time.sleep(1.5)

out['_updated'] = int(time.time())
out['_count'] = len(out) - 2
with open('prices.json', 'w') as f:
    json.dump(out, f, indent=2)
print(f"Done: {out['_count']} prix dans prices.json")
