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
