import os
import sys
import json
import re

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

def check_draft_dir(draft_dir):
    tot = 0
    print(f"Checking draft directory: {draft_dir}")
    for i in range(1, 9):
        p = os.path.join(draft_dir, f"unit-{i}.md")
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                c = prose_count(f.read())
            print(f"  Unit {i}: {c} words")
            tot += c
        else:
            print(f"  Unit {i}: MISSING")
    print(f"Total draft words: {tot}")
    return tot

def check_data_js(data_js_path):
    tot = 0
    print(f"Checking data file: {data_js_path}")
    with open(data_js_path, encoding="utf-8") as f:
        text = f.read()
    idx = text.find("window.COURSE_DATA = ") + len("window.COURSE_DATA = ")
    data = json.loads(text[idx:].rstrip(";\n"))
    for i, u in enumerate(data.get("units", [])):
        w = sum(prose_count(s.get("content", "")) for s in u.get("sections", []))
        for p in u.get("problems", []):
            w += prose_count(p.get("question", ""))
            for step in p.get("steps", []):
                w += prose_count(step.get("explanation", ""))
        print(f"  Unit {i+1}: {w} words")
        tot += w
    print(f"Total data.js words: {tot}")
    return tot

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check-book-prose.py <draft_dir_or_data_js>")
        sys.exit(1)
    target = sys.argv[1]
    if os.path.isdir(target):
        check_draft_dir(target)
    elif target.endswith(".js"):
        check_data_js(target)
    else:
        print(f"Unknown target: {target}")
