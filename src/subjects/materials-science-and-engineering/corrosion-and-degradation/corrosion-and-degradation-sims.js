/* Corrosion and Degradation Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Iron Faraday uniform penetration",
    "input": {
      "name": "i",
      "label": "Dissolution current density",
      "min": 0.1,
      "max": 30,
      "default": 5,
      "step": 0.1,
      "unit": "\u00b5A/cm\u00b2"
    },
    "expression": "i*0.01*0.055845/(2*96485.33212*7850)*31557600000",
    "result_unit": "mm/year",
    "assumptions": "Pure Fe, Fe\u2192Fe\u00b2\u207a, density 7850 kg/m\u00b3, 100% dissolution efficiency and perfectly uniform attack; not a pit-depth forecast.",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Nernst iron-ion potential vs SHE",
    "input": {
      "name": "a",
      "label": "Fe\u00b2\u207a activity",
      "min": 0.0001,
      "max": 1,
      "default": 0.01,
      "step": 0.0001,
      "unit": "dimensionless"
    },
    "expression": "-0.44+(8.314462618*298.15/(2*96485.33212))*Math.log(a)",
    "result_unit": "V vs SHE",
    "assumptions": "Ideal Fe\u00b2\u207a/Fe equilibrium at 298.15 K; illustrative E\u00b0=-0.44 V vs SHE, no complexation or junction potential.",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Single-branch anodic Tafel current",
    "input": {
      "name": "eta",
      "label": "Anodic overpotential",
      "min": 0,
      "max": 0.18,
      "default": 0.07,
      "step": 0.002,
      "unit": "V"
    },
    "expression": "0.5*Math.pow(10,eta/0.12)",
    "result_unit": "\u00b5A/cm\u00b2",
    "assumptions": "Anodic Tafel branch only, exchange-scale 0.5 \u00b5A/cm\u00b2, 0.12 V/decade; excludes reverse, mass transfer and film effects.",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Stern\u2013Geary estimated corrosion current",
    "input": {
      "name": "Rp",
      "label": "Polarization resistance",
      "min": 1000,
      "max": 30000,
      "default": 5000,
      "step": 250,
      "unit": "\u03a9\u00b7cm\u00b2"
    },
    "expression": "26000/Rp",
    "result_unit": "\u00b5A/cm\u00b2",
    "assumptions": "Illustrative coefficient B=26 mV and valid small-signal activation-controlled conditions; Rp excludes uncompensated solution resistance.",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Planar dissolved-oxygen diffusion ceiling",
    "input": {
      "name": "delta",
      "label": "Diffusion-layer thickness",
      "min": 25,
      "max": 500,
      "default": 125,
      "step": 5,
      "unit": "\u00b5m"
    },
    "expression": "4*96485.33212*2e-9*0.25/(delta*1e-6)/10",
    "result_unit": "mA/cm\u00b2",
    "assumptions": "Four-electron oxygen reduction, dissolved oxygen 0.25 mol/m\u00b3, D=2\u00d710\u207b\u2079 m\u00b2/s, planar stagnant film; faradaic ceiling only.",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Localized pit depth from specified factor",
    "input": {
      "name": "pf",
      "label": "Pit depth factor",
      "min": 1,
      "max": 20,
      "default": 5,
      "step": 0.5,
      "unit": "dimensionless"
    },
    "expression": "0.15*pf",
    "result_unit": "mm",
    "assumptions": "Synthetic assumed 0.15 mm average nominal loss and a chosen pit-depth factor; does NOT predict the factor from alloy or chloride.",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Composition-only stainless PREN screening",
    "input": {
      "name": "N",
      "label": "Nitrogen content",
      "min": 0,
      "max": 0.3,
      "default": 0.1,
      "step": 0.01,
      "unit": "wt%"
    },
    "expression": "18+3.3*2+16*N",
    "result_unit": "index",
    "assumptions": "Assumed 18 wt% chromium, 2 wt% molybdenum; empirical composition index limited to certain stainless families and not a life predictor.",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Simple protective-scale growth",
    "input": {
      "name": "t",
      "label": "Isothermal exposure",
      "min": 1,
      "max": 1000,
      "default": 200,
      "step": 1,
      "unit": "hours"
    },
    "expression": "Math.sqrt(0.02*t)",
    "result_unit": "mg/cm\u00b2",
    "assumptions": "Ideal positive parabolic mass-gain law with k\u209a=0.02 (mg/cm\u00b2)\u00b2/h; no spallation, transient oxidation or gas effects.",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Oxide thermal mismatch elastic stress",
    "input": {
      "name": "dT",
      "label": "Temperature change magnitude",
      "min": 10,
      "max": 700,
      "default": 250,
      "step": 10,
      "unit": "K"
    },
    "expression": "0.001*100*3*dT",
    "result_unit": "MPa",
    "assumptions": "Unrelaxed linear-elastic mismatch estimate Eeff=100 GPa, \u0394\u03b1=3 ppm/K, geometry ignored; not an adhesion or failure criterion.",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Illustrative thermal activation multiplier",
    "input": {
      "name": "T",
      "label": "Absolute temperature",
      "min": 600,
      "max": 900,
      "default": 720,
      "step": 5,
      "unit": "K"
    },
    "expression": "Math.exp((80000/8.314462618)*(1/600-1/T))",
    "result_unit": "relative to 600 K",
    "assumptions": "Arrhenius Q=80 kJ/mol relative to 600 K and unchanged mechanism; not validated for cycling, phases or service aging.",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "One-dimensional penetration scale",
    "input": {
      "name": "days",
      "label": "Exposure duration",
      "min": 1,
      "max": 90,
      "default": 20,
      "step": 1,
      "unit": "days"
    },
    "expression": "1e6*Math.sqrt(2*1e-13*days*86400)",
    "result_unit": "\u00b5m",
    "assumptions": "Nominal diffusion length \u221a(2Dt) for D=10\u207b\u00b9\u00b3 m\u00b2/s constant; not an actual chloride threshold or concrete service-life model.",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Hypothetical defect detection probability",
    "input": {
      "name": "n",
      "label": "Independent sampled sites",
      "min": 1,
      "max": 100,
      "default": 25,
      "step": 1,
      "unit": "sites"
    },
    "expression": "100*(1-Math.pow(0.97,n))",
    "result_unit": "%",
    "assumptions": "Each site has independent p=0.03 chance of a perfectly detectable defect; clustering, varying rates and misses excluded.",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Gravimetric corrosion-rate conversion",
    "input": {
      "name": "W",
      "label": "Measured metal mass loss",
      "min": 1,
      "max": 200,
      "default": 40,
      "step": 1,
      "unit": "mg"
    },
    "expression": "87.6*W/(7.85*20*168)",
    "result_unit": "mm/year",
    "assumptions": "Pure density 7.85 g/cm\u00b3, area 20 cm\u00b2, 168 h; consistent cleaned mass loss; general corrosion only.",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Idealized R\u2013C capacitive magnitude",
    "input": {
      "name": "f",
      "label": "Signal frequency",
      "min": 0.1,
      "max": 1000,
      "default": 50,
      "step": 0.1,
      "unit": "Hz"
    },
    "expression": "1/(2*Math.PI*f*0.0001)",
    "result_unit": "\u03a9",
    "assumptions": "Pure capacitor C=100 \u00b5F, sinusoidal linear signal; no pore network, nonideal capacitance or corrosion circuit inference.",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Exposed metal and current demand",
    "input": {
      "name": "f",
      "label": "Coating defect area fraction",
      "min": 0,
      "max": 10,
      "default": 2,
      "step": 0.1,
      "unit": "%"
    },
    "expression": "0.02*f",
    "result_unit": "A",
    "assumptions": "100 m\u00b2 total coated structure, f% uncoated, assumed required 20 mA/m\u00b2 uniformly over exposed area; not a CP design current.",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Uniform wall-thickness margin",
    "input": {
      "name": "y",
      "label": "Additional service duration",
      "min": 0,
      "max": 20,
      "default": 7,
      "step": 0.25,
      "unit": "years"
    },
    "expression": "8-5-0.12*y",
    "result_unit": "mm",
    "assumptions": "Current wall 8 mm, illustrative threshold 5 mm and constant uniformly lost thickness 0.12 mm/year; ignores pits, cracks, wall-map and code requirements.",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Iron Faraday uniform penetration", "input": {"name": "i", "label": "Dissolution current density", "min": 0.1, "max": 30, "default": 5, "step": 0.1, "unit": "µA/cm²"}, "expression": "i*0.01*0.055845/(2*96485.33212*7850)*31557600000", "result_unit": "mm/year", "assumptions": "Pure Fe, Fe→Fe²⁺, density 7850 kg/m³, 100% dissolution efficiency and perfectly uniform attack; not a pit-depth forecast.", "synthetic": true}, {"id": 1, "unit": 1, "title": "Nernst iron-ion potential vs SHE", "input": {"name": "a", "label": "Fe²⁺ activity", "min": 0.0001, "max": 1, "default": 0.01, "step": 0.0001, "unit": "dimensionless"}, "expression": "-0.44+(8.314462618*298.15/(2*96485.33212))*Math.log(a)", "result_unit": "V vs SHE", "assumptions": "Ideal Fe²⁺/Fe equilibrium at 298.15 K; illustrative E°=-0.44 V vs SHE, no complexation or junction potential.", "synthetic": true}, {"id": 2, "unit": 2, "title": "Single-branch anodic Tafel current", "input": {"name": "eta", "label": "Anodic overpotential", "min": 0, "max": 0.18, "default": 0.07, "step": 0.002, "unit": "V"}, "expression": "0.5*Math.pow(10,eta/0.12)", "result_unit": "µA/cm²", "assumptions": "Anodic Tafel branch only, exchange-scale 0.5 µA/cm², 0.12 V/decade; excludes reverse, mass transfer and film effects.", "synthetic": true}, {"id": 3, "unit": 2, "title": "Stern–Geary estimated corrosion current", "input": {"name": "Rp", "label": "Polarization resistance", "min": 1000, "max": 30000, "default": 5000, "step": 250, "unit": "Ω·cm²"}, "expression": "26000/Rp", "result_unit": "µA/cm²", "assumptions": "Illustrative coefficient B=26 mV and valid small-signal activation-controlled conditions; Rp excludes uncompensated solution resistance.", "synthetic": true}, {"id": 4, "unit": 3, "title": "Planar dissolved-oxygen diffusion ceiling", "input": {"name": "delta", "label": "Diffusion-layer thickness", "min": 25, "max": 500, "default": 125, "step": 5, "unit": "µm"}, "expression": "4*96485.33212*2e-9*0.25/(delta*1e-6)/10", "result_unit": "mA/cm²", "assumptions": "Four-electron oxygen reduction, dissolved oxygen 0.25 mol/m³, D=2×10⁻⁹ m²/s, planar stagnant film; faradaic ceiling only.", "synthetic": true}, {"id": 5, "unit": 3, "title": "Localized pit depth from specified factor", "input": {"name": "pf", "label": "Pit depth factor", "min": 1, "max": 20, "default": 5, "step": 0.5, "unit": "dimensionless"}, "expression": "0.15*pf", "result_unit": "mm", "assumptions": "Synthetic assumed 0.15 mm average nominal loss and a chosen pit-depth factor; does NOT predict the factor from alloy or chloride.", "synthetic": true}, {"id": 6, "unit": 4, "title": "Composition-only stainless PREN screening", "input": {"name": "N", "label": "Nitrogen content", "min": 0, "max": 0.3, "default": 0.1, "step": 0.01, "unit": "wt%"}, "expression": "18+3.3*2+16*N", "result_unit": "index", "assumptions": "Assumed 18 wt% chromium, 2 wt% molybdenum; empirical composition index limited to certain stainless families and not a life predictor.", "synthetic": true}, {"id": 7, "unit": 4, "title": "Simple protective-scale growth", "input": {"name": "t", "label": "Isothermal exposure", "min": 1, "max": 1000, "default": 200, "step": 1, "unit": "hours"}, "expression": "Math.sqrt(0.02*t)", "result_unit": "mg/cm²", "assumptions": "Ideal positive parabolic mass-gain law with kₚ=0.02 (mg/cm²)²/h; no spallation, transient oxidation or gas effects.", "synthetic": true}, {"id": 8, "unit": 5, "title": "Oxide thermal mismatch elastic stress", "input": {"name": "dT", "label": "Temperature change magnitude", "min": 10, "max": 700, "default": 250, "step": 10, "unit": "K"}, "expression": "0.001*100*3*dT", "result_unit": "MPa", "assumptions": "Unrelaxed linear-elastic mismatch estimate Eeff=100 GPa, Δα=3 ppm/K, geometry ignored; not an adhesion or failure criterion.", "synthetic": true}, {"id": 9, "unit": 5, "title": "Illustrative thermal activation multiplier", "input": {"name": "T", "label": "Absolute temperature", "min": 600, "max": 900, "default": 720, "step": 5, "unit": "K"}, "expression": "Math.exp((80000/8.314462618)*(1/600-1/T))", "result_unit": "relative to 600 K", "assumptions": "Arrhenius Q=80 kJ/mol relative to 600 K and unchanged mechanism; not validated for cycling, phases or service aging.", "synthetic": true}, {"id": 10, "unit": 6, "title": "One-dimensional penetration scale", "input": {"name": "days", "label": "Exposure duration", "min": 1, "max": 90, "default": 20, "step": 1, "unit": "days"}, "expression": "1e6*Math.sqrt(2*1e-13*days*86400)", "result_unit": "µm", "assumptions": "Nominal diffusion length √(2Dt) for D=10⁻¹³ m²/s constant; not an actual chloride threshold or concrete service-life model.", "synthetic": true}, {"id": 11, "unit": 6, "title": "Hypothetical defect detection probability", "input": {"name": "n", "label": "Independent sampled sites", "min": 1, "max": 100, "default": 25, "step": 1, "unit": "sites"}, "expression": "100*(1-Math.pow(0.97,n))", "result_unit": "%", "assumptions": "Each site has independent p=0.03 chance of a perfectly detectable defect; clustering, varying rates and misses excluded.", "synthetic": true}, {"id": 12, "unit": 7, "title": "Gravimetric corrosion-rate conversion", "input": {"name": "W", "label": "Measured metal mass loss", "min": 1, "max": 200, "default": 40, "step": 1, "unit": "mg"}, "expression": "87.6*W/(7.85*20*168)", "result_unit": "mm/year", "assumptions": "Pure density 7.85 g/cm³, area 20 cm², 168 h; consistent cleaned mass loss; general corrosion only.", "synthetic": true}, {"id": 13, "unit": 7, "title": "Idealized R–C capacitive magnitude", "input": {"name": "f", "label": "Signal frequency", "min": 0.1, "max": 1000, "default": 50, "step": 0.1, "unit": "Hz"}, "expression": "1/(2*Math.PI*f*0.0001)", "result_unit": "Ω", "assumptions": "Pure capacitor C=100 µF, sinusoidal linear signal; no pore network, nonideal capacitance or corrosion circuit inference.", "synthetic": true}, {"id": 14, "unit": 8, "title": "Exposed metal and current demand", "input": {"name": "f", "label": "Coating defect area fraction", "min": 0, "max": 10, "default": 2, "step": 0.1, "unit": "%"}, "expression": "0.02*f", "result_unit": "A", "assumptions": "100 m² total coated structure, f% uncoated, assumed required 20 mA/m² uniformly over exposed area; not a CP design current.", "synthetic": true}, {"id": 15, "unit": 8, "title": "Uniform wall-thickness margin", "input": {"name": "y", "label": "Additional service duration", "min": 0, "max": 20, "default": 7, "step": 0.25, "unit": "years"}, "expression": "8-5-0.12*y", "result_unit": "mm", "assumptions": "Current wall 8 mm, illustrative threshold 5 mm and constant uniformly lost thickness 0.12 mm/year; ignores pits, cracks, wall-map and code requirements.", "synthetic": true}];
function evaluate(id,x){switch(id){
case 0:return x*0.01*0.055845/(2*96485.33212*7850)*31557600000;
case 1:return -0.44+(8.314462618*298.15/(2*96485.33212))*Math.log(x);
case 2:return 0.5*Math.pow(10,x/0.12);
case 3:return 26000/x;
case 4:return 4*96485.33212*2e-9*0.25/(x*1e-6)/10;
case 5:return 0.15*x;
case 6:return 18+3.3*2+16*x;
case 7:return Math.sqrt(0.02*x);
case 8:return 0.001*100*3*x;
case 9:return Math.exp((80000/8.314462618)*(1/600-1/x));
case 10:return 1e6*Math.sqrt(2*1e-13*x*86400);
case 11:return 100*(1-Math.pow(0.97,x));
case 12:return 87.6*x/(7.85*20*168);
case 13:return 1/(2*Math.PI*x*0.0001);
case 14:return 0.02*x;
case 15:return 8-5-0.12*x;
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

