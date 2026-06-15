#!/usr/bin/env python3
"""
send_alerts_v2.py — Mail enrichi VAL.PEA (CORRIGÉ)
Corrections :
  - Bug html+= avant définition → déplacé dans return
  - insights traité en texte HTML brut (pas dict)
  - Secrets MAIL_USER/MAIL_PASS/MAIL_TO + compat GMAIL_USER/GMAIL_PASSWORD
  - Modèle Sonnet pour qualité
"""
import re, json, os, sys, smtplib, urllib.request, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ─── CONFIG SECRETS (double compat) ───────────────────────────────────────
ANTHROPIC_KEY  = os.environ.get('ANTHROPIC_API_KEY', '').strip()
GMAIL_USER     = (os.environ.get('MAIL_USER') or os.environ.get('GMAIL_USER', '')).strip()
GMAIL_PASS     = (os.environ.get('MAIL_PASS') or os.environ.get('GMAIL_PASSWORD', '')).strip()
EMAIL_TO       = (os.environ.get('MAIL_TO') or GMAIL_USER).strip()
TG_TOKEN       = os.environ.get('TELEGRAM_TOKEN', '').strip()
TG_CHAT        = os.environ.get('TELEGRAM_CHAT_ID', '').strip()

print(f"ANTHROPIC_API_KEY: {'✅ ' + str(len(ANTHROPIC_KEY)) + ' chars' if ANTHROPIC_KEY else '❌ manquant'}")
print(f"MAIL_USER: {'✅ ' + GMAIL_USER if GMAIL_USER else '❌ manquant'}")
print(f"MAIL_TO: {'✅ ' + EMAIL_TO if EMAIL_TO else '❌ manquant'}")

# ─── MACRO ────────────────────────────────────────────────────────────────
def fetch_macro():
    macro = {}
    tickers = {
        'VIX':   ('^VIX',      'VIX (peur)'),
        'OR':    ('GC=F',      'Or ($/oz)'),
        'TAUX':  ('^TNX',      'Taux US 10 ans'),
        'DXY':   ('DX-Y.NYB',  'Dollar Index'),
        'CAC40': ('^FCHI',     'CAC 40'),
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
        time.sleep(0.3)
    return macro

def macro_sentiment(macro):
    vix  = macro.get('VIX',  {}).get('value', 20)
    taux = macro.get('TAUX', {}).get('value', 4)
    dxy  = macro.get('DXY',  {}).get('value', 104)
    score = 0
    signals = []
    if   vix < 15: score += 1;  signals.append(('✅', 'VIX bas',        'Calme des marchés'))
    elif vix < 20: signals.append(('🟡', 'VIX modéré',  'Légère prudence'))
    elif vix < 30: score -= 1;  signals.append(('⚠️', 'VIX élevé',      'Volatilité importante'))
    else:          score -= 2;  signals.append(('🚨', 'VIX très élevé', 'Stress extrême'))
    if   taux < 3.5: score += 1; signals.append(('✅', 'Taux bas',    'Favorable aux actions'))
    elif taux < 4.5: signals.append(('🟡', 'Taux neutres', f'{taux}%'))
    else:            score -= 1; signals.append(('⚠️', 'Taux élevés', f'{taux}% — freine valorisation'))
    if   dxy < 100: score += 1; signals.append(('✅', 'Dollar faible', 'Favorable émergents/Europe'))
    elif dxy > 106: score -= 1; signals.append(('⚠️', 'Dollar fort',   'Pression devises'))
    if   score >= 2: verdict = ('✅ FAVORABLE', '#16a34a', '#dcfce7')
    elif score >= 0: verdict = ('🟡 NEUTRE',    '#d97706', '#fef3c7')
    else:            verdict = ('⚠️ PRUDENCE',  '#dc2626', '#fee2e2')
    return verdict, signals

# ─── YOUTUBE + SOURCES WEB via Claude ─────────────────────────────────────
def fetch_youtube_and_web_insights():
    """Retourne du HTML brut — 4 influenceurs + consensus + pépites"""
    if not ANTHROPIC_KEY:
        return None
    prompt = (
        f"Date: {datetime.now().strftime('%d/%m/%Y')}.\n\n"
        "MISSION en HTML direct (pas de markdown) :\n"
        "1. INFLUENCEURS BOURSE FR — dernières publications (7 jours) :\n"
        "   • Guillaume Fournier (YouTube @GuillaumeFournier_Invest)\n"
        "   • Rique Trading (YouTube @riquetrading + Instagram @rique.trading)\n"
        "   • Nicolas Chéron (@NCheron_bourse X + ZoneBourse)\n"
        "   • Jean-Benoît Gambet (@jeanbenoit_gambet Instagram)\n"
        "   Pour chacun : sentiment bull/bear/neutre + 1 ticker mentionné\n\n"
        "2. CONSENSUS analystes ZoneBourse sur les actions CAC40/SBF120 du moment\n"
        "3. RÉSULTATS trimestriels publiés cette semaine (Europe)\n"
        "4. PÉPITE cachée : 1 small/mid cap européenne sous-évaluée\n\n"
        "Format HTML avec <b>noms</b> et <span style='color:#1d4ed8'>tickers</span>. "
        "Chaque section avec un titre <h4>. Direct, factuel, chiffres réels."
    )
    try:
        payload = json.dumps({
            'model': 'claude-sonnet-4-6',
            'max_tokens': 1200,
            'tools': [{'type': 'web_search_20250305', 'name': 'web_search'}],
            'messages': [{'role': 'user', 'content': prompt}]
        }).encode('utf-8')
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
        # Extraire tout le texte (ignorer tool_use blocks)
        text = ''.join(b.get('text', '') for b in data.get('content', []) if b.get('type') == 'text')
        return text.strip() if text else None
    except Exception as e:
        print(f"  insights error: {e}")
        return None

def fetch_extra_sources(top_tickers_str):
    """Analyse marché + pépites small cap"""
    if not ANTHROPIC_KEY:
        return None
    prompt = (
        f"Date: {datetime.now().strftime('%d/%m/%Y')}. Top QARP: {top_tickers_str}\n\n"
        "En HTML direct :\n"
        "1. CAC40 niveaux techniques clés cette semaine\n"
        "2. Consensus analystes pour ces tickers (ZoneBourse/Reuters)\n"
        "3. 1 pépite small cap européenne PEA-éligible sous-évaluée\n"
        "Chiffres précis uniquement."
    )
    try:
        payload = json.dumps({
            'model': 'claude-sonnet-4-6',
            'max_tokens': 600,
            'tools': [{'type': 'web_search_20250305', 'name': 'web_search'}],
            'messages': [{'role': 'user', 'content': prompt}]
        }).encode('utf-8')
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
        text = ''.join(b.get('text', '') for b in data.get('content', []) if b.get('type') == 'text')
        return text.strip() if text else None
    except Exception as e:
        print(f"  extra error: {e}")
        return None

# ─── PARSER STOCKS ────────────────────────────────────────────────────────
def get_stocks(html_content):
    s_start = html_content.find("const S=[")
    if s_start < 0:
        return []
    stocks = []
    seen = set()
    for m in re.finditer(r"\{ticker:'([^']+)'(.*?)(?=\n\n\{ticker:|\n\n\];)", html_content[s_start:], re.DOTALL):
        ticker = m.group(1)
        if ticker in seen: continue
        seen.add(ticker)
        block = m.group(0)
        def gn(key, default=0.0):
            mx = re.search(r'\b'+key+r':([-\d.]+)', block)
            return float(mx.group(1)) if mx else default
        def gs(key, default=''):
            mx = re.search(r"\b"+key+r":'([^']*)'", block)
            return mx.group(1) if mx else default
        def gdb(key, default=''):
            mx = re.search(r'\b'+key+r':"([^"]*)"', block)
            return mx.group(1) if mx else default
        price = gn('price'); dcfm = gn('dcfm')
        s = {
            'ticker': ticker, 'name': gs('name'), 'sector': gs('sector'), 'score': gs('score'),
            'price': price, 'el': gn('el'), 'eh': gn('eh'), 'stop': gn('stop'),
            'o1': gn('o1'), 'dcfb': gn('dcfb'), 'dcfm': dcfm, 'dcfu': gn('dcfu'),
            'roe': gn('roe'), 'margin': gn('margin'), 'fcf': gn('fcf'), 'debt': gn('debt'),
            'pio': gn('pio'), 'rsi': gn('rsi'), 'mm200': gn('mm200'), 'mm50': gn('mm50'),
            'revg': gn('revg'), 'epsg': gn('epsg'), 'pb': gn('pb'),
            'pe': gn('pe'), 'ev_ebitda': gn('ev_ebitda'),
            'om': gn('om'), 'marg_n': gn('marg_n'), 'marg_n1': gn('marg_n1'),
            'thesis': gdb('thesis'), 'contra': gdb('contra'),
        }
        s['in_zone']     = price > 0 and dcfm > 0 and price <= dcfm * 0.88 and s['score'] in ['A','B']
        s['above_mm200'] = price > s['mm200'] if s['mm200'] else False
        s['good_rsi']    = 25 <= s['rsi'] <= 60 if s['rsi'] else False
        s['upside']      = round((dcfm - price) / price * 100, 1) if price and dcfm else 0
        # Beneish
        gmix = (s['marg_n1']/100) / max(s['margin']/100, 0.01) if s['marg_n1'] and s['margin'] else 1.0
        gmix = max(0.5, min(2.5, gmix))
        aqi  = min(1.5, 1 + (0.15 if s['pb'] > 3 else 0))
        sgi  = 1 + s['revg']/100 if s['revg'] > 0 else 1.0
        sgai = min(1.5, 1 + (s['om'] - s['margin'])/100 if s['om'] else 0)
        lvgi = min(2.0, 1 + s['debt'] * 0.1) if s['debt'] > 0 else 1.0
        tata = max(-0.1, min(0.15, (s['margin'] - s['fcf'])/100)) if s['margin'] and s['fcf'] else 0
        s['beneish'] = round(-4.84 + 0.920*1.0 + 0.528*gmix + 0.404*aqi +
                             0.892*sgi + 0.115*1.0 - 0.172*sgai + 4.679*tata - 0.327*lvgi, 2)
        # QARP
        q = 20 if s['roe'] >= 25 else 16 if s['roe'] >= 18 else 11 if s['roe'] >= 12 else 6
        r_avg = (s['margin'] + s['fcf']) / 2
        r = 20 if r_avg >= 20 else 15 if r_avg >= 12 else 10 if r_avg >= 7 else 5
        b = 20 if s['debt'] <= 0.5 and s['pio'] >= 8 else 16 if s['debt'] <= 1 and s['pio'] >= 7 else 11 if s['debt'] <= 2 else 6
        v = 20 if s['upside'] >= 35 else 15 if s['upside'] >= 20 else 10 if s['upside'] >= 10 else 5 if s['upside'] >= 0 else 1
        if s['beneish'] > -1.49: v = max(1, v - 8)
        elif s['beneish'] > -1.78: v = max(1, v - 3)
        mnt = 3
        if s['in_zone']:     mnt += 7
        if s['above_mm200']: mnt += 7
        if s['good_rsi']:    mnt += 3
        s['qarp'] = q + r + b + v + mnt
        # Signal
        s['signal'] = ('ULTIME'    if s['qarp'] >= 70 and s['in_zone'] and s['upside'] > 5 else
                        'FORT'      if s['qarp'] >= 58 and s['score'] in ['A','B'] and s['upside'] > 8 else
                        'SURVEILLER' if s['qarp'] >= 50 and s['score'] == 'A' else None)
        risk   = s['price'] - s['stop'] if s['stop'] else 1
        reward = s['o1'] - s['price'] if s['o1'] else 0
        s['rr'] = round(reward / risk, 1) if risk > 0 else 0
        stocks.append(s)
    return stocks

# ─── CARTE ACTION ─────────────────────────────────────────────────────────
def stock_card(s, highlight=False):
    sc  = '#22c55e' if s['qarp'] >= 70 else '#d97706' if s['qarp'] >= 55 else '#2563eb'
    gc  = {'A':'#16a34a','B':'#d97706','C':'#6b7280','D':'#dc2626'}.get(s['score'],'#6b7280')
    bg  = '#f0fdf4' if highlight else '#f8fafc'
    brd = '#22c55e' if highlight else '#e2e8f0'
    zone_h = ('<span style="background:#dcfce7;color:#16a34a;padding:1px 5px;border-radius:3px;font-size:9px;font-weight:700">EN ZONE</span>'
              if s['in_zone'] else
              '<span style="background:#f1f5f9;color:#64748b;padding:1px 5px;border-radius:3px;font-size:9px">hors zone</span>')
    b_h = ''
    if s['beneish'] > -1.78:
        bc  = '#dc2626' if s['beneish'] > -1.49 else '#d97706'
        b_h = f'<span style="background:#fee2e2;color:{bc};padding:1px 5px;border-radius:3px;font-size:9px;font-weight:700">Beneish {s["beneish"]}</span>'
    upside = s['upside']; price = s['price']; stop = s.get('stop',0); o1 = s.get('o1',0)
    o1_pct    = round((o1 - price)/price*100) if o1 and price else 0
    dist_stop = round((price-stop)/price*100,1) if stop and price else 0
    dist_o1   = round((o1-price)/price*100,1) if o1 and price else 0
    rr = s['rr']
    alerte = ''
    if stop > 0 and price <= stop * 1.05:
        alerte = f'<div style="background:#fee2e2;border-left:4px solid #dc2626;padding:5px 8px;margin-top:6px;border-radius:0 4px 4px 0;font-size:9px;color:#dc2626"><b>ATTENTION : {dist_stop}% du stop ({stop}€)</b></div>'
    elif upside < -10 and not s['in_zone']:
        alerte = f'<div style="background:#fff7ed;border-left:4px solid #ea580c;padding:5px 8px;margin-top:6px;border-radius:0 4px 4px 0;font-size:9px;color:#ea580c"><b>PV latente : cours dépasse le DCF de {abs(upside)}%</b></div>'
    thesis = s.get('thesis','')[:220]
    contra = s.get('contra','')[:180]
    th_h = (f'<div style="margin-top:10px;padding:8px 10px;background:#f0fdf4;border-left:3px solid #16a34a;border-radius:0 4px 4px 0">'
            f'<div style="font-size:8px;color:#16a34a;font-weight:700;text-transform:uppercase;margin-bottom:3px">Pourquoi investir</div>'
            f'<div style="font-size:10px;color:#1a4730;line-height:1.5">{thesis}</div></div>') if thesis else ''
    ct_h = (f'<div style="margin-top:6px;padding:8px 10px;background:#fff5f5;border-left:3px solid #dc2626;border-radius:0 4px 4px 0">'
            f'<div style="font-size:8px;color:#dc2626;font-weight:700;text-transform:uppercase;margin-bottom:3px">Ce que le marché craint</div>'
            f'<div style="font-size:10px;color:#7c2d2d;line-height:1.5">{contra}</div></div>') if contra else ''
    return (f'<div style="background:{bg};border:1px solid {brd};border-radius:8px;padding:14px 16px;margin-bottom:12px'
            f'{";border-left:4px solid #22c55e" if highlight else ""}">'
            f'<table width="100%" cellpadding="0" cellspacing="0"><tr>'
            f'<td style="vertical-align:top">'
            f'<div style="display:flex;align-items:center;gap:6px;margin-bottom:6px;flex-wrap:wrap">'
            f'<span style="background:{gc};color:#fff;padding:2px 8px;border-radius:3px;font-size:10px;font-weight:700">{s["score"]}</span>'
            f'<b style="font-size:15px;color:#0f2540;font-family:monospace">{s["ticker"]}</b>'
            f'<span style="color:#888;font-size:10px">{s["name"][:20]}</span>'
            f'{zone_h}{b_h}</div>'
            f'<div style="font-size:9px;color:#888;margin-bottom:6px">{s.get("sector","")}</div>'
            f'</td><td style="vertical-align:top;text-align:right;min-width:90px">'
            f'<div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:8px;padding:10px 14px;text-align:center">'
            f'<div style="font-size:26px;font-weight:700;color:{sc};font-family:monospace">{s["qarp"]}</div>'
            f'<div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase">/100 QARP</div>'
            f'<div style="margin-top:4px;font-size:9px;color:#f0d080;font-weight:700">{s["signal"] or "—"}</div>'
            f'</div></td></tr></table>'
            f'<table width="100%" cellpadding="3" cellspacing="0" style="font-size:10px;margin-bottom:6px">'
            f'<tr><td style="color:#888">Cours</td><td><b style="font-family:monospace">{price}€</b></td>'
            f'<td style="color:#888">Zone</td><td><b style="font-family:monospace">{s["el"]}–{s["eh"]}€</b></td></tr>'
            f'<tr><td style="color:#888">Stop</td><td><b style="color:#dc2626;font-family:monospace">{stop}€</b></td>'
            f'<td style="color:#888">Obj.1</td><td><b style="color:#16a34a;font-family:monospace">{o1}€ (+{o1_pct}%)</b></td></tr>'
            f'<tr><td style="color:#888">Upside</td><td><b style="color:{"#16a34a" if upside>15 else "#d97706"};font-family:monospace">{"+"+str(upside) if upside>0 else str(upside)}%</b></td>'
            f'<td style="color:#888">R/R</td><td><b style="font-family:monospace;color:{"#16a34a" if rr>=1.5 else "#d97706"}">{rr}x</b></td></tr>'
            f'<tr><td style="color:#888">ROE</td><td><b style="font-family:monospace">{s["roe"]}%</b></td>'
            f'<td style="color:#888">Piotroski</td><td><b style="font-family:monospace">{int(s["pio"])}/9</b></td></tr>'
            f'<tr><td style="color:#888">Marge</td><td><b style="font-family:monospace">{s["margin"]}%</b></td>'
            f'<td style="color:#888">Dette</td><td><b style="font-family:monospace">{s["debt"]}x</b></td></tr>'
            f'</table>'
            + th_h + ct_h + alerte +
            '</div>')

def section_block(title, color, items, max_items=6):
    if not items: return ''
    cards = ''.join(stock_card(s, highlight=(s['signal']=='ULTIME')) for s in items[:max_items])
    return (f'<div style="margin-bottom:20px">'
            f'<div style="background:{color};color:#fff;padding:9px 14px;border-radius:6px 6px 0 0;font-size:12px;font-weight:700;display:flex;justify-content:space-between">'
            f'<span>{title}</span><span style="opacity:.8">{len(items)} action{"s" if len(items)>1 else ""}</span></div>'
            f'<div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 6px 6px;padding:10px">{cards}</div>'
            f'</div>')

# ─── BUILD EMAIL ─────────────────────────────────────────────────────────
def build_email(stocks, macro, insights_html, extra_html, date_str, is_sunday=False):
    ultimes  = sorted([s for s in stocks if s['signal']=='ULTIME'],    key=lambda x: -x['qarp'])
    forts    = sorted([s for s in stocks if s['signal']=='FORT'],      key=lambda x: -x['qarp'])
    surv     = sorted([s for s in stocks if s['signal']=='SURVEILLER' and s['score']=='A'], key=lambda x: -x['qarp'])
    suspects = [s for s in stocks if s['beneish'] > -1.78 and s['score'] in ['A','B']]
    macro_verdict, macro_signals = macro_sentiment(macro)
    today_label = "RADAR DU DIMANCHE" if is_sunday else "RADAR DU SOIR"
    today_fr    = datetime.now().strftime('%A %d %B %Y').capitalize()
    # Macro rows
    macro_rows = ''
    for key in ['CAC40','VIX','OR','TAUX','DXY']:
        m = macro.get(key, {})
        if not m.get('value'): continue
        chg = m.get('chg', 0)
        col = '#16a34a' if chg > 0 else '#dc2626'
        macro_rows += (f'<tr><td style="padding:3px 8px;font-size:10px;color:#888">{m["label"]}</td>'
                       f'<td style="padding:3px 8px;font-family:monospace;font-weight:700;font-size:11px">{m["value"]}</td>'
                       f'<td style="padding:3px 8px;color:{col};font-family:monospace;font-size:10px">{("+" if chg>0 else "")}{chg}%</td></tr>')
    # Section influenceurs/web
    insights_section = ''
    if insights_html:
        insights_section = (
            '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin-bottom:16px">'
            '<div style="font-size:11px;font-family:monospace;color:#0f2540;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px">'
            '🎬 Influenceurs · Consensus · Résultats · Pépites</div>'
            f'<div style="font-size:12px;line-height:1.7;color:#333">{insights_html}</div>'
            '</div>'
        )
    # Section extra (marché + small cap)
    extra_section = ''
    if extra_html:
        extra_section = (
            '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin-bottom:16px">'
            '<div style="font-size:11px;font-family:monospace;color:#0f2540;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px">'
            '📊 Marchés · Technique · Opportunités</div>'
            f'<div style="font-size:12px;line-height:1.7;color:#333">{extra_html}</div>'
            '</div>'
        )
    # Section Beneish
    beneish_section = ''
    if suspects:
        cards = ''.join(f'<span style="background:#fef3c7;color:#92400e;padding:2px 8px;border-radius:3px;font-size:10px;margin:2px;display:inline-block">⚠️ {s["ticker"]} (M={s["beneish"]})</span>' for s in suspects[:6])
        beneish_section = (
            f'<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px;margin-bottom:16px">'
            f'<b style="font-size:10px;color:#92400e">⚠️ Beneish M-Score — Vérification recommandée</b>'
            f'<div style="margin-top:6px">{cards}</div>'
            f'<div style="font-size:9px;color:#78350f;margin-top:6px">Vérifier les états financiers primaires avant tout achat.</div>'
            f'</div>'
        )
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f1f5f9;font-family:Helvetica Neue,Arial,sans-serif">
<div style="max-width:680px;margin:0 auto;padding:16px">

<!-- HEADER -->
<div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:12px;padding:20px 24px;margin-bottom:16px">
<div style="font-size:8px;font-family:monospace;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:3px;margin-bottom:6px">VAL.PEA · CABINET QUANTITATIF · SBF250</div>
<div style="font-size:20px;font-weight:700;color:#f0d080;font-family:Georgia,serif;margin-bottom:3px">{today_label} — {today_fr}</div>
<div style="font-size:11px;color:rgba(255,255,255,.6)">{len(stocks)} valeurs · {sum(1 for s in stocks if s["score"]=="A")} Grade A · {len(ultimes)} signaux ultimes</div>
<div style="display:flex;gap:10px;margin-top:12px;flex-wrap:wrap">
{''.join(f'<div style="background:rgba(255,255,255,.08);border-radius:5px;padding:6px 12px;text-align:center"><div style="font-size:16px;font-weight:700;color:#f0d080;font-family:monospace">{v}</div><div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase">{l}</div></div>' for v,l in [(len(ultimes),"Ultimes"),(len(forts),"Forts"),(sum(1 for s in stocks if s["in_zone"]),"En zone"),(len(suspects),"⚠️ Beneish")])}
</div>
</div>

<!-- MACRO -->
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:14px;margin-bottom:16px">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
<b style="font-size:11px;color:#0f2540;text-transform:uppercase;letter-spacing:1px">Contexte Macro</b>
<span style="padding:3px 10px;background:{macro_verdict[2]};color:{macro_verdict[1]};border-radius:4px;font-size:10px;font-weight:700">{macro_verdict[0]}</span>
</div>
<table width="100%" cellpadding="0" cellspacing="0">
<tr><td colspan="3" style="padding-bottom:6px">
{''.join(f'<div style="font-size:9px;color:#444;margin-bottom:2px">{icon} <b>{label}</b> — {desc}</div>' for icon,label,desc in macro_signals)}
</td></tr>
{macro_rows}
</table>
</div>

{insights_section}
{extra_section}
{beneish_section}

{section_block("🚀 Signaux Ultimes — Score ≥70 + décote DCF", "#16a34a", ultimes)}
{section_block("✅ Signaux Forts — Score ≥58 (Grade A/B)", "#d97706", forts)}
{section_block("👁 À Surveiller — Grade A en approche", "#2563eb", surv, max_items=3)}

<!-- RÈGLE DU DIMANCHE -->
<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px;margin-bottom:16px">
<b style="font-size:10px;color:#d97706">⚡ Règle du dimanche</b><br>
<span style="font-size:10px;color:#78350f">Ce mail détecte, il n'ordonne pas. Toute décision : le dimanche matin après le protocole complet — Score A + Zone + Triptyque + Psycho + Taille. Beneish suspect = vérification obligatoire avant achat.</span>
</div>

<div style="text-align:center;font-size:9px;color:#94a3b8;padding:10px">VAL.PEA · Non-conseil · {date_str}</div>
</div></body></html>'''

# ─── SEND ─────────────────────────────────────────────────────────────────
def send_email(subject, html):
    with open('alert_preview.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Preview: alert_preview.html")
    if not GMAIL_USER or not GMAIL_PASS or not EMAIL_TO:
        print("⚠️ SMTP non configuré — preview only")
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

def send_telegram(stocks, macro_verdict, is_sunday):
    if not TG_TOKEN or not TG_CHAT: return
    ultimes  = [s for s in stocks if s['signal']=='ULTIME']
    forts    = [s for s in stocks if s['signal']=='FORT']
    suspects = [s for s in stocks if s['beneish'] > -1.78 and s['score'] in ['A','B']]
    def esc(t): return str(t).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    msg = (f"📊 <b>VAL.PEA — {'Dimanche' if is_sunday else 'Soir'} {datetime.now().strftime('%d/%m')}</b>\n"
           f"Macro: {esc(macro_verdict[0])}\n\n")
    if ultimes:
        msg += f"🚀 <b>ULTIMES ({len(ultimes)})</b>\n"
        for s in ultimes[:5]:
            msg += f" • <b>{esc(s['ticker'])}</b> {esc(s['name'][:12])} — {s['qarp']}/100 — {s['price']}€\n"
    if forts:
        msg += f"\n✅ <b>FORTS ({len(forts)})</b>\n"
        for s in forts[:4]:
            msg += f" • <b>{esc(s['ticker'])}</b> — {s['qarp']}/100\n"
    if suspects:
        msg += f"\n⚠️ <b>Beneish:</b> {esc(', '.join(s['ticker'] for s in suspects[:4]))}"
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
    print(f"VAL.PEA send_alerts_v2 — {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 60)

    if not os.path.exists('index.html'):
        print("❌ index.html introuvable"); sys.exit(1)
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    print("\n📊 Parsing actions...")
    stocks = get_stocks(content)
    print(f"  {len(stocks)} actions parsées")

    print("\n📡 Récupération macro...")
    macro = fetch_macro()
    for k, v in macro.items():
        if v['value']: print(f"  {v['label']}: {v['value']} ({'+' if v['chg']>0 else ''}{v['chg']}%)")

    is_sunday = datetime.now().weekday() == 6
    is_weekend = datetime.now().weekday() in (5, 6)

    # Insights influenceurs + web (toujours si clé dispo)
    print("\n🎬 Insights influenceurs & web...")
    insights_html = fetch_youtube_and_web_insights() if ANTHROPIC_KEY else None
    if insights_html: print(f"  ✅ {len(insights_html)} chars")
    else: print("  ⏭ Ignoré (pas de clé)")

    # Extra sources
    top5 = ', '.join(s['ticker'] for s in sorted(stocks, key=lambda x: x.get('qarp',0), reverse=True)[:5])
    extra_html = fetch_extra_sources(top5) if ANTHROPIC_KEY and is_weekend else None
    if extra_html: print(f"  ✅ Extra: {len(extra_html)} chars")

    date_str   = datetime.now().strftime('%d/%m/%Y %H:%M')
    email_html = build_email(stocks, macro, insights_html, extra_html, date_str, is_sunday)

    ultimes = [s for s in stocks if s['signal']=='ULTIME']
    forts   = [s for s in stocks if s['signal']=='FORT']
    subject = f"VAL.PEA · {datetime.now().strftime('%d/%m')} · {len(ultimes)} ultime(s) · {len(forts)} fort(s)"

    send_email(subject, email_html)
    macro_verdict, _ = macro_sentiment(macro)
    send_telegram(stocks, macro_verdict, is_sunday)

    print("\n✅ Terminé")
