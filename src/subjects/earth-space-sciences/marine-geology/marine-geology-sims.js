/* Marine Geology Interactive Simulation Suite */
"use strict";
const marineModels=[{"id": "sound-depth", "unit": 1, "title": "Sounding depth from echo return", "label": "Two-way travel time", "input_unit": "s", "min": 0.5, "max": 8, "initial": 3, "output_unit": "m", "js_expression": "1500*x/2", "limitations": "Uniform 1500 m/s sound speed; vertical geometry and no refraction."}, {"id": "profile-depth", "unit": 1, "title": "Sub-bottom acoustic conversion", "label": "Two-way reflection time", "input_unit": "s", "min": 0.05, "max": 0.5, "initial": 0.18, "output_unit": "m", "js_expression": "1600*x/2", "limitations": "Uniform 1600 m/s sediment velocity; not a calibrated depth conversion."}, {"id": "spreading", "unit": 2, "title": "Half-spreading distance", "label": "Millions of years", "input_unit": "Ma", "min": 0, "max": 50, "initial": 10, "output_unit": "km", "js_expression": "25*x", "limitations": "Constant half-spreading rate 25 km/Ma; no plate changes."}, {"id": "plate-motion", "unit": 2, "title": "Displacement along a fault", "label": "Time interval", "input_unit": "Ma", "min": 0, "max": 4, "initial": 1, "output_unit": "km", "js_expression": "30*x", "limitations": "Constant relative slip 30 km/Ma distributed on the chosen ideal fault."}, {"id": "shelf-flux", "unit": 3, "title": "Shelf sediment balance", "label": "Annual export", "input_unit": "Mt/yr", "min": 0, "max": 12, "initial": 4, "output_unit": "Mt/yr", "js_expression": "12-x-3", "limitations": "Constant input 12 and burial 3 Mt/yr; residual need not equal real storage."}, {"id": "canyon-travel", "unit": 3, "title": "Ideal canyon travel time", "label": "Current speed", "input_unit": "m/s", "min": 0.2, "max": 5, "initial": 2, "output_unit": "hours", "js_expression": "18000/(x*3600)", "limitations": "Fixed 18-km path and steady speed; no acceleration or deposition."}, {"id": "phi", "unit": 4, "title": "Grain diameter in phi scale", "label": "Grain size", "input_unit": "mm", "min": 0.063, "max": 2, "initial": 0.25, "output_unit": "phi", "js_expression": "-Math.log2(x)", "limitations": "Ideal log scale; shape and flocculation not represented."}, {"id": "porosity", "unit": 4, "title": "Two-phase bulk sediment density", "label": "Porosity fraction", "input_unit": "fraction", "min": 0, "max": 0.8, "initial": 0.5, "output_unit": "g/cm³", "js_expression": "2.65*(1-x)+1.03*x", "limitations": "Single grain and fluid density; no gas or mineral variability."}, {"id": "accumulation", "unit": 5, "title": "Idealized sediment accumulation", "label": "Accumulation duration", "input_unit": "ka", "min": 1, "max": 60, "initial": 20, "output_unit": "m", "js_expression": "0.15*x", "limitations": "Constant rate 15 cm/ka and no hiatus or compaction."}, {"id": "proxy", "unit": 5, "title": "Measured isotope contrast", "label": "Comparison measurement", "input_unit": "per mil", "min": -1, "max": 5, "initial": 1.3, "output_unit": "per mil", "js_expression": "2.3-x", "limitations": "Measured ratio difference only; not temperature calibration."}, {"id": "shear", "unit": 6, "title": "Ideal driving shear stress", "label": "Slope angle", "input_unit": "degrees", "min": 0, "max": 20, "initial": 5, "output_unit": "Pa", "js_expression": "900*9.81*5*Math.sin(x*Math.PI/180)*Math.cos(x*Math.PI/180)", "limitations": "Uniform infinite-slope geometry; excludes strength and pore pressure."}, {"id": "wave", "unit": 6, "title": "Ideal long-wave speed", "label": "Water depth", "input_unit": "m", "min": 100, "max": 6000, "initial": 4000, "output_unit": "m/s", "js_expression": "Math.sqrt(9.81*x)", "limitations": "Shallow-water limit only; never for emergency warnings."}, {"id": "vent-mixing", "unit": 7, "title": "Conservative vent-water mixture", "label": "Vent-water fraction", "input_unit": "fraction", "min": 0, "max": 1, "initial": 0.2, "output_unit": "µmol/kg", "js_expression": "500*x+2*(1-x)", "limitations": "Conservative ideal tracer; ignores exchange and precipitation."}, {"id": "nodule-age", "unit": 7, "title": "Conceptual nodule layer growth time", "label": "Layer thickness", "input_unit": "mm", "min": 0, "max": 30, "initial": 15, "output_unit": "Ma", "js_expression": "x/3", "limitations": "Constant rate 3 mm/Ma; growth not necessarily continuous."}, {"id": "coverage", "unit": 8, "title": "Gross bathymetric survey area", "label": "Usable swath width", "input_unit": "km", "min": 0.5, "max": 6, "initial": 2.5, "output_unit": "km²", "js_expression": "72*x", "limitations": "Fixed 72-km effective track length; overlap omitted."}, {"id": "uncertainty", "unit": 8, "title": "Independent depth uncertainty combination", "label": "Second random uncertainty", "input_unit": "m", "min": 0, "max": 20, "initial": 4, "output_unit": "m", "js_expression": "Math.sqrt(3*3+x*x)", "limitations": "Independent zero-mean errors; systematic datum bias excluded."}];
function numFmt(x) { return Number.isFinite(x) ? Number(x).toLocaleString('en-US',{maximumSignificantDigits:5}):'undefined'; }
function computeMarine(m,x) {
  const fn=new Function('x','"use strict"; return ('+m.js_expression+');');
  return fn(x);
}
function graphMarine(m) {
  const pts=[]; for(let i=0;i<=60;i++){const x=m.min+(m.max-m.min)*i/60;const y=computeMarine(m,x); if(Number.isFinite(y)) pts.push([x,y]);}
  const ys=pts.map(p=>p[1]);const low=Math.min(...ys), high=Math.max(...ys), span=high-low || 1;
  return pts.map(([x,y],i)=>(i?'L':'M')+(12+(x-m.min)/(m.max-m.min)*480).toFixed(1)+','+(116-(y-low)/span*96).toFixed(1)).join(' ');
}
function setupMarine() {
 for(const m of marineModels) {
   const el=document.getElementById('model-'+m.id); if(!el)continue;
   const range=el.querySelector('input'),output=el.querySelector('output'),mark=el.querySelector('.marker');
   const draw=()=>{const x=Number(range.value),y=computeMarine(m,x);output.textContent=numFmt(y)+' '+m.output_unit;
    range.setAttribute('aria-valuetext',numFmt(x)+' '+m.input_unit);mark.setAttribute('cx',12+(x-m.min)/(m.max-m.min)*480); const vals=Array.from({length:61},(_,i)=>computeMarine(m,m.min+(m.max-m.min)*i/60));const low=Math.min(...vals),high=Math.max(...vals);mark.setAttribute('cy',116-(y-low)/((high-low)||1)*96);};
   el.querySelector('.curve').setAttribute('d',graphMarine(m));range.addEventListener('input',draw);draw();
 }
}
document.addEventListener('DOMContentLoaded',setupMarine);



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

