/* Mechanical Behavior of Solids Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Nominal tensile stress",
    "input": {
      "name": "F",
      "label": "Applied force",
      "min": 1,
      "max": 45,
      "default": 12,
      "step": 0.5,
      "unit": "kN"
    },
    "expression": "F*1000/120",
    "result_unit": "MPa",
    "assumptions": "Initial section A0=120 mm\u00b2; engineering stress for centered uniaxial loading, no local concentration",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Elastic extension of a bar",
    "input": {
      "name": "L",
      "label": "Original bar length",
      "min": 50,
      "max": 500,
      "default": 200,
      "step": 10,
      "unit": "mm"
    },
    "expression": "8000*L/(200000*100)",
    "result_unit": "mm",
    "assumptions": "F=8000 N, E=200000 MPa, A=100 mm\u00b2, uniform small-strain linear elasticity",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Offset yield-section load",
    "input": {
      "name": "A",
      "label": "Original section area",
      "min": 20,
      "max": 250,
      "default": 80,
      "step": 5,
      "unit": "mm\u00b2"
    },
    "expression": "250*A/1000",
    "result_unit": "kN",
    "assumptions": "Illustrative proof stress=250 MPa, uniaxial average stress, no stability or defect allowance",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Nonlinear Ramberg\u2013Osgood strain",
    "input": {
      "name": "S",
      "label": "Applied nominal stress",
      "min": 20,
      "max": 500,
      "default": 240,
      "step": 5,
      "unit": "MPa"
    },
    "expression": "S/210000+Math.pow(S/1100,6)",
    "result_unit": "strain",
    "assumptions": "Simplified epsilon=sigma/E+(sigma/K)^n with E=210000 MPa, K=1100 MPa, n=6; fitted only within fictional regime",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Resolved shear stress",
    "input": {
      "name": "p",
      "label": "Angle to slip-plane normal",
      "min": 5,
      "max": 85,
      "default": 45,
      "step": 1,
      "unit": "degrees"
    },
    "expression": "300*Math.cos(p*Math.PI/180)*Math.cos(Math.PI/4)",
    "result_unit": "MPa",
    "assumptions": "Uniaxial stress=300 MPa, slip direction angle lambda=45 degrees; Schmid-law geometry only",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Hall\u2013Petch proof stress",
    "input": {
      "name": "d",
      "label": "Mean grain diameter",
      "min": 2,
      "max": 120,
      "default": 30,
      "step": 2,
      "unit": "\u03bcm"
    },
    "expression": "100+0.65/Math.sqrt(d*1e-6)",
    "result_unit": "MPa",
    "assumptions": "sigma0=100 MPa and k=0.65 MPa sqrt(m), illustrative limited-range grain strengthening",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Maximum elastic beam stress",
    "input": {
      "name": "M",
      "label": "Applied bending moment",
      "min": 5,
      "max": 200,
      "default": 65,
      "step": 5,
      "unit": "N\u00b7m"
    },
    "expression": "M*1000*10/50000",
    "result_unit": "MPa",
    "assumptions": "Elastic beam, c=10 mm, I=50000 mm\u2074, pure bending, no shear or local instability",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Euler elastic column load",
    "input": {
      "name": "L",
      "label": "Effective pinned column length",
      "min": 0.4,
      "max": 2.4,
      "default": 1.2,
      "step": 0.05,
      "unit": "m"
    },
    "expression": "Math.PI*Math.PI*200e9*2e-8/(L*L)/1000",
    "result_unit": "kN",
    "assumptions": "E=200 GPa, I=2\u00d710\u207b\u2078 m\u2074, K=1, ideal slender pinned column, no imperfection",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Mode I stress-intensity estimate",
    "input": {
      "name": "a",
      "label": "Crack depth",
      "min": 0.2,
      "max": 5,
      "default": 2,
      "step": 0.1,
      "unit": "mm"
    },
    "expression": "1.12*100*Math.sqrt(Math.PI*a/1000)",
    "result_unit": "MPa\u221am",
    "assumptions": "Y=1.12 fixed illustrative geometry, remote tensile stress=100 MPa, LEFM assumptions",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Elastic energy release rate",
    "input": {
      "name": "K",
      "label": "Mode I stress intensity",
      "min": 1,
      "max": 35,
      "default": 12,
      "step": 1,
      "unit": "MPa\u221am"
    },
    "expression": "K*K/220000*1e6",
    "result_unit": "J/m\u00b2",
    "assumptions": "Plane-strain E-prime=220000 MPa; G=K\u00b2/E-prime, ideal isotropic linear elastic fracture",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Paris crack-growth rate",
    "input": {
      "name": "K",
      "label": "Stress intensity range",
      "min": 2,
      "max": 40,
      "default": 16,
      "step": 1,
      "unit": "MPa\u221am"
    },
    "expression": "1e-11*Math.pow(K,3)*1e9",
    "result_unit": "nm/cycle",
    "assumptions": "Synthetic C=10\u207b\u00b9\u00b9 m/cycle/(MPa\u221am)\u00b3 and m=3; intermediate Paris regime only",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Plastic strain-life amplitude",
    "input": {
      "name": "N",
      "label": "Cycles to failure",
      "min": 500,
      "max": 100000,
      "default": 12000,
      "step": 500,
      "unit": "cycles"
    },
    "expression": "100*0.35*Math.pow(2*N,-0.55)",
    "result_unit": "percent",
    "assumptions": "Coffin\u2013Manson plastic term with epsilon_f prime=0.35 and c=-0.55; not total strain-life law",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Norton activated creep rate",
    "input": {
      "name": "T",
      "label": "Absolute temperature",
      "min": 750,
      "max": 1250,
      "default": 1000,
      "step": 10,
      "unit": "K"
    },
    "expression": "100*Math.pow(40,4)*Math.exp(-280000/(8.31446261815324*T))",
    "result_unit": "s\u207b\u00b9",
    "assumptions": "Artificial A=100 s\u207b\u00b9 MPa\u207b\u2074, stress=40 MPa, n=4, Q=280 kJ/mol; not an engineering creep database",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Maxwell stress relaxation",
    "input": {
      "name": "t",
      "label": "Elapsed time",
      "min": 0,
      "max": 72,
      "default": 16,
      "step": 1,
      "unit": "h"
    },
    "expression": "50*Math.exp(-t/12)",
    "result_unit": "MPa",
    "assumptions": "Initial stress=50 MPa, tau=12 h, fixed small imposed strain, ideal Maxwell element",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Illustrative Vickers hardness",
    "input": {
      "name": "d",
      "label": "Average imprint diagonal",
      "min": 0.15,
      "max": 1.2,
      "default": 0.4,
      "step": 0.01,
      "unit": "mm"
    },
    "expression": "0.1891*9.81/(d*d)",
    "result_unit": "HV",
    "assumptions": "Load=9.81 N, ideal diamond indentation relation; hardness number only, no tensile strength conversion",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Weibull survival probability",
    "input": {
      "name": "S",
      "label": "Applied tensile stress",
      "min": 20,
      "max": 300,
      "default": 120,
      "step": 5,
      "unit": "MPa"
    },
    "expression": "Math.exp(-Math.pow(S/180,6))",
    "result_unit": "probability",
    "assumptions": "Hypothetical m=6, scale=180 MPa, fixed geometry and flaw population; not structural certification",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Nominal tensile stress", "input": {"name": "F", "label": "Applied force", "min": 1, "max": 45, "default": 12, "step": 0.5, "unit": "kN"}, "expression": "F*1000/120", "result_unit": "MPa", "assumptions": "Initial section A0=120 mm²; engineering stress for centered uniaxial loading, no local concentration", "synthetic": true}, {"id": 1, "unit": 1, "title": "Elastic extension of a bar", "input": {"name": "L", "label": "Original bar length", "min": 50, "max": 500, "default": 200, "step": 10, "unit": "mm"}, "expression": "8000*L/(200000*100)", "result_unit": "mm", "assumptions": "F=8000 N, E=200000 MPa, A=100 mm², uniform small-strain linear elasticity", "synthetic": true}, {"id": 2, "unit": 2, "title": "Offset yield-section load", "input": {"name": "A", "label": "Original section area", "min": 20, "max": 250, "default": 80, "step": 5, "unit": "mm²"}, "expression": "250*A/1000", "result_unit": "kN", "assumptions": "Illustrative proof stress=250 MPa, uniaxial average stress, no stability or defect allowance", "synthetic": true}, {"id": 3, "unit": 2, "title": "Nonlinear Ramberg–Osgood strain", "input": {"name": "S", "label": "Applied nominal stress", "min": 20, "max": 500, "default": 240, "step": 5, "unit": "MPa"}, "expression": "S/210000+Math.pow(S/1100,6)", "result_unit": "strain", "assumptions": "Simplified epsilon=sigma/E+(sigma/K)^n with E=210000 MPa, K=1100 MPa, n=6; fitted only within fictional regime", "synthetic": true}, {"id": 4, "unit": 3, "title": "Resolved shear stress", "input": {"name": "p", "label": "Angle to slip-plane normal", "min": 5, "max": 85, "default": 45, "step": 1, "unit": "degrees"}, "expression": "300*Math.cos(p*Math.PI/180)*Math.cos(Math.PI/4)", "result_unit": "MPa", "assumptions": "Uniaxial stress=300 MPa, slip direction angle lambda=45 degrees; Schmid-law geometry only", "synthetic": true}, {"id": 5, "unit": 3, "title": "Hall–Petch proof stress", "input": {"name": "d", "label": "Mean grain diameter", "min": 2, "max": 120, "default": 30, "step": 2, "unit": "μm"}, "expression": "100+0.65/Math.sqrt(d*1e-6)", "result_unit": "MPa", "assumptions": "sigma0=100 MPa and k=0.65 MPa sqrt(m), illustrative limited-range grain strengthening", "synthetic": true}, {"id": 6, "unit": 4, "title": "Maximum elastic beam stress", "input": {"name": "M", "label": "Applied bending moment", "min": 5, "max": 200, "default": 65, "step": 5, "unit": "N·m"}, "expression": "M*1000*10/50000", "result_unit": "MPa", "assumptions": "Elastic beam, c=10 mm, I=50000 mm⁴, pure bending, no shear or local instability", "synthetic": true}, {"id": 7, "unit": 4, "title": "Euler elastic column load", "input": {"name": "L", "label": "Effective pinned column length", "min": 0.4, "max": 2.4, "default": 1.2, "step": 0.05, "unit": "m"}, "expression": "Math.PI*Math.PI*200e9*2e-8/(L*L)/1000", "result_unit": "kN", "assumptions": "E=200 GPa, I=2×10⁻⁸ m⁴, K=1, ideal slender pinned column, no imperfection", "synthetic": true}, {"id": 8, "unit": 5, "title": "Mode I stress-intensity estimate", "input": {"name": "a", "label": "Crack depth", "min": 0.2, "max": 5, "default": 2, "step": 0.1, "unit": "mm"}, "expression": "1.12*100*Math.sqrt(Math.PI*a/1000)", "result_unit": "MPa√m", "assumptions": "Y=1.12 fixed illustrative geometry, remote tensile stress=100 MPa, LEFM assumptions", "synthetic": true}, {"id": 9, "unit": 5, "title": "Elastic energy release rate", "input": {"name": "K", "label": "Mode I stress intensity", "min": 1, "max": 35, "default": 12, "step": 1, "unit": "MPa√m"}, "expression": "K*K/220000*1e6", "result_unit": "J/m²", "assumptions": "Plane-strain E-prime=220000 MPa; G=K²/E-prime, ideal isotropic linear elastic fracture", "synthetic": true}, {"id": 10, "unit": 6, "title": "Paris crack-growth rate", "input": {"name": "K", "label": "Stress intensity range", "min": 2, "max": 40, "default": 16, "step": 1, "unit": "MPa√m"}, "expression": "1e-11*Math.pow(K,3)*1e9", "result_unit": "nm/cycle", "assumptions": "Synthetic C=10⁻¹¹ m/cycle/(MPa√m)³ and m=3; intermediate Paris regime only", "synthetic": true}, {"id": 11, "unit": 6, "title": "Plastic strain-life amplitude", "input": {"name": "N", "label": "Cycles to failure", "min": 500, "max": 100000, "default": 12000, "step": 500, "unit": "cycles"}, "expression": "100*0.35*Math.pow(2*N,-0.55)", "result_unit": "percent", "assumptions": "Coffin–Manson plastic term with epsilon_f prime=0.35 and c=-0.55; not total strain-life law", "synthetic": true}, {"id": 12, "unit": 7, "title": "Norton activated creep rate", "input": {"name": "T", "label": "Absolute temperature", "min": 750, "max": 1250, "default": 1000, "step": 10, "unit": "K"}, "expression": "100*Math.pow(40,4)*Math.exp(-280000/(8.31446261815324*T))", "result_unit": "s⁻¹", "assumptions": "Artificial A=100 s⁻¹ MPa⁻⁴, stress=40 MPa, n=4, Q=280 kJ/mol; not an engineering creep database", "synthetic": true}, {"id": 13, "unit": 7, "title": "Maxwell stress relaxation", "input": {"name": "t", "label": "Elapsed time", "min": 0, "max": 72, "default": 16, "step": 1, "unit": "h"}, "expression": "50*Math.exp(-t/12)", "result_unit": "MPa", "assumptions": "Initial stress=50 MPa, tau=12 h, fixed small imposed strain, ideal Maxwell element", "synthetic": true}, {"id": 14, "unit": 8, "title": "Illustrative Vickers hardness", "input": {"name": "d", "label": "Average imprint diagonal", "min": 0.15, "max": 1.2, "default": 0.4, "step": 0.01, "unit": "mm"}, "expression": "0.1891*9.81/(d*d)", "result_unit": "HV", "assumptions": "Load=9.81 N, ideal diamond indentation relation; hardness number only, no tensile strength conversion", "synthetic": true}, {"id": 15, "unit": 8, "title": "Weibull survival probability", "input": {"name": "S", "label": "Applied tensile stress", "min": 20, "max": 300, "default": 120, "step": 5, "unit": "MPa"}, "expression": "Math.exp(-Math.pow(S/180,6))", "result_unit": "probability", "assumptions": "Hypothetical m=6, scale=180 MPa, fixed geometry and flaw population; not structural certification", "synthetic": true}];
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

