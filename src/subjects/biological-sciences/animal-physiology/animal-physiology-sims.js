/* Animal Physiology Interactive Simulation Suite */
/* OpenSTEM Animal Physiology interactive models. Offline, no tracking, no dependencies. */
'use strict';
const MODELS=[{"id":0,"unit":1,"title":"Homeostatic recovery of a perturbation","kind":"feedback","xLabel":"Recovery time (min)","yLabel":"Deviation remaining (units)","aLabel":"Correction gain (/min)","a":0.22,"aMin":0.06,"aMax":0.6,"bLabel":"Initial deviation","b":12,"bMin":4,"bMax":24,"xMin":0,"xMax":20,"warning":"Exponential restoration with constant gain; no time delay, saturation or hormone dynamics."},{"id":1,"unit":1,"title":"Metabolic allometry","kind":"allometry","xLabel":"Body mass (relative units)","yLabel":"Rate (relative units)","aLabel":"Mass exponent","a":0.75,"aMin":0.55,"aMax":1.0,"bLabel":"Reference rate","b":10,"bMin":4,"bMax":20,"xMin":0.5,"xMax":15,"warning":"Power law is empirical and depends on temperature, phylogeny, and which animals are compared."},{"id":2,"unit":2,"title":"Potassium equilibrium potential","kind":"nernst","xLabel":"External K+ (mM)","yLabel":"Potential (mV)","aLabel":"Intracellular K+ (mM)","a":140,"aMin":90,"aMax":180,"bLabel":"Temperature coefficient (mV)","b":61.5,"bMin":55,"bMax":65,"xMin":1,"xMax":20,"warning":"Nernst is ion-specific at equilibrium, not the resting voltage of an entire living neuron."},{"id":3,"unit":2,"title":"Receptor saturation","kind":"sensory","xLabel":"Stimulus magnitude","yLabel":"Response fraction","aLabel":"Threshold","a":5,"aMin":2,"aMax":8,"bLabel":"Steepness","b":1.1,"bMin":0.3,"bMax":2.0,"xMin":0,"xMax":12,"warning":"Logistic teaching fit, not an experimentally measured sensory detection function."},{"id":4,"unit":3,"title":"Muscle force–velocity relation","kind":"forcevelocity","xLabel":"Shortening velocity (m/s)","yLabel":"Concentric force (N)","aLabel":"Maximum isometric force (N)","a":120,"aMin":60,"aMax":180,"bLabel":"Maximum velocity (m/s)","b":1.5,"bMin":0.7,"bMax":3.0,"xMin":0,"xMax":2.7,"warning":"Concentric-only force curve; real muscle also depends on activation, length and temperature."},{"id":5,"unit":3,"title":"Mechanical power with shortening speed","kind":"musclepower","xLabel":"Shortening velocity (m/s)","yLabel":"Power (W)","aLabel":"Maximum isometric force (N)","a":120,"aMin":50,"aMax":180,"bLabel":"Maximum velocity (m/s)","b":1.5,"bMin":0.7,"bMax":3.0,"xMin":0,"xMax":2.7,"warning":"Mechanical output only; assumes a force–velocity fit and does not predict metabolic power."},{"id":6,"unit":4,"title":"Cardiac output under changing rate","kind":"cardiac","xLabel":"Heart rate (beats/min)","yLabel":"Cardiac output (L/min)","aLabel":"Stroke volume (mL)","a":65,"aMin":30,"aMax":120,"bLabel":"Rate-dependent filling factor","b":0.15,"bMin":0,"bMax":0.6,"xMin":30,"xMax":180,"warning":"A phenomenological filling penalty; cardiac physiology cannot be inferred from this toy curve."},{"id":7,"unit":4,"title":"Gas transfer across a barrier","kind":"fick","xLabel":"Oxygen partial-pressure difference (arbitrary)","yLabel":"Transfer (relative units)","aLabel":"Effective diffusion conductance","a":1.5,"aMin":0.4,"aMax":3.0,"bLabel":"Exchange area multiplier","b":1,"bMin":0.3,"bMax":2.0,"xMin":0,"xMax":12,"warning":"Simple steady diffusion assumes unchanged area, barrier geometry and blood-side mixing."},{"id":8,"unit":5,"title":"Osmotic pressure of ideal solute","kind":"osmosis","xLabel":"Effective osmolarity (mOsm/L)","yLabel":"Ideal pressure (kPa)","aLabel":"Temperature (K)","a":300,"aMin":280,"aMax":320,"bLabel":"Reflection factor","b":1,"bMin":0.2,"bMax":1,"xMin":0,"xMax":250,"warning":"Dilute ideal approximation. Reflection coefficient is conceptual, not measured for a real epithelial layer."},{"id":9,"unit":5,"title":"Renal marker clearance","kind":"clearance","xLabel":"Urine marker concentration (mg/L)","yLabel":"Clearance (mL/min)","aLabel":"Urine flow (mL/min)","a":2,"aMin":0.5,"aMax":6,"bLabel":"Plasma concentration (mg/L)","b":2,"bMin":1,"bMax":8,"xMin":5,"xMax":200,"warning":"Clearance assumes matched sample intervals; secretion and reabsorption determine what it means biologically."},{"id":10,"unit":6,"title":"Saturable intestinal uptake","kind":"uptake","xLabel":"Substrate concentration (mmol/L)","yLabel":"Uptake (nmol/min)","aLabel":"Maximal uptake","a":80,"aMin":30,"aMax":140,"bLabel":"Half-saturation concentration","b":2,"bMin":0.5,"bMax":7,"xMin":0,"xMax":15,"warning":"Michaelis–Menten-like surrogate; gut length, flow, mixing and transporter expression are omitted."},{"id":11,"unit":6,"title":"Thermal sensitivity of reactions","kind":"q10","xLabel":"Temperature (°C)","yLabel":"Relative reaction rate","aLabel":"Q10 factor","a":2.0,"aMin":1.1,"aMax":3.0,"bLabel":"Reference rate at 20°C","b":1,"bMin":0.5,"bMax":3,"xMin":5,"xMax":40,"warning":"Q10 is an interval-dependent approximation and fails across thermal injury thresholds."},{"id":12,"unit":7,"title":"Simple endocrine clearance","kind":"endocrine","xLabel":"Time after pulse (min)","yLabel":"Hormone concentration (arbitrary)","aLabel":"Half-life (min)","a":30,"aMin":10,"aMax":80,"bLabel":"Initial pulse amplitude","b":100,"bMin":30,"bMax":180,"xMin":0,"xMax":180,"warning":"Single-compartment decay without ongoing secretion; not a human or animal hormone reference."},{"id":13,"unit":7,"title":"Timing and amplitude of daily signals","kind":"circadian","xLabel":"Clock time (hours)","yLabel":"Relative endocrine activity","aLabel":"Amplitude","a":0.4,"aMin":0.1,"aMax":0.8,"bLabel":"Peak time (hours)","b":8,"bMin":0,"bMax":24,"xMin":0,"xMax":48,"warning":"An illustrative periodic curve; real endocrine rhythms are neither perfectly sinusoidal nor identical between individuals."},{"id":14,"unit":8,"title":"Dry heat loss to the environment","kind":"heat","xLabel":"Ambient temperature (°C)","yLabel":"Dry heat loss (W)","aLabel":"Body temperature (°C)","a":37,"aMin":30,"aMax":41,"bLabel":"Conductance (W/°C)","b":5,"bMin":1,"bMax":10,"xMin":0,"xMax":45,"warning":"Dry exchange only; omits solar radiation, wetness, evaporative heat loss and thermoregulation."},{"id":15,"unit":8,"title":"Available oxygen and modeled dive time","kind":"dive","xLabel":"Oxygen use (L/min)","yLabel":"Estimated aerobic time (min)","aLabel":"Stored usable oxygen (L)","a":1.5,"aMin":0.4,"aMax":3.0,"bLabel":"Available fraction","b":0.8,"bMin":0.4,"bMax":1,"xMin":0.03,"xMax":0.25,"warning":"Not a safe dive limit: assumes constant use and ignores changing circulation, pressure and anaerobic metabolism."}];
const NS='http://www.w3.org/2000/svg';
function result(m,x,a,b){
 switch(m.kind){
  case 'feedback':return b*Math.exp(-a*x);
  case 'allometry':return b*Math.pow(x,a);
  case 'nernst':return b*Math.log10(Math.max(x,0.0001)/a);
  case 'sensory':return 1/(1+Math.exp(-(x-a)*b));
  case 'forcevelocity':return a*Math.max(0,(1-x/b))/(1+2*x/b);
  case 'musclepower':return x*a*Math.max(0,(1-x/b))/(1+2*x/b);
  case 'cardiac':return x*a/1000 * (1-b*Math.max(0,x-90)/90);
  case 'fick':return a*b*x;
  case 'osmosis':return x*0.001*8.314*a*b; /* 1 mOsm/L = 1 mol/m^3, Pa -> kPa */
  case 'clearance':return x*a/b; /* mg/L * mL/min / (mg/L) */
  case 'uptake':return a*x/(b+x);
  case 'q10':return b*Math.pow(a,(x-20)/10);
  case 'endocrine':return b*Math.pow(2,-x/a);
  case 'circadian':return Math.max(0,1+a*Math.cos(2*Math.PI*(x-b)/24));
  case 'heat':return b*(a-x);
  case 'dive':return a*b/Math.max(0.001,x);
 }
 return NaN;
}
function newSvg(tag,attrs){const el=document.createElementNS(NS,tag);Object.entries(attrs||{}).forEach(([k,v])=>el.setAttribute(k,String(v)));return el}
function renderModel(box,m){
 box.replaceChildren();const controls=document.createElement('div');controls.className='controls';const inputs=[];
 for(const side of ['a','b']){
  const line=document.createElement('div');const label=document.createElement('label');const display=document.createElement('output');const input=document.createElement('input');
  input.type='range';input.min=m[side+'Min'];input.max=m[side+'Max'];input.step=((m[side+'Max']-m[side+'Min'])/100).toFixed(6);input.value=m[side];
  input.id='model-'+m.id+'-'+side;label.htmlFor=input.id;const words=document.createElement('span');words.textContent=m[side+'Label'];label.append(words,display);line.append(label,input);controls.appendChild(line);inputs.push({input,display});
 }
 const graph=newSvg('svg',{viewBox:'0 0 620 250',role:'img','aria-label':m.title+' curve; '+m.xLabel+' along horizontal axis and '+m.yLabel+' vertically',class:'chart'});
 const summary=document.createElement('div');summary.className='readout';summary.setAttribute('aria-live','polite');box.append(controls,graph,summary);
 function redraw(){
  const a=Number(inputs[0].input.value),b=Number(inputs[1].input.value);inputs[0].display.textContent=a.toFixed(2);inputs[1].display.textContent=b.toFixed(2);
  const values=Array.from({length:86},(_,i)=>{const x=m.xMin+(m.xMax-m.xMin)*i/85;return {x,y:result(m,x,a,b)}}).filter(p=>Number.isFinite(p.y));
  if(!values.length){summary.textContent='Model unavailable for these inputs';return}
  const ymin=Math.min(0,...values.map(p=>p.y)), ymax=Math.max(1,...values.map(p=>p.y));const lo=ymin-0.09*(ymax-ymin),hi=ymax+0.09*(ymax-ymin);
  const X=x=>48+(x-m.xMin)/(m.xMax-m.xMin)*555,Y=y=>211-(y-lo)/(hi-lo)*170;
  graph.replaceChildren();
  for(let i=0;i<=4;i++){const y=211-170*i/4;graph.append(newSvg('line',{x1:48,y1:y,x2:603,y2:y,stroke:'#d9e9e9'}));const label=newSvg('text',{x:41,y:y+4,'text-anchor':'end','font-size':11,fill:'#415d6b'});label.textContent=(lo+(hi-lo)*i/4).toFixed(1);graph.append(label)}
  const poly=newSvg('polyline',{fill:'none',stroke:'#007c85','stroke-width':3.2,'stroke-linejoin':'round','stroke-linecap':'round',points:values.map(p=>`${X(p.x).toFixed(2)},${Y(p.y).toFixed(2)}`).join(' ')});graph.append(poly);
  for(let i=0;i<=4;i++){const x=m.xMin+(m.xMax-m.xMin)*i/4;const label=newSvg('text',{x:X(x),y:232,'text-anchor':'middle','font-size':11,fill:'#415d6b'});label.textContent=x.toFixed(1);graph.append(label)}
  const tail=values[values.length-1],min=Math.min(...values.map(p=>p.y)),max=Math.max(...values.map(p=>p.y));
  summary.textContent=`Last point: ${tail.y.toPrecision(4)} · Curve range: ${min.toPrecision(4)} to ${max.toPrecision(4)} (${m.yLabel}).`;
 }
 inputs.forEach(({input})=>input.addEventListener('input',redraw));redraw();
}
document.addEventListener('DOMContentLoaded',()=>{document.querySelectorAll('[data-model-id]').forEach(el=>{const m=MODELS[Number(el.dataset.modelId)];if(m)renderModel(el,m)});});



/* SimulationEngine adapter for Animal Physiology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof MODELS === 'undefined' || typeof renderModel !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var idx = (u - 1) * 2;
    var m = MODELS[idx] || MODELS[0];
    if (m) {
      var card = document.createElement('div');
      card.className = 'sim-card';
      var h4 = document.createElement('h4');
      h4.textContent = m.title;
      card.appendChild(h4);
      var simBox = document.createElement('div');
      simBox.className = 'openstem-sim-viewport';
      card.appendChild(simBox);
      host.appendChild(card);
      renderModel(simBox, m);
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

