import zipfile, re

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

batch1_slugs = [
    'engineering-mechanics',
    'mechanics-of-solids',
    'engineering-thermodynamics',
    'fluid-mechanics',
    'manufacturing-processes'
]

prob_regexes = {
    'engineering-mechanics': r'##\s+Worked engineering illustration\n\n([\s\S]*?)(?=(?:##|\Z))',
    'mechanics-of-solids': r'##\s+Worked example and interpretation\n\n([\s\S]*?)(?=(?:##|\Z))',
    'engineering-thermodynamics': r'##\s+3\.\s+Worked teaching example\n\n([\s\S]*?)(?=(?:##|\Z))',
    'fluid-mechanics': r'###\s+Worked illustrative example\n\n([\s\S]*?)(?=(?:###|##|\Z))',
    'manufacturing-processes': r'##\s+Worked numerical screening calculation\n\n([\s\S]*?)(?=(?:##|\Z))'
}

with zipfile.ZipFile(archive, 'r') as z:
    for slug in batch1_slugs:
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/lessons/"
        names = sorted([n for n in z.namelist() if n.startswith(prefix) and n.endswith('.md')])
        pat = prob_regexes[slug]
        
        unit_counts = [0] * 8
        for lf in names:
            fname = lf.split('/')[-1]
            u_match = re.search(r'U(\d+)', fname)
            u_num = int(u_match.group(1)) if u_match else 0
            content = z.read(lf).decode('utf-8', errors='ignore')
            m = re.search(pat, content)
            if m:
                unit_counts[u_num - 1] += 1
            else:
                print(f"Warning: No match in {slug} {fname}")
                
        print(f"{slug:<35}: {unit_counts} -> sum = {sum(unit_counts)}")
