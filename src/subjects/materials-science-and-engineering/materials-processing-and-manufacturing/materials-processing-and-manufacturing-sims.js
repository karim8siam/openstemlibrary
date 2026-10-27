/* Materials Processing and Manufacturing Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Ideal cycle-time capacity",
    "input": {
      "name": "c",
      "label": "Cycle time per part",
      "min": 10,
      "max": 180,
      "default": 60,
      "step": 1,
      "unit": "s/part"
    },
    "expression": "3600/c",
    "result_unit": "parts/h",
    "assumptions": "Continuous ideal operation, one part per cycle, no changeover, downtime or parallel stations; throughput must not be rounded up for actual orders.",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Qualified-part variable cost",
    "input": {
      "name": "p",
      "label": "First-pass yield",
      "min": 50,
      "max": 100,
      "default": 85,
      "step": 1,
      "unit": "%"
    },
    "expression": "(12000+2000)/(1000*p/100)",
    "result_unit": "USD/qualified part",
    "assumptions": "A hypothetical batch incurs USD 12,000 variable and USD 2,000 setup cost for 1000 attempted units; rejects have no salvage and all fixed costs are assigned to passing units.",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Chvorinov ideal solidification time",
    "input": {
      "name": "m",
      "label": "Casting volume-to-area ratio",
      "min": 0.5,
      "max": 4,
      "default": 2,
      "step": 0.1,
      "unit": "cm"
    },
    "expression": "4*m*m",
    "result_unit": "min",
    "assumptions": "Chvorinov scaling with a hypothetical mold constant of 4 min/cm\u00b2; geometry, superheat, interfacial heat transfer and material family otherwise held constant.",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Liquid-to-solid volume shrinkage",
    "input": {
      "name": "s",
      "label": "Volumetric solidification shrinkage",
      "min": 1,
      "max": 12,
      "default": 6,
      "step": 0.5,
      "unit": "%"
    },
    "expression": "1000*s/100",
    "result_unit": "cm\u00b3",
    "assumptions": "A hypothetical 1000 cm\u00b3 liquid casting; shrinkage here is volumetric and excludes liquid cooling, feeding, porosity and constrained distortion.",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "True strain under uniaxial extension",
    "input": {
      "name": "L",
      "label": "Final gauge length",
      "min": 55,
      "max": 120,
      "default": 80,
      "step": 1,
      "unit": "mm"
    },
    "expression": "Math.log(L/50)",
    "result_unit": "dimensionless",
    "assumptions": "Initial gauge length 50 mm; homogeneous uniaxial deformation with length measured consistently; necking makes uniform strain inference invalid.",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Illustrative rolling separating force",
    "input": {
      "name": "k",
      "label": "Mean flow stress",
      "min": 80,
      "max": 400,
      "default": 180,
      "step": 10,
      "unit": "MPa"
    },
    "expression": "0.25*0.04*k*1000000",
    "result_unit": "N",
    "assumptions": "Constant contact length 0.04 m and width 0.25 m, mean pressure equal to flow stress, no friction/redundant work correction; not a mill setup calculation.",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Ideal turning cutting speed",
    "input": {
      "name": "N",
      "label": "Spindle speed",
      "min": 200,
      "max": 2400,
      "default": 900,
      "step": 20,
      "unit": "rev/min"
    },
    "expression": "Math.PI*60*N/1000",
    "result_unit": "m/min",
    "assumptions": "Fixed 60 mm workpiece diameter, no speed reduction with tool engagement or changes in surface diameter.",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Ideal milling metal-removal rate",
    "input": {
      "name": "f",
      "label": "Feed rate",
      "min": 50,
      "max": 700,
      "default": 300,
      "step": 10,
      "unit": "mm/min"
    },
    "expression": "8*2*f/1000",
    "result_unit": "cm\u00b3/min",
    "assumptions": "Width of cut 8 mm and depth 2 mm; constant engagement, uniform material removal and no acceleration or chip evacuation losses.",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Powder-bed layer-count estimate",
    "input": {
      "name": "t",
      "label": "Nominal layer thickness",
      "min": 0.02,
      "max": 0.12,
      "default": 0.05,
      "step": 0.01,
      "unit": "mm"
    },
    "expression": "Math.ceil(20/t)",
    "result_unit": "layers",
    "assumptions": "Fixed 20 mm build height, ideal slicing, no recoater gaps, adaptive layers, contour differences or dimensional compensation.",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Powder-based feed for qualified part",
    "input": {
      "name": "p",
      "label": "Material utilization fraction",
      "min": 20,
      "max": 95,
      "default": 65,
      "step": 1,
      "unit": "%"
    },
    "expression": "500/(p/100)",
    "result_unit": "g feed",
    "assumptions": "A 500 g delivered part and one lumped utilization factor; ignores chemistry drift, contamination, non-recyclable support, powder ageing and transport.",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Extrusion mass throughput",
    "input": {
      "name": "v",
      "label": "Take-off speed",
      "min": 0.5,
      "max": 8,
      "default": 3,
      "step": 0.1,
      "unit": "m/min"
    },
    "expression": "0.0005*v*60*1000",
    "result_unit": "kg/h",
    "assumptions": "Uniform melt density 1000 kg/m\u00b3 and nominal constant cross section 0.0005 m\u00b2; neglects die swell, drawdown, voids and density changes.",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Ideal isotropic sintering shrinkage",
    "input": {
      "name": "p",
      "label": "Final relative density",
      "min": 60,
      "max": 99,
      "default": 90,
      "step": 1,
      "unit": "%"
    },
    "expression": "100*(1-Math.pow(0.55/(p/100),1/3))",
    "result_unit": "% linear shrinkage",
    "assumptions": "Initial relative density 55%, constant solid mass, isotropic uniform densification; real grain growth, differential sintering and restraint can make shrinkage nonuniform.",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Illustrative weld line energy",
    "input": {
      "name": "v",
      "label": "Travel speed",
      "min": 1,
      "max": 20,
      "default": 5,
      "step": 0.5,
      "unit": "mm/s"
    },
    "expression": "0.75*20*150/v",
    "result_unit": "J/mm",
    "assumptions": "Fixed 20 V, 150 A and thermal efficiency 0.75, steady bead; not a qualified weld procedure or a prediction of fusion, microstructure or distortion.",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Ideal diffusion distance",
    "input": {
      "name": "t",
      "label": "Hold duration",
      "min": 1,
      "max": 240,
      "default": 60,
      "step": 1,
      "unit": "min"
    },
    "expression": "Math.sqrt(2*1e-11*t*60)*1000000",
    "result_unit": "\u00b5m",
    "assumptions": "One-dimensional characteristic sqrt(2Dt), D=1e\u221211 m\u00b2/s fixed; real D is strongly temperature- and composition-dependent, boundary conditions and phase effects omitted.",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Cp under fixed specification width",
    "input": {
      "name": "s",
      "label": "Observed within-subgroup sigma",
      "min": 0.01,
      "max": 0.1,
      "default": 0.04,
      "step": 0.005,
      "unit": "mm"
    },
    "expression": "0.30/(6*s)",
    "result_unit": "Cp",
    "assumptions": "Fixed total specification tolerance 0.30 mm; sigma stable and estimated by valid rational subgroup method; Cp does not describe process centering or final defect rate.",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Good-unit cost after reject loss",
    "input": {
      "name": "p",
      "label": "First-pass yield",
      "min": 50,
      "max": 100,
      "default": 92,
      "step": 1,
      "unit": "%"
    },
    "expression": "(1000*12+2000)/(1000*p/100)",
    "result_unit": "USD/accepted part",
    "assumptions": "One invented lot of 1000 attempted parts, USD 12 variable cost each, USD 2000 setup, rejects have zero salvage; no inventory or rework effects.",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Ideal cycle-time capacity", "input": {"name": "c", "label": "Cycle time per part", "min": 10, "max": 180, "default": 60, "step": 1, "unit": "s/part"}, "expression": "3600/c", "result_unit": "parts/h", "assumptions": "Continuous ideal operation, one part per cycle, no changeover, downtime or parallel stations; throughput must not be rounded up for actual orders.", "synthetic": true}, {"id": 1, "unit": 1, "title": "Qualified-part variable cost", "input": {"name": "p", "label": "First-pass yield", "min": 50, "max": 100, "default": 85, "step": 1, "unit": "%"}, "expression": "(12000+2000)/(1000*p/100)", "result_unit": "USD/qualified part", "assumptions": "A hypothetical batch incurs USD 12,000 variable and USD 2,000 setup cost for 1000 attempted units; rejects have no salvage and all fixed costs are assigned to passing units.", "synthetic": true}, {"id": 2, "unit": 2, "title": "Chvorinov ideal solidification time", "input": {"name": "m", "label": "Casting volume-to-area ratio", "min": 0.5, "max": 4, "default": 2, "step": 0.1, "unit": "cm"}, "expression": "4*m*m", "result_unit": "min", "assumptions": "Chvorinov scaling with a hypothetical mold constant of 4 min/cm²; geometry, superheat, interfacial heat transfer and material family otherwise held constant.", "synthetic": true}, {"id": 3, "unit": 2, "title": "Liquid-to-solid volume shrinkage", "input": {"name": "s", "label": "Volumetric solidification shrinkage", "min": 1, "max": 12, "default": 6, "step": 0.5, "unit": "%"}, "expression": "1000*s/100", "result_unit": "cm³", "assumptions": "A hypothetical 1000 cm³ liquid casting; shrinkage here is volumetric and excludes liquid cooling, feeding, porosity and constrained distortion.", "synthetic": true}, {"id": 4, "unit": 3, "title": "True strain under uniaxial extension", "input": {"name": "L", "label": "Final gauge length", "min": 55, "max": 120, "default": 80, "step": 1, "unit": "mm"}, "expression": "Math.log(L/50)", "result_unit": "dimensionless", "assumptions": "Initial gauge length 50 mm; homogeneous uniaxial deformation with length measured consistently; necking makes uniform strain inference invalid.", "synthetic": true}, {"id": 5, "unit": 3, "title": "Illustrative rolling separating force", "input": {"name": "k", "label": "Mean flow stress", "min": 80, "max": 400, "default": 180, "step": 10, "unit": "MPa"}, "expression": "0.25*0.04*k*1000000", "result_unit": "N", "assumptions": "Constant contact length 0.04 m and width 0.25 m, mean pressure equal to flow stress, no friction/redundant work correction; not a mill setup calculation.", "synthetic": true}, {"id": 6, "unit": 4, "title": "Ideal turning cutting speed", "input": {"name": "N", "label": "Spindle speed", "min": 200, "max": 2400, "default": 900, "step": 20, "unit": "rev/min"}, "expression": "Math.PI*60*N/1000", "result_unit": "m/min", "assumptions": "Fixed 60 mm workpiece diameter, no speed reduction with tool engagement or changes in surface diameter.", "synthetic": true}, {"id": 7, "unit": 4, "title": "Ideal milling metal-removal rate", "input": {"name": "f", "label": "Feed rate", "min": 50, "max": 700, "default": 300, "step": 10, "unit": "mm/min"}, "expression": "8*2*f/1000", "result_unit": "cm³/min", "assumptions": "Width of cut 8 mm and depth 2 mm; constant engagement, uniform material removal and no acceleration or chip evacuation losses.", "synthetic": true}, {"id": 8, "unit": 5, "title": "Powder-bed layer-count estimate", "input": {"name": "t", "label": "Nominal layer thickness", "min": 0.02, "max": 0.12, "default": 0.05, "step": 0.01, "unit": "mm"}, "expression": "Math.ceil(20/t)", "result_unit": "layers", "assumptions": "Fixed 20 mm build height, ideal slicing, no recoater gaps, adaptive layers, contour differences or dimensional compensation.", "synthetic": true}, {"id": 9, "unit": 5, "title": "Powder-based feed for qualified part", "input": {"name": "p", "label": "Material utilization fraction", "min": 20, "max": 95, "default": 65, "step": 1, "unit": "%"}, "expression": "500/(p/100)", "result_unit": "g feed", "assumptions": "A 500 g delivered part and one lumped utilization factor; ignores chemistry drift, contamination, non-recyclable support, powder ageing and transport.", "synthetic": true}, {"id": 10, "unit": 6, "title": "Extrusion mass throughput", "input": {"name": "v", "label": "Take-off speed", "min": 0.5, "max": 8, "default": 3, "step": 0.1, "unit": "m/min"}, "expression": "0.0005*v*60*1000", "result_unit": "kg/h", "assumptions": "Uniform melt density 1000 kg/m³ and nominal constant cross section 0.0005 m²; neglects die swell, drawdown, voids and density changes.", "synthetic": true}, {"id": 11, "unit": 6, "title": "Ideal isotropic sintering shrinkage", "input": {"name": "p", "label": "Final relative density", "min": 60, "max": 99, "default": 90, "step": 1, "unit": "%"}, "expression": "100*(1-Math.pow(0.55/(p/100),1/3))", "result_unit": "% linear shrinkage", "assumptions": "Initial relative density 55%, constant solid mass, isotropic uniform densification; real grain growth, differential sintering and restraint can make shrinkage nonuniform.", "synthetic": true}, {"id": 12, "unit": 7, "title": "Illustrative weld line energy", "input": {"name": "v", "label": "Travel speed", "min": 1, "max": 20, "default": 5, "step": 0.5, "unit": "mm/s"}, "expression": "0.75*20*150/v", "result_unit": "J/mm", "assumptions": "Fixed 20 V, 150 A and thermal efficiency 0.75, steady bead; not a qualified weld procedure or a prediction of fusion, microstructure or distortion.", "synthetic": true}, {"id": 13, "unit": 7, "title": "Ideal diffusion distance", "input": {"name": "t", "label": "Hold duration", "min": 1, "max": 240, "default": 60, "step": 1, "unit": "min"}, "expression": "Math.sqrt(2*1e-11*t*60)*1000000", "result_unit": "µm", "assumptions": "One-dimensional characteristic sqrt(2Dt), D=1e−11 m²/s fixed; real D is strongly temperature- and composition-dependent, boundary conditions and phase effects omitted.", "synthetic": true}, {"id": 14, "unit": 8, "title": "Cp under fixed specification width", "input": {"name": "s", "label": "Observed within-subgroup sigma", "min": 0.01, "max": 0.1, "default": 0.04, "step": 0.005, "unit": "mm"}, "expression": "0.30/(6*s)", "result_unit": "Cp", "assumptions": "Fixed total specification tolerance 0.30 mm; sigma stable and estimated by valid rational subgroup method; Cp does not describe process centering or final defect rate.", "synthetic": true}, {"id": 15, "unit": 8, "title": "Good-unit cost after reject loss", "input": {"name": "p", "label": "First-pass yield", "min": 50, "max": 100, "default": 92, "step": 1, "unit": "%"}, "expression": "(1000*12+2000)/(1000*p/100)", "result_unit": "USD/accepted part", "assumptions": "One invented lot of 1000 attempted parts, USD 12 variable cost each, USD 2000 setup, rejects have zero salvage; no inventory or rework effects.", "synthetic": true}];
function evaluate(id,x){switch(id){
case 0:return 3600/x;
case 1:return (12000+2000)/(1000*x/100);
case 2:return 4*x*x;
case 3:return 1000*x/100;
case 4:return Math.log(x/50);
case 5:return 0.25*0.04*x*1000000;
case 6:return Math.PI*60*x/1000;
case 7:return 8*2*x/1000;
case 8:return Math.ceil(20/x);
case 9:return 500/(x/100);
case 10:return 0.0005*x*60*1000;
case 11:return 100*(1-Math.pow(0.55/(x/100),1/3));
case 12:return 0.75*20*150/x;
case 13:return Math.sqrt(2*1e-11*x*60)*1000000;
case 14:return 0.30/(6*x);
case 15:return (1000*12+2000)/(1000*x/100);
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

