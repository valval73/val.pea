#!/usr/bin/env python3
"""
VAL.PEA — Macro Digest Hebdomadaire
Dimanche 9h — Analyse newsletters + recap Grade A
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
    print(f"✅ ANTHROPIC_API_KEY chargee ({len(ANTHROPIC_KEY)} chars)")
else:
    print("⚠️ ANTHROPIC_API_KEY manquante")

SOURCES = [
    'newsletter-investir.lesechos.fr',
    'newsletter.lesechos.fr',
    'substack.com',
    'zonebourse.com',
    'masterbourse.fr',
    'lerevenu.com',
    'cafedelabourse.com',
    'moning.co',
]

# Convictions de Val + actions BPF pour le recap
CONVICTIONS = """
Tu es l analyste personnel de Val, investisseuse francaise avec ces convictions long terme :
1. Inflation structurelle sur 15 ans (dette US insoutenable, demondialisation)
2. Portefeuille cible : 30% ETF MSCI World, 15% actions europeennes pricing power,
   15% dividendes croissants, 10% or/Bitcoin/commodites, 10% liquidites, 20% immobilier/PE
3. Actions BPF (Bon Pere de Famille — ne jamais vendre sauf these brisee) :
   Hermes (RMS), Air Liquide (AI), Legrand (LR), Thales (HO), Schneider (SU),
   TotalEnergies (TTE), EssilorLuxottica (EL), GTT, LVMH (MC), L Oreal (OR),
   Dassault Systemes (DSY), Safran (SAF), ASML, Edenred (EDEN)
4. Horizon 15 ans, PEA, investit 1000 euros par mois

IMPORTANT : Les convictions de Val PEUVENT ETRE FAUSSES. Tu dois aussi presenter
la realite objective du marche, meme si elle contredit ses convictions.
"""

def fetch_newsletters(days_back=7):
    if not GMAIL_USER or not GMAIL_PASSWORD:
        print("⚠️ Credentials Gmail manquants")
        return []
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_USER, GMAIL_PASSWORD)
        mail.select('INBOX')
        since = (datetime.now() - timedelta(days=days_back)).strftime('%d-%b-%Y')
        newsletters = []
        for source in SOURCES:
            try:
                _, msgs = mail.search(None, f'(FROM "{source}" SINCE {since})')
                if not msgs[0]: continue
                for msg_id in msgs[0].split()[-2:]:
                    _, msg_data = mail.fetch(msg_id, '(RFC822)')
                    msg = email.message_from_bytes(msg_data[0][1])
                    subj_raw = msg['Subject'] or ''
                    subj = decode_header(subj_raw)[0][0]
                    if isinstance(subj, bytes): subj = subj.decode('utf-8', errors='ignore')
                    body = ''
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == 'text/plain':
                                try: body = part.get_payload(decode=True).decode('utf-8', errors='ignore'); break
                                except: pass
                            elif part.get_content_type() == 'text/html' and not body:
                                try:
                                    html = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                                    body = re.sub(r'<[^>]+>', ' ', html)
                                    body = re.sub(r'\s+', ' ', body)[:3000]
                                except: pass
                    else:
                        try: body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                        except: body = ''
                    if body:
                        newsletters.append({'source': source, 'subject': subj, 'body': body[:2000]})
                        print(f"  ✅ {source}: {subj[:50]}")
            except Exception as e:
                print(f"  ⚠️ {source}: {e}")
        mail.logout()
        print(f"\n📧 {len(newsletters)} newsletters")
        return newsletters
    except Exception as e:
        print(f"❌ Gmail: {e}")
        return []

def analyze_with_claude(newsletters):
    if not ANTHROPIC_KEY:
        return None
    if not newsletters:
        return "Aucune newsletter recue."

    content = ""
    for nl in newsletters[:8]:
        content += f"\n\n=== {nl['source']} — {nl['subject']} ===\n{nl['body'][:1500]}"

    prompt = f"""{CONVICTIONS}

Newsletters de la semaine :
{content}

Produis un MACRO DIGEST structure en 5 sections EXACTEMENT dans ce format.
Chaque section = 3 a 5 points precis et actionables. Pas de bavardage.

---DEBUT---

REGIME MACRO ACTUEL
[2-3 phrases sur l environnement : taux, croissance, geopolitique, inflation reelle]

CE QUI CONFIRME TES CONVICTIONS
• [point 1 avec donnee chiffree si possible]
• [point 2]
• [point 3]

CE QUI REMET EN QUESTION TES CONVICTIONS
• [point 1 — sois honnete, meme si inconfortable]
• [point 2 ou "Rien de majeur cette semaine"]

IMPLICATIONS POUR TON PORTEFEUILLE
• ETF MSCI World (30%) : [action concrete]
• Actions BPF (Hermes, Air Liquide, Total...) : [signal]
• Or/Bitcoin (10%) : [signal]
• Liquidites (10%) : [deployer ou garder ?]

POINTS A VERIFIER SUR TES BPF CETTE SEMAINE
• [ticker] — [evenement ou resultat a surveiller]
• [ticker] — [catalyseur positif ou risque identifie]
• [ticker] — [ou "Aucun evenement majeur cette semaine"]

LA QUESTION A SE POSER CE DIMANCHE
[Une seule question strategique, concrete, pour guider ta decision mensuelle]

---FIN---

Sois factuel, objectif, meme quand ca contredit les convictions de Val.
Maximum 400 mots total. Format optimise lecture mobile."""

    try:
        data = json.dumps({
            "model": "claude-opus-4-20250514",
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
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode('utf-8'))
            text = result['content'][0]['text']
            print(f"✅ Claude ({len(text)} chars)")
            return text
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        print(f"❌ Claude HTTP {e.code}: {body[:200]}")
        return None
    except Exception as e:
        print(f"⚠️ Claude erreur: {e}")
        return None

def parse_sections(text):
    """Parse le texte Claude en sections structurées"""
    if not text: return {}
    sections = {}
    current = None
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line or line in ('---DEBUT---', '---FIN---'): continue
        # Détecter les titres de section
        titles = {
            'REGIME MACRO ACTUEL': 'macro',
            'CE QUI CONFIRME': 'confirme',
            'CE QUI REMET EN QUESTION': 'remet',
            'IMPLICATIONS POUR TON PORTEFEUILLE': 'implications',
            'POINTS A VERIFIER': 'verifier',
            'LA QUESTION': 'question',
        }
        matched = False
        for keyword, key in titles.items():
            if keyword in line.upper():
                current = key
                sections[current] = []
                matched = True
                break
        if not matched and current:
            if line.startswith('•') or line.startswith('-'):
                sections[current].append(line.lstrip('•- ').strip())
            elif sections[current] is not None and line:
                if isinstance(sections[current], list) and sections[current] == []:
                    sections[current] = line  # Premier texte = paragraphe intro
                elif isinstance(sections[current], str):
                    sections[current] += ' ' + line
                else:
                    sections[current].append(line)
    return sections

def build_email(digest_text, newsletters):
    now = datetime.now().strftime('%d/%m/%Y')
    week = datetime.now().isocalendar()[1]
    sections = parse_sections(digest_text) if digest_text else {}

    def color_box(title, emoji, items, border, bg, title_color='#333'):
        html = f'<div style="border-left:4px solid {border};background:{bg};border-radius:0 8px 8px 0;padding:14px 16px;margin:12px 0">'
        html += f'<div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:{border};margin-bottom:8px">{emoji} {title}</div>'
        if isinstance(items, str):
            html += f'<div style="font-size:13px;line-height:1.7;color:#444">{items}</div>'
        elif isinstance(items, list):
            for item in items:
                html += f'<div style="font-size:13px;line-height:1.8;color:#444;padding:2px 0">• {item}</div>'
        html += '</div>'
        return html

    h = '<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>'
    h += '<body style="font-family:Arial,sans-serif;background:#f0ede6;padding:12px;margin:0;max-width:560px">'
    h += '<div style="max-width:560px;margin:0 auto;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.08)">'

    # Header
    h += '<div style="background:#0f2540;padding:20px;text-align:center">'
    h += '<div style="font-size:22px;font-weight:700;color:#f0d080;letter-spacing:2px">VAL.PEA</div>'
    h += f'<div style="font-size:10px;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:1px;margin-top:4px">MACRO DIGEST · Semaine {week} · {now}</div>'
    h += '</div>'

    if not digest_text or not sections:
        # Fallback sans Claude
        h += '<div style="padding:20px">'
        h += '<p style="font-size:13px;color:#666">Newsletters recues cette semaine :</p>'
        for nl in newsletters:
            h += f'<div style="padding:6px 0;border-bottom:1px solid #f0f0f0;font-size:12px">• <b>{nl["source"]}</b> : {nl["subject"][:70]}</div>'
        h += '<p style="font-size:11px;color:#999;margin-top:12px">(Analyse Claude indisponible)</p>'
        h += '</div>'
    else:
        h += '<div style="padding:16px 18px">'

        # Regime macro — section naturelle (pas de box colorée)
        if sections.get('macro'):
            h += f'<div style="background:#f8f6f2;border-radius:8px;padding:14px;margin-bottom:12px">'
            h += f'<div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:#666;margin-bottom:6px">🌍 Régime Macro Actuel</div>'
            h += f'<div style="font-size:13px;line-height:1.7;color:#333">{sections["macro"] if isinstance(sections["macro"], str) else " ".join(sections["macro"])}</div>'
            h += '</div>'

        if sections.get('confirme'):
            h += color_box('Ce qui confirme tes convictions', '📊', sections['confirme'], '#16a34a', '#f0fdf4')

        if sections.get('remet'):
            h += color_box('Ce qui remet en question', '⚠️', sections['remet'], '#d97706', '#fef3c7')

        if sections.get('implications'):
            h += color_box('Implications pour ton portefeuille', '🎯', sections['implications'], '#1d4ed8', '#dbeafe')

        if sections.get('verifier'):
            h += color_box('Tes BPF à surveiller cette semaine', '🔍', sections['verifier'], '#7c3aed', '#f3e8ff')

        if sections.get('question'):
            q = sections['question']
            if isinstance(q, list): q = ' '.join(q)
            h += f'<div style="background:#0f2540;border-radius:8px;padding:14px;margin-top:12px">'
            h += f'<div style="font-size:10px;font-weight:700;color:#f0d080;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px">💡 La question de ce dimanche</div>'
            h += f'<div style="font-size:14px;line-height:1.6;color:#fff;font-style:italic">{q}</div>'
            h += '</div>'

        h += '</div>'

    # Sources
    if newsletters:
        seen = set()
        sources_list = ''
        for nl in newsletters:
            if nl['source'] not in seen:
                sources_list += f'<span style="font-size:10px;color:#999">{nl["source"]}</span> &nbsp;'
                seen.add(nl['source'])
        h += f'<div style="padding:10px 18px;border-top:1px solid #f0f0f0;font-size:10px;color:#bbb">Sources : {sources_list}</div>'

    # Footer
    h += '<div style="background:#0f2540;padding:10px 18px;text-align:center;font-size:10px;color:rgba(255,255,255,.4)">'
    h += 'VAL.PEA · Digest automatique · Données éducatives uniquement</div>'
    h += '</div></body></html>'
    return h

def send_email(subject, html):
    if not GMAIL_PASSWORD or not EMAIL_TO:
        print("⚠️ Credentials manquants pour envoi")
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
    print("=" * 55)
    print(f"VAL.PEA Macro Digest — {datetime.now().strftime('%d/%m %H:%M')}")
    print("=" * 55)
    print("\n📥 Lecture newsletters...")
    newsletters = fetch_newsletters(days_back=7)
    print("\n🤖 Analyse Claude...")
    digest = analyze_with_claude(newsletters)
    if digest:
        print("\n--- APERCU ---")
        print(digest[:300] + "...")
    week = datetime.now().isocalendar()[1]
    subject = f"VAL.PEA — Macro Digest Semaine {week} — {datetime.now().strftime('%d/%m')}"
    html = build_email(digest, newsletters)
    send_email(subject, html)
    print("\n✅ Terminé")
