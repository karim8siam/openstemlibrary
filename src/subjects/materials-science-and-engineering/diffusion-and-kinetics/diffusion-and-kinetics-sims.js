/* Diffusion and Kinetics Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Steady Fickian molar flux magnitude",
    "input": {
      "name": "L",
      "label": "Diffusion path thickness",
      "min": 0.0002,
      "max": 0.005,
      "default": 0.001,
      "step": 0.0001,
      "unit": "m"
    },
    "expression": "1e-10*200/L",
    "result_unit": "mol/(m\u00b2 s)",
    "assumptions": "D=1\u00d710\u207b\u00b9\u2070 m\u00b2/s, \u0394c=200 mol/m\u00b3, fixed surface concentrations, planar steady state; returns positive flux magnitude",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "One-dimensional random-walk RMS displacement",
    "input": {
      "name": "t",
      "label": "Elapsed time",
      "min": 50,
      "max": 4000,
      "default": 900,
      "step": 50,
      "unit": "s"
    },
    "expression": "Math.sqrt(2*2e-11*t)*1e6",
    "result_unit": "\u03bcm",
    "assumptions": "1D unbiased uncorrelated random walk, D=2\u00d710\u207b\u00b9\u00b9 m\u00b2/s, no boundaries",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Diffusion length over fixed time",
    "input": {
      "name": "D",
      "label": "Diffusivity value",
      "min": 0.05,
      "max": 5,
      "default": 1,
      "step": 0.05,
      "unit": "\u00d710\u207b\u00b9\u00b9 m\u00b2/s"
    },
    "expression": "Math.sqrt(D*1e-11*3600)*1e6",
    "result_unit": "\u03bcm",
    "assumptions": "characteristic \u221a(Dt), t=3600 s, constant D; not a unique physical front location",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Explicit solver stability ratio",
    "input": {
      "name": "dt",
      "label": "Time step",
      "min": 0.1,
      "max": 16,
      "default": 4,
      "step": 0.1,
      "unit": "s"
    },
    "expression": "2e-12*dt/(5e-6*5e-6)",
    "result_unit": "dimensionless",
    "assumptions": "r=D\u0394t/\u0394x\u00b2, D=2\u00d710\u207b\u00b9\u00b2 m\u00b2/s, \u0394x=5 \u03bcm; explicit 1D constant-D scheme stable for r\u22640.5",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Activated bulk diffusivity",
    "input": {
      "name": "T",
      "label": "Temperature",
      "min": 650,
      "max": 1350,
      "default": 950,
      "step": 10,
      "unit": "K"
    },
    "expression": "2e-5*Math.exp(-150000/(8.31446261815324*T))",
    "result_unit": "m\u00b2/s",
    "assumptions": "D0=2\u00d710\u207b\u2075 m\u00b2/s, Q=150 kJ/mol, one transport mechanism, T in kelvin",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Ratio of diffusivities at two temperatures",
    "input": {
      "name": "T",
      "label": "Second temperature",
      "min": 700,
      "max": 1300,
      "default": 1100,
      "step": 10,
      "unit": "K"
    },
    "expression": "Math.exp((90000/8.31446261815324)*(1/900-1/T))",
    "result_unit": "D(T)/D(900 K)",
    "assumptions": "D0 cancels; Q=90 kJ/mol, reference T=900 K, one Arrhenius regime",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Parallel-path effective diffusion estimate",
    "input": {
      "name": "f",
      "label": "Connected fast-path area fraction",
      "min": 0,
      "max": 0.2,
      "default": 0.05,
      "step": 0.005,
      "unit": "fraction"
    },
    "expression": "(1-f)*1e-15+f*1e-11",
    "result_unit": "m\u00b2/s",
    "assumptions": "parallel conducting paths only, Dbulk=10\u207b\u00b9\u2075 and Dfast=10\u207b\u00b9\u00b9 m\u00b2/s; ignores tortuosity and segregation",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Electric-field ionic drift speed magnitude",
    "input": {
      "name": "E",
      "label": "Electric field magnitude",
      "min": 100,
      "max": 10000,
      "default": 2500,
      "step": 100,
      "unit": "V/m"
    },
    "expression": "2e-12*96485.33212*E/(8.31446261815324*700)*1e9",
    "result_unit": "nm/s",
    "assumptions": "Nernst\u2013Einstein mobility, monovalent species, D=2\u00d710\u207b\u00b9\u00b2 m\u00b2/s, T=700 K; field kept constant",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Illustrative carburization half-rise depth",
    "input": {
      "name": "t",
      "label": "Holding time",
      "min": 120,
      "max": 36000,
      "default": 7200,
      "step": 120,
      "unit": "s"
    },
    "expression": "2*0.4769362762*Math.sqrt(3e-11*t)*1e3",
    "result_unit": "mm",
    "assumptions": "erfc(z)=0.5 at z\u22480.476936; D=3\u00d710\u207b\u00b9\u00b9 m\u00b2/s, fixed surface concentration, semi-infinite",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Parabolic reaction-layer thickness",
    "input": {
      "name": "t",
      "label": "Oxidation duration",
      "min": 60,
      "max": 36000,
      "default": 7200,
      "step": 60,
      "unit": "s"
    },
    "expression": "Math.sqrt(3e-16*t)*1e6",
    "result_unit": "\u03bcm",
    "assumptions": "x\u00b2=kp t with kp=3\u00d710\u207b\u00b9\u2076 m\u00b2/s; ideal planar diffusion-limited layer, no spallation",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "First-order conversion",
    "input": {
      "name": "t",
      "label": "Reaction time",
      "min": 0,
      "max": 2400,
      "default": 600,
      "step": 20,
      "unit": "s"
    },
    "expression": "1-Math.exp(-0.0015*t)",
    "result_unit": "fraction",
    "assumptions": "X=1\u2212exp(\u2212kt), constant k=0.0015 s\u207b\u00b9, single lumped first-order reaction",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Avrami-type transformed fraction",
    "input": {
      "name": "t",
      "label": "Isothermal hold duration",
      "min": 0,
      "max": 3600,
      "default": 1200,
      "step": 30,
      "unit": "s"
    },
    "expression": "1-Math.exp(-Math.pow(0.0007*t,2.2))",
    "result_unit": "fraction",
    "assumptions": "X=1\u2212exp[\u2212(kt)^n], k=7\u00d710\u207b\u2074 s\u207b\u00b9, n=2.2, empirical; no incubation delay",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Ostwald coarsening radius",
    "input": {
      "name": "t",
      "label": "Aging duration",
      "min": 0,
      "max": 30000,
      "default": 8000,
      "step": 250,
      "unit": "s"
    },
    "expression": "Math.cbrt(Math.pow(15,3)+0.15*t)",
    "result_unit": "nm",
    "assumptions": "R\u00b3=R0\u00b3+Kt, R0=15 nm, K=0.15 nm\u00b3/s; dilute diffusion-controlled spherical approximation",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Idealized grain-growth size",
    "input": {
      "name": "t",
      "label": "Annealing duration",
      "min": 0,
      "max": 30000,
      "default": 8000,
      "step": 250,
      "unit": "s"
    },
    "expression": "Math.sqrt(Math.pow(8,2)+0.02*t)",
    "result_unit": "\u03bcm",
    "assumptions": "G\u00b2=G0\u00b2+Kt, G0=8 \u03bcm and K=0.02 \u03bcm\u00b2/s, isotropic unpinned grains",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Temperature-dependent process time",
    "input": {
      "name": "T",
      "label": "Holding temperature",
      "min": 650,
      "max": 1250,
      "default": 950,
      "step": 10,
      "unit": "K"
    },
    "expression": "3600*Math.exp((115000/8.31446261815324)*(1/T-1/950))",
    "result_unit": "s",
    "assumptions": "same D\u00d7t target across temperatures, Q=115 kJ/mol, reference hold=3600 s at 950 K",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Relative thermal penetration budget",
    "input": {
      "name": "t",
      "label": "Hold time",
      "min": 60,
      "max": 25000,
      "default": 4000,
      "step": 60,
      "unit": "s"
    },
    "expression": "Math.sqrt(1.5e-11*t)*1e6",
    "result_unit": "\u03bcm",
    "assumptions": "single spatial dimension, uniform D=1.5\u00d710\u207b\u00b9\u00b9 m\u00b2/s; neglects ramp, phase changes, surfaces",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Steady Fickian molar flux magnitude", "input": {"name": "L", "label": "Diffusion path thickness", "min": 0.0002, "max": 0.005, "default": 0.001, "step": 0.0001, "unit": "m"}, "expression": "1e-10*200/L", "result_unit": "mol/(m² s)", "assumptions": "D=1×10⁻¹⁰ m²/s, Δc=200 mol/m³, fixed surface concentrations, planar steady state; returns positive flux magnitude", "synthetic": true}, {"id": 1, "unit": 1, "title": "One-dimensional random-walk RMS displacement", "input": {"name": "t", "label": "Elapsed time", "min": 50, "max": 4000, "default": 900, "step": 50, "unit": "s"}, "expression": "Math.sqrt(2*2e-11*t)*1e6", "result_unit": "μm", "assumptions": "1D unbiased uncorrelated random walk, D=2×10⁻¹¹ m²/s, no boundaries", "synthetic": true}, {"id": 2, "unit": 2, "title": "Diffusion length over fixed time", "input": {"name": "D", "label": "Diffusivity value", "min": 0.05, "max": 5, "default": 1, "step": 0.05, "unit": "×10⁻¹¹ m²/s"}, "expression": "Math.sqrt(D*1e-11*3600)*1e6", "result_unit": "μm", "assumptions": "characteristic √(Dt), t=3600 s, constant D; not a unique physical front location", "synthetic": true}, {"id": 3, "unit": 2, "title": "Explicit solver stability ratio", "input": {"name": "dt", "label": "Time step", "min": 0.1, "max": 16, "default": 4, "step": 0.1, "unit": "s"}, "expression": "2e-12*dt/(5e-6*5e-6)", "result_unit": "dimensionless", "assumptions": "r=DΔt/Δx², D=2×10⁻¹² m²/s, Δx=5 μm; explicit 1D constant-D scheme stable for r≤0.5", "synthetic": true}, {"id": 4, "unit": 3, "title": "Activated bulk diffusivity", "input": {"name": "T", "label": "Temperature", "min": 650, "max": 1350, "default": 950, "step": 10, "unit": "K"}, "expression": "2e-5*Math.exp(-150000/(8.31446261815324*T))", "result_unit": "m²/s", "assumptions": "D0=2×10⁻⁵ m²/s, Q=150 kJ/mol, one transport mechanism, T in kelvin", "synthetic": true}, {"id": 5, "unit": 3, "title": "Ratio of diffusivities at two temperatures", "input": {"name": "T", "label": "Second temperature", "min": 700, "max": 1300, "default": 1100, "step": 10, "unit": "K"}, "expression": "Math.exp((90000/8.31446261815324)*(1/900-1/T))", "result_unit": "D(T)/D(900 K)", "assumptions": "D0 cancels; Q=90 kJ/mol, reference T=900 K, one Arrhenius regime", "synthetic": true}, {"id": 6, "unit": 4, "title": "Parallel-path effective diffusion estimate", "input": {"name": "f", "label": "Connected fast-path area fraction", "min": 0, "max": 0.2, "default": 0.05, "step": 0.005, "unit": "fraction"}, "expression": "(1-f)*1e-15+f*1e-11", "result_unit": "m²/s", "assumptions": "parallel conducting paths only, Dbulk=10⁻¹⁵ and Dfast=10⁻¹¹ m²/s; ignores tortuosity and segregation", "synthetic": true}, {"id": 7, "unit": 4, "title": "Electric-field ionic drift speed magnitude", "input": {"name": "E", "label": "Electric field magnitude", "min": 100, "max": 10000, "default": 2500, "step": 100, "unit": "V/m"}, "expression": "2e-12*96485.33212*E/(8.31446261815324*700)*1e9", "result_unit": "nm/s", "assumptions": "Nernst–Einstein mobility, monovalent species, D=2×10⁻¹² m²/s, T=700 K; field kept constant", "synthetic": true}, {"id": 8, "unit": 5, "title": "Illustrative carburization half-rise depth", "input": {"name": "t", "label": "Holding time", "min": 120, "max": 36000, "default": 7200, "step": 120, "unit": "s"}, "expression": "2*0.4769362762*Math.sqrt(3e-11*t)*1e3", "result_unit": "mm", "assumptions": "erfc(z)=0.5 at z≈0.476936; D=3×10⁻¹¹ m²/s, fixed surface concentration, semi-infinite", "synthetic": true}, {"id": 9, "unit": 5, "title": "Parabolic reaction-layer thickness", "input": {"name": "t", "label": "Oxidation duration", "min": 60, "max": 36000, "default": 7200, "step": 60, "unit": "s"}, "expression": "Math.sqrt(3e-16*t)*1e6", "result_unit": "μm", "assumptions": "x²=kp t with kp=3×10⁻¹⁶ m²/s; ideal planar diffusion-limited layer, no spallation", "synthetic": true}, {"id": 10, "unit": 6, "title": "First-order conversion", "input": {"name": "t", "label": "Reaction time", "min": 0, "max": 2400, "default": 600, "step": 20, "unit": "s"}, "expression": "1-Math.exp(-0.0015*t)", "result_unit": "fraction", "assumptions": "X=1−exp(−kt), constant k=0.0015 s⁻¹, single lumped first-order reaction", "synthetic": true}, {"id": 11, "unit": 6, "title": "Avrami-type transformed fraction", "input": {"name": "t", "label": "Isothermal hold duration", "min": 0, "max": 3600, "default": 1200, "step": 30, "unit": "s"}, "expression": "1-Math.exp(-Math.pow(0.0007*t,2.2))", "result_unit": "fraction", "assumptions": "X=1−exp[−(kt)^n], k=7×10⁻⁴ s⁻¹, n=2.2, empirical; no incubation delay", "synthetic": true}, {"id": 12, "unit": 7, "title": "Ostwald coarsening radius", "input": {"name": "t", "label": "Aging duration", "min": 0, "max": 30000, "default": 8000, "step": 250, "unit": "s"}, "expression": "Math.cbrt(Math.pow(15,3)+0.15*t)", "result_unit": "nm", "assumptions": "R³=R0³+Kt, R0=15 nm, K=0.15 nm³/s; dilute diffusion-controlled spherical approximation", "synthetic": true}, {"id": 13, "unit": 7, "title": "Idealized grain-growth size", "input": {"name": "t", "label": "Annealing duration", "min": 0, "max": 30000, "default": 8000, "step": 250, "unit": "s"}, "expression": "Math.sqrt(Math.pow(8,2)+0.02*t)", "result_unit": "μm", "assumptions": "G²=G0²+Kt, G0=8 μm and K=0.02 μm²/s, isotropic unpinned grains", "synthetic": true}, {"id": 14, "unit": 8, "title": "Temperature-dependent process time", "input": {"name": "T", "label": "Holding temperature", "min": 650, "max": 1250, "default": 950, "step": 10, "unit": "K"}, "expression": "3600*Math.exp((115000/8.31446261815324)*(1/T-1/950))", "result_unit": "s", "assumptions": "same D×t target across temperatures, Q=115 kJ/mol, reference hold=3600 s at 950 K", "synthetic": true}, {"id": 15, "unit": 8, "title": "Relative thermal penetration budget", "input": {"name": "t", "label": "Hold time", "min": 60, "max": 25000, "default": 4000, "step": 60, "unit": "s"}, "expression": "Math.sqrt(1.5e-11*t)*1e6", "result_unit": "μm", "assumptions": "single spatial dimension, uniform D=1.5×10⁻¹¹ m²/s; neglects ramp, phase changes, surfaces", "synthetic": true}];
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

