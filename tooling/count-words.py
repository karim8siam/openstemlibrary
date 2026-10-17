import re
import os

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

tot = 0
for i in range(1, 9):
    p = f'publishing/drafts/statistics-probability-mathematical-statistics/unit-{i}.md'
    if os.path.exists(p):
        cnt = prose(open(p, encoding='utf-8').read())
        print(f'Unit {i}: {cnt} words')
        tot += cnt
print(f'Total: {tot} words')
