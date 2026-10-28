import zipfile, os

archive = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

with zipfile.ZipFile(archive, 'r') as z:
    names = z.namelist()
    books = sorted(list(set(n.split('/')[2] for n in names if len(n.split('/')) > 2 and n.split('/')[0] == 'OpenSTEM-Mechanical-Engineering' and n.split('/')[1] == 'books')))
    
    for slug in books:
        book_files = [n for n in names if n.startswith(f'OpenSTEM-Mechanical-Engineering/books/{slug}/')]
        md_files = [n.split('/')[-1] for n in book_files if n.endswith('.md')]
        subdirs = set(n.split('/')[3] for n in book_files if len(n.split('/')) > 4)
        print(f'{slug}: total_files={len(book_files)}, md_files={len(md_files)}, subdirs={subdirs}')
        if len(md_files) < 10:
            print(f'   MDs: {md_files}')
