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
function dqAll(s){ return [s.dq, s.x2].filter(function(x){return x;}).join(' · '); }
function pct(a,b){ return (a&&b)? ((a/b-1)*100) : null; }
function sgn(x,d){ if(x===null||isNaN(x)) return '—'; return (x>=0?'+':'')+fr(x,d===undefined?0:d)+' %'; }
var C = {gn:'#1d6b45', gn2:'#3f9a68', or:'#a8790f', rd:'#a8322b', ink:'#0e1c33', mu:'#5a6275', bg:'#f5f3ee', line:'#eee9de'};
var UNC = {faible:'faible', moyenne:'moyenne', elevee:'élevée'};
var UNCM = {faible:'10-20 %', moyenne:'15-25 %', elevee:'20-30 %'};
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
  if(s.rec==='buy') return {t:'ACHAT POSSIBLE', c:C.gn, x:'Qualité OK, cours dans la zone d’achat ('+fr(el)+' – '+fr(eh)+' €).'+base};
  if(eh>0 && p<=eh){
    var why = s.knife ? 'mais chute en cours (cours très sous son plus haut d’un an) : comprendre la cause avant d’acheter.'
      : (s.mscore==null||s.mscore<3) ? 'mais moat jugé insuffisant (< 3/5).'
      : (s.regu!=null && s.regn && s.regu < s.regn-1) ? 'mais croissance irrégulière ('+s.regu+'/'+s.regn+' années de hausse du CA).'
      : '';
    return {t:'EN ZONE · PRUDENCE', c:C.or, x:'Cours dans la zone d’achat '+why+base};
  }
  if(eh>0 && p<=eh*1.05) return {t:'PROCHE · ATTENDRE '+fr(eh,0)+' €', c:C.or, x:'Qualité OK, cours à '+fr(pct(p,eh),1)+' % au-dessus de la zone d’achat.'+base};
  if(s.o1>0 && p>s.o1) return {t:'CHÈRE · NE PAS RENFORCER', c:C.rd, x:'Cours au-dessus du scénario optimiste ('+fr(s.o1)+' €) : on n’achète pas, on peut alléger.'+base};
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

// ---- barre de prix ----
function priceBar(s){
  var pts = [s.price, s.el, s.eh, s.stop, s.dcfm, s.vopt, s.vpess, s.tp].filter(function(x){return x>0;});
  var lo = Math.min.apply(null,pts)*0.95, hi = Math.max.apply(null,pts)*1.03, span = hi-lo;
  var pos = function(x){ return Math.max(0,Math.min(100,(x-lo)/span*100)); };
  var h = '<div class="v2-bar"><div class="v2-track"></div>';
  if(s.el>0&&s.eh>0) h += '<div class="v2-zone" style="left:'+pos(s.el)+'%;width:'+(pos(s.eh)-pos(s.el))+'%"></div>'+
    '<div class="v2-lbl" style="left:'+pos(s.el)+'%;top:62px;color:'+C.gn+'">Zone '+fr(s.el,0)+' – '+fr(s.eh,0)+' €</div>';
  if(s.stop>0) h += '<div class="v2-tick" style="left:'+pos(s.stop)+'%;background:'+C.rd+'"></div><div class="v2-lbl" style="left:'+pos(s.stop)+'%;top:80px;color:'+C.rd+'">Relire la thèse '+fr(s.stop,0)+'</div>';
  if(s.tp>0) h += '<div class="v2-tick" style="left:'+pos(s.tp)+'%;background:#6b7487;width:2px"></div><div class="v2-lbl" style="left:'+pos(s.tp)+'%;top:80px;color:'+C.mu+'">analystes '+fr(s.tp,0)+'</div>';
  if(s.dcfm>0) h += '<div class="v2-tick" style="left:'+pos(s.dcfm)+'%;background:'+C.ink+';height:38px;top:26px"></div><div class="v2-lbl" style="left:'+pos(s.dcfm)+'%;top:62px;color:'+C.ink+'">central '+fr(s.dcfm,0)+'</div>';
  if(s.vopt>0) h += '<div class="v2-tick" style="left:'+pos(s.vopt)+'%;background:#b8862b"></div><div class="v2-lbl" style="left:'+pos(s.vopt)+'%;top:80px;color:#8a6420">alléger &gt; '+fr(s.vopt,0)+'</div>';
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
  if(isFin(s)) return '<section class="v2-card"><h2>Qualité</h2><p>Banque ou assurance : grille dédiée (rentabilité des fonds propres, solvabilité, coût du risque) <b>en préparation</b>. Pas de verdict qualité en attendant.</p></section>';
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
    '<div class="v2-small">Note de moat et niveau d’incertitude : jugement de Claude, à valider par toi.</div></section>';
}

// ---- thèse + tableau de bord ----
function thesis(s, F){
  if(!F) return '<section class="v2-card"><h2>Ma thèse d’investissement</h2><p class="v2-small">Pas encore rédigée pour cette valeur (rédigée en priorité pour tes lignes et les valeurs de qualité).</p></section>';
  var rows = (F.kpi||[]).map(function(k){ return '<tr><td>'+esc(k[0])+'</td><td class="v2-mono">'+esc(k[1])+'</td><td>'+esc(k[2])+'</td></tr>'; }).join('');
  return '<section class="v2-card"><div class="v2-head"><h2>Ma thèse d’investissement</h2><span class="v2-pill" style="background:#fbf4e6;color:#8a6420">BROUILLON — À VALIDER</span></div>'+
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
  if(!(s.qok||s.near) || s.vmeth!=='qarp' || !s.vpess){
    return '<section class="v2-card"><h2>Le prix</h2><p>Pas de zone d’achat : la valeur ne passe pas le filtre qualité, la méthode ne cherche donc pas à l’acheter. '+
      (s.tp>0?'Pour information, objectif moyen des analystes : <b>'+fr(s.tp)+' €</b>.':'')+'</p></section>';
  }
  var card = function(t,col,bg,v,txt,out){ return '<div class="v2-scen" style="background:'+bg+(out?';outline:2px solid '+C.ink:'')+'"><div class="v2-k" style="color:'+col+'">'+t+'</div><div class="v2-big">'+fr(v,0)+' € <span style="font-size:14px;color:'+(v>=s.price?C.gn:C.rd)+'">'+sgn(pct(v,s.price))+'</span></div><div class="v2-small">'+txt+'</div></div>'; };
  var gc = s.gused!=null ? Math.max(0,Math.min(12,s.gused)) : null;
  return '<section class="v2-card"><div class="v2-head"><h2>Le prix : trois scénarios, une zone</h2>'+
    (s.unc?'<span class="v2-pill" style="background:#f5f3ee;color:'+C.ink+'">INCERTITUDE '+(UNC[s.unc]||'NON ÉVALUÉE').toUpperCase()+'</span>':'')+'</div>'+
    (s.irr!=null?'<div class="v2-note" style="background:'+(s.irr>=8.5?'#eef6f1':'#fbecea')+'"><span><b>En clair : si tu achètes à '+fr(s.price)+' €</b> et que la croissance retenue ('+fr(s.gused,1)+' %/an) se réalise, l’action devrait rapporter <b class="v2-mono">≈ '+fr(s.irr,1)+' %/an</b> (dividendes compris). La méthode exige 8,5 %/an'+(s.irr>=8.5?' : <b style="color:'+C.gn+'">le prix le permet</b>.':' : <b style="color:'+C.rd+'">trop cher pour ton exigence</b>. La valeur centrale ci-dessous est le prix qui donnerait 8,5 %/an.')+'</span></div>':'')+
    '<div class="v2-grid3">'+
      card('PESSIMISTE',C.rd,'#fbecea',s.vpess,'Plus aucune croissance pendant 10 ans.')+
      card('CENTRAL',C.ink,C.bg,s.dcfm,'Prix pour gagner 8,5 %/an si '+(gc!=null?fr(gc,1)+' %/an au départ':'la croissance retenue')+', ralentissant vers 2,5 %.',true)+
      card('OPTIMISTE',C.gn,'#eef6f1',s.vopt,(gc!=null?fr(Math.min(12,gc+3),1)+' %/an au départ':'croissance + 3 points')+'.')+
    '</div>'+priceBar(s)+
    (s.vmult>0?'<div class="v2-note"><span><b>Contrôle par une 2e méthode</b> (bénéfice sur 5 ans revendu au PER habituel de l’entreprise) : <span class="v2-mono">'+fr(s.vmult,0)+' €</span>, soit '+sgn(pct(s.vmult,s.dcfm),0)+' par rapport au scénario central. '+(Math.abs(s.vmult/s.dcfm-1)>0.35?'<b style="color:'+C.rd+'">Les deux méthodes divergent : zone d’achat à prendre avec prudence.</b>':'Les deux méthodes concordent.')+'</span></div>':'')+
    (s.gimp!=null?'<div class="v2-note"><span><b>Ce que le cours suppose :</b> <span class="v2-mono">'+fr(s.gimp,1)+' %/an</span> contre <span class="v2-mono" style="color:'+C.gn+'">'+fr(s.gused,1)+' %/an retenus</span></span></div>':'')+
    '<div class="v2-small">Décote exigée selon l’incertitude : faible 10-20 % · moyenne 15-25 % · élevée 20-30 %. Sous le seuil de revue : relire la thèse, pas de vente automatique.</div></section>';
}

function technical(s){
  var tr = (s.price>s.mm200) ? 'au-dessus de la moyenne 200 jours : tendance de fond haussière' : 'sous la moyenne 200 jours : tendance de fond baissière';
  return '<details class="v2-card v2-det"><summary>Détails techniques</summary><div class="v2-tiles"><div>Moyenne 50 j<br><b>'+fr(s.mm50)+' €</b></div><div>Moyenne 200 j<br><b>'+fr(s.mm200)+' €</b></div><div>RSI 14 j<br><b>'+fr(s.rsi,1)+'</b></div><div>Plus bas / haut 1 an<br><b>'+fr(s.b52l)+' – '+fr(s.b52h)+'</b></div></div><p class="v2-small">Cours '+tr+'.'+(s.knife?' <b style="color:'+C.rd+'">Chute en cours.</b>':'')+'</p></details>';
}

function sources(s){
  var q = encodeURIComponent(s.name||s.ticker);
  return '<section class="v2-card v2-small"><p>Sources : cours et ratios Yahoo Finance (mise à jour automatique) · croissance : '+esc(s.gsrc||'Yahoo')+' · '+
    (s.x2s?'contrôle croisé du cours : '+esc(s.x2s)+(s.x2?' (écart)':' (concordant)')+' · ':'')+
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
function decision(s){
  var g = (s.qok && s.rec==='buy') ? 'buy' : 'no';
  var L = ceList(s.ticker), last = L[0];
  var age = last ? Math.round((Date.now()-new Date(last.date).getTime())/864e5) : null;
  var tot = ptfTotal(), full = tot*0.05, half = tot*0.025;
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
  } else if(last.concl==='fragilisee'){
    r = {t:'ACHAT : OUI À 50 %', c:C.or, x:'Thèse fragilisée ('+esc(last.point||'')+') : demi-position seulement'+(tot>0?', environ <b>'+fr(half,0)+' €</b> (2,5 % du portefeuille)':'')+', ordre à cours limité <b>'+fr(lim)+' €</b> (bas de la zone). Le reste après la prochaine publication si la thèse se renforce.'};
  } else {
    r = {t:'ACHAT : OUI', c:C.gn, x:'Achat possible et thèse intacte (contre-expertise du '+last.date+'). Position normale'+(tot>0?' : environ <b>'+fr(full,0)+' €</b> (5 % du portefeuille, plafond 10 %)':'')+', ordre à cours limité <b>'+fr(Math.min(s.eh,s.price))+' €</b> maximum.'};
  }
  var stop = (s.stop>0 && (s.qok||s.near)) ? '<p class="v2-small"><b>Stop :</b> pas d’ordre stop automatique sur une valeur de qualité (il vendrait au pire moment). Sous <b>'+fr(s.stop)+' €</b> (seuil de revue) : contre-expertise obligatoire ; si elle conclut « thèse cassée », on vend.</p>' : '';
  return '<section class="v2-card" style="border:2px solid '+r.c+'"><div class="v2-head"><h2>Décision</h2><span class="v2-small">'+esc(window.v2profName?('Portefeuille : '+window.v2profName()):'')+'</span></div>'+
    '<div class="v2-verdict" style="padding:0"><div class="v2-badge" style="background:'+r.c+'">'+r.t+'</div><p>'+r.x+'</p></div>'+stop+
    '<div><button onclick="v2jnl(\''+s.ticker+'\')" style="min-height:44px;padding:8px 16px;border-radius:999px;border:1px solid #0e1c33;background:#fff;cursor:pointer;font-weight:600">Noter ma décision dans le journal</button> <span class="v2-small">pré-rempli avec la fiche (verdict, thèse, contre-expertise, seuil de revue)</span></div></section>';
}


// ---- 06/10/2026 : journal pré-rempli depuis la fiche ----
window.v2jnl = function(t){
  var s=S.find(function(x){return x.ticker===t;}); if(!s) return;
  var F=(typeof FICHE!=='undefined')?FICHE[t]:null, L=ceList(t), last=L[0], v=verdict(s);
  var tab=[].slice.call(document.querySelectorAll('.ntab')).find(function(b){return /jnl/.test(b.getAttribute('onclick')||'');});
  showPg('jnl', tab);
  setTimeout(function(){
    var f=document.getElementById('jnl-form'); if(f && f.style.display!=='block') jnlNew();
    var set=function(id,val){ var e=document.getElementById(id); if(e) e.value=val; };
    set('jnl-ticker', t); set('jnl-cours', s.price);
    set('jnl-type', (s.qok&&s.rec==='buy')?'ACHAT':'ATTENDRE');
    set('jnl-why', 'Screener ('+new Date().toLocaleDateString('fr-FR')+') : '+v.t+' · zone '+fr(s.el)+'–'+fr(s.eh)+' € · valeur centrale '+fr(s.dcfm)+' €'+
      (last?' · contre-expertise du '+last.date+' : '+(CEL[last.concl]?CEL[last.concl][0]:'?'):' · pas de contre-expertise')+
      (F?'\nThèse : '+F.why:'')+'\nMa raison à moi : ');
    set('jnl-exit', (F?F.wrong+'\n':'')+'Seuil de revue : '+fr(s.stop)+' € → contre-expertise obligatoire.');
    var w=document.getElementById('jnl-why'); if(w){ w.focus(); w.setSelectionRange(w.value.length,w.value.length); }
  }, 400);
};

function renderV2(s){
  var F = (typeof FICHE!=='undefined') ? FICHE[s.ticker] : null;
  var v = verdict(s);
  var chg = (s.chg!=null && Math.abs(s.chg)<50) ? '<span style="color:'+(s.chg>=0?'#7fd1a3':'#f2a29b')+'">'+sgn(s.chg,2)+' aujourd’hui</span>' : '';
  return '<div class="v2">'+
    '<header class="v2-top"><div><div class="v2-kick">'+esc(s.ticker)+' · '+esc(s.place||'')+' · '+esc(s.sector||'')+'</div><h1>'+esc(s.name)+'</h1></div>'+
    '<div class="v2-px"><div>'+fr(s.price)+' €</div><div class="v2-small" style="color:#c7cede">'+chg+'</div></div></header>'+
    (dqAll(s)?'<section class="v2-card" style="background:#fbf4e6;border-left:4px solid #a8790f"><b>Donnée à vérifier avant toute décision :</b> '+esc(dqAll(s))+'. <span class="v2-small">Contrôle automatique : la source (Yahoo) peut se tromper ; vérifie sur Zonebourse ou le rapport annuel.</span></section>':'')+
    '<section class="v2-card v2-verdict"><div class="v2-badge" style="background:'+v.c+'">'+v.t+'</div><p>'+v.x+'</p>'+position(s)+'</section>'+
    priceBlock(s)+ratios(s)+
    '<div class="v2-two">'+quality(s)+moat(s,F)+'</div>'+
    thesis(s,F)+figures(s)+technical(s)+ceBlock(s)+decision(s)+sources(s)+
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
    fe.innerHTML = renderV2(s) + '<details class="v2-old"><summary>Ancienne analyse (non mise à jour, peut contredire la fiche ci-dessus)</summary>'+old+'</details>';
  };
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
    (gap!=null&&(s.qok||s.near)?'<span class="v2-small">'+(gap<=0?'en zone':'doit baisser de '+fr(gap,0)+' %')+'</span>':'<span class="v2-small">'+esc((s.qwhy||'').split(',')[0])+'</span>')+
    (s.mscore!=null?'<span class="v2-small">moat '+s.mscore+'/5</span>':'')+'</button>';
}
function buildHome(){
  var pg = document.getElementById('pg-sc'); if(!pg) return;
  var box = document.getElementById('v2-home');
  if(!box){ box=document.createElement('div'); box.id='v2-home'; pg.insertBefore(box, pg.firstChild); }
  var buy=[], watch=[], out=[];
  S.forEach(function(s){ if(!s||!s.ticker||!(s.price>0)) return; var g=group(s); (g==='buy'?buy:g==='watch'?watch:out).push(s); });
  var byGap = function(a,b){ return (a.eh>0?a.price/a.eh:9)-(b.eh>0?b.price/b.eh:9); };
  buy.sort(byGap); watch.sort(byGap); out.sort(function(a,b){return (a.name||'').localeCompare(b.name||'');});
  box.innerHTML = '<div class="v2-home"><div class="v2-hgrp" style="border-top:4px solid '+C.gn+'"><h3>Achat possible <span>'+buy.length+'</span></h3><p class="v2-small">Qualité OK · cours en zone · moat ≥ 3 · croissance régulière · pas de chute</p>'+(buy.map(item).join('')||'<p class="v2-small">Aucune aujourd’hui → versement du mois sur l’ETF Monde.</p>')+'</div>'+
    '<div class="v2-hgrp" style="border-top:4px solid '+C.or+'"><h3>À surveiller <span>'+watch.length+'</span></h3><p class="v2-small">Qualité OK mais trop chère, en chute, ou limite (un critère manqué de peu) · les plus proches de leur zone en premier</p>'+watch.map(item).join('')+'</div>'+
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
function grp(s){ if(s.qok && s.rec==='buy') return 'buy'; if(s.qok||s.near) return 'watch'; return 'out'; }
function mine(){
  var list=(typeof PTF!=='undefined'&&(PTF.length||(window._ptfProfile&&window._ptfProfile!=='val')))?PTF:null;
  if(!list){ try{ list=JSON.parse(localStorage.getItem('pea_ptf_val')||'[]'); }catch(e){ list=[]; } }
  return list.map(function(p){return p&&p.ticker;});
}
var DOT={buy:'#1d6b45',watch:'#a8790f',out:'#9aa1ae'}, LAB={buy:'achat',watch:'surveiller',out:'hors'};
var FILTERS=[['all','Tout'],['buy','Achat possible'],['watch','À surveiller'],['out','Hors qualité'],['mine','Mes lignes'],['large','Large'],['mid','Mid'],['small','Small']];
function apply(key){
  var m=mine();
  fil = S.filter(function(s){
    if(!s||!s.ticker) return false;
    if(key==='all') return true;
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
  c.innerHTML = FILTERS.map(function(f){ return '<button class="fb'+(f[0]==='all'?' active':'')+'" data-f="'+f[0]+'" onclick="v2filt(\''+f[0]+'\')">'+f[1]+'</button>'; }).join('')+
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
  set('hkT', S.length, 'Valeurs');
  set('hkD', n.buy, 'Achat possible');
  set('hkAB', n.watch, 'À surveiller');
  set('hkZ', mine().filter(function(t){return S.some(function(s){return s.ticker===t;});}).length, 'Mes lignes');
  var src=(document.querySelector('script[src*="data.js?v="]')||{}).src||'', ts=(src.match(/v=(\d{9,})/)||[])[1];
  set('hkP', ts? new Date(ts*1000).toLocaleDateString('fr-FR',{day:'2-digit',month:'2-digit'}) : '—', 'Mise à jour');
};
function go(){ try{ bar(); updHK(); buildQ(); }catch(e){ console.error('v2 bar', e); } }
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
  var zone=[], out=[], review=[], high=[], big=[], ce=[];
  S.forEach(function(s){
    if(!s||!s.ticker||!(s.price>0)) return;
    if(s.qok && s.eh>0 && s.price<=s.eh){ now[s.ticker]=1; zone.push(row(s, (s.rec==='buy'?'achat possible':'en zone mais '+(s.knife?'chute en cours':(s.mscore==null||s.mscore<3)?'moat faible':'croissance irrégulière'))+' · zone '+fr(s.el)+'–'+fr(s.eh)+' €', !seen[s.ticker])); }
    var p=held[s.ticker]; if(!p) return;
    if(!s.qok && !s.near) out.push(row(s,'hors qualité : '+esc(s.qwhy||'')+(s.ticker==='TTE'?' → exception « poche cyclique » à écrire (stop proposé 68 €)':' → vendre si confirmé à la prochaine publication')));
    if(s.stop>0 && s.price<s.stop && (s.qok||s.near)) review.push(row(s,'sous le seuil de revue ('+fr(s.stop)+' €) → contre-expertise obligatoire'));
    if(s.vopt>0 && s.price>s.vopt && !/EXCEPTION/.test(s.qwhy||'')) high.push(row(s,'au-dessus du scénario optimiste ('+fr(s.vopt)+' €) → alléger possible, jamais tout vendre'));
    var w=tot>0?s.price*p.qty/tot*100:0; if(w>10) big.push(row(s,'pèse '+fr(w,1)+' % (plafond 10 %) → ne pas renforcer'));
    var L=window.v2ceList?v2ceList(s.ticker):[], age=L[0]?Math.round((Date.now()-new Date(L[0].date).getTime())/864e5):null;
    if(age==null||age>90) ce.push(row(s, age==null?'jamais de contre-expertise':'dernière contre-expertise il y a '+age+' jours'));
  });
  try{ localStorage.setItem('v2_al_seen', JSON.stringify(now)); }catch(e){}
  var who=window.v2profName?v2profName():'Moi';
  box.innerHTML='<div class="v2" style="max-width:1100px;margin:0 auto">'+
    '<header class="v2-top"><div><div class="v2-kick">Alertes · règles de la méthode</div><h1>Ce qui demande ton attention</h1></div><div class="v2-small" style="color:#c7cede">Portefeuille : '+esc(who)+'</div></header>'+
    card('Mes lignes hors qualité','vente si la prochaine publication confirme',out,'#a8322b')+
    card('Mes lignes sous le seuil de revue','contre-expertise obligatoire, pas de vente automatique',review,'#a8322b')+
    card('Valeurs de qualité en zone d’achat','« NOUVEAU » = entrée en zone depuis ta dernière visite',zone,'#1d6b45')+
    card('Mes lignes trop grosses','plafond 10 % par action',big,'#a8790f')+
    card('Mes lignes au-dessus du scénario optimiste','alléger possible',high,'#a8790f')+
    card('Contre-expertises à faire','lignes détenues sans contre-expertise de moins de 3 mois',ce,'#6b7487')+
  '</div>';
}
window.v2alerts=alerts;
function guide(){
  var g=document.getElementById('pg-guide'); if(!g) return;
  g.innerHTML='<div class="v2" style="max-width:980px;margin:0 auto">'+
  '<header class="v2-top"><div><div class="v2-kick">Mode d’emploi · méthode qualité à prix raisonnable</div><h1>Comment je décide</h1></div></header>'+
  '<section class="v2-card"><h2>1. La règle d’or</h2><p>J’achète des entreprises <b>excellentes</b>, seulement quand leur prix est <b>raisonnable</b>, et je les garde tant qu’elles restent excellentes. Je ne vends <b>jamais</b> sur le prix seul.</p></section>'+
  '<section class="v2-card"><h2>2. Le filtre qualité (médianes sur 4 ans)</h2><p>Rentabilité du capital hors écarts d’acquisition ≥ 15 % · rentabilité du capital total ≥ 12 % · bénéfice transformé en cash ≥ 80 % · dette nette ≤ 2,5 × EBITDA · croissance ≥ 3 %/an (chiffres officiels quand ils existent). Plus : moat ≥ 3/5 et chiffre d’affaires en hausse au moins 2 ans sur 3 pour pouvoir acheter.</p></section>'+
  '<section class="v2-card"><h2>3. Le prix</h2><p>Trois scénarios (pessimiste, central, optimiste). Zone d’achat = valeur centrale moins une décote qui dépend de l’incertitude : faible 10-20 %, moyenne 15-25 %, élevée 20-30 %. « Ce que le cours suppose » compare la croissance que le marché paie à la croissance réelle.</p></section>'+
  '<section class="v2-card"><h2>4. Avant d’acheter</h2><p>Une <b>contre-expertise</b> de moins de 3 mois : thèse intacte → achat normal (≈ 5 % du portefeuille) ; fragilisée → demi-position ; cassée → non. Puis je note la décision dans le <b>journal</b> (bouton en bas de chaque fiche).</p></section>'+
  '<section class="v2-card"><h2>5. La routine du mois (1er dimanche, 15 min)</h2><p>1. Versement. 2. Onglet portefeuille : une ligne « REVOIR » deux publications de suite → je vends. 3. Une action « achat possible » avec contre-expertise favorable et ligne &lt; 10 % → j’achète ; sinon le versement va sur l’ETF Monde. 4. Une ligne dans le journal. Le reste du mois : aucune décision.</p></section>'+
  '<section class="v2-card"><h2>6. Garde-fous</h2><p>Maximum 10 % par action · 13 à 15 lignes · seuil de revue = scénario pessimiste − 10 % (contre-expertise obligatoire, pas de vente automatique) · exceptions écrites seulement (Air Liquide ; poche cyclique avec vrai stop pour TotalEnergies).</p></section>'+
  '<section class="v2-card v2-small"><p>Les notes A-D, le « triptyque », les scores Large/Mid et l’ancien radar d’alertes ne servent plus à décider. Le screener informe ; c’est toi qui décides, avec ces règles écrites.</p></section>'+
  '</div>';
}
function tabs(){
  document.querySelectorAll('.ntab').forEach(function(b){
    var o=b.getAttribute('onclick')||'';
    if(/'acad'|'bt'/.test(o)) b.style.display='none';
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
if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', box); else box();
})();
