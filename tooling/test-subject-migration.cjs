/**
 * Prevent unsafe source reorganizations from changing published HTML, JS or URLs.
 * Run after: node tooling/prepare-static-site.cjs
 *
 * Every available textbook must live in exactly one department/book folder.
 * Each deployed textbook file must have identical bytes to its source file.
 */
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const crypto=require('node:crypto');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const dist=path.join(root,'dist');
const groupedRoot=path.join(root,'src','subjects');
const ctx={window:{}};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root,'departments-data.js'),'utf8'),ctx,
  {filename:'departments-data.js',timeout:2000});
const departments=ctx.window.LIBRARY_CATALOG.departments;
const digest=file=>crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
let books=0,chapters=0,verifiedAssets=0;
const allNames=new Set();
const sourceFolders=new Set();

for(const dep of departments) {
 for(const book of dep.courses.filter(c=>c.status==='AVAILABLE')) {
  const stem=book.url.replace(/\.html$/,'');
  const folder=path.join(groupedRoot,dep.id,book.id);
  assert(fs.existsSync(folder),'Missing subject folder: '+dep.id+'/'+book.id);
  sourceFolders.add(path.relative(groupedRoot,folder));
  const entries=fs.readdirSync(folder).filter(n=>fs.statSync(path.join(folder,n)).isFile());
  assert(entries.includes(book.url),'Missing book entry: '+book.url);
  const chapterNames=entries.filter(n=>n.startsWith(stem+'-chapter-') && n.endsWith('.html'));
  assert(chapterNames.length>0,'Missing book chapters: '+book.id);
  assert(entries.includes(stem==='reader'?'course-data.js':stem+'-data.js'),
    'Missing textbook data: '+book.id);
  assert(entries.includes(stem==='reader'?'simulations.js':stem+'-sims.js'),
    'Missing simulation source: '+book.id);
  for(const name of entries){
    assert(!allNames.has(name),'Filename collision across books: '+name);
    allNames.add(name);
    assert(!fs.existsSync(path.join(root,name)),'Duplicate root-level public source: '+name);
    const published=path.join(dist,name);
    assert(fs.existsSync(published),'Missing published asset: '+name);
    assert.equal(digest(path.join(folder,name)),digest(published),
      'Deployed content has changed for: '+name);
    verifiedAssets++;
  }
  books++;
  chapters+=chapterNames.length+1;
 }
}
const expected=departments.reduce((n,d)=>n+d.courses.filter(c=>c.status==='AVAILABLE').length,0);
assert.equal(books,expected);
const otherSourceFolders=[];
for(const dept of fs.readdirSync(groupedRoot,{withFileTypes:true})){
 if(!dept.isDirectory())continue;
 for(const book of fs.readdirSync(path.join(groupedRoot,dept.name),{withFileTypes:true})){
  if(book.isDirectory()&&!sourceFolders.has(dept.name+'/'+book.name))
   otherSourceFolders.push(dept.name+'/'+book.name);
 }
}
assert.deepEqual(otherSourceFolders,[],'Unknown grouped folders outside catalog');
const sitemap=fs.readFileSync(path.join(dist,'sitemap.xml'),'utf8');
const sitemapUrls=[...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m=>m[1]);
assert.equal(sitemapUrls.length,new Set(sitemapUrls).size,'Duplicate sitemap URL');
for(const url of sitemapUrls){
 assert(url.startsWith('https://openstemlibrary.com/'),'Noncanonical sitemap URL: '+url);
 const slug=url.slice('https://openstemlibrary.com/'.length);
 assert(fs.existsSync(path.join(dist,slug?slug+'.html':'index.html')),
   'Broken sitemap target: '+url);
}
console.log(JSON.stringify({
  outcome:'passed',subjects:departments.map(d=>d.id),
  books,chapterPages:chapters,verifiedAcademicAssets:verifiedAssets,
  sitemapUrls:sitemapUrls.length,publicUrlChanges:0
},null,2));
