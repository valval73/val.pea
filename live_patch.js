// ====================================================
// LIVE PATCH - fetchLive via GitHub Actions prices.json
// + Bouton analyse IA Anthropic par action
// ====================================================

// Override fetchLive - lit prices.json genere par GitHub Actions
window.fetchLive = async function(isAuto) {
  const LS = 'valpea_fetch';
  if (isAuto) {
    try { if (Date.now() - parseInt(localStorage.getItem(LS)||0) < 15*60*1000) return; } catch(e) {}
  }
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
    const msg = n + ' cours — ' + age + 'min';
    if (liveEl) { liveEl.textContent = msg; liveEl.style.color = '#22c55e'; }
    console.log('fetchLive: ' + n + ' cours mis a jour depuis GitHub Actions (age: ' + age + 'min)');
  } catch(e) {
    if (liveEl) { liveEl.textContent = 'Echec — reessayez'; liveEl.style.color = '#ef4444'; }
    console.error('fetchLive error:', e);
  }
};

// Bouton analyse IA Anthropic - ajoute dans la fiche action
function addIAButton(ticker, name) {
  const existing = document.getElementById('ia-btn-' + ticker);
  if (existing) return;

  const fiche = document.getElementById('fiche');
  if (!fiche) return;

  const btn = document.createElement('button');
  btn.id = 'ia-btn-' + ticker;
  btn.textContent = 'Analyse IA';
  btn.style.cssText = 'margin:8px 0;padding:8px 16px;background:#7C3AED;color:#fff;border:none;border-radius:6px;font-size:12px;font-weight:700;cursor:pointer;width:100%;letter-spacing:0.5px;';

  const resultDiv = document.createElement('div');
  resultDiv.id = 'ia-result-' + ticker;
  resultDiv.style.cssText = 'margin-top:8px;padding:10px;background:#F5F3FF;border-radius:6px;font-size:12px;line-height:1.6;display:none;';

  btn.onclick = async () => {
    btn.disabled = true;
    btn.textContent = 'Analyse en cours...';
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = '<i>L'IA analyse ' + name + '...</i>';

    try {
      const s = (typeof S !== 'undefined') ? S.find(x => x.ticker === ticker) : null;
      const ctx = s ? 'Prix: ' + s.price + 'EUR, QARP: ' + s.qarp + '/100, Grade: ' + s.grade + ', Dividende: ' + (s.dy||'?') + '%, ROE: ' + (s.roe||'?') + '%, Beneish: ' + (s.beneish||'?') : '';

      const res = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 600,
          tools: [{ type: 'web_search_20250305', name: 'web_search' }],
          messages: [{
            role: 'user',
            content: 'Analyse rapide de ' + name + ' (' + ticker + '.PA) pour un investisseur PEA. ' + ctx + '. En 5 points concis: 1) Catalyseurs actuels, 2) Risques principaux, 3) Valorisation vs pairs, 4) Signal achat/vente/attendre, 5) Horizon recommande. Sois direct et actionnable. Pas de disclaimers.'
          }]
        })
      });
      const d = await res.json();
      const text = (d.content||[]).filter(b => b.type === 'text').map(b => b.text).join('');
      resultDiv.innerHTML = text.replace(/
/g, '<br>') || 'Analyse non disponible';
    } catch(e) {
      resultDiv.innerHTML = 'Erreur: ' + e.message;
    }
    btn.disabled = false;
    btn.textContent = 'Analyse IA';
  };

  // Inserer le bouton dans la fiche
  const analyseSection = fiche.querySelector('[id="pg-sc"]') || fiche;
  fiche.insertBefore(btn, fiche.firstChild);
  fiche.insertBefore(resultDiv, btn.nextSibling);
}

// Observer les changements de fiche pour injecter le bouton IA
const ficheObserver = new MutationObserver(() => {
  const fiche = document.getElementById('fiche');
  if (!fiche || fiche.style.display === 'none') return;
  // Trouver le ticker de l'action affichee
  const tickerEl = fiche.querySelector('.logo-s, [class*="ticker"]');
  if (tickerEl) {
    const ticker = tickerEl.textContent.trim().split(' ')[0];
    const nameEl = fiche.querySelector('h2, .logo-m, [class*="name"]');
    const name = nameEl ? nameEl.textContent.trim() : ticker;
    if (ticker && ticker.length <= 6) addIAButton(ticker, name);
  }
});

// Lancer le patch
document.addEventListener('DOMContentLoaded', () => {
  ficheObserver.observe(document.body, { childList: true, subtree: true });
  // Lancer fetchLive automatiquement au chargement
  setTimeout(() => {
    if (typeof fetchLive === 'function') fetchLive(false);
  }, 1500);
  console.log('live_patch.js charge - fetchLive et IA Anthropic actifs');
});

// Si DOM deja pret
if (document.readyState !== 'loading') {
  ficheObserver.observe(document.body, { childList: true, subtree: true });
  setTimeout(() => {
    if (typeof fetchLive === 'function') fetchLive(false);
  }, 1500);
  console.log('live_patch.js charge (DOM ready) - fetchLive et IA actifs');
}
