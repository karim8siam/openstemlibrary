/* Planetary Science Interactive Simulation Suite */
(()=>{'use strict';const MODELS=[{"id": "temperature-disk", "unit": 1, "name": "Disk irradiation temperature (toy model)", "label": "Distance from Sun", "input_unit": "AU", "min": 0.3, "max": 10, "initial": 2, "output_unit": "K", "expression": "278/Math.sqrt(x)", "note": "Assumes sunlight heating with a fixed 278 K normalization; ignores pressure, opacity, disk viscous heating and varying albedo."}, {"id": "orbital-years", "unit": 1, "name": "Solar two-body orbital period", "label": "Semimajor axis", "input_unit": "AU", "min": 0.25, "max": 20, "initial": 5.2, "output_unit": "years", "expression": "Math.sqrt(x*x*x)", "note": "Negligible-mass Keplerian orbit about the Sun with a measured-year scaling; not a full perturbation ephemeris."}, {"id": "surface-g", "unit": 2, "name": "Surface gravity: mass scaling", "label": "Mass", "input_unit": "Earth masses", "min": 0.1, "max": 8, "initial": 1, "output_unit": "m/s\u00b2", "expression": "9.81*x", "note": "Radius held fixed at one Earth radius. True planetary mass\u2013radius relations do not keep radius fixed."}, {"id": "escape-v", "unit": 2, "name": "Escape speed: mass scaling", "label": "Mass", "input_unit": "Earth masses", "min": 0.1, "max": 8, "initial": 1, "output_unit": "km/s", "expression": "11.186*Math.sqrt(x)", "note": "Radius fixed at one Earth radius and a nonrotating spherical field; not a prediction of atmospheric loss."}, {"id": "crater-density", "unit": 3, "name": "Crater surface density", "label": "Count of craters", "input_unit": "count", "min": 2, "max": 200, "initial": 50, "output_unit": "per 10\u2076 km\u00b2", "expression": "1000000*x/25000", "note": "Fixed mapped area 25,000 km\u00b2 with a uniform detection threshold. Crater density alone is not an absolute age."}, {"id": "band-depth", "unit": 3, "name": "Spectral absorption band depth", "label": "Band reflectance", "input_unit": "reflectance", "min": 0.05, "max": 0.8, "initial": 0.38, "output_unit": "fraction", "expression": "1-x/0.8", "note": "Continuum reflectance fixed at 0.8; assumes proper radiometric calibration and comparable geometry."}, {"id": "energy-balance", "unit": 4, "name": "Airless effective temperature", "label": "Sun distance", "input_unit": "AU", "min": 0.35, "max": 10, "initial": 1, "output_unit": "K", "expression": "Math.pow((0.7*1361)/(4*5.670374419e-8*x*x),0.25)", "note": "Bond albedo 0.30, isotropic emission, no atmosphere and constant solar luminosity."}, {"id": "scale-height", "unit": 4, "name": "Ideal atmospheric scale height", "label": "Temperature", "input_unit": "K", "min": 100, "max": 550, "initial": 240, "output_unit": "km", "expression": "8.314462618*x/(0.028*9.81)/1000", "note": "Isothermal nitrogen-dominated ideal gas with mean molecular mass 28 g/mol and g = 9.81 m/s\u00b2."}, {"id": "ice-flux", "unit": 5, "name": "Conductive heat flux through ice", "label": "Shell thickness", "input_unit": "km", "min": 1, "max": 90, "initial": 20, "output_unit": "W/m\u00b2", "expression": "2.2*110/(x*1000)", "note": "Constant conductivity 2.2 W/(m K), fixed temperature contrast 110 K, one-dimensional steady conduction."}, {"id": "ocean-pressure", "unit": 5, "name": "Pressure increase beneath liquid", "label": "Liquid depth", "input_unit": "km", "min": 0.5, "max": 80, "initial": 20, "output_unit": "MPa", "expression": "1000*1.32*(x*1000)/1e6", "note": "Constant density 1000 kg/m\u00b3, acceleration 1.32 m/s\u00b2; ignores compression and depth-variable gravity."}, {"id": "coriolis", "unit": 6, "name": "Coriolis parameter on a rotating giant", "label": "Latitude", "input_unit": "degrees", "min": -85, "max": 85, "initial": 35, "output_unit": "s\u207b\u00b9", "expression": "2*(2*Math.PI/(10*3600))*Math.sin(x*Math.PI/180)", "note": "Fixed 10-hour rotation period. Simplified spherical planetary atmosphere and local f-plane argument."}, {"id": "ring-roche", "unit": 6, "name": "Fluid Roche limit from primary center", "label": "Satellite density", "input_unit": "kg/m\u00b3", "min": 500, "max": 3500, "initial": 1200, "output_unit": "km", "expression": "2.44*60000*Math.cbrt(1300/x)", "note": "Fluid-satellite approximation with primary radius 60,000 km and density 1,300 kg/m\u00b3; no particle strength."}, {"id": "impact-energy", "unit": 7, "name": "Kinetic impact energy", "label": "Projectile diameter", "input_unit": "m", "min": 2, "max": 160, "initial": 30, "output_unit": "J", "expression": "0.5*(4/3)*Math.PI*Math.pow(x/2,3)*2700*Math.pow(20000,2)", "note": "Solid sphere with density 2,700 kg/m\u00b3 and 20 km/s speed. Does not predict cratering or ground damage."}, {"id": "comet-solar-flux", "unit": 7, "name": "Solar irradiance at an active small body", "label": "Heliocentric distance", "input_unit": "AU", "min": 0.5, "max": 15, "initial": 3, "output_unit": "W/m\u00b2", "expression": "1361/(x*x)", "note": "Inverse-square irradiance; no thermal inertia, gas activity, orientation or self-shadowing."}, {"id": "spectral-res", "unit": 8, "name": "Spectral resolving power", "label": "Spectral bin width", "input_unit": "nm", "min": 0.2, "max": 15, "initial": 2, "output_unit": "\u03bb/\u0394\u03bb", "expression": "1000/x", "note": "Nominal wavelength fixed at 1,000 nm; instrumental line-spread function omitted."}, {"id": "photon-snr", "unit": 8, "name": "Shot-noise-limited signal-to-noise", "label": "Detected photoelectrons", "input_unit": "count", "min": 100, "max": 50000, "initial": 5000, "output_unit": "SNR", "expression": "Math.sqrt(x)", "note": "Poisson counting only, ignoring detector read noise, dark current, background and systematics."}];
const compute=(s,x)=>{switch(s){case "temperature-disk":return 278/Math.sqrt(x);case "orbital-years":return Math.sqrt(x*x*x);case "surface-g":return 9.81*x;case "escape-v":return 11.186*Math.sqrt(x);case "crater-density":return 1000000*x/25000;case "band-depth":return 1-x/0.8;case "energy-balance":return Math.pow((0.7*1361)/(4*5.670374419e-8*x*x),0.25);case "scale-height":return 8.314462618*x/(0.028*9.81)/1000;case "ice-flux":return 2.2*110/(x*1000);case "ocean-pressure":return 1000*1.32*(x*1000)/1e6;case "coriolis":return 2*(2*Math.PI/(10*3600))*Math.sin(x*Math.PI/180);case "ring-roche":return 2.44*60000*Math.cbrt(1300/x);case "impact-energy":return 0.5*(4/3)*Math.PI*Math.pow(x/2,3)*2700*Math.pow(20000,2);case "comet-solar-flux":return 1361/(x*x);case "spectral-res":return 1000/x;case "photon-snr":return Math.sqrt(x); default:throw new Error('Unsupported model '+s)}};
const pretty=x=>Number.isFinite(x)? (Math.abs(x)>1e7||Math.abs(x)<1e-4&&x!==0?x.toExponential(4):x.toLocaleString('en-US',{maximumSignificantDigits:6})):'out of range';
for(const section of document.querySelectorAll('section.model')){const key=section.dataset.model;const m=MODELS.find(v=>v.id===key);if(!m)continue;const input=section.querySelector('input');const output=section.querySelector('output');const plot=section.querySelector('svg');
function update(){const x=Number(input.value);let y=compute(key,x);output.textContent=pretty(y)+' '+m.output_unit;output.value=pretty(y);const pts=[];let lo=Infinity,hi=-Infinity;for(let i=0;i<=80;i++){const xx=m.min+(m.max-m.min)*i/80;const yy=compute(key,xx);if(!Number.isFinite(yy))continue;pts.push([xx,yy]);lo=Math.min(lo,yy);hi=Math.max(hi,yy)}const span=hi-lo||1;const coords=pts.map(([xx,yy])=>[(xx-m.min)/(m.max-m.min)*440+38,142-(yy-lo)/span*114]);const poly=coords.map(([a,b])=>a.toFixed(2)+','+b.toFixed(2)).join(' ');const cx=((x-m.min)/(m.max-m.min)*440+38).toFixed(2);const cy=(142-(y-lo)/span*114).toFixed(2);plot.innerHTML='<line x1="38" y1="142" x2="478" y2="142" stroke="#a2bac7"/><line x1="38" y1="15" x2="38" y2="142" stroke="#a2bac7"/><polyline fill="none" stroke="#137591" stroke-width="3" points="'+poly+'"/><circle cx="'+cx+'" cy="'+cy+'" r="5" fill="#b84b25"/><text x="40" y="165" fill="#39566c" font-size="12">'+m.min+' '+m.input_unit+'</text><text x="370" y="165" fill="#39566c" font-size="12">'+m.max+' '+m.input_unit+'</text>';plot.setAttribute('aria-label','Model relationship: current '+pretty(x)+' '+m.input_unit+' corresponds to '+pretty(y)+' '+m.output_unit);}
input.addEventListener('input',update);update();}}
)();


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

