/* Biological Research Methods Interactive Simulation Suite */
window.BIO_METHOD_MODELS=[{"id": "model-01", "unit": 1, "title": "Question contrast sensitivity", "subtitle": "Synthetic signal-to-noise illustration", "kind": "ratio", "sliderLabel": "Effect / reference noise", "expression": "x/(x+3)", "min": 0, "max": 12, "default": 3, "sliderUnit": "units", "description": "Illustrates why a larger contrast relative to noise is easier to distinguish; the formula is an educational index, not power."}, {"id": "model-02", "unit": 1, "title": "Screening yield", "subtitle": "Screening fraction", "kind": "percent", "sliderLabel": "Eligible record fraction", "expression": "100*x", "min": 0, "max": 1, "default": 0.18, "sliderUnit": "fraction", "description": "The retained fraction depends on scope and indexing; high yield does not certify evidence quality."}, {"id": "model-03", "unit": 2, "title": "Cluster design effect", "subtitle": "Equal-size cluster approximation", "kind": "multiplier", "sliderLabel": "Intraclass correlation", "expression": "1+4*x", "min": 0, "max": 0.8, "default": 0.2, "sliderUnit": "ICC", "description": "Five readings per experimental cluster yield design effect 1+4 ICC under simplifying assumptions."}, {"id": "model-04", "unit": 2, "title": "Factorial interaction", "subtitle": "Difference-of-differences algebra", "kind": "difference", "sliderLabel": "Additional combined effect", "expression": "2*x", "min": -5, "max": 5, "default": 1, "sliderUnit": "units", "description": "Illustrates additivity of two contrasts without claiming a biological interaction mechanism."}, {"id": "model-05", "unit": 3, "title": "Assay response curve", "subtitle": "Idealized linear calibration", "kind": "signal", "sliderLabel": "Reference concentration", "expression": "0.10+0.08*x", "min": 0, "max": 12, "default": 8, "sliderUnit": "units", "description": "A calibration is meaningful only within a validated analytical region and comparable matrix."}, {"id": "model-06", "unit": 3, "title": "Repeat-visit detection", "subtitle": "At least one detection in three visits", "kind": "probability", "sliderLabel": "Per-visit detectability", "expression": "1-(1-x)**3", "min": 0, "max": 1, "default": 0.4, "sliderUnit": "probability", "description": "Assumes independent identical visits and stable ecological state; neither assumption is guaranteed in the field."}, {"id": "model-07", "unit": 4, "title": "Dataset completeness", "subtitle": "Fraction remaining observed", "kind": "observed fraction", "sliderLabel": "Missing record fraction", "expression": "1-x", "min": 0, "max": 1, "default": 0.16, "sliderUnit": "fraction", "description": "Completeness is not the same as unbiasedness; missing-not-at-random mechanisms matter."}, {"id": "model-08", "unit": 4, "title": "Cumulative uncertainty", "subtitle": "Idealized quality reduction index", "kind": "index", "sliderLabel": "Transformation count", "expression": "exp(-x/4)", "min": 0, "max": 12, "default": 3, "sliderUnit": "steps", "description": "Illustrative decay is not a measured effect; provenance and transparent validation are essential."}, {"id": "model-09", "unit": 5, "title": "Confidence interval half-width", "subtitle": "Normal-approximation mean interval", "kind": "units", "sliderLabel": "Independent sample count", "expression": "1.96*6/sqrt(x)", "min": 4, "max": 200, "default": 36, "sliderUnit": "samples", "description": "A fixed SD of six and independent normal-approximation assumptions determine this educational half-width."}, {"id": "model-10", "unit": 5, "title": "Logistic probability", "subtitle": "Link function demonstration", "kind": "probability", "sliderLabel": "Linear predictor position", "expression": "1/(1+exp(-(x-5)))", "min": 0, "max": 10, "default": 5, "sliderUnit": "predictor", "description": "Logistic transformations produce bounded probabilities; correct estimation still needs valid data and model structure."}, {"id": "model-11", "unit": 6, "title": "Sequencing filter yield", "subtitle": "Read retention accounting", "kind": "percent", "sliderLabel": "Percent reads removed", "expression": "100-x", "min": 0, "max": 100, "default": 25, "sliderUnit": "percent removed", "description": "Read retention is not the same as organism abundance or contamination correction."}, {"id": "model-12", "unit": 6, "title": "Qualitative coverage", "subtitle": "Illustrative diminishing capture", "kind": "index", "sliderLabel": "Distinct interview contexts", "expression": "x/(x+2)", "min": 0, "max": 20, "default": 6, "sliderUnit": "contexts", "description": "A teaching curve, not an empirical rule for theme saturation; positionality and recruitment quality remain decisive."}, {"id": "model-13", "unit": 7, "title": "Inverse variance weight", "subtitle": "Relative weight of precise study", "kind": "weight fraction", "sliderLabel": "Variance of other study", "expression": "x/(x+1)", "min": 0.2, "max": 9, "default": 4, "sliderUnit": "variance units", "description": "Under simplified inverse-variance weighting, higher variance in the other study shifts weight to the fixed reference study."}, {"id": "model-14", "unit": 7, "title": "Replication uncertainty", "subtitle": "Sampling uncertainty with n", "kind": "index", "sliderLabel": "Independent replicate count", "expression": "6/sqrt(x)", "min": 4, "max": 200, "default": 30, "sliderUnit": "replicates", "description": "Illustrates how precision can change with independent replication; contextual bias does not disappear."}, {"id": "model-15", "unit": 8, "title": "Data disclosure hazard", "subtitle": "Simplified sensitivity index", "kind": "index", "sliderLabel": "Reidentification opportunity", "expression": "x*x", "min": 0, "max": 1, "default": 0.3, "sliderUnit": "fraction", "description": "A purely illustrative increasing index, not a risk assessment or a privacy security guarantee."}, {"id": "model-16", "unit": 8, "title": "Expected net decision value", "subtitle": "Expected utility under fixed assumptions", "kind": "arbitrary units", "sliderLabel": "Chance of benefit", "expression": "100*x-35", "min": 0, "max": 1, "default": 0.6, "sliderUnit": "probability", "description": "Illustrates a decision calculation, not a recommendation or replacement for ethics and equity analysis."}];
(function(){'use strict';const models=window.BIO_METHOD_MODELS||[];function calc(id,x){switch(id){case 1:return x/(x+3);case 2:return 100*x;case 3:return 1+4*x;case 4:return 2*x;case 5:return .1+.08*x;case 6:return 1-Math.pow(1-x,3);case 7:return 1-x;case 8:return Math.exp(-x/4);case 9:return 1.96*6/Math.sqrt(x);case 10:return 1/(1+Math.exp(-(x-5)));case 11:return 100-x;case 12:return x/(x+2);case 13:return x/(x+1);case 14:return 6/Math.sqrt(x);case 15:return x*x;case 16:return 100*x-35;default:return NaN}}window.BioMethodsCalc=calc;const fmt=n=>Number.isFinite(n)?n.toLocaleString('en-US',{maximumFractionDigits:3}):'not defined';function renderCard(data){let ix=Number(data.id.split('-')[1]);const box=document.createElement('section');box.className='model';let h=document.createElement('h3');h.textContent=data.title;box.append(h);let p=document.createElement('p');p.textContent=data.description;box.append(p);const label=document.createElement('label');label.textContent=data.sliderLabel+' ('+data.sliderUnit+')';const slider=document.createElement('input');slider.type='range';slider.min=data.min;slider.max=data.max;slider.step=(data.max-data.min)/1000;slider.value=data.default;slider.id='slider-'+data.id;label.htmlFor=slider.id;box.append(label,slider);const output=document.createElement('output');output.setAttribute('aria-live','polite');output.htmlFor=slider.id;box.append(output);const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('viewBox','0 0 360 170');svg.setAttribute('role','img');svg.setAttribute('aria-label','Curve of '+data.title+' versus '+data.sliderLabel);const line=document.createElementNS('http://www.w3.org/2000/svg','polyline');line.setAttribute('fill','none');line.setAttribute('stroke','#168879');line.setAttribute('stroke-width','3');svg.append(line);const dot=document.createElementNS('http://www.w3.org/2000/svg','circle');dot.setAttribute('r','5');dot.setAttribute('fill','#b45309');svg.append(dot);box.append(svg);const eq=document.createElement('p');eq.className='equation';eq.textContent='Teaching expression: '+data.expression;box.append(eq);function update(){const xmin=Number(data.min),xmax=Number(data.max),x=Number(slider.value);const pts=Array.from({length:61},(_,j)=>{const v=xmin+(xmax-xmin)*j/60;return [v,calc(ix,v)]}).filter(v=>Number.isFinite(v[1]));const values=pts.map(z=>z[1]),ymin=Math.min(...values),ymax=Math.max(...values),delta=(ymax-ymin)||1;const X=z=>12+336*(z-xmin)/(xmax-xmin);const Y=z=>152-134*(z-ymin)/delta;line.setAttribute('points',pts.map(z=>X(z[0]).toFixed(2)+','+Y(z[1]).toFixed(2)).join(' '));dot.setAttribute('cx',X(x));dot.setAttribute('cy',Y(calc(ix,x)));output.textContent=fmt(x)+' '+data.sliderUnit+' → '+fmt(calc(ix,x))+' '+data.kind;svg.setAttribute('aria-label',data.title+': current input '+fmt(x)+'; output '+fmt(calc(ix,x)));}slider.addEventListener('input',update);update();return box;}document.querySelectorAll('[data-unit-models]').forEach(el=>{let u=Number(el.dataset.unitModels);models.filter(m=>m.unit===u).forEach(m=>el.append(renderCard(m)));});})();


/* SimulationEngine adapter for Biological Research Methods */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof BioMethodsCalc !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var models = window.BIO_METHOD_MODELS || [];
    var data = models.filter(function(x){ return x.unit === u; })[0] || models[0];
    if (data) {
      var ix = Number(data.id.split('-')[1]);
      var box = document.createElement('section');
      box.className = 'sim-card model';
      var h = document.createElement('h4');
      h.textContent = data.title;
      box.append(h);
      var p = document.createElement('p');
      p.textContent = data.description;
      box.append(p);
      var label = document.createElement('label');
      label.textContent = data.sliderLabel + ' (' + data.sliderUnit + ')';
      var slider = document.createElement('input');
      slider.type = 'range';
      slider.min = data.min;
      slider.max = data.max;
      slider.step = (data.max - data.min) / 1000;
      slider.value = data.default;
      slider.id = 'slider-' + data.id;
      label.htmlFor = slider.id;
      box.append(label, slider);
      var output = document.createElement('output');
      output.setAttribute('aria-live', 'polite');
      output.style.display = 'block';
      output.style.margin = '0.5rem 0';
      output.style.fontWeight = '600';
      output.style.color = '#38bdf8';
      box.append(output);
      var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.setAttribute('viewBox', '0 0 360 170');
      svg.setAttribute('role', 'img');
      svg.setAttribute('aria-label', 'Curve of ' + data.title + ' versus ' + data.sliderLabel);
      svg.style.width = '100%';
      svg.style.height = 'auto';
      svg.style.background = '#0f172a';
      svg.style.border = '1px solid #1e293b';
      svg.style.borderRadius = '8px';
      var line = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
      line.setAttribute('fill', 'none');
      line.setAttribute('stroke', '#38bdf8');
      line.setAttribute('stroke-width', '3');
      svg.append(line);
      var dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      dot.setAttribute('r', '5');
      dot.setAttribute('fill', '#f97316');
      svg.append(dot);
      box.append(svg);
      var eq = document.createElement('p');
      eq.className = 'equation readout';
      eq.textContent = 'Teaching expression: ' + data.expression;
      box.append(eq);
      function fmt(n) { return Number.isFinite(n) ? n.toLocaleString('en-US', {maximumFractionDigits: 3}) : 'not defined'; }
      function update() {
        var xmin = Number(data.min), xmax = Number(data.max), x = Number(slider.value);
        var pts = Array.from({length: 61}, function(_, j) {
          var v = xmin + (xmax - xmin) * j / 60;
          return [v, BioMethodsCalc(ix, v)];
        }).filter(function(v){ return Number.isFinite(v[1]); });
        var values = pts.map(function(z){ return z[1]; }), ymin = Math.min.apply(null, values), ymax = Math.max.apply(null, values), delta = (ymax - ymin) || 1;
        var X = function(z){ return 12 + 336 * (z - xmin) / (xmax - xmin); };
        var Y = function(z){ return 152 - 134 * (z - ymin) / delta; };
        line.setAttribute('points', pts.map(function(z){ return X(z[0]).toFixed(2) + ',' + Y(z[1]).toFixed(2); }).join(' '));
        dot.setAttribute('cx', X(x));
        dot.setAttribute('cy', Y(BioMethodsCalc(ix, x)));
        output.textContent = fmt(x) + ' ' + data.sliderUnit + ' → ' + fmt(BioMethodsCalc(ix, x)) + ' ' + data.kind;
      }
      slider.addEventListener('input', update);
      update();
      host.appendChild(box);
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

