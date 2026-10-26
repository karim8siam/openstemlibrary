/* Paleontology Interactive Simulation Suite */
"use strict";
const allPaleoModels = [{"id": "sample-preservation", "unit": 1, "title": "Preserved fossils under ideal sampling", "label": "Estimated preservation/detection probability", "input_unit": "probability", "min": 0.01, "max": 1, "initial": 0.25, "output_unit": "expected preserved from 200", "js_expression": "200*x", "limitations": "Assumes equal independent preservation and detection; geological sampling is usually heterogeneous."}, {"id": "sedimentation", "unit": 1, "title": "Illustrative sediment accumulation time", "label": "Sedimentary package thickness", "input_unit": "m", "min": 1, "max": 60, "initial": 12, "output_unit": "duration (kyr) at 2 cm/kyr", "js_expression": "x/0.02", "limitations": "Uses a fixed 2 cm/kyr net accumulation rate; hiatuses and compaction excluded."}, {"id": "articulation", "unit": 2, "title": "Articulated specimens in a count", "label": "Articulation percentage", "input_unit": "%", "min": 0, "max": 100, "initial": 60, "output_unit": "articulated out of 80", "js_expression": "80*x/100", "limitations": "Samples a defined assemblage, not universal taphonomic conditions."}, {"id": "decay", "unit": 2, "title": "Illustrative exponential soft-tissue survival", "label": "Elapsed decay time", "input_unit": "days", "min": 0, "max": 30, "initial": 5, "output_unit": "surviving tissue fraction", "js_expression": "Math.exp(-0.18*x)", "limitations": "Hypothetical constant rate, not an empirical fit to any organism."}, {"id": "trait-distance", "unit": 3, "title": "Morphological difference in two standardized traits", "label": "Difference in trait 1", "input_unit": "standard deviations", "min": 0, "max": 4, "initial": 1, "output_unit": "two-trait Euclidean distance (trait 2 = 1)", "js_expression": "Math.sqrt(x*x+1)", "limitations": "Equal weighting and already-standardized independent traits assumed."}, {"id": "character-count", "unit": 3, "title": "Minimum parsimony changes", "label": "Observed extra character steps", "input_unit": "changes", "min": 0, "max": 20, "initial": 3, "output_unit": "total tree length (baseline 12)", "js_expression": "12+x", "limitations": "Demonstrates simple additive scoring; tree search and uncertainty omitted."}, {"id": "relative-abundance", "unit": 4, "title": "Microfossil relative abundance", "label": "Count of focal form", "input_unit": "count", "min": 0, "max": 200, "initial": 80, "output_unit": "percent among 200 total", "js_expression": "100*x/200", "limitations": "Fixed counting effort and unambiguous identification assumed."}, {"id": "evenness", "unit": 4, "title": "Two-class Simpson diversity", "label": "Fraction in taxon A", "input_unit": "proportion", "min": 0, "max": 1, "initial": 0.6, "output_unit": "Gini\u2013Simpson (1 - \u03a3p\u00b2)", "js_expression": "1-(x*x+(1-x)*(1-x))", "limitations": "Only two classes and abundance-weighted diversity; not richness itself."}, {"id": "lever-torque", "unit": 5, "title": "Simplified joint torque", "label": "Lever force", "input_unit": "newtons", "min": 0, "max": 1000, "initial": 200, "output_unit": "torque (N m) at 0.15 m", "js_expression": "0.15*x", "limitations": "Force acts perpendicular to the lever; muscle geometry ignored."}, {"id": "stride-index", "unit": 5, "title": "Stride-to-hip-height ratio", "label": "Stride length", "input_unit": "m", "min": 0.2, "max": 5, "initial": 1.6, "output_unit": "dimensionless stride ratio at 0.9 m hip", "js_expression": "x/0.9", "limitations": "Does not estimate speed reliably without a validated locomotion model."}, {"id": "pollen", "unit": 6, "title": "Pollen share in a fixed slide count", "label": "Identified focal pollen grains", "input_unit": "count", "min": 0, "max": 300, "initial": 110, "output_unit": "percent of 300 counted", "js_expression": "100*x/300", "limitations": "Production and transport biases remain; percent is not biomass."}, {"id": "foodweb", "unit": 6, "title": "Food-web connectance", "label": "Directed trophic links", "input_unit": "links", "min": 0, "max": 30, "initial": 12, "output_unit": "connectance out of 30 possible", "js_expression": "x/30", "limitations": "Fixed number of potential links; directed network rules specified for this exercise."}, {"id": "extinction", "unit": 7, "title": "Apparent taxon loss across a boundary", "label": "Surviving taxa", "input_unit": "taxa", "min": 0, "max": 100, "initial": 66, "output_unit": "loss fraction from 100 baseline", "js_expression": "1-x/100", "limitations": "Uses observed bin inventories, not unbiased true biological extinction."}, {"id": "recovery", "unit": 7, "title": "Illustrative diversity recovery curve", "label": "Time since hypothetical disturbance", "input_unit": "Myr", "min": 0, "max": 20, "initial": 3, "output_unit": "fraction of asymptotic recovery", "js_expression": "1-Math.exp(-x/6)", "limitations": "Exponential toy function; recovery varies with taxa, region, environment."}, {"id": "missing-meta", "unit": 8, "title": "Provenance metadata completeness", "label": "Missing metadata entries", "input_unit": "entries", "min": 0, "max": 50, "initial": 8, "output_unit": "complete entries out of 50", "js_expression": "50-x", "limitations": "Equal item weights and exactly fifty entries are assumed."}, {"id": "binomial", "unit": 8, "title": "Binomial standard error of a sampled proportion", "label": "Observed proportion", "input_unit": "fraction", "min": 0.01, "max": 0.99, "initial": 0.4, "output_unit": "approximate SE (n = 100)", "js_expression": "Math.sqrt(x*(1-x)/100)", "limitations": "Requires independent Bernoulli trials; fossil occurrences are often clustered."}];
const computations = {
  "sample-preservation": x => (200*x),
  "sedimentation": x => (x/0.02),
  "articulation": x => (80*x/100),
  "decay": x => (Math.exp(-0.18*x)),
  "trait-distance": x => (Math.sqrt(x*x+1)),
  "character-count": x => (12+x),
  "relative-abundance": x => (100*x/200),
  "evenness": x => (1-(x*x+(1-x)*(1-x))),
  "lever-torque": x => (0.15*x),
  "stride-index": x => (x/0.9),
  "pollen": x => (100*x/300),
  "foodweb": x => (x/30),
  "extinction": x => (1-x/100),
  "recovery": x => (1-Math.exp(-x/6)),
  "missing-meta": x => (50-x),
  "binomial": x => (Math.sqrt(x*(1-x)/100))
};
function graphFor(model, fn, value){
  const samples=Array.from({length:51},(_,i)=>{
    let x=model.min+(model.max-model.min)*i/50;
    let y=fn(x);
    return {x,y};
  }).filter(p=>Number.isFinite(p.y));
  if(!samples.length) return '';
  const lo=Math.min(...samples.map(p=>p.y)),hi=Math.max(...samples.map(p=>p.y));
  const dy=Math.max(hi-lo,1e-9),dx=model.max-model.min;
  const X=x=>14+492*(x-model.min)/dx;
  const Y=y=>115-96*(y-lo)/dy;
  let d=samples.map((p,i)=>(i?'L':'M')+X(p.x).toFixed(2)+' '+Y(p.y).toFixed(2)).join(' ');
  const cy=fn(value);
  return '<path d="'+d+'" fill="none" stroke="#08778c" stroke-width="3"/>'+
   '<circle cx="'+X(value).toFixed(2)+'" cy="'+Y(cy).toFixed(2)+'" r="5" fill="#ba5a22"/>';
}
function activateModels(){
  const mapping=new Map(allPaleoModels.map(m=>[m.id,m]));
  for(const box of document.querySelectorAll('.model[data-model]')){
    const id=box.dataset.model,model=mapping.get(id),fn=computations[id];
    if(!model||!fn) continue;
    const input=box.querySelector('input[type=range]'),display=box.querySelector('output'),svg=box.querySelector('svg');
    if(!input||!display||!svg) continue;
    const update=()=>{
      const v=Number(input.value),y=fn(v);
      display.textContent=Number.isFinite(y) ? y.toPrecision(5)+' '+model.output_unit : 'Undefined for these assumptions';
      input.setAttribute('aria-valuetext',v+' '+model.input_unit);
      svg.innerHTML=graphFor(model,fn,v);
    };
    input.addEventListener('input',update);
    update();
  }
}
document.addEventListener('DOMContentLoaded',activateModels);



/* SimulationEngine adapter for Earth & Space Sciences */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof MODELS === 'undefined' || typeof compute !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var unitModels = MODELS.filter(function(m){ return m.unit === u; });
    if (!unitModels.length) unitModels = [MODELS[0]];
    unitModels.forEach(function(m) {
      var section = document.createElement('section');
      section.className = 'sim-card model';
      section.dataset.model = m.id;
      var titleText = m.name || m.title || m.label || 'Interactive Model';
      var exprText = m.expression || m.formula || '';
      var inUnit = m.input_unit || m.unit || '';
      var outUnit = m.output_unit || m.result_unit || '';
      var minVal = m.min !== undefined ? m.min : 0;
      var maxVal = m.max !== undefined ? m.max : 100;
      var initVal = m.initial !== undefined ? m.initial : (minVal + maxVal)/2;
      var stepVal = m.step || ((maxVal - minVal) / 100) || 1;
      
      section.innerHTML = '<h4>' + titleText + '</h4>' +
        (exprText ? '<p class="formula"><code>' + exprText + '</code></p>' : '') +
        '<label>' + (m.label || 'Input') + (inUnit ? ' (' + inUnit + ')' : '') + ':<br>' +
        '<input type="range" min="' + minVal + '" max="' + maxVal + '" step="' + stepVal + '" value="' + initVal + '">' +
        '</label>' +
        '<p>Output: <output style="color:#38bdf8;font-weight:600;"></output></p>' +
        '<svg viewBox="0 0 500 180" style="width:100%;height:auto;background:#0f172a;border:1px solid #1e293b;border-radius:8px;"></svg>' +
        '<p class="readout">' + (m.note || m.notes || m.description || m.limitations || '') + '</p>';
      host.appendChild(section);
      
      var input = section.querySelector('input');
      var output = section.querySelector('output');
      var plot = section.querySelector('svg');
      
      function update() {
        var x = Number(input.value);
        var y = compute(m.id, x);
        var prettyY = (typeof pretty === 'function') ? pretty(y) : (Number.isFinite(y) ? y.toLocaleString() : 'out of range');
        output.textContent = prettyY + (outUnit ? ' ' + outUnit : '');
        var pts = [];
        var lo = Infinity, hi = -Infinity;
        for (var i = 0; i <= 80; i++) {
          var xx = minVal + (maxVal - minVal) * i / 80;
          var yy = compute(m.id, xx);
          if (!Number.isFinite(yy)) continue;
          pts.push([xx, yy]);
          lo = Math.min(lo, yy);
          hi = Math.max(hi, yy);
        }
        var span = hi - lo || 1;
        var coords = pts.map(function(p){
          return [ (p[0] - minVal) / (maxVal - minVal || 1) * 440 + 38, 142 - (p[1] - lo) / span * 114 ];
        });
        var poly = coords.map(function(c){ return c[0].toFixed(2) + ',' + c[1].toFixed(2); }).join(' ');
        var cx = ((x - minVal) / (maxVal - minVal || 1) * 440 + 38).toFixed(2);
        var cy = (142 - (y - lo) / span * 114).toFixed(2);
        plot.innerHTML = '<line x1="38" y1="142" x2="478" y2="142" stroke="#475569"/>' +
          '<line x1="38" y1="15" x2="38" y2="142" stroke="#475569"/>' +
          '<polyline fill="none" stroke="#38bdf8" stroke-width="3" points="' + poly + '"/>' +
          '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="#f97316"/>' +
          '<text x="40" y="165" fill="#94a3b8" font-size="12">' + minVal + (inUnit ? ' ' + inUnit : '') + '</text>' +
          '<text x="370" y="165" fill="#94a3b8" font-size="12">' + maxVal + (inUnit ? ' ' + inUnit : '') + '</text>';
        plot.setAttribute('aria-label', titleText + ': current input ' + x + ', output ' + prettyY);
      }
      input.addEventListener('input', update);
      update();
    });
  };
})(typeof window === 'undefined' ? globalThis : window);

