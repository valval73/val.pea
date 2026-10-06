#!/usr/bin/env python3
"""
send_alerts_v2.py — VAL.PEA + Méthode B.A.M (Buffett·Ackman·Munger)
Intégration complète du protocole Finance Optimale de Guillaume Fournier
"""
import re, json, os, sys, smtplib, urllib.request, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ─── CONFIG ───────────────────────────────────────────────────────────────
ANTHROPIC_KEY = os.environ.get('ANTHROPIC_API_KEY', '').strip()
GMAIL_USER    = (os.environ.get('MAIL_USER') or os.environ.get('GMAIL_USER', '')).strip()
GMAIL_PASS    = (os.environ.get('MAIL_PASS') or os.environ.get('GMAIL_PASSWORD', '')).strip()
EMAIL_TO      = (os.environ.get('MAIL_TO') or GMAIL_USER).strip()
TG_TOKEN      = os.environ.get('TELEGRAM_TOKEN', '').strip()
TG_CHAT       = os.environ.get('TELEGRAM_CHAT_ID', '').strip()

print(f"ANTHROPIC: {'OK' if ANTHROPIC_KEY else 'MANQUANT'}")
print(f"MAIL: {'OK' if GMAIL_USER else 'MANQUANT'}")

# ─── MACRO ────────────────────────────────────────────────────────────────
def fetch_macro():
    macro = {}
    tickers = {
        'VIX':   ('^VIX',     'VIX'),
        'OR':    ('GC=F',     'Or $/oz'),
        'TAUX':  ('^TNX',     'Taux US 10 ans'),
        'DXY':   ('DX-Y.NYB', 'Dollar Index'),
        'CAC40': ('^FCHI',    'CAC 40'),
    }
    for key, (yf, label) in tickers.items():
        try:
            url = f"https://query2.finance.yahoo.com/v8/finance/chart/{yf}?interval=1d&range=5d"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=8) as r:
                data = json.loads(r.read())
            meta  = data['chart']['result'][0]['meta']
            price = meta.get('regularMarketPrice', 0)
            prev  = meta.get('previousClose', price)
            chg   = round((price - prev) / prev * 100, 2) if prev else 0
            macro[key] = {'label': label, 'value': round(price, 2), 'chg': chg}
        except:
            macro[key] = {'label': label, 'value': 0, 'chg': 0}
        time.sleep(0.2)
    return macro

def macro_verdict(macro):
    vix  = macro.get('VIX',  {}).get('value', 20)
    taux = macro.get('TAUX', {}).get('value', 4)
    dxy  = macro.get('DXY',  {}).get('value', 104)
    score = 0
    signals = []
    if vix < 15:   score += 1; signals.append(('✅', 'VIX bas — marchés calmes'))
    elif vix < 20: signals.append(('🟡', f'VIX modéré {vix} — légère prudence'))
    elif vix < 30: score -= 1; signals.append(('⚠️', f'VIX élevé {vix} — volatilité'))
    else:          score -= 2; signals.append(('🚨', f'VIX {vix} — stress extrême'))
    if taux < 3.5: score += 1; signals.append(('✅', f'Taux {taux}% — favorable actions'))
    elif taux < 4.5: signals.append(('🟡', f'Taux {taux}% — zone neutre'))
    else:          score -= 1; signals.append(('⚠️', f'Taux {taux}% — freine valorisation'))
    if dxy < 100:  score += 1; signals.append(('✅', 'Dollar faible — bon pour Europe/émergents'))
    elif dxy > 106: score -= 1; signals.append(('⚠️', f'Dollar fort {dxy} — pression devises'))
    if score >= 2:   v = ('✅ FAVORABLE', '#16a34a', '#dcfce7')
    elif score >= 0: v = ('🟡 NEUTRE',    '#d97706', '#fef3c7')
    else:            v = ('⚠️ PRUDENCE',  '#dc2626', '#fee2e2')
    return v, signals

# ─── PARSE STOCKS ─────────────────────────────────────────────────────────
def get_stocks(html_content):
    s_start = html_content.find("const S=[")
    if s_start < 0: return []
    stocks = []
    seen = set()
    for m in re.finditer(r"\{ticker:'([^']+)'(.*?)(?=\n\n\{ticker:|\n\n\];)", html_content[s_start:], re.DOTALL):
        ticker = m.group(1)
        if ticker in seen: continue
        seen.add(ticker)
        block = m.group(0)
        def gn(k, d=0.0):
            mx = re.search(r'\b' + k + r':([-\d.]+)', block)
            return float(mx.group(1)) if mx else d
        def gs(k, d=''):
            mx = re.search(r"\b" + k + r":'([^']*)'", block)
            return mx.group(1) if mx else d
        def gdb(k, d=''):
            mx = re.search(r'\b' + k + r':"([^"]*)"', block)
            return mx.group(1) if mx else d
        def glist(k):
            mx = re.search(r'\b' + k + r':\[([^\]]*)\]', block)
            if not mx: return []
            return re.findall(r"'([^']+)'", mx.group(1))[::2]

        price = gn('price'); dcfm = gn('dcfm'); mm200 = gn('mm200')
        upside = round((dcfm - price) / price * 100, 1) if price and dcfm else 0
        in_zone = price > 0 and dcfm > 0 and price <= dcfm * 0.88 and gs('score') in ['A','B']

        # Moat structuré — compter les sources identifiées
        moat_list = glist('moat')
        moat_score = min(5, len(moat_list))  # 0-5 sources Morningstar

        # Régularité EPS (champ eps_reg si présent, sinon estimation)
        eps_reg = gn('eps_reg', 5.0)  # 0-10, défaut 5

        # Thesis check trimestriel
        thesis_ok = int(gn('thesis_ok', 1))  # 1=OK, 0=dégradée

        s = {
            'ticker': ticker, 'name': gs('name'), 'sector': gs('sector'),
            'score': gs('score'), 'price': price,
            'el': gn('el'), 'eh': gn('eh'), 'stop': gn('stop'), 'o1': gn('o1'),
            'dcfb': gn('dcfb'), 'dcfm': dcfm, 'dcfu': gn('dcfu'),
            'roe': gn('roe'), 'margin': gn('margin'), 'fcf': gn('fcf'),
            'debt': gn('debt'), 'pio': gn('pio'), 'rsi': gn('rsi'),
            'mm200': mm200, 'revg': gn('revg'), 'epsg': gn('epsg'),
            'pb': gn('pb'), 'pe': gn('pe'), 'om': gn('om'),
            'marg_n': gn('marg_n'), 'marg_n1': gn('marg_n1'),
            'thesis': gdb('thesis'), 'contra': gdb('contra'),
            'moat': moat_list, 'moat_score': moat_score,
            'eps_reg': eps_reg, 'thesis_ok': thesis_ok,
            'in_zone': in_zone, 'upside': upside,
            'above_mm200': price > mm200 if mm200 else False,
            'good_rsi': 25 <= gn('rsi') <= 60 if gn('rsi') else False,
        }

        # ─── SCORE B.A.M (0-120) ─────────────────────────────────────────
        # B — Buffett Qualité (0-30)
        b_qualite = (20 if s['roe'] >= 25 else 16 if s['roe'] >= 18 else 11 if s['roe'] >= 12 else 6)
        r_avg = (s['margin'] + s['fcf']) / 2
        b_rentabilite = (20 if r_avg >= 20 else 15 if r_avg >= 12 else 10 if r_avg >= 7 else 5)
        b_bilan = (20 if s['debt'] <= 0.5 and s['pio'] >= 8 else 16 if s['debt'] <= 1 and s['pio'] >= 7 else 11 if s['debt'] <= 2 else 6)

        # B — Buffett MOAT (0-10, structuré par nb sources)
        b_moat = moat_score * 2  # 0-10

        # B — Buffett Valorisation (0-20) + régularité EPS
        b_val = (20 if upside >= 35 else 15 if upside >= 20 else 10 if upside >= 10 else 5 if upside >= 0 else 1)
        b_eps_reg = min(10, int(eps_reg))  # 0-10 régularité

        # Malus Beneish
        gmix = (s['marg_n1']/100) / max(s['margin']/100, 0.01) if s['marg_n1'] and s['margin'] else 1.0
        gmix = max(0.5, min(2.5, gmix))
        aqi  = min(1.5, 1 + (0.15 if s['pb'] > 3 else 0))
        sgi  = 1 + s['revg']/100 if s['revg'] > 0 else 1.0
        sgai = min(1.5, 1 + (s['om'] - s['margin'])/100 if s['om'] else 0)
        lvgi = min(2.0, 1 + s['debt'] * 0.1) if s['debt'] > 0 else 1.0
        tata = max(-0.1, min(0.15, (s['margin'] - s['fcf'])/100)) if s['margin'] and s['fcf'] else 0
        s['beneish'] = round(-4.84 + 0.920 + 0.528*gmix + 0.404*aqi + 0.892*sgi + 0.115 - 0.172*sgai + 4.679*tata - 0.327*lvgi, 2)
        if s['beneish'] > -1.49: b_val = max(1, b_val - 8)
        elif s['beneish'] > -1.78: b_val = max(1, b_val - 3)

        # Momentum technique
        mnt = 3
        if in_zone:            mnt += 7
        if s['above_mm200']:   mnt += 7
        if s['good_rsi']:      mnt += 3

        # M — Munger Thèse (0-10)
        m_these = 10 if thesis_ok else 0

        # Score total B.A.M
        bam_score = b_qualite + b_rentabilite + b_bilan + b_moat + b_val + b_eps_reg + mnt + m_these
        s['bam'] = bam_score

        # QARP legacy (compatibilité)
        s['qarp'] = b_qualite + b_rentabilite + b_bilan + b_val + mnt

        # Signal B.A.M
        s['signal'] = (
            'ULTIME'     if bam_score >= 85 and in_zone and upside > 5 and thesis_ok else
            'FORT'       if bam_score >= 68 and s['score'] in ['A','B'] and upside > 8 else
            'SURVEILLER' if bam_score >= 55 and s['score'] == 'A' else
            None
        )

        # Triptyque B.A.M
        s['triptyque'] = {
            'Q': s['roe'] >= 15 and s['margin'] >= 10 and s['debt'] <= 2,  # Qualité
            'M': moat_score >= 2,                                            # MOAT ≥2 sources
            'V': in_zone or (upside >= 15),                                  # Valorisation OK
        }
        s['triptyque_ok'] = all(s['triptyque'].values())

        risk   = price - s['stop'] if s['stop'] else 1
        reward = s['o1'] - price if s['o1'] else 0
        s['rr'] = round(reward / risk, 1) if risk > 0 else 0

        stocks.append(s)
    return stocks

# ─── INSIGHTS WEB ─────────────────────────────────────────────────────────
def fetch_insights_and_web(top_tickers):
    if not ANTHROPIC_KEY: return None
    today = datetime.now().strftime('%d/%m/%Y')
    prompt = (
        f"Date: {today}. Actions top QARP: {top_tickers}\n\n"
        "En HTML direct, 4 sections avec titres <h4> :\n\n"
        "1. INFLUENCEURS BOURSE FR (7 derniers jours) :\n"
        "   Guillaume Fournier (Finance Optimale / @GuillaumeFournier_Invest YouTube)\n"
        "   Rique Trading (@riquetrading YouTube + @rique.trading Instagram)\n"
        "   Nicolas Chéron (@NCheron_bourse X + ZoneBourse)\n"
        "   Jean-Benoît Gambet (@jeanbenoit_gambet Instagram)\n"
        "   Pour chacun: sentiment bull/bear + 1 ticker mentionné\n\n"
        "2. CONSENSUS ANALYSTES ZoneBourse sur: " + top_tickers + "\n\n"
        "3. RÉSULTATS TRIMESTRIELS Europe publiés cette semaine\n\n"
        "4. PÉPITE CACHÉE : 1 small/mid cap PEA sous-évaluée avec moat clair\n\n"
        "Chiffres précis uniquement. Pas de généralités."
    )
    try:
        payload = json.dumps({
            'model': 'claude-sonnet-4-6',
            'max_tokens': 1500,
            'tools': [{'type': 'web_search_20250305', 'name': 'web_search'}],
            'messages': [{'role': 'user', 'content': prompt}]
        }).encode()
        req = urllib.request.Request(
            'https://api.anthropic.com/v1/messages', data=payload,
            headers={
                'Content-Type': 'application/json',
                'x-api-key': ANTHROPIC_KEY,
                'anthropic-version': '2023-06-01',
                'anthropic-beta': 'web-search-2025-03-05'
            }
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        return ''.join(b.get('text','') for b in data.get('content',[]) if b.get('type')=='text').strip() or None
    except Exception as e:
        print(f"  insights error: {e}")
        return None

# ─── CARD ACTION ──────────────────────────────────────────────────────────
def stock_card(s, highlight=False):
    bam  = s['bam']
    sc   = '#22c55e' if bam >= 85 else '#d97706' if bam >= 68 else '#2563eb'
    gc   = {'A':'#16a34a','B':'#d97706','C':'#6b7280','D':'#dc2626'}.get(s['score'],'#6b7280')
    bg   = '#f0fdf4' if highlight else '#f8fafc'
    brd  = '#22c55e' if highlight else '#e2e8f0'

    # Triptyque feux
    tri = s['triptyque']
    feux = (
        ('<span style="color:#16a34a">✅ Qualité</span>' if tri['Q'] else '<span style="color:#dc2626">❌ Qualité</span>') + ' &nbsp;|&nbsp; ' +
        ('<span style="color:#16a34a">✅ MOAT</span>'    if tri['M'] else '<span style="color:#dc2626">❌ MOAT</span>')    + ' &nbsp;|&nbsp; ' +
        ('<span style="color:#16a34a">✅ Prix</span>'    if tri['V'] else '<span style="color:#dc2626">❌ Prix</span>')
    )
    tri_col = '#16a34a' if s['triptyque_ok'] else '#dc2626'
    tri_lbl = '🟢 TRIPTYQUE OK — Les 3 conditions réunies' if s['triptyque_ok'] else '🔴 TRIPTYQUE INCOMPLET'

    # Moat badges
    moat_badges = ''.join(
        '<span style="background:#dbeafe;color:#1d4ed8;padding:1px 6px;border-radius:3px;font-size:9px;margin:1px">' + m + '</span>'
        for m in s['moat'][:4]
    )
    moat_score_str = str(s['moat_score']) + '/5 sources'

    # Thesis check
    thesis_html = ''
    if not s['thesis_ok']:
        thesis_html = '<div style="background:#fee2e2;border-left:4px solid #dc2626;padding:6px 10px;margin-top:6px;font-size:10px;color:#dc2626;font-weight:700">⚠️ THÈSE DÉGRADÉE — Vérifier avant tout achat</div>'

    upside = s['upside']; price = s['price']; stop = s['stop']; o1 = s['o1']
    o1_pct    = round((o1 - price)/price*100) if o1 and price else 0
    dist_stop = round((price-stop)/price*100,1) if stop and price else 0

    th_h = ''
    if s.get('thesis'):
        th_h = ('<div style="margin-top:8px;padding:8px;background:#f0fdf4;border-left:3px solid #16a34a;font-size:10px;color:#1a4730;line-height:1.5">'
                '<b style="font-size:8px;color:#16a34a;text-transform:uppercase">Pourquoi investir (B)</b><br>'
                + s['thesis'][:220] + '</div>')
    ct_h = ''
    if s.get('contra'):
        ct_h = ('<div style="margin-top:4px;padding:8px;background:#fff5f5;border-left:3px solid #dc2626;font-size:10px;color:#7c2d2d;line-height:1.5">'
                '<b style="font-size:8px;color:#dc2626;text-transform:uppercase">Risque marché</b><br>'
                + s['contra'][:180] + '</div>')

    alerte = ''
    if stop > 0 and price <= stop * 1.05:
        alerte = f'<div style="background:#fee2e2;border-left:4px solid #dc2626;padding:5px 8px;margin-top:6px;font-size:9px;color:#dc2626"><b>⚠️ STOP PROCHE : {dist_stop}% du seuil ({stop}€)</b></div>'

    border_style = ';border-left:4px solid #22c55e' if highlight else ''
    zone_badge = '<span style="background:#dcfce7;color:#16a34a;padding:1px 5px;border-radius:3px;font-size:9px;font-weight:700">EN ZONE</span>' if s['in_zone'] else ''
    sector_div = '</div><div style="font-size:9px;color:#888">' + s['sector'][:30] + '</div>'
    moat_div = '<div style="margin-bottom:6px"><span style="font-size:9px;color:#888">MOAT ' + moat_score_str + ' : </span>' + (moat_badges or '<span style="font-size:9px;color:#dc2626">Non identifié</span>') + '</div>'
    upside_col = '#16a34a' if upside > 15 else '#d97706'
    upside_str2 = ('+' if upside > 0 else '') + str(upside) + '%'
    rr_col = '#16a34a' if s['rr'] >= 1.5 else '#d97706'
    eps_col = '#16a34a' if s['eps_reg'] >= 7 else '#d97706'
    sig_str = s['signal'] or '—'
    parts = [
        '<div style="background:' + bg + ';border:1px solid ' + brd + ';border-radius:8px;padding:14px 16px;margin-bottom:12px' + border_style + '">',
        '<table width="100%" cellpadding="0"><tr>',
        '<td style="vertical-align:top">',
        '<div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:4px">',
        '<span style="background:' + gc + ';color:#fff;padding:2px 8px;border-radius:3px;font-size:10px;font-weight:700">' + s['score'] + '</span>',
        '<b style="font-size:15px;color:#0f2540;font-family:monospace">' + s['ticker'] + '</b>',
        '<span style="color:#888;font-size:10px">' + s['name'][:20] + '</span>',
        zone_badge,
        sector_div,
        '</td>',
        '<td style="vertical-align:top;text-align:right;min-width:100px">',
        '<div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:8px;padding:10px 14px;text-align:center">',
        '<div style="font-size:10px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:1px">B.A.M</div>',
        '<div style="font-size:26px;font-weight:700;color:' + sc + ';font-family:monospace">' + str(bam) + '</div>',
        '<div style="font-size:8px;color:rgba(255,255,255,.4)">/120</div>',
        '<div style="margin-top:3px;font-size:9px;color:#f0d080;font-weight:700">' + sig_str + '</div>',
        '</div></td></tr></table>',
        '<div style="background:' + tri_col + '15;border:1px solid ' + tri_col + '40;border-radius:6px;padding:6px 10px;margin:8px 0;font-size:9px">',
        '<b style="color:' + tri_col + '">' + tri_lbl + '</b><br>',
        '<div style="margin-top:4px">' + feux + '</div>',
        '</div>',
        moat_div,
        '<table width="100%" cellpadding="3" style="font-size:10px;margin-bottom:6px">',
        '<tr><td style="color:#888">Cours</td><td><b style="font-family:monospace">' + str(price) + '€</b></td>',
        '<td style="color:#888">Zone</td><td><b style="font-family:monospace">' + str(s['el']) + '–' + str(s['eh']) + '€</b></td></tr>',
        '<tr><td style="color:#888">Stop</td><td><b style="color:#dc2626;font-family:monospace">' + str(stop) + '€</b></td>',
        '<td style="color:#888">Obj.1</td><td><b style="color:#16a34a;font-family:monospace">' + str(o1) + '€ (+' + str(o1_pct) + '%)</b></td></tr>',
        '<tr><td style="color:#888">Upside</td><td><b style="color:' + upside_col + '">' + upside_str2 + '</b></td>',
        '<td style="color:#888">R/R</td><td><b style="color:' + rr_col + '">' + str(s['rr']) + 'x</b></td></tr>',
        '<tr><td style="color:#888">ROE</td><td><b>' + str(s['roe']) + '%</b></td>',
        '<td style="color:#888">Piotroski</td><td><b>' + str(int(s['pio'])) + '/9</b></td></tr>',
        '<tr><td style="color:#888">Marge</td><td><b>' + str(s['margin']) + '%</b></td>',
        '<td style="color:#888">Rég. EPS</td><td><b style="color:' + eps_col + '">' + str(round(s['eps_reg'],1)) + '/10</b></td></tr>',
        '</table>',
        thesis_html, th_h, ct_h, alerte,
        '</div>',
    ]
    return ''.join(parts)

def section_html(title, color, items, max_items=6):
    if not items: return ''
    cards = ''.join(stock_card(s, highlight=(s['signal']=='ULTIME')) for s in items[:max_items])
    return (
        '<div style="margin-bottom:20px">'
        '<div style="background:' + color + ';color:#fff;padding:9px 14px;border-radius:6px 6px 0 0;font-size:12px;font-weight:700;display:flex;justify-content:space-between">'
        '<span>' + title + '</span><span style="opacity:.8">' + str(len(items)) + ' action' + ('s' if len(items)>1 else '') + '</span></div>'
        '<div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 6px 6px;padding:10px">' + cards + '</div>'
        '</div>'
    )

# ─── SECTION PROTOCOLE B.A.M ──────────────────────────────────────────────
def section_bam_protocole(stocks, budget=1000):
    """Section décision du dimanche — protocole B.A.M complet"""
    # Top 3 triptyque complet
    triptyque_valides = sorted(
        [s for s in stocks if s['triptyque_ok'] and s['signal'] in ('ULTIME','FORT')],
        key=lambda x: -x['bam']
    )[:3]

    # Actions avec thèse dégradée
    theses_brisees = [s for s in stocks if not s['thesis_ok'] and s['score'] in ['A','B']]

    # Beneish suspects
    suspects = [s for s in stocks if s['beneish'] > -1.78 and s['score'] in ['A','B']]

    html = (
        '<div style="background:#0f2540;color:#fff;border-radius:12px;padding:20px 24px;margin-bottom:16px">'
        '<div style="font-size:8px;letter-spacing:3px;color:#f0d080;text-transform:uppercase;margin-bottom:8px">PROTOCOLE B.A.M · BUFFETT · ACKMAN · MUNGER</div>'
        '<div style="font-size:18px;font-weight:700;font-family:Georgia,serif;margin-bottom:4px">Décision du dimanche</div>'
        '<div style="font-size:11px;color:rgba(255,255,255,.6)">Triptyque complet requis : Qualité + MOAT ≥2 sources + Valorisation</div>'
        '</div>'
    )

    if triptyque_valides:
        html += '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin-bottom:12px">'
        html += '<div style="font-size:11px;font-weight:700;color:#0f2540;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">🟢 Triptyque validé — Candidats à l\'achat</div>'

        for s in triptyque_valides:
            # Allocation Ackman : max 20 lignes, sizing par conviction
            bam_pct = s['bam'] / 120
            alloc   = round(budget * min(0.15, bam_pct * 0.20))  # max 15% par position
            nb_titres = int(alloc / s['price']) if s['price'] > 0 else 0

            html += (
                '<div style="border:1px solid #dcfce7;border-radius:6px;padding:12px;margin-bottom:8px;background:#f0fdf4">'
                '<div style="display:flex;justify-content:space-between;align-items:center">'
                '<div>'
                '<b style="font-size:14px;font-family:monospace">' + s['ticker'] + '</b>'
                '<span style="color:#888;font-size:11px;margin-left:6px">' + s['name'][:18] + '</span>'
                '</div>'
                '<span style="background:#16a34a;color:#fff;padding:2px 10px;border-radius:3px;font-size:10px;font-weight:700">BAM ' + str(s['bam']) + '/120</span>'
                '</div>'
                '<div style="margin-top:8px;display:grid;grid-template-columns:repeat(3,1fr);gap:6px">'
                '<div style="background:#fff;border-radius:4px;padding:6px;text-align:center">'
                '<div style="font-size:16px;font-weight:700;color:#0f2540">' + str(alloc) + '€</div>'
                '<div style="font-size:8px;color:#888;text-transform:uppercase">Budget alloué</div>'
                '</div>'
                '<div style="background:#fff;border-radius:4px;padding:6px;text-align:center">'
                '<div style="font-size:16px;font-weight:700;color:#0f2540">' + str(nb_titres) + '</div>'
                '<div style="font-size:8px;color:#888;text-transform:uppercase">Nb titres</div>'
                '</div>'
                '<div style="background:#fff;border-radius:4px;padding:6px;text-align:center">'
                '<div style="font-size:16px;font-weight:700;color:#16a34a">+' + str(s['upside']) + '%</div>'
                '<div style="font-size:8px;color:#888;text-transform:uppercase">Upside DCF</div>'
                '</div>'
                '</div>'
                '<div style="margin-top:6px;font-size:9px;color:#444">'
                '📌 Stop : ' + str(s['stop']) + '€ &nbsp;|&nbsp; Obj.1 : ' + str(s['o1']) + '€ &nbsp;|&nbsp; R/R : ' + str(s['rr']) + 'x'
                '</div>'
                '</div>'
            )
        html += '</div>'
    else:
        html += '<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px;margin-bottom:12px;font-size:11px;color:#92400e">⏳ Aucun triptyque complet cette semaine. Patience — qualité + MOAT + valorisation doivent être réunis simultanément.</div>'

    # Thèses dégradées
    if theses_brisees:
        html += '<div style="background:#fff5f5;border:1px solid #fecaca;border-radius:8px;padding:12px;margin-bottom:12px">'
        html += '<div style="font-size:11px;font-weight:700;color:#dc2626;margin-bottom:8px">🔴 Thèses à réévaluer (Munger)</div>'
        for s in theses_brisees[:3]:
            html += '<div style="padding:4px 0;font-size:11px"><b style="font-family:monospace">' + s['ticker'] + '</b> — ' + s['name'][:20] + ' · Vérifier thèse avant maintien</div>'
        html += '</div>'

    # Suspects Beneish
    if suspects:
        html += '<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px;margin-bottom:12px">'
        html += '<div style="font-size:11px;font-weight:700;color:#92400e;margin-bottom:6px">⚠️ Beneish M-Score — Vérification comptable</div>'
        html += '<div style="font-size:10px;color:#78350f">' + ' · '.join(s['ticker'] + ' (M=' + str(s['beneish']) + ')' for s in suspects[:5]) + '</div>'
        html += '</div>'

    # Règle Ackman concentration
    html += (
        '<div style="background:#f8f6ff;border:1px solid #c4b5fd;border-radius:8px;padding:12px">'
        '<div style="font-size:10px;font-weight:700;color:#7c3aed;margin-bottom:4px">📐 Règle Ackman — Concentration</div>'
        '<div style="font-size:10px;color:#5b21b6">Maximum 15-20 lignes. Chaque position doit être explicable en 3 phrases. '
        'Budget mensuel : ' + str(budget) + '€. Sizing proportionnel au score B.A.M. '
        'Ne jamais entrer si le triptyque n\'est pas complet.</div>'
        '</div>'
    )
    return html

# ─── BUILD EMAIL ──────────────────────────────────────────────────────────
def build_email(stocks, macro, insights_html, date_str, is_sunday=False):
    ultimes  = sorted([s for s in stocks if s['signal']=='ULTIME'],    key=lambda x: -x['bam'])
    forts    = sorted([s for s in stocks if s['signal']=='FORT'],      key=lambda x: -x['bam'])
    surv     = sorted([s for s in stocks if s['signal']=='SURVEILLER' and s['score']=='A'], key=lambda x: -x['bam'])
    suspects = [s for s in stocks if s['beneish'] > -1.78 and s['score'] in ['A','B']]
    triptyques_ok = sum(1 for s in stocks if s['triptyque_ok'])

    mv, msignals = macro_verdict(macro)
    today_label  = "PROTOCOLE BAM — DIMANCHE" if is_sunday else "RADAR DU SOIR"
    today_fr     = datetime.now().strftime('%A %d %B %Y').capitalize()

    macro_rows = ''
    for key in ['CAC40','VIX','OR','TAUX','DXY']:
        m = macro.get(key, {})
        if not m.get('value'): continue
        chg = m.get('chg', 0)
        col = '#16a34a' if chg > 0 else '#dc2626'
        macro_rows += (
            '<tr><td style="padding:3px 8px;font-size:10px;color:#888">' + m['label'] + '</td>'
            '<td style="padding:3px 8px;font-family:monospace;font-weight:700;font-size:11px">' + str(m['value']) + '</td>'
            '<td style="padding:3px 8px;color:' + col + ';font-family:monospace;font-size:10px">' + ('+' if chg>0 else '') + str(chg) + '%</td></tr>'
        )

    insights_section = ''
    if insights_html:
        insights_section = (
            '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin-bottom:16px">'
            '<div style="font-size:11px;font-family:monospace;color:#0f2540;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px">'
            '🎬 Influenceurs · Consensus · Résultats · Pépite</div>'
            '<div style="font-size:12px;line-height:1.7;color:#333">' + insights_html + '</div>'
            '</div>'
        )

    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f1f5f9;font-family:Helvetica Neue,Arial,sans-serif">
<div style="max-width:680px;margin:0 auto;padding:16px">

<!-- HEADER -->
<div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:12px;padding:20px 24px;margin-bottom:16px">
<div style="font-size:8px;font-family:monospace;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:3px;margin-bottom:6px">VAL.PEA · MÉTHODE B.A.M · BUFFETT · ACKMAN · MUNGER</div>
<div style="font-size:20px;font-weight:700;color:#f0d080;font-family:Georgia,serif;margin-bottom:3px">{today_label} — {today_fr}</div>
<div style="font-size:11px;color:rgba(255,255,255,.6)">{len(stocks)} valeurs · {sum(1 for s in stocks if s["score"]=="A")} Grade A · {len(ultimes)} ULTIME · {triptyques_ok} Triptyques OK</div>
<div style="display:flex;gap:10px;margin-top:12px;flex-wrap:wrap">
{''.join(f'<div style="background:rgba(255,255,255,.08);border-radius:5px;padding:6px 12px;text-align:center"><div style="font-size:16px;font-weight:700;color:#f0d080;font-family:monospace">{v}</div><div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase">{l}</div></div>' for v,l in [(len(ultimes),"ULTIME"),(len(forts),"FORTS"),(triptyques_ok,"Triptyques"),(len(suspects),"⚠️ Beneish")])}
</div>
</div>

<!-- MACRO -->
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:14px;margin-bottom:16px">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
<b style="font-size:11px;color:#0f2540;text-transform:uppercase;letter-spacing:1px">Contexte Macro</b>
<span style="padding:3px 10px;background:{mv[2]};color:{mv[1]};border-radius:4px;font-size:10px;font-weight:700">{mv[0]}</span>
</div>
<table width="100%" cellpadding="0">
<tr><td colspan="3" style="padding-bottom:6px">
{''.join(f'<div style="font-size:9px;color:#444;margin-bottom:2px">{icon} {desc}</div>' for icon,desc in msignals)}
</td></tr>
{macro_rows}
</table>
</div>

{section_bam_protocole(stocks) if is_sunday else ''}

{insights_section}

{section_html("🚀 Signaux ULTIMES — BAM ≥85 + Triptyque + Zone", "#16a34a", ultimes)}
{section_html("✅ Signaux FORTS — BAM ≥68 (Grade A/B)", "#d97706", forts)}
{section_html("👁 À Surveiller — Grade A en approche", "#2563eb", surv, max_items=3)}

<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px;margin-bottom:16px">
<b style="font-size:10px;color:#d97706">📐 Règle fondamentale B.A.M</b><br>
<span style="font-size:10px;color:#78350f">Ce mail détecte, il n'ordonne pas. Toute entrée requiert : Score A + Triptyque complet (Q+M+V) + Thèse intacte + Sizing Ackman (max 15% par ligne). Jamais sous pression, jamais en semaine.</span>
</div>

<div style="text-align:center;font-size:9px;color:#94a3b8;padding:10px">VAL.PEA · Méthode B.A.M · Non-conseil · {date_str}</div>
</div></body></html>'''

# ─── SEND ─────────────────────────────────────────────────────────────────
def send_email(subject, html):
    with open('alert_preview.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Preview: alert_preview.html")
    if not GMAIL_USER or not GMAIL_PASS or not EMAIL_TO:
        print("⚠️ SMTP non configuré")
        return False
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From']    = GMAIL_USER
        msg['To']      = EMAIL_TO
        msg.attach(MIMEText(html, 'html', 'utf-8'))
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(GMAIL_USER, GMAIL_PASS)
            s.sendmail(GMAIL_USER, EMAIL_TO.split(','), msg.as_string())
        print(f"✅ Mail envoyé à {EMAIL_TO}")
        return True
    except Exception as e:
        print(f"❌ SMTP: {e}")
        return False

def send_telegram(stocks, mv, is_sunday):
    if not TG_TOKEN or not TG_CHAT: return
    ultimes  = [s for s in stocks if s['signal']=='ULTIME']
    forts    = [s for s in stocks if s['signal']=='FORT']
    tri_ok   = [s for s in stocks if s['triptyque_ok'] and s['signal'] in ('ULTIME','FORT')]
    def esc(t): return str(t).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    msg = (f"📊 <b>VAL.PEA B.A.M — {'Dimanche' if is_sunday else 'Soir'} {datetime.now().strftime('%d/%m')}</b>\n"
           f"Macro: {esc(mv[0])}\n\n")
    if tri_ok:
        msg += f"🟢 <b>TRIPTYQUES OK ({len(tri_ok)})</b>\n"
        for s in tri_ok[:3]:
            msg += f" • <b>{esc(s['ticker'])}</b> — BAM {s['bam']}/120 · Upside {s['upside']}%\n"
    if ultimes:
        msg += f"\n🚀 <b>ULTIMES ({len(ultimes)})</b>\n"
        for s in ultimes[:4]: msg += f" • <b>{esc(s['ticker'])}</b> {esc(s['name'][:12])} — {s['bam']}/120\n"
    if forts:
        msg += f"\n✅ <b>FORTS ({len(forts)})</b>\n"
        for s in forts[:3]: msg += f" • <b>{esc(s['ticker'])}</b> — {s['bam']}/120\n"
    payload = json.dumps({'chat_id': TG_CHAT, 'text': msg[:3800], 'parse_mode': 'HTML'})
    try:
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
            data=payload.encode(), headers={'Content-Type':'application/json'})
        urllib.request.urlopen(req, timeout=10)
        print("✅ Telegram envoyé")
    except Exception as e:
        print(f"⚠️ Telegram: {e}")

# ─── MAIN ─────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("=" * 60)
    print(f"VAL.PEA B.A.M — {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 60)

    if not os.path.exists('index.html'):
        print("❌ index.html introuvable"); sys.exit(1)
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    print("\n📊 Parsing actions (B.A.M)...")
    stocks = get_stocks(content)
    print(f"  {len(stocks)} actions · {sum(1 for s in stocks if s['triptyque_ok'])} triptyques OK")

    print("\n📡 Récupération macro...")
    macro = fetch_macro()
    mv, _ = macro_verdict(macro)
    for k, v in macro.items():
        if v['value']: print(f"  {v['label']}: {v['value']} ({'+' if v['chg']>0 else ''}{v['chg']}%)")

    is_sunday  = datetime.now().weekday() == 6
    is_weekend = datetime.now().weekday() in (5, 6)

    print("\n🔍 Insights influenceurs & web...")
    top5 = ', '.join(s['ticker'] for s in sorted(stocks, key=lambda x: -x['bam'])[:5])
    insights_html = fetch_insights_and_web(top5) if ANTHROPIC_KEY else None
    if insights_html: print(f"  ✅ {len(insights_html)} chars")

    date_str   = datetime.now().strftime('%d/%m/%Y %H:%M')
    email_html = build_email(stocks, macro, insights_html, date_str, is_sunday)

    ultimes = [s for s in stocks if s['signal']=='ULTIME']
    forts   = [s for s in stocks if s['signal']=='FORT']
    tri_ok  = sum(1 for s in stocks if s['triptyque_ok'])
    subject = f"VAL.PEA B.A.M · {datetime.now().strftime('%d/%m')} · {len(ultimes)} ULTIME · {tri_ok} Triptyques"

    send_email(subject, email_html)
    send_telegram(stocks, mv, is_sunday)
    print("\n✅ Terminé")
