from pathlib import Path
for p in Path('.').rglob('*'):
    if not p.is_file() or '.git' in p.parts or '__pycache__' in p.parts:
        continue
    try: lines=p.read_text(encoding='utf-8').splitlines()
    except UnicodeDecodeError: continue
    for n,line in enumerate(lines,1):
        if '# TODO:' in line or '<!-- TODO:' in line:
            print(f'{p}:{n}: {line.strip()}')
