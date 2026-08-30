# Stilguide: svensk översättning av korten

Sedan 2026-08-26 levereras varje kort med både engelsk och svensk text.
Svenska översättningar lagras i `translations/<slug>.sv.json` och merjas in i
`data/cards.json` med `python3 tools/apply_translations.py`.

## Schema för `translations/<slug>.sv.json`

```json
{
  "slug": "socrates",
  "person_sv": "Sokrates",
  "cards": [
    {
      "title": "Mannen som aldrig skriver en bok",
      "text_sentences": ["...", "..."],
      "question": "Vem är herr X?",
      "options": ["Sokrates", "Platon", "Aristoteles", "Konfucius"],
      "words": [{"word": "barfota", "explanation": "utan skor"}],
      "main_caption": "...",
      "side_caption": "..."
    }
  ]
}
```

`cards` ligger i samma ordning som i `data/cards.json` (åk 6, åk 9, åk 12, åk 12,
universitet). `options` behåller exakt samma ordning som engelskan; det rätta
svaret identifieras via sin position.

## Regler

1. **Fullständig översättning, mening för mening.** Samma antal meningar som
   engelskan, samma innehåll. Detta är inte tipspromenadens nedkortade format;
   `poangpromenad/stationer.md` används bara som termbank och stilreferens.
2. **Anonymiseringen bevaras**: Mr X → herr X, King X → kung X, Master X →
   mästare X, Prince X → prins X, Khan X → khan X, Land X → land X, Empire X →
   rike X, the X people → folket X, Games X → spelen X, City X → staden X.
3. **Svarsläckan**: kortets rätta svar får aldrig förekomma i kortets egen
   svenska text, bildtext eller ordlista. Kontrollera efter översättning,
   svenska böjningsformer räknas. Undantag som är avsiktliga ledtrådar i
   engelskan (Augustus-kortets "en månad får hans namn: augusti") markeras
   med `"leak_ok": true` på kortet i översättningsfilen.
4. **Inga tankstreck** i löptext, skriv om med komma, kolon eller punkt.
   Undantag: pratminus först i repliker ("- Jag bara samtalar, säger han.")
   behålls som i engelskan.
5. **Inga parenteser**, skriv om med komma (Rogers regel 2026-08-24).
6. **Ordlistan**: `word` är det svenska ord som faktiskt används i den svenska
   korttexten (aqueduct → akvedukt), `explanation` en superenkel svensk
   förklaring. Samma antal ordposter som engelskan om inte ordet blir
   självförklarande på svenska; då ersätts posten med ett annat svårt ord ur
   den svenska texten, eller behålls med förenklad förklaring. Antalet poster
   får inte bli fler än engelskans.
7. **Nivåkänsla**: åk 6-kort på mellanstadiesvenska, universitetskort får vara
   mer avancerade, precis som engelskan.
8. **Tro markeras som tro**: "Christians believe" → "kristna tror",
   "Muslims believe" → "muslimer tror". Ordval kring religiösa gestalter följer
   de granskade formuleringarna i poangpromenad/stationer.md.
9. **Tempus följer engelskan** (historiskt presens i befintliga kort).
10. **Siffror**: svensk formatering med mellanslag, 4 000, 2 500.
11. Citat och talesätt översätts idiomatiskt, inte ordagrant
    ("I know that I know nothing" → "jag vet att jag ingenting vet").

## Terminologi (ur granskade översättningar)

Mesopotamien, Egypten, Fenicierna, Grekland, Olympiska spelen, Romarriket,
Bysantinska riket, Vikingarna, Djingis khan, Siddhartha Gautama, Konfucius,
Hammurabi, Kyros den store, akvedukt, stadsstater, kilskrift, Sidenvägen,
Digerdöden, Korstågen, "den gyllene regeln", "jag vet att jag ingenting vet",
Pax Romana med förklaring "den romerska freden".
