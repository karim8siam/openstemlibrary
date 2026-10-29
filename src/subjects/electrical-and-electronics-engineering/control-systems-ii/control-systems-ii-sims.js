/* Control Systems II Interactive Simulation Suite */
(function(window) {
  'use strict';

  function sample(fn, end, n) {
    if (n === undefined) n = 170;
    var p = [];
    for (var i = 0; i <= n; i++) {
      var t = end * i / n;
      p.push([t, fn(t)]);
    }
    return p;
  }

  function computeCS2(mode, v) {
    var series = [], metric = '', note = '', xlabel = 'Time (s or discrete index)', ylabel = 'Value (normalized)';
    if (mode === 1) {
      var K = v[0], w = v[1];
      var lo = Math.max(0.01, 1 - w), hi = 1 + w;
      series = [
        {name: 'Sensitivity S(0)', values: sample(function(k) { return 1 / (1 + K * (k + lo)); }, hi - lo).map(function(pt) { return [pt[0] + lo, pt[1]]; })},
        {name: 'Tracking T(0)', values: sample(function(k) { return K * (k + lo) / (1 + K * (k + lo)); }, hi - lo).map(function(pt) { return [pt[0] + lo, pt[1]]; })}
      ];
      xlabel = 'Plant DC gain k';
      metric = 'S(0) interval: ' + (1 / (1 + K * hi)).toFixed(3) + ' to ' + (1 / (1 + K * lo)).toFixed(3);
      note = 'All intermediate plant gains in this interval retain negative closed-loop pole -(1+Kk).';
    } else if (mode === 2) {
      var Q = v[0], R = v[1], x0 = v[2];
      var P = R * (-1 + Math.sqrt(1 + Q / R)), K2 = P / R, rate = 1 + K2;
      series = [
        {name: 'State x(t)', values: sample(function(t) { return x0 * Math.exp(-rate * t); }, 5)},
        {name: 'Input u(t)', values: sample(function(t) { return -K2 * x0 * Math.exp(-rate * t); }, 5)}
      ];
      metric = 'LQR gain K=' + K2.toFixed(3) + ', pole = -' + rate.toFixed(3);
      note = 'Initial unconstrained input = ' + (-K2 * x0).toFixed(3) + '. Higher Q speeds up state decay.';
    } else if (mode === 3) {
      var Q3 = v[0], R3 = v[1], bias = v[2];
      var xhat = 0, P3 = 1, est = [], tru = [];
      for (var k3 = 0; k3 <= 60; k3++) {
        var truth = 1 + 0.2 * Math.sin(k3 * 0.22) + 0.025 * k3;
        var meas = truth + 0.55 * Math.sin(1.7 * k3) + 0.22 * Math.cos(k3 * 0.91) + bias;
        var Ppri = P3 + Q3;
        var Kk = Ppri / (Ppri + R3);
        xhat = xhat + Kk * (meas - xhat);
        P3 = (1 - Kk) * Ppri;
        tru.push([k3, truth]);
        est.push([k3, xhat]);
      }
      series = [
        {name: 'True state', values: tru},
        {name: 'Kalman estimate', values: est}
      ];
      metric = 'Steady Kalman gain K ≈ ' + (P3 / (P3 + R3)).toFixed(3);
      note = 'Filter attenuates measurement ripple while tracking smooth underlying trajectory.';
    } else if (mode === 4) {
      var rho = v[0], ubound = v[1], startState = v[2];
      var x4 = startState, traj = [], inputs = [];
      for (var k4 = 0; k4 <= 15; k4++) {
        traj.push([k4, x4]);
        var u_opt = -x4 / (1 + rho);
        var u_sat = Math.max(-ubound, Math.min(ubound, u_opt));
        inputs.push([k4, u_sat]);
        x4 = 0.8 * x4 + u_sat;
      }
      series = [
        {name: 'State x[k]', values: traj},
        {name: 'Control u[k]', values: inputs}
      ];
      metric = 'Initial input u[0] = ' + inputs[0][1].toFixed(3);
      note = 'One-step receding horizon with strict saturation bound |u| <= ' + ubound.toFixed(2);
    } else if (mode === 5) {
      var alpha = v[0], initX = v[1];
      var dt = 0.02, N = 250, traj5 = [], lyap = [];
      var currX = initX;
      for (var i5 = 0; i5 <= N; i5++) {
        var t5 = i5 * dt;
        traj5.push([t5, currX]);
        lyap.push([t5, 0.5 * currX * currX]);
        var xdot = -currX - alpha * Math.pow(currX, 3);
        currX += dt * xdot;
      }
      series = [
        {name: 'State x(t)', values: traj5},
        {name: 'Lyapunov V(x)=0.5 x²', values: lyap}
      ];
      metric = 'Final state x(' + (N * dt).toFixed(1) + 's) = ' + currX.toFixed(4);
      note = 'V_dot = -x² - α x⁴ <= 0 strictly proves global asymptotic stability.';
    } else if (mode === 6) {
      var lam = v[0], ripple = v[1], regAmp = v[2];
      var thetaTrue = 1.85, thetaHat = 0, Pcov = 10, estTheta = [];
      for (var k6 = 0; k6 <= 50; k6++) {
        var phi = regAmp * Math.sin(0.4 * k6 + 0.2);
        var yMeas = phi * thetaTrue + ripple * Math.cos(1.8 * k6);
        var Krls = (Pcov * phi) / (lam + phi * Pcov * phi);
        thetaHat = thetaHat + Krls * (yMeas - phi * thetaHat);
        Pcov = (Pcov - Krls * phi * Pcov) / lam;
        estTheta.push([k6, thetaHat]);
      }
      series = [
        {name: 'Estimated parameter', values: estTheta},
        {name: 'True parameter (1.85)', values: sample(function() { return thetaTrue; }, 50)}
      ];
      metric = 'Final estimate = ' + thetaHat.toFixed(4) + ' (true = 1.8500)';
      note = 'Recursive least squares with forgetting factor λ=' + lam.toFixed(2);
    } else if (mode === 7) {
      var g12 = v[0], g21 = v[1], u2 = v[2];
      var u1Vals = sample(function(u1) { return 1.0 * u1 + g12 * u2; }, 4);
      var y2Vals = sample(function(u1) { return g21 * u1 + 1.2 * u2; }, 4);
      series = [
        {name: 'Output y1 = u1 + g12·u2', values: u1Vals},
        {name: 'Output y2 = g21·u1 + 1.2·u2', values: y2Vals}
      ];
      var rga11 = (1.0 * 1.2) / (1.0 * 1.2 - g12 * g21);
      xlabel = 'Control input u1';
      metric = 'RGA element λ11 = ' + rga11.toFixed(3);
      note = 'Values far from 1.0 indicate strong interaction requiring decoupling or multivariable synthesis.';
    } else if (mode === 8) {
      var K8 = v[0], a8 = v[1], b8 = v[2];
      var xState = 1.0, uDelayed = 0.0, discreteTraj = [];
      for (var n8 = 0; n8 <= 35; n8++) {
        discreteTraj.push([n8, xState]);
        var uNew = -K8 * xState;
        xState = a8 * xState + b8 * uDelayed;
        uDelayed = uNew;
      }
      series = [
        {name: 'State x[n] with 1-step delay', values: discreteTraj}
      ];
      metric = 'Final state at step 35 = ' + xState.toFixed(4);
      note = 'One-sample transport delay augments state dimension and restricts maximum stable feedback gain.';
    }
    return {series: series, metric: metric, note: note, xlabel: xlabel, ylabel: ylabel};
  }

  function makeSvgEl(tag, attrs) {
    var el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, k)) {
        el.setAttribute(k, String(attrs[k]));
      }
    }
    return el;
  }

  var CS2_COLORS = ['#087b9c', '#e67e22', '#27ae60'];

  function renderCS2Plot(plot, d) {
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 340, L = 72, R = 20, T = 24, B = 48;
    var allP = [];
    d.series.forEach(function(s) {
      s.values.forEach(function(pt) {
        if (Number.isFinite(pt[0]) && Number.isFinite(pt[1])) allP.push(pt);
      });
    });
    if (allP.length === 0) return;
    var xs = allP.map(function(p) { return p[0]; }), ys = allP.map(function(p) { return p[1]; });
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
    var ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);
    if (ymax === ymin) { ymax += 1; ymin -= 1; }
    else { var pad = (ymax - ymin) * 0.12; ymin -= pad; ymax += pad; }
    if (xmax === xmin) xmax = xmin + 1;

    var px = function(x) { return L + (W - L - R) * (x - xmin) / (xmax - xmin); };
    var py = function(y) { return T + (H - T - B) * (ymax - y) / (ymax - ymin); };

    // Grid
    for (var i = 0; i <= 4; i++) {
      var gy = T + (H - T - B) * i / 4;
      plot.appendChild(makeSvgEl('line', {x1: L, y1: gy, x2: W - R, y2: gy, stroke: '#e2e8f0', 'stroke-width': 1}));
      var yt = makeSvgEl('text', {x: L - 8, y: gy + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': 11});
      yt.textContent = (ymax - (ymax - ymin) * i / 4).toFixed(2);
      plot.appendChild(yt);
    }
    for (var j = 0; j <= 5; j++) {
      var gx = L + (W - L - R) * j / 5;
      var xv = xmin + (xmax - xmin) * j / 5;
      plot.appendChild(makeSvgEl('line', {x1: gx, y1: T, x2: gx, y2: H - B, stroke: '#f1f5f9', 'stroke-width': 1}));
      var xt = makeSvgEl('text', {x: gx, y: H - B + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11});
      xt.textContent = xv.toFixed(2);
      plot.appendChild(xt);
    }

    // Lines
    d.series.forEach(function(s, idx) {
      var pts = s.values.filter(function(pt) { return Number.isFinite(pt[0]) && Number.isFinite(pt[1]); });
      if (pts.length === 0) return;
      var ptsStr = pts.map(function(pt) { return px(pt[0]).toFixed(1) + ',' + py(pt[1]).toFixed(1); }).join(' ');
      plot.appendChild(makeSvgEl('polyline', {
        points: ptsStr,
        fill: 'none',
        stroke: CS2_COLORS[idx % CS2_COLORS.length],
        'stroke-width': idx === 0 ? 2.5 : 1.8,
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round'
      }));
      var leg = makeSvgEl('text', {x: L + 14 + idx * 170, y: T + 14, fill: CS2_COLORS[idx % CS2_COLORS.length], 'font-size': 11, 'font-weight': 'bold'});
      leg.textContent = '— ' + s.name;
      plot.appendChild(leg);
    });

    var xl = makeSvgEl('text', {x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#334155', 'font-size': 12});
    xl.textContent = d.xlabel;
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {x: 14, y: T + (H - T - B) / 2, transform: 'rotate(-90 14 ' + (T + (H - T - B) / 2) + ')', 'text-anchor': 'middle', fill: '#334155', 'font-size': 12});
    yl.textContent = d.ylabel;
    plot.appendChild(yl);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Uncertainty and sensitivity explorer" + '</h3><p>' + "Evaluate robust sensitivity bounds S(0) and tracking margins across parametric plant uncertainties." + '</p></div>' +
          '<div class="sim-controls" id="controls-cs2-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-metric-cs2-1">-</output></div>' +
          '<p class="note" id="out-note-cs2-1">-</p></div>' +
          '<svg id="plot-cs2-1" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-cs2-1');
        var metricEl = card.querySelector('#out-metric-cs2-1');
        var noteEl = card.querySelector('#out-note-cs2-1');
        var plotEl = card.querySelector('#plot-cs2-1');
        var cfgControls = [["Proportional gain K", 0.2, 8, 3, 0.2], ["Uncertainty range width", 0.1, 1.2, 0.5, 0.05]];
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
          var data = computeCS2(1, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.note;
          if (plotEl) renderCS2Plot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Continuous-time scalar LQR explorer" + '</h3><p>' + "Solve algebraic Riccati equation for optimal state-feedback gain K and inspect state decay rate versus control actuation." + '</p></div>' +
          '<div class="sim-controls" id="controls-cs2-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-metric-cs2-2">-</output></div>' +
          '<p class="note" id="out-note-cs2-2">-</p></div>' +
          '<svg id="plot-cs2-2" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-cs2-2');
        var metricEl = card.querySelector('#out-metric-cs2-2');
        var noteEl = card.querySelector('#out-note-cs2-2');
        var plotEl = card.querySelector('#plot-cs2-2');
        var cfgControls = [["State penalty Q", 0.1, 12, 1, 0.1], ["Input penalty R", 0.1, 8, 1, 0.1], ["Initial state", 0.5, 4, 2, 0.1]];
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
          var data = computeCS2(2, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.note;
          if (plotEl) renderCS2Plot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "Kalman update explorer" + '</h3><p>' + "Discrete-time Kalman filter state estimation: simulate filtering innovation covariance and error convergence under Gaussian noise." + '</p></div>' +
          '<div class="sim-controls" id="controls-cs2-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-metric-cs2-3">-</output></div>' +
          '<p class="note" id="out-note-cs2-3">-</p></div>' +
          '<svg id="plot-cs2-3" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-cs2-3');
        var metricEl = card.querySelector('#out-metric-cs2-3');
        var noteEl = card.querySelector('#out-note-cs2-3');
        var plotEl = card.querySelector('#plot-cs2-3');
        var cfgControls = [["Process variance Q", 0.01, 1.5, 0.25, 0.01], ["Measurement variance R", 0.05, 5, 0.75, 0.05], ["Injected sensor bias", -2, 2, 0, 0.1]];
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
          var data = computeCS2(3, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.note;
          if (plotEl) renderCS2Plot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Constrained one-step MPC explorer" + '</h3><p>' + "Model predictive control trajectory optimization with hard input saturation bounds and receding-horizon performance." + '</p></div>' +
          '<div class="sim-controls" id="controls-cs2-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-metric-cs2-4">-</output></div>' +
          '<p class="note" id="out-note-cs2-4">-</p></div>' +
          '<svg id="plot-cs2-4" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-cs2-4');
        var metricEl = card.querySelector('#out-metric-cs2-4');
        var noteEl = card.querySelector('#out-note-cs2-4');
        var plotEl = card.querySelector('#plot-cs2-4');
        var cfgControls = [["Input penalty rho", 0.1, 8, 1, 0.1], ["Absolute input bound", 0.2, 3, 1, 0.1], ["Starting state", 0.5, 5, 3, 0.1]];
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
          var data = computeCS2(4, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.note;
          if (plotEl) renderCS2Plot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Nonlinear Lyapunov response explorer" + '</h3><p>' + "Nonlinear dynamical system stability: explore phase trajectories and state convergence governed by quadratic Lyapunov candidate function." + '</p></div>' +
          '<div class="sim-controls" id="controls-cs2-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-metric-cs2-5">-</output></div>' +
          '<p class="note" id="out-note-cs2-5">-</p></div>' +
          '<svg id="plot-cs2-5" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-cs2-5');
        var metricEl = card.querySelector('#out-metric-cs2-5');
        var noteEl = card.querySelector('#out-note-cs2-5');
        var plotEl = card.querySelector('#plot-cs2-5');
        var cfgControls = [["Cubic coefficient alpha", 0.1, 3, 1, 0.1], ["Initial state", 0.2, 3, 2, 0.1]];
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
          var data = computeCS2(5, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.note;
          if (plotEl) renderCS2Plot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "Recursive least-squares explorer" + '</h3><p>' + "Online parameter estimation with exponential data weighting and covariance matrix updates under noise." + '</p></div>' +
          '<div class="sim-controls" id="controls-cs2-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-metric-cs2-6">-</output></div>' +
          '<p class="note" id="out-note-cs2-6">-</p></div>' +
          '<svg id="plot-cs2-6" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-cs2-6');
        var metricEl = card.querySelector('#out-metric-cs2-6');
        var noteEl = card.querySelector('#out-note-cs2-6');
        var plotEl = card.querySelector('#plot-cs2-6');
        var cfgControls = [["Forgetting factor lambda", 0.7, 1, 1, 0.01], ["Measurement ripple", 0, 0.8, 0.15, 0.05], ["Regressor amplitude", 0.1, 2, 1, 0.1]];
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
          var data = computeCS2(6, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.note;
          if (plotEl) renderCS2Plot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Multivariable coupling explorer" + '</h3><p>' + "2x2 MIMO cross-coupling analysis: examine interaction indices, decentralized control detuning, and relative gain arrays (RGA)." + '</p></div>' +
          '<div class="sim-controls" id="controls-cs2-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-metric-cs2-7">-</output></div>' +
          '<p class="note" id="out-note-cs2-7">-</p></div>' +
          '<svg id="plot-cs2-7" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-cs2-7');
        var metricEl = card.querySelector('#out-metric-cs2-7');
        var noteEl = card.querySelector('#out-note-cs2-7');
        var plotEl = card.querySelector('#plot-cs2-7');
        var cfgControls = [["Cross gain g12", 0, 1.9, 1, 0.1], ["Cross gain g21", 0, 1.9, 0.5, 0.1], ["Second input u2", 0, 2, 0.6, 0.1]];
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
          var data = computeCS2(7, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.note;
          if (plotEl) renderCS2Plot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Sample delay and stability explorer" + '</h3><p>' + "Sampled-data state feedback with computational delays: inspect discrete pole locus and stability degradation near unit circle." + '</p></div>' +
          '<div class="sim-controls" id="controls-cs2-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-metric-cs2-8">-</output></div>' +
          '<p class="note" id="out-note-cs2-8">-</p></div>' +
          '<svg id="plot-cs2-8" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-cs2-8');
        var metricEl = card.querySelector('#out-metric-cs2-8');
        var noteEl = card.querySelector('#out-note-cs2-8');
        var plotEl = card.querySelector('#plot-cs2-8');
        var cfgControls = [["Controller K", 0.1, 8, 5, 0.1], ["Plant state factor a", 0.2, 0.95, 0.8, 0.05], ["Input factor b", 0.05, 0.4, 0.2, 0.05]];
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
          var data = computeCS2(8, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.note;
          if (plotEl) renderCS2Plot(plotEl, data);
        }
        update();
      } catch (err) {
        console.warn('CS2 init error:', err);
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
