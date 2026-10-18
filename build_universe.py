"""
VAL.PEA -- Construit l'univers elargi : toutes les actions des places de
l'UE/EEE (eligibles PEA par le siege) au-dessus d'environ 300 M EUR de
capitalisation, a partir du screener de Yahoo (meme source que le reste du
screener ; rien n'est repris d'un autre site).

Ecrit la liste 'univers_pea_300M' dans candidats.json (codes 'YF:SYMBOLE'),
sans les valeurs deja suivies dans data.js ni celles des autres listes.
Lance chaque semaine par le workflow Candidats, juste avant le filtre.

Limite connue : Yahoo classe par place de cotation, pas par siege. Une
societe cotee a Paris mais domiciliee hors UE/EEE peut entrer : la fiche
d'une valeur qui passe la grille reste a verifier avant tout achat.
"""
import json, time
import yfinance as yf
from yfinance import EquityQuery as Q
from tickers import YF_MAP
from screen_candidates import yahoo

SEUIL_EUR = 3e8
# region Yahoo -> (place principale, taux approximatif devise locale / EUR)
PLACES = {
    'fr': ('PAR', 1), 'de': ('GER', 1), 'it': ('MIL', 1), 'es': ('MCE', 1),
    'nl': ('AMS', 1), 'be': ('BRU', 1), 'pt': ('LIS', 1), 'at': ('VIE', 1),
    'fi': ('HEL', 1), 'ie': ('ISE', 1), 'gr': ('ATH', 1), 'ee': ('TAL', 1),
    'lt': ('LIT', 1), 'lv': ('RIS', 1), 'se': ('STO', 11.0), 'dk': ('CPH', 7.46),
    'no': ('OSL', 11.6), 'pl': ('WSE', 4.25), 'cz': ('PRA', 25.0),
    'hu': ('BUD', 400.0), 'ro': ('BVB', 5.0), 'is': ('ICE', 150.0),
}


# 18/10/2026 : univers compte-titres, places ouvertes chez Bourse Direct
# (New York, Londres, Suisse). Seuils en devise locale.
# US a 5 Md USD : passage tenable en 5 h malgre la limite de debit Yahoo
PLACES_CTO = {'us': (['NYQ', 'NMS', 'NGM', 'NCM'], 5e9), 'gb': (['LSE'], 1e9), 'ch': (['EBS'], 1e9)}


def region_list(region, exch, fx, seuil=None):
    ex = Q('is-in', ['exchange'] + exch) if isinstance(exch, list) else Q('eq', ['exchange', exch])
    q = Q('and', [Q('eq', ['region', region]), ex,
                  Q('gt', ['intradaymarketcap', seuil if seuil else SEUIL_EUR * fx])])
    out, offset = [], 0
    while True:
        r = yf.screen(q, offset=offset, size=250, sortField='intradaymarketcap', sortAsc=False)
        quotes = (r or {}).get('quotes') or []
        out += [x.get('symbol') for x in quotes if x.get('symbol')]
        total = (r or {}).get('total') or 0
        offset += 250
        if not quotes or offset >= total:
            break
        time.sleep(1)
    return out


def main():
    import sys
    cto = len(sys.argv) > 1 and sys.argv[1] == 'cto'
    cle = 'univers_cto' if cto else 'univers_pea_300M'
    from screen_candidates import charger_listes
    C = charger_listes()
    deja = {s.upper() for s in YF_MAP.values()}
    for k, v in C.items():
        if isinstance(v, list) and k != cle:
            for c in v:
                y_ = yahoo(c)  # codes MIC des autres listes -> symbole Yahoo (pas de doublon)
                if y_:
                    deja.add(y_.upper())
    syms, bilan = [], {}
    places = {r: (e, 1, sl) for r, (e, sl) in PLACES_CTO.items()} if cto else {r: (e, f, None) for r, (e, f) in PLACES.items()}
    for region, (exch, fx, sl) in places.items():
        try:
            lst = region_list(region, exch, fx, sl)
        except Exception as e:
            print('ECHEC', region, e)
            bilan[region] = 'echec'
            continue
        bilan[region] = len(lst)
        syms += [s for s in lst if s.upper() not in deja]
        time.sleep(1)
    syms = sorted(set(syms))
    # 18/10/2026 : fichier propre a chaque univers (les deux workflows ne se
    # disputent plus candidats.json au moment du commit)
    fic = 'univers_cto.json' if cto else 'univers_pea.json'
    json.dump({cle: ['YF:' + s for s in syms]}, open(fic, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('Univers :', bilan, '->', len(syms), 'nouvelles valeurs')


if __name__ == '__main__':
    main()
