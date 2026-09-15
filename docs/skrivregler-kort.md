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
respektive ingenting om Bagdadhuset; Bagdadsetet skriver "a
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
  metafysik och Europa, striden med senare teologer, berättelsen om de fyrtio genomläsningarna
  av Metafysiken tills en kort bok av al-Farabi öppnade den är hans egen
  självbiografi via eleven al-Juzjani och läses kritiskt, inte som legend
  mot självbiografi. Fångar: "Sina", "Avicenna", "Avicennian". Distraktorer: al-Razi,
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
  bröderna Banu Musa och deras maskiner, en matematiker från öster
  (namnges inte, han var vuxen man under al-Ma'mun), arvet till Europa via översättningar i Toledo och på
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
  omkring 120 000 kilometer enligt vanliga uppskattningar (skriv "several
  times as far as the most famous traveler from Venice", kvoten är inte
  fastställd, Marco Polo får namnges, är inget set, men
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
  (seten namnges inte). Universitet: skuggsidan, en del skribenter som använde den nya vetenskapen till att
  rangordna folk medan slavhandeln pågick, och andra som Condorcet och
  Raynal som angrep slaveriet; de stora filosoferna försvarade inte
  slaveriet, skriv inte så, eurocentrismen, kritiken från 1900-talet om förnuftets baksida.
  Fångar: "Enlightenment", "enlightened", "enlighten", "Age of Reason"
  (ordet "reason" ensamt är tillåtet och centralt), svenska "upplysning" i
  alla former och "förnuftets tidsålder". Distraktorer: The Renaissance,
  The Reformation, Romanticism, The Scientific Revolution, Humanism, The
  Counter-Reformation, The Industrial Revolution, Positivism; ledtrådarna
  måste utesluta den vetenskapliga revolutionen (1700-talet, filosofer,
  encyklopedin, salongerna). Bilder: 1700-talets salong bakifrån,
  kaffehus, tryckeri utan läsbara sidor, en glob, inga porträtt, inga
  boktitlar.

## Ämnesnoter, leverans 11

Tredje leveransen ur den utökade listan, Afrikablockets femkortsämnen: rad
86 Norman Borlaug och den gröna revolutionen, 87 transatlantiska
slavhandeln, 88 Mansa Musa och Mali, 92 Swahilikusten, 93 kapplöpningen om
Afrika, 94 Afrikas självständighet. Kategorier: `science` för Borlaug,
`colonialism` (ny, svenska "kolonialism") för slavhandeln och
kapplöpningen, `africa` (ny, svenska "Afrika") för Mansa Musa och
Swahilikusten, `twentieth century` för självständigheten. Etiketten trycks
på kortet och får inte vara en del av svaret; därför inte `africa` på
kapplöpningen om Afrika eller Afrikas självständighet. Målgruppen sitter i
Tanzania och Bhutan: Tanzanias egen historia (Kilwa, Zanzibar, Maji Maji,
Tanganyika 1961) skrivs sakligt och med respekt, utan att bli skolbokens
"vi".

Anonymisering och frågor: Borlaug är Mr X; Mansa Musa är King X ("Who is
King X?", svenska kung X); slavhandeln är Trade X ("Which trade is Trade X?",
svenska "handeln X", "Vilken handel är handeln X?"); Swahilikusten är Place X
("Which place is Place X?"); kapplöpningen är Event X ("Which event is Event
X?"); självständigheten är Movement X ("Which movement is Movement X?").
Svarsalternativen skrivs "Norman Borlaug", "The transatlantic slave trade",
"Mansa Musa", "The Swahili coast", "The Scramble for Africa", "African
independence".

Känslighet, bindande: ingen gore, inga kedjor eller piskor i närbild, inga
lidande kroppar; förslavade människor och koloniserade folk skildras med
handlingskraft (motstånd, uppror, abolitionister av afrikanskt ursprung,
segern vid Adwa), inte bara som offer; både afrikanska och europeiska
aktörer i slavhandeln nämns sakligt, utan att skuld fördelas i procent;
Kongofristatens grymheter och folkmordet på herero och nama nämns som
faktum utan detaljer; Maji Maji och Mau Mau likaså. Islam som historia:
ingen kalligrafi eller pseudoskrift i bilder, Kaba avbildas inte,
pilgrimsfärden visas som karavan. Kartor i bild bara utan bokstäver.
Tro markeras som tro.

Korsläckor att vakta: inget av de sex seten namnger något av de andra fem
("a rich king of Mali" i Swahilisetet är tillåtet men inte hans namn; i
självständighetssetet skrivs inte "Scramble"; slavhandelssetet skriver
"the rush for land in Africa" om det behövs). Befintliga set namnges inte i
löptext: Ibn Battuta ("a traveler from Morocco"), Mandela ("a leader in the
south who spends 27 years in prison" bara om det behövs), Gandhi, Martin
Luther King, FN ("the world organization"), kalla kriget ("the two great
powers"), världskrigen ("the war that ends in 1945"), Columbus, Magellan,
Muhammed, Djingis khan, industriella och amerikanska revolutionen,
Washington, Napoleon, Darwin, Pasteur, Churchill, Hitler. Julius Nyerere
och Wangari Maathai är föreslagna framtida set och namnges inte i löptext
("Tanzania's first president, a former teacher"), men får vara distraktorer.
Kwame Nkrumah, Menelik II, Samori Touré, Olaudah Equiano, Frederick
Douglass, Toussaint Louverture (framtida set 110, namnges inte, skriv "a
successful revolt on a Caribbean island in 1791"), Leopold II, Bismarck får
namnges där de behövs och är då inte distraktorer på det kortet.

- **Norman Borlaug**: Mr X, `science`. Född 1914 på en gård i Iowa,
  norskättad, studerade skogsbruk och sedan växtsjukdomar i Minnesota,
  1944 till Mexiko i ett program finansierat av en amerikansk stiftelse
  (Rockefeller får namnges), vete som stod emot rost, odling på två platser
  med två skördar om året, kortstråigt vete med gener från Japan, Mexiko
  självförsörjande på vete 1956, utsäde till Indien och Pakistan i mitten
  av 1960-talet när hungersnöd hotade, skördarna fördubblades på några år,
  Nobels fredspris 1970, uttrycket "green revolution" myntades 1968 av en
  amerikansk tjänsteman (tillåten ledtråd, det är inte svaret), kritiken:
  konstgödsel, bevattning och grundvatten, bekämpningsmedel, färre sorter,
  skulder för småbönder, ojämn nytta, Afrika kom sent (hans arbete där på
  1980-talet), död 2009. Universitet: har den gröna revolutionen mättat
  eller skuldsatt, Vandana Shiva och kritikerna, jordbruket i Afrika i dag.
  Fångar: "Borlaug", "Norman". Distraktorer: M. S. Swaminathan, Gregor
  Mendel, Wangari Maathai, Fritz Haber, Yuan Longping, George Washington
  Carver, Rachel Carson, Justus von Liebig, Luther Burbank, Louis Pasteur.
  Bilder: vetefält i Mexiko, försöksodlingar, säckar utsäde utan text,
  bondgård i Iowa på 1920-talet, inga porträtt, inga etiketter.
- **The transatlantic slave trade**: Trade X, `colonialism`. Från 1500-talet
  till 1860-talet, omkring 12,5 miljoner människor fördes ombord i Afrika
  och omkring 10,7 miljoner kom fram (siffror från forskningsdatabasen,
  skriv "historians count about"), tre ben: varor till Afrika, människor
  till Amerika, socker, tobak och bomull till Europa, portugiserna först,
  Brasilien tog emot flest, sockeröarna i Karibien näst flest, Nordamerika
  bara några procent, afrikanska kungariken och köpmän sålde fångar (Kongos
  kung Afonso protesterade i brev 1526, får namnges), överfarten sakligt
  utan detaljer, motstånd: uppror på ungefär vart tionde skepp, förrymda
  som byggde egna samhällen, revolten på en karibisk ö 1791, abolitionen:
  Storbritannien förbjöd handeln 1807 och slaveriet i kolonierna 1833, USA
  förbjöd införsel 1808 och slaveriet 1865, Brasilien sist i Amerika 1888, andra länder senare, Olaudah
  Equianos bok 1789, Frederick Douglass, Zong 1781 sakligt. Universitet:
  arvet, den afrikanska diasporan, rasismens rötter, minnesplatser och
  debatten om gottgörelse. Fångar: "slave trade", "transatlantic",
  "triangular trade"; orden "slave", "slavery", "enslaved", "trade" var för
  sig är tillåtna, liksom "Atlantic" som hav. Distraktorer: The
  trans-Saharan trade, The Indian Ocean trade, The Silk Road trade, The
  spice trade, The fur trade, The sugar trade, The opium trade, The
  Hanseatic trade. Bilder: hamnar, skepp på avstånd, sockerrörsfält, en
  tom dörröppning mot havet, ett minnesmärke utan text, inga kedjor i
  närbild, inga lidande människor, inga skeppsritningar.
- **Mansa Musa**: King X, `africa`. Härskade omkring 1312-1337 över Mali,
  riket kring Nigerfloden med guld och salt, pilgrimsfärden till Mecka
  1324-1325 med en enorm karavan (siffrorna 60 000 människor och tusentals
  kilo guld kommer från senare krönikörer, skriv "stories say"), gav bort
  så mycket guld i Kairo att priset föll i flera år (en egyptisk lärd
  skrev det tio år senare, skriv "a scholar in Cairo writes"), tog hem
  lärda och en arkitekt från Granada som enligt senare krönikor byggde en
  moské i Timbuktu 1327 (skriv "stories say"; staden fanns sedan omkring
  1100 och grundades inte av honom), Timbuktu som
  lärdomsstad med handskrifter, kartan från 1375 som visar honom med en
  guldklimp (beskriv inte kartan i bild, den är igenkännbar), "rikast i
  historien" är modern spekulation (skriv "some people say, but nobody can
  know"), rikets nedgång på 1400-talet, Songhai. Universitet: källorna, vad
  krönikörerna ville visa, guldets väg till Europa och myntningen där.
  Fångar: "Musa", "Mansa"; "Mali" och "Timbuktu" är tillåtna ledtrådar.
  Distraktorer: Sundiata Keita, Sonni Ali, Askia Muhammad, Idris Alooma,
  Osei Tutu, Shaka Zulu, Ezana of Aksum, Mutota. Bilder: karavan i öknen,
  saltblock, lermoské på avstånd utan text, Nigerfloden, guldsand i
  händer, inga kartor med text, ingen Kaba.
- **The Swahili coast**: Place X, `africa`. Kusten från Mogadishu till
  Kilwa och Sofala, stadsstater som Kilwa, Mombasa, Malindi, Zanzibar, Lamu,
  blomstring 700-1400-talen, monsunhandel med Arabien, Persien, Indien och
  Kina (kinesiskt porslin i Kilwa, en väldig flotta från Kina besökte
  kusten på 1410-talet, amiralen namnges inte), export av guld från inlandet
  via Sofala, elfenben, och förslavade människor (nämns sakligt, kort),
  import av tyg, porslin, pärlor, hus och moskéer av korallsten, Kilwas
  egna mynt, språket: ett afrikanskt bantuspråk med många lånord från
  arabiskan, i dag talat av över hundra miljoner och nationalspråk i
  Tanzania (språkets namn är svaret, skrivs aldrig), islam från 700-talet,
  portugiserna 1498 och plundringen av Kilwa 1505, Oman från 1698,
  Zanzibars kryddnejlikor och slavhandel på 1800-talet. Universitet: vem
  byggde Kilwa, den gamla myten om "arabiska kolonier" mot arkeologin som
  visar afrikanska städer, arvet i dagens Tanzania. Fångar: "Swahili",
  "Kiswahili", "Zanj". Distraktorer: The Gold Coast, The Malabar Coast,
  The Horn of Africa, The Red Sea coast, The Cape of Good Hope, The
  Coromandel Coast, The Barbary Coast, The Slave Coast. Bilder: dhow med
  latinsegel, korallstensruiner, hamn med monsunmoln, kryddnejlikor,
  porslinsskärvor utan mönstertext, inga kartor med text, ingen kalligrafi.
- **The Scramble for Africa**: Event X, `colonialism`. Omkring 1870 styrde
  européer omkring en tiondel av Afrika, 1914 nästan allt utom Etiopien
  och Liberia, konferensen i Berlin 1884-1885 (Bismarck får namnges, inga
  afrikanska delegater, regler för att göra anspråk, Kongo till Leopold II
  personligen), kinin, ångbåtar och maskingeväret gjorde erövringen möjlig,
  Kongofristatens gummitvång och grymheter sakligt utan detaljer, motstånd:
  Adwa 1896 där Etiopien under Menelik II besegrade Italien, Samori Touré,
  Maji Maji-upproret 1905-1907 i Tyska Östafrika (dagens Tanzania;
  uppskattningarna av antalet döda går från omkring 75 000 i tyska källor
  till 250 000-300 000 hos historikern Iliffe, de flesta av svält; skriv
  "historians count between seventy-five thousand and three hundred
  thousand dead, most of them from hunger"), folkmordet på
  herero och nama 1904-1908 som Tyskland erkände 2021, gränser dragna med
  linjal som delade folk och som till stor del består i dag. Universitet:
  varför just då, ekonomiska och politiska förklaringar, arvet för dagens
  stater, historikerdebatten. Fångar: "Scramble", "partition of Africa";
  "Africa", "Berlin" och "conference" är tillåtna. Distraktorer: The
  Crusades, The Age of Exploration, The Opium Wars, The Great Game, The
  Partition of India, The Congress of Vienna, The Boer War, The Suez
  Crisis. Bilder: konferensbord bakifrån utan kartor med text, ångbåt på
  flod, bergslandskap vid Adwa utan strid, gränsstolpe i savann, inga
  flaggor, inga vapen i närbild.
- **African independence**: Movement X, `twentieth century`. Libyen 1951,
  Sudan 1956, Ghana 1957 med Kwame Nkrumah (får namnges) som första land
  söder om Sahara, Guinea 1958 som sa nej till Frankrike, 1960 som Afrikas
  år med sjutton nya stater, Tanganyika 1961 under en lärare som blev
  president (namnges inte), unionen med Zanzibar 1964 blev Tanzania, Kenya
  1963 efter Mau Mau-upproret och de brittiska lägren, Algeriet 1962 efter
  ett krig med hundratusentals döda, de portugisiska kolonierna 1975 efter
  krig, Zimbabwe 1980, Namibia 1990, majoritetsstyre i söder 1994 (setet
  namnges inte), OAU 1963 i Addis Abeba, de två stormakternas inblandning
  (kalla kriget namnges inte), Bandung 1955, Kongokrisen 1960 och mordet på
  Lumumba 1961 sakligt, ärvda gränser, enpartistater och kupper, ujamaa i
  Tanzania sakligt med både mål och resultat. Universitet: var det verklig
  frihet, ekonomiskt beroende, historikerna om "flag independence", vad
  Tanzania valde. Fångar: "African independence", "independence of Africa",
  "decolonization", "decolonisation"; orden "independence", "independent",
  "free" och "Africa" var för sig är tillåtna. Svenska: skriv "i Afrika",
  aldrig genitiven "Afrikas", och aldrig "avkolonisering". Distraktorer: The
  civil rights movement, The Indian independence movement, The Non-Aligned
  Movement, The anti-apartheid movement, The Négritude movement, The labor
  movement, The Arab nationalist movement, The Pan-African movement (bara
  där ledtrådarna tydligt handlar om stater som blir fria). Bilder:
  folkmassa bakifrån på en plan, en flaggstång utan flagga i gryning,
  skolbarn i en ny skola bakifrån, en lärares kateder, inga flaggor med
  färger som pekar ut ett land, inga porträtt, ingen text.

## Ämnesnoter, leverans 12

Fjärde leveransen ur den utökade listan, Asienblockets femkortsämnen: rad
97 Qin Shi Huangdi, 98 Sidenvägen, 99 Ashoka, 100 Zheng He, 102 Akbar och
Mogulriket, 104 Meijirestaurationen. Kategori `asia` (ny, svenska "Asien")
för alla sex. Målgruppen sitter i Bhutan och Tanzania: Indien, Kina och
Japan skrivs som världshistoria, religion som historia, inga nationella
symboler i bild (inga flaggor, inte Indiens lejonkapitäl eller hjul, inga
läsbara inskrifter).

Anonymisering och frågor: Qin Shi Huangdi, Ashoka och Akbar är Emperor X
("Who is Emperor X?", svenska "kejsar X", "Vem är kejsar X?"); Zheng He är
Admiral X ("Who is Admiral X?", svenska "amiral X"); Sidenvägen är Road X
("Which road is Road X?", svenska "vägen X", "Vilken väg är vägen X?");
Meijirestaurationen är Event X ("Which event is Event X?"). Svarsalternativ:
"Qin Shi Huangdi", "The Silk Road", "Ashoka", "Zheng He", "Akbar", "The
Meiji Restoration".

Korsläckor att vakta: inget av de sex seten namnger något av de andra fem
(Sidenvägssetet skriver inte "Zheng He" eller "Qin"; Zheng He-setet skriver
"the old trade routes over land", inte Sidenvägen). Befintliga set namnges
inte i löptext: Konfucius ("an old teacher's ideas", "the emperor's
scholar-officials", aldrig "Confucian"), Siddhartha Gautama (orden
"Buddhism" och "the Buddha" är tillåtna som vanliga ord, namnet inte),
Alexander den store, Djingis khan ("Mongol" som adjektiv tillåtet), Marco
Polo får namnges (inget set), Ibn Battuta, Columbus, Magellan, Muhammed,
Swahilikusten ("the coast of East Africa"), Mansa Musa, industriella
revolutionen ("industry" och "industrial" som vanliga ord tillåtna),
franska och amerikanska revolutionen ("American ships" är tillåtet),
Napoleon, Ryska revolutionen är inget set och får nämnas som "a revolution
in Russia" på universitetsnivå. Kinesiska och japanska namn skrivs i
pinyin respektive Hepburn utan diakritiska tecken.

- **Qin Shi Huangdi**: Emperor X. Kung av Qin från 246 f.Kr. vid tretton års
  ålder, enade de stridande staterna 221 f.Kr., tog en ny titel som betyder
  den förste kejsaren av allt (titeln är svaret, skriv "a new title that
  means the first ruler of all"), samma skrift, mått, vikter, mynt och
  hjulbredd i hela riket, rådgivaren Li Si och lagarnas hårda skola,
  bokbränningen 213 f.Kr., berättelsen om de levande begravda lärda 212
  f.Kr. kommer från historikern Sima Qian hundra år senare och betvivlas
  av många (skriv "a later historian writes"), murar som bands samman till
  en tidig lång mur (dagens synliga mur är från Mingtiden omkring 1 700 år senare,
  blanda inte ihop), vägar och kanalen Lingqu, mordförsöket 227 f.Kr.,
  jakten på odödlighetens medicin och döden på resa 210 f.Kr. (kvicksilver
  som orsak är en gissning), graven nära Xi'an med terrakottaarmén som
  bönder fann 1974 när de grävde en brunn, omkring 8 000 soldater
  uppskattade och inga två ansikten lika, själva gravkullen är ogrävd, Sima
  Qians beskrivning av floder av kvicksilver och markprover med hög halt,
  dynastin föll 206 f.Kr. Universitet: tyrann eller grundare, Sima Qians
  källvärde, arkeologin mot texten. Fångar: "Qin", "Shi Huang", "Huangdi",
  "First Emperor"; "China", "terracotta", "Xi'an" är tillåtna.
  Distraktorer: Han Wudi, Liu Bang, Tang Taizong, Kublai Khan, Wu Zetian,
  Kangxi, Yongle, Genghis Khan (set, tillåten). Bilder: terrakottasoldater
  bakifrån eller på avstånd utan läsbara märken, en tidig jordmur i
  bergslandskap, bronsvikter utan tecken, inga kinesiska tecken någonstans.
- **The Silk Road**: Road X. Ett nät av vägar från Chang'an till Medelhavet,
  namnet gavs 1877 av en tysk geograf (får sägas, "a German scholar gives
  it a name in 1877"), sändebudet Zhang Qian omkring 138 f.Kr. som öppnade
  vägen västerut, sidenets hemlighet som Kina bevakade, siden i Rom (Rom
  som plats tillåten), varor västerut: siden, papper, porslin; österut:
  hästar, glas, guld, ull; idéer: Buddhismen till Kina, papperstillverkning
  västerut via Samarkand (berättelsen om fångarna efter slaget vid Talas
  751 är en berättelse), pesten på 1300-talet reste samma väg (skriv "a
  great plague", setet namnges inte), Mongolfreden på 1200-talet,
  Samarkand, Buchara, Kashgar, oaserna och kamelerna, grottorna vid
  Dunhuang och biblioteksgrottan som öppnades 1900 och vars handskrifter europeiska
  forskare köpte ut från 1907 (Stein 1907, Pelliot 1908, resten fördes till
  Peking 1910; sakligt, känsligt i Kina), sjövägarna som tog över på
  1500-talet. Universitet: begreppets historia, "vägar" i plural,
  namnet som politik i dag nämns neutralt eller inte alls. Fångar: "Silk
  Road", "Silk Route", "silk roads"; ordet "silk" ensamt är tillåtet.
  Distraktorer: The Amber Road, The Incense Route, The Tea Horse Road, The
  Royal Road, The Spice Route, The Grand Trunk Road, The King's Highway,
  The trans-Saharan trade route. Bilder: kamelkaravan i sanddyner,
  oasstad, silkesmaskar på mullbärsblad, ett tygstycke utan mönster som
  liknar skrift, grottor på avstånd, inga kartor med text.
- **Ashoka**: Emperor X. Maurya-rikets tredje kejsare omkring 268-232
  f.Kr., sonson till grundaren (namnges inte i löptext, Chandragupta Maurya
  bara som distraktor), kriget mot Kalinga omkring 261 f.Kr. där hans egen
  inskrift talar om hundratusen dödade (skriv "his own words on a rock
  say"), ångern, Buddhismen och läran om dhamma, edikten på klippor och
  pelare över hela riket på folkets språk (inskrifterna får inte vara
  läsbara i bild), sändebud till andra länder och traditionen att hans son
  och dotter förde läran till Sri Lanka (skriv "tradition says"), sjukhus
  för människor och djur, träd och brunnar längs vägarna, toleransediktet,
  glömd i nästan två tusen år tills en brittisk tjänsteman läste skriften
  1837 (James Prinsep får namnges), hjulet från hans pelare på Indiens
  flagga i dag (nämns i text, avbildas inte). Universitet: källorna är
  hans egna edikt och senare buddhistiska legender, vad som är
  propaganda, kejsaren som modell för icke-våld i modern indisk politik
  (Gandhi namnges inte). Fångar: "Ashoka", "Asoka", "Piyadasi",
  "Devanampiya", "Maurya", "Mauryan". Distraktorer: Chandragupta Maurya,
  Harsha, Kanishka, Samudragupta, Chandragupta II, Rajaraja Chola,
  Krishnadevaraya, Akbar (set i samma leverans, tillåten). Bilder: en
  pelare utan synlig inskrift på avstånd, en klippa vid en väg, ett
  slagfält efter striden utan kroppar (tomt fält, brutna vagnar), stupa,
  inga lejonkapitäl, inga flaggor.
- **Zheng He**: Admiral X. Född 1371 i Yunnan i en muslimsk familj, tagen
  som pojke av kejsarens armé, gjord till eunuck (skriv "made to serve at
  court" på lägre nivåer, sakligt "castrated" bara på universitetskortet),
  tjänade prinsen som blev kejsaren Yongle (får namnges), sju resor 1405-
  1433 med skattflottorna, enligt Mingkällorna över 60 stora skepp och
  omkring 27 000 man per resa (skriv "records of the time say"), de största
  skeppens längd är omtvistad (skriv "some old records say the biggest
  ships were as long as a football field, but many historians doubt it"),
  Sydostasien, Calicut i Indien, Hormuz, Arabien, Östafrikas kust med
  Malindi och Mogadishu, giraffen till hovet i Nanjing 1414-1415, gåvor och tributdiplomati
  snarare än erövring, men strid på Sri Lanka 1411 och på Sumatra, efter
  Yongles död upphörde resorna, kejsarens lärda ämbetsmän ansåg dem för dyra,
  havsförbud, han dog omkring 1433, troligen till sjöss. Universitet:
  varför Kina slutade, myten att han nådde Amerika (en bok 2002, avfärdad
  av historikerna), källäget. Fångar: "Zheng", "Cheng Ho", "Ma He".
  Distraktorer: Marco Polo, Vasco da Gama, Xu Fu, Zhang Qian, Yi Sun-sin,
  Faxian, Ibn Battuta, Christopher Columbus, Ferdinand Magellan (set,
  tillåtna). Bilder: stora skepp med bambusegel på avstånd utan flaggor,
  en giraff i en palatsgård, en hamn i Calicut, kompass utan tecken, inga
  ansikten, ingen kalligrafi.
- **Akbar**: Emperor X. Mogulkejsare från 1556 vid tretton års ålder,
  förmyndaren Bairam Khan, utvidgade riket över norra Indien, gifte sig
  med rajputprinsessor och band furstarna till sig, avskaffade skatten på
  icke-muslimer 1564, samtalshuset i Fatehpur Sikri byggt 1575, först bara för
  muslimska lärda, från omkring 1578 hinduer, jainer och zoroastrier och
  från 1580 jesuiter från Europa, den lilla
  hovkretsen omkring 1582 som senare kallats en egen religion (historikerna
  är oense, skriv försiktigt), kunde inte läsa men lät läsa högt och
  samlade ett väldigt bibliotek, målarverkstaden, översättningar av
  sanskriteposen till persiska, skatte- och ämbetssystemet med Todar Mal,
  krönikan Akbarnama av Abu'l-Fazl, huvudstaden Fatehpur Sikri som
  han lämnade 1585 för Lahore och gränsen i nordväst (vattenbrist är en
  omtvistad förklaring, skriv "historians are not sure why"), belägringen av Chittor 1568 med massakern sakligt i en mening,
  sonsonen som byggde ett berömt gravmonument (Taj Mahal får namnges).
  Universitet: tolerans som politik, källorna Abu'l-Fazl mot kritikern
  Badauni, kejsaren i dagens indiska debatt sakligt. Fångar: "Akbar";
  "Mughal" och "Mogul" är tillåtna eftersom flera distraktorer är
  mogulkejsare. Distraktorer: Babur, Humayun, Jahangir, Shah Jahan,
  Aurangzeb, Sher Shah Suri, Krishnadevaraya, Timur, Ashoka (set i samma
  leverans, tillåten). Bilder: röd sandstensstad på avstånd, ett samtal i
  en pelarsal bakifrån, miniatyrmåleri utan skrift, elefanter i procession
  utan flaggor, ingen kalligrafi.
- **The Meiji Restoration**: Event X. Japan stängt i över tvåhundra år under
  shogunerna med bara ett fönster i Nagasaki, de svarta skeppen 1853-1854
  (amerikanska, kommendören får namnges), de ojämlika fördragen, striden
  om landets väg, inbördeskriget 1868-1869, en femtonårig kejsare som
  fick makten tillbaka (verbet "restore" är tillåtet, substantivet inte),
  eden 1868, huvudstaden flyttad till Tokyo, samurajerna avskaffade som
  klass med svärdsförbud 1876 och upproret 1877, allmän värnplikt 1873,
  skola för alla från 1872, järnväg Tokyo-Yokohama 1872, Iwakuradelegationen
  1871-1873 som studerade väst, författning 1889 och riksdag 1890, kriget
  mot Kina 1894-1895 och segern över Ryssland 1905, Korea annekterat 1910,
  "rikt land, stark armé", priset: böndernas skatter, fabriksflickorna,
  militarismen längre fram. Universitet: revolution uppifrån, varför just
  Japan, historikerdebatten, vad andra länder i Asien och Afrika tog
  intryck av. Fångar: "Meiji", "Restoration"; "restore/restored" som verb
  och "emperor", "Japan", "Tokyo", "samurai" är tillåtna. Distraktorer: The
  French Revolution (set, tillåten), The Boxer Rebellion, The Taiping
  Rebellion, The Opium Wars, The Young Turk Revolution, The Tanzimat
  reforms, The Glorious Revolution, The Reform Movement of 1898.
  Bilder: svarta ångfartyg i en vik på avstånd, ett ånglok på 1870-talet,
  skolsal med barn bakifrån, samurajsvärd på ett ställ utan text, ett
  telegrafstolpe vid en bygata, inga flaggor, inga tecken.

## Ämnesnoter, leverans 13

Femte leveransen ur den utökade listan, Latinamerika och Mellanöstern: rad
107 Maya, 108 Azteker och Tenochtitlan, 109 Inka, 110 Haitis revolution, 111
Simón Bolívar, 116 Osmanska riket. Kategorier: `latin america` (ny, svenska
"Latinamerika") för de fem första, `middle east` (ny, svenska "Mellanöstern")
för Osmanska riket. Målgruppen sitter i Tanzania och Bhutan: erövring och
kolonisation skrivs balanserat, ursprungsfolken som aktörer och som levande
folk i dag, religion som historia, ingen gore (människooffer sakligt i en
mening, inga bilder av offer), inga nationella symboler i bild (inte örnen
på kaktusen, inga flaggor, inga läsbara glyfer eller inskrifter).

Anonymisering och frågor: Maya, azteker och inka är "the X people" ("Who are
the X people?", svenska "folket X", "Vilka är folket X?"); Haitis revolution
är Revolution X ("Which revolution is Revolution X?"); Bolívar är Mr X;
Osmanska riket är Empire X ("Which empire is Empire X?", svenska "riket X").
Svarsalternativ: "The Maya", "The Aztecs", "The Inca", "The Haitian
Revolution", "Simón Bolívar", "The Ottoman Empire".

Korsläckor att vakta: inget av de sex seten namnger något av de andra fem
(Bolívarsetet skriver "a free Black republic in the Caribbean", inte
Haiti; aztek- och inkaseten namnger inte maya och tvärtom; Osmanska riket
och Bolívar har inget med varandra att göra). Befintliga set namnges inte i
löptext: Columbus ("Spanish ships", aldrig 1492 som ledtråd), Magellan,
Napoleon ("the new ruler of France"), franska revolutionen ("the revolution
in France of 1789" är tillåtet), amerikanska revolutionen ("the revolution
in North America"), Washington, Bysantinska riket ("the old Christian
empire", "its capital on the Bosporus"), korstågen, Muhammed, Djingis khan
("Mongol" som adjektiv tillåtet), världskrigen ("the great war of 1914"),
transatlantiska slavhandeln ("the trade in enslaved people" tillåtet),
Akbar ("Mughal" som adjektiv tillåtet i distraktorer), Renässansen,
Reformationen. Cortés, Pizarro, Moctezuma, Atahualpa, Toussaint Louverture,
Dessalines, Sucre, San Martín, Mehmed II, Süleyman, Atatürk får namnges där
de behövs och är då inte distraktorer på det kortet. Rigoberta Menchú
(framtida set 114), mexikanska revolutionen (112) och Frida Kahlo (113)
namnges inte i löptext men får vara distraktorer.

- **The Maya**: the X people, `latin america`. Klassisk tid omkring 250-900
  e.Kr. i dagens Guatemala, Mexiko, Belize och Honduras, aldrig ett enda
  rike utan många stadsstater (Tikal, Calakmul, Palenque, Copán får
  namnges), skriftsystemet med glyfer (inga läsbara glyfer i bild, stelar på
  avstånd), den långa räkningen och kalendern (myten om världens slut 2012
  markeras som modern myt), talet noll i kalendern oberoende av Indien,
  astronomi med Venus-tabeller, trappstegspyramider, bollspelet, majs som
  grund, kakao som dryck, de södra städernas övergivande 800-950 (torka,
  krig, överbefolkning, historikerna oense), norra städer som Chichén Itzá
  fortsatte, spanjorernas erövring 1520-talet till 1697 (sista staden),
  franciskanen Landa, senare biskop, som brände
  böcker 1562 (bara fyra böcker överlevde; Landa får
  namnges), skriften läst först på 1900-talet (Knorozov 1950-talet får
  namnges), i dag 6-7 miljoner människor som talar omkring 30 språk.
  Universitet: kollapsen som forskningsfråga, dechiffreringen, folket i dag
  och deras rättigheter (Menchú namnges inte). Fångar: "Maya", "Mayan".
  Distraktorer: The Aztecs, The Inca (set i samma leverans, tillåtna),
  The Olmecs, The Toltecs, The Zapotecs, The Mixtecs, The Taíno, The Moche.
  Bilder: pyramid i djungel på avstånd, majsfält, kakaobönor, stela bakifrån
  eller på långt avstånd utan glyfer, bollplan tom, inga glyfer, inga
  kalenderstenar i närbild.
- **The Aztecs**: the X people, `latin america`. Mexica som vandrade in i
  Mexikodalen, staden på ön i sjön Texcoco grundad 1325 (legenden om örnen
  på kaktusen markeras som berättelse och avbildas inte), Tenochtitlan får
  namnges (tillåten ledtråd), chinampas som konstgjorda odlingsöar i
  den grunda sjön, i folkmun kallade flytande trädgårdar, vägbankar
  och akvedukter, det stora templet, omkring 200 000 invånare omkring 1500
  (skriv "historians estimate"), trippelalliansen 1428, tributriket,
  marknaden i Tlatelolco som spanjorerna häpnade över, människooffer
  sakligt i en mening utan detaljer, Moctezuma II, Cortés 1519 med
  inhemska allierade från Tlaxcala som var avgörande, smittkopporna 1520,
  stadens fall 1521 efter belägring, Mexico City byggd på ruinerna,
  nahuatlord i engelskan (chocolate, tomato, avocado), utgrävningarna av
  det stora templet från 1978, nahuatl talas av omkring 1,5 miljoner i
  dag. Universitet: erövringen som allians och sjukdom snarare än
  spanskt underverk, källorna (spanska och inhemska), offren i debatten.
  Fångar: "Aztec", "Aztecs", "Mexica". Distraktorer: The Maya, The Inca,
  The Toltecs, The Olmecs, The Zapotecs, The Mixtecs, The Purépecha, The
  Taíno. Bilder: staden på sjön på avstånd,
  odlingsöar av lera i sjön, marknad
  bakifrån, kanoter, inga örnar med orm, inga flaggor, inga offerscener.
- **The Inca**: the X people, `latin america`. Det största riket i Amerika
  före spanjorerna, Cusco som huvudstad, riket i fyra delar från omkring
  1438 (Pachacuti får namnges) till 1533, vägnätet på omkring 40 000
  kilometer med löpare och repbroar, knutsnören för räkenskaper (ingen
  skrift), terrasser, potatis och majs, lamor, murar utan murbruk, Machu
  Picchu byggt omkring 1450 och känt för världen 1911 genom en amerikan
  som lokalbefolkningen visade vägen (Bingham får namnges), arbetsplikten,
  förrådshusen, solguden och härskaren som hans son (tro markeras som tro),
  Atahualpa fångad i Cajamarca 1532 av Pizarro med omkring 170 män efter
  att smittkoppor och inbördeskrig försvagat riket, rummet med guld,
  avrättningen 1533, motståndet i Vilcabamba till 1572, quechua talat av
  omkring 8-10 miljoner i dag. Universitet: hur 170 män kunde ta ett rike
  (sjukdom, inbördeskrig, allierade, hästar och stål), knutsnörens gåta,
  Machu Picchu och turismen. Fångar: "Inca", "Inka", "Incan",
  "Tawantinsuyu", "Sapa". Distraktorer: The Maya, The Aztecs, The Moche,
  The Nazca, The Chimú, The Tiwanaku, The Mapuche, The Wari. Bilder:
  terrasser i bergen, repbro över klyfta, knutsnöre i händer (inga läsbara
  mönster), stenmur utan murbruk, lamor, Machu Picchu på avstånd i dimma
  (tillåtet, inga skyltar).
- **The Haitian Revolution**: Revolution X, `latin america`. Frankrikes
  rikaste koloni med socker och kaffe, omkring 500 000 förslavade
  människor och några tiotusen fria, upproret i augusti 1791 (ceremonin i
  skogen som traditionen berättar om markeras som tradition), Toussaint
  Louverture som ledare, slaveriet avskaffat i kolonin 1793 och av
  Frankrike 1794, hans styre och författning 1801, Frankrikes nye härskare
  (Napoleon namnges inte) sänder en armé som
  landstiger 1802, Toussaint fångad och död i
  ett franskt fängelse 1803, Dessalines segrar vid Vertières i november
  1803, självständighet 1 januari 1804 som den första staten grundad av
  före detta förslavade människor, namnet från öns ursprungsfolk (skriv
  "the island's old name", namnet är svaret), dödandet av kvarvarande
  fransmän 1804 sakligt i en mening, skulden till Frankrike från 1825 som
  betalades i över hundra år, isoleringen från slavägande stater, USA
  erkände landet först 1862. Universitet: den enda lyckade slavrevolten,
  varför den glömdes i Europas historieböcker, skulden och dagens debatt.
  Fångar: "Haiti", "Haitian", "Ayiti"; "Saint-Domingue" och "the Caribbean"
  är tillåtna ledtrådar. Distraktorer: The French Revolution, The American
  Revolution (set, tillåtna), The Mexican Revolution, The Cuban Revolution,
  The Russian Revolution, The Glorious Revolution, The Chinese Revolution,
  The Texas Revolution. Bilder: sockerrörsfält, en liten fästning på en
  kulle på avstånd (en bergsfästning bara som symbol
  för den nya staten, inte som del av kriget), en armé
  bakifrån i 1790-talets dräkt utan flaggor, ett tomt
  förhandlingsbord, ingen gore.
- **Simón Bolívar**: Mr X, `latin america`. Född 1783 i Caracas i en rik
  kreolsk familj, föräldralös som barn, läraren Rodríguez, resor i Europa,
  eden på kullen i Rom 1805 (hans egen berättelse), juntan 1810, manifestet
  1812, dekretet om krig till döden 1813 sakligt, brevet från Jamaica 1815,
  hjälpen 1816 från en fri svart republik i Karibien mot löfte att befria
  de förslavade (landet namnges inte), marschen över Anderna 1819 och
  segern vid Boyacá, Storcolombia, Carabobo 1821, mötet i Guayaquil 1822
  med befriaren från söder (San Martín får namnges), Peru 1824 med Sucre
  vid Ayacucho, landet som fick hans namn 1825 (namnges inte, "a new
  country takes his name"), diktaturen 1828 och mordförsöket som hans
  följeslagerska avvärjde (Manuela Sáenz får namnges), Storcolombias
  sönderfall 1830, orden om att ha plöjt havet (rapporterade, skriv "he is
  said to write"), döden 1830 i Santa Marta i lungsot. Universitet:
  hjälte eller diktator, hans syn på folkstyre, arvet i dagens politik
  sakligt utan att namnge nutida ledare. Fångar: "Bolívar", "Bolivar",
  "Bolivia", "Bolivarian", "Simón", "Simon", "Liberator", "Libertador".
  Distraktorer: José de San Martín, Bernardo O'Higgins, Antonio José de
  Sucre, Francisco de Miranda, Miguel Hidalgo, José Martí, Toussaint
  Louverture, George Washington (set, tillåten), Emiliano Zapata. Bilder:
  Anderna med en armé bakifrån, en plaza i Caracas på 1790-talet, ett
  skrivbord med brev utan läsbar text, en ryttare bakifrån, inga flaggor.
- **The Ottoman Empire**: Empire X, `middle east`. Grundat omkring 1299 av
  en turkisk furste i Anatolien (namnet är svaret, skriv "a Turkish
  prince"), Bursa och Edirne, erövringen av den gamla kristna
  huvudstaden vid Bosporen 1453 under Mehmed II (staden får kallas
  Constantinople och Istanbul, riket som föll namnges inte), Süleyman
  1520-1566 med lagarna, Mohács 1526 och Wien 1529, janitsjarerna
  (kristna pojkar togs, uppfostrades och blev soldater och ämbetsmän,
  sakligt), det som senare kallas millet-systemet (religiösa grupper skötte
  familjerätt, gudstjänst och skolor; skriv aldrig egna
  domstolar i allmänhet och markera termen som senare),
  moskéerna av Sinan, kaffet till Europa, Lepanto 1571,
  Wien 1683, "Europas sjuke man" som fras från 1800-talet, Tanzimat
  1839-1876, Balkankrigen, det stora kriget från 1914 på Tysklands sida,
  dödandet av det mesta av den armeniska befolkningen 1915 som historikerna
  kallar folkmord (en mening, sakligt, känsligt i Turkiet), slutet 1922 och
  republiken 1923 (Atatürk får namnges), sex hundra år. Universitet:
  nedgångsberättelsen som historikerna ifrågasätter, riket som flerfaldigt
  samhälle, arvet i dagens Mellanöstern och Balkan. Fångar: "Ottoman",
  "Osman", "Osmanli"; "Turkish", "Turkey", "Istanbul", "Constantinople",
  "sultan" är tillåtna. Distraktorer: The Byzantine Empire, The Roman
  Empire (set, tillåtna), The Safavid Empire, The Mughal Empire, The
  Abbasid Caliphate, The Mongol Empire, The Habsburg Empire, The Russian
  Empire. Bilder: kupoler och minareter på avstånd, ett kaffehus bakifrån,
  en kanon utan gravyr vid en stadsmur, ett rådsrum tomt, ingen kalligrafi,
  inga flaggor, inga religiösa figurer.
