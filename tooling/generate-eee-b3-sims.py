import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793271497058_746381a5.zip'

print("Generating Batch 3 EEE Simulation Suites...")

ENGINE_FOOTER = """
  if (!window.SimulationEngine) window.SimulationEngine = {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId || 'sim-container');
    if (!container) return;
    container.innerHTML = '';
    var unitNum = 1;
    if (simType) {
      var m = simType.match(/(\\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    } else {
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {
        var pMatch = window.location.pathname.match(/chapter-(\\d+)/);
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
"""

# ==============================================================================
# 1. CONTROL SYSTEMS I
# ==============================================================================
print("Generating control-systems-i-sims.js...")

cs1_configs = [
  {"controls": [["Static gain K", 0.5, 4, 2, 0.1], ["Time constant τ (s)", 0.1, 3, 0.75, 0.05], ["Step amplitude A", 0.25, 3, 1, 0.05]], "title": "First-order plant transient", "desc": "Investigate the RC-like first-order response. The model has one real stable pole; the 63.2% point occurs at one time constant."},
  {"controls": [["Damping ζ", 0.05, 0.95, 0.4, 0.01], ["Natural frequency ωn (rad/s)", 0.5, 12, 5, 0.1], ["Static gain K", 0.5, 3, 1, 0.1]], "title": "Second-order overshoot and damping", "desc": "Explore step response overshoot, oscillation frequency, and settling time as damping ratio ζ varies from underdamped to critically damped."},
  {"controls": [["Controller gain Kp", 0.2, 15, 4, 0.1], ["Plant DC gain Gp", 0.2, 4, 2, 0.1], ["Open-loop τ (s)", 0.2, 4, 1, 0.1]], "title": "Reference tracking and output disturbance", "desc": "Evaluate sensitivity S and complementary sensitivity T. High loop gain rejects disturbance and accelerates tracking."},
  {"controls": [["Gain K", 0.25, 36, 9, 0.25], ["Damping coefficient a", 0.5, 10, 4, 0.1]], "title": "Pole migration with loop gain", "desc": "Root locus trajectory: observe closed-loop pole locations shifting from real distinct to complex conjugate pairs as loop gain increases."},
  {"controls": [["Loop gain K", 1.01, 30, 8, 0.1], ["First τ1 (s)", 0.1, 2, 0.5, 0.05], ["Second τ2 (s)", 0.01, 0.5, 0.1, 0.01], ["Extra delay Td (s)", 0, 0.5, 0.05, 0.01]], "title": "Bode gain and delay margin", "desc": "Examine gain crossover frequency, phase margin, and the destabilizing impact of transport delay on relative stability."},
  {"controls": [["Proportional gain Kp", 0.2, 8, 3, 0.1], ["Integral gain Ki (1/s)", 0.1, 8, 2, 0.1], ["Actuator limit |u|", 0.5, 4, 1, 0.1], ["Initial step reference", 1, 8, 4, 0.1]], "title": "PI saturation and integral windup", "desc": "Compare unconstrained integral accumulation against conditional anti-windup clamping during large actuator saturation transients."},
  {"controls": [["Stiffness k (N/m)", 1, 30, 9, 0.5], ["Viscous damping c (N·s/m)", 0.2, 12, 2, 0.2], ["Step force F (N)", 0.2, 5, 2, 0.2]], "title": "Mass–spring–damper state response", "desc": "Simulate second-order mechanical position dynamics driven by step force with variable stiffness and viscous damping dissipation."},
  {"controls": [["Sample period Ts (s)", 0.02, 0.5, 0.1, 0.01], ["Gain Kp", 0.2, 12, 5, 0.1], ["Plant τ (s)", 0.2, 2, 0.5, 0.05]], "title": "Sampled proportional feedback", "desc": "Discrete-time zero-order hold sampled dynamics: observe discrete pole location and stability boundary as sampling period Ts expands."}
]

cs1_js = """/* Control Systems I Interactive Simulation Suite */
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
"""

for idx, item in enumerate(cs1_configs, 1):
    u = idx
    ctrls_json = json.dumps(item["controls"])
    title_esc = json.dumps(item["title"])
    desc_esc = json.dumps(item["desc"])
    cs1_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {desc_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Metric</small><output id="out-metric-{idx}">-</output></div>' +
          '<p class="note" id="out-note-{idx}">-</p></div>' +
          '<svg id="plot-{idx}" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-{idx}');
        var metricEl = card.querySelector('#out-metric-{idx}');
        var noteEl = card.querySelector('#out-note-{idx}');
        var plotEl = card.querySelector('#plot-{idx}');
        var cfgControls = {ctrls_json};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {{
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
          inp.addEventListener('input', function() {{
            valSpan.textContent = inp.value;
            update();
          }});
        }});

        function update() {{
          var v = inputs.map(function(el) {{ return Number(el.value); }});
          var data = computeCS1({idx}, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.comment;
          if (plotEl) renderCSPlot(plotEl, data);
        }}
        update();
      }} catch (err) {{
        console.warn('CS1 init error:', err);
      }}
    }}
  }});
"""

cs1_js += ENGINE_FOOTER

cs1_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'control-systems-i', 'control-systems-i-sims.js')
with open(cs1_out, 'w', encoding='utf-8') as f:
    f.write(cs1_js)
print(f"Saved {cs1_out} ({len(cs1_js)} bytes)")

# ==============================================================================
# 2. CONTROL SYSTEMS II
# ==============================================================================
print("Generating control-systems-ii-sims.js...")

cs2_configs = [
  {"controls": [["Proportional gain K", 0.2, 8, 3, 0.2], ["Uncertainty range width", 0.1, 1.2, 0.5, 0.05]], "title": "Uncertainty and sensitivity explorer", "desc": "Evaluate robust sensitivity bounds S(0) and tracking margins across parametric plant uncertainties."},
  {"controls": [["State penalty Q", 0.1, 12, 1, 0.1], ["Input penalty R", 0.1, 8, 1, 0.1], ["Initial state", 0.5, 4, 2, 0.1]], "title": "Continuous-time scalar LQR explorer", "desc": "Solve algebraic Riccati equation for optimal state-feedback gain K and inspect state decay rate versus control actuation."},
  {"controls": [["Process variance Q", 0.01, 1.5, 0.25, 0.01], ["Measurement variance R", 0.05, 5, 0.75, 0.05], ["Injected sensor bias", -2, 2, 0, 0.1]], "title": "Kalman update explorer", "desc": "Discrete-time Kalman filter state estimation: simulate filtering innovation covariance and error convergence under Gaussian noise."},
  {"controls": [["Input penalty rho", 0.1, 8, 1, 0.1], ["Absolute input bound", 0.2, 3, 1, 0.1], ["Starting state", 0.5, 5, 3, 0.1]], "title": "Constrained one-step MPC explorer", "desc": "Model predictive control trajectory optimization with hard input saturation bounds and receding-horizon performance."},
  {"controls": [["Cubic coefficient alpha", 0.1, 3, 1, 0.1], ["Initial state", 0.2, 3, 2, 0.1]], "title": "Nonlinear Lyapunov response explorer", "desc": "Nonlinear dynamical system stability: explore phase trajectories and state convergence governed by quadratic Lyapunov candidate function."},
  {"controls": [["Forgetting factor lambda", 0.7, 1, 1, 0.01], ["Measurement ripple", 0, 0.8, 0.15, 0.05], ["Regressor amplitude", 0.1, 2, 1, 0.1]], "title": "Recursive least-squares explorer", "desc": "Online parameter estimation with exponential data weighting and covariance matrix updates under noise."},
  {"controls": [["Cross gain g12", 0, 1.9, 1, 0.1], ["Cross gain g21", 0, 1.9, 0.5, 0.1], ["Second input u2", 0, 2, 0.6, 0.1]], "title": "Multivariable coupling explorer", "desc": "2x2 MIMO cross-coupling analysis: examine interaction indices, decentralized control detuning, and relative gain arrays (RGA)."},
  {"controls": [["Controller K", 0.1, 8, 5, 0.1], ["Plant state factor a", 0.2, 0.95, 0.8, 0.05], ["Input factor b", 0.05, 0.4, 0.2, 0.05]], "title": "Sample delay and stability explorer", "desc": "Sampled-data state feedback with computational delays: inspect discrete pole locus and stability degradation near unit circle."}
]

cs2_js = """/* Control Systems II Interactive Simulation Suite */
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
"""

for idx, item in enumerate(cs2_configs, 1):
    u = idx
    ctrls_json = json.dumps(item["controls"])
    title_esc = json.dumps(item["title"])
    desc_esc = json.dumps(item["desc"])
    cs2_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {desc_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-cs2-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-metric-cs2-{idx}">-</output></div>' +
          '<p class="note" id="out-note-cs2-{idx}">-</p></div>' +
          '<svg id="plot-cs2-{idx}" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-cs2-{idx}');
        var metricEl = card.querySelector('#out-metric-cs2-{idx}');
        var noteEl = card.querySelector('#out-note-cs2-{idx}');
        var plotEl = card.querySelector('#plot-cs2-{idx}');
        var cfgControls = {ctrls_json};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {{
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
          inp.addEventListener('input', function() {{
            valSpan.textContent = inp.value;
            update();
          }});
        }});

        function update() {{
          var v = inputs.map(function(el) {{ return Number(el.value); }});
          var data = computeCS2({idx}, v);
          if (metricEl) metricEl.textContent = data.metric;
          if (noteEl) noteEl.textContent = data.note;
          if (plotEl) renderCS2Plot(plotEl, data);
        }}
        update();
      }} catch (err) {{
        console.warn('CS2 init error:', err);
      }}
    }}
  }});
"""

cs2_js += ENGINE_FOOTER

cs2_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'control-systems-ii', 'control-systems-ii-sims.js')
with open(cs2_out, 'w', encoding='utf-8') as f:
    f.write(cs2_js)
print(f"Saved {cs2_out} ({len(cs2_js)} bytes)")

# ==============================================================================
# 3. COMMUNICATION SYSTEMS I
# ==============================================================================
print("Generating communication-systems-i-sims.js...")

comm1_models_data = []
with zipfile.ZipFile(ARCHIVE, 'r') as z:
    for i in range(1, 9):
        p = f'OpenSTEM-Electrical-and-Electronics-Engineering/books/communication-systems-i/simulations/model-{i:02d}.html'
        raw = z.read(p).decode('utf-8')
        cfg_str = raw.split('<script type="application/json" id="configuration">')[1].split('</script>')[0]
        cfg = json.loads(cfg_str)
        t_m = re.search(r'<h1>(.*?)</h1>', raw)
        title = t_m.group(1) if t_m else cfg['title']
        lead_m = re.search(r'</h1>\s*<p>(.*?)</p>', raw)
        lead = lead_m.group(1) if lead_m else ""
        comm1_models_data.append({
            'idx': i,
            'title': title,
            'lead': lead,
            'cfg': cfg
        })

comm1_js = """/* Communication Systems I Interactive Simulation Suite */
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
"""

for m in comm1_models_data:
    idx = m['idx']
    u = idx
    cfg_json = json.dumps(m['cfg'])
    title_esc = json.dumps(m['title'])
    lead_esc = json.dumps(m['lead'])
    comm1_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {lead_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-c1-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c1-{idx}">-</output></div></div>' +
          '<svg id="plot-c1-{idx}" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-c1-{idx}');
        var metricEl = card.querySelector('#out-metric-c1-{idx}');
        var plotEl = card.querySelector('#plot-c1-{idx}');
        var cfg = {cfg_json};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {{
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
          inp.addEventListener('input', function() {{
            valSpan.textContent = inp.value;
            update();
          }});
        }});

        function update() {{
          var v = inputs.map(function(el) {{ return Number(el.value); }});
          var res = calcComm1({idx}, v);
          if (metricEl) metricEl.textContent = res.head;
          if (plotEl) renderComm1Plot(plotEl, cfg, res);
        }}
        update();
      }} catch (err) {{
        console.warn('Comm1 init error:', err);
      }}
    }}
  }});
"""

comm1_js += ENGINE_FOOTER

comm1_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'communication-systems-i', 'communication-systems-i-sims.js')
with open(comm1_out, 'w', encoding='utf-8') as f:
    f.write(comm1_js)
print(f"Saved {comm1_out} ({len(comm1_js)} bytes)")

# ==============================================================================
# 4. COMMUNICATION SYSTEMS II
# ==============================================================================
print("Generating communication-systems-ii-sims.js...")

comm2_models_data = []
with zipfile.ZipFile(ARCHIVE, 'r') as z:
    for i in range(1, 9):
        p = f'OpenSTEM-Electrical-and-Electronics-Engineering/books/communication-systems-ii/simulations/model-{i:02d}.html'
        raw = z.read(p).decode('utf-8')
        cfg_str = raw.split('<script id="configuration" type="application/json">')[1].split('</script>')[0]
        cfg = json.loads(cfg_str)
        t_m = re.search(r'<h1>(.*?)</h1>', raw)
        title = t_m.group(1) if t_m else cfg['title']
        lead_m = re.search(r'</h1>\s*<p>(.*?)</p>', raw)
        lead = lead_m.group(1) if lead_m else ""
        comm2_models_data.append({
            'idx': i,
            'title': title,
            'lead': lead,
            'cfg': cfg
        })

comm2_js = """/* Communication Systems II Interactive Simulation Suite */
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
"""

for m in comm2_models_data:
    idx = m['idx']
    u = idx
    cfg_json = json.dumps(m['cfg'])
    title_esc = json.dumps(m['title'])
    lead_esc = json.dumps(m['lead'])
    comm2_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {lead_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-c2-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metrics</small><output id="out-metric-c2-{idx}">-</output></div></div>' +
          '<svg id="plot-c2-{idx}" viewBox="0 0 800 340" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-c2-{idx}');
        var metricEl = card.querySelector('#out-metric-c2-{idx}');
        var plotEl = card.querySelector('#plot-c2-{idx}');
        var cfg = {cfg_json};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfg.parameters.forEach(function(p, pi) {{
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
          inp.addEventListener('input', function() {{
            valSpan.textContent = inp.value;
            update();
          }});
        }});

        function update() {{
          var v = inputs.map(function(el) {{ return Number(el.value); }});
          var res = makeComm2({idx}, v);
          if (metricEl) metricEl.textContent = res.text;
          if (plotEl) renderComm2Plot(plotEl, res);
        }}
        update();
      }} catch (err) {{
        console.warn('Comm2 init error:', err);
      }}
    }}
  }});
"""

comm2_js += ENGINE_FOOTER

comm2_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'communication-systems-ii', 'communication-systems-ii-sims.js')
with open(comm2_out, 'w', encoding='utf-8') as f:
    f.write(comm2_js)
print(f"Saved {comm2_out} ({len(comm2_js)} bytes)")

# ==============================================================================
# 5. DIGITAL SIGNAL PROCESSING
# ==============================================================================
print("Generating digital-signal-processing-sims.js...")

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    dsp_raw_models = z.read("OpenSTEM-Electrical-and-Electronics-Engineering/books/digital-signal-processing/assets/models.js").decode("utf-8")

# Extract the body of models.js (excluding the DOMContentLoaded listener and export)
dsp_core = dsp_raw_models.split('function init(){')[0]

dsp_js = f"""/* Digital Signal Processing Interactive Simulation Suite */
(function(window) {{
  'use strict';

  {dsp_core}

  var MODELS = [];
"""

# Extract configs from dsp_core
cfg_start = dsp_raw_models.find("const configs=[")
idx = dsp_raw_models.find(";\nfunction", cfg_start)
dsp_cfgs = json.loads(dsp_raw_models[cfg_start+14:idx])

for i, c in enumerate(dsp_cfgs, 1):
    u = ((i - 1) // 2) + 1
    title_esc = json.dumps(c['title'])
    desc_esc = json.dumps(c['description'])
    param_lab = json.dumps(c['parameterLabel'])
    p_min = c['min']
    p_max = c['max']
    p_step = c['step']
    p_def = c['default']
    dsp_js += f"""
  MODELS.push({{
    idx: {i},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {i:02d}</span><h3>' + {title_esc} + '</h3><p>' + {desc_esc} + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + {param_lab} + ': <strong id="val-{i}">{p_def}</strong></label>' +
          '<input id="slider-{i}" type="range" min="{p_min}" max="{p_max}" step="{p_step}" value="{p_def}" aria-label="' + {param_lab} + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-{i}">-</output></div></div>' +
          '<canvas id="canvas-{i}" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {{
      try {{
        var slider = card.querySelector('#slider-{i}');
        var valSpan = card.querySelector('#val-{i}');
        var statOut = card.querySelector('#stat-{i}');
        var canvas = card.querySelector('#canvas-{i}');

        function update() {{
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {{
            var res = evaluate({i}, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          }} catch (err) {{
            statOut.textContent = 'Model error: ' + err.message;
          }}
        }}
        slider.addEventListener('input', update);
        update();
      }} catch (err) {{
        console.warn('DSP init error in model {i}:', err);
      }}
    }}
  }});
"""

dsp_js += ENGINE_FOOTER

dsp_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'digital-signal-processing', 'digital-signal-processing-sims.js')
with open(dsp_out, 'w', encoding='utf-8') as f:
    f.write(dsp_js)
print(f"Saved {dsp_out} ({len(dsp_js)} bytes)")

print("Batch 3 simulation suites generated successfully!")
