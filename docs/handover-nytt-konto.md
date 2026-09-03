# Så fortsätter arbetet från ett nytt konto

Checklista för att köra Akelius-projektet från ett annat Claude-konto
(t.ex. Jessicas). Allt projektet vet ligger i repot; `CLAUDE.md` läses
automatiskt av varje ny session och ger den hela sammanhanget.

## 1. GitHub

- Jonas lägger till kontoägarens GitHub-användare som **collaborator med
  skrivrätt** på `Snillsparv/Akelius` (Settings → Collaborators).
- I det nya Claude-kontot: koppla GitHub (claude.ai → Settings → Connectors,
  eller direkt när repot läggs till i Claude Code på webben) och ge appen
  tillgång till repot.

## 2. Miljö i Claude Code på webben

Skapa en miljö för repot (dokumentation:
<https://code.claude.com/docs/en/claude-code-on-the-web>):

- **Repo:** `Snillsparv/Akelius`.
- **Miljövariabel:** `OPENAI_API_KEY` = Jonas OpenAI-nyckel (bildgenereringen
  faktureras där, cirka 0,17 USD per bild).
- **Nätverkspolicy:** tillåt minst `api.openai.com`, `github.com`,
  `snillsparv.github.io`, `registry.npmjs.org`, `pypi.org` och
  `files.pythonhosted.org`. Enklast är den policy som tillåter allmän
  utgående trafik.
- Startkroken `.claude/hooks/session-start.sh` installerar Pillow, docx och
  playwright-core automatiskt när sessionen startar (den ligger i repot och
  aktiveras när den finns på huvudbranchen).

## 3. Första sessionen

Starta en session på repot och klistra in:

> Läs CLAUDE.md och bekräfta kort att du har sammanhanget: status, nästa
> ämnen, hårda regler och gitflödet. Kör sedan `python3 tools/import_cards.py
> --check socrates` och `python3 tools/apply_translations.py --check` för att
> verifiera att verktygen fungerar. Rapportera, men producera inget ännu.

Fungerar det: kör `docs/rutin-produktion.md` som prompt för första riktiga
körningen, eller lägg upp den som Routine.

## 4. Schemaläggning

Skapa en Routine i det nya kontot med prompten i `docs/rutin-produktion.md`.
Valfritt schema; ett par kvällar i veckan klarar 50-listan på några veckor.
**Pausa Jonas söndagsrutin** när det nya kontot tar över produktionen, så att
två sessioner aldrig arbetar mot `data/cards.json` samtidigt.

## 5. Mejlen från Roger

Gmail-kopplingen är per konto och Roger skriver till Jonas. Välj ett:

- Jonas vidarebefordrar Rogers mejl till kontoägaren, som kopplar sin Gmail.
- Jonas behåller mejlkollen i sitt eget konto (billigt) och klistrar in
  beskeden i det nya kontots session.

Oavsett vilket: sessioner skickar aldrig mejl och skapar utkast bara på
uttrycklig begäran.

## 6. Vad man bör kontrollera efter första körningen

- Att huvudbranchen `claude/roger-akelilius-assignment-ax3a4m` fick en
  ff-merge och att <https://snillsparv.github.io/Akelius/presentation.html>
  visar de nya ämnena på båda språken.
- Att `Set med komplett svenska` i valideraren visar alla set.
- Att lägesrapporten nämner eventuella beslut som behöver Jonas eller Roger.

## 7. Credits

Det som kostar Claude-credits är agenterna. Skriv- och översättningsutkast
kan gå på Sonnet, granskningarna på den tunga modellen. Bilderna kostar
OpenAI-pengar, inte credits.
