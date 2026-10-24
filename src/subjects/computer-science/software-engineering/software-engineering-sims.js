/* OpenSTEM Software Engineering: bounded teaching models.
   Each output is a hypothetical illustration, not an empirical estimate. */
(function(root){'use strict';
const SPEC={
 'se-u1-trace':{name:'Requirement evidence coverage',unit:1,unitLabel:'% of 20 requirements with evidence',note:'n is the number of requirements with implementation evidence out of a fixed illustrative total of 20. Coverage does not establish stakeholder validation.',fn:n=>5*n},
 'se-u1-gap':{name:'Unverified requirement count',unit:1,unitLabel:'remaining criteria',note:'Twenty assumed criteria minus n checked items. Severity is not weighted; an unresolved authorization requirement may block release.',fn:n=>20-n},
 'se-u2-pairs':{name:'Potential component connections',unit:2,unitLabel:'undirected component pairs',note:'Complete-graph upper bound n(n-1)/2. Real systems have sparse, directional, differently critical dependencies.',fn:n=>n*(n-1)/2},
 'se-u2-queue':{name:'Illustrative queue response time',unit:2,unitLabel:'seconds (mean system time)',note:'M/M/1 formula 1/(mu-lambda): assumed service rate mu=1/s; arrival rate lambda=n/20 per second, with 2<=n<=16. Independent Poisson arrivals and exponential service times are hypothetical.',fn:n=>1/(1-n/20)},
 'se-u3-iteration':{name:'Iterations at fixed capacity',unit:3,unitLabel:'iterations',note:'n equal-sized independent tasks, exactly three tasks delivered per iteration, no blockers or review constraints.',fn:n=>Math.ceil(n/3)},
 'se-u3-review':{name:'Review queue beyond capacity',unit:3,unitLabel:'patches awaiting review',note:'Assume exactly 8 patches can be reviewed during a period and n arrive; queue starts empty and all reviews cost the same.',fn:n=>Math.max(0,n-8)},
 'se-u4-messages':{name:'Potential directed interface links',unit:4,unitLabel:'directed interactions',note:'Complete directed graph with n components and no self-edges: n(n-1). Real API relationships are not complete graphs.',fn:n=>n*(n-1)},
 'se-u4-docage':{name:'Documentation review interval',unit:4,unitLabel:'days between reviews',note:'Hypothetical once per week times n weeks. Longer intervals can increase risk, but content freshness depends on actual changes.',fn:n=>7*n},
 'se-u5-escape':{name:'Toy defect escape model',unit:5,unitLabel:'% hypothetical undetected',note:'Assume independent stages, each with a constant 30% detection probability; correlations and varying defect classes invalidate literal production predictions.',fn:n=>100*Math.pow(0.7,n)},
 'se-u5-ci':{name:'Serial CI test duration',unit:5,unitLabel:'minutes',note:'Fixed setup 8 minutes and n serial test groups requiring exactly 3 minutes each; ignores caching and parallel stages.',fn:n=>8+3*n},
 'se-u6-change':{name:'Illustrative coupling change cost',unit:6,unitLabel:'toy maintenance points',note:'Pure quadratic sensitivity n²; these are invented points and must never be read as actual engineer-hours or currency.',fn:n=>n*n},
 'se-u6-batches':{name:'Migration batches',unit:6,unitLabel:'batches',note:'Assume n independent records and a safe capacity of exactly 4 records per batch; real migrations require concurrency and reconciliation.',fn:n=>Math.ceil(n/4)},
 'se-u7-pert':{name:'Three-point duration heuristic',unit:7,unitLabel:'days',note:'PERT mean (a+4m+b)/6 using optimistic a=2 days, most likely m=n days, pessimistic b=3n days. It is not a guaranteed deadline.',fn:n=>(2+7*n)/6},
 'se-u7-recovery':{name:'Synthetic recovery-duration estimate',unit:7,unitLabel:'minutes',note:'Assume fixed five-minute verification and two minutes per affected deployment slice. No relation to any measured rollback.',fn:n=>5+2*n},
 'se-u8-energy':{name:'Toy test-run electricity usage',unit:8,unitLabel:'kWh',note:'Exactly 0.05 kWh per test-run is assumed for demonstration; no hardware measurements, emissions, or lifecycle boundaries.',fn:n=>0.05*n},
 'se-u8-retention':{name:'Rolling event volume',unit:8,unitLabel:'stored events',note:'Assume a constant 1,000 events/day retained for n complete days; does not establish any legal right or requirement to retain data.',fn:n=>1000*n}
};
function calculate(type,n){
 if(!Object.prototype.hasOwnProperty.call(SPEC,type))throw new RangeError('Unknown model');
 if(!Number.isInteger(n)||n<2||n>16)throw new RangeError('Input n must be integer in 2..16');
 const spec=SPEC[type];const value=spec.fn(n);if(!Number.isFinite(value))throw new Error('Non-finite output');
 return {model:type,n,value,name:spec.name,unit:spec.unit,unitLabel:spec.unitLabel,notes:spec.note};
}
function initSimulation(elementId,type){
 if(typeof document==='undefined')return false;
 const el=document.getElementById(elementId);if(!el||!Object.prototype.hasOwnProperty.call(SPEC,type))return false;
 el.replaceChildren();
 const title=document.createElement('h4');title.textContent=SPEC[type].name;
 const label=document.createElement('label');label.textContent='Explore integer input n (2 to 16): ';
 const slider=document.createElement('input');slider.type='range';slider.min='2';slider.max='16';slider.step='1';slider.value='6';slider.setAttribute('aria-label','Model input n for '+SPEC[type].name);
 label.append(slider);const value=document.createElement('output');value.setAttribute('role','status');value.setAttribute('aria-live','polite');value.style.display='block';value.style.margin='0.5rem 0';value.style.fontWeight='650';
 const note=document.createElement('p');const reset=document.createElement('button');reset.type='button';reset.textContent='Reset simulation';reset.setAttribute('aria-label','Reset '+SPEC[type].name);
 const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('viewBox','0 0 360 150');svg.setAttribute('role','img');svg.setAttribute('aria-label','Bar chart of simulated output across input values 2 to 16; numeric output is also shown above');svg.style.maxWidth='100%';svg.style.width='520px';
 const render=()=>{const n=Number(slider.value),r=calculate(type,n);value.textContent='Input n = '+n+'; output '+Number(r.value.toPrecision(8))+' '+r.unitLabel;note.textContent='Model assumptions and limitations: '+r.notes;
  while(svg.firstChild)svg.removeChild(svg.firstChild);
  const points=Array.from({length:15},(_,i)=>calculate(type,i+2));const max=Math.max(...points.map(p=>Math.abs(p.value)),1e-9);
  points.forEach((p,i)=>{const b=document.createElementNS('http://www.w3.org/2000/svg','rect');b.setAttribute('x',String(7+i*23));b.setAttribute('y',String(136-110*Math.abs(p.value)/max));b.setAttribute('height',String(110*Math.abs(p.value)/max));b.setAttribute('width','17');b.setAttribute('rx','2');b.setAttribute('fill',p.n===n?'#e8a13c':'#4288b5');const tip=document.createElementNS('http://www.w3.org/2000/svg','title');tip.textContent='Input '+p.n+', output '+Number(p.value.toPrecision(7));b.append(tip);svg.append(b);});
 };
 slider.addEventListener('input',render);reset.addEventListener('click',()=>{slider.value='6';render()});el.append(title,label,value,svg,note,reset);render();return true;
}
root.OpenSTEMModel={book:'software-engineering',calculate,types:Object.keys(SPEC),initSimulation};
root.SimulationEngine={...(root.SimulationEngine||{}),initSimulation};
})(typeof window==='undefined'?globalThis:window);
