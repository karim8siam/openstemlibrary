import zipfile, re

ARCHIVE = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793784172679_25036646.zip"
b2_slugs = ["heat-transfer-in-processes", "mass-transfer", "separation-processes-i", "separation-processes-ii"]

with zipfile.ZipFile(ARCHIVE, "r") as z:
    for slug in b2_slugs:
        prefix = f"OpenSTEM-Chemical-Process-Engineering/books/{slug}/"
        unit_files = sorted([n for n in z.namelist() if n.startswith(prefix + "units/") and n.endswith(".md")])
        print(f"\n=== {slug} ({len(unit_files)} unit files) ===")
        for uf in unit_files:
            txt = z.read(uf).decode("utf-8")
            first_line = txt.splitlines()[0] if txt.splitlines() else "EMPTY"
            print(f"  {uf.split('/')[-1]}: {first_line}")
