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


def region_list(region, exch, fx):
    q = Q('and', [Q('eq', ['region', region]), Q('eq', ['exchange', exch]),
                  Q('gt', ['intradaymarketcap', SEUIL_EUR * fx])])
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
    C = json.load(open('candidats.json', encoding='utf-8'))
    deja = {s.upper() for s in YF_MAP.values()}
    for k, v in C.items():
        if isinstance(v, list) and k != 'univers_pea_300M':
            deja |= {c.split(':', 1)[1].upper() for c in v if c.startswith('YF:')}
    syms, bilan = [], {}
    for region, (exch, fx) in PLACES.items():
        try:
            lst = region_list(region, exch, fx)
        except Exception as e:
            print('ECHEC', region, e)
            bilan[region] = 'echec'
            continue
        bilan[region] = len(lst)
        syms += [s for s in lst if s.upper() not in deja]
        time.sleep(1)
    syms = sorted(set(syms))
    C['univers_pea_300M'] = ['YF:' + s for s in syms]
    json.dump(C, open('candidats.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('Univers :', bilan, '->', len(syms), 'nouvelles valeurs')


if __name__ == '__main__':
    main()
