const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const base=__dirname,api=require('./bayes-explorer.js');
const {JSDOM}=require(process.env.OPENSTEM_JSDOM_PATH||'jsdom');
let numeric=0,interactions=0;
function near(actual,expected,tolerance=1e-12){assert.ok(Math.abs(actual-expected)<=tolerance,`${actual} differs from ${expected}`);numeric++;}
const law=api.model([.2,.5,.3],[.08,.03,.01]);near(law.flagProbability,.034);law.posterior.forEach((x,i)=>near(x,[8/17,15/34,3/34][i]));
assert.equal(api.model([1,0,0],[0,1,1]).posterior,null);numeric++;
assert.deepEqual(api.model([1,0,0],[1,0,0]).posterior,[1,0,0]);numeric++;
for(const args of [[[.2,.5,.4],[.1,.2,.3]],[[NaN,.5,.5],[.1,.2,.3]],[[1,0,0],[-.1,0,0]],[[.2,.3,.5],[1.1,0,0]]]){assert.throws(()=>api.model(...args));numeric++;}
assert.throws(()=>api.sample([1,0,0],[1,0,0],0,1));assert.throws(()=>api.sample([1,0,0],[1,0,0],1,-1));numeric+=2;
const trials=api.sample([.2,.5,.3],[.08,.03,.01],100000,20261013);
assert.deepEqual(trials,api.sample([.2,.5,.3],[.08,.03,.01],100000,20261013));numeric++;
assert.equal(trials.sourceCounts.reduce((a,b)=>a+b),100000);numeric++;
near(trials.flagFrequency,.034,.002);
trials.posteriorFrequency.forEach((x,i)=>near(x,law.posterior[i],.025));
for(let i=0;i<3;i++){assert.ok(trials.flagCounts[i]<=trials.sourceCounts[i]);numeric++;}
const dom=new JSDOM('<body><div id="bayes-test"></div></body>',{runScripts:'outside-only'}),w=dom.window;
w.eval(fs.readFileSync(path.join(base,'bayes-explorer.js'),'utf8'));
const container=w.document.getElementById('bayes-test');w.ProbabilityBayes.mount(container);
const initial=container.querySelector('.prob-model-status').textContent;
for(const input of container.querySelectorAll('input')){assert.ok(w.document.querySelector(`label[for="${input.id}"]`));interactions++;}
assert.ok(container.querySelector('table caption'));assert.equal(container.querySelectorAll('tbody th[scope="row"]').length,3);interactions+=2;
assert.equal(container.querySelectorAll('[role="status"][aria-live="polite"]').length,2);interactions++;
container.querySelector('[data-draw]').click();assert.ok(container.querySelector('.prob-draw-status').textContent.includes('Generated 10000 trials'));interactions++;
const sampled=container.querySelector('.prob-draw-status').textContent;
container.querySelector('[data-draw]').click();assert.equal(container.querySelector('.prob-draw-status').textContent,sampled);interactions++;
container.querySelector('input').value='.8';container.querySelector('input').dispatchEvent(new w.Event('input'));assert.equal(container.querySelector('[data-draw]').disabled,true);interactions++;
container.querySelector('[data-reset]').click();assert.equal(container.querySelector('.prob-model-status').textContent,initial);assert.equal(container.querySelector('.prob-draw-status').textContent,'No random trials generated.');interactions+=2;
const rates=[...container.querySelectorAll('input')].slice(2);rates.forEach(x=>{x.value='0';x.dispatchEvent(new w.Event('input'));});
assert.ok(container.querySelector('.prob-model-status').textContent.includes('posterior is undefined'));container.querySelector('[data-draw]').click();assert.ok(container.querySelector('.prob-draw-status').textContent.includes('No sampled flags'));interactions+=2;
assert.ok(!/NaN|Infinity/.test(container.textContent));interactions++;
w.ProbabilityBayes.mount(container);assert.equal(container.querySelectorAll('[data-reset]').length,1);interactions++;
const report={status:'pass',model_sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(base,'bayes-explorer.js'))).digest('hex'),test_sha256:crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),scope:'Draft Bayes explorer numerical model, seeded sampling, DOM interactions and semantic accessibility only. Not a full rendered mobile-reader or live integration test.',numeric_checks:numeric,interaction_checks:interactions,default_seed:20261013,large_sample:trials,limitations:['Reader adapter not integrated yet.','Rendered mobile layout and keyboard workflow still require browser verification before publication.']};
fs.writeFileSync(path.join(base,'bayes-checks.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:report.status,numeric,interactions}));w.close();
