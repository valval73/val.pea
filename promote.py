"""
VAL.PEA -- 19/10/2026 : promotion automatique du radar vers le screener.

Toute valeur du radar elargi (PEA ou compte-titres) qui passe la grille
qualite recoit une fiche complete dans data.js (paliers, alertes, seuil de
sortie), mise a jour comme les autres. Une fois promue, elle reste suivie
(meme si elle sort ensuite de la grille : elle passe alors en "hors qualite",
masquee par defaut mais toujours analysee).

Devises prises en charge : EUR, USD, CHF, SEK, NOK, DKK, PLN. Londres (cours
en pence) est exclu tant que la conversion pence/livre n'est pas verifiee.
"""
import json, re, os
from tickers import YF_MAP

FICHIER = 'radar_promus.json'
DEVISES = {'EUR', 'USD', 'CHF', 'SEK', 'NOK', 'DKK', 'PLN'}
SOURCES = [('PEA', 'candidats_resultats.json'), ('CTO', 'candidats_cto_resultats.json')]


def ident(sym, pris):
    base, _, suf = sym.partition('.')
    tk = re.sub(r'[^A-Z0-9]', '', base.upper()) + re.sub(r'[^A-Z]', '', suf.upper())
    tk = tk[:12] or 'X'
    i = 2
    while tk in pris:
        tk = tk[:10] + str(i); i += 1
    return tk


STOPN = {'SE','AG','SA','AB','ASA','INC','PLC','NV','N','V','OYJ','SPA','S','A','THE','GROUP','HOLDING','HOLDINGS',
         'CORP','CORPORATION','LTD','LIMITED','CO','KGAA','I'}
SECONDAIRES = ('VI', 'F', 'DU', 'MU', 'BE', 'SG', 'HM')


def cle_nom(n):
    w = [x for x in re.sub(r'[^A-Z0-9 ]', ' ', str(n or '').upper()).split() if x not in STOPN]
    return ' '.join(w[:2])


def rang(sym):
    """Plus petit = cotation preferee : place principale europeenne, puis US, puis secondaires."""
    suf = sym.rpartition('.')[2] if '.' in sym else ''
    return 2 if suf in SECONDAIRES else (1 if not suf else 0)


def nom_propre(n):
    n = re.sub(r'\s{2,}.*$', '', str(n or '')).strip()
    return n.replace("'", ' ')[:60]


def main():
    deja = json.load(open(FICHIER)) if os.path.exists(FICHIER) else []
    syms = {r[1].upper() for r in deja} | {v.upper() for v in YF_MAP.values()}
    pris = set(YF_MAP) | {r[0] for r in deja}
    # 19/10/2026 : une societe = une fiche (Strabag, Ryanair, Hochtief... etaient en double)
    noms = {cle_nom(r[2]) for r in deja}
    try:
        t = open('data.js', encoding='utf-8').read().split('const ETF')[0]
        noms |= {cle_nom(n) for n in re.findall(r"name:'((?:[^'\\]|\\.)*)'", t)}
    except Exception:
        pass
    cand = []
    for compte, f in SOURCES:
        if not os.path.exists(f):
            continue
        for liste in (json.load(open(f)).get('listes') or {}).values():
            for l in liste.get('lignes') or []:
                cand.append((rang((l.get('yahoo') or '').upper()), compte, l))
    cand.sort(key=lambda x: x[0])
    ajout = 0
    for _, compte, l in cand:
        sym = (l.get('yahoo') or '').upper()
        if not l.get('qok') or not sym or sym in syms or l.get('devise') not in DEVISES:
            continue
        if cle_nom(l.get('nom')) in noms:
            continue
        cap = l.get('cap_Md') or 0
        taille = 'large' if cap >= 10 else 'mid' if cap >= 2 else 'small'
        tk = ident(sym, pris)
        deja.append([tk, l['yahoo'], nom_propre(l.get('nom')),
                     (l.get('secteur') or 'Autre') + (' (compte-titres)' if compte == 'CTO' else ''),
                     taille, l['devise'], compte])
        syms.add(sym); pris.add(tk); noms.add(cle_nom(l.get('nom'))); ajout += 1
    json.dump(deja, open(FICHIER, 'w'), ensure_ascii=False, indent=0)
    print(f'Radar -> screener : {ajout} nouvelles fiches, {len(deja)} promues au total')


if __name__ == '__main__':
    main()
