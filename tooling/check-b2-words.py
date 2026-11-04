import zipfile, re

ARCHIVE = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793784172679_25036646.zip"
b2_slugs = ["heat-transfer-in-processes", "mass-transfer", "separation-processes-i", "separation-processes-ii"]

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

with zipfile.ZipFile(ARCHIVE, "r") as z:
    for slug in b2_slugs:
        prefix = f"OpenSTEM-Chemical-Process-Engineering/books/{slug}/"
        files = [n for n in z.namelist() if n.startswith(prefix)]
        lessons = [n for n in files if "/lessons/" in n and n.endswith(".md")]
        labs = [n for n in files if "/labs/" in n and n.endswith(".md")]
        assessments = [n for n in files if "/assessments/" in n and n.endswith(".md")]
        worked = [n for n in files if "/worked-cases/" in n and n.endswith(".md")]
        projects = [n for n in files if "/projects/" in n and n.endswith(".md")]
        
        words_lessons = sum(prose_count(z.read(n).decode("utf-8")) for n in lessons)
        words_labs = sum(prose_count(z.read(n).decode("utf-8")) for n in labs)
        words_assess = sum(prose_count(z.read(n).decode("utf-8")) for n in assessments)
        words_worked = sum(prose_count(z.read(n).decode("utf-8")) for n in worked)
        words_projects = sum(prose_count(z.read(n).decode("utf-8")) for n in projects)
        total = words_lessons + words_labs + words_assess + words_worked + words_projects
        print(f"{slug}:")
        print(f"  lessons: {words_lessons}, labs: {words_labs}, assess: {words_assess}, worked: {words_worked}, proj: {words_projects} => TOTAL: {total}")
