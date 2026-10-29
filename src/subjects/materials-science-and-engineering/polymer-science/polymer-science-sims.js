/* Polymer Science Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Ideal number-average polymerization degree",
    "input": {
      "name": "Mn",
      "label": "Number-average molar mass",
      "min": 10000,
      "max": 150000,
      "default": 50000,
      "step": 1000,
      "unit": "g/mol"
    },
    "expression": "Mn/100",
    "result_unit": "repeat units",
    "assumptions": "Linear homopolymer, repeat-unit mass 100 g/mol, chain-end masses neglected",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Molar-mass dispersity at fixed Mn",
    "input": {
      "name": "Mm",
      "label": "Mass-average molar mass",
      "min": 50000,
      "max": 300000,
      "default": 100000,
      "step": 5000,
      "unit": "g/mol"
    },
    "expression": "Mm/50000",
    "result_unit": "dimensionless",
    "assumptions": "Mn=50000 g/mol fixed; independent variation of Mm is illustrative and does not define a chain-length distribution",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Fox estimate of miscible blend Tg",
    "input": {
      "name": "w",
      "label": "Mass fraction of component one",
      "min": 0,
      "max": 1,
      "default": 0.5,
      "step": 0.025,
      "unit": "fraction"
    },
    "expression": "1/(w/250+(1-w)/380)",
    "result_unit": "K",
    "assumptions": "Hypothetical miscible binary amorphous blend Tg1=250 K, Tg2=380 K; Fox reciprocal rule only; no phase separation",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Ideal Gibbs-Thomson lamellar melting point",
    "input": {
      "name": "l",
      "label": "Crystal lamellar thickness",
      "min": 3,
      "max": 40,
      "default": 12,
      "step": 0.5,
      "unit": "nm"
    },
    "expression": "450*(1-2*0.08/(1.5e8*l*1e-9))",
    "result_unit": "K",
    "assumptions": "Planar lamella equilibrium approximation Tm_inf=450 K, fold surface energy 0.08 J/m\u00b2, enthalpy density 1.5e8 J/m\u00b3; no recrystallization",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Ideal balanced step-growth DPn",
    "input": {
      "name": "p",
      "label": "Functional-group conversion",
      "min": 0.85,
      "max": 0.999,
      "default": 0.97,
      "step": 0.001,
      "unit": "fraction"
    },
    "expression": "1/(1-p)",
    "result_unit": "repeat units",
    "assumptions": "Ideal bifunctional, stoichiometrically balanced equal-reactivity step growth with no cycles or side reactions",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Steady-state radical propagation rate",
    "input": {
      "name": "I",
      "label": "Initiator concentration",
      "min": 0.001,
      "max": 0.1,
      "default": 0.02,
      "step": 0.001,
      "unit": "mol/L"
    },
    "expression": "100*2*Math.sqrt(2*0.6*1e-5*I/1e7)",
    "result_unit": "mol/(L s)",
    "assumptions": "Hypothetical kp=100 L/(mol s), [M]=2 mol/L, f=0.6, kd=1e-5 s\u207b\u00b9, kt=1e7 L/(mol s) defined for effective radical disappearance kt[R\u2022]\u00b2; steady state, isothermal, no gel effect",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Single Maxwell relaxation modulus",
    "input": {
      "name": "t",
      "label": "Time after step strain",
      "min": 0,
      "max": 50,
      "default": 10,
      "step": 0.5,
      "unit": "s"
    },
    "expression": "1000*Math.exp(-t/10)",
    "result_unit": "MPa",
    "assumptions": "Single small-strain Maxwell mode E0=1000 MPa, tau=10 s, temperature fixed; not a full relaxation spectrum",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Power-law shear-thinning melt viscosity",
    "input": {
      "name": "g",
      "label": "Shear rate",
      "min": 0.1,
      "max": 1000,
      "default": 10,
      "step": 0.1,
      "unit": "1/s"
    },
    "expression": "100*Math.pow(g,-0.4)",
    "result_unit": "Pa s",
    "assumptions": "Power-law synthetic fit with K=100 Pa s at 1/s, n=0.6; excludes Newtonian plateaus, shear heating, slip and melt fracture",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Linear-elastic tensile stress",
    "input": {
      "name": "e",
      "label": "Engineering tensile strain",
      "min": 0.1,
      "max": 3,
      "default": 1,
      "step": 0.05,
      "unit": "%"
    },
    "expression": "1200*e/100",
    "result_unit": "MPa",
    "assumptions": "Small-strain isotropic linear elastic approximation E=1200 MPa, no yield or environmental effects; limit before nonlinear response",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Illustrative mode-I crack intensity",
    "input": {
      "name": "a",
      "label": "Initial crack length",
      "min": 10,
      "max": 600,
      "default": 100,
      "step": 10,
      "unit": "\u00b5m"
    },
    "expression": "1.12*25*Math.sqrt(Math.PI*a*1e-6)",
    "result_unit": "MPa sqrt(m)",
    "assumptions": "Nominal tensile stress=25 MPa, Y=1.12, geometry-specific LEFM; no polymer viscoelasticity, plastic zone or crack-growth law",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Nominal extruder residence time",
    "input": {
      "name": "Q",
      "label": "Volumetric polymer throughput",
      "min": 10,
      "max": 100,
      "default": 50,
      "step": 1,
      "unit": "cm\u00b3/s"
    },
    "expression": "250/Q",
    "result_unit": "s",
    "assumptions": "Assumed filled material volume 250 cm\u00b3 with constant Q; no residence-time distribution, mixing or dead zones",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Characteristic conduction time",
    "input": {
      "name": "h",
      "label": "Characteristic half-thickness",
      "min": 0.5,
      "max": 5,
      "default": 2,
      "step": 0.1,
      "unit": "mm"
    },
    "expression": "Math.pow(h*1e-3,2)/1.2e-7",
    "result_unit": "s",
    "assumptions": "Simplified h\u00b2/alpha scale with constant alpha=1.2e-7 m\u00b2/s; not mold cycle time, ignores crystallization and contacts",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Illustrative SEC calibration curve",
    "input": {
      "name": "t",
      "label": "Retention time",
      "min": 12,
      "max": 32,
      "default": 20,
      "step": 0.5,
      "unit": "min"
    },
    "expression": "Math.pow(10,7.2-0.12*t)",
    "result_unit": "apparent g/mol",
    "assumptions": "Fictional log-linear apparent molar mass calibration; only valid in selected retention window under unspecified demo chromatography conditions",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Ideal DSC crystallinity estimate",
    "input": {
      "name": "H",
      "label": "Melting enthalpy per sample mass",
      "min": 0,
      "max": 150,
      "default": 80,
      "step": 2.5,
      "unit": "J/g"
    },
    "expression": "100*H/(0.8*200)",
    "result_unit": "% crystallinity",
    "assumptions": "Hypothetical 80% polymer mass, reference fusion enthalpy 200 J/g-polymer, no cold crystallization, baseline or multiple-phase issues",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Ideal gas permeation flux",
    "input": {
      "name": "L",
      "label": "Film thickness",
      "min": 20,
      "max": 200,
      "default": 50,
      "step": 2,
      "unit": "\u00b5m"
    },
    "expression": "1e-15*5000/(L*1e-6)",
    "result_unit": "mol/(m\u00b2 s)",
    "assumptions": "1D steady solution-diffusion, P=1e-15 mol m/(m\u00b2 s Pa), delta pressure 5000 Pa, intact homogeneous film",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Synthetic retained Mn fraction",
    "input": {
      "name": "t",
      "label": "Hydrolytic exposure time",
      "min": 0,
      "max": 365,
      "default": 100,
      "step": 5,
      "unit": "days"
    },
    "expression": "100*Math.exp(-0.008*t)",
    "result_unit": "% original Mn",
    "assumptions": "Hypothetical first-order apparent Mn decline 0.008/day; not mass loss, biodegradability, implant lifetime or CO2 mineralization",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Ideal number-average polymerization degree", "input": {"name": "Mn", "label": "Number-average molar mass", "min": 10000, "max": 150000, "default": 50000, "step": 1000, "unit": "g/mol"}, "expression": "Mn/100", "result_unit": "repeat units", "assumptions": "Linear homopolymer, repeat-unit mass 100 g/mol, chain-end masses neglected", "synthetic": true}, {"id": 1, "unit": 1, "title": "Molar-mass dispersity at fixed Mn", "input": {"name": "Mm", "label": "Mass-average molar mass", "min": 50000, "max": 300000, "default": 100000, "step": 5000, "unit": "g/mol"}, "expression": "Mm/50000", "result_unit": "dimensionless", "assumptions": "Mn=50000 g/mol fixed; independent variation of Mm is illustrative and does not define a chain-length distribution", "synthetic": true}, {"id": 2, "unit": 2, "title": "Fox estimate of miscible blend Tg", "input": {"name": "w", "label": "Mass fraction of component one", "min": 0, "max": 1, "default": 0.5, "step": 0.025, "unit": "fraction"}, "expression": "1/(w/250+(1-w)/380)", "result_unit": "K", "assumptions": "Hypothetical miscible binary amorphous blend Tg1=250 K, Tg2=380 K; Fox reciprocal rule only; no phase separation", "synthetic": true}, {"id": 3, "unit": 2, "title": "Ideal Gibbs-Thomson lamellar melting point", "input": {"name": "l", "label": "Crystal lamellar thickness", "min": 3, "max": 40, "default": 12, "step": 0.5, "unit": "nm"}, "expression": "450*(1-2*0.08/(1.5e8*l*1e-9))", "result_unit": "K", "assumptions": "Planar lamella equilibrium approximation Tm_inf=450 K, fold surface energy 0.08 J/m², enthalpy density 1.5e8 J/m³; no recrystallization", "synthetic": true}, {"id": 4, "unit": 3, "title": "Ideal balanced step-growth DPn", "input": {"name": "p", "label": "Functional-group conversion", "min": 0.85, "max": 0.999, "default": 0.97, "step": 0.001, "unit": "fraction"}, "expression": "1/(1-p)", "result_unit": "repeat units", "assumptions": "Ideal bifunctional, stoichiometrically balanced equal-reactivity step growth with no cycles or side reactions", "synthetic": true}, {"id": 5, "unit": 3, "title": "Steady-state radical propagation rate", "input": {"name": "I", "label": "Initiator concentration", "min": 0.001, "max": 0.1, "default": 0.02, "step": 0.001, "unit": "mol/L"}, "expression": "100*2*Math.sqrt(2*0.6*1e-5*I/1e7)", "result_unit": "mol/(L s)", "assumptions": "Hypothetical kp=100 L/(mol s), [M]=2 mol/L, f=0.6, kd=1e-5 s⁻¹, kt=1e7 L/(mol s) defined for effective radical disappearance kt[R•]²; steady state, isothermal, no gel effect", "synthetic": true}, {"id": 6, "unit": 4, "title": "Single Maxwell relaxation modulus", "input": {"name": "t", "label": "Time after step strain", "min": 0, "max": 50, "default": 10, "step": 0.5, "unit": "s"}, "expression": "1000*Math.exp(-t/10)", "result_unit": "MPa", "assumptions": "Single small-strain Maxwell mode E0=1000 MPa, tau=10 s, temperature fixed; not a full relaxation spectrum", "synthetic": true}, {"id": 7, "unit": 4, "title": "Power-law shear-thinning melt viscosity", "input": {"name": "g", "label": "Shear rate", "min": 0.1, "max": 1000, "default": 10, "step": 0.1, "unit": "1/s"}, "expression": "100*Math.pow(g,-0.4)", "result_unit": "Pa s", "assumptions": "Power-law synthetic fit with K=100 Pa s at 1/s, n=0.6; excludes Newtonian plateaus, shear heating, slip and melt fracture", "synthetic": true}, {"id": 8, "unit": 5, "title": "Linear-elastic tensile stress", "input": {"name": "e", "label": "Engineering tensile strain", "min": 0.1, "max": 3, "default": 1, "step": 0.05, "unit": "%"}, "expression": "1200*e/100", "result_unit": "MPa", "assumptions": "Small-strain isotropic linear elastic approximation E=1200 MPa, no yield or environmental effects; limit before nonlinear response", "synthetic": true}, {"id": 9, "unit": 5, "title": "Illustrative mode-I crack intensity", "input": {"name": "a", "label": "Initial crack length", "min": 10, "max": 600, "default": 100, "step": 10, "unit": "µm"}, "expression": "1.12*25*Math.sqrt(Math.PI*a*1e-6)", "result_unit": "MPa sqrt(m)", "assumptions": "Nominal tensile stress=25 MPa, Y=1.12, geometry-specific LEFM; no polymer viscoelasticity, plastic zone or crack-growth law", "synthetic": true}, {"id": 10, "unit": 6, "title": "Nominal extruder residence time", "input": {"name": "Q", "label": "Volumetric polymer throughput", "min": 10, "max": 100, "default": 50, "step": 1, "unit": "cm³/s"}, "expression": "250/Q", "result_unit": "s", "assumptions": "Assumed filled material volume 250 cm³ with constant Q; no residence-time distribution, mixing or dead zones", "synthetic": true}, {"id": 11, "unit": 6, "title": "Characteristic conduction time", "input": {"name": "h", "label": "Characteristic half-thickness", "min": 0.5, "max": 5, "default": 2, "step": 0.1, "unit": "mm"}, "expression": "Math.pow(h*1e-3,2)/1.2e-7", "result_unit": "s", "assumptions": "Simplified h²/alpha scale with constant alpha=1.2e-7 m²/s; not mold cycle time, ignores crystallization and contacts", "synthetic": true}, {"id": 12, "unit": 7, "title": "Illustrative SEC calibration curve", "input": {"name": "t", "label": "Retention time", "min": 12, "max": 32, "default": 20, "step": 0.5, "unit": "min"}, "expression": "Math.pow(10,7.2-0.12*t)", "result_unit": "apparent g/mol", "assumptions": "Fictional log-linear apparent molar mass calibration; only valid in selected retention window under unspecified demo chromatography conditions", "synthetic": true}, {"id": 13, "unit": 7, "title": "Ideal DSC crystallinity estimate", "input": {"name": "H", "label": "Melting enthalpy per sample mass", "min": 0, "max": 150, "default": 80, "step": 2.5, "unit": "J/g"}, "expression": "100*H/(0.8*200)", "result_unit": "% crystallinity", "assumptions": "Hypothetical 80% polymer mass, reference fusion enthalpy 200 J/g-polymer, no cold crystallization, baseline or multiple-phase issues", "synthetic": true}, {"id": 14, "unit": 8, "title": "Ideal gas permeation flux", "input": {"name": "L", "label": "Film thickness", "min": 20, "max": 200, "default": 50, "step": 2, "unit": "µm"}, "expression": "1e-15*5000/(L*1e-6)", "result_unit": "mol/(m² s)", "assumptions": "1D steady solution-diffusion, P=1e-15 mol m/(m² s Pa), delta pressure 5000 Pa, intact homogeneous film", "synthetic": true}, {"id": 15, "unit": 8, "title": "Synthetic retained Mn fraction", "input": {"name": "t", "label": "Hydrolytic exposure time", "min": 0, "max": 365, "default": 100, "step": 5, "unit": "days"}, "expression": "100*Math.exp(-0.008*t)", "result_unit": "% original Mn", "assumptions": "Hypothetical first-order apparent Mn decline 0.008/day; not mass loss, biodegradability, implant lifetime or CO2 mineralization", "synthetic": true}];
function evaluate(id, x){const d=MODELS[id];return Number(new Function(d.input.name,`return (${d.expression});`)(x));}
function redraw(card){const id=Number(card.dataset.model),d=MODELS[id],r=card.querySelector('input'),x=Number(r.value),result=evaluate(id,x);
 const out=card.querySelector('output');out.textContent=Number.isFinite(result)?Number(result.toPrecision(7)).toString()+' '+d.result_unit:'Out of range';
 card.querySelector('.input-value').textContent=x+' '+d.input.unit;
 const pts=[];let ymin=Infinity,ymax=-Infinity;for(let n=0;n<45;n++){let xx=d.input.min+(d.input.max-d.input.min)*n/44;let yy=evaluate(id,xx);pts.push(yy);if(Number.isFinite(yy)){ymin=Math.min(ymin,yy);ymax=Math.max(ymax,yy)}}
 let rr=Math.max(1e-12,ymax-ymin);let path=pts.map((y,n)=>Number.isFinite(y)?`${16+8*n},${91-70*(y-ymin)/rr}`:null).filter(Boolean).join(' ');
 card.querySelector('polyline').setAttribute('points',path);
 let k=Math.max(0,Math.min(44,Math.round((x-d.input.min)/(d.input.max-d.input.min)*44)));let mark=card.querySelector('circle');
 mark.setAttribute('cx',String(16+8*k));mark.setAttribute('cy',String(91-70*(pts[k]-ymin)/rr));
 card.querySelector('.plot-min').textContent=Number(ymin.toPrecision(3));card.querySelector('.plot-max').textContent=Number(ymax.toPrecision(3));
}
document.addEventListener('DOMContentLoaded',()=>{for(const card of document.querySelectorAll('.model-card')){
 const r=card.querySelector('input');r.addEventListener('input',()=>redraw(card));redraw(card);
}});



(function(window) {
  if (!window.SimulationEngine) {
    window.SimulationEngine = {};
  }
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = '';
    
    var unitNum = 1;
    var mMatch = (simType || '').match(/(\d+)$/);
    if (!mMatch && typeof document !== 'undefined') {
      var bIdx = document.body.dataset.chapterIndex;
      if (bIdx !== undefined && bIdx !== null && bIdx !== '') {
        unitNum = parseInt(bIdx, 10) + 1;
      }
    }
    if (mMatch) unitNum = parseInt(mMatch[1], 10);
    
    var modelsToRender = [];
    if (typeof MODELS !== 'undefined' && Array.isArray(MODELS)) {
      modelsToRender = MODELS.filter(function(m) { return m.unit === unitNum; });
      if (modelsToRender.length === 0) {
        modelsToRender = [MODELS[(unitNum - 1) % MODELS.length]];
      }
    } else if (typeof MSE_MODELS !== 'undefined' && Array.isArray(MSE_MODELS)) {
      var startIdx = (unitNum - 1) * 2;
      modelsToRender = MSE_MODELS.slice(startIdx, startIdx + 2);
      if (modelsToRender.length === 0 && MSE_MODELS.length > 0) {
        modelsToRender = [MSE_MODELS[0]];
      }
    }
    
    modelsToRender.forEach(function(m, idx) {
      var titleText = m.title || m.name || ('Model ' + unitNum + '.' + (idx + 1));
      var inputName = 'x', inLabel = 'Parameter', inUnit = '', minVal = 0, maxVal = 100, defaultVal = 50, stepVal = 1;
      var outLabel = 'Calculated Result', outUnit = m.result_unit || m.units || '';
      var formulaText = m.expression || m.equation || m.javascript_expression || '';
      var notes = m.assumption || m.assumptions || m.limitations || '';

      if (m.input) {
        inputName = m.input.name || 'x';
        inLabel = m.input.label || 'Parameter';
        inUnit = m.input.unit || '';
        minVal = m.input.min !== undefined ? m.input.min : 0;
        maxVal = m.input.max !== undefined ? m.input.max : 100;
        defaultVal = m.input.default !== undefined ? m.input.default : ((minVal + maxVal) / 2);
        stepVal = m.input.step || ((maxVal - minVal) / 100);
      } else if (m.vars && Array.isArray(m.vars) && m.vars.length > 0) {
        var v0 = m.vars[0];
        inputName = v0[0];
        inLabel = v0[1];
        minVal = v0[2];
        maxVal = v0[3];
        defaultVal = v0[4];
        stepVal = v0[5] || ((maxVal - minVal) / 100);
      }

      function computeY(xVal) {
        try {
          if (typeof evaluate === 'function' && m.id !== undefined) {
            return evaluate(m.id, xVal);
          }
          if (m.input && m.expression) {
            return (new Function(inputName, 'return (' + m.expression + ');'))(xVal);
          } else if (m.vars && m.javascript_expression) {
            var vObj = {};
            m.vars.forEach(function(v) { vObj[v[0]] = v[4]; });
            vObj[inputName] = xVal;
            return (new Function('v', 'return (' + m.javascript_expression + ');'))(vObj);
          }
        } catch(e) {
          return xVal * 1.5;
        }
        return xVal;
      }

      var card = document.createElement('section');
      card.className = 'sim-card model';
      card.style.background = '#0f172a';
      card.style.border = '1px solid #334155';
      card.style.borderRadius = '8px';
      card.style.padding = '16px';
      card.style.marginBottom = '20px';
      card.style.color = '#f8fafc';
      
      card.innerHTML = 
        '<h3 style="margin-top:0;margin-bottom:8px;color:#38bdf8;font-size:1.15rem;">' + titleText + '</h3>' +
        (formulaText ? '<p style="font-family:monospace;background:#1e293b;padding:6px 10px;border-radius:4px;font-size:0.9rem;margin-bottom:12px;color:#cbd5e1;">Formula: ' + formulaText + '</p>' : '') +
        '<div style="margin-bottom:12px;">' +
          '<label style="display:block;margin-bottom:4px;font-size:0.9rem;color:#94a3b8;">' + inLabel + ': <strong class="val-display" style="color:#f8fafc;">' + defaultVal + '</strong> ' + inUnit + '</label>' +
          '<input type="range" class="sim-slider" min="' + minVal + '" max="' + maxVal + '" step="' + stepVal + '" value="' + defaultVal + '" style="width:100%;cursor:pointer;">' +
        '</div>' +
        '<div style="background:#1e293b;border-radius:6px;padding:10px;margin-bottom:12px;">' +
          '<div style="font-size:0.85rem;color:#94a3b8;">' + outLabel + '</div>' +
          '<div class="out-display" style="font-size:1.3rem;font-weight:bold;color:#38bdf8;">--</div>' +
        '</div>' +
        '<svg class="sim-plot" viewBox="0 0 500 180" style="width:100%;height:auto;background:#020617;border-radius:6px;border:1px solid #1e293b;margin-bottom:8px;"></svg>' +
        (notes ? '<p style="font-size:0.8rem;color:#64748b;margin:0;">Note: ' + notes + '</p>' : '');
        
      container.appendChild(card);
      
      var input = card.querySelector('.sim-slider');
      var valDisplay = card.querySelector('.val-display');
      var outDisplay = card.querySelector('.out-display');
      var plot = card.querySelector('.sim-plot');
      
      function update() {
        var x = parseFloat(input.value);
        valDisplay.textContent = x.toFixed(2);
        var y = computeY(x);
        var prettyY = (typeof y === 'number') ? (Math.abs(y) > 1e4 || (Math.abs(y) < 0.01 && y !== 0) ? y.toExponential(3) : y.toFixed(3)) : y;
        outDisplay.textContent = prettyY + (outUnit ? ' ' + outUnit : '');
        
        var pts = [];
        var span = maxVal - minVal;
        if (span <= 0) span = 1;
        var lo = 1e9, hi = -1e9;
        var yVals = [];
        for (var step = 0; step <= 20; step++) {
          var px = minVal + (step / 20) * span;
          var py = computeY(px);
          if (typeof py !== 'number' || isNaN(py)) py = px;
          yVals.push(py);
          if (py < lo) lo = py;
          if (py > hi) hi = py;
        }
        var ySpan = (hi - lo);
        if (ySpan === 0) { ySpan = 1; lo -= 0.5; }
        for (var i = 0; i <= 20; i++) {
          var svgX = 38 + (i / 20) * (478 - 38);
          var svgY = 142 - ((yVals[i] - lo) / ySpan) * (142 - 28);
          pts.push(svgX.toFixed(1) + ',' + svgY.toFixed(1));
        }
        var poly = pts.join(' ');
        var cx = (38 + ((x - minVal) / span) * 440).toFixed(2);
        var cy = (142 - (y - lo) / ySpan * 114).toFixed(2);
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

