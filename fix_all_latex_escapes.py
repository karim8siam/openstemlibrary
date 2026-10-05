import glob
import json
import re

def repair_latex_string(s):
    if not isinstance(s, str):
        return s
    
    # Formfeed (\x0c) -> \f...
    s = s.replace("\x0crac", "\\frac")
    
    # Backspace (\x08) -> \b...
    s = s.replace("\x08eta", "\\beta")
    s = s.replace("\x08ar", "\\bar")
    s = s.replace("\x08inom", "\\binom")
    s = s.replace("\x08egin", "\\begin")
    s = s.replace("\x08oldsymbol", "\\boldsymbol")
    s = s.replace("\x08f", "\\bf")
    s = s.replace("\x08mathbf", "\\mathbf")
    
    # Carriage return (\r) -> \r...
    s = s.replace("\right", "\\right")
    s = s.replace("\rho", "\\rho")
    s = s.replace("\rangle", "\\rangle")
    
    # Tab (\t) -> \t...
    s = s.replace("\text", "\\text")
    s = s.replace("\theta", "\\theta")
    s = s.replace("\times", "\\times")
    s = s.replace("\to", "\\to")
    s = s.replace("\tau", "\\tau")
    s = s.replace("\tilde", "\\tilde")
    s = s.replace("\tan", "\\tan")
    s = s.replace("\textbf", "\\textbf")
    s = s.replace("\textit", "\\textit")
    
    # Newline (\n) when immediately followed by LaTeX keywords
    s = re.sub(r"\n(nu|nabla|neq|neg|notin)([^a-zA-Z])", r"\\\1\2", s)
    s = re.sub(r"\n(nu|nabla|neq|neg|notin)$", r"\\\1", s)
    
    return s

def walk(o):
    if isinstance(o, str):
        return repair_latex_string(o)
    elif isinstance(o, list):
        return [walk(v) for v in o]
    elif isinstance(o, dict):
        return {k: walk(v) for k, v in o.items()}
    return o

# 1. Fix all JSON files
for fn in sorted(glob.glob("*.json")):
    try:
        with open(fn, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        continue
    
    repaired = walk(data)
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(repaired, f, indent=2)
    print(f"Fixed JSON: {fn}")

# 2. Fix all JS data files
for fn in sorted(glob.glob("*-data.js")):
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()
    content_repaired = repair_latex_string(content)
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content_repaired)
    print(f"Fixed JS: {fn}")

# 3. Fix all HTML files
for fn in sorted(glob.glob("*.html")):
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()
    content_repaired = repair_latex_string(content)
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content_repaired)
    print(f"Fixed HTML: {fn}")

print("\nALL FILES IN REPOSITORY FIXED!")
