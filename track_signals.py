"""
VAL.PEA -- Suivi en conditions reelles (12/10/2026).

Pourquoi : le backtest reconstitue le passe avec les valeurs de qualite
d'aujourd'hui (biais du survivant). La seule preuve qui compte est de noter
les signaux AU MOMENT ou ils sont emis, puis de regarder 12 mois plus tard.

Une fois par mois civil (premiere mise a jour du mois), on photographie :
  - panier "achat"  : valeurs du filtre qualite dont le cours est dans la zone
                      d'achat (cours <= haut du palier 1) ;
  - panier "filtre" : toutes les valeurs du filtre qualite ;
  - la reference    : ETF MSCI World capitalisant (CW8).
Au bout de 365 jours, chaque photo est evaluee une fois, puis figee :
rendement moyen (poids egaux) de chaque panier contre l'ETF.
Dividendes : approximes par le dividende des 12 mois precedant la photo.
Aucune position personnelle n'est enregistree. Fichier : signals_history.json
"""
import json
from datetime import date

from routine_mail import load

OUT = 'signals_history.json'
BENCH = 'CW8'
HORIZON = 365


def snapshot(D):
    S = [s for s in D['S'] if s and s.get('ticker') and (s.get('price') or 0) > 0]
    etf = {e['ticker']: e.get('price') for e in D['ETF']}
    q = [s for s in S if s.get('qok')]
    buy = [s for s in q if (s.get('eh') or 0) > 0 and s['price'] <= s['eh']]
    row = lambda s: {'t': s['ticker'], 'p': s['price'], 'd': s.get('div12') or 0}
    return {'date': date.today().isoformat(), 'bench': etf.get(BENCH),
            'achat': [row(s) for s in buy], 'filtre': [row(s) for s in q]}


def basket_return(items, now):
    rs = [((now[i['t']] + i['d']) / i['p'] - 1) * 100 for i in items if now.get(i['t']) and i['p']]
    return (round(sum(rs) / len(rs), 1), len(rs)) if rs else (None, 0)


def main():
    import subprocess
    try:
        D = load()
    except subprocess.CalledProcessError as e:
        print('ERREUR NODE :', (e.stderr or '')[-1500:])
        raise
    try:
        H = json.load(open(OUT, encoding='utf-8'))
    except Exception:
        H = {'snapshots': []}
    today = date.today()
    snaps = H['snapshots']
    if not snaps or snaps[-1]['date'][:7] != today.isoformat()[:7]:
        snaps.append(snapshot(D))
        print('photo du mois enregistree :', len(snaps[-1]['achat']), 'en zone,', len(snaps[-1]['filtre']), 'dans le filtre')
    now = {s['ticker']: s['price'] for s in D['S'] if s and s.get('ticker') and s.get('price')}
    bench_now = {e['ticker']: e.get('price') for e in D['ETF']}.get(BENCH)
    for s in snaps:
        if 'res' in s or (today - date.fromisoformat(s['date'])).days < HORIZON:
            continue
        a, na = basket_return(s['achat'], now)
        f, nf = basket_return(s['filtre'], now)
        b = round((bench_now / s['bench'] - 1) * 100, 1) if (bench_now and s.get('bench')) else None
        s['res'] = {'evalue': today.isoformat(), 'achat': a, 'n_achat': na, 'filtre': f, 'n_filtre': nf, 'etf': b}
        print('evaluation', s['date'], s['res'])
    done = [s['res'] for s in snaps if 'res' in s]
    H['bilan'] = {'photos': len(snaps), 'evaluees': len(done),
                  'achat_bat_etf': sum(1 for r in done if r['achat'] is not None and r['etf'] is not None and r['achat'] > r['etf']),
                  'filtre_bat_etf': sum(1 for r in done if r['filtre'] is not None and r['etf'] is not None and r['filtre'] > r['etf'])}
    json.dump(H, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('bilan :', H['bilan'])


if __name__ == '__main__':
    main()
