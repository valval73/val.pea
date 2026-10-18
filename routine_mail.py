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


def exit_state(s):
    """Meme regle que la fiche : >= 80 % garder ; 60-80 % sans renfort ;
    < 60 % deux ans de suite = vendre. Pas pour banques, assurances, foncieres."""
    if s.get('grid') in ('banque', 'fonciere'):
        return None
    if re.search(r'banque|assur|bancaire|financ|fonci|immobil|reit|centres commerciaux|entrep[oô]ts logistiques', s.get('sector') or '', re.I):
        return None
    f = str(s.get('fcfh') or '').split('|'); n = str(s.get('nih') or '').split('|'); y = str(s.get('yrs') or '').split('|')
    L = []
    for i in range(min(len(f), len(n))):
        try:
            fi, ni = float(f[i]), float(n[i])
        except ValueError:
            continue
        if ni > 0:
            L.append((y[i] if i < len(y) else '', round(fi / ni * 100)))
    if not L:
        return None
    a = L[0][1]; b = L[1][1] if len(L) > 1 else None
    if a < 60 and b is not None and b < 60:
        return ('vendre', f"cash sous 60 % deux ans ({L[0][0]} : {a} %, {L[1][0]} : {b} %) -> VENDRE")
    if a < 60:
        return ('alerte', f"cash {a} % en {L[0][0]} (< 60 %) -> contre-expertise ; vente si l'annee suivante reste sous 60 %")
    if a < 80:
        return ('garder', f"cash {a} % en {L[0][0]} (60-80 %) -> garder sans renforcer, contre-expertise")
    return ('ok', '')


def main():
    D = load()
    S = [s for s in D['S'] if s and s.get('ticker') and (s.get('price') or 0) > 0]
    try:  # controle par les comptes officiels (official_accounts.py)
        oc = json.load(open('official_check.json', encoding='utf-8')).get('res', {})
        for s in S:
            s['x2'] = ' · '.join((oc.get(s['ticker']) or {}).get('issues', []))
    except Exception:
        pass
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
    # 10/10/2026 : GitHub lance parfois les taches programmees avec plusieurs
    # heures de retard ; si le mail a deja ete envoye aujourd'hui (lancement
    # manuel), on n'en renvoie pas un second.
    if prev.get('date') == date.today().isoformat() and not os.environ.get('FORCE_MAIL'):
        print('Mail deja envoye aujourd hui : rien a faire')
        return
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
        # 13/10/2026 : seuil de sortie sur la conversion du benefice en cash
        st_ = exit_state(s)
        if st_ and st_[0] == 'vendre':
            sell.append((s, 'seuil de sortie : ' + st_[1]))
        elif st_ and st_[0] in ('alerte', 'garder'):
            review.append((s, 'seuil de sortie : ' + st_[1]))
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
        else:
            z2 = round(s['dcfm'] * (1 - {'faible': 0.20, 'elevee': 0.40}.get(s.get('unc'), 0.30)), 2) if s.get('dcfm') else None
            P = 2 if (z2 and s['price'] <= z2) else 1
            lvl = P - 1 if c.get('concl') == 'fragilisee' else P
            if lvl >= 2:
                dec = f"OUI, POSITION COMPLÈTE (palier 2, 5 % du portefeuille), ordre limité {fr(min(z2, s['price']))} €"
            elif lvl == 1:
                dec = f"OUI À 50 % (palier 1, 2,5 %), ordre limité {fr(min(s['eh'], s['price']))} € ; le reste sous {fr(z2)} €"
            else:
                dec = f"PAS ENCORE : thèse fragilisée au palier 1, on attend {fr(z2)} € (palier 2)"
        dq_ = ' · '.join(x for x in (s.get('dq'), s.get('x2')) if x)
        if dq_:
            dec = 'PAS ENCORE : donnée à vérifier (' + dq_ + ')'
        buys.append((s, f"zone {fr(s['el'])}–{fr(s['eh'])} € · {dec}"))

    # 11/10/2026 : mouvements forts de la semaine (>= 10 % en 5 seances)
    moves = []
    for s_ in sorted([x for x in S if x.get('chg5') is not None and abs(x['chg5']) >= 10 and (x.get('qok') or x.get('near'))],
                     key=lambda x: x['chg5']):
        first = (s_.get('news5') or '').split(' ;; ')[0].split('|')
        txt_ = f"{'+' if s_['chg5'] > 0 else ''}{fr(s_['chg5'], 1)} % en 5 séances"
        if first and first[0]:
            link = first[1] if len(first) > 1 and first[1].startswith('http') else ''
            txt_ += ' · ' + (f'<a href="{link}">{first[0]}</a>' if link else first[0])
        moves.append((s_, txt_))

    # 12/10/2026 : alerte "a moins de 5 % du palier 1" -> preparer la these et
    # poser l'ordre limite AVANT que le cours arrive (au palier, il y a
    # toujours une mauvaise nouvelle, et c'est la qu'on renonce).
    near5 = []
    for s in sorted([s for s in S if (s.get('qok') or s.get('near')) and (s.get('eh') or 0) > 0
                     and s['eh'] < s['price'] <= s['eh'] * 1.05], key=lambda s: s['price'] / s['eh']):
        c = last_ce(D['CE'], s['ticker'])
        age = (date.today() - date.fromisoformat(c['date'])).days if c else None
        ce_txt = ('contre-expertise à faire cette semaine' if (c is None or age > 90)
                  else f"contre-expertise du {c['date']} : {c.get('concl', '?')}")
        near5.append((s, f"à {fr((s['price'] / s['eh'] - 1) * 100, 1)} % du palier 1 · "
                         f"ordre limité à poser : {fr(s['eh'])} € · {ce_txt}"
                         + ('' if s.get('qok') else ' · hors filtre de peu (à surveiller)')))
    n5 = {s['ticker'] for s, _ in near5}
    watch_close = sorted([s for s in S if group(s) == 'watch' and (s.get('eh') or 0) > 0 and s['price'] > s['eh']
                          and s['ticker'] not in n5],
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

    # 18/10/2026 : univers elargi -- valeurs hors screener qui entrent ou sortent de la grille
    def cand_li(rows, color, sortie=False):
        if not rows:
            return '<p style="margin:4px 0;color:#5a6275;font-size:13px">Rien cette semaine.</p>'
        out_ = ''
        for r in rows[:25]:
            pea = 'CTO (hors PEA)' if r.get('liste', '').startswith('cto') else 'PEA'
            det = (f"échoue : {r.get('echec')}" if sortie else
                   f"ROIC {fr(r.get('roic'), 1)} % · cash {fr(r.get('cash'), 0)} % · croissance {fr(r.get('croissance'), 1)} %/an"
                   + (f" · cours {fr(r.get('cours'))} · palier 1 {fr(r.get('palier1'))} · palier 2 {fr(r.get('palier2'))}" if r.get('palier1') else '')
                   + (f"<br>Bourse Direct : {r.get('courtage')}" if r.get('courtage') else ''))
            out_ += (f'<div style="padding:8px 10px;margin:4px 0;background:#f5f3ee;border-left:3px solid {color};border-radius:4px;font-size:13px">'
                     f'<b>{r.get("nom") or r.get("code")}</b> <span style="color:#5a6275">({r.get("code")} · {pea})</span><br>'
                     f'<span style="color:#5a6275">{det}</span></div>')
        if len(rows) > 25:
            out_ += f'<p style="font-size:12px;color:#5a6275">… et {len(rows) - 25} autre(s) : voir candidats_resultats.json.</p>'
        return out_
    # 18/10/2026 : paliers des candidats pas encore fiables (BTP de haut de cycle,
    # donnees Yahoo des petites valeurs) -> section masquee jusqu'a verification
    AFFICHER_ZONE_CANDIDATS = False
    c_in, c_out, c_zone, dates_ = [], [], [], []
    for f_ in ('candidats_resultats.json', 'candidats_cto_resultats.json'):
        try:
            CR = json.load(open(f_, encoding='utf-8'))
        except Exception:
            continue
        c_in += CR.get('entrees', []); c_out += CR.get('sorties', []); c_zone += CR.get('en_zone', [])
        dates_.append(CR.get('genere', ''))
    c_date = ' / '.join(d for d in dates_ if d)

    # 12/10/2026 : preuve de la methode sur de vraies donnees futures (track_signals.py)
    try:
        B = json.load(open('signals_history.json', encoding='utf-8')).get('bilan', {})
        suivi = (f"{B.get('photos', 0)} photo(s) mensuelle(s) des signaux, {B.get('evaluees', 0)} évaluée(s) à 12 mois."
                 + (f" Les achats en zone ont battu l'ETF Monde {B['achat_bat_etf']} fois sur {B['evaluees']} ;"
                    f" le filtre qualité {B['filtre_bat_etf']} fois sur {B['evaluees']}." if B.get('evaluees') else
                    " Premier verdict 12 mois après la première photo."))
    except Exception:
        suivi = 'Pas encore de photo des signaux.'
    # 12/10/2026 : croissances officielles saisies a la main (official_growth.py)
    # -> elles vieillissent sans prevenir. Plus de 6 mois = au moins une
    # publication est passee depuis : la valeur de l'action est calculee sur
    # un chiffre perime. On ne signale que les valeurs du filtre ou limites.
    stale = []
    try:
        from official_growth import OFFICIAL_GROWTH
        for t_, (g_, det_, d_) in sorted(OFFICIAL_GROWTH.items(), key=lambda kv: kv[1][2]):
            age_ = (date.today() - date.fromisoformat(d_)).days
            s_ = by.get(t_)
            if age_ > 182 and s_ and (s_.get('qok') or s_.get('near')):
                stale.append((s_, f"croissance retenue {fr(g_, 1)} %/an, saisie le {d_} ({age_} jours) : à mettre à jour avec les derniers résultats"))
    except Exception as e_:
        print('croissances officielles : controle impossible', e_)
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
{sec('2. Acheter ?', li(buys, '#1d6b45') + ('' if buys else '<p style="font-size:13px">Aucune action en zone : <b>le versement du mois va sur l’ETF Monde</b>. L’ETF est ta poche d’attente : le jour où une action touche son palier, tu vends la part d’ETF correspondante dans le PEA (sans impôt) pour l’acheter.</p>'))}
{sec('3. Ne pas renforcer', li(big, '#a8790f') if ptf else '<p style="font-size:13px;color:#5a6275">Tes positions ne sont pas connues du mail (confidentialité) : regarde l’onglet Alertes du screener pour tes lignes.</p>')}
{sec('Mouvements de plus de 10 % cette semaine', li(moves, '#24508a') + '<p style="font-size:12px;color:#5a6275">La thèse est-elle touchée, ou seulement le prix ? On ne décide jamais sur un mouvement de prix seul.</p>')}
{sec('À moins de 5 % du palier 1 : prépare-toi', li(near5, '#c9a45c') + '<p style="font-size:12px;color:#5a6275">La thèse se vérifie maintenant, à froid. L’ordre limité se pose à l’avance : la baisse peut ne durer que quelques heures.</p>')}
{sec('Entrées en zone d’achat depuis le dernier mail', li([(by[t], 'nouvelle en zone · ' + ('achat possible' if group(by[t]) == 'buy' else 'à surveiller (chute, moat ou régularité)')) for t in new_zone], '#1d6b45'))}
{sec('Alerte : le capital ajouté rapporte peu', li([(s, f"capitaux investis en hausse, rendement du capital ajouté {('négatif' if s.get('roiic') is None else fr(s.get('roiic'), 1) + ' %')} sur 4 ans · ROIC {fr(s.get('roic'), 1)} %") for s in S if s.get('roiica') and (s.get('qok') or s.get('near'))], '#a8322b') + '<p style="font-size:12px;color:#5a6275">Le signal de la lettre MasterBourse (cas Atos) : l’entreprise investit plus mais gagne peu sur ce qu’elle ajoute. Une alerte, pas une vente : contre-expertise, puis vente seulement si la thèse est cassée.</p>')}
{sec('Univers élargi : nouvelles venues dans ta grille', cand_li(c_in, '#1d6b45') + f'<p style="font-size:12px;color:#5a6275">Valeurs hors screener qui passent maintenant tous tes critères (passage du {c_date}). Pas un achat : une fiche à ouvrir et une contre-expertise à faire.</p>')}
{sec('Univers élargi : sorties de la grille', cand_li(c_out, '#a8322b', sortie=True))}
{'' if not AFFICHER_ZONE_CANDIDATS else sec('Univers élargi : candidats sous leur palier 1', cand_li(c_zone, '#c9a45c') + '<p style="font-size:12px;color:#5a6275">Mêmes paliers que le screener, avec la marge la plus prudente (moat non évalué). Avant tout achat : fiche dans le screener, moat, contre-expertise. Vérifie aussi les frais : sur 500 €, un minimum de 41,90 € coûte 8 %.</p>')}
{sec('Les plus proches de leur zone', li([(s, f"doit baisser de {fr((s['price'] / s['eh'] - 1) * 100, 0)} % (zone ≤ {fr(s['eh'])} €)") for s in watch_close], '#a8790f'))}
{sec('Croissances officielles périmées', li(stale, '#a8790f'))}
{sec('Suivi en conditions réelles', '<p style="font-size:13px">' + suivi + '</p>')}
{sec('Contre-expertises à faire (mes lignes)', li(ce_todo, '#6b7487'))}
{sec('Prochains rendez-vous de mes lignes', li(nexts, '#6b7487'))}
<p style="margin-top:22px"><a href="{SITE}" style="background:#0e1c33;color:#f0d080;padding:12px 18px;border-radius:999px;text-decoration:none;font-weight:bold">Ouvrir le screener</a></p>
<p style="font-size:11px;color:#94a3b8;margin-top:18px">Calculé sans IA à partir du screener. Tes positions restent privées dans ton navigateur : les rubriques « mes lignes » sont dans l’onglet Alertes du screener. Pas un conseil en investissement : c’est toi qui décides, avec tes règles écrites.</p>
</div></body></html>'''

    subject = f"VAL.PEA · {'Routine de dimanche' if first_sunday else 'Point hebdo'} · {n_buy} achat possible · {len(new_zone)} nouvelle(s) en zone · {len(near5)} à moins de 5 %"
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
