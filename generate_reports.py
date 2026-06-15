#!/usr/bin/env python3
"""
VAL.PEA — generate_reports.py (corrigé: backslash in f-string)
Mail enrichi : RSS news, YouTube influenceurs, IA analyse, signaux, portfolio
"""
import re, json, sys, os, time, html as html_lib
from datetime import datetime, timedelta
from urllib.request import urlopen, Request
import urllib.parse, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ─── CONFIG ──────────────────────────────────────────────────────────────────
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
SMTP_USER = (os.environ.get('MAIL_USER') or os.environ.get('GMAIL_USER', '')).strip()
SMTP_PASS = (os.environ.get('MAIL_PASS') or os.environ.get('GMAIL_PASSWORD', '')).strip()
SMTP_TO   = (os.environ.get('MAIL_TO') or SMTP_USER).strip()

print(f"ANTHROPIC_API_KEY: {'OK ' + str(len(ANTHROPIC_API_KEY)) + ' chars' if ANTHROPIC_API_KEY else 'MANQUANT'}")
print(f"MAIL_USER: {SMTP_USER or 'MANQUANT'}")
print(f"MAIL_TO:   {SMTP_TO or 'MANQUANT'}")

YOUTUBE_CHANNELS = {
    'Guillaume Fournier': 'https://www.youtube.com/@GuillaumeFournier_Invest/videos',
    'Rique Trading':      'https://www.youtube.com/@riquetrading/videos',
    'Nicolas Cheron':     'https://www.youtube.com/@NicolasCheron/videos',
    'JB Gambet':          'https://www.youtube.com/@jbgambet/videos',
}

RSS_FEEDS = [
    ('Les Echos',  'https://rss.lesechos.fr/lesechos-bourse'),
    ('Boursorama', 'https://www.boursorama.com/actualites/rss/'),
    ('Reuters FR', 'https://fr.reuters.com/rssFeed/businessNews'),
    ('ZoneBourse', 'https://www.zonebourse.com/rss/actualites-bourse/'),
]

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

def http_get(url, timeout=10):
    try:
        req = Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
        with urlopen(req, timeout=timeout) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f'  SKIP {url[:60]}: {e}')
        return ''

# ─── RSS ─────────────────────────────────────────────────────────────────────
def parse_rss(xml_text):
    items = []
    for m in re.finditer(r'<item>(.*?)</item>', xml_text, re.DOTALL):
        block = m.group(1)
        def get(tag):
            mx = re.search(r'<' + tag + r'[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</' + tag + r'>', block, re.DOTALL)
            return html_lib.unescape(mx.group(1).strip()) if mx else ''
        title = get('title')
        link  = get('link') or get('guid')
        pub   = (get('pubDate') or get('dc:date') or '')[:16]
        desc  = re.sub(r'<[^>]+>', '', get('description'))[:200]
        if title:
            items.append({'title': title, 'link': link, 'pub': pub, 'desc': desc, 'source': ''})
    return items[:20]

def fetch_all_news():
    all_news = []
    for source, url in RSS_FEEDS:
        print(f'  RSS: {source}...')
        xml = http_get(url)
        if xml:
            items = parse_rss(xml)
            for item in items:
                item['source'] = source
            all_news.extend(items)
        time.sleep(0.5)
    print(f'  Total: {len(all_news)} articles')
    return all_news

def news_for_ticker(ticker, name, all_news, max_items=2):
    SYNONYMS = {
        'MC':['lvmh','arnault'],'RMS':['hermes','birkin'],'AIR':['airbus'],
        'SAF':['safran'],'OR':['loreal'],'SAN':['sanofi'],'TTE':['totalenergies'],
        'DSY':['dassault'],'ASML':['asml','euv'],'BNP':['bnp paribas'],
    }
    keywords = [ticker.lower(), name.lower().split()[0]] + SYNONYMS.get(ticker, [])
    results = []
    for item in all_news:
        text = (item['title'] + ' ' + item.get('desc','')).lower()
        if any(kw in text for kw in keywords):
            results.append(item)
            if len(results) >= max_items:
                break
    return results

# ─── YOUTUBE ─────────────────────────────────────────────────────────────────
def fetch_youtube_videos(channel_url, max_videos=3):
    html_content = http_get(channel_url)
    if not html_content:
        return []
    videos = []
    for m in re.finditer(r'"title":\{"runs":\[\{"text":"([^"]+)"', html_content):
        title = m.group(1)
        if len(title) > 10 and title not in [v['title'] for v in videos]:
            videos.append({'title': title})
            if len(videos) >= max_videos:
                break
    return videos[:max_videos]

def fetch_all_youtube():
    results = {}
    for name, url in YOUTUBE_CHANNELS.items():
        print(f'  YouTube: {name}...')
        results[name] = fetch_youtube_videos(url)
        time.sleep(1)
    return results

# ─── ANALYSE IA ──────────────────────────────────────────────────────────────
def ia_analysis_for_mail(ticker, name, stock_data):
    if not ANTHROPIC_API_KEY:
        return None
    import urllib.request as ur
    ctx = (f"PE {stock_data.get('pe','?')}x, ROE {stock_data.get('roe','?')}%, "
           f"Marge {stock_data.get('margin','?')}%, Piotroski {stock_data.get('pio','?')}/9")
    nl = "\n"
    prompt = (
        "Note investissement courte pour " + name + " (" + ticker + ") PEA." + nl
        + "Donnees: " + ctx + nl + nl
        + "Format STRICT 4 lignes:" + nl
        + "VERDICT: [INVESTIR/PASSER/ATTENDRE] a [X]EUR" + nl
        + "MOAT: [une phrase chiffree]" + nl
        + "RISQUE: [principal risque concret]" + nl
        + "SIGNAL: [ACHETER/CONSERVER/VENDRE] - [raison courte]" + nl
        + "Zero disclaimer."
    )
    try:
        payload = json.dumps({
            'model': 'claude-sonnet-4-6',
            'max_tokens': 150,
            'messages': [{'role': 'user', 'content': prompt}]
        }).encode()
        req = ur.Request('https://api.anthropic.com/v1/messages', data=payload,
                         headers={'Content-Type': 'application/json',
                                  'x-api-key': ANTHROPIC_API_KEY,
                                  'anthropic-version': '2023-06-01'})
        with ur.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
        return d['content'][0]['text'].strip()
    except Exception as e:
        print(f'  IA error {ticker}: {e}')
        return None

# ─── PARSE STOCKS depuis index.html ──────────────────────────────────────────
def parse_stocks_simple(html_content):
    """Parse simplifié des actions depuis const S=[...]"""
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
        def gn(key, d=0.0):
            mx = re.search(r'\b' + key + r':([-\d.]+)', block)
            return float(mx.group(1)) if mx else d
        def gs(key, d=''):
            mx = re.search(r"\b" + key + r":'([^']*)'", block)
            return mx.group(1) if mx else d
        def gdb(key, d=''):
            mx = re.search(r'\b' + key + r':"([^"]*)"', block)
            return mx.group(1) if mx else d
        price = gn('price'); dcfm = gn('dcfm')
        upside = round((dcfm - price) / price * 100, 1) if price and dcfm else 0
        in_zone = price > 0 and dcfm > 0 and price <= dcfm * 0.88 and gs('score') in ['A','B']
        s = {
            'ticker': ticker, 'name': gs('name'), 'sector': gs('sector'), 'score': gs('score'),
            'price': price, 'el': gn('el'), 'eh': gn('eh'), 'stop': gn('stop'), 'o1': gn('o1'),
            'dcfm': dcfm, 'roe': gn('roe'), 'margin': gn('margin'), 'fcf': gn('fcf'),
            'debt': gn('debt'), 'pio': gn('pio'), 'rsi': gn('rsi'),
            'pe': gn('pe'), 'upside': upside, 'in_zone': in_zone,
            'thesis': gdb('thesis'), 'contra': gdb('contra'),
        }
        # QARP simplifié
        q = 20 if s['roe'] >= 25 else 16 if s['roe'] >= 18 else 11 if s['roe'] >= 12 else 6
        r_avg = (s['margin'] + s['fcf']) / 2
        r = 20 if r_avg >= 20 else 15 if r_avg >= 12 else 10 if r_avg >= 7 else 5
        b = 16 if s['debt'] <= 1 and s['pio'] >= 7 else 11 if s['debt'] <= 2 else 6
        v = 20 if upside >= 35 else 15 if upside >= 20 else 10 if upside >= 10 else 5 if upside >= 0 else 1
        mnt = 3 + (7 if in_zone else 0) + (7 if price > gn('mm200') and gn('mm200') else 0) + (3 if 25 <= s['rsi'] <= 60 and s['rsi'] else 0)
        s['qarp'] = q + r + b + v + mnt
        s['signal'] = ('ULTIME' if s['qarp'] >= 70 and in_zone and upside > 5 else
                       'FORT'   if s['qarp'] >= 58 and s['score'] in ['A','B'] and upside > 8 else
                       'SURVEILLER' if s['qarp'] >= 50 and s['score'] == 'A' else None)
        risk = price - s['stop'] if s['stop'] else 1
        s['rr'] = round((s['o1'] - price) / risk, 1) if risk > 0 and s['o1'] else 0
        stocks.append(s)
    return stocks

# ─── HTML MAIL ───────────────────────────────────────────────────────────────
def generate_html_mail(data):
    now          = data['now']
    signals      = data['signals']
    portfolio    = data['portfolio']
    all_news     = data['news']
    youtube      = data['youtube']
    earnings_week = data['earnings_week']
    ia_notes     = data['ia_notes']

    # Traduction mois — PAS dans f-string pour éviter le bug backslash
    MONTHS = {
        'January':'janvier','February':'février','March':'mars','April':'avril',
        'May':'mai','June':'juin','July':'juillet','August':'août',
        'September':'septembre','October':'octobre','November':'novembre','December':'décembre'
    }
    date_en = now.strftime('%d %B %Y')
    date_fr = date_en
    for en, fr in MONTHS.items():
        date_fr = date_fr.replace(en, fr)

    parts = []

    # Header
    header = (
        '<!DOCTYPE html><html><head><meta charset="utf-8"></head>'
        '<body style="margin:0;background:#f1f5f9;">'
        '<div style="max-width:680px;margin:0 auto;font-family:Arial,sans-serif;">'
        '<div style="background:linear-gradient(135deg,#0F2540,#1A3A5C);padding:28px 24px;text-align:center;">'
        '<div style="color:#F0D080;font-size:22px;font-weight:bold;">📊 VAL.PEA — ' + date_fr + '</div>'
        '<div style="color:#AABBCC;font-size:12px;margin-top:6px;">Screener PEA · Quality Investing · Décisions du week-end</div>'
        '</div>'
    )
    parts.append(header)

    # Résultats trimestriels
    if earnings_week:
        parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
        parts.append('<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">📅 Résultats publiés cette semaine</div>')
        for e in earnings_week:
            # Construire la ligne sans backslash dans f-string
            ticker_html = '<span style="background:#0F2540;color:#F0D080;padding:2px 8px;border-radius:4px;font-weight:bold;">' + e['ticker'] + '</span>'
            name_html   = '<strong style="margin-left:8px;">' + e['name'] + '</strong>'
            summary     = e.get('summary', 'Résultats publiés — vérifier les chiffres clés')
            summary_html = '<div style="font-size:12px;color:#555;margin-top:4px;">' + summary + '</div>'
            parts.append('<div style="padding:8px 0;border-bottom:1px solid #f0f0f0;">' + ticker_html + name_html + summary_html + '</div>')
        parts.append('</div>')

    # Signaux
    nb_sig = len(signals)
    parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
    parts.append('<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">🎯 Signaux du dimanche — ' + str(nb_sig) + ' opportunité(s)</div>')

    if signals:
        for s in signals[:5]:
            news = news_for_ticker(s['ticker'], s['name'], all_news, 2)
            ia   = ia_notes.get(s['ticker'], '')
            upside_str  = '+' + str(s['upside']) + '%' if s['upside'] > 0 else str(s['upside']) + '%'
            zone_str    = str(s['el']) + '–' + str(s['eh']) + '€'
            signal_lbl  = s.get('signal') or '—'
            qarp_val    = str(s.get('qarp', '?'))
            price_str   = str(s['price']) + '€'
            roe_str     = str(s['roe']) + '%'
            margin_str  = str(s['margin']) + '%'
            pio_str     = str(int(s['pio'])) + '/9'
            stop_str    = str(s['stop']) + '€'
            rr_str      = str(s['rr']) + 'x'

            card = (
                '<div style="border:1px solid #DCFCE7;border-radius:8px;padding:14px;margin:10px 0;background:#F0FDF4;">'
                '<div style="display:flex;justify-content:space-between;align-items:center;">'
                '<div>'
                '<span style="background:#0F2540;color:#F0D080;padding:2px 8px;border-radius:4px;font-weight:bold;font-size:13px;">' + s['ticker'] + '</span>'
                '<strong style="font-size:14px;margin-left:6px;">' + s['name'] + '</strong>'
                '<span style="background:#DCFCE7;color:#16A34A;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:bold;margin-left:4px;">QARP ' + qarp_val + '/100 — ' + signal_lbl + '</span>'
                '</div>'
                '<div style="text-align:right;">'
                '<div style="font-size:18px;font-weight:bold;color:#0F2540;">' + price_str + '</div>'
                '<div style="font-size:11px;color:#16A34A;">Zone ' + zone_str + ' | Upside ' + upside_str + '</div>'
                '</div></div>'
                '<div style="font-size:12px;margin-top:8px;display:flex;gap:12px;flex-wrap:wrap;">'
                '<span>R/R <strong>' + rr_str + '</strong></span>'
                '<span>ROE <strong>' + roe_str + '</strong></span>'
                '<span>Marge <strong>' + margin_str + '</strong></span>'
                '<span>Pio <strong>' + pio_str + '</strong></span>'
                '<span>Stop <strong>' + stop_str + '</strong></span>'
                '</div>'
            )

            # Thesis / Contra
            if s.get('thesis'):
                card += ('<div style="margin-top:8px;padding:8px;background:#f0fdf4;border-left:3px solid #16a34a;font-size:11px;color:#1a4730;">'
                         '<b>Pourquoi investir : </b>' + s['thesis'][:200] + '</div>')
            if s.get('contra'):
                card += ('<div style="margin-top:4px;padding:8px;background:#fff5f5;border-left:3px solid #dc2626;font-size:11px;color:#7c2d2d;">'
                         '<b>Risque marché : </b>' + s['contra'][:180] + '</div>')

            # News RSS
            if news:
                card += '<div style="margin-top:8px;font-size:11px;color:#555;font-weight:bold;">📰 Actualités :</div>'
                for n in news:
                    card += ('<div style="border-left:3px solid #F0D080;padding:4px 8px;margin:4px 0;background:#FFFBF0;">'
                             '<a href="' + n['link'] + '" style="color:#0F2540;text-decoration:none;font-size:12px;"><strong>' + n['title'][:80] + '</strong></a>'
                             '<div style="font-size:10px;color:#888;">' + n['source'] + ' · ' + n['pub'] + '</div></div>')

            # IA note
            if ia:
                card += ('<div style="background:#F0F9FF;border:1px solid #BAE6FD;border-radius:6px;padding:10px;margin-top:8px;font-size:12px;">'
                         '<strong>🤖 Analyse IA :</strong>'
                         '<pre style="font-family:Arial;margin:4px 0;white-space:pre-wrap;font-size:11px;">' + ia + '</pre></div>')

            card += '</div>'
            parts.append(card)
    else:
        parts.append('<p style="color:#D97706;">⏳ Aucun signal Grade A + Zone + QARP ≥ 70 cette semaine. Patience.</p>')

    parts.append('</div>')

    # Portfolio
    if portfolio:
        total_val = sum(p['val'] for p in portfolio)
        total_pnl = sum(p['pnl'] for p in portfolio)
        base      = total_val - total_pnl
        pnl_pct   = total_pnl / base * 100 if base > 0 else 0
        pnl_col   = '#16A34A' if total_pnl >= 0 else '#DC2626'
        pnl_sign  = '+' if total_pnl >= 0 else ''
        pnl_str   = pnl_sign + str(round(total_pnl)) + '€ (' + pnl_sign + str(round(pnl_pct,1)) + '%)'

        parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
        parts.append('<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">💼 Portefeuille — ' + str(round(total_val)) + '€ | PV/MV <span style="color:' + pnl_col + ';">' + pnl_str + '</span></div>')
        parts.append('<table style="width:100%;border-collapse:collapse;font-size:12px;"><tr style="background:#0F2540;color:#fff;"><th style="padding:6px;text-align:left;">Valeur</th><th>Cours</th><th>PV/MV</th><th>Zone</th><th>Avis</th></tr>')

        for p in portfolio:
            s    = p['s']
            pct  = p['pct']
            iz   = s.get('in_zone', False)
            bg   = '#F0FDF4' if pct >= 0 else '#FFF5F5'
            col  = '#16A34A' if pct >= 0 else '#DC2626'
            pct_s = ('+' if pct >= 0 else '') + str(round(pct,1)) + '%'
            zone_s   = '✅ Zone' if iz else '—'
            zone_col = '#16A34A' if iz else '#6B7280'
            cours    = p['cours']
            stop_val = s.get('stop', 0)

            if stop_val and cours <= stop_val * 1.05 and stop_val > 0:
                avis = '⚠️ STOP'
            elif iz and s.get('rr', 0) >= 1.5:
                avis = '✅ Renforcer'
            elif pct > 40 and s.get('upside', 0) < 0:
                avis = '📤 Alléger'
            elif pct >= 0:
                avis = '○ Tenir'
            else:
                avis = '👁 Surveiller'

            news = news_for_ticker(s['ticker'], s['name'], all_news, 1)
            news_s = ('<div style="font-size:10px;color:#888;">📰 ' + news[0]['title'][:60] + '</div>') if news else ''

            parts.append(
                '<tr style="background:' + bg + ';border-bottom:1px solid #e0e0e0;">'
                '<td style="padding:6px;"><strong>' + s['ticker'] + '</strong> ' + s['name'][:14] + news_s + '</td>'
                '<td style="padding:6px;">' + str(cours) + '€</td>'
                '<td style="padding:6px;color:' + col + ';font-weight:bold;">' + pct_s + '</td>'
                '<td style="padding:6px;color:' + zone_col + ';font-size:11px;">' + zone_s + '</td>'
                '<td style="padding:6px;font-size:11px;">' + avis + '</td>'
                '</tr>'
            )
        parts.append('</table></div>')

    # Actualités marchés
    mkt_news = [n for n in all_news if any(kw in n['title'].lower() for kw in ['cac','marche','bourse','fed','bce','taux','inflation'])][:5]
    if mkt_news:
        parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
        parts.append('<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">📰 Actualités marchés</div>')
        for n in mkt_news:
            parts.append(
                '<div style="border-left:3px solid #F0D080;padding:6px 10px;margin:6px 0;background:#FFFBF0;">'
                '<a href="' + n['link'] + '" style="color:#0F2540;text-decoration:none;font-size:13px;"><strong>' + n['title'] + '</strong></a>'
                '<div style="font-size:11px;color:#888;margin-top:2px;">' + n['source'] + ' · ' + n['pub'] + '</div>'
                '</div>'
            )
        parts.append('</div>')

    # YouTube influenceurs
    parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
    parts.append('<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 4px;border-bottom:2px solid #F0D080;padding-bottom:6px;">📺 Ce que disent les influenceurs</div>')
    parts.append('<p style="font-size:11px;color:#888;margin:0 0 12px;">Vérifier manuellement avant votre décision du week-end</p>')

    ICONS = {'Guillaume Fournier': '🎓', 'Rique Trading': '📈', 'Nicolas Cheron': '🔍', 'JB Gambet': '💡'}
    for name_yt, videos in youtube.items():
        icon = ICONS.get(name_yt, '▶️')
        parts.append('<div style="margin-bottom:14px;"><strong>' + icon + ' ' + name_yt + '</strong>')
        if videos:
            for v in videos:
                parts.append('<div style="border-left:3px solid #7C3AED;padding:5px 10px;margin:4px 0;background:#F8F5FF;font-size:12px;">▶️ ' + v['title'] + '</div>')
        else:
            parts.append('<div style="font-size:12px;color:#888;padding:4px 8px;">Impossible de récupérer les vidéos — vérifier manuellement.</div>')
        parts.append('</div>')
    parts.append('</div>')

    # Footer
    parts.append('<div style="text-align:center;padding:16px;color:#888;font-size:11px;">VAL.PEA · ' + date_fr + ' · Non-conseil en investissement</div></div></body></html>')

    return '\n'.join(parts)

# ─── SEND MAIL ───────────────────────────────────────────────────────────────
def send_mail(subject, html_body, attachments=None):
    with open('mail_preview.html', 'w', encoding='utf-8') as f:
        f.write(html_body)
    print('-> mail_preview.html sauvegardé')

    if not SMTP_USER or not SMTP_TO:
        print('SMTP non configuré — définir MAIL_USER, MAIL_PASS, MAIL_TO dans les secrets GitHub')
        return

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From']    = SMTP_USER
    msg['To']      = SMTP_TO
    msg.attach(MIMEText(html_body, 'html', 'utf-8'))

    if attachments:
        for path in attachments:
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="' + os.path.basename(path) + '"')
                msg.attach(part)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(SMTP_USER, SMTP_TO.split(','), msg.as_string())
        print('Mail envoyé à ' + SMTP_TO)
    except Exception as e:
        print('Erreur SMTP: ' + str(e))

# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    now = datetime.now()
    print('VAL.PEA generate_reports --- ' + now.strftime('%Y-%m-%d %H:%M'))

    if not os.path.exists('index.html'):
        print('ERROR: index.html not found'); sys.exit(1)
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    print('Parsing actions...')
    stocks_all = parse_stocks_simple(html_content)
    print(str(len(stocks_all)) + ' actions')

    # Signaux ULTIME/FORT
    signals = sorted(
        [s for s in stocks_all if s.get('signal') in ('ULTIME', 'FORT')],
        key=lambda x: -x.get('qarp', 0)
    )
    print(str(len(signals)) + ' signaux')

    # Portefeuille (positions hardcodées depuis les données connues)
    PTF = [
        ('PAEEM',13,30.91),('PTPXE',3,34.46),('DCAM',80,5.51),('ESE',10,29.86),
        ('RMS',1,2037),('AI',10,159),('LR',5,139),('HO',3,237),
        ('SU',7,241),('TTE',20,50),('EL',3,212),('GTT',4,197),
        ('ELIS',45,19),('ASML',1,654),
    ]
    portfolio = []
    for ticker, qty, pru in PTF:
        s = next((x for x in stocks_all if x['ticker'] == ticker), None)
        if not s: continue
        cours = s['price']
        if cours <= 0: continue
        pnl = round((cours - pru) * qty, 2)
        pct = round((cours - pru) / pru * 100, 2) if pru else 0
        portfolio.append({'ticker': ticker, 'qty': qty, 'pru': pru, 's': s,
                          'cours': cours, 'val': round(cours * qty, 2), 'pnl': pnl, 'pct': pct})

    print('Fetching news...')
    all_news = fetch_all_news()

    print('Fetching YouTube...')
    youtube = fetch_all_youtube()

    # Earnings depuis fundamentals_log.json
    earnings_week = []
    try:
        if os.path.exists('fundamentals_log.json'):
            with open('fundamentals_log.json') as f:
                log = json.load(f)
            for e in log.get('earnings', []):
                if -7 <= e.get('days_away', 99) <= 0:
                    s = next((x for x in stocks_all if x['ticker'] == e['ticker']), None)
                    earnings_week.append({
                        'ticker': e['ticker'],
                        'name': s['name'] if s else e['ticker'],
                        'summary': ''
                    })
    except Exception as ex:
        print('earnings error: ' + str(ex))

    # IA pour top 3 signaux
    ia_notes = {}
    if ANTHROPIC_API_KEY and signals:
        print('Analyses IA top 3...')
        for s in signals[:3]:
            note = ia_analysis_for_mail(s['ticker'], s['name'], s)
            if note:
                ia_notes[s['ticker']] = note
            time.sleep(2)

    print('Génération mail HTML...')
    html_body = generate_html_mail({
        'now': now, 'signals': signals, 'portfolio': portfolio,
        'news': all_news, 'youtube': youtube,
        'earnings_week': earnings_week, 'ia_notes': ia_notes
    })

    # DOCX (optionnel — si generate_reports_legacy existe)
    attachments = []
    try:
        from generate_reports_legacy import generate_revue_vendredi, generate_signaux_dimanche
        MONTHS2 = {'January':'janvier','February':'février','March':'mars','April':'avril',
                   'May':'mai','June':'juin','July':'juillet','August':'août',
                   'September':'septembre','October':'octobre','November':'novembre','December':'décembre'}
        date_str = now.strftime('%d %B %Y')
        for en, fr in MONTHS2.items():
            date_str = date_str.replace(en, fr)
        revue_path = 'VAL_PEA_Revue_' + now.strftime('%Y%m%d') + '.docx'
        generate_revue_vendredi(html_content, revue_path, date_str)
        attachments.append(revue_path)
        if signals:
            sig_path = 'VAL_PEA_Signaux_' + now.strftime('%Y%m%d') + '.docx'
            generate_signaux_dimanche(html_content, sig_path, date_str)
            attachments.append(sig_path)
    except Exception as e:
        print('DOCX ignoré: ' + str(e))

    nb_sig = len(signals)
    subject = 'VAL.PEA — ' + now.strftime('%d/%m/%Y') + ' — ' + str(nb_sig) + ' signal(s)'
    send_mail(subject, html_body, attachments)
    print('DONE')

if __name__ == '__main__':
    main()
