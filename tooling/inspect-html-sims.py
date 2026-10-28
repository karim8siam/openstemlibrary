import zipfile, re

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    for slug in ['engineering-mechanics', 'fluid-mechanics', 'heat-transfer']:
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/simulations/"
        html_files = [n for n in z.namelist() if n.startswith(prefix) and n.endswith('.html')]
        if html_files:
            print(f"=== {slug} -> {html_files[0].split('/')[-1]} ===")
            content = z.read(html_files[0]).decode('utf-8')
            scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', content)
            script_srcs = re.findall(r'<script[^>]+src=[\"\']([^\"\']+)[\"\']', content)
            print(f"  Script srcs: {script_srcs}")
            print(f"  Inline scripts: {len(scripts)}")
            for s in scripts:
                if s.strip():
                    print("  Inline script preview:")
                    for l in s.strip().splitlines()[:15]:
                        print("   ", l)
            print()
