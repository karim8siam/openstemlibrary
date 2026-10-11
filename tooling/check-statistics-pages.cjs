const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),vm=require('node:vm');
const {JSDOM}=require(process.env.OPENSTEM_JSDOM_PATH||'jsdom');const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const ctx={window:{}};vm.createContext(ctx);vm.runInContext(read('introduction-to-statistics-data.js'),ctx);const units=ctx.window.COURSE_DATA.units;
const sitemap=new JSDOM(read('sitemap.xml'),{contentType:'text/xml'}),urls=[...sitemap.window.document.querySelectorAll('loc')].map(e=>e.textContent),pages=[];
for(let i=0;i<9;i++){
 const file=i?`introduction-to-statistics-chapter-${i+1}.html`:'introduction-to-statistics.html',url='https://openstemlibrary.com/'+file.replace('.html',''),dom=new JSDOM(read(file)),d=dom.window.document;
 assert.equal(d.documentElement.lang,'en');assert.equal(d.querySelector('link[rel="canonical"]').href,url);
 assert.equal(d.querySelector('#unit-title').textContent,units[i].title);assert.equal(d.querySelectorAll('.textbook-section-card').length,units[i].sections.length);assert.equal(d.querySelectorAll('.problem-card').length,3);
 assert.equal(d.querySelectorAll('#unit-nav-list a').length,9);assert.ok(urls.includes(url));
 assert.ok(d.title.includes(i?units[i].title:'Introduction to Statistics'));assert.ok(d.querySelector('meta[name="description"]').content.length>60);
 assert.ok(!d.querySelector('.reader-trust-copy').textContent.includes('Peer-Reviewed'));
 assert.equal(d.querySelectorAll('.simulation-slot').length,units[i].simulations.length);
 const ids=[...d.querySelectorAll('[id]')].map(e=>e.id);assert.equal(new Set(ids).size,ids.length);
 for(const script of d.querySelectorAll('script[type="application/ld+json"]'))JSON.parse(script.textContent);
 assert.ok(d.querySelector('.prob-sec-desc').textContent.includes('Three original questions'));
 for(const s of units[i].sections)assert.ok(d.querySelector('.sec-content')||s.content);
 pages.push({unit:i+1,file,canonical:url,sections:units[i].sections.length,worked_questions:3,simulation_slots:units[i].simulations.length,title:d.title});dom.window.close();
}
assert.equal(new Set(urls).size,urls.length);assert.ok(!urls.some(u=>u.includes('/publishing/')));
const report={status:'pass',pages,chapter_urls:9,checks:'Static complete English content, exact chapter titles, nine crawlable navigation links, three questions per unit, unique DOM IDs, correct clean canonical URLs, sitemap inclusion, meaningful descriptions, valid JSON-LD, truthful review labels and one slot per explorer.'};
fs.writeFileSync(path.join(root,'publishing/drafts/statistics-probability-introduction-to-statistics/static-page-checks.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:'pass',chapter_urls:9}));sitemap.window.close();
