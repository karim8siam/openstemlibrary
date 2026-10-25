/* Ecology Interactive Simulation Suite */
"use strict";
const MODELS = [{"name": "Logistic population growth", "alabel": "Population N", "blabel": "Carrying capacity K", "amin": 10, "amax": 900, "astep": 10, "bmin": 200, "bmax": 1500, "bstep": 50, "unit": "individuals/year", "expression": "0.25*a*(1-a/b)", "note": "Illustrative growth r=0.25 year^-1; models instantaneous change and permits negative value above K."}, {"name": "Exponential projection", "alabel": "Initial population", "blabel": "Annual fractional growth r", "amin": 20, "amax": 600, "astep": 20, "bmin": -0.2, "bmax": 0.4, "bstep": 0.02, "unit": "individuals after 3 years", "expression": "a*Math.pow(1+b,3)", "note": "Discrete annual compound growth; constant growth factor, no density feedback."}, {"name": "Occupancy detection", "alabel": "Per-visit detection p", "blabel": "Survey visits", "amin": 0.02, "amax": 0.98, "astep": 0.02, "bmin": 1, "bmax": 10, "bstep": 1, "unit": "detection probability", "expression": "1-Math.pow(1-a,b)", "note": "Assumes site occupied, independence, constant p and no false positives."}, {"name": "Simple survivorship contribution", "alabel": "Survival to age", "blabel": "Fecundity at age", "amin": 0, "amax": 1, "astep": 0.02, "bmin": 0, "bmax": 8, "bstep": 0.25, "unit": "offspring per newborn", "expression": "a*b", "note": "One l_x m_x term for net reproductive rate; not an intrinsic rate of increase."}, {"name": "Type-II feeding rate", "alabel": "Prey density", "blabel": "Handling time", "amin": 0, "amax": 250, "astep": 5, "bmin": 0.05, "bmax": 1, "bstep": 0.05, "unit": "prey per model time", "expression": "(0.07*a)/(1+0.07*b*a)", "note": "Attack coefficient held at 0.07 in compatible arbitrary units."}, {"name": "Competition suppression", "alabel": "Without-neighbor biomass", "blabel": "With-neighbor biomass", "amin": 1, "amax": 120, "astep": 1, "bmin": 0, "bmax": 120, "bstep": 2, "unit": "relative change", "expression": "(a-b)/a", "note": "Paired treatments assumed; negative values show higher biomass with neighbors."}, {"name": "Mutualism benefit contrast", "alabel": "Partner biomass", "blabel": "No-partner biomass", "amin": 1, "amax": 100, "astep": 1, "bmin": 1, "bmax": 100, "bstep": 1, "unit": "biomass difference", "expression": "a-b", "note": "Difference is not proof of direct nutrient exchange; depends on controlled conditions."}, {"name": "Trophic energy transfer", "alabel": "Producer energy", "blabel": "Transfer efficiency", "amin": 100, "amax": 20000, "astep": 100, "bmin": 0.02, "bmax": 0.3, "bstep": 0.01, "unit": "energy available next level", "expression": "a*b", "note": "Constant fraction of an energy budget, not a universal ten-percent law."}, {"name": "Net primary production", "alabel": "Gross production GPP", "blabel": "Producer respiration Ra", "amin": 100, "amax": 2000, "astep": 50, "bmin": 0, "bmax": 1700, "bstep": 50, "unit": "net production, same units", "expression": "a-b", "note": "Negative outputs indicate conditions inconsistent with positive NPP; illustrative accounting."}, {"name": "Decomposition of litter", "alabel": "Starting dry mass", "blabel": "Decay rate per month", "amin": 20, "amax": 500, "astep": 10, "bmin": 0, "bmax": 0.6, "bstep": 0.02, "unit": "remaining after 4 months", "expression": "a*Math.exp(-4*b)", "note": "Single-pool exponential model; leaching and weather-dependent processes omitted."}, {"name": "Catchment nutrient load", "alabel": "Flow m3 per second", "blabel": "Concentration mg per liter", "amin": 0, "amax": 5, "astep": 0.1, "bmin": 0, "bmax": 3, "bstep": 0.1, "unit": "kg per day", "expression": "a*1000*b*86400/1000000", "note": "Flow and concentration treated constant over one day."}, {"name": "Proportional ecosystem retention", "alabel": "Carbon inputs", "blabel": "Carbon losses", "amin": 100, "amax": 3000, "astep": 100, "bmin": 0, "bmax": 3000, "bstep": 100, "unit": "net retained carbon", "expression": "a-b", "note": "Full boundary flux inventory assumed; omitted streams and harvest can reverse sign."}, {"name": "Gini–Simpson evenness model", "alabel": "Focal species proportion", "blabel": "Second species proportion", "amin": 0, "amax": 1, "astep": 0.02, "bmin": 0, "bmax": 1, "bstep": 0.02, "unit": "Gini–Simpson index", "expression": "1-(a*a+b*b+Math.pow(1-a-b,2))", "note": "Three species with valid frequencies only when a+b<=1; negative third abundance invalid."}, {"name": "Species-area curve", "alabel": "Reference richness", "blabel": "Area multiplier", "amin": 1, "amax": 100, "astep": 1, "bmin": 0.25, "bmax": 8, "bstep": 0.25, "unit": "predicted richness", "expression": "a*Math.pow(b,0.25)", "note": "Hypothetical fixed exponent z=0.25; use only in calibration range."}, {"name": "Habitat core area", "alabel": "Square patch side", "blabel": "Edge effect distance", "amin": 100, "amax": 2000, "astep": 25, "bmin": 0, "bmax": 450, "bstep": 25, "unit": "core area square meters", "expression": "Math.pow(Math.max(0,a-2*b),2)", "note": "Square-patch approximation, species-specific edge penetration not estimated."}, {"name": "Discounted management cost", "alabel": "Future cost", "blabel": "Annual discount rate", "amin": 100, "amax": 10000, "astep": 100, "bmin": 0, "bmax": 0.2, "bstep": 0.01, "unit": "present monetary units", "expression": "a/Math.pow(1+b,3)", "note": "One fixed expenditure after three years; does not assign a price to biodiversity."}];
const SAFEFORMULAS = [(a,b)=>0.25*a*(1-a/b),
(a,b)=>a*Math.pow(1+b,3),
(a,b)=>1-Math.pow(1-a,b),
(a,b)=>a*b,
(a,b)=>(0.07*a)/(1+0.07*b*a),
(a,b)=>(a-b)/a,
(a,b)=>a-b,
(a,b)=>a*b,
(a,b)=>a-b,
(a,b)=>a*Math.exp(-4*b),
(a,b)=>a*1000*b*86400/1000000,
(a,b)=>a-b,
(a,b)=>1-(a*a+b*b+Math.pow(1-a-b,2)),
(a,b)=>a*Math.pow(b,0.25),
(a,b)=>Math.pow(Math.max(0,a-2*b),2),
(a,b)=>a/Math.pow(1+b,3)];
function calculateModel(i,a,b){if(i===12 && a+b>1)return NaN;return SAFEFORMULAS[i](a,b);}
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
   let v=calculateModel(i,a,b);result.textContent=fmt(v)+' '+m.unit+(Number.isFinite(v)?'':' (invalid parameter combination)');
   let values=[];for(let k=0;k<=55;k++){let x=m.amin+(m.amax-m.amin)*k/55;let z=calculateModel(i,x,b); if(Number.isFinite(z))values.push([x,z]);}
   const minY=Math.min(0,...values.map(v=>v[1]));const maxY=Math.max(0,...values.map(v=>v[1]));const span=Math.max(1e-9,maxY-minY);
   const coords=values.map(([x,y])=>(14+292*(x-m.amin)/(m.amax-m.amin)).toFixed(2)+','+(105-88*(y-minY)/span).toFixed(2)).join(' ');
   svg.replaceChildren();
   const axis=document.createElementNS('http://www.w3.org/2000/svg','path');axis.setAttribute('d','M 14 10 V 105 H 306');axis.setAttribute('fill','none');axis.setAttribute('stroke','currentColor');axis.setAttribute('stroke-opacity','.35');svg.append(axis);
   const curve=document.createElementNS('http://www.w3.org/2000/svg','polyline');curve.setAttribute('points',coords);curve.setAttribute('fill','none');curve.setAttribute('stroke','#2a9578');curve.setAttribute('stroke-width','3');svg.append(curve);
   const circle=document.createElementNS('http://www.w3.org/2000/svg','circle');circle.setAttribute('cx',14+292*(a-m.amin)/(m.amax-m.amin));circle.setAttribute('cy',Number.isFinite(v)?105-88*(v-minY)/span:-20);circle.setAttribute('r','4.5');circle.setAttribute('fill','#a66a22');svg.append(circle);
  };
  if(i===12){inputs[0].value='0.30';inputs[1].value='0.20';}inputs.forEach(el=>el.addEventListener('input',update));update();root.append(section);
 });
}
if(typeof document!=='undefined'){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',renderModels);else renderModels();}
if(typeof module!=='undefined')module.exports={MODELS,calculateModel};



/* SimulationEngine adapter for Ecology */
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

