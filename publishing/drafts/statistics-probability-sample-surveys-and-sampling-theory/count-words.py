#!/usr/bin/env python3
import sys, re
from pathlib import Path

def prose(text):
    t = str(text or '')
    t = re.sub(r'```[\s\S]*?```', ' ', t)
    t = re.sub(r'<script\b[^>]*>[\s\S]*?</script>', ' ', t, flags=re.I)
    t = re.sub(r'<style\b[^>]*>[\s\S]*?</style>', ' ', t, flags=re.I)
    t = re.sub(r'\$\$[\s\S]*?\$\$', ' ', t)
    t = re.sub(r'\$[^$\n]+\$', ' ', t)
    t = re.sub(r'\\\[[\s\S]*?\\\]', ' ', t)
    t = re.sub(r'\\\(.*?\\\)', ' ', t)
    t = re.sub(r'<[^>]*>', ' ', t)
    t = re.sub(r'&[a-z0-9#]+;', ' ', t, flags=re.I)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    return t

def count(text):
    return len(re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", prose(text)))

if __name__ == '__main__':
    files = sys.argv[1:]
    if not files:
        draft_dir = Path(__file__).resolve().parent
        files = sorted(draft_dir.glob('unit-*.md'))
    total = 0
    for f in files:
        p = Path(f)
        if p.exists():
            c = count(p.read_text('utf-8'))
            print(f"{p.name}: {c} substantive words")
            total += c
    print(f"Total: {total} words")
