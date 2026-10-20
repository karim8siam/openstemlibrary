/**
 * Non-destructive HTTP diagnostics for Search Console coverage investigations.
 * Samples canonical/duplicate URL variants; does not request Google reindexing.
 * Run: node tooling/audit-canonical-variants.cjs
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const https = require('node:https');

const canonicalBase = 'https://openstemlibrary.com';
const variants = [
  '/', '/index', '/index.html',
  '/reader', '/reader.html',
  '/reader-chapter-2', '/reader-chapter-2.html',
  '/calculus-1', '/calculus-1.html',
  '/calculus-1-chapter-2', '/calculus-1-chapter-2.html',
  '/statistical-estimation', '/statistical-estimation.html',
  '/inorganic-chemistry-1', '/inorganic-chemistry-1.html',
  '/sitemap.xml', '/robots.txt',
  '/__openstem_unpublished_example__'
];
const hostVariants = [
  'https://www.openstemlibrary.com/reader',
  'http://openstemlibrary.com/reader'
];
const urls = [...variants.map(x => canonicalBase + x), ...hostVariants];
const timeoutMs = 14000;

function get(url) {
  // Redirects are deliberately not followed to distinguish 200 duplicates
  // from a proper HTTP 301/308 consolidation.
  return new Promise(resolve => {
    const request = (url.startsWith('https:')? require('node:https'):require('node:http')).get(url, {
      timeout:timeoutMs,
      headers: {'Accept':'text/html,application/xml,text/plain;q=0.7','User-Agent':'OpenSTEM-SEO-Audit/1.0'}
    }, response => {
      const chunks=[];
      let bytes=0;
      response.on('data',chunk=>{
        if(bytes<300000)chunks.push(chunk);
        bytes+=chunk.length;
      });
      response.on('end',()=>{
        const html=Buffer.concat(chunks).toString('utf8');
        const canonicals=[...html.matchAll(/<link\b(?=[^>]*\brel=["']canonical["'])(?=[^>]*\bhref=["']([^"']+)["'])[^>]*>/gi)].map(x=>x[1]);
        const robots=[...html.matchAll(/<meta\b(?=[^>]*\bname=["']robots["'])(?=[^>]*\bcontent=["']([^"']+)["'])[^>]*>/gi)].map(x=>x[1]);
        resolve({
          url,status:response.statusCode,location:response.headers.location||null,
          canonical:canonicals,robots,xRobotsTag:response.headers['x-robots-tag']||null,
          contentType:response.headers['content-type']||null,
          bytes
        });
      });
    });
    request.on('timeout',()=>request.destroy(new Error('timeout')));
    request.on('error', e=>resolve({url,error:e.message}));
  });
}
(async()=>{
  const findings=[];
  for(const url of urls) findings.push(await get(url));
  const byURL=new Map(findings.map(x=>[x.url,x]));
  const problems=[];
  const warnings=[];
  for (const record of findings) {
    if(record.error) {
      warnings.push('Could not reach '+record.url+': '+record.error);
      continue;
    }
    const parsed=new URL(record.url);
    const pathname=parsed.pathname;
    const canonicalCandidate=canonicalBase+(pathname.endsWith('.html')?pathname.slice(0,-5):pathname);
    const isHtml=(record.contentType||'').includes('text/html');
    if(isHtml && record.status===200 && record.canonical.length!==1)
      problems.push('Missing/multiple canonical links: '+record.url);
    if(isHtml && record.status===200 && record.canonical.length===1 && record.canonical[0]!==canonicalCandidate && pathname!=='/index' && pathname!=='/index.html')
      warnings.push('Canonical differs from expected: '+record.url+' -> '+record.canonical[0]);
    if(pathname.endsWith('.html') && record.status===200)
      warnings.push('Duplicate HTML variant responds 200 (canonical only): '+record.url);
    if(record.status===200 && ((record.xRobotsTag||'').includes('noindex')||record.robots.some(r=>r.includes('noindex'))))
      problems.push('Published public page has noindex: '+record.url);
  }
  const report={checked:new Date().toISOString(),totalChecked:findings.length,problems,warnings,findings};
  fs.mkdirSync(path.join(process.cwd(),'browser-test-artifacts'),{recursive:true});
  fs.writeFileSync(path.join(process.cwd(),'browser-test-artifacts','canonical-variants.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
  if(problems.length)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});