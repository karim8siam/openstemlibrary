/* Geodesy and Earth Observation Interactive Simulation Suite */
(()=>{'use strict';const models=[{"id": "ellipsoid-minor", "title": "Reference ellipsoid minor axis", "unit": 1, "label": "Inverse flattening", "input_unit": "1", "min": 250, "max": 350, "initial": 298.257223563, "output_unit": "km", "js_expression": "6378.137*(1-1/x)", "limitations": "WGS 84 nominal semi-major axis 6378.137 km; inverse flattening varies hypothetically."}, {"id": "arc-length", "title": "Spherical approximation to great-circle arc", "unit": 1, "label": "Central angle", "input_unit": "degrees", "min": 0.1, "max": 12, "initial": 5, "output_unit": "km", "js_expression": "6371*x*Math.PI/180", "limitations": "Illustrative spherical approximation; not a high-accuracy ellipsoid geodesic."}, {"id": "east-offset", "title": "Small eastward offset", "unit": 2, "label": "Longitude separation", "input_unit": "degrees", "min": 0.001, "max": 0.25, "initial": 0.05, "output_unit": "km", "js_expression": "111.195*Math.cos(25*Math.PI/180)*x", "limitations": "Local spherical approximation at fixed latitude 25°; neglects ellipsoidal curvature."}, {"id": "grid-scale", "title": "Ground distance from mapped grid distance", "unit": 2, "label": "Grid distance", "input_unit": "m", "min": 20, "max": 2000, "initial": 800, "output_unit": "m", "js_expression": "x/0.9996", "limitations": "Hypothetical constant map scale 0.9996; no elevation factor or local distortion."}, {"id": "clock-range", "title": "Equivalent range error from receiver clock offset", "unit": 3, "label": "Clock bias", "input_unit": "ns", "min": 0, "max": 120, "initial": 15, "output_unit": "m", "js_expression": "0.299792458*x", "limitations": "Vacuum speed of light; clock effect shown before any GNSS correction."}, {"id": "iono-delay", "title": "First-order ionospheric group delay at L1", "unit": 3, "label": "Total electron content", "input_unit": "TECU", "min": 1, "max": 80, "initial": 15, "output_unit": "m", "js_expression": "40.3*x*1e16/(1575.42e6**2)", "limitations": "Vertical-equivalent first-order delay; slant geometry and higher-order effects omitted."}, {"id": "orthometric", "title": "Illustrative orthometric height", "unit": 4, "label": "Ellipsoidal height", "input_unit": "m", "min": -10, "max": 600, "initial": 120, "output_unit": "m", "js_expression": "x-27.6", "limitations": "Assumes fixed compatible geoid undulation of +27.6 m; not a geographic geoid lookup."}, {"id": "bouguer", "title": "Ideal slab gravity attraction", "unit": 4, "label": "Slab thickness", "input_unit": "m", "min": 1, "max": 1000, "initial": 200, "output_unit": "mGal", "js_expression": "2*Math.PI*6.67430e-11*2670*x*1e5", "limitations": "Infinite horizontal slab, density 2670 kg/m³; no terrain or regional corrections."}, {"id": "plate-motion", "title": "Projected displacement at fixed velocity", "unit": 5, "label": "Elapsed time", "input_unit": "years", "min": 0, "max": 45, "initial": 10, "output_unit": "mm", "js_expression": "8*x", "limitations": "Assumes constant eastward velocity 8 mm/year and no coseismic steps."}, {"id": "los", "title": "Radar line-of-sight displacement", "unit": 5, "label": "Unwrapped phase change", "input_unit": "rad", "min": -6.28, "max": 6.28, "initial": 1.57, "output_unit": "cm", "js_expression": "5.6*x/(4*Math.PI)", "limitations": "Assumes C-band radar wavelength 5.6 cm; sign convention is illustrative."}, {"id": "orbit-period", "title": "Ideal circular-orbit period", "unit": 6, "label": "Altitude above spherical Earth", "input_unit": "km", "min": 250, "max": 1400, "initial": 700, "output_unit": "minutes", "js_expression": "2*Math.PI*Math.sqrt((6371+x)**3/398600.4418)/60", "limitations": "Keplerian two-body circular orbit, μ=398600.4418 km³/s²; ignores J2 and drag."}, {"id": "ndvi", "title": "Normalized difference vegetation index", "unit": 6, "label": "NIR reflectance", "input_unit": "reflectance", "min": 0.05, "max": 0.9, "initial": 0.58, "output_unit": "index", "js_expression": "(x-0.14)/(x+0.14)", "limitations": "Fixed red reflectance 0.14; assumes atmospherically corrected surface reflectance."}, {"id": "insar", "title": "Line-of-sight displacement", "unit": 7, "label": "Unwrapped phase", "input_unit": "rad", "min": -6, "max": 6, "initial": 2, "output_unit": "cm", "js_expression": "5.6*x/(4*Math.PI)", "limitations": "Teaching geometry only: atmosphere, orbit, DEM and phase-unwrapping errors absent."}, {"id": "altimeter", "title": "Uncorrected range-derived surface height", "unit": 7, "label": "Measured range", "input_unit": "km", "min": 698, "max": 701, "initial": 699.86, "output_unit": "m", "js_expression": "(700-x)*1000", "limitations": "Illustrative nominal orbit radius offset: platform altitude 700 km; ignores corrections and datum."}, {"id": "rmse", "title": "Root-mean-square check-point error", "unit": 8, "label": "One affected point residual", "input_unit": "m", "min": 0, "max": 5, "initial": 1.2, "output_unit": "m", "js_expression": "Math.sqrt((0.2**2+0.4**2+0.3**2+x**2)/4)", "limitations": "Four synthetic horizontal check-point residual magnitudes; assumes comparable definition."}, {"id": "classifier-recall", "title": "Flood-detection recall", "unit": 8, "label": "Correct flood detections", "input_unit": "count", "min": 0, "max": 95, "initial": 72, "output_unit": "fraction", "js_expression": "x/(x+18)", "limitations": "Fixed 18 missed flooded pixels; this measures sensitivity, not overall accuracy."}];function val(m,x){let fn=new Function('x','return '+m.js_expression);return Number(fn(x));}function fmt(v){if(!Number.isFinite(v))return 'not defined';if(Math.abs(v)>0&&Math.abs(v)<0.0001)return v.toExponential(3);return Number(v.toPrecision(6)).toLocaleString('en-US',{maximumFractionDigits:6});}function plot(node,m,x){const n=70,values=[];for(let i=0;i<=n;i++){let z=m.min+(m.max-m.min)*i/n;values.push([z,val(m,z)]);}const ys=values.map(q=>q[1]).filter(Number.isFinite);if(!ys.length)return;const low=Math.min(...ys),high=Math.max(...ys),span=Math.max(1e-10,high-low),w=660,h=145,p=20;const points=values.map(([a,b])=>{const xx=p+(a-m.min)/(m.max-m.min)*(w-2*p);const yy=h-p-(b-low)/span*(h-2*p);return xx.toFixed(2)+','+yy.toFixed(2)}).join(' ');const xp=p+(x-m.min)/(m.max-m.min)*(w-2*p);const yp=h-p-(val(m,x)-low)/span*(h-2*p);node.innerHTML='<title>'+m.title+' calculated curve</title><path d="M20 15 V125 H640" fill="none" stroke="#9db3bf"/><polyline points="'+points+'" fill="none" stroke="#087e94" stroke-width="3"/><circle cx="'+xp+'" cy="'+yp+'" r="5" fill="#cb5a20"/>';node.setAttribute('aria-label',m.title+': curve from '+fmt(m.min)+' to '+fmt(m.max)+' '+m.input_unit+'. At '+fmt(x)+' output is '+fmt(val(m,x))+' '+m.output_unit+'.');}document.querySelectorAll('[data-model]').forEach(section=>{let m=models.find(o=>o.id===section.dataset.model);if(!m)return;const inp=section.querySelector('input'),out=section.querySelector('output'),chart=section.querySelector('svg');let update=()=>{let x=Number(inp.value);out.textContent=fmt(val(m,x))+' '+m.output_unit;plot(chart,m,x)};inp.addEventListener('input',update);update();});})();


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

