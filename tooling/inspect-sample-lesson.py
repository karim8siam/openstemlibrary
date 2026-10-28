import zipfile

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    for slug in ['automotive-engineering', 'engineering-mechanics', 'heat-transfer']:
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/lessons/"
        names = [n for n in z.namelist() if n.startswith(prefix) and n.endswith('.md')]
        if names:
            print(f"=== {slug} -> {names[0].split('/')[-1]} ===")
            content = z.read(names[0]).decode('utf-8')
            for line in content.splitlines()[:35]:
                print(line)
            print("...\n")
