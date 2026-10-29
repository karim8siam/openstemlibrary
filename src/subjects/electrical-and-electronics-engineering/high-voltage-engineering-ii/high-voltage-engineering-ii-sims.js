/* High Voltage Engineering II Interactive Simulation Suite */
(function(window) {
  'use strict';

  var lin = function(a, b, n) {
    if (n === undefined) n = 160;
    return Array.from({length: n}, function(_, i) { return a + (b - a) * i / (n - 1); });
  };

  var unit = 1;

  function calc(a,b){let xs=[],ys=[],headline='',xl='',yl='',detail='';
if(unit===1){xs=lin(50,800);ys=xs.map(z=>90*(1+(z-a)/(z+a)));const g=(b-a)/(b+a);headline=`Γ=${g.toFixed(4)}; initial reflected=${(90*g).toFixed(2)} kV; transmitted=${(90*(1+g)).toFixed(2)} kV`;xl='Outgoing line impedance Z₂ (Ω)';yl='First transmitted step (kV)';detail='One discontinuity, incoming wave +90 kV';}
if(unit===2){xs=lin(0,60);ys=xs.map(i=>i*a);headline=`Tower voltage proxy=${(a*b).toFixed(1)} kV`;xl='Hypothetical current peak (kA)';yl='Ideal voltage proxy (kV)';detail='Frequency-independent effective impulse impedance';}
if(unit===3){xs=lin(0,1,200);let f=a*1000,tau=b/1000;ys=xs.map(t=>100*(1-Math.exp(-(t/1000)/tau)*Math.cos(2*Math.PI*f*(t/1000))));let peak=Math.max(...ys);headline=`Illustrative sampled peak=${peak.toFixed(1)} kV; final asymptote=100 kV`;xl='Time after interruption (ms)';yl='Modeled voltage (kV)';detail='Synthetic damped oscillator, 100 kV asymptote';}
if(unit===4){xs=lin(-2,2,160);ys=xs.map(logI=>b*Math.pow(Math.pow(10,logI),1/a));headline=`At I=10 kA: toy residual voltage=${(b*Math.pow(10,1/a)).toFixed(2)} kV`;xl='log₁₀(current/kA)';yl='Toy residual voltage (kV)';detail='Iref=1 kA, voltage ref set by slider';}
if(unit===5){xs=lin(.05,5);ys=xs.map(r=>b/(.001+.001*r)/1e3);let e1=b/(1+a),e2=a*e1;headline=`Layer 1=${e1.toFixed(3)} MV/m; layer 2=${e2.toFixed(3)} MV/m`;xl='Conductivity ratio σ₁/σ₂';yl='Steady E₁ (MV/m)';detail='Both layers 1 mm; DC voltage distributed via constant conductivities';}
if(unit===6){xs=lin(2,50);ys=xs.map(L=>2*L/(b*1e8)*1e6);headline=`One-way=${(a/(b*1e8)*1e6).toFixed(3)} µs; first round-trip echo=${(2*a/(b*1e8)*1e6).toFixed(3)} µs`;xl='Segment length (m)';yl='Round-trip time (µs)';detail='No attenuation, no multiple reflections';}
if(unit===7){xs=lin(.5,25);ys=xs.map(pct=>{let p=pct/100,se=a/100,sp=.95;return 100*se*p/(se*p+(1-sp)*(1-p))});let p=b/100,se=a/100,sp=.95;headline=`Positive predictive value=${(100*se*p/(se*p+(1-sp)*(1-p))).toFixed(1)}%`;xl='Prior fault prevalence (%)';yl='Posterior P(fault | alarm) (%)';detail='Specificity fixed at 95%, independent binary-classification event';}
if(unit===8){xs=lin(0,20);ys=xs.map(t=>100*(1-Math.exp(-a*t)));headline=`Probability of ≥1 event=${(100*(1-Math.exp(-a*b))).toFixed(2)}%`;xl='Exposure duration (years)';yl='Event probability (%)';detail='Constant hazard and stationary independent event model';}
return{xs,ys,headline,xl,yl,detail};}

  function makeSvgEl(tag, attrs) {
    var el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, k)) {
        el.setAttribute(k, String(attrs[k]));
      }
    }
    return el;
  }

  function renderHVE2Plot(plot, res) {
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
      stroke: '#087a9b',
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
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Traveling wave reflection at line junction" + '</h3><p>' + "Bewley lattice reflection \u0393 = (Z2 - Z1)/(Z2 + Z1) and refraction at line-cable boundary." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve2-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Performance</small><output id="out-metric-hve2-1">-</output></div>' +
          '<p class="note" id="out-detail-hve2-1">-</p></div>' +
          '<svg id="plot-hve2-1" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve2-1');
        var metricEl = card.querySelector('#out-metric-hve2-1');
        var detailEl = card.querySelector('#out-detail-hve2-1');
        var plotEl = card.querySelector('#plot-hve2-1');
        var cfgControls = [["Incoming line Z1 (\u03a9)", 100, 600, 350, 10], ["Outgoing line Z2 (\u03a9)", 20, 600, 50, 5]];
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
          unit = 1;
          var res = calc(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (detailEl) detailEl.textContent = 'Detail: ' + res.detail;
            if (plotEl) renderHVE2Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Lightning stroke tower top potential rise" + '</h3><p>' + "Direct stroke lightning surge current into tower surge impedance and footing resistance." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve2-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Performance</small><output id="out-metric-hve2-2">-</output></div>' +
          '<p class="note" id="out-detail-hve2-2">-</p></div>' +
          '<svg id="plot-hve2-2" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve2-2');
        var metricEl = card.querySelector('#out-metric-hve2-2');
        var detailEl = card.querySelector('#out-detail-hve2-2');
        var plotEl = card.querySelector('#plot-hve2-2');
        var cfgControls = [["Stroke current I (kA)", 10, 200, 60, 5], ["Footing resistance R (\u03a9)", 5, 50, 15, 1]];
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
          unit = 2;
          var res = calc(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (detailEl) detailEl.textContent = 'Detail: ' + res.detail;
            if (plotEl) renderHVE2Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "Transient recovery voltage (TRV) across breaker" + '</h3><p>' + "LC oscillation recovery voltage v(t) = V0\u00b7(1 - e^(-t/\u03c4)\u00b7cos(\u03c9_0 t)) following fault clearing." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve2-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Performance</small><output id="out-metric-hve2-3">-</output></div>' +
          '<p class="note" id="out-detail-hve2-3">-</p></div>' +
          '<svg id="plot-hve2-3" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve2-3');
        var metricEl = card.querySelector('#out-metric-hve2-3');
        var detailEl = card.querySelector('#out-detail-hve2-3');
        var plotEl = card.querySelector('#plot-hve2-3');
        var cfgControls = [["Natural frequency (kHz)", 1, 50, 15, 1], ["Damping time const (ms)", 0.05, 1.0, 0.2, 0.05]];
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
          unit = 3;
          var res = calc(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (detailEl) detailEl.textContent = 'Detail: ' + res.detail;
            if (plotEl) renderHVE2Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Metal-oxide surge arrester non-linear V-I curve" + '</h3><p>' + "Zinc-oxide (ZnO) varistor non-linear characteristic I = k\u00b7V^\u03b1 clamping overvoltages." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve2-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Performance</small><output id="out-metric-hve2-4">-</output></div>' +
          '<p class="note" id="out-detail-hve2-4">-</p></div>' +
          '<svg id="plot-hve2-4" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve2-4');
        var metricEl = card.querySelector('#out-metric-hve2-4');
        var detailEl = card.querySelector('#out-detail-hve2-4');
        var plotEl = card.querySelector('#plot-hve2-4');
        var cfgControls = [["Exponent alpha \u03b1", 20, 50, 35, 1], ["Reference voltage (kV)", 50, 300, 120, 5]];
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
          unit = 4;
          var res = calc(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (detailEl) detailEl.textContent = 'Detail: ' + res.detail;
            if (plotEl) renderHVE2Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Statistical insulation coordination and BIL margins" + '</h3><p>' + "Overvoltage probability density vs insulation breakdown cumulative Weibull distribution." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve2-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Performance</small><output id="out-metric-hve2-5">-</output></div>' +
          '<p class="note" id="out-detail-hve2-5">-</p></div>' +
          '<svg id="plot-hve2-5" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve2-5');
        var metricEl = card.querySelector('#out-metric-hve2-5');
        var detailEl = card.querySelector('#out-detail-hve2-5');
        var plotEl = card.querySelector('#plot-hve2-5');
        var cfgControls = [["Surge standard dev (kV)", 10, 100, 40, 5], ["Withstand BIL (kV)", 400, 1200, 750, 25]];
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
          unit = 5;
          var res = calc(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (detailEl) detailEl.textContent = 'Detail: ' + res.detail;
            if (plotEl) renderHVE2Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "High-voltage divider frequency response" + '</h3><p>' + "Mixed resistive-capacitive high-voltage divider compensation and step-response rise time." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve2-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Performance</small><output id="out-metric-hve2-6">-</output></div>' +
          '<p class="note" id="out-detail-hve2-6">-</p></div>' +
          '<svg id="plot-hve2-6" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve2-6');
        var metricEl = card.querySelector('#out-metric-hve2-6');
        var detailEl = card.querySelector('#out-detail-hve2-6');
        var plotEl = card.querySelector('#plot-hve2-6');
        var cfgControls = [["Divider ratio factor", 100, 5000, 1000, 50], ["Stray capacitance (pF)", 5, 100, 25, 2]];
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
          unit = 6;
          var res = calc(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (detailEl) detailEl.textContent = 'Detail: ' + res.detail;
            if (plotEl) renderHVE2Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Corona inception electric field gradient" + '</h3><p>' + "Peek empirical law for visual and disruptive corona inception gradient on stranded conductors." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve2-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Performance</small><output id="out-metric-hve2-7">-</output></div>' +
          '<p class="note" id="out-detail-hve2-7">-</p></div>' +
          '<svg id="plot-hve2-7" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve2-7');
        var metricEl = card.querySelector('#out-metric-hve2-7');
        var detailEl = card.querySelector('#out-detail-hve2-7');
        var plotEl = card.querySelector('#plot-hve2-7');
        var cfgControls = [["Conductor radius r (cm)", 0.5, 4.0, 1.5, 0.1], ["Air density factor \u03b4", 0.8, 1.1, 1.0, 0.02]];
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
          unit = 7;
          var res = calc(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (detailEl) detailEl.textContent = 'Detail: ' + res.detail;
            if (plotEl) renderHVE2Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Partial discharge apparent charge pulse" + '</h3><p>' + "Internal cavity partial discharge breakdown and void capacitive charge transfer \u0394q." + '</p></div>' +
          '<div class="sim-controls" id="controls-hve2-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Performance</small><output id="out-metric-hve2-8">-</output></div>' +
          '<p class="note" id="out-detail-hve2-8">-</p></div>' +
          '<svg id="plot-hve2-8" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-hve2-8');
        var metricEl = card.querySelector('#out-metric-hve2-8');
        var detailEl = card.querySelector('#out-detail-hve2-8');
        var plotEl = card.querySelector('#plot-hve2-8');
        var cfgControls = [["Cavity diameter (mm)", 0.1, 3.0, 0.8, 0.1], ["Applied electric stress (kV/mm)", 1, 15, 5, 0.5]];
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
          unit = 8;
          var res = calc(a, b);
          if (res) {
            if (metricEl) metricEl.textContent = res.headline;
            if (detailEl) detailEl.textContent = 'Detail: ' + res.detail;
            if (plotEl) renderHVE2Plot(plotEl, res);
          }
        }
        update();
      } catch (err) {
        console.warn('HVE2 init error:', err);
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
