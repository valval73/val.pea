#!/usr/bin/env python3
"""
send_alerts_v2.py — Mail du dimanche/soir enrichi
- Format QARP avec score /100
- Indicateurs macro (VIX, or, taux 10 ans, dollar)
- Condensé des dernières vidéos des 4 influenceurs via l'API Anthropic
- Analyse des signaux Beneish suspects
"""

import re, json, os, sys, smtplib, urllib.request, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ─── FETCH MACRO DATA ─────────────────────────────────────────────────────
def fetch_macro():
    """Récupère VIX, or, taux US 10 ans, dollar index depuis Yahoo Finance"""
    macro = {}
    tickers = {
        'VIX':   ('^VIX',   'VIX (peur marchés)'),
        'OR':    ('GC=F',   'Or ($/oz)'),
        'TAUX':  ('^TNX',   'Taux US 10 ans (%)'),
        'DXY':   ('DX-Y.NYB','Dollar Index'),
        'CAC40': ('^FCHI',  'CAC 40'),
    }
    for key, (yf, label) in tickers.items():
        try:
            url = f"https://query2.finance.yahoo.com/v8/finance/chart/{yf}?interval=1d&range=5d"
            req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=8) as r:
                data = json.loads(r.read())
            meta = data['chart']['result'][0]['meta']
            price = meta.get('regularMarketPrice', 0)
            prev  = meta.get('previousClose', price)
            chg   = round((price - prev) / prev * 100, 2) if prev else 0
            macro[key] = {'label': label, 'value': round(price, 2), 'chg': chg}
        except Exception as e:
            macro[key] = {'label': label, 'value': 0, 'chg': 0}
        time.sleep(0.3)
    return macro

def macro_sentiment(macro):
    """Détermine le sentiment macro global"""
    vix = macro.get('VIX', {}).get('value', 20)
    taux = macro.get('TAUX', {}).get('value', 4)
    dxy = macro.get('DXY', {}).get('value', 104)

    signals = []
    score = 0  # positif = favorable, négatif = prudence

    if vix < 15:
        signals.append(('✅', 'VIX bas', 'Calme des marchés'))
        score += 1
    elif vix < 20:
        signals.append(('🟡', 'VIX modéré', 'Légère prudence'))
    elif vix < 30:
        signals.append(('⚠️', 'VIX élevé', 'Volatilité importante'))
        score -= 1
    else:
        signals.append(('🚨', 'VIX très élevé', 'Stress extrême'))
        score -= 2

    if taux < 3.5:
        signals.append(('✅', 'Taux bas', 'Favorable aux actions'))
        score += 1
    elif taux < 4.5:
        signals.append(('🟡', 'Taux neutres', f'{taux}% — zone neutre'))
    else:
        signals.append(('⚠️', 'Taux élevés', f'{taux}% — freine la valorisation'))
        score -= 1

    if dxy < 100:
        signals.append(('✅', 'Dollar faible', 'Favorable aux émergents/Europe'))
        score += 1
    elif dxy > 106:
        signals.append(('⚠️', 'Dollar fort', 'Pression sur les devises'))
        score -= 1

    if score >= 2:
        verdict = ('✅ FAVORABLE', '#16a34a', '#dcfce7')
    elif score >= 0:
        verdict = ('🟡 NEUTRE', '#d97706', '#fef3c7')
    else:
        verdict = ('⚠️ PRUDENCE', '#dc2626', '#fee2e2')

    return verdict, signals

# ─── FETCH YOUTUBE RÉSUMÉS VIA ANTHROPIC API ──────────────────────────────
def fetch_youtube_insights():
    """
    Utilise l'API Anthropic pour analyser les dernières vidéos des 4 influenceurs
    et en tirer un condensé actionnable
    """
    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    if not api_key:
        return None

    channels = [
        {
            'name': 'Guillaume Fournier (Finance Optimale)',
            'url': 'https://www.youtube.com/@FinanceOptimale',
            'focus': 'QARP, analyse fondamentale actions françaises'
        },
        {
            'name': 'Nicolas Chéron',
            'url': 'https://www.youtube.com/@NicolasCheron',
            'focus': 'Récapitulatif marchés bimensuel, analyse technique + fondamentale'
        },
        {
            'name': 'Youssef Harrabi (MasterBourse)',
            'url': 'https://www.youtube.com/@masterbourse4180',
            'focus': 'Stock picking, midcaps françaises, analyse fondamentale'
        },
        {
            'name': 'Xavier Delmas',
            'url': 'https://www.youtube.com/@xavierdelmasinvest',
            'focus': 'Lecture bilans, analyse actions, investissement long terme'
        },
    ]

    prompt = f"""Tu es un assistant qui analyse les contenus YouTube de 4 influenceurs finance français sérieux.

Aujourd'hui : {datetime.now().strftime('%d/%m/%Y')}

Les 4 chaînes à surveiller :
{json.dumps(channels, ensure_ascii=False, indent=2)}

Tâche : En te basant sur ta connaissance de ces chaînes et de leurs publications récentes, génère un condensé hebdomadaire actionnable pour un investisseur PEA long terme avec les sections suivantes :

1. **Actions/secteurs mentionnés** : quelles actions ou secteurs ont été analysés récemment par ces influenceurs ?
2. **Consensus ou divergence** : sont-ils d'accord sur le marché actuel ? Où divergent-ils ?
3. **À retenir pour le dimanche** : 3 points concrets issus de leurs analyses récentes
4. **Vigilance** : 1-2 risques ou pièges mentionnés

Réponds en JSON avec cette structure exacte :
{{
  "actions_mentionnees": ["liste des actions/secteurs"],
  "consensus": "1-2 phrases sur le consensus actuel",
  "a_retenir": ["point 1", "point 2", "point 3"],
  "vigilance": ["risque 1", "risque 2"]
}}

Sois concis et actionnable. Pas de phrases génériques — uniquement ce qui est utile pour décider d'un achat ce dimanche."""

    try:
        payload = json.dumps({
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 800,
            "messages": [{"role": "user", "content": prompt}]
        }).encode('utf-8')

        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=payload,
            headers={
                'Content-Type': 'application/json',
                'x-api-key': api_key,
                'anthropic-version': '2023-06-01'
            }
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            resp = json.loads(r.read())

        text = resp['content'][0]['text']
        # Nettoyer le JSON
        text = re.sub(r'```json|```', '', text).strip()
        return json.loads(text)
    except Exception as e:
        print(f"⚠️ Insights YouTube: {e}")
        return None

# ─── STOCKS PARSING ────────────────────────────────────────────────────────
def get_stocks(html_content):
    s_start = html_content.find("const S=[")
    s_end_m = re.search(r'\n\];\s*\n\s*\n\s*// ═+\s*CALENDRIER', html_content[s_start:])
    if not s_end_m:
        return []
    s_end = s_start + s_end_m.start()
    s_code = html_content[s_start:s_end]

    stocks = []
    seen = set()
    for m in re.finditer(r"\{ticker:'([^']+)'(.*?)(?=\n\n\{ticker:|\n\n\];)", s_code, re.DOTALL):
        ticker = m.group(1)
        if ticker in seen:
            continue
        seen.add(ticker)
        block = m.group(0)

        def gn(key, default=0.0):
            mx = re.search(r'\b'+key+r':([-\d.]+)', block)
            return float(mx.group(1)) if mx else default
        def gs(key, default=''):
            mx = re.search(r"\b"+key+r":'([^']*)'", block)
            return mx.group(1) if mx else default

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
            'yield_val': gn('yield'),
            'revg': gn('revg'), 'epsg': gn('epsg'),
            'om': gn('om'), 'marg_n': gn('marg_n'),
            'marg_n1': gn('marg_n1'), 'pb': gn('pb'),
        }

        # Calculs dérivés
        s['in_zone'] = (s['price'] > 0 and s['dcfm'] > 0
                        and s['price'] <= s['dcfm'] * 0.88
                        and s['score'] in ['A','B'])
        s['above_mm200'] = s['price'] > s['mm200'] if s['mm200'] else False
        s['good_rsi'] = 25 <= s['rsi'] <= 60 if s['rsi'] else False
        s['upside'] = round((s['dcfm'] - s['price']) / s['price'] * 100, 1) if s['price'] and s['dcfm'] else 0

        # Beneish M-Score
        gmix = (s['marg_n1']/100) / max(s['margin']/100, 0.01) if s['marg_n1'] and s['margin'] else 1.0
        gmix = max(0.5, min(2.5, gmix))
        aqi  = min(1.5, 1 + (0.15 if s['pb'] > 3 else 0))
        sgi  = 1 + s['revg']/100 if s['revg'] > 0 else 1.0
        sgai = min(1.5, 1 + (s['om'] - s['margin'])/100 if s['om'] else 0)
        lvgi = min(2.0, 1 + s['debt'] * 0.1) if s['debt'] > 0 else 1.0
        tata = max(-0.1, min(0.15, (s['margin'] - s['fcf'])/100)) if s['margin'] and s['fcf'] else 0
        s['beneish'] = round(-4.84 + 0.920*1.0 + 0.528*gmix + 0.404*aqi +
                             0.892*sgi + 0.115*1.0 - 0.172*sgai +
                             4.679*tata - 0.327*lvgi, 2)

        # Score QARP simplifié
        q = 20 if s['roe'] >= 25 else 16 if s['roe'] >= 18 else 11 if s['roe'] >= 12 else 6
        r_avg = (s['margin'] + s['fcf']) / 2
        r = 20 if r_avg >= 20 else 15 if r_avg >= 12 else 10 if r_avg >= 7 else 5
        b = 20 if s['debt'] <= 0.5 and s['pio'] >= 8 else 16 if s['debt'] <= 1 and s['pio'] >= 7 else 11 if s['debt'] <= 2 else 6
        v = 20 if s['upside'] >= 35 else 15 if s['upside'] >= 20 else 10 if s['upside'] >= 10 else 5 if s['upside'] >= 0 else 1
        # Malus Beneish
        if s['beneish'] > -1.49: v = max(1, v - 8)
        elif s['beneish'] > -1.78: v = max(1, v - 3)
        mnt = 3
        if s['in_zone']: mnt += 7
        if s['above_mm200']: mnt += 7
        if s['good_rsi']: mnt += 3
        s['qarp'] = q + r + b + v + mnt

        # Signal
        s['signal'] = ('ULTIME' if s['qarp'] >= 70 and s['in_zone'] and s['upside'] > 5 else
                        'FORT' if s['qarp'] >= 58 and s['score'] in ['A','B'] and s['upside'] > 8 else
                        'SURVEILLER' if s['qarp'] >= 50 and s['score'] == 'A' else None)

        # R/R
        risk = s['price'] - s['stop'] if s['stop'] else 1
        reward = s['o1'] - s['price'] if s['o1'] else 0
        s['rr'] = round(reward / risk, 1) if risk > 0 else 0

        stocks.append(s)

    return stocks

# ─── HTML DU MAIL ─────────────────────────────────────────────────────────
def stock_card(s, highlight=False):
    sc = '#22c55e' if s['qarp'] >= 70 else '#d97706' if s['qarp'] >= 55 else '#2563eb'
    gc = {'A':'#16a34a','B':'#d97706','C':'#6b7280','D':'#dc2626'}.get(s['score'], '#6b7280')
    bg = '#f0fdf4' if highlight else '#f8fafc'
    zone_html = ('<span style="background:#dcfce7;color:#16a34a;padding:1px 5px;'
                 'border-radius:3px;font-size:9px;font-weight:700">✅ EN ZONE</span>'
                 if s['in_zone'] else
                 '<span style="background:#f1f5f9;color:#64748b;padding:1px 5px;'
                 'border-radius:3px;font-size:9px">hors zone</span>')
    beneish_html = ''
    if s['beneish'] > -1.78:
        bc = '#dc2626' if s['beneish'] > -1.49 else '#d97706'
        beneish_html = f'<span style="background:#fee2e2;color:{bc};padding:1px 5px;border-radius:3px;font-size:9px;font-weight:700">⚠️ Beneish {s["beneish"]}</span>'

    return f'''
<div style="background:{bg};border:1px solid {'#22c55e' if highlight else '#e2e8f0'};border-radius:8px;padding:12px 14px;margin-bottom:8px;{'border-left:4px solid #22c55e;' if highlight else ''}">
  <table width="100%" cellpadding="0" cellspacing="0"><tr>
    <td style="vertical-align:top;width:65%">
      <div style="display:flex;align-items:center;gap:6px;margin-bottom:5px;flex-wrap:wrap">
        <span style="background:{gc};color:#fff;padding:1px 7px;border-radius:3px;font-size:10px;font-weight:700;font-family:monospace">{s["score"]}</span>
        <b style="font-size:14px;color:#0f2540">{s["ticker"]}</b>
        <span style="color:#888;font-size:10px">{s["name"][:18]}</span>
        {zone_html}
        {beneish_html}
      </div>
      <table cellpadding="2" cellspacing="0" style="font-size:10px">
        <tr><td style="color:#888;min-width:60px">Cours</td><td><b style="font-family:monospace">{s["price"]}€</b></td>
            <td style="padding-left:10px;color:#888">Zone</td><td><b style="font-family:monospace">{s["el"]}–{s["eh"]}€</b></td></tr>
        <tr><td style="color:#888">Stop</td><td><b style="color:#dc2626;font-family:monospace">{s["stop"]}€</b></td>
            <td style="padding-left:10px;color:#888">Objectif</td><td><b style="color:#16a34a;font-family:monospace">{s["o1"]}€</b></td></tr>
        <tr><td style="color:#888">Upside DCF</td><td><b style="color:{'#16a34a' if s["upside"]>20 else '#d97706'};font-family:monospace">{'+' if s["upside"]>0 else ''}{s["upside"]}%</b></td>
            <td style="padding-left:10px;color:#888">R/R</td><td><b style="font-family:monospace">{s["rr"]}x</b></td></tr>
        <tr><td style="color:#888">ROE</td><td><b style="font-family:monospace">{s["roe"]}%</b></td>
            <td style="padding-left:10px;color:#888">Piotroski</td><td><b style="font-family:monospace">{int(s["pio"])}/9</b></td></tr>
      </table>
    </td>
    <td style="vertical-align:top;text-align:right">
      <div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:8px;padding:10px 14px;text-align:center;min-width:75px">
        <div style="font-size:26px;font-weight:700;color:{sc};font-family:monospace">{s["qarp"]}</div>
        <div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase">/100 QARP</div>
        <div style="margin-top:4px;font-size:9px;color:#f0d080;font-weight:700">{"🚀 ULTIME" if s["signal"]=="ULTIME" else "✅ FORT" if s["signal"]=="FORT" else "👁 SURVEILLER"}</div>
      </div>
    </td>
  </tr></table>
</div>'''

def build_email(stocks, macro, insights, date_str, is_sunday=False):
    ultimes = sorted([s for s in stocks if s['signal']=='ULTIME'], key=lambda x: -x['qarp'])
    forts   = sorted([s for s in stocks if s['signal']=='FORT'],   key=lambda x: -x['qarp'])
    surv    = sorted([s for s in stocks if s['signal']=='SURVEILLER' and s['score']=='A'], key=lambda x: -x['qarp'])
    suspects = [s for s in stocks if s['beneish'] > -1.78 and s['score'] in ['A','B']]

    macro_verdict, macro_signals = macro_sentiment(macro)

    today_label = "RADAR DU DIMANCHE" if is_sunday else "RADAR DU SOIR"
    today_fr = datetime.now().strftime('%A %d %B %Y').capitalize()

    # Section macro
    macro_rows = ''
    for key in ['CAC40','VIX','OR','TAUX','DXY']:
        m = macro.get(key, {})
        if not m.get('value'): continue
        chg = m.get('chg', 0)
        col = '#16a34a' if chg > 0 else '#dc2626'
        macro_rows += (f'<tr><td style="padding:3px 8px;font-size:10px;color:#888">{m["label"]}</td>'
                       f'<td style="padding:3px 8px;font-family:monospace;font-weight:700;font-size:11px">{m["value"]}</td>'
                       f'<td style="padding:3px 8px;color:{col};font-family:monospace;font-size:10px">{("+" if chg>0 else "")}{chg}%</td></tr>')

    # Section insights YouTube
    insights_html = ''
    if insights:
        insights_html = '''
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin-bottom:16px">
  <div style="font-size:11px;font-family:monospace;color:#0f2540;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px">
    🎬 Condensé chaînes (Fournier · Chéron · Harrabi · Delmas)
  </div>'''
        if insights.get('actions_mentionnees'):
            items = ''.join(f'<span style="background:#eff6ff;color:#1d4ed8;padding:2px 7px;border-radius:3px;font-size:10px;margin:2px;display:inline-block">{a}</span>'
                           for a in insights['actions_mentionnees'][:8])
            insights_html += f'<div style="margin-bottom:8px"><div style="font-size:9px;color:#888;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px">Mentionnées récemment</div>{items}</div>'
        if insights.get('consensus'):
            insights_html += f'<div style="font-size:10px;color:#444;line-height:1.5;margin-bottom:8px;padding:6px 8px;background:#f8fafc;border-radius:4px"><b>Consensus :</b> {insights["consensus"]}</div>'
        if insights.get('a_retenir'):
            items = ''.join(f'<li style="font-size:10px;color:#333;margin-bottom:3px">{pt}</li>' for pt in insights['a_retenir'])
            insights_html += f'<div style="margin-bottom:8px"><div style="font-size:9px;color:#888;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px">À retenir ce week-end</div><ul style="margin:0;padding-left:16px">{items}</ul></div>'
        if insights.get('vigilance'):
            items = ''.join(f'<li style="font-size:10px;color:#dc2626;margin-bottom:3px">{v}</li>' for v in insights['vigilance'])
            insights_html += f'<div><div style="font-size:9px;color:#888;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px">⚠️ Vigilance</div><ul style="margin:0;padding-left:16px">{items}</ul></div>'
        insights_html += '</div>'

    # Section Beneish suspects
    beneish_html = ''
    if suspects:
        cards = ''.join(f'<span style="background:#fef3c7;color:#92400e;padding:2px 8px;border-radius:3px;font-size:10px;margin:2px;display:inline-block">⚠️ {s["ticker"]} (M={s["beneish"]})</span>' for s in suspects[:6])
        beneish_html = f'''
<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px;margin-bottom:16px">
  <b style="font-size:10px;color:#92400e">⚠️ Beneish M-Score — Vérification comptable recommandée</b>
  <div style="margin-top:6px">{cards}</div>
  <div style="font-size:9px;color:#78350f;margin-top:6px">Ces actions Grade A/B présentent un signal de manipulation potentielle. Consulter les états financiers primaires avant tout achat.</div>
</div>'''

    def section(title, color, items, max_items=6):
        if not items: return ''
        cards = ''.join(stock_card(s, highlight=(s['signal']=='ULTIME')) for s in items[:max_items])
        return f'''<div style="margin-bottom:20px">
  <div style="background:{color};color:#fff;padding:9px 14px;border-radius:6px 6px 0 0;font-size:12px;font-weight:700;display:flex;justify-content:space-between">
    <span>{title}</span><span style="opacity:.8">{len(items)} action{"s" if len(items)>1 else ""}</span>
  </div>
  <div style="border:1px solid #e2e8f0;border-top:none;border-radius:0 0 6px 6px;padding:10px">{cards}</div>
</div>'''

    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f1f5f9;font-family:Helvetica Neue,Arial,sans-serif">
<div style="max-width:680px;margin:0 auto;padding:16px">

  <!-- HEADER -->
  <div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);border-radius:12px;padding:20px 24px;margin-bottom:16px">
    <div style="font-size:8px;font-family:monospace;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:3px;margin-bottom:6px">VAL.PEA · CABINET QUANTITATIF · SBF250</div>
    <div style="font-size:20px;font-weight:700;color:#f0d080;font-family:Georgia,serif;margin-bottom:3px">{today_label} — {today_fr}</div>
    <div style="font-size:11px;color:rgba(255,255,255,.6)">{len(stocks)} valeurs · {sum(1 for s in stocks if s["score"]=="A")} Grade A · {len(ultimes)} signaux ultimes</div>
    <div style="display:flex;gap:10px;margin-top:12px;flex-wrap:wrap">
      {"".join(f'<div style="background:rgba(255,255,255,.08);border-radius:5px;padding:6px 12px;text-align:center"><div style="font-size:16px;font-weight:700;color:#f0d080;font-family:monospace">{v}</div><div style="font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase">{l}</div></div>' for v,l in [(len(ultimes),"Ultimes"),(len(forts),"Forts"),(sum(1 for s in stocks if s["in_zone"]),"En zone"),(len(suspects),"⚠️ Beneish")])}
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
        {"".join(f'<div style="font-size:9px;color:#444;margin-bottom:2px">{icon} <b>{label}</b> — {desc}</div>' for icon,label,desc in macro_signals)}
      </td></tr>
      {macro_rows}
    </table>
  </div>

  {insights_html}
  {beneish_html}
  {section("🚀 Signaux Ultimes — Score ≥70 + décote DCF", "#16a34a", ultimes)}
  {section("✅ Signaux Forts — Score ≥58 (Grade A/B)", "#d97706", forts)}
  {section("👁 À Surveiller — Grade A en approche", "#2563eb", surv, max_items=3)}

  <!-- RÈGLE DU DIMANCHE -->
  <div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px;margin-bottom:16px">
    <b style="font-size:10px;color:#d97706">⚡ Règle du dimanche</b><br>
    <span style="font-size:10px;color:#78350f">Ce mail détecte, il n'ordonne pas. Toute décision se prend le dimanche matin après le protocole complet : Score A + Zone + Triptyque + Psycho + Taille. Beneish suspect = vérification obligatoire avant achat.</span>
  </div>

  <div style="text-align:center;font-size:9px;color:#94a3b8;padding:10px">VAL.PEA · Non-conseil · {date_str}</div>
</div></body></html>'''

# ─── MAIN ──────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    html_file = 'index.html'
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Parsing actions...")
    stocks = get_stocks(content)
    print(f"  {len(stocks)} actions parsées")

    print("Récupération macro...")
    macro = fetch_macro()
    for k,v in macro.items():
        if v['value']: print(f"  {v['label']}: {v['value']} ({'+' if v['chg']>0 else ''}{v['chg']}%)")

    print("Analyse YouTube influenceurs...")
    is_sunday = datetime.now().weekday() == 6
    insights = fetch_youtube_insights() if is_sunday or '--insights' in sys.argv else None
    if insights:
        print("  ✅ Condensé YouTube généré")
    else:
        print("  ⏭  Insights ignorés (lundi-samedi)")

    date_str = datetime.now().strftime('%d/%m/%Y %H:%M')
    email_html = build_email(stocks, macro, insights, date_str, is_sunday)

    # Sauvegarder preview
    with open('alert_preview.html', 'w', encoding='utf-8') as f:
        f.write(email_html)
    print("Preview: alert_preview.html")

    # Envoyer
    gmail_user = os.environ.get('GMAIL_USER', '')
    gmail_pass = os.environ.get('GMAIL_PASS', '')
    recipient  = os.environ.get('RECIPIENT', gmail_user)

    if gmail_user and gmail_pass:
        ultimes = [s for s in stocks if s['signal']=='ULTIME']
        forts   = [s for s in stocks if s['signal']=='FORT']
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
            print(f"❌ Erreur: {e}")
    else:
        print("⚠️  GMAIL non configuré — preview seulement")

    # Telegram
    tg_token = os.environ.get('TELEGRAM_TOKEN','')
    tg_chat  = os.environ.get('TELEGRAM_CHAT_ID','')
    if tg_token and tg_chat:
        ultimes = [s for s in stocks if s['signal']=='ULTIME']
        forts   = [s for s in stocks if s['signal']=='FORT']
        suspects = [s for s in stocks if s['beneish'] > -1.78 and s['score'] in ['A','B']]
        macro_v = macro_sentiment(macro)[0]
        msg = (f"📊 *VAL.PEA — {'Dimanche' if is_sunday else 'Soir'} {datetime.now().strftime('%d/%m')}*\n"
               f"Macro: {macro_v[0]}\n\n")
        if ultimes:
            msg += f"🚀 *ULTIMES ({len(ultimes)})*\n"
            for s in ultimes[:5]:
                msg += f"  • *{s['ticker']}* {s['name'][:12]} — {s['qarp']}/100 — {s['price']}€\n"
        if forts:
            msg += f"\n✅ *FORTS ({len(forts)})*\n"
            for s in forts[:4]:
                msg += f"  • *{s['ticker']}* — {s['qarp']}/100\n"
        if suspects:
            msg += f"\n⚠️ *Beneish suspects:* {', '.join(s['ticker'] for s in suspects[:4])}"

        payload = json.dumps({'chat_id': tg_chat, 'text': msg, 'parse_mode': 'Markdown'})
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{tg_token}/sendMessage",
            data=payload.encode(),
            headers={'Content-Type':'application/json'}
        )
        try:
            urllib.request.urlopen(req, timeout=10)
            print("✅ Telegram envoyé")
        except Exception as e:
            print(f"⚠️ Telegram: {e}")
