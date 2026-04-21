#!/usr/bin/env python3
"""
send_alerts.py - Génère et envoie le mail du soir format QARP
S'exécute après update_prices_v2.py dans le workflow GitHub Actions
"""

import re, json, os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def get_stocks(html_content):
    """Extraire les stocks depuis S[]"""
    s_start = html_content.find("const S=[")
    s_end_match = re.search(r'\n\];\s*\n\s*\n\s*// ═+\s*CALENDRIER', html_content[s_start:])
    s_end = s_start + s_end_match.start()
    s_code = html_content[s_start:s_end]
    
    stocks = []
    for m in re.finditer(r"\{ticker:'([^']+)'(.*?)(?=\n\n\{ticker:|\n\n\];)", s_code, re.DOTALL):
        ticker = m.group(1)
        block = m.group(0)
        
        def gn(key):
            mx = re.search(r'\b'+key+r':([\d.]+)', block)
            return float(mx.group(1)) if mx else 0
        def gs(key):
            mx = re.search(r"\b"+key+r":'([^']+)'", block)
            return mx.group(1) if mx else ''
        def gb(key):
            mx = re.search(r'\b'+key+r':(true|false)', block)
            return mx.group(1) == 'true' if mx else False
        
        s = {
            'ticker': ticker,
            'name': gs('name'),
            'sector': gs('sector'),
            'score': gs('score'),
            'price': gn('price'),
            'el': gn('el'), 'eh': gn('eh'),
            'stop': gn('stop'), 'o1': gn('o1'),
            'dcfm': gn('dcfm'),
            'roe': gn('roe'), 'margin': gn('margin'),
            'fcf': gn('fcf'), 'debt': gn('debt'),
            'pio': gn('pio'), 'rsi': gn('rsi'),
            'mm200': gn('mm200'), 'mm50': gn('mm50'),
            'yield': gn('yield'),
            'bpf': gb('bpf'),
        }
        
        # Calculs dérivés
        s['in_zone'] = s['el'] <= s['price'] <= s['eh'] if s['el'] and s['eh'] else False
        s['above_mm200'] = s['price'] > s['mm200'] if s['mm200'] else False
        s['good_rsi'] = 25 <= s['rsi'] <= 60 if s['rsi'] else False
        s['upside'] = round((s['dcfm'] - s['price']) / s['price'] * 100, 1) if s['price'] and s['dcfm'] else 0
        
        # Score QARP simplifié
        q = 20 if s['roe'] >= 25 else 16 if s['roe'] >= 18 else 11 if s['roe'] >= 12 else 6
        r_avg = (s['margin'] + s['fcf']) / 2
        r = 20 if r_avg >= 20 else 15 if r_avg >= 12 else 10 if r_avg >= 7 else 5
        b = 20 if s['debt'] <= 0.5 and s['pio'] >= 8 else 16 if s['debt'] <= 1 and s['pio'] >= 7 else 11 if s['debt'] <= 2 else 6
        v = 20 if s['upside'] >= 35 else 15 if s['upside'] >= 20 else 10 if s['upside'] >= 10 else 5 if s['upside'] >= 0 else 1
        mnt = 3
        if s['in_zone']: mnt += 7
        if s['above_mm200']: mnt += 7
        if s['good_rsi']: mnt += 3
        s['qarp'] = q + r + b + v + mnt
        
        # Signal
        trip = sum([s['in_zone'], s['above_mm200'], s['good_rsi']])
        s['signal'] = 'ULTIME' if s['qarp'] >= 70 and s['in_zone'] else \
                      'FORT' if s['qarp'] >= 55 else \
                      'SURVEILLER' if s['qarp'] >= 40 else None
        s['trip_count'] = trip
        
        # R/R
        risk = s['price'] - s['stop'] if s['stop'] else 1
        reward = s['o1'] - s['price'] if s['o1'] else 0
        s['rr'] = round(reward / risk, 1) if risk > 0 else 0
        
        stocks.append(s)
    
    return stocks

def score_color(score):
    if score >= 70: return '#16a34a'
    if score >= 55: return '#d97706'
    return '#2563eb'

def grade_color(grade):
    return {'A':'#16a34a','B':'#d97706','C':'#6b7280','D':'#dc2626'}.get(grade, '#6b7280')

def build_email_html(stocks, date_str):
    """Construire le mail HTML format QARP"""
    
    ultimes = [s for s in stocks if s['signal'] == 'ULTIME' and s['score'] in ['A','B']]
    forts   = [s for s in stocks if s['signal'] == 'FORT'   and s['score'] in ['A','B']]
    surveiller = [s for s in stocks if s['signal'] == 'SURVEILLER' and s['score'] == 'A']
    
    # Trier par QARP desc
    ultimes.sort(key=lambda x: -x['qarp'])
    forts.sort(key=lambda x: -x['qarp'])
    surveiller.sort(key=lambda x: -x['qarp'])
    
    def stock_card(s, highlight=False):
        sc = score_color(s['qarp'])
        gc = grade_color(s['score'])
        bg = '#f0fdf4' if highlight else '#f8fafc'
        border = '#22c55e' if highlight else '#e2e8f0'
        zone_badge = '<span style="background:#dcfce7;color:#16a34a;padding:1px 6px;border-radius:3px;font-size:10px;font-weight:700">✅ EN ZONE</span>' if s['in_zone'] else '<span style="background:#fee2e2;color:#dc2626;padding:1px 6px;border-radius:3px;font-size:10px">Hors zone</span>'
        
        return f'''
<div style="background:{bg};border:1px solid {border};border-radius:8px;padding:14px 16px;margin-bottom:10px;{'border-left:4px solid #22c55e;' if highlight else ''}">
  <table width="100%" cellpadding="0" cellspacing="0">
    <tr>
      <td style="vertical-align:top;width:60%">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">
          <span style="background:{gc};color:#fff;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:700;font-family:monospace">{s['score']}</span>
          <b style="font-size:15px;color:#0f2540">{s['ticker']}</b>
          <span style="color:#888;font-size:11px">{s['name'][:20]}</span>
          {zone_badge}
        </div>
        <table cellpadding="3" cellspacing="0" style="font-size:11px">
          <tr>
            <td style="color:#888;min-width:65px">Cours</td>
            <td><b style="font-family:monospace">{s['price']}€</b></td>
            <td style="padding-left:12px;color:#888">Zone achat</td>
            <td><b style="font-family:monospace">{s['el']}–{s['eh']}€</b></td>
          </tr>
          <tr>
            <td style="color:#888">Stop loss</td>
            <td><b style="color:#dc2626;font-family:monospace">{s['stop']}€</b></td>
            <td style="padding-left:12px;color:#888">Objectif</td>
            <td><b style="color:#16a34a;font-family:monospace">{s['o1']}€</b></td>
          </tr>
          <tr>
            <td style="color:#888">Upside DCF</td>
            <td><b style="color:{'#16a34a' if s['upside']>20 else '#d97706'};font-family:monospace">{'+' if s['upside']>0 else ''}{s['upside']}%</b></td>
            <td style="padding-left:12px;color:#888">R/R</td>
            <td><b style="font-family:monospace">{s['rr']}x</b></td>
          </tr>
          <tr>
            <td style="color:#888">ROE</td>
            <td><b style="font-family:monospace">{s['roe']}%</b></td>
            <td style="padding-left:12px;color:#888">Piotroski</td>
            <td><b style="font-family:monospace">{int(s['pio'])}/9</b></td>
          </tr>
        </table>
      </td>
      <td style="vertical-align:top;text-align:right;padding-left:10px">
        <div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:8px;padding:12px 16px;display:inline-block;min-width:80px;text-align:center">
          <div style="font-size:28px;font-weight:700;color:{sc};font-family:monospace">{s['qarp']}</div>
          <div style="font-size:9px;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:1px">/100 QARP</div>
          <div style="margin-top:6px;font-size:9px;color:#f0d080;font-weight:700">
            {'🚀 ULTIME' if s['signal']=='ULTIME' else '✅ FORT' if s['signal']=='FORT' else '👁️ SURVEILLER'}
          </div>
        </div>
        <div style="margin-top:8px;font-size:10px;color:#888;text-align:right">
          {'🔵 RSI ' if s['good_rsi'] else ''}{int(s['rsi']) if s['rsi'] else ''}{'  🟡 ↑MM200' if s['above_mm200'] else ''}
        </div>
      </td>
    </tr>
  </table>
</div>'''

    def section(title, color, items, max_items=5):
        if not items: return ''
        cards = ''.join(stock_card(s, highlight=(s['signal']=='ULTIME')) for s in items[:max_items])
        return f'''
<div style="margin-bottom:24px">
  <div style="background:{color};color:#fff;padding:10px 16px;border-radius:6px 6px 0 0;font-size:13px;font-weight:700;display:flex;justify-content:space-between">
    <span>{title}</span>
    <span style="opacity:.8">{len(items)} action{'s' if len(items)>1 else ''}</span>
  </div>
  <div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 6px 6px;padding:12px">
    {cards}
  </div>
</div>'''

    today_fr = datetime.now().strftime('%A %d %B %Y').capitalize()
    nb_zone = sum(1 for s in stocks if s['in_zone'])
    nb_a = sum(1 for s in stocks if s['score']=='A')

    html = f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f1f5f9;font-family:'Helvetica Neue',Arial,sans-serif">
<div style="max-width:680px;margin:0 auto;padding:20px">

  <!-- HEADER -->
  <div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:12px;padding:24px 28px;margin-bottom:20px">
    <div style="font-size:9px;font-family:monospace;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:3px;margin-bottom:8px">
      VAL.PEA · CABINET QUANTITATIF · SBF250
    </div>
    <div style="font-size:22px;font-weight:700;color:#f0d080;font-family:Georgia,serif;margin-bottom:4px">
      Radar du soir — {today_fr}
    </div>
    <div style="font-size:12px;color:rgba(255,255,255,.6)">
      {len(stocks)} valeurs analysées · {nb_a} Grade A · {nb_zone} en zone achat · {len(ultimes)} signaux ultimes
    </div>
    <!-- STATS RAPIDES -->
    <div style="display:flex;gap:12px;margin-top:16px;flex-wrap:wrap">
      {''.join(f'<div style="background:rgba(255,255,255,.08);border-radius:6px;padding:8px 14px;text-align:center"><div style="font-size:18px;font-weight:700;color:#f0d080;font-family:monospace">{v}</div><div style="font-size:9px;color:rgba(255,255,255,.4);text-transform:uppercase">{l}</div></div>' for v, l in [(len(ultimes),'Signaux ultimes'),(len(forts),'Signaux forts'),(nb_zone,'En zone achat'),(len(surveiller),'A surveiller')])}
    </div>
  </div>

  {section('🚀 Signaux Ultimes — Score ≥70, en zone achat', '#16a34a', ultimes)}
  {section('✅ Signaux Forts — Score ≥55 (Grade A/B)', '#d97706', forts)}
  {section('👁️ À Surveiller — Grade A en approche', '#2563eb', surveiller, max_items=3)}

  <!-- RAPPEL RÈGLE DIMANCHE -->
  <div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:14px 16px;margin-bottom:20px">
    <b style="color:#d97706">⚡ Règle du dimanche</b><br>
    <span style="font-size:12px;color:#78350f">
      Ce mail est un détecteur, pas une instruction d'achat. Toute décision se prend le dimanche matin après protocole complet : Score A + Zone + Triptyque + Psycho + Taille.
    </span>
  </div>

  <!-- FOOTER -->
  <div style="text-align:center;font-size:10px;color:#94a3b8;padding:12px">
    VAL.PEA Screener · Données indicatives · Non-conseil en investissement<br>
    Généré automatiquement le {date_str}
  </div>

</div>
</body>
</html>'''
    
    return html

# ─── MAIN ──────────────────────────────────────────────
if __name__ == '__main__':
    html_file = 'index.html'
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stocks = get_stocks(content)
    date_str = datetime.now().strftime('%d/%m/%Y à %H:%M')
    
    email_html = build_email_html(stocks, date_str)
    
    # Sauvegarder pour debug
    with open('alert_preview.html', 'w', encoding='utf-8') as f:
        f.write(email_html)
    
    # Envoyer via Gmail SMTP
    gmail_user = os.environ.get('GMAIL_USER')
    gmail_pass = os.environ.get('GMAIL_PASS')
    recipient  = os.environ.get('RECIPIENT', gmail_user)
    
    if not gmail_user or not gmail_pass:
        print("⚠️  GMAIL_USER/GMAIL_PASS non configurés — mail non envoyé")
        print(f"Preview sauvé: alert_preview.html")
    else:
        ultimes = [s for s in stocks if s['signal'] == 'ULTIME' and s['score'] in ['A','B']]
        forts   = [s for s in stocks if s['signal'] == 'FORT'   and s['score'] in ['A','B']]
        
        subject = f"VAL.PEA · {datetime.now().strftime('%d/%m')} · {len(ultimes)} ultime(s) · {len(forts)} fort(s)"
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = gmail_user
        msg['To'] = recipient
        msg.attach(MIMEText(email_html, 'html', 'utf-8'))
        
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(gmail_user, gmail_pass)
                smtp.sendmail(gmail_user, recipient, msg.as_string())
            print(f"✅ Mail envoyé: {subject}")
        except Exception as e:
            print(f"❌ Erreur envoi: {e}")
    
    # Telegram
    tg_token = os.environ.get('TELEGRAM_TOKEN')
    tg_chat  = os.environ.get('TELEGRAM_CHAT_ID')
    if tg_token and tg_chat:
        import urllib.request
        ultimes = [s for s in stocks if s['signal'] == 'ULTIME' and s['score'] in ['A','B']]
        forts   = [s for s in stocks if s['signal'] == 'FORT'   and s['score'] in ['A','B']]
        
        tg_msg = f"📊 *VAL.PEA — Radar du soir*\n_{datetime.now().strftime('%d/%m/%Y %H:%M')}_\n\n"
        if ultimes:
            tg_msg += f"🚀 *SIGNAUX ULTIMES ({len(ultimes)})*\n"
            for s in ultimes[:5]:
                tg_msg += f"  • *{s['ticker']}* {s['name'][:15]} — {s['qarp']}/100 QARP — cours {s['price']}€\n"
        if forts:
            tg_msg += f"\n✅ *SIGNAUX FORTS ({len(forts)})*\n"
            for s in forts[:5]:
                tg_msg += f"  • *{s['ticker']}* {s['name'][:15]} — {s['qarp']}/100 — cours {s['price']}€\n"
        tg_msg += f"\n_Règle du dimanche : décision uniquement le week-end_"
        
        payload = json.dumps({'chat_id': tg_chat, 'text': tg_msg, 'parse_mode': 'Markdown'})
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{tg_token}/sendMessage",
            data=payload.encode(), 
            headers={'Content-Type': 'application/json'}
        )
        try:
            urllib.request.urlopen(req, timeout=10)
            print("✅ Telegram envoyé")
        except Exception as e:
            print(f"⚠️  Telegram: {e}")
