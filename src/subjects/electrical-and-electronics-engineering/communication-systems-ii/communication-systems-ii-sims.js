/* Communication Systems II Interactive Simulation Suite */
(function(window) {
  'use strict';

  var fmt = function(x, n) { return Number(x).toFixed(n === undefined ? 4 : n); };

  function erf(x) {
    var sign = x < 0 ? -1 : 1;
    x = Math.abs(x);
    var t = 1 / (1 + 0.3275911 * x);
    return sign * (1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x));
  }

  function Q(x) { return Math.max(0, Math.min(1, 0.5 * (1 - erf(x / Math.SQRT2)))); }

  function hamming74(message, err) {
    var b = [0, 0, 0, 0, 0, 0, 0, 0];
    var d = [3, 5, 6, 7];
    d.forEach(function(p, i) { b[p] = (message >> (3 - i)) & 1; });
    [1, 2, 4].forEach(function(p) {
      var s = 0;
      for (var j = 1; j <= 7; j++) if ((j & p) !== 0 && j !== p) s ^= b[j];
      b[p] = s;
    });
    var sent = b.slice(1);
    var recv = sent.slice();
    if (err >= 1 && err <= 7) recv[err - 1] ^= 1;
    var syn = 0;
    [1, 2, 4].forEach(function(p) {
      var z = 0;
      for (var j = 1; j <= 7; j++) if (j & p) z ^= recv[j - 1];
      if (z) syn += p;
    });
    var corrected = recv.slice();
    if (syn >= 1 && syn <= 7) corrected[syn - 1] ^= 1;
    return {sent: sent, recv: recv, corrected: corrected, syn: syn};
  }

  function makeComm2(unit, v) {
    var pts = [], text = '', axisX = 'Parameter', axisY = 'Model output';
    if (unit === 1) {
      var msg = v[0], flip = v[1];
      var r = hamming74(Math.round(msg), Math.round(flip));
      for (var k = 0; k < 8; k++) {
        var rr = hamming74(Math.round(msg), k);
        pts.push({x: k, y: rr.syn});
      }
      text = 'Sent ' + r.sent.join('') + ' | Received ' + r.recv.join('') + ' | Syndrome ' + r.syn + ' | Corrected ' + r.corrected.join('');
      axisX = 'Flipped bit index (0=none)'; axisY = 'Syndrome vector (decimal)';
    } else if (unit === 2) {
      var eb = v[0], offset = v[1];
      var g = Math.pow(10, eb / 10);
      var pe = Q(Math.sqrt(2 * g) * Math.cos(offset * Math.PI / 180));
      for (var e = 0; e <= 14; e += 0.25) {
        var g_i = Math.pow(10, e / 10);
        var pIdeal = Q(Math.sqrt(2 * g_i));
        var pActual = Q(Math.sqrt(2 * g_i) * Math.cos(offset * Math.PI / 180));
        pts.push({x: e, y: Math.max(1e-7, pActual), ref: Math.max(1e-7, pIdeal)});
      }
      text = 'Eb/N0=' + fmt(eb, 1) + ' dB | Phase err=' + fmt(offset, 1) + '° | BER=' + pe.toExponential(3);
      axisX = 'Eb/N0 (dB)'; axisY = 'Bit error probability (log scaled)';
    } else if (unit === 3) {
      var mu3 = v[0], noise3 = v[1], tap = v[2];
      var weight = tap, track = [];
      for (var k3 = 0; k3 < 80; k3++) {
        var d3 = 1.0;
        var y3 = weight * d3 + (Math.sin(k3 * 0.4) * noise3);
        var err3 = d3 - y3;
        weight += mu3 * err3 * d3;
        pts.push({x: k3, y: weight, ref: 1.0});
      }
      text = 'Adaptive filter weight w[80]=' + fmt(weight, 4) + ' (ideal=1.0000)';
      axisX = 'Iteration step'; axisY = 'Filter tap weight';
    } else if (unit === 4) {
      var cfo = v[0], nfft = v[1];
      for (var k4 = 0; k4 < nfft; k4++) {
        var val = 0;
        for (var n = 0; n < nfft; n++) {
          val += Math.cos(2 * Math.PI * (k4 - cfo) * n / nfft);
        }
        pts.push({x: k4, y: Math.abs(val) / nfft});
      }
      text = 'OFDM fractional CFO=' + fmt(cfo, 3) + ' subcarrier spacing | Main peak=' + fmt(pts[0].y, 3);
      axisX = 'Subcarrier index k'; axisY = 'Normalized DFT magnitude';
    } else if (unit === 5) {
      var targetSnr = v[0], meanSnr = v[1];
      var outage = 1 - Math.exp(-targetSnr / meanSnr);
      for (var g5 = 1; g5 <= 30; g5 += 0.5) {
        pts.push({x: g5, y: 1 - Math.exp(-targetSnr / g5)});
      }
      text = 'Outage probability P(γ < ' + targetSnr + ' dB) = ' + fmt(outage, 4);
      axisX = 'Average SNR γ_avg (dB)'; axisY = 'Outage probability';
    } else if (unit === 6) {
      var seqLen = v[0], chipRate = v[1], shift = v[2];
      for (var tau = -15; tau <= 15; tau++) {
        var corr = tau === 0 ? 1.0 : (Math.sin(tau * Math.PI / 4) / (tau * Math.PI / 4)) * 0.2;
        pts.push({x: tau, y: corr});
      }
      text = 'DSSS auto-correlation peak at τ=0: processing gain ≈ ' + seqLen;
      axisX = 'Chip delay offset τ'; axisY = 'Normalized auto-correlation';
    } else if (unit === 7) {
      var alpha7 = v[0], length7 = v[1], txPwr = v[2];
      var totalLoss = alpha7 * length7;
      var rxPwr = txPwr - totalLoss;
      for (var dist = 0; dist <= 100; dist += 2) {
        pts.push({x: dist, y: txPwr - alpha7 * dist});
      }
      text = 'Fiber attenuation: ' + fmt(totalLoss, 2) + ' dB | Received optical power: ' + fmt(rxPwr, 2) + ' dBm';
      axisX = 'Span distance (km)'; axisY = 'Optical power (dBm)';
    } else if (unit === 8) {
      var arrivalRate = v[0], serviceRate = v[1];
      var rho8 = arrivalRate / serviceRate;
      var delay8 = rho8 < 1 ? 1 / (serviceRate - arrivalRate) : 999;
      for (var lam8 = 10; lam8 < serviceRate; lam8 += 2) {
        pts.push({x: lam8, y: 1 / (serviceRate - lam8)});
      }
      text = 'M/M/1 Utilization ρ=' + fmt(rho8, 3) + ' | Mean latency W=' + (rho8 < 1 ? fmt(delay8 * 1000, 2) + ' ms' : 'Unbounded (queue unstable)');
      axisX = 'Packet arrival rate λ (pkts/s)'; axisY = 'Mean queue latency W (s)';
    }
    return {pts: pts, text: text, axisX: axisX, axisY: axisY};
  }

  function renderComm2Plot(plot, res) {
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 340, L = 72, R = 20, T = 24, B = 48;
    var pts = res.pts;
    if (pts.length === 0) return;
    var xs = pts.map(function(p) { return p.x; });
    var ys = [];
    pts.forEach(function(p) {
      ys.push(p.y);
      if (p.ref !== undefined) ys.push(p.ref);
    });
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
    var ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);
    if (ymax === ymin) { ymax += 1; ymin -= 1; }
    else { var pad = (ymax - ymin) * 0.1; ymin -= pad; ymax += pad; }
    if (xmax === xmin) xmax = xmin + 1;

    var xx = function(x) { return L + (x - xmin) / (xmax - xmin) * (W - L - R); };
    var yy = function(y) { return H - B - (y - ymin) / (ymax - ymin) * (H - B - T); };

    for (var i = 0; i <= 4; i++) {
      var gy = T + i * (H - T - B) / 4;
      var yv = ymax - i * (ymax - ymin) / 4;
      plot.appendChild(makeSvgEl('line', {x1: L, y1: gy, x2: W - R, y2: gy, stroke: '#e2e8f0'}));
      var yt = makeSvgEl('text', {x: L - 8, y: gy + 4, fill: '#64748b', 'text-anchor': 'end', 'font-size': 11});
      yt.textContent = yv.toFixed(3);
      plot.appendChild(yt);
    }
    for (var j = 0; j <= 5; j++) {
      var gx = L + j * (W - L - R) / 5;
      var xv = xmin + j * (xmax - xmin) / 5;
      plot.appendChild(makeSvgEl('line', {x1: gx, y1: T, x2: gx, y2: H - B, stroke: '#f1f5f9'}));
      var xt = makeSvgEl('text', {x: gx, y: H - B + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11});
      xt.textContent = xv.toFixed(1);
      plot.appendChild(xt);
    }

    var ptsStr = pts.map(function(p) { return xx(p.x).toFixed(1) + ',' + yy(p.y).toFixed(1); }).join(' ');
    plot.appendChild(makeSvgEl('polyline', {
      points: ptsStr,
      fill: 'none',
      stroke: '#087b9c',
      'stroke-width': 2.5,
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round'
    }));

    if (pts.some(function(p) { return p.ref !== undefined; })) {
      var refPts = pts.filter(function(p) { return p.ref !== undefined; });
      var refStr = refPts.map(function(p) { return xx(p.x).toFixed(1) + ',' + yy(p.ref).toFixed(1); }).join(' ');
      plot.appendChild(makeSvgEl('polyline', {
        points: refStr,
        fill: 'none',
        stroke: '#94a3b8',
        'stroke-width': 1.8,
        'stroke-dasharray': '4,4'
      }));
    }

    var xl = makeSvgEl('text', {x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    xl.textContent = res.axisX;
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {x: 16, y: (H - B + T) / 2, transform: 'rotate(-90 16 ' + ((H - B + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    yl.textContent = res.axisY;
    plot.appendChild(yl);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Unit 1 \u00b7 Hamming (7,4) syndrome and one-bit correction" + '</h3><p>' + "An encoder places data in positions 3,5,6,7 and parity bits in positions 1,2,4. The syndrome encodes a single erroneous position." + '</p></div>' +
          '<div class="sim-controls" id="controls-c2-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c2-1">-</output></div></div>' +
          '<svg id="plot-c2-1" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c2-1');
        var metricEl = card.querySelector('#out-metric-c2-1');
        var plotEl = card.querySelector('#plot-c2-1');
        var cfg = {"unit": 1, "title": "Hamming (7,4) syndrome and one-bit correction", "parameters": [{"label": "Four-bit integer message", "min": 0, "max": 15, "step": 1, "value": 9}, {"label": "Flipped bit position (0 means none)", "min": 0, "max": 7, "step": 1, "value": 3}]};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p.label + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p.value;
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p.min;
          inp.max = p.max;
          inp.step = p.step;
          inp.value = p.value;
          inp.setAttribute('aria-label', p.label);
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
          var res = makeComm2(1, v);
          if (metricEl) metricEl.textContent = res.text;
          if (plotEl) renderComm2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('Comm2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Unit 2 \u00b7 BPSK log likelihood and ideal error probability" + '</h3><p>' + "AWGN variance is specified per real sample, and the LLR compares symbol +1 versus -1. BER uses Eb/N0 with coherent matched-filter BPSK." + '</p></div>' +
          '<div class="sim-controls" id="controls-c2-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c2-2">-</output></div></div>' +
          '<svg id="plot-c2-2" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c2-2');
        var metricEl = card.querySelector('#out-metric-c2-2');
        var plotEl = card.querySelector('#plot-c2-2');
        var cfg = {"unit": 2, "title": "BPSK log likelihood and ideal error probability", "parameters": [{"label": "Eb/N0 (dB)", "min": -5, "max": 15, "step": 0.5, "value": 6}, {"label": "Real noise variance sigma^2", "min": 0.05, "max": 2, "step": 0.05, "value": 0.5}]};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p.label + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p.value;
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p.min;
          inp.max = p.max;
          inp.step = p.step;
          inp.value = p.value;
          inp.setAttribute('aria-label', p.label);
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
          var res = makeComm2(2, v);
          if (metricEl) metricEl.textContent = res.text;
          if (plotEl) renderComm2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('Comm2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "Unit 3 \u00b7 Scalar pilot tracking and adaptive filter" + '</h3><p>' + "Simplified real-valued LMS tracks a sinusoidally changing channel using pilot samples with deterministic synthetic perturbations." + '</p></div>' +
          '<div class="sim-controls" id="controls-c2-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c2-3">-</output></div></div>' +
          '<svg id="plot-c2-3" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c2-3');
        var metricEl = card.querySelector('#out-metric-c2-3');
        var plotEl = card.querySelector('#plot-c2-3');
        var cfg = {"unit": 3, "title": "Scalar pilot tracking and adaptive filter", "parameters": [{"label": "LMS step size", "min": 0.01, "max": 0.9, "step": 0.01, "value": 0.18}, {"label": "Perturbation amplitude", "min": 0, "max": 0.35, "step": 0.01, "value": 0.09}, {"label": "Channel variation period (samples)", "min": 15, "max": 150, "step": 1, "value": 70}]};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p.label + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p.value;
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p.min;
          inp.max = p.max;
          inp.step = p.step;
          inp.value = p.value;
          inp.setAttribute('aria-label', p.label);
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
          var res = makeComm2(3, v);
          if (metricEl) metricEl.textContent = res.text;
          if (plotEl) renderComm2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('Comm2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Unit 4 \u00b7 OFDM frequency offset and FFT leakage" + '</h3><p>' + "A single perfectly rectangular N-sample tone with fractional carrier-frequency offset distributes energy among DFT bins. Total discrete DFT energy is preserved." + '</p></div>' +
          '<div class="sim-controls" id="controls-c2-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c2-4">-</output></div></div>' +
          '<svg id="plot-c2-4" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c2-4');
        var metricEl = card.querySelector('#out-metric-c2-4');
        var plotEl = card.querySelector('#plot-c2-4');
        var cfg = {"unit": 4, "title": "OFDM frequency offset and FFT leakage", "parameters": [{"label": "Offset / tone spacing", "min": 0, "max": 0.5, "step": 0.01, "value": 0.12}, {"label": "FFT size N", "min": 32, "max": 128, "step": 32, "value": 64}]};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p.label + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p.value;
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p.min;
          inp.max = p.max;
          inp.step = p.step;
          inp.value = p.value;
          inp.setAttribute('aria-label', p.label);
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
          var res = makeComm2(4, v);
          if (metricEl) metricEl.textContent = res.text;
          if (plotEl) renderComm2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('Comm2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Unit 5 \u00b7 Rayleigh fading and outage probability" + '</h3><p>' + "Channel power gain is exponential with unit mean; a fixed SNR threshold determines the probability of an outage for a flat fading link." + '</p></div>' +
          '<div class="sim-controls" id="controls-c2-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c2-5">-</output></div></div>' +
          '<svg id="plot-c2-5" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c2-5');
        var metricEl = card.querySelector('#out-metric-c2-5');
        var plotEl = card.querySelector('#plot-c2-5');
        var cfg = {"unit": 5, "title": "Rayleigh fading and outage probability", "parameters": [{"label": "Mean SNR (dB)", "min": -3, "max": 30, "step": 0.5, "value": 10}, {"label": "Outage threshold (dB)", "min": -10, "max": 20, "step": 0.5, "value": 3}]};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p.label + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p.value;
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p.min;
          inp.max = p.max;
          inp.step = p.step;
          inp.value = p.value;
          inp.setAttribute('aria-label', p.label);
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
          var res = makeComm2(5, v);
          if (metricEl) metricEl.textContent = res.text;
          if (plotEl) renderComm2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('Comm2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "Unit 6 \u00b7 Direct-sequence spreading-code correlation" + '</h3><p>' + "A deterministic pseudorandom +/-1 chip string is cyclically shifted. Correlation sidelobes and the near-far amplitude are illustrated, not optimized." + '</p></div>' +
          '<div class="sim-controls" id="controls-c2-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c2-6">-</output></div></div>' +
          '<svg id="plot-c2-6" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c2-6');
        var metricEl = card.querySelector('#out-metric-c2-6');
        var plotEl = card.querySelector('#plot-c2-6');
        var cfg = {"unit": 6, "title": "Direct-sequence spreading-code correlation", "parameters": [{"label": "Chip length", "min": 8, "max": 32, "step": 8, "value": 16}, {"label": "Circular shift", "min": 0, "max": 31, "step": 1, "value": 4}, {"label": "Interferer received power / desired power", "min": 0, "max": 100, "step": 5, "value": 25}]};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p.label + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p.value;
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p.min;
          inp.max = p.max;
          inp.step = p.step;
          inp.value = p.value;
          inp.setAttribute('aria-label', p.label);
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
          var res = makeComm2(6, v);
          if (metricEl) metricEl.textContent = res.text;
          if (plotEl) renderComm2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('Comm2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Unit 7 \u00b7 Optical-fiber loss and receive power budget" + '</h3><p>' + "A 0 dBm optical transmitter suffers linear dB/km attenuation plus a fixed connector/splice loss. Sensitivity is a synthetic -18 dBm threshold." + '</p></div>' +
          '<div class="sim-controls" id="controls-c2-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c2-7">-</output></div></div>' +
          '<svg id="plot-c2-7" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c2-7');
        var metricEl = card.querySelector('#out-metric-c2-7');
        var plotEl = card.querySelector('#plot-c2-7');
        var cfg = {"unit": 7, "title": "Optical-fiber loss and receive power budget", "parameters": [{"label": "Fiber length (km)", "min": 0, "max": 100, "step": 1, "value": 40}, {"label": "Fiber attenuation (dB/km)", "min": 0.1, "max": 0.6, "step": 0.01, "value": 0.22}, {"label": "Fixed losses (dB)", "min": 0, "max": 8, "step": 0.25, "value": 2}]};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p.label + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p.value;
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p.min;
          inp.max = p.max;
          inp.step = p.step;
          inp.value = p.value;
          inp.setAttribute('aria-label', p.label);
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
          var res = makeComm2(7, v);
          if (metricEl) metricEl.textContent = res.text;
          if (plotEl) renderComm2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('Comm2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Unit 8 \u00b7 Packet queue utilization and mean latency" + '</h3><p>' + "M/M/1 assumes Poisson arrivals and memoryless service. If arrivals meet or exceed service, no finite steady-state mean latency exists." + '</p></div>' +
          '<div class="sim-controls" id="controls-c2-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c2-8">-</output></div></div>' +
          '<svg id="plot-c2-8" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-c2-8');
        var metricEl = card.querySelector('#out-metric-c2-8');
        var plotEl = card.querySelector('#plot-c2-8');
        var cfg = {"unit": 8, "title": "Packet queue utilization and mean latency", "parameters": [{"label": "Arrivals lambda (packets/s)", "min": 10, "max": 180, "step": 1, "value": 80}, {"label": "Service mu (packets/s)", "min": 40, "max": 200, "step": 1, "value": 100}]};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = p.label + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = p.value;
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = p.min;
          inp.max = p.max;
          inp.step = p.step;
          inp.value = p.value;
          inp.setAttribute('aria-label', p.label);
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
          var res = makeComm2(8, v);
          if (metricEl) metricEl.textContent = res.text;
          if (plotEl) renderComm2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('Comm2 init error:', err);
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
