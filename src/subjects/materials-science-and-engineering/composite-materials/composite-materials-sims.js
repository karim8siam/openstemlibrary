/* Composite Materials Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Nominal fiber volume from mass fraction",
    "input": {
      "name": "w",
      "label": "Fiber mass fraction",
      "min": 0.2,
      "max": 0.8,
      "default": 0.6,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "(w/1.8)/(w/1.8+(1-w)/1.2)",
    "result_unit": "fraction",
    "assumptions": "No voids, two phases, hypothetical fiber and matrix densities 1.8 and 1.2 g/cm3; no sizing or fillers",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Void-free mixture density",
    "input": {
      "name": "Vf",
      "label": "Fiber volume fraction",
      "min": 0.15,
      "max": 0.75,
      "default": 0.5,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "1.8*Vf+1.2*(1-Vf)",
    "result_unit": "g/cm3",
    "assumptions": "Two constituents with densities 1.8 and 1.2 g/cm3, zero voids, no chemical volume change",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Aligned axial iso-strain modulus",
    "input": {
      "name": "Vf",
      "label": "Fiber volume fraction",
      "min": 0.1,
      "max": 0.75,
      "default": 0.55,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "230*Vf+3*(1-Vf)",
    "result_unit": "GPa",
    "assumptions": "Long straight aligned fibers, perfect bond, Ef=230 GPa and Em=3 GPa; only small-strain axial modulus",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Ideal inverse-mixture transverse modulus",
    "input": {
      "name": "Vf",
      "label": "Fiber volume fraction",
      "min": 0.1,
      "max": 0.75,
      "default": 0.55,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "1/(Vf/230+(1-Vf)/3)",
    "result_unit": "GPa",
    "assumptions": "Illustrative serial isostress idealization; Ef=230 GPa, Em=3 GPa; not measured true transverse property",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Reciprocal Poisson ratio",
    "input": {
      "name": "E2",
      "label": "Transverse modulus",
      "min": 3,
      "max": 25,
      "default": 9,
      "step": 0.5,
      "unit": "GPa"
    },
    "expression": "0.28*E2/135",
    "result_unit": "dimensionless",
    "assumptions": "E1=135 GPa, nu12=0.28, reciprocal plane-stress orthotropic linear elasticity",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Local shear from global axial tension",
    "input": {
      "name": "theta",
      "label": "Ply angle",
      "min": 0,
      "max": 90,
      "default": 45,
      "step": 1,
      "unit": "degrees"
    },
    "expression": "100*Math.abs(Math.sin(theta*Math.PI/180)*Math.cos(theta*Math.PI/180))",
    "result_unit": "MPa",
    "assumptions": "Global uniaxial tensile stress 100 MPa, ideal stress tensor rotation; shear sign omitted; does not assess failure",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "A11 for a homogeneous aligned panel",
    "input": {
      "name": "t",
      "label": "Laminate thickness",
      "min": 0.5,
      "max": 8,
      "default": 2,
      "step": 0.1,
      "unit": "mm"
    },
    "expression": "135000*t",
    "result_unit": "N/mm",
    "assumptions": "Qbar11=135000 MPa; for thickness t in mm, A11=Qbar11*t in N/mm; single homogeneous aligned region",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "D11 for a homogeneous aligned panel",
    "input": {
      "name": "t",
      "label": "Laminate thickness",
      "min": 0.5,
      "max": 8,
      "default": 2,
      "step": 0.1,
      "unit": "mm"
    },
    "expression": "135000*Math.pow(t,3)/12",
    "result_unit": "N mm",
    "assumptions": "Qbar11=135000 N/mm2; D11=Qbar11*t^3/12 in N mm per unit width under classical thin plate assumptions",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Ideal first-order cure conversion",
    "input": {
      "name": "t",
      "label": "Isothermal cure time",
      "min": 0,
      "max": 120,
      "default": 30,
      "step": 2,
      "unit": "min"
    },
    "expression": "100*(1-Math.exp(-0.035*t))",
    "result_unit": "% conversion",
    "assumptions": "Hypothetical first-order rate 0.035/min, isothermal, no diffusion limitation or cure exotherm",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Darcy superficial infusion velocity",
    "input": {
      "name": "K",
      "label": "Porous permeability",
      "min": 1,
      "max": 50,
      "default": 10,
      "step": 1,
      "unit": "10^-12 m2"
    },
    "expression": "K*1e-12*100000/0.5*1000000",
    "result_unit": "micrometers/s",
    "assumptions": "Pressure gradient 100 kPa/m, viscosity 0.5 Pa s, one-dimensional Darcy flow without race tracking or variable cure viscosity",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Directional strength-utilization index",
    "input": {
      "name": "sigma",
      "label": "Positive longitudinal stress",
      "min": 100,
      "max": 1100,
      "default": 600,
      "step": 10,
      "unit": "MPa"
    },
    "expression": "sigma/1200",
    "result_unit": "dimensionless",
    "assumptions": "Unidirectional positive fiber-direction tension allowable 1200 MPa; a single uncoupled screening ratio",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Mode-I delamination driving ratio",
    "input": {
      "name": "G",
      "label": "Mode-I release rate",
      "min": 25,
      "max": 550,
      "default": 250,
      "step": 5,
      "unit": "J/m2"
    },
    "expression": "G/400",
    "result_unit": "dimensionless",
    "assumptions": "Assumed independent fixed initiation resistance GIc=400 J/m2, pure opening mode, simple scalar comparison; no bridging or mixed mode",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Ideal particulate composite density",
    "input": {
      "name": "Vp",
      "label": "Particle volume fraction",
      "min": 0.05,
      "max": 0.55,
      "default": 0.25,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "3.9*Vp+2.7*(1-Vp)",
    "result_unit": "g/cm3",
    "assumptions": "No voids, hypothetical ceramic particle density 3.9 g/cm3 and metal matrix density 2.7 g/cm3",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Toy percolation threshold behavior",
    "input": {
      "name": "phi",
      "label": "Conductive filler fraction",
      "min": 0.06,
      "max": 0.3,
      "default": 0.15,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "100*Math.pow(Math.max(0,phi-0.05),2)",
    "result_unit": "S/m",
    "assumptions": "Synthetic percolation-like response, phi_c=0.05, exponent 2 and coefficient 100 chosen for teaching, not a material prediction",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Illustrative ultrasonic POD curve",
    "input": {
      "name": "a",
      "label": "Flaw size",
      "min": 0.1,
      "max": 8,
      "default": 2,
      "step": 0.1,
      "unit": "mm"
    },
    "expression": "100/(1+Math.exp(-(a-3)/0.8))",
    "result_unit": "% detection",
    "assumptions": "Hypothetical logistics-style curve midpoint 3 mm, width 0.8 mm; NOT a validated probability-of-detection result",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Recovered fiber mass proxy",
    "input": {
      "name": "r",
      "label": "Material recovery yield",
      "min": 0,
      "max": 95,
      "default": 65,
      "step": 1,
      "unit": "%"
    },
    "expression": "75*r/100",
    "result_unit": "kg",
    "assumptions": "Hypothetical 100 kg feed with 75 kg fiber; yield is retained fiber mass fraction; excludes quality losses, emissions, energy, circularity",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Nominal fiber volume from mass fraction", "input": {"name": "w", "label": "Fiber mass fraction", "min": 0.2, "max": 0.8, "default": 0.6, "step": 0.01, "unit": "fraction"}, "expression": "(w/1.8)/(w/1.8+(1-w)/1.2)", "result_unit": "fraction", "assumptions": "No voids, two phases, hypothetical fiber and matrix densities 1.8 and 1.2 g/cm3; no sizing or fillers", "synthetic": true}, {"id": 1, "unit": 1, "title": "Void-free mixture density", "input": {"name": "Vf", "label": "Fiber volume fraction", "min": 0.15, "max": 0.75, "default": 0.5, "step": 0.01, "unit": "fraction"}, "expression": "1.8*Vf+1.2*(1-Vf)", "result_unit": "g/cm3", "assumptions": "Two constituents with densities 1.8 and 1.2 g/cm3, zero voids, no chemical volume change", "synthetic": true}, {"id": 2, "unit": 2, "title": "Aligned axial iso-strain modulus", "input": {"name": "Vf", "label": "Fiber volume fraction", "min": 0.1, "max": 0.75, "default": 0.55, "step": 0.01, "unit": "fraction"}, "expression": "230*Vf+3*(1-Vf)", "result_unit": "GPa", "assumptions": "Long straight aligned fibers, perfect bond, Ef=230 GPa and Em=3 GPa; only small-strain axial modulus", "synthetic": true}, {"id": 3, "unit": 2, "title": "Ideal inverse-mixture transverse modulus", "input": {"name": "Vf", "label": "Fiber volume fraction", "min": 0.1, "max": 0.75, "default": 0.55, "step": 0.01, "unit": "fraction"}, "expression": "1/(Vf/230+(1-Vf)/3)", "result_unit": "GPa", "assumptions": "Illustrative serial isostress idealization; Ef=230 GPa, Em=3 GPa; not measured true transverse property", "synthetic": true}, {"id": 4, "unit": 3, "title": "Reciprocal Poisson ratio", "input": {"name": "E2", "label": "Transverse modulus", "min": 3, "max": 25, "default": 9, "step": 0.5, "unit": "GPa"}, "expression": "0.28*E2/135", "result_unit": "dimensionless", "assumptions": "E1=135 GPa, nu12=0.28, reciprocal plane-stress orthotropic linear elasticity", "synthetic": true}, {"id": 5, "unit": 3, "title": "Local shear from global axial tension", "input": {"name": "theta", "label": "Ply angle", "min": 0, "max": 90, "default": 45, "step": 1, "unit": "degrees"}, "expression": "100*Math.abs(Math.sin(theta*Math.PI/180)*Math.cos(theta*Math.PI/180))", "result_unit": "MPa", "assumptions": "Global uniaxial tensile stress 100 MPa, ideal stress tensor rotation; shear sign omitted; does not assess failure", "synthetic": true}, {"id": 6, "unit": 4, "title": "A11 for a homogeneous aligned panel", "input": {"name": "t", "label": "Laminate thickness", "min": 0.5, "max": 8, "default": 2, "step": 0.1, "unit": "mm"}, "expression": "135000*t", "result_unit": "N/mm", "assumptions": "Qbar11=135000 MPa; for thickness t in mm, A11=Qbar11*t in N/mm; single homogeneous aligned region", "synthetic": true}, {"id": 7, "unit": 4, "title": "D11 for a homogeneous aligned panel", "input": {"name": "t", "label": "Laminate thickness", "min": 0.5, "max": 8, "default": 2, "step": 0.1, "unit": "mm"}, "expression": "135000*Math.pow(t,3)/12", "result_unit": "N mm", "assumptions": "Qbar11=135000 N/mm2; D11=Qbar11*t^3/12 in N mm per unit width under classical thin plate assumptions", "synthetic": true}, {"id": 8, "unit": 5, "title": "Ideal first-order cure conversion", "input": {"name": "t", "label": "Isothermal cure time", "min": 0, "max": 120, "default": 30, "step": 2, "unit": "min"}, "expression": "100*(1-Math.exp(-0.035*t))", "result_unit": "% conversion", "assumptions": "Hypothetical first-order rate 0.035/min, isothermal, no diffusion limitation or cure exotherm", "synthetic": true}, {"id": 9, "unit": 5, "title": "Darcy superficial infusion velocity", "input": {"name": "K", "label": "Porous permeability", "min": 1, "max": 50, "default": 10, "step": 1, "unit": "10^-12 m2"}, "expression": "K*1e-12*100000/0.5*1000000", "result_unit": "micrometers/s", "assumptions": "Pressure gradient 100 kPa/m, viscosity 0.5 Pa s, one-dimensional Darcy flow without race tracking or variable cure viscosity", "synthetic": true}, {"id": 10, "unit": 6, "title": "Directional strength-utilization index", "input": {"name": "sigma", "label": "Positive longitudinal stress", "min": 100, "max": 1100, "default": 600, "step": 10, "unit": "MPa"}, "expression": "sigma/1200", "result_unit": "dimensionless", "assumptions": "Unidirectional positive fiber-direction tension allowable 1200 MPa; a single uncoupled screening ratio", "synthetic": true}, {"id": 11, "unit": 6, "title": "Mode-I delamination driving ratio", "input": {"name": "G", "label": "Mode-I release rate", "min": 25, "max": 550, "default": 250, "step": 5, "unit": "J/m2"}, "expression": "G/400", "result_unit": "dimensionless", "assumptions": "Assumed independent fixed initiation resistance GIc=400 J/m2, pure opening mode, simple scalar comparison; no bridging or mixed mode", "synthetic": true}, {"id": 12, "unit": 7, "title": "Ideal particulate composite density", "input": {"name": "Vp", "label": "Particle volume fraction", "min": 0.05, "max": 0.55, "default": 0.25, "step": 0.01, "unit": "fraction"}, "expression": "3.9*Vp+2.7*(1-Vp)", "result_unit": "g/cm3", "assumptions": "No voids, hypothetical ceramic particle density 3.9 g/cm3 and metal matrix density 2.7 g/cm3", "synthetic": true}, {"id": 13, "unit": 7, "title": "Toy percolation threshold behavior", "input": {"name": "phi", "label": "Conductive filler fraction", "min": 0.06, "max": 0.3, "default": 0.15, "step": 0.01, "unit": "fraction"}, "expression": "100*Math.pow(Math.max(0,phi-0.05),2)", "result_unit": "S/m", "assumptions": "Synthetic percolation-like response, phi_c=0.05, exponent 2 and coefficient 100 chosen for teaching, not a material prediction", "synthetic": true}, {"id": 14, "unit": 8, "title": "Illustrative ultrasonic POD curve", "input": {"name": "a", "label": "Flaw size", "min": 0.1, "max": 8, "default": 2, "step": 0.1, "unit": "mm"}, "expression": "100/(1+Math.exp(-(a-3)/0.8))", "result_unit": "% detection", "assumptions": "Hypothetical logistics-style curve midpoint 3 mm, width 0.8 mm; NOT a validated probability-of-detection result", "synthetic": true}, {"id": 15, "unit": 8, "title": "Recovered fiber mass proxy", "input": {"name": "r", "label": "Material recovery yield", "min": 0, "max": 95, "default": 65, "step": 1, "unit": "%"}, "expression": "75*r/100", "result_unit": "kg", "assumptions": "Hypothetical 100 kg feed with 75 kg fiber; yield is retained fiber mass fraction; excludes quality losses, emissions, energy, circularity", "synthetic": true}];
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

