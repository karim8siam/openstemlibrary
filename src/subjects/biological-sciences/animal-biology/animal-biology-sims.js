/* Animal Biology Interactive Simulation Suite */
"use strict";
const MODELS = [{"id": 0, "name": "Character sharing", "alabel": "Shared derived states", "blabel": "Total compared states", "amin": 0, "amax": 12, "astep": 1, "bmin": 12, "bmax": 24, "bstep": 1, "unit": "percent", "note": "Similarity among scored characters, not a phylogenetic support probability."}, {"id": 1, "name": "Occupancy detection", "alabel": "True occupied fraction", "blabel": "Detection probability", "amin": 0.1, "amax": 1, "astep": 0.05, "bmin": 0.2, "bmax": 1, "bstep": 0.05, "unit": "observed fraction", "note": "A sampling-process approximation; different sites may have different detectability."}, {"id": 2, "name": "Idealized cleavage", "alabel": "Starting cells", "blabel": "Synchronized rounds", "amin": 1, "amax": 8, "astep": 1, "bmin": 0, "bmax": 8, "bstep": 1, "unit": "cells", "note": "Assumes perfect cell doubling and ignores development-dependent division timing."}, {"id": 3, "name": "Sphere exchange geometry", "alabel": "Sphere radius (µm)", "blabel": "Surface roughness factor", "amin": 1, "amax": 20, "astep": 1, "bmin": 1, "bmax": 2, "bstep": 0.1, "unit": "µm⁻¹", "note": "An effective SA:V teaching index, not a validated whole-embryo transport law."}, {"id": 4, "name": "Particle filtration", "alabel": "Water processed (L/min)", "blabel": "Capture fraction", "amin": 0, "amax": 3, "astep": 0.1, "bmin": 0, "bmax": 1, "bstep": 0.05, "unit": "L/min effective", "note": "Effective cleared volume; feeding assimilation is not established by particle removal."}, {"id": 5, "name": "Swimming pulse proxy", "alabel": "Pulses per minute", "blabel": "Displacement per pulse (cm)", "amin": 0, "amax": 90, "astep": 5, "bmin": 0, "bmax": 4, "bstep": 0.2, "unit": "cm/min", "note": "Kinematic proxy; currents and body orientation alter net movement."}, {"id": 6, "name": "Simple lever output", "alabel": "Input force (N)", "blabel": "In-lever / out-lever", "amin": 0, "amax": 100, "astep": 5, "bmin": 0.1, "bmax": 1.5, "bstep": 0.05, "unit": "N", "note": "Static mechanical advantage is not full moving-jaw performance."}, {"id": 7, "name": "Wing loading", "alabel": "Body mass (g)", "blabel": "Wing area (cm²)", "amin": 0.5, "amax": 50, "astep": 0.5, "bmin": 1, "bmax": 100, "bstep": 1, "unit": "N/m²", "note": "Uses mass in grams converted to weight, with simplified total wing area."}, {"id": 8, "name": "Anatomical trait score", "alabel": "Observed characters", "blabel": "Reference characters", "amin": 0, "amax": 6, "astep": 1, "bmin": 5, "bmax": 10, "bstep": 1, "unit": "percent", "note": "Character observability at a stage; cannot settle ancestry on its own."}, {"id": 9, "name": "Egg mass loss", "alabel": "Initial egg mass (g)", "blabel": "Mass decrease (g)", "amin": 5, "amax": 80, "astep": 1, "bmin": 0, "bmax": 5, "bstep": 0.1, "unit": "percent", "note": "Mass differences are only proxies for water loss when other processes are controlled."}, {"id": 10, "name": "Oxygen-use balance", "alabel": "Blood flow (L/min)", "blabel": "Content difference (mL/L)", "amin": 0.1, "amax": 8, "astep": 0.1, "bmin": 0, "bmax": 120, "bstep": 5, "unit": "mL O₂/min", "note": "Steady-state Fick-style balance; do not treat as clinical monitoring."}, {"id": 11, "name": "Q10 temperature model", "alabel": "Temperature increase (°C)", "blabel": "Q10", "amin": 0, "amax": 25, "astep": 1, "bmin": 1, "bmax": 3, "bstep": 0.1, "unit": "rate multiplier", "note": "Assumes stable Q10 across the displayed temperature interval."}, {"id": 12, "name": "Patch intake rate", "alabel": "Energy gained (kJ)", "blabel": "Foraging plus travel time (min)", "amin": 1, "amax": 100, "astep": 1, "bmin": 1, "bmax": 60, "bstep": 1, "unit": "kJ/min", "note": "Ignores risk, tissue maintenance and lost opportunities."}, {"id": 13, "name": "Signal discriminability proxy", "alabel": "Hit rate (%)", "blabel": "False-alarm rate (%)", "amin": 0, "amax": 100, "astep": 5, "bmin": 0, "bmax": 100, "bstep": 5, "unit": "percentage points", "note": "Not signal-detection d-prime: use the full response distribution for that."}, {"id": 14, "name": "Annual finite growth", "alabel": "Population next year", "blabel": "Population this year", "amin": 20, "amax": 1000, "astep": 20, "bmin": 20, "bmax": 1000, "bstep": 20, "unit": "lambda", "note": "Both counts must have comparable detection effort and population boundaries."}, {"id": 15, "name": "Occupancy correction check", "alabel": "Naive occupancy", "blabel": "Detectability", "amin": 0, "amax": 1, "astep": 0.05, "bmin": 0.2, "bmax": 1, "bstep": 0.05, "unit": "corrected occupancy", "note": "Values exceeding 1 expose failure of this naive approximation; never clip silently."}];
function calculate(m,a,b){
 switch(m.id){
 case 0:return a<=b?100*a/b:NaN;
 case 1:return a*b;
 case 2:return a*Math.pow(2,b);
 case 3:return 3*b/a;
 case 4:return a*b;
 case 5:return a*b;
 case 6:return a*b;
 case 7:return a*0.00981/(b*0.0001);
 case 8:return a<=b?100*a/b:NaN;
 case 9:return a>=b?100*b/a:NaN;
 case 10:return a*b;
 case 11:return Math.pow(b,a/10);
 case 12:return a/b;
 case 13:return a-b;
 case 14:return a/b;
 case 15:return a/b;
 default:throw Error("Unknown model id");
 }
}
function plot(container,m,b){
 const path=document.createElementNS('http://www.w3.org/2000/svg','path');
 const samples=Array.from({length:51},(_,i)=>calculate(m,m.amin+(m.amax-m.amin)*i/50,b));
 const finite=samples.filter(Number.isFinite);if(!finite.length)return;
 const lo=Math.min(...finite),hi=Math.max(...finite),span=hi-lo||1;
 const p=samples.map((v,i)=>Number.isFinite(v)?`${i===0?'M':'L'}${(6+288*i/50).toFixed(1)},${(94-83*(v-lo)/span).toFixed(1)}`:'').filter(Boolean).join(' ');
 const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('viewBox','0 0 300 105');svg.setAttribute('aria-label','Curve of simplified model output against the first input');svg.setAttribute('role','img');
 const axis=document.createElementNS('http://www.w3.org/2000/svg','path');axis.setAttribute('d','M6 8 V94 H294');axis.setAttribute('fill','none');axis.setAttribute('stroke','#749784');svg.append(axis);
 path.setAttribute('d',p);path.setAttribute('stroke','#187c60');path.setAttribute('fill','none');path.setAttribute('stroke-width','2.5');svg.append(path);container.replaceChildren(svg);
}
function buildModels(){const host=document.getElementById('models');if(!host)return;const u=Number(host.dataset.unit);MODELS.slice(2*(u-1),2*u).forEach(m=>{
 const card=document.createElement('section');card.className='model';const h=document.createElement('h3');h.textContent=m.name;card.append(h);
 function slider(label,min,max,step,initial){const l=document.createElement('label');l.textContent=label+': ';const inp=document.createElement('input');inp.type='range';inp.min=min;inp.max=max;inp.step=step;inp.value=initial;l.append(inp);const value=document.createElement('span');l.append(value);card.append(l);return {inp,value}}
 const av=slider(m.alabel,m.amin,m.amax,m.astep,(m.amin+m.amax)/2);
 const bv=slider(m.blabel,m.bmin,m.bmax,m.bstep,(m.bmin+m.bmax)/2);
 const out=document.createElement('output');const graph=document.createElement('div');const desc=document.createElement('p');desc.className='note';desc.textContent=m.note+' All displayed values are teaching approximations, not validated predictions.';
 function update(){const a=Number(av.inp.value),b=Number(bv.inp.value),ans=calculate(m,a,b);av.value.textContent=String(a);bv.value.textContent=String(b);out.textContent=Number.isFinite(ans)?`${ans.toFixed(3)} ${m.unit}`:'Invalid combination: increase the reference value';plot(graph,m,b);if(m.id===15&&ans>1)out.textContent+= ' — invalid occupancy (>1): model assumptions fail.';}
 av.inp.addEventListener('input',update);bv.inp.addEventListener('input',update);card.append(out,graph,desc);host.append(card);update();
 });}
if(typeof document!=='undefined')document.addEventListener('DOMContentLoaded',buildModels);
if(typeof module!=='undefined')module.exports={MODELS,calculate};



/* SimulationEngine adapter for Animal Biology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof buildModels === 'function') {
      buildModels(host);
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

