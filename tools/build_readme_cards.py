#!/usr/bin/env python3
"""Regenerera README-sektionen "## Korten" från data/cards.json.

Skriver om allt mellan rubriken "## Korten" och "## Kortens struktur"
i samma format som tidigare leveranser: ett <details>-block per kort med
blockquote-text, svarsrad med facit och ordlista. Kör efter varje import:
  python3 tools/build_readme_cards.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEVELS = {'grade 6': 'Årskurs 6', 'grade 9': 'Årskurs 9',
          'grade 12': 'Årskurs 12', 'university': 'Universitet'}


def render(sets):
    out = ['## Korten', '']
    for s in sets:
        out.append(f"### {s.get('person_sv', s['person'])}")
        out.append('')
        for i, c in enumerate(s['cards'], 1):
            out.append('<details>')
            out.append(f"<summary><b>Kort {i} · {LEVELS[c['level']]}</b> — {c['title']}</summary>")
            out.append('')
            for sent in c['text_sentences']:
                out.append(f'> {sent}  ')
            out.append(f"> **{c['question']}**")
            out.append('')
            svar = ' · '.join(('✅ ' if o == c['correct'] else '⬜ ') + o for o in c['options'])
            out.append(f'**Svar:** {svar}')
            if c['words']:
                out.append('')
                ord_ = ' · '.join(f"*{w['word']}* — {w['explanation']}" for w in c['words'])
                out.append(f'**Ord:** {ord_}')
            out.append('')
            out.append('</details>')
            out.append('')
    return '\n'.join(out)


def main():
    data = json.loads((ROOT / 'data' / 'cards.json').read_text(encoding='utf-8'))
    p = ROOT / 'README.md'
    t = p.read_text(encoding='utf-8')
    start = t.index('## Korten')
    end = t.index('## Kortens struktur')
    p.write_text(t[:start] + render(data['sets']) + '\n' + t[end:], encoding='utf-8')
    n = sum(len(s['cards']) for s in data['sets'])
    print(f"README: Korten-sektionen ombyggd, {len(data['sets'])} ämnen, {n} kort")


if __name__ == '__main__':
    main()
