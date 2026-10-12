"""Verify actual public deployment against the saved textbook and sitemap."""
import hashlib,json,concurrent.futures,subprocess,xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
root=Path(__file__).resolve().parents[1]
base='https://openstemlibrary.com/'
class Page(HTMLParser):
    def __init__(self):super().__init__();self.sections=0;self.questions=0;self.canonical=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);classes=a.get('class','').split()
        if 'textbook-section-card' in classes:self.sections+=1
        if 'problem-card' in classes:self.questions+=1
        if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
def fetch(path):
    response=subprocess.run(['curl','-fsSL','--max-time','30','-w','\n__DEPLOYMENT_HTTP__%{http_code} %{url_effective}',base+path],capture_output=True,check=True)
    body,metadata=response.stdout.rsplit(b'\n__DEPLOYMENT_HTTP__',1)
    status,url=metadata.decode().split(' ',1)
    return path,int(status),url,body
paths=['introduction-to-statistics']+[f'introduction-to-statistics-chapter-{i}' for i in range(2,10)]+['introduction-to-statistics-data.js','introduction-to-statistics-sims.js','sitemap.xml','departments-data.js']
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(fetch,paths))
records=[]
for path,status,url,body in results:
    assert status==200,(path,status)
    if path.endswith('.js'):
        local=(root/path).read_bytes();assert hashlib.sha256(body).digest()==hashlib.sha256(local).digest(),(path,'deployed source differs')
        records.append(dict(path=path,status=status,sha256=hashlib.sha256(body).hexdigest()))
    elif path=='sitemap.xml':
        tree=ET.fromstring(body);locs=[e.text for e in tree.findall('.//{*}loc')]
        for p in paths[:9]:assert base+p in locs,(p,'not in live sitemap')
        assert not any('/publishing/' in u for u in locs)
        records.append(dict(path=path,status=status,new_book_urls=9))
    else:
        parser=Page();parser.feed(body.decode());assert parser.sections>=10,(path,'incomplete static sections');assert parser.questions==3,(path,parser.questions);assert parser.canonical==base+path,(path,parser.canonical)
        records.append(dict(path=path,status=status,url=url,sections=parser.sections,worked_questions=parser.questions,canonical=parser.canonical))
report=dict(status='pass',records=records,checks='Live HTTP 200, complete static chapters, three questions each, exact deployed data/simulation/catalog hashes and nine live sitemap URLs.')
(root/'publishing/drafts/statistics-probability-introduction-to-statistics/live-deployment.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'pass','verified_resources':len(records),'book_urls':9}))
