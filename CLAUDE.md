# Akelius frågekort: projektkontext för Claude Code

Läs detta först i varje session. Det ersätter minnet av tidigare samtal.
Repot är **publikt** (GitHub Pages), så inga ersättningsbelopp eller andra
affärsvillkor får skrivas in någonstans i repot.

## Uppdraget

Frågekort i världshistoria för Akelius Foundations skolor (Afrika, Asien,
Latinamerika, Europa) på uppdrag av Roger Akelius. Beställare: Jonas von Essen
(jonas.superminne@gmail.com). Kollegan Jessica kan köra sessioner från eget
konto; arbetet sker i samma repo med samma regler.

Varje kort: anonymiserad ledtrådstext på superenkel engelska, en fetstilad
fråga, fyra svarsalternativ, ordförklaringar, huvudbild och sidobild, samt
sedan 2026-08-26 **svensk översättning av all elevvänd text**. Eleven ska kunna
resonera sig till svaret; svaret får aldrig läcka i text, titel, bildtext,
ordlista eller bild.

## Status (uppdatera vid varje leverans)

- 27 ämnen, 135 kort, 270 bilder, 100 procent tvåspråkigt (leverans 1-4).
- Näst på tur: rad 28-50 i `docs/master-lista-50.md` (Magellan, Kopernikus,
  Galilei ...), därefter förslag på utökad lista mot Rogers mål 600+ kort
  (idéhistoria, matematiker, fysiker, nobelpristagare).
- Öppet hos Roger: baksidestexter för befintliga kort, nivå 3-kort,
  "about X years ago" kontra århundraden.

## Var allt ligger

| Plats | Innehåll |
|---|---|
| `cards/<slug>.md` | Källfil per ämne i husformat (engelska), parsas av importern |
| `translations/<slug>.sv.json` | Svensk översättning per ämne, merjas in i cards.json |
| `data/cards.json` | Sanningskällan: allt innehåll inkl. `sv`-fält, `person_sv` |
| `data/image-prompts.csv` | Bildprompter, genereras från cards.json |
| `images/*.png` | Produktionsmaster (main 1536x1024, side 1024x1365); `images/web/` webbkopior |
| `index.html`, `presentation.html` | Intern förhandsvisning resp. granskningssida för Roger, bägge med språkknapp |
| `docs/skrivregler-kort.md` | Bindande skrivregler för nya set, inkl. ämnesnoter |
| `docs/oversattning-stilguide.md` | Bindande regler för svensk översättning |
| `docs/regler-2026-08-sammanfattning.md` | Rogers regeldokument och alla hans beslut, datumstämplade |
| `docs/uppdrag-spec.md`, `docs/master-lista-50.md` | Ursprunglig kravspec och ämneslista med status |
| `docs/rutin-produktion.md` | Prompten för schemalagda produktionskörningar |
| `docs/handover-nytt-konto.md` | Så sätter man upp ett nytt konto/miljö |
| `poangpromenad/` | Sidospår: tipspromenaden i Vara (klar, levererad) |

## Produktionskedjan (körs i denna ordning per leverans)

1. **Skriv** `cards/<slug>.md` per ämne med skrivaragenter (en per ämne, parallellt).
   Varje agent läser `docs/skrivregler-kort.md` plus två befintliga set som mall
   och självvaliderar med `python3 tools/import_cards.py --check <slug>`.
2. **Granska** med två oberoende agenter över hela batchen: historikerlins
   (fakta, myter, anakronismer, källpåståenden) och redaktörslins (läckor,
   ledtrådskedja, språk, struktur, bildbriefer, motivdubbletter). JSON-rapporter.
3. **Finalisera**: en agent för in alla fynd enligt redaktionella beslut,
   validerar igen. Egen kontroll: grep efter svarsord i egna set.
4. **Importera**: `python3 tools/import_cards.py <slugs>` (skriver om setet i
   cards.json och tar bort `sv`-fälten för det setet, så kör alltid steg 6 igen efteråt).
5. **Översätt**: translator-agent skriver `translations/<slug>.sv.json`,
   validerar med `python3 tools/apply_translations.py --check <slugs>`;
   sedan oberoende svensk granskare; fynd förs in.
6. **Merja svenskan**: `python3 tools/apply_translations.py <slugs>`.
7. **Bilder**: `python3 tools/build_prompts.py` sedan
   `python3 tools/generate_images.py --only <slug> --workers 4` (gpt-image-2,
   kräver `OPENAI_API_KEY`, cirka 0,17 USD per bild).
8. **Bildgranska** per set med en agent som läser briefen i md-filen och
   öppnar varje bild: motiv, textförbud, svarsläcka, känslighet, AI-fel,
   räknebara påståenden. Underkända genereras om med två kandidater och
   korrigerad prompt; **kontrollera ersättningen själv** (zooma, räkna) innan
   den läggs i `images/`. Uppdatera AI-prompten i md-filen, importera om,
   merja svenskan igen.
9. **Bygg och publicera**: `python3 tools/build_index.py`,
   `python3 tools/build_readme_cards.py`, uppdatera statusrader i README och
   masterlistan, committa, pusha, merga till huvudbranchen.

Verifiera sidorna vid behov med Playwright: `node` + `playwright-core` med
`executablePath: '/opt/pw-browsers/chromium'` (ladda aldrig ner webbläsare).

## Hårda regler (får aldrig brytas)

- Svaret eller genomskinliga former (Socratic, olympisk, Vinci) aldrig i
  elevvänd text, titel, bildtext, ordlista eller kategorietikett; anonymisering
  Mr X / Land X / folket X. Avsiktliga namnekon (Alexandria, juli, augusti)
  är tillåtna ledtrådar; markera dem med `leak_ok` i översättningsfilen.
- Ett kort får inte skänka bort ett ANNAT sets svar (t.ex. namnge vikingarna
  på Columbus-kortet).
- Exakt fyra alternativ, ett rätt. Nivåer: grade 6, 9, 12, 12, university
  (nivå 3 finns i Rogers system men är inte producerad).
- Inga parenteser i korttext, inga tankstreck utom pratminus i replikstart,
  inga emdash i användarvänd prosa, e-post eller presentationstexter.
- Muhammed avbildas aldrig, ingen arabisk kalligrafi (även pseudo). Jesus
  bara på avstånd eller bakifrån utan tydligt ansikte. Tro markeras alltid
  som tro. Korståg/kolonisation/erövring balanserat, ingen gore, inga
  hornhjälmar på vikingar, inga olympiska ringar, inga läsbara bokstäver
  eller siffror i någon bild.
- Faktafel är enligt Roger AI:s största problem: ingen text går vidare utan
  oberoende historikergranskning.

## Git

- Huvudbranch (GitHub Pages): `claude/roger-akelilius-assignment-ax3a4m`.
  Arbeta på sessionens egen branch, merga med `--ff-only` till huvudbranchen
  efter varje färdigt delmoment, pusha båda.
- Börja varje session med `git fetch origin` och rebasa mot huvudbranchen så
  att inga parallella körningar kolliderar i `data/cards.json`. **Kör aldrig två
  produktionssessioner samtidigt från olika konton.**
- Engelska committmeddelanden, inga modellnamn i repofiler, inga
  affärsvillkor. Beroenden installeras av `.claude/hooks/session-start.sh`.

## Kontakt med Roger och Claes

- Skicka **aldrig** e-post automatiskt och skapa inga utkast på eget
  initiativ. Utkast bara när Jonas ber om det; Jonas skickar.
- Läs gärna nya mejl om Gmail är kopplat: entydiga produktionsbesked arbetas
  in i `docs/regler-2026-08-sammanfattning.md` och i produktionen, tvetydiga
  eller känsliga beslut lyfts till Jonas i rapporten.
- Roger skriver korta, ibland dikterade mejl med snabba beslut. Han vill ha
  lättläst text, kommatecken i stället för parenteser, foto framför teckning
  framför AI, och religionshistoria som historia. Claes Svensson gör layout.

## Beslut som redan är fattade (ändra inte utan Jonas)

- Renässans-setets kategori är `exploration` (etiketten trycks på kortet och
  fick inte vara lika med svaret). Personseten i samma epok har `renaissance`.
- Svenska: Mr X = herr X, Miss X = fröken X, Captain X = kapten X;
  typografiska citattecken ”…”; Kopernikus, Djingis khan, tainofolket.
- Presenskravet är hävt (2026-08-26); befintliga presenstexter behålls.
- Sju ord per mening är riktmärke, inte lag.

## Rapportformat efter en körning

Kort lägesrapport i sessionen: vad som producerades, totalstatus (ämnen, kort,
bilder, andel svenska), vad som står näst på tur, beslut som fattats, frågor
till Jonas. Inga långa utläggningar, inga emdash.
