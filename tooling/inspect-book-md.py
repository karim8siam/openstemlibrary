import zipfile, re

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    for slug in ['engineering-mechanics', 'mechanics-of-solids', 'fluid-mechanics']:
        content = z.read(f"OpenSTEM-Mechanical-Engineering/books/{slug}/BOOK.md").decode('utf-8', errors='ignore')
        print(f"=== {slug} BOOK.md ===")
        # search for Unit headings
        units = re.findall(r'#+\s*(?:Unit\s+\d+|Part\s+\d+)[^\n]+', content)
        print(f"  Unit headings found: {len(units)}")
        for u in units[:8]:
            print(f"    {u}")
        print()
