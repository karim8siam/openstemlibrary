import zipfile, re, json

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    for slug in ['engineering-mechanics', 'fluid-mechanics']:
        print(f"=== {slug} Extracted Models ===")
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/simulations/"
        sim_htmls = sorted([n for n in z.namelist() if n.startswith(prefix) and n.endswith('.html')])
        for h in sim_htmls[:2]:
            content = z.read(h).decode('utf-8', errors='ignore')
            title = re.search(r'<h1>(.*?)</h1>', content).group(1).strip()
            
            # Check for S JSON object (used in fluid-mechanics)
            s_m = re.search(r'const\s+S\s*=\s*(\{[\s\S]*?\});', content)
            if s_m:
                s_obj = json.loads(s_m.group(1))
                print(f"  {h.split('/')[-1]}: {title}")
                print(f"    S obj: {s_obj}")
            else:
                # Extract inputs
                inputs = re.findall(r'<input[^>]+id=[\"\']([^\"\']+)[\"\'][^>]*>', content)
                labels = re.findall(r'<label[^>]*>(.*?)</label>', content, re.DOTALL)
                clean_labels = [re.sub(r'<[^>]+>', '', l).strip() for l in labels]
                formula_m = re.search(r'const\s+model\s*=\s*\((.*?)\)\s*=>\s*([^;]+);|function\s+(?:evaluateModel|model|calc)\((.*?)\)\s*\{([\s\S]*?)\}', content)
                print(f"  {h.split('/')[-1]}: {title}")
                print(f"    Labels: {clean_labels}")
                if formula_m:
                    print(f"    Formula: {formula_m.group(0)[:80]}")
