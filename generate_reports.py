#!/usr/bin/env python3
"""
VAL.PEA — generate_reports_v2.py
Mail du dimanche enrichi :
  - News RSS par action (Les Echos, Boursorama, Reuters)
  - YouTube : Guillaume Fournier, Rique Trading, Nicolas Cheron, JB Gambet
  - Resultats trimestriels de la semaine
  - Analyse IA Anthropic par action (si cle disponible)
  - Signaux + revue portefeuille
"""
import re, json, sys, os, time, html as html_lib
from datetime import datetime, timedelta
from urllib.request import urlopen, Request
from urllib.error import URLError
import urllib.parse

# ─── CONFIG ──────────────────────────────────────────────────────────────────
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
SMTP_USER = os.environ.get('MAIL_USER', '')
SMTP_PASS = os.environ.get('MAIL_PASS', '')
SMTP_TO   = os.environ.get('MAIL_TO', '')

# Influenceurs YouTube a suivre
YOUTUBE_CHANNELS = {
    'Guillaume Fournier': 'https://www.youtube.com/@GuillaumeFournier_Invest/videos',
    'Rique Trading': 'https://www.youtube.com/@riquetrading/videos',
    'Nicolas Cheron': 'https://www.youtube.com/@NicolasCheron/videos',
    'JB Gambet': 'https://www.youtube.com/@jbgambet/videos',
}

# Flux RSS financiers francais
RSS_FEEDS = [
    ('Les Echos', 'https://rss.lesechos.fr/lesechos-bourse'),
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

# ─── RSS PARSER ─────────────────────────────────────────────────────────────
def parse_rss(xml_text):
    items = []
    for m in re.finditer(r'<item>(.*?)</item>', xml_text, re.DOTALL):
        block = m.group(1)
        def get(tag):
            mx = re.search(r'<'+tag+r'[^>]*>(?:<![CDATA[)?(.*?)(?:]]>)?</'+tag+r'>', block, re.DOTALL)
            return html_lib.unescape(mx.group(1).strip()) if mx else ''
        title = get('title')
        link = get('link') or get('guid')
        pub = get('pubDate') or get('dc:date') or ''
        desc = re.sub(r'<[^>]+>', '', get('description'))[:200]
        if title:
            items.append({'title': title, 'link': link, 'pub': pub[:16], 'desc': desc, 'source': ''})
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
        'MC': ['lvmh','arnault','moet','hennessy'],
        'RMS': ['hermes','birkin'],
        'AIR': ['airbus','boeing','leap'],
        'SAF': ['safran','cfm'],
        'OR': ['loreal'],
        'SAN': ['sanofi','dupixent'],
        'TTE': ['totalenergies','total energie'],
        'DSY': ['dassault','catia'],
        'CAP': ['capgemini'],
        'ASML': ['asml','lithographie','euv'],
        'BNP': ['bnp paribas'],
        'ACA': ['credit agricole'],
        'GLE': ['societe generale'],
        'ENGI': ['engie'],
    }
    keywords = [ticker.lower(), name.lower().split()[0]] + SYNONYMS.get(ticker, [])
    results = []
    for item in all_news:
        text = (item['title'] + ' ' + item.get('desc', '')).lower()
        if any(kw in text for kw in keywords):
            results.append(item)
        if len(results) >= max_items:
            break
    return results

# ─── YOUTUBE SCRAPER ────────────────────────────────────────────────────────
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
    if not videos:
        for m in re.finditer(r'aria-label="([^"]{20,100})"', html_content):
            title = m.group(1)
            if any(kw in title.lower() for kw in ['bourse','marche','action','cac','invest','analyse','trading']):
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

# ─── ANALYSE IA ANTHROPIC ───────────────────────────────────────────────────
def ia_analysis_for_mail(ticker, name, stock_data):
    if not ANTHROPIC_API_KEY:
        return None
    import urllib.request as ur
    ctx = (f"PE {stock_data.get('pe','?')}x, ROE {stock_data.get('roe','?')}%, "
           f"Marge {stock_data.get('margin','?')}%, Piotroski {stock_data.get('pio','?')}/9")
    prompt = (f"Note d investissement courte pour {name} ({ticker}) PEA.\n"
              f"Donnees: {ctx}\n\n"
              f"Format STRICT 4 lignes:\n"
              f"VERDICT: [INVESTIR/PASSER/ATTENDRE] a [X]\u20ac\n"
              f"MOAT: [une phrase chiffree]\n"
              f"RISQUE: [principal risque concret]\n"
              f"SIGNAL: [ACHETER/CONSERVER/VENDRE] - [raison courte]\n\n"
              f"Zero disclaimer.")
    try:
        payload = json.dumps({'model':'claude-sonnet-4-20250514','max_tokens':150,'messages':[{'role':'user','content':prompt}]}).encode()
        req = ur.Request('https://api.anthropic.com/v1/messages', data=payload,
            headers={'Content-Type':'application/json','x-api-key':ANTHROPIC_API_KEY,'anthropic-version':'2023-06-01'})
        with ur.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
            return d['content'][0]['text'].strip()
    except Exception as e:
        print(f'  IA error {ticker}: {e}')
        return None

# ─── GENERATEUR HTML MAIL ───────────────────────────────────────────────────
def generate_html_mail(data):
    now = data['now']
    signals = data['signals']
    portfolio = data['portfolio']
    all_news = data['news']
    youtube = data['youtube']
    earnings_week = data['earnings_week']
    ia_notes = data['ia_notes']

    MONTHS = {'January':'janvier','February':'f\xe9vrier','March':'mars','April':'avril',
               'May':'mai','June':'juin','July':'juillet','August':'ao\xfbt',
               'September':'septembre','October':'octobre','November':'novembre','December':'d\xe9cembre'}
    date_fr = now.strftime('%d %B %Y')
    for en, fr in MONTHS.items():
        date_fr = date_fr.replace(en, fr)

    parts = []
    parts.append(f'''<!DOCTYPE html><html><head><meta charset="utf-8"></head><body style="margin:0;background:#f1f5f9;">
<div style="max-width:680px;margin:0 auto;font-family:Arial,sans-serif;">
<div style="background:linear-gradient(135deg,#0F2540,#1A3A5C);padding:28px 24px;text-align:center;">
  <div style="color:#F0D080;font-size:22px;font-weight:bold;">\ud83d\udcca VAL.PEA \u2014 {date_fr}</div>
  <div style="color:#AABBCC;font-size:12px;margin-top:6px;">Screener PEA \xb7 Quality Investing \xb7 D\xe9cisions du week-end</div>
</div>''')

    # Resultats trimestriels
    if earnings_week:
        parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
        parts.append('<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">\ud83d\udcc5 R\xe9sultats publi\xe9s cette semaine</div>')
        for e in earnings_week:
            parts.append(f'<div style="padding:8px 0;border-bottom:1px solid #f0f0f0;"><span style="background:#0F2540;color:#F0D080;padding:2px 8px;border-radius:4px;font-weight:bold;">{e["ticker"]}</span> <strong style="margin-left:8px;">{e["name"]}</strong><div style="font-size:12px;color:#555;margin-top:4px;">{e.get("summary","R\xe9sultats publi\xe9s \u2014 v\xe9rifier les chiffres cl\xe9s")}</div></div>')
        parts.append('</div>')

    # Signaux
    nb_sig = len(signals)
    parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
    parts.append(f'<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">\ud83c\udfaf Signaux du dimanche \u2014 {nb_sig} opportunit\xe9(s)</div>')
    if signals:
        for s in signals[:5]:
            q = s.get('qarp', {})
            news = news_for_ticker(s['ticker'], s['name'], all_news, 2)
            ia = ia_notes.get(s['ticker'], '')
            parts.append(f'''<div style="border:1px solid #DCFCE7;border-radius:8px;padding:14px;margin:10px 0;background:#F0FDF4;">
  <div style="display:flex;justify-content:space-between;align-items:center;">
    <div><span style="background:#0F2540;color:#F0D080;padding:2px 8px;border-radius:4px;font-weight:bold;font-size:13px;">{s["ticker"]}</span> <strong style="font-size:14px;margin-left:6px;">{s["name"]}</strong> <span style="background:#DCFCE7;color:#16A34A;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:bold;margin-left:4px;">Score {q.get("total","?")}/100</span></div>
    <div style="text-align:right;"><div style="font-size:18px;font-weight:bold;color:#0F2540;">{s["price"]}\u20ac</div><div style="font-size:11px;color:#16A34A;">Zone {s["el"]}\u2013{s["eh"]}\u20ac | Upside +{s["upside"]}%</div></div>
  </div>
  <div style="font-size:12px;margin-top:8px;display:flex;gap:12px;flex-wrap:wrap;">
    <span>R/R <strong>{s["rr"]}x</strong></span><span>ROE <strong>{s["roe"]}%</strong></span><span>Marge <strong>{s["margin"]}%</strong></span><span>Pio <strong>{int(s["pio"])}/9</strong></span><span>Stop <strong>{s["stop"]}\u20ac</strong></span>
  </div>''')
            if news:
                parts.append('<div style="margin-top:8px;font-size:11px;color:#555;font-weight:bold;">\ud83d\udcf0 Actualit\xe9s :</div>')
                for n in news:
                    parts.append(f'<div style="border-left:3px solid #F0D080;padding:4px 8px;margin:4px 0;background:#FFFBF0;"><a href="{n["link"]}" style="color:#0F2540;text-decoration:none;font-size:12px;"><strong>{n["title"][:80]}</strong></a><div style="font-size:10px;color:#888;">{n["source"]} \xb7 {n["pub"]}</div></div>')
            if ia:
                parts.append(f'<div style="background:#F0F9FF;border:1px solid #BAE6FD;border-radius:6px;padding:10px;margin-top:8px;font-size:12px;"><strong>\ud83e\udd16 Analyse IA :</strong><pre style="font-family:Arial;margin:4px 0;white-space:pre-wrap;font-size:11px;">{ia}</pre></div>')
            parts.append('</div>')
    else:
        parts.append('<p style="color:#D97706;">\u23f3 Aucun signal Grade A + Zone + Score \u2265 70 cette semaine. Patience.</p>')
    parts.append('</div>')

    # Portefeuille
    if portfolio:
        total_val = sum(p['val'] for p in portfolio)
        total_pnl = sum(p['pnl'] for p in portfolio)
        base = total_val - total_pnl
        pnl_pct = total_pnl / base * 100 if base > 0 else 0
        pnl_col = '#16A34A' if total_pnl >= 0 else '#DC2626'
        pnl_str = f"+{total_pnl:.0f}\u20ac (+{pnl_pct:.1f}%)" if total_pnl >= 0 else f"{total_pnl:.0f}\u20ac ({pnl_pct:.1f}%)"
        parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
        parts.append(f'<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">\ud83d\udcbc Portefeuille \u2014 {total_val:.0f}\u20ac | PV/MV <span style="color:{pnl_col};">{pnl_str}</span></div>')
        parts.append('<table style="width:100%;border-collapse:collapse;font-size:12px;"><tr style="background:#0F2540;color:#fff;"><th style="padding:6px;text-align:left;">Valeur</th><th>Cours</th><th>PV/MV</th><th>Zone</th><th>Avis</th></tr>')
        for p in portfolio:
            s = p['s']
            pct = p['pct']
            iz = s.get('in_zone') or s.get('dcf_zone')
            bg = '#F0FDF4' if pct >= 0 else '#FFF5F5'
            col = '#16A34A' if pct >= 0 else '#DC2626'
            pct_s = f"+{pct:.1f}%" if pct >= 0 else f"{pct:.1f}%"
            zone_s = '\u2705 Zone' if iz else '\u2014'
            zone_col = '#16A34A' if iz else '#6B7280'
            if s.get('stop') and p['cours'] <= s['stop'] * 1.05 and s['stop'] > 0:
                avis = '\u26a0\ufe0f STOP'
            elif iz and s.get('rr', 0) >= 1.5:
                avis = '\u2705 Renforcer'
            elif pct > 40 and s.get('upside', 0) < 0:
                avis = '\ud83d\udce4 All\xe9ger'
            elif pct >= 0:
                avis = '\u25cb Tenir'
            else:
                avis = '\ud83d\udc41 Surveiller'
            news = news_for_ticker(s['ticker'], s['name'], all_news, 1)
            news_s = f'<div style="font-size:10px;color:#888;">\ud83d\udcf0 {news[0]["title"][:70]}</div>' if news else ''
            parts.append(f'<tr style="background:{bg};border-bottom:1px solid #e0e0e0;"><td style="padding:6px;"><strong>{s["ticker"]}</strong> {s["name"][:15]}{news_s}</td><td style="padding:6px;">{p["cours"]}\u20ac</td><td style="padding:6px;color:{col};font-weight:bold;">{pct_s}</td><td style="padding:6px;color:{zone_col};font-size:11px;">{zone_s}</td><td style="padding:6px;font-size:11px;">{avis}</td></tr>')
        parts.append('</table></div>')

    # Actualites marche
    mkt_news = [n for n in all_news if any(kw in n['title'].lower() for kw in ['cac','marche','bourse','fed','bce','taux','inflation','euro','europe'])][:5]
    if mkt_news:
        parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
        parts.append('<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">\ud83d\udcf0 Actualit\xe9s march\xe9s</div>')
        for n in mkt_news:
            parts.append(f'<div style="border-left:3px solid #F0D080;padding:6px 10px;margin:6px 0;background:#FFFBF0;"><a href="{n["link"]}" style="color:#0F2540;text-decoration:none;font-size:13px;"><strong>{n["title"]}</strong></a><div style="font-size:11px;color:#888;margin-top:2px;">{n["source"]} \xb7 {n["pub"]} \xb7 {n.get("desc","")[:100]}</div></div>')
        parts.append('</div>')

    # YouTube
    parts.append('<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">')
    parts.append('<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 4px;border-bottom:2px solid #F0D080;padding-bottom:6px;">\ud83d\udcfa Ce que disent les influenceurs</div>')
    parts.append('<p style="font-size:11px;color:#888;margin:0 0 12px;">V\xe9rifier manuellement avant votre d\xe9cision du week-end</p>')
    ICONS = {'Guillaume Fournier':'\ud83c\udf93','Rique Trading':'\ud83d\udcc8','Nicolas Cheron':'\ud83d\udd0d','JB Gambet':'\ud83d\udca1'}
    for name_yt, videos in youtube.items():
        icon = ICONS.get(name_yt, '\u25b6\ufe0f')
        parts.append(f'<div style="margin-bottom:14px;"><strong>{icon} {name_yt}</strong>')
        if videos:
            for v in videos:
                parts.append(f'<div style="border-left:3px solid #7C3AED;padding:5px 10px;margin:4px 0;background:#F8F5FF;font-size:12px;">\u25b6\ufe0f {v["title"]}</div>')
        else:
            parts.append('<div style="font-size:12px;color:#888;padding:4px 8px;">Impossible de r\xe9cup\xe9rer les vid\xe9os \u2014 v\xe9rifier manuellement.</div>')
        parts.append('</div>')
    parts.append('</div>')

    # Footer
    parts.append(f'<div style="text-align:center;padding:16px;color:#888;font-size:11px;">VAL.PEA \xb7 {date_fr} \xb7 Non-conseil en investissement \xb7 Sources : Yahoo Finance, RSS presse, YouTube</div></div></body></html>')
    return '\n'.join(parts)

# ─── EMAIL SENDER ────────────────────────────────────────────────────────────
def send_mail(subject, html_body, attachments=None):
    # Toujours sauvegarder localement
    with open('mail_preview.html', 'w', encoding='utf-8') as f:
        f.write(html_body)
    print('-> mail_preview.html sauvegarde')

    if not SMTP_USER or not SMTP_TO:
        print('SMTP non configure (definir MAIL_USER, MAIL_PASS, MAIL_TO dans les secrets GitHub)')
        return

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = SMTP_TO
    msg.attach(MIMEText(html_body, 'html', 'utf-8'))

    if attachments:
        for path in (attachments or []):
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(path)}"')
                    msg.attach(part)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(SMTP_USER, SMTP_TO.split(','), msg.as_string())
        print(f'Mail envoye a {SMTP_TO}')
    except Exception as e:
        print(f'Erreur SMTP: {e}')

# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    now = datetime.now()
    print(f'VAL.PEA generate_reports_v2 --- {now.strftime("%Y-%m-%d %H:%M")}')

    html_file = 'index.html'
    if not os.path.exists(html_file):
        print(f'ERROR: {html_file} not found'); sys.exit(1)

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    try:
        from generate_reports import parse_stocks, parse_ptf, calc_qarp, gen_avis
        from generate_reports import generate_revue_vendredi, generate_signaux_dimanche
        stocks_all = parse_stocks(html_content)
        ptf_raw = parse_ptf(html_content)
    except Exception as e:
        print(f'Import error: {e}'); stocks_all = []; ptf_raw = []

    print(f'{len(stocks_all)} actions, {len(ptf_raw)} positions')

    # Signaux
    signals = []
    for s in stocks_all:
        if s.get('score') != 'A': continue
        try:
            qarp = calc_qarp(s)
            if qarp['total'] < 70: continue
            if not (s.get('in_zone') or s.get('dcf_zone')): continue
            s['qarp'] = qarp
            signals.append(s)
        except: pass
    signals.sort(key=lambda x: x.get('qarp', {}).get('total', 0), reverse=True)
    print(f'{len(signals)} signaux')

    # Portefeuille
    portfolio = []
    for pos in ptf_raw:
        s = next((x for x in stocks_all if x['ticker'] == pos['ticker']), None)
        if not s: continue
        cours = s['price']
        pnl = round((cours - pos['pru']) * pos['qty'], 2)
        pct = round((cours - pos['pru']) / pos['pru'] * 100, 2) if pos['pru'] else 0
        try:
            qarp = calc_qarp(s)
        except:
            qarp = {}
        portfolio.append({**pos, 's': s, 'cours': cours, 'val': round(cours * pos['qty'], 2), 'pnl': pnl, 'pct': pct, 'qarp': qarp})

    print('\nFetching news...')
    all_news = fetch_all_news()

    print('\nFetching YouTube...')
    youtube = fetch_all_youtube()

    # Earnings de la semaine
    earnings_week = []
    try:
        if os.path.exists('fundamentals_log.json'):
            with open('fundamentals_log.json') as f:
                log = json.load(f)
            for e in log.get('earnings', []):
                if -7 <= e.get('days_away', 99) <= 0:
                    s = next((x for x in stocks_all if x['ticker'] == e['ticker']), None)
                    earnings_week.append({'ticker': e['ticker'], 'name': s['name'] if s else e['ticker'], 'summary': ''})
    except: pass

    # IA pour top 3 signaux
    ia_notes = {}
    if ANTHROPIC_API_KEY and signals:
        print('\nAnalyses IA...')
        for s in signals[:3]:
            note = ia_analysis_for_mail(s['ticker'], s['name'], s)
            if note:
                ia_notes[s['ticker']] = note
            time.sleep(2)

    print('\nGeneration mail HTML...')
    html_body = generate_html_mail({'now': now, 'signals': signals, 'portfolio': portfolio,
        'news': all_news, 'youtube': youtube, 'earnings_week': earnings_week, 'ia_notes': ia_notes})

    # DOCX en pieces jointes
    attachments = []
    try:
        MONTHS = {'January':'janvier','February':'f\xe9vrier','March':'mars','April':'avril',
               'May':'mai','June':'juin','July':'juillet','August':'ao\xfbt',
               'September':'septembre','October':'octobre','November':'novembre','December':'d\xe9cembre'}
        date_str = now.strftime('%d %B %Y')
        for en, fr in MONTHS.items():
            date_str = date_str.replace(en, fr)
        revue_path = f"VAL_PEA_Revue_{now.strftime('%Y%m%d')}.docx"
        generate_revue_vendredi(html_content, revue_path, date_str)
        attachments.append(revue_path)
        if signals:
            sig_path = f"VAL_PEA_Signaux_{now.strftime('%Y%m%d')}.docx"
            generate_signaux_dimanche(html_content, sig_path, date_str)
            attachments.append(sig_path)
    except Exception as e:
        print(f'DOCX error: {e}')

    subject = f"VAL.PEA --- {now.strftime('%d/%m/%Y')} --- {len(signals)} signal(s) * {len(all_news)} news"
    send_mail(subject, html_body, attachments)
    print('\nDONE')

if __name__ == '__main__':
    main()
