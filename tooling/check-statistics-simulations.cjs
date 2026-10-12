const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {JSDOM}=require(process.env.OPENSTEM_JSDOM_PATH||'jsdom');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const draft='publishing/drafts/statistics-probability-introduction-to-statistics/';
const dom=new JSDOM('<body></body>',{runScripts:'outside-only'}),w=dom.window;
w.eval(read('introduction-to-statistics-sims.js'));const math=w.StatisticsMath;
let numeric=0,interaction=0;
function near(a,b){assert.ok(Math.abs(a-b)<=1e-9*Math.max(1,Math.abs(b)),`${a} != ${b}`);numeric++;}
for(const fixture of JSON.parse(read(draft+'simulation-fixtures.json'))){const result=math.summary(fixture.values);for(const [key,value]of Object.entries(fixture.expected)){if(value===null)assert.equal(result[key],null);else near(result[key],value);}}
assert.equal(math.summary([]),null);assert.equal(math.summary([NaN]),null);assert.equal(math.quantile([1],2),null);
assert.equal(math.regression([1,2],[1]),null);assert.equal(math.regression([1,1],[2,3]).r,null);assert.equal(math.regression([1,1],[2,3]).slope,null);
const r=math.regression([1,2,3,4],[2,3,5,4]);for(const [key,value]of Object.entries({slope:.8,intercept:1.5,sse:1.8,ssr:3.2,syy:5,r:.8,rSquared:.64}))near(r[key],value);
near(r.residuals.reduce((a,b)=>a+b,0),0);near(r.residuals.reduce((a,b,i)=>a+(i+1)*b,0),0);
near(math.regression([-2,-1,0,1,2],[4,1,0,1,4]).r,0);
assert.equal(math.summary([3,3]).skewness,null);assert.equal(math.summary([3,3]).rawKurtosis,null);
assert.equal(math.sample(13,1,42),null);assert.equal(math.sample(2,0,42),null);near(math.mean(math.population),10);
for(let seed=1;seed<=100;seed++){const s=math.sample(5,4,seed);assert.equal(new Set(s.map(v=>v.i)).size,5);assert.equal(s.length,5);}
near(math.mean(math.sample(12,10,42).map(v=>v.v)),10);
const types=['stat-sampling','stat-histogram','stat-boxplot','stat-location','stat-variation','stat-shape','stat-association','stat-regression'];
for(const type of types){
 const el=w.document.createElement('div');el.id='sim-container-'+type;w.document.body.append(el);w.SimulationEngine.initSimulation(el.id,type);
 const initial=el.querySelector('.stat-results').textContent;
 assert.ok(el.querySelector('svg[role="img"][aria-label]'));assert.ok(el.querySelector('.stat-results[aria-live="polite"]'));
 for(const input of el.querySelectorAll('input'))assert.ok(w.document.querySelector(`label[for="${input.id}"]`));
 const input=el.querySelector('input');input.value=input.max;input.dispatchEvent(new w.Event('input',{bubbles:true}));
 assert.notEqual(el.querySelector('.stat-results').textContent,initial);
 el.querySelector('[data-reset]').click();assert.equal(el.querySelector('.stat-results').textContent,initial);interaction+=3;
 if(type==='stat-shape'){input.value='3';input.dispatchEvent(new w.Event('input'));assert.ok(!el.querySelector('.stat-results').textContent.includes('Unavailable'));interaction++;}
 if(type==='stat-sampling'){
   el.querySelector('[data-draw]').click();assert.notEqual(el.querySelector('.stat-results').textContent,initial);interaction++;
   input.value='12';input.dispatchEvent(new w.Event('input'));const summary=el.querySelector('.stat-summary').textContent;assert.ok(summary.includes('Sample mean10'));interaction++;
 }
 assert.ok(!/NaN|Infinity|undefined/.test(el.querySelector('.stat-results').textContent));
 w.SimulationEngine.initSimulation(el.id,type);assert.equal(el.querySelectorAll('[data-reset]').length,1);
}
const report={status:'pass',numeric_comparisons:numeric,interaction_checks:interaction,explorers:types,checks:'Independent NumPy/SciPy fixtures, variance/shape degeneracy, constant-column regression, random sampling uniqueness, census equality, input updates, labelled controls, accessible numeric results, SVG labels and reset.'};
fs.writeFileSync(path.join(root,draft+'simulation-checks.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));w.close();
