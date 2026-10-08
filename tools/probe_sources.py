"""Sonde filings.xbrl.org (resultat dans probe_sources.json)."""
import json, requests
B = 'https://filings.xbrl.org'
out = {}
def get(u):
    r = requests.get(u if u.startswith('http') else B + u, timeout=30)
    return r.status_code, r.json()
try:
    st, d = get('/api/entities?page[size]=2&filter=' + json.dumps([{"name": "name", "op": "ilike", "val": "%LVMH%"}]))
    e = d['data'][0]
    out['entity'] = e
    rel = e.get('relationships', {}).get('filings', {}).get('links', {}).get('related')
    out['rel'] = rel
    if rel:
        st, f = get(rel + ('&' if '?' in rel else '?') + 'page[size]=10')
        out['filings'] = [(x['attributes'].get('period_end'), x['attributes'].get('json_url'), x['attributes'].get('date_added')) for x in f.get('data', [])]
    # filtre relationnel direct
    flt = [{"name": "entity", "op": "has", "val": {"name": "identifier", "op": "eq", "val": e['attributes']['identifier']}}]
    st, f2 = get('/api/filings?page[size]=5&sort=-period_end&filter=' + json.dumps(flt))
    out['has_filter'] = [st, [(x['attributes'].get('period_end'), x['attributes'].get('json_url')) for x in f2.get('data', [])] if isinstance(f2, dict) else str(f2)[:200]]
    # faits d'un rapport LVMH
    ju = (out.get('filings') or [[None, None]])[0][1]
    if ju:
        st, j = get(ju)
        facts = j.get('facts', {})
        sample = {}
        for f in facts.values():
            dm = f.get('dimensions', {})
            c = dm.get('concept', '')
            if c in ('ifrs-full:Revenue', 'ifrs-full:RevenueFromContractsWithCustomers', 'ifrs-full:ProfitLossAttributableToOwnersOfParent'):
                sample.setdefault(c, []).append([f.get('value'), dm.get('period'), dm.get('unit'), sorted(dm.keys()), f.get('decimals')])
        out['facts'] = {k: v[:6] for k, v in sample.items()}
    # autres entites test
    out['names'] = {}
    for n in ('AIR LIQUIDE', 'HERMES', 'SCHNEIDER', 'AMADEUS', 'ASML', 'THALES', 'ELIS', 'INTERPARFUMS', 'TOTALENERGIES', 'WOLTERS'):
        st, d = get('/api/entities?page[size]=5&filter=' + json.dumps([{"name": "name", "op": "ilike", "val": f"%{n}%"}]))
        out['names'][n] = [(x['attributes'].get('name'), x['attributes'].get('identifier')) for x in d.get('data', [])]
except Exception as ex:
    out['error'] = repr(ex)[:400]
json.dump(out, open('probe_sources.json', 'w'), indent=1, ensure_ascii=False)
