import urllib.request, json, time

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

syms = list(YF_MAP.values())
prices = {}
hdrs = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}

for i in range(0, len(syms), 20):
    batch = ",".join(syms[i:i+20])
    url = ("https://query1.finance.yahoo.com/v7/finance/quote"
           "?symbols=" + batch +
           "&fields=regularMarketPrice,regularMarketChangePercent"
           ",fiftyTwoWeekHigh,fiftyTwoWeekLow")
    try:
        req = urllib.request.Request(url, headers=hdrs)
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        for q in data.get("quoteResponse", {}).get("result", []):
            s = q.get("symbol", "")
            p = q.get("regularMarketPrice", 0)
            if p > 0:
                prices[s] = {
                    "p": round(p, 2),
                    "c": round(q.get("regularMarketChangePercent", 0), 2),
                    "h52": round(q.get("fiftyTwoWeekHigh", 0), 2),
                    "l52": round(q.get("fiftyTwoWeekLow", 0), 2)
                }
        print(f"Batch {i//20+1}: {len(prices)} total OK")
    except Exception as e:
        print(f"Batch {i//20+1} ERR: {e}")
    time.sleep(0.8)

rev = {v: k for k, v in YF_MAP.items()}
out = {rev[s]: v for s, v in prices.items() if s in rev}
out["_updated"] = int(time.time())
out["_count"] = len(out) - 2

with open("prices.json", "w") as f:
    json.dump(out, f, indent=2)

print(f"Done: {out['_count']} prices written to prices.json")
