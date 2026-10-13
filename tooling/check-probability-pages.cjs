const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),vm=require('node:vm');
const {JSDOM}=require(process.env.OPENSTEM_JSDOM_PATH||'jsdom'),root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8'),slug='probability-and-probability-distributions',draft='publishing/drafts/statistics-probability-probability-and-probability-distributions';
const ctx={window:{}};vm.createContext(ctx);vm.runInContext(read(slug+'-data.js'),ctx);const units=ctx.window.COURSE_DATA.units;
const sm=new JSDOM(read('sitemap.xml'),{contentType:'text/xml'}),urls=[...sm.window.document.querySelectorAll('loc')].map(e=>e.textContent),pages=[],titles=[];
for(let i=0;i<units.length;i++){
 const file=slug+(i?'-chapter-'+(i+1):'')+'.html',url='https://openstemlibrary.com/'+file.replace('.html',''),dom=new JSDOM(read(file),{runScripts:'outside-only'}),d=dom.window.document,w=dom.window;
 assert.equal(d.documentElement.lang,'en');assert.equal(d.querySelector('link[rel="canonical"]').href,url);assert.equal(d.querySelector('#unit-title').textContent,units[i].title);
 assert.equal(d.querySelectorAll('.textbook-section-card').length,units[i].sections.length);assert.equal(d.querySelectorAll('.problem-card').length,3);assert.equal(d.querySelectorAll('#unit-nav-list a').length,10);assert.equal(urls.filter(u=>u===url).length,1);
 assert.ok(d.title.includes(i?units[i].title:'Probability and Probability Distributions'));titles.push(d.title);
 assert.ok(d.querySelector('meta[name="description"]').content.length>60);assert.equal(d.querySelector('meta[property="og:title"]').content,d.title);assert.equal(d.querySelector('meta[name="twitter:title"]').content,d.title);
 assert.equal(d.querySelectorAll('.simulation-slot').length,units[i].simulations.length);const ids=[...d.querySelectorAll('[id]')].map(e=>e.id);assert.equal(new Set(ids).size,ids.length);
 for(const script of d.querySelectorAll('script[type="application/ld+json"]'))JSON.parse(script.textContent);
 assert.ok(d.querySelector('.stat-editorial-note').textContent.includes('has not received independent academic peer review'));
 // Compare every serialized content and solution element with freshly rendered source,
 // including sections after the worked questions in the manuscript.
 w.setTimeout=()=>0;w.scrollTo=()=>{};w.eval(read(slug+'-data.js'));w.eval(read('app.js').split('\nif (document.readyState === "loading")')[0].replace('// Initialize App','window.__qaFormat = formatMarkdownContent;\n  // Initialize App'));w.startApp();
 const probe=d.createElement('div');
 for(const source of ['The event is $P(90<X<115)$ and $P(X>120)$.','$$0<x<y<1$$','\\[\\begin{pmatrix}1&2\\\\3&4\\end{pmatrix}\\]','Inline \\(x<y\\) remains intact.']){
  probe.innerHTML=w.__qaFormat(source);
  assert.ok(probe.textContent.includes(source.includes('pmatrix')?'1&2':source.includes('90<X')?'P(90<X<115)':source.includes('0<x')?'0<x<y<1':'x<y'));
 }
 // Check each source mathematical token survives HTML serialization exactly.
 for(const content of [...units[i].sections.map(s=>s.content),...units[i].problems.flatMap(p=>[p.question,...p.steps.map(s=>s.explanation)])]){
  probe.innerHTML=w.__qaFormat(content);
  for(const m of content.matchAll(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$|\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)){
   const tex=(m[1]||m[2]||m[3]||m[4]).trim().replace(/\s+/g,' ');
   assert.ok(probe.textContent.replace(/\s+/g,' ').includes(tex),`Lost mathematical text in unit ${i+1}: ${tex}`);
  }
 }
 const sourceSections=[...d.querySelectorAll('.sec-content')].map(e=>e.textContent),sourceQuestions=[...d.querySelectorAll('.problem-question-box')].map(e=>e.textContent),sourceSolutions=[...d.querySelectorAll('.solution-content')].map(e=>e.textContent);
 const renderText=text=>{probe.innerHTML=w.__qaFormat(text);return probe.textContent;};assert.equal(JSON.stringify(sourceSections.map(s=>s.trim())),JSON.stringify(units[i].sections.map(s=>renderText(s.content).trim())));assert.equal(JSON.stringify(sourceQuestions.map(s=>s.trim())),JSON.stringify(units[i].problems.map(p=>renderText(p.question).trim())));for(let j=0;j<3;j++)for(const step of units[i].problems[j].steps)assert.ok(sourceSolutions[j].includes(renderText(step.explanation)));
 assert.ok(sourceSections.every(s=>s.trim().length>100));assert.ok(sourceSolutions.every(s=>s.trim().length>350));
 pages.push({unit:i+1,file,canonical:url,sections:units[i].sections.length,worked_questions:3,explorers:units[i].simulations.length,title:d.title});w.close();
}
assert.equal(new Set(titles).size,10);assert.equal(new Set(urls).size,urls.length);assert.ok(!urls.some(u=>u.includes('/publishing/')));
const home=new JSDOM(read('index.html'));assert.ok([...home.window.document.querySelectorAll('a')].some(a=>a.getAttribute('href')===slug));assert.ok(home.window.document.querySelector('a[href="#dept-statistics-probability"]'));
const report={status:'pass',pages,sitemap_urls:urls.length,checks:'Complete serialized prose and solutions match every source section/question/step; ten linked chapter URLs; three questions per unit; correct metadata, unique DOM IDs, valid structured data, explorer slots, sitemap uniqueness and catalog/homepage links.'};fs.writeFileSync(path.join(root,draft,'static-page-checks.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:'pass',chapters:10,sitemap_urls:urls.length}));home.window.close();sm.window.close();
