/* Mineralogy Interactive Simulation Suite */
(()=>{
// Offline teaching models; arbitrary instructional inputs, never field-calibrated.
const models=[{"id": 1, "unit": 1, "title": "Bulk specimen density", "control": "Measured specimen volume", "minimum": 35, "maximum": 100, "initial": 53, "input_unit": "cm³", "expression": "185/x", "output_unit": "g/cm³", "limitations": "Specimen mass fixed at 185 g; porosity and water uptake excluded."}, {"id": 2, "unit": 1, "title": "Diagnostic prevalence", "control": "Grains with a diagnostic feature", "minimum": 0, "maximum": 50, "initial": 28, "input_unit": "grains", "expression": "100*x/50", "output_unit": "%", "limitations": "50 selected grains, not representative of all outcrops."}, {"id": 3, "unit": 2, "title": "Orthorhombic cell volume", "control": "Cell edge c", "minimum": 3, "maximum": 12, "initial": 6, "input_unit": "Å", "expression": "4*5*x", "output_unit": "Å³", "limitations": "a=4 Å and b=5 Å fixed; all interaxial angles 90°."}, {"id": 4, "unit": 2, "title": "Cubic plane spacing d111", "control": "Cell edge a", "minimum": 3, "maximum": 7, "initial": 4, "input_unit": "Å", "expression": "x/Math.sqrt(3)", "output_unit": "Å", "limitations": "Cubic geometry and 111 plane only."}, {"id": 5, "unit": 3, "title": "Scherrer apparent domain size", "control": "Peak width beta", "minimum": 0.002, "maximum": 0.012, "initial": 0.003, "input_unit": "rad", "expression": ".9*.154/(x*Math.cos(15*Math.PI/180))", "output_unit": "nm", "limitations": "Assumes instrumental broadening already removed and no strain."}, {"id": 6, "unit": 3, "title": "Simplified Mg endmember fraction", "control": "Mg site fraction", "minimum": 0, "maximum": 1, "initial": 0.72, "input_unit": "mol fraction", "expression": "100*x", "output_unit": "mol%", "limitations": "Two-site Fe-Mg model does not establish bulk phase identity."}, {"id": 7, "unit": 4, "title": "Shared oxygen in silicate framework", "control": "Number of silicon tetrahedra", "minimum": 1, "maximum": 30, "initial": 12, "input_unit": "Si", "expression": "2*x", "output_unit": "O equivalents", "limitations": "Full corner sharing, no Al substitutions, and idealized net accounting."}, {"id": 8, "unit": 4, "title": "Chain-silicate cleavage complement", "control": "Acute cleavage angle", "minimum": 30, "maximum": 80, "initial": 56, "input_unit": "degrees", "expression": "180-x", "output_unit": "degrees", "limitations": "Supplement of ideal angle; thin section apparent geometry differs."}, {"id": 9, "unit": 5, "title": "Theoretical iron in FeS₂", "control": "Fe atomic mass", "minimum": 54, "maximum": 58, "initial": 55.845, "input_unit": "g/mol", "expression": "100*x/(x+2*32.06)", "output_unit": "% Fe", "limitations": "Ideal pure FeS2; not assay grade."}, {"id": 10, "unit": 5, "title": "Salt solution concentration", "control": "Recovered dissolved salt mass", "minimum": 1, "maximum": 20, "initial": 5, "input_unit": "g", "expression": "x/.25", "output_unit": "g/L", "limitations": "250 mL volume fixed; not a saturation calculation."}, {"id": 11, "unit": 6, "title": "Retardation at fixed birefringence", "control": "Section thickness", "minimum": 20, "maximum": 50, "initial": 30, "input_unit": "µm", "expression": "0.009*x*1000", "output_unit": "nm", "limitations": "Birefringence orientation fixed for illustration."}, {"id": 12, "unit": 6, "title": "Optical contrast", "control": "Specimen refractive index", "minimum": 1.45, "maximum": 1.9, "initial": 1.65, "input_unit": "index", "expression": "Math.abs(x-1.54)", "output_unit": "RI difference", "limitations": "Mounting medium n=1.54 assumed, not identification alone."}, {"id": 13, "unit": 7, "title": "Bragg plane spacing", "control": "Half scattering angle theta", "minimum": 7, "maximum": 35, "initial": 15, "input_unit": "degrees", "expression": ".154/(2*Math.sin(x*Math.PI/180))", "output_unit": "nm", "limitations": "First-order diffraction λ=.154 nm; angle is theta not 2theta."}, {"id": 14, "unit": 7, "title": "EDS host contamination proxy", "control": "Inclusion diameter", "minimum": 2, "maximum": 25, "initial": 5, "input_unit": "µm", "expression": "18/x", "output_unit": "interaction/inclusion width", "limitations": "Screening width ratio only; not a calibrated contamination fraction."}, {"id": 15, "unit": 8, "title": "Contained metal in hypothetical material", "control": "Head grade", "minimum": 0.1, "maximum": 2, "initial": 0.8, "input_unit": "wt%", "expression": "2e6*x/100", "output_unit": "tonnes", "limitations": "Two million tonnes fixed; does not imply economically recoverable reserve."}, {"id": 16, "unit": 8, "title": "Relative percent difference", "control": "Second duplicate reading", "minimum": 35, "maximum": 65, "initial": 49, "input_unit": "units", "expression": "100*Math.abs(51-x)/((51+x)/2)", "output_unit": "% RPD", "limitations": "One duplicate pair with first result 51; not an accuracy estimate."}];
function calc(expr,x){ const f=new Function('x', 'return ('+expr+');'); return f(x);}
const nice=v=>Number.isFinite(v)?Number(v.toPrecision(5)).toLocaleString('en-US',{maximumFractionDigits:5}):'undefined';
for (const el of document.querySelectorAll('[data-model]')) {
 const m=models[Number(el.dataset.model)-1]; if(!m)continue;
 const inp=el.querySelector('input');const out=el.querySelector('output');const svg=el.querySelector('svg');
 const r=svg.querySelector('polyline'),dot=svg.querySelector('circle');
 const raw=[]; for(let k=0;k<=60;k++){let x=m.minimum+(m.maximum-m.minimum)*k/60;let y=calc(m.expression,x);raw.push([x,y]);}
 const finite=raw.map(v=>v[1]).filter(Number.isFinite);let lo=Math.min(...finite),hi=Math.max(...finite);if(hi===lo){lo-=1;hi+=1};let pad=(hi-lo)*.08;lo-=pad;hi+=pad;
 r.setAttribute('points',raw.map(([x,y])=>`${(x-m.minimum)/(m.maximum-m.minimum)*300},${95-(y-lo)/(hi-lo)*80}`).join(' '));
 function update(){let x=Number(inp.value),y=calc(m.expression,x);out.textContent=`${nice(y)} ${m.output_unit}`;out.value=out.textContent;const cx=(x-m.minimum)/(m.maximum-m.minimum)*300,cy=95-(y-lo)/(hi-lo)*80;dot.setAttribute('cx',cx);dot.setAttribute('cy',cy);el.querySelector('[data-current]').textContent=nice(x)+' '+m.input_unit;}
 inp.addEventListener('input',update);update();
}

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

