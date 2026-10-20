/**
 * Search Console discovery + student navigation regression audit.
 * Checks real deployed HTML, NOT the GitHub folder layout.
 * Run after: node tooling/prepare-static-site.cjs
 *
 * Standard <a href="..."> links are the primary paths students and Googlebot
 * can follow. Sitemaps only supplement those navigational links.
 */
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const dist=path.join(root,'dist');
const sitemap=fs.readFileSync(path.join(dist,'sitemap.xml'),'utf8');
const site='https://openstemlibrary.com';
const urls=[...sitemap.matchAll(/<loc>\s*(https:\/\/openstemlibrary\.com\/[^<\s]+)\s*<\/loc>/g)].map(m=>m[1]);
const canonicals=new Set(urls);
assert(urls.length>100,'Expected full textbook library sitemap');
const inbound=new Map(urls.map(url=>[url,new Set()]));
const pageStats=[];
const absentTitles=[];
const unresolvableLinks=new Set();
const unresolvedTargets=new Map();
let internalLinks=0;
const linkPattern=/<a\b[^>]*\bhref\s*=\s*(?:"([^"]*)"|'([^']*)')[^>]*>/gi;
function normalizedURL(href,from) {
  const raw=href.replace(/&amp;/g,'&').trim();
  if(!raw||raw.startsWith('#')||/^(?:mailto:|tel:|javascript:|data:)/i.test(raw))return null;
  let dest;
  try {dest=new URL(raw,from);}catch{return null;}
  if(!['openstemlibrary.com','www.openstemlibrary.com'].includes(dest.hostname))return null;
  if(!['http:','https:'].includes(dest.protocol))return null;
  let route=dest.pathname.replace(/\/index(?:\.html)?$/,'/').replace(/\.html$/,'');
  if(route!=='/')route=route.replace(/\/$/,'');
  return site+route;
}
for(const url of urls) {
  const route=url.slice(site.length);
  const file=path.join(dist,route==='/'?'index.html':route.slice(1)+'.html');
  assert(fs.existsSync(file),'Missing published HTML: '+url);
  const html=fs.readFileSync(file,'utf8');
  const title=html.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1].trim()||'';
  if(!title)absentTitles.push(url);
  let matches,external=0,within=0,siblings=0;
  linkPattern.lastIndex=0;
  while((matches=linkPattern.exec(html))!==null) {
    const href=matches[1]||matches[2];
    if(!href||href.startsWith('#'))continue;
    const normalized=normalizedURL(href,url);
    if(!normalized){external++;continue;}
    within++;
    internalLinks++;
    if(canonicals.has(normalized)) {
      inbound.get(normalized).add(url);
      const stem=route.replace(/-chapter-\d+$/,'');
      if(stem!=='/'&&normalized.includes(stem))siblings++;
    } else {
      // Non-sitemap links could be legacy redirect routes or support pages.
      const candidate=normalized.slice(site.length);
      if(!fs.existsSync(path.join(dist,candidate==='/'?'index.html':candidate.slice(1)+'.html'))){
        unresolvedTargets.set(normalized,(unresolvedTargets.get(normalized)||0)+1);
        if(unresolvableLinks.size<60)unresolvableLinks.add(url+' → '+normalized);
      }
    }
  }
  pageStats.push({url,title,internalLinks:within,otherLinks:external,siblingLinks:siblings,bytes:Buffer.byteLength(html)});
}
const orphaned=urls.filter(url=>inbound.get(url).size===0);
const weak=urls.filter(url=>inbound.get(url).size===1);
const chapterOrphans=orphaned.filter(url=>/-chapter-\d+$/.test(url));
const chapters=urls.filter(url=>/-chapter-\d+$/.test(url));
const report={
  sitemapURLs:urls.length,chapterURLs:chapters.length,
  totalInternalAnchorLinks:internalLinks,
  noInboundFromSitemap:orphaned,
  chaptersWithNoInbound:chapterOrphans,
  pagesWithOnlyOneInbound:weak.length,
  missingTitles:absentTitles,
  unresolvedLinkOccurrences:[...unresolvedTargets.values()].reduce((sum,n)=>sum+n,0),
  unresolvedTargetCount:unresolvedTargets.size,
  unresolvedTargets:[...unresolvedTargets].sort((a,b)=>b[1]-a[1]).slice(0,60).map(([url,links])=>({url,links})),
  possibleBrokenInternalLinks:[...unresolvableLinks],
  sampledLowInbound:urls
    .map(url=>({url,inbound:inbound.get(url).size}))
    .filter(p=>p.url.includes('-chapter-')).sort((a,b)=>a.inbound-b.inbound)
    .slice(0,25)
};
fs.mkdirSync(path.join(root,'browser-test-artifacts'),{recursive:true});
fs.writeFileSync(path.join(root,'browser-test-artifacts','internal-link-coverage.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
if(chapterOrphans.length||absentTitles.length)process.exitCode=1;
