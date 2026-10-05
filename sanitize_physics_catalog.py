import os, sys, json, re, glob

print("=== OPENSTEM PHYSICS CATALOG COMPREHENSIVE SANITIZER ===")

# 1. Clean control characters and escaped control chars in all JSON files
json_files = sorted(glob.glob("*.json"))

replacements = [
    (r"\\u0007pprox", r"\\approx"),
    (r"\x07pprox", r"\\approx"),
    (r"\\u0007lpha", r"\\alpha"),
    (r"\x07lpha", r"\\alpha"),
    (r"\\u0007ngle", r"\\angle"),
    (r"\x07ngle", r"\\angle"),
    (r"\\u000bec", r"\\vec"),
    (r"\x0bec", r"\\vec"),
    (r"\\u000barepsilon", r"\\varepsilon"),
    (r"\x0barepsilon", r"\\varepsilon"),
    (r"\\u0007", r""),
    (r"\x07", r""),
    (r"\\u000b", r""),
    (r"\x0b", r""),
]

for jf in json_files:
    with open(jf, "r", encoding="utf-8") as f:
        content = f.read()
    
    orig = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)
        
    if content != orig:
        with open(jf, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Sanitized control escapes in: {jf}")

print("Phase 1 complete: Control characters replaced in JSON files.")
