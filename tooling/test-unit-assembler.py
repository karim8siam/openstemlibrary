import zipfile, re, json

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    slug = 'engineering-mechanics'
    prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/lessons/"
    u1_lessons = sorted([n for n in z.namelist() if n.startswith(f"{prefix}U01-L") and n.endswith('.md')])
    
    sections = []
    problems = []
    
    for l_idx, lf in enumerate(u1_lessons):
        content = z.read(lf).decode('utf-8', errors='ignore')
        lines = content.splitlines()
        
        # Lesson title
        l_title = f"Lesson 1.{l_idx+1}"
        for line in lines:
            if line.startswith("# "):
                l_title = re.sub(r"^#\s*Unit\s+\d+.*[—\-]\s*", "", line).strip()
                break
                
        # Extract worked calculation / problem
        prob_match = re.search(r'##\s+(?:Worked|Guided|3\.\s+Worked)[^\n]*\n\n([\s\S]*?)(?=(?:##|\Z))', content)
        if prob_match:
            body = prob_match.group(1).strip()
            paras = [p.strip() for p in body.split("\n\n") if p.strip()]
            q_text = paras[0] if paras else f"Engineering mechanics calculation for {l_title}."
            steps = [{'explanation': p} for p in paras[1:]] if len(paras) > 1 else [{'explanation': body}]
            final_ans = paras[-1] if paras else "Derivation complete."
            problems.append({
                "id": f"EM-U1-P{l_idx+1}",
                "title": l_title,
                "question": q_text,
                "steps": steps,
                "finalAnswer": final_ans
            })
            
        sections.append({
            "secNumber": f"1.{l_idx+1}",
            "heading": l_title,
            "content": content,
            "simulations": []
        })
        
    print(f"Assembled Unit 1 for {slug}:")
    print(f"  Sections count: {len(sections)}")
    print(f"  Problems count: {len(problems)}")
    for p in problems:
        print(f"    {p['id']}: {p['title']}")
        print(f"      Q: {p['question'][:80]}...")
