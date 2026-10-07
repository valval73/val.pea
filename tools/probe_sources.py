"""Sonde des sources de donnees gratuites (resultat ecrit dans probe_sources.json)."""
import json, requests
out = {}
B = 'https://filings.xbrl.org'
try:
    q = B + '/api/filings?page[size]=3&sort=-date_added&filter=' + json.dumps([{"name": "country", "op": "eq", "val": "FR"}])
    r = requests.get(q, timeout=20)
    d = r.json()
    out['xbrl_status'] = r.status_code
    items = d.get('data', [])
    out['xbrl_n'] = len(items)
    if items:
        a = items[0].get('attributes', {})
        out['xbrl_keys'] = list(a)[:30]
        out['xbrl_first'] = {k: a.get(k) for k in ('fxo_id', 'period_end', 'json_url', 'date_added')}
        ju = a.get('json_url')
        if ju:
            j = requests.get(B + ju if ju.startswith('/') else ju, timeout=60).json()
            facts = j.get('facts', {})
            out['xbrl_facts'] = len(facts)
            cs = {}
            for f in facts.values():
                c = f.get('dimensions', {}).get('concept', '')
                if c in ('ifrs-full:Revenue', 'ifrs-full:ProfitLoss', 'ifrs-full:ProfitLossAttributableToOwnersOfParent',
                         'ifrs-full:CashFlowsFromUsedInOperatingActivities', 'ifrs-full:Equity', 'ifrs-full:BasicEarningsLossPerShare'):
                    cs.setdefault(c, []).append([f.get('value'), f.get('dimensions', {}).get('period'), len(f.get('dimensions', {}))])
            out['xbrl_sample'] = {k: v[:3] for k, v in cs.items()}
    # recherche par nom d'entite
    r2 = requests.get(B + '/api/entities?page[size]=3&filter=' + json.dumps([{"name": "name", "op": "ilike", "val": "%LVMH%"}]), timeout=20)
    out['xbrl_entity'] = [(e.get('attributes', {}).get('name'), e.get('attributes', {}).get('identifier')) for e in r2.json().get('data', [])]
except Exception as e:
    out['xbrl_error'] = str(e)[:300]
json.dump(out, open('probe_sources.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1)[:3000])
