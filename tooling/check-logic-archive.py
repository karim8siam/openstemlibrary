import zipfile, re, os, json

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793141595693_55b360e9.zip'

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

slugs = [
    'formal-logic',
    'model-theory-and-mathematical-semantics',
    'proof-theory-and-deductive-systems',
    'set-theory-and-foundations',
    'symbolic-and-predicate-logic'
]

with zipfile.ZipFile(archive, 'r') as z:
    for slug in slugs:
        prefix = f'OpenSTEM-Logic-and-Systems-Science/books/{slug}/'
        total_u = 0
        unit_words = []
        for u in range(1, 9):
            path = f'{prefix}unit-{u:02d}.md'
            content = z.read(path).decode('utf-8') if path in z.namelist() else ''
            cnt = prose_count(content)
            unit_words.append(cnt)
            total_u += cnt
        intro = prose_count(z.read(f'{prefix}INTRODUCTION.md').decode('utf-8')) if f'{prefix}INTRODUCTION.md' in z.namelist() else 0
        app = prose_count(z.read(f'{prefix}METHODS-APPENDIX.md').decode('utf-8')) if f'{prefix}METHODS-APPENDIX.md' in z.namelist() else 0
        refs = prose_count(z.read(f'{prefix}REFERENCES.md').decode('utf-8')) if f'{prefix}REFERENCES.md' in z.namelist() else 0
        print(f'{slug}:')
        print(f'  Units: {unit_words} -> sum = {total_u}')
        print(f'  Intro: {intro}, Appendix: {app}, Refs: {refs}')
        print(f'  Grand Total: {total_u + intro + app + refs}')
