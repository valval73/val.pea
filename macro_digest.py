#!/usr/bin/env python3
"""
VAL.PEA — Macro Digest Hebdomadaire
=====================================
Lit les newsletters financieres dans Gmail et envoie un resume
chaque dimanche matin via l API Claude (Anthropic).

CONFIGURATION dans GitHub Secrets :
  GMAIL_USER        : romence1@gmail.com
  GMAIL_PASSWORD    : mot de passe application Gmail
  ANTHROPIC_API_KEY : ta cle API Anthropic

POUR AJOUTER dans daily.yml — un job separe le dimanche :
  schedule:
    - cron: '0 7 * * 0'   # Dimanche 9h Paris
"""

import os, sys, smtplib, json, re
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Dependances
try:
    import urllib.request
    import base64
except ImportError:
    pass

# ══════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════
GMAIL_USER      = os.environ.get('GMAIL_USER', '')
GMAIL_PASSWORD  = os.environ.get('GMAIL_PASSWORD', '')
ANTHROPIC_KEY   = os.environ.get('ANTHROPIC_API_KEY', '').strip()
if ANTHROPIC_KEY:
    print(f"✅ ANTHROPIC_API_KEY chargee ({len(ANTHROPIC_KEY)} chars)")
else:
    print("⚠️ ANTHROPIC_API_KEY vide ou absente")
EMAIL_TO        = os.environ.get('GMAIL_USER', '')

# Sources a surveiller dans Gmail
SOURCES = [
    'newsletter-investir.lesechos.fr',  # Investir / Les Echos
    'newsletter.lesechos.fr',
    'substack.com',                      # TKer, Macro Compass, autres
    'zonebourse.com',                    # Morning Meeting
    'masterbourse.fr',                   # MasterBourse
    'lerevenu.com',                      # Le Revenu
    'cafedelabourse.com',                # Cafe de la Bourse
    'moning.co',                         # Suivi performance
    'investing.com',                     # Investing.com
    'morningstar.fr',                    # Morningstar
]

# Convictions de Val — filtre thematique
CONVICTIONS = """
Tu analyses les newsletters financieres pour Val, investisseuse francaise avec ces convictions :
1. Inflation structurelle forte sur 15 ans (dette US insoutenable, demondialisation)
2. Portefeuille : 30% ETF MSCI World (IA/croissance mondiale), 15% actions europeennes 
   resilientes inflation (pricing power : luxe, gaz industriels, energie), 
   15% dividendes croissants, 10% or/Bitcoin/matieres premieres, 
   10% obligations court terme (poudre seche), 20% immobilier/private equity
3. Horizon 15 ans, PEA principalement

Pour chaque newsletter, extrais UNIQUEMENT ce qui est pertinent pour ces convictions.
Ignore l immobilier residentiel, fiscalite personnelle, epargne retraite classique.
"""

# ══════════════════════════════════════
# LECTURE GMAIL
# ══════════════════════════════════════
def get_gmail_token():
    """Authentification Gmail via IMAP"""
    import imaplib
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_USER, GMAIL_PASSWORD)
        return mail
    except Exception as e:
        print(f"❌ Gmail IMAP erreur: {e}")
        return None

def fetch_recent_newsletters(days_back=7):
    """Recupere les newsletters des 7 derniers jours"""
    import imaplib, email
    from email.header import decode_header

    mail = get_gmail_token()
    if not mail:
        return []

    mail.select('INBOX')
    
    # Date de recherche
    since_date = (datetime.now() - timedelta(days=days_back)).strftime('%d-%b-%Y')
    
    newsletters = []
    
    for source in SOURCES:
        try:
            _, msgs = mail.search(None, f'(FROM "{source}" SINCE {since_date})')
            if not msgs[0]:
                continue
            
            msg_ids = msgs[0].split()[-3:]  # Max 3 derniers par source
            
            for msg_id in msg_ids:
                _, msg_data = mail.fetch(msg_id, '(RFC822)')
                msg = email.message_from_bytes(msg_data[0][1])
                
                # Sujet
                subject_raw = msg['Subject'] or ''
                subject = decode_header(subject_raw)[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode('utf-8', errors='ignore')
                
                # Corps du message
                body = ''
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            try:
                                body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                                break
                            except:
                                pass
                        elif part.get_content_type() == 'text/html' and not body:
                            try:
                                html = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                                # Extraction texte basique depuis HTML
                                body = re.sub(r'<[^>]+>', ' ', html)
                                body = re.sub(r'\s+', ' ', body)[:3000]
                            except:
                                pass
                else:
                    try:
                        body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                    except:
                        body = ''
                
                if body:
                    newsletters.append({
                        'source': source,
                        'subject': subject,
                        'date': msg['Date'],
                        'body': body[:2000]  # Limite pour l API
                    })
                    print(f"  ✅ {source}: {subject[:50]}")
        except Exception as e:
            print(f"  ⚠️ {source}: {e}")
    
    mail.logout()
    print(f"\n📧 {len(newsletters)} newsletters recuperees")
    return newsletters

# ══════════════════════════════════════
# ANALYSE PAR CLAUDE
# ══════════════════════════════════════
def analyze_with_claude(newsletters):
    """Envoie les newsletters a Claude pour analyse macro"""
    if not ANTHROPIC_KEY:
        print("⚠️ ANTHROPIC_API_KEY non configure")
        return generate_fallback_digest(newsletters)
    
    if not newsletters:
        return "Aucune newsletter recue cette semaine."
    
    # Construire le prompt
    content = ""
    for nl in newsletters[:8]:  # Max 8 newsletters
        content += f"\n\n=== {nl['source']} — {nl['subject']} ===\n{nl['body'][:1500]}"
    
    prompt = f"""{CONVICTIONS}

Voici les newsletters de la semaine :
{content}

Produis un RESUME MACRO pour Val en exactement ce format :

🌍 REGIME MACRO ACTUEL (2-3 phrases sur l environnement general)

📊 CE QUI CONFIRME TES CONVICTIONS
• [point 1]
• [point 2]  
• [point 3]

⚠️ CE QUI REMET EN QUESTION TES CONVICTIONS
• [point 1 ou "Rien de significatif cette semaine"]

🎯 IMPLICATIONS POUR TON PORTEFEUILLE
• ETF MSCI World (30%) : [action a envisager]
• Actions europeennes (15%) : [secteurs a surveiller]
• Or/Bitcoin (10%) : [signal]
• Liquidites (10%) : [deployer ou garder]

💡 LA QUESTION A SE POSER CETTE SEMAINE
[Une seule question strategique]

Sois direct, concis, actionnable. Maximum 300 mots au total."""

    try:
        import urllib.request, urllib.error
        data = json.dumps({
            "model": "claude-opus-4-20250514",
            "max_tokens": 1500,
            "messages": [{"role": "user", "content": prompt}]
        }).encode('utf-8')
        
        req = urllib.request.Request(
            'https://api.anthropic.com/v1/messages',
            data=data,
            method='POST',
            headers={
                'Content-Type': 'application/json',
                'x-api-key': ANTHROPIC_KEY,
                'anthropic-version': '2023-06-01'
            }
        )
        
        print(f"📡 Appel Claude API...")
        with urllib.request.urlopen(req, timeout=60) as response:
            raw = response.read().decode('utf-8')
            result = json.loads(raw)
            text = result['content'][0]['text']
            print(f"✅ Claude a répondu ({len(text)} chars)")
            return text
    
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        print(f"❌ Claude API HTTP {e.code}: {body[:300]}")
        return generate_fallback_digest(newsletters)
    except Exception as e:
        print(f"⚠️ Claude API erreur: {type(e).__name__}: {e}")
        return generate_fallback_digest(newsletters)

def generate_fallback_digest(newsletters):
    """Resume basique si Claude API indisponible"""
    if not newsletters:
        return "Aucune newsletter cette semaine."
    lines = ["📰 Newsletters recues cette semaine :"]
    for nl in newsletters:
        lines.append(f"• {nl['source']} : {nl['subject'][:80]}")
    lines.append("\n(Analyse Claude indisponible — verifier ANTHROPIC_API_KEY)")
    return '\n'.join(lines)

# ══════════════════════════════════════
# EMAIL HTML
# ══════════════════════════════════════
def build_digest_email(digest_text, newsletters):
    now = datetime.now().strftime('%d/%m/%Y')
    week = datetime.now().isocalendar()[1]
    
    # Convertir le texte en HTML
    html_digest = digest_text.replace('\n\n', '</p><p>').replace('\n', '<br>')
    html_digest = '<p>' + html_digest + '</p>'
    
    # Mettre en valeur les sections
    for emoji, color, bg in [
        ('🌍', '#0f2540', '#e8f4f8'),
        ('📊', '#16a34a', '#f0fdf4'),
        ('⚠️', '#d97706', '#fef3c7'),
        ('🎯', '#1d4ed8', '#dbeafe'),
        ('💡', '#7c3aed', '#f3e8ff'),
    ]:
        html_digest = html_digest.replace(
            emoji,
            f'</p><div style="background:{bg};border-radius:6px;padding:12px 14px;margin:10px 0;border-left:4px solid {color}">'
            f'<span style="font-size:16px">{emoji}</span>'
        )
    
    sources_list = ''
    seen = set()
    for nl in newsletters:
        if nl['source'] not in seen:
            sources_list += '<li>' + nl['source'] + '</li>'
            seen.add(nl['source'])
    
    h = '<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body style="font-family:Arial,sans-serif;background:#f5f3ef;padding:10px;margin:0">'
    h += '<div style="max-width:560px;margin:0 auto;background:#fff;border-radius:8px;overflow:hidden">'
    
    # Header
    h += '<div style="background:#0f2540;padding:20px;text-align:center">'
    h += '<div style="font-size:20px;font-weight:700;color:#f0d080;letter-spacing:2px">VAL.PEA</div>'
    h += '<div style="font-size:10px;color:rgba(255,255,255,.5);text-transform:uppercase;margin-top:4px">MACRO DIGEST — Semaine ' + str(week) + ' — ' + now + '</div>'
    h += '</div>'
    
    # Digest
    h += '<div style="padding:20px;font-size:13px;line-height:1.7;color:#333">'
    h += html_digest
    h += '</div>'
    
    # Sources
    if sources_list:
        h += '<div style="background:#f8f7f4;padding:12px 20px;font-size:11px;color:#888">'
        h += '<b>Sources analysees :</b><ul style="margin:4px 0;padding-left:16px">' + sources_list + '</ul>'
        h += '</div>'
    
    # Footer
    h += '<div style="background:#0f2540;padding:12px 20px;font-size:10px;color:rgba(255,255,255,.5);text-align:center">'
    h += 'VAL.PEA · Digest automatique · Données éducatives uniquement'
    h += '</div></div></body></html>'
    
    return h

def send_email(subject, html_content):
    if not GMAIL_PASSWORD:
        print("⚠️ GMAIL_PASSWORD manquant")
        return False
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = GMAIL_USER
        msg['To'] = EMAIL_TO
        msg.attach(MIMEText(html_content, 'html', 'utf-8'))
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(GMAIL_USER, GMAIL_PASSWORD)
            s.send_message(msg)
        print(f"✅ Digest envoye a {EMAIL_TO}")
        return True
    except Exception as e:
        print(f"❌ Erreur email: {e}")
        return False

# ══════════════════════════════════════
# MAIN
# ══════════════════════════════════════
if __name__ == '__main__':
    print("=" * 55)
    print(f"VAL.PEA Macro Digest — {datetime.now().strftime('%d/%m %H:%M')}")
    print("=" * 55)
    
    print("\n📥 Lecture des newsletters Gmail...")
    newsletters = fetch_recent_newsletters(days_back=7)
    
    print("\n🤖 Analyse macro par Claude...")
    digest = analyze_with_claude(newsletters)
    
    print("\nResume genere :")
    print("-" * 40)
    print(digest)
    print("-" * 40)
    
    week = datetime.now().isocalendar()[1]
    subject = f"VAL.PEA — Macro Digest Semaine {week} — {datetime.now().strftime('%d/%m')}"
    
    html = build_digest_email(digest, newsletters)
    send_email(subject, html)
    
    print("\n" + "=" * 55)
    print("✅ Macro Digest termine")
    print("=" * 55)
