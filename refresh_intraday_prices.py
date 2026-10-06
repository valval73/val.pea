#!/usr/bin/env python3
"""
VAL.PEA -- Rafraichissement rapide des prix en heures de marche.
Remplace l'ancien fetchLive() cote navigateur (proxies CORS publics
corsproxy.io / api.allorigins.win, morts depuis des mois -- 0 succes
sur 441 runs consecutifs, cf audit du 26/08/2026).

Ne touche que price + chg (pas les fondamentaux, deja geres par
fetch_fundamentals.py 2x/jour). Utilise yfinance.fast_info, beaucoup
plus rapide que .info pour juste un prix, avec repli sur history()
si un ticker donne echoue silencieusement (audit du 04/09/2026).

Declenche par GitHub Actions toutes les heures, Lun-Ven, heures de marche.
"""
import yfinance as yf
import re
from datetime import datetime
import pytz

PARIS = pytz.timezone('Europe/Paris')

# Mapping ticker interne -> symbole Yahoo Finance
# (porte depuis le YF_MAP cote JS de index.html, plus complet que
#  celui de fetch_fundamentals.py -- couvre aussi les mid/small caps)
from tickers import YF_MAP, NON_EUR  # table unique partagee (04/10/2026)


import time

def fetch_one_with_retry(sym, tks):
    """Essaie fast_info, retente une fois apres une pause, puis se
    rabat sur history() -- un endpoint Yahoo different, generalement
    plus fiable pour un simple cours de cloture -- si fast_info reste
    muet. Avant ce correctif, un ticker capricieux (ex: EL.PA) restait
    silencieusement fige indefiniment, sans aucune erreur visible
    (audit du 04/09/2026)."""
    for attempt in range(2):
        try:
            fi = tks.tickers[sym].fast_info
            price = fi.get('last_price') or fi.get('lastPrice')
            prev = fi.get('previous_close') or fi.get('previousClose')
            if price and price > 0.05:
                return price, prev
        except Exception:
            pass
        if attempt == 0:
            time.sleep(1.5)
    try:
        h = yf.Ticker(sym).history(period='2d')
        if not h.empty:
            price = float(h['Close'].iloc[-1])
            prev = float(h['Close'].iloc[-2]) if len(h) > 1 else price
            if price > 0.05:
                return price, prev
    except Exception:
        pass
    return None, None


def fetch_all():
    yf_syms = list(dict.fromkeys(YF_MAP.values()))  # dedupe (ALSTOM/ALO doublon)
    rev = {}
    for tk, sym in YF_MAP.items():
        rev.setdefault(sym, []).append(tk)

    out = {}
    failed = []
    # Traitement par petits paquets avec pause entre chacun -- ~95
    # tickers tapes d'affilee sans respiration declenchait un
    # rate-limit Yahoo qui faisait echouer des valeurs meme tres
    # liquides (Air Liquide et d'autres, pas seulement les tickers
    # capricieux) -- audit du 04/09/2026. Meme principe deja eprouve
    # dans fetch_fundamentals.py (paquets de 5, pause 2s).
    CHUNK = 6
    for i in range(0, len(yf_syms), CHUNK):
        chunk = yf_syms[i:i+CHUNK]
        tks = yf.Tickers(' '.join(chunk))
        for sym in chunk:
            price, prev = fetch_one_with_retry(sym, tks)
            if not price:
                failed.append(sym)
                continue
            fx = NON_EUR.get(sym, 1)
            price_eur = round(price / fx, 2)
            chg = round((price / prev - 1) * 100, 2) if prev else 0
            for tk in rev[sym]:
                out[tk] = (price_eur, chg)
        if i + CHUNK < len(yf_syms):
            time.sleep(2)
    if failed:
        print(f"  ECHEC malgre repli pour {len(failed)} valeur(s) : {', '.join(failed)}")
    return out


def patch_data_js(quotes):
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    for ticker, (price, chg) in quotes.items():
        tp = content.find(f"ticker:'{ticker}'")
        if tp == -1:
            continue
        np = content.find("ticker:'", tp + 1)
        block_end = np if np > -1 else len(content)
        block = content[tp:block_end]
        nb = re.sub(r'price:[+-]?\d+\.?\d*', f'price:{price}', block, count=1)
        if nb != block:
            block = nb
            updated += 1
        nb2 = re.sub(r'chg:[+-]?\d+\.?\d*', f'chg:{chg}', block, count=1)
        if nb2 != block:
            block = nb2
        content = content[:tp] + block + content[block_end:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    return updated


def main():
    now = datetime.now(PARIS)
    print(f"VAL.PEA -- refresh intraday -- {now.strftime('%Y-%m-%d %H:%M')} Paris")
    quotes = fetch_all()
    print(f"{len(quotes)}/{len(YF_MAP)} cours recuperes")
    if not quotes:
        print("ECHEC total -- aucun commit, on ne veut pas ecraser data.js avec du vide")
        return
    updated = patch_data_js(quotes)
    if updated: bump_index_html_version()
    print(f"data.js : {updated} valeur(s) modifiee(s) sur {len(quotes)} cours recuperes "
          f"({len(quotes)-updated} deja identiques -- rien a changer, pas une erreur)")


def bump_index_html_version():
    """Casse le cache CDN de GitHub Pages en changeant l URL de data.js a
    chaque ecriture reussie -- meme correctif que fetch_fundamentals.py
    (audit du 08/09/2026)."""
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
            print('index.html : version data.js mise a jour (cache casse)')
    except Exception as e:
        print(f'  WARN bump version: {e}')


if __name__ == '__main__':
    main()
