import os, sys, json, re, glob

print("Fixing double backslashes for valid JSON...")

# Restore any git-tracked or replace in json files:
for jf in sorted(glob.glob("*.json")):
    with open(jf, "r", encoding="utf-8") as f:
        content = f.read()
    
    # If there is a single backslash before approx, alpha, angle, vec, varepsilon in JSON:
    # e.g. [^\\]\approx -> \\approx
    content = re.sub(r'(?<!\\)\\approx', r'\\\\approx', content)
    content = re.sub(r'(?<!\\)\\alpha', r'\\\\alpha', content)
    content = re.sub(r'(?<!\\)\\angle', r'\\\\angle', content)
    content = re.sub(r'(?<!\\)\\vec', r'\\\\vec', content)
    content = re.sub(r'(?<!\\)\\varepsilon', r'\\\\varepsilon', content)
    
    # Try parsing
    try:
        data = json.loads(content)
        with open(jf, "w", encoding="utf-8") as f:
            f.write(content)
        # print(f"Successfully validated {jf}")
    except Exception as e:
        print(f"Error in {jf}: {e}")

