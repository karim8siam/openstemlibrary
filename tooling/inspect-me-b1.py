import zipfile, re, json

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

batch1_slugs = [
    'engineering-mechanics',
    'mechanics-of-solids',
    'engineering-thermodynamics',
    'fluid-mechanics',
    'manufacturing-processes'
]

with zipfile.ZipFile(archive, 'r') as z:
    names = z.namelist()
    for slug in batch1_slugs:
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/"
        book_files = [n for n in names if n.startswith(prefix)]
        lessons = sorted([n for n in book_files if n.startswith(f"{prefix}lessons/") and n.endswith('.md')])
        sim_htmls = sorted([n for n in book_files if n.startswith(f"{prefix}simulations/") and n.endswith('.html')])
        sim_js = sorted([n for n in book_files if n.startswith(f"{prefix}simulations/") and n.endswith('.js')])
        refs_exist = f"{prefix}REFERENCES.md" in names
        book_md_exist = f"{prefix}BOOK.md" in names
        
        print(f"=== {slug} ===")
        print(f"  Lessons count: {len(lessons)}")
        print(f"  Sim HTMLs: {len(sim_htmls)}, Sim JS: {len(sim_js)}")
        print(f"  REFERENCES.md: {refs_exist}, BOOK.md: {book_md_exist}")
        
        # Check simulation model title in model-01.html
        if sim_htmls:
            s1 = z.read(sim_htmls[0]).decode('utf-8', errors='ignore')
            t_m = re.search(r'<h1>(.*?)</h1>|<title>(.*?)</title>', s1)
            title = (t_m.group(1) or t_m.group(2) or "").strip()
            print(f"  Model 1 Title: {title}")
        print()
