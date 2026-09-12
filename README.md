# Akelius frågekort — världshistoria

Produktion av frågekort i världshistoria för Akelius Foundations utbildningsmaterial,
på uppdrag av Roger Akelius (mejl 2026-07-12).

Korten används tryckta som spelkort och online, i skolor i Afrika, Asien,
Latinamerika och Europa, samt i språkundervisning för flyktingar.
Akelius översätter till tio andra språk.

## Levererade kort

**280 kort · 56 ämnen**, samtliga faktagranskade och specgranskade.
Sedan 2026-08-26 levereras varje kort tvåspråkigt: engelsk text plus granskad
svensk översättning (växla språk med knappen på förhandsvisningssidorna).

- **Leverans 1** — Sokrates, Platon *(Rogers startförslag)*
- **Leverans 2** — Aristoteles, Forntida Egypten (pyramiderna), Mesopotamien,
  Hammurabi, Fenicierna & alfabetet, Alexander den store, Romerska
  republiken/kejsardömet, Julius Caesar, Konfucius, Siddhartha Gautama (Buddha)
- **Leverans 3** — Antikens Grekland, Olympiska spelen, Augustus, Jesus från
  Nasaret, Muhammed, Bysantinska riket, Vikingarna, Korstågen, Digerdöden,
  Djingis khan
- **Leverans 4** — Jeanne d'Arc, Renässansen, Leonardo da Vinci, Johannes
  Gutenberg, Christofer Columbus
- **Leverans 5** — Ferdinand Magellan, Nicolaus Kopernikus, Galileo Galilei,
  Reformationen, Martin Luther
- **Leverans 6** — Amerikanska revolutionen, George Washington, Franska
  revolutionen, Napoleon Bonaparte, Industriella revolutionen, Charles Darwin,
  Karl Marx
- **Leverans 7** — Första världskriget, Andra världskriget, Winston Churchill,
  Adolf Hitler, Mahatma Gandhi, Förenta nationerna
- **Leverans 8** — Kalla kriget, Martin Luther King, Nelson Mandela,
  Berlinmurens fall, Den första månlandningen
- **Leverans 9** — Isaac Newton, Albert Einstein, Marie Curie, Louis Pasteur,
  Alan Turing, Florence Nightingale *(första leveransen ur den utökade listan)*

Alla korten går att läsa direkt här nedanför under [Korten](#korten)
— fäll ut ett kort för att se text, svarsalternativ med facit och ordlista.

**🌐 Grafisk förhandsvisning (GitHub Pages):**
<https://snillsparv.github.io/Akelius/> — korten i samma layout som
exempelkorten, med facit-toggle, bildbriefer och utskriftsvänligt läge.
Uppdateras automatiskt vid varje push.

**🎁 Presentationssida för granskning:**
<https://snillsparv.github.io/Akelius/presentation.html> — putsad sida att
skicka till Roger: visar bara ämnen där alla bilder är klara, utan interna
bildbriefer och platshållare. Byggs om automatiskt av `tools/build_index.py`
och växer i takt med att nya bildbatchar blir klara.

| Fil | Innehåll |
|---|---|
| `cards/<ämne>.md` | 5 kort per ämne i läsbart format, med bildbriefer |
| `data/cards.json` | Allt innehåll maskinläsbart, för Akelius produktion |
| `data/image-prompts.csv` | Alla bildprompter i genereringsordning, med bild-ID:n |
| `images/` | Färdiga kortbilder i full upplösning (PNG, produktionsmaster); `images/web/` är webbkopior för förhandsvisningen |
| `index.html` | Förhandsvisningssidan som GitHub Pages publicerar på <https://snillsparv.github.io/Akelius/> |
| `tools/rename_images.py` | Döper om nedladdade AI-bilder till sina bild-ID:n |
| `tools/build_index.py` | Bygger om förhandsvisningen efter ny bildbatch eller kortändring |
| `docs/uppdrag-spec.md` | Kravspecen destillerad ur Rogers mejl |
| `docs/master-lista-50.md` | Listan med 50 personer/skeenden + produktionsstatus |

## Poängpromenaden i Vara (aug 2026)

Sidospår på Rogers begäran (mejl 2026-08-22): 2 × 10 historiefrågor till
poängpromenaden vid invigningen av Akelius Math Factory i Vara. Tio skyltar
med en lätt (åk 6-9) och en normal (åk 9-12) fråga vardera, hämtade ur
åk 6- och åk 9-korten, översatta till svenska och nedkortade till
tipspromenadformat. Allt ligger i `poangpromenad/`:

- `stationer.md` — källfilen med alla frågor, alternativ, facit och regler
- `Historia-poangpromenad-Vara.docx` (+ pdf) — skyltunderlag till layout, utan facit
- `Historia-poangpromenad-facit.docx` (+ pdf) — separat facit
- `bilder/` + `historia-bilder-vara.zip` — de 20 bilderna som JPEG i full upplösning
- byggs om med `node tools/build_poangpromenad_docx.js` efter ändring i `stationer.md`

Frågorna är parade så att de två frågorna på samma skylt aldrig har varandras
svar bland alternativen, och svaren krockar inte med geografidelens facit.

## Bilder

Bilderna AI-genereras batchvis från prompterna i `data/image-prompts.csv`
(560 st för leverans 1–9: 280 kort × huvudbild + sidobild).

**Status: 544 av 560 bilder klara** — samtliga kort i leverans 1–8 har
huvudbild och sidobild; i leverans 9 saknas 16 bilder (Einstein kort 3–5 och
hela Marie Curie) i väntan på påfyllda krediter hos bildtjänsten. Varje batch
har kvalitetsgranskats bild för bild mot sina briefer, och underkända bilder
har genererats om.

Arbetsflöde per batch:

1. Generera bilderna i CSV-ordning och lägg de nedladdade filerna i en mapp.
2. `python3 tools/rename_images.py <mapp> --start <radnr>` — dry run, kontrollera
   mappningen, kör sedan med `--apply`.
3. Flytta filerna till `images/` och kör `python3 tools/build_index.py` —
   skapar webbkopior i `images/web/` och kopplar in bilderna i förhandsvisningen.

PNG-filerna i `images/` är produktionsmaster och rörs inte av verktygen.
Obs för slutleverans: bild-ID:na (filnamnen) innehåller ämnesnamnet, t.ex.
`ancient-egypt-pyramids-…` — i elevvänt material måste filnamn/alt-texter bytas
så att de inte avslöjar kortets svar (bildtexterna på korten är redan säkra).

## Korten

### Forntida Egypten: pyramiderna

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A land by one long river</summary>

> Land X lies along one long river in Africa.  
> Almost no rain falls there.  
> But long ago, the river flooded every year.  
> The flood left black soil on the fields.  
> Farmers grew wheat in the black soil.  
> The river still gives life to the whole land.  
> The kings of Land X built huge stone tombs.  
> The most famous tombs have a square bottom.  
> The top is one point.  
> The biggest one is about 4,500 years old.  
> For thousands of years, it was the tallest building on Earth.  
> **Which land is this?**

**Svar:** ⬜ Mexico · ✅ Egypt · ⬜ China · ⬜ India

**Ord:** *flood* — the river rises and water covers the land · *soil* — the earth where plants grow · *tomb* — a room or building for a dead person · *wheat* — a plant; people make bread from it

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Thousands of workers, no modern machines</summary>

> Land X is a dry land by a long river.  
> The king wants a pyramid for his body after he dies.  
> There are no modern machines.  
> Thousands of workers pull heavy stones on wooden sledges.  
> They drag the stones up long ramps of earth and stone.  
> They cut the stone with tools of copper, a soft metal.  
> Today, archaeologists study the workers' village near the pyramids.  
> The workers are not slaves.  
> They get pay: bread, fish, and a place to sleep.  
> How do you feed thousands of workers, day after day?  
> Only a strong and well-planned land can do this.  
> **Which land is this?**

**Svar:** ⬜ Peru · ⬜ Mesopotamia · ✅ Egypt · ⬜ Mexico

**Ord:** *pyramid* — a building with a square bottom and one point at the top · *sledge* — a flat wooden board for pulling heavy things · *ramp* — a road that goes up, little by little · *archaeologist* — a scientist who digs in the ground to learn about old times

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A mountain of stone</summary>

> Why does a land build a mountain of stone?  
> Land X lies by a long river, at the edge of a great desert.  
> Its people believe their king is close to the gods.  
> While the king still lives, they build him a huge stone tomb.  
> It has a square bottom and one point at the top.  
> When the king dies, they make his body into a mummy.  
> They believe the body must last for the next life.  
> The tomb is a message in stone: our king lives on.  
> A building can show what people believe.  
> Think of the biggest buildings today: temples, banks, towers, stadiums.  
> What do they say about us?  
> **Which land is this?**

**Svar:** ⬜ China · ⬜ Mexico · ✅ Egypt · ⬜ Iraq

**Ord:** *mummy* — a dead body that is dried and wrapped so it lasts a very long time · *tomb* — a room or building for a dead person · *temple* — a building where people pray to a god · *desert* — very dry land with sand and almost no rain

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The scribes and the flood</summary>

> In Land X, a scribe sits by a field and counts sacks of wheat.  
> He writes signs on papyrus.  
> Picture-signs cover the temple walls.  
> The scribes collect taxes for the king.  
> Every year, the long river rises and covers the fields with water.  
> The water leaves rich black earth on the fields.  
> But the water also washes away the lines between the fields.  
> So every year, people must measure the land again.  
> All this measuring helps geometry grow.  
> A big kingdom needs writing and mathematics.  
> No scribes means no taxes, and no taxes means no pyramids.  
> **Which land is this?**

**Svar:** ⬜ Mesopotamia · ⬜ China · ✅ Egypt · ⬜ Greece

**Ord:** *scribe* — a person whose work is writing and counting · *papyrus* — a kind of paper; people make it from a river plant · *tax* — things people must give to the king or the state, like wheat or money · *geometry* — the mathematics of shapes and of measuring land

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The stone with three scripts</summary>

> Land X is full of old picture-writing.  
> The signs cover temple walls and the huge stone tombs of kings.  
> For many hundreds of years, nobody can read them.  
> More than 200 years ago, soldiers find a special stone by the river.  
> On the stone, the same text is written three times, in three scripts.  
> One script is old Greek, and scholars can read Greek.  
> For many years, scholars compare the scripts, sign by sign.  
> At last, they can read the picture-signs again.  
> Now we can read the land's prayers, its laws, even its shopping lists.  
> When a script is lost, a land's memory goes silent.  
> Archaeology can give the voice back.  
> **Which land is this?**

**Svar:** ⬜ Persia · ✅ Egypt · ⬜ Mesopotamia · ⬜ China

**Ord:** *script* — a set of signs for writing a language · *scholar* — a person who studies a subject very deeply · *archaeology* — the study of things people from long ago leave behind · *tomb* — a room or building for a dead person

</details>

### Mesopotamien: de första städerna och skriften

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Land Between Two Rivers</summary>

> Land X lies between two big rivers, the Tigris and the Euphrates.  
> The sun is hot, and there is little rain.  
> So people dig canals.  
> The canals carry river water to the fields.  
> The fields give much grain, and the villages grow.  
> The villages become the first big cities on earth.  
> Over time, the cities get walls, markets, and tall temple towers.  
> People press small signs into wet clay.  
> It is the first writing that we know of.  
> The name of this land means 'between the rivers'.  
> **Which land is this?**

**Svar:** ⬜ Egypt · ✅ Mesopotamia · ⬜ India · ⬜ China

**Ord:** *canal* — a small river that people dig; it carries water to the fields · *clay* — soft, wet earth; it gets hard when it dries · *temple* — a house for a god · *grain* — the seeds of plants like wheat; people make bread from it

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Why People Invent Writing</summary>

> The temple storehouses in Land X are full: grain, wool, oil, and sheep.  
> The workers must count everything.  
> Who brings ten sheep?  
> Who gets three jars of oil?  
> Memory alone is not enough.  
> At first, people count with small clay tokens.  
> The two big rivers, the Euphrates and the Tigris, give endless mud, and mud gives clay.  
> Later, people press signs into wet clay with a cut reed.  
> Over time, the signs become little wedges.  
> The first writing that we know of is not a poem - it is accounting.  
> Much later, people write letters, laws, and stories.  
> **Which land is this?**

**Svar:** ⬜ China · ⬜ Egypt · ✅ Mesopotamia · ⬜ Phoenicia

**Ord:** *token* — a small clay piece that stands for one thing, like one sheep · *reed* — a tall grass that grows by the river · *wedge* — a small shape like the tip of a nail · *accounting* — counting goods and writing the numbers down

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The City: A Big Invention</summary>

> In Land X, between two big rivers, the fields need canals.  
> Families must share the river water fairly.  
> So they agree on shared rules and work together.  
> The watered fields give more food than the farmers can eat.  
> This extra food changes everything: some people can stop farming.  
> They become builders, potters, priests, and traders.  
> Each person learns one craft well.  
> This is specialization.  
> Soon thousands of strangers live together in one place: the first city.  
> Today this land is mostly in Iraq.  
> Maybe the city is the biggest invention that people ever make.  
> **Which land is this?**

**Svar:** ⬜ Egypt · ⬜ the Indus Valley · ✅ Mesopotamia · ⬜ China

**Ord:** *canal* — a small river that people dig; it brings water to the fields · *specialization* — when each person learns one job very well · *craft* — a special skill or job; you learn it with long practice · *stranger* — a person you do not know

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The First Great Story</summary>

> The people of Land X write the oldest great story that we can still read.  
> They write it on clay tablets.  
> It tells about Gilgamesh, a king in the city of Uruk, between the rivers Euphrates and Tigris.  
> Gilgamesh loses his best friend, and now he is afraid of death.  
> He travels to the end of the world to find eternal life.  
> He fails.  
> A wise man tells him: no human lives forever.  
> So Gilgamesh goes home.  
> He learns to live well: build your city, love your people, enjoy your bread.  
> How do we live well, when life is short?  
> People ask this question 4,000 years ago, and we still ask it today.  
> **Which land is this?**

**Svar:** ⬜ Greece · ⬜ Egypt · ⬜ India · ✅ Mesopotamia

**Ord:** *eternal* — forever, without end · *tablet* — a flat piece of clay for writing · *clay* — soft, wet earth; it gets hard when it dries

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Clay Outlasts Paper</summary>

> Paper burns, but clay dries hard and lasts almost forever.  
> Land X is a hot plain between two rivers, the Tigris and the Euphrates.  
> The plain has much river mud, but few trees and few stones.  
> So the people write on soft clay tablets, and they leave us hundreds of thousands of them.  
> There are laws and lists of kings, but also receipts, letters, and school exercises.  
> One angry customer even complains about bad copper.  
> For a long time, nobody can read the wedge-shaped signs.  
> On a high rock in Persia, there is a king's message in three languages.  
> Scholars compare the languages and learn to read the signs.  
> Suddenly, everyday voices speak to us from about 4,000 years ago.  
> Durable writing materials keep the small voices alive, not only the voices of kings.  
> **Which land is this?**

**Svar:** ⬜ Greece · ⬜ Egypt · ⬜ China · ✅ Mesopotamia

**Ord:** *receipt* — a note that shows what somebody buys or pays · *scholar* — a person who studies one subject very deeply · *durable* — strong; it lasts a very long time · *wedge-shaped* — looking like small triangles, wide at one end and sharp at the other

</details>

### Hammurabi och hans lagar

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The King and the Tall Law Stone</summary>

> King X lives in the city of Babylon.  
> Babylon lies in a land between two big rivers.  
> Farmers use water from the rivers to grow food.  
> King X leads Babylon and many other cities.  
> He collects laws for the whole land.  
> A law is a rule that everyone must follow.  
> Workers carve the laws onto a tall black stone.  
> The stone is taller than a person.  
> It stands where all people can see it.  
> The king wants everyone to know the rules, not only powerful people.  
> This happens almost 4,000 years ago.  
> **Who is King X?**

**Svar:** ✅ Hammurabi · ⬜ Julius Caesar · ⬜ Alexander the Great · ⬜ Confucius

**Ord:** *carve* — to cut letters or pictures into hard stone · *powerful* — able to tell many people what to do, like a king

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Laws for All to See</summary>

> King X is the king of Babylon, a rich city in Mesopotamia.  
> His land is big, and every town has its own old rules.  
> The rules are not the same everywhere.  
> King X wants one set of laws for the whole land.  
> Workers write his laws on a tall stone, for all to see.  
> Anyone can point at the stone.  
> - Look, this is the law.  
> A judge cannot change it as he likes.  
> The king says the laws protect the weak from the strong.  
> He says the law must also help widows and orphans.  
> When all people can know the law, life is more fair.  
> **Who is King X?**

**Svar:** ✅ Hammurabi · ⬜ Cyrus the Great · ⬜ Julius Caesar · ⬜ Alexander the Great

**Ord:** *Mesopotamia* — an old land between two big rivers, in today's Iraq · *judge* — a person who decides who is right when people fight about rules · *widow* — a woman whose husband is dead · *orphan* — a child whose parents are dead

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A Window into Daily Life</summary>

> King X rules the city of Babylon about 3,800 years ago.  
> His workers cut nearly 300 laws into one tall stone.  
> The laws talk about wages for workers and prices in the market.  
> They talk about doctors' fees, the rent for a boat, marriage, and adoption.  
> One law says: a builder builds a bad wall.  
> The wall falls.  
> Then the builder must pay.  
> Why is this stone so exciting for us today?  
> From one stone, we can see how people live in old Babylon.  
> Laws show the problems people really have: work, money, family, houses.  
> Old laws are a window into daily life.  
> **Who is King X?**

**Svar:** ✅ Hammurabi · ⬜ Augustus · ⬜ Ashoka · ⬜ Alexander the Great

**Ord:** *wage* — the money you get for your work · *fee* — the money you pay for a service, for example to a doctor · *rent* — the money you pay to use a thing, like a boat or a house · *adoption* — taking a child into your family as your own child

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — An Eye for an Eye?</summary>

> King X of Babylon puts his laws on a tall stone.  
> His laws are some of the first written laws in the world.  
> One famous rule says: an eye for an eye.  
> But in Babylon, people are not equal.  
> Some people are free, and some people are slaves.  
> The punishment is not the same for every person.  
> If a man makes a free man blind, he can lose his own eye.  
> If he makes a slave blind, he only pays silver to the slave's owner.  
> Today, many lands want the same law for every person.  
> Ideas of justice have a history.  
> They can change, and they can get better.  
> **Who is King X?**

**Svar:** ✅ Hammurabi · ⬜ Moses · ⬜ Solon · ⬜ Julius Caesar

**Ord:** *slave* — a person who is not free and must work for an owner · *punishment* — something bad you must accept because you broke a rule · *equal* — the same for everyone · *justice* — when people are treated in a fair and right way

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Stone That Travels Through Time</summary>

> King X is a king of Babylon, in the land between two big rivers.  
> His laws are carved on a tall black stone.  
> At the top of the stone, there is a picture.  
> In the picture, the sun god gives King X a rod and a ring.  
> The message is strong: this law comes with the power of a god.  
> Centuries later, an army from another land carries the heavy stone away.  
> For them, it is a war prize.  
> More than a hundred years ago, archaeologists dig the stone out of the earth.  
> Today the stone stands in a museum in Paris.  
> There are older laws, but no other old law stone is kept so well.  
> One stone shows how law, power, and things travel through time.  
> **Who is King X?**

**Svar:** ✅ Hammurabi · ⬜ Gilgamesh · ⬜ Cyrus the Great · ⬜ Alexander the Great

**Ord:** *rod* — a short straight stick · *war prize* — a special thing that the winners take home after a war · *archaeologist* — a scientist who digs in the earth to find things from the past

</details>

### Fenicierna och alfabetet

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Ships, cedar, and purple</summary>

> The X people live about 3,000 years ago.  
> Their home is on the east coast of the Mediterranean Sea.  
> Behind their cities, the mountains are full of tall cedar trees.  
> They build strong ships from the cedar wood.  
> They are great sailors and traders.  
> They sail from city to city with wood, oil, and cloth.  
> They also make a famous purple dye from sea snails.  
> Purple cloth is so rare that kings pay gold for it.  
> They sell the purple cloth to the Greeks and to the kings of Egypt.  
> Their trading cities send ships all over the sea.  
> Their land is small, but the open sea makes them rich.  
> **Who are the X people?**

**Svar:** ⬜ The Egyptians · ✅ The Phoenicians · ⬜ The Greeks · ⬜ The Vikings

**Ord:** *trader* — a person who buys and sells things · *cedar* — a tall tree with strong, good-smelling wood · *dye* — something that gives color to cloth · *rare* — very hard to find; there is only a little of it

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Twenty-two little signs</summary>

> The X people are traders on the Mediterranean Sea.  
> Egyptian and Sumerian writing systems have hundreds of signs.  
> Only a few scribes learn it, after years of school.  
> But traders need fast notes in every port.  
> They write prices, names, and lists of the things they sell.  
> So the X people use a new, simple writing with only 22 signs.  
> One sign means one sound.  
> Now a child can learn to read in months, not years.  
> Their ships carry the signs to many lands.  
> Later, the Greeks learn the signs from the X people.  
> Most alphabets today come from those signs.  
> A simple tool can change the world.  
> **Who are the X people?**

**Svar:** ⬜ The Sumerians · ⬜ The Egyptians · ✅ The Phoenicians · ⬜ The Greeks

**Ord:** *sign* — a simple mark that you write, like a letter · *scribe* — a person whose job is writing · *port* — a town by the sea where ships stop · *alphabet* — a small set of letters that people use to write all words

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A network, not an empire</summary>

> The X people live in port cities on the east coast of the Mediterranean Sea.  
> Each city, like Tyre or Byblos, is a city-state with its own king.  
> The cities never join into one big empire.  
> Instead, the X people start small trading towns on many coasts, from Cyprus to Spain.  
> One of these towns is Carthage, in North Africa.  
> Carthage later grows into a great power of its own.  
> Their ships carry glass, purple cloth, and metals.  
> The ships also carry things you cannot put in a box.  
> They carry skills, ideas, and letters for writing.  
> Even the Greeks learn these letters from the X people.  
> Cities, towns, and sea roads form one big network.  
> Power can grow from trade, not from conquest.  
> **Who are the X people?**

**Svar:** ⬜ The Romans · ⬜ The Greeks · ✅ The Phoenicians · ⬜ The Egyptians

**Ord:** *city-state* — a city that is its own small country · *empire* — one ruler over many lands and peoples · *network* — many points joined together, like a spider web · *conquest* — taking land by war

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The journey of the letter A</summary>

> Look at the letter A on this card.  
> The X people are sea traders on the east coast of the Mediterranean Sea.  
> They write with only 22 simple signs.  
> Their first sign is called aleph.  
> Long before their time, aleph starts as a picture of an ox head.  
> Turn a big letter A upside down.  
> You can still see the two horns.  
> Greek sailors borrow the signs from the X traders.  
> The Greeks add vowels, like A, E, and O.  
> Later, in Italy, the Etruscans and then the Romans shape the letters again.  
> Hebrew and Arabic letters also come from those old signs.  
> A small idea can travel further than any ship.  
> **Who are the X people?**

**Svar:** ⬜ The Greeks · ⬜ The Romans · ⬜ The Hebrews · ✅ The Phoenicians

**Ord:** *trader* — a person who buys and sells things · *vowel* — a letter for an open sound, like A, E, O · *ox* — a strong farm animal, like a big cow · *sign* — a simple mark that you write, like a letter

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The people without a voice</summary>

> The X people spread simple letters all around the Mediterranean Sea.  
> Their home is the narrow coast where Lebanon is today.  
> But something strange happens to their story.  
> They write their notes and books on papyrus.  
> Papyrus rots fast in the wet air of the coast.  
> So almost all their own books are lost.  
> We know them mostly through their neighbors, like the Greeks and the Romans.  
> Those neighbors are often rivals, so their words are not always fair.  
> Even the name we use for the X people comes from a Greek word.  
> It is probably the Greek word for the purple color they make and sell.  
> Archaeologists read their story from broken pots, old ships, and short texts on stone.  
> When you read history, ask: who tells the story, and why?  
> **Who are the X people?**

**Svar:** ⬜ The Etruscans · ✅ The Phoenicians · ⬜ The Egyptians · ⬜ The Persians

**Ord:** *papyrus* — a kind of paper made from a river plant · *rot* — to slowly break down and fall apart, like old wet wood · *rival* — a person or group that fights or competes with you · *archaeologist* — a scientist who digs in the ground and studies old things

</details>

### Sokrates

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The man who never writes a book</summary>

> Mr X lives long ago in Athens.  
> Athens is a famous city in ancient Greece.  
> He has a simple life.  
> He often walks barefoot.  
> All day he walks around the city.  
> He talks with everyone: young people, workers, rich people.  
> He teaches them, but he does not want money for it.  
> He never writes a book.  
> - I only talk with people, he says.  
> - That is how I teach.  
> His students write down the words of Mr X.  
> That is why we still know his ideas today.  
> **Who is Mr X?**

**Svar:** ✅ Socrates · ⬜ Plato · ⬜ Aristotle · ⬜ Confucius

**Ord:** *barefoot* — with no shoes on your feet · *ancient* — very old, from a time long ago

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Answer with a question</summary>

> Mr X lives in Athens almost 2,500 years ago.  
> When you ask him a question, he does not answer.  
> He asks you a question back.  
> - What is your reason?  
> - Can you give an example?  
> Step by step, he tests each idea with you.  
> Weak ideas fall.  
> Strong ideas stay.  
> He is famous for one saying: I know that I know nothing.  
> He means: never be too sure of an idea.  
> Schools today still use his way of asking.  
> It also helps you check news, rumors, and advertising.  
> **Who is Mr X?**

**Svar:** ✅ Socrates · ⬜ Plato · ⬜ Buddha · ⬜ Aristotle

**Ord:** *reason* — why you think something is true · *saying* — a short sentence that many people know and repeat · *rumor* — a story people tell each other, but no one checks if it is true · *advertising* — words and pictures that try to make you buy something

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The trial of the questioner</summary>

> Athens loses a long war.  
> The people are afraid and angry.  
> Mr X is an old man, famous for his hard questions.  
> Three men take him to court.  
> - He leads the young people the wrong way, they say.  
> - He does not respect the gods of our city.  
> A jury of about 500 normal people votes: guilty.  
> The court says: he must die.  
> His friends want to help him run away, but he says no.  
> He will not stop asking questions, and he will not run away.  
> He calmly drinks a cup of poison and dies.  
> His trial leaves us a big question: what may a country do to a thinker?  
> **Who is Mr X?**

**Svar:** ✅ Socrates · ⬜ Galileo Galilei · ⬜ Gandhi · ⬜ Nelson Mandela

**Ord:** *trial* — when a court (the place of judges) decides: did a person do a crime? · *jury* — a group of normal people who vote in court: did he do it or not? · *guilty* — the court says: yes, he did it · *poison* — a thing that kills you when you drink or eat it

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The soul is worth more than gold</summary>

> Mr X walks through Athens.  
> He stops people and talks with them.  
> He stops the rich and important people too.  
> - You want money and fame, he says.  
> - But do you care for your soul?  
> He believes a good soul matters more than gold.  
> He says: when you do wrong, you hurt yourself most of all.  
> A man who cheats hurts his own soul.  
> He also says: the unexamined life is not worth living.  
> He means: stop and ask yourself, do I live in a good way?  
> His questions show that the powerful men often know little.  
> That is why many powerful men become his enemies.  
> **Who is Mr X?**

**Svar:** ✅ Socrates · ⬜ Aristotle · ⬜ Buddha · ⬜ Confucius

**Ord:** *soul* — the inner part of you: your thoughts, feelings, and character · *fame* — when many people know your name · *unexamined* — not checked, not looked at · *cheat* — to lie or trick people to win or get money

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Three pictures of one man</summary>

> Mr X writes nothing.  
> But he changes thinking forever.  
> We know him only through the books of other people.  
> His student Plato writes many dialogues about him.  
> Another student, Xenophon, shows a simpler man of daily life.  
> A comedy writer in Athens laughs at him on stage.  
> The three pictures of him are not the same.  
> Experts still ask: who is the real man?  
> His method is refutation.  
> He questions each claim until it cannot stand.  
> This method starts ethics, the study of right and wrong.  
> Later, Aristotle turns this testing into logic, the study of good arguments.  
> **Who is Mr X?**

**Svar:** ✅ Socrates · ⬜ Plato · ⬜ Confucius · ⬜ Buddha

**Ord:** *dialogue* — a written talk between two or more people · *expert* — a person who knows very much about one thing · *refutation* — showing, step by step, that an idea cannot stand · *claim* — something a person says is true

</details>

### Platon

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The student who writes it all into books</summary>

> Mr X lives in Athens, a city in Greece.  
> His teacher asks people questions at the big square.  
> His teacher does not write books.  
> One day, a big court in the city says his teacher must die.  
> Mr X is very sad and travels to other countries.  
> Later he comes back and opens a school in a quiet garden.  
> The school is called the Academy.  
> A young student named Aristotle studies at his school.  
> Mr X writes many books.  
> His books look like conversations.  
> In his books, his teacher asks questions, just like in real life.  
> Mr X writes, so his teacher's ideas never die.  
> **Who is Mr X?**

**Svar:** ✅ Plato · ⬜ Socrates · ⬜ Aristotle · ⬜ Confucius

**Ord:** *Academy* — the name of his school. Many schools use this name today. · *conversation* — two or more people talking together · *square* — an open place in the middle of a town · *scroll* — a long piece of paper that you roll up

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The cave and the shadows</summary>

> Mr X lives in Athens about 2,400 years ago.  
> His teacher is Socrates.  
> Mr X writes a famous story about a cave.  
> Prisoners sit in a dark cave.  
> They are chained, so they can only look at the wall.  
> A fire behind them makes shadows on the wall.  
> They think the shadows are the whole world.  
> One prisoner gets free and sees the sun.  
> He goes back to tell the others.  
> They do not believe him.  
> Mr X says: learning is like walking out of the cave.  
> Today, a phone screen can be like that wall.  
> **Who is Mr X?**

**Svar:** ✅ Plato · ⬜ Socrates · ⬜ Buddha · ⬜ Karl Marx

**Ord:** *cave* — a big dark hole in a rock or under the ground · *prisoner* — a person who is not free and cannot go out · *shadow* — the dark shape a thing makes when it blocks light · *chained* — tied with metal rings, so you cannot move away

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The perfect circle</summary>

> Mr X starts a famous school in Athens.  
> He is a student of Socrates.  
> Mr X is a philosopher, not a mathematician.  
> But his school loves geometry.  
> Try this: draw a circle.  
> Look closely: the line is always a little bit wrong.  
> No drawing is ever a perfect circle.  
> But the idea of a circle is perfect.  
> Mr X teaches that our eyes see only imperfect copies.  
> Only the mind can see the perfect ideas.  
> Geometry trains the mind to work with perfect ideas.  
> Ask yourself: do you trust your eyes, or your mind?  
> **Who is Mr X?**

**Svar:** ✅ Plato · ⬜ Pythagoras · ⬜ Euclid · ⬜ Socrates

**Ord:** *philosopher* — a person who thinks hard about big questions · *mathematician* — a person who works with numbers and shapes · *geometry* — mathematics about shapes, like circles and triangles · *imperfect* — not perfect; with small mistakes

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Who should rule?</summary>

> Mr X lives in Athens.  
> One day, a big jury judges his teacher, Socrates.  
> Hundreds of people vote, and the teacher must die.  
> So Mr X does not trust every decision of the crowd.  
> A clever talker can trick a crowd.  
> Later, Mr X writes a famous book called The Republic.  
> The book asks: what makes a state fair?  
> He says: rulers must be wise and love learning.  
> Not the richest people, not the loudest people.  
> A good ruler loves truth more than power.  
> Mr X teaches this to his student Aristotle.  
> His question is still alive today: how should we choose our leaders?  
> **Who is Mr X?**

**Svar:** ✅ Plato · ⬜ Aristotle · ⬜ Socrates · ⬜ Karl Marx

**Ord:** *jury* — a group of people who decide if someone did wrong · *state* — a country and the people who lead it · *ruler* — a person who leads a country

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — What is knowledge?</summary>

> Mr X starts a school in Athens.  
> His teacher is Socrates.  
> The school stays open for about three hundred years.  
> Mr X asks a hard question: what is knowledge?  
> A lucky guess can be true, but it is not knowledge.  
> In one book he tests an answer.  
> You know something when your true belief has good reasons.  
> In another book, a boy with no schooling solves a problem about a square.  
> The boy only answers good questions, step by step.  
> Mr X says: questions wake up the mind, so learning is like remembering.  
> A famous modern thinker says: European philosophy is footnotes to Mr X's books.  
> So when you read the news, ask: do I know this, or do I only believe it?  
> **Who is Mr X?**

**Svar:** ✅ Plato · ⬜ Socrates · ⬜ Confucius · ⬜ Buddha

**Ord:** *belief* — something you think is true · *knowledge* — the things you really know, not only believe · *philosophy* — thinking hard about big questions · *footnote* — a small extra note at the bottom of a page

</details>

### Aristoteles

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Teacher Who Studies Everything</summary>

> Long ago, Mr X lives in Greece.  
> He wants to know about everything.  
> He studies animals, fish, birds, stars, and the weather.  
> He collects many things and compares them.  
> He has a school with a garden in Athens.  
> People tell a story: he walks when he teaches.  
> His students walk with him.  
> He also teaches a young prince.  
> This prince later becomes a very famous king: Alexander the Great.  
> He teaches his students to look closely at the world.  
> When you look closely and compare, you learn new things.  
> **Who is Mr X?**

**Svar:** ✅ Aristotle · ⬜ Socrates · ⬜ Plato · ⬜ Darwin

**Ord:** *collect* — to bring many things together in one place · *compare* — to look at two things and see what is the same and what is different · *prince* — the son of a king

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Use Your Eyes</summary>

> Mr X lives in Greece.  
> It is more than 2,300 years ago.  
> His teacher in Athens is the famous thinker Plato.  
> Plato trusts thinking more than looking.  
> But Mr X thinks you must also use your eyes!  
> He watches bees and octopuses for many hours.  
> He opens dead animals to see what is inside.  
> He describes hundreds of kinds of animals.  
> Many people call him the first biologist.  
> His big idea: do not only think - look and check.  
> This idea is a root of modern science.  
> **Who is Mr X?**

**Svar:** ✅ Aristotle · ⬜ Darwin · ⬜ Socrates · ⬜ Hippocrates

**Ord:** *octopus* — a sea animal with eight arms · *biologist* — a scientist who studies living things · *root* — the place where something begins, like the root of a plant

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The Rules of Good Thinking</summary>

> Mr X is a student at Plato's school in Athens.  
> After many years, he opens his own school.  
> He asks: when is an argument good?  
> He writes clear rules for thinking.  
> Much later, teachers give a famous example of his rules:  
> All humans are mortal.  
> Socrates is a human.  
> So Socrates is mortal.  
> If the first two sentences are true, the third must be true.  
> People call this science logic.  
> Mathematics and computers still build on this science today.  
> **Who is Mr X?**

**Svar:** ✅ Aristotle · ⬜ Socrates · ⬜ Pythagoras · ⬜ Euclid

**Ord:** *argument* — reasons that you give to show that something is true · *mortal* — somebody who must die one day · *logic* — the rules for good, clear thinking

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The Good Middle</summary>

> Mr X is a Greek thinker.  
> He learns from Plato for many years.  
> Plato's own teacher is Socrates.  
> Later, Mr X opens his own school in Athens.  
> He asks: what is a good life?  
> His answer: look for the good middle.  
> Courage is in the middle, between being a coward and being reckless.  
> Generosity is between wasting money and giving nothing.  
> You become good by training good habits, like training a muscle.  
> Happiness is not one moment of fun, he says.  
> Happiness is a whole life, lived well.  
> **Who is Mr X?**

**Svar:** ✅ Aristotle · ⬜ Plato · ⬜ Buddha · ⬜ Confucius

**Ord:** *courage* — being brave when something is hard · *coward* — a person who is too afraid to act · *reckless* — doing wild, dangerous things without thinking · *generosity* — giving gladly to other people

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Check Every Authority</summary>

> Mr X is a Greek thinker.  
> He writes many books: about logic, nature, and the good life.  
> He loves his teacher Plato, but he loves truth more.  
> After his death, scholars in the Arabic world translate and study his books.  
> Later, the great scholar Ibn Rushd explains his ideas.  
> For many centuries, teachers say: if he writes it, it is true.  
> But he also writes: heavy things fall faster than light things.  
> Much later, scientists test this - and it is wrong.  
> Is this bad for him?  
> No - he himself teaches: when facts and ideas disagree, believe the facts.  
> Check every authority - even Mr X.  
> **Who is Mr X?**

**Svar:** ✅ Aristotle · ⬜ Plato · ⬜ Galileo Galilei · ⬜ Copernicus

**Ord:** *scholar* — a person who studies books deeply · *authority* — a person or a book that many people trust and follow · *century* — one hundred years · *logic* — the rules for good, clear thinking

</details>

### Alexander den store

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Boy and the Horse No One Can Ride</summary>

> King X is a young king from Macedonia, near Greece.  
> A famous old story tells about him as a boy.  
> There is a horse that no one can ride.  
> Everyone is afraid of the horse, but the boy watches it carefully.  
> He sees that the horse is afraid of its own shadow.  
> He turns the horse toward the sun, and the horse becomes calm.  
> He wins the horse with understanding, not with force.  
> The boy's teacher is the famous thinker Aristotle.  
> Later, he leads his army east, all the way to India.  
> In Egypt, he builds a new city and gives it his own name.  
> The name of this city sounds like the name of King X.  
> **Who is King X?**

**Svar:** ⬜ Julius Caesar · ✅ Alexander the Great · ⬜ Augustus · ⬜ Hammurabi

**Ord:** *shadow* — the dark shape you make on the ground when you stand in the sun · *force* — strong power; when you push or fight to make something happen · *understanding* — when you watch and learn why something happens

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A Language Travels East</summary>

> King X is the king of Macedonia, a land next to Greece.  
> He and his soldiers speak Greek.  
> He leads a strong army east, through Egypt and Persia, to India.  
> The Greek language travels with the army.  
> Soon, many people from Egypt to Central Asia speak and write Greek.  
> New cities grow along the army roads.  
> They have theaters, sports fields, and marketplaces, like cities in Greece.  
> Greek, Egyptian, and Persian customs mix into something new.  
> King X dies young, and his empire quickly breaks apart.  
> An army can hold people together for a short time.  
> A language can hold them together for hundreds of years.  
> **Who is King X?**

**Svar:** ⬜ Cyrus the Great · ⬜ Genghis Khan · ✅ Alexander the Great · ⬜ Julius Caesar

**Ord:** *customs* — the ways people usually do things, for example food, clothes, and holidays · *empire* — many lands and many people under one king · *marketplace* — an open place where people buy and sell things

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The City of Knowledge</summary>

> King X, a king from the Greek world, takes lands from Greece to India.  
> In Egypt, he builds a new city by the sea and gives it his own name.  
> After his death, this city becomes the most important city for knowledge in the ancient world.  
> Its famous library tries to collect every book in the world.  
> One story tells that the library takes the books from every ship in the harbor.  
> The ships get back only copies.  
> A giant lighthouse guides ships to the city.  
> People call it one of the wonders of the world.  
> Here a scholar measures the size of the whole Earth, with sticks, shadows, and mathematics.  
> When knowledge from many lands meets in one place, people can do new things.  
> The king's sword is gone, but his city of ideas still changes the world.  
> **Who is King X?**

**Svar:** ✅ Alexander the Great · ⬜ Cleopatra · ⬜ Julius Caesar · ⬜ Augustus

**Ord:** *lighthouse* — a tall tower with a fire or light on top; it shows ships the way · *scholar* — a person whose work is to study and learn · *harbor* — a safe place by the sea where ships stop · *wonder* — an amazing building or thing; old lists name seven wonders of the world

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Great for Which People?</summary>

> People call King X "the Great".  
> He wants to be like Achilles, a hero from the old Greek poems.  
> His army wins many fights from Greece to India.  
> But look at the other side of the story.  
> His wars kill hundreds of thousands of people.  
> He burns Persepolis, the palace city of the Persian kings.  
> He fights the Persian kings, but he is not born one of them.  
> He dies young, and his generals break his empire into pieces.  
> So, is he great?  
> Great for which people - the winners, the dead, or the conquered?  
> The names we give people in history are a choice, not a fact.  
> **Who is King X?**

**Svar:** ⬜ Napoleon · ⬜ Genghis Khan · ✅ Alexander the Great · ⬜ Julius Caesar

**Ord:** *conquered* — people whose land is taken by force · *general* — a leader in an army · *palace* — a very big and fine house of a king · *empire* — many lands under one king

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Man and the Myth</summary>

> King X is a young king from the Greek world.  
> His armies go east, all the way to India.  
> He dies young, but people never stop telling his story.  
> For more than 2,000 years, his legend grows.  
> People from Ethiopia to Malaysia tell stories about him.  
> In some stories, he even looks for magic water that gives life forever.  
> Here is the problem for historians.  
> His friends and soldiers write books about him, but all those books are lost.  
> The oldest history books we still have are written centuries after his death.  
> So historians must ask which stories are facts and which are dreams.  
> The historian's hardest job is to find the real man behind the myth.  
> **Who is King X?**

**Svar:** ✅ Alexander the Great · ⬜ Genghis Khan · ⬜ Cyrus the Great · ⬜ Julius Caesar

**Ord:** *legend* — an old famous story; it may be true or not true · *myth* — a story many people tell, but it is not a proven fact · *source* — an old text or thing that gives us information about the past · *historian* — a person who studies the past

</details>

### Romerska republiken och kejsardömet

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The city on seven hills</summary>

> Empire X starts as a small town on a hill in Italy.  
> The town grows until it covers seven hills.  
> Slowly, it becomes a giant empire.  
> Its lands go all the way around the Mediterranean Sea.  
> Its people build long, straight roads of stone.  
> Stone channels carry fresh water into the cities.  
> People call these channels aqueducts.  
> People from many different lands live in this empire.  
> In most places, they use the same coins and the same laws.  
> So a trader can travel far and still feel at home.  
> You can still walk on some of the old roads today.  
> Today, that first town is the capital of Italy.  
> **Which empire is this?**

**Svar:** ✅ Rome · ⬜ Persia · ⬜ Egypt · ⬜ Carthage

**Ord:** *empire* — many lands and people under one ruler · *channel* — a long open way made for water to run in · *aqueduct* — a stone channel that carries fresh water into a city, sometimes on tall arches · *Mediterranean Sea* — the big sea between Europe, Africa, and Asia

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The public thing</summary>

> The people of City X tell this old story:  
> About 2,500 years ago, they throw out their king.  
> They promise: we never want a king again.  
> Now, every year, they choose two new leaders, called consuls.  
> One consul can always stop the other.  
> A senate of old, wise men gives advice.  
> Free men meet and vote on the laws.  
> Women cannot vote.  
> The people call their state res publica - 'the public thing'.  
> Our word 'republic' comes from this.  
> The city lies in Italy.  
> But many countries far from Italy still use these ideas today.  
> **Which city is this?**

**Svar:** ✅ Rome · ⬜ Athens · ⬜ Sparta · ⬜ Carthage

**Ord:** *consul* — one of the two chosen leaders of the city · *senate* — a group of old, wise men who give advice · *vote* — to say your choice when a group decides something · *republic* — a country without a king; the people choose their leaders

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — How a republic dies</summary>

> At first, kings rule City X.  
> Then the people send the kings away.  
> The city becomes a republic.  
> For hundreds of years, the people choose new leaders every year.  
> Then rich generals begin to give their soldiers money and land.  
> The soldiers now follow their general, not their city.  
> Generals fight generals: civil war.  
> People become tired and afraid, and they only want peace.  
> In the end, one man holds all the power in this city in Italy.  
> He keeps the old names, and he calls himself the 'first citizen'.  
> The republic is over.  
> Institutions last only when people protect them.  
> **Which city is this?**

**Svar:** ✅ Rome · ⬜ Athens · ⬜ Carthage · ⬜ Babylon

**Ord:** *republic* — a country without a king; the people choose their leaders · *general* — a leader of soldiers · *civil war* — a war between people of the same country · *institution* — a rule or group of a country that lasts a long time, for example a court

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Empires end, ideas remain</summary>

> Empire X rules the lands around the Mediterranean Sea for centuries.  
> Then it ends, slowly, like all empires end.  
> But its language, Latin, does not die.  
> Latin grows into Italian, Spanish, Portuguese, French, and Romanian.  
> Its law shapes laws in many countries today.  
> One example: an accusation is not enough.  
> You must show that it is true.  
> Its concrete buildings still stand, like the Pantheon with its great round roof.  
> And it has a powerful idea: a conquered person can become a citizen.  
> So belonging is not only about family and blood.  
> It can also come from law.  
> Empires end, but ideas and words remain.  
> **Which empire is this?**

**Svar:** ✅ Rome · ⬜ Greece · ⬜ Egypt · ⬜ Persia

**Ord:** *accusation* — when someone says: this person did a bad thing · *concrete* — a building material, like liquid stone that becomes very hard · *conquered* — beaten in a war and taken over by the winners · *citizen* — a full member of a country, with rights and duties

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Fall or transformation?</summary>

> Empire X rules all the lands around the Mediterranean Sea, from west to east.  
> Then hard times come to the west: wars at the borders, plagues, and money problems.  
> The western half breaks apart, piece by piece.  
> Many people say: the empire falls.  
> But wait.  
> The eastern half lives on for about a thousand years.  
> Its rulers sit in Constantinople.  
> Its people still call themselves by the old empire's name.  
> Some historians say 'fall'.  
> Other historians say 'transformation'.  
> Each word teaches a different lesson.  
> You choose the lesson.  
> **Which empire is this?**

**Svar:** ✅ Rome · ⬜ The Ottoman Empire · ⬜ Persia · ⬜ Egypt

**Ord:** *border* — the line where one land ends and another land begins · *plague* — a sickness that spreads fast and kills many people · *historian* — a person who studies the past · *transformation* — a big, slow change from one form into another

</details>

### Julius Caesar

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Name in Everyday Words</summary>

> Mr X lives in Rome, a little more than 2,000 years ago.  
> He is a famous Roman leader.  
> He leads soldiers in many lands.  
> He writes books about what he sees and does there.  
> His adopted son later becomes the first emperor of Rome.  
> One month of the year gets his name: July.  
> His family name becomes the word for "emperor" in other languages.  
> Germans say "Kaiser".  
> Russians say "tsar".  
> People still use his name today, in everyday words.  
> **Who is Mr X?**

**Svar:** ✅ Julius Caesar · ⬜ Augustus · ⬜ Alexander the Great · ⬜ Hammurabi

**Ord:** *emperor* — like a king, but over many lands · *adopted* — an adopted son is not born in the family; the family takes him in as their child, by law

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A Year That Follows the Sun</summary>

> Look at a calendar.  
> It comes from Mr X.  
> Mr X is the leader of Rome, long ago.  
> The old Roman calendar is a mess.  
> Some powerful men add an extra month when it helps their friends.  
> So the months no longer fit the seasons.  
> Mr X asks an astronomer from Egypt for help.  
> The new calendar gets 365 days, and a leap day every four years.  
> Now the year follows the sun, not powerful men.  
> People later call it the Julian calendar.  
> Today, after one small change, most of the world uses this calendar.  
> **Who is Mr X?**

**Svar:** ✅ Julius Caesar · ⬜ Copernicus · ⬜ Augustus · ⬜ Leonardo da Vinci

**Ord:** *mess* — things in bad order; nothing is in its right place · *astronomer* — a scientist who studies the sun, the moon, and the stars · *leap day* — one extra day, 29 February; it comes every four years

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The River of No Return</summary>

> Rome is a republic, a state without a king.  
> One rule protects it.  
> A general may not bring his army into Italy without permission.  
> Mr X is a famous Roman general.  
> One winter day, he stands with his soldiers at a small border river.  
> The river's name is the Rubicon.  
> Old writers tell us that he says: "The die is cast."  
> He crosses.  
> Civil war follows, and he becomes ruler for life.  
> Even today, people say "crossing the Rubicon" about a step with no way back.  
> When one man breaks the rule that protects the state, the state changes forever.  
> **Who is Mr X?**

**Svar:** ✅ Julius Caesar · ⬜ Augustus · ⬜ Alexander the Great · ⬜ Hannibal

**Ord:** *republic* — a state without a king; the people choose their leaders · *general* — a leader of an army · *civil war* — a war between people of the same country · *the die is cast* — a die is a small cube for games; you throw it, and you cannot take the throw back

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Can Violence Save a Republic?</summary>

> Mr X rules Rome alone.  
> Rome is a republic, and Romans do not want a king.  
> He wears no crown, but he rules like a king.  
> Many senators fear him, even his friend Brutus.  
> One day, at a meeting of the senate, they kill him with daggers.  
> One old story tells us that he asks: "You too, my child?"  
> The killers say that they want to save the republic.  
> But the killing brings new wars, Roman against Roman.  
> In the end, the republic dies anyway.  
> His heir, Augustus, wins and becomes the first emperor.  
> Violence almost never builds the future that people plan.  
> **Who is Mr X?**

**Svar:** ✅ Julius Caesar · ⬜ Alexander the Great · ⬜ Socrates · ⬜ Gandhi

**Ord:** *senate* — a group of powerful men who guide the Roman state; the men in this group are senators · *republic* — a state without a king; the people choose their leaders · *heir* — the person who gets your money and property after your death · *emperor* — like a king, but over many lands

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Hero of His Own Story</summary>

> Mr X is a Roman general and politician.  
> He wins a long war in Gaul, in the north.  
> He writes the report of the war himself.  
> In the book, he writes his own name, not "I".  
> He sounds like a calm reporter: Mr X hurries, Mr X decides, Mr X wins.  
> His face appears on coins while he is still alive.  
> No living Roman does this before him.  
> He takes the job of dictator, an emergency job for six months.  
> He keeps the job until he dies.  
> We know about the war mostly from his own book.  
> Source criticism asks: who writes this, and why?  
> **Who is Mr X?**

**Svar:** ✅ Julius Caesar · ⬜ Augustus · ⬜ Alexander the Great · ⬜ Marx

**Ord:** *dictator* — in Rome, a leader who gets all power alone, for a short time, in an emergency · *emergency* — a sudden time of danger · *source* — a text or an object that gives us information about the past · *source criticism* — asking who makes a source, and why, before you trust it

</details>

### Konfucius

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A School for Rich and Poor</summary>

> Master X lives in China about 2,500 years ago.  
> He is a teacher.  
> He takes any student who really wants to learn.  
> Rich or poor - it does not matter.  
> A small gift of dried meat is enough, he says.  
> That is his school fee.  
> He teaches kindness, honesty, and respect for parents and old people.  
> Why does he take poor students too?  
> Because everyone can learn to be good, he believes.  
> People still learn from him today.  
> **Who is Master X?**

**Svar:** ✅ Confucius · ⬜ Buddha · ⬜ Socrates · ⬜ Plato

**Ord:** *school fee* — money or a gift you give so you can learn at a school · *kindness* — being good and friendly to other people · *honesty* — telling the truth · *respect* — you show that a person is important to you

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — One Rule for Life</summary>

> Master X is a teacher in China, long ago.  
> A student asks him a question.  
> - Is there one rule for the whole of life?  
> - Yes, Master X says.  
> - Do not do to other people what you do not want them to do to you.  
> Today, people call this the golden rule.  
> People in many cultures teach this same rule.  
> Master X starts with everyday life: how we treat each other.  
> Being good starts at home, with your family, he says.  
> Then it grows: to the village, the town, the world.  
> **Who is Master X?**

**Svar:** ⬜ Buddha · ✅ Confucius · ⬜ Socrates · ⬜ Aristotle

**Ord:** *golden rule* — a famous rule: treat other people as you want them to treat you - Master X says it with a 'do not' · *culture* — the way of life of a group of people · *treat* — how you act toward a person, good or bad

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Lead by Good Example</summary>

> Master X teaches in China, about 2,500 years ago.  
> Some rulers ask him for advice.  
> - Lead by good example, he says.  
> - Care for the people like a good parent.  
> - Do not rule through fear and hard punishment.  
> - If the ruler is honest, the people become honest.  
> - Choose officials who study and live honestly.  
> - Do not choose them because they are born into powerful families.  
> Few rulers listen to him.  
> But many centuries later, China chooses its officials with big examinations.  
> Can a test find a good heart too?  
> **Who is Master X?**

**Svar:** ⬜ Plato · ✅ Confucius · ⬜ Buddha · ⬜ Marx

**Ord:** *official* — a person who does work for the country and its ruler · *punishment* — trouble you get when you break a rule · *examination* — a big, important test · *honest* — you say what is true; you do not lie or cheat

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The Glue of Society</summary>

> Master X lives in China, long ago.  
> He teaches "li" - the polite forms of daily life.  
> How to greet, how to eat together, how to speak with old people.  
> For him, these small forms are the glue of society.  
> They show respect, and respect holds people together.  
> He does not talk much about gods.  
> He talks about how people live together.  
> But some people ask questions.  
> - Does so much respect for old people stop new ideas?  
> - May a student question the teacher?  
> People can respect a tradition and still ask questions about it.  
> **Who is Master X?**

**Svar:** ⬜ Socrates · ⬜ Buddha · ✅ Confucius · ⬜ Gandhi

**Ord:** *li* — a Chinese word for polite ways to do things, like greeting or eating together · *glue* — a sticky material that holds things together; here: what holds people together · *society* — all the people who live together in a country or group · *tradition* — old ways that pass from parents to children

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Long Life of Ideas</summary>

> Master X is a teacher in China, long ago.  
> Like Socrates in Greece, he writes no book himself.  
> Much later, his students and their students collect his sayings.  
> This little book of sayings carries his voice through time.  
> He teaches about family, respect, and good rulers.  
> Centuries after his death, China's rulers choose his teaching.  
> They follow it for about 2,000 years.  
> Then times change.  
> Modern reformers say his ideas are old-fashioned.  
> Today, people study him and show him respect again.  
> Ideas are like tools: each new time uses them for its own questions.  
> **Who is Master X?**

**Svar:** ⬜ Plato · ⬜ Buddha · ⬜ Marx · ✅ Confucius

**Ord:** *sayings* — short wise sentences that a person says · *century* — a time of one hundred years · *reformer* — a person who wants to change the old ways · *old-fashioned* — from an old time; not fitting the new time

</details>

### Siddhartha Gautama

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The prince who leaves the palace</summary>

> His followers tell this story about Prince X.  
> Long ago, a prince lives in a palace near the Himalaya mountains.  
> His father hides everything sad from him.  
> One day, the prince rides outside the palace walls.  
> He sees an old man, a sick man, and a dead man.  
> - Why do people suffer? he asks.  
> He also sees a calm holy man with no home.  
> He leaves the palace to understand suffering.  
> At last, he sits under a big fig tree and thinks deeply.  
> From that day, people call him "the awakened one".  
> His teaching, in simple words: do not hide from sad things.  
> Try to understand them.  
> **Who is Prince X?**

**Svar:** ✅ Siddhartha Gautama · ⬜ Alexander the Great · ⬜ Confucius · ⬜ Gandhi

**Ord:** *palace* — a very big and rich house for a king's family · *suffer* — to feel pain in the body or the heart · *fig tree* — a tree with fig fruits. The tree in this story has heart-shaped leaves. · *awakened* — awake, not asleep. Here it means: a person who sees life clearly.

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Not too much, not too little</summary>

> Prince X lives long ago, in what is now Nepal and India.  
> The old stories tell us: as a young man he has every luxury.  
> Fine food, music, soft beds - but they do not make him happy.  
> The stories go on: he tries the opposite and eats almost nothing.  
> He almost dies, and he finds no answer.  
> So he chooses a middle way.  
> Live simply, hurt no one, train a calm and clear mind.  
> His teaching starts with an honest look at life.  
> Suffering is real, it has causes, and there is a way to end it.  
> One big cause, he says, is that we always want more.  
> Not too much, not too little - people still find this idea wise today.  
> **Who is Prince X?**

**Svar:** ✅ Siddhartha Gautama · ⬜ Confucius · ⬜ Socrates · ⬜ Gandhi

**Ord:** *luxury* — many fine and expensive things · *opposite* — the other side of something. Hot is the opposite of cold. · *suffering* — pain in the body or the heart

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A quiet revolution</summary>

> Prince X lives in India, about 2,500 years ago.  
> In his land, people are born into fixed groups.  
> These groups are called castes.  
> Priests say they are the highest group.  
> Prince X becomes a teacher.  
> He teaches the same way to everyone: farmers, barbers, kings.  
> - What you do matters more than the group you are born in, he says.  
> His followers say that a poor barber becomes one of his best students.  
> Women also join him and become nuns.  
> At this time, few teachers accept women as students.  
> It is a quiet revolution: change through ideas, not weapons.  
> **Who is Prince X?**

**Svar:** ✅ Siddhartha Gautama · ⬜ Confucius · ⬜ Gandhi · ⬜ Mandela

**Ord:** *caste* — a fixed group of people. You are born into it. · *priest* — a person who leads people in their religion · *nun* — a woman who lives a simple religious life · *revolution* — a big change in how people live or think

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — An idea travels without an army</summary>

> Prince X lives in India, long ago.  
> Old stories say he leaves his palace to find answers.  
> Later, he becomes a teacher.  
> He teaches peace and a calm mind.  
> Long after his death, the emperor Ashoka rules India.  
> After a terrible war, Ashoka is full of regret.  
> He gives up new conquests.  
> He sends teachers to many lands.  
> Over hundreds of years, the teaching of Prince X travels the trade roads.  
> It reaches Sri Lanka, then China, Japan, and Southeast Asia.  
> In each land, it takes a new form: new art, new temples.  
> Ideas can travel farther than any sword.  
> **Who is Prince X?**

**Svar:** ✅ Siddhartha Gautama · ⬜ Alexander the Great · ⬜ Confucius · ⬜ Marx

**Ord:** *emperor* — a ruler of many lands and peoples · *conquest* — taking land from others by war · *regret* — a sad feeling about something you did · *trade road* — a road that people use to carry things to sell, from land to land

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Living books</summary>

> Prince X teaches in India long ago, but he writes nothing down.  
> For about four hundred years, monks learn his words by heart.  
> They recite the texts together, in groups.  
> If one monk makes a mistake, the others hear it and correct it.  
> They work like living books.  
> Then monks in Sri Lanka write the oldest full collection on palm leaves.  
> The leaves grow old, so monks copy them again and again.  
> Scholars today compare old copies to find his real words.  
> One part of his training of the mind is called mindfulness.  
> Hospitals around the world now use it to help people with stress and pain.  
> An old idea lives on: first in memory, then on leaves, now in hospitals.  
> **Who is Prince X?**

**Svar:** ✅ Siddhartha Gautama · ⬜ Socrates · ⬜ Confucius · ⬜ Aristotle

**Ord:** *monk* — a man who lives a simple religious life in a group · *recite* — to say a text aloud from memory · *scholar* — a person who studies a subject very deeply · *mindfulness* — training to notice calmly what happens in your mind and body right now

</details>

### Antikens Grekland

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Mountains, islands, and the sea</summary>

> Land X lies in the south of Europe.  
> It has high mountains and hundreds of islands.  
> The warm blue sea is never far away.  
> The soil is thin, but olive trees and grapes grow well.  
> Many people become fishers, sailors, and traders.  
> Long ago, the land has no single king.  
> Instead, people live in many small city-states.  
> These cities are proud, and they often compete with each other.  
> In the middle of the city lies the agora, a busy market square.  
> People meet there, buy food, and talk about the news.  
> High on a rock over one famous city, a white marble temple still stands today.  
> **Which land is this?**

**Svar:** ⬜ Egypt · ✅ Greece · ⬜ Rome · ⬜ Phoenicia

**Ord:** *soil* — the earth on the ground where plants grow · *city-state* — a city with its own laws and leaders, like a small country · *agora* — the open market square in the middle of the city · *marble* — a hard, shiny stone for fine buildings

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The people rule</summary>

> About 2,500 years ago, one city-state in Land X tries a new idea.  
> The free men of the city meet on a hill.  
> They talk, and then they vote by raising their hands.  
> They decide about laws, money, war, and peace.  
> Many city jobs go by lot, like names from a hat.  
> The people call this demokratia - 'the people rule'.  
> Our word 'democracy' comes from this.  
> But most people in the city cannot vote.  
> Women cannot vote, and neither can slaves or people from other cities.  
> So this democracy is a start, not the finish.  
> Today, many lands build on the idea, and more people can vote.  
> **Which land is this?**

**Svar:** ⬜ Rome · ⬜ Egypt · ✅ Greece · ⬜ Mesopotamia

**Ord:** *vote* — to say your choice when a group decides something · *by lot* — chosen by chance, like pulling a name from a hat · *slave* — a person who is not free and is owned by another person · *democracy* — the people rule: the people of a land decide together

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The theater on the hillside</summary>

> About 2,500 years ago, the people of Land X build the first great theaters.  
> First people sit on wooden benches.  
> Later they cut half-circles of stone seats into their hillsides.  
> Some theaters hold more than ten thousand people.  
> The actors wear masks with big, clear faces.  
> So people far up on the hill can still see who is sad or angry.  
> A sad play is a tragedy: it shows great people who fall through their own mistakes.  
> A funny play is a comedy: it laughs at the rich and powerful.  
> The plays ask big questions.  
> What is right, what is fair, and who decides?  
> Thousands of people watch together and feel together.  
> Our words 'theater', 'drama', 'tragedy', and 'comedy' come from the language of Land X.  
> **Which land is this?**

**Svar:** ✅ Greece · ⬜ Rome · ⬜ Egypt · ⬜ Mesopotamia

**Ord:** *mask* — a false face you wear over your own face · *tragedy* — a serious, sad play · *comedy* — a funny play · *actor* — a person who plays someone else in a play

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Frogs around a pond</summary>

> In old times, Land X is not one country.  
> It is hundreds of proud city-states, and they often quarrel.  
> Two of them are famous opposites.  
> One famous city loves ships, trade, and open talk.  
> Its rival loves order, simple food, and hard training.  
> Yet all these cities feel like one people.  
> They speak one language and honor the same gods.  
> They share the same stories about gods and heroes.  
> Many cities also send ships out and start colonies.  
> These new towns grow on coasts from Spain to the Black Sea.  
> A famous thinker from Land X writes: we live around the sea like frogs around a pond.  
> **Which land is this?**

**Svar:** ⬜ Phoenicia · ⬜ Egypt · ✅ Greece · ⬜ Rome

**Ord:** *city-state* — a city with its own laws and leaders, like a small country · *quarrel* — to argue and fight with each other · *honor* — to show great respect for someone · *colony* — a new town that people from a city build in a faraway land

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The white marble dream</summary>

> Historians ask: how do we know the story of Land X?  
> Its old books - plays, science, and philosophy - survive only as copies of copies.  
> For centuries, scribes in Constantinople copy them, and scholars in Baghdad translate many science and philosophy books into Arabic.  
> Without this long work, most of the old books are gone today.  
> The white marble ruins tell only half the truth, too.  
> New research shows: long ago, the temples and statues shine with bright colors.  
> Later ages love the bare white stone and dream of a pure, perfect Land X.  
> But real life there includes slavery and long wars between the cities.  
> So historians see two lands: the real one, and the beautiful dream.  
> Both of them shape our world today.  
> **Which land is this?**

**Svar:** ⬜ Rome · ⬜ Egypt · ⬜ Mesopotamia · ✅ Greece

**Ord:** *philosophy* — the study of big questions about life and thinking · *scribe* — a person whose work is copying books by hand · *ruin* — a broken old building

</details>

### De olympiska spelen

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A crown of olive leaves</summary>

> Games X take place in Greece, long ago.  
> They happen every four years, at one holy place.  
> People travel there from many Greek towns.  
> They watch runners, wrestlers, and jumpers.  
> The stadium has room for many thousands of people.  
> The winner gets no gold and no money.  
> He gets a crown of leaves from a holy olive tree.  
> At home, people greet the winner like a hero.  
> The games go on for more than a thousand years.  
> Today, the biggest games in the world carry the same name.  
> **Which games are these?**

**Svar:** ⬜ The Roman gladiator games · ✅ The Olympic Games · ⬜ The Pythian Games · ⬜ The Panathenaic Games

**Ord:** *holy* — very special for a god or a religion · *wrestler* — a sports person who tries to bring another person to the ground, without hitting · *stadium* — a big place for sport, with room for many watchers · *crown* — a ring that you wear on your head

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The holy peace</summary>

> In Greece, long ago, the towns often fight each other.  
> But every four years, something special happens.  
> Messengers walk from town to town.  
> They call out: Games X start soon!  
> Games X are the oldest and greatest games in Greece.  
> They honor the king of the Greek gods.  
> Now a holy peace begins.  
> Everyone who travels to the games must be safe.  
> Athletes and visitors walk through enemy land, and no one may harm them.  
> At the games, enemies compete in sport, not in war.  
> For a short time, sport brings the Greek world together.  
> **Which games are these?**

**Svar:** ⬜ The Panathenaic Games · ⬜ The Pythian Games · ✅ The Olympic Games · ⬜ The Isthmian Games

**Ord:** *messenger* — a person who carries news from place to place · *holy* — very special for a god or a religion · *athlete* — a person who does sport, for example a runner · *compete* — to try to win against others

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Win with honor</summary>

> Games X take place at a holy place in Greece, every four years.  
> The oldest event is simple: a short, fast run across the stadium.  
> Later come wrestling, the long jump, and the discus throw.  
> Before the games, every athlete swears an oath: I follow the rules.  
> A cheater must pay money.  
> The money pays for statues on the way into the stadium.  
> The statues warn every new athlete: win with honor.  
> The Greeks believe: a strong body and a sharp mind belong together.  
> But the games are not open to everyone.  
> Only free Greek men may compete.  
> Girls hold their own races for a goddess, at the same holy place.  
> **Which games are these?**

**Svar:** ✅ The Olympic Games · ⬜ The Isthmian Games · ⬜ The Nemean Games · ⬜ The Pythian Games

**Ord:** *oath* — a very serious promise · *cheater* — a person who breaks the rules to win · *discus* — a flat, round, heavy plate that athletes throw far · *honor* — when people see you as good and fair

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The games wake up again</summary>

> Games X begin in Greece, almost 3,000 years ago.  
> Athletes meet there every four years, for more than a thousand years.  
> Then new rulers come, with a new religion.  
> They do not like festivals for the old gods. Slowly, the games stop.  
> For about 1,500 years, there are no games.  
> At the end of the 1800s, a man in France gets a big idea.  
> His big idea: let the young people of the world meet in sport, not in war.  
> So the games wake up again — now for the whole world.  
> A new city hosts them every four years.  
> Now women compete too.  
> Today, before the games begin, a flame travels from the old place in Greece to the new stadium.  
> **Which games are these?**

**Svar:** ⬜ The Panathenaic Games · ⬜ The Pythian Games · ✅ The Olympic Games · ⬜ The Isthmian Games

**Ord:** *religion* — belief in a god or gods, with its own rules and feasts · *festival* — a big feast or celebration for many people · *host* — to hold the games in your own city · *flame* — the bright, burning part of a fire

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Lists, a traveler, and a buried stadium</summary>

> How do we know about Games X in old Greece?  
> First: lists.  
> Greek writers keep long lists of the winners.  
> Later historians even count time with these games: four years, from games to games.  
> Second: a traveler.  
> About 1,800 years ago, a travel writer visits the holy place and describes its temples and statues.  
> Third: the ground.  
> Rivers and earthquakes bury the old place under sand and earth.  
> In the 1800s, archaeologists start to dig it out: the temples and stones with the winners' names. Later they also uncover the stadium.  
> One warning: many people say that all wars stop during the games.  
> The sources show less: a holy peace protects the travelers, but wars go on in other places.  
> **Which games are these?**

**Svar:** ⬜ The Pythian Games · ⬜ The Panathenaic Games · ⬜ The Nemean Games · ✅ The Olympic Games

**Ord:** *source* — an old text or thing that gives us knowledge about the past · *earthquake* — when the ground shakes strongly · *bury* — to cover something with earth or sand · *archaeologist* — a person who digs in the ground to find things from the past

</details>

### Augustus

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Boy with a Powerful Name</summary>

> Mr X lives in Rome, about 2,000 years ago.  
> He is only eighteen when his famous great-uncle dies.  
> The great-uncle is Rome's most famous leader.  
> In his will, the great-uncle adopts Mr X as his son.  
> Suddenly, the young man carries a very powerful name.  
> Many older men think: he is only a boy.  
> But Mr X is patient and careful.  
> After many hard years, he becomes the first emperor of Rome.  
> He rules for more than forty years, and Rome has peace.  
> One month of the year gets his name: August.  
> **Who is Mr X?**

**Svar:** ⬜ Julius Caesar · ✅ Augustus · ⬜ Nero · ⬜ Alexander the Great

**Ord:** *great-uncle* — the brother of your grandmother or grandfather · *will* — a paper that says who gets your money and things after your death · *adopt* — to take a child into your family as your own child, by law · *emperor* — like a king, but over many lands

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — From Brick to Marble</summary>

> For many years, Romans fight Romans in civil wars.  
> Then one man wins, and the fighting stops.  
> He becomes Emperor X, the first emperor of Rome.  
> A long time of peace begins.  
> People later call it Pax Romana - the Roman Peace.  
> Farmers can work, and traders can travel safely again.  
> The emperor repairs old temples and builds many new buildings.  
> An old writer tells us his words: "I find Rome a city of brick. I leave it a city of marble."  
> The peace lasts, with few breaks, for about two hundred years.  
> His long peace makes Rome richer than any war.  
> **Who is Emperor X?**

**Svar:** ⬜ Julius Caesar · ⬜ Constantine · ⬜ Alexander the Great · ✅ Augustus

**Ord:** *civil war* — a war between people of the same country · *trader* — a person who buys and sells things · *brick* — a small building block of baked clay · *marble* — a fine, shiny stone for beautiful buildings

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Power without a Crown</summary>

> The people of Rome hate the word "king".  
> Long ago, they throw their kings out.  
> Mr X knows this well.  
> He rules Rome alone, but he never takes the title of king.  
> He wears no crown.  
> He calls himself "princeps" - the first citizen.  
> Elections and the old jobs continue, like before.  
> But Mr X keeps control of the army and the money.  
> He says that he gives the republic back to the senate and the people.  
> He rules like this for more than forty years and dies as an old man.  
> Words can hide power as well as show it.  
> **Who is Mr X?**

**Svar:** ✅ Augustus · ⬜ Julius Caesar · ⬜ Nero · ⬜ Constantine

**Ord:** *title* — an official name for a person's job or rank · *princeps* — a Latin word: the first citizen, the first man of the state · *senate* — a group of powerful men who guide the Roman state · *republic* — a state without a king; the people choose their leaders

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The Face That Never Grows Old</summary>

> Emperor X is the first emperor of Rome, and he rules for a long time.  
> Everywhere in the empire, people see his face.  
> In city after city, statues show him young, calm, and strong.  
> He grows old, but his statues never do.  
> Coins travel through the whole empire, and his face travels with them.  
> Great poets write that a new golden age begins with him.  
> One famous poem says that the gods choose Rome to rule the world.  
> The emperor and his rich friends support these poets.  
> Is this art, or is it advertising for one man?  
> Today we have a word for it: propaganda - pictures and words that build power.  
> **Who is Emperor X?**

**Svar:** ⬜ Julius Caesar · ⬜ Alexander the Great · ✅ Augustus · ⬜ Nero

**Ord:** *statue* — a figure of a person, made of stone or metal · *golden age* — a very good and happy time · *advertising* — pictures and words that try to sell something · *propaganda* — pictures, words, and art that try to control what people think

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Carved in Stone</summary>

> Near the end of his long life, Emperor X writes a short report about himself.  
> The title means: "The things I did".  
> After his death, workers carve the text in stone in cities across the empire.  
> One big copy survives on a temple wall in today's Turkey.  
> In the text, the first emperor of Rome counts his buildings, his gifts, and his honors.  
> He writes that he saves the state and refuses to be a dictator.  
> He does not name his old enemies, and he does not mention his mistakes.  
> For historians, the text is a treasure: facts from the ruler himself.  
> But it is also a story with one storyteller - the main person himself.  
> So historians compare it with coins, ruins, and other writers.  
> Every source answers the question: who speaks, and who is silent?  
> **Who is Emperor X?**

**Svar:** ⬜ Julius Caesar · ⬜ Hammurabi · ⬜ Constantine · ✅ Augustus

**Ord:** *carve* — to cut letters or pictures into stone or wood · *dictator* — in Rome, a leader who gets all power alone, for a short time, in an emergency · *historian* — a person who studies the past · *source* — a text or an object that gives us information about the past

</details>

### Jesus från Nasaret

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The carpenter's son</summary>

> Mr X lives about 2,000 years ago.  
> He grows up in a small, quiet village.  
> His father is a carpenter, and Mr X learns to work with wood too.  
> As a grown man, he becomes a teacher.  
> He walks from village to village near a big lake.  
> Fishermen leave their boats to hear him.  
> He teaches with short stories from everyday life.  
> One story is about a shepherd who looks for one lost sheep.  
> The shepherd does not rest until he finds it.  
> Every person matters, the story says.  
> People all over the world still tell his stories today.  
> **Who is Mr X?**

**Svar:** ⬜ Buddha · ✅ Jesus · ⬜ Muhammad · ⬜ Moses

**Ord:** *carpenter* — a person who builds things from wood · *fisherman* — a person who catches fish · *shepherd* — a person who takes care of sheep

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Love your enemies too</summary>

> Mr X is a teacher who lives about 2,000 years ago.  
> Crowds follow him from village to village and up a green hillside.  
> - Love your neighbor as yourself, he teaches.  
> And he goes further: love your enemies too, he teaches.  
> He also teaches forgiveness: do not pay back a bad thing with a bad thing.  
> Forgive - not once, but again and again, he says.  
> And he gives one simple rule for daily life:  
> - Do to other people what you want them to do to you.  
> People later call this the golden rule.  
> Easy to say, hard to do - then and now.  
> **Who is Mr X?**

**Svar:** ⬜ Moses · ⬜ Buddha · ✅ Jesus · ⬜ Muhammad

**Ord:** *neighbor* — a person who lives near you; here it means every other person · *enemy* — a person who is against you · *forgiveness* — you stop being angry with a person who did a bad thing to you · *golden rule* — a famous rule: treat other people as you want them to treat you; Mr X says it with a 'do', not a 'do not'

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The good stranger</summary>

> Mr X is a famous teacher, about 2,000 years ago.  
> He answers big questions with small stories, called parables.  
> A man asks him: who is my neighbor?  
> Mr X answers with a parable.  
> A traveler is robbed and lies hurt by the road.  
> Two respected men see him - and walk past.  
> Then a foreigner stops, a man from a group that many people look down on.  
> He cleans the traveler's wounds, puts him on his own donkey, and pays for his care.  
> - Who is the neighbor in the story? Mr X asks.  
> The listener must find the answer himself: the one who helps.  
> A rule is easy to forget, but a good story stays with you.  
> **Who is Mr X?**

**Svar:** ✅ Jesus · ⬜ Socrates · ⬜ Buddha · ⬜ Muhammad

**Ord:** *parable* — a short story with a lesson inside · *foreigner* — a person from another land or group · *wound* — a hurt place on the body · *look down on* — to think that a person is less important

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The year on the calendar</summary>

> Mr X lives about 2,000 years ago, in a land ruled by Rome.  
> He is a teacher with a small group of followers.  
> The Roman rulers see him as a danger, and he is put to death.  
> But his followers do not give up.  
> His followers believe that he rises from death.  
> This faith makes them brave, and they carry his teaching from land to land.  
> Today, his followers form the largest religion in the world.  
> Our calendar counts the years from his birth.  
> But the monk who works out his birth year, many centuries later, makes a small mistake.  
> So Mr X is probably born a few years 'before' year one!  
> **Who is Mr X?**

**Svar:** ⬜ Muhammad · ⬜ Julius Caesar · ✅ Jesus · ⬜ Buddha

**Ord:** *follower* — a person who believes in a teacher and lives by his words · *faith* — a strong belief in a religion · *calendar* — the way we count and name days and years · *monk* — a man who lives a simple, religious life

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — How do we know?</summary>

> Mr X is a teacher who lives about 2,000 years ago.  
> He writes no book himself.  
> So how do we know about him?  
> Decades after his death, his followers write four short books about his life.  
> The writers are believers, not neutral reporters.  
> Old Roman and Jewish historians also mention him, in a few short lines.  
> Because of this, almost all historians agree: the man is real.  
> He teaches, he gathers followers, and he is put to death by Roman power.  
> Believers say much more: for them, he is the Son of God.  
> History cannot prove such faith, and it cannot show it is wrong.  
> Historians and believers read the same old pages - with different questions.  
> **Who is Mr X?**

**Svar:** ⬜ Socrates · ⬜ Muhammad · ⬜ Buddha · ✅ Jesus

**Ord:** *decade* — a time of ten years · *believer* — a person who belongs to a religion · *neutral* — not taking any side · *historian* — a person who studies the past

</details>

### Muhammed

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Trader and the Quiet Cave</summary>

> Mr X lives in Arabia, about 1,400 years ago.  
> His town, Mecca, is a busy trading town in the desert.  
> Camel caravans stop there on long journeys.  
> Mr X works as a trader.  
> People trust him with their goods and money.  
> He often goes to a quiet cave in the mountains to think.  
> Muslims believe that an angel speaks to him there.  
> The angel brings him messages from God, Muslims believe.  
> Mr X starts to teach these messages to others.  
> Today, almost two billion people follow his message.  
> They are called Muslims.  
> **Who is Mr X?**

**Svar:** ⬜ Jesus · ⬜ Buddha · ✅ Muhammad · ⬜ Moses

**Ord:** *trader* — a person who buys and sells things · *caravan* — a group of people and animals that travel together · *cave* — a big hole in a rock or mountain · *angel* — a messenger from God, in many religions

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A New Start in a New Town</summary>

> Mr X is a teacher in Arabia, about 1,400 years ago.  
> As an adult, he begins to teach.  
> His message is simple and strong.  
> - There is only one God, he teaches.  
> - Care for the poor and protect orphans.  
> - Be fair when you buy and sell.  
> Rich leaders in his hometown, Mecca, do not like this message.  
> They make life hard for him and his followers.  
> So he moves to another town, Medina.  
> There, his followers become a strong community: the umma.  
> This new start is so important that the Muslim calendar begins in that year.  
> **Who is Mr X?**

**Svar:** ✅ Muhammad · ⬜ Moses · ⬜ Jesus · ⬜ Buddha

**Ord:** *orphan* — a child whose mother and father are dead · *follower* — a person who believes in a teacher and follows him · *community* — a group of people who live together and help each other · *umma* — an Arabic word for the community of all Muslims

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A Book to Learn by Heart</summary>

> Mr X lives in Arabia, about 1,400 years ago.  
> He brings his people a message in Arabic, in beautiful and powerful language.  
> Muslims believe that the words come from God.  
> Mr X speaks the words out loud to the people.  
> His followers learn them by heart.  
> They recite them: they say them from memory, again and again.  
> These words become the Quran, the holy book of Islam.  
> The name Quran means "the recitation".  
> After the death of Mr X, his followers collect all the words in one book.  
> Today, Muslims all over the world read it in Arabic.  
> Many learn the whole book by heart.  
> **Who is Mr X?**

**Svar:** ⬜ Martin Luther · ⬜ Jesus · ✅ Muhammad · ⬜ Buddha

**Ord:** *recite* — to say a text out loud from memory · *by heart* — from memory, without reading · *holy* — very special and important in a religion · *Arabic* — the language of Arabia, spoken in many countries today

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — From the Desert to a World of Knowledge</summary>

> Mr X is a teacher in Arabia, about 1,400 years ago.  
> His message unites many desert tribes into one community.  
> After his death, this message travels far and fast.  
> Within one century, it reaches from Spain in the west to the river Indus in the east.  
> In this big new world, trade and learning grow.  
> Scholars translate old books from Greek, Persian, and Indian thinkers.  
> In the city of Baghdad, a famous library is called the House of Wisdom.  
> Scholars there work on algebra, astronomy, and medicine.  
> The word "algebra" comes from Arabic.  
> Even our numbers, 1, 2, 3, come to Europe through this world.  
> A message in the desert opens a new world of knowledge.  
> **Who is Mr X?**

**Svar:** ⬜ Alexander the Great · ✅ Muhammad · ⬜ Genghis Khan · ⬜ Jesus

**Ord:** *tribe* — a big group of families with one leader · *scholar* — a person who studies and knows very much · *algebra* — a part of mathematics; it uses letters for unknown numbers · *astronomy* — the study of stars and planets

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — How Do Historians Know?</summary>

> Mr X lives in Arabia, about 1,400 years ago.  
> How do historians know about his life?  
> The oldest source is the Quran, the holy book of Islam.  
> But it says little about the events of his life.  
> Stories about his words and actions are called hadith.  
> For generations, people pass these stories on, from teacher to student.  
> Only later do scholars write them down in big collections.  
> Muslim scholars check every story: who tells it, and who heard it from whom?  
> Modern historians ask the same kind of questions about all old sources.  
> Some pages of the Quran that still exist today are very, very old.  
> **Who is Mr X?**

**Svar:** ⬜ Socrates · ⬜ Jesus · ⬜ Buddha · ✅ Muhammad

**Ord:** *source* — a text or thing from the past that gives us knowledge · *hadith* — a story about the words or actions of Mr X · *generation* — parents are one generation; their children are the next · *collection* — many things gathered together in one book or place

</details>

### Bysantinska riket

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The city between two seas</summary>

> Empire X is a Christian empire with a capital city between two seas.  
> The city sits where Europe meets Asia.  
> Water protects it on two sides.  
> On the land side, the people build two strong walls, one behind the other.  
> For many centuries, no enemy army can break through these land walls.  
> Ships from many lands fill the city's great harbor.  
> Traders bring silk from the east and furs from the north.  
> Trade roads from Asia and Europe meet in this city.  
> Inside the walls, churches shine with pictures made of small golden stones.  
> People call these pictures mosaics.  
> Travelers say: no city on earth is richer.  
> **Which empire is this?**

**Svar:** ⬜ Egypt · ⬜ Rome · ✅ The Byzantine Empire · ⬜ The Ottoman Empire

**Ord:** *capital* — the main city of a land, where the ruler lives · *harbor* — a safe place by the water where ships can stop · *silk* — a fine, soft cloth that costs very much, first made in China · *mosaic* — a picture made of many small colored stones

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The dome that seems to float</summary>

> Empire X is a Christian empire in the east.  
> In its capital stands a very famous building.  
> The emperor wants a church greater than any other church.  
> Workers finish it in only five years, about 1,500 years ago.  
> Its giant dome seems to float in the air.  
> Light falls in through a ring of windows under the dome.  
> An old story says the emperor cries out: I have built something greater than the greatest temple!  
> For about 900 years, the building is a church.  
> Then new rulers take the city, and the church becomes a mosque.  
> Much later it becomes a museum, and today it is a mosque again.  
> One building tells the long story of its city.  
> **Which empire is this?**

**Svar:** ✅ The Byzantine Empire · ⬜ Greece · ⬜ The Ottoman Empire · ⬜ Egypt

**Ord:** *dome* — a round roof, like the top half of a ball · *emperor* — the ruler of an empire · *mosque* — a building where Muslims pray · *museum* — a building where people can look at old and important things

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A thousand years of laws</summary>

> About 1,500 years ago, an emperor rules Empire X from a rich city in the east.  
> His empire still uses the laws of old Rome.  
> But after a thousand years, the laws are a mess.  
> There are too many laws, and some laws say opposite things.  
> So the emperor calls a team of law experts.  
> Their job: read everything, and sort the good rules into clear books.  
> The team also writes a small first book for new law students.  
> Empires end, but these law books survive.  
> Many centuries later, law schools in Europe study them again.  
> Today, the laws of many countries still stand on this old foundation.  
> Good laws can live longer than the lands that write them.  
> **Which empire is this?**

**Svar:** ⬜ Persia · ⬜ Rome · ⬜ Egypt · ✅ The Byzantine Empire

**Ord:** *mess* — many things mixed up, without order · *expert* — a person who knows very much about one thing · *opposite* — totally different; the other way around · *foundation* — the strong part under a building; here: the base that something stands on

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A bridge of books</summary>

> The people of Empire X speak Greek, and they guard the old books of Greece.  
> For about a thousand years, scribes copy these books by hand, page by page.  
> Plays, poems, science, and philosophy survive this way.  
> The empire also argues about holy pictures.  
> For a time, the emperors even forbid them.  
> Later, the pictures come back.  
> About 600 years ago, an army from a new empire takes the capital.  
> Many scholars flee west, to Italy.  
> In their bags are old Greek books.  
> In Italy, people are hungry for old knowledge.  
> The old books feed this new age of art and learning: the Renaissance.  
> **Which empire is this?**

**Svar:** ⬜ Rome · ✅ The Byzantine Empire · ⬜ The Ottoman Empire · ⬜ Persia

**Ord:** *scribe* — a person whose work is to copy books by hand · *scholar* — a person who studies and knows very much · *philosophy* — thinking hard about life, truth, and right and wrong · *Renaissance* — a time in Europe when art and learning grow fast; the word means 'rebirth'

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Who names the past?</summary>

> Here is a strange fact: Empire X never hears its own modern name.  
> Its people call themselves Romans, in the Greek language.  
> Their neighbors in the west call them Greeks.  
> The empire lives long, but one day it falls.  
> About a hundred years later, a scholar in the west prints a book about its history.  
> He needs a name, so he uses the capital's very old Greek name.  
> His new name wins: today, history books all over the world use it.  
> Why not simply say Romans?  
> In the west, kings and popes keep that name for themselves.  
> Names in history are not neutral: someone chooses them, later, and for a reason.  
> So ask: who names the past?  
> **Which empire is this?**

**Svar:** ⬜ The Ottoman Empire · ⬜ Persia · ⬜ Egypt · ✅ The Byzantine Empire

**Ord:** *scholar* — a person who studies and knows very much · *print* — to make many copies of a book with a machine · *neutral* — not taking any side

</details>

### Vikingarna

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Ships for sea and river</summary>

> The X people live in the cold north of Europe, about 1,000 years ago.  
> Most of them are farmers and fishers.  
> But they are also great sailors.  
> They build long, fast ships of wood.  
> The bottom of the ship is almost flat.  
> So the ship can cross the deep sea, and it can also sail up shallow rivers.  
> The sailors can even pull the ship up on a beach.  
> With these ships, the X people travel very far.  
> Some travel to trade, and some travel to rob other lands.  
> Today, you can see some of their real ships in museums.  
> **Who are the X people?**

**Svar:** ⬜ The Romans · ✅ The Vikings · ⬜ The Phoenicians · ⬜ The Greeks

**Ord:** *sailor* — a person who travels and works on a ship · *shallow* — not deep · *trade* — to buy and sell things · *rob* — to take things from people with force

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — East to the big city</summary>

> The X people live in the north of Europe, about 1,000 years ago.  
> Many of them are traders.  
> They sail east over the sea, and then they row up the big rivers.  
> Between two rivers, they sometimes carry their boats over land.  
> The rivers lead them south to Constantinople, a very rich city.  
> In their own language, they call it Miklagard - 'the big city'.  
> There they sell furs from their forests and amber from their sea.  
> They travel home with fine cloth and bright silver coins.  
> Archaeologists still find many old silver coins in the ground in the north.  
> Other traders from the same people sail west, to Ireland.  
> Their trade routes go from Ireland in the west to Constantinople in the east.  
> **Who are the X people?**

**Svar:** ⬜ The Phoenicians · ⬜ The Greeks · ✅ The Vikings · ⬜ The Romans

**Ord:** *trader* — a person who buys and sells things · *fur* — the warm, hairy skin of an animal · *amber* — a hard, gold-colored material from old tree sap; people make beads and jewelry from it · *archaeologist* — a person who digs in the ground to learn about the past

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Land in the west</summary>

> The X people are sailors from the north of Europe.  
> They sail west over the open ocean in wooden ships.  
> They have no compass and no sea maps.  
> They read the sun, the stars, the birds, and the waves.  
> First, they settle on Iceland, an island with volcanoes and hot springs.  
> Later, some sail on to Greenland and build farms there.  
> Old stories tell of one more land in the west, with wild grapes.  
> The stories call it Vinland.  
> For a long time, people think Vinland is only a story.  
> Then archaeologists find remains of their houses in Canada.  
> People already live in this land, and the old stories tell of meetings with them.  
> So these sailors reach America about 500 years before Columbus.  
> **Who are the X people?**

**Svar:** ✅ The Vikings · ⬜ The Phoenicians · ⬜ The Greeks · ⬜ The Romans

**Ord:** *compass* — a tool that always shows you which way is north · *settle* — to move to a new place and make your home there · *hot spring* — a place where hot water comes up out of the ground · *remains* — the parts of something old that are still there

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Stones that remember</summary>

> The X people live on farms in the north of Europe, about 1,000 years ago.  
> They grow food, keep cows and sheep, fish, and make wool cloth.  
> They also have their own letters, called runes.  
> Runes have straight lines, so a knife can cut them into wood, bone, and stone.  
> When a loved person dies, the family can raise a big stone with runes on it.  
> The stone tells the person's name and good deeds.  
> Many of these memory stones still stand today.  
> A woman in this society can have real power: she can own a farm, and she can inherit land.  
> When the men sail away on long journeys, women often lead the farm at home.  
> **Who are the X people?**

**Svar:** ⬜ The Phoenicians · ⬜ The Egyptians · ⬜ The Maya · ✅ The Vikings

**Ord:** *runes* — old letters made of straight lines · *deed* — a thing that a person does · *society* — all the people who live together in a country or group · *inherit* — to get land, money, or things from a family member who dies

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Who writes their story?</summary>

> About 1,000 years ago, ships from the north of Europe land in many countries.  
> Some of the X people on the ships rob churches and towns.  
> The monks in the churches can write, and they write about the attacks.  
> The X people themselves write only short texts.  
> Their own long stories are written down only hundreds of years later.  
> So most old books about them come from their victims.  
> Of course, these books show them as wild and cruel.  
> Much later, artists add new details to the picture.  
> About 150 years ago, a costume designer draws horned helmets for an opera.  
> Archaeologists never find one horned helmet from the real X people.  
> But films and cartoons still show the horned helmets today.  
> So when you read history, always ask: who writes this, and why?  
> **Who are the X people?**

**Svar:** ⬜ The Mongols · ⬜ The Romans · ✅ The Vikings · ⬜ The Ottomans

**Ord:** *monk* — a religious man who lives simply and prays; many monks can write · *victim* — a person that something bad happens to · *cruel* — very unkind; a cruel person hurts others · *costume designer* — a person who makes the clothes for a play or a film

</details>

### Korstågen

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The long journey east</summary>

> The X wars begin about 900 years ago.  
> Knights, farmers, and priests in Europe pack their bags and start walking east.  
> Their goal is a city far away, in the lands at the east end of the Mediterranean Sea.  
> The city is holy for Jews, for Christians, and for Muslims.  
> The travelers sew a cross of cloth on their clothes.  
> The name of the X wars comes from this sign.  
> The journey takes months, over mountains and over the sea.  
> The way is long and dangerous, and many travelers die before they arrive.  
> The X wars come and go for about 200 years.  
> People of all three religions suffer in them.  
> **Which wars are these?**

**Svar:** ⬜ The Viking raids · ✅ The Crusades · ⬜ The Punic Wars · ⬜ The Mongol conquests

**Ord:** *knight* — a soldier on a horse with metal clothes, long ago · *holy* — very special and important for a religion · *priest* — a man who leads prayers in a church · *sew* — to join cloth with a needle and thread

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Why do so many go?</summary>

> The X wars begin about 900 years ago.  
> A powerful church leader in Europe gives a famous speech.  
> He asks people to march east and fight for a holy city, far away.  
> He promises: God forgives the sins of everyone who goes.  
> Why do so many people say yes?  
> Some truly believe, and want to pray in the holy city.  
> Some are poor, and hope for a better life.  
> Some knights dream of honor and adventure.  
> Some merchants hope for new trade.  
> In the east, the travelers see rich cities, bigger than any city at home.  
> But the people who live there see something else: strange armies at their gates.  
> **Which wars are these?**

**Svar:** ✅ The Crusades · ⬜ The Persian Wars · ⬜ The Viking raids · ⬜ The Mongol conquests

**Ord:** *sin* — a bad act against the rules of a religion · *forgive* — to stop being angry about a bad act · *honor* — a good name; people think highly of you · *merchant* — a person who buys and sells things

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Goods and ideas cross the sea</summary>

> The X wars begin about 900 years ago.  
> Armies from Europe sail east, to the lands at the east end of the Mediterranean Sea.  
> The wars return again and again, for many years.  
> But soldiers are not the only travelers between the two shores.  
> Ships also carry merchants, pilgrims, and ideas.  
> Europeans taste sugar and lemons, and they want more.  
> They buy paper, fine glass, and soft cotton cloth.  
> Arab doctors keep old Greek and Persian medicine alive in their books, and add new knowledge of their own.  
> Some of this knowledge slowly reaches Europe - through trade, and through translated books.  
> Much also comes the peaceful way, through Spain and Sicily.  
> War closes doors; trade and books open them again.  
> **Which wars are these?**

**Svar:** ⬜ The Persian Wars · ⬜ The Mongol conquests · ✅ The Crusades · ⬜ The Viking raids

**Ord:** *shore* — the land at the edge of the sea · *pilgrim* — a person who travels far to visit a holy place · *merchant* — a person who buys and sells things · *translate* — to say or write something again in another language

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — No simple story</summary>

> During the X wars, about 900 years ago, an army from Europe reaches the holy city at last.  
> The soldiers break through the walls, and many people in the city die - Muslims and Jews.  
> Writers from both sides describe terrible days.  
> Almost 100 years later, a famous Muslim leader takes the city back.  
> This time, many people can buy their freedom and leave alive.  
> The same wars - but not the same choices.  
> There are more dark chapters.  
> On the way east, some armies attack Jewish families in European towns.  
> And one army attacks Constantinople, a rich Christian city, and robs it - Christians against Christians.  
> Over 200 years, both sides show cruelty, and both sides show mercy.  
> So the X wars are not a simple story of good against evil.  
> In every war, ordinary people of every religion pay the highest price.  
> **Which wars are these?**

**Svar:** ✅ The Crusades · ⬜ The Mongol conquests · ⬜ The Viking raids · ⬜ The Punic Wars

**Ord:** *chapter* — one part of a book; here: one part of a story · *rob* — to take things from people with force · *Constantinople* — a big old city by the sea; today it is Istanbul in Turkey · *ordinary* — normal, not special

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Two books about the same wars</summary>

> The X wars take place about 900 years ago, around a holy city at the east end of the Mediterranean Sea.  
> European writers of that time call the fighters from Europe holy pilgrims.  
> Arab writers of the same time call them simply "the Franks".  
> One Arab writer, Usama ibn Munqidh, meets Franks as enemies - and some as friends.  
> Another, Ibn al-Athir, later writes about the fall of the holy city with deep sadness.  
> European books tell the same days as a great victory.  
> Same city, same days - two very different stories.  
> Today, politicians sometimes use the name of these wars as a weapon in their speeches.  
> The old word still makes people angry or proud.  
> A historian reads both sides and checks every story against the sources.  
> **Which wars are these?**

**Svar:** ⬜ The Persian Wars · ⬜ The Punic Wars · ⬜ The Mongol conquests · ✅ The Crusades

**Ord:** *the Franks* — an old Arabic name for people from western Europe · *politician* — a person who works with power and government in a country · *source* — an old text or thing that gives us knowledge about the past · *historian* — a person who studies the past

</details>

### Digerdöden

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The sickness on the ships</summary>

> Sickness X comes about 700 years ago.  
> It comes on ships from far away.  
> The ships sail across the sea to busy ports.  
> From the ports, it moves along the trade roads.  
> It travels from town to town.  
> It spreads very fast.  
> Very many people fall sick.  
> Sadly, many of them die.  
> In these years, people do not know what makes them sick.  
> They cannot see the real cause.  
> They are afraid, and they cannot stop it.  
> **Which sickness is this?**

**Svar:** ✅ The Black Death · ⬜ smallpox · ⬜ cholera · ⬜ leprosy

**Ord:** *port* — a place by the sea where ships stop · *trade road* — a road where people carry things to buy and sell · *spread* — to go from one place or person to many · *cause* — the thing that makes something happen

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Guessing and knowing</summary>

> About 700 years ago, Sickness X spreads across many lands.  
> People want to know why.  
> Some say the air is bad and full of a bad smell.  
> Some say it is a punishment.  
> They try many strange cures, but the cures do not work.  
> They are only guessing.  
> Today, we know the real cause.  
> A tiny living thing, a germ, makes people sick.  
> This germ lives on small fleas.  
> The fleas ride on rats, and the rats travel with people and ships.  
> Guessing and knowing are not the same thing.  
> **Which sickness is this?**

**Svar:** ⬜ smallpox · ⬜ malaria · ✅ The Black Death · ⬜ cholera

**Ord:** *punishment* — trouble you get when you do something wrong · *cure* — something that makes a sick person well again · *germ* — a tiny living thing, too small to see, that can make you sick · *flea* — a very small jumping insect that bites animals and people

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — When workers become few</summary>

> About 700 years ago, Sickness X spreads across many lands.  
> So many people die that some villages stand empty.  
> Before, there are many workers and little land.  
> Now there are few workers and much land.  
> But the lords still need people to work the fields.  
> So workers can ask for more pay and better food.  
> Some workers leave a hard lord and walk to a kinder one.  
> Before, many farmers are bound to one lord's land.  
> Now this old rule grows weak in many lands in western Europe.  
> A terrible sickness changes who holds the power.  
> When people are few, their work is worth more.  
> **Which sickness is this?**

**Svar:** ⬜ cholera · ⬜ leprosy · ⬜ smallpox · ✅ The Black Death

**Ord:** *village* — a very small town · *lord* — a rich man who owns land, and the people work for him · *bound* — tied to a place, and not free to leave · *pay* — the money you get for your work

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Fear and forty days</summary>

> About 700 years ago, Sickness X brings great fear.  
> People are afraid, and they look for someone to blame.  
> In some towns, people wrongly blame their Jewish neighbors.  
> This is not true, and it is deeply unfair.  
> Sadly, many Jewish people are hurt and killed.  
> Fear can make people cruel to the innocent.  
> Other towns choose a wiser way.  
> In one city by the sea, ships must wait before they may land.  
> This wait lasts forty days.  
> From these "forty days" comes our word "quarantine".  
> In hard times, fear can lead to cruelty, or to wise care.  
> **Which sickness is this?**

**Svar:** ⬜ leprosy · ✅ The Black Death · ⬜ smallpox · ⬜ cholera

**Ord:** *blame* — to say that someone did a bad thing · *innocent* — a person who did nothing wrong · *cruel* — very unkind; wanting to hurt someone · *quarantine* — to keep people or ships apart for some days, so a sickness cannot spread

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — How we know</summary>

> About 700 years ago, Sickness X changes the world.  
> But how do we know about it today?  
> Writers of that time keep chronicles, and they tell of the sickness.  
> Yet fear and rumor can bend their words.  
> So historians also read old tax lists and church records that name the priests who died.  
> When many names drop from a list, it can mean many people are gone.  
> And now there is newer proof, from science.  
> Scientists study very old bones from graves.  
> In the teeth, they find the DNA of one tiny germ: Yersinia pestis.  
> So an old guess becomes a clear fact.  
> Many kinds of sources, put together, show us the truth.  
> **Which sickness is this?**

**Svar:** ⬜ smallpox · ⬜ leprosy · ✅ The Black Death · ⬜ malaria

**Ord:** *chronicle* — an old written record of things that happen, year by year · *tax list* — an old list of people who must pay money to the ruler · *DNA* — a tiny code inside living things that tells what they are · *source* — something from the past that tells us what happened, like a book or a bone

</details>

### Djingis khan

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Poor Boy from the Sea of Grass</summary>

> Khan X lives about 800 years ago, on the wide grasslands of Asia.  
> His people live in round felt tents and move with their horses, sheep, and goats.  
> His father dies when he is a young boy.  
> His family becomes poor and often has too little food.  
> The boy learns to ride, to hunt, and to never give up.  
> The clans of the grasslands fight each other all the time.  
> When he grows up, he does something new.  
> He brings the fighting clans together into one people.  
> The clans give him a new name and title.  
> It may mean "strong ruler" or "ruler of all".  
> **Who is Khan X?**

**Svar:** ⬜ Alexander the Great · ✅ Genghis Khan · ⬜ Napoleon Bonaparte · ⬜ Kublai Khan

**Ord:** *grassland* — big open land where grass grows · *felt* — thick cloth made of pressed wool · *clan* — a big group of families that belong together · *title* — a special name for a ruler or an important person

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The Empire of Fast Horses</summary>

> Khan X grows up on the grasslands of Asia and unites the riding clans.  
> Then he and his riders build a huge empire on land.  
> His wars are terrible for the people he conquers.  
> After his death, his sons and grandsons make it even bigger.  
> It becomes the largest land empire in history.  
> It reaches from the sea in the east far into Europe.  
> How can one ruler control such a wide land?  
> Khan X and his family order horse stations along the big roads.  
> At each station, fresh horses wait.  
> A messenger rides fast, changes to a fresh horse, and rides on.  
> Messages travel day and night, faster than ever before.  
> This empire runs on grass, horses, and information.  
> **Who is Khan X?**

**Svar:** ⬜ Kublai Khan · ⬜ Alexander the Great · ⬜ Julius Caesar · ✅ Genghis Khan

**Ord:** *empire* — many lands and many people under one ruler · *station* — a stop-place on a long road · *messenger* — a person who carries a message

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The Ruler Who Cannot Read</summary>

> Khan X is a ruler from the grasslands of Asia.  
> As a boy, he has no school, and he probably never learns to read.  
> As a young man, he unites the fighting clans into one people.  
> He orders a writing system for his people's language.  
> He gives his empire strict laws.  
> He chooses his generals for their skill, not for their family name.  
> Even a poor herder's son can become a top commander.  
> People of many religions live in his empire, and all can pray in their own way.  
> When his army takes a city, it spares the skilled craft workers.  
> But they must move far away and work for the empire.  
> Many of the other people in these cities are killed or lose their homes.  
> A ruler who cannot read builds a state that runs on writing, law, and skill.  
> **Who is Khan X?**

**Svar:** ✅ Genghis Khan · ⬜ Hammurabi · ⬜ Napoleon Bonaparte · ⬜ Kublai Khan

**Ord:** *strict* — very firm; the rules must be followed · *herder* — a person who keeps and moves animals, like sheep or horses · *commander* — a leader of soldiers · *craft worker* — a person who makes things with their hands, like pots, cloth, or tools

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Safe Roads, Terrible Price</summary>

> Khan X, a rider who unites the clans of the grasslands, builds a giant empire across Asia.  
> Under him and his family, one power guards the long trade roads between east and west.  
> An old saying tells: a girl can carry a bag of gold across the empire, and no one robs her.  
> Silk, paper, and new ideas travel from land to land.  
> But the roads carry more than goods.  
> About a hundred years later, a deadly sickness follows them all the way to Europe.  
> And this peace has a terrible price.  
> The wars of Khan X kill millions of people.  
> Cities that do not give up are destroyed.  
> Traders remember the safe roads. The destroyed cities remember something else.  
> The empire opens roads for the world, and destroys millions of lives to build them.  
> **Who is Khan X?**

**Svar:** ⬜ Alexander the Great · ⬜ Napoleon Bonaparte · ✅ Genghis Khan · ⬜ Kublai Khan

**Ord:** *trade* — buying and selling things · *goods* — things people buy and sell · *deadly* — so dangerous that people die from it

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Monster or State-Builder?</summary>

> Khan X, a ruler from the grasslands of Asia, builds a huge empire about 800 years ago.  
> How can we know about him today?  
> Soon after his death, his own people write his story in their own language.  
> That book is even called "The Secret History."  
> It shows him from the inside: his poor childhood, his fears, and his mistakes.  
> The peoples he conquers write about him too, in Persian, Arabic, and Chinese.  
> They see their burned cities, and in their books he is often a monster.  
> Later, travelers from Europe visit the empire and send home reports.  
> Some report wild "barbarians"; others report law, order, and safe roads.  
> So who is he — a monster, or a builder of a state?  
> Every source stands somewhere; the historian's job is to see where.  
> **Who is Khan X?**

**Svar:** ⬜ Alexander the Great · ⬜ Napoleon Bonaparte · ✅ Genghis Khan · ⬜ Kublai Khan

**Ord:** *source* — an old text or thing that gives us information about the past · *conquer* — to take a land by force · *report* — a text that tells what a person sees and learns · *barbarian* — an unfair old word for people that writers see as wild and simple

</details>

### Jeanne d'Arc

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Farm Girl in Armor</summary>

> Miss X lives in France about 600 years ago.  
> She is a farm girl in a small village.  
> She watches the animals and helps at home.  
> She cannot read or write.  
> Her land is at war with England, year after year.  
> One day she tells people a strange thing.  
> She says holy voices speak to her.  
> The voices tell her to save France, she says.  
> She is only about seventeen years old.  
> Yet she gets armor, a horse, and a place in the army.  
> Soon grown soldiers follow the farm girl into battle.  
> **Who is Miss X?**

**Svar:** ⬜ Mulan · ✅ Joan of Arc · ⬜ Cleopatra · ⬜ Boudicca

**Ord:** *armor* — hard metal clothes that keep a soldier safe · *holy* — of God, or close to God · *battle* — a fight between armies

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The Siege That Turns a War</summary>

> Miss X is a young woman in France, about 600 years ago.  
> France and England fight a war that lasts about a hundred years.  
> Now an English army surrounds Orléans, a key city on a river.  
> The siege lasts many months, and food runs low.  
> If this city falls, all France may fall.  
> Miss X says God sends her to save the city.  
> She rides in with fresh soldiers and food.  
> She carries a white banner into the fight.  
> She loves it more than her sword, she says.  
> The tired defenders find new hope and attack.  
> Within about a week, the English army leaves.  
> The long war slowly begins to turn.  
> **Who is Miss X?**

**Svar:** ⬜ Boudicca · ⬜ Isabella I of Castile · ⬜ Elizabeth I · ✅ Joan of Arc

**Ord:** *siege* — an army waits around a city so no food or help can come in · *banner* — a flag on a pole that soldiers follow · *defender* — a person who fights to keep a place safe

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Every Word Is Written Down</summary>

> Miss X is a young French woman, famous from a long war.  
> She is captured in battle and sold to the English side.  
> Simply killing a famous prisoner is not enough for them.  
> They set up a church court to judge her.  
> The judges ask about the voices she says she hears.  
> They hope to prove that her voices are not from God.  
> Scribes write down every question and every answer.  
> For weeks, they question her, day after day.  
> She cannot read, yet she answers with care.  
> One question is a trap: is she in God's grace?  
> - If I am not, may God put me there, she answers.  
> Still, the court finds her guilty, and she is put to death.  
> **Who is Miss X?**

**Svar:** ✅ Joan of Arc · ⬜ Anne Boleyn · ⬜ Marie Antoinette · ⬜ Mary, Queen of Scots

**Ord:** *capture* — to take a person prisoner · *scribe* — a person whose job is to write things down · *grace* — God's love and help, in Christian belief · *guilty* — the court says: this person did the bad thing

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The Prince Who Needs a Sign</summary>

> About 600 years ago, France is torn by war.  
> The king of England says the French crown is his.  
> Many French lords take the English side.  
> The young French prince is poor and full of doubt.  
> He is not even crowned in Reims, the city of kings.  
> Then Miss X, a village girl, comes to his court.  
> She says God sends her to make him true king.  
> In that age, a sign from God is strong politics.  
> The prince decides to try her help, and it works.  
> After a big victory, she leads him to Reims.  
> He is crowned there, and many doubters accept him.  
> When she is taken prisoner later, her king sends no help.  
> **Who is Miss X?**

**Svar:** ⬜ Eleanor of Aquitaine · ⬜ Margaret of Anjou · ✅ Joan of Arc · ⬜ Isabella I of Castile

**Ord:** *crown* — to make a person king or queen in a holy ceremony · *lord* — a rich and powerful man who rules land · *doubt* — a feeling that a thing may not be true or real

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Two Courts, Two Stories</summary>

> Miss X is a French village girl from about 600 years ago.  
> Most village girls of her time leave no trace.  
> Yet historians know her better than most kings.  
> The reason: her famous trial is written down, word for word.  
> About twenty-five years later, a new court reopens her case.  
> It listens to her childhood friends and her old soldiers.  
> Their memories fill page after page.  
> The first court wants her guilty; the second wants her innocent.  
> So historians read both records with careful, cool eyes.  
> Almost five hundred years after her death, the Church names her a saint.  
> Today she is a national symbol of France.  
> Many political groups, left and right, use her as their sign.  
> **Who is Miss X?**

**Svar:** ⬜ Bernadette of Lourdes · ✅ Joan of Arc · ⬜ Catherine of Siena · ⬜ Hildegard of Bingen

**Ord:** *trace* — a small sign that a person or thing was there · *record* — a written text that saves what people say and do · *innocent* — not guilty; the person did not do the bad thing · *symbol* — a person or thing that stands for a bigger idea

</details>

### Renässansen

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Silk, spices, and new art</summary>

> Period X begins about 600 years ago, in the trading cities of Italy.  
> These cities grow rich from silk, spices, wool, and banks.  
> Ships and mule roads connect them with faraway lands.  
> The richest families want fine art in their homes and churches.  
> They pay artists to paint walls and build domes.  
> The artists learn from old Roman statues and buildings.  
> A young artist starts as a helper in a master's workshop.  
> He cleans brushes, mixes colors, and copies drawings.  
> After many years, he can become a master too.  
> Each city wants finer churches and statues than its neighbors.  
> So the cities compete with art, not only with ships and gold.  
> **Which period is this?**

**Svar:** ⬜ The Middle Ages · ✅ The Renaissance · ⬜ The Industrial Revolution · ⬜ The Enlightenment

**Ord:** *spices* — parts of plants that give food a strong taste · *workshop* — a room where a master and helpers make things · *master* — a fully trained artist or craftsman who teaches others · *dome* — a round roof, like half a ball

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The hunt for old books</summary>

> Period X starts in Italy about 600 years ago and spreads across Europe.  
> In this period, scholars hunt for old books.  
> They search in the dusty book rooms of monasteries.  
> There they find texts from ancient Rome, copied by monks long ago.  
> Some of these texts lie almost forgotten for a thousand years.  
> Scholars from the Greek east bring more old texts to Italy.  
> Now people can read famous Greek thinkers again.  
> The scholars compare the copies and fix mistakes in them.  
> Rich men pay for new libraries, open to readers.  
> The old texts are full of ideas about law, nature, and a good life.  
> Readers begin to ask new questions about their own time.  
> **Which period is this?**

**Svar:** ⬜ The Reformation · ⬜ The Middle Ages · ✅ The Renaissance · ⬜ The Enlightenment

**Ord:** *scholar* — a person whose work is studying and learning · *monastery* — a house where monks live, work, and pray · *monk* — a religious man who lives simply in a monastery

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A window in the wall</summary>

> Period X brings new art to Italy about 600 years ago.  
> The painters of this time face an old problem.  
> A wall or a wood panel is flat.  
> How can a painting look deep, like a view through a window?  
> An architect in Florence finds exact rules for this.  
> Far things must be painted smaller, by fixed rules.  
> Lines that run away from the viewer must meet in one point.  
> Painters draw floors, streets, and halls with these rules.  
> Now the picture opens like a window in the wall.  
> Painters also study light, shadow, and the human body.  
> Rooms in their paintings look real enough to step into.  
> **Which period is this?**

**Svar:** ✅ The Renaissance · ⬜ The Middle Ages · ⬜ The Enlightenment · ⬜ The Reformation

**Ord:** *panel* — a flat piece of wood that artists paint on · *architect* — a person who plans and designs buildings · *shadow* — the dark place where light does not reach

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Back to the sources</summary>

> Period X spreads from Italy across Europe about 500 years ago.  
> In the middle of this period, a new machine appears in Europe.  
> In Germany, printers build presses with movable metal letters.  
> People in China and Korea print with movable letters much earlier.  
> In Europe this is new, and it changes how ideas travel.  
> A printed book costs much less than a hand-written copy.  
> A scholar in Italy writes about an old Roman text.  
> A few months later, students in Paris read the printed pages.  
> Scholars like him are called humanists.  
> They study language, history, poetry, and the good life.  
> Their rule is: go back to the sources, read the oldest texts yourself.  
> **Which period is this?**

**Svar:** ⬜ The Reformation · ⬜ The Industrial Revolution · ⬜ The Enlightenment · ✅ The Renaissance

**Ord:** *press* — a machine that pushes ink onto paper · *movable* — easy to move and use again in a new place · *humanist* — a scholar who studies language, history, and poetry · *source* — the oldest text, where an idea first comes from

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Sharp break or slow change?</summary>

> Historians give names to the periods of the past.  
> But who chooses the names, and where do the lines go?  
> Period X shows how hard this is.  
> About 160 years ago, the Swiss historian Jacob Burckhardt writes a famous book about it.  
> He says: in Italy, six or seven hundred years ago, old art and learning are born again.  
> People there discover the world and themselves, he writes.  
> Later historians doubt this sharp, clean break.  
> Life for most farmers changes little in these years.  
> Scholars in the centuries before also read old Roman texts.  
> Some historians say: the sharp break is a story told long afterwards.  
> Today, many see both continuity and real new things in art and learning.  
> **Which period is this?**

**Svar:** ⬜ The Middle Ages · ⬜ The Enlightenment · ✅ The Renaissance · ⬜ The Reformation

**Ord:** *historian* — a person who studies and writes about the past · *doubt* — to not feel sure that something is true · *continuity* — when life goes on without a sharp change

</details>

### Leonardo da Vinci

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Apprentice Who Asks Why</summary>

> Mr X lives in Italy more than five hundred years ago.  
> He is born in a small village among hills.  
> As a boy, he draws everything he sees.  
> His father takes him to the rich city of Florence.  
> There he becomes an apprentice in a famous workshop.  
> He learns to paint, to mix colors, and to shape metal.  
> But he asks questions about everything.  
> He asks why birds fly and how water moves.  
> A story tells: one day the student paints better than his master.  
> Later he paints a portrait of a woman with a quiet smile.  
> Today it may be the most famous painting in the world.  
> **Who is Mr X?**

**Svar:** ⬜ Michelangelo · ✅ Leonardo da Vinci · ⬜ Raphael · ⬜ Galileo Galilei

**Ord:** *apprentice* — a young person who learns a job from a master · *workshop* — a room where people make things with their hands · *portrait* — a painting of a person

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The Notebooks Written Backwards</summary>

> Mr X is an artist and thinker in Italy, about five hundred years ago.  
> He carries a small notebook on his belt.  
> He fills page after page with drawings and notes.  
> Machines, rivers, plants, faces: he draws everything.  
> In all, thousands of pages survive today.  
> But his writing runs from right to left.  
> Every letter is turned, as in a mirror.  
> To read it, you can hold the page to a mirror.  
> Maybe he hides his ideas from curious eyes.  
> Or maybe it is simply easier for his left hand.  
> Writing this way, the wet ink does not smear.  
> He plans big books, but he never finishes them.  
> **Who is Mr X?**

**Svar:** ⬜ Johannes Gutenberg · ⬜ Galileo Galilei · ⬜ Isaac Newton · ✅ Leonardo da Vinci

**Ord:** *notebook* — a small book with empty pages for writing and drawing · *mirror* — glass in which you can see yourself · *curious* — wanting very much to know things · *smear* — to make wet ink dirty by touching it

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — What Is Under the Skin</summary>

> Mr X, a painter in Italy, lives about five hundred years ago.  
> He wants to paint people as they really are.  
> So he asks: what is under the skin?  
> Doctors at a hospital let him study the dead.  
> He works at night, carefully, layer by layer.  
> He draws every muscle, every bone, every vein.  
> He draws the heart and its small doors.  
> He draws how a baby lies in the womb.  
> His anatomy drawings are centuries ahead of their time.  
> But he keeps them in his private papers.  
> Doctors learn nothing from them for hundreds of years.  
> The artist's eye sees what science has not yet seen.  
> **Who is Mr X?**

**Svar:** ✅ Leonardo da Vinci · ⬜ Michelangelo · ⬜ Charles Darwin · ⬜ Isaac Newton

**Ord:** *muscle* — a part of the body that moves your bones · *vein* — a thin tube that carries blood in the body · *womb* — the place inside a mother where a baby grows · *anatomy* — the science of how the body is built

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Wings on Paper</summary>

> Mr X lives in Italy about five hundred years ago.  
> Rich rulers pay him as their engineer.  
> For them he plans bridges, canals, and machines of war.  
> Yet he writes: war is a beastly madness.  
> But he has a dream of his own: humans should fly.  
> He watches birds and bats for hours.  
> He draws wings for a man to flap.  
> He draws a screw to climb the air.  
> He draws a cloth tent to fall slowly: a parachute.  
> Almost none of these machines are built in his lifetime.  
> Human muscles are too weak, and there is no motor.  
> Centuries later, people test some designs, and a few really work.  
> **Who is Mr X?**

**Svar:** ⬜ Isaac Newton · ⬜ Johannes Gutenberg · ✅ Leonardo da Vinci · ⬜ Galileo Galilei

**Ord:** *engineer* — a person who plans and builds machines, roads, or bridges · *canal* — a river dug by people, for boats or water · *beastly* — wild and cruel, like a dangerous animal · *parachute* — a big cloth that lets a person fall slowly and safely

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Scattered Pages</summary>

> Mr X, an Italian artist and thinker, dies about five hundred years ago.  
> How can we know his ideas today?  
> He leaves thousands of notebook pages to a loyal student.  
> After that student's death, the pages begin to travel.  
> Collectors buy them, cut them, and mix their order.  
> Today the pages lie in libraries in several lands.  
> Two lost notebooks appear again in Spain, only about sixty years ago.  
> Scholars think that perhaps half of all pages are gone.  
> Historians must date every page and rebuild the order.  
> People say he is good in almost every field.  
> But researchers still ask: lone genius, or man of a big workshop full of helpers?  
> Every claim about him rides on the scattered pages.  
> **Who is Mr X?**

**Svar:** ⬜ Michelangelo · ✅ Leonardo da Vinci · ⬜ Nicolaus Copernicus · ⬜ Galileo Galilei

**Ord:** *collector* — a person who buys and keeps old or rare things · *scholar* — a person who studies books deeply · *genius* — a person with a very great mind · *scattered* — spread out to many different places

</details>

### Johannes Gutenberg

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Book That Costs a Farm</summary>

> Mr X lives in Europe, about 600 years ago.  
> At this time, every book is written by hand.  
> A worker called a scribe copies every page.  
> One thick book can take years of work.  
> A book can cost as much as a farm.  
> Some libraries even chain their books to the shelf.  
> Most people never own a book.  
> Mr X is a metal worker with a new idea.  
> In his workshop, he builds a machine that makes book pages.  
> The machine makes hundreds of copies of a page in one day.  
> Slowly, books become cheap enough for more homes.  
> **Who is Mr X?**

**Svar:** ⬜ Leonardo da Vinci · ✅ Johannes Gutenberg · ⬜ Martin Luther · ⬜ Nicolaus Copernicus

**Ord:** *scribe* — a person whose job is writing · *chain* — to lock something to a place with metal rings · *workshop* — a room or building where people make things

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A Wine Press for Words</summary>

> Mr X is a goldsmith in the German city of Mainz.  
> About 600 years ago, he builds a new way to make books.  
> He makes small metal blocks, one letter on each block.  
> With a hand mold, he pours thousands of equal blocks.  
> A worker sets the blocks in rows to build a page.  
> The worker covers the blocks with thick, sticky ink.  
> A strong press, like a wine press, pushes paper onto the blocks.  
> One pull of the press prints a whole page.  
> The press makes copy after copy of the same page.  
> Then the workers take the rows apart.  
> The same blocks now build the next page.  
> A box of metal letters can print any book in his language.  
> **Who is Mr X?**

**Svar:** ⬜ Aldus Manutius · ⬜ Leonardo da Vinci · ⬜ Nicolaus Copernicus · ✅ Johannes Gutenberg

**Ord:** *goldsmith* — a person who makes fine things from gold and other metals · *mold* — a hollow form; you pour something in, and it takes that shape · *ink* — the colored liquid used for writing and printing · *press* — a machine that pushes two things hard together

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Not the First in the World</summary>

> In Mainz, Mr X builds his famous printing workshop, about 600 years ago.  
> But he is not the first to print with movable letters.  
> In China, printers press whole book pages from carved wood blocks, centuries before him.  
> One Chinese printer even makes single letters of baked clay.  
> In Korea, printers cast letters of metal before Mr X is born.  
> One Korean book printed this way still exists today.  
> So what does Mr X really add?  
> Chinese writing uses thousands of different signs.  
> A European alphabet needs only about two dozen letters.  
> Mr X packs the whole craft into one cheap, fast system.  
> Any town with money can start its own workshop.  
> Within fifty years, printing workshops open all across Europe.  
> **Who is Mr X?**

**Svar:** ✅ Johannes Gutenberg · ⬜ Aldus Manutius · ⬜ Leonardo da Vinci · ⬜ Galileo Galilei

**Ord:** *carve* — to cut a shape into wood or stone with a tool · *clay* — soft earth that becomes hard when you bake it · *cast* — to make a thing by pouring hot metal into a form

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Ideas Too Fast to Stop</summary>

> Mr X of Mainz starts Europe's age of cheap printed books.  
> A printed book costs far less than a hand-written book.  
> Printers also sell small news booklets for little money.  
> A new idea can now cross a land in weeks.  
> About fifty years after Mr X dies, a German monk gets angry.  
> The church sells special papers, and buyers believe the papers bring God's forgiveness.  
> The monk writes sharp points against this sale.  
> Printers turn his protest into thousands of cheap copies.  
> The quarrel grows and splits the church in western Europe.  
> Kings and church leaders try to control the presses.  
> They learn that printed ideas are hard to stop.  
> Without the machine of Mr X, the protest may stay small.  
> **Who is Mr X?**

**Svar:** ⬜ Martin Luther · ⬜ Aldus Manutius · ✅ Johannes Gutenberg · ⬜ Nicolaus Copernicus

**Ord:** *monk* — a religious man who lives a simple life for his faith · *forgiveness* — when someone stops being angry about a wrong thing you did · *protest* — strong words or actions against something · *quarrel* — a long, angry fight with words

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Famous Man We Hardly Know</summary>

> Mr X of Mainz is called the father of European printing.  
> Yet historians know very little about the man.  
> No document records his birth, and no true portrait of him exists.  
> Even his famous printed Bible does not name its maker.  
> We know him mostly from money papers and court records.  
> He borrows a fortune from a business partner for his workshop.  
> Later, the partner takes him to court over the money.  
> Mr X loses the case.  
> Historians think the partner then takes over the Bible workshop.  
> Scholars also debate the word "revolution".  
> One famous study says print changes Europe fast and deeply.  
> Critics answer that people, not machines, make change, and slowly.  
> **Who is Mr X?**

**Svar:** ⬜ Laurens Janszoon Coster · ✅ Johannes Gutenberg · ⬜ Aldus Manutius · ⬜ Leonardo da Vinci

**Ord:** *document* — an official paper with information · *portrait* — a picture of a person's face · *court* — the place where a judge decides who is right · *debate* — a public fight with arguments, not weapons

</details>

### Christofer Columbus

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Three Ships on an Unknown Sea</summary>

> Captain X lives about 500 years ago, in Europe.  
> The queen and king of Spain give him three small wooden ships.  
> He sails west, into the open ocean.  
> No map shows how far the water goes.  
> About ninety sailors are on board.  
> They eat hard bread, salted meat, and dried peas.  
> They drink water and wine from wooden barrels.  
> Most sailors sleep on the deck, under the stars.  
> After more than four weeks, the crew grows afraid.  
> Then, one night, a lookout sees land ahead.  
> The ships land on a green island in a warm sea.  
> People already live there, and they meet the sailors on the beach.  
> **Who is Captain X?**

**Svar:** ⬜ Ferdinand Magellan · ⬜ Vasco da Gama · ✅ Christopher Columbus · ⬜ Leif Eriksson

**Ord:** *barrel* — a big round wooden container for food or drink · *deck* — the open floor of a ship · *crew* — all the people who work on a ship · *lookout* — a sailor whose job is to watch for land or danger

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The Wrong Size of the World</summary>

> Captain X is a sailor from a port city in Italy.  
> In his time, educated people know well that the earth is round.  
> The open question is how big the earth is.  
> Captain X reads old travel books and makes his own calculation.  
> His answer is far too small.  
> So he believes Asia lies only a few weeks west of Europe.  
> Experts in Portugal and in Spain check his numbers and say the ocean is far too wide.  
> The experts are right, but the rulers of Spain pay for his voyage anyway.  
> He sails west, and he does find islands.  
> He believes they lie near India, so he calls the people there Indians.  
> He makes four voyages, and he dies still sure that he has been to Asia.  
> He never learns that a continent unknown to Europe blocks his way.  
> **Who is Captain X?**

**Svar:** ✅ Christopher Columbus · ⬜ Marco Polo · ⬜ Vasco da Gama · ⬜ Amerigo Vespucci

**Ord:** *calculation* — finding an answer with numbers · *expert* — a person who knows one subject very well · *voyage* — a long journey by ship · *continent* — one of the biggest land areas of the earth, like Africa or Asia

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The Islands Are Not Empty</summary>

> About 500 years ago, ships from Spain under Captain X reach islands in the Caribbean Sea.  
> The islands are not empty.  
> The Taíno people have lived there for more than a thousand years.  
> They farm cassava and maize, fish from canoes, and sleep in hammocks.  
> Words like hammock, canoe, and hurricane come from their language.  
> This meeting joins two halves of the world.  
> In the years that follow, ships carry maize, tomatoes, cacao, and potatoes east to Europe.  
> Other ships carry horses, cows, sugar cane, and wheat west.  
> But the ships also carry something invisible.  
> Smallpox and measles are new here, and the islanders' bodies have no defense.  
> Within about fifty years, most of the Taíno have died.  
> Sickness kills far more people than any weapon.  
> **Who is Captain X?**

**Svar:** ⬜ Ferdinand Magellan · ⬜ Leif Eriksson · ⬜ Amerigo Vespucci · ✅ Christopher Columbus

**Ord:** *cassava* — a root plant; people make flour and bread from it · *hammock* — a hanging bed made of woven cloth or net · *smallpox* — a deadly sickness with high fever and sores on the skin · *defense* — protection against an attack or a sickness

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Gold, a Colony, and a Priest's Pen</summary>

> On his second voyage west, Captain X returns to the Caribbean islands with seventeen ships.  
> More than a thousand men sail with him, and this time they come to stay.  
> Spain makes the islands a colony, and Captain X becomes its governor.  
> He orders the Taíno people to bring him gold.  
> Those who fail are punished, and families must wash river sand for gold, day after day.  
> Some Taíno leaders fight back, but bows cannot stop steel weapons and horses.  
> Years later, reports of harsh rule reach Spain.  
> A royal officer then sends Captain X home in chains.  
> How do we know all this?  
> A young colonist named Bartolomé de las Casas comes to the islands.  
> Later he becomes a priest and turns against the system.  
> He writes down the cruelty he sees, and through his books the Taíno story reaches us today.  
> **Who is Captain X?**

**Svar:** ⬜ Vasco da Gama · ✅ Christopher Columbus · ⬜ Hernán Cortés · ⬜ Ferdinand Magellan

**Ord:** *colony* — a land that people from another country take and rule · *governor* — the leader who rules a colony · *punish* — to make a person suffer for something · *cruelty* — very unkind acts that hurt people

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Discovery on Trial</summary>

> About 500 years ago, Captain X sails west from Spain and reaches lands unknown to Europe.  
> For centuries, schoolbooks tell that he discovers a new world.  
> Historians now question every word in that sentence.  
> Can anyone discover a land where millions of people already live?  
> Sailors from the cold north reach the same lands about 500 years before him.  
> Archaeologists find the remains of their houses on the coast of Canada.  
> Even the captain's own logbook is a problem: the original is lost.  
> We read his words only in a later copy.  
> Another writer changes parts of the text.  
> Statues of him rise in cities on both sides of the ocean, and now some come down.  
> The lands themselves later get the name of a different sailor, not his.  
> In parts of the Americas, his old holiday now honors the indigenous peoples instead.  
> **Who is Captain X?**

**Svar:** ⬜ Leif Eriksson · ⬜ Amerigo Vespucci · ✅ Christopher Columbus · ⬜ Ferdinand Magellan

**Ord:** *logbook* — a book where a ship's captain writes what happens every day · *archaeologist* — a person who digs in the ground to study how people lived long ago · *statue* — a figure of a person, made of stone or metal · *indigenous* — belonging to the first peoples of a land

</details>

### Ferdinand Magellan

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Five Ships and a Calm New Ocean</summary>

> Captain X lives about 500 years ago.  
> He comes from Portugal, but he sails for the king of Spain.  
> The king gives him five wooden ships and about 270 men.  
> Captain X wants to sail west, all the way to the Spice Islands in Asia.  
> The ships cross the ocean and follow the coast of South America.  
> They sail south for many months, and the weather gets cold.  
> On the shore, the sailors see penguins and big sea lions.  
> Far in the south, they find a strait, a narrow water road through the land.  
> At night, they see fires on the shore, and later that land gets the name Land of Fire.  
> Only three ships come out of the strait. A huge new ocean opens in front of them.  
> The water is calm, so Captain X gives this ocean a name that means peaceful.  
> We still use that name today.  
> **Who is Captain X?**

**Svar:** ⬜ Christopher Columbus · ⬜ Vasco da Gama · ✅ Ferdinand Magellan · ⬜ Francis Drake

**Ord:** *strait* — a narrow line of water between two pieces of land · *spice* — a dried plant part that gives food a strong taste, like pepper · *calm* — quiet and still, without wind or big waves · *penguin* — a black and white sea bird that swims but cannot fly

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The Ocean Nobody Can Measure</summary>

> About 500 years ago, Captain X sails for Spain around the south of the Americas into a new ocean.  
> He believes the islands of cloves and nutmeg lie only a few weeks further west.  
> Nobody in Europe knows how wide this ocean is.  
> Captain X sails west for more than three months without any new food.  
> The ship's bread turns to powder full of worms.  
> The drinking water turns yellow and smells bad.  
> The men eat leather from the ship's ropes and yards and even hunt rats.  
> Then scurvy comes: gums swell and teeth fall out.  
> About twenty men die of it. Nobody yet knows that fresh fruit stops this sickness.  
> In all those weeks, the sailors see only two small empty islands.  
> They have crossed an ocean that covers about one third of the earth.  
> **Who is Captain X?**

**Svar:** ⬜ James Cook · ✅ Ferdinand Magellan · ⬜ Christopher Columbus · ⬜ Francis Drake

**Ord:** *clove* — a spice, the dried flower bud of a tree · *leather* — strong material made from the skin of an animal · *scurvy* — a sickness that comes from too little fresh food · *gums* — the soft pink flesh around the teeth

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The Chief Who Says No</summary>

> About 500 years ago, three ships from Spain reach the islands we now call the Philippines.  
> Their leader, Captain X, sails for the king of Spain.  
> People here have their own rulers and trade with China.  
> The ruler of Cebu welcomes the strangers and makes a friendship pact with Captain X.  
> He and hundreds of his people accept the sailors' religion.  
> Captain X now demands that the chiefs nearby obey Cebu and the king of Spain.  
> On the small island of Mactan, the chief Lapulapu refuses.  
> He is a rival of Cebu. He will not bow to a king across the sea.  
> At dawn, Captain X attacks Mactan with about sixty men in armor.  
> The water is shallow, so the boats and the ships' guns stay far from the beach.  
> Far more than sixty warriors meet the sailors in the water, and Captain X is killed.  
> The ships sail on without him. In the Philippines today, Lapulapu is a national hero.  
> **Who is Captain X?**

**Svar:** ⬜ James Cook · ⬜ Christopher Columbus · ⬜ Vasco da Gama · ✅ Ferdinand Magellan

**Ord:** *chief* — the leader of a village or a people · *pact* — a promise between two sides to help each other · *shallow* — not deep · *warrior* — a person who fights for his people

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The Interpreter from Malacca</summary>

> Long before his famous voyage, Captain X is a soldier for Portugal in Asia.  
> In the port of Malacca, he takes a young man as a slave and calls him Enrique.  
> Enrique speaks Malay, the trade language of the seas of Southeast Asia.  
> Captain X takes him to Europe, and later west across two oceans as his interpreter.  
> After months at sea, the ships reach islands east of Malacca.  
> Enrique speaks to the islanders, and they understand him.  
> Then Captain X dies in a fight on one of the islands.  
> His will says Enrique is now free, but the new leaders refuse to let him go.  
> Soon the ruler of Cebu turns against the sailors. More than twenty of them are killed at a feast.  
> The sailors blame Enrique, but nobody knows the truth, and the sources never mention him again.  
> Some say Enrique is the first person to go around the world, back to his own language.  
> Others say: not quite, because he never reaches Malacca itself.  
> **Who is Captain X?**

**Svar:** ✅ Ferdinand Magellan · ⬜ Vasco da Gama · ⬜ Christopher Columbus · ⬜ Amerigo Vespucci

**Ord:** *slave* — a person who is owned by another person and is not free · *interpreter* — a person who turns words from one language into another · *will* — a paper that says what happens to a person's things after death · *feast* — a big meal for many people

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Eighteen Men and a Lost Day</summary>

> About 500 years ago, five ships leave Spain under Captain X to reach the Spice Islands from the west.  
> Three years later, one ship comes back with eighteen men of about 270, and Captain X is not among them.  
> How do we know the story? A young Italian gentleman, Antonio Pigafetta, joins to see the world and keeps a diary through the whole voyage.  
> The original is lost; we read it in four later handwritten copies.  
> A pilot's logbook and pay lists in the archives of Seville fill the gaps.  
> Pigafetta records a puzzle at the end: the sailors have lost a day.  
> They count every day with care, but at the first port on the way home the diary says Wednesday, and it is Thursday.  
> Sailing west with the sun, they have seen one sunrise fewer than people at home.  
> Today the date line in the middle of the ocean solves this puzzle.  
> So who first goes around the world? In one voyage, it is the last captain, Elcano, with seventeen men.  
> As a young soldier, Captain X reaches these seas by sailing east, to Malacca. As captain he reaches islands a little further east by sailing west.  
> Whether he ever sails that last stretch, no source tells us.  
> **Who is Captain X?**

**Svar:** ⬜ Francis Drake · ✅ Ferdinand Magellan · ⬜ Christopher Columbus · ⬜ James Cook

**Ord:** *gentleman* — a man of good family who does not need to work with his hands · *diary* — a book where a person writes what happens every day · *pilot* — the sailor who guides the ship on its course · *archive* — a place where old papers are kept and protected

</details>

### Nicolaus Kopernikus

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Quiet Man in the Tower</summary>

> Mr X lives about 500 years ago, in the north of Poland.  
> He works at a cathedral by the sea.  
> He is also a doctor and helps sick people.  
> He has a small tower in the wall around the cathedral.  
> At night, he climbs up and watches the sky.  
> He has no telescope, only his eyes and simple wooden tools.  
> In his time, people say: the earth stands still.  
> The sun, the moon, and the stars go around us.  
> Mr X thinks about this for many years.  
> Then he says something new: the sun stands in the middle.  
> The earth is a planet, and it goes around the sun.  
> **Who is Mr X?**

**Svar:** ⬜ Galileo Galilei · ✅ Nicolaus Copernicus · ⬜ Isaac Newton · ⬜ Leonardo da Vinci

**Ord:** *cathedral* — a very big and important church · *telescope* — a tube with glass inside that makes far things look near · *planet* — a big round world that goes around the sun, like the earth

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Why Nobody Feels the Earth Move</summary>

> In the sixteenth century, Mr X is a church official in Poland who studies the sky.  
> Everybody in his time is sure: the earth does not move.  
> We do not feel it move.  
> A stone falls straight down, and birds are not left behind.  
> Every night, the sky seems to turn around us.  
> But the planets make trouble.  
> A planet moves forward for months, then slides backward, then forward again.  
> The old books explain this with circles upon circles.  
> Mr X asks: what if the earth moves too?  
> Then the backward slide is easy to explain.  
> The earth overtakes a slower planet, like a fast runner passing a slow runner.  
> For a short time, the slow runner seems to go backward.  
> **Who is Mr X?**

**Svar:** ⬜ Ptolemy · ⬜ Tycho Brahe · ✅ Nicolaus Copernicus · ⬜ Johannes Kepler

**Ord:** *official* — a person with a job in the church or the government · *overtake* — to catch up with somebody and pass them · *backward* — in the direction behind you

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A Book on His Last Day</summary>

> Mr X, a church official in the north of Poland, writes a big book about the sky.  
> In it, the sun stands in the middle, and the earth moves.  
> He works on the book for about thirty years.  
> He is afraid that people will laugh, so he does not print it.  
> A cardinal in Rome writes and asks him to publish.  
> Then a young mathematician from Germany visits him and pushes him too.  
> At last, the book goes to a printer in Nuremberg.  
> A story tells: the printed book reaches Mr X on the day he dies.  
> The book has a strange preface without a name.  
> It says: this is only a tool for calculation, not the truth.  
> Mr X never writes those words. A church scholar in the printing town adds them without permission.  
> For decades, readers think the words are his.  
> **Who is Mr X?**

**Svar:** ✅ Nicolaus Copernicus · ⬜ Johannes Kepler · ⬜ Galileo Galilei · ⬜ Tycho Brahe

**Ord:** *cardinal* — a very high leader in the Catholic church · *publish* — to print a text so that people can buy and read it · *preface* — the words at the start of a book, before the main text · *calculation* — working with numbers to find an answer

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — An Old Idea with New Numbers</summary>

> Mr X of Poland puts the sun in the middle of the world, in the sixteenth century.  
> The idea itself is old: about 1,800 years earlier, the Greek thinker Aristarchus says the same.  
> Almost nobody follows him.  
> Most scholars follow another Greek, Ptolemy, who keeps the earth in the middle.  
> Mr X finds the old idea in Greek and Roman books.  
> In his handwritten pages, he names Aristarchus, then crosses the lines out.  
> He works for years to make the idea fit the numbers.  
> But his system is not simpler, and its predictions are not better.  
> Critics say: if the earth moves, the stars should seem to shift.  
> They do not shift. Mr X answers: the stars are very, very far away.  
> He proposes, and he calculates, but he cannot prove.  
> The tiny shift of the stars is measured only about three hundred years later.  
> **Who is Mr X?**

**Svar:** ⬜ Johannes Kepler · ⬜ Isaac Newton · ✅ Nicolaus Copernicus · ⬜ Tycho Brahe

**Ord:** *scholar* — a person who studies books deeply · *prediction* — a statement about what will happen · *shift* — to move a little to one side · *prove* — to show that something is surely true

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — A Very Slow Revolution</summary>

> Mr X, a church official in Poland, publishes his book about the moving earth in the sixteenth century.  
> Where does his knowledge come from?  
> He makes few observations of his own, and sea fog often hides the sky.  
> He builds on old star records from Greek and Arab astronomers.  
> Some of his mathematical tools match older tools from astronomers in Persia and Syria.  
> Nobody knows how those ideas reach him.  
> He dedicates the book to the Pope, and for decades the church takes no action.  
> Most astronomers use his tables but keep the earth in the middle.  
> Tycho Brahe offers a middle way: the planets circle the sun, and the sun circles the earth.  
> The church forbids the book more than seventy years after his death, and only "until corrected".  
> Much later, historians call his idea a revolution.  
> The word in his own book title means only this: a turning around.  
> **Who is Mr X?**

**Svar:** ⬜ Johannes Kepler · ⬜ Galileo Galilei · ⬜ Giordano Bruno · ✅ Nicolaus Copernicus

**Ord:** *observation* — looking at something carefully and writing down what you see · *dedicate* — to write a book in honor of a person, and say so at the start · *forbid* — to say that something is not allowed · *revolution* — a big change in how people think or live; the word also means one full turn

</details>

### Galileo Galilei

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Four Small Lights Beside Jupiter</summary>

> Mr X lives in Italy about four hundred years ago.  
> He teaches mathematics at a university.  
> One day he hears about a new tool from the Netherlands.  
> It is a tube with two glass lenses.  
> Far things look close through it.  
> Mr X does not invent it, but he builds a much better one.  
> He shows it to the leaders of Venice from a high tower.  
> They see ships far out at sea, long before other people.  
> Then he points his tube at the night sky.  
> Next to the planet Jupiter he sees four small lights.  
> Night after night, the lights move around Jupiter.  
> So not everything in the sky goes around the earth!  
> **Who is Mr X?**

**Svar:** ⬜ Nicolaus Copernicus · ✅ Galileo Galilei · ⬜ Isaac Newton · ⬜ Leonardo da Vinci

**Ord:** *lens* — a round piece of glass that makes things look bigger or closer · *invent* — to make a new thing that nobody has made before · *planet* — a big ball in space that goes around the sun, like the earth

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The Ball, the Ramp, and the Water Clock</summary>

> Mr X teaches mathematics in Italy, about four hundred years ago.  
> For almost two thousand years, teachers trust an old Greek book.  
> The book says: heavy things fall faster than light things.  
> Mr X says: do not only trust the book, look and measure!  
> A famous story tells: he drops two balls from a tall tower.  
> Historians are not sure the story is true.  
> But we know that he rolls balls down a long wooden ramp.  
> The ramp makes the fall slow, so he can measure the time.  
> He measures with water that drips into a cup.  
> He finds a rule: in double the time, the ball goes four times as far.  
> He also studies a hanging weight, a pendulum, and its swing.  
> Wide swing or small swing, each swing takes about the same time.  
> **Who is Mr X?**

**Svar:** ✅ Galileo Galilei · ⬜ Aristotle · ⬜ Isaac Newton · ⬜ Leonardo da Vinci

**Ord:** *measure* — to find out how long, how heavy, or how fast something is · *ramp* — a flat board that goes up on one side, like a small hill · *pendulum* — a weight that hangs on a string and swings from side to side

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The Sky Is Not Perfect</summary>

> Mr X is an Italian astronomer with a new, strong telescope.  
> Old books teach: everything in the sky is perfect and smooth.  
> Mr X looks at the moon and sees mountains and valleys.  
> From their shadows, he even measures how high they are.  
> He also sees dark spots on the sun, and they move across it.  
> Then, for months, he watches the planet Venus.  
> Venus shows phases like the moon, from thin crescent to almost full.  
> When Venus is full, it looks small and far away.  
> In the old picture of the sky, Venus can never look full.  
> So Venus must go around the sun, not around the earth.  
> This does not yet prove that the earth moves too.  
> But the perfect sky of the old books is gone.  
> **Who is Mr X?**

**Svar:** ⬜ Johannes Kepler · ⬜ Tycho Brahe · ⬜ Nicolaus Copernicus · ✅ Galileo Galilei

**Ord:** *astronomer* — a scientist who studies the stars and the planets · *phase* — the shape of the lit part of the moon or a planet, as we see it · *crescent* — a thin curved shape, like the young moon · *prove* — to show with facts that something is true

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — An Old Man Kneels in Rome</summary>

> Mr X is a famous astronomer in Italy, almost seventy years old.  
> Ninety years before, an astronomer from the north writes: the earth goes around the sun.  
> The Church says: this is against the Bible, so Mr X must not defend it.  
> But now he writes a big book, and in it, the idea wins.  
> The Pope calls him to Rome, to a church court.  
> For weeks, the judges question him.  
> Another thinker is burned in Rome years before, for his ideas about God, but Mr X is not tortured or burned.  
> Still, he must kneel and say: I give up this idea.  
> A later story tells: he whispers, and yet it moves.  
> Historians find no proof for those words.  
> The court bans his book and puts him under house arrest for life.  
> There, going blind, he still writes a new book about how things move.  
> **Who is Mr X?**

**Svar:** ⬜ Giordano Bruno · ⬜ Nicolaus Copernicus · ✅ Galileo Galilei · ⬜ Johannes Kepler

**Ord:** *court* — the place where judges decide if a person did something wrong · *torture* — to hurt a person on purpose to make them talk or obey · *kneel* — to go down on your knees · *house arrest* — a punishment: you must stay in your own home and may not leave

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — More Than Church Against Science</summary>

> Mr X is an Italian astronomer from about four hundred years ago.  
> Later writers tell his story as a war: the Church against science.  
> Historians today say: look closer, it is not so simple.  
> His first opponents are university professors, not priests.  
> They defend the old Greek view, and some refuse even to look through his telescope.  
> Astronomers of the Church in Rome check his discoveries and confirm them.  
> The Pope himself admires him and allows his big book, a talk between three men.  
> The foolish one defends the old view, using the Pope's own favorite argument.  
> The Pope feels mocked, and the friendship ends in a trial.  
> Mr X is right about the planets, but his main proof, from the tides, is wrong.  
> More than 350 years after the trial, the Church says clearly: the judges of that time make mistakes.  
> Power can ban a book, but not the evidence.  
> **Who is Mr X?**

**Svar:** ⬜ Nicolaus Copernicus · ⬜ Charles Darwin · ✅ Galileo Galilei · ⬜ Johannes Kepler

**Ord:** *opponent* — a person who is against you in a fight or a debate · *mock* — to laugh at a person in an unkind way · *tide* — the sea rising and falling along the coast, twice a day · *evidence* — facts that show what is true

</details>

### Reformationen

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Paper for coins</summary>

> Movement X begins in Europe about 500 years ago.  
> Almost everyone in western Europe belongs to one church then.  
> Its leader, the pope, lives in Rome.  
> He wants a huge new church there, and that costs a lot of money.  
> So church men travel from town to town and sell special papers.  
> The church teaches, and buyers believe: this paper makes God's punishment after death shorter.  
> A monk in Germany believes this is wrong.  
> Forgiveness is a gift from God, he believes, and no one can buy it.  
> He writes a list of points against the sale.  
> He sends the list to his bishop, and friends print it.  
> His words spread fast, and the pope says the monk is wrong.  
> But the quarrel grows, and the church in western Europe splits into several churches.  
> **Which movement is Movement X?**

**Svar:** ⬜ The Crusades · ✅ The Protestant Reformation · ⬜ The Renaissance · ⬜ The Great Schism

**Ord:** *pope* — the leader of the church in Rome · *punishment* — something bad that you must go through because you did wrong · *monk* — a religious man who lives a simple life and prays a lot · *forgiveness* — when God, or a person, stops being angry about a wrong thing you did

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Small booklets, big change</summary>

> Movement X begins in Germany about 500 years ago.  
> A monk there starts a quarrel with the church.  
> His friends and his enemies all write about it.  
> Printers translate the texts into German and turn them into thin, cheap booklets.  
> In Europe, printing with movable metal letters is new, only about seventy years old.  
> One press can now make more than a thousand pages in a day.  
> Within a few months, the booklets reach towns all over Germany.  
> Some booklets have pictures, so people who cannot read can follow too.  
> Soon, translators put the Bible into German, English, and other everyday languages.  
> Now a farmer or a weaver can hear the holy book in his own words.  
> Leaders of the old church print answers too, but fewer, and later.  
> For the first time, a quarrel in the church is fought with thousands of cheap booklets.  
> **Which movement is Movement X?**

**Svar:** ⬜ The Renaissance · ⬜ The Enlightenment · ⬜ The Industrial Revolution · ✅ The Protestant Reformation

**Ord:** *booklet* — a small, thin book with only a few pages · *press* — a machine that pushes ink onto paper to make many copies · *translate* — to say or write something again in another language · *weaver* — a person who makes cloth from threads

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Why the rulers choose sides</summary>

> Movement X splits the church in western Europe about 500 years ago.  
> Some rulers join the new churches, and some stay with Rome.  
> Why do they choose as they do?  
> Some truly believe the new teaching, but power and money matter too.  
> A ruler who breaks with Rome can take the church's land, houses, and silver.  
> He can stop sending money to Rome, and he can choose the bishops himself.  
> In Sweden, the king takes church silver and land to pay his debts.  
> In England, the king wants to end his marriage, and the pope says no.  
> So the king makes himself head of the church in his land and closes the monasteries.  
> Rulers who stay with Rome have reasons too, and belief counts there as well.  
> The kings of France and Spain already choose their own bishops. They gain less from a break.  
> After years of quarrel and war in Germany, a treaty is signed. Each prince decides the faith of his land.  
> **Which movement is Movement X?**

**Svar:** ✅ The Protestant Reformation · ⬜ The Great Schism · ⬜ The Crusades · ⬜ The Enlightenment

**Ord:** *bishop* — a high church leader who leads all the churches in one region · *monastery* — a house where monks live, work, and pray · *debt* — money that you owe and must pay back · *treaty* — a written agreement between rulers or lands

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Not one man, but many</summary>

> Movement X begins with a monk in Germany about 500 years ago. But it is not one man's work.  
> In Zürich, a priest named Zwingli preaches only what he finds in the Bible.  
> The city council agrees and removes the pictures and statues from its churches.  
> In Geneva, a Frenchman named Calvin builds a strict new church with tight rules for daily life.  
> His school trains preachers, who carry his teaching to France, the Netherlands, and Scotland.  
> The monk and Zwingli quarrel over the bread and wine in church. They never make peace.  
> Smaller groups baptize only grown people, and both big sides punish them hard.  
> The old church answers too, at a long meeting in the town of Trent.  
> There its leaders state their faith in clear words. They also end the sale of forgiveness papers for money.  
> Priests get better training. New orders of priests open schools as far away as India and Japan.  
> Each side believes it holds the true faith, and history cannot decide that question.  
> **Which movement is Movement X?**

**Svar:** ⬜ The Counter-Reformation · ⬜ The Renaissance · ✅ The Protestant Reformation · ⬜ The Great Schism

**Ord:** *city council* — the group of men who rule a city · *preacher* — a person who speaks about religion to a group of people · *baptize* — to pour water on a person, or dip the person in water, to make him or her a member of the church · *order* — here: a group of priests or monks who live by the same rules

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Faith, power, or bread?</summary>

> Movement X splits the church in western Europe in the sixteenth century.  
> Historians agree on the events. But they argue about the cause: faith, power, or everyday life?  
> Older books tell the story of one brave monk in Germany and his conscience.  
> Later historians look at the princes and free cities that use the quarrel to win power.  
> Others look at the farmers and the poor of the towns.  
> Farmers in Germany soon read the new ideas as freedom from their lords too.  
> They rise up, and the princes crush them. Perhaps a hundred thousand die, and the monk takes the princes' side.  
> Wars over faith and power follow, in France, in the Netherlands, and across central Europe.  
> The biggest of them lasts thirty years.  
> Some regions lose a third of their people to fighting, hunger, and sickness.  
> One effect lasts: the new churches want every child to read the Bible, so village schools spread.  
> The old church answers with new schools of its own, and reading grows on both sides.  
> **Which movement is Movement X?**

**Svar:** ⬜ The Renaissance · ⬜ The Enlightenment · ⬜ The Counter-Reformation · ✅ The Protestant Reformation

**Ord:** *cause* — the reason why something happens · *conscience* — the inner feeling that tells you what is right and wrong · *lord* — a powerful man who owns the land that farmers work on · *region* — a part of a land, bigger than a town

</details>

### Martin Luther

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Monk Who Is Afraid of God</summary>

> Brother X lives in Germany, about 500 years ago.  
> As a young man, he studies to become a lawyer.  
> One day, a thunderstorm catches him on an open road.  
> Lightning strikes close, and he is very afraid.  
> In his fear, he calls to a saint: help me, and I will become a monk.  
> He keeps his promise and enters a monastery.  
> There he prays, he works, and he fasts.  
> But he still feels afraid of God.  
> I can never be good enough, he thinks.  
> Then he reads an old letter in the Bible, again and again.  
> He finds a new idea there: God's forgiveness is a free gift, he believes.  
> No one can earn it, and no one can buy it. This idea will soon split the church in Europe.  
> **Who is Brother X?**

**Svar:** ⬜ Johannes Gutenberg · ✅ Martin Luther · ⬜ John Calvin · ⬜ Ignatius of Loyola

**Ord:** *lawyer* — a person who knows the law and helps people in court · *saint* — a holy person; some Christians ask saints to help them · *monastery* — a house where monks live, pray, and work · *fast* — here: to eat no food for a time, for God

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Ninety-Five Points Against a Sale</summary>

> Mr X is a monk and teacher in Wittenberg, Germany, about 500 years ago.  
> A preacher comes to the area and sells letters of pardon from the church.  
> The church calls these letters indulgences.  
> Buy a letter, the preacher says, and the punishment for your sins is gone.  
> Part of the money helps to build a great new church in Rome.  
> Mr X is angry: forgiveness is not for sale, he believes.  
> He writes ninety-five short points against the sale, in Latin, for a debate.  
> He sends them in a letter to the archbishop.  
> A story tells that he also nails them to the church door.  
> Historians are not sure the door story is true.  
> Printers copy the points, and friends translate them into German.  
> Within a few months, people read them all over Germany.  
> **Who is Mr X?**

**Svar:** ⬜ Jan Hus · ⬜ Erasmus · ✅ Martin Luther · ⬜ John Calvin

**Ord:** *pardon* — forgiveness for a bad thing you did · *indulgence* — a church letter; the church teaches that it takes away punishment for sins · *sin* — a bad act against God's rules, in a religion · *archbishop* — a high leader of the church over a big area

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — I Cannot Take It Back</summary>

> Mr X is a monk from Wittenberg who writes against the sale of pardons.  
> His books spread fast, and the pope throws him out of the church.  
> About 500 years ago, the young emperor calls him to the city of Worms.  
> Princes, bishops, and the emperor wait for him in a great hall.  
> - Do you take back what you have written? they ask.  
> He asks for one day to think.  
> Next day he answers: no, unless the Bible or clear reason proves him wrong.  
> The first printed reports add a famous line: here I stand, I can do no other.  
> It is not in the official record, so historians doubt it.  
> On the road home, masked riders take him away.  
> A friendly prince hides him in a castle, with a new name and a beard.  
> Soon the emperor declares him an outlaw: anyone may now kill him without punishment.  
> **Who is Mr X?**

**Svar:** ✅ Martin Luther · ⬜ Jan Hus · ⬜ Thomas More · ⬜ John Calvin

**Ord:** *emperor* — a ruler over many lands and many princes · *take back* — to say that your own words were wrong · *outlaw* — a person outside the law; no one is punished for hurting him · *prince* — the ruler of one land inside the empire

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A Bible for the Mother in the House</summary>

> Mr X is a German monk and teacher, about 500 years ago.  
> In church, the Bible is read in Latin, a language few people know.  
> Hidden in a castle, Mr X begins to translate.  
> He works from the old Greek text, not from the church's Latin.  
> He wants words that a mother in the house and a child in the street can understand.  
> In about eleven weeks, the New Testament is ready in German.  
> Printers sell it in the thousands and print it again and again.  
> German has many dialects, and his book helps shape one written German.  
> He asks towns to open schools for girls and boys, so all can read it.  
> Church leaders in Rome say: the church must guide the reading.  
> Mr X says: every believer can read and judge for himself.  
> Each side believes it is right, and the question still divides churches today.  
> **Who is Mr X?**

**Svar:** ⬜ Erasmus · ⬜ Johannes Gutenberg · ⬜ William Tyndale · ✅ Martin Luther

**Ord:** *Latin* — the old language of Rome; the church uses it for centuries · *translate* — to put a text from one language into another · *New Testament* — the second part of the Christian Bible; it tells about Jesus and his followers · *dialect* — the way a language is spoken in one area

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — A Hundred Volumes and a Dark Page</summary>

> Mr X is a German monk whose quarrel with Rome splits the western church, about 500 years ago.  
> Few people from his time leave so many sources.  
> His collected works fill more than one hundred thick volumes.  
> More than two thousand of his letters survive.  
> Students even write down his talk at the dinner table.  
> But they write in haste or from memory, and later editors change the words, so historians read them with care.  
> Even the famous story of the church door rests on two late reports, written decades after the event.  
> His legacy is divided too.  
> In his old age, he writes books full of hate against Jews.  
> Centuries later, others use these books for their own hate, and historians study how.  
> Churches that follow his teaching today reject these words.  
> In our own century, the pope prays with leaders of those churches, in Sweden.  
> **Who is Mr X?**

**Svar:** ⬜ John Calvin · ⬜ Jan Hus · ⬜ Ulrich Zwingli · ✅ Martin Luther

**Ord:** *source* — a text or thing from the past that gives us knowledge · *volume* — one book in a long row of books that belong together · *legacy* — what a person leaves behind for later times, good and bad · *reject* — to say clearly: this is wrong, we do not accept it

</details>

### Industriella revolutionen

<details>
<summary><b>Kort 1 · Årskurs 6</b> — From wheel to mill by the river</summary>

> Revolution X begins in Britain about 250 years ago.  
> At first, women spin cotton thread by hand at home.  
> They turn a small wheel next to the fire.  
> New machines can spin much more thread at once.  
> Workers build a large mill beside a river.  
> A big wheel in the river turns the machines inside.  
> Later, a new engine burns coal for power instead.  
> Now a mill does not need a river nearby.  
> A town in the north of England grows very fast.  
> Thousands of people move there to work in the mills.  
> Tall chimneys rise over the town, and smoke fills the sky.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The Agricultural Revolution · ✅ The Industrial Revolution · ⬜ The Scientific Revolution · ⬜ The French Revolution

**Ord:** *spin* — to turn cotton or wool into long thread · *mill* — a large building full of machines that make cloth · *engine* — a machine that makes power from burning fuel · *chimney* — a tall pipe that carries smoke up into the sky

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Twelve hours in the mill</summary>

> About 200 years ago, Revolution X changes life for working families.  
> Children as young as six work inside the mills.  
> A working day often lasts twelve to fourteen hours.  
> Small children crawl under moving machines to sweep up loose cotton.  
> Other children work far underground, pulling carts of coal in mines.  
> Families move from small villages into fast-growing cities.  
> Many of them live crowded together in one small room.  
> There is little clean water, and sickness spreads fast.  
> A disease called cholera kills tens of thousands in poor city streets.  
> Slowly, new laws limit how young a working child can be.  
> Workers also start to join together in groups called unions.  
> Together, they ask for shorter days and safer machines.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The French Revolution · ✅ The Industrial Revolution · ⬜ The Agricultural Revolution · ⬜ The American Revolution

**Ord:** *mine* — a deep hole or tunnel where workers dig out coal · *cholera* — a dangerous disease that spreads through dirty water · *union* — a group of workers who join together to ask for better and safer work · *crowded* — full of too many people in a small space

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The engine that changes distance</summary>

> Revolution X depends on a new kind of engine.  
> Earlier engines already pump water out of coal mines.  
> An engineer named Watt makes this kind of engine far better.  
> He receives a patent for his improved engine about 250 years ago.  
> Mines and ironworks use his engines from the 1770s.  
> From the 1780s, his engines also turn machines in mills.  
> Britain also mines huge amounts of coal and iron.  
> Workers first move heavy goods along new canals by boat.  
> In 1830, the first passenger railway links two English cities.  
> A steam engine now pulls both passengers and goods.  
> Soon, steam also powers ships on wide rivers and across oceans.  
> Journeys that once took days can now take only hours.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The Scientific Revolution · ⬜ The Agricultural Revolution · ✅ The Industrial Revolution · ⬜ The Digital Revolution

**Ord:** *engineer* — a person who designs and builds machines or structures · *patent* — an official paper that gives one person the right to an invention · *canal* — a waterway that people dig for boats to travel on · *passenger* — a person who travels in a vehicle but does not drive it

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Cotton from three continents</summary>

> Revolution X starts in Britain, but it soon changes the whole world.  
> British mills need huge amounts of raw cotton every year.  
> Enslaved workers in the southern United States pick most of it.  
> Farmers in India and Egypt also grow cotton for British mills.  
> For centuries, skilled weavers in India make fine cotton cloth by hand.  
> Now cheap cloth from British mills floods their local markets.  
> Many Indian weavers slowly lose their work and their income.  
> Other countries soon build mills and factories of their own.  
> Belgium and parts of Germany build mills within a few decades.  
> The United States and later Japan follow a similar path.  
> Everywhere, burning coal sends smoke and gas into the air.  
> Over two centuries, this gas slowly warms the whole planet.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The Scientific Revolution · ⬜ The American Revolution · ✅ The Industrial Revolution · ⬜ The Agricultural Revolution

**Ord:** *enslaved* — forced to work without pay and owned by another person · *weaver* — a person who makes cloth from thread, often by hand · *income* — the money a person earns from work · *decade* — a period of ten years

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Revolution or slow change?</summary>

> Historians even argue about the word revolution itself.  
> Some changes come fast, like the first steam railways.  
> But many other changes take a full century to spread.  
> So some historians prefer to speak of slow, steady change.  
> Others still call it a true revolution in how people live.  
> A second question asks why this begins in Britain first.  
> Britain has coal, money to invest, and colonies for raw goods.  
> It also has wide markets and, some say, well-paid workers.  
> Historians compare Britain with wealthy regions in China at the time.  
> Some historians say both regions look similarly advanced for a long time.  
> Then their paths separate, and historians call this the great divergence.  
> Historians read factory inspectors' reports, church records, and old wage lists.  
> **Which revolution is Revolution X?**

**Svar:** ✅ The Industrial Revolution · ⬜ The Scientific Revolution · ⬜ The Agricultural Revolution · ⬜ The French Revolution

**Ord:** *historian* — a person who studies and writes about the past · *colony* — a land ruled and used by another, more powerful country · *divergence* — the point where two similar things start to become very different · *inspector* — a person whose job is to check that rules are followed

</details>

### Charles Darwin

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Beetles, Seasickness, and Five Years at Sea</summary>

> Mr X is a young man in Britain, almost 200 years ago.  
> He studies medicine in Edinburgh but hates it.  
> Blood and pain make him feel sick.  
> He collects rare beetles as a hobby.  
> His father wants him to work for the church instead.  
> Then a ship captain invites him to sail.  
> The small ship sails around the whole world.  
> The long voyage lasts almost five years.  
> Mr X feels seasick almost every day at sea.  
> On islands in the Pacific, he meets giant tortoises.  
> He also sees strange birds that live nowhere else.  
> **Who is Mr X?**

**Svar:** ✅ Charles Darwin · ⬜ Alfred Russel Wallace · ⬜ Louis Pasteur · ⬜ Carl Linnaeus

**Ord:** *beetle* — a small insect with a hard shiny cover over its wings · *voyage* — a long journey by ship · *seasick* — feeling sick because a ship moves on the waves · *tortoise* — a slow animal with a hard shell that walks on land

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Twenty Years of Notebooks and a Letter from Asia</summary>

> Mr X returns to England after five years at sea.  
> For years, he thinks about living things and change.  
> He notices something: animals fit their surroundings well.  
> Animals that fit well survive and have young.  
> Over a very long time, this slowly changes all living things.  
> Mr X calls this idea natural selection.  
> He fills notebook after notebook with his ideas.  
> Twenty years pass, and he tells almost nobody.  
> Then a letter arrives from a naturalist in Asia.  
> That man, Wallace, has the very same idea.  
> The next year, Mr X finally publishes his famous book.  
> **Who is Mr X?**

**Svar:** ✅ Charles Darwin · ⬜ Alfred Russel Wallace · ⬜ Jean-Baptiste Lamarck · ⬜ Gregor Mendel

**Ord:** *survive* — to stay alive · *natural selection* — nature lets the best-fitting animals and plants survive and have young · *naturalist* — a person who studies plants, animals, and nature

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Pigeons, Barnacles, and Patient Experiments</summary>

> More than 150 years ago, Mr X works quietly at home in England.  
> He breeds many different kinds of pigeons himself.  
> Breeders already change pigeons a lot by choosing parents.  
> Mr X wonders if nature chooses in the same way.  
> For eight long years, he studies tiny sea barnacles.  
> He carefully describes every known kind of barnacle.  
> In his garden, he studies unusual orchid flowers.  
> He watches how earthworms slowly move soil under grass.  
> He works alone and patiently tests idea after idea.  
> He writes many letters to farmers and gardeners.  
> Slowly, many small experiments at home support one big idea.  
> **Who is Mr X?**

**Svar:** ⬜ Gregor Mendel · ✅ Charles Darwin · ⬜ Carl Linnaeus · ⬜ Jean-Baptiste Lamarck

**Ord:** *breed* — to keep animals or plants so they have young with chosen traits · *barnacle* — a small sea animal that sticks tightly to rocks or ships · *orchid* — a flower with an unusual shape, often grown for its beauty

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A Debate in Oxford, Retold Many Ways</summary>

> In 1859, Mr X publishes a book that changes science.  
> It says that all living things slowly change over time.  
> Many people read it, and a big argument starts.  
> The next year, scholars debate the book in Oxford.  
> A bishop and a scientist argue in front of a crowd.  
> Later writers describe the debate in different ways.  
> Even people who are there remember the words differently.  
> Some religious leaders feel angry about the new idea.  
> Other believers see no conflict with their own faith.  
> Mr X himself stays quietly at home, often unwell.  
> He dies more than twenty years later, old and respected.  
> He is buried with honor in Westminster Abbey.  
> **Who is Mr X?**

**Svar:** ⬜ Galileo Galilei · ⬜ Isaac Newton · ✅ Charles Darwin · ⬜ Louis Pasteur

**Ord:** *bishop* — a senior leader in the Christian church · *debate* — a formal argument between people with different views · *faith* — strong belief, often in God or a religion

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — A Tree Sketch, a Second Discoverer, and a Misused Legacy</summary>

> Mr X visits Pacific islands as a young man.  
> Later stories say finches teach him everything at once.  
> In fact, he hardly notes which island each finch comes from.  
> Mockingbirds interest him more at the time.  
> Later scientists and school books shape the famous finch story.  
> In the 1980s, a historian shows the story is a legend.  
> Some historians ask if Wallace, another naturalist, deserves more credit.  
> We know his ideas from notebooks and many letters.  
> One page from 1837 shows a small sketch of a tree.  
> Above the sketch, he writes two words: I think.  
> Other men later misuse his ideas to excuse racism.  
> He never calls for such policies himself.  
> **Who is Mr X?**

**Svar:** ⬜ Alfred Russel Wallace · ✅ Charles Darwin · ⬜ Carl Linnaeus · ⬜ Jean-Baptiste Lamarck

**Ord:** *legend* — a well-known story that is not fully true · *naturalist* — a person who studies plants, animals, and nature · *sketch* — a quick, simple drawing · *credit* — praise or recognition for doing something

</details>

### Karl Marx

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Writer in a Cold Room</summary>

> Mr X lives in a small flat in London, about 175 years ago.  
> Before that, in Germany, the government closes his newspaper, so he leaves.  
> Every day, Mr X sits at a small table and writes.  
> He writes about poor workers and rich factory owners.  
> The workers do the work, he says, but the owners get rich.  
> The family is very poor, and the flat is cold in winter.  
> Some of his children become sick and die.  
> His good friend Friedrich Engels lives in Manchester.  
> The Engels family owns part of a big cotton mill.  
> Friedrich sends money again and again, so the family can eat.  
> Mr X keeps writing, year after year.  
> **Who is Mr X?**

**Svar:** ⬜ Friedrich Engels · ✅ Karl Marx · ⬜ Charles Dickens · ⬜ Adam Smith

**Ord:** *government* — the group of people who rule a country · *cotton* — a soft plant fibre used to make cloth · *mill* — a big factory, here one that spins cotton into thread

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A Small Book for the Workers</summary>

> Mr X lives in Brussels, in Belgium.  
> It is the year 1848.  
> With a friend who worked in Manchester, he writes a short book.  
> It is for a small group of workers.  
> The book says: history is a story of struggle.  
> In every age, some people own the tools and the land.  
> Other people work for them, for low pay.  
> The book calls this a struggle between classes.  
> It ends with a call: workers of all lands, unite!  
> The book is short, cheap, and easy to print.  
> At first, almost no one reads it.  
> Much later, it becomes one of the most printed books ever.  
> **Who is Mr X?**

**Svar:** ⬜ Robert Owen · ⬜ Vladimir Lenin · ✅ Karl Marx · ⬜ Georg Hegel

**Ord:** *struggle* — a hard fight to get or keep something · *class* — a group of people with a similar place in society · *unite* — to join together as one group

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Where Does Profit Come From?</summary>

> Mr X studies in the reading room of a great London museum.  
> He reads there year after year to write a huge new book.  
> The book comes out about 160 years ago.  
> It asks a hard question: where does profit come from?  
> A worker makes goods worth more than his pay, the book says.  
> The owner of the factory keeps the extra value.  
> Mr X calls this extra value surplus.  
> For proof, he reads real government reports.  
> The reports describe men, women, and children at the machines.  
> Many work twelve hours a day or more.  
> The book is thick, and few people finish it while he is alive.  
> **Who is Mr X?**

**Svar:** ✅ Karl Marx · ⬜ Adam Smith · ⬜ John Stuart Mill · ⬜ Friedrich Engels

**Ord:** *profit* — money a business earns above its costs · *value* — how much something is worth · *surplus* — an amount left over, more than what is needed

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A Man Who Cannot Go Home</summary>

> Mr X is born more than 200 years ago in Trier.  
> Trier is a town in Prussia, a German state.  
> His family has Jewish roots, and his father is a lawyer.  
> Mr X studies law and philosophy in Bonn and Berlin.  
> Then he becomes the editor of a newspaper.  
> After a few months, the government closes the newspaper.  
> He leaves the country and lives most of his life in exile.  
> He lives first in Paris, then in Brussels, then in London.  
> His wife Jenny comes from a noble family in Germany.  
> Jenny copies his messy handwriting into clean pages for the printer.  
> He dies more than 140 years ago.  
> Only about eleven people come to his funeral.  
> **Who is Mr X?**

**Svar:** ⬜ Georg Hegel · ⬜ Friedrich Engels · ⬜ Charles Dickens · ✅ Karl Marx

**Ord:** *editor* — a person who runs a newspaper and decides what it prints · *exile* — living away from your home country, often because you cannot go back · *noble* — belonging to a family of high rank

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — A Name That Outlives the Man</summary>

> Mr X writes about history, work, and money, more than 150 years ago.  
> He dies more than 140 years ago.  
> Later, in the twentieth century, states in Russia and China take his name.  
> These states rule with violence and famine that Mr X never sees.  
> Historians ask a hard question: how much of this is his fault?  
> Many historians separate the thinker from the later movements named after him.  
> His old friend Friedrich Engels later reports one sentence.  
> Some followers in France use his name for their ideas.  
> Mr X says about them: I am not one of them.  
> No one else records this sentence, so historians treat it with care.  
> Today, some economists still study his idea of crisis in the market.  
> Many historians say the future does not turn out as he expects.  
> **Who is Mr X?**

**Svar:** ⬜ Vladimir Lenin · ✅ Karl Marx · ⬜ Friedrich Engels · ⬜ Georg Hegel

**Ord:** *famine* — a time when many people have little or no food · *movement* — a group of people who work together for one big idea · *economist* — a person who studies money, work, and trade · *crisis* — a very hard and dangerous time, often in money or the economy

</details>

### Amerikanska revolutionen

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Tea in the harbor</summary>

> Revolution X begins about 250 years ago.  
> Thirteen colonies sit on the east coast of North America.  
> Settlers there live under a king who rules from far away.  
> His country has just ended a long, costly war.  
> He needs money, so his parliament puts new taxes on the colonies.  
> The colonists have no voice in his faraway parliament.  
> No taxation without representation, they say.  
> One cold night, colonists board three ships in the harbor of Boston.  
> They break open chests of tea and dump it into the water.  
> The king's government answers with harsh new laws.  
> Anger now spreads fast across all thirteen colonies.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The Glorious Revolution · ✅ The American Revolution · ⬜ The French Revolution · ⬜ The Industrial Revolution

**Ord:** *colonies* — lands ruled by another, faraway country · *parliament* — a group of people who make the laws of a country · *taxes* — money that people must pay to their government · *representation* — having someone who speaks and votes for you

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A declaration, and a war</summary>

> Revolution X turns into full war about 250 years ago.  
> Colonists take up arms against the king's soldiers.  
> A tall general from Virginia leads the colonial army.  
> Representatives from all thirteen colonies meet.  
> In 1776, they declare independence from the king.  
> Their declaration states that all men are created equal.  
> Yet about one in five people in the colonies live enslaved.  
> The declaration does not free them.  
> Some colonists disagree with the revolt and stay loyal to the king.  
> The new nation must now win its independence in war.  
> The king's army is strong, and the war lasts for years.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The Russian Revolution · ⬜ The Haitian Revolution · ✅ The American Revolution · ⬜ The Glorious Revolution

**Ord:** *representatives* — people chosen to speak and act for a group · *declare* — to say something clearly and officially · *enslaved* — forced to work for no pay and with no freedom · *loyal* — staying faithful and true to someone

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Whose liberty?</summary>

> Revolution X promises liberty to the colonies.  
> But that liberty is not equal for everyone.  
> Most enslaved people gain nothing from the new liberty.  
> Some northern states begin to end slavery slowly, but the south keeps it.  
> Free women support the cause with money, letters, and even secret spying.  
> Still, almost no woman gains the right to vote.  
> Loyalists, who wish to stay under the king, become outsiders overnight.  
> Tens of thousands leave for Canada or Britain, losing land and property.  
> Most Native nations along the frontier side with the king during the war.  
> They fear that independent settlers will take even more of their land.  
> After the war, that fear comes true again and again.  
> So the liberty of some becomes the loss of others.  
> **Which revolution is Revolution X?**

**Svar:** ✅ The American Revolution · ⬜ The Mexican Revolution · ⬜ The Industrial Revolution · ⬜ The Haitian Revolution

**Ord:** *liberty* — freedom to live and choose as you wish · *loyalists* — people who stay faithful to the old king · *frontier* — the edge of settled land, close to the wild land beyond · *property* — land or things that a person owns

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A costly rescue at sea</summary>

> After two years of war, Revolution X is going badly for the colonies.  
> The colonial army loses battle after battle.  
> It is often short of food, pay, and supplies.  
> Then the colonists win a big battle in the north.  
> Now France decides to help, partly to weaken its old rival across the sea.  
> The next year, French ships, soldiers, weapons, and money arrive.  
> Three years later, French warships trap the king's army near the coast.  
> Surrounded by land and sea, that army finally surrenders.  
> The colonies have now won their war.  
> But helping costs the French king enormous sums of money.  
> His treasury sinks even deeper into debt.  
> That royal debt soon helps cause serious trouble back home too.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The Mexican Revolution · ✅ The American Revolution · ⬜ The Russian Revolution · ⬜ The Glorious Revolution

**Ord:** *rival* — a country or person competing against another · *surrenders* — stops fighting and admits defeat · *treasury* — the money and wealth that a government or king controls · *debt* — money that you owe and must pay back

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — One revolution's long echo</summary>

> Historians still debate the true impact of Revolution X.  
> Is it a true revolution, or only a change of rulers?  
> The new republic replaces a distant king with elected leaders.  
> Yet plantation slavery grows for decades after.  
> Freedom of religion and a free press become law, new ideas for the time.  
> A written constitution, ratified in the 1780s, still shapes government today.  
> Its early history relies on letters, diaries, and army records, many saved by chance.  
> Newspapers of the time already tell the story differently, depending on who prints them.  
> One generation later, the idea inspires new fighters far to the south.  
> In South America, a general named Simón Bolívar reads about the northern revolt.  
> He leads years of war so his own homeland can also become independent.  
> So one revolution's words echo across a continent, long after Revolution X itself ends.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The French Revolution · ⬜ The Industrial Revolution · ✅ The American Revolution · ⬜ The Haitian Revolution

**Ord:** *ratified* — officially approved and accepted · *republic* — a country led by chosen leaders, not a king · *inspires* — gives someone else a new idea or wish to act · *homeland* — the country where a person is born and belongs

</details>

### George Washington

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The General Who Will Not Quit</summary>

> General X grows up on a farm in Virginia.  
> As a young man, he works as a surveyor.  
> He walks through forests and measures wild land as his job.  
> Years later, thirteen colonies in North America rise up against the British king.  
> Leaders choose General X to lead their new army.  
> His soldiers are mostly farmers, not trained soldiers.  
> In many early battles, his army must retreat.  
> On a freezing Christmas night, he crosses an icy river in the dark.  
> His tired men win a small battle early the next morning.  
> The next winter, his army camps in cold and mud with little food.  
> About two thousand of his soldiers die from sickness and cold that winter.  
> General X stays with his men, and the army holds together.  
> **Who is General X?**

**Svar:** ⬜ Napoleon Bonaparte · ✅ George Washington · ⬜ Simón Bolívar · ⬜ Alexander Hamilton

**Ord:** *surveyor* — a person whose job is to measure and map land · *colonies* — lands ruled by a country far away, across the sea · *retreat* — to move back and away from a battle, not forward

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The General Who Gives Back His Command</summary>

> Mr X leads thirteen colonies in a long war against their British king.  
> Near the end of the war, one of his officers writes him a letter.  
> The officer suggests that Mr X should become a king.  
> Mr X refuses at once, angry at the idea.  
> The colonies win the war, with important help from France.  
> Many expect Mr X to become the most powerful man in the land.  
> Instead, he goes in uniform to the new lawmakers and hands back his commission.  
> He gives up all his power and goes home to his farm.  
> Across Europe, people are amazed: a winning general who does not want to rule.  
> A few years later, leaders choose him as the country's first president.  
> After two terms, he steps down and goes home again.  
> Today, the capital of his country carries his name.  
> **Who is Mr X?**

**Svar:** ⬜ John Adams · ⬜ Thomas Jefferson · ✅ George Washington · ⬜ Benjamin Franklin

**Ord:** *commission* — the official paper that gives an officer his rank and command · *term* — a fixed period of years in a job like president · *capital* — the main city of a country, where its leaders work · *refuse* — to say no, and mean it

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A Farm Built on Slavery</summary>

> Mr X owns a large farm called Mount Vernon, in Virginia.  
> Hundreds of enslaved people live and work there, forced and unpaid.  
> Mr X personally owns more than one hundred of these people.  
> One enslaved woman named Ona works as his wife's personal maid.  
> While Mr X serves as the country's first president, Ona plans her escape.  
> She flees north to a city and never goes back.  
> Mr X tries hard to find her and bring her back.  
> Ona is never caught.  
> She lives free in a northern town for the rest of her life.  
> In his will, Mr X gives an order: free the people I own.  
> But the will delays this until his wife also dies.  
> Historians see him as both a founder and an enslaver.  
> **Who is Mr X?**

**Svar:** ✅ George Washington · ⬜ Thomas Jefferson · ⬜ Abraham Lincoln · ⬜ Benjamin Franklin

**Ord:** *enslaved* — forced to work for no pay and with no freedom, as property · *will* — a paper that says what happens to a person's things after they die · *escape* — to get away and become free

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A Shot in the Forest, a World at War</summary>

> As a young officer, Mr X serves the British in North America.  
> Britain and France both want the same forest land, further west.  
> Mr X and his Native allies lead a small group into the forest.  
> In a short, sudden fight, several French soldiers are killed.  
> Weeks later, young Mr X must surrender a small fort to French forces.  
> This small clash in the forest helps start a much bigger war.  
> Soon Britain and France fight each other on several continents.  
> Years later, the colonies rise up, and Mr X leads their new army.  
> Now France becomes his key ally against the British king.  
> Near a coastal town, Mr X and French troops trap a British army.  
> A French fleet blocks the sea, so no escape is possible by water.  
> The trapped army surrenders, and Britain soon starts to seek peace.  
> **Who is Mr X?**

**Svar:** ⬜ Napoleon Bonaparte · ⬜ Alexander Hamilton · ⬜ John Adams · ✅ George Washington

**Ord:** *ally* — a country or group that fights on your side · *surrender* — to stop fighting and admit defeat · *fleet* — a large group of warships that sail together

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Cherry Tree That Never Was</summary>

> Mr X dies at the end of the eighteenth century.  
> A few years later, a preacher and writer publishes a short book about him.  
> The book tells a sweet story: young Mr X damages a cherry tree.  
> When his father asks who did it, the boy says: I cannot tell a lie.  
> No letter, diary, or witness from Mr X's own lifetime mentions this story.  
> Historians agree: the writer most likely invents the whole scene.  
> Still, generations of children learn the story as if it is true.  
> The new nation wants a perfect founding hero, honest and brave.  
> Historians instead study his letters and account books.  
> These pages record daily details, from crops sold to money spent.  
> From small, dry facts, historians slowly rebuild a truer picture of his life.  
> This picture is less simple than the cherry tree story.  
> **Who is Mr X?**

**Svar:** ⬜ Abraham Lincoln · ✅ George Washington · ⬜ Thomas Jefferson · ⬜ John Adams

**Ord:** *invent* — to make up something that is not true or real · *witness* — a person who sees an event happen and can tell about it · *generations* — groups of people born and living around the same time

</details>

### Franska revolutionen

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Not enough bread</summary>

> Revolution X begins in France in 1789, almost 240 years ago.  
> Bad harvests make bread very expensive.  
> Poor families cannot buy enough food.  
> Society here has three big groups, called estates.  
> The first estate is priests, and the second is nobles.  
> The third estate is everyone else, almost everybody.  
> The third estate pays nearly all the taxes.  
> Anger grows over hunger and unfair taxes.  
> In Paris, the capital city, a crowd gathers.  
> The crowd attacks an old fortress used as a prison.  
> Only seven prisoners are inside the huge building.  
> The crowd breaks in and takes the gunpowder stored there.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The American Revolution · ✅ The French Revolution · ⬜ The Russian Revolution · ⬜ The Industrial Revolution

**Ord:** *estate* — one of the big social groups in an old kingdom · *noble* — a person born into a rich, powerful family · *fortress* — a strong building built to defend against attack · *tax* — money that people must pay to a government

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A king tries to run</summary>

> In France, Revolution X is only a few months old.  
> A new parliament takes power from the king.  
> Nobles must give up their old special rights.  
> The rich must now pay taxes too.  
> The parliament then writes a declaration of rights.  
> All men are born free and equal, it states.  
> Free speech and fair trials become new rights.  
> A few weeks later, bread is still hard to find in Paris.  
> Thousands of women march to the king's palace outside the city.  
> They demand bread, and they want the king to live in Paris.  
> He agrees, and the royal family moves to the city under guard.  
> Two years later, the king tries to flee in secret, but he is caught.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The Glorious Revolution · ⬜ The Mexican Revolution · ✅ The French Revolution · ⬜ The Haitian Revolution

**Ord:** *parliament* — a group of people chosen to make laws for a country · *declaration* — an official written statement that says something clearly · *guard* — a soldier who protects a person or a place · *flee* — to run away from danger, often in secret

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The king stands trial</summary>

> In France, Revolution X removes the old king's power step by step.  
> After three years, its leaders end the monarchy and declare a republic.  
> The former king stands trial for crimes against the new nation.  
> Soon after, the new republic executes him.  
> Fear of enemies, at home and abroad, grows fast.  
> A period called the Terror begins.  
> Courts work quickly, and they sentence thousands of suspected enemies to death.  
> Official records count about seventeen thousand such deaths in one year.  
> Many more die in prisons or in fighting across the country.  
> One powerful leader, Robespierre, leads much of this.  
> The following year, his own allies turn against him, and he is executed too.  
> **Which revolution is Revolution X?**

**Svar:** ✅ The French Revolution · ⬜ The Russian Revolution · ⬜ The American Revolution · ⬜ The Haitian Revolution

**Ord:** *monarchy* — a country ruled by a king or queen · *republic* — a state without a king, led by chosen representatives · *trial* — a formal process in court that decides if someone is guilty · *execute* — to kill a person as a legal punishment

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Not Yet for Everyone</summary>

> Revolution X promises liberty, equality, and brotherhood for all.  
> At first, though, only some men can vote.  
> A woman writer named Olympe de Gouges disagrees.  
> She writes her own declaration for the rights of woman.  
> She demands votes and equal rights for women too.  
> Later she attacks the new leaders in print.  
> They have her executed.  
> Far away, in the colony of Saint-Domingue, enslaved people rise up against their enslavers.  
> A few years later, the parliament in France abolishes slavery in its colonies.  
> It is one of the first such laws anywhere in the world.  
> The new government also creates a new system of measurement.  
> Meters and kilograms slowly replace hundreds of old local units.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The Haitian Revolution · ✅ The French Revolution · ⬜ The Industrial Revolution · ⬜ The Glorious Revolution

**Ord:** *liberty* — freedom; the right to live and choose without being controlled by others · *colony* — a land ruled and controlled by another, distant country · *abolish* — to end something completely, especially by law · *enslaved* — forced by others to work without freedom or pay

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — One revolution, many stories</summary>

> Historians still argue about the causes of Revolution X.  
> Older historians tell a story of class struggle.  
> In this story, a rising middle class overthrows a tired old nobility.  
> Later historians, called revisionists, question this simple picture.  
> They study pamphlets, letters, and police reports from Paris and the provinces.  
> These sources show many local causes, not just one big class conflict.  
> Politics, personal networks, and pure chance also matter.  
> Historians also compare Revolution X with the uprising in Saint-Domingue.  
> Enslaved people there use the same words about liberty and rights.  
> Yet their revolution follows its own separate path to freedom.  
> The comparison shows how one revolution's ideals can travel far.  
> Every generation of historians asks new questions of the same old sources.  
> **Which revolution is Revolution X?**

**Svar:** ⬜ The Russian Revolution · ⬜ The Mexican Revolution · ⬜ The Glorious Revolution · ✅ The French Revolution

**Ord:** *pamphlet* — a small, thin printed text that argues for an idea · *revisionist* — a historian who questions and rewrites an older, accepted story · *nobility* — the group of people born into powerful, high-ranking families · *source* — an old text or thing that gives us knowledge about the past

</details>

### Napoleon Bonaparte

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Boy from an Island Becomes a General</summary>

> Mr X is born on a small island.  
> The island is called Corsica, near Italy.  
> France takes the island the year before he is born.  
> All his life, he speaks French with an accent.  
> He leaves home young to go to a military school in France.  
> There he studies maps, math, and the science of cannons.  
> He becomes an officer who commands cannons.  
> At this time, the revolution in France changes everything.  
> Old rules about noble birth and rank start to break.  
> Now, a soldier can rise fast through skill alone.  
> Mr X rises very fast, and becomes a general at only twenty-four.  
> **Who is Mr X?**

**Svar:** ✅ Napoleon Bonaparte · ⬜ Julius Caesar · ⬜ Charlemagne · ⬜ Otto von Bismarck

**Ord:** *officer* — a leader in the army, with soldiers under his command · *cannons* — big heavy guns that shoot iron balls far away · *revolution* — a fast, big change in a country's rulers and rules · *rank* — your level or position in an army or a group

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The Man Who Crowns Himself</summary>

> At first, Emperor X is only a young general.  
> After many victories for France, he takes power in a coup, with little fighting.  
> He sells Louisiana, a huge area in North America, to a young country.  
> A few years after the coup, he makes himself emperor in a great ceremony.  
> In a great church in Paris, the pope stands beside him.  
> But Emperor X takes the crown himself and places it on his own head.  
> Under him, law experts write a new book of laws for the country.  
> It gives all men the same rules, and clear rules for property and family.  
> Women get fewer rights than men.  
> Many countries still use ideas from this book today.  
> His armies fight many wars across Europe.  
> Soon he rules over much of the continent, directly or through his family.  
> **Who is Emperor X?**

**Svar:** ✅ Napoleon Bonaparte · ⬜ Louis XIV · ⬜ Charlemagne · ⬜ George Washington

**Ord:** *coup* — a sudden takeover of power, often fast and by surprise · *ceremony* — a special formal event that marks an important moment · *emperor* — a ruler above kings, who rules a very large land or many lands · *property* — things or land that belong to a person by law

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The Long Road Back from Russia</summary>

> In 1812, Emperor X marches into Russia with about six hundred thousand soldiers.  
> On the long march, sickness, hunger, and battle cost him most of his men.  
> When he reaches the great city, it is empty, and soon much of it burns.  
> Then winter comes, and the Russian army attacks his retreat.  
> Soldiers die by the thousands from cold, hunger, and fighting.  
> Most of his huge army never comes home.  
> Other countries then unite against him, and two years later he gives up his throne.  
> His enemies send him to a small island called Elba.  
> Within a year, he escapes, and rules again for a hundred days.  
> His last battle ends in defeat near a village called Waterloo.  
> This time, his enemies send him to a lonely island far out at sea.  
> He dies there about six years later.  
> **Who is Emperor X?**

**Svar:** ✅ Napoleon Bonaparte · ⬜ Julius Caesar · ⬜ Alexander the Great · ⬜ The Duke of Wellington

**Ord:** *retreat* — when an army stops fighting and moves back · *throne* — the special seat and power of a king or emperor · *defeat* — when you lose a battle or a fight · *unite* — to join together for one purpose

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The Other Side of the Story</summary>

> Mr X leads a French army into Egypt, with scientists and artists too.  
> By the river Nile, his soldiers rebuild an old fort.  
> In one wall, they find a dark grey stone with three kinds of writing.  
> This stone later helps experts read ancient Egyptian writing.  
> Some years before this, France ends slavery in its colonies.  
> Mr X brings slavery back to the French colonies.  
> On one island, people freed from slavery fight to stay free.  
> They defeat his army there, and their colony becomes independent.  
> Many call it the first free nation of formerly enslaved people.  
> Old cartoons and enemy jokes show Mr X as a very short man.  
> Historians check the records: he is about one meter sixty-eight, a normal height for his time.  
> So the story of the short leader is a myth, not a fact.  
> **Who is Mr X?**

**Svar:** ✅ Napoleon Bonaparte · ⬜ Simón Bolívar · ⬜ Louis XIV · ⬜ Charlemagne

**Ord:** *colonies* — lands ruled and controlled by another, faraway country · *enslaved* — forced by others to work, with no freedom and no pay · *independent* — free to rule itself, not controlled by another country · *myth* — a story many people believe, but it is not true

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Hero of the Revolution or Its Gravedigger</summary>

> Historians still argue about Emperor X.  
> Some call him the heir of the revolution, who saves its best ideas.  
> Others call him its gravedigger, who buries freedom under his own crown.  
> As ruler, he controls most newspapers in the country.  
> He also pays painters to make heroic pictures of himself in battle.  
> These pictures shape how people see him for generations.  
> On his last island, he has many empty years.  
> He dictates his own life story to loyal followers there.  
> In his story, he is always wise, and his mistakes are small.  
> Historians read these memoirs with great care.  
> They compare his words with letters, orders, and reports from his own time.  
> The true picture of Emperor X lies somewhere between the myth and the man.  
> **Who is Emperor X?**

**Svar:** ✅ Napoleon Bonaparte · ⬜ Otto von Bismarck · ⬜ Julius Caesar · ⬜ Simón Bolívar

**Ord:** *heir* — a person who continues someone else's work or place · *memoirs* — a book where a person writes the story of their own life · *loyal* — always faithful and supportive, especially to a leader · *generations* — large groups of people born and living around the same time

</details>

### Adolf Hitler

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Country Loses Its Freedom</summary>

> Mr X lives in Germany, about ninety years ago.  
> His country holds free elections and has free newspapers.  
> Hard times come, and millions of people lose their jobs.  
> Mr X leads a party with an angry, simple promise.  
> He blames Jewish people and other groups for the hard times.  
> He promises to make the country strong and proud again.  
> In 1933, the old president names him head of government.  
> Within months, the government shuts down free newspapers.  
> It bans every other political party.  
> People go to prison simply for their opinions.  
> In school, children now learn to hate these groups.  
> **Who is Mr X?**

**Svar:** ⬜ Joseph Stalin · ✅ Adolf Hitler · ⬜ Benito Mussolini · ⬜ Francisco Franco

**Ord:** *elections* — when people vote to choose their leaders · *president* — the highest elected leader of a country · *bans* — makes something against the law · *opinions* — what a person thinks or believes

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The Failed Painter Who Wants Power</summary>

> Mr X wants to become a painter as a young man.  
> He moves to Vienna and tries to enter the art academy.  
> The academy rejects him, not once but twice.  
> He lives alone in a cheap shelter for poor men.  
> When the great war of 1914 begins, he becomes a soldier.  
> He is wounded, and near the end of the war he is gassed.  
> After the war, he joins a small party blaming Jews and democracy for the defeat.  
> In Munich, he tries to seize power by force.  
> The attempt fails, and he goes to prison.  
> In prison, he writes a book full of hate.  
> In one election, his party wins fewer than three votes in every hundred.  
> After a great economic crisis, one voter in three chooses his party, never a majority.  
> **Who is Mr X?**

**Svar:** ⬜ Kaiser Wilhelm II · ⬜ Paul von Hindenburg · ✅ Adolf Hitler · ⬜ Benito Mussolini

**Ord:** *academy* — a school for special skills, like art or science · *gassed* — poisoned by a dangerous gas, used as a weapon in the war · *seize* — to take something suddenly and by force · *economic crisis* — a time when many businesses fail and people lose work and money

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Windows Break Across a Country</summary>

> Mr X leads the government of Germany.  
> His government targets one group above all: Jewish citizens.  
> In his first year in power, his supporters block the doors of Jewish shops.  
> Two years later, new laws take away their rights as citizens.  
> The same laws forbid marriage between Jews and other Germans.  
> In November 1938, his party sends its men to attack Jewish homes, shops, and synagogues.  
> Crowds join in, and windows break across the country in one night.  
> About thirty thousand Jewish men are sent to camps.  
> Jewish families now try to leave the country.  
> Many countries let in only a few of them.  
> Then war comes, and the persecution turns into mass murder.  
> His state murders six million Jews, and also Roma people, disabled people, and others.  
> **Who is Mr X?**

**Svar:** ⬜ Joseph Stalin · ⬜ Hideki Tojo · ✅ Adolf Hitler · ⬜ Francisco Franco

**Ord:** *citizens* — people who legally belong to a country and share its rights · *synagogues* — buildings where Jewish people gather to pray · *camps* — here: guarded places where prisoners are kept against their will · *persecution* — cruel and unfair treatment of a group, again and again

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — One Voice in the Kitchen</summary>

> Mr X's government in Germany controls what people hear and see.  
> A radio stands in most homes, and one voice fills it.  
> Huge rallies gather crowds under bright lights and loud music.  
> One group of students burns books that the government calls dangerous.  
> Children must join youth groups run by the state.  
> A secret police force listens for any word against the government.  
> Neighbors grow afraid to trust each other.  
> Most people simply join in, or quietly look away.  
> A different group of students resists: in Munich, they print leaflets against the government.  
> In February 1943, the government executes three of them for their leaflets.  
> Fear alone cannot explain it all: many ordinary people choose to believe.  
> **Who is Mr X?**

**Svar:** ⬜ Benito Mussolini · ✅ Adolf Hitler · ⬜ Joseph Stalin · ⬜ Hideki Tojo

**Ord:** *rallies* — big public meetings to cheer for a leader or a cause · *youth groups* — clubs where children and teenagers meet, often run by the state · *secret police* — police who spy on citizens in secret, not openly · *leaflets* — small printed sheets of paper with a message

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Not One Man, But a Whole Machine</summary>

> Historians no longer explain Mr X as one evil genius acting alone.  
> They ask a harder question: how does a whole society follow him?  
> One group of historians stresses his own choices and intentions.  
> Another group stresses the structures around him: rivals, chaos, and weak institutions.  
> A famous phrase describes officials who guess his wishes and act without orders.  
> One historian calls this: working towards the leader.  
> The sources include party files, private diaries, and letters home.  
> After the war, trials use these sources to judge the accused.  
> Some people later deny that the murder of six million Jews and others even happened.  
> Historians study this denial too, as a phenomenon in itself.  
> In 1945, with his war lost and Berlin surrounded, Mr X takes his own life.  
> **Who is Mr X?**

**Svar:** ⬜ Francisco Franco · ⬜ Hideki Tojo · ⬜ Joseph Stalin · ✅ Adolf Hitler

**Ord:** *intentions* — the plans or purposes inside a person's mind · *institutions* — the organizations and systems that run a country · *phenomenon* — something that happens and that can be studied and explained · *denial* — refusing to accept that something true really happened

</details>

### Mahatma Gandhi

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Long Walk to the Sea</summary>

> Mr X lives in India, where British rulers are in charge.  
> An old law says only the rulers may make and sell salt.  
> Salt comes free from the sea, but people must pay a tax.  
> Mr X says this law is not fair to poor people.  
> In 1930, he starts to walk from his home toward the coast.  
> Every day along the road, more people join him.  
> The walk takes about twenty-four days in all.  
> He and his followers walk nearly four hundred kilometers.  
> At the seashore, Mr X bends down to the water.  
> He picks up a small handful of natural salt.  
> With this quiet act, he breaks the tax law.  
> Police arrest tens of thousands of his followers, but they do not fight back.  
> **Who is Mr X?**

**Svar:** ⬜ Jawaharlal Nehru · ✅ Mahatma Gandhi · ⬜ Muhammad Ali Jinnah · ⬜ Subhas Chandra Bose

**Ord:** *tax* — money that people must pay to the rulers · *coast* — the land next to the sea · *followers* — people who join and support a leader · *arrest* — when police take a person away and do not let them go free

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A Fight With No Weapons</summary>

> Mr X leads a movement in India, about a hundred years ago.  
> He believes people can fight injustice without any weapons.  
> He calls this method satyagraha, or holding on to truth.  
> Instead of buying British cloth, he asks people to spin their own.  
> He often sits and spins cotton thread on a simple wooden wheel.  
> Homespun cloth becomes a quiet symbol of independence.  
> British rulers repeatedly send Mr X to prison for his protests.  
> In total, he spends about six years of his life in prison.  
> Sometimes he refuses all food as a form of protest.  
> He calls these fasts an appeal to people's conscience.  
> Slowly, a small movement grows into one that includes millions.  
> **Who is Mr X?**

**Svar:** ⬜ Rabindranath Tagore · ⬜ B. R. Ambedkar · ✅ Mahatma Gandhi · ⬜ Muhammad Ali Jinnah

**Ord:** *injustice* — something that is not fair or right · *satyagraha* — a special word for fighting for what is right without violence · *homespun* — cloth spun and woven by hand at home, not made in a factory · *conscience* — the inner feeling that tells a person right from wrong

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Thrown Off the Train</summary>

> Mr X studies law in London, more than a hundred years ago.  
> After his studies, he takes work in South Africa.  
> There, laws treat people differently because of the color of their skin.  
> One night, he sits in a first-class train carriage with a valid ticket.  
> An official orders him off because of his skin color.  
> He refuses to move, and guards throw him off the train.  
> Cold and angry on the empty platform, he decides to act.  
> Over the next twenty-one years, he builds a method of peaceful resistance.  
> He organizes Indians in South Africa to resist unfair laws without violence.  
> Historians note that his early writings there share the prejudice of his time against Africans.  
> Only later does his thinking grow to include all people.  
> **Who is Mr X?**

**Svar:** ⬜ Jawaharlal Nehru · ⬜ Subhas Chandra Bose · ⬜ Rabindranath Tagore · ✅ Mahatma Gandhi

**Ord:** *carriage* — a train car where passengers sit · *official* — a person who works for a government or a company and has some power · *resistance* — fighting against something, here without weapons · *prejudice* — an unfair opinion about people, often based on the group they belong to

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A Country Splits in Two</summary>

> In 1947, Mr X's homeland finally becomes independent.  
> British rulers and Indian leaders also divide the land into two new countries.  
> Millions of Hindus, Muslims, and Sikhs must suddenly move.  
> Violence breaks out between neighbors of different faiths.  
> Estimates say hundreds of thousands of people, maybe far more, are killed.  
> Mr X is heartbroken by violence he has tried to prevent.  
> In the capital, he refuses all food to make the killing stop.  
> His fast works: Hindu and Sikh leaders promise to protect their Muslim neighbors.  
> Not everyone welcomes his message of friendship between faiths.  
> Twelve days later, a Hindu nationalist shoots him dead.  
> The gunman believes Mr X is too friendly toward Muslims.  
> His death shocks the young nation.  
> **Who is Mr X?**

**Svar:** ⬜ B. R. Ambedkar · ⬜ Muhammad Ali Jinnah · ⬜ Jawaharlal Nehru · ✅ Mahatma Gandhi

**Ord:** *independent* — free to rule itself, not controlled by another country · *violence* — actions that hurt or kill people · *estimates* — careful guesses based on the facts we have · *nationalist* — a person with very strong pride in one nation, sometimes against other groups

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Debates That Outlive Him</summary>

> Mr X becomes one of the most studied leaders of the twentieth century.  
> Not everyone in India agrees with his methods or his ideas.  
> B. R. Ambedkar is a leader of the Dalits, the people the caste system places lowest.  
> He says Mr X defends the caste order and does too little against caste discrimination.  
> Ambedkar wants strong legal protection, not only a change of heart.  
> Other leaders find peaceful protest too slow and want an armed uprising instead.  
> Mr X insists that the method matters as much as the goal.  
> Decades later, movements on other continents study his method of nonviolent protest.  
> He writes a long autobiography, openly admitting many of his own mistakes.  
> His collected writings and letters fill about one hundred volumes.  
> Even British police files, kept to watch him, survive as evidence today.  
> Together, these sources let historians question the popular image of the man.  
> **Who is Mr X?**

**Svar:** ⬜ Jawaharlal Nehru · ✅ Mahatma Gandhi · ⬜ Muhammad Ali Jinnah · ⬜ Subhas Chandra Bose

**Ord:** *caste* — a group a person is born into in India's old social order, ranked above or below other groups · *discrimination* — treating a group of people unfairly because of who they are · *autobiography* — a book a person writes about their own life · *volume* — one book in a long series of books that belong together

</details>

### Förenta nationerna

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Talk Instead of Fight</summary>

> The biggest war in history ends in 1945.  
> Many countries want peace to last this time.  
> Fifty countries meet in San Francisco, a city by the sea.  
> There they sign a long agreement together.  
> One more country signs it a little later.  
> Now Organization X starts with fifty-one countries.  
> Today, almost every country in the world belongs to it.  
> Every country sends people to one huge hall.  
> In that hall, each country gets exactly one vote.  
> Organization X also feeds hungry children and sends doctors.  
> **Which organization is Organization X?**

**Svar:** ⬜ The League of Nations · ✅ The United Nations · ⬜ The Commonwealth · ⬜ NATO

**Ord:** *agreement* — a promise that two or more people or countries make together · *peace* — a time with no war or fighting

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — The Rule That Can Stop Everything</summary>

> Organization X works by clear, simple rules.  
> All member countries meet in one big assembly.  
> There, the biggest and the smallest country have one vote each.  
> A smaller council also meets, with fewer countries.  
> Five countries always have a seat on that council.  
> The council can send soldiers to keep the peace.  
> The soldiers wear plain blue helmets for this work.  
> Each of the five can also say no to a plan.  
> This power to block a plan is called a veto.  
> One veto is enough to stop the whole council.  
> So the same five stay strong, but help can be blocked too.  
> **Which organization is Organization X?**

**Svar:** ⬜ The World Bank · ⬜ The Arab League · ✅ The United Nations · ⬜ The European Union

**Ord:** *assembly* — a big meeting where every member has a seat · *council* — a smaller group that meets often and decides on quick action · *veto* — the power to say no and stop a plan, even if everyone else says yes · *helmet* — a hard hat that protects the head

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A List for Every Human</summary>

> In 1948, Organization X writes a new kind of list.  
> The list names rights that every human should have.  
> People from many cultures help write thirty short articles.  
> A woman leads the committee that writes the text.  
> A philosopher from China also shapes the final words.  
> Long debates happen about rights that fit every culture.  
> When the vote comes, no country votes against the list.  
> A few countries choose not to vote for or against.  
> Translators later put the text into hundreds of languages.  
> Still, the list is only words on paper.  
> The gap between the words and daily life stays wide.  
> **Which organization is Organization X?**

**Svar:** ⬜ The League of Nations · ⬜ The Red Cross · ⬜ The European Union · ✅ The United Nations

**Ord:** *committee* — a small group of people chosen to do one job · *philosopher* — a person who thinks deeply about big questions like right and wrong · *articles* — short, numbered parts of a longer written text

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — New Members, Hard Failures</summary>

> About eighty years ago, empires still rule most of Africa and much of Asia.  
> Over the next decades, dozens of new countries join Organization X.  
> Each new member brings its own voice to the big assembly.  
> Organization X openly supports countries that want independence.  
> Later, it bans arms sales to the apartheid state in South Africa.  
> It also calls on countries to stop trading with that state.  
> But Organization X also fails badly at times.  
> In 1994, in Rwanda, its soldiers are ordered to stand back.  
> About eight hundred thousand people are killed there in only a few months.  
> The next year, in Srebrenica, its soldiers cannot protect a town that trusts them.  
> About eight thousand men and boys are killed after the town falls.  
> Both failures are studied closely so such harm does not happen again.  
> **Which organization is Organization X?**

**Svar:** ✅ The United Nations · ⬜ The Organization of African Unity · ⬜ The Commonwealth · ⬜ The World Bank

**Ord:** *empires* — large groups of lands and peoples ruled by one strong power · *independence* — being free to rule yourself, without another country in charge · *apartheid* — a system of laws in South Africa that kept people apart by skin color and gave white people the power

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Question Archives Cannot Answer</summary>

> Historians study Organization X like any other institution.  
> After an earlier great war, countries make a first attempt at world peace.  
> That first attempt is too weak, and it collapses within twenty years.  
> Its failure shapes the design of the second attempt in 1945.  
> Five countries keep a veto from the very first drafts.  
> For decades, diplomats argue about who deserves a permanent seat too.  
> Historians disagree about how to measure the organization's success.  
> Some count wars it stops, others count wars it fails to stop.  
> Old archives and internal memos help settle some of these arguments.  
> But the records cannot answer the hardest question of all.  
> Can states protect people from their own governments?  
> That question stays open.  
> **Which organization is Organization X?**

**Svar:** ⬜ The League of Nations · ⬜ NATO · ✅ The United Nations · ⬜ The Red Cross

**Ord:** *institution* — a large, lasting organization with clear rules · *archives* — old papers and records kept safe for later study · *diplomats* — people who represent their country and talk with other countries

</details>

### Första världskriget

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Two rows of dominoes</summary>

> War X starts more than a hundred years ago, in Europe.  
> Many countries have signed alliances before the war starts.  
> These alliances work like two rows of dominoes.  
> If one country falls into war, its allies often follow.  
> In the summer of 1914, a prince is shot and killed.  
> It happens in a city named Sarajevo, in the Balkans.  
> Historians call this shot the spark, not the cause.  
> Alliances turn one shot into a war across a continent.  
> Many young men, not all, march off cheering.  
> Many believe they will be home again by Christmas.  
> Instead, War X lasts four long years.  
> **Which war is War X?**

**Svar:** ⬜ The Balkan Wars · ✅ World War I · ⬜ World War II · ⬜ The Russian Civil War

**Ord:** *alliance* — a promise between countries to help each other in war · *spark* — a small thing that starts something much bigger · *continent* — a very large area of land, like Europe or Africa · *dominoes* — small flat game pieces, when one falls, it knocks over the next

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A line that does not move</summary>

> War X is fought mostly in the fields of Europe.  
> Soldiers on each side dig long trenches in the earth.  
> These trenches stretch across the land for hundreds of kilometers.  
> Between the two lines lies open ground called no man's land.  
> Machine guns can fire hundreds of bullets every minute.  
> Both sides also use poison gases that burn the eyes and lungs.  
> For years, the front line barely moves at all.  
> Soldiers spend long weeks in mud, cold, and fear.  
> They write letters home to wives, mothers, and children.  
> Lice and rats share the trenches with the soldiers.  
> By the end, about ten million soldiers have died.  
> **Which war is War X?**

**Svar:** ⬜ The Vietnam War · ⬜ The Korean War · ✅ World War I · ⬜ The Spanish Civil War

**Ord:** *trench* — a long, deep ditch dug in the ground · *no man's land* — the open, dangerous ground between two enemy lines · *lice* — tiny bugs that live in hair or clothes and bite

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Soldiers from every continent</summary>

> War X is fought by soldiers from every continent.  
> It begins in 1914 and lasts four years.  
> European countries call on soldiers from their colonies too.  
> Soldiers from India fight in the trenches of France and on other fronts.  
> Men from Senegal cross the sea to fight in France.  
> Australians, Canadians, and soldiers from the Caribbean join as well.  
> The Ottoman Empire, ruling much of the Middle East, fights too.  
> It loses the war, and the empire falls apart.  
> New borders are then drawn across the Middle East.  
> Some of these borders still shape the region today.  
> At home, many men leave their jobs to fight.  
> Women take their place in factories that make weapons and tools.  
> **Which war is War X?**

**Svar:** ⬜ World War II · ⬜ The Korean War · ⬜ The Balkan Wars · ✅ World War I

**Ord:** *colonies* — lands ruled by a country far away · *empire* — many lands and peoples ruled by one strong state · *front* — here: a line where two armies fight each other

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The eleventh hour</summary>

> In 1917, War X has already lasted for years.  
> The United States joins the war and sends soldiers across the ocean.  
> That same year, a revolution shakes the empire of Russia.  
> Its new leaders soon pull the country out of the war.  
> Fighting on the other fronts continues for one more year.  
> At last, an armistice stops the fighting.  
> It is eleven o'clock on the eleventh day of the eleventh month.  
> Crowds in many cities cheer, cry, and hug strangers.  
> The next year, leaders sign a peace treaty at the palace of Versailles.  
> It says one country caused the war and must pay for the damage.  
> Around the same time, a new sickness spreads across the world.  
> In two more years, it kills even more people than the war.  
> **Which war is War X?**

**Svar:** ⬜ The Russian Civil War · ✅ World War I · ⬜ The Spanish Civil War · ⬜ World War II

**Ord:** *armistice* — an agreement between enemies to stop fighting · *revolution* — a sudden, big change in who rules a country · *treaty* — a written agreement between countries

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Whose fault, and how do we know</summary>

> Historians agree on the main events of War X.  
> It begins in Europe in 1914, more than a hundred years ago.  
> But historians still argue about its deeper cause.  
> One group of historians blames the ambition of one country in particular.  
> Another group says the leaders of Europe drift into war like sleepwalkers.  
> On this view, no leader wants the huge war that follows.  
> The sources from the time are hard to use.  
> Soldiers write letters home, but a censor removes some lines.  
> A diary gives private views, yet not many soldiers keep one.  
> After the war, each government writes its own official history.  
> Even the number of soldiers who die is still debated today.  
> Historians keep comparing new sources to test old answers.  
> **Which war is War X?**

**Svar:** ⬜ The Balkan Wars · ⬜ The Vietnam War · ✅ World War I · ⬜ The Korean War

**Ord:** *censor* — a person who reads letters and removes parts before they are sent · *diary* — a book where a person writes each day about life · *ambition* — a strong wish to gain power or success

</details>

### Andra världskriget

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A small suitcase and a new home</summary>

> War X begins in 1939.  
> It grows bigger than any war before it.  
> Armies fight on land, at sea, and in the air.  
> Soldiers fight on three continents and across the oceans.  
> In some countries, governments evacuate many children from the big cities.  
> Each child carries a small suitcase and a name tag.  
> Trains carry them to new families in the countryside.  
> Back home, food grows scarce, so families use ration books.  
> A ration book says how much sugar or meat you may buy.  
> Thick, dark curtains cover every window at night.  
> No light may show outside, or planes might see the town.  
> At school, children practice putting on gas masks.  
> **Which war is War X?**

**Svar:** ⬜ The Korean War · ✅ World War II · ⬜ The Chinese Civil War · ⬜ The Spanish Civil War

**Ord:** *evacuate* — to send people away from a dangerous place to somewhere safer · *ration book* — a small book that says how much food a family may buy · *scarce* — hard to find, because there is not much of it · *gas mask* — a mask that covers your face and helps you breathe clean air

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — One war, many fronts</summary>

> War X does not begin only in Europe.  
> In Asia, Japan already fights a long war in China.  
> In Europe, a dictator's armies conquer most of the continent in two years.  
> Then his armies invade the Soviet Union, a huge country to the east.  
> Soon after, Japan attacks an American naval base in the Pacific.  
> The United States joins the war.  
> Now fighting truly covers most of the world.  
> Deep inside the Soviet Union, one long battle becomes a turning point.  
> In the Pacific, a great sea battle turns the tide too.  
> Soldiers from many countries land on the beaches of northern France.  
> Steadily, armies push the dictator's forces back toward Germany.  
> After almost six years of war, Germany surrenders in 1945.  
> **Which war is War X?**

**Svar:** ⬜ World War I · ⬜ The Vietnam War · ✅ World War II · ⬜ The Gulf War

**Ord:** *invade* — to enter another country with an army in order to take control of it · *continent* — one of the world's very large areas of land, such as Europe or Asia · *turning point* — the moment when something starts to change in a big way · *tide* — here: the direction that a war is going, toward one side winning

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Six million, and how we know</summary>

> In Germany, more than eighty years ago, a dictator takes power.  
> His government spreads hatred and blames Jewish people for the country's problems.  
> Step by step, new laws take away their rights and their safety.  
> During the war, the dictator's state turns this hatred into organized mass murder.  
> In occupied lands, it forces Jewish families into sealed districts called ghettos.  
> In the east, its police and special units shoot huge numbers of Jewish civilians.  
> The regime also builds camps whose only purpose is killing people.  
> Roma people are murdered there too, and so are other groups.  
> Disabled people are murdered in special killing centers in Germany.  
> In total, about six million Jewish people are murdered in this genocide.  
> Not everyone looks away. Some neighbors hide families at great risk.  
> After the war, survivors tell their stories, so today we know what happened.  
> **Which war is War X?**

**Svar:** ✅ World War II · ⬜ The Chinese Civil War · ⬜ World War I · ⬜ The Gulf War

**Ord:** *ghetto* — a closed off part of a city where a group of people is forced to live · *genocide* — the planned murder of a whole group of people because of who they are · *regime* — a government, especially one with great and often harsh power · *survivor* — a person who lives through something very dangerous

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Soldiers, workers, and bombs across the world</summary>

> War X reaches almost every part of the world, not only Europe.  
> Millions of soldiers from Africa and India fight for the empires ruling them.  
> Soldiers and workers from the Caribbean and Latin America join too.  
> At home, women take new jobs building weapons and bombers.  
> Bombers attack cities on every side, and many civilians die.  
> In August 1945, two powerful new bombs destroy two cities in Japan.  
> By the end of that year, about two hundred thousand people are dead.  
> Days later, Japan surrenders, and the fighting finally stops everywhere.  
> In total, historians count more than sixty million dead.  
> Most of them are not soldiers, but ordinary civilians.  
> **Which war is War X?**

**Svar:** ⬜ The Vietnam War · ⬜ The Korean War · ⬜ The Spanish Civil War · ✅ World War II

**Ord:** *empire* — a large group of countries or peoples ruled by one powerful country · *surrender* — to stop fighting and admit defeat · *bomber* — a plane built to carry and drop bombs · *civilian* — a person who is not a soldier

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Counting the dead, keeping the memory</summary>

> Historians still argue about the exact number of dead in War X.  
> Estimates range from about fifty million to about eighty million people.  
> In some countries, records are incomplete, lost, or never kept.  
> After the war, courts in Nuremberg and Tokyo try the former leaders.  
> Judges from the winning countries hear evidence of war crimes and mass murder.  
> Historians also debate the two atomic bombs dropped on Japan.  
> Some argue the bombs saved lives by ending the war quickly.  
> Others argue that the war was already close to its end.  
> They add that the Soviet attack on Japan mattered too.  
> Museums, memorials, and survivor testimony keep the memory of the war alive.  
> A few people falsely deny the genocide of six million Jewish people.  
> Historians answer with documents, photographs, and the words of survivors.  
> **Which war is War X?**

**Svar:** ⬜ World War I · ✅ World War II · ⬜ The Chinese Civil War · ⬜ The Vietnam War

**Ord:** *estimate* — a careful guess based on the information you have · *testimony* — what a witness says about what happened · *deny* — to say that something is not true, even when it is · *memorial* — a place built to help people remember something important

</details>

### Winston Churchill

<details>
<summary><b>Kort 1 · Årskurs 6</b> — An Escape Among Coal Sacks</summary>

> As a boy, Mr X does badly in Latin and mathematics.  
> He loves toy soldiers more than lessons.  
> More than a hundred years ago, he becomes a young army officer.  
> He fights for his country's army in Sudan and writes for newspapers.  
> Later, he travels with soldiers in South Africa, as a reporter.  
> Boer fighters capture him and lock him in a prison camp.  
> One night, Mr X climbs over the camp wall.  
> He hides among coal sacks on a goods train.  
> Then helpers hide him in a mine and on another train.  
> After a long, dangerous journey, he reaches safety.  
> Newspapers print his escape story, and he becomes famous.  
> Years later, he leads his country's government in the war against Germany's dictator.  
> **Who is Mr X?**

**Svar:** ⬜ David Lloyd George · ✅ Winston Churchill · ⬜ Neville Chamberlain · ⬜ Harold Macmillan

**Ord:** *reporter* — a person whose job is to write news for a newspaper · *prison camp* — a guarded place where captured soldiers are kept · *toy soldiers* — small model soldiers that children play with · *Boer* — a farmer of Dutch family background in South Africa, more than a hundred years ago

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Only Blood, Toil, Tears, and Sweat</summary>

> In 1940, Mr X becomes the leader of his country's government.  
> It stands almost alone in the war against the dictator in Germany.  
> In parliament he promises only blood, toil, tears, and sweat.  
> Newspapers print his words, and people repeat them.  
> His words are simple, and many people say they give them courage.  
> Soon, enemy planes bomb the capital city, night after night.  
> Families hide in shelters and underground stations.  
> Fires burn through whole streets by morning.  
> Mr X walks through the ruins the next day.  
> He talks with tired families among the broken houses.  
> His speeches from these months become famous around the world.  
> **Who is Mr X?**

**Svar:** ⬜ Neville Chamberlain · ⬜ Charles de Gaulle · ⬜ Clement Attlee · ✅ Winston Churchill

**Ord:** *toil* — hard, tiring work · *parliament* — the group of elected people who make a country's laws · *shelter* — a safe place that protects people from danger · *ruins* — what is left after buildings are destroyed

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Blame, Warnings, and a Lost Election</summary>

> In 1915, Mr X pushes hard for a bold naval attack.  
> The target is a narrow sea strait, far from the main front.  
> The plan fails badly.  
> More than one hundred thousand soldiers die on both sides.  
> Mr X takes much of the blame, and he loses his government job.  
> He returns within two years and holds high office in the 1920s.  
> Then come ten years without office, which biographers later call his wilderness years.  
> In these years, he warns that a dictator in Germany grows more dangerous.  
> Few politicians want to listen to his warnings.  
> Later, he leads his country through the war in Europe.  
> Weeks after victory, his country holds an election.  
> Voters choose another party, which promises new housing, health care, and jobs.  
> **Who is Mr X?**

**Svar:** ✅ Winston Churchill · ⬜ David Lloyd George · ⬜ Neville Chamberlain · ⬜ Clement Attlee

**Ord:** *strait* — a narrow strip of sea between two areas of land · *wilderness years* — a long period out of power and influence · *blame* — responsibility for something bad that happens

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Empire, India, and a Famine in Bengal</summary>

> Mr X leads his country's government in the war against Germany's dictator.  
> He believes strongly that his country's empire is a good thing.  
> He says harsh words about Indian people and their wish for independence.  
> In 1943, famine strikes the region of Bengal, in India.  
> A cyclone and floods ruin the rice harvest, and crop disease spreads.  
> The war cuts off rice from Burma, and ships carry weapons, not grain.  
> Officials in India beg his government for more help.  
> His government refuses to send enough food ships.  
> About three million people die from hunger and disease.  
> Historians still argue about how much blame belongs to Mr X.  
> Some point to wartime shipping shortages everywhere.  
> Others point to his own words and choices about India.  
> **Who is Mr X?**

**Svar:** ⬜ Clement Attlee · ⬜ Harold Macmillan · ✅ Winston Churchill · ⬜ David Lloyd George

**Ord:** *famine* — a time when many people cannot get enough food · *cyclone* — a huge storm with very strong winds that comes in from the sea · *harvest* — the crops gathered from fields at the end of the growing season · *shortage* — not having enough of something that is needed

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Man Who Writes His Own History</summary>

> After the war in Europe, Mr X writes his own history of it.  
> A team of helpers works with him.  
> His account fills six thick volumes.  
> The books shape how people remember the war for decades.  
> In 1953, he receives the Nobel Prize in Literature.  
> The prize honors his speeches and his historical writing, not his politics.  
> Away from politics, Mr X often paints quiet landscapes.  
> He calls painting his way to escape dark moods.  
> Historians later study his private papers, letters, and cabinet documents.  
> These sources sometimes support his own account, and sometimes contradict it.  
> Slowly, historians separate his own myth from the documented record.  
> His own story remains powerful, but it is now read with care.  
> **Who is Mr X?**

**Svar:** ⬜ Charles de Gaulle · ✅ Winston Churchill · ⬜ Joseph Stalin · ⬜ Franklin Roosevelt

**Ord:** *volume* — one book in a set of books that belong together · *account* — here: a person's own telling of what happened · *cabinet* — the group of top ministers who advise a country's leader · *myth* — a popular story that is not fully true

</details>

### Berlinmurens fall

<details>
<summary><b>Kort 1 · Årskurs 6</b> — One evening in November</summary>

> A big city named Berlin stands cut in two by a wall.  
> The wall stands there for twenty-eight years.  
> Families on one side cannot visit the other side.  
> Guards watch the wall every day and every night.  
> Then, one evening in November 1989, everything suddenly changes.  
> Guards at the checkpoints let people through the gates.  
> Thousands of people walk across to the other side.  
> Strangers on both sides hug each other and cry.  
> Some climb up onto the wall itself that night.  
> They swing hammers and chip small pieces off it.  
> That November night is Event X.  
> **Which event is Event X?**

**Svar:** ✅ The fall of the Berlin Wall · ⬜ The Cuban Missile Crisis · ⬜ The Hungarian uprising of 1956 · ⬜ The collapse of the Soviet Union

**Ord:** *checkpoints* — places where guards check who may pass · *chip* — to break a small piece off something hard · *strangers* — people you do not know

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A city cut in two</summary>

> After the biggest war in history, a city lies in ruins.  
> The winners of the war divide the city into four parts.  
> One part belongs to a state with closed borders.  
> In that state, people cannot travel freely to other countries.  
> Every year, hundreds of thousands leave through the open city border.  
> So in August 1961, the state acts in one night.  
> Soldiers roll out barbed wire across the city.  
> In the days after, workers add a long concrete wall.  
> Soldiers with dogs and searchlights guard the new border.  
> At least one hundred and forty people die at the wall.  
> About a hundred of them die trying to cross it.  
> Event X comes many years later, the night the wall opens.  
> **Which event is Event X?**

**Svar:** ⬜ The Prague Spring · ✅ The fall of the Berlin Wall · ⬜ The Solidarity strikes in Poland · ⬜ The end of apartheid

**Ord:** *concrete* — a hard grey material made from sand, stone and cement · *searchlights* — strong lights used to light up a dark area · *border* — the line where one country or area ends and another begins

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A spokesman reads it wrong</summary>

> By the autumn of 1989, the wall has stood for years.  
> The leader of the eastern giant now allows reforms.  
> That September, Hungary announces on television that its western border is open.  
> Tens of thousands from behind the wall escape through that gap.  
> Every Monday, crowds in Leipzig grow into hundreds of thousands.  
> They chant one simple phrase, "We are the people."  
> Under this pressure, the old leader of the state is pushed out.  
> One evening, a party spokesman holds a press conference on live television.  
> At the press table, he reads a new travel rule badly.  
> A reporter asks when it starts, and he answers, "immediately".  
> Crowds rush to the checkpoints that same night.  
> Confused guards finally lift the barrier, and Event X begins.  
> **Which event is Event X?**

**Svar:** ⬜ The Hungarian uprising of 1956 · ⬜ The collapse of the Soviet Union · ⬜ The Solidarity strikes in Poland · ✅ The fall of the Berlin Wall

**Ord:** *reforms* — changes made to improve how a country is run · *chant* — to say or shout the same words together, again and again · *spokesman* — a person who speaks to the public for a government or a group · *barrier* — something that blocks the way, like a gate or a fence

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — The night the gates open</summary>

> Event X is the night when the wall opens.  
> After that night, huge changes follow very fast.  
> In the autumn of 1989, change sweeps across the whole region.  
> One by one, other closed states loosen their grip on power.  
> In most places, the change happens peacefully.  
> In Romania, though, the change turns violent.  
> Less than a year later, the divided country becomes one again.  
> Reunion brings joy, yet it also brings hard change in the east.  
> Many old factories close, and workers there suddenly lose their jobs.  
> For years, the secret police have watched millions of ordinary citizens.  
> Two years after Event X, people can read their own secret files.  
> Some are shocked to learn who reported on them, even neighbors.  
> **Which event is Event X?**

**Svar:** ⬜ The Cuban Missile Crisis · ✅ The fall of the Berlin Wall · ⬜ The Prague Spring · ⬜ The end of apartheid

**Ord:** *secret police* — police who work in secret to watch and control people · *reunion* — coming back together after being apart · *violent* — involving force that hurts people or damages things

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Planned, or by mistake</summary>

> Event X is the night the wall opens in 1989.  
> Historians still debate why it happens.  
> Some stress the reformer in the eastern giant who allows change.  
> Others point to the huge crowds who force the pace of events.  
> Others again stress the churches that shelter the first protest meetings.  
> Still others point to one spokesman's mistake at the press conference.  
> Some also point to western television, which reports the gates are open.  
> No single cause fully explains what happens that night.  
> To study it, historians use grainy television footage from the time.  
> They also read files kept by the old secret police.  
> Interviews with people who were there add memory to the record.  
> Yet memory itself differs, and east and west recall that night differently.  
> **Which event is Event X?**

**Svar:** ⬜ The Hungarian uprising of 1956 · ⬜ The Cuban Missile Crisis · ✅ The fall of the Berlin Wall · ⬜ The Solidarity strikes in Poland

**Ord:** *debate* — to discuss a question on which people disagree · *reformer* — a person who works to change and improve a system · *footage* — recorded pictures from a film or video camera

</details>

### Den första månlandningen

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Rocket Taller Than a Building</summary>

> Event X happens in July 1969, more than fifty years ago.  
> Three men sit inside a tiny capsule.  
> A giant rocket lifts the capsule into the sky.  
> The rocket stands taller than a building with thirty floors.  
> The three men travel through space for four days.  
> They aim for the Moon, high above the Earth.  
> Two men climb down a ladder onto grey dust.  
> The dust keeps their footprints, because there is no wind.  
> Back home, about 600 million people watch on television.  
> The two men gather grey stones and carry them home.  
> **Which event is Event X?**

**Svar:** ⬜ The first flight across the Atlantic · ⬜ The first spacewalk · ✅ The first Moon landing · ⬜ The first space station

**Ord:** *capsule* — a small closed vehicle that carries people through space · *rocket* — a tall machine that burns fuel to fly into space · *footprints* — marks left in the ground by feet

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A President Promises the Moon</summary>

> Two great powers compete for years.  
> One of them sends the first satellite into space.  
> That happens in 1957, and it shocks the other side.  
> Some years later, that power also sends the first human into space.  
> His name is Yuri Gagarin, and he circles the Earth once.  
> Soon after, a president speaks to his country's lawmakers.  
> He promises to reach the Moon before the decade ends.  
> About 400,000 people join the huge program that follows.  
> Many are engineers, and some are mathematicians.  
> One mathematician, Katherine Johnson, checks flight paths by hand.  
> During a test on the ground, a sudden fire kills three astronauts.  
> Even so, the program moves forward, and Event X still lies ahead.  
> **Which event is Event X?**

**Svar:** ✅ The first Moon landing · ⬜ The first spacewalk · ⬜ The first woman in space · ⬜ The first flight across the Atlantic

**Ord:** *satellite* — an object that circles a planet or a moon in space · *engineers* — people who design and build machines · *mathematician* — a person who works with numbers and shapes · *decade* — a period of ten years

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Seconds of Fuel Left</summary>

> Event X almost fails before it truly begins.  
> During the final approach, an onboard computer overloads with alarms.  
> The commander looks out and sees large rocks ahead.  
> He takes control and steers past the rocks by hand.  
> Only seconds of fuel remain when he sets the small craft down.  
> Hours later, he climbs down onto the dust.  
> He calls it "one small step for man, one giant leap for mankind."  
> A second man joins him for about two and a half hours.  
> A third man waits alone in the main ship, circling above.  
> Each time he passes behind the Moon, its body blocks radio contact.  
> Later, all three men fly home in the main ship.  
> It falls through hot flames and splashes down in the ocean.  
> **Which event is Event X?**

**Svar:** ⬜ The first spacewalk · ⬜ The first human in space · ✅ The first Moon landing · ⬜ The first space station

**Ord:** *overloads* — takes in more signals or work than it can handle · *commander* — the person in charge of a crew · *radio contact* — a spoken link between two places, sent through the air · *splashes down* — comes down and hits water at the end of a flight

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A Rat Bites His Sister</summary>

> Event X is the high point of a huge program.  
> The whole program costs about 25 billion dollars.  
> That is in the money of that time.  
> Critics say the money could instead fight poverty at home.  
> At the same time, the country fights a costly war in Asia.  
> One poet writes a bitter poem about the huge cost.  
> In it, a rat bites his sister while a man walks on the Moon.  
> Not everyone at home shares the pride many feel that summer.  
> Even so, five more crews step onto the surface after this one.  
> Three later crews even drive a small open car on the surface.  
> Then the program ends after only a few years.  
> No astronaut has walked on the Moon since 1972.  
> **Which event is Event X?**

**Svar:** ⬜ The first satellite in orbit · ✅ The first Moon landing · ⬜ The first expedition to the South Pole · ⬜ The first woman in space

**Ord:** *critics* — people who say something is wrong or has faults · *poverty* — the state of being very poor · *poet* — a person who writes poems

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Mirrors on the Moon</summary>

> Scientists still study Event X using hard evidence today.  
> Six crews together bring home 382 kilograms of grey rock.  
> Labs across the world study these stones for new clues.  
> Some equipment left on the surface still works after decades.  
> Small mirrors reflect laser light sent from telescopes on Earth.  
> These signals measure the exact distance between Earth and the Moon.  
> The rival great power also follows each flight closely.  
> Its scientists track the flights and never call them fake.  
> Even so, some people later claim the event never happens at all.  
> Historians study this false claim as a case of modern doubt.  
> Scholars still debate whether the program is mainly science, politics, or show.  
> **Which event is Event X?**

**Svar:** ⬜ The first expedition to the South Pole · ⬜ The first woman in space · ⬜ The first flight across the Atlantic · ✅ The first Moon landing

**Ord:** *kilograms* — a unit used to measure how heavy something is · *laser* — a strong, narrow beam of light · *reflect* — to bounce back, the way light bounces off a mirror · *rival* — a person or group competing against another

</details>

### Kalla kriget

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Two giants that never fight</summary>

> Conflict X starts after the biggest war in history ends in 1945.  
> Two very strong powers come out of that war.  
> One power stands in the west, one power stands in the east.  
> Each side builds bombs strong enough to destroy whole cities.  
> The two powers never openly fight each other.  
> Instead, each side fears the plans of the other.  
> A line of fences and guards cuts Europe in two.  
> People call this line an iron curtain.  
> In some schools, children practice a hiding drill under their desks.  
> They fear a bomb might fall from the sky.  
> This tense rivalry lasts for more than forty years.  
> **Which conflict is Conflict X?**

**Svar:** ⬜ World War II · ✅ The Cold War · ⬜ The Korean War · ⬜ The Vietnam War

**Ord:** *iron curtain* — a name for the guarded line that cuts Europe in two · *guard* — a person whose job is to stop people from crossing a border · *drill* — a practice exercise done again and again to prepare for danger · *rivalry* — a long contest between two sides that both want to be the strongest

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Fighting through other people's wars</summary>

> Conflict X is fought mostly through other countries and other people.  
> The two rival powers rarely send soldiers to fight each other.  
> In the early 1950s, the western power fights in Korea with its own army.  
> The eastern power secretly arms the other side.  
> Later, the western power sends its army into a long war in Vietnam.  
> The eastern power later sends soldiers into a war in Afghanistan.  
> Both powers send weapons and money into a civil war in Angola.  
> They also back rival sides in several wars across Central America.  
> The two powers also race each other into space.  
> A wall cuts one divided city in Europe in two.  
> Millions of soldiers and civilians die in these wars.  
> **Which conflict is Conflict X?**

**Svar:** ⬜ The Gulf War · ⬜ The Yugoslav Wars · ✅ The Cold War · ⬜ The Spanish Civil War

**Ord:** *rival* — a country or person competing strongly against another · *civil war* — a war fought between groups inside one country · *civilian* — a person who is not a soldier

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Thirteen days that shake the world</summary>

> In October 1962, Conflict X reaches its most dangerous moment.  
> Spy planes find missiles hidden on an island near the United States.  
> These missiles could reach many cities within minutes.  
> For thirteen tense days, the world fears a nuclear war.  
> The two leaders exchange secret letters late at night.  
> Military officers on both sides prepare for the worst.  
> At last, the two sides agree on a deal, part of it secret.  
> One side promises to remove its missiles from the island.  
> The other side promises not to invade the island.  
> It also secretly agrees to remove missiles near its rival.  
> After the crisis, the two leaders set up a direct line for urgent messages.  
> They hope fast contact can prevent such danger in the future.  
> **Which conflict is Conflict X?**

**Svar:** ⬜ The Vietnam War · ⬜ The Yugoslav Wars · ⬜ The Korean War · ✅ The Cold War

**Ord:** *missile* — a weapon that flies through the air to hit a target far away · *nuclear* — using the huge power inside atoms, strong enough to destroy whole cities · *spy plane* — an aircraft that flies high and takes secret photographs of another country

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A rivalry that reaches every continent</summary>

> Conflict X shapes lives in Asia, Africa and Latin America too.  
> Many countries in Asia and Africa become independent around this time.  
> In 1955, representatives from twenty-nine countries meet in a city named Bandung.  
> Many of them want to stay out of the rivalry between the two powers.  
> Still, the rivalry reaches into their countries in painful ways.  
> In Congo, outside powers help remove the country's first elected leader.  
> Years of crisis and civil conflict follow.  
> In Chile, a coup overthrows an elected leader.  
> One power helps prepare the coup and welcomes it.  
> In Indonesia, political violence kills several hundred thousand people.  
> Dictators in many poorer countries receive support from one side or the other.  
> Ordinary people bear the heaviest cost of this global rivalry.  
> **Which conflict is Conflict X?**

**Svar:** ✅ The Cold War · ⬜ The Yugoslav Wars · ⬜ The Gulf War · ⬜ The Korean War

**Ord:** *representative* — a person sent to speak and act for a country or group · *coup* — a sudden illegal takeover of a government, often by the army · *dictator* — a ruler who holds total power and allows little freedom

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Whose fault, and how does it end</summary>

> Historians disagree about who is most to blame for Conflict X.  
> One early group of historians blames the eastern power's ambitions.  
> A later group of historians blames the western power's actions instead.  
> A third group argues that fear and misunderstanding drive both sides.  
> The rivalry ends gradually between the late 1980s and the early 1990s.  
> The eastern power lets its allies in Europe hold free elections.  
> Soon after, the eastern superpower breaks apart into fifteen separate countries.  
> After 1991, archives in the east open to researchers.  
> The new documents force historians to revise some earlier conclusions.  
> Historians still argue about which explanation fits the evidence best.  
> Each newly opened archive can quietly change the accepted story.  
> **Which conflict is Conflict X?**

**Svar:** ⬜ World War II · ⬜ The Vietnam War · ⬜ The Yugoslav Wars · ✅ The Cold War

**Ord:** *ambition* — a strong wish to gain power, success, or influence · *archive* — a place where old documents and records are kept · *superpower* — an extremely powerful country with influence across the world

</details>

### Martin Luther King

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Year Without the Bus</summary>

> Mr X lives in a city in the southern United States.  
> In 1955, Black passengers must sit at the back of buses.  
> One day, a woman named Rosa Parks refuses to give up her seat.  
> Police arrest her, and Black leaders plan a protest.  
> They choose Mr X, a young pastor of twenty-six, to lead it.  
> For more than a year, Black residents refuse to ride the buses.  
> They walk long distances or share rides in cars instead.  
> The bus company loses money every single day.  
> At last, a court rules that the seating rule is against the law.  
> **Who is Mr X?**

**Svar:** ⬜ Thurgood Marshall · ⬜ Jesse Jackson · ✅ Martin Luther King Jr. · ⬜ John Lewis

**Ord:** *pastor* — a leader of a Christian church · *protest* — a public action that shows something is wrong · *residents* — people who live in a place · *arrest* — when police take a person away and do not let them go free

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Dogs, Hoses, and a Letter from Jail</summary>

> Mr X studies the ideas of a leader in India who fights without weapons.  
> He believes protest should never turn to violence, even when police attack.  
> In the southern United States, activists sit at lunch counters that refuse to serve them.  
> Police arrest Mr X again and again for these peaceful protests.  
> In 1963, police put him in jail in a city called Birmingham.  
> In jail, Mr X writes a long letter.  
> In it, he explains why people must not wait patiently for freedom.  
> A few weeks later, children join a big march in the same city.  
> Police turn dogs and powerful water hoses on the young marchers.  
> Cameras film the attack, and people around the world watch on television.  
> **Who is Mr X?**

**Svar:** ⬜ Thurgood Marshall · ✅ Martin Luther King Jr. · ⬜ Medgar Evers · ⬜ Jesse Jackson

**Ord:** *activists* — people who work hard to bring about change · *lunch counter* — a long table in a shop where people sit to eat a quick meal · *marchers* — people who walk together to show what they believe · *jail* — a place where police keep people who are arrested

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A Dream at the Capital</summary>

> In 1963, Mr X helps lead a huge march in the United States.  
> About two hundred fifty thousand people gather in the capital to listen.  
> He gives a famous speech about his dream for the future.  
> He dreams that people will judge his children by their character, not their skin.  
> The speech becomes one of the most quoted in the country's history.  
> The next year, a new law bans segregation in public places across the country.  
> That same year, Mr X receives a great prize for peace.  
> At thirty-five, he is then the youngest person ever to win it.  
> The year after, another new law protects the right of Black citizens to vote.  
> **Who is Mr X?**

**Svar:** ⬜ John Lewis · ⬜ W. E. B. Du Bois · ⬜ Medgar Evers · ✅ Martin Luther King Jr.

**Ord:** *capital* — the main city of a country, where the government meets · *segregation* — the unfair separation of people because of skin color · *citizens* — people who legally belong to a country · *character* — a person's inner qualities, like honesty and kindness

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — Too Slow for the Young</summary>

> Mr X faces sharp criticism from other Black leaders.  
> A leader named Malcolm X calls his peaceful method too slow.  
> In his last years, many younger activists say the same.  
> They want faster change and are ready to use force if needed.  
> Mr X begins to speak out against the war in Vietnam.  
> The president and many old allies turn against him because of this stand.  
> He starts a new campaign against poverty for poor Americans of every color.  
> In 1968, he travels to Memphis to support sanitation workers who are on strike.  
> There, on a motel balcony, a gunman shoots him dead.  
> His death shocks the nation, and riots break out in many cities.  
> **Who is Mr X?**

**Svar:** ✅ Martin Luther King Jr. · ⬜ John Lewis · ⬜ Thurgood Marshall · ⬜ Jesse Jackson

**Ord:** *criticism* — comments that say what is wrong with something · *campaign* — an organized effort to reach a goal · *poverty* — the state of being very poor · *sanitation* — the systems that keep a place clean, like trash collection

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Man Behind the Myth</summary>

> Historians still debate how much one leader can shape a mass movement.  
> Mr X leads a movement for equal rights in the United States after 1955.  
> Some argue thousands of local organizers do the daily, quiet work.  
> Women such as Ella Baker and Jo Ann Robinson plan and organize for years.  
> Yet public memory often remembers only a handful of famous names.  
> For years, government agents secretly watch Mr X.  
> They record his private conversations and try to damage his reputation.  
> Historians study his sermons, recordings, and court records to understand him.  
> Today, textbooks often remember a calm dreamer of peaceful change.  
> Fewer people remember his later, sharper criticism of poverty and war.  
> Historians argue that both pictures are true, and both are incomplete.  
> **Who is Mr X?**

**Svar:** ⬜ Thurgood Marshall · ⬜ John Lewis · ✅ Martin Luther King Jr. · ⬜ W. E. B. Du Bois

**Ord:** *organizers* — people who plan and arrange the work of a group · *reputation* — what other people think and say about a person · *sermons* — religious speeches given in a church · *incomplete* — not whole, missing some parts

</details>

### Nelson Mandela

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Boy Who Runs to the City</summary>

> Mr X grows up in a small village in South Africa.  
> As a boy, he herds cattle on green hills.  
> On his first day of school, a teacher gives him a new name.  
> Later, his family arranges a marriage for him.  
> Mr X does not want this marriage, so he runs away.  
> He travels far to a big city and begins to study law.  
> New laws now say where people may sit, eat, and travel.  
> These laws depend only on the color of a person's skin.  
> Mr X decides that these laws are not fair.  
> Many years later, he becomes his country's first Black president.  
> **Who is Mr X?**

**Svar:** ⬜ Steve Biko · ✅ Nelson Mandela · ⬜ Desmond Tutu · ⬜ Oliver Tambo

**Ord:** *herd* — to move a group of animals together · *cattle* — cows and bulls kept by farmers · *arrange* — to plan something before it happens · *marriage* — when two people become husband and wife

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Eighteen Years on an Island</summary>

> Mr X works as a lawyer in Johannesburg.  
> In 1964, he stands trial for actions against an unfair government.  
> In court, he speaks of his ideal of a free society.  
> He says he is ready to die for this ideal.  
> The judge sends him to prison for the rest of his life.  
> Guards take him to an island near Cape Town for eighteen years.  
> For thirteen years, he breaks stone in a hot limestone quarry.  
> Dust and sunlight from the quarry harm his eyes.  
> He may write and receive only a few censored letters.  
> Later, guards let him grow a small garden in the yard.  
> In total, Mr X spends twenty-seven years behind bars.  
> Outside, more and more people around the world sing songs about him.  
> **Who is Mr X?**

**Svar:** ⬜ Walter Sisulu · ⬜ Julius Nyerere · ✅ Nelson Mandela · ⬜ F. W. de Klerk

**Ord:** *trial* — when a court decides if a person did something wrong · *quarry* — a place where workers cut or break stone from the ground · *censored* — checked and partly blocked by an authority before it is allowed · *ideal* — an idea of how something should be, at its best

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — From Protest to Sabotage</summary>

> For years, Mr X and his movement in South Africa protest without weapons.  
> In 1960, police open fire on an unarmed crowd, killing sixty-nine people.  
> After this massacre, Mr X changes his mind about peaceful protest alone.  
> He believes peaceful methods now meet only violence in return.  
> With others, he starts a small armed group for sabotage.  
> Later, he explains that it attacks power lines and empty buildings, not people.  
> Police arrest him, and at his trial he defends this choice himself.  
> He calls it a hard decision, taken only when other paths close.  
> While he is in prison, his colleague Oliver Tambo leads the movement from abroad.  
> In the 1980s, parts of the movement also turn to violence against people.  
> In the end, Mr X chooses talks over more fighting.  
> **Who is Mr X?**

**Svar:** ⬜ Desmond Tutu · ⬜ Walter Sisulu · ⬜ Kwame Nkrumah · ✅ Nelson Mandela

**Ord:** *massacre* — the killing of many people who cannot fight back · *unarmed* — carrying no weapons · *sabotage* — damaging machines or buildings on purpose to stop an enemy · *colleague* — a person who works with you for the same cause

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — From a Locked Gate to the Ballot Box</summary>

> In 1990, guards in South Africa finally open the prison gate for Mr X.  
> He walks out hand in hand with his wife.  
> Mr X then holds long talks with the white president, F. W. de Klerk.  
> During these years, political violence in the country kills thousands of people.  
> At last, all sides agree that every adult may now vote.  
> Four years after his release, people of every color vote in a first free election.  
> Many wait for hours in long, patient lines to vote.  
> At seventy-five years old, Mr X becomes the country's new president.  
> Later, a commission lets victims and those who hurt them both speak.  
> Desmond Tutu leads this Truth and Reconciliation Commission.  
> After only one term as president, Mr X steps down from power.  
> **Who is Mr X?**

**Svar:** ✅ Nelson Mandela · ⬜ Walter Sisulu · ⬜ Oliver Tambo · ⬜ Julius Nyerere

**Ord:** *commission* — a group of people given an official job to do · *reconciliation* — becoming friendly again after a conflict · *victims* — people who are hurt or harmed by others · *term* — a fixed length of time in an official job

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Hero, Compromise, or Both?</summary>

> Historians still debate how to judge Mr X, a leader in South Africa.  
> Some call him a hero who ends a brutal system peacefully.  
> Others say he compromises too much, and inequality remains after 1994.  
> The gap between rich and poor in his country stays wide for decades.  
> Historians also ask how much credit belongs to one man alone.  
> A whole movement of thousands works and suffers for the same cause.  
> Mr X writes a long autobiography with help, a rich but personal source.  
> Historians note what the book leaves out, as well as what it tells.  
> Prison guards and officials also keep careful written records of his prison years.  
> These archives let researchers check and sometimes correct his own account.  
> His country once jails him as a terrorist.  
> Later, it calls him a father of the nation.  
> **Who is Mr X?**

**Svar:** ⬜ Steve Biko · ✅ Nelson Mandela · ⬜ Kwame Nkrumah · ⬜ Julius Nyerere

**Ord:** *compromise* — giving up part of what you want, to reach agreement · *inequality* — when wealth or chances are not shared fairly · *autobiography* — a book a person writes about their own life · *archives* — collections of old documents kept for the future

</details>

### Louis Pasteur

<details>
<summary><b>Kort 1 · Årskurs 6</b> — Sour Wine, Gentle Heat, and a Boy Bitten by a Dog</summary>

> Mr X is a scientist who lives in France, about 150 years ago.  
> He studies tiny living things that people cannot see.  
> These tiny living things can make milk and wine turn sour.  
> They can also make cuts and wounds turn bad.  
> Mr X finds a way to heat wine and beer very gently.  
> The gentle heat kills the tiny living things inside.  
> After that, the wine and beer stay good for much longer.  
> Later, other people use his idea for milk.  
> In 1885, a dog with rabies bites a boy named Joseph Meister.  
> Two doctors say the boy will die without help.  
> Mr X makes a new treatment in his laboratory.  
> A doctor gives the boy the treatment while Mr X watches, and the boy lives.  
> **Who is Mr X?**

**Svar:** ⬜ Edward Jenner · ✅ Louis Pasteur · ⬜ Alexander Fleming · ⬜ Ignaz Semmelweis

**Ord:** *sour* — tasting sharp and bad, like old milk · *wound* — a cut or hurt place on the body · *rabies* — a dangerous disease that a sick animal can give with a bite · *laboratory* — a room where a scientist does tests and experiments

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A Bent Glass Neck, Sick Silkworms, and a Field of Sheep</summary>

> Mr X works in a laboratory in France, about 160 years ago.  
> Many people believe that life can appear from nothing inside old soup.  
> Mr X boils broth inside a glass flask with a long, bent neck.  
> Air can enter the flask, but dust and germs cannot pass the bend.  
> The broth stays clear for months, so life does not appear by itself.  
> This experiment shows that germs always come from other germs.  
> Later, Mr X helps save the French silk industry from a silkworm disease.  
> He shows which tiny living things make the silkworms sick.  
> Farmers learn to keep only healthy silkworm eggs.  
> He then makes a vaccine from weakened germs.  
> In 1881, he tests it on sheep in front of a large crowd.  
> The treated sheep stay healthy, and the idea spreads across the world.  
> **Who is Mr X?**

**Svar:** ⬜ Robert Koch · ⬜ Joseph Lister · ✅ Louis Pasteur · ⬜ Charles Darwin

**Ord:** *broth* — a thin, watery liquid made by boiling something, like a simple soup · *silkworm* — a small caterpillar that makes silk thread · *vaccine* — a weak form of a germ given to protect the body against the strong form · *weakened* — made less strong than before

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — An Idea Doctors Do Not Want to Believe</summary>

> In France, about 150 years ago, many doctors do not believe that germs cause disease.  
> Some doctors still think that bad smells and bad air alone make people sick.  
> Mr X strongly disagrees, and he calls this old idea wrong and dangerous.  
> He argues that germs too small to see cause infection in wounds and blood.  
> Many respected doctors mock this idea, and Mr X faces years of criticism.  
> A famous story says that in 1879 an assistant leaves the laboratory to go on holiday.  
> He forgets to inject hens with a fresh culture of chicken cholera germs.  
> When he returns, he uses the old, weak sample instead.  
> The hens get slightly sick but recover, and they survive a later infection too.  
> Mr X understands that a weakened germ can train the body to fight disease.  
> This discovery slowly changes how doctors around the world think about illness.  
> **Who is Mr X?**

**Svar:** ⬜ Joseph Lister · ⬜ Robert Koch · ⬜ Ignaz Semmelweis · ✅ Louis Pasteur

**Ord:** *infection* — illness caused by germs getting into the body · *criticism* — when people say something is wrong or bad · *culture* — a group of tiny living things grown together in a laboratory · *recover* — to get well again after being sick

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A New Research Center in Paris and a Life of Loss</summary>

> Mr X is a French chemist, not a licensed doctor.  
> He studies the tiny living things that cause disease.  
> In 1885, his treatment saves a boy bitten by a dog with rabies.  
> Newspapers around the world report the extraordinary news.  
> People from many countries send money to thank him.  
> With this money, a new research center opens in Paris in 1888.  
> Scientists there study disease and treat rabies patients who travel from far away.  
> Mr X already knows deep personal loss.  
> Three of his daughters die as children, two of them of typhoid.  
> Years earlier, a stroke leaves one side of his body weak.  
> Even so, he keeps directing his research with the help of loyal assistants.  
> After his death, these assistants carry on his work at the center.  
> **Who is Mr X?**

**Svar:** ⬜ Edward Jenner · ⬜ Robert Koch · ✅ Louis Pasteur · ⬜ Alexander Fleming

**Ord:** *licensed* — officially allowed to do a job, like being a doctor · *extraordinary* — very unusual or amazing · *typhoid* — a serious disease spread by dirty water and food · *stroke* — a sudden illness in the brain that can leave part of the body weak

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Polished Notebooks and a Rival in Berlin</summary>

> Mr X keeps detailed laboratory notebooks throughout his working life.  
> He tells his family that nobody may ever read them.  
> Decades later, in the 1970s, a historian finally studies these private notebooks.  
> The notebooks reveal that his public reports sometimes hide the messy, real story.  
> In one famous case, his published method differs from what he actually used.  
> Historians still debate how much this changes his reputation as a careful scientist.  
> They also ask if it was ethical to treat a boy for rabies in 1885 before the animal tests were finished.  
> In the 1880s, a rival scientist in Berlin, Robert Koch, studies the germs behind tuberculosis.  
> Robert Koch and Mr X compete fiercely, partly because their countries are rivals too.  
> This competition between French and German science pushes both men to work faster.  
> As germ theory becomes accepted, more hospitals begin washing hands and cleaning instruments carefully.  
> Death rates from infection in hospitals and disease in growing cities begin to fall.  
> **Who is Mr X?**

**Svar:** ⬜ Edward Jenner · ✅ Louis Pasteur · ⬜ Alexander Fleming · ⬜ Charles Darwin

**Ord:** *reputation* — what other people think and say about someone · *ethical* — right and fair according to moral rules · *rival* — someone who competes strongly against another person · *tuberculosis* — a serious lung disease caused by germs

</details>

### Alan Turing

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Boy Who Loved Puzzles and Long Runs</summary>

> Mr X is a boy in England, about a hundred years ago.  
> He loves numbers and hard puzzles.  
> He also loves running very long distances alone.  
> He is not the best student in other subjects.  
> Later, he studies at a famous old university in England.  
> As a young man, he dreams of a machine that follows a list of steps.  
> Such a machine could solve almost any puzzle.  
> Then a great war starts in Europe.  
> Mr X moves to a secret place with wooden huts.  
> Many clever men and women work there in secret.  
> They try to break a very hard enemy code.  
> Mr X and his friends find a way to read the enemy's secret messages.  
> **Who is Mr X?**

**Svar:** ⬜ Charles Babbage · ✅ Alan Turing · ⬜ Ada Lovelace · ⬜ Konrad Zuse

**Ord:** *hut* — a small simple building, often made of wood · *code* — a secret way of writing so only some people can read it · *puzzle* — a problem that is fun and hard to solve · *enemy* — a country or person you are fighting against in a war

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Bletchley Park, Enigma, and a Machine Called the Bombe</summary>

> Mr X studies mathematics at Cambridge, in England.  
> In 1939, a great war begins in Europe.  
> Mr X moves to Bletchley Park, a secret country estate.  
> There, teams try to break Enigma, a German machine that makes secret codes.  
> Polish mathematicians break the machine's secrets first, before the war.  
> Building on their work, Mr X helps design a large machine called the bombe.  
> Every day, it tests thousands of possible code settings.  
> Reading the German messages helps convoys of ships cross the Atlantic safely.  
> Thousands of people work at Bletchley Park, and most of them are women.  
> They must never tell anyone what they do there.  
> The secret is kept for about thirty years after the war.  
> **Who is Mr X?**

**Svar:** ✅ Alan Turing · ⬜ John von Neumann · ⬜ Claude Shannon · ⬜ Grace Hopper

**Ord:** *mathematics* — the study of numbers, shapes and patterns · *estate* — a large piece of land with a big house on it · *setting* — one specific way that a machine's parts are arranged · *convoy* — a group of ships that travel together for safety

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — A Machine on Paper and a Question About Thinking</summary>

> In 1936, a young Cambridge mathematician named Mr X publishes an unusual paper.  
> He imagines a simple machine that reads and writes symbols on a paper tape.  
> One such machine, built the right way, can copy the work of any other.  
> Soon after, he spends two years studying in Princeton, in the United States.  
> In 1948, he moves to Manchester and writes programs for one of the first real computers.  
> In 1950, he publishes a paper asking a simple question: can machines think?  
> He describes a game: a judge asks written questions to two hidden players.  
> One player is a person, the other is a computer program.  
> If the judge often cannot tell which is which, he says, the machine has passed the test.  
> In 1952, a law of that time punishes him for loving another man.  
> The government says sorry in 2009, and he is pardoned in 2013.  
> **Who is Mr X?**

**Svar:** ⬜ Charles Babbage · ⬜ Konrad Zuse · ✅ Alan Turing · ⬜ John von Neumann

**Ord:** *symbol* — a written mark that stands for a letter, a number or a sound · *tape* — a long thin strip, here used to store information · *judge* — a person who decides who is right, or who wins a game · *program* — a list of steps that tells a computer what to do

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A Computer Design, a Chess Program, and a Marathon Runner</summary>

> Mr X is a British mathematician who does secret work during a world war.  
> When the war ends in 1945, he still cannot tell anyone what he has done.  
> He joins a national laboratory near London and designs a computer of his own.  
> The machine is built later, smaller than he planned, and a company sells copies of it.  
> He also writes one of the first chess programs, by hand on paper.  
> No computer of the time can run it, so he plays the moves himself.  
> Outside work, he runs marathons and is among the fastest marathon runners in Britain.  
> In 1952, a law of that time punishes him for loving another man.  
> He dies in 1954.  
> The government says sorry in 2009, and he is pardoned in 2013.  
> **Who is Mr X?**

**Svar:** ⬜ Claude Shannon · ⬜ Konrad Zuse · ⬜ Grace Hopper · ✅ Alan Turing

**Ord:** *laboratory* — a place where scientists do tests and build new things · *designs* — makes a plan for how to build something · *chess* — a board game for two players with kings, queens and knights · *marathon* — a running race of about forty-two kilometers

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Founder, Secrets, and a Late Apology</summary>

> Historians today call Mr X one of the founders of computer science.  
> In 1936, he proves that some problems can never be solved by any machine.  
> Real computers, built about ten years later, follow the basic idea of his paper.  
> His codebreaking role in a world war is barely known until the 1970s.  
> Only then can historians begin to judge his part in that war.  
> The question and the game he describes in 1950 still shape how we test machines today.  
> Late in life, he studies why spots and stripes form on animal skin.  
> In 1952, a law of that time punishes him for loving another man.  
> He dies in 1954, and the inquest calls it suicide.  
> The government says sorry in 2009, and he is pardoned in 2013.  
> Today, the highest prize in computer science carries his name.  
> **Who is Mr X?**

**Svar:** ⬜ John von Neumann · ✅ Alan Turing · ⬜ Claude Shannon · ⬜ Charles Babbage

**Ord:** *founder* — a person who starts something important, like a new field of study · *codebreaking* — finding out how to read secret messages · *inquest* — an official inquiry to find out how a person died

</details>

### Florence Nightingale

<details>
<summary><b>Kort 1 · Årskurs 6</b> — The Rich Girl Who Wants to Nurse the Sick</summary>

> Miss X grows up in a rich family in England, about 200 years ago.  
> She has a big house, servants, and a comfortable life.  
> Most rich girls of her time do not choose a job at all.  
> One day, she says she hears a call from God.  
> She believes God wants her to help sick and hurt people.  
> Her family is not happy about her plan.  
> They want her to marry and stay quietly at home instead.  
> She trains as a nurse anyway, far from home.  
> Later, her country goes to war in a land far away.  
> She travels there with a small team of nurses.  
> At night, she walks through the hospital with a small lamp.  
> **Who is Miss X?**

**Svar:** ⬜ Mary Seacole · ✅ Florence Nightingale · ⬜ Elizabeth Blackwell · ⬜ Clara Barton

**Ord:** *servants* — people who are paid to work and help in a rich home · *call* — here, a strong feeling that God wants you to do something · *train* — to learn the skills you need for a job · *lamp* — a small light that burns oil or holds a candle

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Thirty-Eight Nurses in a Filthy War Hospital</summary>

> Miss X is a nurse in England in 1854.  
> Her country fights a war far away, called the Crimean War.  
> Newspapers report that wounded soldiers get very poor care.  
> Miss X leads a team of thirty-eight nurses to help.  
> They travel to a huge army hospital at Scutari, near Constantinople.  
> The building is dirty, cold, and full of rats.  
> Clean water and clean bandages are hard to find.  
> More soldiers die from disease than from their wounds.  
> Miss X works hard to make the wards cleaner and calmer.  
> She buys food and clean shirts for the soldiers with money from newspaper readers at home.  
> The next year, a special team cleans the hospital's sewers, and far fewer soldiers die.  
> When she goes home, the whole country calls her a hero.  
> **Who is Miss X?**

**Svar:** ⬜ Clara Barton · ⬜ Mary Seacole · ✅ Florence Nightingale · ⬜ Dorothea Dix

**Ord:** *wounded* — hurt badly in a fight or accident · *bandages* — strips of cloth used to cover a wound · *disease* — an illness, often caused by germs, not an injury · *ward* — a large room in a hospital with many beds · *sewer* — an underground pipe that carries away dirty water and waste

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Diagrams That Explain Why Soldiers Die</summary>

> Miss X is a nurse who comes home from a war far away.  
> After the war, she studies numbers, not battles.  
> She collects careful facts about every soldier who dies in hospital.  
> Most deaths come from disease, not from enemy weapons.  
> She draws colorful diagrams to show this clearly.  
> Army officials and politicians find the diagrams easy to read.  
> The diagrams help push for cleaner hospitals and cleaner army camps.  
> In 1858, a scientific society elects her as its first woman member.  
> That society studies numbers and facts about people and countries, called statistics.  
> Miss X argues that careful facts, not luck, save lives.  
> Her careful work slowly changes how governments plan health care.  
> **Who is Miss X?**

**Svar:** ⬜ Ada Lovelace · ✅ Florence Nightingale · ⬜ Elizabeth Blackwell · ⬜ Marie Curie

**Ord:** *diagrams* — pictures that use shapes or lines to show facts clearly · *officials* — people who have an important job in the army or government · *elects* — chooses someone for a role by voting · *statistics* — the study of facts and numbers about many people or things

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A School, a Book, and Years in Bed</summary>

> Miss X is born in an Italian city, and her family names her after it.  
> She grows up rich in England but later becomes sick from her time at war.  
> For the rest of her life, weak health often keeps her in bed.  
> Yet she keeps working hard from her bedroom for many years.  
> She writes a famous book about good nursing care.  
> Soon after, she opens a school for nurses in London.  
> The school trains women to nurse with clean, careful methods.  
> Officials in India ask for her advice about clean water and clean camps.  
> She never travels to India herself, but she studies its reports closely.  
> In 1907, a king gives her a high honor, the first time for a woman.  
> **Who is Miss X?**

**Svar:** ⬜ Marie Curie · ⬜ Edith Cavell · ⬜ Elizabeth Garrett Anderson · ✅ Florence Nightingale

**Ord:** *advice* — ideas about what someone should do · *honor* — a special way of showing great respect · *method* — a careful, planned way of doing something · *reports* — written accounts that describe facts or events

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — A Statistician, a Legend, and Another Nurse From Jamaica</summary>

> Miss X believes dirty air, not tiny living germs, causes most disease.  
> Later scientists show that germs are the true cause of infection.  
> Still, her hunt for clean air pushes hospitals to become cleaner anyway.  
> In 1855, during the Crimean War, deaths at her army hospital fall sharply after a team cleans its sewers.  
> Years later, Miss X studies this result closely and draws a clear lesson from it.  
> Popular stories later remember her mostly for her kindness at night.  
> Historians remind us she is also a tough, careful statistician.  
> Mary Seacole, a nurse from Jamaica, also wants to help in that war.  
> She asks to join the nurses sent out, but the officials say no.  
> So Mary Seacole cares for soldiers her own way instead.  
> Today, both women are honored as pioneers of modern nursing.  
> **Who is Miss X?**

**Svar:** ✅ Florence Nightingale · ⬜ Elizabeth Blackwell · ⬜ Clara Barton · ⬜ Marie Curie

**Ord:** *germs* — tiny living things, too small to see, that can cause disease · *infection* — illness caused by germs getting into the body · *statistician* — a person who studies facts and numbers carefully · *pioneers* — people who are among the first to try or achieve something new

</details>

### Isaac Newton

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Story About an Apple</summary>

> Mr X is born in a small village in England.  
> His father dies just before he is born.  
> He grows up on the family farm.  
> Later, he studies at a university.  
> A serious sickness closes the university for a time.  
> Mr X goes home to the farm.  
> He stays there for more than a year.  
> He thinks and thinks about the world around him.  
> Later in life, he tells a story about an apple.  
> He says he watches an apple fall from a tree.  
> He asks himself what pulls the apple down to the ground.  
> He wonders if the same pull holds the moon in the sky.  
> **Who is Mr X?**

**Svar:** ✅ Isaac Newton · ⬜ Galileo Galilei · ⬜ Charles Darwin · ⬜ Robert Hooke

**Ord:** *village* — a small place where people live, smaller than a town · *university* — a school where adults study after ordinary school · *sickness* — an illness, a disease · *pull* — a force that draws something toward it

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — A Prism, a Mirror, and Three Laws</summary>

> Mr X studies at a university in England.  
> A deadly plague closes it for a time, and he goes home.  
> He lets sunlight pass through a glass prism.  
> White light spreads into all the colors of a rainbow.  
> So white light is a mix of all colors, he says.  
> A glass lens splits light in the same way, so old telescopes blur the picture.  
> In 1668, he builds a telescope with a curved mirror instead.  
> The picture is sharper, and the tube is much shorter.  
> He becomes a professor at only 26.  
> Scholars in London are amazed by his small telescope.  
> He also writes down three simple laws about how things move.  
> One law says a moving thing keeps moving unless something stops it.  
> **Who is Mr X?**

**Svar:** ✅ Isaac Newton · ⬜ Galileo Galilei · ⬜ Robert Hooke · ⬜ Edmond Halley

**Ord:** *plague* — a dangerous disease that spreads quickly and kills many people · *prism* — a piece of glass with flat sides that splits light into colors · *lens* — a curved piece of glass that bends light · *mirror* — a smooth surface that reflects light and shows a picture

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — One Force for Earth and Sky</summary>

> Mr X becomes a famous scholar in England.  
> In a letter to a rival, he writes a line that sounds humble.  
> He says he sees far only by standing on the shoulders of giants.  
> In 1687, he publishes his greatest book.  
> The book gives exact laws for how forces move all things.  
> It also describes one single force called gravitation.  
> Every object pulls every other object, he says, and heavy objects pull hardest.  
> The force that makes a stone fall also holds the moon in its path.  
> The moon's pull lifts the seas and makes the tides.  
> The same force keeps every planet moving around the sun.  
> Before this book, earth and sky seem to follow different rules.  
> After it, one set of laws explains both.  
> **Who is Mr X?**

**Svar:** ⬜ Galileo Galilei · ✅ Isaac Newton · ⬜ Johannes Kepler · ⬜ Gottfried Leibniz

**Ord:** *scholar* — a person who studies and knows a lot about a subject · *rival* — a person who competes against you or disagrees with you · *gravitation* — the pulling force between the earth, the moon, and all other things · *tide* — the rise and fall of the sea, twice each day

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A Bitter Argument, a Coin, and a Secret Furnace</summary>

> Mr X invents a powerful new kind of mathematics.  
> Some years later, a mathematician in Paris invents very similar ideas.  
> His name is Gottfried Leibniz, and he works alone too.  
> For years, the two men argue about who was first.  
> Followers on both sides write angry letters.  
> The bitter argument lasts until both men are dead.  
> Later in life, Mr X takes a high post at the royal money house.  
> There, he hunts down men who make fake coins.  
> He studies court records and questions witnesses himself.  
> Few people know that he also spends years on secret experiments.  
> In a hot furnace, he tries to turn cheap metals into gold.  
> He also fills many private pages with his own ideas about the Bible.  
> **Who is Mr X?**

**Svar:** ⬜ Johannes Kepler · ✅ Isaac Newton · ⬜ Robert Hooke · ⬜ Edmond Halley

**Ord:** *mathematician* — a person who is an expert in numbers and mathematics · *witness* — a person who sees something happen and can tell others about it · *fake* — not real, made to look like something it is not · *furnace* — a closed fire built to make things very hot

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — Standing on Other Men's Work</summary>

> Mr X becomes one of the most famous scientists in history.  
> But historians remind us he does not work alone in an empty room.  
> Earlier thinkers already study falling objects and moving planets.  
> A rival scientist already guesses that a pulling force weakens with distance.  
> Mr X takes such scattered clues and proves them with exact mathematics.  
> He writes far more pages about old chemistry and about the Bible than about motion.  
> Colleagues describe him as brilliant but also difficult and secretive.  
> He rarely admits his own mistakes, and he almost never forgives a rival.  
> More than two hundred years later, new science changes some of his rules.  
> Even so, his basic laws still guide bridges, rockets, and machines today.  
> **Who is Mr X?**

**Svar:** ⬜ Robert Hooke · ✅ Isaac Newton · ⬜ Christiaan Huygens · ⬜ Gottfried Leibniz

**Ord:** *historian* — a person who studies and writes about the past · *distance* — how far away one thing is from another · *colleague* — a person you work with · *secretive* — keeping many things hidden or private

</details>

### Albert Einstein

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Compass, a Desk, and a Big Question</summary>

> Mr X is a small boy in Germany, more than 140 years ago.  
> His family says he is slow to start talking.  
> One day his father shows him a small compass.  
> The needle always points the same way, and this amazes him.  
> He wants to know why, and he never stops asking why.  
> He also loves to play the violin.  
> As a young man, he cannot find a steady job as a teacher.  
> He takes a job in an office in Switzerland instead.  
> His job is to check other people's new inventions.  
> In his free time, he thinks about light and time.  
> Years later, his strange ideas are tested, and he becomes famous all over the world.  
> **Who is Mr X?**

**Svar:** ✅ Albert Einstein · ⬜ Isaac Newton · ⬜ Michael Faraday · ⬜ Niels Bohr

**Ord:** *compass* — a small tool with a needle that always points north · *violin* — a small wooden music instrument with strings, played with a bow · *invention* — a new thing that a person makes for the first time · *amaze* — to surprise someone very much

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — One Strange Year, Then a Ship Away</summary>

> Mr X works in a quiet office, more than 100 years ago.  
> In one single year, he writes four amazing papers.  
> One paper says light can act like tiny particles, not only waves.  
> Another paper explains why tiny bits of matter dance in water under a microscope.  
> A third paper gives strange new rules for space and time.  
> A fourth paper says mass and huge energy are really the same thing.  
> Only a few scientists notice these papers at first.  
> Many years later, he wins a great science prize.  
> The prize is for the paper about light as particles.  
> It is not for his idea called relativity, which is even more famous.  
> In 1933, a new dictator takes power in his home country.  
> Mr X leaves for good and sails to safety in the United States.  
> **Who is Mr X?**

**Svar:** ⬜ Max Planck · ✅ Albert Einstein · ⬜ Ernest Rutherford · ⬜ Lise Meitner

**Ord:** *particle* — a very, very small piece of something · *matter* — anything that takes up space, like water, wood, or air · *microscope* — a tool with lenses that makes very small things look big · *dictator* — a ruler who has all the power and lets nobody disagree

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — Starlight Bends, Just as He Says</summary>

> Mr X works out a strange new idea about space and time.  
> Others soon call the idea relativity.  
> Nothing can travel faster than the speed of light, he says.  
> Time itself can run slower or faster, depending on speed.  
> Ten years later, he finishes an even bigger version of the idea.  
> This time, it is about gravity.  
> Gravity is not a pull, he says, but a bending of space itself.  
> Heavy stars and planets bend the space and time around them.  
> If he is right, starlight should bend when it passes close to the sun.  
> In 1919, a total eclipse hides the sun's light for a few minutes.  
> Scientists photograph stars near the darkened sun and measure the bending.  
> The result supports his idea, and he becomes famous all over the world.  
> **Who is Mr X?**

**Svar:** ⬜ Arthur Eddington · ⬜ Max Planck · ✅ Albert Einstein · ⬜ James Clerk Maxwell

**Ord:** *gravity* — the force that pulls things toward each other, like the earth pulling you down · *relativity* — a scientific idea that connects space, time, and motion · *eclipse* — when the moon covers the sun and the sky goes dark for a while · *bend* — to curve, so something is no longer straight

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — A Letter, a Weapon, and an Offer Refused</summary>

> In 1933, a dictator takes power in Germany.  
> Mr X leaves, and by the late 1930s he lives safely in the United States.  
> He hears that scientists in Europe can now split the tiny core of an atom.  
> Splitting this core can release a huge burst of energy.  
> Other scientists worry that the dictator's country could build a powerful weapon.  
> Just before a great war begins in Europe, Mr X signs a letter to the American president.  
> The letter warns that such a weapon is now possible.  
> He never works on the weapon project himself.  
> Years later, the weapon is used, and he feels deep regret.  
> For the rest of his life, he speaks and writes for peace between nations.  
> Late in his life, Israel offers him its highest office.  
> He kindly refuses, saying he understands ideas better than people.  
> **Who is Mr X?**

**Svar:** ⬜ Leo Szilard · ⬜ Otto Hahn · ✅ Albert Einstein · ⬜ Max Planck

**Ord:** *atom* — one of the very small pieces that everything is made of · *weapon* — a tool made to hurt or destroy · *regret* — a sad feeling about something you wish had not happened · *refuse* — to say no to an offer

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — The Icon and the Man Behind It</summary>

> By the 1920s, Mr X has changed how scientists think about space, time, and gravity.  
> His ideas go beyond the laws of motion that rule science for two hundred years.  
> In the same decade, a new and stranger science takes full shape: quantum theory.  
> This theory says that, deep down, nature may only offer chances, never certainty.  
> Mr X helps start this new science, but he never accepts its full picture.  
> He famously argues that nature cannot simply leave things to pure chance.  
> Most physicists disagree with him, and quantum theory keeps succeeding.  
> In 1939, worried colleagues persuade him to sign a fateful letter.  
> Historians still debate how much responsibility one signature really carries.  
> His face becomes one of the most printed and copied images in history.  
> Yet the real man is often anxious, uncertain, and privately self-critical.  
> The famous icon and the real man are not quite the same person.  
> **Who is Mr X?**

**Svar:** ⬜ Niels Bohr · ⬜ Isaac Newton · ✅ Albert Einstein · ⬜ Ernest Rutherford

**Ord:** *quantum theory* — a science of very small things, like atoms, that often works by chance · *certainty* — being completely sure that something is true · *fateful* — having very important and serious results later · *icon* — a person or image that stands for something famous and important

</details>

### Marie Curie

<details>
<summary><b>Kort 1 · Årskurs 6</b> — A Secret School and a Glowing Jar in a Shed</summary>

> Mrs X is a girl in Warsaw, more than 150 years ago.  
> A foreign empire rules her country at this time.  
> Girls cannot study at the university there.  
> So young women study in secret, in a different room each time.  
> For about five years, Mrs X works as a governess.  
> She saves money to help her sister study first.  
> At last, she travels to Paris herself.  
> She studies late into the night, often hungry and cold.  
> Later, she works in a cold wooden shed.  
> Inside, a strange new substance glows softly in the dark.  
> **Who is Mrs X?**

**Svar:** ✅ Marie Curie · ⬜ Rosalind Franklin · ⬜ Emmy Noether · ⬜ Ada Lovelace

**Ord:** *empire* — a large group of countries or lands ruled by one power · *governess* — a woman paid to teach children at home · *substance* — a material, the stuff that a thing is made of · *glow* — to give off a soft, gentle light

</details>

<details>
<summary><b>Kort 2 · Årskurs 9</b> — Two New Elements and a Prize Never Given to a Woman Before</summary>

> Mrs X now works as a scientist in Paris.  
> She studies strange rays coming from a heavy dark ore.  
> With her husband, she searches for their true source.  
> Within one year, they find two new elements.  
> They name one polonium, after her home country, and one radium.  
> It then takes years of hard work to make a tiny amount of pure radium.  
> In 1903, Mrs X wins the Nobel Prize.  
> She is the first woman ever to win it.  
> Three years later, her husband dies in a street accident.  
> She keeps working alone, deep in grief.  
> The Sorbonne then gives her his old post.  
> She becomes its very first woman professor.  
> **Who is Mrs X?**

**Svar:** ⬜ Lise Meitner · ✅ Marie Curie · ⬜ Chien-Shiung Wu · ⬜ Elizabeth Blackwell

**Ord:** *ore* — rock that contains a useful metal or material · *element* — one of the basic simple substances that make up everything · *grief* — the deep sad feeling after someone dies · *post* — a job or official position

</details>

<details>
<summary><b>Kort 3 · Årskurs 12</b> — The Second Prize, and a Body Slowly Paying the Price</summary>

> Mrs X already holds the Nobel Prize from years earlier.  
> Her husband has died, but she keeps working alone.  
> In 1911, she wins the Nobel Prize a second time, for her own research.  
> She becomes the first person in history to win two.  
> By now, she works daily with strong glowing substances.  
> People say she carries small glowing tubes around in her pocket.  
> She loves the soft light they give at night.  
> Few yet understand how much the invisible rays can hurt the body over many years.  
> Slowly, her hands grow rough, and her eyes grow weak.  
> Years of exposure quietly damage her health.  
> **Who is Mrs X?**

**Svar:** ⬜ Elizabeth Blackwell · ⬜ Grace Hopper · ✅ Marie Curie · ⬜ Mary Seacole

**Ord:** *research* — careful study to find out new things · *substance* — a material, the stuff that a thing is made of · *invisible* — impossible to see · *exposure* — being close to something, again and again, over time

</details>

<details>
<summary><b>Kort 4 · Årskurs 12</b> — X-ray Cars at the Front, and Notebooks Locked in Lead</summary>

> The great war of 1914 begins in Europe.  
> Wounded soldiers arrive at hospitals every single day.  
> Mrs X has an idea to help doctors see broken bones fast.  
> She puts simple X-ray machines inside ordinary cars.  
> She trains young women to drive and use the machines near the front.  
> Her own teenage daughter works beside her as a helper.  
> The X-ray service they build examines more than a million wounded men.  
> After the war, Mrs X returns to her quiet laboratory.  
> She dies in 1934, worn out after decades near strong radiation.  
> Even today, her old notebooks are too radioactive to touch safely.  
> **Who is Mrs X?**

**Svar:** ⬜ Lise Meitner · ✅ Marie Curie · ⬜ Mary Seacole · ⬜ Rosalind Franklin

**Ord:** *wounded* — hurt or injured, often in a war · *front* — the place where two armies fight closest to each other · *radioactive* — giving off strong invisible rays that can harm the body

</details>

<details>
<summary><b>Kort 5 · Universitet</b> — A Prize Almost Without Her Name</summary>

> In 1903, a Nobel Prize committee first plans to honor only two men.  
> One of the men, her husband, insists that her name be added too.  
> So her name is added, and she shares the prize.  
> Eight years later, a second prize follows, for her own work alone.  
> That same year, a hostile press attacks her private life instead of her science.  
> Some newspapers even question whether a foreign-born woman deserves such honors.  
> Historians later study these attacks as a case of gender and prejudice.  
> Her life also raises a hard question about the price of new knowledge.  
> More than sixty years after her death, France moves her remains to its great hall of honored citizens.  
> She becomes the first woman honored there for her own achievements.  
> **Who is Mrs X?**

**Svar:** ⬜ Emmy Noether · ✅ Marie Curie · ⬜ Chien-Shiung Wu · ⬜ Lise Meitner

**Ord:** *committee* — a small group of people chosen to decide something · *hostile* — unfriendly and full of anger · *prejudice* — an unfair opinion about someone formed before knowing them · *remains* — here: the body of a person who has died

</details>

## Kortens struktur

Varje person får fem oberoende kort med stigande svårighetsgrad:

- 1 kort årskurs 6
- 1 kort årskurs 9
- 2 kort årskurs 12
- 1 kort universitet

Varje kort innehåller:

- **Korttext**: 7–12 superkorta meningar på superenkel engelska.
  Personen anonymiseras som "Mr X" och frågan är "Who is Mr X?".
  (De befintliga korten är skrivna i presens; kravet hävdes av Roger
  2026-08-26, så tempus är fritt i kommande produktion.)
- **Fyra svarsalternativ**, varav ett rätt (Rogers regeldokument aug 2026).
  Distraktorerna hämtas i möjligaste mån från masterlistans övriga namn.
- **Ordlista**: 1–4 svåra ord med superenkla förklaringar (som i exempelkorten).
- **Två bildbriefer** (huvudbild + sidobild): beskrivning, Shutterstock-sökning,
  AI-prompt som alternativ, samt bildtext på enkel engelska. Sidobilden förklarar
  där det går ett svårt ord eller nyckelbegrepp.
- **Svensk översättning** av korttext, fråga, svarsalternativ, ordförklaringar
  och bildtexter (nytt upplägg 2026-08-26: varje kort levereras på både
  engelska och svenska). Svenska fält för befintliga kort produceras löpande;
  de 20 granskade översättningarna i `poangpromenad/stationer.md` återanvänds.

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

- ~~Fyra eller fem svarsalternativ?~~ **Avgjort** i Rogers regeldokument aug 2026:
  fyra gäller. Samtliga kort har uppdaterats (svagaste distraktorn struken).
  Se `docs/regler-2026-08-sammanfattning.md` för övriga nya regler och öppna frågor.
- Vilket filformat vill Akelius produktion ha i slutänden? `data/cards.json` är
  strukturerad så att den lätt kan omvandlas; be gärna om Akelius mallfil.
- Bildlicenser: briefer med Shutterstock-sökningar och AI-prompter ingår per kort;
  själva bildvalet/inköpet görs lämpligen mot Akelius Shutterstock-konto.

## Nästa steg

Fortsätta beta av masterlistan (se `docs/master-lista-50.md`) i valfri ordning —
korten är produktionsmässigt oberoende per person/skeende, precis som Roger noterar.
