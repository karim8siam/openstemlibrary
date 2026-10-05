import json, re

print("=== FIXING MATH, NEQ, AND PROBLEM STATEMENTS ===")

# 1. Fix amp_u5.json newline neq
with open("amp_u5.json", "r", encoding="utf-8") as f:
    u5_data = json.load(f)

for sec in u5_data.get("sections", []):
    c = sec.get("content", "")
    c = re.sub(r"\$S\s*\n\s*eq\s*0\$", r"$S \\neq 0$", c)
    c = re.sub(r"\$g_i\s*\n\s*eq\s*g_f\$", r"$g_i \\neq g_f$", c)
    sec["content"] = c

with open("amp_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5_data, f, indent=2)
print("Fixed amp_u5.json newline neq.")

# 2. Fix amp_u6.json newline neq
with open("amp_u6.json", "r", encoding="utf-8") as f:
    u6_data = json.load(f)

for sec in u6_data.get("sections", []):
    c = sec.get("content", "")
    c = re.sub(r"\\mu_\{el\}\s*\n\s*eq\s*0", r"\\mu_{el} \\neq 0", c)
    c = re.sub(r"\\partial\\mu/\\partial q\s*\n\s*eq\s*0", r"\\partial\\mu/\\partial q \\neq 0", c)
    c = re.sub(r"\\partial\\alpha/\\partial q\s*\n\s*eq\s*0", r"\\partial\\alpha/\\partial q \\neq 0", c)
    sec["content"] = c

with open("amp_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6_data, f, indent=2)
print("Fixed amp_u6.json newline neq.")

# 3. Fix dig_u5.json and dig_u7.json missing $$
with open("dig_u5.json", "r", encoding="utf-8") as f:
    u5_dig = json.load(f)

for sec in u5_dig.get("sections", []):
    c = sec.get("content", "")
    c = c.replace(
        '<div class="math-display">\n\\text{Initial State: } 1000_2 \\longrightarrow 0100_2 \\longrightarrow 0010_2 \\longrightarrow 0001_2 \\longrightarrow 1000_2\n</div>',
        '<div class="math-display">\n$$\\text{Initial State: } 1000_2 \\longrightarrow 0100_2 \\longrightarrow 0010_2 \\longrightarrow 0001_2 \\longrightarrow 1000_2$$\n</div>'
    )
    c = c.replace(
        '<div class="math-display">\n\\text{States: } 0000 \\to 1000 \\to 1100 \\to 1110 \\to 1111 \\to 0111 \\to 0011 \\to 0001 \\to 0000\n</div>',
        '<div class="math-display">\n$$\\text{States: } 0000 \\to 1000 \\to 1100 \\to 1110 \\to 1111 \\to 0111 \\to 0011 \\to 0001 \\to 0000$$\n</div>'
    )
    sec["content"] = c

with open("dig_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5_dig, f, indent=2)
print("Fixed dig_u5.json math-display delimiters.")

with open("dig_u7.json", "r", encoding="utf-8") as f:
    u7_dig = json.load(f)

for sec in u7_dig.get("sections", []):
    c = sec.get("content", "")
    c = re.sub(
        r'<div class="math-display">\n(\\text\{CPU Core Registers \}.*?)\n</div>',
        r'<div class="math-display">\n$$\1$$\n</div>',
        c
    )
    sec["content"] = c

with open("dig_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7_dig, f, indent=2)
print("Fixed dig_u7.json math-display delimiters.")

