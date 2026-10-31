"""VAL.PEA -- alertes d'anticipation (31/10/2026).

Ce que le marché « voit » avant les résultats, avec des chiffres publics :
  1. Révision des analystes : bénéfice par action attendu pour l'exercice
     suivant, aujourd'hui contre il y a 90 jours (Yahoo, eps_trend).
     Alerte si baisse de plus de 5 %.
  2. Retard sur les concurrents : croissance du chiffre d'affaires de
     l'action inférieure de plus de 5 points à la médiane de ses 3
     concurrents (peers.js), à deux publications de suite. Une seule
     publication = « à surveiller ».

Règle : une alerte = une contre-expertise à faire. Jamais un achat ni une
vente à elle seule. Même règle pour toutes les actions (portefeuille comme
candidates). Le cas « le cours baisse mais ni 1 ni 2 ne bouge » se lit
comme du bruit de marché : rien à coder.

Lancé chaque dimanche après fetch_peers.py. Sortie : anticipation.json.
"""
import json, os, re, time, datetime
import yfinance as yf
from tickers import YF_MAP

FICHIER = 'anticipation.json'
SEUIL_REVISION = -5.0   # % en 90 jours
SEUIL_ECART = -5.0      # points de croissance sous la médiane des concurrents


def revision(sym):
    """(période, bpa actuel, bpa il y a 90 j, variation %) ou None."""
    try:
        df = yf.Ticker(sym).eps_trend
    except Exception as e:
        print('  eps_trend', sym, e)
        return None
    if df is None or getattr(df, 'empty', True):
        return None
    for per in ('+1y', '0y'):
        if per not in df.index:
            continue
        r = df.loc[per]
        cur, old = r.get('current'), r.get('90daysAgo')
        try:
            cur, old = float(cur), float(old)
        except (TypeError, ValueError):
            continue
        if cur != cur or old != old or old <= 0:   # NaN ou bénéfice négatif : pas de %
            continue
        return per, round(cur, 3), round(old, 3), round((cur / old - 1) * 100, 1)
    return None


def lire_peers():
    try:
        t = open('peers.js', encoding='utf-8').read()
        return json.loads(re.search(r'const PEERS = (\{.*\});', t, re.S).group(1)).get('groups', {})
    except Exception as e:
        print('peers.js illisible', e)
        return {}


def main():
    today = datetime.date.today().isoformat()
    old = json.load(open(FICHIER, encoding='utf-8')) if os.path.exists(FICHIER) else {}
    hist = old.get('ecart_hist', {})
    alertes, surveiller = [], []

    # 1. Révisions des analystes : toutes les actions du screener
    eps = {}
    for t, sym in YF_MAP.items():
        r = revision(sym)
        time.sleep(0.3)
        if not r:
            continue
        per, cur, o90, var = r
        eps[t] = {'periode': per, 'bpa': cur, 'bpa_90j': o90, 'var': var}
        if var <= SEUIL_REVISION:
            alertes.append({'t': t, 'type': 'revision',
                            'txt': f"bénéfice attendu ({'exercice suivant' if per == '+1y' else 'exercice en cours'}) "
                                   f"révisé de {var:+.1f} % en 90 jours ({o90} → {cur})"})
    print(f'{len(eps)} actions avec révisions')

    # 2. Retard sur les concurrents : actions avec concurrents définis
    for t, g in lire_peers().items():
        me, med = (g.get('self') or {}).get('revg'), (g.get('med') or {}).get('revg')
        if me is None or med is None:
            continue
        H = hist.setdefault(t, [])
        if not H or H[-1][1] != me:          # nouveau chiffre = nouvelle publication
            H.append([today, me, med])
            del H[:-6]
        derniers = H[-2:]
        en_retard = [h for h in derniers if h[1] - h[2] <= SEUIL_ECART]
        txt = f"croissance {me:+.1f} % contre {med:+.1f} % pour la médiane des concurrents"
        if len(derniers) == 2 and len(en_retard) == 2:
            alertes.append({'t': t, 'type': 'concurrents', 'txt': txt + ' — deux publications de suite'})
        elif H[-1][1] - H[-1][2] <= SEUIL_ECART:
            surveiller.append({'t': t, 'type': 'concurrents',
                               'txt': txt + ' — une seule publication (à confirmer ; chiffre Yahoo, devises et acquisitions comprises)'})

    out = {'date': today, 'alertes': alertes, 'surveiller': surveiller, 'eps': eps, 'ecart_hist': hist}
    json.dump(out, open(FICHIER, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{len(alertes)} alerte(s), {len(surveiller)} à surveiller')


if __name__ == '__main__':
    main()
