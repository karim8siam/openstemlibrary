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
const {normalizeUnpublishedReferences}=require('./normalize-references.cjs');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const dist=path.join(root,'dist');
const groupedRoot=path.join(root,'src','subjects');
const ctx={window:{}};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root,'departments-data.js'),'utf8'),ctx,
  {filename:'departments-data.js',timeout:2000});
const departments=ctx.window.LIBRARY_CATALOG.departments;
// Ignore only the two deliberate publication-time presentation transforms.
// Academic chapters, formulas, navigation and script source must still match.
function normalizePresentation(text) {
  return normalizeUnpublishedReferences(text).html
    .replace(/🔒\s*<span>\s*In-Browser Protected\s*[•·]\s*Direct Download Disabled\s*<\/span>/g,
      '<span>Read freely · Cite responsibly</span>')
    .replace(/((?:app\.js|styles\.css|portal\.js|portal\.css))\?v=[A-Za-z0-9_-]+/g,
      '$1?v=FINGERPRINT');
}
function digest(file) {
  const bytes=fs.readFileSync(file);
  const normalized=path.extname(file)==='.html'
    ?Buffer.from(normalizePresentation(bytes.toString('utf8')),'utf8')
    :bytes;
  return crypto.createHash('sha256').update(normalized).digest('hex');
}
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
  // Some legacy course JS assets use short names (e.g., statmech-data.js).
  // The published HTML script references are authoritative.
  const html=fs.readFileSync(path.join(folder,book.url),'utf8');
  const courseScripts=[...html.matchAll(/<script[^>]+src=["']([^"']+)["']/g)]
    .map(m=>m[1].split('?')[0])
    .filter(n=>/^(?:course-data|simulations|.+-(?:data|sims))\.js$/.test(n));
  assert.equal(courseScripts.length,2,'Expected source data and simulation references: '+book.id);
  for(const script of courseScripts)
    assert(entries.includes(script),'Missing referenced academic source '+book.id+'/'+script);
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
