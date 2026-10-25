/* Developmental Biology Interactive Simulation Suite */
"use strict";
const models=[{"unit": 1, "title": "Cell fate response threshold", "kind": "sigmoid", "xLabel": "Signal (relative units)", "yLabel": "Marker-positive probability", "aLabel": "Steepness of response", "a": 5, "aMin": 1, "aMax": 12, "bLabel": "Half-activation signal", "b": 0.5, "bMin": 0.1, "bMax": 0.9, "warning": "Illustrative logistic probability; not measured individual-cell fate."}, {"unit": 1, "title": "Cellular memory after signal withdrawal", "kind": "decay", "xLabel": "Time (hours)", "yLabel": "Remaining reporter activity", "aLabel": "Decay rate (per hour)", "a": 0.18, "aMin": 0.05, "aMax": 0.5, "bLabel": "Initial activity", "b": 1, "bMin": 0.2, "bMax": 1.0, "warning": "Single exponential reporter decay; does not prove commitment."}, {"unit": 2, "title": "Cleavage cell count", "kind": "cleavage", "xLabel": "Division round", "yLabel": "Ideal number of cells", "aLabel": "Division rounds", "a": 6, "aMin": 1, "aMax": 10, "bLabel": "Starting cells", "b": 1, "bMin": 1, "bMax": 4, "warning": "Synchronous binary division; no cell loss or delayed division."}, {"unit": 2, "title": "Blastomere volume during cleavage", "kind": "volume", "xLabel": "Division round", "yLabel": "Mean volume (arbitrary units)", "aLabel": "Division rounds", "a": 6, "aMin": 1, "aMax": 10, "bLabel": "Initial embryo volume", "b": 1, "bMin": 0.4, "bMax": 2, "warning": "Total cytoplasmic volume fixed and partitioned equally."}, {"unit": 3, "title": "Morphogen spatial profile", "kind": "gradient", "xLabel": "Distance (\u00b5m)", "yLabel": "Relative ligand signal", "aLabel": "Decay length (\u00b5m)", "a": 110, "aMin": 30, "aMax": 240, "bLabel": "Source amplitude", "b": 1, "bMin": 0.2, "bMax": 1.5, "warning": "Assumed static exponential diffusion-loss profile."}, {"unit": 3, "title": "Segmentation clock and formed length", "kind": "segments", "xLabel": "Time (minutes)", "yLabel": "Estimated segmented length (\u00b5m)", "aLabel": "Clock period (minutes)", "a": 22, "aMin": 10, "aMax": 60, "bLabel": "Front speed (\u00b5m/min)", "b": 1.0, "bMin": 0.2, "bMax": 2.0, "warning": "Simplified constant speed and period without oscillator coupling."}, {"unit": 4, "title": "Neural-plate closure proxy", "kind": "closure", "xLabel": "Time (relative)", "yLabel": "Gap remaining (\u00b5m)", "aLabel": "Closure rate", "a": 0.45, "aMin": 0.1, "aMax": 0.8, "bLabel": "Initial gap (\u00b5m)", "b": 220, "bMin": 100, "bMax": 400, "warning": "Monotonic geometric proxy; not a biomechanical or clinical closure predictor."}, {"unit": 4, "title": "Branching organ tip growth", "kind": "branch", "xLabel": "Time (days)", "yLabel": "Predicted tip count", "aLabel": "Branch emergence rate", "a": 0.3, "aMin": 0.1, "aMax": 0.7, "bLabel": "Initial tips", "b": 2, "bMin": 1, "bMax": 6, "warning": "Continuous average approximation, not discrete branching anatomy."}, {"unit": 5, "title": "Directed cell-migration tracks", "kind": "migration", "xLabel": "Time (minutes)", "yLabel": "Net directed distance (\u00b5m)", "aLabel": "Speed (\u00b5m/min)", "a": 8, "aMin": 1, "aMax": 18, "bLabel": "Directional persistence", "b": 0.7, "bMin": 0.1, "bMax": 1.0, "warning": "Average net movement assumes persistent direction; not true stochastic trajectories."}, {"unit": 5, "title": "Tissue growth and cell loss", "kind": "balance", "xLabel": "Time (hours)", "yLabel": "Net cell count", "aLabel": "Proliferation rate (per hour)", "a": 0.12, "aMin": 0.01, "aMax": 0.3, "bLabel": "Loss rate (per hour)", "b": 0.06, "bMin": 0.01, "bMax": 0.3, "warning": "Exponential mean-field net growth, ignoring carrying capacity and geometry."}, {"unit": 6, "title": "Cooperative enhancer response", "kind": "hill", "xLabel": "Signal dose", "yLabel": "Normalized gene output", "aLabel": "Hill coefficient", "a": 3, "aMin": 1, "aMax": 6, "bLabel": "Half-activation K", "b": 4, "bMin": 1, "bMax": 8, "warning": "Phenomenological Hill curve: switch-like is not equivalent to bistable."}, {"unit": 6, "title": "Inhibitory feedback response", "kind": "feedback", "xLabel": "Signal dose", "yLabel": "Output under feedback", "aLabel": "Feedback strength", "a": 1.5, "aMin": 0.1, "aMax": 4, "bLabel": "Half-activation K", "b": 4, "bMin": 1, "bMax": 8, "warning": "Toy inhibitory feedback relation, not a fitted regulatory network."}, {"unit": 7, "title": "Regeneration growth ceiling", "kind": "regrowth", "xLabel": "Time (weeks)", "yLabel": "Recovered size fraction", "aLabel": "Recovery rate (per week)", "a": 0.35, "aMin": 0.05, "aMax": 0.8, "bLabel": "Maximum recovered fraction", "b": 0.9, "bMin": 0.3, "bMax": 1, "warning": "Size recovery alone is not functional anatomical regeneration."}, {"unit": 7, "title": "Plant phyllotactic divergence", "kind": "phyllo", "xLabel": "Primordium index", "yLabel": "Cumulative orientation (degrees)", "aLabel": "Divergence angle (degrees)", "a": 137.5, "aMin": 120, "aMax": 155, "bLabel": "Number of primordia", "b": 12, "bMin": 5, "bMax": 20, "warning": "Geometric layout only; no auxin transport or developmental dynamics."}, {"unit": 8, "title": "Sparse-lineage labeling", "kind": "label", "xLabel": "Eligible cells", "yLabel": "Expected labeled cells", "aLabel": "Label probability", "a": 0.08, "aMin": 0.01, "aMax": 0.4, "bLabel": "Clone survival fraction", "b": 0.8, "bMin": 0.2, "bMax": 1, "warning": "Expectation without collision, unequal clone growth or lineage selection."}, {"unit": 8, "title": "Perturbation dose response", "kind": "dose", "xLabel": "Dose (relative)", "yLabel": "Phenotype fraction", "aLabel": "Sensitivity K", "a": 5, "aMin": 1, "aMax": 9, "bLabel": "Maximum observable fraction", "b": 0.85, "bMin": 0.3, "bMax": 1, "warning": "Hypothetical saturating response, not dose guidance for embryo experiments."}];
function evaluateModel(m,x,a,b){
 switch(m.kind){
 case 'sigmoid':return 1/(1+Math.exp(-a*(x-b)));
 case 'decay':return b*Math.exp(-a*x);
 case 'cleavage':return b*Math.pow(2,Math.floor(x*a/10));
 case 'volume':return b/Math.pow(2,Math.floor(x*a/10));
 case 'gradient':return b*Math.exp(-x/a);
 case 'segments':return Math.floor(x/a)*a*b;
 case 'closure':return b*Math.exp(-a*x/10);
 case 'branch':return b*Math.exp(a*x/10);
 case 'migration':return x*a*b;
 case 'balance':return 100*Math.exp((a-b)*x/12);
 case 'hill':return Math.pow(x,a)/(Math.pow(b,a)+Math.pow(x,a));
 case 'feedback':{let raw=x/(b+x);return raw/(1+a*raw)}
 case 'regrowth':return b*(1-Math.exp(-a*x/3));
 case 'phyllo':return ((Math.floor(x*b/20)*a)%360);
 case 'label':return x*a*b;
 case 'dose':return b*x/(a+x);
 default:return 0;
 }
}
function formatNum(v){return Number.isFinite(v)?v.toLocaleString('en-US',{maximumFractionDigits:3}):'–'}
function makeModel(index,container){
 const m=models[index];if(!m)return;
 const id='devmodel-'+index;
 container.innerHTML=`<div class="controls"><label for="${id}-a">${m.aLabel}: <output id="${id}-av">${m.a}</output><input id="${id}-a" type="range" min="${m.aMin}" max="${m.aMax}" value="${m.a}" step="${(m.aMax-m.aMin)>40?1:0.01}"></label><label for="${id}-b">${m.bLabel}: <output id="${id}-bv">${m.b}</output><input id="${id}-b" type="range" min="${m.bMin}" max="${m.bMax}" value="${m.b}" step="${(m.bMax-m.bMin)>40?1:0.01}"></label></div><svg class="graph" viewBox="0 0 400 190" role="img" aria-label="Interactive line chart: ${m.title}"><line x1="40" y1="10" x2="40" y2="155" stroke="#688c8c"/><line x1="40" y1="155" x2="387" y2="155" stroke="#688c8c"/><polyline class="plot" fill="none" stroke="#087f7d" stroke-width="3" stroke-linejoin="round"/><text x="52" y="18" font-size="10" fill="#446b6b">${m.yLabel}</text><text x="260" y="180" font-size="10" fill="#446b6b">${m.xLabel}</text></svg><div class="figure-summary" aria-live="polite" id="${id}-summary"></div>`;
 const aEl=container.querySelector('#'+id+'-a'),bEl=container.querySelector('#'+id+'-b');
 function update(){const a=+aEl.value,b=+bEl.value;aEl.previousElementSibling.textContent=formatNum(a);bEl.previousElementSibling.textContent=formatNum(b);
 const n=120, xMax=m.kind==='gradient'?500:m.kind==='segments'?180:m.kind==='phyllo'?20:m.kind==='cleavage'||m.kind==='volume'?10:m.kind==='hill'||m.kind==='feedback'||m.kind==='sigmoid'||m.kind==='dose'?10:25;
 const vals=Array.from({length:n+1},(_,i)=>evaluateModel(m,xMax*i/n,a,b));
 const envelope=[];for(const aa of [m.aMin,m.aMax])for(const bb of [m.bMin,m.bMax])for(let k=0;k<=n;k++)envelope.push(evaluateModel(m,xMax*k/n,aa,bb));
 const lo=Math.min(...envelope,0),hi=Math.max(...envelope,0),span=Math.max(1e-8,hi-lo);
 const pts=vals.map((y,i)=>(40+347*i/n).toFixed(2)+','+(150-130*(y-lo)/span).toFixed(2)).join(' ');
 container.querySelector('.plot').setAttribute('points',pts);
 const last=vals[vals.length-1];container.querySelector('#'+id+'-summary').textContent='End-of-range model output: '+formatNum(last)+' · domain 0–'+formatNum(xMax)+' · illustrative only';
 }
 aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
}
document.addEventListener('DOMContentLoaded',()=>document.querySelectorAll('[data-model]').forEach(el=>makeModel(Number(el.dataset.model),el)));



/* SimulationEngine adapter for Developmental Biology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof makeModel === 'function') {
      makeModel(0, host);
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

