#!/usr/bin/env python3
"""Rename AI-generated card images to their prompt IDs.

The generated files must have been downloaded in the same order as the
prompts in data/image-prompts.csv. The script sorts the files by their
modification time and pairs them with the CSV rows.

Usage:
  python3 rename_images.py <folder>                 dry run - shows the mapping
  python3 rename_images.py <folder> --apply         actually renames the files
  python3 rename_images.py <folder> --start 51      for the next batch of images
  python3 rename_images.py <folder> --csv <path>    use a local CSV instead of the web

Always check the dry-run mapping (and the spot checks it suggests) before --apply.
"""
import argparse, csv, io, pathlib, sys, urllib.request

CSV_URL = 'https://snillsparv.github.io/Akelius/data/image-prompts.csv'
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp', '.tif', '.tiff'}


def load_rows(csv_arg):
    if csv_arg:
        text = pathlib.Path(csv_arg).read_text(encoding='utf-8')
    else:
        local = pathlib.Path(__file__).resolve().parent.parent / 'data' / 'image-prompts.csv'
        if local.exists():
            text = local.read_text(encoding='utf-8')
        else:
            print(f'Hämtar promptlistan från {CSV_URL} ...')
            with urllib.request.urlopen(CSV_URL) as r:
                text = r.read().decode('utf-8')
    return list(csv.DictReader(io.StringIO(text)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('folder', help='mapp med de nedladdade bilderna')
    ap.add_argument('--apply', action='store_true', help='döp om på riktigt (annars bara visning)')
    ap.add_argument('--start', type=int, default=1, help='första promptens radnummer i CSV:n (1 = första)')
    ap.add_argument('--csv', help='sökväg till image-prompts.csv (annars repo/webben)')
    args = ap.parse_args()

    rows = load_rows(args.csv)
    folder = pathlib.Path(args.folder).expanduser()
    files = sorted(
        (p for p in folder.iterdir() if p.suffix.lower() in IMAGE_EXTS and p.is_file()),
        key=lambda p: (p.stat().st_mtime, p.name),
    )
    if not files:
        sys.exit(f'Inga bildfiler hittades i {folder}')

    ids = [r['id'] for r in rows[args.start - 1: args.start - 1 + len(files)]]
    if len(ids) < len(files):
        sys.exit(f'CSV:n har bara {len(ids)} prompter kvar från rad {args.start}, '
                 f'men mappen innehåller {len(files)} bilder. Fel --start?')

    width = max(len(f.name) for f in files)
    print(f'{len(files)} bilder i {folder} (sorterade på ändringstid):\n')
    for f, pid in zip(files, ids):
        print(f'  {f.name:<{width}}  ->  {pid}{f.suffix.lower()}')

    first, last = ids[0], ids[-1]
    print(f'\nStickprov innan du kör --apply:')
    print(f'  Äldsta filen ({files[0].name}) ska vara: {first}')
    print(f'  Nyaste filen ({files[-1].name}) ska vara: {last}')

    if not args.apply:
        print('\nTorrkörning - inget har döpts om. Kör igen med --apply när mappningen ser rätt ut.')
        return

    taken = {p.name for p in folder.iterdir()}
    for f, pid in zip(files, ids):
        target = folder / f'{pid}{f.suffix.lower()}'
        if target.name in taken and target != f:
            sys.exit(f'Stopp: {target.name} finns redan i mappen - städa och försök igen.')
    for f, pid in zip(files, ids):
        f.rename(folder / f'{pid}{f.suffix.lower()}')
    print(f'\nKlart! {len(files)} filer omdöpta.')


if __name__ == '__main__':
    main()
