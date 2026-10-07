"""
VAL.PEA -- 2e source de donnees (07/10/2026).
Compare le cours Yahoo (data.js) a une source independante :
  - Stooq (gratuit, sans cle) ;
  - Financial Modeling Prep si une cle FMP_KEY est fournie (secret GitHub, optionnel),
    qui permet aussi de comparer le PER et la croissance.
Ecart > 3 % sur le cours (ou > 25 % sur le PER) -> ajoute au champ dq de la fiche
("donnee a verifier"), ce qui bloque la decision d'achat dans le screener.
Ne corrige jamais une donnee : signale seulement.
"""
import csv, io, json, os, re, sys, time
import requests
from tickers import YF_MAP

FMP = (os.environ.get('FMP_KEY') or '').strip()
UA = {'User-Agent': 'Mozilla/5.0'}
SUFFIX = {'.PA': '.fr', '.AS': '.nl', '.DE': '.de', '.MI': '.it', '.CO': '.dk', '.BR': '.be',
          '.MC': '.es', '.L': '.uk', '.SW': '.ch', '.ST': '.se', '.HE': '.fi', '.OL': '.no', '.LS': '.pt'}


def stooq_sym(y):
    for k, v in SUFFIX.items():
        if y.endswith(k):
            return y[:-len(k)].lower() + v
    return None


def stooq_price(y):
    s = stooq_sym(y)
    if not s:
        return None
    try:
        r = requests.get(f'https://stooq.com/q/l/?s={s}&f=sd2t2ohlcv&h&e=csv', headers=UA, timeout=8)
        rows = list(csv.DictReader(io.StringIO(r.text)))
        c = rows[0].get('Close') if rows else None
        return float(c) if c and c not in ('N/D', '') else None
    except Exception:
        return None


def fmp_quote(y):
    if not FMP:
        return None
    try:
        r = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{y}?apikey={FMP}', timeout=15)
        d = r.json()
        return d[0] if isinstance(d, list) and d else None
    except Exception:
        return None


def load_stocks():
    t = open('data.js', encoding='utf-8').read().split('const ETF')[0]
    out = {}
    for b in re.split(r"\{ticker:'", t)[1:]:
        tk = b.split("'")[0]
        g = lambda k: (re.search(r'\b' + k + r":(-?[0-9.]+)", b) or [None, None])[1]
        out[tk] = {'price': float(g('price') or 0), 'pe': float(g('pe') or 0)}
    return out


def main():
    S = load_stocks()
    res, n_ok, n_src, miss = {}, 0, 0, 0
    for tk, y in YF_MAP.items():
        if tk not in S or not S[tk]['price']:
            continue
        p0 = S[tk]['price']
        alt, src, pe_alt = None, None, None
        q = fmp_quote(y)
        if q and q.get('price'):
            alt, src, pe_alt = float(q['price']), 'FMP', q.get('pe')
        elif miss < 10 or n_src:  # arret rapide si la source ne repond pas
            alt = stooq_price(y)
            src = 'Stooq' if alt else None
            miss = 0 if alt else miss + 1
        time.sleep(0.3)
        if not alt:
            continue
        n_src += 1
        d = (alt / p0 - 1) * 100
        issues = []
        if abs(d) > 3:
            issues.append(f'cours {src} {alt:.2f} contre Yahoo {p0:.2f} ({d:+.0f} %)')
        if pe_alt and S[tk]['pe'] and abs(pe_alt / S[tk]['pe'] - 1) > 0.25:
            issues.append(f'PER {src} {pe_alt:.1f} contre Yahoo {S[tk]["pe"]:.1f}')
        if not issues:
            n_ok += 1
        res[tk] = {'src': src, 'alt': round(alt, 2), 'diff': round(d, 1), 'issues': issues}
    json.dump({'date': time.strftime('%Y-%m-%d'), 'n': n_src, 'ok': n_ok, 'res': res},
              open('cross_check.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'2e source : {n_src} valeurs comparees, {n_ok} concordantes')
    for tk, r in res.items():
        if r['issues']:
            print(' ', tk, ' · '.join(r['issues']))
    # report dans data.js (champ x2 : ecarts de la 2e source)
    js = open('data.js', encoding='utf-8').read()
    head, sep, tail = js.partition('const ETF')
    def patch(m):
        blk = m.group(0)
        tk = blk[len("{ticker:'"):].split("'")[0]
        iss = ' · '.join(res.get(tk, {}).get('issues', [])).replace("'", ' ')
        src = res.get(tk, {}).get('src') or ''
        blk = re.sub(r",x2:'[^']*',x2s:'[^']*'", '', blk)
        return blk.replace("{ticker:'" + tk + "'", "{ticker:'" + tk + "',x2:'" + iss + "',x2s:'" + src + "'", 1)
    head = re.sub(r"\{ticker:'[^']+'(?:,x2:'[^']*',x2s:'[^']*')?", patch, head)
    open('data.js', 'w', encoding='utf-8').write(head + sep + tail)


if __name__ == '__main__':
    main()
