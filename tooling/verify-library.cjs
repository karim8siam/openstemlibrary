const fs=require('node:fs'), path=require('node:path'), vm=require('node:vm'), cp=require('node:child_process');
const {JSDOM}=require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');
const root=path.resolve(__dirname,'..'), read=f=>fs.readFileSync(path.join(root,f),'utf8');
const catalog={window:{}}; vm.createContext(catalog); vm.runInContext(read('departments-data.js'),catalog);
const books=catalog.window.LIBRARY_CATALOG.departments.flatMap(d=>d.courses.filter(c=>c.status==='AVAILABLE'));
const failures=[]; let chapters=0, problems=0; const sitemap=new JSDOM(read('sitemap.xml'),{contentType:'text/xml'});
const urls=new Set([...sitemap.window.document.querySelectorAll('loc')].map(n=>n.textContent)); sitemap.window.close();
async function verify() {
for(const book of books){
  const original=cp.execFileSync('git',['show','HEAD:'+book.url],{cwd:root,encoding:'utf8',maxBuffer:10e6});
  const old=new JSDOM(original), base=new JSDOM(read(book.url));
  for(const selector of ['#textbook-sections .sec-content','.problem-question-box','.solution-content']){
    const a=[...old.window.document.querySelectorAll(selector)].map(n=>n.textContent);
    const b=[...base.window.document.querySelectorAll(selector)].map(n=>n.textContent);
    if(JSON.stringify(a)!==JSON.stringify(b))failures.push('Changed original academic content: '+book.url+' '+selector);
  }
  const script=[...base.window.document.querySelectorAll('script[src]')].map(n=>n.getAttribute('src').split('?')[0]).find(p=>/(?:-data|course-data)\.js$/.test(p));
  const data={window:{}}; vm.createContext(data); vm.runInContext(read(script),data);
  old.window.close(); base.window.close();
  for(let i=0;i<data.window.COURSE_DATA.units.length;i++){
    const file=i===0?book.url:book.url.replace(/\.html$/,`-chapter-${i+1}.html`);
    if(!fs.existsSync(path.join(root,file))){failures.push('Missing page: '+file);continue;}
    const dom=new JSDOM(read(file)), d=dom.window.document, unit=data.window.COURSE_DATA.units[i]; chapters++;
    if(d.querySelector('link[rel="canonical"]')?.getAttribute('href')!=='https://openstemlibrary.com/'+file.replace(/\.html$/, ''))failures.push('Wrong canonical '+file);
    if(!urls.has('https://openstemlibrary.com/'+file.replace(/\.html$/, '')))failures.push('Missing sitemap entry '+file);
    if(i>0 && d.getElementById('unit-title')?.textContent!==unit.title)failures.push('Wrong heading '+file);
    if(i>0 && d.querySelectorAll('.textbook-section-card').length!==unit.sections.length)failures.push('Missing sections '+file);
    if(i>0 && d.querySelectorAll('.problem-card').length!==(unit.problems||[]).length)failures.push('Missing problems '+file);
    problems+=d.querySelectorAll('.problem-card').length;
    for(const el of d.querySelectorAll('a[href],script[src],link[href]')){
      const url=el.getAttribute('href')||el.getAttribute('src');
      if(!url||/^(https?:|mailto:|data:|#)/.test(url))continue;
      const local=url.split(/[?#]/)[0];
      if(local && !fs.existsSync(path.join(root,local)) && !fs.existsSync(path.join(root,local+'.html')))failures.push('Broken reference '+file+' -> '+local);
    }
    if(d.querySelectorAll('.unit-nav-link').length!==data.window.COURSE_DATA.units.length)failures.push('Missing navigation '+file);
    dom.window.close();
    await new Promise(setImmediate);
    if (global.gc) global.gc();
  }
}
if(cp.execFileSync('git',['diff','--name-only'],{cwd:root,encoding:'utf8'}).split('\n').some(p=>/(?:-data|course-data|-sims|simulations)\.js$/.test(p)))failures.push('Academic data or simulation source changed');
console.log(JSON.stringify({books:books.length,chapterPages:chapters,workedProblems:problems,failures},null,2));
process.exit(failures.length?1:0);
}
verify().catch(err=>{console.error(err);process.exit(1)});
