import zipfile, re

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    prefix = "OpenSTEM-Mechanical-Engineering/books/engineering-mechanics/simulations/"
    sim_htmls = sorted([n for n in z.namelist() if n.startswith(prefix) and n.endswith('.html')])
    for h in sim_htmls:
        content = z.read(h).decode('utf-8', errors='ignore')
        t = re.search(r'<h1>(.*?)</h1>', content).group(1).strip()
        script = re.search(r'<script[^>]*>([\s\S]*?)</script>', content).group(1).strip()
        # extract inputs
        labels = re.findall(r'<label[^>]*>(.*?)</label>', content, re.DOTALL)
        clean_labels = [re.sub(r'<[^>]+>', '', l).strip() for l in labels]
        print(f"{h.split('/')[-1]}: {t}")
        print(f"  Labels: {clean_labels}")
