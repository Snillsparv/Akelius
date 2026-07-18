#!/usr/bin/env python3
"""Importera kortset från cards/<slug>.md till data/cards.json.

Parsar husformatet (rubriker, blockquote-korttext, ✅/⬜-alternativ,
ordförklaringar och bildbriefernas fyra fält) och lägger till/ersätter
setet i cards.json. Validerar strukturen innan något skrivs.

Användning:
  python3 tools/import_cards.py <slug> [<slug> ...]
  python3 tools/import_cards.py --check <slug>   (bara validera, skriv inget)
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

LEVELS = {
    'Årskurs 6': 'grade 6',
    'Årskurs 9': 'grade 9',
    'Årskurs 12 (A)': 'grade 12 A',
    'Årskurs 12 (B)': 'grade 12 B',
    'Universitet': 'university',
}


def parse_set(slug):
    text = (ROOT / 'cards' / f'{slug}.md').read_text(encoding='utf-8')
    m = re.match(r'# (.+?) — fem frågekort', text)
    if not m:
        sys.exit(f'{slug}: hittar ingen titelrad')
    person = m.group(1).strip()

    card_blocks = re.split(r'(?m)^## Kort ', text)[1:]
    if len(card_blocks) != 5:
        sys.exit(f'{slug}: {len(card_blocks)} kort, förväntade 5')

    cards = []
    for block in card_blocks:
        head = re.match(r'(\d) · (.+?) — (.+)', block.splitlines()[0])
        if not head:
            sys.exit(f'{slug}: oväntad kortrubrik: {block.splitlines()[0]!r}')
        level = LEVELS.get(head.group(2).strip())
        if not level:
            sys.exit(f'{slug}: okänd nivå {head.group(2)!r}')
        title = head.group(3).strip()

        cat = re.search(r'\*\*Kategori:\*\* `([^`]+)`', block)
        if not cat:
            sys.exit(f'{slug} kort {head.group(1)}: saknar kategori')

        quote = re.findall(r'(?m)^> (.*?)[ \t]*$', block)
        if not quote:
            sys.exit(f'{slug} kort {head.group(1)}: saknar korttext')
        qm = re.match(r'\*\*(.+?)\*\*$', quote[-1])
        if not qm:
            sys.exit(f'{slug} kort {head.group(1)}: sista blockquote-raden är inte fetstilad fråga')
        question = qm.group(1).strip()
        sentences = [q for q in quote[:-1] if q.strip()]
        if not 7 <= len(sentences) <= 12:
            sys.exit(f'{slug} kort {head.group(1)}: {len(sentences)} meningar (utanför 7–12)')

        opts = re.findall(r'(?m)^- (✅|⬜) (.+?)[ \t]*$', block)
        if len(opts) != 5 or sum(1 for s, _ in opts if s == '✅') != 1:
            sys.exit(f'{slug} kort {head.group(1)}: alternativfel ({len(opts)} st)')
        options = [o for _, o in opts]
        correct = next(o for s, o in opts if s == '✅')

        words = [{'word': w, 'explanation': e} for w, e in
                 re.findall(r'(?m)^- \*\*(.+?)\*\* — \*(.+?)\*[ \t]*$', block)]

        def image(section):
            part = re.search(r'### ' + section + r'\n(.*?)(?=\n### |\n---|\Z)', block, re.S)
            if not part:
                sys.exit(f'{slug} kort {head.group(1)}: saknar {section}')
            t = part.group(1)
            fields = {}
            for key, pat in [
                ('description', r'\*\*Motiv:\*\* (.+)'),
                ('caption', r'\*\*Bildtext:\*\* \*(.+?)\*'),
                ('shutterstock_query', r'\*\*Shutterstock-sökning:\*\* `(.+?)`'),
                ('ai_prompt', r'\*\*AI-prompt(?: \(alternativ\))?:\*\* (.+)'),
            ]:
                fm = re.search(pat, t)
                if not fm:
                    sys.exit(f'{slug} kort {head.group(1)} {section}: saknar {key}')
                fields[key] = fm.group(1).strip()
            return fields

        cards.append({
            'level': level, 'title': title, 'category': cat.group(1),
            'text_sentences': sentences, 'question': question,
            'options': options, 'correct': correct, 'words': words,
            'main_image': image('Huvudbild'), 'side_image': image('Sidobild'),
        })
    return {'slug': slug, 'person': person, 'cards': cards}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    check_only = '--check' in sys.argv
    if not args:
        sys.exit(__doc__)
    parsed = [parse_set(slug) for slug in args]
    for p in parsed:
        print(f"{p['slug']}: OK — {p['person']}, 5 kort, "
              f"nivåer {[c['level'] for c in p['cards']]}")
    if check_only:
        return
    path = ROOT / 'data' / 'cards.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    existing = {s['slug']: i for i, s in enumerate(data['sets'])}
    for p in parsed:
        if p['slug'] in existing:
            data['sets'][existing[p['slug']]] = p
        else:
            data['sets'].append(p)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f"cards.json: nu {len(data['sets'])} set")


if __name__ == '__main__':
    main()
