/* Biotechnology Interactive Simulation Suite */
"use strict";
// All math below is a fictional educational model; no laboratory or clinical deployment.
const modelFormulas={
 recovery:x=>x, qpcr:x=>Math.pow(1.9,x), identity:x=>x, delivery:x=>x,
 hill:x=>100*x*x/(900+x*x), burden:x=>x*Math.exp(-x/45),
 growth:x=>Math.exp(.35*x), recovery2:x=>.85*x,
 mm:x=>120*x/(30+x), binding:x=>100*x/(25+x),
 crop:x=>1200*x/100-90, decay:x=>100*Math.exp(-.1*x),
 ppv:x=>100*(.9*x/1000)/(.9*x/1000+.05*(1-x/1000)),
 risk:x=>12-x, breakeven:x=>Math.ceil(x*1000/7), capability:x=>10/(3*x)
};
function computeModel(kind,x){if(!Object.prototype.hasOwnProperty.call(modelFormulas,kind))throw Error('Unrecognized model');return modelFormulas[kind](Number(x));}
function numberFmt(y){return !Number.isFinite(y)?'Undefined':Math.abs(y)>0&&Math.abs(y)<0.001?y.toExponential(3):Number(y.toPrecision(5)).toString()}
function makeGraph(kind,lo,hi,current){const N=80;let samples=[];for(let i=0;i<=N;i++){let x=lo+(hi-lo)*i/N;samples.push(computeModel(kind,x))};let mn=Math.min(...samples),mx=Math.max(...samples);if(mx==mn)mx=mn+1;let points=samples.map((y,i)=>`${(18+460*i/N).toFixed(1)},${(154-120*(y-mn)/(mx-mn)).toFixed(1)}`).join(' ');let cy=154-120*(computeModel(kind,current)-mn)/(mx-mn);let cx=18+460*(current-lo)/(hi-lo);return `<svg viewBox="0 0 500 174" role="img" aria-label="Model output curve with marker at current slider value"><line x1="18" y1="154" x2="478" y2="154" stroke="#afc9d4" stroke-width="2"/><polyline points="${points}" fill="none" stroke="#12617a" stroke-width="3"/><circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="6" fill="#e08325" stroke="#fff" stroke-width="2"/><text x="18" y="170" font-size="11">${lo}</text><text x="478" y="170" text-anchor="end" font-size="11">${hi}</text></svg>`}
function setupModels(){document.querySelectorAll('section.model[data-kind]').forEach(card=>{const kind=card.dataset.kind;if(!modelFormulas[kind])return;const slider=card.querySelector('input'),out=card.querySelector('output'),graph=card.querySelector('.viz');const min=Number(slider.min),max=Number(slider.max);function update(){const x=Number(slider.value),y=computeModel(kind,x);out.textContent=`Input ${numberFmt(x)} → ${numberFmt(y)} ${card.dataset.units}`;graph.innerHTML=makeGraph(kind,min,max,x);}slider.addEventListener('input',update);update();})}
if(typeof document!=='undefined'){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',setupModels);else setupModels();}
if(typeof module!=='undefined')module.exports={computeModel,modelFormulas};


window.BIOTECH_MODELS = [
  {
    "id": "recovery",
    "unit": 1,
    "title": "Sample recovery estimate",
    "label": "Recovered samples out of 100",
    "kind": "recovery",
    "min": 0,
    "max": 100,
    "initial": 70,
    "step": 1,
    "resultUnits": "% recovered",
    "formula": "100 \u00d7 recovered / 100",
    "limitation": "Only counts laboratory records in a synthetic example"
  },
  {
    "id": "qpcr",
    "unit": 1,
    "title": "Idealized amplification multiplier",
    "label": "Amplification cycle count",
    "kind": "qpcr",
    "min": 0,
    "max": 20,
    "initial": 8,
    "step": 1,
    "resultUnits": "fold",
    "formula": "1.9^cycle count",
    "limitation": "Assumes fixed 90% efficiency; MIQE 2.0 details real validation"
  },
  {
    "id": "identity",
    "unit": 2,
    "title": "Sequence-block agreement",
    "label": "Matching blocks among 100",
    "kind": "identity",
    "min": 0,
    "max": 100,
    "initial": 88,
    "step": 1,
    "resultUnits": "% agreement",
    "formula": "100 \u00d7 matches / 100",
    "limitation": "Agreement does not imply functional equivalence"
  },
  {
    "id": "delivery",
    "unit": 2,
    "title": "Functional delivery among uptake-positive cells",
    "label": "Function-positive among 100 uptake-positive cells",
    "kind": "delivery",
    "min": 0,
    "max": 100,
    "initial": 37,
    "step": 1,
    "resultUnits": "% function-positive",
    "formula": "100 \u00d7 function-positive / 100",
    "limitation": "Assumes measurement-specific denominators"
  },
  {
    "id": "hill",
    "unit": 3,
    "title": "Idealized Hill response",
    "label": "Input (arbitrary units)",
    "kind": "hill",
    "min": 0,
    "max": 100,
    "initial": 25,
    "step": 1,
    "resultUnits": "% maximal response",
    "formula": "100 \u00d7 x\u00b2 / (30\u00b2 + x\u00b2)",
    "limitation": "Not evidence that molecular interactions are cooperative"
  },
  {
    "id": "burden",
    "unit": 3,
    "title": "Toy resource burden curve",
    "label": "Expression drive (relative 0\u2013100)",
    "kind": "burden",
    "min": 0,
    "max": 100,
    "initial": 50,
    "step": 1,
    "resultUnits": "relative output",
    "formula": "x \u00d7 exp(\u2212x/45)",
    "limitation": "Demonstrates potential trade-off, not a universal cell model"
  },
  {
    "id": "growth",
    "unit": 4,
    "title": "Exponential growth multiplier",
    "label": "Hours elapsed",
    "kind": "growth",
    "min": 0,
    "max": 12,
    "initial": 5,
    "step": 0.5,
    "resultUnits": "fold",
    "formula": "exp(0.35 \u00d7 t)",
    "limitation": "Assumes uninterrupted exponential phase"
  },
  {
    "id": "recovery2",
    "unit": 4,
    "title": "Two-stage recovered material",
    "label": "Second-stage recovery percentage",
    "kind": "recovery2",
    "min": 10,
    "max": 100,
    "initial": 75,
    "step": 1,
    "resultUnits": "% total recovery",
    "formula": "0.85 \u00d7 stage2 recovery (%)",
    "limitation": "First stage fixed at 85%"
  },
  {
    "id": "mm",
    "unit": 5,
    "title": "Michaelis\u2013Menten rate",
    "label": "Substrate concentration units",
    "kind": "mm",
    "min": 0,
    "max": 100,
    "initial": 30,
    "step": 1,
    "resultUnits": "rate units",
    "formula": "120 \u00d7 S/(30 + S)",
    "limitation": "Idealized initial rate without inhibition"
  },
  {
    "id": "binding",
    "unit": 5,
    "title": "One-site occupancy",
    "label": "Ligand concentration units",
    "kind": "binding",
    "min": 0,
    "max": 100,
    "initial": 35,
    "step": 1,
    "resultUnits": "% bound",
    "formula": "100 \u00d7 L/(25 + L)",
    "limitation": "Equilibrium one-site approximation only"
  },
  {
    "id": "crop",
    "unit": 6,
    "title": "Crop margin under a yield premium",
    "label": "Gross yield gain in percent",
    "kind": "crop",
    "min": -20,
    "max": 40,
    "initial": 12,
    "step": 1,
    "resultUnits": "USD/ha net incremental margin",
    "formula": "1200\u00d7gain/100 \u2212 90",
    "limitation": "Prices and costs are invented and held fixed"
  },
  {
    "id": "decay",
    "unit": 6,
    "title": "Illustrative residual pollutant fraction",
    "label": "Days elapsed",
    "kind": "decay",
    "min": 0,
    "max": 30,
    "initial": 10,
    "step": 0.5,
    "resultUnits": "% remaining",
    "formula": "100\u00d7exp(\u22120.1\u00d7days)",
    "limitation": "Not a claim about any real pollutant or ecosystem"
  },
  {
    "id": "ppv",
    "unit": 7,
    "title": "Positive predictive value under Bayes rule",
    "label": "Prevalence out of 1000",
    "kind": "ppv",
    "min": 1,
    "max": 100,
    "initial": 10,
    "step": 1,
    "resultUnits": "% PPV",
    "formula": "100\u00d7[0.90 p/(0.90p+0.05(1\u2212p))]",
    "limitation": "Toy specificity 95%, sensitivity 90%; never medical guidance"
  },
  {
    "id": "risk",
    "unit": 7,
    "title": "Toy absolute risk reduction",
    "label": "Event count in treated group of 100",
    "kind": "risk",
    "min": 0,
    "max": 20,
    "initial": 8,
    "step": 1,
    "resultUnits": "percentage points",
    "formula": "12 \u2212 treated event count",
    "limitation": "Assumes 12 events/100 in fictional comparison group"
  },
  {
    "id": "breakeven",
    "unit": 8,
    "title": "Simple break-even units",
    "label": "Fixed cost in thousands of USD",
    "kind": "breakeven",
    "min": 1,
    "max": 100,
    "initial": 24,
    "step": 1,
    "resultUnits": "units",
    "formula": "ceil(fixed USD / 7 USD contribution)",
    "limitation": "Assumes a saleable unit margin of 7 USD"
  },
  {
    "id": "capability",
    "unit": 8,
    "title": "Simplified upper-side process capability",
    "label": "Standard deviation of process metric",
    "kind": "capability",
    "min": 1,
    "max": 10,
    "initial": 4,
    "step": 0.5,
    "resultUnits": "Cpk upper term",
    "formula": "(110\u2212100)/(3\u03c3)",
    "limitation": "Only one side of capability; no distribution validation"
  }
];


/* SimulationEngine adapter for Biotechnology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof computeModel !== 'function' || typeof makeGraph !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var models = window.BIOTECH_MODELS || [];
    var m = models.filter(function(x){ return x.unit === u; })[0] || models[0];
    if (m) {
      var card = document.createElement('section');
      card.className = 'sim-card model';
      card.dataset.kind = m.kind;
      card.dataset.units = m.resultUnits || '';
      card.innerHTML = '<h4>' + m.title + '</h4>' +
        '<p class="formula"><code>' + m.formula + '</code></p>' +
        '<label>' + m.label + ':<br><input type="range" min="' + m.min + '" max="' + m.max + '" step="' + m.step + '" value="' + m.initial + '"></label>' +
        '<output style="display:block;margin:0.5rem 0;font-weight:600;color:#38bdf8;"></output>' +
        '<div class="viz"></div>' +
        '<p class="readout">' + (m.limitation || '') + '</p>';
      host.appendChild(card);
      var slider = card.querySelector('input');
      var out = card.querySelector('output');
      var graph = card.querySelector('.viz');
      var min = Number(slider.min), max = Number(slider.max);
      function update() {
        var x = Number(slider.value), y = computeModel(m.kind, x);
        out.textContent = 'Input ' + numberFmt(x) + ' → ' + numberFmt(y) + ' ' + (m.resultUnits || '');
        graph.innerHTML = makeGraph(m.kind, min, max, x);
      }
      slider.addEventListener('input', update);
      update();
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

