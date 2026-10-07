"""
VAL.PEA -- Croissance OFFICIELLE (communiques de resultats des societes),
prioritaire sur la croissance calculee depuis Yahoo.

Pourquoi (05/10/2026) : Yahoo ne donne que des chiffres publies bruts (effets
de change, rachats, elements exceptionnels). Exemple : Schneider ressortait a
5,9 %/an chez Yahoo alors que sa croissance organique 2025 est de +9 % et son
objectif 2026 de +7 a +10 %. Sa valeur estimee etait donc sous-evaluee.

Regle : croissance retenue = moyenne(croissance organique du dernier exercice,
milieu de l'objectif annonce pour l'exercice suivant). Croissance organique =
hors rachats et a taux de change constants. A METTRE A JOUR apres chaque
publication annuelle (et semestrielle si l'objectif change).
"""

# ticker: (croissance retenue %/an, detail, date de mise a jour)
OFFICIAL_GROWTH = {
    'AI':     (6.2,  "RN recurrent +6,2 % (07/10 : les ventes comparables +2 % sont faussees par la refacturation de l'energie, on retient le benefice)", '2026-10-07'),
    'OR':     (4.0,  "ventes comparables 2025 +4 %", '2026-10-05'),
    'RMS':    (7.5,  "2025 +9 % a changes constants ; S1 2026 +6 %", '2026-10-05'),
    'SAF':    (15.0, "CA ajuste 2025 +15 % ; objectif 2026 ~+15 %", '2026-10-05'),
    'SU':     (10.25, "organique 2025 +9 % ; objectif 2026 releve a +10 a +13 % (S1 2026 +14 %)", '2026-10-06'),
    'AIR':    (7.8,  "CA 2025 +6 % ; objectif 2026 ~870 livraisons (+9,7 %)", '2026-10-05'),
    'DG':     (2.6,  "organique 2025 +2,6 %", '2026-10-05'),
    'LR':     (8.35, "organique 2025 +7,7 % ; objectif 2026 releve a +8 a +10 % (S1 2026 +9,8 %)", '2026-10-06'),
    'DSY':    (4.0,  "2025 +4 % a changes constants ; objectif 2026 +3 a +5 %", '2026-10-05'),
    'GTT':    (9.8,  "CA 2025 +25 % ; objectif 2026 740-780 M EUR (-5 %)", '2026-10-05'),
    'SOP':    (1.5,  "2025 en recul ; objectif 2026 organique +1 a +2 %", '2026-10-05'),
    'HO':     (8.4, "organique 2025 +8,8 % ; objectif 2026 +7 a +9 % (S1 2026 +7,8 %)", '2026-10-06'),
    'ASML':   (25.0, "CA 2025 +15,5 % ; objectif 2026 releve a 43-45 Md EUR (~+35 %) -- plafonne a 12 % dans le calcul", '2026-10-06'),
    'IPSEN':  (12.0, "2025 +10,9 % a changes constants ; objectif 2026 > +13 %", '2026-10-05'),
    'FDJU':   (-1.0, "2025 -2,9 % a perimetre comparable ; objectif 2026 'legere croissance'", '2026-10-05'),
    'NRO':    (5.05, "organique 2025 +5,1 % ; objectif 2026 ~+5 %", '2026-10-05'),
    'PLNW':   (10.15,"2025 +10,3 % a changes constants ; objectif 2026 ~+10 %", '2026-10-05'),
    'WAVE':   (1.0,  "organique 2025/26 +1 % ; objectif 2026/27 -1 % a faible croissance", '2026-10-05'),
    # --- leaders europeens (ajoutes le 05/10/2026) ---
    'WKL':    (6.0,  "organique 2025 ~+6 % ; 2026 annonce comparable", '2026-10-05'),
    'ITX':    (8.0,  "exercice 2025 +7,0 % a changes constants ; debut 2026 +9 %", '2026-10-05'),
    'AMS':    (5.5,  "S1 2026 +5,1 % a changes constants (reservations +1,1 %) ; objectif 2026 'moyen a haut a un chiffre' -- contre-expertise du 06/10", '2026-10-06'),
    'RAA':    (8.0,  "2025 +8 % hors effet change", '2026-10-05'),
    'NEM':    (14.5, "objectif 2026 +14 a +15 % a changes constants (2025 +22,6 % rachats inclus, non retenu)", '2026-10-05'),
    'MONC':   (3.0,  "2025 +3 % a changes constants (T4 +7 %)", '2026-10-05'),
    'UMG':    (8.7,  "2025 +8,7 % a changes constants", '2026-10-05'),
    'RHM':    (35.75,"2025 +29 % ; objectif 2026 +40 a +45 % (plafonne a 12 % dans le calcul)", '2026-10-05'),
    'ATCO':   (2.0,  "approximatif : T4 2025 revenus organiques 0 %, commandes +4 % (bas de cycle) -- chiffre annuel a confirmer", '2026-10-05'),
}
