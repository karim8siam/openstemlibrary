// Read-only production audit. No requests modify the website.
// Usage: node tooling/audit-public-host.cjs [https://openstemlibrary.com]
// Generates browser-test-artifacts/live-site-audit.json.
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');

const base=(process.argv[2] || process.env.OPENSTEM_BASE_URL || 'https://openstemlibrary.com').replace(/\/$/, '');
assert(/^https:\/\/[a-z0-9.-]+$/i.test(base),'Supply a public HTTPS base URL');
const probes=[
  ['home','/',200],
  ['book','/reader',200],
  ['chapter','/reader-chapter-2',200],
  ['mathematics_book','/calculus-1',200],
  ['mathematics_chapter','/calculus-1-chapter-2',200],
  ['chemistry_book','/inorganic-chemistry-1',200],
  ['statistics_book','/statistical-estimation',200],
  ['physics_book','/mechanics',200],
  ['reader_css','/styles.css',200],
  ['reader_js','/app.js',200],
  ['robots','/robots.txt',200],
  ['sitemap','/sitemap.xml',200],
  ['publication_drafts','/publishing/README.md',404],
  ['internal_tooling','/tooling/README.md',404],
  ['missing_page','/__openstem_intentionally_missing_page__',404],
];

const publicResults={url:base,timestamp:new Date().toISOString(),tests:[],warnings:[],errors:[]};
async function get(url) {
  const controller=new AbortController();
  const timeout=setTimeout(()=>controller.abort(),14000);
  try {
    const res=await fetch(url,{redirect:'follow',signal:controller.signal,headers:{
      'User-Agent':'OpenSTEM-Release-Verification/1.0 (+https://openstemlibrary.com/)',
      'Accept':'text/html,text/plain,application/xml,*/*'
    }});
    const body=await res.text();
    return {status:res.status,finalUrl:res.url,body,contentType:res.headers.get('content-type')||'',
      server:res.headers.get('server')||'',cache:res.headers.get('cf-cache-status')||'',
      xRobotsTag:res.headers.get('x-robots-tag')||''};
  } finally {
    clearTimeout(timeout);
  }
}
(async()=>{
  const results=new Map();
  for (const [name,route,expected] of probes) {
    try {
      const result=await get(base+route);
      results.set(name,result);
      const info={name,route,status:result.status,expected,bytes:Buffer.byteLength(result.body),contentType:result.contentType,
        cache:result.cache,xRobotsTag:result.xRobotsTag,finalUrl:result.finalUrl};
      publicResults.tests.push(info);
      if(expected!==null && result.status!==expected)
        publicResults.errors.push(name+' expected HTTP '+expected+', got '+result.status);
      if((name==='publication_drafts'||name==='internal_tooling') && result.status===200) {
        publicResults.warnings.push(name+' public source files reachable (these should be excluded after dist cutover)');
        if (!result.xRobotsTag.toLowerCase().includes('noindex'))
          publicResults.warnings.push(name+' lacks an X-Robots-Tag noindex response header');
      }
    }catch(err){
      publicResults.tests.push({name,route,error:String(err)});
      if(expected!==null)publicResults.errors.push(name+' request failed: '+String(err));
    }
  }
  const home=results.get('home')?.body||'';
  const reader=results.get('book')?.body||'';
  const js=results.get('reader_js')?.body||'';
  const sitemap=results.get('sitemap')?.body||'';
  const robots=results.get('robots')?.body||'';
  if(reader && !reader.includes('https://openstemlibrary.com/reader'))
    publicResults.errors.push('Reader missing its expected canonical URL');
  // This is a reader-accessibility requirement, independent of Google indexing.
  // The page must be truthful even if users block JavaScript or have old caches.
  if(reader && reader.includes('In-Browser Protected'))
    publicResults.errors.push('Static reader still contains a misleading content-protection claim');
  if(reader && !reader.includes('Read freely · Cite responsibly'))
    publicResults.errors.push('Static reader missing its accessible reading notice');

  if(js && !js.includes('initReadingAppearance'))
    publicResults.errors.push('Production app.js does not contain the reader theme control; check deployment cache');
  if(sitemap && !sitemap.includes('https://openstemlibrary.com/reader'))
    publicResults.errors.push('Sitemap missing known textbook route');
  if(robots && !robots.includes('Sitemap: https://openstemlibrary.com/sitemap.xml'))
    publicResults.errors.push('robots.txt missing declared production sitemap');
  if(home && !home.includes('https://openstemlibrary.com/'))
    publicResults.warnings.push('Could not recognize production canonical in home HTML');
  const output=path.resolve(process.cwd(),'browser-test-artifacts');
  fs.mkdirSync(output,{recursive:true});
  fs.writeFileSync(path.join(output,'live-site-audit.json'),JSON.stringify(publicResults,null,2)+'\n');
  console.log(JSON.stringify(publicResults,null,2));
  process.exitCode=publicResults.errors.length?1:0;
})().catch(err=>{console.error(err);process.exitCode=1;});
