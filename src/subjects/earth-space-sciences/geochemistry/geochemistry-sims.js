/* Geochemistry Interactive Simulation Suite */
"use strict";
const geochemModels = [{"id": "inventory", "unit": 1, "title": "Element inventory from concentration", "label": "Concentration of trace element", "input_unit": "mg/kg", "min": 0, "max": 500, "initial": 120, "output_unit": "kg element in 1000 kg rock", "js_expression": "x*0.001", "limitations": "Multiply mg/kg by rock mass 1000 kg and convert milligrams to kilograms."}, {"id": "enrichment", "unit": 1, "title": "Reference normalized concentration", "label": "Sample concentration", "input_unit": "mg/kg", "min": 1, "max": 200, "initial": 75, "output_unit": "ratio to 25 mg/kg reference", "js_expression": "x/25", "limitations": "Requires a named valid reference; enrichment is not a hazard threshold."}, {"id": "ionic-strength", "unit": 2, "title": "Ionic strength of ideal NaCl", "label": "Fully dissociated NaCl", "input_unit": "mol/kg", "min": 0, "max": 0.1, "initial": 0.015, "output_unit": "mol/kg ionic strength", "js_expression": "x", "limitations": "Assumes NaCl fully dissociated and molal concentrations."}, {"id": "pH", "unit": 2, "title": "pH from hydrogen-ion activity", "label": "Hydrogen-ion activity", "input_unit": "micromolal ratio", "min": 0.0001, "max": 100, "initial": 0.25, "output_unit": "pH", "js_expression": "-Math.log10(x*1e-6)", "limitations": "Hydrogen-ion activity is represented as a scaled dimensionless value relative to standard state; acid-base complexities omitted."}, {"id": "batch-melt", "unit": 3, "title": "Batch partial-melting enrichment", "label": "Melt fraction", "input_unit": "fraction", "min": 0.01, "max": 0.9, "initial": 0.2, "output_unit": "C_l/C_0", "js_expression": "1/(0.05+x*(1-0.05))", "limitations": "Constant bulk distribution D=0.05, ideal batch melting with fixed source."}, {"id": "rayleigh", "unit": 3, "title": "Rayleigh melt enrichment", "label": "Residual melt fraction", "input_unit": "fraction", "min": 0.1, "max": 1, "initial": 0.4, "output_unit": "C_l/C_0", "js_expression": "Math.pow(x,0.3-1)", "limitations": "Fixed D=0.3, closed fractional crystallization in idealized system."}, {"id": "delta-isotope", "unit": 4, "title": "Isotope delta deviation", "label": "R_sample/R_standard", "input_unit": "ratio", "min": 0.95, "max": 1.05, "initial": 0.995, "output_unit": "per mil", "js_expression": "1000*(x-1)", "limitations": "Reference ratio fixed, input dimensionless; check scale and analytical uncertainty."}, {"id": "decay", "unit": 4, "title": "Remaining parent fraction", "label": "Elapsed half-lives", "input_unit": "half-lives", "min": 0, "max": 5, "initial": 2, "output_unit": "fraction", "js_expression": "Math.pow(2,-x)", "limitations": "Closed-system exponential decay, does not model daughter correction or mineral resetting."}, {"id": "alkalinity", "unit": 5, "title": "Alkalinity as CaCO3 equivalents", "label": "Alkalinity", "input_unit": "meq/L", "min": 0, "max": 10, "initial": 2.4, "output_unit": "mg/L CaCO3", "js_expression": "50.04*x", "limitations": "Mass equivalents only; does not resolve noncarbonate alkalinity species."}, {"id": "charge", "unit": 5, "title": "Ion charge-balance residual", "label": "Measured cation charge", "input_unit": "meq/L", "min": 1, "max": 10, "initial": 4.4, "output_unit": "percent residual", "js_expression": "100*(x-4)/(x+4)", "limitations": "Anion charge fixed at 4 meq/L; requires all ions included."}, {"id": "cia", "unit": 6, "title": "Chemical index of alteration", "label": "Molar Al2O3 share", "input_unit": "molar share", "min": 0, "max": 1, "initial": 0.45, "output_unit": "CIA percent", "js_expression": "100*x/(x+0.55)", "limitations": "Other specified molar oxide sum fixed at 0.55; parent-rock corrections not included."}, {"id": "solute-export", "unit": 6, "title": "Dissolved export for constant flow", "label": "Discharge", "input_unit": "m3/s", "min": 0, "max": 10, "initial": 0.4, "output_unit": "kg/year", "js_expression": "2*x*1000*31536000/1e6", "limitations": "Concentration fixed 2 mg/L; ignores seasonality and sample representativeness."}, {"id": "mixing", "unit": 7, "title": "Two-source tracer mixture", "label": "Mass fraction of source A", "input_unit": "fraction", "min": 0, "max": 1, "initial": 0.5, "output_unit": "mg/kg", "js_expression": "x*40+(1-x)*100", "limitations": "Conservative two-endmember assumption; source A=40, B=100 mg/kg."}, {"id": "deposition", "unit": 7, "title": "Collector deposition flux", "label": "Collector mass", "input_unit": "g", "min": 0, "max": 10, "initial": 1.5, "output_unit": "g/m2/day", "js_expression": "x/(0.5*30)", "limitations": "Collection area 0.5 m² and exposure 30 days; no blank or resuspension correction."}, {"id": "dilution", "unit": 8, "title": "Back-calculate pre-dilution", "label": "Measured diluted concentration", "input_unit": "mg/L", "min": 0, "max": 20, "initial": 0.8, "output_unit": "mg/L original", "js_expression": "x*25", "limitations": "Fifty milliliters final from two milliliters aliquot, no matrix effects."}, {"id": "recovery", "unit": 8, "title": "Matrix spike recovery", "label": "Spiked sample concentration", "input_unit": "mg/L", "min": 3, "max": 10, "initial": 7.5, "output_unit": "percent", "js_expression": "100*(x-3)/5", "limitations": "Native=3 mg/L, added spike=5 mg/L; negative or >100% possible when biased."}];
function calculateModel(m,x){ const v=Number(x); if(!Number.isFinite(v))throw new Error("Nonfinite input");const f=new Function("x",`"use strict";return (${m.js_expression});`);const y=f(v);if(!Number.isFinite(y))throw new Error("Invalid modeled result");return y;}
function modelCard(m){const section=document.createElement("section");section.className="model";section.id="model-"+m.id;const h=document.createElement("h3");h.textContent=m.title;section.appendChild(h);const label=document.createElement("label");label.htmlFor="slider-"+m.id;label.textContent=m.label+" ("+m.input_unit+")";section.appendChild(label);const input=document.createElement("input");input.type="range";input.id=label.htmlFor;input.min=m.min;input.max=m.max;input.step=(m.max-m.min)/1000;input.value=m.initial;section.appendChild(input);const value=document.createElement("output");value.htmlFor=input.id;value.className="readout";value.setAttribute("aria-live","polite");section.appendChild(value);const svg=document.createElementNS("http://www.w3.org/2000/svg","svg");svg.setAttribute("viewBox","0 0 500 135");svg.setAttribute("role","img");svg.setAttribute("aria-label","Predicted output versus slider input for "+m.title);section.appendChild(svg);const desc=document.createElement("p");desc.className="small";desc.textContent="Model boundary: "+m.limitations;section.appendChild(desc);function draw(){const x=Number(input.value);const y=calculateModel(m,x);value.value=Number(y).toPrecision(6)+" "+m.output_unit;value.textContent=Number(y).toPrecision(6)+" "+m.output_unit;const n=80;let values=[];for(let j=0;j<=n;j++){let u=m.min+(m.max-m.min)*j/n;values.push([u,calculateModel(m,u)]);}let minY=Math.min(...values.map(a=>a[1]));let maxY=Math.max(...values.map(a=>a[1]));if(maxY===minY){maxY+=1;minY-=1}let points=values.map(([u,v])=>`${20+(u-m.min)/(m.max-m.min)*460},${112-(v-minY)/(maxY-minY)*90}`).join(" ");svg.replaceChildren();const poly=document.createElementNS(svg.namespaceURI,"polyline");poly.setAttribute("points",points);poly.setAttribute("fill","none");poly.setAttribute("stroke","#087b9b");poly.setAttribute("stroke-width","3");svg.appendChild(poly);const dot=document.createElementNS(svg.namespaceURI,"circle");dot.setAttribute("cx",20+(x-m.min)/(m.max-m.min)*460);dot.setAttribute("cy",112-(y-minY)/(maxY-minY)*90);dot.setAttribute("r",5);dot.setAttribute("fill","#e27f20");svg.appendChild(dot)}input.addEventListener("input",draw);draw();return section}
document.addEventListener("DOMContentLoaded",()=>{document.querySelectorAll("[data-unit-models]").forEach(host=>{const unit=Number(host.dataset.unitModels);geochemModels.filter(m=>m.unit===unit).forEach(m=>host.appendChild(modelCard(m)));});});



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

