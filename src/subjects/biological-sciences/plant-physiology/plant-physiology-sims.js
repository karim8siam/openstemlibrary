/* Plant Physiology Interactive Simulation Suite */
"use strict";
const MODELS=[{"id":0,"unit":1,"title":"Ideal osmotic potential","kind":"osmotic","xLabel":"Non-dissociating solute (mol/L)","yLabel":"Solute potential (MPa)","a":{"label":"Temperature (K)","value":298,"min":280,"max":310},"b":{"label":"Osmotic multiplier","value":1,"min":0.5,"max":2},"xMin":0,"xMax":0.6,"warning":"Van’t Hoff ideal dilute relation. Real sap includes ion activities and mixtures."},{"id":1,"unit":1,"title":"Simple root hydraulic flux","kind":"hydraulic","xLabel":"Water-potential gradient (MPa)","yLabel":"Volume flux (mL/h)","a":{"label":"Hydraulic conductance","value":4,"min":1,"max":8},"b":{"label":"Parallel pathway factor","value":1,"min":0.5,"max":2},"xMin":0,"xMax":1.2,"warning":"Constant conductance, no soil resistance dynamics or embolism."},{"id":2,"unit":2,"title":"Ideal uptake saturation","kind":"uptake","xLabel":"External nutrient (mM)","yLabel":"Nutrient uptake (µmol/h)","a":{"label":"Vmax (µmol/h)","value":16,"min":5,"max":25},"b":{"label":"Km (mM)","value":0.7,"min":0.2,"max":1.8},"xMin":0,"xMax":4,"warning":"Single saturating transporter. Ignores efflux and competing ions."},{"id":3,"unit":2,"title":"Rhizosphere diffusion","kind":"diffusion","xLabel":"Diffusion distance (mm)","yLabel":"Illustrative nutrient flux (relative)","a":{"label":"Concentration contrast","value":4,"min":1,"max":10},"b":{"label":"Effective coefficient","value":0.7,"min":0.2,"max":2},"xMin":0.2,"xMax":4,"warning":"Inverse-distance proxy, not a calibrated soil diffusion estimate."},{"id":4,"unit":3,"title":"Light response of carbon uptake","kind":"lightcurve","xLabel":"Photon input (relative)","yLabel":"Net assimilation (relative)","a":{"label":"Photosynthetic capacity","value":20,"min":8,"max":30},"b":{"label":"Saturation intensity","value":200,"min":80,"max":450},"xMin":0,"xMax":900,"warning":"Rectangular hyperbola minus a constant respiratory term; no photoinhibition."},{"id":5,"unit":3,"title":"Carbon concentration benefit","kind":"c4","xLabel":"Ambient CO₂ proxy","yLabel":"Rubisco CO₂ supply proxy","a":{"label":"Concentration multiplier","value":2,"min":1,"max":5},"b":{"label":"Leakiness (%)","value":15,"min":0,"max":45},"xMin":0,"xMax":500,"warning":"Not a biochemical C4 or CAM cycle; simply illustrates concentration versus leakage."},{"id":6,"unit":4,"title":"Temperature sensitivity of respiration","kind":"q10","xLabel":"Temperature (°C)","yLabel":"Relative respiratory rate","a":{"label":"Q10","value":2,"min":1.2,"max":3.2},"b":{"label":"Reference rate at 20°C","value":1,"min":0.5,"max":3},"xMin":5,"xMax":40,"warning":"Q10 holds only over modest, non-injurious intervals."},{"id":7,"unit":4,"title":"Nighttime starch drawdown","kind":"starch","xLabel":"Hours after dusk","yLabel":"Starch remaining (mg)","a":{"label":"Dusk starch (mg)","value":10,"min":5,"max":25},"b":{"label":"Consumption rate (mg/h)","value":0.7,"min":0.2,"max":2},"xMin":0,"xMax":14,"warning":"Linear store depletion with a zero floor; real starch turnover is circadian-regulated."},{"id":8,"unit":5,"title":"Xylem steady flow","kind":"xylem","xLabel":"Potential difference (MPa)","yLabel":"Volume flux (mL/h)","a":{"label":"Conductance","value":4.5,"min":1,"max":8},"b":{"label":"Functional conduit fraction","value":0.8,"min":0.3,"max":1},"xMin":0,"xMax":1.3,"warning":"No storage flux or embolism accumulation across time."},{"id":9,"unit":5,"title":"Source-to-sink sugar movement","kind":"sugarflux","xLabel":"Phloem flow (mL/h)","yLabel":"Sucrose flux (mmol/h)","a":{"label":"Sucrose concentration (mmol/mL)","value":0.5,"min":0.1,"max":0.9},"b":{"label":"Unloading efficiency","value":0.85,"min":0.4,"max":1},"xMin":0,"xMax":0.2,"warning":"Simple mass balance, ignores complex pressure-flow network."},{"id":10,"unit":6,"title":"Directional growth angle","kind":"curvature","xLabel":"Illumination exposure (hours)","yLabel":"Curvature (degrees)","a":{"label":"Curvature rate (degrees/h)","value":8,"min":2,"max":16},"b":{"label":"Response lag (h)","value":0.6,"min":0,"max":2.5},"xMin":0,"xMax":6,"warning":"Linear growth after delay; hormones and wall properties not explicit."},{"id":11,"unit":6,"title":"ABA-dependent aperture proxy","kind":"aba","xLabel":"Relative ABA signal","yLabel":"Aperture (µm)","a":{"label":"Maximum aperture (µm)","value":9,"min":5,"max":14},"b":{"label":"Response sensitivity","value":1.1,"min":0.3,"max":3},"xMin":0,"xMax":5,"warning":"A bounded phenomenological response, not an ion-channel model."},{"id":12,"unit":7,"title":"Photoperiodic response","kind":"flowering","xLabel":"Night length (h)","yLabel":"Flowering signal (relative)","a":{"label":"Critical night length (h)","value":11,"min":8,"max":16},"b":{"label":"Steepness","value":1.5,"min":0.5,"max":4},"xMin":6,"xMax":18,"warning":"Logistic proxy for one hypothetical short-day response; not universal."},{"id":13,"unit":7,"title":"Seed germination curve","kind":"germination","xLabel":"Days after imbibition","yLabel":"Cumulative germination (%)","a":{"label":"Maximum viable fraction (%)","value":85,"min":50,"max":99},"b":{"label":"Rate parameter (/day)","value":0.6,"min":0.2,"max":1.4},"xMin":0,"xMax":12,"warning":"Simple cumulative exponential, assumes non-dormant responsive seeds."},{"id":14,"unit":8,"title":"Salinity inhibition","kind":"salt","xLabel":"External salt index","yLabel":"Relative growth (%)","a":{"label":"Tolerance scale","value":5,"min":2,"max":10},"b":{"label":"Maximal depression","value":85,"min":30,"max":99},"xMin":0,"xMax":20,"warning":"A dose-response proxy; ion composition, duration and acclimation ignored."},{"id":15,"unit":8,"title":"Combined stress response","kind":"stress","xLabel":"Stress exposure (relative days)","yLabel":"Relative functional capacity (%)","a":{"label":"Recovery factor","value":0.35,"min":0.1,"max":1},"b":{"label":"Damage coefficient","value":0.45,"min":0.1,"max":1},"xMin":0,"xMax":10,"warning":"Toy injury-and-recovery balance, not a field forecast."}];
function predict(m,x){let a=m.a.value,b=m.b.value;switch(m.kind){
case 'osmotic':return -x*0.008314*a*b;
case 'hydraulic':return x*a*b;
case 'uptake':return a*x/(b+x);
case 'diffusion':return a*b/(0.3+x);
case 'lightcurve':return a*x/(b+x)-1.5;
case 'c4':return x*a*(1-b/100);
case 'q10':return b*Math.pow(a,(x-20)/10);
case 'starch':return Math.max(0,a-b*x);
case 'xylem':return x*a*b;
case 'sugarflux':return x*a*b;
case 'curvature':return a*Math.max(0,x-b);
case 'aba':return a/(1+b*x);
case 'flowering':return 1/(1+Math.exp(-b*(x-a)));
case 'germination':return a*(1-Math.exp(-b*x));
case 'salt':return 100-b*x/(a+x);
case 'stress':return 100*Math.max(0,Math.min(1,Math.exp(-b*x)+a*(1-Math.exp(-x/3))));
default:return 0;
}}
const svgNS='http://www.w3.org/2000/svg';
function S(tag,attrs){let el=document.createElementNS(svgNS,tag);for(let [k,v] of Object.entries(attrs||{}))el.setAttribute(k,String(v));return el;}
function draw(el,m){
 const data=[];for(let i=0;i<=80;i++){let x=m.xMin+(m.xMax-m.xMin)*i/80;let y=predict(m,x);if(!Number.isFinite(y)){el.querySelector('[data-summary]').textContent='Model parameters produced a non-finite result.';return;}data.push({x,y});}
 let ymin=Math.min(...data.map(d=>d.y)),ymax=Math.max(...data.map(d=>d.y)),span=ymax-ymin||1;ymin-=span*0.12;ymax+=span*0.12;
 const svg=el.querySelector('svg');svg.replaceChildren();const X=x=>56+(x-m.xMin)/(m.xMax-m.xMin)*524,Y=y=>208-(y-ymin)/(ymax-ymin)*165;
 for(let i=0;i<=4;i++){const y=208-i*165/4;svg.appendChild(S('line',{x1:56,y1:y,x2:580,y2:y,stroke:'#d0e3dd'}));const label=S('text',{x:49,y:y+4,'text-anchor':'end','font-size':11,fill:'#4d625d'});label.textContent=(ymin+(ymax-ymin)*i/4).toPrecision(3);svg.appendChild(label);}
 svg.appendChild(S('polyline',{points:data.map(d=>X(d.x).toFixed(2)+','+Y(d.y).toFixed(2)).join(' '),fill:'none',stroke:'#0b7461','stroke-width':3,'stroke-linecap':'round','stroke-linejoin':'round'}));
 for(let i=0;i<=4;i++){let x=m.xMin+(m.xMax-m.xMin)*i/4;const t=S('text',{x:X(x),y:229,'text-anchor':'middle','font-size':11,fill:'#4d625d'});t.textContent=x.toPrecision(3);svg.appendChild(t)}
 el.querySelector('[data-summary]').textContent='Curve range '+Math.min(...data.map(d=>d.y)).toPrecision(4)+' to '+Math.max(...data.map(d=>d.y)).toPrecision(4)+' ('+m.yLabel+').';
 }
function setup(el,m){
 let fields=document.createElement('div');fields.className='model-controls';
 for(let p of ['a','b']){let d=m[p],wrap=document.createElement('label');wrap.className='model-field';let name=document.createElement('span');name.textContent=d.label;let output=document.createElement('output');output.textContent=d.value;let input=document.createElement('input');input.type='range';input.min=d.min;input.max=d.max;input.step=(d.max-d.min)/100;input.value=d.value;input.setAttribute('aria-label',d.label);input.addEventListener('input',()=>{d.value=Number(input.value);output.textContent=Number(input.value).toPrecision(4);draw(el,m)});wrap.append(name,output,input);fields.appendChild(wrap);}
 const graph=S('svg',{viewBox:'0 0 620 250',role:'img','aria-label':'Interactive plot: '+m.title});graph.style.width='100%';graph.style.height='auto';
 const summary=document.createElement('p');summary.setAttribute('data-summary','');summary.className='small';summary.setAttribute('aria-live','polite');
 el.append(fields,graph,summary);draw(el,m);
}
document.addEventListener('DOMContentLoaded',()=>document.querySelectorAll('[data-model-id]').forEach(el=>{let m=MODELS[Number(el.dataset.modelId)];if(m)setup(el,JSON.parse(JSON.stringify(m)))}));



/* SimulationEngine adapter for Plant Physiology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof MODELS === 'undefined' || typeof setup !== 'function') return;
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
      setup(simBox, JSON.parse(JSON.stringify(m)));
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

