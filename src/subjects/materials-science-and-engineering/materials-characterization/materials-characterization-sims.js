/* Materials Characterization Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Independent-mean standard error",
    "input": {
      "name": "n",
      "label": "Independent specimens",
      "min": 4,
      "max": 100,
      "default": 16,
      "step": 1,
      "unit": "specimens"
    },
    "expression": "8/Math.sqrt(n)",
    "result_unit": "MPa",
    "assumptions": "Illustrative specimen-to-specimen standard deviation 8 MPa; all specimens independent and identically distributed; excludes systematic uncertainty and correlated sampling.",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Linear response and fixed calibration offset",
    "input": {
      "name": "x",
      "label": "True reference level",
      "min": 0,
      "max": 100,
      "default": 50,
      "step": 1,
      "unit": "arb. unit"
    },
    "expression": "1.02*x+1.5",
    "result_unit": "detector units",
    "assumptions": "Ideal detector gain 1.02 and fixed offset 1.5; no noise, saturation, temperature drift or matrix dependence.",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Diffraction-limited optical lateral resolution",
    "input": {
      "name": "lambda_nm",
      "label": "Illumination wavelength",
      "min": 400,
      "max": 750,
      "default": 550,
      "step": 5,
      "unit": "nm"
    },
    "expression": "0.61*lambda_nm/0.8",
    "result_unit": "nm",
    "assumptions": "Idealized incoherent imaging with objective NA=0.8; Rayleigh-type resolution estimate, not camera pixel size or guaranteed feature detection.",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Sampling pixel pitch",
    "input": {
      "name": "W",
      "label": "Image field width",
      "min": 20,
      "max": 200,
      "default": 80,
      "step": 5,
      "unit": "\u00b5m"
    },
    "expression": "1000*W/2048",
    "result_unit": "nm/pixel",
    "assumptions": "2048 image samples along one axis; this gives nominal pixel pitch and does not establish effective physical resolution.",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Bragg interplanar spacing",
    "input": {
      "name": "twoTheta",
      "label": "Scattering angle 2\u03b8",
      "min": 25,
      "max": 90,
      "default": 45,
      "step": 1,
      "unit": "degrees"
    },
    "expression": "1.5406/(2*Math.sin(twoTheta*Math.PI/360))",
    "result_unit": "\u00c5",
    "assumptions": "First-order Bragg relation, Cu K-alpha approximate wavelength 1.5406 \u00c5; ignores zero shift, sample displacement, refraction and multiple wavelengths.",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Scherrer coherent-domain peak width",
    "input": {
      "name": "L",
      "label": "Coherent domain length",
      "min": 10,
      "max": 120,
      "default": 40,
      "step": 2,
      "unit": "nm"
    },
    "expression": "(0.9*0.15406/(L*Math.cos(20*Math.PI/180)))*(180/Math.PI)",
    "result_unit": "degrees of 2\u03b8",
    "assumptions": "K=0.9, wavelength 0.15406 nm, Bragg \u03b8=20\u00b0; width in radians converted to degrees of 2\u03b8; no strain or instrument broadening.",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Surface-photoelectron overlayer attenuation",
    "input": {
      "name": "t",
      "label": "Overlayer thickness",
      "min": 0,
      "max": 15,
      "default": 3,
      "step": 0.25,
      "unit": "nm"
    },
    "expression": "100*Math.exp(-t/(2.5*Math.cos(30*Math.PI/180)))",
    "result_unit": "% remaining signal",
    "assumptions": "Exponential homogeneous overlayer model, effective attenuation length 2.5 nm, emission angle 30\u00b0 from normal; no roughness or elastic-scattering correction.",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Ideal Beer\u2013Lambert absorbance",
    "input": {
      "name": "c",
      "label": "Solute concentration",
      "min": 0,
      "max": 0.1,
      "default": 0.04,
      "step": 0.002,
      "unit": "mol/L"
    },
    "expression": "25*c*1",
    "result_unit": "absorbance",
    "assumptions": "Molar absorption coefficient 25 L mol^-1 cm^-1 and optical path 1 cm; no scattering, chemical equilibria or stray light.",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Programmed DSC sensible heat flow",
    "input": {
      "name": "beta",
      "label": "Heating rate",
      "min": 1,
      "max": 30,
      "default": 10,
      "step": 1,
      "unit": "K/min"
    },
    "expression": "10*1.2*beta/60",
    "result_unit": "mW",
    "assumptions": "Sample mass 10 mg and specific heat 1.2 J/(g K); converted mg/g and mW/W exactly; no latent events or thermal lag.",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Ideal contact hardness by fixed area",
    "input": {
      "name": "P",
      "label": "Peak normal load",
      "min": 0.1,
      "max": 10,
      "default": 3,
      "step": 0.1,
      "unit": "mN"
    },
    "expression": "P*1e-3/(2e-12)/1e9",
    "result_unit": "GPa",
    "assumptions": "Fixed projected contact area 2 \u03bcm\u00b2 and applied load in mN; unrealistic when area grows with load; use only as unit-conversion demonstration.",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Calibrated AFM cantilever force",
    "input": {
      "name": "delta",
      "label": "Cantilever deflection",
      "min": 1,
      "max": 80,
      "default": 30,
      "step": 1,
      "unit": "nm"
    },
    "expression": "2*delta",
    "result_unit": "nN",
    "assumptions": "Linear cantilever stiffness 2 N/m and small deflection; excludes adhesive forces, lateral forces and contact dynamics.",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Tomography nominal voxel pitch",
    "input": {
      "name": "W",
      "label": "Reconstruction field of view",
      "min": 1,
      "max": 30,
      "default": 12,
      "step": 0.5,
      "unit": "mm"
    },
    "expression": "1000*W/1024",
    "result_unit": "\u00b5m/voxel",
    "assumptions": "1024 voxels span given axis; effective feature detection may require several voxels and depends on blur, contrast and segmentation.",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Uniform-bar electrical resistivity",
    "input": {
      "name": "R",
      "label": "Measured bar resistance",
      "min": 0.01,
      "max": 20,
      "default": 5,
      "step": 0.01,
      "unit": "\u03a9"
    },
    "expression": "0.01*R",
    "result_unit": "\u03a9\u00b7cm",
    "assumptions": "Uniform bar with cross section 1 mm\u00b2 and voltage-probe spacing 10 mm, four-probe ideal; no contact mixing, gradients or temperature changes.",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Illustrative Curie magnetic susceptibility",
    "input": {
      "name": "T",
      "label": "Temperature",
      "min": 100,
      "max": 400,
      "default": 300,
      "step": 5,
      "unit": "K"
    },
    "expression": "0.03/T",
    "result_unit": "dimensionless",
    "assumptions": "Ideal weak-field noninteracting paramagnet with SI Curie constant 0.03 K; no magnetic ordering, field saturation or sample holder background.",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Independent quadrature uncertainty",
    "input": {
      "name": "u",
      "label": "Type A standard uncertainty",
      "min": 0.1,
      "max": 5,
      "default": 2,
      "step": 0.1,
      "unit": "units"
    },
    "expression": "Math.sqrt(u*u+4)",
    "result_unit": "units",
    "assumptions": "Second uncertainty component fixed at 2 units; zero covariance assumed; all standard uncertainties refer to the same measurand and unit.",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Probability of at least one detected rare defect",
    "input": {
      "name": "n",
      "label": "Independent specimens",
      "min": 1,
      "max": 100,
      "default": 20,
      "step": 1,
      "unit": "specimens"
    },
    "expression": "100*(1-Math.pow(0.97,n))",
    "result_unit": "%",
    "assumptions": "Each specimen independently has a 3% chance of a perfectly detectable event; ignores clustering, false positives and inspection sensitivity below 100%.",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Independent-mean standard error", "input": {"name": "n", "label": "Independent specimens", "min": 4, "max": 100, "default": 16, "step": 1, "unit": "specimens"}, "expression": "8/Math.sqrt(n)", "result_unit": "MPa", "assumptions": "Illustrative specimen-to-specimen standard deviation 8 MPa; all specimens independent and identically distributed; excludes systematic uncertainty and correlated sampling.", "synthetic": true}, {"id": 1, "unit": 1, "title": "Linear response and fixed calibration offset", "input": {"name": "x", "label": "True reference level", "min": 0, "max": 100, "default": 50, "step": 1, "unit": "arb. unit"}, "expression": "1.02*x+1.5", "result_unit": "detector units", "assumptions": "Ideal detector gain 1.02 and fixed offset 1.5; no noise, saturation, temperature drift or matrix dependence.", "synthetic": true}, {"id": 2, "unit": 2, "title": "Diffraction-limited optical lateral resolution", "input": {"name": "lambda_nm", "label": "Illumination wavelength", "min": 400, "max": 750, "default": 550, "step": 5, "unit": "nm"}, "expression": "0.61*lambda_nm/0.8", "result_unit": "nm", "assumptions": "Idealized incoherent imaging with objective NA=0.8; Rayleigh-type resolution estimate, not camera pixel size or guaranteed feature detection.", "synthetic": true}, {"id": 3, "unit": 2, "title": "Sampling pixel pitch", "input": {"name": "W", "label": "Image field width", "min": 20, "max": 200, "default": 80, "step": 5, "unit": "µm"}, "expression": "1000*W/2048", "result_unit": "nm/pixel", "assumptions": "2048 image samples along one axis; this gives nominal pixel pitch and does not establish effective physical resolution.", "synthetic": true}, {"id": 4, "unit": 3, "title": "Bragg interplanar spacing", "input": {"name": "twoTheta", "label": "Scattering angle 2θ", "min": 25, "max": 90, "default": 45, "step": 1, "unit": "degrees"}, "expression": "1.5406/(2*Math.sin(twoTheta*Math.PI/360))", "result_unit": "Å", "assumptions": "First-order Bragg relation, Cu K-alpha approximate wavelength 1.5406 Å; ignores zero shift, sample displacement, refraction and multiple wavelengths.", "synthetic": true}, {"id": 5, "unit": 3, "title": "Scherrer coherent-domain peak width", "input": {"name": "L", "label": "Coherent domain length", "min": 10, "max": 120, "default": 40, "step": 2, "unit": "nm"}, "expression": "(0.9*0.15406/(L*Math.cos(20*Math.PI/180)))*(180/Math.PI)", "result_unit": "degrees of 2θ", "assumptions": "K=0.9, wavelength 0.15406 nm, Bragg θ=20°; width in radians converted to degrees of 2θ; no strain or instrument broadening.", "synthetic": true}, {"id": 6, "unit": 4, "title": "Surface-photoelectron overlayer attenuation", "input": {"name": "t", "label": "Overlayer thickness", "min": 0, "max": 15, "default": 3, "step": 0.25, "unit": "nm"}, "expression": "100*Math.exp(-t/(2.5*Math.cos(30*Math.PI/180)))", "result_unit": "% remaining signal", "assumptions": "Exponential homogeneous overlayer model, effective attenuation length 2.5 nm, emission angle 30° from normal; no roughness or elastic-scattering correction.", "synthetic": true}, {"id": 7, "unit": 4, "title": "Ideal Beer–Lambert absorbance", "input": {"name": "c", "label": "Solute concentration", "min": 0, "max": 0.1, "default": 0.04, "step": 0.002, "unit": "mol/L"}, "expression": "25*c*1", "result_unit": "absorbance", "assumptions": "Molar absorption coefficient 25 L mol^-1 cm^-1 and optical path 1 cm; no scattering, chemical equilibria or stray light.", "synthetic": true}, {"id": 8, "unit": 5, "title": "Programmed DSC sensible heat flow", "input": {"name": "beta", "label": "Heating rate", "min": 1, "max": 30, "default": 10, "step": 1, "unit": "K/min"}, "expression": "10*1.2*beta/60", "result_unit": "mW", "assumptions": "Sample mass 10 mg and specific heat 1.2 J/(g K); converted mg/g and mW/W exactly; no latent events or thermal lag.", "synthetic": true}, {"id": 9, "unit": 5, "title": "Ideal contact hardness by fixed area", "input": {"name": "P", "label": "Peak normal load", "min": 0.1, "max": 10, "default": 3, "step": 0.1, "unit": "mN"}, "expression": "P*1e-3/(2e-12)/1e9", "result_unit": "GPa", "assumptions": "Fixed projected contact area 2 μm² and applied load in mN; unrealistic when area grows with load; use only as unit-conversion demonstration.", "synthetic": true}, {"id": 10, "unit": 6, "title": "Calibrated AFM cantilever force", "input": {"name": "delta", "label": "Cantilever deflection", "min": 1, "max": 80, "default": 30, "step": 1, "unit": "nm"}, "expression": "2*delta", "result_unit": "nN", "assumptions": "Linear cantilever stiffness 2 N/m and small deflection; excludes adhesive forces, lateral forces and contact dynamics.", "synthetic": true}, {"id": 11, "unit": 6, "title": "Tomography nominal voxel pitch", "input": {"name": "W", "label": "Reconstruction field of view", "min": 1, "max": 30, "default": 12, "step": 0.5, "unit": "mm"}, "expression": "1000*W/1024", "result_unit": "µm/voxel", "assumptions": "1024 voxels span given axis; effective feature detection may require several voxels and depends on blur, contrast and segmentation.", "synthetic": true}, {"id": 12, "unit": 7, "title": "Uniform-bar electrical resistivity", "input": {"name": "R", "label": "Measured bar resistance", "min": 0.01, "max": 20, "default": 5, "step": 0.01, "unit": "Ω"}, "expression": "0.01*R", "result_unit": "Ω·cm", "assumptions": "Uniform bar with cross section 1 mm² and voltage-probe spacing 10 mm, four-probe ideal; no contact mixing, gradients or temperature changes.", "synthetic": true}, {"id": 13, "unit": 7, "title": "Illustrative Curie magnetic susceptibility", "input": {"name": "T", "label": "Temperature", "min": 100, "max": 400, "default": 300, "step": 5, "unit": "K"}, "expression": "0.03/T", "result_unit": "dimensionless", "assumptions": "Ideal weak-field noninteracting paramagnet with SI Curie constant 0.03 K; no magnetic ordering, field saturation or sample holder background.", "synthetic": true}, {"id": 14, "unit": 8, "title": "Independent quadrature uncertainty", "input": {"name": "u", "label": "Type A standard uncertainty", "min": 0.1, "max": 5, "default": 2, "step": 0.1, "unit": "units"}, "expression": "Math.sqrt(u*u+4)", "result_unit": "units", "assumptions": "Second uncertainty component fixed at 2 units; zero covariance assumed; all standard uncertainties refer to the same measurand and unit.", "synthetic": true}, {"id": 15, "unit": 8, "title": "Probability of at least one detected rare defect", "input": {"name": "n", "label": "Independent specimens", "min": 1, "max": 100, "default": 20, "step": 1, "unit": "specimens"}, "expression": "100*(1-Math.pow(0.97,n))", "result_unit": "%", "assumptions": "Each specimen independently has a 3% chance of a perfectly detectable event; ignores clustering, false positives and inspection sensitivity below 100%.", "synthetic": true}];
function evaluate(id,x){switch(id){
case 0:return 8/Math.sqrt(x);
case 1:return 1.02*x+1.5;
case 2:return 0.61*x/0.8;
case 3:return 1000*x/2048;
case 4:return 1.5406/(2*Math.sin(x*Math.PI/360));
case 5:return (0.9*0.15406/(x*Math.cos(20*Math.PI/180)))*(180/Math.PI);
case 6:return 100*Math.exp(-x/(2.5*Math.cos(30*Math.PI/180)));
case 7:return 25*x*1;
case 8:return 10*1.2*x/60;
case 9:return x*1e-3/(2e-12)/1e9;
case 10:return 2*x;
case 11:return 1000*x/1024;
case 12:return 0.01*x;
case 13:return 0.03/x;
case 14:return Math.sqrt(x*x+4);
case 15:return 100*(1-Math.pow(0.97,x));
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

