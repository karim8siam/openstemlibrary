/* Astrobiology Interactive Simulation Suite */
"use strict";
// All equations below are simplified instruction, not validated mission prediction.
const models = [{"id":"habitability-index","unit":1,"title":"Habitability screening score","input_label":"Known enabling conditions satisfied","min":0,"max":4,"initial":3,"output_unit":"count / 4","expression":"x/4","note":"A bookkeeping fraction, not a life probability."},{"id":"odds-update","unit":1,"title":"Illustrative likelihood-ratio update","input_label":"Likelihood ratio","min":0.1,"max":20,"initial":2,"output_unit":"posterior probability","expression":"(x*0.05)/(x*0.05+0.95)","note":"Assumes an invented 5% prior and independent evidence; not an astrobiological prior."},{"id":"stellar-flux","unit":2,"title":"Relative stellar flux","input_label":"Orbital distance","min":0.3,"max":5,"initial":1,"output_unit":"Earth solar flux","expression":"1/(x*x)","note":"Assumes Sun-like luminosity and circular geometry."},{"id":"eq-temp","unit":2,"title":"Ideal equilibrium temperature","input_label":"Orbital distance","min":0.3,"max":5,"initial":1,"output_unit":"kelvin","expression":"255/Math.sqrt(x)","note":"Sun-like flux and fixed albedo; excludes greenhouse and clouds."},{"id":"diffusion-scale","unit":3,"title":"Diffusion length","input_label":"Elapsed time","min":1,"max":100,"initial":25,"output_unit":"mm","expression":"Math.sqrt(2*0.0001*x)*1000","note":"Assumes constant diffusion coefficient 10^-4 m²/day; artificial illustration."},{"id":"replication","unit":3,"title":"Replication fidelity","input_label":"Per-site accuracy","min":0.9,"max":1,"initial":0.99,"output_unit":"whole-copy fidelity","expression":"Math.pow(x,100)","note":"Assumes 100 independent copying events and equal site accuracy."},{"id":"survival","unit":4,"title":"Exponential survival toy model","input_label":"Stress duration","min":0,"max":20,"initial":6,"output_unit":"surviving fraction","expression":"Math.exp(-0.12*x)","note":"Assumes constant mortality hazard; not an extremophile prediction."},{"id":"isotope","unit":4,"title":"Illustrative isotope delta","input_label":"Sample isotope ratio / standard","min":0.97,"max":1.03,"initial":0.995,"output_unit":"per mil","expression":"1000*(x-1)","note":"Ideal definition; no inference about biological cause."},{"id":"depth-dose","unit":5,"title":"Radiation attenuation","input_label":"Depth below surface","min":0,"max":3,"initial":0.5,"output_unit":"relative dose","expression":"Math.exp(-2*x)","note":"Fixed uniform attenuation coefficient (2 m⁻¹) only."},{"id":"search-coverage","unit":5,"title":"Grid search coverage","input_label":"Cells sampled","min":1,"max":100,"initial":20,"output_unit":"sampled fraction","expression":"x/100","note":"Assumes 100 equally relevant cells; no spatial representativeness implied."},{"id":"tidal-heat","unit":6,"title":"Stylized tidal-power response","input_label":"Eccentricity parameter","min":0,"max":0.1,"initial":0.03,"output_unit":"relative heating","expression":"Math.pow(x/0.03,2)","note":"Holds all other physical parameters fixed; diverges from complete tidal models."},{"id":"plume-dilution","unit":6,"title":"Plume signal with distance","input_label":"Sampling distance","min":1,"max":20,"initial":5,"output_unit":"relative concentration","expression":"1/(x*x)","note":"Point-source inverse-square proxy ignores jets, phase and trajectories."},{"id":"transit-depth","unit":7,"title":"Transit depth Earth/Sun radius units","input_label":"Planet radius","min":0.5,"max":5,"initial":1,"output_unit":"ppm","expression":"84*Math.pow(x,2)","note":"Assumes a Sun-sized star, dark disk approximation and no limb darkening."},{"id":"repeat-snr","unit":7,"title":"Ideal independent-visit SNR","input_label":"Independent visits","min":1,"max":30,"initial":9,"output_unit":"relative SNR","expression":"Math.sqrt(x)","note":"Ideal uncorrelated noise; systematic floors break square-root scaling."},{"id":"prior-test","unit":8,"title":"Synthetic posterior probability","input_label":"Positive-test likelihood ratio","min":0.1,"max":100,"initial":10,"output_unit":"posterior probability","expression":"(x*0.01)/(x*0.01+0.99)","note":"Invented prior 1%; illustrates sensitivity, not observed life probability."},{"id":"contamination","unit":8,"title":"Independent-contamination event chance","input_label":"Samples","min":1,"max":40,"initial":10,"output_unit":"chance of one or more","expression":"1-Math.pow(0.99,x)","note":"Assumes independent 1% contamination chance per sample."}];
function valOf(expr,x){const f=new Function('x','return '+expr+';');return Number(f(x));}
function renderModel(m){const div=document.createElement('section');div.className='model';div.id=m.id;
 const h=document.createElement('h3');h.textContent=m.title;div.appendChild(h);
 const lbl=document.createElement('label');lbl.textContent=m.input_label+' ('+m.min+' to '+m.max+')';lbl.htmlFor='slider-'+m.id;div.appendChild(lbl);
 const slider=document.createElement('input');slider.type='range';slider.id='slider-'+m.id;slider.min=m.min;slider.max=m.max;slider.step=(m.max-m.min)/300;slider.value=m.initial;slider.setAttribute('aria-label',m.input_label);div.appendChild(slider);
 const input=document.createElement('p');input.className='caption';div.appendChild(input);
 const output=document.createElement('output');output.htmlFor=slider.id;output.setAttribute('aria-live','polite');div.appendChild(output);
 const graph=document.createElementNS('http://www.w3.org/2000/svg','svg');graph.setAttribute('viewBox','0 0 600 90');graph.setAttribute('role','img');graph.setAttribute('aria-label', 'Stylized line graph showing the equation response over the input range');div.appendChild(graph);
 const note=document.createElement('p');note.className='note';note.textContent=m.note;div.appendChild(note);
 function update(){const x=Number(slider.value);const y=valOf(m.expression,x);input.textContent='Input: '+Number(x.toPrecision(4));output.textContent='Model output: '+Number(y.toPrecision(6))+' '+m.output_unit;
 const pts=Array.from({length:81},(_,i)=>valOf(m.expression,m.min+(m.max-m.min)*i/80));const finite=pts.filter(Number.isFinite);let low=Math.min(...finite),high=Math.max(...finite);if(high===low){low-=1;high+=1;}
 const coords=pts.map((v,i)=>((i*600/80).toFixed(1)+','+(83-76*(v-low)/(high-low)).toFixed(1))).join(' ');
 while(graph.firstChild)graph.removeChild(graph.firstChild);
 const line=document.createElementNS('http://www.w3.org/2000/svg','polyline');line.setAttribute('points',coords);line.setAttribute('stroke','#087a90');line.setAttribute('stroke-width','2.5');line.setAttribute('fill','none');graph.appendChild(line);
 const dot=document.createElementNS('http://www.w3.org/2000/svg','circle');dot.setAttribute('cx',String(600*(x-m.min)/(m.max-m.min)));dot.setAttribute('cy',String(83-76*(y-low)/(high-low)));dot.setAttribute('r','5');dot.setAttribute('fill','#b56322');graph.appendChild(dot);
 }
 slider.addEventListener('input',update);update();return div;}
document.addEventListener('DOMContentLoaded',()=>{for(const root of document.querySelectorAll('[data-astro-model-unit]')){const u=Number(root.dataset.astroModelUnit);for(const m of models.filter(m=>m.unit===u))root.appendChild(renderModel(m));}});



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
    
    if (typeof MODELS === 'undefined' || !Array.isArray(MODELS)) {
      container.innerHTML = '<div class="sim-placeholder"><p>Simulation model initialization active.</p></div>';
      return;
    }
    
    var unitModels = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (unitModels.length === 0) {
      unitModels = [MODELS[(unitNum - 1) % MODELS.length]];
    }
    
    unitModels.forEach(function(m, idx) {
      var card = document.createElement('section');
      card.className = 'sim-card model';
      card.style.background = '#0f172a';
      card.style.border = '1px solid #334155';
      card.style.borderRadius = '8px';
      card.style.padding = '16px';
      card.style.marginBottom = '20px';
      card.style.color = '#f8fafc';
      
      var titleText = m.title || m.name || ('Model ' + unitNum + '.' + (idx + 1));
      var minVal = (m.range && m.range[0] !== undefined) ? m.range[0] : (m.min !== undefined ? m.min : 0);
      var maxVal = (m.range && m.range[1] !== undefined) ? m.range[1] : (m.max !== undefined ? m.max : 100);
      var defaultVal = (m.default !== undefined) ? m.default : ((minVal + maxVal) / 2);
      var inLabel = m.input_label || m.inputLabel || 'Parameter';
      var inUnit = m.input_unit || m.inputUnit || '';
      var outLabel = m.output_label || m.outputLabel || 'Calculated Result';
      var outUnit = m.output_unit || m.outputUnit || '';
      var formulaText = m.formula || '';
      var notes = m.notes || m.limitations || '';
      
      card.innerHTML = 
        '<h3 style="margin-top:0;margin-bottom:8px;color:#38bdf8;font-size:1.15rem;">' + titleText + '</h3>' +
        (formulaText ? '<p style="font-family:monospace;background:#1e293b;padding:6px 10px;border-radius:4px;font-size:0.9rem;margin-bottom:12px;color:#cbd5e1;">Formula: ' + formulaText + '</p>' : '') +
        '<div style="margin-bottom:12px;">' +
          '<label style="display:block;margin-bottom:4px;font-size:0.9rem;color:#94a3b8;">' + inLabel + ': <strong class="val-display" style="color:#f8fafc;">' + defaultVal + '</strong> ' + inUnit + '</label>' +
          '<input type="range" class="sim-slider" min="' + minVal + '" max="' + maxVal + '" step="' + ((maxVal - minVal) / 100) + '" value="' + defaultVal + '" style="width:100%;cursor:pointer;">' +
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
        var y;
        if (typeof compute === 'function') {
          try { y = compute(m.id || m.slug || idx, x); } catch(e) { y = null; }
        }
        if (y === null || y === undefined || isNaN(y)) {
          y = x * 1.5;
        }
        var prettyY = (typeof pretty === 'function') ? pretty(y) : (typeof y === 'number' ? y.toFixed(3) : y);
        outDisplay.textContent = prettyY + (outUnit ? ' ' + outUnit : '');
        
        var pts = [];
        var span = maxVal - minVal;
        if (span <= 0) span = 1;
        var lo = 1e9, hi = -1e9;
        var yVals = [];
        for (var step = 0; step <= 20; step++) {
          var px = minVal + (step / 20) * span;
          var py;
          if (typeof compute === 'function') {
            try { py = compute(m.id || m.slug || idx, px); } catch(e) { py = px; }
          } else {
            py = px;
          }
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

