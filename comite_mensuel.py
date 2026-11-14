#!/usr/bin/env python3
"""
comite_mensuel.py — VAL.PEA (14/11/2026)

Rapport du comité d'investissement mensuel (1er dimanche du mois), lu avant
de décider. Quatre blocs fixes, dans l'ordre du mandat (MANDAT.md, point 7) :
  1. Performance de la poche actions depuis l'instant T (1er nov. 2026) contre l'ETF Monde
  2. Lignes détenues hors grille (qualité, cash, données à vérifier, contre-expertise périmée)
  3. Candidats en zone d'achat et état de leur contre-expertise
  4. Rappels : décisions attendues, ordre du jour, journal

Positions : jamais dans le code public. Lues depuis le secret PTF_JSON
([{"ticker":"XXX","qty":10,"pru":84.38}, ...]). Sans secret, les blocs 1 et 2
sont remplacés par la consigne pour l'ajouter.

Usage : python comite_mensuel.py            -> comite_preview.html (+ mail si SMTP)
        FORCE_COMITE=1 pour forcer hors 1er dimanche.
"""
import json, os, smtplib, sys
from datetime import date, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from routine_mail import load, fr, group, last_ce, exit_state, GMAIL_USER, GMAIL_PASS, EMAIL_TO

T0 = '2026-11-01'            # instant T : debut de la mesure (decide le 1er nov. 2026)
ETF_REF = 'EUNL.DE'          # iShares Core MSCI World (EUR)
CE_MAX_DAYS = 90             # contre-expertise valable 3 mois
MAX_LINE = 10.0              # % de la poche actions (mandat 3)
MAX_STOCKS = 30.0            # % du PEA en actions (mandat 3)
IRR_MIN = 12.0               # mandat 5.2


def first_sunday():
    t = date.today()
    return t.weekday() == 6 and t.day <= 7


def hist_ret(sym, start):
    """Rendement total (dividendes réinvestis) depuis `start`, en %. None si indisponible."""
    try:
        import yfinance as yf
        h = yf.Ticker(sym).history(start=start, auto_adjust=True)['Close'].dropna()
        if len(h) < 2:
            return None
        return round((float(h.iloc[-1]) / float(h.iloc[0]) - 1) * 100, 2)
    except Exception:
        return None


def main():
    if not first_sunday() and not os.environ.get('FORCE_COMITE'):
        print('Pas le 1er dimanche du mois : rien a faire.')
        return
    D = load()
    S = [s for s in D['S'] if s and s.get('ticker') and (s.get('price') or 0) > 0]
    by = {s['ticker']: s for s in S}
    CE = D['CE']
    try:
        from tickers import YF_MAP
    except Exception:
        YF_MAP = {}
    try:
        ptf = json.loads(os.environ.get('PTF_JSON') or '[]')
    except Exception:
        ptf = []
    today = date.today()
    H = []
    out = lambda s: H.append(s)

    out(f"<h1>Comité d'investissement — {today.strftime('%d/%m/%Y')}</h1>")
    out("<p style='color:#6b7487'>Mandat v1.0 · lire les quatre blocs, puis écrire une ligne au journal (même « rien »). Aucune opération hors comité.</p>")

    # ---------- 1. Performance ----------
    out("<h2>1. Performance depuis le 1er novembre 2026</h2>")
    etf_ret = hist_ret(ETF_REF, T0)
    stocks = [p for p in ptf if p['ticker'] in by]
    if not ptf:
        out("<p><b>Positions non fournies.</b> Ajouter le secret <code>PTF_JSON</code> (GitHub › Settings › Secrets › Actions) : "
            "<code>[{\"ticker\":\"XXX\",\"qty\":10,\"pru\":84.38}, …]</code>. Il n'est jamais écrit dans le dépôt.</p>")
    else:
        val_tot = 0.0; rows = []; w_ret = 0.0; w_sum = 0.0
        for p in ptf:
            s = by.get(p['ticker'])
            px = s['price'] if s else next((e['price'] for e in D['ETF'] if e['ticker'] == p['ticker']), p.get('pru'))
            v = (px or 0) * p['qty']; val_tot += v
            p['_v'] = v
        stock_val = sum(p['_v'] for p in stocks)
        for p in sorted(stocks, key=lambda x: -x['_v']):
            s = by[p['ticker']]
            r = hist_ret(YF_MAP.get(p['ticker'], ''), T0) if YF_MAP.get(p['ticker']) else None
            w = p['_v'] / stock_val * 100 if stock_val else 0
            if r is not None:
                w_ret += r * w; w_sum += w
            flag = ' <b style="color:#b3261e">&gt; 10 % → ramener à 5 %</b>' if w > MAX_LINE else ''
            rows.append(f"<tr><td>{s.get('name', p['ticker'])}</td><td>{fr(w,1)} %{flag}</td><td>{fr(r,1) if r is not None else '—'} %</td>"
                        f"<td>{fr(s['price'])}</td><td>{fr(p.get('pru'))}</td></tr>")
        port_ret = round(w_ret / w_sum, 2) if w_sum else None
        part = stock_val / val_tot * 100 if val_tot else 0
        out(f"<p><b>Poche actions : {fr(port_ret,1) if port_ret is not None else '—'} %</b> (pondéré par les poids actuels) · "
            f"<b>ETF Monde : {fr(etf_ret,1) if etf_ret is not None else '—'} %</b> · "
            f"écart : <b>{fr((port_ret or 0) - (etf_ret or 0),1) if port_ret is not None and etf_ret is not None else '—'} pt</b></p>")
        out(f"<p>Part actions du PEA : <b>{fr(part,1)} %</b> (plafond {MAX_STOCKS:.0f} %) → "
            + ("<b>argent neuf → ETF</b>" if part > MAX_STOCKS else "achat d'action possible si un candidat remplit le mandat (bloc 3)") + "</p>")
        out("<table border=1 cellpadding=4 style='border-collapse:collapse'><tr><th>Ligne</th><th>Poids poche actions</th><th>Depuis le 01/11</th><th>Cours</th><th>PRU</th></tr>"
            + ''.join(rows) + "</table>")
        out("<p style='color:#6b7487'>Le bilan qui compte est à 3 ans (novembre 2029). Un mois ne dit rien ; il est affiché pour que l'habitude de mesurer s'installe.</p>")

    # ---------- 2. Lignes hors grille ----------
    out("<h2>2. Lignes détenues : ce qui sort du mandat</h2>")
    if not stocks:
        out("<p>—</p>")
    else:
        items = []
        for p in stocks:
            s = by[p['ticker']]; t = p['ticker']; pb = []
            if not s.get('qok'):
                pb.append(f"<b>hors grille qualité</b> ({s.get('qwhy') or 'critères non remplis'}) → motif de vente n°1 si confirmé sur deux publications annuelles")
            ex = exit_state(s)
            if ex and ex[0] in ('vendre', 'alerte'):
                pb.append(ex[1])
            if s.get('dq') or s.get('x2'):
                pb.append(f"donnée à vérifier : {s.get('dq') or ''} {s.get('x2') or ''}")
            ce = last_ce(CE, t)
            if not ce:
                pb.append("aucune contre-expertise écrite → à faire")
            else:
                age = (today - datetime.strptime(ce['date'], '%Y-%m-%d').date()).days
                if ce.get('concl') == 'cassee':
                    pb.append(f"contre-expertise du {ce['date']} : <b>CASSÉE</b> → vente (motif n°2)")
                elif age > CE_MAX_DAYS:
                    pb.append(f"contre-expertise périmée ({ce['date']}, {age} j) → à refaire")
                elif ce.get('concl') == 'fragilisee':
                    pb.append(f"contre-expertise du {ce['date']} : fragilisée (une seconde après une autre publication = vente)")
            if pb:
                items.append(f"<li><b>{s.get('name', t)}</b> : " + ' · '.join(pb) + "</li>")
        out("<ul>" + ''.join(items) + "</ul>" if items else "<p>Toutes les lignes passent la grille, contre-expertises à jour.</p>")

    # ---------- 3. Candidats ----------
    out("<h2>3. Candidats en zone d'achat (mandat 5)</h2>")
    cands = []
    for s in S:
        if group(s) != 'buy':
            continue
        irr = s.get('irr') or 0
        ce = last_ce(CE, s['ticker'])
        st = []
        if irr < IRR_MIN:
            st.append(f"rendement attendu {fr(irr,1)} % &lt; 12 % → non")
        if s.get('dq') or s.get('x2'):
            st.append("donnée à vérifier → non")
        if not ce:
            st.append("contre-expertise à faire")
        else:
            age = (today - datetime.strptime(ce['date'], '%Y-%m-%d').date()).days
            st.append(f"contre-expertise {ce['date']} : {ce.get('concl')}" + (" (périmée)" if age > CE_MAX_DAYS else ""))
        held = any(p['ticker'] == s['ticker'] for p in stocks)
        pal = 2 if s.get('price') <= (s.get('el') or 0) else 1
        fresh = ce and (today - datetime.strptime(ce['date'], '%Y-%m-%d').date()).days <= CE_MAX_DAYS
        base = irr >= IRR_MIN and not (s.get('dq') or s.get('x2')) and fresh and not held
        # mandat 5.4 : intacte -> palier normal ; fragilisee -> un palier de moins (rien au palier 1, demi au palier 2)
        ok = base and (ce.get('concl') == 'intacte' or (ce.get('concl') == 'fragilisee' and pal == 2))
        taille = ('position complète 5 %' if ce and ce.get('concl') == 'intacte' and pal == 2 else 'demi-position 2,5 %') if ok else ''
        cands.append((0 if ok else 1, -irr,
                      f"<li>{'✅ ' + taille + ' · ' if ok else ''}<b>{s.get('name')}</b> ({s['ticker']}) · palier {pal} · {fr(s['price'])} vs centrale {fr(s.get('dcfm'))} · "
                      f"rendement attendu {fr(irr,1)} % · " + ' · '.join(st) + (" · <i>déjà en portefeuille : pas de renfort</i>" if held else "") + "</li>"))
    cands.sort()
    out("<ul>" + ''.join(c[2] for c in cands) + "</ul>" if cands else "<p>Aucun candidat en zone. Le versement du mois va à l'ETF.</p>")
    out("<p style='color:#6b7487'>✅ = tous les critères du mandat remplis ; l'achat reste une décision du comité, une seule par mois au plus.</p>")

    # ---------- 4. Ordre du jour ----------
    out("<h2>4. Ordre du jour et journal</h2><ol>"
        "<li>Versement du mois fait ?</li>"
        "<li>Bloc 2 : chaque ligne signalée a-t-elle une décision écrite (garder / contre-expertise / vendre) ?</li>"
        "<li>Bloc 3 : un seul achat au plus, uniquement sur ✅ ; sinon ETF.</li>"
        "<li>Décisions du comité précédent exécutées ? (relire la dernière ligne du journal)</li>"
        "<li><b>Écrire une ligne au journal</b>, même « rien ». Un comité sans ligne n'a pas eu lieu.</li></ol>"
        "<p style='color:#6b7487'>Mandat : MANDAT.md. Prochain comité : 1er dimanche du mois suivant. Le mandat ne change qu'au bilan d'octobre 2027.</p>")

    html = "<html><body style='font-family:system-ui;max-width:900px;margin:auto;line-height:1.45'>" + '\n'.join(H) + "</body></html>"
    open('comite_preview.html', 'w', encoding='utf-8').write(html)
    print('Rapport ecrit : comite_preview.html')
    if not GMAIL_USER or not EMAIL_TO or not GMAIL_PASS:
        print('SMTP non configure : apercu seulement')
        return
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"VAL.PEA · Comité du {today.strftime('%d/%m/%Y')}"
    msg['From'], msg['To'] = GMAIL_USER, EMAIL_TO
    msg.attach(MIMEText(html, 'html', 'utf-8'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
        s.login(GMAIL_USER, GMAIL_PASS)
        s.sendmail(GMAIL_USER, EMAIL_TO.split(','), msg.as_string())
    print('Comite envoye a', EMAIL_TO)


if __name__ == '__main__':
    main()
