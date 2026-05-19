// ================================================================
// PEA SCREENER PRO — live_patch.js v4.1
// Prix live multi-proxy + Analyse IA Anthropic
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
  const targetUrl = YF_BASE + yfSym + '?range=1d&interval=5m';
  const order = [_activeProxyIdx, ...PROXIES.map((_,i)=>i).filter(i=>i!==_activeProxyIdx)];
  for (const idx of order) {
    try {
      const r = await fetch(PROXIES[idx](targetUrl), { signal: AbortSignal.timeout(8000) });
      if (!r.ok) continue;
      const d = await r.json();
      const m = d?.chart?.result?.[0]?.meta;
      if (!m || !m.regularMarketPrice) continue;
      _activeProxyIdx = idx;
      return {
        p: Math.round(m.regularMarketPrice * 100) / 100,
        c: Math.round((m.regularMarketPrice - m.chartPreviousClose) / m.chartPreviousClose * 10000) / 100,
        h52: Math.round((m.fiftyTwoWeekHigh || 0) * 100) / 100,
        l52: Math.round((m.fiftyTwoWeekLow || 0) * 100) / 100
      };
    } catch(e) {}
  }
  return null;
}

window.fetchLive = async function(isAuto) {
  const LS = 'valpea_fetch';
  if (isAuto) {
    try { if (Date.now() - parseInt(localStorage.getItem(LS)||0) < 15*60*1000) return; } catch(e) {}
  }
  try { localStorage.setItem(LS, Date.now()); } catch(e) {}
  const liveEl = document.getElementById('live-st');
  const upd = (msg, col) => { if(liveEl) { liveEl.textContent=msg; liveEl.style.color=col||'#f59e0b'; } };
  upd('Connexion...', '#f59e0b');
  const tickers = typeof S !== 'undefined' ? S.map(s=>s.ticker).filter(t=>YF_MAP[t]) : Object.keys(YF_MAP);
  let ok = 0, fail = 0;
  for (let i = 0; i < tickers.length; i += 6) {
    await Promise.all(tickers.slice(i,i+6).map(async ticker => {
      try {
        const data = await fetchOnePrice(YF_MAP[ticker]);
        if (data && typeof S !== 'undefined') {
          const s = S.find(x=>x.ticker===ticker);
          if (s) {
            s.price=data.p; s.chg=data.c;
            if (data.h52>0) s.b52h=data.h52;
            if (data.l52>0) s.b52l=data.l52;
            if (typeof render==='function') render(s);
            ok++;
          }
        }
      } catch(e) { fail++; }
    }));
    upd(ok+'/'+tickers.length+' cours...','#f59e0b');
    if (i+6 < tickers.length) await new Promise(r=>setTimeout(r,400));
  }
  const now = new Date().toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit'});
  upd(ok>0 ? ok+' cours live · '+now : 'Hors marché · données statiques', ok>0?'#22c55e':'#6b7280');
  console.log('[v4.1] '+ok+' OK, '+fail+' fail, proxy#'+_activeProxyIdx);
};

function getANTKey() {
  if (window._ANT) return window._ANT;
  const k = localStorage.getItem('_ant_key');
  if (k) { window._ANT=k; return k; }
  return null;
}

function showKeyPrompt(onSave) {
  if (document.getElementById('ia-key-modal')) return;
  const m = document.createElement('div');
  m.id = 'ia-key-modal';
  m.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.75);z-index:9999;display:flex;align-items:center;justify-content:center;';
  const box = document.createElement('div');
  box.style.cssText = 'background:#0f2540;border-radius:14px;padding:28px;max-width:440px;width:92%;border:1px solid rgba(255,255,255,.1);';
  box.innerHTML = '<div style="font-size:16px;font-weight:700;color:#fff;margin-bottom:6px;">🤖 Clé API Anthropic</div>'
    + '<div style="font-size:12px;color:#8899aa;margin-bottom:18px;">Pour analyser avec IA + recherche web temps réel</div>'
    + '<input id="ant-inp" type="password" placeholder="sk-ant-api03-..." style="width:100%;padding:11px;background:#1a3050;border:1px solid #2a4060;border-radius:8px;color:#fff;font-size:12px;font-family:monospace;box-sizing:border-box;outline:none;" />'
    + '<div style="font-size:11px;color:#8899aa;margin-top:8px;">Stockée localement · <a href="https://console.anthropic.com" target="_blank" style="color:#7C3AED;">Obtenir une clé</a></div>'
    + '<div style="display:flex;gap:10px;margin-top:18px;">'
    + '<button id="ant-save" style="flex:1;padding:10px;background:#7C3AED;color:#fff;border:none;border-radius:7px;font-weight:700;cursor:pointer;">Activer l’IA</button>'
    + '<button id="ant-skip" style="padding:10px 16px;background:transparent;color:#8899aa;border:1px solid #2a4060;border-radius:7px;cursor:pointer;">Plus tard</button>'
    + '</div>';
  m.appendChild(box);
  document.body.appendChild(m);
  document.getElementById('ant-save').onclick = function() {
    var k = document.getElementById('ant-inp').value.trim();
    if (k.startsWith('sk-ant')) { localStorage.setItem('_ant_key',k); window._ANT=k; m.remove(); if(onSave) onSave(k); }
    else document.getElementById('ant-inp').style.borderColor='#ef4444';
  };
  document.getElementById('ant-skip').onclick = function() { m.remove(); };
}

async function runIAAnalysis(ticker, name, scoreData, resEl, btn) {
  var key = getANTKey();
  if (!key) { showKeyPrompt(function(k){ window._ANT=k; runIAAnalysis(ticker,name,scoreData,resEl,btn); }); return; }
  btn.disabled=true; btn.textContent='⏳ Analyse...';
  resEl.style.display='block';
  resEl.innerHTML='<div style="color:#7C3AED;padding:8px;font-size:12px;">🔍 Recherche <b>'+name+'</b>...</div>';
  var ctx = scoreData ? 'Score QARP '+scoreData.qarp+'/100, Grade '+scoreData.grade+', Prix '+(scoreData.price||'?')+'€, ROE '+(scoreData.roe||'?')+'%, Div '+(scoreData.dy||'?')+'%, Beneish '+(scoreData.beneish||'?') : '';
  var prompt = 'Analyse rapide de '+name+' ('+ticker+') PEA. '+ctx+'.'
    + '\n\n5 points concis:'
    + '\n1) Actualité récente et catalyseurs'
    + '\n2) Risques principaux'
    + '\n3) Valorisation vs secteur'
    + '\n4) Signal: ACHETER / ATTENDRE / VENDRE'
    + '\n5) Horizon recommandé'
    + '\n\nStyle cabinet, direct, sans disclaimers.';
  try {
    var resp = await fetch('https://api.anthropic.com/v1/messages', {
      method:'POST',
      headers:{'Content-Type':'application/json','x-api-key':key,'anthropic-version':'2023-06-01','anthropic-beta':'web-search-2025-03-05','anthropic-dangerous-direct-browser-access':'true'},
      body: JSON.stringify({model:'claude-sonnet-4-20250514',max_tokens:700,tools:[{type:'web_search_20250305',name:'web_search'}],messages:[{role:'user',content:prompt}]})
    });
    if (!resp.ok) { var e=await resp.json().catch(function(){return{};}); throw new Error(e.error&&e.error.message?e.error.message:'HTTP '+resp.status); }
    var d = await resp.json();
    var text = (d.content||[]).filter(function(b){return b.type==='text';}).map(function(b){return b.text;}).join('').trim();
    if (text) {
      var html = text.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\n\n/g,'</p><p>').replace(/\n/g,'<br>');
      resEl.innerHTML='<div style="line-height:1.7;color:#1a1a2e;font-size:12px;"><p>'+html+'</p></div>';
    } else { resEl.innerHTML='<div style="color:#888;font-size:12px;">Analyse non disponible</div>'; }
  } catch(e) {
    if (e.message.indexOf('401')>=0||e.message.indexOf('invalid_api_key')>=0) {
      localStorage.removeItem('_ant_key'); window._ANT=null;
      resEl.innerHTML='<div style="color:#ef4444;font-size:12px;">Clé invalide. <a href="#" onclick="localStorage.removeItem('_ant_key');window._ANT=null;location.reload();" style="color:#7C3AED;">Reconfigurer</a></div>';
    } else { resEl.innerHTML='<div style="color:#ef4444;font-size:12px;">Erreur: '+e.message+'</div>'; }
  }
  btn.disabled=false; btn.textContent='🤖 Analyse IA';
}

function injectIAButton(ticker, name, scoreData) {
  var fiche = document.getElementById('fiche');
  if (!fiche||document.getElementById('ia-btn-'+ticker)) return;
  var wrap=document.createElement('div'); wrap.style.cssText='padding:0 0 8px 0;';
  var btn=document.createElement('button'); btn.id='ia-btn-'+ticker;
  btn.textContent='🤖 Analyse IA';
  btn.style.cssText='width:100%;padding:10px;background:linear-gradient(135deg,#7C3AED,#5b21b6);color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:700;cursor:pointer;letter-spacing:.3px;transition:opacity .2s;';
  btn.onmouseover=function(){btn.style.opacity='.85';};
  btn.onmouseout=function(){btn.style.opacity='1';};
  var res=document.createElement('div'); res.id='ia-res-'+ticker;
  res.style.cssText='display:none;margin-top:6px;padding:12px;background:#f8f5ff;border-left:3px solid #7C3AED;border-radius:0 6px 6px 0;max-height:320px;overflow-y:auto;';
  btn.onclick=function(){runIAAnalysis(ticker,name,scoreData,res,btn);};
  wrap.appendChild(btn); wrap.appendChild(res); fiche.insertBefore(wrap,fiche.firstChild);
}

var _ficheObs = new MutationObserver(function(){
  var fiche=document.getElementById('fiche');
  if (!fiche||fiche.style.display==='none') return;
  var tickerEl=fiche.querySelector('.logo-s'); if (!tickerEl) return;
  var ticker=tickerEl.textContent.trim().replace(/\s+.*/,'');
  if (!ticker||ticker.length<2||ticker.length>6) return;
  var nameEl=fiche.querySelector('.logo-m');
  var name=nameEl?nameEl.textContent.trim():ticker;
  var s=typeof S!=='undefined'?S.find(function(x){return x.ticker===ticker;}):null;
  setTimeout(function(){injectIAButton(ticker,name,s);},400);
});
_ficheObs.observe(document.body,{childList:true,subtree:true});

var _k=localStorage.getItem('_ant_key'); if (_k) window._ANT=_k;
setTimeout(function(){if (typeof window.fetchLive==='function') window.fetchLive(false);},2500);
console.log('[live_patch v4.1] OK | cle IA:',!!window._ANT,'| proxies:',PROXIES.length);
