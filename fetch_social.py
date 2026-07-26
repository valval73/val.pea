#!/usr/bin/env python3
"""
VAL.PEA — fetch_social.py
Veille réseaux sociaux — envoi samedi 8h Paris
Sources : Nicolas Chéron, JB Gambet, Guillaume Fournier,
          Rique Trading, Matthieu Louvet + Substack Fabrice Seiman
"""
import re, json, os, time, html as hl
from datetime import datetime, timedelta
from urllib.request import urlopen, Request

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY','')
GMAIL_USER        = os.environ.get('GMAIL_USER','')
GMAIL_PASSWORD    = os.environ.get('GMAIL_PASSWORD','')
RECIPIENT_EMAIL   = os.environ.get('RECIPIENT_EMAIL','')
TELEGRAM_TOKEN    = os.environ.get('TELEGRAM_TOKEN','')
TELEGRAM_CHAT_ID  = os.environ.get('TELEGRAM_CHAT_ID','')
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

INFLUENCEURS = [
    {'name':'Nicolas Chéron','handle':'@NicolasCheron',
     'focus':'fin de vidéo = analyses actions avec niveaux prix'},
    {'name':'JB Gambet','handle':'@jbgambet',
     'focus':'1 analyse fondamentale par jour, valorisation long terme'},
    {'name':'Guillaume Fournier','handle':'@GuillaumeFournier_Invest',
     'focus':'quality investing, moat, Buffett'},
    {'name':'Rique Trading','handle':'@riquetrading',
     'focus':'technique, momentum, niveaux entrée/sortie'},
    {'name':'Matthieu Louvet','handle':'@linvestisseurfrancais',
     'focus':'quality investing PEA, concentration'},
]
SUBSTACK = [
    {'name':'Le Curieux des marchés (Fabrice Seiman)',
     'rss':'https://lecurieuxdesmarches.substack.com/feed'},
]

def get(url, t=12):
    try:
        r = urlopen(Request(url, headers={'User-Agent':UA}), timeout=t)
        return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f'  HTTP {url[:50]}: {e}'); return ''

def youtube_rss(handle, days=8):
    page = get(f'https://www.youtube.com/{handle}/videos')
    ch = re.search(r'"channelId":"(UC[^"]+)"', page or '')
    rss = f'https://www.youtube.com/feeds/videos.xml?channel_id={ch.group(1)}' if ch else           f'https://www.youtube.com/feeds/videos.xml?user={handle.lstrip("@")}'
    xml = get(rss)
    if not xml: return []
    cut = datetime.utcnow() - timedelta(days=days)
    vids = []
    for e in re.finditer(r'<entry>(.*?)</entry>', xml, re.DOTALL):
        b = e.group(1)
        g = lambda t: (m.group(1).strip() if (m:=re.search(rf'<{t}[^>]*>(?:<![CDATA[)?(.*?)(?:]]>)?</{t}>', b, re.DOTALL)) else '')
        title = hl.unescape(g('title')); pub = g('published')[:10]
        vid_m = re.search(r'<yt:videoId>([^<]+)', b)
        vid = vid_m.group(1) if vid_m else ''
        lnk = re.search(r'<link[^>]+href="([^"]+)"', b)
        url = lnk.group(1) if lnk else f'https://youtube.com/watch?v={vid}'
        desc = re.sub(r'\s+', ' ', g('media:description'))[:300]
        try:
            if datetime.strptime(pub, '%Y-%m-%d') < cut: continue
        except: pass
        if title and vid: vids.append({'title':title,'url':url,'vid':vid,'pub':pub,'desc':desc})
    return vids[:5]

def transcript(vid):
    page = get(f'https://www.youtube.com/watch?v={vid}')
    if not page: return None
    cm = re.search(r'"captionTracks":\[([^\]]+)\]', page)
    if not cm: return None
    tracks = [{'url':m.group(1).replace('\\u0026','&'),'lang':m.group(2)}
              for m in re.finditer(r'"baseUrl":"([^"]+)".*?"languageCode":"([^"]+)"', cm.group(1))]
    sel = next((t for p in ['fr','fr-FR','a.fr','en','a.en'] for t in tracks if t['lang'].startswith(p)), tracks[0] if tracks else None)
    if not sel: return None
    xml = get(sel['url'])
    if not xml: return None
    txt = ' '.join(hl.unescape(t).replace('\n',' ') for t in re.findall(r'<text[^>]*>([^<]*)</text>', xml))
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt if len(txt) > 100 else None

def ia(prompt, max_tok=500):
    if not ANTHROPIC_API_KEY: return None
    import urllib.request as ur
    try:
        pl = json.dumps({'model':'claude-sonnet-4-20250514','max_tokens':max_tok,
                         'messages':[{'role':'user','content':prompt}]}).encode()
        req = ur.Request('https://api.anthropic.com/v1/messages', data=pl,
            headers={'Content-Type':'application/json','x-api-key':ANTHROPIC_API_KEY,'anthropic-version':'2023-06-01'})
        return json.loads(ur.urlopen(req, timeout=20).read())['content'][0]['text'].strip()
    except Exception as e:
        print(f'  IA: {e}'); return None

def extract_stocks(infl, title, tr, focus):
    if not tr: return None
    return ia(f'Tu analyses la transcription de {infl} : "{title}".\n'
              f'Focus : {focus}\n\nTRANSCRIPTION :\n{tr[:5000]}\n\n'
              f'Extrais TOUTES les actions mentionnées.\n'
              f'FORMAT (une par ligne) : [TICKER] NOM | VERDICT | Ce qu\'il dit | Prix si mentionné\n'
              f'VERDICT = POSITIF / NÉGATIF / SURVEILLER / NEUTRE\n'
              f'Si aucune action : AUCUNE ACTION\nZéro commentaire.')

def summarize_article(src, title, content):
    return ia(f'Article de {src} : "{title}"\n\n{content[:3000]}\n\n'
              f'1. Idée principale (1 phrase)\n'
              f'2. Actions : [TICKER] NOM | VERDICT | Ce qu\'il dit\nZéro intro.', max_tok=300)

def parse_ia(txt, infl, title, url):
    if not txt or 'AUCUNE ACTION' in txt: return []
    out = []
    for line in txt.split('\n'):
        pts = [p.strip() for p in line.strip().split('|')]
        if len(pts) < 2: continue
        tm = re.match(r'\[([A-Z0-9]{1,6})\]\s*(.*)', pts[0])
        out.append({'ticker':tm.group(1) if tm else '','name':tm.group(2).strip() if tm else pts[0],
                    'verdict':pts[1] if len(pts)>1 else '','detail':pts[2] if len(pts)>2 else '',
                    'prix':pts[3] if len(pts)>3 else '','influenceur':infl,'source':title,'url':url})
    return out

def substack_articles(rss, days=8):
    xml = get(rss)
    if not xml: return []
    arts = []; cut = datetime.utcnow() - timedelta(days=days)
    for m in re.finditer(r'<item>(.*?)</item>', xml, re.DOTALL):
        b = m.group(1)
        g = lambda t: (mx.group(1).strip() if (mx:=re.search(rf'<{t}[^>]*>(?:<![CDATA[)?(.*?)(?:]]>)?</{t}>', b, re.DOTALL)) else '')
        title = g('title'); link = g('link') or g('guid'); pub = g('pubDate')
        content = re.sub(r'<[^>]+',' ',g('description') or g('content:encoded'))[:3000]
        try:
            from email.utils import parsedate_to_datetime
            if parsedate_to_datetime(pub).replace(tzinfo=None) < cut: continue
        except: pass
        if title: arts.append({'title':title,'link':link,'pub':pub[:16],'content':content})
    return arts[:3]

def load_pea():
    tickers = {}
    if os.path.exists('data.js'):
        with open('data.js','r',encoding='utf-8') as f: c = f.read()
        for m in re.finditer(r"ticker:'([A-Z0-9]+)'.*?name:'([^']+)'", c):
            tickers[m.group(1)] = m.group(2)
    return tickers or {'MC':'LVMH','RMS':'Hermès','OR':'L\'Oréal','AI':'Air Liquide',
        'SAN':'Sanofi','SAF':'Safran','AIR':'Airbus','DSY':'Dassault Systèmes','ASML':'ASML',
        'TTE':'TotalEnergies','CAP':'Capgemini','GTT':'GTT','ABCA':'ABC Arbitrage'}

def crossovers(mentions, pea):
    out = []; seen = set(); pu = {k.upper():v for k,v in pea.items()}
    for m in mentions:
        tk = m.get('ticker','').upper(); key = tk+m.get('influenceur','')
        if key in seen: continue
        if tk in pu: seen.add(key); out.append({**m,'pea_name':pu[tk]})
    return out

def send_telegram(msg):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID: return
    try:
        pl = json.dumps({'chat_id':TELEGRAM_CHAT_ID,'text':msg,'parse_mode':'HTML'}).encode()
        urlopen(Request(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage',
            data=pl,headers={'Content-Type':'application/json'}),timeout=10)
        print('Telegram OK')
    except Exception as e: print(f'Telegram: {e}')

def send_mail(subj, body):
    with open('social_preview.html','w',encoding='utf-8') as f: f.write(body)
    if not GMAIL_USER or not RECIPIENT_EMAIL: return
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    msg = MIMEMultipart('alternative')
    msg['Subject']=subj; msg['From']=GMAIL_USER; msg['To']=RECIPIENT_EMAIL
    msg.attach(MIMEText(body,'html','utf-8'))
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as s:
            s.login(GMAIL_USER,GMAIL_PASSWORD); s.sendmail(GMAIL_USER,RECIPIENT_EMAIL,msg.as_string())
        print(f'Mail → {RECIPIENT_EMAIL}')
    except Exception as e: print(f'SMTP: {e}')

def build_mail(now, results, subs, cross):
    MONTHS = {'January':'janvier','February':'février','March':'mars','April':'avril',
              'May':'mai','June':'juin','July':'juillet','August':'août',
              'September':'septembre','October':'octobre','November':'novembre','December':'décembre'}
    df = now.strftime('%d %B %Y')
    for en,fr in MONTHS.items(): df = df.replace(en,fr)
    VC={'POSITIF':'#16A34A','NÉGATIF':'#DC2626','SURVEILLER':'#D97706','NEUTRE':'#6B7280'}
    VI={'POSITIF':'🟢','NÉGATIF':'🔴','SURVEILLER':'🟡','NEUTRE':'⚪'}
    p = [f'<!DOCTYPE html><html><head><meta charset="utf-8"></head><body style="margin:0;background:#f1f5f9;font-family:Arial,sans-serif;">',
         f'<div style="max-width:680px;margin:0 auto;">',
         f'<div style="background:linear-gradient(135deg,#0F2540,#1A3A5C);padding:28px;text-align:center;">',
         f'<div style="color:#F0D080;font-size:22px;font-weight:bold;">📡 VAL.PEA — Veille Réseaux Sociaux</div>',
         f'<div style="color:#AABBCC;font-size:12px;margin-top:6px;">Semaine du {(now-timedelta(days=6)).strftime("%d/%m")} au {now.strftime("%d/%m/%Y")} · IA + Transcriptions YouTube</div>',
         '</div>']
    # Recoupements screener
    if cross:
        p += ['<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">',
              '<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">🎯 Actions dans votre screener PEA</div>']
        for c in cross:
            vd = c.get('verdict', 'NEUTRE').upper()
            col = VC.get(vd, '#6B7280')
            icon = VI.get(vd, '⚪')
            tk = c.get('ticker', '?')
            nm = c.get('pea_name', c.get('name', '?'))
            infl_name = c.get('influenceur', '?')
            detail_html = ('<div style="font-size:12px;color:#555;margin-top:4px;">' + c.get('detail','') + '</div>') if c.get('detail') else ''
            prix_html = ('<div style="font-size:11px;color:#888;">💶 ' + c.get('prix','') + '</div>') if c.get('prix') else ''
            src_url = c.get('url','#')
            row = ('<div style="background:#F0FDF4;border:1px solid #86EFAC;border-radius:8px;padding:10px 14px;margin:6px 0;">'
                   + '<span style="background:#0F2540;color:#F0D080;padding:2px 8px;border-radius:4px;font-weight:bold;">' + tk + '</span> '
                   + '<strong>' + nm + '</strong> '
                   + '<span style="color:' + col + ';font-size:12px;">' + icon + ' ' + vd + '</span> '
                   + '<span style="font-size:11px;color:#666;">via ' + infl_name + '</span>'
                   + detail_html + prix_html
                   + '<div style="font-size:11px;margin-top:4px;"><a href="' + src_url + '" style="color:#7C3AED;">▶ Voir</a></div></div>')
            p.append(row)
        p.append('</div>')
    # YouTube
    p += ['<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">',
          '<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">📺 Analyses YouTube de la semaine</div>']
    for bloc in results:
        infl=bloc['infl']; vids=bloc['vids']
        p.append(f'<div style="margin-bottom:18px;border-left:4px solid #7C3AED;padding-left:12px;">'
                 f'<div style="font-size:14px;font-weight:bold;color:#0F2540;margin-bottom:8px;">'
                 f'🎤 {infl["name"]}</div>')
        if not vids:
            p.append('<div style="font-size:12px;color:#888;font-style:italic;">Aucune nouvelle vidéo cette semaine.</div>')
        for v in vids:
            p.append(f'<div style="margin-bottom:8px;"><div style="font-size:13px;font-weight:bold;">'
                     f'<a href="{v["url"]}" style="color:#0F2540;text-decoration:none;">▶ {v["title"]}</a> '
                     f'<span style="font-size:10px;background:#eee;padding:1px 5px;border-radius:3px;">{v["pub"]}</span></div>')
            ia_txt = v.get('ia_txt','')
            if ia_txt and 'AUCUNE ACTION' not in ia_txt:
                for line in ia_txt.split('\n'):
                    pts=[x.strip() for x in line.strip().split('|')]
                    if len(pts)<2: continue
                    vd2=pts[1].upper(); col2=VC.get(vd2,'#6B7280'); icon2=VI.get(vd2,'⚪')
                    tm=re.match(r'\[([A-Z0-9]{1,6})\]\s*(.*)',pts[0])
                    tk_h=f'<span style="background:#0F2540;color:#F0D080;padding:1px 5px;border-radius:3px;font-size:11px;">{tm.group(1)}</span> {tm.group(2)}' if tm else pts[0]
                    p.append(f'<div style="font-size:12px;padding:3px 0;border-bottom:1px solid #f5f5f5;">'
                             f'{tk_h} <span style="color:{col2};">{icon2} {vd2}</span>'
                             f'{"<span style=\"color:#555;font-size:11px;\"> — " + pts[2] + "</span>" if len(pts)>2 and pts[2] else ""}'
                             f'{"<span style=\"color:#888;font-size:10px;\">" + pts[3] + "</span>" if len(pts)>3 and pts[3] else ""}'
                             f'</div>')
            elif v.get('desc'):
                p.append(f'<div style="font-size:11px;color:#888;font-style:italic;">{v["desc"][:200]}</div>')
            p.append('</div>')
        p.append('</div>')
    p.append('</div>')
    # Substack
    sub_arts = [b for b in subs if b['arts']]
    if sub_arts:
        p += ['<div style="background:#fff;border-radius:10px;margin:12px 16px;padding:18px 20px;border:1px solid #e2e8f0;">',
              '<div style="color:#0F2540;font-size:16px;font-weight:bold;margin:0 0 12px;border-bottom:2px solid #F0D080;padding-bottom:6px;">📰 Newsletters</div>']
        for b in sub_arts:
            p.append(f'<div style="border-left:4px solid #F0D080;padding-left:12px;margin-bottom:14px;">'
                     f'<div style="font-size:14px;font-weight:bold;margin-bottom:8px;">✍ {b["source"]}</div>')
            for a in b['arts']:
                p.append(f'<div style="margin-bottom:8px;"><div style="font-size:13px;font-weight:bold;">'
                         f'<a href="{a.get("link","#")}" style="color:#0F2540;text-decoration:none;">{a["title"]}</a></div>'
                         f'{"<div style=\"font-size:12px;color:#555;margin-top:4px;white-space:pre-line;\">" + a["ia"] + "</div>" if a.get("ia") else ""}</div>')
            p.append('</div>')
        p.append('</div>')
    p += [f'<div style="text-align:center;padding:16px;color:#888;font-size:11px;">VAL.PEA · Veille sociale samedi · {df}<br>Non-conseil en investissement</div>',
          '</div></body></html>']
    return '\n'.join(p)

def main():
    now = datetime.now()
    print(f'VAL.PEA fetch_social — {now.strftime("%Y-%m-%d %H:%M")}')
    pea = load_pea(); print(f'PEA : {len(pea)} actions')
    all_m=[]; results=[]
    for infl in INFLUENCEURS:
        print(f'\n{infl["name"]}...')
        vids = youtube_rss(infl['handle']); print(f'  {len(vids)} vidéo(s)')
        enriched=[]
        for v in vids:
            print(f'  → {v["title"][:55]}')
            ia_txt=None
            tr = transcript(v['vid'])
            if tr:
                print(f'    Transcription {len(tr)} chars')
                ia_txt = extract_stocks(infl['name'],v['title'],tr,infl['focus'])
                if ia_txt: all_m.extend(parse_ia(ia_txt,infl['name'],v['title'],v['url']))
                time.sleep(1.5)
            enriched.append({**v,'ia_txt':ia_txt})
        results.append({'infl':infl,'vids':enriched}); time.sleep(2)
    for src in SUBSTACK:
        print(f'\n{src["name"]}...')
        arts=substack_articles(src['rss']); enriched=[]
        for a in arts:
            ia_t=summarize_article(src['name'],a['title'],a['content'])
            if ia_t: all_m.extend(parse_ia(ia_t,src['name'],a['title'],a.get('link','')))
            enriched.append({**a,'ia':ia_t}); time.sleep(1.5)
        subs_out.append({'source':src['name'],'arts':enriched})
    cross = crossovers(all_m, pea)
    print(f'\n{len(cross)} recoupements screener')
    if cross:
        msg=f'📡 <b>VAL.PEA Veille sociale</b> — {now.strftime("%d/%m/%Y")}\n\n🎯 <b>{len(cross)} action(s)</b> dans votre screener :\n'
        for c in cross:
            icon={'’POSITIF':'🟢','NÉGATIF':'🔴','SURVEILLER':'🟡'}.get(c.get('verdict','').upper(),'⚪')
            msg+=f'{icon} <b>{c.get("ticker","?")}</b> — {c.get("influenceur","?")} — {c.get("verdict","")}\n'
        send_telegram(msg)
    html=build_mail(now,results,subs_out,cross)
    nb_v=sum(len(b['vids']) for b in results)
    send_mail(f'📡 VAL.PEA Veille sociale — {now.strftime("%d/%m/%Y")} — {nb_v} vidéos · {len(cross)} recoupements', html)
    json.dump({'generated':now.isoformat(),'crossovers':cross,'mentions':len(all_m)},
              open('social_log.json','w',encoding='utf-8'),ensure_ascii=False,indent=2,default=str)
    print('\nDONE')

if __name__ == '__main__':
    main()
