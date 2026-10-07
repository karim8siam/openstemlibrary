/**
 * OpenSTEM Academic Library: Ordinary Differential Equations II (MTH 3104)
 * High-Performance 60 FPS Interactive Numerical Simulations Suite
 *
 * Simulations:
 * 1. ode2-phase-portrait-sim    - 2D Autonomous Linear Phase Plane (Trace-Determinant & Orbits)
 * 2. ode2-eigen-decomp-sim      - Generalized Eigenvectors & Defective Jordan Chain Visualizer
 * 3. ode2-matrix-exp-sim        - Matrix Exponential Flow e^(At) & Flow Map Operator
 * 4. ode2-legendre-series-sim   - Legendre Polynomials P_n(x), Orthogonality & Roots
 * 5. ode2-frobenius-sim         - Frobenius Singular Solutions & Logarithmic Branch Divergence
 * 6. ode2-bessel-harmonics-sim  - Bessel Functions J_n, Y_n & Vibrating Circular Membrane
 * 7. ode2-sturm-liouville-sim   - Sturm-Liouville Eigenvalue Shooting & Oscillation Theorem
 * 8. ode2-greens-function-sim   - Green's Function Kernel G(x, xi) & Inhomogeneous Response
 */

(function() {
  'use strict';

  window.SimulationEngine = window.SimulationEngine || {
    registry: {},
    activeInstances: {},

    register: function(type, initFn) {
      this.registry[type] = initFn;
    },

    initSimulation: function(containerId, type) {
      if (this.activeInstances[containerId]) {
        try { this.activeInstances[containerId].destroy(); } catch (e) {}
        delete this.activeInstances[containerId];
      }
      var container = document.getElementById(containerId);
      if (!container) return;
      if (this.registry[type]) {
        var instance = this.registry[type](container);
        if (instance) this.activeInstances[containerId] = instance;
      } else {
        container.innerHTML = '<div style="padding:1.5rem;color:#f87171;text-align:center;">Simulation ' + type + ' registered soon.</div>';
      }
    }
  };

  // Helper: Create Canvas with High-DPI support
  function setupCanvas(container, heightPx) {
    container.innerHTML = '';
    var wrapper = document.createElement('div');
    wrapper.style.position = 'relative';
    wrapper.style.width = '100%';
    wrapper.style.background = '#090d16';
    wrapper.style.borderRadius = '12px';
    wrapper.style.overflow = 'hidden';
    wrapper.style.border = '1px solid #1e293b';

    var canvas = document.createElement('canvas');
    canvas.style.display = 'block';
    canvas.style.width = '100%';
    canvas.style.height = (heightPx || 340) + 'px';
    wrapper.appendChild(canvas);

    var controls = document.createElement('div');
    controls.style.padding = '10px 14px';
    controls.style.background = '#0d1322';
    controls.style.borderTop = '1px solid #1e293b';
    controls.style.display = 'flex';
    controls.style.flexWrap = 'wrap';
    controls.style.gap = '12px';
    controls.style.alignItems = 'center';
    controls.style.fontSize = '12px';
    controls.style.color = '#cbd5e1';
    wrapper.appendChild(controls);

    container.appendChild(wrapper);

    var dpr = window.devicePixelRatio || 1;
    function resize() {
      var rect = canvas.getBoundingClientRect();
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
    }
    resize();
    window.addEventListener('resize', resize);

    return {
      canvas: canvas,
      ctx: canvas.getContext('2d'),
      controls: controls,
      wrapper: wrapper,
      dpr: dpr,
      resize: resize,
      cleanup: function() {
        window.removeEventListener('resize', resize);
      }
    };
  }

  // =========================================================================
  // 1. ode2-phase-portrait-sim: 2D Autonomous Linear Phase Plane
  // =========================================================================
  window.SimulationEngine.register('ode2-phase-portrait-sim', function(container) {
    var kit = setupCanvas(container, 360);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    // Parameters: Matrix A = [[a, b], [c, d]]
    var a = -0.5, b = 2.0, c = -2.0, d = -0.5;
    var running = true;
    var animId = null;
    var particles = [];

    // Controls
    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Preset:</span>
        <select id="ode2-preset" style="background:#1e293b;color:#f8fafc;border:1px solid #334155;border-radius:4px;padding:3px 6px;">
          <option value="stable-focus">Stable Spiral (Focus)</option>
          <option value="center">Neutral Center (Ellipses)</option>
          <option value="saddle">Saddle Point</option>
          <option value="stable-node">Stable Node</option>
          <option value="unstable-spiral">Unstable Spiral</option>
          <option value="degenerate-node">Star / Degenerate Node</option>
        </select>
      </label>
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Speed:</span>
        <input type="range" id="ode2-speed" min="0.2" max="2.5" step="0.1" value="1.0" style="width:70px;">
      </label>
      <button id="ode2-clear" style="background:#3b82f6;color:white;border:none;padding:4px 10px;border-radius:4px;cursor:pointer;">Reset Particles</button>
      <div id="ode2-stats" style="margin-left:auto;font-family:monospace;color:#38bdf8;"></div>
    `;

    var presetSelect = controls.querySelector('#ode2-preset');
    var speedInput = controls.querySelector('#ode2-speed');
    var clearBtn = controls.querySelector('#ode2-clear');
    var statsEl = controls.querySelector('#ode2-stats');

    function applyPreset(p) {
      if (p === 'stable-focus') { a = -0.4; b = 2.0; c = -2.0; d = -0.4; }
      else if (p === 'center') { a = 0.0; b = 2.5; c = -2.5; d = 0.0; }
      else if (p === 'saddle') { a = 1.0; b = 1.5; c = 1.5; d = -1.0; }
      else if (p === 'stable-node') { a = -2.0; b = 0.0; c = 0.0; d = -1.0; }
      else if (p === 'unstable-spiral') { a = 0.3; b = 2.0; c = -2.0; d = 0.3; }
      else if (p === 'degenerate-node') { a = -1.0; b = 1.0; c = 0.0; d = -1.0; }
      resetParticles();
    }

    presetSelect.addEventListener('change', function() { applyPreset(this.value); });
    clearBtn.addEventListener('click', resetParticles);

    // Click canvas to spawn particle
    canvas.addEventListener('click', function(e) {
      var rect = canvas.getBoundingClientRect();
      var x = ((e.clientX - rect.left) / rect.width) * 8 - 4;
      var y = -(((e.clientY - rect.top) / rect.height) * 8 - 4);
      particles.push({ x: x, y: y, path: [{x:x, y:y}], life: 0, color: '#f59e0b' });
    });

    function resetParticles() {
      particles = [];
      for (var i = 0; i < 30; i++) {
        var ang = (i / 30) * Math.PI * 2;
        var r = 1.5 + (i % 3) * 0.9;
        var px = r * Math.cos(ang);
        var py = r * Math.sin(ang);
        particles.push({
          x: px, y: py,
          path: [{x: px, y: py}],
          life: 0,
          color: (i % 2 === 0) ? '#38bdf8' : '#a78bfa'
        });
      }
    }
    resetParticles();

    function render() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      // Coordinate transformation: range [-4, 4] in x and y
      function toScreen(x, y) {
        return {
          sx: ((x + 4) / 8) * w,
          sy: ((4 - y) / 8) * h
        };
      }

      // Draw grid
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      for (var g = -4; g <= 4; g++) {
        var p1 = toScreen(g, -4), p2 = toScreen(g, 4);
        ctx.beginPath(); ctx.moveTo(p1.sx, p1.sy); ctx.lineTo(p2.sx, p2.sy); ctx.stroke();
        var p3 = toScreen(-4, g), p4 = toScreen(4, g);
        ctx.beginPath(); ctx.moveTo(p3.sx, p3.sy); ctx.lineTo(p4.sx, p4.sy); ctx.stroke();
      }

      // Axes
      var origin = toScreen(0, 0);
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(origin.sx, 0); ctx.lineTo(origin.sx, h); ctx.stroke();

      // Vector Field Grid
      var steps = 14;
      for (var ix = 0; ix <= steps; ix++) {
        for (var iy = 0; iy <= steps; iy++) {
          var vx = -3.8 + (ix / steps) * 7.6;
          var vy = -3.8 + (iy / steps) * 7.6;
          var dx = a * vx + b * vy;
          var dy = c * vx + d * vy;
          var len = Math.hypot(dx, dy);
          if (len > 1e-4) {
            var normLen = 0.22;
            var ex = vx + (dx / len) * normLen;
            var ey = vy + (dy / len) * normLen;
            var s0 = toScreen(vx, vy);
            var s1 = toScreen(ex, ey);

            ctx.strokeStyle = 'rgba(148, 163, 184, 0.25)';
            ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(s0.sx, s0.sy); ctx.lineTo(s1.sx, s1.sy); ctx.stroke();
          }
        }
      }

      // Eigenvalues & Invariants
      var tr = a + d;
      var det = a * d - b * c;
      var disc = tr * tr - 4 * det;
      var typeStr = '';
      if (det < 0) typeStr = 'Saddle Point (Unstable)';
      else if (Math.abs(tr) < 1e-4 && det > 0) typeStr = 'Center (Stable Ellipses)';
      else if (disc < 0) typeStr = (tr < 0 ? 'Stable Spiral (Focus)' : 'Unstable Spiral');
      else typeStr = (tr < 0 ? 'Stable Node' : 'Unstable Node');

      statsEl.innerText = `Tr(A)=${tr.toFixed(2)}  Det(A)=${det.toFixed(2)}  [${typeStr}]`;

      // Update & Draw Particles (RK4 integration)
      var dt = 0.02 * parseFloat(speedInput.value);
      for (var i = 0; i < particles.length; i++) {
        var p = particles[i];

        // RK4 Step
        function deriv(x, y) {
          return { dx: a * x + b * y, dy: c * x + d * y };
        }
        var k1 = deriv(p.x, p.y);
        var k2 = deriv(p.x + 0.5 * dt * k1.dx, p.y + 0.5 * dt * k1.dy);
        var k3 = deriv(p.x + 0.5 * dt * k2.dx, p.y + 0.5 * dt * k2.dy);
        var k4 = deriv(p.x + dt * k3.dx, p.y + dt * k3.dy);

        p.x += (dt / 6) * (k1.dx + 2 * k2.dx + 2 * k3.dx + k4.dx);
        p.y += (dt / 6) * (k1.dy + 2 * k2.dy + 2 * k3.dy + k4.dy);
        p.path.push({ x: p.x, y: p.y });
        if (p.path.length > 90) p.path.shift();
        p.life += dt;

        // Reset if drifted outside or converged too close
        if (Math.abs(p.x) > 4.5 || Math.abs(p.y) > 4.5 || Math.hypot(p.x, p.y) < 0.02 || p.life > 18) {
          var ang = Math.random() * Math.PI * 2;
          var r = 1.0 + Math.random() * 2.5;
          p.x = r * Math.cos(ang);
          p.y = r * Math.sin(ang);
          p.path = [{x: p.x, y: p.y}];
          p.life = 0;
        }

        // Draw trajectory trail
        if (p.path.length > 1) {
          ctx.strokeStyle = p.color;
          ctx.lineWidth = 1.8;
          ctx.beginPath();
          var start = toScreen(p.path[0].x, p.path[0].y);
          ctx.moveTo(start.sx, start.sy);
          for (var j = 1; j < p.path.length; j++) {
            var pt = toScreen(p.path[j].x, p.path[j].y);
            ctx.lineTo(pt.sx, pt.sy);
          }
          ctx.stroke();
        }

        // Draw particle head
        var cur = toScreen(p.x, p.y);
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(cur.sx, cur.sy, 3, 0, Math.PI * 2);
        ctx.fill();
      }

      if (running) animId = requestAnimationFrame(render);
    }
    render();

    return {
      destroy: function() {
        running = false;
        if (animId) cancelAnimationFrame(animId);
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 2. ode2-eigen-decomp-sim: Generalized Eigenvectors & Jordan Chains
  // =========================================================================
  window.SimulationEngine.register('ode2-eigen-decomp-sim', function(container) {
    var kit = setupCanvas(container, 340);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var lambda = -0.5;
    var shear = 1.0;
    var time = 0;
    var running = true;
    var animId = null;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Defect Shear \\eta:</span>
        <input type="range" id="ode2-shear" min="0.0" max="2.0" step="0.1" value="1.0" style="width:80px;">
        <span id="ode2-shear-val" style="font-family:monospace;width:30px;">1.0</span>
      </label>
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Eigenvalue \\lambda:</span>
        <input type="range" id="ode2-lambda" min="-1.5" max="0.5" step="0.1" value="-0.5" style="width:80px;">
        <span id="ode2-lambda-val" style="font-family:monospace;width:35px;">-0.5</span>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#a855f7;">
        \\vec{x}(t) = e^{\\lambda t}(\\vec{v}_1 + \\eta t \\vec{v}_2)
      </div>
    `;

    var shearSlider = controls.querySelector('#ode2-shear');
    var lambdaSlider = controls.querySelector('#ode2-lambda');
    var shearVal = controls.querySelector('#ode2-shear-val');
    var lambdaVal = controls.querySelector('#ode2-lambda-val');

    shearSlider.addEventListener('input', function() {
      shear = parseFloat(this.value);
      shearVal.innerText = shear.toFixed(1);
    });
    lambdaSlider.addEventListener('input', function() {
      lambda = parseFloat(this.value);
      lambdaVal.innerText = lambda.toFixed(1);
    });

    function render() {
      time += 0.02;
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      function toScreen(x, y) {
        return {
          sx: ((x + 3.5) / 7.0) * w,
          sy: ((3.5 - y) / 7.0) * h
        };
      }

      // Draw Axes
      var origin = toScreen(0, 0);
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(origin.sx, 0); ctx.lineTo(origin.sx, h); ctx.stroke();

      // Draw Eigenvector v1 = [1, 0] along X-axis
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      var ev1Start = toScreen(-3, 0), ev1End = toScreen(3, 0);
      ctx.beginPath(); ctx.moveTo(ev1Start.sx, ev1Start.sy); ctx.lineTo(ev1End.sx, ev1End.sy); ctx.stroke();
      ctx.fillStyle = '#38bdf8';
      ctx.font = '12px sans-serif';
      ctx.fillText('Eigenvector v₁ span', ev1End.sx - 130, ev1End.sy - 8);

      // Trajectories for multiple initial points
      var inits = [
        {x: 2.0, y: 1.5, col: '#f43f5e'},
        {x: 2.0, y: -1.5, col: '#fb923c'},
        {x: -2.0, y: 1.5, col: '#a855f7'},
        {x: -2.0, y: -1.5, col: '#10b981'},
        {x: 0.2, y: 2.2, col: '#eab308'},
        {x: -0.2, y: -2.2, col: '#06b6d4'}
      ];

      for (var i = 0; i < inits.length; i++) {
        var pt = inits[i];
        ctx.strokeStyle = pt.col;
        ctx.lineWidth = 2;
        ctx.beginPath();

        var tSpan = 4.0;
        var tStep = 0.05;
        var first = true;
        for (var t = 0; t <= tSpan; t += tStep) {
          // Jordan defective form: x(t) = e^(lambda*t) * (x0 + eta * t * y0), y(t) = e^(lambda*t) * y0
          var expF = Math.exp(lambda * t);
          var xt = expF * (pt.x + shear * t * pt.y);
          var yt = expF * pt.y;
          var sc = toScreen(xt, yt);
          if (first) { ctx.moveTo(sc.sx, sc.sy); first = false; }
          else { ctx.lineTo(sc.sx, sc.sy); }
        }
        ctx.stroke();

        // Pulsing head
        var tCur = (time * 0.8) % tSpan;
        var expFC = Math.exp(lambda * tCur);
        var xC = expFC * (pt.x + shear * tCur * pt.y);
        var yC = expFC * pt.y;
        var scCur = toScreen(xC, yC);
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(scCur.sx, scCur.sy, 4, 0, Math.PI * 2);
        ctx.fill();
      }

      if (running) animId = requestAnimationFrame(render);
    }
    render();

    return {
      destroy: function() {
        running = false;
        if (animId) cancelAnimationFrame(animId);
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 3. ode2-matrix-exp-sim: Matrix Exponential Flow e^(At)
  // =========================================================================
  window.SimulationEngine.register('ode2-matrix-exp-sim', function(container) {
    var kit = setupCanvas(container, 340);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var omega = 1.2;
    var sigma = -0.2;
    var t = 0;
    var running = true;
    var animId = null;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Damping \\sigma:</span>
        <input type="range" id="ode2-sigma" min="-0.8" max="0.4" step="0.05" value="-0.2" style="width:80px;">
        <span id="ode2-sigma-val" style="font-family:monospace;width:35px;">-0.2</span>
      </label>
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Rotation \\omega:</span>
        <input type="range" id="ode2-omega" min="0.2" max="3.0" step="0.2" value="1.2" style="width:80px;">
        <span id="ode2-omega-val" style="font-family:monospace;width:30px;">1.2</span>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#38bdf8;">
        e^{\\mathbf{A}t} = e^{\\sigma t}\\begin{pmatrix} \\cos\\omega t & -\\sin\\omega t \\\\ \\sin\\omega t & \\cos\\omega t \\end{pmatrix}
      </div>
    `;

    var sigmaSlider = controls.querySelector('#ode2-sigma');
    var omegaSlider = controls.querySelector('#ode2-omega');
    var sigmaVal = controls.querySelector('#ode2-sigma-val');
    var omegaVal = controls.querySelector('#ode2-omega-val');

    sigmaSlider.addEventListener('input', function() {
      sigma = parseFloat(this.value);
      sigmaVal.innerText = sigma.toFixed(2);
    });
    omegaSlider.addEventListener('input', function() {
      omega = parseFloat(this.value);
      omegaVal.innerText = omega.toFixed(1);
    });

    function render() {
      t += 0.025;
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      function toScreen(x, y) {
        return {
          sx: ((x + 2.5) / 5.0) * w,
          sy: ((2.5 - y) / 5.0) * h
        };
      }

      var origin = toScreen(0, 0);
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(origin.sx, 0); ctx.lineTo(origin.sx, h); ctx.stroke();

      // Current transformation of unit square vertices: (0,0), (1,0), (1,1), (0,1)
      var tMod = t % 8.0;
      var sFac = Math.exp(sigma * tMod);
      var cW = Math.cos(omega * tMod), sW = Math.sin(omega * tMod);

      // Basis vector e1 transforms to [sFac*cos, sFac*sin]
      // Basis vector e2 transforms to [-sFac*sin, sFac*cos]
      var p0 = toScreen(0, 0);
      var p1 = toScreen(sFac * cW, sFac * sW);
      var p2 = toScreen(sFac * (cW - sW), sFac * (sW + cW));
      var p3 = toScreen(-sFac * sW, sFac * cW);

      // Transformed area
      ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(p0.sx, p0.sy);
      ctx.lineTo(p1.sx, p1.sy);
      ctx.lineTo(p2.sx, p2.sy);
      ctx.lineTo(p3.sx, p3.sy);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Draw basis vector arrows
      function drawArrow(from, to, color, label) {
        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(from.sx, from.sy); ctx.lineTo(to.sx, to.sy); ctx.stroke();
        ctx.beginPath(); ctx.arc(to.sx, to.sy, 4, 0, Math.PI * 2); ctx.fill();
        ctx.font = '12px monospace';
        ctx.fillText(label, to.sx + 6, to.sy - 6);
      }
      drawArrow(p0, p1, '#ec4899', 'e^(At) e₁');
      drawArrow(p0, p3, '#10b981', 'e^(At) e₂');

      if (running) animId = requestAnimationFrame(render);
    }
    render();

    return {
      destroy: function() {
        running = false;
        if (animId) cancelAnimationFrame(animId);
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 4. ode2-legendre-series-sim: Legendre Polynomials P_n(x)
  // =========================================================================
  window.SimulationEngine.register('ode2-legendre-series-sim', function(container) {
    var kit = setupCanvas(container, 340);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    // Polynomial degree active selections
    var activeDegrees = { 0: true, 1: true, 2: true, 3: true, 4: true, 5: false };
    var colors = ['#64748b', '#38bdf8', '#4ade80', '#fbbf24', '#f43f5e', '#a855f7'];

    controls.innerHTML = `
      <span style="font-weight:600;">Degrees:</span>
      ${[0, 1, 2, 3, 4, 5].map(n => `
        <label style="display:flex;align-items:center;gap:4px;cursor:pointer;">
          <input type="checkbox" data-degree="${n}" ${activeDegrees[n] ? 'checked' : ''}>
          <span style="color:${colors[n]};font-family:monospace;font-weight:600;">P_{${n}}</span>
        </label>
      `).join('')}
      <div style="margin-left:auto;font-family:monospace;color:#94a3b8;">
        \\int_{-1}^1 P_n(x)P_m(x)dx = \\frac{2}{2n+1}\\delta_{nm}
      </div>
    `;

    controls.querySelectorAll('input[type="checkbox"]').forEach(function(cb) {
      cb.addEventListener('change', function() {
        var d = parseInt(this.dataset.degree);
        activeDegrees[d] = this.checked;
        drawCurves();
      });
    });

    // Compute Legendre polynomial value P_n(x) via Bonnet's recurrence
    function legendreP(n, x) {
      if (n === 0) return 1;
      if (n === 1) return x;
      var p0 = 1, p1 = x, p2 = 0;
      for (var k = 2; k <= n; k++) {
        p2 = ((2 * k - 1) * x * p1 - (k - 1) * p0) / k;
        p0 = p1;
        p1 = p2;
      }
      return p1;
    }

    function drawCurves() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      // Coordinate mapping: x in [-1.15, 1.15], y in [-1.2, 1.2]
      function toScreen(x, y) {
        return {
          sx: ((x + 1.15) / 2.3) * w,
          sy: ((1.2 - y) / 2.4) * h
        };
      }

      // Draw Grid & Boundaries [-1, 1]
      var bLeft = toScreen(-1, 0), bRight = toScreen(1, 0);
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(bLeft.sx, 0); ctx.lineTo(bLeft.sx, h); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(bRight.sx, 0); ctx.lineTo(bRight.sx, h); ctx.stroke();
      ctx.setLineDash([]);

      // Axes
      var origin = toScreen(0, 0);
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(origin.sx, 0); ctx.lineTo(origin.sx, h); ctx.stroke();

      // Draw each active polynomial
      for (var n = 0; n <= 5; n++) {
        if (!activeDegrees[n]) continue;
        ctx.strokeStyle = colors[n];
        ctx.lineWidth = 2.2;
        ctx.beginPath();

        var steps = 250;
        var first = true;
        for (var s = 0; s <= steps; s++) {
          var x = -1.0 + (s / steps) * 2.0;
          var y = legendreP(n, x);
          var pt = toScreen(x, y);
          if (first) { ctx.moveTo(pt.sx, pt.sy); first = false; }
          else { ctx.lineTo(pt.sx, pt.sy); }
        }
        ctx.stroke();
      }
    }
    drawCurves();

    return {
      destroy: function() {
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 5. ode2-frobenius-sim: Frobenius Method & Logarithmic Singular Solution
  // =========================================================================
  window.SimulationEngine.register('ode2-frobenius-sim', function(container) {
    var kit = setupCanvas(container, 340);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var r1 = 0.5;
    var r2 = 0.0;
    var logFactor = 0.0; // Case 2 toggle

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Frobenius Case:</span>
        <select id="ode2-frob-case" style="background:#1e293b;color:#f8fafc;border:1px solid #334155;border-radius:4px;padding:3px 6px;">
          <option value="distinct">Case 1: r₁ - r₂ ∉ ℤ (r₁=0.5, r₂=0.0)</option>
          <option value="equal">Case 2: r₁ = r₂ = 0 (Logarithmic Singularity)</option>
          <option value="integer">Case 3: r₁ - r₂ = 1 (Log Factor C ln x)</option>
        </select>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#38bdf8;">
        y(x) = x^r \\sum_{n=0}^\\infty a_n x^n + C y_1(x) \\ln x
      </div>
    `;

    var caseSelect = controls.querySelector('#ode2-frob-case');

    function updateParams() {
      var val = caseSelect.value;
      if (val === 'distinct') { r1 = 0.5; r2 = 0.0; logFactor = 0.0; }
      else if (val === 'equal') { r1 = 0.0; r2 = 0.0; logFactor = 1.0; }
      else if (val === 'integer') { r1 = 1.0; r2 = 0.0; logFactor = 0.5; }
      drawFrobenius();
    }
    caseSelect.addEventListener('change', updateParams);

    function drawFrobenius() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      function toScreen(x, y) {
        return {
          sx: (x / 2.5) * w,
          sy: ((2.0 - y) / 4.0) * h
        };
      }

      // Axes
      var origin = toScreen(0, 0);
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(origin.sx, 0); ctx.lineTo(origin.sx, h); ctx.stroke();

      // Solution 1: y1(x) = x^r1 * (1 - 0.5x + 0.1x^2)
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      var steps = 180;
      var first = true;
      for (var i = 1; i <= steps; i++) {
        var x = (i / steps) * 2.4;
        var y1 = Math.pow(x, r1) * (1 - 0.4 * x + 0.08 * x * x);
        var pt = toScreen(x, y1);
        if (first) { ctx.moveTo(pt.sx, pt.sy); first = false; }
        else { ctx.lineTo(pt.sx, pt.sy); }
      }
      ctx.stroke();

      // Solution 2: y2(x)
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      first = true;
      for (var j = 1; j <= steps; j++) {
        var x = (j / steps) * 2.4;
        var y1 = Math.pow(x, r1) * (1 - 0.4 * x + 0.08 * x * x);
        var y2 = Math.pow(x, r2) * (1 - 0.2 * x);
        if (logFactor > 0) {
          y2 += logFactor * y1 * Math.log(x);
        }
        var pt = toScreen(x, y2);
        if (pt.sy >= 0 && pt.sy <= h) {
          if (first) { ctx.moveTo(pt.sx, pt.sy); first = false; }
          else { ctx.lineTo(pt.sx, pt.sy); }
        }
      }
      ctx.stroke();

      // Labels
      ctx.font = '12px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('y₁(x) Branch', w - 120, toScreen(2.3, 0.8).sy);
      ctx.fillStyle = '#f43f5e';
      ctx.fillText('y₂(x) (Logarithmic/Second)', w - 210, toScreen(2.3, -0.6).sy);
    }
    drawFrobenius();

    return {
      destroy: function() {
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 6. ode2-bessel-harmonics-sim: Bessel Functions J_n & Drum Membrane Modes
  // =========================================================================
  window.SimulationEngine.register('ode2-bessel-harmonics-sim', function(container) {
    var kit = setupCanvas(container, 350);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var mode = 'curves'; // 'curves' or 'membrane'
    var order = 0;
    var time = 0;
    var running = true;
    var animId = null;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>View:</span>
        <select id="ode2-bessel-view" style="background:#1e293b;color:#f8fafc;border:1px solid #334155;border-radius:4px;padding:3px 6px;">
          <option value="curves">Cylindrical Functions J_0, J_1, J_2, Y_0</option>
          <option value="membrane">Vibrating Drum Membrane (2D Radial Modes)</option>
        </select>
      </label>
      <label id="ode2-mode-lbl" style="display:flex;align-items:center;gap:6px;">
        <span>Order n:</span>
        <select id="ode2-bessel-order" style="background:#1e293b;color:#f8fafc;border:1px solid #334155;border-radius:4px;padding:3px 6px;">
          <option value="0">n = 0 (Radially Symmetric)</option>
          <option value="1">n = 1 (One Nodal Diameter)</option>
          <option value="2">n = 2 (Two Nodal Diameters)</option>
        </select>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#10b981;">
        x^2 y'' + x y' + (x^2 - n^2)y = 0
      </div>
    `;

    var viewSelect = controls.querySelector('#ode2-bessel-view');
    var orderSelect = controls.querySelector('#ode2-bessel-order');

    viewSelect.addEventListener('change', function() { mode = this.value; });
    orderSelect.addEventListener('change', function() { order = parseInt(this.value); });

    // Bessel J_n approximations
    function besselJ(n, x) {
      if (x < 1e-4) return (n === 0 ? 1 : 0);
      if (x > 14) {
        return Math.sqrt(2 / (Math.PI * x)) * Math.cos(x - (n * Math.PI) / 2 - Math.PI / 4);
      }
      // Polynomial / series evaluation
      var sum = 0;
      var xHalf = x / 2;
      for (var m = 0; m < 12; m++) {
        var num = Math.pow(-1, m) * Math.pow(xHalf, 2 * m + n);
        // Factorial helper
        var factM = 1, factMN = 1;
        for (var k = 1; k <= m; k++) factM *= k;
        for (var k = 1; k <= m + n; k++) factMN *= k;
        sum += num / (factM * factMN);
      }
      return sum;
    }

    function render() {
      time += 0.03;
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      if (mode === 'curves') {
        // Curve Plotter Mode
        function toScreen(x, y) {
          return {
            sx: (x / 14.0) * w,
            sy: ((1.2 - y) / 2.2) * h
          };
        }

        var origin = toScreen(0, 0);
        ctx.strokeStyle = '#475569';
        ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(origin.sx, 0); ctx.lineTo(origin.sx, h); ctx.stroke();

        var curves = [
          { n: 0, col: '#38bdf8', label: 'J₀(x)' },
          { n: 1, col: '#4ade80', label: 'J₁(x)' },
          { n: 2, col: '#f59e0b', label: 'J₂(x)' }
        ];

        curves.forEach(function(c) {
          ctx.strokeStyle = c.col;
          ctx.lineWidth = 2.2;
          ctx.beginPath();
          var first = true;
          for (var s = 0; s <= 200; s++) {
            var x = (s / 200) * 14.0;
            var y = besselJ(c.n, x);
            var pt = toScreen(x, y);
            if (first) { ctx.moveTo(pt.sx, pt.sy); first = false; }
            else { ctx.lineTo(pt.sx, pt.sy); }
          }
          ctx.stroke();

          var labelPt = toScreen(12.5, besselJ(c.n, 12.5));
          ctx.fillStyle = c.col;
          ctx.font = '12px monospace';
          ctx.fillText(c.label, labelPt.sx, labelPt.sy - 6);
        });

      } else {
        // 2D Vibrating Drum Membrane Mode
        var cx = w / 2, cy = h / 2;
        var maxR = Math.min(w, h) * 0.42;
        var kRoot = (order === 0 ? 2.4048 : (order === 1 ? 3.8317 : 5.1356));
        var freq = 2.2;

        var imgData = ctx.createImageData(w, h);
        var data = imgData.data;

        for (var py = 0; py < h; py += 2) {
          for (var px = 0; px < w; px += 2) {
            var dx = px - cx;
            var dy = py - cy;
            var rPix = Math.hypot(dx, dy);
            if (rPix <= maxR) {
              var rNorm = (rPix / maxR) * kRoot;
              var theta = Math.atan2(dy, dx);
              var z = besselJ(order, rNorm) * Math.cos(order * theta) * Math.cos(freq * time);

              // Color mapping based on z deflection
              var rC = 15, gC = 23, bC = 42;
              if (z > 0) {
                // Blue-cyan elevation
                var factor = Math.min(1.0, z * 1.5);
                rC = Math.floor(15 + factor * 50);
                gC = Math.floor(23 + factor * 180);
                bC = Math.floor(42 + factor * 210);
              } else {
                // Purple-rose depression
                var factor = Math.min(1.0, -z * 1.5);
                rC = Math.floor(15 + factor * 220);
                gC = Math.floor(23 + factor * 60);
                bC = Math.floor(42 + factor * 120);
              }

              for (var oy = 0; oy < 2; oy++) {
                for (var ox = 0; ox < 2; ox++) {
                  var idx = ((py + oy) * w + (px + ox)) * 4;
                  data[idx] = rC;
                  data[idx + 1] = gC;
                  data[idx + 2] = bC;
                  data[idx + 3] = 255;
                }
              }
            }
          }
        }
        ctx.putImageData(imgData, 0, 0);

        // Clamped boundary ring
        ctx.strokeStyle = '#e2e8f0';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(cx, cy, maxR, 0, Math.PI * 2);
        ctx.stroke();
      }

      if (running) animId = requestAnimationFrame(render);
    }
    render();

    return {
      destroy: function() {
        running = false;
        if (animId) cancelAnimationFrame(animId);
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 7. ode2-sturm-liouville-sim: Sturm-Liouville Eigenvalue Shooting
  // =========================================================================
  window.SimulationEngine.register('ode2-sturm-liouville-sim', function(container) {
    var kit = setupCanvas(container, 340);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var lambdaVal = 4.0;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Trial Eigenvalue \\lambda:</span>
        <input type="range" id="ode2-sl-lambda" min="0.2" max="25.0" step="0.1" value="4.0" style="width:120px;">
        <span id="ode2-sl-val" style="font-family:monospace;width:40px;color:#38bdf8;">4.00</span>
      </label>
      <button id="ode2-sl-snap" style="background:#22c55e;color:white;border:none;padding:4px 10px;border-radius:4px;cursor:pointer;">Snap to Nearest Eigenmode</button>
      <div id="ode2-sl-stat" style="margin-left:auto;font-family:monospace;"></div>
    `;

    var lambdaSlider = controls.querySelector('#ode2-sl-lambda');
    var lambdaText = controls.querySelector('#ode2-sl-val');
    var snapBtn = controls.querySelector('#ode2-sl-snap');
    var statEl = controls.querySelector('#ode2-sl-stat');

    function drawSL() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      lambdaText.innerText = lambdaVal.toFixed(2);

      // System: y'' + lambda*y = 0, y(0) = 0, y(pi) = 0.
      // Exact solution y(x) = sin(sqrt(lambda)*x)
      var k = Math.sqrt(lambdaVal);
      var endVal = Math.sin(k * Math.PI);
      var isEigen = Math.abs(endVal) < 0.08;

      statEl.innerHTML = isEigen ? 
        `<span style="color:#4ade80;font-weight:bold;">★ Valid Eigenmode (y(π) ≈ 0, Nodes = ${Math.round(k)-1})</span>` :
        `<span style="color:#f87171;">Boundary Residual |y(π)| = ${Math.abs(endVal).toFixed(3)}</span>`;

      function toScreen(x, y) {
        return {
          sx: (x / (Math.PI * 1.15)) * w,
          sy: ((1.4 - y) / 2.8) * h
        };
      }

      // Boundary line at x = pi
      var bPi = toScreen(Math.PI, 0);
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(bPi.sx, 0); ctx.lineTo(bPi.sx, h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#ef4444';
      ctx.font = '12px sans-serif';
      ctx.fillText('x = π Target Boundary', bPi.sx - 130, 20);

      // Axes
      var origin = toScreen(0, 0);
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(origin.sx, 0); ctx.lineTo(origin.sx, h); ctx.stroke();

      // Plot Trajectory
      ctx.strokeStyle = isEigen ? '#22c55e' : '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      var steps = 200;
      var first = true;
      for (var s = 0; s <= steps; s++) {
        var x = (s / steps) * Math.PI;
        var y = Math.sin(k * x);
        var pt = toScreen(x, y);
        if (first) { ctx.moveTo(pt.sx, pt.sy); first = false; }
        else { ctx.lineTo(pt.sx, pt.sy); }
      }
      ctx.stroke();

      // Marker at end point
      var endPt = toScreen(Math.PI, endVal);
      ctx.fillStyle = isEigen ? '#22c55e' : '#ef4444';
      ctx.beginPath();
      ctx.arc(endPt.sx, endPt.sy, 6, 0, Math.PI * 2);
      ctx.fill();
    }

    lambdaSlider.addEventListener('input', function() {
      lambdaVal = parseFloat(this.value);
      drawSL();
    });

    snapBtn.addEventListener('click', function() {
      var k = Math.round(Math.sqrt(lambdaVal));
      if (k < 1) k = 1;
      lambdaVal = k * k;
      lambdaSlider.value = lambdaVal;
      drawSL();
    });

    drawSL();

    return {
      destroy: function() {
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 8. ode2-greens-function-sim: Green's Function Kernel & Response
  // =========================================================================
  window.SimulationEngine.register('ode2-greens-function-sim', function(container) {
    var kit = setupCanvas(container, 350);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var xi = 0.5; // Load location in (0, 1)

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Point Load Source \\xi:</span>
        <input type="range" id="ode2-gf-xi" min="0.05" max="0.95" step="0.01" value="0.5" style="width:120px;">
        <span id="ode2-gf-val" style="font-family:monospace;width:35px;color:#38bdf8;">0.50</span>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#f59e0b;">
        G(x, \\xi) = \\begin{cases} x(1-\\xi), & x \\le \\xi \\\\ \\xi(1-x), & x > \\xi \\end{cases}
      </div>
    `;

    var xiSlider = controls.querySelector('#ode2-gf-xi');
    var xiVal = controls.querySelector('#ode2-gf-val');

    function drawGreens() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      xiVal.innerText = xi.toFixed(2);

      function toScreen(x, y) {
        return {
          sx: ((x + 0.08) / 1.16) * w,
          sy: ((0.35 - y) / 0.42) * h
        };
      }

      // Boundaries at x=0 and x=1
      var b0 = toScreen(0, 0), b1 = toScreen(1, 0);
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(b0.sx, 0); ctx.lineTo(b0.sx, h); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(b1.sx, 0); ctx.lineTo(b1.sx, h); ctx.stroke();

      // Axis
      var origin = toScreen(0, 0);
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();

      // Load indicator arrow at xi
      var loadTop = toScreen(xi, 0.3);
      var loadBottom = toScreen(xi, xi * (1 - xi));
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(loadTop.sx, loadTop.sy); ctx.lineTo(loadBottom.sx, loadBottom.sy); ctx.stroke();
      ctx.fillStyle = '#f43f5e';
      ctx.beginPath();
      ctx.moveTo(loadBottom.sx, loadBottom.sy);
      ctx.lineTo(loadBottom.sx - 5, loadBottom.sy - 10);
      ctx.lineTo(loadBottom.sx + 5, loadBottom.sy - 10);
      ctx.closePath();
      ctx.fill();
      ctx.font = '12px sans-serif';
      ctx.fillText('Dirac Delta δ(x - ξ)', loadTop.sx - 45, loadTop.sy - 8);

      // Plot Green's Function Response
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.8;
      ctx.beginPath();
      var steps = 150;
      var first = true;
      for (var s = 0; s <= steps; s++) {
        var x = s / steps;
        var G = (x <= xi) ? x * (1 - xi) : xi * (1 - x);
        var pt = toScreen(x, G);
        if (first) { ctx.moveTo(pt.sx, pt.sy); first = false; }
        else { ctx.lineTo(pt.sx, pt.sy); }
      }
      ctx.stroke();

      // Shaded area under G(x, xi)
      ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
      ctx.lineTo(b1.sx, origin.sy);
      ctx.lineTo(b0.sx, origin.sy);
      ctx.closePath();
      ctx.fill();

      // Peak vertex
      var peak = toScreen(xi, xi * (1 - xi));
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.arc(peak.sx, peak.sy, 5, 0, Math.PI * 2);
      ctx.fill();
    }

    xiSlider.addEventListener('input', function() {
      xi = parseFloat(this.value);
      drawGreens();
    });

    drawGreens();

    return {
      destroy: function() {
        kit.cleanup();
      }
    };
  });

})();
