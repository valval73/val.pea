// LIVE PATCH v2 - fetchLive + IA Anthropic (CORS fix)
window.fetchLive = async function(isAuto) {
  const LS = 'valpea_fetch';
  if (isAuto) { try { if (Date.now() - parseInt(localStorage.getItem(LS)||0) < 15*60*1000) return; } catch(e) {} }
  try { localStorage.setItem(LS, Date.now()); } catch(e) {}
  const liveEl = document.getElementById('live-st');
  if (liveEl) { liveEl.textContent = 'Mise a jour cours...'; liveEl.style.color = '#f59e0b'; }
  try {
    const r = await fetch('https://raw.githubusercontent.com/valval73/val.pea/main/prices.json?t=' + Date.now());
    if (!r.ok) throw new Error('HTTP ' + r.status);
    const data = await r.json();
    let n = 0;
    if (typeof S !== 'undefined') {
      S.forEach(s => {
        const d = data[s.ticker];
        if (d && d.p > 0.05) {
          const fx = (typeof NON_EUR !== 'undefined' && NON_EUR[s.ticker]) || 1;
          s.price = Math.round(d.p / fx * 100) / 100;
          s.chg   = Math.round((d.c || 0) * 100) / 100;
          if (d.h52) s.b52h = Math.round(d.h52 / fx * 100) / 100;
          if (d.l52) s.b52l = Math.round(d.l52 / fx * 100) / 100;
          if (typeof render === 'function') render(s);
          n++;
        }
      });
    }
    const age = data._updated ? Math.round((Date.now()/1000 - data._updated) / 60) : '?';
    if (liveEl) { liveEl.textContent = n + ' cours — ' + age + 'min'; liveEl.style.color = '#22c55e'; }
  } catch(e) {
    if (liveEl) { liveEl.textContent = 'Echec — reessayez'; liveEl.style.color = '#ef4444'; }
  }
};

// Bouton IA Anthropic avec header CORS
function injectIAButton(ticker, name, scoreData) {
  const ficheEl = document.getElementById('fiche');
  if (!ficheEl || document.getElementById('ia-btn-' + ticker)) return;
  const btn = document.createElement('button');
  btn.id = 'ia-btn-' + ticker;
  btn.innerHTML = '🤖 Analyse IA Claude';
  btn.style.cssText = 'display:block;width:100%;margin:6px 0;padding:10px;background:#7C3AED;color:#fff;border:none;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;';
  const res = document.createElement('div');
  res.id = 'ia-res-' + ticker;
  res.style.cssText = 'display:none;margin:6px 0;padding:12px;background:#F5F3FF;border-left:3px solid #7C3AED;border-radius:6px;font-size:12px;line-height:1.65;';
  btn.onclick = async () => {
    btn.disabled = true; btn.innerHTML = '⏳ Analyse...';
    res.style.display = 'block'; res.innerHTML = 'Analyse de <b>' + name + '</b>...';
    try {
      const ctx = scoreData ? 'QARP ' + scoreData.qarp + '/100, Grade ' + scoreData.grade + ', Prix ' + scoreData.price + 'EUR, ROE ' + scoreData.roe + '%, Div ' + scoreData.dy + '%' : '';
      const resp = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': window._ANT || '',
          'anthropic-version': '2023-06-01',
          'anthropic-beta': 'web-search-2025-03-05',
          'anthropic-dangerous-direct-browser-access': 'true'
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514', max_tokens: 500,
          tools: [{ type: 'web_search_20250305', name: 'web_search' }],
          messages: [{ role: 'user', content: 'Analyse ' + name + ' (' + ticker + ') pour PEA. ' + ctx + '. 5 points: 1)Catalyseurs 2)Risques 3)Valorisation 4)Signal 5)Horizon. Direct.' }]
        })
      });
      if (!resp.ok) throw new Error(resp.status + ': ' + (await resp.text()).substring(0,80));
      const d = await resp.json();
      const text = (d.content||[]).filter(b=>b.type==='text').map(b=>b.text).join('');
      res.innerHTML = text ? text.replace(/\n/g,'<br>') : 'Non disponible';
    } catch(e) { res.innerHTML = '<b style="color:red">Erreur:</b> ' + e.message; }
    btn.disabled = false; btn.innerHTML = '🤖 Analyse IA Claude';
  };
  ficheEl.insertBefore(res, ficheEl.firstChild);
  ficheEl.insertBefore(btn, ficheEl.firstChild);
}

// Observer fiche
const ficheObs = new MutationObserver(() => {
  const fiche = document.getElementById('fiche');
  if (!fiche || fiche.style.display === 'none') return;
  const tickerEl = fiche.querySelector('.logo-s');
  if (!tickerEl) return;
  const ticker = tickerEl.textContent.trim().split(' ')[0];
  const nameEl = fiche.querySelector('.logo-m, h2');
  const name = nameEl ? nameEl.textContent.trim() : ticker;
  if (ticker && /^[A-Z]{2,6}$/.test(ticker)) {
    const s = typeof S !== 'undefined' ? S.find(x => x.ticker === ticker) : null;
    setTimeout(() => injectIAButton(ticker, name, s), 400);
  }
});

ficheObs.observe(document.body, { childList: true, subtree: true });
setTimeout(() => { if (typeof fetchLive === 'function') fetchLive(false); }, 1500);
console.log('live_patch v2 OK');
