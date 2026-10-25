/* Evolutionary Biology Interactive Simulation Suite */
"use strict";
const MODELS = [{"name": "Fossil sample detection", "alabel": "Preservation probability", "blabel": "Survey discovery probability", "amin": 0.05, "amax": 0.95, "astep": 0.05, "bmin": 0.05, "bmax": 0.95, "bstep": 0.05, "unit": "detected fraction", "expression": "a*b", "note": "Independent per-occurrence preservation and survey detection; not a date estimator."}, {"name": "Time interval between horizons", "alabel": "Older horizon (Ma)", "blabel": "Younger horizon (Ma)", "amin": 50, "amax": 500, "astep": 5, "bmin": 0, "bmax": 300, "bstep": 5, "unit": "million years", "expression": "Math.max(0,a-b)", "note": "Positive age gap only; values are synthetic geological ages."}, {"name": "Expected heterozygote count", "alabel": "Allele frequency p", "blabel": "Number of diploid individuals", "amin": 0, "amax": 1, "astep": 0.02, "bmin": 20, "bmax": 500, "bstep": 10, "unit": "expected heterozygotes", "expression": "2*a*(1-a)*b", "note": "Under ideal Hardy–Weinberg conditions; counts are expected values, not actual measured individuals."}, {"name": "Selection, haploid", "alabel": "Starting allele frequency", "blabel": "Relative fitness of focal type", "amin": 0.02, "amax": 0.98, "astep": 0.02, "bmin": 0.5, "bmax": 1.8, "bstep": 0.05, "unit": "next-generation p", "expression": "a*b/(a*b+(1-a))", "note": "Alternative type relative fitness fixed at 1; ignores sampling drift."}, {"name": "Plastic reaction slope", "alabel": "Trait difference", "blabel": "Environment difference", "amin": -25, "amax": 25, "astep": 1, "bmin": 1, "bmax": 20, "bstep": 1, "unit": "slope", "expression": "a/b", "note": "Assumes linearity only over observed interval."}, {"name": "Short-term response to selection", "alabel": "Heritability h²", "blabel": "Selection differential", "amin": 0, "amax": 1, "astep": 0.02, "bmin": -10, "bmax": 10, "bstep": 0.5, "unit": "response in trait units", "expression": "a*b", "note": "Breeder’s equation is a conditional, one-generation approximation."}, {"name": "Barrier-stage success", "alabel": "Encounter probability", "blabel": "Conditional fertilization probability", "amin": 0, "amax": 1, "astep": 0.02, "bmin": 0, "bmax": 1, "bstep": 0.02, "unit": "combined probability", "expression": "a*b", "note": "Ignores later viability, fertility and environmental effects."}, {"name": "Migration admixture", "alabel": "Local allele frequency", "blabel": "Migrant fraction", "amin": 0, "amax": 1, "astep": 0.02, "bmin": 0, "bmax": 1, "bstep": 0.02, "unit": "recipient p", "expression": "(1-b)*a+b*0.8", "note": "Source population frequency fixed at 0.8 for teaching."}, {"name": "Sequence clock", "alabel": "Two-lineage corrected distance", "blabel": "Rate per lineage per Myr", "amin": 0.001, "amax": 0.2, "astep": 0.005, "bmin": 0.001, "bmax": 0.01, "bstep": 0.001, "unit": "million years", "expression": "a/(2*b)", "note": "Strict equal-rate assumption; calibrated clock uncertainty omitted."}, {"name": "Character transition count", "alabel": "Gain events", "blabel": "Loss events", "amin": 0, "amax": 15, "astep": 1, "bmin": 0, "bmax": 15, "bstep": 1, "unit": "minimum changes", "expression": "a+b", "note": "Simple count on a fixed inferred tree; hidden changes not included."}, {"name": "Net diversification rate", "alabel": "Speciation rate", "blabel": "Extinction rate", "amin": 0, "amax": 0.5, "astep": 0.01, "bmin": 0, "bmax": 0.5, "bstep": 0.01, "unit": "net per lineage-time", "expression": "a-b", "note": "Constant-rate birth–death approximation, not a measured natural clade."}, {"name": "Sampling survival fraction", "alabel": "Lineages surviving", "blabel": "Lineages sampled before", "amin": 0, "amax": 50, "astep": 1, "bmin": 1, "bmax": 100, "bstep": 1, "unit": "percent surviving", "expression": "100*Math.min(a,b)/b", "note": "Assumes comparable taxonomic and preservation sampling."}, {"name": "Lifetime reproduction", "alabel": "Survival to early breeding", "blabel": "Early fecundity", "amin": 0, "amax": 1, "astep": 0.02, "bmin": 0, "bmax": 8, "bstep": 0.25, "unit": "expected early offspring", "expression": "a*b", "note": "One age contribution to R0, not annual growth rate."}, {"name": "Hamilton inequality score", "alabel": "Relatedness", "blabel": "Recipient benefit", "amin": 0, "amax": 1, "astep": 0.02, "bmin": 0, "bmax": 10, "bstep": 0.5, "unit": "rb-c", "expression": "a*b-1", "note": "Actor cost fixed at 1 in compatible hypothetical fitness units."}, {"name": "Resistance survival ratio", "alabel": "Resistant survival", "blabel": "Susceptible survival", "amin": 0.1, "amax": 1, "astep": 0.05, "bmin": 0.05, "bmax": 1, "bstep": 0.05, "unit": "survival ratio", "expression": "a/b", "note": "Not necessarily lifetime reproductive fitness or a treatment recommendation."}, {"name": "Heterozygosity change", "alabel": "Initial heterozygosity", "blabel": "Final heterozygosity", "amin": 0, "amax": 1, "astep": 0.02, "bmin": 0, "bmax": 1, "bstep": 0.02, "unit": "absolute difference", "expression": "b-a", "note": "Diversity statistic alone cannot establish population recovery."}];
const SAFEFORMULAS = [(a,b)=>a*b,
(a,b)=>Math.max(0,a-b),
(a,b)=>2*a*(1-a)*b,
(a,b)=>a*b/(a*b+(1-a)),
(a,b)=>a/b,
(a,b)=>a*b,
(a,b)=>a*b,
(a,b)=>(1-b)*a+b*0.8,
(a,b)=>a/(2*b),
(a,b)=>a+b,
(a,b)=>a-b,
(a,b)=>100*Math.min(a,b)/b,
(a,b)=>a*b,
(a,b)=>a*b-1,
(a,b)=>a/b,
(a,b)=>b-a];
function calculateModel(i,a,b){return SAFEFORMULAS[i](a,b);}
function fmt(v){return Number.isFinite(v) ? Number(v.toPrecision(6)).toString() : 'invalid';}
function renderModels(){
 const root=document.getElementById('modelgrid'); if(!root)return;
 MODELS.forEach((m,i)=>{
  const section=document.createElement('section');section.className='simulation';section.setAttribute('aria-label',m.name);
  const heading=document.createElement('h3');heading.textContent=(i+1)+'. '+m.name;section.append(heading);
  const ids=[];const inputs=[];const readouts=[];
  [[m.alabel,m.amin,m.amax,m.astep],[m.blabel,m.bmin,m.bmax,m.bstep]].forEach((a,j)=>{
   const id='model-'+i+'-'+j; ids.push(id);const label=document.createElement('label');label.htmlFor=id;label.textContent=a[0];section.append(label);
   const range=document.createElement('input');range.id=id;range.type='range';range.min=a[1];range.max=a[2];range.step=a[3];range.value=Number(a[1]+(a[2]-a[1])*(j===0?0.6:0.63)).toFixed(4);range.setAttribute('aria-label',a[0]);section.append(range);inputs.push(range);
   const val=document.createElement('span');val.className='value';val.setAttribute('aria-live','off');section.append(val);readouts.push(val);
  });
  const result=document.createElement('output');result.setAttribute('aria-live','polite');section.append(result);
  const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('viewBox','0 0 320 120');svg.setAttribute('role','img');svg.setAttribute('aria-label','Response curve for the first variable with second parameter held fixed');section.append(svg);
  const note=document.createElement('p');note.textContent='Model limits: '+m.note;section.append(note);
  const update=()=>{
   let a=Number(inputs[0].value),b=Number(inputs[1].value);
   readouts[0].textContent=' '+fmt(a);readouts[1].textContent=' '+fmt(b);
   let v=calculateModel(i,a,b);result.textContent=fmt(v)+' '+m.unit;
   let values=[];for(let k=0;k<=55;k++){let x=m.amin+(m.amax-m.amin)*k/55;let z=calculateModel(i,x,b); if(Number.isFinite(z))values.push([x,z]);}
   const minY=Math.min(0,...values.map(v=>v[1]));const maxY=Math.max(0,...values.map(v=>v[1]));const span=Math.max(1e-9,maxY-minY);
   const coords=values.map(([x,y])=>(14+292*(x-m.amin)/(m.amax-m.amin)).toFixed(2)+','+(105-88*(y-minY)/span).toFixed(2)).join(' ');
   svg.replaceChildren();
   const axis=document.createElementNS('http://www.w3.org/2000/svg','path');axis.setAttribute('d','M 14 10 V 105 H 306');axis.setAttribute('fill','none');axis.setAttribute('stroke','currentColor');axis.setAttribute('stroke-opacity','.35');svg.append(axis);
   const curve=document.createElementNS('http://www.w3.org/2000/svg','polyline');curve.setAttribute('points',coords);curve.setAttribute('fill','none');curve.setAttribute('stroke','#2a9578');curve.setAttribute('stroke-width','3');svg.append(curve);
   const circle=document.createElementNS('http://www.w3.org/2000/svg','circle');circle.setAttribute('cx',14+292*(a-m.amin)/(m.amax-m.amin));circle.setAttribute('cy',105-88*(v-minY)/span);circle.setAttribute('r','4.5');circle.setAttribute('fill','#a66a22');svg.append(circle);
  };
  inputs.forEach(el=>el.addEventListener('input',update));update();root.append(section);
 });
}
if(typeof document!=='undefined'){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',renderModels);else renderModels();}
if(typeof module!=='undefined')module.exports={MODELS,calculateModel};



/* SimulationEngine adapter for Evolutionary Biology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof renderModels === 'function') {
      renderModels(host);
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

