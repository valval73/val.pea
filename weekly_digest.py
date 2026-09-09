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

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'

# ─── LECTURE DEPUIS data.js (source unique de verite) ────────────────────
# L'ancienne version lisait index.html, qui contenait le tableau de
# donnees en dur -- depuis la correction de la cause racine (08/09/2026,
# index.html charge desormais data.js en externe), ce mail lisait un
# fichier qui ne contient plus aucune action. Corrige le 09/09/2026 :
# lecture directe de data.js, et filtre sur le grade A recalcule par
# fetch_fundamentals.py plutot que de recalculer un score BAM parallele
# en JS-parse, pour eviter d'avoir deux methodes de notation qui peuvent
# diverger.
MOAT_CRITERIA_LABELS = [
    "Modele economique clair", "Produits essentiels", "Achats reguliers",
    "Base clients large/diversifiee", "Attachement client / cout de changement",
    "Effet de reseau", "Leadership sectoriel", "Avantage competitif durable",
    "Pricing power", "Potentiel de croissance", "Faible dependance tech externe",
    "Management aligne actionnaires"
]

def parse_stocks(datajs_content):
    stocks = []
    seen = set()
    for m in re.finditer(r"\{ticker:'([^']+)'(.*?)(?=\n\n\{ticker:|\n\n\];)", datajs_content, re.DOTALL):
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

        score = gs('score')
        if score != 'A':
            continue  # on ne garde que le grade A -- demande explicite du 09/09/2026

        price = gn('price'); dcfm = gn('dcfm'); mm200 = gn('mm200')
        upside = round((dcfm - price)/price*100, 1) if price and dcfm else 0
        el = gn('el'); eh = gn('eh'); stop = gn('stop'); o1 = gn('o1')
        in_zone = price > 0 and el > 0 and eh > 0 and el <= price <= eh
        roe = gn('roe'); margin = gn('margin'); debt = gn('debt'); pio = gn('pio')

        # Grille moat notee (si evaluee via l'interface de coche)
        moat_m = re.search(r'moatChk:\[([^\]]*)\]', block)
        moat_pct = None
        moat_answered = 0
        if moat_m:
            vals = [x.strip() for x in moat_m.group(1).split(',') if x.strip() != '']
            nums = []
            for v in vals:
                try: nums.append(float(v))
                except: pass
            if nums:
                moat_answered = len(nums)
                moat_pct = round(sum(nums)/len(nums)*100)

        risk = price - stop if stop and price > stop else 1
        reward = o1 - price if o1 else 0
        rr = round(reward/risk, 1) if risk > 0 else 0

        s = {
            'ticker': ticker, 'name': gs('name'), 'sector': gs('sector'),
            'score': score, 'price': price, 'upside': upside,
            'el': el, 'eh': eh, 'stop': stop, 'o1': o1,
            'dcfm': dcfm, 'roe': roe, 'margin': margin,
            'debt': debt, 'pio': pio, 'mm200': mm200,
            'in_zone': in_zone, 'moat_pct': moat_pct, 'moat_answered': moat_answered,
            'thesis': gdb('thesis'), 'contra': gdb('contra'),
            'rr': rr,
        }
        stocks.append(s)
    return sorted(stocks, key=lambda x: (-1 if x['in_zone'] else 0, -(x['upside'] or 0)))

def research_moat(s):
    """Recherche reelle (web search active) des 12 criteres de la grille
    moat pour une action Grade A -- c'est la vraie valeur-ajoutee du mail
    par rapport a juste regarder le screener en direct (demande du
    09/09/2026). Regle d'honnetete stricte : si la recherche ne trouve
    pas assez d'info sur un critere precis, le score est null et la note
    dit "information insuffisante" -- jamais invente. Meme principe que
    la correction "recherche infructueuse" faite plus tot sur les
    influenceurs."""
    if not ANTHROPIC_KEY: return None
    criteres_txt = '\n'.join(f"{i+1}. {c}" for i, c in enumerate(MOAT_CRITERIA_LABELS))
    prompt = (f"Tu es analyste actions. Recherche sur le web des informations reelles et "
              f"recentes sur {s['name']} ({s['ticker']}, cotee a Paris) -- rapport annuel, "
              f"lettre aux actionnaires, presentations investisseurs, articles d'analystes serieux.\n\n"
              f"Pour CHACUN des 12 criteres suivants, donne une note basee UNIQUEMENT sur ce que "
              f"tu trouves reellement en cherchant -- jamais une supposition :\n{criteres_txt}\n\n"
              f"Note : 1 = Bien, 0.5 = Moyen, 0 = Pas bien, null = information insuffisante trouvee "
              f"(n'invente JAMAIS une note sans base reelle -- null est une reponse honnete valide).\n\n"
              f"Reponds UNIQUEMENT en JSON strict, rien d'autre :\n"
              f'{{"scores":[note1,note2,...note12],"notes":["justification courte 1",...],"sources":["url ou nom de source",...]}}')
    try:
        payload = json.dumps({
            'model': 'claude-sonnet-5', 'max_tokens': 1200,
            'tools': [{'type': 'web_search_20250305', 'name': 'web_search', 'max_uses': 8}],
            'messages': [{'role': 'user', 'content': prompt}]
        }).encode()
        req = ur.Request('https://api.anthropic.com/v1/messages', data=payload,
            headers={'Content-Type': 'application/json', 'x-api-key': ANTHROPIC_KEY, 'anthropic-version': '2023-06-01'})
        with ur.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
        text_blocks = [b['text'] for b in d.get('content', []) if b.get('type') == 'text']
        full_text = ' '.join(text_blocks)
        jm = re.search(r'\{.*\}', full_text, re.DOTALL)
        if not jm: return None
        parsed = json.loads(jm.group())
        scores = parsed.get('scores', [])
        notes = parsed.get('notes', [])
        sources = parsed.get('sources', [])
        if len(scores) != 12: return None
        clean_scores = [float(v) if v is not None and str(v).lower() != 'null' else None for v in scores]
        return {'scores': clean_scores, 'notes': notes[:12], 'sources': sources[:5]}
    except Exception as e:
        print(f"  Recherche moat {s['ticker']}: {e}")
        return None

def patch_moat_scores(results):
    """Ecrit les scores moat trouves dans data.js -- pour que ca reste
    sur le screener, pas juste dans le mail (demande explicite du
    09/09/2026)."""
    if not results: return 0
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    for ticker, r in results.items():
        tp = content.find(f"ticker:'{ticker}'")
        if tp == -1: continue
        np_ = content.find("ticker:'", tp + 1)
        block_end = np_ if np_ > -1 else len(content)
        block = content[tp:block_end]
        vals_str = ','.join('null' if v is None else str(v) for v in r['scores'])
        new_field = f"moatChk:[{vals_str}]"
        if 'moatChk:[' in block:
            nb = re.sub(r"moatChk:\[[^\]]*\]", new_field, block, count=1)
        else:
            nb = block.replace("score:'", new_field + ",score:'", 1)
        if nb != block:
            block = nb
            updated += 1
        content = content[:tp] + block + content[block_end:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Grille moat ecrite dans data.js pour {updated} action(s)")
    return updated

def ia_analyse(s):
    if not ANTHROPIC_KEY: return ''
    moat_str = f"{s['moat_pct']}% ({s['moat_answered']}/12 criteres évalués)" if s['moat_pct'] is not None else 'non encore évalué'
    prompt = (f"Note investissement PEA pour {s['name']} ({s['ticker']}).\n"
              f"ROE {s['roe']}%, Marge {s['margin']}%, Dette {s['debt']}x, "
              f"Piotroski {int(s['pio'])}/9, Upside DCF {s['upside']}%, Grille moat notée: {moat_str}\n\n"
              "Format 4 lignes:\n"
              "VERDICT: [ACHETER/ATTENDRE/ÉVITER] à [X]€\n"
              "MOAT: [avantage durable — 1 phrase chiffrée]\n"
              "RISQUE: [principal risque concret]\n"
              "SIGNAL: [ENTRER/CONSERVER/SORTIR] — [raison courte]")
    try:
        payload = json.dumps({'model':'claude-sonnet-5','max_tokens':180,
            'messages':[{'role':'user','content':prompt}]}).encode()
        req = ur.Request('https://api.anthropic.com/v1/messages', data=payload,
            headers={'Content-Type':'application/json','x-api-key':ANTHROPIC_KEY,'anthropic-version':'2023-06-01'})
        with ur.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
        return d['content'][0]['text'].strip()
    except Exception as e:
        detail = ''
        if hasattr(e, 'read'):
            try: detail = ' | ' + e.read().decode('utf-8','ignore')[:400]
            except: pass
        print(f'  IA {s["ticker"]}: {e}{detail}')
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
    upside_str = ('+' if s['upside']>0 else '') + str(s['upside']) + '%'
    upside_col = '#16a34a' if s['upside']>15 else '#d97706' if s['upside']>0 else '#dc2626'

    # Grille moat notee
    if s['moat_pct'] is not None:
        moat_col = '#16a34a' if s['moat_pct']>=70 else '#d97706' if s['moat_pct']>=45 else '#dc2626'
        complet = s['moat_answered'] >= 12
        notes_html = ''
        if s.get('moat_notes'):
            items = ''.join(f'<li style="margin:2px 0">{n}</li>' for n in s['moat_notes'][:6] if n)
            notes_html = f'<ul style="margin:6px 0 0 0;padding-left:16px;font-size:9px;color:#555">{items}</ul>'
        sources_html = ''
        if s.get('moat_sources'):
            sources_html = f'<div style="font-size:8px;color:#aaa;margin-top:4px">Sources : {", ".join(s["moat_sources"][:3])}</div>'
        moat_html = (f'<div style="margin:6px 0;padding:8px;background:{moat_col}15;border:1px solid {moat_col}40;border-radius:6px;font-size:10px">'
                     f'<b style="color:{moat_col}">Grille Moat : {s["moat_pct"]}%</b> '
                     f'<span style="color:#888">({s["moat_answered"]}/12 critères{"" if complet else " -- évaluation partielle, recherche web"})</span>'
                     f'{notes_html}{sources_html}</div>')
    else:
        moat_html = '<div style="font-size:9px;color:#d97706;margin:4px 0;padding:6px;background:#fffbeb;border-radius:4px">⏳ Grille moat -- recherche prévue prochain envoi</div>'

    thesis_html = ''
    if s.get('thesis'):
        thesis_html = (f'<div style="margin-top:6px;padding:8px;background:#f0fdf4;border-left:3px solid #16a34a;font-size:10px;color:#1a4730;line-height:1.5">'
                       f'<b style="font-size:8px;text-transform:uppercase;color:#16a34a">Thèse d\'investissement</b><br>{s["thesis"][:200]}</div>')
    contra_html = ''
    if s.get('contra'):
        contra_html = (f'<div style="margin-top:4px;padding:8px;background:#fff5f5;border-left:3px solid #dc2626;font-size:10px;color:#7c2d2d;line-height:1.5">'
                       f'<b style="font-size:8px;text-transform:uppercase;color:#dc2626">Risque principal</b><br>{s["contra"][:180]}</div>')

    ia_html = ''
    if ia_note:
        ia_html = (f'<div style="margin-top:6px;background:#f0f9ff;border:1px solid #bae6fd;border-radius:6px;padding:8px;font-size:10px">'
                   f'<b style="color:#0369a1">🤖 Analyse IA</b><br>'
                   f'<pre style="font-family:Arial;margin:4px 0;white-space:pre-wrap;font-size:10px;color:#1e3a5f">{ia_note}</pre></div>')

    o1_pct = round((s['o1']-s['price'])/s['price']*100) if s['o1'] and s['price'] else 0

    return f'''<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:12px;border-left:4px solid #16a34a">
<table width="100%" cellpadding="0" cellspacing="0"><tr>
<td style="vertical-align:top">
<div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:4px">
<span style="background:#16a34a;color:#fff;padding:2px 8px;border-radius:3px;font-size:10px;font-weight:700">A</span>
<b style="font-size:16px;font-family:monospace;color:#0f2540">{s["ticker"]}</b>
<span style="color:#888;font-size:11px">{s["name"][:22]}</span>
{('<span style="background:#dcfce7;color:#16a34a;padding:1px 6px;border-radius:3px;font-size:9px;font-weight:700">EN ZONE</span>' if s["in_zone"] else '')}
</div>
<div style="font-size:9px;color:#94a3b8">{s.get("sector","")[:35]}</div>
</td>
</tr></table>

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
</tr>
</table>
{thesis_html}{contra_html}{ia_html}
</div>'''

# ─── BUILD EMAIL ──────────────────────────────────────────────────────────
def build_email(stocks, macro, date_fr):
    in_zone = [s for s in stocks if s['in_zone']]
    hors_zone = [s for s in stocks if not s['in_zone']]
    not_assessed = sum(1 for s in stocks if s['moat_pct'] is None)

    ia_notes = {}
    if ANTHROPIC_KEY:
        print('\n🤖 Analyse IA -- actions en zone (max 5)...')
        for s in in_zone[:5]:
            note = ia_analyse(s)
            if note: ia_notes[s['ticker']] = note
            time.sleep(1.5)

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

    def sig_section(title, col, items, ia_notes_map=None):
        if not items: return ''
        cards = ''.join(stock_card(s, (ia_notes_map or {}).get(s['ticker'],'')) for s in items)
        return (f'<div style="margin-bottom:20px">'
                f'<div style="background:{col};color:#fff;padding:10px 16px;border-radius:8px 8px 0 0;'
                f'font-size:12px;font-weight:700;display:flex;justify-content:space-between">'
                f'<span>{title}</span><span style="opacity:.7">{len(items)} valeur{"s" if len(items)>1 else ""}</span></div>'
                f'<div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 8px 8px;padding:12px">{cards}</div>'
                f'</div>')

    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  h4{{color:#0f2540;font-size:13px;margin:14px 0 6px;border-bottom:2px solid #f0d080;padding-bottom:4px;font-weight:700}}
  b{{color:#0f2540}} i{{color:#888}}
</style>
</head>
<body style="margin:0;padding:0;background:#f1f5f9;font-family:Helvetica Neue,Arial,sans-serif">
<div style="max-width:680px;margin:0 auto;padding:16px">

<div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:12px;padding:24px;margin-bottom:16px">
<div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:3px;margin-bottom:8px">
VAL.PEA · MÉTHODE B.A.M · BUFFETT · ACKMAN · MUNGER</div>
<div style="font-size:22px;font-weight:700;color:#f0d080;font-family:Georgia,serif">📊 Revue hebdomadaire -- Grade A</div>
<div style="font-size:13px;color:rgba(255,255,255,.7);margin-top:4px">{date_fr}</div>
<div style="display:flex;gap:12px;margin-top:14px;flex-wrap:wrap">
{"".join(f'<div style="background:rgba(255,255,255,.1);border-radius:6px;padding:8px 14px;text-align:center"><div style="font-size:20px;font-weight:700;color:#f0d080;font-family:monospace">{v}</div><div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase;margin-top:2px">{l}</div></div>' for v,l in [(len(stocks),"Grade A"),(len(in_zone),"En zone"),(len(stocks)-not_assessed,"Moat évalué")])}
</div>
</div>

<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:16px">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
<b style="font-size:11px;color:#0f2540;text-transform:uppercase;letter-spacing:1px">Contexte macro</b>
<span style="background:{macro_color}20;color:{macro_color};border:1px solid {macro_color}40;padding:3px 10px;border-radius:4px;font-size:10px;font-weight:700">{macro_label}</span>
</div>
<table width="100%" cellpadding="0" cellspacing="0">{macro_rows}</table>
</div>

{sig_section("🟢 Grade A — En zone d'achat", "#16a34a", in_zone, ia_notes)}
{sig_section("👁 Grade A — Hors zone (à surveiller)", "#2563eb", hors_zone)}

<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:14px;margin-bottom:16px">
<b style="font-size:10px;color:#d97706">📐 Rappel</b><br>
<span style="font-size:10px;color:#78350f;line-height:1.6">
Le grade A vient du calcul quantitatif (Piotroski, Altman, marge de sécurité DCF, ROE) -- la grille moat, elle, vient de ta lecture. Les deux ensemble comptent plus que l'un seul. {not_assessed} action{"s" if not_assessed!=1 else ""} Grade A n'{"ont" if not_assessed!=1 else "a"} pas encore de grille moat renseignée.
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
    in_zone = [s for s in stocks if s['in_zone']]
    def esc(t): return str(t).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    msg = f"📊 <b>VAL.PEA — Revue {date_str}</b>\n\n"
    msg += f"🎯 <b>Grade A : {len(stocks)}</b> ({len(in_zone)} en zone d'achat)\n\n"
    if in_zone:
        msg += f"🟢 <b>En zone ({len(in_zone)})</b>\n"
        for s in in_zone[:5]: msg += f" • <b>{esc(s['ticker'])}</b> {esc(s['name'][:14])} · +{s['upside']}%\n"
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

    if not os.path.exists('data.js'):
        print('❌ data.js introuvable'); sys.exit(1)
    with open('data.js','r',encoding='utf-8') as f:
        content = f.read()

    print('\n📊 Parsing des actions Grade A depuis data.js...')
    stocks = parse_stocks(content)
    n_zone = sum(1 for s in stocks if s['in_zone'])
    n_moat = sum(1 for s in stocks if s['moat_pct'] is not None)
    print(f'  {len(stocks)} actions Grade A · {n_zone} en zone d\'achat · {n_moat} avec grille moat évaluée')

    print('\n🔎 Recherche moat (web) -- actions non encore évaluées, max 10 par run...')
    to_research = [s for s in stocks if s['moat_pct'] is None][:10]
    moat_results = {}
    for s in to_research:
        print(f'  Recherche {s["ticker"]}...')
        r = research_moat(s)
        if r:
            moat_results[s['ticker']] = r
            answered = sum(1 for v in r['scores'] if v is not None)
            pct = round(sum(v for v in r['scores'] if v is not None) / answered * 100) if answered else None
            s['moat_pct'] = pct
            s['moat_answered'] = answered
            s['moat_notes'] = r['notes']
            s['moat_sources'] = r['sources']
            print(f'    -> {pct}% ({answered}/12 trouvés)')
        time.sleep(2)
    if moat_results:
        patch_moat_scores(moat_results)

    print('\n📡 Macro...')
    macro = fetch_macro()

    print('\n📨 Construction mail...')
    html = build_email(stocks, macro, date_fr)

    subject = f"VAL.PEA · Revue {now.strftime('%d/%m')} · {len(stocks)} Grade A · {n_zone} en zone"

    send(subject, html)
    send_telegram_summary(stocks, now.strftime('%d/%m'))
    print('\n✅ Done')
