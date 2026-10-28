import zipfile, re, os

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
    
    print(f"{'Book Slug':<50} | {'Lessons':<7} | {'Units':<5} | {'Lessons Words':<13} | {'Book.md Words':<13} | {'Status'}")
    print("-" * 105)
    
    total_lesson_words = 0
    all_passed = True
    
    for slug in books:
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/"
        lesson_files = [n for n in names if n.startswith(f"{prefix}lessons/") and n.endswith('.md')]
        
        # calculate words by unit
        unit_words = {}
        for lf in lesson_files:
            fname = lf.split('/')[-1]
            u_match = re.search(r'U(\d+)', fname)
            u_num = int(u_match.group(1)) if u_match else 0
            text = z.read(lf).decode('utf-8')
            cnt = prose_count(text)
            unit_words[u_num] = unit_words.get(u_num, 0) + cnt
            
        sum_lessons = sum(unit_words.values())
        total_lesson_words += sum_lessons
        
        # Check BOOK.md if present
        book_md_words = 0
        if f"{prefix}BOOK.md" in names:
            book_md_words = prose_count(z.read(f"{prefix}BOOK.md").decode('utf-8'))
            
        best_words = max(sum_lessons, book_md_words)
        units_present = len([u for u in range(1, 9) if u in unit_words and unit_words[u] > 0])
        passed = best_words >= 25000 and units_present == 8
        if not passed: all_passed = False
        
        status = "PASS" if passed else f"FAIL ({best_words})"
        print(f"{slug:<50} | {len(lesson_files):<7} | {units_present:<5} | {sum_lessons:<13} | {book_md_words:<13} | {status}")

    print("-" * 105)
    print(f"Total lesson words across all 20 books: {total_lesson_words:,}")
    print(f"All 20 books meet >= 25,000 words & 8 units: {all_passed}")
