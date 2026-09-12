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
- Ange huvudpersonens och folkmängdens hudfärg uttryckligen när den bär
  historien ("a Black South African man seen from behind", "Black and white
  spectators"). Utan det ritar bildmodellen vita figurer; i leverans 8 föll
  två Mandelabilder på detta.

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

## Ämnesnoter, leverans 7

Kategori för alla sex set: `twentieth century` (svensk etikett "1900-talet").
Etiketten trycks på kortet, så alla distraktorer måste också höra hemma på
1900-talet (Koreakriget, Vietnamkriget, spanska inbördeskriget, Stalin,
Mussolini, Franco, Nehru, Jinnah, Nationernas förbund, Röda korset, Nato).

Korsläckor att vakta: världskrigsseten namnger inte Hitler eller Churchill
("a dictator in Germany", "the British prime minister" räcker); Hitlersetet
och Churchillsetet får inte skriva "World War II", skriv "the great war that
follows", "the war in Europe" i högst en kontextrad; Gandhisetet namnger inte
Martin Luther King eller Mandela (rad 47-48); FN-setet namnger inte kalla
kriget (rad 46), skriv "the long rivalry between two great powers". Inget set
namnger Berlinmuren, kalla kriget, Mandela eller månlandningen.

Känslighet: detta är den känsligaste leveransen hittills. Inga hakkors, inga
nazistiska eller fascistiska symboler, inga porträtt av Hitler, ingen
Hitlerhälsning, inga uniformsdetaljer som fungerar som symboler, inga bilder
från lägren med offer, ingen svampmolnsestetik. Förintelsen berättas
sakligt, lugnt och utan gore, med människorna i centrum, aldrig förövarens
perspektiv som spännande. Krig berättas från de 99 procentens sida:
soldater från Afrika, Indien och Karibien, kvinnorna i fabrikerna, barnen
som evakueras, hungern. Balans för klassrum i Asien och Afrika: Churchills
imperiesyn och svälten i Bengalen 1943, Gandhis år i Sydafrika och kritiken
från Ambedkar, kolonialtruppernas insats i bägge världskrigen, FN:s
misslyckanden lika sakligt som dess framgångar.

- **World War I**: War X, frågan "Which war is War X?". Alliansernas
  Europa, skottet i Sarajevo 1914 som gnista, inte orsak; skyttegravarna,
  kulsprutan och gasen sakligt; soldater från Indien, Senegal, Australien,
  Kanada; Osmanska rikets fall och Mellanösterns nya gränser; hemmafronten
  och kvinnornas arbete; ryska revolutionen 1917 får nämnas som följd;
  freden i Versailles och skulden; spanska sjukan 1918-1920 som dödar fler
  än kriget. Universitet: orsaksdebatten (Fischer, "sömngångarna"),
  källorna (brev, dagböcker, censur). Cirka 9-10 miljoner stupade soldater,
  skriv "about ten million soldiers".
- **World War II**: War X. Börjar 1939 i Europa, i Asien redan 1937 med
  Japans krig i Kina; blixtkrig, Stalingrad, ökenkriget, Stilla havet,
  Normandie; Förintelsen: sex miljoner judar mördas, också romer, funktions-
  nedsatta och andra, sakligt utan gore; barnen som evakueras, ransoneringen;
  atombomberna över Hiroshima och Nagasaki sakligt, med offren i centrum;
  soldater och arbetare från Afrika, Indien, Karibien och Latinamerika;
  cirka 60-70 miljoner döda, de flesta civila, skriv "more than sixty
  million people, most of them civilians". Universitet: hur vet vi detta,
  rättegångarna i Nürnberg, minneskulturen, debatten om bomberna.
- **Winston Churchill**: Mr X. Skolpojken som är dålig i skolan, soldaten
  och journalisten i Sudan och Sydafrika, flykten från boernas fångläger,
  ministern som misslyckas vid Gallipoli 1915, "vildmarksåren", talen 1940
  ("we shall fight on the beaches" är dokumenterat, får citeras kort som
  återgivet), valförlusten 1945 mitt i segern, Nobelpriset i litteratur
  1953, målandet. Balans: hans syn på imperiet och på indier, svälten i
  Bengalen 1943 med omkring tre miljoner döda där hans regering nekade
  hjälp, sakligt återgivet på gymnasie- eller universitetsnivå. Inga
  igenkännbara porträtt: ingen cigarr, ingen V-gest, ingen plommonstop
  som svarsläcka.
- **Adolf Hitler**: Mr X. Syftet med setet är att förklara hur en
  demokrati kan förstöras, inte att berätta om en person med fascination.
  Den misslyckade konstnären i Wien, soldaten 1914-1918, kuppförsöket 1923
  och fängelset, boken, partiet som växer i den ekonomiska krisen efter
  1929, valen där partiet aldrig får egen majoritet, utnämningen till
  rikskansler 1933 av presidenten, riksdagsbranden och lagarna som
  avskaffar demokratin på några månader, propagandan, judeförföljelsen från
  bojkott 1933 till Nürnberglagarna 1935 och novemberpogromen 1938, kriget
  och Förintelsen som han beordrar, självmordet 1945. Nivå åk 6: hur ett
  land tappar sin frihet steg för steg, utan skräckbilder. Universitet: hur
  historiker förklarar stödet (Kershaw "working towards the Führer"),
  källorna, ansvarsfrågan, förnekelsens historia. Bilder: aldrig hans
  ansikte, aldrig symboler, aldrig massmöten med hälsningar; motiv som
  tomma gator, stängda tidningar, brända böcker på avstånd utan läsbar
  text, en stängd skoldörr, resväskor.
- **Mahatma Gandhi**: Mr X. Barndomen i Gujarat, juridiken i London,
  tjugoett år i Sydafrika där han möter rasismen och utvecklar satyagraha
  (kort och sakligt: hans tidiga uttalanden om afrikaner var fördomsfulla,
  får nämnas på universitetsnivå), hemkomsten 1915, saltmarschen 1930,
  spinnrocken och hemvävt tyg, fängelseåren, fastorna, Ambedkars kritik i
  kastfrågan, självständigheten 1947 och delningen med hundratusentals
  döda som han sörjer, mordet 1948 av en hindunationalist. Tro markeras
  som tro. Inga porträtt med de runda glasögonen som svarsläcka, inga
  läsbara texter. "Mahatma" är en hederstitel och får inte förekomma i
  texten, inte heller "Bapu".
- **The United Nations**: Organization X, frågan "Which organization is
  Organization X?". Bildas 1945 efter kriget, stadgan i San Francisco,
  51 länder från början, i dag 193; Nationernas förbund som misslyckad
  föregångare; generalförsamlingen där varje land har en röst,
  säkerhetsrådet med fem permanenta medlemmar och veto; den allmänna
  förklaringen om de mänskliga rättigheterna 1948 med Eleanor Roosevelt
  och Peng Chun Chang; avkoloniseringen som fyller församlingen med nya
  stater; fredsbevarande styrkor med blå hjälmar; barnfonden och
  matprogrammet; misslyckandena i Rwanda 1994 och Srebrenica 1995
  sakligt; högkvarteret i New York på mark skänkt av Rockefeller.
  Universitet: vetots historia och reformdebatten. Bilder: inga flaggor
  eller emblem med läsbar form, inga blå hjälmar med bokstäver; svenska
  läckor att vakta i översättningen: FN, Förenta nationerna.

## Ämnesnoter, leverans 8

Kategori för alla fem set: `twentieth century`. Distraktorer ur 1900-talet.

Korsläckor att vakta: kalla kriget-setet får inte skriva "Berlin Wall" eller
namnge månlandningen ("the two powers race into space" räcker), inte
Mandela eller King; Kingsetet namnger inte Gandhi ("a leader in India who
fights without weapons"), inte Mandela; Mandelasetet namnger inte King
eller Gandhi; Berlinmursetet får inte skriva "Cold War" (skriv "the long
rivalry between two great powers") och inte namnge Mandela; månlandnings-
setet får inte skriva "Cold War". Inget set skriver "World War", Hitler,
Churchill eller FN vid namn.

- **The Cold War**: Conflict X, frågan "Which conflict is Conflict X?".
  Två stormakter efter 1945 som aldrig krigar direkt mot varandra men
  hotar med kärnvapen, delar Europa med en järnridå, för krig genom
  andra i Korea, Vietnam, Afghanistan, Angola och Latinamerika; rymd-
  kapplöpningen utan att namnge månlandningen; Kubakrisen 1962 sakligt
  (får inte vara distraktor på det kort som berättar den); de alliansfria
  staterna i Bandung 1955 och vad rivaliteten kostade Afrika, Asien och
  Latinamerika; slutet omkring 1989-1991. Universitet: vem bär skulden,
  ortodoxa, revisionister och postrevisionister, arkiven som öppnades
  efter 1991. Undvik orden "cold" och "Cold War" helt i elevvänd text.
- **Martin Luther King Jr.**: Mr X. Pastorssonen i Atlanta, bussbojkotten
  i Montgomery 1955-1956 som Rosa Parks utlöser, ickevåld lärt av en
  ledare i Indien (namnges inte), marschen till Washington 1963 med
  "I have a dream" (dokumenterat, får citeras kort), Birmingham och
  brevet från fängelset, rösträttslagen 1965, Selma, kritiken från
  Malcolm X och de yngre, hans kritik av Vietnamkriget och fattigdomen,
  mordet i Memphis 1968. Fångar: "king", "King", "Luther" och "Martin"
  används inte i elevvänd text; reformatorn med samma namn nämns inte.
  Bilder: inga igenkännbara porträtt, inga läsbara plakat, marschen
  bakifrån.
- **Nelson Mandela**: Mr X. Pojken i Transkei, juriststudenten, apartheid-
  lagarna, ANC, Sharpeville 1960, den väpnade grenen som han grundar
  1961 sakligt utan förskönande, Rivoniarättegången 1964 och talet om
  idealet han är beredd att dö för, 27 år i fängelse varav 18 på Robben
  Island med kalkbrottet, frigivningen 1990, förhandlingarna, valet
  1994, sannings- och försoningskommissionen, en enda mandatperiod.
  Kritiken: våldet på 1980-talet i rörelsen, ekonomin efter 1994.
  Tro markeras som tro. Fångar: "Mandela", "Madiba", "Rolihlahla",
  "Nelson". Bilder: inga porträtt, inga flaggor, kalkbrottet, en cell,
  en valkö 1994 bakifrån.
- **The fall of the Berlin Wall**: Event X, frågan "Which event is Event
  X?". Staden delad sedan 1961, muren byggd på en natt, minst 140 döda
  vid försök att ta sig över, den hemliga polisen, hösten 1989: Ungern
  öppnar gränsen, måndagsdemonstrationerna i Leipzig, presskonferensen
  9 november där en talesman läser fel om resetillstånd, folkmassorna,
  gränsvakterna som öppnar, hammare och mejsel, återföreningen 1990.
  Orden "Berlin" och "wall" får användas som ledtrådar men aldrig
  frasen "Berlin Wall" och inte "fall of the"; skriv "the wall opens",
  "the wall comes down". Bilder: inga läsbara klotter, inga flaggor.
- **The first Moon landing**: Event X. Rymdkapplöpningen med den andra
  stormaktens försprång (första satelliten 1957, första människan 1961),
  det stora programmet med 400 000 människor inklusive räknarna, tre
  män i juli 1969, fyra dagar dit, två går på ytan, "a small step"
  (dokumenterat citat), 600 miljoner tittar, stenarna hem, kostnaden och
  kritiken i USA under fattigdom och krig, de senare landningarna, myten
  att det var iscensatt behandlas på universitetskortet som studerat
  fenomen. Fångar: "landing", "Moon landing"; ordet "Moon" är en tillåten
  ledtråd. Bilder: inga flaggor, inga läsbara texter på dräkter eller
  landare, jorden över horisonten.

## Ämnesnoter, leverans 9

Första leveransen ur den utökade listan (`docs/forslag-utokad-lista.md`),
vetenskapsblockets femkortsämnen: rad 51 Newton, 52 Einstein, 53 Marie
Curie, 54 Pasteur, 59 Turing, 79 Florence Nightingale. Kategori för alla
sex set: `science` (etiketten finns redan, jämför Kopernikus, Galilei,
Darwin). Distraktorer ur vetenskapshistorien, gärna kvinnor och forskare
utanför Europa: Galileo Galilei, Nicolaus Copernicus, Johannes Kepler,
Charles Darwin, Michael Faraday, James Clerk Maxwell, Niels Bohr, Max
Planck, Ernest Rutherford, Lise Meitner, Rosalind Franklin, Robert Koch,
Edward Jenner, Joseph Lister, Alexander Fleming, Ignaz Semmelweis, Mary
Seacole, Elizabeth Blackwell, Clara Barton, Charles Babbage, Ada Lovelace,
Grace Hopper, John von Neumann, Claude Shannon, Gottfried Leibniz, Robert
Hooke, Edmond Halley, Chien-Shiung Wu, C. V. Raman, Hideki Yukawa, Abdus
Salam. Sedan 2026-09-12 får ett annat sets svar stå som distraktor, men
löptexten namnger fortfarande inte andra sets svar.

Korsläckor att vakta: inget av de sex seten namnger något av de andra
fem i elevvänd text. Einsteinsetet skriver "the laws of motion from two
hundred years earlier", inte Newton. Inget set namnger Galilei, Kopernikus,
Darwin, Hitler eller Churchill i löptexten, och skriver inte "World War I"
eller "World War II" som egennamn; "the war", "a world war", "the great war
that begins in 1939" räcker. Nobelpriset får nämnas fritt, det är inget set.

Anonymisering: Mr X för männen, Miss X för Nightingale, Mrs X för Curie
(svenska: fru X). Frågan alltid "Who is Mr X?" respektive "Who is Miss X?",
"Who is Mrs X?".

- **Isaac Newton**: Mr X. Född i en by i England 1642 enligt dåtidens
  kalender, fadern död före födseln, pestens år 1665-1666 hemma på gården
  då de stora idéerna föds, prismat som visar att vitt ljus består av
  alla färger, spegelteleskopet 1668, de tre rörelselagarna och den
  allmänna gravitationen i boken 1687, samma kraft som får äpplet att falla
  håller månen i sin bana. Äpplet är en berättelse han själv spred på
  ålderns höst, skriv "a story says". Striden med Leibniz om vem som
  uppfann den nya matematiken, alkemin och teologin han ägnade lika mycket
  tid åt, chefen för myntverket som jagade falskmyntare, "standing on the
  shoulders of giants" i brevet 1675, begravd i Westminster Abbey.
  Universitet: hur mycket han byggde på andra, alkemin, den svåra
  personligheten. Fångar: "Newton", "Newtonian", "newton", "Isaac".
  Bilder: 1600-talets England, peruker, ljus och prisma, inga läsbara
  boksidor, inga formler.
- **Albert Einstein**: Mr X. Född i Ulm 1879, sen att tala enligt
  familjelegenden, kompassen som barn, patentkontoret i Bern, underåret
  1905 med fyra artiklar: ljuset som partiklar, molekylernas dans i vatten,
  den speciella relativiteten, massa och energi som samma sak. Allmänna
  relativiteten 1915, solförmörkelsen 1919 som visade att ljus böjs vid
  solen och gjorde honom världsberömd, Nobelpriset för ljuset som partiklar,
  inte för relativiteten. Lämnar Tyskland 1933 när diktatorn tar makten,
  Princeton, brevet till presidenten 1939 om att en bomb var möjlig, ångern
  efteråt och fredsarbetet, tackade nej till att bli Israels president 1952.
  Universitet: vad relativiteten ändrade, kvantfysiken han aldrig
  accepterade, brevet och ansvaret. Formeln skrivs aldrig ut med bokstäver,
  beskriv den med ord. Fångar: "Einstein", "Albert", "Einsteinian";
  "relativity" är en tillåten ledtråd. Bilder: inga porträtt med det kända
  håret, inga tavlor med formler, inga läsbara papper.
- **Marie Curie**: Mrs X. Född i Warszawa 1867 under ryskt styre, flickor
  fick inte läsa vid universitetet, det hemliga "flygande universitetet",
  guvernant i omkring fem år 1885-1890 för att betala systerns studier, Paris 1891, bäst i
  klassen i fysik, gifter sig 1895 med en fysiker (skriv "her husband",
  aldrig hans namn), två nya grundämnen 1898 varav ett uppkallat efter
  hemlandet, tonvis med malm kokad i ett skjul, första kvinnan att få
  Nobelpriset 1903, maken dör i en olycka 1906, första kvinnliga
  professorn vid Sorbonne, andra Nobelpriset 1911 som första människa med
  två, röntgenbilar vid fronten 1914-1918 med dottern (skriv "her
  daughter"), dör 1934 av sjukdom från strålningen, anteckningsböckerna
  strålar än, Panthéon 1995. Universitet: hur priset 1903 först bara skulle
  gå till männen, pressen 1911, strålningens pris. Fångar: "Curie",
  "curie", "Marie", "Maria", "Skłodowska", "Pierre", "Irène". Bilder:
  1890-talets Paris, skjulet, glödande glas i mörker, inga etiketter.
- **Louis Pasteur**: Mr X. Kemist från östra Frankrike, kristallerna 1848,
  jäsning orsakas av levande mikrober, svanhalskolven 1859-1861 som
  avgjorde att liv inte uppstår av sig självt i buljong, silkesmaskarnas
  sjukdom 1865, uppvärmningen som gör vin och öl hållbar, mjölken kom senare genom andra (skriv
  "gentle heating kills the germs", ordet för processen är förbjudet),
  hönskoleran 1879 där försvagade odlingar gav idén om försvagade smittämnen, berättelsen om den glömda odlingen över sommaren är en anekdot och skrivs "a story says",
  mjältbrandsvaccinet 1881 på fåren i Pouilly-le-Fort, rabiesvaccinet 1885
  på pojken Joseph Meister, institutet i Paris 1888, tre döttrar döda som barn, minst två i tyfus, slaganfallet 1868, rivalen i Berlin (Robert Koch, får namnges,
  är inget set). Universitet: anteckningsböckerna som visade att han ibland
  förskönade sina resultat, etiken kring Meister, striden med Koch.
  Fångar: "Pasteur", "pasteur", "Louis", alla former av "pasteuriz".
  Svenska: "pastör" i alla former förbjudet. Bilder: 1800-talets
  laboratorium, glaskolvar, får, inga etiketter eller skyltar.
- **Alan Turing**: Mr X. Skolpojken som sprang milsvitt, vännen som dog
  1930, Cambridge, artikeln 1936 om en tänkt maskin som kan räkna allt som
  går att räkna, datorns idé före datorn, Princeton, Bletchley Park från
  1939, den tyska kodmaskinen Enigma, bomben, den elektromekaniska maskinen
  som sökte inställningar, byggde vidare på polska matematikers arbete
  före kriget (måste nämnas), ubåtskriget i Atlanten, hemligheten som
  hölls i trettio år, datorn i Manchester 1948, artikeln 1950 om huruvida
  maskiner kan tänka och spelet där en domare inte ska kunna skilja
  människa från maskin, mönstren i naturen 1952. Döms 1952 enligt dåtidens
  lag för sitt privatliv, förlorar sitt säkerhetstillstånd, dör 1954 av
  cyanid, dödsorsaken bedömdes som självmord, regeringens ursäkt 2009 och
  benådningen 2013. Känslighet: kort 1 och 2 utelämnar domen helt; kort
  3-5 nämner den i en eller två neutrala meningar, "a law of that time
  punishes him for loving another man", ingen medicinsk detalj, ingen
  moralisering, ursäkten och benådningen nämns alltid i samma andetag.
  Klassrummen finns i Tanzania och Bhutan; lyft formuleringen till Jonas.
  Fångar: "Turing", "Alan". Premiärministern namnges inte. Bilder: 1940-
  talets maskiner utan läsbara paneler, inga sedlar, inga porträtt.
- **Florence Nightingale**: Miss X. Född 1820 i en italiensk stad hon
  fick sitt namn efter (staden namnges inte), rik engelsk familj, säger
  sig ha hört ett kall (tro markeras som tro), familjen emot, utbildning
  vid ett sjukhus i Tyskland, Krimkriget 1854 med 38 sjuksköterskor till
  militärsjukhuset i Scutari vid Konstantinopel, smutsen, dödligheten i
  sjukdom större än i sår, nattronden med lampan (motivet får användas
  men inte som fast epitet med stor bokstav), dödligheten föll framför
  allt efter att en sanitetskommission 1855 rensade avlopp (historikerna
  är ense om det), hem 1856 som nationalhjälte, diagrammen som visade
  varför soldaterna dog, första kvinnan i det statistiska sällskapet 1858,
  boken om sjukvård 1859, sjuksköterskeskolan i London 1860, sängliggande
  i årtionden av en sjukdom från Krim, rådgivare om Indiens sanitet, Order
  of Merit 1907 som första kvinna. Balans: Mary Seacole från Jamaica, som
  vårdade soldater i samma krig och nekades plats i gruppen, får nämnas
  och är bra distraktor. Fångar: "Nightingale", "nightingale", "Florence",
  "Lady with the Lamp". Bilder: 1850-talets sjukhussal, lampa, inga
  läsbara diagram, ingen gore.

## Ämnesnoter, leverans 10

Andra leveransen ur den utökade listan, i förslagets ordning bland
femkortsämnena: rad 61 Arkimedes, 62 al-Khwarizmi, 71 Ibn Sina, 72 Visdomens
hus i Bagdad, 74 Ibn Battuta, 76 Upplysningen. Kategorier: `mathematics`
(ny etikett, svenska "matematik") för Arkimedes och al-Khwarizmi, `ideas` för
Ibn Sina, Visdomens hus och Upplysningen, `exploration` för Ibn Battuta.
Bilder produceras när bildtjänstens krediter är påfyllda; briefer skrivs
ändå färdiga nu.

Islamisk guldålder, bindande för fyra av seten: Muhammed avbildas aldrig
och namnges inte i löptexten (skriv "the Prophet's city" bara om det
behövs, hellre "Mecca" och "the pilgrimage"). Ingen arabisk kalligrafi i
någon bild, inte heller pseudokalligrafi eller skriftband på väggar och
tyger; manuskript visas stängda, på avstånd eller i sådan vinkel att inga
tecken syns; astrolabier och instrument utan gravyr; geometriska
mönster är tillåtna. Tro markeras som tro. Koranen får nämnas som bok
("the holy book of Islam"). Kaba och böneplatser avbildas inte; visa
karavaner, hamnar, gårdar, bibliotek utan synlig text.

Korsläckor att vakta: inget av de sex seten namnger något av de andra fem.
Al-Khwarizmisetet och Ibn Sina-setet skriver "a great library in Baghdad"
respektive ingenting om Bagdadhuset; Bagdadsetet skriver "a young
mathematician from the east" utan namn. Aristoteles, Platon, Sokrates,
Alexander, Julius Caesar, Kopernikus, Galilei, Newton, Columbus, Magellan,
Djingis khan, digerdöden, renässansen, reformationen, amerikanska och
franska revolutionen, Washington och Napoleon namnges inte i löptexten
(alla är set); skriv "an ancient Greek philosopher", "an English scientist's
laws", "the revolutions in North America and France", "a great plague",
"the army from the steppes". Orden "Greek", "Roman", "Mongol" som adjektiv
är tillåtna eftersom de inte är något sets svar. Alexandria, Baghdad,
Mecca, Tangier, Syracuse, Paris är avsiktliga ledtrådar och får nämnas.

Anonymisering: Mr X för personerna; Visdomens hus är Place X med frågan
"Which place is Place X?" (svenska "platsen X", "Vilken plats är platsen
X?"); Upplysningen är Movement X med frågan "Which movement is Movement X?"
(svenska "rörelsen X").

- **Archimedes**: Mr X. Grekisk matematiker i Syrakusa på Sicilien, född
  omkring 287 f.Kr., troligen studier i Alexandria, hävstången ("give me a
  place to stand" är ett senare citat, skriv "a story says"), badkaret och
  kronan är en berättelse från Vitruvius två sekler senare (skriv "a famous
  story says", ropet i badet nämns inte med ordet), vattenskruven för
  bevattning, pi inringat mellan två bråk med månghörningar, klotets volym
  som två tredjedelar av cylindern och att han ville ha figuren på sin
  gravsten (Cicero fann graven 75 f.Kr.), Sandräknaren med enorma tal,
  krigsmaskinerna under romarnas belägring 214-212 f.Kr. (brännspeglarna
  är en sen legend, utelämna eller markera), dödad av en romersk soldat när
  staden föll trots order att skona honom ("do not disturb my circles" är
  en senare berättelse), palimpsesten: en avskrift från 900-talet skrapades
  och överskrevs med en bönbok på 1200-talet, hittades 1906 och lästes med
  modern bildteknik 1998-2008 och avslöjade Metoden. Universitet: vad som
  är dokumenterat och vad som är legend, metoden som föregrep integralen.
  Fångar: "Archimedes", "Archimedean", "Eureka", "Archimedes' screw" (skriv
  "the water screw"). Distraktorer: Euclid, Pythagoras, Eratosthenes, Hero
  of Alexandria, Thales, Hipparchus, Apollonius, Hypatia, Ptolemy. Bilder:
  antik hamnstad, skruv i flod, badkar utan person, geometriska figurer i
  sand utan bokstäver, inga togor med text, inga sköldar med emblem.
- **al-Khwarizmi**: Mr X. Persisk lärd i Bagdad omkring 780-850 under
  kalifen al-Ma'mun (får namnges), arbetade vid det stora biblioteket
  (namnges inte), boken om "restoring and balancing" som gav Europa ordet
  algebra (ordet "algebra" är en tillåten ledtråd, det kommer från
  boktiteln, inte från hans namn), lösning av andragradsekvationer i ord
  och figurer utan symboler, boken om de indiska siffrorna med nollan som
  spreds till Europa via latinska översättningar på 1100-talet, hans
  latiniserade namn gav ordet för en steg-för-steg-regel (ordet
  "algorithm" är förbjudet, liksom "Algoritmi"), astronomiska tabeller,
  geografiboken med förbättrad världskarta, namnet kommer från en region i
  Centralasien (namnges inte, "Khwarazm" förbjudet, skriv "a region east of
  the Caspian Sea"). Universitet: vad som är hans eget och vad som är arv
  från Indien och Grekland, hur sifferboken överlevde bara på latin.
  Fångar: "Khwarizmi", "Khwarazm", "Algoritmi", "algorithm", "algorithmic".
  Distraktorer: Omar Khayyam, al-Kindi, al-Biruni, Ibn al-Haytham,
  Fibonacci, Brahmagupta, Thabit ibn Qurra, al-Battani, Nasir al-Din
  al-Tusi. Bilder: räknebräde med stenar, karavan, observatorium, kartor
  utan text, inga siffror i bild.
- **Ibn Sina**: Mr X. Född 980 nära Buchara i dagens Uzbekistan, persisk,
  enligt sin egen självbiografi kunde han den heliga boken utantill vid tio
  år (skriv "he says"), läkare vid sexton eller arton, botade emiren och
  fick tillgång till palatsbiblioteket, den stora medicinboken i fem delar
  ("Canon" får nämnas som boktitel, hellre "his great book of medicine")
  som användes vid Europas universitet in på 1600-talet, boken om
  helandet med filosofi och naturvetenskap, tankeexperimentet med den
  svävande människan, tanken att sjukdomar sprids av något osynligt i vatten
  och luft (skriv försiktigt, inte "bakterier"), byggde på en antik grekisk
  filosof (namnges inte), vandrade mellan hov i Hamadan och Isfahan, var
  vesir, satt kort i fängelse, dog 1037 i Hamadan. Universitet: hans
  metafysik och Europa, striden med senare teologer, myten om det totala
  minnet. Fångar: "Sina", "Avicenna", "Avicennian". Distraktorer: al-Razi,
  Ibn Rushd, al-Biruni, Ibn al-Haytham, Maimonides, al-Farabi, al-Zahrawi,
  Hippocrates, Galen. Bilder: 1000-talets Centralasien, apotek med krukor
  utan etiketter, palatsbibliotek med stängda böcker, karavanväg.
- **The House of Wisdom in Baghdad**: Place X. Bagdad grundat 762 som rund
  stad av kalifen al-Mansur, världens största stad omkring år 800,
  översättningsrörelsen på 700-900-talen: grekiska, persiska och indiska
  verk till arabiska, Hunayn ibn Ishaq som chefsöversättare (berättelsen
  att han fick böckernas vikt i guld är en legend, skriv "a story says"),
  papperet från Kina (legenden om kinesiska fångar efter slaget vid Talas
  751 markeras som berättelse; pappersbruk i Bagdad omkring 794),
  kalifen al-Ma'mun som beskyddare, astronomer som mätte jordens omkrets,
  bröderna Banu Musa och deras maskiner, en ung matematiker från öster
  (namnges inte), arvet till Europa via översättningar i Toledo och på
  Sicilien på 1100-talet, staden plundrad 1258 av armén från stäpperna
  (ledaren namnges inte, berättelsen om floden svart av bläck är en
  berättelse). Universitet: historikerna är oense om huset var en stor
  akademi eller främst kalifens bibliotek, mycket av bilden är senare
  legend. Fångar: "House of Wisdom", "Wisdom", "Bayt al-Hikma", "Hikma".
  Distraktorer: The Library of Alexandria, The Academy in Athens,
  Al-Qarawiyyin in Fez, Al-Azhar in Cairo, The University of Bologna, The
  Library of Cordoba, Nalanda, Sankore in Timbuktu. Bilder: rund stad från
  ovan, papperstillverkning, observatorium, bokhyllor på avstånd utan
  synlig skrift, Tigris med båtar.
- **Ibn Battuta**: Mr X. Född 1304 i Tanger i Marocko, lämnade hemmet 1325
  vid 21 år för pilgrimsfärden till Mecka, reste i nära trettio år och
  omkring 120 000 kilometer (skriv "about three times as far as the most
  famous traveler from Venice", Marco Polo får namnges, är inget set, men
  då inte distraktor på det kortet), Östafrikas kust med Kilwa och
  Mogadishu, Anatolien, stäppriket vid Volga, Konstantinopel, Centralasien,
  Delhi där sultanen gjorde honom till domare i flera år, Maldiverna som
  domare, Sri Lanka, Sumatra, Kina (historikerna tvivlar på delar av
  Kinaavsnittet), hem 1349 under en stor pest (namnges inte), sedan
  Granada och Mali över Sahara 1352-1353 med guldet, saltet och det som
  förvånade honom vid hovet, dikterade reseboken 1355 för en skrivare i Fez
  (Ibn Juzayy får namnges). Universitet: lån från andra reseskildringar,
  vad som är sett och vad som är hört, hans blick på kvinnor och slavar i
  de länder han beskriver, sakligt. Fångar: "Battuta", "Batuta".
  Distraktorer: Marco Polo, Zheng He, Xuanzang, Evliya Celebi, Leo
  Africanus, Rabban Bar Sauma, Benjamin of Tudela, Vasco da Gama,
  Christopher Columbus, Ferdinand Magellan. Bilder: kamelkaravan, dhow i
  monsunvind, Delhi-palats på avstånd, saltblock, inga kartor med text,
  inga flaggor, Kaba avbildas inte.
- **The Enlightenment**: Movement X. Europa på 1700-talet, förnuftet och
  erfarenheten som domare över tradition och auktoritet, Kants svar 1784
  "have the courage to use your own understanding" (dokumenterat, får
  citeras kort), Encyklopedin 1751-1772 av Diderot och d'Alembert med
  tusentals artiklar om hantverk och vetenskap, förbjuden 1759 och ändå
  fullbordad, Voltaire och toleransen med Calas-affären 1762, Montesquieu
  och maktdelningen 1748, Rousseau om samhällsfördraget och uppfostran
  1762, Locke som föregångare 1689, salongerna som kvinnor ledde och
  kaffehusen, en engelsk vetenskapsmans lagar som förebild (namnges inte),
  Beccaria mot tortyr och dödsstraff 1764, Wollstonecraft 1792 om kvinnors
  rättigheter, idéerna bakom revolutionerna i Nordamerika och Frankrike
  (seten namnges inte). Universitet: skuggsidan, tänkare som rättfärdigade
  slaveri och rashierarkier medan andra som Condorcet och Raynal fördömde
  dem, eurocentrismen, kritiken från 1900-talet om förnuftets baksida.
  Fångar: "Enlightenment", "enlightened", "enlighten", "Age of Reason"
  (ordet "reason" ensamt är tillåtet och centralt), svenska "upplysning" i
  alla former och "förnuftets tidsålder". Distraktorer: The Renaissance,
  The Reformation, Romanticism, The Scientific Revolution, Humanism, The
  Counter-Reformation, The Industrial Revolution, Positivism; ledtrådarna
  måste utesluta den vetenskapliga revolutionen (1700-talet, filosofer,
  encyklopedin, salongerna). Bilder: 1700-talets salong bakifrån,
  kaffehus, tryckeri utan läsbara sidor, en glob, inga porträtt, inga
  boktitlar.
