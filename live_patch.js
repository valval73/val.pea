// ================================================================
// PEA SCREENER PRO — live_patch.js v3
// Prix live via corsproxy.io + Analyse IA Anthropic par action
// ================================================================

const PROXY = 'https://corsproxy.io/?';
const YF_BASE = 'https://query1.finance.yahoo.com/v8/finance/chart/';

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

// ─── FETCH PRIX LIVE via corsproxy ──────────────────────────────
async function fetchOnePrice(yfSym) {
  const url = PROXY + encodeURIComponent(YF_BASE + yfSym + '?range=1d&interval=5m');
  const r = await fetch(url);
  if (!r.ok) throw new Error(r.status);
  const d = await r.json();
  const m = d?.chart?.result?.[0]?.meta;
  if (!m || !m.regularMarketPrice) return null;
  return {
    p: Math.round(m.regularMarketPrice * 100) / 100,
    c: Math.round((m.regularMarketPrice - m.chartPreviousClose) / m.chartPreviousClose * 10000) / 100,
    h52: Math.round((m.fiftyTwoWeekHigh || 0) * 100) / 100,
    l52: Math.round((m.fiftyTwoWeekLow || 0) * 100) / 100
  };
}

window.fetchLive = async function(isAuto) {
  const LS = 'valpea_fetch';
  if (isAuto) {
    try { if (Date.now() - parseInt(localStorage.getItem(LS)||0) < 10*60*1000) return; } catch(e) {}
  }
  try { localStorage.setItem(LS, Date.now()); } catch(e) {}
  const liveEl = document.getElementById('live-st');
  const upd = (msg, col) => { if(liveEl) { liveEl.textContent = msg; liveEl.style.color = col; } };
  upd('Mise à jour cours...', '#f59e0b');

  const tickers = typeof S !== 'undefined' ? S.map(s => s.ticker).filter(t => YF_MAP[t]) : Object.keys(YF_MAP);
  let ok = 0, fail = 0;
  const BATCH = 8;

  for (let i = 0; i < tickers.length; i += BATCH) {
    const batch = tickers.slice(i, i + BATCH);
    await Promise.all(batch.map(async ticker => {
      try {
        const data = await fetchOnePrice(YF_MAP[ticker]);
        if (data && typeof S !== 'undefined') {
          const s = S.find(x => x.ticker === ticker);
          if (s) {
            s.price = data.p; s.chg = data.c;
            if (data.h52) s.b52h = data.h52;
            if (data.l52) s.b52l = data.l52;
            if (typeof render === 'function') render(s);
            ok++;
          }
        }
      } catch(e) { fail++; }
    }));
    upd(ok + '/' + tickers.length + ' cours...', '#f59e0b');
    if (i + BATCH < tickers.length) await new Promise(r => setTimeout(r, 300));
  }

  const now = new Date().toLocaleTimeString('fr-FR', {hour:'2-digit', minute:'2-digit'});
  upd(ok + ' cours live · ' + now, '#22c55e');
  console.log('fetchLive: ' + ok + ' OK, ' + fail + ' fail');
};

// ─── BOUTON IA ANTHROPIC ────────────────────────────────────────
function getANTKey() {
  if (window._ANT) return window._ANT;
  const k = localStorage.getItem('_ant_key');
  if (k) { window._ANT = k; return k; }
  return null;
}

function showKeyPrompt(onSave) {
  if (document.getElementById('ia-key-modal')) return;
  const m = document.createElement('div');
  m.id = 'ia-key-modal';
  m.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.75);z-index:9999;display:flex;align-items:center;justify-content:center;';
  m.innerHTML = `<div style="background:#0f2540;border-radius:14px;padding:28px;max-width:440px;width:92%;border:1px solid rgba(255,255,255,.1);">
    <div style="font-size:16px;font-weight:700;color:#fff;margin-bottom:6px;">🤖 Clé API Anthropic</div>
    <div style="font-size:12px;color:#8899aa;margin-bottom:18px;">Pour analyser les actions avec IA + recherche web temps réel</div>
    <input id="ant-inp" type="password" placeholder="sk-ant-api03-..." style="width:100%;padding:11px;background:#1a3050;border:1px solid #2a4060;border-radius:8px;color:#fff;font-size:12px;font-family:monospace;box-sizing:border-box;outline:none;" />
    <div style="font-size:11px;color:#8899aa;margin-top:8px;">Stockée localement dans votre navigateur uniquement · <a href="https://console.anthropic.com" target="_blank" style="color:#7C3AED;">Obtenir une clé</a></div>
    <div style="display:flex;gap:10px;margin-top:18px;">
      <button id="ant-save" style="flex:1;padding:10px;background:#7C3AED;color:#fff;border:none;border-radius:7px;font-weight:700;cursor:pointer;font-size:13px;">Activer l'IA</button>
      <button id="ant-skip" style="padding:10px 16px;background:transparent;color:#8899aa;border:1px solid #2a4060;border-radius:7px;cursor:pointer;font-size:12px;">Plus tard</button>
    </div>
  </div>`;
  document.body.appendChild(m);
  document.getElementById('ant-save').onclick = () => {
    const k = document.getElementById('ant-inp').value.trim();
    if (k.startsWith('sk-ant')) {
      localStorage.setItem('_ant_key', k); window._ANT = k;
      m.remove(); if(onSave) onSave(k);
    } else { document.getElementById('ant-inp').style.borderColor='#ef4444'; }
  };
  document.getElementById('ant-skip').onclick = () => m.remove();
}

async function runIAAnalysis(ticker, name, scoreData, resEl, btn) {
  const key = getANTKey();
  if (!key) { showKeyPrompt(k => { window._ANT=k; runIAAnalysis(ticker,name,scoreData,resEl,btn); }); return; }

  btn.disabled = true; btn.textContent = '⏳ Analyse en cours...';
  resEl.style.display = 'block';
  resEl.innerHTML = '<div style="color:#7C3AED;padding:8px;">Analyse de <b>' + name + '</b> avec recherche web...</div>';

  const ctx = scoreData ?
    'Score QARP ' + scoreData.qarp + '/100, Grade ' + scoreData.grade +
    ', Prix actuel ' + (scoreData.price||'?') + '€' +
    ', ROE ' + (scoreData.roe||'?') + '%, Dividende ' + (scoreData.dy||'?') + '%' +
    ', Beneish M-Score ' + (scoreData.beneish||'?') : '';

  try {
    const resp = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': key,
        'anthropic-version': '2023-06-01',
        'anthropic-beta': 'web-search-2025-03-05',
        'anthropic-dangerous-direct-browser-access': 'true'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 600,
        tools: [{ type: 'web_search_20250305', name: 'web_search' }],
        messages: [{
          role: 'user',
          content: 'Analyse rapide de ' + name + ' (' + ticker + ') pour portefeuille PEA. ' + ctx + '.\n\nDonne en 5 points concis (2 lignes max chacun):\n1) Actualité récente et catalyseurs\n2) Risques principaux\n3) Valorisation vs secteur (P/E, P/B)\n4) Signal: ACHETER / ATTENDRE / VENDRE et pourquoi\n5) Horizon recommandé\n\nStyle cabinet d\'analyse. Direct et actionnable. Pas de disclaimers.'
        }]
      })
    });
    if (!resp.ok) {
      const err = await resp.json();
      throw new Error(err.error?.message || resp.status);
    }
    const d = await resp.json();
    const text = (d.content||[]).filter(b=>b.type==='text').map(b=>b.text).join('').trim();
    resEl.innerHTML = text
      ? '<div style="line-height:1.7;color:#1a1a2e;">' + text.replace(/
/g,'<br>') + '</div>'
      : '<div style="color:#888;">Analyse non disponible</div>';
  } catch(e) {
    if (e.message.includes('401') || e.message.includes('invalid')) {
      localStorage.removeItem('_ant_key'); window._ANT = null;
      resEl.innerHTML = '<div style="color:#ef4444;">Clé invalide. <a href="#" onclick="localStorage.removeItem('_ant_key');location.reload();">Reconfigurer</a></div>';
    } else {
      resEl.innerHTML = '<div style="color:#ef4444;">Erreur: ' + e.message + '</div>';
    }
  }
  btn.disabled = false; btn.textContent = '🤖 Analyse IA';
}

function injectIAButton(ticker, name, scoreData) {
  const fiche = document.getElementById('fiche');
  if (!fiche || document.getElementById('ia-btn-' + ticker)) return;

  const wrap = document.createElement('div');
  wrap.style.cssText = 'padding:0 0 6px 0;';

  const btn = document.createElement('button');
  btn.id = 'ia-btn-' + ticker;
  btn.textContent = '🤖 Analyse IA';
  btn.style.cssText = 'width:100%;padding:10px;background:linear-gradient(135deg,#7C3AED,#5b21b6);color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:700;cursor:pointer;letter-spacing:.3px;transition:opacity.2s;';
  btn.onmouseover = () => btn.style.opacity = '.85';
  btn.onmouseout = () => btn.style.opacity = '1';

  const res = document.createElement('div');
  res.id = 'ia-res-' + ticker;
  res.style.cssText = 'display:none;margin-top:6px;padding:12px;background:#f8f5ff;border-left:3px solid #7C3AED;border-radius:0 6px 6px 0;font-size:12px;max-height:300px;overflow-y:auto;';

  btn.onclick = () => runIAAnalysis(ticker, name, scoreData, res, btn);
  wrap.appendChild(btn);
  wrap.appendChild(res);
  fiche.insertBefore(wrap, fiche.firstChild);
}

// ─── OBSERVER FICHE ─────────────────────────────────────────────
const _ficheObs = new MutationObserver(() => {
  const fiche = document.getElementById('fiche');
  if (!fiche || fiche.style.display === 'none') return;
  const tickerEl = fiche.querySelector('.logo-s');
  if (!tickerEl) return;
  const ticker = tickerEl.textContent.trim().replace(/\s+.*/, '');
  if (!ticker || ticker.length < 2 || ticker.length > 6) return;
  const nameEl = fiche.querySelector('.logo-m');
  const name = nameEl ? nameEl.textContent.trim() : ticker;
  const s = typeof S !== 'undefined' ? S.find(x => x.ticker === ticker) : null;
  setTimeout(() => injectIAButton(ticker, name, s), 400);
});
_ficheObs.observe(document.body, { childList: true, subtree: true });

// ─── INIT ───────────────────────────────────────────────────────
// Charger clé en mémoire
const _k = localStorage.getItem('_ant_key');
if (_k) window._ANT = _k;

// Lancer fetchLive au chargement (avec délai pour laisser le screener s'initialiser)
setTimeout(() => {
  if (typeof window.fetchLive === 'function') window.fetchLive(false);
}, 2000);

console.log('live_patch v3 OK | IA key:', !!window._ANT, '| fetchLive: corsproxy');
