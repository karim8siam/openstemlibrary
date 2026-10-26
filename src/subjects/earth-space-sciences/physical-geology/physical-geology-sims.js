/* Physical Geology Interactive Simulation Suite */
window.GEO_FORMULAS={1:x=>(x*25000/100000),2:x=>(720/x),3:x=>(156/x),4:x=>(x*2.6+(1-x)*3.0),5:x=>(20+880*Math.exp(-0.02*x)),6:x=>(2400000*x),7:x=>(80/x),8:x=>(Math.pow(0.5,x)),9:x=>(4.2*x*10),10:x=>(x*Math.tan(35*Math.PI/180)),11:x=>(2700*9.81*x/1000),12:x=>((x-0.2)/0.2*100),13:x=>(500*9.81*Math.sin(x*Math.PI/180)),14:x=>(6*1.5*x),15:x=>(.0002*x*18),16:x=>(100*(1-Math.pow(0.98,x)))};
window.GEO_MODELS=[{"id": 1, "unit": 1, "title": "Map scale and inferred distance", "control": "Map length", "minimum": 2, "maximum": 30, "initial": 12, "input_unit": "cm", "expression": "x*25000/100000", "output_unit": "km", "limitations": "1:25,000 scale; horizontal ground distance only."}, {"id": 2, "unit": 1, "title": "Seismic direct arrival", "control": "P speed", "minimum": 3, "maximum": 9, "initial": 6, "input_unit": "km/s", "expression": "720/x", "output_unit": "s", "limitations": "Straight 720-km ray through homogeneous material."}, {"id": 3, "unit": 2, "title": "Mineral density experiment", "control": "Specimen volume", "minimum": 20, "maximum": 110, "initial": 60, "input_unit": "cm³", "expression": "156/x", "output_unit": "g/cm³", "limitations": "Dry mass fixed at 156 g; excluded water absorption."}, {"id": 4, "unit": 2, "title": "Two-phase density mixing", "control": "Fraction of phase A", "minimum": 0, "maximum": 1, "initial": 0.35, "input_unit": "fraction", "expression": "x*2.6+(1-x)*3.0", "output_unit": "g/cm³", "limitations": "No voids; fixed material densities."}, {"id": 5, "unit": 3, "title": "Conductive cooling proxy", "control": "Minutes since exposure", "minimum": 0, "maximum": 120, "initial": 30, "input_unit": "min", "expression": "20+880*Math.exp(-0.02*x)", "output_unit": "°C", "limitations": "Lumped body cooling; field magma bodies are not uniform."}, {"id": 6, "unit": 3, "title": "Estimated lava volume", "control": "Mean flow thickness", "minimum": 1, "maximum": 18, "initial": 6, "input_unit": "m", "expression": "2400000*x", "output_unit": "m³", "limitations": "Uniform thickness over 2.4 km²."}, {"id": 7, "unit": 4, "title": "Mean sediment accumulation", "control": "Duration", "minimum": 0.5, "maximum": 8, "initial": 2.5, "input_unit": "Ma", "expression": "80/x", "output_unit": "m/Ma", "limitations": "80 m preserved thickness; no compaction."}, {"id": 8, "unit": 4, "title": "Radiometric remaining parent", "control": "Elapsed half-lives", "minimum": 0, "maximum": 6, "initial": 3, "input_unit": "half-lives", "expression": "Math.pow(0.5,x)", "output_unit": "fraction", "limitations": "Ideal closed parent-only decay."}, {"id": 9, "unit": 5, "title": "Plate displacement", "control": "Motion duration", "minimum": 0.2, "maximum": 10, "initial": 3, "input_unit": "Ma", "expression": "4.2*x*10", "output_unit": "km", "limitations": "Constant 4.2 cm/yr plate speed."}, {"id": 10, "unit": 5, "title": "Inclined slab depth", "control": "Horizontal distance", "minimum": 0, "maximum": 250, "initial": 90, "input_unit": "km", "expression": "x*Math.tan(35*Math.PI/180)", "output_unit": "km", "limitations": "Planar slab with fixed 35° dip."}, {"id": 11, "unit": 6, "title": "Lithostatic pressure", "control": "Depth", "minimum": 0, "maximum": 30, "initial": 12, "input_unit": "km", "expression": "2700*9.81*x/1000", "output_unit": "MPa", "limitations": "Uniform 2700 kg/m³ rock and g=9.81 m/s²."}, {"id": 12, "unit": 6, "title": "Linear grain-size growth", "control": "New grain diameter", "minimum": 0.2, "maximum": 1, "initial": 0.5, "input_unit": "mm", "expression": "(x-0.2)/0.2*100", "output_unit": "%", "limitations": "Reference starting diameter 0.20 mm."}, {"id": 13, "unit": 7, "title": "Gravity-driven block force", "control": "Slope angle", "minimum": 0, "maximum": 65, "initial": 22, "input_unit": "degrees", "expression": "500*9.81*Math.sin(x*Math.PI/180)", "output_unit": "N", "limitations": "Friction and pore pressure omitted; not a safety metric."}, {"id": 14, "unit": 7, "title": "Channel discharge", "control": "Mean flow velocity", "minimum": 0.1, "maximum": 3, "initial": 0.8, "input_unit": "m/s", "expression": "6*1.5*x", "output_unit": "m³/s", "limitations": "Rectangular 6 m by 1.5 m channel."}, {"id": 15, "unit": 8, "title": "Darcy groundwater discharge", "control": "Hydraulic gradient", "minimum": 0.001, "maximum": 0.08, "initial": 0.02, "input_unit": "fraction", "expression": ".0002*x*18", "output_unit": "m³/s", "limitations": "K=0.0002 m/s; homogeneous Darcy conditions."}, {"id": 16, "unit": 8, "title": "Cumulative exceedance chance", "control": "Years observed", "minimum": 1, "maximum": 60, "initial": 20, "input_unit": "yr", "expression": "100*(1-Math.pow(0.98,x))", "output_unit": "%", "limitations": "Illustrative independent 2% annual rate; not a prediction."}];
"use strict";
(function(){
const models=window.GEO_MODELS||[];
function compute(m,x){const F=window.GEO_FORMULAS;return F[m.id](x)}
function format(y){if(!Number.isFinite(y))return 'undefined';if(y===0)return '0';if(Math.abs(y)<.001 || Math.abs(y)>1e5)return y.toExponential(3);return Number(y.toPrecision(6)).toLocaleString('en-US')}
function draw(svg,m,x,y){const W=520,H=220,p=40;
 const n=90,pts=[];for(let i=0;i<=n;i++){let v=m.minimum+(m.maximum-m.minimum)*i/n;pts.push([v,compute(m,v)])}
 const ys=pts.map(z=>z[1]).filter(Number.isFinite);let lo=Math.min(...ys),hi=Math.max(...ys);if(hi===lo){hi+=1;lo-=1}
 const px=v=>p+(v-m.minimum)/(m.maximum-m.minimum)*(W-2*p),py=v=>H-p-(v-lo)/(hi-lo)*(H-2*p);
 const path=pts.map((d,i)=>(i?'L':'M')+px(d[0]).toFixed(2)+' '+py(d[1]).toFixed(2)).join(' ');
 svg.innerHTML=`<title>${m.title}: output versus ${m.control}</title><path d="M${p} 16 V${H-p} H${W-10}" stroke="#7c999c" fill="none"/><path d="${path}" fill="none" stroke="#13695c" stroke-width="3"/><line x1="${px(x)}" x2="${px(x)}" y1="16" y2="${H-p}" stroke="#8e5c2e" stroke-dasharray="5 4"/><circle cx="${px(x)}" cy="${py(y)}" r="5.5" fill="#9a511d"/><text x="${p}" y="12" font-size="12" fill="#345">${format(hi)} ${m.output_unit}</text><text x="${p}" y="${H-10}" font-size="12" fill="#345">${m.minimum} ${m.input_unit}</text><text x="${W-p-65}" y="${H-10}" font-size="12" fill="#345">${m.maximum} ${m.input_unit}</text>`;}
function init(el){let id=Number(el.dataset.model);let m=models.find(x=>x.id===id);if(!m)return;let range=el.querySelector('input');let result=el.querySelector('.result');let svg=el.querySelector('svg');function update(){const x=Number(range.value),y=compute(m,x);result.textContent=format(y)+' '+m.output_unit+' ('+format(x)+' '+m.input_unit+')';draw(svg,m,x,y)}range.addEventListener('input',update);update()}
for(const el of document.querySelectorAll('[data-model]'))init(el);
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

