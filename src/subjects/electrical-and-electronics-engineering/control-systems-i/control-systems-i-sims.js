/* Control Systems I Interactive Simulation Suite */
(function(window) {
  'use strict';

  function sample(fn, tmax, n) {
    if (n === undefined) n = 220;
    var a = [];
    for (var i = 0; i <= n; i++) {
      var x = tmax * i / n;
      a.push([x, fn(x)]);
    }
    return a;
  }

  function computeCS1(type, v) {
    var series = [], metric = '', comment = '', xlabel = 'Time (s)', ylabel = 'Output (normalized)', logx = false;
    if (type === 1) {
      var K = v[0], tau = v[1], A = v[2];
      var end = 6 * tau;
      series = [
        {label: 'Plant output', values: sample(function(t) { return K * A * (1 - Math.exp(-t / tau)); }, end)},
        {label: 'Command × static gain', values: sample(function() { return K * A; }, end)}
      ];
      metric = 'Final output = ' + (K * A).toFixed(3);
      comment = '63.2% reached at τ=' + tau.toFixed(2) + ' s; ideal 2% settling ≈ ' + (3.912 * tau).toFixed(2) + ' s.';
    } else if (type === 2) {
      var z = v[0], w = v[1], K2 = v[2];
      var d = w * Math.sqrt(1 - z * z), end2 = 12 / w;
      var yy = function(t) {
        return K2 * (1 - Math.exp(-z * w * t) * (Math.cos(d * t) + (z / Math.sqrt(1 - z * z)) * Math.sin(d * t)));
      };
      series = [
        {label: 'Second-order step', values: sample(yy, end2)},
        {label: 'Final reference', values: sample(function() { return K2; }, end2)}
      ];
      metric = 'Overshoot ≈ ' + (100 * Math.exp(-Math.PI * z / Math.sqrt(1 - z * z))).toFixed(1) + '%';
      comment = 'ωd=' + d.toFixed(3) + ' rad/s; approximate 2% settling ≈ ' + (4 / (z * w)).toFixed(2) + ' s.';
    } else if (type === 3) {
      var Kp = v[0], Gp = v[1], tau3 = v[2], L = Kp * Gp, T = L / (1 + L), tcl = tau3 / (1 + L), end3 = 6 * tcl;
      series = [
        {label: 'Reference step output', values: sample(function(t) { return T * (1 - Math.exp(-t / tcl)); }, end3)},
        {label: 'Output disturbance response', values: sample(function(t) { return 1 - T * (1 - Math.exp(-t / tcl)); }, end3)}
      ];
      metric = 'DC sensitivity S = ' + (1 / (1 + L)).toFixed(3);
      comment = 'Reference DC gain T=' + T.toFixed(3) + '. Disturbance enters at output: attenuated by feedback.';
    } else if (type === 4) {
      var K4 = v[0], a4 = v[1];
      var wn = Math.sqrt(K4), z4 = a4 / (2 * wn), end4 = Math.max(4, Math.min(30, 12 / Math.max(0.3, a4 / 2)));
      var yy4 = function(t) {
        if (z4 < 0.99999) {
          var wd = wn * Math.sqrt(1 - z4 * z4);
          return 1 - Math.exp(-z4 * wn * t) * (Math.cos(wd * t) + (z4 / Math.sqrt(1 - z4 * z4)) * Math.sin(wd * t));
        }
        if (z4 > 1.00001) {
          var p1 = -wn * (z4 - Math.sqrt(z4 * z4 - 1)), p2 = -wn * (z4 + Math.sqrt(z4 * z4 - 1));
          return 1 + (p2 * Math.exp(p1 * t) - p1 * Math.exp(p2 * t)) / (p1 - p2);
        }
        return 1 - (1 + wn * t) * Math.exp(-wn * t);
      };
      series = [
        {label: 'Closed-loop unit step', values: sample(yy4, end4)},
        {label: 'Final value', values: sample(function() { return 1; }, end4)}
      ];
      var disc = a4 * a4 - 4 * K4;
      metric = disc < 0 ? ('Poles: ' + (-a4 / 2).toFixed(2) + ' ± j' + (Math.sqrt(-disc) / 2).toFixed(2)) : ('Poles: ' + ((-a4 + Math.sqrt(disc)) / 2).toFixed(2) + ', ' + ((-a4 - Math.sqrt(disc)) / 2).toFixed(2));
      comment = 'ζ=' + z4.toFixed(3) + '; positive coefficients ensure textbook-model asymptotic stability.';
    } else if (type === 5) {
      var K5 = v[0], t1 = v[1], t2 = v[2], delay = v[3];
      var mag = function(w) { return K5 / Math.sqrt((1 + Math.pow(w * t1, 2)) * (1 + Math.pow(w * t2, 2))); };
      var low = 0.05 / Math.max(t1, t2), high = 50 / Math.min(t1, t2);
      var vals = sample(function(p) { return 20 * Math.log10(mag(Math.exp(p))); }, Math.log(high / low), 230).map(function(pt) {
        return [low * Math.exp(pt[0]), pt[1]];
      });
      var a5 = 0, b5 = high;
      for (var k = 0; k < 75; k++) {
        var mid = (a5 + b5) / 2;
        if (mag(mid) > 1) a5 = mid; else b5 = mid;
      }
      var crossover = (a5 + b5) / 2;
      var ph = -(Math.atan(crossover * t1) + Math.atan(crossover * t2) + crossover * delay) * 180 / Math.PI;
      series = [
        {label: 'Magnitude (dB)', values: vals},
        {label: '0 dB crossover', values: [[low, 0], [high, 0]]}
      ];
      xlabel = 'Angular frequency ω (rad/s, logarithmic)';
      ylabel = 'Magnitude (dB)';
      metric = 'Phase margin with delay ≈ ' + (180 + ph).toFixed(1) + '°';
      comment = 'Gain crossover ≈ ' + crossover.toFixed(3) + ' rad/s. Extra delay reduces phase margin.';
      logx = true;
    } else if (type === 6) {
      var kp = v[0], ki = v[1], umax = v[2], rhi = v[3];
      var dt = 0.005, N = Math.round(12 / dt);
      var out1 = [], out2 = [], ref = [];
      var y1 = 0, y2 = 0, I1 = 0, I2 = 0;
      for (var i6 = 0; i6 <= N; i6++) {
        var t6 = i6 * dt, r = t6 < 5 ? rhi : 0.5;
        if (i6 % 5 === 0) { out1.push([t6, y1]); out2.push([t6, y2]); ref.push([t6, r]); }
        var e1 = r - y1, raw1 = kp * e1 + ki * I1, u1 = Math.max(-umax, Math.min(umax, raw1));
        I1 += dt * e1; y1 += dt * (-y1 + u1);
        var e2 = r - y2, raw2 = kp * e2 + ki * I2, u2 = Math.max(-umax, Math.min(umax, raw2));
        if (!((raw2 > umax && e2 > 0) || (raw2 < -umax && e2 < 0))) I2 += dt * e2;
        y2 += dt * (-y2 + u2);
      }
      series = [
        {label: 'No antiwindup', values: out1},
        {label: 'Conditional antiwindup', values: out2},
        {label: 'Reference', values: ref}
      ];
      metric = 'At 12 s: no AW y=' + y1.toFixed(2) + ', AW y=' + y2.toFixed(2);
      comment = 'Initial reference ' + rhi.toFixed(1) + ' drops to 0.5 at t=5 s. Anti-windup eliminates overshoot.';
    } else if (type === 7) {
      var k7 = v[0], c7 = v[1], F7 = v[2], dt7 = 0.002, N7 = 9000, end7 = dt7 * N7;
      var x7 = 0, vel7 = 0, arr7 = [];
      for (var i7 = 0; i7 <= N7; i7++) {
        var t7 = i7 * dt7;
        if (i7 % 40 === 0) arr7.push([t7, x7]);
        var acc = F7 - c7 * vel7 - k7 * x7;
        vel7 += dt7 * acc; x7 += dt7 * vel7;
      }
      series = [
        {label: 'Position (m)', values: arr7},
        {label: 'Equilibrium F/k (m)', values: sample(function() { return F7 / k7; }, end7)}
      ];
      metric = 'Equilibrium x = ' + (F7 / k7).toFixed(3) + ' m';
      comment = 'Damping ratio ζ=' + (c7 / (2 * Math.sqrt(k7))).toFixed(3) + ' for m=1 kg.';
    } else if (type === 8) {
      var Ts = v[0], Kp8 = v[1], tau8 = v[2], a8 = Math.exp(-Ts / tau8), lambda = a8 - (1 - a8) * Kp8;
      var y8 = 0, pts8 = [];
      for (var n8 = 0; n8 <= 80; n8++) {
        pts8.push([n8 * Ts, Math.max(-100, Math.min(100, y8))]);
        y8 = lambda * y8 + (1 - a8) * Kp8;
      }
      series = [
        {label: 'Sampled output', values: pts8},
        {label: 'Command', values: [[0, 1], [80 * Ts, 1]]}
      ];
      metric = 'Closed-loop multiplier λ = ' + lambda.toFixed(3);
      comment = '|λ|' + (Math.abs(lambda) < 1 ? '<1: stable' : '≥1: marginal or unstable') + '; sampled steady tracking.';
    }
    return {series: series, metric: metric, comment: comment, xlabel: xlabel, ylabel: ylabel, logx: logx};
  }

  var COLORS = ['#1376a1', '#dc7b29', '#4d9a69'];

  function makeSvgEl(tag, attrs) {
    var el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, k)) {
        el.setAttribute(k, String(attrs[k]));
      }
    }
    return el;
  }

  function renderCSPlot(plot, data) {
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var w = 800, h = 340, left = 68, right = 20, top = 24, bottom = 48;
    var innerW = w - left - right, innerH = h - top - bottom;
    var allPts = [];
    data.series.forEach(function(s) {
      s.values.forEach(function(pt) {
        if (Number.isFinite(pt[0]) && Number.isFinite(pt[1])) allPts.push(pt);
      });
    });
    if (allPts.length === 0) return;
    var xs = allPts.map(function(p) { return p[0]; }), ys = allPts.map(function(p) { return p[1]; });
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
    var ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);
    if (ymax === ymin) { ymax += 1; ymin -= 1; }
    else { var extra = (ymax - ymin) * 0.12; ymax += extra; ymin -= extra; }
    if (xmax === xmin) xmax = xmin + 1;

    var tx = function(x) {
      var ratio = data.logx ? (Math.log(x / xmin) / Math.log(xmax / xmin)) : ((x - xmin) / (xmax - xmin));
      return left + innerW * (ratio || 0);
    };
    var ty = function(y) {
      return top + innerH * (ymax - y) / (ymax - ymin);
    };

    // Grid lines
    for (var i = 0; i <= 4; i++) {
      var gy = top + i * innerH / 4;
      plot.appendChild(makeSvgEl('line', {x1: left, y1: gy, x2: w - right, y2: gy, stroke: '#e2e8f0', 'stroke-width': 1}));
      var yt = makeSvgEl('text', {x: left - 8, y: gy + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': 11});
      yt.textContent = (ymax - i * (ymax - ymin) / 4).toFixed(2);
      plot.appendChild(yt);
    }
    for (var j = 0; j <= 5; j++) {
      var gx = left + j * innerW / 5;
      var xv = data.logx ? xmin * Math.exp(Math.log(xmax / xmin) * j / 5) : xmin + (xmax - xmin) * j / 5;
      plot.appendChild(makeSvgEl('line', {x1: gx, y1: top, x2: gx, y2: h - bottom, stroke: '#f1f5f9', 'stroke-width': 1}));
      var xt = makeSvgEl('text', {x: gx, y: h - bottom + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11});
      xt.textContent = xv >= 100 ? xv.toFixed(0) : (xv >= 1 ? xv.toFixed(1) : xv.toPrecision(2));
      plot.appendChild(xt);
    }

    // Series
    data.series.forEach(function(s, idx) {
      var validPts = s.values.filter(function(pt) { return Number.isFinite(pt[0]) && Number.isFinite(pt[1]); });
      if (validPts.length === 0) return;
      var ptsStr = validPts.map(function(pt) { return tx(pt[0]).toFixed(1) + ',' + ty(pt[1]).toFixed(1); }).join(' ');
      plot.appendChild(makeSvgEl('polyline', {
        points: ptsStr,
        fill: 'none',
        stroke: COLORS[idx % COLORS.length],
        'stroke-width': idx === 0 ? 2.5 : 1.8,
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round'
      }));
      var leg = makeSvgEl('text', {x: left + 14 + idx * 160, y: top + 14, fill: COLORS[idx % COLORS.length], 'font-size': 11, 'font-weight': 'bold'});
      leg.textContent = '— ' + s.label;
      plot.appendChild(leg);
    });

    var xl = makeSvgEl('text', {x: w / 2, y: h - 8, 'text-anchor': 'middle', fill: '#334155', 'font-size': 12});
    xl.textContent = data.xlabel;
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {x: 14, y: top + innerH / 2, transform: 'rotate(-90 14 ' + (top + innerH / 2) + ')', 'text-anchor': 'middle', fill: '#334155', 'font-size': 12});
    yl.textContent = data.ylabel;
    plot.appendChild(yl);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "First-order plant transient" + '</h3><p>' + "Investigate the RC-like first-order response. The model has one real stable pole; the 63.2% point occurs at one time constant." + '</p></div>' +
          '<div class="sim-controls" id="controls-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Metric</small><output id="out-metric-1">-</output></div>' +
          '<p class="note" id="out-note-1">-</p></div>' +
          '<svg id="plot-1" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-1');
        var metricEl = card.querySelector('#out-metric-1');
        var noteEl = card.querySelector('#out-note-1');
        var plotEl = card.querySelector('#plot-1');
        var cfgControls = [["Static gain K", 0.5, 4, 2, 0.1], ["Time constant \u03c4 (s)", 0.1, 3, 0.75, 0.05], ["Step amplitude A", 0.25, 3, 1, 0.05]];
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var data = computeCS1(1, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.comment;
          if (plotEl) renderCSPlot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Second-order overshoot and damping" + '</h3><p>' + "Explore step response overshoot, oscillation frequency, and settling time as damping ratio \u03b6 varies from underdamped to critically damped." + '</p></div>' +
          '<div class="sim-controls" id="controls-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Metric</small><output id="out-metric-2">-</output></div>' +
          '<p class="note" id="out-note-2">-</p></div>' +
          '<svg id="plot-2" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-2');
        var metricEl = card.querySelector('#out-metric-2');
        var noteEl = card.querySelector('#out-note-2');
        var plotEl = card.querySelector('#plot-2');
        var cfgControls = [["Damping \u03b6", 0.05, 0.95, 0.4, 0.01], ["Natural frequency \u03c9n (rad/s)", 0.5, 12, 5, 0.1], ["Static gain K", 0.5, 3, 1, 0.1]];
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var data = computeCS1(2, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.comment;
          if (plotEl) renderCSPlot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "Reference tracking and output disturbance" + '</h3><p>' + "Evaluate sensitivity S and complementary sensitivity T. High loop gain rejects disturbance and accelerates tracking." + '</p></div>' +
          '<div class="sim-controls" id="controls-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Metric</small><output id="out-metric-3">-</output></div>' +
          '<p class="note" id="out-note-3">-</p></div>' +
          '<svg id="plot-3" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-3');
        var metricEl = card.querySelector('#out-metric-3');
        var noteEl = card.querySelector('#out-note-3');
        var plotEl = card.querySelector('#plot-3');
        var cfgControls = [["Controller gain Kp", 0.2, 15, 4, 0.1], ["Plant DC gain Gp", 0.2, 4, 2, 0.1], ["Open-loop \u03c4 (s)", 0.2, 4, 1, 0.1]];
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var data = computeCS1(3, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.comment;
          if (plotEl) renderCSPlot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Pole migration with loop gain" + '</h3><p>' + "Root locus trajectory: observe closed-loop pole locations shifting from real distinct to complex conjugate pairs as loop gain increases." + '</p></div>' +
          '<div class="sim-controls" id="controls-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Metric</small><output id="out-metric-4">-</output></div>' +
          '<p class="note" id="out-note-4">-</p></div>' +
          '<svg id="plot-4" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-4');
        var metricEl = card.querySelector('#out-metric-4');
        var noteEl = card.querySelector('#out-note-4');
        var plotEl = card.querySelector('#plot-4');
        var cfgControls = [["Gain K", 0.25, 36, 9, 0.25], ["Damping coefficient a", 0.5, 10, 4, 0.1]];
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var data = computeCS1(4, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.comment;
          if (plotEl) renderCSPlot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Bode gain and delay margin" + '</h3><p>' + "Examine gain crossover frequency, phase margin, and the destabilizing impact of transport delay on relative stability." + '</p></div>' +
          '<div class="sim-controls" id="controls-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Metric</small><output id="out-metric-5">-</output></div>' +
          '<p class="note" id="out-note-5">-</p></div>' +
          '<svg id="plot-5" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-5');
        var metricEl = card.querySelector('#out-metric-5');
        var noteEl = card.querySelector('#out-note-5');
        var plotEl = card.querySelector('#plot-5');
        var cfgControls = [["Loop gain K", 1.01, 30, 8, 0.1], ["First \u03c41 (s)", 0.1, 2, 0.5, 0.05], ["Second \u03c42 (s)", 0.01, 0.5, 0.1, 0.01], ["Extra delay Td (s)", 0, 0.5, 0.05, 0.01]];
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var data = computeCS1(5, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.comment;
          if (plotEl) renderCSPlot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "PI saturation and integral windup" + '</h3><p>' + "Compare unconstrained integral accumulation against conditional anti-windup clamping during large actuator saturation transients." + '</p></div>' +
          '<div class="sim-controls" id="controls-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Metric</small><output id="out-metric-6">-</output></div>' +
          '<p class="note" id="out-note-6">-</p></div>' +
          '<svg id="plot-6" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-6');
        var metricEl = card.querySelector('#out-metric-6');
        var noteEl = card.querySelector('#out-note-6');
        var plotEl = card.querySelector('#plot-6');
        var cfgControls = [["Proportional gain Kp", 0.2, 8, 3, 0.1], ["Integral gain Ki (1/s)", 0.1, 8, 2, 0.1], ["Actuator limit |u|", 0.5, 4, 1, 0.1], ["Initial step reference", 1, 8, 4, 0.1]];
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var data = computeCS1(6, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.comment;
          if (plotEl) renderCSPlot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Mass\u2013spring\u2013damper state response" + '</h3><p>' + "Simulate second-order mechanical position dynamics driven by step force with variable stiffness and viscous damping dissipation." + '</p></div>' +
          '<div class="sim-controls" id="controls-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Metric</small><output id="out-metric-7">-</output></div>' +
          '<p class="note" id="out-note-7">-</p></div>' +
          '<svg id="plot-7" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-7');
        var metricEl = card.querySelector('#out-metric-7');
        var noteEl = card.querySelector('#out-note-7');
        var plotEl = card.querySelector('#plot-7');
        var cfgControls = [["Stiffness k (N/m)", 1, 30, 9, 0.5], ["Viscous damping c (N\u00b7s/m)", 0.2, 12, 2, 0.2], ["Step force F (N)", 0.2, 5, 2, 0.2]];
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var data = computeCS1(7, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.comment;
          if (plotEl) renderCSPlot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Sampled proportional feedback" + '</h3><p>' + "Discrete-time zero-order hold sampled dynamics: observe discrete pole location and stability boundary as sampling period Ts expands." + '</p></div>' +
          '<div class="sim-controls" id="controls-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Metric</small><output id="out-metric-8">-</output></div>' +
          '<p class="note" id="out-note-8">-</p></div>' +
          '<svg id="plot-8" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-8');
        var metricEl = card.querySelector('#out-metric-8');
        var noteEl = card.querySelector('#out-note-8');
        var plotEl = card.querySelector('#plot-8');
        var cfgControls = [["Sample period Ts (s)", 0.02, 0.5, 0.1, 0.01], ["Gain Kp", 0.2, 12, 5, 0.1], ["Plant \u03c4 (s)", 0.2, 2, 0.5, 0.05]];
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
          var v = inputs.map(function(el) { return Number(el.value); });
          var data = computeCS1(8, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.comment;
          if (plotEl) renderCSPlot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS1 init error:', err);
      }
    }
  });

  if (!window.SimulationEngine) window.SimulationEngine = {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId) ||
                    document.getElementById('sim-container') ||
                    document.querySelector('.simulation-slot');
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
    var autoInit = function() {
      var slot = document.getElementById('sim-container') || document.querySelector('.simulation-slot');
      if (slot && slot.children.length === 0) {
        window.SimulationEngine.initSimulation(slot.id || 'sim-container');
      }
    };
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', autoInit);
    } else {
      autoInit();
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
