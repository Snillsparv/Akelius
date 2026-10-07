#!/usr/bin/env python3
"""Exportera alla kort till granskningsbara filer för Akelius layoutteam.

Skapar i export/:
  Akelius-quiz-cards-EN-<datum>.pdf   ett kort per A4-sida, engelska
  Akelius-quiz-cards-SV-<datum>.pdf   samma på svenska
  Akelius-quiz-cards-text-<datum>.xlsx all text, en rad per kort, EN och SV

Sidlayouten följer Akelius A6-skiss (Daniel Shea, sept/okt 2026): vänster
del är framsidan (ledtrådstext, bild, fråga, fyra svar), höger del är
baksidan (svar, ordförklaringar, andra bilden). Ordlisteord är fetade i
texten som i skissen. Kort utan färdig bild visar bildbriefen.

PDF:erna renderas med tools/export_pdf.js (Playwright + systemets Chromium),
som också kontrollerar att ingen sida flödar över. Kör:
  python3 tools/export_cards.py [--date 2026-10-07] [--skip-pdf]
"""
import html, json, pathlib, re, subprocess, sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = ROOT / 'images'
OUT = ROOT / 'export'
BUILD = OUT / 'build'
IMG_OUT = BUILD / 'img'
PAGES_URL = 'https://snillsparv.github.io/Akelius/images/'

MAIN_W, SIDE_W, JPEG_Q = 580, 380, 70

T = {
    'en': {
        'front': 'Front', 'back': 'Back', 'answer': 'Answer', 'words': 'Words',
        'pending': 'Picture in production', 'brief': 'Picture brief',
        'topic': 'Topic', 'card': 'Card {k} of {n}', 'page': 'Page',
        'levels': {'grade 6': 'Grade 6', 'grade 9': 'Grade 9',
                   'grade 12': 'Grade 12', 'university': 'University'},
        'contents': 'Contents', 'pics_pending': 'pictures in production',
        'cover_title': 'Akelius Quiz Cards',
        'cover_sub': 'World history',
        'cover_count': '{t} topics · {c} cards · English',
        'cover_date': 'Content export, {d}',
        'cover_by': 'Text and pictures: Jonas von Essen',
        'legend_h': 'How to read this file',
        'legend': [
            'Each page is one card. The left part is the front: clue text, '
            'picture, question and four answers. The right part is the back: '
            'the answer, word explanations and a second picture.',
            'The correct answer is marked with a tick. Words in bold in the '
            'clue text are explained on the back.',
            'Every topic has five cards: grade 6, grade 9, two cards for '
            'grade 12, and university. Each card stands alone.',
            'All text has passed an independent historian review and an '
            'editor review. Every card also exists in Swedish.',
            'The pictures are AI-generated and reviewed one by one. For '
            '{p} topics some or all pictures are still in production; those '
            'cards show a short picture brief instead.',
            'All text is also in the Excel file, one row per card, ready for '
            'layout and translation.',
        ],
    },
    'sv': {
        'front': 'Framsida', 'back': 'Baksida', 'answer': 'Rätt svar',
        'words': 'Ordförklaringar', 'pending': 'Bild under produktion',
        'brief': 'Bildbrief på engelska', 'topic': 'Ämne', 'card': 'Kort {k} av {n}',
        'page': 'Sida',
        'levels': {'grade 6': 'Årskurs 6', 'grade 9': 'Årskurs 9',
                   'grade 12': 'Årskurs 12', 'university': 'Universitet'},
        'contents': 'Innehåll', 'pics_pending': 'bilder under produktion',
        'cover_title': 'Akelius frågekort',
        'cover_sub': 'Världshistoria',
        'cover_count': '{t} ämnen · {c} kort · svenska',
        'cover_date': 'Innehållsexport, {d}',
        'cover_by': 'Text och bild: Jonas von Essen',
        'legend_h': 'Så läser du filen',
        'legend': [
            'Varje sida är ett kort. Vänstra delen är framsidan: ledtrådstext, '
            'bild, fråga och fyra svar. Högra delen är baksidan: svaret, '
            'ordförklaringar och en andra bild.',
            'Rätt svar är markerat med en bock. Fetade ord i ledtrådstexten '
            'förklaras på baksidan.',
            'Varje ämne har fem kort: årskurs 6, årskurs 9, två kort för '
            'årskurs 12 och universitet. Varje kort fungerar fristående.',
            'All text har gått igenom oberoende historikergranskning och '
            'redaktörsgranskning. Varje kort finns också på engelska.',
            'Bilderna är AI-genererade och granskade en och en. För {p} ämnen '
            'är några eller alla bilder fortfarande under produktion; de korten '
            'visar en kort bildbrief, på engelska, i stället.',
            'All text finns också i Excelfilen, en rad per kort, redo för '
            'layout och översättning.',
        ],
    },
}

CAT_SV = {'civilizations': 'civilisation', 'religions': 'religion',
          'middle ages': 'medeltiden', 'renaissance': 'renässansen',
          'exploration': 'upptäcktsresor', 'science': 'vetenskap',
          'revolutions': 'revolutioner', 'ideas': 'idéhistoria',
          'twentieth century': '1900-talet', 'mathematics': 'matematik',
          'africa': 'Afrika', 'colonialism': 'kolonialism', 'asia': 'Asien',
          'latin america': 'Latinamerika', 'middle east': 'Mellanöstern'}

CAT_EN = {'africa': 'Africa', 'asia': 'Asia', 'latin america': 'Latin America',
          'middle east': 'Middle East'}

SUFFIX = {'en': r'(?:s|es|ed|d|ing|er|ers)?',
          'sv': r'(?:en|et|n|t|na|er|ar|or|erna|arna|orna|a|e|s|ande|de|te|r|ens|ets|s)?'}

CSS = """
@page { size: 297mm 210mm; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: Verdana, 'DejaVu Sans', sans-serif; color: #111; }
.page { width: 297mm; height: 210mm; padding: 9mm 11mm 8mm; position: relative;
  overflow: hidden; page-break-after: always; break-after: page; }
.page:last-child { page-break-after: auto; break-after: auto; }
.pno { position: absolute; bottom: 4mm; right: 11mm; font-size: 7pt; color: #777; }
.head { display: flex; justify-content: space-between; align-items: baseline;
  font-size: 8pt; color: #555; border-bottom: 0.3mm solid #bbb; padding-bottom: 1.5mm;
  margin-bottom: 4mm; height: 7mm; }
.head b { color: #111; font-size: 9.5pt; }
.body { display: flex; gap: 0; height: 176mm; }
.front { width: 186mm; padding-right: 6mm; display: flex; gap: 6mm; }
.back { width: 89mm; border-left: 0.4mm dashed #999; padding-left: 6mm;
  display: flex; flex-direction: column; }
.label { font-size: 7pt; letter-spacing: 0.12em; text-transform: uppercase;
  color: #777; margin-bottom: 2mm; }
.textcol { width: 96mm; display: flex; flex-direction: column; overflow: hidden; }
.text { font-size: 10.5pt; line-height: 1.38; overflow: hidden; }
.text p { margin: 0 0 1.1mm; }
.right { width: 78mm; display: flex; flex-direction: column; overflow: hidden; }
.mainimg { width: 78mm; height: 52mm; object-fit: cover; display: block; background: #eee; }
.cap { font-size: 7.5pt; color: #444; font-style: italic; margin: 1.2mm 0 0; line-height: 1.3; }
.q { font-size: 10.5pt; font-weight: bold; margin: 4mm 0 2mm; line-height: 1.35; }
.opts { list-style: none; margin: 0; padding: 0; font-size: 10.5pt; }
.opts li { display: flex; align-items: flex-start; gap: 2.5mm; margin-bottom: 1.8mm; line-height: 1.3; }
.box { width: 3.6mm; height: 3.6mm; border: 0.35mm solid #333; flex: none; margin-top: 0.5mm;
  display: flex; align-items: center; justify-content: center; font-size: 8pt; line-height: 1; }
.opts li.ok { font-weight: bold; }
.opts li.ok .box { background: #111; color: #fff; }
.tag { margin-top: auto; font-size: 8pt; color: #333; }
.tag span { display: inline-block; border: 0.3mm solid #333; padding: 0.6mm 2mm; margin-right: 1.5mm; }
.ans { font-size: 11pt; font-weight: bold; margin-bottom: 4mm; }
.words { font-size: 9pt; line-height: 1.35; margin: 0 0 3mm; }
.words div { margin-bottom: 2mm; }
.sideimg { width: 54mm; height: 72mm; object-fit: cover; display: block; background: #eee; margin-top: auto; }
.ph { background: #eee; border: 0.3mm dashed #999; color: #444; font-size: 7.5pt;
  padding: 3mm; line-height: 1.35; overflow: hidden; }
.ph b { display: block; font-size: 8pt; margin-bottom: 1mm; color: #222; }
.ph.main { width: 78mm; height: 52mm; }
.ph.side { width: 54mm; height: 72mm; margin-top: auto; }
.title { font-size: 8pt; color: #555; }
.nw { white-space: nowrap; }
/* stegvis tätare typografi om en sida inte får plats */
.page.fit1 .text, .page.fit1 .q, .page.fit1 .opts { font-size: 9.8pt; }
.page.fit2 .text, .page.fit2 .q, .page.fit2 .opts { font-size: 9.2pt; }
.page.fit2 .words { font-size: 8.4pt; }
.page.fit3 .text, .page.fit3 .q, .page.fit3 .opts { font-size: 8.6pt; }
.page.fit3 .words { font-size: 8pt; }
.page.fit2 .ph, .page.fit3 .ph { font-size: 6.8pt; }
/* omslag och innehåll */
.cover { padding: 22mm 26mm; }
.cover h1 { font-size: 30pt; margin: 0 0 2mm; }
.cover .sub { font-size: 15pt; color: #333; margin-bottom: 8mm; }
.cover .meta { font-size: 10.5pt; line-height: 1.7; margin-bottom: 10mm; }
.cover h2 { font-size: 12pt; margin: 0 0 3mm; }
.cover ul { font-size: 10pt; line-height: 1.5; margin: 0; padding-left: 5mm; max-width: 220mm; }
.cover li { margin-bottom: 2mm; }
.toc h2 { font-size: 13pt; margin: 0 0 4mm; }
.toc .cols { column-count: 2; column-gap: 12mm; font-size: 8.6pt; line-height: 1.42; }
.toc .row { display: flex; break-inside: avoid; }
.toc .row .n { width: 8mm; color: #666; }
.toc .row .t { flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
.toc .row .p { width: 14mm; text-align: right; }
.toc .note { font-size: 8pt; color: #555; margin-top: 3mm; }
"""


def esc(s):
    return html.escape(str(s), quote=True)


def brief(s):
    """Bildbriefer är interna arbetsanteckningar med tankstreck; utåt blir de kommatecken."""
    return re.sub(r'\s*[—–]\s*|\s+-\s+', ', ', s or '')


def motif(s, limit=420):
    """Platshållarens text: briefens motiv utan produktionsnoten, kapat vid meningsgräns."""
    m = re.split(r'(?i)\s*(?:important\s+)?production note\s*:', brief(s))[0].strip()
    # meningar om vilket engelskt ordlisteord bilden förklarar hör inte hemma utåt
    m = re.sub(r"(?i)(?:^|(?<=[.;] ))(?:(?:it|this|the)(?:\s+(?:picture|image|photo))?\s+)?(?:also\s+)?"
               r"(?:helps?\s+(?:to\s+)?)?(?:explains?|supports?|illustrates?)\b[^.;]*\b(?:words?|phrase)\b"
               r"[^.;]*[.;]\s*", '', m).strip()
    if len(m) <= limit:
        return m
    cut = max(m.rfind('. ', 0, limit), m.rfind('; ', 0, limit))
    return (m[:cut + 1] if cut > limit // 2 else m[:m.rfind(' ', 0, limit)].rstrip(',;')) + ' …'


def image_ids():
    return {p.stem for p in IMAGES.glob('*.png')}


def prepare_images(ids):
    from PIL import Image
    IMG_OUT.mkdir(parents=True, exist_ok=True)
    stamp = IMG_OUT / '.params'
    params = f'{MAIN_W}-{SIDE_W}-{JPEG_Q}'
    fresh = stamp.exists() and stamp.read_text() == params
    made = 0
    for iid in sorted(ids):
        src = IMAGES / f'{iid}.png'
        dst = IMG_OUT / f'{iid}.jpg'
        if fresh and dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
            continue
        w = MAIN_W if iid.endswith('-main') else SIDE_W
        im = Image.open(src).convert('RGB')
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(dst, 'JPEG', quality=JPEG_Q,
                                               optimize=True, progressive=True)
        made += 1
    stamp.write_text(params)
    return made


def topic_name(s, lang):
    """Visningsnamn för ett ämne; tankstreck i namnet blir kolon."""
    name = s.get('person_sv', s['person']) if lang == 'sv' else s['person']
    return name.replace(' - ', ': ')


STEM_RULES = {
    'en': (('man', 'men'), ('y', ''), ('e', '')),
    # handelsman/handelsmän, kloster/klostret, partikel/partiklar, öken/öknen
    'sv': (('man', 'män'), ('are', 'ar'), ('ium', 'i'), ('a', ''), ('e', ''),
           ('er', 'r'), ('el', 'l'), ('en', 'n')),
}


def stems(word, lang, minlen=4):
    """Ordstammar som tål böjningar där ändelsen byts: källa/källor, century/centuries."""
    out = [word]
    for end, new in STEM_RULES[lang]:
        if word.lower().endswith(end):
            out.append(word[:-len(end)] + new)
    return [s for s in out if len(s) >= minlen]


def term_patterns(term, lang):
    """Mönster i fallande säkerhet: exakt ord med ändelse, stam som också fångar
    sammansättningar (laser i laserljus), och för partikelverb (köra om, hitta på)
    verbet med partikeln, eller bara verbet när partikeln följer några ord senare."""
    words = term.split()
    yield r'(?<!\w)(' + re.escape(esc(term)) + SUFFIX[lang] + r')(?!\w)'
    if len(words) == 1:
        for st in stems(term, lang):
            yield r'(?<!\w)(' + re.escape(esc(st)) + r'\w*)'
        return
    first = [re.escape(esc(st)) for st in stems(words[0], lang, minlen=3) or [words[0]]]
    rest = r'\s+'.join(re.escape(esc(x)) for x in words[1:]) + r'(?!\w)'
    for st in first:
        yield r'(?<!\w)(' + st + r'\w*\s+' + rest + ')'
    for st in first:
        yield r'(?<!\w)(' + st + r'\w*)(?=(?:\s+[^\s<]+){0,4}\s+' + rest + ')'


def bold_words(sentences, words, lang):
    """Feta första förekomsten av varje ordlisteord, som i Akelius skiss. Förekomster
    med samma skiftläge som ordlistan går före, så att "stat" inte fetas i "Staten"."""
    out = [esc(s) for s in sentences]

    def bold_first(pat):
        for i, s in enumerate(out):
            # hoppa över redan fetad text för att inte nästla taggar
            parts = re.split(r'(<b>.*?</b>)', s)
            for j, part in enumerate(parts):
                if part.startswith('<b>'):
                    continue
                new, n = pat.subn(r'<b>\1</b>', part, count=1)
                if n:
                    parts[j] = new
                    out[i] = ''.join(parts)
                    return True
        return False

    for w in words:
        term = w['word'].strip()
        if term:
            any(bold_first(re.compile(p, flags))
                for p in term_patterns(term, lang) for flags in (0, re.IGNORECASE))
    # 1430-talet och liknande bryts aldrig vid bindestrecket
    return [re.sub(r'(\w+(?:-\w+)+)', r'<span class="nw">\1</span>', x) for x in out]


def localized(card, lang):
    if lang == 'en':
        return {
            'title': card['title'], 'sentences': card['text_sentences'],
            'question': card['question'], 'options': card['options'],
            'correct': card['correct'], 'words': card['words'],
            'main_cap': card['main_image']['caption'],
            'side_cap': card['side_image']['caption'],
            'category': CAT_EN.get(card['category'], card['category']),
        }
    sv = card['sv']
    return {
        'title': sv['title'], 'sentences': sv['text_sentences'],
        'question': sv['question'], 'options': sv['options'],
        'correct': sv['correct'], 'words': sv['words'],
        'main_cap': sv['main_caption'], 'side_cap': sv['side_caption'],
        'category': CAT_SV.get(card['category'], card['category']),
    }


def figure(kind, iid, have, cap, desc, t):
    if iid in have:
        cls = 'mainimg' if kind == 'main' else 'sideimg'
        img = f'<img class="{cls}" src="img/{iid}.jpg" alt="">'
    else:
        img = (f'<div class="ph {kind}"><b>{esc(t["pending"])}</b>'
               f'{esc(t["brief"])}: {esc(motif(desc))}</div>')
    return img + f'<p class="cap">{esc(cap)}</p>'


def card_page(set_no, s, k, card, have, lang, page_no):
    t = T[lang]
    L = localized(card, lang)
    topic = topic_name(s, lang)
    n = len(s['cards'])
    iid = f"{s['slug']}-{k}"
    sentences = bold_words(L['sentences'], L['words'], lang)
    opts = ''.join(
        f'<li class="{"ok" if o == L["correct"] else ""}"><span class="box">'
        f'{"✓" if o == L["correct"] else ""}</span><span>{esc(o)}</span></li>'
        for o in L['options'])
    words = ''.join(f'<div><b>{esc(w["word"])}</b>: {esc(w["explanation"])}</div>'
                    for w in L['words'])
    level = t['levels'].get(card['level'], card['level'])
    question = re.sub(r' X(?!\w)', ' X', L['question'])  # "X?" hamnar aldrig ensamt på en rad
    return f"""
<section class="page card" data-id="{iid}">
  <div class="head">
    <div><b>{esc(t['topic'])} {set_no} · {esc(topic)}</b>
      &nbsp;·&nbsp; {esc(t['card'].format(k=k, n=n))}</div>
    <div class="title">{esc(L['title'])}</div>
  </div>
  <div class="body">
    <div class="front">
      <div class="textcol">
        <div class="label">{esc(t['front'])}</div>
        <div class="text">{''.join(f'<p>{x}</p>' for x in sentences)}</div>
      </div>
      <div class="right">
        <div class="label">&nbsp;</div>
        {figure('main', iid + '-main', have, L['main_cap'], card['main_image']['description'], t)}
        <div class="q">{esc(question)}</div>
        <ul class="opts">{opts}</ul>
        <div class="tag"><span>{esc(level)}</span><span>{esc(L['category'])}</span></div>
      </div>
    </div>
    <div class="back">
      <div class="label">{esc(t['back'])}</div>
      <div class="ans">{esc(t['answer'])}: {esc(L['correct'])}</div>
      <div class="words">{words}</div>
      {figure('side', iid + '-side', have, L['side_cap'], card['side_image']['description'], t)}
    </div>
  </div>
  <div class="pno">{esc(t['page'])} {page_no}</div>
</section>"""


def build_html(data, have, lang, when):
    t = T[lang]
    sets = data['sets']
    pending = [s for s in sets if not all(
        f"{s['slug']}-{k}-{x}" in have for k in range(1, len(s['cards']) + 1)
        for x in ('main', 'side'))]
    n_cards = sum(len(s['cards']) for s in sets)
    first_card_page = 3
    pages = []
    legend = ''.join(f'<li>{esc(x.format(p=len(pending)))}</li>' for x in t['legend'])
    pages.append(f"""
<section class="page cover">
  <h1>{esc(t['cover_title'])}</h1>
  <div class="sub">{esc(t['cover_sub'])}</div>
  <div class="meta">{esc(t['cover_count'].format(t=len(sets), c=n_cards))}<br>
    {esc(t['cover_date'].format(d=when))}<br>{esc(t['cover_by'])}</div>
  <h2>{esc(t['legend_h'])}</h2>
  <ul>{legend}</ul>
  <div class="pno">{esc(t['page'])} 1</div>
</section>""")
    rows, p = [], first_card_page
    pend_slugs = {s['slug'] for s in pending}
    for i, s in enumerate(sets, 1):
        name = topic_name(s, lang)
        star = ' *' if s['slug'] in pend_slugs else ''
        rows.append(f'<div class="row"><span class="n">{i}</span>'
                    f'<span class="t">{esc(name)}{star}</span><span class="p">{p}</span></div>')
        p += len(s['cards'])
    pages.append(f"""
<section class="page toc">
  <h2>{esc(t['contents'])}</h2>
  <div class="cols">{''.join(rows)}</div>
  <div class="note">* {esc(t['pics_pending'])}</div>
  <div class="pno">{esc(t['page'])} 2</div>
</section>""")
    p = first_card_page
    for i, s in enumerate(sets, 1):
        for k, card in enumerate(s['cards'], 1):
            pages.append(card_page(i, s, k, card, have, lang, p))
            p += 1
    doc = (f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8">'
           f'<title>{esc(t["cover_title"])}</title><style>{CSS}</style></head>'
           f'<body>{"".join(pages)}</body></html>')
    return doc, p - 1, len(pending)


def build_xlsx(data, have, path, when):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font
    from openpyxl.utils import get_column_letter
    wb = Workbook()
    readme = wb.active
    readme.title = 'Read me'
    n_cards = sum(len(s['cards']) for s in data['sets'])
    lines = [
        ('Akelius Quiz Cards · World history', True),
        (f'Content export {when}. {len(data["sets"])} topics, {n_cards} cards, '
         'English and Swedish.', False),
        ('', False),
        ('Sheets', True),
        ('Topics: one row per topic, with picture status.', False),
        ('Cards EN and Cards SV: one row per card. Text has one sentence per line.', False),
        ('', False),
        ('Columns', True),
        ('Card ID: topic number and card number, for example 012-3.', False),
        ('Correct: the right answer, also given as a letter A to D in the order of the options.', False),
        ('Words: word explanations, one per line as word: explanation.', False),
        ('Main and side picture: file name, link to the full-resolution file, caption, '
         'picture brief and a Shutterstock search query for replacing the AI picture with a photo.', False),
        ('', False),
        ('Notes', True),
        ('Picture file names contain the topic name, which is the answer. Rename them '
         'before any student-facing use.', False),
        ('Pictures are AI-generated and reviewed one by one. Where the link is empty, '
         'the picture is still in production.', False),
        ('Card text, title, captions and word list never name the answer.', False),
    ]
    for r, (txt, bold) in enumerate(lines, 1):
        c = readme.cell(row=r, column=1, value=txt)
        c.font = Font(bold=bold, size=12 if bold else 11)
    readme.column_dimensions['A'].width = 120

    topics = wb.create_sheet('Topics')
    head = ['#', 'Topic (EN)', 'Topic (SV)', 'Category', 'Cards', 'Pictures ready', 'Slug']
    topics.append(head)
    for i, s in enumerate(data['sets'], 1):
        ready = sum(1 for k in range(1, len(s['cards']) + 1) for x in ('main', 'side')
                    if f"{s['slug']}-{k}-{x}" in have)
        topics.append([i, topic_name(s, 'en'), topic_name(s, 'sv'), s['cards'][0]['category'],
                       len(s['cards']), f'{ready} of {2 * len(s["cards"])}', s['slug']])

    def card_rows(lang):
        rows = []
        for i, s in enumerate(data['sets'], 1):
            for k, card in enumerate(s['cards'], 1):
                L = localized(card, lang)
                iid = f"{s['slug']}-{k}"
                letter = 'ABCD'[L['options'].index(L['correct'])]
                level = T[lang]['levels'].get(card['level'], card['level'])
                topic = topic_name(s, lang)
                row = [f'{i:03d}-{k}', i, topic, k, level, L['category'], L['title'],
                       '\n'.join(L['sentences']), L['question'], *L['options'],
                       L['correct'], letter,
                       '\n'.join(f"{w['word']}: {w['explanation']}" for w in L['words'])]
                for kind, cap in (('main', L['main_cap']), ('side', L['side_cap'])):
                    pid = f'{iid}-{kind}'
                    img = card[f'{kind}_image']
                    row += [f'{pid}.png', PAGES_URL + f'{pid}.png' if pid in have else '',
                            cap, brief(img['description']), brief(img['shutterstock_query'])]
                rows.append(row)
        return rows

    cols = ['Card ID', 'Topic #', 'Topic', 'Card #', 'Level', 'Category', 'Title',
            'Text', 'Question', 'Option A', 'Option B', 'Option C', 'Option D',
            'Correct', 'Correct letter', 'Words',
            'Main picture file', 'Main picture link', 'Main caption', 'Main picture brief',
            'Main Shutterstock query',
            'Side picture file', 'Side picture link', 'Side caption', 'Side picture brief',
            'Side Shutterstock query']
    widths = [9, 7, 26, 6, 11, 14, 30, 70, 22, 18, 18, 18, 18, 18, 7, 45,
              26, 30, 36, 45, 30, 26, 30, 36, 45, 30]
    for name, lang in (('Cards EN', 'en'), ('Cards SV', 'sv')):
        ws = wb.create_sheet(name)
        ws.append(cols)
        for row in card_rows(lang):
            ws.append(row)
        for c, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(c)].width = w
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.alignment = Alignment(wrap_text=True, vertical='top')
        ws.freeze_panes = 'C2'
        ws.auto_filter.ref = ws.dimensions
    for ws in (topics, wb['Cards EN'], wb['Cards SV']):
        for cell in ws[1]:
            cell.font = Font(bold=True)
    topics.freeze_panes = 'A2'
    for c, w in enumerate([5, 40, 40, 18, 7, 14, 28], 1):
        topics.column_dimensions[get_column_letter(c)].width = w
    wb.save(path)


def main():
    args = sys.argv[1:]
    when = args[args.index('--date') + 1] if '--date' in args else date.today().isoformat()
    data = json.loads((ROOT / 'data' / 'cards.json').read_text(encoding='utf-8'))
    missing_sv = [s['slug'] for s in data['sets'] if not all('sv' in c for c in s['cards'])]
    if missing_sv:
        sys.exit(f'Svenska saknas för: {missing_sv}')
    have = image_ids()
    BUILD.mkdir(parents=True, exist_ok=True)
    made = prepare_images(have)
    print(f'bilder: {len(have)} finns, {made} nya exportkopior')
    xlsx = OUT / f'Akelius-quiz-cards-text-{when}.xlsx'
    build_xlsx(data, have, xlsx, when)
    print('skrev', xlsx.relative_to(ROOT))
    for lang in ('en', 'sv'):
        doc, last_page, n_pending = build_html(data, have, lang, when)
        html_path = BUILD / f'cards-{lang}.html'
        html_path.write_text(doc, encoding='utf-8')
        pdf = OUT / f'Akelius-quiz-cards-{lang.upper()}-{when}.pdf'
        print(f'{lang}: {last_page} sidor, {n_pending} ämnen med bilder under produktion')
        if '--skip-pdf' in args:
            continue
        subprocess.run(['node', str(ROOT / 'tools' / 'export_pdf.js'), str(html_path),
                        str(pdf), str(last_page)], check=True)


if __name__ == '__main__':
    main()
