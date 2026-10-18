import glob

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

if 'href="linear-algebra.html"' not in idx_content:
    old_target = '<a href="calculus-3.html" class="footer-link">Calculus III</a>'
    new_target = '<a href="calculus-3.html" class="footer-link">Calculus III</a>\n      <a href="linear-algebra.html" class="footer-link">Linear Algebra</a>'
    if old_target in idx_content:
        idx_content = idx_content.replace(old_target, new_target)
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(idx_content)
        print("Updated index.html footer")

# 2. Update all reader HTML files
html_files = sorted(glob.glob("*.html"))
updated_count = 0

for hf in html_files:
    if hf in ["index.html", "linear-algebra.html"]:
        continue
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    
    if 'href="linear-algebra.html"' not in content:
        old_reader_target = '<a href="calculus-3.html" class="reader-trust-link">Calculus III</a>'
        new_reader_target = '<a href="calculus-3.html" class="reader-trust-link">Calculus III</a>\n              <a href="linear-algebra.html" class="reader-trust-link">Linear Algebra</a>'
        if old_reader_target in content:
            content = content.replace(old_reader_target, new_reader_target)
            with open(hf, "w", encoding="utf-8") as f:
                f.write(content)
            updated_count += 1
            print(f"Updated footer in: {hf}")
        else:
            print(f"Target not found in: {hf}")

print(f"Total reader files updated with Linear Algebra footer link: {updated_count}")
