#!/usr/bin/env python3
"""
update_fundamentals.py - Mise à jour automatique des fondamentaux
Récupère depuis Yahoo Finance v10 : ROE, marge, FCF, dette, PE, croissance
Injecte dans index.html et calcule le score Piotroski F-Score
Lance : manuellement ou via GitHub Actions chaque trimestre
"""

import re, json, os, sys, time
import urllib.request
from datetime import datetime

# ─── MAPPING TICKERS → YAHOO FINANCE ─────────────────────────────────────
YF_MAP = {
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA',
    'ORA':'ORA.PA','VIE':'VIE.PA','RNO':'RNO.PA','SGO':'SGO.PA','CAP':'CAP.PA',
    'DG':'DG.PA','VIV':'VIV.PA','LR':'LR.PA','WLN':'WLN.PA','DSY':'DSY.PA',
    'STM':'STM.PA','EL':'EL.PA','ML':'ML.PA','ENGI':'ENGI.PA','HO':'HO.PA',
    'GTT':'GTT.PA','ELIS':'ELIS.PA','SEB':'SK.PA','ERF':'ERF.PA',
    'ASML':'ASML.AS','NOVO':'NOVO-B.CO','SAP':'SAP.DE',
    'COFA':'COFA.PA','SPIE':'SPIE.PA','ALO':'ALO.PA','EDENRED':'EDEN.PA',
    'BVI':'BVI.PA','FDJ':'FDJ.PA','NRO':'NRO.PA','PERNOD':'RI.PA',
    'GTT':'GTT.PA','TRIGANO':'TRI.PA','BOIRON':'BOI.PA',
    'VIRBAC':'VIRP.PA','SOP':'SOP.PA','IPSEN':'IPN.PA','REXEL':'RXL.PA',
    'SEB2':'SK.PA','LNA':'LNA.PA','ABCA':'ABCA.PA','VK':'VK.PA',
    'FNAC':'FNAC.PA','CNP':'CNP.PA','KLPI':'LI.PA','EIFFAGE':'FGR.PA',
    'NEXANS':'NEX.PA','PLUXEE':'PLX.PA','FORVIA':'FRVIA.PA',
    'DIORCDI':'CDI.PA','HERM2':'RMS.PA',
}

def fetch_yahoo_fundamentals(yf_ticker):
    """Récupère les fondamentaux depuis Yahoo Finance v10"""
    url = (f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{yf_ticker}"
           f"?modules=defaultKeyStatistics,financialData,incomeStatementHistory,"
           f"balanceSheetHistory,cashflowStatementHistory")
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read())
        result = data.get('quoteSummary', {}).get('result', [None])[0]
        if not result:
            return None
        return result
    except Exception as e:
        print(f"    Erreur {yf_ticker}: {e}")
        return None

def safe_pct(val, default=0.0):
    """Convertit une valeur Yahoo (raw ou fmt) en pourcentage"""
    if val is None:
        return default
    if isinstance(val, dict):
        raw = val.get('raw', val.get('fmt', default))
        if isinstance(raw, str):
            raw = raw.replace('%','').replace(',','.')
            try: raw = float(raw)
            except: return default
        return round(float(raw) * 100, 1) if abs(float(raw)) < 10 else round(float(raw), 1)
    try:
        v = float(val)
        return round(v * 100, 1) if abs(v) < 10 else round(v, 1)
    except:
        return default

def safe_val(val, default=0.0, multiplier=1.0):
    """Extrait une valeur numérique brute"""
    if val is None:
        return default
    if isinstance(val, dict):
        raw = val.get('raw', default)
    else:
        raw = val
    try:
        return round(float(raw) * multiplier, 2)
    except:
        return default

def calc_piotroski(fd, ks, inc_hist, bal_hist, cf_hist):
    """
    Calcule le F-Score de Piotroski (0-9)
    9 critères binaires sur rentabilité, levier, efficacité
    """
    score = 0
    signals = []

    try:
        # === RENTABILITÉ (4 points) ===
        # F1: ROA positif
        roa = safe_pct(fd.get('returnOnAssets'), 0) / 100
        if roa > 0:
            score += 1; signals.append("F1✓ ROA>0")
        else:
            signals.append("F1✗ ROA≤0")

        # F2: Cash flow opérationnel positif
        cfo = safe_val(fd.get('operatingCashflow'), 0)
        if cfo > 0:
            score += 1; signals.append("F2✓ CFO>0")
        else:
            signals.append("F2✗ CFO≤0")

        # F3: ROA en hausse (comparaison N vs N-1)
        if inc_hist and len(inc_hist) >= 2:
            ni_n = safe_val(inc_hist[0].get('netIncome'), 0)
            ni_prev = safe_val(inc_hist[1].get('netIncome'), 0)
            ta_n = safe_val(bal_hist[0].get('totalAssets'), 1) if bal_hist else 1
            ta_prev = safe_val(bal_hist[1].get('totalAssets'), 1) if bal_hist and len(bal_hist)>1 else 1
            roa_n = ni_n / ta_n if ta_n else 0
            roa_prev = ni_prev / ta_prev if ta_prev else 0
            if roa_n > roa_prev:
                score += 1; signals.append("F3✓ ROA↑")
            else:
                signals.append("F3✗ ROA↓")

        # F4: Accruals (CFO > ROA*TA)
        ta = safe_val(bal_hist[0].get('totalAssets'), 1) if bal_hist else 1
        if ta > 0 and cfo / ta > roa:
            score += 1; signals.append("F4✓ Accruals")
        else:
            signals.append("F4✗ Accruals")

        # === LEVIER / LIQUIDITÉ (3 points) ===
        # F5: Dette long terme en baisse
        if bal_hist and len(bal_hist) >= 2:
            ltd_n = safe_val(bal_hist[0].get('longTermDebt'), 0)
            ltd_prev = safe_val(bal_hist[1].get('longTermDebt'), 0)
            if ltd_n <= ltd_prev:
                score += 1; signals.append("F5✓ Dette↓")
            else:
                signals.append("F5✗ Dette↑")

        # F6: Ratio courant en hausse
        cr_n = safe_val(fd.get('currentRatio'), 0)
        if cr_n > 1.0:
            score += 1; signals.append("F6✓ CR>1")
        else:
            signals.append("F6✗ CR<1")

        # F7: Pas de dilution (pas d'émission actions)
        if ks:
            shares_n = safe_val(ks.get('sharesOutstanding'), 0)
            shares_prev = safe_val(ks.get('floatShares'), 0)
            if shares_n <= shares_prev * 1.02:  # tolérance 2%
                score += 1; signals.append("F7✓ NoDilution")
            else:
                signals.append("F7✗ Dilution")
        else:
            score += 1; signals.append("F7~ NoDilution(défaut)")

        # === EFFICACITÉ OPÉRATIONNELLE (2 points) ===
        # F8: Marge brute en hausse
        gm_n = safe_pct(fd.get('grossMargins'), 0)
        if inc_hist and len(inc_hist) >= 2:
            rev_n = safe_val(inc_hist[0].get('totalRevenue'), 0)
            rev_prev = safe_val(inc_hist[1].get('totalRevenue'), 0)
            gp_n = safe_val(inc_hist[0].get('grossProfit'), 0)
            gp_prev = safe_val(inc_hist[1].get('grossProfit'), 0)
            gm_n_calc = gp_n / rev_n if rev_n else 0
            gm_prev_calc = gp_prev / rev_prev if rev_prev else 0
            if gm_n_calc >= gm_prev_calc:
                score += 1; signals.append("F8✓ Marge↑")
            else:
                signals.append("F8✗ Marge↓")
        else:
            score += 1; signals.append("F8~ Marge(défaut)")

        # F9: Rotation actifs en hausse
        if inc_hist and bal_hist and len(inc_hist) >= 2 and len(bal_hist) >= 2:
            rev_n = safe_val(inc_hist[0].get('totalRevenue'), 0)
            rev_prev = safe_val(inc_hist[1].get('totalRevenue'), 0)
            ta_n = safe_val(bal_hist[0].get('totalAssets'), 1)
            ta_prev = safe_val(bal_hist[1].get('totalAssets'), 1)
            rot_n = rev_n / ta_n if ta_n else 0
            rot_prev = rev_prev / ta_prev if ta_prev else 0
            if rot_n >= rot_prev:
                score += 1; signals.append("F9✓ Rotation↑")
            else:
                signals.append("F9✗ Rotation↓")
        else:
            score += 1; signals.append("F9~ Rotation(défaut)")

    except Exception as e:
        print(f"    Erreur Piotroski: {e}")

    return score, signals

def get_ca_history(inc_hist):
    """Extrait CA sur 3 ans en Md€"""
    result = {}
    if not inc_hist:
        return result
    for i, period in enumerate(inc_hist[:3]):
        rev = safe_val(period.get('totalRevenue'), 0)
        rev_md = round(rev / 1e9, 1)
        key = ['ca_n', 'ca_n1', 'ca_n2'][i]
        result[key] = rev_md
    return result

def get_margin_history(inc_hist):
    """Extrait marge nette sur 3 ans"""
    result = {}
    if not inc_hist:
        return result
    for i, period in enumerate(inc_hist[:3]):
        rev = safe_val(period.get('totalRevenue'), 0)
        net = safe_val(period.get('netIncome'), 0)
        marg = round(net / rev * 100, 1) if rev else 0
        key = ['marg_n', 'marg_n1', 'marg_n2'][i]
        result[key] = marg
    return result

def extract_fundamentals(data, ticker):
    """Extrait tous les fondamentaux d'une réponse Yahoo"""
    if not data:
        return None

    fd = data.get('financialData', {})
    ks = data.get('defaultKeyStatistics', {})
    inc = data.get('incomeStatementHistory', {}).get('incomeStatementHistory', [])
    bal = data.get('balanceSheetHistory', {}).get('balanceSheetStatements', [])
    cf  = data.get('cashflowStatementHistory', {}).get('cashflowStatements', [])

    # Fondamentaux principaux
    roe    = safe_pct(fd.get('returnOnEquity'))
    roa    = safe_pct(fd.get('returnOnAssets'))
    roic   = safe_pct(fd.get('returnOnCapital')) or round(roe * 0.75, 1)
    margin = safe_pct(fd.get('profitMargins'))
    gm     = safe_pct(fd.get('grossMargins'))
    om     = safe_pct(fd.get('operatingMargins'))
    revg   = safe_pct(fd.get('revenueGrowth'))
    epsg   = safe_pct(fd.get('earningsGrowth'))
    fcf_raw= safe_val(fd.get('freeCashflow'), 0)
    mkt_cap= safe_val(ks.get('marketCap'), 0)
    fcf_yield = round(fcf_raw / mkt_cap * 100, 1) if mkt_cap > 0 and fcf_raw else 0
    debt   = safe_val(fd.get('totalDebt'), 0)
    ebitda = safe_val(fd.get('ebitda'), 0)
    debt_ebitda = round(debt / ebitda, 1) if ebitda > 0 else 0
    cr     = safe_val(fd.get('currentRatio'), 0)
    beta   = safe_val(ks.get('beta'), 1.0)
    pe     = safe_val(fd.get('currentPrice'), 0) / safe_val(fd.get('earningsPerShare'), 1) if safe_val(fd.get('earningsPerShare'), 0) != 0 else safe_val(ks.get('forwardPE'), 0)
    pe     = round(safe_val(ks.get('forwardPE'), 0) or safe_val(ks.get('trailingPE'), 0) or pe, 1)
    pb     = safe_val(ks.get('priceToBook'), 0)
    ev_eb  = safe_val(ks.get('enterpriseToEbitda'), 0)
    div    = safe_pct(fd.get('dividendYield')) or safe_pct(ks.get('dividendYield'))
    mkt_str= f"{round(mkt_cap/1e9, 0):.0f}Md€" if mkt_cap > 1e9 else f"{round(mkt_cap/1e6, 0):.0f}M€"

    # Piotroski
    pio_score, pio_signals = calc_piotroski(fd, ks, inc, bal, cf)

    # Historique CA et marges
    ca_hist = get_ca_history(inc)
    marg_hist = get_margin_history(inc)

    # Tendance marges
    if 'marg_n' in marg_hist and 'marg_n2' in marg_hist:
        m_diff = marg_hist['marg_n'] - marg_hist['marg_n2']
        marg_trend = 'up' if m_diff > 0.5 else 'down' if m_diff < -0.5 else 'flat'
    else:
        marg_trend = 'flat'

    # PE historique 5 ans (estimation)
    pe5y = round(pe * 0.95, 1)  # approximation conservatrice

    result = {
        'roe': roe, 'roa': roa, 'roic': roic,
        'margin': margin, 'gm': gm, 'om': om,
        'revg': revg, 'epsg': epsg,
        'fcf': fcf_yield,
        'debt': debt_ebitda, 'cr': round(cr, 1),
        'beta': round(beta, 1),
        'pe': round(pe, 1), 'pb': round(pb, 1), 'ev_ebitda': round(ev_eb, 1),
        'yield': round(div, 1),
        'pio': pio_score,
        'mkt': mkt_str,
        **ca_hist, **marg_hist,
        'marg_trend': marg_trend, 'pe5y': pe5y,
    }

    return result

def update_stock_in_html(content, ticker, fundamentals):
    """Met à jour les fondamentaux d'une action dans le HTML"""
    if not fundamentals:
        return content, False

    # Trouver le bloc de l'action
    pattern = "{ticker:'" + ticker + "',"
    pos = content.find(pattern)
    if pos < 0:
        return content, False

    # Trouver la fin du bloc
    end = content.find('\n\n{ticker:', pos+1)
    if end < 0:
        end = content.find('\n\n];', pos)
    if end < 0:
        return content, False

    block = content[pos:end]
    new_block = block

    # Mapping champ HTML → valeur calculée
    field_map = {
        'roe': fundamentals.get('roe', 0),
        'roa': fundamentals.get('roa', 0),
        'roic': fundamentals.get('roic', 0),
        'margin': fundamentals.get('margin', 0),
        'gm': fundamentals.get('gm', 0),
        'om': fundamentals.get('om', 0),
        'revg': fundamentals.get('revg', 0),
        'epsg': fundamentals.get('epsg', 0),
        'fcf': fundamentals.get('fcf', 0),
        'debt': fundamentals.get('debt', 0),
        'cr': fundamentals.get('cr', 0),
        'beta': fundamentals.get('beta', 1.0),
        'pe': fundamentals.get('pe', 0),
        'pb': fundamentals.get('pb', 0),
        'ev_ebitda': fundamentals.get('ev_ebitda', 0),
        'yield': fundamentals.get('yield', 0),
        'pio': fundamentals.get('pio', 5),
    }

    # Mettre à jour chaque champ numérique
    modified = False
    for key, val in field_map.items():
        if val and val != 0:
            old_pattern = r'\b' + re.escape(key) + r':([-\d.]+)'
            new_str = key + ':' + str(val)
            new_block_candidate = re.sub(old_pattern, new_str, new_block, count=1)
            if new_block_candidate != new_block:
                new_block = new_block_candidate
                modified = True

    # Mettre à jour les champs de tendance CA/Marge
    for key in ['ca_n', 'ca_n1', 'ca_n2', 'marg_n', 'marg_n1', 'marg_n2', 'pe5y']:
        val = fundamentals.get(key)
        if val is not None:
            old_p = r'\b' + re.escape(key) + r':([-\d.]+)'
            new_s = key + ':' + str(val)
            if re.search(old_p, new_block):
                new_block = re.sub(old_p, new_s, new_block, count=1)
                modified = True
            else:
                # Ajouter avant 'marg_trend' ou avant 'alt:'
                insert_before = 'marg_trend' if 'marg_trend' in new_block else 'alt:'
                if insert_before in new_block:
                    new_block = new_block.replace(insert_before, key + ':' + str(val) + ',' + insert_before, 1)
                    modified = True

    # Mettre à jour marg_trend
    trend = fundamentals.get('marg_trend', 'flat')
    if 'marg_trend:' in new_block:
        new_block = re.sub(r"marg_trend:'[^']*'", "marg_trend:'" + trend + "'", new_block)
        modified = True
    else:
        # Ajouter après ca_n si présent
        if 'ca_n:' in new_block:
            new_block = re.sub(r'(ca_n:[\d.]+)', r'\1,marg_trend:\'' + trend + '\'', new_block)
            modified = True

    if modified:
        content = content[:pos] + new_block + content[end:]

    return content, modified

# ─── MAIN ─────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    html_file = 'index.html'
    if not os.path.exists(html_file):
        print(f"ERREUR: {html_file} introuvable")
        sys.exit(1)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Déterminer quels tickers mettre à jour
    # Par défaut: les 30 plus importantes (top par capitalisation)
    priority = [
        'MC','AI','OR','RMS','SAN','TTE','SAF','SU','AXA','BNP',
        'ACA','GLE','AIR','KER','PUB','ORA','DG','LR','WLN','DSY',
        'HO','GTT','EL','STM','ASML','NOVO','CAP','VIV','ENGI','SEB',
        'ELIS','SPIE','COFA','EDENRED','NRO','BVI','PERNOD',
    ]

    # Option --all pour tout mettre à jour (plus long)
    if '--all' in sys.argv:
        tickers_to_update = [t for t in YF_MAP.keys()]
    elif '--ticker' in sys.argv:
        idx = sys.argv.index('--ticker')
        tickers_to_update = [sys.argv[idx+1]]
    else:
        tickers_to_update = priority

    print(f"Mise à jour fondamentaux — {len(tickers_to_update)} actions")
    print(f"Mode: {'--all' if '--all' in sys.argv else 'prioritaires'}")
    print(f"Début: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("="*50)

    updated = 0
    errors = []
    log = []

    for ticker in tickers_to_update:
        yf = YF_MAP.get(ticker)
        if not yf:
            print(f"  ⚠  {ticker}: pas de mapping Yahoo Finance")
            continue

        print(f"  → {ticker} ({yf})...", end=' ', flush=True)
        data = fetch_yahoo_fundamentals(yf)

        if not data:
            errors.append(ticker)
            print("❌ (pas de données)")
            continue

        fundamentals = extract_fundamentals(data, ticker)
        if not fundamentals:
            errors.append(ticker)
            print("❌ (extraction échouée)")
            continue

        content, modified = update_stock_in_html(content, ticker, fundamentals)

        if modified:
            updated += 1
            pio = fundamentals.get('pio', '?')
            roe = fundamentals.get('roe', 0)
            margin = fundamentals.get('margin', 0)
            trend = fundamentals.get('marg_trend', '?')
            trend_icon = '↑' if trend == 'up' else '↓' if trend == 'down' else '→'
            print(f"✅ ROE:{roe}% Marge:{margin}% FCF:{fundamentals.get('fcf',0)}% Pio:{pio}/9 {trend_icon}")
            log.append(f"{ticker}: ROE={roe}% Marge={margin}% Pio={pio}/9 trend={trend}")
        else:
            print("~ (inchangé)")

        # Pause pour éviter le rate limiting Yahoo
        time.sleep(0.5)

    # Sauvegarder
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # Log de mise à jour
    ts = datetime.now().strftime('%d/%m/%Y %H:%M')
    with open('fundamentals_log.json', 'w') as f:
        json.dump({'date': ts, 'updated': updated, 'errors': errors, 'details': log}, f, indent=2)

    print(f"\n{'='*50}")
    print(f"✅ {updated} actions mises à jour")
    if errors:
        print(f"⚠  {len(errors)} erreurs: {errors[:5]}")
    print(f"Log sauvé: fundamentals_log.json")
    print(f"Fin: {ts}")
