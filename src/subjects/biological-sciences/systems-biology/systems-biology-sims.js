/* Systems Biology Interactive Simulation Suite */
"use strict";
// OpenSTEM Book 20 teaching visualizations: idealized deterministic formulas only.
const modelFuncs = {
  "sb-01": (x) => 1-Math.exp(-x/3),
  "sb-02": (x) => x/(x+2),
  "sb-03": (x) => x/(x+5),
  "sb-04": (x) => x*x/(16+x*x),
  "sb-05": (x) => Math.exp(-0.24*x),
  "sb-06": (x) => 1/(1+x),
  "sb-07": (x) => Math.min(5,x/2),
  "sb-08": (x) => x/(1+x),
  "sb-09": (x) => Math.exp(-x),
  "sb-10": (x) => 1/Math.sqrt(x),
  "sb-11": (x) => 2+8*x,
  "sb-12": (x) => Math.sqrt(x/0.25),
  "sb-13": (x) => 20*Math.exp(-0.14*x),
  "sb-14": (x) => x/(x+3),
  "sb-15": (x) => 0.05+0.90*x*x,
  "sb-16": (x) => 0.2+0.6*x,
};
const modelDefs = [{"id":"sb-01","unit":1,"title":"Finite boundary response","sliderLabel":"Input intensity","expression":"1-exp(-x/3)","min":0,"max":12,"default":4,"sliderUnit":"arbitrary input","outputUnit":"saturating response","description":"A finite-capacity idealized response; true ligand depletion would require an external-pool state."},{"id":"sb-02","unit":1,"title":"Reporter background","sliderLabel":"Signal-to-background ratio","expression":"x/(x+2)","min":0,"max":12,"default":3,"sliderUnit":"ratio","outputUnit":"fraction","description":"A dimensionless illustration of improving contrast; it is not an assay calibration."},{"id":"sb-03","unit":2,"title":"Interaction coverage","sliderLabel":"Recorded-edge opportunity","expression":"x/(x+5)","min":0,"max":20,"default":8,"sliderUnit":"hypothetical edges","outputUnit":"index","description":"Observing more interactions does not automatically increase biological validity."},{"id":"sb-04","unit":2,"title":"Cooperative regulatory response","sliderLabel":"Input concentration","expression":"x*x/(16+x*x)","min":0,"max":12,"default":4,"sliderUnit":"relative units","outputUnit":"fraction","description":"A Hill-like steady response, which alone does not establish a bistable system."},{"id":"sb-05","unit":3,"title":"First-order clearance","sliderLabel":"Time","expression":"exp(-0.24*x)","min":0,"max":20,"default":5,"sliderUnit":"minutes","outputUnit":"fraction remaining","description":"First-order decay with no source and constant rate."},{"id":"sb-06","unit":3,"title":"Idealized feedback attenuation","sliderLabel":"Loop gain","expression":"1/(1+x)","min":0,"max":12,"default":3,"sliderUnit":"dimensionless","outputUnit":"sensitivity fraction","description":"A static small-signal analogy without delays or dynamical oscillation."},{"id":"sb-07","unit":4,"title":"Nutrient-limited capacity","sliderLabel":"Available substrate","expression":"min(5,x/2)","min":0,"max":14,"default":6,"sliderUnit":"substrate flux","outputUnit":"objective units","description":"Toy carbon demand and an independent capacity bound; not a reconstructed organism."},{"id":"sb-08","unit":4,"title":"Alternate-pathway allocation","sliderLabel":"Preference weight","expression":"x/(1+x)","min":0,"max":12,"default":3,"sliderUnit":"relative","outputUnit":"fraction","description":"A hypothetical split between parallel pathways, not flux variability analysis."},{"id":"sb-09","unit":5,"title":"Zero-count probability","sliderLabel":"Stationary expected count","expression":"exp(-x)","min":0,"max":12,"default":3,"sliderUnit":"molecules","outputUnit":"probability","description":"Poisson benchmark probability of a zero count at a chosen mean."},{"id":"sb-10","unit":5,"title":"Count relative variation","sliderLabel":"Mean molecule count","expression":"1/sqrt(x)","min":0.5,"max":25,"default":5,"sliderUnit":"molecules","outputUnit":"coefficient of variation","description":"Poisson relative variability; bursty and extrinsic noise need richer models."},{"id":"sb-11","unit":6,"title":"Mixture-average reporter","sliderLabel":"High-response cell fraction","expression":"2+8*x","min":0,"max":1,"default":0.35,"sliderUnit":"fraction","outputUnit":"relative abundance","description":"Bulk signal from low state 2 and high state 10 without within-state regulation."},{"id":"sb-12","unit":6,"title":"Diffusion length scale","sliderLabel":"Diffusion coefficient","expression":"sqrt(x/0.25)","min":0.1,"max":9,"default":4,"sliderUnit":"length\u00b2/time","outputUnit":"length units","description":"Simple linear diffusion\u2013degradation length scale with fixed loss constant."},{"id":"sb-13","unit":7,"title":"Fitted exponential signal","sliderLabel":"Elapsed time","expression":"20*exp(-0.14*x)","min":0,"max":15,"default":5,"sliderUnit":"minutes","outputUnit":"signal units","description":"An arbitrary calibrated decay prediction at one fixed parameter value."},{"id":"sb-14","unit":7,"title":"Saturating sensitivity","sliderLabel":"Resource amount","expression":"x/(x+3)","min":0.1,"max":14,"default":4,"sliderUnit":"relative resource","outputUnit":"fraction","description":"A response becomes less sensitive near saturation; derivative importance varies with x."},{"id":"sb-15","unit":8,"title":"Synthetic circuit leakage","sliderLabel":"Normalized input","expression":"0.05+0.90*x*x","min":0,"max":1,"default":0.65,"sliderUnit":"fraction","outputUnit":"relative output","description":"An illustrative gate with basal leakage, not a validated engineered device."},{"id":"sb-16","unit":8,"title":"Population-average response","sliderLabel":"High-response population fraction","expression":"0.2+0.6*x","min":0,"max":1,"default":0.4,"sliderUnit":"fraction","outputUnit":"mean response","description":"Average conceals subgroup disparity and does not represent a clinical recommendation."}];
function graphPoly(model, fun, currentX) {
  const xs=Array.from({length:81},(_,i)=>model.min+(model.max-model.min)*i/80);
  const ys=xs.map(x=>fun(x));
  if(!ys.every(Number.isFinite))return null;
  let low=Math.min(0,...ys),high=Math.max(...ys);
  if(high===low){high+=1;low-=1;}
  const coords=ys.map((y,i)=>`${(15+320*i/80).toFixed(2)},${(130-108*(y-low)/(high-low)).toFixed(2)}`).join(' ');
  const val=fun(currentX);
  return {coords,val,cx:15+320*(currentX-model.min)/(model.max-model.min),cy:130-108*(val-low)/(high-low),low,high};
}
function initModels(){
  document.querySelectorAll('[data-model]').forEach(card=>{
    const model=modelDefs.find(m=>m.id===card.dataset.model);
    if(!model) return;
    const fun=modelFuncs[model.id], slider=card.querySelector('input[type=range]');
    const output=card.querySelector('output'), svg=card.querySelector('svg');
    const poly=svg.querySelector('polyline'),point=svg.querySelector('circle');
    const render=()=>{
      const x=Number(slider.value),data=graphPoly(model,fun,x);
      if(!data){output.textContent='Invalid domain';return;}
      poly.setAttribute('points',data.coords);
      point.setAttribute('cx',data.cx);point.setAttribute('cy',data.cy);
      output.textContent=`Input ${x.toFixed(2)} ${model.sliderUnit}; result ${data.val.toFixed(4)} ${model.outputUnit}`;
      slider.setAttribute('aria-valuetext',`${x.toFixed(2)} ${model.sliderUnit}`);
      svg.setAttribute('aria-label',`${model.title}: value ${data.val.toFixed(4)} ${model.outputUnit} for input ${x.toFixed(2)}`);
    };
    slider.addEventListener('input',render);
    slider.addEventListener('change',render);
    render();
  });
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initModels);else initModels();



/* SimulationEngine adapter for Systems Biology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof modelDefs === 'undefined' || typeof modelFuncs === 'undefined' || typeof graphPoly !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var m = modelDefs.filter(function(x){ return x.unit === u; })[0] || modelDefs[0];
    if (m) {
      var card = document.createElement('div');
      card.className = 'sim-card';
      card.dataset.model = m.id;
      card.innerHTML = '<h4>' + m.title + '</h4>' +
        '<p class="formula"><code>' + m.expression + '</code></p>' +
        '<label>' + m.sliderLabel + ' (' + m.sliderUnit + '):<br><input type="range" min="' + m.min + '" max="' + m.max + '" step="' + ((m.max-m.min)/100) + '" value="' + m.default + '"></label>' +
        '<output style="display:block;margin:0.5rem 0;font-weight:600;color:#38bdf8;"></output>' +
        '<svg viewBox="0 0 350 150" style="width:100%;height:auto;background:#0f172a;border:1px solid #1e293b;border-radius:8px;"><polyline fill="none" stroke="#38bdf8" stroke-width="2.5"/><circle r="5" fill="#f97316"/></svg>' +
        '<p class="readout">' + (m.description || '') + '</p>';
      host.appendChild(card);
      var fun = modelFuncs[m.id], slider = card.querySelector('input[type=range]');
      var output = card.querySelector('output'), svg = card.querySelector('svg');
      var poly = svg.querySelector('polyline'), point = svg.querySelector('circle');
      var render = function() {
        var x = Number(slider.value), data = graphPoly(m, fun, x);
        if (!data) { output.textContent = 'Invalid domain'; return; }
        poly.setAttribute('points', data.coords);
        point.setAttribute('cx', data.cx); point.setAttribute('cy', data.cy);
        output.textContent = 'Input ' + x.toFixed(2) + ' ' + m.sliderUnit + ' → ' + data.val.toFixed(4) + ' ' + m.outputUnit;
      };
      slider.addEventListener('input', render);
      render();
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

