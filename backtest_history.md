# Historique des backtests QARP

Suivi mensuel : corrélation du score aux rendements réels, alpha, poids suggérés.
Permet de vérifier que le screener reste calibré dans le temps, pas seulement au lancement.

## 2026-08-25

```
CONCLUSIONS
=================================================================

1. Score Unifié : corrél. 0.404
   ✅ Modèle valide

2. Alpha Score ≥65 vs Score <50 : +11.9%/an
   ✅ Alpha significatif

3. Large Caps (n=50) :
   Score Large corrél. 0.454

4. Midcaps (n=35) :
   Score Mid corrél. 0.391

5. Poids optimaux suggérés (à implémenter dans calcQARPLarge) :
   PE fwd          corrél=0.423  → suggère ~27 pts
   ROE             corrél=0.323  → suggère ~21 pts
   Dette           corrél=0.302  → suggère ~19 pts
   Marge           corrél=0.285  → suggère ~18 pts
   Croiss.CA       corrél=0.215  → suggère ~14 pts
   Croiss.BPA      corrél=0.015  → suggère ~1 pts
```
