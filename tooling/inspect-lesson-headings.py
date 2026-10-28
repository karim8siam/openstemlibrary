import zipfile, re

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

batch1_slugs = [
    'engineering-mechanics',
    'mechanics-of-solids',
    'engineering-thermodynamics',
    'fluid-mechanics',
    'manufacturing-processes'
]

with zipfile.ZipFile(archive, 'r') as z:
    for slug in batch1_slugs:
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/lessons/"
        names = sorted([n for n in z.namelist() if n.startswith(prefix) and n.endswith('.md')])
        print(f"=== {slug} ({len(names)} lessons) ===")
        # check headings in lesson 1 and lesson 2
        for lf in names[:2]:
            content = z.read(lf).decode('utf-8', errors='ignore')
            h2s = [l.strip() for l in content.splitlines() if l.startswith('##')]
            print(f"  {lf.split('/')[-1]}: {h2s}")
        print()
