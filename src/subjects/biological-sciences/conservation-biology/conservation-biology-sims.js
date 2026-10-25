/* Conservation Biology Interactive Simulation Suite */
(function(){"use strict";
function compute(kind,x){const exp=Math.exp;
switch(kind){case"area":return 4.5*Math.pow(x,.27);case"decline":return 100*Math.pow(.93,x);case"logistic":return 300/(1+4*exp(-.30*x));case"drift":return 100*Math.pow(1-1/80,x);case"connectivity":return 100*exp(-x/8);case"interior":return 100*Math.pow(Math.max(0,x-.4)/x,2);case"occupancy":return 100*(1-Math.pow(1-.35,x));case"capture":return 4800/x;case"restore":return 100*(1-exp(-.12*x));case"invasive":return 500/(1+19*exp(-.48*x));case"flow":return 100*Math.min(x/40,1);case"fishing":return 100*exp(-.18*x);case"equity":return 120*x/100;case"protected":return 70*x/100;case"did":return 8-x;case"decision":return 80*x/100;default:throw Error("Unknown model");}}
function draw(el,x){const svg=el.querySelector('svg'),kind=el.dataset.kind,lo=Number(el.dataset.min),hi=Number(el.dataset.max);const vals=[];for(let i=0;i<=70;i++){const n=lo+(hi-lo)*i/70;vals.push([n,compute(kind,n)])}let ymin=Math.min(...vals.map(v=>v[1])),ymax=Math.max(...vals.map(v=>v[1]));if(ymin===ymax)ymax=ymin+1;const sx=v=>45+380*(v-lo)/(hi-lo),sy=v=>160-130*(v-ymin)/(ymax-ymin);const pts=vals.map(v=>sx(v[0]).toFixed(2)+','+sy(v[1]).toFixed(2)).join(' ');svg.innerHTML='<line x1="45" x2="425" y1="160" y2="160" stroke="#a3afa8"/><line x1="45" x2="45" y1="24" y2="160" stroke="#a3afa8"/><polyline fill="none" stroke="#1d775e" stroke-width="3" points="'+pts+'"/><circle cx="'+sx(x).toFixed(2)+'" cy="'+sy(compute(kind,x)).toFixed(2)+'" r="5" fill="#be6a19"/><text x="45" y="181" font-size="11" fill="#52665b">'+lo+'</text><text x="425" y="181" text-anchor="end" font-size="11" fill="#52665b">'+hi+'</text><text x="45" y="14" font-size="11" fill="#52665b">'+ymax.toFixed(1)+'</text>'}
function init(el){const input=el.querySelector('input'),out=el.querySelector('.num'),readout=el.querySelector('.readout');function update(){const x=Number(input.value),y=compute(el.dataset.kind,x);out.textContent=Number.isFinite(y)?y.toFixed(2):'undefined';readout.textContent='Input '+x+', calculated output '+y.toFixed(2)+' '+el.dataset.output;draw(el,x)}input.addEventListener('input',update);update()}
document.querySelectorAll('.model').forEach(init);window.ConservationModels={compute:compute};})();

window.CONSERVATION_MODELS = [
  {
    "id": "conservation-01",
    "unit": 1,
    "title": "Species\u2013area relationship",
    "sliderLabel": "Area in hectares",
    "resultLabel": "Species richness (toy)",
    "min": 1,
    "max": 300,
    "initial": 70,
    "step": 1,
    "kind": "area",
    "formula": "S = 4.5 A^0.27",
    "limitation": "Illustrative species\u2013area curve; not an actual site inventory.",
    "initialOutput": 14.170624
  },
  {
    "id": "conservation-02",
    "unit": 1,
    "title": "Constant annual decline",
    "sliderLabel": "Years",
    "resultLabel": "Population (initial 100)",
    "min": 0,
    "max": 25,
    "initial": 8,
    "step": 1,
    "kind": "decline",
    "formula": "N = 100 \u00d7 0.93^t",
    "limitation": "Constant proportional decline is unrealistic across long periods.",
    "initialOutput": 55.958181
  },
  {
    "id": "conservation-03",
    "unit": 2,
    "title": "Logistic population trajectory",
    "sliderLabel": "Years",
    "resultLabel": "Population (animals)",
    "min": 0,
    "max": 30,
    "initial": 8,
    "step": 1,
    "kind": "logistic",
    "formula": "N = 300/(1+4 exp(\u22120.30t))",
    "limitation": "Density and environment are held constant.",
    "initialOutput": 220.123417
  },
  {
    "id": "conservation-04",
    "unit": 2,
    "title": "Genetic drift illustration",
    "sliderLabel": "Generations",
    "resultLabel": "% original heterozygosity",
    "min": 0,
    "max": 60,
    "initial": 15,
    "step": 1,
    "kind": "drift",
    "formula": "H(t) = 100(1\u22121/80)^t",
    "limitation": "Idealized Ne=40, no migration or mutation.",
    "initialOutput": 82.805001
  },
  {
    "id": "conservation-05",
    "unit": 3,
    "title": "Connectivity with distance",
    "sliderLabel": "Separation distance (km)",
    "resultLabel": "Relative exchange",
    "min": 0,
    "max": 40,
    "initial": 15,
    "step": 1,
    "kind": "connectivity",
    "formula": "100 exp(\u2212d/8)",
    "limitation": "No hard barriers, species differences or matrix effect.",
    "initialOutput": 15.335497
  },
  {
    "id": "conservation-06",
    "unit": 3,
    "title": "Interior patch-area model",
    "sliderLabel": "Square patch width (km)",
    "resultLabel": "% interior habitat",
    "min": 0.2,
    "max": 6,
    "initial": 2,
    "step": 0.1,
    "kind": "interior",
    "formula": "100[max(0,w\u22120.4)/w]^2",
    "limitation": "Square habitat patch with fixed 0.2 km edge depth.",
    "initialOutput": 64.0
  },
  {
    "id": "conservation-07",
    "unit": 4,
    "title": "Detection across repeat visits",
    "sliderLabel": "Independent survey visits",
    "resultLabel": "% detection if present",
    "min": 1,
    "max": 15,
    "initial": 4,
    "step": 1,
    "kind": "occupancy",
    "formula": "100[1\u2212(1\u22120.35)^k]",
    "limitation": "Assumes occupancy closure and constant detection probability.",
    "initialOutput": 82.149375
  },
  {
    "id": "conservation-08",
    "unit": 4,
    "title": "Abundance from recaptures",
    "sliderLabel": "Number of marked recaptures",
    "resultLabel": "Estimated N",
    "min": 5,
    "max": 50,
    "initial": 12,
    "step": 1,
    "kind": "capture",
    "formula": "N = (80\u00d760)/recaptures",
    "limitation": "Oversimplified closed-population Lincoln\u2013Petersen estimate.",
    "initialOutput": 400.0
  },
  {
    "id": "conservation-09",
    "unit": 5,
    "title": "Restoration recovery curve",
    "sliderLabel": "Years since treatment",
    "resultLabel": "% hypothetical reference condition",
    "min": 0,
    "max": 35,
    "initial": 10,
    "step": 1,
    "kind": "restore",
    "formula": "100(1\u2212exp(\u22120.12t))",
    "limitation": "Reference target and asymptote are hypothetical.",
    "initialOutput": 69.880579
  },
  {
    "id": "conservation-10",
    "unit": 5,
    "title": "Invasive population logistic",
    "sliderLabel": "Years",
    "resultLabel": "Individuals",
    "min": 0,
    "max": 20,
    "initial": 7,
    "step": 1,
    "kind": "invasive",
    "formula": "N = 500/(1+19 exp(\u22120.48t))",
    "limitation": "No management, seasonality or stochasticity.",
    "initialOutput": 301.210277
  },
  {
    "id": "conservation-11",
    "unit": 6,
    "title": "Freshwater flow adequacy",
    "sliderLabel": "Ecological pulse days",
    "resultLabel": "% reference days",
    "min": 0,
    "max": 60,
    "initial": 25,
    "step": 1,
    "kind": "flow",
    "formula": "100 min(days/40,1)",
    "limitation": "Only one flow dimension: not an environmental flow assessment.",
    "initialOutput": 62.5
  },
  {
    "id": "conservation-12",
    "unit": 6,
    "title": "Marine fishing mortality survival",
    "sliderLabel": "Fishing exposure (relative)",
    "resultLabel": "% annual survival proxy",
    "min": 0,
    "max": 10,
    "initial": 4,
    "step": 0.1,
    "kind": "fishing",
    "formula": "100 exp(\u22120.18F)",
    "limitation": "Excludes recruitment, natural mortality and selectivity.",
    "initialOutput": 48.675226
  },
  {
    "id": "conservation-13",
    "unit": 7,
    "title": "Benefit distribution",
    "sliderLabel": "Share to affected community (%)",
    "resultLabel": "Community benefit units",
    "min": 0,
    "max": 100,
    "initial": 40,
    "step": 1,
    "kind": "equity",
    "formula": "Total 120 \u00d7 share/100",
    "limitation": "Counts units not consent, influence or fairness.",
    "initialOutput": 48.0
  },
  {
    "id": "conservation-14",
    "unit": 7,
    "title": "Protected-area effective coverage",
    "sliderLabel": "% nominal area managed well",
    "resultLabel": "Effectively managed hectares",
    "min": 0,
    "max": 100,
    "initial": 35,
    "step": 1,
    "kind": "protected",
    "formula": "70 \u00d7 share/100",
    "limitation": "Simple accounting, not biodiversity effectiveness.",
    "initialOutput": 24.5
  },
  {
    "id": "conservation-15",
    "unit": 8,
    "title": "Counterfactual net impact",
    "sliderLabel": "Improvement at control site",
    "resultLabel": "Additional change (count units)",
    "min": 0,
    "max": 20,
    "initial": 4,
    "step": 1,
    "kind": "did",
    "formula": "(24\u221216) \u2212 control gain",
    "limitation": "Parallel trends and no spillovers are unverified.",
    "initialOutput": 4
  },
  {
    "id": "conservation-16",
    "unit": 8,
    "title": "Probability-weighted benefit",
    "sliderLabel": "Chance of successful implementation (%)",
    "resultLabel": "Expected outcome units",
    "min": 0,
    "max": 100,
    "initial": 65,
    "step": 1,
    "kind": "decision",
    "formula": "80 \u00d7 chance/100",
    "limitation": "Outcome units and probability are invented for teaching.",
    "initialOutput": 52.0
  }
];


/* SimulationEngine adapter for Conservation Biology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof ConservationModels === 'undefined' || typeof ConservationModels.compute !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var models = window.CONSERVATION_MODELS || [];
    var m = models.filter(function(x){ return x.unit === u; })[0] || models[0];
    if (m) {
      var card = document.createElement('div');
      card.className = 'sim-card model';
      card.dataset.kind = m.kind;
      card.dataset.min = m.min;
      card.dataset.max = m.max;
      card.dataset.output = m.resultLabel || '';
      card.innerHTML = '<h4>' + m.title + '</h4>' +
        '<p class="formula"><code>' + m.formula + '</code></p>' +
        '<label>' + m.sliderLabel + ':<br><input type="range" min="' + m.min + '" max="' + m.max + '" step="' + m.step + '" value="' + m.initial + '"></label>' +
        '<p>Output: <strong class="num" style="color:#38bdf8;">' + m.initialOutput + '</strong> ' + m.resultLabel + '</p>' +
        '<svg viewBox="0 0 450 190" style="width:100%;height:auto;background:#0f172a;border:1px solid #1e293b;border-radius:8px;"></svg>' +
        '<p class="readout">' + (m.limitation || '') + '</p>';
      host.appendChild(card);
      var input = card.querySelector('input'), out = card.querySelector('.num'), readout = card.querySelector('.readout'), svg = card.querySelector('svg');
      function drawChart(x) {
        var lo = Number(m.min), hi = Number(m.max);
        var vals = [];
        for (var i = 0; i <= 70; i++) {
          var n = lo + (hi - lo) * i / 70;
          vals.push([n, ConservationModels.compute(m.kind, n)]);
        }
        var ymin = Math.min.apply(null, vals.map(function(v){ return v[1]; })), ymax = Math.max.apply(null, vals.map(function(v){ return v[1]; }));
        if (ymin === ymax) ymax = ymin + 1;
        var sx = function(v){ return 45 + 380 * (v - lo) / (hi - lo); };
        var sy = function(v){ return 160 - 130 * (v - ymin) / (ymax - ymin); };
        var pts = vals.map(function(v){ return sx(v[0]).toFixed(2) + ',' + sy(v[1]).toFixed(2); }).join(' ');
        var cx = sx(x).toFixed(2), cy = sy(ConservationModels.compute(m.kind, x)).toFixed(2);
        svg.innerHTML = '<line x1="45" x2="425" y1="160" y2="160" stroke="#475569"/>' +
          '<line x1="45" x2="45" y1="24" y2="160" stroke="#475569"/>' +
          '<polyline fill="none" stroke="#38bdf8" stroke-width="3" points="' + pts + '"/>' +
          '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="#f97316"/>' +
          '<text x="45" y="181" font-size="11" fill="#94a3b8">' + lo + '</text>' +
          '<text x="425" y="181" text-anchor="end" font-size="11" fill="#94a3b8">' + hi + '</text>' +
          '<text x="45" y="18" font-size="11" fill="#94a3b8">' + ymax.toFixed(1) + '</text>';
      }
      function update() {
        var x = Number(input.value), y = ConservationModels.compute(m.kind, x);
        out.textContent = Number.isFinite(y) ? y.toFixed(2) : 'undefined';
        readout.textContent = 'Input ' + x + ', calculated output ' + y.toFixed(2) + ' ' + (m.resultLabel || '');
        drawChart(x);
      }
      input.addEventListener('input', update);
      update();
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

