import zipfile

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    names = z.namelist()
    for slug in ['automotive-engineering', 'fluid-mechanics', 'engineering-reliability-and-maintenance', 'heat-transfer']:
        print(f'=== {slug} ===')
        book_files = [n for n in names if n.startswith(f'OpenSTEM-Mechanical-Engineering/books/{slug}/')]
        for f in sorted(book_files)[:25]:
            print(' ', f.replace(f'OpenSTEM-Mechanical-Engineering/books/{slug}/', ''))
