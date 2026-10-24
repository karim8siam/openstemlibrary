/* Original OpenSTEM software-testing teaching models. Pure functions deliberately small,
   assumptions explicit, input bounded, all values finite. No network or user data. */
(function (root) {
  'use strict';
  const MODELS={
    'requirement-coverage': {title:'Requirements exercised', units:'percent', min:0,max:100,step:1, defaultValue:60, base:100,
      note:'Assumes 100 equally weighted requirements; exercising a requirement does not establish it passed.',
      calculate(x){return {covered:x,uncovered:100-x,percent:x};}},
    'oracle-precision': {title:'Oracle true positives',units:'percent',min:0,max:100,step:1,defaultValue:50,base:80,
      note:'Assumes 80 true-positive alerts and changes only false positives; alert precision is TP/(TP+FP).',
      calculate(x){return {truePositives:80,falsePositives:x,precision:100*80/(80+x)};}},
    'fixture-contamination': {title:'Shared fixture contamination risk',units:'percent',min:0,max:50,step:1,defaultValue:10,base:20,
      note:'Illustrative independent per-test contamination probability. Real shared-state failures are often correlated.',
      calculate(x){return {perTestRisk:x,clean20:100*Math.pow(1-x/100,20),contaminated20:100*(1-Math.pow(1-x/100,20))};}},
    'retry-probability': {title:'Independent retry success',units:'percent',min:0,max:100,step:1,defaultValue:70,base:3,
      note:'Assumes three independent attempts, an operation safe to retry, and fixed success chance per attempt.',
      calculate(x){return {perAttemptSuccess:x,successByAttempt3:100*(1-Math.pow(1-x/100,3)),failureAll3:100*Math.pow(1-x/100,3)};}},
    'journey-coverage': {title:'User journeys exercised',units:'journeys',min:0,max:24,step:1,defaultValue:6,base:24,
      note:'Assumes 24 listed risk scenarios; a covered scenario is not evidence that every execution path is correct.',
      calculate(x){return {scenarios:x,coveragePercent:100*x/24,remaining:24-x};}},
    'contrast-ratio': {title:'Foreground luminance',units:'relative luminance',min:0,max:1,step:0.01,defaultValue:0.18,base:1,
      note:'Compares sampled relative luminance against white background L=1; real accessibility also depends on text context.',
      calculate(x){return {foreground:x,background:1,contrast:(1.05)/(x+0.05),normalTextAA:(1.05)/(x+0.05)>=4.5};}},
    'boundary-cases': {title:'Inclusive upper score boundary',units:'score',min:1,max:100,step:1,defaultValue:80,base:0,
      note:'Shows six boundary-neighbor tests for integer range [0,U], with duplicates removed when U is small.',
      calculate(x){const v=[-1,0,1,x-1,x,x+1];return {upper:x,candidates:[...new Set(v)].sort((a,b)=>a-b),numberOfCases:new Set(v).size};}},
    'pairwise-targets': {title:'Values in third factor',units:'factor values',min:2,max:8,step:1,defaultValue:3,base:0,
      note:'Pairwise targets for factors of sizes 2, 3, and k; count sums across factor pairs, not minimum number of tests.',
      calculate(x){return {factorSizes:[2,3,x],allCombinations:6*x,pairTargets:6+2*x+3*x};}},
    'interval-transform': {title:'Input upper interval bound',units:'value',min:2,max:50,step:1,defaultValue:5,base:2,
      note:'Interval [2,U] transformed by y=3x+1, over mathematical integers without overflow.',
      calculate(x){return {input:[2,x],output:[7,3*x+1],safeBelow100:(3*x+1)<100};}},
    'transfer-invariant': {title:'Atomic transfer amount',units:'currency units',min:0,max:80,step:1,defaultValue:35,base:0,
      note:'Transfers amount from a source of 80 to destination of 20. Ignores fees and concurrent changes.',
      calculate(x){return {sourceAfter:80-x,destinationAfter:20+x,totalAfter:100};}},
    'bounded-progress': {title:'Processing completion step',units:'steps',min:0,max:30,step:1,defaultValue:7,base:10,
      note:'Toy bounded response: a durable submission must be recorded by step 10 under healthy-worker assumptions.',
      calculate(x){return {completedAt:x,deadlineSteps:10,meetsBound:x<=10,delayBeyondBound:Math.max(0,x-10)};}},
    'state-space': {title:'Number of independent clients',units:'clients',min:1,max:8,step:1,defaultValue:3,base:3,
      note:'Three possible local states per client; multiplies states without reducing unreachable or symmetric states.',
      calculate(x){return {clients:x,rawGlobalStates:Math.pow(3,x),rawTransitionsUpperBound:x*Math.pow(3,x)};}},
    'queue-overload': {title:'Arrival rate',units:'requests/s',min:0,max:250,step:1,defaultValue:160,base:120,
      note:'Idealized fixed service capacity 120 requests/s and a 30-second measurement interval. No finite buffer/drop modeling.',
      calculate(x){return {arrival:x,service:120,backlogAfter30s:30*Math.max(0,x-120),netDrainPerSecond:Math.max(0,120-x)};}},
    'redundant-availability': {title:'Independent replica failure chance',units:'percent',min:0,max:100,step:1,defaultValue:10,base:3,
      note:'Three independent replicas; shared network, power, software, and control-plane failures violate this assumption.',
      calculate(x){return {replicas:3,individualFailurePercent:x,anyReplicaAvailablePercent:100*(1-Math.pow(x/100,3))};}},
    'flakiness-rate': {title:'Failed reruns',units:'failures',min:0,max:50,step:1,defaultValue:3,base:50,
      note:'Empirical failure frequency from 50 runs; this is not a universal failure probability or a confidence bound.',
      calculate(x){return {failed:x,runs:50,observedFailurePercent:2*x,passed:50-x};}},
    'mutation-score': {title:'Killed non-equivalent mutants',units:'mutants',min:0,max:20,step:1,defaultValue:16,base:20,
      note:'Assumes 20 known non-equivalent, runnable mutants; equivalent and invalid mutants must be excluded separately.',
      calculate(x){return {killed:x,survivors:20-x,scorePercent:5*x};}}
  };
  function requireValid(name,value){let m=MODELS[name];if(!m) throw new Error('Unknown simulation '+name);if(!Number.isFinite(value)||value<m.min||value>m.max || Math.abs((value-m.min)/m.step-Math.round((value-m.min)/m.step))>1e-7) throw new RangeError('Value outside permitted bounds/step');return m;}
  function calculate(name,value){const m=requireValid(name,value);const out=m.calculate(value);for (const [k,v] of Object.entries(out)){if(typeof v==='number' && !Number.isFinite(v))throw new Error('Nonfinite result '+k);}return out;}
  function fmt(v){return typeof v==='number'?Number(v.toFixed(5)).toLocaleString('en-US'):Array.isArray(v)?v.join(', '):String(v)}
  function render(container, name){const m=MODELS[name]; if(!m)throw Error('Unknown model');container.innerHTML=''; const heading=document.createElement('h4');heading.textContent=m.title;
   const label=document.createElement('label');label.textContent='Adjust '+m.title+' ('+m.units+')';const input=document.createElement('input');input.type='range';input.min=m.min;input.max=m.max;input.step=m.step;input.value=m.defaultValue; input.setAttribute('aria-label',m.title);label.append(input);
   const value=document.createElement('output');value.setAttribute('aria-live','polite');const result=document.createElement('dl');const note=document.createElement('p');note.textContent='Assumption: '+m.note;
   const reset=document.createElement('button');reset.type='button';reset.textContent='Reset simulation';reset.addEventListener('click',()=>{input.value=m.defaultValue;update()});
   function update(){const x=Number(input.value);value.textContent='Current input: '+fmt(x);result.innerHTML='';Object.entries(calculate(name,x)).forEach(([key,v])=>{const dt=document.createElement('dt');const dd=document.createElement('dd');dt.textContent=key.replace(/[A-Z]/g,c=>' '+c.toLowerCase());dd.textContent=fmt(v);result.append(dt,dd)});}
   input.addEventListener('input',update);container.append(heading,label,value,result,note,reset);update();return {input,reset,value,result};
  }
  root.OpenSTEMTestingSims={MODELS,calculate,render};
  if (typeof module!=='undefined' && module.exports)module.exports={MODELS,calculate};
})(typeof window!=='undefined'?window:globalThis);

/* SimulationEngine adapter for Software Testing and Verification */
(function(root){
  if (typeof document !== 'undefined') {
    var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
    root.SimulationEngine = root.SimulationEngine || {};
    root.SimulationEngine.initSimulation = function(containerId, simType) {
      var el = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
      if (root.OpenSTEMTestingSims && root.OpenSTEMTestingSims.MODELS && root.OpenSTEMTestingSims.MODELS[simType]) {
        return root.OpenSTEMTestingSims.render(el, simType);
      }
      if (typeof previous === 'function') {
        return previous.call(this, containerId, simType);
      }
    };
  }
})(typeof window !== 'undefined' ? window : globalThis);
