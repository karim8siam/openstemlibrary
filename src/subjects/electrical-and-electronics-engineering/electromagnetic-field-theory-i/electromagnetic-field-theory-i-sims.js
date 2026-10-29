/* Electromagnetic Field Theory I Interactive Simulation Suite */
(function(window) {
  'use strict';
  const eps0 = 8.8541878128e-12, mu0 = 4 * Math.PI * 1e-7, k = 1 / (4 * Math.PI * eps0), eta = Math.sqrt(mu0 / eps0);
  const fmt = x => Number(x).toExponential(4);

  function computeModel(mode, a, b) {
    let rows = [], summary = '', curveLabel = '';
    if (mode === 1) {
      const q = a * 1e-9, d = b * 0.01, y = 0.05;
      for (let i = 0; i <= 200; i++) {
        const x = -0.3 + 0.6 * i / 200;
        const r1 = Math.hypot(x + d / 2, y), r2 = Math.hypot(x - d / 2, y);
        const Ex = k * q * ((x + d / 2) / (r1 ** 3) + (x - d / 2) / (r2 ** 3));
        rows.push({x, y: Ex});
      }
      curveLabel = 'Ex along line y=0.05m (V/m)';
      summary = `Peak Ex: ${fmt(Math.max(...rows.map(r => Math.abs(r.y))))} V/m | Charges at ±${(d * 50).toFixed(1)} cm`;
    } else if (mode === 2) {
      const q = a * 1e-9, R = b * 0.01;
      for (let i = 1; i <= 200; i++) {
        const r = 0.3 * i / 200;
        const Dr = r < R ? (q / (4 * Math.PI * R ** 3)) * r : q / (4 * Math.PI * r ** 2);
        rows.push({x: r, y: Dr});
      }
      curveLabel = 'Radial displacement Dr (C/m²)';
      summary = `Peak surface Dr: ${fmt(q / (4 * Math.PI * R ** 2))} C/m² at R=${(R * 100).toFixed(1)} cm`;
    } else if (mode === 3) {
      const V0 = a, d = b * 0.001;
      for (let i = 0; i <= 200; i++) {
        const x = d * i / 200;
        const V = V0 * (1 - x / d);
        rows.push({x, y: V});
      }
      curveLabel = 'Potential V(x) across gap (V)';
      summary = `Uniform Electric Field: ${fmt(V0 / d)} V/m across ${d * 1000} mm gap`;
    } else if (mode === 4) {
      const V0 = a, er = b, a_rad = 0.005, b_rad = 0.025;
      for (let i = 0; i <= 200; i++) {
        const r = a_rad + (b_rad - a_rad) * i / 200;
        const V = V0 * Math.log(b_rad / r) / Math.log(b_rad / a_rad);
        rows.push({x: r, y: V});
      }
      curveLabel = 'Coaxial potential profile V(r) (V)';
      summary = `Capacitance per meter: ${fmt(2 * Math.PI * eps0 * er / Math.log(b_rad / a_rad))} F/m`;
    } else if (mode === 5) {
      const V = a, sigma = b * 1e6, L = 1.0;
      for (let i = 0; i <= 200; i++) {
        const z = L * i / 200;
        const J = sigma * (V / L);
        rows.push({x: z, y: J});
      }
      curveLabel = 'Current density J (A/m²)';
      summary = `Current density: ${fmt(sigma * V / L)} A/m² | Electric Field: ${(V / L).toFixed(2)} V/m`;
    } else if (mode === 6) {
      const I = a, rmax = b * 0.01;
      for (let i = 1; i <= 200; i++) {
        const r = 0.002 + (rmax - 0.002) * i / 200;
        const B = (mu0 * I) / (2 * Math.PI * r);
        rows.push({x: r, y: B});
      }
      curveLabel = 'Magnetic flux density B(r) (Tesla)';
      summary = `B at closest r: ${fmt(rows[0].y)} T | Decay at outer edge: ${fmt(rows[rows.length - 1].y)} T`;
    } else if (mode === 7) {
      const N = a, mur = b, L = 0.2;
      for (let i = 0; i <= 200; i++) {
        const I = 0.05 * i / 200;
        const B = (mu0 * mur * N * I) / L;
        rows.push({x: I, y: B});
      }
      curveLabel = 'Core flux density B vs Current (T)';
      summary = `Permeability multiplier: ${mur}x | Core B at 0.05A: ${fmt(rows[rows.length - 1].y)} T`;
    } else if (mode === 8) {
      const theta1 = a * Math.PI / 180, mur2 = b;
      for (let i = 1; i <= 180; i++) {
        const th1 = i * 0.5 * Math.PI / 180;
        const tanTh2 = mur2 * Math.tan(th1);
        const th2 = Math.atan(tanTh2) * 180 / Math.PI;
        rows.push({x: i * 0.5, y: th2});
      }
      const activeTh2 = Math.atan(mur2 * Math.tan(theta1)) * 180 / Math.PI;
      curveLabel = 'Refracted angle θ2 vs Incident θ1 (degrees)';
      summary = `Incident θ1: ${a}° → Refracted θ2 in iron: ${activeTh2.toFixed(2)}° (normal alignment)`;
    }
    return {rows, summary, curveLabel};
  }

  function drawCanvas(canvas, rows, curveLabel) {
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
    ctx.font = '12px sans-serif';
    ctx.fillText(curveLabel, pad, 25);
    ctx.fillText(minX.toPrecision(3), pad, H - 20);
    ctx.fillText(maxX.toPrecision(3), W - pad - 30, H - 20);
    ctx.fillText(fmt(maxY), 8, pad + 10);
    ctx.fillText(fmt(minY), 8, H - pad);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>Two-Charge Electric Field Sampler</h3><p>Charge superposition in air: two equal positive charges at x=±d/2.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-1">Charge (nC): <output id="v1-1"></output>' +
              '<input id="p1-1" type="range" min="1" max="10" step="1" value="2"/>' +
            '</label>' +
            '<label for="p2-1">Separation (cm): <output id="v2-1"></output>' +
              '<input id="p2-1" type="range" min="5" max="30" step="1" value="20"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-1" width="680" height="260" role="img" aria-label="Electromagnetic field curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="summary-1">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-1');
        var p2 = card.querySelector('#p2-1');
        var v1 = card.querySelector('#v1-1');
        var v2 = card.querySelector('#v2-1');
        var canvas = card.querySelector('#canvas-1');
        var summary = card.querySelector('#summary-1');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a);
          if (v2) v2.textContent = String(b);
          var res = computeModel(1, a, b);
          if (summary) summary.textContent = res.summary;
          if (canvas) drawCanvas(canvas, res.rows, res.curveLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory I sim error in model 1:', err);
      }
    }
  });
  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>Spherical Gaussian Flux Profiler</h3><p>Flux density D and total enclosed charge across radial shells.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-2">Enclosed Q (nC): <output id="v1-2"></output>' +
              '<input id="p1-2" type="range" min="1" max="20" step="1" value="5"/>' +
            '</label>' +
            '<label for="p2-2">Outer radius R (cm): <output id="v2-2"></output>' +
              '<input id="p2-2" type="range" min="5" max="25" step="1" value="10"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-2" width="680" height="260" role="img" aria-label="Electromagnetic field curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="summary-2">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-2');
        var p2 = card.querySelector('#p2-2');
        var v1 = card.querySelector('#v1-2');
        var v2 = card.querySelector('#v2-2');
        var canvas = card.querySelector('#canvas-2');
        var summary = card.querySelector('#summary-2');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a);
          if (v2) v2.textContent = String(b);
          var res = computeModel(2, a, b);
          if (summary) summary.textContent = res.summary;
          if (canvas) drawCanvas(canvas, res.rows, res.curveLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory I sim error in model 2:', err);
      }
    }
  });
  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>1D Parallel Plate Potential Solver</h3><p>Linear potential fall and constant electric field between conducting plates.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-3">Plate voltage V0 (V): <output id="v1-3"></output>' +
              '<input id="p1-3" type="range" min="10" max="200" step="5" value="50"/>' +
            '</label>' +
            '<label for="p2-3">Gap distance d (mm): <output id="v2-3"></output>' +
              '<input id="p2-3" type="range" min="1" max="10" step="1" value="4"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-3" width="680" height="260" role="img" aria-label="Electromagnetic field curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="summary-3">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-3');
        var p2 = card.querySelector('#p2-3');
        var v1 = card.querySelector('#v1-3');
        var v2 = card.querySelector('#v2-3');
        var canvas = card.querySelector('#canvas-3');
        var summary = card.querySelector('#summary-3');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a);
          if (v2) v2.textContent = String(b);
          var res = computeModel(3, a, b);
          if (summary) summary.textContent = res.summary;
          if (canvas) drawCanvas(canvas, res.rows, res.curveLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory I sim error in model 3:', err);
      }
    }
  });
  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>Coaxial Dielectric Displacement</h3><p>Radial displacement field and potential gradient with relative permittivity.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-4">Inner core potential (V): <output id="v1-4"></output>' +
              '<input id="p1-4" type="range" min="10" max="100" step="5" value="50"/>' +
            '</label>' +
            '<label for="p2-4">Relative permittivity εr: <output id="v2-4"></output>' +
              '<input id="p2-4" type="range" min="1" max="10" step="0.5" value="3"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-4" width="680" height="260" role="img" aria-label="Electromagnetic field curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="summary-4">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-4');
        var p2 = card.querySelector('#p2-4');
        var v1 = card.querySelector('#v1-4');
        var v2 = card.querySelector('#v2-4');
        var canvas = card.querySelector('#canvas-4');
        var summary = card.querySelector('#summary-4');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a);
          if (v2) v2.textContent = String(b);
          var res = computeModel(4, a, b);
          if (summary) summary.textContent = res.summary;
          if (canvas) drawCanvas(canvas, res.rows, res.curveLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory I sim error in model 4:', err);
      }
    }
  });
  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>Steady Wire Current Density & Resistance</h3><p>Ohmic voltage gradient, current density J, and conductor heating.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-5">Applied Voltage (V): <output id="v1-5"></output>' +
              '<input id="p1-5" type="range" min="1" max="50" step="1" value="12"/>' +
            '</label>' +
            '<label for="p2-5">Conductivity σ (MS/m): <output id="v2-5"></output>' +
              '<input id="p2-5" type="range" min="10" max="60" step="5" value="35"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-5" width="680" height="260" role="img" aria-label="Electromagnetic field curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="summary-5">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-5');
        var p2 = card.querySelector('#p2-5');
        var v1 = card.querySelector('#v1-5');
        var v2 = card.querySelector('#v2-5');
        var canvas = card.querySelector('#canvas-5');
        var summary = card.querySelector('#summary-5');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a);
          if (v2) v2.textContent = String(b);
          var res = computeModel(5, a, b);
          if (summary) summary.textContent = res.summary;
          if (canvas) drawCanvas(canvas, res.rows, res.curveLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory I sim error in model 5:', err);
      }
    }
  });
  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>Biot-Savart Filamentary Magnetic Field</h3><p>Radial decay of magnetic flux density B around a straight wire.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-6">Current I (A): <output id="v1-6"></output>' +
              '<input id="p1-6" type="range" min="1" max="50" step="1" value="10"/>' +
            '</label>' +
            '<label for="p2-6">Radial distance max (cm): <output id="v2-6"></output>' +
              '<input id="p2-6" type="range" min="5" max="30" step="1" value="15"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-6" width="680" height="260" role="img" aria-label="Electromagnetic field curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="summary-6">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-6');
        var p2 = card.querySelector('#p2-6');
        var v1 = card.querySelector('#v1-6');
        var v2 = card.querySelector('#v2-6');
        var canvas = card.querySelector('#canvas-6');
        var summary = card.querySelector('#summary-6');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a);
          if (v2) v2.textContent = String(b);
          var res = computeModel(6, a, b);
          if (summary) summary.textContent = res.summary;
          if (canvas) drawCanvas(canvas, res.rows, res.curveLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory I sim error in model 6:', err);
      }
    }
  });
  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>Solenoid Core Magnetic Flux Density</h3><p>Interior uniform magnetic field and permeability boost from magnetic core.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-7">Turns count N: <output id="v1-7"></output>' +
              '<input id="p1-7" type="range" min="100" max="1000" step="50" value="400"/>' +
            '</label>' +
            '<label for="p2-7">Core relative μr: <output id="v2-7"></output>' +
              '<input id="p2-7" type="range" min="1" max="500" step="10" value="100"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-7" width="680" height="260" role="img" aria-label="Electromagnetic field curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="summary-7">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-7');
        var p2 = card.querySelector('#p2-7');
        var v1 = card.querySelector('#v1-7');
        var v2 = card.querySelector('#v2-7');
        var canvas = card.querySelector('#canvas-7');
        var summary = card.querySelector('#summary-7');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a);
          if (v2) v2.textContent = String(b);
          var res = computeModel(7, a, b);
          if (summary) summary.textContent = res.summary;
          if (canvas) drawCanvas(canvas, res.rows, res.curveLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory I sim error in model 7:', err);
      }
    }
  });
  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>Magnetic Interface Boundary Refraction</h3><p>Tangential H continuity and normal B continuity at iron-air boundary.</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-8">Incident angle θ1 (deg): <output id="v1-8"></output>' +
              '<input id="p1-8" type="range" min="5" max="85" step="5" value="45"/>' +
            '</label>' +
            '<label for="p2-8">Relative μr of core: <output id="v2-8"></output>' +
              '<input id="p2-8" type="range" min="10" max="500" step="10" value="150"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-8" width="680" height="260" role="img" aria-label="Electromagnetic field curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="summary-8">-</output></div></div>',
    init: function(card) {
      try {
        var p1 = card.querySelector('#p1-8');
        var p2 = card.querySelector('#p2-8');
        var v1 = card.querySelector('#v1-8');
        var v2 = card.querySelector('#v2-8');
        var canvas = card.querySelector('#canvas-8');
        var summary = card.querySelector('#summary-8');
        function update() {
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a);
          if (v2) v2.textContent = String(b);
          var res = computeModel(8, a, b);
          if (summary) summary.textContent = res.summary;
          if (canvas) drawCanvas(canvas, res.rows, res.curveLabel);
        }
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Electromagnetic Field Theory I sim error in model 8:', err);
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
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);
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
