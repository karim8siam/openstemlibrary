import zipfile, re, json

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    names = z.namelist()
    books = sorted(list(set(n.split('/')[2] for n in names if len(n.split('/')) > 2 and n.split('/')[0] == 'OpenSTEM-Mechanical-Engineering' and n.split('/')[1] == 'books')))
    
    print(f"Auditing simulations for {len(books)} books:\n")
    for slug in books:
        prefix = f"OpenSTEM-Mechanical-Engineering/books/{slug}/simulations/"
        sim_files = [n.replace(prefix, '') for n in names if n.startswith(prefix)]
        js_files = [f for f in sim_files if f.endswith('.js')]
        html_files = [f for f in sim_files if f.endswith('.html')]
        json_files = [f for f in sim_files if f.endswith('.json')]
        csv_files = [f for f in sim_files if f.endswith('.csv')]
        
        # Check if there is a main js file or models
        js_info = ""
        for j in js_files[:2]:
            content = z.read(f"{prefix}{j}").decode('utf-8', errors='ignore')
            js_info += f"{j}({len(content)}b) "
            
        print(f"{slug:<50}: total_sim_files={len(sim_files):<3} | js={len(js_files):<2} | html={len(html_files):<2} | json={len(json_files):<2} | {js_info}")
