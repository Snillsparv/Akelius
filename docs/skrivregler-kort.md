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
