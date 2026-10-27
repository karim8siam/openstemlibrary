/* Phase Transformations Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Lever-rule product fraction",
    "input": {
      "name": "c",
      "label": "Bulk solute fraction",
      "min": 0.16,
      "max": 0.74,
      "default": 0.35,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "(c-0.15)/(0.75-0.15)",
    "result_unit": "fraction",
    "assumptions": "Two-phase binary tie line c_alpha=0.15 and c_beta=0.75; single consistent mass basis, full equilibrium",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Undercooling driving force",
    "input": {
      "name": "dt",
      "label": "Undercooling",
      "min": 1,
      "max": 100,
      "default": 50,
      "step": 1,
      "unit": "K"
    },
    "expression": "10000*dt/1000",
    "result_unit": "J/mol",
    "assumptions": "Transition temperature 1000 K, molar latent heat 10000 J/mol, near-transition linearization",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Classical critical nucleus radius",
    "input": {
      "name": "g",
      "label": "Interfacial energy",
      "min": 0.04,
      "max": 0.24,
      "default": 0.12,
      "step": 0.005,
      "unit": "J/m\u00b2"
    },
    "expression": "2*g/2e8*1e9",
    "result_unit": "nm",
    "assumptions": "Spherical unstrained capillarity, |Delta g_v|=2e8 J/m\u00b3; nanoscale approximation may fail",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Heterogeneous shape factor",
    "input": {
      "name": "a",
      "label": "Contact angle",
      "min": 10,
      "max": 175,
      "default": 60,
      "step": 1,
      "unit": "degrees"
    },
    "expression": "(2+Math.cos(a*Math.PI/180))*Math.pow(1-Math.cos(a*Math.PI/180),2)/4",
    "result_unit": "fraction",
    "assumptions": "Ideal spherical cap and planar chemically homogeneous substrate; barrier is f(theta)*barrier_hom",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Diffusion penetration scale",
    "input": {
      "name": "t",
      "label": "Elapsed time",
      "min": 5,
      "max": 1000,
      "default": 400,
      "step": 5,
      "unit": "s"
    },
    "expression": "Math.sqrt(1e-14*t)*1e6",
    "result_unit": "\u00b5m",
    "assumptions": "Diffusivity=1e-14 m\u00b2/s constant, characteristic sqrt(Dt) only; not a moving-boundary solution",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Isothermal Avrami transformed fraction",
    "input": {
      "name": "t",
      "label": "Hold time",
      "min": 0,
      "max": 900,
      "default": 300,
      "step": 5,
      "unit": "s"
    },
    "expression": "1-Math.exp(-Math.pow(0.004*t,2.5))",
    "result_unit": "fraction",
    "assumptions": "Effective isothermal JMAK k=0.004 s\u207b\u00b9, n=2.5; single-stage homogeneous idealization",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Scheil residual-liquid composition",
    "input": {
      "name": "f",
      "label": "Fraction solidified",
      "min": 0,
      "max": 0.9,
      "default": 0.64,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "0.05*Math.pow(1-f,-0.5)",
    "result_unit": "fraction",
    "assumptions": "Constant partition coefficient k=0.5, initial c0=0.05, mixed liquid, no back-diffusion, no terminal new phases",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Cooling-window residence time",
    "input": {
      "name": "r",
      "label": "Cooling rate",
      "min": 1,
      "max": 80,
      "default": 10,
      "step": 1,
      "unit": "K/s"
    },
    "expression": "300/r",
    "result_unit": "s",
    "assumptions": "Fixed 300 K thermal window, constant rate through window; not a CCT phase-fraction predictor",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Steel idealized carbide mass fraction",
    "input": {
      "name": "c",
      "label": "Overall carbon concentration",
      "min": 0.03,
      "max": 1.8,
      "default": 0.76,
      "step": 0.01,
      "unit": "wt%"
    },
    "expression": "(c-0.022)/(6.67-0.022)",
    "result_unit": "fraction",
    "assumptions": "Only illustrative alpha+cementite tie line just below eutectoid, C_alpha=0.022 wt%, C_cementite=6.67 wt%, full equilibrium",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Empirical martensite cooling fraction",
    "input": {
      "name": "t",
      "label": "Steel temperature",
      "min": 100,
      "max": 350,
      "default": 300,
      "step": 5,
      "unit": "\u00b0C"
    },
    "expression": "1-Math.exp(-0.011*(350-t))",
    "result_unit": "fraction",
    "assumptions": "Koistinen\u2013Marburger pedagogical fit, Ms=350 \u00b0C, alpha=0.011 K\u207b\u00b9, valid only below Ms and within invented domain",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Coarsening characteristic radius",
    "input": {
      "name": "t",
      "label": "Aging duration",
      "min": 0,
      "max": 70,
      "default": 7,
      "step": 1,
      "unit": "h"
    },
    "expression": "Math.cbrt(Math.pow(20,3)+8000*t)",
    "result_unit": "nm",
    "assumptions": "LSW-style R0=20 nm, K=8000 nm\u00b3/h, idealized dilute diffusion-controlled coarsening",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Relative obstacle spacing strength",
    "input": {
      "name": "s",
      "label": "Obstacle spacing",
      "min": 40,
      "max": 200,
      "default": 80,
      "step": 2,
      "unit": "nm"
    },
    "expression": "80/s",
    "result_unit": "relative",
    "assumptions": "Only sigma_relative proportional to 1/spacing with baseline at 80 nm; no absolute strength or particle physics claimed",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Order parameter from intensity",
    "input": {
      "name": "i",
      "label": "Normalized superlattice intensity",
      "min": 0,
      "max": 1,
      "default": 0.16,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "Math.sqrt(i)",
    "result_unit": "dimensionless",
    "assumptions": "Diffraction intensity proportional to S\u00b2 under fixed geometry and normalized fully ordered reference",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Free isotropic linear expansion",
    "input": {
      "name": "v",
      "label": "Transformation volume change",
      "min": 0,
      "max": 8,
      "default": 3,
      "step": 0.25,
      "unit": "percent"
    },
    "expression": "100*(Math.pow(1+v/100,1/3)-1)",
    "result_unit": "percent",
    "assumptions": "Free isotropic strain, no mechanical constraint, illustrative transformation-associated volume change",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "DSC specific transition enthalpy",
    "input": {
      "name": "q",
      "label": "Measured heat",
      "min": 0.1,
      "max": 2.0,
      "default": 0.6,
      "step": 0.05,
      "unit": "J"
    },
    "expression": "q/0.01",
    "result_unit": "J/g",
    "assumptions": "Sample mass 10 mg (0.01 g), baseline and calibration assumed corrected",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Thermal diffusion Fourier number",
    "input": {
      "name": "t",
      "label": "Hold duration",
      "min": 1,
      "max": 120,
      "default": 15,
      "step": 1,
      "unit": "s"
    },
    "expression": "1e-5*t/Math.pow(0.01,2)",
    "result_unit": "dimensionless",
    "assumptions": "Thermal diffusivity 1e-5 m\u00b2/s, half-thickness L=10 mm, simple conduction scale, no convection model",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Lever-rule product fraction", "input": {"name": "c", "label": "Bulk solute fraction", "min": 0.16, "max": 0.74, "default": 0.35, "step": 0.01, "unit": "fraction"}, "expression": "(c-0.15)/(0.75-0.15)", "result_unit": "fraction", "assumptions": "Two-phase binary tie line c_alpha=0.15 and c_beta=0.75; single consistent mass basis, full equilibrium", "synthetic": true}, {"id": 1, "unit": 1, "title": "Undercooling driving force", "input": {"name": "dt", "label": "Undercooling", "min": 1, "max": 100, "default": 50, "step": 1, "unit": "K"}, "expression": "10000*dt/1000", "result_unit": "J/mol", "assumptions": "Transition temperature 1000 K, molar latent heat 10000 J/mol, near-transition linearization", "synthetic": true}, {"id": 2, "unit": 2, "title": "Classical critical nucleus radius", "input": {"name": "g", "label": "Interfacial energy", "min": 0.04, "max": 0.24, "default": 0.12, "step": 0.005, "unit": "J/m²"}, "expression": "2*g/2e8*1e9", "result_unit": "nm", "assumptions": "Spherical unstrained capillarity, |Delta g_v|=2e8 J/m³; nanoscale approximation may fail", "synthetic": true}, {"id": 3, "unit": 2, "title": "Heterogeneous shape factor", "input": {"name": "a", "label": "Contact angle", "min": 10, "max": 175, "default": 60, "step": 1, "unit": "degrees"}, "expression": "(2+Math.cos(a*Math.PI/180))*Math.pow(1-Math.cos(a*Math.PI/180),2)/4", "result_unit": "fraction", "assumptions": "Ideal spherical cap and planar chemically homogeneous substrate; barrier is f(theta)*barrier_hom", "synthetic": true}, {"id": 4, "unit": 3, "title": "Diffusion penetration scale", "input": {"name": "t", "label": "Elapsed time", "min": 5, "max": 1000, "default": 400, "step": 5, "unit": "s"}, "expression": "Math.sqrt(1e-14*t)*1e6", "result_unit": "µm", "assumptions": "Diffusivity=1e-14 m²/s constant, characteristic sqrt(Dt) only; not a moving-boundary solution", "synthetic": true}, {"id": 5, "unit": 3, "title": "Isothermal Avrami transformed fraction", "input": {"name": "t", "label": "Hold time", "min": 0, "max": 900, "default": 300, "step": 5, "unit": "s"}, "expression": "1-Math.exp(-Math.pow(0.004*t,2.5))", "result_unit": "fraction", "assumptions": "Effective isothermal JMAK k=0.004 s⁻¹, n=2.5; single-stage homogeneous idealization", "synthetic": true}, {"id": 6, "unit": 4, "title": "Scheil residual-liquid composition", "input": {"name": "f", "label": "Fraction solidified", "min": 0, "max": 0.9, "default": 0.64, "step": 0.01, "unit": "fraction"}, "expression": "0.05*Math.pow(1-f,-0.5)", "result_unit": "fraction", "assumptions": "Constant partition coefficient k=0.5, initial c0=0.05, mixed liquid, no back-diffusion, no terminal new phases", "synthetic": true}, {"id": 7, "unit": 4, "title": "Cooling-window residence time", "input": {"name": "r", "label": "Cooling rate", "min": 1, "max": 80, "default": 10, "step": 1, "unit": "K/s"}, "expression": "300/r", "result_unit": "s", "assumptions": "Fixed 300 K thermal window, constant rate through window; not a CCT phase-fraction predictor", "synthetic": true}, {"id": 8, "unit": 5, "title": "Steel idealized carbide mass fraction", "input": {"name": "c", "label": "Overall carbon concentration", "min": 0.03, "max": 1.8, "default": 0.76, "step": 0.01, "unit": "wt%"}, "expression": "(c-0.022)/(6.67-0.022)", "result_unit": "fraction", "assumptions": "Only illustrative alpha+cementite tie line just below eutectoid, C_alpha=0.022 wt%, C_cementite=6.67 wt%, full equilibrium", "synthetic": true}, {"id": 9, "unit": 5, "title": "Empirical martensite cooling fraction", "input": {"name": "t", "label": "Steel temperature", "min": 100, "max": 350, "default": 300, "step": 5, "unit": "°C"}, "expression": "1-Math.exp(-0.011*(350-t))", "result_unit": "fraction", "assumptions": "Koistinen–Marburger pedagogical fit, Ms=350 °C, alpha=0.011 K⁻¹, valid only below Ms and within invented domain", "synthetic": true}, {"id": 10, "unit": 6, "title": "Coarsening characteristic radius", "input": {"name": "t", "label": "Aging duration", "min": 0, "max": 70, "default": 7, "step": 1, "unit": "h"}, "expression": "Math.cbrt(Math.pow(20,3)+8000*t)", "result_unit": "nm", "assumptions": "LSW-style R0=20 nm, K=8000 nm³/h, idealized dilute diffusion-controlled coarsening", "synthetic": true}, {"id": 11, "unit": 6, "title": "Relative obstacle spacing strength", "input": {"name": "s", "label": "Obstacle spacing", "min": 40, "max": 200, "default": 80, "step": 2, "unit": "nm"}, "expression": "80/s", "result_unit": "relative", "assumptions": "Only sigma_relative proportional to 1/spacing with baseline at 80 nm; no absolute strength or particle physics claimed", "synthetic": true}, {"id": 12, "unit": 7, "title": "Order parameter from intensity", "input": {"name": "i", "label": "Normalized superlattice intensity", "min": 0, "max": 1, "default": 0.16, "step": 0.01, "unit": "fraction"}, "expression": "Math.sqrt(i)", "result_unit": "dimensionless", "assumptions": "Diffraction intensity proportional to S² under fixed geometry and normalized fully ordered reference", "synthetic": true}, {"id": 13, "unit": 7, "title": "Free isotropic linear expansion", "input": {"name": "v", "label": "Transformation volume change", "min": 0, "max": 8, "default": 3, "step": 0.25, "unit": "percent"}, "expression": "100*(Math.pow(1+v/100,1/3)-1)", "result_unit": "percent", "assumptions": "Free isotropic strain, no mechanical constraint, illustrative transformation-associated volume change", "synthetic": true}, {"id": 14, "unit": 8, "title": "DSC specific transition enthalpy", "input": {"name": "q", "label": "Measured heat", "min": 0.1, "max": 2.0, "default": 0.6, "step": 0.05, "unit": "J"}, "expression": "q/0.01", "result_unit": "J/g", "assumptions": "Sample mass 10 mg (0.01 g), baseline and calibration assumed corrected", "synthetic": true}, {"id": 15, "unit": 8, "title": "Thermal diffusion Fourier number", "input": {"name": "t", "label": "Hold duration", "min": 1, "max": 120, "default": 15, "step": 1, "unit": "s"}, "expression": "1e-5*t/Math.pow(0.01,2)", "result_unit": "dimensionless", "assumptions": "Thermal diffusivity 1e-5 m²/s, half-thickness L=10 mm, simple conduction scale, no convection model", "synthetic": true}];
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
    var mMatch = simType.match(/(\d+)$/);
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

