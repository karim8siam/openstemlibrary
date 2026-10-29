/* Communication Systems I Interactive Simulation Suite */
(function(window) {
  'use strict';

  var fm = function(x, d) { return Number(x).toFixed(d === undefined ? 3 : d); };

  function erf(x) {
    var sign = x < 0 ? -1 : 1;
    x = Math.abs(x);
    var t = 1 / (1 + 0.3275911 * x);
    var y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x);
    return sign * y;
  }

  function Q(x) { return 0.5 * (1 - erf(x / Math.SQRT2)); }

  function calcComm1(unit, v) {
    var points = [], head = '';
    if (unit === 1) {
      var tx = v[0], R = v[1], f = v[2], nf = v[3];
      var floor = -174 + 10 * Math.log10(1e5) + nf;
      var fspl = function(r) { return 32.44 + 20 * Math.log10(f) + 20 * Math.log10(r / 1000); };
      var pr = tx - 2 - fspl(R);
      var snr = pr - floor;
      head = 'Received ' + fm(pr, 2) + ' dBm | Noise floor ' + fm(floor, 2) + ' dBm | SNR ' + fm(snr, 2) + ' dB';
      for (var x = 10; x <= 5000; x += 35) points.push({x: x, y: tx - 2 - fspl(x) - floor});
    } else if (unit === 2) {
      var f2 = v[0], fs2 = v[1], A2 = v[2];
      var folded = Math.abs(((f2 + fs2 / 2) % fs2 + fs2) % fs2 - fs2 / 2);
      head = 'Sampling f=' + fm(f2, 2) + ' kHz at fs=' + fm(fs2, 2) + ' kSa/s | Alias magnitude ' + fm(folded, 2) + ' kHz';
      for (var i = 0; i < 81; i++) points.push({x: i, y: A2 * Math.cos(2 * Math.PI * f2 * i / fs2)});
    } else if (unit === 3) {
      var mu = v[0], fm0 = v[1], fc = v[2];
      head = 'Modulation index μ=' + fm(mu, 2) + ' | Power ratio sideband/carrier=' + fm(mu * mu / 2, 3);
      for (var t3 = 0; t3 < 100; t3 += 0.25) {
        var env = 1 + mu * Math.cos(2 * Math.PI * fm0 * t3 / 100);
        points.push({x: t3, y: env * Math.cos(2 * Math.PI * fc * t3 / 100)});
      }
    } else if (unit === 4) {
      var df = v[0], fm4 = v[1], ptx = v[2];
      var beta = df / fm4;
      var carson = 2 * (df + fm4);
      head = 'Modulation index β=' + fm(beta, 2) + ' | Carson bandwidth B_T=' + fm(carson, 2) + ' kHz';
      for (var ff = -40; ff <= 40; ff += 0.5) {
        var mag4 = Math.exp(-Math.pow((ff / (df + 1e-6)), 2));
        points.push({x: ff, y: mag4 * ptx});
      }
    } else if (unit === 5) {
      var bits = v[0], Vpp = v[1], amp = v[2];
      var L5 = Math.pow(2, bits);
      var delta = Vpp / L5;
      var sqnr = 6.02 * bits + 1.76;
      head = 'Levels L=' + L5 + ' | Step Δ=' + fm(delta, 4) + ' V | Theoretical SQNR ≈ ' + fm(sqnr, 1) + ' dB';
      for (var t5 = 0; t5 <= 80; t5++) {
        var analog = (amp * Vpp / 2) * Math.sin(2 * Math.PI * t5 / 80);
        var qLevel = Math.round(analog / delta) * delta;
        points.push({x: t5, y: qLevel});
      }
    } else if (unit === 6) {
      var ebno_db = v[0], rate6 = v[1];
      var ebno_lin = Math.pow(10, ebno_db / 10);
      var ber = Q(Math.sqrt(2 * ebno_lin));
      head = 'Eb/N0 = ' + fm(ebno_db, 1) + ' dB | Theoretical BPSK BER ≈ ' + ber.toExponential(3);
      for (var eb = 0; eb <= 12; eb += 0.2) {
        var lin = Math.pow(10, eb / 10);
        points.push({x: eb, y: Math.max(-10, Math.log10(Math.max(1e-10, Q(Math.sqrt(2 * lin)))))});
      }
    } else if (unit === 7) {
      var bw = v[0], snr_db = v[1], margin = v[2];
      var snr_lin = Math.pow(10, (snr_db - margin) / 10);
      var cap = bw * Math.log2(1 + snr_lin);
      head = 'Shannon Capacity C = ' + fm(cap, 2) + ' kbps (BW=' + bw + ' kHz, SNR=' + snr_db + ' dB)';
      for (var s = -10; s <= 30; s += 0.5) {
        var slin = Math.pow(10, (s - margin) / 10);
        points.push({x: s, y: bw * Math.log2(1 + slin)});
      }
    } else if (unit === 8) {
      var phase_err = v[0], noise_std = v[1], syms = v[2];
      head = 'QPSK constellation: phase offset ' + fm(phase_err, 1) + '° | Gaussian noise σ=' + fm(noise_std, 2);
      var qConst = [[1, 1], [-1, 1], [-1, -1], [1, -1]];
      var phiRad = phase_err * Math.PI / 180;
      for (var si = 0; si < syms; si++) {
        var base = qConst[si % 4];
        var rotX = base[0] * Math.cos(phiRad) - base[1] * Math.sin(phiRad);
        var rotY = base[0] * Math.sin(phiRad) + base[1] * Math.cos(phiRad);
        var u1 = Math.max(1e-9, Math.random()), u2 = Math.random();
        var nX = noise_std * Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
        var nY = noise_std * Math.sqrt(-2 * Math.log(u1)) * Math.sin(2 * Math.PI * u2);
        points.push({x: rotX + nX, y: rotY + nY});
      }
    }
    return {points: points, head: head};
  }

  function renderComm1Plot(plot, cfg, res) {
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 340, L = 72, R = 20, T = 24, D = 48;
    var vals = res.points;
    if (vals.length === 0) return;
    var minx = Math.min.apply(null, vals.map(function(a) { return a.x; })), maxx = Math.max.apply(null, vals.map(function(a) { return a.x; }));
    var miny = Math.min.apply(null, vals.map(function(a) { return a.y; })), maxy = Math.max.apply(null, vals.map(function(a) { return a.y; }));
    if (cfg.unit === 8) { minx = -2.5; maxx = 2.5; miny = -2.5; maxy = 2.5; }
    if (maxy - miny < 1e-9) { miny -= 1; maxy += 1; }
    if (maxx - minx < 1e-9) { minx -= 1; maxx += 1; }
    var dy = maxy - miny;
    if (cfg.unit !== 8) { miny -= dy * 0.1; maxy += dy * 0.1; }

    var xx = function(x) { return L + (x - minx) / (maxx - minx) * (W - L - R); };
    var yy = function(y) { return H - D - (y - miny) / (maxy - miny) * (H - D - T); };

    for (var i = 0; i <= 4; i++) {
      var yv = miny + (maxy - miny) * i / 4;
      plot.appendChild(makeSvgEl('line', {x1: L, y1: yy(yv), x2: W - R, y2: yy(yv), stroke: '#e2e8f0'}));
      var yt = makeSvgEl('text', {x: L - 8, y: yy(yv) + 4, fill: '#64748b', 'text-anchor': 'end', 'font-size': 11});
      yt.textContent = cfg.unit === 6 ? '10^' + yv.toFixed(1) : yv.toFixed(2);
      plot.appendChild(yt);
    }
    for (var j = 0; j <= 5; j++) {
      var xv = minx + (maxx - minx) * j / 5;
      plot.appendChild(makeSvgEl('line', {x1: xx(xv), y1: T, x2: xx(xv), y2: H - D, stroke: '#f1f5f9'}));
      var xt = makeSvgEl('text', {x: xx(xv), y: H - D + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11});
      xt.textContent = xv.toFixed(1);
      plot.appendChild(xt);
    }

    if (cfg.unit === 8) {
      vals.forEach(function(p) {
        plot.appendChild(makeSvgEl('circle', {cx: xx(p.x), cy: yy(p.y), r: 2.5, fill: '#0a7fa2', opacity: 0.6}));
      });
    } else {
      var dStr = vals.map(function(a, idx) { return (idx ? 'L' : 'M') + xx(a.x).toFixed(1) + ' ' + yy(a.y).toFixed(1); }).join(' ');
      plot.appendChild(makeSvgEl('path', {d: dStr, fill: 'none', stroke: '#0a7190', 'stroke-width': 2.2, 'stroke-linecap': 'round'}));
    }

    var xl = makeSvgEl('text', {x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    xl.textContent = cfg.x || 'Parameter';
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {x: 16, y: (H - D + T) / 2, transform: 'rotate(-90 16 ' + ((H - D + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    yl.textContent = cfg.y || 'Response';
    plot.appendChild(yl);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Unit 1 \u00b7 Free-space link budget and receiver noise floor" + '</h3><p>' + "Fixed 0 dBi antenna gains, 2 dB combined feeder loss, 100 kHz noise bandwidth, and 290 K source temperature. Far-field free-space budget is not urban coverage prediction." + '</p></div>' +
          '<div class="sim-controls" id="controls-c1-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c1-1">-</output></div></div>' +
          '<svg id="plot-c1-1" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c1-1');
        var metricEl = card.querySelector('#out-metric-c1-1');
        var plotEl = card.querySelector('#plot-c1-1');
        var cfg = {"title": "Free-space link budget and receiver noise floor", "parameters": [["Tx power (dBm)", 15, -10, 35, 1], ["Range (m)", 300, 10, 5000, 10], ["Carrier (MHz)", 915, 100, 5800, 5], ["Receiver NF (dB)", 6, 0, 15, 0.5]], "x": "Range (m)", "y": "Received SNR (dB)", "help": "Fixed 0 dBi antenna gains, 2 dB combined feeder loss, 100 kHz noise bandwidth, and 290 K source temperature. Far-field free-space budget is not urban coverage prediction.", "unit": 1};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p[1];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p[2];
          inp.max = p[3];
          inp.step = p[4];
          inp.value = p[1];
          inp.setAttribute('aria-label', p[0]);
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcComm1(1, v);
          if (metricEl) metricEl.textContent = res.head;
          if (plotEl) renderComm1Plot(plotEl, cfg, res);
        }
        update();
      } catch (err) {
        console.warn('Comm1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Unit 2 \u00b7 Sampling, aliasing and frequency folding" + '</h3><p>' + "An ideal sinusoid is sampled uniformly. Input analog anti-alias filtering is intentionally omitted so you can observe the mathematical alias." + '</p></div>' +
          '<div class="sim-controls" id="controls-c1-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c1-2">-</output></div></div>' +
          '<svg id="plot-c1-2" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c1-2');
        var metricEl = card.querySelector('#out-metric-c1-2');
        var plotEl = card.querySelector('#plot-c1-2');
        var cfg = {"title": "Sampling, aliasing and frequency folding", "parameters": [["Analog tone (kHz)", 7, 0, 20, 0.25], ["Sample rate (kHz)", 10, 2, 40, 0.5], ["Signal amplitude", 1, 0.2, 2, 0.1]], "x": "Sample index", "y": "Sample value", "help": "An ideal sinusoid is sampled uniformly. Input analog anti-alias filtering is intentionally omitted so you can observe the mathematical alias.", "unit": 2};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p[1];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p[2];
          inp.max = p[3];
          inp.step = p[4];
          inp.value = p[1];
          inp.setAttribute('aria-label', p[0]);
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcComm1(2, v);
          if (metricEl) metricEl.textContent = res.head;
          if (plotEl) renderComm1Plot(plotEl, cfg, res);
        }
        update();
      } catch (err) {
        console.warn('Comm1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "Unit 3 \u00b7 AM modulation depth and envelope crossings" + '</h3><p>' + "Envelope is 1+\u03bc cos(2\u03c0fmt). When \u03bc exceeds 1, the envelope changes sign; a simple diode detector cannot reconstruct correctly." + '</p></div>' +
          '<div class="sim-controls" id="controls-c1-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c1-3">-</output></div></div>' +
          '<svg id="plot-c1-3" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c1-3');
        var metricEl = card.querySelector('#out-metric-c1-3');
        var plotEl = card.querySelector('#plot-c1-3');
        var cfg = {"title": "AM modulation depth and envelope crossings", "parameters": [["Modulation index \u03bc", 0.8, 0, 1.5, 0.05], ["Message frequency (kHz)", 2, 0.5, 8, 0.5], ["Carrier frequency (kHz)", 80, 20, 200, 5]], "x": "Message phase (cycles)", "y": "Signed amplitude envelope", "help": "Envelope is 1+\u03bc cos(2\u03c0fmt). When \u03bc exceeds 1, the envelope changes sign; a simple diode detector cannot reconstruct correctly.", "unit": 3};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p[1];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p[2];
          inp.max = p[3];
          inp.step = p[4];
          inp.value = p[1];
          inp.setAttribute('aria-label', p[0]);
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcComm1(3, v);
          if (metricEl) metricEl.textContent = res.head;
          if (plotEl) renderComm1Plot(plotEl, cfg, res);
        }
        update();
      } catch (err) {
        console.warn('Comm1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Unit 4 \u00b7 FM deviation, index and Carson bandwidth" + '</h3><p>' + "For single-tone FM, the plotted frequency offset is \u0394f cos(2\u03c0fmt); Carson bandwidth is a planning approximation, not a hard spectral edge." + '</p></div>' +
          '<div class="sim-controls" id="controls-c1-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c1-4">-</output></div></div>' +
          '<svg id="plot-c1-4" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c1-4');
        var metricEl = card.querySelector('#out-metric-c1-4');
        var plotEl = card.querySelector('#plot-c1-4');
        var cfg = {"title": "FM deviation, index and Carson bandwidth", "parameters": [["Peak deviation (kHz)", 12, 0, 100, 1], ["Message frequency (kHz)", 3, 0.5, 15, 0.5], ["Carrier frequency (MHz)", 100, 1, 200, 1]], "x": "Message phase (cycles)", "y": "Instantaneous frequency offset (kHz)", "help": "For single-tone FM, the plotted frequency offset is \u0394f cos(2\u03c0fmt); Carson bandwidth is a planning approximation, not a hard spectral edge.", "unit": 4};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p[1];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p[2];
          inp.max = p[3];
          inp.step = p[4];
          inp.value = p[1];
          inp.setAttribute('aria-label', p[0]);
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcComm1(4, v);
          if (metricEl) metricEl.textContent = res.head;
          if (plotEl) renderComm1Plot(plotEl, cfg, res);
        }
        update();
      } catch (err) {
        console.warn('Comm1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Unit 5 \u00b7 Uniform quantization and step size" + '</h3><p>' + "Midrise uniform quantizer with range [-1,+1) volts and no additive dither or saturation recovery. Ideal SQNR expression assumes full-scale sine." + '</p></div>' +
          '<div class="sim-controls" id="controls-c1-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c1-5">-</output></div></div>' +
          '<svg id="plot-c1-5" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c1-5');
        var metricEl = card.querySelector('#out-metric-c1-5');
        var plotEl = card.querySelector('#plot-c1-5');
        var cfg = {"title": "Uniform quantization and step size", "parameters": [["Bits per sample", 5, 2, 12, 1], ["Sine amplitude (V)", 0.85, 0.05, 1, 0.05], ["Input offset (V)", 0, -0.5, 0.5, 0.05]], "x": "Sample phase (cycles)", "y": "Quantized voltage (V)", "help": "Midrise uniform quantizer with range [-1,+1) volts and no additive dither or saturation recovery. Ideal SQNR expression assumes full-scale sine.", "unit": 5};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p[1];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p[2];
          inp.max = p[3];
          inp.step = p[4];
          inp.value = p[1];
          inp.setAttribute('aria-label', p[0]);
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcComm1(5, v);
          if (metricEl) metricEl.textContent = res.head;
          if (plotEl) renderComm1Plot(plotEl, cfg, res);
        }
        update();
      } catch (err) {
        console.warn('Comm1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "Unit 6 \u00b7 Coherent BPSK AWGN error probability" + '</h3><p>' + "The plot is the exact ideal formula Q(sqrt(2Eb/N0)) evaluated numerically, not a random trial. Expected count is N times probability, not an observed error count." + '</p></div>' +
          '<div class="sim-controls" id="controls-c1-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c1-6">-</output></div></div>' +
          '<svg id="plot-c1-6" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c1-6');
        var metricEl = card.querySelector('#out-metric-c1-6');
        var plotEl = card.querySelector('#plot-c1-6');
        var cfg = {"title": "Coherent BPSK AWGN error probability", "parameters": [["Eb/N0 (dB)", 6, -3, 14, 0.5], ["Trials for expectation", 100000, 1000, 500000, 1000]], "x": "Eb/N0 (dB)", "y": "Bit error probability (log scale)", "help": "The plot is the exact ideal formula Q(sqrt(2Eb/N0)) evaluated numerically, not a random trial. Expected count is N times probability, not an observed error count.", "unit": 6};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p[1];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p[2];
          inp.max = p[3];
          inp.step = p[4];
          inp.value = p[1];
          inp.setAttribute('aria-label', p[0]);
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcComm1(6, v);
          if (metricEl) metricEl.textContent = res.head;
          if (plotEl) renderComm1Plot(plotEl, cfg, res);
        }
        update();
      } catch (err) {
        console.warn('Comm1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Unit 7 \u00b7 AWGN channel capacity versus SNR" + '</h3><p>' + "Shannon\u2013Hartley model assumes an ideal bandlimited AWGN channel with appropriate coding. Payload efficiency is a separate illustrative overhead factor." + '</p></div>' +
          '<div class="sim-controls" id="controls-c1-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c1-7">-</output></div></div>' +
          '<svg id="plot-c1-7" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c1-7');
        var metricEl = card.querySelector('#out-metric-c1-7');
        var plotEl = card.querySelector('#plot-c1-7');
        var cfg = {"title": "AWGN channel capacity versus SNR", "parameters": [["Bandwidth (MHz)", 1, 0.05, 10, 0.05], ["SNR (dB)", 15, -10, 40, 1], ["Payload efficiency (%)", 75, 20, 100, 5]], "x": "SNR (dB)", "y": "Capacity (Mbit/s)", "help": "Shannon\u2013Hartley model assumes an ideal bandlimited AWGN channel with appropriate coding. Payload efficiency is a separate illustrative overhead factor.", "unit": 7};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p[1];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p[2];
          inp.max = p[3];
          inp.step = p[4];
          inp.value = p[1];
          inp.setAttribute('aria-label', p[0]);
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcComm1(7, v);
          if (metricEl) metricEl.textContent = res.head;
          if (plotEl) renderComm1Plot(plotEl, cfg, res);
        }
        update();
      } catch (err) {
        console.warn('Comm1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Unit 8 \u00b7 QPSK constellation with phase error and noise" + '</h3><p>' + "The points are synthetic samples around QPSK constellation locations. Phase rotates all four clusters; Gaussian-like deterministic pseudo-noise broadens them." + '</p></div>' +
          '<div class="sim-controls" id="controls-c1-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c1-8">-</output></div></div>' +
          '<svg id="plot-c1-8" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c1-8');
        var metricEl = card.querySelector('#out-metric-c1-8');
        var plotEl = card.querySelector('#plot-c1-8');
        var cfg = {"title": "QPSK constellation with phase error and noise", "parameters": [["Phase rotation (degrees)", 20, -90, 90, 1], ["Noise std per axis", 0.18, 0, 0.8, 0.01], ["Points per symbol", 25, 5, 80, 1]], "x": "In-phase coordinate", "y": "Quadrature coordinate", "help": "The points are synthetic samples around QPSK constellation locations. Phase rotates all four clusters; Gaussian-like deterministic pseudo-noise broadens them.", "unit": 8};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p[1];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p[2];
          inp.max = p[3];
          inp.step = p[4];
          inp.value = p[1];
          inp.setAttribute('aria-label', p[0]);
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcComm1(8, v);
          if (metricEl) metricEl.textContent = res.head;
          if (plotEl) renderComm1Plot(plotEl, cfg, res);
        }
        update();
      } catch (err) {
        console.warn('Comm1 init error:', err);
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
