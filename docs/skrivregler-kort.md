# Skrivregler för nya kortset

Gäller all nyproduktion från leverans 4. Källor: Rogers uppdragsmejl 2026-07-12,
regeldokumentet aug 2026 (`regler-2026-08-sammanfattning.md`) och besluten i
mejlväxlingen aug 2026.

## Format

Varje set skrivs som `cards/<slug>.md` i husformatet. Följ ett befintligt set
(t.ex. `cards/genghis-khan.md`) exakt: titelrad `# <Namn> — fem frågekort`,
rad 3 `Svenskt arbetsnamn: <namn>. Superenkel engelska.`, därefter fem block
`## Kort N · <Nivå> — <Titel>` med **Kategori**, blockquote-korttext som slutar
med exakt en fetstilad fråga, fyra alternativ (`- ✅` / `- ⬜`), `### Ordförklaringar`
samt `### Huvudbild` och `### Sidobild` med fälten **Motiv**, **Bildtext**,
**Shutterstock-sökning**, **AI-prompt**. Validera med
`python3 tools/import_cards.py --check <slug>` tills kontrollen är ren.

## Nivåer och struktur

- Fem kort: Årskurs 6, Årskurs 9, Årskurs 12 (A), Årskurs 12 (B), Universitet.
- 7–12 meningar per kort, superenkel engelska, riktmärke ca sju ord per mening.
- Tempus är fritt sedan 2026-08-26; historiskt presens rekommenderas för
  enhetlighet med befintliga 22 set.
- Korten är oberoende: högst en kort kontextrad återetableras per kort,
  resten varieras. Ingen innehållsupprepning mellan korten i setet.
- Svårighetsramp: åk 6 konkret berättelse, universitet metaperspektiv
  (källor, historiografi, "hur vet vi detta?").

## Frågedesign

- Personen/ämnet anonymiseras (Mr X, Land X, the X people ...) och frågan står
  som enda fetstilade sista blockquote-rad, aldrig dessutom i löptexten.
- Ledtrådskedja: eleven ska kunna resonera sig till svaret. Svaret får aldrig
  förekomma i korttext, korttitel, bildtext eller ordlista, inte heller i
  genomskinlig adjektiv- eller böjningsform ("Socratic", "olympisk").
  Avsiktliga namnekon (Alexandria, juli, augusti, Kaiser) är tillåtna ledtrådar.
- Exakt fyra alternativ, ett rätt. Distraktorer hämtas i första hand från
  masterlistan; behåll "staket"-distraktorer som bär kortets förväxlingspoäng.
- Minimalt med årtal: århundraden eller "about X hundred years ago".
- Skippa åsiktsord (bigger, beautiful, many) eller kvalificera dem.
- Inga parenteser i korttext (skriv om med komma); tankstreck bara som
  pratminus först i replik.

## Ordförklaringar

1–4 svåra ord (utanför de 1 000 vanligaste) med superenkla förklaringar.
Ordet ska förekomma i kortets text.

## Bildbriefer

- Huvudbild liggande 3:2, sidobild stående 2:3. Sidobilden förklarar där det
  går ett svårt ord eller nyckelbegrepp.
- Bildtexter i Mr X-stil, aldrig svaret, aldrig svarsavslöjande motiv.
- Motiv utan läsbar text, bokstäver, siffror eller logotyper (AI-prompterna
  får sitt no-text-suffix automatiskt av pipelinen, men välj motiv där kravet
  är realistiskt, t.ex. boksidor på avstånd eller i vinkel).
- Upprepa inte samma bildmotiv mellan kort i setet (en Sokratesstaty räcker).
- Ange alltid epokens klädsel, vapen och teknik uttryckligen i AI-prompten
  (t.ex. "1770s dress, tricorn hats, knee breeches, muskets", "1840s
  locomotive with tall chimney") och förbjud det troliga felet ("no steel
  helmets, no khaki, no motor vehicles, no electric lamps"). Utan sådana
  ankare faller bildmodellen tillbaka på 1900-talet; i leverans 6 föll 18 av
  70 bilder på detta. Undvik motiv som är textbärare av naturen (tidslinjer,
  liggare, sigill med prägling, boksidor i närbild, skyltar).

## Känslighet och balans

- Idéhistoria före krig; inget krigsförhärligande, ingen gore.
- Kulturneutralt för klassrum i Afrika, Asien, Latinamerika och Europa.
- Tro markeras alltid som tro ("Christians believe", "she says she hears"),
  aldrig som faktum; religiösa gestalter behandlas med samma varsamhet som i
  befintliga set (Muhammed avbildas aldrig; Jesus utan tydligt ansikte).
- Erövring och kolonisation skildras ärligt med båda perspektiven, som i
  korstågs- och Djingis-seten.

## Ämnesnoter, leverans 4

- **Joan of Arc**: rösterna och synerna återges som hennes utsaga och samtidens
  tro, inte som fakta. Rättegång och avrättning sakligt och lugnt, inga
  bålmotiv i bilderna. Lyft källrikedomen (rättegångsprotokollen) på
  universitetskortet.
- **The Renaissance**: inte myten att renässansen "börjar 1453". Handelsstäder
  i Italien, återupptäckta antika texter, perspektivmåleri, tryckpressen som
  spridare. Kategori `renaissance`.
- **Leonardo da Vinci**: bredden (konst, anatomi, ingenjörskonst),
  anteckningsböckerna och spegelskriften som motiv utan läsbara bokstäver.
- **Johannes Gutenberg**: Kina och Korea trycker med lösa typer tidigare;
  Gutenbergs bidrag är det billiga, skalbara systemet i Europa. Inga läsbara
  bokstäver i bildmotiven (typer på avstånd, i vinkel, ur fokus).
- **Christopher Columbus**: ärlig balans utan hjältenarrativ: felräkningen av
  jordens storlek, att han aldrig förstår att det är en för Europa okänd
  kontinent, mötets följder för urfolken (sjukdomar, kolonisation) sakligt
  skildrade. Skriv för elever i Latinamerika.

## Ämnesnoter, leverans 5

Kategorier: Magellan `exploration`; Kopernikus och Galilei `science`;
reformationen och Luther `religions` (etiketten `reformation` vore lika med
reformationssetets svar, samma krock som renässansen). Korsläckor att vakta:
reformationssetet får inte namnge Luther ("a monk in Germany" räcker),
Luthersetet får inte använda ordet Reformation, Galileisetet får inte namnge
Kopernikus ("an astronomer from the north" eller liknande), Magellansetet
inte Columbus.

- **Ferdinand Magellan**: han dör på Filippinerna (Mactan, Lapulapu) och
  fullbordar inte resan själv; Elcano för ett skepp hem, 18 man av cirka 270.
  Ge det filippinska perspektivet plats. Nämn Enrique, hans tolk från
  Malacka, som möjligen var den förste som verkligen kom runt jorden.
  Sundet, Stilla havets storlek, skörbjugg sakligt utan gore.
- **Nicolaus Copernicus**: han bevisar inte heliocentrismen, han föreslår
  och räknar; boken trycks 1543 när han dör; Aristarchos tänkte tanken i
  antiken; matematiska verktyg från islamiska astronomer (Maragha) får
  nämnas på universitetsnivå; kyrkans reaktion kom först decennier senare,
  inte mot honom personligen.
- **Galileo Galilei**: kikaren förbättras, uppfinns inte av honom; Jupiters
  månar, Venus faser, månens berg; rättegången 1633 slutar i husarrest,
  ingen tortyr, inget bål (Bruno är en annan person, blanda inte ihop);
  "och ändå rör hon sig" är en senare legend och ska markeras som sådan.
  Undvik den förenklade bilden "kyrkan mot vetenskapen", visa att
  många av hans motståndare var andra lärde.
- **The Protestant Reformation**: inte bara en man: avlaten, tryckpressen,
  furstarnas intressen, Zwingli, Calvin, den katolska motreformationen.
  Kyrkodörrslegenden bara som "a story tells". Trosfrågor markeras som tro
  på alla sidor; ingen sida framställs som den rätta (Rogers regel). Krigen
  som följde sakligt och kort.
- **Martin Luther**: munken, ångesten, avlatsbreven, de 95 punkterna,
  riksdagen i Worms ("här står jag" är osäkert citat, markera), bibeln på
  tyska och vad det gör med språket och läsandet. Universitetskortet får
  kort och sakligt nämna att hans sena skrifter mot judar är en mörk del av
  arvet som historiker studerar. Inga porträtt av honom som svarsläcka:
  bildmotiv utan igenkännbart Cranach-ansikte.

## Ämnesnoter, leverans 6

Kategorier: amerikanska revolutionen, Washington, franska revolutionen,
Napoleon och industriella revolutionen `revolutions` (etiketten "revolutioner"
pekar inte ut vilken revolution som är svaret, alla alternativ är revolutioner
eller personer); Darwin `science`; Marx `ideas` (svensk etikett "idéhistoria").

Korsläckor att vakta: amerikanska revolutionen-setet får inte namnge
Washington ("a general from Virginia" räcker); Washington-setet får inte
använda frasen "American Revolution" (beskriv: "thirteen colonies fight to
leave the British king", högst en kontextrad, återberätta inte skatte- och
tekedjan). Franska revolutionen-setet får inte namnge Napoleon ("a young
general takes power"); Napoleon-setet får kalla det "the revolution in France"
i en kontextrad men inte återberätta revolutionens ledtrådskedja (Bastiljen,
brödpriserna, kungens avrättning). Industriella revolutionen-setet får inte
namnge Marx eller Darwin; Marx-setet får inte använda frasen "Industrial
Revolution" (skriv "the new factories", "the machines"). Inget set i
leveransen namnger personer eller skeenden på rad 40-50 (världskrigen,
Churchill, Hitler, kalla kriget, FN); skriv "a later war in Europe", "later
states in Russia and China" och liknande.

- **The American Revolution**: Revolution X, frågan "Which revolution is
  Revolution X?". Tretton kolonier vid Atlantkusten, skatter efter det dyra
  kriget mot Frankrike, "no taxation without representation", teet i
  hamnen i Boston, kriget börjar 1775, förklaringen 1776 med "all men are
  created equal" samtidigt som ungefär en femtedel av befolkningen är
  förslavad; lojalister, urfolkens nationer som mest står på Storbritanniens
  sida, Frankrikes ingripande som avgör kriget, freden 1783, konstitutionen.
  Inget hjältenarrativ, skriv för elever i Tanzania och Bhutan. Universitet:
  hur revolutionär var revolutionen, och ekot i Latinamerika (Bolívar).
  Inga flaggor med läsbara stjärnor eller dokument med läsbar text i bild.
- **George Washington**: plantageägare i Virginia, lantmätare som ung, officer
  i kriget mot Frankrike, befälhavare 1775, förlorar många slag men håller
  armén samman, vintern i Valley Forge, floden Delaware julnatten 1776,
  Yorktown med fransk hjälp, lämnar tillbaka befälet, första presidenten
  1789, avböjer att bli kung, avgår efter två perioder. Han äger över 300
  förslavade människor på Mount Vernon; de han själv äger frias i hans
  testamente, först efter hustruns död; Ona Judge flyr. Körsbärsträdet är
  en senare uppfinning, markera som saga. Huvudstaden med hans namn är en
  tillåten namnekoledtråd.
- **The French Revolution**: Revolution X. Brödpriser efter missväxt, statens
  skulder, tre stånd, ständerna 1789, nationalförsamlingen, Bastiljen 14
  juli (ett fängelse med sju fångar), förklaringen om människans rättigheter,
  kvinnornas marsch till Versailles, kungen avrättas 1793 sakligt utan gore
  och utan giljotin i bild, skräckväldet med tiotusentals döda, Robespierre,
  Olympe de Gouges, slaveriet avskaffas 1794 efter resningen på
  Saint-Domingue, metersystemet, "frihet, jämlikhet, broderskap".
  Universitet: tolkningsstriden (klasskamp kontra revisionister) och
  Haitis revolution som spegel.
- **Napoleon Bonaparte**: född på Korsika året efter att ön blivit fransk,
  artilleriofficer, revolutionen öppnar karriärer för begåvning, general vid
  24, Egypten med forskare (stenen med tre skrifter får nämnas men aldrig
  visas läsbar), statskuppen 1799, lagboken 1804 som präglar lagar i många
  länder än i dag, sätter själv kronan på sitt huvud, återinför slaveriet i
  kolonierna 1802 och förlorar Haiti, säljer Louisiana, Trafalgar,
  Austerlitz, Ryssland 1812 där de flesta aldrig kommer hem, Elba, de hundra
  dagarna, Waterloo, Sankt Helena. Myten att han var kort markeras som myt.
  Bilder: aldrig tvåkornshatten, handen i västen eller ett igenkännbart
  porträtt, det är svarsläckor.
- **The Industrial Revolution**: Revolution X. Storbritannien från slutet av
  1700-talet: kol, järn, ångmaskinen som förbättras, inte uppfinns, av Watt,
  spinnmaskinerna, fabrikerna i Manchester, kanaler och järnvägar, ångfartyg.
  De 99 procenten: tolv till fjorton timmars dagar, barn i gruvor och
  spinnerier, fabrikslagarna, fackföreningar, rök och kolera i städerna.
  Varför Storbritannien: kol, kapital, kolonier, marknader. Globalt: bomull
  från förslavade i USA och från Indien, Indiens vävare förlorar,
  spridningen till Belgien, Tyskland, USA och Japan, kolutsläppen som börjar
  då. Universitet: "revolution eller långsam utveckling" och debatten om den
  stora divergensen. Inga läsbara skyltar på fabriker eller lok.
- **Charles Darwin**: medicin i Edinburgh som han avskyr, präststudier i
  Cambridge, skalbaggssamlare, fem år på Beagle, sjösjuk, fossil och
  jordbävning i Sydamerika, Galápagos med sköldpaddor och härmtrastar;
  finkarna är delvis en senare rekonstruktion och ska inte bära berättelsen.
  Duvuppfödning, trädskissen 1837, tjugo års väntan, brevet från Wallace
  1858, boken 1859, debatten 1860 återges olika av samtida, markera.
  Religiös känslighet: många troende ser ingen konflikt, andra gör det,
  skriv som vetenskapshistoria. Universitet: Wallace och prioriteten, hur
  idéerna missbrukas för rasism och "socialdarwinism", markerat som missbruk.
  Bilder: inget igenkännbart skäggigt ålderdomsporträtt.
- **Karl Marx**: född i Trier, jurist- och filosofistudier, journalist vars
  tidning stängs, exil i Paris, Bryssel och London, Jenny von Westphalen,
  fattigdomen i Soho där barn dör, Engels som fabrikörsson försörjer honom,
  manifestet 1848, läsesalen i British Museum, Kapitalet 1867, idéerna:
  historien drivs av strider mellan klasser, arbetarna skapar värdet och
  ägarna behåller överskottet, kriserna. Elva personer på begravningen.
  Universitet: stater som senare tar hans namn, deras våld och svält som
  han aldrig såg, skillnaden mellan Marx och "marxismen", det rapporterade
  citatet "jag är ingen marxist" markerat som återgivet av Engels.
  Balanserat som idéhistoria för klassrum på fyra kontinenter. Bilder: inget
  igenkännbart porträtt, inga hammare-och-skära-symboler, inga röda fanor
  med text.
