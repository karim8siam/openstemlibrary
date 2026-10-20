// Tensor Analysis Interactive Simulations Engine (60 FPS Canvas)
// Strictly ZERO course numbers permitted.
(function() {
  'use strict';

  // Global registry for simulation initialization
  window.TensorSims = window.TensorSims || {};

  // =========================================================================
  // Helper: HiDPI Canvas Setup
  // =========================================================================
  function setupCanvas(canvas) {
    var dpr = window.devicePixelRatio || 1;
    var rect = canvas.getBoundingClientRect();
    var width = rect.width || canvas.width || 800;
    var height = rect.height || canvas.height || 420;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    var ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);
    return { ctx: ctx, width: width, height: height, dpr: dpr };
  }

  // =========================================================================
  // 1. UNIT 1: Curvilinear Coordinates & Dual Basis Visualizer
  // =========================================================================
  window.TensorSims.sim_tensor_coord_transform = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      mode: 'polar', // polar, shear, parabolic
      angle: 0.35,
      shear: 0.5,
      curvature: 0.4,
      u: 1.8,
      v: 1.2
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">System:
          <select id="${canvasId}-mode" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.25rem 0.5rem; border-radius:4px;">
            <option value="polar">Polar Coordinates (r, θ)</option>
            <option value="shear">Oblique / Affine Shear</option>
            <option value="parabolic">Parabolic Coordinates (u, v)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem;">Parameter:
          <input type="range" id="${canvasId}-param" min="0" max="1" step="0.01" value="0.5" style="vertical-align:middle; width:100px;">
        </label>
        <div id="${canvasId}-metrics" style="color:#38bdf8; font-family:monospace; font-size:0.8rem; margin-left:auto;"></div>
      `;

      var modeSelect = document.getElementById(canvasId + '-mode');
      var paramSlider = document.getElementById(canvasId + '-param');

      if (modeSelect) modeSelect.onchange = function(e) { state.mode = e.target.value; };
      if (paramSlider) paramSlider.oninput = function(e) {
        var val = parseFloat(e.target.value);
        state.shear = val * 1.5;
        state.curvature = val * 0.8;
        state.angle = val * Math.PI;
      };
    }

    var animId;
    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);

      // Background grid
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      var cx = w / 2;
      var cy = h / 2;
      var scale = 55;

      // Draw background Cartesian reference axes
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(0, cy); ctx.lineTo(w, cy);
      ctx.moveTo(cx, 0); ctx.lineTo(cx, h);
      ctx.stroke();

      // Transform functions: map (u, v) -> (x, y)
      function forward(u, v) {
        if (state.mode === 'polar') {
          // u = r, v = theta
          return { x: u * Math.cos(v), y: u * Math.sin(v) };
        } else if (state.mode === 'shear') {
          // x = u + s * v, y = v
          return { x: u + state.shear * v, y: v };
        } else {
          // Parabolic: x = (u^2 - v^2)/2, y = u * v
          return { x: (u*u - v*v) * 0.5, y: u * v };
        }
      }

      // Draw curvilinear coordinate mesh lines
      ctx.lineWidth = 1;
      var uMin = state.mode === 'polar' ? 0.4 : -3;
      var uMax = state.mode === 'polar' ? 3.5 : 3;
      var uStep = state.mode === 'polar' ? 0.6 : 0.6;

      var vMin = state.mode === 'polar' ? 0 : -3;
      var vMax = state.mode === 'polar' ? Math.PI * 2 : 3;
      var vStep = state.mode === 'polar' ? Math.PI / 8 : 0.6;

      // Lines of constant v (coordinate curves of u)
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.25)';
      for (var v = vMin; v <= vMax + 0.001; v += vStep) {
        ctx.beginPath();
        for (var u = uMin; u <= uMax; u += 0.05) {
          var p = forward(u, v);
          var px = cx + p.x * scale;
          var py = cy - p.y * scale;
          if (u === uMin) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Lines of constant u (coordinate curves of v)
      ctx.strokeStyle = 'rgba(168, 85, 247, 0.25)';
      for (var u = uMin; u <= uMax + 0.001; u += uStep) {
        ctx.beginPath();
        for (var v = vMin; v <= vMax; v += 0.05) {
          var p = forward(u, v);
          var px = cx + p.x * scale;
          var py = cy - p.y * scale;
          if (v === vMin) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Evaluation point P(u0, v0)
      var u0 = 2.0;
      var v0 = state.mode === 'polar' ? Math.PI / 4 : 1.2;
      var P = forward(u0, v0);
      var Px = cx + P.x * scale;
      var Py = cy - P.y * scale;

      // Compute Tangent Basis Vectors (e_1 = dr/du, e_2 = dr/dv) via finite difference
      var eps = 0.001;
      var Pu = forward(u0 + eps, v0);
      var Pv = forward(u0, v0 + eps);
      var e1x = (Pu.x - P.x) / eps;
      var e1y = (Pu.y - P.y) / eps;
      var e2x = (Pv.x - P.x) / eps;
      var e2y = (Pv.y - P.y) / eps;

      // Metric tensor components g_ij = e_i . e_j
      var g11 = e1x * e1x + e1y * e1y;
      var g12 = e1x * e2x + e1y * e2y;
      var g22 = e2x * e2x + e2y * e2y;
      var detG = g11 * g22 - g12 * g12;

      // Dual Reciprocal Basis e^1, e^2 (e^i = g^ij e_j)
      var ig11 = g22 / detG;
      var ig12 = -g12 / detG;
      var ig22 = g11 / detG;
      var e1_up_x = ig11 * e1x + ig12 * e2x;
      var e1_up_y = ig11 * e1y + ig12 * e2y;
      var e2_up_x = ig12 * e1x + ig22 * e2x;
      var e2_up_y = ig12 * e1y + ig22 * e2y;

      // Vector rendering helper
      function drawVector(ox, oy, vx, vy, color, label) {
        var vLen = Math.sqrt(vx * vx + vy * vy);
        var arrowScale = 40;
        var ex = ox + vx * arrowScale;
        var ey = oy - vy * arrowScale;

        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(ox, oy);
        ctx.lineTo(ex, ey);
        ctx.stroke();

        // Arrow head
        var angle = Math.atan2(-vy, vx);
        ctx.beginPath();
        ctx.moveTo(ex, ey);
        ctx.lineTo(ex - 10 * Math.cos(angle - Math.PI / 6), ey - 10 * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(ex - 10 * Math.cos(angle + Math.PI / 6), ey - 10 * Math.sin(angle + Math.PI / 6));
        ctx.fill();

        ctx.font = 'bold 12px monospace';
        ctx.fillText(label, ex + 6 * Math.cos(angle), ey + 6 * Math.sin(angle));
      }

      // Draw P
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.arc(Px, Py, 5, 0, Math.PI * 2);
      ctx.fill();

      // Tangent basis e_1 (cyan) and e_2 (purple)
      drawVector(Px, Py, e1x, e1y, '#38bdf8', 'e₁ = ∂r/∂u');
      drawVector(Px, Py, e2x, e2y, '#c084fc', 'e₂ = ∂r/∂v');

      // Dual reciprocal covectors e^1 (amber) and e^2 (emerald)
      drawVector(Px, Py, e1_up_x, e1_up_y, '#fbbf24', 'e¹ = ∇u');
      drawVector(Px, Py, e2_up_x, e2_up_y, '#34d399', 'e² = ∇v');

      // Update metrics readout
      var metricsEl = document.getElementById(canvasId + '-metrics');
      if (metricsEl) {
        metricsEl.innerHTML = `g₁₁=${g11.toFixed(2)} | g₁₂=${g12.toFixed(2)} | g₂₂=${g22.toFixed(2)} | √g=${Math.sqrt(Math.abs(detG)).toFixed(2)}`;
      }

      // HUD Legend
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.fillRect(15, 15, 270, 75);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(15, 15, 270, 75);
      ctx.fillStyle = '#f8fafc';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Natural Tangent Basis: e₁ (cyan), e₂ (purple)', 25, 35);
      ctx.fillText('Reciprocal Dual Basis: e¹ (amber), e² (green)', 25, 55);
      ctx.fillText('Dual Invariance: e_i · e^j = δ_i^j', 25, 75);

      animId = requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 2. UNIT 2: Tensor Algebra, Outer Products & Index Contraction
  // =========================================================================
  window.TensorSims.sim_tensor_algebra_contraction = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      preset: 'stress', // stress, shear, metric
      contract: true
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Preset Tensor T_ij:
          <select id="${canvasId}-preset" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.25rem 0.5rem; border-radius:4px;">
            <option value="stress">Cauchy Stress Tensor</option>
            <option value="shear">Asymmetric Rotation-Shear</option>
            <option value="orthogonal">Orthogonal Projector</option>
          </select>
        </label>
        <button id="${canvasId}-btn-toggle" style="background:#0284c7; color:#fff; border:none; padding:0.3rem 0.75rem; border-radius:4px; font-size:0.85rem; cursor:pointer;">
          Toggle Contraction Mode
        </button>
      `;

      var pSelect = document.getElementById(canvasId + '-preset');
      var tBtn = document.getElementById(canvasId + '-btn-toggle');
      if (pSelect) pSelect.onchange = function(e) { state.preset = e.target.value; };
      if (tBtn) tBtn.onclick = function() { state.contract = !state.contract; };
    }

    var t = 0;
    function render() {
      t += 0.02;
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = '#090d16';
      ctx.fillRect(0, 0, w, h);

      // Define 3x3 tensor based on preset
      var M = [
        [3.0 + 0.5 * Math.sin(t), 1.2, -0.8],
        [1.2, 2.0 + 0.3 * Math.cos(t), 0.5],
        [-0.8, 0.5, 1.5]
      ];
      if (state.preset === 'shear') {
        M = [
          [2.0, 1.5 * Math.sin(t), -0.5],
          [-1.5 * Math.sin(t), 2.0, 1.0],
          [0.8, -1.0, 1.0]
        ];
      } else if (state.preset === 'orthogonal') {
        M = [
          [1.0, 0.0, 0.0],
          [0.0, Math.cos(t), -Math.sin(t)],
          [0.0, Math.sin(t), Math.cos(t)]
        ];
      }

      // Compute Symmetric T_(ij) and Antisymmetric T_[ij] parts
      var S = [[0,0,0],[0,0,0],[0,0,0]];
      var A = [[0,0,0],[0,0,0],[0,0,0]];
      var trace = 0;
      for (var i = 0; i < 3; i++) {
        trace += M[i][i];
        for (var j = 0; j < 3; j++) {
          S[i][j] = 0.5 * (M[i][j] + M[j][i]);
          A[i][j] = 0.5 * (M[i][j] - M[j][i]);
        }
      }

      // Matrix drawing function
      function drawMatrix(mat, ox, oy, title, color) {
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 13px Inter, sans-serif';
        ctx.fillText(title, ox, oy - 15);

        var cellW = 55;
        var cellH = 32;
        ctx.strokeStyle = color;
        ctx.lineWidth = 1.5;

        // Brackets
        ctx.beginPath();
        ctx.moveTo(ox - 5, oy); ctx.lineTo(ox - 10, oy); ctx.lineTo(ox - 10, oy + 3 * cellH); ctx.lineTo(ox - 5, oy + 3 * cellH);
        ctx.moveTo(ox + 3 * cellW + 5, oy); ctx.lineTo(ox + 3 * cellW + 10, oy); ctx.lineTo(ox + 3 * cellW + 10, oy + 3 * cellH); ctx.lineTo(ox + 3 * cellW + 5, oy + 3 * cellH);
        ctx.stroke();

        ctx.font = '12px monospace';
        for (var r = 0; r < 3; r++) {
          for (var c = 0; c < 3; c++) {
            var val = mat[r][c];
            var isDiag = r === c;
            ctx.fillStyle = isDiag ? '#38bdf8' : (val < 0 ? '#f43f5e' : '#cbd5e1');
            ctx.fillText(val.toFixed(2), ox + c * cellW + 10, oy + r * cellH + 20);
          }
        }
      }

      drawMatrix(M, 40, 80, 'Full Mixed Tensor Tⁱ_j', '#38bdf8');
      drawMatrix(S, 270, 80, 'Symmetric Part T₍ᵢⱼ₎', '#34d399');
      drawMatrix(A, 500, 80, 'Antisymmetric Part T_{[ij]}', '#f43f5e');

      // Visual Contraction / Trace Invariant display
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(40, 220, 680, 160);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(40, 220, 680, 160);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '14px Inter, sans-serif';
      ctx.fillText('Tensor Invariant: Trace Contraction Tr(T) = Tⁱ_i = δⁱ_j Tʲ_i', 60, 250);

      ctx.font = '13px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`Scalar Invariant I₁ = Tr(T) = ${M[0][0].toFixed(2)} + ${M[1][1].toFixed(2)} + ${M[2][2].toFixed(2)} = ${trace.toFixed(3)}`, 60, 280);

      var detM = M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]);
      ctx.fillStyle = '#34d399';
      ctx.fillText(`Third Invariant I₃ = det(T) = ${detM.toFixed(3)} (Invariant under coordinate rotation/reflection)`, 60, 310);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Quotient Law Rule: If T_ij u^i v^j = Inv for all arbitrary vectors u, v, then T_ij transforms strictly as a rank-(0,2) tensor.', 60, 345);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 3. UNIT 3: Riemannian Metric Geometry & Musical Isomorphisms
  // =========================================================================
  window.TensorSims.sim_tensor_metric_geometry = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      g11: 1.5,
      g12: 0.6,
      g22: 2.0,
      u1: 1.5,
      u2: 0.8,
      v1: -0.8,
      v2: 1.6
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">g₁₁:
          <input type="range" id="${canvasId}-g11" min="0.5" max="3" step="0.1" value="1.5" style="width:70px;">
        </label>
        <label style="color:#94a3b8; font-size:0.85rem;">g₁₂:
          <input type="range" id="${canvasId}-g12" min="-1.2" max="1.2" step="0.05" value="0.6" style="width:70px;">
        </label>
        <label style="color:#94a3b8; font-size:0.85rem;">g₂₂:
          <input type="range" id="${canvasId}-g22" min="0.5" max="3" step="0.1" value="2.0" style="width:70px;">
        </label>
        <span id="${canvasId}-feedback" style="color:#38bdf8; font-family:monospace; font-size:0.85rem; margin-left:auto;"></span>
      `;

      var g11In = document.getElementById(canvasId + '-g11');
      var g12In = document.getElementById(canvasId + '-g12');
      var g22In = document.getElementById(canvasId + '-g22');

      function updateMetric() {
        state.g11 = parseFloat(g11In.value);
        state.g12 = parseFloat(g12In.value);
        state.g22 = parseFloat(g22In.value);
      }
      if (g11In) g11In.oninput = updateMetric;
      if (g12In) g12In.oninput = updateMetric;
      if (g22In) g22In.oninput = updateMetric;
    }

    var dragging = null;
    canvas.onmousedown = function(e) {
      var rect = canvas.getBoundingClientRect();
      var mx = e.clientX - rect.left - (canvas.width / (2 * (window.devicePixelRatio||1)));
      var my = (canvas.height / (2 * (window.devicePixelRatio||1))) - (e.clientY - rect.top);
      var scale = 70;
      var curU = { x: state.u1 * scale, y: state.u2 * scale };
      var curV = { x: state.v1 * scale, y: state.v2 * scale };
      if (Math.hypot(mx - curU.x, my - curU.y) < 25) dragging = 'u';
      else if (Math.hypot(mx - curV.x, my - curV.y) < 25) dragging = 'v';
    };
    window.addEventListener('mouseup', function() { dragging = null; });
    window.addEventListener('mousemove', function(e) {
      if (!dragging) return;
      var rect = canvas.getBoundingClientRect();
      var mx = e.clientX - rect.left - (rect.width / 2);
      var my = (rect.height / 2) - (e.clientY - rect.top);
      var scale = 70;
      if (dragging === 'u') {
        state.u1 = mx / scale;
        state.u2 = my / scale;
      } else if (dragging === 'v') {
        state.v1 = mx / scale;
        state.v2 = my / scale;
      }
    });

    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var cx = w / 2;
      var cy = h / 2;
      var scale = 70;

      // Determinant of metric
      var detG = state.g11 * state.g22 - state.g12 * state.g12;
      var fbEl = document.getElementById(canvasId + '-feedback');
      if (fbEl) {
        if (detG <= 0) {
          fbEl.innerHTML = `<span style="color:#ef4444;">⚠️ det(g) ≤ 0 (Non-Riemannian!)</span>`;
        } else {
          fbEl.innerHTML = `det(g) = ${detG.toFixed(2)} | Positive Definite ✓`;
        }
      }

      // Draw metric indicatrix ellipse: g11 x^2 + 2 g12 x y + g22 y^2 = 1
      if (detG > 0) {
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        for (var theta = 0; theta <= Math.PI * 2; theta += 0.05) {
          var cosT = Math.cos(theta);
          var sinT = Math.sin(theta);
          var denom = state.g11 * cosT * cosT + 2 * state.g12 * cosT * sinT + state.g22 * sinT * sinT;
          if (denom > 0) {
            var r = 1.0 / Math.sqrt(denom);
            var px = cx + r * cosT * scale;
            var py = cy - r * sinT * scale;
            if (theta === 0) ctx.moveTo(px, py);
            else ctx.lineTo(px, py);
          }
        }
        ctx.closePath();
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Coordinate axes
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(0, cy); ctx.lineTo(w, cy);
      ctx.moveTo(cx, 0); ctx.lineTo(cx, h);
      ctx.stroke();

      // Vector rendering
      function drawVec(v1, v2, color, label) {
        var px = cx + v1 * scale;
        var py = cy - v2 * scale;
        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(px, py);
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(px, py, 6, 0, Math.PI * 2);
        ctx.fill();

        ctx.font = 'bold 13px Inter, sans-serif';
        ctx.fillText(label, px + 8, py - 8);
      }

      drawVec(state.u1, state.u2, '#38bdf8', 'u (drag)');
      drawVec(state.v1, state.v2, '#ec4899', 'v (drag)');

      // Riemannian inner product & lengths
      var lenU2 = state.g11 * state.u1 * state.u1 + 2 * state.g12 * state.u1 * state.u2 + state.g22 * state.u2 * state.u2;
      var lenV2 = state.g11 * state.v1 * state.v1 + 2 * state.g12 * state.v1 * state.v2 + state.g22 * state.v2 * state.v2;
      var lenU = lenU2 > 0 ? Math.sqrt(lenU2) : 0;
      var lenV = lenV2 > 0 ? Math.sqrt(lenV2) : 0;
      var innerProd = state.g11 * state.u1 * state.v1 + state.g12 * (state.u1 * state.v2 + state.u2 * state.v1) + state.g22 * state.u2 * state.v2;
      var cosTheta = (lenU > 0 && lenV > 0) ? (innerProd / (lenU * lenV)) : 0;
      cosTheta = Math.max(-1, Math.min(1, cosTheta));
      var angleDeg = Math.acos(cosTheta) * 180 / Math.PI;

      // Lowering indices: u_i = g_ij u^j
      var u_sub1 = state.g11 * state.u1 + state.g12 * state.u2;
      var u_sub2 = state.g12 * state.u1 + state.g22 * state.u2;

      // Info box
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(15, 15, 300, 140);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(15, 15, 300, 140);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('Riemannian Geometry Invariants:', 25, 35);
      ctx.font = '12px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`||u||_g = √(g_ij uⁱ uʲ) = ${lenU.toFixed(3)}`, 25, 58);
      ctx.fillStyle = '#ec4899';
      ctx.fillText(`||v||_g = √(g_ij vⁱ vʲ) = ${lenV.toFixed(3)}`, 25, 78);
      ctx.fillStyle = '#facc15';
      ctx.fillText(`g_ij uⁱ vʲ = ${innerProd.toFixed(3)}`, 25, 98);
      ctx.fillText(`Riemannian Angle θ = ${angleDeg.toFixed(1)}°`, 25, 118);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Index Lowering: u₁=${u_sub1.toFixed(2)}, u₂=${u_sub2.toFixed(2)}`, 25, 138);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 4. UNIT 4: Christoffel Symbols & Numerical Geodesic Ray Tracer
  // =========================================================================
  window.TensorSims.sim_tensor_christoffel_geodesic = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      surface: 'sphere', // sphere, torus, paraboloid
      launchAngle: 0.5,
      speed: 1.0,
      trail: []
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Surface Geometry:
          <select id="${canvasId}-geom" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.25rem 0.5rem; border-radius:4px;">
            <option value="sphere">2-Sphere S² (Constant K > 0)</option>
            <option value="hyperboloid">Poincaré Hyperbolic Disk (K < 0)</option>
            <option value="cylinder">Flat Cylinder (K = 0)</option>
          </select>
        </label>
        <button id="${canvasId}-btn-launch" style="background:#0284c7; color:#fff; border:none; padding:0.3rem 0.75rem; border-radius:4px; font-size:0.85rem; cursor:pointer;">
          Relaunch Geodesic
        </button>
      `;

      var gSelect = document.getElementById(canvasId + '-geom');
      var lBtn = document.getElementById(canvasId + '-btn-launch');
      if (gSelect) gSelect.onchange = function(e) {
        state.surface = e.target.value;
        resetGeodesic();
      };
      if (lBtn) lBtn.onclick = function() { resetGeodesic(); };
    }

    var pos = { u: 0.5, v: 0.0 };
    var vel = { u: 0.4, v: 0.8 };

    function resetGeodesic() {
      state.trail = [];
      if (state.surface === 'sphere') {
        pos = { u: Math.PI / 4, v: 0 };
        vel = { u: 0.0, v: 1.0 };
      } else if (state.surface === 'hyperboloid') {
        pos = { u: 0.0, v: 0.0 };
        vel = { u: 0.6, v: 0.5 };
      } else {
        pos = { u: 0.0, v: 0.0 };
        vel = { u: 0.8, v: 0.6 };
      }
    }
    resetGeodesic();

    function getChristoffel(u, v) {
      // Returns Gamma^k_ij for (u, v)
      if (state.surface === 'sphere') {
        // u = theta (colatitude), v = phi (azimuth). ds^2 = R^2 dθ^2 + R^2 sin^2θ dφ^2
        // Non-zero: Γ^θ_φφ = -sinθ cosθ, Γ^φ_θφ = cotθ
        var sinU = Math.sin(u);
        var cosU = Math.cos(u);
        var cotU = cosU / (sinU + 1e-6);
        return {
          G1_11: 0, G1_12: 0, G1_22: -sinU * cosU,
          G2_11: 0, G2_12: cotU, G2_22: 0
        };
      } else if (state.surface === 'hyperboloid') {
        // Poincaré metric ds^2 = 4(du^2 + dv^2)/(1 - (u^2 + v^2))^2
        var r2 = u * u + v * v;
        var factor = 2.0 / (1.0 - r2 + 1e-4);
        return {
          G1_11: factor * u, G1_12: factor * v, G1_22: -factor * u,
          G2_11: -factor * v, G2_12: factor * u, G2_22: factor * v
        };
      } else {
        // Flat cylinder ds^2 = dz^2 + R^2 dθ^2 -> all Christoffel vanish
        return {
          G1_11: 0, G1_12: 0, G1_22: 0,
          G2_11: 0, G2_12: 0, G2_22: 0
        };
      }
    }

    function stepGeodesic(dt) {
      // RK4 integration of geodesic equation:
      // d^2 u/ds^2 = - (Γ^1_11 u'^2 + 2 Γ^1_12 u' v' + Γ^1_22 v'^2)
      // d^2 v/ds^2 = - (Γ^2_11 u'^2 + 2 Γ^2_12 u' v' + Γ^2_22 v'^2)
      var G = getChristoffel(pos.u, pos.v);
      var accelU = -(G.G1_11 * vel.u * vel.u + 2 * G.G1_12 * vel.u * vel.v + G.G1_22 * vel.v * vel.v);
      var accelV = -(G.G2_11 * vel.u * vel.u + 2 * G.G2_12 * vel.u * vel.v + G.G2_22 * vel.v * vel.v);

      vel.u += accelU * dt;
      vel.v += accelV * dt;
      pos.u += vel.u * dt;
      pos.v += vel.v * dt;

      // Keep within domain
      if (state.surface === 'sphere') {
        if (pos.u < 0.05) pos.u = 0.05;
        if (pos.u > Math.PI - 0.05) pos.u = Math.PI - 0.05;
      }
      state.trail.push({ u: pos.u, v: pos.v });
      if (state.trail.length > 300) state.trail.shift();
    }

    function render() {
      for (var s = 0; s < 2; s++) stepGeodesic(0.02);

      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      var cx = w / 2;
      var cy = h / 2;

      // Map (u, v) to canvas screen coords
      function project(u, v) {
        if (state.surface === 'sphere') {
          // Equirectangular or orthographic projection of sphere
          var rad = 130;
          var x = cx + rad * Math.sin(u) * Math.sin(v);
          var y = cy - rad * Math.cos(u);
          return { x: x, y: y };
        } else if (state.surface === 'hyperboloid') {
          var rScale = 140;
          return { x: cx + u * rScale, y: cy - v * rScale };
        } else {
          var sc = 50;
          return { x: cx + v * sc, y: cy - u * sc };
        }
      }

      // Draw background sphere boundary / disk
      if (state.surface === 'sphere') {
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(cx, cy, 130, 0, Math.PI * 2);
        ctx.stroke();

        // Parallels & meridians
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        for (var lat = 0.3; lat < Math.PI; lat += 0.5) {
          ctx.beginPath();
          for (var lon = 0; lon <= Math.PI * 2; lon += 0.1) {
            var p = project(lat, lon);
            if (lon === 0) ctx.moveTo(p.x, p.y);
            else ctx.lineTo(p.x, p.y);
          }
          ctx.stroke();
        }
      } else if (state.surface === 'hyperboloid') {
        ctx.strokeStyle = 'rgba(168, 85, 247, 0.6)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(cx, cy, 140, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Draw geodesic trail
      if (state.trail.length > 1) {
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (var i = 0; i < state.trail.length; i++) {
          var pt = project(state.trail[i].u, state.trail[i].v);
          if (i === 0) ctx.moveTo(pt.x, pt.y);
          else ctx.lineTo(pt.x, pt.y);
        }
        ctx.stroke();
      }

      // Draw current particle position
      var cur = project(pos.u, pos.v);
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(cur.x, cur.y, 6, 0, Math.PI * 2);
      ctx.fill();

      // Non-zero Christoffel table display
      var G = getChristoffel(pos.u, pos.v);
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.fillRect(15, 15, 270, 110);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(15, 15, 270, 110);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('Live Christoffel Symbols Γᵏ_ij:', 25, 35);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`Γ¹_22 = ${G.G1_22.toFixed(3)}  |  Γ²_12 = ${G.G2_12.toFixed(3)}`, 25, 60);
      ctx.fillText(`Γ¹_11 = ${G.G1_11.toFixed(3)}  |  Γ²_22 = ${G.G2_22.toFixed(3)}`, 25, 80);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Geodesic Eq: d²xᵏ/ds² + Γᵏ_ij (dxⁱ/ds)(dxʲ/ds) = 0', 25, 105);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 5. UNIT 5: Parallel Transport, Holonomy Deficit & Covariant Derivative
  // =========================================================================
  window.TensorSims.sim_tensor_covariant_diff = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      colatitude: 0.7, // theta_0
      phi: 0.0,
      autoPlay: true
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Latitude Ring (θ₀):
          <input type="range" id="${canvasId}-lat" min="0.2" max="1.4" step="0.05" value="0.7" style="width:100px;">
        </label>
        <button id="${canvasId}-btn-play" style="background:#0284c7; color:#fff; border:none; padding:0.3rem 0.75rem; border-radius:4px; font-size:0.85rem; cursor:pointer;">
          Pause / Play Loop
        </button>
      `;

      var latIn = document.getElementById(canvasId + '-lat');
      var pBtn = document.getElementById(canvasId + '-btn-play');
      if (latIn) latIn.oninput = function(e) { state.colatitude = parseFloat(e.target.value); };
      if (pBtn) pBtn.onclick = function() { state.autoPlay = !state.autoPlay; };
    }

    var R = 130;
    function render() {
      if (state.autoPlay) {
        state.phi += 0.015;
        if (state.phi > Math.PI * 2) state.phi = 0;
      }

      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#090d16';
      ctx.fillRect(0, 0, w, h);

      var cx = w / 2;
      var cy = h / 2;

      // Draw Sphere outline
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(cx, cy, R, 0, Math.PI * 2);
      ctx.stroke();

      // Draw latitude ring at theta = colatitude
      var ringY = cy - R * Math.cos(state.colatitude);
      var ringRx = R * Math.sin(state.colatitude);
      var ringRy = ringRx * 0.35; // perspective flattening

      ctx.strokeStyle = 'rgba(251, 191, 36, 0.4)';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.ellipse(cx, ringY, ringRx, ringRy, 0, 0, Math.PI * 2);
      ctx.stroke();

      // Current point on ring
      var px = cx + ringRx * Math.cos(state.phi);
      var py = ringY + ringRy * Math.sin(state.phi);

      // Holonomy Angle calculation:
      // Parallel transport along a circle of colatitude θ rotates the vector by Δα = -2π cos(θ)
      // Instantaneous angle of the vector relative to the meridian:
      var vectorAngle = -state.phi * Math.cos(state.colatitude);
      var vecLen = 45;
      var vx = px + vecLen * Math.cos(vectorAngle);
      var vy = py - vecLen * Math.sin(vectorAngle);

      // Draw initial vector at phi = 0
      var initX = cx + ringRx;
      var initY = ringY;
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)';
      ctx.lineWidth = 2;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(initX, initY);
      ctx.lineTo(initX + vecLen, initY);
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw current parallel-transported vector
      ctx.strokeStyle = '#38bdf8';
      ctx.fillStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(px, py);
      ctx.lineTo(vx, vy);
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(px, py, 5, 0, Math.PI * 2);
      ctx.fill();

      // Total deficit angle after 2pi loop
      var totalDeficit = 2 * Math.PI * (1 - Math.cos(state.colatitude));
      var deficitDeg = (totalDeficit * 180 / Math.PI) % 360;

      // Invariant Info Panel
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.fillRect(15, 15, 320, 130);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(15, 15, 320, 130);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('Parallel Transport & Holonomy Deficit', 25, 35);
      ctx.font = '12px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`Transport Eq: DAⁱ/dt = dAⁱ/dt + Γⁱ_jk Aʲ (dxᵏ/dt) = 0`, 25, 60);
      ctx.fillStyle = '#facc15';
      ctx.fillText(`Current Azimuth φ: ${(state.phi * 180 / Math.PI).toFixed(1)}°`, 25, 80);
      ctx.fillStyle = '#34d399';
      ctx.fillText(`Holonomy Deficit Δψ = ∬ K dA = ${deficitDeg.toFixed(1)}°`, 25, 100);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Non-zero deficit directly reveals Riemann curvature!', 25, 125);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 6. UNIT 6: Riemann Curvature Tensor & Geodesic Deviation Visualizer
  // =========================================================================
  window.TensorSims.sim_tensor_riemann_curvature = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      curvatureK: 1.0, // positive, zero, negative
      separation: 15
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Curvature Regime:
          <select id="${canvasId}-k-select" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.25rem 0.5rem; border-radius:4px;">
            <option value="1.0">Elliptic / Positive (K > 0, Sphere)</option>
            <option value="0.0">Euclidean / Flat (K = 0, Plane)</option>
            <option value="-1.0">Hyperbolic / Negative (K < 0, Saddle)</option>
          </select>
        </label>
      `;

      var kSel = document.getElementById(canvasId + '-k-select');
      if (kSel) kSel.onchange = function(e) { state.curvatureK = parseFloat(e.target.value); };
    }

    var t = 0;
    function render() {
      t += 0.02;
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var cx = w / 2;
      var cy = h / 2;

      // Jacobi Geodesic Deviation equation: D^2 ξ / ds^2 + K ξ = 0
      // Solutions:
      // K > 0: ξ(s) = ξ_0 cos(√K s)  (Geodesics converge & cross)
      // K = 0: ξ(s) = ξ_0            (Geodesics remain parallel)
      // K < 0: ξ(s) = ξ_0 cosh(√|K| s) (Geodesics diverge exponentially)

      var K = state.curvatureK;
      var sMax = 3.5;
      var ds = 0.05;
      var scaleX = 85;
      var startX = 80;

      // Draw two geodesic rays starting with separation ξ0
      var xi0 = 25;

      ctx.lineWidth = 2.5;

      // Center baseline
      ctx.strokeStyle = '#334155';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(startX, cy);
      ctx.lineTo(startX + sMax * scaleX, cy);
      ctx.stroke();
      ctx.setLineDash([]);

      // Upper and lower geodesic curves
      ctx.strokeStyle = '#38bdf8';
      ctx.beginPath();
      for (var s = 0; s <= sMax; s += ds) {
        var xi;
        if (K > 0) xi = xi0 * Math.cos(Math.sqrt(K) * s * 0.8);
        else if (K < 0) xi = xi0 * Math.cosh(Math.sqrt(Math.abs(K)) * s * 0.5);
        else xi = xi0;

        var px = startX + s * scaleX;
        var py = cy - xi;
        if (s === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.strokeStyle = '#c084fc';
      ctx.beginPath();
      for (var s = 0; s <= sMax; s += ds) {
        var xi;
        if (K > 0) xi = xi0 * Math.cos(Math.sqrt(K) * s * 0.8);
        else if (K < 0) xi = xi0 * Math.cosh(Math.sqrt(Math.abs(K)) * s * 0.5);
        else xi = xi0;

        var px = startX + s * scaleX;
        var py = cy + xi;
        if (s === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Animated test particles
      var curS = (t % sMax);
      var curXi;
      if (K > 0) curXi = xi0 * Math.cos(Math.sqrt(K) * curS * 0.8);
      else if (K < 0) curXi = xi0 * Math.cosh(Math.sqrt(Math.abs(K)) * curS * 0.5);
      else curXi = xi0;

      var curPx = startX + curS * scaleX;
      // Draw deviation vector ξ
      ctx.strokeStyle = '#facc15';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(curPx, cy - curXi);
      ctx.lineTo(curPx, cy + curXi);
      ctx.stroke();

      ctx.fillStyle = '#38bdf8';
      ctx.beginPath(); ctx.arc(curPx, cy - curXi, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#c084fc';
      ctx.beginPath(); ctx.arc(curPx, cy + curXi, 5, 0, Math.PI * 2); ctx.fill();

      // Info Dashboard
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(440, 25, 330, 140);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(440, 25, 330, 140);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('Jacobi Geodesic Deviation Equation:', 455, 48);

      ctx.font = '12px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('D²ξⁱ/ds² + Rⁱ_jkl Tʲ Tᵏ ξˡ = 0', 455, 75);

      ctx.fillStyle = K > 0 ? '#34d399' : (K < 0 ? '#f43f5e' : '#94a3b8');
      var beh = K > 0 ? 'Converging (Tidal Attraction / Sphere)' : (K < 0 ? 'Diverging (Tidal Repulsion / Saddle)' : 'Parallel (Zero Curvature / Flat)');
      ctx.fillText(`Gaussian Curvature K = ${K.toFixed(1)}`, 455, 100);
      ctx.fillText(`Behavior: ${beh}`, 455, 120);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('The Riemann curvature tensor directly governs tidal forces.', 455, 145);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 7. UNIT 7: Conformal Rescaling & Angle Preservation Explorer
  // =========================================================================
  window.TensorSims.sim_tensor_weyl_conformal = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      omegaScale: 0.5,
      mode: 'joukowsky'
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Conformal Factor Ω²(x):
          <input type="range" id="${canvasId}-omega" min="0.1" max="1.0" step="0.05" value="0.5" style="width:100px;">
        </label>
        <span style="color:#38bdf8; font-size:0.85rem; margin-left:auto;">
          Metric: g̃_ij = Ω²(x) g_ij (Angles Invariant)
        </span>
      `;

      var oIn = document.getElementById(canvasId + '-omega');
      if (oIn) oIn.oninput = function(e) { state.omegaScale = parseFloat(e.target.value); };
    }

    var t = 0;
    function render() {
      t += 0.015;
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#090d16';
      ctx.fillRect(0, 0, w, h);

      var cx1 = w * 0.28;
      var cx2 = w * 0.72;
      var cy = h / 2;
      var scale = 40;

      // Draw original orthogonal grid on the left
      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Physical Domain (g_ij)', cx1 - 60, 30);
      ctx.fillText('Conformally Scaled (g̃_ij = Ω² g_ij)', cx2 - 90, 30);

      // Draw left grid
      ctx.lineWidth = 1;
      for (var u = -2; u <= 2; u += 0.5) {
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.35)';
        ctx.beginPath();
        ctx.moveTo(cx1 + u * scale, cy - 2 * scale);
        ctx.lineTo(cx1 + u * scale, cy + 2 * scale);
        ctx.stroke();

        ctx.strokeStyle = 'rgba(168, 85, 247, 0.35)';
        ctx.beginPath();
        ctx.moveTo(cx1 - 2 * scale, cy + u * scale);
        ctx.lineTo(cx1 + 2 * scale, cy + u * scale);
        ctx.stroke();
      }

      // Draw intersecting test lines showing 90-degree angle
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#facc15';
      ctx.beginPath();
      ctx.moveTo(cx1 - 1.2 * scale, cy);
      ctx.lineTo(cx1 + 1.2 * scale, cy);
      ctx.moveTo(cx1, cy - 1.2 * scale);
      ctx.lineTo(cx1, cy + 1.2 * scale);
      ctx.stroke();

      // Right: Conformal transformation w = z + a^2 / z or exp(z)
      function conformalMap(x, y) {
        var r2 = x * x + y * y + 0.1;
        var factor = 1.0 + state.omegaScale * Math.sin(t + x);
        return {
          x: x * factor - y * 0.2 * state.omegaScale,
          y: y * factor + x * 0.2 * state.omegaScale
        };
      }

      // Draw mapped curves on the right
      for (var u = -2; u <= 2; u += 0.5) {
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
        ctx.beginPath();
        for (var v = -2; v <= 2; v += 0.05) {
          var p = conformalMap(u, v);
          var px = cx2 + p.x * scale;
          var py = cy + p.y * scale;
          if (v === -2) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        ctx.strokeStyle = 'rgba(168, 85, 247, 0.4)';
        ctx.beginPath();
        for (var v = -2; v <= 2; v += 0.05) {
          var p = conformalMap(v, u);
          var px = cx2 + p.x * scale;
          var py = cy + p.y * scale;
          if (v === -2) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Right test lines (showing that intersection remains strictly 90 degrees!)
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#facc15';
      ctx.beginPath();
      for (var v = -1.2; v <= 1.2; v += 0.05) {
        var p = conformalMap(v, 0);
        var px = cx2 + p.x * scale;
        var py = cy + p.y * scale;
        if (v === -1.2) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      for (var v = -1.2; v <= 1.2; v += 0.05) {
        var p = conformalMap(0, v);
        var px = cx2 + p.x * scale;
        var py = cy + p.y * scale;
        if (v === -1.2) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Info text
      ctx.fillStyle = '#f8fafc';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Weyl Conformal Invariance: cos(θ) = g_ij uⁱ vʲ / (||u|| ||v||) is strictly invariant!', 140, 395);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 8. UNIT 8: Spacetime Curvature & Schwarzschild Geodesic Simulator
  // =========================================================================
  window.TensorSims.sim_tensor_einstein_field = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      mass: 1.0,
      relativity: 1.0, // 0 = Newtonian, 1 = Full Relativistic Schwarzschild
      r: 120,
      phi: 0,
      vr: 0,
      vphi: 1.6,
      trail: []
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Central Mass M:
          <input type="range" id="${canvasId}-mass" min="0.5" max="2.5" step="0.1" value="1.0" style="width:70px;">
        </label>
        <label style="color:#94a3b8; font-size:0.85rem;">Precession Boost:
          <input type="range" id="${canvasId}-rel" min="0" max="3" step="0.2" value="1.5" style="width:70px;">
        </label>
        <button id="${canvasId}-btn-reset" style="background:#0284c7; color:#fff; border:none; padding:0.3rem 0.75rem; border-radius:4px; font-size:0.85rem; cursor:pointer;">
          Reset Orbit
        </button>
      `;

      var mIn = document.getElementById(canvasId + '-mass');
      var rIn = document.getElementById(canvasId + '-rel');
      var bReset = document.getElementById(canvasId + '-btn-reset');

      if (mIn) mIn.oninput = function(e) { state.mass = parseFloat(e.target.value); };
      if (rIn) rIn.oninput = function(e) { state.relativity = parseFloat(e.target.value); };
      if (bReset) bReset.onclick = function() {
        state.r = 130;
        state.phi = 0;
        state.vr = 0;
        state.vphi = 1.65;
        state.trail = [];
      };
    }

    function stepOrbit(dt) {
      // Relativistic Binet Equation / Geodesic radial acceleration:
      // d^2 r / dt^2 = - GM/r^2 + L^2/r^3 - (3GM/c^2) (L^2 / r^4)
      var GM = 3000 * state.mass;
      var L = state.r * state.vphi; // specific angular momentum

      // Newtonian term + Relativistic Schwarzschild correction:
      var accelR = -GM / (state.r * state.r) + (L * L) / (state.r * state.r * state.r)
                   - (3 * GM * state.relativity * L * L) / (state.r * state.r * state.r * state.r * 15);

      state.vr += accelR * dt;
      state.r += state.vr * dt;
      state.phi += (L / (state.r * state.r)) * dt;

      // Event horizon collision prevention
      var rs = 18 * state.mass;
      if (state.r < rs) {
        state.r = rs;
        state.vr = -state.vr * 0.5;
      }

      state.trail.push({ r: state.r, phi: state.phi });
      if (state.trail.length > 500) state.trail.shift();
    }

    function render() {
      for (var s = 0; s < 4; s++) stepOrbit(0.015);

      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#060a12';
      ctx.fillRect(0, 0, w, h);

      var cx = w / 2;
      var cy = h / 2;

      // Draw Central Mass (Black Hole / Star)
      var rs = 16 * state.mass;
      // Gravitational Lensing glow
      var grad = ctx.createRadialGradient(cx, cy, rs * 0.5, cx, cy, rs * 3);
      grad.addColorStop(0, 'rgba(251, 191, 36, 0.8)');
      grad.addColorStop(0.5, 'rgba(245, 158, 11, 0.2)');
      grad.addColorStop(1, 'rgba(245, 158, 11, 0)');
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(cx, cy, rs * 3, 0, Math.PI * 2);
      ctx.fill();

      // Event horizon
      ctx.fillStyle = '#000000';
      ctx.beginPath();
      ctx.arc(cx, cy, rs, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Photon Sphere r = 1.5 rs
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.setLineDash([2, 4]);
      ctx.beginPath();
      ctx.arc(cx, cy, rs * 1.5, 0, Math.PI * 2);
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Orbit Trail showing Perihelion Precession (rosette pattern!)
      if (state.trail.length > 1) {
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 1.8;
        ctx.beginPath();
        for (var i = 0; i < state.trail.length; i++) {
          var tr = state.trail[i];
          var px = cx + tr.r * Math.cos(tr.phi);
          var py = cy - tr.r * Math.sin(tr.phi);
          if (i === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Draw Orbiting Body (e.g. Mercury)
      var px = cx + state.r * Math.cos(state.phi);
      var py = cy - state.r * Math.sin(state.phi);
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.arc(px, py, 5, 0, Math.PI * 2);
      ctx.fill();

      // Dashboard
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(15, 15, 340, 130);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(15, 15, 340, 130);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('Einstein Field Equations: G_μν = (8πG/c⁴) T_μν', 25, 35);
      ctx.font = '12px monospace';
      ctx.fillStyle = '#f59e0b';
      ctx.fillText(`Schwarzschild Radius r_s = 2GM/c² = ${rs.toFixed(1)} px`, 25, 58);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`Orbital Radius r(τ) = ${state.r.toFixed(1)} px`, 25, 78);
      ctx.fillStyle = '#34d399';
      ctx.fillText(`Relativistic Shift Δφ = 6πGM / [c² a(1-e²)]`, 25, 98);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Notice the relativistic rosette perihelion advance!', 25, 125);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // Platform Mount Adapter for SimulationEngine (compatible with app.js)
  // =========================================================================
  var SIM_TITLES = {
    sim_tensor_coord_transform: "2D Curvilinear Coordinate Transformations & Basis Vectors Engine",
    sim_tensor_algebra_contraction: "Tensor Products, Symmetrization & Contraction Visualizer",
    sim_tensor_metric_geometry: "Riemannian Metric Tensor g_ij, Ellipsoids & Lightcones",
    sim_tensor_christoffel_geodesic: "Geodesic Trajectories & Tidal Deviation Jacobi Field",
    sim_tensor_covariant_diff: "Covariant Differentiation & Parallel Transport Holonomy Engine",
    sim_tensor_riemann_curvature: "Riemann Curvature Commutator [∇_i, ∇_j] & Sectional Curvature",
    sim_tensor_weyl_conformal: "Conformal Invariance & Weyl Curvature Tensor Visualizer",
    sim_tensor_einstein_field: "Einstein Field Equations, Schwarzschild Spacetime & Perihelion Precession"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.TensorSims || typeof window.TensorSims[simType] !== 'function') {
      console.warn('Simulation type not found in TensorSims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Tensor Analysis Interactive Simulation";
    var canvasId = containerId + '-canvas';
    var controlsId = containerId + '-controls';

    container.innerHTML = `
      <div class="simulation-card" style="margin: 1.5rem 0;">
        <div class="sim-header">
          <div class="sim-title">${title}</div>
          <div class="sim-badge">60 FPS Real-Time Canvas Engine</div>
        </div>
        <div class="canvas-wrapper" style="position: relative; width: 100%; height: 420px; background: #080d19; border-radius: 8px; overflow: hidden;">
          <canvas id="${canvasId}" width="800" height="420" class="sim-canvas" style="width: 100%; height: 100%; display: block;"></canvas>
        </div>
        <div class="sim-controls" id="${controlsId}" style="padding: 0.75rem 1rem; background: #0b1120; border-top: 1px solid #1e293b; display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center;"></div>
      </div>
    `;

    setTimeout(function() {
      window.TensorSims[simType](canvasId, controlsId);
    }, 50);
  };

})();
