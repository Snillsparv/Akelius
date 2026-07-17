#!/usr/bin/env python3
"""Bygg webbsidorna från data/cards.json och images/.

Gör två saker:
  1. Skapar webboptimerade JPEG-kopior av images/*.png i images/web/
     (originalen i PNG är produktionsmaster och rörs aldrig).
  2. Skriver om de genererade raderna i index.html (interna förhandsvisningen
     med briefer och platshållare) och presentation.html (granskningssidan
     som bara visar ämnen där alla bilder är klara):
       const DATA = [...];        <- innehållet i data/cards.json (sets)
       const HAVE = new Set([...]); <- bild-ID:n som har filer i images/

Kör efter varje ny bildbatch eller ändring i cards.json:
  python3 tools/build_index.py
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = ROOT / 'images'
WEB = IMAGES / 'web'
JPEG_QUALITY = 87


def build_web_copies():
    try:
        from PIL import Image
    except ImportError:
        sys.exit('Pillow saknas - kör: pip install pillow')
    WEB.mkdir(exist_ok=True)
    made = 0
    for png in sorted(IMAGES.glob('*.png')):
        jpg = WEB / (png.stem + '.jpg')
        if jpg.exists() and jpg.stat().st_mtime >= png.stat().st_mtime:
            continue
        img = Image.open(png).convert('RGB')
        img.save(jpg, 'JPEG', quality=JPEG_QUALITY, optimize=True, progressive=True)
        made += 1
    return made


def main():
    made = build_web_copies() if IMAGES.exists() else 0
    ids = sorted(p.stem for p in IMAGES.glob('*.png')) if IMAGES.exists() else []

    cards = json.loads((ROOT / 'data' / 'cards.json').read_text(encoding='utf-8'))
    missing = [s['person'] for s in cards['sets'] if 'slug' not in s]
    if missing:
        sys.exit(f'Sets utan slug i cards.json: {missing}')

    data_line = 'const DATA = ' + json.dumps(cards['sets'], ensure_ascii=False) + ';'
    have_line = 'const HAVE = new Set(' + json.dumps(ids) + ');'

    for name in ('index.html', 'presentation.html'):
        html_path = ROOT / name
        if not html_path.exists():
            continue
        html = html_path.read_text(encoding='utf-8')
        html, n_data = re.subn(r'(?m)^const DATA = .*$', lambda m: data_line, html, count=1)
        if not n_data:
            sys.exit(f'Hittade inte raden "const DATA = ..." i {name}')
        if re.search(r'(?m)^const HAVE = .*$', html):
            html = re.sub(r'(?m)^const HAVE = .*$', lambda m: have_line, html, count=1)
        else:
            html = html.replace(data_line, data_line + '\n' + have_line, 1)
        html_path.write_text(html, encoding='utf-8')

    n_sets = len(cards['sets'])
    n_cards = sum(len(s['cards']) for s in cards['sets'])
    print(f'index.html + presentation.html uppdaterade: {n_sets} ämnen, '
          f'{n_cards} kort, {len(ids)} bilder ({made} nya webbkopior).')


if __name__ == '__main__':
    main()
