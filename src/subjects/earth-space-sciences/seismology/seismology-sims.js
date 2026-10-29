/* Seismology Interactive Simulation Suite */
(()=>{const models=[{"id": "slip-moment", "unit": 1, "title": "Seismic moment from average slip", "label": "Average fault slip", "input_unit": "m", "min": 0.05, "max": 4, "initial": 0.7, "output_unit": "N m", "js_expression": "3e19*x", "limitations": "Assumes 30 GPa rigidity and 1000 km\u00b2 rupture area; not site-specific."}, {"id": "rupture-slip", "unit": 1, "title": "Average slip for a fixed seismic moment", "label": "Seismic moment", "input_unit": "10\u00b9\u2079 N m", "min": 0.1, "max": 8, "initial": 1.8, "output_unit": "m", "js_expression": "x/3", "limitations": "Assumes area 1000 km\u00b2 and rigidity 30 GPa; heterogeneous slip ignored."}, {"id": "shear-speed", "unit": 2, "title": "Shear wave speed in an isotropic solid", "label": "Shear modulus", "input_unit": "GPa", "min": 10, "max": 60, "initial": 30, "output_unit": "km/s", "js_expression": "Math.sqrt(x*1e9/2700)/1000", "limitations": "Assumes density 2700 kg/m\u00b3 and homogeneous isotropic linear elasticity."}, {"id": "wavelength", "unit": 2, "title": "Wave wavelength from frequency", "label": "Frequency", "input_unit": "Hz", "min": 0.2, "max": 12, "initial": 2, "output_unit": "km", "js_expression": "3.5/x", "limitations": "Assumes nondispersive phase speed 3.5 km/s."}, {"id": "nyquist", "unit": 3, "title": "Nyquist frequency", "label": "Sample rate", "input_unit": "samples/s", "min": 10, "max": 250, "initial": 80, "output_unit": "Hz", "js_expression": "x/2", "limitations": "Useful bandwidth also depends on analog antialias filters and sensor response."}, {"id": "alias", "unit": 3, "title": "Illustrative observed alias of a 16 Hz tone", "label": "Sample rate", "input_unit": "samples/s", "min": 9, "max": 40, "initial": 18, "output_unit": "Hz", "js_expression": "Math.abs(16-Math.round(16/x)*x)", "limitations": "Sampling ideal single sinusoid; analog anti-alias filters are deliberately omitted."}, {"id": "ps-delay", "unit": 4, "title": "Direct P\u2013S arrival time separation", "label": "Hypocentral straight-line distance", "input_unit": "km", "min": 5, "max": 300, "initial": 55, "output_unit": "s", "js_expression": "x*(1/3.5-1/6)", "limitations": "Vp=6 km/s and Vs=3.5 km/s, straight path, same origin time."}, {"id": "moment-mag", "unit": 4, "title": "Moment magnitude from scalar seismic moment", "label": "Moment in units of 10\u00b9\u2078 N m", "input_unit": "10\u00b9\u2078 N m", "min": 0.1, "max": 300, "initial": 8, "output_unit": "Mw", "js_expression": "(2/3)*(Math.log10(x*1e18)-9.1)", "limitations": "Uses SI M0 and standard approximate Mw conversion; not direct Richter intensity."}, {"id": "site-freq", "unit": 5, "title": "Quarter-wavelength fundamental site frequency", "label": "Layer thickness", "input_unit": "m", "min": 10, "max": 200, "initial": 35, "output_unit": "Hz", "js_expression": "350/(4*x)", "limitations": "One-dimensional uniform low-velocity layer Vs=350 m/s above rigid base."}, {"id": "amplitude-loss", "unit": 5, "title": "Intrinsic attenuation amplitude ratio", "label": "Path length", "input_unit": "km", "min": 10, "max": 450, "initial": 80, "output_unit": "ratio", "js_expression": "Math.exp(-Math.PI*2*x/(150*3.5))", "limitations": "f=2 Hz, Q=150, v=3.5 km/s; geometric spreading and scattering excluded."}, {"id": "gr-count", "unit": 6, "title": "Gutenberg\u2013Richter toy cumulative count", "label": "Magnitude threshold", "input_unit": "Mw", "min": 2, "max": 6, "initial": 4, "output_unit": "events", "js_expression": "Math.pow(10,6-x)", "limitations": "Assumes a=6, b=1 in an invented fixed space/time window and complete catalog."}, {"id": "poisson-prob", "unit": 6, "title": "At least one event in ten years", "label": "Expected annual rate", "input_unit": "events/year", "min": 0.001, "max": 0.5, "initial": 0.05, "output_unit": "probability", "js_expression": "1-Math.exp(-10*x)", "limitations": "Independent stationary Poisson example; not a fault-specific forecast."}, {"id": "travel-time", "unit": 7, "title": "Ideal teleseismic travel time", "label": "Ray path length", "input_unit": "km", "min": 100, "max": 4500, "initial": 1200, "output_unit": "s", "js_expression": "x/8", "limitations": "Constant 8 km/s ray velocity, not realistic curved-ray global travel times."}, {"id": "crust-depth", "unit": 7, "title": "Ideal thickness from vertical P-to-S delay", "label": "P\u2013S conversion delay", "input_unit": "s", "min": 0.5, "max": 9, "initial": 4, "output_unit": "km", "js_expression": "x/(1/3.7-1/6.4)", "limitations": "Simplified vertical ray approximation with Vp=6.4 and Vs=3.7 km/s."}, {"id": "early-warning", "unit": 8, "title": "Illustrative remaining warning lead time", "label": "Distance to source", "input_unit": "km", "min": 10, "max": 200, "initial": 75, "output_unit": "s", "js_expression": "Math.max(0,x/3.5-7)", "limitations": "Vs=3.5 km/s with imposed 7 s detection+communication latency; not operational."}, {"id": "hazard-prob", "unit": 8, "title": "Fifty-year probability at constant annual rate", "label": "Annual exceedance rate", "input_unit": "per year", "min": 0.0001, "max": 0.05, "initial": 0.005, "output_unit": "percent", "js_expression": "100*(1-Math.exp(-50*x))", "limitations": "Stationary Poisson assumption; actual hazard curves and local code decisions require experts."}];const funcs={"slip-moment":x=>(3e19*x),"rupture-slip":x=>(x/3),"shear-speed":x=>(Math.sqrt(x*1e9/2700)/1000),"wavelength":x=>(3.5/x),"nyquist":x=>(x/2),"alias":x=>(Math.abs(16-Math.round(16/x)*x)),"ps-delay":x=>(x*(1/3.5-1/6)),"moment-mag":x=>((2/3)*(Math.log10(x*1e18)-9.1)),"site-freq":x=>(350/(4*x)),"amplitude-loss":x=>(Math.exp(-Math.PI*2*x/(150*3.5))),"gr-count":x=>(Math.pow(10,6-x)),"poisson-prob":x=>(1-Math.exp(-10*x)),"travel-time":x=>(x/8),"crust-depth":x=>(x/(1/3.7-1/6.4)),"early-warning":x=>(Math.max(0,x/3.5-7)),"hazard-prob":x=>(100*(1-Math.exp(-50*x)))};const fmt=v=>Number.isFinite(v)?Number(v.toPrecision(6)).toLocaleString('en-US'):'undefined';function plot(m,f,x){const p=Array.from({length:65},(_,i)=>{const a=m.min+(m.max-m.min)*i/64;return {x:a,y:f(a)}}).filter(t=>Number.isFinite(t.y));if(!p.length)return '';const ymin=Math.min(...p.map(t=>t.y)),ymax=Math.max(...p.map(t=>t.y));const xp=t=>15+480*(t-m.min)/(m.max-m.min),yp=v=>116-91*(v-ymin)/Math.max(1e-10,ymax-ymin);return '<path d="'+p.map((t,i)=>(i?'L':'M')+xp(t.x).toFixed(2)+' '+yp(t.y).toFixed(2)).join(' ')+'" stroke="#087b89" fill="none" stroke-width="3"/><circle cx="'+xp(x).toFixed(2)+'" cy="'+yp(f(x)).toFixed(2)+'" r="5" fill="#b45517"/>';}document.addEventListener('DOMContentLoaded',()=>{const lookup=new Map(models.map(m=>[m.id,m]));document.querySelectorAll('section.model[data-model]').forEach(s=>{const id=s.dataset.model,m=lookup.get(id),fn=funcs[id],input=s.querySelector('input'),output=s.querySelector('output'),chart=s.querySelector('svg');if(!m||!fn||!input||!output||!chart)return;function update(){const x=+input.value;output.textContent=fmt(fn(x))+' '+m.output_unit;input.setAttribute('aria-valuetext',x+' '+m.input_unit);chart.innerHTML=plot(m,fn,x)}input.addEventListener('input',update);update()})})})();


(function(window) {
  if (!window.SimulationEngine) {
    window.SimulationEngine = {};
  }
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = '';
    
    var unitNum = 1;
    var mMatch = (simType || '').match(/(\d+)$/);
    if (!mMatch && typeof document !== 'undefined') {
      var bIdx = document.body.dataset.chapterIndex;
      if (bIdx !== undefined && bIdx !== null && bIdx !== '') {
        unitNum = parseInt(bIdx, 10) + 1;
      }
    }
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

