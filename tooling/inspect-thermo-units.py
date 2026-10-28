import zipfile, re

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    content = z.read("OpenSTEM-Mechanical-Engineering/books/engineering-thermodynamics/BOOK.md").decode('utf-8', errors='ignore')
    for line in content.splitlines():
        if re.match(r'^#+\s*Unit\s+\d+.*Lesson\s+1\b', line):
            print(line)
