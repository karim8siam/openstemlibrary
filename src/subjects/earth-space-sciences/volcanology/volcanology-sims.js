/* Volcanology Interactive Simulation Suite */
(()=>{
"use strict";
const modelList=[{"id": "plate-motion", "unit": 1, "title": "Plate displacement over two million years", "label": "Assumed plate speed", "input_unit": "mm/year", "min": 1, "max": 120, "initial": 42, "output_unit": "km in 2 million years", "js_expression": "2*x", "limitations": "Rigid constant-rate movement: not a measured subduction history."}, {"id": "surface-slope", "unit": 1, "title": "Apparent edifice slope from rise and run", "label": "Vertical rise over 1 km", "input_unit": "m", "min": 0, "max": 700, "initial": 240, "output_unit": "slope angle (degrees)", "js_expression": "Math.atan(x/1000)*180/Math.PI", "limitations": "Ignores edifice curvature, mapped area, datum and erosion."}, {"id": "melt-window", "unit": 2, "title": "Illustrative fraction melted between solidus and liquidus", "label": "Temperature", "input_unit": "degrees Celsius", "min": 900, "max": 1400, "initial": 1120, "output_unit": "melt fraction", "js_expression": "Math.max(0,Math.min(1,(x-950)/350))", "limitations": "Linear interpolation is a teaching approximation, not a real multi-phase melt model."}, {"id": "viscosity", "unit": 2, "title": "Fixed-composition illustrative melt viscosity", "label": "Melt temperature", "input_unit": "degrees Celsius", "min": 900, "max": 1350, "initial": 1160, "output_unit": "dynamic viscosity (Pa s)", "js_expression": "1e5*Math.exp(150000/8.314*(1/(x+273.15)-1/1473.15))", "limitations": "Arrhenius example only; crystals, shear rate, gases and composition held fixed."}, {"id": "gas-expansion", "unit": 3, "title": "Idealized isothermal gas expansion", "label": "Pressure", "input_unit": "MPa", "min": 0.5, "max": 60, "initial": 15, "output_unit": "volume multiple relative to 20 MPa", "js_expression": "20/x", "limitations": "Ideal gas: no gas dissolution, non-ideal compressibility or temperature change."}, {"id": "ascent", "unit": 3, "title": "Constant-speed ascent from five kilometres depth", "label": "Rise speed", "input_unit": "m/s", "min": 0.05, "max": 5, "initial": 0.7, "output_unit": "ascent travel time (hours)", "js_expression": "5000/(x*3600)", "limitations": "No acceleration, conduit changes, friction or episodic arrest; not a forecast."}, {"id": "effusion", "unit": 4, "title": "Toy lava eruption volume over one day", "label": "Mean effusion rate", "input_unit": "m³/s", "min": 1, "max": 500, "initial": 60, "output_unit": "daily erupted volume (m³)", "js_expression": "86400*x", "limitations": "Assumes constant output and ignores density and void changes."}, {"id": "lava-travel", "unit": 4, "title": "Toy lava travel time at fixed speed", "label": "Path length", "input_unit": "km", "min": 0.1, "max": 8, "initial": 2.2, "output_unit": "travel time (hours)", "js_expression": "x*1000/(0.5*60)", "limitations": "Imposed 0.5 m/min speed: NOT usable for lava-flow prediction."}, {"id": "tephra-loading", "unit": 5, "title": "Dry tephra mass per square metre", "label": "Deposit thickness", "input_unit": "cm", "min": 0, "max": 30, "initial": 6, "output_unit": "dry load (kg/m²)", "js_expression": "10*x", "limitations": "Assumes constant bulk density 1000 kg/m³; wet loads and roofs vary."}, {"id": "ash-settling", "unit": 5, "title": "Stokes settling speed for ideal spherical ash", "label": "Grain diameter", "input_unit": "micrometres", "min": 5, "max": 35, "initial": 18, "output_unit": "terminal settling speed (m/s)", "js_expression": "(2300-1.2)*9.81*Math.pow(x*1e-6,2)/(18*1.8e-5)", "limitations": "Low-Re, still air, nonaggregated spherical grain; not an aviation calculation."}, {"id": "lahar-time", "unit": 6, "title": "Illustrative lahar travel time at constant speed", "label": "Travel distance", "input_unit": "km", "min": 1, "max": 30, "initial": 10, "output_unit": "time (hours)", "js_expression": "x/18", "limitations": "Assumes a constant 5 m/s with no channel or rheological effects; not evacuation guidance."}, {"id": "pdc-energy", "unit": 6, "title": "Specific kinetic energy in an idealized moving mass", "label": "Flow speed", "input_unit": "m/s", "min": 5, "max": 100, "initial": 35, "output_unit": "J per kg", "js_expression": "0.5*x*x", "limitations": "Does not calculate PDC temperature, propagation, exposure or survivability."}, {"id": "mogi", "unit": 7, "title": "Mogi point-source uplift directly above a source offset", "label": "Volume change", "input_unit": "million m³", "min": 0, "max": 10, "initial": 1.2, "output_unit": "vertical displacement (m)", "js_expression": "(0.75*(x*1e6)/Math.PI)*3000/Math.pow(2000*2000+3000*3000,1.5)", "limitations": "Assumes homogeneous elastic half-space, point source, nu=0.25, r=2 km, depth=3 km."}, {"id": "gas-daily", "unit": 7, "title": "Convert sulfur dioxide mass flux into daily tons", "label": "SO₂ flux", "input_unit": "kg/s", "min": 0, "max": 10, "initial": 2.5, "output_unit": "tons per day", "js_expression": "86.4*x", "limitations": "Continuous constant flux assumed; measurement uncertainty and meteorology absent."}, {"id": "geothermal-heat", "unit": 8, "title": "Thermal power of a simplified water flow", "label": "Mass flow rate", "input_unit": "kg/s", "min": 0, "max": 80, "initial": 22, "output_unit": "thermal power (MW)", "js_expression": "x*4200*30/1e6", "limitations": "Assumes 30 K temperature drop and cp=4200 J/kg/K; not electric output."}, {"id": "expected-loss", "unit": 8, "title": "Expected annual direct loss in a toy scenario", "label": "Annual scenario probability", "input_unit": "percent", "min": 0, "max": 20, "initial": 2, "output_unit": "expected loss (USD/year)", "js_expression": "8000*x", "limitations": "Uses a synthetic $2 million exposure and 40% damage fraction; not real risk or insurance advice."}];
const functions={
"plate-motion": x => (2*x),
"surface-slope": x => (Math.atan(x/1000)*180/Math.PI),
"melt-window": x => (Math.max(0,Math.min(1,(x-950)/350))),
"viscosity": x => (1e5*Math.exp(150000/8.314*(1/(x+273.15)-1/1473.15))),
"gas-expansion": x => (20/x),
"ascent": x => (5000/(x*3600)),
"effusion": x => (86400*x),
"lava-travel": x => (x*1000/(0.5*60)),
"tephra-loading": x => (10*x),
"ash-settling": x => ((2300-1.2)*9.81*Math.pow(x*1e-6,2)/(18*1.8e-5)),
"lahar-time": x => (x/18),
"pdc-energy": x => (0.5*x*x),
"mogi": x => ((0.75*(x*1e6)/Math.PI)*3000/Math.pow(2000*2000+3000*3000,1.5)),
"gas-daily": x => (86.4*x),
"geothermal-heat": x => (x*4200*30/1e6),
"expected-loss": x => (8000*x)
};
function graph(model,f,value){
 const points=Array.from({length:65},(_,i)=>{const x=model.min+(model.max-model.min)*i/64; return {x,y:f(x)};}).filter(v=>Number.isFinite(v.y));
 if(!points.length) return '';
 const lo=Math.min(...points.map(p=>p.y)), hi=Math.max(...points.map(p=>p.y));
 const xd=x=>15+480*(x-model.min)/(model.max-model.min);
 const yd=y=>112-93*(y-lo)/Math.max(hi-lo,1e-9);
 const d=points.map((p,i)=>(i?'L':'M')+xd(p.x).toFixed(2)+' '+yd(p.y).toFixed(2)).join(' ');
 return '<path d="'+d+'" fill="none" stroke="#08778c" stroke-width="3"/><circle cx="'+xd(value).toFixed(2)+'" cy="'+yd(f(value)).toFixed(2)+'" r="5" fill="#a84c18"/>';
}
function start(){
 const byId=new Map(modelList.map(m=>[m.id,m]));
 document.querySelectorAll('section.model[data-model]').forEach(box=>{
  const id=box.getAttribute('data-model'),model=byId.get(id),fn=functions[id];if(!model||!fn)return;
  const input=box.querySelector('input[type=range]'),output=box.querySelector('output'),svg=box.querySelector('svg');if(!input||!output||!svg)return;
  function update(){let x=Number(input.value),y=fn(x);output.textContent=(Number.isFinite(y)?Number(y.toPrecision(6)).toLocaleString(): 'Undefined')+' '+model.output_unit;input.setAttribute('aria-valuetext',x+' '+model.input_unit);svg.innerHTML=graph(model,fn,x);}
  input.addEventListener('input',update);update();
 });
}
document.addEventListener('DOMContentLoaded',start);

})();


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

