/* Ceramic Materials Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Ideal crystal density",
    "input": {
      "name": "a",
      "label": "Cubic unit-cell edge",
      "min": 0.38,
      "max": 0.62,
      "default": 0.48,
      "step": 0.005,
      "unit": "nm"
    },
    "expression": "2*0.10196/(6.02214076e23*Math.pow(a*1e-9,3))",
    "result_unit": "kg/m\u00b3",
    "assumptions": "Hypothetical cubic solid: Z=2 formula units, formula mass M=0.10196 kg/mol, ideal dense phase, no variation of composition or temperature",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Ideal dilute defect fraction",
    "input": {
      "name": "T",
      "label": "Absolute temperature",
      "min": 900,
      "max": 1800,
      "default": 1200,
      "step": 10,
      "unit": "K"
    },
    "expression": "Math.exp(-1.2/(8.617333262e-5*T))",
    "result_unit": "site fraction",
    "assumptions": "Single hypothetical noninteracting defect species with E_f=1.2 eV; formation entropy and oxygen chemical potential neglected",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Spherical powder surface area",
    "input": {
      "name": "d",
      "label": "Ideal particle diameter",
      "min": 1,
      "max": 40,
      "default": 8,
      "step": 0.5,
      "unit": "\u00b5m"
    },
    "expression": "6/(3300*d*1e-6)",
    "result_unit": "m\u00b2/kg",
    "assumptions": "Smooth monodisperse nonporous spherical particles, particle density 3300 kg/m\u00b3; real BET area differs",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Green porosity fraction",
    "input": {
      "name": "rho",
      "label": "Dry bulk green density",
      "min": 1400,
      "max": 3000,
      "default": 2100,
      "step": 25,
      "unit": "kg/m\u00b3"
    },
    "expression": "1-rho/3200",
    "result_unit": "fraction",
    "assumptions": "Hypothetical skeletal density 3200 kg/m\u00b3; binder volume and residual solvent excluded; uniform density",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Illustrative viscous neck ratio",
    "input": {
      "name": "t",
      "label": "Isothermal hold duration",
      "min": 0,
      "max": 1500,
      "default": 500,
      "step": 25,
      "unit": "s"
    },
    "expression": "Math.sqrt(3*t/(2*1e10*1e-6))",
    "result_unit": "neck/radius",
    "assumptions": "Two equal spheres r=1 \u00b5m, viscosity 1e10 Pa\u00b7s, surface energy 1 J/m\u00b2; early-stage toy viscous-flow only, not crystalline solid-state sintering",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Ideal isotropic linear shrinkage",
    "input": {
      "name": "rhof",
      "label": "Final relative density",
      "min": 0.75,
      "max": 0.99,
      "default": 0.92,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "100*(1-Math.pow(0.55/rhof,1/3))",
    "result_unit": "% length decrease",
    "assumptions": "Start relative density=0.55, conserved mass, unchanged reference solid density, spatially uniform isotropic shrinkage",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Ideal plate capacitance",
    "input": {
      "name": "d",
      "label": "Dielectric thickness",
      "min": 0.1,
      "max": 2.0,
      "default": 0.75,
      "step": 0.05,
      "unit": "mm"
    },
    "expression": "8.8541878128e-12*1000*1e-4/(d*1e-3)*1e12",
    "result_unit": "pF",
    "assumptions": "A=1 cm\u00b2, epsilon_r=1000, linear ideal parallel plate, zero fringe loss and no frequency or field dependence",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Arrhenius ionic transport ratio",
    "input": {
      "name": "T",
      "label": "Operating temperature",
      "min": 800,
      "max": 1300,
      "default": 1000,
      "step": 10,
      "unit": "K"
    },
    "expression": "Math.exp(-0.85/8.617333262e-5*(1/T-1/1000))",
    "result_unit": "relative to 1000 K",
    "assumptions": "Illustrative activation energy=0.85 eV, fixed prefactor and reference T=1000 K; no carrier association or leakage",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Ideal slab thermal resistance",
    "input": {
      "name": "k",
      "label": "Thermal conductivity",
      "min": 0.5,
      "max": 20,
      "default": 4,
      "step": 0.5,
      "unit": "W/(m K)"
    },
    "expression": "0.01/(k*0.005)",
    "result_unit": "K/W",
    "assumptions": "Single layer thickness=10 mm and area=0.005 m\u00b2, 1D steady conduction with k constant, no contacts or radiation",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Fully constrained thermal stress",
    "input": {
      "name": "dT",
      "label": "Absolute temperature difference",
      "min": 20,
      "max": 400,
      "default": 120,
      "step": 10,
      "unit": "K"
    },
    "expression": "250e9*7e-6*dT/(1-0.25)/1e6",
    "result_unit": "MPa",
    "assumptions": "Uniform equibiaxial elastic constraint; E=250 GPa, alpha=7e-6 /K, nu=0.25; stress magnitude only; ignores temperature fields and fracture",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Ideal mode-I crack-limited stress",
    "input": {
      "name": "a",
      "label": "Representative crack depth",
      "min": 10,
      "max": 800,
      "default": 120,
      "step": 10,
      "unit": "\u00b5m"
    },
    "expression": "3/(1.12*Math.sqrt(Math.PI*a*1e-6))",
    "result_unit": "MPa",
    "assumptions": "Fixed K_IC=3 MPa sqrt(m) and geometry factor Y=1.12, LEFM applicable; not a calibrated ceramic or certified crack geometry",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Illustrative Weibull failure probability",
    "input": {
      "name": "s",
      "label": "Nominal applied tensile stress",
      "min": 50,
      "max": 500,
      "default": 250,
      "step": 10,
      "unit": "MPa"
    },
    "expression": "1-Math.exp(-Math.pow(s/300,8))",
    "result_unit": "probability",
    "assumptions": "Two-parameter Weibull with characteristic strength 300 MPa and m=8 for fixed stressed-volume and environment; synthetic fit",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Illustrative glass log-viscosity",
    "input": {
      "name": "T",
      "label": "Absolute forming temperature",
      "min": 700,
      "max": 1200,
      "default": 900,
      "step": 10,
      "unit": "K"
    },
    "expression": "-3+4000/(T-400)",
    "result_unit": "log10(Pa\u00b7s)",
    "assumptions": "Synthetic VFT-like equation A=-3, B=4000 K, T0=400 K, 700<=T<=1200 K; not calibrated to any glass",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Glass absorption-only transmission",
    "input": {
      "name": "L",
      "label": "Optical path length",
      "min": 1,
      "max": 20,
      "default": 8,
      "step": 1,
      "unit": "mm"
    },
    "expression": "100*Math.exp(-5*L/1000)",
    "result_unit": "% transmitted",
    "assumptions": "Monochromatic uniform absorption coefficient=5 m^-1; no scattering, interfacial reflection, interference or wavelength dependence",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Synthetic fractional release",
    "input": {
      "name": "t",
      "label": "Elapsed time",
      "min": 1,
      "max": 60,
      "default": 14,
      "step": 1,
      "unit": "day"
    },
    "expression": "100*(1-Math.exp(-0.035*t))",
    "result_unit": "% released",
    "assumptions": "One-compartment constant-rate coefficient 0.035 per day; educational curve only, not a physiological bioactivity or clinical kinetics claim",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Electricity-only manufacturing CO2 proxy",
    "input": {
      "name": "E",
      "label": "Furnace electricity per product mass",
      "min": 0.2,
      "max": 10,
      "default": 3,
      "step": 0.2,
      "unit": "kWh/kg"
    },
    "expression": "0.45*E",
    "result_unit": "kg CO2e/kg",
    "assumptions": "Assumed grid factor=0.45 kg CO2e/kWh; excludes embodied raw materials, upstream energy, rejected yield, transport, life cycle and date-specific grid data",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Ideal crystal density", "input": {"name": "a", "label": "Cubic unit-cell edge", "min": 0.38, "max": 0.62, "default": 0.48, "step": 0.005, "unit": "nm"}, "expression": "2*0.10196/(6.02214076e23*Math.pow(a*1e-9,3))", "result_unit": "kg/m³", "assumptions": "Hypothetical cubic solid: Z=2 formula units, formula mass M=0.10196 kg/mol, ideal dense phase, no variation of composition or temperature", "synthetic": true}, {"id": 1, "unit": 1, "title": "Ideal dilute defect fraction", "input": {"name": "T", "label": "Absolute temperature", "min": 900, "max": 1800, "default": 1200, "step": 10, "unit": "K"}, "expression": "Math.exp(-1.2/(8.617333262e-5*T))", "result_unit": "site fraction", "assumptions": "Single hypothetical noninteracting defect species with E_f=1.2 eV; formation entropy and oxygen chemical potential neglected", "synthetic": true}, {"id": 2, "unit": 2, "title": "Spherical powder surface area", "input": {"name": "d", "label": "Ideal particle diameter", "min": 1, "max": 40, "default": 8, "step": 0.5, "unit": "µm"}, "expression": "6/(3300*d*1e-6)", "result_unit": "m²/kg", "assumptions": "Smooth monodisperse nonporous spherical particles, particle density 3300 kg/m³; real BET area differs", "synthetic": true}, {"id": 3, "unit": 2, "title": "Green porosity fraction", "input": {"name": "rho", "label": "Dry bulk green density", "min": 1400, "max": 3000, "default": 2100, "step": 25, "unit": "kg/m³"}, "expression": "1-rho/3200", "result_unit": "fraction", "assumptions": "Hypothetical skeletal density 3200 kg/m³; binder volume and residual solvent excluded; uniform density", "synthetic": true}, {"id": 4, "unit": 3, "title": "Illustrative viscous neck ratio", "input": {"name": "t", "label": "Isothermal hold duration", "min": 0, "max": 1500, "default": 500, "step": 25, "unit": "s"}, "expression": "Math.sqrt(3*t/(2*1e10*1e-6))", "result_unit": "neck/radius", "assumptions": "Two equal spheres r=1 µm, viscosity 1e10 Pa·s, surface energy 1 J/m²; early-stage toy viscous-flow only, not crystalline solid-state sintering", "synthetic": true}, {"id": 5, "unit": 3, "title": "Ideal isotropic linear shrinkage", "input": {"name": "rhof", "label": "Final relative density", "min": 0.75, "max": 0.99, "default": 0.92, "step": 0.01, "unit": "fraction"}, "expression": "100*(1-Math.pow(0.55/rhof,1/3))", "result_unit": "% length decrease", "assumptions": "Start relative density=0.55, conserved mass, unchanged reference solid density, spatially uniform isotropic shrinkage", "synthetic": true}, {"id": 6, "unit": 4, "title": "Ideal plate capacitance", "input": {"name": "d", "label": "Dielectric thickness", "min": 0.1, "max": 2.0, "default": 0.75, "step": 0.05, "unit": "mm"}, "expression": "8.8541878128e-12*1000*1e-4/(d*1e-3)*1e12", "result_unit": "pF", "assumptions": "A=1 cm², epsilon_r=1000, linear ideal parallel plate, zero fringe loss and no frequency or field dependence", "synthetic": true}, {"id": 7, "unit": 4, "title": "Arrhenius ionic transport ratio", "input": {"name": "T", "label": "Operating temperature", "min": 800, "max": 1300, "default": 1000, "step": 10, "unit": "K"}, "expression": "Math.exp(-0.85/8.617333262e-5*(1/T-1/1000))", "result_unit": "relative to 1000 K", "assumptions": "Illustrative activation energy=0.85 eV, fixed prefactor and reference T=1000 K; no carrier association or leakage", "synthetic": true}, {"id": 8, "unit": 5, "title": "Ideal slab thermal resistance", "input": {"name": "k", "label": "Thermal conductivity", "min": 0.5, "max": 20, "default": 4, "step": 0.5, "unit": "W/(m K)"}, "expression": "0.01/(k*0.005)", "result_unit": "K/W", "assumptions": "Single layer thickness=10 mm and area=0.005 m², 1D steady conduction with k constant, no contacts or radiation", "synthetic": true}, {"id": 9, "unit": 5, "title": "Fully constrained thermal stress", "input": {"name": "dT", "label": "Absolute temperature difference", "min": 20, "max": 400, "default": 120, "step": 10, "unit": "K"}, "expression": "250e9*7e-6*dT/(1-0.25)/1e6", "result_unit": "MPa", "assumptions": "Uniform equibiaxial elastic constraint; E=250 GPa, alpha=7e-6 /K, nu=0.25; stress magnitude only; ignores temperature fields and fracture", "synthetic": true}, {"id": 10, "unit": 6, "title": "Ideal mode-I crack-limited stress", "input": {"name": "a", "label": "Representative crack depth", "min": 10, "max": 800, "default": 120, "step": 10, "unit": "µm"}, "expression": "3/(1.12*Math.sqrt(Math.PI*a*1e-6))", "result_unit": "MPa", "assumptions": "Fixed K_IC=3 MPa sqrt(m) and geometry factor Y=1.12, LEFM applicable; not a calibrated ceramic or certified crack geometry", "synthetic": true}, {"id": 11, "unit": 6, "title": "Illustrative Weibull failure probability", "input": {"name": "s", "label": "Nominal applied tensile stress", "min": 50, "max": 500, "default": 250, "step": 10, "unit": "MPa"}, "expression": "1-Math.exp(-Math.pow(s/300,8))", "result_unit": "probability", "assumptions": "Two-parameter Weibull with characteristic strength 300 MPa and m=8 for fixed stressed-volume and environment; synthetic fit", "synthetic": true}, {"id": 12, "unit": 7, "title": "Illustrative glass log-viscosity", "input": {"name": "T", "label": "Absolute forming temperature", "min": 700, "max": 1200, "default": 900, "step": 10, "unit": "K"}, "expression": "-3+4000/(T-400)", "result_unit": "log10(Pa·s)", "assumptions": "Synthetic VFT-like equation A=-3, B=4000 K, T0=400 K, 700<=T<=1200 K; not calibrated to any glass", "synthetic": true}, {"id": 13, "unit": 7, "title": "Glass absorption-only transmission", "input": {"name": "L", "label": "Optical path length", "min": 1, "max": 20, "default": 8, "step": 1, "unit": "mm"}, "expression": "100*Math.exp(-5*L/1000)", "result_unit": "% transmitted", "assumptions": "Monochromatic uniform absorption coefficient=5 m^-1; no scattering, interfacial reflection, interference or wavelength dependence", "synthetic": true}, {"id": 14, "unit": 8, "title": "Synthetic fractional release", "input": {"name": "t", "label": "Elapsed time", "min": 1, "max": 60, "default": 14, "step": 1, "unit": "day"}, "expression": "100*(1-Math.exp(-0.035*t))", "result_unit": "% released", "assumptions": "One-compartment constant-rate coefficient 0.035 per day; educational curve only, not a physiological bioactivity or clinical kinetics claim", "synthetic": true}, {"id": 15, "unit": 8, "title": "Electricity-only manufacturing CO2 proxy", "input": {"name": "E", "label": "Furnace electricity per product mass", "min": 0.2, "max": 10, "default": 3, "step": 0.2, "unit": "kWh/kg"}, "expression": "0.45*E", "result_unit": "kg CO2e/kg", "assumptions": "Assumed grid factor=0.45 kg CO2e/kWh; excludes embodied raw materials, upstream energy, rejected yield, transport, life cycle and date-specific grid data", "synthetic": true}];
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

