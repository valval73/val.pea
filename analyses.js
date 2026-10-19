// VAL.PEA -- registre des analyses completes (methode en 6 etapes, 13/10/2026).
// Une ligne par analyse, la plus recente en premier. Le lien ouvre le document
// d'analyse (prive : visible seulement par sa proprietaire). Les valeurs du
// screener ont aussi leur contre-expertise dans leur fiche.
const ANALYSES = [
  {t:'WKL', nom:'Wolters Kluwer (exemple type : fiche à suivre)', date:'2026-10-19', compte:'PEA', verdict:'ACHAT 1/2', cours:84.26, p1:94.86, p2:78.12, dev:'€',
   lien:'https://claude.ai/code/artifact/da5454bd-23c3-4dc4-97f1-e552904dd142'},
  {t:'NRO', nom:'Neurones', date:'2026-10-13', compte:'PEA', verdict:'ATTENDRE', cours:36.65, p1:33.70, p2:29.80, dev:'€',
   lien:'https://claude.ai/code/artifact/e070bf0c-ca97-4cfa-8956-db23e556c24b'},
  {t:'FDS', nom:'FactSet (hors screener, compte-titres)', date:'2026-10-13', compte:'CTO', verdict:'ATTENDRE', cours:288.67, p1:245, p2:217, dev:'$',
   lien:'https://claude.ai/code/artifact/087b4654-4351-4418-9a99-797f37e3a57f'}
];
