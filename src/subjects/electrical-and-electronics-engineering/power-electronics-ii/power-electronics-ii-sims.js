/* Power Electronics II Interactive Simulation Suite */
(function(window) {
  'use strict';

  function calcPE2(idx, v) {
    var main = '', second = '', xaxis = 'Parameter', yaxis = 'Output', pts = [];
    if (idx === 1) {
      var Vin = v[0], D = v[1], Lm = v[2] * 1e-6;
      var fsw = 100e3, T = 1 / fsw, ton = D * T;
      var Ipk = (Vin * ton) / Lm;
      var Estored = 0.5 * Lm * Ipk * Ipk;
      var Ptrans = Estored * fsw;
      main = 'Peak magnetizing current = ' + Ipk.toFixed(2) + ' A';
      second = 'Stored energy = ' + (Estored * 1e3).toFixed(2) + ' mJ | Throughput power ≈ ' + Ptrans.toFixed(1) + ' W';
      xaxis = 'Duty cycle D'; yaxis = 'Peak current (A)';
      for (var d = 0.1; d <= 0.65; d += 0.02) {
        pts.push([d, (Vin * d * T) / Lm]);
      }
    } else if (idx === 2) {
      var phi = v[0], Ipri = v[1];
      var Deff = phi / 180;
      var Veff = 400 * Deff;
      main = 'Effective duty D_eff = ' + Deff.toFixed(2) + ' | V_out = ' + Veff.toFixed(1) + ' V';
      second = 'Circulating primary reactive energy decreases at higher phase angles';
      xaxis = 'Phase shift angle (°)'; yaxis = 'Effective output (V)';
      for (var a = 0; a <= 180; a += 5) {
        pts.push([a, 400 * (a / 180)]);
      }
    } else if (idx === 3) {
      var fn = v[0], Q = v[1];
      var ln = 5.0; // Lm / Lr
      var denom = Math.sqrt(Math.pow(1 + 1/ln - 1/(ln * fn * fn), 2) + Math.pow(Q * (fn - 1/fn), 2));
      var gain = 1 / (denom || 1);
      main = 'LLC Tank gain M = ' + gain.toFixed(3) + ' at fn=' + fn.toFixed(2);
      second = fn >= 1 ? 'Zero-voltage switching (ZVS) inductive region' : 'Capacitive region (caution: ZCS risk)';
      xaxis = 'Normalized frequency fn'; yaxis = 'Voltage gain M';
      for (var f = 0.5; f <= 2.0; f += 0.03) {
        var d_i = Math.sqrt(Math.pow(1 + 1/ln - 1/(ln * f * f), 2) + Math.pow(Q * (f - 1/f), 2));
        pts.push([f, 1 / (d_i || 1)]);
      }
    } else if (idx === 4) {
      var ma = v[0], mf = v[1];
      var v1 = ma * (400 / 2);
      var thd = ma <= 1.0 ? (5 / (ma * 10)) : (5 + (ma - 1) * 35);
      main = 'Fundamental peak V1 = ' + v1.toFixed(1) + ' V';
      second = 'Estimated carrier THD ≈ ' + thd.toFixed(1) + '% (mf=' + mf + ')';
      xaxis = 'Modulation index ma'; yaxis = 'Fundamental V1 (V)';
      for (var m = 0.2; m <= 1.2; m += 0.02) {
        pts.push([m, m * 200]);
      }
    } else if (idx === 5) {
      var mratio = v[0], deg = v[1];
      var rad = deg * Math.PI / 180;
      var sector = Math.floor(deg / 60) + 1;
      main = 'Sector ' + sector + ' reference trajectory | Modulation |V_ref| = ' + mratio.toFixed(2);
      second = 'Active state durations T1, T2 synthesize rotating stator voltage space vector';
      xaxis = 'Vector angle (°)'; yaxis = 'Reference modulation';
      for (var ang = 0; ang <= 360; ang += 5) {
        pts.push([ang, mratio * Math.sin(ang * Math.PI / 180)]);
      }
    } else if (idx === 6) {
      var ma6 = v[0], vdelta = v[1];
      var levels = 3;
      var stepV = 400 / 2;
      main = 'Phase output: ±' + stepV + 'V and 0V tiers';
      second = 'DC midpoint imbalance: ' + vdelta.toFixed(1) + ' V (requires redundant zero-state switching)';
      xaxis = 'Modulation index ma'; yaxis = 'Phase peak V (V)';
      for (var mm = 0.2; mm <= 1.0; mm += 0.02) {
        pts.push([mm, mm * stepV]);
      }
    } else if (idx === 7) {
      var Vrms = v[0], Pout = v[1];
      var Irms = Pout / (Vrms * 0.99);
      var pf = 0.995;
      main = 'Input RMS current = ' + Irms.toFixed(2) + ' A | Power factor PF ≈ ' + pf.toFixed(3);
      second = 'Boost PFC pre-regulator maintains sinusoidal line current in phase with voltage';
      xaxis = 'Output power (W)'; yaxis = 'Input current (A)';
      for (var p = 100; p <= 1500; p += 30) {
        pts.push([p, p / (Vrms * 0.99)]);
      }
    } else if (idx === 8) {
      var L1 = v[0] * 1e-6, L2 = v[1] * 1e-6, Cf = v[2] * 1e-6;
      var Leq = (L1 * L2) / (L1 + L2);
      var fres = 1 / (2 * Math.PI * Math.sqrt(Leq * Cf));
      main = 'LCL resonance frequency f_res = ' + (fres / 1000).toFixed(2) + ' kHz';
      second = 'Must be placed between 10x grid frequency and 0.5x switching frequency';
      xaxis = 'Filter capacitance (µF)'; yaxis = 'Resonance f_res (kHz)';
      for (var c = 2; c <= 50; c += 1) {
        var fr = 1 / (2 * Math.PI * Math.sqrt(Leq * (c * 1e-6)));
        pts.push([c, fr / 1000]);
      }
    }
    return {main: main, second: second, xaxis: xaxis, yaxis: yaxis, pts: pts};
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

  function renderPE2Plot(plot, res) {
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 320, L = 72, R = 20, T = 20, B = 48;
    var pts = res.pts;
    if (pts.length === 0) return;
    var xs = pts.map(function(p) { return p[0]; }), ys = pts.map(function(p) { return p[1]; });
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
    var ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);
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
      yt.textContent = yv >= 100 ? yv.toFixed(0) : yv.toFixed(1);
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

    var ptsStr = pts.map(function(p) { return px(p[0]).toFixed(1) + ',' + py(p[1]).toFixed(1); }).join(' ');
    plot.appendChild(makeSvgEl('polyline', {
      points: ptsStr,
      fill: 'none',
      stroke: '#0891b2',
      'stroke-width': 2.5,
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round'
    }));

    var xl = makeSvgEl('text', {x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    xl.textContent = res.xaxis;
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {x: 16, y: (H - B + T) / 2, transform: 'rotate(-90 16 ' + ((H - B + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    yl.textContent = res.yaxis;
    plot.appendChild(yl);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Flyback transformer magnetizing reset" + '</h3><p>' + "Discontinuous conduction mode magnetizing energy reset and snubber clamp dissipation." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe2-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe2-1">-</output></div>' +
          '<p class="note" id="out-sec-pe2-1">-</p></div>' +
          '<svg id="plot-pe2-1" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe2-1');
        var mainEl = card.querySelector('#out-main-pe2-1');
        var secEl = card.querySelector('#out-sec-pe2-1');
        var plotEl = card.querySelector('#plot-pe2-1');
        var cfgControls = [["Input DC voltage (V)", 100, 400, 200, 10, "V"], ["Duty cycle D", 0.1, 0.6, 0.4, 0.05, "ratio"], ["Magnetizing L (\u00b5H)", 50, 500, 150, 10, "\u00b5H"]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3] + (c[5] ? ' ' + c[5] : '');
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
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcPE2(1, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Full-bridge phase-shift modulation" + '</h3><p>' + "Phase-shifted full-bridge primary circulating current and zero-voltage turn-on transitions." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe2-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe2-2">-</output></div>' +
          '<p class="note" id="out-sec-pe2-2">-</p></div>' +
          '<svg id="plot-pe2-2" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe2-2');
        var mainEl = card.querySelector('#out-main-pe2-2');
        var secEl = card.querySelector('#out-sec-pe2-2');
        var plotEl = card.querySelector('#plot-pe2-2');
        var cfgControls = [["Phase shift angle (\u00b0)", 0, 180, 90, 5, "\u00b0"], ["Primary load current (A)", 1, 20, 8, 0.5, "A"]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3] + (c[5] ? ' ' + c[5] : '');
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
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcPE2(2, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "LLC series-parallel resonant tank" + '</h3><p>' + "Resonant tank voltage gain and normalized frequency characteristics across load variations." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe2-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe2-3">-</output></div>' +
          '<p class="note" id="out-sec-pe2-3">-</p></div>' +
          '<svg id="plot-pe2-3" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe2-3');
        var mainEl = card.querySelector('#out-main-pe2-3');
        var secEl = card.querySelector('#out-sec-pe2-3');
        var plotEl = card.querySelector('#plot-pe2-3');
        var cfgControls = [["Normalized frequency fn", 0.5, 2.0, 1.0, 0.05, "f/fr"], ["Quality factor Q", 0.2, 5.0, 1.0, 0.1, "Q"]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3] + (c[5] ? ' ' + c[5] : '');
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
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcPE2(3, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Sinusoidal PWM inverter harmonic spectrum" + '</h3><p>' + "Carrier-frequency sideband harmonics and modulation index linear modulation boundary." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe2-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe2-4">-</output></div>' +
          '<p class="note" id="out-sec-pe2-4">-</p></div>' +
          '<svg id="plot-pe2-4" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe2-4');
        var mainEl = card.querySelector('#out-main-pe2-4');
        var secEl = card.querySelector('#out-sec-pe2-4');
        var plotEl = card.querySelector('#plot-pe2-4');
        var cfgControls = [["Modulation index ma", 0.2, 1.2, 0.85, 0.05, "ratio"], ["Frequency ratio mf", 9, 45, 21, 2, "ratio"]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3] + (c[5] ? ' ' + c[5] : '');
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
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcPE2(4, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Space vector PWM (SVPWM) sector trajectories" + '</h3><p>' + "Rotating voltage reference vector decomposition into adjacent stationary active and zero vectors." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe2-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe2-5">-</output></div>' +
          '<p class="note" id="out-sec-pe2-5">-</p></div>' +
          '<svg id="plot-pe2-5" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe2-5');
        var mainEl = card.querySelector('#out-main-pe2-5');
        var secEl = card.querySelector('#out-sec-pe2-5');
        var plotEl = card.querySelector('#plot-pe2-5');
        var cfgControls = [["Vector magnitude ratio", 0.1, 0.95, 0.8, 0.05, "ratio"], ["Electrical angle (\u00b0)", 0, 360, 45, 5, "\u00b0"]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3] + (c[5] ? ' ' + c[5] : '');
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
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcPE2(5, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "Three-level diode-clamped inverter" + '</h3><p>' + "Neutral-point clamped phase voltage synthesis and DC-link capacitor voltage balance." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe2-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe2-6">-</output></div>' +
          '<p class="note" id="out-sec-pe2-6">-</p></div>' +
          '<svg id="plot-pe2-6" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe2-6');
        var mainEl = card.querySelector('#out-main-pe2-6');
        var secEl = card.querySelector('#out-sec-pe2-6');
        var plotEl = card.querySelector('#plot-pe2-6');
        var cfgControls = [["Modulation index ma", 0.2, 1.0, 0.8, 0.05, "ratio"], ["Neutral voltage delta (V)", -20, 20, 0, 1, "V"]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3] + (c[5] ? ' ' + c[5] : '');
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
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcPE2(6, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Active PFC boost converter power factor" + '</h3><p>' + "Continuous conduction mode average current control and input displacement power factor." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe2-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe2-7">-</output></div>' +
          '<p class="note" id="out-sec-pe2-7">-</p></div>' +
          '<svg id="plot-pe2-7" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe2-7');
        var mainEl = card.querySelector('#out-main-pe2-7');
        var secEl = card.querySelector('#out-sec-pe2-7');
        var plotEl = card.querySelector('#plot-pe2-7');
        var cfgControls = [["Line RMS voltage (V)", 90, 260, 230, 5, "V"], ["Output power (W)", 100, 1500, 500, 50, "W"]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3] + (c[5] ? ' ' + c[5] : '');
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
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcPE2(7, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Grid-connected inverter LCL filter resonance" + '</h3><p>' + "Resonance frequency and high-frequency switching attenuation of grid interface LCL filter." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe2-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe2-8">-</output></div>' +
          '<p class="note" id="out-sec-pe2-8">-</p></div>' +
          '<svg id="plot-pe2-8" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe2-8');
        var mainEl = card.querySelector('#out-main-pe2-8');
        var secEl = card.querySelector('#out-sec-pe2-8');
        var plotEl = card.querySelector('#plot-pe2-8');
        var cfgControls = [["Inverter L1 (\u00b5H)", 100, 1000, 350, 25, "\u00b5H"], ["Grid L2 (\u00b5H)", 50, 500, 150, 10, "\u00b5H"], ["Filter C (\u00b5F)", 2, 50, 10, 1, "\u00b5F"]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3] + (c[5] ? ' ' + c[5] : '');
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
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var res = calcPE2(8, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE2Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE2 init error:', err);
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
