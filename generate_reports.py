#!/usr/bin/env python3
"""
VAL.PEA — generate_reports.py
Mail enrichi complet :
- Newsletter Chéron (Gmail IMAP bimensuelle)
- Réseaux sociaux : Fournier, Rique Trading, Chéron, Gambet, L'Analyste Curieux
- RSS marchés
- IA analyse top signaux B.A.M
- Résumé semaine complet
"""
import re, json, sys, os, time, html as html_lib, imaplib, email
from datetime import datetime, timedelta
from urllib.request import urlopen, Request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import decode_header

# ─── CONFIG ──────────────────────────────────────────────────────────────
ANTHROPIC_KEY = (os.environ.get('ANTHROPIC_API_KEY') or '').strip()
SMTP_USER = (os.environ.get('MAIL_USER') or os.environ.get('GMAIL_USER') or '').strip()
SMTP_PASS = (os.environ.get('MAIL_PASS') or os.environ.get('GMAIL_PASSWORD') or '').strip()
SMTP_TO   = (os.environ.get('MAIL_TO') or os.environ.get('RECIPIENT_EMAIL') or SMTP_USER or '').strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

print(f"ANTHROPIC: {'OK ' + str(len(ANTHROPIC_KEY)) + ' chars' if ANTHROPIC_KEY else 'MANQUANT'}")
print(f"MAIL_USER: {SMTP_USER or 'MANQUANT'}")
print(f"MAIL_PASS: {'OK' if SMTP_PASS else 'MANQUANT'}")
print(f"MAIL_TO:   {SMTP_TO or 'MANQUANT'}")

# ─── SOURCES RÉSEAUX SOCIAUX ─────────────────────────────────────────────
INFLUENCEURS = {
    'Guillaume Fournier': {
        'youtube': 'https://www.youtube.com/@GuillaumeFournier_Invest/videos',
        'instagram': 'guillaumefournier_invest',
        'x': 'GFournier_Inv',
        'desc': 'Finance Optimale · Méthode B.A.M · Quality Investing'
    },
    'Rique Trading': {
        'youtube': 'https://www.youtube.com/@riquetrading/videos',
        'instagram': 'rique.trading',
        'newsletter_gmail': 'rique',
        'desc': 'Analyse technique + fondamentale · PEA sous-évalués · Newsletter'
    },
    'Nicolas Chéron': {
        'youtube': 'https://www.youtube.com/@NicolasCheron/videos',
        'x': 'NCheron_bourse',
        'zonebourse': True,
        'newsletter_gmail': 'cheron',  # mot-clé pour trouver sa newsletter dans Gmail
        'desc': 'Macro + technique + sentiment · ZoneBourse · Newsletter bimensuelle'
    },
    'Jean-Benoît Gambet': {
        'instagram': 'jeanbenoit_gambet',
        'desc': 'Institutionnel · Qualité + valorisation'
    },
    "L'Analyste Curieux": {
        'instagram': 'lanalystecurieux',
        'x': 'AnalysteCurieux',
        'desc': 'Analyse actions individuelles · Décryptage fondamental'
    },
}

# Newsletters Gmail à lire
NEWSLETTERS_SOURCES = [
    'cheron',
    'rique',
    'zonebourse',
    'lesechos',
    'investir',
    'boursorama',
    'reuters',
    'finance optimale',
    'analyste curieux',
]

RSS_FEEDS = [
    ('Les Echos',   'https://www.lesechos.fr/rss/rss_finance.xml'),
    ('Reuters FR',  'https://feeds.reuters.com/reuters/businessNews'),
    ('ZoneBourse',  'https://www.zonebourse.com/rss/news-bourse/'),
    ('Boursorama',  'https://www.boursorama.com/bourse/actualites/rss/une'),
    ('Investir',    'https://investir.lesechos.fr/rss/actualites.xml'),
]

# ─── HTTP ────────────────────────────────────────────────────────────────
def http_get(url, timeout=10):
    try:
        req = Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
        with urlopen(req, timeout=timeout) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f'  SKIP {url[:60]}: {e}')
        return ''

# ─── GMAIL IMAP — newsletters + Chéron ───────────────────────────────────
def fetch_gmail_newsletters(days_back=7):
    """Lit toutes les newsletters financières dans Gmail des X derniers jours"""
    if not SMTP_USER or not SMTP_PASS:
        return []
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(SMTP_USER, SMTP_PASS)
        mail.select('INBOX')
        since = (datetime.now() - timedelta(days=days_back)).strftime('%d-%b-%Y')
        newsletters = []

        for source_kw in NEWSLETTERS_SOURCES:
            try:
                _, msgs = mail.search(None, f'(FROM "{source_kw}" SINCE {since})')
                if not msgs[0]: continue
                for msg_id in msgs[0].split()[-1:]:  # dernier uniquement
                    try:
                        _, msg_data = mail.fetch(msg_id, '(RFC822)')
                        msg_obj = email.message_from_bytes(msg_data[0][1])
                        # Sujet
                        subj_raw = msg_obj['Subject'] or ''
                        subj_parts = decode_header(subj_raw)
                        subj = ''
                        for part, enc in subj_parts:
                            if isinstance(part, bytes):
                                subj += part.decode(enc or 'utf-8', errors='ignore')
                            else:
                                subj += str(part)
                        # Filtre promo
                        if any(x in subj.lower() for x in ['promo','réduction','offre','-40%']):
                            continue
                        # Corps
                        body = ''
                        if msg_obj.is_multipart():
                            for part in msg_obj.walk():
                                ct = part.get_content_type()
                                if ct == 'text/plain':
                                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                                    break
                                elif ct == 'text/html' and not body:
                                    html_raw = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                                    body = re.sub(r'<[^>]+>', ' ', re.sub(r'<style[^>]*>.*?</style>', '', html_raw, flags=re.DOTALL))
                                    body = re.sub(r'\s+', ' ', body).strip()
                        else:
                            body = msg_obj.get_payload(decode=True).decode('utf-8', errors='ignore')

                        if len(body) > 300:
                            newsletters.append({
                                'source': source_kw,
                                'subject': subj[:120],
                                'body': body[:4000],
                                'date': msg_obj['Date'] or ''
                            })
                            print(f'  ✅ Gmail [{source_kw}]: {subj[:60]}')
                    except: pass
            except: pass

        mail.logout()
        print(f'  Total newsletters Gmail: {len(newsletters)}')
        return newsletters
    except Exception as e:
        print(f'  Gmail IMAP error: {e}')
        return []

# ─── RSS ─────────────────────────────────────────────────────────────────
def fetch_rss():
    all_news = []
    for source, url in RSS_FEEDS:
        xml = http_get(url)
        if not xml: continue
        for m in re.finditer(r'<item>(.*?)</item>', xml, re.DOTALL):
            block = m.group(1)
            def get(tag):
                mx = re.search(r'<' + tag + r'[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</' + tag + r'>', block, re.DOTALL)
                return html_lib.unescape(mx.group(1).strip()) if mx else ''
            title = get('title')
            if title:
                all_news.append({
                    'title': title,
                    'link': get('link') or get('guid'),
                    'pub': (get('pubDate') or '')[:16],
                    'desc': re.sub(r'<[^>]+>', '', get('description'))[:200],
                    'source': source
                })
        time.sleep(0.3)
    print(f'  Total RSS: {len(all_news)} articles')
    return all_news

# ─── YOUTUBE ─────────────────────────────────────────────────────────────
def fetch_youtube(url, max_videos=3):
    content = http_get(url)
    if not content: return []
    videos = []
    for m in re.finditer(r'"title":\{"runs":\[\{"text":"([^"]+)"', content):
        t = m.group(1)
        if len(t) > 10 and t not in [v['title'] for v in videos]:
            videos.append({'title': t})
            if len(videos) >= max_videos: break
    return videos

# ─── IA — RÉSUMÉ RÉSEAUX SOCIAUX COMPLET ─────────────────────────────────
def fetch_social_media_summary(newsletters):
    """Claude fait une recherche web sur tous les influenceurs + résume les newsletters"""
    if not ANTHROPIC_KEY: return None

    today = datetime.now().strftime('%d/%m/%Y')

    # Contenu newsletters pour contexte
    nl_context = ''
    for nl in newsletters[:5]:
        nl_context += f"\n\nNEWSLETTER [{nl['source']}] — {nl['subject']}\n{nl['body'][:2000]}"

    prompt = f"""Date: {today}. Tu es un analyste financier pour une investisseuse PEA française.

MISSION : Résumé COMPLET de la semaine sur les réseaux sociaux et newsletters financières françaises.

SOURCES À CHERCHER (7 derniers jours uniquement — semaine en cours) :
Si un influenceur n'a rien publié cette semaine, indiquer clairement 'Pas de publication cette semaine'.

1. GUILLAUME FOURNIER (@GuillaumeFournier_Invest YouTube, Instagram, Finance Optimale)
   → Ses dernières vidéos et posts : actions analysées, sentiment, méthode B.A.M appliquée

2. RIQUE TRADING (@riquetrading YouTube, @rique.trading Instagram)
   → Analyses techniques + fondamentales récentes, actions mentionnées
   → NEWSLETTER (contenu ci-dessous si disponible dans Gmail)

3. NICOLAS CHÉRON (@NCheron_bourse sur X, YouTube, ZoneBourse)
   → Posts X cette semaine, analyses publiées sur ZoneBourse
   → VIDÉO YOUTUBE bimensuelle : analyse approfondie d'actions du marché français
   → NEWSLETTER BIMENSUELLE (contenu ci-dessous si disponible dans Gmail)

4. JEAN-BENOÎT GAMBET (@jeanbenoit_gambet Instagram)
   → Posts récents, actions ou secteurs mentionnés

5. L'ANALYSTE CURIEUX (@lanalystecurieux Instagram + X)
   → Analyses actions publiées cette semaine

{('CONTENU NEWSLETTERS GMAIL REÇUES :' + nl_context) if nl_context else ''}

FORMAT HTML PUR — pas de markdown, pas d'astérisques, pas de tirets ---
Utilise uniquement des balises HTML : <h4>, <b>, <span>, <div>, <ul>, <li>

Pour chaque influenceur, structure OBLIGATOIRE :
<h4>📱 [Nom] — <span style="color:#16a34a">BULLISH</span> ou <span style="color:#dc2626">BEARISH</span> ou <span style="color:#d97706">NEUTRE</span></h4>
<b>Activité cette semaine :</b> [vidéo/post/reel publié — titre exact + date]<br>
<b>Actions analysées :</b>
<ul>
<li><b>TICKER (Nom)</b> — [verdict BUY/HOLD/SELL] — [raison en 1 phrase chiffrée]</li>
</ul>
<b>Message clé :</b> [1 phrase résumant le sentiment]

<h4>📱 Guillaume Fournier</h4>
[Cherche sur YouTube "Guillaume Fournier Finance Optimale" + Instagram + site financeoptimale.fr]

<h4>📱 Rique Trading</h4>
[Cherche sur YouTube "Rique Trading" + Instagram rique.trading + investing.com]

<h4>📱 Nicolas Chéron</h4>
[Cherche sur YouTube "Nicolas Cheron point de marche" + X @NCheron_bourse + zonebourse.com/nicolas-cheron]
[IMPORTANT : Chéron publie une vidéo YouTube bimensuelle "Point de marché" avec revue détaillée de 5-10 actions — extraire TOUTES les actions mentionnées avec leur verdict]

<h4>📱 Jean-Benoît Gambet</h4>
[Cherche sur Instagram jeanbenoit_gambet + LinkedIn "Jean-Benoît Gambet Eiffel"]

<h4>📱 L'Analyste Curieux</h4>
[Cherche sur analystecurieux.fr + X @AnalysteCurieux + Instagram lanalystecurieux]
[Extraire toutes les fiches entreprises publiées cette semaine]

<h4>🎯 Consensus de la semaine</h4>
<b>Tickers cités par 2+ influenceurs :</b> [liste]<br>
<b>Sentiment global :</b> [BULLISH/BEARISH/NEUTRE]<br>
<b>Pépite PEA de la semaine :</b> [1 action sous-évaluée avec MOAT clair]<br>
<b>Action à éviter :</b> [1 action sur laquelle plusieurs sont négatifs]

Si une info n'est pas trouvée : écris clairement "<i>Non trouvé publiquement cette semaine</i>" plutôt que d'inventer."""

    try:
        payload = json.dumps({
            'model': 'claude-sonnet-4-6',
            'max_tokens': 2000,
            'tools': [{'type': 'web_search_20250305', 'name': 'web_search'}],
            'messages': [{'role': 'user', 'content': prompt}]
        }).encode()
        req = Request(
            'https://api.anthropic.com/v1/messages', data=payload,
            headers={
                'Content-Type': 'application/json',
                'x-api-key': ANTHROPIC_KEY,
                'anthropic-version': '2023-06-01',
                'anthropic-beta': 'web-search-2025-03-05'
            }
        )
        with urlopen(req, timeout=90) as resp:
            data = json.loads(resp.read())
        text = ''.join(b.get('text','') for b in data.get('content',[]) if b.get('type')=='text')
        print(f'  ✅ Résumé réseaux sociaux: {len(text)} chars')
        return text.strip() or None
    except Exception as e:
        print(f'  Social media error: {e}')
        return None

# ─── IA — ANALYSE TOP ACTIONS B.A.M ──────────────────────────────────────
def analyse_top_bam(stocks_top3):
    """Analyse IA courte pour les 3 meilleures actions"""
    if not ANTHROPIC_KEY or not stocks_top3: return {}
    results = {}
    for s in stocks_top3:
        ctx = f"ROE {s.get('roe','?')}%, Marge {s.get('margin','?')}%, Dette {s.get('debt','?')}x, Piotroski {s.get('pio','?')}/9, Upside DCF {s.get('upside','?')}%"
        prompt = (f"Note investissement pour {s['name']} ({s['ticker']}) PEA. {ctx}\n"
                  "4 lignes max:\nVERDICT: [ACHETER/ATTENDRE] à [X]€\n"
                  "MOAT: [avantage durable en 1 phrase chiffrée]\n"
                  "RISQUE: [risque principal concret]\n"
                  "SIGNAL: [ENTRER/CONSERVER/ÉVITER] — [raison]")
        try:
            payload = json.dumps({
                'model': 'claude-sonnet-4-6',
                'max_tokens': 150,
                'messages': [{'role': 'user', 'content': prompt}]
            }).encode()
            req = Request('https://api.anthropic.com/v1/messages', data=payload,
                         headers={'Content-Type':'application/json','x-api-key':ANTHROPIC_KEY,'anthropic-version':'2023-06-01'})
            with urlopen(req, timeout=15) as r:
                d = json.loads(r.read())
            results[s['ticker']] = d['content'][0]['text'].strip()
            time.sleep(1)
        except Exception as e:
            print(f'  IA {s["ticker"]}: {e}')
    return results

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
        price = gn('price'); dcfm = gn('dcfm')
        upside = round((dcfm - price)/price*100,1) if price and dcfm else 0
        in_zone = price > 0 and dcfm > 0 and price <= dcfm*0.88 and gs('score') in ['A','B']
        # Score B.A.M simplifié
        roe = gn('roe'); margin = gn('margin'); fcf = gn('fcf'); debt = gn('debt'); pio = gn('pio')
        q = 20 if roe>=25 else 16 if roe>=18 else 11 if roe>=12 else 6
        r = 20 if (margin+fcf)/2>=20 else 15 if (margin+fcf)/2>=12 else 10 if (margin+fcf)/2>=7 else 5
        b = 16 if debt<=1 and pio>=7 else 11 if debt<=2 else 6
        v = 20 if upside>=35 else 15 if upside>=20 else 10 if upside>=10 else 5 if upside>=0 else 1
        mnt = 3 + (7 if in_zone else 0) + (7 if gn('price')>gn('mm200') and gn('mm200') else 0)
        bam = q + r + b + v + mnt
        stocks.append({
            'ticker': ticker, 'name': gs('name'), 'score': gs('score'),
            'price': price, 'upside': upside, 'in_zone': in_zone,
            'roe': roe, 'margin': margin, 'fcf': fcf, 'debt': debt, 'pio': pio,
            'el': gn('el'), 'eh': gn('eh'), 'stop': gn('stop'), 'o1': gn('o1'),
            'bam': bam, 'thesis': gdb('thesis'), 'contra': gdb('contra'),
        })
    return sorted(stocks, key=lambda x: -x['bam'])

# ─── HTML MAIL ────────────────────────────────────────────────────────────
def build_mail(stocks, all_news, social_summary, ia_notes, newsletters):
    MONTHS = {'January':'janvier','February':'février','March':'mars','April':'avril',
              'May':'mai','June':'juin','July':'juillet','August':'août',
              'September':'septembre','October':'octobre','November':'novembre','December':'décembre'}
    now = datetime.now()
    date_fr = now.strftime('%d %B %Y')
    for en, fr in MONTHS.items(): date_fr = date_fr.replace(en, fr)

    signals = [s for s in stocks if s['bam'] >= 55 and s['score'] in ['A','B']]
    ultimes  = [s for s in signals if s['bam'] >= 85 and s['in_zone']]
    forts    = [s for s in signals if 68 <= s['bam'] < 85]

    parts = []

    # HEADER
    parts.append(
        '<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>'
        '<body style="margin:0;padding:0;background:#f1f5f9;font-family:Helvetica Neue,Arial,sans-serif">'
        '<div style="max-width:680px;margin:0 auto;padding:16px">'
        '<div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:12px;padding:20px 24px;margin-bottom:16px">'
        '<div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:3px;margin-bottom:6px">VAL.PEA · MÉTHODE B.A.M · ' + date_fr + '</div>'
        '<div style="font-size:20px;font-weight:700;color:#f0d080;font-family:Georgia,serif">Revue hebdomadaire complète</div>'
        '<div style="font-size:11px;color:rgba(255,255,255,.6);margin-top:4px">'
        + str(len(stocks)) + ' valeurs · ' + str(len(ultimes)) + ' ULTIME · ' + str(len(forts)) + ' FORT · '
        + str(len(newsletters)) + ' newsletters lues</div>'
        '</div>'
    )

    # SECTION RÉSEAUX SOCIAUX — la plus importante
    if social_summary:
        parts.append(
            '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin-bottom:16px">'
            '<div style="background:#0f2540;color:#f0d080;padding:8px 14px;border-radius:6px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">'
            '📱 Résumé réseaux sociaux & newsletters — semaine du ' + (now - timedelta(days=7)).strftime('%d/%m') + ' au ' + now.strftime('%d/%m') + '</div>'
            '<style>h4{color:#0f2540;font-size:13px;margin:14px 0 6px;border-bottom:1px solid #e2e8f0;padding-bottom:4px}'
            'ul{margin:4px 0 8px;padding-left:18px}li{margin:3px 0}'
            'b{color:#0f2540}</style>'
            '<div style="font-size:12px;line-height:1.8;color:#333">' + social_summary + '</div>'
            '</div>'
        )

    # SIGNAUX B.A.M
    if signals:
        parts.append(
            '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin-bottom:16px">'
            '<div style="font-size:11px;font-weight:700;color:#0f2540;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">'
            '🎯 Signaux B.A.M de la semaine</div>'
        )
        for s in signals[:6]:
            ia = ia_notes.get(s['ticker'], '')
            bam_col = '#16a34a' if s['bam']>=85 else '#d97706' if s['bam']>=68 else '#2563eb'
            sig_lbl = 'ULTIME' if s['bam']>=85 and s['in_zone'] else 'FORT' if s['bam']>=68 else 'SURVEILLER'
            upside_str = ('+' if s['upside']>0 else '') + str(s['upside']) + '%'
            parts.append(
                '<div style="border:1px solid ' + bam_col + '40;border-left:4px solid ' + bam_col + ';border-radius:0 6px 6px 0;padding:12px;margin-bottom:8px">'
                '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">'
                '<div><b style="font-family:monospace;font-size:14px">' + s['ticker'] + '</b> <span style="color:#888;font-size:11px">' + s['name'][:18] + '</span></div>'
                '<span style="background:' + bam_col + ';color:#fff;padding:2px 8px;border-radius:3px;font-size:10px;font-weight:700">' + sig_lbl + ' · BAM ' + str(s['bam']) + '/120</span>'
                '</div>'
                '<div style="font-size:10px;display:flex;gap:12px;flex-wrap:wrap;color:#555">'
                '<span>Cours <b>' + str(s['price']) + '€</b></span>'
                '<span>Upside <b style="color:' + ('#16a34a' if s['upside']>0 else '#dc2626') + '">' + upside_str + '</b></span>'
                '<span>Zone <b>' + str(s['el']) + '–' + str(s['eh']) + '€</b></span>'
                '<span>Stop <b>' + str(s['stop']) + '€</b></span>'
                '<span>R/R <b>' + str(round((s['o1']-s['price'])/(s['price']-s['stop']),1) if s['stop'] and s['o1'] and s['price']>s['stop'] else 0) + 'x</b></span>'
                '</div>'
                + (('<div style="margin-top:6px;background:#f0fdf4;border-left:2px solid #16a34a;padding:6px;font-size:10px;color:#1a4730">' + s['thesis'][:180] + '</div>') if s.get('thesis') else '')
                + (('<div style="margin-top:4px;background:#f0f9ff;border:1px solid #bae6fd;border-radius:4px;padding:6px;font-size:10px"><b>🤖 IA :</b> ' + ia + '</div>') if ia else '')
                + '</div>'
            )
        parts.append('</div>')

    # ACTUALITÉS MARCHÉS
    mkt_news = [n for n in all_news if any(kw in n['title'].lower() for kw in ['cac','marché','bourse','fed','bce','taux','inflation','euro'])][:5]
    if mkt_news:
        parts.append(
            '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin-bottom:16px">'
            '<div style="font-size:11px;font-weight:700;color:#0f2540;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px">📰 Actualités marchés</div>'
        )
        for n in mkt_news:
            parts.append(
                '<div style="border-left:3px solid #f0d080;padding:5px 10px;margin:5px 0;background:#fffbf0">'
                '<a href="' + n['link'] + '" style="color:#0f2540;text-decoration:none;font-size:12px;font-weight:600">' + n['title'][:90] + '</a>'
                '<div style="font-size:10px;color:#888;margin-top:2px">' + n['source'] + ' · ' + n['pub'] + '</div>'
                '</div>'
            )
        parts.append('</div>')

    # FOOTER
    parts.append(
        '<div style="text-align:center;font-size:9px;color:#94a3b8;padding:10px">'
        'VAL.PEA · Méthode B.A.M · ' + date_fr + ' · Non-conseil en investissement</div>'
        '</div></body></html>'
    )
    return '\n'.join(parts)

# ─── SEND ─────────────────────────────────────────────────────────────────
def send_mail(subject, html_body):
    with open('mail_preview.html', 'w', encoding='utf-8') as f:
        f.write(html_body)
    print('  Preview: mail_preview.html')
    if not SMTP_USER or not SMTP_TO:
        print('  ⚠️ SMTP non configuré'); return
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From']    = SMTP_USER
    msg['To']      = SMTP_TO
    msg.attach(MIMEText(html_body, 'html', 'utf-8'))
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(SMTP_USER, SMTP_TO.split(','), msg.as_string())
        print(f'  ✅ Mail envoyé à {SMTP_TO}')
    except Exception as e:
        print(f'  ❌ SMTP: {e}')

# ─── MAIN ─────────────────────────────────────────────────────────────────
def main():
    now = datetime.now()
    print('=' * 60)
    print(f'VAL.PEA generate_reports — {now.strftime("%d/%m/%Y %H:%M")}')
    print('=' * 60)

    if not os.path.exists('index.html'):
        print('❌ index.html introuvable'); sys.exit(1)
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    print('\n📊 Parsing stocks...')
    stocks = parse_stocks(html_content)
    print(f'  {len(stocks)} actions')

    print('\n📧 Lecture newsletters Gmail (15 jours)...')
    newsletters = fetch_gmail_newsletters(days_back=15)

    print('\n📡 Récupération RSS...')
    all_news = fetch_rss()

    print('\n📱 Résumé réseaux sociaux (Claude + web_search)...')
    social_summary = fetch_social_media_summary(newsletters)

    print('\n🤖 Analyse IA top 3 B.A.M...')
    top3 = [s for s in stocks if s['score']=='A'][:3]
    ia_notes = analyse_top_bam(top3)

    print('\n📨 Construction mail...')
    html_body = build_mail(stocks, all_news, social_summary, ia_notes, newsletters)

    nb_sig = len([s for s in stocks if s['bam']>=68])
    subject = f"VAL.PEA · Revue {now.strftime('%d/%m')} · {nb_sig} signaux B.A.M · Résumé réseaux"
    send_mail(subject, html_body)
    print('\n✅ Done')

if __name__ == '__main__':
    main()
