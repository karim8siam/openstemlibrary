/* High Voltage Engineering I Interactive Simulation Suite */
(function(window) {
  'use strict';

  var lin = function(a, b, n) {
    if (n === undefined) n = 130;
    return Array.from({length: n}, function(_, i) { return a + (b - a) * i / (n - 1); });
  };

  var paschen = function(pd, g) {
    var den = Math.log(15 * pd) - Math.log(Math.log(1 + 1 / g));
    return den > 0 ? 365 * pd / den : NaN;
  };

  var idx = 1;

  function calculate(a,b){let xs,ys,headline='',xl='',yl='',valid='';
if(idx===1){let v=a*1000,inner=b/1000,outer=.020;xs=lin(inner,outer);ys=xs.map(r=>v/(r*Math.log(outer/inner))/1e6);headline='Maximum radial field: '+ys[0].toFixed(3)+' MV/m';xl='radius (mm)';yl='E (MV/m)';xs=xs.map(x=>x*1000);valid='a < b, long coax, uniform dielectric';}
if(idx===2){let pd=Math.pow(10,a),g=b;xs=lin(-.3,2.5).map(v=>Math.pow(10,v));ys=xs.map(p=>paschen(p,g));headline='Modeled breakdown at p·d='+pd.toFixed(3)+' torr·cm: '+(Number.isFinite(paschen(pd,g))?paschen(pd,g).toFixed(0)+' V':'outside positive denominator');xl='p·d (torr·cm; nonlinear spacing)';yl='model Vb (V)';xs=xs.map(x=>Math.log10(x));ys=ys.map(y=>Number.isFinite(y)&&y<30000?y:null);valid='empirical curve only; no physical withstand guarantee';}
if(idx===3){xs=lin(10,500);ys=xs.map(f=>2*Math.PI*f*2e-9*1000*1000*a*1000);headline='At selected f: '+(2*Math.PI*b*2e-9*1e6*a*1000).toFixed(3)+' mW';xl='frequency (Hz)';yl='dielectric loss (mW)';valid='constant capacitance, fixed RMS voltage and tanδ';}
if(idx===4){const alpha=1/a,beta=1/b,peakTime=Math.log(beta/alpha)/(beta-alpha),peak=Math.exp(-alpha*peakTime)-Math.exp(-beta*peakTime);xs=lin(0,150);ys=xs.map(t=>100*(Math.exp(-alpha*t)-Math.exp(-beta*t))/peak);headline='Peak time: '+peakTime.toFixed(3)+' µs (not standardized front time)';xl='time (µs)';yl='normalized amplitude (%)';valid='mathematical double exponential with synthetic parameters';}
if(idx===5){xs=lin(50,1000);ys=xs.map(z=>(z-300)/(z+300)*b);const g=(a-300)/(a+300);headline='Reflection coefficient: '+g.toFixed(4)+'; reflected: '+(g*b).toFixed(3)+' kV; initial transmitted: '+((1+g)*b).toFixed(3)+' kV';xl='ZL (Ω)';yl='reflected voltage (kV)';valid='one lossless interface; first arrival only';}
if(idx===6){xs=lin(.1,50);ys=xs.map(r=>{const r2=b*1000,rin=r*1e6,x=r2*rin/(r2+rin);return 100*x/(9e6+x)});const r2=b*1000,rin=a*1e6,re=r2*rin/(r2+rin);headline='Loaded output ratio: '+(re/(9e6+re)).toFixed(6);xl='instrument Rin (MΩ)';yl='output (% input)';valid='DC equivalent, not impulse-calibrated';}
if(idx===7){xs=lin(0,360,240);ys=xs.map((x,i)=>2+11*Math.pow(Math.sin((x+b)*Math.PI/180),2)+2*Math.sin(i*8.73));const ct=ys.filter(v=>v>a).length;headline='Synthetic points above threshold: '+ct+'/'+ys.length;xl='phase angle (degrees)';yl='synthetic event amplitude';valid='not diagnostic data; threshold and phase shift are hypothetical';}
if(idx===8){xs=lin(1,2);ys=xs.map(f=>b*f);headline='At chosen factor: '+(a*b).toFixed(3)+' MV/m modeled peak';xl='geometry stress multiplier';yl='peak field (MV/m)';valid='no qualified material limit or failure probability supplied';}
return{xs,ys,headline,xl,yl,valid};}

  function makeSvgEl(tag, attrs) {
    var el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, k)) {
        el.setAttribute(k, String(attrs[k]));
      }
    }
    return el;
  }

  function renderHVE1Plot(plot, res) {
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 320, L = 72, R = 20, T = 20, B = 48;
    var xs = res.xs, ys = res.ys;
    var validPts = [];
    for (var k = 0; k < xs.length; k++) {
      if (Number.isFinite(xs[k]) && Number.isFinite(ys[k])) validPts.push([xs[k], ys[k]]);
    }
    if (validPts.length === 0) return;
    var pXs = validPts.map(function(p) { return p[0]; }), pYs = validPts.map(function(p) { return p[1]; });
    var xmin = Math.min.apply(null, pXs), xmax = Math.max.apply(null, pXs);
    var ymin = Math.min.apply(null, pYs), ymax = Math.max.apply(null, pYs);
    if (ymax === ymin) { ymax += 1; ymin -= 1; }
    else { var pad = (ymax - ymin) * 0.1; ymin -= pad; ymax += pad; }
    if (xmax === xmin) xmax = xmin + 1;

    var px = function(x) { return L + (W - L - R) * (x - xmin) / (xmax - xmin); };
    var py = function(y) { return T + (H - T - B) * (ymax - y) / (ymax - ymin); };

    for (var i = 0; i <= 4; i++) {
      var gy = T + i * (H - T - B) / 4;
      var yv = ymax - i * (ymax - ymin) / 4;
      plot.appendChild(makeSvgEl('line', {x1: L, y1: gy, x2: W - R, y2: gy, stroke: '#e2e8f0'}));
      var yt = makeSvgEl('text', {x: L - 8, y: gy + 4, fill: '#64748b', 'text-anchor': 'end', 'font-size': 11});
      yt.textContent = yv.toPrecision(3);
      plot.appendChild(yt);
    }
    for (var j = 0; j <= 5; j++) {
      var gx = L + j * (W - L - R) / 5;
      var xv = xmin + j * (xmax - xmin) / 5;
      plot.appendChild(makeSvgEl('line', {x1: gx, y1: T, x2: gx, y2: H - B, stroke: '#f1f5f9'}));
      var xt = makeSvgEl('text', {x: gx, y: H - B + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11});
      xt.textContent = xv.toPrecision(3);
      plot.appendChild(xt);
    }

    var ptsStr = validPts.map(function(p) { return px(p[0]).toFixed(1) + ',' + py(p[1]).toFixed(1); }).join(' ');
    plot.appendChild(makeSvgEl('polyline', {
      points: ptsStr,
      fill: 'none',
      stroke: '#0284c7',
      'stroke-width': 2.5,
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round'
    }));

    var xl = makeSvgEl('text', {x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    xl.textContent = res.xl || 'Parameter';
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {x: 16, y: (H - B + T) / 2, transform: 'rotate(-90 16 ' + ((H - B + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    yl.textContent = res.yl || 'Response';
    plot.appendChild(yl);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Coaxial electrode electric field distribution" + '</h3><p>' + "Radial electric field stress E(r) = V / (r\u00b7ln(b/a)) and maximum surface gradient at inner conductor." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve1-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Stress & Rating</small><output id="out-metric-hve1-1">-</output></div>' +
          '<p class="note" id="out-valid-hve1-1">-</p></div>' +
          '<svg id="plot-hve1-1" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve1-1');
        var metricEl = card.querySelector('#out-metric-hve1-1');
        var validEl = card.querySelector('#out-valid-hve1-1');
        var plotEl = card.querySelector('#plot-hve1-1');
        var cfgControls = [["Applied voltage V (kV)", 10, 200, 100, 5], ["Inner radius a (mm)", 1, 10, 4, 0.5]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          idx = 1;
          var res = calculate(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (validEl) validEl.textContent = 'Assumptions: ' + res.valid;
            if (plotEl) renderHVE1Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Paschen curve for gaseous dielectric breakdown" + '</h3><p>' + "Breakdown voltage V_b versus pressure-distance product p\u00b7d in uniform fields." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve1-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Stress & Rating</small><output id="out-metric-hve1-2">-</output></div>' +
          '<p class="note" id="out-valid-hve1-2">-</p></div>' +
          '<svg id="plot-hve1-2" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve1-2');
        var metricEl = card.querySelector('#out-metric-hve1-2');
        var validEl = card.querySelector('#out-valid-hve1-2');
        var plotEl = card.querySelector('#plot-hve1-2');
        var cfgControls = [["Log10(p\u00b7d) (torr\u00b7cm)", -0.3, 2.5, 0.8, 0.05], ["Second coefficient \u03b3", 0.001, 0.1, 0.02, 0.005]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          idx = 2;
          var res = calculate(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (validEl) validEl.textContent = 'Assumptions: ' + res.valid;
            if (plotEl) renderHVE1Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "Liquid dielectric dielectric loss and dissipation" + '</h3><p>' + "Dielectric power loss P = 2\u03c0 f C V\u00b2 tan \u03b4 across frequency in insulating oil." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve1-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Stress & Rating</small><output id="out-metric-hve1-3">-</output></div>' +
          '<p class="note" id="out-valid-hve1-3">-</p></div>' +
          '<svg id="plot-hve1-3" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve1-3');
        var metricEl = card.querySelector('#out-metric-hve1-3');
        var validEl = card.querySelector('#out-valid-hve1-3');
        var plotEl = card.querySelector('#plot-hve1-3');
        var cfgControls = [["Tan delta dissipation", 0.001, 0.05, 0.005, 0.001], ["Frequency f (Hz)", 10, 500, 50, 10]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          idx = 3;
          var res = calculate(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (validEl) validEl.textContent = 'Assumptions: ' + res.valid;
            if (plotEl) renderHVE1Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Solid insulation electromechanical breakdown" + '</h3><p>' + "Stark-Garton electrostatic compressive stress vs elastic modulus and critical field." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve1-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Stress & Rating</small><output id="out-metric-hve1-4">-</output></div>' +
          '<p class="note" id="out-valid-hve1-4">-</p></div>' +
          '<svg id="plot-hve1-4" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve1-4');
        var metricEl = card.querySelector('#out-metric-hve1-4');
        var validEl = card.querySelector('#out-valid-hve1-4');
        var plotEl = card.querySelector('#plot-hve1-4');
        var cfgControls = [["Young modulus Y (MPa)", 100, 5000, 1000, 50], ["Thickness d (mm)", 0.1, 5.0, 1.0, 0.1]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          idx = 4;
          var res = calculate(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (validEl) validEl.textContent = 'Assumptions: ' + res.valid;
            if (plotEl) renderHVE1Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Cockcroft-Walton multi-stage voltage multiplier" + '</h3><p>' + "Output DC voltage, regulation drop \u0394V = I/(f\u00b7C)\u00b7(2n\u00b3/3 + n\u00b2/2), and stage ripple." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve1-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Stress & Rating</small><output id="out-metric-hve1-5">-</output></div>' +
          '<p class="note" id="out-valid-hve1-5">-</p></div>' +
          '<svg id="plot-hve1-5" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve1-5');
        var metricEl = card.querySelector('#out-metric-hve1-5');
        var validEl = card.querySelector('#out-valid-hve1-5');
        var plotEl = card.querySelector('#plot-hve1-5');
        var cfgControls = [["Stage count n", 2, 12, 6, 1], ["Load current I (mA)", 0.1, 10, 2, 0.1]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          idx = 5;
          var res = calculate(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (validEl) validEl.textContent = 'Assumptions: ' + res.valid;
            if (plotEl) renderHVE1Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "Series resonant test transformer tuning" + '</h3><p>' + "Variable-inductance series resonance tuning and test specimen capacitive quality factor Q." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve1-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Stress & Rating</small><output id="out-metric-hve1-6">-</output></div>' +
          '<p class="note" id="out-valid-hve1-6">-</p></div>' +
          '<svg id="plot-hve1-6" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve1-6');
        var metricEl = card.querySelector('#out-metric-hve1-6');
        var validEl = card.querySelector('#out-valid-hve1-6');
        var plotEl = card.querySelector('#plot-hve1-6');
        var cfgControls = [["Test specimen C (nF)", 1, 50, 10, 1], ["Resonance tuning L (H)", 1, 50, 25, 1]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          idx = 6;
          var res = calculate(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (validEl) validEl.textContent = 'Assumptions: ' + res.valid;
            if (plotEl) renderHVE1Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Standard 1.2/50 \u00b5s impulse waveform shaping" + '</h3><p>' + "Double-exponential lightning impulse wave: V(t) = V0\u00b7(e^(-\u03b1 t) - e^(-\u03b2 t))." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve1-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Stress & Rating</small><output id="out-metric-hve1-7">-</output></div>' +
          '<p class="note" id="out-valid-hve1-7">-</p></div>' +
          '<svg id="plot-hve1-7" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve1-7');
        var metricEl = card.querySelector('#out-metric-hve1-7');
        var validEl = card.querySelector('#out-valid-hve1-7');
        var plotEl = card.querySelector('#plot-hve1-7');
        var cfgControls = [["Wavefront resistor R1 (\u03a9)", 50, 500, 150, 10], ["Wavetail resistor R2 (\u03a9)", 500, 5000, 2000, 50]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          idx = 7;
          var res = calculate(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (validEl) validEl.textContent = 'Assumptions: ' + res.valid;
            if (plotEl) renderHVE1Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Multi-stage Marx impulse generator discharge" + '</h3><p>' + "Parallel charging at V0 and spark-gap series discharge into capacitive divider burden." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve1-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Stress & Rating</small><output id="out-metric-hve1-8">-</output></div>' +
          '<p class="note" id="out-valid-hve1-8">-</p></div>' +
          '<svg id="plot-hve1-8" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve1-8');
        var metricEl = card.querySelector('#out-metric-hve1-8');
        var validEl = card.querySelector('#out-valid-hve1-8');
        var plotEl = card.querySelector('#plot-hve1-8');
        var cfgControls = [["Marx stages n", 2, 16, 8, 1], ["Stage charging V0 (kV)", 20, 100, 50, 5]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          idx = 8;
          var res = calculate(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (validEl) validEl.textContent = 'Assumptions: ' + res.valid;
            if (plotEl) renderHVE1Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE1 init error:', err);
      }
    }
  });

  if (!window.SimulationEngine) window.SimulationEngine = {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId || 'sim-container');
    if (!container) return;
    container.innerHTML = '';
    var unitNum = 1;
    if (simType) {
      var m = simType.match(/(\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    } else {
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {
        var pMatch = window.location.pathname.match(/chapter-(\d+)/);
        if (pMatch) unitNum = parseInt(pMatch[1], 10);
      }
    }
    if (isNaN(unitNum) || unitNum < 1 || unitNum > 8) unitNum = 1;
    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 1);
    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'eee-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    });
  };

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
      });
    } else {
      if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
