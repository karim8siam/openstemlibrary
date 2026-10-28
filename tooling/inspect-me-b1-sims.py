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
        print(f"=== {slug} Simulations ===")
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/simulations/"
        sim_htmls = sorted([n for n in z.namelist() if n.startswith(prefix) and n.endswith('.html')])
        for h in sim_htmls[:4]:
            content = z.read(h).decode('utf-8', errors='ignore')
            m_title = re.search(r'<h1>(.*?)</h1>', content)
            t = m_title.group(1).strip() if m_title else h.split('/')[-1]
            
            # Look for formula or inputs
            formula = re.search(r'function\s+(?:formula|model|evaluateModel|calc)[^\{]*\{([\s\S]*?)\}', content)
            inputs = re.findall(r'<input[^>]+(?:id|name)=[\"\']([^\"\']+)[\"\'][^>]*>', content)
            s_obj = re.search(r'const\s+S\s*=\s*(\{[\s\S]*?\});', content)
            
            print(f"  {h.split('/')[-1]}: {t}")
            if s_obj:
                print(f"    S obj: {s_obj.group(1)[:120]}...")
            elif formula:
                print(f"    Formula: {formula.group(1).strip()[:100]}")
            print(f"    Inputs: {inputs[:4]}")
        print()
