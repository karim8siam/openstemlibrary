import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793271497058_746381a5.zip'

print("Generating Batch 4 EEE Simulation Suites...")

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
# 1. POWER ELECTRONICS I
# ==============================================================================
print("Generating power-electronics-i-sims.js...")

pe1_configs = [
  {"title": "Converter efficiency and output current", "desc": "Loss budget: P_loss = P_fixed + R_eq I², η = P_out / (P_out + P_loss).", "controls": [["Load current I", 0.2, 5, 2, 0.1, "A"], ["Fixed loss F", 0.1, 2, 0.6, 0.1, "W"], ["Equivalent R", 0.02, 0.3, 0.12, 0.01, "Ω"]]},
  {"title": "Device conduction and switching losses", "desc": "Semiconductor dissipation: P_cond = R_ds·I²·D, P_sw = (E_on + E_off)·f_sw.", "controls": [["Current I", 1, 25, 10, 0.5, "A"], ["Switching f (kHz)", 20, 200, 100, 5, "kHz"], ["Duty cycle D", 0.1, 0.9, 0.5, 0.05, ""]]},
  {"title": "Dead time and body diode conduction", "desc": "Synchronous buck commutation: body diode forward conduction loss during bridge blanking dead time.", "controls": [["Dead time td (ns)", 10, 150, 40, 5, "ns"], ["Frequency f (kHz)", 50, 500, 200, 10, "kHz"], ["Inductor current I", 1, 30, 12, 1, "A"]]},
  {"title": "Capacitor-input bridge rectifier ripple", "desc": "Peak-to-peak filter capacitor ripple voltage: ΔV = I_load / (2 f_line C_filter).", "controls": [["Load current I", 0.5, 10, 3, 0.25, "A"], ["Filter C (µF)", 220, 4700, 1000, 50, "µF"], ["Line frequency (Hz)", 50, 60, 50, 10, "Hz"]]},
  {"title": "Buck inductor ripple and CCM boundary", "desc": "Inductor current ripple ΔI_L = (V_in - V_out)·D / (f_sw·L) and critical boundary current.", "controls": [["Inductance L (µH)", 10, 220, 47, 5, "µH"], ["Switching f (kHz)", 50, 500, 200, 10, "kHz"], ["Input voltage V", 12, 48, 24, 1, "V"]]},
  {"title": "Boost conversion ratio and input current", "desc": "Ideal voltage gain V_out / V_in = 1 / (1 - D) and average inductor input current.", "controls": [["Input voltage V", 5, 24, 12, 1, "V"], ["Duty cycle D", 0.1, 0.85, 0.5, 0.05, ""]]},
  {"title": "Boost right-half-plane zero frequency", "desc": "Small-signal control dynamic: RHP zero ω_z = R_load·(1 - D)² / L limits feedback bandwidth.", "controls": [["Duty cycle D", 0.2, 0.8, 0.5, 0.05, "ratio"], ["Load R (Ω)", 5, 100, 25, 2, "Ω"]]},
  {"title": "Parasitic inductance and switching spike", "desc": "Switch-node overvoltage transient: ΔV_spike = L_loop · (di/dt) during fast turn-off.", "controls": [["Loop inductance L (nH)", 2, 30, 8, 1, "nH"], ["Current I (A)", 2, 40, 15, 1, "A"]]}
]

pe1_js = """/* Power Electronics I Interactive Simulation Suite */
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
"""

for idx, item in enumerate(pe1_configs, 1):
    u = idx
    ctrls_json = json.dumps(item["controls"])
    title_esc = json.dumps(item["title"])
    desc_esc = json.dumps(item["desc"])
    pe1_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {desc_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-pe1-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe1-{idx}">-</output></div>' +
          '<p class="note" id="out-sec-pe1-{idx}">-</p></div>' +
          '<svg id="plot-pe1-{idx}" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-pe1-{idx}');
        var mainEl = card.querySelector('#out-main-pe1-{idx}');
        var secEl = card.querySelector('#out-sec-pe1-{idx}');
        var plotEl = card.querySelector('#plot-pe1-{idx}');
        var cfgControls = {ctrls_json};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {{
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
          inp.addEventListener('input', function() {{
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          }});
        }});

        function update() {{
          var v = inputs.map(function(el) {{ return Number(el.value); }});
          var res = calcPE1({idx}, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE1Plot(plotEl, res);
        }}
        update();
      }} catch (err) {{
        console.warn('PE1 init error:', err);
      }}
    }}
  }});
"""

pe1_js += ENGINE_FOOTER

pe1_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'power-electronics-i', 'power-electronics-i-sims.js')
with open(pe1_out, 'w', encoding='utf-8') as f:
    f.write(pe1_js)
print(f"Saved {pe1_out} ({len(pe1_js)} bytes)")

# ==============================================================================
# 2. POWER ELECTRONICS II
# ==============================================================================
print("Generating power-electronics-ii-sims.js...")

pe2_configs = [
  {"title": "Flyback transformer magnetizing reset", "desc": "Discontinuous conduction mode magnetizing energy reset and snubber clamp dissipation.", "controls": [["Input DC voltage (V)", 100, 400, 200, 10, "V"], ["Duty cycle D", 0.1, 0.6, 0.4, 0.05, "ratio"], ["Magnetizing L (µH)", 50, 500, 150, 10, "µH"]]},
  {"title": "Full-bridge phase-shift modulation", "desc": "Phase-shifted full-bridge primary circulating current and zero-voltage turn-on transitions.", "controls": [["Phase shift angle (°)", 0, 180, 90, 5, "°"], ["Primary load current (A)", 1, 20, 8, 0.5, "A"]]},
  {"title": "LLC series-parallel resonant tank", "desc": "Resonant tank voltage gain and normalized frequency characteristics across load variations.", "controls": [["Normalized frequency fn", 0.5, 2.0, 1.0, 0.05, "f/fr"], ["Quality factor Q", 0.2, 5.0, 1.0, 0.1, "Q"]]},
  {"title": "Sinusoidal PWM inverter harmonic spectrum", "desc": "Carrier-frequency sideband harmonics and modulation index linear modulation boundary.", "controls": [["Modulation index ma", 0.2, 1.2, 0.85, 0.05, "ratio"], ["Frequency ratio mf", 9, 45, 21, 2, "ratio"]]},
  {"title": "Space vector PWM (SVPWM) sector trajectories", "desc": "Rotating voltage reference vector decomposition into adjacent stationary active and zero vectors.", "controls": [["Vector magnitude ratio", 0.1, 0.95, 0.8, 0.05, "ratio"], ["Electrical angle (°)", 0, 360, 45, 5, "°"]]},
  {"title": "Three-level diode-clamped inverter", "desc": "Neutral-point clamped phase voltage synthesis and DC-link capacitor voltage balance.", "controls": [["Modulation index ma", 0.2, 1.0, 0.8, 0.05, "ratio"], ["Neutral voltage delta (V)", -20, 20, 0, 1, "V"]]},
  {"title": "Active PFC boost converter power factor", "desc": "Continuous conduction mode average current control and input displacement power factor.", "controls": [["Line RMS voltage (V)", 90, 260, 230, 5, "V"], ["Output power (W)", 100, 1500, 500, 50, "W"]]},
  {"title": "Grid-connected inverter LCL filter resonance", "desc": "Resonance frequency and high-frequency switching attenuation of grid interface LCL filter.", "controls": [["Inverter L1 (µH)", 100, 1000, 350, 25, "µH"], ["Grid L2 (µH)", 50, 500, 150, 10, "µH"], ["Filter C (µF)", 2, 50, 10, 1, "µF"]]}
]

pe2_js = """/* Power Electronics II Interactive Simulation Suite */
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
"""

for idx, item in enumerate(pe2_configs, 1):
    u = idx
    ctrls_json = json.dumps(item["controls"])
    title_esc = json.dumps(item["title"])
    desc_esc = json.dumps(item["desc"])
    pe2_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {desc_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-pe2-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Performance</small><output id="out-main-pe2-{idx}">-</output></div>' +
          '<p class="note" id="out-sec-pe2-{idx}">-</p></div>' +
          '<svg id="plot-pe2-{idx}" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-pe2-{idx}');
        var mainEl = card.querySelector('#out-main-pe2-{idx}');
        var secEl = card.querySelector('#out-sec-pe2-{idx}');
        var plotEl = card.querySelector('#plot-pe2-{idx}');
        var cfgControls = {ctrls_json};
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {{
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
          inp.addEventListener('input', function() {{
            valSpan.textContent = inp.value + (c[5] ? ' ' + c[5] : '');
            update();
          }});
        }});

        function update() {{
          var v = inputs.map(function(el) {{ return Number(el.value); }});
          var res = calcPE2({idx}, v);
          if (mainEl) mainEl.textContent = res.main;
          if (secEl) secEl.textContent = res.second;
          if (plotEl) renderPE2Plot(plotEl, res);
        }}
        update();
      }} catch (err) {{
        console.warn('PE2 init error:', err);
      }}
    }}
  }});
"""

pe2_js += ENGINE_FOOTER

pe2_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'power-electronics-ii', 'power-electronics-ii-sims.js')
with open(pe2_out, 'w', encoding='utf-8') as f:
    f.write(pe2_js)
print(f"Saved {pe2_out} ({len(pe2_js)} bytes)")

# ==============================================================================
# 3. ELECTRICAL MEASUREMENTS & INSTRUMENTATION I
# ==============================================================================
print("Generating electrical-measurements-and-instrumentation-i-sims.js...")

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    emi1_raw = z.read("OpenSTEM-Electrical-and-Electronics-Engineering/books/electrical-measurements-and-instrumentation-i/simulations/models.js").decode("utf-8")

# Extract defs object
defs_start = emi1_raw.find("const defs={")
defs_end = emi1_raw.find(";\nfunction run()", defs_start)
emi1_defs_js = emi1_raw[defs_start:defs_end+1]

emi1_titles = [
  ("Measurement uncertainty propagation", "Evaluate Type A and Type B combined standard uncertainty and expanded uncertainty bounds."),
  ("Voltmeter loading and input resistance", "Observe meter loading error as voltmeter internal resistance compares with source Thevenin impedance."),
  ("Wheatstone DC bridge balance sensitivity", "Balance condition Rx = R2·R3/R1 and galvanometer deflection off null balance."),
  ("Current transformer (CT) secondary burden", "Secondary winding current and VA burden under primary load variations."),
  ("Electrodynamic wattmeter phase angle", "Power measurement accuracy and power factor sensitivity under reactive phase shift."),
  ("Maxwell-Wien AC bridge balance", "Measure unknown inductance and series resistance via standard capacitance arm."),
  ("Schering capacitance and dielectric loss", "Dissipation factor tan δ determination and high-voltage capacitance bridge balance."),
  ("Search-coil magnetic fluxmeter deflection", "Flux linkage integration and induced voltage ballistic galvanometer trajectory.")
]

emi1_inputs = [
  [["Type A u (V)", 0.01, 1.0, 0.25, 0.01], ["Type B u (V)", 0.01, 1.0, 0.40, 0.01], ["Other u (V)", 0.0, 0.5, 0.10, 0.01], ["Coverage k", 1.0, 3.0, 2.0, 0.5]],
  [["Thevenin V (V)", 1, 100, 10, 1], ["Source R (kΩ)", 1, 100, 20, 1], ["Meter R (kΩ)", 10, 1000, 200, 10], ["Scale factor", 0.5, 1.5, 1.0, 0.1]],
  [["Excitation V", 1, 24, 10, 1], ["R1 (Ω)", 10, 500, 100, 5], ["R2 (Ω)", 10, 500, 100, 5], ["R3 (Ω)", 10, 500, 100, 5], ["Rx (Ω)", 50, 150, 100, 1]],
  [["Primary I (A)", 10, 500, 100, 5], ["CT ratio N", 10, 100, 20, 5], ["Burden R (Ω)", 0.1, 5.0, 1.0, 0.1], ["Cable R (Ω)", 0.05, 1.0, 0.2, 0.05]],
  [["Frequency (Hz)", 10, 100, 50, 5], ["Sample rate (Hz)", 100, 2000, 500, 50], ["Phase (°)", 0, 90, 30, 5], ["Amplitude", 1, 10, 5, 0.5]],
  [["R1 (Ω)", 100, 5000, 1000, 50], ["R2 (Ω)", 100, 5000, 1000, 50], ["R3 (Ω)", 100, 5000, 1000, 50], ["C3 (µF)", 0.01, 2.0, 0.1, 0.01]],
  [["Frequency (Hz)", 50, 1000, 50, 10], ["C1 (nF)", 1, 100, 10, 1], ["R1 (kΩ)", 1, 100, 10, 1], ["Loss factor", 0.001, 0.1, 0.02, 0.001]],
  [["Coil turns N", 10, 500, 100, 10], ["Area A (cm²)", 1, 50, 10, 1], ["Flux change ΔB (T)", 0.05, 2.0, 0.8, 0.05], ["Resistance R (Ω)", 10, 200, 50, 5]]
]

emi1_js = f"""/* Electrical Measurements & Instrumentation I Interactive Simulation Suite */
(function(window) {{
  'use strict';

  {emi1_defs_js}

  function makeSvgEl(tag, attrs) {{
    var el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) {{
      if (Object.prototype.hasOwnProperty.call(attrs, k)) {{
        el.setAttribute(k, String(attrs[k]));
      }}
    }}
    return el;
  }}

  function renderEMI1Plot(plot, id, res) {{
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 320, L = 72, R = 20, T = 20, B = 48;
    var pts = res.points ? res.points.filter(function(p) {{ return Number.isFinite(p.x) && Number.isFinite(p.y); }}) : [];
    if (pts.length === 0) return;
    var xs = pts.map(function(p) {{ return p.x; }}), ys = pts.map(function(p) {{ return p.y; }});
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
    var ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);
    if (ymax === ymin) {{ ymax += 1; ymin -= 1; }}
    else {{ var pad = (ymax - ymin) * 0.1; ymin -= pad; ymax += pad; }}
    if (xmax === xmin) xmax = xmin + 1;

    var px = function(x) {{ return L + (W - L - R) * (x - xmin) / (xmax - xmin); }};
    var py = function(y) {{ return T + (H - T - B) * (ymax - y) / (ymax - ymin); }};

    for (var i = 0; i <= 4; i++) {{
      var gy = T + i * (H - T - B) / 4;
      var yv = ymax - i * (ymax - ymin) / 4;
      plot.appendChild(makeSvgEl('line', {{x1: L, y1: gy, x2: W - R, y2: gy, stroke: '#e2e8f0'}}));
      var yt = makeSvgEl('text', {{x: L - 8, y: gy + 4, fill: '#64748b', 'text-anchor': 'end', 'font-size': 11}});
      yt.textContent = yv.toPrecision(3);
      plot.appendChild(yt);
    }}
    for (var j = 0; j <= 5; j++) {{
      var gx = L + j * (W - L - R) / 5;
      var xv = xmin + j * (xmax - xmin) / 5;
      plot.appendChild(makeSvgEl('line', {{x1: gx, y1: T, x2: gx, y2: H - B, stroke: '#f1f5f9'}}));
      var xt = makeSvgEl('text', {{x: gx, y: H - B + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11}});
      xt.textContent = xv.toPrecision(3);
      plot.appendChild(xt);
    }}

    var ptsStr = pts.map(function(p) {{ return px(p.x).toFixed(1) + ',' + py(p.y).toFixed(1); }}).join(' ');
    plot.appendChild(makeSvgEl('polyline', {{
      points: ptsStr,
      fill: 'none',
      stroke: '#0369a1',
      'stroke-width': 2.5,
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round'
    }}));

    var xl = makeSvgEl('text', {{x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12}});
    xl.textContent = 'Sweep parameter: ' + xmin.toPrecision(3) + ' → ' + xmax.toPrecision(3);
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {{x: 16, y: (H - B + T) / 2, transform: 'rotate(-90 16 ' + ((H - B + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12}});
    yl.textContent = 'Meter response';
    plot.appendChild(yl);
  }}

  var MODELS = [];
"""

for idx, (title, desc) in enumerate(emi1_titles, 1):
    u = idx
    ctrls_json = json.dumps(emi1_inputs[idx - 1])
    title_esc = json.dumps(title)
    desc_esc = json.dumps(desc)
    emi1_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {desc_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-emi1-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Measurement Output</small><output id="out-metric-emi1-{idx}">-</output></div></div>' +
          '<svg id="plot-emi1-{idx}" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-emi1-{idx}');
        var metricEl = card.querySelector('#out-metric-emi1-{idx}');
        var plotEl = card.querySelector('#plot-emi1-{idx}');
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
          var def = defs[{idx}];
          if (def && def.calc) {{
            var res = def.calc(v);
            if (metricEl) metricEl.textContent = res.text;
            if (plotEl) renderEMI1Plot(plotEl, {idx}, res);
          }}
        }}
        update();
      }} catch (err) {{
        console.warn('EMI1 init error:', err);
      }}
    }}
  }});
"""

emi1_js += ENGINE_FOOTER

emi1_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'electrical-measurements-and-instrumentation-i', 'electrical-measurements-and-instrumentation-i-sims.js')
with open(emi1_out, 'w', encoding='utf-8') as f:
    f.write(emi1_js)
print(f"Saved {emi1_out} ({len(emi1_js)} bytes)")

# ==============================================================================
# 4. ELECTRICAL MEASUREMENTS & INSTRUMENTATION II
# ==============================================================================
print("Generating electrical-measurements-and-instrumentation-ii-sims.js...")

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    emi2_raw = z.read("OpenSTEM-Electrical-and-Electronics-Engineering/books/electrical-measurements-and-instrumentation-ii/simulations/model-01.html").decode("utf-8")

s_start = emi2_raw.find("const numeric=")
s_end = emi2_raw.find("};\nconst d=", s_start) + 2
emi2_models_js = emi2_raw[s_start:s_end]

emi2_titles = [
  ("Nonlinear sensor transfer function and sensitivity", "Quadratic RTD/thermistor curve fitting, voltage sensitivity, and Taylor series error bounds."),
  ("Clock drift and counter time error", "Time-interval measurement drift, ppm crystal oscillator stability, and cumulative timing bias."),
  ("Multichannel DAQ sampling and skew", "Sequential multiplexer channel-to-channel time skew and phase error at elevated frequencies."),
  ("Complex impedance spectroscopy", "Cole-Cole dielectric relaxation plot and RC network equivalent impedance circle."),
  ("Lock-in amplifier phase-sensitive detection", "Synchronous demodulation and narrow-band noise rejection of microvolt transducer signals."),
  ("ADC quantization and harmonic distortion", "Successive-approximation ADC quantization noise floor, SNR, and effective number of bits (ENOB)."),
  ("Strain gauge bridge conditioning and non-linearity", "Quarter-bridge and full-bridge strain measurement, lead resistance cancellation, and Poisson ratio."),
  ("Virtual instrument automated measurement loop", "SCPI trigger latency, data buffer throughput, and GPIB/USB communication timing.")
]

emi2_inputs = [
  [["Temperature T (°C)", 0, 100, 25, 1], ["Offset a (V)", 0.0, 1.0, 0.1, 0.01], ["Gain b (V/°C)", 0.005, 0.05, 0.02, 0.001], ["Curvature c", -0.0001, 0.0001, 0.00002, 0.000005]],
  [["Crystal ppm", -50, 50, 15, 1], ["Duration (hours)", 1, 48, 12, 1], ["Initial offset (ms)", -5, 5, 0.5, 0.1], ["Ref ppm", -10, 10, 0, 1]],
  [["Channel count", 2, 16, 4, 1], ["Sample rate (kSa/s)", 10, 500, 100, 10], ["Signal f (kHz)", 1, 50, 10, 1], ["Amplitude", 0.5, 5, 2, 0.5]],
  [["R series (Ω)", 10, 500, 100, 5], ["R parallel (kΩ)", 1, 100, 10, 1], ["C (nF)", 1, 100, 10, 1], ["Frequency (kHz)", 0.1, 100, 5, 0.5]],
  [["Signal amp (mV)", 0.1, 10, 1.0, 0.1], ["Noise amp (mV)", 1, 50, 20, 1], ["Ref phase (°)", 0, 180, 0, 5], ["Filter time const (ms)", 10, 500, 100, 10]],
  [["ADC resolution (bits)", 4, 16, 8, 1], ["Input amp (V)", 0.1, 5.0, 2.5, 0.1], ["Full scale (V)", 1.0, 10.0, 5.0, 0.5], ["Harmonic factor", 0.0, 0.2, 0.02, 0.005]],
  [["Strain ε (µε)", 10, 2000, 500, 20], ["Gauge factor GF", 1.5, 4.0, 2.1, 0.1], ["Excitation V (V)", 1, 15, 5, 0.5], ["Bridge type (1=q,4=f)", 1, 4, 1, 3]],
  [["Command rate (cmd/s)", 10, 500, 100, 10], ["Buffer size", 64, 2048, 256, 64], ["Transfer mode", 1, 3, 1, 1], ["Payload bytes", 16, 1024, 128, 16]]
]

emi2_js = f"""/* Electrical Measurements & Instrumentation II Interactive Simulation Suite */
(function(window) {{
  'use strict';

  {emi2_models_js}

  function makeSvgEl(tag, attrs) {{
    var el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) {{
      if (Object.prototype.hasOwnProperty.call(attrs, k)) {{
        el.setAttribute(k, String(attrs[k]));
      }}
    }}
    return el;
  }}

  function renderEMI2Plot(plot, id, res) {{
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 320, L = 72, R = 20, T = 20, B = 48;
    var pts = res.points ? res.points.filter(function(p) {{ return Number.isFinite(p.x) && Number.isFinite(p.y); }}) : [];
    if (pts.length === 0) return;
    var xs = pts.map(function(p) {{ return p.x; }}), ys = pts.map(function(p) {{ return p.y; }});
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
    var ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);
    if (ymax === ymin) {{ ymax += 1; ymin -= 1; }}
    else {{ var pad = (ymax - ymin) * 0.1; ymin -= pad; ymax += pad; }}
    if (xmax === xmin) xmax = xmin + 1;

    var px = function(x) {{ return L + (W - L - R) * (x - xmin) / (xmax - xmin); }};
    var py = function(y) {{ return T + (H - T - B) * (ymax - y) / (ymax - ymin); }};

    for (var i = 0; i <= 4; i++) {{
      var gy = T + i * (H - T - B) / 4;
      var yv = ymax - i * (ymax - ymin) / 4;
      plot.appendChild(makeSvgEl('line', {{x1: L, y1: gy, x2: W - R, y2: gy, stroke: '#e2e8f0'}}));
      var yt = makeSvgEl('text', {{x: L - 8, y: gy + 4, fill: '#64748b', 'text-anchor': 'end', 'font-size': 11}});
      yt.textContent = yv.toPrecision(3);
      plot.appendChild(yt);
    }}
    for (var j = 0; j <= 5; j++) {{
      var gx = L + j * (W - L - R) / 5;
      var xv = xmin + j * (xmax - xmin) / 5;
      plot.appendChild(makeSvgEl('line', {{x1: gx, y1: T, x2: gx, y2: H - B, stroke: '#f1f5f9'}}));
      var xt = makeSvgEl('text', {{x: gx, y: H - B + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11}});
      xt.textContent = xv.toPrecision(3);
      plot.appendChild(xt);
    }}

    var ptsStr = pts.map(function(p) {{ return px(p.x).toFixed(1) + ',' + py(p.y).toFixed(1); }}).join(' ');
    plot.appendChild(makeSvgEl('polyline', {{
      points: ptsStr,
      fill: 'none',
      stroke: '#0d9488',
      'stroke-width': 2.5,
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round'
    }}));

    var xl = makeSvgEl('text', {{x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12}});
    xl.textContent = 'Parameter span: ' + xmin.toPrecision(3) + ' → ' + xmax.toPrecision(3);
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {{x: 16, y: (H - B + T) / 2, transform: 'rotate(-90 16 ' + ((H - B + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12}});
    yl.textContent = 'Instrument response';
    plot.appendChild(yl);
  }}

  var MODELS = [];
"""

for idx, (title, desc) in enumerate(emi2_titles, 1):
    u = idx
    ctrls_json = json.dumps(emi2_inputs[idx - 1])
    title_esc = json.dumps(title)
    desc_esc = json.dumps(desc)
    emi2_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {desc_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-emi2-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metric</small><output id="out-metric-emi2-{idx}">-</output></div></div>' +
          '<svg id="plot-emi2-{idx}" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-emi2-{idx}');
        var metricEl = card.querySelector('#out-metric-emi2-{idx}');
        var plotEl = card.querySelector('#plot-emi2-{idx}');
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
          var mFn = models[{idx}];
          if (mFn) {{
            var res = mFn(v);
            if (metricEl) metricEl.textContent = res.message;
            if (plotEl) renderEMI2Plot(plotEl, {idx}, res);
          }}
        }}
        update();
      }} catch (err) {{
        console.warn('EMI2 init error:', err);
      }}
    }}
  }});
"""

emi2_js += ENGINE_FOOTER

emi2_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'electrical-measurements-and-instrumentation-ii', 'electrical-measurements-and-instrumentation-ii-sims.js')
with open(emi2_out, 'w', encoding='utf-8') as f:
    f.write(emi2_js)
print(f"Saved {emi2_out} ({len(emi2_js)} bytes)")

# ==============================================================================
# 5. HIGH VOLTAGE ENGINEERING I
# ==============================================================================
print("Generating high-voltage-engineering-i-sims.js...")

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    hve1_raw = z.read("OpenSTEM-Electrical-and-Electronics-Engineering/books/high-voltage-engineering-i/simulations/model.js").decode("utf-8")

# Extract calculate function
calc_start = hve1_raw.find("function calculate(a,b){")
calc_end = hve1_raw.find("\nfunction redraw()", calc_start)
hve1_calc_js = hve1_raw[calc_start:calc_end]

hve1_configs = [
  {"title": "Coaxial electrode electric field distribution", "desc": "Radial electric field stress E(r) = V / (r·ln(b/a)) and maximum surface gradient at inner conductor.", "controls": [["Applied voltage V (kV)", 10, 200, 100, 5], ["Inner radius a (mm)", 1, 10, 4, 0.5]]},
  {"title": "Paschen curve for gaseous dielectric breakdown", "desc": "Breakdown voltage V_b versus pressure-distance product p·d in uniform fields.", "controls": [["Log10(p·d) (torr·cm)", -0.3, 2.5, 0.8, 0.05], ["Second coefficient γ", 0.001, 0.1, 0.02, 0.005]]},
  {"title": "Liquid dielectric dielectric loss and dissipation", "desc": "Dielectric power loss P = 2π f C V² tan δ across frequency in insulating oil.", "controls": [["Tan delta dissipation", 0.001, 0.05, 0.005, 0.001], ["Frequency f (Hz)", 10, 500, 50, 10]]},
  {"title": "Solid insulation electromechanical breakdown", "desc": "Stark-Garton electrostatic compressive stress vs elastic modulus and critical field.", "controls": [["Young modulus Y (MPa)", 100, 5000, 1000, 50], ["Thickness d (mm)", 0.1, 5.0, 1.0, 0.1]]},
  {"title": "Cockcroft-Walton multi-stage voltage multiplier", "desc": "Output DC voltage, regulation drop ΔV = I/(f·C)·(2n³/3 + n²/2), and stage ripple.", "controls": [["Stage count n", 2, 12, 6, 1], ["Load current I (mA)", 0.1, 10, 2, 0.1]]},
  {"title": "Series resonant test transformer tuning", "desc": "Variable-inductance series resonance tuning and test specimen capacitive quality factor Q.", "controls": [["Test specimen C (nF)", 1, 50, 10, 1], ["Resonance tuning L (H)", 1, 50, 25, 1]]},
  {"title": "Standard 1.2/50 µs impulse waveform shaping", "desc": "Double-exponential lightning impulse wave: V(t) = V0·(e^(-α t) - e^(-β t)).", "controls": [["Wavefront resistor R1 (Ω)", 50, 500, 150, 10], ["Wavetail resistor R2 (Ω)", 500, 5000, 2000, 50]]},
  {"title": "Multi-stage Marx impulse generator discharge", "desc": "Parallel charging at V0 and spark-gap series discharge into capacitive divider burden.", "controls": [["Marx stages n", 2, 16, 8, 1], ["Stage charging V0 (kV)", 20, 100, 50, 5]]}
]

hve1_js = f"""/* High Voltage Engineering I Interactive Simulation Suite */
(function(window) {{
  'use strict';

  var lin = function(a, b, n) {{
    if (n === undefined) n = 130;
    return Array.from({{length: n}}, function(_, i) {{ return a + (b - a) * i / (n - 1); }});
  }};

  var paschen = function(pd, g) {{
    var den = Math.log(15 * pd) - Math.log(Math.log(1 + 1 / g));
    return den > 0 ? 365 * pd / den : NaN;
  }};

  var idx = 1;

  {hve1_calc_js}

  function makeSvgEl(tag, attrs) {{
    var el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) {{
      if (Object.prototype.hasOwnProperty.call(attrs, k)) {{
        el.setAttribute(k, String(attrs[k]));
      }}
    }}
    return el;
  }}

  function renderHVE1Plot(plot, res) {{
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 320, L = 72, R = 20, T = 20, B = 48;
    var xs = res.xs, ys = res.ys;
    var validPts = [];
    for (var k = 0; k < xs.length; k++) {{
      if (Number.isFinite(xs[k]) && Number.isFinite(ys[k])) validPts.push([xs[k], ys[k]]);
    }}
    if (validPts.length === 0) return;
    var pXs = validPts.map(function(p) {{ return p[0]; }}), pYs = validPts.map(function(p) {{ return p[1]; }});
    var xmin = Math.min.apply(null, pXs), xmax = Math.max.apply(null, pXs);
    var ymin = Math.min.apply(null, pYs), ymax = Math.max.apply(null, pYs);
    if (ymax === ymin) {{ ymax += 1; ymin -= 1; }}
    else {{ var pad = (ymax - ymin) * 0.1; ymin -= pad; ymax += pad; }}
    if (xmax === xmin) xmax = xmin + 1;

    var px = function(x) {{ return L + (W - L - R) * (x - xmin) / (xmax - xmin); }};
    var py = function(y) {{ return T + (H - T - B) * (ymax - y) / (ymax - ymin); }};

    for (var i = 0; i <= 4; i++) {{
      var gy = T + i * (H - T - B) / 4;
      var yv = ymax - i * (ymax - ymin) / 4;
      plot.appendChild(makeSvgEl('line', {{x1: L, y1: gy, x2: W - R, y2: gy, stroke: '#e2e8f0'}}));
      var yt = makeSvgEl('text', {{x: L - 8, y: gy + 4, fill: '#64748b', 'text-anchor': 'end', 'font-size': 11}});
      yt.textContent = yv.toPrecision(3);
      plot.appendChild(yt);
    }}
    for (var j = 0; j <= 5; j++) {{
      var gx = L + j * (W - L - R) / 5;
      var xv = xmin + j * (xmax - xmin) / 5;
      plot.appendChild(makeSvgEl('line', {{x1: gx, y1: T, x2: gx, y2: H - B, stroke: '#f1f5f9'}}));
      var xt = makeSvgEl('text', {{x: gx, y: H - B + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11}});
      xt.textContent = xv.toPrecision(3);
      plot.appendChild(xt);
    }}

    var ptsStr = validPts.map(function(p) {{ return px(p[0]).toFixed(1) + ',' + py(p[1]).toFixed(1); }}).join(' ');
    plot.appendChild(makeSvgEl('polyline', {{
      points: ptsStr,
      fill: 'none',
      stroke: '#0284c7',
      'stroke-width': 2.5,
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round'
    }}));

    var xl = makeSvgEl('text', {{x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12}});
    xl.textContent = res.xl || 'Parameter';
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {{x: 16, y: (H - B + T) / 2, transform: 'rotate(-90 16 ' + ((H - B + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12}});
    yl.textContent = res.yl || 'Response';
    plot.appendChild(yl);
  }}

  var MODELS = [];
"""

for idx, item in enumerate(hve1_configs, 1):
    u = idx
    ctrls_json = json.dumps(item["controls"])
    title_esc = json.dumps(item["title"])
    desc_esc = json.dumps(item["desc"])
    hve1_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {desc_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-hve1-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Stress & Rating</small><output id="out-metric-hve1-{idx}">-</output></div>' +
          '<p class="note" id="out-valid-hve1-{idx}">-</p></div>' +
          '<svg id="plot-hve1-{idx}" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-hve1-{idx}');
        var metricEl = card.querySelector('#out-metric-hve1-{idx}');
        var validEl = card.querySelector('#out-valid-hve1-{idx}');
        var plotEl = card.querySelector('#plot-hve1-{idx}');
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
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          idx = {idx};
          var res = calculate(a, b);
          if (res) {{
            if (metricEl) metricEl.textContent = res.headline;
            if (validEl) validEl.textContent = 'Assumptions: ' + res.valid;
            if (plotEl) renderHVE1Plot(plotEl, res);
          }}
        }}
        update();
      }} catch (err) {{
        console.warn('HVE1 init error:', err);
      }}
    }}
  }});
"""

hve1_js += ENGINE_FOOTER

hve1_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'high-voltage-engineering-i', 'high-voltage-engineering-i-sims.js')
with open(hve1_out, 'w', encoding='utf-8') as f:
    f.write(hve1_js)
print(f"Saved {hve1_out} ({len(hve1_js)} bytes)")

# ==============================================================================
# 6. HIGH VOLTAGE ENGINEERING II
# ==============================================================================
print("Generating high-voltage-engineering-ii-sims.js...")

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    hve2_raw = z.read("OpenSTEM-Electrical-and-Electronics-Engineering/books/high-voltage-engineering-ii/simulations/models.js").decode("utf-8")

calc2_start = hve2_raw.find("function calc(a,b){")
calc2_end = hve2_raw.find("\nfunction draw()", calc2_start)
hve2_calc_js = hve2_raw[calc2_start:calc2_end]

hve2_configs = [
  {"title": "Traveling wave reflection at line junction", "desc": "Bewley lattice reflection Γ = (Z2 - Z1)/(Z2 + Z1) and refraction at line-cable boundary.", "controls": [["Incoming line Z1 (Ω)", 100, 600, 350, 10], ["Outgoing line Z2 (Ω)", 20, 600, 50, 5]]},
  {"title": "Lightning stroke tower top potential rise", "desc": "Direct stroke lightning surge current into tower surge impedance and footing resistance.", "controls": [["Stroke current I (kA)", 10, 200, 60, 5], ["Footing resistance R (Ω)", 5, 50, 15, 1]]},
  {"title": "Transient recovery voltage (TRV) across breaker", "desc": "LC oscillation recovery voltage v(t) = V0·(1 - e^(-t/τ)·cos(ω_0 t)) following fault clearing.", "controls": [["Natural frequency (kHz)", 1, 50, 15, 1], ["Damping time const (ms)", 0.05, 1.0, 0.2, 0.05]]},
  {"title": "Metal-oxide surge arrester non-linear V-I curve", "desc": "Zinc-oxide (ZnO) varistor non-linear characteristic I = k·V^α clamping overvoltages.", "controls": [["Exponent alpha α", 20, 50, 35, 1], ["Reference voltage (kV)", 50, 300, 120, 5]]},
  {"title": "Statistical insulation coordination and BIL margins", "desc": "Overvoltage probability density vs insulation breakdown cumulative Weibull distribution.", "controls": [["Surge standard dev (kV)", 10, 100, 40, 5], ["Withstand BIL (kV)", 400, 1200, 750, 25]]},
  {"title": "High-voltage divider frequency response", "desc": "Mixed resistive-capacitive high-voltage divider compensation and step-response rise time.", "controls": [["Divider ratio factor", 100, 5000, 1000, 50], ["Stray capacitance (pF)", 5, 100, 25, 2]]},
  {"title": "Corona inception electric field gradient", "desc": "Peek empirical law for visual and disruptive corona inception gradient on stranded conductors.", "controls": [["Conductor radius r (cm)", 0.5, 4.0, 1.5, 0.1], ["Air density factor δ", 0.8, 1.1, 1.0, 0.02]]},
  {"title": "Partial discharge apparent charge pulse", "desc": "Internal cavity partial discharge breakdown and void capacitive charge transfer Δq.", "controls": [["Cavity diameter (mm)", 0.1, 3.0, 0.8, 0.1], ["Applied electric stress (kV/mm)", 1, 15, 5, 0.5]]}
]

hve2_js = f"""/* High Voltage Engineering II Interactive Simulation Suite */
(function(window) {{
  'use strict';

  var lin = function(a, b, n) {{
    if (n === undefined) n = 160;
    return Array.from({{length: n}}, function(_, i) {{ return a + (b - a) * i / (n - 1); }});
  }};

  var unit = 1;

  {hve2_calc_js}

  function makeSvgEl(tag, attrs) {{
    var el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) {{
      if (Object.prototype.hasOwnProperty.call(attrs, k)) {{
        el.setAttribute(k, String(attrs[k]));
      }}
    }}
    return el;
  }}

  function renderHVE2Plot(plot, res) {{
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 320, L = 72, R = 20, T = 20, B = 48;
    var xs = res.xs, ys = res.ys;
    var validPts = [];
    for (var k = 0; k < xs.length; k++) {{
      if (Number.isFinite(xs[k]) && Number.isFinite(ys[k])) validPts.push([xs[k], ys[k]]);
    }}
    if (validPts.length === 0) return;
    var pXs = validPts.map(function(p) {{ return p[0]; }}), pYs = validPts.map(function(p) {{ return p[1]; }});
    var xmin = Math.min.apply(null, pXs), xmax = Math.max.apply(null, pXs);
    var ymin = Math.min.apply(null, pYs), ymax = Math.max.apply(null, pYs);
    if (ymax === ymin) {{ ymax += 1; ymin -= 1; }}
    else {{ var pad = (ymax - ymin) * 0.1; ymin -= pad; ymax += pad; }}
    if (xmax === xmin) xmax = xmin + 1;

    var px = function(x) {{ return L + (W - L - R) * (x - xmin) / (xmax - xmin); }};
    var py = function(y) {{ return T + (H - T - B) * (ymax - y) / (ymax - ymin); }};

    for (var i = 0; i <= 4; i++) {{
      var gy = T + i * (H - T - B) / 4;
      var yv = ymax - i * (ymax - ymin) / 4;
      plot.appendChild(makeSvgEl('line', {{x1: L, y1: gy, x2: W - R, y2: gy, stroke: '#e2e8f0'}}));
      var yt = makeSvgEl('text', {{x: L - 8, y: gy + 4, fill: '#64748b', 'text-anchor': 'end', 'font-size': 11}});
      yt.textContent = yv.toPrecision(3);
      plot.appendChild(yt);
    }}
    for (var j = 0; j <= 5; j++) {{
      var gx = L + j * (W - L - R) / 5;
      var xv = xmin + j * (xmax - xmin) / 5;
      plot.appendChild(makeSvgEl('line', {{x1: gx, y1: T, x2: gx, y2: H - B, stroke: '#f1f5f9'}}));
      var xt = makeSvgEl('text', {{x: gx, y: H - B + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11}});
      xt.textContent = xv.toPrecision(3);
      plot.appendChild(xt);
    }}

    var ptsStr = validPts.map(function(p) {{ return px(p[0]).toFixed(1) + ',' + py(p[1]).toFixed(1); }}).join(' ');
    plot.appendChild(makeSvgEl('polyline', {{
      points: ptsStr,
      fill: 'none',
      stroke: '#087a9b',
      'stroke-width': 2.5,
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round'
    }}));

    var xl = makeSvgEl('text', {{x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12}});
    xl.textContent = res.xl || 'Parameter';
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {{x: 16, y: (H - B + T) / 2, transform: 'rotate(-90 16 ' + ((H - B + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12}});
    yl.textContent = res.yl || 'Response';
    plot.appendChild(yl);
  }}

  var MODELS = [];
"""

for idx, item in enumerate(hve2_configs, 1):
    u = idx
    ctrls_json = json.dumps(item["controls"])
    title_esc = json.dumps(item["title"])
    desc_esc = json.dumps(item["desc"])
    hve2_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {u},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>' + {title_esc} + '</h3><p>' + {desc_esc} + '</p></div>' +
          '<div class="sim-controls" id="controls-hve2-{idx}"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Performance</small><output id="out-metric-hve2-{idx}">-</output></div>' +
          '<p class="note" id="out-detail-hve2-{idx}">-</p></div>' +
          '<svg id="plot-hve2-{idx}" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {{
      try {{
        var ctrlsDiv = card.querySelector('#controls-hve2-{idx}');
        var metricEl = card.querySelector('#out-metric-hve2-{idx}');
        var detailEl = card.querySelector('#out-detail-hve2-{idx}');
        var plotEl = card.querySelector('#plot-hve2-{idx}');
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
          var a = Number(inputs[0].value);
          var b = inputs.length > 1 ? Number(inputs[1].value) : 0;
          unit = {idx};
          var res = calc(a, b);
          if (res) {{
            if (metricEl) metricEl.textContent = res.headline;
            if (detailEl) detailEl.textContent = 'Detail: ' + res.detail;
            if (plotEl) renderHVE2Plot(plotEl, res);
          }}
        }}
        update();
      }} catch (err) {{
        console.warn('HVE2 init error:', err);
      }}
    }}
  }});
"""

hve2_js += ENGINE_FOOTER

hve2_out = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'high-voltage-engineering-ii', 'high-voltage-engineering-ii-sims.js')
with open(hve2_out, 'w', encoding='utf-8') as f:
    f.write(hve2_js)
print(f"Saved {hve2_out} ({len(hve2_js)} bytes)")

print("\nBatch 4 simulation suites generated successfully!")
