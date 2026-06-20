#!/usr/bin/env python3
"""
VAL.PEA — weekly_digest.py
UN SEUL MAIL — Samedi matin 8h
Contient : réseaux sociaux semaine + signaux BAM + MOAT + sizing Ackman
"""
import re, json, os, sys, time, smtplib, imaplib, email
import urllib.request as ur
import html as html_lib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import decode_header

# ─── CONFIG ───────────────────────────────────────────────────────────────
ANTHROPIC_KEY = (os.environ.get('ANTHROPIC_API_KEY') or '').strip()
GMAIL_USER    = (os.environ.get('GMAIL_USER') or os.environ.get('MAIL_USER') or '').strip()
GMAIL_PASS    = (os.environ.get('GMAIL_PASSWORD') or os.environ.get('MAIL_PASS') or '').strip()
EMAIL_TO      = (os.environ.get('RECIPIENT_EMAIL') or os.environ.get('MAIL_TO') or GMAIL_USER).strip()
TG_TOKEN      = os.environ.get('TELEGRAM_TOKEN', '').strip()
TG_CHAT       = os.environ.get('TELEGRAM_CHAT_ID', '').strip()

print(f"ANTHROPIC: {'✅ OK' if ANTHROPIC_KEY else '❌ MANQUANT'}")
print(f"GMAIL:     {'✅ ' + GMAIL_USER if GMAIL_USER else '❌ MANQUANT'}")
print(f"TO:        {'✅ ' + EMAIL_TO if EMAIL_TO else '❌ MANQUANT'}")

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'

SUBSTACK_FEEDS = [
    ('Rique Trading',       'https://riquetradingetbourse.substack.com/feed'),
    ("L'Analyste Curieux",  'https://analystecurieux.substack.com/feed'),
]

# ─── HTTP ─────────────────────────────────────────────────────────────────
def http_get(url, timeout=10):
    try:
        req = ur.Request(url, headers={'User-Agent': UA})
        with ur.urlopen(req, timeout=timeout) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f'  SKIP {url[:55]}: {e}')
        return ''

# ─── GMAIL NEWSLETTERS ────────────────────────────────────────────────────
def fetch_newsletters():
    if not GMAIL_USER or not GMAIL_PASS:
        print('  ⚠️ Gmail non configuré')
        return []
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_USER, GMAIL_PASS)
        mail.select('INBOX')
        since = (datetime.now() - timedelta(days=7)).strftime('%d-%b-%Y')
        keywords = ['cheron', 'rique', 'finance optimale', 'analyste curieux', 'zonebourse', 'investir']
        results = []
        for kw in keywords:
            try:
                _, msgs = mail.search(None, f'(FROM "{kw}" SINCE {since})')
                if not msgs[0]: continue
                for mid in msgs[0].split()[-1:]:
                    _, data = mail.fetch(mid, '(RFC822)')
                    msg = email.message_from_bytes(data[0][1])
                    subj = ''
                    for part, enc in decode_header(msg['Subject'] or ''):
                        subj += (part.decode(enc or 'utf-8', errors='ignore') if isinstance(part, bytes) else str(part))
                    if any(x in subj.lower() for x in ['promo','réduction','-50%','-40%']):
                        continue
                    body = ''
                    if msg.is_multipart():
                        for p in msg.walk():
                            if p.get_content_type() == 'text/plain':
                                body = p.get_payload(decode=True).decode('utf-8', errors='ignore')
                                break
                            elif p.get_content_type() == 'text/html' and not body:
                                raw = p.get_payload(decode=True).decode('utf-8', errors='ignore')
                                body = re.sub(r'<[^>]+>', ' ', re.sub(r'<style.*?</style>', '', raw, flags=re.DOTALL))
                                body = re.sub(r'\s+', ' ', body).strip()
                    else:
                        body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                    if len(body) > 300:
                        results.append({'source': kw, 'subject': subj[:100], 'body': body[:3000]})
                        print(f'  ✅ Gmail [{kw}]: {subj[:50]}')
            except: pass
        mail.logout()
        return results
    except Exception as e:
        print(f'  Gmail error: {e}')
        return []

# ─── SUBSTACK RSS PUBLIC ──────────────────────────────────────────────────
def fetch_substacks():
    all_items = {}
    for name, url in SUBSTACK_FEEDS:
        xml = http_get(url)
        items = []
        for m in re.finditer(r'<item>(.*?)</item>', xml, re.DOTALL):
            b = m.group(1)
            def g(tag, block=b):
                mx = re.search(r'<' + tag + r'[^>]*>(.*?)</' + tag + r'>', block, re.DOTALL)
                if not mx: return ''
                v = re.sub(r'<!\[CDATA\[|\]\]>', '', mx.group(1))
                return html_lib.unescape(v.strip())
            title = g('title')
            pub   = g('pubDate')[:16]
            desc  = re.sub(r'<[^>]+>', '', g('description'))[:500].strip()
            link  = g('link')
            if title:
                items.append({'title': title, 'pub': pub, 'desc': desc, 'link': link})
        all_items[name] = items[:3]
        if items: print(f'  ✅ Substack [{name}]: {len(items)} articles')
        time.sleep(0.3)
    return all_items

# ─── PARSE STOCKS ─────────────────────────────────────────────────────────
def parse_stocks(html_content):
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
            return [x.strip().strip("'") for x in mx.group(1).split(',') if x.strip().strip("'")]

        price = gn('price'); dcfm = gn('dcfm'); mm200 = gn('mm200')
        upside = round((dcfm - price)/price*100, 1) if price and dcfm else 0
        in_zone = price > 0 and dcfm > 0 and price <= dcfm * 0.88 and gs('score') in ['A','B']
        moat_list = glist('moat')
        roe = gn('roe'); margin = gn('margin'); fcf = gn('fcf')
        debt = gn('debt'); pio = gn('pio'); rsi = gn('rsi')
        o1 = gn('o1'); stop = gn('stop')

        # Score BAM
        q   = 20 if roe>=25 else 16 if roe>=18 else 11 if roe>=12 else 6
        r   = 20 if (margin+fcf)/2>=20 else 15 if (margin+fcf)/2>=12 else 10 if (margin+fcf)/2>=7 else 5
        b   = 20 if debt<=0.5 and pio>=8 else 16 if debt<=1 and pio>=7 else 11 if debt<=2 else 6
        v   = 20 if upside>=35 else 15 if upside>=20 else 10 if upside>=10 else 5 if upside>=0 else 1
        moat_pts = min(10, len(moat_list)*2)
        mnt = 3 + (7 if in_zone else 0) + (7 if price>mm200 and mm200 else 0) + (3 if 25<=rsi<=60 and rsi else 0)
        bam = q + r + b + v + moat_pts + mnt

        # Triptyque
        tri_q = roe >= 15 and margin >= 8 and debt <= 2
        tri_m = len(moat_list) >= 1
        tri_v = in_zone or upside >= 15
        tri_ok = tri_q and tri_m and tri_v

        risk   = price - stop if stop and price > stop else 1
        reward = o1 - price if o1 else 0
        rr     = round(reward/risk, 1) if risk > 0 else 0

        s = {
            'ticker': ticker, 'name': gs('name'), 'sector': gs('sector'),
            'score': gs('score'), 'price': price, 'upside': upside,
            'el': gn('el'), 'eh': gn('eh'), 'stop': stop, 'o1': o1,
            'dcfm': dcfm, 'roe': roe, 'margin': margin, 'fcf': fcf,
            'debt': debt, 'pio': pio, 'rsi': rsi, 'mm200': mm200,
            'in_zone': in_zone, 'moat': moat_list,
            'thesis': gdb('thesis'), 'contra': gdb('contra'),
            'bam': bam, 'tri_ok': tri_ok,
            'tri_q': tri_q, 'tri_m': tri_m, 'tri_v': tri_v,
            'rr': rr,
        }
        sig = ('ULTIME' if bam>=85 and in_zone and upside>5
               else 'FORT' if bam>=68 and gs('score') in ['A','B'] and upside>5
               else 'SURVEILLER' if bam>=55 and gs('score')=='A' else None)
        s['signal'] = sig
        stocks.append(s)
    return sorted(stocks, key=lambda x: -x['bam'])

# ─── RÉSUMÉ RÉSEAUX SOCIAUX IA ────────────────────────────────────────────
def fetch_social_summary(newsletters, substacks):
    if not ANTHROPIC_KEY: return None
    today = datetime.now().strftime('%d/%m/%Y')
    week_start = (datetime.now() - timedelta(days=7)).strftime('%d/%m/%Y')

    # Contexte newsletters Gmail
    nl_ctx = ''
    for nl in newsletters[:4]:
        nl_ctx += f"\n\nNEWSLETTER [{nl['source']}] — {nl['subject']}\n{nl['body'][:2500]}"

    # Contexte Substack public
    for name, articles in substacks.items():
        if articles:
            nl_ctx += f"\n\nSUBSTACK [{name}]:"
            for a in articles:
                nl_ctx += f"\n• {a['pub']} — {a['title']}\n  {a['desc'][:400]}"

    prompt = f"""Date: {today}. Semaine analysée: {week_start} → {today}.
Tu es analyste pour une investisseuse PEA française. Fais le résumé de la semaine.

SOURCES À ANALYSER (cherche sur le web ET utilise le contenu ci-dessous) :

1. GUILLAUME FOURNIER — YouTube @GuillaumeFournier_Invest + site financeoptimale.fr
   → Dernière vidéo publiée cette semaine : titre + actions analysées + verdict

2. RIQUE TRADING — YouTube @riquetrading + Substack riquetradingetbourse.substack.com
   → Dernière vidéo + dernier article Substack : actions PEA mentionnées + prix cibles

3. NICOLAS CHÉRON — YouTube @NicolasCheron + X @NCheron_bourse + zonebourse.com
   → Point de marché bimensuel : TOUTES les actions passées en revue + verdict technique
   → Posts X de la semaine : alertes, signaux, analyses

4. JEAN-BENOÎT GAMBET — Instagram @jeanbenoit_gambet + LinkedIn Eiffel Investment Group
   → Posts récents : secteurs favoris, convictions, actions citées

5. L'ANALYSTE CURIEUX — X @analystecurieux + Substack analystecurieux.substack.com + Instagram
   → Fiches entreprises publiées cette semaine : analyse MOAT + valorisation + juste prix

CONTENU REÇU (newsletters Gmail + Substack):{nl_ctx if nl_ctx else ' Aucun contenu reçu cette semaine.'}

FORMAT HTML STRICT — pas de markdown, pas d'astérisques :

<h4>📺 Guillaume Fournier</h4>
<b>Sentiment :</b> <span style="color:#16a34a">BULLISH</span> / <span style="color:#dc2626">BEARISH</span> / <span style="color:#d97706">NEUTRE</span><br>
<b>Activité :</b> [titre vidéo/article exact + date]<br>
<b>Actions analysées :</b><ul>
<li><b>TICKER</b> — [verdict] — [raison chiffrée]</li>
</ul>

<h4>📈 Rique Trading</h4>
[même structure + prix cibles PER si disponibles]

<h4>📊 Nicolas Chéron</h4>
[même structure + TOUTES actions mentionnées dans point de marché]

<h4>👔 Jean-Benoît Gambet</h4>
[même structure]

<h4>🔍 L'Analyste Curieux</h4>
[même structure + MOAT identifié + zone d'achat]

<h4>🎯 Synthèse de la semaine</h4>
<b>Tickers cités par 2+ influenceurs :</b> [liste en gras]<br>
<b>Consensus :</b> [BULLISH/BEARISH/NEUTRE + raison]<br>
<b>Pépite PEA :</b> [1 action sous-évaluée avec MOAT]<br>
<b>À éviter :</b> [1 action sur laquelle plusieurs sont négatifs]

Si info non trouvée : écrire <i>Non trouvé publiquement cette semaine</i>. Ne pas inventer."""

    try:
        payload = json.dumps({
            'model': 'claude-sonnet-4-6',
            'max_tokens': 2500,
            'tools': [{'type': 'web_search_20250305', 'name': 'web_search'}],
            'messages': [{'role': 'user', 'content': prompt}]
        }).encode()
        req = ur.Request('https://api.anthropic.com/v1/messages', data=payload,
            headers={'Content-Type':'application/json','x-api-key':ANTHROPIC_KEY,
                     'anthropic-version':'2023-06-01','anthropic-beta':'web-search-2025-03-05'})
        with ur.urlopen(req, timeout=90) as r:
            data = json.loads(r.read())
        text = ''.join(b.get('text','') for b in data.get('content',[]) if b.get('type')=='text')
        print(f'  ✅ Résumé social: {len(text)} chars')
        return text.strip() or None
    except Exception as e:
        print(f'  ❌ Social error: {e}')
        return None

# ─── ANALYSE IA TOP 3 ─────────────────────────────────────────────────────
def ia_analyse(s):
    if not ANTHROPIC_KEY: return ''
    moat_str = ', '.join(s['moat'][:3]) if s['moat'] else 'non identifié'
    prompt = (f"Note investissement PEA pour {s['name']} ({s['ticker']}).\n"
              f"ROE {s['roe']}%, Marge {s['margin']}%, Dette {s['debt']}x, "
              f"Piotroski {int(s['pio'])}/9, Upside DCF {s['upside']}%, MOAT: {moat_str}\n\n"
              "Format 4 lignes:\n"
              "VERDICT: [ACHETER/ATTENDRE/ÉVITER] à [X]€\n"
              "MOAT: [avantage durable — 1 phrase chiffrée]\n"
              "RISQUE: [principal risque concret]\n"
              "SIGNAL: [ENTRER/CONSERVER/SORTIR] — [raison courte]")
    try:
        payload = json.dumps({'model':'claude-sonnet-4-6','max_tokens':180,
            'messages':[{'role':'user','content':prompt}]}).encode()
        req = ur.Request('https://api.anthropic.com/v1/messages', data=payload,
            headers={'Content-Type':'application/json','x-api-key':ANTHROPIC_KEY,'anthropic-version':'2023-06-01'})
        with ur.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
        return d['content'][0]['text'].strip()
    except Exception as e:
        print(f'  IA {s["ticker"]}: {e}')
        return ''

# ─── MACRO ────────────────────────────────────────────────────────────────
def fetch_macro():
    tickers = {
        'VIX':   ('^VIX',     'VIX'),
        'CAC40': ('^FCHI',    'CAC 40'),
        'OR':    ('GC=F',     'Or $/oz'),
        'TAUX':  ('^TNX',     'Taux US 10Y'),
        'DXY':   ('DX-Y.NYB', 'Dollar Index'),
    }
    macro = {}
    for key, (yf, label) in tickers.items():
        try:
            url = f"https://query2.finance.yahoo.com/v8/finance/chart/{yf}?interval=1d&range=5d"
            req = ur.Request(url, headers={'User-Agent': UA})
            with ur.urlopen(req, timeout=8) as r:
                data = json.loads(r.read())
            meta  = data['chart']['result'][0]['meta']
            price = meta.get('regularMarketPrice', 0)
            prev  = meta.get('previousClose', price)
            chg   = round((price-prev)/prev*100, 2) if prev else 0
            macro[key] = {'label': label, 'value': round(price,2), 'chg': chg}
        except:
            macro[key] = {'label': label, 'value': 0, 'chg': 0}
        time.sleep(0.2)
    return macro

# ─── CARTE ACTION ─────────────────────────────────────────────────────────
def stock_card(s, ia_note=''):
    bam = s['bam']
    bam_col = '#16a34a' if bam>=85 else '#d97706' if bam>=68 else '#2563eb'
    grade_col = {'A':'#16a34a','B':'#d97706','C':'#6b7280','D':'#dc2626'}.get(s['score'],'#6b7280')
    upside_str = ('+' if s['upside']>0 else '') + str(s['upside']) + '%'
    upside_col = '#16a34a' if s['upside']>15 else '#d97706' if s['upside']>0 else '#dc2626'

    # Triptyque
    tri_items = [
        ('✅' if s['tri_q'] else '❌', 'Qualité'),
        ('✅' if s['tri_m'] else '❌', 'MOAT'),
        ('✅' if s['tri_v'] else '❌', 'Valorisation'),
    ]
    tri_html = ' &nbsp; '.join(f'{icon} <b>{lbl}</b>' for icon, lbl in tri_items)
    tri_col = '#16a34a' if s['tri_ok'] else '#dc2626'
    tri_lbl = '🟢 TRIPTYQUE COMPLET' if s['tri_ok'] else '🔴 Triptyque incomplet'

    # MOAT badges
    moat_html = ''
    if s['moat']:
        moat_html = '<div style="margin:6px 0">'
        for m in s['moat'][:5]:
            moat_html += f'<span style="background:#dbeafe;color:#1d4ed8;padding:2px 8px;border-radius:3px;font-size:9px;margin:1px;display:inline-block">{m}</span>'
        moat_html += '</div>'
    else:
        moat_html = '<div style="font-size:9px;color:#dc2626;margin:4px 0">⚠️ MOAT non renseigné</div>'

    # Thesis / Contra
    thesis_html = ''
    if s.get('thesis'):
        thesis_html = (f'<div style="margin-top:6px;padding:8px;background:#f0fdf4;border-left:3px solid #16a34a;font-size:10px;color:#1a4730;line-height:1.5">'
                       f'<b style="font-size:8px;text-transform:uppercase;color:#16a34a">Thèse d\'investissement</b><br>{s["thesis"][:200]}</div>')
    contra_html = ''
    if s.get('contra'):
        contra_html = (f'<div style="margin-top:4px;padding:8px;background:#fff5f5;border-left:3px solid #dc2626;font-size:10px;color:#7c2d2d;line-height:1.5">'
                       f'<b style="font-size:8px;text-transform:uppercase;color:#dc2626">Risque principal</b><br>{s["contra"][:180]}</div>')

    # IA
    ia_html = ''
    if ia_note:
        ia_html = (f'<div style="margin-top:6px;background:#f0f9ff;border:1px solid #bae6fd;border-radius:6px;padding:8px;font-size:10px">'
                   f'<b style="color:#0369a1">🤖 Analyse IA</b><br>'
                   f'<pre style="font-family:Arial;margin:4px 0;white-space:pre-wrap;font-size:10px;color:#1e3a5f">{ia_note}</pre></div>')

    # R/R calcul
    risk = s['price'] - s['stop'] if s['stop'] and s['price'] > s['stop'] else 1
    o1_pct = round((s['o1']-s['price'])/s['price']*100) if s['o1'] and s['price'] else 0

    return f'''<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:12px;border-left:4px solid {bam_col}">
<table width="100%" cellpadding="0" cellspacing="0"><tr>
<td style="vertical-align:top">
<div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:4px">
<span style="background:{grade_col};color:#fff;padding:2px 8px;border-radius:3px;font-size:10px;font-weight:700">{s["score"]}</span>
<b style="font-size:16px;font-family:monospace;color:#0f2540">{s["ticker"]}</b>
<span style="color:#888;font-size:11px">{s["name"][:22]}</span>
{('<span style="background:#dcfce7;color:#16a34a;padding:1px 6px;border-radius:3px;font-size:9px;font-weight:700">EN ZONE</span>' if s["in_zone"] else '')}
</div>
<div style="font-size:9px;color:#94a3b8">{s.get("sector","")[:35]}</div>
</td>
<td style="text-align:right;min-width:110px;vertical-align:top">
<div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:8px;padding:10px 14px;text-align:center">
<div style="font-size:9px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:1px">B.A.M</div>
<div style="font-size:28px;font-weight:700;color:{bam_col};font-family:monospace">{bam}</div>
<div style="font-size:8px;color:rgba(255,255,255,.3)">/120</div>
<div style="font-size:9px;color:#f0d080;font-weight:700;margin-top:2px">{s["signal"] or "—"}</div>
</div>
</td>
</tr></table>

<div style="background:{tri_col}15;border:1px solid {tri_col}40;border-radius:6px;padding:6px 10px;margin:8px 0;font-size:9px">
<b style="color:{tri_col}">{tri_lbl}</b> &nbsp; {tri_html}
</div>

{moat_html}

<table width="100%" cellpadding="3" cellspacing="0" style="font-size:10px;margin:6px 0">
<tr>
<td style="color:#888;width:25%">Cours</td><td><b style="font-family:monospace">{s["price"]}€</b></td>
<td style="color:#888;width:25%">Zone achat</td><td><b style="font-family:monospace">{s["el"]}–{s["eh"]}€</b></td>
</tr><tr>
<td style="color:#888">Stop</td><td><b style="color:#dc2626;font-family:monospace">{s["stop"]}€</b></td>
<td style="color:#888">Objectif 1</td><td><b style="color:#16a34a;font-family:monospace">{s["o1"]}€ (+{o1_pct}%)</b></td>
</tr><tr>
<td style="color:#888">Upside DCF</td><td><b style="color:{upside_col}">{upside_str}</b></td>
<td style="color:#888">R/R</td><td><b style="color:{'#16a34a' if s['rr']>=1.5 else '#d97706'}">{s["rr"]}x</b></td>
</tr><tr>
<td style="color:#888">ROE</td><td><b>{s["roe"]}%</b></td>
<td style="color:#888">Piotroski</td><td><b>{int(s["pio"])}/9</b></td>
</tr><tr>
<td style="color:#888">Marge nette</td><td><b>{s["margin"]}%</b></td>
<td style="color:#888">Dette/EBITDA</td><td><b style="color:{'#16a34a' if s['debt']<=1 else '#d97706' if s['debt']<=2 else '#dc2626'}">{s["debt"]}x</b></td>
</tr>
</table>
{thesis_html}{contra_html}{ia_html}
</div>'''

# ─── BUILD EMAIL ──────────────────────────────────────────────────────────
def build_email(stocks, macro, social_html, date_fr):
    ultimes  = [s for s in stocks if s['signal']=='ULTIME']
    forts    = [s for s in stocks if s['signal']=='FORT']
    surv     = [s for s in stocks if s['signal']=='SURVEILLER' and s['score']=='A']
    triptyques = [s for s in stocks if s['tri_ok'] and s['signal'] in ('ULTIME','FORT')]

    # IA sur top 3
    ia_notes = {}
    if ANTHROPIC_KEY:
        print('\n🤖 Analyse IA top 3...')
        for s in (ultimes + forts)[:3]:
            note = ia_analyse(s)
            if note: ia_notes[s['ticker']] = note
            time.sleep(1.5)

    # Macro
    vix = macro.get('VIX',{}).get('value',20)
    macro_color = '#16a34a' if vix < 15 else '#d97706' if vix < 22 else '#dc2626'
    macro_label = 'FAVORABLE' if vix < 15 else 'NEUTRE' if vix < 22 else 'PRUDENCE'
    macro_rows = ''
    for key in ['CAC40','VIX','OR','TAUX','DXY']:
        m = macro.get(key,{})
        if not m.get('value'): continue
        col = '#16a34a' if m['chg']>0 else '#dc2626'
        sign = '+' if m['chg']>0 else ''
        macro_rows += (f'<tr><td style="padding:3px 8px;font-size:11px;color:#666">{m["label"]}</td>'
                       f'<td style="padding:3px 8px;font-family:monospace;font-weight:700">{m["value"]}</td>'
                       f'<td style="padding:3px 8px;color:{col};font-family:monospace">{sign}{m["chg"]}%</td></tr>')

    # Section signaux
    def sig_section(title, col, items, max_n=5):
        if not items: return ''
        cards = ''.join(stock_card(s, ia_notes.get(s['ticker'],'')) for s in items[:max_n])
        return (f'<div style="margin-bottom:20px">'
                f'<div style="background:{col};color:#fff;padding:10px 16px;border-radius:8px 8px 0 0;'
                f'font-size:12px;font-weight:700;display:flex;justify-content:space-between">'
                f'<span>{title}</span><span style="opacity:.7">{len(items)} valeur{"s" if len(items)>1 else ""}</span></div>'
                f'<div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 8px 8px;padding:12px">{cards}</div>'
                f'</div>')

    # Protocole dimanche
    proto_html = ''
    if triptyques:
        proto_html = '<div style="background:#fff;border:1px solid #dcfce7;border-radius:10px;padding:16px;margin-bottom:16px">'
        proto_html += '<div style="font-size:11px;font-weight:700;color:#16a34a;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">🟢 Protocole B.A.M — Triptyque complet</div>'
        for s in triptyques[:3]:
            alloc = min(15, round(s['bam']/120*20))
            proto_html += (f'<div style="border:1px solid #dcfce7;border-radius:6px;padding:10px;margin-bottom:8px;background:#f0fdf4">'
                          f'<div style="display:flex;justify-content:space-between;align-items:center">'
                          f'<b style="font-family:monospace">{s["ticker"]}</b> <span style="color:#888;font-size:11px">{s["name"][:18]}</span>'
                          f'<span style="background:#16a34a;color:#fff;padding:2px 8px;border-radius:3px;font-size:10px">BAM {s["bam"]}/120 · {alloc}% max</span></div>'
                          f'<div style="font-size:10px;color:#555;margin-top:6px">'
                          f'Zone {s["el"]}–{s["eh"]}€ · Stop {s["stop"]}€ · Upside +{s["upside"]}% · R/R {s["rr"]}x</div></div>')
        proto_html += '</div>'

    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  h4{{color:#0f2540;font-size:13px;margin:14px 0 6px;border-bottom:2px solid #f0d080;padding-bottom:4px;font-weight:700}}
  ul{{margin:4px 0 10px;padding-left:18px}} li{{margin:4px 0;font-size:12px;line-height:1.5}}
  b{{color:#0f2540}} i{{color:#888}}
</style>
</head>
<body style="margin:0;padding:0;background:#f1f5f9;font-family:Helvetica Neue,Arial,sans-serif">
<div style="max-width:680px;margin:0 auto;padding:16px">

<!-- HEADER -->
<div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:12px;padding:24px;margin-bottom:16px">
<div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:3px;margin-bottom:8px">
VAL.PEA · MÉTHODE B.A.M · BUFFETT · ACKMAN · MUNGER</div>
<div style="font-size:22px;font-weight:700;color:#f0d080;font-family:Georgia,serif">📊 Revue hebdomadaire</div>
<div style="font-size:13px;color:rgba(255,255,255,.7);margin-top:4px">{date_fr}</div>
<div style="display:flex;gap:12px;margin-top:14px;flex-wrap:wrap">
{"".join(f'<div style="background:rgba(255,255,255,.1);border-radius:6px;padding:8px 14px;text-align:center"><div style="font-size:20px;font-weight:700;color:#f0d080;font-family:monospace">{v}</div><div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase;margin-top:2px">{l}</div></div>' for v,l in [(len(stocks),"Valeurs"),(len(ultimes),"Ultime"),(len(forts),"Forts"),(len(triptyques),"Triptyques")])}
</div>
</div>

<!-- MACRO -->
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:16px">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
<b style="font-size:11px;color:#0f2540;text-transform:uppercase;letter-spacing:1px">Contexte macro</b>
<span style="background:{macro_color}20;color:{macro_color};border:1px solid {macro_color}40;padding:3px 10px;border-radius:4px;font-size:10px;font-weight:700">{macro_label}</span>
</div>
<table width="100%" cellpadding="0" cellspacing="0">{macro_rows}</table>
</div>

<!-- RÉSEAUX SOCIAUX -->
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:16px">
<div style="background:#0f2540;color:#f0d080;padding:10px 14px;border-radius:6px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:14px">
📱 Réseaux sociaux & newsletters — semaine du {(datetime.now()-timedelta(days=7)).strftime("%d/%m")} au {datetime.now().strftime("%d/%m/%Y")}
</div>
<div style="font-size:12px;line-height:1.8;color:#333">
{social_html if social_html else '<i style="color:#888">Résumé non disponible cette semaine.</i>'}
</div>
</div>

{proto_html}

{sig_section("🚀 Signaux ULTIMES — BAM ≥85 · Triptyque · Zone DCF", "#16a34a", ultimes)}
{sig_section("✅ Signaux FORTS — BAM ≥68 (Grade A/B)", "#d97706", forts)}
{sig_section("👁 À Surveiller — Grade A en approche", "#2563eb", surv, max_n=3)}

<!-- RÈGLE FONDAMENTALE -->
<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:14px;margin-bottom:16px">
<b style="font-size:10px;color:#d97706">📐 Règle B.A.M — Décision du week-end uniquement</b><br>
<span style="font-size:10px;color:#78350f;line-height:1.6">
Triptyque complet requis : Qualité (ROE≥15%·Dette≤2x·Pio≥7) + MOAT identifié + Valorisation (zone DCF ou upside≥15%).
Max 15 lignes en portefeuille. Sizing max 15% par position. Jamais en semaine, jamais sous pression.
</span>
</div>

<div style="text-align:center;font-size:9px;color:#94a3b8;padding:8px">
VAL.PEA · Méthode B.A.M · {date_fr} · Non-conseil en investissement
</div>
</div></body></html>'''

# ─── SEND ─────────────────────────────────────────────────────────────────
def send(subject, html):
    with open('weekly_preview.html','w',encoding='utf-8') as f:
        f.write(html)
    print('  Preview: weekly_preview.html')
    if not GMAIL_USER or not EMAIL_TO:
        print('  ⚠️ SMTP non configuré'); return False
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From']    = GMAIL_USER
        msg['To']      = EMAIL_TO
        msg.attach(MIMEText(html,'html','utf-8'))
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as s:
            s.login(GMAIL_USER, GMAIL_PASS)
            s.sendmail(GMAIL_USER, EMAIL_TO.split(','), msg.as_string())
        print(f'  ✅ Mail envoyé à {EMAIL_TO}')
        return True
    except Exception as e:
        print(f'  ❌ SMTP: {e}'); return False

def send_telegram_summary(stocks, date_str):
    if not TG_TOKEN or not TG_CHAT: return
    ultimes = [s for s in stocks if s['signal']=='ULTIME']
    forts   = [s for s in stocks if s['signal']=='FORT']
    tri     = [s for s in stocks if s['tri_ok']]
    def esc(t): return str(t).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    msg = f"📊 <b>VAL.PEA — Revue {date_str}</b>\n\n"
    if tri:
        msg += f"🟢 <b>Triptyques OK ({len(tri)})</b>\n"
        for s in tri[:3]: msg += f" • <b>{esc(s['ticker'])}</b> — BAM {s['bam']}/120 · Upside +{s['upside']}%\n"
    if ultimes:
        msg += f"\n🚀 <b>ULTIMES ({len(ultimes)})</b>\n"
        for s in ultimes[:4]: msg += f" • <b>{esc(s['ticker'])}</b> {esc(s['name'][:12])} · {s['bam']}/120\n"
    if forts:
        msg += f"\n✅ <b>FORTS ({len(forts)})</b>\n"
        for s in forts[:3]: msg += f" • <b>{esc(s['ticker'])}</b> · {s['bam']}/120\n"
    payload = json.dumps({'chat_id':TG_CHAT,'text':msg[:3800],'parse_mode':'HTML'})
    try:
        req = ur.Request(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
            data=payload.encode(), headers={'Content-Type':'application/json'})
        ur.urlopen(req, timeout=10)
        print('  ✅ Telegram envoyé')
    except Exception as e:
        print(f'  ⚠️ Telegram: {e}')

# ─── MAIN ─────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    now = datetime.now()
    print('='*60)
    print(f'VAL.PEA Weekly Digest — {now.strftime("%d/%m/%Y %H:%M")}')
    print('='*60)

    MONTHS = {'January':'janvier','February':'février','March':'mars','April':'avril',
              'May':'mai','June':'juin','July':'juillet','August':'août',
              'September':'septembre','October':'octobre','November':'novembre','December':'décembre'}
    date_fr = now.strftime('%A %d %B %Y').capitalize()
    for en, fr in MONTHS.items(): date_fr = date_fr.replace(en, fr)

    if not os.path.exists('index.html'):
        print('❌ index.html introuvable'); sys.exit(1)
    with open('index.html','r',encoding='utf-8') as f:
        content = f.read()

    print('\n📊 Parsing stocks...')
    stocks = parse_stocks(content)
    print(f'  {len(stocks)} actions · {sum(1 for s in stocks if s["signal"]=="ULTIME")} ULTIME · {sum(1 for s in stocks if s["tri_ok"])} Triptyques OK')

    print('\n📡 Macro...')
    macro = fetch_macro()

    print('\n📧 Newsletters Gmail...')
    newsletters = fetch_newsletters()

    print('\n📖 Substack RSS...')
    substacks = fetch_substacks()

    print('\n📱 Résumé réseaux sociaux...')
    social_html = fetch_social_summary(newsletters, substacks)

    print('\n📨 Construction mail...')
    html = build_email(stocks, macro, social_html, date_fr)

    n_sig = sum(1 for s in stocks if s['signal'] in ('ULTIME','FORT'))
    n_tri = sum(1 for s in stocks if s['tri_ok'])
    subject = f"VAL.PEA · Revue {now.strftime('%d/%m')} · {n_sig} signaux B.A.M · {n_tri} Triptyque{'s' if n_tri!=1 else ''}"

    send(subject, html)
    send_telegram_summary(stocks, now.strftime('%d/%m'))
    print('\n✅ Done')
