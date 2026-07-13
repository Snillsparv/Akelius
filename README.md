# Akelius frågekort — världshistoria

Produktion av frågekort i världshistoria för Akelius Foundations utbildningsmaterial,
på uppdrag av Roger Akelius (mejl 2026-07-12).

Korten används tryckta som spelkort och online, i skolor i Afrika, Asien,
Latinamerika och Europa, samt i språkundervisning för flyktingar.
Akelius översätter till tio andra språk.

## Leverans 1: Sokrates och Platon

Rogers förslag var att börja med fem frågekort vardera om Sokrates och Platon.
Den leveransen ligger klar i detta repo: **10 kort, faktagranskade och specgranskade.**

| Fil | Innehåll |
|---|---|
| `cards/socrates.md` | 5 kort om Sokrates, läsbart format med bildbriefer |
| `cards/plato.md` | 5 kort om Platon, läsbart format med bildbriefer |
| `data/cards.json` | Samma innehåll maskinläsbart, för Akelius produktion |
| `preview/index.html` | Förhandsvisning i samma layout som exempelkorten (öppna i webbläsare, utskriftsvänlig) |
| `docs/uppdrag-spec.md` | Kravspecen destillerad ur Rogers mejl |
| `docs/master-lista-50.md` | Listan med 50 personer/skeenden + produktionsstatus |

## Kortens struktur

Varje person får fem oberoende kort med stigande svårighetsgrad:

- 1 kort årskurs 6
- 1 kort årskurs 9
- 2 kort årskurs 12
- 1 kort universitet

Varje kort innehåller:

- **Korttext**: 7–12 superkorta meningar på superenkel engelska, i presens.
  Personen anonymiseras som "Mr X" och frågan är "Who is Mr X?".
- **Fem svarsalternativ**, varav ett rätt. Distraktorerna hämtas i möjligaste mån
  från masterlistans övriga namn, så att eleven möter fler historiska personer.
- **Ordlista**: 1–4 svåra ord med superenkla förklaringar (som i exempelkorten).
- **Två bildbriefer** (huvudbild + sidobild): beskrivning, Shutterstock-sökning,
  AI-prompt som alternativ, samt bildtext på enkel engelska. Sidobilden förklarar
  där det går ett svårt ord eller nyckelbegrepp.

Pedagogiska principer från Roger som styrt skrivandet:

- idéhistoria viktigare än krig — inget krigsförhärligande
- minimalt med årtal, århundraden i stället
- eleven ska aldrig behöva rabbla ur minnet — varje kort innehåller en ledtrådskedja
  så att svaret går att **resonera** sig till ur korttexten, plus en "varför"-insikt
- kulturneutralt: ska fungera i klassrum på fyra kontinenter

## Kvalitetsprocess

Varje kort har passerat tre steg:

1. **Utkast** — skrivet mot en genomtänkt vinkelplan (fem olika vinklar per person,
   inga upprepningar mellan korten, inga dubbletter av de tre befintliga exempelkorten)
2. **Adversariell granskning** — två oberoende granskningar per kort:
   en historikerlins (faktafel, felcitat, anakronismer) och en redaktörslins
   (meningslängd, ordval, tempus, nivå, ledtrådskedja, distraktorkvalitet)
3. **Slutredigering** — samtliga fynd åtgärdade, plus en korsgranskning av hela
   femkortsserien (svårighetsramp, ingen innehållsöverlappning)

## Öppna frågor till Roger/Claes

- Roger skriver "fyra multiple-choice svar", men exempelkorten (Akelius mall) har
  **fem** alternativ. Korten här följer mallen med fem — att stryka en distraktor
  är trivialt om fyra är det som gäller.
- Vilket filformat vill Akelius produktion ha i slutänden? `data/cards.json` är
  strukturerad så att den lätt kan omvandlas; be gärna om Akelius mallfil.
- Bildlicenser: briefer med Shutterstock-sökningar och AI-prompter ingår per kort;
  själva bildvalet/inköpet görs lämpligen mot Akelius Shutterstock-konto.

## Nästa steg

Fortsätta beta av masterlistan (se `docs/master-lista-50.md`) i valfri ordning —
korten är produktionsmässigt oberoende per person/skeende, precis som Roger noterar.
