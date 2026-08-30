#!/usr/bin/env python3
"""Generera saknade kortbilder med gpt-image-2 från data/image-prompts.csv.

Huvudbilder (3:2) genereras i 1536x1024 och sparas som de är.
Sidobilder (3:4) genereras i 1024x1536 och mittbeskärs till 1024x1365
(fönster (0, 85, 1024, 1450)), samma efterbehandling som leverans 1-3.

Hoppar över id:n som redan har fil i images/. Kör:
  python3 tools/generate_images.py [--only <prefix>] [--workers N] [--limit N]
"""
import base64, concurrent.futures, csv, io, json, os, pathlib, sys, time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = ROOT / 'images'
API = 'https://api.openai.com/v1/images/generations'
SIZES = {'3:2': '1536x1024', '3:4': '1024x1536'}
SIDE_CROP = (0, 85, 1024, 1450)


def generate(row):
    from PIL import Image
    out = IMAGES / (row['id'] + '.png')
    body = json.dumps({
        'model': 'gpt-image-2', 'prompt': row['prompt'],
        'size': SIZES[row['ratio']], 'quality': 'high', 'n': 1,
    }).encode()
    for attempt in range(3):
        try:
            req = urllib.request.Request(API, data=body, headers={
                'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY'],
                'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=600) as r:
                data = json.load(r)
            png = base64.b64decode(data['data'][0]['b64_json'])
            img = Image.open(io.BytesIO(png))
            if row['ratio'] == '3:4':
                img = img.crop(SIDE_CROP)
            img.save(out, 'PNG')
            return row['id'], 'ok'
        except Exception as e:
            if attempt == 2:
                return row['id'], f'FEL: {e}'
            time.sleep(5 * (attempt + 1))


def main():
    args = sys.argv[1:]
    only = args[args.index('--only') + 1] if '--only' in args else ''
    workers = int(args[args.index('--workers') + 1]) if '--workers' in args else 4
    limit = int(args[args.index('--limit') + 1]) if '--limit' in args else None
    rows = list(csv.DictReader((ROOT / 'data' / 'image-prompts.csv').open(encoding='utf-8')))
    todo = [r for r in rows if r['id'].startswith(only) and not (IMAGES / (r['id'] + '.png')).exists()]
    if limit:
        todo = todo[:limit]
    print(f'{len(todo)} bilder att generera ({workers} parallella)')
    fails = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        for iid, status in ex.map(generate, todo):
            print(iid, status, flush=True)
            fails += status != 'ok'
    print(f'klart: {len(todo) - fails} ok, {fails} fel')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
