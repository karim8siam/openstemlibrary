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
        content = z.read(f"OpenSTEM-Mechanical-Engineering/books/{slug}/BOOK.md").decode('utf-8', errors='ignore')
        print(f"=== {slug} ===")
        # search for Unit 1 through Unit 8
        for u in range(1, 9):
            m = re.search(r'#+\s*Unit\s+' + str(u) + r'\s*[:—\-]\s*([^\n]+)', content)
            if m:
                # clean if has lesson in it
                t = m.group(1).strip()
                t = re.sub(r'\s*·\s*Lesson.*$', '', t)
                print(f"  Unit {u}: {t}")
            else:
                print(f"  Unit {u}: Not found by regex")
        print()
