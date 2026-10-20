// Read-only WCAG 2.1 A/AA accessibility scan against the locally built site.
// Diagnostics only; no user data is sent to external services.
'use strict';
const fs=require('node:fs');
const {chromium}=require('playwright');
const axePath=require.resolve('axe-core/axe.min.js');
const out='browser-test-artifacts';
fs.mkdirSync(out,{recursive:true});
(async()=>{
  const browser=await chromium.launch({headless:true});
  const audits=[];
  try{
   for(const file of ['index.html','reader.html','calculus-1.html','statistical-estimation.html']){
    for(const viewport of [{width:1440,height:900},{width:390,height:844}]){
     const page=await browser.newPage({viewport});
     await page.goto('http://127.0.0.1:8765/'+file,{waitUntil:'domcontentloaded'});
     await page.addScriptTag({path:axePath});
     const result=await page.evaluate(()=>window.axe.run(document,{
       runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}
     }));
     const issues=result.violations.map(x=>({
       rule:x.id,impact:x.impact,help:x.help,count:x.nodes.length,
       selectors:x.nodes.slice(0,6).map(n=>n.target.join(' '))
     }));
     audits.push({file,device:viewport.width<500?'mobile':'desktop',issues});
     console.log(JSON.stringify({page:file,device:viewport.width<500?'mobile':'desktop',issues}));
     await page.close();
    }
   }
  }finally{await browser.close();}
  fs.writeFileSync(out+'/accessibility-audit.json',JSON.stringify(audits,null,2));
  console.log('ACCESSIBILITY_AUDIT_TOTAL',JSON.stringify({
   screens:audits.length,
   critical:audits.reduce((n,x)=>n+x.issues.filter(i=>i.impact==='critical').length,0),
   serious:audits.reduce((n,x)=>n+x.issues.filter(i=>i.impact==='serious').length,0),
   distinctRules:[...new Set(audits.flatMap(x=>x.issues.map(i=>i.rule)))]
  }));
})().catch(e=>{console.error(e);process.exitCode=1;});