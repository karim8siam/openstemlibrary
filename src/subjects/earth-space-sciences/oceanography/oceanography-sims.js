/* Oceanography Interactive Simulation Suite */
"use strict";
const oceanModels = [{"id": "sonar", "unit": 1, "title": "Sounding depth from echo return", "label": "Round-trip echo travel time (s)", "min": 0.5, "max": 8, "initial": 3, "units": "m", "python_expression": "1480*x/2", "limits": "Constant sound speed 1480 m/s; real sound speed varies with temperature, pressure and salinity.", "js_expression": "1480*x/2"}, {"id": "slope", "unit": 1, "title": "Local seafloor slope", "label": "Depth change across 1 km (m)", "min": 0, "max": 400, "initial": 80, "units": "degrees", "python_expression": "math.degrees(math.atan(x/1000))", "limits": "Ideal straight transect; slope depends on grid scale and the distance reference.", "js_expression": "(x=>x*180/Math.PI)(Math.atan(x/1000))"}, {"id": "salinity", "unit": 2, "title": "Two-endmember salinity mixing", "label": "Fraction of 35 g/kg endmember", "min": 0, "max": 1, "initial": 0.6, "units": "g/kg", "python_expression": "30*(1-x)+35*x", "limits": "Fixed conservative endmembers at 30 and 35 g/kg; no evaporation or reactions.", "js_expression": "30*(1-x)+35*x"}, {"id": "heat", "unit": 2, "title": "Temperature change after 30 days of heating", "label": "Mixed-layer depth (m)", "min": 5, "max": 150, "initial": 40, "units": "°C", "python_expression": "70*30*86400/(1025*3990*x)", "limits": "Constant 70 W/m² net flux, no entrainment, loss or lateral advection.", "js_expression": "70*30*86400/(1025*3990*x)"}, {"id": "coriolis", "unit": 3, "title": "Coriolis frequency", "label": "Latitude (degrees)", "min": -80, "max": 80, "initial": 35, "units": "s⁻¹", "python_expression": "2*7.2921159e-5*math.sin(math.radians(x))", "limits": "Spherical rigid Earth and local f-plane; no equatorial geostrophy.", "js_expression": "2*7.2921159e-5*Math.sin((x=>x*Math.PI/180)(x))"}, {"id": "geostrophic", "unit": 3, "title": "Ideal sea-level-slope current", "label": "Sea-surface difference over 100 km (m)", "min": 0.01, "max": 1, "initial": 0.2, "units": "m/s", "python_expression": "9.81*x/(1e5*(2*7.2921159e-5*math.sin(math.radians(40))))", "limits": "40°N, steady geostrophic balance, ignores friction and atmospheric corrections.", "js_expression": "9.81*x/(1e5*(2*7.2921159e-5*Math.sin((x=>x*Math.PI/180)(40))))"}, {"id": "shallowwave", "unit": 4, "title": "Long gravity-wave speed", "label": "Water depth (m)", "min": 5, "max": 6000, "initial": 100, "units": "m/s", "python_expression": "math.sqrt(9.81*x)", "limits": "Shallow-water wavelength assumption; not an arbitrary short wind wave.", "js_expression": "Math.sqrt(9.81*x)"}, {"id": "waveenergy", "unit": 4, "title": "Linear significant-wave energy per area", "label": "Significant wave height (m)", "min": 0.5, "max": 10, "initial": 3, "units": "J/m²", "python_expression": "1025*9.81*x*x/16", "limits": "Linear irregular sea approximation; excludes breaking and directionality.", "js_expression": "1025*9.81*x*x/16"}, {"id": "temperature", "unit": 5, "title": "Surface-flux-driven temperature tendency", "label": "Net flux (W/m²)", "min": -250, "max": 250, "initial": 80, "units": "K/day", "python_expression": "x*86400/(1025*3990*40)", "limits": "Forty-meter mixed layer fixed; no vertical entrainment or advection.", "js_expression": "x*86400/(1025*3990*40)"}, {"id": "steric", "unit": 5, "title": "Simplified thermal expansion contribution", "label": "Layer warming (K)", "min": 0, "max": 5, "initial": 1, "units": "m", "python_expression": "2.0e-4*x*700", "limits": "Constant expansion coefficient and a 700 m layer; nonuniform real ocean.", "js_expression": "2.0e-4*x*700"}, {"id": "ph", "unit": 6, "title": "Hydrogen-ion activity ratio to pH 8.1", "label": "Comparison pH", "min": 7.4, "max": 8.5, "initial": 8.0, "units": "ratio", "python_expression": "10**(8.1-x)", "limits": "Activity ratio in a consistent pH scale; not an estimate of carbonate saturation.", "js_expression": "10**(8.1-x)"}, {"id": "residence", "unit": 6, "title": "One-box residence-time proxy", "label": "Reservoir stock (million tonnes)", "min": 1, "max": 100, "initial": 30, "units": "years", "python_expression": "x/3", "limits": "Steady sink at 3 million tonnes/year; no recirculation or storage trend.", "js_expression": "x/3"}, {"id": "attenuation", "unit": 7, "title": "Photosynthetically available light at 20 m", "label": "Attenuation coefficient (m⁻¹)", "min": 0.02, "max": 0.5, "initial": 0.12, "units": "% surface", "python_expression": "100*math.exp(-20*x)", "limits": "Single exponential coefficient; spectrum and angular light field omitted.", "js_expression": "100*Math.exp(-20*x)"}, {"id": "export", "unit": 7, "title": "Particle export reaching depth", "label": "Remineralization exponent", "min": 0.2, "max": 1.5, "initial": 0.8, "units": "%", "python_expression": "100*(100/1000)**x", "limits": "Martin-type power-law toy model between 100 and 1000 m; region dependent.", "js_expression": "100*(100/1000)**x"}, {"id": "assimilation", "unit": 8, "title": "Scalar inverse-variance estimate", "label": "Observation error SD", "min": 0.2, "max": 5, "initial": 1.2, "units": "units", "python_expression": "(10/4+12/(x*x))/(1/4+1/(x*x))", "limits": "Prior 10±2 and observation 12±x, independent Gaussian errors.", "js_expression": "(10/4+12/(x*x))/(1/4+1/(x*x))"}, {"id": "tsunami", "unit": 8, "title": "Long-wave travel time for 900 km", "label": "Water depth (m)", "min": 20, "max": 6000, "initial": 4000, "units": "hours", "python_expression": "900000/math.sqrt(9.81*x)/3600", "limits": "Uniform depth, ideal long wave, ignores complicated coastline and refraction.", "js_expression": "900000/Math.sqrt(9.81*x)/3600"}];
function renderModel(m) {
  const fig=document.getElementById('model-'+m.id);
  if (!fig) return;
  const s=fig.querySelector('input[type=range]'), v=fig.querySelector('.readout'), plot=fig.querySelector('svg');
  const calc=new Function('x', 'return ('+m.js_expression+');');
  function f(x){try{const y=calc(x);return Number.isFinite(y)?y:null}catch(e){return null}}
  function update(){const x=Number(s.value), y=f(x);v.textContent=y===null?'unavailable':y.toLocaleString('en-US',{maximumFractionDigits:5})+' '+m.units;
    const vals=[];for(let i=0;i<75;i++) vals.push(f(m.min+(m.max-m.min)*i/74));
    const good=vals.filter(x=>x!==null), mi=Math.min(...good), ma=Math.max(...good),span=ma-mi||1;
    const pts=vals.map((w,i)=>w===null?'':(10+280*i/74)+','+(90-70*(w-mi)/span)).join(' ');
    while(plot.firstChild)plot.removeChild(plot.firstChild);
    let l=document.createElementNS('http://www.w3.org/2000/svg','polyline');l.setAttribute('fill','none');l.setAttribute('stroke','#087e8b');l.setAttribute('stroke-width','3');l.setAttribute('points',pts);plot.appendChild(l);
    let dot=document.createElementNS('http://www.w3.org/2000/svg','circle');dot.setAttribute('cx',String(10+280*(x-m.min)/(m.max-m.min)));dot.setAttribute('cy',String(90-70*((y??mi)-mi)/span));dot.setAttribute('r','5');dot.setAttribute('fill','#dd6b42');plot.appendChild(dot);
  }
  s.addEventListener('input',update);update();
}
document.addEventListener('DOMContentLoaded',()=>oceanModels.forEach(renderModel));



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

