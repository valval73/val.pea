import yfinance as yf
import json, time

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
rev = {v:k for k,v in YF_MAP.items()}
all_yf = list(YF_MAP.values())

for i in range(0, len(all_yf), 20):
    batch = all_yf[i:i+20]
    try:
        tickers = yf.Tickers(" ".join(batch))
        for sym in batch:
            try:
                info = tickers.tickers[sym].fast_info
                p = info.last_price
                prev = info.previous_close
                if p and p > 0 and prev and prev > 0:
                    c = round((p-prev)/prev*100, 2)
                    tk = rev.get(sym)
                    if tk:
                        out[tk] = {"p":round(float(p),2),"c":c,"h52":round(float(info.year_high or 0),2),"l52":round(float(info.year_low or 0),2)}
            except: pass
        print(f"Batch {i//20+1}: OK")
    except Exception as e:
        print(f"Batch {i//20+1} ERR: {e}")
    time.sleep(1)

out["_updated"] = int(time.time())
out["_count"] = len(out) - 2
with open("prices.json","w") as f:
    json.dump(out, f, indent=2)
print(f"Done: {out['_count']} prices")
