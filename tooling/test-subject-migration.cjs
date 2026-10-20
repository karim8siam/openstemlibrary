/**
 * Dry-run relocation of a complete Calculus I textbook into the proposed
 * subject-based source structure. GitHub Actions performs this only inside
 * its disposable checkout; repository and live URLs remain untouched.
 */
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const cp=require('node:child_process');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const folder=path.join(root,'src','subjects','mathematics','calculus-2');
const original=fs.readdirSync(root).filter(n =>
  /^calculus-2(?:-chapter-\d+)?\.html$/.test(n) ||
  /^calculus-2-(?:data|sims)\.js$/.test(n)
);
assert(original.includes('calculus-2.html'),'Missing Calculus I index');
assert(original.some(n=>n.includes('-chapter-')),'Missing Calculus I chapters');
assert(original.includes('calculus-2-data.js'),'Missing book data');
assert(original.includes('calculus-2-sims.js'),'Missing simulation source');
assert(!fs.existsSync(folder),'Migration fixture collides with existing source folder');

const digest=file=>crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const build=()=>cp.execFileSync(process.execPath,[path.join(root,'tooling','prepare-static-site.cjs')],{cwd:root,encoding:'utf8'});
build();
const before=new Map(fs.readdirSync(path.join(root,'dist')).map(name=>
  [name,digest(path.join(root,'dist',name))]));
const moved=[];
try {
  fs.mkdirSync(folder,{recursive:true});
  for(const name of original) {
    fs.renameSync(path.join(root,name),path.join(folder,name));
    moved.push(name);
  }
  const info=JSON.parse(build());
  const after=new Map(fs.readdirSync(path.join(root,'dist')).map(name=>
    [name,digest(path.join(root,'dist',name))]));
  assert.equal(after.size,before.size,'Number of deploy assets changed during move');
  for(const [name,sha] of before)
    assert.equal(after.get(name),sha,'Public asset changed when moving source: '+name);
  assert.equal(info.preservedRoutes,true);
  console.log(JSON.stringify({
    dryRun:'passed',sourceFilesRelocated:moved.length,
    outputFilesCompared:after.size,canonicalRoutesChanged:0,
    expectedPublicUrl:'https://openstemlibrary.com/calculus-2'
  },null,2));
} finally {
  for(const name of moved) {
    if(fs.existsSync(path.join(folder,name)))
      fs.renameSync(path.join(folder,name),path.join(root,name));
  }
  fs.rmSync(folder,{recursive:true,force:true});
  for(const relative of ['src/subjects/mathematics','src/subjects','src']) {
    const dir=path.join(root,relative);
    if(fs.existsSync(dir) && fs.readdirSync(dir).length===0) fs.rmdirSync(dir);
  }
}
