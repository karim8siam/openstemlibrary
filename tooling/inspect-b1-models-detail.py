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
    for slug in batch1_slugs:
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/simulations/"
        sim_htmls = sorted([n for n in z.namelist() if n.startswith(prefix) and n.endswith('.html')])
        print(f"=== {slug} ({len(sim_htmls)} HTMLs) ===")
        for idx, h in enumerate(sim_htmls[:3]):
            content = z.read(h).decode('utf-8', errors='ignore')
            t_m = re.search(r'<h1>(.*?)</h1>', content)
            title = t_m.group(1).strip() if t_m else h
            
            # Check for inputs
            input_tags = re.findall(r'<input[^>]+>', content)
            print(f"  Model {idx+1}: {title}")
            for it in input_tags[:3]:
                print(f"    input: {it}")
