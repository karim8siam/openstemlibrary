/* Electromagnetic Field Theory II Interactive Simulation Suite */
(function(window) {
  'use strict';
  const c = 299792458, eta0 = 376.7303135;
  const f = n => Number.isFinite(n) ? Number(n).toPrecision(4) : 'not defined';

  function calcModel(mode, a, b) {
    let rows = [], message = '', xLabel = '', yLabel = '';
    if (mode === 1) {
      const C = a * 1e-12, fr = b * 1e6, peak = C * 2 * Math.PI * fr * 5 * 1e3;
      for (let i = 0; i <= 200; i++) {
        const t = i / (200 * fr);
        rows.push({x: t * 1e9, y: peak * Math.cos(2 * Math.PI * fr * t)});
      }
      xLabel = 'Time (ns)'; yLabel = 'Current (mA)';
      message = 'Peak displacement current: ' + f(peak) + ' mA. Ideal capacitor, no dielectric conduction.';
    } else if (mode === 2) {
      const v = c / Math.sqrt(b), wl = v / (a * 1e6), e = 5;
      for (let i = 0; i <= 200; i++) {
        let x = (i / 200) * 3 * wl;
        rows.push({x: x, y: e * Math.cos(2 * Math.PI * x / wl)});
      }
      xLabel = 'Distance (m)'; yLabel = 'E field (V/m)';
      message = 'Wave velocity: ' + f(v) + ' m/s, Wavelength: ' + f(wl) + ' m, Intrinsic impedance: ' + f(eta0 / Math.sqrt(b)) + ' Ω.';
    } else if (mode === 3) {
      for (let i = 0; i <= 200; i++) {
        let eps2 = 1 + i * 15 / 200, z1 = eta0 / Math.sqrt(a), z2 = eta0 / Math.sqrt(eps2), g = (z2 - z1) / (z2 + z1);
        rows.push({x: eps2, y: g * g});
      }
      let z1 = eta0 / Math.sqrt(a), z2 = eta0 / Math.sqrt(b), g = (z2 - z1) / (z2 + z1);
      xLabel = 'Transmitted εr2'; yLabel = 'Power Reflection R';
      message = 'At εr2=' + b + ': Reflection Γ=' + f(g) + ', Power R=' + f(g * g) + ', Transmission T=' + f(1 - g * g) + '.';
    } else if (mode === 4) {
      const g = (a - 50) / (a + 50), wl = c / (b * 1e6), beta = 2 * Math.PI / wl;
      for (let i = 0; i <= 200; i++) {
        const z = (i / 200) * 2 * wl;
        rows.push({x: z, y: Math.sqrt(1 + g * g + 2 * g * Math.cos(2 * beta * z))});
      }
      const vswr = (1 + Math.abs(g)) / (1 - Math.abs(g) || 1e-6);
      xLabel = 'Distance from load (m)'; yLabel = '|V| / |V+|';
      message = 'VSWR: ' + f(vswr) + ', Reflection coefficient: ' + f(g) + ' on 50 Ω reference line.';
    } else if (mode === 5) {
      const fc = (c / (2 * a * 1e-3)) * 1e-9;
      for (let i = 0; i <= 200; i++) {
        const freq = 1 + (25 * i / 200);
        const ratio = freq > fc ? Math.sqrt(1 - (fc / freq) ** 2) : 0;
        rows.push({x: freq, y: ratio});
      }
      const activeRatio = b > fc ? Math.sqrt(1 - (fc / b) ** 2) : 0;
      xLabel = 'Frequency (GHz)'; yLabel = 'β / k (propagation)';
      message = 'Cutoff fc=' + f(fc) + ' GHz. At f=' + b + ' GHz: ' + (b > fc ? 'Propagating mode (β/k=' + f(activeRatio) + ')' : 'Evanescent mode (cutoff)');
    } else if (mode === 6) {
      for (let i = 0; i <= 180; i++) {
        const theta = i * Math.PI / 180;
        rows.push({x: i, y: (Math.sin(theta) ** 2) * b});
      }
      xLabel = 'Polar angle θ (degrees)'; yLabel = 'Gain (linear)';
      message = 'Hertzian dipole sin²(θ) donut pattern. Peak broadside gain at θ=90°: ' + f(1.5 * b) + ' (dBi: ' + f(10 * Math.log10(1.5 * b)) + ').';
    } else if (mode === 7) {
      for (let i = 0; i <= 200; i++) {
        const thick = 0.1 + 6 * i / 200;
        const seAbs = 8.686 * thick;
        const total = Math.min(seAbs + b, 120);
        rows.push({x: thick, y: total});
      }
      xLabel = 'Thickness (skin depths)'; yLabel = 'Shielding SE (dB)';
      message = 'Total SE: ' + f(Math.min(8.686 * a + b, 120)) + ' dB. Absorption: ' + f(8.686 * a) + ' dB, Seam floor limit: ' + b + ' dB.';
    } else if (mode === 8) {
      for (let i = 5; i <= 40; i++) {
        const num = (2 / a) * Math.asin(a * Math.sin(Math.PI / i));
        rows.push({x: i, y: num / (2 * Math.PI / i)});
      }
      xLabel = 'Points per wavelength'; yLabel = 'Phase velocity ratio';
      message = 'Courant number S=' + a + (a > 1 ? ' (UNSTABLE: CFL violated!)' : ' (STABLE).') + ' Numerical dispersion decreases with finer grid sampling.';
    }
    return {rows, message, xLabel, yLabel};
  }

  function drawPlot(canvas, rows, xLabel, yLabel) {
    const ctx = canvas.getContext('2d');
    const W = canvas.width, H = canvas.height;
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, W, H);
    if (!rows || rows.length < 2) return;
    const xs = rows.map(r => r.x), ys = rows.map(r => r.y);
    const minX = Math.min(...xs), maxX = Math.max(...xs);
    let minY = Math.min(...ys), maxY = Math.max(...ys);
    if (minY === maxY) { minY -= 1; maxY += 1; }
    const pad = 50;
    const sx = x => pad + ((x - minX) / (maxX - minX || 1)) * (W - 2 * pad);
    const sy = y => H - pad - ((y - minY) / (maxY - minY || 1)) * (H - 2 * pad);
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(pad, pad); ctx.lineTo(pad, H - pad); ctx.lineTo(W - pad, H - pad);
    ctx.stroke();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    rows.forEach((r, i) => {
      const x = sx(r.x), y = sy(r.y);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    });
    ctx.stroke();
    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText(xLabel, W / 2 - 40, H - 15);
    ctx.fillText(yLabel, pad, 25);
    ctx.fillText(f(minX), pad, H - 25);
    ctx.fillText(f(maxX), W - pad - 25, H - 25);
    ctx.fillText(f(maxY), 8, pad + 10);
    ctx.fillText(f(minY), 8, H - pad);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>Displacement current in a capacitor</h3><p>Ideal sinusoidal excitation V(t)=5 sin(2πft) V.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-1">Capacitance (pF): <output id="v1-1"></output>' +
              '<input id="p1-1" type="range" min="20" max="500" step="5" value="100"/>' +
            '</label>' +
            '<label for="p2-1">Frequency (MHz): <output id="v2-1"></output>' +
              '<input id="p2-1" type="range" min="1" max="50" step="1" value="5"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-1" width="680" height="260" role="img" aria-label="EM wave response curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="msg-1">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-1');
        var p2 = card.querySelector('#p2-1');
        var v1 = card.querySelector('#v1-1');
        var v2 = card.querySelector('#v2-1');
        var canvas = card.querySelector('#canvas-1');
        var msg = card.querySelector('#msg-1');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a) + ' pF';
          if (v2) v2.textContent = String(b) + ' MHz';
          var res = calcModel(1, a, b);
          if (msg) msg.textContent = res.message;
          if (canvas) drawPlot(canvas, res.rows, res.xLabel, res.yLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory II sim error in model 1:', err);
      }
    }
  });
  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>Lossless plane-wave propagation</h3><p>Lossless wave velocity, wavelength, and intrinsic impedance.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-2">Frequency (MHz): <output id="v1-2"></output>' +
              '<input id="p1-2" type="range" min="20" max="1000" step="10" value="200"/>' +
            '</label>' +
            '<label for="p2-2">Relative permittivity (): <output id="v2-2"></output>' +
              '<input id="p2-2" type="range" min="1" max="10" step="0.1" value="4"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-2" width="680" height="260" role="img" aria-label="EM wave response curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="msg-2">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-2');
        var p2 = card.querySelector('#p2-2');
        var v1 = card.querySelector('#v1-2');
        var v2 = card.querySelector('#v2-2');
        var canvas = card.querySelector('#canvas-2');
        var msg = card.querySelector('#msg-2');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a) + ' MHz';
          if (v2) v2.textContent = String(b) + ' ';
          var res = calcModel(2, a, b);
          if (msg) msg.textContent = res.message;
          if (canvas) drawPlot(canvas, res.rows, res.xLabel, res.yLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory II sim error in model 2:', err);
      }
    }
  });
  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>Normal-incidence Fresnel power reflection</h3><p>Reflection and transmission coefficients at planar dielectric boundary.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-3">Incident εr (): <output id="v1-3"></output>' +
              '<input id="p1-3" type="range" min="1" max="5" step="0.1" value="1"/>' +
            '</label>' +
            '<label for="p2-3">Transmitted εr (): <output id="v2-3"></output>' +
              '<input id="p2-3" type="range" min="1" max="16" step="0.2" value="4"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-3" width="680" height="260" role="img" aria-label="EM wave response curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="msg-3">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-3');
        var p2 = card.querySelector('#p2-3');
        var v1 = card.querySelector('#v1-3');
        var v2 = card.querySelector('#v2-3');
        var canvas = card.querySelector('#canvas-3');
        var msg = card.querySelector('#msg-3');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a) + ' ';
          if (v2) v2.textContent = String(b) + ' ';
          var res = calcModel(3, a, b);
          if (msg) msg.textContent = res.message;
          if (canvas) drawPlot(canvas, res.rows, res.xLabel, res.yLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory II sim error in model 3:', err);
      }
    }
  });
  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>Lossless line standing-wave profile</h3><p>Voltage standing wave ratio (VSWR) and voltage envelope.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-4">Load resistance (Ω): <output id="v1-4"></output>' +
              '<input id="p1-4" type="range" min="5" max="200" step="1" value="100"/>' +
            '</label>' +
            '<label for="p2-4">Frequency (MHz): <output id="v2-4"></output>' +
              '<input id="p2-4" type="range" min="50" max="1000" step="10" value="200"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-4" width="680" height="260" role="img" aria-label="EM wave response curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="msg-4">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-4');
        var p2 = card.querySelector('#p2-4');
        var v1 = card.querySelector('#v1-4');
        var v2 = card.querySelector('#v2-4');
        var canvas = card.querySelector('#canvas-4');
        var msg = card.querySelector('#msg-4');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a) + ' Ω';
          if (v2) v2.textContent = String(b) + ' MHz';
          var res = calcModel(4, a, b);
          if (msg) msg.textContent = res.message;
          if (canvas) drawPlot(canvas, res.rows, res.xLabel, res.yLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory II sim error in model 4:', err);
      }
    }
  });
  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>Rectangular TE10 guide cutoff</h3><p>Dispersion relation, cutoff frequency, and phase velocity in metallic guide.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-5">Broad wall a (mm): <output id="v1-5"></output>' +
              '<input id="p1-5" type="range" min="10" max="40" step="0.5" value="22.86"/>' +
            '</label>' +
            '<label for="p2-5">Operating frequency (GHz): <output id="v2-5"></output>' +
              '<input id="p2-5" type="range" min="3" max="20" step="0.2" value="10"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-5" width="680" height="260" role="img" aria-label="EM wave response curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="msg-5">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-5');
        var p2 = card.querySelector('#p2-5');
        var v1 = card.querySelector('#v1-5');
        var v2 = card.querySelector('#v2-5');
        var canvas = card.querySelector('#canvas-5');
        var msg = card.querySelector('#msg-5');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a) + ' mm';
          if (v2) v2.textContent = String(b) + ' GHz';
          var res = calcModel(5, a, b);
          if (msg) msg.textContent = res.message;
          if (canvas) drawPlot(canvas, res.rows, res.xLabel, res.yLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory II sim error in model 5:', err);
      }
    }
  });
  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>Hertzian element radiation pattern</h3><p>Far-field radiation pattern and directivity of electrically short dipole.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-6">Length / wavelength (): <output id="v1-6"></output>' +
              '<input id="p1-6" type="range" min="0.01" max="0.1" step="0.005" value="0.05"/>' +
            '</label>' +
            '<label for="p2-6">Radiation efficiency (): <output id="v2-6"></output>' +
              '<input id="p2-6" type="range" min="0.1" max="1" step="0.05" value="0.8"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-6" width="680" height="260" role="img" aria-label="EM wave response curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="msg-6">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-6');
        var p2 = card.querySelector('#p2-6');
        var v1 = card.querySelector('#v1-6');
        var v2 = card.querySelector('#v2-6');
        var canvas = card.querySelector('#canvas-6');
        var msg = card.querySelector('#msg-6');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a) + ' ';
          if (v2) v2.textContent = String(b) + ' ';
          var res = calcModel(6, a, b);
          if (msg) msg.textContent = res.message;
          if (canvas) drawPlot(canvas, res.rows, res.xLabel, res.yLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory II sim error in model 6:', err);
      }
    }
  });
  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>Enclosure absorption and seam leakage</h3><p>Shielding effectiveness against conducted and radiated interference.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-7">Thickness / skin depth (): <output id="v1-7"></output>' +
              '<input id="p1-7" type="range" min="0.2" max="6" step="0.1" value="3"/>' +
            '</label>' +
            '<label for="p2-7">Seam SE floor (dB): <output id="v2-7"></output>' +
              '<input id="p2-7" type="range" min="5" max="60" step="1" value="30"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-7" width="680" height="260" role="img" aria-label="EM wave response curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="msg-7">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-7');
        var p2 = card.querySelector('#p2-7');
        var v1 = card.querySelector('#v1-7');
        var v2 = card.querySelector('#v2-7');
        var canvas = card.querySelector('#canvas-7');
        var msg = card.querySelector('#msg-7');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a) + ' ';
          if (v2) v2.textContent = String(b) + ' dB';
          var res = calcModel(7, a, b);
          if (msg) msg.textContent = res.message;
          if (canvas) drawPlot(canvas, res.rows, res.xLabel, res.yLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory II sim error in model 7:', err);
      }
    }
  });
  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>FDTD discrete phase and CFL check</h3><p>Numerical phase velocity error and Courant-Friedrichs-Lewy stability condition.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-8">Courant factor (): <output id="v1-8"></output>' +
              '<input id="p1-8" type="range" min="0.5" max="1.3" step="0.01" value="0.9"/>' +
            '</label>' +
            '<label for="p2-8">Points / wavelength (): <output id="v2-8"></output>' +
              '<input id="p2-8" type="range" min="5" max="40" step="1" value="15"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-8" width="680" height="260" role="img" aria-label="EM wave response curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="msg-8">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-8');
        var p2 = card.querySelector('#p2-8');
        var v1 = card.querySelector('#v1-8');
        var v2 = card.querySelector('#v2-8');
        var canvas = card.querySelector('#canvas-8');
        var msg = card.querySelector('#msg-8');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a) + ' ';
          if (v2) v2.textContent = String(b) + ' ';
          var res = calcModel(8, a, b);
          if (msg) msg.textContent = res.message;
          if (canvas) drawPlot(canvas, res.rows, res.xLabel, res.yLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory II sim error in model 8:', err);
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
