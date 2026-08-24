# Akelius frågekort — världshistoria

Produktion av frågekort i världshistoria för Akelius Foundations utbildningsmaterial,
på uppdrag av Roger Akelius (mejl 2026-07-12).

Korten används tryckta som spelkort och online, i skolor i Afrika, Asien,
Latinamerika och Europa, samt i språkundervisning för flyktingar.
Akelius översätter till tio andra språk.

## Levererade kort

**110 kort · 22 ämnen**, samtliga faktagranskade och specgranskade:

- **Leverans 1** — Sokrates, Platon *(Rogers startförslag)*
- **Leverans 2** — Aristoteles, Forntida Egypten (pyramiderna), Mesopotamien,
  Hammurabi, Fenicierna & alfabetet, Alexander den store, Romerska
  republiken/kejsardömet, Julius Caesar, Konfucius, Siddhartha Gautama (Buddha)
- **Leverans 3** — Antikens Grekland, Olympiska spelen, Augustus, Jesus från
  Nasaret, Muhammed, Bysantinska riket, Vikingarna, Korstågen, Digerdöden,
  Djingis khan

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
(220 st för leverans 1–3: 110 kort × huvudbild + sidobild).

**Status: 220 av 220 bilder klara** — samtliga kort i leverans 1–3 har
huvudbild och sidobild. Varje batch har kvalitetsgranskats bild för bild
mot sina briefer, och underkända bilder har genererats om.

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

Fullständiga kort med bildbriefer finns i `cards/`-mappen; här visas text,
svar (✅ = rätt) och ordlista.

<!-- CARDS:START -->

### Forntida Egypten – pyramiderna

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


### Mesopotamien – de första städerna och skriften

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
<summary><b>Kort 5 · Universitet</b> — The Socratic problem</summary>

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


### Siddhartha Gautama (Buddha)

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


<!-- CARDS:END -->

## Kortens struktur

Varje person får fem oberoende kort med stigande svårighetsgrad:

- 1 kort årskurs 6
- 1 kort årskurs 9
- 2 kort årskurs 12
- 1 kort universitet

Varje kort innehåller:

- **Korttext**: 7–12 superkorta meningar på superenkel engelska, i presens.
  Personen anonymiseras som "Mr X" och frågan är "Who is Mr X?".
- **Fyra svarsalternativ**, varav ett rätt (Rogers regeldokument aug 2026).
  Distraktorerna hämtas i möjligaste mån från masterlistans övriga namn.
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
