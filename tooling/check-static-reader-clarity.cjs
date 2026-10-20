// Student-first production HTML checks, without a browser or network connection.
// Run after: node tooling/prepare-static-site.cjs
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const dist=path.join(root,'dist');
const fingerprint=name=>crypto.createHash('sha256').update(fs.readFileSync(path.join(root,name))).digest('hex').slice(0,12);
let inspected=0,readers=0,notices=0;
for(const file of fs.readdirSync(dist).filter(x=>x.endsWith('.html'))) {
  const html=fs.readFileSync(path.join(dist,file),'utf8');
  inspected++;
  assert(!html.includes('In-Browser Protected'),file+' still claims browser content is protected');
  assert(!html.includes('Direct Download Disabled'),file+' still claims downloads are blocked');
  assert(!/href=["']https:\/\/openstemlibrary\.com\/references\//.test(html),
    file+' still links to an unpublished reference page');
  if(!html.includes('protection-notice')) continue;
  readers++;
  assert(html.includes('Read freely · Cite responsibly'),file+' missing truthful reading notice');
  notices++;
  for (const asset of ['app.js','styles.css']) {
    assert(html.includes(asset+'?v='+fingerprint(asset)),file+' has stale '+asset+' browser cache key');
  }
}
assert(readers>=60,'Expected the existing textbook library to be included in this deploy');
assert.equal(readers,notices,'Every reader must show the static notice');
console.log(JSON.stringify({status:'passed',htmlFiles:inspected,readerPages:readers,
  trueReaderNotices:notices,staleProtectionClaims:0,fingerprintedResources:true},null,2));