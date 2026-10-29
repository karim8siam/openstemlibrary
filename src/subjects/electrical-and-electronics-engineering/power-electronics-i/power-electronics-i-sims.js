/* Power Electronics I Interactive Simulation Suite */
(function(window) {
  'use strict';

  function calcPE1(idx, v) {
    var main = '', second = '', xaxis = 'Parameter', yaxis = 'Output', pts = [];
    if (idx === 1) {
      var I1 = v[0], F1 = v[1], R1 = v[2];
      var loss1 = F1 + R1 * I1 * I1, po1 = 12 * I1, eff1 = 100 * po1 / (po1 + loss1);
      main = eff1.toFixed(2) + '% efficiency';
      second = loss1.toFixed(3) + ' W total loss (P_out=' + po1.toFixed(1) + ' W)';
      xaxis = 'Load current (A)'; yaxis = 'Efficiency (%)';
      for (var k1 = 0.2; k1 <= 5.05; k1 += 0.05) {
        var pl = F1 + R1 * k1 * k1, po = 12 * k1;
        pts.push([k1, 100 * po / (po + pl)]);
      }
    } else if (idx === 2) {
      var I2 = v[0], f2 = v[1] * 1000, D2 = v[2];
      var pcond = 0.025 * I2 * I2 * D2;
      var psw = 2e-7 * 48 * I2 * f2;
      var ptot = pcond + psw;
      main = ptot.toFixed(2) + ' W total loss';
      second = 'Conduction: ' + pcond.toFixed(2) + ' W | Switching: ' + psw.toFixed(2) + ' W';
      xaxis = 'Load current (A)'; yaxis = 'Dissipation (W)';
      for (var k2 = 1; k2 <= 25; k2 += 0.5) {
        pts.push([k2, 0.025 * k2 * k2 * D2 + 2e-7 * 48 * k2 * f2]);
      }
    } else if (idx === 3) {
      var td = v[0] * 1e-9, f3 = v[1] * 1000, I3 = v[2];
      var pd = 2 * td * 0.7 * I3 * f3;
      main = pd.toFixed(3) + ' W diode loss';
      second = 'Conduction time: ' + (2 * td * f3 * 100).toFixed(2) + '% of period';
      xaxis = 'Dead time td (ns)'; yaxis = 'Diode loss (W)';
      for (var k3 = 10; k3 <= 150; k3 += 2) {
        pts.push([k3, 2 * k3 * 1e-9 * 0.7 * I3 * f3]);
      }
    } else if (idx === 4) {
      var I4 = v[0], C4 = v[1] * 1e-6, fline = v[2];
      var rip = I4 / (2 * fline * C4);
      main = rip.toFixed(2) + ' V peak-to-peak ripple';
      second = 'Percent ripple: ' + (rip / 48 * 100).toFixed(1) + '% of nominal 48 V DC';
      xaxis = 'Filter capacitance (µF)'; yaxis = 'Ripple ΔV (V)';
      for (var k4 = 220; k4 <= 4700; k4 += 50) {
        pts.push([k4, I4 / (2 * fline * k4 * 1e-6)]);
      }
    } else if (idx === 5) {
      var L5 = v[0] * 1e-6, fsw5 = v[1] * 1000, Vin5 = v[2];
      var Vout5 = 5.0, D5 = Vout5 / Vin5;
      var dIL = (Vin5 - Vout5) * D5 / (fsw5 * L5);
      var I_crit = dIL / 2;
      main = 'Ripple ΔI_L = ' + dIL.toFixed(2) + ' A';
      second = 'CCM boundary I_crit = ' + I_crit.toFixed(2) + ' A (Duty D=' + D5.toFixed(2) + ')';
      xaxis = 'Inductance L (µH)'; yaxis = 'Ripple ΔI_L (A)';
      for (var k5 = 10; k5 <= 220; k5 += 2) {
        pts.push([k5, (Vin5 - Vout5) * D5 / (fsw5 * k5 * 1e-6)]);
      }
    } else if (idx === 6) {
      var Vin6 = v[0], D6 = v[1];
      var Vout6 = Vin6 / (1 - D6);
      var gain6 = 1 / (1 - D6);
      main = 'V_out = ' + Vout6.toFixed(1) + ' V (Gain=' + gain6.toFixed(2) + 'x)';
      second = 'Inductor current I_in ≈ ' + (2 * gain6).toFixed(1) + ' A for 2 A load';
      xaxis = 'Duty cycle D'; yaxis = 'Output voltage V_out (V)';
      for (var k6 = 0.1; k6 <= 0.85; k6 += 0.01) {
        pts.push([k6, Vin6 / (1 - k6)]);
      }
    } else if (idx === 7) {
      var D7 = v[0], R7 = v[1];
      var L7 = 47e-6;
      var f_rhp = (R7 * Math.pow(1 - D7, 2)) / (2 * Math.PI * L7);
      main = 'RHP zero f_z = ' + (f_rhp / 1000).toFixed(1) + ' kHz';
      second = 'Maximum closed-loop crossover must stay below ' + (f_rhp / 3000).toFixed(1) + ' kHz';
      xaxis = 'Load resistance R (Ω)'; yaxis = 'RHP zero (kHz)';
      for (var k7 = 5; k7 <= 100; k7 += 1) {
        pts.push([k7, (k7 * Math.pow(1 - D7, 2)) / (2 * Math.PI * L7 * 1000)]);
      }
    } else if (idx === 8) {
      var L8 = v[0] * 1e-9, I8 = v[1];
      var dt8 = 10e-9;
      var vspike = L8 * (I8 / dt8);
      main = 'Overvoltage spike ΔV = ' + vspike.toFixed(1) + ' V';
      second = 'Assumes turn-off fall time tf=10 ns. Total switch peak = ' + (48 + vspike).toFixed(1) + ' V';
      xaxis = 'Loop inductance L (nH)'; yaxis = 'Voltage spike ΔV (V)';
      for (var k8 = 2; k8 <= 30; k8 += 0.5) {
        pts.push([k8, k8 * 1e-9 * (I8 / dt8)]);
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

  function renderPE1Plot(plot, res) {
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
      stroke: '#0284c7',
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
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Converter efficiency and output current" + '</h3><p>' + "Loss budget: P_loss = P_fixed + R_eq I\u00b2, \u03b7 = P_out / (P_out + P_loss)." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe1-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe1-1">-</output></div>' +
          '<p class="note" id="out-sec-pe1-1">-</p></div>' +
          '<svg id="plot-pe1-1" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe1-1');
        var mainEl = card.querySelector('#out-main-pe1-1');
        var secEl = card.querySelector('#out-sec-pe1-1');
        var plotEl = card.querySelector('#plot-pe1-1');
        var cfgControls = [["Load current I", 0.2, 5, 2, 0.1, "A"], ["Fixed loss F", 0.1, 2, 0.6, 0.1, "W"], ["Equivalent R", 0.02, 0.3, 0.12, 0.01, "\u03a9"]];
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
          var res = calcPE1(1, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE1Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Device conduction and switching losses" + '</h3><p>' + "Semiconductor dissipation: P_cond = R_ds\u00b7I\u00b2\u00b7D, P_sw = (E_on + E_off)\u00b7f_sw." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe1-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe1-2">-</output></div>' +
          '<p class="note" id="out-sec-pe1-2">-</p></div>' +
          '<svg id="plot-pe1-2" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe1-2');
        var mainEl = card.querySelector('#out-main-pe1-2');
        var secEl = card.querySelector('#out-sec-pe1-2');
        var plotEl = card.querySelector('#plot-pe1-2');
        var cfgControls = [["Current I", 1, 25, 10, 0.5, "A"], ["Switching f (kHz)", 20, 200, 100, 5, "kHz"], ["Duty cycle D", 0.1, 0.9, 0.5, 0.05, ""]];
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
          var res = calcPE1(2, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE1Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "Dead time and body diode conduction" + '</h3><p>' + "Synchronous buck commutation: body diode forward conduction loss during bridge blanking dead time." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe1-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe1-3">-</output></div>' +
          '<p class="note" id="out-sec-pe1-3">-</p></div>' +
          '<svg id="plot-pe1-3" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe1-3');
        var mainEl = card.querySelector('#out-main-pe1-3');
        var secEl = card.querySelector('#out-sec-pe1-3');
        var plotEl = card.querySelector('#plot-pe1-3');
        var cfgControls = [["Dead time td (ns)", 10, 150, 40, 5, "ns"], ["Frequency f (kHz)", 50, 500, 200, 10, "kHz"], ["Inductor current I", 1, 30, 12, 1, "A"]];
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
          var res = calcPE1(3, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE1Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Capacitor-input bridge rectifier ripple" + '</h3><p>' + "Peak-to-peak filter capacitor ripple voltage: \u0394V = I_load / (2 f_line C_filter)." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe1-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe1-4">-</output></div>' +
          '<p class="note" id="out-sec-pe1-4">-</p></div>' +
          '<svg id="plot-pe1-4" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe1-4');
        var mainEl = card.querySelector('#out-main-pe1-4');
        var secEl = card.querySelector('#out-sec-pe1-4');
        var plotEl = card.querySelector('#plot-pe1-4');
        var cfgControls = [["Load current I", 0.5, 10, 3, 0.25, "A"], ["Filter C (\u00b5F)", 220, 4700, 1000, 50, "\u00b5F"], ["Line frequency (Hz)", 50, 60, 50, 10, "Hz"]];
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
          var res = calcPE1(4, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE1Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Buck inductor ripple and CCM boundary" + '</h3><p>' + "Inductor current ripple \u0394I_L = (V_in - V_out)\u00b7D / (f_sw\u00b7L) and critical boundary current." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe1-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe1-5">-</output></div>' +
          '<p class="note" id="out-sec-pe1-5">-</p></div>' +
          '<svg id="plot-pe1-5" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe1-5');
        var mainEl = card.querySelector('#out-main-pe1-5');
        var secEl = card.querySelector('#out-sec-pe1-5');
        var plotEl = card.querySelector('#plot-pe1-5');
        var cfgControls = [["Inductance L (\u00b5H)", 10, 220, 47, 5, "\u00b5H"], ["Switching f (kHz)", 50, 500, 200, 10, "kHz"], ["Input voltage V", 12, 48, 24, 1, "V"]];
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
          var res = calcPE1(5, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE1Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "Boost conversion ratio and input current" + '</h3><p>' + "Ideal voltage gain V_out / V_in = 1 / (1 - D) and average inductor input current." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe1-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe1-6">-</output></div>' +
          '<p class="note" id="out-sec-pe1-6">-</p></div>' +
          '<svg id="plot-pe1-6" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe1-6');
        var mainEl = card.querySelector('#out-main-pe1-6');
        var secEl = card.querySelector('#out-sec-pe1-6');
        var plotEl = card.querySelector('#plot-pe1-6');
        var cfgControls = [["Input voltage V", 5, 24, 12, 1, "V"], ["Duty cycle D", 0.1, 0.85, 0.5, 0.05, ""]];
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
          var res = calcPE1(6, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE1Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Boost right-half-plane zero frequency" + '</h3><p>' + "Small-signal control dynamic: RHP zero \u03c9_z = R_load\u00b7(1 - D)\u00b2 / L limits feedback bandwidth." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe1-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe1-7">-</output></div>' +
          '<p class="note" id="out-sec-pe1-7">-</p></div>' +
          '<svg id="plot-pe1-7" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe1-7');
        var mainEl = card.querySelector('#out-main-pe1-7');
        var secEl = card.querySelector('#out-sec-pe1-7');
        var plotEl = card.querySelector('#plot-pe1-7');
        var cfgControls = [["Duty cycle D", 0.2, 0.8, 0.5, 0.05, "ratio"], ["Load R (\u03a9)", 5, 100, 25, 2, "\u03a9"]];
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
          var res = calcPE1(7, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE1Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Parasitic inductance and switching spike" + '</h3><p>' + "Switch-node overvoltage transient: \u0394V_spike = L_loop \u00b7 (di/dt) during fast turn-off." + '</p></div>' +
          '<div class="sim-controls" id="controls-pe1-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe1-8">-</output></div>' +
          '<p class="note" id="out-sec-pe1-8">-</p></div>' +
          '<svg id="plot-pe1-8" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-pe1-8');
        var mainEl = card.querySelector('#out-main-pe1-8');
        var secEl = card.querySelector('#out-sec-pe1-8');
        var plotEl = card.querySelector('#plot-pe1-8');
        var cfgControls = [["Loop inductance L (nH)", 2, 30, 8, 1, "nH"], ["Current I (A)", 2, 40, 15, 1, "A"]];
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
          var res = calcPE1(8, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE1Plot(plotEl, res);
        }
        update();
      } catch (err) {
        console.warn('PE1 init error:', err);
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
