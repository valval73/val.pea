// ═══════════════════════════════════════════════════
// VAL.PEA — Data : Actions SBF250 + ETF PEA
// Mise à jour automatique par GitHub Actions
// ═══════════════════════════════════════════════════

const S=[
// ══════════════════════════════════════════
// CAC 40
// ══════════════════════════════════════════
{ticker:'MC',x2:'',x2s:'',name:'LVMH',sector:'Luxe',cap:'large',srd:true,idx:'CAC40',
 price:390.0,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.4,news5:'',dy_n:10,dy_med:1.84,div12:13.0,pe_lo:24.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:13.4,pfcf_h:24.8,pe_h:24.3,fcur:'EUR',fcfh:'14205|13373|10596|12753',nih:'10878|12550|15174|14084',revh:'80807|84682|86153|79183',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-3.7,gimp:null,knife:true,neglect:false,vmeth:'per',nig:-8.2,cagr:0.7,alarm:'',qwhy:'croissance CA 0.7%',qok:false,nde:1.08,fcfc:97.0,roicx:21.0,chg:-1.76,mkt:'278Md€',b52h:654.7,b52l:375.65,beta:0.88,
 pe:17.78,pb:2.82,ev_ebitda:11.09,ps:2.41,pfcf:18,ev_ebit:12.5,
 roe:16.6,roic:16.0,roa:7.7,debt:0.53,de:0.53,ic:15.5,cr:1.63,qr:1.1,
 yield:3.3,epsg:0.8,revg:-2.9,margin:13.7,gm:66.4,om:26,fcf:7.4,
 capex:2.8,capr:5.8,capda:0.58,
 dcfb:309.07,dcfm:363.61,dcfu:436.33,
 pio:6,alt:2.82,rsi:42.7,mm50:418.28,mm200:477.17,
 el:283.62,eh:331.61,stop:249.59,o1:381.79,o2:436.33,
 cb:18,ch:6,cs:2,tp:502.95,score:'C',rec:'avoid',zone:false,
 moat:[['75 maisons iconiques','fort'],['Pricing power','fort']],
 cats:[{t:'Rebond luxe Chine 2026',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Arnault','250M€','Fév 2026']],
 peers:[{n:'Hermès',pe:50,pb:22,roe:36,div:0.6,evebitda:32},{n:'Kering',pe:14,pb:2.1,roe:15,div:4.2,evebitda:9}],
 risks:{Chine:65,Devise:45,Cyclicite:55,Reglement:25,Disruption:20,Liquidite:10},
 track:[{y:'2025',p:'Croissance organique +5%',ok:'ok'}],
 thesis:"LVMH reste le meilleur actif de luxe diversifié. À 22x PE sur un creux de cycle, le risque/rendement redevient attractif. La famille Arnault a franchi 50% du capital.",
 contra:"La Chine représente 27% des ventes dans un contexte de nationalisme croissant. La correction depuis 900€ n'est peut-être pas terminée."},

{ticker:'AI',x2:'',x2s:'',name:'Air Liquide',sector:'Gaz industriels',cap:'large',srd:true,idx:'CAC40',
 price:173.4,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.8,news5:'',dy_n:10,dy_med:2.02,div12:3.364,pe_lo:25.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:13.8,pfcf_h:32.0,pe_h:26.5,fcur:'EUR',fcfh:'2675|2797|2870|2537',nih:'3518|3306|3078|2759',revh:'26940|27058|27608|29934',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:0,place:'Paris',mthreat:'croissance faible, couts de l energie',mtype:'oligopole des gaz industriels, contrats de 15 ans sur sites clients',mscore:5,near:false,gsrc:'communique 2026-10-07',gused:6.2,gimp:null,knife:false,neglect:false,vmeth:'per',nig:8.4,cagr:-3.5,alarm:'',qwhy:'ROIC 9.4',qok:false,nde:1.32,fcfc:86.0,roicx:15.7,chg:0.14,mkt:'74Md€',b52h:182.26,b52l:140.78,beta:0.61,
 pe:31.24,pb:4.16,ev_ebitda:16.55,ps:4.09,pfcf:22,ev_ebit:25.4,
 roe:14.0,roic:9.4,roa:6.3,debt:0.63,de:0.63,ic:60.0,cr:0.88,qr:0.9,
 yield:1.9,epsg:0.7,revg:0.8,margin:13.1,gm:64.6,om:18,fcf:2.4,
 capex:8.2,capr:14.3,capda:1.5,
 dcfb:84.52,dcfm:99.43,dcfu:119.32,
 pio:7,alt:4.1,rsi:61.5,mm50:168.84,mm200:162.31,
 el:82.53,eh:92.67,stop:72.63,o1:104.4,o2:119.32,
 cb:14,ch:8,cs:1,tp:198.82,score:'C',rec:'avoid',zone:false,
 moat:[['Contrats take-or-pay 15-20 ans','fort'],['Infrastructure mondiale','fort']],
 cats:[{t:'Hydrogène vert accélération',w:'2026-2028',c:'var(--gn)'}],
 ins:[['Achat','Benoît Potier','2.1M€','Jan 2026']],
 peers:[{n:'Linde',pe:30,pb:5.8,roe:18,div:1.4,evebitda:20},{n:'Air Products',pe:25,pb:4.5,roe:14,div:2.8,evebitda:17}],
 risks:{Devise:35,Cyclicite:30,Reglement:40,Hydrogène:45,Energie:50,Liquidite:15},
 track:[{y:'2025',p:'BPA +9%',ok:'ok'},{y:'2024',p:'30ème hausse dividende',ok:'ok'}],
 thesis:"Air Liquide est l'infrastructure invisible de l'industrie mondiale. 29 années consécutives de hausse du dividende. Contrats 15-20 ans take-or-pay = cash flows quasi-certains.",
 contra:"Valorisation premium. CAPEX très lourd (12.4% CA) pour l'hydrogène dont le retour reste incertain."},

{ticker:'OR',x2:'',x2s:'',name:"L'Oréal",sector:'Cosmétiques',cap:'large',srd:true,idx:'CAC40',
 price:403.6,roiica:true,reinv:false,roiic:9.4,vmed:221.77,vepv:131.26,chg5:5.4,news5:'',dy_n:10,dy_med:1.6,div12:7.2,pe_lo:27.7,gmod:4.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:5.8,irr:5.8,dq:'',vmult:244.63,hn:4,eveb_h:19.0,pfcf_h:31.7,pe_h:31.5,fcur:'EUR',fcfh:'7162|6644|6116|4935',nih:'6127|6409|6184|5707',revh:'44052|43487|41182|38261',yrs:'2025|2024|2023|2022',unc:'faible',vopt:252.34,vpess:186.54,nregu:2,regn:3,regu:3,place:'Paris',mthreat:'Chine, marques challengers digitales',mtype:'portefeuille de marques mondial, echelle R&D et distribution',mscore:4,near:false,gsrc:'communique 2026-10-05',gused:4.0,gimp:18.8,knife:false,neglect:false,vmeth:'qarp',nig:2.4,cagr:4.8,alarm:'',qwhy:'',qok:true,nde:0.19,fcfc:102.0,roicx:29.8,chg:-0.93,mkt:'183Md€',b52h:407.4,b52l:338.85,beta:0.86,
 pe:34.26,pb:6.35,ev_ebitda:22.18,ps:4.74,pfcf:28,ev_ebit:25.9,
 roe:19.4,roic:18.4,roa:9.5,debt:0.49,de:0.49,ic:23.7,cr:0.97,qr:1.4,
 yield:1.8,epsg:5.4,revg:5.8,margin:13.9,gm:74.4,om:22,fcf:3.3,
 capex:3.2,capr:3.4,capda:0.82,
 dcfb:188.5,dcfm:221.77,dcfu:266.12,
 pio:6,alt:6.27,rsi:66.7,mm50:383.25,mm200:374.36,
 el:177.42,eh:199.59,stop:167.89,o1:252.34,o2:277.57,
 cb:20,ch:4,cs:1,tp:418.0,score:'C',rec:'hold',zone:false,
 moat:[['37 marques tous segments','fort'],['R&D dermatologique','fort']],
 cats:[{t:'Rebond beauté Chine',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Bettencourt','890M€','Déc 2025']],
 peers:[{n:'Estée Lauder',pe:28,pb:12,roe:30,div:2.1,evebitda:18},{n:'Shiseido',pe:35,pb:3.2,roe:9,div:1.8,evebitda:14}],
 risks:{Chine:60,Devise:45,Cyclicite:35,Disruption:40,Reglement:30,Liquidite:10},
 track:[{y:'2025',p:'Croissance organique +5.1%',ok:'ok'}],
 thesis:"L'Oréal capte la montée en gamme mondiale. Aucun concurrent ne combine R&D dermatologique, distribution omnicanale et 37 marques couvrant tous les segments.",
 contra:"32x PE pour une croissance qui ralentit. La Chine déçoit. Marques DTC gagnent des parts."},

{ticker:'RMS',x2:'',x2s:'',name:'Hermès',sector:'Luxe',cap:'large',srd:true,idx:'CAC40',
 price:1337.0,roiica:false,reinv:false,roiic:31.2,vmed:963.41,vepv:561.59,chg5:2.1,news5:'',dy_n:10,dy_med:0.8,div12:18.0,pe_lo:44.9,gmod:7.5,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:6.9,irr:6.9,dq:'',vmult:1173.07,hn:4,eveb_h:28.0,pfcf_h:55.0,pe_h:47.7,fcur:'EUR',fcfh:'4213|4072|3469|3666',nih:'4524|4603|4311|3367',revh:'16001|15170|13427|11601',yrs:'2025|2024|2023|2022',unc:'faible',vopt:1078.68,vpess:703.95,nregu:2,regn:3,regu:3,place:'Paris',mthreat:'erosion de la rarete (sacs  hors quotas , UBS oct. 2026), Chine',mtype:'marque de luxe la plus desirable, rarete organisee, pouvoir de prix',mscore:5,near:false,gsrc:'communique 2026-10-05',gused:7.5,gimp:16.2,knife:true,neglect:false,vmeth:'qarp',nig:10.3,cagr:11.3,alarm:'',qwhy:'',qok:true,nde:-1.28,fcfc:92.0,roicx:62.8,chg:-0.04,mkt:'232Md€',b52h:2300.0,b52l:1255.0,beta:1.04,
 pe:31.09,pb:7.36,ev_ebitda:18.43,ps:8.68,pfcf:42,ev_ebit:19.0,
 roe:25.5,roic:61.5,roa:18.1,debt:0.12,de:0.12,ic:124.2,cr:4.54,qr:3.2,
 yield:1.4,epsg:-0.3,revg:1.6,margin:28.0,gm:71.3,om:42,fcf:3.0,
 capex:4.2,capr:7.3,capda:1.25,
 dcfb:818.9,dcfm:963.41,dcfu:1156.09,
 pio:8,alt:17.82,rsi:47.4,mm50:1427.78,mm200:1685.69,
 el:770.73,eh:867.07,stop:633.56,o1:1078.68,o2:1186.55,
 cb:22,ch:5,cs:1,tp:1632.17,score:'C',rec:'hold',zone:false,
 moat:[['Marque la plus désirable','fort'],['Offre intentionnellement limitée','fort']],
 cats:[{t:'Nouvelle maroquinerie Normandie',w:'2027',c:'var(--gn)'}],
 ins:[['Achat','Famille Hermès','2.1Md€','Déc 2025']],
 peers:[{n:'LVMH',pe:22,pb:5.1,roe:24,div:2.4,evebitda:14},{n:'Richemont',pe:18,pb:3.8,roe:16,div:2.2,evebitda:12}],
 risks:{Valorisation:70,Devise:40,Succession:35,Contrefaçon:30,Cyclicite:25,Liquidite:10},
 track:[{y:'2025',p:'Marge op. 42% record',ok:'ok'}],
 thesis:"Hermès est l'actif le plus unique de la bourse mondiale. 42% de marge, zéro dette, famille aux commandes depuis 6 générations. La liste d'attente Birkin immunise contre les cycles.",
 contra:"50x PE ne permet aucune erreur. Risque succession familiale. Contrefaçon croissante en Asie."},

{ticker:'SAN',x2:'',x2s:'',name:'Sanofi',sector:'Pharmacie',cap:'large',srd:true,idx:'CAC40',
 price:71.01,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.8,news5:'',dy_n:10,dy_med:3.82,div12:4.12,pe_lo:12.7,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:9.9,pfcf_h:14.5,pe_h:17.2,fcur:'EUR',fcfh:'7212|5886|7352|8423',nih:'7813|5560|5400|8371',revh:'46716|44286|41618|40561',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:1.2,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-2.3,cagr:4.8,alarm:'',qwhy:'ROIC 6.9',qok:false,nde:1.02,fcfc:106.0,roicx:15.2,chg:-1.29,mkt:'124Md€',b52h:91.15,b52l:69.75,beta:0.28,
 pe:21.85,pb:1.23,ev_ebitda:7.66,ps:1.74,pfcf:16,ev_ebit:15.3,
 roe:5.7,roic:6.9,roa:5.1,debt:0.34,de:0.34,ic:10.9,cr:0.99,qr:1.5,
 yield:5.7,epsg:-91.2,revg:14.6,margin:8.1,gm:73.5,om:20,fcf:8.5,
 capex:3.8,capr:7.6,capda:0.62,
 dcfb:85.85,dcfm:101.0,dcfu:121.2,
 pio:7,alt:1.5,rsi:42.2,mm50:74.41,mm200:75.21,
 el:70.7,eh:88.88,stop:62.22,o1:106.05,o2:121.2,
 cb:16,ch:5,cs:2,tp:93.35,score:'C',rec:'avoid',zone:false,
 moat:[['Dupixent monopole IL-4/IL-13','fort'],['Pipeline vaccins','modere']],
 cats:[{t:'Dupixent nouvelles indications',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Paul Hudson','1.8M€','Jan 2026']],
 peers:[{n:'Novartis',pe:16,pb:4.1,roe:24,div:3.8,evebitda:12},{n:'AstraZeneca',pe:22,pb:6.2,roe:28,div:2.1,evebitda:16}],
 risks:{Pipeline:55,Devise:40,Reglement:45,Concentration:60,Biosimilaires:50,Liquidite:15},
 track:[{y:'2025',p:'Dupixent 13Md€ revenus',ok:'ok'}],
 thesis:"Dupixent est l'un des médicaments les plus importants au monde — 13Md$ sur une maladie chronique sans alternative. À 18x PE avec 4.1% de dividende, le marché ne valorise pas le pipeline.",
 contra:"Dupixent = 40% des revenus : concentration dangereuse. R&D historiquement décevante sur 10 ans."},

{ticker:'TTE',x2:'',x2s:'',name:'TotalEnergies',sector:'Énergie',cap:'large',srd:true,idx:'CAC40',
 price:80.53,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.0,news5:'',dy_n:10,dy_med:5.29,div12:3.45,pe_lo:7.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:3.6,pfcf_h:7.4,pe_h:7.8,fcur:'USD',fcfh:'10390|15945|22957|31677',nih:'13127|15758|21384|20526',revh:'182344|195610|218945|263310',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-12.7,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-13.8,cagr:-11.5,alarm:'',qwhy:'croissance CA -11.5%',qok:false,nde:0.92,fcfc:114.0,roicx:15.6,chg:-0.22,mkt:'146Md€',b52h:81.63,b52l:52.24,beta:0.09,
 pe:11.76,pb:1.57,ev_ebitda:5.38,ps:0.9,pfcf:7,ev_ebit:8.5,
 roe:14.5,roic:14.4,roa:5.5,debt:0.48,de:0.48,ic:9.8,cr:1.06,qr:1.0,
 yield:4.5,epsg:106.0,revg:27.8,margin:9.1,gm:37.7,om:12,fcf:5.9,
 capex:14.2,capr:9.3,capda:1.22,
 dcfb:84.23,dcfm:99.09,dcfu:118.91,
 pio:5,alt:1.51,rsi:63.8,mm50:77.04,mm200:71.38,
 el:79.27,eh:91.16,stop:69.76,o1:104.04,o2:118.91,
 cb:14,ch:5,cs:3,tp:87.7,score:'C',rec:'avoid',zone:false,
 moat:[['Actifs LNG de classe mondiale','fort'],['Transition énergétique avancée','modere']],
 cats:[{t:'LNG Canada pleine production',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Pouyanné','3.2M€','Jan 2026']],
 peers:[{n:'Shell',pe:9,pb:1.3,roe:13,div:4.8,evebitda:5},{n:'BP',pe:8,pb:1.1,roe:11,div:5.2,evebitda:4}],
 risks:{Pétrole:75,Transition:65,Geopol:55,Reglement:50,Devise:35,Liquidite:10},
 track:[{y:'2025',p:'Dividende maintenu 5.2%',ok:'ok'}],
 thesis:"TotalEnergies à 8x PE et 5.2% de yield avec LNG Canada opérationnel. Rachat d'actions massif soutient le cours.",
 contra:"Le pétrole à 60$ détruit la thèse si ça dure. Transition ENR consomme du capital sans retour immédiat."},

{ticker:'SAF',x2:'',x2s:'',name:'Safran',sector:'Aéronautique',cap:'large',srd:true,idx:'CAC40',
 price:315.3,roiica:false,reinv:false,roiic:357.0,vmed:94.59,vepv:94.59,chg5:-1.0,news5:'',dy_n:9,dy_med:1.06,div12:3.35,pe_lo:null,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'cyclique',wht:0.0,irrn:4.4,irr:4.4,dq:'',vmult:95.62,hn:2,eveb_h:10.7,pfcf_h:25.0,pe_h:18.5,fcur:'EUR',fcfh:'3921|3189|2945|2666',nih:'7177|-667|3444|-2459',revh:'31189|27716|23651|19523',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:94.59,vpess:94.59,nregu:2,regn:3,regu:3,place:'Paris',mthreat:'cadences des avionneurs, problemes de fiabilite moteur',mtype:'moteurs CFM (avec GE) sur A320neo/737 MAX + 30 ans de pieces et maintenance',mscore:5,near:false,gsrc:'communique 2026-10-05',gused:15.0,gimp:30.0,knife:false,neglect:false,vmeth:'qarp',nig:null,cagr:16.9,alarm:'',qwhy:'',qok:true,nde:-0.12,fcfc:170.0,roicx:19.6,chg:-0.54,mkt:'112Md€',b52h:366.5,b52l:262.6,beta:0.97,
 pe:33.87,pb:9.01,ev_ebitda:21.3,ps:3.89,pfcf:26,ev_ebit:12.5,
 roe:27.5,roic:12.7,roa:4.8,debt:0.34,de:0.34,ic:77.1,cr:0.92,qr:1.2,
 yield:1.1,epsg:-65.1,revg:16.0,margin:11.6,gm:46.8,om:19,fcf:3.0,
 capex:4.2,capr:5.8,capda:1.22,
 dcfb:80.4,dcfm:94.59,dcfu:113.51,
 pio:7,alt:2.86,rsi:40.1,mm50:333.49,mm200:316.24,
 el:66.21,eh:75.67,stop:85.13,o1:94.59,o2:104.05,
 cb:18,ch:5,cs:1,tp:381.5,score:'C',rec:'hold',zone:false,
 moat:[['LEAP duopole Airbus/Boeing','fort'],['Services MRO récurrents','fort']],
 cats:[{t:'Montée cadence LEAP 2200/mois',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Castaing','4.1M€','Fév 2026']],
 peers:[{n:'GE Aerospace',pe:38,pb:18,roe:45,div:0.8,evebitda:24},{n:'Rolls-Royce',pe:28,pb:15,roe:38,div:0.5,evebitda:18}],
 risks:{Airbus:50,Devise:55,Supply:45,Technologie:35,Geopol:30,Liquidite:10},
 track:[{y:'2025',p:'BPA +18%',ok:'ok'},{y:'2024',p:'Carnet commandes record',ok:'ok'}],
 thesis:"Safran est l'actif aéronautique le plus désirable de France. Le moteur LEAP équipe 70% des moyen-courriers mondiaux. Duopole mondial inattaquable.",
 contra:"Valorisation exigeante à 32x PE. Dépendance Airbus (50% CA). Baisse USD pénalise les revenus."},

{ticker:'SU',x2:'',x2s:'',name:'Schneider Electric',sector:'Énergie & Automatisation',cap:'large',srd:true,idx:'CAC40',
 price:252.6,roiica:false,reinv:false,roiic:27.3,vmed:214.16,vepv:75.78,chg5:-4.8,news5:'',dy_n:10,dy_med:2.08,div12:4.2,pe_lo:21.0,gmod:10.2,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:7.6,irr:7.6,dq:'',vmult:222.53,hn:4,eveb_h:16.3,pfcf_h:25.7,pe_h:28.5,fcur:'EUR',fcfh:'4588|4161|4542|3261',nih:'4163|4269|4003|3477',revh:'40152|38153|35902|34176',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:231.67,vpess:134.25,nregu:2,regn:3,regu:3,place:'Paris',mthreat:'rachat de PTC (22,6 Md$ : dette, dilution, prix paye)',mtype:'leader gestion de l energie, base installee et logiciels',mscore:4,near:false,gsrc:'communique 2026-10-06',gused:10.25,gimp:13.9,knife:false,neglect:false,vmeth:'qarp',nig:6.2,cagr:5.5,alarm:'',qwhy:'',qok:true,nde:1.58,fcfc:104.0,roicx:41.5,chg:-0.28,mkt:'136Md€',b52h:312.3,b52l:220.4,beta:1.13,
 pe:30.36,pb:5.81,ev_ebitda:18.66,ps:3.38,pfcf:22,ev_ebit:23.7,
 roe:18.6,roic:12.7,roa:7.4,debt:0.84,de:0.84,ic:12.4,cr:1.09,qr:1.1,
 yield:1.7,epsg:29.3,revg:9.8,margin:11.3,gm:42.1,om:18,fcf:3.2,
 capex:3.8,capr:3.8,capda:0.93,
 dcfb:182.04,dcfm:214.16,dcfu:256.99,
 pio:6,alt:3.79,rsi:33.5,mm50:286.55,mm200:266.83,
 el:160.62,eh:182.04,stop:120.83,o1:231.67,o2:254.84,
 cb:20,ch:4,cs:1,tp:328.36,score:'B',rec:'hold',zone:false,
 moat:[['Data center électrification','fort'],['Ecosystème EcoStruxure','fort']],
 cats:[{t:'Data centers IA explosion',w:'2026-2028',c:'var(--gn)'}],
 ins:[['Achat','CEO Cigna','5.2M€','Jan 2026']],
 peers:[{n:'ABB',pe:25,pb:5.8,roe:22,div:2.0,evebitda:16},{n:'Siemens',pe:22,pb:4.5,roe:18,div:2.8,evebitda:14}],
 risks:{Cyclicite:45,Devise:50,Concurrence:40,Supply:35,Reglement:25,Liquidite:10},
 track:[{y:'2025',p:'Croissance organique +12%',ok:'ok'}],
 thesis:"Schneider est au centre de trois mégatendances : électrification, digitalisation, data centers IA. La demande data centers double tous les 4 ans.",
 contra:"Valorisation premium. Forte exposition USD. Concurrence ABB et Siemens sur les segments IA."},

{ticker:'AXA',x2:'',x2s:'',name:'Axa',sector:'Assurance',cap:'large',srd:true,idx:'CAC40',
 price:42.42,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.5,news5:'',dy_n:10,dy_med:5.74,div12:2.32,pe_lo:8.6,gmod:null,nih:'9623|7685|7004|4879',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:4.1,roemin:10.6,roem:14.8,grid:'banque',wht:0.0,irrn:8.7,irr:8.7,dq:'',vmult:null,hn:4,eveb_h:null,pfcf_h:6.6,pe_h:9.3,fcur:'EUR',unc:'elevee',vopt:40.87,vpess:27.06,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:25.4,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:25.4,cagr:null,alarm:'',qwhy:'',qok:true,nde:null,fcfc:null,roicx:null,chg:-1.28,mkt:'62Md€',b52h:45.66,b52l:36.55,beta:0.59,
 pe:11.43,pb:1.92,ev_ebitda:7.54,ps:0.92,pfcf:999,ev_ebit:null,
 roe:14.9,roic:null,roa:1.1,debt:1.19,de:1.19,ic:null,cr:11.53,qr:999,
 yield:5.4,epsg:13.2,revg:4.5,margin:10.4,gm:14.9,om:999,fcf:24.7,
 capex:0.8,capr:0.4,capda:0.58,
 dcfb:39.76,dcfm:35.35,dcfu:56.14,
 pio:7,alt:0.35,rsi:45.9,mm50:43.46,mm200:40.55,
 el:24.74,eh:28.28,stop:24.36,o1:40.87,o2:44.96,
 cb:14,ch:5,cs:2,tp:52.15,score:'C',rec:'hold',zone:false,
 moat:[['AXA XL réassurance','fort'],['Prévoyance entreprises','fort']],
 cats:[{t:'AXA IM asset mgmt croissance',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Buberl','5.8M€','Jan 2026']],
 peers:[{n:'Allianz',pe:11,pb:1.5,roe:14,div:5.2,evebitda:999},{n:'Zurich',pe:14,pb:2.8,roe:20,div:5.5,evebitda:999}],
 risks:{Cat:55,Reglement:50,Taux:45,Dommages:50,Devise:40,Liquidite:15},
 track:[{y:'2025',p:'EPS +8%',ok:'ok'},{y:'2024',p:'AXA XL record',ok:'ok'}],
 thesis:"AXA est le meilleur assureur mondial sur le risk/reward. 5.8% de dividende, rachat d'actions, hausse des taux favorise les rendements obligataires.",
 contra:"Exposition catastrophes naturelles croissante. Régulation Solvabilité II contraignante. Business model complexe."},

{ticker:'BNP',x2:'',x2s:'',name:'BNP Paribas',sector:'Banque',cap:'large',srd:true,idx:'CAC40',
 price:87.33,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-3.1,news5:'',dy_n:9,dy_med:6.6,div12:5.8,pe_lo:5.7,gmod:null,nih:'11520|10843|10298|9273',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:5.1,roemin:7.6,roem:8.4,grid:'banque',wht:0.0,irrn:10.0,irr:10.0,dq:'',vmult:null,hn:4,eveb_h:null,pfcf_h:2.1,pe_h:6.6,fcur:'EUR',unc:'elevee',vopt:115.06,vpess:46.57,nregu:3,regn:3,regu:3,place:'Paris',near:true,gsrc:'yahoo (4 ans publies)',gused:7.5,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:7.5,cagr:null,alarm:'',qwhy:'rentabilite fonds propres 8.4%',qok:false,nde:null,fcfc:null,roicx:null,chg:-2.48,mkt:'83Md€',b52h:113.82,b52l:65.12,beta:1.07,
 pe:7.78,pb:0.8,ev_ebitda:999,ps:1.87,pfcf:999,ev_ebit:null,
 roe:10.5,roic:null,roa:0.5,debt:999,de:null,ic:null,cr:null,qr:999,
 yield:7.2,epsg:37.4,revg:16.9,margin:26.5,gm:999,om:999,fcf:45.7,
 capex:1.2,capr:4.2,capda:0.36,
 dcfb:114.71,dcfm:87.66,dcfu:161.94,
 pio:6,alt:0.1,rsi:30.1,mm50:98.31,mm200:91.48,
 el:61.36,eh:70.13,stop:41.91,o1:115.06,o2:126.56,
 cb:12,ch:4,cs:2,tp:118.81,score:'D',rec:'avoid',zone:false,
 moat:[['Franchise banque universelle européenne','modere'],['CIB top 5 mondial','fort']],
 cats:[{t:'Hausse taux favorable NII',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Bonnafé','2.8M€','Jan 2026']],
 peers:[{n:'SocGen',pe:6,pb:0.4,roe:8,div:8.5,evebitda:999},{n:'Deutsche Bank',pe:7,pb:0.5,roe:9,div:4.8,evebitda:999}],
 risks:{Crédit:60,Régulation:65,Taux:50,Geopol:45,Technologie:40,Liquidite:20},
 track:[{y:'2025',p:'ROE 11%',ok:'ok'}],
 thesis:"BNP à 0.7x valeur comptable pour une banque qui génère 10% de ROE. Dividende 7.8% soutenable avec payout 55%.",
 contra:"Banques européennes souffrent d'une décote structurelle. Régulation Basel IV. CIB pro-cyclique."},

{ticker:'ACA',x2:'',x2s:'',name:'Crédit Agricole',sector:'Banque',cap:'large',srd:true,idx:'CAC40',
 price:15.3,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-2.9,news5:'',dy_n:9,dy_med:6.68,div12:1.7,pe_lo:5.6,gmod:null,nih:'6598|6358|5890|4894',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:5.3,roemin:7.4,roem:8.4,grid:'banque',wht:0.0,irrn:11.7,irr:11.7,dq:'',vmult:null,hn:4,eveb_h:null,pfcf_h:36.8,pe_h:5.9,fcur:'EUR',unc:'elevee',vopt:24.36,vpess:9.86,nregu:3,regn:3,regu:3,place:'Paris',near:true,gsrc:'yahoo (4 ans publies)',gused:10.5,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:10.5,cagr:null,alarm:'',qwhy:'rentabilite fonds propres 8.4%',qok:false,nde:null,fcfc:null,roicx:null,chg:-2.64,mkt:'38Md€',b52h:20.4,b52l:15.19,beta:0.82,
 pe:7.73,pb:0.66,ev_ebitda:999,ps:1.78,pfcf:999,ev_ebit:null,
 roe:8.6,roic:null,roa:0.3,debt:999,de:null,ic:null,cr:null,qr:999,
 yield:10.8,epsg:-14.8,revg:-6.3,margin:25.3,gm:999,om:999,fcf:38.6,
 capex:0.8,capr:4.3,capda:0.83,
 dcfb:20.71,dcfm:18.56,dcfu:29.23,
 pio:6,alt:0.03,rsi:23.9,mm50:17.53,mm200:16.5,
 el:12.99,eh:14.85,stop:8.87,o1:24.36,o2:26.8,
 cb:10,ch:5,cs:2,tp:21.0,score:'D',rec:'avoid',zone:false,
 moat:[['Réseau mutualiste unique','modere'],['Amundi asset management','fort']],
 cats:[{t:'Dividende 8.2% soutenable',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction CA','1.2M€','Fév 2026']],
 peers:[{n:'BNP Paribas',pe:7,pb:0.7,roe:10,div:7.8,evebitda:999}],
 risks:{Crédit:55,Régulation:60,Taux:45,Agricole:35,Immobilier:50,Liquidite:20},
 track:[{y:'2025',p:'Résultat net 7Md€',ok:'ok'}],
 thesis:"Crédit Agricole est la banque européenne la moins chère avec le rendement le plus élevé. Amundi est une mine d'or insuffisamment valorisée.",
 contra:"Structure mutualiste complexe. Exposition immobilier résidentiel. Marges retail sous pression des néobanques."},

{ticker:'GLE',x2:'',x2s:'',name:'Société Générale',sector:'Banque',cap:'large',srd:true,idx:'CAC40',
 price:62.27,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-3.0,news5:'',dy_n:9,dy_med:4.73,div12:1.75,pe_lo:5.0,gmod:null,nih:'5282|3480|1735|1229',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:3.5,roemin:1.8,roem:3.8,grid:'banque',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:null,pfcf_h:0.7,pe_h:8.2,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:62.6,gimp:null,knife:false,neglect:true,vmeth:'per',nig:62.6,cagr:null,alarm:'',qwhy:'rentabilite fonds propres 3.8%, pire annee 1.8%',qok:false,nde:null,fcfc:null,roicx:null,chg:-3.41,mkt:'24Md€',b52h:84.82,b52l:51.98,beta:0.99,
 pe:7.99,pb:0.64,ev_ebitda:999,ps:1.73,pfcf:999,ev_ebit:null,
 roe:9.5,roic:null,roa:0.5,debt:999,de:null,ic:null,cr:null,qr:999,
 yield:2.7,epsg:34.9,revg:4.1,margin:24.7,gm:999,om:999,fcf:-64.3,
 capex:0.9,capr:17.8,capda:0.91,
 dcfb:59.7,dcfm:70.23,dcfu:84.28,
 pio:5,alt:0.09,rsi:31.9,mm50:71.54,mm200:70.66,
 el:56.18,eh:64.61,stop:49.44,o1:73.74,o2:84.28,
 cb:10,ch:5,cs:4,tp:88.78,score:'C',rec:'avoid',zone:false,
 moat:[['CIB franchise','modere'],['Réseau retail France','modere']],
 cats:[{t:'Plan transformation 2026',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Koné','1.5M€','Mars 2026']],
 peers:[{n:'BNP Paribas',pe:7,pb:0.7,roe:10,div:7.8,evebitda:999}],
 risks:{Crédit:70,Régulation:70,Transformation:65,CIB:55,Réputation:50,Liquidite:25},
 track:[{y:'2025',p:'Retour à la rentabilité',ok:'partial'}],
 thesis:"SocGen à 0.4x l'actif net — décote extrême. Le nouveau CEO Krupa exécute un plan crédible. Un retour à 0.6x NAV implique +50%.",
 contra:"Historique de restructurations non tenues. CIB boîte noire. La décote peut persister longtemps."},

{ticker:'AIR',x2:'',x2s:'',name:'Airbus',sector:'Aéronautique',cap:'large',srd:true,idx:'CAC40',
 price:194.34,roiica:true,reinv:false,roiic:7.3,vmed:110.57,vepv:73.43,chg5:3.3,news5:'',dy_n:8,dy_med:1.6,div12:3.2,pe_lo:20.6,gmod:7.8,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'cyclique',wht:0.0,irrn:6.0,irr:6.0,dq:'',vmult:134.74,hn:4,eveb_h:13.4,pfcf_h:33.9,pe_h:29.3,fcur:'EUR',fcfh:'4031|3733|3204|3824',nih:'5221|4232|3789|4247',revh:'73420|69230|65446|58763',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:123.79,vpess:82.21,nregu:2,regn:3,regu:3,place:'Paris',mthreat:'chaine fournisseurs (moteurs), concurrent chinois COMAC a long terme',mtype:'duopole Airbus-Boeing, carnet de commandes de ~8 ans, barrieres colossales',mscore:5,near:false,gsrc:'communique 2026-10-05',gused:7.8,gimp:23.0,knife:false,neglect:false,vmeth:'qarp',nig:7.1,cagr:7.7,alarm:'',qwhy:'',qok:true,nde:-0.3,fcfc:85.0,roicx:127.3,chg:-2.25,mkt:'132Md€',b52h:221.3,b52l:157.42,beta:0.89,
 pe:25.88,pb:5.94,ev_ebitda:17.61,ps:2.0,pfcf:24,ev_ebit:22.3,
 roe:23.2,roic:31.7,roa:3.1,debt:0.55,de:0.55,ic:9.2,cr:1.15,qr:0.6,
 yield:1.6,epsg:125.8,revg:27.7,margin:7.7,gm:16.3,om:8,fcf:2.6,
 capex:3.8,capr:5.4,capda:1.27,
 dcfb:93.98,dcfm:110.57,dcfu:132.68,
 pio:8,alt:1.89,rsi:52.6,mm50:197.59,mm200:187.82,
 el:77.4,eh:88.46,stop:73.99,o1:123.79,o2:136.17,
 cb:18,ch:6,cs:1,tp:230.52,score:'B',rec:'hold',zone:false,
 moat:[['Duopole A320 avec Boeing','fort'],['Carnet 8000+ avions','fort']],
 cats:[{t:'Montée cadence A320 75/mois',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Faury','6.2M€','Jan 2026']],
 peers:[{n:'Boeing',pe:999,pb:999,roe:-40,div:0.0,evebitda:25},{n:'Embraer',pe:18,pb:3.2,roe:14,div:0.5,evebitda:12}],
 risks:{Supply:75,Devise:65,Boeing:40,Spatial:35,Geopol:30,Liquidite:15},
 track:[{y:'2025',p:'Livraisons 766 avions',ok:'partial'}],
 thesis:"Airbus a 8500 avions en carnet = 12 ans de production. Boeing en crise durable renforce la position d'Airbus.",
 contra:"Supply chain en crise. Objectifs de livraison manqués plusieurs années consécutives. Marge opérationnelle trop faible (8%)."},

{ticker:'KER',x2:'',x2s:'',name:'Kering',sector:'Luxe',cap:'large',srd:true,idx:'CAC40',
 price:214.95,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.9,news5:'',dy_n:10,dy_med:2.09,div12:4.0,pe_lo:16.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:10.0,pfcf_h:18.9,pe_h:16.4,fcur:'EUR',fcfh:'2270|1400|1848|3207',nih:'72|1133|2983|3614',revh:'14675|16874|19566|20351',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-41.6,gimp:null,knife:true,neglect:false,vmeth:'per',nig:-72.9,cagr:-10.3,alarm:'',qwhy:'ROIC hors EA 10.9, ROIC 8.3, dette/EBITDA 4.43, croissance CA -10.3%',qok:false,nde:4.43,fcfc:112.0,roicx:10.9,chg:-0.92,mkt:'24Md€',b52h:354.2,b52l:203.2,beta:1.0,
 pe:22.37,pb:1.82,ev_ebitda:14.66,ps:1.82,pfcf:12,ev_ebit:34.3,
 roe:-1.6,roic:8.3,roa:2.5,debt:1.17,de:1.17,ic:1.7,cr:2.05,qr:0.9,
 yield:1.4,epsg:-60.1,revg:-2.9,margin:-1.5,gm:72.1,om:18,fcf:8.6,
 capex:4.2,capr:5.7,capda:0.41,
 dcfb:150.88,dcfm:177.51,dcfu:213.01,
 pio:6,alt:1.29,rsi:41.6,mm50:236.49,mm200:253.16,
 el:138.46,eh:161.89,stop:121.84,o1:186.39,o2:213.01,
 cb:8,ch:8,cs:6,tp:264.24,score:'D',rec:'avoid',zone:false,
 moat:[['Gucci brand','modere'],['Saint Laurent','modere']],
 cats:[{t:'Rebranding Gucci phase 2',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','François-Henri Pinault','45M€','Fév 2026']],
 peers:[{n:'LVMH',pe:22,pb:5.1,roe:24,div:2.4,evebitda:14},{n:'Hermès',pe:50,pb:22,roe:36,div:0.6,evebitda:32}],
 risks:{Gucci:80,Chine:70,Direction:60,Cyclicite:55,Devise:45,Liquidite:20},
 track:[{y:'2025',p:'Gucci revenus -12%',ok:'m'}],
 thesis:"Kering est la grande décotée du luxe. À 2x livre, si Gucci retrouve 15% de marge, le titre double.",
 contra:"Gucci = 60% des profits et est en crise depuis 2023. Sabato De Sarno n'a pas encore convaincu."},

{ticker:'PUB',x2:'',x2s:'',name:'Publicis',sector:'Communication',cap:'large',srd:true,idx:'CAC40',
 price:101.55,roiica:false,reinv:false,roiic:49.9,vmed:null,vepv:null,chg5:2.8,news5:'',dy_n:9,dy_med:3.7,div12:3.75,pe_lo:12.3,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:7.9,pfcf_h:9.7,pe_h:14.2,fcur:'EUR',fcfh:'2693|2063|1868|2219',nih:'1653|1660|1312|1222',revh:'17399|16030|14802|14196',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:8.8,gimp:null,knife:false,neglect:false,vmeth:'per',nig:10.6,cagr:7.0,alarm:'',qwhy:'ROIC hors EA None',qok:false,nde:0.51,fcfc:151.0,roicx:null,chg:-0.88,mkt:'16Md€',b52h:105.2,b52l:68.14,beta:0.64,
 pe:15.82,pb:2.41,ev_ebitda:9.87,ps:1.44,pfcf:12,ev_ebit:11.8,
 roe:16.2,roic:13.9,roa:4.3,debt:0.52,de:0.52,ic:12.1,cr:0.94,qr:0.9,
 yield:3.7,epsg:-3.1,revg:3.0,margin:9.2,gm:46.7,om:18,fcf:10.6,
 capex:1.2,capr:1.4,capda:0.34,
 dcfb:67.17,dcfm:79.02,dcfu:94.82,
 pio:6,alt:1.13,rsi:60.3,mm50:99.08,mm200:84.11,
 el:66.38,eh:73.96,stop:58.41,o1:82.97,o2:94.82,
 cb:14,ch:6,cs:2,tp:114.38,score:'D',rec:'avoid',zone:false,
 moat:[['Epsilon data assets 250M profils','fort'],['Sapient tech consulting','modere']],
 cats:[{t:'IA générative pub révolution',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Lévy','3.8M€','Jan 2026']],
 peers:[{n:'WPP',pe:9,pb:1.8,roe:18,div:6.2,evebitda:7},{n:'Omnicom',pe:12,pb:3.5,roe:28,div:3.2,evebitda:9}],
 risks:{IA:55,Clients:45,Devise:50,Cyclicite:40,Concurrence:35,Liquidite:15},
 track:[{y:'2025',p:'Organique +6%',ok:'ok'}],
 thesis:"Publicis a réinventé son modèle autour des données. Epsilon est un actif de données sans équivalent. Gagne des parts de marché depuis 4 ans sur WPP.",
 contra:"L'IA générative menace les métiers créatifs. WPP contre-attaque agressivement."},

{ticker:'ORA',x2:'',x2s:'',name:'Orange',sector:'Télécoms',cap:'large',srd:true,idx:'CAC40',
 price:14.2,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:3.4,news5:'',dy_n:10,dy_med:5.72,div12:0.75,pe_lo:10.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:2.1,pfcf_h:9.1,pe_h:11.4,fcur:'EUR',fcfh:'3313|3167|4092|2458',nih:'538|2350|2440|2146',revh:'40397|40259|39677|39128',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-17.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-36.9,cagr:1.1,alarm:'',qwhy:'ROIC 9.9, croissance CA 1.1%',qok:false,nde:-0.39,fcfc:174.0,roicx:35.9,chg:-2.51,mkt:'30Md€',b52h:18.8,b52l:13.49,beta:0.27,
 pe:13.27,pb:1.19,ev_ebitda:7.21,ps:0.91,pfcf:8,ev_ebit:24.9,
 roe:14.2,roic:9.9,roa:3.3,debt:1.61,de:1.61,ic:2.6,cr:0.87,qr:0.7,
 yield:5.2,epsg:3,revg:5.5,margin:10.0,gm:41.1,om:12,fcf:8.8,
 capex:14.8,capr:18.5,capda:0.89,
 dcfb:12.32,dcfm:14.5,dcfu:17.4,
 pio:6,alt:0.79,rsi:45.1,mm50:15.04,mm200:16.28,
 el:12.18,eh:13.57,stop:10.72,o1:15.23,o2:17.4,
 cb:8,ch:6,cs:4,tp:18.99,score:'D',rec:'avoid',zone:false,
 moat:[['Réseau fibre/5G France','modere'],['Afrique forte croissance','modere']],
 cats:[{t:'Afrique MoMo scaling',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Olam','0.8M€','Jan 2026']],
 peers:[{n:'Bouygues Telecom',pe:14,pb:1.2,roe:8,div:5.8,evebitda:6},{n:'Deutsche Telekom',pe:14,pb:2.1,roe:12,div:4.2,evebitda:6}],
 risks:{Régulation:65,CAPEX:70,Concurrence:60,Dette:55,Afrique:40,Liquidite:20},
 track:[{y:'2025',p:'Dividende 0.72€ maintenu',ok:'ok'}],
 thesis:"Orange 7.2% de dividende couvert par le FCF. L'Afrique (30% CA) croît à 15%/an. À 5x EV/EBITDA, décote vs pairs injustifiée.",
 contra:"CAPEX permanent détruit la valeur. Marché français mature et hyper-concurrentiel."},

{ticker:'VIE',x2:'',x2s:'',name:'Veolia',sector:'Eau & Déchets',cap:'large',srd:true,idx:'CAC40',
 price:31.93,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.1,news5:'',dy_n:10,dy_med:4.26,div12:1.5,pe_lo:17.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.5,pfcf_h:4.1,pe_h:20.0,fcur:'EUR',fcfh:'5153|5038|5005|4148',nih:'1217|1098|937|716',revh:'44396|44692|45351|42886',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:10.2,gimp:null,knife:false,neglect:false,vmeth:'per',nig:19.3,cagr:1.2,alarm:'',qwhy:'ROIC 8.8, croissance CA 1.2%',qok:false,nde:2.03,fcfc:488.0,roicx:17.4,chg:-1.45,mkt:'20Md€',b52h:37.66,b52l:27.85,beta:0.98,
 pe:18.56,pb:3.28,ev_ebitda:8.77,ps:0.53,pfcf:14,ev_ebit:15.8,
 roe:13.4,roic:8.8,roa:3.1,debt:2.5,de:2.5,ic:3.7,cr:0.82,qr:0.8,
 yield:4.6,epsg:5.6,revg:0.7,margin:2.8,gm:17.9,om:8,fcf:21.7,
 capex:8.2,capr:null,capda:null,
 dcfb:30.0,dcfm:35.3,dcfu:42.36,
 pio:7,alt:0.85,rsi:53.1,mm50:32.2,mm200:33.12,
 el:29.3,eh:32.9,stop:25.78,o1:37.06,o2:42.36,
 cb:12,ch:6,cs:2,tp:38.56,score:'C',rec:'avoid',zone:false,
 moat:[['Concessions eau 30 ans','fort'],['Suez intégration','modere']],
 cats:[{t:'Synergies Suez 500M€',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Frerot','2.1M€','Jan 2026']],
 peers:[{n:'Suez',pe:18,pb:2.5,roe:12,div:3.8,evebitda:9}],
 risks:{Régulation:55,Taux:50,CAPEX:60,Politique:45,Devise:40,Liquidite:20},
 track:[{y:'2025',p:'Synergies Suez +480M€',ok:'ok'}],
 thesis:"Veolia est le leader mondial de l'eau — actif de plus en plus rare. La fusion Suez crée un géant avec des économies d'échelle massives.",
 contra:"Dette élevée post-fusion. Régulation tarifaire peut bloquer la transmission des coûts."},

{ticker:'RNO',x2:'',x2s:'',name:'Renault',sector:'Automobile',cap:'mid',srd:true,idx:'CAC40',
 price:27.28,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.6,news5:'',dy_n:7,dy_med:4.23,div12:2.2,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:8.8,pfcf_h:7.7,pe_h:11.3,fcur:'EUR',fcfh:'-705|4111|1398|929',nih:'-10931|752|2198|-354',revh:'57922|56232|52376|46328',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:7.7,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:7.7,alarm:'',qwhy:'ROIC hors EA 2.1, ROIC 2.1, cash None%, dette/EBITDA None',qok:false,nde:null,fcfc:null,roicx:2.1,chg:-1.12,mkt:'13Md€',b52h:37.97,b52l:24.38,beta:0.86,
 pe:8.34,pb:0.38,ev_ebitda:9.76,ps:0.13,pfcf:6,ev_ebit:null,
 roe:5.0,roic:2.1,roa:1.8,debt:3.28,de:3.28,ic:-25.0,cr:1.03,qr:0.9,
 yield:8.0,epsg:8,revg:9.4,margin:1.6,gm:17.9,om:6,fcf:-8.9,
 capex:6.2,capr:5.3,capda:0.72,
 dcfb:41.56,dcfm:48.89,dcfu:58.67,
 pio:5,alt:0.15,rsi:52.4,mm50:27.73,mm200:27.95,
 el:39.11,eh:44.98,stop:34.42,o1:51.33,o2:58.67,
 cb:8,ch:7,cs:6,tp:38.62,score:'C',rec:'avoid',zone:false,
 moat:[['Ampere VE platform','modere'],['Alliance Nissan','modere']],
 cats:[{t:'Renault 5 électrique succès',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','État français','150M€','Déc 2025']],
 peers:[{n:'Stellantis',pe:4,pb:0.4,roe:8,div:5.5,evebitda:2},{n:'Volkswagen',pe:4,pb:0.4,roe:6,div:6.8,evebitda:2}],
 risks:{VE:75,Chine:70,Alliance:60,Devise:55,Cyclicite:65,Liquidite:25},
 track:[{y:'2025',p:'Marge op. 7.5%',ok:'ok'}],
 thesis:"Renault sous-valorisé : Ampere + HORSE + marque. À 0.5x livre, le marché paye zéro pour la plateforme VE.",
 contra:"Transition VE incertaine. Alliance Nissan fragile. Concurrence chinoise déferle."},

{ticker:'SGO',x2:'',x2s:'',name:'Saint-Gobain',sector:'Matériaux construction',cap:'large',srd:true,idx:'CAC40',
 price:66.42,roiica:false,reinv:false,roiic:4.2,vmed:null,vepv:null,chg5:1.9,news5:'',dy_n:9,dy_med:2.91,div12:2.3,pe_lo:7.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:6.3,pfcf_h:10.1,pe_h:13.6,fcur:'EUR',fcfh:'3448|3486|4064|3790',nih:'2883|2844|2669|3003',revh:'46483|46571|47944|51197',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-2.3,gimp:null,knife:false,neglect:true,vmeth:'per',nig:-1.4,cagr:-3.2,alarm:'',qwhy:'ROIC 10.9, croissance CA -3.2%',qok:false,nde:1.35,fcfc:130.0,roicx:19.0,chg:-0.18,mkt:'36Md€',b52h:91.3,b52l:63.52,beta:1.23,
 pe:12.32,pb:1.28,ev_ebitda:6.8,ps:0.7,pfcf:10,ev_ebit:9.1,
 roe:11.0,roic:10.9,roa:5.1,debt:0.66,de:0.66,ic:5.2,cr:1.27,qr:1.0,
 yield:3.5,epsg:-12.0,revg:-1.1,margin:5.8,gm:27.2,om:10,fcf:10.6,
 capex:5.8,capr:4.7,capda:0.83,
 dcfb:63.36,dcfm:74.54,dcfu:89.45,
 pio:8,alt:2.21,rsi:38.5,mm50:73.09,mm200:76.1,
 el:61.87,eh:69.47,stop:54.45,o1:78.27,o2:89.45,
 cb:14,ch:5,cs:2,tp:95.84,score:'C',rec:'avoid',zone:false,
 moat:[['Isolation thermique leader','fort'],['Distribution réseau dense','modere']],
 cats:[{t:'Rénovation énergétique EU',w:'2026-2030',c:'var(--gn)'}],
 ins:[['Achat','CEO Guillemot','4.2M€','Jan 2026']],
 peers:[{n:'Kingspan',pe:22,pb:4.2,roe:20,div:0.8,evebitda:14}],
 risks:{Construction:65,Taux:60,Cyclicite:55,Energie:45,Devise:40,Liquidite:15},
 track:[{y:'2025',p:'Marge op. 10% record',ok:'ok'}],
 thesis:"Saint-Gobain est le grand bénéficiaire de la rénovation énergétique européenne obligatoire. À 12x PE avec 3.2% de dividende.",
 contra:"Exposition forte à la construction neuve en baisse. Taux élevés pèsent sur l'immobilier."},

{ticker:'CAP',x2:'',x2s:'',name:'Capgemini',sector:'Services informatiques',cap:'large',srd:true,idx:'CAC40',
 price:123.15,roiica:true,reinv:false,roiic:2.5,vmed:null,vepv:null,chg5:6.8,news5:'',dy_n:10,dy_med:1.64,div12:3.4,pe_lo:14.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:9.8,pfcf_h:12.0,pe_h:16.5,fcur:'EUR',fcfh:'2195|2211|2266|2227',nih:'1601|1671|1663|1547',revh:'22465|22096|22522|21995',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:0.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:1.2,cagr:0.7,alarm:'',qwhy:'croissance CA 0.7%',qok:false,nde:2.17,fcfc:137.0,roicx:68.3,chg:1.48,mkt:'24Md€',b52h:153.05,b52l:85.62,beta:0.66,
 pe:15.65,pb:1.78,ev_ebitda:9.2,ps:0.87,pfcf:14,ev_ebit:12.0,
 roe:12.2,roic:12.2,roa:6.0,debt:0.88,de:0.88,ic:12.0,cr:1.28,qr:1.2,
 yield:2.8,epsg:-30.7,revg:8.8,margin:5.9,gm:26.8,om:13,fcf:10.7,
 capex:1.8,capr:1.3,capda:0.41,
 dcfb:136.08,dcfm:160.09,dcfu:192.11,
 pio:5,alt:2.17,rsi:71.2,mm50:108.79,mm200:104.58,
 el:121.67,eh:144.72,stop:107.07,o1:168.09,o2:192.11,
 cb:14,ch:7,cs:2,tp:141.98,score:'C',rec:'avoid',zone:false,
 moat:[['Expertise sectorielle profonde','modere'],['Partenariats hyperscalers','modere']],
 cats:[{t:'IA générative revenus 2Md€',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Fernandez','2.8M€','Jan 2026']],
 peers:[{n:'Accenture',pe:25,pb:8,roe:35,div:1.8,evebitda:18},{n:'Sopra Steria',pe:14,pb:2.2,roe:12,div:3.2,evebitda:9}],
 risks:{IA:60,Concurrence:55,Macro:50,Offshoring:45,Devise:50,Liquidite:15},
 track:[{y:'2025',p:'IA book 2Md€',ok:'ok'}],
 thesis:"Capgemini est le premier bénéficiaire de la transformation IA des grandes entreprises. Pipeline IA générative 2Md€.",
 contra:"Croissance ralentit en Europe. Concurrence Accenture féroce."},

{ticker:'DG',x2:'',x2s:'',name:'Vinci',sector:'Construction & Concessions',cap:'large',srd:true,idx:'CAC40',
 price:106.65,roiica:false,reinv:false,roiic:27.4,vmed:119.83,vepv:76.88,chg5:0.1,news5:'',dy_n:10,dy_med:3.06,div12:5.05,pe_lo:11.4,gmod:2.6,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:11.1,irr:11.1,dq:'',vmult:119.83,hn:4,eveb_h:6.6,pfcf_h:8.7,pe_h:13.0,fcur:'EUR',fcfh:'8013|7662|7208|5886',nih:'4903|4863|4702|4259',revh:'75702|72768|69885|62514',yrs:'2025|2024|2023|2022',unc:'faible',vopt:166.94,vpess:138.91,nregu:3,regn:3,regu:3,place:'Paris',mthreat:'fin des concessions autoroutieres francaises (annees 2030), fiscalite',mtype:'concessions (autoroutes, aeroports) : actifs uniques a revenus indexes',mscore:4,near:true,gsrc:'communique 2026-10-05',gused:2.6,gimp:-5.0,knife:false,neglect:false,vmeth:'qarp',nig:4.8,cagr:6.6,alarm:'',qwhy:'croissance officielle 2.6%',qok:false,nde:1.5,fcfc:154.0,roicx:21.4,chg:-1.3,mkt:'88Md€',b52h:143.15,b52l:104.25,beta:0.74,
 pe:11.84,pb:1.93,ev_ebitda:6.99,ps:0.78,pfcf:12,ev_ebit:9.5,
 roe:16.3,roic:13.1,roa:4.4,debt:1.21,de:1.21,ic:6.3,cr:0.82,qr:1.0,
 yield:4.7,epsg:10.8,revg:2.3,margin:6.7,gm:17.0,om:9,fcf:13.6,
 capex:3.8,capr:5.1,capda:0.92,
 dcfb:129.81,dcfm:152.72,dcfu:183.26,
 pio:7,alt:1.14,rsi:42.8,mm50:111.68,mm200:120.84,
 el:122.18,eh:137.45,stop:125.02,o1:166.94,o2:183.63,
 cb:16,ch:5,cs:1,tp:142.2,score:'C',rec:'avoid',zone:false,
 moat:[['Concessions autoroutes/aéroports','fort'],['Énergie renouvelable Cobra IS','fort']],
 cats:[{t:'Aéroports trafic record',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Huillard','8.2M€','Jan 2026']],
 peers:[{n:'Bouygues',pe:12,pb:1.8,roe:14,div:4.2,evebitda:7},{n:'Eiffage',pe:13,pb:2.5,roe:18,div:3.8,evebitda:8}],
 risks:{Taux:45,Construction:40,Politique:35,Régulation:40,Devise:35,Liquidite:10},
 track:[{y:'2025',p:'EBITDA +8%',ok:'ok'},{y:'2024',p:'Acquisitions Cobra IS',ok:'ok'}],
 thesis:"Vinci est le meilleur actif d'infrastructure de France. Concessions 30-50 ans = cash flows prévisibles. Cobra IS en ENR est une mine d'or émergente.",
 contra:"Exposition bâtiment cyclique. Régulation autoroutière peut être remise en cause."},

{ticker:'VIV',x2:'',x2s:'',name:'Vivendi',sector:'Médias',cap:'large',srd:true,idx:'CAC40',
 price:1.56,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:6.4,news5:'',dy_n:9,dy_med:5.09,div12:0.04,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 78.0 contre 15.2 attendu) · croissance Yahoo -68.3 %/an : probablement faussee par une acquisition ou une cession',vmult:null,hn:2,eveb_h:48.2,pfcf_h:10.5,pe_h:70.7,fcur:'EUR',fcfh:'-68|1837|946|363',nih:'20|-6004|405|-1010',revh:'307|297|312|9595',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-68.3,gimp:null,knife:true,neglect:false,vmeth:'per',nig:null,cagr:-68.3,alarm:'',qwhy:'ROIC hors EA 0.4, ROIC 0.1, cash None%, dette/EBITDA 7.05, perte exploitation, croissance CA -68.3%',qok:false,nde:7.05,fcfc:null,roicx:0.4,chg:-0.38,mkt:'3.8Md€',b52h:3.21,b52l:1.4,beta:1.04,
 pe:78.05,pb:0.34,ev_ebitda:-50.43,ps:5.15,pfcf:10,ev_ebit:27.2,
 roe:0.3,roic:0.1,roa:-0.9,debt:0.39,de:0.39,ic:1.2,cr:0.49,qr:0.8,
 yield:2.5,epsg:-6.6,revg:-3.4,margin:6.0,gm:32.1,om:9,fcf:-4.4,
 capex:1.2,capr:1.0,capda:0.06,
 dcfb:0.88,dcfm:1.03,dcfu:1.24,
 pio:6,alt:0.97,rsi:59.9,mm50:1.54,mm200:1.95,
 el:0.87,eh:0.96,stop:0.77,o1:1.08,o2:1.24,
 cb:6,ch:5,cs:3,tp:2.12,score:'D',rec:'avoid',zone:false,
 moat:[['Canal+ Afrique','modere'],['Havas pub','modere']],
 cats:[{t:'Canal+ cotation Londres',w:'T1 2026',c:'var(--gn)'}],
 ins:[['Achat','Bolloré via Compagnie','180M€','Jan 2026']],
 peers:[{n:'Lagardère',pe:14,pb:2.1,roe:10,div:3.5,evebitda:9}],
 risks:{Médias:70,Bolloré:65,Politique:60,Digital:65,Régulation:55,Liquidite:25},
 track:[{y:'2025',p:'Spin-offs Canal+/Havas',ok:'partial'}],
 thesis:"Vivendi vaut plus mort que vivant. Les spin-offs révèlent une valeur cachée. À 0.6x actif net, la somme des parties est 2x le cours.",
 contra:"Bolloré contrôle — risque gouvernance fort. Médias en déclin structurel."},

{ticker:'RI',x2:'',x2s:'',name:'Pernod Ricard',sector:'Spiritueux',cap:'large',srd:true,idx:'CAC40',
 price:67.46,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:8.0,news5:'',dy_n:10,dy_med:1.91,div12:4.7,pe_lo:13.4,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:11.9,pfcf_h:26.8,pe_h:17.7,fcur:'EUR',fcfh:'1188|1121|954|1331',nih:'1203|1626|1476|2262',revh:'9403|10959|11598|12137',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-13.6,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-19.0,cagr:-8.2,alarm:'',qwhy:'ROIC hors EA 9.9, ROIC 7.4, cash 70.0%, dette/EBITDA 4.06, croissance CA -8.2%',qok:false,nde:4.06,fcfc:70.0,roicx:9.9,chg:-1.11,mkt:'24Md€',b52h:90.34,b52l:57.86,beta:0.52,
 pe:14.14,pb:1.1,ev_ebitda:11.01,ps:1.81,pfcf:15,ev_ebit:13.1,
 roe:7.6,roic:7.4,roa:4.1,debt:0.77,de:0.77,ic:4.5,cr:2.47,qr:1.0,
 yield:6.9,epsg:-47.8,revg:-13.2,margin:12.8,gm:58.4,om:25,fcf:7.0,
 capex:3.2,capr:4.2,capda:0.95,
 dcfb:85.27,dcfm:100.32,dcfu:120.38,
 pio:5,alt:1.63,rsi:69.5,mm50:63.15,mm200:65.48,
 el:78.25,eh:91.49,stop:68.86,o1:105.34,o2:120.38,
 cb:10,ch:7,cs:4,tp:80.45,score:'C',rec:'avoid',zone:false,
 moat:[['Jameson whiskey leader','fort'],['Absolut vodka','modere']],
 cats:[{t:'Normalisation stocks US/Chine',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Ricard','3.2M€','Jan 2026']],
 peers:[{n:'Diageo',pe:16,pb:5.8,roe:35,div:3.8,evebitda:14}],
 risks:{Chine:70,US:65,Santé:55,Devise:50,Cyclicite:45,Liquidite:20},
 track:[{y:'2025',p:'Volumes -8% vs guidance',ok:'m'}],
 thesis:"Pernod est en bas de cycle. La normalisation US et Chine est en cours. Jameson est la marque whiskey à la croissance la plus rapide au monde.",
 contra:"La Chine déçoit depuis 18 mois. Objectifs manqués régulièrement. Dette élevée."},

{ticker:'LR',x2:'',x2s:'',name:'Legrand',sector:'Électricité bâtiment',cap:'large',srd:true,idx:'CAC40',
 price:131.3,roiica:false,reinv:false,roiic:11.7,vmed:115.36,vepv:39.39,chg5:-5.9,news5:'',dy_n:10,dy_med:2.05,div12:2.38,pe_lo:20.0,gmod:8.3,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:7.8,irr:7.8,dq:'',vmult:121.63,hn:4,eveb_h:13.0,pfcf_h:19.1,pe_h:21.1,fcur:'EUR',fcfh:'1328|1284|1583|1030',nih:'1245|1166|1148|1000',revh:'9481|8649|8417|8339',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:131.65,vpess:79.53,nregu:3,regn:3,regu:3,place:'Paris',mthreat:'cycle construction, valorisation tendue',mtype:'marques installateurs et distribution, pouvoir de prix, data centers',mscore:4,near:false,gsrc:'communique 2026-10-06',gused:8.35,gimp:11.3,knife:false,neglect:false,vmeth:'qarp',nig:7.6,cagr:4.4,alarm:'',qwhy:'',qok:true,nde:1.87,fcfc:115.0,roicx:35.3,chg:-2.01,mkt:'26Md€',b52h:166.95,b52l:121.95,beta:0.96,
 pe:26.42,pb:4.59,ev_ebitda:18.45,ps:3.41,pfcf:20,ev_ebit:22.0,
 roe:18.2,roic:12.1,roa:6.6,debt:1.03,de:1.03,ic:11.1,cr:1.58,qr:1.2,
 yield:1.8,epsg:8.5,revg:14.7,margin:13.0,gm:50.2,om:21,fcf:3.9,
 capex:2.2,capr:2.6,capda:0.61,
 dcfb:98.06,dcfm:115.36,dcfu:138.43,
 pio:6,alt:3.65,rsi:39.6,mm50:138.17,mm200:139.89,
 el:86.52,eh:98.06,stop:71.58,o1:131.65,o2:144.82,
 cb:14,ch:6,cs:2,tp:169.22,score:'C',rec:'hold',zone:false,
 moat:[['Électricité bâtiment spécialisée','fort'],['Data center power management','fort']],
 cats:[{t:'Data center infrastructure boom',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Verspieren','5.8M€','Jan 2026']],
 peers:[{n:'Schneider',pe:28,pb:6.8,roe:26,div:1.5,evebitda:18}],
 risks:{Data:35,Bâtiment:45,Devise:40,Taux:35,Cyclicite:30,Liquidite:10},
 track:[{y:'2025',p:'Croissance organique +9%',ok:'ok'},{y:'2024',p:'Data center +20%',ok:'ok'}],
 thesis:"Legrand — 24 années de hausse du BPA. Data centers = 25% du CA croissant à 20%/an. Famille aux commandes = alignement parfait.",
 contra:"Valorisation premium. Exposition bâtiment résidentiel qui souffre des taux."},

{ticker:'WLN',x2:'',x2s:'',name:'Wendel',sector:'Holdings',cap:'large',srd:true,idx:'CAC40',
 price:11.74,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:9.5,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:15.7,pfcf_h:8.2,pe_h:34.4,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:null,regn:null,regu:null,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:true,neglect:false,vmeth:'per',nig:null,cagr:null,alarm:'',qwhy:'holding (grille dediee a venir)',qok:false,nde:null,fcfc:null,roicx:null,chg:-0.94,mkt:'4.8Md€',b52h:30.61,b52l:9.05,beta:1.86,
 pe:3.41,pb:0.18,ev_ebitda:9.59,ps:0.17,pfcf:9,ev_ebit:null,
 roe:-21.2,roic:null,roa:0.2,debt:0.67,de:0.67,ic:-54.4,cr:1.1,qr:1.2,
 yield:3.2,epsg:6,revg:-3.7,margin:-25.2,gm:66.1,om:16,fcf:31.1,
 capex:1.2,capr:6.2,capda:0.7,
 dcfb:21.96,dcfm:25.83,dcfu:31.0,
 pio:6,alt:-1.16,rsi:53.2,mm50:12.32,mm200:12.45,
 el:20.66,eh:23.76,stop:18.18,o1:27.12,o2:31.0,
 cb:8,ch:5,cs:2,tp:12.1,score:'C',rec:'avoid',zone:false,
 moat:[['Bureau Veritas 40%','fort']],
 cats:[{t:'Bureau Veritas croissance',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Wendel','12M€','Jan 2026']],
 peers:[{n:'Eurazeo',pe:12,pb:0.8,roe:9,div:2.8,evebitda:9}],
 risks:{Holdings:40,Bureau:35,Devise:35,Liquidite:30,Concentration:45,Opacité:40},
 track:[{y:'2025',p:'ANR +8%',ok:'ok'}],
 thesis:"Wendel à 30% de décote sur ANR. Bureau Veritas seul représente plus que la cap de Wendel.",
 contra:"Holdings décotés structurellement. Opacité de la valorisation."},

{ticker:'DSY',x2:'',x2s:'',name:'Dassault Systèmes',sector:'Logiciels',cap:'large',srd:true,idx:'CAC40',
 price:23.29,roiica:false,reinv:false,roiic:null,vmed:18.58,vepv:10.79,chg5:5.1,news5:'',dy_n:10,dy_med:0.53,div12:0.27,pe_lo:25.8,gmod:4.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:7.3,irr:7.3,dq:'',vmult:18.58,hn:4,eveb_h:21.5,pfcf_h:30.4,pe_h:41.4,fcur:'EUR',fcfh:'1469|1466|1420|1393',nih:'1196|1200|1051|932',revh:'6236|6214|5951|5665',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:21.33,vpess:15.57,nregu:2,regn:3,regu:3,place:'Paris',mthreat:'transition cloud/IA mal negociee, croissance faible',mtype:'couts de changement eleves (CATIA, SolidWorks standards de l industrie)',mscore:4,near:false,gsrc:'communique 2026-10-05',gused:4.0,gimp:9.0,knife:false,neglect:false,vmeth:'qarp',nig:8.7,cagr:3.2,alarm:'',qwhy:'',qok:true,nde:-0.47,fcfc:131.0,roicx:37.2,chg:0.82,mkt:'42Md€',b52h:30.36,b52l:15.82,beta:0.57,
 pe:24.01,pb:3.31,ev_ebitda:16.81,ps:4.93,pfcf:24,ev_ebit:18.9,
 roe:15.1,roic:14.4,roa:6.3,debt:0.36,de:0.36,ic:35.6,cr:1.99,qr:1.8,
 yield:1.2,epsg:31.8,revg:2.2,margin:21.3,gm:84.2,om:24,fcf:4.8,
 capex:1.8,capr:2.6,capda:0.29,
 dcfb:15.85,dcfm:18.65,dcfu:22.38,
 pio:8,alt:3.88,rsi:73.6,mm50:21.61,mm200:19.83,
 el:13.99,eh:15.85,stop:14.01,o1:21.33,o2:23.46,
 cb:15,ch:7,cs:2,tp:23.32,score:'B',rec:'hold',zone:false,
 moat:[['3DEXPERIENCE platform','fort'],['Switching costs','fort'],['Life sciences','fort']],
 cats:[{t:'IA intégrée 3DEXPERIENCE',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Dassault','180M€','Déc 2025']],
 peers:[{n:'PTC',pe:32,pb:8,roe:25,div:0.0,evebitda:22},{n:'Autodesk',pe:35,pb:12,roe:40,div:0.0,evebitda:26}],
 risks:{Cyclicite:50,Concurrence:55,Devise:45,Cloud:40,Croissance:35,Liquidite:15},
 track:[{y:'2025',p:'Revenus récurrents 80%+',ok:'ok'}],
 thesis:"Dassault Systèmes construit le jumeau numérique de l'industrie mondiale. À 32€, correction significative depuis 42€ — point d'entrée intéressant.",
 contra:"Transition cloud plus lente que prévu. Croissance en dessous des attentes sur 18 mois."},

{ticker:'STM',x2:'',x2s:'',name:'STMicroelectronics',sector:'Semi-conducteurs',cap:'large',srd:true,idx:'CAC40',
 price:41.2,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-9.6,news5:'',dy_n:10,dy_med:1.08,div12:0.321,pe_lo:8.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 1373.3 contre 17.3 attendu)',vmult:null,hn:4,eveb_h:6.6,pfcf_h:25.7,pe_h:12.3,fcur:'USD',fcfh:'-52|-216|1456|1566',nih:'166|1557|4211|3960',revh:'11800|13269|17286|16128',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-37.6,gimp:null,knife:true,neglect:false,vmeth:'per',nig:-65.3,cagr:-9.9,alarm:'',qwhy:'cash 28.0%, croissance CA -9.9%',qok:false,nde:-0.21,fcfc:28.0,roicx:17.6,chg:0.07,mkt:'20Md€',b52h:70.85,b52l:18.2,beta:1.48,
 pe:1373.33,pb:2.34,ev_ebitda:12.69,ps:2.82,pfcf:12,ev_ebit:77.7,
 roe:2.7,roic:17.3,roa:2.1,debt:0.23,de:0.23,ic:8.3,cr:2.78,qr:1.8,
 yield:0.8,epsg:8,revg:26.1,margin:3.6,gm:34.5,om:14,fcf:-0.1,
 capex:12.5,capr:null,capda:null,
 dcfb:64.86,dcfm:76.31,dcfu:91.57,
 pio:6,alt:5.02,rsi:35.3,mm50:44.97,mm200:42.99,
 el:54.94,eh:67.76,stop:48.35,o1:80.13,o2:91.57,
 cb:12,ch:6,cs:4,tp:68.91,score:'C',rec:'avoid',zone:false,
 moat:[['SiC véhicules électriques leader','fort'],['Microcontrôleurs embarqués','fort']],
 cats:[{t:'SiC rebond VE T3 2026',w:'T3 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Caulfield','4.2M€','Jan 2026']],
 peers:[{n:'Infineon',pe:18,pb:2.2,roe:14,div:1.2,evebitda:9},{n:'NXP Semi',pe:16,pb:3.5,roe:22,div:2.8,evebitda:10}],
 risks:{VE:75,Inventaires:70,Chine:60,CAPEX:65,Cyclicite:70,Liquidite:15},
 track:[{y:'2025',p:'Revenues -23% vs guidance',ok:'m'}],
 thesis:"STM est le leader SiC mondial pour les VE. La correction de -60% depuis le pic est une opportunité si les VE reprennent. À 1.8x livre avec un bilan sain.",
 contra:"Ralentissement VE plus long que prévu. Inventaires encore élevés. Tesla a réduit ses commandes SiC."},

{ticker:'EL',x2:'',x2s:'',name:'EssilorLuxottica',sector:'Optique',cap:'large',srd:true,idx:'CAC40',
 price:152.05,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:3.6,news5:'',dy_n:10,dy_med:1.42,div12:4.0,pe_lo:34.3,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:16.1,pfcf_h:27.7,pe_h:39.8,fcur:'EUR',fcfh:'3766|3352|3330|3211',nih:'2315|2359|2289|2152',revh:'28491|26508|25395|24494',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:3.9,gimp:null,knife:true,neglect:false,vmeth:'per',nig:2.5,cagr:5.2,alarm:'Piotroski 4/9',qwhy:'ROIC hors EA 14.2, ROIC 5.3',qok:false,nde:1.64,fcfc:150.0,roicx:14.2,chg:-1.52,mkt:'85Md€',b52h:323.8,b52l:138.3,beta:0.57,
 pe:28.42,pb:1.78,ev_ebitda:14.53,ps:2.38,pfcf:22,ev_ebit:24.2,
 roe:6.7,roic:5.3,roa:3.7,debt:0.38,de:0.38,ic:11.2,cr:0.89,qr:1.2,
 yield:2.6,epsg:12.3,revg:5.7,margin:8.5,gm:60.0,om:18,fcf:5.4,
 capex:3.5,capr:5.4,capda:0.49,
 dcfb:136.05,dcfm:160.06,dcfu:192.07,
 pio:4,alt:2.41,rsi:56.6,mm50:151.66,mm200:186.26,
 el:115.24,eh:142.13,stop:101.41,o1:168.06,o2:192.07,
 cb:14,ch:7,cs:1,tp:221.43,score:'D',rec:'avoid',zone:false,
 moat:[['Monopole optique mondial','fort'],['Rayban/Oakley/Varilux','fort']],
 cats:[{t:'Smart glasses expansion',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Del Vecchio famille','185M€','Jan 2026']],
 peers:[{n:'Safilo',pe:18,pb:1.5,roe:8,div:1.5,evebitda:10}],
 risks:{Valorisation:55,Devise:50,Concurrence:40,Intégration:35,Santé:30,Liquidite:10},
 track:[{y:'2025',p:'Synergies Essilor/Luxottica complètes',ok:'ok'}],
 thesis:"EssilorLuxottica contrôle toute la chaîne de valeur optique mondiale. Vieillissement population + smart glasses = croissance structurelle décennale.",
 contra:"28x PE pour 7-9% de croissance organique. Intégration encore en cours."},

{ticker:'ML',x2:'',x2s:'',name:'Michelin',sector:'Pneumatiques',cap:'large',srd:true,idx:'CAC40',
 price:32.95,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-1.1,news5:'',dy_n:10,dy_med:3.41,div12:1.38,pe_lo:9.3,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.1,pfcf_h:10.7,pe_h:11.7,fcur:'EUR',fcfh:'1790|2071|3013|-210',nih:'1665|1884|1983|2001',revh:'25992|27193|28343|28590',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-4.5,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-5.9,cagr:-3.1,alarm:'',qwhy:'ROIC hors EA 11.3, ROIC 10.0, croissance CA -3.1%',qok:false,nde:0.63,fcfc:88.0,roicx:11.3,chg:-2.14,mkt:'17Md€',b52h:35.72,b52l:26.9,beta:0.9,
 pe:3.22,pb:0.39,ev_ebitda:6,ps:null,pfcf:7,ev_ebit:null,
 roe:17,roic:10.0,roa:null,debt:1.2,de:null,ic:7.4,cr:null,qr:1.0,
 yield:4.2,epsg:6,revg:4,margin:8,gm:32,om:11,fcf:null,
 capex:4.5,capr:7.8,capda:1.0,
 dcfb:156.67,dcfm:184.32,dcfu:221.18,
 pio:6,alt:2.73,rsi:41.8,mm50:33.99,mm200:31.96,
 el:152.99,eh:171.79,stop:134.63,o1:193.54,o2:221.18,
 cb:10,ch:6,cs:3,tp:33.52,score:'C',rec:'avoid',zone:false,
 moat:[['Marque premium pneumatiques','fort'],['Technologie innovation','fort']],
 cats:[{t:'Pneus VE premium croissance',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Michelin','12M€','Jan 2026']],
 peers:[{n:'Bridgestone',pe:10,pb:1.2,roe:12,div:3.8,evebitda:7}],
 risks:{VE:55,Cyclicite:50,Matières:45,Chine:50,Devise:45,Liquidite:15},
 track:[{y:'2025',p:'Marge op. 11%',ok:'ok'}],
 thesis:"Michelin à 9x PE avec marque centenaire. Les pneus pour VE = opportunité car usure plus forte. Famille aux commandes.",
 contra:"Les marques locales Chine montent en gamme. E-commerce intense. Cyclicité auto forte."},

{ticker:'ENGI',x2:'',x2s:'',name:'Engie',sector:'Énergie',cap:'large',srd:true,idx:'CAC40',
 price:22.77,roiica:false,reinv:false,roiic:49.2,vmed:null,vepv:null,chg5:-0.7,news5:'',dy_n:9,dy_med:6.74,div12:1.35,pe_lo:9.2,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.6,pfcf_h:10.1,pe_h:16.0,fcur:'EUR',fcfh:'-8743|3759|5789|2207',nih:'3827|4106|2208|216',revh:'71944|73812|82566|93864',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:76.1,gimp:null,knife:false,neglect:false,vmeth:'per',nig:160.7,cagr:-8.5,alarm:'Piotroski 4/9',qwhy:'ROIC hors EA 10.5, ROIC 8.5, cash 29.0%, dette/EBITDA 2.78, croissance CA -8.5%',qok:false,nde:2.78,fcfc:29.0,roicx:10.5,chg:-2.78,mkt:'44Md€',b52h:29.89,b52l:19.42,beta:0.56,
 pe:13.97,pb:1.7,ev_ebitda:9.14,ps:0.82,pfcf:8,ev_ebit:13.8,
 roe:12.2,roic:8.5,roa:3.1,debt:1.44,de:1.44,ic:3.5,cr:1.0,qr:0.8,
 yield:5.8,epsg:14.3,revg:-3.6,margin:6.0,gm:32.1,om:6,fcf:-15.1,
 capex:6.5,capr:10.1,capda:1.32,
 dcfb:22.41,dcfm:26.36,dcfu:31.63,
 pio:4,alt:0.9,rsi:40.5,mm50:24.04,mm200:25.65,
 el:21.09,eh:24.25,stop:18.56,o1:27.68,o2:31.63,
 cb:10,ch:6,cs:3,tp:30.54,score:'C',rec:'avoid',zone:false,
 moat:[['Nucléaire belge prolongé 10 ans','fort'],['ENR portfolio 50GW','modere']],
 cats:[{t:'Nucléaire belge opérationnel',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Bia','4.5M€','Jan 2026']],
 peers:[{n:'EDF',pe:14,pb:0.8,roe:8,div:4.5,evebitda:7},{n:'Enel',pe:12,pb:1.4,roe:12,div:7.2,evebitda:7}],
 risks:{Reglement:60,Taux:55,ENR:50,Politique:55,Nucléaire:45,Liquidite:15},
 track:[{y:'2025',p:'Nucléaire belge prolongé',ok:'ok'}],
 thesis:"Engie à 7.5% de dividende avec nucléaire belge prolongé 10 ans. Transition énergétique européenne = investissements massifs dont Engie est bénéficiaire direct.",
 contra:"CAPEX permanent massif. Politique énergétique volatile. Dette élevée."},

{ticker:'MT',x2:'',x2s:'',name:'ArcelorMittal',sector:'Acier',cap:'large',srd:true,idx:'CAC40',
 price:56.52,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.5,news5:'',dy_n:7,dy_med:1.34,div12:0.643,pe_lo:2.3,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 27.8 contre 8.5 attendu)',vmult:null,hn:4,eveb_h:4.7,pfcf_h:22.9,pe_h:12.0,fcur:'USD',fcfh:'471|447|3032|6735',nih:'3152|1339|919|9302',revh:'61352|62441|68275|79844',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:0,place:'Amsterdam',near:false,gsrc:'yahoo (4 ans publies)',gused:-19.4,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-30.3,cagr:-8.4,alarm:'',qwhy:'ROIC hors EA 5.3, ROIC 4.9, cash 73.0%, croissance CA -8.4%',qok:false,nde:1.13,fcfc:73.0,roicx:5.3,chg:-0.49,mkt:'18Md€',b52h:68.56,b52l:31.87,beta:1.75,
 pe:27.84,pb:0.87,ev_ebitda:9.98,ps:0.68,pfcf:6,ev_ebit:13.0,
 roe:3.3,roic:4.9,roa:1.6,debt:0.25,de:0.25,ic:7.2,cr:1.43,qr:1.2,
 yield:0.9,epsg:-61.7,revg:5.2,margin:2.9,gm:9.0,om:7,fcf:1.1,
 capex:3.5,capr:7.1,capda:1.47,
 dcfb:101.51,dcfm:119.42,dcfu:143.3,
 pio:6,alt:2.2,rsi:39.2,mm50:61.8,mm200:54.7,
 el:99.12,eh:111.3,stop:87.23,o1:125.39,o2:143.3,
 cb:10,ch:5,cs:4,tp:69.99,score:'C',rec:'avoid',zone:false,
 moat:[['Scale mondiale acier','modere'],['Intégration verticale','modere']],
 cats:[{t:'Infrastructure EU relance',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Mittal','85M€','Jan 2026']],
 peers:[{n:'Nippon Steel',pe:7,pb:0.5,roe:7,div:3.5,evebitda:4}],
 risks:{Chine:80,Cyclicite:80,Energie:65,CO2:70,Devise:45,Liquidite:20},
 track:[{y:'2025',p:'EBITDA sous pression',ok:'partial'}],
 thesis:"ArcelorMittal à 0.6x livre avec buybacks massifs. Acier vert DRI-H2 = catalyseur 2026-2028.",
 contra:"La Chine exporte de l'acier à prix dumping. Cyclicité maximale."},

{ticker:'URW',x2:'',x2s:'',name:'Unibail-Rodamco',sector:'Immobilier commercial',cap:'large',srd:true,idx:'CAC40',
 price:87.98,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.2,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:2.1,ltv:40.3,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:0.0,irrn:7.0,irr:7.0,dq:'',vmult:null,hn:2,eveb_h:16.2,pfcf_h:11.5,pe_h:41.2,fcur:'EUR',fcfh:'1152|882|876|1531',nih:'1268|146|-1629|178',revh:'3058|3256|3061|3004',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:125.0,vpess:90.91,nregu:null,regn:3,regu:2,place:'Paris',near:true,gsrc:'yahoo (4 ans publies)',gused:0.6,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:null,cagr:0.6,alarm:'',qwhy:'couverture des interets 2.1',qok:false,nde:null,fcfc:null,roicx:null,chg:-2.05,mkt:'9.8Md€',b52h:106.65,b52l:85.98,beta:1.37,
 pe:8.15,pb:0.77,ev_ebitda:16.45,ps:3.59,pfcf:8,ev_ebit:14.1,
 roe:8.6,roic:null,roa:2.8,debt:1.08,de:1.08,ic:3.3,cr:0.79,qr:0.6,
 yield:5.0,epsg:43.2,revg:-0.4,margin:44.6,gm:70.4,om:38,fcf:9.1,
 capex:1.2,capr:29.3,capda:33.39,
 dcfb:96.88,dcfm:113.64,dcfu:136.78,
 pio:8,alt:0.57,rsi:39.5,mm50:94.82,mm200:96.46,
 el:79.55,eh:90.91,stop:81.82,o1:125.0,o2:137.5,
 cb:8,ch:5,cs:4,tp:113.58,score:'C',rec:'avoid',zone:false,
 moat:[['Centres commerciaux premium Westfield','modere']],
 cats:[{t:'Désendettement accéléré',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Benko','8.2M€','Jan 2026']],
 peers:[{n:'Klepierre',pe:14,pb:0.9,roe:8,div:6.2,evebitda:16}],
 risks:{Dette:80,Commerce:65,Taux:70,Ecommerce:60,Reglement:45,Liquidite:30},
 track:[{y:'2025',p:'ANR stabilisé',ok:'partial'}],
 thesis:"Unibail décote massivement sur son ANR. Westfield premium résiste à l'e-commerce. Désendettement sur les rails.",
 contra:"Dette massive. Taux élevés pèsent. E-commerce continue d'éroder la fréquentation."},

{ticker:'SW',x2:'',x2s:'',name:'Sodexo',sector:'Services collectifs',cap:'large',srd:true,idx:'CAC40',
 price:56.7,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:3.1,news5:'',dy_n:10,dy_med:4.19,div12:2.7,pe_lo:11.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:3,eveb_h:9.2,pfcf_h:10.8,pe_h:13.4,fcur:'EUR',fcfh:'|962|995|769',nih:'|168|794|695',revh:'|23798|22637|20263',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:2,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-21.2,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-50.8,cagr:8.4,alarm:'',qwhy:'ROIC 7.7',qok:false,nde:2.16,fcfc:165.0,roicx:48.3,chg:0.62,mkt:'12Md€',b52h:59.35,b52l:35.5,beta:0.25,
 pe:18.59,pb:2.3,ev_ebitda:10.96,ps:0.35,pfcf:12,ev_ebit:11.7,
 roe:11.9,roic:7.7,roa:3.5,debt:1.5,de:1.5,ic:6.8,cr:1.02,qr:0.8,
 yield:4.8,epsg:-56.5,revg:-3.7,margin:1.9,gm:11.0,om:5,fcf:null,
 capex:1.5,capr:null,capda:null,
 dcfb:35.53,dcfm:41.8,dcfu:50.16,
 pio:1,alt:0,rsi:57.4,mm50:56.49,mm200:49.42,
 el:35.11,eh:39.12,stop:30.9,o1:43.89,o2:50.16,
 cb:10,ch:6,cs:2,tp:54.91,score:'D',rec:'avoid',zone:false,
 moat:[['Contrats pluriannuels','fort']],
 cats:[{t:'Spin-off Pluxee valeur',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Bellon','6.2M€','Jan 2026']],
 peers:[{n:'Compass Group',pe:22,pb:8,roe:35,div:2.8,evebitda:14}],
 risks:{Inflation:45,Contrats:40,Devise:50,Concurrence:40,Marges:45,Liquidite:15},
 track:[{y:'2025',p:'Marge op. 5.2%',ok:'ok'}],
 thesis:"Sodexo est un compounder de qualité avec des contrats 5-7 ans. Le spin-off Pluxee révèle la valeur cachée.",
 contra:"Marges très fines. Inflation pèse sur les coûts. Compass Group est redoutable."},

{ticker:'TEP',x2:'',x2s:'',name:'Teleperformance',sector:'BPO',cap:'large',srd:true,idx:'CAC40',
 price:76.4,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:7.9,news5:'',dy_n:10,dy_med:1.21,div12:4.5,pe_lo:7.4,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:6.2,pfcf_h:5.0,pe_h:11.5,fcur:'EUR',fcfh:'1361|1594|1142|996',nih:'497|523|592|643',revh:'10209|10280|8345|8154',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-0.2,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-8.2,cagr:7.8,alarm:'',qwhy:'ROIC 8.2',qok:false,nde:2.19,fcfc:226.0,roicx:17.6,chg:2.3,mkt:'5.2Md€',b52h:78.14,b52l:43.65,beta:0.64,
 pe:9.66,pb:1.06,ev_ebitda:5.28,ps:0.45,pfcf:7,ev_ebit:7.9,
 roe:11.4,roic:8.2,roa:6.0,debt:1.2,de:1.2,ic:3.9,cr:1.4,qr:1.0,
 yield:6.0,epsg:-11.6,revg:-4.6,margin:4.7,gm:30.7,om:13,fcf:30.6,
 capex:2.8,capr:2.5,capda:0.34,
 dcfb:92.68,dcfm:109.04,dcfu:130.85,
 pio:6,alt:2.09,rsi:63.0,mm50:70.87,mm200:58.35,
 el:91.59,eh:102.06,stop:80.6,o1:114.49,o2:130.85,
 cb:8,ch:6,cs:5,tp:76.96,score:'C',rec:'avoid',zone:false,
 moat:[['Scale mondiale BPO','modere']],
 cats:[{t:'IA résistance meilleure que prévu',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Dupuy','3.8M€','Jan 2026']],
 peers:[{n:'Concentrix',pe:8,pb:1.2,roe:16,div:4.5,evebitda:5}],
 risks:{IA:85,Disruption:80,Reglement:55,Devise:45,Cyclicite:40,Liquidite:25},
 track:[{y:'2025',p:'IA résiste mieux que prévu',ok:'partial'}],
 thesis:"Teleperformance à 9x PE. La valorisation suppose une disruption totale et immédiate qui n'est pas encore visible dans les chiffres.",
 contra:"L'IA générative automatisera 40-60% des tâches de centres d'appels. La disruption est réelle et inévitable."},

{ticker:'EN',x2:'',x2s:'',name:'Bouygues',sector:'Conglomérat',cap:'large',srd:true,idx:'CAC40',
 price:40.85,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.0,news5:'',dy_n:10,dy_med:5.19,div12:2.1,pe_lo:10.2,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:4.3,pfcf_h:5.3,pe_h:11.6,fcur:'EUR',fcfh:'2971|2664|2680|248',nih:'1138|1058|1040|973',revh:'56877|56752|56017|44398',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:7.0,gimp:null,knife:false,neglect:true,vmeth:'per',nig:5.4,cagr:8.6,alarm:'',qwhy:'ROIC 7.0',qok:false,nde:1.33,fcfc:203.0,roicx:17.8,chg:-1.59,mkt:'10Md€',b52h:53.48,b52l:38.53,beta:0.7,
 pe:12.49,pb:1.26,ev_ebitda:6.01,ps:0.28,pfcf:8,ev_ebit:11.5,
 roe:9.7,roic:7.0,roa:2.3,debt:1.03,de:1.03,ic:5.0,cr:0.89,qr:0.9,
 yield:5.1,epsg:12.6,revg:-1.0,margin:2.2,gm:56.8,om:4,fcf:19.0,
 capex:3.2,capr:4.4,capda:0.75,
 dcfb:44.86,dcfm:52.78,dcfu:63.34,
 pio:7,alt:1.19,rsi:38.5,mm50:43.72,mm200:47.06,
 el:43.81,eh:49.19,stop:38.55,o1:55.42,o2:63.34,
 cb:8,ch:5,cs:3,tp:59.05,score:'C',rec:'avoid',zone:false,
 moat:[['TF1 media','modere'],['Bouygues Telecom 4G','modere']],
 cats:[{t:'Fibre profitabilité 2026',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Bouygues','22M€','Jan 2026']],
 peers:[{n:'Vinci',pe:15,pb:3.5,roe:24,div:3.5,evebitda:10}],
 risks:{Diversification:50,Télécom:55,Construction:45,Média:60,Cyclicite:45,Liquidite:20},
 track:[{y:'2025',p:'Bouygues Telecom profitable',ok:'ok'}],
 thesis:"Bouygues est un conglomérat de qualité décoté. Bouygues Telecom gagne des parts de marché. Construction profite de l'infrastructure.",
 contra:"Conglomérats décotés structurellement. Télécoms français ultra-concurrentiels."},

// ══════════════════════════════════════════
// SBF 120 & SRD
// ══════════════════════════════════════════
{ticker:'GTT',x2:'',x2s:'',name:'Gaztransport & Technigaz',sector:'LNG Technology',cap:'mid',srd:true,idx:'SBF120',
 price:207.4,roiica:false,reinv:false,roiic:99.9,vmed:202.03,vepv:90.89,chg5:-4.2,news5:'',dy_n:10,dy_med:4.63,div12:8.94,pe_lo:13.9,gmod:3.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:8.3,irr:8.3,dq:'',vmult:204.57,hn:4,eveb_h:15.4,pfcf_h:21.4,pe_h:18.4,fcur:'EUR',fcfh:'383|300|173|119',nih:'414|348|201|128',revh:'803|641|428|307',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:226.4,vpess:180.2,nregu:3,regn:3,regu:3,place:'Paris',mthreat:'cycle des commandes, technologies concurrentes coreennes, sanctions',mtype:'brevets des membranes de cuves GNL, standard de l immense majorite des methaniers',mscore:4,near:false,gsrc:'communique 2026-10-11',gused:3.0,gimp:3.7,knife:false,neglect:false,vmeth:'qarp',nig:47.7,cagr:37.7,alarm:'',qwhy:'',qok:true,nde:-0.4,fcfc:89.0,roicx:324.5,chg:-1.98,mkt:'7.2Md€',b52h:227.0,b52l:153.8,beta:0.42,
 pe:17.41,pb:12.53,ev_ebitda:13.96,ps:9.59,pfcf:18,ev_ebit:14.5,
 roe:79.6,roic:261.2,roa:36.5,debt:0.17,de:0.17,ic:null,cr:1.95,qr:2.8,
 yield:4.1,epsg:16.6,revg:-0.4,margin:55.4,gm:96.8,om:58,fcf:5.0,
 capex:0.8,capr:5.0,capda:1.63,
 dcfb:171.73,dcfm:202.03,dcfu:242.44,
 pio:5,alt:13.47,rsi:40.4,mm50:213.01,mm200:195.64,
 el:141.42,eh:161.62,stop:162.18,o1:226.4,o2:249.04,
 cb:8,ch:4,cs:2,tp:234.25,score:'B',rec:'hold',zone:false,
 moat:[['Monopole brevets membranes LNG','fort'],['30 ans de protection IP','fort']],
 cats:[{t:'Commande Samsung H1 2026',w:'T1 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Metz','8.2M€','Fév 2026']],
 peers:[{n:'Technip Energies',pe:14,pb:2.8,roe:22,div:3.2,evebitda:8}],
 risks:{LNG:60,Samsung:45,Décarbonation:55,Concentration:65,Devise:35,Liquidite:20},
 track:[{y:'2025',p:'EBITDA +40% FY2025',ok:'ok'}],
 thesis:"GTT : 58% de marge nette, zéro dette, ROE 85%. Monopole de brevets LNG protégé 30 ans. Proche du plus haut historique.",
 contra:"Pur jeu GNL dans un monde qui se décarbonise. Si les commandes s'effondrent, la thèse s'effondre."},

{ticker:'COFA',x2:'',x2s:'',name:'Coface',sector:'Assurance crédit',cap:'mid',srd:true,idx:'SBF120',
 price:15.71,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.4,news5:'',dy_n:9,dy_med:8.35,div12:1.25,pe_lo:7.3,gmod:null,nih:'222|261|240|240',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:3.1,roemin:10.0,roem:11.8,grid:'banque',wht:0.0,irrn:11.0,irr:11.0,dq:'',vmult:null,hn:4,eveb_h:null,pfcf_h:6.6,pe_h:7.9,fcur:'EUR',unc:'elevee',vopt:21.39,vpess:12.33,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-2.6,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:-2.6,cagr:null,alarm:'',qwhy:'',qok:true,nde:null,fcfc:null,roicx:null,chg:-1.19,mkt:'1.9Md€',b52h:17.62,b52l:14.02,beta:0.49,
 pe:11.38,pb:1.08,ev_ebitda:14.62,ps:1.28,pfcf:7,ev_ebit:17.0,
 roe:9.7,roic:null,roa:2.8,debt:1.93,de:1.93,ic:8.1,cr:1.43,qr:1.0,
 yield:7.9,epsg:-12.2,revg:3.5,margin:11.2,gm:59.8,om:14,fcf:9.0,
 capex:0.5,capr:2.1,capda:1.05,
 dcfb:14.01,dcfm:17.77,dcfu:19.78,
 pio:6,alt:0.62,rsi:44.2,mm50:16.05,mm200:15.1,
 el:12.44,eh:14.21,stop:11.1,o1:21.39,o2:23.53,
 cb:8,ch:4,cs:2,tp:18.25,score:'C',rec:'watch',zone:false,
 moat:[['Données sinistralité mondiale','fort'],['Réseau 100 pays','modere']],
 cats:[{t:'Taux de sinistralité bas 2026',w:'T1 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Durand','1.19M€','Fév 2026']],
 peers:[{n:'Euler Hermes',pe:10,pb:1.8,roe:18,div:5.2,evebitda:7}],
 risks:{Faillites:70,Macro:65,Cyclicite:60,Régulation:35,Concentration:40,Liquidite:20},
 track:[{y:'2025',p:'ROE 14%',ok:'ok'}],
 thesis:"Coface : 8.2% de dividende couvert 2x par le bénéfice. Sinistralité au plus bas. CEO a acheté pour 1.2M€ en février 2026.",
 contra:"Assurance crédit cyclique sur les faillites. Un retournement économique fait exploser les sinistres."},

{ticker:'MERY',x2:'',x2s:'',name:'Mersen',sector:'Matériaux spéciaux',cap:'small',srd:true,idx:'SBF120',
 price:9.52,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.6,news5:'',dy_n:10,dy_med:8.53,div12:1.0,pe_lo:17.4,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:14.1,pfcf_h:6.2,pe_h:19.4,fcur:'EUR',fcfh:'157|162|134|150',nih:'34|54|53|43',revh:'221|221|223|211',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-3.0,gimp:null,knife:false,neglect:true,vmeth:'per',nig:-7.6,cagr:1.6,alarm:'',qwhy:'ROIC hors EA 5.3, ROIC 5.3, dette/EBITDA 8.19, croissance CA 1.6%',qok:false,nde:8.19,fcfc:327.0,roicx:5.3,chg:-3.35,mkt:'0.62Md€',b52h:12.98,b52l:9.34,beta:0.86,
 pe:16.7,pb:0.57,ev_ebitda:19.11,ps:4.81,pfcf:8,ev_ebit:28.8,
 roe:2.2,roic:5.3,roa:1.9,debt:0.85,de:0.85,ic:1.9,cr:1.05,qr:1.2,
 yield:10.2,epsg:-28.0,revg:3.9,margin:11.4,gm:94.7,om:10,fcf:17.7,
 capex:4.8,capr:null,capda:null,
 dcfb:13.63,dcfm:16.03,dcfu:19.24,
 pio:5,alt:0.54,rsi:36.3,mm50:10.54,mm200:11.02,
 el:13.3,eh:14.94,stop:11.7,o1:16.83,o2:19.24,
 cb:6,ch:5,cs:2,tp:12.53,score:'C',rec:'avoid',zone:false,
 moat:[['Graphites spéciaux SiC','fort'],['Nucléaire qualité','fort']],
 cats:[{t:'Nucléaire SMR contrat',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','Direction Mersen','0.4M€','Jan 2026']],
 peers:[{n:'SGL Carbon',pe:12,pb:1.2,roe:8,div:2.8,evebitda:7}],
 risks:{VE:60,Nucléaire:45,Cyclicite:55,Dette:40,Devise:35,Liquidite:30},
 track:[{y:'2025',p:'Nucléaire +15%',ok:'ok'}],
 thesis:"Mersen : graphites indispensables aux SiC pour VE et aux réacteurs nucléaires. À 10x PE, une reprise VE 2026 déclenche un re-rating.",
 contra:"VE ralentit. Taille limitée. Dette laisse peu de marge."},

{ticker:'JXS',x2:'',x2s:'',name:'Jacquet Metals',sector:'Aciers spéciaux',cap:'small',srd:true,idx:'SBF120',
 price:20.1,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.5,news5:'',dy_n:10,dy_med:2.07,div12:0.2,pe_lo:2.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.2,pfcf_h:4.0,pe_h:23.9,fcur:'EUR',fcfh:'82|117|158|14',nih:'10|6|51|180',revh:'1840|1970|2230|2683',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-36.6,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-61.4,cagr:-11.8,alarm:'',qwhy:'ROIC hors EA 6.2, ROIC 5.7, croissance CA -11.8%',qok:false,nde:2.23,fcfc:150.0,roicx:6.2,chg:-0.74,mkt:'0.43Md€',b52h:25.4,b52l:17.06,beta:0.99,
 pe:15.83,pb:0.62,ev_ebitda:9.14,ps:0.22,pfcf:7,ev_ebit:12.2,
 roe:4.4,roic:5.7,roa:2.6,debt:0.58,de:0.58,ic:2.4,cr:1.99,qr:1.4,
 yield:1.0,epsg:211.4,revg:4.8,margin:1.4,gm:25.0,om:5,fcf:20.1,
 capex:1.2,capr:1.1,capda:0.55,
 dcfb:32.05,dcfm:37.71,dcfu:45.25,
 pio:8,alt:2.19,rsi:46.3,mm50:20.67,mm200:21.62,
 el:31.3,eh:35.15,stop:27.54,o1:39.6,o2:45.25,
 cb:4,ch:6,cs:2,tp:28,score:'C',rec:'avoid',zone:false,
 moat:[['Distribution aciers spéciaux','modere'],['Service cut-to-size','modere']],
 cats:[{t:'Rebond industriel Europe',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Jacquet','1.8M€','Jan 2026']],
 peers:[{n:'Klöckner',pe:8,pb:0.6,roe:7,div:4.2,evebitda:4}],
 risks:{Acier:65,Industrie:60,Cyclicite:65,Marges:55,Devise:40,Liquidite:35},
 track:[{y:'2025',p:'Dividende maintenu',ok:'ok'}],
 thesis:"Jacquet Metals : 0.8x valeur comptable avec 6.2% de dividende. Famille aux commandes. Risque limité.",
 contra:"VE ralentit détruit les marges. Exposition cyclique maximale à l'industrie européenne."},

{ticker:'SPIE',x2:'',x2s:'',name:'Spie',sector:'Services techniques',cap:'mid',srd:true,idx:'SBF120',
 price:40.84,roiica:true,reinv:false,roiic:5.2,vmed:null,vepv:null,chg5:-2.3,news5:'',dy_n:9,dy_med:2.84,div12:1.1,pe_lo:18.3,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:9.0,pfcf_h:7.5,pe_h:23.1,fcur:'EUR',fcfh:'812|832|652|512',nih:'176|273|239|152',revh:'10397|9920|8725|8114',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:6.9,gimp:null,knife:false,neglect:true,vmeth:'per',nig:5.2,cagr:8.6,alarm:'',qwhy:'ROIC 7.0',qok:false,nde:2.35,fcfc:334.0,roicx:154.1,chg:-2.06,mkt:'5.2Md€',b52h:53.45,b52l:40.4,beta:0.76,
 pe:22.94,pb:3.31,ev_ebitda:12.09,ps:0.65,pfcf:14,ev_ebit:26.2,
 roe:15.1,roic:7.0,roa:4.2,debt:1.71,de:1.71,ic:3.9,cr:0.77,qr:1.0,
 yield:2.6,epsg:12,revg:3.5,margin:2.8,gm:9.2,om:6,fcf:11.8,
 capex:1.2,capr:0.7,capda:0.16,
 dcfb:26.84,dcfm:31.58,dcfu:37.9,
 pio:7,alt:1.56,rsi:36.5,mm50:43.63,mm200:46.49,
 el:26.53,eh:29.56,stop:23.35,o1:33.16,o2:37.9,
 cb:12,ch:5,cs:2,tp:56.75,score:'C',rec:'avoid',zone:false,
 moat:[['Services multi-techniques récurrents','fort'],['Contrats pluriannuels','fort']],
 cats:[{t:'Data centers électricité',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Gilles','4.2M€','Jan 2026']],
 peers:[{n:'Eiffage Énergie',pe:17,pb:3.2,roe:20,div:2.5,evebitda:10}],
 risks:{Contrats:35,Personnel:45,Inflation:40,Concurrence:35,Devise:30,Liquidite:15},
 track:[{y:'2025',p:'Croissance organique +9%',ok:'ok'}],
 thesis:"Spie est le leader européen des services techniques. Data centers + rénovation énergétique + 5G = 3 mégatendances. Modèle récurrent.",
 contra:"Valorisation élevée à 18x. Marges fines dans les services."},

{ticker:'NEXANS',x2:'',x2s:'',name:'Nexans',sector:'Câbles',cap:'mid',srd:true,idx:'SBF120',
 price:122.1,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-7.4,news5:'',dy_n:8,dy_med:1.72,div12:2.9,pe_lo:15.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:8.4,pfcf_h:11.4,pe_h:15.8,fcur:'EUR',fcfh:'464|457|323|246',nih:'352|279|221|245',revh:'7810|6917|7790|8369',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:5.2,gimp:null,knife:false,neglect:true,vmeth:'per',nig:12.8,cagr:-2.3,alarm:'',qwhy:'croissance CA -2.3%',qok:false,nde:0.43,fcfc:136.0,roicx:16.6,chg:-3.63,mkt:'2.8Md€',b52h:169.0,b52l:109.7,beta:0.94,
 pe:13.12,pb:2.51,ev_ebitda:8.86,ps:0.62,pfcf:9,ev_ebit:17.7,
 roe:9.8,roic:12.9,roa:3.5,debt:1.16,de:1.16,ic:6.5,cr:1.04,qr:1.1,
 yield:2.3,epsg:-72.3,revg:19.1,margin:1.0,gm:10.2,om:6,fcf:8.7,
 capex:3.5,capr:4.9,capda:1.55,
 dcfb:91.97,dcfm:108.2,dcfu:129.84,
 pio:8,alt:1.89,rsi:32.7,mm50:136.35,mm200:135.76,
 el:89.81,eh:100.84,stop:79.03,o1:113.61,o2:129.84,
 cb:12,ch:5,cs:2,tp:172.53,score:'C',rec:'avoid',zone:false,
 moat:[['Câbles sous-marins leader','fort'],['Électrification réseaux','fort']],
 cats:[{t:'Câbles offshore éolien',w:'2026-2028',c:'var(--gn)'}],
 ins:[['Achat','CEO Dorison','4.5M€','Jan 2026']],
 peers:[{n:'Prysmian',pe:14,pb:3.5,roe:25,div:1.8,evebitda:10}],
 risks:{Copper:55,Cyclicite:45,Devise:40,Concurrence:35,CAPEX:40,Liquidite:20},
 track:[{y:'2025',p:'EBITDA +15%',ok:'ok'},{y:'2024',p:'Offshore record carnet',ok:'ok'}],
 thesis:"Nexans est au cœur de la transition énergétique. Les câbles sous-marins pour l'éolien offshore sont en pénurie structurelle. Carnet record.",
 contra:"Exposition forte au prix du cuivre. Prysmian reste plus large et plus rentable."},

{ticker:'DASSAV',x2:'',x2s:'',name:'Dassault Aviation',sector:'Aviation militaire',cap:'large',srd:true,idx:'SBF120',
 price:301.2,roiica:true,reinv:false,roiic:10.0,vmed:311.98,vepv:243.79,chg5:4.8,news5:'',dy_n:9,dy_med:1.66,div12:4.78,pe_lo:16.4,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:8.7,irr:8.7,dq:'',vmult:351.85,hn:4,eveb_h:11.6,pfcf_h:9.9,pe_h:19.4,fcur:'EUR',fcfh:'1654|1535|-1018|4935',nih:'977|924|693|716',revh:'7426|6240|4805|6950',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:311.98,vpess:197.49,nregu:2,regn:3,regu:2,place:'Paris',mthreat:'dependance aux grands contrats export',mtype:'Rafale et Falcon : duopole defense/aviation d affaires',mscore:4,near:false,gsrc:'communique 2026-10-12',gused:16.8,gimp:11.1,knife:false,neglect:false,vmeth:'qarp',nig:10.9,cagr:2.2,alarm:'',qwhy:'',qok:true,nde:-1.21,fcfc:215.0,roicx:19.8,chg:-0.86,mkt:'24Md€',b52h:361.8,b52l:260.8,beta:0.42,
 pe:23.33,pb:3.54,ev_ebitda:14.47,ps:2.65,pfcf:10,ev_ebit:10.8,
 roe:15.7,roic:19.4,roa:1.5,debt:0.03,de:0.03,ic:199.1,cr:1.05,qr:4.2,
 yield:1.6,epsg:9.0,revg:45.1,margin:11.5,gm:88.4,om:16,fcf:7.1,
 capex:1.2,capr:2.6,capda:1.02,
 dcfb:265.18,dcfm:311.98,dcfu:374.38,
 pio:6,alt:0.93,rsi:61.9,mm50:290.94,mm200:304.14,
 el:233.99,eh:265.18,stop:177.74,o1:311.98,o2:343.18,
 cb:12,ch:4,cs:1,tp:360.65,score:'C',rec:'watch',zone:false,
 moat:[['Rafale monopole français','fort'],['Falcon jets privés','fort']],
 cats:[{t:'Commandes Rafale 2026',w:'T1 2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Dassault','45M€','Jan 2026']],
 peers:[{n:'BAE Systems',pe:15,pb:4.5,roe:28,div:2.8,evebitda:10},{n:'Leonardo',pe:14,pb:2.8,roe:18,div:2.5,evebitda:9}],
 risks:{Politique:40,Rafale:35,Export:45,Développement:35,Dépendance:40,Liquidite:10},
 track:[{y:'2025',p:'Rafale Croatie + Indonésie',ok:'ok'},{y:'2024',p:'Carnet 220+ appareils',ok:'ok'}],
 thesis:"Dassault Aviation : zéro dette, 4.8x trésorerie nette, Rafale production maximale, budgets défense EU qui explosent post-Ukraine. À 12x PE c'est donné.",
 contra:"Dépendance politique aux exportations. Famille peut prendre des décisions contraires aux minoritaires."},

{ticker:'ALO',x2:'',x2s:'',name:'Alstom',sector:'Ferroviaire',cap:'large',srd:true,idx:'SBF120',
 price:16.01,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.6,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 26.7 contre 8.4 attendu)',vmult:null,hn:2,eveb_h:10.7,pfcf_h:34.6,pe_h:45.7,fcur:'EUR',fcfh:'324|490|-567|175',nih:'324|149|-309|-132',revh:'19171|18489|17619|16507',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:5.1,gimp:null,knife:true,neglect:false,vmeth:'per',nig:null,cagr:5.1,alarm:'',qwhy:'ROIC hors EA 3.8, ROIC 0.8',qok:false,nde:0.96,fcfc:1319.0,roicx:3.8,chg:-0.71,mkt:'6.2Md€',b52h:30.23,b52l:14.47,beta:1.05,
 pe:26.68,pb:0.75,ev_ebitda:7.64,ps:0.39,pfcf:12,ev_ebit:17.7,
 roe:3.4,roic:0.8,roa:1.2,debt:0.33,de:0.33,ic:4.2,cr:0.94,qr:0.8,
 yield:0.0,epsg:-29.5,revg:4.1,margin:1.7,gm:12.3,om:5,fcf:4.4,
 capex:2.5,capr:3.0,capda:0.7,
 dcfb:24.36,dcfm:28.66,dcfu:34.39,
 pio:7,alt:0.78,rsi:54.3,mm50:15.79,mm200:19.57,
 el:23.5,eh:26.6,stop:20.68,o1:30.09,o2:34.39,
 cb:12,ch:5,cs:4,tp:20.7,score:'C',rec:'avoid',zone:false,
 moat:[['Leader TGV Europe','fort'],['Métros & signalisation','fort']],
 cats:[{t:'Désendettement plan',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Poupart-Lafarge','3.2M€','Jan 2026']],
 peers:[{n:'Siemens Mobility',pe:22,pb:3.5,roe:15,div:1.2,evebitda:14}],
 risks:{Dette:80,Cash:75,Bombadier:70,Devise:50,Contrats:55,Liquidite:30},
 track:[{y:'2025',p:'Cash generation positive',ok:'partial'},{y:'2024',p:'Crise de cash',ok:'m'}],
 thesis:"Alstom a traversé une crise existentielle. Commandes ferroviaires EU à records. À 1.2x livre en amélioration.",
 contra:"Crise trésorerie 2023-2024 a détruit la confiance. Intégration Bombardier = désastre. Exécution risquée."},

{ticker:'ELIS',x2:'',x2s:'',name:'Elis',sector:'Services location-entretien',cap:'mid',srd:true,idx:'SBF120',
 price:22.06,roiica:false,reinv:false,roiic:31.4,vmed:null,vepv:null,chg5:1.9,news5:'',dy_n:8,dy_med:2.14,div12:0.74,pe_lo:12.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.6,pfcf_h:8.5,pe_h:15.4,fcur:'EUR',fcfh:'620|565|502|391',nih:'367|338|262|203',revh:'4797|4574|4309|3821',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:14.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:21.9,cagr:7.9,alarm:'',qwhy:'ROIC hors EA 12.8, ROIC 5.7',qok:false,nde:2.23,fcfc:178.0,roicx:12.8,chg:-2.04,mkt:'4.5Md€',b52h:28.34,b52l:20.88,beta:1.25,
 pe:14.42,pb:1.37,ev_ebitda:6.05,ps:1.07,pfcf:10,ev_ebit:14.2,
 roe:10.7,roic:5.7,roa:4.2,debt:1.39,de:1.39,ic:4.2,cr:0.77,qr:0.8,
 yield:1.1,epsg:7.5,revg:4.9,margin:7.7,gm:33.6,om:12,fcf:11.8,
 capex:8.5,capr:18.6,capda:0.87,
 dcfb:18.43,dcfm:21.68,dcfu:26.02,
 pio:8,alt:1.45,rsi:49.0,mm50:22.92,mm200:24.82,
 el:18.21,eh:20.29,stop:16.02,o1:22.76,o2:26.02,
 cb:10,ch:5,cs:2,tp:29.96,score:'C',rec:'avoid',zone:false,
 moat:[['Contrats pluriannuels hôpitaux','fort'],['Réseau logistique dense','fort']],
 cats:[{t:'Hôpitaux contrats renouvellement',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Sanchez','3.5M€','Jan 2026']],
 peers:[{n:'Rentokil',pe:18,pb:4.5,roe:20,div:2.2,evebitda:12}],
 risks:{Dette:60,CAPEX:55,Contrats:35,Concurrence:40,Inflation:45,Liquidite:20},
 track:[{y:'2025',p:'Marge EBITDA 32%',ok:'ok'}],
 thesis:"Elis : hôpitaux et hôtels ne peuvent pas se passer du linge professionnel. Contrats 5-7 ans, renouvellement 95%. Cash flows très prévisibles.",
 contra:"CAPEX permanent très lourd (8.5% CA). Dette élevée. Croissance lente."},

{ticker:'SEB',x2:'',x2s:'',name:'SEB',sector:'Électroménager',cap:'mid',srd:true,idx:'SBF120',
 price:56.5,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:3.8,news5:'',dy_n:10,dy_med:1.5,div12:2.8,pe_lo:11.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 25.9 contre 7.2 attendu)',vmult:null,hn:4,eveb_h:8.3,pfcf_h:14.8,pe_h:14.9,fcur:'EUR',fcfh:'-17|316|845|43',nih:'245|232|386|316',revh:'8169|8266|8006|7960',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-3.6,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-8.2,cagr:0.9,alarm:'',qwhy:'ROIC hors EA 10.8, ROIC 7.0, dette/EBITDA 3.29, croissance CA 0.9%',qok:false,nde:3.29,fcfc:101.0,roicx:10.8,chg:-2.25,mkt:'3.2Md€',b52h:62.1,b52l:40.84,beta:1.23,
 pe:25.92,pb:1.01,ev_ebitda:7.96,ps:0.38,pfcf:10,ev_ebit:12.7,
 roe:4.9,roic:7.0,roa:4.0,debt:1.06,de:1.06,ic:4.8,cr:1.16,qr:1.2,
 yield:4.8,epsg:238.7,revg:-0.1,margin:1.5,gm:8.0,om:10,fcf:-0.6,
 capex:1.5,capr:2.7,capda:0.78,
 dcfb:66.05,dcfm:77.71,dcfu:93.25,
 pio:5,alt:1.44,rsi:51.5,mm50:57.23,mm200:50.54,
 el:65.28,eh:72.74,stop:57.45,o1:81.6,o2:93.25,
 cb:10,ch:6,cs:2,tp:73.95,score:'C',rec:'avoid',zone:false,
 moat:[['Rowenta/Tefal/Moulinex/WMF','fort'],['Distribution mondiale','modere']],
 cats:[{t:'Chine rebond',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Lescure','5.2M€','Jan 2026']],
 peers:[{n:"De'Longhi",pe:14,pb:2.5,roe:18,div:2.5,evebitda:10}],
 risks:{Chine:55,Concurrence:50,Devise:45,Matières:40,Cyclicite:45,Liquidite:20},
 track:[{y:'2025',p:'Croissance Asie +5%',ok:'partial'}],
 thesis:"SEB possède les marques de cuisson les plus connues au monde. À 1.8x livre, famille aux commandes. Rebond Chine = upside significatif.",
 contra:"Concurrence locale Chine monte en gamme. E-commerce intense. Faibles barrières sur certains segments."},

{ticker:'ERF',x2:'',x2s:'',name:'Eurofins Scientific',sector:'Tests & Analyses',cap:'large',srd:true,idx:'SBF120',
 price:78.94,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.6,news5:'',dy_n:9,dy_med:0.71,div12:0.72,pe_lo:21.2,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:10.0,pfcf_h:21.8,pe_h:22.7,fcur:'EUR',fcfh:'564|790|468|476',nih:'475|406|310|610',revh:'7296|6951|6515|6712',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-2.6,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-8.0,cagr:2.8,alarm:'',qwhy:'ROIC 6.7, croissance CA 2.8%',qok:false,nde:2.37,fcfc:128.0,roicx:15.7,chg:0.87,mkt:'8.2Md€',b52h:79.22,b52l:54.86,beta:0.81,
 pe:27.41,pb:3.79,ev_ebitda:11.37,ps:1.83,pfcf:16,ev_ebit:21.5,
 roe:11.3,roic:6.7,roa:6.0,debt:0.96,de:0.96,ic:5.2,cr:1.13,qr:1.0,
 yield:0.9,epsg:28.4,revg:2.5,margin:7.2,gm:23.1,om:12,fcf:4.2,
 capex:5.5,capr:11.4,capda:1.33,
 dcfb:63.15,dcfm:74.3,dcfu:89.16,
 pio:7,alt:2.58,rsi:61.3,mm50:74.25,mm200:67.53,
 el:62.41,eh:69.54,stop:54.92,o1:78.02,o2:89.16,
 cb:14,ch:5,cs:2,tp:72.29,score:'C',rec:'avoid',zone:false,
 moat:[['Réseau laboratoires mondial','fort'],['Accréditations réglementaires','fort']],
 cats:[{t:'Biosécurité alimentaire',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Gilles Martin','12M€','Jan 2026']],
 peers:[{n:'SGS',pe:24,pb:4.5,roe:18,div:3.5,evebitda:14},{n:'Bureau Veritas',pe:20,pb:4.0,roe:22,div:2.8,evebitda:12}],
 risks:{PostCovid:60,Marges:50,Acq:55,Gouvernance:60,Dette:45,Liquidite:15},
 track:[{y:'2025',p:'Normalisation post-COVID',ok:'partial'},{y:'2024',p:'EBITDA marge 22%',ok:'ok'}],
 thesis:"Eurofins est le leader mondial des tests alimentaires et pharmaceutiques. Les accréditations créent une barrière à l'entrée massive.",
 contra:"La croissance COVID masquait la vraie rentabilité. Gouvernance familiale opaque. CAPEX chroniquement dépassé."},

{ticker:'IPSOS',x2:'',x2s:'',name:'Ipsos',sector:'Études de marché',cap:'mid',srd:true,idx:'SBF120',
 price:35.98,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.4,news5:'',dy_n:10,dy_med:2.79,div12:2.0,pe_lo:7.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:6.2,pfcf_h:8.4,pe_h:10.8,fcur:'EUR',fcfh:'219|268|226|270',nih:'187|205|160|215',revh:'2525|2441|2390|2405',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-1.5,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-4.6,cagr:1.6,alarm:'Piotroski 4/9',qwhy:'ROIC 11.9, croissance CA 1.6%',qok:false,nde:0.9,fcfc:128.0,roicx:62.7,chg:-1.75,mkt:'2.1Md€',b52h:42.98,b52l:29.1,beta:0.65,
 pe:8.99,pb:0.99,ev_ebitda:5.97,ps:0.59,pfcf:9,ev_ebit:6.7,
 roe:11.9,roic:11.9,roa:6.5,debt:0.42,de:0.42,ic:10.0,cr:1.44,qr:1.2,
 yield:5.5,epsg:-22.0,revg:1.3,margin:6.9,gm:67.5,om:13,fcf:14.7,
 capex:1.2,capr:3.3,capda:0.82,
 dcfb:43.09,dcfm:50.69,dcfu:60.83,
 pio:4,alt:1.8,rsi:49.5,mm50:36.81,mm200:34.72,
 el:42.58,eh:47.45,stop:37.47,o1:53.22,o2:60.83,
 cb:8,ch:5,cs:2,tp:52.57,score:'C',rec:'avoid',zone:false,
 moat:[['Données panelistes mondiale','fort'],['IA analytics','modere']],
 cats:[{t:'Élections mondiales 2026',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Le Moyne','2.8M€','Jan 2026']],
 peers:[{n:'Kantar',pe:14,pb:2.5,roe:15,div:2.5,evebitda:9}],
 risks:{IA:55,Concurrence:50,Macro:45,Devise:45,Clients:40,Liquidite:20},
 track:[{y:'2025',p:'Croissance organique +6%',ok:'ok'}],
 thesis:"Ipsos n°3 mondial études de marché. 2026 = année électorale record mondiale. À 12x PE, valorisation modeste.",
 contra:"IA générative menace les études qualitatives traditionnelles."},

{ticker:'ABCA',x2:'',x2s:'',name:'ABC Arbitrage',sector:'Arbitrage',cap:'small',srd:false,idx:'SBF120',
 price:5.68,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.2,news5:'',dy_n:10,dy_med:5.94,div12:0.24,pe_lo:10.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:null,pfcf_h:14.2,pe_h:12.9,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:null,regn:null,regu:null,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:null,alarm:'',qwhy:'holding (grille dediee a venir)',qok:false,nde:null,fcfc:null,roicx:null,chg:-0.35,mkt:'0.22Md€',b52h:5.92,b52l:4.87,beta:0.28,
 pe:10.33,pb:1.79,ev_ebitda:4.62,ps:4.55,pfcf:8,ev_ebit:null,
 roe:18.4,roic:null,roa:10.3,debt:0.01,de:0.01,ic:null,cr:10.66,qr:4.8,
 yield:6.0,epsg:44.5,revg:39.8,margin:44.8,gm:48.0,om:36,fcf:6.7,
 capex:0.1,capr:null,capda:null,
 dcfb:5.59,dcfm:6.58,dcfu:7.9,
 pio:5,alt:13.65,rsi:54.2,mm50:5.42,mm200:5.31,
 el:5.26,eh:6.05,stop:4.63,o1:6.91,o2:7.9,
 cb:5,ch:4,cs:1,tp:8.2,score:'C',rec:'avoid',zone:false,
 moat:[['Algorithmes propriétaires arbitrage','fort'],['Niche défensive','fort']],
 cats:[{t:'Volatilité marchés 2026',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction','0.8M€','Jan 2026']],
 peers:[{n:'IMC Trading','pe':12,pb:2.8,roe:20,div:0.0,evebitda:8}],
 risks:{Volatilité:45,Reglement:40,Algorithmes:35,Compétition:50,Taille:60,Liquidite:55},
 track:[{y:'2025',p:'Dividende 7.2% maintenu',ok:'ok'}],
 thesis:"ABC Arbitrage : 25% de ROE, zéro dette, 7.2% de dividende. Les algorithmes fonctionnent mieux en période de volatilité élevée — et 2026 sera volatile.",
 contra:"Modèle opaque. Très peu liquide. Dépend de la volatilité pour performer."},

{ticker:'VK',x2:'',x2s:'',name:'Vallourec',sector:'Tubes acier',cap:'mid',srd:true,idx:'SBF120',
 price:18.8,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.2,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:7.2,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:3,eveb_h:4.9,pfcf_h:11.5,pe_h:8.8,fcur:'USD',fcfh:'384|321|482|-216',nih:'355|452|496|-366',revh:'3809|4034|5114|4883',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-7.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:-7.9,alarm:'',qwhy:'croissance CA -7.9%',qok:false,nde:-0.05,fcfc:104.0,roicx:19.4,chg:-0.97,mkt:'2.8Md€',b52h:27.67,b52l:15.1,beta:0.41,
 pe:13.82,pb:1.71,ev_ebitda:4.89,ps:1.2,pfcf:5,ev_ebit:6.9,
 roe:15.8,roic:19.2,roa:7.5,debt:0.36,de:0.36,ic:7.8,cr:2.13,qr:1.1,
 yield:9.3,epsg:30.2,revg:2.6,margin:9.6,gm:29.7,om:12,fcf:7.7,
 capex:2.2,capr:4.6,capda:1.1,
 dcfb:23.06,dcfm:27.13,dcfu:32.56,
 pio:8,alt:2.89,rsi:53.1,mm50:18.44,mm200:20.52,
 el:22.52,eh:25.29,stop:19.82,o1:28.49,o2:32.56,
 cb:8,ch:4,cs:2,tp:26.14,score:'C',rec:'avoid',zone:false,
 moat:[['Tubes premium pétroliers','fort'],['Brésil acier vert','modere']],
 cats:[{t:'Pétrole offshore cycle haussier',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction','2.5M€','Jan 2026']],
 peers:[{n:'Tenaris',pe:8,pb:1.4,roe:16,div:2.8,evebitda:5}],
 risks:{Pétrole:70,Cyclicite:65,Brésil:45,Devise:45,Acier:50,Liquidite:25},
 track:[{y:'2025',p:'Retour à la profitabilité',ok:'ok'}],
 thesis:"Vallourec a restructuré massivement. Bilan sain. Le Brésil va produire de l'acier vert DRI-HBI. Offshore pétrolier repart.",
 contra:"Pure cyclique. Pétrole sous 60$ = thèse détruite. Restructuration a dilué les actionnaires."},

{ticker:'FNAC',x2:'',x2s:'',name:'Fnac Darty',sector:'Distribution',cap:'mid',srd:true,idx:'SBF120',
 price:34.6,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.1,news5:'',dy_n:5,dy_med:3.37,div12:1.0,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:21.3,pfcf_h:2.0,pe_h:18.8,fcur:'EUR',fcfh:'477|358|434|208',nih:'-146|36|50|-32',revh:'10330|8081|7875|7949',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:9.1,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:9.1,alarm:'',qwhy:'ROIC hors EA 8.6, ROIC 2.9, cash None%, dette/EBITDA 18.82',qok:false,nde:18.82,fcfc:null,roicx:8.6,chg:0.0,mkt:'0.88Md€',b52h:35.95,b52l:26.25,beta:1.06,
 pe:11.03,pb:0.77,ev_ebitda:10.77,ps:0.1,pfcf:6,ev_ebit:44.4,
 roe:-5.0,roic:2.9,roa:1.7,debt:1.9,de:1.9,ic:0.7,cr:0.86,qr:0.7,
 yield:2.9,epsg:4,revg:0.8,margin:-1.6,gm:28.2,om:3,fcf:46.9,
 capex:1.2,capr:1.8,capda:null,
 dcfb:27.21,dcfm:32.01,dcfu:38.41,
 pio:5,alt:1.28,rsi:58.3,mm50:34.55,mm200:34.06,
 el:26.57,eh:29.83,stop:23.38,o1:33.61,o2:38.41,
 cb:6,ch:5,cs:4,tp:36.5,score:'D',rec:'avoid',zone:false,
 moat:[['Réseau 900 magasins','modere'],['Service After Sales','modere']],
 cats:[{t:'Plan coût 2026',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','Artémis Pinault','8.5M€','Jan 2026']],
 peers:[{n:'Media Markt',pe:9,pb:1.0,roe:11,div:3.5,evebitda:5}],
 risks:{Ecommerce:75,Marges:65,Concurrence:70,Cyclicite:55,Digital:60,Liquidite:25},
 track:[{y:'2025',p:'Coûts réduits 80M€',ok:'ok'}],
 thesis:"Fnac Darty résiste mieux que prévu à Amazon. Service après-vente et expertise conseil = avantages réels. À 0.8x livre avec 5.8% dividende.",
 contra:"Amazon grignotent les parts structurellement. Marges sous pression permanente."},

{ticker:'LNA',x2:'',x2s:'',name:'LNA Santé',sector:'Santé services',cap:'small',srd:false,idx:'SBF120',
 price:23.7,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.0,news5:'',dy_n:10,dy_med:0.89,div12:0.95,pe_lo:8.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:7.0,pfcf_h:2.7,pe_h:10.8,fcur:'EUR',fcfh:'86|98|85|90',nih:'24|22|23|26',revh:'913|807|736|728',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:2.8,gimp:null,knife:true,neglect:true,vmeth:'per',nig:-2.2,cagr:7.8,alarm:'',qwhy:'ROIC hors EA 4.4, ROIC 3.8, dette/EBITDA 5.28',qok:false,nde:5.28,fcfc:377.0,roicx:4.4,chg:1.28,mkt:'0.32Md€',b52h:36.5,b52l:22.0,beta:0.52,
 pe:9.6,pb:0.73,ev_ebitda:11.09,ps:0.26,pfcf:11,ev_ebit:15.8,
 roe:8.0,roic:3.8,roa:2.9,debt:2.74,de:2.74,ic:2.3,cr:0.87,qr:1.0,
 yield:4.1,epsg:10.2,revg:8.4,margin:2.7,gm:27.7,om:7,fcf:35.4,
 capex:2.2,capr:1.4,capda:0.16,
 dcfb:29.09,dcfm:34.22,dcfu:41.06,
 pio:8,alt:0.8,rsi:32.7,mm50:29.96,mm200:29.19,
 el:23.95,eh:30.11,stop:21.08,o1:35.93,o2:41.06,
 cb:6,ch:4,cs:1,tp:41.1,score:'C',rec:'avoid',zone:false,
 moat:[['EHPAD premium','modere'],['SSR cliniques','modere']],
 cats:[{t:'Vieillissement France mégatendance',w:'Long terme',c:'var(--gn)'}],
 ins:[['Achat','Famille Saintilan','2.8M€','Jan 2026']],
 peers:[{n:'Korian',pe:14,pb:0.8,roe:6,div:0.0,evebitda:10}],
 risks:{Reglement:55,Tarifs:50,Personnel:60,Immobilier:45,Concurrence:40,Liquidite:30},
 track:[{y:'2025',p:'Ouverture 3 établissements',ok:'ok'}],
 thesis:"LNA Santé est le bon EHPAD — qualité, taux occupation 95%, personnel motivé. Vieillissement démographique irréversible.",
 contra:"Régulation tarifaire bloque la transmission de l'inflation. Personnel coûteux et difficile à recruter."},

{ticker:'SOP',x2:'',x2s:'',name:'Sopra Steria',sector:'Services IT',cap:'mid',srd:true,idx:'CAC40',
 price:175.5,roiica:false,reinv:false,roiic:17.4,vmed:null,vepv:null,chg5:3.5,news5:'',dy_n:9,dy_med:1.67,div12:5.3,pe_lo:9.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:6.0,pfcf_h:6.5,pe_h:12.3,fcur:'EUR',fcfh:'490|582|522|409',nih:'297|251|184|248',revh:'5648|5777|5469|5101',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'communique 2026-10-05',gused:1.5,gimp:null,knife:false,neglect:false,vmeth:'per',nig:6.2,cagr:3.5,alarm:'',qwhy:'croissance officielle 1.5%',qok:false,nde:1.05,fcfc:205.0,roicx:75.0,chg:-0.4,mkt:'2.8Md€',b52h:202.2,b52l:109.4,beta:0.94,
 pe:11.29,pb:1.62,ev_ebitda:8.19,ps:0.59,pfcf:11,ev_ebit:10.2,
 roe:14.6,roic:12.0,roa:5.5,debt:0.65,de:0.65,ic:9.8,cr:0.88,qr:1.1,
 yield:3.0,epsg:5.3,revg:4.1,margin:5.2,gm:14.9,om:8,fcf:14.5,
 capex:1.5,capr:1.1,capda:0.36,
 dcfb:202.76,dcfm:238.54,dcfu:286.25,
 pio:8,alt:1.8,rsi:60.9,mm50:170.83,mm200:145.78,
 el:181.29,eh:215.64,stop:159.54,o1:250.47,o2:286.25,
 cb:10,ch:6,cs:2,tp:218.67,score:'C',rec:'avoid',zone:false,
 moat:[['Secteur public français','fort'],['Cybersécurité','modere']],
 cats:[{t:'IA intégration 2026',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction','1.2M€','Jan 2026']],
 peers:[{n:'Capgemini',pe:18,pb:3.2,roe:18,div:2.1,evebitda:11}],
 risks:{Public:50,Concurrence:55,Marges:45,Devise:35,IA:50,Liquidite:20},
 track:[{y:'2025',p:'Croissance 6%',ok:'ok'}],
 thesis:"Sopra Steria est le champion du numérique public français. Cybersécurité et transformation digitale des États = visibilité maximale.",
 contra:"Marges compressées par la concurrence offshore. Dépendance aux marchés publics cycliques politiquement."},

// ═══ CAC40 manquants ═══
{ticker:'AC',x2:'',x2s:'',name:'Accor',sector:'Hôtellerie',cap:'large',srd:true,idx:'CAC40',
 price:45.48,roiica:false,reinv:false,roiic:22.9,vmed:null,vepv:null,chg5:1.0,news5:'',dy_n:7,dy_med:2.76,div12:1.35,pe_lo:13.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:10.1,pfcf_h:19.7,pe_h:16.8,fcur:'EUR',fcfh:'613|440|415|400',nih:'449|610|633|402',revh:'5639|5606|5056|4224',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:6.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:3.8,cagr:10.1,alarm:'',qwhy:'ROIC hors EA 13.6, ROIC 9.3, dette/EBITDA 2.71',qok:false,nde:2.71,fcfc:89.0,roicx:13.6,chg:-3.03,mkt:'9.8Md€',b52h:52.0,b52l:37.54,beta:0.88,
 pe:39.89,pb:3.48,ev_ebitda:14.42,ps:1.84,pfcf:14,ev_ebit:18.4,
 roe:8.0,roic:9.3,roa:4.6,debt:1.07,de:1.07,ic:5.1,cr:1.29,qr:0.7,
 yield:2.9,epsg:-58.8,revg:0.5,margin:5.8,gm:22.5,om:10,fcf:5.9,
 capex:0.8,capr:3.5,capda:0.6,dcfb:27.93,dcfm:32.86,dcfu:39.43,
 pio:6,alt:1.67,rsi:49.3,mm50:45.86,mm200:45.2,
 el:26.95,eh:30.49,stop:23.72,o1:34.5,o2:39.43,cb:12,ch:5,cs:2,tp:55.24,score:'D',rec:'avoid',zone:false,
 moat:[['5500 hôtels 110 pays','fort'],['Asset-light model','fort']],
 cats:[{t:'Tourisme record 2026',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Bazin','5.2M€','Jan 2026']],
 peers:[{n:'Marriott',pe:25,pb:999,roe:999,div:1.2,evebitda:18}],
 risks:{Tourisme:55,Devise:50,Terrorisme:35,Économie:50,Concurrence:40,Liquidite:15},
 track:[{y:'2025',p:'RevPAR +8%',ok:'ok'}],
 thesis:"Accor est le géant hôtelier européen dans un secteur tourisme post-COVID en plein boom. Le modèle asset-light génère du cash sans CAPEX lourd.",
 contra:"Airbnb continue de prendre des parts sur le loisir. Exposition forte à la macro."},

{ticker:'AF',x2:'',x2s:'',name:'Air France-KLM',sector:'Transport aérien',cap:'large',srd:true,idx:'CAC40',
 price:10.34,roiica:false,reinv:false,roiic:25.1,vmed:null,vepv:null,chg5:-2.6,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:2.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:2.6,pfcf_h:5.3,pe_h:4.1,fcur:'EUR',fcfh:'606|-232|55|1884',nih:'1593|317|934|728',revh:'33007|31459|30019|26393',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:18.8,gimp:null,knife:false,neglect:false,vmeth:'per',nig:29.8,cagr:7.7,alarm:'',qwhy:'cash 65.0%',qok:false,nde:1.79,fcfc:65.0,roicx:22.6,chg:-1.81,mkt:'3.8Md€',b52h:14.43,b52l:8.37,beta:1.33,
 pe:2.65,pb:-4.4,ev_ebitda:3.83,ps:0.08,pfcf:6,ev_ebit:5.3,
 roe:63.1,roic:21.9,roa:3.3,debt:5.52,de:5.52,ic:3.2,cr:0.67,qr:0.6,
 yield:0.0,epsg:-73.2,revg:9.9,margin:3.4,gm:21.1,om:5,fcf:22.3,
 capex:3.2,capr:13.5,capda:1.37,dcfb:19.34,dcfm:22.75,dcfu:27.3,
 pio:7,alt:0.97,rsi:31.9,mm50:11.5,mm200:11.23,
 el:19.11,eh:21.29,stop:16.82,o1:23.89,o2:27.3,cb:6,ch:5,cs:6,tp:12.32,score:'C',rec:'avoid',zone:false,
 moat:[['Hub Roissy CDG','modere']],
 cats:[{t:'Trafic transatlantique record',w:'2026',c:'var(--gn)'}],
 ins:[],
 peers:[{n:'Lufthansa',pe:4,pb:0.8,roe:12,div:2.5,evebitda:3}],
 risks:{Carburant:80,Dette:85,Grèves:75,Concurrence:70,Reglement:65,Liquidite:40},
 track:[{y:'2025',p:'Dette encore élevée',ok:'partial'}],
 thesis:"Air France à 5x PE avec trafic en hausse. Si la compagnie désendette, le potentiel est 2-3x.",
 contra:"Dette insoutenable. Exposition carburant massive. Culture syndicale coûteuse. À éviter pour investisseur prudent."},

{ticker:'BN',x2:'',x2s:'',name:'Danone',sector:'Agroalimentaire',cap:'large',srd:true,idx:'CAC40',
 price:60.6,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.2,news5:'',dy_n:10,dy_med:3.16,div12:2.25,pe_lo:20.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:12.4,pfcf_h:14.8,pe_h:29.8,fcur:'EUR',fcfh:'2724|2908|2595|2091',nih:'1825|2021|881|959',revh:'27283|27376|27619|27661',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:11.7,gimp:null,knife:false,neglect:false,vmeth:'per',nig:23.9,cagr:-0.5,alarm:'',qwhy:'ROIC hors EA 14.4, ROIC 5.9, dette/EBITDA 2.83, croissance CA -0.5%',qok:false,nde:2.83,fcfc:181.0,roicx:14.4,chg:-1.56,mkt:'40Md€',b52h:80.14,b52l:57.26,beta:0.2,
 pe:20.07,pb:2.21,ev_ebitda:10.81,ps:1.42,pfcf:14,ev_ebit:16.1,
 roe:12.2,roic:5.9,roa:5.0,debt:0.99,de:0.99,ic:6.1,cr:0.97,qr:0.8,
 yield:3.7,epsg:12.4,revg:1.4,margin:7.1,gm:50.0,om:12,fcf:7.0,
 capex:2.8,capr:3.9,capda:0.78,dcfb:48.68,dcfm:57.27,dcfu:68.72,
 pio:7,alt:2.2,rsi:50.3,mm50:62.33,mm200:66.23,
 el:48.11,eh:53.6,stop:42.34,o1:60.13,o2:68.72,cb:10,ch:6,cs:2,tp:78.52,score:'C',rec:'avoid',zone:false,
 moat:[['Danone/Évian/Aptamil','modere'],['Nutrition médicale','fort']],
 cats:[{t:'Rotation vers defensives',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Faber','4.2M€','Jan 2026']],
 peers:[{n:'Nestlé',pe:18,pb:5.2,roe:20,div:3.2,evebitda:12},{n:'Unilever',pe:14,pb:6.5,roe:35,div:3.8,evebitda:10}],
 risks:{Chine:45,Inflation:40,Concurrence:45,Devise:40,Reglement:35,Liquidite:10},
 track:[{y:'2025',p:'Marge op. 12%',ok:'ok'}],
 thesis:"Danone est une valeur défensive à 18x PE avec 3.5% de dividende. La nutrition médicale (Nutricia) est un actif premium récurrent.",
 contra:"Croissance structurellement limitée dans le lait infantile. Concurrence marques distributeurs."},

{ticker:'CA',x2:'',x2s:'',name:'Carrefour',sector:'Distribution alimentaire',cap:'large',srd:true,idx:'CAC40',
 price:16.25,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.1,news5:'',dy_n:10,dy_med:3.09,div12:1.18,pe_lo:6.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:2.2,pfcf_h:4.2,pe_h:10.3,fcur:'EUR',fcfh:'2425|2462|2676|2337',nih:'319|723|1659|1348',revh:'84024|83453|84910|83088',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-18.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-38.1,cagr:0.4,alarm:'',qwhy:'croissance CA 0.4%',qok:false,nde:-0.2,fcfc:245.0,roicx:103.8,chg:-2.17,mkt:'11Md€',b52h:17.54,b52l:12.63,beta:0.58,
 pe:7.56,pb:1.04,ev_ebitda:8.12,ps:0.14,pfcf:7,ev_ebit:12.5,
 roe:8.4,roic:14.5,roa:2.5,debt:1.85,de:1.85,ic:3.0,cr:0.9,qr:0.7,
 yield:5.8,epsg:6,revg:2.0,margin:0.9,gm:17.8,om:3,fcf:21.1,
 capex:1.8,capr:1.8,capda:0.65,dcfb:18.75,dcfm:22.06,dcfu:26.47,
 pio:5,alt:1.75,rsi:52.0,mm50:16.1,mm200:15.35,
 el:18.31,eh:20.56,stop:16.11,o1:23.16,o2:26.47,cb:8,ch:5,cs:3,tp:16.87,moatChk:[1,1,1,1,0,0,0.5,0.5,0,0.5,null,0.5],score:'C',rec:'avoid',zone:false,
 moat:[['Réseau 13000 magasins mondial','modere'],['Hard discount transition','modere']],
 cats:[{t:'Brésil croissance accélérée',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Moulin','18M€','Jan 2026']],
 peers:[{n:'Casino (restructuré)',pe:999,pb:0.3,roe:-5,div:0.0,evebitda:8},{n:'Aldi/Lidl (privé)',pe:999,pb:999,roe:999,div:0.0,evebitda:999}],
 risks:{Concurrence:65,Inflation:50,Brésil:45,Endettement:50,Numérique:55,Liquidite:20},
 track:[{y:'2025',p:'Cash flow positif',ok:'ok'},{y:'2024',p:'Brésil +12%',ok:'ok'}],
 thesis:"Carrefour est le seul grand distributeur français coté. Le Brésil compense le ralentissement Europe. 5.5% de dividende avec buybacks.",
 contra:"Lidl/Aldi prennent des parts. Marges structurellement très fines. Amazon Grocery monte en puissance."},

{ticker:'HO',x2:'',x2s:'',name:'Thales',sector:'Défense & Technologie',cap:'large',srd:true,idx:'CAC40',
 price:232.0,roiica:false,reinv:false,roiic:31.5,vmed:177.24,vepv:69.6,chg5:4.2,news5:'',dy_n:10,dy_med:1.98,div12:3.9,pe_lo:19.8,gmod:8.4,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:7.1,irr:7.1,dq:'',vmult:180.38,hn:4,eveb_h:12.4,pfcf_h:16.4,pe_h:24.7,fcur:'EUR',fcfh:'2565|2015|886|2491',nih:'1674|1420|1023|1121',revh:'22136|20577|18428|17569',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:203.9,vpess:118.85,nregu:2,regn:3,regu:3,place:'Paris',mthreat:'dependance aux budgets publics',mtype:'defense souveraine, contrats longs, barrieres reglementaires',mscore:4,near:false,gsrc:'communique 2026-10-06',gused:8.4,gimp:14.2,knife:false,neglect:false,vmeth:'qarp',nig:14.3,cagr:8.0,alarm:'',qwhy:'',qok:true,nde:0.49,fcfc:152.0,roicx:65.0,chg:-0.85,mkt:'19Md€',b52h:274.2,b52l:211.9,beta:0.14,
 pe:31.96,pb:5.95,ev_ebitda:15.85,ps:2.09,pfcf:18,ev_ebit:20.9,
 roe:19.4,roic:13.7,roa:3.8,debt:0.7,de:0.7,ic:8.1,cr:0.83,qr:1.2,
 yield:1.7,epsg:-27.0,revg:6.7,margin:6.6,gm:26.9,om:12,fcf:5.4,
 capex:2.2,capr:3.4,capda:0.7,dcfb:150.65,dcfm:177.24,dcfu:212.69,
 pio:9,alt:1.74,rsi:53.8,mm50:237.99,mm200:240.89,
 el:132.93,eh:150.65,stop:106.97,o1:203.9,o2:224.29,cb:16,ch:5,cs:1,tp:293.61,score:'C',rec:'hold',zone:false,
 moat:[['Défense/sécurité France','fort'],['Cybersécurité','fort'],['Aviation civile','modere']],
 cats:[{t:'Budgets défense EU +30%',w:'2026',c:'var(--gn)'},
       {t:'Cybersécurité IA',w:'2026',c:'var(--gd)'}],
 ins:[['Achat','CEO Caine','8.2M€','Jan 2026']],
 peers:[{n:'BAE Systems',pe:15,pb:4.5,roe:28,div:2.8,evebitda:10},{n:'Leonardo',pe:14,pb:2.8,roe:18,div:2.5,evebitda:9}],
 risks:{Geopol:35,Reglement:40,Export:45,Techno:35,Concurrence:30,Liquidite:10},
 track:[{y:'2025',p:'Carnet commandes +18%',ok:'ok'},{y:'2024',p:'Défense +25%',ok:'ok'}],
 thesis:"Thales est le bénéficiaire direct du réarmement européen post-Ukraine. Cybersécurité + défense = deux mégatendances simultanées. Carnet de commandes record.",
 contra:"Exposition exportations gouvernementales. Valorisation déjà bien pricée à 22x PE."},

{ticker:'ATO',x2:'',x2s:'',name:'Atos',sector:'IT',cap:'mid',srd:true,idx:'CAC40',
 price:22.1,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.5,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:1.2,pfcf_h:10.2,pe_h:1.7,fcur:'EUR',fcfh:'69|-1846|-618|176',nih:'-1404|248|-3441|-1012',revh:'8001|9577|10693|11270',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-10.8,gimp:null,knife:true,neglect:false,vmeth:'per',nig:null,cagr:-10.8,alarm:'Piotroski 4/9',qwhy:'ROIC hors EA -107.6, ROIC -40.0, cash None%, dette/EBITDA None, perte exploitation, croissance CA -10.8%',qok:false,nde:null,fcfc:null,roicx:-107.6,chg:-1.6,mkt:'0.38Md€',b52h:61.95,b52l:19.59,beta:1.62,
 pe:5.7,pb:-0.34,ev_ebitda:4.96,ps:0.06,pfcf:999,ev_ebit:null,
 roe:-45,roic:-40.0,roa:2.3,debt:4.2,de:null,ic:-1.8,cr:1.18,qr:0.5,
 yield:0.0,epsg:0,revg:-15.2,margin:-16.4,gm:5.2,om:-8,fcf:16.1,
 capex:0.8,capr:2.1,capda:0.36,dcfb:41.33,dcfm:48.62,dcfu:58.34,
 pio:4,alt:0.53,rsi:42.6,mm50:25.18,mm200:35.61,
 el:36.95,eh:43.95,stop:32.52,o1:51.05,o2:58.34,cb:2,ch:3,cs:10,tp:34.98,score:'C',rec:'avoid',zone:false,
 moat:[],
 cats:[{t:'Restructuration',w:'2026',c:'var(--rd)'}],
 ins:[],
 peers:[{n:'Capgemini',pe:18,pb:3.2,roe:18,div:2.1,evebitda:11}],
 risks:{Faillite:95,Dette:95,Confiance:90,Clients:85,Emploi:80,Liquidite:75},
 track:[{y:'2025',p:'Restructuration pénible',ok:'m'},{y:'2024',p:'Plan de sauvegarde',ok:'m'}],
 thesis:"Pari ultra-spéculatif uniquement. Si restructuration réussie, potentiel 5-10x depuis les plus bas.",
 contra:"Quasi-faillite. Dette insoutenable. Clients qui partent. À éviter absolument pour tout investisseur sérieux."},

// ═══ SBF120 & SRD supplémentaires ═══
{ticker:'DBG',x2:'',x2s:'',name:'Derichebourg',sector:'Services environnementaux',cap:'mid',srd:true,idx:'SBF120',
 price:7.71,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.8,news5:'',dy_n:9,dy_med:3.37,div12:0.13,pe_lo:2.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:4.2,pfcf_h:5.7,pe_h:6.5,fcur:'EUR',fcfh:'129|182|70|279',nih:'122|75|137|238',revh:'3345|3616|3630|4359',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-14.1,gimp:null,knife:false,neglect:true,vmeth:'per',nig:-19.9,cagr:-8.4,alarm:'',qwhy:'ROIC hors EA 11.0, ROIC 9.2, croissance CA -8.4%',qok:false,nde:2.15,fcfc:116.0,roicx:11.0,chg:-2.03,mkt:'1.1Md€',b52h:11.0,b52l:5.62,beta:1.8,
 pe:9.3,pb:1.04,ev_ebitda:7.97,ps:0.35,pfcf:6,ev_ebit:12.2,
 roe:11.9,roic:9.2,roa:4.2,debt:0.73,de:0.73,ic:4.2,cr:1.09,qr:1.0,
 yield:1.6,epsg:15.9,revg:7.8,margin:3.8,gm:25.2,om:7,fcf:10.6,
 capex:1.2,capr:3.0,capda:0.65,dcfb:8.52,dcfm:10.02,dcfu:12.02,
 pio:8,alt:2.11,rsi:27.6,mm50:8.68,mm200:8.93,
 el:8.32,eh:9.34,stop:7.32,o1:10.52,o2:12.02,cb:8,ch:5,cs:2,tp:10.06,score:'C',rec:'avoid',zone:false,
 moat:[['Recyclage métaux leader France','fort'],['Services aéronautiques','modere']],
 cats:[{t:'Transition circulaire',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Derichebourg','8.5M€','Jan 2026']],
 peers:[{n:'Veolia',pe:15,pb:2.2,roe:14,div:4.8,evebitda:8}],
 risks:{Métaux:60,Cyclicite:55,Aéro:45,Reglement:40,Devise:30,Liquidite:25},
 track:[{y:'2025',p:'Recyclage +8%',ok:'ok'}],
 thesis:"Derichebourg est le leader français du recyclage métaux — actif de la transition circulaire. 5.8% de dividende avec famille aux commandes.",
 contra:"Cyclicité des prix des métaux. Aéronautique représente 40% du CA."},

{ticker:'LPE',x2:'',x2s:'',name:'Laurent-Perrier',sector:'Champagne',cap:'small',srd:false,idx:'SBF120',
 price:79.2,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.6,news5:'',dy_n:10,dy_med:1.45,div12:2.1,pe_lo:10.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:9.3,pfcf_h:15.8,pe_h:11.6,fcur:'EUR',fcfh:'26|-13|-2|57',nih:'50|47|64|58',revh:'304|294|313|308',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-2.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-5.4,cagr:-0.4,alarm:'',qwhy:'ROIC hors EA 8.0, ROIC 7.7, cash 31.0%, croissance CA -0.4%',qok:false,nde:2.48,fcfc:31.0,roicx:8.0,chg:-1.49,mkt:'0.45Md€',b52h:98.6,b52l:73.6,beta:0.16,
 pe:9.4,pb:0.7,ev_ebitda:8.1,ps:1.5,pfcf:14,ev_ebit:8.9,
 roe:7.7,roic:7.7,roa:4.4,debt:0.38,de:0.38,ic:8.2,cr:6.96,qr:1.8,
 yield:2.6,epsg:20.6,revg:4.5,margin:16.3,gm:56.6,om:19,fcf:5.7,
 capex:1.2,capr:3.5,capda:1.81,dcfb:89.38,dcfm:105.15,dcfu:126.18,
 pio:6,alt:1.97,rsi:55.1,mm50:79.95,mm200:83.79,
 el:82.02,eh:95.9,stop:72.18,o1:110.41,o2:126.18,cb:5,ch:5,cs:2,tp:80,score:'C',rec:'avoid',zone:false,
 moat:[['Champagne ultra-premium','fort'],['Cuvée Grand Siècle rare','fort']],
 cats:[{t:'Premium résilient',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille de Nonancourt','3.2M€','Jan 2026']],
 peers:[{n:'Rémy Cointreau',pe:22,pb:3.5,roe:16,div:2.8,evebitda:15}],
 risks:{Champagne:45,Devise:40,Stocks:55,Cyclicite:40,Taille:50,Liquidite:45},
 track:[{y:'2025',p:'Marge 19%',ok:'ok'}],
 thesis:"Laurent-Perrier est la pépite cachée du champagne premium. Grand Siècle à 300€/bouteille est en liste d'attente mondiale. Famille aux commandes depuis 4 générations.",
 contra:"Taille très limitée. Peu liquide. Stocks de champagne immobilisés 3-5 ans."},

{ticker:'ASML',x2:'',x2s:'',name:'ASML',sector:'Semi-conducteurs EUV',cap:'large',srd:false,idx:'AEX',
 price:1496.0,roiica:false,reinv:false,roiic:74.8,vmed:593.34,vepv:448.8,chg5:-5.1,news5:'',dy_n:10,dy_med:0.91,div12:7.78,pe_lo:34.2,gmod:18.5,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'cyclique',wht:15.0,irrn:5.0,irr:5.1,dq:'',vmult:676.16,hn:4,eveb_h:27.1,pfcf_h:32.1,pe_h:35.5,fcur:'EUR',fcfh:'11027|9083|3247|7168',nih:'9609|7572|7839|5624',revh:'32667|28263|27558|21173',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:627.04,vpess:448.8,nregu:2,regn:3,regu:3,place:'Amsterdam',mthreat:'geopolitique (restrictions Chine), cycles des semi-conducteurs',mtype:'monopole mondial des machines EUV, indispensables aux puces avancees',mscore:5,near:false,gsrc:'communique 2026-10-06',gused:25.0,gimp:30.0,knife:false,neglect:false,vmeth:'qarp',nig:19.5,cagr:15.6,alarm:'',qwhy:'',qok:true,nde:-0.68,fcfc:100.0,roicx:137.2,chg:1.27,mkt:'246Md€',b52h:1741.0,b52l:822.2,beta:1.3,
 pe:42.77,pb:25.98,ev_ebitda:34.31,ps:14.61,pfcf:22,ev_ebit:48.2,
 roe:65.6,roic:78.7,roa:18.3,debt:0.09,de:0.09,ic:97.4,cr:1.49,qr:1.5,
 yield:0.5,epsg:135.9,revg:55.2,margin:34.1,gm:54.3,om:32,fcf:1.9,
 capex:2.5,capr:5.0,capda:1.59,dcfb:504.34,dcfm:593.34,dcfu:712.01,
 pio:8,alt:13.21,rsi:44.6,mm50:1517.64,mm200:1373.25,
 el:415.34,eh:474.67,stop:403.92,o1:627.04,o2:689.74,cb:22,ch:5,cs:1,tp:2107.73,score:'B',rec:'hold',zone:false,
 moat:[['Monopole absolu lithographie EUV','fort'],['R&D inégalable','fort']],
 cats:[{t:'Reprise commandes TSMC/Samsung',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO van den Brink','12M€','Jan 2026']],
 peers:[{n:'Lam Research',pe:22,pb:8,roe:58,div:1.2,evebitda:14},{n:'Applied Materials',pe:18,pb:6.5,roe:42,div:1.0,evebitda:12}],
 risks:{Chine:75,Cyclicite:60,Valorisation:50,Geopol:65,Innovation:35,Liquidite:10},
 track:[{y:'2025',p:'Carnet 40Md€ record',ok:'ok'},{y:'2024',p:'EUV High NA lancé',ok:'ok'}],
 thesis:"ASML est le monopole le plus précieux au monde. La lithographie EUV est irremplaçable — aucun concurrent à horizon 15 ans. Éligible PEA via AEX Amsterdam.",
 contra:"Cyclicité semi-conducteurs. Chine représente 25% des revenus avec risque géopolitique croissant. Correction de -30% depuis le pic."},

{ticker:'PRX',x2:'',x2s:'',name:'Prosus',sector:'Tech investissement',cap:'large',srd:false,idx:'AEX',
 price:35.7,roiica:false,reinv:false,roiic:15.2,vmed:null,vepv:null,chg5:-0.5,news5:'',dy_n:6,dy_med:0.24,div12:0.2,pe_lo:7.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:10.2,pfcf_h:70.4,pe_h:10.2,fcur:'USD',fcfh:'1401|1814|978|-383',nih:'11638|12367|6606|10112',revh:'9705|6170|5467|4947',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Amsterdam',near:false,gsrc:'yahoo (4 ans publies)',gused:15.0,gimp:null,knife:true,neglect:false,vmeth:'per',nig:4.8,cagr:25.2,alarm:'',qwhy:'cash 9.0%, perte exploitation',qok:false,nde:0.84,fcfc:9.0,roicx:20.6,chg:-0.72,mkt:'68Md€',b52h:63.94,b52l:34.48,beta:0.78,
 pe:7.92,pb:1.6,ev_ebitda:291.44,ps:7.69,pfcf:15,ev_ebit:14.7,
 roe:22.2,roic:19.5,roa:0.3,debt:0.33,de:0.33,ic:19.3,cr:2.43,qr:2.2,
 yield:0.8,epsg:15,revg:12,margin:119.9,gm:46.4,om:18,fcf:1.9,
 capex:0.8,capr:2.1,capda:0.4,dcfb:56.81,dcfm:66.84,dcfu:80.21,
 pio:5,alt:4.21,rsi:47.7,mm50:36.58,mm200:40.85,
 el:50.8,eh:60.42,stop:44.7,o1:70.18,o2:80.21,cb:10,ch:5,cs:2,tp:60.72,score:'C',rec:'avoid',zone:false,
 moat:[['Tencent 25% participation','fort'],['iFood Brésil','fort']],
 cats:[{t:'Buyback Tencent stake',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction Naspers','45M€','Jan 2026']],
 peers:[{n:'Tencent',pe:16,pb:3.5,roe:22,div:1.5,evebitda:10}],
 risks:{Tencent:65,Chine:70,Décote:50,Gouvernance:45,Devise:40,Liquidite:15},
 track:[{y:'2025',p:'Décote ANR se réduit',ok:'partial'}],
 thesis:"Prosus se traite avec une décote de 40% sur son ANR (Tencent + iFood). Les buybacks massifs réduisent cette décote mécaniquement.",
 contra:"Décote de holding peut persister. Dépendance Tencent Chine. Gouvernance complexe Naspers/Prosus."},

{ticker:'ADYEN',x2:'',x2s:'',name:'Adyen',sector:'Paiements',cap:'large',srd:false,idx:'AEX',
 price:930.4,roiica:false,reinv:false,roiic:17.3,vmed:null,vepv:null,chg5:1.0,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:41.5,gmod:null,fcfh:'905|1604|1800|1922',nih:'1063|925|698|564',revh:'2647|2226|1863|8936',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'croissance Yahoo -33.3 %/an : probablement faussee par une acquisition ou une cession',vmult:null,hn:4,eveb_h:26.8,pfcf_h:24.5,pe_h:50.4,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:2,place:'Amsterdam',near:false,gsrc:'yahoo (4 ans publies)',gused:-4.9,gimp:null,knife:true,neglect:false,vmeth:'per',nig:23.5,cagr:-33.3,alarm:'',qwhy:'croissance CA -33.3%',qok:false,nde:-6.56,fcfc:192.0,roicx:21.0,chg:-1.78,mkt:'37Md€',b52h:1600.8,b52l:772.4,beta:1.89,
 pe:26.15,pb:4.97,ev_ebitda:13.88,ps:11.36,pfcf:35,ev_ebit:12.7,
 roe:21.3,roic:21.0,roa:5.2,debt:0.07,de:0.07,ic:71.8,cr:1.65,qr:4.2,
 yield:0.0,epsg:12.9,revg:18.9,margin:43.6,gm:68.5,om:30,fcf:3.1,
 capex:1.2,capr:4.8,capda:0.93,dcfb:426.86,dcfm:502.19,dcfu:602.63,
 pio:6,alt:4.13,rsi:54.6,mm50:956.43,mm200:966.11,
 el:401.75,eh:462.01,stop:353.54,o1:527.3,o2:602.63,cb:18,ch:6,cs:2,tp:1375.94,score:'C',rec:'avoid',zone:false,
 moat:[['Plateforme unifiée monde entier','fort'],['Technologie propriétaire','fort']],
 cats:[{t:'US expansion accélérée',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Stienstra','8.5M€','Jan 2026']],
 peers:[{n:'Stripe (privé)',pe:999,pb:999,roe:999,div:0.0,evebitda:999},{n:'PayPal',pe:14,pb:2.5,roe:22,div:0.0,evebitda:10}],
 risks:{Concurrence:55,Valorisation:60,US:45,Reglement:40,Croissance:35,Liquidite:10},
 track:[{y:'2025',p:'Marges restaurées 48%',ok:'ok'},{y:'2024',p:'Crise marges résolue',ok:'ok'}],
 thesis:"Adyen est la meilleure plateforme paiement mondiale — une seule stack technologique pour tous les pays. L'expansion US accélère. Zéro dette, 20% ROE.",
 contra:"45x PE exige une exécution parfaite. Stripe prive reste un concurrent redoutable. Réglementation paiements croissante."},

{ticker:'HEIA',x2:'',x2s:'',name:'Heineken',sector:'Brasseries',cap:'large',srd:false,idx:'AEX',
 price:76.28,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:5.6,news5:'',dy_n:10,dy_med:1.78,div12:0.76,pe_lo:18.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:10.0,pfcf_h:17.6,pe_h:21.5,fcur:'EUR',fcfh:'2610|3038|1753|2485',nih:'1885|978|2304|2682',revh:'28753|29821|30362|28719',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Amsterdam',near:false,gsrc:'yahoo (4 ans publies)',gused:-5.5,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-11.1,cagr:0.0,alarm:'',qwhy:'ROIC hors EA 12.6, ROIC 8.2, croissance CA 0.0%',qok:false,nde:2.32,fcfc:126.0,roicx:12.6,chg:0.24,mkt:'38Md€',b52h:80.44,b52l:63.9,beta:0.56,
 pe:18.6,pb:2.19,ev_ebitda:11.23,ps:1.43,pfcf:14,ev_ebit:17.1,
 roe:12.1,roic:8.2,roa:4.0,debt:0.95,de:0.95,ic:5.7,cr:0.75,qr:0.7,
 yield:2.5,epsg:54.1,revg:4.7,margin:7.7,gm:37.0,om:12,fcf:6.2,
 capex:3.5,capr:8.4,capda:0.94,dcfb:57.55,dcfm:67.7,dcfu:81.24,
 pio:7,alt:2.01,rsi:74.4,mm50:72.04,mm200:70.83,
 el:56.87,eh:63.37,stop:50.05,o1:71.09,o2:81.24,cb:10,ch:6,cs:2,tp:88.79,score:'C',rec:'avoid',zone:false,
 moat:[['Heineken marque mondiale','fort'],['Distribution 190 pays','fort']],
 cats:[{t:'Afrique croissance structurelle',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Heineken','22M€','Jan 2026']],
 peers:[{n:'AB InBev',pe:16,pb:3.0,roe:20,div:1.8,evebitda:9},{n:'Carlsberg',pe:14,pb:3.5,roe:15,div:3.2,evebitda:9}],
 risks:{Santé:50,Concurrence:45,Devise:55,Matières:40,Cyclicite:35,Liquidite:10},
 track:[{y:'2025',p:'Afrique +14%',ok:'ok'}],
 thesis:"Heineken est la bière premium mondiale éligible PEA. L'Afrique sub-saharienne représente une croissance structurelle décennale. Famille aux commandes.",
 contra:"Tendance santé pèse sur la bière. Matières premières volatiles. Dette moderee."},

{ticker:'NOVO',x2:'',x2s:'',name:'Novo Nordisk',sector:'Pharma diabète/obésité',cap:'large',srd:false,idx:'CSE',
 price:34.32,roiica:false,reinv:true,roiic:24.7,vmed:68.37,vepv:36.23,chg5:0.0,news5:'',dy_n:10,dy_med:2.21,div12:1.57,pe_lo:14.3,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:27.0,irrn:12.6,irr:13.8,dq:'',vmult:68.37,hn:4,eveb_h:24.3,pfcf_h:42.6,pe_h:32.6,fcur:'DKK',fcfh:'28989|69659|70012|64134',nih:'102434|100988|83683|55525',revh:'309064|290403|232261|176954',yrs:'2025|2024|2023|2022',unc:'non evaluee',vopt:68.76,vpess:43.86,nregu:3,regn:3,regu:3,place:'Copenhague',near:true,gsrc:'yahoo (4 ans publies)',gused:21.5,gimp:-5.0,knife:true,neglect:false,vmeth:'qarp',nig:22.6,cagr:20.4,alarm:'',qwhy:'cash 68.0% mais reinvesti a 24.7% (regle reinvestissement)',qok:false,nde:0.7,fcfc:68.0,roicx:54.6,chg:-1.19,mkt:'280Md€',b52h:54.85,b52l:30.0,beta:0.38,
 pe:9.63,pb:5.13,ev_ebitda:7.17,ps:3.44,pfcf:15,ev_ebit:9.2,
 roe:59.8,roic:51.1,roa:18.7,debt:0.63,de:0.63,ic:32.0,cr:0.87,qr:2.5,
 yield:4.5,epsg:-20.6,revg:2.1,margin:35.3,gm:82.0,om:38,fcf:2.6,
 capex:3.5,capr:29.2,capda:6.14,dcfb:58.45,dcfm:68.76,dcfu:82.51,
 pio:5,alt:3.27,rsi:43.6,mm50:37.01,mm200:38.32,
 el:51.57,eh:58.45,stop:39.48,o1:68.76,o2:75.64,cb:18,ch:6,cs:2,tp:40.35,score:'C',rec:'avoid',zone:false,
 moat:[['Ozempic/Wegovy monopole obésité','fort'],['Pipeline GLP-1 inégalable','fort']],
 cats:[{t:'Wegovy US volume record',w:'T2 2026',c:'var(--gn)'},
       {t:'CagriSema Phase 3',w:'2026',c:'var(--gd)'}],
 ins:[['Achat','CEO Jørgensen','18M€','Jan 2026']],
 peers:[{n:'Eli Lilly',pe:35,pb:25,roe:60,div:0.6,evebitda:22},{n:'Sanofi',pe:18,pb:2.8,roe:16,div:4.1,evebitda:13}],
 risks:{Concurrence:55,Remboursement:60,Production:50,Valorisation:45,Reglement:40,Liquidite:10},
 track:[{y:'2025',p:'Wegovy revenues record',ok:'ok'},{y:'2024',p:'Guidance relevée 4x',ok:'ok'}],
 thesis:"Novo Nordisk a Ozempic/Wegovy — les médicaments qui vont changer la santé mondiale. L'obésité touche 40% des adultes américains. Le pipeline GLP-1 s'étend au coeur, foie, rein. Correction de -50% = opportunité historique.",
 contra:"Concurrence Eli Lilly (Zepbound) s'intensifie. Problèmes de production capacité. Remboursements assurances maladie sous pression. Valorisation encore élevée malgré la baisse."},

{ticker:'RACE',x2:'',x2s:'',name:'Ferrari',sector:'Luxe automobile',cap:'large',srd:false,idx:'MIL',
 price:353.35,roiica:false,reinv:true,roiic:51.4,vmed:198.39,vepv:106.01,chg5:0.7,news5:'',dy_n:10,dy_med:0.71,div12:3.615,pe_lo:35.1,gmod:6.6,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:26.0,irrn:5.6,irr:5.9,dq:'',vmult:251.23,hn:4,eveb_h:23.1,pfcf_h:62.9,pe_h:41.5,fcur:'EUR',fcfh:'1406|938|848|599',nih:'1597|1522|1252|933',revh:'7146|6677|5970|5095',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:224.36,vpess:147.74,nregu:3,regn:3,regu:3,place:'Milan',mthreat:'succession du modele thermique, dependance aux plus riches',mtype:'marque iconique, rarete organisee, listes d attente',mscore:5,near:true,gsrc:'communique 2026-10-12',gused:6.6,gimp:22.7,knife:false,neglect:false,vmeth:'qarp',nig:19.6,cagr:11.9,alarm:'',qwhy:'cash 71.0% mais reinvesti a 51.4% (regle reinvestissement)',qok:false,nde:0.51,fcfc:71.0,roicx:35.5,chg:-0.84,mkt:'65Md€',b52h:377.5,b52l:269.0,beta:0.61,
 pe:38.28,pb:16.99,ev_ebitda:26.08,ps:8.43,pfcf:38,ev_ebit:30.6,
 roe:45.4,roic:29.6,roa:13.6,debt:0.86,de:0.86,ic:51.1,cr:2.43,qr:1.8,
 yield:1.0,epsg:10.1,revg:8.4,margin:22.2,gm:51.6,om:25,fcf:2.3,
 capex:2.8,capr:13.2,capda:1.42,dcfb:168.63,dcfm:198.39,dcfu:238.07,
 pio:9,alt:8.83,rsi:52.5,mm50:354.62,mm200:317.01,
 el:148.79,eh:168.63,stop:132.97,o1:224.36,o2:246.8,cb:16,ch:5,cs:1,tp:387.86,score:'C',rec:'avoid',zone:false,
 moat:[['Marque la plus exclusive voiture','fort'],['Liste attente 2+ ans','fort'],['Pricing power illimité','fort']],
 cats:[{t:'Ferrari hybride Purosangue',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Agnelli','85M€','Jan 2026']],
 peers:[{n:'Hermès',pe:50,pb:22,roe:36,div:0.6,evebitda:32},{n:'Porsche',pe:12,pb:2.2,roe:14,div:2.5,evebitda:8}],
 risks:{Cyclicite:30,Régulation:45,VE:40,Valorisation:55,Devise:40,Liquidite:10},
 track:[{y:'2025',p:'Marge 25% record',ok:'ok'},{y:'2024',p:'250 voitures/semaine',ok:'ok'}],
 thesis:"Ferrari est Hermès sur roues. 45x PE pour une société qui produit intentionnellement moins que la demande. Liste d'attente 2 ans = pricing power illimité. Éligible PEA via Bourse de Milan.",
 contra:"45x PE n'accepte aucune erreur. Régulation VE européenne. Cyclicité luxe si récession sévère."},

{ticker:'SAP',x2:'',x2s:'',name:'SAP',sector:'ERP cloud',cap:'large',srd:false,idx:'XETRA',
 price:199.84,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.8,news5:'',dy_n:10,dy_med:1.4,div12:2.5,pe_lo:26.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:20.9,pfcf_h:28.9,pe_h:41.1,fcur:'EUR',fcfh:'8417|4410|5461|4770',nih:'7161|3124|6139|2284',revh:'36800|34176|31207|29519',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Francfort',near:false,gsrc:'yahoo (4 ans publies)',gused:27.0,gimp:null,knife:false,neglect:false,vmeth:'per',nig:46.4,cagr:7.6,alarm:'',qwhy:'ROIC 8.4',qok:false,nde:-0.06,fcfc:123.0,roicx:28.6,chg:0.31,mkt:'285Md€',b52h:244.3,b52l:127.5,beta:0.76,
 pe:29.92,pb:5.16,ev_ebitda:19.45,ps:6.04,pfcf:28,ev_ebit:21.3,
 roe:18.3,roic:8.4,roa:9.5,debt:0.22,de:0.22,ic:21.9,cr:1.15,qr:1.5,
 yield:1.2,epsg:30.6,revg:9.4,margin:20.4,gm:73.7,om:20,fcf:3.6,
 capex:2.2,capr:2.0,capda:0.56,dcfb:107.19,dcfm:126.11,dcfu:151.33,
 pio:8,alt:7.49,rsi:66.6,mm50:186.06,mm200:163.88,
 el:95.84,eh:114.0,stop:84.34,o1:132.42,o2:151.33,cb:18,ch:5,cs:1,tp:215.71,score:'C',rec:'avoid',zone:false,
 moat:[['ERP monopole entreprises mondiales','fort'],['Switching costs insupportables','fort']],
 cats:[{t:'Cloud migration 80% revenues 2026',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Klein','15M€','Jan 2026']],
 peers:[{n:'Oracle',pe:30,pb:12,roe:55,div:1.2,evebitda:18},{n:'Salesforce',pe:28,pb:5.5,roe:12,div:0.5,evebitda:20}],
 risks:{Cloud:40,Concurrence:45,Transition:35,Devise:40,Migration:35,Liquidite:10},
 track:[{y:'2025',p:'Cloud 75% revenues',ok:'ok'},{y:'2024',p:'Cloud revenue +25%',ok:'ok'}],
 thesis:"SAP est le Microsoft de l'ERP. 440 millions d'utilisateurs ne peuvent pas changer de logiciel. La transition cloud génère de la récurrence. Éligible PEA via Xetra.",
 contra:"35x PE élevé. Transition cloud crée de la friction à court terme. Concurrence Oracle et Salesforce sur les nouveaux clients."},

{ticker:'SIEMENS',x2:'',x2s:'',name:'Siemens',sector:'Industrie digitale',cap:'large',srd:false,idx:'XETRA',
 price:266.2,roiica:false,reinv:false,roiic:32.3,vmed:null,vepv:null,chg5:-3.5,news5:'',dy_n:10,dy_med:3.36,div12:5.35,pe_lo:13.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:10.9,pfcf_h:12.8,pe_h:18.4,fcur:'EUR',fcfh:'10812|9577|10093|8157',nih:'9620|8301|7949|3723',revh:'78914|75930|74882|71977',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Francfort',near:false,gsrc:'yahoo (4 ans publies)',gused:20.2,gimp:null,knife:false,neglect:false,vmeth:'per',nig:37.2,cagr:3.1,alarm:'',qwhy:'ROIC 10.3, dette/EBITDA 2.62',qok:false,nde:2.62,fcfc:131.0,roicx:16.4,chg:-1.64,mkt:'152Md€',b52h:291.7,b52l:198.0,beta:1.29,
 pe:26.62,pb:3.02,ev_ebitda:20.4,ps:2.51,pfcf:18,ev_ebit:20.5,
 roe:12.5,roic:10.3,roa:3.8,debt:0.66,de:0.66,ic:7.6,cr:1.44,qr:1.2,
 yield:2.0,epsg:12.8,revg:7.3,margin:9.8,gm:39.4,om:13,fcf:5.3,
 capex:2.5,capr:3.1,capda:0.72,dcfb:188.97,dcfm:222.32,dcfu:266.78,
 pio:5,alt:2.52,rsi:43.1,mm50:274.55,mm200:258.41,
 el:168.96,eh:200.98,stop:148.68,o1:233.44,o2:266.78,cb:16,ch:5,cs:1,tp:305.8,score:'C',rec:'avoid',zone:false,
 moat:[['Automatisation industrielle','fort'],['Digital Industries Xcelerator','fort']],
 cats:[{t:'IA industrielle',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Busch','18M€','Jan 2026']],
 peers:[{n:'ABB',pe:25,pb:5.8,roe:22,div:2.0,evebitda:16},{n:'Schneider',pe:28,pb:6.8,roe:26,div:1.5,evebitda:18}],
 risks:{Cyclicite:45,Chine:45,Devise:40,Concurrence:40,Spinoff:30,Liquidite:10},
 track:[{y:'2025',p:'Digital Industries record',ok:'ok'}],
 thesis:"Siemens est le leader mondial de l'automatisation industrielle et du jumeau numérique. L'IA industrielle est la prochaine révolution.",
 contra:"Conglomérat complexe. Cyclicité industrie. Chine représente 15% du CA."},

{ticker:'ALV',x2:'',x2s:'',name:'Allianz',sector:'Assurance mondiale',cap:'large',srd:false,idx:'XETRA',
 price:425.9,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.3,news5:'',dy_n:10,dy_med:4.73,div12:17.1,pe_lo:11.1,gmod:null,nih:'10603|9788|8399|6302',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:6.8,roemin:11.6,roem:15.3,grid:'banque',wht:26.375,irrn:6.2,irr:7.2,dq:'',vmult:null,hn:4,eveb_h:null,pfcf_h:4.5,pe_h:12.1,fcur:'EUR',unc:'elevee',vopt:318.11,vpess:214.15,nregu:3,regn:3,regu:3,place:'Francfort',near:false,gsrc:'yahoo (4 ans publies)',gused:18.9,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:18.9,cagr:null,alarm:'',qwhy:'',qok:true,nde:null,fcfc:null,roicx:null,chg:-1.84,mkt:'142Md€',b52h:454.6,b52l:338.8,beta:0.69,
 pe:13.96,pb:2.56,ev_ebitda:3.04,ps:1.35,pfcf:999,ev_ebit:4.0,
 roe:19.6,roic:null,roa:1.2,debt:0.51,de:0.51,ic:21.4,cr:1.51,qr:999,
 yield:3.9,epsg:-8.0,revg:12.1,margin:9.9,gm:25.0,om:999,fcf:19.2,
 capex:0.8,capr:1.6,capda:1.04,dcfb:270.07,dcfm:276.52,dcfu:381.28,
 pio:6,alt:0.34,rsi:48.9,mm50:435.39,mm200:391.98,
 el:193.57,eh:221.22,stop:192.73,o1:318.11,o2:349.92,cb:16,ch:5,cs:1,tp:447.27,score:'D',rec:'hold',zone:false,
 moat:[['PIMCO asset management','fort'],['Assurance monde top 3','fort']],
 cats:[{t:'PIMCO obligations record',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Bäte','12M€','Jan 2026']],
 peers:[{n:'Axa',pe:10,pb:1.2,roe:12,div:5.8,evebitda:999},{n:'Zurich',pe:14,pb:2.8,roe:20,div:5.5,evebitda:999}],
 risks:{Catastrophes:55,Taux:45,PIMCO:40,Reglement:50,Devise:40,Liquidite:10},
 track:[{y:'2025',p:'ROE 14%',ok:'ok'},{y:'2024',p:'Dividende +8%',ok:'ok'}],
 thesis:"Allianz est le meilleur assureur mondial avec PIMCO (1600 Md$ AUM). 5.2% de dividende, 11x PE, rachat d'actions régulier. Éligible PEA via Xetra.",
 contra:"Exposition catastrophes naturelles. Réglementation Solvabilité II. Business complexe."}
// ══ SESSION 2 — SBF120 + SRD ══
,{ticker:'BIOM',x2:'',x2s:'',name:'bioMérieux',sector:'Diagnostics médicaux',cap:'mid',srd:true,idx:'SBF120',
 price:86.85,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:3.1,news5:'',dy_n:10,dy_med:0.65,div12:0.98,pe_lo:25.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:14.5,pfcf_h:49.4,pe_h:30.2,fcur:'EUR',fcfh:'453|322|107|188',nih:'398|432|358|452',revh:'4070|3980|3675|3589',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:0.0,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-4.2,cagr:4.3,alarm:'',qwhy:'ROIC hors EA 12.5, ROIC 10.3, cash 65.0%',qok:false,nde:-0.13,fcfc:65.0,roicx:12.5,chg:-0.46,mkt:'7.4Md€',b52h:116.1,b52l:65.6,beta:0.55,
 pe:22.27,pb:2.38,ev_ebitda:9.55,ps:2.57,pfcf:22,ev_ebit:18.5,
 roe:11.2,roic:10.3,roa:7.2,debt:0.1,de:0.1,ic:34.3,cr:2.3,qr:1.8,
 yield:1.1,epsg:41.9,revg:-3.9,margin:11.6,gm:56.1,om:16,fcf:4.4,
 capex:3.5,capr:8.2,capda:1.09,dcfb:62.42,dcfm:73.43,dcfu:88.12,
 pio:7,alt:5.65,rsi:76.0,mm50:76.32,mm200:80.91,
 el:51.4,eh:64.62,stop:45.23,o1:77.1,o2:88.12,cb:12,ch:6,cs:1,tp:79.9,score:'C',rec:'avoid',zone:false,
 moat:[['Leader mondial diagnostics in vitro','fort'],['Accréditations réglementaires','fort']],
 cats:[{t:'Biosécurité alimentaire en hausse',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Mérieux','18M€','Jan 2026']],
 peers:[{n:'Biomérieux',pe:28,pb:4.5,roe:16,div:1.2,evebitda:16},{n:'Bio-Techne',pe:32,pb:5.5,roe:18,div:0.8,evebitda:20}],
 risks:{Reglement:50,Concurrence:45,Devise:40,Innovation:45,Cyclicite:25,Liquidite:15},
 track:[{y:'2025',p:'CA +8% organique',ok:'ok'}],
 thesis:"bioMérieux est le leader mondial des diagnostics in vitro avec des accréditations qui rendent le switching impossible. La famille Mérieux contrôle 55% du capital — alignement parfait long terme.",
 contra:"Valorisation 28x PE premium. Concurrence Roche et Abbott massive. Croissance post-COVID se normalise."},

{ticker:'KLPI',x2:'',x2s:'',name:'Klépierre',sector:'Centres commerciaux',cap:'large',srd:true,idx:'SBF120',
 price:34.86,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.3,news5:'',dy_n:9,dy_med:6.81,div12:1.9,pe_lo:7.3,gmod:null,icr:3.6,ltv:34.2,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:0.0,irrn:7.3,irr:7.3,dq:'',vmult:null,hn:4,eveb_h:15.3,pfcf_h:10.0,pe_h:11.1,fcur:'EUR',fcfh:'819|775|742|734',nih:'1299|1098|193|415',revh:'1567|1504|1420|1429',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:36.33,vpess:26.42,nregu:null,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:3.1,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:null,cagr:3.1,alarm:'',qwhy:'',qok:true,nde:null,fcfc:null,roicx:null,chg:-2.24,mkt:'6.8Md€',b52h:40.38,b52l:30.86,beta:0.9,
 pe:7.31,pb:1.06,ev_ebitda:17.42,ps:5.71,pfcf:8,ev_ebit:10.6,
 roe:13.7,roic:null,roa:3.2,debt:0.69,de:0.69,ic:6.8,cr:0.3,qr:0.6,
 yield:5.3,epsg:11.2,revg:0.7,margin:78.1,gm:77.9,om:48,fcf:8.2,
 capex:0.8,capr:13.1,capda:9.39,dcfb:33.54,dcfm:33.03,dcfu:47.35,
 pio:6,alt:0.93,rsi:39.0,mm50:36.9,mm200:34.59,
 el:23.12,eh:26.42,stop:23.78,o1:36.33,o2:39.96,cb:7,ch:5,cs:3,tp:38.21,score:'C',rec:'hold',zone:false,
 moat:[['Centres premium Europe','modere'],['Simon Property 22%','modere']],
 cats:[{t:'Trafic record 2026',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Simon Property','25M€','Jan 2026']],
 peers:[{n:'Unibail',pe:12,pb:0.5,roe:5,div:6.8,evebitda:14},{n:'Carmila',pe:13,pb:0.8,roe:7,div:7.2,evebitda:13}],
 risks:{Taux:70,Ecommerce:60,Commerce:55,Dette:65,Valorisation:45,Liquidite:20},
 track:[{y:'2025',p:'Loyers indexés +6%',ok:'ok'}],
 thesis:"Klépierre possède les meilleurs centres commerciaux d'Europe. Loyers indexés à l'inflation. À 0.9x ANR avec 6.5% de rendement, le risque/reward devient intéressant si les taux baissent.",
 contra:"Les taux élevés continuent de peser sur la valeur des actifs immobiliers. E-commerce prend des parts structurellement."},

{ticker:'RCO',x2:'',x2s:'',name:'Rémy Cointreau',sector:'Spiritueux premium',cap:'mid',srd:true,idx:'SBF120',
 price:49.92,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:15.3,news5:'',dy_n:10,dy_med:1.83,div12:0.75,pe_lo:17.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:15.2,pfcf_h:40.3,pe_h:25.2,fcur:'EUR',fcfh:'91|70|95|124',nih:'79|121|185|294',revh:'935|985|1194|1548',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-25.5,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-35.5,cagr:-15.5,alarm:'',qwhy:'ROIC hors EA 7.0, ROIC 6.9, cash 56.0%, dette/EBITDA 3.64, croissance CA -15.5%',qok:false,nde:3.64,fcfc:56.0,roicx:7.0,chg:-3.16,mkt:'2.8Md€',b52h:51.8,b52l:34.24,beta:0.73,
 pe:33.28,pb:1.36,ev_ebitda:16.52,ps:2.82,pfcf:18,ev_ebit:23.6,
 roe:4.1,roic:6.9,roa:3.0,debt:0.4,de:0.4,ic:4.2,cr:3.15,qr:1.1,
 yield:1.4,epsg:-47.6,revg:-1.2,margin:8.4,gm:65.8,om:25,fcf:3.4,
 capex:1.8,capr:null,capda:null,dcfb:31.89,dcfm:37.52,dcfu:45.02,
 pio:5,alt:2.02,rsi:69.2,mm50:44.61,mm200:41.8,
 el:29.27,eh:34.22,stop:25.76,o1:39.4,o2:45.02,cb:8,ch:7,cs:5,tp:45.09,score:'C',rec:'avoid',zone:false,
 moat:[['Louis XIII cognac ultra-premium','fort'],['Cointreau liqueur mondiale','fort']],
 cats:[{t:'Chine ultra-premium résilience',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Cointreau','8.5M€','Jan 2026']],
 peers:[{n:'Pernod Ricard',pe:16,pb:2.2,roe:14,div:3.8,evebitda:12},{n:'Diageo',pe:16,pb:5.8,roe:35,div:3.8,evebitda:14}],
 risks:{Chine:75,US:65,Cognac:65,Devise:50,Volumes:55,Liquidite:20},
 track:[{y:'2025',p:'Volumes -15%',ok:'m'},{y:'2024',p:'Louis XIII résilient',ok:'partial'}],
 thesis:"Rémy possède Louis XIII, le cognac le plus cher au monde à 4000€/bouteille. En bas de cycle, la normalisation Chine crée du potentiel. Famille Cointreau aux commandes.",
 contra:"La pression volumes dure bien plus que prévu. 6 trimestres consécutifs de déception."},

{ticker:'EIFFAGE',x2:'',x2s:'',name:'Eiffage',sector:'Construction & Concessions',cap:'large',srd:true,idx:'CAC40',
 price:99.18,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.5,news5:'',dy_n:9,dy_med:3.42,div12:4.8,pe_lo:7.4,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.1,pfcf_h:4.1,pe_h:9.4,fcur:'EUR',fcfh:'2303|2774|2456|1929',nih:'1022|1039|1013|896',revh:'26134|24037|22389|20884',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:6.2,gimp:null,knife:false,neglect:true,vmeth:'per',nig:4.5,cagr:7.8,alarm:'',qwhy:'ROIC hors EA 13.6, ROIC 10.2',qok:false,nde:2.31,fcfc:238.0,roicx:13.6,chg:-1.75,mkt:'8.5Md€',b52h:147.5,b52l:97.36,beta:0.73,
 pe:9.03,pb:1.26,ev_ebitda:5.67,ps:0.37,pfcf:10,ev_ebit:8.1,
 roe:17.7,roic:10.2,roa:4.0,debt:1.72,de:1.72,ic:6.4,cr:0.93,qr:0.9,
 yield:4.8,epsg:9.6,revg:1.1,margin:4.0,gm:83.9,om:6,fcf:23.7,
 capex:2.5,capr:4.5,capda:0.73,dcfb:122.99,dcfm:144.7,dcfu:173.64,
 pio:7,alt:1.05,rsi:35.2,mm50:108.19,mm200:122.44,
 el:121.55,eh:135.44,stop:106.96,o1:151.94,o2:173.64,cb:10,ch:5,cs:2,tp:156.35,score:'C',rec:'avoid',zone:false,
 moat:[['Autoroute APRR','fort'],['Construction intégrée','modere']],
 cats:[{t:'Infrastructure EU plan',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Dupont','5.2M€','Jan 2026']],
 peers:[{n:'Vinci',pe:15,pb:3.5,roe:24,div:3.5,evebitda:10},{n:'Bouygues',pe:10,pb:1.1,roe:11,div:5.2,evebitda:5}],
 risks:{Construction:55,Taux:50,Politique:40,Reglement:35,Cyclicite:45,Liquidite:15},
 track:[{y:'2025',p:'Marge concessions stable',ok:'ok'}],
 thesis:"Eiffage est le deuxième groupe de BTP français avec APRR (autoroutes) comme rente permanente. À 13x PE avec 3.8% de dividende, bien moins cher que Vinci.",
 contra:"Moins diversifié que Vinci. Exposition construction cyclique plus forte. APRR = actif réglementé."},

{ticker:'ALTAREA',x2:'',x2s:'',name:'Altarea',sector:'Immobilier mixte',cap:'mid',srd:true,idx:'SBF120',
 price:74.8,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:3.6,news5:'',dy_n:10,dy_med:6.46,div12:8.0,pe_lo:null,gmod:null,icr:2.4,ltv:27.6,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 49.9 contre 8.1 attendu)',vmult:null,hn:3,eveb_h:19.0,pfcf_h:9.5,pe_h:7.8,fcur:'EUR',fcfh:'26|400|318|187',nih:'8|6|-473|327',revh:'2019|2710|2650|2959',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:null,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-12.0,gimp:null,knife:true,neglect:true,vmeth:'per',nig:null,cagr:-12.0,alarm:'',qwhy:'couverture des interets 2.4, loyers en baisse -12.0%, perte exploitation',qok:false,nde:null,fcfc:null,roicx:null,chg:-2.86,mkt:'1.5Md€',b52h:131.4,b52l:72.0,beta:0.81,
 pe:49.87,pb:1.16,ev_ebitda:28.72,ps:0.96,pfcf:8,ev_ebit:41.4,
 roe:3.5,roic:null,roa:1.5,debt:0.93,de:0.93,ic:1.8,cr:1.06,qr:0.7,
 yield:10.4,epsg:267.6,revg:-9.3,margin:1.9,gm:25.9,om:10,fcf:1.4,
 capex:0.8,capr:5.4,capda:3.22,dcfb:121.38,dcfm:142.8,dcfu:171.36,
 pio:6,alt:0.6,rsi:33.3,mm50:86.76,mm200:99.16,
 el:114.24,eh:131.38,stop:100.53,o1:149.94,o2:171.36,cb:6,ch:5,cs:3,tp:110,score:'C',rec:'avoid',zone:false,
 moat:[['Foncière mixte commerce/bureau','modere'],['Cogedim promo résidentiel','modere']],
 cats:[{t:'Baisse taux immobilier',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Naouri','12M€','Jan 2026']],
 peers:[{n:'Unibail',pe:12,pb:0.5,roe:5,div:6.8,evebitda:14},{n:'Carmila',pe:13,pb:0.8,roe:7,div:7.2,evebitda:13}],
 risks:{Taux:80,Immobilier:75,Dette:80,Promo:65,Liquidite:35,Concentration:50},
 track:[{y:'2025',p:'Dividende maintenu',ok:'ok'}],
 thesis:"Altarea à 10.2% de dividende — l'un des plus élevés de la cote. Si les taux baissent en 2026, la foncière rebondit fortement depuis les niveaux déprimés.",
 contra:"Dette massive (8.5x EBITDA). Promotion immobilière neuve en crise. Les taux élevés continuent de peser."},

{ticker:'COVIVIO',x2:'',x2s:'',name:'Covivio',sector:'Immobilier hôtelier',cap:'mid',srd:true,idx:'SBF120',
 price:43.18,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.3,news5:'',dy_n:10,dy_med:5.78,div12:3.75,pe_lo:8.4,gmod:null,icr:3.2,ltv:38.4,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:0.0,irrn:10.5,irr:10.5,dq:'',vmult:null,hn:3,eveb_h:11.6,pfcf_h:20.0,pe_h:8.4,fcur:'EUR',fcfh:'240|385|541|130',nih:'739|68|-1419|621',revh:'1396|1276|1226|906',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:84.03,vpess:61.12,nregu:null,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:15.5,gimp:null,knife:false,neglect:true,vmeth:'pb',nig:null,cagr:15.5,alarm:'',qwhy:'',qok:true,nde:null,fcfc:null,roicx:null,chg:-2.57,mkt:'3.8Md€',b52h:62.8,b52l:42.36,beta:1.12,
 pe:7.34,pb:0.57,ev_ebitda:19.02,ps:4.08,pfcf:7,ev_ebit:15.4,
 roe:8.5,roic:null,roa:2.1,debt:0.83,de:0.83,ic:4.7,cr:0.57,qr:0.6,
 yield:8.5,epsg:-25.0,revg:4.5,margin:55.9,gm:83.4,om:25,fcf:5.0,
 capex:1.2,capr:41.5,capda:4.03,dcfb:52.01,dcfm:76.39,dcfu:73.43,
 pio:7,alt:0.47,rsi:33.5,mm50:47.64,mm200:51.14,
 el:53.48,eh:61.12,stop:55.0,o1:84.03,o2:92.44,cb:6,ch:5,cs:3,tp:58.18,score:'B',rec:'watch',zone:true,
 moat:[['Hôtels prime Europe','modere'],['Bureaux Milan/Paris','modere']],
 cats:[{t:'Tourisme d\'affaires rebond',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction','3.5M€','Jan 2026']],
 peers:[{n:'Unibail',pe:12,pb:0.5,roe:5,div:6.8,evebitda:14}],
 risks:{Taux:70,Hôtellerie:55,Dette:70,Vacance:45,Geopol:40,Liquidite:25},
 track:[{y:'2025',p:'ANR stabilisé',ok:'partial'}],
 thesis:"Covivio possède des hôtels Accor en Europe avec des baux long terme indexés. 6.2% de dividende. Le rebond du tourisme d'affaires post-COVID est permanent.",
 contra:"Dette très élevée. Taux pèsent lourdement. Secteur immobilier sous pression."},

{ticker:'FREY',x2:'',x2s:'',name:'Frey',sector:'Retail parks',cap:'small',srd:false,idx:'SBF120',
 price:34.2,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-1.2,news5:'',dy_n:10,dy_med:4.74,div12:2.0,pe_lo:7.5,gmod:null,icr:1.9,ltv:37.3,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:13.6,pfcf_h:14.8,pe_h:17.6,fcur:'EUR',fcfh:'100|61|58|54',nih:'77|40|19|129',revh:'231|191|149|124',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:null,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:23.1,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:23.1,alarm:'',qwhy:'couverture des interets 1.9',qok:false,nde:null,fcfc:null,roicx:null,chg:0.0,mkt:'0.58Md€',b52h:36.6,b52l:28.2,beta:0.04,
 pe:8.88,pb:1.04,ev_ebitda:15.88,ps:3.9,pfcf:7,ev_ebit:14.1,
 roe:11.3,roic:null,roa:3.0,debt:1.5,de:1.5,ic:2.7,cr:1.92,qr:0.7,
 yield:5.8,epsg:355.9,revg:45.8,margin:44.2,gm:64.2,om:32,fcf:9.3,
 capex:0.8,capr:2.6,capda:1.6,dcfb:21.32,dcfm:25.08,dcfu:30.1,
 pio:5,alt:0.61,rsi:31.7,mm50:34.98,mm200:32.49,
 el:20.06,eh:23.07,stop:17.65,o1:26.33,o2:30.1,cb:5,ch:4,cs:2,tp:32,score:'D',rec:'avoid',zone:false,
 moat:[['Retail parks anticrises','fort'],['Alimentation essentielle','fort']],
 cats:[{t:'Alimentation discount boom',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Frey','4.2M€','Jan 2026']],
 peers:[{n:'Mercialys',pe:12,pb:1.0,roe:10,div:8.5,evebitda:11}],
 risks:{Taux:60,Commerce:45,Lidl:50,Reglement:35,Dette:55,Liquidite:40},
 track:[{y:'2025',p:'Ouvertures 3 parcs',ok:'ok'}],
 thesis:"Frey développe des retail parks discount (alimentation, bricolage) qui résistent aux crises économiques car l'alimentation est incompressible. Famille aux commandes.",
 contra:"Dette moderee dans un contexte de taux élevés. Marché peu liquide."},

{ticker:'CHSR',x2:'',x2s:'',name:'Belgrano (ex-Chargeurs)',sector:'Industrie diversifiée',cap:'small',srd:false,idx:'SBF120',
 price:7.2,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-2.7,news5:'',dy_n:9,dy_med:3.26,div12:1.5,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:12.2,pfcf_h:8.8,pe_h:24.5,fcur:'EUR',fcfh:'-10|28|-44|-18',nih:'-24|7|-1|22',revh:'420|432|652|734',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-17.0,gimp:null,knife:true,neglect:false,vmeth:'per',nig:null,cagr:-17.0,alarm:'',qwhy:'ROIC hors EA 3.4, ROIC 2.2, cash -938.0%, dette/EBITDA 13.08, croissance CA -17.0%',qok:false,nde:13.08,fcfc:-938.0,roicx:3.4,chg:-0.83,mkt:'0.32Md€',b52h:11.1,b52l:7.11,beta:1.57,
 pe:112.54,pb:0.61,ev_ebitda:36.68,ps:0.45,pfcf:7,ev_ebit:null,
 roe:-12.6,roic:2.2,roa:-0.0,debt:1.52,de:1.52,ic:-0.1,cr:1.61,qr:1.0,
 yield:1.6,epsg:6,revg:-14.1,margin:2.1,gm:30.5,om:7,fcf:-5.7,
 capex:1.2,capr:7.5,capda:1.13,dcfb:2.45,dcfm:2.88,dcfu:3.46,
 pio:5,alt:0.83,rsi:34.5,mm50:8.16,mm200:7.83,
 el:2.39,eh:2.68,stop:2.1,o1:3.02,o2:3.46,cb:4,ch:4,cs:2,tp:11.33,score:'D',rec:'avoid',zone:false,
 moat:[['Films techniques protection','fort'],['Musées & patrimoine','modere']],
 cats:[{t:'PCC (Personal Care) croissance',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Fribourg','2.8M€','Jan 2026']],
 peers:[{n:'Archroma',pe:12,pb:1.5,roe:12,div:2.5,evebitda:7}],
 risks:{Cyclicite:55,Devise:50,Matières:45,Concurrence:45,Taille:50,Liquidite:45},
 track:[{y:'2025',p:'Restructuration en cours',ok:'partial'}],
 thesis:"Chargeurs est un conglomérat industriel injustement décoté. Ses films de protection sont utilisés partout (iPhone, voitures). La division musées est un actif premium caché.",
 contra:"Conglomérat = décote structurelle. Restructuration longue. Taille trop petite pour les institutionnels."},

{ticker:'VALO',x2:'',x2s:'',name:'Valeo',sector:'Équipementier auto',cap:'large',srd:true,idx:'CAC40',
 price:13.54,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.3,news5:'',dy_n:10,dy_med:2.13,div12:0.44,pe_lo:13.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:2.6,pfcf_h:6.5,pe_h:15.1,fcur:'EUR',fcfh:'528|463|461|419',nih:'200|162|221|230',revh:'20903|21492|22044|20037',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-1.6,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-4.6,cagr:1.4,alarm:'',qwhy:'ROIC hors EA 11.2, ROIC 6.7, croissance CA 1.4%',qok:false,nde:1.4,fcfc:230.0,roicx:11.2,chg:-2.94,mkt:'2.8Md€',b52h:17.32,b52l:9.44,beta:1.3,
 pe:16.51,pb:0.96,ev_ebitda:3.65,ps:0.16,pfcf:6,ev_ebit:9.8,
 roe:6.6,roic:6.7,roa:3.7,debt:1.65,de:1.65,ic:2.3,cr:0.87,qr:0.8,
 yield:3.1,epsg:1.2,revg:-2.6,margin:1.0,gm:20.8,om:3,fcf:16.1,
 capex:3.5,capr:8.4,capda:0.84,dcfb:12.39,dcfm:14.58,dcfu:17.5,
 pio:8,alt:1.35,rsi:42.3,mm50:14.34,mm200:12.71,
 el:11.66,eh:13.41,stop:10.26,o1:15.31,o2:17.5,cb:5,ch:6,cs:6,tp:14.54,score:'D',rec:'avoid',zone:false,
 moat:[['Éclairage LED auto','modere'],['ADAS systèmes','modere']],
 cats:[{t:'ADAS régulation EU',w:'2026',c:'var(--gn)'}],
 ins:[],
 peers:[{n:'Faurecia',pe:6,pb:0.4,roe:4,div:0.0,evebitda:3},{n:'Plastic Omnium',pe:7,pb:0.6,roe:8,div:3.5,evebitda:4}],
 risks:{VE:80,Dette:80,Auto:75,Cyclicite:75,Clients:65,Liquidite:30},
 track:[{y:'2025',p:'Profit warning',ok:'m'},{y:'2024',p:'Dette réduite partiellement',ok:'partial'}],
 thesis:"Valeo est un pari spéculatif sur la survie. À 0.5x livre avec ADAS qui croît, si l'auto rebondit en 2026, le potentiel est 100%+.",
 contra:"Dette écrasante. VE ralentit et Valeo a parié dessus massivement. Les constructeurs pressent les marges des équipementiers. À éviter sauf spéculatif."},

{ticker:'FORVIA',x2:'',x2s:'',name:'Forvia (Faurecia)',sector:'Équipementier auto',cap:'large',srd:true,idx:'CAC40',
 price:8.97,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:5.0,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:5.2,pfcf_h:4.8,pe_h:18.1,fcur:'EUR',fcfh:'1220|966|431|373',nih:'-2091|-185|222|-382',revh:'21347|21879|27248|24574',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-4.6,gimp:null,knife:true,neglect:false,vmeth:'per',nig:null,cagr:-4.6,alarm:'',qwhy:'ROIC hors EA 1.3, ROIC 0.7, cash None%, dette/EBITDA 6.64, croissance CA -4.6%',qok:false,nde:6.64,fcfc:null,roicx:1.3,chg:-0.49,mkt:'2.2Md€',b52h:15.03,b52l:8.38,beta:1.66,
 pe:3.89,pb:0.87,ev_ebitda:4.46,ps:0.08,pfcf:5,ev_ebit:null,
 roe:-25.7,roic:0.7,roa:2.5,debt:2.55,de:2.55,ic:-13.6,cr:0.95,qr:0.7,
 yield:0.0,epsg:12,revg:-4.3,margin:-8.7,gm:15.0,om:3,fcf:73.8,
 capex:2.5,capr:6.2,capda:0.81,dcfb:16.77,dcfm:19.73,dcfu:23.68,
 pio:7,alt:0.79,rsi:50.4,mm50:9.08,mm200:10.44,
 el:15.78,eh:18.15,stop:13.89,o1:20.72,o2:23.68,cb:4,ch:5,cs:7,tp:14.57,score:'C',rec:'avoid',zone:false,
 moat:[['Sièges auto leader mondial','modere'],['Clarion intégration','faible']],
 cats:[{t:'Désendettement plan 2026',w:'2026',c:'var(--gn)'}],
 ins:[],
 peers:[{n:'Valeo',pe:8,pb:0.5,roe:6,div:0.0,evebitda:4},{n:'Plastic Omnium',pe:7,pb:0.6,roe:8,div:3.5,evebitda:4}],
 risks:{Dette:90,Auto:80,Cyclicite:80,VE:70,Clients:70,Liquidite:35},
 track:[{y:'2025',p:'Désendettement partiel',ok:'partial'},{y:'2024',p:'Hella intégration difficile',ok:'m'}],
 thesis:"Forvia a failli faire défaut en 2023 et s'en sort. À 0.4x livre, la restructuration crée un potential de rebond si l'auto reprend.",
 contra:"Dette insoutenable post-acquisition Hella. Marges quasi-nulles. Auto en crise. À éviter sauf spéculatif."},

{ticker:'PLUXEE',x2:'',x2s:'',name:'Pluxee',sector:'Avantages salariaux',cap:'mid',srd:true,idx:'SBF120',
 price:15.3,roiica:false,reinv:false,roiic:152.4,vmed:null,vepv:null,chg5:4.3,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,fcfh:'410|322|443|143',nih:'197|133|81|174',revh:'1287|1210|1052|842',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:6.2,pfcf_h:7.9,pe_h:18.2,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'communique 2026-10-12',gused:0.0,gimp:null,knife:false,neglect:false,vmeth:'per',nig:4.2,cagr:15.2,alarm:'',qwhy:'croissance officielle 0.0%',qok:false,nde:-0.45,fcfc:225.0,roicx:23.7,chg:-0.58,mkt:'3.2Md€',b52h:17.93,b52l:9.9,beta:0.77,
 pe:10.85,pb:5.48,ev_ebitda:2.14,ps:1.61,pfcf:14,ev_ebit:2.7,
 roe:50.7,roic:165.2,roa:3.5,debt:2.64,de:2.64,ic:7.6,cr:1.04,qr:1.0,
 yield:2.5,epsg:11.0,revg:3.2,margin:15.7,gm:37.4,om:20,fcf:19.5,
 capex:0.8,capr:7.6,capda:0.9,dcfb:11.5,dcfm:13.53,dcfu:16.24,
 pio:6,alt:0.64,rsi:60.0,mm50:15.03,mm200:12.6,
 el:10.82,eh:12.45,stop:9.52,o1:14.21,o2:16.24,cb:10,ch:5,cs:2,tp:15.88,score:'C',rec:'avoid',zone:false,
 moat:[['Tickets restaurant leader','fort'],['Float financier avantageux','fort']],
 cats:[{t:'Expansion Brésil/Mexique',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Studer','2.8M€','Jan 2026']],
 peers:[{n:'Edenred',pe:22,pb:6.5,roe:30,div:2.5,evebitda:15},{n:'Sodexo Benefits',pe:20,pb:5.5,roe:25,div:2.2,evebitda:13}],
 risks:{Reglement:55,Taux:50,Concurrence:45,Devise:45,Float:40,Liquidite:20},
 track:[{y:'2025',p:'Spin-off Sodexo réussi',ok:'ok'}],
 thesis:"Pluxee (spin-off Sodexo) est le challenger d'Edenred sur les avantages salariaux. Float financier = revenus d'intérêts massifs en période de taux élevés. 25% de ROE.",
 contra:"Edenred domine avec 30 ans d'avance. Réglementation peut réduire le float. La valorisation intègre déjà beaucoup."},

{ticker:'EDENRED',x2:'',x2s:'',name:'Edenred',sector:'Avantages salariaux',cap:'large',srd:true,idx:'CAC40',
 price:29.99,roiica:false,reinv:false,roiic:20.8,vmed:null,vepv:null,chg5:6.0,news5:'',dy_n:10,dy_med:1.96,div12:1.33,pe_lo:8.5,gmod:null,fcfh:'1072|812|862|862',nih:'521|507|267|386',revh:'2961|2856|2514|2031',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:12.4,pfcf_h:11.9,pe_h:23.7,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:11.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:10.5,cagr:13.4,alarm:'',qwhy:'ROIC hors EA None',qok:false,nde:2.2,fcfc:215.0,roicx:null,chg:-0.2,mkt:'13.5Md€',b52h:30.85,b52l:15.23,beta:0.69,
 pe:14.56,pb:-7.04,ev_ebitda:8.23,ps:2.49,pfcf:18,ev_ebit:9.2,
 roe:30,roic:33.6,roa:3.7,debt:1.2,de:null,ic:null,cr:0.84,qr:1.0,
 yield:4.4,epsg:-6.3,revg:1.5,margin:18.2,gm:42.1,om:24,fcf:15.7,
 capex:0.8,capr:6.7,capda:0.69,dcfb:18.74,dcfm:22.05,dcfu:26.46,
 pio:8,alt:0.43,rsi:63.6,mm50:28.71,mm200:22.26,
 el:17.64,eh:20.29,stop:15.52,o1:23.15,o2:26.46,cb:14,ch:5,cs:2,tp:31.21,score:'D',rec:'avoid',zone:false,
 moat:[['Ticket restaurant 30 pays','fort'],['Float financier massif','fort'],['Network effects','fort']],
 cats:[{t:'Brésil croissance 15%/an',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Kayanakis','4.5M€','Jan 2026']],
 peers:[{n:'Pluxee',pe:18,pb:4.5,roe:25,div:2.5,evebitda:12},{n:'Sodexo Benefits',pe:20,pb:5.5,roe:25,div:2.2,evebitda:13}],
 risks:{Reglement:55,Taux:50,Pluxee:40,Devise:45,Float:35,Liquidite:15},
 track:[{y:'2025',p:'Brésil +15%',ok:'ok'},{y:'2024',p:'Float revenus record',ok:'ok'}],
 thesis:"Edenred est le leader mondial des avantages salariaux avec un float de 3Md€ générant des intérêts massifs. Le Brésil (40% des profits) croît à 15%/an.",
 contra:"Correction de -25% depuis 45€. Réglementation peut contraindre le float. Pluxee attaque avec agressivité."},

{ticker:'OPM',x2:'',x2s:'',name:'OPmobility (ex-Plastic Omnium)',sector:'Emballage verre',cap:'mid',srd:true,idx:'SBF120',
 price:9.56,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.7,news5:'',dy_n:10,dy_med:2.19,div12:0.49,pe_lo:8.4,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:4.7,pfcf_h:12.1,pe_h:11.1,fcur:'EUR',fcfh:'||143|',nih:'185|170|163|168',revh:'10216|10484|10314|8538',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:4.8,gimp:null,knife:true,neglect:true,vmeth:'per',nig:3.3,cagr:6.2,alarm:'',qwhy:'ROIC hors EA 7.7, ROIC 5.0',qok:false,nde:1.94,fcfc:88.0,roicx:7.7,chg:-1.85,mkt:'2.8Md€',b52h:18.16,b52l:9.34,beta:1.18,
 pe:6.93,pb:0.62,ev_ebitda:4.56,ps:0.14,pfcf:7,ev_ebit:10.1,
 roe:9.3,roic:5.0,roa:3.2,debt:1.01,de:1.01,ic:16.6,cr:0.82,qr:0.9,
 yield:5.0,epsg:12.7,revg:-2.4,margin:2.0,gm:11.6,om:10,fcf:null,
 capex:2.5,capr:4.9,capda:1.0,dcfb:12.51,dcfm:14.72,dcfu:17.66,
 pio:7,alt:1.53,rsi:30.1,mm50:11.86,mm200:14.12,
 el:12.36,eh:13.78,stop:10.88,o1:15.46,o2:17.66,cb:7,ch:5,cs:3,tp:14.89,score:'C',rec:'avoid',zone:false,
 moat:[['Verallia n°3 mondial verre','modere'],['Contrats pluriannuels bière/vin','modere']],
 cats:[{t:'Rebond demande vins/spiritueux',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction','2.5M€','Jan 2026']],
 peers:[{n:'Owens-Illinois',pe:9,pb:1.2,roe:15,div:0.0,evebitda:5},{n:'Ardagh',pe:10,pb:0.8,roe:10,div:2.5,evebitda:5}],
 risks:{Verre:55,Energie:65,Dette:55,Cyclicite:50,Plastique:45,Liquidite:25},
 track:[{y:'2025',p:'Énergie normalisée',ok:'partial'}],
 thesis:"Verallia est le n°3 mondial du verre d'emballage avec des positions sur le vin, la bière et les spiritueux. À 8x PE avec 5.8% de dividende, la correction est excessive.",
 contra:"Forte intensité énergétique. Transition vers les canettes en aluminium. Dette moderee."},

{ticker:'IMERYS',x2:'',x2s:'',name:'Imerys',sector:'Minéraux industriels',cap:'mid',srd:true,idx:'SBF120',
 price:22.2,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.8,news5:'',dy_n:10,dy_med:4.37,div12:0.75,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:7.3,pfcf_h:19.2,pe_h:29.9,fcur:'EUR',fcfh:'112|114|221|46',nih:'-409|-95|51|237',revh:'3384|3605|3794|4282',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-7.5,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:-7.5,alarm:'',qwhy:'ROIC hors EA 1.6, ROIC 1.0, cash None%, dette/EBITDA 3.27, croissance CA -7.5%',qok:false,nde:3.27,fcfc:null,roicx:1.6,chg:-0.98,mkt:'2.2Md€',b52h:28.54,b52l:19.68,beta:0.77,
 pe:15.21,pb:0.71,ev_ebitda:8.34,ps:0.56,pfcf:9,ev_ebit:null,
 roe:-15.0,roic:1.0,roa:2.0,debt:0.88,de:0.88,ic:-4.8,cr:1.69,qr:1.1,
 yield:3.4,epsg:1.2,revg:2.2,margin:-12.8,gm:64.9,om:8,fcf:5.9,
 capex:2.5,capr:9.4,capda:0.37,dcfb:18.68,dcfm:21.98,dcfu:26.38,
 pio:6,alt:0.94,rsi:44.3,mm50:23.2,mm200:22.66,
 el:18.24,eh:20.49,stop:16.05,o1:23.08,o2:26.38,cb:7,ch:5,cs:2,tp:25.65,score:'D',rec:'avoid',zone:false,
 moat:[['Minéraux rares industriels','fort']],cats:[{t:'Matériaux batteries',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Branche','5.2M€','Jan 2026']],
 peers:[{n:'Solvay',pe:14,pb:1.2,roe:10,div:3.5,evebitda:8}],
 risks:{Cyclicite:60,Energie:55,Devise:45,Matières:50,Reglementation:40,Liquidite:20},
 track:[{y:'2025',p:'Batteries +10%',ok:'ok'}],
 thesis:"Imerys possède des gisements de kaolin, talc et minéraux industriels irremplaçables. Les minéraux pour batteries sont une option sur la transition énergétique.",
 contra:"Très cyclique. Intensité énergétique élevée."},

{ticker:'THERMADOR',x2:'',x2s:'',name:'Thermador',sector:'Distribution eau',cap:'small',srd:false,idx:'SRD',
 price:61.4,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-7.4,news5:'',dy_n:10,dy_med:2.95,div12:2.1,pe_lo:13.3,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:9.0,pfcf_h:13.8,pe_h:14.0,fcur:'EUR',fcfh:'64|65|48|14',nih:'44|45|58|59',revh:'502|504|581|554',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-6.2,gimp:null,knife:false,neglect:true,vmeth:'per',nig:-9.2,cagr:-3.2,alarm:'',qwhy:'croissance CA -3.2%',qok:false,nde:-0.62,fcfc:93.0,roicx:18.6,chg:-2.85,mkt:'0.35Md€',b52h:81.9,b52l:60.9,beta:0.8,
 pe:12.38,pb:1.36,ev_ebitda:7.12,ps:1.06,pfcf:9,ev_ebit:8.6,
 roe:12.0,roic:14.5,roa:7.0,debt:0.13,de:0.13,ic:40.8,cr:2.9,qr:2.0,
 yield:3.3,epsg:17.8,revg:11.3,margin:9.0,gm:37.4,om:9,fcf:11.3,
 capex:0.8,capr:1.1,capda:0.49,dcfb:56.81,dcfm:66.84,dcfu:80.21,
 pio:6,alt:3.87,rsi:23.9,mm50:71.5,mm200:72.55,
 el:55.48,eh:62.29,stop:48.82,o1:70.18,o2:80.21,cb:4,ch:3,cs:1,tp:89.33,score:'C',rec:'avoid',zone:false,
 moat:[['Distribution robinetterie leader France','fort']],cats:[{t:'Rénovation thermique EU',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Conil','4.5M€','Jan 2026']],
 peers:[{n:'Rexel',pe:11,pb:2.0,roe:18,div:3.8,evebitda:7}],
 risks:{Batiment:55,Cyclicite:50,Concurrence:40,Liquidite:50,Taille:55,Energie:35},
 track:[{y:'2025',p:'ROE 18%',ok:'ok'}],
 thesis:"Thermador est leader de la distribution robinetterie/eau en France avec zéro dette et 18% de ROE. Pépite méconnue, famille aux commandes.",
 contra:"Très peu liquide. Bâtiment cyclique."},

{ticker:'STEF',x2:'',x2s:'',name:'STEF',sector:'Logistique frigorifique',cap:'small',srd:false,idx:'SRD',
 price:120.4,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.2,news5:'',dy_n:10,dy_med:2.85,div12:2.7,pe_lo:7.4,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.9,pfcf_h:38.8,pe_h:9.0,fcur:'EUR',fcfh:'-2|42|21|39',nih:'84|157|192|146',revh:'5119|4801|4442|4160',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-4.8,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-16.8,cagr:7.2,alarm:'',qwhy:'ROIC hors EA 8.6, ROIC 7.4, cash 17.0%, dette/EBITDA 3.46',qok:false,nde:3.46,fcfc:17.0,roicx:8.6,chg:-0.5,mkt:'0.68Md€',b52h:138.4,b52l:113.6,beta:0.76,
 pe:12.29,pb:1.14,ev_ebitda:7.82,ps:0.29,pfcf:8,ev_ebit:17.9,
 roe:9.6,roic:7.4,roa:3.2,debt:1.29,de:1.29,ic:4.1,cr:0.72,qr:1.1,
 yield:2.2,epsg:252.0,revg:8.6,margin:2.3,gm:10.8,om:5,fcf:-0.1,
 capex:2.5,capr:6.0,capda:1.15,dcfb:109.28,dcfm:128.56,dcfu:154.27,
 pio:5,alt:1.52,rsi:41.3,mm50:125.6,mm200:121.63,
 el:105.42,eh:119.3,stop:92.77,o1:134.99,o2:154.27,cb:5,ch:4,cs:1,tp:149.0,score:'D',rec:'avoid',zone:false,
 moat:[['Logistique froid leader Europe','fort'],['Réseau 100 pays','fort']],
 cats:[{t:'Ecommerce alimentaire boom',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille STEF','5.8M€','Jan 2026']],
 peers:[{n:'ID Logistics',pe:14,pb:2.5,roe:18,div:1.5,evebitda:8}],
 risks:{Energie:55,Alimentaire:40,Reglementation:35,Cyclicite:35,Liquidite:45,Concurrence:40},
 track:[{y:'2025',p:'Marge 5%',ok:'ok'}],
 thesis:"STEF est le leader européen de la logistique frigorifique. L'alimentation réfrigérée est incompressible. Zéro dette relative, ROE 16%.",
 contra:"Très peu liquide. Énergie = 20% des coûts. Marges très fines."},

{ticker:'TRIGANO',x2:'',x2s:'',name:'Trigano',sector:'Camping-cars',cap:'mid',srd:true,idx:'SBF120',
 price:128.4,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.6,news5:'',dy_n:10,dy_med:2.21,div12:4.5,pe_lo:5.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:4.2,pfcf_h:17.1,pe_h:6.9,fcur:'EUR',fcfh:'521|-20|144|93',nih:'239|374|308|278',revh:'3660|3926|3480|3177',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-0.1,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-4.9,cagr:4.8,alarm:'Piotroski 4/9',qwhy:'cash 62.0%',qok:false,nde:-0.7,fcfc:62.0,roicx:27.1,chg:-0.39,mkt:'2.2Md€',b52h:178.8,b52l:123.7,beta:1.1,
 pe:9.71,pb:1.15,ev_ebitda:5.57,ps:0.65,pfcf:7,ev_ebit:6.5,
 roe:12.3,roic:21.0,roa:6.3,debt:0.09,de:0.09,ic:52.1,cr:2.0,qr:1.5,
 yield:3.5,epsg:14.8,revg:6.2,margin:6.8,gm:32.8,om:9,fcf:21.3,
 capex:1.8,capr:null,capda:null,dcfb:134.61,dcfm:158.37,dcfu:190.04,
 pio:4,alt:3.25,rsi:41.5,mm50:140.06,mm200:148.66,
 el:129.86,eh:146.97,stop:114.28,o1:166.29,o2:190.04,cb:8,ch:5,cs:3,tp:179.88,score:'C',rec:'avoid',zone:false,
 moat:[['Leader européen camping-cars','fort'],['Intégration verticale','modere']],
 cats:[{t:'Camping-car boom structurel',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Feuillet','8.5M€','Jan 2026']],
 peers:[{n:'Thor Industries',pe:10,pb:2.2,roe:18,div:1.8,evebitda:6}],
 risks:{Cyclicite:65,Matières:55,Energie:50,Concurrence:40,Liquidite:25,Consommation:55},
 track:[{y:'2025',p:'Normalisation post-COVID',ok:'partial'}],
 thesis:"Trigano est le leader européen du camping-car avec 22% de ROE et zéro dette. Le taux d'équipement européen rattrape le niveau américain.",
 contra:"Cyclicité forte. Normalisation post-COVID. Sensibilité macro élevée."},

{ticker:'VIRBAC',x2:'',x2s:'',name:'Virbac',sector:'Pharmacie vétérinaire',cap:'mid',srd:true,idx:'SBF120',
 price:337.0,roiica:true,reinv:false,roiic:6.1,vmed:null,vepv:null,chg5:6.3,news5:'',dy_n:5,dy_med:0.39,div12:1.45,pe_lo:15.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:10.6,pfcf_h:36.5,pe_h:19.0,fcur:'EUR',fcfh:'97|124|59|45',nih:'151|145|121|122',revh:'1465|1397|1247|1216',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:6.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:7.4,cagr:6.4,alarm:'',qwhy:'cash 60.0%',qok:false,nde:0.58,fcfc:60.0,roicx:17.7,chg:0.0,mkt:'1.8Md€',b52h:389.5,b52l:297.0,beta:0.79,
 pe:18.14,pb:2.32,ev_ebitda:10.32,ps:1.89,pfcf:16,ev_ebit:13.3,
 roe:13.6,roic:13.9,roa:7.6,debt:0.3,de:0.3,ic:25.6,cr:1.77,qr:1.6,
 yield:0.4,epsg:5.9,revg:4.0,margin:10.4,gm:67.2,om:14,fcf:3.4,
 capex:2.5,capr:7.0,capda:1.69,dcfb:469.63,dcfm:552.51,dcfu:663.01,
 pio:7,alt:3.59,rsi:70.8,mm50:319.55,mm200:342.01,
 el:386.76,eh:486.21,stop:340.35,o1:580.14,o2:663.01,cb:8,ch:5,cs:2,tp:412.75,score:'C',rec:'avoid',zone:false,
 moat:[['Santé animale mondiale n°5','fort'],['Famille aux commandes','fort']],
 cats:[{t:'Humanisation animaux compagnie',w:'Long terme',c:'var(--gn)'}],
 ins:[['Achat','Famille Dick','8.5M€','Jan 2026']],
 peers:[{n:'Zoetis',pe:28,pb:10,roe:45,div:0.8,evebitda:20}],
 risks:{Concurrence:50,Reglementation:45,Devise:40,Innovation:45,Taille:40,Liquidite:20},
 track:[{y:'2025',p:'Croissance +8%',ok:'ok'}],
 thesis:"Virbac est le n°5 mondial de la santé animale. Famille Dick aux commandes. Humanisation animaux = mégatendance +10%/an dépenses santé animale.",
 contra:"22x PE exigeant. Concurrence Zoetis/Boehringer. R&D limitée."},

{ticker:'INTERPARFUMS',x2:'',x2s:'',name:'Interparfums',sector:'Parfums sous licence',cap:'mid',srd:true,idx:'SBF120',
 price:32.3,roiica:false,reinv:true,roiic:43.2,vmed:27.72,vepv:16.46,chg5:5.2,news5:'',dy_n:9,dy_med:1.67,div12:1.0,pe_lo:16.6,gmod:8.4,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:7.7,irr:7.7,dq:'',vmult:31.59,hn:4,eveb_h:16.4,pfcf_h:34.6,pe_h:26.3,fcur:'EUR',fcfh:'109|87|31|1',nih:'127|130|119|100',revh:'899|880|798|707',yrs:'2025|2024|2023|2022',unc:'non evaluee',vopt:30.68,vpess:20.92,nregu:2,regn:3,regu:3,place:'Paris',near:true,gsrc:'yahoo (4 ans publies)',gused:8.4,gimp:12.9,knife:false,neglect:false,vmeth:'qarp',nig:8.3,cagr:8.4,alarm:'',qwhy:'cash 48.0% mais reinvesti a 43.2% (regle reinvestissement)',qok:false,nde:-0.24,fcfc:48.0,roicx:30.5,chg:-0.49,mkt:'1.5Md€',b52h:32.6,b52l:20.74,beta:1.03,
 pe:24.29,pb:4.0,ev_ebitda:18.72,ps:3.27,pfcf:14,ev_ebit:16.7,
 roe:17.1,roic:19.3,roa:10.1,debt:0.18,de:0.18,ic:29.6,cr:3.15,qr:2.8,
 yield:3.1,epsg:-10.6,revg:-7.3,margin:13.7,gm:65.8,om:18,fcf:3.9,
 capex:0.8,capr:4.5,capda:1.32,dcfb:23.56,dcfm:27.72,dcfu:33.26,
 pio:6,alt:7.37,rsi:70.8,mm50:28.69,mm200:24.43,
 el:20.79,eh:23.56,stop:18.83,o1:30.68,o2:33.75,cb:8,ch:5,cs:1,tp:30.37,score:'C',rec:'avoid',zone:false,
 moat:[['Licences DKNY/Montblanc/Coach','fort'],['Cash flows récurrents','fort']],
 cats:[{t:'Nouvelles licences luxe 2026',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Bennaim','6.5M€','Jan 2026']],
 peers:[{n:'Puig',pe:22,pb:4.5,roe:28,div:1.5,evebitda:15}],
 risks:{Licences:55,Mode:45,Devise:50,Concurrence:40,Cyclicite:40,Liquidite:25},
 track:[{y:'2025',p:'CA +10%',ok:'ok'}],
 thesis:"Interparfums crée des parfums sous licence pour DKNY, Montblanc, Coach. Zéro dette, ROE 22%, modèle asset-light parfait.",
 contra:"Dépendance licences renouvelables tous 7-10 ans. Mode volatile. Exposition USD."},

{ticker:'ARGAN',x2:'',x2s:'',name:'Argan',sector:'Entrepôts logistiques',cap:'mid',srd:true,idx:'SBF120',
 price:67.6,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.4,news5:'',dy_n:10,dy_med:2.7,div12:3.45,pe_lo:6.2,gmod:null,icr:5.1,ltv:40.6,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:0.0,irrn:7.1,irr:7.1,dq:'',vmult:null,hn:3,eveb_h:12.0,pfcf_h:9.8,pe_h:6.8,fcur:'EUR',fcfh:'188|174|185|129',nih:'245|246|-263|95',revh:'252|239|221|198',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:105.76,vpess:76.92,nregu:null,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:8.3,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:null,cagr:8.3,alarm:'',qwhy:'',qok:true,nde:null,fcfc:null,roicx:null,chg:-0.59,mkt:'1.5Md€',b52h:78.2,b52l:56.1,beta:1.1,
 pe:6.56,pb:0.7,ev_ebitda:18.25,ps:6.74,pfcf:7,ev_ebit:12.9,
 roe:11.1,roic:null,roa:2.8,debt:0.89,de:0.89,ic:7.4,cr:0.45,qr:0.6,
 yield:5.1,epsg:14.3,revg:4.8,margin:102.8,gm:82.3,om:58,fcf:10.8,
 capex:1.2,capr:4.6,capda:41.99,dcfb:66.95,dcfm:96.14,dcfu:94.51,
 pio:5,alt:0.71,rsi:41.8,mm50:70.88,mm200:64.49,
 el:67.3,eh:76.92,stop:69.22,o1:105.76,o2:116.33,cb:6,ch:5,cs:3,tp:78.85,score:'B',rec:'watch',zone:true,
 moat:[['Entrepôts XXL ecommerce','fort'],['Amazon locataire','fort']],
 cats:[{t:'Ecommerce logistique boom',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Assouline','8.5M€','Jan 2026']],
 peers:[{n:'Prologis',pe:28,pb:2.5,roe:8,div:3.2,evebitda:22}],
 risks:{Taux:70,Amazon:50,Dette:65,Commerce:40,Valorisation:55,Liquidite:25},
 track:[{y:'2025',p:'Dividende maintenu',ok:'ok'}],
 thesis:"Argan est la seule pure-play entrepôts XXL e-commerce en France. Amazon locataire majeur. Logistique e-commerce irréversible.",
 contra:"Dette élevée. Taux élevés pèsent. Dépendance Amazon (50% revenus)."},

{ticker:'BOIRON',x2:'',x2s:'',name:'Boiron',sector:'Homéopathie',cap:'small',srd:false,idx:'SBF120',
 price:18.15,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:5.2,news5:'',dy_n:10,dy_med:2.73,div12:1.35,pe_lo:16.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:8.0,pfcf_h:20.5,pe_h:19.6,fcur:'EUR',fcfh:'30|24|27|40',nih:'33|11|36|45',revh:'501|488|493|534',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-6.0,gimp:null,knife:true,neglect:true,vmeth:'per',nig:-9.9,cagr:-2.1,alarm:'',qwhy:'ROIC hors EA 13.7, ROIC 10.1, croissance CA -2.1%',qok:false,nde:-0.76,fcfc:97.0,roicx:13.7,chg:-2.42,mkt:'0.38Md€',b52h:32.25,b52l:16.9,beta:0.27,
 pe:12.02,pb:0.84,ev_ebitda:5.22,ps:0.64,pfcf:8,ev_ebit:6.7,
 roe:7.0,roic:10.1,roa:4.3,debt:0.06,de:0.06,ic:39.6,cr:2.25,qr:2.5,
 yield:7.3,epsg:-56.8,revg:-2.2,margin:5.3,gm:72.2,om:8,fcf:9.4,
 capex:0.8,capr:4.7,capda:1.27,dcfb:23.34,dcfm:27.46,dcfu:32.95,
 pio:5,alt:2.29,rsi:33.1,mm50:22.92,mm200:25.84,
 el:19.22,eh:24.16,stop:16.91,o1:28.83,o2:32.95,cb:3,ch:4,cs:4,tp:46,score:'C',rec:'avoid',zone:false,
 moat:[['Oscillococcinum marque mondiale','fort']],
 cats:[{t:'Cosmétiques diversification',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Boiron','3.5M€','Jan 2026']],
 peers:[{n:'Lehning',pe:15,pb:2.0,roe:10,div:3.5,evebitda:8}],
 risks:{Reglementation:75,Efficacité:70,Remboursement:80,Concurrence:45,Taille:55,Liquidite:45},
 track:[{y:'2025',p:'Déremboursement géré',ok:'partial'}],
 thesis:"Boiron à 10x PE avec 4.8% dividende et zéro dette. Oscillococcinum = marque mondiale. Diversification cosmétiques.",
 contra:"Déremboursement détruit la thèse principale. Controverse scientifique. Croissance quasi-nulle."},
{ticker:'LECTRA',x2:'',x2s:'',name:'Lectra',sector:'Logiciel coupe textile',cap:'small',srd:true,idx:'SBF120',
 price:21.25,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.7,news5:'',dy_n:10,dy_med:1.61,div12:0.35,pe_lo:29.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:13.4,pfcf_h:18.7,pe_h:33.4,fcur:'EUR',fcfh:'64|82|52|50',nih:'26|31|34|44',revh:'507|527|478|522',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-8.7,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-16.4,cagr:-1.0,alarm:'',qwhy:'ROIC 8.5, croissance CA -1.0%',qok:false,nde:0.59,fcfc:183.0,roicx:47.0,chg:1.92,mkt:'0.85Md€',b52h:25.5,b52l:15.02,beta:0.86,
 pe:34.84,pb:2.39,ev_ebitda:14.57,ps:1.62,pfcf:14,ev_ebit:25.8,
 roe:7.0,roic:8.5,roa:2.5,debt:0.38,de:0.38,ic:7.2,cr:0.67,qr:1.8,
 yield:1.7,epsg:63.6,revg:-0.3,margin:4.8,gm:73.8,om:14,fcf:8.1,
 capex:0.8,capr:2.0,capda:0.22,dcfb:15.06,dcfm:17.72,dcfu:21.26,
 pio:7,alt:1.99,rsi:53.6,mm50:21.64,mm200:19.1,
 el:13.47,eh:16.02,stop:11.85,o1:18.61,o2:21.26,cb:5,ch:4,cs:2,tp:23.17,score:'D',rec:'avoid',zone:false,
 moat:[['Systemes coupe cuir textile','fort'],['Mode auto aero clients','fort']],
 cats:[{t:'Mode durable automatisation',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Karoubi','2.5M€','Jan 2026']],
 peers:[{n:'Gerber Technology',pe:20,pb:3.5,roe:18,div:1.5,evebitda:13}],
 risks:{Mode:55,Auto:50,Cyclicite:50,Devise:45,Liquidite:30,Concurrence:35},
 track:[{y:'2025',p:'SaaS transition +12%',ok:'ok'}],
 thesis:"Lectra est le leader mondial des solutions de coupe automatisée pour le textile, cuir et automobile. La transition SaaS accélère la récurrence.",
 contra:"Cyclicité mode et auto. Post-acquisition Gerber intégration en cours."},

{ticker:'LACROIX',x2:'',x2s:'',name:'Lacroix',sector:'Electronique embarquee',cap:'small',srd:true,idx:'SBF120',
 price:17.1,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-5.0,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:5.7,pfcf_h:2.4,pe_h:21.7,fcur:'EUR',fcfh:'31|18|20|-18',nih:'-40|-34|4|12',revh:'445|494|734|708',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-14.3,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:-14.3,alarm:'',qwhy:'ROIC hors EA 6.1, ROIC 4.3, cash None%, croissance CA -14.3%',qok:false,nde:2.41,fcfc:null,roicx:6.1,chg:-0.29,mkt:'0.32Md€',b52h:20.9,b52l:9.7,beta:1.11,
 pe:5.41,pb:0.88,ev_ebitda:4.11,ps:0.18,pfcf:10,ev_ebit:9.1,
 roe:9.0,roic:4.3,roa:3.8,debt:1.31,de:1.31,ic:4.2,cr:1.32,qr:1.0,
 yield:2.5,epsg:8,revg:3.2,margin:-3.8,gm:36.8,om:5,fcf:38.4,
 capex:2.5,capr:1.9,capda:0.45,dcfb:31.98,dcfm:37.62,dcfu:45.14,
 pio:6,alt:1.41,rsi:41.6,mm50:17.73,mm200:15.96,
 el:27.09,eh:33.41,stop:23.84,o1:39.5,o2:45.14,cb:5,ch:4,cs:2,tp:45,score:'C',rec:'avoid',zone:false,
 moat:[['EMS electronique industrielle','modere'],['Ville intelligente','modere']],
 cats:[{t:'Smart city panneaux routiers',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Lacroix','3.2M€','Jan 2026']],
 peers:[{n:'Neways',pe:13,pb:1.2,roe:9,div:2.0,evebitda:6}],
 risks:{Auto:55,Cyclicite:55,Concurrence:45,Marges:55,Liquidite:30,Taille:45},
 track:[{y:'2025',p:'Smart city +10%',ok:'ok'}],
 thesis:"Lacroix est un fabricant EMS spécialisé dans la ville intelligente. Famille aux commandes.",
 contra:"Marges EMS très fines. Cyclicité industrielle. Concurrence asiatique."},

{ticker:'IDLG',x2:'',x2s:'',name:'ID Logistics',sector:'Logistique 3PL',cap:'mid',srd:true,idx:'SBF120',
 price:333.0,roiica:true,reinv:false,roiic:7.3,vmed:null,vepv:null,chg5:2.1,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:36.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:6.9,pfcf_h:5.9,pe_h:40.6,fcur:'EUR',fcfh:'331|385|355|276',nih:'63|53|52|38',revh:'3737|3271|2747|2481',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:16.4,gimp:null,knife:false,neglect:false,vmeth:'per',nig:18.3,cagr:14.6,alarm:'',qwhy:'ROIC hors EA 8.3, ROIC 5.9',qok:false,nde:2.35,fcfc:652.0,roicx:8.3,chg:-0.6,mkt:'2.2Md€',b52h:438.5,b52l:296.5,beta:1.0,
 pe:34.65,pb:3.18,ev_ebitda:40.79,ps:0.53,pfcf:12,ev_ebit:22.2,
 roe:10.5,roic:5.9,roa:3.2,debt:2.67,de:2.67,ic:2.2,cr:0.84,qr:1.0,
 yield:1.0,epsg:19.4,revg:18.3,margin:1.7,gm:16.2,om:4,fcf:15.3,
 capex:2.5,capr:4.4,capda:0.4,dcfb:177.34,dcfm:208.64,dcfu:250.37,
 pio:7,alt:1.76,rsi:58.4,mm50:327.32,mm200:356.25,
 el:171.08,eh:193.62,stop:150.55,o1:219.07,o2:250.37,cb:8,ch:5,cs:2,tp:506.0,score:'C',rec:'avoid',zone:false,
 moat:[['3PL logistique ecommerce','fort'],['Automation entrepots','fort']],
 cats:[{t:'Ecommerce automatisation croissance',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Gaber','8.5M€','Jan 2026']],
 peers:[{n:'GXO Logistics',pe:22,pb:2.5,roe:14,div:0.0,evebitda:11}],
 risks:{Ecommerce:45,Auto:50,Personnel:55,Cyclicite:50,Dette:45,Liquidite:20},
 track:[{y:'2025',p:'Expansion Bresil US',ok:'ok'}],
 thesis:"ID Logistics est le champion européen de la logistique 3PL pour le e-commerce. Famille Gaber, automation croissante, international. ROE 16%.",
 contra:"Marges fines (3%). Personnel intensif. Cyclicité e-commerce."},

{ticker:'ELIOR',x2:'',x2s:'',name:'Elior',sector:'Restauration collective',cap:'mid',srd:true,idx:'SBF120',
 price:1.78,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.4,news5:'',dy_n:5,dy_med:2.84,div12:0.04,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:7.2,pfcf_h:4.1,pe_h:8.2,fcur:'EUR',fcfh:'200|195|-60|-101',nih:'88|-46|-93|-427',revh:'6150|6053|5223|4451',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:11.4,gimp:null,knife:true,neglect:false,vmeth:'per',nig:null,cagr:11.4,alarm:'',qwhy:'ROIC hors EA 7.7, ROIC 1.1, cash None%, dette/EBITDA 3.2, perte exploitation',qok:false,nde:3.2,fcfc:null,roicx:7.7,chg:-4.51,mkt:'0.68Md€',b52h:3.2,b52l:1.7,beta:1.97,
 pe:7.12,pb:0.53,ev_ebitda:8.18,ps:0.07,pfcf:7,ev_ebit:9.6,
 roe:7.7,roic:1.1,roa:2.3,debt:1.48,de:1.48,ic:1.6,cr:0.55,qr:0.6,
 yield:2.1,epsg:-52.9,revg:-1.1,margin:1.1,gm:16.3,om:3,fcf:44.8,
 capex:1.2,capr:2.4,capda:0.85,dcfb:1.96,dcfm:2.31,dcfu:2.77,
 pio:7,alt:1.61,rsi:41.3,mm50:1.95,mm200:2.29,
 el:1.94,eh:2.16,stop:1.71,o1:2.43,o2:2.77,cb:6,ch:4,cs:4,tp:2.29,score:'C',rec:'avoid',zone:false,
 moat:[['Restauration collective France','modere'],['Ecoles hopitaux captifs','modere']],
 cats:[{t:'Prix repas indexe inflation',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction','5.5M€','Jan 2026']],
 peers:[{n:'Sodexo',pe:18,pb:2.5,roe:18,div:3.5,evebitda:9}],
 risks:{Dette:70,Energie:55,Personnel:65,Cyclicite:45,Liquidite:25,Reglementation:45},
 track:[{y:'2025',p:'Retour profitabilite',ok:'partial'}],
 thesis:"Elior sort d'une période difficile. À 0.6x livre avec restructuration avancée, retour possible 2-3x. Repas scolaires et hospitaliers = revenus captifs.",
 contra:"Dette encore élevée. Inflation coûts alimentaires et personnel. Margin recovery lente."},

{ticker:'WAGA',x2:'',x2s:'',name:'Waga Energy',sector:'Biogaz biomethane',cap:'small',srd:true,idx:'SRD',
 price:22.8,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:5.1,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'croissance Yahoo 46.0 %/an : probablement faussee par une acquisition ou une cession',vmult:null,hn:0,eveb_h:null,pfcf_h:null,pe_h:null,fcur:'EUR',fcfh:'-115|-73|-66|-48',nih:'-30|-18|-16|-10',revh:'60|56|33|19',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:46.0,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:46.0,alarm:'Piotroski 3/9',qwhy:'ROIC hors EA -7.0, ROIC -6.9, cash None%, dette/EBITDA None, perte exploitation',qok:false,nde:null,fcfc:null,roicx:-7.0,chg:-0.22,mkt:'0.52Md€',b52h:24.5,b52l:21.15,beta:0.44,
 pe:-26.21,pb:5.87,ev_ebitda:817.76,ps:9.28,pfcf:999,ev_ebit:null,
 roe:-27.8,roic:-6.9,roa:-1.3,debt:2.6,de:2.6,ic:-2.0,cr:0.87,qr:1.5,
 yield:0.0,epsg:40,revg:22.2,margin:-47.9,gm:50.4,om:18,fcf:-18.8,
 capex:3.5,capr:198.6,capda:10.87,dcfb:14,dcfm:22,dcfu:35,
 pio:3,alt:1.29,rsi:54.3,mm50:22.89,mm200:22.99,
 el:15,eh:22,stop:13,o1:26,o2:32,cb:6,ch:4,cs:2,tp:26,score:'D',rec:'avoid',zone:false,
 moat:[['WAGABOX technologie unique','fort'],['Biogaz decharges','fort']],
 cats:[{t:'Biomethane EU directive',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Dupont','2.8M€','Jan 2026']],
 peers:[{n:'Everfuel',pe:999,pb:2.5,roe:-25,div:0.0,evebitda:999}],
 risks:{Reglementation:50,CAPEX:60,Pipeline:55,Concurrence:45,Cash:45,Liquidite:25},
 track:[{y:'2025',p:'Sites UK US deployes',ok:'ok'}],
 thesis:"Waga Energy déploie WAGABOX pour upgrader le biogaz de décharge en biométhane injectable dans le réseau. Seule énergie renouvelable compatible réseau existant.",
 contra:"Valorisation élevée. CAPEX intensif. Pipeline de sites limité."},

{ticker:'LDLC',x2:'',x2s:'',name:'LDLC Group',sector:'Ecommerce high-tech',cap:'small',srd:false,idx:'SRD',
 price:8.8,roiica:false,reinv:false,roiic:26.8,vmed:null,vepv:null,chg5:-9.6,news5:'',dy_n:5,dy_med:3.49,div12:0.73,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:9.6,pfcf_h:6.3,pe_h:58.0,fcur:'EUR',fcfh:'-37|-0|15|-11',nih:'10|-11|-0|1',revh:'554|534|572|568',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:50.6,gimp:null,knife:true,neglect:true,vmeth:'per',nig:102.0,cagr:-0.8,alarm:'',qwhy:'ROIC hors EA 2.1, ROIC 1.4, cash -9411.0%, perte exploitation, croissance CA -0.8%',qok:false,nde:1.85,fcfc:-9411.0,roicx:2.1,chg:-1.12,mkt:'0.22Md€',b52h:20.6,b52l:7.82,beta:0.81,
 pe:5.33,pb:0.54,ev_ebitda:4.19,ps:0.1,pfcf:8,ev_ebit:6.3,
 roe:10.7,roic:1.4,roa:3.7,debt:0.49,de:0.49,ic:10.5,cr:1.25,qr:1.0,
 yield:8.2,epsg:5,revg:-1.2,margin:1.8,gm:24.5,om:3,fcf:-68.2,
 capex:0.8,capr:0.8,capda:null,dcfb:11.68,dcfm:13.74,dcfu:16.49,
 pio:6,alt:2.8,rsi:28.5,mm50:10.99,mm200:12.06,
 el:11.4,eh:12.81,stop:10.03,o1:14.43,o2:16.49,cb:4,ch:4,cs:2,tp:24,score:'C',rec:'avoid',zone:false,
 moat:[['Ecommerce tech France leader','modere'],['Réseau magasins web','modere']],
 cats:[{t:'IA PC gaming boom',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Ozanne','2.5M€','Jan 2026']],
 peers:[{n:'Fnac Darty',pe:9,pb:1.0,roe:11,div:4.2,evebitda:4}],
 risks:{Amazon:70,Marges:65,Cyclicite:55,Concurrence:65,Liquidite:35,Techno:40},
 track:[{y:'2025',p:'Gaming PC reprise',ok:'partial'}],
 thesis:"LDLC est le e-commerçant high-tech de référence en France avec réseau physique. À 10x PE avec 3.8% dividende.",
 contra:"Amazon domine. Marges très fines (2%). Concurrence extreme."}

,{ticker:'DBV',x2:'',x2s:'',name:'DBV Technologies',sector:'Biotech allergie',cap:'small',srd:false,idx:'SRD',
 price:1.59,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-6.1,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:0,eveb_h:null,pfcf_h:null,pe_h:null,fcur:'USD',fcfh:'-122|-107|-80|-56',nih:'-147|-114|-73|-96',revh:'0|0|0|0',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:true,neglect:true,vmeth:'per',nig:null,cagr:null,alarm:'Piotroski 4/9',qwhy:'ROIC hors EA -570.6, ROIC -564.7, cash None%, dette/EBITDA None, perte exploitation, croissance CA None%',qok:false,nde:null,fcfc:null,roicx:-570.6,chg:1.66,mkt:'0.28Md€',b52h:4.5,b52l:1.53,beta:-0.24,
 pe:-10.7,pb:3.3,ev_ebitda:-1.7,ps:99.46,pfcf:999,ev_ebit:null,
 roe:-142.7,roic:-564.7,roa:-60.6,debt:0.05,de:0.05,ic:null,cr:3.72,qr:4.2,
 yield:0.0,epsg:0,revg:-53.3,margin:-40,gm:100.0,om:-30,fcf:-24.3,
 capex:0.2,capr:null,capda:0.17,dcfb:4,dcfm:8,dcfu:15,
 pio:4,alt:0.98,rsi:27.5,mm50:2.15,mm200:2.99,
 el:4.5,eh:6.5,stop:3.8,o1:9.0,o2:13.0,cb:4,ch:3,cs:3,tp:3.64,score:'C',rec:'avoid',zone:false,
 moat:[['Viaskin patch allergie arachides','fort'],['FDA PDUFA date 2026','fort']],
 cats:[{t:'FDA decision Viaskin Peanut T2 2026',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Morgan','1.8M€','Jan 2026']],
 peers:[{n:'ALK Abello',pe:25,pb:3.5,roe:12,div:0.5,evebitda:15}],
 risks:{FDA:80,Cash:70,Dilution:65,Pipeline:75,Reglementation:70,Liquidite:30},
 track:[{y:'2025',p:'Dialogue FDA positif',ok:'partial'}],
 thesis:"DBV Technologies a Viaskin Peanut, le seul patch d'immunotherapie pour allergie arachides chez les enfants. Si FDA approuve en 2026, le marche est 2 millions d'enfants americains x 1000$/an = 2Md$ de potentiel. CEO a achete 1.8M€.",
 contra:"FDA a deja rejete deux fois. Cash limite, dilution certaine. Pari binaire pur. Reserver aux investisseurs sophistiques avec tolerance aux pertes totales."},

{ticker:'HIPAY',x2:'',x2s:'',name:'HiPay',sector:'Paiements cross-border',cap:'small',srd:false,idx:'SRD',
 price:4.24,roiica:false,reinv:false,roiic:83.8,vmed:null,vepv:null,chg5:-2.3,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:4.5,gmod:null,fcfh:'-0|5|3|-3',nih:'6|6|2|-8',revh:'75|74|65|59',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:3,eveb_h:6.2,pfcf_h:9.2,pe_h:8.6,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:8.3,gimp:null,knife:true,neglect:false,vmeth:'per',nig:null,cagr:8.3,alarm:'Piotroski 4/9',qwhy:'ROIC 9.4, cash 69.0%, perte exploitation',qok:false,nde:1.59,fcfc:69.0,roicx:45.0,chg:-2.3,mkt:'0.12Md€',b52h:9.9,b52l:3.83,beta:1.26,
 pe:6.52,pb:0.64,ev_ebitda:13.72,ps:0.36,pfcf:15,ev_ebit:8.2,
 roe:10.5,roic:9.4,roa:0.9,debt:0.76,de:0.76,ic:3.6,cr:1.01,qr:2.2,
 yield:0.0,epsg:15,revg:-2.1,margin:5.7,gm:24.4,om:10,fcf:-1.1,
 capex:0.5,capr:8.7,capda:1.7,dcfb:7.93,dcfm:9.33,dcfu:11.2,
 pio:4,alt:0.55,rsi:44.4,mm50:4.72,mm200:5.5,
 el:7.46,eh:8.58,stop:6.56,o1:9.8,o2:11.2,cb:4,ch:3,cs:1,tp:15.5,score:'C',rec:'avoid',zone:false,
 moat:[['Paiements ecommerce cross-border','fort'],['Agrement EMI europeen','fort']],
 cats:[{t:'Cross-border ecommerce EU',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Meeschaert','2.5M€','Jan 2026']],
 peers:[{n:'Adyen',pe:45,pb:8.5,roe:20,div:0.0,evebitda:28}],
 risks:{Concurrence:60,Adyen:65,Reglementation:50,Liquidite:45,Taille:55,Tech:45},
 track:[{y:'2025',p:'Croissance 12%',ok:'ok'}],
 thesis:"HiPay est specialiste des paiements ecommerce cross-border avec agrement EMI europeen. Les marchands cherchent des alternatives a Adyen moins cheres. Croissance 12% a 20x PE.",
 contra:"Adyen et Stripe sont 100x plus gros. La differenciation tarifaire s'erode. Taille insuffisante pour les grands retailers."},

{ticker:'LISI',x2:'',x2s:'',name:'Lisi',sector:'Fixations aeronautiques',cap:'mid',srd:true,idx:'SBF120',
 price:61.7,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:4.9,news5:'',dy_n:9,dy_med:1.29,div12:0.46,pe_lo:17.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:7.6,pfcf_h:26.8,pe_h:18.3,fcur:'EUR',fcfh:'96|80|38|23',nih:'140|56|38|57',revh:'1748|1609|1630|1425',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:20.9,gimp:null,knife:false,neglect:false,vmeth:'per',nig:34.9,cagr:7.0,alarm:'',qwhy:'ROIC hors EA 6.2, ROIC 4.5',qok:false,nde:1.1,fcfc:82.0,roicx:6.2,chg:1.15,mkt:'0.65Md€',b52h:72.6,b52l:45.0,beta:1.08,
 pe:32.99,pb:2.49,ev_ebitda:12.53,ps:1.53,pfcf:10,ev_ebit:27.0,
 roe:8.7,roic:4.5,roa:5.0,debt:0.45,de:0.45,ic:4.4,cr:1.74,qr:1.2,
 yield:0.8,epsg:60.2,revg:4.4,margin:8.9,gm:50.9,om:7,fcf:3.4,
 capex:1.5,capr:5.8,capda:1.03,dcfb:59.8,dcfm:70.35,dcfu:84.42,
 pio:9,alt:3.03,rsi:53.8,mm50:62.0,mm200:60.81,
 el:59.09,eh:65.85,stop:52.0,o1:73.87,o2:84.42,cb:6,ch:4,cs:2,tp:75.86,score:'C',rec:'avoid',zone:false,
 moat:[['Fixations titane aeronautique','fort'],['Airbus Boeing clients directs','fort']],
 cats:[{t:'Airbus production acceleration',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Orsatelli','4.5M€','Jan 2026']],
 peers:[{n:'SPS Technologies',pe:16,pb:2.5,roe:15,div:2.0,evebitda:10}],
 risks:{Airbus:55,Cyclicite:50,Titane:45,Liquidite:25,Defense:35,Concentration:50},
 track:[{y:'2025',p:'Cadence Airbus +8%',ok:'ok'}],
 thesis:"Lisi est le specialiste mondial des fixations pour l'aeronautique (titane, inconel). Chaque A320 utilise 500 000 fixations Lisi. La montee en cadence d'Airbus a 75/mois en 2026 est un catalyseur mecanique.",
 contra:"Forte dependance Airbus/Boeing. Perturbation chaine titane post-Ukraine. Cyclicite aeronautique."},

{ticker:'SYENSQO',x2:'',x2s:'',name:'Syensqo',sector:'Chimie haute performance',cap:'mid',srd:false,idx:'EURONEXT',
 price:80.5,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.3,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:8.2,pfcf_h:29.3,pe_h:51.4,fcur:'EUR',fcfh:'243|217|425|745',nih:'-62|-5|193|950',revh:'5969|6445|7065|8123',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:0,place:'Bruxelles',near:false,gsrc:'yahoo (4 ans publies)',gused:-9.8,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:-9.8,alarm:'Piotroski 4/9',qwhy:'ROIC hors EA 5.5, ROIC 3.9, croissance CA -9.8%',qok:false,nde:2.36,fcfc:151.0,roicx:5.5,chg:-0.62,mkt:'5.8Md€',b52h:83.4,b52l:41.76,beta:0.52,
 pe:18.45,pb:1.35,ev_ebitda:9.19,ps:1.39,pfcf:14,ev_ebit:53.0,
 roe:-1.0,roic:3.9,roa:2.2,debt:0.46,de:0.46,ic:1.3,cr:1.65,qr:1.2,
 yield:2.0,epsg:-52.4,revg:4.1,margin:-0.4,gm:30.9,om:14,fcf:3.0,
 capex:2.8,capr:9.0,capda:0.77,dcfb:47.06,dcfm:55.36,dcfu:66.43,
 pio:4,alt:2.21,rsi:54.1,mm50:79.89,mm200:67.31,
 el:45.95,eh:51.6,stop:40.44,o1:58.13,o2:66.43,cb:8,ch:5,cs:2,tp:82.5,score:'D',rec:'avoid',zone:false,
 moat:[['Specialites chimiques brevetes','fort'],['Batteries aero auto defense','fort']],
 cats:[{t:'Batteries next-gen materiaux',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Plante','5.5M€','Jan 2026']],
 peers:[{n:'Arkema',pe:14,pb:1.8,roe:12,div:3.5,evebitda:8},{n:'DSM-Firmenich',pe:22,pb:3.5,roe:15,div:2.5,evebitda:14}],
 risks:{Cyclicite:50,Energie:45,Concurrence:45,CAPEX:50,Devise:40,Liquidite:15},
 track:[{y:'2025',p:'Demerger puis croissance',ok:'ok'}],
 thesis:"Syensqo (spin-off Solvay) regroupe les specialites chimiques haute valeur : electrolytes batteries, composites aerospatial, solutions defense. Un actif de transition energetique a 18x PE avec ROE 15%.",
 contra:"Jeune entite cotee = decouverte de prix en cours. Cyclicite chimique malgre la niche."},

{ticker:'IPSEN',x2:'',x2s:'',name:'Ipsen',sector:'Pharma maladies rares',cap:'mid',srd:true,idx:'SBF120',
 price:148.4,roiica:true,reinv:false,roiic:null,vmed:157.02,vepv:82.57,chg5:3.0,news5:'',dy_n:10,dy_med:1.15,div12:1.6,pe_lo:12.8,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:8.8,irr:8.8,dq:'',vmult:160.96,hn:4,eveb_h:7.5,pfcf_h:12.5,pe_h:17.7,fcur:'EUR',fcfh:'810|133|677|718',nih:'444|346|644|649',revh:'3929|3574|3306|3156',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:157.02,vpess:100.4,nregu:1,regn:3,regu:3,place:'Paris',mthreat:'expirations de brevets (generiques), dependance aux succes de R&D',mtype:'medicaments de specialite proteges par brevets',mscore:2,near:false,gsrc:'communique 2026-10-05',gused:12.0,gimp:10.5,knife:false,neglect:false,vmeth:'qarp',nig:-11.9,cagr:7.6,alarm:'',qwhy:'',qok:true,nde:-0.53,fcfc:112.0,roicx:18.8,chg:-0.4,mkt:'8.5Md€',b52h:174.0,b52l:112.7,beta:0.35,
 pe:24.01,pb:2.6,ev_ebitda:7.55,ps:2.85,pfcf:14,ev_ebit:18.1,
 roe:11.4,roic:15.5,roa:10.3,debt:0.2,de:0.2,ic:14.1,cr:1.97,qr:1.6,
 yield:1.1,epsg:21.5,revg:18.7,margin:11.9,gm:81.0,om:22,fcf:6.6,
 capex:1.5,capr:8.4,capda:0.53,dcfb:133.47,dcfm:157.02,dcfu:188.42,
 pio:8,alt:4.01,rsi:50.6,mm50:154.43,mm200:154.9,
 el:109.91,eh:125.62,stop:90.36,o1:157.02,o2:172.72,cb:10,ch:5,cs:2,tp:164.29,score:'B',rec:'watch',zone:false,
 moat:[['Somatuline acromegalie monopole','fort'],['Maladies rares orphelines','fort'],['Cabometyx cancer rein','fort']],
 cats:[{t:'Cabometyx expansion oncologie',w:'2026',c:'var(--gn)'},{t:'Spongosine nerfs pipeline',w:'T2 2026',c:'var(--gd)'}],
 ins:[['Achat','Famille Beaufour','18M€','Jan 2026']],
 peers:[{n:'Sanofi',pe:18,pb:2.8,roe:16,div:4.1,evebitda:13},{n:'BioMarin',pe:28,pb:3.5,roe:10,div:0,evebitda:20}],
 risks:{Concurrence:50,Pipeline:45,FDA:40,Devise:40,Brevet:55,Liquidite:15},
 track:[{y:'2025',p:'Cabometyx +15%',ok:'ok'},{y:'2024',p:'Maladies rares expansion',ok:'ok'}],
 thesis:"Ipsen est la pharma des maladies rares avec Somatuline (acromegalie, tumeurs neuroendocrines), Cabometyx (cancer rein/foie), Dysport (neurologie). ROE 22%, pipeline solide, famille Beaufour aux commandes depuis 1920. A 16x PE pour une pharma de qualite rare.",
 contra:"Exposition brevet Somatuline (expiration 2027-2028). Concurrence Novartis/Pfizer sur maladies rares. Pipeline a prouver."},

{ticker:'REXEL',x2:'',x2s:'',name:'Rexel',sector:'Distribution electrique',cap:'large',srd:true,idx:'SBF120',
 price:33.07,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-4.3,news5:'',dy_n:8,dy_med:3.74,div12:1.2,pe_lo:6.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:7.6,pfcf_h:9.5,pe_h:13.2,fcur:'EUR',fcfh:'650|745|784|709',nih:'589|339|775|922',revh:'19415|19285|19153|18702',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-6.3,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-13.9,cagr:1.3,alarm:'',qwhy:'ROIC 9.0, dette/EBITDA 2.69, croissance CA 1.3%',qok:false,nde:2.69,fcfc:110.0,roicx:15.5,chg:-1.08,mkt:'4.8Md€',b52h:39.8,b52l:28.37,beta:0.98,
 pe:14.63,pb:1.76,ev_ebitda:12.07,ps:0.52,pfcf:8,ev_ebit:13.7,
 roe:12.6,roic:9.0,roa:4.8,debt:1.07,de:1.07,ic:4.8,cr:1.66,qr:1.0,
 yield:3.6,epsg:30.9,revg:2.2,margin:3.4,gm:25.2,om:5,fcf:6.4,
 capex:0.8,capr:0.7,capda:0.33,dcfb:28.93,dcfm:34.03,dcfu:40.84,
 pio:8,alt:2.88,rsi:39.9,mm50:35.76,mm200:35.62,
 el:28.24,eh:31.72,stop:24.85,o1:35.73,o2:40.84,cb:8,ch:5,cs:2,tp:41.44,score:'C',rec:'avoid',zone:false,
 moat:[['Distribution electrique 2800 agences','fort'],['Transition energie captive','fort']],
 cats:[{t:'Renovation energetique EU',w:'Long terme',c:'var(--gn)'}],
 ins:[['Achat','CEO Gannaway','5.5M€','Jan 2026']],
 peers:[{n:'Sonepar prive',pe:999,pb:999,roe:999,div:0,evebitda:999}],
 risks:{Cyclicite:55,Construction:60,Concurrence:45,Distribution:45,Marges:55,Liquidite:15},
 track:[{y:'2025',p:'Renovation energetique stable',ok:'ok'}],
 thesis:"Rexel est le distributeur electrique mondial (2800 agences). Chaque renovation energetique, chaque borne VE, chaque installation solaire passe par ses comptoirs. A 11x PE avec 4.5% dividende, c'est une exposition a la transition energetique a prix raisonnable.",
 contra:"Distribution = marges fines. Cyclicite construction forte. Amazon B2B menace le modele."},

{ticker:'FIGEAC',x2:'',x2s:'',name:'Figeac Aero',sector:'Usinage aeronautique',cap:'small',srd:false,idx:'SRD',
 price:10.3,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-7.2,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 515.0 contre 13.6 attendu)',vmult:null,hn:1,eveb_h:10.1,pfcf_h:15.4,pe_h:null,fcur:'EUR',fcfh:'30|21|-19|-1',nih:'1||-12|-18',revh:'487||397|342',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:2,regn:2,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:19.4,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:19.4,alarm:'',qwhy:'ROIC hors EA -1.4, ROIC -1.4, cash None%, dette/EBITDA 3.81, perte exploitation',qok:false,nde:3.81,fcfc:null,roicx:-1.4,chg:-4.1,mkt:'0.22Md€',b52h:12.8,b52l:9.02,beta:0.76,
 pe:515.0,pb:5.27,ev_ebitda:9.81,ps:0.94,pfcf:7,ev_ebit:38.2,
 roe:1.1,roic:-1.4,roa:2.5,debt:4.44,de:4.44,ic:1.0,cr:1.39,qr:0.8,
 yield:0.0,epsg:192.1,revg:16.8,margin:0.2,gm:36.7,om:6,fcf:6.6,
 capex:1.8,capr:10.8,capda:1.16,dcfb:12.88,dcfm:15.15,dcfu:18.18,
 pio:3,alt:1.35,rsi:36.6,mm50:10.93,mm200:10.77,
 el:12.73,eh:14.18,stop:11.2,o1:15.91,o2:18.18,cb:5,ch:4,cs:2,tp:13.43,score:'C',rec:'avoid',zone:false,
 moat:[['Usinage titane aluminium aero','fort'],['Airbus Boeing Tier 1','fort']],
 cats:[{t:'Cadence Airbus rattrapage',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Figeac','3.5M€','Jan 2026']],
 peers:[{n:'Daher',pe:12,pb:1.2,roe:10,div:2.0,evebitda:6}],
 risks:{Dette:65,Airbus:55,Cyclicite:60,Taux:50,Liquidite:25,Titane:45},
 track:[{y:'2025',p:'Desendettement en cours',ok:'partial'}],
 thesis:"Figeac Aero usine les pieces structurelles en titane et aluminium pour Airbus (A350, A320) et Boeing. La remontee en cadence d'Airbus a 75 avions/mois en 2026 est un catalyseur mecanique. Famille fondatrice aux commandes.",
 contra:"Endettement post-COVID encore eleve. Dependance Airbus (70% CA). Titane sous pression post-Ukraine."}
,{ticker:'DIOR',x2:'',x2s:'',name:'Christian Dior',sector:'Luxe holding',cap:'large',srd:true,idx:'CAC40',
 price:423.4,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.9,news5:'',dy_n:10,dy_med:1.75,div12:14.3,pe_lo:20.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.3,pfcf_h:8.7,pe_h:20.7,fcur:'EUR',fcfh:'14190|13367|10590|12747',nih:'4531|5208|6304|5797',revh:'80807|84682|86153|79183',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-3.6,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-7.9,cagr:0.7,alarm:'',qwhy:'croissance CA 0.7%',qok:false,nde:1.07,fcfc:233.0,roicx:46.4,chg:-2.26,mkt:'130Md€',b52h:611.5,b52l:363.8,beta:0.83,
 pe:16.78,pb:3.06,ev_ebitda:7.21,ps:0.96,pfcf:16,ev_ebit:8.1,
 roe:17.1,roic:28.2,roa:7.6,debt:0.55,de:0.55,ic:14.9,cr:1.64,qr:1.1,
 yield:3.3,epsg:0.9,revg:-2.9,margin:5.7,gm:66.4,om:22,fcf:18.6,
 capex:2.5,capr:5.8,capda:0.58,dcfb:341.27,dcfm:401.49,dcfu:481.79,
 pio:6,alt:1.84,rsi:57.2,mm50:404.07,mm200:449.84,
 el:313.16,eh:366.16,stop:275.58,o1:421.56,o2:481.79,cb:12,ch:5,cs:2,tp:790,score:'D',rec:'avoid',zone:false,
 moat:[['Holding LVMH 41.5% a decote','fort'],['Christian Dior Couture direct','fort']],
 cats:[{t:'Decote holding resorption',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Arnault','85M€','Jan 2026']],
 peers:[{n:'LVMH',pe:22,pb:5.1,roe:24,div:2.4,evebitda:14}],
 risks:{LVMH:65,Holding:50,Luxe:45,Chine:55,Liquidite:15,Decote:40},
 track:[{y:'2025',p:'Decote holding stable',ok:'partial'}],
 thesis:"Christian Dior est la holding de controle de LVMH (41.5%) avec une decote de 15-20% sur sa valeur de marche. Acheter Dior c est acheter LVMH moins cher. La famille Arnault concentre son patrimoine ici. La decote peut se resorber par une OPE.",
 contra:"Decote de holding peut persister. Moins liquide que LVMH direct. Exposition concentree."},

{ticker:'ABIVAX',x2:'',x2s:'',name:'Abivax',sector:'Biotech immunologie',cap:'small',srd:true,idx:'SBF120',
 price:77.95,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.3,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:0,eveb_h:null,pfcf_h:null,pe_h:null,fcur:'EUR',fcfh:'-161|-155|-97|-54',nih:'-336|-176|-148|-61',revh:'0|0|0|0',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:true,neglect:true,vmeth:'per',nig:null,cagr:null,alarm:'Piotroski 4/9',qwhy:'ROIC hors EA -102.8, ROIC -148.5, cash None%, dette/EBITDA None, perte exploitation, croissance CA None%',qok:false,nde:null,fcfc:null,roicx:-102.8,chg:-1.27,mkt:'0.52Md€',b52h:139.0,b52l:60.45,beta:-0.23,
 pe:-26.91,pb:16.99,ev_ebitda:-20.24,ps:1457.33,pfcf:999,ev_ebit:null,
 roe:-252.3,roic:-148.5,roa:-62.9,debt:0.08,de:0.0,ic:-10.6,cr:5.96,qr:4.5,
 yield:0.0,epsg:0,revg:-6.8,margin:-80,gm:100.0,om:-70,fcf:-2.4,
 capex:0.2,capr:null,capda:0.13,dcfb:8,dcfm:18,dcfu:35,
 pio:4,alt:29.14,rsi:36.9,mm50:92.35,mm200:99.98,
 el:10,eh:15,stop:8.5,o1:22,o2:35,cb:5,ch:3,cs:4,tp:134.86,score:'D',rec:'avoid',zone:false,
 moat:[['ABX464 maladies inflammatoires','fort'],['Phase 3 Crohn RCH positive','fort']],
 cats:[{t:'FDA submission RCH 2026',w:'T3 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Kieny','2.5M€','Fev 2026']],
 peers:[{n:'AbbVie Humira',pe:18,pb:6.5,roe:45,div:4.2,evebitda:12},{n:'UCB',pe:22,pb:3.5,roe:18,div:1.5,evebitda:14}],
 risks:{FDA:75,Cash:65,Dilution:70,Concurrence:60,Pipeline:70,Liquidite:25},
 track:[{y:'2025',p:'Phase 3 RCH positive p<0.05',ok:'ok'},{y:'2024',p:'Partenariat Moderna avance',ok:'ok'}],
 thesis:"Abivax a ABX464 (obefazimod) un ARN regulateur pour les maladies inflammatoires. La Phase 3 est positive. Si FDA approuve en 2026, le marche IBD vaut 20Md$ avec peu de concurrence directe sur ce mecanisme. CEO a investi 2.5M€ personnellement.",
 contra:"Biotech pre-revenus. Cash brule 4.5M par trimestre. FDA peut rejeter malgre Phase 3 positive. Concurrence AbbVie massive."},

{ticker:'NANOBT',x2:'',x2s:'',name:'Nanobiotix',sector:'Radioenhancement cancer',cap:'small',srd:false,idx:'SRD',
 price:18.85,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-10.0,news5:'NBTX Chaîne d’options - NASDAQ:NBTX|https://news.google.com/rss/articles/CBMibkFVX3lxTE1ZNUJ0blgzWEpTT0FucDl4N1VjX0J5Q1lpaU1kbFJ1NW05N3hiVkFYalQ1Q21OaUYydXZMVHRsVXg5S0JoX2FlOHdNWFpQMDd5bk5sSDE2amloLXFubVJvY1ZXZS1oZmZNS2RkMHBB?oc=5|TradingView ;; Action Nanobiotix : faut-il acheter fin 2026 ?|https://news.google.com/rss/articles/CBMiZkFVX3lxTE1oX0VUd2ZCaXNvMDVqX2FLSlFtRjYtY1UzMm9MR1RnVzVqZTdSVFBqR29PLW5uaFFoRlgtX2NhVzFJd2UwdXo2NTFJbUlIZ3c4c2ROTUNWNU5ZSHdLOVoxWEFadVFCdw?oc=5|Cafédelabourse',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:0,eveb_h:null,pfcf_h:null,pe_h:null,fcur:'EUR',fcfh:'-34|-20|-13|-37',nih:'-24|-68|-40|-57',revh:'30|-12|30|0',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:true,neglect:true,vmeth:'per',nig:null,cagr:null,alarm:'Piotroski 3/9',qwhy:'ROIC hors EA -94.0, ROIC -93.9, cash None%, dette/EBITDA None, perte exploitation, croissance CA None%',qok:false,nde:null,fcfc:null,roicx:-94.0,chg:-1.41,mkt:'0.38Md€',b52h:47.66,b52l:13.1,beta:0.59,
 pe:-75.4,pb:-28.69,ev_ebitda:-32.47,ps:83.42,pfcf:999,ev_ebit:null,
 roe:-30,roic:-93.9,roa:-21.3,debt:0.4,de:null,ic:-1.3,cr:1.44,qr:4.0,
 yield:0.0,epsg:0,revg:-79.2,margin:-55,gm:100.0,om:-45,fcf:-3.5,
 capex:0.3,capr:1.8,capda:0.37,dcfb:6,dcfm:12,dcfu:22,
 pio:3,alt:3.16,rsi:21.1,mm50:29.69,mm200:28.85,
 el:7.5,eh:10,stop:6.5,o1:14,o2:20,cb:5,ch:3,cs:3,tp:52.2,score:'D',rec:'avoid',zone:false,
 moat:[['Nanoparticules NBTXR3 radio','fort'],['Partenariat Johnson Johnson','fort']],
 cats:[{t:'NBTXR3 label US cancers multiples',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Levy','2.2M€','Jan 2026']],
 peers:[{n:'Novocure TTFields',pe:35,pb:6.5,roe:8,div:0.0,evebitda:25}],
 risks:{FDA:70,Cash:60,JnJ:65,Pipeline:65,Concurrence:55,Liquidite:35},
 track:[{y:'2025',p:'Phase 3 Head Neck positive',ok:'ok'},{y:'2024',p:'JnJ 60M milestones',ok:'ok'}],
 thesis:"Nanobiotix injecte des nanoparticules (NBTXR3) dans les tumeurs qui amplifient l effet de la radiotherapie jusqu a 4x. Johnson Johnson a investi 60M pour les droits US. 5 essais Phase 3 en cours.",
 contra:"Pari multiple FDA. Cash critique si JnJ ne declenche pas les milestones. Adoption lente."},

{ticker:'ICAD',x2:'',x2s:'',name:'iCade',sector:'Immobilier sante',cap:'mid',srd:true,idx:'SBF120',
 price:14.45,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.2,news5:'',dy_n:10,dy_med:6.05,div12:1.92,pe_lo:null,gmod:null,icr:3.4,ltv:36.5,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:null,pfcf_h:10.4,pe_h:56.4,fcur:'EUR',fcfh:'-5|166|4|-234',nih:'-123|-276|-1250|54',revh:'1342|1452|1528|1568',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:null,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-5.1,gimp:null,knife:true,neglect:true,vmeth:'per',nig:null,cagr:-5.1,alarm:'',qwhy:'loyers en baisse -5.1%',qok:false,nde:null,fcfc:null,roicx:null,chg:-2.23,mkt:'1.2Md€',b52h:22.76,b52l:14.21,beta:0.92,
 pe:5.07,pb:0.31,ev_ebitda:16.96,ps:0.83,pfcf:7,ev_ebit:null,
 roe:-5.2,roic:null,roa:1.6,debt:1.12,de:1.12,ic:-0.3,cr:1.21,qr:0.6,
 yield:13.0,epsg:4,revg:-3.0,margin:-14.2,gm:36.5,om:25,fcf:-0.5,
 capex:1.2,capr:22.8,capda:8.96,dcfb:22.58,dcfm:26.56,dcfu:31.87,
 pio:7,alt:0.28,rsi:28.5,mm50:16.97,mm200:18.31,
 el:21.25,eh:24.44,stop:18.7,o1:27.89,o2:31.87,cb:6,ch:5,cs:3,tp:19.35,score:'C',rec:'avoid',zone:false,
 moat:[['Cliniques EHPAD securite','fort'],['Loyers triple-net long terme','fort']],
 cats:[{t:'Sante vieillissement structurel',w:'Long terme',c:'var(--gn)'}],
 ins:[['Achat','Direction','2.8M€','Jan 2026']],
 peers:[{n:'Cofinimmo',pe:20,pb:0.8,roe:4,div:6.5,evebitda:16}],
 risks:{Taux:70,EHPAD:55,Dette:70,Locataires:50,Reglementation:55,Liquidite:20},
 track:[{y:'2025',p:'Portefeuille sante resilient',ok:'ok'}],
 thesis:"iCade est la SIIC de sante leader avec cliniques, EHPAD et residences seniors. Baux triple-net 12 ans avec indexation. Le vieillissement demographique EU est un vent porteur structurel de 30 ans.",
 contra:"Dette elevee. Regulation EHPAD sous pression. Dependance locataires sante."},

{ticker:'GLEVT',x2:'',x2s:'',name:'GL Events',sector:'Evenementiel',cap:'small',srd:false,idx:'SBF120',
 price:31.5,roiica:false,reinv:false,roiic:38.9,vmed:null,vepv:null,chg5:29.4,news5:'GL events sous les feux de la rampe après un relèvement d’objectifs|https://news.google.com/rss/articles/CBMixgFBVV95cUxNQkphbl81ME5uZ1UzV0x5MlpGMzcwS1ZZdkFrTTRCcWJlT1hzWDI2NmlHOVY3V2UwRUctNXlpYWtuSmhjQVo0UU5zekxkNW1XNjFwMGwzdlVpWXlzOU9vV1g1RWY0d2JtemNLLWl6THlwdklXZ2hkLXpnQm9fMlhBYmVaSlphcjRYWEZDZFc4S1pyWEFMX2RRNnRreGVyWnN2b25KV3UxWFpwYTA0U011MnFiRzAzVFQ0Qjl5N2F0Z0poa3AxLXc?oc=5|Zonebourse Suisse ;; GL Events fait le show, la tech perd les pédales|https://news.google.com/rss/articles/CBMirAFBVV95cUxOamlYMmV3ZWdJRUg2U1RWUXh0bHYzS0JHTGJ2bHVRYlp3elJsZDBIUlYtV21hVHF4TXVwb2I2cmlYOU9JRE9hN0doTFQyZFpZdy02REU5V3pPM2xmWlZyX0xoWUJOUXRkMlhfTU1IR3hhbDBmRFU1SWY2YVlocXZMYm8yUkstV1BPYjFQcDktWnd1c3Rwc2t4ZnNzZ0xldmVEMDZOMEFwRm12TWRw?oc=5|Zonebourse ;; Action GL events / Cours GLO Bourse Euronext Paris|https://news.google.com/rss/articles/CBMiZkFVX3lxTE56LUtvWVl5dGQxOVAtY1NocHJTblBPVzQxOUZlaVM2MU9ZVDVvM21qX0NBeFZNYktwR2lWNWJBN2VqZENHbkNUYzV3RldQdnI5a1RvVkI2ai1RM1lfQm40SGVTbHpEdw?oc=5|Zonebourse',dy_n:7,dy_med:2.94,div12:1.0,pe_lo:7.2,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:6.0,pfcf_h:4.5,pe_h:9.3,fcur:'EUR',fcfh:'158|64|159|149',nih:'82|73|60|53',revh:'1717|1634|1419|1310',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:12.6,gimp:null,knife:false,neglect:false,vmeth:'per',nig:15.8,cagr:9.4,alarm:'',qwhy:'ROIC 8.3, dette/EBITDA 3.36',qok:false,nde:3.36,fcfc:198.0,roicx:19.0,chg:0.32,mkt:'0.45Md€',b52h:36.25,b52l:23.4,beta:1.15,
 pe:11.05,pb:1.69,ev_ebitda:10.34,ps:0.51,pfcf:8,ev_ebit:11.6,
 roe:14.9,roic:8.3,roa:3.5,debt:2.55,de:2.55,ic:2.9,cr:0.94,qr:1.0,
 yield:3.2,epsg:8.2,revg:8.9,margin:4.8,gm:94.9,om:8,fcf:17.1,
 capex:1.5,capr:4.9,capda:1.11,dcfb:27.45,dcfm:32.3,dcfu:38.76,
 pio:7,alt:0.91,rsi:78.0,mm50:27.22,mm200:30.65,
 el:27.13,eh:30.23,stop:23.87,o1:33.91,o2:38.76,cb:5,ch:4,cs:2,tp:37.6,score:'C',rec:'avoid',zone:false,
 moat:[['Partenaire olympique stades','modere'],['Centres congres internationaux','modere']],
 cats:[{t:'Paris Expo 2030 candidature',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Clavel','2.5M€','Jan 2026']],
 peers:[{n:'Reed Exhibitions',pe:14,pb:2.5,roe:18,div:2.5,evebitda:10}],
 risks:{Evenements:55,Pandemie:45,Cyclicite:50,Dette:40,Devise:35,Liquidite:35},
 track:[{y:'2025',p:'JO Paris heritage +12%',ok:'ok'}],
 thesis:"GL Events a profite des JO Paris 2024. Le carnet international reste solide. Sous-valorise a 10x PE. La candidature Paris Expo 2030 est un catalyseur potentiel.",
 contra:"Post-JO effet base defavorable. Cyclicite evenementielle."},

{ticker:'VRMTX',x2:'',x2s:'',name:'Verimatrix',sector:'Cybersecurite contenu',cap:'small',srd:true,idx:'SBF120',
 price:0.26,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-8.0,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:0,eveb_h:30.0,pfcf_h:null,pe_h:null,fcur:'USD',fcfh:'-2|-4|-4|-1',nih:'-79|-10|-14|-18',revh:'47|57|62|61',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-8.7,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:-8.7,alarm:'Piotroski 3/9',qwhy:'ROIC hors EA -33.6, ROIC -5.2, cash None%, dette/EBITDA None, perte exploitation, croissance CA -8.7%',qok:false,nde:null,fcfc:null,roicx:-33.6,chg:-5.38,mkt:'0.18Md€',b52h:0.38,b52l:0.14,beta:1.63,
 pe:-11.83,pb:0.75,ev_ebitda:-7.33,ps:0.55,pfcf:14,ev_ebit:null,
 roe:-39.8,roic:-5.2,roa:-3.7,debt:0.81,de:0.81,ic:-22.6,cr:1.07,qr:1.8,
 yield:0.0,epsg:12,revg:-18.2,margin:-37.8,gm:62.7,om:10,fcf:-10.1,
 capex:0.5,capr:4.4,capda:0.37,dcfb:3.0,dcfm:4.5,dcfu:6.2,
 pio:3,alt:-3.28,rsi:25.1,mm50:0.32,mm200:0.23,
 el:3.3,eh:4.3,stop:2.8,o1:5.2,o2:6.2,cb:4,ch:3,cs:1,tp:5.2,score:'C',rec:'avoid',zone:false,
 moat:[['DRM securite video OTT','fort'],['Clients Canal TF1 Netflix','fort']],
 cats:[{t:'Streaming securite contenu',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction','1.2M€','Jan 2026']],
 peers:[{n:'Irdeto',pe:20,pb:3.5,roe:18,div:1.5,evebitda:13}],
 risks:{Streaming:50,Concurrence:55,Piratage:45,Liquidite:40,Taille:50,Techno:45},
 track:[{y:'2025',p:'ARR +12%',ok:'ok'}],
 thesis:"Verimatrix protege le contenu video contre le piratage pour Canal+, TF1, Netflix. La securisation DRM est obligatoire pour les licences studios. Croissance 10%/an sur le streaming.",
 contra:"Competition Irdeto/Nagravision. Streaming consolide = moins de clients."},
{ticker:'SAMSE',x2:'',x2s:'',name:'Samse',sector:'Distribution materiaux',cap:'small',srd:false,idx:'SBF120',
 price:113.0,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-3.0,news5:'',dy_n:10,dy_med:5.01,div12:5.0,pe_lo:6.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:6.3,pfcf_h:7.1,pe_h:13.3,fcur:'EUR',fcfh:'83|74|92|79',nih:'26|26|76|95',revh:'1925|1932|1889|1912',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-17.6,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-35.4,cagr:0.2,alarm:'',qwhy:'ROIC hors EA 6.6, ROIC 6.2, dette/EBITDA 3.62, croissance CA 0.2%',qok:false,nde:3.62,fcfc:147.0,roicx:6.6,chg:-0.88,mkt:'0.88Md€',b52h:134.0,b52l:112.0,beta:0.46,
 pe:11.78,pb:0.64,ev_ebitda:12.85,ps:0.2,pfcf:9,ev_ebit:18.2,
 roe:5.8,roic:6.2,roa:1.8,debt:0.99,de:0.99,ic:3.8,cr:1.42,qr:1.1,
 yield:4.4,epsg:985.2,revg:1.0,margin:1.7,gm:29.6,om:5,fcf:21.9,
 capex:1.2,capr:1.9,capda:0.42,dcfb:142.14,dcfm:167.22,dcfu:200.66,
 pio:7,alt:1.69,rsi:24.0,mm50:118.41,mm200:117.89,
 el:138.79,eh:155.85,stop:122.14,o1:175.58,o2:200.66,cb:6,ch:4,cs:2,tp:268,score:'C',rec:'avoid',zone:false,
 moat:[['Distribution materiaux Sud-Est leader','fort'],['450 agences reseau capillaire','fort']],
 cats:[{t:'Renovation energetique EU 2026',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Fribourg','5.5M€','Jan 2026']],
 peers:[{n:'Saint-Gobain Distrib',pe:14,pb:2.5,roe:18,div:3.5,evebitda:9},{n:'Point.P',pe:13,pb:2.0,roe:16,div:4.0,evebitda:8}],
 risks:{Construction:55,Cyclicite:55,Concurrence:45,Taux:50,Liquidite:35,Energie:35},
 track:[{y:'2025',p:'Renovation energetique stable',ok:'ok'}],
 thesis:"Samse est le distributeur de materiaux leader dans le Sud-Est avec 450 agences. Chaque maitre d oeuvre, artisan et particulier de la region passe par ses comptoirs. La renovation energetique des batiments (obligation EU) est son marche pour les 15 prochaines annees. A 12x PE avec 4.8% dividende.",
 contra:"Cyclicite construction forte. Saint-Gobain Distribution attaque le marche pro. Famille peut privatiser."},

{ticker:'MANITOU',x2:'',x2s:'',name:'Manitou',sector:'Engins manutention',cap:'mid',srd:true,idx:'SBF120',
 price:20.0,roiica:true,reinv:false,roiic:8.7,vmed:null,vepv:null,chg5:1.3,news5:'',dy_n:10,dy_med:2.8,div12:0.75,pe_lo:5.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:4.8,pfcf_h:4.4,pe_h:8.5,fcur:'EUR',fcfh:'187|137|-158|-198',nih:'68|122|143|55',revh:'2564|2656|2871|2362',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:5.2,gimp:null,knife:false,neglect:false,vmeth:'per',nig:7.7,cagr:2.8,alarm:'',qwhy:'ROIC hors EA 8.2, ROIC 8.2, cash -8.0%, croissance CA 2.8%',qok:false,nde:1.2,fcfc:-8.0,roicx:8.2,chg:-0.99,mkt:'1.4Md€',b52h:24.35,b52l:16.9,beta:1.44,
 pe:11.05,pb:0.77,ev_ebitda:4.8,ps:0.28,pfcf:8,ev_ebit:8.3,
 roe:9.0,roic:8.2,roa:5.0,debt:0.32,de:0.32,ic:8.5,cr:1.48,qr:1.2,
 yield:3.7,epsg:57.6,revg:12.0,margin:3.2,gm:17.7,om:7,fcf:24.4,
 capex:1.8,capr:4.5,capda:1.33,dcfb:24.17,dcfm:28.44,dcfu:34.13,
 pio:5,alt:2.18,rsi:43.1,mm50:21.18,mm200:20.31,
 el:23.61,eh:26.51,stop:20.78,o1:29.86,o2:34.13,cb:8,ch:5,cs:2,tp:24.6,score:'C',rec:'avoid',zone:false,
 moat:[['Leader mondial chariots telescopiques','fort'],['Agriculture precision equipement','fort']],
 cats:[{t:'Agriculture precision mecanisation',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Braud','5.2M€','Jan 2026']],
 peers:[{n:'JCB',pe:12,pb:2.0,roe:16,div:2.5,evebitda:7},{n:'Caterpillar',pe:18,pb:5.5,roe:45,div:2.0,evebitda:12}],
 risks:{Agriculture:55,Cyclicite:55,Concurrence:45,Devise:40,Marges:50,Liquidite:20},
 track:[{y:'2025',p:'Agriculture stable',ok:'ok'}],
 thesis:"Manitou est le numero 1 mondial des chariots telescopiques pour l agriculture et la construction. Son produit phare (le telesco) permet a un seul agriculteur de faire le travail de 5. La mecanisation agricole mondiale est une tendance irreversible. A 10x PE avec 4.2% dividende, sous-valorise vs Caterpillar.",
 contra:"Cyclicite agriculture et construction. Caterpillar et JCB attaquent. Mais niche telesco reste dominee."},

{ticker:'NEXTY',x2:'',x2s:'',name:'Nexity',sector:'Promotion immobiliere',cap:'large',srd:true,idx:'SBF120',
 price:4.7,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.0,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:9.4,pfcf_h:4.5,pe_h:28.1,fcur:'EUR',fcfh:'177|184|179|200',nih:'-188|-62|19|188',revh:'2821|3333|3964|4352',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-13.5,gimp:null,knife:true,neglect:true,vmeth:'per',nig:null,cagr:-13.5,alarm:'',qwhy:'ROIC hors EA 2.4, ROIC 1.6, cash None%, dette/EBITDA 25.93, perte exploitation, croissance CA -13.5%',qok:false,nde:25.93,fcfc:null,roicx:2.4,chg:-1.8,mkt:'1.2Md€',b52h:10.45,b52l:4.31,beta:0.82,
 pe:37.17,pb:0.17,ev_ebitda:20.0,ps:0.1,pfcf:7,ev_ebit:null,
 roe:-10.0,roic:1.6,roa:0.3,debt:1.16,de:1.16,ic:-1.8,cr:1.17,qr:0.8,
 yield:0.0,epsg:8,revg:-18.3,margin:-6.8,gm:29.1,om:6,fcf:67.9,
 capex:0.8,capr:1.6,capda:0.21,dcfb:1.72,dcfm:2.02,dcfu:2.42,
 pio:6,alt:0.54,rsi:35.4,mm50:5.79,mm200:7.63,
 el:1.62,eh:1.86,stop:1.43,o1:2.12,o2:2.42,cb:6,ch:4,cs:5,tp:10.12,score:'D',rec:'avoid',zone:false,
 moat:[['Premier promoteur France','modere'],['Nexity Services recurrents','modere']],
 cats:[{t:'Baisse taux BCE rebond immobilier',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Vandermersch','3.5M€','Jan 2026']],
 peers:[{n:'Bouygues Immo',pe:999,pb:999,roe:999,div:0,evebitda:999},{n:'Kaufman Broad',pe:12,pb:1.2,roe:12,div:5.5,evebitda:6}],
 risks:{Immobilier:75,Taux:75,Construction:65,Dette:65,Reserves:60,Liquidite:20},
 track:[{y:'2025',p:'Reservations -35%',ok:'m'},{y:'2024',p:'Restructuration',ok:'partial'}],
 thesis:"Nexity au plus bas historique. Si les taux BCE baissent en 2026, le rebond des reservations peut etre violent depuis ce point. Les Francais veulent toujours devenir proprietaires. La penurie de logements neuf est structurelle.",
 contra:"La crise peut durer. Les acquants ne peuvent toujours pas emprunter. Dette a surveiller. Direction a prouver sa credibilite."}

,{ticker:'SCBSM',x2:'',x2s:'',name:'SCBSM Bureaux',sector:'Immobilier bureaux Paris',cap:'small',srd:false,idx:'SRD',
 price:9.15,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:5.2,news5:'',dy_n:6,dy_med:1.47,div12:0.19,pe_lo:3.4,gmod:null,icr:2.2,ltv:39.5,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:0.0,irrn:2.0,irr:2.0,dq:'',vmult:null,hn:4,eveb_h:16.7,pfcf_h:8.0,pe_h:9.1,fcur:'EUR',fcfh:'17|16|15|11',nih:'13|0|9|34',revh:'23|22|20|19',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:21.45,vpess:15.6,nregu:null,regn:3,regu:3,place:'Paris',near:true,gsrc:'yahoo (4 ans publies)',gused:6.3,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:null,cagr:6.3,alarm:'',qwhy:'couverture des interets 2.2',qok:false,nde:null,fcfc:null,roicx:null,chg:0.0,mkt:'0.22Md€',b52h:10.2,b52l:8.7,beta:0.7,
 pe:9.73,pb:0.47,ev_ebitda:9,ps:null,pfcf:8,ev_ebit:null,
 roe:7,roic:null,roa:null,debt:3.5,de:null,ic:2.6,cr:null,qr:0.7,
 yield:6.5,epsg:3,revg:2,margin:25,gm:58,om:28,fcf:13.5,
 capex:0.5,capr:null,capda:null,dcfb:12.78,dcfm:19.5,dcfu:18.05,
 pio:6,alt:0.56,rsi:50.5,mm50:9.44,mm200:9.59,
 el:13.65,eh:15.6,stop:14.04,o1:21.45,o2:23.59,cb:4,ch:3,cs:2,tp:15,score:'C',rec:'avoid',zone:false,
 moat:[['Bureaux Paris intra-muros premium','fort'],['Loyers indices triple-net','fort']],
 cats:[{t:'Bureaux Paris penurie offre',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction','1.2M€','Jan 2026']],
 peers:[{n:'Gecina',pe:15,pb:0.9,roe:5,div:5.8,evebitda:18}],
 risks:{Taux:70,Teletravail:60,Dette:65,Vacance:55,Liquidite:55,Paris:35},
 track:[{y:'2025',p:'Taux occupation 96%',ok:'ok'}],
 thesis:"SCBSM loue des bureaux premium dans Paris intra-muros ou l offre est structurellement rare. 6.5% de dividende avec des baux long terme indexes. L immobilier de bureau parisien prime est defensif et rare.",
 contra:"Le teletravail a reduit la demande. Taux hauts font souffrir les foncieres. Dette elevee."},

{ticker:'EMEIS',x2:'',x2s:'',name:'Emeis EHPAD',sector:'EHPAD maisons retraite',cap:'large',srd:true,idx:'SBF120',
 price:10.02,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.8,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:12.8,pfcf_h:3.8,pe_h:1.6,fcur:'EUR',fcfh:'514|329|225|273',nih:'-298|-412|1355|-4027',revh:'5895|5636|5198|4681',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:8.0,gimp:null,knife:true,neglect:true,vmeth:'per',nig:null,cagr:8.0,alarm:'',qwhy:'ROIC hors EA 0.5, ROIC 0.5, cash None%, dette/EBITDA 11.17, perte exploitation',qok:false,nde:11.17,fcfc:null,roicx:0.5,chg:-3.75,mkt:'4.5Md€',b52h:16.01,b52l:9.54,beta:0.67,
 pe:50.1,pb:1.19,ev_ebitda:17.29,ps:0.27,pfcf:10,ev_ebit:123.0,
 roe:-10.6,roic:0.5,roa:1.2,debt:3.81,de:3.81,ic:0.2,cr:0.82,qr:0.7,
 yield:2.5,epsg:10,revg:3.5,margin:-3.4,gm:14.6,om:7,fcf:31.9,
 capex:1.8,capr:2.8,capda:0.48,dcfb:3.41,dcfm:4.01,dcfu:4.81,
 pio:7,alt:0.45,rsi:31.8,mm50:12.14,mm200:13.68,
 el:3.21,eh:3.69,stop:2.82,o1:4.21,o2:4.81,cb:8,ch:5,cs:3,tp:16.37,score:'D',rec:'avoid',zone:false,
 moat:[['Leader EHPAD Europe 1200 maisons','fort'],['Vieillissement demographique captif','fort']],
 cats:[{t:'Papy-boom EHPAD 2026-2035',w:'Long terme',c:'var(--gn)'}],
 ins:[['Achat','Direction','5.5M€','Jan 2026']],
 peers:[{n:'Orpea renomme Emeis',pe:18,pb:2.0,roe:12,div:2.5,evebitda:9}],
 risks:{Reglementation:65,Personnel:60,Dette:70,Scandales:55,Politique:60,Liquidite:20},
 track:[{y:'2025',p:'Restructuration avancee',ok:'partial'}],
 thesis:"Emeis (ex-Korian) est le leader europeen des EHPAD avec 1200 maisons de retraite. Le vieillissement demographique est la tendance la plus certaine au monde — le nombre de personnes dependantes double d ici 2040. Apres la crise 2022-2023, le groupe est en restructuration avancee.",
 contra:"Scandales mediatiques. Reglementation renforcee = couts. Dette encore elevee. Reputation a reconstruire."},

{ticker:'ALFPC',x2:'',x2s:'',name:'Fountaine Pajot',sector:'Catamarans voiliers',cap:'small',srd:true,idx:'SBF120',
 price:74.8,roiica:true,reinv:false,roiic:7.8,vmed:null,vepv:null,chg5:0.9,news5:'',dy_n:10,dy_med:1.59,div12:2.52,pe_lo:5.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 24.1 contre 5.7 attendu)',vmult:null,hn:4,eveb_h:3.4,pfcf_h:6.9,pe_h:8.1,fcur:'EUR',fcfh:'-14|-10|19|46',nih:'30|33|11|16',revh:'323|351|277|220',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:18.5,gimp:null,knife:true,neglect:true,vmeth:'per',nig:23.4,cagr:13.7,alarm:'',qwhy:'cash 46.0%',qok:false,nde:0.13,fcfc:46.0,roicx:54.7,chg:0.0,mkt:'0.88Md€',b52h:117.4,b52l:70.6,beta:0.72,
 pe:24.05,pb:0.92,ev_ebitda:1.5,ps:0.41,pfcf:10,ev_ebit:1.0,
 roe:11.3,roic:41.4,roa:3.1,debt:0.34,de:0.34,ic:26.1,cr:1.32,qr:2.0,
 yield:3.4,epsg:-66.3,revg:-12.3,margin:6.5,gm:50.3,om:14,fcf:-11.1,
 capex:1.5,capr:8.9,capda:1.54,dcfb:82.65,dcfm:97.24,dcfu:116.69,
 pio:6,alt:2.24,rsi:34.4,mm50:80.91,mm200:89.17,
 el:79.74,eh:90.24,stop:70.17,o1:102.1,o2:116.69,cb:8,ch:4,cs:1,tp:165,score:'C',rec:'avoid',zone:false,
 moat:[['Leader catamarans voiliers monde','fort'],['Marque Lipari Elba premium','fort']],
 cats:[{t:'Nautisme premium 8%/an structurel',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Poncin','8.5M€','Jan 2026']],
 peers:[{n:'Beneteau',pe:10,pb:1.2,roe:14,div:3.5,evebitda:5}],
 risks:{Cyclicite:50,Devise:45,Materiaux:45,Carnet:40,Liquidite:30,Nautisme:45},
 track:[{y:'2025',p:'Carnet 3 ans plein',ok:'ok'},{y:'2024',p:'ROE 24%',ok:'ok'}],
 thesis:"Fountaine Pajot est le numero 1 mondial des catamarans a voile. Carnet de commandes plein 3 ans, ROE 24%, zero dette, famille fondatrice. Le nautisme premium croit de 8%/an structurellement sur la montee des classes moyennes mondiales.",
 contra:"Cyclicite loisirs premium. Expo devises (ventes en dollars). Carnet sensible aux annulations si recession."},

{ticker:'SELENV',x2:'',x2s:'',name:'Seche Environnement',sector:'Dechets dangereux',cap:'mid',srd:true,idx:'SBF120',
 price:70.5,roiica:true,reinv:false,roiic:1.9,vmed:null,vepv:null,chg5:1.4,news5:'',dy_n:10,dy_med:2.2,div12:1.2,pe_lo:15.7,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:7.2,pfcf_h:7.1,pe_h:17.6,fcur:'EUR',fcfh:'116|116|95|48',nih:'21|36|48|45',revh:'1254|1190|1089|973',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-6.4,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-21.6,cagr:8.8,alarm:'',qwhy:'ROIC hors EA 13.0, ROIC 6.0, dette/EBITDA 2.6',qok:false,nde:2.6,fcfc:252.0,roicx:13.0,chg:-0.28,mkt:'0.95Md€',b52h:91.5,b52l:55.6,beta:0.46,
 pe:30.79,pb:0.83,ev_ebitda:8.42,ps:0.42,pfcf:10,ev_ebit:17.6,
 roe:3.9,roic:6.0,roa:2.1,debt:1.45,de:1.45,ic:1.9,cr:1.67,qr:1.2,
 yield:1.7,epsg:-23.4,revg:6.4,margin:1.4,gm:56.6,om:12,fcf:21.2,
 capex:2.5,capr:8.8,capda:0.89,dcfb:59.44,dcfm:69.93,dcfu:83.92,
 pio:6,alt:1.05,rsi:42.3,mm50:76.95,mm200:76.71,
 el:58.04,eh:65.17,stop:51.08,o1:73.43,o2:83.92,cb:6,ch:4,cs:2,tp:86.67,score:'C',rec:'avoid',zone:false,
 moat:[['Incinerateurs dechets dangereux','fort'],['Autorisation prefectorale 30 ans','fort']],
 cats:[{t:'Dechets industriels reglementation EU',w:'2026',c:'var(--gn)'}],
 ins:[['Famille Seche','Direction','8.5M€','Jan 2026']],
 peers:[{n:'Veolia',pe:18,pb:2.0,roe:12,div:4.0,evebitda:10}],
 risks:{Reglementation:45,CAPEX:50,Accidents:55,Dette:45,Cyclicite:40,Liquidite:25},
 track:[{y:'2025',p:'ROE 18%',ok:'ok'},{y:'2024',p:'Acquisitions EU',ok:'ok'}],
 thesis:"Seche Environnement incinere les dechets industriels dangereux. Chaque autorisation prefectorale prend 10-15 ans a obtenir — personne ne peut ouvrir un concurrent demain. Moat reglementaire absolu. ROE 18%, famille fondatrice aux commandes. La pepite du traitement des dechets.",
 contra:"CAPEX intensif. Accidents industriels = risque reputationnel. Dette a surveiller."},

{ticker:'LNSBN',x2:'',x2s:'',name:'Lanson BCC',sector:'Champagne premium',cap:'small',srd:false,idx:'SRD',
 price:25.8,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.0,news5:'',dy_n:9,dy_med:1.81,div12:0.6,pe_lo:5.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:12.3,pfcf_h:17.9,pe_h:8.6,fcur:'EUR',fcfh:'12|8|-15|40',nih:'16|24|37|39',revh:'233|255|272|289',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-16.1,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-25.2,cagr:-6.9,alarm:'',qwhy:'ROIC hors EA 4.8, ROIC 4.6, cash 40.0%, dette/EBITDA 11.47, croissance CA -6.9%',qok:false,nde:11.47,fcfc:40.0,roicx:4.8,chg:-0.77,mkt:'0.22Md€',b52h:36.1,b52l:25.6,beta:0.23,
 pe:10.75,pb:0.44,ev_ebitda:15.94,ps:0.73,pfcf:10,ev_ebit:18.8,
 roe:4.3,roic:4.6,roa:2.2,debt:1.45,de:1.45,ic:2.3,cr:1.81,qr:0.7,
 yield:2.3,epsg:-28.9,revg:-15.7,margin:7.0,gm:49.2,om:7,fcf:7.1,
 capex:0.8,capr:3.1,capda:0.75,dcfb:28.51,dcfm:33.54,dcfu:40.25,
 pio:6,alt:0.83,rsi:38.2,mm50:26.82,mm200:27.37,
 el:26.16,eh:30.59,stop:23.02,o1:35.22,o2:40.25,cb:4,ch:3,cs:2,tp:24,score:'C',rec:'avoid',zone:false,
 moat:[['Champagne Lanson marque 270 ans','fort'],['Stocks vieillissement 3 ans','fort']],
 cats:[{t:'Champagne premium Asie croissance',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille BCC','2.5M€','Jan 2026']],
 peers:[{n:'Laurent-Perrier',pe:14,pb:0.9,roe:8,div:3.5,evebitda:9}],
 risks:{Champagne:55,Chine:50,Cyclicite:55,Dette:50,Liquidite:45,Climat:45},
 track:[{y:'2025',p:'Asie en hausse',ok:'partial'}],
 thesis:"Lanson est une maison de Champagne fondee en 1760 — 270 ans de savoir-faire. L appellation champagne est geographiquement protegee, personne ne peut imiter. La classe aisee asiatique est son marche de demain. A 0.8x livre avec dividende.",
 contra:"Cyclicite fetes premium. Dette relative aux stocks de champagne. Climat menace les vignobles."},

{ticker:'ALTGX',x2:'',x2s:'',name:'Touax Rail',sector:'Location wagons fret',cap:'small',srd:false,idx:'SRD',
 price:3.13,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.6,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:6.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.9,pfcf_h:2.0,pe_h:9.2,fcur:'EUR',fcfh:'3|16|19|-2',nih:'2|4|4|7',revh:'182|199|195|211',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-21.8,gimp:null,knife:true,neglect:true,vmeth:'per',nig:-38.8,cagr:-4.7,alarm:'',qwhy:'ROIC hors EA 4.7, ROIC 4.6, dette/EBITDA 6.23, croissance CA -4.7%',qok:false,nde:6.23,fcfc:218.0,roicx:4.7,chg:-0.95,mkt:'0.12Md€',b52h:4.94,b52l:3.01,beta:1.09,
 pe:2.63,pb:0.31,ev_ebitda:10.66,ps:0.13,pfcf:8,ev_ebit:20.5,
 roe:-4.2,roic:4.6,roa:1.1,debt:2.34,de:2.34,ic:1.0,cr:1.09,qr:0.7,
 yield:3.2,epsg:5,revg:-14.3,margin:-2.9,gm:45.4,om:10,fcf:14.7,
 capex:1.8,capr:0.3,capda:0.02,dcfb:3.46,dcfm:4.07,dcfu:4.88,
 pio:5,alt:0.52,rsi:36.0,mm50:3.63,mm200:3.97,
 el:3.34,eh:3.78,stop:2.94,o1:4.27,o2:4.88,cb:4,ch:3,cs:2,tp:22,score:'D',rec:'avoid',zone:false,
 moat:[['Parc wagons fret ferroviaire EU','modere'],['Conteneurs fluviaux location','modere']],
 cats:[{t:'Fret ferroviaire modal shift',w:'2026',c:'var(--gn)'}],
 ins:[['Famille Jourdain','Direction','1.5M€','Jan 2026']],
 peers:[{n:'GATX Rail',pe:12,pb:1.0,roe:8,div:4.5,evebitda:8}],
 risks:{Fret:55,Taux:65,Dette:70,Cyclicite:55,Liquidite:50,Ferroviaire:45},
 track:[{y:'2025',p:'Taux remplissage stable',ok:'partial'}],
 thesis:"Touax loue des wagons de fret et des conteneurs fluviaux — des actifs tangibles qui beneficient du report modal de la route vers le rail. A 0.7x livre avec 5.5% de dividende.",
 contra:"Dette tres elevee. Taux hauts = cout de financement douloureux. Fret ferroviaire EU encore peu developpe."},

{ticker:'SOLVB',x2:'',x2s:'',name:'Solvay SA',sector:'Chimie specialites',cap:'large',srd:false,idx:'EURONEXT',
 price:24.9,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.2,news5:'',dy_n:10,dy_med:17.25,div12:2.43,pe_lo:1.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 830.0 contre 10.1 attendu)',vmult:null,hn:4,eveb_h:3.9,pfcf_h:4.8,pe_h:7.9,fcur:'EUR',fcfh:'462|330|847|1097',nih:'30|223|2093|1905',revh:'4746|5130|6025|7978',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Bruxelles',near:false,gsrc:'yahoo (4 ans publies)',gused:-45.4,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-74.9,cagr:-15.9,alarm:'',qwhy:'ROIC hors EA 13.7, ROIC 9.8, cash 64.0%, croissance CA -15.9%',qok:false,nde:2.33,fcfc:64.0,roicx:13.7,chg:-1.11,mkt:'2.5Md€',b52h:29.16,b52l:23.54,beta:0.26,
 pe:830.0,pb:2.49,ev_ebitda:7.77,ps:0.57,pfcf:9,ev_ebit:16.2,
 roe:0.8,roic:9.8,roa:3.7,debt:2.01,de:2.01,ic:2.3,cr:1.15,qr:1.0,
 res:{q1:'05/2026',q2:'07/2026',q3:'10/2026',ra:'02/2027'},
 yield:9.7,epsg:317.8,revg:-5.9,margin:0.1,gm:21.4,om:8,fcf:17.8,
 capex:2.5,capr:4.6,capda:0.54,dcfb:36.68,dcfm:43.15,dcfu:51.78,
 pio:5,alt:1.63,rsi:46.2,mm50:25.46,mm200:25.64,
 el:35.81,eh:40.22,stop:31.51,o1:45.31,o2:51.78,cb:7,ch:5,cs:2,tp:24.77,score:'C',rec:'avoid',zone:false,
 moat:[['Chimie speciaux niche soda ash','modere'],['Batteries LFP ingredient','modere']],
 cats:[{t:'Batteries LFP soda ash demande',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Direction','3.5M€','Jan 2026']],
 peers:[{n:'Lanxess',pe:10,pb:0.7,roe:5,div:3.5,evebitda:5}],
 risks:{Energie:65,Cyclicite:60,Concurrence:55,Chine:50,Dette:50,Liquidite:15},
 track:[{y:'2025',p:'Demerger Syensqo complet',ok:'ok'}],
 thesis:"Post-scission avec Syensqo, la nouvelle Solvay se concentre sur le soda ash et la silice. A 0.8x livre, le marche valorise mal la position de leader soda ash indispensable aux batteries LFP de prochaine generation. Le soda ash est une matieres premiere critique EU.",
 contra:"Cyclicite chimique maximale. Energie = 25% des couts. Concurrence Chine sur soda ash croissante."},

{ticker:'BNENF',x2:'',x2s:'',name:'Beneteau',sector:'Bateaux voiliers',cap:'mid',srd:true,idx:'SBF120',
 price:4.79,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.7,news5:'',dy_n:9,dy_med:2.56,div12:0.2,pe_lo:5.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:3,eveb_h:5.9,pfcf_h:8.3,pe_h:7.5,fcur:'EUR',fcfh:'67|103|-69|-88',nih:'-43|93|185|103',revh:'849|1034|1465|1251',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-12.1,gimp:null,knife:true,neglect:true,vmeth:'per',nig:null,cagr:-12.1,alarm:'Piotroski 3/9',qwhy:'ROIC hors EA 9.0, ROIC 8.1, cash 4.0%, dette/EBITDA 2.62, perte exploitation, croissance CA -12.1%',qok:false,nde:2.62,fcfc:4.0,roicx:9.0,chg:-4.39,mkt:'0.85Md€',b52h:9.0,b52l:4.7,beta:0.77,
 pe:14.44,pb:0.53,ev_ebitda:5.67,ps:0.42,pfcf:8,ev_ebit:null,
 roe:-7.5,roic:8.1,roa:-0.0,debt:0.54,de:0.54,ic:-6.7,cr:1.46,qr:1.4,
 res:{q1:'06/2026',q2:'09/2026',q3:'--',ra:'10/2026'},
 yield:4.0,epsg:7,revg:11.2,margin:-4.4,gm:55.8,om:7,fcf:17.9,
 capex:1.5,capr:6.3,capda:0.85,dcfb:3.58,dcfm:4.21,dcfu:5.05,
 pio:3,alt:1.08,rsi:39.3,mm50:5.43,mm200:6.5,
 el:3.45,eh:3.91,stop:3.04,o1:4.42,o2:5.05,cb:6,ch:4,cs:2,tp:7.05,score:'D',rec:'avoid',zone:false,
 moat:[['Beneteau Jeanneau Lagoon marques','fort'],['Leader voiliers motorises monde','fort']],
 cats:[{t:'Nautisme premium croissance',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Roux','5.5M€','Jan 2026']],
 peers:[{n:'Fountaine Pajot',pe:12,pb:2.8,roe:24,div:2.5,evebitda:7}],
 risks:{Cyclicite:55,Devise:50,Materiaux:45,Carnet:45,Liquidite:25,Nautisme:50},
 track:[{y:'2025',p:'Carnet normalise',ok:'partial'}],
 thesis:"Beneteau est le leader mondial de la plaisance avec Beneteau, Jeanneau et Lagoon. 3 marques iconiques dans 3 segments du nautisme. A 10x PE, sous-valorise par rapport a son historique. Le marche se normalise apres le boom COVID.",
 contra:"Cyclicite nautisme forte. Carnet en cours de normalisation post-COVID. Matiere premieres."},

{ticker:'IDSF',x2:'',x2s:'',name:'Infotel',sector:'ESN IT finance',cap:'small',srd:false,idx:'SRD',
 price:38.55,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-1.5,news5:'',dy_n:10,dy_med:3.16,div12:2.0,pe_lo:16.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:7.4,pfcf_h:15.7,pe_h:18.2,fcur:'EUR',fcfh:'20|32|22|22',nih:'16|18|18|20',revh:'294|295|308|300',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-4.0,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-7.4,cagr:-0.7,alarm:'',qwhy:'croissance CA -0.7%',qok:false,nde:-2.58,fcfc:129.0,roicx:57.2,chg:-0.26,mkt:'0.25Md€',b52h:44.2,b52l:33.5,beta:0.34,
 pe:16.4,pb:2.23,ev_ebitda:5.89,ps:0.86,pfcf:10,ev_ebit:9.0,
 roe:20.8,roic:39.2,roa:7.6,debt:0.2,de:0.2,ic:29.6,cr:1.89,qr:3.0,
 yield:5.2,epsg:142.9,revg:9.4,margin:7.5,gm:55.4,om:8,fcf:7.4,
 capex:0.5,capr:2.1,capda:0.56,dcfb:45.09,dcfm:53.05,dcfu:63.66,
 pio:7,alt:3.15,rsi:48.0,mm50:39.55,mm200:37.77,
 el:40.32,eh:47.96,stop:35.48,o1:55.7,o2:63.66,cb:3,ch:3,cs:1,tp:51.38,score:'C',rec:'avoid',zone:false,
 moat:[['ESN specialisee banque assurance','fort'],['BNP SocGen AXA clients captifs','fort']],
 cats:[{t:'Core banking modernisation IA',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Famille Drahi','3.5M€','Jan 2026']],
 peers:[{n:'Sopra Steria',pe:14,pb:1.8,roe:14,div:2.5,evebitda:8}],
 risks:{Cyclicite:45,Banque:40,Concurrence:45,Marges:50,Liquidite:40,ESN:40},
 track:[{y:'2025',p:'Banque +10%',ok:'ok'},{y:'2024',p:'ROE 22%',ok:'ok'}],
 thesis:"Infotel est une ESN qui fait exclusivement de l informatique pour les banques et assurances — les systemes les plus complexes et les plus critiques. BNP, SocGen, AXA ne peuvent pas se passer de ses equipes. ROE 22%, zero dette, dividende 3.8%. Une perle meconnue.",
 contra:"Marche tres concentre (finance). Cyclicite bancaire. Concurrence Sopra Steria sur la meme niche."},

{ticker:'GENIE',x2:'',x2s:'',name:'Genfit',sector:'Biotech NASH hepatite',cap:'small',srd:true,idx:'SBF120',
 price:8.31,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-1.2,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'croissance Yahoo 48.0 %/an : probablement faussee par une acquisition ou une cession',vmult:null,hn:1,eveb_h:19.2,pfcf_h:12.3,pe_h:119.1,fcur:'EUR',fcfh:'-30|15|-58|-73',nih:'-86|2|-29|-24',revh:'65|67|29|20',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:48.0,gimp:null,knife:true,neglect:true,vmeth:'per',nig:null,cagr:48.0,alarm:'Piotroski 3/9',qwhy:'ROIC hors EA -154.7, ROIC -36.4, cash None%, dette/EBITDA None, perte exploitation',qok:false,nde:null,fcfc:null,roicx:-154.7,chg:-1.07,mkt:'0.28Md€',b52h:15.48,b52l:3.4,beta:1.19,
 pe:-845.37,pb:-8.57,ev_ebitda:-8.03,ps:6.99,pfcf:999,ev_ebit:null,
 roe:-5189.6,roic:-36.4,roa:-21.1,debt:0.3,de:null,ic:-70.7,cr:1.58,qr:4.0,
 yield:0.0,epsg:0,revg:-32.0,margin:-171.7,gm:100.0,om:-25,fcf:-7.1,
 capex:0.2,capr:5.2,capda:1.86,dcfb:2.86,dcfm:3.36,dcfu:4.03,
 pio:3,alt:-3.63,rsi:34.3,mm50:11.6,mm200:9.76,
 el:2.35,eh:2.96,stop:2.07,o1:3.53,o2:4.03,cb:5,ch:3,cs:3,tp:17.48,score:'D',rec:'avoid',zone:false,
 moat:[['Elafibranor NASH PBC molecules','fort'],['IND ALD biochimie hepatite','fort']],
 cats:[{t:'NASH approved Ocaliva competitor',w:'T2 2026',c:'var(--gn)'}],
 ins:[['Achat','CEO Neyret','1.8M€','Jan 2026']],
 peers:[{n:'Intercept Pharma',pe:999,pb:2.5,roe:-30,div:0,evebitda:999},{n:'Madrigal',pe:999,pb:5.5,roe:-15,div:0,evebitda:999}],
 risks:{FDA:75,Cash:65,NASH:70,Dilution:65,Concurrence:60,Liquidite:25},
 track:[{y:'2025',p:'Elafibranor PBC soumis FDA',ok:'ok'},{y:'2024',p:'Phase 3 NASH concluant',ok:'ok'}],
 thesis:"Genfit a elafibranor approuve au Canada et en soumission FDA pour la Cholangite Biliaire Primitive. Si FDA approuve en 2026, le marche est 60 000 patients US sans alternative. CEO achete. Le NASH est le marche de 20Md$ qui arrive.",
 contra:"Biotech pre-revenus. Cash brule. FDA peut rejeter. Concurrence Madrigal/Intercept sur NASH."},

{ticker:'CDRCK',x2:'',x2s:'',name:'Carmila',sector:'Centres commerciaux CA',cap:'mid',srd:true,idx:'SBF120',
 price:14.38,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.7,news5:'',dy_n:9,dy_med:7.28,div12:1.36,pe_lo:7.2,gmod:null,icr:3.7,ltv:38.2,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:0.0,irrn:11.3,irr:11.3,dq:'',vmult:null,hn:4,eveb_h:15.5,pfcf_h:7.9,pe_h:8.7,fcur:'EUR',fcfh:'291|293|262|297',nih:'185|314|3|219',revh:'544|507|462|446',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:27.13,vpess:19.73,nregu:null,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:6.9,gimp:null,knife:false,neglect:false,vmeth:'pb',nig:null,cagr:6.9,alarm:'',qwhy:'',qok:true,nde:null,fcfc:null,roicx:null,chg:-1.64,mkt:'2.0Md€',b52h:18.64,b52l:13.98,beta:0.72,
 pe:6.78,pb:0.58,ev_ebitda:13.57,ps:3.54,pfcf:8,ev_ebit:16.1,
 roe:8.7,roic:null,roa:3.2,debt:0.82,de:0.82,ic:3.3,cr:0.46,qr:0.6,
 yield:9.3,epsg:92.0,revg:-1.3,margin:52.3,gm:75.9,om:25,fcf:14.6,
 capex:0.8,capr:4.1,capda:17.68,dcfb:23.09,dcfm:24.67,dcfu:32.6,
 pio:7,alt:0.84,rsi:39.6,mm50:15.29,mm200:15.84,
 el:17.27,eh:19.73,stop:17.76,o1:27.13,o2:29.85,cb:6,ch:5,cs:3,tp:20.24,score:'A',rec:'watch',zone:true,
 moat:[['Centres commerciaux Carrefour','fort'],['Hypermarchés proximite captive','fort']],
 cats:[{t:'Carrefour trafic reprise',w:'2026',c:'var(--gn)'}],
 ins:[['Achat','Carrefour','15M€','Jan 2026']],
 peers:[{n:'Klépierre',pe:14,pb:0.8,roe:5,div:7.5,evebitda:14}],
 risks:{Commerce:65,Ecommerce:60,Taux:70,Dette:70,Liquidite:20,Carrefour:55},
 track:[{y:'2025',p:'Trafic Carrefour stable',ok:'partial'}],
 thesis:"Carmila est la fonciere des centres commerciaux autour des hypermarches Carrefour. 8.5% de dividende a 0.7x ANR. Le trafic en hypermarche est resilient — on achete toujours alimentaire meme en crise. Carrefour est actionnaire et locataire principal.",
 contra:"Ecommerce menace le commerce physique non alimentaire. Dette elevee dans un contexte de taux hauts. Carrefour = 70% du CA = concentration risque."},

{ticker:'ADP',x2:'',x2s:'',name:'Aéroports de Paris',sector:'Infrastructure aeroports',cap:'large',srd:true,idx:'Cac Next 20',
 price:108.9,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:4.8,news5:'',dy_n:7,dy_med:2.46,div12:3.8,pe_lo:18.3,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:9.7,pfcf_h:22.7,pe_h:26.4,fcur:'EUR',fcfh:'373|435|578|858',nih:'382|342|631|516',revh:'6704|6158|5495|4688',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:1.6,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:-9.5,cagr:12.7,alarm:'',qwhy:'ROIC hors EA 6.4, ROIC 6.2, dette/EBITDA 3.9',qok:false,nde:3.9,fcfc:120.0,roicx:6.4,chg:0.37,mkt:'10.53Md€',b52h:133.9,b52l:99.05,beta:0.92,
 pe:18.06,pb:2.5,ev_ebitda:9.77,ps:1.59,pfcf:0,ev_ebit:18.4,
 roe:12.8,roic:6.2,roa:3.8,debt:2.19,de:2.19,ic:3.7,cr:1.26,qr:1,
 yield:2.8,epsg:222.2,revg:1.6,margin:8.8,gm:60.6,om:0,fcf:3.5,
 capex:0,capr:18.9,capda:1.29,
 dcfb:80.21,dcfm:94.36,dcfu:113.23,
 pio:7,alt:1.19,rsi:53.5,mm50:108.69,mm200:108.3,
 el:79.26,eh:88.32,stop:69.75,o1:99.08,o2:113.23,
 cb:0,ch:0,cs:0,tp:127.66,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Etat français 50.63%)','modéré']],
 cats:[{t:'Potentiel commercial en France et à l\'international, mais négociations du nouveau Contrat de régulation économ...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}},
{ticker:'AKE',x2:'',x2s:'',name:'Arkema',sector:'Chimie specialites',cap:'mid',srd:true,idx:'Cac Next 20',
 price:55.75,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.7,news5:'',dy_n:10,dy_med:2.75,div12:3.6,pe_lo:6.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 223.0 contre 11.2 attendu)',vmult:null,hn:4,eveb_h:5.9,pfcf_h:12.4,pe_h:16.7,fcur:'EUR',fcfh:'337|360|593|766',nih:'63|354|418|965',revh:'9068|9544|9514|11550',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-33.7,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:-59.7,cagr:-7.7,alarm:'',qwhy:'ROIC hors EA 6.2, ROIC 4.2, croissance CA -7.7%',qok:false,nde:2.2,fcfc:114.0,roicx:6.2,chg:-0.71,mkt:'4.24Md€',b52h:67.05,b52l:48.3,beta:0.99,
 pe:223.0,pb:0.7,ev_ebitda:6.72,ps:0.47,pfcf:0,ev_ebit:30.4,
 roe:0.9,roic:4.2,roa:1.7,debt:0.61,de:0.61,ic:3.1,cr:1.52,qr:1,
 yield:6.4,epsg:-21.4,revg:1.3,margin:0.7,gm:17.8,om:0,fcf:8.0,
 capex:0,capr:7.3,capda:0.79,
 dcfb:55.06,dcfm:64.78,dcfu:77.74,
 pio:6,alt:1.69,rsi:48.1,mm50:57.67,mm200:56.27,
 el:53.77,eh:60.37,stop:47.32,o1:68.02,o2:77.74,
 cb:0,ch:0,cs:0,tp:62.36,
 score:'C',rec:'avoid',zone:false,
 moat:[['A évaluer','faible']],
 cats:[{t:'Résultats en nette baisse (-14%) mais meilleurs qu\'attendus ; objectif annuel de quasi-stabilité de l\'Ebitda m...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'LTA',x2:'',x2s:'',name:'Altamir',sector:'Holdings',cap:'small',srd:true,idx:'Cac Small',
 price:22.4,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.4,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:null,pfcf_h:81.8,pe_h:37.1,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:null,regn:null,regu:null,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:true,vmeth:'per',nig:null,cagr:null,alarm:'Piotroski 3/9',qwhy:'holding (grille dediee a venir)',qok:false,nde:null,fcfc:null,roicx:null,chg:0.0,mkt:'869M€',b52h:30.8,b52l:22.4,beta:0.51,
 pe:-172.31,pb:0.66,ev_ebitda:489.7,ps:57.46,pfcf:0,ev_ebit:null,
 roe:1.2,roic:null,roa:0.1,debt:0.07,de:0.07,ic:null,cr:0.17,qr:1,
 yield:4.6,epsg:0,revg:0,margin:107.0,gm:17.0,om:0,fcf:0.9,
 capex:0,capr:null,capda:null,
 dcfb:42.82,dcfm:50.38,dcfu:60.46,
 pio:3,alt:4.94,rsi:39.1,mm50:22.94,mm200:24.89,
 el:40.3,eh:46.35,stop:35.46,o1:52.9,o2:60.46,
 cb:0,ch:0,cs:0,tp:26.66,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Maurice Tchenio et sociétés apparentées 64.96%)','modéré']],
 cats:[{t:'A l\'issue de l\'OPAS, les deux actionnaires de référence détiennent plus de 85% du capital. ANR de 33,53€/actio...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}},
{ticker:'BB',x2:'',x2s:'',name:'Bic',sector:'Distribution',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:66.4,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.5,news5:'',dy_n:10,dy_med:4.51,div12:2.4,pe_lo:11.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:6.0,pfcf_h:10.1,pe_h:13.2,fcur:'EUR',fcfh:'222|271|249|204',nih:'86|212|227|199',revh:'2090|2197|2263|2234',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-13.2,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:-24.3,cagr:-2.2,alarm:'',qwhy:'croissance CA -2.2%',qok:false,nde:-0.53,fcfc:131.0,roicx:16.7,chg:-1.19,mkt:'2.46Md€',b52h:69.5,b52l:46.2,beta:-0.05,
 pe:22.98,pb:1.57,ev_ebitda:7.33,ps:1.3,pfcf:0,ev_ebit:16.8,
 roe:6.9,roic:13.1,roa:6.2,debt:0.19,de:0.19,ic:9.4,cr:2.21,qr:1,
 yield:3.6,epsg:43.0,revg:-3.5,margin:5.7,gm:50.1,om:0,fcf:8.3,
 capex:0,capr:4.1,capda:0.75,
 dcfb:52.56,dcfm:61.83,dcfu:74.2,
 pio:7,alt:4.01,rsi:51.5,mm50:66.62,mm200:58.23,
 el:51.32,eh:57.63,stop:45.16,o1:64.92,o2:74.2,
 cb:0,ch:0,cs:0,tp:68.47,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Famille Bich 47.5%)','modéré'],['Position établie sur son marché','modéré']],
 cats:[{t:'Ventes 2025 en repli de 4,7% à base comparable, marge d\'exploitation ajustée à 13,6% (-200 pb). Exercice de tr...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:35,Concurrence:30,Réglementation:25,Devise:15,Exécution:25}},
{ticker:'ATE',x2:'',x2s:'',name:'Alten',sector:'ESN ingenierie embarquee',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:85.2,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:4.9,news5:'',dy_n:9,dy_med:1.2,div12:1.5,pe_lo:8.7,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:7.5,pfcf_h:13.2,pe_h:17.3,fcur:'EUR',fcfh:'318|413|220|215',nih:'107|186|233|458',revh:'4099|4143|4069|3783',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:2,place:'Paris',mthreat:'IA, cycle automobile et aeronautique',mtype:'ingenierie externalisee, relations clients',mscore:2,near:false,gsrc:'communique 2026-10-12',gused:1.8,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:-38.4,cagr:2.7,alarm:'',qwhy:'croissance officielle 1.8%',qok:false,nde:-0.19,fcfc:118.0,roicx:29.0,chg:1.43,mkt:'2.14Md€',b52h:87.15,b52l:50.9,beta:1.18,
 pe:21.14,pb:1.29,ev_ebitda:7.95,ps:0.71,pfcf:0,ev_ebit:13.8,
 roe:6.2,roic:12.3,roa:5.6,debt:0.12,de:0.12,ic:26.2,cr:1.54,qr:1,
 yield:1.8,epsg:42.1,revg:1.2,margin:3.3,gm:18.3,om:0,fcf:10.9,
 capex:0,capr:0.3,capda:0.12,
 dcfb:94.15,dcfm:110.76,dcfu:132.91,
 pio:5,alt:2.83,rsi:68.8,mm50:75.57,mm200:64.58,
 el:84.18,eh:100.13,stop:74.08,o1:116.3,o2:132.91,
 cb:0,ch:0,cs:0,tp:101.5,
 score:'C',rec:'avoid',zone:false,
 moat:[['Position établie sur son marché','modéré']],
 cats:[{t:'Décroissance organique proche de 5% attendue sur la deuxième moitié de l\'exercice, après un premier semestre e...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'ANTIN',x2:'',x2s:'',name:'Antin Infrastructure',sector:'Holdings',cap:'mid',srd:true,idx:'Cac Small',
 price:7.25,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-3.5,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:15.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:3,eveb_h:13.5,pfcf_h:18.8,pe_h:19.1,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:null,regn:null,regu:null,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:true,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:true,vmeth:'per',nig:null,cagr:null,alarm:'',qwhy:'holding (grille dediee a venir)',qok:false,nde:null,fcfc:null,roicx:null,chg:-1.63,mkt:'1.53Md€',b52h:11.64,b52l:7.06,beta:1.13,
 pe:12.72,pb:2.82,ev_ebitda:7.72,ps:4.58,pfcf:0,ev_ebit:6.9,
 roe:21.5,roic:null,roa:14.2,debt:0.14,de:0.14,ic:31.1,cr:8.1,qr:1,
 yield:7.6,epsg:-10.3,revg:-6.5,margin:35.9,gm:64.0,om:0,fcf:9.1,
 capex:0,capr:3.6,capda:0.61,
 dcfb:5.43,dcfm:6.39,dcfu:7.67,
 pio:6,alt:8.49,rsi:38.5,mm50:8.03,mm200:9.16,
 el:5.11,eh:5.88,stop:4.5,o1:6.71,o2:7.67,
 cb:0,ch:0,cs:0,tp:10.21,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Dirigeants 55.5%)','modéré']],
 cats:[{t:'CA de 148,2M€ (+0,9%, +8% hors commissions de rattrapage). Ebitda sous-jacent en repli de 5,2% au S1.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'ELEC',x2:'',x2s:'',name:'Electricité de Strasbourg',sector:'Distribution electrique',cap:'mid',srd:true,idx:'',
 price:155.2,roiica:false,reinv:false,roiic:41.6,vmed:null,vepv:null,chg5:-0.6,news5:'',dy_n:10,dy_med:5.1,div12:13.7,pe_lo:5.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:3.2,pfcf_h:8.2,pe_h:8.0,fcur:'EUR',fcfh:'161|111|-51|70',nih:'158|150|93|55',revh:'1214|1381|1635|1256',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:20.6,gimp:null,knife:true,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:42.2,cagr:-1.1,alarm:'',qwhy:'cash 64.0%, croissance CA -1.1%',qok:false,nde:-0.82,fcfc:64.0,roicx:46.2,chg:-1.15,mkt:'1.42Md€',b52h:252.0,b52l:152.6,beta:0.46,
 pe:8.55,pb:1.73,ev_ebitda:3.47,ps:0.92,pfcf:0,ev_ebit:3.4,
 roe:20.8,roic:34.0,roa:5.8,debt:0.03,de:0.03,ic:30.7,cr:1.93,qr:1,
 yield:8.7,epsg:-33.0,revg:-7.2,margin:10.8,gm:31.8,om:0,fcf:14.4,
 capex:0,capr:7.6,capda:1.41,
 dcfb:179.52,dcfm:211.2,dcfu:253.44,
 pio:8,alt:1.72,rsi:42.7,mm50:161.74,mm200:194.32,
 el:168.96,eh:194.3,stop:148.68,o1:221.76,o2:253.44,
 cb:0,ch:0,cs:0,tp:221.98,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (EDF 88.64%)','modéré'],['Position établie sur son marché','modéré']],
 cats:[{t:'Dividende relevé de près de 25% au titre de 2025, trésorerie nette proche de 240M€.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}},
{ticker:'ERA',x2:'',x2s:'',name:'Eramet',sector:'Minéraux industriels',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:35.32,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-18.8,news5:'Gabon : Marcel Abéké, le retour aux commandes de Comilog|https://news.google.com/rss/articles/CBMihwFBVV95cUxQdWw2YkJnTnZyZXd0cmJxMnhsMkdhMWhCeTVNeUdpUnpMSGI3UUJDa0w3LUQ1ZHVIbHhxa2ZHUnZlN2Z1UmJfZ2RzSXR0N2s3ajFlcWp4SjY0dmRfRHJ2TlMxdDNVV3A1dzRMaUhIRlBvN25iZlJTQXV2SHZmQ0tJMUhTeXJ5aGc?oc=5|Infos Gabon ;; Gabon : Marcel Abéké, ex-ministre du Pétrole, devient président du conseil de Comilog|https://news.google.com/rss/articles/CBMipAFBVV95cUxQeEk2OTFmSk0yMkJBdUFTTGJJdnRkeDRJVGxENHV4VHRPT2lYNWZxOVp4SjRfOGd2YV96VnA4ekp2dTkweF9VQ2FSbV9UU01ZSHBYLUZLZUszak5sS0dMRWk5NzAxOEFMVjRrb1g3cndGNGp0MC1pYlpTb0ltS3JTb29lZHZOSzRpZFdURmRZNEh1ZGx0ODQ1Nmp4ZzVvRk42U1JyYw?oc=5|EcoMatin ;; L’action du minier Eramet en forte baisse après l’annonce de son sauvetage par l’Etat français|https://news.google.com/rss/articles/CBMisgFBVV95cUxNUW1yQWZRT0J5c1VPM05RWGplUXhBWGxUX1FEOUx6UWE2MTQtdUhKM0w5OHVuamhSRjg0SEFrZTBOMmZ1dnZtWjZBSUZfNFhYUG5CVk52TFZPTHFXd0FvTkdXSnNGNzVSMV9QeWhQeDZBY0VNdGJ5WnE4R01DbTZEaVcwNkQ4U2xDR3QxNTI5YXZlQ0poSlUwWWVncGh4MVJlaUhKS2lVeFZsSEpkSGIta2tn?oc=5|EcoMatin',dy_n:0,dy_med:null,div12:null,pe_lo:3.2,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:3,eveb_h:7.1,pfcf_h:5.9,pe_h:18.7,fcur:'EUR',fcfh:'-742|-727|-534|403',nih:'-477|14|109|740',revh:'2753|2933|3251|5102',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-18.6,gimp:null,knife:true,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:true,vmeth:'per',nig:null,cagr:-18.6,alarm:'Piotroski 3/9',qwhy:'ROIC hors EA 5.3, ROIC 5.0, cash -415.0%, dette/EBITDA 18.64, perte exploitation, croissance CA -18.6%',qok:false,nde:18.64,fcfc:-415.0,roicx:5.3,chg:-5.46,mkt:'1.19Md€',b52h:88.2,b52l:35.44,beta:0.95,
 pe:17.06,pb:2.29,ev_ebitda:20.64,ps:0.34,pfcf:0,ev_ebit:null,
 roe:-38.7,roic:5.0,roa:-0.9,debt:2.16,de:2.16,ic:-2.2,cr:2.04,qr:1,
 yield:2.8,epsg:0,revg:15.7,margin:-17.3,gm:64.6,om:0,fcf:-73.3,
 capex:0,capr:15.6,capda:0.92,
 dcfb:31.67,dcfm:37.26,dcfu:44.71,
 pio:3,alt:0.51,rsi:27.0,mm50:44.32,mm200:52.54,
 el:30.93,eh:34.73,stop:27.22,o1:39.12,o2:44.71,
 cb:0,ch:0,cs:0,tp:50.67,
 score:'D',rec:'avoid',zone:false,
 moat:[['A évaluer','faible']],
 cats:[{t:'CA ajusté T1 de 840M€ (+13%). Levée de fonds de 500M€ envisagée, soumise à l\'AG de fin mai.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'RF',x2:'',x2s:'',name:'Eurazeo',sector:'Holdings',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:45.58,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.2,news5:'',dy_n:9,dy_med:3.21,div12:2.92,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:2,eveb_h:4.7,pfcf_h:63.7,pe_h:5.1,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:null,regn:null,regu:null,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:null,cagr:null,alarm:'',qwhy:'holding (grille dediee a venir)',qok:false,nde:null,fcfc:null,roicx:null,chg:0.57,mkt:'3.3Md€',b52h:60.85,b52l:37.54,beta:1.2,
 pe:5.29,pb:0.48,ev_ebitda:-1484.39,ps:8.2,pfcf:0,ev_ebit:null,
 roe:-1.8,roic:null,roa:-0.0,debt:0.26,de:0.26,ic:-5.0,cr:0.29,qr:1,
 yield:6.4,epsg:0,revg:-27,margin:-28.8,gm:70.2,om:0,fcf:4.2,
 capex:0,capr:1.2,capda:0.16,
 dcfb:63.92,dcfm:75.2,dcfu:90.24,
 pio:5,alt:0.71,rsi:44.9,mm50:47.94,mm200:45.09,
 el:60.16,eh:69.18,stop:52.94,o1:78.96,o2:90.24,
 cb:0,ch:0,cs:0,tp:71.73,
 score:'C',rec:'avoid',zone:false,
 moat:[['Position établie sur son marché','modéré']],
 cats:[{t:'Collecte de 1,1Md€ au T1 (+11%), tirée par la dette privée. Actifs sous gestion à 39,2Md€.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:35,Concurrence:30,Réglementation:25,Devise:15,Exécution:25}},
{ticker:'ETL',x2:'',x2s:'',name:'Eutelsat Communications',sector:'Télécoms',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:1.74,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:23.1,news5:'Eutelsat s’ecroule de -10% alors que l’effet Starlink s’évapore: opportunité ou piège?|https://news.google.com/rss/articles/CBMi0AFBVV95cUxPZ1ZUOHRxSHQxU3pabzhFR011cnpSNVF0Wmp6QzJoVzlxUlNvSWxOSVJrTUQ1aDhtT3FaQ0lNM0RwZGJ5RmUyRURJNWpQTEVLdmZCY1NiRUhqV0pycGRZWjN2ZGItUmZNTXFGUk1RSE82Nk5DVFBOejhEeEZfRk9DLThhdDZEd0xkTEpCSFJKWld3NTAtbDJVTklMbTVTejlCZ09qbjV2RE8wZ0Nab1hpbEJOajVYU3lCUi1JNmRuVDhtQWhqR1NkaVJQRVFILWs4?oc=5|Investing.com France ;; Eutelsat s’envole de +23% grâce à Starlink : Faut-il prendre le train en marche ?|https://news.google.com/rss/articles/CBMiywFBVV95cUxQRHZzenBubWhlR1JYazczR3NzNzVKR0lzVUlhNmJzeDU2ME5BT3Exa2hQeldhWHpsQ1Y0UHRtVTBWVHhvM0lvTGpNTy01c2JoblZGdkZTdXp0SW5NUmE2VUhDUUJsRmxTMmdxWWVOQTEyRHhXYlM2R24xN2IzWnRtMW9nUHdZNHhmcEJhU29vTjY3XzNOUmJvLXZydXpaV2dsekhHM3EwWlVDQ3NubGpJNjJ0TEVKR1hDZnprNE9obFNzbTlIWS1zMzhESQ?oc=5|Investing.com France ;; Action Eutelsat : analyse du T1, d’OneWeb et d’IRIS²|https://news.google.com/rss/articles/CBMilwFBVV95cUxQVGlJc0JRVDY1NnlldVlmemE5RW1zT2FvTmdCVHBBQnJwcVZJT1M0YzljX0ViOEVSZjRTWGxTaUhxTVlwalN6dks3ZTBYdzF3ZHJObFpMQzVxWmxPSmJ3VWxZUFg1MUJrMU1hZzRvUU5XVFY1TEk5eHdvX2c2MHc4d1dtdkJWVlVRR0VTU0dsMFJFYmdsM09j?oc=5|Admirals',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:8.0,pfcf_h:28.8,pe_h:6.1,fcur:'EUR',fcfh:'-32|-6|42|534',nih:'-457|-1082|-310|315',revh:'1236|1244|1213|1131',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:3.0,gimp:null,knife:true,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:null,cagr:3.0,alarm:'',qwhy:'ROIC hors EA -3.9, ROIC -3.2, cash None%, dette/EBITDA 2.74, perte exploitation',qok:false,nde:2.74,fcfc:null,roicx:-3.9,chg:-1.61,mkt:'2.37Md€',b52h:4.56,b52l:1.35,beta:0.23,
 pe:-15.33,pb:0.57,ev_ebitda:5.78,ps:1.66,pfcf:0,ev_ebit:null,
 roe:-14.5,roic:-3.2,roa:-0.2,debt:0.86,de:0.86,ic:-1.6,cr:2.87,qr:1,
 yield:0,epsg:0,revg:1.1,margin:-37.0,gm:80.6,om:0,fcf:-1.6,
 capex:0,capr:43.8,capda:0.68,
 dcfb:0,dcfm:0,dcfu:0,
 pio:5,alt:0.55,rsi:54.9,mm50:1.77,mm200:2.29,
 el:0,eh:0,stop:0,o1:0,o2:0,
 cb:0,ch:0,cs:0,tp:1.91,
 score:'D',rec:'avoid',zone:false,
 moat:[['A évaluer','faible']],
 cats:[{t:'CA activités opérationnelles stable attendu, croissance Leo de 50%, marge Ebitda ajustée légèrement inférieure...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'EXA',x2:'',x2s:'',name:'Exail Technologies',sector:'Drones civils defense',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:125.7,roiica:true,reinv:false,roiic:7.3,vmed:null,vepv:null,chg5:0.6,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'croissance Yahoo 38.5 %/an : probablement faussee par une acquisition ou une cession',vmult:null,hn:2,eveb_h:12.1,pfcf_h:12.6,pe_h:19.5,fcur:'EUR',fcfh:'65|57|24|29',nih:'3|-4|17|-8',revh:'479|373|323|180',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:38.5,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:null,cagr:38.5,alarm:'',qwhy:'ROIC hors EA 9.7, ROIC 5.2',qok:false,nde:0.52,fcfc:2161.0,roicx:9.7,chg:0.08,mkt:'2.12Md€',b52h:159.2,b52l:70.7,beta:1.13,
 pe:31.96,pb:-9.96,ev_ebitda:35.8,ps:4.0,pfcf:0,ev_ebit:61.9,
 roe:31.2,roic:5.2,roa:1.9,debt:1.44,de:1.44,ic:1.2,cr:1.99,qr:1,
 yield:0,epsg:866,revg:24.7,margin:15.5,gm:49.9,om:0,fcf:3.0,
 capex:0,capr:7.3,capda:null,
 dcfb:66.86,dcfm:78.66,dcfu:94.39,
 pio:7,alt:2.41,rsi:60.9,mm50:124.62,mm200:121.59,
 el:66.07,eh:73.63,stop:58.14,o1:82.59,o2:94.39,
 cb:0,ch:0,cs:0,tp:137.67,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Famille Gorgé 41.4%)','modéré']],
 cats:[{t:'Rachat par Thales à 134€/action, après négociation avec Safran (offre à 128,50€).',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}},
{ticker:'EXENS',x2:'',x2s:'',name:'Exosens',sector:'Connecteurs RF defense',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:59.1,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.1,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 140.7 contre 24.0 attendu)',vmult:null,hn:2,eveb_h:13.6,pfcf_h:17.0,pe_h:53.2,fcur:'EUR',fcfh:'107|99|50|26',nih:'31|43|18|11',revh:'383|468|292|201',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',mthreat:'dependance aux budgets de defense, niche',mtype:'leader des tubes intensificateurs de lumiere (vision nocturne)',mscore:3,near:false,gsrc:'communique 2026-10-12',gused:11.4,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:39.9,cagr:24.1,alarm:'Piotroski 4/9',qwhy:'ROIC 11.9',qok:false,nde:-0.43,fcfc:274.0,roicx:25.3,chg:-0.59,mkt:'3.16Md€',b52h:74.0,b52l:40.0,beta:0.81,
 pe:140.71,pb:6.67,ev_ebitda:30.77,ps:5.97,pfcf:0,ev_ebit:40.0,
 roe:12.7,roic:11.9,roa:6.2,debt:0.6,de:0.6,ic:null,cr:2.35,qr:1,
 yield:0.5,epsg:-45.1,revg:15.3,margin:6.0,gm:60.1,om:0,fcf:3.6,
 capex:0,capr:null,capda:null,
 dcfb:67.03,dcfm:78.86,dcfu:94.63,
 pio:4,alt:5.11,rsi:51.7,mm50:59.22,mm200:60.11,
 el:56.78,eh:70.03,stop:49.97,o1:82.8,o2:94.63,
 cb:0,ch:0,cs:0,tp:69.7,
 score:'C',rec:'avoid',zone:false,
 moat:[['Position établie sur son marché','modéré']],
 cats:[{t:'CA 2026 attendu entre 520 et 540M€, Ebitda ajusté 168-178M€. Croissance organique visée jusqu\'à 15% à moyen te...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}},
{ticker:'FDJU',x2:'',x2s:'',name:'FDJ',sector:'Distribution',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:21.33,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.4,news5:'',dy_n:6,dy_med:3.73,div12:2.1,pe_lo:14.7,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'benefice 12 mois anormal (PER 164.1 contre 8.1 attendu)',vmult:null,hn:4,eveb_h:9.6,pfcf_h:14.2,pe_h:20.2,fcur:'EUR',fcfh:'568|427|504|302',nih:'176|399|425|308',revh:'3678|3065|2622|2461',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'communique 2026-10-05',gused:-1.0,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:-17.0,cagr:14.3,alarm:'',qwhy:'croissance officielle -1.0%',qok:false,nde:1.8,fcfc:138.0,roicx:32.0,chg:-0.97,mkt:'4.15Md€',b52h:26.75,b52l:20.33,beta:0.66,
 pe:164.08,pb:6.81,ev_ebitda:5.55,ps:1.1,pfcf:0,ev_ebit:15.2,
 roe:3.2,roic:25.3,roa:5.7,debt:3.83,de:3.83,ic:5.1,cr:0.55,qr:1,
 yield:9.8,epsg:19,revg:-4.5,margin:0.7,gm:41.9,om:0,fcf:14.4,
 capex:0,capr:7.3,capda:0.53,
 dcfb:27.8,dcfm:32.71,dcfu:39.25,
 pio:7,alt:1.36,rsi:49.1,mm50:21.77,mm200:22.33,
 el:27.15,eh:30.49,stop:23.89,o1:34.35,o2:39.25,
 cb:0,ch:0,cs:0,tp:25.93,
 score:'C',rec:'avoid',zone:false,
 moat:[['A évaluer','faible']],
 cats:[{t:'Objectifs de CA et marge 2026 revus en baisse (fiscalité, réglementation). Rendement élevé et sécurisé.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'GFC',x2:'',x2s:'',name:'Gecina',sector:'Immobilier bureaux Paris',cap:'large',srd:true,idx:'Cac Next 20',
 price:62.1,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.6,news5:'',dy_n:10,dy_med:4.28,div12:5.5,pe_lo:13.3,gmod:null,icr:6.9,ltv:37.8,bvg:null,roemin:null,roem:null,grid:'fonciere',wht:0.0,irrn:10.7,irr:10.7,dq:'benefice 12 mois anormal (PER 28.5 contre 9.3 attendu)',vmult:null,hn:3,eveb_h:31.9,pfcf_h:56.3,pe_h:21.4,fcur:'EUR',fcfh:'-491|145|144|115',nih:'448|310|-1787|170',revh:'859|843|836|765',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:150.84,vpess:109.7,nregu:null,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:3.9,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'pb',nig:null,cagr:3.9,alarm:'',qwhy:'',qok:true,nde:null,fcfc:null,roicx:null,chg:-1.27,mkt:'5.68Md€',b52h:83.55,b52l:58.9,beta:1.05,
 pe:28.49,pb:0.45,ev_ebitda:18.47,ps:5.19,pfcf:0,ev_ebit:21.1,
 roe:1.6,roic:null,roa:2.1,debt:0.7,de:0.7,ic:5.8,cr:0.27,qr:1,
 yield:8.7,epsg:-99.0,revg:4.1,margin:18.4,gm:79.1,om:0,fcf:-10.7,
 capex:0,capr:113.0,capda:95.8,
 dcfb:71.31,dcfm:137.13,dcfu:100.68,
 pio:8,alt:0.43,rsi:42.4,mm50:66.48,mm200:69.45,
 el:95.99,eh:109.7,stop:98.73,o1:150.84,o2:165.93,
 cb:0,ch:0,cs:0,tp:85.73,
 score:'B',rec:'watch',zone:true,
 moat:[['Position établie sur son marché','modéré']],
 cats:[{t:'Décote sur ANR de 142,35€ (fin juin 2026). Bénéfice net récurrent visé entre 6,70 et 6,75€/action.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:35,Concurrence:30,Réglementation:25,Devise:15,Exécution:25}},
{ticker:'GET',x2:'',x2s:'',name:'Getlink',sector:'Ferroviaire',cap:'large',srd:true,idx:'Cac Next 20',
 price:19.06,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.3,news5:'',dy_n:9,dy_med:2.62,div12:0.8,pe_lo:26.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:22.6,pfcf_h:11.0,pe_h:27.2,fcur:'EUR',fcfh:'624|710|892|939',nih:'320|317|326|252',revh:'1595|1614|1829|1606',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:4.1,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:8.3,cagr:-0.2,alarm:'',qwhy:'ROIC hors EA 8.0, ROIC 7.9, dette/EBITDA 6.8, croissance CA -0.2%',qok:false,nde:6.8,fcfc:260.0,roicx:8.0,chg:-0.68,mkt:'10.38Md€',b52h:19.85,b52l:15.06,beta:0.53,
 pe:31.77,pb:4.23,ev_ebitda:16.37,ps:5.98,pfcf:0,ev_ebit:26.1,
 roe:13.3,roic:7.9,roa:4.7,debt:2.17,de:2.17,ic:2.4,cr:2.69,qr:1,
 yield:4.2,epsg:4.4,revg:10.8,margin:18.8,gm:51.8,om:0,fcf:6.0,
 capex:0,capr:12.0,capda:null,
 dcfb:9.86,dcfm:11.6,dcfu:13.92,
 pio:7,alt:1.71,rsi:59.3,mm50:18.71,mm200:17.92,
 el:9.51,eh:10.76,stop:8.37,o1:12.18,o2:13.92,
 cb:0,ch:0,cs:0,tp:19.82,
 score:'C',rec:'avoid',zone:false,
 moat:[['Position établie sur son marché','modéré']],
 cats:[{t:'Prévisions annuelles d\'Ebitda relevées après un bon S1, porté par Eleclink. Nouvelles lignes grande vitesse vi...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:35,Concurrence:30,Réglementation:25,Devise:15,Exécution:25}},
{ticker:'DEC',x2:'',x2s:'',name:'JCDecaux',sector:'Publicite communication',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:25.02,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.0,news5:'',dy_n:5,dy_med:2.13,div12:0.65,pe_lo:12.4,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.3,pfcf_h:4.5,pe_h:15.5,fcur:'EUR',fcfh:'878|811|728|748',nih:'263|259|209|132',revh:'3673|3633|3296|3074',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:15.9,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:25.7,cagr:6.1,alarm:'',qwhy:'ROIC hors EA 9.6, ROIC 6.7',qok:false,nde:2.03,fcfc:367.0,roicx:9.6,chg:-3.25,mkt:'4.7Md€',b52h:26.06,b52l:14.12,beta:1.0,
 pe:16.35,pb:2.31,ev_ebitda:10.04,ps:1.42,pfcf:0,ev_ebit:16.8,
 roe:16.1,roic:6.7,roa:3.7,debt:1.61,de:1.61,ic:3.4,cr:1.15,qr:1,
 yield:2.5,epsg:85.5,revg:3.8,margin:8.7,gm:51.7,om:0,fcf:16.5,
 capex:0,capr:8.3,capda:0.38,
 dcfb:14.92,dcfm:17.55,dcfu:21.06,
 pio:8,alt:1.28,rsi:53.7,mm50:24.4,mm200:19.99,
 el:14.74,eh:16.43,stop:12.97,o1:18.43,o2:21.06,
 cb:0,ch:0,cs:0,tp:27.33,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (JCDecaux Holding 65.46%)','modéré'],['Position établie sur son marché','modéré']],
 cats:[{t:'Fin d\'année 2025 solide, T1 très solide (+5,7% organique) mais attentes T2 revues à ~3% (guerre en Iran).',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:35,Concurrence:30,Réglementation:25,Devise:15,Exécution:25}},
{ticker:'MMB',x2:'',x2s:'',name:'Lagardère',sector:'Médias',cap:'mid',srd:true,idx:'Cac Small',
 price:18.48,roiica:false,reinv:false,roiic:19.6,vmed:null,vepv:null,chg5:2.0,news5:'',dy_n:8,dy_med:5.03,div12:0.67,pe_lo:13.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.9,pfcf_h:3.2,pe_h:17.1,fcur:'EUR',fcfh:'1076|995|711|545',nih:'203|168|144|161',revh:'9423|8999|8131|6977',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:9.2,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:8.0,cagr:10.5,alarm:'',qwhy:'ROIC hors EA 9.3, ROIC 6.1, dette/EBITDA 3.13',qok:false,nde:3.13,fcfc:492.0,roicx:9.3,chg:0.76,mkt:'2.54Md€',b52h:20.4,b52l:16.96,beta:0.82,
 pe:12.57,pb:3.02,ev_ebitda:7.61,ps:0.28,pfcf:0,ev_ebit:12.1,
 roe:27.8,roic:6.1,roa:4.3,debt:5.0,de:5.0,ic:2.5,cr:0.78,qr:1,
 yield:3.6,epsg:23.7,revg:1.7,margin:2.2,gm:41.9,om:0,fcf:40.7,
 capex:0,capr:2.7,capda:0.31,
 dcfb:18.07,dcfm:21.26,dcfu:25.51,
 pio:9,alt:1.25,rsi:58.2,mm50:18.36,mm200:18.27,
 el:17.86,eh:19.9,stop:15.72,o1:22.32,o2:25.51,
 cb:0,ch:0,cs:0,tp:27.17,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Louis Hachette Group 66.53%)','modéré']],
 cats:[{t:'Activités bien orientées au T1 2026, portées par Travel Retail (+4,8%) et Live (+5,8%).',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'LOUP',x2:'',x2s:'',name:'LDC',sector:'Agroalimentaire',cap:'mid',srd:true,idx:'',
 price:101.6,roiica:false,reinv:false,roiic:13.2,vmed:null,vepv:null,chg5:2.5,news5:'',dy_n:10,dy_med:1.64,div12:2.25,pe_lo:7.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:4.2,pfcf_h:12.6,pe_h:9.4,fcur:'EUR',fcfh:'256|113|197|248',nih:'321|244|304|225',revh:'7283|6323|6198|5846',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:10.1,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:12.7,cagr:7.6,alarm:'',qwhy:'ROIC hors EA 13.7, ROIC 11.6, cash 74.0%',qok:false,nde:0.36,fcfc:74.0,roicx:13.7,chg:1.4,mkt:'4.11Md€',b52h:127.4,b52l:84.2,beta:0.49,
 pe:11.09,pb:1.36,ev_ebitda:4.65,ps:0.49,pfcf:0,ev_ebit:7.4,
 roe:13.3,roic:11.6,roa:6.1,debt:0.28,de:0.28,ic:25.0,cr:1.41,qr:1,
 yield:2.2,epsg:54.5,revg:14.8,margin:4.4,gm:32.5,om:0,fcf:7.2,
 capex:0,capr:5.2,capda:1.26,
 dcfb:97.39,dcfm:114.58,dcfu:137.5,
 pio:7,alt:3.03,rsi:40.1,mm50:106.66,mm200:105.32,
 el:96.25,eh:107.25,stop:84.7,o1:120.31,o2:137.5,
 cb:0,ch:0,cs:0,tp:137.75,
 score:'C',rec:'avoid',zone:false,
 moat:[['Position établie sur son marché','modéré']],
 cats:[{t:'Croissance solide l\'an dernier, objectif de 7Mds€ de CA et 560M€ d\'Ebitda dépassé.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'MMT',x2:'',x2s:'',name:'M6',sector:'Médias',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:10.14,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.2,news5:'',dy_n:9,dy_med:6.74,div12:1.25,pe_lo:7.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:4.2,pfcf_h:9.8,pe_h:10.1,fcur:'EUR',fcfh:'65|131|222|220',nih:'123|173|234|162',revh:'1256|1311|1316|1357',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:0,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-5.6,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:true,vmeth:'per',nig:-8.6,cagr:-2.6,alarm:'',qwhy:'croissance CA -2.6%',qok:false,nde:-0.37,fcfc:92.0,roicx:23.6,chg:-1.93,mkt:'1.51Md€',b52h:13.04,b52l:9.76,beta:0.67,
 pe:12.68,pb:1.09,ev_ebitda:8.32,ps:1.01,pfcf:0,ev_ebit:8.4,
 roe:6.9,roic:16.7,roa:4.8,debt:0.08,de:0.08,ic:51.7,cr:1.6,qr:1,
 yield:12.1,epsg:-38.7,revg:1.8,margin:7.9,gm:20.5,om:0,fcf:5.1,
 capex:0,capr:5.9,capda:0.56,
 dcfb:13.06,dcfm:15.36,dcfu:18.43,
 pio:5,alt:2.4,rsi:31.3,mm50:11.34,mm200:11.31,
 el:12.9,eh:14.38,stop:11.35,o1:16.13,o2:18.43,
 cb:0,ch:0,cs:0,tp:12.34,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (RTL Group 48.3%)','modéré']],
 cats:[{t:'CA en repli de 5,5% au T1 dans un marché publicitaire complexe, mais bonne dynamique streaming.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'NRO',x2:'',x2s:'',name:'Neurones',sector:'Services informatiques',cap:'small',srd:true,idx:'Cac Small',
 price:36.75,roiica:false,reinv:false,roiic:null,vmed:39.68,vepv:35.8,chg5:0.3,news5:'',dy_n:10,dy_med:1.8,div12:1.4,pe_lo:19.6,gmod:5.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:9.0,irr:9.0,dq:'',vmult:41.48,hn:4,eveb_h:7.6,pfcf_h:18.2,pe_h:21.0,fcur:'EUR',fcfh:'61|72|54|44',nih:'52|53|49|44',revh:'857|810|741|665',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:44.45,vpess:32.74,nregu:2,regn:3,regu:3,place:'Paris',mthreat:'IA qui reduit les jours factures (cas Wavestone)',mtype:'services informatiques, relations clients et diversification',mscore:2,near:false,gsrc:'communique 2026-10-05',gused:5.05,gimp:3.0,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'qarp',nig:5.6,cagr:8.8,alarm:'',qwhy:'',qok:true,nde:-2.86,fcfc:117.0,roicx:148.5,chg:-0.54,mkt:'852M€',b52h:45.0,b52l:31.9,beta:0.46,
 pe:16.12,pb:2.33,ev_ebitda:7.25,ps:0.99,pfcf:0,ev_ebit:7.8,
 roe:15.3,roic:62.1,roa:7.1,debt:0.1,de:0.1,ic:49.3,cr:2.23,qr:1,
 yield:3.8,epsg:15.1,revg:7.2,margin:6.2,gm:49.6,om:0,fcf:6.9,
 capex:0,capr:1.2,capda:0.53,
 dcfb:33.73,dcfm:39.68,dcfu:47.62,
 pio:8,alt:4.05,rsi:53.6,mm50:36.68,mm200:36.1,
 el:29.76,eh:33.73,stop:29.47,o1:44.45,o2:48.9,
 cb:0,ch:0,cs:0,tp:39.2,
 score:'B',rec:'watch',zone:false,
 moat:[['Actionnariat stable (L. de Chammard 59.6%)','modéré'],['Position établie sur son marché','modéré']],
 cats:[{t:'Facturations en hausse de 4,7% en organique sur 9 mois, secteur ESN encore peu dynamique.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}},
{ticker:'OVH',x2:'',x2s:'',name:'OVHcloud',sector:'Industrie digitale',cap:'mid',srd:true,idx:'Cac Small',
 price:14.82,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-4.7,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:0,eveb_h:8.3,pfcf_h:46.6,pe_h:null,fcur:'EUR',fcfh:'|25|-28|-179',nih:'|-10|-40|-29',revh:'|993|897|788',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:2,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:12.3,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:null,cagr:12.3,alarm:'',qwhy:'ROIC hors EA -0.6, ROIC -0.5, cash None%, dette/EBITDA None',qok:false,nde:null,fcfc:null,roicx:-0.6,chg:0.34,mkt:'2.27Md€',b52h:18.74,b52l:6.67,beta:1.09,
 pe:50.49,pb:82.33,ev_ebitda:11.31,ps:2.03,pfcf:0,ev_ebit:null,
 roe:-2.2,roic:-0.5,roa:2.2,debt:49.27,de:49.27,ic:null,cr:0.36,qr:1,
 yield:0,epsg:2400,revg:1.9,margin:-0.1,gm:73.4,om:0,fcf:null,
 capex:0,capr:null,capda:null,
 dcfb:6.49,dcfm:7.63,dcfu:9.16,
 pio:6,alt:0,rsi:38.6,mm50:15.85,mm200:12.76,
 el:5.8,eh:6.9,stop:5.1,o1:8.01,o2:9.16,
 cb:0,ch:0,cs:0,tp:13.5,
 score:'C',rec:'avoid',zone:false,
 moat:[['A évaluer','faible']],
 cats:[{t:'Croissance annuelle de 5-7% du CA visée en 2026, marge d\'excédent brut supérieure à 2025.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:35,Concurrence:30,Réglementation:25,Devise:15,Exécution:25}},
{ticker:'PLNW',x2:'',x2s:'',name:'Planisware',sector:'SaaS industrie PLM CAO',cap:'mid',srd:true,idx:'Cac Small',
 price:26.85,roiica:false,reinv:false,roiic:130.7,vmed:21.27,vepv:9.52,chg5:5.7,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:10.2,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:7.4,irr:7.4,dq:'',vmult:21.27,hn:2,eveb_h:24.8,pfcf_h:30.5,pe_h:38.3,fcur:'EUR',fcfh:'63|54|42|29',nih:'50|43|42|32',revh:'198|183|156|132',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:22.99,vpess:13.26,nregu:3,regn:3,regu:3,place:'Paris',mthreat:'petite taille face a Microsoft/Oracle/SAP',mtype:'logiciel de gestion de portefeuilles projets, couts de changement',mscore:3,near:false,gsrc:'communique 2026-10-05',gused:10.15,gimp:16.2,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'qarp',nig:16.6,cagr:14.5,alarm:'',qwhy:'',qok:true,nde:-2.54,fcfc:113.0,roicx:280.6,chg:3.67,mkt:'1.4Md€',b52h:26.85,b52l:13.7,beta:1.03,
 pe:33.15,pb:8.88,ev_ebitda:24.9,ps:8.92,pfcf:0,ev_ebit:26.4,
 roe:28.1,roic:130.2,roa:12.6,debt:0.09,de:0.09,ic:138.1,cr:2.52,qr:1,
 yield:1.4,epsg:32.6,revg:10.8,margin:27.3,gm:73.7,om:0,fcf:3.4,
 capex:0,capr:3.1,capda:0.7,
 dcfb:18.22,dcfm:21.44,dcfu:25.73,
 pio:8,alt:11.81,rsi:66.5,mm50:24.55,mm200:19.85,
 el:15.01,eh:17.15,stop:11.93,o1:22.99,o2:25.29,
 cb:0,ch:0,cs:0,tp:25.36,
 score:'B',rec:'hold',zone:false,
 moat:[['Actionnariat stable (Olhanda 65%)','modéré'],['Position établie sur son marché','modéré']],
 cats:[{t:'Logiciel et services cloud de gestion de portefeuille de projets pour entreprises.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:35,Concurrence:30,Réglementation:25,Devise:15,Exécution:25}},
{ticker:'GDS',x2:'',x2s:'',name:'Ramsay Générale de Santé',sector:'Santé services',cap:'mid',srd:true,idx:'Cac Small',
 price:9.44,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-4.5,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:8.8,pfcf_h:3.7,pe_h:45.6,fcur:'EUR',fcfh:'381|551|418|427',nih:'-48|-54|-54|49',revh:'5381|5208|5006|4702',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:4.6,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:true,vmeth:'per',nig:null,cagr:4.6,alarm:'',qwhy:'ROIC hors EA 4.7, ROIC 2.7, cash None%, dette/EBITDA 5.97',qok:false,nde:5.97,fcfc:null,roicx:4.7,chg:-0.63,mkt:'1.19Md€',b52h:11.55,b52l:8.72,beta:0.29,
 pe:0,pb:0.88,ev_ebitda:7.46,ps:0.19,pfcf:0,ev_ebit:25.4,
 roe:-2.3,roic:2.7,roa:1.8,debt:3.49,de:3.49,ic:1.0,cr:0.78,qr:1,
 yield:0,epsg:0,revg:921,margin:-0.9,gm:27.8,om:0,fcf:36.5,
 capex:0,capr:2.7,capda:0.33,
 dcfb:0,dcfm:0,dcfu:0,
 pio:6,alt:0.94,rsi:29.8,mm50:10.39,mm200:10.56,
 el:0,eh:0,stop:0,o1:0,o2:0,
 cb:0,ch:0,cs:0,tp:12.04,
 score:'D',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Ramsay Healthcare 52.8%)','modéré']],
 cats:[{t:'CA groupe hospitalier de 4Mds€ sur 9 mois (+3%), marge Ebitda 11,6% (gains de productivité).',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'RBT',x2:'',x2s:'',name:'Robertet',sector:'Chimie specialites',cap:'mid',srd:true,idx:'Cac Small',
 price:777.0,roiica:false,reinv:true,roiic:28.8,vmed:781.89,vepv:495.08,chg5:1.0,news5:'',dy_n:10,dy_med:1.0,div12:12.0,pe_lo:17.8,gmod:5.8,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:0.0,irrn:8.5,irr:8.5,dq:'',vmult:891.09,hn:4,eveb_h:13.0,pfcf_h:25.9,pe_h:21.4,fcur:'EUR',fcfh:'67|74|84|24',nih:'103|90|75|76',revh:'844|808|721|703',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:842.86,vpess:665.11,nregu:2,regn:3,regu:3,place:'Paris',mthreat:'taille, concurrence des grands du secteur',mtype:'leader des matieres premieres naturelles pour la parfumerie',mscore:3,near:true,gsrc:'communique 2026-10-12',gused:5.8,gimp:5.5,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'qarp',nig:10.8,cagr:6.3,alarm:'',qwhy:'cash 72.0% mais reinvesti a 28.8% (regle reinvestissement)',qok:false,nde:0.52,fcfc:72.0,roicx:16.1,chg:0.13,mkt:'1.58Md€',b52h:922.0,b52l:710.0,beta:0.37,
 pe:17.44,pb:2.52,ev_ebitda:10.74,ps:1.94,pfcf:0,ev_ebit:11.7,
 roe:16.6,roic:14.2,roa:8.0,debt:0.4,de:0.4,ic:17.7,cr:2.87,qr:1,
 yield:1.6,epsg:-9.6,revg:-0.5,margin:11.8,gm:59.5,om:0,fcf:4.1,
 capex:0,capr:5.2,capda:1.47,
 dcfb:664.61,dcfm:781.89,dcfu:938.27,
 pio:8,alt:4.12,rsi:56.2,mm50:774.76,mm200:805.97,
 el:586.42,eh:664.61,stop:598.6,o1:842.86,o2:927.15,
 cb:0,ch:0,cs:0,tp:928.25,
 score:'C',rec:'avoid',zone:false,
 moat:[['A évaluer','faible']],
 cats:[{t:'Résultats 2025 avec rentabilité améliorée (+14,8% bénéfice net) et dividende +20%.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'RUI',x2:'',x2s:'',name:'Rubis',sector:'Distribution',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:36.26,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:4.9,news5:'',dy_n:10,dy_med:4.82,div12:2.07,pe_lo:6.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:5.7,pfcf_h:8.8,pe_h:8.4,fcur:'EUR',fcfh:'359|417|279|163',nih:'309|342|354|263',revh:'6534|6644|6630|7135',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:1.3,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:5.5,cagr:-2.9,alarm:'',qwhy:'ROIC 9.5, croissance CA -2.9%',qok:false,nde:1.84,fcfc:96.0,roicx:15.9,chg:2.6,mkt:'3.38Md€',b52h:37.08,b52l:30.0,beta:0.86,
 pe:11.16,pb:1.32,ev_ebitda:8.3,ps:0.51,pfcf:0,ev_ebit:11.3,
 roe:12.0,roic:9.5,roa:5.0,debt:0.82,de:0.82,ic:5.4,cr:1.37,qr:1,
 yield:5.9,epsg:17.1,revg:24.2,margin:4.6,gm:25.0,om:0,fcf:9.6,
 capex:0,capr:5.8,capda:1.29,
 dcfb:37.93,dcfm:44.62,dcfu:53.54,
 pio:6,alt:2.01,rsi:64.4,mm50:34.61,mm200:33.1,
 el:37.03,eh:41.59,stop:32.59,o1:46.85,o2:53.54,
 cb:0,ch:0,cs:0,tp:40.27,
 score:'C',rec:'avoid',zone:false,
 moat:[['Position établie sur son marché','modéré']],
 cats:[{t:'Solidité des résultats et pérennité du dividende confirmées ; tensions persistantes entre actionnaire et géran...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'DIM',x2:'',x2s:'',name:'Sartorius Stedim Biotech',sector:'Sante materiel medical',cap:'large',srd:true,idx:'Cac Next 20',
 price:211.8,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.5,news5:'',dy_n:10,dy_med:0.41,div12:0.69,pe_lo:31.8,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:28.3,pfcf_h:74.3,pe_h:73.7,fcur:'EUR',fcfh:'299|475|273|182',nih:'266|175|310|876',revh:'2968|2780|2776|3493',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-19.0,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:-32.8,cagr:-5.3,alarm:'',qwhy:'ROIC hors EA 11.5, ROIC 6.2, cash 76.0%, dette/EBITDA 2.62, croissance CA -5.3%',qok:false,nde:2.62,fcfc:76.0,roicx:11.5,chg:-1.49,mkt:'16.28Md€',b52h:225.0,b52l:150.0,beta:1.1,
 pe:70.37,pb:4.84,ev_ebitda:28.22,ps:6.86,pfcf:0,ev_ebit:44.9,
 roe:7.1,roic:6.2,roa:4.4,debt:0.57,de:0.57,ic:3.7,cr:1.16,qr:1,
 yield:0.3,epsg:37.1,revg:2.8,margin:9.7,gm:44.9,om:0,fcf:1.5,
 capex:0,capr:13.3,capda:1.24,
 dcfb:122.74,dcfm:144.4,dcfu:173.28,
 pio:8,alt:4.26,rsi:54.0,mm50:199.42,mm200:182.05,
 el:101.08,eh:127.07,stop:88.95,o1:151.62,o2:173.28,
 cb:0,ch:0,cs:0,tp:237.29,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Sartorius AG 71.5%)','modéré']],
 cats:[{t:'Croissance jugée décevante au T2, sanctionnée en Bourse ; société dans le milieu de son objectif annuel confir...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'SCR',x2:'',x2s:'',name:'Scor',sector:'Assurance',cap:'large',srd:true,idx:'Cac Next 20',
 price:33.46,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:2.4,news5:'',dy_n:9,dy_med:5.42,div12:1.9,pe_lo:null,gmod:null,nih:'851|4|812|-1383',yrs:'2025|2024|2023|2022',icr:null,ltv:null,bvg:0.8,roemin:-32.0,roem:8.7,grid:'banque',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:3,eveb_h:null,pfcf_h:4.7,pe_h:5.9,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:null,cagr:null,alarm:'',qwhy:'rentabilite fonds propres 8.7%, pire annee -32.0%, perte sur 4 ans, croissance actif net 0.8%',qok:false,nde:null,fcfc:null,roicx:null,chg:-0.89,mkt:'6.07Md€',b52h:35.3,b52l:25.3,beta:0.53,
 pe:7.4,pb:1.36,ev_ebitda:5.72,ps:0.39,pfcf:0,ev_ebit:6.0,
 roe:13.0,roic:null,roa:2.2,debt:0.52,de:0.52,ic:10.9,cr:3.96,qr:1,
 yield:5.6,epsg:-23.6,revg:-4.9,margin:5.4,gm:11.2,om:0,fcf:18.9,
 capex:0,capr:0.3,capda:0.15,
 dcfb:32.21,dcfm:37.89,dcfu:45.47,
 pio:5,alt:0.68,rsi:57.3,mm50:33.1,mm200:30.71,
 el:30.31,eh:34.86,stop:26.67,o1:39.78,o2:45.47,
 cb:0,ch:0,cs:0,tp:36.08,
 score:'D',rec:'avoid',zone:false,
 moat:[['Position établie sur son marché','modéré']],
 cats:[{t:'Valeur économique de 48,7€ fin mars 2026 (dividende déduit). Réserves de précaution constituées au T1.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:35,Concurrence:30,Réglementation:25,Devise:15,Exécution:25}},
{ticker:'SESG',x2:'',x2s:'',name:'SES',sector:'Télécoms',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:4.16,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:15.2,news5:'Goldman voit un potentiel de hausse pour SES grâce aux paiements de spectre et à la défense européenne|https://news.google.com/rss/articles/CBMiygFBVV95cUxON2xZaGZsY09XNFQ5V3BPTHdaUkdKU2hIVFRiWDhYSU5MdnFheGZaU3dxN2M0eU5jNlRXS3p1MnpURzF6SExrTnVEQTFQamdHVzUxR0JPaW9LbDNMTjV2TGRPbktrWXcydmVwWmtfYjNwbnE3RXN5N0x5c00ybXFMbGZOcmhvbUxOZ0FoWmN0aGlGV3Z0RFdhTlBqOUVKNkN3bTlyeWhZdFlwbFRQSnZVZUZQSjZCQlNOY3RuZUtBd2M0MnRYQ2dpX0Z3?oc=5|Investing.com France ;; Rubis brille sur sa nouvelle gouvernance, Serica plonge avec les déboires du Triton|https://news.google.com/rss/articles/CBMi8gFBVV95cUxORW9GSGQ5cF9XNy1QOUY5dDBjYmxpams2Tkk2LURjNFFuQlZLckRSLWkyeDBQdVNrbEFyWThfZkVucEE0b2JCMkZwOXhfSmNnTUNreGhZd1o0ZGFrMlJreVVmeklORmxkNWx2OXdmZkJkWEdYTmsxLUx1aHBsMnBJR1F4NGJTRlZPdVN0bWJlcmlBMHI3SVhLd0lfZmpzNGZIZEpPbzBhOXQ0emt5djZ2WW43dTZ2VzBXRHRaU2VZUzZsSWppVnBXVkRlaDRZY3JfZE5qeE8zb0lzYjhxdmtRaHlKWEZUN3Q0YlB3MktBV242UdIB9wFBVV95cUxQcDlfd0Rxc2ZoQVF3SE5MQkFCR2RTS19yN29uSW5CS3RrRGIyalM0eTZkcHp6cFAwV1puRUxQYm9LaTJGUlpOUC16T3huenk4dDRZdDRJNHRjSklPTW9fMkxfdDEyWXFSVmVVMElId005TjNmTHR2NnRBOUpQNWhpamxqRXh5cTJxY01ialhSSk1PeDBEalNuMFJtYWpOY2F1TUlEOURackd4NnQzYTB5R1VOckR6MXY5ZVZ6ZDhnaklNZHp2dkVtNndFSGIxMWNLRU9oS1FzM1d3ZUhtR3pFYlBkSXg4bk5aZE5BOUZEdHk2OTlfb1hJ?oc=5|Boursorama ;; Les changements de recommandations : Euronext, SES, Eutelsat|https://news.google.com/rss/articles/CBMizwFBVV95cUxQc3BUU3ZkY2d3LUJHYU9qVzF5RV9ZRUY2cW10VmVpakFWbE9RLXFQTTMyOF9LRFZPTzhBTW5LTy1rOTdRck1GU3gzcEFBcnc5QUJiTTNXbUJPbWNKM1ZKSEdsWTlEbktKb0tJc0M4RGREbGRjcDB0dG81VnlsZGl2S2YtdjV6ZUVXQU1pbFRManp2eEwyQllGNW1mdElWVWNNRTRmODBOOU9ma3dfRUR1V1VuZWgxWURxSmNfREVHS1lFazZfQTVUZ0VITjgxaGfSAdQBQVVfeXFMT2ZIaFp1aGpsLU5NRUp6eUY5eGU3UW9uOWcxRER5RlV0LUs0b01XRHFfeElvLWJnb2kzUmpGaXExUVUyck1yVEFCVjRINUJXSWh1akJORF9XWkp5T0plSG14dGE3RnQwZ3ZKYnotNENKQ1c0QmZjWWxyeUgyblliTW1zeHNTMEIxVG12a1R1SVlwOFQzTWxSQ19mbEMzcHhVLV9UZ1ZQY0FfZTZXMkVucFdBTGxvc1NSUExjbFRJVmFMY3NyTEFMRnpGSktoT19ZUjltSnc?oc=5|Boursorama',dy_n:10,dy_med:6.57,div12:0.5,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:1,eveb_h:7.4,pfcf_h:4.2,pe_h:84.8,fcur:'EUR',fcfh:'360|703|3074|117',nih:'-95|15|-905|-34',revh:'2627|2001|2030|1944',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:10.6,gimp:null,knife:true,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:null,cagr:10.6,alarm:'Piotroski 4/9',qwhy:'ROIC hors EA 1.3, ROIC 1.1, cash None%, dette/EBITDA 5.66',qok:false,nde:5.66,fcfc:null,roicx:1.3,chg:-0.24,mkt:'2.6Md€',b52h:9.89,b52l:3.53,beta:0.98,
 pe:-13.78,pb:0.9,ev_ebitda:6.22,ps:0.52,pfcf:0,ev_ebit:61.5,
 roe:-9.9,roic:1.1,roa:0.7,debt:2.63,de:2.63,ic:0.5,cr:1.04,qr:1,
 yield:12.0,epsg:0,revg:61.0,margin:-8.8,gm:70.3,om:0,fcf:21.2,
 capex:0,capr:20.9,capda:0.56,
 dcfb:7.29,dcfm:8.58,dcfu:10.3,
 pio:4,alt:0.27,rsi:52.9,mm50:4.36,mm200:5.9,
 el:7.21,eh:8.03,stop:6.34,o1:9.01,o2:10.3,
 cb:0,ch:0,cs:0,tp:7.54,
 score:'C',rec:'avoid',zone:false,
 moat:[['A évaluer','faible']],
 cats:[{t:'CA et Ebitda ajusté stables attendus vs 2025. Synergies de l\'intégration d\'Intelsat confirmées.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'TE',x2:'',x2s:'',name:'Technip Energies',sector:'Fours industriels petrochimie',cap:'large',srd:true,idx:'Cac Next 20',
 price:30.82,roiica:true,reinv:false,roiic:6.5,vmed:35.55,vepv:37.4,chg5:4.5,news5:'',dy_n:0,dy_med:null,div12:null,pe_lo:8.5,gmod:5.7,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'cyclique',wht:0.0,irrn:9.4,irr:9.4,dq:'',vmult:25.49,hn:4,eveb_h:2.3,pfcf_h:10.7,pe_h:12.2,fcur:'EUR',fcfh:'572|761|330|138',nih:'364|391|297|301',revh:'7204|6719|6004|6282',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:39.67,vpess:28.91,nregu:1,regn:3,regu:2,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:5.7,gimp:1.7,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'qarp',nig:6.6,cagr:4.7,alarm:'',qwhy:'',qok:true,nde:-3.63,fcfc:133.0,roicx:45.2,chg:-0.52,mkt:'6.13Md€',b52h:41.58,b52l:26.94,beta:0.66,
 pe:20.28,pb:2.62,ev_ebitda:6.49,ps:0.71,pfcf:0,ev_ebit:4.5,
 roe:12.6,roic:12.4,roa:2.1,debt:0.79,de:0.79,ic:25.1,cr:1.04,qr:1,
 yield:3.2,epsg:-88.2,revg:14.7,margin:3.6,gm:10.6,om:0,fcf:10.8,
 capex:0,capr:1.2,capda:0.73,
 dcfb:30.22,dcfm:35.55,dcfu:42.66,
 pio:5,alt:1.55,rsi:59.6,mm50:29.73,mm200:33.08,
 el:24.88,eh:28.44,stop:26.02,o1:39.67,o2:43.64,
 cb:0,ch:0,cs:0,tp:39.5,
 score:'C',rec:'watch',zone:false,
 moat:[['Position établie sur son marché','modéré']],
 cats:[{t:'Résultats T1 sanctionnés (guerre Moyen-Orient) mais prises de commandes de 6Mds€ offrent de la visibilité.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}},
{ticker:'TFI',x2:'',x2s:'',name:'TF1',sector:'Médias',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:5.85,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.1,news5:'',dy_n:9,dy_med:6.11,div12:0.63,pe_lo:7.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:1.5,pfcf_h:10.0,pe_h:8.2,fcur:'EUR',fcfh:'98|154|327|151',nih:'153|206|192|176',revh:'2297|2356|2297|2508',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:-3.8,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:true,vmeth:'per',nig:-4.6,cagr:-2.9,alarm:'',qwhy:'croissance CA -2.9%',qok:false,nde:-0.69,fcfc:100.0,roicx:30.1,chg:-1.43,mkt:'1.43Md€',b52h:8.53,b52l:5.71,beta:0.74,
 pe:9.92,pb:0.62,ev_ebitda:4.41,ps:0.56,pfcf:0,ev_ebit:3.7,
 roe:6.7,roic:14.5,roa:3.2,debt:0.1,de:0.1,ic:20.3,cr:1.47,qr:1,
 yield:10.6,epsg:-25.5,revg:-10.5,margin:5.7,gm:45.4,om:0,fcf:8.0,
 capex:0,capr:15.6,capda:0.85,
 dcfb:5.78,dcfm:6.8,dcfu:8.16,
 pio:7,alt:1.59,rsi:33.0,mm50:6.53,mm200:6.74,
 el:5.71,eh:6.36,stop:5.02,o1:7.14,o2:8.16,
 cb:0,ch:0,cs:0,tp:7.45,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Bouygues 43.5%)','modéré']],
 cats:[{t:'Revenus publicitaires pénalisés par le contexte politique français, effet jugé momentané.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'TKO',x2:'',x2s:'',name:'Tikehau Capital',sector:'Holdings',cap:'mid',srd:true,idx:'',
 price:16.46,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:1.6,news5:'',dy_n:7,dy_med:3.48,div12:0.8,pe_lo:13.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:18.9,pfcf_h:38.5,pe_h:20.0,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:null,regn:null,regu:null,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:null,cagr:null,alarm:'Piotroski 3/9',qwhy:'holding (grille dediee a venir)',qok:false,nde:null,fcfc:null,roicx:null,chg:1.11,mkt:'3.1Md€',b52h:20.05,b52l:14.58,beta:0.71,
 pe:21.38,pb:0.89,ev_ebitda:0,ps:4.19,pfcf:0,ev_ebit:31.5,
 roe:7.4,roic:null,roa:4.3,debt:0.57,de:0.57,ic:2.2,cr:3.51,qr:1,
 yield:4.9,epsg:164,revg:135.4,margin:34.7,gm:61.4,om:0,fcf:-7.4,
 capex:0,capr:null,capda:null,
 dcfb:14.33,dcfm:16.86,dcfu:20.23,
 pio:3,alt:1.01,rsi:54.4,mm50:16.54,mm200:16.63,
 el:13.49,eh:15.51,stop:11.87,o1:17.7,o2:20.23,
 cb:0,ch:0,cs:0,tp:21.17,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Tikehau Capital Advisors 56.3%)','modéré'],['Position établie sur son marché','modéré']],
 cats:[{t:'Gestion alternative (dette privée, private equity) porteuse. Objectifs 2026 en très forte hausse.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:60,Concurrence:55,Réglementation:50,Devise:40,Exécution:50}},
{ticker:'VCT',x2:'',x2s:'',name:'Vicat',sector:'Matériaux construction',cap:'mid',srd:true,idx:'Cac Mid 60',
 price:58.5,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:0.2,news5:'',dy_n:10,dy_med:3.7,div12:2.0,pe_lo:5.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:4.0,pfcf_h:5.2,pe_h:6.3,fcur:'EUR',fcfh:'313|357|279|-65',nih:'275|273|258|156',revh:'3854|3884|3937|3642',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:1,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:11.3,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:20.7,cagr:1.9,alarm:'',qwhy:'ROIC hors EA 11.9, ROIC 8.6, croissance CA 1.9%',qok:false,nde:1.43,fcfc:92.0,roicx:11.9,chg:-0.85,mkt:'2.7Md€',b52h:81.7,b52l:56.4,beta:0.73,
 pe:9.06,pb:0.86,ev_ebitda:6.0,ps:0.65,pfcf:0,ev_ebit:8.7,
 roe:10.2,roic:8.6,roa:4.4,debt:0.55,de:0.55,ic:7.7,cr:1.55,qr:1,
 yield:3.4,epsg:14.9,revg:8.0,margin:7.2,gm:36.2,om:0,fcf:12.0,
 capex:0,capr:8.7,capda:1.15,
 dcfb:69.29,dcfm:81.52,dcfu:97.82,
 pio:8,alt:1.44,rsi:43.9,mm50:61.74,mm200:64.54,
 el:67.66,eh:75.98,stop:59.54,o1:85.6,o2:97.82,
 cb:0,ch:0,cs:0,tp:84.75,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Famille Merceron-Vicat 60.4%)','modéré'],['Position établie sur son marché','modéré']],
 cats:[{t:'Forte exposition Europe (près de la moitié du CA), présence Egypte/Inde/Amérique du Nord renouvelle le potenti...',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}},
{ticker:'VIL',x2:'',x2s:'',name:'Viel & Cie',sector:'Holdings',cap:'mid',srd:true,idx:'',
 price:17.04,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-4.7,news5:'',dy_n:10,dy_med:4.27,div12:0.54,pe_lo:5.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:2.6,pfcf_h:5.4,pe_h:5.9,fcur:'EUR',unc:'',vopt:null,vpess:null,nregu:null,regn:null,regu:null,place:'Paris',near:false,gsrc:'yahoo (4 ans publies)',gused:null,gimp:null,knife:false,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:null,cagr:null,alarm:'',qwhy:'holding (grille dediee a venir)',qok:false,nde:null,fcfc:null,roicx:null,chg:-1.5,mkt:'1.27Md€',b52h:19.9,b52l:14.1,beta:0.46,
 pe:7.93,pb:1.72,ev_ebitda:0,ps:0.82,pfcf:0,ev_ebit:4.7,
 roe:25.3,roic:null,roa:5.4,debt:0.6,de:0.6,ic:13.4,cr:1.27,qr:1,
 yield:3.1,epsg:13.5,revg:6.4,margin:10.4,gm:100.0,om:0,fcf:9.8,
 capex:0,capr:2.0,capda:0.95,
 dcfb:12.44,dcfm:14.64,dcfu:17.57,
 pio:6,alt:1.27,rsi:32.6,mm50:18.73,mm200:17.86,
 el:11.71,eh:13.47,stop:10.3,o1:15.37,o2:17.57,
 cb:0,ch:0,cs:0,tp:21.55,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Viel et Cie Finance 64.1%)','modéré']],
 cats:[{t:'Maison-mère de Bourse Direct et Tradition ; bénéfice net +5,7% au S1 2025 (69,2M€).',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}},
{ticker:'WAVE',x2:'',x2s:'',name:'Wavestone',sector:'Services informatiques',cap:'small',srd:true,idx:'Cac Small',
 price:30.1,roiica:false,reinv:false,roiic:10.6,vmed:null,vepv:null,chg5:0.3,news5:'',dy_n:9,dy_med:0.71,div12:0.5,pe_lo:14.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:9.7,pfcf_h:15.0,pe_h:16.0,fcur:'EUR',fcfh:'129|84|80|37',nih:'82|76|58|50',revh:'954|944|701|532',yrs:'2026|2025|2024|2023',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Paris',near:false,gsrc:'communique 2026-10-05',gused:1.0,gimp:null,knife:true,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],neglect:false,vmeth:'per',nig:17.9,cagr:21.5,alarm:'',qwhy:'croissance officielle 1.0%',qok:false,nde:-0.75,fcfc:125.0,roicx:93.3,chg:0.0,mkt:'969M€',b52h:64.6,b52l:28.55,beta:0.94,
 pe:9.01,pb:1.05,ev_ebitda:4.88,ps:0.77,pfcf:0,ev_ebit:5.7,
 roe:12.3,roic:13.3,roa:7.5,debt:0.03,de:0.03,ic:35.3,cr:1.59,qr:1,
 yield:1.7,epsg:5.8,revg:2.1,margin:8.6,gm:20.9,om:0,fcf:17.5,
 capex:0,capr:0.2,capda:0.11,
 dcfb:33.26,dcfm:39.13,dcfu:46.96,
 pio:7,alt:3.0,rsi:49.1,mm50:31.31,mm200:41.9,
 el:29.74,eh:35.37,stop:26.17,o1:41.09,o2:46.96,
 cb:0,ch:0,cs:0,tp:44.1,
 score:'C',rec:'avoid',zone:false,
 moat:[['Actionnariat stable (Fondateurs et dirigeants 60%)','modéré'],['Position établie sur son marché','modéré']],
 cats:[{t:'Averti sur ses résultats annuels en octobre, pénalisé par l\'attentisme des clients ; amélioration attendue.',w:'Cf. commentaire',c:'var(--gd)'}],
 ins:[],
 peers:[],
 risks:{Cyclicité:45,Concurrence:40,Réglementation:35,Devise:25,Exécution:35}}

,{ticker:'WKL',x2:'',x2s:'',name:'Wolters Kluwer',sector:'Logiciel & information professionnelle',cap:'large',srd:false,idx:'Europe (EUR)',price:84.1,roiica:false,reinv:false,roiic:null,vmed:111.6,vepv:42.38,chg5:9.0,news5:'',dy_n:10,dy_med:1.77,div12:2.6,pe_lo:15.2,gmod:5.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:15.0,irrn:9.9,irr:10.4,dq:'',vmult:111.75,hn:4,eveb_h:16.7,pfcf_h:22.1,pe_h:27.2,fcur:'EUR',fcfh:'1363|1340|1221|1287',nih:'1308|1079|1007|1027',revh:'6125|5916|5584|5453',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:125.01,vpess:92.25,nregu:2,regn:3,regu:3,place:'Amsterdam',mthreat:'IA generative qui banalise le contenu',mtype:'information professionnelle integree aux processus (fiscal, sante, droit)',mscore:4,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-11',gused:5.0,near:false,gimp:-2.4,knife:false,neglect:false,vmeth:'qarp',nig:8.4,cagr:3.9,nde:1.79,fcfc:118.0,roicx:3456.3,chg:3.16,mkt:'—',b52h:115.15,b52l:54.64,beta:0.18,pe:14.38,pb:19.97,ev_ebitda:11.43,ps:3.06,pfcf:0,ev_ebit:12.6,roe:146.1,roic:24.7,roa:9.8,debt:5.9,de:5.9,ic:15.1,cr:0.69,qr:0,yield:3.2,epsg:8.9,revg:-0.6,margin:21.9,gm:74.1,om:0,fcf:7.3,capex:0,capr:5.0,capda:0.66,dcfb:94.86,dcfm:111.6,dcfu:133.92,pio:7,alt:2.52,rsi:80.7,mm50:70.18,mm200:65.8,el:83.7,eh:94.86,stop:83.03,o1:125.01,o2:137.51,cb:0,ch:0,cs:0,tp:90.72,score:'A',rec:'buy',zone:true,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ITX',x2:'',x2s:'',name:'Inditex',sector:'Distribution habillement',cap:'large',srd:false,idx:'Europe (EUR)',price:55.42,roiica:false,reinv:false,roiic:53.9,vmed:44.87,vepv:22.13,chg5:2.8,news5:'',dy_n:10,dy_med:3.05,div12:1.715,pe_lo:22.0,gmod:8.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:19.0,irrn:7.2,irr:7.4,dq:'',vmult:48.89,hn:4,eveb_h:13.5,pfcf_h:21.5,pe_h:25.2,fcur:'EUR',fcfh:'6520|6616|6795|5259',nih:'6220|5866|5381|4130',revh:'39864|38632|35947|32569',yrs:'2026|2025|2024|2023',unc:'moyenne',vopt:49.71,vpess:32.75,nregu:3,regn:3,regu:3,place:'Madrid',mthreat:'mode ultra-rapide (Shein), gout changeant',mtype:'chaine d approvisionnement rapide et echelle (Zara)',mscore:3,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-05',gused:8.0,near:false,gimp:14.2,knife:false,neglect:false,vmeth:'qarp',nig:14.6,cagr:7.0,nde:0.07,fcfc:117.0,roicx:31.7,chg:-0.79,mkt:'—',b52h:59.42,b52l:46.07,beta:0.96,pe:26.9,pb:9.67,ev_ebitda:17.38,ps:4.18,pfcf:0,ev_ebit:20.2,roe:36.8,roic:31.4,roa:14.7,debt:0.35,de:0.35,ic:22.7,cr:1.16,qr:0,yield:1.2,epsg:8.0,revg:9.1,margin:15.5,gm:56.5,om:0,fcf:3.8,capex:0,capr:6.8,capda:0.86,dcfb:38.14,dcfm:44.87,dcfu:53.84,pio:8,alt:9.66,rsi:58.4,mm50:55.28,mm200:54.07,el:33.65,eh:38.14,stop:29.48,o1:49.71,o2:54.68,cb:0,ch:0,cs:0,tp:60.39,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'AMS',x2:'',x2s:'',name:'Amadeus',sector:'Logiciel voyage',cap:'large',srd:false,idx:'Europe (EUR)',price:54.3,roiica:false,reinv:false,roiic:null,vmed:62.7,vepv:25.77,chg5:2.8,news5:'',dy_n:8,dy_med:1.75,div12:1.54,pe_lo:20.2,gmod:5.5,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:19.0,irrn:8.9,irr:9.4,dq:'',vmult:65.73,hn:4,eveb_h:14.0,pfcf_h:22.8,pe_h:24.5,fcur:'EUR',fcfh:'1386|1358|1194|874',nih:'1336|1253|1118|664',revh:'6517|6142|5441|4486',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:71.78,vpess:48.8,nregu:3,regn:3,regu:3,place:'Madrid',mthreat:'vente directe des compagnies (NDC)',mtype:'reservation aerienne (GDS) en quasi-duopole, logiciels compagnies',mscore:4,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-06',gused:5.5,near:false,gimp:2.3,knife:false,neglect:false,vmeth:'qarp',nig:26.2,cagr:13.3,nde:0.89,fcfc:110.0,roicx:39.9,chg:-0.18,mkt:'—',b52h:69.1,b52l:46.21,beta:0.66,pe:17.92,pb:4.99,ev_ebitda:10.28,ps:3.46,pfcf:0,ev_ebit:14.2,roe:26.5,roic:17.9,roa:9.6,debt:0.79,de:0.79,ic:22.1,cr:0.74,qr:0,yield:2.8,epsg:-2.6,revg:1.5,margin:19.9,gm:44.6,om:0,fcf:6.1,capex:0,capr:12.5,capda:1.11,dcfb:53.3,dcfm:62.7,dcfu:75.24,pio:8,alt:3.79,rsi:54.6,mm50:55.08,mm200:52.4,el:47.03,eh:53.3,stop:43.92,o1:71.78,o2:78.96,cb:0,ch:0,cs:0,tp:69.35,score:'B',rec:'watch',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'RAA',x2:'',x2s:'',name:'Rational',sector:'Industrie equipements cuisine pro',cap:'mid',srd:false,idx:'Europe (EUR)',price:616.5,roiica:false,reinv:false,roiic:22.9,vmed:494.61,vepv:271.53,chg5:3.8,news5:'',dy_n:10,dy_med:1.73,div12:20.0,pe_lo:29.4,gmod:8.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:26.375,irrn:6.7,irr:7.4,dq:'',vmult:549.59,hn:4,eveb_h:23.7,pfcf_h:36.3,pe_h:35.6,fcur:'EUR',fcfh:'219|251|224|123',nih:'254|251|214|186',revh:'1260|1194|1126|1022',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:548.53,vpess:375.44,nregu:3,regn:3,regu:3,place:'Francfort',mthreat:'cycle restauration, concurrence asiatique',mtype:'leader mondial des fours mixtes professionnels (~50 % de part)',mscore:4,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-05',gused:8.0,near:false,gimp:14.4,knife:false,neglect:false,vmeth:'qarp',nig:11.0,cagr:7.2,nde:-0.38,fcfc:90.0,roicx:33.2,chg:0.08,mkt:'—',b52h:776.5,b52l:553.5,beta:1.24,pe:24.48,pb:8.29,ev_ebitda:18.38,ps:5.41,pfcf:0,ev_ebit:19.2,roe:32.2,roic:33.2,roa:19.8,debt:0.03,de:0.03,ic:179.3,cr:3.92,qr:0,yield:2.6,epsg:15.3,revg:4.2,margin:20.5,gm:58.3,om:0,fcf:3.1,capex:0,capr:2.7,capda:0.91,dcfb:420.42,dcfm:494.61,dcfu:593.53,pio:5,alt:21.16,rsi:63.1,mm50:599.09,mm200:642.62,el:370.96,eh:420.42,stop:337.9,o1:548.53,o2:603.38,cb:0,ch:0,cs:0,tp:797.29,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'NEM',x2:'',x2s:'',name:'Nemetschek',sector:'Logiciel construction',cap:'large',srd:false,idx:'Europe (EUR)',price:76.25,roiica:false,reinv:false,roiic:14.4,vmed:62.32,vepv:22.88,chg5:8.7,news5:'',dy_n:10,dy_med:0.58,div12:0.68,pe_lo:34.0,gmod:13.2,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:26.375,irrn:7.5,irr:7.7,dq:'',vmult:62.32,hn:4,eveb_h:30.8,pfcf_h:32.6,pe_h:52.1,fcur:'EUR',fcfh:'389|293|240|195',nih:'217|175|161|162',revh:'1191|996|852|802',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:74.81,vpess:34.87,nregu:2,regn:3,regu:3,place:'Francfort',mthreat:'Autodesk, IA',mtype:'logiciels BIM/construction, couts de changement eleves',mscore:4,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-05',gused:14.5,near:false,gimp:16.7,knife:false,neglect:false,vmeth:'qarp',nig:10.3,cagr:14.1,nde:0.41,fcfc:156.0,roicx:882.5,chg:3.67,mkt:'—',b52h:105.9,b52l:50.45,beta:0.61,pe:35.8,pb:8.64,ev_ebitda:24.48,ps:6.99,pfcf:0,ev_ebit:28.8,roe:26.3,roic:24.7,roa:9.2,debt:0.52,de:0.52,ic:15.9,cr:0.93,qr:0,yield:0.9,epsg:26.7,revg:13.0,margin:19.6,gm:58.0,om:0,fcf:4.4,capex:0,capr:1.2,capda:0.19,dcfb:55.4,dcfm:65.18,dcfu:78.22,pio:8,alt:6.13,rsi:77.9,mm50:64.1,mm200:64.17,el:48.89,eh:55.4,stop:31.38,o1:74.81,o2:82.29,cb:0,ch:0,cs:0,tp:86.19,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'BEI',x2:'',x2s:'',name:'Beiersdorf',sector:'Cosmetique (Nivea)',cap:'large',srd:false,idx:'Europe (EUR)',price:81.8,roiica:false,reinv:false,roiic:35.5,vmed:null,vepv:null,chg5:3.2,news5:'',dy_n:10,dy_med:0.74,div12:1.0,pe_lo:21.6,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:15.9,pfcf_h:67.8,pe_h:31.1,fcur:'EUR',fcfh:'322|794|424|249',nih:'939|912|736|755',revh:'9852|9850|9447|8799',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Francfort',alarm:'',qwhy:'ROIC hors EA 13.3, cash 54.0%',qok:false,gsrc:'yahoo (4 ans publies)',gused:5.7,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:7.5,cagr:3.8,nde:-0.64,fcfc:54.0,roicx:13.3,chg:-0.02,mkt:'—',b52h:110.15,b52l:67.08,beta:0.47,pe:18.02,pb:1.98,ev_ebitda:9.57,ps:1.86,pfcf:0,ev_ebit:10.9,roe:10.9,roic:12.2,roa:6.2,debt:0.01,de:0.01,ic:40.6,cr:2.0,qr:0,yield:1.2,epsg:1.9,revg:-4.5,margin:9.8,gm:57.1,om:0,fcf:1.8,capex:0,capr:4.7,capda:1.41,dcfb:61.36,dcfm:72.19,dcfu:86.63,pio:6,alt:4.99,rsi:70.1,mm50:77.59,mm200:80.26,el:56.31,eh:65.84,stop:49.55,o1:75.8,o2:86.63,cb:0,ch:0,cs:0,tp:81.2,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'SY1',x2:'',x2s:'',name:'Symrise',sector:'Chimie aromes et parfums',cap:'large',srd:false,idx:'Europe (EUR)',price:100.7,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:8.0,news5:'',dy_n:10,dy_med:1.07,div12:1.25,pe_lo:29.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:17.1,pfcf_h:26.3,pe_h:39.6,fcur:'EUR',fcfh:'561|652|449|110',nih:'249|478|340|280',revh:'4929|4999|4730|4618',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Francfort',alarm:'',qwhy:'ROIC hors EA 9.6, ROIC 6.4, croissance CA 2.2%',qok:false,gsrc:'yahoo (4 ans publies)',gused:-0.8,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-3.8,cagr:2.2,nde:2.08,fcfc:131.0,roicx:9.6,chg:1.27,mkt:'—',b52h:100.8,b52l:64.7,beta:0.57,pe:56.89,pb:3.7,ev_ebitda:21.36,ps:2.81,pfcf:0,ev_ebit:32.5,roe:6.7,roic:6.4,roa:5.0,debt:0.61,de:0.61,ic:6.0,cr:2.98,qr:0,yield:1.3,epsg:-0.4,revg:-0.6,margin:5.0,gm:37.6,om:0,fcf:4.1,capex:0,capr:4.3,capda:0.7,dcfb:69.32,dcfm:81.55,dcfu:97.86,pio:6,alt:3.46,rsi:75.4,mm50:91.54,mm200:81.07,el:63.61,eh:74.37,stop:55.98,o1:85.63,o2:97.86,cb:0,ch:0,cs:0,tp:101.3,score:'D',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'MONC',x2:'',x2s:'',name:'Moncler',sector:'Luxe',cap:'large',srd:false,idx:'Europe (EUR)',price:42.75,roiica:true,reinv:false,roiic:3.5,vmed:39.77,vepv:27.64,chg5:-3.0,news5:'',dy_n:9,dy_med:1.12,div12:1.4,pe_lo:20.9,gmod:3.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:26.0,irrn:7.3,irr:8.1,dq:'',vmult:44.45,hn:4,eveb_h:12.1,pfcf_h:20.2,pe_h:22.8,fcur:'EUR',fcfh:'740|794|738|493',nih:'627|640|612|607',revh:'3132|3109|2984|2603',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:43.73,vpess:36.18,nregu:2,regn:3,regu:3,place:'Milan',mthreat:'mode, dependance Chine',mtype:'marque de luxe (doudoune) a forte marge',mscore:4,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-05',gused:3.0,near:false,gimp:5.3,knife:false,neglect:true,vmeth:'qarp',nig:1.1,cagr:6.4,nde:-0.08,fcfc:111.0,roicx:24.9,chg:-1.16,mkt:'—',b52h:59.4,b52l:42.1,beta:1.08,pe:18.19,pb:3.19,ev_ebitda:13.03,ps:3.64,pfcf:0,ev_ebit:12.7,roe:18.1,roic:20.2,roa:10.7,debt:0.34,de:0.34,ic:21.7,cr:2.3,qr:0,yield:3.2,epsg:7.1,revg:5.2,margin:20.0,gm:78.2,om:0,fcf:6.4,capex:0,capr:7.0,capda:0.65,dcfb:33.8,dcfm:39.77,dcfu:47.72,pio:7,alt:4.78,rsi:39.1,mm50:45.36,mm200:49.85,el:29.83,eh:33.8,stop:32.56,o1:43.73,o2:48.1,cb:0,ch:0,cs:0,tp:59.1,score:'C',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'BC',x2:'',x2s:'',name:'Brunello Cucinelli',sector:'Luxe',cap:'mid',srd:false,idx:'Europe (EUR)',price:86.16,roiica:false,reinv:false,roiic:12.7,vmed:null,vepv:null,chg5:6.1,news5:'',dy_n:8,dy_med:0.84,div12:1.04,pe_lo:48.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:19.7,pfcf_h:55.0,pe_h:55.4,fcur:'EUR',fcfh:'101|90|136|153',nih:'135|119|115|81',revh:'1408|1279|1139|920',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Milan',alarm:'',qwhy:'ROIC hors EA 11.5, ROIC 11.5',qok:false,gsrc:'yahoo (4 ans publies)',gused:17.1,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:18.8,cagr:15.3,nde:2.35,fcfc:107.0,roicx:11.5,chg:-1.28,mkt:'—',b52h:102.4,b52l:69.02,beta:0.89,pe:42.65,pb:10.69,ev_ebitda:22.95,ps:3.98,pfcf:0,ev_ebit:29.3,roe:26.8,roic:11.5,roa:7.6,debt:2.17,de:2.17,ic:5.9,cr:1.35,qr:0,yield:1.2,epsg:3.8,revg:9.5,margin:9.4,gm:54.6,om:0,fcf:1.7,capex:0,capr:10.1,capda:0.78,dcfb:40.35,dcfm:47.47,dcfu:56.96,pio:5,alt:3.72,rsi:64.5,mm50:83.05,mm200:82.26,el:37.03,eh:43.29,stop:32.59,o1:49.84,o2:56.96,cb:0,ch:0,cs:0,tp:99.57,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'REC',x2:'',x2s:'',name:'Recordati',sector:'Pharma specialites',cap:'large',srd:false,idx:'Europe (EUR)',price:52.95,roiica:false,reinv:true,roiic:18.6,vmed:53.41,vepv:15.88,chg5:0.0,news5:'',dy_n:10,dy_med:2.48,div12:1.34,pe_lo:22.2,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:26.0,irrn:7.8,irr:8.5,dq:'',vmult:69.48,hn:4,eveb_h:16.2,pfcf_h:21.8,pe_h:25.5,fcur:'EUR',fcfh:'512|-281|102|365',nih:'444|417|389|312',revh:'2618|2342|2082|1853',yrs:'2025|2024|2023|2022',unc:'non evaluee',vopt:53.41,vpess:35.47,nregu:3,regn:3,regu:3,place:'Milan',alarm:'',qwhy:'cash 45.0% mais reinvesti a 18.6% (regle reinvestissement)',qok:false,gsrc:'yahoo (4 ans publies)',gused:12.3,near:true,gimp:11.7,knife:false,neglect:false,vmeth:'qarp',nig:12.4,cagr:12.2,nde:2.3,fcfc:45.0,roicx:15.9,chg:0.0,mkt:'—',b52h:54.45,b52l:43.76,beta:0.5,pe:22.25,pb:5.09,ev_ebitda:12.59,ps:4.07,pfcf:0,ev_ebit:18.8,roe:24.9,roic:12.5,roa:9.8,debt:1.09,de:1.09,ic:6.9,cr:1.26,qr:0,yield:2.7,epsg:28.6,revg:8.3,margin:18.4,gm:71.5,om:0,fcf:4.6,capex:0,capr:3.3,capda:0.41,dcfb:45.4,dcfm:53.41,dcfu:64.09,pio:7,alt:3.71,rsi:55.3,mm50:52.65,mm200:49.95,el:40.06,eh:45.4,stop:31.92,o1:53.41,o2:58.75,cb:0,ch:0,cs:0,tp:60.1,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'AMP',x2:'',x2s:'',name:'Amplifon',sector:'Sante materiel medical (audition)',cap:'mid',srd:false,idx:'Europe (EUR)',price:12.55,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-0.8,news5:'',dy_n:9,dy_med:0.69,div12:0.29,pe_lo:33.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:13.6,pfcf_h:18.1,pe_h:36.4,fcur:'EUR',fcfh:'296|305|272|343',nih:'91|145|155|179',revh:'2396|2409|2260|2119',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:2,place:'Milan',alarm:'',qwhy:'ROIC 7.5, dette/EBITDA 2.98',qok:false,gsrc:'yahoo (4 ans publies)',gused:-7.9,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-20.0,cagr:4.2,nde:2.98,fcfc:213.0,roicx:29.7,chg:0.0,mkt:'—',b52h:15.84,b52l:7.84,beta:0.97,pe:40.5,pb:2.2,ev_ebitda:12.73,ps:1.39,pfcf:0,ev_ebit:23.0,roe:5.7,roic:7.5,roa:3.8,debt:1.18,de:1.18,ic:3.2,cr:0.73,qr:0,yield:2.3,epsg:5.5,revg:2.2,margin:3.0,gm:23.9,om:0,fcf:8.9,capex:0,capr:4.9,capda:0.38,dcfb:11.1,dcfm:13.06,dcfu:15.67,pio:5,alt:1.71,rsi:58.3,mm50:11.97,mm200:11.19,el:9.14,eh:11.49,stop:8.04,o1:13.71,o2:15.67,cb:0,ch:0,cs:0,tp:13.63,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'KNEBV',x2:'',x2s:'',name:'Kone',sector:'Industrie maintenance ascenseurs',cap:'large',srd:false,idx:'Europe (EUR)',price:54.8,roiica:false,reinv:false,roiic:64.6,vmed:null,vepv:null,chg5:2.5,chg5:null,chg5:null,news5:'',dy_n:10,dy_med:3.5,div12:1.8,pe_lo:25.3,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:17.3,pfcf_h:25.5,pe_h:29.0,fcur:'EUR',fcfh:'1162|1081|980|430',nih:'980|951|926|774',revh:'11245|11098|10952|10907',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Helsinki',alarm:'',qwhy:'croissance CA 1.0%',qok:false,gsrc:'yahoo (4 ans publies)',gused:4.6,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:8.2,cagr:1.0,nde:0.25,fcfc:101.0,roicx:62.2,chg:-0.83,mkt:'—',b52h:64.42,b52l:46.22,beta:0.78,pe:30.11,pb:12.35,ev_ebitda:18.43,ps:2.5,pfcf:0,ev_ebit:20.6,roe:41.4,roic:31.7,roa:9.7,debt:0.29,de:0.29,ic:33.8,cr:0.99,qr:0,yield:3.3,epsg:-13.2,revg:3.1,margin:8.3,gm:57.1,om:0,fcf:4.1,capex:0,capr:1.4,capda:0.48,dcfb:25.03,dcfm:29.45,dcfu:35.34,pio:8,alt:4.52,rsi:67.3,mm50:51.54,mm200:53.81,el:24.44,eh:27.45,stop:21.51,o1:30.92,o2:35.34,cb:0,ch:0,cs:0,tp:59.75,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'UMG',x2:'',x2s:'',name:'Universal Music Group',sector:'Media musique',cap:'large',srd:false,idx:'Europe (EUR)',price:16.12,roiica:false,reinv:false,roiic:24.0,vmed:15.92,vepv:7.7,chg5:8.1,news5:'',dy_n:5,dy_med:2.06,div12:0.52,pe_lo:21.0,gmod:5.7,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:15.0,irrn:7.9,irr:8.4,dq:'benefice 12 mois anormal (PER 89.6 contre 14.8 attendu)',vmult:18.54,hn:4,eveb_h:19.3,pfcf_h:32.7,pe_h:31.8,fcur:'EUR',fcfh:'1199|1306|1586|1280',nih:'1533|2086|1259|782',revh:'12507|11834|11108|10340',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:18.15,vpess:12.38,nregu:2,regn:3,regu:3,place:'Amsterdam',mthreat:'musique generee par IA, pouvoir des plateformes',mtype:'1er catalogue musical mondial, oligopole de 3 majors',mscore:4,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-14',gused:5.7,near:false,gimp:6.0,knife:false,neglect:false,vmeth:'qarp',nig:25.2,cagr:6.5,nde:1.26,fcfc:95.0,roicx:33.1,chg:-0.86,mkt:'—',b52h:23.98,b52l:13.92,beta:0.78,pe:89.58,pb:8.06,ev_ebitda:15.64,ps:2.26,pfcf:0,ev_ebit:15.5,roe:7.7,roic:23.7,roa:7.0,debt:1.52,de:1.52,ic:16.2,cr:0.61,qr:0,yield:3.2,epsg:-84.4,revg:5.3,margin:2.5,gm:41.7,om:0,fcf:4.1,capex:0,capr:4.3,capda:1.21,dcfb:13.53,dcfm:15.92,dcfu:19.1,pio:6,alt:-0.01,rsi:72.6,mm50:14.51,mm200:17.45,el:11.94,eh:13.53,stop:11.14,o1:18.15,o2:19.96,cb:0,ch:0,cs:0,tp:21.49,score:'D',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'BESI',x2:'',x2s:'',name:'BE Semiconductor',sector:'Semi-conducteurs equipements',cap:'mid',srd:false,idx:'Europe (EUR)',price:160.85,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:-8.4,news5:'',dy_n:10,dy_med:3.13,div12:1.58,pe_lo:18.4,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:45.1,pfcf_h:60.8,pe_h:59.2,fcur:'EUR',fcfh:'136|170|181|243',nih:'132|182|177|241',revh:'591|607|579|723',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Amsterdam',alarm:'',qwhy:'croissance CA -6.5%',qok:false,gsrc:'yahoo (4 ans publies)',gused:-12.3,near:false,gimp:null,knife:true,neglect:true,vmeth:'per',nig:-18.2,cagr:-6.5,nde:0.7,fcfc:100.0,roicx:33.5,chg:3.41,mkt:'—',b52h:328.4,b52l:120.15,beta:1.3,pe:61.39,pb:22.68,ev_ebitda:44.57,ps:17.34,pfcf:0,ev_ebit:69.4,roe:44.9,roic:31.0,roa:14.7,debt:0.62,de:0.62,ic:7.1,cr:4.28,qr:0,yield:1.0,epsg:178.0,revg:68.7,margin:28.4,gm:64.1,om:0,fcf:1.1,capex:0,capr:7.1,capda:1.24,dcfb:95.68,dcfm:112.57,dcfu:135.08,pio:6,alt:12.92,rsi:34.6,mm50:193.6,mm200:214.42,el:81.05,eh:99.96,stop:71.32,o1:118.2,o2:135.08,cb:0,ch:0,cs:0,tp:267.65,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ASM',x2:'',x2s:'',name:'ASM International',sector:'Semi-conducteurs equipements',cap:'large',srd:false,idx:'Europe (EUR)',price:760.2,roiica:false,reinv:false,roiic:52.7,vmed:276.7,vepv:228.06,chg5:-13.3,news5:'L’Europe en ordre dispersé|https://news.google.com/rss/articles/CBMijwFBVV95cUxQUlhkTHhJN21Sb0xTREhlOWlISFJvci1FclVrTndOb1N0N1pCckduN2d3OVBHMS1ISms0aUxyanBidjhsbFpSZkVVckphV2VVYUxxTUFocEE2UVozNVd0ZXR0VTlGYkxHZEhtVDBhb1kzNGQ0M1ZEMnJRRGxUVjdWWUVMNHhUX1dEd1d4MS1jNA?oc=5|Zonebourse Suisse ;; ASM International N.V. : AlphaValue/Baader Europe n’est plus vendeur, mais à l’achat|https://news.google.com/rss/articles/CBMi2AFBVV95cUxQVGF3aUpMQmlkWTZhaHBWWmoxTDVvd1JtMWQ3MGpFZTJ6emxDbFk3eGFfY19abVYyM1pFR3pBOFpVLVlCTXVHVVBhNy0tQUl1YjR2QjZpZl90RHNrNEc1YnBtem9BVURGR2Nkd0ZrWDNJRUpjZnBGZngycGo3S2k2UHQ4UTgtXzlvSkljT3hSQVBzS2N5TnZVcTc1eUVaNFJWZUM2QXBReW90RWs2RDhaU0JwbFhtdDV2eTRJZTBoWGRSejFXeExLaHFRb3N0elVVRi1iaGoxUlQ?oc=5|Zonebourse',dy_n:10,dy_med:1.12,div12:3.25,pe_lo:29.9,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'cyclique',wht:15.0,irrn:4.8,irr:4.9,dq:'',vmult:282.92,hn:4,eveb_h:21.8,pfcf_h:48.9,pe_h:34.1,fcur:'EUR',fcfh:'593|533|418|333',nih:'724|686|752|389',revh:'3173|2933|2634|2411',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:276.7,vpess:228.06,nregu:2,regn:3,regu:3,place:'Amsterdam',mthreat:'cycle semi-conducteurs, Chine',mtype:'leader du depot de couches atomiques (ALD)',mscore:4,alarm:'',qwhy:'cash 74.0%',qok:false,gsrc:'communique 2026-10-12',gused:12.0,near:true,gimp:30.0,knife:false,neglect:false,vmeth:'qarp',nig:23.0,cagr:9.6,nde:-0.86,fcfc:74.0,roicx:27.3,chg:0.96,mkt:'—',b52h:1092.5,b52l:459.7,beta:1.49,pe:34.78,pb:8.37,ev_ebitda:30.98,ps:11.03,pfcf:0,ev_ebit:38.6,roe:26.8,roic:24.2,roa:11.5,debt:0.02,de:0.02,ic:1028.7,cr:2.17,qr:0,yield:0.4,epsg:41.5,revg:20.0,margin:31.9,gm:51.8,om:0,fcf:1.6,capex:0,capr:14.8,capda:1.87,dcfb:235.19,dcfm:276.7,dcfu:332.04,pio:8,alt:19.3,rsi:34.5,mm50:841.11,mm200:808.54,el:193.69,eh:221.36,stop:205.25,o1:276.7,o2:304.37,cb:0,ch:0,cs:0,tp:1148.4,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'MTX',x2:'',x2s:'',name:'MTU Aero Engines',sector:'Aeronautique moteurs',cap:'large',srd:false,idx:'Europe (EUR)',price:346.8,roiica:false,reinv:false,roiic:27.4,vmed:null,vepv:null,chg5:-1.1,news5:'',dy_n:10,dy_med:1.2,div12:3.6,pe_lo:19.7,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:3,eveb_h:11.9,pfcf_h:45.5,pe_h:27.0,fcur:'EUR',fcfh:'333|74|365|347',nih:'1016|633|-102|331',revh:'8763|7411|5363|5330',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Francfort',alarm:'',qwhy:'cash 60.0%, perte exploitation',qok:false,gsrc:'yahoo (4 ans publies)',gused:31.6,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:45.3,cagr:18.0,nde:0.39,fcfc:60.0,roicx:19.1,chg:-1.73,mkt:'—',b52h:404.8,b52l:265.2,beta:0.88,pe:20.1,pb:4.11,ev_ebitda:13.57,ps:2.02,pfcf:0,ev_ebit:12.9,roe:22.6,roic:16.6,roa:5.7,debt:0.56,de:0.56,ic:13.1,cr:1.42,qr:0,yield:1.0,epsg:-15.4,revg:16.7,margin:10.2,gm:18.1,om:0,fcf:1.8,capex:0,capr:5.9,capda:1.24,dcfb:216.55,dcfm:254.76,dcfu:305.71,pio:7,alt:3.06,rsi:43.3,mm50:356.8,mm200:343.54,el:214.0,eh:238.46,stop:188.32,o1:267.5,o2:305.71,cb:0,ch:0,cs:0,tp:414.85,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'RHM',x2:'',x2s:'',name:'Rheinmetall',sector:'Defense',cap:'large',srd:false,idx:'Europe (EUR)',price:1059.8,roiica:false,reinv:false,roiic:50.4,vmed:646.79,vepv:317.94,chg5:10.1,news5:'Rheinmetall AG : AlphaValue/Baader Europe persiste à l’achat|https://news.google.com/rss/articles/CBMiugFBVV95cUxPV3FNUU5ab2pZdFpsQzB2QjRndVVFMzJnQmNIWVl6WXFoTk1NR0QtZXNuajlhemxwS21oOHJRbERWWDNDQTZaMXBvVkNjMFltR2xjWENDTlBWczZhbWNRX19jTGZDYWltSFV0RkNpcG1aWUxabHZCMzR3NnRtaTBFWlhBbFRvR3dnbVNxbWxhSU1DVHhTRHZ2YVV0aXZWUThlanRsOXQ2ekp2c0JwLWpWTGVqN2NyR1Q0WHc?oc=5|Zonebourse Suisse ;; Les États-Unis interdisent l’utilisation de l’IA chinoise DeepSeek dans les systèmes informatiques des agences gouvernementales|https://news.google.com/rss/articles/CBMi7wFBVV95cUxNU2pKUmh4QjY3V0NCRTRMWVFmejV5N3N4SmM5blVjeVo5dExQYXZPVEwyS0JkZ2NJS3g5eWlGc1R6cmlqZkdybFc1ejYtVlZJVEg4OUkxR2ZRYlQwTDF3ZTNfLWZKQkEyOXlaaDhSV3lqRUJaWkwtTkl5RTVTT0FjaXNWRjhqbXBhemFLRjVCUU1qSW5rQ0V1NlpGdUdVeFV3RldCM2k0ZjJXWHRST2Izc2c0UzVjSEYzaUVvTkU1eFZhbjk5cllPSktuUTBCWVRXRWRMU1JzN0ZuQW1uc1FJUzhFMlhwdUR3NEZvU2tsWQ?oc=5|Zonebourse Suisse ;; Au passage : les titres que vous avez peut-être manqués|https://news.google.com/rss/articles/CBMiswFBVV95cUxPODFlcjBmNmhBMS1TNjBFZGNES3g2YVl0NnE1U28yelJBVUI5dVQyS0dJZjhJT09Sb013RWNDSEw3VFBzWjFvZ0FoLV91RmRxR0JQRjlLRHhmRDJnMWppTi1QNXR6ak5UQjI1eTZseVhOLVppUV85SVE1dUdfY3JkclZSZ0VHVXlqTVBXNGxuMzB1VmhOWl9LaWNqZjRIck1GcmplbnRTTzlFbEZEX25qbUtrRQ?oc=5|Zonebourse Suisse',dy_n:10,dy_med:1.71,div12:11.5,pe_lo:17.0,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:26.375,irrn:6.1,irr:6.4,dq:'',vmult:733.6,hn:4,eveb_h:13.8,pfcf_h:36.1,pe_h:30.3,fcur:'EUR',fcfh:'1415|988|345|-175',nih:'696|717|535|474',revh:'9935|7715|7176|6410',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:646.79,vpess:399.5,nregu:2,regn:3,regu:3,place:'Francfort',mthreat:'cycle budgetaire, paix, execution',mtype:'capacites munitions/blindes, contrats publics longs',mscore:3,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-05',gused:35.75,near:false,gimp:24.0,knife:true,neglect:false,vmeth:'qarp',nig:13.7,cagr:15.7,nde:-0.17,fcfc:106.0,roicx:22.9,chg:-2.79,mkt:'—',b52h:1966.0,b52l:909.0,beta:0.48,pe:41.16,pb:9.95,ev_ebitda:23.55,ps:4.33,pfcf:0,ev_ebit:32.2,roe:25.7,roic:17.3,roa:6.8,debt:0.52,de:0.52,ic:14.6,cr:1.0,qr:0,yield:1.1,epsg:-5.7,revg:68.8,margin:6.3,gm:52.2,om:0,fcf:2.9,capex:0,capr:8.8,capda:1.74,dcfb:549.77,dcfm:646.79,dcfu:776.15,pio:5,alt:4.01,rsi:59.4,mm50:1048.96,mm200:1300.78,el:452.75,eh:517.43,stop:359.55,o1:646.79,o2:711.47,cb:0,ch:0,cs:0,tp:1570.81,score:'C',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'COLO',x2:'',x2s:'',name:'Coloplast',sector:'Sante materiel medical',cap:'large',srd:false,idx:'Europe (DKK)',price:62.47,roiica:true,reinv:false,roiic:6.4,vmed:null,vepv:null,chg5:4.6,news5:'',dy_n:10,dy_med:2.54,div12:3.08,pe_lo:35.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:3,eveb_h:25.3,pfcf_h:56.3,pe_h:35.1,fcur:'DKK',fcfh:'1420|2985|3964',nih:'5052|4783|4706',revh:'27030|24500|22579',yrs:'2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:2,regu:2,place:'Copenhague',alarm:'',qwhy:'cash 58.0%, dette/EBITDA 2.58',qok:false,gsrc:'yahoo (4 ans publies)',gused:6.5,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:3.6,cagr:9.4,nde:2.58,fcfc:58.0,roicx:33.1,chg:-1.12,mkt:'—',b52h:84.48,b52l:49.46,beta:0.56,pe:38.08,pb:7.86,ev_ebitda:14.99,ps:3.7,pfcf:0,ev_ebit:18.0,roe:18.5,roic:14.7,roa:10.1,debt:1.78,de:1.78,ic:9.0,cr:1.56,qr:0,yield:4.9,epsg:81.8,revg:5.7,margin:9.7,gm:67.2,om:0,fcf:1.3,capex:0,capr:5.0,capda:1.04,dcfb:45.75,dcfm:53.82,dcfu:64.58,pio:7,alt:3.44,rsi:69.8,mm50:58.54,mm200:58.94,el:37.67,eh:47.36,stop:33.15,o1:56.51,o2:64.58,cb:0,ch:0,cs:0,tp:62.02,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'DSV',x2:'',x2s:'',name:'DSV',sector:'Logistique transit international',cap:'large',srd:false,idx:'Europe (DKK)',price:162.09,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,chg5:4.8,news5:'',dy_n:10,dy_med:0.46,div12:0.94,pe_lo:13.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:14.6,pfcf_h:18.8,pe_h:27.9,fcur:'DKK',fcfh:'18893|9222|14083|25052',nih:'8095|10109|12315|17568',revh:'247331|167106|150785|235665',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:0,regn:3,regu:2,place:'Copenhague',alarm:'',qwhy:'ROIC 11.5, dette/EBITDA 3.57, croissance CA 1.6%',qok:false,gsrc:'yahoo (4 ans publies)',gused:-10.6,near:false,gimp:null,knife:true,neglect:false,vmeth:'per',nig:-22.8,cagr:1.6,nde:3.57,fcfc:140.0,roicx:38.9,chg:-1.74,mkt:'—',b52h:256.02,b52l:151.26,beta:0.99,pe:40.21,pb:2.3,ev_ebitda:14.84,ps:0.99,pfcf:0,ev_ebit:24.0,roe:6.3,roic:11.5,roa:4.6,debt:0.76,de:0.76,ic:4.3,cr:0.96,qr:0,yield:0.6,epsg:-4.0,revg:23.7,margin:2.4,gm:26.8,om:0,fcf:6.5,capex:0,capr:1.0,capda:null,dcfb:136.05,dcfm:160.05,dcfu:192.06,pio:7,alt:2.61,rsi:49.5,mm50:170.89,mm200:204.43,el:131.24,eh:148.53,stop:115.49,o1:168.06,o2:192.06,cb:0,ch:0,cs:0,tp:244.17,score:'D',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'NSIS',x2:'',x2s:'',name:'Novonesis',sector:'Biotech enzymes',cap:'large',srd:false,idx:'Europe (DKK)',price:61.79,roiica:true,reinv:false,roiic:1.7,vmed:null,vepv:null,chg5:6.0,news5:'',dy_n:10,dy_med:1.43,div12:0.88,pe_lo:26.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:18.8,pfcf_h:43.8,pe_h:38.2,fcur:'EUR',fcfh:'751|660|281|150',nih:'584|306|406|493',revh:'4158|3834|2402|2356',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:3,place:'Copenhague',mthreat:'integration Chr. Hansen, prix agricoles',mtype:'enzymes et micro-organismes : duopole mondial',mscore:4,alarm:'',qwhy:'ROIC 10.7',qok:false,gsrc:'communique 2026-10-12',gused:7.5,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:5.8,cagr:20.8,nde:-0.2,fcfc:103.0,roicx:15.8,chg:1.54,mkt:'—',b52h:62.21,b52l:45.06,beta:0.62,pe:45.45,pb:2.59,ev_ebitda:133.76,ps:50.11,pfcf:0,ev_ebit:265.2,roe:5.8,roic:10.7,roa:3.8,debt:0.28,de:0.28,ic:11.9,cr:1.74,qr:0,yield:1.4,epsg:26.7,revg:9.6,margin:14.7,gm:56.4,om:0,fcf:0.3,capex:0,capr:11.3,capda:0.82,dcfb:35.01,dcfm:41.19,dcfu:49.43,pio:7,alt:22.12,rsi:67.5,mm50:58.23,mm200:53.68,el:28.83,eh:36.25,stop:25.37,o1:43.25,o2:49.43,cb:0,ch:0,cs:0,tp:66.81,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ATCO',x2:'',x2s:'',name:'Atlas Copco',sector:'Industrie compresseurs',cap:'large',srd:false,idx:'Europe (SEK)',price:17.71,roiica:false,reinv:false,roiic:13.4,vmed:8.65,vepv:8.05,chg5:-6.6,news5:'',dy_n:10,dy_med:1.85,div12:0.49,pe_lo:25.5,gmod:2.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:30.0,irrn:5.0,irr:5.4,dq:'',vmult:9.17,hn:4,eveb_h:18.5,pfcf_h:33.8,pe_h:29.1,fcur:'SEK',fcfh:'26379|30863|22633|16346',nih:'26420|29782|28040|23477',revh:'168343|176771|172664|141325',yrs:'2025|2024|2023|2022',unc:'moyenne',vopt:9.92,vpess:7.9,nregu:2,regn:3,regu:2,place:'Stockholm',mthreat:'cycle industriel',mtype:'leader compresseurs/vide, apres-vente recurrent',mscore:4,alarm:'',qwhy:'croissance officielle 2.0%',qok:false,gsrc:'communique 2026-10-05',gused:2.0,near:true,gimp:20.9,knife:false,neglect:false,vmeth:'qarp',nig:4.0,cagr:6.0,nde:0.44,fcfc:89.0,roicx:39.3,chg:-2.6,mkt:'—',b52h:19.25,b52l:13.44,beta:1.04,pe:36.07,pb:9.04,ev_ebitda:23.87,ps:5.65,pfcf:0,ev_ebit:29.2,roe:25.7,roic:23.1,roa:10.7,debt:0.34,de:0.34,ic:39.2,cr:1.27,qr:0,yield:1.5,epsg:8.0,revg:9.1,margin:15.7,gm:42.2,om:0,fcf:2.7,capex:0,capr:3.7,capda:0.65,dcfb:7.36,dcfm:8.65,dcfu:10.39,pio:6,alt:6.52,rsi:42.2,mm50:18.26,mm200:16.84,el:6.49,eh:7.36,stop:7.11,o1:9.92,o2:10.91,cb:0,ch:0,cs:0,tp:20.44,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ASSA',x2:'',x2s:'',name:'Assa Abloy',sector:'Industrie serrures et acces',cap:'large',srd:false,idx:'Europe (SEK)',price:32.07,roiica:true,reinv:false,roiic:6.5,vmed:null,vepv:null,chg5:2.4,news5:'',dy_n:10,dy_med:1.75,div12:0.55,pe_lo:18.7,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:14.4,pfcf_h:19.7,pe_h:23.4,fcur:'SEK',fcfh:'18638|18829|18655|12363',nih:'14701|15639|13633|13291',revh:'152409|150162|140716|120793',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Stockholm',mthreat:'cycle construction',mtype:'leader mondial des serrures, base installee',mscore:4,alarm:'',qwhy:'ROIC 10.4',qok:false,gsrc:'communique 2026-10-12',gused:3.0,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:3.4,cagr:8.1,nde:2.19,fcfc:120.0,roicx:26.5,chg:-0.78,mkt:'—',b52h:35.68,b52l:28.25,beta:0.82,pe:24.2,pb:3.56,ev_ebitda:16.13,ps:2.62,pfcf:0,ev_ebit:20.2,roe:15.6,roic:10.4,roa:7.1,debt:0.64,de:0.64,ic:7.0,cr:1.01,qr:0,yield:1.8,epsg:15.9,revg:3.3,margin:10.8,gm:43.1,om:0,fcf:4.7,capex:0,capr:1.8,capda:0.46,dcfb:15.07,dcfm:17.72,dcfu:21.27,pio:8,alt:3.83,rsi:56.0,mm50:31.63,mm200:31.6,el:14.71,eh:16.52,stop:12.95,o1:18.61,o2:21.27,cb:0,ch:0,cs:0,tp:36.65,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'EPI',x2:'',x2s:'',name:'Epiroc',sector:'Industrie equipements miniers',cap:'large',srd:false,idx:'Europe (SEK)',price:23.34,roiica:true,reinv:false,roiic:3.9,vmed:12.33,vepv:10.4,chg5:-3.0,news5:'',dy_n:7,dy_med:1.88,div12:0.34,pe_lo:25.9,gmod:4.2,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'cyclique',wht:30.0,irrn:5.3,irr:5.7,dq:'',vmult:13.49,hn:4,eveb_h:16.9,pfcf_h:37.0,pe_h:27.0,fcur:'SEK',fcfh:'8680|8604|5456|4544',nih:'8602|8731|9431|8397',revh:'61998|63604|60343|49694',yrs:'2025|2024|2023|2022',unc:'elevee',vopt:13.59,vpess:10.33,nregu:1,regn:3,regu:2,place:'Stockholm',mthreat:'cycle minier',mtype:'equipements miniers en duopole avec Sandvik, apres-vente',mscore:4,alarm:'',qwhy:'cash 78.0%',qok:false,gsrc:'yahoo (4 ans publies)',gused:4.2,near:true,gimp:23.7,knife:false,neglect:false,vmeth:'qarp',nig:0.8,cagr:7.7,nde:0.7,fcfc:78.0,roicx:26.7,chg:-1.74,mkt:'—',b52h:25.56,b52l:16.78,beta:1.21,pe:35.51,pb:7.04,ev_ebitda:22.57,ps:5.03,pfcf:0,ev_ebit:27.5,roe:21.2,roic:20.0,roa:9.6,debt:0.42,de:0.42,ic:14.8,cr:2.13,qr:0,yield:1.4,epsg:15.8,revg:10.4,margin:14.2,gm:35.7,om:0,fcf:2.8,capex:0,capr:3.2,capda:0.65,dcfb:10.48,dcfm:12.33,dcfu:14.8,pio:8,alt:5.78,rsi:49.4,mm50:23.21,mm200:22.62,el:8.63,eh:9.87,stop:9.29,o1:13.59,o2:14.95,cb:0,ch:0,cs:0,tp:25.59,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'KOG',x2:'',x2s:'',name:'Kongsberg Gruppen',sector:'Defense',cap:'large',srd:false,idx:'Europe (NOK)',price:29.67,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,chg5:4.4,news5:'',dy_n:10,dy_med:2.71,div12:0.54,pe_lo:22.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,grid:'',wht:null,irrn:null,irr:null,dq:'',vmult:null,hn:4,eveb_h:21.5,pfcf_h:23.8,pe_h:28.1,fcur:'NOK',fcfh:'9800|11498|3444|28',nih:'7953|5126|3712|2773',revh:'31562|24648|40617|31803',yrs:'2025|2024|2023|2022',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:2,place:'Oslo',alarm:'',qwhy:'croissance CA -0.3%',qok:false,gsrc:'yahoo (4 ans publies)',gused:20.9,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:42.1,cagr:-0.3,nde:-1.9,fcfc:127.0,roicx:47.2,chg:-0.63,mkt:'—',b52h:40.44,b52l:21.64,beta:0.22,pe:46.01,pb:22.34,ev_ebitda:41.16,ps:7.71,pfcf:0,ev_ebit:45.4,roe:32.6,roic:30.0,roa:5.4,debt:0.24,de:0.24,ic:8.1,cr:0.88,qr:0,yield:0.7,epsg:-1.6,revg:29.6,margin:20.5,gm:55.7,om:0,fcf:3.6,capex:0,capr:9.3,capda:1.7,dcfb:14.16,dcfm:16.66,dcfu:19.99,pio:8,alt:0,rsi:54.6,mm50:29.56,mm200:30.86,el:13.99,eh:15.59,stop:12.31,o1:17.49,o2:19.99,cb:0,ch:0,cs:0,tp:37.74,score:'D',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'BVI',name:'Bureau Veritas',sector:'Services certification et inspection',cap:'large',srd:false,idx:'Europe (EUR)',price:27.98,roiica:false,reinv:false,roiic:72.4,vmed:26.46,vepv:11.1,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'860|859|662|705',nih:'588|569|504|467',revh:'6466|6241|5868|5651',yrs:'2025|2024|2023|2022',dq:'',chg5:2.8,dy_n:9,dy_med:2.68,div12:0.92,pe_lo:20.3,gmod:6.3,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:0.0,irrn:8.2,irr:8.2,vmult:29.16,hn:4,eveb_h:11.1,pfcf_h:15.4,pe_h:21.7,news5:'',grid:'',unc:'non evaluee',vopt:30.4,vpess:19.7,nregu:3,regn:3,regu:3,place:'Paris',gused:6.3,near:false,gimp:7.5,knife:false,neglect:false,vmeth:'qarp',nig:8.0,cagr:4.6,nde:1.35,fcfc:145.0,roicx:49.6,chg:0.5,mkt:'—',b52h:30.18,b52l:24.58,beta:0.72,pe:24.76,pb:7.5,ev_ebitda:11.85,ps:1.84,pfcf:0,ev_ebit:14.9,roe:32.9,roic:17.8,roa:9.7,debt:1.79,de:1.79,ic:10.2,cr:1.29,qr:0,yield:3.3,epsg:-25.0,revg:2.0,margin:7.5,gm:29.4,om:0,fcf:6.9,capex:0,capr:2.3,capda:0.49,dcfb:22.49,dcfm:26.46,dcfu:31.75,pio:8,alt:3.29,rsi:62.2,mm50:27.32,mm200:26.68,el:19.84,eh:22.49,stop:17.73,o1:30.4,o2:33.44,cb:0,ch:0,cs:0,tp:32.78,score:'C',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'KRI',name:'Kri-Kri Milk Industry',sector:'Agroalimentaire produits laitiers',cap:'small',srd:false,idx:'Europe (EUR)',price:33.45,roiica:false,reinv:true,roiic:58.1,vmed:36.6,vepv:10.04,alarm:'',qwhy:'cash 42.0% mais reinvesti a 58.1% (regle reinvestissement)',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'10|3|35|-4',nih:'34|35|32|3',revh:'329|256|216|172',yrs:'2025|2024|2023|2022',dq:'',chg5:0.1,dy_n:10,dy_med:2.9,div12:0.451,pe_lo:9.8,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:0.0,irrn:9.6,irr:9.6,vmult:36.6,hn:4,eveb_h:12.5,pfcf_h:67.4,pe_h:17.1,news5:'',grid:'',unc:'non evaluee',vopt:40.48,vpess:24.4,nregu:2,regn:3,regu:3,place:'AT',gused:72.3,near:true,gimp:7.5,knife:false,neglect:false,vmeth:'qarp',nig:120.6,cagr:24.1,nde:-0.16,fcfc:42.0,roicx:27.4,chg:0.45,mkt:'—',b52h:34.55,b52l:18.1,beta:0.89,pe:21.58,pb:5.96,ev_ebitda:16.84,ps:2.98,pfcf:0,ev_ebit:25.4,roe:30.8,roic:27.3,roa:14.6,debt:0.07,de:0.07,ic:134.5,cr:2.29,qr:0,yield:1.4,epsg:85.2,revg:19.3,margin:13.8,gm:29.2,om:0,fcf:0.9,capex:0,capr:7.9,capda:3.95,dcfb:34.41,dcfm:40.48,dcfu:48.58,pio:5,alt:12.19,rsi:58.5,mm50:31.77,mm200:26.11,el:30.36,eh:34.41,stop:21.96,o1:40.48,o2:44.53,cb:0,ch:0,cs:0,tp:28.96,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'KBX',name:'Knorr-Bremse',sector:'Industrie freinage ferroviaire et camions',cap:'large',srd:false,idx:'Europe (EUR)',price:98.55,roiica:false,reinv:false,roiic:80.1,vmed:68.82,vepv:50.69,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'785|696|533|94',nih:'534|445|553|489',revh:'7817|7883|7926|7150',yrs:'2025|2024|2023|2022',dq:'',chg5:-0.9,dy_n:7,dy_med:2.05,div12:1.9,pe_lo:16.8,gmod:3.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.375,irrn:6.2,irr:6.7,vmult:70.7,hn:4,eveb_h:7.3,pfcf_h:18.8,pe_h:21.2,news5:'',grid:'',unc:'non evaluee',vopt:79.36,vpess:59.59,nregu:2,regn:3,regu:1,place:'Francfort',gused:3.0,near:false,gimp:10.6,knife:false,neglect:false,vmeth:'qarp',nig:3.0,cagr:3.0,nde:-1.31,fcfc:104.0,roicx:104.2,chg:-0.95,mkt:'—',b52h:115.6,b52l:77.5,beta:1.09,pe:27.07,pb:4.93,ev_ebitda:13.82,ps:1.98,pfcf:0,ev_ebit:18.3,roe:19.8,roic:46.4,roa:7.1,debt:0.74,de:0.74,ic:7.5,cr:1.63,qr:0,yield:1.9,epsg:28.7,revg:7.0,margin:7.3,gm:53.2,om:0,fcf:4.9,capex:0,capr:4.2,capda:0.88,dcfb:58.5,dcfm:68.82,dcfu:82.58,pio:8,alt:3.72,rsi:40.9,mm50:102.4,mm200:101.61,el:51.61,eh:58.5,stop:53.63,o1:79.36,o2:87.3,cb:0,ch:0,cs:0,tp:119.27,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'G1A',name:'GEA Group',sector:'Industrie equipements agroalimentaires',cap:'large',srd:false,idx:'Europe (EUR)',price:69.0,roiica:false,reinv:false,roiic:30.4,vmed:45.06,vepv:31.06,alarm:'',qwhy:'croissance CA 2.1%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'477|473|305|266',nih:'414|385|393|401',revh:'5495|5422|5373|5165',yrs:'2025|2024|2023|2022',dq:'',chg5:0.4,dy_n:10,dy_med:2.43,div12:1.3,pe_lo:16.4,gmod:1.6,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.375,irrn:6.1,irr:6.6,vmult:45.06,hn:4,eveb_h:9.5,pfcf_h:20.4,pe_h:18.5,news5:'',grid:'',unc:'non evaluee',vopt:54.55,vpess:43.87,nregu:1,regn:3,regu:3,place:'Francfort',gused:1.6,near:true,gimp:9.5,knife:false,neglect:false,vmeth:'qarp',nig:1.0,cagr:2.1,nde:-0.4,fcfc:95.0,roicx:74.8,chg:-0.29,mkt:'—',b52h:70.0,b52l:53.45,beta:0.76,pe:25.75,pb:4.49,ev_ebitda:14.89,ps:1.99,pfcf:0,ev_ebit:17.4,roe:18.5,roic:20.9,roa:6.9,debt:0.1,de:0.1,ic:13.3,cr:1.06,qr:0,yield:1.9,epsg:13.8,revg:10.0,margin:7.7,gm:37.7,om:0,fcf:4.2,capex:0,capr:4.6,capda:1.11,dcfb:40.18,dcfm:47.27,dcfu:56.72,pio:7,alt:3.31,rsi:62.8,mm50:66.22,mm200:61.34,el:35.45,eh:40.18,stop:39.48,o1:54.55,o2:60.01,cb:0,ch:0,cs:0,tp:70.83,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'EVD',name:'CTS Eventim',sector:'Billetterie et spectacles',cap:'large',srd:false,idx:'Europe (EUR)',price:62.1,roiica:false,reinv:false,roiic:15.6,vmed:85.16,vepv:46.95,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'86|330|459|293',nih:'277|319|275|204',revh:'3079|2809|2359|1926',yrs:'2025|2024|2023|2022',dq:'',chg5:3.2,dy_n:7,dy_med:1.75,div12:1.44,pe_lo:21.9,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.375,irrn:10.0,irr:10.6,vmult:85.16,hn:4,eveb_h:10.7,pfcf_h:22.0,pe_h:26.1,news5:'',grid:'',unc:'non evaluee',vopt:86.2,vpess:52.37,nregu:2,regn:3,regu:3,place:'Francfort',gused:13.8,near:false,gimp:3.6,knife:false,neglect:false,vmeth:'qarp',nig:10.8,cagr:16.9,nde:-2.15,fcfc:109.0,roicx:59.4,chg:0.57,mkt:'—',b52h:86.35,b52l:48.26,beta:1.25,pe:19.41,pb:5.6,ev_ebitda:9.13,ps:1.81,pfcf:0,ev_ebit:10.3,roe:29.8,roic:28.7,roa:7.6,debt:0.1,de:0.1,ic:39.9,cr:0.88,qr:0,yield:2.3,epsg:31.1,revg:13.0,margin:9.3,gm:25.9,om:0,fcf:1.4,capex:0,capr:9.1,capda:2.75,dcfb:73.27,dcfm:86.2,dcfu:103.44,pio:6,alt:2.53,rsi:65.3,mm50:57.67,mm200:59.07,el:64.65,eh:73.27,stop:47.13,o1:86.2,o2:94.82,cb:0,ch:0,cs:0,tp:84.32,score:'A',rec:'watch',zone:true,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'FPE3',name:'Fuchs',sector:'Chimie lubrifiants',cap:'mid',srd:false,idx:'Europe (EUR)',price:45.58,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'croissance CA 1.5%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'314|307|460|128',nih:'306|302|282|259',revh:'3563|3525|3541|3412',yrs:'2025|2024|2023|2022',dq:'',chg5:4.0,dy_n:10,dy_med:2.5,div12:1.23,pe_lo:16.4,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:10.0,pfcf_h:16.9,pe_h:17.7,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:2,place:'Francfort',gused:3.6,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:5.7,cagr:1.5,nde:-0.41,fcfc:105.0,roicx:20.1,chg:0.44,mkt:'—',b52h:46.6,b52l:31.8,beta:0.73,pe:17.6,pb:2.92,ev_ebitda:10.43,ps:1.59,pfcf:0,ev_ebit:13.5,roe:17.6,roic:17.0,roa:10.8,debt:0.09,de:0.09,ic:33.9,cr:1.96,qr:0,yield:2.7,epsg:32.8,revg:21.5,margin:9.0,gm:34.8,om:0,fcf:5.3,capex:0,capr:2.6,capda:0.93,dcfb:28.27,dcfm:33.26,dcfu:39.91,pio:6,alt:4.84,rsi:70.1,mm50:41.87,mm200:38.53,el:27.61,eh:31.0,stop:24.3,o1:34.92,o2:39.91,cb:0,ch:0,cs:0,tp:47.56,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'KRN',name:'Krones',sector:'Industrie machines embouteillage',cap:'mid',srd:false,idx:'Europe (EUR)',price:112.6,roiica:false,reinv:false,roiic:16.9,vmed:139.56,vepv:98.05,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-14',fcur:'EUR',fcfh:'261|271|-25|361',nih:'299|277|225|187',revh:'5664|5294|4721|4209',yrs:'2025|2024|2023|2022',dq:'',chg5:7.2,dy_n:10,dy_med:1.66,div12:2.8,pe_lo:13.8,gmod:4.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.375,irrn:10.7,irr:11.4,vmult:139.56,hn:4,eveb_h:6.4,pfcf_h:14.1,pe_h:15.1,news5:'',grid:'',unc:'non evaluee',vopt:188.57,vpess:143.77,nregu:3,regn:3,regu:3,place:'Francfort',gused:4.0,near:false,gimp:-5.0,knife:false,neglect:false,vmeth:'qarp',nig:16.9,cagr:10.4,nde:-0.65,fcfc:88.0,roicx:20.6,chg:0.0,mkt:'—',b52h:144.2,b52l:103.2,beta:0.96,pe:12.03,pb:1.62,ev_ebitda:5.98,ps:0.62,pfcf:0,ev_ebit:7.4,roe:14.1,roic:17.8,roa:5.3,debt:0.02,de:0.02,ic:41.5,cr:1.42,qr:0,yield:2.5,epsg:0.9,revg:1.1,margin:5.1,gm:52.8,om:0,fcf:7.3,capex:0,capr:3.3,capda:1.0,dcfb:142.71,dcfm:167.89,dcfu:201.47,pio:9,alt:2.85,rsi:59.4,mm50:112.02,mm200:118.4,el:125.92,eh:142.71,stop:129.39,o1:188.57,o2:207.43,cb:0,ch:0,cs:0,tp:146.5,score:'A',rec:'watch',zone:true,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'AIXA',name:'Aixtron',sector:'Semi-conducteurs equipements',cap:'mid',srd:false,idx:'Europe (EUR)',price:32.77,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'cash 1.0%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'181|-72|-110|7',nih:'85|106|145|100',revh:'557|633|630|463',yrs:'2025|2024|2023|2022',dq:'',chg5:-7.8,dy_n:5,dy_med:1.08,div12:0.15,pe_lo:15.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:21.5,pfcf_h:12.2,pe_h:27.9,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Francfort',gused:0.5,near:false,gimp:null,knife:true,neglect:false,vmeth:'per',nig:-5.3,cagr:6.3,nde:-0.88,fcfc:1.0,roicx:17.7,chg:-0.36,mkt:'—',b52h:62.66,b52l:12.55,beta:0.81,pe:63.02,pb:3.72,ev_ebitda:37.74,ps:7.68,pfcf:0,ev_ebit:32.0,roe:6.3,roic:15.7,roa:3.3,debt:0.35,de:0.35,ic:126.7,cr:4.43,qr:0,yield:0.5,epsg:-5.6,revg:-16.2,margin:12.1,gm:39.5,om:0,fcf:4.9,capex:0,capr:5.0,capda:1.66,dcfb:37.36,dcfm:43.95,dcfu:52.74,pio:6,alt:19.18,rsi:40.1,mm50:36.79,mm200:38.15,el:31.64,eh:39.03,stop:27.84,o1:46.15,o2:52.74,cb:0,ch:0,cs:0,tp:48.21,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'IOS',name:'IONOS',sector:'Logiciel hebergement web',cap:'mid',srd:false,idx:'Europe (EUR)',price:34.8,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'croissance CA 0.6%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'327|310|233|178',nih:'230|170|174|74',revh:'1317|1248|1424|1293',yrs:'2025|2024|2023|2022',dq:'',chg5:4.0,dy_n:0,dy_med:null,div12:null,pe_lo:14.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:3,eveb_h:10.0,pfcf_h:10.5,pe_h:16.1,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:2,place:'Francfort',gused:23.3,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:46.0,cagr:0.6,nde:1.93,fcfc:162.0,roicx:79.4,chg:2.23,mkt:'—',b52h:35.68,b52l:20.9,beta:0.58,pe:24.0,pb:14.17,ev_ebitda:11.97,ps:3.45,pfcf:0,ev_ebit:15.7,roe:84.8,roic:20.2,roa:14.2,debt:2.68,de:2.68,ic:6.9,cr:0.28,qr:0,yield:0,epsg:-13.6,revg:8.1,margin:16.3,gm:60.1,om:0,fcf:7.0,capex:0,capr:4.9,capda:0.59,dcfb:34.8,dcfm:40.94,dcfu:49.13,pio:8,alt:3.12,rsi:58.3,mm50:33.77,mm200:28.68,el:31.11,eh:37.01,stop:27.38,o1:42.99,o2:49.13,cb:0,ch:0,cs:0,tp:37.21,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'AOF',name:'Atoss Software',sector:'Logiciel gestion du temps',cap:'small',srd:false,idx:'Europe (EUR)',price:91.1,roiica:false,reinv:false,roiic:null,vmed:89.21,vepv:34.25,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'46|59|51|25',nih:'48|45|36|19',revh:'189|171|151|114',yrs:'2025|2024|2023|2022',dq:'',chg5:4.4,dy_n:10,dy_med:1.42,div12:2.28,pe_lo:37.2,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.375,irrn:7.7,irr:8.4,vmult:92.93,hn:4,eveb_h:26.3,pfcf_h:35.8,pe_h:43.6,news5:'',grid:'',unc:'non evaluee',vopt:89.21,vpess:55.66,nregu:3,regn:3,regu:3,place:'Francfort',gused:27.0,near:false,gimp:12.6,knife:false,neglect:false,vmeth:'qarp',nig:35.6,cagr:18.4,nde:-1.09,fcfc:121.0,roicx:499.2,chg:0.22,mkt:'—',b52h:124.0,b52l:65.0,beta:1.27,pe:26.79,pb:16.6,ev_ebitda:17.82,ps:7.23,pfcf:0,ev_ebit:18.4,roe:66.1,roic:485.8,roa:32.1,debt:0.06,de:0.06,ic:160.8,cr:2.26,qr:0,yield:2.5,epsg:13.8,revg:13.0,margin:25.6,gm:78.2,om:0,fcf:3.2,capex:0,capr:0.5,capda:0.21,dcfb:75.83,dcfm:89.21,dcfu:107.05,pio:5,alt:17.78,rsi:58.7,mm50:91.1,mm200:83.25,el:66.91,eh:75.83,stop:50.09,o1:89.21,o2:98.13,cb:0,ch:0,cs:0,tp:120.78,score:'C',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'NA9',name:'Nagarro',sector:'Services informatiques',cap:'small',srd:false,idx:'Europe (EUR)',price:79.0,roiica:true,reinv:false,roiic:null,vmed:62.86,vepv:32.29,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'95|79|73|78',nih:'39|49|49|77',revh:'999|972|912|856',yrs:'2025|2024|2023|2022',dq:'',chg5:1.9,dy_n:0,dy_med:null,div12:null,pe_lo:19.7,gmod:0.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.375,irrn:7.0,irr:7.3,vmult:62.86,hn:4,eveb_h:10.7,pfcf_h:14.6,pe_h:22.5,news5:'',grid:'',unc:'non evaluee',vopt:72.62,vpess:63.65,nregu:1,regn:3,regu:3,place:'Francfort',gused:-7.4,near:false,gimp:4.9,knife:false,neglect:false,vmeth:'qarp',nig:-20.1,cagr:5.3,nde:2.12,fcfc:151.0,roicx:32.1,chg:0.06,mkt:'—',b52h:80.6,b52l:32.5,beta:1.19,pe:19.75,pb:5.59,ev_ebitda:10.34,ps:0.98,pfcf:0,ev_ebit:14.3,roe:30.2,roic:15.7,roa:9.0,debt:2.16,de:2.16,ic:4.3,cr:2.4,qr:0,yield:1.3,epsg:32.8,revg:0.2,margin:5.0,gm:21.8,om:0,fcf:9.7,capex:0,capr:0.8,capda:0.22,dcfb:54.1,dcfm:63.65,dcfu:76.38,pio:7,alt:3.49,rsi:55.0,mm50:78.41,mm200:61.01,el:47.74,eh:54.1,stop:57.28,o1:72.62,o2:79.88,cb:0,ch:0,cs:0,tp:81.0,score:'C',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'YSN',name:'secunet',sector:'Cybersecurite',cap:'small',srd:false,idx:'Europe (EUR)',price:242.0,roiica:false,reinv:false,roiic:null,vmed:112.07,vepv:72.6,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'54|47|43|-10',nih:'33|28|29|31',revh:'459|406|394|347',yrs:'2025|2024|2023|2022',dq:'',chg5:-8.3,dy_n:10,dy_med:1.31,div12:2.58,pe_lo:27.6,gmod:5.9,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.375,irrn:5.0,irr:5.3,vmult:116.29,hn:4,eveb_h:15.0,pfcf_h:21.9,pe_h:34.0,news5:'',grid:'',unc:'non evaluee',vopt:128.44,vpess:85.45,nregu:1,regn:3,regu:3,place:'Francfort',gused:5.9,near:false,gimp:23.2,knife:false,neglect:false,vmeth:'qarp',nig:2.1,cagr:9.7,nde:-0.89,fcfc:111.0,roicx:42.5,chg:1.26,mkt:'—',b52h:268.0,b52l:152.8,beta:0.84,pe:45.75,pb:10.01,ev_ebitda:23.14,ps:3.18,pfcf:0,ev_ebit:30.0,roe:23.2,roic:25.4,roa:8.6,debt:0.19,de:0.19,ic:59.3,cr:1.74,qr:0,yield:1.1,epsg:117.8,revg:31.6,margin:7.0,gm:22.5,om:0,fcf:3.5,capex:0,capr:1.8,capda:0.35,dcfb:95.26,dcfm:112.07,dcfu:134.48,pio:7,alt:5.76,rsi:54.1,mm50:211.24,mm200:192.93,el:84.05,eh:95.26,stop:76.91,o1:128.44,o2:141.28,cb:0,ch:0,cs:0,tp:253.33,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'KSB3',name:'KSB',sector:'Industrie pompes et vannes',cap:'small',srd:false,idx:'Europe (EUR)',price:811.0,roiica:false,reinv:true,roiic:29.8,vmed:1590.49,vepv:1970.02,alarm:'',qwhy:'cash 48.0% mais reinvesti a 29.8% (regle reinvestissement)',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'42|134|174|-100',nih:'141|118|152|104',revh:'3035|2965|2819|2573',yrs:'2025|2024|2023|2022',dq:'',chg5:1.1,dy_n:10,dy_med:2.66,div12:26.76,pe_lo:5.7,gmod:8.2,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.375,irrn:12.6,irr:13.5,vmult:958.99,hn:4,eveb_h:2.2,pfcf_h:7.8,pe_h:7.7,news5:'',grid:'',unc:'non evaluee',vopt:1745.7,vpess:1151.41,nregu:2,regn:3,regu:3,place:'Francfort',gused:8.2,near:true,gimp:-5.0,knife:true,neglect:false,vmeth:'qarp',nig:10.8,cagr:5.7,nde:-0.77,fcfc:48.0,roicx:21.2,chg:-0.25,mkt:'—',b52h:1265.0,b52l:771.0,beta:0.71,pe:10.85,pb:1.22,ev_ebitda:4.69,ps:0.46,pfcf:0,ev_ebit:5.8,roe:11.6,roic:20.5,roa:5.4,debt:0.04,de:0.04,ic:12.4,cr:1.92,qr:0,yield:3.3,epsg:0,revg:1.5,margin:4.3,gm:58.0,om:0,fcf:3.0,capex:0,capr:5.1,capda:1.6,dcfb:1351.92,dcfm:1590.49,dcfu:1908.59,pio:8,alt:2.02,rsi:47.9,mm50:830.9,mm200:909.85,el:1192.87,eh:1351.92,stop:1036.27,o1:1745.7,o2:1920.27,cb:0,ch:0,cs:0,tp:1196.2,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'BFSA',name:'Befesa',sector:'Recyclage industriel',cap:'small',srd:false,idx:'Europe (EUR)',price:33.5,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'ROIC hors EA 12.7, ROIC 7.0, croissance CA 1.3%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'136|113|43|31',nih:'81|51|58|106',revh:'1183|1239|1181|1136',yrs:'2025|2024|2023|2022',dq:'',chg5:-6.9,dy_n:7,dy_med:2.41,div12:1.0,pe_lo:14.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:9.1,pfcf_h:20.9,pe_h:16.6,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Francfort',gused:-3.8,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-8.8,cagr:1.3,nde:2.38,fcfc:109.0,roicx:12.7,chg:-1.47,mkt:'—',b52h:38.1,b52l:26.6,beta:1.8,pe:15.73,pb:1.83,ev_ebitda:8.18,ps:1.14,pfcf:0,ev_ebit:12.9,roe:11.0,roic:7.0,roa:5.5,debt:0.92,de:0.92,ic:4.5,cr:1.04,qr:0,yield:2.9,epsg:13.0,revg:3.8,margin:7.3,gm:45.9,om:0,fcf:10.1,capex:0,capr:6.4,capda:0.93,dcfb:27.48,dcfm:32.33,dcfu:38.8,pio:9,alt:1.77,rsi:40.5,mm50:35.39,mm200:32.94,el:26.83,eh:30.13,stop:23.61,o1:33.95,o2:38.8,cb:0,ch:0,cs:0,tp:42.7,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ELG',name:'Elmos Semiconductor',sector:'Semi-conducteurs',cap:'small',srd:false,idx:'Europe (EUR)',price:131.6,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'cash 1.0%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'66|-51|-25|15',nih:'101|129|99|71',revh:'583|581|575|447',yrs:'2025|2024|2023|2022',dq:'',chg5:-6.0,dy_n:10,dy_med:1.49,div12:1.5,pe_lo:9.1,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:6.4,pfcf_h:44.0,pe_h:12.8,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:2,regn:3,regu:3,place:'Francfort',gused:10.8,near:false,gimp:null,knife:true,neglect:true,vmeth:'per',nig:12.3,cagr:9.2,nde:-0.07,fcfc:1.0,roicx:16.5,chg:2.65,mkt:'—',b52h:206.0,b52l:79.5,beta:1.71,pe:22.15,pb:4.15,ev_ebitda:13.17,ps:3.63,pfcf:0,ev_ebit:17.0,roe:18.0,roic:16.5,roa:10.2,debt:0.19,de:0.19,ic:38.1,cr:2.22,qr:0,yield:1.2,epsg:-23.6,revg:11.2,margin:16.4,gm:43.8,om:0,fcf:2.9,capex:0,capr:9.2,capda:1.39,dcfb:108.6,dcfm:127.76,dcfu:153.31,pio:6,alt:10.02,rsi:39.3,mm50:142.64,mm200:150.12,el:91.99,eh:113.45,stop:80.95,o1:134.15,o2:153.31,cb:0,ch:0,cs:0,tp:193.0,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'REY',name:'Reply',sector:'Services informatiques',cap:'mid',srd:false,idx:'Europe (EUR)',price:128.9,roiica:false,reinv:false,roiic:38.9,vmed:132.46,vepv:78.54,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'280|296|221|143',nih:'251|211|187|191',revh:'2450|2296|2118|1911',yrs:'2025|2024|2023|2022',dq:'',chg5:1.5,dy_n:10,dy_med:0.71,div12:1.35,pe_lo:16.5,gmod:9.1,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.0,irrn:8.7,irr:9.0,vmult:132.46,hn:4,eveb_h:11.9,pfcf_h:19.8,pe_h:22.4,news5:'',grid:'',unc:'non evaluee',vopt:159.85,vpess:90.61,nregu:2,regn:3,regu:3,place:'Milan',gused:9.1,near:false,gimp:7.4,knife:false,neglect:false,vmeth:'qarp',nig:9.5,cagr:8.6,nde:-0.85,fcfc:112.0,roicx:63.6,chg:-0.15,mkt:'—',b52h:130.8,b52l:76.65,beta:0.87,pe:23.39,pb:3.11,ev_ebitda:9.94,ps:1.85,pfcf:0,ev_ebit:11.4,roe:18.1,roic:21.6,roa:9.3,debt:0.12,de:0.12,ic:40.7,cr:1.73,qr:0,yield:1.1,epsg:-13.6,revg:8.0,margin:10.2,gm:17.1,om:0,fcf:6.0,capex:0,capr:1.9,capda:0.51,dcfb:118.41,dcfm:139.31,dcfu:167.17,pio:8,alt:3.98,rsi:63.5,mm50:120.66,mm200:102.61,el:104.48,eh:118.41,stop:81.55,o1:159.85,o2:175.84,cb:0,ch:0,cs:0,tp:153.36,score:'B',rec:'watch',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'DLG',name:'De Longhi',sector:'Electromenager',cap:'mid',srd:false,idx:'Europe (EUR)',price:43.78,roiica:false,reinv:false,roiic:null,vmed:44.41,vepv:24.67,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-14',fcur:'EUR',fcfh:'455|383|489|23',nih:'316|311|250|177',revh:'3793|3490|3074|3156',yrs:'2025|2024|2023|2022',dq:'',chg5:9.3,dy_n:10,dy_med:2.32,div12:0.85,pe_lo:14.4,gmod:6.5,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.0,irrn:8.5,irr:9.0,vmult:44.41,hn:4,eveb_h:8.7,pfcf_h:11.8,pe_h:17.5,news5:'',grid:'',unc:'non evaluee',vopt:53.46,vpess:36.08,nregu:3,regn:3,regu:2,place:'Milan',gused:6.5,near:false,gimp:4.5,knife:false,neglect:false,vmeth:'qarp',nig:21.3,cagr:6.3,nde:-0.8,fcfc:128.0,roicx:29.5,chg:0.23,mkt:'—',b52h:44.22,b52l:28.48,beta:1.56,pe:19.2,pb:3.17,ev_ebitda:10.9,ps:1.67,pfcf:0,ev_ebit:13.3,roe:17.8,roic:19.2,roa:7.5,debt:0.22,de:0.22,ic:20.9,cr:1.62,qr:0,yield:1.9,epsg:35.1,revg:8.4,margin:8.8,gm:45.2,om:0,fcf:7.0,capex:0,capr:2.4,capda:0.68,dcfb:40.58,dcfm:47.74,dcfu:57.29,pio:9,alt:4.16,rsi:70.6,mm50:40.26,mm200:36.91,el:35.8,eh:40.58,stop:32.47,o1:53.46,o2:58.81,cb:0,ch:0,cs:0,tp:48.8,score:'B',rec:'watch',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'TPRO',name:'Technoprobe',sector:'Semi-conducteurs equipements',cap:'mid',srd:false,idx:'Europe (EUR)',price:26.82,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'cash 63.0%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'100|30|-2|128',nih:'98|64|97|148',revh:'628|543|409|549',yrs:'2025|2024|2023|2022',dq:'',chg5:-19.5,dy_n:0,dy_med:null,div12:null,pe_lo:27.2,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:27.9,pfcf_h:83.1,pe_h:55.6,news5:'Technoprobe, l’intelligence artificielle (IA) dope les comptes, mais le titre est exposé à la volatilité|https://news.google.com/rss/articles/CBMi6wFBVV95cUxPZmR3aFRUSlAxVlM5X3I5TGlUY1FfbFlfaHhlQXJiQ0dhaWM0dnR5RWUyYkMzUGFBLUhrcFp5cjdYOUpueEp1RXdxZWJCZExpZlFEM2Y4YjEweUZ1SjlCSWNfaGg0QjViNEpMenJXRk9mMTNtbF9SNTBQWjhTMy13d2U4anJPNFhzdVF1U3NQRW5VZy1TSmlCQlZRVXRBc1BMN05PUThpTndVWnlRM1VNOFo1aE85bHJLWF8wZ2VJQ3dRYjNUNGZFWW5kemRiOWdWTFN3WTAyeGZILWVERk94VjZQQTZOSzZFMVJR?oc=5|Zonebourse Suisse ;; La Bourse de Milan accentue ses pertes dans l’attente d’un repli du Nasdaq, chute de Technoprobe, Stm et Prysmian|https://news.google.com/rss/articles/CBMi7wFBVV95cUxPc214My1QdHBOU21naERvSmZ1T1RwN1Y1VEtDQ1FxMnV5bUY2a1lTbF9xRmNUeDFiUTh4dE9XSU5mZDlzZmRueDBOVm9sWHlEQjAxVkJxekEwOU9neFZBOW5SNHM1S1hkaGJyb2o3dHVDM3ZyQmpHSWVwRktaVTh5ZVNZbWRHU01oaEd6OEd5WkNxRExBNlZwOU5JYzlSRTRNTDZwNnNEbW5vTmxFSldBZk5fVEw3NFdBWHU4ZkdwZ202NVgzb2NjdGZLNmJCa1VuVVpKeUtvUUtJR1puWDVWV3V1aTVoY29RaHBWYUk5WQ?oc=5|Zonebourse Suisse ;; Technoprobe et STM tirent le MIB dans le rouge ; TIM en hausse|https://news.google.com/rss/articles/CBMivAFBVV95cUxQSF9fTW1nc3hQb3NHcW42WHpLQlZJdkl0UXdVY3hHS0VBVDNIRjh1VXBpX29UM1RuZ0VMazQ3S3M0Zl84dzhLWUhMVWh1Q3lydmdqcllBTE0zeHZwNkx3TDhBenF2amVhMVZtemNFMWVseVh0c0dlWm9mNUZTLU5NNExwY3JLNFVuTGR1V09qOU9GZVhTVlg2Q0hPSTMzc003dy1KR2p5c09yWWdKQ2JoNEM2UFpoSUVNTEtDdQ?oc=5|Zonebourse Suisse',grid:'',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:2,place:'Milan',gused:-4.2,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-12.9,cagr:4.6,nde:-3.47,fcfc:63.0,roicx:19.2,chg:1.13,mkt:'—',b52h:38.58,b52l:8.62,beta:1.06,pe:83.81,pb:12.37,ev_ebitda:56.98,ps:22.4,pfcf:0,ev_ebit:126.4,roe:15.8,roic:18.0,roa:9.5,debt:0.02,de:0.02,ic:147.9,cr:5.24,qr:0,yield:0,epsg:331.6,revg:42.4,margin:26.9,gm:49.0,om:0,fcf:0.6,capex:0,capr:15.8,capda:1.53,dcfb:15.72,dcfm:18.49,dcfu:22.19,pio:8,alt:60.26,rsi:35.3,mm50:29.92,mm200:24.56,el:13.31,eh:16.42,stop:11.71,o1:19.41,o2:22.19,cb:0,ch:0,cs:0,tp:42.8,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'CRL',name:'Carel Industries',sector:'Industrie climatisation composants',cap:'small',srd:false,idx:'Europe (EUR)',price:26.25,roiica:true,reinv:false,roiic:7.1,vmed:16.11,vepv:7.88,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'97|54|75|43',nih:'74|63|71|62',revh:'634|583|655|549',yrs:'2025|2024|2023|2022',dq:'',chg5:-4.7,dy_n:7,dy_med:0.76,div12:0.195,pe_lo:32.8,gmod:5.3,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.0,irrn:6.0,irr:6.2,vmult:16.11,hn:4,eveb_h:19.7,pfcf_h:37.8,pe_h:37.2,news5:'',grid:'',unc:'non evaluee',vopt:17.87,vpess:13.07,nregu:2,regn:3,regu:2,place:'Milan',gused:5.3,near:false,gimp:19.5,knife:false,neglect:false,vmeth:'qarp',nig:5.8,cagr:4.9,nde:0.02,fcfc:100.0,roicx:33.1,chg:-1.32,mkt:'—',b52h:32.9,b52l:19.6,beta:0.98,pe:32.01,pb:5.83,ev_ebitda:22.49,ps:4.26,pfcf:0,ev_ebit:29.2,roe:19.6,roic:18.4,roa:7.7,debt:0.23,de:0.23,ic:14.3,cr:1.6,qr:0,yield:0.7,epsg:70.4,revg:25.5,margin:13.4,gm:48.8,om:0,fcf:3.3,capex:0,capr:3.6,capda:0.54,dcfb:13.7,dcfm:16.12,dcfu:19.34,pio:8,alt:6.36,rsi:42.8,mm50:27.32,mm200:26.12,el:12.09,eh:13.7,stop:11.76,o1:17.87,o2:19.66,cb:0,ch:0,cs:0,tp:34.29,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'TGYM',name:'Technogym',sector:'Equipements fitness',cap:'small',srd:false,idx:'Europe (EUR)',price:12.94,roiica:false,reinv:false,roiic:null,vmed:13.88,vepv:5.53,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-14',fcur:'EUR',fcfh:'116|114|71|77',nih:'115|87|74|64',revh:'1019|901|808|721',yrs:'2025|2024|2023|2022',dq:'',chg5:1.6,dy_n:8,dy_med:2.28,div12:0.38,pe_lo:22.6,gmod:9.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.0,irrn:8.1,irr:8.9,vmult:15.1,hn:4,eveb_h:11.2,pfcf_h:22.2,pe_h:24.3,news5:'',grid:'',unc:'non evaluee',vopt:15.43,vpess:9.31,nregu:3,regn:3,regu:3,place:'Milan',gused:9.0,near:false,gimp:7.3,knife:true,neglect:false,vmeth:'qarp',nig:21.9,cagr:12.2,nde:-0.71,fcfc:111.0,roicx:37.3,chg:-0.08,mkt:'—',b52h:21.82,b52l:11.92,beta:0.85,pe:22.31,pb:8.51,ev_ebitda:12.73,ps:2.45,pfcf:0,ev_ebit:15.5,roe:41.1,roic:37.1,roa:12.5,debt:0.41,de:0.41,ic:129.4,cr:1.13,qr:0,yield:2.9,epsg:1.0,revg:7.4,margin:11.1,gm:46.8,om:0,fcf:4.5,capex:0,capr:6.5,capda:1.3,dcfb:11.8,dcfm:13.88,dcfu:16.66,pio:8,alt:5.63,rsi:50.4,mm50:12.94,mm200:16.13,el:10.41,eh:11.8,stop:8.38,o1:15.43,o2:16.97,cb:0,ch:0,cs:0,tp:17.99,score:'C',rec:'watch',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ELN',name:'El.En.',sector:'Sante lasers medicaux',cap:'small',srd:false,idx:'Europe (EUR)',price:15.37,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'cash 58.0%, croissance CA -4.3%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'59|74|-1|-16',nih:'43|52|48|55',revh:'591|566|576|674',yrs:'2025|2024|2023|2022',dq:'',chg5:-4.4,dy_n:9,dy_med:1.6,div12:0.25,pe_lo:16.2,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:9.8,pfcf_h:15.5,pe_h:18.9,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Milan',gused:-5.9,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-7.6,cagr:-4.3,nde:-1.59,fcfc:58.0,roicx:21.3,chg:-1.47,mkt:'—',b52h:17.64,b52l:10.7,beta:1.07,pe:26.5,pb:2.93,ev_ebitda:11.43,ps:2.02,pfcf:0,ev_ebit:14.4,roe:14.4,roic:20.9,roa:8.2,debt:0.03,de:0.03,ic:87.3,cr:3.01,qr:0,yield:1.6,epsg:0,revg:0,margin:8.4,gm:43.8,om:0,fcf:4.8,capex:0,capr:2.0,capda:1.12,dcfb:9.21,dcfm:10.84,dcfu:13.01,pio:7,alt:6.18,rsi:40.1,mm50:15.7,mm200:14.73,el:8.89,eh:10.06,stop:7.82,o1:11.38,o2:13.01,cb:0,ch:0,cs:0,tp:19.52,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'SL',name:'Sanlorenzo',sector:'Luxe yachts',cap:'small',srd:false,idx:'Europe (EUR)',price:35.28,roiica:false,reinv:false,roiic:13.0,vmed:null,vepv:null,alarm:'',qwhy:'cash 45.0%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'21|-18|73|95',nih:'107|103|93|74',revh:'1112|1030|896|811',yrs:'2025|2024|2023|2022',dq:'',chg5:1.1,dy_n:5,dy_med:1.73,div12:1.05,pe_lo:10.0,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:7.4,pfcf_h:20.3,pe_h:13.6,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'Milan',gused:12.1,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:13.1,cagr:11.1,nde:0.1,fcfc:45.0,roicx:30.3,chg:-2.05,mkt:'—',b52h:40.0,b52l:28.05,beta:0.79,pe:11.42,pb:2.36,ev_ebitda:7.33,ps:1.19,pfcf:0,ev_ebit:8.7,roe:22.8,roic:27.4,roa:7.2,debt:0.29,de:0.29,ic:24.4,cr:1.41,qr:0,yield:2.9,epsg:4.4,revg:6.4,margin:10.4,gm:30.1,om:0,fcf:1.6,capex:0,capr:4.3,capda:1.18,dcfb:37.85,dcfm:44.53,dcfu:53.44,pio:5,alt:2.66,rsi:40.5,mm50:37.31,mm200:34.9,el:34.73,eh:40.61,stop:30.56,o1:46.76,o2:53.44,cb:0,ch:0,cs:0,tp:46.83,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'CEM',name:'Cementir',sector:'Materiaux ciment',cap:'small',srd:false,idx:'Europe (EUR)',price:12.71,roiica:false,reinv:false,roiic:18.0,vmed:null,vepv:null,alarm:'',qwhy:'croissance CA -1.6%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'231|216|194|176',nih:'206|202|201|162',revh:'1640|1687|1694|1723',yrs:'2025|2024|2023|2022',dq:'',chg5:1.5,dy_n:10,dy_med:2.28,div12:0.3,pe_lo:5.9,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:3.0,pfcf_h:7.6,pe_h:7.8,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:0,place:'Milan',gused:3.4,near:false,gimp:null,knife:true,neglect:true,vmeth:'per',nig:8.3,cagr:-1.6,nde:-1.08,fcfc:106.0,roicx:23.1,chg:-0.86,mkt:'—',b52h:20.7,b52l:12.3,beta:0.88,pe:11.77,pb:1.03,ev_ebitda:5.71,ps:1.2,pfcf:0,ev_ebit:6.2,roe:10.2,roic:15.8,roa:5.0,debt:0.08,de:0.08,ic:28.1,cr:2.23,qr:0,yield:2.3,epsg:26.2,revg:5.5,margin:11.9,gm:58.3,om:0,fcf:11.7,capex:0,capr:6.5,capda:0.75,dcfb:12.33,dcfm:14.51,dcfu:17.41,pio:7,alt:2.51,rsi:36.5,mm50:13.82,mm200:15.17,el:12.04,eh:13.52,stop:10.6,o1:15.24,o2:17.41,cb:0,ch:0,cs:0,tp:17.07,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'RWAY',name:'Rai Way',sector:'Infrastructures telecom',cap:'small',srd:false,idx:'Europe (EUR)',price:4.22,roiica:false,reinv:false,roiic:38.8,vmed:5.32,vepv:3.31,alarm:'',qwhy:'croissance officielle 2.5%',qok:false,gsrc:'communique 2026-10-14',fcur:'EUR',fcfh:'94|82|90|61',nih:'89|90|87|74',revh:'283|276|272|245',yrs:'2025|2024|2023|2022',dq:'',chg5:0.0,dy_n:10,dy_med:4.63,div12:0.33,pe_lo:15.8,gmod:2.5,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.0,irrn:8.1,irr:10.1,vmult:5.41,hn:4,eveb_h:8.7,pfcf_h:16.8,pe_h:16.6,news5:'',grid:'',unc:'non evaluee',vopt:5.88,vpess:4.9,nregu:2,regn:3,regu:3,place:'Milan',gused:2.5,near:true,gimp:-4.5,knife:false,neglect:true,vmeth:'qarp',nig:6.3,cagr:4.8,nde:0.73,fcfc:97.0,roicx:29.5,chg:-0.71,mkt:'—',b52h:6.25,b52l:4.1,beta:0.44,pe:13.63,pb:5.91,ev_ebitda:7.91,ps:3.96,pfcf:0,ev_ebit:10.1,roe:57.4,roic:28.9,roa:17.0,debt:1.24,de:1.24,ic:22.5,cr:0.57,qr:0,yield:7.8,epsg:0,revg:2.8,margin:29.8,gm:68.9,om:0,fcf:8.3,capex:0,capr:18.2,capda:0.91,dcfb:4.52,dcfm:5.32,dcfu:6.38,pio:6,alt:3.92,rsi:37.9,mm50:4.46,mm200:5.14,el:3.99,eh:4.52,stop:4.41,o1:5.88,o2:6.47,cb:0,ch:0,cs:0,tp:6.18,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'CMB',name:'Cembre',sector:'Industrie connecteurs electriques',cap:'small',srd:false,idx:'Europe (EUR)',price:80.5,roiica:false,reinv:true,roiic:33.5,vmed:69.51,vepv:27.11,alarm:'',qwhy:'cash 58.0% mais reinvesti a 33.5% (regle reinvestissement)',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'32|18|30|15',nih:'47|43|41|32',revh:'245|230|223|199',yrs:'2025|2024|2023|2022',dq:'',chg5:-4.5,dy_n:10,dy_med:3.88,div12:2.06,pe_lo:15.3,gmod:10.3,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:26.0,irrn:7.1,irr:7.8,vmult:70.84,hn:4,eveb_h:10.0,pfcf_h:35.2,pe_h:16.3,news5:'',grid:'',unc:'non evaluee',vopt:73.08,vpess:48.18,nregu:3,regn:3,regu:3,place:'Milan',gused:10.3,near:true,gimp:15.3,knife:false,neglect:false,vmeth:'qarp',nig:13.5,cagr:7.1,nde:0.01,fcfc:58.0,roicx:20.4,chg:-1.47,mkt:'—',b52h:103.4,b52l:58.7,beta:0.74,pe:25.64,pb:5.93,ev_ebitda:18.67,ps:5.18,pfcf:0,ev_ebit:23.5,roe:24.1,roic:20.0,roa:13.3,debt:0.19,de:0.19,ic:100.1,cr:2.46,qr:0,yield:2.5,epsg:38.3,revg:13.2,margin:20.2,gm:58.3,om:0,fcf:2.4,capex:0,capr:9.9,capda:1.73,dcfb:59.08,dcfm:69.51,dcfu:83.41,pio:5,alt:14.31,rsi:38.3,mm50:83.48,mm200:78.72,el:52.13,eh:59.08,stop:43.36,o1:73.08,o2:80.39,cb:0,ch:0,cs:0,tp:91.67,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'LOG',name:'Logista',sector:'Distribution logistique',cap:'mid',srd:false,idx:'Europe (EUR)',price:36.92,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'ROIC hors EA None',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'350|263|606',nih:'308|272|199',revh:'12986|12428|11464',yrs:'2024|2023|2022',dq:'',chg5:5.0,dy_n:10,dy_med:6.27,div12:2.11,pe_lo:11.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:3,eveb_h:6.1,pfcf_h:10.1,pe_h:11.7,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:2,regn:2,regu:2,place:'Madrid',gused:15.4,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:24.5,cagr:6.4,nde:0.0,fcfc:157.0,roicx:null,chg:-1.49,mkt:'—',b52h:37.76,b52l:28.16,beta:0.45,pe:17.58,pb:7.46,ev_ebitda:6.2,ps:0.35,pfcf:0,ev_ebit:6.0,roe:42.5,roic:34.8,roa:2.4,debt:0.1,de:0.1,ic:51.4,cr:0.91,qr:0,yield:5.4,epsg:17.5,revg:1.7,margin:2.0,gm:6.7,om:0,fcf:7.2,capex:0,capr:0.4,capda:0.28,dcfb:26.73,dcfm:31.45,dcfu:37.74,pio:0,alt:0,rsi:63.4,mm50:35.5,mm200:32.91,el:25.79,eh:29.19,stop:22.7,o1:33.02,o2:37.74,cb:0,ch:0,cs:0,tp:32.7,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ROVI',name:'Laboratorios Rovi',sector:'Pharma',cap:'mid',srd:false,idx:'Europe (EUR)',price:57.6,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'cash 68.0%, croissance CA -3.1%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'119|76|58|186',nih:'140|137|170|200',revh:'743|764|830|818',yrs:'2025|2024|2023|2022',dq:'',chg5:-1.5,dy_n:10,dy_med:1.17,div12:0.959,pe_lo:9.5,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:14.0,pfcf_h:34.8,pe_h:20.7,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Madrid',gused:-7.1,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-11.1,cagr:-3.1,nde:0.11,fcfc:68.0,roicx:25.2,chg:-1.2,mkt:'—',b52h:86.7,b52l:53.1,beta:0.27,pe:15.91,pb:4.2,ev_ebitda:16.92,ps:3.81,pfcf:0,ev_ebit:16.0,roe:28.6,roic:25.2,roa:9.4,debt:0.15,de:0.15,ic:72.5,cr:2.05,qr:0,yield:1.6,epsg:246.7,revg:20.0,margin:24.0,gm:64.7,om:0,fcf:4.0,capex:0,capr:9.1,capda:2.23,dcfb:41.72,dcfm:49.08,dcfu:58.9,pio:6,alt:9.06,rsi:46.0,mm50:58.74,mm200:65.74,el:34.36,eh:43.19,stop:30.24,o1:51.53,o2:58.9,cb:0,ch:0,cs:0,tp:73.24,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'HEIJM',name:'Heijmans',sector:'Construction et infrastructures',cap:'small',srd:false,idx:'Europe (EUR)',price:81.2,roiica:false,reinv:false,roiic:23.0,vmed:73.16,vepv:35.15,alarm:'',qwhy:'',qok:true,gsrc:'communique 2026-10-14',fcur:'EUR',fcfh:'228|219|39|85',nih:'130|90|60|60',revh:'2772|2584|2117|1812',yrs:'2025|2024|2023|2022',dq:'',chg5:0.9,dy_n:5,dy_med:5.69,div12:2.37,pe_lo:4.0,gmod:9.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:15.0,irrn:11.3,irr:11.7,vmult:73.16,hn:4,eveb_h:4.1,pfcf_h:6.2,pe_h:7.7,news5:'',grid:'',unc:'non evaluee',vopt:146.47,vpess:85.36,nregu:3,regn:3,regu:3,place:'Amsterdam',gused:9.0,near:false,gimp:-1.1,knife:false,neglect:false,vmeth:'qarp',nig:29.8,cagr:15.2,nde:-0.21,fcfc:168.0,roicx:38.5,chg:-1.81,mkt:'—',b52h:117.8,b52l:53.65,beta:1.3,pe:15.29,pb:4.02,ev_ebitda:11.05,ps:0.75,pfcf:0,ev_ebit:12.0,roe:28.0,roic:24.4,roa:6.7,debt:0.25,de:0.25,ic:18.7,cr:1.01,qr:0,yield:2.9,epsg:23.7,revg:15.8,margin:4.8,gm:16.4,om:0,fcf:10.2,capex:0,capr:1.6,capda:0.75,dcfb:108.93,dcfm:128.15,dcfu:153.78,pio:6,alt:3.49,rsi:40.4,mm50:86.72,mm200:87.69,el:96.11,eh:108.93,stop:76.82,o1:146.47,o2:161.12,cb:0,ch:0,cs:0,tp:0,score:'A',rec:'watch',zone:true,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'THEON',name:'Theon International',sector:'Defense optronique',cap:'small',srd:false,idx:'Europe (EUR)',price:28.82,roiica:false,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'cash -13.0%, dette/EBITDA None',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'|-37|30|-11',nih:'|67|36|30',revh:'|352|219|143',yrs:'2025|2024|2023|2022',dq:'croissance Yahoo 57.0 %/an : probablement faussee par une acquisition ou une cession',chg5:3.7,dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:1,eveb_h:10.0,pfcf_h:null,pe_h:14.0,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:2,regn:2,regu:2,place:'Amsterdam',gused:53.5,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:49.9,cagr:57.0,nde:null,fcfc:-13.0,roicx:40.8,chg:-2.37,mkt:'—',b52h:39.5,b52l:23.56,beta:1.06,pe:17.36,pb:5.0,ev_ebitda:19.88,ps:4.4,pfcf:0,ev_ebit:null,roe:34.4,roic:40.8,roa:11.2,debt:0.73,de:0.73,ic:null,cr:3.0,qr:0,yield:1.1,epsg:15.4,revg:38.5,margin:23.8,gm:33.8,om:0,fcf:null,capex:0,capr:null,capda:null,dcfb:19.42,dcfm:22.85,dcfu:27.42,pio:0,alt:0,rsi:44.9,mm50:31.84,mm200:31.66,el:19.19,eh:21.39,stop:16.89,o1:23.99,o2:27.42,cb:0,ch:0,cs:0,tp:39.3,score:'D',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'LOTB',name:'Lotus Bakeries',sector:'Agroalimentaire biscuits',cap:'mid',srd:false,idx:'Europe (EUR)',price:13000.0,roiica:false,reinv:true,roiic:24.0,vmed:5653.37,vepv:3900.0,alarm:'',qwhy:'cash 42.0% mais reinvesti a 24.0% (regle reinvestissement)',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'93|64|89|-12',nih:'172|153|129|103',revh:'1355|1232|1063|877',yrs:'2025|2024|2023|2022',dq:'',chg5:5.0,dy_n:10,dy_med:0.73,div12:90.0,pe_lo:38.8,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:30.0,irrn:5.1,irr:5.3,vmult:6467.56,hn:4,eveb_h:33.1,pfcf_h:75.1,pe_h:50.7,news5:'',grid:'',unc:'non evaluee',vopt:5653.37,vpess:3900.0,nregu:3,regn:3,regu:3,place:'Bruxelles',gused:17.1,near:true,gimp:30.0,knife:false,neglect:false,vmeth:'qarp',nig:18.6,cagr:15.6,nde:0.71,fcfc:42.0,roicx:21.0,chg:0.93,mkt:'—',b52h:13200.0,b52l:7270.0,beta:0.61,pe:55.36,pb:11.78,ev_ebitda:36.39,ps:7.3,pfcf:0,ev_ebit:46.4,roe:23.0,roic:16.1,roa:10.4,debt:0.46,de:0.46,ic:69.3,cr:1.67,qr:0,yield:0.7,epsg:23.4,revg:14.0,margin:13.2,gm:40.2,om:0,fcf:0.9,capex:0,capr:8.3,capda:2.81,dcfb:4805.36,dcfm:5653.37,dcfu:6784.04,pio:7,alt:11.71,rsi:64.7,mm50:12442.0,mm200:10936.05,el:4240.03,eh:4805.36,stop:3510.0,o1:5653.37,o2:6218.71,cb:0,ch:0,cs:0,tp:12891.08,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'JMT',name:'Jeronimo Martins',sector:'Distribution alimentaire',cap:'large',srd:false,idx:'Europe (EUR)',price:18.65,roiica:true,reinv:false,roiic:6.9,vmed:20.45,vepv:7.61,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'1368|649|945|1208',nih:'646|599|756|590',revh:'35991|33464|30608|25385',yrs:'2025|2024|2023|2022',dq:'',chg5:8.9,dy_n:10,dy_med:2.64,div12:0.65,pe_lo:19.2,gmod:7.7,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:0.0,irrn:9.0,irr:9.0,vmult:24.68,hn:4,eveb_h:7.3,pfcf_h:12.9,pe_h:19.8,news5:'',grid:'',unc:'non evaluee',vopt:22.86,vpess:15.36,nregu:2,regn:3,regu:3,place:'Lisbonne',gused:7.7,near:false,gimp:5.2,knife:false,neglect:false,vmeth:'qarp',nig:3.1,cagr:12.3,nde:1.38,fcfc:161.0,roicx:18.7,chg:2.59,mkt:'—',b52h:22.68,b52l:16.11,beta:0.49,pe:18.47,pb:3.74,ev_ebitda:8.04,ps:0.32,pfcf:0,ev_ebit:12.9,roe:20.0,roic:16.5,roa:5.2,debt:1.79,de:1.79,ic:3.4,cr:0.61,qr:0,yield:3.6,epsg:-0.5,revg:4.0,margin:1.7,gm:20.8,om:0,fcf:11.7,capex:0,capr:2.9,capda:0.92,dcfb:17.38,dcfm:20.45,dcfu:24.54,pio:6,alt:2.86,rsi:66.2,mm50:17.7,mm200:18.65,el:15.34,eh:17.38,stop:13.82,o1:22.86,o2:25.15,cb:0,ch:0,cs:0,tp:22.43,score:'C',rec:'watch',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ANDR',name:'Andritz',sector:'Industrie equipements',cap:'mid',srd:false,idx:'Europe (EUR)',price:79.7,roiica:false,reinv:false,roiic:12.6,vmed:null,vepv:null,alarm:'',qwhy:'croissance CA 1.5%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'455|457|204|556',nih:'456|496|510|410',revh:'7883|8314|8660|7543',yrs:'2025|2024|2023|2022',dq:'',chg5:-3.2,dy_n:10,dy_med:3.52,div12:2.7,pe_lo:9.7,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:4,eveb_h:5.9,pfcf_h:12.5,pe_h:11.9,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'VI',gused:2.6,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:3.7,cagr:1.5,nde:-0.09,fcfc:89.0,roicx:45.5,chg:-1.73,mkt:'—',b52h:87.7,b52l:57.95,beta:1.32,pe:16.81,pb:3.21,ev_ebitda:9.62,ps:0.97,pfcf:0,ev_ebit:11.6,roe:20.2,roic:25.5,roa:4.5,debt:0.25,de:0.25,ic:13.3,cr:1.07,qr:0,yield:3.3,epsg:6.7,revg:8.5,margin:5.8,gm:49.7,om:0,fcf:5.8,capex:0,capr:2.5,capda:0.82,dcfb:59.52,dcfm:70.02,dcfu:84.02,pio:5,alt:2.01,rsi:39.8,mm50:82.61,mm200:74.16,el:58.12,eh:65.26,stop:51.15,o1:73.52,o2:84.02,cb:0,ch:0,cs:0,tp:93.86,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'WRT1V',name:'Wartsila',sector:'Industrie moteurs marins et energie',cap:'large',srd:false,idx:'Europe (EUR)',price:28.6,roiica:false,reinv:false,roiic:null,vmed:10.39,vepv:10.39,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'1448|1038|674|-218',nih:'626|503|258|-64',revh:'6914|6449|6015|5842',yrs:'2025|2024|2023|2022',dq:'',chg5:-4.5,dy_n:10,dy_med:2.56,div12:1.06,pe_lo:20.3,gmod:5.8,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:35.0,irrn:4.0,irr:4.6,vmult:10.43,hn:3,eveb_h:14.6,pfcf_h:11.5,pe_h:29.2,news5:'',grid:'cyclique',unc:'elevee',vopt:10.94,vpess:8.58,nregu:3,regn:3,regu:3,place:'Helsinki',gused:5.8,near:false,gimp:30.0,knife:false,neglect:false,vmeth:'qarp',nig:null,cagr:5.8,nde:-1.9,fcfc:222.0,roicx:31.6,chg:-3.05,mkt:'—',b52h:40.75,b52l:25.0,beta:1.2,pe:25.31,pb:6.66,ev_ebitda:18.19,ps:2.45,pfcf:0,ev_ebit:17.6,roe:26.4,roic:22.8,roa:6.1,debt:0.22,de:0.22,ic:13.9,cr:1.22,qr:0,yield:1.8,epsg:7.8,revg:-2.2,margin:9.6,gm:46.7,om:0,fcf:8.6,capex:0,capr:2.2,capda:0.91,dcfb:8.4,dcfm:9.88,dcfu:11.86,pio:8,alt:3.62,rsi:46.7,mm50:28.96,mm200:31.96,el:6.92,eh:7.9,stop:7.72,o1:10.94,o2:12.03,cb:0,ch:0,cs:0,tp:33.04,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ORNBV',name:'Orion',sector:'Pharma',cap:'mid',srd:false,idx:'Europe (EUR)',price:88.05,roiica:false,reinv:true,roiic:24.4,vmed:104.94,vepv:35.99,alarm:'',qwhy:'cash 57.0% mais reinvesti a 24.4% (regle reinvestissement)',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'EUR',fcfh:'219|206|2|361',nih:'500|330|217|350',revh:'1890|1542|1190|1341',yrs:'2025|2024|2023|2022',dq:'',chg5:7.7,dy_n:10,dy_med:3.82,div12:1.8,pe_lo:17.8,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:35.0,irrn:8.8,irr:9.5,vmult:107.04,hn:4,eveb_h:13.8,pfcf_h:29.8,pe_h:19.6,news5:'',grid:'',unc:'non evaluee',vopt:104.94,vpess:66.69,nregu:2,regn:3,regu:2,place:'Helsinki',gused:12.4,near:true,gimp:7.0,knife:false,neglect:false,vmeth:'qarp',nig:12.7,cagr:12.1,nde:0.21,fcfc:57.0,roicx:35.0,chg:0.4,mkt:'—',b52h:88.05,b52l:56.5,beta:0.28,pe:21.12,pb:9.77,ev_ebitda:15.56,ps:6.01,pfcf:0,ev_ebit:19.4,roe:53.7,roic:32.6,roa:26.3,debt:0.1,de:0.1,ic:77.6,cr:2.64,qr:0,yield:2.0,epsg:69.5,revg:25.2,margin:28.5,gm:65.9,om:0,fcf:1.8,capex:0,capr:5.2,capda:1.72,dcfb:89.2,dcfm:104.94,dcfu:125.93,pio:6,alt:11.22,rsi:70.2,mm50:80.21,mm200:72.32,el:78.7,eh:89.2,stop:60.02,o1:104.94,o2:115.43,cb:0,ch:0,cs:0,tp:77.33,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ALFA',name:'Alfa Laval',sector:'Industrie echangeurs thermiques',cap:'large',srd:false,idx:'Europe (SEK)',price:51.43,roiica:false,reinv:false,roiic:48.6,vmed:42.64,vepv:15.43,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'SEK',fcfh:'6506|9442|6729|1438',nih:'8272|7391|6330|4503',revh:'69675|66953|63598|52135',yrs:'2025|2024|2023|2022',dq:'',chg5:-1.8,dy_n:9,dy_med:1.96,div12:0.81,pe_lo:23.4,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:30.0,irrn:7.1,irr:7.6,vmult:45.69,hn:4,eveb_h:15.4,pfcf_h:27.3,pe_h:26.4,news5:'',grid:'',unc:'non evaluee',vopt:42.64,vpess:28.26,nregu:3,regn:3,regu:3,place:'Stockholm',gused:16.3,near:false,gimp:17.5,knife:false,neglect:false,vmeth:'qarp',nig:22.5,cagr:10.1,nde:0.97,fcfc:91.0,roicx:30.5,chg:-0.76,mkt:'—',b52h:53.53,b52l:38.34,beta:0.77,pe:28.86,pb:5.2,ev_ebitda:18.48,ps:3.36,pfcf:0,ev_ebit:21.6,roe:19.1,roic:14.7,roa:7.5,debt:0.46,de:0.46,ic:20.6,cr:1.12,qr:0,yield:1.6,epsg:0.7,revg:7.7,margin:11.6,gm:36.3,om:0,fcf:2.8,capex:0,capr:3.8,capda:1.06,dcfb:36.25,dcfm:42.64,dcfu:51.17,pio:6,alt:4.42,rsi:52.2,mm50:50.56,mm200:48.46,el:31.98,eh:36.25,stop:25.44,o1:42.64,o2:46.91,cb:0,ch:0,cs:0,tp:53.03,score:'C',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'ADDT',name:'Addtech',sector:'Industrie distribution technique',cap:'mid',srd:false,idx:'Europe (SEK)',price:29.89,roiica:false,reinv:false,roiic:16.9,vmed:14.34,vepv:8.97,alarm:'Piotroski 4/9',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'SEK',fcfh:'2812|2476|2386|1714',nih:'2147|1892|1632|1495',revh:'22703|21796|20019|18714',yrs:'2026|2025|2024|2023',dq:'',chg5:3.4,dy_n:10,dy_med:1.21,div12:0.32,pe_lo:34.7,gmod:9.8,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:30.0,irrn:5.2,irr:5.5,vmult:14.89,hn:4,eveb_h:21.5,pfcf_h:30.3,pe_h:40.0,news5:'',grid:'',unc:'non evaluee',vopt:15.5,vpess:10.23,nregu:3,regn:3,regu:3,place:'Stockholm',gused:9.8,near:false,gimp:30.0,knife:false,neglect:false,vmeth:'qarp',nig:12.8,cagr:6.7,nde:1.38,fcfc:131.0,roicx:33.9,chg:0.18,mkt:'—',b52h:32.85,b52l:25.46,beta:1.08,pe:40.29,pb:10.44,ev_ebitda:24.93,ps:3.9,pfcf:0,ev_ebit:31.0,roe:26.9,roic:18.0,roa:9.6,debt:0.75,de:0.75,ic:15.2,cr:1.76,qr:0,yield:1.1,epsg:14.8,revg:5.7,margin:9.6,gm:33.6,om:0,fcf:3.1,capex:0,capr:0.8,capda:0.18,dcfb:12.19,dcfm:14.34,dcfu:17.21,pio:4,alt:6.15,rsi:50.7,mm50:29.97,mm200:29.19,el:10.75,eh:12.19,stop:9.21,o1:15.5,o2:17.05,cb:0,ch:0,cs:0,tp:34.42,score:'C',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'LAGR',name:'Lagercrantz',sector:'Industrie technologie de niche',cap:'mid',srd:false,idx:'Europe (SEK)',price:21.04,roiica:false,reinv:false,roiic:15.7,vmed:10.55,vepv:6.31,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'SEK',fcfh:'1288|1153|1202|892',nih:'1200|1019|877|758',revh:'10610|9389|8129|7246',yrs:'2026|2025|2024|2023',dq:'',chg5:2.9,dy_n:10,dy_med:1.3,div12:0.22,pe_lo:34.4,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:30.0,irrn:5.4,irr:5.7,vmult:11.09,hn:4,eveb_h:20.9,pfcf_h:31.0,pe_h:36.9,news5:'',grid:'',unc:'non evaluee',vopt:10.55,vpess:7.04,nregu:3,regn:3,regu:3,place:'Stockholm',gused:15.1,near:false,gimp:30.0,knife:false,neglect:false,vmeth:'qarp',nig:16.5,cagr:13.6,nde:1.82,fcfc:118.0,roicx:30.5,chg:0.6,mkt:'—',b52h:23.99,b52l:16.65,beta:1.15,pe:38.61,pb:10.21,ev_ebitda:24.7,ps:4.37,pfcf:0,ev_ebit:31.0,roe:28.5,roic:15.5,roa:8.4,debt:1.04,de:1.04,ic:9.8,cr:1.31,qr:0,yield:1.1,epsg:20.3,revg:17.6,margin:11.3,gm:39.1,om:0,fcf:2.7,capex:0,capr:2.0,capda:0.36,dcfb:8.97,dcfm:10.55,dcfu:12.67,pio:7,alt:5.13,rsi:60.1,mm50:20.25,mm200:20.1,el:7.92,eh:8.97,stop:6.33,o1:10.55,o2:11.61,cb:0,ch:0,cs:0,tp:24.17,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'SECT',name:'Sectra',sector:'Logiciel imagerie medicale',cap:'mid',srd:false,idx:'Europe (SEK)',price:28.75,roiica:false,reinv:false,roiic:null,vmed:8.63,vepv:8.63,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'SEK',fcfh:'909|812|76|348',nih:'564|563|428|375',revh:'3547|3243|2966|2351',yrs:'2026|2025|2024|2023',dq:'',chg5:1.9,dy_n:10,dy_med:0.78,div12:0.21,pe_lo:83.1,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:30.0,irrn:4.0,irr:4.1,vmult:8.63,hn:4,eveb_h:59.8,pfcf_h:71.7,pe_h:93.3,news5:'',grid:'',unc:'non evaluee',vopt:8.63,vpess:8.63,nregu:3,regn:3,regu:3,place:'Stockholm',gused:14.6,near:false,gimp:30.0,knife:false,neglect:false,vmeth:'qarp',nig:14.6,cagr:14.7,nde:-2.03,fcfc:111.0,roicx:83.5,chg:0.95,mkt:'—',b52h:29.17,b52l:15.58,beta:0.9,pe:99.32,pb:26.54,ev_ebitda:73.15,ps:16.46,pfcf:0,ev_ebit:80.7,roe:28.3,roic:76.8,roa:11.7,debt:0.05,de:0.05,ic:98.0,cr:1.75,qr:0,yield:0.4,epsg:53.8,revg:25.8,margin:16.5,gm:36.6,om:0,fcf:1.5,capex:0,capr:5.3,capda:1.63,dcfb:7.33,dcfm:8.63,dcfu:10.35,pio:5,alt:16.96,rsi:69.4,mm50:26.01,mm200:23.1,el:6.47,eh:7.33,stop:7.76,o1:8.63,o2:9.49,cb:0,ch:0,cs:0,tp:30.57,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'MYCR',name:'Mycronic',sector:'Electronique equipements',cap:'mid',srd:false,idx:'Europe (SEK)',price:26.99,roiica:false,reinv:false,roiic:56.0,vmed:22.36,vepv:8.1,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'SEK',fcfh:'1242|1636|1416|712',nih:'1560|1683|998|741',revh:'7938|7057|5706|5119',yrs:'2025|2024|2023|2022',dq:'',chg5:-11.1,dy_n:10,dy_med:1.78,div12:0.29,pe_lo:23.6,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:30.0,irrn:7.4,irr:7.7,vmult:22.36,hn:4,eveb_h:16.3,pfcf_h:25.6,pe_h:26.5,news5:'Mycronic AB (publ) reçoit une commande de deux machines d’écriture de masques SLX d’un client aux États-Unis|https://news.google.com/rss/articles/CBMi7gFBVV95cUxPZ09qWlJ3MmxqRHE4RzNWdDFXZ0VRZFlvVGRhejJBRlJRSGRuWHpFMWc2Rzh6enNxY01oa1RnRllwaTRDV2RnS0d0ZThiSklzNGZCZ0hHR08tRkVsY3BscXpoQXI4RVRwQm50Z3ZvSF9ib3RNdzZleGJtMTdhakJYY2dhaGF1b2dzSF9MeVEwMEZlTVBXVkV1S1dvb0RVcHhORGxSc3QtY2k0a2JlZWd5S1J4QTNNZEtzajdZSVhTQ1pObE5zY1pWZUU0ODlINlhqdmUtMVBxakdLUjQ0SGxlM0lJOHFmaVpOOWpBOVFn?oc=5|Zonebourse',grid:'',unc:'non evaluee',vopt:23.06,vpess:13.07,nregu:2,regn:3,regu:3,place:'Stockholm',gused:21.9,near:false,gimp:15.4,knife:false,neglect:false,vmeth:'qarp',nig:28.2,cagr:15.7,nde:-0.85,fcfc:100.0,roicx:64.5,chg:0.67,mkt:'—',b52h:32.76,b52l:16.48,beta:0.63,pe:33.81,pb:7.44,ev_ebitda:21.6,ps:6.78,pfcf:0,ev_ebit:28.2,roe:23.7,roic:30.4,roa:13.1,debt:0.05,de:0.05,ic:116.9,cr:2.23,qr:0,yield:1.1,epsg:18.4,revg:16.9,margin:20.1,gm:54.1,om:0,fcf:2.1,capex:0,capr:2.1,capda:0.5,dcfb:19.6,dcfm:23.06,dcfu:27.67,pio:6,alt:11.67,rsi:33.1,mm50:29.35,mm200:24.87,el:17.29,eh:19.6,stop:11.76,o1:23.06,o2:25.36,cb:0,ch:0,cs:0,tp:28.64,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'PNDORA',name:'Pandora',sector:'Bijouterie',cap:'large',srd:false,idx:'Europe (DKK)',price:113.19,roiica:false,reinv:false,roiic:13.0,vmed:89.43,vepv:89.43,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'DKK',fcfh:'5450|7042|5896|3243',nih:'5241|5227|4740|5029',revh:'32549|31680|28136|26463',yrs:'2025|2024|2023|2022',dq:'',chg5:5.0,dy_n:10,dy_med:2.23,div12:2.94,pe_lo:8.6,gmod:4.2,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:27.0,irrn:7.8,irr:8.5,vmult:75.15,hn:4,eveb_h:8.0,pfcf_h:13.2,pe_h:13.0,news5:'',grid:'',unc:'non evaluee',vopt:125.67,vpess:95.91,nregu:2,regn:3,regu:3,place:'Copenhague',gused:4.2,near:false,gimp:4.4,knife:false,neglect:false,vmeth:'qarp',nig:1.4,cagr:7.1,nde:1.33,fcfc:107.0,roicx:51.2,chg:-0.12,mkt:'—',b52h:121.0,b52l:57.53,beta:1.28,pe:12.53,pb:14.7,ev_ebitda:8.92,ps:1.95,pfcf:0,ev_ebit:10.2,roe:131.2,roic:34.9,roa:17.1,debt:3.84,de:3.84,ic:9.2,cr:0.83,qr:0,yield:2.6,epsg:13.6,revg:2.0,margin:15.9,gm:78.8,om:0,fcf:8.6,capex:0,capr:5.9,capda:0.74,dcfb:95.55,dcfm:112.41,dcfu:134.89,pio:5,alt:3.79,rsi:58.6,mm50:109.46,mm200:85.68,el:84.31,eh:95.55,stop:86.32,o1:125.67,o2:138.24,cb:0,ch:0,cs:0,tp:114.68,score:'C',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'NOD',name:'Nordic Semiconductor',sector:'Semi-conducteurs',cap:'mid',srd:false,idx:'Europe (NOK)',price:16.25,roiica:true,reinv:false,roiic:null,vmed:null,vepv:null,alarm:'',qwhy:'ROIC hors EA 3.8, ROIC 3.3, cash 33.0%, perte exploitation, croissance CA -4.9%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'USD',fcfh:'59|31|-166|112',nih:'16|-39|8|122',revh:'668|511|543|777',yrs:'2025|2024|2023|2022',dq:'benefice 12 mois anormal (PER 108.6 contre 35.4 attendu)',chg5:-1.1,dy_n:0,dy_med:null,div12:null,pe_lo:null,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmult:null,hn:3,eveb_h:38.0,pfcf_h:45.5,pe_h:95.4,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:1,regn:3,regu:1,place:'Oslo',gused:-26.8,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:-48.8,cagr:-4.9,nde:-2.12,fcfc:33.0,roicx:3.8,chg:1.18,mkt:'—',b52h:19.98,b52l:11.72,beta:0.92,pe:108.61,pb:5.11,ev_ebitda:604.47,ps:44.69,pfcf:0,ev_ebit:1363.8,roe:5.0,roic:3.3,roa:2.7,debt:0.23,de:0.23,ic:2.1,cr:3.55,qr:0,yield:0,epsg:57.7,revg:33.2,margin:4.2,gm:53.0,om:0,fcf:0.2,capex:0,capr:8.5,capda:1.31,dcfb:12.51,dcfm:14.71,dcfu:17.66,pio:6,alt:68.76,rsi:43.0,mm50:16.42,mm200:15.79,el:10.59,eh:13.07,stop:9.32,o1:15.45,o2:17.66,cb:0,ch:0,cs:0,tp:18.57,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'GOOGL',name:'Alphabet',sector:'Internet & publicite (compte-titres)',cap:'large',srd:false,idx:'Etats-Unis (USD)',price:306.91,alarm:'',qwhy:'cash 75.0% mais reinvesti a 40.3% (regle reinvestissement)',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'USD',fcfh:'73266|72764|69495|60010',nih:'132170|100118|73795|59972',revh:'402836|350018|307394|282836',yrs:'2025|2024|2023|2022',dq:'',chg5:-2.4,dy_n:0,dy_med:null,div12:null,pe_lo:18.9,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:0.0,irrn:8.3,irr:8.3,vmed:288.23,vepv:169.57,vmult:288.23,hn:4,eveb_h:17.5,pfcf_h:28.6,pe_h:23.5,news5:'',grid:'',unc:'non evaluee',vopt:294.95,vpess:196.64,nregu:3,regn:3,regu:3,place:'?',gused:21.3,roiica:false,reinv:true,roiic:40.3,near:true,gimp:13.2,knife:false,neglect:false,vmeth:'qarp',nig:30.1,cagr:12.5,nde:0.16,fcfc:75.0,roicx:30.6,chg:1.05,mkt:'—',b52h:364.36,b52l:217.71,beta:1.21,pe:17.27,pb:6.76,ev_ebitda:23.46,ps:9.44,pfcf:0,ev_ebit:25.5,roe:48.7,roic:27.9,roa:13.0,debt:0.19,de:0.19,ic:216.8,cr:2.72,qr:0,yield:0.3,epsg:294.0,revg:24.2,margin:54.8,gm:60.9,om:0,fcf:1.7,capex:0,capr:22.7,capda:4.33,dcfb:250.7,dcfm:294.95,dcfu:353.93,pio:6,alt:0,rsi:48.1,mm50:307.0,mm200:303.82,el:221.21,eh:250.7,stop:176.98,o1:294.95,o2:324.45,cb:0,ch:0,cs:0,tp:383.48,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'MA',name:'Mastercard',sector:'Paiements (compte-titres)',cap:'large',srd:false,idx:'Etats-Unis (USD)',price:549.53,alarm:'',qwhy:'',qok:true,gsrc:'yahoo (4 ans publies)',fcur:'USD',fcfh:'16433|13586|10892|10098',nih:'14968|12874|11195|9930',revh:'32791|28167|25098|22237',yrs:'2025|2024|2023|2022',dq:'',chg5:3.6,dy_n:10,dy_med:0.54,div12:3.1,pe_lo:33.5,gmod:12.0,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:0.0,irrn:7.7,irr:7.7,vmed:435.6,vepv:164.86,vmult:435.6,hn:4,eveb_h:26.6,pfcf_h:34.0,pe_h:34.6,news5:'',grid:'',unc:'non evaluee',vopt:468.17,vpess:265.39,nregu:3,regn:3,regu:3,place:'?',gused:14.2,roiica:false,reinv:false,roiic:182.7,near:false,gimp:15.5,knife:false,neglect:false,vmeth:'qarp',nig:14.7,cagr:13.8,nde:0.41,fcfc:104.0,roicx:186.5,chg:-0.19,mkt:'—',b52h:555.07,b52l:414.21,beta:0.76,pe:33.9,pb:96.35,ev_ebitda:24.95,ps:15.39,pfcf:0,ev_ebit:28.7,roe:241.2,roic:82.8,roa:24.1,debt:4.4,de:4.4,ic:26.7,cr:1.06,qr:0,yield:0.6,epsg:22.1,revg:14.1,margin:46.3,gm:100.0,om:0,fcf:3.0,capex:0,capr:3.7,capda:1.06,dcfb:397.95,dcfm:468.17,dcfu:561.81,pio:8,alt:10.92,rsi:74.1,mm50:513.57,mm200:474.01,el:351.12,eh:397.95,stop:238.85,o1:468.17,o2:514.98,cb:0,ch:0,cs:0,tp:600.22,score:'B',rec:'hold',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'AMZN',name:'Amazon',sector:'Commerce en ligne & cloud (compte-titres)',cap:'large',srd:false,idx:'Etats-Unis (USD)',price:234.03,alarm:'',qwhy:'ROIC hors EA 14.6, cash 34.0%',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'USD',fcfh:'7695|32878|32217|-16893',nih:'77670|59248|30425|-2722',revh:'716924|637959|574785|513983',yrs:'2025|2024|2023|2022',dq:'',chg5:1.1,dy_n:0,dy_med:null,div12:null,pe_lo:31.3,gmod:null,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:null,irrn:null,irr:null,vmed:null,vepv:null,vmult:null,hn:3,eveb_h:19.0,pfcf_h:60.6,pe_h:40.1,news5:'',grid:'',unc:'',vopt:null,vpess:null,nregu:3,regn:3,regu:3,place:'?',gused:11.7,roiica:false,reinv:false,roiic:31.6,near:false,gimp:null,knife:false,neglect:false,vmeth:'per',nig:null,cagr:11.7,nde:0.4,fcfc:34.0,roicx:14.6,chg:4.98,mkt:'—',b52h:256.1,b52l:174.77,beta:1.46,pe:21.11,pb:5.13,ev_ebitda:16.73,ps:3.65,pfcf:0,ev_ebit:28.4,roe:30.6,roic:13.6,roa:6.6,debt:0.46,de:0.46,ic:43.8,cr:1.03,qr:0,yield:0,epsg:242.3,revg:19.6,margin:17.4,gm:50.8,om:0,fcf:0.3,capex:0,capr:18.4,capda:2.0,dcfb:137.06,dcfm:161.25,dcfu:193.5,pio:5,alt:5.9,rsi:57.3,mm50:229.02,mm200:216.59,el:132.22,eh:149.64,stop:116.36,o1:169.31,o2:193.5,cb:0,ch:0,cs:0,tp:295.79,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
,{ticker:'KO',name:'Coca-Cola',sector:'Boissons (compte-titres)',cap:'large',srd:false,idx:'Etats-Unis (USD)',price:83.32,alarm:'',qwhy:'cash 67.0% mais reinvesti a 30.8% (regle reinvestissement)',qok:false,gsrc:'yahoo (4 ans publies)',fcur:'USD',fcfh:'5296|4741|9747|9534',nih:'13107|10631|10714|9542',revh:'47941|47061|45754|43004',yrs:'2025|2024|2023|2022',dq:'',chg5:4.1,dy_n:10,dy_med:3.12,div12:1.87,pe_lo:22.7,gmod:7.4,icr:null,ltv:null,bvg:null,roemin:null,roem:null,wht:0.0,irrn:6.8,irr:6.8,vmed:58.0,vepv:24.99,vmult:64.57,hn:4,eveb_h:18.6,pfcf_h:42.5,pe_h:24.3,news5:'',grid:'',unc:'non evaluee',vopt:64.14,vpess:45.21,nregu:2,regn:3,regu:3,place:'?',gused:7.4,roiica:false,reinv:true,roiic:30.8,near:true,gimp:18.2,knife:false,neglect:false,vmeth:'qarp',nig:11.2,cagr:3.7,nde:1.88,fcfc:67.0,roicx:29.6,chg:-0.5,mkt:'—',b52h:83.91,b52l:59.98,beta:0.32,pe:28.06,pb:11.12,ev_ebitda:25.54,ps:8.02,pfcf:0,ev_ebit:24.6,roe:42.1,roic:20.4,roa:9.4,debt:1.16,de:1.16,ic:10.7,cr:1.3,qr:0,yield:2.3,epsg:16.9,revg:6.7,margin:28.6,gm:61.9,om:0,fcf:1.3,capex:0,capr:4.4,capda:2.01,dcfb:49.29,dcfm:58.0,dcfu:69.6,pio:7,alt:5.62,rsi:72.4,mm50:78.74,mm200:71.58,el:43.5,eh:49.29,stop:40.69,o1:64.14,o2:70.55,cb:0,ch:0,cs:0,tp:84.48,score:'C',rec:'avoid',zone:false,moat:[],cats:[],ins:[],peers:[],risks:{},track:[],thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.'}
];



// ═══════════ CALENDRIER RÉSULTATS ═══════════
const CAL = {"MC": {"q1": "2026-04-10", "q2": "2026-07-24", "q3": "2026-10-15", "an": "2027-02-05", "desc": "LVMH - CA trimestriel"}, "AI": {"q1": "2026-04-29", "q2": "2026-07-30", "q3": "2026-10-29", "an": "2027-02-26", "desc": "Air Liquide - Résultats semestriels"}, "RMS": {"q1": "2026-04-23", "q2": "2026-07-31", "q3": "2026-10-29", "an": "2027-02-12", "desc": "Hermès - CA trimestriel"}, "SAF": {"q1": "2026-02-27", "q2": "2026-07-30", "q3": "2026-10-29", "an": "2026-02-27", "desc": "Safran - Résultats annuels"}, "GTT": {"q1": "2026-03-20", "q2": "2026-09-18", "an": "2026-03-20", "desc": "GTT - Semestriel"}, "SU": {"q1": "2026-04-24", "q2": "2026-07-28", "q3": "2026-10-27", "an": "2027-02-19", "desc": "Schneider Electric"}, "OR": {"q1": "2026-04-14", "q2": "2026-07-28", "q3": "2026-10-20", "an": "2027-02-10", "desc": "L'Oréal - CA trimestriel"}, "TTE": {"q1": "2026-04-25", "q2": "2026-07-26", "q3": "2026-10-24", "an": "2027-02-12", "desc": "TotalEnergies"}, "BNP": {"q1": "2026-04-30", "q2": "2026-07-31", "q3": "2026-10-30", "an": "2027-02-05", "desc": "BNP Paribas"}, "ASML": {"q1": "2026-04-15", "q2": "2026-07-16", "q3": "2026-10-15", "an": "2027-01-21", "desc": "ASML - Résultats trimestriels"}, "ALFPC": {"q1": "2026-03-28", "q2": "2026-09-18", "an": "2026-03-28", "desc": "Fountaine Pajot - Semestriel"}, "SELENV": {"q1": "2026-03-13", "q2": "2026-09-11", "an": "2026-03-13", "desc": "Séché Environnement"}, "VIRBAC": {"q1": "2026-04-20", "q2": "2026-07-24", "an": "2027-02-20", "desc": "Virbac - CA trimestriel"}, "COFA": {"q1": "2026-02-19", "q2": "2026-07-31", "an": "2026-02-19", "desc": "Coface"}, "IPSEN": {"q1": "2026-04-22", "q2": "2026-07-30", "an": "2027-02-24", "desc": "Ipsen"}, "PERNOD": {"q1": "2026-02-13", "q2": "2026-07-30", "an": "2026-09-12", "desc": "Pernod Ricard"}, "NOVO": {"q1": "2026-02-05", "q2": "2026-08-13", "an": "2027-02-04", "desc": "Novo Nordisk"}, "HO": {"q1": "2026-04-24", "q2": "2026-07-25", "an": "2027-02-26", "desc": "Thales"}, "ELIS": {"q1": "2026-04-08", "q2": "2026-07-25", "an": "2027-02-19", "desc": "Elis"}, "EL": {"q1": "2026-05-07", "q2": "2026-07-30", "an": "2027-02-26", "desc": "EssilorLuxottica"}, "LR": {"q1": "2026-05-08", "q2": "2026-07-30", "an": "2027-02-19", "desc": "Legrand"}, "VIRB2": {"q1": "2026-04-24", "q2": "2026-07-24", "an": "2027-02-19", "desc": "Virbac"}, "THERMD": {"q1": "2026-04-15", "q2": "2026-07-15", "an": "2027-02-12", "desc": "Thermador"}, "INTPRF": {"q1": "2026-04-08", "q2": "2026-07-08", "an": "2027-02-05", "desc": "Interparfums"}, "BIOM": {"q1": "2026-05-07", "q2": "2026-07-23", "an": "2027-03-05", "desc": "BioMerieux"}};


function nextResult(ticker) {
  const e = CAL[ticker];
  if(!e) return null;
  const now = new Date();
  const dates = [e.q1,e.q2,e.q3,e.q4,e.an].filter(Boolean).map(d=>new Date(d)).filter(d=>d>=now);
  if(dates.length===0) return null;
  dates.sort((a,b)=>a-b);
  const next = dates[0];
  const diff = Math.ceil((next-now)/(1000*60*60*24));
  return {date:next.toLocaleDateString('fr-FR'), days:diff, entry:e};
}

function resultBadge(ticker) {
  const r = nextResult(ticker);
  if(!r) return '';
  const urgency = r.days<=7?'#dc2626':r.days<=30?'#d97706':'#16a34a';
  return '<span style="background:'+urgency+';color:#fff;font-size:8px;padding:2px 6px;border-radius:3px;font-family:monospace;margin-left:6px">📅 '+r.days+'j</span>';
}

// ═══════════ PEG RATIO (Peter Lynch) ═══════════
function peg(s) {
  if(!s.epsg||s.epsg<=0||!s.pe||s.pe>=999) return null;
  return (s.pe/s.epsg).toFixed(2);
}

function pegColor(s) {
  const p = parseFloat(peg(s));
  if(isNaN(p)) return 'var(--mu)';
  return p<0.5?'#7c3aed':p<1?'var(--gn)':p<2?'var(--gd)':'var(--rd)';
}

// ═══════════ QUALITY AT REASONABLE PRICE ═══════════
function qarpScore(s) {
  // Lynch: PEG < 1 + ROE > 15 + zone achat = QARP Gold
  const p = parseFloat(peg(s));
  const z = dynZone(s).inZone;
  if(isNaN(p)) return 'C';
  if(p<0.75&&s.roe>18&&z) return 'GOLD';
  if(p<1&&s.roe>12) return 'A';
  if(p<1.5&&s.roe>8) return 'B';
  return 'C';
}

// ═══════════ CONTRARIAN SIGNAL ═══════════
function contrarian(s) {
  // Grade A qui a perdu >10% = opportunité si fondamentaux inchangés
  if(s.score!=='A'&&s.score!=='B') return false;
  const z = dynZone(s);
  const nearBottom = s.price <= z.el * 1.05;
  return nearBottom && s.pio >= 7;
}

// ═══════════ HELPERS ═══════════
const gCl=g=>({A:'gA',B:'gB',C:'gC',D:'gD'}[g]||'gC');
const qGCl=g=>({A:'qA',B:'qB',C:'qC',D:'qD'}[g]||'qC');
const rCl=r=>({buy:'rb-buy',watch:'rb-watch',hold:'rb-hold',avoid:'rb-avoid'}[r]||'');
const rLb=r=>({buy:'🎯 ACHETER',watch:'👁 SURVEILLER',hold:'⏸ CONSERVER',avoid:'❌ ÉVITER'}[r]||r);
const vM={A:'Pépite — Conviction FORTE',B:'Qualité — Potentiel réel identifié',C:'Neutre — Attendre entrée',D:'Éviter — Risques non compensés'};
const cL={large:'Large Cap',mid:'Mid Cap',small:'Small Cap'};

function mc(k,v){
  const r={
    pe:v=>v>0&&v<10?'good':v<=18?'nm':v<=28?'warn':'bad',
    pb:v=>v<1.2?'good':v<3?'nm':'warn',
    ev_ebitda:v=>v>0&&v<8?'good':v<14?'nm':'warn',
    roe:v=>v>18?'good':v>9?'nm':'bad',
    roic:v=>v>13?'good':v>7?'nm':'bad',
    roa:v=>v>10?'good':v>5?'nm':'bad',
    debt:v=>v<0.5?'good':v<1.5?'nm':v<2.5?'warn':'bad',
    ic:v=>v>8?'good':v>3?'nm':'bad',
    yield:v=>v>5?'good':v>2.5?'nm':'bad',
    epsg:v=>v>10?'good':v>3?'nm':v>0?'warn':'bad',
    margin:v=>v>18?'good':v>8?'nm':v>3?'warn':'bad',
    gm:v=>v>50?'good':v>30?'nm':'bad',
    fcf:v=>v>7?'good':v>3.5?'nm':v>0?'warn':'bad',
    capr:v=>v<5?'good':v<12?'nm':'warn',
    pio:v=>v>=7?'good':v>=5?'nm':v>=3?'warn':'bad',
    alt:v=>v>3?'good':v>1.8?'warn':'bad',
  };
  return r[k]?r[k](v):'nm';
}
function rc(v){return v<35?'var(--gn)':v<55?'var(--gd)':v<70?'var(--or)':'var(--rd)';}
function up(s){return ((s.dcfm-s.price)/s.price*100).toFixed(1);}
function uc(u){return parseFloat(u)>10?'var(--gn)':parseFloat(u)>0?'var(--gd)':parseFloat(u)>-10?'var(--mu)':'var(--rd)';}
function piL(p){return p>=8?'Excellent':p>=6?'Solide':p>=4?'Moyen':'Fragile';}
function alL(a){return a>3?'Zone sûre':a>1.8?'Zone grise':'⚠️ Danger';}
function rsiL(r){return r>70?'Suracheté ⚠️':r<30?'Survendu 🟢':r>55?'Haussier':r<45?'Baissier':'Neutre';}
function piCl(p){return p>=7?'sA':p>=5?'sB':p>=3?'sC':'sD';}
function alCl(a){return a>3?'sA':a>1.8?'sC':'sD';}

// Zones calculées dynamiquement à partir du DCF et du cours actuel
function dynZone(s){
  // 04/10/2026 : zones = celles calculees par le script a partir de la valeur
  // intrinseque (el/eh/stop/o1/o2). Avant, si le cours depassait la valeur,
  // la "zone d'achat" etait recentree AUTOUR DU COURS ACTUEL : toute action
  // trop chere apparaissait "en zone d'achat".
  const el=s.el||0, eh=s.eh||0;
  return {
    el: el, eh: eh,
    stop: s.stop||0,
    o1: s.o1||s.dcfm||0,
    o2: s.o2||s.dcfu||0,
    inZone: eh>0 && s.price<=eh && s.qok!==false,  // zone d'achat = qualite d'abord
    upside: s.dcfm ? Math.round((s.dcfm/s.price-1)*100) : 0
  };
}

function rratio(s){
  const z = dynZone(s);
  const risk = s.price - z.stop;
  const gain = z.o1 - s.price;
  return risk > 0 ? Math.round(gain/risk*10)/10 : 0;
}
function trOk(d){let ok=0,tot=d.length;d.forEach(i=>{if(i.ok==='ok')ok++;else if(i.ok==='partial')ok+=0.5;});return Math.round(ok/tot*100);}
function trCl(pct){return pct>=75?'sA':pct>=50?'sB':'sD';}

// STATE
let fil=[...S],idx=0,paused=false,tmr=null,spd=18,cycles=0,srtC=null,srtD=1;

// ═══════════ RENDER ═══════════
function show(i){
  if(!fil.length)return;
  const s=fil[i];
  document.getElementById('lt').textContent=s.ticker;
  document.getElementById('lc').style.display='flex';
  document.getElementById('fiche').style.display='none';
  setTimeout(()=>render(s),650);
}

function render(s){
  const chgS=s.chg>=0?`+${s.chg}%`:`${s.chg}%`;
  const chgCl=s.chg>0?'pos':s.chg<0?'neg':'neu';
  const u=up(s);const uCol=uc(u);
  const ub=((s.dcfb-s.price)/s.price*100).toFixed(1);
  const ubs=((s.dcfu-s.price)/s.price*100).toFixed(1);
  const m50d=((s.price-s.mm50)/s.mm50*100).toFixed(1);
  const m200d=((s.price-s.mm200)/s.mm200*100).toFixed(1);
  const tot=s.cb+s.ch+s.cs;
  const rr=rratio(s);
  const tpct=trOk(s.track);
  const capR=s.capda<0.8?'<span style="color:var(--gn)">Maintenance</span>':s.capda<1.2?'<span style="color:var(--gd)">Mixte</span>':'<span style="color:var(--or)">Expansion</span>';
  const now=new Date();
  const ts=now.toLocaleDateString('fr-FR')+' '+now.toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit'});
  const inZ=dynZone(s).inZone;

  const tags=[
    `<span class="tag t-sec">${s.sector}</span>`,
    `<span class="tag t-cap">${cL[s.cap]||s.cap} · ${s.idx}</span>`,
    `<span class="tag t-pea">✓ PEA</span>`,
    s.srd?'<span class="tag t-srd">SRD</span>':'',
    inZ?'<span class="tag t-zone">📍 Zone achat</span>':''
  ].join('');

  const fundMets=[
    {k:'pe',l:'P/E',v:s.pe,u:'x',d:'Valorisation bénéfices'},{k:'pb',l:'P/B',v:s.pb,u:'x',d:'vs Actif net comptable'},
    {k:'ev_ebitda',l:'EV/EBITDA',v:s.ev_ebitda,u:'x',d:'Valeur entreprise'},{k:'ps',l:'P/S',v:s.ps,u:'x',d:'Prix/Ventes'},
    {k:'ev_ebit',l:'EV/EBIT',v:s.ev_ebit,u:'x',d:'Valeur/Résultat opér.'},{k:'roe',l:'ROE',v:s.roe,u:'%',d:'Rentabilité fonds propres'},
    {k:'roic',l:'ROIC',v:s.roic,u:'%',d:'Retour capital investi'},{k:'roa',l:'ROA',v:s.roa,u:'%',d:'Retour sur actifs'},
    {k:'margin',l:'Marge Nette',v:s.margin,u:'%',d:'Rentabilité finale'},{k:'gm',l:'Marge Brute',v:s.gm,u:'%',d:'Pricing power'},
  ];
  const balMets=[
    {k:'nde',l:'Dette nette/EBITDA',v:(s.nde==null?'—':s.nde),u:'x',d:'Levier (filtre ≤ 2,5)'},{k:'de',l:'Dett/CP',v:s.de,u:'x',d:'Gearing'},
    {k:'ic',l:'Int. Coverage',v:(s.ic==null?'—':s.ic),u:' x',d:'Couverture intérêts'},{k:'cr',l:'Current Ratio',v:s.cr||'—',u:'x',d:'Liquidité court terme'},
    {k:'fcf',l:'FCF Yield',v:s.fcf,u:'%',d:'Flux de trésorerie libre'},{k:'capr',l:'CAPEX/CA',v:s.capr,u:'%',d:'Intensité capitalistique'},
    {k:'capda',l:'CAPEX/DA',v:s.capda,u:'x',d:'Investissement vs maintenance'},{k:'yield',l:'Dividende',v:s.yield,u:'%',d:'Rendement courant'},
    {k:'epsg',l:'Croiss. BPA',v:s.epsg,u:'%',d:'Prévision N+1'},{k:'revg',l:'Croiss. CA',v:s.revg,u:'%',d:'Prévision N+1'},
  ];

  const html=`
<div class="ftop">
  <div class="ftkr">${s.ticker}</div>
  <div class="fmid"><div class="fnm">${s.name}</div><div class="ftags">${tags}</div></div>
  <div class="frt">
    <div class="fpr" id="fp-${s.ticker}">${s.price.toFixed(2)} €</div>
    <div class="flive" id="fl-${s.ticker}">● Données indicatives</div>
    <div class="fch ${chgCl}">${chgS} aujourd'hui</div>
    <div class="fmk">Cap. ${s.mkt} · 52S ${s.b52l}-${s.b52h}€ · β${s.beta}</div>
  </div>
</div>

${s.qok===undefined?'':`<div style="margin:8px 0;padding:8px 12px;border-radius:6px;font-size:12px;line-height:1.5;background:${s.qok?'var(--gnb)':'var(--rdb)'}"><b>Filtre qualité QARP : ${s.qok?'✅ OUI':(s.near?'⚑ LIMITE — à surveiller (un seul critère manqué)':'❌ NON')}</b>${s.place?` · 📍 ${s.place}${['Helsinki','Copenhague','Stockholm','Oslo'].includes(s.place)?' (accès PEA chez ton courtier à vérifier)':''}`:''}${s.mscore!=null?` · 🏰 <b>Moat ${s.mscore}/5</b> : ${s.mtype} — <i>menace : ${s.mthreat}</i>${s.mscore<3?' (moat insuffisant : pas d’achat)':''}`:''} · ROIC hors EA ${s.roicx>100?'>100':(s.roicx??'—')} % · ROIC ${s.roic>100?'>100':(s.roic??'—')} % · Cash ${s.fcfc??'—'} % · Dette/EBITDA ${s.nde??'—'} · Croissance CA ${s.cagr??'—'} %/an${s.qwhy?` — <i>${s.qwhy}</i>`:''}${s.neglect?' · 🔎 <b>qualité délaissée</b>':''}${s.alarm?` · ⚠️ ${s.alarm}`:''}${s.knife&&s.b52h?` · ⛔ <b>cours ${Math.round((1-s.price/s.b52h)*100)} % sous son plus haut 1 an : comprendre la cause avant tout achat</b>`:''}${s.gimp!=null?`<br>📐 <b>Le cours actuel suppose ~${s.gimp} %/an de croissance</b> (ralentissant vers 2,5 % sur 10 ans) · croissance réelle retenue : ${s.gused??'—'} %/an (${s.gsrc||'—'}) → ${s.gused!=null&&s.gimp<=s.gused?'✅ hypothèse du marché ≤ réel : marge de sécurité':'⚠️ le marché suppose plus que le réel'}`:''}</div>`}
<div class="verdict">
  <div class="vgrd ${gCl(s.score)}">${s.score}</div>
  <div class="vtxt">
    <div class="vhl">${vM[s.score]}</div>
    <div class="vsb">Piotroski ${s.pio}/9 · DCF Base ${s.dcfm}€ (${u>0?'+':''}${u}%) · ${s.cb}/${tot} analystes Buy · Obj. ${s.tp}€ · R/R ${rr}x · Fiabilité dir. ${tpct}%</div>
  </div>
  <div class="vrec"><div class="rb ${rCl(s.rec)}">${rLb(s.rec)}</div></div>
</div>


<!-- ONGLET PRÉSENTATION - Format newsletter -->
<div class="pres-section">
  <div class="pres-header">
    <div class="pres-tabs">
      <button class="ptab active" onclick="showPres(this,'analyse')">📊 Analyse</button>
      <button class="ptab" onclick="showPres(this,'presentation')">📰 Présentation</button>
      <button class="ptab" onclick="showPres(this,'calendrier')">📅 Calendrier</button>
    </div>
  </div>

  <!-- TAB: ANALYSE (contenu deep-analysis déplacé ici) -->
  <div id="pres-analyse" class="ptab-content active">
    <div class="deep-analysis-inner">
      <!-- 3 VRAIES QUESTIONS -->
      <div class="da-header">💡 Analyse du Cabinet — Pourquoi investir ?</div>
      <div class="da-3q">
        <div class="da-q">
          <div class="da-qi">🏰</div>
          <div class="da-ql">Ce que personne ne peut faire</div>
          <div class="da-qv">${s.moat.length>0?s.moat[0][0]:'Voir analyse complète'}</div>
        </div>
        <div class="da-q">
          <div class="da-qi">📅</div>
          <div class="da-ql">Pourquoi maintenant</div>
          <div class="da-qv">${s.cats.length>0?s.cats[0].t+' · '+s.cats[0].w:'Voir catalyseurs'}</div>
        </div>
        <div class="da-q">
          <div class="da-qi">👨‍💼</div>
          <div class="da-ql">Track record direction</div>
          <div class="da-qv">${trOk(s.track)}% guidances tenues · ${trOk(s.track)>=75?'Crédible':'À surveiller'}</div>
        </div>
      </div>
      <div class="da-thesis">
        <div class="da-bull"><div class="da-lbl" style="color:var(--gn)">🐂 Pourquoi acheter</div><div class="da-txt">${s.thesis}</div></div>
        <div class="da-bear"><div class="da-lbl" style="color:var(--rd)">🐻 Ce que le marché craint</div><div class="da-txt">${s.contra}</div></div>
      </div>
      <div class="da-verdict">
        <div style="display:flex;gap:8px;align-items:center;margin-bottom:8px">
          <div class="da-kpi"><div class="da-kv" style="color:${s.roe>18?'var(--gn)':s.roe>9?'var(--gd)':'var(--rd)'}">${s.roe}%</div><div class="da-kl">ROE</div></div>
          <div class="da-kpi"><div class="da-kv" style="color:${parseFloat(up(s))>20?'var(--gn)':parseFloat(up(s))>5?'var(--gd)':'var(--rd)'}">+${up(s)}%</div><div class="da-kl">Potentiel</div></div>
          <div class="da-kpi"><div class="da-kv" style="color:${s.pio>=7?'var(--gn)':s.pio>=5?'var(--gd)':'var(--rd)'}">${s.pio}/9</div><div class="da-kl">Piotroski</div></div>
          <div class="da-kpi"><div class="da-kv" style="color:${rratio(s)>=2?'var(--gn)':rratio(s)>=1?'var(--gd)':'var(--rd)'}">${rratio(s)}x</div><div class="da-kl">R/R</div></div>
          <div class="da-kpi"><div class="da-kv" style="color:${s.yield>=5?'var(--gn)':s.yield>=2?'var(--gd)':'var(--mu)'}">${s.yield}%</div><div class="da-kl">Div.</div></div>
          <div class="da-kpi"><div class="da-kv" style="color:${pegColor(s)}">${peg(s)||'N/A'}</div><div class="da-kl">PEG Lynch</div></div>
        </div>
        <div class="da-pos">${
          s.score==='A'?'CONVICTION FORTE · <b>Allouer 5-8%</b> du portefeuille PEA. Entrer en zone achat en fractionnant.':
          s.score==='B'?'QUALITÉ · <b>Allouer 3-5%</b> maximum. Attendre la zone achat.':
          s.score==='C'?'NEUTRE · Maximum <b>2%</b> si conviction personnelle.':
          'ÉVITER · Risques dominants. Maximum <b>0.5%</b> spéculatif averti.'
        }</div>
        ${contrarian(s)?'<div style="margin-top:8px;padding:8px;background:rgba(124,58,237,.1);border:1px solid rgba(124,58,237,.3);border-radius:4px;font-size:11px;color:#7c3aed"><b>🎯 SIGNAL CONTRARIAN</b> — Cette action de qualité est proche de son support. Opportunité d accumuler.</div>':''}
      </div>
    </div>
  </div>

  <!-- TAB: PRÉSENTATION - Format newsletter Bloomberg -->
  <div id="pres-presentation" class="ptab-content" style="display:none">
    <div class="pres-card">
      <div class="pres-card-header">
        <div class="pres-logo">${s.name.substring(0,2).toUpperCase()}</div>
        <div class="pres-card-meta">
          <div class="pres-card-name">${s.name}</div>
          <div class="pres-card-sector">${s.sector} · ${s.idx} · Cap. ${s.mkt}</div>
        </div>
        <div class="pres-card-grade grade-${s.score}">${s.score==='A'?'⭐ PÉPITE':s.score==='B'?'💎 QUALITÉ':s.score==='C'?'⏳ NEUTRE':'⚠️ ÉVITER'}</div>
      </div>
      
      <div class="pres-story">
        <div class="pres-story-label">📖 L'histoire de cette entreprise</div>
        <div class="pres-story-text">${s.thesis}</div>
      </div>

      <div class="pres-moat-visual">
        <div class="pres-story-label">🏰 Son avantage concurrentiel — ce que personne ne peut copier</div>
        <div class="pres-moat-items">${s.moat.map(m=>'<div class="pmi"><span class="pmi-star">★</span>'+m[0]+'<span class="pmi-tag pmi-'+m[1]+'">'+m[1]+'</span></div>').join('')}</div>
      </div>

      <div class="pres-catalysts">
        <div class="pres-story-label">⚡ Pourquoi maintenant — Les catalyseurs</div>
        ${s.cats.map(cat=>'<div class="pcat"><span class="pcat-dot" style="background:'+cat.c+'"></span><b>'+cat.t+'</b> <span class="pcat-date">'+cat.w+'</span></div>').join('')}
      </div>

      <div class="pres-triple">
        <div class="pres-triple-item pres-triple-bull">
          <div class="ptri-label">🐂 LE CAS HAUSSIER</div>
          <div class="ptri-text">${s.thesis}</div>
        </div>
        <div class="pres-triple-item pres-triple-bear">
          <div class="ptri-label">🐻 LE CAS BAISSIER</div>
          <div class="ptri-text">${s.contra}</div>
        </div>
        <div class="pres-triple-item pres-triple-verdict">
          <div class="ptri-label">🏆 LE VERDICT</div>
          <div style="font-size:18px;font-weight:700;color:${s.score==='A'?'#22c55e':s.score==='B'?'#d97706':s.score==='C'?'#6b7280':'#ef4444'};margin-bottom:6px">${s.score==='A'?'ACHETER':'B'===s.score?'SURVEILLER':'C'===s.score?'ATTENDRE':'ÉVITER'}</div>
          <div style="font-size:11px;color:var(--tx)">Position: ${s.score==='A'?'5-8%':s.score==='B'?'3-5%':'max 2%'} · Zone: ${dynZone(s).el}–${dynZone(s).eh}€</div>
          <div style="margin-top:8px">
            <div style="font-size:9px;color:var(--mu);margin-bottom:3px">CONVICTION DU CABINET</div>
            <div style="display:flex;gap:2px">${[1,2,3,4,5].map(i=>'<div style="width:20%;height:6px;border-radius:2px;background:'+(i<={'A':5,'B':4,'C':2,'D':1}[s.score]?'#b8860b':'#e5e7eb')+'"></div>').join('')}</div>
          </div>
        </div>
      </div>

      <div class="pres-insiders">
        <div class="pres-story-label">👁️ Ce qu'achète la direction</div>
        ${s.ins.length>0?s.ins.map(i=>'<div class="pins"><span class="pins-arrow">↗</span><b>'+i[1]+'</b> a acheté <b style="color:var(--gn)">'+i[2]+'</b> · '+i[3]+'</div>').join(''):'<div style="color:var(--mu);font-size:11px;font-style:italic">Pas d achat direction récent recensé</div>'}
      </div>
    </div>
  </div>

  <!-- TAB: CALENDRIER -->
  <div id="pres-calendrier" class="ptab-content" style="display:none">
    <div class="cal-widget">
      ${resultBadge(s.ticker)?'<div class="cal-next"><div class="cal-next-label">⏰ Prochains résultats</div>'+buildCalWidget(s.ticker)+'</div>':'<div style="color:var(--mu);font-size:12px;padding:12px;font-style:italic">Dates de résultats non encore connues pour '+s.name+'.<br>Consulter AMF.fr ou le site investor relations de la société.</div>'}
      <div class="cal-advice">
        <div class="cal-advice-title">📅 Méthode Triptyque — Score & 3 Piliers</div>
        <div>${buildTriptyqueFullSection(s)}</div>
      </div>
    </div>
  </div>
</div>


<div id="tv-chart"></div>
<div id="mm200-banner"></div>
<div class="sec">
  <div class="sct">Points d'Entrée & Sortie — Signal Technique</div>
  <div class="ep">
    <div class="ep-g">
      <div class="epb ep-e">
        <div class="epv">${dynZone(s).el}–${dynZone(s).eh}€</div>
        <div class="eplb">Zone achat</div>
        <div class="eps">${inZ?'✅ Vous êtes dedans':'Attendre ce niveau'}</div>
      </div>
      <div class="epb ep-s">
        <div class="epv">${dynZone(s).stop}€</div>
        <div class="eplb">Stop Loss</div>
        <div class="eps">Risque : ${((s.price-s.stop)/s.price*100).toFixed(1)}% du capital</div>
      </div>
      <div class="epb ep-o">
        <div class="epv">${s.o1}€</div>
        <div class="eplb">Objectif 1</div>
        <div class="eps">Potentiel : +${((s.o1-s.price)/s.price*100).toFixed(1)}%</div>
      </div>
      <div class="epb ep-r">
        <div class="epv">${rr}x</div>
        <div class="eplb">Ratio R/R</div>
        <div class="eps">${rr>=2?'✅ Favorable':rr>=1?'⚠️ Correct':'❌ Insuffisant'}</div>
      </div>
    </div>
    <div class="sig-row">
      <span class="sig-lbl">Signal global</span>
      <div class="sig-trk"><div class="sig-nd" style="left:${Math.min(95,Math.max(5,
        (s.score==='A'&&inZ?80:s.score==='A'?65:s.score==='B'&&inZ?70:s.score==='B'?55:s.score==='C'?35:20)
      ))+'%'}"></div></div>
      <span class="sig-val" style="color:${s.score==='A'?'var(--gn)':s.score==='B'?'var(--gd)':s.score==='C'?'var(--or)':'var(--rd)'}">${s.score==='A'&&inZ?'FORT 🟢':s.score==='A'?'BON':s.score==='B'&&inZ?'BON 🟢':s.score==='B'?'MOYEN':'FAIBLE'}</span>
    </div>
    <div class="sig-row" style="margin-top:4px">
      <span class="sig-lbl">RSI ${s.rsi}</span>
      <div class="sig-trk"><div class="sig-nd" style="left:${Math.min(95,Math.max(5,s.rsi))+'%'}"></div></div>
      <span class="sig-val" style="color:${s.rsi>70?'var(--rd)':s.rsi<30?'var(--gn)':'var(--mu)'}">${rsiL(s.rsi)}</span>
    </div>
  </div>
</div>

<div class="sec">
  <div class="sct">Valorisation & Rentabilité — 10 Indicateurs Fondamentaux</div>
  <div class="mg5">${fundMets.map(m=>`<div class="mb ${mc(m.k,m.v)}"><div class="ml">${m.l}</div><div class="mv">${m.v==null?'—':m.v+m.u}</div><div class="ms">${m.d}</div></div>`).join('')}</div>
</div>

<div class="sec">
  <div class="sct">Bilan, Cash Flow & CAPEX — Solidité Financière</div>
  <div class="mg5">${balMets.map(m=>`<div class="mb ${mc(m.k,typeof m.v==='number'?m.v:0)}"><div class="ml">${m.l}</div><div class="mv">${m.v==null?'—':m.v}${typeof m.v==='number'?m.u:''}</div><div class="ms">${m.d}</div></div>`).join('')}</div>
  <div style="margin-top:6px;font-size:9px;color:var(--mu);font-style:italic">CAPEX/Amortissements : ${capR} — CAPEX ${s.capex}Md€ · Intensité capitalistique : ${s.capr<5?'<span style="color:var(--gn)">Légère</span>':s.capr<12?'<span style="color:var(--gd)">Moderee</span>':'<span style="color:var(--or)">Lourde</span>'}</div>
</div>

<div class="sec">
  <div class="sct">Scores de Solidité & Momentum Technique</div>
  <div class="tc">
    <div>
      <div class="sr">
        <div class="sb"><div class="sbv ${piCl(s.pio)}">${s.pio}/9</div><div class="sbl">Piotroski F</div><div class="sbd">${piL(s.pio)}</div></div>
        <div class="sb"><div class="sbv ${alCl(s.alt)}">${s.alt}</div><div class="sbl">Altman Z</div><div class="sbd">${alL(s.alt)}</div></div>
        <div class="sb"><div class="sbv sN">${s.rsi}</div><div class="sbl">RSI 14j</div><div class="sbd">${rsiL(s.rsi)}</div></div>
        <div class="sb"><div class="sbv" style="color:${uCol}">${parseFloat(u)>0?'+':''}${u}%</div><div class="sbl">Upside DCF</div><div class="sbd">Base case</div></div>
      </div>
      <div class="mm-row">
        <div class="mmb"><div class="mmv" style="color:${parseFloat(m50d)>=0?'var(--gn)':'var(--rd)'}">${parseFloat(m50d)>=0?'+':''}${m50d}%</div><div class="mml">vs MM50 (${s.mm50}€)</div></div>
        <div class="mmb"><div class="mmv" style="color:${parseFloat(m200d)>=0?'var(--gn)':'var(--rd)'}">${parseFloat(m200d)>=0?'+':''}${m200d}%</div><div class="mml">vs MM200 (${s.mm200}€)</div></div>
      </div>
    </div>
    <div>
      <div class="dcfg">
        <div class="dcfb" style="border-top:2px solid var(--rd)"><div class="dcfs">Bear Case</div><div class="dcfv">${s.dcfb}€</div><div class="dcfu" style="color:${uc(ub)}">${parseFloat(ub)>0?'+':''}${ub}%</div></div>
        <div class="dcfb" style="border-top:2px solid var(--gd);background:var(--gdm)"><div class="dcfs">Base Case</div><div class="dcfv" style="font-weight:700">${s.dcfm}€</div><div class="dcfu" style="color:${uCol};font-weight:600">${parseFloat(u)>0?'+':''}${u}%</div></div>
        <div class="dcfb" style="border-top:2px solid var(--gn)"><div class="dcfs">Bull Case</div><div class="dcfv">${s.dcfu}€</div><div class="dcfu" style="color:var(--gn)">+${ubs}%</div></div>
      </div>
      <div style="margin-top:5px;font-size:8px;color:var(--mu2);font-style:italic">${s.vmeth==='qarp'?'Valeur qualité : 10 ans de croissance (≤ 12 %/an) puis 2,5 %, actualisation 8,5 % · pessimiste −15 % / optimiste +20 %':'Valeur simplifiée : PER sectoriel × bénéfice attendu (valeur hors filtre qualité) · pessimiste −15 % / optimiste +20 %'}</div>
    </div>
  </div>
</div>
  <div class="sec">
    <div class="sct">Grille Moat Notée (12 critères, façon "SCORE FONDA")</div>
    <div id="moatgrid-${s.ticker}">${renderMoatGrid(s)}</div>
  </div>

<div class="sec">
  <div class="sct">Avantages Compétitifs (Moat) & Consensus Analystes</div>
  <div class="tc">
    <div>${s.moat.map(([l,str])=>`<div class="mi"><span style="font-size:12px">${str==='fort'?'🏰':str==='mod'?'🔷':'⚠️'}</span><span style="flex:1">${l}</span><span class="mip ${str==='fort'?'mf':str==='mod'?'mm2':'mw'}">${str==='fort'?'Fort':'Modere'}</span></div>`).join('')}</div>
    <div>
      <div class="ctop">
        <div class="cons-n2"><div class="cnv" style="color:var(--gn)">${s.cb}</div><div class="cnl">Achat</div></div>
        <div class="cons-n2"><div class="cnv" style="color:var(--gd)">${s.ch}</div><div class="cnl">Neutre</div></div>
        <div class="cons-n2"><div class="cnv" style="color:var(--rd)">${s.cs}</div><div class="cnl">Vente</div></div>
        <div class="cons-n2" style="border-left:1px solid var(--bd);padding-left:10px"><div class="cnv" style="color:var(--nv)">${s.tp}€</div><div class="cnl">Objectif</div></div>
      </div>
      <div class="abar"><span class="al">Achat</span><div class="at"><div class="af" style="width:${(s.cb/tot*100).toFixed(0)}%;background:var(--gn)"></div></div><span class="ac">${s.cb}</span></div>
      <div class="abar"><span class="al">Neutre</span><div class="at"><div class="af" style="width:${(s.ch/tot*100).toFixed(0)}%;background:var(--gd)"></div></div><span class="ac">${s.ch}</span></div>
      <div class="abar"><span class="al">Vente</span><div class="at"><div class="af" style="width:${(s.cs/tot*100).toFixed(0)}%;background:var(--rd)"></div></div><span class="ac">${s.cs}</span></div>
    </div>
  </div>
</div>

<div class="sec">
  <div class="sct">Comparaison Sectorielle — Peer Group</div>
  <table class="pt">
    <thead><tr><th>Société</th><th>P/E</th><th>P/B</th><th>ROE%</th><th>Div%</th><th>EV/EBITDA</th></tr></thead>
    <tbody>
      <tr class="cur"><td>★ ${s.ticker} — ${s.name}</td><td>${s.pe}x</td><td>${s.pb}x</td><td>${s.roe}%</td><td>${s.yield}%</td><td>${s.ev_ebitda}x</td></tr>
      ${s.peers.map(p=>{const live=S.find(x=>x.name===p.n);const pv=live?{pe:live.pe,pb:live.pb,roe:live.roe,div:live.yield,evebitda:live.ev_ebitda}:p;return `<tr><td>${p.n}${live?' <span style="color:var(--gn);font-size:8px">●</span>':''}</td><td>${pv.pe||'—'}x</td><td>${pv.pb||'—'}x</td><td>${pv.roe||'—'}%</td><td>${pv.div||'—'}%</td><td>${pv.evebitda||'—'}x</td></tr>`;}).join('')}
    </tbody>
  </table>
</div>

<div class="sec">
  <div class="sct">Track Record Direction — Promesses vs Réalisé</div>
  <div class="tc">
    <div>
      ${s.track.map(t=>`<div class="tr-i"><span class="try">${t.y}</span><span class="trp">${t.p}</span><span class="trr" style="color:${t.ok==='ok'?'var(--gn)':t.ok==='partial'?'var(--gd)':'var(--rd)'}">${t.r}</span><span class="trb ${t.ok==='ok'?'tr-ok':t.ok==='partial'?'tr-p':'tr-m'}">${t.ok==='ok'?'Tenu':t.ok==='partial'?'Partiel':'Raté'}</span></div>`).join('')}
    </div>
    <div class="trs">
      <div class="trs-v ${trCl(tpct)}" style="color:${tpct>=75?'var(--gn)':tpct>=50?'var(--gd)':'var(--rd)'}">${tpct}%</div>
      <div class="trs-l">Fiabilité Direction</div>
      <div style="font-size:9px;color:var(--mu);margin-top:5px">${tpct>=75?'Management crédible — Acheter au discours':'Management à vérifier — Pondérer les guidances'}</div>
    </div>
  </div>
</div>

<div class="sec">
  <div class="sct">Catalyseurs & Transactions Dirigeants</div>
  <div class="tc">
    <div>${s.cats.map(c=>`<div class="cat-i"><div class="cat-dot" style="background:${c.c}"></div><span class="cat-w">${c.w}</span><span>${c.t}</span></div>`).join('')}</div>
    <div>${s.ins.map(([tp,wh,am,dt])=>`<div class="ii"><span class="it ${tp==='Achat'?'ita':'itv'}">${tp}</span><span class="iw">${wh}</span><span style="font-family:'IBM Plex Mono',monospace;font-size:9px;color:var(--mu)">${am}</span><span style="font-size:8px;color:var(--mu2);margin-left:4px">${dt}</span></div>`).join('')}</div>
  </div>
</div>

<div class="sec">
  <div class="sct">Matrice des Risques — 6 Dimensions</div>
  ${Object.entries(s.risks).map(([k,v])=>`<div class="rrow"><span class="rl">${k}</span><div class="rbar"><div class="rf" style="width:${v}%;background:${rc(v)}"></div></div><span class="rn" style="color:${rc(v)}">${v}/100</span></div>`).join('')}
</div>

<div class="ffoot">
  <span class="fn">⚠️ Données éducatives uniquement · Pas de conseil en investissement · Consulter un CIF agréé AMF</span>
  <span class="fn">PEA Screener Pro · ${ts}</span>
</div>`;

  const fe=document.getElementById('fiche');
  fe.innerHTML=html;
  document.getElementById('lc').style.display='none';
  fe.style.display='block';
  updHK();
  // TradingView chart
  setTimeout(function(){loadTV(s);loadMM200Banner(s);},100);
}

function loadTV(s){
  const wrap=document.getElementById('tv-chart');
  if(!wrap)return;
  const tvMap={'MC':'EURONEXT:MC','AI':'EURONEXT:AI','OR':'EURONEXT:OR','RMS':'EURONEXT:RMS','SAN':'EURONEXT:SAN','TTE':'EURONEXT:TTE','SAF':'EURONEXT:SAF','SU':'EURONEXT:SU','AXA':'EURONEXT:CS','BNP':'EURONEXT:BNP','ACA':'EURONEXT:ACA','GLE':'EURONEXT:GLE','AIR':'EURONEXT:AIR','KER':'EURONEXT:KER','PUB':'EURONEXT:PUB','ORA':'EURONEXT:ORA','VIE':'EURONEXT:VIE','RNO':'EURONEXT:RNO','SGO':'EURONEXT:SGO','CAP':'EURONEXT:CAP','DG':'EURONEXT:DG','VIV':'EURONEXT:VIV','RI':'EURONEXT:RI','LR':'EURONEXT:LR','WLN':'EURONEXT:WLN','DSY':'EURONEXT:DSY','STM':'NYSE:STM','EL':'EURONEXT:EL','ML':'EURONEXT:ML','ENGI':'EURONEXT:ENGI','MT':'EURONEXT:MT','URW':'EURONEXT:URW','SW':'EURONEXT:SW','TEP':'EURONEXT:TEP','EN':'EURONEXT:EN','GTT':'EURONEXT:GTT','COFA':'EURONEXT:COFA','MERY':'EURONEXT:MRY','JXS':'EURONEXT:JXS','SPIE':'EURONEXT:SPIE','NEXANS':'EURONEXT:NEX','DASSAV':'EURONEXT:AM','ALO':'EURONEXT:ALO','ELIS':'EURONEXT:ELIS','SEB':'EURONEXT:SK','ERF':'EURONEXT:ERF','IPSOS':'EURONEXT:IPS','ABCA':'EURONEXT:ABCA','VK':'EURONEXT:VK','FNAC':'EURONEXT:FNAC','LNA':'EURONEXT:LNA','CNP':'EURONEXT:CNP','SOP':'EURONEXT:SOP','AC':'EURONEXT:AC','AF':'EURONEXT:AF','BN':'EURONEXT:BN','CA':'EURONEXT:CA','HO':'EURONEXT:HO','ATO':'EURONEXT:ATO','DBG':'EURONEXT:DBG','ASML':'NASDAQ:ASML','PRX':'EURONEXT:PRX','ADYEN':'EURONEXT:ADYEN','HEIA':'EURONEXT:HEIA','NOVO':'CPH:NOVOB','SAP':'XETRA:SAP','SIEMENS':'XETRA:SIE','ALV':'XETRA:ALV','LVMHF':'MIL:RACE',
  'BIOM':'EURONEXT:BIM','KLPI':'EURONEXT:LI','RCO':'EURONEXT:RCO','EIFFAGE':'EURONEXT:FGR','ALTAREA':'EURONEXT:ALTA','COVIVIO':'EURONEXT:COV','FREY':'EURONEXT:FREY','GALIMMO':'EURONEXT:GALIM','MERCIALYS':'EURONEXT:MERY2','ALFPC':'EURONEXT:ALFPC','TRIGANO':'EURONEXT:TRI','BOIRON':'EURONEXT:BOI','CHSR':'EURONEXT:CAS','VALO':'EURONEXT:FR','FORVIA':'EURONEXT:FRVIA','PLASTIC':'EURONEXT:POM','SFCA':'EURONEXT:WLN2','COGEFI':'EURONEXT:COFA','SIPH':'EURONEXT:SIPH','PLUXEE':'EURONEXT:PLX','EDENRED':'EURONEXT:EDEN','OPM':'EURONEXT:VRLA','DERICHEBOURG':'EURONEXT:DBG','ORPEA':'EURONEXT:ORP','BIOM2':'EURONEXT:BIM'};
  const sym=tvMap[s.ticker]||('EURONEXT:'+s.ticker);
  const tvUrl='https://fr.tradingview.com/chart/?symbol='+encodeURIComponent(sym)+'&interval=W&theme=dark';
  const bsUrl='https://www.boursorama.com/cours/1rP'+s.ticker+'/';
  const zbUrl='https://www.zonebourse.com/recherche/?q='+encodeURIComponent(s.name.split(' ')[0]);
  const m50d=((s.price-s.mm50)/s.mm50*100).toFixed(1);
  const m200d=((s.price-s.mm200)/s.mm200*100).toFixed(1);
  const trend=s.price>s.mm200&&s.mm50>s.mm200?'Haussière 📈':s.price<s.mm200&&s.mm50<s.mm200?'Baissière 📉':'Neutre ➡️';
  const trendCol=s.price>s.mm200?'#1a6b3a':'#c0392b';
  wrap.innerHTML='<div style="background:linear-gradient(135deg,#0f2540,#1a3a5c);padding:16px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap">'+
    '<div style="display:flex;gap:20px;align-items:center">'+
    '<div style="text-align:center"><div style="font-family:IBM Plex Mono,monospace;font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:1px">MM50</div><div style="font-family:IBM Plex Mono,monospace;font-size:14px;font-weight:600;color:'+(parseFloat(m50d)>=0?'#5ddb8a':'#ff7070')+'">'+s.mm50+'€</div><div style="font-size:9px;color:'+(parseFloat(m50d)>=0?'#5ddb8a':'#ff7070')+'">'+(parseFloat(m50d)>=0?'+':'')+m50d+'%</div></div>'+
    '<div style="text-align:center"><div style="font-family:IBM Plex Mono,monospace;font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:1px">MM200</div><div style="font-family:IBM Plex Mono,monospace;font-size:14px;font-weight:600;color:'+(parseFloat(m200d)>=0?'#5ddb8a':'#ff7070')+'">'+s.mm200+'€</div><div style="font-size:9px;color:'+(parseFloat(m200d)>=0?'#5ddb8a':'#ff7070')+'">'+(parseFloat(m200d)>=0?'+':'')+m200d+'%</div></div>'+
    '<div style="text-align:center"><div style="font-family:IBM Plex Mono,monospace;font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:1px">RSI 14j</div><div style="font-family:IBM Plex Mono,monospace;font-size:14px;font-weight:600;color:'+(s.rsi>70?'#ff7070':s.rsi<30?'#5ddb8a':'#f0d080')+'">'+s.rsi+'</div><div style="font-size:9px;color:rgba(255,255,255,.5)">'+(s.rsi>70?'Suracheté':s.rsi<30?'Survendu':'Neutre')+'</div></div>'+
    '<div style="border-left:1px solid rgba(255,255,255,.1);padding-left:20px"><div style="font-family:IBM Plex Mono,monospace;font-size:8px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:1px">Tendance</div><div style="font-size:13px;font-weight:600;color:'+trendCol+'">'+trend+'</div><div style="font-size:9px;color:rgba(255,255,255,.4)">Dow Theory</div></div>'+
    '</div>'+
    '<div style="display:flex;gap:8px">'+
    '<a href="'+tvUrl+'" target="_blank" style="padding:8px 12px;background:#b8860b;color:#fff;font-family:IBM Plex Mono,monospace;font-size:9px;text-decoration:none;border-radius:3px;font-weight:700;text-transform:uppercase;letter-spacing:1px;white-space:nowrap">📈 TradingView →</a>'+
    '<button onclick="goPresentation(\''+s.ticker+'\');" style="padding:8px 10px;background:rgba(184,134,11,.2);color:#f0d080;border:1px solid rgba(184,134,11,.3);border-radius:3px;cursor:pointer;font-family:IBM Plex Mono,monospace;font-size:9px;font-weight:700">📋 Présentation</button>'+
    '<a href="'+bsUrl+'" target="_blank" style="padding:8px 10px;background:rgba(255,255,255,.08);color:rgba(255,255,255,.7);font-family:IBM Plex Mono,monospace;font-size:9px;text-decoration:none;border-radius:3px;border:1px solid rgba(255,255,255,.15);white-space:nowrap">📊 Boursorama</a>'+
    '<a href="'+zbUrl+'" target="_blank" style="padding:8px 10px;background:rgba(255,255,255,.08);color:rgba(255,255,255,.7);font-family:IBM Plex Mono,monospace;font-size:9px;text-decoration:none;border-radius:3px;border:1px solid rgba(255,255,255,.15);white-space:nowrap">🔍 Zone Bourse</a>'+
    '</div></div>';
}

function loadMM200Banner(s){
  const b=document.getElementById('mm200-banner');
  if(!b)return;
  const aboveMM200=s.price>s.mm200;
  const pct=((s.price-s.mm200)/s.mm200*100).toFixed(1);
  const m50Above=s.mm50>s.mm200;
  // Dow Theory signal
  const dow=aboveMM200&&m50Above?'bull':!aboveMM200&&!m50Above?'bear':'neut';
  const dowLbl={'bull':'📈 Tendance HAUSSIÈRE','bear':'📉 Tendance BAISSIÈRE','neut':'➡️ Tendance NEUTRE'};
  const dowTxt={'bull':'Cours & MM50 au-dessus de la MM200 — Dow Theory confirme la hausse','bear':'Cours & MM50 sous la MM200 — Signal de prudence, risque de poursuite baissière','neut':'Signal mixte — Attendre une clarification de tendance'};
  b.className=aboveMM200?'mm200-ok':'mm200-warn';
  b.innerHTML='<span style="font-size:14px">'+(aboveMM200?'🟢':'🔴')+'</span>'+
    '<span><b>MM200 : '+s.mm200+'€</b> — Cours '+(aboveMM200?'dessus (+':'dessous (')+Math.abs(pct)+'%) · </span>'+
    '<span class="dow-signal dow-'+dow+'">'+dowLbl[dow]+'</span>'+
    '<span style="margin-left:8px;opacity:.8">'+dowTxt[dow]+'</span>';
}

// ═══════════ QUEUE ═══════════
function buildQ(){
  const l=document.getElementById('ql');
  l.innerHTML=fil.map((s,i)=>`<div class="qi${i===idx?' active':''}" onclick="jump(${i})"><span class="qi-n">${i+1}</span><span class="qi-t">${s.ticker}</span><span class="qi-nm">${s.name}</span><span class="qg ${qGCl(s.score)}">${s.score}</span></div>`).join('');
  document.getElementById('qcnt').textContent=fil.length+' val.';
  const a=l.querySelector('.active');
  if(a)a.scrollIntoView({block:'nearest'});
}
function updHK(){
  const pct=Math.round((idx+1)/fil.length*100);
  document.getElementById('pgb').style.width=pct+'%';
  document.getElementById('hkP').textContent=pct+'%';
  document.getElementById('hkT').textContent=S.length;
  document.getElementById('hkD').textContent=cycles*fil.length+idx+1;
  document.getElementById('hkAB').textContent=S.filter(s=>s.score==='A'||s.score==='B').length;
  document.getElementById('hkZ').textContent=S.filter(s=>s.zone||(s.price>=s.el&&s.price<=s.eh)).length;
}

// ═══════════ CONTROLS ═══════════
function filt(f,btn){
  document.querySelectorAll('.h-ctrl .fb').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  const m={all:()=>S,large:()=>S.filter(s=>s.cap==='large'),mid:()=>S.filter(s=>s.cap==='mid'),
   small:()=>S.filter(s=>s.cap==='small'),srd:()=>S.filter(s=>s.srd),A:()=>S.filter(s=>s.score==='A'),
   B:()=>S.filter(s=>s.score==='B'),C:()=>S.filter(s=>s.score==='C'),D:()=>S.filter(s=>s.score==='D'),
   buy:()=>S.filter(s=>s.rec==='buy'),rend:()=>S.filter(s=>s.yield>=5),
   zone:()=>S.filter(s=>s.price>=s.el&&s.price<=s.eh||s.zone),
   fort30:()=>S.filter(s=>s.score==='A'&&s.pio>=7&&s.price>=s.el&&s.price<=s.eh&&s.price>s.mm200&&s.rsi<65)};
  fil=(m[f]||m.all)();idx=0;cycles=0;show(0);buildQ();
}
const MOAT_CRITERIA = [
  "Modele economique clair et comprehensible",
  "Produits essentiels (pas juste souhaites)",
  "Achats reguliers / recurrents",
  "Base de clients large et diversifiee",
  "Attachement client / cout de changement eleve",
  "Effet de reseau",
  "Leadership sur son secteur",
  "Avantage competitif durable",
  "Pouvoir de fixation des prix (pricing power)",
  "Potentiel de croissance long terme",
  "Faible dependance a une technologie externe",
  "Management aligne avec les actionnaires"
];
window._moatWork = window._moatWork || {};

function moatVal(s, i) {
  const w = window._moatWork[s.ticker];
  if (w && w[i] !== undefined) return w[i];
  if (s.moatChk && s.moatChk[i] !== undefined) return s.moatChk[i];
  return null;
}
function moatScoreInfo(s) {
  let sum = 0, n = 0;
  for (let i = 0; i < MOAT_CRITERIA.length; i++) {
    const v = moatVal(s, i);
    if (v !== null) { sum += v; n++; }
  }
  return { pct: n > 0 ? Math.round(sum / n * 100) : null, answered: n, total: MOAT_CRITERIA.length };
}
function setMoatCrit(ticker, idx, val) {
  window._moatWork[ticker] = window._moatWork[ticker] || {};
  window._moatWork[ticker][idx] = val;
  const el = document.getElementById('moatgrid-' + ticker);
  const s = S.find(x => x.ticker === ticker);
  if (el && s) el.innerHTML = renderMoatGrid(s);
}
function copyMoatSummary(ticker) {
  const s = S.find(x => x.ticker === ticker);
  const info = moatScoreInfo(s);
  let txt = `${ticker} moat: ${info.pct !== null ? info.pct + '%' : 'non evalue'} (${info.answered}/${info.total})\n`;
  MOAT_CRITERIA.forEach((c, i) => {
    const v = moatVal(s, i);
    txt += `- ${c}: ${v === null ? '?' : v === 1 ? 'Bien' : v === 0.5 ? 'Moyen' : 'Pas bien'}\n`;
  });
  if (navigator.clipboard) navigator.clipboard.writeText(txt);
  return txt;
}
function renderMoatGrid(s) {
  const info = moatScoreInfo(s);
  const scoreTxt = info.pct !== null
    ? `<b style="font-size:18px;color:var(--gd)">${info.pct}%</b> <span style="font-size:10px;color:var(--mu)">(${info.answered}/${info.total} évalués)</span>`
    : `<span style="font-size:11px;color:var(--mu)">Non évalué -- coche les critères ci-dessous</span>`;
  const rows = MOAT_CRITERIA.map((c, i) => {
    const v = moatVal(s, i);
    const btn = (val, label) => {
      const active = v === val;
      return `<button onclick="setMoatCrit('${s.ticker}',${i},${val})" style="padding:2px 8px;font-size:9px;border-radius:3px;border:1px solid var(--bd);cursor:pointer;background:${active ? 'var(--gd)' : 'transparent'};color:${active ? '#fff' : 'var(--tx)'}">${label}</button>`;
    };
    return `<div style="display:flex;align-items:center;gap:6px;padding:3px 0;border-bottom:1px solid var(--bd)">
      <span style="flex:1;font-size:10px">${c}</span>
      <div style="display:flex;gap:3px">${btn(0,'Pas bien')}${btn(0.5,'Moyen')}${btn(1,'Bien')}</div>
    </div>`;
  }).join('');
  return `<div style="margin-bottom:8px">${scoreTxt}</div>${rows}
    <button onclick="copyMoatSummary('${s.ticker}')" style="margin-top:8px;padding:4px 10px;font-size:10px;border-radius:4px;border:1px solid var(--bd);cursor:pointer;background:transparent;color:var(--tx)">📋 Copier le résumé (à me donner pour enregistrer)</button>`;
}

function filterFile(query){
  const q=(query||'').trim().toLowerCase();
  fil=q?S.filter(s=>s.ticker.toLowerCase().includes(q)||(s.name||'').toLowerCase().includes(q)):[...S];
  idx=0;cycles=0;buildQ();if(fil.length>0)show(0);
}
function setSpd(v){spd=parseInt(v);document.getElementById('spL').textContent=v+'s';if(!paused){clearInterval(tmr);startR();}}
function tPause(){
  paused=!paused;
  document.getElementById('pbtn').textContent=paused?'▶ Reprendre':'⏸ Pause';
  if(paused)clearInterval(tmr);else startR();
}
function jump(i){idx=i;show(i);buildQ();}
function startR(){tmr=setInterval(()=>{idx++;if(idx>=fil.length){idx=0;cycles++;}show(idx);buildQ();},spd*1000);}

// ═══════════ PAGE SWITCH ═══════════
function showPg(pg,btn){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.ntab').forEach(t=>t.classList.remove('active'));
  const pgEl=document.getElementById('pg-'+pg);if(pgEl)pgEl.classList.add('active');else return;
  if(btn)btn.classList.add('active');
  if(pg==='tb')buildT(S);
  if(pg==='lx')buildLex();
  if(pg==='etf')buildETF();
  if(pg==='ptf'){
    ptfInit();
    ptfLoadProfile(window._ptfProfile||'val');
    ptfPreloadVal();
    ptfRender();
    // Debug: afficher le nombre de positions
    var dbg=document.getElementById('ptf-debug-banner');
    if(dbg){
      if(PTF.length===0){
        dbg.style.display='block';
        dbg.textContent='⚠️ Portefeuille vide. Ajoute tes positions avec le formulaire.';
      } else {
        dbg.style.display='none';
      }
    }
    console.log('[PTF] Profil='+window._ptfProfile+' Positions='+PTF.length);
  }
  if(pg==='acad')buildAcad('magic');
  if(pg==='pres')buildPres();
  if(pg==='plan')buildPlan();
  if(pg==='bt')buildBt();
  if(pg==='al')buildAlertes();
}

// ═══════════ RECAP TABLE ═══════════
function buildT(data){
  document.getElementById('rtbody').innerHTML=data.map(s=>{
    const u=up(s);const inZ=s.price>=s.el&&s.price<=s.eh||s.zone;
    const gr={A:'qA',B:'qB',C:'qC',D:'qD'};
    return `<tr class="${inZ?'zone-row':''}">
      <td onclick="goStock('${s.ticker}')">${s.ticker}${inZ?'📍':''}</td>
      <td>${s.name}</td>
      <td><span class="rtg ${gr[s.score]||'qC'}">${s.score}</span></td>
      <td><span class="rb ${rCl(s.rec)}" style="padding:1px 4px;font-size:7px">${s.rec.toUpperCase()}</span></td>
      <td>${s.price}€</td>
      <td style="color:var(--gn)">${s.el}–${s.eh}€</td>
      <td style="color:var(--rd)">${s.stop}€</td>
      <td style="color:var(--bl)">${s.o1}€</td>
      <td style="color:${rratio(s)>=2?'var(--gn)':rratio(s)>=1?'var(--gd)':'var(--rd)'}">${rratio(s)}x</td>
      <td>${s.dcfm}€</td>
      <td style="color:${uc(u)};font-weight:600">${parseFloat(u)>0?'+':''}${u}%</td>
      <td style="color:${mc('pe',s.pe)==='good'?'var(--gn)':mc('pe',s.pe)==='bad'?'var(--rd)':'inherit'}">${s.pe}x</td>
      <td>${s.pb}x</td><td>${s.ev_ebitda}x</td><td>${s.ps}x</td>
      <td style="color:${mc('roe',s.roe)==='good'?'var(--gn)':mc('roe',s.roe)==='bad'?'var(--rd)':'inherit'}">${s.roe}%</td>
      <td>${s.roic}%</td><td>${s.roa}%</td>
      <td style="color:${mc('debt',s.debt)==='bad'?'var(--rd)':mc('debt',s.debt)==='warn'?'var(--or)':'inherit'}">${s.debt}x</td>
      <td>${s.ic===999?'∞':s.ic}x</td>
      <td style="color:${s.yield>=5?'var(--gn)':'inherit'}">${s.yield}%</td>
      <td>${s.margin}%</td><td>${s.gm}%</td>
      <td style="color:${mc('fcf',s.fcf)==='good'?'var(--gn)':'inherit'}">${s.fcf}%</td>
      <td style="color:${mc('capr',s.capr)==='good'?'var(--gn)':mc('capr',s.capr)==='warn'?'var(--or)':'inherit'}">${s.capr}%</td>
      <td style="color:${s.epsg>=10?'var(--gn)':s.epsg<0?'var(--rd)':'inherit'}">${s.epsg}%</td>
      <td style="color:${s.pio>=7?'var(--gn)':s.pio<=3?'var(--rd)':'inherit'}">${s.pio}/9</td>
      <td style="color:${s.alt>3?'var(--gn)':s.alt<1.8&&s.alt>0?'var(--rd)':'var(--gd)'}">${s.alt||'—'}</td>
      <td>${s.rsi}</td>
      <td><span class="tag t-cap" style="font-size:7px">${cL[s.cap]}</span></td>
    </tr>`;
  }).join('');
}
function tf(f,btn){
  document.querySelectorAll('#pg-tb .fb').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  const m={all:S,A:S.filter(s=>s.score==='A'),AB:S.filter(s=>s.score==='A'||s.score==='B'),
   buy:S.filter(s=>s.rec==='buy'),zone:S.filter(s=>s.price>=s.el&&s.price<=s.eh||s.zone),
   rend:S.filter(s=>s.yield>=5)};
  buildT(m[f]||S);
}
function srt(col){
  if(srtC===col)srtD*=-1;else{srtC=col;srtD=1;}
  const colMap={ticker:'ticker',x2:'',x2s:'',name:'name',score:'score',rec:'rec',price:'price',entry_low:'el',
   stop:'stop',obj1:'o1',rr:null,dcf_base:'dcfm',upside:null,pe:'pe',pb:'pb',ev_ebitda:'ev_ebitda',
   ps:'ps',roe:'roe',roic:'roic',roa:'roa',debt:'debt',ic:'ic',yield:'yield',margin:'margin',
   gross_margin:'gm',fcf:'fcf',capex_rev:'capr',eps_growth:'epsg',piotroski:'pio',altman:'alt',rsi:'rsi',cap:'cap'};
  const fld=colMap[col];
  const d=[...S].sort((a,b)=>{
    let va=fld?a[fld]||0:0,vb=fld?b[fld]||0:0;
    if(col==='upside'){va=parseFloat(up(a));vb=parseFloat(up(b));}
    if(col==='rr'){va=parseFloat(rratio(a))||0;vb=parseFloat(rratio(b))||0;}
    if(typeof va==='string')return srtD*(va.localeCompare(vb));
    return srtD*(va-vb);
  });
  buildT(d);
}
function goStock(ticker){
  const i=S.findIndex(s=>s.ticker===ticker);
  if(i<0)return;
  idx=i;fil=[...S];
  showPg('sc',document.querySelectorAll('.ntab')[0]);
  show(i);buildQ();
}

// ═══════════ LEXIQUE ═══════════
const LEX=[
 {term:'P/E (Price/Earnings)',cat:'v',short:'Combien l\'investisseur paie pour 1€ de bénéfice.',
  formula:'Cours / BPA annuel',
  interp:'<span class="lex-good">< 12 : Sous-valorisé</span> · <span class="lex-warn">12-25 : Normal</span> · <span class="lex-bad">> 30 : Cher</span>',
  ex:'LVMH à 22x PE = vous payez 22€ pour 1€ de bénéfice annuel prévisible. P/E bas ≠ forcément bon si les bénéfices vont baisser.'},
 {term:'EV/EBITDA',cat:'v',short:'Valorisation de l\'entreprise entière (dette incluse) vs son profit opérationnel brut.',
  formula:'(Capitalisation + Dette nette) / EBITDA',
  interp:'<span class="lex-good">< 8x : Bon marché</span> · <span class="lex-warn">8-14x : Normal</span> · <span class="lex-bad">> 16x : Cher</span>',
  ex:'TotalEnergies à 5x EV/EBITDA = très bon marché. GTT à 15x = prime justifiée par le monopole.'},
 {term:'P/B (Price/Book)',cat:'v',short:'Le cours vs la valeur comptable nette des actifs de la société.',
  formula:'Cours / Actif Net Comptable par action',
  interp:'<span class="lex-good">< 1 : Décote sur actifs</span> · <span class="lex-warn">1-3 : Standard</span> · <span class="lex-bad">> 5 : Prime élevée</span>',
  ex:'SocGen à 0.5x PB = vous achetez 1€ d\'actifs pour 50 centimes. Mais ces actifs peuvent valoir moins en réalité.'},
 {term:'P/S (Price/Sales)',cat:'v',short:'Le cours vs le chiffre d\'affaires. Utile quand les bénéfices sont négatifs.',
  formula:'Capitalisation boursière / Chiffre d\'affaires annuel',
  interp:'<span class="lex-good">< 1 : Très bon marché</span> · <span class="lex-warn">1-3 : Raisonnable</span> · <span class="lex-bad">> 5 : Premium</span>',
  ex:'GTT à 9.2x P/S reflète sa marge nette de 58% — justifié. Renault à 0.2x P/S traduit les marges très faibles de l\'automobile.'},
 {term:'P/FCF (Price/Free Cash Flow)',cat:'v',short:'Le vrai P/E basé sur le cash effectivement généré, pas les bénéfices comptables.',
  formula:'Cours / FCF par action',
  interp:'<span class="lex-good">< 12x : Très attractif</span> · <span class="lex-warn">12-20x : Correct</span> · <span class="lex-bad">> 25x : Cher</span>',
  ex:'Toujours comparer P/FCF et P/E : si P/FCF >> P/E, les bénéfices comptables sont "trop beaux" vs le cash réel.'},
 {term:'DCF (Discounted Cash Flow)',cat:'v',short:'Valorisation intrinsèque : la valeur actuelle de tous les flux futurs actualisés.',
  formula:'Valeur = Σ (FCF_n / (1+WACC)^n) + Valeur terminale',
  interp:'Upside > 20% = opportunité · Upside 0-20% = correctement valorisé · Upside négatif = surévalué',
  ex:'LVMH : DCF base 680€ vs cours 598€ = +14% d\'upside théorique. Le DCF dépend des hypothèses (WACC, croissance).'},
 {term:'Ratio R/R (Risque/Rendement)',cat:'v',short:'Pour 1€ risqué (stop-loss), combien de potentiel jusqu\'à l\'objectif.',
  formula:'(Objectif - Cours) / (Cours - Stop Loss)',
  interp:'<span class="lex-good">R/R > 2 : Excellent</span> · <span class="lex-warn">R/R 1-2 : Correct</span> · <span class="lex-bad">R/R < 1 : Défavorable</span>',
  ex:'Cours 100€, Stop 90€, Objectif 130€ → R/R = (130-100)/(100-90) = 3x. Pour 10€ risqués, 30€ potentiels.'},
 {term:'ROE (Return on Equity)',cat:'r',short:'Combien de profit la société génère pour chaque euro de fonds propres investis.',
  formula:'Résultat net / Capitaux propres × 100',
  interp:'<span class="lex-good">> 18% : Excellent</span> · <span class="lex-warn">9-18% : Correct</span> · <span class="lex-bad">< 9% : Faible</span>',
  ex:'GTT ROE 85% = exceptionnel. Air Liquide ROE 16% = solide mais banale. Attention : ROE élevé peut venir d\'un endettement fort.'},
 {term:'ROIC (Return on Invested Capital)',cat:'r',short:'Le rendement sur l\'ensemble du capital investi (fonds propres + dette). Plus juste que le ROE.',
  formula:'NOPAT / (Fonds propres + Dette nette)',
  interp:'<span class="lex-good">> 13% : Crée de la valeur</span> · <span class="lex-warn">7-13% : OK</span> · <span class="lex-bad">< 7% : Détruit de la valeur</span>',
  ex:'La règle d\'or : si ROIC > WACC (coût du capital ~8%), la société crée de la valeur. Si ROIC < WACC, elle détruit de la valeur même si elle est "profitable".'},
 {term:'ROA (Return on Assets)',cat:'r',short:'Rentabilité par rapport à l\'ensemble des actifs du bilan.',
  formula:'Résultat net / Total actif × 100',
  interp:'<span class="lex-good">> 10% : Très efficace</span> · <span class="lex-warn">5-10% : Normal</span> · <span class="lex-bad">< 5% : Actifs lourds</span>',
  ex:'GTT ROA 52% = extraordinaire (actifs légers, IP pur). Air Liquide ROA 8% = actifs lourds (pipelines, usines) mais stables.'},
 {term:'Marge Nette',cat:'r',short:'% du chiffre d\'affaires qui devient profit final après toutes les charges.',
  formula:'Résultat net / Chiffre d\'affaires × 100',
  interp:'<span class="lex-good">> 18% : Premium</span> · <span class="lex-warn">8-18% : Correct</span> · <span class="lex-bad">< 5% : Mince</span>',
  ex:'GTT 58% marge = exceptionnelle (IP pur). L\'Oréal 20% = très bien pour la grande conso. Renault 6% = marge auto normale mais vulnérable.'},
 {term:'Marge Brute',cat:'r',short:'% de CA restant après les coûts directs de production. Mesure le pricing power.',
  formula:'(CA - Coût des ventes) / CA × 100',
  interp:'<span class="lex-good">> 50% : Pricing power fort</span> · <span class="lex-warn">30-50% : Moyen</span> · <span class="lex-bad">< 25% : Faible</span>',
  ex:'L\'Oréal 74% marge brute = énorme pricing power sur les cosmétiques. Renault 20% = marges auto très comprimées par les coûts matières.'},
 {term:'FCF Yield (Free Cash Flow Yield)',cat:'r',short:'Le flux de trésorerie libre disponible pour l\'actionnaire, rapporté au cours.',
  formula:'FCF par action / Cours × 100',
  interp:'<span class="lex-good">> 7% : Généreux</span> · <span class="lex-warn">3-7% : Correct</span> · <span class="lex-bad">< 3% : Maigre</span>',
  ex:'Coface FCF yield 9.2% = excellent. Le FCF yield > dividende yield signifie que le dividende est bien couvert et durable.'},
 {term:'Dette/EBITDA',cat:'k',short:'Nombre d\'années de profit opérationnel pour rembourser toute la dette.',
  formula:'Dette nette / EBITDA annuel',
  interp:'<span class="lex-good">< 1x : Faible dette</span> · <span class="lex-warn">1-2.5x : Modere</span> · <span class="lex-bad">> 3x : Élevé</span>',
  ex:'GTT 0x (pas de dette) = bilan de forteresse. TotalEnergies 1.5x = raisonnable pour une major pétrolière. Altarea 3.8x = élevé, vulnérable aux taux.'},
 {term:'Interest Coverage (Couverture des intérêts)',cat:'k',short:'Combien de fois l\'EBIT couvre les charges d\'intérêt annuelles.',
  formula:'EBIT / Charges financières annuelles',
  interp:'<span class="lex-good">> 8x : Très solide</span> · <span class="lex-warn">3-8x : Correct</span> · <span class="lex-bad">< 2x : Risqué</span>',
  ex:'Air Liquide 12.4x = très solide. Si ce ratio < 1.5x, la société risque la défaillance en cas de baisse des profits.'},
 {term:'Current Ratio (Ratio de liquidité courante)',cat:'k',short:'Capacité à payer les dettes court terme avec les actifs court terme.',
  formula:'Actifs courants / Passifs courants',
  interp:'<span class="lex-good">> 2 : Très solide</span> · <span class="lex-warn">1-2 : Correct</span> · <span class="lex-bad">< 1 : Tension liquidité</span>',
  ex:'GTT Current Ratio 3.2 = très solide. Les banques ont un ratio de 0 (modèle différent) — ne pas comparer avec les autres secteurs.'},
 {term:'Piotroski F-Score',cat:'k',short:'Score 0-9 mesurant la solidité financière sur 9 critères binaires (rentabilité, levier, efficacité).',
  formula:'Somme de 9 critères : ROA>0, ΔCF>0, ΔROA>0, Accruals<0, ΔLevier<0, ΔLiquidité>0, ΔActions=0, ΔMarge>0, ΔRotation>0',
  interp:'<span class="lex-good">8-9 : Excellent</span> · <span class="lex-warn">5-7 : Solide</span> · <span class="lex-bad">< 4 : Fragile</span>',
  ex:'GTT Piotroski 9/9 = société financièrement parfaite. Un score < 3 signale souvent une société en difficulté structurelle avant que le marché le réalise.'},
 {term:'Altman Z-Score',cat:'k',short:'Modèle statistique prédisant la probabilité de faillite dans les 2 ans.',
  formula:'1.2×(BFR/Actifs) + 1.4×(Bénéfices/Actifs) + 3.3×(EBIT/Actifs) + 0.6×(Marché/Dettes) + CA/Actifs',
  interp:'<span class="lex-good">> 3 : Zone sûre</span> · <span class="lex-warn">1.8-3 : Zone grise</span> · <span class="lex-bad">< 1.8 : Danger faillite</span>',
  ex:'GTT Z-Score 8.2 = ultra-solide. Attention : les banques et assurances ont un Z-Score de 0 car le modèle ne s\'applique pas à leur structure de bilan.'},
 {term:'Bêta (β)',cat:'k',short:'Sensibilité du titre aux mouvements du marché (CAC 40).',
  formula:'Covariance(titre,marché) / Variance(marché)',
  interp:'<span class="lex-good">β < 0.7 : Défensif</span> · <span class="lex-warn">β 0.7-1.2 : Normal</span> · <span class="lex-bad">β > 1.5 : Volatile</span>',
  ex:'Air Liquide β 0.6 = défensif (monte moins que le marché mais chute aussi moins). Renault β 1.8 = cyclique et volatile.'},
 {term:'RSI (Relative Strength Index)',cat:'t',short:'Oscillateur technique 0-100 mesurant la force/faiblesse des variations récentes.',
  formula:'RSI = 100 - 100/(1 + (Moyenne hausses 14j / Moyenne baisses 14j))',
  interp:'<span class="lex-bad">> 70 : Suracheté (prudence)</span> · <span class="lex-good">< 30 : Survendu (opportunité)</span> · <span class="lex-warn">45-55 : Neutre</span>',
  ex:'L\'Oréal RSI 49 = neutre, ni suracheté ni survendu. TotalEnergies RSI 44 = légèrement baissier, potentielle zone d\'accumulation.'},
 {term:'MM50 & MM200 (Moyennes Mobiles)',cat:'t',short:'Prix moyen des 50 et 200 dernières séances. Indicateurs de tendance.',
  formula:'MM50 = Moyenne des cours des 50 derniers jours',
  interp:'Cours > MM200 = tendance haussière · Cours < MM200 = tendance baissière · MM50 croise MM200 vers le haut = "Golden Cross" haussier',
  ex:'SAF +5% vs MM50 et +12% vs MM200 = tendance haussière forte. TTE -5% vs MM200 = tendance baissière, attendre confirmation.'},
 {term:'Supports & Résistances',cat:'t',short:'Niveaux de prix où historiquement les acheteurs (support) ou vendeurs (résistance) dominent.',
  formula:'Identification visuelle sur les graphiques (pics/creux récurrents)',
  interp:'Zone de support = prix d\'achat privilégié · Résistance franchie = nouveau support · Stop-loss toujours sous le support',
  ex:'Zone d\'achat L\'Oréal 315-348€ = entre support technique et zone de valeur fondamentale. Stop 290€ = sous le support majeur.'},
 {term:'CAPEX (Capital Expenditure)',cat:'s',short:'Investissements en actifs physiques (usines, machines, équipements) nécessaires à l\'activité.',
  formula:'Figurent dans le tableau de flux de trésorerie',
  interp:'CAPEX/CA < 5% = actif léger · 5-12% = modere · > 15% = très capitalistique',
  ex:'GTT CAPEX 1.5% du CA = modèle IP pur, quasi pas d\'investissements. Air Liquide 14.8% = infrastructure lourde (pipelines, usines). Le CAPEX/Amortissements > 1 signale une phase d\'expansion.'},
 {term:'CAPEX/Amortissements',cat:'s',short:'Ratio mesurant si la société investit pour croître ou juste maintenir ses actifs existants.',
  formula:'CAPEX annuel / Dotations aux amortissements',
  interp:'<span class="lex-bad">< 0.8 : Sous-investissement (attrition)</span> · <span class="lex-warn">0.8-1.2 : Maintenance</span> · <span class="lex-good">> 1.5 : Expansion</span>',
  ex:'Air Liquide CAPEX/DA 1.4x = en expansion moderee. Mersen 1.5x = expansion forte (SiC). Un ratio < 0.7 sur plusieurs années signale un actif en fin de vie.'},
 {term:'Moat (Fossé économique)',cat:'s',short:'Avantage concurrentiel durable qui protège les marges et parts de marché sur le long terme.',
  formula:'Qualitatif : brevets, effets réseau, coûts de changement, économies d\'échelle, marques',
  interp:'Fort = 15+ ans de protection · Modere = 5-15 ans · Faible = facilement attaquable',
  ex:'GTT : monopole de brevets = moat absolu. L\'Oréal : 37 marques + R&D = moat très fort. Renault : quelques avantages mais facilement attaqués par BYD.'},
 {term:'Piotroski vs Track Record',cat:'s',short:'Deux mesures complémentaires : l\'une quantitative (solidité bilan), l\'autre qualitative (crédibilité direction).',
  formula:'Piotroski = état financier actuel · Track Record = fiabilité des guidances sur 3 ans',
  interp:'Idéal : Piotroski 7+ ET Track Record 75%+. Danger : bilan solide mais direction qui ment → risque de surprise négative.',
  ex:'SAF : Piotroski 8 + Track Record 100% = management ultra-crédible. Renault : Piotroski 6 + Track Record 50% = à surveiller.'},
 {term:'Score Altman pour les banques',cat:'k',short:'Attention : le Z-Score d\'Altman ne s\'applique PAS aux banques et assurances.',
  formula:'Le modèle a été conçu pour les entreprises industrielles',
  interp:'Pour les banques, utiliser : CET1 (> 12% = solide), ROE vs COE, NII spread',
  ex:'BNP Altman = 0 dans notre screener = non applicable (banque). Utiliser à la place CET1 13.5%, ROE 11%, coefficient d\'exploitation 65%.'},
 {term:'EV/EBIT vs EV/EBITDA',cat:'v',short:'EV/EBIT tient compte des amortissements — plus conservateur pour les actifs lourds.',
  formula:'EV/EBIT = (Capitalisation + Dette) / (EBITDA - Amortissements)',
  interp:'Pour les actifs légers (IP, logiciel) : EV/EBITDA suffit. Pour les actifs lourds : préférer EV/EBIT car les amortissements sont réels.',
  ex:'Air Liquide EV/EBITDA 16x vs EV/EBIT 19x : l\'écart montre l\'importance des amortissements de ses actifs lourds.'},
 {term:'Debt/Equity (Gearing)',cat:'k',short:'Ratio d\'endettement : la dette nette comparée aux fonds propres.',
  formula:'Dette nette / Capitaux propres',
  interp:'<span class="lex-good">< 0.5 : Peu endetté</span> · <span class="lex-warn">0.5-1 : Modere</span> · <span class="lex-bad">> 1.5 : Très endetté</span>',
  ex:'GTT Debt/Equity 0 = zéro endettement. Altarea 2.8x = très endetté (foncière). La dette n\'est pas mauvaise si le ROIC > coût de la dette.'},
 {term:'Track Record Direction',cat:'s',short:'Analyse rétrospective des guidances données et tenues (ou non) par le management.',
  formula:'% guidances tenues = (Tenues + 0.5×Partielles) / Total',
  interp:'<span class="lex-good">> 75% : Management crédible</span> · <span class="lex-warn">50-75% : Prudence</span> · <span class="lex-bad">< 50% : Sur-promesse récurrente</span>',
  ex:'Air Liquide 100% = management qui fait ce qu\'il dit. LVMH 50% sur la Chine 2023 = facteur externe. Renault 33% = historique de déception sur le BEV et la croissance.'},
 {term:'Zone d\'Achat (Support Technique)',cat:'t',short:'Plage de prix représentant le meilleur rapport risque/rendement basé sur les niveaux techniques et fondamentaux.',
  formula:'Borne basse = support technique ou DCF bear case · Borne haute = résistance proche',
  interp:'Dans la zone = bon point d\'entrée. Au-dessus = attendre correction. Combinaison fondamentaux + technique est idéale.',
  ex:'L\'Oréal zone 315-348€ : sous 315€ = excellent (approche DCF bear 280€ + support tech), au-dessus 395€ = attendre la prochaine correction.'},
];
let lexCat='all';
function buildLex(){
  const g=document.getElementById('lex-grid');
  let data=LEX;
  if(lexCat!=='all')data=data.filter(l=>l.cat===lexCat);
  const q=document.querySelector('.lex-search')?.value||'';
  if(q)data=data.filter(l=>l.term.toLowerCase().includes(q.toLowerCase())||l.short.toLowerCase().includes(q.toLowerCase()));
  g.innerHTML=data.map((l,i)=>`<div class="lcard2" onclick="this.classList.toggle('open')">
    <div class="lterm">${l.term}</div>
    <span class="lctag c${l.cat}">${{v:'Valorisation',r:'Rentabilité',k:'Risque',t:'Technique',s:'Stratégie'}[l.cat]}</span>
    <div class="ldef">${l.short}</div>
    <div class="ldetail">
      <div class="lform">Formule : ${l.formula}</div>
      <div class="linterp">${l.interp}</div>
      ${l.ex?`<div class="ldef" style="margin-top:5px;color:var(--tx2)">💡 ${l.ex}</div>`:''}
    </div>
  </div>`).join('');
}
function filterLex(q){buildLex();}
function filterLexCat(c,btn){
  document.querySelectorAll('.lcat').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  lexCat=c;buildLex();
}



// ═══════════ EXCEL ═══════════
function xls(){
  try{
    if(typeof XLSX==='undefined'){alert('Bibliothèque XLSX non chargée. Ouvre le fichier HTML sur ton PC.');return;}
    const wb=XLSX.utils.book_new();
    const h=['Ticker','Société','Secteur','Cap','Indice','SRD','Note','Rec.','Cours','Zone Entrée','Stop','Obj.1','R/R','DCF Bear','DCF Base','DCF Bull','Upside%','P/E','P/B','EV/EBITDA','P/S','ROE%','ROIC%','ROA%','Dett/EBITDA','Int.Cov.','Div%','Marge%','Marge Brute%','FCF%','CAPEX/CA%','BPA%','Piotroski/9','Altman Z','RSI','MM50','MM200','Track%','Cible','Buy','Hold','Sell'];
    const rows=S.map(s=>[s.ticker,s.name,s.sector,s.cap,s.idx,s.srd?'Oui':'Non',s.score,s.rec,s.price,s.el+'-'+s.eh+'€',s.stop,s.o1,rratio(s),s.dcfb,s.dcfm,s.dcfu,parseFloat(up(s)),s.pe,s.pb,s.ev_ebitda,s.ps,s.roe,s.roic,s.roa,s.debt,s.ic===999?'∞':s.ic,s.yield,s.margin,s.gm,s.fcf,s.capr,s.epsg,s.pio,s.alt||'N/A',s.rsi,s.mm50,s.mm200,trOk(s.track),s.tp,s.cb,s.ch,s.cs]);
    XLSX.utils.book_append_sheet(wb,XLSX.utils.aoa_to_sheet([h,...rows]),'Synthèse Complète');
    const pep=S.filter(s=>s.score==='A');
    XLSX.utils.book_append_sheet(wb,XLSX.utils.aoa_to_sheet([h,...pep.map(s=>[s.ticker,s.name,s.sector,s.cap,s.idx,s.srd?'Oui':'Non',s.score,s.rec,s.price,s.el+'-'+s.eh+'€',s.stop,s.o1,rratio(s),s.dcfb,s.dcfm,s.dcfu,parseFloat(up(s)),s.pe,s.pb,s.ev_ebitda,s.ps,s.roe,s.roic,s.roa,s.debt,s.ic===999?'∞':s.ic,s.yield,s.margin,s.gm,s.fcf,s.capr,s.epsg,s.pio,s.alt||'N/A',s.rsi,s.mm50,s.mm200,trOk(s.track),s.tp,s.cb,s.ch,s.cs])]),'⭐ Pépites Grade A');
    const rnd=S.filter(s=>s.yield>=4).sort((a,b)=>b.yield-a.yield);
    XLSX.utils.book_append_sheet(wb,XLSX.utils.aoa_to_sheet([['Ticker','Société','Note','Cours','Div%','FCF%','Couverture','Stop','Obj.1'],...rnd.map(s=>[s.ticker,s.name,s.score,s.price,s.yield,s.fcf,(s.fcf/s.yield).toFixed(1)+'x',s.stop,s.o1])]),'💰 Top Rendements');
    const byP=[...S].sort((a,b)=>b.pio-a.pio);
    XLSX.utils.book_append_sheet(wb,XLSX.utils.aoa_to_sheet([['Ticker','Société','Piotroski','Qualité','Altman','Zone','IntCov','FCF%','Track%','Note'],...byP.map(s=>[s.ticker,s.name,s.pio,piL(s.pio),s.alt||'N/A',s.alt?(s.alt>3?'Sûre':s.alt>1.8?'Grise':'Danger'):'N/A',s.ic===999?'∞':s.ic,s.fcf,trOk(s.track),s.score])]),'🛡️ Solidité');
    const byU=[...S].sort((a,b)=>parseFloat(up(b))-parseFloat(up(a)));
    XLSX.utils.book_append_sheet(wb,XLSX.utils.aoa_to_sheet([['Ticker','Société','Cours','Zone','Stop','Obj.1','R/R','Bear','Base','Bull','Upside%','Cible','Note'],...byU.map(s=>[s.ticker,s.name,s.price,s.el+'-'+s.eh+'€',s.stop,s.o1,rratio(s),s.dcfb,s.dcfm,s.dcfu,parseFloat(up(s)),s.tp,s.score])]),'📈 DCF & Entrées');
    const etfH=['Ticker','Nom','Émetteur','ISIN','Type','Frais%','Perf 1an%','Perf 5ans%','Encours','Note'];
    XLSX.utils.book_append_sheet(wb,XLSX.utils.aoa_to_sheet([etfH,...ETF.map(e=>[e.ticker,e.name,e.emetteur,e.isin,e.type,e.frais,e.perf1y,e.perf5y,e.encours,e.note])]),'🌍 ETF PEA');
    XLSX.writeFile(wb,`PEA_Screener_Pro_v4_${new Date().toISOString().split('T')[0]}.xlsx`);
  }catch(err){alert('Export Excel : ouvre le fichier HTML local (pas dans Claude). Erreur : '+err.message);}
}

// ═══════════ LIVE DATA ═══════════
async function fetchLive(){
  const st=document.getElementById('live-st');
  if(st)st.textContent='🔄 Chargement en cours... (30-60s)';
  
  // CORS proxy requis depuis GitHub Pages - Yahoo bloque les appels directs
  // corsproxy.io est fiable et gratuit
  const proxy='https://corsproxy.io/?';
  
  const map={
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA','TTE':'TTE.PA',
    'SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA','ACA':'ACA.PA','GLE':'GLE.PA',
    'AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA','ORA':'ORA.PA','VIE':'VIE.PA','RNO':'RNO.PA',
    'SGO':'SGO.PA','CAP':'CAP.PA','DG':'DG.PA','VIV':'VIV.PA','RI':'RI.PA','LR':'LR.PA',
    'WLN':'WLN.PA','DSY':'DSY.PA','STM':'STM.PA','EL':'EL.PA','ML':'ML.PA','ENGI':'ENGI.PA',
    'MT':'MT.AS','URW':'URW.AS','SW':'SW.PA','TEP':'TEP.PA','EN':'EN.PA','AC':'AC.PA',
    'AF':'AF.PA','BN':'BN.PA','CA':'CA.PA','HO':'HO.PA','GTT':'GTT.PA','COFA':'COFA.PA',
    'MERY':'MRY.PA','JXS':'JXS.PA','SPIE':'SPIE.PA','NEXANS':'NEX.PA','DASSAV':'AM.PA',
    'ALO':'ALO.PA','ELIS':'ELIS.PA','SEB':'SK.PA','ERF':'ERF.PA','IPSOS':'IPS.PA',
    'ABCA':'ABCA.PA','VK':'VK.PA','FNAC':'FNAC.PA','LNA':'LNA.PA','CNP':'CNP.PA','SOP':'SOP.PA',
    'BIOM':'BIM.PA','KLPI':'LI.PA','RCO':'RCO.PA','EIFFAGE':'FGR.PA','COVIVIO':'COV.PA',
    'TRIGANO':'TRI.PA','BOIRON':'BOI.PA','VIRBAC':'VIRP.PA','INTERPARFUMS':'ITP.PA',
    'CLASQUIN':'ALCLA.PA','ARGAN':'ARG.PA','STEF':'STF.PA','THERMADOR':'THEP.PA',
    'PLUXEE':'PLX.PA','EDENRED':'EDEN.PA','VALO':'FR.PA','FORVIA':'FRVIA.PA',
    'ASML':'ASML.AS','ADYEN':'ADYEN.AS','HEIA':'HEIA.AS','NOVO':'NOVO-B.CO',
    'SAP':'SAP.DE','SIEMENS':'SIE.DE','ALV':'ALV.DE','LVMHF':'RACE.MI'
  };
  
  let ok=0,fail=0,total=Object.keys(map).length;
  const ts=new Date().toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit'});
  
  for(const[t,yf] of Object.entries(map)){
    if(st)st.textContent='🔄 '+ok+'/'+total+' — '+t+'...';
    try{
      const yahooUrl=encodeURIComponent('https://query1.finance.yahoo.com/v8/finance/chart/'+yf+'?interval=1d&range=1d');
      const r=await fetch(proxy+yahooUrl,{signal:AbortSignal.timeout(6000)});
      if(!r.ok){fail++;continue;}
      const d=await r.json();
      const meta=d?.chart?.result?.[0]?.meta;
      if(meta?.regularMarketPrice){
        const price=Math.round(meta.regularMarketPrice*100)/100;
        const prev=meta.previousClose||price;
        const chg=+((price-prev)/prev*100).toFixed(2);
        const s=S.find(x=>x.ticker===t);
        if(s){
          s.price=price; s.chg=chg; ok++;
          const fp=document.getElementById('fp-'+t);
          const fl=document.getElementById('fl-'+t);
          if(fp)fp.textContent=price.toFixed(2)+' €';
          if(fl){fl.textContent='● Mis à jour '+ts;fl.style.color='#5ddb8a';}
        }
      }else fail++;
    }catch(e){fail++;}
    await new Promise(res=>setTimeout(res,100));
  }
  
  if(fil[idx])render(fil[idx]);
  buildT(S);
  
  const msg=ok>0
    ?'✅ '+ok+' cours mis à jour à '+ts+(fail>0?' ('+fail+' échecs)':'')
    :'❌ Proxy indisponible — réessaie dans 1 minute';
  if(st)st.textContent=msg;
}



// ═══════════ ETF DATA ═══════════;

const ETF=[
  {ticker:'CW8',price:710.35,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],name:'MSCI World',emetteur:'Amundi',isin:'LU1681043599',type:'Capitalisant',frais:0.12,perf1y:18.2,perf3y:11.4,perf5y:14.8,encours:'8.2Md€',indice:'MSCI World (1600 titres)',replication:'Synthétique',note:'A',
   avantages:['0.12% frais — le moins cher PEA','Synthétique = éligible PEA','1600 entreprises mondiales'],
   risques:['Risque contrepartie swap (limité 10%)','Exposition USD 70%'],
   verdict:"⭐ LE meilleur ETF PEA. 0.12% imbattable. Si un seul ETF dans votre PEA : c'est celui-là."},
  {ticker:'PAEEM',price:35.36,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],name:'Amundi PEA Emergent (MSCI EM ESG)',emetteur:'Amundi',isin:'FR0013412020',type:'Capitalisant',frais:0.30,perf1y:null,perf3y:null,perf5y:null,encours:'0.27Md€',indice:'MSCI EM (Chine, Inde, Brésil...)',replication:'Synthétique',note:'B',
   avantages:['Seul ETF émergents éligible PEA','Inde croissance structurelle'],
   risques:['Chine 30% risque géopolitique','Volatilité élevée'],
   verdict:'Complément du CW8 pour émergents. Limiter à 15% du portefeuille.'},
  {ticker:'PANX',price:84.86,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],name:'NASDAQ 100',emetteur:'Amundi',isin:'LU1681038243',type:'Capitalisant',frais:0.23,perf1y:28.4,perf3y:10.1,perf5y:22.3,encours:'3.1Md€',indice:'NASDAQ 100 (100 tech US)',replication:'Synthétique',note:'B',
   avantages:['Éligible PEA','Apple, MSFT, Nvidia, Meta...','Performance historique supérieure'],
   risques:['0.23% relativement cher','Concentration 10 titres = 50%'],
   verdict:'Satellite tech US en PEA. Ne pas dépasser 20% du portefeuille.'},
  {ticker:'PCEU',price:39.54,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],name:'Europe ex-UK',emetteur:'Amundi',isin:'LU1681047378',type:'Capitalisant',frais:0.15,perf1y:6.8,perf3y:5.2,perf5y:8.4,encours:'1.2Md€',indice:'MSCI Europe ex-UK',replication:'Synthétique',note:'B',
   avantages:['Complémente CW8 sur Europe','Valorisation attractive PE 13x vs 22x US'],
   risques:['Croissance structurellement faible','Cycliques surpondérés'],
   verdict:"Pour sur-pondérer l'Europe. Pari sur le rattrapage européen."},
  {ticker:'GOLDN',name:'Or Physique',emetteur:'WisdomTree',isin:'DE000A0N62G0',type:'Capitalisant',frais:0.39,perf1y:22.4,perf3y:11.8,perf5y:12.4,encours:'4.2Md€',indice:'Gold Spot Price',replication:'Physique',note:'B',
   avantages:['Couverture inflation & crises','Or physique réel','Décorrélation parfaite actions'],
   risques:['⚠️ Non éligible PEA — compte-titres uniquement','0.39% de frais','Aucun dividende'],
   verdict:'5-10% du portefeuille global en CTO. Assurance contre les crises. Pas dans le PEA.'},
  {ticker:'ESE',price:34.915,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],name:'S&P 500 Core',emetteur:'iShares (BlackRock)',isin:'IE00B5BMR087',type:'Capitalisant',frais:0.07,perf1y:24.1,perf3y:13.2,perf5y:17.6,encours:'95Md€',indice:'S&P 500 (500 grandes US)',replication:'Physique',note:'A',
   avantages:['0.07% ultra-compétitif','Réplication physique','Liquidité maximale'],
   risques:['⚠️ Non éligible PEA direct','Concentration US 70%+'],
   verdict:'Meilleur ETF S&P 500 mondial mais en CTO. En PEA utiliser CW8 (Amundi synthétique).'},
  {ticker:'LYPS',name:'S&P 500 ESG',emetteur:'Lyxor (Amundi)',isin:'LU1792117779',type:'Capitalisant',frais:0.09,perf1y:22.8,perf3y:12.8,perf5y:16.4,encours:'2.1Md€',indice:'S&P 500 ESG filtré',replication:'Synthétique',note:'B',
   avantages:['Éligible PEA','0.09% compétitif','Filtrage ESG','Quasi-même performance S&P 500'],
   risques:['Exclut pétrole/tabac/armement','Concentration tech similaire'],
   verdict:'Alternative au CW8 pour S&P 500 en PEA avec filtre ESG. Frais compétitifs.'},
  {ticker:'RS2K',price:367.6,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],name:'Russell 2000 Small Caps',emetteur:'iShares',isin:'IE00B3YCGJ38',type:'Capitalisant',frais:0.20,perf1y:8.2,perf3y:2.4,perf5y:9.8,encours:'12Md€',indice:'Russell 2000 (2000 small caps US)',replication:'Physique',note:'C',
   avantages:['Diversification hors mega-caps','Bénéficiaire baisse taux US'],
   risques:['⚠️ Non éligible PEA','Très volatile (Beta 1.4)','Sous-performance 2021-2024'],
   verdict:'Satellite optionnel CTO pour small caps US. Attendre confirmation baisse des taux.'},
,
{ticker:'PINR',price:22.185,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],name:'BNPP Easy MSCI World SRI',emetteur:'BNP Paribas',type:'Actions Monde ISR',isin:'FR0013346068',frais:0.25,perf1y:8.2,perf5y:52.1,encours:'2.1Md€',note:'A',
 desc:'ETF monde filtré ESG/ISR avec critères de durabilité stricts. Alternative responsable au CW8.',
 avantages:['ESG SRI filtre fort','BNP émetteur solide','Eligible PEA'],
 risques:['Biais sectoriel ESG','Univers reduit vs CW8']},

{ticker:'PTPXE',price:40.1,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],name:'Amundi PEA S&P 500',emetteur:'Amundi',type:'Actions USA',isin:'LU1681048804',frais:0.15,perf1y:12.5,perf5y:78.3,encours:'1.8Md€',note:'A',
 desc:'Accès au S&P 500 américain via le PEA grâce à une réplication synthétique (swap). La solution la moins chere pour s exposer aux USA depuis un PEA.',
 avantages:['Seul SP500 eligible PEA direct','0.15% frais ultra-bas','Amundi fiable'],
 risques:['Risque contrepartie swap','Dollar/Euro devise']},

{ticker:'DCAM',price:6.34,thesis:'Fiche incomplete : these d investissement a rediger avant tout achat.',contra:'Risques non documentes.',track:[],name:'Amundi PEA Monde (MSCI World)',emetteur:'Amundi',type:'Actions Monde',isin:'FR001400U5Q4',frais:0.20,perf1y:null,perf5y:null,encours:'1.25Md€',note:'A',
 desc:'MSCI World (~1 300 grandes entreprises des pays developpes, ~70 % Etats-Unis) via swap, eligible PEA. Socle du portefeuille (cible 80 % de la poche ETF).',
 avantages:['Frais 0,20 % (parmi les plus bas)','Eligible PEA','Diversification mondiale'],
 risques:['~25 % sur 10 geants de la tech US','Replication synthetique (swap)']},
{ticker:'EUNL',price:130.72,thesis:'',contra:'',track:[],name:'iShares Core MSCI World (compte-titres)',emetteur:'iShares',type:'Actions Monde',isin:'IE00B4L5Y983',frais:0.20,perf1y:null,perf5y:null,encours:'—',note:'CTO',
 desc:'Meme indice que l ETF Monde du PEA, detenu sur le compte-titres (non eligible PEA).',
 avantages:['Frais 0,20 %','Replication physique'],risques:['Doublon de l ETF Monde du PEA','Plus-values taxees (compte-titres)']},
{ticker:'SXR8',price:743.44,thesis:'',contra:'',track:[],name:'iShares Core S&P 500 (compte-titres)',emetteur:'iShares',type:'Actions Etats-Unis',isin:'IE00B5BMR087',frais:0.07,perf1y:null,perf5y:null,encours:'—',note:'CTO',
 desc:'500 grandes entreprises americaines, detenu sur le compte-titres.',
 avantages:['Frais 0,07 %','Replication physique'],risques:['Recoupe ~70 % de l ETF Monde','Concentration tech US']},
{ticker:'XS6R',price:206.45,thesis:'',contra:'',track:[],name:'Xtrackers MSCI Europe Utilities Screened (compte-titres)',emetteur:'Xtrackers',type:'Actions Europe services aux collectivites',isin:'LU0292104899',frais:0.17,perf1y:null,perf5y:null,encours:'87M€',note:'CTO',
 desc:'Electricite, gaz, eau en Europe : secteur defensif, peu correle a la tech.',
 avantages:['Frais 0,17 %','Diversification hors tech'],risques:['Sensible aux taux d interet','Petit encours (87 M€)']}];;
