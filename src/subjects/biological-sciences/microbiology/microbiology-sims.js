/* Microbiology Interactive Simulation Suite */
"use strict";
(function(g){
const specs=[{"key":"read-fraction","unit":1,"title":"Sequencing read fraction","xLabel":"Reads classified in target group","xmin":0,"xmax":1000,"x0":260,"xstep":1,"pLabel":"Reads in other groups","pmin":100,"pmax":1000,"p0":740,"pstep":1,"unitLabel":"%","note":"Read fraction is not the living-cell fraction; marker copy number and extraction bias are not represented.","formula":"100 × a/(a+b)","test":"Compare the chart with the fractional count calculation; distinguish reads from cells."},{"key":"mismatch","unit":1,"title":"Observed marker mismatch fraction","xLabel":"Mismatched aligned positions","xmin":0,"xmax":400,"x0":60,"xstep":1,"pLabel":"Comparable positions","pmin":600,"pmax":1600,"p0":1000,"pstep":1,"unitLabel":"%","note":"Uncorrected sequence p-distance; not elapsed evolutionary time and not a species threshold.","formula":"100 × mismatches/sites","test":"Check why one additional mismatch has different influence at different alignment lengths."},{"key":"surface","unit":2,"title":"Spherical cell surface-to-volume indicator","xLabel":"Cell radius (µm)","xmin":0.5,"xmax":8,"x0":1,"pLabel":"Idealized area multiplier","pmin":1,"pmax":4,"p0":1,"unitLabel":"µm⁻¹","note":"For a sphere A/V=3/r; multiplier is illustrative area augmentation, not an empirical folding measurement.","formula":"3 × multiplier / radius","test":"Double the radius, verify the ratio halves at fixed multiplier."},{"key":"randomwalk","unit":2,"title":"Unbiased two-dimensional RMS displacement","xLabel":"Elapsed time (min)","xmin":0,"xmax":120,"x0":30,"pLabel":"Effective diffusivity (µm²/min)","pmin":0.1,"pmax":5,"p0":2,"unitLabel":"µm","note":"Statistical displacement proxy; directed swimming, chemotaxis and flow are excluded.","formula":"√(4 × D × time)","test":"Quadruple time to double predicted RMS displacement when D is held fixed."},{"key":"growth","unit":3,"title":"Ideal unrestricted population doubling","xLabel":"Elapsed time (h)","xmin":0,"xmax":12,"x0":6,"pLabel":"Generation time (h)","pmin":1,"pmax":6,"p0":2,"unitLabel":"× initial population","note":"No lag, death, nutrient exhaustion or population heterogeneity; relative counts only.","formula":"2^(time/generation time)","test":"At three generations the predicted multiplier is eight."},{"key":"monod","unit":3,"title":"Monod-type substrate response","xLabel":"Substrate concentration (mg/L)","xmin":0,"xmax":100,"x0":20,"pLabel":"Half-saturation Ks (mg/L)","pmin":5,"pmax":60,"p0":20,"unitLabel":"h⁻¹","note":"Illustrative µmax=0.8/h and one limiting substrate; not an empirically fitted culture model.","formula":"0.8 × S/(Ks + S)","test":"At S=Ks the predicted rate is half the specified upper rate."},{"key":"events","unit":4,"title":"At least one hypothetical event","xLabel":"Expected events per window","xmin":0,"xmax":8,"x0":2,"pLabel":"Window scaling factor","pmin":0.2,"pmax":2,"p0":1,"unitLabel":"%","note":"Poisson independent constant-rate event model; not a measurement of mutation biology.","formula":"100 × (1 − exp(−λ × scale))","test":"With expected events two at scale one, compare with the probability of zero events."},{"key":"selection","unit":4,"title":"Deterministic one-generation frequency change","xLabel":"Starting type-A frequency","xmin":0.01,"xmax":0.99,"x0":0.3,"pLabel":"Relative advantage s","pmin":-0.5,"pmax":0.7,"p0":0.1,"unitLabel":"proportion","note":"Type A weight 1+s; type B weight 1; excludes drift, transfer and changing environment.","formula":"p(1+s)/[p(1+s)+(1−p)]","test":"Verify normalization for s=0 and compare changing starting frequency."},{"key":"attenuation","unit":5,"title":"Ideal biofilm concentration attenuation","xLabel":"Depth (mm)","xmin":0,"xmax":3,"x0":0.4,"pLabel":"Attenuation length L (mm)","pmin":0.2,"pmax":2,"p0":0.8,"unitLabel":"% surface value","note":"Exponential phenomenological shape; cannot determine diffusion versus reaction mechanisms.","formula":"100 × exp(−depth/L)","test":"At a depth equal to L, compare to about 36.8% of surface concentration."},{"key":"entropy","unit":5,"title":"Shannon entropy of uneven community","xLabel":"Dominant group fraction","xmin":0.05,"xmax":0.95,"x0":0.5,"pLabel":"Number of equal minor groups","pmin":2,"pmax":8,"p0":3,"pstep":1,"unitLabel":"nats","note":"Other groups share the remaining probability equally; category resolution controls the index.","formula":"−p ln p − (1−p) ln((1−p)/N)","test":"Examine how evenness and the number of categories change the entropy."},{"key":"binding","unit":6,"title":"Idealized molecular receptor occupancy","xLabel":"Ligand concentration (arbitrary)","xmin":0.01,"xmax":20,"x0":5,"pLabel":"Dissociation constant Kd","pmin":0.1,"pmax":10,"p0":5,"unitLabel":"%","note":"Equilibrium one-site binding only; not a quantitative prediction of host immunity.","formula":"100 × ligand/(ligand+Kd)","test":"Set ligand equal to Kd and check the 50% value."},{"key":"effectiveR","unit":6,"title":"Effective-reproduction threshold illustration","xLabel":"Susceptible population fraction","xmin":0,"xmax":1,"x0":0.5,"pLabel":"Hypothetical baseline R₀","pmin":0.5,"pmax":5,"p0":2,"unitLabel":"ratio","note":"Homogeneous idealized relation only; cannot forecast infection or clinical outcomes.","formula":"R₀ × susceptible fraction","test":"Find where the line crosses one for the selected baseline parameter."},{"key":"yield","unit":7,"title":"Simplified biomass-yield mass balance","xLabel":"Substrate consumed (g)","xmin":0,"xmax":100,"x0":40,"pLabel":"Dry-biomass yield (g/g)","pmin":0.05,"pmax":0.8,"p0":0.3,"unitLabel":"g dry mass","note":"Biomass accumulation proxy, excluding maintenance, carbon losses and byproducts.","formula":"Consumed substrate × yield","test":"Check units and explain why accumulated biomass differs from volumetric productivity."},{"key":"half-life","unit":7,"title":"Illustrative first-order residual fraction","xLabel":"Elapsed time (h)","xmin":0,"xmax":48,"x0":8,"pLabel":"Apparent half-life (h)","pmin":2,"pmax":24,"p0":8,"unitLabel":"% remaining","note":"Loss from sampled compartment does not itself demonstrate microbial degradation.","formula":"100 × 2^(−time/half-life)","test":"At one half-life, the predicted remaining percentage is 50."},{"key":"bayes","unit":8,"title":"Positive predictive value and base rate","xLabel":"Underlying fraction with target condition","xmin":0.001,"xmax":0.3,"x0":0.02,"pLabel":"Sensitivity","pmin":0.6,"pmax":0.99,"p0":0.95,"unitLabel":"%","note":"Assumes specificity exactly 95% and validation parameters apply; no patient-level diagnosis.","formula":"100 × sens×prev / [sens×prev + 0.05×(1−prev)]","test":"Lower prevalence without changing assay performance and inspect PPV."},{"key":"sem","unit":8,"title":"Standard error of an independent sample mean","xLabel":"Independent observation count","xmin":2,"xmax":100,"x0":25,"xstep":1,"pLabel":"Standard deviation (measurement units)","pmin":1,"pmax":20,"p0":8,"unitLabel":"measurement units","note":"Assumes independent, identically distributed observations; technical repeats are not biological replicates.","formula":"SD/√n","test":"At four times the sample count, verify standard error halves."}];
function compute(id,x,p){
if(typeof x!=="number"||typeof p!=="number"||!Number.isFinite(x)||!Number.isFinite(p))throw new TypeError('Finite numeric values required');
const s=specs.find(k=>k.key===id);if(!s)throw new Error('Unknown model '+id);
if(x<s.xmin||x>s.xmax||p<s.pmin||p>s.pmax)throw new RangeError('Input outside documented range');
switch(id){
case'read-fraction':return 100*x/(x+p);
case'mismatch':return 100*x/p;
case'surface':return 3*p/x;
case'randomwalk':return Math.sqrt(4*p*x);
case'growth':return Math.pow(2,x/p);
case'monod':return .8*x/(p+x);
case'events':return 100*(-Math.expm1(-x*p));
case'selection':return x*(1+p)/(x*(1+p)+(1-x));
case'attenuation':return 100*Math.exp(-x/p);
case'entropy':return -x*Math.log(x)-(1-x)*Math.log((1-x)/p);
case'binding':return 100*x/(x+p);
case'effectiveR':return x*p;
case'yield':return x*p;
case'half-life':return 100*Math.pow(2,-x/p);
case'bayes':return 100*p*x/(p*x+.05*(1-x));
case'sem':return p/Math.sqrt(x);
}
throw new Error('Not implemented '+id);
}
function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function smart(n){return Number(n).toLocaleString('en',{maximumFractionDigits:4});}
function plot(def,x,p){
const width=620,height=235, left=58,right=18,top=14,bottom=44;const pw=width-left-right,ph=height-top-bottom;
const ys=[],compare=[],xs=[];const pCompare=def.key==='entropy' ? (p===def.pmax ? Math.max(def.pmin,Math.round(p*.7)) : Math.min(def.pmax,Math.round(p*1.3))) : (p===def.pmax? Math.max(def.pmin,p*.7):Math.min(def.pmax,p*1.3));
for(let j=0;j<=90;j++){const xx=def.xmin+(def.xmax-def.xmin)*j/90;xs.push(xx);ys.push(compute(def.key,xx,p));compare.push(compute(def.key,xx,pCompare));}
const maxv=Math.max(...ys,...compare,compute(def.key,x,p),.0001)*1.08;
const xy=(a,b)=>`${(left+(a-def.xmin)/(def.xmax-def.xmin)*pw).toFixed(2)},${(top+ph-b/maxv*ph).toFixed(2)}`;
const line=vals=>vals.map((v,i)=>xy(xs[i],v)).join(' ');
const selected=compute(def.key,x,p),px=left+(x-def.xmin)/(def.xmax-def.xmin)*pw,py=top+ph-selected/maxv*ph;
const grids=Array.from({length:5},(_,i)=>{const val=maxv*i/4;const y=top+ph-(val/maxv)*ph;return `<line x1="${left}" y1="${y}" x2="${width-right}" y2="${y}" stroke="#26354c" stroke-dasharray="4 6"/><text x="${left-7}" y="${y+4}" text-anchor="end" fill="#8297ab" font-size="11">${smart(val)}</text>`;}).join('');
return `<svg viewBox="0 0 ${width} ${height}" role="img" aria-label="${esc(def.title)} plotted against ${esc(def.xLabel)} with scenario comparison" class="model-chart" preserveAspectRatio="xMidYMid meet"><rect x="0" y="0" width="${width}" height="${height}" rx="12" fill="#101b2d"/>${grids}<polyline points="${line(compare)}" fill="none" stroke="#d4a65b" stroke-width="2" stroke-dasharray="6 5"/><polyline points="${line(ys)}" fill="none" stroke="#62d8ba" stroke-width="3"/><line x1="${px}" y1="${py}" x2="${px}" y2="${top+ph}" stroke="#c2d0e0" stroke-dasharray="3 4"/><circle cx="${px}" cy="${py}" r="6" fill="#d6f6ef" stroke="#0f6259" stroke-width="2"/><text x="${left}" y="${height-17}" fill="#b6c9db" font-size="11">${esc(def.xLabel)}</text><text x="${width-right}" y="${height-17}" text-anchor="end" fill="#92f0d6" font-size="11">Current parameter</text><text x="${width-right}" y="${height-31}" text-anchor="end" fill="#e3b776" font-size="11">Alternative parameter</text></svg>`;
}
function create(el){const d=specs.find(x=>x.key===el.dataset.model); if(!d)return;
const id=d.key.replace(/[^a-z0-9]/gi,'');
el.innerHTML=`<h3>${esc(d.title)}</h3><p class="model-description"><strong>Model:</strong> ${esc(d.formula)}</p><div class="sim-controls"><label for="${id}-x">${esc(d.xLabel)}: <output class="live-x">${smart(d.x0)}</output><input id="${id}-x" class="control-x" type="range" min="${d.xmin}" max="${d.xmax}" step="${d.xstep||'any'}" value="${d.x0}" /></label><label for="${id}-p">${esc(d.pLabel)}: <output class="live-p">${smart(d.p0)}</output><input id="${id}-p" class="control-p" type="range" min="${d.pmin}" max="${d.pmax}" step="${d.pstep||'any'}" value="${d.p0}" /></label></div><div class="output" aria-live="polite"></div><div class="chartbox"></div><p class="note"><strong>Model boundary:</strong> ${esc(d.note)}</p><p class="note"><strong>Try this:</strong> ${esc(d.test)}</p><button class="reset" type="button">Reset both controls</button>`;
const xc=el.querySelector('.control-x'),pc=el.querySelector('.control-p');
function render(){let xx=Number(xc.value),pp=Number(pc.value);el.querySelector('.live-x').textContent=smart(xx);el.querySelector('.live-p').textContent=smart(pp);el.querySelector('.output').textContent=`Model prediction: ${smart(compute(d.key,xx,pp))} ${d.unitLabel}`;el.querySelector('.chartbox').innerHTML=plot(d,xx,pp);}
xc.addEventListener('input',render);pc.addEventListener('input',render);el.querySelector('.reset').addEventListener('click',()=>{xc.value=d.x0;pc.value=d.p0;render();});render();
}
function mount(root=document){root.querySelectorAll('[data-model]').forEach(create);}
g.MicroModels={specs,compute,plot,mount};
if(typeof document!=='undefined'){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>mount());else mount();}
})(typeof globalThis!=='undefined'?globalThis:this);



/* SimulationEngine adapter for Microbiology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (root.MicroModels && root.MicroModels.mount) {
      root.MicroModels.mount(host, simType);
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

