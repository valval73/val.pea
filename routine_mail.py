"""
VAL.PEA -- Mail hebdomadaire "routine" (06/10/2026).
Remplace weekly_digest.py (ancien systeme : grades A-D, IA payante).
AUCUN appel a une IA : tout est calcule a partir des fichiers du site
(data.js, fiches.js, contre_expertises.js, portefeuille de l'utilisatrice dans index.html).

Contenu = les questions de la routine du mois :
  1. Vendre ?   (mes lignes hors qualite, sous le seuil de revue)
  2. Acheter ?  (achat possible + decision selon la contre-expertise)
  3. Ne pas renforcer (lignes > 10 %)
  + entrees en zone depuis le mail precedent, contre-expertises a faire.
Limite : le portefeuille utilise est celui ecrit dans index.html
(PTF_VAL_DEFAULT) ; les changements faits seulement dans le navigateur
ne sont pas connus ici.
"""
import json, os, re, smtplib, subprocess
from datetime import datetime, timedelta, date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_USER = (os.environ.get('GMAIL_USER') or os.environ.get('MAIL_USER') or '').strip()
GMAIL_PASS = (os.environ.get('GMAIL_PASSWORD') or os.environ.get('MAIL_PASS') or '').strip()
EMAIL_TO = (os.environ.get('RECIPIENT_EMAIL') or os.environ.get('MAIL_TO') or GMAIL_USER).strip()
SITE = 'https://valval73.github.io/val.pea/'
STATE = 'routine_state.json'

NODE = r"""
const fs=require('fs');
function grab(file, start){
  // extrait le litteral [..] ou {..} qui suit `start`, en sautant les chaines
  const t=fs.readFileSync(file,'utf8'); let i=t.indexOf(start); if(i<0) return null;
  i += start.length-1; const open=t[i], close=open==='['?']':'}'; let depth=0, q=null;
  for(let j=i;j<t.length;j++){
    const c=t[j];
    if(q){ if(c==='\\'){j++;continue;} if(c===q) q=null; continue; }
    if(c==="'"||c==='"'||c==='`'){ q=c; continue; }
    if(c===open) depth++; else if(c===close){ depth--; if(depth===0) return t.slice(i,j+1); }
  }
  return null;
}
const S=eval(grab('data.js','const S=['));
const ETF=eval(grab('data.js','const ETF=['));
let FICHE={}, CE={};
try{ FICHE=eval('('+grab('fiches.js','const FICHE = {')+')'); }catch(e){}
try{ CE=eval('('+grab('contre_expertises.js','const CE = {')+')'); }catch(e){}
const PTF=eval(grab('index.html','var PTF_VAL_DEFAULT = ['));
process.stdout.write(JSON.stringify({S, ETF:ETF.filter(Boolean).map(e=>({ticker:e.ticker,price:e.price})), FICHE, CE, PTF}));
"""


def load():
    out = subprocess.run(['node', '-e', NODE], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def fr(x, d=2):
    if x is None:
        return '—'
    s = f"{x:,.{d}f}".replace(',', ' ').replace('.', ',')
    return s


def group(s):
    if s.get('qok') and s.get('rec') == 'buy':
        return 'buy'
    if s.get('qok') or s.get('near'):
        return 'watch'
    return 'out'


def last_ce(ce, t):
    L = sorted(ce.get(t, []), key=lambda c: c.get('date', ''), reverse=True)
    return L[0] if L else None


def main():
    D = load()
    S = [s for s in D['S'] if s and s.get('ticker') and (s.get('price') or 0) > 0]
    by = {s['ticker']: s for s in S}
    etf = {e['ticker']: e.get('price') for e in D['ETF']}
    # 06/10/2026 : positions jamais dans le code public. Optionnel : variable
    # secrete PTF_JSON (GitHub > Settings > Secrets) pour un mail personnalise.
    try:
        ptf = json.loads(os.environ.get('PTF_JSON') or '[]') or D['PTF']
    except Exception:
        ptf = D['PTF']
    tot = 0.0
    for p in ptf:
        px = by[p['ticker']]['price'] if p['ticker'] in by else (etf.get(p['ticker']) or p['pru'])
        tot += px * p['qty']
    held = {p['ticker']: p for p in ptf}

    prev = {}
    try:
        prev = json.load(open(STATE, encoding='utf-8'))
    except Exception:
        pass
    in_zone = {s['ticker'] for s in S if s.get('qok') and (s.get('eh') or 0) > 0 and s['price'] <= s['eh']}
    new_zone = sorted(in_zone - set(prev.get('in_zone', [])))

    sell, review, big, ce_todo = [], [], [], []
    for t, p in held.items():
        s = by.get(t)
        if not s:
            continue
        w = s['price'] * p['qty'] / tot * 100 if tot else 0
        if not s.get('qok') and not s.get('near'):
            sell.append((s, 'hors qualité : ' + (s.get('qwhy') or '')))
        if (s.get('stop') or 0) > 0 and s['price'] < s['stop'] and (s.get('qok') or s.get('near')):
            review.append((s, f"sous le seuil de revue ({fr(s['stop'])} €) → contre-expertise obligatoire"))
        if w > 10:
            big.append((s, f"pèse {fr(w, 1)} % (plafond 10 %)"))
        c = last_ce(D['CE'], t)
        age = (date.today() - date.fromisoformat(c['date'])).days if c else None
        if age is None or age > 90:
            ce_todo.append((s, 'jamais de contre-expertise' if age is None else f'dernière il y a {age} jours'))

    buys = []
    for s in sorted([s for s in S if group(s) == 'buy'], key=lambda s: s['price'] / s['eh']):
        c = last_ce(D['CE'], s['ticker'])
        age = (date.today() - date.fromisoformat(c['date'])).days if c else None
        if c is None or age > 90:
            dec = 'PAS ENCORE : contre-expertise à faire avant d’acheter'
        elif c.get('concl') == 'cassee':
            dec = 'NON : thèse cassée'
        elif c.get('concl') == 'fragilisee':
            dec = f"OUI À 50 % : demi-position ({'environ ' + fr(tot * 0.025, 0) + ' €, ' if tot else ''}2,5 % du portefeuille), ordre limité {fr(min(s['el'], s['price']))} €"
        else:
            dec = f"OUI : position normale ({'environ ' + fr(tot * 0.05, 0) + ' €, ' if tot else ''}5 % du portefeuille), ordre limité {fr(min(s['eh'], s['price']))} €"
        if s.get('dq'):
            dec = 'PAS ENCORE : donnée à vérifier (' + s['dq'] + ')'
        buys.append((s, f"zone {fr(s['el'])}–{fr(s['eh'])} € · {dec}"))

    watch_close = sorted([s for s in S if group(s) == 'watch' and (s.get('eh') or 0) > 0 and s['price'] > s['eh']],
                         key=lambda s: s['price'] / s['eh'])[:5]
    nexts = [(by[t], FICHE_next) for t in held if t in by and (FICHE_next := (D['FICHE'].get(t) or {}).get('next'))]

    # premier dimanche du mois a venir ?
    today = date.today()
    sunday = today + timedelta(days=(6 - today.weekday()) % 7)
    first_sunday = sunday.day <= 7

    def li(rows, color):
        if not rows:
            return '<p style="margin:4px 0;color:#5a6275;font-size:13px">Rien.</p>'
        return ''.join(
            f'<div style="padding:8px 10px;margin:4px 0;background:#f5f3ee;border-left:3px solid {color};border-radius:4px;font-size:13px">'
            f'<b>{s["ticker"]}</b> {s.get("name","")} · <span style="font-family:monospace">{fr(s["price"])} €</span><br>'
            f'<span style="color:#5a6275">{txt}</span></div>' for s, txt in rows)

    def sec(title, body):
        return f'<h2 style="font-family:Georgia,serif;font-size:18px;margin:22px 0 6px;color:#0e1c33">{title}</h2>{body}'

    n_buy = len(buys)
    head = ('<b>Dimanche, c’est la routine du mois</b> (15 min, puis aucune décision le reste du mois).'
            if first_sunday else 'Point de la semaine : aucune décision obligatoire avant la routine du 1er dimanche.')
    html = f'''<!doctype html><html><body style="margin:0;background:#f4f2ec;font-family:Arial,Helvetica,sans-serif;color:#1a2233">
<div style="max-width:640px;margin:0 auto;padding:18px">
<div style="background:#0e1c33;color:#f4efe3;border-radius:8px;padding:18px 20px">
<div style="font-size:11px;letter-spacing:2px;color:#c9a45c">VAL.PEA · ROUTINE · {today.strftime('%d/%m/%Y')}</div>
<div style="font-family:Georgia,serif;font-size:22px;margin-top:4px">{n_buy} achat{"s" if n_buy != 1 else ""} possible{"s" if n_buy != 1 else ""} {(' · ' + str(len(sell)) + ' ligne(s) hors qualité') if ptf else ''}</div>
</div>
<p style="font-size:14px;line-height:1.5">{head}</p>
{sec('1. Vendre ?', li(sell, '#a8322b') + li(review, '#a8322b') + '<p style="font-size:12px;color:#5a6275">Règle : on vend seulement si la perte de qualité est confirmée à la publication suivante, ou si une contre-expertise conclut « thèse cassée ». Jamais sur le prix seul.</p>')}
{sec('2. Acheter ?', li(buys, '#1d6b45') + ('' if buys else '<p style="font-size:13px">Aucune action en zone : <b>le versement du mois va sur l’ETF Monde</b>.</p>'))}
{sec('3. Ne pas renforcer', li(big, '#a8790f') if ptf else '<p style="font-size:13px;color:#5a6275">Tes positions ne sont pas connues du mail (confidentialité) : regarde l’onglet Alertes du screener pour tes lignes.</p>')}
{sec('Entrées en zone d’achat depuis le dernier mail', li([(by[t], 'nouvelle en zone · ' + ('achat possible' if group(by[t]) == 'buy' else 'à surveiller (chute, moat ou régularité)')) for t in new_zone], '#1d6b45'))}
{sec('Les plus proches de leur zone', li([(s, f"doit baisser de {fr((s['price'] / s['eh'] - 1) * 100, 0)} % (zone ≤ {fr(s['eh'])} €)") for s in watch_close], '#a8790f'))}
{sec('Contre-expertises à faire (mes lignes)', li(ce_todo, '#6b7487'))}
{sec('Prochains rendez-vous de mes lignes', li(nexts, '#6b7487'))}
<p style="margin-top:22px"><a href="{SITE}" style="background:#0e1c33;color:#f0d080;padding:12px 18px;border-radius:999px;text-decoration:none;font-weight:bold">Ouvrir le screener</a></p>
<p style="font-size:11px;color:#94a3b8;margin-top:18px">Calculé sans IA à partir du screener. Tes positions restent privées dans ton navigateur : les rubriques « mes lignes » sont dans l’onglet Alertes du screener. Pas un conseil en investissement : c’est toi qui décides, avec tes règles écrites.</p>
</div></body></html>'''

    subject = f"VAL.PEA · {'Routine de dimanche' if first_sunday else 'Point hebdo'} · {n_buy} achat possible · {len(new_zone)} nouvelle(s) en zone"
    with open('routine_preview.html', 'w', encoding='utf-8') as f:
        f.write(html)
    json.dump({'in_zone': sorted(in_zone), 'date': today.isoformat()}, open(STATE, 'w', encoding='utf-8'))
    print(subject)
    if not GMAIL_USER or not EMAIL_TO or not GMAIL_PASS:
        print('SMTP non configure : apercu dans routine_preview.html')
        return
    msg = MIMEMultipart('alternative')
    msg['Subject'], msg['From'], msg['To'] = subject, GMAIL_USER, EMAIL_TO
    msg.attach(MIMEText(html, 'html', 'utf-8'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
        s.login(GMAIL_USER, GMAIL_PASS)
        s.sendmail(GMAIL_USER, EMAIL_TO.split(','), msg.as_string())
    print('Mail envoye a', EMAIL_TO)


if __name__ == '__main__':
    main()
