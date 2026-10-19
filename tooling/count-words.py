import re
import os
import sys

def prose(text):
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
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

target_dir = sys.argv[1] if len(sys.argv) > 1 else 'publishing/drafts/statistics-probability-mathematical-statistics'

tot = 0
for i in range(1, 9):
    p = os.path.join(target_dir, f'unit-{i}.md')
    if os.path.exists(p):
        cnt = prose(open(p, encoding='utf-8').read())
        print(f'Unit {i}: {cnt} words ({os.path.getsize(p)} bytes)')
        tot += cnt
    else:
        print(f'Unit {i}: missing')
print(f'Total: {tot} words')

