#!/usr/bin/env python3
"""
generate_complex_sims.py
Generates complex-analysis-sims.js containing 8 real-time 60 FPS HTML5 Canvas
numerical simulations for MTH 3103: Complex Analysis.
"""

sims_code = r'''/**
 * OpenSTEM Academic Library: Complex Analysis (MTH 3103)
 * High-Performance 60 FPS Interactive Numerical Simulations Suite
 *
 * Simulations:
 * 1. complex-stereographic-sim   - Stereographic Projection & The Riemann Sphere
 * 2. complex-cr-flow-sim         - Cauchy-Riemann Orthogonal Grid & Streamlines
 * 3. complex-contour-sim         - Interactive Contour Integration & Winding Numbers
 * 4. complex-max-modulus-sim     - Maximum Modulus Principle Landscape Visualizer
 * 5. complex-laurent-annulus-sim - Laurent Series Annular Convergence & Singularities
 * 6. complex-rouche-roots-sim    - Rouché's Theorem & Continuous Root Trajectories
 * 7. complex-contour-indent-sim  - Indented Contours & Branch Cut Keyhole Integrator
 * 8. complex-mobius-grid-sim     - Möbius (Bilinear) Transformation & Conformal Grid
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

  // Helper: Create High-DPI Canvas
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
    canvas.style.height = (heightPx || 350) + 'px';
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
  // 1. complex-stereographic-sim: Stereographic Projection & Riemann Sphere
  // =========================================================================
  window.SimulationEngine.register('complex-stereographic-sim', function(container) {
    var kit = setupCanvas(container, 360);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var px = 1.2, py = 0.8;
    var rotAngle = 0.6;
    var running = true;
    var animId = null;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Real x:</span>
        <input type="range" id="comp-stereo-x" min="-3.0" max="3.0" step="0.1" value="1.2" style="width:75px;">
        <span id="comp-stereo-x-val" style="font-family:monospace;width:30px;">1.2</span>
      </label>
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Imag y:</span>
        <input type="range" id="comp-stereo-y" min="-3.0" max="3.0" step="0.1" value="0.8" style="width:75px;">
        <span id="comp-stereo-y-val" style="font-family:monospace;width:30px;">0.8</span>
      </label>
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Sphere Rotate:</span>
        <input type="range" id="comp-stereo-rot" min="0" max="6.28" step="0.05" value="0.6" style="width:75px;">
      </label>
      <div id="comp-stereo-coords" style="margin-left:auto;font-family:monospace;color:#38bdf8;"></div>
    `;

    var xSlider = controls.querySelector('#comp-stereo-x');
    var ySlider = controls.querySelector('#comp-stereo-y');
    var rotSlider = controls.querySelector('#comp-stereo-rot');
    var xVal = controls.querySelector('#comp-stereo-x-val');
    var yVal = controls.querySelector('#comp-stereo-y-val');
    var coordsEl = controls.querySelector('#comp-stereo-coords');

    xSlider.addEventListener('input', function() { px = parseFloat(this.value); xVal.innerText = px.toFixed(1); });
    ySlider.addEventListener('input', function() { py = parseFloat(this.value); yVal.innerText = py.toFixed(1); });
    rotSlider.addEventListener('input', function() { rotAngle = parseFloat(this.value); });

    function render() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      // Stereographic formula from North Pole (0, 0, 1) to z = x + iy on plane Z = 0:
      // X = 2x / (|z|^2 + 1), Y = 2y / (|z|^2 + 1), Z = (|z|^2 - 1) / (|z|^2 + 1)
      var modSq = px * px + py * py;
      var denom = modSq + 1.0;
      var sX = (2 * px) / denom;
      var sY = (2 * py) / denom;
      var sZ = (modSq - 1.0) / denom;

      coordsEl.innerText = `z = ${px.toFixed(2)} + ${py.toFixed(2)}i  =>  S = (${sX.toFixed(2)}, ${sY.toFixed(2)}, ${sZ.toFixed(2)})`;

      // 3D Isometric Projection setup
      var cx = w * 0.5, cy = h * 0.52;
      var scale = Math.min(w, h) * 0.22;

      function project3D(x, y, z) {
        // Rotate around Z axis by rotAngle
        var rx = x * Math.cos(rotAngle) - y * Math.sin(rotAngle);
        var ry = x * Math.sin(rotAngle) + y * Math.cos(rotAngle);
        // Standard oblique / dimetric projection
        var sx = cx + (rx - ry * 0.4) * scale;
        var sy = cy + (-z + ry * 0.5) * scale;
        return { sx: sx, sy: sy };
      }

      // Draw Complex Plane Grid at Z = 0
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      for (var g = -3; g <= 3; g++) {
        var p1 = project3D(g, -3, -1), p2 = project3D(g, 3, -1);
        ctx.beginPath(); ctx.moveTo(p1.sx, p1.sy); ctx.lineTo(p2.sx, p2.sy); ctx.stroke();
        var p3 = project3D(-3, g, -1), p4 = project3D(3, g, -1);
        ctx.beginPath(); ctx.moveTo(p3.sx, p3.sy); ctx.lineTo(p4.sx, p4.sy); ctx.stroke();
      }

      // Draw Unit Sphere Wireframe
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.2)';
      ctx.lineWidth = 1.2;

      // Equator circle
      ctx.beginPath();
      for (var a = 0; a <= 60; a++) {
        var ang = (a / 60) * Math.PI * 2;
        var pt = project3D(Math.cos(ang), Math.sin(ang), 0);
        if (a === 0) ctx.moveTo(pt.sx, pt.sy); else ctx.lineTo(pt.sx, pt.sy);
      }
      ctx.stroke();

      // Meridians
      for (var m = 0; m < 4; m++) {
        var mAng = (m / 4) * Math.PI;
        ctx.beginPath();
        for (var a = 0; a <= 60; a++) {
          var ang = (a / 60) * Math.PI * 2;
          var pt = project3D(Math.cos(ang) * Math.cos(mAng), Math.cos(ang) * Math.sin(mAng), Math.sin(ang));
          if (a === 0) ctx.moveTo(pt.sx, pt.sy); else ctx.lineTo(pt.sx, pt.sy);
        }
        ctx.stroke();
      }

      // North Pole N = (0, 0, 1)
      var ptN = project3D(0, 0, 1);
      ctx.fillStyle = '#f43f5e';
      ctx.beginPath(); ctx.arc(ptN.sx, ptN.sy, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#f43f5e';
      ctx.font = '12px monospace';
      ctx.fillText('North Pole N (∞)', ptN.sx + 8, ptN.sy - 4);

      // Point on sphere S = (sX, sY, sZ)
      var ptS = project3D(sX, sY, sZ);
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath(); ctx.arc(ptS.sx, ptS.sy, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('P(z) on S²', ptS.sx + 8, ptS.sy - 4);

      // Point on complex plane z = (px, py, -1)
      var ptZ = project3D(px, py, -1);
      ctx.fillStyle = '#a855f7';
      ctx.beginPath(); ctx.arc(ptZ.sx, ptZ.sy, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#a855f7';
      ctx.fillText('z in ℂ', ptZ.sx + 8, ptZ.sy + 12);

      // Projection Ray: N -> S -> z (Straight line in 3D)
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 2;
      ctx.setLineDash([5, 4]);
      ctx.beginPath();
      ctx.moveTo(ptN.sx, ptN.sy);
      ctx.lineTo(ptZ.sx, ptZ.sy);
      ctx.stroke();
      ctx.setLineDash([]);

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
  // 2. complex-cr-flow-sim: Cauchy-Riemann Orthogonal Grid & Streamlines
  // =========================================================================
  window.SimulationEngine.register('complex-cr-flow-sim', function(container) {
    var kit = setupCanvas(container, 350);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var power = 2; // f(z) = z^2, z^3, or 1/z
    var numLines = 10;
    var running = true;
    var animId = null;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Function f(z):</span>
        <select id="comp-cr-func" style="background:#1e293b;color:#f8fafc;border:1px solid #334155;border-radius:4px;padding:3px 6px;">
          <option value="z2">f(z) = z² (Stagnation Flow)</option>
          <option value="z3">f(z) = z³ (Sextant Flow)</option>
          <option value="invz">f(z) = 1/z (Dipole Field)</option>
          <option value="expz">f(z) = exp(z) (Exponential Map)</option>
        </select>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#10b981;">
        <span style="color:#38bdf8;">— Potential u(x,y)=c</span> &nbsp;&nbsp;
        <span style="color:#f43f5e;">— Streamline v(x,y)=k</span>
      </div>
    `;

    var funcSelect = controls.querySelector('#comp-cr-func');
    var funcType = 'z2';
    funcSelect.addEventListener('change', function() { funcType = this.value; });

    function render() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      function toScreen(x, y) {
        return {
          sx: ((x + 2.5) / 5.0) * w,
          sy: ((2.5 - y) / 5.0) * h
        };
      }

      // Draw Grid Axes
      var origin = toScreen(0, 0);
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(origin.sx, 0); ctx.lineTo(origin.sx, h); ctx.stroke();

      // Marching squares or parameter curves for u = const and v = const
      // For f(z) = z^2: u = x^2 - y^2 = c, v = 2xy = k
      // For f(z) = z^3: u = x^3 - 3xy^2, v = 3x^2y - y^3
      // For f(z) = 1/z: u = x/(x^2+y^2), v = -y/(x^2+y^2)
      // For f(z) = exp(z): u = e^x cos y, v = e^x sin y

      var res = 120;
      var dx = 5.0 / res, dy = 5.0 / res;

      // Draw level curves via sampling
      function evalF(x, y) {
        if (funcType === 'z2') return { u: x * x - y * y, v: 2 * x * y };
        if (funcType === 'z3') return { u: x * x * x - 3 * x * y * y, v: 3 * x * x * y - y * y * y };
        if (funcType === 'invz') {
          var r2 = x * x + y * y + 1e-4;
          return { u: x / r2, v: -y / r2 };
        }
        if (funcType === 'expz') return { u: Math.exp(x) * Math.cos(y), v: Math.exp(x) * Math.sin(y) };
        return { u: x, v: y };
      }

      // Draw equipotentials u = c (Cyan)
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 1.6;
      for (var cVal = -3.0; cVal <= 3.0; cVal += 0.8) {
        ctx.beginPath();
        for (var i = 0; i <= res; i++) {
          var gx = -2.5 + i * dx;
          for (var j = 0; j <= res; j++) {
            var gy = -2.5 + j * dy;
            var val = evalF(gx, gy).u;
            var valNext = evalF(gx + dx, gy).u;
            if ((val - cVal) * (valNext - cVal) <= 0) {
              var pt = toScreen(gx, gy);
              ctx.rect(pt.sx, pt.sy, 1.5, 1.5);
            }
          }
        }
        ctx.stroke();
      }

      // Draw streamlines v = k (Rose)
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 1.6;
      for (var kVal = -3.0; kVal <= 3.0; kVal += 0.8) {
        ctx.beginPath();
        for (var i = 0; i <= res; i++) {
          var gx = -2.5 + i * dx;
          for (var j = 0; j <= res; j++) {
            var gy = -2.5 + j * dy;
            var val = evalF(gx, gy).v;
            var valNext = evalF(gx, gy + dy).v;
            if ((val - kVal) * (valNext - kVal) <= 0) {
              var pt = toScreen(gx, gy);
              ctx.rect(pt.sx, pt.sy, 1.5, 1.5);
            }
          }
        }
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
  // 3. complex-contour-sim: Interactive Contour & Winding Numbers
  // =========================================================================
  window.SimulationEngine.register('complex-contour-sim', function(container) {
    var kit = setupCanvas(container, 350);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    // Poles at z1 = -1, z2 = 1
    var poles = [{x: -1.0, y: 0.0, res: 1.0}, {x: 1.0, y: 0.0, res: -1.0}];
    var radius = 1.8;
    var centerX = 0.0, centerY = 0.0;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Radius R:</span>
        <input type="range" id="comp-cntr-r" min="0.5" max="2.6" step="0.1" value="1.8" style="width:80px;">
        <span id="comp-cntr-r-val" style="font-family:monospace;width:30px;">1.8</span>
      </label>
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Center X:</span>
        <input type="range" id="comp-cntr-cx" min="-2.0" max="2.0" step="0.1" value="0.0" style="width:80px;">
        <span id="comp-cntr-cx-val" style="font-family:monospace;width:30px;">0.0</span>
      </label>
      <div id="comp-cntr-res" style="margin-left:auto;font-family:monospace;color:#facc15;font-weight:bold;"></div>
    `;

    var rSlider = controls.querySelector('#comp-cntr-r');
    var cxSlider = controls.querySelector('#comp-cntr-cx');
    var rVal = controls.querySelector('#comp-cntr-r-val');
    var cxVal = controls.querySelector('#comp-cntr-cx-val');
    var resEl = controls.querySelector('#comp-cntr-res');

    rSlider.addEventListener('input', function() { radius = parseFloat(this.value); rVal.innerText = radius.toFixed(1); drawContour(); });
    cxSlider.addEventListener('input', function() { centerX = parseFloat(this.value); cxVal.innerText = centerX.toFixed(1); drawContour(); });

    function drawContour() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      function toScreen(x, y) {
        return {
          sx: ((x + 3.0) / 6.0) * w,
          sy: ((2.2 - y) / 4.4) * h
        };
      }

      // Draw Axes
      var origin = toScreen(0, 0);
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(0, origin.sy); ctx.lineTo(w, origin.sy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(origin.sx, 0); ctx.lineTo(origin.sx, h); ctx.stroke();

      // Check which poles are enclosed
      var totalRes = 0;
      var enclosedCount = 0;
      for (var i = 0; i < poles.length; i++) {
        var p = poles[i];
        var dist = Math.hypot(p.x - centerX, p.y - centerY);
        var inside = dist < radius;
        if (inside) {
          totalRes += p.res;
          enclosedCount++;
        }

        // Draw pole marker
        var sp = toScreen(p.x, p.y);
        ctx.fillStyle = inside ? '#22c55e' : '#ef4444';
        ctx.beginPath(); ctx.arc(sp.sx, sp.sy, 6, 0, Math.PI * 2); ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(sp.sx - 4, sp.sy - 4); ctx.lineTo(sp.sx + 4, sp.sy + 4);
        ctx.moveTo(sp.sx + 4, sp.sy - 4); ctx.lineTo(sp.sx - 4, sp.sy + 4);
        ctx.stroke();

        ctx.fillStyle = inside ? '#22c55e' : '#ef4444';
        ctx.font = '12px monospace';
        ctx.fillText(`Pole z=${p.x} (Res=${p.res > 0 ? '+'+p.res : p.res})`, sp.sx - 40, sp.sy - 10);
      }

      resEl.innerText = `∮_C f(z)dz = 2πi(${totalRes}) = ${(totalRes * 2).toFixed(1)}πi`;

      // Draw Contour Loop C
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
      ctx.beginPath();
      var cCenter = toScreen(centerX, centerY);
      var rPix = (radius / 6.0) * w;
      ctx.arc(cCenter.sx, cCenter.sy, rPix, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // Draw orientation arrows on contour
      for (var k = 0; k < 4; k++) {
        var ang = (k / 4) * Math.PI * 2;
        var ax = centerX + radius * Math.cos(ang);
        var ay = centerY + radius * Math.sin(ang);
        var as = toScreen(ax, ay);
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(as.sx, as.sy, 4, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    drawContour();

    return {
      destroy: function() {
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 4. complex-max-modulus-sim: Maximum Modulus Principle Visualizer
  // =========================================================================
  window.SimulationEngine.register('complex-max-modulus-sim', function(container) {
    var kit = setupCanvas(container, 350);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var power = 2;
    var running = true;
    var animId = null;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Holomorphic Function:</span>
        <select id="comp-mm-func" style="background:#1e293b;color:#f8fafc;border:1px solid #334155;border-radius:4px;padding:3px 6px;">
          <option value="z2">f(z) = z² + 0.5</option>
          <option value="z3">f(z) = z³ - 0.3z</option>
          <option value="expz">f(z) = exp(z)</option>
        </select>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#4ade80;">
        max_{|z|≤1} |f(z)| strictly achieved on boundary |z|=1
      </div>
    `;

    var funcSel = controls.querySelector('#comp-mm-func');
    var currentF = 'z2';
    funcSel.addEventListener('change', function() { currentF = this.value; });

    function render() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      var cx = w * 0.5, cy = h * 0.5;
      var R = Math.min(w, h) * 0.42;

      // Color density map of |f(z)| inside unit disk
      var imgData = ctx.createImageData(w, h);
      var data = imgData.data;

      var maxVal = 1.5;

      for (var py = 0; py < h; py += 2) {
        for (var px = 0; px < w; px += 2) {
          var dx = (px - cx) / R;
          var dy = (cy - py) / R;
          var rMod = Math.hypot(dx, dy);
          if (rMod <= 1.0) {
            var modF = 0;
            if (currentF === 'z2') {
              // (x + iy)^2 + 0.5 = x^2 - y^2 + 0.5 + 2ixy
              var u = dx * dx - dy * dy + 0.5;
              var v = 2 * dx * dy;
              modF = Math.hypot(u, v);
            } else if (currentF === 'z3') {
              var u = dx * (dx * dx - 3 * dy * dy) - 0.3 * dx;
              var v = dy * (3 * dx * dx - dy * dy) - 0.3 * dy;
              modF = Math.hypot(u, v);
            } else if (currentF === 'expz') {
              modF = Math.exp(dx);
            }

            var norm = Math.min(1.0, modF / 2.5);
            // Color map: deep purple -> cyan -> yellow
            var red = Math.floor(norm * 255);
            var green = Math.floor(Math.sin(norm * Math.PI) * 200 + 40);
            var blue = Math.floor((1 - norm) * 220 + 35);

            for (var oy = 0; oy < 2; oy++) {
              for (var ox = 0; ox < 2; ox++) {
                var idx = ((py + oy) * w + (px + ox)) * 4;
                data[idx] = red;
                data[idx + 1] = green;
                data[idx + 2] = blue;
                data[idx + 3] = 255;
              }
            }
          }
        }
      }
      ctx.putImageData(imgData, 0, 0);

      // Boundary circle |z| = 1
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.arc(cx, cy, R, 0, Math.PI * 2);
      ctx.stroke();

      ctx.fillStyle = '#ffffff';
      ctx.font = '12px monospace';
      ctx.fillText('Boundary |z| = 1 (Peak Value Set)', cx - 110, cy - R - 8);

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
  // 5. complex-laurent-annulus-sim: Laurent Series Annular Convergence
  // =========================================================================
  window.SimulationEngine.register('complex-laurent-annulus-sim', function(container) {
    var kit = setupCanvas(container, 350);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var rInner = 0.8;
    var rOuter = 2.0;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Inner Radius r:</span>
        <input type="range" id="comp-lr-inner" min="0.3" max="1.4" step="0.1" value="0.8" style="width:80px;">
        <span id="comp-lr-inner-val" style="font-family:monospace;width:30px;">0.8</span>
      </label>
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Outer Radius R:</span>
        <input type="range" id="comp-lr-outer" min="1.5" max="2.6" step="0.1" value="2.0" style="width:80px;">
        <span id="comp-lr-outer-val" style="font-family:monospace;width:30px;">2.0</span>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#38bdf8;">
        f(z) = \\sum_{n=-\\infty}^\\infty c_n (z - z_0)^n
      </div>
    `;

    var inSlider = controls.querySelector('#comp-lr-inner');
    var outSlider = controls.querySelector('#comp-lr-outer');
    var inVal = controls.querySelector('#comp-lr-inner-val');
    var outVal = controls.querySelector('#comp-lr-outer-val');

    inSlider.addEventListener('input', function() { rInner = parseFloat(this.value); inVal.innerText = rInner.toFixed(1); drawAnnulus(); });
    outSlider.addEventListener('input', function() { rOuter = parseFloat(this.value); outVal.innerText = rOuter.toFixed(1); drawAnnulus(); });

    function drawAnnulus() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      var cx = w * 0.5, cy = h * 0.5;
      var scale = Math.min(w, h) * 0.16;

      // Draw Annulus Shading
      var rPixIn = rInner * scale;
      var rPixOut = rOuter * scale;

      ctx.fillStyle = 'rgba(56, 189, 248, 0.18)';
      ctx.beginPath();
      ctx.arc(cx, cy, rPixOut, 0, Math.PI * 2, false);
      ctx.arc(cx, cy, rPixIn, 0, Math.PI * 2, true);
      ctx.fill();

      // Outer boundary (Cyan)
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.2;
      ctx.beginPath(); ctx.arc(cx, cy, rPixOut, 0, Math.PI * 2); ctx.stroke();

      // Inner boundary (Rose)
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2.2;
      ctx.beginPath(); ctx.arc(cx, cy, rPixIn, 0, Math.PI * 2); ctx.stroke();

      // Central singularity z0
      ctx.fillStyle = '#ef4444';
      ctx.beginPath(); ctx.arc(cx, cy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#f87171';
      ctx.font = '12px monospace';
      ctx.fillText('Isolated Singularity z₀', cx - 75, cy + 22);

      // Labels
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`Outer Boundary |z - z₀| = R (${rOuter.toFixed(1)})`, cx + rPixOut + 8, cy - 8);
      ctx.fillStyle = '#f43f5e';
      ctx.fillText(`Inner Boundary |z - z₀| = r (${rInner.toFixed(1)})`, cx + rPixIn + 8, cy + 16);
    }
    drawAnnulus();

    return {
      destroy: function() {
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 6. complex-rouche-roots-sim: Rouché's Theorem & Continuous Root Trajectories
  // =========================================================================
  window.SimulationEngine.register('complex-rouche-roots-sim', function(container) {
    var kit = setupCanvas(container, 350);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    // Equation: f(z) + t g(z) = 0 for z^4 + t(2z + 1) = 0 inside |z| = 1.5
    var tParam = 0.5;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Perturbation t:</span>
        <input type="range" id="comp-rouche-t" min="0.0" max="1.5" step="0.05" value="0.5" style="width:100px;">
        <span id="comp-rouche-t-val" style="font-family:monospace;width:35px;color:#38bdf8;">0.50</span>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#22c55e;">
        |f(z)| > |g(z)| on C ⇒ Z_{f+g} = Z_f = 4 roots inside C
      </div>
    `;

    var tSlider = controls.querySelector('#comp-rouche-t');
    var tVal = controls.querySelector('#comp-rouche-t-val');

    tSlider.addEventListener('input', function() {
      tParam = parseFloat(this.value);
      tVal.innerText = tParam.toFixed(2);
      drawRouche();
    });

    function drawRouche() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      var cx = w * 0.5, cy = h * 0.5;
      var scale = Math.min(w, h) * 0.22;

      // Contour boundary C: |z| = 1.6
      var cRadius = 1.6 * scale;
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
      ctx.beginPath();
      ctx.arc(cx, cy, cRadius, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // Axes
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(0, cy); ctx.lineTo(w, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, 0); ctx.lineTo(cx, h); ctx.stroke();

      // Compute roots of z^4 + t(2z + 1) = 0 via Newton iteration
      for (var k = 0; k < 4; k++) {
        var baseAng = (k / 4) * Math.PI * 2 + Math.PI / 4;
        var rGuess = 1.0;
        var rx = rGuess * Math.cos(baseAng);
        var ry = rGuess * Math.sin(baseAng);

        // Newton-Raphson in 2D
        for (var it = 0; it < 15; it++) {
          // z^4
          var r2 = rx * rx - ry * ry;
          var i2 = 2 * rx * ry;
          var r4 = r2 * r2 - i2 * i2;
          var i4 = 2 * r2 * i2;
          // P(z) = z^4 + 2t z + t
          var P_re = r4 + 2 * tParam * rx + tParam;
          var P_im = i4 + 2 * tParam * ry;
          // P'(z) = 4z^3 + 2t
          var r3 = rx * r2 - ry * i2;
          var i3 = rx * i2 + ry * r2;
          var dP_re = 4 * r3 + 2 * tParam;
          var dP_im = 4 * i3;
          var dDenom = dP_re * dP_re + dP_im * dP_im + 1e-6;

          var corr_re = (P_re * dP_re + P_im * dP_im) / dDenom;
          var corr_im = (P_im * dP_re - P_re * dP_im) / dDenom;

          rx -= corr_re;
          ry -= corr_im;
        }

        var sRootX = cx + rx * scale;
        var sRootY = cy - ry * scale;

        // Draw Root Node
        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.arc(sRootX, sRootY, 6, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = '11px monospace';
        ctx.fillText(`Root z_${k+1}`, sRootX + 8, sRootY - 6);
      }

      ctx.fillStyle = '#38bdf8';
      ctx.font = '12px monospace';
      ctx.fillText('Contour |z| = 1.6', cx + cRadius - 130, cy - cRadius - 8);
    }
    drawRouche();

    return {
      destroy: function() {
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 7. complex-contour-indent-sim: Indented Contour & Keyhole Visualizer
  // =========================================================================
  window.SimulationEngine.register('complex-contour-indent-sim', function(container) {
    var kit = setupCanvas(container, 350);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    var contourMode = 'indent'; // 'indent' or 'keyhole'
    var eps = 0.25;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Contour Geometry:</span>
        <select id="comp-indent-mode" style="background:#1e293b;color:#f8fafc;border:1px solid #334155;border-radius:4px;padding:3px 6px;">
          <option value="indent">Semicircle with Indentation at z = 0 (Dirichlet/Jordan)</option>
          <option value="keyhole">Keyhole Contour around Branch Cut [0, ∞)</option>
        </select>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#f59e0b;">
        \\lim_{\\epsilon \\to 0} \\int_{\\Gamma_\\epsilon} = -i\\pi \\text{Res}(f, 0)
      </div>
    `;

    var modeSelect = controls.querySelector('#comp-indent-mode');
    modeSelect.addEventListener('change', function() {
      contourMode = this.value;
      drawContourShape();
    });

    function drawContourShape() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      var cx = w * 0.5, cy = h * 0.65;
      var R = Math.min(w, h) * 0.45;
      var epsPix = eps * R * 0.4;

      // Axis
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(0, cy); ctx.lineTo(w, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, 0); ctx.lineTo(cx, h); ctx.stroke();

      if (contourMode === 'indent') {
        // Indented Upper Semicircle
        ctx.strokeStyle = '#38bdf8';
        ctx.fillStyle = 'rgba(56, 189, 248, 0.12)';
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        // 1. Segment [-R, -eps] on real axis
        ctx.moveTo(cx - R, cy);
        ctx.lineTo(cx - epsPix, cy);

        // 2. Small clockwise semicircle over origin
        ctx.arc(cx, cy, epsPix, Math.PI, 0, true);

        // 3. Segment [eps, R] on real axis
        ctx.lineTo(cx + R, cy);

        // 4. Large counter-clockwise upper semicircle
        ctx.arc(cx, cy, R, 0, Math.PI, true);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Label Pole at 0
        ctx.fillStyle = '#ef4444';
        ctx.beginPath(); ctx.arc(cx, cy, 4, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#f87171';
        ctx.font = '12px monospace';
        ctx.fillText('Pole on axis (z = 0)', cx - 65, cy + 18);

        ctx.fillStyle = '#38bdf8';
        ctx.fillText('Large Arc Γ_R (R → ∞)', cx - 60, cy - R - 8);
        ctx.fillText('Indentation γ_ε (ε → 0)', cx + epsPix + 6, cy - epsPix - 4);

      } else {
        // Keyhole contour around [0, ∞)
        cy = h * 0.5;
        ctx.strokeStyle = '#f59e0b';
        ctx.fillStyle = 'rgba(245, 158, 11, 0.12)';
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        // Branch cut zigzag on positive real axis
        ctx.setLineDash([3, 3]);
        ctx.strokeStyle = '#ef4444';
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + R + 20, cy); ctx.stroke();
        ctx.setLineDash([]);

        ctx.strokeStyle = '#f59e0b';
        // Inner circle clockwise
        ctx.arc(cx, cy, epsPix, 0.15, Math.PI * 2 - 0.15, true);
        // Lower horizontal line to R
        ctx.lineTo(cx + R, cy + epsPix * 0.3);
        // Outer circle counter-clockwise
        ctx.arc(cx, cy, R, 0.05, Math.PI * 2 - 0.05, false);
        // Upper horizontal line back to inner circle
        ctx.lineTo(cx + epsPix, cy - epsPix * 0.3);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#ef4444';
        ctx.font = '12px monospace';
        ctx.fillText('Branch Cut [0, ∞)', cx + R * 0.4, cy + 20);
        ctx.fillStyle = '#f59e0b';
        ctx.fillText('Keyhole Corridor', cx + R * 0.4, cy - 14);
      }
    }
    drawContourShape();

    return {
      destroy: function() {
        kit.cleanup();
      }
    };
  });

  // =========================================================================
  // 8. complex-mobius-grid-sim: Möbius (Bilinear) Transformation Conformal Map
  // =========================================================================
  window.SimulationEngine.register('complex-mobius-grid-sim', function(container) {
    var kit = setupCanvas(container, 350);
    var canvas = kit.canvas, ctx = kit.ctx, controls = kit.controls;

    // w = (z - a) / (z + a) (Cayley map mapping right half plane to unit disk)
    var aParam = 1.0;

    controls.innerHTML = `
      <label style="display:flex;align-items:center;gap:6px;">
        <span>Parameter a:</span>
        <input type="range" id="comp-mob-a" min="0.4" max="2.5" step="0.1" value="1.0" style="width:100px;">
        <span id="comp-mob-a-val" style="font-family:monospace;width:30px;color:#38bdf8;">1.0</span>
      </label>
      <div style="margin-left:auto;font-family:monospace;color:#a855f7;">
        w = \\frac{z - a}{z + a} \\quad (\\text{Orthogonal Circles Preserved})
      </div>
    `;

    var aSlider = controls.querySelector('#comp-mob-a');
    var aVal = controls.querySelector('#comp-mob-a-val');

    aSlider.addEventListener('input', function() {
      aParam = parseFloat(this.value);
      aVal.innerText = aParam.toFixed(1);
      drawMobius();
    });

    function drawMobius() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      var cx = w * 0.5, cy = h * 0.5;
      var scale = Math.min(w, h) * 0.35;

      // Transform z = x + iy -> w = (z - a)/(z + a)
      function mobius(x, y) {
        var numX = x - aParam, numY = y;
        var denX = x + aParam, denY = y;
        var denMag = denX * denX + denY * denY + 1e-5;
        var wx = (numX * denX + numY * denY) / denMag;
        var wy = (numY * denX - numX * denY) / denMag;
        return { u: wx, v: wy };
      }

      function toScreen(u, v) {
        return {
          sx: cx + u * scale,
          sy: cy - v * scale
        };
      }

      // Unit Disk Boundary |w| = 1
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.arc(cx, cy, scale, 0, Math.PI * 2);
      ctx.stroke();

      // Transform vertical lines x = const in right-half plane (become circles in disk)
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 1.5;
      for (var vx = 0.1; vx <= 3.0; vx += 0.4) {
        ctx.beginPath();
        var first = true;
        for (var vy = -12.0; vy <= 12.0; vy += 0.2) {
          var mw = mobius(vx, vy);
          var pt = toScreen(mw.u, mw.v);
          if (first) { ctx.moveTo(pt.sx, pt.sy); first = false; }
          else { ctx.lineTo(pt.sx, pt.sy); }
        }
        ctx.stroke();
      }

      // Transform horizontal lines y = const (become orthogonal circular arcs)
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 1.5;
      for (var hy = -3.0; hy <= 3.0; hy += 0.5) {
        ctx.beginPath();
        var first = true;
        for (var hx = 0.0; hx <= 8.0; hx += 0.15) {
          var mw = mobius(hx, hy);
          var pt = toScreen(mw.u, mw.v);
          if (first) { ctx.moveTo(pt.sx, pt.sy); first = false; }
          else { ctx.lineTo(pt.sx, pt.sy); }
        }
        ctx.stroke();
      }

      ctx.fillStyle = '#ffffff';
      ctx.font = '12px monospace';
      ctx.fillText('Unit Disk |w| ≤ 1 (Conformal Image of RHP)', cx - 140, cy - scale - 8);
    }
    drawMobius();

    return {
      destroy: function() {
        kit.cleanup();
      }
    };
  });

})();
'''

with open('complex-analysis-sims.js', 'w', encoding='utf-8') as f:
    f.write(sims_code)
print('Successfully generated complex-analysis-sims.js')
