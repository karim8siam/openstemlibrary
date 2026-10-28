import zipfile, re, os, json

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

def prose_count(text):
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', str(text or ''))
    text = re.sub(r'\$[^$\n]+\$', ' ', text)
    text = re.sub(r'```[\s\S]*?```', ' ', text)
    text = re.sub(r'`[^`\n]+`', ' ', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'^#+\s.*$', ' ', text, flags=re.MULTILINE)
    text = re.sub(r'^[-*+]\s+', ' ', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+\.\s+', ' ', text, flags=re.MULTILINE)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    words = re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", text)
    return len(words)

with zipfile.ZipFile(archive, 'r') as z:
    names = z.namelist()
    books = sorted(list(set(n.split('/')[2] for n in names if len(n.split('/')) > 2 and n.split('/')[0] == 'OpenSTEM-Mechanical-Engineering' and n.split('/')[1] == 'books')))
    
    print(f'Auditing {len(books)} Mechanical Engineering books:')
    total_words_all = 0
    all_pass = True
    
    results = []
    for slug in books:
        prefix = f'OpenSTEM-Mechanical-Engineering/books/{slug}/'
        unit_words = []
        for u in range(1, 9):
            path = f'{prefix}unit-{u:02d}.md'
            if path in names:
                cnt = prose_count(z.read(path).decode('utf-8'))
            else:
                cnt = 0
            unit_words.append(cnt)
        
        intro_cnt = prose_count(z.read(f'{prefix}INTRODUCTION.md').decode('utf-8')) if f'{prefix}INTRODUCTION.md' in names else 0
        app_cnt = prose_count(z.read(f'{prefix}METHODS-APPENDIX.md').decode('utf-8')) if f'{prefix}METHODS-APPENDIX.md' in names else 0
        refs_cnt = prose_count(z.read(f'{prefix}REFERENCES.md').decode('utf-8')) if f'{prefix}REFERENCES.md' in names else 0
        
        sum_u = sum(unit_words)
        grand = sum_u + intro_cnt + app_cnt + refs_cnt
        total_words_all += grand
        passed = sum_u >= 25000 or grand >= 25000
        if not passed: all_pass = False
        status_str = 'PASS' if passed else 'FAIL'
        results.append({
            'slug': slug,
            'sum_u': sum_u,
            'grand': grand,
            'passed': passed,
            'unit_words': unit_words
        })
        print(f'{slug:<50}: 8-Units={sum_u:>6} (Grand={grand:>6}) [{status_str}]')

    print(f'\nTotal words across all 20 books: {total_words_all:,}')
    print(f'All books pass 25,000-word gate: {all_pass}')
