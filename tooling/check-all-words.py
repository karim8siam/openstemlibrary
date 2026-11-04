import zipfile, re

ARCHIVE = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793784172679_25036646.zip"

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
    "chemical-reaction-engineering-i", "chemical-reaction-engineering-ii",
    "process-dynamics-and-control", "process-simulation",
    "process-design", "process-safety",
    "biochemical-engineering", "polymer-process-engineering",
    "petroleum-and-petrochemical-processes"
]

with zipfile.ZipFile(ARCHIVE, "r") as z:
    for slug in slugs:
        prefix = f"OpenSTEM-Chemical-Process-Engineering/books/{slug}/"
        files = [n for n in z.namelist() if n.startswith(prefix)]
        md_files = [n for n in files if n.endswith(".md") and not n.endswith("README.md")]
        total = sum(prose_count(z.read(n).decode("utf-8")) for n in md_files)
        print(f"{slug}: {total} words in {len(md_files)} markdown files")
