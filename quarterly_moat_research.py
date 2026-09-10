#!/usr/bin/env python3
"""
VAL.PEA -- Recherche trimestrielle de la grille moat (12 criteres notes,
methode SCORE FONDA) pour toutes les actions Grade A.

Separe du mail hebdomadaire (09/09/2026) : le moat d'une entreprise
(modele economique, position concurrentielle, confiance du management)
ne change pas d'une semaine a l'autre, contrairement au prix ou au DCF.
Faire tourner cette recherche chaque semaine, plafonnee a 10 actions,
etait a la fois inutile et trop lent pour couvrir tout l'univers Grade A.

Ce script tourne une fois par trimestre, traite TOUTES les actions
Grade A qui n'ont jamais ete evaluees ou dont l'evaluation a echoue
(tout a null) -- sans plafond artificiel.

Regle d'honnetete stricte : une grande valeur connue et documentee doit
normalement avoir 10+ criteres sur 12 renseignes (verifie en conditions
reelles sur Carrefour le 09/09/2026 : 11/12 trouves avec 3 recherches
simples). null reste une reponse honnete pour un critere genuinement
introuvable, mais ne doit pas etre la reponse par defaut.
"""
import re, json, os, sys, time
import urllib.request as ur
from datetime import datetime, timedelta

ANTHROPIC_KEY = (os.environ.get('ANTHROPIC_API_KEY') or '').strip()
print(f"ANTHROPIC: {'✅' if ANTHROPIC_KEY else '❌ MANQUANT'}")

MOAT_CRITERIA_LABELS = [
    "Modele economique clair", "Produits essentiels", "Achats reguliers",
    "Base clients large/diversifiee", "Attachement client / cout de changement",
    "Effet de reseau", "Leadership sectoriel", "Avantage competitif durable",
    "Pricing power", "Potentiel de croissance", "Faible dependance tech externe",
    "Management aligne actionnaires"
]

def parse_stocks(datajs_content):
    stocks = []
    seen = set()
    for m in re.finditer(r"\{ticker:'([^']+)'(.*?)(?=\n\n\{ticker:|\n\n\];)", datajs_content, re.DOTALL):
        ticker = m.group(1)
        if ticker in seen: continue
        seen.add(ticker)
        block = m.group(0)
        def gn(k, d=0.0):
            mx = re.search(r'\b' + k + r':([-\d.]+)', block)
            return float(mx.group(1)) if mx else d
        def gs(k, d=''):
            mx = re.search(r"\b" + k + r":'([^']*)'", block)
            return mx.group(1) if mx else d

        score = gs('score')
        if score != 'A':
            continue

        moat_m = re.search(r'moatChk:\[([^\]]*)\]', block)
        moat_pct = None
        moat_answered = 0
        moat_attempted = moat_m is not None
        if moat_m:
            vals = [x.strip() for x in moat_m.group(1).split(',') if x.strip() != '']
            nums = []
            for v in vals:
                try: nums.append(float(v))
                except: pass
            if nums:
                moat_answered = len(nums)
                moat_pct = round(sum(nums)/len(nums)*100)

        date_m = re.search(r"moatDate:'([\d-]+)'", block)
        moat_date = date_m.group(1) if date_m else None

        stocks.append({
            'ticker': ticker, 'name': gs('name'), 'sector': gs('sector'),
            'moat_pct': moat_pct, 'moat_answered': moat_answered,
            'moat_attempted': moat_attempted, 'moat_date': moat_date,
        })
    return stocks

def research_moat(s):
    """Recherche reelle (web search active) des 12 criteres de la grille
    moat -- prompt valide en conditions reelles sur Carrefour le
    09/09/2026 (recherche manuelle : 11/12 criteres trouves en quelques
    recherches simples). Encourage une evaluation genuine pour les
    grandes valeurs connues plutot qu'un reflexe de prudence excessive."""
    if not ANTHROPIC_KEY: return None
    criteres_txt = '\n'.join(f"{i+1}. {c}" for i, c in enumerate(MOAT_CRITERIA_LABELS))
    prompt = (f"Tu es analyste actions experimente. Utilise l'outil de recherche web -- fais "
              f"PLUSIEURS recherches reelles (au moins 3-4) -- sur {s['name']} ({s['ticker']}, "
              f"cotee a Paris) : son modele economique, son dernier rapport annuel ou presentation "
              f"investisseurs, sa position concurrentielle, des articles d'analystes, qui dirige "
              f"l'entreprise et si le conseil d'administration lui renouvelle sa confiance.\n\n"
              f"Pour CHACUN des 12 criteres suivants, donne ton evaluation d'analyste en te basant "
              f"sur ce que tu sais de l'entreprise ET ce que tu trouves en cherchant :\n{criteres_txt}\n\n"
              f"Note : 1 = Bien, 0.5 = Moyen, 0 = Pas bien. Une entreprise connue et documentee "
              f"(grande capitalisation, leader sectoriel) doit pouvoir etre evaluee sur la plupart "
              f"des criteres -- ne mets null QUE pour une entreprise vraiment tres peu documentee "
              f"ou un critere genuinement impossible a estimer meme approximativement. Pour une "
              f"grande valeur connue, avoir 10+ criteres sur 12 renseignes est l'attendu normal, "
              f"pas l'exception -- ne sois pas excessivement prudent.\n\n"
              f"Cherche d'abord activement (plusieurs recherches), reflechis a ce que tu trouves, "
              f"PUIS termine ta reponse par un bloc JSON strict avec ce format exact "
              f"(rien apres ce bloc) :\n"
              f'{{"scores":[note1,note2,...note12],"notes":["justification courte 1",...],"sources":["url ou nom de source",...]}}')
    try:
        payload = json.dumps({
            'model': 'claude-sonnet-5', 'max_tokens': 1500,
            'tools': [{'type': 'web_search_20250305', 'name': 'web_search', 'max_uses': 8}],
            'messages': [{'role': 'user', 'content': prompt}]
        }).encode()
        req = ur.Request('https://api.anthropic.com/v1/messages', data=payload,
            headers={'Content-Type': 'application/json', 'x-api-key': ANTHROPIC_KEY, 'anthropic-version': '2023-06-01'})
        with ur.urlopen(req, timeout=90) as r:
            d = json.loads(r.read())
        text_blocks = [b['text'] for b in d.get('content', []) if b.get('type') == 'text']
        full_text = ' '.join(text_blocks)

        start = full_text.rfind('{"scores"')
        if start == -1:
            start = full_text.find('{')
        parsed = None
        if start != -1:
            depth = 0
            for i in range(start, len(full_text)):
                if full_text[i] == '{': depth += 1
                elif full_text[i] == '}':
                    depth -= 1
                    if depth == 0:
                        try:
                            parsed = json.loads(full_text[start:i+1])
                        except Exception:
                            parsed = None
                        break
        if not parsed: return None
        scores = parsed.get('scores', [])
        notes = parsed.get('notes', [])
        sources = parsed.get('sources', [])
        if len(scores) != 12: return None
        clean_scores = [float(v) if v is not None and str(v).lower() != 'null' else None for v in scores]
        return {'scores': clean_scores, 'notes': notes[:12], 'sources': sources[:5]}
    except Exception as e:
        print(f"  Recherche moat {s['ticker']}: {e}")
        return None

def patch_moat_scores(results):
    if not results: return 0
    today = datetime.now().strftime('%Y-%m-%d')
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    for ticker, r in results.items():
        tp = content.find(f"ticker:'{ticker}'")
        if tp == -1: continue
        np_ = content.find("ticker:'", tp + 1)
        block_end = np_ if np_ > -1 else len(content)
        block = content[tp:block_end]
        vals_str = ','.join('null' if v is None else str(v) for v in r['scores'])
        new_field = f"moatChk:[{vals_str}],moatDate:'{today}'"
        if 'moatChk:[' in block:
            # Retire l'ancien moatDate s'il existe, avant de le re-ecrire
            block = re.sub(r",?moatDate:'[^']*'", '', block, count=1)
            nb = re.sub(r"moatChk:\[[^\]]*\]", new_field, block, count=1)
        else:
            nb = block.replace("score:'", new_field + ",score:'", 1)
        if nb != block:
            block = nb
            updated += 1
        content = content[:tp] + block + content[block_end:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Grille moat ecrite dans data.js pour {updated} action(s)")
    return updated


if __name__ == '__main__':
    if not os.path.exists('data.js'):
        print('❌ data.js introuvable'); sys.exit(1)
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    stocks = parse_stocks(content)
    print(f'{len(stocks)} actions Grade A au total')

    un_an = datetime.now() - timedelta(days=365)
    def est_perime(s):
        if not s['moat_date']: return False
        try:
            return datetime.strptime(s['moat_date'], '%Y-%m-%d') < un_an
        except Exception:
            return False

    never_tried = [s for s in stocks if s['moat_pct'] is None and not s['moat_attempted']]
    failed_before = [s for s in stocks if s['moat_pct'] is None and s['moat_attempted']]
    perimees = [s for s in stocks if s['moat_pct'] is not None and est_perime(s)]
    to_research = never_tried + failed_before + perimees  # PAS de plafond -- traitement trimestriel complet
    print(f'{len(to_research)} action(s) a rechercher ce trimestre '
          f'({len(never_tried)} jamais tentees, {len(failed_before)} echec precedent, '
          f'{len(perimees)} evaluation perimee (>1 an, probablement nouveau rapport annuel depuis)) '
          f'-- {len(stocks)-len(to_research)} a jour, pas retouchees')

    results = {}
    ok_count = 0
    for s in to_research:
        print(f'\n🔎 {s["ticker"]} ({s["name"]})...')
        try:
            r = research_moat(s)
            if r:
                answered = sum(1 for v in r['scores'] if v is not None)
                pct = round(sum(v for v in r['scores'] if v is not None) / answered * 100) if answered else None
                print(f'   -> {pct}% ({answered}/12 trouvés)')
                if answered > 0:
                    results[s['ticker']] = r
                    ok_count += 1
            else:
                print('   -> aucun résultat exploitable')
        except Exception as e:
            print(f'   -> ECHEC {s["ticker"]}: {e} (on continue avec les suivantes)')
        time.sleep(2)

    if results:
        patch_moat_scores(results)
    print(f'\n✅ Terminé : {ok_count}/{len(to_research)} actions avec au moins une donnée trouvée')
