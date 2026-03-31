#!/usr/bin/env python3
"""
VAL.PEA — Macro Digest Hebdomadaire
Format : vraie lettre financière personnalisée, pas une liste de bullets
Dimanche 9h Paris
"""

import os, sys, smtplib, json, re, imaplib, email
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
import urllib.request, urllib.error

GMAIL_USER     = os.environ.get('GMAIL_USER', '').strip()
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD', '').strip()
ANTHROPIC_KEY  = os.environ.get('ANTHROPIC_API_KEY', '').strip()
EMAIL_TO       = os.environ.get('GMAIL_USER', '').strip()

if ANTHROPIC_KEY:
    print(f"✅ ANTHROPIC_API_KEY ({len(ANTHROPIC_KEY)} chars)")
else:
    print("⚠️ ANTHROPIC_API_KEY manquante")

# Sources financières utiles (filtrage strict)
SOURCES_FINANCIERES = [
    'newsletter-investir.lesechos.fr',
    'substack.com',
    'zonebourse.com',
    'masterbourse.fr',
    'lerevenu.com',
    'cafedelabourse.com',
    'moning.co',
]

# Sources à ignorer
SOURCES_IGNORER = [
    'fnac.com', 'sncf', 'cresus', 'infirmiers', 'boursobank',
    'investing.com', 'investing', 'boursedirect'
]

PROMPT_LETTRE = """
Tu es l'analyste financier personnel de Val, infirmière cardiologue à Monaco, 
investisseuse long terme avec 1000€/mois sur PEA, horizon 15 ans.

PROFIL DE VAL :
- Convictions : inflation structurelle (dette US), démondialisation, pricing power
- Portefeuille BPF : Hermès, Air Liquide, Legrand, Thales, Schneider, TotalEnergies, 
  EssilorLuxottica, GTT, LVMH, L'Oréal, Dassault, Safran, ASML, Edenred
- Règle : ne jamais vendre une BPF sauf thèse brisée
- Décisions : seulement le dimanche matin, jamais sous pression

TU DOIS ÉCRIRE UNE VRAIE LETTRE FINANCIÈRE PERSONNALISÉE.
Pas une liste de bullets. Pas un tableau de bord.
Une lettre comme si un gérant de patrimoine ami t'écrivait chaque dimanche matin.

TON STYLE :
- Chaleureux et direct, comme un ami expert
- Des phrases complètes, pas des tirets
- Des chiffres concrets quand disponibles
- Honnête même si les nouvelles sont mauvaises
- Maximum 450 mots — lisible en 3 minutes sur mobile

FORMAT OBLIGATOIRE (respecter ces 5 sections avec ces titres exacts) :

CE QUI S'EST PASSÉ CETTE SEMAINE
[2-3 phrases sur les faits marquants des marchés et de l'économie cette semaine.
Donner des chiffres précis. Pas de généralités.]

CE QUE ÇA CHANGE POUR TOI
[2-3 phrases qui connectent les événements de la semaine à ton portefeuille spécifique.
Mentionner des tickers précis. Être concret.]

CE QUI CONFIRME TES CONVICTIONS
[1-2 phrases maximum. Un fait précis, pas une liste.]

CE QUI MÉRITE TA VIGILANCE
[1-2 phrases honnêtes sur ce qui pourrait aller contre tes convictions.
Pas de langue de bois.]

TA DÉCISION DE CE DIMANCHE
[Une seule décision concrète avec chiffres : acheter/renforcer/attendre/tenir.
Exemple : "Avec 1000€ ce mois-ci : 300€ sur CW8, 500€ sur Hermès qui est en zone DCF 
à 1620€, 200€ en attente. Air Liquide T1 dans J-32 — ne pas renforcer avant les résultats."]

IMPORTANT :
- Mentionne des faits réels des newsletters reçues cette semaine
- Cite des chiffres précis (cours, %, dates)
- Reste honnête sur les incertitudes
- Ne survends pas les opportunités
"""

def extraire_texte_email(msg_obj):
    """Extrait le texte lisible d'un email"""
    body = ''
    if msg_obj.is_multipart():
        for part in msg_obj.walk():
            ct = part.get_content_type()
            if ct == 'text/plain':
                try:
                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    break
                except: pass
            elif ct == 'text/html' and not body:
                try:
                    html = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    # Extraction texte propre
                    text = re.sub(r'<style[^>]*>.*?</style>', ' ', html, flags=re.DOTALL)
                    text = re.sub(r'<script[^>]*>.*?</script>', ' ', text, flags=re.DOTALL)
                    text = re.sub(r'<[^>]+>', ' ', text)
                    text = re.sub(r'&[a-z#0-9]+;', ' ', text)
                    text = re.sub(r'\s+', ' ', text).strip()
                    body = text
                except: pass
    else:
        try:
            body = msg_obj.get_payload(decode=True).decode('utf-8', errors='ignore')
        except: body = ''
    
    # Nettoyer si HTML
    if '<' in body:
        body = re.sub(r'<style[^>]*>.*?</style>', ' ', body, flags=re.DOTALL)
        body = re.sub(r'<[^>]+>', ' ', body)
        body = re.sub(r'&[a-z#0-9]+;', ' ', body)
        body = re.sub(r'\s+', ' ', body).strip()
    
    return body[:4000]  # Plus de texte pour une meilleure analyse

def fetch_newsletters(days_back=7):
    """Récupère les newsletters financières des 7 derniers jours"""
    if not GMAIL_USER or not GMAIL_PASSWORD:
        print("⚠️ Credentials Gmail manquants")
        return []
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_USER, GMAIL_PASSWORD)
        mail.select('INBOX')
        since = (datetime.now() - timedelta(days=days_back)).strftime('%d-%b-%Y')
        newsletters = []

        for source in SOURCES_FINANCIERES:
            try:
                _, msgs = mail.search(None, f'(FROM "{source}" SINCE {since})')
                if not msgs[0]: continue
                
                # Prendre les 3 derniers par source
                for msg_id in msgs[0].split()[-3:]:
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
                        
                        # Filtrer les emails non financiers
                        subj_lower = subj.lower()
                        if any(x in subj_lower for x in ['promo', 'réduction', '-40%', 'soldes', 'offre']):
                            continue
                        
                        # Extraire texte
                        body = extraire_texte_email(msg_obj)
                        
                        if len(body) > 200:
                            newsletters.append({
                                'source': source,
                                'subject': subj[:100],
                                'body': body
                            })
                            print(f"  ✅ [{source}] {subj[:60]}")
                    except Exception as e:
                        print(f"  ⚠️ msg {msg_id}: {e}")
                        
            except Exception as e:
                print(f"  ⚠️ {source}: {e}")

        mail.logout()
        print(f"\n📧 {len(newsletters)} newsletters récupérées")
        return newsletters
        
    except Exception as e:
        print(f"❌ Gmail IMAP: {e}")
        return []

def analyser_avec_claude(newsletters):
    """Génère la lettre financière personnalisée"""
    if not ANTHROPIC_KEY:
        return None
    if not newsletters:
        return None

    # Construire le contexte avec le vrai contenu des newsletters
    contenu = ""
    for nl in newsletters[:6]:
        contenu += f"\n\n{'='*50}\n"
        contenu += f"SOURCE : {nl['source']}\n"
        contenu += f"SUJET : {nl['subject']}\n"
        contenu += f"CONTENU :\n{nl['body'][:3000]}\n"

    prompt = f"""{PROMPT_LETTRE}

Voici le contenu complet des newsletters de cette semaine :
{contenu}

Écris maintenant la lettre financière pour Val. 
Utilise les faits réels de ces newsletters — chiffres, noms d'actions, événements précis.
Ne fabrique pas d'informations qui ne sont pas dans les newsletters."""

    try:
        data = json.dumps({
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 1500,
            "messages": [{"role": "user", "content": prompt}]
        }).encode('utf-8')

        req = urllib.request.Request(
            'https://api.anthropic.com/v1/messages',
            data=data, method='POST',
            headers={
                'Content-Type': 'application/json',
                'x-api-key': ANTHROPIC_KEY,
                'anthropic-version': '2023-06-01'
            }
        )
        print("📡 Appel Claude API...")
        with urllib.request.urlopen(req, timeout=90) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            lettre = result['content'][0]['text']
            print(f"✅ Lettre générée ({len(lettre)} chars)")
            return lettre
    except urllib.error.HTTPError as e:
        print(f"❌ Claude HTTP {e.code}: {e.read().decode()[:200]}")
        return None
    except Exception as e:
        print(f"⚠️ Claude erreur: {e}")
        return None

def parser_sections(lettre):
    """Parse les 5 sections de la lettre"""
    if not lettre:
        return {}
    
    titres = {
        "CE QUI S'EST PASSÉ": 'semaine',
        "CE QUI S'EST PASSE": 'semaine',
        "CE QUE ÇA CHANGE": 'impact',
        "CE QUE CA CHANGE": 'impact',
        "CE QUI CONFIRME": 'confirme',
        "CE QUI MÉRITE": 'vigilance',
        "CE QUI MERITE": 'vigilance',
        "TA DÉCISION": 'decision',
        "TA DECISION": 'decision',
    }
    
    sections = {}
    current_key = None
    current_text = []
    
    for line in lettre.split('\n'):
        line_clean = line.strip()
        if not line_clean:
            if current_key and current_text:
                current_text.append('')
            continue
        
        matched = False
        for titre, key in titres.items():
            if titre in line_clean.upper():
                if current_key and current_text:
                    sections[current_key] = ' '.join(t for t in current_text if t).strip()
                current_key = key
                current_text = []
                matched = True
                break
        
        if not matched and current_key:
            # Retirer les marqueurs de liste
            clean = re.sub(r'^[•\-\*]\s*', '', line_clean)
            if clean:
                current_text.append(clean)
    
    if current_key and current_text:
        sections[current_key] = ' '.join(t for t in current_text if t).strip()
    
    return sections

def build_email_html(lettre, newsletters):
    """Construit l'email HTML — style lettre premium"""
    now = datetime.now()
    date_fr = now.strftime('%d %B %Y').lower()
    date_fr = date_fr[0].upper() + date_fr[1:]
    week = now.isocalendar()[1]
    
    sections = parser_sections(lettre) if lettre else {}
    
    # Couleurs et icônes par section
    config_sections = [
        ('semaine', "Ce qui s'est passé cette semaine", '📰', '#0f2540', '#e8eef5'),
        ('impact',  "Ce que ça change pour toi",         '🎯', '#1d4ed8', '#dbeafe'),
        ('confirme',"Ce qui confirme tes convictions",    '✅', '#16a34a', '#f0fdf4'),
        ('vigilance',"Ce qui mérite ta vigilance",        '⚠️', '#d97706', '#fef3c7'),
        ('decision',"Ta décision de ce dimanche",         '💡', '#7c3aed', '#f3e8ff'),
    ]
    
    h = '''<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: Georgia, 'Times New Roman', serif; background: #f0ede6; color: #222; }
.wrap { max-width: 560px; margin: 0 auto; }
.header { background: #0f2540; padding: 28px 24px 20px; }
.header-title { font-size: 28px; font-weight: 700; color: #f0d080; letter-spacing: 3px; font-family: Arial, sans-serif; }
.header-sub { font-size: 11px; color: rgba(255,255,255,.45); text-transform: uppercase; letter-spacing: 2px; margin-top: 6px; font-family: Arial; }
.header-date { font-size: 13px; color: rgba(255,255,255,.6); margin-top: 8px; font-family: Arial; font-style: italic; }
.card { background: #fff; border-radius: 0; }
.section { padding: 18px 22px; border-bottom: 1px solid #f0ede6; }
.section:last-child { border-bottom: none; }
.section-label { font-size: 9px; text-transform: uppercase; letter-spacing: 2px; font-family: Arial; font-weight: 700; margin-bottom: 8px; }
.section-text { font-size: 14px; line-height: 1.85; color: #333; }
.decision-box { background: #0f2540; padding: 20px 22px; }
.decision-label { font-size: 9px; text-transform: uppercase; letter-spacing: 2px; color: #f0d080; font-family: Arial; font-weight: 700; margin-bottom: 10px; }
.decision-text { font-size: 15px; line-height: 1.8; color: #fff; font-style: italic; }
.sources { background: #f8f6f2; padding: 10px 22px; }
.footer { background: #0f2540; padding: 12px 22px; text-align: center; font-size: 10px; color: rgba(255,255,255,.35); font-family: Arial; }
</style>
</head>
<body><div class="wrap">'''

    # Header
    h += f'''<div class="header">
  <div class="header-title">VAL.PEA</div>
  <div class="header-sub">Lettre hebdomadaire · Semaine {week}</div>
  <div class="header-date">{date_fr}</div>
</div>
<div class="card">'''

    if not lettre or not sections:
        # Fallback
        h += '<div class="section"><div class="section-text">Newsletters reçues cette semaine :<br><br>'
        for nl in newsletters:
            h += f'• <b>{nl["source"]}</b> : {nl["subject"]}<br>'
        h += '<br><em>(Analyse Claude indisponible — vérifier ANTHROPIC_API_KEY et crédits)</em>'
        h += '</div></div>'
    else:
        # 4 premières sections
        for key, titre, icone, color, bg in config_sections[:-1]:
            texte = sections.get(key, '')
            if not texte:
                continue
            h += f'''<div class="section" style="border-left: 4px solid {color}; background: {bg}20;">
  <div class="section-label" style="color: {color};">{icone} {titre}</div>
  <div class="section-text">{texte}</div>
</div>'''
        
        # Section décision — style spécial
        decision = sections.get('decision', '')
        if decision:
            h += f'''</div>
<div class="decision-box">
  <div class="decision-label">💡 Ta décision de ce dimanche</div>
  <div class="decision-text">{decision}</div>
</div>
<div class="card">'''

    # Sources
    if newsletters:
        seen = set()
        sources_txt = []
        for nl in newsletters:
            if nl['source'] not in seen:
                sources_txt.append(nl['source'])
                seen.add(nl['source'])
        h += f'<div class="sources" style="font-size:10px;color:#999;font-family:Arial">Sources analysées : {" · ".join(sources_txt)}</div>'

    h += '</div>'
    h += '<div class="footer">VAL.PEA · Lettre personnalisée automatique · Données éducatives uniquement</div>'
    h += '</div></body></html>'
    return h

def send_email(subject, html):
    if not GMAIL_PASSWORD or not EMAIL_TO:
        print("⚠️ Credentials email manquants")
        return False
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = GMAIL_USER
        msg['To'] = EMAIL_TO
        msg.attach(MIMEText(html, 'html', 'utf-8'))
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(GMAIL_USER, GMAIL_PASSWORD)
            s.send_message(msg)
        print(f"✅ Email envoyé à {EMAIL_TO}")
        return True
    except Exception as e:
        print(f"❌ Email: {e}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print(f"VAL.PEA Macro Digest — {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 60)
    
    print("\n📥 Récupération newsletters...")
    newsletters = fetch_newsletters(days_back=7)
    
    print("\n✍️  Rédaction de la lettre...")
    lettre = analyser_avec_claude(newsletters)
    
    if lettre:
        print("\n--- APERÇU ---")
        print(lettre[:400] + "...")
    
    week = datetime.now().isocalendar()[1]
    sujet = f"VAL.PEA — Semaine {week} — {datetime.now().strftime('%d/%m')}"
    html = build_email_html(lettre, newsletters)
    send_email(sujet, html)
    print("\n✅ Terminé")
