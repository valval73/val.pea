#!/usr/bin/env python3
"""
VAL.PEA — Alerte Signal Ultime
================================
Script à ajouter dans GitHub Actions après update_prices.py
Analyse les signaux et envoie un email si confluence détectée

CONFIGURATION REQUISE dans GitHub Secrets :
  GMAIL_USER     : romence1@gmail.com
  GMAIL_PASSWORD : mot de passe d'application Gmail (pas ton vrai mdp)
  
Pour créer un mot de passe d'application Gmail :
  1. myaccount.google.com → Sécurité
  2. Validation en 2 étapes → Mots de passe des applications
  3. Créer → copier le code de 16 caractères
  4. Dans GitHub : Settings → Secrets → New secret → GMAIL_PASSWORD
"""

import re, json, smtplib, sys
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# ══════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════
GMAIL_USER     = os.environ.get('GMAIL_USER', 'romence1@gmail.com')
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD', '')
EMAIL_TO       = 'romence1@gmail.com'

# Seuils du Signal Ultime
SEUIL_SCORE_ULTIME  = 80   # Score /100 minimum pour alerte
SEUIL_SCORE_FORT    = 68   # Signal fort (email moins urgent)
MIN_GRADE           = ['A', 'B']  # Grades acceptés
MAX_RSI             = 55   # RSI max (éviter surachat)
MIN_RSI             = 25   # RSI min (éviter panique)

# ══════════════════════════════════════════════════
# LECTURE DES DONNÉES
# ══════════════════════════════════════════════════
def extract_stocks(html_path='index.html'):
    """Extrait les données des actions depuis index.html"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraire const S=[...]
    idx_s = content.find('const S=[')
    idx_etf = content.find('\nconst ETF=')
    if idx_s < 0 or idx_etf < 0:
        print("❌ Données S[] non trouvées")
        return []
    
    s_data = content[idx_s:idx_etf]
    
    # Parser les tickers et données clés
    stocks = []
    # Pattern pour extraire les données de chaque stock
    pattern = r"ticker:'([^']+)',name:'([^']+)'.*?price:([\d.]+),chg:([-\d.]+).*?rsi:([\d.]+).*?score:'([ABCD])'.*?zone:(true|false)"
    
    for m in re.finditer(pattern, s_data, re.DOTALL):
        try:
            ticker = m.group(1)
            name   = m.group(2)
            price  = float(m.group(3))
            chg    = float(m.group(4))
            rsi    = float(m.group(5))
            score  = m.group(6)
            zone   = m.group(7) == 'true'
            
            # Extraire vratio si disponible
            vratio_match = re.search(r"ticker:'" + re.escape(ticker) + r"'.*?vratio:([\d.]+)", s_data[:500000], re.DOTALL)
            vratio = float(vratio_match.group(1)) if vratio_match else 1.0
            
            # Extraire mm200
            mm200_match = re.search(r"ticker:'" + re.escape(ticker) + r"'.*?mm200:([\d.]+)", s_data[:500000], re.DOTALL)
            mm200 = float(mm200_match.group(1)) if mm200_match else 0
            
            # Extraire pio
            pio_match = re.search(r"ticker:'" + re.escape(ticker) + r"'.*?pio:(\d+)", s_data[:500000], re.DOTALL)
            pio = int(pio_match.group(1)) if pio_match else 0
            
            # Extraire zone DCF (el, eh)
            dcf_match = re.search(r"ticker:'" + re.escape(ticker) + r"'.*?el:([\d.]+),eh:([\d.]+),stop:([\d.]+),o1:([\d.]+)", s_data[:500000], re.DOTALL)
            el = float(dcf_match.group(1)) if dcf_match else 0
            eh = float(dcf_match.group(2)) if dcf_match else 0
            stop = float(dcf_match.group(3)) if dcf_match else 0
            o1   = float(dcf_match.group(4)) if dcf_match else 0
            
            stocks.append({
                'ticker': ticker, 'name': name, 'price': price,
                'chg': chg, 'rsi': rsi, 'score': score, 'zone': zone,
                'vratio': vratio, 'mm200': mm200, 'pio': pio,
                'el': el, 'eh': eh, 'stop': stop, 'o1': o1
            })
        except:
            continue
    
    print(f"✅ {len(stocks)} actions extraites")
    return stocks

# ══════════════════════════════════════════════════
# CALCUL DU SIGNAL ULTIME
# ══════════════════════════════════════════════════
def calc_signal(s):
    """
    Calcule le Signal Ultime pour une action.
    Retourne un score /100 et une liste de signaux.
    """
    score = 0
    signaux = []
    
    # 1. FONDAMENTAL — Grade + Piotroski
    if s['score'] == 'A':
        score += 25
        signaux.append(('🟢', f"Grade A — pépite confirmée"))
    elif s['score'] == 'B':
        score += 12
        signaux.append(('🟡', f"Grade B — qualité solide"))
    else:
        return None  # Grade C/D → pas d alerte
    
    if s['pio'] >= 8:
        score += 15
        signaux.append(('🟢', f"Piotroski {s['pio']}/9 — bilan excellent"))
    elif s['pio'] >= 7:
        score += 8
        signaux.append(('🟡', f"Piotroski {s['pio']}/9 — bilan solide"))
    
    # 2. VALORISATION — Zone DCF
    if s['el'] > 0 and s['eh'] > 0:
        in_zone = s['el'] <= s['price'] <= s['eh'] * 1.05
        if in_zone:
            score += 25
            signaux.append(('🟢', f"Zone DCF ({s['el']}€–{s['eh']}€) — valorisation attractive"))
        elif s['price'] < s['el'] * 1.1:
            score += 12
            signaux.append(('🟡', f"Proche zone DCF (cible: {s['el']}€)"))
    
    # 3. RSI — zone optimale 30-52
    if 30 <= s['rsi'] <= 42:
        score += 20
        signaux.append(('🟢', f"RSI {s['rsi']} — zone de survente idéale"))
    elif 42 < s['rsi'] <= 52:
        score += 10
        signaux.append(('🟡', f"RSI {s['rsi']} — zone neutre favorable"))
    elif s['rsi'] < 30:
        score += 5  # Trop vendu = peut continuer à baisser
        signaux.append(('⚠️', f"RSI {s['rsi']} — panique, attendre stabilisation"))
    
    # 4. VOLUME — accumulation institutionnelle
    vr = s['vratio']
    if vr >= 2.0:
        score += 20
        signaux.append(('🔴', f"Pic volume x{vr:.1f} — mouvement majeur"))
    elif vr >= 1.5:
        score += 15
        signaux.append(('🟠', f"Accumulation x{vr:.1f} — institutionnels actifs"))
    elif vr >= 1.2:
        score += 5
        signaux.append(('🟡', f"Volume légèrement élevé x{vr:.1f}"))
    
    # 5. TECHNIQUE — MM200
    if s['mm200'] > 0:
        dist = (s['price'] - s['mm200']) / s['mm200'] * 100
        if -5 <= dist <= 5:
            score += 10
            signaux.append(('🟡', f"Sur MM200 ({s['mm200']}€) ±{abs(dist):.1f}%"))
        elif s['price'] > s['mm200']:
            score += 5
            signaux.append(('🟢', f"Au-dessus MM200 +{dist:.1f}%"))
    
    # Calcul R/R
    rr = 0
    if s['o1'] > s['price'] > s['stop'] > 0:
        rr = (s['o1'] - s['price']) / (s['price'] - s['stop'])
    
    return {
        'ticker': s['ticker'],
        'name': s['name'],
        'score': min(100, score),
        'price': s['price'],
        'chg': s['chg'],
        'score_grade': s['score'],
        'rsi': s['rsi'],
        'vratio': s['vratio'],
        'zone_achat': s['el'] <= s['price'] <= s['eh'] * 1.05 if s['el'] > 0 else False,
        'el': s['el'], 'eh': s['eh'],
        'stop': s['stop'], 'o1': s['o1'],
        'rr': round(rr, 1),
        'signaux': signaux
    }

# ══════════════════════════════════════════════════
# GÉNÉRATION EMAIL HTML
# ══════════════════════════════════════════════════
def build_email(alertes_max, alertes_fort):
    """Génère le HTML de l'email d'alerte"""
    now = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  *{{box-sizing:border-box;margin:0;padding:0;}}
  body{{font-family:Arial,sans-serif;background:#f5f3ef;padding:10px;}}
  .container{{max-width:560px;margin:0 auto;background:#fff;border-radius:8px;overflow:hidden;}}
  .header{{background:#0f2540;padding:20px;text-align:center;}}
  .logo{{font-family:Georgia,serif;font-size:20px;font-weight:700;color:#f0d080;letter-spacing:2px;}}
  .subtitle{{font-size:10px;color:rgba(255,255,255,.5);text-transform:uppercase;margin-top:4px;}}
  .section{{padding:14px 16px;}}
  .section-title{{font-size:11px;font-weight:700;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;}}
  .signal-card{{background:#f0fdf4;border-radius:6px;padding:12px;margin-bottom:8px;border-left:4px solid #16a34a;}}
  .signal-card.fort{{border-left-color:#d97706;background:#fef3c7;}}
  .signal-top{{margin-bottom:8px;}}
  .ticker-row{{display:table;width:100%;}}
  .ticker-left{{display:table-cell;vertical-align:middle;}}
  .ticker-right{{display:table-cell;vertical-align:middle;text-align:right;width:70px;}}
  .ticker{{font-size:16px;font-weight:700;color:#0f2540;}}
  .name{{font-size:11px;color:#666;margin-top:2px;}}
  .score-badge{{font-size:18px;font-weight:700;color:#16a34a;}}
  .score-badge.fort{{color:#d97706;}}
  .grid{{width:100%;border-collapse:collapse;margin:8px 0;}}
  .grid td{{width:25%;padding:6px 4px;text-align:center;background:#fff;border-radius:4px;}}
  .cell-label{{font-size:9px;color:#888;text-transform:uppercase;display:block;}}
  .cell-value{{font-size:12px;font-weight:700;color:#0f2540;display:block;}}
  .signaux{{font-size:11px;line-height:1.9;color:#444;margin-top:6px;}}
  .btn{{display:block;text-align:center;background:#0f2540;color:#f0d080 !important;text-decoration:none;padding:12px;border-radius:6px;font-weight:700;font-size:13px;margin:14px 16px;}}
  .footer{{background:#f0ede8;padding:10px 16px;font-size:10px;color:#888;text-align:center;}}
  .tag{{display:inline-block;padding:2px 5px;border-radius:3px;font-size:9px;font-weight:700;}}
  .tag-zone{{background:#dcfce7;color:#16a34a;}}
  .tag-grade{{background:#0f2540;color:#f0d080;}}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="logo">VAL.PEA</div>
    <div class="subtitle">Radar Signaux — {now}</div>
  </div>
"""
    
    if alertes_max:
        html += f"""
  <div class="section">
    <div class="section-title">🚀 Signal Ultime — {{len(alertes_max)}} opportunité(s) maximale(s)</div>
"""
        for a in alertes_max:
            zone_tag = '<span class="tag tag-zone">✅ EN ZONE</span>' if a['zone_achat'] else ''
            html += f"""
    <div class="signal-card ultime">
      <div class="signal-top">
        <div>
          <span class="ticker">{{a['ticker']}}</span>
          <span class="tag tag-grade">{{a['score_grade']}}</span>
          {{zone_tag}}
          <div class="name">{{a['name']}}</div>
        </div>
        <div class="score-badge ultime">{{a['score']}}/100</div>
      </div>
      <table class="grid" cellpadding="4" cellspacing="2">
        <tr>
          <td><span class="cell-label">Cours</span><span class="cell-value">{{a['price']}}€</span></td>
          <td><span class="cell-label">Stop</span><span class="cell-value" style="color:#dc2626">{{a['stop']}}€</span></td>
          <td><span class="cell-label">Objectif</span><span class="cell-value" style="color:#16a34a">{{a['o1']}}€</span></td>
          <td><span class="cell-label">R/R</span><span class="cell-value" style="color:#1d4ed8">{{a['rr']}}x</span></td>
        </tr>
      </table>
      <div class="signaux">
"""
        for icon, txt in a['signaux']:
            html += f"        {{icon}} {{txt}}<br>\n"
        html += """      </div>
    </div>
"""
        html += "  </div>\n"
    
    if alertes_fort:
        html += f"""
  <div class="section">
    <div class="section-title">⚡ Signaux Forts — {{len(alertes_fort)}} à surveiller</div>
"""
        for a in alertes_fort:
            html += f"""
    <div class="signal-card fort">
      <div class="signal-top">
        <div>
          <span class="ticker">{{a['ticker']}}</span>
          <span class="tag tag-grade">{{a['score_grade']}}</span>
          <div class="name">{{a['name']}} · RSI {{a['rsi']}} · Vol x{{a['vratio']:.1f}}</div>
        </div>
        <div class="score-badge fort">{{a['score']}}/100</div>
      </div>
      <div class="signaux">
"""
        for icon, txt in a['signaux']:
            html += f"        {{icon}} {{txt}}<br>\n"
        html += "      </div>\n    </div>\n"
        html += "  </div>\n"
    
    html += """
  <a class="btn" href="https://valval73.github.io/val.pea">→ Ouvrir VAL.PEA Screener</a>
  <div class="footer">
    VAL.PEA · Données indicatives uniquement · Pas de conseil en investissement<br>
    Mis à jour automatiquement chaque jour ouvré à 17h35
  </div>
</div>
</body>
</html>
"""
    return html

# ══════════════════════════════════════════════════
# ENVOI EMAIL
# ══════════════════════════════════════════════════
def send_email(subject, html_content):
    """Envoie l'email via Gmail SMTP"""
    if not GMAIL_PASSWORD:
        print("⚠️ GMAIL_PASSWORD non configuré — email non envoyé")
        return False
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From']    = GMAIL_USER
    msg['To']      = EMAIL_TO
    
    msg.attach(MIMEText(html_content, 'html', 'utf-8'))
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Email envoyé → {EMAIL_TO}")
        return True
    except Exception as e:
        print(f"❌ Erreur email: {e}")
        return False

# ══════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════
if __name__ == '__main__':
    print("=" * 55)
    print(f"VAL.PEA Signal Ultime — {datetime.now().strftime('%d/%m %H:%M')}")
    print("=" * 55)
    
    stocks = extract_stocks('index.html')
    if not stocks:
        print("❌ Aucune donnée — arrêt")
        sys.exit(0)
    
    # Calculer les signaux
    resultats = []
    for s in stocks:
        if s['score'] not in MIN_GRADE:
            continue
        sig = calc_signal(s)
        if sig and sig['score'] >= SEUIL_SCORE_FORT:
            resultats.append(sig)
    
    # Dédupliquer par ticker (garder le meilleur score)
    seen = {}
    for r in resultats:
        if r['ticker'] not in seen or r['score'] > seen[r['ticker']]['score']:
            seen[r['ticker']] = r
    resultats = list(seen.values())

    # Trier par score décroissant
    resultats.sort(key=lambda x: x['score'], reverse=True)

    alertes_max  = [r for r in resultats if r['score'] >= SEUIL_SCORE_ULTIME and r['zone_achat']]
    alertes_fort = [r for r in resultats if SEUIL_SCORE_FORT <= r['score'] < SEUIL_SCORE_ULTIME]
    
    print(f"\n📊 Résultats:")
    print(f"  Signaux ULTIMES (≥{SEUIL_SCORE_ULTIME}/100) : {len(alertes_max)}")
    for a in alertes_max:
        print(f"    🚀 {a['ticker']} — {a['name']} — {a['score']}/100")
    
    print(f"  Signaux FORTS  ({SEUIL_SCORE_FORT}-{SEUIL_SCORE_ULTIME}/100)  : {len(alertes_fort)}")
    for a in alertes_fort[:5]:
        print(f"    ⚡ {a['ticker']} — {a['score']}/100")
    
    # Construire et envoyer l'email
    if alertes_max or alertes_fort:
        nb = len(alertes_max)
        if nb > 0:
            subject = f"VAL.PEA — {nb} Signal(s) Ultime(s) — {datetime.now().strftime('%d/%m')}"
        else:
            subject = f"VAL.PEA — {len(alertes_fort)} Signal(s) Fort(s) — {datetime.now().strftime('%d/%m')}"
        
        try:
            html = build_email(alertes_max[:10], alertes_fort[:5])
            send_email(subject, html)
        except Exception as e:
            print(f"⚠️ Email non envoyé: {e}")
            # Ne pas faire échouer le workflow
    else:
        print("\n✅ Aucun signal suffisant aujourd'hui — pas d'email")
    
    print("\n" + "=" * 55)
    print("✅ Analyse terminée")
    print("=" * 55)
