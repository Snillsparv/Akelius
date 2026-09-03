# Rutinprompt för schemalagd produktion

Klistra in som prompt i en Routine (Claude Code på webben, valfritt schema).
Fungerar oberoende av konto eftersom all kontext ligger i `CLAUDE.md`.

---

Schemalagd produktionskörning för Akelius-kortprojektet. Läs CLAUDE.md i
repots rot först och följ den.

1. Börja med `git fetch origin` och rebasa sessionens branch mot huvudbranchen
   claude/roger-akelilius-assignment-ax3a4m. Om en annan produktionssession
   nyligen mergat: utgå från det.

2. Om Gmail-verktygen är tillgängliga: kolla efter nya mejl från Roger
   (roger.akelius@yahoo.se) eller Claes (claes.svensson14@gmail.com) sedan förra
   körningen. Entydiga produktionsbesked arbetas in i reglerna och
   produktionen; tvetydiga eller känsliga beslut noteras och lyfts i rapporten.
   Skicka aldrig mejl, skapa inga utkast på eget initiativ. Saknas Gmail:
   hoppa över och notera det.

3. Producera nästa ämnen i docs/master-lista-50.md enligt produktionskedjan i
   CLAUDE.md (skriv, dubbelgranska, finalisera, importera, översätt med
   granskning, merja svenskan, generera bilder, bildgranska, regenerera
   underkända med egen kontroll, bygg sidorna). När 50-listan är slut: ta fram
   ett förslag på utökad lista mot 600+ kort och stanna där tills Jonas eller
   Roger valt.

4. Committa och merga efter varje färdigt delmoment. Jobba i hela,
   committbara enheter. Om API-anrop eller agenter börjar fejla på ett sätt som
   tyder på spend limit: avsluta snyggt, committa det som är klart, avrunda.

5. Uppdatera statusraderna i CLAUDE.md, README och masterlistan.

6. Avsluta med lägesrapporten enligt CLAUDE.md.

---

Tips för att spara credits: låt skrivutkast och översättningsutkast gå på en
billigare modell (Sonnet) och behåll den tunga modellen för historiker-,
redaktörs- och bildgranskning. Bildgenereringen kostar OpenAI-pengar, inte
Claude-credits.
