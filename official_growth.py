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

Exception (11/10/2026, contre-expertise Baggr sur GTT) : si l'objectif de
l'exercice suivant est en BAISSE, on ne fait pas la moyenne avec l'annee
precedente (souvent un pic de cycle) : on retient la croissance attendue par
le consensus a 3-5 ans, plafonnee a 3 %.
"""

# ticker: (croissance retenue %/an, detail, date de mise a jour)
OFFICIAL_GROWTH = {
    'AI':     (6.2,  "RN recurrent +6,2 % (07/10 : les ventes comparables +2 % sont faussees par la refacturation de l'energie, on retient le benefice)", '2026-10-07'),
    'OR':    (5.45, "ventes comparables 2025 +4 % ; 9 mois 2026 +6,9 % (pas d'objectif chiffre)", '2026-11-06'),
    'RMS':    (7.5,  "2025 +9 % a changes constants ; S1 2026 +6 %", '2026-10-05'),
    'SAF':   (15.0, 'CA ajuste 2025 +15 % ; objectif 2026 ~+15 % confirme le 23/10 (9 mois +17,5 % publie)', '2026-11-06'),
    'SU':    (11.0, 'organique 2025 +9 % ; objectif 2026 releve le 16/10 a +12 a +14 % (9 mois +15 %)', '2026-11-06'),
    'AIR':   (7.8, 'CA 2025 +6 % ; objectif 2026 ~870 livraisons confirme le 28/10 (+9,7 %)', '2026-11-06'),
    'DG':    (2.2, 'organique 2025 +2,6 % ; 9 mois 2026 +1,8 % (presse)', '2026-11-06'),
    'LR':    (9.85, 'organique 2025 +7,7 % ; objectif 2026 releve le 05/11 a +11 a +13 % (9 mois +12,7 %)', '2026-11-06'),
    'DSY':   (4.25, '2025 +4 % a changes constants ; objectif 2026 releve a +4 a +5 % (ArisGlobal compris)', '2026-11-06'),
    'GTT':   (3.0, '9 mois 2026 CA -4,9 % (creux attendu) ; objectif 2026 confirme 740-780 M EUR (-5 %) ; pas de moyenne avec le pic 2025', '2026-11-06'),
    'SOP':   (2.75, 'objectif 2026 releve le 29/10 a +2,5 a +3,0 % organique (T3 +4,3 %)', '2026-11-06'),
    'HO':    (7.9, "organique 2025 +8,8 % ; objectif 2026 haut de +6 a +7 % 'voire au-dela' (9 mois +8,1 %)", '2026-11-06'),
    'ASML':   (25.0, "CA 2025 +15,5 % ; objectif 2026 releve a 43-45 Md EUR (~+35 %) -- plafonne a 12 % dans le calcul", '2026-10-06'),
    'IPSEN': (16.95, '2025 +10,9 % a changes constants ; objectif 2026 releve a ~+23 % (9 mois +24,6 %)', '2026-11-06'),
    'FDJU':  (-5.0, 'objectif 2026 abaisse le 21/10 : CA ~-5 % (9 mois -5,6 % publie) ; objectif en baisse : pas de moyenne, consensus 3-5 ans non verifie', '2026-11-06'),
    'NRO':   (6.0, 'organique 2025 +5,1 % ; 9 mois 2026 +6,9 % (objectif CA > 900 M EUR)', '2026-11-06'),
    'PLNW':  (11.65, '2025 +10,3 % a changes constants ; objectif 2026 au moins +13 % confirme (9 mois +14,9 %)', '2026-11-06'),
    'WAVE':  (0.75, 'organique 2025/26 +1 % ; objectif 2026/27 -1 % a faible croissance confirme (S1 -1 %)', '2026-11-06'),
    # --- leaders europeens (ajoutes le 05/10/2026) ---
    'WKL':   (6.0, "organique 2025 +6 % ; 9 mois 2026 +6 % (pas d'objectif de croissance groupe)", '2026-11-06'),
    'ITX':    (8.0,  "exercice 2025 +7,0 % a changes constants ; debut 2026 +9 %", '2026-10-05'),
    'AMS':   (5.0, "9 mois 2026 +5,2 % a changes constants ; objectif 2026 'moyen a haut a un chiffre' tenu en bas de fourchette (06/11)", '2026-11-06'),
    'RAA':   (6.5, "2025 +8 % hors change ; 2026 attendu en bas de 'moyen a haut a un chiffre' (~5 %), 9 mois +7 %", '2026-11-06'),
    'NEM':   (14.5, 'objectif 2026 +14 a +15 % organique confirme le 05/11 (T3 +12,5 %, 9 mois +14,6 %)', '2026-11-06'),
    'MONC':  (3.0, "2025 +3 % a changes constants ; 9 mois 2026 +6 % mais T3 0 % : prudence, pas d'objectif", '2026-11-06'),
    'UMG':   (5.5, '9 mois 2026 +11,1 % a changes constants mais +5,5 % hors Downtown (acquisition) ; T3 +5,3 % hors Downtown', '2026-11-06'),
    'RHM':   (31.0, '2025 +29 % ; objectif 2026 abaisse le 05/11 a ~13,2 Md EUR (~+33 %) (plafonne a 12 % dans le calcul)', '2026-11-06'),
    'ATCO':  (2.0, 'approximatif : T3 2026 CA +11 % organique, commandes +25 % ; chiffre annuel organique non verifie', '2026-11-06'),
    # --- 12/10/2026 : valeurs du filtre encore valorisees avec la croissance Yahoo ---
    'ASM':   (23.5, '2025 +12 % a changes constants ; objectif 2026 ~+35 % (T3 +44 %)', '2026-11-06'),
    'ASSA':  (3.0, 'organique 2025 +3 % ; 9 mois 2026 +3 % (T3 +4 %)', '2026-11-06'),
    'ATE':   (2.0, 'objectif 2026 releve le 27/10 a ~+2 % organique (T3 +3,6 %)', '2026-11-06'),
    'DASSAV': (16.8, "CA ajuste 2025 +19 % (7,42 Md EUR) ; objectif 2026 ~8,5 Md EUR (~+14,6 %) -- livraisons Rafale, activite par a-coups", '2026-10-12'),
    'EXENS': (14.4, 'organique 9 mois 2026 +14,4 % ; objectif 2026 558-570 M EUR confirme (rachats inclus, non retenu)', '2026-11-06'),
    'NSIS':  (7.5, 'objectif 2026 +7 a +8 % organique confirme le 05/11 (9 mois +7 %) ; 2025 non verifie', '2026-11-06'),
    'PLUXEE':(0.0, "exercice 2026 +0,7 % organique (T4 -4,9 %) ; objectif 2027 EBITDA >= 440 M EUR (-10 %), pas d'objectif de CA : objectif en baisse", '2026-11-06'),
    'RACE':  (7.0, 'CA 2025 ~+7 % ; objectif 2026 releve le 03/11 a ~7,65 Md EUR (~+7 %)', '2026-11-06'),
    'RBT':    (5.8,  "organique 2025 +7,6 % ; objectif 2026 abaisse a +3 a +5 % (S1 2026 -0,5 % publie)", '2026-10-12'),
    # --- 14/10/2026 : contre-expertises des valeurs en zone (croissance Yahoo gonflee) ---
    'KRN':   (1.5, 'objectif 2026 abaisse le 22/10 a +1 a +2 % a changes constants (9 mois +0,8 %)', '2026-11-06'),
    'HEIJM': (9.0, 'S1 2026 ~+9 % hors acquisition (calcul) ; objectif 2026 CA ~3,1 Md EUR inchange (30/10)', '2026-11-06'),
    'TGYM':  (6.9, "9 mois 2026 +6,9 % a changes constants (le +9 % du S1 n'a pas ete retrouve) ; pas d'objectif", '2026-11-06'),
    'DLG':    (6.5,  "S1 2026 +8 % a changes constants ; objectif 2026 'moyen a un chiffre'", '2026-10-14'),
    'RWAY':   (2.5,  "S1 2026 CA +2,5 %", '2026-10-14'),
    # Non renseignees faute d'objectif annuel officiel (restent sur Yahoo) :
    # EPI (Epiroc : organique 2025 +2 %, T2 2026 +11 %, cyclique, pas d'objectif)
    # TE  (Technip Energies : objectifs 2026 par segment abaisses le 30/04, pas de croissance globale publiee)
}
