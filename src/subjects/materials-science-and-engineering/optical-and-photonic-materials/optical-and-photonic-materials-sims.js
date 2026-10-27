/* Optical and Photonic Materials Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Normal-incidence Fresnel power reflection",
    "input": {
      "name": "n",
      "label": "Refractive index",
      "min": 1.05,
      "max": 3.5,
      "default": 1.5,
      "step": 0.05,
      "unit": "dimensionless"
    },
    "expression": "100*Math.pow((n-1)/(n+1),2)",
    "result_unit": "%",
    "assumptions": "Air to lossless nonmagnetic dielectric; normal incidence; one isolated flat interface",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Photon energy from vacuum wavelength",
    "input": {
      "name": "lam",
      "label": "Wavelength",
      "min": 350,
      "max": 1600,
      "default": 550,
      "step": 25,
      "unit": "nm"
    },
    "expression": "1239.8419843320026/lam",
    "result_unit": "eV",
    "assumptions": "Vacuum photon energy hc/\u03bb; assumes light can be represented by photons and wavelength is the vacuum wavelength",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Illustrative silica Sellmeier phase index",
    "input": {
      "name": "lam",
      "label": "Vacuum wavelength",
      "min": 0.45,
      "max": 1.9,
      "default": 1.0,
      "step": 0.025,
      "unit": "\u00b5m"
    },
    "expression": "Math.sqrt(1+(0.6961663*lam*lam)/(lam*lam-0.0684043*0.0684043)+(0.4079426*lam*lam)/(lam*lam-0.1162414*0.1162414)+(0.8974794*lam*lam)/(lam*lam-9.896161*9.896161))",
    "result_unit": "dimensionless",
    "assumptions": "Fused-silica example using commonly tabulated Sellmeier coefficients, wavelength in micrometers; transparent region only, ignores temperature and impurity changes",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Cauchy-model group refractive index",
    "input": {
      "name": "lam",
      "label": "Vacuum wavelength",
      "min": 0.6,
      "max": 1.8,
      "default": 1.2,
      "step": 0.025,
      "unit": "\u00b5m"
    },
    "expression": "1.45+0.012/(lam*lam)",
    "result_unit": "dimensionless",
    "assumptions": "n(\u03bb)=1.45+0.004/\u03bb\u00b2 where \u03bb is in \u00b5m; ng=n\u2212\u03bb dn/d\u03bb; illustrative coefficients not a glass certificate",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Beer\u2013Lambert internal transmitted power",
    "input": {
      "name": "a",
      "label": "Intensity absorption coefficient",
      "min": 0,
      "max": 150,
      "default": 40,
      "step": 2,
      "unit": "cm\u207b\u00b9"
    },
    "expression": "100*Math.exp(-a*0.01)",
    "result_unit": "%",
    "assumptions": "Uniform slab with 0.01 cm optical path and constant absorption coefficient; internal absorption only, ignores both Fresnel interfaces and scattering",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Ideal Urbach-tail absorbance sensitivity",
    "input": {
      "name": "E",
      "label": "Photon energy",
      "min": 1.75,
      "max": 2.0,
      "default": 1.85,
      "step": 0.005,
      "unit": "eV"
    },
    "expression": "2*Math.exp((E-1.9)/0.05)",
    "result_unit": "cm\u207b\u00b9",
    "assumptions": "Assumed \u03b1(E)=2 exp[(E\u22121.9)/0.05] cm\u207b\u00b9 with energy in eV; phenomenological absorption tail, no valid bandgap inference by itself",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Quarter-wave dielectric-layer thickness",
    "input": {
      "name": "lam",
      "label": "Design vacuum wavelength",
      "min": 400,
      "max": 1000,
      "default": 600,
      "step": 10,
      "unit": "nm"
    },
    "expression": "lam/(4*1.45)",
    "result_unit": "nm",
    "assumptions": "Normal incidence, nonabsorbing material n=1.45, quarter-wave optical thickness and zero dispersion",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Fabry\u2013P\u00e9rot ideal power transmission",
    "input": {
      "name": "lam",
      "label": "Vacuum wavelength",
      "min": 500,
      "max": 900,
      "default": 700,
      "step": 5,
      "unit": "nm"
    },
    "expression": "100/(1+(4*0.3/Math.pow(1-0.3,2))*Math.pow(Math.sin(2*Math.PI*1.5*1000/lam),2))",
    "result_unit": "%",
    "assumptions": "Symmetric lossless cavity with mirror power reflectance R=0.3, spacer thickness 1000 nm, n=1.5; no phase shifts or angle effects",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Step-index fiber normalized frequency V",
    "input": {
      "name": "a",
      "label": "Core radius",
      "min": 2.0,
      "max": 6.0,
      "default": 4.0,
      "step": 0.1,
      "unit": "\u00b5m"
    },
    "expression": "(2*Math.PI*a/1.55)*Math.sqrt(1.450*1.450-1.444*1.444)",
    "result_unit": "dimensionless",
    "assumptions": "Circular ideal weak-guidance step-index fiber, \u03bb=1.55 \u00b5m, ncore=1.450, nclad=1.444; LP11 cutoff V\u22482.405 for idealized fiber",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Fiber power after uniform dB attenuation",
    "input": {
      "name": "L",
      "label": "Fiber length",
      "min": 0,
      "max": 80,
      "default": 25,
      "step": 1,
      "unit": "km"
    },
    "expression": "100*Math.pow(10,-0.2*L/10)",
    "result_unit": "%",
    "assumptions": "Fiber attenuation 0.2 dB/km constant across length; neglects splice losses, reflections and wavelength changes",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Radiative fraction from competing lifetimes",
    "input": {
      "name": "knr",
      "label": "Nonradiative rate",
      "min": 10000000.0,
      "max": 900000000.0,
      "default": 100000000.0,
      "step": 10000000.0,
      "unit": "s\u207b\u00b9"
    },
    "expression": "100*1e8/(1e8+knr)",
    "result_unit": "%",
    "assumptions": "Simple single-population branching ratio with radiative rate kr=10\u2078 s\u207b\u00b9 and competing knr; not full LED external efficiency",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Emitted photon energy for wavelength",
    "input": {
      "name": "lam",
      "label": "Emission wavelength",
      "min": 400,
      "max": 950,
      "default": 650,
      "step": 10,
      "unit": "nm"
    },
    "expression": "1239.8419843320026/lam",
    "result_unit": "eV",
    "assumptions": "Photon energy hc/\u03bb; not equal to semiconductor band gap in all cases because of Stokes shift and spectral broadening",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Thermo-optic resonant shift",
    "input": {
      "name": "dT",
      "label": "Temperature change",
      "min": 0,
      "max": 40,
      "default": 10,
      "step": 1,
      "unit": "K"
    },
    "expression": "(1550/4)*(1.8e-4*dT)",
    "result_unit": "nm",
    "assumptions": "First-order perturbation \u03bb0/ng\u00d7\u0394n with \u03bb0=1550 nm, ng=4, dn/dT=1.8e\u22124/K; excludes thermal expansion and thermoelastic effects",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Ideal Kerr nonlinear phase shift",
    "input": {
      "name": "P",
      "label": "Optical power",
      "min": 0,
      "max": 2,
      "default": 0.5,
      "step": 0.05,
      "unit": "W"
    },
    "expression": "1.3*P*10",
    "result_unit": "rad",
    "assumptions": "Effective fiber nonlinear coefficient \u03b3=1.3 W\u207b\u00b9 km\u207b\u00b9, uniform power, L=10 km; neglects attenuation and dispersion",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Rayleigh-type wavelength scaling",
    "input": {
      "name": "lam",
      "label": "Vacuum wavelength",
      "min": 400,
      "max": 1000,
      "default": 600,
      "step": 10,
      "unit": "nm"
    },
    "expression": "Math.pow(550/lam,4)",
    "result_unit": "relative",
    "assumptions": "Idealized scatter-loss proxy proportional to \u03bb\u207b\u2074 at fixed particle-size distribution, normalized to 550 nm; not a measured glass or haze spectrum",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Optical resonator quality factor",
    "input": {
      "name": "dw",
      "label": "Resonance linewidth",
      "min": 0.01,
      "max": 2,
      "default": 0.2,
      "step": 0.01,
      "unit": "nm"
    },
    "expression": "1550/dw",
    "result_unit": "dimensionless",
    "assumptions": "Q\u2248\u03bb0/\u0394\u03bb for narrow resonances at 1550 nm, with a consistently defined linewidth; assumes spectral Q estimates apply",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Normal-incidence Fresnel power reflection", "input": {"name": "n", "label": "Refractive index", "min": 1.05, "max": 3.5, "default": 1.5, "step": 0.05, "unit": "dimensionless"}, "expression": "100*Math.pow((n-1)/(n+1),2)", "result_unit": "%", "assumptions": "Air to lossless nonmagnetic dielectric; normal incidence; one isolated flat interface", "synthetic": true}, {"id": 1, "unit": 1, "title": "Photon energy from vacuum wavelength", "input": {"name": "lam", "label": "Wavelength", "min": 350, "max": 1600, "default": 550, "step": 25, "unit": "nm"}, "expression": "1239.8419843320026/lam", "result_unit": "eV", "assumptions": "Vacuum photon energy hc/λ; assumes light can be represented by photons and wavelength is the vacuum wavelength", "synthetic": true}, {"id": 2, "unit": 2, "title": "Illustrative silica Sellmeier phase index", "input": {"name": "lam", "label": "Vacuum wavelength", "min": 0.45, "max": 1.9, "default": 1.0, "step": 0.025, "unit": "µm"}, "expression": "Math.sqrt(1+(0.6961663*lam*lam)/(lam*lam-0.0684043*0.0684043)+(0.4079426*lam*lam)/(lam*lam-0.1162414*0.1162414)+(0.8974794*lam*lam)/(lam*lam-9.896161*9.896161))", "result_unit": "dimensionless", "assumptions": "Fused-silica example using commonly tabulated Sellmeier coefficients, wavelength in micrometers; transparent region only, ignores temperature and impurity changes", "synthetic": true}, {"id": 3, "unit": 2, "title": "Cauchy-model group refractive index", "input": {"name": "lam", "label": "Vacuum wavelength", "min": 0.6, "max": 1.8, "default": 1.2, "step": 0.025, "unit": "µm"}, "expression": "1.45+0.012/(lam*lam)", "result_unit": "dimensionless", "assumptions": "n(λ)=1.45+0.004/λ² where λ is in µm; ng=n−λ dn/dλ; illustrative coefficients not a glass certificate", "synthetic": true}, {"id": 4, "unit": 3, "title": "Beer–Lambert internal transmitted power", "input": {"name": "a", "label": "Intensity absorption coefficient", "min": 0, "max": 150, "default": 40, "step": 2, "unit": "cm⁻¹"}, "expression": "100*Math.exp(-a*0.01)", "result_unit": "%", "assumptions": "Uniform slab with 0.01 cm optical path and constant absorption coefficient; internal absorption only, ignores both Fresnel interfaces and scattering", "synthetic": true}, {"id": 5, "unit": 3, "title": "Ideal Urbach-tail absorbance sensitivity", "input": {"name": "E", "label": "Photon energy", "min": 1.75, "max": 2.0, "default": 1.85, "step": 0.005, "unit": "eV"}, "expression": "2*Math.exp((E-1.9)/0.05)", "result_unit": "cm⁻¹", "assumptions": "Assumed α(E)=2 exp[(E−1.9)/0.05] cm⁻¹ with energy in eV; phenomenological absorption tail, no valid bandgap inference by itself", "synthetic": true}, {"id": 6, "unit": 4, "title": "Quarter-wave dielectric-layer thickness", "input": {"name": "lam", "label": "Design vacuum wavelength", "min": 400, "max": 1000, "default": 600, "step": 10, "unit": "nm"}, "expression": "lam/(4*1.45)", "result_unit": "nm", "assumptions": "Normal incidence, nonabsorbing material n=1.45, quarter-wave optical thickness and zero dispersion", "synthetic": true}, {"id": 7, "unit": 4, "title": "Fabry–Pérot ideal power transmission", "input": {"name": "lam", "label": "Vacuum wavelength", "min": 500, "max": 900, "default": 700, "step": 5, "unit": "nm"}, "expression": "100/(1+(4*0.3/Math.pow(1-0.3,2))*Math.pow(Math.sin(2*Math.PI*1.5*1000/lam),2))", "result_unit": "%", "assumptions": "Symmetric lossless cavity with mirror power reflectance R=0.3, spacer thickness 1000 nm, n=1.5; no phase shifts or angle effects", "synthetic": true}, {"id": 8, "unit": 5, "title": "Step-index fiber normalized frequency V", "input": {"name": "a", "label": "Core radius", "min": 2.0, "max": 6.0, "default": 4.0, "step": 0.1, "unit": "µm"}, "expression": "(2*Math.PI*a/1.55)*Math.sqrt(1.450*1.450-1.444*1.444)", "result_unit": "dimensionless", "assumptions": "Circular ideal weak-guidance step-index fiber, λ=1.55 µm, ncore=1.450, nclad=1.444; LP11 cutoff V≈2.405 for idealized fiber", "synthetic": true}, {"id": 9, "unit": 5, "title": "Fiber power after uniform dB attenuation", "input": {"name": "L", "label": "Fiber length", "min": 0, "max": 80, "default": 25, "step": 1, "unit": "km"}, "expression": "100*Math.pow(10,-0.2*L/10)", "result_unit": "%", "assumptions": "Fiber attenuation 0.2 dB/km constant across length; neglects splice losses, reflections and wavelength changes", "synthetic": true}, {"id": 10, "unit": 6, "title": "Radiative fraction from competing lifetimes", "input": {"name": "knr", "label": "Nonradiative rate", "min": 10000000.0, "max": 900000000.0, "default": 100000000.0, "step": 10000000.0, "unit": "s⁻¹"}, "expression": "100*1e8/(1e8+knr)", "result_unit": "%", "assumptions": "Simple single-population branching ratio with radiative rate kr=10⁸ s⁻¹ and competing knr; not full LED external efficiency", "synthetic": true}, {"id": 11, "unit": 6, "title": "Emitted photon energy for wavelength", "input": {"name": "lam", "label": "Emission wavelength", "min": 400, "max": 950, "default": 650, "step": 10, "unit": "nm"}, "expression": "1239.8419843320026/lam", "result_unit": "eV", "assumptions": "Photon energy hc/λ; not equal to semiconductor band gap in all cases because of Stokes shift and spectral broadening", "synthetic": true}, {"id": 12, "unit": 7, "title": "Thermo-optic resonant shift", "input": {"name": "dT", "label": "Temperature change", "min": 0, "max": 40, "default": 10, "step": 1, "unit": "K"}, "expression": "(1550/4)*(1.8e-4*dT)", "result_unit": "nm", "assumptions": "First-order perturbation λ0/ng×Δn with λ0=1550 nm, ng=4, dn/dT=1.8e−4/K; excludes thermal expansion and thermoelastic effects", "synthetic": true}, {"id": 13, "unit": 7, "title": "Ideal Kerr nonlinear phase shift", "input": {"name": "P", "label": "Optical power", "min": 0, "max": 2, "default": 0.5, "step": 0.05, "unit": "W"}, "expression": "1.3*P*10", "result_unit": "rad", "assumptions": "Effective fiber nonlinear coefficient γ=1.3 W⁻¹ km⁻¹, uniform power, L=10 km; neglects attenuation and dispersion", "synthetic": true}, {"id": 14, "unit": 8, "title": "Rayleigh-type wavelength scaling", "input": {"name": "lam", "label": "Vacuum wavelength", "min": 400, "max": 1000, "default": 600, "step": 10, "unit": "nm"}, "expression": "Math.pow(550/lam,4)", "result_unit": "relative", "assumptions": "Idealized scatter-loss proxy proportional to λ⁻⁴ at fixed particle-size distribution, normalized to 550 nm; not a measured glass or haze spectrum", "synthetic": true}, {"id": 15, "unit": 8, "title": "Optical resonator quality factor", "input": {"name": "dw", "label": "Resonance linewidth", "min": 0.01, "max": 2, "default": 0.2, "step": 0.01, "unit": "nm"}, "expression": "1550/dw", "result_unit": "dimensionless", "assumptions": "Q≈λ0/Δλ for narrow resonances at 1550 nm, with a consistently defined linewidth; assumes spectral Q estimates apply", "synthetic": true}];
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

