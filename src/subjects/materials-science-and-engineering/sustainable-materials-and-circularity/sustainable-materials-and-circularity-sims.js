/* Sustainable Materials and Circularity Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Burden per achieved service",
    "input": {
      "name": "n",
      "label": "Achieved uses per product",
      "min": 1,
      "max": 50,
      "default": 12,
      "step": 1,
      "unit": "uses"
    },
    "expression": "150/n+3",
    "result_unit": "kg CO\u2082e/use",
    "assumptions": "Synthetic manufacture 150 kg CO\u2082e/product, fixed use burden 3 kg CO\u2082e/use, no returns or failure effects.",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Material stock under fixed flows",
    "input": {
      "name": "y",
      "label": "Years of steady net accumulation",
      "min": 0,
      "max": 25,
      "default": 10,
      "step": 1,
      "unit": "years"
    },
    "expression": "5000+140*y",
    "result_unit": "tonnes",
    "assumptions": "Start stock 5000 t; inflow 400 t/y; outflow 260 t/y; no nonlinear demand or stock aging.",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Manufacturing plus transport inventory",
    "input": {
      "name": "d",
      "label": "Delivery distance for one tonne",
      "min": 0,
      "max": 1000,
      "default": 250,
      "step": 10,
      "unit": "km"
    },
    "expression": "50+0.08*d",
    "result_unit": "kg CO\u2082e",
    "assumptions": "One-tonne output, 50 kg CO\u2082e base and 0.08 kg CO\u2082e/t-km transportation factor; no route/load complications.",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Attributional burden allocation",
    "input": {
      "name": "p",
      "label": "Co-product allocation share",
      "min": 0,
      "max": 100,
      "default": 35,
      "step": 1,
      "unit": "%"
    },
    "expression": "500*p/100",
    "result_unit": "kg CO\u2082e",
    "assumptions": "Synthetic 500 kg CO\u2082e joint-process burden; shares sum to 100%; allocation is a convention, not a physical observed effect.",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Ideal dilution of scrap impurity",
    "input": {
      "name": "p",
      "label": "Clean-metal blend share",
      "min": 0,
      "max": 100,
      "default": 55,
      "step": 1,
      "unit": "%"
    },
    "expression": "(0.5*(100-p)+0.02*p)/100",
    "result_unit": "wt% Cu",
    "assumptions": "Dirty scrap contains 0.50 wt% copper, clean metal 0.02 wt%; perfect mixing and no elemental loss.",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Qualified remelt output",
    "input": {
      "name": "p",
      "label": "Qualified metal yield",
      "min": 50,
      "max": 100,
      "default": 86,
      "step": 1,
      "unit": "%"
    },
    "expression": "1000*p/100",
    "result_unit": "kg",
    "assumptions": "Exactly 1000 kg of dry incoming metallic feed; quality and mass yield collapsed to one parameter.",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Hypothetical polymer-property retention",
    "input": {
      "name": "n",
      "label": "Reprocessing cycles",
      "min": 0,
      "max": 10,
      "default": 4,
      "step": 1,
      "unit": "cycles"
    },
    "expression": "100*Math.exp(-0.04*n)",
    "result_unit": "% reference strength",
    "assumptions": "Arbitrary exponential demonstration, not a universal polymer degradation law; excludes additives and weathering.",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Recovered compatible polymer",
    "input": {
      "name": "p",
      "label": "Non-target contamination fraction",
      "min": 0,
      "max": 50,
      "default": 15,
      "step": 1,
      "unit": "%"
    },
    "expression": "500*(1-p/100)*0.8",
    "result_unit": "kg",
    "assumptions": "500 kg incoming dry plastic, non-target fraction p%, 80% recovery of compatible portion, constant process efficiency.",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Clinker fraction sensitivity",
    "input": {
      "name": "p",
      "label": "Clinker mass fraction of binder",
      "min": 20,
      "max": 100,
      "default": 65,
      "step": 1,
      "unit": "%"
    },
    "expression": "1000*(0.85*p/100+0.15*(1-p/100))",
    "result_unit": "kg CO\u2082e/tonne binder",
    "assumptions": "1000 kg binder, hypothetical clinker factor 0.85 kg CO\u2082e/kg and substitution factor 0.15; ignores durability changes.",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Refillable container burden per use",
    "input": {
      "name": "n",
      "label": "Successful refill cycles",
      "min": 1,
      "max": 50,
      "default": 15,
      "step": 1,
      "unit": "cycles"
    },
    "expression": "16/n+0.5",
    "result_unit": "kg CO\u2082e/use",
    "assumptions": "Hypothetical bottle manufacture 16 kg CO\u2082e, cleaning+return 0.5 per use; no breakage variability.",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Recovered lithium in sorted battery stream",
    "input": {
      "name": "p",
      "label": "Element recovery yield",
      "min": 20,
      "max": 100,
      "default": 78,
      "step": 1,
      "unit": "%"
    },
    "expression": "60*p/100",
    "result_unit": "kg Li",
    "assumptions": "1000 kg active material at an illustrative fixed 6 mass% lithium; recovery and sorting ideal except variable yield.",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Electronic module qualified reuse",
    "input": {
      "name": "p",
      "label": "Inspection acceptance rate",
      "min": 0,
      "max": 100,
      "default": 40,
      "step": 1,
      "unit": "%"
    },
    "expression": "400*p/100",
    "result_unit": "modules",
    "assumptions": "400 tested modules, uniform module definition, fractional model output represents expected count not an exact integer.",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Heat needed to warm water",
    "input": {
      "name": "dT",
      "label": "Required water temperature increase",
      "min": 5,
      "max": 80,
      "default": 30,
      "step": 1,
      "unit": "K"
    },
    "expression": "1000*4.18*dT/3600",
    "result_unit": "kWh thermal",
    "assumptions": "1000 kg water, heat capacity 4.18 kJ/(kg K), no heat loss or phase change.",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Illustrative water withdrawal",
    "input": {
      "name": "p",
      "label": "Reuse fraction of reducible flow",
      "min": 0,
      "max": 95,
      "default": 60,
      "step": 1,
      "unit": "%"
    },
    "expression": "100*(1-p/100)+10",
    "result_unit": "m\u00b3/day",
    "assumptions": "100 m\u00b3/day reducible demand plus fixed 10 m\u00b3/day makeup; no worsening water quality or treatment losses.",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Return system burden",
    "input": {
      "name": "n",
      "label": "Achieved delivery cycles",
      "min": 1,
      "max": 40,
      "default": 9,
      "step": 1,
      "unit": "cycles"
    },
    "expression": "25/n+1",
    "result_unit": "kg CO\u2082e/delivery",
    "assumptions": "Synthetic container production 25 kg CO\u2082e, 1 kg CO\u2082e each return-and-clean cycle; only achieved cycles counted.",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Five-year cash-flow NPV",
    "input": {
      "name": "c",
      "label": "Net yearly cash flow",
      "min": 0,
      "max": 30000,
      "default": 12000,
      "step": 500,
      "unit": "USD/year"
    },
    "expression": "-40000+c*(1-Math.pow(1.08,-5))/0.08",
    "result_unit": "USD",
    "assumptions": "$40,000 initial investment, five annual end-of-year level net cash flows, fixed nominal discount 8%, no taxes or terminal value.",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Burden per achieved service", "input": {"name": "n", "label": "Achieved uses per product", "min": 1, "max": 50, "default": 12, "step": 1, "unit": "uses"}, "expression": "150/n+3", "result_unit": "kg CO₂e/use", "assumptions": "Synthetic manufacture 150 kg CO₂e/product, fixed use burden 3 kg CO₂e/use, no returns or failure effects.", "synthetic": true}, {"id": 1, "unit": 1, "title": "Material stock under fixed flows", "input": {"name": "y", "label": "Years of steady net accumulation", "min": 0, "max": 25, "default": 10, "step": 1, "unit": "years"}, "expression": "5000+140*y", "result_unit": "tonnes", "assumptions": "Start stock 5000 t; inflow 400 t/y; outflow 260 t/y; no nonlinear demand or stock aging.", "synthetic": true}, {"id": 2, "unit": 2, "title": "Manufacturing plus transport inventory", "input": {"name": "d", "label": "Delivery distance for one tonne", "min": 0, "max": 1000, "default": 250, "step": 10, "unit": "km"}, "expression": "50+0.08*d", "result_unit": "kg CO₂e", "assumptions": "One-tonne output, 50 kg CO₂e base and 0.08 kg CO₂e/t-km transportation factor; no route/load complications.", "synthetic": true}, {"id": 3, "unit": 2, "title": "Attributional burden allocation", "input": {"name": "p", "label": "Co-product allocation share", "min": 0, "max": 100, "default": 35, "step": 1, "unit": "%"}, "expression": "500*p/100", "result_unit": "kg CO₂e", "assumptions": "Synthetic 500 kg CO₂e joint-process burden; shares sum to 100%; allocation is a convention, not a physical observed effect.", "synthetic": true}, {"id": 4, "unit": 3, "title": "Ideal dilution of scrap impurity", "input": {"name": "p", "label": "Clean-metal blend share", "min": 0, "max": 100, "default": 55, "step": 1, "unit": "%"}, "expression": "(0.5*(100-p)+0.02*p)/100", "result_unit": "wt% Cu", "assumptions": "Dirty scrap contains 0.50 wt% copper, clean metal 0.02 wt%; perfect mixing and no elemental loss.", "synthetic": true}, {"id": 5, "unit": 3, "title": "Qualified remelt output", "input": {"name": "p", "label": "Qualified metal yield", "min": 50, "max": 100, "default": 86, "step": 1, "unit": "%"}, "expression": "1000*p/100", "result_unit": "kg", "assumptions": "Exactly 1000 kg of dry incoming metallic feed; quality and mass yield collapsed to one parameter.", "synthetic": true}, {"id": 6, "unit": 4, "title": "Hypothetical polymer-property retention", "input": {"name": "n", "label": "Reprocessing cycles", "min": 0, "max": 10, "default": 4, "step": 1, "unit": "cycles"}, "expression": "100*Math.exp(-0.04*n)", "result_unit": "% reference strength", "assumptions": "Arbitrary exponential demonstration, not a universal polymer degradation law; excludes additives and weathering.", "synthetic": true}, {"id": 7, "unit": 4, "title": "Recovered compatible polymer", "input": {"name": "p", "label": "Non-target contamination fraction", "min": 0, "max": 50, "default": 15, "step": 1, "unit": "%"}, "expression": "500*(1-p/100)*0.8", "result_unit": "kg", "assumptions": "500 kg incoming dry plastic, non-target fraction p%, 80% recovery of compatible portion, constant process efficiency.", "synthetic": true}, {"id": 8, "unit": 5, "title": "Clinker fraction sensitivity", "input": {"name": "p", "label": "Clinker mass fraction of binder", "min": 20, "max": 100, "default": 65, "step": 1, "unit": "%"}, "expression": "1000*(0.85*p/100+0.15*(1-p/100))", "result_unit": "kg CO₂e/tonne binder", "assumptions": "1000 kg binder, hypothetical clinker factor 0.85 kg CO₂e/kg and substitution factor 0.15; ignores durability changes.", "synthetic": true}, {"id": 9, "unit": 5, "title": "Refillable container burden per use", "input": {"name": "n", "label": "Successful refill cycles", "min": 1, "max": 50, "default": 15, "step": 1, "unit": "cycles"}, "expression": "16/n+0.5", "result_unit": "kg CO₂e/use", "assumptions": "Hypothetical bottle manufacture 16 kg CO₂e, cleaning+return 0.5 per use; no breakage variability.", "synthetic": true}, {"id": 10, "unit": 6, "title": "Recovered lithium in sorted battery stream", "input": {"name": "p", "label": "Element recovery yield", "min": 20, "max": 100, "default": 78, "step": 1, "unit": "%"}, "expression": "60*p/100", "result_unit": "kg Li", "assumptions": "1000 kg active material at an illustrative fixed 6 mass% lithium; recovery and sorting ideal except variable yield.", "synthetic": true}, {"id": 11, "unit": 6, "title": "Electronic module qualified reuse", "input": {"name": "p", "label": "Inspection acceptance rate", "min": 0, "max": 100, "default": 40, "step": 1, "unit": "%"}, "expression": "400*p/100", "result_unit": "modules", "assumptions": "400 tested modules, uniform module definition, fractional model output represents expected count not an exact integer.", "synthetic": true}, {"id": 12, "unit": 7, "title": "Heat needed to warm water", "input": {"name": "dT", "label": "Required water temperature increase", "min": 5, "max": 80, "default": 30, "step": 1, "unit": "K"}, "expression": "1000*4.18*dT/3600", "result_unit": "kWh thermal", "assumptions": "1000 kg water, heat capacity 4.18 kJ/(kg K), no heat loss or phase change.", "synthetic": true}, {"id": 13, "unit": 7, "title": "Illustrative water withdrawal", "input": {"name": "p", "label": "Reuse fraction of reducible flow", "min": 0, "max": 95, "default": 60, "step": 1, "unit": "%"}, "expression": "100*(1-p/100)+10", "result_unit": "m³/day", "assumptions": "100 m³/day reducible demand plus fixed 10 m³/day makeup; no worsening water quality or treatment losses.", "synthetic": true}, {"id": 14, "unit": 8, "title": "Return system burden", "input": {"name": "n", "label": "Achieved delivery cycles", "min": 1, "max": 40, "default": 9, "step": 1, "unit": "cycles"}, "expression": "25/n+1", "result_unit": "kg CO₂e/delivery", "assumptions": "Synthetic container production 25 kg CO₂e, 1 kg CO₂e each return-and-clean cycle; only achieved cycles counted.", "synthetic": true}, {"id": 15, "unit": 8, "title": "Five-year cash-flow NPV", "input": {"name": "c", "label": "Net yearly cash flow", "min": 0, "max": 30000, "default": 12000, "step": 500, "unit": "USD/year"}, "expression": "-40000+c*(1-Math.pow(1.08,-5))/0.08", "result_unit": "USD", "assumptions": "$40,000 initial investment, five annual end-of-year level net cash flows, fixed nominal discount 8%, no taxes or terminal value.", "synthetic": true}];
function evaluate(id,x){switch(id){
case 0:return 150/x+3;
case 1:return 5000+140*x;
case 2:return 50+0.08*x;
case 3:return 500*x/100;
case 4:return (0.5*(100-x)+0.02*x)/100;
case 5:return 1000*x/100;
case 6:return 100*Math.exp(-0.04*x);
case 7:return 500*(1-x/100)*0.8;
case 8:return 1000*(0.85*x/100+0.15*(1-x/100));
case 9:return 16/x+0.5;
case 10:return 60*x/100;
case 11:return 400*x/100;
case 12:return 1000*4.18*x/3600;
case 13:return 100*(1-x/100)+10;
case 14:return 25/x+1;
case 15:return -40000+x*(1-Math.pow(1.08,-5))/0.08;
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

