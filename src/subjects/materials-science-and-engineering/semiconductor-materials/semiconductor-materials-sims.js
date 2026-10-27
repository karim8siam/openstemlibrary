/* Semiconductor Materials Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Epitaxial lattice mismatch",
    "input": {
      "name": "af",
      "label": "Relaxed film lattice parameter",
      "min": 5.38,
      "max": 5.64,
      "default": 5.5,
      "step": 0.002,
      "unit": "angstrom"
    },
    "expression": "100*(af-5.431)/5.431",
    "result_unit": "%",
    "assumptions": "Cubic aligned substrate a=5.431 \u00c5, same temperature and relaxed film parameter; geometry-only mismatch; not a prediction of dislocations",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Bragg diffraction angle",
    "input": {
      "name": "d",
      "label": "Plane spacing",
      "min": 0.16,
      "max": 0.38,
      "default": 0.25,
      "step": 0.002,
      "unit": "nm"
    },
    "expression": "(360/Math.PI)*Math.asin(0.15406/(2*d))",
    "result_unit": "degrees 2\u03b8",
    "assumptions": "First order m=1; monochromatic Cu K\u03b1-like \u03bb=0.15406 nm; perfect geometric diffraction, no refraction or instrument zero",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Band gap and photon wavelength",
    "input": {
      "name": "eg",
      "label": "Photonic transition energy",
      "min": 0.8,
      "max": 3.5,
      "default": 1.5,
      "step": 0.02,
      "unit": "eV"
    },
    "expression": "1239.841984/eg",
    "result_unit": "nm",
    "assumptions": "Vacuum wavelength equivalent to E=hc/\u03bb; not a prediction of absorption strength or radiative efficiency",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Effective conduction density of states",
    "input": {
      "name": "T",
      "label": "Temperature",
      "min": 220,
      "max": 440,
      "default": 300,
      "step": 5,
      "unit": "K"
    },
    "expression": "2.8e19*Math.pow(T/300,1.5)/1e19",
    "result_unit": "10^19 cm^-3",
    "assumptions": "Fixed conduction-band effective mass, 3D parabolic band, nondegenerate approximation; 2.8e19 cm^-3 at 300 K is an illustrative reference",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Intrinsic carrier density, fixed-gap model",
    "input": {
      "name": "T",
      "label": "Absolute temperature",
      "min": 250,
      "max": 400,
      "default": 300,
      "step": 5,
      "unit": "K"
    },
    "expression": "1e10*Math.pow(T/300,1.5)*Math.exp(-1.12/(2*8.617333262145e-5)*(1/T-1/300))/1e10",
    "result_unit": "10^10 cm^-3",
    "assumptions": "Normalized ni at 300 K=1e10 cm^-3, constant Eg=1.12 eV and effective masses; no band-gap narrowing",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Single-carrier conductivity",
    "input": {
      "name": "n",
      "label": "Electron density",
      "min": 100000000000000.0,
      "max": 1e+17,
      "default": 1e+16,
      "step": 100000000000000.0,
      "unit": "cm^-3"
    },
    "expression": "1.602176634e-19*n*1350",
    "result_unit": "S/cm",
    "assumptions": "Electrons dominate; fixed \u03bcn=1350 cm2/(V s), uniform low-field conditions; ignores concentration-dependent scattering",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Mobility\u2013diffusivity relation",
    "input": {
      "name": "mu",
      "label": "Mobility",
      "min": 100,
      "max": 2000,
      "default": 800,
      "step": 25,
      "unit": "cm2/(V s)"
    },
    "expression": "mu*8.617333262145e-5*300",
    "result_unit": "cm2/s",
    "assumptions": "300 K, nondegenerate equilibrium, Einstein relation D=\u03bckT/q; kT/q numerically 0.025852 V",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Minority-carrier diffusion length",
    "input": {
      "name": "tau",
      "label": "Effective lifetime",
      "min": 0.05,
      "max": 10,
      "default": 1.0,
      "step": 0.05,
      "unit": "microseconds"
    },
    "expression": "10000*Math.sqrt(25*tau*1e-6)",
    "result_unit": "micrometers",
    "assumptions": "Uniform D=25 cm2/s, \u03c4 in microseconds, low-injection homogeneous transport, no surface recombination boundaries",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Abrupt junction depletion width",
    "input": {
      "name": "Vr",
      "label": "Applied reverse bias",
      "min": 0,
      "max": 15,
      "default": 2,
      "step": 0.25,
      "unit": "V"
    },
    "expression": "10000*Math.sqrt(2*11.7*8.8541878128e-14/1.602176634e-19*(2/1e16)*(0.7+Vr))",
    "result_unit": "micrometers",
    "assumptions": "Si \u03b5r=11.7, Na=Nd=10^16 cm^-3, built-in potential 0.7 V, ideal abrupt 1D depletion; VR\u22650",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Illustrative diode current density",
    "input": {
      "name": "V",
      "label": "Forward voltage",
      "min": 0,
      "max": 0.65,
      "default": 0.3,
      "step": 0.01,
      "unit": "V"
    },
    "expression": "1e12*(1e-12*(Math.exp(V/(1.5*8.617333262145e-5*300))-1))",
    "result_unit": "pA/cm2",
    "assumptions": "Current in pA/cm2; J0=1e-12 A/cm2, n=1.5, T=300 K; no series resistance, heating, shunts, or reverse breakdown",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Geometric SiO2 capacitance per area",
    "input": {
      "name": "t",
      "label": "Dielectric thickness",
      "min": 2,
      "max": 30,
      "default": 5,
      "step": 0.5,
      "unit": "nm"
    },
    "expression": "(3.9*8.8541878128e-14/(t*1e-7))*1e6",
    "result_unit": "microF/cm2",
    "assumptions": "Relative permittivity 3.9; planar uniform oxide, no quantum capacitance, leakage, interface layer or fringe",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Two-dimensional sheet resistance",
    "input": {
      "name": "ns",
      "label": "Sheet electron density",
      "min": 100000000000.0,
      "max": 10000000000000.0,
      "default": 1000000000000.0,
      "step": 100000000000.0,
      "unit": "cm^-2"
    },
    "expression": "1/(1.602176634e-19*ns*500)",
    "result_unit": "ohm/square",
    "assumptions": "One electron layer, \u03bc=500 cm2/(V s), simple weak-field Drude response; no parallel channels, contacts or localization",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Beer\u2013Lambert absorbed percentage",
    "input": {
      "name": "d",
      "label": "Active-layer thickness",
      "min": 0.1,
      "max": 20,
      "default": 5,
      "step": 0.1,
      "unit": "micrometers"
    },
    "expression": "100*(1-Math.exp(-1000*d*1e-4))",
    "result_unit": "%",
    "assumptions": "Single-pass \u03b1=1000 cm^-1, no surface reflection, spectral changes, scattering or interference",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Photon flux at fixed irradiance",
    "input": {
      "name": "E",
      "label": "Photon energy",
      "min": 1,
      "max": 3.5,
      "default": 2,
      "step": 0.05,
      "unit": "eV"
    },
    "expression": "(0.001/(1.602176634e-19*E))/1e15",
    "result_unit": "10^15 photons/(cm2 s)",
    "assumptions": "Monochromatic radiant power 1 mW/cm2; all photons counted regardless of absorption, no photocarrier yield predicted",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Through-thickness thermal resistance",
    "input": {
      "name": "L",
      "label": "Layer thickness",
      "min": 50,
      "max": 1000,
      "default": 500,
      "step": 10,
      "unit": "micrometers"
    },
    "expression": "(L*1e-6)/(130*1e-4)",
    "result_unit": "K/W",
    "assumptions": "Uniform k=130 W/(m K), area 1 cm2, 1D steady conduction; excludes boundary and spreading resistance",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Poisson random-fatal-defect yield",
    "input": {
      "name": "A",
      "label": "Die area",
      "min": 0.01,
      "max": 3,
      "default": 0.5,
      "step": 0.01,
      "unit": "cm2"
    },
    "expression": "100*Math.exp(-0.5*A)",
    "result_unit": "%",
    "assumptions": "Random spatially independent *fatal* defect density 0.5 per cm2; excludes nonfatal defects, clustering, systematic/parametric failures and time aging",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Epitaxial lattice mismatch", "input": {"name": "af", "label": "Relaxed film lattice parameter", "min": 5.38, "max": 5.64, "default": 5.5, "step": 0.002, "unit": "angstrom"}, "expression": "100*(af-5.431)/5.431", "result_unit": "%", "assumptions": "Cubic aligned substrate a=5.431 Å, same temperature and relaxed film parameter; geometry-only mismatch; not a prediction of dislocations", "synthetic": true}, {"id": 1, "unit": 1, "title": "Bragg diffraction angle", "input": {"name": "d", "label": "Plane spacing", "min": 0.16, "max": 0.38, "default": 0.25, "step": 0.002, "unit": "nm"}, "expression": "(360/Math.PI)*Math.asin(0.15406/(2*d))", "result_unit": "degrees 2θ", "assumptions": "First order m=1; monochromatic Cu Kα-like λ=0.15406 nm; perfect geometric diffraction, no refraction or instrument zero", "synthetic": true}, {"id": 2, "unit": 2, "title": "Band gap and photon wavelength", "input": {"name": "eg", "label": "Photonic transition energy", "min": 0.8, "max": 3.5, "default": 1.5, "step": 0.02, "unit": "eV"}, "expression": "1239.841984/eg", "result_unit": "nm", "assumptions": "Vacuum wavelength equivalent to E=hc/λ; not a prediction of absorption strength or radiative efficiency", "synthetic": true}, {"id": 3, "unit": 2, "title": "Effective conduction density of states", "input": {"name": "T", "label": "Temperature", "min": 220, "max": 440, "default": 300, "step": 5, "unit": "K"}, "expression": "2.8e19*Math.pow(T/300,1.5)/1e19", "result_unit": "10^19 cm^-3", "assumptions": "Fixed conduction-band effective mass, 3D parabolic band, nondegenerate approximation; 2.8e19 cm^-3 at 300 K is an illustrative reference", "synthetic": true}, {"id": 4, "unit": 3, "title": "Intrinsic carrier density, fixed-gap model", "input": {"name": "T", "label": "Absolute temperature", "min": 250, "max": 400, "default": 300, "step": 5, "unit": "K"}, "expression": "1e10*Math.pow(T/300,1.5)*Math.exp(-1.12/(2*8.617333262145e-5)*(1/T-1/300))/1e10", "result_unit": "10^10 cm^-3", "assumptions": "Normalized ni at 300 K=1e10 cm^-3, constant Eg=1.12 eV and effective masses; no band-gap narrowing", "synthetic": true}, {"id": 5, "unit": 3, "title": "Single-carrier conductivity", "input": {"name": "n", "label": "Electron density", "min": 100000000000000.0, "max": 1e+17, "default": 1e+16, "step": 100000000000000.0, "unit": "cm^-3"}, "expression": "1.602176634e-19*n*1350", "result_unit": "S/cm", "assumptions": "Electrons dominate; fixed μn=1350 cm2/(V s), uniform low-field conditions; ignores concentration-dependent scattering", "synthetic": true}, {"id": 6, "unit": 4, "title": "Mobility–diffusivity relation", "input": {"name": "mu", "label": "Mobility", "min": 100, "max": 2000, "default": 800, "step": 25, "unit": "cm2/(V s)"}, "expression": "mu*8.617333262145e-5*300", "result_unit": "cm2/s", "assumptions": "300 K, nondegenerate equilibrium, Einstein relation D=μkT/q; kT/q numerically 0.025852 V", "synthetic": true}, {"id": 7, "unit": 4, "title": "Minority-carrier diffusion length", "input": {"name": "tau", "label": "Effective lifetime", "min": 0.05, "max": 10, "default": 1.0, "step": 0.05, "unit": "microseconds"}, "expression": "10000*Math.sqrt(25*tau*1e-6)", "result_unit": "micrometers", "assumptions": "Uniform D=25 cm2/s, τ in microseconds, low-injection homogeneous transport, no surface recombination boundaries", "synthetic": true}, {"id": 8, "unit": 5, "title": "Abrupt junction depletion width", "input": {"name": "Vr", "label": "Applied reverse bias", "min": 0, "max": 15, "default": 2, "step": 0.25, "unit": "V"}, "expression": "10000*Math.sqrt(2*11.7*8.8541878128e-14/1.602176634e-19*(2/1e16)*(0.7+Vr))", "result_unit": "micrometers", "assumptions": "Si εr=11.7, Na=Nd=10^16 cm^-3, built-in potential 0.7 V, ideal abrupt 1D depletion; VR≥0", "synthetic": true}, {"id": 9, "unit": 5, "title": "Illustrative diode current density", "input": {"name": "V", "label": "Forward voltage", "min": 0, "max": 0.65, "default": 0.3, "step": 0.01, "unit": "V"}, "expression": "1e12*(1e-12*(Math.exp(V/(1.5*8.617333262145e-5*300))-1))", "result_unit": "pA/cm2", "assumptions": "Current in pA/cm2; J0=1e-12 A/cm2, n=1.5, T=300 K; no series resistance, heating, shunts, or reverse breakdown", "synthetic": true}, {"id": 10, "unit": 6, "title": "Geometric SiO2 capacitance per area", "input": {"name": "t", "label": "Dielectric thickness", "min": 2, "max": 30, "default": 5, "step": 0.5, "unit": "nm"}, "expression": "(3.9*8.8541878128e-14/(t*1e-7))*1e6", "result_unit": "microF/cm2", "assumptions": "Relative permittivity 3.9; planar uniform oxide, no quantum capacitance, leakage, interface layer or fringe", "synthetic": true}, {"id": 11, "unit": 6, "title": "Two-dimensional sheet resistance", "input": {"name": "ns", "label": "Sheet electron density", "min": 100000000000.0, "max": 10000000000000.0, "default": 1000000000000.0, "step": 100000000000.0, "unit": "cm^-2"}, "expression": "1/(1.602176634e-19*ns*500)", "result_unit": "ohm/square", "assumptions": "One electron layer, μ=500 cm2/(V s), simple weak-field Drude response; no parallel channels, contacts or localization", "synthetic": true}, {"id": 12, "unit": 7, "title": "Beer–Lambert absorbed percentage", "input": {"name": "d", "label": "Active-layer thickness", "min": 0.1, "max": 20, "default": 5, "step": 0.1, "unit": "micrometers"}, "expression": "100*(1-Math.exp(-1000*d*1e-4))", "result_unit": "%", "assumptions": "Single-pass α=1000 cm^-1, no surface reflection, spectral changes, scattering or interference", "synthetic": true}, {"id": 13, "unit": 7, "title": "Photon flux at fixed irradiance", "input": {"name": "E", "label": "Photon energy", "min": 1, "max": 3.5, "default": 2, "step": 0.05, "unit": "eV"}, "expression": "(0.001/(1.602176634e-19*E))/1e15", "result_unit": "10^15 photons/(cm2 s)", "assumptions": "Monochromatic radiant power 1 mW/cm2; all photons counted regardless of absorption, no photocarrier yield predicted", "synthetic": true}, {"id": 14, "unit": 8, "title": "Through-thickness thermal resistance", "input": {"name": "L", "label": "Layer thickness", "min": 50, "max": 1000, "default": 500, "step": 10, "unit": "micrometers"}, "expression": "(L*1e-6)/(130*1e-4)", "result_unit": "K/W", "assumptions": "Uniform k=130 W/(m K), area 1 cm2, 1D steady conduction; excludes boundary and spreading resistance", "synthetic": true}, {"id": 15, "unit": 8, "title": "Poisson random-fatal-defect yield", "input": {"name": "A", "label": "Die area", "min": 0.01, "max": 3, "default": 0.5, "step": 0.01, "unit": "cm2"}, "expression": "100*Math.exp(-0.5*A)", "result_unit": "%", "assumptions": "Random spatially independent *fatal* defect density 0.5 per cm2; excludes nonfatal defects, clustering, systematic/parametric failures and time aging", "synthetic": true}];
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

