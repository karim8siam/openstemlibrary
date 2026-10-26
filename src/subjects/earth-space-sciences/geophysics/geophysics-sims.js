/* Geophysics Interactive Simulation Suite */
"use strict";
const geophysicalModels=[{"id":"gravity-diff","unit":1,"title":"Acceleration difference","label":"Change in acceleration","input_unit":"m/s²","min":0,"max":0.001,"initial":0.0003,"output_unit":"mGal","js_expression":"x*100000","limitations":"Exactly 1 mGal equals 10^-5 m/s²; reference effects ignored."},{"id":"alias","unit":1,"title":"Ideal sampling requirement","label":"Wavelength","input_unit":"m","min":50,"max":1000,"initial":240,"output_unit":"m","js_expression":"x/2","limitations":"Nyquist half-wavelength threshold for ideal bandlimited signals, not guaranteed field resolution."},{"id":"sp-delay","unit":2,"title":"S minus P arrival lag","label":"Source distance","input_unit":"km","min":1,"max":200,"initial":42,"output_unit":"s","js_expression":"x/3.5-x/6","limitations":"Homogeneous straight-ray approximation only."},{"id":"mw","unit":2,"title":"Moment magnitude from seismic moment","label":"Seismic moment in 10^18 N m","input_unit":"10¹⁸ N m","min":0.01,"max":200,"initial":1,"output_unit":"Mw","js_expression":"(2/3)*(Math.log10(x*1e18)-9.1)","limitations":"Magnitude expression uses SI N m and fixed convention."},{"id":"reflect","unit":3,"title":"Normal-incidence acoustic reflectivity","label":"Second impedance","input_unit":"MRayl","min":5,"max":30,"initial":15,"output_unit":"ratio","js_expression":"(x-10)/(x+10)","limitations":"First impedance fixed at 10 MRayl; simple normal-incidence acoustic case."},{"id":"seismic-depth","unit":3,"title":"Two-way-time seismic depth","label":"Two-way travel time","input_unit":"s","min":0.1,"max":3,"initial":0.8,"output_unit":"m","js_expression":"2500*x/2","limitations":"Constant 2500 m/s vertical speed; no dips or anisotropy."},{"id":"free-air","unit":4,"title":"Free-air correction magnitude","label":"Height above datum","input_unit":"m","min":0,"max":1000,"initial":300,"output_unit":"mGal","js_expression":"0.3086*x","limitations":"First-order 0.3086 mGal/m magnitude only; correction sign set by reduction convention."},{"id":"bouguer","unit":4,"title":"Bouguer slab attraction magnitude","label":"Height of slab","input_unit":"m","min":0,"max":500,"initial":150,"output_unit":"mGal","js_expression":"2*Math.PI*6.67430e-11*2670*x*100000","limitations":"Infinite slab and density 2670 kg/m³, omits terrain."},{"id":"induced","unit":5,"title":"Induced magnetization","label":"Magnetic field strength","input_unit":"A/m","min":0,"max":70,"initial":40,"output_unit":"A/m","js_expression":"0.02*x","limitations":"Scalar susceptibility fixed at 0.02; remanence absent."},{"id":"half-rate","unit":5,"title":"Half-spreading distance","label":"Duration","input_unit":"Ma","min":0,"max":20,"initial":3,"output_unit":"km","js_expression":"24*x","limitations":"Fixed 24 km/Ma rate; no reversal-correlation error."},{"id":"wenner","unit":6,"title":"Wenner apparent resistivity","label":"Electrode separation","input_unit":"m","min":1,"max":20,"initial":5,"output_unit":"ohm m","js_expression":"2*Math.PI*x*0.12/0.01","limitations":"Fixed current/voltage and ideal geometry; result apparent, not a layer property."},{"id":"skin","unit":6,"title":"EM half-space skin depth","label":"Frequency","input_unit":"Hz","min":10,"max":10000,"initial":1000,"output_unit":"m","js_expression":"503*Math.sqrt(100/x)","limitations":"Nonmagnetic uniform half-space, resistivity 100 ohm m."},{"id":"heat-flux","unit":7,"title":"Conduction heat-flux magnitude","label":"Geothermal gradient","input_unit":"K/km","min":1,"max":60,"initial":25,"output_unit":"W/m²","js_expression":"2.5*x/1000","limitations":"One-dimensional steady-state conduction; fixed thermal conductivity 2.5 W/(m K)."},{"id":"strain","unit":7,"title":"Baseline extension strain rate","label":"Annual separation","input_unit":"mm/yr","min":0,"max":10,"initial":2,"output_unit":"1/yr","js_expression":"(x/1000)/50000","limitations":"50 km static baseline, one-dimensional rate only."},{"id":"chi","unit":8,"title":"Normalized least-squares misfit","label":"Second normalized residual","input_unit":"standard deviations","min":0,"max":5,"initial":3,"output_unit":"ratio","js_expression":"4+x*x","limitations":"Assumes one fixed normalized residual of 2 and independent standard errors."},{"id":"holdout","unit":8,"title":"Prediction error reduction","label":"New holdout error","input_unit":"mGal","min":2,"max":12,"initial":9,"output_unit":"%","js_expression":"100*(12-x)/12","limitations":"Baseline prediction error fixed 12 mGal; no confidence interval."}];
function geophysicalValue(m,x){
 const fn=new Function('x','"use strict";return ('+m.js_expression+');');
 return Number(fn(x));
}
function fmtGeo(y){return Number.isFinite(y)?Number(y).toLocaleString('en-US',{maximumSignificantDigits:6}):'undefined';}
function initGeo(){
 document.querySelectorAll('[data-geophysical-id]').forEach(panel=>{
  const m=geophysicalModels.find(e=>e.id===panel.dataset.geophysicalId);if(!m)return;
  const control=panel.querySelector('input');const readout=panel.querySelector('output');const path=panel.querySelector('polyline');
  const ymin=Math.min(...Array.from({length:81},(_,i)=>geophysicalValue(m,m.min+(m.max-m.min)*i/80)));
  const ymax=Math.max(...Array.from({length:81},(_,i)=>geophysicalValue(m,m.min+(m.max-m.min)*i/80)));
  const dy=Math.max(Math.abs(ymax-ymin),1e-12);
  const pts=Array.from({length:81},(_,i)=>{const x=m.min+(m.max-m.min)*i/80; const y=geophysicalValue(m,x);return `${20+460*i/80},${124-104*(y-ymin)/dy}`}).join(' ');
  if(path)path.setAttribute('points',pts);
  function update(){const x=Number(control.value);const y=geophysicalValue(m,x);readout.textContent=fmtGeo(y)+' '+m.output_unit+' (input '+fmtGeo(x)+' '+m.input_unit+')';}
  control.addEventListener('input',update);update();
 });
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initGeo);else initGeo();



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

