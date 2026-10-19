"""19/10/2026 : la SEC repond-elle depuis GitHub Actions ?"""
import json, requests
out = {}
for ua in ['VAL.PEA screener personnel valpea@users.noreply.github.com', 'ValPea Research valpea@users.noreply.github.com', 'Mozilla/5.0 (compatible; ValPea/1.0; +https://github.com/valval73/val.pea) valpea@users.noreply.github.com']:
    for u in ['https://www.sec.gov/files/company_tickers.json', 'https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json']:
        try:
            r = requests.get(u, headers={'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate'}, timeout=30)
            out[ua[:20] + ' | ' + u[-40:]] = [r.status_code, r.text[:120]]
        except Exception as e:
            out[ua[:20] + ' | ' + u[-40:]] = str(e)
json.dump(out, open('probe_sources.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
