import zipfile, re

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    names = z.namelist()
    books = sorted(list(set(n.split('/')[2] for n in names if len(n.split('/')) > 2 and n.split('/')[0] == 'OpenSTEM-Mechanical-Engineering' and n.split('/')[1] == 'books')))
    
    print("Auditing Simulations and Questions for 20 ME books:\n")
    
    for slug in books[:5]:
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/"
        sim_files = [n.replace(prefix, '') for n in names if n.startswith(f"{prefix}simulations/")]
        
        # Check a sample lesson for problems
        sample_lesson = [n for n in names if n.startswith(f"{prefix}lessons/U01-L01") and n.endswith('.md')]
        prob_found = []
        if sample_lesson:
            content = z.read(sample_lesson[0]).decode('utf-8')
            prob_matches = re.findall(r'(###\s+[^\n]*(?:example|problem|calculation|exercise|worked)[^\n]*)', content, re.IGNORECASE)
            h3s = [l for l in content.splitlines() if l.startswith('###')]
            prob_found = prob_matches or h3s
            
        print(f"=== {slug} ===")
        print(f"  Simulations: {len(sim_files)} files -> {[f for f in sim_files if f.endswith('.js') or f.endswith('.json')][:5]}")
        print(f"  Sample Lesson Headings (U01-L01): {len(prob_found)}")
        for h in prob_found[:6]:
            print(f"    {h}")
        print()
