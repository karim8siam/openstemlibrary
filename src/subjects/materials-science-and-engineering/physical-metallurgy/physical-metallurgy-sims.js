/* Physical Metallurgy Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Resolved shear stress",
    "input": {
      "name": "theta",
      "label": "Angle to slip plane normal",
      "min": 35,
      "max": 80,
      "default": 55,
      "step": 1,
      "unit": "degrees"
    },
    "expression": "120*Math.cos(theta*Math.PI/180)*Math.cos(55*Math.PI/180)",
    "result_unit": "MPa",
    "assumptions": "Uniaxial sigma=120 MPa; slip-direction angle fixed at 55 degrees; theta>=35 ensures geometrically compatible orthogonal plane normal and slip direction; Schmid factor <=0.5",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Hall\u2013Petch illustrative yield stress",
    "input": {
      "name": "d",
      "label": "Grain diameter",
      "min": 4,
      "max": 120,
      "default": 24,
      "step": 2,
      "unit": "\u00b5m"
    },
    "expression": "90+0.45/Math.sqrt(d*1e-6)",
    "result_unit": "MPa",
    "assumptions": "sigma0=90 MPa, ky=0.45 MPa sqrt(m), no extrapolation to nanograins or temperature effects",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Ideal binary configurational entropy",
    "input": {
      "name": "x",
      "label": "Mole fraction of B",
      "min": 0.05,
      "max": 0.95,
      "default": 0.5,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "-8.314462618*(x*Math.log(x)+(1-x)*Math.log(1-x))",
    "result_unit": "J/(mol K)",
    "assumptions": "Ideal random substitutional mixing, entropy only; no ordering or excess interaction enthalpy",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Equilibrium beta-phase mass fraction",
    "input": {
      "name": "c",
      "label": "Overall solute fraction",
      "min": 0.1,
      "max": 0.7,
      "default": 0.34,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "(c-0.1)/0.6",
    "result_unit": "fraction",
    "assumptions": "Two hypothetical phases with endpoints c_alpha=0.1 and c_beta=0.7 at one temperature, equal composition basis",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Scheil residual-liquid enrichment",
    "input": {
      "name": "fs",
      "label": "Fraction solid",
      "min": 0,
      "max": 0.8,
      "default": 0.5,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "0.04*Math.pow(1-fs,-0.5)",
    "result_unit": "fraction",
    "assumptions": "Initial solute fraction 0.04, partition coefficient k=0.5, completely mixed liquid, zero solid back-diffusion; not final-eutectic predictor",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Solidification shrinkage volume",
    "input": {
      "name": "v",
      "label": "Starting liquid volume",
      "min": 20,
      "max": 400,
      "default": 200,
      "step": 5,
      "unit": "cm\u00b3"
    },
    "expression": "0.04*v",
    "result_unit": "cm\u00b3",
    "assumptions": "Assumed 4% volume shrinkage from initial liquid volume; ideal conservation estimate, not a riser design",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Rolling true-thickness strain",
    "input": {
      "name": "tf",
      "label": "Final strip thickness",
      "min": 2,
      "max": 9,
      "default": 6,
      "step": 0.1,
      "unit": "mm"
    },
    "expression": "Math.log(10/tf)",
    "result_unit": "dimensionless",
    "assumptions": "Starting thickness 10 mm; uniform thickness compression; ignores spread, friction and redundant strain",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Simplified isothermal grain growth",
    "input": {
      "name": "t",
      "label": "Annealing duration",
      "min": 0,
      "max": 48,
      "default": 10,
      "step": 1,
      "unit": "h"
    },
    "expression": "Math.sqrt(100+10*t)",
    "result_unit": "\u00b5m",
    "assumptions": "Initial grain diameter 10 \u00b5m, parabolic K=10 \u00b5m\u00b2/h; no pinning, abnormal growth or transient recrystallization",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Fictional Jominy hardness profile",
    "input": {
      "name": "z",
      "label": "Distance from quenched end",
      "min": 0,
      "max": 50,
      "default": 15,
      "step": 1,
      "unit": "mm"
    },
    "expression": "30+25*Math.exp(-z/12)",
    "result_unit": "HRC",
    "assumptions": "Hypothetical HRC profile, never measured, unrelated to an actual grade; only a curve-shape illustration",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Thermal Fourier-number estimate",
    "input": {
      "name": "t",
      "label": "Cooling or heating time",
      "min": 1,
      "max": 240,
      "default": 40,
      "step": 1,
      "unit": "s"
    },
    "expression": "1e-5*t/(0.01*0.01)",
    "result_unit": "dimensionless",
    "assumptions": "Thermal diffusivity 1e-5 m\u00b2/s, length 10 mm; conduction scale only, not a phase or quench predictor",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Specific stiffness comparison",
    "input": {
      "name": "rho",
      "label": "Density",
      "min": 2400,
      "max": 9000,
      "default": 2700,
      "step": 100,
      "unit": "kg/m\u00b3"
    },
    "expression": "70/(rho/1000)",
    "result_unit": "GPa per (g/cm\u00b3)",
    "assumptions": "Young modulus fixed at 70 GPa, mass density varied synthetically; a screening index for selected geometries",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Copper conductor resistance",
    "input": {
      "name": "L",
      "label": "Copper conductor length",
      "min": 0.1,
      "max": 10,
      "default": 3,
      "step": 0.1,
      "unit": "m"
    },
    "expression": "1.72e-8*L/1e-6",
    "result_unit": "ohm",
    "assumptions": "Electrical resistivity 1.72e-8 ohm m and fixed area 1 mm\u00b2 at a single temperature; no contact resistance",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Crack-size limited nominal stress",
    "input": {
      "name": "a",
      "label": "Crack size",
      "min": 0.25,
      "max": 7,
      "default": 2,
      "step": 0.05,
      "unit": "mm"
    },
    "expression": "40/(1.12*Math.sqrt(Math.PI*a/1000))",
    "result_unit": "MPa",
    "assumptions": "K=40 MPa sqrt(m), Y=1.12 fixed; elementary mode-I LEFM criterion only, no plane-strain or geometry validation",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Relative creep stress sensitivity",
    "input": {
      "name": "s",
      "label": "Applied stress",
      "min": 50,
      "max": 250,
      "default": 150,
      "step": 5,
      "unit": "MPa"
    },
    "expression": "Math.pow(s/100,4)",
    "result_unit": "relative",
    "assumptions": "Norton stress exponent n=4 at one temperature, normalized rate=1 at 100 MPa; no time-to-failure implied",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Weld line energy",
    "input": {
      "name": "v",
      "label": "Welding travel speed",
      "min": 1,
      "max": 15,
      "default": 5,
      "step": 0.5,
      "unit": "mm/s"
    },
    "expression": "0.8*20*150/v",
    "result_unit": "J/mm",
    "assumptions": "Illustrative arc 20 V \u00d7150 A, efficiency eta=0.8, constant travel; actual weld pool geometry excluded",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Independent-counting fraction error",
    "input": {
      "name": "N",
      "label": "Number of sampled points",
      "min": 50,
      "max": 2000,
      "default": 500,
      "step": 25,
      "unit": "samples"
    },
    "expression": "Math.sqrt(0.25*0.75/N)",
    "result_unit": "fraction",
    "assumptions": "True hypothetical phase area fraction 0.25, independent points; correlated microstructure produces larger effective uncertainty",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Resolved shear stress", "input": {"name": "theta", "label": "Angle to slip plane normal", "min": 35, "max": 80, "default": 55, "step": 1, "unit": "degrees"}, "expression": "120*Math.cos(theta*Math.PI/180)*Math.cos(55*Math.PI/180)", "result_unit": "MPa", "assumptions": "Uniaxial sigma=120 MPa; slip-direction angle fixed at 55 degrees; theta>=35 ensures geometrically compatible orthogonal plane normal and slip direction; Schmid factor <=0.5", "synthetic": true}, {"id": 1, "unit": 1, "title": "Hall–Petch illustrative yield stress", "input": {"name": "d", "label": "Grain diameter", "min": 4, "max": 120, "default": 24, "step": 2, "unit": "µm"}, "expression": "90+0.45/Math.sqrt(d*1e-6)", "result_unit": "MPa", "assumptions": "sigma0=90 MPa, ky=0.45 MPa sqrt(m), no extrapolation to nanograins or temperature effects", "synthetic": true}, {"id": 2, "unit": 2, "title": "Ideal binary configurational entropy", "input": {"name": "x", "label": "Mole fraction of B", "min": 0.05, "max": 0.95, "default": 0.5, "step": 0.01, "unit": "fraction"}, "expression": "-8.314462618*(x*Math.log(x)+(1-x)*Math.log(1-x))", "result_unit": "J/(mol K)", "assumptions": "Ideal random substitutional mixing, entropy only; no ordering or excess interaction enthalpy", "synthetic": true}, {"id": 3, "unit": 2, "title": "Equilibrium beta-phase mass fraction", "input": {"name": "c", "label": "Overall solute fraction", "min": 0.1, "max": 0.7, "default": 0.34, "step": 0.01, "unit": "fraction"}, "expression": "(c-0.1)/0.6", "result_unit": "fraction", "assumptions": "Two hypothetical phases with endpoints c_alpha=0.1 and c_beta=0.7 at one temperature, equal composition basis", "synthetic": true}, {"id": 4, "unit": 3, "title": "Scheil residual-liquid enrichment", "input": {"name": "fs", "label": "Fraction solid", "min": 0, "max": 0.8, "default": 0.5, "step": 0.01, "unit": "fraction"}, "expression": "0.04*Math.pow(1-fs,-0.5)", "result_unit": "fraction", "assumptions": "Initial solute fraction 0.04, partition coefficient k=0.5, completely mixed liquid, zero solid back-diffusion; not final-eutectic predictor", "synthetic": true}, {"id": 5, "unit": 3, "title": "Solidification shrinkage volume", "input": {"name": "v", "label": "Starting liquid volume", "min": 20, "max": 400, "default": 200, "step": 5, "unit": "cm³"}, "expression": "0.04*v", "result_unit": "cm³", "assumptions": "Assumed 4% volume shrinkage from initial liquid volume; ideal conservation estimate, not a riser design", "synthetic": true}, {"id": 6, "unit": 4, "title": "Rolling true-thickness strain", "input": {"name": "tf", "label": "Final strip thickness", "min": 2, "max": 9, "default": 6, "step": 0.1, "unit": "mm"}, "expression": "Math.log(10/tf)", "result_unit": "dimensionless", "assumptions": "Starting thickness 10 mm; uniform thickness compression; ignores spread, friction and redundant strain", "synthetic": true}, {"id": 7, "unit": 4, "title": "Simplified isothermal grain growth", "input": {"name": "t", "label": "Annealing duration", "min": 0, "max": 48, "default": 10, "step": 1, "unit": "h"}, "expression": "Math.sqrt(100+10*t)", "result_unit": "µm", "assumptions": "Initial grain diameter 10 µm, parabolic K=10 µm²/h; no pinning, abnormal growth or transient recrystallization", "synthetic": true}, {"id": 8, "unit": 5, "title": "Fictional Jominy hardness profile", "input": {"name": "z", "label": "Distance from quenched end", "min": 0, "max": 50, "default": 15, "step": 1, "unit": "mm"}, "expression": "30+25*Math.exp(-z/12)", "result_unit": "HRC", "assumptions": "Hypothetical HRC profile, never measured, unrelated to an actual grade; only a curve-shape illustration", "synthetic": true}, {"id": 9, "unit": 5, "title": "Thermal Fourier-number estimate", "input": {"name": "t", "label": "Cooling or heating time", "min": 1, "max": 240, "default": 40, "step": 1, "unit": "s"}, "expression": "1e-5*t/(0.01*0.01)", "result_unit": "dimensionless", "assumptions": "Thermal diffusivity 1e-5 m²/s, length 10 mm; conduction scale only, not a phase or quench predictor", "synthetic": true}, {"id": 10, "unit": 6, "title": "Specific stiffness comparison", "input": {"name": "rho", "label": "Density", "min": 2400, "max": 9000, "default": 2700, "step": 100, "unit": "kg/m³"}, "expression": "70/(rho/1000)", "result_unit": "GPa per (g/cm³)", "assumptions": "Young modulus fixed at 70 GPa, mass density varied synthetically; a screening index for selected geometries", "synthetic": true}, {"id": 11, "unit": 6, "title": "Copper conductor resistance", "input": {"name": "L", "label": "Copper conductor length", "min": 0.1, "max": 10, "default": 3, "step": 0.1, "unit": "m"}, "expression": "1.72e-8*L/1e-6", "result_unit": "ohm", "assumptions": "Electrical resistivity 1.72e-8 ohm m and fixed area 1 mm² at a single temperature; no contact resistance", "synthetic": true}, {"id": 12, "unit": 7, "title": "Crack-size limited nominal stress", "input": {"name": "a", "label": "Crack size", "min": 0.25, "max": 7, "default": 2, "step": 0.05, "unit": "mm"}, "expression": "40/(1.12*Math.sqrt(Math.PI*a/1000))", "result_unit": "MPa", "assumptions": "K=40 MPa sqrt(m), Y=1.12 fixed; elementary mode-I LEFM criterion only, no plane-strain or geometry validation", "synthetic": true}, {"id": 13, "unit": 7, "title": "Relative creep stress sensitivity", "input": {"name": "s", "label": "Applied stress", "min": 50, "max": 250, "default": 150, "step": 5, "unit": "MPa"}, "expression": "Math.pow(s/100,4)", "result_unit": "relative", "assumptions": "Norton stress exponent n=4 at one temperature, normalized rate=1 at 100 MPa; no time-to-failure implied", "synthetic": true}, {"id": 14, "unit": 8, "title": "Weld line energy", "input": {"name": "v", "label": "Welding travel speed", "min": 1, "max": 15, "default": 5, "step": 0.5, "unit": "mm/s"}, "expression": "0.8*20*150/v", "result_unit": "J/mm", "assumptions": "Illustrative arc 20 V ×150 A, efficiency eta=0.8, constant travel; actual weld pool geometry excluded", "synthetic": true}, {"id": 15, "unit": 8, "title": "Independent-counting fraction error", "input": {"name": "N", "label": "Number of sampled points", "min": 50, "max": 2000, "default": 500, "step": 25, "unit": "samples"}, "expression": "Math.sqrt(0.25*0.75/N)", "result_unit": "fraction", "assumptions": "True hypothetical phase area fraction 0.25, independent points; correlated microstructure produces larger effective uncertainty", "synthetic": true}];
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

