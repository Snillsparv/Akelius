#!/usr/bin/env python3
"""Bygg om data/image-prompts.csv från data/cards.json.

En rad per bild: <slug>-<kortnr>-main (3:2) och <slug>-<kortnr>-side (3:4).
Prompten är kortets ai_prompt med avslutande punkt plus det fasta
no-text-suffixet. Kör efter varje ny import:
  python3 tools/build_prompts.py
"""
import csv, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SUFFIX = ' No readable text, letters, numbers, logos, or watermarks anywhere in the image.'


def main():
    data = json.loads((ROOT / 'data' / 'cards.json').read_text(encoding='utf-8'))
    rows = []
    for s in data['sets']:
        for i, c in enumerate(s['cards'], 1):
            for kind, ratio in (('main', '3:2'), ('side', '3:4')):
                prompt = c[f'{kind}_image']['ai_prompt'].strip()
                if not prompt.endswith('.'):
                    prompt += '.'
                rows.append({'id': f"{s['slug']}-{i}-{kind}", 'ratio': ratio,
                             'prompt': prompt + SUFFIX})
    path = ROOT / 'data' / 'image-prompts.csv'
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'ratio', 'prompt'])
        w.writeheader()
        w.writerows(rows)
    print(f'image-prompts.csv: {len(rows)} rader')


if __name__ == '__main__':
    main()
