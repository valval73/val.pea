"""
VAL.PEA -- Corrections d'affichage appliquees a data.js (qui contient aussi
le code des fiches). Ajoutees le 04/10/2026 :
  - 'Dett/EBITDA' affichait en realite dette/fonds propres -> vraie dette nette/EBITDA
  - 'Int. Coverage' affichait le current ratio -> vraie couverture des interets
  - valeurs absentes affichees '—' au lieu de 'null'
  - libelle 'WACC 8 % · 10 ans' faux (aucun DCF de ce type n'etait calcule)
  - bandeau 'Filtre qualite QARP' en tete de fiche
  - fiches ETF DCAM (etiquetee 'CAC 40 ESG' a tort) et PAEEM (ISIN/frais faux)
Idempotent : une correction deja appliquee n'est pas reappliquee.
"""
TP = [
 ("{k:'debt',l:'Dett/EBITDA',v:s.debt,u:'x',d:'Levier financier'}",
  "{k:'nde',l:'Dette nette/EBITDA',v:(s.nde==null?'—':s.nde),u:'x',d:'Levier (filtre ≤ 2,5)'}"),
 ("{k:'ic',l:'Int. Coverage',v:s.ic===999?'∞':s.ic,u:s.ic===999?'':' x',d:'Couverture intérêts'}",
  "{k:'ic',l:'Int. Coverage',v:(s.ic==null?'—':s.ic),u:' x',d:'Couverture intérêts'}"),
 ('<div class="mv">${m.v}${m.u}</div>', '<div class="mv">${m.v==null?\'—\':m.v+m.u}</div>'),
 ('<div class="mv">${m.v}${typeof m.v===', '<div class="mv">${m.v==null?\'—\':m.v}${typeof m.v==='),
 ('WACC 8% · Croissance terminale 2% · 10 ans',
  "${s.vmeth==='qarp'?'Valeur qualité : 10 ans de croissance (≤ 12 %/an) puis 2,5 %, actualisation 8,5 % · pessimiste −15 % / optimiste +20 %':'Valeur simplifiée : PER sectoriel × bénéfice attendu (valeur hors filtre qualité) · pessimiste −15 % / optimiste +20 %'}"),
 ('<div class="verdict">',
  "${s.qok===undefined?'':`<div style=\"margin:8px 0;padding:8px 12px;border-radius:6px;font-size:12px;line-height:1.5;background:${s.qok?'var(--gnb)':'var(--rdb)'}\"><b>Filtre qualité QARP : ${s.qok?'✅ OUI':'❌ NON'}</b> · ROIC hors EA ${s.roicx??'—'} % · ROIC ${s.roic??'—'} % · Cash ${s.fcfc??'—'} % · Dette/EBITDA ${s.nde??'—'} · Croissance CA ${s.cagr??'—'} %/an${s.qwhy?` — <i>${s.qwhy}</i>`:''}${s.neglect?' · 🔎 <b>qualité délaissée</b>':''}${s.alarm?` · ⚠️ ${s.alarm}`:''}</div>`}\n<div class=\"verdict\">", "Filtre qualité QARP"),
 ("{ticker:'DCAM',name:'Amundi CAC 40 ESG',emetteur:'Amundi',type:'Actions France ESG',isin:'LU1681042609',frais:0.25,perf1y:6.8,perf5y:38.5,encours:'0.9Md€',note:'B',\n desc:'CAC 40 filtre avec criteres ESG - retire les entreprises les moins responsables. Combine exposition France et approche durable.',\n avantages:['Exposition France ESG','Eligble PEA','Amundi solide'],\n risques:['Concentration France','Moins performant que CW8 long terme']}",
  "{ticker:'DCAM',name:'Amundi PEA Monde (MSCI World)',emetteur:'Amundi',type:'Actions Monde',isin:'FR001400U5Q4',frais:0.20,perf1y:null,perf5y:null,encours:'1.25Md€',note:'A',\n desc:'MSCI World (~1 300 grandes entreprises des pays developpes, ~70 % Etats-Unis) via swap, eligible PEA. Socle du portefeuille (cible 80 % de la poche ETF).',\n avantages:['Frais 0,20 % (parmi les plus bas)','Eligible PEA','Diversification mondiale'],\n risques:['~25 % sur 10 geants de la tech US','Replication synthetique (swap)']}"),
 ("{ticker:'PAEEM',name:'MSCI Emerging Markets',emetteur:'Amundi',isin:'LU1681045370',type:'Capitalisant',frais:0.20,perf1y:8.4,perf3y:2.1,perf5y:4.8,encours:'2.8Md€',",
  "{ticker:'PAEEM',name:'Amundi PEA Emergent (MSCI EM ESG)',emetteur:'Amundi',isin:'FR0013412020',type:'Capitalisant',frais:0.30,perf1y:null,perf3y:null,perf5y:null,encours:'0.27Md€',"),
 ("function dynZone(s){\n  // Zone achat = autour du DCF bas, jamais au-dessus du cours si le cours est déjà en dessous\n  const dcfLow = s.dcfb || s.price * 0.88;\n  const dcfMid = s.dcfm || s.price * 1.15;\n  const dcfHigh = s.dcfu || s.price * 1.35;\n  \n  // Règle: zone achat doit être <= cours actuel ou très proche (<5% au-dessus)\n  let elCalc = Math.min(dcfLow * 0.95, s.price * 0.96);\n  let ehCalc = Math.min(dcfLow * 1.05, s.price * 1.04);\n  \n  // Si le DCF bas est déjà sous le cours: zone = autour du cours actuel\n  if(dcfLow < s.price * 0.85){\n    elCalc = s.price * 0.92;\n    ehCalc = s.price * 1.02;\n  }\n  \n  const stopCalc = elCalc * 0.87;\n  const o1Calc = dcfMid;\n  const o2Calc = dcfHigh;\n  \n  const stopFinal=Math.min(stopCalc,s.price*0.87);\n  const o1Final=o1Calc>s.price?o1Calc:s.price*1.15;\n  return {\n    el: Math.round(elCalc * 10)/10,\n    eh: Math.round(ehCalc * 10)/10,\n    stop: Math.round(stopFinal * 10)/10,\n    o1: Math.round(o1Final * 10)/10,\n    o2: Math.round(o2Calc * 10)/10,\n    inZone: s.price >= elCalc && s.price <= ehCalc,\n    upside: Math.round((o1Calc/s.price - 1)*100)\n  };\n}\n\n",
  "function dynZone(s){\n  // 04/10/2026 : zones = celles calculees par le script a partir de la valeur\n  // intrinseque (el/eh/stop/o1/o2). Avant, si le cours depassait la valeur,\n  // la \"zone d'achat\" etait recentree AUTOUR DU COURS ACTUEL : toute action\n  // trop chere apparaissait \"en zone d'achat\".\n  const el=s.el||0, eh=s.eh||0;\n  return {\n    el: el, eh: eh,\n    stop: s.stop||0,\n    o1: s.o1||s.dcfm||0,\n    o2: s.o2||s.dcfu||0,\n    inZone: eh>0 && s.price<=eh && s.qok!==false,  // zone d'achat = qualite d'abord\n    upside: s.dcfm ? Math.round((s.dcfm/s.price-1)*100) : 0\n  };\n}\n\n"),
 # mise a niveau d'une version deja appliquee de dynZone (zone reservee au filtre qualite)
 ("    inZone: eh>0 && s.price<=eh,\n", "    inZone: eh>0 && s.price<=eh && s.qok!==false,  // zone d'achat = qualite d'abord\n"),
 # bandeau : alerte chute > 35 % sur 1 an (05/10/2026)
 ("${s.alarm?` · ⚠️ ${s.alarm}`:''}</div>`}",
  "${s.alarm?` · ⚠️ ${s.alarm}`:''}${s.knife&&s.b52h?` · ⛔ <b>cours ${Math.round((1-s.price/s.b52h)*100)} % sous son plus haut 1 an : comprendre la cause avant tout achat</b>`:''}</div>`}"),
 # bandeau : croissance supposee par le cours vs croissance reelle (05/10/2026)
 ("comprendre la cause avant tout achat</b>`:''}</div>`}",
  "comprendre la cause avant tout achat</b>`:''}${s.gimp!=null?`<br>📐 <b>Le cours actuel suppose ~${s.gimp} %/an de croissance</b> (ralentissant vers 2,5 % sur 10 ans) · croissance réelle retenue : ${s.gused??'—'} %/an (${s.gsrc||'—'}) → ${s.gused!=null&&s.gimp<=s.gused?'✅ hypothèse du marché ≤ réel : marge de sécurité':'⚠️ le marché suppose plus que le réel'}`:''}</div>`}", "Le cours actuel suppose"),
 # bandeau : valeur limite a surveiller (05/10/2026)
 ("<b>Filtre qualité QARP : ${s.qok?'✅ OUI':'❌ NON'}</b>",
  "<b>Filtre qualité QARP : ${s.qok?'✅ OUI':(s.near?'⚑ LIMITE — à surveiller (un seul critère manqué)':'❌ NON')}</b>"),
 # bandeau : moat (05/10/2026)
 ("<b>Filtre qualité QARP : ${s.qok?'✅ OUI':(s.near?'⚑ LIMITE — à surveiller (un seul critère manqué)':'❌ NON')}</b>",
  "<b>Filtre qualité QARP : ${s.qok?'✅ OUI':(s.near?'⚑ LIMITE — à surveiller (un seul critère manqué)':'❌ NON')}</b>${s.mscore!=null?` · 🏰 <b>Moat ${s.mscore}/5</b> : ${s.mtype} — <i>menace : ${s.mthreat}</i>${s.mscore<3?' (moat insuffisant : pas d’achat)':''}`:''}", "🏰 <b>Moat"),
 # 05/10/2026 : ROIC > 100 % (capital tangible quasi nul, ex. Wolters Kluwer
 # 3 456 %) affiche '>100' : le chiffre exact n'a pas de sens economique.
 ("ROIC hors EA ${s.roicx??'—'} %", "ROIC hors EA ${s.roicx>100?'>100':(s.roicx??'—')} %"),
 ("· ROIC ${s.roic??'—'} %", "· ROIC ${s.roic>100?'>100':(s.roic??'—')} %"),
 # 05/10/2026 : place de cotation ; bourses nordiques = acces courtier a verifier
 ("(s.near?'⚑ LIMITE — à surveiller (un seul critère manqué)':'❌ NON')}</b>",
  "(s.near?'⚑ LIMITE — à surveiller (un seul critère manqué)':'❌ NON')}</b>${s.place?` · 📍 ${s.place}${['Helsinki','Copenhague','Stockholm','Oslo'].includes(s.place)?' (accès PEA chez ton courtier à vérifier)':''}`:''}"),
]


def apply_template_patches(data_js_path='data.js'):
    with open(data_js_path, encoding='utf-8') as f:
        d = f.read()
    n = 0
    for item in TP:
        old, new = item[0], item[1]
        guard = item[2] if len(item) > 2 else None
        # guard : texte dont la presence prouve que la correction est deja faite
        # (necessaire quand une correction ulterieure modifie le resultat)
        if guard and guard in d:
            continue
        if old in d and new not in d:
            d = d.replace(old, new, 1)
            n += 1
    d, k = ensure_fiche_fields(d)
    n += k
    d, k = ensure_new_stocks(d)
    n += k
    if n:
        with open(data_js_path, 'w', encoding='utf-8') as f:
            f.write(d)
    return n


# Fiches creees sans these/risques/historique (les 34 valeurs SRD ajoutees le
# 24/07/2026) : leur fiche plantait a l'ouverture (s.track undefined) -- constate
# le 05/10/2026 en ouvrant les 157 fiches une par une dans un navigateur.
FICHE_DEFAULTS = [
    ('thesis', "'Fiche incomplete : these d investissement a rediger avant tout achat.'"),
    ('contra', "'Risques non documentes.'"),
    ('track', '[]'),
]

def ensure_fiche_fields(d):
    import re
    starts = [m.start() for m in re.finditer(r"\{ticker:'", d)]
    out, last, k = [], 0, 0
    for i, st in enumerate(starts):
        en = starts[i + 1] if i + 1 < len(starts) else len(d)
        block = d[st:en]
        m = re.search(r"price:[+-]?\d+\.?\d*", block)
        if m:
            add = ''.join(f",{f}:{v}" for f, v in FICHE_DEFAULTS
                          if not re.search(r"(?<![A-Za-z0-9_])" + f + ":", block))
            if add:
                block = block[:m.end()] + add + block[m.end():]
                k += 1
        out.append(d[last:st]); out.append(block); last = en
    out.append(d[last:])
    return ''.join(out), k


# Fiches des nouvelles valeurs (tickers.EU_LEADERS) : creees vides une seule
# fois, puis remplies par fetch_fundamentals au meme run (prix, ratios,
# filtre qualite...). Les champs descriptifs restent a rediger.
_NEW_FIELDS = ("price:0,chg:0,mkt:'—',b52h:0,b52l:0,beta:0,pe:0,pb:0,ev_ebitda:0,ps:0,"
               "pfcf:0,ev_ebit:0,roe:0,roic:0,roa:0,debt:0,de:0,ic:0,cr:0,qr:0,yield:0,"
               "epsg:0,revg:0,margin:0,gm:0,om:0,fcf:0,capex:0,capr:0,capda:0,dcfb:0,"
               "dcfm:0,dcfu:0,pio:0,alt:0,rsi:50,mm50:0,mm200:0,el:0,eh:0,stop:0,o1:0,"
               "o2:0,cb:0,ch:0,cs:0,tp:0,score:'C',rec:'watch',zone:false,moat:[],"
               "cats:[],ins:[],peers:[],risks:{},track:[],"
               "thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',"
               "contra:'Risques non documentes.'")

def ensure_new_stocks(d):
    try:
        from tickers import EU_LEADERS
    except Exception:
        return d, 0
    s0 = d.find('const S=[')
    if s0 < 0:
        return d, 0
    end = d.find('\n];', s0)
    if end < 0:
        return d, 0
    add = []
    for tk, sym, name, sector, cap, cur in EU_LEADERS:
        if "{ticker:'" + tk + "'" in d:
            continue
        name = name.replace("'", " ")
        add.append(f"\n,{{ticker:'{tk}',name:'{name}',sector:'{sector}',cap:'{cap}',"
                   f"srd:false,idx:'Europe ({cur})',{_NEW_FIELDS}}}")
    if not add:
        return d, 0
    return d[:end] + ''.join(add) + d[end:], len(add)
