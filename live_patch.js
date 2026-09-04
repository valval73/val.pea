// PEA SCREENER PRO — live_patch.js v5.2
// Prompt IA Quality Investing / Buffett — Décision binaire
// ================================================================

// Ancien mecanisme fetchLive() base sur proxies CORS morts (codetabs,
// thingproxy, allorigins) retire ici -- il ecrasait window.fetchLive
// (defini proprement dans index.html) ET se relancait automatiquement
// a chaque chargement de page via un setTimeout, d'ou le flot d'erreurs
// dans la console a chaque ouverture du site. Les prix sont desormais
// rafraichis cote serveur (refresh_intraday_prices.py, toutes les heures
// en Bourse) -- audit du 04/09/2026.

function getANTKey(){if(window._ANT)return window._ANT;const k=localStorage.getItem('_ant_key');if(k){window._ANT=k;return k;}return null;}
function clearANTKey(){localStorage.removeItem('_ant_key');window._ANT=null;}

function showKeyPrompt(onSave){
  if(document.getElementById('ia-key-modal'))return;
  const ov=document.createElement('div');ov.id='ia-key-modal';
  ov.style.cssText='position:fixed;inset:0;background:rgba(0,0,0,.75);z-index:9999;display:flex;align-items:center;justify-content:center;';
  const box=document.createElement('div');box.style.cssText='background:#0f2540;border-radius:14px;padding:28px;max-width:440px;width:92%;border:1px solid rgba(255,255,255,.1);';
  const t=document.createElement('div');t.style.cssText='font-size:16px;font-weight:700;color:#fff;margin-bottom:6px;';t.textContent='🤖 Clé API Anthropic';
  const s=document.createElement('div');s.style.cssText='font-size:12px;color:#8899aa;margin-bottom:18px;';s.textContent='Pour analyser avec IA + recherche web temps réel';
  const inp=document.createElement('input');inp.id='ant-inp';inp.type='password';inp.placeholder='sk-ant-api03-...';
  inp.style.cssText='width:100%;padding:11px;background:#1a3050;border:1px solid #2a4060;border-radius:8px;color:#fff;font-size:12px;font-family:monospace;box-sizing:border-box;outline:none;';
  const lnk=document.createElement('div');lnk.style.cssText='font-size:11px;color:#8899aa;margin-top:8px;';
  lnk.innerHTML='Stockée localement · <a href="https://console.anthropic.com/settings/keys" target="_blank" style="color:#7C3AED;">Obtenir une clé →</a>';
  const row=document.createElement('div');row.style.cssText='display:flex;gap:10px;margin-top:18px;';
  const bS=document.createElement('button');bS.style.cssText='flex:1;padding:10px;background:#7C3AED;color:#fff;border:none;border-radius:7px;font-weight:700;cursor:pointer;';
  bS.textContent='Activer l’IA';
  const bK=document.createElement('button');bK.style.cssText='padding:10px 16px;background:transparent;color:#8899aa;border:1px solid #2a4060;border-radius:7px;cursor:pointer;';bK.textContent='Plus tard';
  row.appendChild(bS);row.appendChild(bK);
  box.appendChild(t);box.appendChild(s);box.appendChild(inp);box.appendChild(lnk);box.appendChild(row);
  ov.appendChild(box);document.body.appendChild(ov);
  bS.onclick=function(){const k=inp.value.trim();if(k.startsWith('sk-ant')){localStorage.setItem('_ant_key',k);window._ANT=k;ov.remove();if(onSave)onSave(k);}else inp.style.borderColor='#ef4444';};
  bK.onclick=function(){ov.remove();};
}

// ─── ANALYSE IA — PROMPT QUALITY INVESTING / BUFFETT ──────────
async function runIAAnalysis(ticker, name, scoreData, resEl, btn) {
  const key=getANTKey();
  if(!key){showKeyPrompt(function(k){window._ANT=k;runIAAnalysis(ticker,name,scoreData,resEl,btn);});return;}
  btn.disabled=true;btn.textContent='⏳ Analyse...';
  resEl.style.display='block';
  resEl.innerHTML='<div style="color:#7C3AED;padding:8px;font-size:12px;">🔍 Analyse Quality Investing <b>'+name+'</b>...</div>';

  const ctx=scoreData?'Score QARP '+scoreData.qarp+'/100, Grade '+scoreData.grade
    +', Prix '+(scoreData.price||'?')+'€'
    +', PE '+(scoreData.pe||'?')+'x, ROE '+(scoreData.roe||'?')+'%'
    +', Marge '+(scoreData.margin||'?')+'%'
    +', Div '+(scoreData.dy||'?')+'%'
    +', Dette/Eq '+(scoreData.debt||'?')
    +', Beneish '+(scoreData.beneish||'?')
    +', Piotroski '+(scoreData.pio||'?')+'/9':'';

  const NL='\n';
  const prompt='Tu es gérant de portefeuille long terme, Quality Investing / Buffett. Décision pour PEA.'+NL
    +'ACTION : '+name+' ('+ticker+') | PRIX : '+(scoreData&&scoreData.price?scoreData.price:'?')+'€ | '+ctx+NL+NL
    +'RÈGLES ABSOLUES :'+NL
    +'- Zéro résumé de communiqué de presse'+NL
    +'- Chaque affirmation chiffrée et sourced'+NL
    +'- Conclusion BINAIRE : INVESTIR ou PASSER (pas de nuance)'+NL+NL
    +'## VERDICT : [INVESTIR / PASSER / ATTENDRE ZONE]'+NL
    +'(une ligne, sans nuance, avec le prix d\'entrée si ATTENDRE)'+NL+NL
    +'## MOAT — Machine à cash durable ?'+NL
    +'- Avantage concurrentiel : [nom précis + chiffre qui le prouve]'+NL
    +'- Pricing power : marge brute % vs moyenne secteur %'+NL
    +'- Risque disruption 5 ans : faible/moyen/fort + raison'+NL+NL
    +'## VALORISATION — Prix payé ?'+NL
    +'- FCF Yield estimé : [%] → cher/juste/opportunité'+NL
    +'- PE actuel vs historique 10 ans : [X]x vs [Y]x'+NL
    +'- Zone d\'achat optimale : [X€ à Y€]'+NL
    +'- Scénario baissier (-20% résultats) : cours = [Z€]'+NL+NL
    +'## BILAN — Solidité récession ?'+NL
    +'- Dette nette/EBITDA : [x] → safe/limite/danger'+NL
    +'- Dividende couvert par FCF : oui/non'+NL+NL
    +'## CATALYSEURS vs RISQUES'+NL
    +'- Catalyseur #1 : [impact estimé sur résultats %]'+NL
    +'- Catalyseur #2 : [concret]'+NL
    +'- Risque #1 : [probabilité] + [impact si réalisé]'+NL
    +'- Risque #2 : [concret]'+NL+NL
    +'## D�CISION FINALE'+NL
    +'- Action : ACHETER/RENFORCER/CONSERVER/ALLÉGER/VENDRE/PASSER'+NL
    +'- Taille position : [X% du portefeuille PEA]'+NL
    +'- Point d\'entrée : [X€ ou déjà en zone]'+NL
    +'- Objectif 3 ans : [Y€] (+X%)'+NL
    +'- Stop loss logique : [Z€]'+NL+NL
    +'Aucun disclaimer. Structure stricte obligatoire.';

  try {
    const resp=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{'Content-Type':'application/json','x-api-key':key,'anthropic-version':'2023-06-01','anthropic-beta':'web-search-2025-03-05','anthropic-dangerous-direct-browser-access':'true'},
      body:JSON.stringify({model:'claude-sonnet-4-20250514',max_tokens:1200,tools:[{type:'web_search_20250305',name:'web_search'}],messages:[{role:'user',content:prompt}]})
    });
    if(!resp.ok){const e=await resp.json().catch(function(){return{};});throw new Error(e.error&&e.error.message?e.error.message:'HTTP '+resp.status);}
    const d=await resp.json();
    const text=(d.content||[]).filter(function(b){return b.type==='text';}).map(function(b){return b.text;}).join('').trim();
    if(text){
      let html=text
        .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
        .replace(/## ([^\n]+)/g,'<h4 style="color:#1e293b;margin:10px 0 4px;font-size:12px;border-bottom:1px solid #e2e8f0;padding-bottom:3px;">$1</h4>')
        .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
        .split('\n- ').join('<br>• ')
        .split('\n\n').join('</p><p style="margin:6px 0">')
        .split('\n').join('<br>');
      resEl.innerHTML='<div style="line-height:1.6;color:#1e293b;font-size:12px;"><p style="margin:0">'+html+'</p></div>';
    } else {resEl.innerHTML='<div style="color:#888;font-size:12px;">Analyse non disponible</div>';}
  } catch(e){
    if(e.message.indexOf('401')>=0||e.message.indexOf('invalid_api_key')>=0){
      clearANTKey();
      const ed=document.createElement('div');ed.style.cssText='color:#ef4444;font-size:12px;';ed.textContent='Clé invalide. ';
      const rc=document.createElement('a');rc.href='#';rc.style.color='#7C3AED';rc.textContent='Reconfigurer';
      rc.onclick=function(ev){ev.preventDefault();clearANTKey();resEl.style.display='none';btn.disabled=false;btn.textContent='🤖 Analyse IA';};
      ed.appendChild(rc);resEl.innerHTML='';resEl.appendChild(ed);
    } else {resEl.innerHTML='<div style="color:#ef4444;font-size:12px;">Erreur: '+e.message+'</div>';}
  }
  btn.disabled=false;btn.textContent='🤖 Analyse IA';
}

function injectIAButton(ticker,name,scoreData){
  const fiche=document.getElementById('fiche');
  if(!fiche||document.getElementById('ia-btn-'+ticker))return;
  const wrap=document.createElement('div');wrap.style.cssText='padding:0 0 8px 0;';
  const btn=document.createElement('button');btn.id='ia-btn-'+ticker;
  btn.textContent='🤖 Analyse IA';
  btn.style.cssText='width:100%;padding:10px;background:linear-gradient(135deg,#7C3AED,#5b21b6);color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:700;cursor:pointer;transition:opacity .2s;';
  btn.onmouseover=function(){btn.style.opacity='.85';};btn.onmouseout=function(){btn.style.opacity='1';};
  const res=document.createElement('div');res.id='ia-res-'+ticker;
  res.style.cssText='display:none;margin-top:6px;padding:12px;background:#f8f5ff;border-left:3px solid #7C3AED;border-radius:0 6px 6px 0;max-height:420px;overflow-y:auto;';
  btn.onclick=function(){runIAAnalysis(ticker,name,scoreData,res,btn);};
  wrap.appendChild(btn);wrap.appendChild(res);fiche.insertBefore(wrap,fiche.firstChild);
}

function _tryInjectIA(){
  const fiche=document.getElementById('fiche');
  if(!fiche||fiche.style.display==='none')return;
  const tkEl=fiche.querySelector('.ftkr')||fiche.querySelector('.logo-s');if(!tkEl)return;
  const ticker=tkEl.textContent.trim().split(' ')[0].split('\t')[0].trim();
  if(!ticker||ticker.length<2||ticker.length>6)return;
  const nameEl=fiche.querySelector('.fnm')||fiche.querySelector('.logo-m');
  const name=nameEl?nameEl.textContent.trim():ticker;
  const s=typeof S!=='undefined'?S.find(function(x){return x.ticker===ticker;}):null;
  setTimeout(function(){injectIAButton(ticker,name,s);},400);
}
new MutationObserver(_tryInjectIA).observe(document.body,{childList:true,subtree:true});

var _k=localStorage.getItem('_ant_key');if(_k)window._ANT=_k;
// (ancien auto-declenchement fetchLive retire -- cf commentaire plus haut)
setTimeout(function(){
  try{
    if(typeof ETF!=='undefined'&&Array.isArray(ETF)){
      ETF.forEach(function(e){
        if(!e||typeof e!=='object')return;
        if(e.ter!==undefined&&e.frais===undefined)e.frais=e.ter;
        if(!e.frais&&e.frais!==0)e.frais=0.20;
        if(!Array.isArray(e.avantages))e.avantages=e.desc?[e.desc]:[];
        if(!Array.isArray(e.risques))e.risques=[];
        if(!e.verdict)e.verdict=e.desc||'';
        if(!e.note)e.note='B';
        if(!e.type)e.type='Capitalisant';
        if(!e.emetteur)e.emetteur=e.name?e.name.split(' ')[0]:'';
        if(!e.replication)e.replication='Synthétique';
        if(!e.indice)e.indice=e.name||'';
      });
      if(typeof buildETF==='function')buildETF();
    }
    _tryInjectIA();
  }catch(e){console.log('[v5.2] patch error:',e.message);}
},3000);
console.log('[live_patch v5.2] OK | prompt:Quality-Investing | cle IA:',!!window._ANT);

