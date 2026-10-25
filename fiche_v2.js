// VAL.PEA — fiche v2 et page d'accueil "liste de décision" (05/10/2026).
// Chargé après data.js et le code de index.html. Remplace render() : la
// nouvelle fiche s'affiche en haut ; l'ancienne analyse reste disponible,
// repliée, en bas (elle n'est plus mise à jour et peut contredire la fiche).
(function(){
'use strict';
var COC = 8.5; // cout du capital retenu dans le modele de valeur (%)

function fr(n, d){
  if(n===null||n===undefined||n===''||isNaN(n)) return '—';
  return Number(n).toLocaleString('fr-FR',{minimumFractionDigits:d===undefined?0:d,maximumFractionDigits:d===undefined?2:d});
}
function esc(t){ return String(t===undefined||t===null?'':t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function newsHtml(s){
  if(!s.news5) return '';
  return '<ul style="margin:4px 0 0 18px;padding:0">'+String(s.news5).split(' ;; ').map(function(x){ var a=x.split('|'); var t=esc(a[0]||''), u=a[1]||'', pv=esc(a[2]||'');
    return '<li>'+(/^https?:/.test(u)?'<a href="'+esc(u)+'" target="_blank" rel="noopener">'+t+'</a>':t)+(pv?' <span class="v2-small">('+pv+')</span>':'')+'</li>'; }).join('')+'</ul>';
}
function moveBanner(s){
  if(!(s.chg5!=null && Math.abs(s.chg5)>=10)) return '';
  var dn=s.chg5<0;
  return '<section class="v2-card" style="background:'+(dn?'#fbecea':'#eef6f1')+';border-left:4px solid '+(dn?C.rd:C.gn)+'"><b>Mouvement fort : '+sgn(s.chg5,1)+' en 5 séances.</b> '+
    (s.news5?'Actualités du moment (Yahoo) :':'Aucune actualité trouvée automatiquement : regarder Zonebourse ou Boursorama.')+newsHtml(s)+
    '<div class="v2-small" style="margin-top:4px">Question à se poser : la <b>thèse</b> est-elle touchée (voir « ce qui prouverait que j’ai tort ») ou est-ce seulement le prix ? On ne vend ni n’achète sur un mouvement de prix seul.</div></section>';
}
window.v2moveBanner=moveBanner;
function dqAll(s){ return [s.dq, s.x2].filter(function(x){return x;}).join(' · '); }
function pct(a,b){ return (a&&b)? ((a/b-1)*100) : null; }
function sgn(x,d){ if(x===null||isNaN(x)) return '—'; return (x>=0?'+':'')+fr(x,d===undefined?0:d)+' %'; }
var C = {gn:'#1d6b45', gn2:'#3f9a68', or:'#a8790f', rd:'#a8322b', ink:'#0e1c33', mu:'#5a6275', bg:'#f5f3ee', line:'#eee9de'};
var UNC = {faible:'faible', moyenne:'moyenne', elevee:'élevée'};
var UNCM = {faible:'10-20 %', moyenne:'15-25 %', elevee:'20-30 %'};
// 08/10/2026 : deux paliers d'achat. Palier 1 = zone actuelle (demi-position) ;
// palier 2 = decote Morningstar 5 etoiles (20/30/40 % sous la valeur centrale) -> position complete.
var Z2M = {faible:0.20, moyenne:0.30, elevee:0.40};
function z2(s){ return s.dcfm>0 ? Math.round(s.dcfm*(1-(Z2M[s.unc]||0.30))*100)/100 : null; }
// 19/10/2026 : montants dans la devise de cotation (c'est elle que voit le courtier), euros entre parentheses
var CUR_SYM={USD:'$',CHF:'CHF',SEK:'SEK',NOK:'NOK',DKK:'DKK',PLN:'PLN',GBP:'£'};
function M(s,x,d){ if(x==null||!isFinite(x)) return '—'; if(s&&s.fxr>0&&s.qcur&&s.qcur!=='EUR') return fr(x*s.fxr,d)+' '+(CUR_SYM[s.qcur]||s.qcur)+' <span style="opacity:.7;font-size:.8em">('+fr(x,d)+' €)</span>'; return fr(x,d)+' €'; }
function palier(s){ if(!(s.qok&&s.eh>0)) return 0; var p2=z2(s); if(p2 && s.price<=p2) return 2; return s.price<=s.eh?1:0; }
window.v2palier = palier; window.v2z2 = z2;
function isFin(s){ return /banque|assur|bancaire|financ/i.test(s.sector||''); }
function isRealEstate(s){ return /fonci|immobil|reit/i.test(s.sector||''); }

// ---- groupe de décision (page d'accueil et verdict) ----
function group(s){
  if(s.qok && s.rec==='buy') return 'buy';
  if(s.qok || s.near) return 'watch';
  return 'out';
}
function verdict(s){
  var p=s.price, eh=s.eh, el=s.el;
  if(!s.qok && !s.near) return {t:'HORS QUALITÉ', c:'#6b7487', x:'Ne passe pas le filtre qualité ('+(s.qwhy||'critères')+'). La méthode n’achète pas cette action, quel que soit son prix.'};
  if(!s.qok && s.near) return {t:'LIMITE · À SURVEILLER', c:C.or, x:'Un seul critère manque de peu ('+(s.qwhy||'')+'). Pas d’achat tant qu’il n’est pas rempli.'};
  var base = s.gimp!=null && s.gused!=null ? ' Le cours suppose '+fr(s.gimp,1)+' %/an de croissance, contre '+fr(s.gused,1)+' % retenus.' : '';
  if(s.rec==='buy') return palier(s)===2 ? {t:'ACHAT POSSIBLE · PALIER 2', c:C.gn, x:'Qualité OK, cours sous le palier 2 ('+fr(z2(s))+' €) : vraie occasion, position complète possible.'+base} : {t:'ACHAT POSSIBLE · PALIER 1', c:C.gn, x:'Qualité OK, cours sous le palier 1 ('+fr(eh)+' €) : demi-position ; position complète sous '+fr(z2(s))+' € (palier 2).'+base};
  if(eh>0 && p<=eh){
    var why = s.knife ? 'mais chute en cours (cours très sous son plus haut d’un an) : comprendre la cause avant d’acheter.'
      : (s.mscore==null||s.mscore<3) ? 'mais moat jugé insuffisant (< 3/5).'
      : (s.regu!=null && s.regn && s.regu < s.regn-1) ? 'mais croissance irrégulière ('+s.regu+'/'+s.regn+' années de hausse du CA).'
      : '';
    return {t:'EN ZONE · PRUDENCE', c:C.or, x:'Cours dans la zone d’achat '+why+base};
  }
  if(eh>0 && p<=eh*1.05) return {t:'PROCHE · ATTENDRE '+fr(eh,0)+' €', c:C.or, x:'Qualité OK, cours à '+fr(pct(p,eh),1)+' % au-dessus de la zone d’achat.'+base};
  if(s.o1>0 && p>s.o1) return {t:'CHÈRE · NE PAS RENFORCER', c:C.rd, x:'Cours au-dessus du scénario optimiste ('+fr(s.o1)+' €) : on n’achète pas ; si tu la détiens, tu vends la moitié de la ligne (une fois), jamais tout.'+base};
  return {t:'QUALITÉ · TROP CHÈRE POUR L’INSTANT', c:'#6b7487', x:'Qualité OK, mais le cours ('+fr(p)+' €) reste au-dessus de la zone d’achat ('+fr(el)+' – '+fr(eh)+' €).'+base};
}

// ---- position dans le portefeuille de l'utilisatrice ----
function position(s){
  var list = (typeof PTF!=='undefined' && (PTF.length || (window._ptfProfile && window._ptfProfile!=='val'))) ? PTF : null;
  if(!list){ try{ list = JSON.parse(localStorage.getItem('pea_ptf_val')||'[]'); }catch(e){ list=[]; } }
  var pos = list.find(function(x){return x&&x.ticker===s.ticker;});
  if(!pos) return '';
  var tot = 0;
  list.forEach(function(x){
    var st = S.find(function(y){return y&&y.ticker===x.ticker;});
    var et = (typeof ETF!=='undefined') ? ETF.find(function(y){return y&&y.ticker===x.ticker;}) : null;
    var px = st ? st.price : (et && et.price ? et.price : x.pru);
    tot += px * x.qty;
  });
  var w = tot>0 ? s.price*pos.qty/tot*100 : 0;
  var g = pct(s.price,pos.pru);
  return '<div class="v2-pos"><span>Position '+((window._ptfProfile&&window._ptfProfile!=='val')?'('+(window.v2profName?window.v2profName():'')+') ':'')+': <b>'+pos.qty+' actions · PRU '+fr(pos.pru)+' €</b></span>'+
    '<span>'+(g>=0?'Plus-value':'Moins-value')+' : <b style="color:'+(g>=0?C.gn:C.rd)+'">'+sgn(g,1)+'</b> · poids <b style="color:'+(w>10?C.rd:C.ink)+'">'+fr(w,1)+' %</b> (plafond 10 %)</span></div>';
}


// ---- 11/10/2026 : plan d'achat en un ou deux paliers (lisible d'un coup d'oeil) ----
function myPos(s){
  var list = (typeof PTF!=='undefined' && (PTF.length || (window._ptfProfile && window._ptfProfile!=='val'))) ? PTF : null;
  if(!list){ try{ list = JSON.parse(localStorage.getItem('pea_ptf_val')||'[]'); }catch(e){ list=[]; } }
  var pos = list.find(function(x){return x&&x.ticker===s.ticker;}), tot=0;
  list.forEach(function(x){
    var st = S.find(function(y){return y&&y.ticker===x.ticker;});
    var et = (typeof ETF!=='undefined') ? ETF.find(function(y){return y&&y.ticker===x.ticker;}) : null;
    tot += (st ? st.price : (et && et.price ? et.price : x.pru)) * x.qty;
  });
  return {pos:pos, tot:tot};
}
function buyPlan(s){
  if(!(s.qok&&s.eh>0)) return '<section class="v2-card"><h2>Mes paliers d’achat</h2><p class="v2-small">Aucun palier : la valeur ne passe pas le filtre qualité, on ne cherche pas à l’acheter.</p></section>';
  var ACC=/compte-titres/i.test((s.idx||'')+' '+(s.sector||''))?'du compte-titres':'du PEA';
  var p1=s.eh, p2=z2(s), P=myPos(s), tot=P.tot, held=P.pos?P.pos.qty*s.price:0, wNow=tot>0?held/tot*100:0;
  var amt=function(w){ if(!(tot>0)) return ''; var e=Math.max(0,tot*w/100-held); return e>0?' · ≈ <b>'+fr(e,0)+' €</b>, soit '+Math.max(1,Math.round(e/s.price))+' action'+(Math.round(e/s.price)>1?'s':''):' · <b>poids déjà détenu</b>'; };
  var dist=function(x){ var d=pct(x,s.price); return d>=0?'<b style="color:'+C.gn+'">atteint</b> (cours '+M(s,s.price)+')':'le cours doit baisser de <b>'+fr(-d,0)+' %</b>'; };
  var row=function(n,lbl,x,w,txt){ return '<div class="v2-scen" style="background:'+(s.price<=x?'#eef6f1':C.bg)+'"><div class="v2-k" style="color:'+C.gn+'">'+n+'</div><div class="v2-big">sous '+M(s,x,0)+'</div><div class="v2-small">'+lbl+amt(w)+'<br>'+dist(x)+'<br>'+txt+'</div></div>'; };
  // 11/10/2026 : une phrase d'etat en tete, pour ne pas avoir a deduire la situation des cartes
  var st, stc, deco = s.dcfm>0 ? (1 - s.price/s.dcfm)*100 : 0;
  if(dqAll(s)){ st='<b>Achat bloqué pour l’instant</b> : une donnée est à vérifier ('+esc(dqAll(s))+'). Tant qu’elle n’est pas vérifiée, les paliers ne comptent pas.'; stc='#fbf4e6'; }
  else if(p2 && s.price<=p2){ st='<b>Le cours ('+M(s,s.price)+') est déjà sous les deux paliers</b> : position complète possible, <b>après</b> une contre-expertise « intacte ».'; stc='#eef6f1'; }
  else if(s.price<=p1){ st='<b>Le cours ('+M(s,s.price)+') est sous le palier 1</b> : demi-position possible après contre-expertise ; le reste si le cours passe sous '+M(s,p2,0)+'.'; stc='#eef6f1'; }
  else { st='<b>Aucun palier atteint</b> : il faudrait une baisse de '+fr(-pct(p1,s.price),0)+' % pour le palier 1. On attend.'; stc=C.bg; }
  var warn = deco>=40 ? '<div class="v2-note" style="background:#fbecea"><span><b>Décote de '+fr(deco,0)+' % : trop beau pour être vrai tant qu’on ne sait pas pourquoi le marché refuse ce prix.</b> '+(s.grid==='fonciere'?'Pour une foncière, la valeur centrale est l’actif net comptable (la valeur des immeubles inscrite au bilan). Depuis la hausse des taux, les foncières européennes se paient souvent 30 à 50 % sous cet actif net : le marché pense que les immeubles valent moins que ce qui est écrit. La décote n’est donc pas une aubaine automatique.':'Soit le marché se trompe, soit nos chiffres (bénéfice, croissance) sont faux ou dépassés : la contre-expertise doit trancher.')+'</span></div>' : '';
  return '<section class="v2-card" style="border-left:4px solid '+C.gn+'"><div class="v2-head"><h2>Mes paliers d’achat</h2><span class="v2-small">'+(P.pos?'déjà '+fr(wNow,1)+' % '+ACC:'pas encore en portefeuille')+'</span></div>'+
    '<div class="v2-note" style="background:'+stc+'"><span>'+st+'</span></div>'+warn+(sizes(s).cyc?'<div class="v2-note" style="background:#eef1f6"><span><b>Cyclique : paliers indicatifs, peu fiables.</b> Le modèle ne sait pas valoriser une cyclique en pleine accélération ou au creux. '+(s.gimp!=null?'La bonne question : <b>le cours suppose environ '+fr(s.gimp,0)+' % de croissance par an'+(s.gimp>=30?' ou plus':'')+'</b>. Y crois-tu sur dix ans ?':'Raisonne sur le cash moyen d’un cycle complet, pas sur l’année en cours.')+' Taille réduite de moitié (1,25 % puis 2,5 %).</span></div>':'')+
    '<div class="v2-grid3">'+
      row('PALIER 1 · DEMI-POSITION',fr(sizes(s).half,sizes(s).half===1.25?2:1)+' % '+ACC,p1,sizes(s).half,'Première moitié.'+(sizes(s).cyc?' Cyclique : tailles divisées par deux.':''))+
      (p2?row('PALIER 2 · POSITION COMPLÈTE','compléter jusqu’à '+fr(sizes(s).full,1)+' %',p2,sizes(s).full,'Seconde moitié.'):'')+
      '<div class="v2-scen" style="background:#fbf4e6"><div class="v2-k" style="color:'+C.or+'">PAS UN PRIX D’ACHAT</div><div class="v2-big">'+(s.vopt>0?'&gt; '+M(s,s.vopt,0):'—')+'</div><div class="v2-small">Au-dessus du scénario optimiste : <b>vendre la moitié</b> de la ligne, une seule fois, jamais tout. Le « central » ('+M(s,s.dcfm,0)+') est une estimation de valeur, pas un prix d’achat.</div></div>'+
    '</div>'+
    '<p class="v2-small"><b>En deux fois</b> : demi-position au palier 1, le reste au palier 2. <b>En une fois</b> : si le cours tombe directement sous le palier 2, position complète d’un coup. Si le palier 2 n’arrive jamais, tu restes à demi-position : c’est voulu. '+
    '<b>Condition</b> : contre-expertise de moins de 3 mois « intacte » ; « fragilisée » → un palier plus bas ; « cassée » → rien. '+
    '<b>À faire</b> : poser deux alertes de cours chez ton courtier, à '+M(s,p1,0)+(p2?' et '+M(s,p2,0):'')+(s.qcur&&s.qcur!=='EUR'?' (dans la devise de cotation : c’est elle que voit ton courtier)':'')+'. Les paliers sont recalculés après chaque publication de résultats.</p></section>';
}

// ---- barre de prix ----
function priceBar(s){
  var pts = [s.price, s.el, s.eh, z2(s), s.stop, s.dcfm, s.vopt, s.vpess, s.tp].filter(function(x){return x>0;});
  var lo = Math.min.apply(null,pts)*0.95, hi = Math.max.apply(null,pts)*1.03, span = hi-lo;
  var pos = function(x){ return Math.max(0,Math.min(100,(x-lo)/span*100)); };
  var h = '<div class="v2-bar"><div class="v2-track"></div>';
  // 19/10/2026 : la zone va du palier 2 au palier 1 (l'ancienne borne 'el' embrouillait)
  var zl=z2(s)>0?z2(s):s.el;
  if(zl>0&&s.eh>0) h += '<div class="v2-zone" style="left:'+pos(zl)+'%;width:'+(pos(s.eh)-pos(zl))+'%"></div>'+
    '<div class="v2-lbl" style="left:'+pos(zl)+'%;top:62px;color:'+C.gn+'">Achat '+fr(zl,0)+' – '+fr(s.eh,0)+' €</div>';
  var Z=z2(s), near_=(Z>0&&s.stop>0&&Math.abs(pos(Z)-pos(s.stop))<9);
  if(Z>0) h += '<div class="v2-tick" style="left:'+pos(Z)+'%;background:'+C.gn+';width:4px"></div>';
  if(s.stop>0) h += '<div class="v2-tick" style="left:'+pos(s.stop)+'%;background:'+C.rd+'"></div><div class="v2-lbl" style="left:'+pos(s.stop)+'%;top:80px;color:'+C.rd+'">'+(near_?'<span style="color:'+C.gn+'">palier 2 '+fr(Z,0)+'</span> · ':'')+'relire la thèse '+fr(s.stop,0)+'</div>';
  if(Z>0 && !near_) h += '<div class="v2-lbl" style="left:'+pos(Z)+'%;top:80px;color:'+C.gn+'">palier 2 '+fr(Z,0)+'</div>';
  if(s.tp>0) h += '<div class="v2-tick" style="left:'+pos(s.tp)+'%;background:#6b7487;width:2px"></div><div class="v2-lbl" style="left:'+pos(s.tp)+'%;top:80px;color:'+C.mu+'">analystes '+fr(s.tp,0)+'</div>';
  if(s.dcfm>0) h += '<div class="v2-tick" style="left:'+pos(s.dcfm)+'%;background:'+C.ink+';height:38px;top:26px"></div><div class="v2-lbl" style="left:'+pos(s.dcfm)+'%;top:62px;color:'+C.ink+'">central '+fr(s.dcfm,0)+'</div>';
  if(s.vopt>0) h += '<div class="v2-tick" style="left:'+pos(s.vopt)+'%;background:#b8862b"></div><div class="v2-lbl" style="left:'+pos(s.vopt)+'%;top:80px;color:#8a6420">vendre ½ &gt; '+fr(sellKey(s),0)+'</div>';
  h += '<div class="v2-price" style="left:'+pos(s.price)+'%"><span>cours '+fr(s.price)+'</span><i></i></div></div>';
  return h;
}

// ---- les 6 ratios ----
function gauge(name, val, scale, cuts, note, faded){
  if(val===null||val===undefined||isNaN(val)||val<=0) return '';
  var i = val<cuts[0]?0:val<cuts[1]?1:val<cuts[2]?2:3;
  var lo=[0,cuts[0],cuts[1],cuts[2]][i], hi=[cuts[0],cuts[1],cuts[2],cuts[2]*2][i];
  var p = Math.min(98, i*25 + Math.min(1,(val-lo)/(hi-lo))*25);
  var lab = ['Attractif','Juste prix','Élevé','Très élevé'][i], col=[C.gn,C.gn2,C.or,C.rd][i];
  return '<div class="v2-ratio'+(faded?' v2-faded':'')+'"><div><b>'+name+'</b> <span class="v2-mono">'+fr(val,1)+'</span><br><span class="v2-small">'+scale+'</span></div>'+
    '<div class="v2-gauge"><span style="left:'+p+'%"></span></div>'+
    '<div class="v2-small"><b style="color:'+(faded?C.mu:col)+'">'+(faded?'Peu pertinent':lab)+'</b>'+(note?' · '+note:'')+'</div></div>';
}
function ratios(s){
  var fin=isFin(s), re=isRealEstate(s), hiMargin = s.margin>20;
  var peg = (s.pe>0 && s.gused>0) ? s.pe/s.gused : null;
  var pfcf = s.fcf>0 ? 100/s.fcf : null;
  var h = gauge('PER', s.pe, '<10 · 10-20 · 20-30 · >30', [10,20,30], '', false) +
    gauge('PEG', peg, '<1 · 1-2 · 2-3 · >3', [1,2,3], 'PER ÷ croissance retenue', fin) +
    gauge('Cours / cash libre', pfcf, '<10 · 10-20 · 20-30 · >30', [10,20,30], '', fin) +
    gauge('VE / EBITDA', s.ev_ebitda, '<8 · 8-12 · 12-18 · >18', [8,12,18], hiMargin?'élevé normal si marge forte':'', fin) +
    gauge('Cours / actif net', s.pb, '<1 · 1-2 · 2-4 · >4', [1,2,4], (fin||re)?'ratio clé ici':'peu utile hors banques/foncières', !(fin||re)) +
    gauge('Cours / ventes', s.ps, '<1 · 1-3 · 3-6 · >6', [1,3,6], hiMargin?'marge nette '+fr(s.margin,0)+' %':'', hiMargin);
  // 07/10/2026 : comparaison avec l'historique propre de l'entreprise
  var hc = function(lbl, now, past){
    if(!(now>0) || !(past>0)) return '';
    var d = (now/past-1)*100, col = d<=-10?C.gn:d>=10?C.rd:C.mu;
    return '<div class="v2-crit"><span>'+lbl+' <span class="v2-small">aujourd’hui '+fr(now,1)+' · médiane '+(s.hn||'')+' clôtures annuelles '+fr(past,1)+'</span></span><b class="v2-mono" style="color:'+col+'">'+(d<=-10?'moins cher que d’habitude':d>=10?'plus cher que d’habitude':'dans ses habitudes')+' ('+sgn(d,0)+')</b></div>';
  };
  var hx = fin ? '' : hc('PER', s.pe, s.pe_h)+hc('Cours / cash libre', pfcf, s.pfcf_h)+hc('VE / EBITDA', s.ev_ebitda, s.eveb_h);
  // 11/10/2026 : repères d'entrée (méthode de l'Analyste Curieux)
  var eps = (s.pe>0) ? s.price/s.pe : null;
  if(!fin && eps && s.pe_lo>0) hx += (s.pe < s.pe_lo)
    ? '<div class="v2-crit"><span>PER le plus bas des dernières années : '+fr(s.pe_lo,1)+' <span class="v2-small">(aujourd’hui '+fr(s.pe,1)+')</span></span><b class="v2-mono" style="color:'+C.gn+'">déjà moins cher qu’à son point le plus bas — chercher pourquoi</b></div>'
    : '<div class="v2-crit"><span>Prix si l’action retombait à son PER le plus bas des dernières années <span class="v2-small">('+fr(s.pe_lo,1)+' × bénéfice)</span></span><b class="v2-mono">'+fr(eps*s.pe_lo,0)+' € <span class="v2-small">('+sgn(pct(eps*s.pe_lo,s.price),0)+')</span></b></div>';
  if(s.div12>0 && s.dy_med>0){ var dyn=s.div12/s.price*100, pdy=s.div12/(s.dy_med/100);
    hx += '<div class="v2-crit"><span>Rendement du dividende <span class="v2-small">aujourd’hui '+fr(dyn,1)+' % · médiane '+s.dy_n+' ans '+fr(s.dy_med,1)+' %</span></span><b class="v2-mono">prix au rendement médian '+fr(pdy,0)+' € <span class="v2-small">('+sgn(pct(pdy,s.price),0)+')</span></b></div>'; }
  if(hx) h += '<div class="v2-k" style="margin-top:8px">Par rapport à sa propre histoire</div>'+hx+'<div class="v2-small">Plus parlant que le barème général : une entreprise de qualité se paie souvent cher, la question est « plus cher que d’habitude ? ».</div>';
  return h ? '<section class="v2-card"><div class="v2-head"><h2>Est-ce cher ? Les 6 ratios</h2><span class="v2-small">Barème général · les ratios grisés ne sont pas pertinents pour ce métier</span></div>'+
    '<div class="v2-scale"><div style="background:'+C.gn+'">ATTRACTIF</div><div style="background:'+C.gn2+'">JUSTE PRIX</div><div style="background:'+C.or+'">ÉLEVÉ</div><div style="background:'+C.rd+'">TRÈS ÉLEVÉ</div></div>'+h+'</section>' : '';
}

// ---- qualité ----
function crit(label, thr, val, ok){
  return '<div class="v2-crit"><span>'+label+' <span class="v2-small">('+thr+')</span></span><b class="v2-mono" style="color:'+(ok===null?C.mu:ok?C.gn:C.rd)+'">'+val+'</b></div>';
}
function hist(s){
  if(!s.revh) return null;
  var yrs=(s.yrs||'').split('|'), rv=s.revh.split('|').map(Number), ni=(s.nih||'').split('|').map(Number), fc=(s.fcfh||'').split('|').map(Number);
  return {yrs:yrs, rv:rv, ni:ni, fc:fc};
}
function quality(s){
  if(s.grid==='banque'){
    var b1=s.roem!=null&&s.roem>=10, b2=s.roemin!=null&&s.roemin>=6, b4=s.bvg!=null&&s.bvg>=2;
    var nn=(s.nih||'').split('|').filter(function(x){return x!=='';}).map(Number), b3=nn.length>0&&nn.every(function(x){return x>0;});
    return '<section class="v2-card"><h2>Qualité (grille banque / assurance) : '+[b1,b2,b3,b4].filter(Boolean).length+' / 4</h2>'+
      crit('Rentabilité des fonds propres (médiane 4 ans)','≥ 10 %', s.roem==null?'—':fr(s.roem,1)+' %', s.roem==null?null:b1)+
      crit('Pire année','≥ 6 %', s.roemin==null?'—':fr(s.roemin,1)+' %', s.roemin==null?null:b2)+
      crit('Aucune perte sur 4 ans','oui', nn.length?(b3?'oui':'non'):'—', nn.length?b3:null)+
      crit('Croissance de l’actif net par action','≥ 2 %/an', s.bvg==null?'—':fr(s.bvg,1)+' %', s.bvg==null?null:b4)+
      '<div class="v2-note" style="background:#fbf4e6"><span><b>À vérifier dans la contre-expertise</b> (pas dans les données gratuites) : solvabilité (ratio CET1 ≥ 12 % pour une banque, Solvabilité II ≥ 170 % pour un assureur) et coût du risque.</span></div>'+
      (s.qwhy?'<div class="v2-small">'+esc(s.qwhy)+'</div>':'')+'</section>';
  }
  if(s.grid==='fonciere'){
    var f1=s.ltv!=null&&s.ltv<=45, f2=s.icr!=null&&s.icr>=2.5, f3=s.cagr!=null&&s.cagr>=0;
    return '<section class="v2-card"><h2>Qualité (grille foncière) : '+[f1,f2,f3].filter(Boolean).length+' / 3 + exploitation</h2>'+
      crit('Dette nette / actifs (approche du LTV)','≤ 45 %', s.ltv==null?'—':fr(s.ltv,1)+' %', s.ltv==null?null:f1)+
      crit('Couverture des intérêts (résultat d’exploitation / intérêts)','≥ 2,5', s.icr==null?'—':fr(s.icr,1), s.icr==null?null:f2)+
      crit('Loyers (chiffre d’affaires) sur 4 ans','stables ou en hausse', s.cagr==null?'—':fr(s.cagr,1)+' %/an', s.cagr==null?null:f3)+
      '<div class="v2-note" style="background:#fbf4e6"><span><b>À vérifier dans la contre-expertise :</b> actif net réévalué officiel (EPRA NTA), LTV publié, taux d’occupation, échéance de la dette.</span></div>'+
      (s.qwhy?'<div class="v2-small">'+esc(s.qwhy)+'</div>':'')+'</section>';
  }
  if(isFin(s)) return '<section class="v2-card"><h2>Qualité</h2><p>Holding : grille dédiée (décote sur actif net réévalué) <b>en préparation</b>. Pas de verdict qualité en attendant.</p></section>';
  var n=0, h='';
  var c1 = s.roicx!=null && s.roicx>=15, c2 = s.roic!=null && s.roic>=12, c3 = s.fcfc!=null && s.fcfc>=80, c4 = s.nde!=null && s.nde<=2.5, c5 = s.gused!=null && s.gused>=3;
  [c1,c2,c3,c4,c5].forEach(function(x){ if(x) n++; });
  h += crit('Rentabilité du capital hors écarts d’acquisition','≥ 15 %', s.roicx==null?'—':(s.roicx>100?'>100':fr(s.roicx,1))+' %', s.roicx==null?null:c1);
  h += crit('Rentabilité du capital total','≥ 12 %', s.roic==null?'—':(s.roic>100?'>100':fr(s.roic,1))+' %', s.roic==null?null:c2);
  h += crit('Bénéfice transformé en cash','≥ 80 %', s.fcfc==null?'—':fr(s.fcfc,0)+' %', s.fcfc==null?null:c3);
  h += crit('Dette nette / EBITDA','≤ 2,5', s.nde==null?'—':(s.nde<0?'trésorerie nette':fr(s.nde,2)), s.nde==null?null:c4);
  h += crit('Croissance retenue'+(s.gsrc&&/communique/.test(s.gsrc)?' (communiqué)':' (Yahoo)'),'≥ 3 %/an', s.gused==null?'—':fr(s.gused,1)+' %', s.gused==null?null:c5);
  var reg='';
  var H = hist(s);
  if(s.regn){
    var ok = s.regu >= s.regn-1;
    var bars='';
    if(H){
      var mx=Math.max.apply(null,H.rv.filter(function(x){return !isNaN(x);}))||1;
      for(var i=H.rv.length-1;i>=0;i--){ if(isNaN(H.rv[i])) continue;
        bars += '<div class="v2-col"><span class="v2-mono">'+fr(H.rv[i],0)+'</span><i style="height:'+Math.max(4,Math.round(H.rv[i]/mx*62))+'px;background:'+(i===0?C.gn:C.gn2)+'"></i><span class="v2-small">'+(H.yrs[i]||'')+'</span></div>'; }
    }
    reg = '<div class="v2-reg" style="background:'+(ok?'#eef6f1':'#fbecea')+'"><div class="v2-crit" style="border:0"><span><b>Régularité</b> <span class="v2-small">(achat possible si CA en hausse ≥ '+(s.regn-1)+' ans sur '+s.regn+')</span></span><b class="v2-mono" style="color:'+(ok?C.gn:C.rd)+'">'+s.regu+' / '+s.regn+'</b></div>'+
      (bars?'<div class="v2-bars">'+bars+'</div><div class="v2-small">Chiffre d’affaires en millions ('+esc(s.fcur||'')+')'+(s.nregu!=null?' · bénéfice en hausse '+s.nregu+' an(s) sur '+s.regn:'')+'</div>':'')+'</div>';
  }
  var roicTxt = (s.roicx!=null) ? '<span><b>Création de valeur :</b> rentabilité du capital '+(s.roicx>100?'>100':fr(s.roicx,1))+' % contre un coût du capital de ~'+COC+' %'+(s.roicx>COC*1.5?' → l’entreprise crée de la valeur.':s.roicx>COC?' → crée un peu de valeur.':' → <b style="color:'+C.rd+'">détruit de la valeur</b>.')+'</span>' : '';
  var pio = s.pio!=null ? '<span class="v2-small">Santé financière (Piotroski) '+s.pio+'/9'+(s.pio<=4?' · <b style="color:'+C.rd+'">alerte</b>':'')+'</span>' : '';
  return '<section class="v2-card"><h2>Qualité : '+n+' / 5 critères'+(s.regn?' + régularité':'')+'</h2>'+h+reg+
    '<div class="v2-note">'+roicTxt+pio+'</div>'+
    (s.qwhy?'<div class="v2-small">'+esc(s.qwhy)+'</div>':'')+'</section>';
}

// ---- moat + concurrents ----
function moat(s, F){
  var sc = s.mscore;
  var comp = (F&&F.comp) ? '<div class="v2-comp">'+F.comp.map(function(c){return '<div><b>'+esc(c[0])+'</b><br><span class="v2-small">'+esc(c[1])+'</span></div>';}).join('')+'</div>' : '<div class="v2-small">Concurrents : à rédiger.</div>';
  return '<section class="v2-card"><div class="v2-head"><h2>Moat : '+(sc!=null?sc+' / 5':'non évalué')+'</h2>'+
    (s.unc?'<span class="v2-pill" style="background:'+(s.unc==='elevee'?'#fbecea':s.unc==='faible'?'#eef6f1':'#fbf4e6')+';color:'+(s.unc==='elevee'?C.rd:s.unc==='faible'?C.gn:'#8a6420')+'">INCERTITUDE '+(UNC[s.unc]||'NON ÉVALUÉE').toUpperCase()+(UNCM[s.unc]?' → DÉCOTE '+UNCM[s.unc]:'')+'</span>':'')+'</div>'+
    (s.mtype?'<p><b>D’où vient l’avantage :</b> '+esc(s.mtype)+'.</p>':'')+
    '<div><b>Pourquoi pas un concurrent ?</b></div>'+comp+
    (s.mthreat?'<div style="color:'+C.rd+'"><b>Menace :</b> '+esc(s.mthreat)+'.</div>':'')+
    '<div class="v2-small">'+((typeof FICHE!=='undefined'&&FICHE[s.ticker]&&FICHE[s.ticker].val)?'Note de moat validée par toi le '+esc(FICHE[s.ticker].val.split('-').reverse().join('/'))+'.':'Note de moat et niveau d’incertitude : jugement de Claude, à valider par toi.')+'</div></section>';
}

// ---- thèse + tableau de bord ----
// 24/10/2026 : profil de Peter Lynch (étiquette, pas une règle) et fiche validée par Val
var PROF = {lente:['Lente','le dividende et sa solidité'], solide:['Solide','le prix payé : croissance régulière, mais souvent chère'], rapide:['Rapide','la durée de la croissance ; si elle s’arrête, le multiple baisse'], cyclique:['Cyclique','où on en est dans le cycle ; un PER bas au sommet est un piège'], retournement:['Retournement','les preuves du redressement'], actifs:['Valeur d’actifs','ce que valent réellement les actifs']};
function thesis(s, F){
  if(!F) return '<section class="v2-card"><h2>Ma thèse d’investissement</h2><p class="v2-small">Pas encore rédigée pour cette valeur (rédigée en priorité pour tes lignes et les valeurs de qualité).</p></section>';
  var rows = (F.kpi||[]).map(function(k){ return '<tr><td>'+esc(k[0])+'</td><td class="v2-mono">'+esc(k[1])+'</td><td>'+esc(k[2])+'</td></tr>'; }).join('');
  return '<section class="v2-card"><div class="v2-head"><h2>Ma thèse d’investissement</h2>'+(F.prof&&PROF[F.prof]?'<span class="v2-pill" style="background:#eef1f6;color:#0e1c33">'+PROF[F.prof][0].toUpperCase()+'</span> ':'')+(F.val?'<span class="v2-pill" style="background:#eef6f1;color:'+C.gn+'">VALIDÉE LE '+esc(F.val.split('-').reverse().join('/'))+'</span>':'<span class="v2-pill" style="background:#fbf4e6;color:#8a6420">BROUILLON — À VALIDER</span>')+'</div>'+(F.prof&&PROF[F.prof]?'<p class="v2-small"><b>Profil '+PROF[F.prof][0].toLowerCase()+' :</b> à regarder en priorité, '+PROF[F.prof][1]+'.</p>':'')+
    '<div class="v2-grid3"><div><div class="v2-k" style="color:'+C.gn+'">Pourquoi la posséder</div>'+esc(F.why)+'</div>'+
    '<div><div class="v2-k">Pourquoi maintenant</div>'+(s.gimp!=null&&s.gused!=null?'Le cours suppose '+fr(s.gimp,1)+' %/an ; on retient '+fr(s.gused,1)+' %. '+(s.gimp<s.gused?'Le marché est plus pessimiste que l’entreprise.':'Le marché est déjà plus optimiste que l’entreprise.'):'Voir la zone d’achat.')+'</div>'+
    '<div><div class="v2-k" style="color:'+C.rd+'">Ce qui prouverait que j’ai tort</div>'+esc(F.wrong)+'</div></div>'+
    (rows?'<div class="v2-k" style="margin-top:6px">Tableau de bord de la thèse <span class="v2-small">· à vérifier à chaque publication</span></div><div class="v2-scroll"><table class="v2-tab"><thead><tr><th>Indicateur</th><th>Dernière valeur</th><th>Alerte si</th></tr></thead><tbody>'+rows+'</tbody></table></div><div class="v2-small">Deux alertes en même temps = thèse cassée → vente, quel que soit le cours.</div>':'')+
    '<div class="v2-small">'+(F.dep?'Dépendance : '+esc(F.dep):'')+(F.next?' · Prochain rendez-vous : '+esc(F.next):'')+'</div></section>';
}

// ---- chiffres clés ----
function figures(s){
  var H = hist(s); if(!H) return '';
  var head='', r1='', r2='', r3='', r4='';
  for(var i=H.rv.length-1;i>=0;i--){
    head+='<th>'+esc(H.yrs[i]||'')+'</th>';
    r1+='<td>'+fr(H.rv[i],0)+'</td>';
    r2+='<td>'+fr(H.ni[i],0)+'</td>';
    r3+='<td>'+((H.rv[i]&&!isNaN(H.ni[i]))?fr(H.ni[i]/H.rv[i]*100,1)+' %':'—')+'</td>';
    r4+='<td>'+fr(H.fc[i],0)+'</td>';
  }
  return '<section class="v2-card"><h2>Chiffres clés <span class="v2-small">(millions '+esc(s.fcur||'')+', Yahoo, comptes annuels publiés)</span></h2><div class="v2-scroll"><table class="v2-tab v2-num"><thead><tr><th>Key figures</th>'+head+'</tr></thead><tbody>'+
    '<tr><td>Chiffre d’affaires (Revenue)</td>'+r1+'</tr><tr><td>Résultat net (Net income)</td>'+r2+'</tr><tr><td>Marge nette (Net margin)</td>'+r3+'</tr><tr><td>Cash-flow libre (Free cash flow)</td>'+r4+'</tr></tbody></table></div>'+
    '<div class="v2-tiles"><div>PER<br><b>'+fr(s.pe,1)+'</b></div><div>VE / EBITDA<br><b>'+fr(s.ev_ebitda,1)+'</b></div><div>Rendement<br><b>'+fr(s.yield,1)+' %</b></div><div>Rendement cash (FCF)<br><b>'+fr(s.fcf,1)+' %</b></div></div></section>';
}

// ---- prix : scénarios et zone ----
function priceBlock(s){
  if(!(s.qok||s.near) || (s.vmeth!=='qarp'&&s.vmeth!=='pb') || !s.vpess){
    return '<section class="v2-card"><h2>Le prix</h2><p>Pas de zone d’achat : la valeur ne passe pas le filtre qualité, la méthode ne cherche donc pas à l’acheter. '+
      (s.tp>0?'Pour information, objectif moyen des analystes : <b>'+fr(s.tp)+' €</b>.':'')+'</p></section>';
  }
  var card = function(t,col,bg,v,txt,out){ return '<div class="v2-scen" style="background:'+bg+(out?';outline:2px solid '+C.ink:'')+'"><div class="v2-k" style="color:'+col+'">'+t+'</div><div class="v2-big">'+fr(v,0)+' € <span style="font-size:14px;color:'+(v>=s.price?C.gn:C.rd)+'">'+sgn(pct(v,s.price))+'</span></div><div class="v2-small">'+txt+'</div></div>'; };
  var gc = s.gmod!=null ? s.gmod : (s.gused!=null ? Math.max(0,Math.min(12,s.gused)) : null);
  var gcap = (gc!=null && gc>12) ? 20 : 12;
  return '<section class="v2-card"><div class="v2-head"><h2>Ce que vaut l’action : trois estimations</h2>'+
    (s.unc?'<span class="v2-pill" style="background:#f5f3ee;color:'+C.ink+'">INCERTITUDE '+(UNC[s.unc]||'NON ÉVALUÉE').toUpperCase()+'</span>':'')+'</div>'+
    (s.irr!=null?(function(){ var R=(s.irrn!=null?s.irrn:s.irr), RQ=(s.grid==='banque'?10:8.5), RQs=fr(RQ,1); var hyp=(s.grid==='banque'?'la rentabilité des fonds propres ('+fr(s.roem,1)+' %) se maintient':s.grid==='fonciere'?'les loyers suivent l’inflation (estimation simple : rendement + 2 %)':'la croissance retenue ('+fr(s.gused,1)+' %/an'+(s.gmod!=null&&s.gused!=null&&s.gmod<s.gused-0.05?', dont '+fr(s.gmod,1)+' % pris en compte : au-delà de 12 %, on ne retient que la moitié, plafond 20 %, et seulement pour un moat ≥ 4':'')+') se réalise'); return '<div class="v2-note" style="background:'+(R>=RQ?'#eef6f1':'#fbecea')+'"><span><b>En clair : si tu achètes à '+fr(s.price)+' €</b> et que '+hyp+', l’action devrait rapporter <b class="v2-mono">≈ '+fr(R,1)+' %/an</b> (dividendes compris'+(s.wht>0?', <b>net de la retenue à la source de '+fr(s.wht,1)+' % perdue en PEA</b> ; '+fr(s.irr,1)+' % avant':'')+'). La méthode exige '+RQs+' %/an'+(s.grid==='banque'?' (banque ou assurance : plus risqué)':'')+(R>=RQ?' : <b style="color:'+C.gn+'">le prix le permet</b>.':' : <b style="color:'+C.rd+'">trop cher pour ton exigence</b>. La valeur centrale ci-dessous est le prix qui donnerait '+RQs+' %/an.')+'</span></div>'; })():'')+
    '<div class="v2-grid3">'+
      (s.grid==='banque' ?
        card('PESSIMISTE',C.rd,'#fbecea',s.vpess,'Rentabilité des fonds propres '+fr(s.roem-3,1)+' % (3 points de moins).')+
        card('CENTRAL',C.ink,C.bg,s.dcfm,'Prix pour gagner 10 %/an si la rentabilité reste à '+fr(s.roem,1)+' %.',true)+
        card('OPTIMISTE',C.gn,'#eef6f1',s.vopt,'Rentabilité '+fr(s.roem+2,1)+' % (2 points de plus).')
      : s.grid==='fonciere' ?
        card('PESSIMISTE',C.rd,'#fbecea',s.vpess,'Patrimoine dévalué de 20 %.')+
        card('CENTRAL',C.ink,C.bg,s.dcfm,'Actif net comptable par action (approche de l’actif net réévalué).',true)+
        card('OPTIMISTE',C.gn,'#eef6f1',s.vopt,'Patrimoine réévalué de 10 %.')
      :
      card('PESSIMISTE',C.rd,'#fbecea',s.vpess,'Plus aucune croissance pendant 10 ans.')+
      card('CENTRAL',C.ink,C.bg,s.dcfm,'Prix pour gagner 8,5 %/an si '+(gc!=null?fr(gc,1)+' %/an au départ':'la croissance retenue')+', ralentissant vers 2,5 %.',true)+
      card('OPTIMISTE',C.gn,'#eef6f1',s.vopt,(gc!=null?fr(Math.min(gcap,gc+3),1)+' %/an au départ':'croissance + 3 points')+'.'))+
    '</div>'+(s.vref==='mediane'?'<div class="v2-note" style="background:#fbf4e6"><span><b>Valeur ramenée à la médiane des 3 méthodes</b> : le calcul central dépassait de plus de 30 % les deux contrôles. Sur 33 valeurs comparées à Baggr, ce cas était presque toujours trop optimiste ; les paliers partent donc de la valeur la plus prudente.</span></div>':'')+'<p class="v2-small">Ce ne sont <b>pas des prévisions de cours</b> : c’est ce que l’entreprise vaut selon trois hypothèses. Le « +x % » est l’écart avec le cours d’aujourd’hui, rien ne garantit que le marché le comble.</p>'+priceBar(s)+
    (s.vepv>0?'<div class="v2-note"><span><b>Contrôle n°1 · valeur sans aucune croissance</b> (ce n’est pas un prix d’achat : seuls les paliers décident) — résultat d’exploitation moyen sur 4 ans, après impôt, divisé par 8,5 %, plus la trésorerie, moins toute la dette : <span class="v2-mono">'+fr(s.vepv,0)+' €</span>. '+(s.price>s.vepv?'Au cours actuel, tu paies <b>'+fr(s.price-s.vepv,0)+' €</b> par action pour la croissance future ('+fr((1-s.vepv/s.price)*100,0)+' % du cours).':'<b style="color:'+C.gn+'">Le cours est sous la valeur sans croissance</b> : le marché parie sur un déclin, ou c’est une vraie affaire. À vérifier.')+(s.vmed>0?' <b>Valeur médiane des 3 méthodes : <span class="v2-mono">'+fr(s.vmed,0)+' €</span></b>.':'')+'</span></div>':'')+
    (s.vmult>0?'<div class="v2-note"><span><b>Contrôle n°2 · méthode des multiples</b> (bénéfice sur 5 ans revendu au PER habituel de l’entreprise, plafonné à 20 — 25 pour un moat de 5) : <span class="v2-mono">'+fr(s.vmult,0)+' €</span>, soit '+sgn(pct(s.vmult,s.dcfm),0)+' par rapport au scénario central. '+(Math.abs(s.vmult/s.dcfm-1)>0.35?'<b style="color:'+C.rd+'">Les deux méthodes divergent : zone d’achat à prendre avec prudence.</b>':'Les deux méthodes concordent.')+'</span></div>':'')+
    (s.gimp!=null?'<div class="v2-note"><span><b>Ce que le cours suppose :</b> <span class="v2-mono">'+fr(s.gimp,1)+' %/an</span> contre <span class="v2-mono" style="color:'+C.gn+'">'+fr(s.gused,1)+' %/an retenus</span></span></div>':'')+
    '<div class="v2-small">Deux paliers : <b>palier 1</b> = zone d’achat (décote 10-20 % / 15-25 % / 20-30 % selon l’incertitude) → demi-position ; <b>palier 2</b> = décote Morningstar 5 étoiles (20 / 30 / 40 %) → position complète. Sous le seuil de revue : relire la thèse, pas de vente automatique.</div></section>';
}

function technical(s){
  var tr = (s.price>s.mm200) ? 'au-dessus de la moyenne 200 jours : tendance de fond haussière' : 'sous la moyenne 200 jours : tendance de fond baissière';
  return '<details class="v2-card v2-det"><summary>Détails techniques</summary><div class="v2-tiles"><div>Moyenne 50 j<br><b>'+fr(s.mm50)+' €</b></div><div>Moyenne 200 j<br><b>'+fr(s.mm200)+' €</b></div><div>RSI 14 j<br><b>'+fr(s.rsi,1)+'</b></div><div>Plus bas / haut 1 an<br><b>'+fr(s.b52l)+' – '+fr(s.b52h)+'</b></div></div><p class="v2-small">Cours '+tr+'.'+(s.knife?' <b style="color:'+C.rd+'">Chute en cours.</b>':'')+'</p>'+
    '<div class="v2-k" style="margin-top:8px">Rentabilité et bilan (pour comprendre, ne décident rien)</div><div class="v2-tiles">'+
    [['VE / EBIT',s.ev_ebit,'x'],['Rentabilité des fonds propres (ROE)',s.roe,' %'],['Rentabilité des actifs (ROA)',s.roa,' %'],['Marge brute',s.gm,' %'],['Marge nette',s.margin,' %'],
     ['Investissements / ventes',s.capr,' %'],['Dette / fonds propres',s.de,'x'],['Couverture des intérêts',s.icr,'x'],['Liquidité courante',s.cr,'x']]
      .filter(function(x){return x[1]!=null && x[1]!==0;}).map(function(x){return '<div>'+x[0]+'<br><b>'+fr(x[1],1)+x[2]+'</b></div>';}).join('')+'</div>'+
    '<p class="v2-small">Un ROE très élevé avec peu de fonds propres (rachats d’actions) n’est pas un signe de qualité en soi : c’est le ROIC qui compte.</p></details>';
}

function sources(s){
  var q = encodeURIComponent(s.name||s.ticker);
  return '<section class="v2-card v2-small"><p>Sources : cours et ratios Yahoo Finance (mise à jour automatique) · croissance : '+esc(s.gsrc||'Yahoo')+' · '+
    (s.x2s?'contrôle par les '+esc(s.x2s)+' (filings.xbrl.org)'+(s.x2?' : <b>écart</b>':' : concordant')+' · ':'')+
    (s.bg?'contrôle Baggr du '+esc(s.bg.date)+' : '+(s.bg.verdict==='ecart'?'<b style="color:#a8322b">écart</b>'+(s.bg.note?' ('+esc(s.bg.note)+')':''):s.bg.verdict==='non verifiable'?'non vérifiable'+(s.bg.note?' ('+esc(s.bg.note)+')':''):'concordant'+(s.bg.note?' ('+esc(s.bg.note)+')':''))+' · ':'')+
    '<a href="https://www.zonebourse.com/recherche/?q='+q+'" target="_blank" rel="noopener">Zonebourse</a> · '+
    '<a href="https://www.boursorama.com/recherche/'+q+'/" target="_blank" rel="noopener">Boursorama</a></p></section>';
}


// ---- 06/10/2026 : mémoire des contre-expertises + décision finale ----
var CEL = {intacte:['THÈSE INTACTE',C.gn,'#eef6f1'], fragilisee:['THÈSE FRAGILISÉE',C.or,'#fbf4e6'], cassee:['THÈSE CASSÉE',C.rd,'#fbecea']};
function ceList(t){
  var a = (typeof CE!=='undefined' && CE[t]) ? CE[t].slice() : [];
  try{ var loc = JSON.parse(localStorage.getItem('v2_ce_'+t)||'[]'); a = a.concat(loc); }catch(e){}
  return a.sort(function(x,y){ return x.date<y.date?1:-1; });
}
window.v2ceList = ceList;
function ceBlock(s){
  var L = ceList(s.ticker);
  var items = L.map(function(c,i){
    var k = CEL[c.concl]||['À LIRE','#6b7487','#f5f3ee'];
    var kpi = (c.kpi||[]).map(function(r){ return '<tr><td>'+esc(r[0])+'</td><td class="v2-mono">'+esc(r[1])+'</td><td><b style="color:'+(/^OK/.test(r[2])?C.gn:/^NON/.test(r[2])?C.mu:C.rd)+'">'+esc(r[2])+'</b></td></tr>'; }).join('');
    var src = (c.sources||[]).map(function(x){ return '<a href="'+esc(x[1])+'" target="_blank" rel="noopener">'+esc(x[0])+'</a>'; }).join(' · ');
    var body = c.html ? '<div class="v2-small" style="color:#1a2233;line-height:1.55">'+c.html+'</div>' :
      '<p>'+esc(c.resume||'')+'</p>'+
      (kpi?'<div class="v2-scroll"><table class="v2-tab"><thead><tr><th>Indicateur</th><th>Valeur trouvée</th><th>État</th></tr></thead><tbody>'+kpi+'</tbody></table></div>':'')+
      (c.direction?'<p class="v2-small"><b>Direction :</b> '+esc(c.direction)+'</p>':'')+
      (c.analystes?'<p class="v2-small"><b>Analystes :</b> '+esc(c.analystes)+'</p>':'')+
      (c.contre?'<p class="v2-small"><b style="color:'+C.rd+'">Meilleur argument contre :</b> '+esc(c.contre)+'</p>':'')+
      (c.decision?'<p class="v2-small"><b>Décision proposée alors :</b> '+esc(c.decision)+'</p>':'')+
      (c.lien?'<p><a href="'+esc(c.lien)+'" target="_blank" rel="noopener" style="font-weight:600">Lire l’analyse complète (6 étapes)</a> <span class="v2-small">document privé, visible seulement par toi</span></p>':'')+
      (src?'<p class="v2-small">Sources : '+src+'</p>':'');
    return '<details class="v2-ce"'+(i===0?' open':'')+'><summary><span class="v2-pill" style="background:'+k[2]+';color:'+k[1]+'">'+k[0]+(c.point?' · '+esc(c.point):'')+'</span> <span class="v2-small">'+esc(c.date)+' · '+esc(c.by||'')+'</span></summary>'+body+'</details>';
  }).join('');
  return '<section class="v2-card"><div class="v2-head"><h2>Contre-expertises</h2><span class="v2-small">Photo datée à l’instant T · jamais effacée · à refaire après chaque publication</span></div>'+
    (items || '<p class="v2-small">Aucune contre-expertise pour l’instant. Demande-la à Claude dans la conversation, ou utilise le bouton (nécessite du crédit API).</p>')+
    '<div id="v2-ce-slot"></div></section>';
}
function ptfTotal(){
  var list=(typeof PTF!=='undefined')?PTF:[], tot=0;
  list.forEach(function(x){
    var st=S.find(function(y){return y&&y.ticker===x.ticker;});
    var et=(typeof ETF!=='undefined')?ETF.find(function(y){return y&&y.ticker===x.ticker;}):null;
    tot += (st?st.price:(et&&et.price?et.price:x.pru))*x.qty;
  });
  return tot;
}
// ---- 13/10/2026 : controle avant achat (cases a cocher, pas de texte) ----
// Les cases automatiques viennent du screener ; les autres sont cochees a la
// main apres l'analyse. Gardees dans CE navigateur seulement (rien de public),
// valables 90 jours. Tant qu'il manque une case, la decision reste "PAS ENCORE".
var CHK = [
  ['metier',  'J’explique le métier en une phrase'],
  ['moat',    'J’ai nommé le moat et ce qui pourrait le casser'],
  ['sources', 'Deux sources concordent sur les chiffres (screener + une autre)'],
  ['contre',  'J’ai écrit la meilleure raison de ne PAS acheter'],
  ['calcul',  'Mon calcul (onglet Analyser) et le screener concordent à 25 % près'],
  ['tort',    'J’ai écrit les 3 chiffres qui me feraient dire que j’avais tort']
];
function chkGet(t){ try{ var o=JSON.parse(localStorage.getItem('v2_chk_'+t)||'{}'); if(o.date && (Date.now()-new Date(o.date).getTime())/864e5>90) return {}; return o; }catch(e){ return {}; } }
function chkState(s){
  var o=chkGet(s.ticker), auto=[['qualite','Les critères de qualité passent', !!s.qok],['zone','Le cours est dans la zone d’achat', palier(s)>0]];
  var man=CHK.map(function(c){ return [c[0], c[1], !!o[c[0]]]; });
  var all=auto.concat(man), done=all.filter(function(x){return x[2];}).length;
  return {auto:auto, man:man, done:done, total:all.length, ok:done===all.length, date:o.date};
}
window.v2chk = function(t, k, on){
  var o=chkGet(t); o[k]=on; o.date=new Date().toISOString().slice(0,10);
  try{ localStorage.setItem('v2_chk_'+t, JSON.stringify(o)); }catch(e){}
  var s=S.find(function(x){return x.ticker===t;}); if(s && typeof render==='function') render(s);
};
function checklist(s){
  if(!(s.qok||s.near)) return '';
  var st=chkState(s);
  var line=function(x, auto){ return '<label style="display:flex;gap:10px;align-items:flex-start;padding:6px 0;min-height:32px;cursor:'+(auto?'default':'pointer')+'"><input type="checkbox" '+(x[2]?'checked ':'')+(auto?'disabled ':'onchange="v2chk(\''+s.ticker+'\',\''+x[0]+'\',this.checked)" ')+'style="width:20px;height:20px;flex:none;margin-top:1px"><span>'+x[1]+(auto?' <span class="v2-small">(automatique)</span>':'')+'</span></label>'; };
  return '<section class="v2-card" style="border-left:4px solid '+(st.ok?C.gn:C.or)+'"><div class="v2-head"><h2>Contrôle avant achat : '+st.done+' / '+st.total+'</h2><span class="v2-small">'+(st.date?'coché le '+st.date+' · valable 90 jours':'gardé dans ce navigateur seulement')+'</span></div>'+
    st.auto.map(function(x){return line(x,true);}).join('')+st.man.map(function(x){return line(x,false);}).join('')+
    '<p class="v2-small" style="margin-top:8px"><b>'+(st.ok?'Contrôle complet : l’achat peut être validé.':'Achat bloqué tant qu’une case manque.')+'</b> Méthode détaillée : onglet « Analyser une action ».</p></section>';
}

// ---- 13/10/2026 : seuil de sortie (decide avec l'utilisatrice) ----
// Conversion annuelle du benefice en cash : >= 80 % garder ; 60-80 % garder
// sans renforcer (these fragilisee, contre-expertise) ; < 60 % deux annees de
// suite = vendre. Sous le seuil de revue (prix) : contre-expertise obligatoire.
// Pas pour banques, assurances, foncieres (le cash libre s'y lit autrement).
function cashConv(s){
  var f=String(s.fcfh||'').split('|').map(Number), n=String(s.nih||'').split('|').map(Number), y=String(s.yrs||'').split('|');
  var out=[]; for(var i=0;i<Math.min(f.length,n.length);i++){ if(n[i]>0 && isFinite(f[i])) out.push({y:y[i]||'', c:Math.round(f[i]/n[i]*100)}); }
  return out; // plus recente en premier
}
function exitState(s){
  if(isFin(s)||isRealEstate(s)||s.grid==='fonciere'||s.grid==='banque'||/centres commerciaux|entrep[oô]ts logistiques/i.test(s.sector||'')) return null;
  var L=cashConv(s); if(!L.length) return null;
  var a=L[0].c, b=L[1]?L[1].c:null;
  if(a<60 && b!==null && b<60) return {k:'vendre', t:'VENDRE', c:C.rd, x:'Conversion en cash sous 60 % deux années de suite ('+L[0].y+' : '+a+' %, '+L[1].y+' : '+b+' %).'};
  if(a<60) return {k:'alerte', t:'ALERTE', c:C.rd, x:'Conversion en cash sous 60 % en '+L[0].y+' ('+a+' %). Contre-expertise : si l’année suivante reste sous 60 %, on vend.'};
  if(a<80) return {k:'garder', t:'GARDER SANS RENFORCER', c:C.or, x:'Conversion en cash entre 60 et 80 % en '+L[0].y+' ('+a+' %) : thèse fragilisée, contre-expertise pour comprendre la cause.'};
  return {k:'ok', t:'GARDER', c:C.gn, x:'Conversion en cash de '+a+' % en '+L[0].y+' (seuil 80 %).'};
}
function exitBlock(s){
  var e=exitState(s), L=cashConv(s);
  var rev=(s.stop>0)?'<p class="v2-small"><b>Prix :</b> sous <b>'+fr(s.stop)+' €</b> (seuil de revue), contre-expertise obligatoire dans la semaine. Une baisse est un signal à vérifier, pas une preuve : elle peut venir du marché ou d’un cycle.</p>':'';
  if(!e) return rev?'<section class="v2-card"><h2>Seuil de sortie</h2>'+rev+'</section>':'';
  var hist=L.slice(0,4).map(function(r){ return '<td class="v2-mono" style="color:'+(r.c>=80?C.gn:r.c>=60?C.or:C.rd)+'">'+r.c+' %</td>'; }).join('');
  var hy=L.slice(0,4).map(function(r){ return '<th>'+esc(r.y)+'</th>'; }).join('');
  return '<section class="v2-card" style="border-left:4px solid '+e.c+'"><div class="v2-head"><h2>Seuil de sortie : '+e.t+'</h2><span class="v2-small">règle : ≥ 80 % garder · 60-80 % sans renfort · < 60 % deux ans = vendre</span></div>'+
    '<p>'+e.x+'</p><div class="v2-scroll"><table class="v2-tab"><thead><tr><th>Cash libre / bénéfice</th>'+hy+'</tr></thead><tbody><tr><td></td>'+hist+'</tr></tbody></table></div>'+rev+
    '<p class="v2-small">On ne vend ni parce qu’on a gagné, ni pour éviter de perdre : le prix d’achat n’entre jamais dans la décision.</p></section>';
}

function decision(s){
  var g = (s.qok && s.rec==='buy') ? 'buy' : 'no';
  var L = ceList(s.ticker), last = L[0];
  var age = last ? Math.round((Date.now()-new Date(last.date).getTime())/864e5) : null;
  var SZ = sizes(s), tot = ptfTotal(), full = tot*SZ.full/100, half = tot*SZ.half/100;
  var lim = s.el>0 ? Math.min(s.el, s.price) : s.price;
  var r;
  if(g!=='buy'){
    var v = verdict(s);
    r = {t:'ACHAT : NON', c:'#6b7487', x:v.t.charAt(0)+v.t.slice(1).toLowerCase()+'. '+(s.qok&&s.eh>0?'On attend un cours sous '+fr(s.eh)+' € et une contre-expertise favorable.':'La méthode n’achète pas cette valeur.')};
  } else if(dqAll(s)){
    r = {t:'ACHAT : PAS ENCORE', c:C.or, x:'Le screener dit « achat possible », mais une donnée est suspecte ('+esc(dqAll(s))+'). Vérifie-la sur Zonebourse ou le rapport annuel avant d’acheter.'};
  } else if(!last || age>90){
    r = {t:'ACHAT : PAS ENCORE', c:C.or, x:'Le screener dit « achat possible », mais '+(last?'la dernière contre-expertise date de '+age+' jours':'il n’y a pas encore de contre-expertise')+'. Règle : pas d’achat sans contre-expertise de moins de 3 mois.'};
  } else if(last.concl==='cassee'){
    r = {t:'ACHAT : NON', c:C.rd, x:'La contre-expertise du '+last.date+' conclut que la thèse est cassée.'};
  } else if(exitState(s) && exitState(s).k!=='ok'){
    r = {t:'ACHAT : NON', c:exitState(s).c, x:'Seuil de sortie : '+exitState(s).x+' On ne renforce pas.'};
  } else if(!chkState(s).ok){
    r = {t:'ACHAT : PAS ENCORE', c:C.or, x:'Le parcours est incomplet ('+chkState(s).done+' / '+chkState(s).total+' cases). Coche-les dans « Mon parcours en 6 étapes », en haut de la fiche.'};
  } else {
    var P = palier(s), p2 = z2(s), frag = last.concl==='fragilisee';
    var lvl = frag ? P-1 : P;   // these fragilisee : on descend d'un palier
    var why = frag ? 'Thèse fragilisée ('+esc(last.point||'')+') : on descend d’un palier. ' : 'Thèse intacte (contre-expertise du '+last.date+'). ';
    if(lvl>=2){
      r = {t:'ACHAT : OUI, POSITION COMPLÈTE', c:C.gn, x:why+'Cours sous le palier 2 ('+fr(p2)+' €) : vraie occasion. Position complète'+(tot>0?' : environ <b>'+fr(full,0)+' €</b> ('+fr(SZ.full,1)+' % du portefeuille'+(SZ.cyc?', cyclique':'')+', plafond 10 %)':' ('+fr(SZ.full,1)+' % du portefeuille)')+', ordre à cours limité <b>'+fr(Math.min(p2,s.price))+' €</b> maximum. Si tu as déjà la demi-position, tu la complètes.'};
    } else if(lvl===1){
      r = {t:'ACHAT : OUI À 50 % (PALIER 1)', c:C.or, x:why+'Demi-position'+(tot>0?' : environ <b>'+fr(half,0)+' €</b> ('+fr(SZ.half,SZ.half===1.25?2:1)+' % du portefeuille)':' ('+fr(SZ.half,SZ.half===1.25?2:1)+' % du portefeuille)')+', ordre à cours limité <b>'+fr(Math.min(s.eh,s.price))+' €</b> maximum. Le complément seulement sous <b>'+fr(p2)+' €</b> (palier 2)'+(frag?' et après une contre-expertise « intacte »':'')+'. Si tu as déjà la demi-position : rien à faire, on attend.'};
    } else {
      r = {t:'ACHAT : PAS ENCORE', c:C.or, x:why+'Au palier 1 avec une thèse fragilisée, on n’achète pas. On attend le palier 2 (<b>'+fr(p2)+' €</b>) ou une contre-expertise « intacte ».'};
    }
  }
  var stop = (s.stop>0 && (s.qok||s.near)) ? '<p class="v2-small"><b>Stop :</b> pas d’ordre stop automatique sur une valeur de qualité (il vendrait au pire moment). Sous <b>'+fr(s.stop)+' €</b> (seuil de revue) : contre-expertise obligatoire ; si elle conclut « thèse cassée », on vend.</p>' : '';
  return '<section class="v2-card" style="border:2px solid '+r.c+'"><div class="v2-head"><h2>Décision</h2><span class="v2-small">'+esc(window.v2profName?('Portefeuille : '+window.v2profName()):'')+'</span></div>'+
    '<div class="v2-verdict" style="padding:0"><div class="v2-badge" style="background:'+r.c+'">'+r.t+'</div><p>'+r.x+'</p></div>'+stop+
    '<div><button onclick="v2jnl(\''+s.ticker+'\')" style="min-height:44px;padding:8px 16px;border-radius:999px;border:1px solid #0e1c33;background:#fff;cursor:pointer;font-weight:600">Noter ma décision dans le journal</button> <span class="v2-small">pré-rempli avec la fiche (verdict, thèse, contre-expertise, seuil de revue)</span></div></section>';
}


// ---- 06/10/2026 : journal pré-rempli depuis la fiche ----
// 24/10/2026 : le pré-remplissage reprend le contenu de la fiche (métier, moat,
// chiffres de la contre-expertise, contre-thèse, 3 chiffres d'erreur) et marche
// aussi depuis « Nouvelle entrée » du journal dès qu'on choisit l'action.
function jnlResolve(q){
  if(!q||typeof S==='undefined') return null;
  var n=function(x){ return String(x||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().trim(); };
  var k=n(q), u=String(q).trim().toUpperCase();
  return S.find(function(x){return x.ticker===u;}) || S.find(function(x){return n(x.name)===k;}) ||
         (k.length>=3 ? S.find(function(x){return n(x.name).indexOf(k)===0;}) || S.find(function(x){return n(x.name).indexOf(k)>=0;}) : null) || null;
}
function jnlFill(t, keepType){
  var s=S.find(function(x){return x.ticker===t;}); if(!s) return false;
  var F=(typeof FICHE!=='undefined')?FICHE[t]:null, L=ceList(t), last=L[0], v=verdict(s);
  var set=function(id,val){ var e=document.getElementById(id); if(e) e.value=val; };
  var line=function(a){ return a&&a.length ? a.join(' · ') : ''; };
  set('jnl-ticker', t); set('jnl-cours', s.price);
  if(!keepType) set('jnl-type', (s.qok&&s.rec==='buy')?'ACHAT':'ATTENDRE');
  var moat = (s.mtype||'') + (s.mthreat?' · menace : '+s.mthreat:'') + ((s.mscore||typeof s.moat==='number')?' · note '+(s.mscore||s.moat)+'/5':'');
  var chif = last ? ('contre-expertise du '+last.date+(last.resume?' : '+last.resume:'')+(last.kpi&&last.kpi.length?'\n'+last.kpi.map(function(k){return '- '+line(k);}).join('\n'):'')) : '';
  var contre = (last&&last.contre) ? last.contre : (F&&F.wrong ? F.wrong : '');
  var why = 'Screener ('+new Date().toLocaleDateString('fr-FR')+') : '+v.t+' · cours '+fr(s.price)+' · palier 1 '+fr(s.eh)+' · palier 2 '+fr(z2(s))+' · valeur centrale '+fr(s.dcfm)+
      (last?' · '+(CEL[last.concl]?CEL[last.concl][0].toLowerCase():'?')+' ('+last.date+')':' · pas de contre-expertise')+
      '\n\n1. Le métier en une phrase : '+(F&&F.why?F.why:'')+
      '\n2. Le moat, et ce qui pourrait le casser : '+moat+
      '\n3. Chiffres vérifiés : '+(chif||'à vérifier dans une deuxième source')+
      '\n4. Pourquoi elle peut perdre 30 % : '+(contre||'au moins 3 familles de risques')+
      '\n5. Pourquoi maintenant (le prix) : ';
  var kp = (F&&F.kpi&&F.kpi.length) ? F.kpi.map(function(k){ return '- '+k[0]+' · aujourd’hui '+(k[1]||'—')+' · alerte si '+(k[2]||'—'); }).join('\n') : '- Moteur : \n- Moat : \n- Cash ou bilan : ';
  set('jnl-why', why);
  set('jnl-exit', '6. Mes 3 chiffres qui diraient que j’avais tort :\n'+kp+'\nVente de moitié si le cours dépasse '+fr(sellKey(s))+' (max valeur optimiste / objectif des analystes, plafonné à 1,5 fois la valeur optimiste).');
  var w=document.getElementById('jnl-why'); if(w){ w.dataset.auto=w.value; w.focus(); w.setSelectionRange(w.value.length,w.value.length); }
  return true;
}
window.v2jnlFill = jnlFill;
window.v2jnl = function(t){
  var tab=[].slice.call(document.querySelectorAll('.ntab')).find(function(b){return /jnl/.test(b.getAttribute('onclick')||'');});
  showPg('jnl', tab);
  setTimeout(function(){
    var f=document.getElementById('jnl-form'); if(f && f.style.display!=='block') jnlNew();
    jnlFill(t, false);
  }, 400);
};
document.addEventListener('change', function(e){
  if(!e.target || e.target.id!=='jnl-ticker') return;
  var s=jnlResolve(e.target.value); if(!s) return;
  var w=document.getElementById('jnl-why');
  if(w && w.value.trim() && w.value!==w.dataset.auto){ e.target.value=s.ticker; return; } // ne jamais écraser ce que tu as écrit
  jnlFill(s.ticker, true);
});

function renderV2(s){
  var F = (typeof FICHE!=='undefined') ? FICHE[s.ticker] : null;
  var v = verdict(s);
  var chg = (s.chg!=null && Math.abs(s.chg)<50) ? '<span style="color:'+(s.chg>=0?'#7fd1a3':'#f2a29b')+'">'+sgn(s.chg,2)+' aujourd’hui</span>' : '';
  return '<div class="v2">'+
    '<header class="v2-top"><div><div class="v2-kick">'+esc(s.ticker)+' · '+esc(s.place||'')+' · '+esc(s.sector||'')+'</div><h1>'+esc(s.name)+'</h1></div>'+
    '<div class="v2-px"><div>'+M(s,s.price)+'</div><div class="v2-small" style="color:#c7cede">'+chg+'</div></div></header>'+
    moveBanner(s)+
    (dqAll(s)?'<section class="v2-card" style="background:#fbf4e6;border-left:4px solid #a8790f"><b>Donnée à vérifier avant toute décision :</b> '+esc(dqAll(s))+'. <span class="v2-small">Contrôle automatique : la source (Yahoo) peut se tromper ; vérifie sur Zonebourse ou le rapport annuel.</span></section>':'')+
    '<section class="v2-card v2-verdict"><div class="v2-badge" style="background:'+v.c+'">'+v.t+'</div><p>'+v.x+'</p>'+position(s)+'</section>'+
    parcours(s,F)+
    step(1,'Le métier',thesis(s,F))+
    step(2,'Le moat',moat(s,F))+
    step(3,'Les chiffres',quality(s)+figures(s))+
    step(4,'La contre-thèse : pourquoi elle peut perdre 30 %',docLink(s)+ceBlock(s))+
    step(5,'Le prix',feeLine(s)+buyPlan(s)+priceBlock(s)+ratios(s))+
    step(6,'Mes chiffres d’erreur et la sortie',exitBlock(s))+
    decision(s)+technical(s)+sources(s)+
  '</div>';
}

// ---- remplacement de render() ----
if(typeof render==='function'){
  var oldRender = render;
  window.render = render = function(s){
    oldRender(s);
    var fe = document.getElementById('fiche');
    if(!fe) return;
    var old = fe.innerHTML;
    // 20/10/2026 : ancienne analyse retiree (positions 5-8 %, stop loss, RSI : contredisait la methode)
    fe.innerHTML = renderV2(s);
  };
}



// 25/10/2026 : taille des positions selon le profil (cyclique = moitié : 1,25 % puis 2,5 %)
function sizes(s){ var F=(typeof FICHE!=='undefined')?FICHE[s.ticker]:null; var cyc=(F&&F.prof==='cyclique')||s.grid==='cyclique';
  return cyc?{half:1.25, full:2.5, cyc:true}:{half:2.5, full:5, cyc:false}; }
// ---- 20/10/2026 : frais d'achat (grille Bourse Direct du 18/10/2026 ; compte-titres = Trade Republic 1 EUR) ----
// Regle : frais <= 1 % de l'ordre.
function feeInfo(s){
  var pl=s.place||'', cto=/compte-titres/.test(s.sector||'');
  var f=function(m){ return 0; }, nom='', acces='';
  if(cto){ nom='Trade Republic (compte-titres)'; f=function(m){return 1;}; }
  else if(/^(Paris|Amsterdam|Bruxelles)$/.test(pl)){ nom='Euronext'; var ttf=(pl==='Paris'&&/large|mid/.test(s.cap||''))?0.004:0;
    f=function(m){return (m<=500?0.99:m<=1000?1.90:m<=2000?2.90:m<=4400?3.80:m*0.0009)+m*ttf;}; if(ttf) acces=' · taxe sur les transactions financières de 0,4 % incluse (sociétés françaises de plus de 1 Md€, liste officielle de 121 sociétés en 2026 ; achat seulement)'; }
  else if(/^(Francfort|F)$/.test(pl)){ nom='Xetra'; f=function(m){return Math.max(15,m*0.0015);}; }
  else if(/^(Madrid|Lisbonne|SW)$/.test(pl)){ nom=pl==='SW'?'Suisse':pl; f=function(m){return Math.max(18,m*0.002);}; }
  else { nom=({WA:'Varsovie',VI:'Vienne',AT:'Vienne',IR:'Dublin',VS:'Vilnius'})[pl]||pl; acces=' · accès chez Bourse Direct à confirmer'; f=function(m){return Math.max(41.90,m*0.0048);}; }
  var mn=500; while(mn<20000 && f(mn)/mn>0.01) mn+=100;
  return {nom:nom, f500:f(500), p500:f(500)/5, min:mn, acces:acces, ok:f(500)/500<=0.01};
}
function feeLine(s){
  var x=feeInfo(s);
  var comp=(parcoursOn(s)?'<p class="v2-small" style="margin:0 0 8px;padding:8px 10px;border-radius:8px;background:#eef1f6"><b>Avant d’acheter</b> : un concurrent direct (voir la thèse) est-il meilleur et moins cher ? Compare son PER, sa marge et sa croissance ; s’il gagne sur les trois, c’est lui qu’il faut étudier.</p>':'');
  return comp+'<p class="v2-small" style="margin:0 0 8px;padding:8px 10px;border-radius:8px;background:'+(x.ok?'#eef6f1':'#fbf4e6')+'"><b>Frais d’achat ('+x.nom+')</b> : '+fr(x.f500)+' € pour un ordre de 500 € ('+fr(x.p500,1)+' %)'+
    (x.ok?' : sous la règle de 1 %.':' : au-dessus de la règle de 1 %. Ordre minimum pour respecter la règle : <b>'+fr(x.min,0)+' €</b> (regrouper plusieurs mois).')+x.acces+'</p>';
}

// 24/10/2026 : lien vers l'analyse complete (document) quand elle existe
function docLink(s){
  var a=(typeof ANALYSES!=='undefined')?ANALYSES.find(function(x){return x.t===s.ticker;}):null;
  if(!a||!a.lien) return '';
  return '<section class="v2-card" style="border-left:4px solid #24508a"><b>Analyse complète du '+esc(a.date)+'</b> (verdict alors : '+esc(a.verdict||'')+') · <a href="'+a.lien+'" target="_blank" rel="noopener">Lire le document d’analyse</a></section>';
}
// ---- 20/10/2026 : meme ordre pour toutes les fiches = les 6 etapes de la methode ----
function step(n, t, html){
  if(!html) return '';
  return '<div id="v2st'+n+'"><div style="margin:18px 0 6px;font:700 12px/1.2 system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:'+C.mu+'">Étape '+n+' · '+t+'</div>'+html+'</div>';
}
window.v2go = function(n){ var e=document.getElementById('v2st'+n); if(e) e.scrollIntoView({behavior:'smooth',block:'start'}); };
// Parcours (resume + cases) seulement pour les achats possibles
function parcoursOn(s){ return !!(s.qok && s.eh>0 && s.rec==='buy'); }
function parcours(s, F){
  if(!parcoursOn(s)) return '';
  var L=ceList(s.ticker), last=L[0], st=chkState(s), o=chkGet(s.ticker);
  var met = F&&F.why ? F.why : (last&&last.resume&&/^Métier en une phrase/.test(last.resume) ? last.resume.split(/\.\s/)[0].replace(/^Métier en une phrase\s*:\s*/,'')+'.' : '');
  var mo = s.mtype ? 'Avantage : '+s.mtype+(s.mthreat?' · ce qui peut le casser : '+s.mthreat:'') : '';
  var ch = (s.qok?'Qualité 5/5':'Qualité limite')+(s.bg?' · contrôle Baggr du '+s.bg.date+' : '+(s.bg.verdict==='ecart'?'écart':s.bg.verdict==='non verifiable'?'non vérifiable':'concordant'):' · pas encore de deuxième source');
  var ct = last ? 'Contre-expertise du '+last.date+' : '+(CEL[last.concl]?CEL[last.concl][0].toLowerCase():'?')+(last.point?' ('+last.point+')':'') : '';
  var P=palier(s), r=(s.tp>0&&s.dcfm>0)?s.dcfm/s.tp:null;
  var fi=feeInfo(s);
  var px = (P===2?'Sous le palier 2':P===1?'Sous le palier 1':'Pas encore dans la zone (palier 1 : '+M(s,s.eh)+')')+' · frais '+fr(fi.p500,1)+' % sur 500 €'+(fi.ok?'':' (ordre minimum '+fr(fi.min,0)+' €)')+(r?' · valeur du screener = '+fr(r,2)+' × l’objectif des analystes'+(r>1.5?(/analystes/.test(dqAll(s))?' : blocage, contre-expertise requise':' : au-dessus de 1,5, blocage levé par la contre-expertise'):''):'');
  var kp = last&&last.kpi ? last.kpi.filter(function(k){return /ALERTE/.test(k[2]);}).length : null;
  var er = last&&last.kpi ? last.kpi.length+' chiffres suivis dans la contre-expertise, '+kp+' en alerte (2 en alerte = thèse cassée)' : '';
  var rows=[[1,'Le métier en une phrase','metier',met,'J’explique le métier en une phrase, avec mes mots'],
    [2,'Le moat','moat',mo,'J’ai nommé le moat et ce qui pourrait le casser'],
    [3,'Les chiffres','sources',ch,'Deux sources concordent sur les chiffres'],
    [4,'La contre-thèse','contre',ct,'J’ai écrit au moins 3 raisons pour lesquelles elle peut perdre 30 %'],
    [5,'Le prix','calcul',px,'Mon calcul (onglet Analyser) et le screener concordent à 25 % près'],
    [6,'Mes 3 chiffres d’erreur','tort',er,'J’ai écrit mes 3 chiffres d’erreur avec leur seuil']];
  var auto = st.auto.every(function(x){return x[2];});
  return '<section class="v2-card" style="border-left:4px solid '+(st.ok?C.gn:C.or)+'"><div class="v2-head"><h2>Mon parcours en 6 étapes : '+st.done+' / '+st.total+'</h2><span class="v2-small">'+(st.date?'coché le '+st.date+' · valable 90 jours':'cases gardées dans ce navigateur seulement')+'</span></div>'+
    '<p class="v2-small" style="margin:0 0 6px">'+(auto?'Contrôles automatiques OK (qualité et zone d’achat).':'Contrôles automatiques : '+st.auto.map(function(x){return (x[2]?'OK ':'NON ')+x[1].toLowerCase();}).join(' · '))+' Clique sur une étape pour voir le détail.</p>'+
    rows.map(function(x){ var done=!!o[x[2]];
      return '<div style="display:flex;gap:10px;align-items:flex-start;padding:7px 0;border-top:1px solid '+C.line+'">'+
        '<input type="checkbox" '+(done?'checked ':'')+'onchange="v2chk(\''+s.ticker+'\',\''+x[2]+'\',this.checked)" title="'+x[4]+'" style="width:20px;height:20px;flex:none;margin-top:2px">'+
        '<div style="flex:1"><div><b style="cursor:pointer;text-decoration:underline" onclick="v2go('+x[0]+')">'+x[0]+'. '+x[1]+'</b> <span class="v2-small">· '+x[4]+'</span></div>'+
        '<div class="v2-small" style="margin-top:2px;color:'+(x[3]?C.ink:C.or)+'">'+(x[3]?esc(x[3]):'à rédiger')+'</div></div></div>';
    }).join('')+
    '<p class="v2-small" style="margin-top:8px"><b>'+(st.ok?'Parcours complet : l’achat peut être validé.':'Achat bloqué tant qu’une case manque.')+'</b> Méthode détaillée : PDF « Ma méthode d’achat ».</p></section>';
}
// ---- page d'accueil : liste de décision ----
function openTicker(t){
  var i = fil.findIndex(function(x){return x.ticker===t;});
  if(i<0){ fil=[...S]; i = fil.findIndex(function(x){return x.ticker===t;}); }
  if(i>=0){ jump(i); var f=document.getElementById('lc'); if(f) f.scrollIntoView({behavior:'smooth',block:'start'}); }
}
window.v2open = openTicker;
function item(s){
  var gap = s.eh>0 ? pct(s.price,s.eh) : null;
  return '<button class="v2-it" onclick="v2open(\''+s.ticker+'\')"><b>'+esc(s.ticker)+'</b> <span>'+esc(s.name)+'</span>'+
    '<span class="v2-mono">'+fr(s.price)+' €</span>'+
    (gap!=null&&(s.qok||s.near)?'<span class="v2-small">'+(gap<=0?(s.rec==='buy'?(palier(s)===2?'palier 2':'palier 1'):'en zone, bloquée : '+(dqAll(s)?'donnée à vérifier':s.knife?'chute en cours':(s.mscore==null||s.mscore<3)?'moat faible ou non noté':!s.qok?'qualité limite':'croissance irrégulière')):'doit baisser de '+fr(gap,0)+' %')+'</span>':'<span class="v2-small">'+esc((s.qwhy||'').split(',')[0])+'</span>')+
    (s.mscore!=null?'<span class="v2-small">moat '+s.mscore+'/5</span>':'')+(window.v2held&&window.v2held[s.ticker]?'<span class="v2-small" style="color:#24508a">· en portefeuille'+(palier(s)===2?' : complément possible':' : complément sous '+fr(z2(s))+' €')+'</span>':'')+'</button>';
}
function buildHome(){
  var pg = document.getElementById('pg-sc'); if(!pg) return;
  var box = document.getElementById('v2-home');
  if(!box){ box=document.createElement('div'); box.id='v2-home'; pg.insertBefore(box, pg.firstChild); }
  var buy=[], watch=[], out=[];
  // 20/10/2026 : une ligne deja detenue n'est plus un « achat possible », sauf complement sous le palier 2
  var held={}; ['pea_ptf_val','pea_ptf_p2'].forEach(function(k){ try{ JSON.parse(localStorage.getItem(k)||'[]').forEach(function(p){ if(p&&p.ticker&&p.qty>0) held[p.ticker]=1; }); }catch(e){} });
  try{ if(typeof PTF!=='undefined') PTF.forEach(function(p){ if(p&&p.ticker&&p.qty>0) held[p.ticker]=1; }); }catch(e){}
  window.v2held = held;
  S.forEach(function(s){ if(!s||!s.ticker||!(s.price>0)) return; var g=group(s); if(g==='buy' && held[s.ticker] && palier(s)<2) g='watch'; (g==='buy'?buy:g==='watch'?watch:out).push(s); });
  // 19/10/2026 : une donnee a verifier passe apres (sinon les valeurs aux chiffres faux arrivent en tete)
  var byGap = function(a,b){ return ((dqAll(a)?10:0)+(a.eh>0?a.price/a.eh:9))-((dqAll(b)?10:0)+(b.eh>0?b.price/b.eh:9)); };
  buy.sort(byGap); watch.sort(byGap); out.sort(function(a,b){return (a.name||'').localeCompare(b.name||'');});
  box.innerHTML = '<div class="v2-home"><div class="v2-hgrp" style="border-top:4px solid '+C.gn+'"><h3>Achat possible <span>'+buy.length+'</span></h3><p class="v2-small">Qualité OK · cours en zone · moat ≥ 3 · croissance régulière · pas de chute</p>'+(buy.map(item).join('')||'<p class="v2-small">Aucune aujourd’hui → versement du mois sur l’ETF Monde.</p>')+'</div>'+
    '<div class="v2-hgrp" style="border-top:4px solid '+C.or+'"><h3>À surveiller <span>'+watch.length+'</span></h3><p class="v2-small">Qualité OK mais trop chère, en chute, ou limite · <b>les 20 plus proches de leur palier 1</b></p>'+watch.slice(0,20).map(item).join('')+
      (watch.length>20?'<details><summary class="v2-small">Voir les '+(watch.length-20)+' autres (plus loin de leur palier)</summary>'+watch.slice(20).map(item).join('')+'</details>':'')+'</div>'+
    '<div class="v2-hgrp" style="border-top:4px solid #9aa1ae"><h3>Hors qualité <span>'+out.length+'</span></h3><details><summary class="v2-small">Afficher la liste</summary>'+out.map(item).join('')+'</details></div></div>';
}
window.v2buildHome = buildHome;

// ---- légende de droite : 3 groupes au lieu des notes A-D ----
function legend(){
  document.querySelectorAll('#pg-sc .sh').forEach(function(h){
    if(h.textContent.trim()==='Notation'){
      var sc=h.parentElement;
      sc.innerHTML='<div class="sh">Lecture</div><div class="v2-leg"><p><b style="color:'+C.gn+'">Achat possible</b> : toutes les règles sont remplies.</p><p><b style="color:'+C.or+'">À surveiller</b> : bonne entreprise, mauvais moment ou un critère limite.</p><p><b style="color:#6b7487">Hors qualité</b> : la méthode n’achète pas.</p><p class="v2-small">L’ancienne note A-D reste dans « Ancienne analyse », elle ne sert plus à décider.</p></div>';
    }
  });
}

function init(){
  try{ buildHome(); legend(); }catch(e){ console.error('v2 home', e); }
  try{ if(typeof paused!=='undefined' && !paused && typeof tPause==='function') tPause(); }catch(e){}
  try{ var mb=document.getElementById('macro-banner'); if(mb) mb.style.setProperty('display','none','important'); }catch(e){}
}
if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', init); else init();
window.renderV2 = renderV2;
})();

// ═══ 06/10/2026 : barre de filtres, compteurs et file alignés sur la méthode ═══
(function(){
'use strict';
function grp(s){ if(s.qok && s.rec==='buy' && !(window.v2held&&window.v2held[s.ticker]&&window.v2palier&&window.v2palier(s)<2)) return 'buy'; if(s.qok||s.near) return 'watch'; return 'out'; }
function mine(){
  var list=(typeof PTF!=='undefined'&&(PTF.length||(window._ptfProfile&&window._ptfProfile!=='val')))?PTF:null;
  if(!list){ try{ list=JSON.parse(localStorage.getItem('pea_ptf_val')||'[]'); }catch(e){ list=[]; } }
  return list.map(function(p){return p&&p.ticker;});
}
var DOT={buy:'#1d6b45',watch:'#a8790f',out:'#9aa1ae'}, LAB={buy:'achat',watch:'surveiller',out:'hors'};
var FILTERS=[['sel','Achat + à surveiller'],['buy','Achat possible'],['watch','À surveiller'],['mine','Mes lignes'],['out','Hors qualité'],['all','Toutes les fiches'],['large','Large'],['mid','Mid'],['small','Small']];
function apply(key){
  var m=mine();
  fil = S.filter(function(s){
    if(!s||!s.ticker) return false;
    if(key==='all') return true;
    if(key==='sel') return grp(s)!=='out' || m.indexOf(s.ticker)>=0;
    if(key==='buy'||key==='watch'||key==='out') return grp(s)===key;
    if(key==='mine') return m.indexOf(s.ticker)>=0;
    return s.cap===key;
  });
  idx=0; if(typeof cycles!=='undefined') cycles=0;
  document.querySelectorAll('.h-ctrl .fb').forEach(function(b){ b.classList.toggle('active', b.getAttribute('data-f')===key); });
  buildQ(); if(fil.length) show(0);
}
window.v2filt = apply;
// plus de défilement automatique : on choisit l'action qu'on veut voir
try{ window.startR = startR = function(){}; }catch(e){}
function bar(){
  var c=document.querySelector('.h-ctrl'); if(!c) return;
  c.innerHTML = FILTERS.map(function(f){ return '<button class="fb'+(f[0]==='sel'?' active':'')+'" data-f="'+f[0]+'" onclick="v2filt(\''+f[0]+'\')">'+f[1]+'</button>'; }).join('')+
    '<span style="margin-left:auto;font-size:10px;color:#9aa1ae">Cliquer un filtre met à jour la file à droite et affiche la 1re fiche</span>';
  var pw=document.querySelector('.prog-wrap'); if(pw) pw.style.display='none';
}
window.buildQ = buildQ = function(){
  var l=document.getElementById('ql'); if(!l) return;
  l.innerHTML = fil.map(function(s,i){ var g=grp(s);
    return '<div class="qi'+(i===idx?' active':'')+'" onclick="jump('+i+')"><span class="qi-n">'+(i+1)+'</span><span class="qi-t">'+s.ticker+'</span><span class="qi-nm">'+s.name+'</span><span title="'+LAB[g]+'" style="width:10px;height:10px;border-radius:50%;background:'+DOT[g]+';flex:none"></span></div>'; }).join('');
  var q=document.getElementById('qcnt'); if(q) q.textContent=fil.length+' val.';
  var a=l.querySelector('.active'); if(a) a.scrollIntoView({block:'nearest'});
};
window.updHK = updHK = function(){
  var set=function(id,v,lab){ var e=document.getElementById(id); if(!e) return; e.textContent=v; var l=e.parentElement&&e.parentElement.querySelector('.hk-l'); if(l&&lab) l.textContent=lab; };
  var n={buy:0,watch:0,out:0}; S.forEach(function(s){ if(s&&s.ticker) n[grp(s)]++; });
  set('hkT', S.length, 'Fiches');
  // 19/10/2026 : nombre total de valeurs analysees (fiches + radar elargi)
  if(!window._v2nAn){ window._v2nAn=1; Promise.all(['candidats_resultats.json','candidats_cto_resultats.json'].map(function(f){ return fetch(f).then(function(r){return r.json();}).catch(function(){return {};}); })).then(function(L){
    var t=0; L.forEach(function(o){ Object.keys(o.listes||{}).forEach(function(k){ var x=o.listes[k]; t+=(x.total||0)-(x.hors_pea_ou_doublon||0)-(x.sans_donnees||0); }); });
    window._v2nAn=t; set('hkT', (S.length+t).toLocaleString('fr-FR'), 'Analysées'); }); }
  else if(window._v2nAn>1) set('hkT', (S.length+window._v2nAn).toLocaleString('fr-FR'), 'Analysées');
  set('hkD', n.buy, 'Achat possible');
  set('hkAB', n.watch, 'À surveiller');
  set('hkZ', mine().filter(function(t){return S.some(function(s){return s.ticker===t;});}).length, 'Mes lignes');
  var src=(document.querySelector('script[src*="data.js?v="]')||{}).src||'', ts=(src.match(/v=(\d{9,})/)||[])[1];
  set('hkP', ts? new Date(ts*1000).toLocaleDateString('fr-FR',{day:'2-digit',month:'2-digit'}) : '—', 'Mise à jour');
};
function go(){ try{ bar(); updHK(); buildQ(); try{ if(typeof S!=='undefined'&&S.length) apply('sel'); }catch(e2){} }catch(e){ console.error('v2 bar', e); } }
if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', go); else go();
})();

// ═══ 06/10/2026 : trois portefeuilles (noms gardés dans le navigateur) ═══
(function(){
'use strict';
var DEF={val:'Moi',p2:'Portefeuille 2',p3:'Portefeuille 3'};
// les prénoms ne sont jamais écrits dans le code public : ils restent dans ton navigateur
var NAMES=(function(){ try{ return Object.assign({},DEF,JSON.parse(localStorage.getItem('v2_prof_names')||'{}')); }catch(e){ return DEF; } })();
window.v2profNames=function(){ return NAMES; };
window.v2rename=function(){
  var box=document.getElementById('v2-rename'); if(!box) return;
  box.style.display = box.style.display==='flex'?'none':'flex';
};
window.v2saveNames=function(){
  ['val','p2','p3'].forEach(function(p){ var e=document.getElementById('v2-n-'+p); if(e&&e.value.trim()) NAMES[p]=e.value.trim(); });
  try{ localStorage.setItem('v2_prof_names', JSON.stringify(NAMES)); }catch(e){}
  document.querySelectorAll('.v2-prof button[data-p]').forEach(function(b){ b.textContent=NAMES[b.getAttribute('data-p')]; });
  ['val','p2','p3'].forEach(function(p){ var b=document.getElementById('prof-'+p); if(b) b.textContent='💼 '+NAMES[p]; });
  document.getElementById('v2-rename').style.display='none';
};
function paint(){
  var cur=window._ptfProfile||'val';
  document.querySelectorAll('.v2-prof button').forEach(function(b){
    var on=b.getAttribute('data-p')===cur;
    b.style.background=on?'#0e1c33':'#fff'; b.style.color=on?'#f0d080':'#1a2233'; b.style.fontWeight=on?'700':'500';
  });
}
function bar(){
  var pg=document.getElementById('pg-ptf'); if(!pg||document.querySelector('.v2-prof')) return;
  var d=document.createElement('div'); d.className='v2-prof';
  d.style.cssText='display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:14px 18px 4px;font-family:IBM Plex Sans,system-ui,sans-serif';
  d.innerHTML='<span style="font-size:13px;color:#5a6275;margin-right:4px">Portefeuille :</span>'+
    ['val','p2','p3'].map(function(p){return '<button data-p="'+p+'" style="min-height:44px;padding:8px 18px;border:1px solid #ddd8cb;border-radius:999px;cursor:pointer;font-size:14px">'+NAMES[p]+'</button>';}).join('')+
    '<button onclick="v2rename()" style="min-height:36px;padding:6px 12px;border:0;background:none;color:#1d4f91;cursor:pointer;font-size:13px">Renommer</button>'+
    '<span style="font-size:12px;color:#5a6275;margin-left:8px">Chaque portefeuille a sa routine, ses poids et ses signaux. Les noms et positions restent dans ton navigateur, jamais en ligne.</span>'+
    '<div id="v2-rename" style="display:none;flex-wrap:wrap;gap:8px;width:100%;align-items:center">'+['val','p2','p3'].map(function(p){return '<label class="v2-small">'+DEF[p]+' <input id="v2-n-'+p+'" value="'+NAMES[p]+'" style="padding:6px;border:1px solid #ddd8cb;border-radius:6px"></label>';}).join('')+'<button onclick="v2saveNames()" style="min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid #0e1c33;background:#0e1c33;color:#fff;cursor:pointer">Enregistrer</button></div>';
  pg.insertBefore(d, pg.firstChild);
  d.querySelectorAll('button').forEach(function(b){ b.onclick=function(){ ptfSwitchProfile(b.getAttribute('data-p')); }; });
  paint();
}
if(typeof ptfSwitchProfile==='function'){
  var orig=ptfSwitchProfile;
  window.ptfSwitchProfile = ptfSwitchProfile = function(name,btn){
    orig(name,btn); paint();
    try{ if(typeof updHK==='function') updHK(); }catch(e){}
  };
}
if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', bar); else bar();
window.v2profName=function(){ return NAMES[window._ptfProfile||'val']; };
})();

// ═══ 06/10/2026 : onglets nettoyés, alertes de la méthode, mode d'emploi ═══
(function(){
'use strict';
function fr(n,d){ if(n==null||isNaN(n)) return '—'; return Number(n).toLocaleString('fr-FR',{maximumFractionDigits:d==null?2:d}); }
function esc(t){ return String(t==null?'':t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function mineList(){ return (typeof PTF!=='undefined')?PTF:[]; }
// 19/10/2026 : vue d'ensemble de TOUS les portefeuilles du navigateur (PEA + compte-titres)
function overview(){ try{ return overview_(); }catch(e){ console.error('vue d ensemble', e); return ''; } }
function overview_(){
  var C={gn:'#1d6b45', rd:'#a8322b', ink:'#0e1c33'};
  var names=(window.v2profNames?v2profNames():{val:'Moi',p2:'Portefeuille 2',p3:'Portefeuille 3'});
  var lines=[], tot=0;
  ['val','p2','p3'].forEach(function(pf){
    var L=[]; try{ L=JSON.parse(localStorage.getItem('pea_ptf_'+pf)||'[]'); }catch(e){}
    L.forEach(function(p){
      var st=S.find(function(x){return x&&x.ticker===p.ticker;}), et=(typeof ETF!=='undefined')?ETF.find(function(x){return x&&x.ticker===p.ticker;}):null;
      var px=st?st.price:(et&&et.price?et.price:p.pru), v=px*p.qty; if(!(v>0)) return;
      lines.push({t:p.ticker, pf:names[pf]||pf, v:v, etf:!!et, cur:st?(st.qcur||'EUR'):(et?(/S&P|Etats-Unis/i.test(et.name+' '+(et.type||''))?'USD':'mixte'):'EUR'), sec:st?String(st.sector||'').replace(' (compte-titres)',''):(et?'ETF':'?')});
      tot+=v;
    });
  });
  if(!lines.length) return '';
  var pc=function(x){return fr(x/tot*100,0)+' %';};
  var etf=lines.filter(function(l){return l.etf;}).reduce(function(a,l){return a+l.v;},0), act=tot-etf;
  var nAct=lines.filter(function(l){return !l.etf;}).length;
  var by=function(k){ var m={}; lines.forEach(function(l){ if(l.etf) return; m[l[k]]=(m[l[k]]||0)+l.v; }); return Object.keys(m).sort(function(a,b){return m[b]-m[a];}).slice(0,4).map(function(x){return esc(x)+' '+pc(m[x]);}).join(' · '); };
  var big=lines.filter(function(l){return !l.etf;}).sort(function(a,b){return b.v-a.v;})[0];
  var ok=function(c){return '<b style="color:'+(c?C.gn:C.rd)+'">'+(c?'oui':'non')+'</b>';};
  return '<section class="v2-card" style="border-left:4px solid '+C.ink+'"><div class="v2-head"><h2>Vue d’ensemble</h2><span class="v2-small">tous tes portefeuilles de ce navigateur · '+fr(tot,0)+' €</span></div>'+
    '<p>ETF '+pc(etf)+' · actions en direct '+pc(act)+' — règle « 20 % maximum en direct » : '+ok(act/tot<=0.2)+'</p>'+
    '<p>Lignes : '+lines.length+' (dont '+nAct+' actions) — règle « 13 à 15 lignes maximum » : '+ok(lines.length<=15)+'</p>'+
    (big?'<p>Plus grosse action : <b>'+esc(big.t)+'</b>, '+pc(big.v)+' du total</p>':'')+
    '<p class="v2-small">Actions par secteur : '+by('sec')+'<br>Actions par devise : '+by('cur')+'. Les ETF Monde sont eux-mêmes à environ 70 % en dollars : ton exposition réelle au dollar est plus forte que ce tableau.</p></section>';
}
function card(title, sub, rows, col){
  return '<section class="v2-card" style="border-left:4px solid '+col+'"><div class="v2-head"><h2>'+title+' <span class="v2-mono" style="font-size:14px;color:#5a6275">'+rows.length+'</span></h2><span class="v2-small">'+sub+'</span></div>'+
    (rows.length?rows.join(''):'<p class="v2-small">Rien à signaler.</p>')+'</section>';
}
function row(s, txt, isNew){
  return '<button class="v2-it" onclick="v2goFiche(\''+s.ticker+'\')"><b>'+esc(s.ticker)+'</b> <span>'+esc(s.name)+'</span><span class="v2-mono">'+fr(s.price)+' €</span><span class="v2-small">'+txt+'</span>'+(isNew?'<span class="v2-pill" style="background:#1d6b45;color:#fff">NOUVEAU</span>':'')+'</button>';
}
window.v2goFiche=function(t){
  var tab=[].slice.call(document.querySelectorAll('.ntab')).find(function(b){return /'sc'/.test(b.getAttribute('onclick')||'');});
  showPg('sc', tab); setTimeout(function(){ if(window.v2open) v2open(t); }, 200);
};
function alerts(){
  var box=document.getElementById('pg-al'); if(!box) return;
  var seen={}; try{ seen=JSON.parse(localStorage.getItem('v2_al_seen')||'{}'); }catch(e){}
  var now={}, held={}, tot=0;
  mineList().forEach(function(p){ var s=S.find(function(x){return x.ticker===p.ticker;}); held[p.ticker]=p; if(s) tot+=s.price*p.qty;
    else { var e=(typeof ETF!=='undefined')?ETF.find(function(x){return x&&x.ticker===p.ticker;}):null; tot+=(e&&e.price?e.price:p.pru)*p.qty; } });
  var zone=[], out=[], review=[], high=[], big=[], ce=[], moves=[], thes=[];
  S.forEach(function(s){
    if(!s||!s.ticker||!(s.price>0)) return;
    if(s.qok && s.eh>0 && s.price<=s.eh){ now[s.ticker]=1; zone.push(row(s, (s.rec==='buy'?'achat possible':'en zone mais '+(s.knife?'chute en cours':(s.mscore==null||s.mscore<3)?'moat faible':'croissance irrégulière'))+' · '+(window.v2palier(s)===2?'<b>palier 2</b> (sous '+fr(window.v2z2(s))+' €)':'palier 1 · palier 2 sous '+fr(window.v2z2(s))+' €'), !seen[s.ticker])); }
    if(s.chg5!=null && Math.abs(s.chg5)>=10 && (held[s.ticker]||s.qok||s.near)) moves.push(row(s, (held[s.ticker]?'<b>ma ligne</b> · ':'')+(s.chg5>0?'+':'')+String(s.chg5).replace('.',',')+' % en 5 séances'+(s.news5?' · '+esc(String(s.news5).split(' ;; ')[0].split('|')[0]):'')));
    var p=held[s.ticker]; if(!p) return;
    if(!s.qok && !s.near) out.push(row(s,'hors qualité : '+esc(s.qwhy||'')+' → ne pas renforcer ; vente seulement si le seuil de sortie le dit (cash sous 60 % deux ans) ou si la thèse est cassée'));
    if(s.stop>0 && s.price<s.stop && (s.qok||s.near)) review.push(row(s,'sous le seuil de revue ('+fr(s.stop)+' €) → contre-expertise obligatoire'));
    // 19/10/2026 : aussi pour les lignes hors qualite (pas de scenario optimiste) :
    // valeur centrale + 30 %. Regle : vendre la moitie, une fois, jamais tout.
    // 21/10/2026 : vente a DEUX cles = cours au-dessus de la valeur optimiste ET de
    // l'objectif moyen des analystes (le modele plafonne la croissance et sous-evalue
    // les entreprises exceptionnelles : ASML, Hermes). Une ligne d'une action ne se coupe pas.
    var hv_=s.vopt>0?s.vopt:0, hi_=sellKey(s);
    if(hi_>0 && s.price>hi_){ var half_=Math.floor((p.qty||0)/2);
      high.push(row(s,'au-dessus de '+fr(hi_)+' €'+(hv_>0?' (scénario optimiste '+fr(hv_)+' €'+(s.tp>0?', objectif des analystes '+fr(s.tp)+' € plafonné à 1,5 fois':'')+')':' (objectif des analystes)')+(half_>=1?' → vendre la moitié ('+half_+' action'+(half_>1?'s':'')+'), une fois, jamais tout':' → ligne d’une seule action : pas de vente partielle possible, on garde'))); }
    var w=tot>0?s.price*p.qty/tot*100:0; if(w>10) big.push(row(s,'pèse '+fr(w,1)+' % (plafond 10 %) → ne pas renforcer'));
    var L=window.v2ceList?v2ceList(s.ticker):[], age=L[0]?Math.round((Date.now()-new Date(L[0].date).getTime())/864e5):null;
    if(age==null||age>90) ce.push(row(s, age==null?'jamais de contre-expertise':'dernière contre-expertise il y a '+age+' jours'));
    // 20/10/2026 : these et chiffres d'erreur (tableau de bord de la derniere contre-expertise)
    if(L[0]){ var na=(L[0].kpi||[]).filter(function(k){return /ALERTE/.test(k[2]||'');}).length;
      if(L[0].concl==='cassee') thes.push(row(s,'thèse cassée ('+esc(L[0].date)+') : '+esc(L[0].point||'')+' → vendre'));
      else if(na>=2) thes.push(row(s,na+' chiffres d’erreur en alerte : la règle dit thèse cassée → contre-expertise et vente'));
      else if(L[0].concl==='fragilisee') thes.push(row(s,'thèse fragilisée ('+esc(L[0].date)+') : '+esc(L[0].point||'')+' → ne pas renforcer'+(na?' · '+na+' chiffre en alerte':'')));
      else if(na===1) thes.push(row(s,'1 chiffre d’erreur en alerte : à surveiller, pas encore cassée'));
    }
  });
  try{ localStorage.setItem('v2_al_seen', JSON.stringify(now)); }catch(e){}
  var who=window.v2profName?v2profName():'Moi';
  box.innerHTML='<div class="v2" style="max-width:1100px;margin:0 auto">'+
    '<header class="v2-top"><div><div class="v2-kick">Alertes · règles de la méthode</div><h1>Ce qui demande ton attention</h1></div><div class="v2-small" style="color:#c7cede">Portefeuille : '+esc(who)+'</div></header>'+
    overview()+
    card('Mouvements de plus de 10 % en 5 séances','mes lignes et les valeurs de qualité · ouvrir la fiche pour les actualités',moves,'#24508a')+
    card('Mes lignes : thèse et chiffres d’erreur','mis à jour à chaque contre-expertise · 2 chiffres en alerte = thèse cassée',thes,'#a8322b')+
    card('Mes lignes hors qualité','vente si la prochaine publication confirme',out,'#a8322b')+
    card('Mes lignes sous le seuil de revue','contre-expertise obligatoire, pas de vente automatique',review,'#a8322b')+
    card('Valeurs de qualité en zone d’achat','« NOUVEAU » = entrée en zone depuis ta dernière visite',zone,'#1d6b45')+
    card('Mes lignes trop grosses','plafond 10 % par action',big,'#a8790f')+
    card('Mes lignes trop chères','au-dessus de l’optimiste ET des analystes · vendre la moitié, une fois · le reste suit la thèse',high,'#a8790f')+
    card('Contre-expertises à faire','lignes détenues sans contre-expertise de moins de 3 mois',ce,'#6b7487')+
  '</div>';
}
window.v2alerts=alerts;
function guide(){
  var g=document.getElementById('pg-guide'); if(!g) return;
  g.innerHTML='<div class="v2" style="max-width:980px;margin:0 auto">'+
  '<header class="v2-top"><div><div class="v2-kick">Mode d’emploi · méthode qualité à prix raisonnable</div><h1>Comment je décide</h1></div></header>'+
  '<section class="v2-card"><h2>1. La règle d’or</h2><p>J’achète des entreprises <b>excellentes</b>, seulement quand leur prix est <b>raisonnable</b>, et je les garde tant qu’elles restent excellentes. Je ne vends <b>jamais</b> sur le prix seul.</p></section>'+
  '<section class="v2-card"><h2>2. Le filtre qualité (médianes sur 4 ans)</h2><p>Rentabilité du capital hors écarts d’acquisition ≥ 15 % · rentabilité du capital total ≥ 12 % · bénéfice transformé en cash ≥ 80 % · dette nette ≤ 2,5 × EBITDA · croissance ≥ 3 %/an (chiffres officiels quand ils existent). Plus : moat ≥ 3/5 et chiffre d’affaires en hausse au moins 2 ans sur 3 pour pouvoir acheter. Banques, assurances et foncières : grilles dédiées (point 7).</p></section>'+
  '<section class="v2-card"><h2>3. Le prix</h2><p>Trois scénarios (pessimiste, central, optimiste). Deux paliers d’achat sous la valeur centrale, selon l’incertitude : <b>palier 1</b> (décote 10-20 % / 15-25 % / 20-30 %) → demi-position ; <b>palier 2</b> (décote 20 / 30 / 40 %, le niveau « 5 étoiles » de Morningstar) → position complète. On apprend à acheter en deux fois. « Ce que le cours suppose » compare la croissance que le marché paie à la croissance réelle. Croissance utilisée : celle annoncée par l’entreprise ; au-delà de 12 %/an, on n’en retient que la moitié (plafond 20 %), et seulement si la rentabilité du capital dépasse 20 % et le moat vaut au moins 4.</p></section>'+
  '<section class="v2-card"><h2>4. Avant d’acheter</h2><p>Une <b>contre-expertise</b> de moins de 3 mois : thèse intacte → palier 1 : demi-position (2,5 %), palier 2 : position complète (5 %) ; pour une cyclique, tailles divisées par deux (1,25 % puis 2,5 %) ; fragilisée → on descend d’un palier (rien au palier 1, demi-position au palier 2) ; cassée → non. Puis je note la décision dans le <b>journal</b> (bouton en bas de chaque fiche).</p></section>'+
  '<section class="v2-card"><h2>5. La routine du mois (1er dimanche, 15 min)</h2><p>1. Versement. 2. Onglet portefeuille : une ligne « REVOIR » deux publications de suite → je vends. 3. Une action « achat possible » avec contre-expertise favorable et ligne &lt; 10 % → j’achète ; sinon le versement va sur l’ETF Monde. 4. Une ligne dans le journal. Le reste du mois : aucune décision.</p></section>'+
  '<section class="v2-card"><h2>6. Garde-fous</h2><p>Maximum 10 % par action · 13 à 15 lignes · seuil de revue = scénario pessimiste − 10 % (contre-expertise obligatoire, pas de vente automatique) · aucune exception, aucun stop : seules les règles de vente décident · <b>actions ≤ 30 % du PEA</b> (le reste en ETF) : tant que c’est au-dessus, tout l’argent neuf va à l’ETF ; l’argent d’une vente faite selon les règles peut racheter une action seulement au palier 2, sinon il va à l’ETF · plafond revu au bilan d’octobre 2027.</p></section>'+
  '<section class="v2-card"><h2>6 bis. Vendre : deux règles, et rien d’autre</h2><p><b>La qualité</b> : conversion du bénéfice en cash ≥ 80 % garder ; 60-80 % garder sans renforcer ; sous 60 % deux ans de suite → contre-expertise, et elle seule décide. Si la chute vient d’un paiement exceptionnel chiffré par l’entreprise elle-même, la contre-expertise l’écrit et on garde ; sinon on vend tout. <b>Le prix</b> : quand le cours dépasse <b>à la fois</b> le scénario optimiste du screener <b>et</b> l’objectif moyen des analystes, on vend la moitié, une seule fois (depuis le 21/10/2026 : le screener plafonne la croissance et sous-évalue les entreprises exceptionnelles comme ASML ou Hermès ; la deuxième clé évite de les vendre trop tôt). Une ligne d’une seule action ne se coupe pas. Les deux questions sont indépendantes. <b>Cas d’école, octobre 2026 — Coca-Cola</b> : cash faussé par le paiement de fairlife (qualité intacte, on garde) mais cours au-dessus de l’optimiste (on vend la moitié). Le prix d’achat n’entre jamais dans la décision.</p></section>'+
  '<section class="v2-card"><h2>7. Banques, assurances, foncières</h2><p>Grilles dédiées. <b>Banque / assurance</b> : rentabilité des fonds propres ≥ 10 % (pire année ≥ 6 %), aucune perte sur 4 ans, actif net par action en hausse ≥ 2 %/an ; valeur = actif net × rentabilité, rendement exigé 10 %/an. <b>Foncière</b> : dette nette / actifs ≤ 45 %, intérêts couverts 2,5 fois, loyers stables ou en hausse ; valeur ≈ actif net comptable. La solvabilité (CET1, Solvabilité II) et l’actif net réévalué officiel se vérifient dans la contre-expertise.</p></section>'+
  '<section class="v2-card"><h2>8. Deux sources de chiffres</h2><p>Yahoo (mise à jour automatique) est recoupé chaque lundi avec les <b>comptes officiels</b> déposés au format européen (filings.xbrl.org). Écart de plus de 5 % sur le chiffre d’affaires ou le résultat net → « donnée à vérifier » : l’achat est bloqué tant que ce n’est pas éclairci.</p></section>'+
  '<section class="v2-card"><h2>9. Ce que dit le test sur le passé</h2><div id="v2-bt" class="v2-small">Chargement…</div></section>'+
  '<section class="v2-card v2-small"><p>Les notes A-D, le « triptyque », les scores Large/Mid et l’ancien radar d’alertes ne servent plus à décider. Le screener informe ; c’est toi qui décides, avec ces règles écrites.</p></section>'+
  '</div>';
  try{
    fetch('backtest_paliers.json?d='+Date.now()).then(function(r){return r.ok?r.json():null;}).then(function(b){
      var el=document.getElementById('v2-bt'); if(!el||!b) return;
      var row=function(l,o){ return o?'<tr><td>'+l+'</td><td class="v2-mono">'+fr(o.rendement_annuel,1)+' %/an</td><td class="v2-mono">'+fr(o.valeur,0)+'</td></tr>':''; };
      el.innerHTML='<p>Versement de 1 000 par mois du '+b.periode[0]+' au '+b.periode[1]+' ('+b.mois+' mois), mêmes règles que le screener.</p>'+
        '<table class="v2-tab"><thead><tr><th>Stratégie</th><th>Rendement</th><th>Valeur finale</th></tr></thead><tbody>'+
        row('ETF Monde seul',b.A_etf_seul)+row('Europe (Stoxx 600)',b.D_europe_stoxx600)+row('Les actions de qualité, achetées chaque mois sans regarder le prix',b.B_actions_chaque_mois)+row('<b>Les deux paliers + ETF Monde</b> (méthode)',b.C_paliers_plus_etf)+'</tbody></table>'+
        '<p>'+b.achats.total+' achats aux paliers ('+b.achats.palier1+' au palier 1, '+b.achats.palier2+' au palier 2) ; '+b.achats.battent_etf+' ont fait mieux que l’ETF sur la même période.</p>'+
        '<p><b>Limites :</b> '+(b.biais||[]).join(' · ')+'. Test refait automatiquement chaque mois.</p>';
    }).catch(function(){});
  }catch(e){}
}
function tabs(){
  document.querySelectorAll('.ntab').forEach(function(b){
    var o=b.getAttribute('onclick')||'';
    if(/'acad'|'bt'|'labo'/.test(o)) b.style.display='none'; // 19/10/2026 : labo psycho remplace par le Journal et la routine du mois
  });
}
if(typeof showPg==='function'){
  var orig=showPg;
  window.showPg = showPg = function(pg,btn){ orig(pg,btn); if(pg==='al') try{ alerts(); }catch(e){ console.error(e); } };
}
function go(){ try{ tabs(); guide(); }catch(e){ console.error('v2 tabs', e); } }
if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', go); else go();
})();

// ═══ 07/10/2026 : sauvegarde / restauration de tes données (portefeuilles, journal, contre-expertises) ═══
(function(){
'use strict';
window.v2backup = function(){
  var out = {app:'VAL.PEA', version:1, date:new Date().toISOString(), data:{}};
  for(var i=0;i<localStorage.length;i++){
    var k=localStorage.key(i);
    if(!k || k==='_ant_key') continue; // jamais la clé API dans une sauvegarde
    out.data[k]=localStorage.getItem(k);
  }
  var blob=new Blob([JSON.stringify(out,null,1)],{type:'application/json'});
  var a=document.createElement('a'); a.href=URL.createObjectURL(blob);
  a.download='valpea-sauvegarde-'+new Date().toISOString().slice(0,10)+'.json';
  document.body.appendChild(a); a.click(); setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 1000);
  try{ localStorage.setItem('v2_last_backup', new Date().toISOString()); }catch(e){}
  var s=document.getElementById('v2-bk-st'); if(s) s.textContent='Sauvegardé aujourd’hui.';
};
window.v2restore = function(input){
  var f=input.files&&input.files[0]; if(!f) return;
  var r=new FileReader();
  r.onload=function(){
    var s=document.getElementById('v2-bk-st');
    try{
      var o=JSON.parse(r.result);
      if(!o||o.app!=='VAL.PEA'||!o.data) throw new Error('fichier non reconnu');
      Object.keys(o.data).forEach(function(k){ if(k!=='_ant_key') localStorage.setItem(k,o.data[k]); });
      if(s) s.textContent='Restauré ('+Object.keys(o.data).length+' éléments du '+String(o.date).slice(0,10)+'). Rechargement…';
      setTimeout(function(){ location.reload(); }, 900);
    }catch(e){ if(s) s.textContent='Échec : '+e.message; }
  };
  r.readAsText(f);
};
function box(){
  var pg=document.getElementById('pg-ptf'); if(!pg||document.getElementById('v2-bk')) return;
  var last=null; try{ last=localStorage.getItem('v2_last_backup'); }catch(e){}
  var age=last?Math.round((Date.now()-new Date(last).getTime())/864e5):null;
  var d=document.createElement('div'); d.id='v2-bk';
  d.style.cssText='display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:4px 18px 8px;font-family:IBM Plex Sans,system-ui,sans-serif;font-size:13px';
  d.innerHTML='<button onclick="v2backup()" style="min-height:40px;padding:6px 14px;border-radius:999px;border:1px solid #0e1c33;background:#fff;cursor:pointer">Sauvegarder mes données (fichier)</button>'+
    '<label style="min-height:40px;padding:9px 14px;border-radius:999px;border:1px solid #ddd8cb;background:#fff;cursor:pointer;box-sizing:border-box">Restaurer depuis un fichier<input type="file" accept=".json,application/json" onchange="v2restore(this)" style="display:none"></label>'+
    '<span id="v2-bk-st" style="color:'+(age==null||age>30?'#a8322b':'#5a6275')+'">'+(age==null?'Jamais sauvegardé : tes portefeuilles n’existent que dans ce navigateur.':'Dernière sauvegarde il y a '+age+' jour(s).')+'</span>';
  var bar=document.querySelector('.v2-prof'); if(bar&&bar.nextSibling) pg.insertBefore(d, bar.nextSibling); else pg.insertBefore(d, pg.firstChild);
}
// 09/10/2026 : rappel de sauvegarde dès qu'une donnée personnelle change
// (portefeuilles, historique, journal, convictions, thèses, contre-expertises).
var DIRTY=/^(pea_ptf_(?!.*_ver$)|pea_hist_|valpea_journal|valpea_convictions|these_|v2_ce_|v2_prof_names|pea_notes|ptf_positions)/;
try{
  var _set=Storage.prototype.setItem;
  Storage.prototype.setItem=function(k,v){
    var old=null; try{ old=this.getItem(k); }catch(e){}
    _set.apply(this,arguments);
    if(this===window.localStorage && DIRTY.test(k) && old!==String(v)){
      try{ _set.call(this,'v2_dirty',new Date().toISOString()); }catch(e){}
      setTimeout(banner,50);
    }
  };
}catch(e){}
function banner(){
  var d=null,b=null; try{ d=localStorage.getItem('v2_dirty'); b=localStorage.getItem('v2_last_backup'); }catch(e){}
  var el=document.getElementById('v2-dirty');
  var need = d && (!b || new Date(d)>new Date(b));
  if(!need){ if(el) el.remove(); return; }
  if(el) return;
  el=document.createElement('div'); el.id='v2-dirty';
  el.style.cssText='position:fixed;left:12px;right:12px;bottom:12px;z-index:9999;max-width:560px;margin:0 auto;background:#fbf4e6;border:1px solid #c9a45c;border-radius:10px;padding:10px 14px;font:14px system-ui,sans-serif;color:#1a2233;box-shadow:0 4px 16px rgba(0,0,0,.15);display:flex;gap:10px;align-items:center;flex-wrap:wrap';
  el.innerHTML='<span style="flex:1;min-width:200px"><b>Données modifiées</b> depuis la dernière sauvegarde : elles n’existent que dans ce navigateur.</span><button style="min-height:40px;padding:6px 14px;border-radius:999px;border:1px solid #0e1c33;background:#0e1c33;color:#f4efe3;cursor:pointer" onclick="v2backup();document.getElementById(\'v2-dirty\')&&document.getElementById(\'v2-dirty\').remove()">Sauvegarder</button>';
  document.body.appendChild(el);
}
window.v2banner=banner;
function init(){ box(); banner(); }
if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

// ---- 08/10/2026 : contrôle par les comptes officiels (official_check.json) ----
(function(){
  try{
    fetch('official_check.json?d='+Date.now()).then(function(r){ return r.ok?r.json():null; }).then(function(o){
      if(!o||!o.res||typeof S==='undefined') return;
      S.forEach(function(s){
        var r=o.res[s.ticker]; if(!r) return;
        s.x2=(r.issues||[]).join(' · ');
        s.x2s=(r.checked&&r.checked.length)?'comptes officiels '+String(r.period_end||'').slice(0,4):'';
      });
    }).catch(function(){});
  }catch(e){}
})();

// ═══ 19/10/2026 : Radar élargi — l'univers complet passé chaque semaine à la grille ═══
// PEA : actions UE/EEE > 300 M€ (+ listes repérées) ; CTO : US > 5 Md$, Londres et Suisse > 1 Md.
// Les valeurs qui passent la grille apparaissent ici, même si elles n'ont pas (encore) de fiche.
(function(){
'use strict';
var R=null, F={q:'',c:'tout',z:false,sort:'roic'};
function n(x,d){ return (x==null||x==='')?'—':Number(x).toLocaleString('fr-FR',{maximumFractionDigits:d==null?1:d}); }
function esc(s){ return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];}); }
function load(cb){
  if(R) return cb();
  var fs=[['PEA','candidats_resultats.json'],['CTO','candidats_cto_resultats.json']], out={rows:[],stats:[]}, k=0;
  fs.forEach(function(f){
    fetch(f[1]+'?v='+Date.now()).then(function(r){return r.json();}).then(function(o){
      var seen={};
      Object.keys(o.listes||{}).forEach(function(nm){ var L=o.listes[nm];
        out.stats.push({c:f[0], nom:nm, total:(L.total||0)-(L.hors_pea_ou_doublon||0)-(L.sans_donnees||0), passent:L.passent, date:o.genere});
        (L.lignes||[]).forEach(function(l){ if(!l.qok) return; var key=(l.yahoo||l.code); if(seen[key]) return; seen[key]=1; l.compte=f[0]; out.rows.push(l); });
      });
    }).catch(function(e){ console.error('radar', f[1], e); }).then(function(){ if(++k===fs.length){ R=out; cb(); } });
  });
}
function render(){
  var box=document.getElementById('pg-radar'); if(!box||!R) return;
  var tot=R.stats.reduce(function(a,s){return a+(s.total||0);},0), pas=R.rows.length;
  var rows=R.rows.filter(function(l){
    if(F.c!=='tout'&&l.compte!==F.c) return false;
    if(F.z&&!l.en_zone) return false;
    if(F.q&&(l.nom+' '+l.code+' '+(l.secteur||'')).toLowerCase().indexOf(F.q.toLowerCase())<0) return false;
    return true;
  }).sort(function(a,b){ return F.sort==='nom'?String(a.nom).localeCompare(b.nom):((b[F.sort]||-1e9)-(a[F.sort]||-1e9)); });
  var dates=R.stats.map(function(s){return s.c+' '+String(s.date||'').slice(0,10);}).filter(function(v,i,a){return a.indexOf(v)===i;}).join(' · ');
  var th=function(k,t){ return '<th style="cursor:pointer;text-align:left;padding:6px" onclick="v2radarSort(\''+k+'\')">'+t+(F.sort===k?' ▾':'')+'</th>'; };
  box.innerHTML='<div class="v2" style="max-width:1100px;margin:0 auto">'+
    '<header class="v2-top"><div><div class="v2-kick">Radar élargi · mis à jour chaque semaine ('+esc(dates)+')</div><h1>'+n(pas,0)+' valeurs passent la grille sur '+n(tot,0)+' analysées</h1></div></header>'+
    '<section class="v2-card"><p class="v2-small">Mêmes critères que le screener (ROIC, cash, dette, croissance). PEA : actions de l’UE/EEE de plus de 300 M€ ; compte-titres : États-Unis plus de 5 Md$, Londres et Suisse plus de 1 Md. <b>Une valeur d’ici n’est pas encore vérifiée</b> : pas de contre-expertise, chiffres d’une seule source. Avant tout achat, demande sa fiche complète. Les cycliques n’ont pas de palier ; banques, assurances et foncières attendent leur grille.</p>'+
    '<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:8px">'+
    '<input id="v2-rq" placeholder="Nom, code ou secteur…" value="'+esc(F.q)+'" oninput="v2radarQ(this.value)" style="min-height:40px;padding:6px 12px;border:1px solid #ddd8cb;border-radius:999px;flex:1;min-width:180px">'+
    ['tout','PEA','CTO'].map(function(c){return '<button onclick="v2radarC(\''+c+'\')" style="min-height:40px;padding:6px 14px;border-radius:999px;border:1px solid #0e1c33;background:'+(F.c===c?'#0e1c33;color:#fff':'#fff')+';cursor:pointer">'+(c==='tout'?'Tout':c)+'</button>';}).join('')+
    '<label style="display:flex;gap:6px;align-items:center;min-height:40px"><input type="checkbox" '+(F.z?'checked ':'')+'onchange="v2radarZ(this.checked)" style="width:18px;height:18px"> sous le palier 1</label></div></section>'+
    '<section class="v2-card" style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:13px"><tr style="border-bottom:2px solid #0e1c33">'+
    th('nom','Valeur')+th('roic','ROIC')+th('cash','Cash')+th('croissance','Croissance')+th('dette_ebitda','Dette/EBITDA')+th('cap_Md','Capi (Md)')+'<th style="text-align:left;padding:6px">Cours · palier 1 · palier 2</th><th style="text-align:left;padding:6px">Courtage</th></tr>'+
    rows.map(function(l){
      var pal=l.palier1?(n(l.cours,2)+' · <b style="color:'+(l.en_zone?'#1d6b45':'inherit')+'">'+n(l.palier1,2)+'</b> · '+n(l.palier2,2)+' '+esc(l.devise||'')):'<span class="v2-small">'+esc(l.note?String(l.note).split(':')[0]:'pas de palier')+'</span>';
      return '<tr style="border-bottom:1px solid #eee"><td style="padding:6px"><b>'+esc(l.nom)+'</b> <span class="v2-small">'+esc(l.compte)+' · '+esc(l.code)+(l.secteur?' · '+esc(l.secteur):'')+'</span>'+(l.en_zone?' <span style="background:#1d6b45;color:#fff;border-radius:999px;padding:1px 8px;font-size:11px">sous le palier 1</span>':'')+'</td>'+
        '<td style="padding:6px">'+n(l.roic)+' %</td><td style="padding:6px">'+n(l.cash,0)+' %</td><td style="padding:6px">'+n(l.croissance)+' %</td><td style="padding:6px">'+n(l.dette_ebitda)+'</td><td style="padding:6px">'+n(l.cap_Md)+'</td><td style="padding:6px">'+pal+'</td><td style="padding:6px" class="v2-small">'+esc(l.courtage||'')+'</td></tr>';
    }).join('')+'</table>'+(rows.length?'':'<p class="v2-small">Aucune valeur pour ce filtre.</p>')+'</section></div>';
  var q=document.getElementById('v2-rq'); if(q&&F.q){ q.focus(); q.setSelectionRange(F.q.length,F.q.length); }
}
window.v2radarQ=function(v){ F.q=v; render(); };
window.v2radarC=function(c){ F.c=c; render(); };
window.v2radarZ=function(z){ F.z=z; render(); };
window.v2radarSort=function(k){ F.sort=k; render(); };
window.v2radar=function(){ var b=document.getElementById('pg-radar'); if(b&&!R) b.innerHTML='<p style="padding:24px">Chargement du radar…</p>'; load(render); };
function setup(){
  var al=document.getElementById('pg-al'); if(!al||document.getElementById('pg-radar')) return;
  var pg=document.createElement('div'); pg.className='page'; pg.id='pg-radar'; al.parentNode.insertBefore(pg, al.nextSibling);
  var tab=[].slice.call(document.querySelectorAll('.ntab')).find(function(b){return /'al'/.test(b.getAttribute('onclick')||'');});
  if(tab){ var t=document.createElement('div'); t.className='ntab'; t.setAttribute('onclick',"showPg('radar',this);v2radar()");
    t.style.cssText='background:linear-gradient(135deg,#1d6b45,#2f9466);color:#fff;font-weight:700'; t.textContent='📡 Radar élargi';
    tab.parentNode.insertBefore(t, tab.nextSibling); }
}
if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', setup); else setup();
})();

// ═══ 19/10/2026 : santé des données (health.json, écrit à chaque mise à jour) ═══
(function(){
  function show(txt){
    var d=document.createElement('div'); d.id='v2-health';
    d.style.cssText='background:#a8322b;color:#fff;padding:10px 18px;font:14px/1.4 IBM Plex Sans,system-ui,sans-serif;text-align:center';
    d.innerHTML=txt; document.body.insertBefore(d, document.body.firstChild);
  }
  try{
    fetch('health.json?d='+Date.now()).then(function(r){ return r.ok?r.json():null; }).then(function(h){
      if(!h){ return; }
      var age=(Date.now()-new Date(String(h.date).replace(' ','T')+':00').getTime())/864e5;
      if(h.statut!=='ok') show('<b>Données incomplètes</b> : dernière mise à jour ('+h.date+') : '+h.ok+' fiches sur '+h.total+' à jour. Aucune décision tant qu’un passage complet n’a pas eu lieu.');
      else if(age>3) show('<b>Données anciennes</b> : dernière mise à jour le '+h.date+'. Aucune décision avant la prochaine mise à jour.');
    }).catch(function(){});
  }catch(e){}
})();

// ═══ 20/10/2026 : contrôle manuel Baggr (verdict seulement, aucun chiffre Baggr publié) ═══
(function(){
  try{
    fetch('baggr_check.json?d='+Date.now()).then(function(r){ return r.ok?r.json():null; }).then(function(o){
      if(!o||typeof S==='undefined') return;
      S.forEach(function(s){ var b=o[s.ticker]; if(b){ s.bg=b; } });
    }).catch(function(){});
  }catch(e){}
})();
