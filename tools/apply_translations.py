#!/usr/bin/env python3
"""Merga svenska översättningar från translations/<slug>.sv.json in i data/cards.json.

Validerar varje översättning innan något skrivs:
  - samma antal kort som setet, samma antal meningar per kort som engelskan
  - exakt fyra options i samma ordning som engelskan (positionsmatchning),
    och det rätta svarets svenska form sätts som cards[i].sv.correct
  - inga tankstreck i löptext (pratminus "- " först i mening är ok)
  - inga parenteser i svenska textfält
  - svarsläcka: kortets rätta svenska svar (ordstam) får inte förekomma i
    kortets egen svenska text, bildtexter eller ordförklaringar
  - ordlistan högst lika många poster som engelskan

Användning:
  python3 tools/apply_translations.py [--check] [<slug> ...]   (utan slugs: alla filer)
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TRANS = ROOT / 'translations'

REQUIRED = ['title', 'text_sentences', 'question', 'options', 'words',
            'main_caption', 'side_caption']


def leak_stem(answer):
    """Ordstam för läckkontroll: 'Vikingarna' -> 'viking', 'Rom' -> 'rom'."""
    a = answer.lower()
    a = re.sub(r'^(the |de |den |det )', '', a)
    a = a.split()[0] if a.split() else a
    for suffix in ('arna', 'erna', 'orna', 'en', 'et', 'na', 'ar', 'er'):
        if len(a) > len(suffix) + 3 and a.endswith(suffix):
            return a[:-len(suffix)]
    return a


def validate(slug, tr, eng_set, problems):
    cards = tr.get('cards', [])
    if len(cards) != len(eng_set['cards']):
        problems.append(f'{slug}: {len(cards)} kort, engelskan har {len(eng_set["cards"])}')
        return
    if not tr.get('person_sv'):
        problems.append(f'{slug}: saknar person_sv')
    for i, (sv, en) in enumerate(zip(cards, eng_set['cards']), 1):
        where = f'{slug} kort {i}'
        for f in REQUIRED:
            if f not in sv:
                problems.append(f'{where}: saknar fältet {f}')
        if len(sv.get('text_sentences', [])) != len(en['text_sentences']):
            problems.append(f'{where}: {len(sv.get("text_sentences", []))} meningar, '
                            f'engelskan har {len(en["text_sentences"])}')
        opts = sv.get('options', [])
        if len(opts) != 4:
            problems.append(f'{where}: {len(opts)} options')
        if len(sv.get('words', [])) > len(en['words']):
            problems.append(f'{where}: fler ordposter än engelskan')
        text_fields = (sv.get('text_sentences', []) +
                       [sv.get('question', ''), sv.get('main_caption', ''), sv.get('side_caption', '')] +
                       [w.get('word', '') + ' ' + w.get('explanation', '') for w in sv.get('words', [])])
        joined = '\n'.join(text_fields)
        if '—' in joined or '–' in joined:
            problems.append(f'{where}: tankstreck i svensk text')
        for t in text_fields:
            if re.search(r'\S - ', t):
                problems.append(f'{where}: bindestreck som tankstreck mitt i mening: {t[:60]!r}')
        if '(' in joined or ')' in joined:
            problems.append(f'{where}: parentes i svensk text')
        try:
            correct_sv = opts[en['options'].index(en['correct'])]
        except (ValueError, IndexError):
            problems.append(f'{where}: kan inte positionsmatcha rätt svar')
            continue
        stem = leak_stem(correct_sv)
        if sv.get('leak_ok'):
            continue  # dokumenterat undantag, t.ex. Augustus-kortets "augusti"-ledtråd
        if len(stem) >= 3:
            for t in text_fields:
                if re.search(r'(?i)' + re.escape(stem), t):
                    problems.append(f'{where}: möjlig svarsläcka, stammen {stem!r} i {t[:60]!r}')


def main():
    check_only = '--check' in sys.argv
    slugs = [a for a in sys.argv[1:] if not a.startswith('--')]
    data = json.loads((ROOT / 'data' / 'cards.json').read_text(encoding='utf-8'))
    by_slug = {s['slug']: s for s in data['sets']}
    files = ([TRANS / f'{s}.sv.json' for s in slugs] if slugs
             else sorted(TRANS.glob('*.sv.json')))
    problems, applied = [], 0
    for path in files:
        if not path.exists():
            problems.append(f'{path.name}: filen saknas')
            continue
        tr = json.loads(path.read_text(encoding='utf-8'))
        slug = tr.get('slug', path.stem.replace('.sv', ''))
        if slug not in by_slug:
            problems.append(f'{slug}: okänt set')
            continue
        eng_set = by_slug[slug]
        before = len(problems)
        validate(slug, tr, eng_set, problems)
        if len(problems) > before:
            continue
        applied += 1
        if check_only:
            continue
        eng_set['person_sv'] = tr['person_sv']
        for sv, en in zip(tr['cards'], eng_set['cards']):
            en['sv'] = {
                'title': sv['title'],
                'text_sentences': sv['text_sentences'],
                'question': sv['question'],
                'options': sv['options'],
                'correct': sv['options'][en['options'].index(en['correct'])],
                'words': sv['words'],
                'main_caption': sv['main_caption'],
                'side_caption': sv['side_caption'],
            }
    for p in problems:
        print('PROBLEM:', p)
    if problems and not check_only:
        sys.exit(f'{len(problems)} problem - inget skrivet för berörda set')
    if not check_only and applied:
        (ROOT / 'data' / 'cards.json').write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    done = sum(1 for s in data['sets'] if all('sv' in c for c in s['cards']))
    print(f'{"kontrollerade" if check_only else "applicerade"}: {applied} set, '
          f'{len(problems)} problem. Set med komplett svenska: {done}/{len(data["sets"])}')


if __name__ == '__main__':
    main()
