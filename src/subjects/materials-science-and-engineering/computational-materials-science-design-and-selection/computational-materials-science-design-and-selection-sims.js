/* Computational Materials Science, Design and Selection Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Toy discretization-error scaling",
    "input": {
      "name": "h",
      "label": "Grid spacing ratio",
      "min": 0.1,
      "max": 2,
      "default": 1,
      "step": 0.05,
      "unit": "dimensionless"
    },
    "expression": "0.02*h*h",
    "result_unit": "relative error",
    "assumptions": "Hypothetical second-order error coefficient 0.02; only truncation scaling is represented, not the total error or spatial convergence of any actual PDE code.",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Amdahl parallel ideal speedup",
    "input": {
      "name": "f",
      "label": "Parallelizable workload",
      "min": 20,
      "max": 99,
      "default": 80,
      "step": 1,
      "unit": "%"
    },
    "expression": "1/((1-f/100)+(f/100)/8)",
    "result_unit": "speedup \u00d7",
    "assumptions": "Eight ideal equal workers, zero communication overhead, fixed problem size, serial fraction exactly 1\u2212f; actual scalability requires measurement.",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Harmonic pair energy relative to minimum",
    "input": {
      "name": "r",
      "label": "Atom separation",
      "min": 1.6,
      "max": 2.5,
      "default": 2,
      "step": 0.01,
      "unit": "\u00c5"
    },
    "expression": "0.5*40*Math.pow(r-2,2)",
    "result_unit": "eV",
    "assumptions": "One invented pair with equilibrium distance 2 \u00c5 and curvature 40 eV/\u00c5\u00b2; does not represent a calibrated crystal potential, phase diagram, or real atomic pair.",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Toy Arrhenius activated-event rate",
    "input": {
      "name": "T",
      "label": "Temperature",
      "min": 350,
      "max": 1200,
      "default": 700,
      "step": 10,
      "unit": "K"
    },
    "expression": "1e12*Math.exp(-0.75/(8.617333262e-5*T))",
    "result_unit": "events/s per site",
    "assumptions": "Invented barrier 0.75 eV and attempt rate 1e12 s\u207b\u00b9; independent events and fixed mechanism, no temperature-dependent entropy or competing paths.",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "One-dimensional diffusion RMS displacement",
    "input": {
      "name": "t",
      "label": "Diffusion time",
      "min": 0.5,
      "max": 100,
      "default": 12,
      "step": 0.5,
      "unit": "h"
    },
    "expression": "Math.sqrt(2*1e-16*t*3600)*1e6",
    "result_unit": "\u00b5m",
    "assumptions": "Constant D=1e\u221216 m\u00b2/s and unbounded 1D diffusion; effective transport in real materials can be anisotropic, concentration-dependent, trapped or boundary-limited.",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Ideal regular-solution mixing Gibbs energy",
    "input": {
      "name": "x",
      "label": "Component A mole fraction",
      "min": 5,
      "max": 95,
      "default": 50,
      "step": 1,
      "unit": "%"
    },
    "expression": "(8.314*800*((x/100)*Math.log(x/100)+(1-x/100)*Math.log(1-x/100))+16000*(x/100)*(1-x/100))/1000",
    "result_unit": "kJ/mol",
    "assumptions": "T=800 K, invented constant interaction \u03a9=16 kJ/mol, ideal configurational entropy, no other phases or magnetic/vibrational free energies; purely illustrative.",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Uniaxial elastic strain",
    "input": {
      "name": "s",
      "label": "Applied engineering stress",
      "min": 20,
      "max": 400,
      "default": 180,
      "step": 10,
      "unit": "MPa"
    },
    "expression": "s/200000*1e6",
    "result_unit": "microstrain",
    "assumptions": "Linear uniaxial small-strain elasticity with E=200 GPa, no plasticity, creep, anisotropy, thermal stress or damage.",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Ideal thermal diffusion time",
    "input": {
      "name": "L",
      "label": "Thermal length scale",
      "min": 1,
      "max": 20,
      "default": 5,
      "step": 0.5,
      "unit": "mm"
    },
    "expression": "Math.pow(L/1000,2)/1e-5",
    "result_unit": "s",
    "assumptions": "Constant thermal diffusivity 1e\u22125 m\u00b2/s and simple L\u00b2/\u03b1 scaling, omitting geometry factors, boundary exchange, radiative losses and phase changes.",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Nominal Gaussian predictive half-width",
    "input": {
      "name": "sig",
      "label": "Residual standard deviation",
      "min": 0.05,
      "max": 0.6,
      "default": 0.2,
      "step": 0.01,
      "unit": "property units"
    },
    "expression": "1.96*sig",
    "result_unit": "property units",
    "assumptions": "Assumes unbiased Gaussian independent residuals and correct \u03c3 including model and measurement uncertainty; not guaranteed calibrated out of distribution.",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Toy input-space novelty score",
    "input": {
      "name": "d",
      "label": "Standardized feature deviation",
      "min": 0,
      "max": 5,
      "default": 2,
      "step": 0.1,
      "unit": "standard deviations"
    },
    "expression": "Math.sqrt(3*d*d+1)",
    "result_unit": "dimensionless score",
    "assumptions": "Invented score from one feature deviation and three equal contributions; not a trained OOD detector, p-value or prediction error estimate.",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Toy stiffness-limited material index",
    "input": {
      "name": "E",
      "label": "Young modulus",
      "min": 20,
      "max": 300,
      "default": 120,
      "step": 5,
      "unit": "GPa"
    },
    "expression": "Math.sqrt(E)/2.7",
    "result_unit": "\u221aGPa/(g/cm\u00b3)",
    "assumptions": "Fixed density 2.7 g/cm\u00b3 and square-root modulus over density scaling for selected similarly scaled beam designs; does not rank real parts under all constraints.",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Service-normalized acquisition cost",
    "input": {
      "name": "life",
      "label": "Service life",
      "min": 2,
      "max": 30,
      "default": 10,
      "step": 1,
      "unit": "years"
    },
    "expression": "400/life",
    "result_unit": "USD/year",
    "assumptions": "Fixed illustrative acquisition cost USD 400, constant useful function, no discounting, upkeep, failure consequence, salvage or depreciation effects.",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Linear two-phase rule of mixtures",
    "input": {
      "name": "x",
      "label": "Volume fraction of stiff phase",
      "min": 0,
      "max": 100,
      "default": 50,
      "step": 1,
      "unit": "%"
    },
    "expression": "120*(x/100)+80*(1-x/100)",
    "result_unit": "GPa",
    "assumptions": "Invented phase moduli 120 and 80 GPa with iso-strain upper-bound ideal mixture, perfect bonding and no porosity or geometry dependence.",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Chebyshev failure-probability upper bound",
    "input": {
      "name": "m",
      "label": "Margin to failure limit",
      "min": 2,
      "max": 10,
      "default": 5,
      "step": 0.25,
      "unit": "property units"
    },
    "expression": "Math.min(1,4/(m*m))",
    "result_unit": "probability upper bound",
    "assumptions": "Variance assumed \u03c3\u00b2=4 in matching property units; upper bound from Chebyshev under finite variance, not predicted actual probability or distribution model.",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Toy thermal activation transport",
    "input": {
      "name": "T",
      "label": "Operating temperature",
      "min": 300,
      "max": 800,
      "default": 450,
      "step": 10,
      "unit": "K"
    },
    "expression": "1e-7*Math.exp(-0.40/(8.617333262e-5*T))",
    "result_unit": "m\u00b2/s",
    "assumptions": "Fixed hypothetical prefactor 1e\u22127 m\u00b2/s and activation energy 0.40 eV; no changes in phase, chemistry, mechanism or temperature-dependent prefactor.",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Train versus external-test absolute-error gap",
    "input": {
      "name": "test",
      "label": "External test MAE",
      "min": 0.05,
      "max": 0.6,
      "default": 0.25,
      "step": 0.01,
      "unit": "property units"
    },
    "expression": "test-0.07",
    "result_unit": "property units",
    "assumptions": "Invented training MAE fixed at 0.07 property units; gap does not alone diagnose dataset shift or model validity.",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Toy discretization-error scaling", "input": {"name": "h", "label": "Grid spacing ratio", "min": 0.1, "max": 2, "default": 1, "step": 0.05, "unit": "dimensionless"}, "expression": "0.02*h*h", "result_unit": "relative error", "assumptions": "Hypothetical second-order error coefficient 0.02; only truncation scaling is represented, not the total error or spatial convergence of any actual PDE code.", "synthetic": true}, {"id": 1, "unit": 1, "title": "Amdahl parallel ideal speedup", "input": {"name": "f", "label": "Parallelizable workload", "min": 20, "max": 99, "default": 80, "step": 1, "unit": "%"}, "expression": "1/((1-f/100)+(f/100)/8)", "result_unit": "speedup ×", "assumptions": "Eight ideal equal workers, zero communication overhead, fixed problem size, serial fraction exactly 1−f; actual scalability requires measurement.", "synthetic": true}, {"id": 2, "unit": 2, "title": "Harmonic pair energy relative to minimum", "input": {"name": "r", "label": "Atom separation", "min": 1.6, "max": 2.5, "default": 2, "step": 0.01, "unit": "Å"}, "expression": "0.5*40*Math.pow(r-2,2)", "result_unit": "eV", "assumptions": "One invented pair with equilibrium distance 2 Å and curvature 40 eV/Å²; does not represent a calibrated crystal potential, phase diagram, or real atomic pair.", "synthetic": true}, {"id": 3, "unit": 2, "title": "Toy Arrhenius activated-event rate", "input": {"name": "T", "label": "Temperature", "min": 350, "max": 1200, "default": 700, "step": 10, "unit": "K"}, "expression": "1e12*Math.exp(-0.75/(8.617333262e-5*T))", "result_unit": "events/s per site", "assumptions": "Invented barrier 0.75 eV and attempt rate 1e12 s⁻¹; independent events and fixed mechanism, no temperature-dependent entropy or competing paths.", "synthetic": true}, {"id": 4, "unit": 3, "title": "One-dimensional diffusion RMS displacement", "input": {"name": "t", "label": "Diffusion time", "min": 0.5, "max": 100, "default": 12, "step": 0.5, "unit": "h"}, "expression": "Math.sqrt(2*1e-16*t*3600)*1e6", "result_unit": "µm", "assumptions": "Constant D=1e−16 m²/s and unbounded 1D diffusion; effective transport in real materials can be anisotropic, concentration-dependent, trapped or boundary-limited.", "synthetic": true}, {"id": 5, "unit": 3, "title": "Ideal regular-solution mixing Gibbs energy", "input": {"name": "x", "label": "Component A mole fraction", "min": 5, "max": 95, "default": 50, "step": 1, "unit": "%"}, "expression": "(8.314*800*((x/100)*Math.log(x/100)+(1-x/100)*Math.log(1-x/100))+16000*(x/100)*(1-x/100))/1000", "result_unit": "kJ/mol", "assumptions": "T=800 K, invented constant interaction Ω=16 kJ/mol, ideal configurational entropy, no other phases or magnetic/vibrational free energies; purely illustrative.", "synthetic": true}, {"id": 6, "unit": 4, "title": "Uniaxial elastic strain", "input": {"name": "s", "label": "Applied engineering stress", "min": 20, "max": 400, "default": 180, "step": 10, "unit": "MPa"}, "expression": "s/200000*1e6", "result_unit": "microstrain", "assumptions": "Linear uniaxial small-strain elasticity with E=200 GPa, no plasticity, creep, anisotropy, thermal stress or damage.", "synthetic": true}, {"id": 7, "unit": 4, "title": "Ideal thermal diffusion time", "input": {"name": "L", "label": "Thermal length scale", "min": 1, "max": 20, "default": 5, "step": 0.5, "unit": "mm"}, "expression": "Math.pow(L/1000,2)/1e-5", "result_unit": "s", "assumptions": "Constant thermal diffusivity 1e−5 m²/s and simple L²/α scaling, omitting geometry factors, boundary exchange, radiative losses and phase changes.", "synthetic": true}, {"id": 8, "unit": 5, "title": "Nominal Gaussian predictive half-width", "input": {"name": "sig", "label": "Residual standard deviation", "min": 0.05, "max": 0.6, "default": 0.2, "step": 0.01, "unit": "property units"}, "expression": "1.96*sig", "result_unit": "property units", "assumptions": "Assumes unbiased Gaussian independent residuals and correct σ including model and measurement uncertainty; not guaranteed calibrated out of distribution.", "synthetic": true}, {"id": 9, "unit": 5, "title": "Toy input-space novelty score", "input": {"name": "d", "label": "Standardized feature deviation", "min": 0, "max": 5, "default": 2, "step": 0.1, "unit": "standard deviations"}, "expression": "Math.sqrt(3*d*d+1)", "result_unit": "dimensionless score", "assumptions": "Invented score from one feature deviation and three equal contributions; not a trained OOD detector, p-value or prediction error estimate.", "synthetic": true}, {"id": 10, "unit": 6, "title": "Toy stiffness-limited material index", "input": {"name": "E", "label": "Young modulus", "min": 20, "max": 300, "default": 120, "step": 5, "unit": "GPa"}, "expression": "Math.sqrt(E)/2.7", "result_unit": "√GPa/(g/cm³)", "assumptions": "Fixed density 2.7 g/cm³ and square-root modulus over density scaling for selected similarly scaled beam designs; does not rank real parts under all constraints.", "synthetic": true}, {"id": 11, "unit": 6, "title": "Service-normalized acquisition cost", "input": {"name": "life", "label": "Service life", "min": 2, "max": 30, "default": 10, "step": 1, "unit": "years"}, "expression": "400/life", "result_unit": "USD/year", "assumptions": "Fixed illustrative acquisition cost USD 400, constant useful function, no discounting, upkeep, failure consequence, salvage or depreciation effects.", "synthetic": true}, {"id": 12, "unit": 7, "title": "Linear two-phase rule of mixtures", "input": {"name": "x", "label": "Volume fraction of stiff phase", "min": 0, "max": 100, "default": 50, "step": 1, "unit": "%"}, "expression": "120*(x/100)+80*(1-x/100)", "result_unit": "GPa", "assumptions": "Invented phase moduli 120 and 80 GPa with iso-strain upper-bound ideal mixture, perfect bonding and no porosity or geometry dependence.", "synthetic": true}, {"id": 13, "unit": 7, "title": "Chebyshev failure-probability upper bound", "input": {"name": "m", "label": "Margin to failure limit", "min": 2, "max": 10, "default": 5, "step": 0.25, "unit": "property units"}, "expression": "Math.min(1,4/(m*m))", "result_unit": "probability upper bound", "assumptions": "Variance assumed σ²=4 in matching property units; upper bound from Chebyshev under finite variance, not predicted actual probability or distribution model.", "synthetic": true}, {"id": 14, "unit": 8, "title": "Toy thermal activation transport", "input": {"name": "T", "label": "Operating temperature", "min": 300, "max": 800, "default": 450, "step": 10, "unit": "K"}, "expression": "1e-7*Math.exp(-0.40/(8.617333262e-5*T))", "result_unit": "m²/s", "assumptions": "Fixed hypothetical prefactor 1e−7 m²/s and activation energy 0.40 eV; no changes in phase, chemistry, mechanism or temperature-dependent prefactor.", "synthetic": true}, {"id": 15, "unit": 8, "title": "Train versus external-test absolute-error gap", "input": {"name": "test", "label": "External test MAE", "min": 0.05, "max": 0.6, "default": 0.25, "step": 0.01, "unit": "property units"}, "expression": "test-0.07", "result_unit": "property units", "assumptions": "Invented training MAE fixed at 0.07 property units; gap does not alone diagnose dataset shift or model validity.", "synthetic": true}];
function evaluate(id,x){switch(id){
case 0:return 0.02*x*x;
case 1:return 1/((1-x/100)+(x/100)/8);
case 2:return 0.5*40*Math.pow(x-2,2);
case 3:return 1e12*Math.exp(-0.75/(8.617333262e-5*x));
case 4:return Math.sqrt(2*1e-16*x*3600)*1e6;
case 5:return (8.314*800*((x/100)*Math.log(x/100)+(1-x/100)*Math.log(1-x/100))+16000*(x/100)*(1-x/100))/1000;
case 6:return x/200000*1e6;
case 7:return Math.pow(x/1000,2)/1e-5;
case 8:return 1.96*x;
case 9:return Math.sqrt(3*x*x+1);
case 10:return Math.sqrt(x)/2.7;
case 11:return 400/x;
case 12:return 120*(x/100)+80*(1-x/100);
case 13:return Math.min(1,4/(x*x));
case 14:return 1e-7*Math.exp(-0.40/(8.617333262e-5*x));
case 15:return x-0.07;
default:throw Error("unknown model");}}
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
if(typeof document !== 'undefined') document.addEventListener('DOMContentLoaded',()=>{for(const card of document.querySelectorAll('.model-card')){
 const r=card.querySelector('input');r.addEventListener('input',()=>redraw(card));redraw(card);
}});





if(typeof module!=="undefined" && module.exports){module.exports={evaluate};}



(function (global) {
  'use strict';

  global.mountSimulation = function (container, simType) {
    if (!container) return;
    container.innerHTML = '';
    container.className = 'sim-instance simulation-suite active';

    var match = (simType || '').match(/(\d+)$/);
    var unitNum = match ? parseInt(match[1], 10) : 1;

    var unitModels = [];
    if (typeof MSE_MODELS !== 'undefined' && Array.isArray(MSE_MODELS)) {
      unitModels = MSE_MODELS.filter(function (m) {
        return m.unit === unitNum;
      });
      if (unitModels.length === 0) {
        var startIdx = (unitNum - 1) * 2;
        unitModels = MSE_MODELS.slice(startIdx, startIdx + 2);
      }
    }

    if (unitModels.length === 0) {
      container.innerHTML = '<div style="padding:1.5rem;text-align:center;color:#94a3b8;">' +
        'Interactive calculation simulation initializing for Unit ' + unitNum + '...</div>';
      return;
    }

    var header = document.createElement('div');
    header.style.marginBottom = '1.25rem';
    header.innerHTML = '<h3 style="margin:0 0 0.4rem 0;color:#f8fafc;font-size:1.15rem;">Unit ' + unitNum + ' Interactive Parameter Calculator</h3>' +
      '<p style="margin:0;color:#94a3b8;font-size:0.9rem;">Explore analytical expressions and parameter sensitivities by adjusting input values.</p>';
    container.appendChild(header);

    unitModels.forEach(function (model, mIdx) {
      var card = document.createElement('section');
      card.className = 'sim-card model';
      card.style.background = '#0f172a';
      card.style.border = '1px solid #334155';
      card.style.borderRadius = '0.75rem';
      card.style.padding = '1.25rem';
      card.style.marginBottom = '1.5rem';

      var titleText = model.name || model.title || ('Model ' + (mIdx + 1));
      var descText = model.topic || model.description || '';
      var formulaText = model.expression || model.formula || '';
      var inputDef = model.input || {};
      var outputDef = model.output || {};

      var minVal = (typeof inputDef.min === 'number') ? inputDef.min : 0;
      var maxVal = (typeof inputDef.max === 'number') ? inputDef.max : 100;
      var defaultVal = (typeof inputDef.default === 'number') ? inputDef.default : (minVal + maxVal) / 2;
      var inStep = (typeof inputDef.step === 'number') ? inputDef.step : ((maxVal - minVal) / 100);
      var inUnit = inputDef.unit || '';
      var outUnit = outputDef.unit || '';

      var cardHtml = '<div style="margin-bottom:1rem;">' +
        '<h4 style="margin:0 0 0.35rem 0;color:#38bdf8;font-size:1.05rem;">' + titleText + '</h4>' +
        (descText ? '<p style="margin:0 0 0.5rem 0;color:#cbd5e1;font-size:0.875rem;">' + descText + '</p>' : '') +
        (formulaText ? '<div style="padding:0.4rem 0.75rem;background:#1e293b;border-radius:0.375rem;font-family:monospace;color:#a5f3fc;font-size:0.85rem;margin-bottom:0.75rem;">' + formulaText + '</div>' : '') +
        '</div>';

      cardHtml += '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;align-items:center;">' +
        '<div>' +
        '<label style="display:block;font-size:0.85rem;font-weight:600;color:#e2e8f0;margin-bottom:0.35rem;">Input Parameter (' + (inUnit || 'value') + '): <span class="val-display" style="color:#38bdf8;font-family:monospace;">' + defaultVal + '</span></label>' +
        '<input type="range" class="param-slider" min="' + minVal + '" max="' + maxVal + '" step="' + inStep + '" value="' + defaultVal + '" style="width:100%;accent-color:#0284c7;cursor:pointer;"/>' +
        '</div>' +
        '<div style="background:#1e293b;padding:0.75rem 1rem;border-radius:0.5rem;border-left:4px solid #0284c7;">' +
        '<div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.05em;color:#94a3b8;">Calculated Output (' + (outUnit || 'result') + ')</div>' +
        '<div class="calc-output" style="font-size:1.35rem;font-weight:700;color:#38bdf8;font-family:monospace;margin-top:0.25rem;">--</div>' +
        '</div>' +
        '</div>';

      cardHtml += '<div style="margin-top:1.25rem;padding:0.75rem;background:#1e293b;border-radius:0.5rem;">' +
        '<svg class="plot-svg" viewBox="0 0 400 170" style="width:100%;height:170px;overflow:visible;" role="img" aria-label="' + titleText + ' plot"></svg>' +
        '</div>';

      card.innerHTML = cardHtml;
      container.appendChild(card);

      var slider = card.querySelector('.param-slider');
      var valDisplay = card.querySelector('.val-display');
      var outDisplay = card.querySelector('.calc-output');
      var plot = card.querySelector('.plot-svg');

      function evaluateExpr(x) {
        try {
          if (typeof model.compute === 'function') {
            return model.compute(x);
          }
          if (formulaText) {
            var sanitized = formulaText
              .replace(/\^/g, '**')
              .replace(/exp\(/g, 'Math.exp(')
              .replace(/log\(/g, 'Math.log(')
              .replace(/sqrt\(/g, 'Math.sqrt(')
              .replace(/sin\(/g, 'Math.sin(')
              .replace(/cos\(/g, 'Math.cos(')
              .replace(/pi/gi, 'Math.PI');
            var fn = new Function('x', 'with(Math){ return (' + sanitized + '); }');
            var res = fn(x);
            if (!isNaN(res) && isFinite(res)) return res;
          }
        } catch (e) {
          // fallback linear model
        }
        var mSlope = (outputDef.max - outputDef.min) / (maxVal - minVal || 1);
        return (outputDef.min || 0) + mSlope * (x - minVal);
      }

      function update() {
        var x = parseFloat(slider.value);
        valDisplay.textContent = x.toLocaleString(undefined, { maximumFractionDigits: 3 });
        var y = evaluateExpr(x);
        var prettyY = (typeof y === 'number' && !isNaN(y)) ? y.toLocaleString(undefined, { maximumFractionDigits: 4 }) : '--';
        outDisplay.textContent = prettyY + (outUnit ? ' ' + outUnit : '');

        var nPts = 50;
        var pts = [];
        var yMin = Infinity, yMax = -Infinity;
        for (var i = 0; i <= nPts; i++) {
          var px = minVal + (i / nPts) * (maxVal - minVal);
          var py = evaluateExpr(px);
          if (isFinite(py)) {
            pts.push({ x: px, y: py });
            if (py < yMin) yMin = py;
            if (py > yMax) yMax = py;
          }
        }
        if (yMin === yMax) { yMin -= 1; yMax += 1; }
        var ySpan = yMax - yMin || 1;

        var poly = pts.map(function (pt) {
          var sx = 40 + ((pt.x - minVal) / (maxVal - minVal || 1)) * 330;
          var sy = 140 - ((pt.y - yMin) / ySpan) * 120;
          return sx.toFixed(1) + ',' + sy.toFixed(1);
        }).join(' ');

        var curPx = 40 + ((x - minVal) / (maxVal - minVal || 1)) * 330;
        var curPy = 140 - ((y - yMin) / ySpan) * 120;
        if (!isFinite(curPy)) curPy = 80;
        var cx = curPx.toFixed(1);
        var cy = curPy.toFixed(1);

        plot.innerHTML = '<rect width="400" height="170" fill="#0f172a" rx="4"/>' +
          '<line x1="38" y1="142" x2="372" y2="142" stroke="#475569" stroke-width="1.5"/>' +
          '<line x1="38" y1="15" x2="38" y2="142" stroke="#475569" stroke-width="1.5"/>' +
          '<polyline fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" points="' + poly + '"/>' +
          '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="#f97316"/>' +
          '<text x="40" y="160" fill="#94a3b8" font-size="11">' + minVal + (inUnit ? ' ' + inUnit : '') + '</text>' +
          '<text x="370" y="160" fill="#94a3b8" font-size="11" text-anchor="end">' + maxVal + (inUnit ? ' ' + inUnit : '') + '</text>' +
          '<text x="35" y="25" fill="#94a3b8" font-size="10" text-anchor="end">' + (isFinite(yMax) ? yMax.toFixed(1) : '') + '</text>' +
          '<text x="35" y="142" fill="#94a3b8" font-size="10" text-anchor="end">' + (isFinite(yMin) ? yMin.toFixed(1) : '') + '</text>';
        plot.setAttribute('aria-label', titleText + ': current input ' + x + ', output ' + prettyY);
      }

      slider.addEventListener('input', update);
      update();
    });
  };
})(typeof window === 'undefined' ? globalThis : window);

