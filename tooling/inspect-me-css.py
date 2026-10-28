import zipfile

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    css_files = [n for n in z.namelist() if n.endswith('.css')]
    print(f"Total CSS files: {len(css_files)}")
    for c in css_files[:10]:
        print(c)
        content = z.read(c).decode('utf-8', errors='ignore')
        for l in content.splitlines()[:5]:
            print("  ", l)
