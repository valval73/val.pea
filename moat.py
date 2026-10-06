"""
VAL.PEA -- Couche MOAT (avantage concurrentiel durable), 05/10/2026.

Un moat n'est PAS "pas de concurrence aujourd'hui" (monopoles d'Etat taxables,
leaders disruptes comme Wavestone, brevets qui expirent). C'est une
rentabilite elevee qui RESISTE aux concurrents dans la duree.

Score 0-5 (evaluation qualitative de Claude, A VALIDER par l'utilisatrice) :
  5 = quasi infranchissable (monopole technique, marque iconique, duopole)
  4 = fort et durable, avec une menace identifiee
  3 = reel mais limite (niche, taille, dependance)
  2 = faible (metier de services, relations clients)
  0-1 = absent
Regle ecrite : pas de signal 'acheter' si moat < 3.
A revoir chaque annee, et immediatement si la 'menace' se materialise.
"""

# ticker: (score, type de moat, menace principale)
MOAT = {
    # --- les 14 du filtre qualite ---
    'ASML':  (5, "monopole mondial des machines EUV, indispensables aux puces avancees",
                 "geopolitique (restrictions Chine), cycles des semi-conducteurs"),
    'AIR':   (5, "duopole Airbus-Boeing, carnet de commandes de ~8 ans, barrieres colossales",
                 "chaine fournisseurs (moteurs), concurrent chinois COMAC a long terme"),
    'SAF':   (5, "moteurs CFM (avec GE) sur A320neo/737 MAX + 30 ans de pieces et maintenance",
                 "cadences des avionneurs, problemes de fiabilite moteur"),
    'RMS':   (5, "marque de luxe la plus desirable, rarete organisee, pouvoir de prix",
                 "erosion de la rarete (sacs 'hors quotas', UBS oct. 2026), Chine"),
    'AI':    (5, "oligopole des gaz industriels, contrats de 15 ans sur sites clients",
                 "croissance faible, couts de l'energie"),
    'GTT':   (4, "brevets des membranes de cuves GNL, standard de l'immense majorite des methaniers",
                 "cycle des commandes, technologies concurrentes coreennes, sanctions"),
    'DSY':   (4, "couts de changement eleves (CATIA, SolidWorks standards de l'industrie)",
                 "transition cloud/IA mal negociee, croissance faible"),
    'HO':    (4, "defense souveraine, contrats longs, barrieres reglementaires",
                 "dependance aux budgets publics"),
    'LR':    (4, "marques installateurs et distribution, pouvoir de prix, data centers",
                 "cycle construction, valorisation tendue"),
    'SU':    (4, "leader gestion de l'energie, base installee et logiciels",
                 "rachat de PTC (22,6 Md$ : dette, dilution, prix paye)"),
    'OR':    (4, "portefeuille de marques mondial, echelle R&D et distribution",
                 "Chine, marques challengers digitales"),
    'PLNW':  (3, "logiciel de gestion de portefeuilles projets, couts de changement",
                 "petite taille face a Microsoft/Oracle/SAP"),
    'IPSEN': (2, "medicaments de specialite proteges par brevets",
                 "expirations de brevets (generiques), dependance aux succes de R&D"),
    'NRO':   (2, "services informatiques, relations clients et diversification",
                 "IA qui reduit les jours factures (cas Wavestone)"),
    # --- les 6 valeurs 'limites' ---
    'DG':    (4, "concessions (autoroutes, aeroports) : actifs uniques a revenus indexes",
                 "fin des concessions autoroutieres francaises (annees 2030), fiscalite"),
    'DASSAV':(4, "Rafale et Falcon : duopole defense/aviation d'affaires",
                 "dependance aux grands contrats export"),
    'RACE':  (5, "marque iconique, rarete organisee, listes d'attente",
                 "succession du modele thermique, dependance aux plus riches"),
    'EXENS': (3, "leader des tubes intensificateurs de lumiere (vision nocturne)",
                 "dependance aux budgets de defense, niche"),
    'RBT':   (3, "leader des matieres premieres naturelles pour la parfumerie",
                 "taille, concurrence des grands du secteur"),
    'ATE':   (2, "ingenierie externalisee, relations clients",
                 "IA, cycle automobile et aeronautique"),
    # --- leaders europeens (05/10/2026) ---
    'WKL':   (4, "information professionnelle integree aux processus (fiscal, sante, droit)", "IA generative qui banalise le contenu"),
    'ITX':   (3, "chaine d'approvisionnement rapide et echelle (Zara)", "mode ultra-rapide (Shein), gout changeant"),
    'AMS':   (4, "reservation aerienne (GDS) en quasi-duopole, logiciels compagnies", "vente directe des compagnies (NDC)"),
    'RAA':   (4, "leader mondial des fours mixtes professionnels (~50 % de part)", "cycle restauration, concurrence asiatique"),
    'NEM':   (4, "logiciels BIM/construction, couts de changement eleves", "Autodesk, IA"),
    'MONC':  (4, "marque de luxe (doudoune) a forte marge", "mode, dependance Chine"),
    'UMG':   (4, "1er catalogue musical mondial, oligopole de 3 majors", "musique generee par IA, pouvoir des plateformes"),
    'RHM':   (3, "capacites munitions/blindes, contrats publics longs", "cycle budgetaire, paix, execution"),
    'ATCO':  (4, "leader compresseurs/vide, apres-vente recurrent", "cycle industriel"),
    'ASM':   (4, "leader du depot de couches atomiques (ALD)", "cycle semi-conducteurs, Chine"),
    'NSIS':  (4, "enzymes et micro-organismes : duopole mondial", "integration Chr. Hansen, prix agricoles"),
    'ASSA':  (4, "leader mondial des serrures, base installee", "cycle construction"),
    'EPI':   (4, "equipements miniers en duopole avec Sandvik, apres-vente", "cycle minier"),
}
MOAT_MIN_BUY = 3

# Incertitude sur la valeur estimee (05/10/2026, jugement de Claude, a valider
# par l'utilisatrice) : plus l'avenir est difficile a prevoir, plus la decote exigee est
# grande (methode Morningstar simplifiee). faible : achat entre -10 et -20 %
# sous la valeur ; moyenne : -15 a -25 % ; elevee : -20 a -30 %.
UNCERTAINTY = {
    # faible : activite tres previsible, contrats longs, marques dominantes
    'AI': 'faible', 'OR': 'faible', 'RMS': 'faible', 'DG': 'faible',
    # moyenne
    'SU': 'moyenne', 'LR': 'moyenne', 'DSY': 'moyenne', 'HO': 'moyenne',
    'SAF': 'moyenne', 'AIR': 'moyenne', 'ASML': 'moyenne', 'NRO': 'moyenne',
    'WKL': 'moyenne', 'ITX': 'moyenne', 'AMS': 'moyenne', 'RAA': 'moyenne',
    'NEM': 'moyenne', 'MONC': 'moyenne', 'UMG': 'moyenne', 'ATCO': 'moyenne',
    'ASSA': 'moyenne', 'NSIS': 'moyenne', 'RACE': 'moyenne', 'DASSAV': 'moyenne',
    'RBT': 'moyenne',
    # elevee : une seule activite, cycle marque, brevets, petite taille
    'GTT': 'elevee', 'PLNW': 'elevee', 'IPSEN': 'elevee', 'RHM': 'elevee',
    'EXENS': 'elevee', 'ATE': 'elevee', 'ASM': 'elevee', 'EPI': 'elevee',
    'WAVE': 'elevee',
}
# (bas de zone, haut de zone) = valeur x (1 - decote)
MARGIN = {'faible': (0.20, 0.10), 'moyenne': (0.25, 0.15), 'elevee': (0.30, 0.20)}
