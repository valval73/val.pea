#!/usr/bin/env python3
"""
VAL.PEA -- Mise a jour automatique des donnees fondamentales
Declenche par GitHub Actions 2x/jour (7h + 17h35 Paris)
Met a jour : PE, PB, ROE, dividende, bilan, prochains resultats,
ainsi que le DCF (dcfb/dcfm/dcfu) et les zones d'achat (el/eh/stop/o1/o2).

Le DCF etait fige depuis la creation de chaque fiche (jamais recalcule --
audit du 26/08/2026). Il est maintenant recalcule a chaque run, avec une
vraie classification sectorielle (18 categories couvrant les 193 secteurs
reels du screener, contre 4/193 avant).
"""
import yfinance as yf
import re, json, sys, math, unicodedata
from datetime import datetime
import pytz

PARIS = pytz.timezone('Europe/Paris')

from tickers import YF_MAP, NON_EUR, check_coverage, purge_data_js
try:
    from official_growth import OFFICIAL_GROWTH
except Exception:
    OFFICIAL_GROWTH = {}
try:
    from moat import MOAT, MOAT_MIN_BUY
except Exception:
    MOAT, MOAT_MIN_BUY = {}, 3
try:
    from moat import UNCERTAINTY, MARGIN
except Exception:
    UNCERTAINTY, MARGIN = {}, {'moyenne': (0.25, 0.15)}

# ─── Classification sectorielle (mots-cles, couvre 193/193 secteurs reels
#      du screener -- audit du 26/08/2026 avait trouve 4/193 seulement) ───
def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# Regles prioritaires (1re correspondance gagnante). Avant le 04/10/2026,
# 'electrique'/'gaz industriels'/'energie' envoyaient Air Liquide,
# Schneider, Legrand et Rexel dans 'Energie' (PER juste 14, celui d'un
# petrolier) : leur valeur intrinseque etait divisee par ~2 et le
# screener les classait 'eviter'.
SECTOR_RULES = [
    ('gaz industriels', 'Industrie'), ('automatisation', 'Industrie'),
    ('electricite batiment', 'Industrie'), ('lng technology', 'Industrie'),
    ('luxe', 'Luxe'), ('maroquinerie', 'Luxe'), ('parfum', 'Luxe'),
    ('champagne', 'Luxe'), ('cosmetique', 'Luxe'), ('bijou', 'Luxe'),
    ('spiritueux', 'Luxe'), ('vins bordeaux', 'Luxe'), ('licences parfums', 'Luxe'),
    ('semi-conducteur', 'Semiconducteurs'), ('connecteurs rf', 'Semiconducteurs'),
    ('instruments mesure', 'Semiconducteurs'), ('instruments scientifiques', 'Semiconducteurs'),
    ('electronique embarquee', 'Semiconducteurs'), ('optique', 'Semiconducteurs'),
    ('saas', 'Logiciel'), ('erp cloud', 'Logiciel'), ('logiciel', 'Logiciel'),
    ('cybersecurite', 'Logiciel'), ('industrie digitale', 'Logiciel'),
    ('esn ', 'Logiciel'), ('services it', 'Logiciel'), ('services informatiques', 'Logiciel'),
    ('recrutement tech', 'Logiciel'), ('tech investissement', 'Logiciel'),
    ('visioconference', 'Logiciel'), ('diagnostic medical ia', 'Logiciel'),
    ('iot industriel', 'Logiciel'),
    ('biotech', 'Biotech'), ('pharma', 'Biotech'), ('homeopathie', 'Biotech'),
    ('radioenhancement', 'Biotech'), ('chimie pharmaceutique', 'Biotech'),
    ('laboratoires analyses', 'Biotech'), ('diagnostics medicaux', 'Biotech'),
    ('sante materiel medical', 'Biotech'), ('sante services', 'Biotech'),
    ('aviation', 'Defense'), ('aeronautique', 'Defense'), ('defense', 'Defense'),
    ('drones', 'Defense'), ('pyrotechnie', 'Defense'), ('simulation combat', 'Defense'),
    ('fixations aeronautiques', 'Defense'), ('usinage aeronautique', 'Defense'),
    ('ingenierie thermique spatial', 'Defense'), ('infrastructure aeroports', 'Defense'),
    ('transport aerien', 'Defense'),
    ('energie', 'Energie'), ('electrique', 'Energie'), ('electricite', 'Energie'), ('eolien', 'Energie'),
    ('solaire', 'Energie'), ('biogaz', 'Energie'), ('biomethane', 'Energie'),
    ('bienergie', 'Energie'), ('uranium', 'Energie'), ('gaz industriels', 'Energie'),
    ('lng technology', 'Energie'), ('membranes methaniers', 'Energie'),
    ('data energie', 'Energie'), ('data souterrain', 'Energie'), ('option achat gtt', 'Energie'),
    ('assurance', 'Financier'), ('banque', 'Financier'), ('paiements', 'Financier'),
    ('arbitrage', 'Financier'), ('holding', 'Financier'), ('avantages salariaux', 'Financier'),
    ('immobilier', 'Immobilier'), ('centres commerciaux', 'Immobilier'),
    ('entrepots logistiques', 'Immobilier'), ('retail parks', 'Immobilier'),
    ('promotion immobiliere', 'Immobilier'), ('tourisme residences', 'Immobilier'),
    ('ehpad', 'Immobilier'),
    ('dechets', 'Environnement'), ('recyclage', 'Environnement'),
    ('environnementaux', 'Environnement'), ('eau traitement', 'Environnement'),
    ('distribution eau', 'Environnement'), ('mesure pollution', 'Environnement'),
    ('eau & dechets', 'Environnement'),
    ('ferroviaire', 'Transport'), ('wagons fret', 'Transport'), ('logistique', 'Transport'),
    ('transit international', 'Transport'), ('ports logistique', 'Transport'),
    ('transport frigorifique', 'Transport'), ('commission fret', 'Transport'),
    ('bateaux', 'Transport'), ('catamarans', 'Transport'), ('propulsion velique', 'Transport'),
    ('camping-car', 'Transport'), ('vehicules loisirs', 'Transport'),
    ('telecom', 'Telecoms'), ('media', 'Telecoms'), ('communication', 'Telecoms'),
    ('publicite', 'Telecoms'), ('evenementiel', 'Telecoms'),
    ('distribution', 'Distribution'), ('ecommerce', 'Distribution'),
    ('agroalimentaire', 'Conso'), ('agriculture tropicale', 'Conso'),
    ('gastronomie', 'Conso'), ('brasseries', 'Conso'), ('restauration collective', 'Conso'),
    ('emballage', 'Conso'), ('electromenager', 'Conso'),
    ('bpo', 'Services'), ('services techniques', 'Services'), ('services collectifs', 'Services'),
    ('services location-entretien', 'Services'), ('tests & analyses', 'Services'),
    ('etudes de marche', 'Services'), ('construction & concessions', 'Services'),
    ('automobile', 'Automobile'), ('equipementier auto', 'Automobile'),
    ('plasturgie auto', 'Automobile'),
    ('hotellerie', 'Hotellerie'),
    ('industrie', 'Industrie'), ('engins manutention', 'Industrie'), ('fours industriels', 'Industrie'),
    ('isolation phonique', 'Industrie'), ('menuiserie', 'Industrie'), ('materiaux', 'Industrie'),
    ('plasturgie', 'Industrie'), ('pneumatiques', 'Industrie'), ('tubes acier', 'Industrie'),
    ('acier', 'Industrie'), ('tuyaux flexibles', 'Industrie'), ('films protection', 'Industrie'),
    ('cables', 'Industrie'), ('piscines acier', 'Industrie'), ('maintenance ascenseurs', 'Industrie'),
    ('materiel brasserie', 'Industrie'), ('chimie', 'Industrie'), ('conglomerat', 'Industrie'),
]
FAIR_PE = {
    'Luxe': 28, 'Semiconducteurs': 32, 'Logiciel': 26, 'Biotech': 24, 'Defense': 20,
    'Energie': 14, 'Financier': 12, 'Immobilier': 16, 'Environnement': 17, 'Transport': 15,
    'Telecoms': 14, 'Distribution': 16, 'Conso': 18, 'Services': 16, 'Automobile': 12,
    'Hotellerie': 18, 'Industrie': 18, 'default': 18,
}
DECOTE = {
    'Luxe': 0.22, 'Semiconducteurs': 0.28, 'Logiciel': 0.24, 'Biotech': 0.30, 'Defense': 0.16,
    'Energie': 0.20, 'Financier': 0.20, 'Immobilier': 0.20, 'Environnement': 0.17, 'Transport': 0.18,
    'Telecoms': 0.16, 'Distribution': 0.17, 'Conso': 0.16, 'Services': 0.16, 'Automobile': 0.20,
    'Hotellerie': 0.18, 'Industrie': 0.17, 'default': 0.18,
}

# Cas ou le libelle de secteur est ambigu (meme libelle, metiers differents)
TICKER_CAT = {'REXEL': 'Distribution'}  # distributeur, pas producteur d'electricite (ELEC)

def classify_sector(sector):
    s = strip_accents(sector or '').lower().strip()
    if s == 'it':
        return 'Logiciel'
    for kw, cat in SECTOR_RULES:
        if kw in s:
            return cat
    return 'default'

def load_sectors_from_data_js():
    """Lit le secteur de chaque ticker directement depuis data.js (source
    de verite : la taxonomie maison, pas celle -- differente -- de Yahoo)."""
    sectors = {}
    try:
        with open('data.js', 'r', encoding='utf-8') as f:
            content = f.read()
        for m in re.finditer(r"ticker:'([A-Z0-9]+)'.*?sector:'([^']*)'", content):
            sectors[m.group(1)] = m.group(2)
    except Exception as e:
        print(f"  WARN lecture secteurs: {e}")
    return sectors

def compute_dcf_and_zones(ticker, sector, price, info):
    """Recalcule le DCF (3 methodes consolidees) et les zones d'achat.
    Repris de zones_dynamiques.py (jamais branche en prod -- audit du
    26/08/2026), avec la classification sectorielle complete ci-dessus."""
    try:
        eps_ttm = info.get('trailingEps') or 0
        eps_fwd = info.get('forwardEps') or (eps_ttm * 1.08 if eps_ttm else 0)
        eps_growth = info.get('earningsGrowth') or info.get('revenueGrowth') or 0.05
        # earningsGrowth de yfinance est un YoY brut, parfois extreme (ex-effet
        # de base sur creux/rebond) -- sans plafond, un exposant sur 3 ans
        # (1+g)^3 peut exploser et inverser dcfb/dcfu (ex: LVMH dcfb>dcfu
        # constate en prod). Plafonne a une croissance soutenable long terme.
        eps_growth_proj = max(min(eps_growth, 0.25), -0.15)
        # yfinance renvoie desormais dividendYield en POURCENT (4.8 = 4,8 %),
        # deja corrige pour l'affichage le 09/09/2026 mais PAS ici : le
        # Gordon multipliait le cours par 4.8 au lieu de 0.048 (dividende
        # x100), ce qui envoyait la methode au plafond 2.2x du cours sur
        # tout l'univers -- cause principale des DCF a ~2x le cours
        # (audit du 04/10/2026). On prefere dividendRate (EUR/action).
        dividend = info.get('dividendYield') or 0
        if dividend > 0.30:
            dividend = dividend / 100
        div_rate = info.get('dividendRate') or 0
        roe = info.get('returnOnEquity') or 0
        book_value = info.get('bookValue') or 0
        pe_ttm = info.get('trailingPE') or (price / eps_ttm if eps_ttm else 0)

        cat = TICKER_CAT.get(ticker) or classify_sector(sector)
        pe_normal = FAIR_PE.get(cat, FAIR_PE['default'])
        decote = DECOTE.get(cat, DECOTE['default'])

        # Fair PE x BPA prevu N+1 -- valeur d'aujourd'hui, pas une projection
        # a 3 ans traitee a tort comme un prix actuel (cause reelle des DCF a
        # 3-5x le cours meme avec la croissance plafonnee -- audit du
        # 07/09/2026). Le PE sectoriel "normal" est deja une hypothese
        # generuse ; l'appliquer a un profit a 3 ans double l'optimisme.
        dcf_pe = pe_normal * eps_fwd if eps_fwd and eps_fwd > 0 else 0

        dcf_gordon = 0
        if dividend and dividend > 0.01 and price > 0:
            div_amount = div_rate if 0 < div_rate < price * 0.25 else price * dividend
            # Gordon-Shapiro = croissance PERPETUELLE du dividende : elle ne
            # peut pas depasser la croissance nominale long terme (~2-3 %).
            # Avant le 04/10/2026 : ke 8 % et g jusqu'a 7 % -> denominateur
            # de 1 %, soit 107x le dividende (TotalEnergies valorisee 380 EUR
            # avant plafond, DCF median 146 EUR pour un cours de 74 EUR).
            ke = 0.09
            g = max(min(eps_growth, 0.03), 0.0)
            dcf_gordon = div_amount * (1 + g) / (ke - g)

        dcf_pb = 0
        if roe and roe > 0.15 and book_value and book_value > 0:
            ke = 0.09
            dcf_pb = book_value * (roe / ke)

        # Garde-fou final : quelle que soit la cause (action decotee pour
        # raison specifique -- ex Air France, Atos, Worldline -- pas un
        # simple retard sectoriel), aucune methode individuelle ne doit
        # pousser le "juste prix" au-dela d'un multiple raisonnable du
        # cours actuel. Un DCF a 4-6x le cours n'est pas un signal
        # d'opportunite fiable, c'est un artefact de calcul -- audit du
        # 07/09/2026 (48/891 combinaisons testees hors [0.25x-2.5x]
        # avant ce garde-fou).
        def _clamp(v, lo=0.4, hi=2.2):
            if not v or v <= 0 or price <= 0: return v
            return max(min(v, price * hi), price * lo)
        dcf_pe = _clamp(dcf_pe)
        dcf_gordon = _clamp(dcf_gordon)
        dcf_pb = _clamp(dcf_pb)

        dcfs = [d for d in [dcf_pe, dcf_gordon, dcf_pb] if d > price * 0.3]
        if not dcfs:
            if pe_ttm and pe_ttm > 0:
                dcfs = [price * (pe_normal / pe_ttm)]
            else:
                return None

        dcfm = round(sum(dcfs) / len(dcfs), 2)
        dcfb = round(dcfm * 0.85, 2)
        dcfu = round(dcfm * 1.20, 2)

        el = round(dcfm * (1 - decote), 2)
        eh = round(dcfm * (1 - decote * 0.4), 2)
        stop = round(el * 0.88, 2)
        o1 = round(dcfm * 1.05, 2)
        o2 = round(dcfm * 1.20, 2)

        if not (el < eh and o1 > el):
            return None

        return {'dcfb': dcfb, 'dcfm': dcfm, 'dcfu': dcfu,
                'el': el, 'eh': eh, 'stop': stop, 'o1': o1, 'o2': o2,
                'sector_cat': cat}
    except Exception as e:
        print(f"  DCF SKIP {ticker}: {e}")
        return None

def compute_rsi(closes, period=14):
    """RSI (methode de Wilder), sans dependance pandas. closes = liste de
    cours de cloture du plus ancien au plus recent. Rend None si pas
    assez d'historique -- mieux vaut ne rien afficher qu'afficher un
    chiffre invente. Filtre les trous de cotation (NaN) en amont --
    trouve en verifiant ce meme risque apres l'incident Altman du
    08/09/2026 : un historique Yahoo troue peut sinon produire un NaN
    qui casse tout data.js."""
    closes = [c for c in closes if c is not None and not math.isnan(c)]
    if len(closes) < period + 1:
        return None
    deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    gains = [d if d > 0 else 0.0 for d in deltas]
    losses = [-d if d < 0 else 0.0 for d in deltas]
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    if avg_loss == 0:
        return 100.0 if avg_gain > 0 else 50.0
    rs = avg_gain / avg_loss
    val = round(100 - (100 / (1 + rs)), 1)
    return None if math.isnan(val) else val

def compute_ma(closes, window):
    closes = [c for c in closes if c is not None and not math.isnan(c)]
    if len(closes) < window:
        return None
    val = round(sum(closes[-window:]) / window, 2)
    return None if math.isnan(val) else val

def _get_row(df, *names):
    """Cherche une ligne de bilan/resultat en essayant plusieurs libelles
    possibles -- yfinance a change ses noms de champs selon les versions,
    et je n'ai pas d'acces reseau pour verifier en direct lesquels sont
    actifs. Renvoie la valeur la plus recente (1ere colonne) ou None.
    Traite NaN comme absent -- pandas utilise NaN (pas None) pour une
    case vide, et 'val is not None' laissait passer NaN, qui s'ecrivait
    ensuite tel quel dans data.js (litteral 'nan', invalide en JS) et
    cassait le chargement de tout le site -- incident du 08/09/2026."""
    if df is None or df.empty:
        return None
    for name in names:
        if name in df.index:
            try:
                val = df.loc[name].iloc[0]
                if val is None:
                    continue
                fval = float(val)
                if math.isnan(fval) or math.isinf(fval):
                    continue
                return fval
            except Exception:
                continue
    return None

def _get_row_prev(df, *names):
    """Meme chose mais pour l'annee precedente (2e colonne). Meme
    traitement NaN que _get_row (cf note ci-dessus)."""
    if df is None or df.empty or df.shape[1] < 2:
        return None
    for name in names:
        if name in df.index:
            try:
                val = df.loc[name].iloc[1]
                if val is None:
                    continue
                fval = float(val)
                if math.isnan(fval) or math.isinf(fval):
                    continue
                return fval
            except Exception:
                continue
    return None

def compute_roic(t):
    """ROIC = EBIT x (1 - taux d'impot) / (dette totale + capitaux propres
    - tresorerie), en %. Avant le 04/10/2026, roic etait une simple copie
    du ROE (et n'etait meme pas ecrit dans data.js : les valeurs affichees,
    ex. 1.06 pour TotalEnergies, etaient figees depuis la creation des
    fiches). Renvoie None si une donnee manque -- jamais de chiffre invente."""
    try:
        fin, bs = t.financials, t.balance_sheet
        ebit = _get_row(fin, 'EBIT', 'Operating Income')
        pretax = _get_row(fin, 'Pretax Income')
        tax = _get_row(fin, 'Tax Provision')
        debt = _get_row(bs, 'Total Debt') or 0
        equity = _get_row(bs, 'Stockholders Equity', 'Common Stock Equity')
        cash = _get_row(bs, 'Cash And Cash Equivalents',
                        'Cash Cash Equivalents And Short Term Investments') or 0
        if ebit is None or equity is None:
            return None
        rate = tax / pretax if (tax is not None and pretax and pretax > 0) else 0.25
        rate = min(max(rate, 0.0), 0.40)
        invested = debt + equity - cash
        if invested <= 0:
            return None
        v = round(ebit * (1 - rate) / invested * 100, 1)
        return v if -100 < v < 200 else None
    except Exception as e:
        print(f"  ROIC SKIP: {e}")
        return None

# ═══ FILTRE QUALITE QARP (regle ecrite validee par l'utilisatrice le 04/10/2026) ═══
# Tous obligatoires (hors banques/assurances, voir plus bas) :
#   1. ROIC hors ecart d'acquisition, MEDIANE sur les annees dispo (4 max) >= 15 %
#   2. ROIC avec ecart d'acquisition (mediane)                              >= 12 %
#   3. Conversion cash-flow libre / resultat net (cumul 4 ans)              >= 80 %
#   4. Dette nette / EBITDA (derniere annee)                                <= 2,5
#   5. Resultat d'exploitation positif chaque annee
#   6. Croissance du chiffre d'affaires (taux annuel moyen, 4 ans)         >= 3 %
#      (ajout 04/10 : ecarte les societes rentables mais sans croissance)
# Alarme (revue de these, pas un filtre) : Piotroski <= 4.
# Donnee manquante = filtre NON valide (jamais de qualite supposee).
Q_ROIC_X, Q_ROIC, Q_FCF, Q_ND, Q_GROWTH = 15.0, 12.0, 80.0, 2.5, 3.0

# Exceptions ECRITES, decidees par l'utilisatrice (pas de derogation au cas par cas) :
# la valeur reste eligible a l'argent neuf meme si elle echoue au filtre.
EXCEPTIONS = {'AI': 'pilier long terme (prime de fidelite)'}

def _row_series(df, *names):
    """Valeurs d'une ligne pour toutes les annees (plus recente d'abord),
    NaN filtres. Liste vide si la ligne est absente."""
    if df is None or getattr(df, 'empty', True):
        return []
    for name in names:
        if name in df.index:
            out = []
            for v in df.loc[name].tolist():
                try:
                    f = float(v)
                    out.append(None if (math.isnan(f) or math.isinf(f)) else f)
                except Exception:
                    out.append(None)
            return out
    return []

def _median(vals):
    v = sorted(x for x in vals if x is not None)
    if not v: return None
    n = len(v)
    return v[n//2] if n % 2 else (v[n//2-1] + v[n//2]) / 2

def compute_quality(t, sector_cat):
    """Calcule les 5 criteres et renvoie un dict :
    roic (mediane avec ecart d'acquisition), roicx (sans), fcfc (%),
    nde (dette nette/EBITDA), qok (bool), qwhy (criteres en echec)."""
    res = {'roic': None, 'roicx': None, 'fcfc': None, 'nde': None, 'cagr': None,
           'nig': None, 'qok': False, 'qwhy': ''}
    if sector_cat == 'Financier':
        # ROIC / EBITDA n'ont pas de sens pour une banque ou un assureur :
        # grille dediee a construire (ROE + solvabilite). En attendant, hors filtre.
        res['qwhy'] = 'financiere (grille dediee a venir)'
        return res
    try:
        fin, bs, cf = t.financials, t.balance_sheet, t.cashflow
        ebit   = _row_series(fin, 'EBIT', 'Operating Income')
        opinc  = _row_series(fin, 'Operating Income', 'EBIT')
        pretax = _row_series(fin, 'Pretax Income')
        tax    = _row_series(fin, 'Tax Provision')
        ni     = _row_series(fin, 'Net Income', 'Net Income Common Stockholders')
        ebitda = _row_series(fin, 'EBITDA', 'Normalized EBITDA')
        debt   = _row_series(bs, 'Total Debt')
        eq     = _row_series(bs, 'Stockholders Equity', 'Common Stock Equity')
        cash   = _row_series(bs, 'Cash And Cash Equivalents',
                             'Cash Cash Equivalents And Short Term Investments')
        gw     = _row_series(bs, 'Goodwill', 'Goodwill And Other Intangible Assets')
        rev    = _row_series(fin, 'Total Revenue', 'Operating Revenue')
        fcf    = _row_series(cf, 'Free Cash Flow')
        if not fcf:
            ocf = _row_series(cf, 'Operating Cash Flow')
            capex = _row_series(cf, 'Capital Expenditure')
            fcf = [(o + c) if (o is not None and c is not None) else None
                   for o, c in zip(ocf, capex)]
        # Historique affiche dans la fiche (05/10/2026) : CA, resultat net,
        # cash-flow libre en millions, du plus recent au plus ancien.
        try:
            fmt_ = lambda lst: '|'.join('' if x is None else f"{x / 1e6:.0f}" for x in lst[:4])
            res['yrs'] = '|'.join(str(c.year) for c in list(fin.columns)[:4])
            res['revh'], res['nih'], res['fcfh'] = fmt_(rev), fmt_(ni), fmt_(fcf)
        except Exception:
            pass
        g = lambda lst, i: lst[i] if i < len(lst) else None
        n = min(len(ebit), len(eq)) if ebit and eq else 0
        roics, roicxs = [], []
        for i in range(min(n, 4)):
            e, q = g(ebit, i), g(eq, i)
            if e is None or q is None: continue
            pt, tx = g(pretax, i), g(tax, i)
            rate = tx / pt if (tx is not None and pt and pt > 0) else 0.25
            rate = min(max(rate, 0.0), 0.40)
            nopat = e * (1 - rate)
            ic = (g(debt, i) or 0) + q - (g(cash, i) or 0)
            if ic > 0:
                roics.append(nopat / ic * 100)
            icx = ic - (g(gw, i) or 0)
            if icx > 0:
                roicxs.append(nopat / icx * 100)
        res['roic'] = round(_median(roics), 1) if roics else None
        res['roicx'] = round(_median(roicxs), 1) if roicxs else None
        # Conversion cash : cumul sur les annees communes (plus robuste
        # qu'une mediane de ratios annuels quand une annee est atypique)
        pairs = [(f, r) for f, r in zip(fcf[:4], ni[:4]) if f is not None and r is not None]
        sni = sum(r for _, r in pairs)
        if pairs and sni > 0:
            res['fcfc'] = round(sum(f for f, _ in pairs) / sni * 100, 0)
        e0 = g(ebitda, 0)
        if e0 and e0 > 0:
            res['nde'] = round(((g(debt, 0) or 0) - (g(cash, 0) or 0)) / e0, 2)
        revs = [x for x in rev[:4] if x is not None]
        nis = [x for x in ni[:4] if x is not None]
        if len(nis) >= 2 and nis[-1] > 0 and nis[0] > 0:
            res['nig'] = round(((nis[0] / nis[-1]) ** (1 / (len(nis) - 1)) - 1) * 100, 1)
        # Regularite (05/10/2026, methode Fournier) : annees de hausse du CA
        # et du benefice sur les 4 exercices publies (3 comparaisons).
        if len(revs) >= 3:
            res['regn'] = len(revs) - 1
            res['regu'] = sum(1 for i in range(len(revs) - 1) if revs[i] > revs[i + 1])
        if len(nis) >= 3:
            res['nregu'] = sum(1 for i in range(len(nis) - 1) if nis[i] > nis[i + 1])
        if len(revs) >= 2 and revs[-1] > 0 and revs[0] > 0:
            res['cagr'] = round(((revs[0] / revs[-1]) ** (1 / (len(revs) - 1)) - 1) * 100, 1)
        ops = [x for x in opinc[:4] if x is not None]
        op_ok = bool(ops) and all(x > 0 for x in ops)
        why = []
        if res['roicx'] is None or res['roicx'] < Q_ROIC_X: why.append(f"ROIC hors EA {res['roicx']}")
        if res['roic'] is None or res['roic'] < Q_ROIC:     why.append(f"ROIC {res['roic']}")
        if res['fcfc'] is None or res['fcfc'] < Q_FCF:      why.append(f"cash {res['fcfc']}%")
        if res['nde'] is None or res['nde'] > Q_ND:         why.append(f"dette/EBITDA {res['nde']}")
        if not op_ok:                                       why.append('perte exploitation')
        if res['cagr'] is None or res['cagr'] < Q_GROWTH:   why.append(f"croissance CA {res['cagr']}%")
        res['qok'] = not why
        res['qwhy'] = ', '.join(why)
    except Exception as e:
        res['qwhy'] = f'donnees indisponibles ({e})'[:80]
    return res

# ═══ ETAPE 2 : JUSTE PRIX AJUSTE A LA QUALITE (valeurs qui passent le filtre) ═══
# Le PER sectoriel unique ne payait jamais la qualite (Hermes, ASML, L'Oreal
# toujours "cheres"). Modele a 2 etapes, standard en analyse :
#   - 10 ans de croissance partant de g1 = moyenne(croissance CA 4 ans,
#     croissance benefice 4 ans), bornee a [0 ; 12 %], qui ralentit
#     lineairement jusqu'a 2,5 % ;
#   - puis croissance perpetuelle 2,5 % ;
#   - la part du benefice distribuable = 1 - croissance / ROIC hors ecart
#     d'acquisition (borne a 60 % : la croissance organique se finance avec
#     du capital tangible, pas avec du goodwill) (une societe
#     a ROIC eleve finance sa croissance avec peu de capital : c'est
#     exactement la prime de qualite) ;
#   - actualisation 8,5 % (cout des fonds propres ; teste 8 / 8,5 / 9 % le
#     04/10 : 9 % jugeait TOUTES les valeurs de qualite surevaluees,
#     8 % trop genereux).
# Hypotheses volontairement prudentes : c'est une valeur de reference, pas
# une prediction. A 8,5 %, payer ce prix rapporte ~8,5 %/an si les hypotheses
# se realisent.
QV_R, QV_G2, QV_YEARS, QV_GMAX, QV_ROIC_CAP = 0.085, 0.025, 10, 0.12, 60.0

def qarp_value(eps_fwd, eps_ttm, cagr, nig, roic_pct, g1_override=None):
    if roic_pct is None:
        return None
    if g1_override is not None:
        g1 = g1_override
    else:
        gs = [x for x in (cagr, nig) if x is not None]
        if not gs:
            return None
        g1 = max(0.0, min(sum(gs) / len(gs) / 100, QV_GMAX))
    # Benefice de depart : le BPA prevu par les analystes, plafonne a +10 %
    # au-dessus de ce que donne le BPA publie x (1+g1). Teste le 04/10 : le
    # BPA prevu brut de Yahoo gonflait certaines valeurs de 50 a 100 %
    # (Thales, Ipsen, FDJ) -- les previsions sont structurellement optimistes.
    if eps_fwd and eps_fwd > 0 and eps_ttm and eps_ttm > 0:
        eps = min(eps_fwd, eps_ttm * (1 + g1) * 1.10)
    elif eps_ttm and eps_ttm > 0:
        eps = eps_ttm * (1 + g1)
    else:
        return None
    roic = max(min(roic_pct, QV_ROIC_CAP) / 100, 0.10)
    pay2 = max(0.2, 1 - QV_G2 / roic)
    v, e = 0.0, eps
    for t_ in range(1, QV_YEARS + 1):
        # croissance qui ralentit lineairement de g1 vers 2,5 % en 10 ans
        # (une croissance forte constante 10 ans surevaluait Thales, GTT...)
        g = g1 + (QV_G2 - g1) * (t_ - 1) / (QV_YEARS - 1)
        e *= (1 + g)
        pay = max(0.2, 1 - g / roic)
        v += e * pay / (1 + QV_R) ** t_
    tv = e * (1 + QV_G2) * pay2 / (QV_R - QV_G2)
    v += tv / (1 + QV_R) ** QV_YEARS
    return v

def normalized_eps(t, info):
    """BPA publie, remplace par le BPA median 4 ans s'il est plus eleve.
    05/10/2026, cas Universal Music : BPA 12 mois ecrase par des elements
    exceptionnels (PER 78 contre 13 attendu) -> valeur estimee a 4 EUR pour un
    cours de 14 EUR. Garde-fou : le BPA median n'est retenu que s'il reste
    sous 1,2 x le BPA prevu (evite un nombre d'actions mal compte par Yahoo,
    ex. societes a 2 categories d'actions)."""
    ttm, fwd = info.get('trailingEps'), info.get('forwardEps')
    try:
        ni = _row_series(t.financials, 'Net Income', 'Net Income Common Stockholders')
        sh = info.get('sharesOutstanding')
        vals = sorted(x for x in ni[:4] if x is not None)
        if not vals or not sh or not fwd or fwd <= 0:
            return ttm
        n = len(vals)
        med = (vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2) / sh
        if med > 0 and med <= fwd * 1.2 and (not ttm or med > ttm):
            return med
    except Exception as e:
        print(f"  EPS normalise SKIP: {e}")
    return ttm

def implied_growth(eps_fwd, eps_ttm, roic_pct, price):
    """Croissance de depart (%/an, ralentissant vers 2,5 % sur 10 ans) que
    le cours ACTUEL suppose, avec le meme modele et le meme taux de 8,5 %.
    C'est la question utile : 'est-ce realiste ?' plutot qu'une zone d'achat
    qui depend d'hypotheses cachees (methode 'reverse DCF', 05/10/2026)."""
    if not price or price <= 0 or roic_pct is None:
        return None
    f = lambda g: qarp_value(eps_fwd, eps_ttm, None, None, roic_pct, g1_override=g)
    lo, hi = -0.05, 0.30
    vlo, vhi = f(lo), f(hi)
    if vlo is None or vhi is None:
        return None
    if price <= vlo:
        return -5.0
    if price >= vhi:
        return 30.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if f(mid) < price:
            lo = mid
        else:
            hi = mid
    return round((lo + hi) / 2 * 100, 1)

def zones_from_value(v, price, cat):
    """Memes regles de zones que compute_dcf_and_zones, a partir d'une valeur."""
    v = max(min(v, price * 3.0), price * 0.3)
    decote = DECOTE.get(cat, DECOTE['default'])
    dcfm = round(v, 2)
    el = round(dcfm * (1 - decote), 2)
    return {'dcfm': dcfm, 'dcfb': round(dcfm * 0.85, 2), 'dcfu': round(dcfm * 1.20, 2),
            'el': el, 'eh': round(dcfm * (1 - decote * 0.4), 2), 'stop': round(el * 0.88, 2),
            'o1': round(dcfm * 1.05, 2), 'o2': round(dcfm * 1.20, 2)}

# ═══ ETAPE 4 : indicateurs affiches autrefois figes (crees a la main) ═══
def compute_extras(t, info):
    """Recalcule les indicateurs de la fiche qui n'etaient jamais mis a jour.
    None si incalculable : la fiche affiche alors un tiret, pas un faux chiffre."""
    x = {}
    def sv(v, mult=1, dec=1):
        try:
            f = float(v) * mult
            return None if (math.isnan(f) or math.isinf(f)) else round(f, dec)
        except Exception:
            return None
    x['ps'] = sv(info.get('priceToSalesTrailing12Months'), 1, 2)
    x['roa'] = sv(info.get('returnOnAssets'), 100)
    x['de'] = sv(info.get('debtToEquity'), 0.01, 2)
    x['cr'] = sv(info.get('currentRatio'), 1, 2)
    try:
        fin, cf = t.financials, t.cashflow
        ebit = _get_row(fin, 'EBIT', 'Operating Income')
        intr = _get_row(fin, 'Interest Expense', 'Interest Expense Non Operating')
        rev = _get_row(fin, 'Total Revenue')
        capex = _get_row(cf, 'Capital Expenditure')
        da = _get_row(cf, 'Depreciation And Amortization', 'Depreciation Amortization Depletion')
        fcf = _get_row(cf, 'Free Cash Flow')
        mcap = info.get('marketCap')
        ev = info.get('enterpriseValue')
        if ebit and intr and abs(intr) > 0:
            x['ic'] = round(ebit / abs(intr), 1)
        if fcf is not None and mcap:
            x['fcf'] = round(fcf / mcap * 100, 1)
        if capex is not None and rev:
            x['capr'] = round(abs(capex) / rev * 100, 1)
        if capex is not None and da:
            x['capda'] = round(abs(capex) / abs(da), 2)
        if ev and ebit and ebit > 0:
            x['ev_ebit'] = round(ev / ebit, 1)
    except Exception as e:
        print(f"  EXTRAS SKIP: {e}")
    for k in ('ic', 'fcf', 'capr', 'capda', 'ev_ebit'):
        x.setdefault(k, None)
    return x

def compute_piotroski(t, info):
    """F-Score de Piotroski (0-9). Echoue proprement (None) si le bilan
    n'a pas assez d'historique -- mieux vaut ne rien afficher qu'un faux
    chiffre. A verifier sur le premier run reel (cf note plus haut)."""
    try:
        bs = t.balance_sheet
        inc = t.financials
        cf = t.cashflow
        if bs is None or bs.empty or inc is None or inc.empty:
            return None

        total_assets = _get_row(bs, 'Total Assets')
        total_assets_prev = _get_row_prev(bs, 'Total Assets')
        net_income = _get_row(inc, 'Net Income', 'Net Income Common Stockholders')
        ocf = _get_row(cf, 'Operating Cash Flow', 'Total Cash From Operating Activities', 'Cash Flow From Continuing Operating Activities')
        ltd = _get_row(bs, 'Long Term Debt', 'Long Term Debt And Capital Lease Obligation')
        ltd_prev = _get_row_prev(bs, 'Long Term Debt', 'Long Term Debt And Capital Lease Obligation')
        cur_assets = _get_row(bs, 'Total Current Assets', 'Current Assets')
        cur_liab = _get_row(bs, 'Total Current Liabilities', 'Current Liabilities')
        cur_assets_prev = _get_row_prev(bs, 'Total Current Assets', 'Current Assets')
        cur_liab_prev = _get_row_prev(bs, 'Total Current Liabilities', 'Current Liabilities')
        shares = _get_row(bs, 'Share Issued', 'Ordinary Shares Number')
        shares_prev = _get_row_prev(bs, 'Share Issued', 'Ordinary Shares Number')
        gross_profit = _get_row(inc, 'Gross Profit')
        gross_profit_prev = _get_row_prev(inc, 'Gross Profit')
        revenue = _get_row(inc, 'Total Revenue')
        revenue_prev = _get_row_prev(inc, 'Total Revenue')
        net_income_prev = _get_row_prev(inc, 'Net Income', 'Net Income Common Stockholders')

        if total_assets is None or net_income is None or total_assets_prev is None:
            return None

        roa = net_income / total_assets if total_assets else None
        roa_prev = (net_income_prev / total_assets_prev) if (net_income_prev is not None and total_assets_prev) else None

        score = 0
        # Rentabilite (4 points)
        if roa is not None and roa > 0: score += 1
        if ocf is not None and ocf > 0: score += 1
        if roa is not None and roa_prev is not None and roa > roa_prev: score += 1
        if ocf is not None and net_income is not None and ocf > net_income: score += 1
        # Levier / liquidite (3 points)
        if ltd is not None and ltd_prev is not None and ltd <= ltd_prev: score += 1
        if cur_assets and cur_liab and cur_assets_prev and cur_liab_prev:
            if (cur_assets/cur_liab) > (cur_assets_prev/cur_liab_prev): score += 1
        if shares is not None and shares_prev is not None and shares <= shares_prev * 1.01: score += 1
        # Efficacite operationnelle (2 points)
        if gross_profit and revenue and gross_profit_prev and revenue_prev:
            if (gross_profit/revenue) > (gross_profit_prev/revenue_prev): score += 1
        if revenue and revenue_prev and total_assets_prev:
            if (revenue/total_assets) > (revenue_prev/total_assets_prev): score += 1
        return score
    except Exception as e:
        print(f"  Piotroski SKIP: {e}")
        return None

def compute_altman_z(t, info, price, shares_out):
    """Z-Score d'Altman. Meme reserve que Piotroski sur les noms de
    champs yfinance. Formule standard (entreprises industrielles cotees)."""
    try:
        bs = t.balance_sheet
        inc = t.financials
        if bs is None or bs.empty or inc is None or inc.empty:
            return None

        total_assets = _get_row(bs, 'Total Assets')
        cur_assets = _get_row(bs, 'Total Current Assets', 'Current Assets')
        cur_liab = _get_row(bs, 'Total Current Liabilities', 'Current Liabilities')
        total_liab = _get_row(bs, 'Total Liab', 'Total Liabilities Net Minority Interest')
        retained_earnings = _get_row(bs, 'Retained Earnings')
        ebit = _get_row(inc, 'EBIT', 'Operating Income')
        revenue = _get_row(inc, 'Total Revenue')

        if not total_assets or not total_liab:
            return None

        working_capital = (cur_assets - cur_liab) if (cur_assets is not None and cur_liab is not None) else 0
        market_cap = (price * shares_out) if (price and shares_out) else info.get('marketCap')

        A = working_capital / total_assets
        B = (retained_earnings or 0) / total_assets
        C = (ebit or 0) / total_assets
        D = (market_cap / total_liab) if (market_cap and total_liab) else 0
        E = (revenue or 0) / total_assets

        z = 1.2*A + 1.4*B + 3.3*C + 0.6*D + 1.0*E
        if math.isnan(z) or math.isinf(z):
            return None
        return round(z, 2)
    except Exception as e:
        print(f"  Altman SKIP: {e}")
        return None

def safe(v, d=0, dec=2):
    try:
        f = float(v)
        if math.isnan(f) or math.isinf(f): return d
        return round(f, dec)
    except: return d

def pct(v, d=0): return safe(v * 100 if v else 0, d, 1)


# ═══ 07/10/2026 : multiples historiques et 2e methode de valeur ═══
def hist_multiples(t, info):
    """PER, cours/cash libre et VE/EBITDA a chaque cloture annuelle publiee
    (jusqu'a 4 ans), puis leur mediane. Permet de dire 'PER 17 contre 24 en
    moyenne pour cette entreprise' au lieu d'un bareme general."""
    out = {'pe_h': None, 'pfcf_h': None, 'eveb_h': None, 'hn': 0}
    try:
        fin, bs, cf = t.financials, t.balance_sheet, t.cashflow
        h = t.history(period='5y', interval='1wk')
        if fin is None or fin.empty or h is None or h.empty:
            return out
        closes = h['Close']
        try:
            closes.index = closes.index.tz_localize(None)
        except Exception:
            pass
        # comptes dans une autre devise que le cours (ex. TotalEnergies en USD) :
        # on convertit le cours dans la devise des comptes a chaque date
        fc_, c_ = info.get('financialCurrency'), info.get('currency')
        if fc_ and c_ and fc_ != c_:
            try:
                fx = yf.Ticker(f'{c_}{fc_}=X').history(period='5y', interval='1wk')['Close']
                try:
                    fx.index = fx.index.tz_localize(None)
                except Exception:
                    pass
                fx = fx.reindex(closes.index, method='nearest')
                if fx.isna().all():
                    raise ValueError('fx vide')
                closes = closes * fx
            except Exception:
                out['hcur'] = 1
                return out
        ni = _row_series(fin, 'Net Income', 'Net Income Common Stockholders')
        ebitda = _row_series(fin, 'EBITDA', 'Normalized EBITDA')
        fcf = _row_series(cf, 'Free Cash Flow')
        sh = _row_series(bs, 'Ordinary Shares Number', 'Share Issued')
        debt = _row_series(bs, 'Total Debt')
        cash = _row_series(bs, 'Cash And Cash Equivalents', 'Cash Cash Equivalents And Short Term Investments')
        g = lambda lst, i: lst[i] if i < len(lst) else None
        pes, pfs, evs = [], [], []
        for i, col in enumerate(list(fin.columns)[:4]):
            try:
                dt = col.to_pydatetime().replace(tzinfo=None) if hasattr(col, 'to_pydatetime') else col
                px_ = closes[closes.index <= dt]
                if px_.empty:
                    continue
                px = float(px_.iloc[-1])
            except Exception:
                continue
            n_ = g(sh, i) or info.get('sharesOutstanding')
            if not n_:
                continue
            mcap = px * n_
            if g(ni, i) and g(ni, i) > 0:
                pes.append(mcap / g(ni, i))
            if g(fcf, i) and g(fcf, i) > 0:
                pfs.append(mcap / g(fcf, i))
            if g(ebitda, i) and g(ebitda, i) > 0:
                evs.append((mcap + (g(debt, i) or 0) - (g(cash, i) or 0)) / g(ebitda, i))
        med = lambda v: round(sorted(v)[len(v) // 2] if len(v) % 2 else (sorted(v)[len(v) // 2 - 1] + sorted(v)[len(v) // 2]) / 2, 1) if v else None
        ok = lambda v: [x for x in v if 0 < x < 300]
        out.update({'pe_h': med(ok(pes)), 'pfcf_h': med(ok(pfs)), 'eveb_h': med(ok(evs)), 'hn': len(pes)})
    except Exception as e:
        print(f"  HIST SKIP: {e}")
    return out

def mult_value(eps_fwd, eps_ttm, g_pct, pe_exit, payout, years=5, r=QV_R):
    """Methode 2 (multiples) : benefice qui croit de g pendant 5 ans,
    dividendes encaisses, puis revente au PER habituel de l'entreprise
    (borne 10-30), le tout actualise a 8,5 %."""
    if not pe_exit or g_pct is None:
        return None
    base = None
    g1 = max(0.0, min(g_pct, QV_GMAX * 100)) / 100
    if eps_fwd and eps_fwd > 0 and eps_ttm and eps_ttm > 0:
        base = min(eps_fwd, eps_ttm * (1 + g1) * 1.10)
    elif eps_ttm and eps_ttm > 0:
        base = eps_ttm * (1 + g1)
    if not base:
        return None
    pay = max(0.0, min(payout or 0.0, 0.9))
    v, e = 0.0, base
    for t_ in range(1, years + 1):
        if t_ > 1:
            e *= (1 + g1)
        v += e * pay / (1 + r) ** t_
    v += e * max(10.0, min(pe_exit, 30.0)) / (1 + r) ** years
    return v

def fetch_one(ticker, yf_sym, sector):
    result = {'ticker': ticker, 'updated': datetime.now(PARIS).isoformat()}
    # Place de cotation (05/10/2026) : toutes les valeurs sont eligibles PEA
    # (siege UE/EEE), mais un courtier n'ouvre pas forcement toutes les bourses.
    _PL = {'PA': 'Paris', 'AS': 'Amsterdam', 'BR': 'Bruxelles', 'LS': 'Lisbonne',
           'DE': 'Francfort', 'MI': 'Milan', 'MC': 'Madrid', 'HE': 'Helsinki',
           'CO': 'Copenhague', 'ST': 'Stockholm', 'OL': 'Oslo'}
    _suf = yf_sym.rsplit('.', 1)[-1] if '.' in yf_sym else ''
    result['place'] = _PL.get(_suf, _suf or '?')
    try:
        t = yf.Ticker(yf_sym)
        info = t.info
        result['price']   = safe(info.get('currentPrice') or info.get('regularMarketPrice'))
        if result['price'] <= 0:
            # Repli : .info peut revenir vide pour un ticker donne sans
            # lever d'erreur (cas reel observe sur EL.PA -- audit du
            # 04/09/2026). history() est un endpoint different, plus
            # fiable pour un simple cours de cloture.
            try:
                h = t.history(period='2d')
                if not h.empty:
                    result['price'] = safe(h['Close'].iloc[-1])
            except Exception:
                pass
        # regularMarketChangePercent est DEJA en % (ex. 0.85) : pct() le
        # multipliait par 100 -> fiches affichant '+84,6 % aujourd'hui' (05/10/2026)
        result['chg']     = safe(info.get('regularMarketChangePercent', 0), 0, 2)
        result['pe']      = safe(info.get('trailingPE') or info.get('forwardPE'))
        result['pe_fwd']  = safe(info.get('forwardPE'))
        result['pb']      = safe(info.get('priceToBook'))
        result['ps']      = safe(info.get('priceToSalesTrailing12Months'))
        result['ev_ebitda']= safe(info.get('enterpriseToEbitda'))
        result['roe']     = pct(info.get('returnOnEquity', 0))
        result['margin']  = pct(info.get('profitMargins', 0))
        result['gm']      = pct(info.get('grossMargins', 0))
        result['debt']    = safe(info.get('debtToEquity', 0) / 100)
        result['revg']    = pct(info.get('revenueGrowth', 0))
        result['epsg']    = pct(info.get('earningsGrowth', 0))
        # dividendYield de yfinance est deja exprime en pourcentage direct
        # (ex: 3.05 pour 3.05%), pas en fraction -- utiliser pct() ici
        # multipliait par 100 une deuxieme fois (LVMH affichait 305%,
        # Credit Agricole 910%, sur pres de la moitie de l'univers --
        # signale par l'utilisatrice le 09/09/2026, trouve via GTT).
        result['yield']   = safe(info.get('dividendYield', 0), 0, 1)
        result['payout']  = pct(info.get('payoutRatio', 0))
        result['beta']    = safe(info.get('beta'))
        result['b52h']    = safe(info.get('fiftyTwoWeekHigh'))
        result['b52l']    = safe(info.get('fiftyTwoWeekLow'))
        result['fcur'] = info.get('financialCurrency') or ''
        result['nb_analysts'] = int(safe(info.get('numberOfAnalystOpinions', 0), 0, 0))
        result['target_price'] = safe(info.get('targetMeanPrice'))
        result['recommendation'] = info.get('recommendationKey', '')
        # DCF + zones d'achat (recalcule desormais a chaque run -- avant
        # ces valeurs etaient figees depuis la creation de la fiche)
        if result['price'] > 0:
            dcf = compute_dcf_and_zones(ticker, sector, result['price'], info)
            if dcf:
                result.update({k: v for k, v in dcf.items() if k != 'sector_cat'})
                print(f"  OK {ticker} [{dcf['sector_cat']}]: PE={result['pe']} ROE={result['roe']}% "
                      f"DCF={dcf['dcfm']}€ Zone={dcf['el']}-{dcf['eh']}€")
            else:
                print(f"  OK {ticker}: PE={result['pe']} ROE={result['roe']}% (DCF non calculable)")
        # RSI + moyennes mobiles (recalcules a chaque run -- avant geles
        # depuis la creation de chaque fiche, cf audit du 08/09/2026)
        try:
            hist = t.history(period='1y')
            if not hist.empty and len(hist) > 15:
                closes = hist['Close'].tolist()
                rsi = compute_rsi(closes)
                mm50 = compute_ma(closes, 50)
                mm200 = compute_ma(closes, 200)
                if rsi is not None: result['rsi'] = rsi
                if mm50 is not None: result['mm50'] = mm50
                if mm200 is not None: result['mm200'] = mm200
        except Exception as e:
            print(f"  RSI/MM SKIP {ticker}: {e}")
        # Piotroski + Altman Z (a verifier sur le premier run reel --
        # voir reserve dans compute_piotroski/compute_altman_z)
        pio = compute_piotroski(t, info)
        shares_out = info.get('sharesOutstanding')
        alt = compute_altman_z(t, info, result['price'], shares_out)
        if pio is not None: result['pio'] = pio
        if alt is not None: result['alt'] = alt
        # Filtre qualite QARP (ROIC median 4 ans, cash, dette)
        cat = TICKER_CAT.get(ticker) or classify_sector(sector)
        result.update(compute_quality(t, cat))
        result.update(hist_multiples(t, info))
        # Croissance officielle (communiques) prioritaire sur Yahoo, y compris
        # pour le critere 'croissance >= 3 %' du filtre qualite
        off = OFFICIAL_GROWTH.get(ticker)
        if off:
            result['gused'], result['gsrc'] = off[0], 'communique ' + off[2]
            parts = [x for x in (result.get('qwhy') or '').split(', ')
                     if x and not x.startswith('croissance CA')]
            if off[0] < Q_GROWTH:
                parts.append(f"croissance officielle {off[0]}%")
            result['qok'] = not parts
            result['qwhy'] = ', '.join(parts)
        else:
            gs = [x for x in (result.get('cagr'), result.get('nig')) if x is not None]
            result['gused'] = round(sum(gs) / len(gs), 1) if gs else None
            result['gsrc'] = 'yahoo (4 ans publies)'
        # Valeur "limite" (05/10/2026, cas Vinci : croissance 2,6 % pour une
        # barre a 3 %) : un SEUL critere en echec -> reste hors filtre, mais
        # signalee "a surveiller" au lieu d'etre ignoree.
        _fails = [x for x in (result.get('qwhy') or '').split(', ') if x]
        # "Limite" = un seul critere manque ET de peu (sinon 34 valeurs
        # etaient signalees au premier essai, dont des reculs de -11 %).
        def _close(f):
            import re as _re
            m = _re.search(r"(-?\d+(?:\.\d+)?)", f.split(' ')[-1])
            if not m:
                return False
            v = float(m.group(1))
            if f.startswith('croissance'):   return v >= Q_GROWTH - 1.0
            if f.startswith('ROIC hors EA'): return v >= Q_ROIC_X - 2.0
            if f.startswith('ROIC'):         return v >= Q_ROIC - 2.0
            if f.startswith('cash'):         return v >= Q_FCF - 10.0
            if f.startswith('dette'):        return v <= Q_ND + 0.5
            return False
        result['near'] = (not result.get('qok') and len(_fails) == 1 and _close(_fails[0]))
        if ticker in EXCEPTIONS and not result.get('qok'):
            result['qok'] = True
            result['qwhy'] = 'EXCEPTION (' + EXCEPTIONS[ticker] + ') : ' + result.get('qwhy', '')
        if pio is not None and pio <= 4:
            result['alarm'] = f'Piotroski {pio}/9'
        # Etape 2 : juste prix ajuste a la qualite pour les valeurs du filtre
        if (result.get('qok') or result.get('near')) and result.get('price', 0) > 0:
            g_in = off[0] if off else None
            eps_ttm = normalized_eps(t, info)
            v = qarp_value(info.get('forwardEps'), eps_ttm,
                           g_in if off else result.get('cagr'),
                           g_in if off else result.get('nig'),
                           result.get('roicx') or result.get('roic'))
            result['gimp'] = implied_growth(info.get('forwardEps'), eps_ttm,
                                            result.get('roicx') or result.get('roic'),
                                            result['price'])
            if v:
                result.update(zones_from_value(v, result['price'], cat))
                result['vmeth'] = 'qarp'
                # 05/10/2026 : trois scenarios et zone selon l'incertitude
                roic_v = result.get('roicx') or result.get('roic')
                g_c = g_in if off else None
                if g_c is None:
                    gs_ = [x for x in (result.get('cagr'), result.get('nig')) if x is not None]
                    g_c = sum(gs_) / len(gs_) if gs_ else 0.0
                g_c = max(0.0, min(g_c, QV_GMAX * 100))
                vp = qarp_value(info.get('forwardEps'), eps_ttm, 0.0, 0.0, roic_v)
                vo = qarp_value(info.get('forwardEps'), eps_ttm, min(g_c + 3, QV_GMAX * 100),
                                min(g_c + 3, QV_GMAX * 100), roic_v)
                p_ = result['price']
                clamp = lambda x: round(max(min(x, p_ * 3.0), p_ * 0.3), 2)
                unc = UNCERTAINTY.get(ticker)
                lo_m, hi_m = MARGIN.get(unc or 'moyenne', (0.25, 0.15))
                vc = result['dcfm']
                result['unc'] = unc or 'non evaluee'
                result['vpess'] = clamp(vp) if vp else None
                result['vopt'] = clamp(vo) if vo else None
                result['el'] = round(vc * (1 - lo_m), 2)
                result['eh'] = round(vc * (1 - hi_m), 2)
                # seuil de revue = 10 % sous le scenario pessimiste ;
                # alleger au-dessus du scenario optimiste
                if result['vpess']:
                    result['stop'] = round(result['vpess'] * 0.90, 2)
                if result['vopt']:
                    result['o1'] = result['vopt']
                    result['o2'] = round(result['vopt'] * 1.10, 2)
                # methode 2 : multiples historiques (controle croise)
                vm = mult_value(info.get('forwardEps'), eps_ttm, g_c, result.get('pe_h'),
                                info.get('payoutRatio'))
                same_cur = not (info.get('financialCurrency') and info.get('currency')
                                and info.get('financialCurrency') != info.get('currency'))
                result['vmult'] = clamp(vm) if (vm and same_cur) else None
        if 'vmeth' not in result:
            result['vmeth'] = 'per'
        # Etape 3 : "qualite delaissee" = cours >10 % sous la MM200 et RSI < 40
        mm200, rsi_ = result.get('mm200'), result.get('rsi')
        result['neglect'] = bool(mm200 and rsi_ is not None
                                 and result.get('price', 0) < mm200 * 0.9 and rsi_ < 40)
        # Controles de vraisemblance (07/10/2026) : signaler, ne pas corriger
        dq = []
        pe_, pf_ = result.get('pe') or 0, result.get('pe_fwd') or 0
        if pe_ > 150 or (pe_ and pf_ and pe_ / pf_ > 3):
            dq.append('benefice 12 mois anormal (PER %s contre %s attendu)' % (round(pe_, 1), round(pf_, 1)))
        if result.get('hcur'):
            dq.append('comptes publies dans une autre devise que le cours')
        # croissance Yahoo aberrante seulement si c'est elle qui est retenue
        # (si le communique officiel est utilise, l'ecart est normal)
        if not str(result.get('gsrc', '')).startswith('communique') and result.get('cagr') is not None \
                and abs(result['cagr']) > 30:
            dq.append('croissance Yahoo %s %%/an : probablement faussee par une acquisition ou une cession' % result['cagr'])
        # la divergence entre les 2 methodes est affichee dans la fiche, pas bloquante
        result['dq'] = ' · '.join(dq)
        # Couche moat (evaluation qualitative, moat.py)
        mo = MOAT.get(ticker)
        if mo:
            result['mscore'], result['mtype'], result['mthreat'] = mo
        # Garde-fou "couteau qui tombe" (05/10/2026, cas Wavestone) : un cours
        # a plus de 35 % sous son plus haut sur 1 an signale que le marche sait
        # quelque chose que 4 ans de comptes ne montrent pas encore (Wavestone :
        # -55 %, CA en recul et objectifs abaisses fin juillet 2026). Pas
        # d'achat automatique : la these doit etre reverifiee a la main.
        b52h = result.get('b52h') or 0
        result['knife'] = bool(b52h > 0 and result.get('price', 0) < b52h * 0.65)
        # Etape 4 : indicateurs de fiche recalcules
        result.update(compute_extras(t, info))
        # Cotations hors euro (ex. Novo Nordisk en DKK) : tout ce qui est un
        # prix est converti en EUR -- avant, Novo s'affichait en couronnes.
        fx = NON_EUR.get(yf_sym)
        if fx:
            for k in ('price','b52h','b52l','dcfb','dcfm','dcfu','el','eh','stop',
                      'o1','o2','mm50','mm200','target_price'):
                if result.get(k): result[k] = round(result[k] / fx, 2)
        # Objectif de cours = consensus analystes (si >= 3 analystes),
        # au lieu d'un 'tp' saisi a la main a la creation et jamais mis a jour.
        if result.get('nb_analysts', 0) >= 3 and result.get('target_price'):
            result['tp'] = result['target_price']
        # Prochaine publication resultats
        try:
            cal = t.calendar
            if cal is not None and not cal.empty:
                row = cal.iloc[0] if len(cal) > 0 else None
                if row is not None:
                    ed = row.get('Earnings Date') if hasattr(row, 'get') else None
                    if ed: result['next_earnings'] = str(ed)
        except: pass
    except Exception as e:
        print(f"  SKIP {ticker}: {e}")
        result['error'] = str(e)
    return result

def bam_score(price, dcfm, pio, alt, roe, epsg):
    """Score aligne methode BAM (Buffett-Ackman-Munger) : la marge de
    securite DCF et la solidite financiere pesent plus que le momentum
    ou la taille. Bareme continu (pas de paliers fixes) pour eviter les
    gros paquets d'ex-aequo qui gonflaient artificiellement le nombre
    de A -- corrige suite a une question directe du 09/09/2026."""
    score = 0
    if price > 0 and dcfm > 0:
        upside = (dcfm/price - 1) * 100
        score += min(35, max(0, upside * 0.7))
    score += (max(0, min(9, pio)) / 9) * 25
    score += min(15, max(0, alt * 4))
    score += min(15, max(0, roe * 0.7))
    score += min(10, max(0, epsg * 1.0))
    return round(min(100, score))

def compute_all_scores():
    """Relit data.js apres la mise a jour des fondamentaux et recalcule
    le score A/B/C/D de chaque action -- seuils calcules par categorie
    (large/mid/small), pas sur l'univers entier mele, pour comparer
    chaque valeur a ses pairs de taille comparable (cf audit du
    09/09/2026 : comparer Safran a des small caps n'a pas de sens).
    Extraction par blocs simples (meme methode que patch_data_js,
    deja eprouvee) plutot que par regex complexe -- suite a un echec
    silencieux en environnement reel non reproduit localement, on
    reduit le risque en reutilisant ce qui marche deja ailleurs."""
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    entries = []
    tickers_found = list(re.finditer(r"\{ticker:'([A-Z0-9]+)'", content))
    for i, m in enumerate(tickers_found):
        tk = m.group(1)
        start = m.start()
        end = tickers_found[i+1].start() if i+1 < len(tickers_found) else len(content)
        block = content[start:end]
        def g(field, d=0):
            mm = re.search(r'(?<![A-Za-z0-9_])' + field + r":([\d.-]+)", block)
            return float(mm.group(1)) if mm else d
        cap_m = re.search(r"cap:'(\w+)'", block)
        cap = cap_m.group(1) if cap_m else 'mid'
        price = g('price')
        if price <= 0: continue
        cs = bam_score(price, g('dcfm'), g('pio'), g('alt'), g('roe'), g('epsg'))
        entries.append({'ticker': tk, 'cap': cap, 'score': cs, 'price': price,
                        'dcfm': g('dcfm'), 'el': g('el'), 'eh': g('eh'),
                        'stop': g('stop'), 'o1': g('o1'),
                        'qok': bool(re.search(r"(?<![A-Za-z0-9_])qok:true", block)),
                        'knife': bool(re.search(r"(?<![A-Za-z0-9_])knife:true", block)),
                        'mscore': g('mscore', None), 'regu': g('regu', None), 'regn': g('regn', None)})

    by_cap = {}
    for e in entries:
        by_cap.setdefault(e['cap'], []).append(e['score'])
    thresholds = {}
    for cap, vals in by_cap.items():
        vs = sorted(vals, reverse=True)
        n = len(vs)
        if n < 5:
            thresholds[cap] = (75, 60, 45)
            continue
        thresholds[cap] = (vs[max(0,int(n*0.10)-1)], vs[max(0,int(n*0.45)-1)], vs[max(0,int(n*0.80)-1)])

    grades = {}
    for e in entries:
        a, b, cc = thresholds.get(e['cap'], (75, 60, 45))
        if e['score'] >= a: g = 'A'
        elif e['score'] >= b: g = 'B'
        elif e['score'] >= cc: g = 'C'
        else: g = 'D'
        # Regle QARP : une valeur hors filtre qualite ne peut pas etre A ou B
        # (avant : 'Pepite - Conviction forte' affiche sur des valeurs
        # qui echouaient au filtre)
        if not e.get('qok') and g in ('A', 'B'):
            g = 'C'
        # Chute > 35 % sur 1 an : jamais 'Pepite - conviction forte' tant que
        # la cause n'est pas comprise (cas Wavestone, 05/10/2026)
        if e.get('knife') and g in ('A', 'B'):
            g = 'C'
        grades[e['ticker']] = (g, derive_signal(g, e))
    return grades

def derive_signal(grade, e):
    """Conseil derive des chiffres -- regle QARP du 04/10/2026 :
    la QUALITE d'abord (filtre ecrit), le PRIX ensuite.
      avoid = ne passe pas le filtre qualite : pas d'argent neuf
              (ce n'est PAS un ordre de vente d'une ligne detenue)
      buy   = qualite OK ET cours dans la zone d'achat (<= eh)
              ET pas de chute > 35 % sous le plus haut 1 an (sinon watch)
      watch = qualite OK, cours sous la valeur intrinseque, pas encore en zone
      hold  = qualite OK mais cours au-dessus de la valeur intrinseque"""
    p, dcfm, eh = e['price'], e['dcfm'], e['eh']
    if not e.get('qok'):
        return ('avoid', False)
    if p <= 0 or dcfm <= 0 or eh <= 0:
        return ('watch', False)
    if p <= eh:
        # chute > 35 % sur 1 an : en zone, mais these a reverifier avant achat
        # moat insuffisant (< 3) : la decote seule ne suffit pas
        # moat non evalue = pas d'achat automatique (05/10/2026 : Amadeus 'buy'
        # sur une croissance Yahoo gonflee par le rebond post-COVID)
        weak_moat = e.get('mscore') is None or e['mscore'] < MOAT_MIN_BUY
        # croissance reguliere exigee : CA en hausse au moins 2 ans sur 3
        irregular = (e.get('regu') is not None and e.get('regn') and e['regn'] >= 2
                     and e['regu'] < e['regn'] - 1)
        return ('watch', True) if (e.get('knife') or weak_moat or irregular) else ('buy', True)
    if p <= dcfm:
        return ('watch', False)
    return ('hold', False)

def patch_scores(grades):
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    for ticker, (grade, (rec, zone)) in grades.items():
        tp = content.find(f"ticker:'{ticker}'")
        if tp == -1: continue
        np_ = content.find("ticker:'", tp + 1)
        block_end = np_ if np_ > -1 else len(content)
        block = content[tp:block_end]
        nb = re.sub(r"score:'[ABCD]'", f"score:'{grade}'", block, count=1)
        nb = re.sub(r"rec:'\w+'", f"rec:'{rec}'", nb, count=1)
        nb = re.sub(r"zone:(true|false)", f"zone:{'true' if zone else 'false'}", nb, count=1)
        if nb != block:
            block = nb; updated += 1
        content = content[:tp] + block + content[block_end:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Scores A/B/C/D recalcules : {updated} valeurs mises a jour")
    return updated

def _set_field(block, key, js_value):
    """Remplace key:valeur si present, sinon l'insere juste apres price:."""
    pat = r"(?<![A-Za-z0-9_])" + key + r":(?:'[^']*'|true|false|null|[+-]?\d+\.?\d*)"
    if re.search(pat, block):
        return re.sub(pat, lambda m: f"{key}:{js_value}", block, count=1)
    return re.sub(r"(price:[+-]?\d+\.?\d*)", lambda m: f"{m.group(1)},{key}:{js_value}", block, count=1)

def set_quality_fields(block, data):
    if 'qok' not in data:
        return block
    def num(v): return 'null' if v is None else str(v)
    def txt(v): return "'" + str(v or '').replace("'", " ").replace("\\", " ") + "'"
    # roic=null si incalculable (ex. banques) : efface les anciens 999 figes
    block = _set_field(block, 'roic', num(data.get('roic')))
    block = _set_field(block, 'roicx', num(data.get('roicx')))
    block = _set_field(block, 'fcfc', num(data.get('fcfc')))
    block = _set_field(block, 'nde', num(data.get('nde')))
    block = _set_field(block, 'cagr', num(data.get('cagr')))
    block = _set_field(block, 'nig', num(data.get('nig')))
    block = _set_field(block, 'vmeth', txt(data.get('vmeth')))
    block = _set_field(block, 'neglect', 'true' if data.get('neglect') else 'false')
    block = _set_field(block, 'knife', 'true' if data.get('knife') else 'false')
    block = _set_field(block, 'gimp', num(data.get('gimp')))
    block = _set_field(block, 'near', 'true' if data.get('near') else 'false')
    if data.get('mscore') is not None:
        block = _set_field(block, 'mscore', num(data.get('mscore')))
        block = _set_field(block, 'mtype', txt(data.get('mtype')))
        block = _set_field(block, 'mthreat', txt(data.get('mthreat')))
    block = _set_field(block, 'gused', num(data.get('gused')))
    block = _set_field(block, 'place', txt(data.get('place')))
    for k in ('regu', 'regn', 'nregu', 'vpess', 'vopt'):
        block = _set_field(block, k, num(data.get(k)))
    block = _set_field(block, 'unc', txt(data.get('unc')))
    for k in ('pe_h', 'pfcf_h', 'eveb_h', 'hn', 'vmult'):
        block = _set_field(block, k, num(data.get(k)))
    block = _set_field(block, 'dq', txt(data.get('dq')))
    for k in ('yrs', 'revh', 'nih', 'fcfh', 'fcur'):
        if data.get(k):
            block = _set_field(block, k, txt(data.get(k)))
    block = _set_field(block, 'gsrc', txt(data.get('gsrc')))
    for k in ('ps', 'roa', 'de', 'cr', 'ic', 'fcf', 'capr', 'capda', 'ev_ebit'):
        if k in data:
            block = _set_field(block, k, num(data.get(k)))
    block = _set_field(block, 'qok', 'true' if data.get('qok') else 'false')
    block = _set_field(block, 'qwhy', txt(data.get('qwhy')))
    block = _set_field(block, 'alarm', txt(data.get('alarm')))
    return block

def patch_data_js(all_results):
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    FIELDS = {'price':'price','chg':'chg','pe':'pe','pb':'pb','ev_ebitda':'ev_ebitda',
               'roe':'roe','margin':'margin','gm':'gm','debt':'debt','ic':'ic',
               'revg':'revg','epsg':'epsg','yield':'yield','beta':'beta','b52h':'b52h','b52l':'b52l',
               'dcfb':'dcfb','dcfm':'dcfm','dcfu':'dcfu',
               'el':'el','eh':'eh','stop':'stop','o1':'o1','o2':'o2',
               'rsi':'rsi','mm50':'mm50','mm200':'mm200','pio':'pio','alt':'alt',
               'roic':'roic','tp':'tp'}
    for ticker, data in all_results.items():
        if 'error' in data and 'price' not in data: continue
        tp = content.find(f"ticker:'{ticker}'")
        if tp == -1: continue
        np = content.find("ticker:'", tp + 1)
        block_end = np if np > -1 else len(content)
        block = content[tp:block_end]
        for dk, jk in FIELDS.items():
            val = data.get(dk)
            # 0 est une vraie valeur pour la variation du jour (sinon une
            # ancienne valeur aberrante restait affichee, ex. FNAC +57,9 %)
            if val is None or (val == 0 and dk != 'chg'): continue
            # Garde-fou universel : un NaN/Infinity ecrit tel quel (litteral
            # 'nan'/'inf') casse la syntaxe JS de tout data.js et rend le
            # site entier vide -- incident reel du 08/09/2026 (bug Altman
            # Z, mais cette protection couvre n'importe quel champ futur).
            if isinstance(val, float) and (math.isnan(val) or math.isinf(val)):
                print(f"  IGNORE {ticker}.{dk}: valeur invalide ({val})")
                continue
            nb = re.sub(r'(?<![A-Za-z0-9_])' + jk + r':[+-]?\d+\.?\d*', jk + ':' + str(val), block, count=1)
            if nb != block: block = nb; updated += 1
        block = set_quality_fields(block, data)
        content = content[:tp] + block + content[block_end:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nMaj data.js: {updated} champs")
    return updated

def build_earnings_calendar(all_results):
    cal = []
    today = datetime.now(PARIS).date()
    for ticker, data in all_results.items():
        if 'next_earnings' not in data: continue
        try:
            from datetime import date
            d = datetime.fromisoformat(str(data['next_earnings']).split(' ')[0]).date()
            cal.append({'ticker':ticker,'date':str(d),'days_away':(d-today).days,
                        'type':'Resultats','confirmed':True,
                        'target_price':data.get('target_price'),
                        'recommendation':data.get('recommendation',''),
                        'nb_analysts':data.get('nb_analysts',0),
                        'revg':data.get('revg')})
        except: pass
    cal.sort(key=lambda x: x['days_away'])
    print(f"\nEarnings calendar: {len(cal)} dates")
    for e in cal[:10]:
        if e['days_away'] >= 0:
            print(f"  {'🔴' if e['days_away']<=7 else '🟠' if e['days_away']<=30 else '🟡'} {e['ticker']:6s}: {e['date']} (J+{e['days_away']})")
    return cal

def main():
    print(f"VAL.PEA Fundamentals -- {datetime.now(PARIS).strftime('%Y-%m-%d %H:%M')} Paris")
    print('='*50)
    purged = purge_data_js()
    try:
        from template_patches import apply_template_patches
        n_tp = apply_template_patches()
        if n_tp:
            print(f"🛠  {n_tp} correction(s) d'affichage appliquee(s) a data.js")
    except Exception as e:
        print(f"  WARN corrections d'affichage : {e}")
    if purged:
        print(f"🧹 {len(purged)} fiche(s) retiree(s) de data.js : {purged}")
    missing = check_coverage()
    if missing:
        print(f"⚠️ {len(missing)} fiche(s) data.js SANS symbole Yahoo (resteront figees) : {missing}")
    # Taux de change du jour pour les cotations hors euro (repli : tickers.NON_EUR)
    try:
        from tickers import CURRENCY
        rates = {}
        for cur in sorted(set(CURRENCY.values())):
            h = yf.Ticker(f'EUR{cur}=X').history(period='5d')
            if not h.empty:
                r = float(h['Close'].iloc[-1])
                if 1 < r < 50:
                    rates[cur] = r
        for sym, cur in CURRENCY.items():
            if cur in rates:
                NON_EUR[sym] = rates[cur]
        print(f"Taux de change : {rates}")
    except Exception as e:
        print(f"  WARN taux de change (valeurs de secours utilisees) : {e}")
    sectors = load_sectors_from_data_js()
    print(f"Secteurs charges pour {len(sectors)} tickers")
    all_results = {}
    items = list(YF_MAP.items())
    import time
    for i in range(0, len(items), 5):
        for ticker, sym in items[i:i+5]:
            all_results[ticker] = fetch_one(ticker, sym, sectors.get(ticker, ''))
        time.sleep(2)
    updated = patch_data_js(all_results)
    try:
        n_etf = update_etf_prices()
        print(f"ETF : {n_etf} cours mis a jour")
    except Exception as e:
        print(f"  WARN cours ETF : {e}")
    if updated: bump_index_html_version()
    score_status = {'ok': False, 'error': None, 'distribution': None, 'count': 0}
    try:
        grades = compute_all_scores()
        n = patch_scores(grades)
        from collections import Counter
        score_status = {'ok': True, 'error': None,
                         'distribution': dict(Counter(g for g, _ in grades.values())),
                         'signals': dict(Counter(r for _, (r, _z) in grades.values())),
                         'count': n, 'total_computed': len(grades)}
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        print(f"❌ ECHEC recalcul des scores A/B/C/D : {e}")
        print(tb)
        print("(les scores existants restent inchanges pour ce run -- prix et fondamentaux, eux, sont bien a jour)")
        score_status = {'ok': False, 'error': str(e), 'traceback': tb, 'distribution': None, 'count': 0}
    calendar_status = {'ok': False, 'error': None}
    try:
        calendar = build_earnings_calendar(all_results)
        calendar_status = {'ok': True, 'error': None}
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        print(f"❌ ECHEC calendrier de resultats : {e}")
        print(tb)
        calendar = []
        calendar_status = {'ok': False, 'error': str(e), 'traceback': tb}

    # Ecriture du journal isolee dans son propre garde-fou -- si la
    # construction du dict 'data' (tous les tickers) plante pour une
    # raison quelconque, on ecrit quand meme un journal minimal avec le
    # statut du score, plutot que de tout perdre silencieusement comme
    # le 09/09/2026 (1 seul fichier commite au lieu de 3, signe d'un
    # plantage juste apres l'ecriture de data.js).
    try:
        log = {'generated': datetime.now(PARIS).isoformat(), 'updated_count': updated,
               'score_computation': score_status, 'calendar_computation': calendar_status,
               'earnings': calendar,
               'data': {k: {f:v for f,v in d.items() if f!='error'} for k,d in all_results.items()}}
        with open('fundamentals_log.json', 'w', encoding='utf-8') as f:
            json.dump(log, f, ensure_ascii=False, indent=2, default=str)
        print(f"\nfundamentals_log.json sauvegarde (complet)")
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        print(f"❌ ECHEC ecriture fundamentals_log.json (version complete) : {e}")
        print(tb)
        try:
            minimal_log = {'generated': datetime.now(PARIS).isoformat(), 'updated_count': updated,
                            'score_computation': score_status, 'calendar_computation': calendar_status,
                            'write_error': str(e)}
            with open('fundamentals_log.json', 'w', encoding='utf-8') as f:
                json.dump(minimal_log, f, ensure_ascii=False, indent=2, default=str)
            print("fundamentals_log.json sauvegarde (version minimale de secours)")
        except Exception as e2:
            print(f"❌ ECHEC MEME de la version minimale : {e2}")

def update_etf_prices(path='data.js'):
    """05/10/2026 : les ETF n'avaient aucun cours -> le portefeuille comptait
    tes ETF a leur prix d'achat (gain/perte toujours 0) et sous-estimait leur
    poids. On ecrit price:X dans chaque fiche ETF (cotation Paris, .PA)."""
    from tickers import ETF_TICKERS
    with open(path, encoding='utf-8') as f:
        content = f.read()
    start = content.find('const ETF=[')
    if start < 0:
        return 0
    n = 0
    for tk in sorted(ETF_TICKERS):
        try:
            h = yf.Ticker(f'{tk}.PA').history(period='5d')
            if h.empty:
                continue
            px = round(float(h['Close'].iloc[-1]), 3)
            if math.isnan(px) or px <= 0:
                continue
        except Exception as e:
            print(f"  ETF {tk} SKIP: {e}")
            continue
        i = content.find("{ticker:'" + tk + "'", start)
        if i < 0:
            continue
        head = "{ticker:'" + tk + "',"
        j = i + len(head)
        m = re.match(r"price:[+-]?\d+\.?\d*,", content[j:])
        if m:
            content = content[:j] + f"price:{px}," + content[j + m.end():]
        else:
            content = content[:j] + f"price:{px}," + content[j:]
        n += 1
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return n

def bump_index_html_version():
    """Casse le cache CDN de GitHub Pages en changeant l'URL de data.js a
    chaque ecriture reussie -- data.js etait fige depuis des semaines cote
    site public car son URL ne changeait jamais (audit du 08/09/2026)."""
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
            print("index.html : version data.js mise a jour (cache casse)")
    except Exception as e:
        print(f"  WARN bump version: {e}")

if __name__ == '__main__':
    main()
