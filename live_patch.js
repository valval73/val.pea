
// PEA SCREENER PRO — live_patch.js v5.1
// Prompt IA pro (Quality Investing / Buffett) + fréquence optimisée
// ================================================================

const YF_BASE = 'https://query1.finance.yahoo.com/v8/finance/chart/';

const PROXIES = [
  url => 'https://api.codetabs.com/v1/proxy?quest=' + encodeURIComponent(url),
  url => 'https://thingproxy.freeboard.io/fetch/' + encodeURIComponent(url),
  url => 'https://api.allorigins.win/raw?url=' + encodeURIComponent(url)
];

const YF_MAP = {
MC:'MC.PA',AI:'AI.PA',OR:'OR.PA',RMS:'RMS.PA',SAN:'SAN.PA',
TTE:'TTE.PA',SAF:'SAF.PA',SU:'SU.PA',AXA:'CS.PA',BNP:'BNP.PA',
ACA:'ACA.PA',GLE:'GLE.PA',AIR:'AIR.PA',CAP:'CAP.PA',DSY:'DSY.PA',
LR:'LR.PA',PUB:'PUB.PA',RI:'RI.PA',SGO:'SGO.PA',VIE:'VIE.PA',
ORA:'ORA.PA',EL:'EL.PA',KER:'KER.PA',STM:'STM.PA',ENX:'ENX.PA',
ENGI:'ENGI.PA',DG:'DG.PA',HO:'HO.PA',BN:'BN.PA',CA:'CA.PA',
WLN:'WLN.PA',RNO:'RNO.PA',TEP:'TEP.PA',FTI:'FTI.PA',ALO:'ALO.PA',
EDEN:'EDEN.PA',SAM:'SAM.PA',GTT:'GTT.PA',SEB:'SK.PA',VK:'VK.PA',
MT:'MT.AS',STLA:'STLA.MI',SAP:'SAP.DE',ASML:'ASML.AS',
SIE:'SIE.DE',BAYN:'BAYN.DE',BMW:'BMW.DE',ALV:'ALV.DE',
ENEL:'ENEL.MI',ENI:'ENI.MI',UCG:'UCG.MI',RACE:'RACE.MI',
CABK:'CABK.MC',BBVA:'BBVA.MC',IBE:'IBE.MC',ITX:'ITX.MC',
TEF:'TEF.MC',NN:'NN.AS',INGA:'INGA.AS',AD:'AD.AS'
};

let _activeProxyIdx = 0;

async function fetchOnePrice(yfSym) {
  const url0 = YF_BASE + yfSym + '?range=1d&interval=5m';
  const order = [_activeProxyIdx, ...PROXIES.map((_,i)=>i).filter(i=>i!==_activeProxyIdx)];
  for (const idx of order) {
    try {
      const r = await fetch(PROXIES[idx](url0), { signal: AbortSignal.timeout(8000) });
      if (!r.ok) continue;
      const d = await r.json();
      const m = d && d.chart && d.chart.result && d.chart.result[0] && d.chart.result[0].meta;
      if (!m || !m.regularMarketPrice) continue;
      _activeProxyIdx = idx;
      return {
        p: Math.round(m.regularMarketPrice*100)/100,
        c: Math.round((m.regularMarketPrice-m.chartPreviousClose)/m.chartPreviousClose*10000)/100,
        h52: Math.round((m.fiftyTwoWeekHigh||0)*100)/100,
        l52: Math.round((m.fiftyTwoWeekLow||0)*100)/100
      };
    } catch(e) {}
  }
  return null;
}

window.fetchLive = async function(isAuto) {
  const LS = 'valpea_fetch';
  if (isAuto) { try { if (Date.now()-parseInt(localStorage.getItem(LS)||0)<15*60*1000) return; } catch(e){} }
  try { localStorage.setItem(LS, Date.now()); } catch(e) {}
  const liveEl = document.getElementById('live-st');
  const upd = function(msg,col){ if(liveEl){liveEl.textContent=msg;liveEl.style.color=col||'#f59e0b';} };
  upd('Connexion...','#f59e0b');
  const tickers = typeof S!=='undefined' ? S.map(function(s){return s.ticker;}).filter(function(t){return YF_MAP[t];}) : Object.keys(YF_MAP);
  let ok=0, fail=0;
  for (let i=0; i<tickers.length; i+=6) {
    await Promise.all(tickers.slice(i,i+6).map(async function(ticker) {
      try {
        const data = await fetchOnePrice(YF_MAP[ticker]);
        if (data && typeof S!=='undefined') {
          const s = S.find(function(x){return x.ticker===ticker;});
          if (s) { s.price=data.p; s.chg=data.c; if(data.h52>0)s.b52h=data.h52; if(data.l52>0)s.b52l=data.l52; if(typeof render==='function')render(s); ok++; }
        }
      } catch(e) { fail++; }
    }));
    upd(ok+'/'+tickers.length+' cours...','#f59e0b');
    if (i+6<tickers.length) await new Promise(function(r){setTimeout(r,400);});
  }
  const now = new Date().toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit'});
  upd(ok>0?ok+' cours live · '+now:'Hors marché · données statiques',ok>0?'#22c55e':'#6b7280');
};

// ─── CLÉ IA ────────────────────────────────────────────────────
function getANTKey(){if(window._ANT)return window._ANT;const k=localStorage.getItem('_ant_key');if(k){window._ANT=k;return k;}return null;}
function clearANTKey(){localStorage.removeItem('_ant_key');window._ANT=null;}

function showKeyPrompt(onSave){
  if(document.getElementById('ia-key-modal'))return;
  const ov=document.createElement('div'); ov.id='ia-key-modal';
  ov.style.cssText='position:fixed;inset:0;background:rgba(0,0,0,.75);z-index:9999;display:flex;align-items:center;justify-content:center;';
  const box=document.createElement('div'); box.style.cssText='background:#0f2540;border-radius:14px;padding:28px;max-width:440px;width:92%;border:1px solid rgba(255,255,255,.1);';
  const t=document.createElement('div'); t.style.cssText='font-size:16px;font-weight:700;color:#fff;margin-bottom:6px;'; t.textContent='🤖 Clé API Anthropic';
  const s=document.createElement('div'); s.style.cssText='font-size:12px;color:#8899aa;margin-bottom:18px;'; s.textContent='Pour analyser avec IA + recherche web temps réel';
  const inp=document.createElement('input'); inp.id='ant-inp'; inp.type='password'; inp.placeholder='sk-ant-api03-...';
  inp.style.cssText='width:100%;padding:11px;background:#1a3050;border:1px solid #2a4060;border-radius:8px;color:#fff;font-size:12px;font-family:monospace;box-sizing:border-box;outline:none;';
  const lnk=document.createElement('div'); lnk.style.cssText='font-size:11px;color:#8899aa;margin-top:8px;';
  lnk.innerHTML='Stockée localement · <a href="https://console.anthropic.com/settings/keys" target="_blank" style="color:#7C3AED;">Obtenir une clé</a>';
  const row=document.createElement('div'); row.style.cssText='display:flex;gap:10px;margin-top:18px;';
  const bS=document.createElement('button'); bS.style.cssText='flex:1;padding:10px;background:#7C3AED;color:#fff;border:none;border-radius:7px;font-weight:700;cursor:pointer;'; bS.textContent='Activer l’IA';
  const bK=document.createElement('button'); bK.style.cssText='padding:10px 16px;background:transparent;color:#8899aa;border:1px solid #2a4060;border-radius:7px;cursor:pointer;'; bK.textContent='Plus tard';
  row.appendChild(bS); row.appendChild(bK);
  box.appendChild(t); box.appendChild(s); box.appendChild(inp); box.appendChild(lnk); box.appendChild(row);
  ov.appendChild(box); document.body.appendChild(ov);
  bS.onclick=function(){const k=inp.value.trim();if(k.startsWith('sk-ant')){localStorage.setItem('_ant_key',k);window._ANT=k;ov.remove();if(onSave)onSave(k);}else inp.style.borderColor='#ef4444';};
  bK.onclick=function(){ov.remove();};
}

// ─── ANALYSE IA — PROMPT PROFESSIONNEL QUALITY INVESTING ─────────
async function runIAAnalysis(ticker, name, scoreData, resEl, btn) {
  const key = getANTKey();
  if (!key) { showKeyPrompt(function(k){window._ANT=k;runIAAnalysis(ticker,name,scoreData,resEl,btn);}); return; }
  btn.disabled=true; btn.textContent='⏳ Analyse...';
  resEl.style.display='block';
  resEl.innerHTML='<div style="color:#7C3AED;padding:8px;font-size:12px;">🔍 Analyse Quality Investing <b>'+name+'</b>...</div>';

  const ctx = scoreData ? 'Score QARP '+scoreData.qarp+'/100, Grade '+scoreData.grade
    +', Prix '+(scoreData.price||'?')+'€'
    +', PE '+(scoreData.pe||'?')+'x'
    +', ROE '+(scoreData.roe||'?')+'%'
    +', Marge '+(scoreData.margin||'?')+'%'
    +', Div '+(scoreData.dy||'?')+'%'
    +', Dette/Eq '+(scoreData.debt||'?')
    +', Beneish '+(scoreData.beneish||'?')
    +', Piotroski '+(scoreData.pio||'?')+'/9' : '';

  const prompt = 'Tu es gérant de portefeuille long terme, Quality Investing / Buffett. Décision pour PEA.\n'
    + 'ACTION : '+name+' ('+ticker+') | PRIX : '+(scoreData&&scoreData.price?scoreData.price:'?')+'€ | '+ctx+'\n\n'
    + 'RÈGLES ABSOLUES :\n'
    + '- Zéro résumé de communiqué de presse\n'
    + '- Chaque affirmation chiffrée et sourced\n'
    + '- Conclusion BINAIRE : INVESTIR ou PASSER (pas de nuance)\n\n'
    + '## VERDICT : [INVESTIR / PASSER / ATTENDRE ZONE]\n'
    + '(une ligne, sans nuance, avec le prix d\'entrée si ATTENDRE)\n\n'
    + '## MOAT — Machine à cash durable ?\n'
    + '- Avantage concurrentiel : [nom précis + chiffre qui le prouve]\n'
    + '- Pricing power : marge brute % vs moyenne secteur %\n'
    + '- Risque disruption 5 ans : faible/moyen/fort + raison\n\n'
    + '## VALORISATION — Prix payé ?\n'
    + '- FCF Yield estimé : [%] → cher/juste/opportunité\n'
    + '- PE actuel vs historique 10 ans : [X]x vs [Y]x\n'
    + '- Zone d\'achat optimale : [X€ à Y€]\n'
    + '- Scénario baissier (-20% résultats) : cours = [Z€]\n\n'
    + '## BILAN — Solidité récession ?\n'
    + '- Dette nette/EBITDA : [x] → safe/limite/danger\n'
    + '- Dividende couvert par FCF : oui/non\n\n'
    + '## CATALYSEURS vs RISQUES\n'
    + '- Catalyseur #1 : [impact estimé sur résultats %]\n'
    + '- Catalyseur #2 : [concret]\n'
    + '- Risque #1 : [probabilité] + [impact si réalisé]\n'
    + '- Risque #2 : [concret]\n\n'
    + '## DÉCISION FINALE\n'
    + '- Action : ACHETER/RENFORCER/CONSERVER/ALLÉGER/VENDRE/PASSER\n'
    + '- Taille position : [X% du portefeuille PEA]\n'
    + '- Point d\'entrée : [X€ ou déjà en zone]\n'
    + '- Objectif 3 ans : [Y€] (+X%)\n'
    + '- Stop loss logique : [Z€]\n\n'
    + 'Aucun disclaimer. Structure stricte obligatoire.';

  try {
    const resp = await fetch('https://api.anthropic.com/v1/messages', {
      method:'POST',
      headers:{'Content-Type':'application/json','x-api-key':key,'anthropic-version':'2023-06-01','anthropic-beta':'web-search-2025-03-05','anthropic-dangerous-direct-browser-access':'true'},
      body: JSON.stringify({model:'claude-sonnet-4-20250514', max_tokens:1200,
        tools:[{type:'web_search_20250305',name:'web_search'}],
        messages:[{role:'user',content:prompt}]})
    });
    if (!resp.ok) { const e=await resp.json().catch(function(){return{};}); throw new Error(e.error&&e.error.message?e.error.message:'HTTP '+resp.status); }
    const d = await resp.json();
    const text = (d.content||[]).filter(function(b){return b.type==='text';}).map(function(b){return b.text;}).join('').trim();
    if (text) {
      // Format markdown → HTML
      let html = text
        .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
        .replace(/## (.+)/g,'<h4 style="color:#1e293b;margin:10px 0 4px;font-size:12px;border-bottom:1px solid #e2e8f0;padding-bottom:3px;">$1</h4>')
        .replace(/**(.+?)**/g,'<strong>$1</strong>')
        .replace(/
- /g,'<br>• ')
        .replace(/

/g,'</p><p style="margin:6px 0">')
        .replace(/
/g,'<br>');
      resEl.innerHTML='<div style="line-height:1.6;color:#1e293b;font-size:12px;"><p style="margin:0">'+html+'</p></div>';
    } else { resEl.innerHTML='<div style="color:#888;font-size:12px;">Analyse non disponible</div>'; }
  } catch(e) {
    if (e.message.indexOf('401')>=0||e.message.indexOf('invalid_api_key')>=0) {
      clearANTKey();
      const ed=document.createElement('div'); ed.style.cssText='color:#ef4444;font-size:12px;';
      ed.textContent='Clé invalide. ';
      const rc=document.createElement('a'); rc.href='#'; rc.style.color='#7C3AED'; rc.textContent='Reconfigurer';
      rc.onclick=function(ev){ev.preventDefault();clearANTKey();resEl.style.display='none';btn.disabled=false;btn.textContent='🤖 Analyse IA';};
      ed.appendChild(rc); resEl.innerHTML=''; resEl.appendChild(ed);
    } else { resEl.innerHTML='<div style="color:#ef4444;font-size:12px;">Erreur: '+e.message+'</div>'; }
  }
  btn.disabled=false; btn.textContent='🤖 Analyse IA';
}

function injectIAButton(ticker, name, scoreData) {
  const fiche=document.getElementById('fiche');
  if (!fiche||document.getElementById('ia-btn-'+ticker)) return;
  const wrap=document.createElement('div'); wrap.style.cssText='padding:0 0 8px 0;';
  const btn=document.createElement('button'); btn.id='ia-btn-'+ticker;
  btn.textContent='🤖 Analyse IA';
  btn.style.cssText='width:100%;padding:10px;background:linear-gradient(135deg,#7C3AED,#5b21b6);color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:700;cursor:pointer;transition:opacity .2s;';
  btn.onmouseover=function(){btn.style.opacity='.85';}; btn.onmouseout=function(){btn.style.opacity='1';};
  const res=document.createElement('div'); res.id='ia-res-'+ticker;
  res.style.cssText='display:none;margin-top:6px;padding:12px;background:#f8f5ff;border-left:3px solid #7C3AED;border-radius:0 6px 6px 0;max-height:400px;overflow-y:auto;';
  btn.onclick=function(){runIAAnalysis(ticker,name,scoreData,res,btn);};
  wrap.appendChild(btn); wrap.appendChild(res); fiche.insertBefore(wrap,fiche.firstChild);
}

function _tryInjectIA() {
  const fiche=document.getElementById('fiche');
  if (!fiche||fiche.style.display==='none') return;
  const tkEl=fiche.querySelector('.ftkr')||fiche.querySelector('.logo-s'); if (!tkEl) return;
  const ticker=tkEl.textContent.trim().replace(/\s+.*/,'');
  if (!ticker||ticker.length<2||ticker.length>6) return;
  const nameEl=fiche.querySelector('.fnm')||fiche.querySelector('.logo-m');
  const name=nameEl?nameEl.textContent.trim():ticker;
  const s=typeof S!=='undefined'?S.find(function(x){return x.ticker===ticker;}):null;
  setTimeout(function(){injectIAButton(ticker,name,s);},400);
}
new MutationObserver(_tryInjectIA).observe(document.body,{childList:true,subtree:true});

// ─── PATCH ETF ────────────────────────────────────────────────
var _k=localStorage.getItem('_ant_key'); if(_k) window._ANT=_k;
setTimeout(function(){if(typeof window.fetchLive==='function')window.fetchLive(false);},2500);
setTimeout(function(){
  try {
    if(typeof ETF!=='undefined'&&Array.isArray(ETF)){
      ETF.forEach(function(etf){
        if(!etf||typeof etf!=='object')return;
        if(etf.ter!==undefined&&etf.frais===undefined)etf.frais=etf.ter;
        if(!etf.frais&&etf.frais!==0)etf.frais=0.20;
        if(!Array.isArray(etf.avantages))etf.avantages=etf.desc?[etf.desc]:[];
        if(!Array.isArray(etf.risques))etf.risques=[];
        if(!etf.verdict)etf.verdict=etf.desc||'';
        if(!etf.note)etf.note='B';
        if(!etf.type)etf.type='Capitalisant';
        if(!etf.emetteur)etf.emetteur=etf.name?etf.name.split(' ')[0]:'';
        if(!etf.replication)etf.replication='Synthétique';
        if(!etf.indice)etf.indice=etf.name||'';
      });
      if(typeof buildETF==='function')buildETF();
    }
    _tryInjectIA();
  } catch(e){console.log('[v5.1] patch error:',e.message);}
},3000);

console.log('[live_patch v5.1] OK | prompt:Quality-Investing | cle IA:',!!window._ANT);
