# -*- coding: utf-8 -*-
"""
generate_pde_sims.py
Generates partial-differential-equations-sims.js with 8 interactive 60 FPS HTML5 Canvas simulations
Strictly ZERO course numbers.
"""

def generate_sims_js():
    js_code = r'''// Partial Differential Equations Interactive Computational Simulations Engine
// High-performance 60 FPS HTML5 Canvas models registered to window.SIMULATIONS

window.SIMULATIONS = window.SIMULATIONS || {};

// ============================================================================
// 1. Unit 1: Method of Characteristics & Quasilinear Conservation Laws
// ============================================================================
window.SIMULATIONS["sim_pde_lagrange_characteristics"] = {
  title: "Quasilinear Conservation Laws & Characteristic Curves Visualizer",
  description: "Simulate the 1D conservation law u_t + c(u) u_x = 0 (traffic flow & Burgers equation). Observe characteristic curves dx/dt = c(u) in the (x,t) spacetime plane, wave steepening, characteristic crossing (shock wave formation), and expansion/rarefaction fans.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let waveType = "shock"; // "shock", "rarefaction", "gaussian"
    let waveSpeedK = 1.0;
    let animTime = 0.0;
    let isPlaying = true;
    let showSpacetime = true;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Initial Profile:</label>
        <select id="pde-wave-type" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="shock" selected>Compressive Wave (Shock Formation)</option>
          <option value="rarefaction">Rarefaction Fan (Expansion Wave)</option>
          <option value="gaussian">Gaussian Smooth Wave (Wave Steepening)</option>
        </select>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Speed Factor c:</label>
        <input type="range" id="pde-wave-speed" min="0.5" max="2.0" step="0.1" value="1.0" style="vertical-align: middle; width: 80px;">
        <span id="pde-speed-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">1.0</span>
        <button id="btn-pde-play" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Pause</button>
        <button id="btn-pde-reset" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Reset Time</button>
        <button id="btn-pde-toggle-view" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Toggle Spacetime</button>
      `;

      const typeSelect = document.getElementById("pde-wave-type");
      const speedSlider = document.getElementById("pde-wave-speed");
      const speedSpan = document.getElementById("pde-speed-val");
      const btnPlay = document.getElementById("btn-pde-play");
      const btnReset = document.getElementById("btn-pde-reset");
      const btnView = document.getElementById("btn-pde-toggle-view");

      typeSelect.onchange = (e) => {
        waveType = e.target.value;
        animTime = 0.0;
      };

      speedSlider.oninput = (e) => {
        waveSpeedK = parseFloat(e.target.value);
        speedSpan.innerText = waveSpeedK.toFixed(1);
      };

      btnPlay.onclick = () => {
        isPlaying = !isPlaying;
        btnPlay.innerText = isPlaying ? "Pause" : "Play";
      };

      btnReset.onclick = () => {
        animTime = 0.0;
      };

      btnView.onclick = () => {
        showSpacetime = !showSpacetime;
      };
    }

    function u0(x) {
      if (waveType === "shock") {
        return 0.5 * (1.0 - Math.tanh(2.5 * x)) + 0.1;
      } else if (waveType === "rarefaction") {
        return 0.5 * (1.0 + Math.tanh(2.5 * x)) + 0.1;
      } else {
        return Math.exp(-2.0 * x * x) + 0.1;
      }
    }

    let lastTimestamp = performance.now();

    function render(timestamp) {
      const dt = (timestamp - lastTimestamp) / 1000;
      lastTimestamp = timestamp;

      if (isPlaying) {
        animTime += dt * 0.6;
        if (animTime > 2.5) animTime = 0.0;
      }

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      // Split screen: Top is u(x, t) profile, Bottom is (x, t) characteristics
      const splitY = showSpacetime ? H * 0.55 : H - 30;

      // 1. Draw u(x, t) profile
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, W, splitY);

      // Grid for top
      ctx.strokeStyle = "#1e293b";
      ctx.lineWidth = 1;
      ctx.beginPath();
      for (let y = 30; y < splitY; y += 30) {
        ctx.moveTo(30, y); ctx.lineTo(W - 20, y);
      }
      ctx.stroke();

      // Axes for top
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(40, splitY - 15); ctx.lineTo(W - 20, splitY - 15);
      ctx.moveTo(W / 2, 20); ctx.lineTo(W / 2, splitY - 15);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("x (Space)", W - 65, splitY - 20);
      ctx.fillText("u(x, t)", W / 2 + 10, 30);
      ctx.fillText(`Current t = ${animTime.toFixed(2)} s`, 45, 30);

      // Draw initial curve u(x, 0) dashed
      ctx.strokeStyle = "#64748b";
      ctx.setLineDash([4, 4]);
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      const nPts = 120;
      for (let i = 0; i <= nPts; i++) {
        const xPhys = -2.5 + (5.0 * i) / nPts;
        const uVal = u0(xPhys);
        const px = W / 2 + (xPhys / 2.5) * (W * 0.42);
        const py = splitY - 20 - uVal * (splitY - 50);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw current curve u(x, t) via method of characteristics: x(t) = x0 + c(u0)*t
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= nPts; i++) {
        const x0Val = -2.5 + (5.0 * i) / nPts;
        const uVal = u0(x0Val);
        const cVal = waveSpeedK * uVal;
        const xPhys = x0Val + cVal * animTime;
        const px = W / 2 + (xPhys / 2.5) * (W * 0.42);
        const py = splitY - 20 - uVal * (splitY - 50);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("— u(x, t)", 160, 30);
      ctx.fillStyle = "#94a3b8";
      ctx.fillText("--- u(x, 0) Initial", 230, 30);

      // 2. Spacetime Characteristics Diagram
      if (showSpacetime) {
        ctx.fillStyle = "#090d16";
        ctx.fillRect(0, splitY, W, H - splitY);

        ctx.strokeStyle = "#334155";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        // Time axis pointing upward in bottom section
        ctx.moveTo(W / 2, splitY + 10); ctx.lineTo(W / 2, H - 20);
        // Space axis at bottom
        ctx.moveTo(40, H - 25); ctx.lineTo(W - 20, H - 25);
        ctx.stroke();

        ctx.fillStyle = "#94a3b8";
        ctx.fillText("t (Time)", W / 2 + 10, splitY + 25);
        ctx.fillText("x (Space)", W - 65, H - 30);

        // Draw characteristic rays dx/dt = c(u0)
        const nRays = 30;
        for (let i = 0; i <= nRays; i++) {
          const x0Val = -2.2 + (4.4 * i) / nRays;
          const uVal = u0(x0Val);
          const cVal = waveSpeedK * uVal;

          const px0 = W / 2 + (x0Val / 2.5) * (W * 0.42);
          const py0 = H - 25;

          const maxT = 2.5;
          const pxEnd = W / 2 + ((x0Val + cVal * maxT) / 2.5) * (W * 0.42);
          const pyEnd = splitY + 15;

          // Color coded by speed c(u)
          const hue = 200 - Math.min(180, Math.max(0, (uVal - 0.1) * 160));
          ctx.strokeStyle = `hsla(${hue}, 85%, 60%, 0.45)`;
          ctx.lineWidth = 1.2;
          ctx.beginPath();
          ctx.moveTo(px0, py0);
          ctx.lineTo(pxEnd, pyEnd);
          ctx.stroke();

          // Marker at current time animTime
          const pxNow = W / 2 + ((x0Val + cVal * animTime) / 2.5) * (W * 0.42);
          const pyNow = py0 - (animTime / maxT) * (py0 - pyEnd);
          ctx.fillStyle = `hsl(${hue}, 90%, 65%)`;
          ctx.beginPath();
          ctx.arc(pxNow, pyNow, 2.5, 0, Math.PI * 2);
          ctx.fill();
        }

        // Horizontal line for current t
        const currentY = (H - 25) - (animTime / 2.5) * (H - 25 - (splitY + 15));
        ctx.strokeStyle = "rgba(244, 63, 94, 0.7)";
        ctx.lineWidth = 1.5;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(40, currentY); ctx.lineTo(W - 20, currentY);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#f43f5e";
        ctx.fillText(`Current Time Horizon t = ${animTime.toFixed(2)}`, 50, currentY - 5);
      }

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 2. Unit 2: Monge Cones & Characteristic Strips for Non-Linear PDEs
// ============================================================================
window.SIMULATIONS["sim_pde_charpit_monge_cone"] = {
  title: "Non-Linear PDEs: Monge Cones & Characteristic Strips Explorer",
  description: "Examine the contact geometry of non-linear first-order PDEs F(x,y,z,p,q) = 0. Visualizes the Monge cone generated by envelope tangent planes at a point, characteristic direction dx:dy:dz = F_p:F_q:(pF_p+qF_q), and integration of strips (x,y,z,p,q).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let pdeType = "eikonal"; // "eikonal", "paraboloid", "clairaut"
    let angleRot = 0.6;
    let elevation = 0.4;
    let showTangentPlanes = true;
    let isDragging = false;
    let lastMouseX = 0, lastMouseY = 0;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">PDE Geometry:</label>
        <select id="pde-monge-type" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="eikonal" selected>Eikonal / Unit Slope: p² + q² = 1 (Circular Monge Cone)</option>
          <option value="paraboloid">Parabolic Generator: p² + q² = z</option>
          <option value="clairaut">Clairaut Equation: z = px + qy + p² + q² (Envelope Surface)</option>
        </select>
        <button id="btn-toggle-planes" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Toggle Tangent Family</button>
        <button id="btn-reset-view" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Reset 3D View</button>
      `;

      const typeSelect = document.getElementById("pde-monge-type");
      const btnPlanes = document.getElementById("btn-toggle-planes");
      const btnResetView = document.getElementById("btn-reset-view");

      typeSelect.onchange = (e) => {
        pdeType = e.target.value;
      };

      btnPlanes.onclick = () => {
        showTangentPlanes = !showTangentPlanes;
      };

      btnResetView.onclick = () => {
        angleRot = 0.6;
        elevation = 0.4;
      };
    }

    canvas.onmousedown = (e) => {
      isDragging = true;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
    };
    window.addEventListener("mouseup", () => { isDragging = false; });
    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      const dx = e.clientX - lastMouseX;
      const dy = e.clientY - lastMouseY;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
      angleRot += dx * 0.01;
      elevation = Math.max(-1.2, Math.min(1.2, elevation - dy * 0.01));
    });

    function project3D(x, y, z, cx, cy, scale) {
      // Rotation around Z, then tilt by elevation
      const cosA = Math.cos(angleRot), sinA = Math.sin(angleRot);
      const cosE = Math.cos(elevation), sinE = Math.sin(elevation);

      const x1 = x * cosA - y * sinA;
      const y1 = x * sinA + y * cosA;
      const z1 = z;

      const y2 = y1 * cosE - z1 * sinE;
      const z2 = y1 * sinE + z1 * cosE;

      return {
        px: cx + x1 * scale,
        py: cy - z2 * scale,
        depth: y2
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const cx = W / 2;
      const cy = H / 2 + 20;
      const scale = Math.min(W, H) * 0.35;

      // Coordinate axes
      const origin = project3D(0, 0, 0, cx, cy, scale);
      const axX = project3D(1.4, 0, 0, cx, cy, scale);
      const axY = project3D(0, 1.4, 0, cx, cy, scale);
      const axZ = project3D(0, 0, 1.4, cx, cy, scale);

      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1.5;

      // X Axis
      ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(axX.px, axX.py); ctx.stroke();
      ctx.fillStyle = "#ef4444"; ctx.font = "11px Inter, sans-serif"; ctx.fillText("X (F_p)", axX.px + 5, axX.py);

      // Y Axis
      ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(axY.px, axY.py); ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.fillText("Y (F_q)", axY.px + 5, axY.py);

      // Z Axis
      ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(axZ.px, axZ.py); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.fillText("Z (Surface / Strip)", axZ.px + 5, axZ.py - 5);

      // Draw Monge Cone geometry at apex (0, 0, 0)
      const nGenerators = 36;
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 1.2;

      for (let i = 0; i < nGenerators; i++) {
        const theta = (2 * Math.PI * i) / nGenerators;
        let gx, gy, gz;

        if (pdeType === "eikonal") {
          // Monge cone for p^2 + q^2 = 1 is dx^2 + dy^2 = dz^2
          const rad = 0.8;
          gx = rad * Math.cos(theta);
          gy = rad * Math.sin(theta);
          gz = rad;
        } else if (pdeType === "paraboloid") {
          const rad = 0.9;
          gx = rad * Math.cos(theta);
          gy = rad * Math.sin(theta);
          gz = 0.5 * (rad * rad);
        } else {
          // Clairaut singular envelope: z = -0.25 (x^2 + y^2)
          const rad = 0.85;
          gx = rad * Math.cos(theta);
          gy = rad * Math.sin(theta);
          gz = -0.3 * (gx * gx + gy * gy);
        }

        const pTop = project3D(gx, gy, gz, cx, cy, scale);
        ctx.beginPath();
        ctx.moveTo(origin.px, origin.py);
        ctx.lineTo(pTop.px, pTop.py);
        ctx.stroke();

        // Rim ring
        const thetaNext = (2 * Math.PI * (i + 1)) / nGenerators;
        let gxNext = gx, gyNext = gy, gzNext = gz;
        if (pdeType === "eikonal") {
          gxNext = 0.8 * Math.cos(thetaNext); gyNext = 0.8 * Math.sin(thetaNext); gzNext = 0.8;
        } else if (pdeType === "paraboloid") {
          gxNext = 0.9 * Math.cos(thetaNext); gyNext = 0.9 * Math.sin(thetaNext); gzNext = 0.5 * 0.81;
        } else {
          gxNext = 0.85 * Math.cos(thetaNext); gyNext = 0.85 * Math.sin(thetaNext); gzNext = -0.3 * 0.72;
        }
        const pNext = project3D(gxNext, gyNext, gzNext, cx, cy, scale);
        ctx.strokeStyle = "#38bdf8";
        ctx.beginPath(); ctx.moveTo(pTop.px, pTop.py); ctx.lineTo(pNext.px, pNext.py); ctx.stroke();
        ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      }

      // Draw tangent planes enveloping the Monge cone
      if (showTangentPlanes) {
        const nPlanes = 6;
        for (let k = 0; k < nPlanes; k++) {
          const phi = (2 * Math.PI * k) / nPlanes + performance.now() * 0.0003;
          // Normal vector (p, q, -1) with p = cos(phi), q = sin(phi)
          const p = Math.cos(phi), q = Math.sin(phi);
          // Tangent plane passing through origin: p x + q y - z = 0 => z = p x + q y
          // Draw a quadrilateral patch
          const s = 0.6;
          const u_vec = { x: -q * s, y: p * s, z: 0 };
          const v_vec = { x: p * s, y: q * s, z: (p*p + q*q) * s };

          const c1 = project3D(u_vec.x + v_vec.x, u_vec.y + v_vec.y, u_vec.z + v_vec.z, cx, cy, scale);
          const c2 = project3D(-u_vec.x + v_vec.x, -u_vec.y + v_vec.y, -u_vec.z + v_vec.z, cx, cy, scale);
          const c3 = project3D(-u_vec.x - v_vec.x, -u_vec.y - v_vec.y, -u_vec.z - v_vec.z, cx, cy, scale);
          const c4 = project3D(u_vec.x - v_vec.x, u_vec.y - v_vec.y, u_vec.z - v_vec.z, cx, cy, scale);

          ctx.fillStyle = "rgba(168, 85, 247, 0.12)";
          ctx.strokeStyle = "rgba(168, 85, 247, 0.45)";
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(c1.px, c1.py);
          ctx.lineTo(c2.px, c2.py);
          ctx.lineTo(c3.px, c3.py);
          ctx.lineTo(c4.px, c4.py);
          ctx.closePath();
          ctx.fill();
          ctx.stroke();
        }
      }

      // Highlight a single characteristic strip generator
      const genTheta = performance.now() * 0.0008;
      const gX = 0.8 * Math.cos(genTheta);
      const gY = 0.8 * Math.sin(genTheta);
      const gZ = 0.8;
      const stripHead = project3D(gX, gY, gZ, cx, cy, scale);

      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(origin.px, origin.py);
      ctx.lineTo(stripHead.px, stripHead.py);
      ctx.stroke();

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(stripHead.px, stripHead.py, 4, 0, Math.PI * 2);
      ctx.fill();

      // Legend Overlay
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(15, 15, 280, 70);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(15, 15, 280, 70);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Monge Cone: Envelope of Tangent Planes", 25, 32);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText("— Characteristic Direction (F_p, F_q, pF_p+qF_q)", 25, 50);
      ctx.fillStyle = "#a855f7";
      ctx.fillText("■ Tangent Element [p, q, -1] satisfying F=0", 25, 68);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 3. Unit 3: 2nd-Order PDE Canonical Discriminant & Characteristic Curves
// ============================================================================
window.SIMULATIONS["sim_pde_canonical_classifier"] = {
  title: "2nd-Order PDE Canonical Classifier & Characteristic Curves",
  description: "Interactively explore the classification of A u_xx + 2B u_xy + C u_yy = 0 via discriminant Δ = B² - AC. Observe real vs complex characteristic coordinates (ξ, η) and watch the Tricomi equation y u_xx + u_yy = 0 transition continuously across elliptic (y>0), parabolic (y=0), and hyperbolic (y<0) regimes.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let coefA = 1.0;
    let coefB = 0.0;
    let coefC = -1.0;
    let isTricomiMode = false;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Preset / Mode:</label>
        <select id="pde-preset-select" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="wave" selected>Wave Eq: u_xx - u_yy = 0 (Hyperbolic, Δ > 0)</option>
          <option value="heat">Heat Spatial: u_xx = 0 (Parabolic, Δ = 0)</option>
          <option value="laplace">Laplace Eq: u_xx + u_yy = 0 (Elliptic, Δ < 0)</option>
          <option value="tricomi">Tricomi Eq: y u_xx + u_yy = 0 (Mixed Type)</option>
        </select>
        <span id="coef-sliders-group">
          <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">B:</label>
          <input type="range" id="pde-b-slider" min="-2.0" max="2.0" step="0.1" value="0.0" style="vertical-align: middle; width: 75px;">
        </span>
        <span id="pde-discrim-badge" style="display: inline-block; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.8rem; font-weight: 600; margin-left: 0.5rem; background: rgba(56, 189, 248, 0.2); color: #38bdf8;">
          Δ = +1.00 (Hyperbolic)
        </span>
      `;

      const presetSelect = document.getElementById("pde-preset-select");
      const bSlider = document.getElementById("pde-b-slider");
      const badge = document.getElementById("pde-discrim-badge");
      const slidersGroup = document.getElementById("coef-sliders-group");

      function updateBadge() {
        if (isTricomiMode) {
          badge.style.background = "rgba(234, 179, 8, 0.2)";
          badge.style.color = "#eab308";
          badge.innerText = "Tricomi Mixed Type: Elliptic (y>0) | Parabolic (y=0) | Hyperbolic (y<0)";
          slidersGroup.style.display = "none";
          return;
        }
        slidersGroup.style.display = "inline";
        const delta = coefB * coefB - coefA * coefC;
        if (delta > 0.01) {
          badge.style.background = "rgba(56, 189, 248, 0.2)";
          badge.style.color = "#38bdf8";
          badge.innerText = `Δ = ${delta.toFixed(2)} (Hyperbolic: 2 Real Characteristics)`;
        } else if (Math.abs(delta) <= 0.01) {
          badge.style.background = "rgba(234, 179, 8, 0.2)";
          badge.style.color = "#eab308";
          badge.innerText = `Δ = 0.00 (Parabolic: 1 Real Characteristic)`;
        } else {
          badge.style.background = "rgba(168, 85, 247, 0.2)";
          badge.style.color = "#a855f7";
          badge.innerText = `Δ = ${delta.toFixed(2)} (Elliptic: Complex Characteristics)`;
        }
      }

      presetSelect.onchange = (e) => {
        const val = e.target.value;
        if (val === "wave") {
          isTricomiMode = false; coefA = 1.0; coefB = 0.0; coefC = -1.0; bSlider.value = "0.0";
        } else if (val === "heat") {
          isTricomiMode = false; coefA = 1.0; coefB = 0.0; coefC = 0.0; bSlider.value = "0.0";
        } else if (val === "laplace") {
          isTricomiMode = false; coefA = 1.0; coefB = 0.0; coefC = 1.0; bSlider.value = "0.0";
        } else if (val === "tricomi") {
          isTricomiMode = true;
        }
        updateBadge();
      };

      bSlider.oninput = (e) => {
        coefB = parseFloat(e.target.value);
        updateBadge();
      };

      updateBadge();
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const midX = W / 2;
      const midY = H / 2;

      // Coordinate axes (x, y)
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(30, midY); ctx.lineTo(W - 30, midY);
      ctx.moveTo(midX, 20); ctx.lineTo(midX, H - 20);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("x", W - 25, midY - 8);
      ctx.fillText("y", midX + 8, 25);

      if (isTricomiMode) {
        // Tricomi Equation: y u_xx + u_yy = 0
        // Elliptic for y > 0 (shaded purple)
        ctx.fillStyle = "rgba(168, 85, 247, 0.08)";
        ctx.fillRect(30, 20, W - 60, midY - 20);

        // Hyperbolic for y < 0 (shaded cyan)
        ctx.fillStyle = "rgba(56, 189, 248, 0.08)";
        ctx.fillRect(30, midY, W - 60, H - 20 - midY);

        // Parabolic line y = 0
        ctx.strokeStyle = "#eab308";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(30, midY); ctx.lineTo(W - 30, midY);
        ctx.stroke();

        ctx.fillStyle = "#eab308";
        ctx.fillText("Parabolic Transition Line y = 0", midX - 90, midY - 8);

        ctx.fillStyle = "#a855f7";
        ctx.fillText("Elliptic Region (y > 0): No real characteristics", 50, 45);

        ctx.fillStyle = "#38bdf8";
        ctx.fillText("Hyperbolic Region (y < 0): Real characteristics ξ, η = 2/3 (-y)^(3/2) ± x", 50, H - 35);

        // Draw characteristic cusps for y < 0: dy/dx = ± sqrt(-y)
        // Curves: x ± (2/3)(-y)^(3/2) = c  =>  y = - (1.5 * |x - c|)^(2/3)
        const scale = 50;
        ctx.strokeStyle = "rgba(56, 189, 248, 0.6)";
        ctx.lineWidth = 1.5;

        for (let c = -3; c <= 3; c += 1.0) {
          // Plus family
          ctx.beginPath();
          for (let py = 0; py <= 120; py += 3) {
            const yPhys = -py / scale;
            const xPhys1 = c + (2.0 / 3.0) * Math.pow(-yPhys, 1.5);
            const px1 = midX + xPhys1 * scale;
            const py1 = midY + py;
            if (py === 0) ctx.moveTo(px1, py1); else ctx.lineTo(px1, py1);
          }
          ctx.stroke();

          // Minus family
          ctx.beginPath();
          for (let py = 0; py <= 120; py += 3) {
            const yPhys = -py / scale;
            const xPhys2 = c - (2.0 / 3.0) * Math.pow(-yPhys, 1.5);
            const px2 = midX + xPhys2 * scale;
            const py2 = midY + py;
            if (py === 0) ctx.moveTo(px2, py2); else ctx.lineTo(px2, py2);
          }
          ctx.stroke();
        }

      } else {
        // Standard Constant-Coefficient PDE
        const delta = coefB * coefB - coefA * coefC;
        const scale = 50;

        if (delta > 0.01) {
          // Hyperbolic: dy/dx = (B ± sqrt(B^2 - AC)) / A
          const m1 = (coefB + Math.sqrt(delta)) / coefA;
          const m2 = (coefB - Math.sqrt(delta)) / coefA;

          // Family 1
          ctx.strokeStyle = "rgba(56, 189, 248, 0.55)";
          ctx.lineWidth = 1.5;
          for (let c = -200; c <= 200; c += 35) {
            ctx.beginPath();
            ctx.moveTo(30, midY - (m1 * (30 - midX) + c));
            ctx.lineTo(W - 30, midY - (m1 * (W - 30 - midX) + c));
            ctx.stroke();
          }

          // Family 2
          ctx.strokeStyle = "rgba(244, 63, 94, 0.55)";
          for (let c = -200; c <= 200; c += 35) {
            ctx.beginPath();
            ctx.moveTo(30, midY - (m2 * (30 - midX) + c));
            ctx.lineTo(W - 30, midY - (m2 * (W - 30 - midX) + c));
            ctx.stroke();
          }

          ctx.fillStyle = "#38bdf8";
          ctx.fillText(`Characteristic Family 1: Slope m₁ = ${m1.toFixed(2)}`, 45, 40);
          ctx.fillStyle = "#f43f5e";
          ctx.fillText(`Characteristic Family 2: Slope m₂ = ${m2.toFixed(2)}`, 45, 58);

        } else if (Math.abs(delta) <= 0.01) {
          // Parabolic: dy/dx = B / A
          const m = coefB / coefA;
          ctx.strokeStyle = "rgba(234, 179, 8, 0.65)";
          ctx.lineWidth = 1.8;
          for (let c = -200; c <= 200; c += 30) {
            ctx.beginPath();
            ctx.moveTo(30, midY - (m * (30 - midX) + c));
            ctx.lineTo(W - 30, midY - (m * (W - 30 - midX) + c));
            ctx.stroke();
          }
          ctx.fillStyle = "#eab308";
          ctx.fillText(`Single Degenerate Characteristic Family: Slope m = ${m.toFixed(2)}`, 45, 45);

        } else {
          // Elliptic: Complex characteristics -> Conformal Ellipses/Circles in (ξ, η)
          ctx.strokeStyle = "rgba(168, 85, 247, 0.5)";
          ctx.lineWidth = 1.5;
          for (let r = 25; r <= 160; r += 25) {
            ctx.beginPath();
            ctx.ellipse(midX, midY, r, r * 0.75, 0, 0, Math.PI * 2);
            ctx.stroke();
          }
          ctx.fillStyle = "#a855f7";
          ctx.fillText("No Real Characteristics: Complex Conjugate Slopes m = α ± iβ", 45, 45);
          ctx.fillText("Equipotential Conformal Coordinate Contours (ξ, η)", 45, 65);
        }
      }

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 4. Unit 4: 1D Wave Equation D'Alembert & Standing Normal Modes
// ============================================================================
window.SIMULATIONS["sim_pde_wave_dalembert_modes"] = {
  title: "1D Wave Equation: D'Alembert Decomposition & Standing Normal Modes",
  description: "Experience the dynamics of the 1D wave equation u_tt - c² u_xx = 0. Decompose initial pulses into right-traveling f(x - ct) and left-traveling g(x + ct) waves, observe reflections at fixed/free boundaries, and synthesize pure Fourier normal modes.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let modeType = "pulse"; // "pulse", "mode1", "mode2", "mode3"
    let waveC = 1.2;
    let animT = 0.0;
    let isPlaying = true;
    let showComponents = true;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Wave Mode:</label>
        <select id="pde-wave-select" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="pulse" selected>D'Alembert Splitting: Gaussian Pulse</option>
          <option value="mode1">Normal Mode n = 1 (Fundamental Standing Wave)</option>
          <option value="mode2">Normal Mode n = 2 (Second Harmonic with Center Node)</option>
          <option value="mode3">Normal Mode n = 3 (Third Harmonic)</option>
        </select>
        <button id="btn-toggle-comps" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Toggle Right/Left Waves</button>
        <button id="btn-wave-play" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Pause</button>
        <button id="btn-wave-reset" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Reset</button>
      `;

      const sel = document.getElementById("pde-wave-select");
      const btnComps = document.getElementById("btn-toggle-comps");
      const btnPlay = document.getElementById("btn-wave-play");
      const btnReset = document.getElementById("btn-wave-reset");

      sel.onchange = (e) => {
        modeType = e.target.value;
        animT = 0.0;
      };

      btnComps.onclick = () => {
        showComponents = !showComponents;
      };

      btnPlay.onclick = () => {
        isPlaying = !isPlaying;
        btnPlay.innerText = isPlaying ? "Pause" : "Play";
      };

      btnReset.onclick = () => {
        animT = 0.0;
      };
    }

    let lastTime = performance.now();

    function render(timestamp) {
      const dt = (timestamp - lastTime) / 1000;
      lastTime = timestamp;

      if (isPlaying) {
        animT += dt * 0.8;
      }

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const midY = H / 2 + 10;
      const padX = 50;
      const lengthX = W - 2 * padX;

      // Draw string equilibrium line
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padX, midY); ctx.lineTo(W - padX, midY);
      ctx.stroke();

      // Fixed boundary clamp supports
      ctx.fillStyle = "#64748b";
      ctx.fillRect(padX - 8, midY - 30, 8, 60);
      ctx.fillRect(W - padX, midY - 30, 8, 60);

      const nSamples = 150;
      const L = 1.0;

      function pulseProfile(x) {
        return Math.exp(-60.0 * (x - 0.5) * (x - 0.5));
      }

      // Compute displacement u(x, t)
      let uVals = [];
      let rightVals = [];
      let leftVals = [];

      for (let i = 0; i <= nSamples; i++) {
        const xPhys = (i / nSamples) * L;
        let u = 0;
        let rWave = 0, lWave = 0;

        if (modeType === "pulse") {
          // Periodic reflection with Dirichlet fixed ends via odd image lattice
          const ct = waveC * animT;
          // Sum over images
          for (let k = -2; k <= 2; k++) {
            const shiftOdd = 2 * k * L;
            rWave += 0.5 * pulseProfile(xPhys - ct - shiftOdd);
            rWave -= 0.5 * pulseProfile(-xPhys - ct - shiftOdd);
            lWave += 0.5 * pulseProfile(xPhys + ct - shiftOdd);
            lWave -= 0.5 * pulseProfile(-xPhys + ct - shiftOdd);
          }
          u = rWave + lWave;
        } else if (modeType === "mode1") {
          const omega = (Math.PI * waveC) / L;
          u = Math.sin((Math.PI * xPhys) / L) * Math.cos(omega * animT);
          rWave = 0.5 * Math.sin((Math.PI * (xPhys - waveC * animT)) / L);
          lWave = 0.5 * Math.sin((Math.PI * (xPhys + waveC * animT)) / L);
        } else if (modeType === "mode2") {
          const omega = (2 * Math.PI * waveC) / L;
          u = Math.sin((2 * Math.PI * xPhys) / L) * Math.cos(omega * animT);
          rWave = 0.5 * Math.sin((2 * Math.PI * (xPhys - waveC * animT)) / L);
          lWave = 0.5 * Math.sin((2 * Math.PI * (xPhys + waveC * animT)) / L);
        } else if (modeType === "mode3") {
          const omega = (3 * Math.PI * waveC) / L;
          u = Math.sin((3 * Math.PI * xPhys) / L) * Math.cos(omega * animT);
          rWave = 0.5 * Math.sin((3 * Math.PI * (xPhys - waveC * animT)) / L);
          lWave = 0.5 * Math.sin((3 * Math.PI * (xPhys + waveC * animT)) / L);
        }

        uVals.push(u);
        rightVals.push(rWave);
        leftVals.push(lWave);
      }

      const ampScale = 85;

      // Draw forward / backward components if enabled
      if (showComponents && modeType === "pulse") {
        // Right-moving wave (cyan dashed)
        ctx.strokeStyle = "rgba(56, 189, 248, 0.45)";
        ctx.setLineDash([4, 4]);
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        for (let i = 0; i <= nSamples; i++) {
          const px = padX + (i / nSamples) * lengthX;
          const py = midY - rightVals[i] * ampScale;
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Left-moving wave (amber dashed)
        ctx.strokeStyle = "rgba(245, 158, 11, 0.45)";
        ctx.beginPath();
        for (let i = 0; i <= nSamples; i++) {
          const px = padX + (i / nSamples) * lengthX;
          const py = midY - leftVals[i] * ampScale;
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Draw resultant string profile u(x, t)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3.0;
      ctx.beginPath();
      for (let i = 0; i <= nSamples; i++) {
        const px = padX + (i / nSamples) * lengthX;
        const py = midY - uVals[i] * ampScale;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Nodes highlighting (zero displacement points)
      if (modeType === "mode2") {
        ctx.fillStyle = "#f43f5e";
        ctx.beginPath();
        ctx.arc(padX + lengthX * 0.5, midY, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Node (u = 0)", padX + lengthX * 0.5 - 28, midY + 18);
      } else if (modeType === "mode3") {
        ctx.fillStyle = "#f43f5e";
        [1/3, 2/3].forEach(frac => {
          ctx.beginPath();
          ctx.arc(padX + lengthX * frac, midY, 5, 0, Math.PI * 2);
          ctx.fill();
        });
      }

      // HUD & Legend
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`— Resultant Wave u(x, t) | t = ${animT.toFixed(2)} s`, padX, 35);

      if (showComponents && modeType === "pulse") {
        ctx.fillStyle = "rgba(56, 189, 248, 0.7)";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText("--- Right-Traveling Wave 1/2 f(x - ct)", padX, 55);
        ctx.fillStyle = "rgba(245, 158, 11, 0.7)";
        ctx.fillText("--- Left-Traveling Wave 1/2 f(x + ct)", padX + 220, 55);
      }

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 5. Unit 5: Heat Diffusion & Gaussian Fundamental Solution Visualizer
// ============================================================================
window.SIMULATIONS["sim_pde_heat_diffusion_kernel"] = {
  title: "1D Heat Equation: Gaussian Kernel & Boundary Conditions",
  description: "Examine thermal diffusion u_t = α u_xx on a finite rod [0, L]. Observe how sharp thermal gradients smooth out irrevocably in time, toggle between Dirichlet (fixed temperature), Neumann (insulated ends), and Robin boundaries, or simulate an instantaneous point-source Dirac delta delta(x - x_0).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let bcType = "dirichlet"; // "dirichlet", "neumann", "robin"
    let alphaDiff = 0.08;
    let animTime = 0.0;
    let isPlaying = true;
    let initProfile = "step"; // "step", "delta", "gaussian"

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Boundary Condition:</label>
        <select id="pde-heat-bc" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="dirichlet" selected>Dirichlet: Fixed Zero Ends u(0)=u(L)=0</option>
          <option value="neumann">Neumann: Insulated Ends ∂u/∂x=0</option>
          <option value="robin">Robin: Convective Cooling -k ∂u/∂n = h u</option>
        </select>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Diffusivity α:</label>
        <input type="range" id="pde-alpha-slider" min="0.02" max="0.25" step="0.01" value="0.08" style="vertical-align: middle; width: 75px;">
        <span id="pde-alpha-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">0.08</span>
        <button id="btn-heat-profile" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Profile: Step</button>
        <button id="btn-heat-reset" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Reset</button>
      `;

      const bcSelect = document.getElementById("pde-heat-bc");
      const alphaSlider = document.getElementById("pde-alpha-slider");
      const alphaSpan = document.getElementById("pde-alpha-val");
      const btnProf = document.getElementById("btn-heat-profile");
      const btnReset = document.getElementById("btn-heat-reset");

      bcSelect.onchange = (e) => {
        bcType = e.target.value;
        animTime = 0.0;
      };

      alphaSlider.oninput = (e) => {
        alphaDiff = parseFloat(e.target.value);
        alphaSpan.innerText = alphaDiff.toFixed(2);
      };

      btnProf.onclick = () => {
        if (initProfile === "step") initProfile = "delta";
        else if (initProfile === "delta") initProfile = "gaussian";
        else initProfile = "step";
        btnProf.innerText = `Profile: ${initProfile.charAt(0).toUpperCase() + initProfile.slice(1)}`;
        animTime = 0.0;
      };

      btnReset.onclick = () => {
        animTime = 0.0;
      };
    }

    let lastTimestamp = performance.now();

    function render(timestamp) {
      const dt = (timestamp - lastTimestamp) / 1000;
      lastTimestamp = timestamp;

      if (isPlaying) {
        animTime += dt * 0.5;
        if (animTime > 4.0) animTime = 0.0;
      }

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const padX = 50;
      const lengthX = W - 2 * padX;
      const baseY = H - 50;
      const maxH = H - 90;

      // Coordinate axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padX, baseY); ctx.lineTo(W - padX, baseY);
      ctx.moveTo(padX, 30); ctx.lineTo(padX, baseY);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("x = 0", padX - 10, baseY + 18);
      ctx.fillText("x = L", W - padX - 15, baseY + 18);
      ctx.fillText("Temperature u(x, t)", padX + 10, 35);
      ctx.fillText(`Diffusion Time t = ${animTime.toFixed(2)} s`, W - 180, 35);

      const nSamples = 160;
      const L = 1.0;

      // Compute temperature profile u(x, t) via Fourier series expansion
      ctx.strokeStyle = "#f97316";
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      // Pre-evaluate points
      let points = [];
      for (let i = 0; i <= nSamples; i++) {
        const xPhys = (i / nSamples) * L;
        let u = 0;

        if (bcType === "dirichlet") {
          // u(0) = u(L) = 0 => sum b_n sin(n pi x / L) e^(-alpha (n pi / L)^2 t)
          const nTerms = 25;
          for (let n = 1; n <= nTerms; n++) {
            let bn = 0;
            if (initProfile === "step") {
              // f(x) = 1 on [0.25, 0.75]
              bn = (2.0 / (n * Math.PI)) * (Math.cos(n * Math.PI * 0.25) - Math.cos(n * Math.PI * 0.75));
            } else if (initProfile === "delta") {
              // f(x) = delta(x - 0.5)
              bn = 2.0 * Math.sin(n * Math.PI * 0.5);
            } else {
              // Gaussian bump centered at 0.5
              bn = 2.0 * Math.exp(-0.05 * n * n) * Math.sin(n * Math.PI * 0.5);
            }
            const decay = Math.exp(-alphaDiff * Math.pow((n * Math.PI) / L, 2) * animTime);
            u += bn * Math.sin((n * Math.PI * xPhys) / L) * decay;
          }
        } else if (bcType === "neumann") {
          // Insulated => u_x(0) = u_x(L) = 0 => a_0/2 + sum a_n cos(n pi x / L) e^(-alpha (n pi / L)^2 t)
          let a0 = (initProfile === "step") ? 1.0 : 0.6;
          u = a0 * 0.5;
          for (let n = 1; n <= 20; n++) {
            let an = 0;
            if (initProfile === "step") {
              an = (2.0 / (n * Math.PI)) * (Math.sin(n * Math.PI * 0.75) - Math.sin(n * Math.PI * 0.25));
            } else {
              an = 1.5 * Math.exp(-0.06 * n * n) * Math.cos(n * Math.PI * 0.5);
            }
            const decay = Math.exp(-alphaDiff * Math.pow((n * Math.PI) / L, 2) * animTime);
            u += an * Math.cos((n * Math.PI * xPhys) / L) * decay;
          }
        } else {
          // Robin boundary: Newton's cooling
          const nTerms = 15;
          for (let n = 1; n <= nTerms; n++) {
            const lambdaN = (n - 0.5) * Math.PI;
            const decay = Math.exp(-alphaDiff * Math.pow(lambdaN / L, 2) * animTime);
            u += (4.0 / lambdaN) * Math.sin((lambdaN * xPhys) / L) * decay * 0.7;
          }
        }

        const px = padX + (i / nSamples) * lengthX;
        const py = baseY - Math.max(0, Math.min(1.4, u)) * (maxH * 0.7);
        points.push({ px, py, u });

        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Shaded thermal fill
      ctx.lineTo(padX + lengthX, baseY);
      ctx.lineTo(padX, baseY);
      ctx.closePath();
      const grad = ctx.createLinearGradient(0, baseY - maxH, 0, baseY);
      grad.addColorStop(0, "rgba(249, 115, 22, 0.35)");
      grad.addColorStop(1, "rgba(249, 115, 22, 0.02)");
      ctx.fillStyle = grad;
      ctx.fill();

      // Thermal rod heat map bar at bottom
      const barY = baseY + 24;
      const barH = 14;
      ctx.strokeStyle = "#475569";
      ctx.strokeRect(padX, barY, lengthX, barH);

      for (let i = 0; i < nSamples; i++) {
        const uVal = Math.max(0, Math.min(1.0, points[i].u));
        // Cold blue to red gradient
        const r = Math.floor(uVal * 255);
        const b = Math.floor((1 - uVal) * 220);
        ctx.fillStyle = `rgb(${r}, 40, ${b})`;
        const px = padX + (i / nSamples) * lengthX;
        ctx.fillRect(px, barY, lengthX / nSamples + 1, barH);
      }

      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Physical Rod Thermal Density Map", padX, barY + barH + 12);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 6. Unit 6: Laplace & Poisson 2D Harmonic Potential Relaxation Engine
// ============================================================================
window.SIMULATIONS["sim_pde_laplace_harmonic_potential"] = {
  title: "2D Laplace & Poisson Potential Field Relaxation Engine",
  description: "Real-time Jacobi numerical relaxation solving ∇²u = 0 on a 2D domain. Interactively adjust Dirichlet edge potentials (Top, Bottom, Left, Right), observe smooth equipotential contour lines, and click anywhere to verify the Mean Value Property: u(x_0, y_0) = 1/(2π) ∮ u dl.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    const N = 40; // 40x40 grid
    let grid = new Float32Array(N * N);
    let nextGrid = new Float32Array(N * N);

    let vTop = 100.0;
    let vBottom = 0.0;
    let vLeft = 50.0;
    let vRight = 50.0;
    let probeX = N / 2, probeY = N / 2;
    let showContours = true;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Top V:</label>
        <input type="range" id="pde-v-top" min="0" max="100" value="100" style="vertical-align: middle; width: 65px;">
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.4rem;">Bottom V:</label>
        <input type="range" id="pde-v-bot" min="0" max="100" value="0" style="vertical-align: middle; width: 65px;">
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.4rem;">Left V:</label>
        <input type="range" id="pde-v-left" min="0" max="100" value="50" style="vertical-align: middle; width: 65px;">
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.4rem;">Right V:</label>
        <input type="range" id="pde-v-right" min="0" max="100" value="50" style="vertical-align: middle; width: 65px;">
        <button id="btn-toggle-contours" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Contours</button>
      `;

      const sTop = document.getElementById("pde-v-top");
      const sBot = document.getElementById("pde-v-bot");
      const sLeft = document.getElementById("pde-v-left");
      const sRight = document.getElementById("pde-v-right");
      const btnCont = document.getElementById("btn-toggle-contours");

      sTop.oninput = (e) => { vTop = parseFloat(e.target.value); applyBC(); };
      sBot.oninput = (e) => { vBottom = parseFloat(e.target.value); applyBC(); };
      sLeft.oninput = (e) => { vLeft = parseFloat(e.target.value); applyBC(); };
      sRight.oninput = (e) => { vRight = parseFloat(e.target.value); applyBC(); };
      btnCont.onclick = () => { showContours = !showContours; };
    }

    function applyBC() {
      for (let i = 0; i < N; i++) {
        grid[0 * N + i] = vTop; // row 0
        grid[(N - 1) * N + i] = vBottom; // row N-1
        grid[i * N + 0] = vLeft; // col 0
        grid[i * N + (N - 1)] = vRight; // col N-1
      }
    }

    applyBC();

    // Initialize interior with linear interpolation
    for (let r = 1; r < N - 1; r++) {
      for (let c = 1; c < N - 1; c++) {
        const fy = r / (N - 1);
        const fx = c / (N - 1);
        grid[r * N + c] = (1 - fy) * vTop + fy * vBottom;
      }
    }

    canvas.onmousedown = (e) => {
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;
      const pad = 40;
      const fieldSize = Math.min(canvas.width - 2 * pad, canvas.height - 2 * pad);
      const c = Math.floor(((mx - pad) / fieldSize) * N);
      const r = Math.floor(((my - pad) / fieldSize) * N);
      if (r >= 2 && r < N - 2 && c >= 2 && c < N - 2) {
        probeX = c; probeY = r;
      }
    };

    function stepJacobi(iterations) {
      applyBC();
      for (let it = 0; it < iterations; it++) {
        for (let r = 1; r < N - 1; r++) {
          for (let c = 1; c < N - 1; c++) {
            nextGrid[r * N + c] = 0.25 * (
              grid[(r - 1) * N + c] +
              grid[(r + 1) * N + c] +
              grid[r * N + (c - 1)] +
              grid[r * N + (c + 1)]
            );
          }
        }
        for (let i = 0; i < N * N; i++) grid[i] = nextGrid[i];
        applyBC();
      }
    }

    function render() {
      stepJacobi(5);

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const pad = 40;
      const fieldSize = Math.min(W - 2 * pad, H - 2 * pad);
      const cellW = fieldSize / N;
      const cellH = fieldSize / N;

      // Render Heatmap cells
      for (let r = 0; r < N; r++) {
        for (let c = 0; c < N; c++) {
          const val = Math.max(0, Math.min(100, grid[r * N + c]));
          // Hue from blue (220) to red (0)
          const hue = 220 - (val / 100) * 220;
          ctx.fillStyle = `hsl(${hue}, 85%, 45%)`;
          ctx.fillRect(pad + c * cellW, pad + r * cellH, cellW + 0.5, cellH + 0.5);
        }
      }

      // Outer border
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 2;
      ctx.strokeRect(pad, pad, fieldSize, fieldSize);

      // Mean Value Property Probe at (probeX, probeY)
      const probePx = pad + (probeX + 0.5) * cellW;
      const probePy = pad + (probeY + 0.5) * cellH;
      const probeR = cellW * 4.5;

      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 1.8;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.arc(probePx, probePy, probeR, 0, Math.PI * 2);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#ffffff";
      ctx.beginPath();
      ctx.arc(probePx, probePy, 3.5, 0, Math.PI * 2);
      ctx.fill();

      // Sample boundary of circle
      let sumCirc = 0;
      const nSampleCirc = 24;
      for (let k = 0; k < nSampleCirc; k++) {
        const th = (2 * Math.PI * k) / nSampleCirc;
        const sx = probeX + 4.5 * Math.cos(th);
        const sy = probeY + 4.5 * Math.sin(th);
        const ir = Math.round(sy), ic = Math.round(sx);
        if (ir >= 0 && ir < N && ic >= 0 && ic < N) {
          sumCirc += grid[ir * N + ic];
        }
      }
      const meanCirc = sumCirc / nSampleCirc;
      const centerVal = grid[probeY * N + probeX];

      // Overlay MVP Stats
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(W - 250, 15, 235, 75);
      ctx.strokeStyle = "#38bdf8";
      ctx.strokeRect(W - 250, 15, 235, 75);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Mean Value Property Verification:", W - 240, 32);
      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`u(x₀, y₀) Center: ${centerVal.toFixed(2)} V`, W - 240, 50);
      ctx.fillStyle = "#a3e635";
      ctx.fillText(`1/(2π) ∮ u ds Circle: ${meanCirc.toFixed(2)} V`, W - 240, 68);
      ctx.fillStyle = "#94a3b8";
      ctx.fillText(`(Click domain to reposition probe)`, pad, H - 15);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 7. Unit 7: Circular Drumhead Vibrations & Bessel Mode (m, n) Synthesizer
// ============================================================================
window.SIMULATIONS["sim_pde_cylindrical_drumhead_bessel"] = {
  title: "Vibrating Circular Drumhead & Bessel Modes (m, n)",
  description: "Visualize the eigenfunctions of the 2D Laplacian on a circular membrane of radius R: u(r, θ, t) = J_m(α_{m,n} r / R) cos(m θ) cos(ω_{m,n} t). Observe nodal circles (zeros of J_m) and nodal diameters (zeros of cos(m θ)) under continuous 60 FPS real-time oscillation.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let modeM = 1; // Azimuthal: 0, 1, 2, 3
    let modeN = 2; // Radial zero index: 1, 2, 3
    let animT = 0.0;
    let isPlaying = true;
    let show3DWireframe = false;

    // Approximate roots alpha_{m,n} of Bessel function J_m(x) = 0
    const besselZeros = {
      0: [2.4048, 5.5201, 8.6537],
      1: [3.8317, 7.0156, 10.1735],
      2: [5.1356, 8.4172, 11.6198],
      3: [6.3802, 9.7610, 13.0152]
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Azimuthal Mode m:</label>
        <select id="pde-mode-m" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="0">m = 0 (Axisymmetric)</option>
          <option value="1" selected>m = 1 (1 Nodal Diameter)</option>
          <option value="2">m = 2 (2 Nodal Diameters)</option>
          <option value="3">m = 3 (3 Nodal Diameters)</option>
        </select>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Radial Mode n:</label>
        <select id="pde-mode-n" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="1">n = 1 (Fundamental Rim Boundary)</option>
          <option value="2" selected>n = 2 (1 Internal Nodal Circle)</option>
          <option value="3">n = 3 (2 Internal Nodal Circles)</option>
        </select>
        <button id="btn-toggle-3d" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Toggle 3D Grid</button>
        <button id="btn-drum-play" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Pause</button>
      `;

      const selM = document.getElementById("pde-mode-m");
      const selN = document.getElementById("pde-mode-n");
      const btn3D = document.getElementById("btn-toggle-3d");
      const btnPlay = document.getElementById("btn-drum-play");

      selM.onchange = (e) => { modeM = parseInt(e.target.value); };
      selN.onchange = (e) => { modeN = parseInt(e.target.value); };
      btn3D.onclick = () => { show3DWireframe = !show3DWireframe; };
      btnPlay.onclick = () => {
        isPlaying = !isPlaying;
        btnPlay.innerText = isPlaying ? "Pause" : "Play";
      };
    }

    // High accuracy Bessel J_m approximation via polynomial expansion & series
    function besselJ(m, x) {
      if (x < 0) return (m % 2 === 0 ? 1 : -1) * besselJ(m, -x);
      // Direct series summation
      let sum = 0;
      let term = Math.pow(x / 2, m);
      // Factorial m!
      let mFact = 1;
      for (let i = 1; i <= m; i++) mFact *= i;
      term /= mFact;

      for (let k = 0; k < 14; k++) {
        sum += term;
        term *= - (x * x) / (4.0 * (k + 1) * (k + 1 + m));
      }
      return sum;
    }

    let lastTimestamp = performance.now();

    function render(timestamp) {
      const dt = (timestamp - lastTimestamp) / 1000;
      lastTimestamp = timestamp;

      const alphaRoot = besselZeros[modeM][modeN - 1];
      const omega = alphaRoot * 1.5;

      if (isPlaying) {
        animT += dt * omega * 0.45;
      }

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const cx = W / 2;
      const cy = H / 2;
      const R = Math.min(W, H) * 0.4;

      const timeFactor = Math.cos(animT);

      if (!show3DWireframe) {
        // 2D Density Disk View
        const numR = 40;
        const numTh = 60;

        for (let ir = 0; ir < numR; ir++) {
          const r1 = (ir / numR) * R;
          const r2 = ((ir + 1) / numR) * R;
          const rMid = (r1 + r2) / 2;
          const normR = rMid / R;

          const Jval = besselJ(modeM, normR * alphaRoot);

          for (let ith = 0; ith < numTh; ith++) {
            const th1 = (2 * Math.PI * ith) / numTh;
            const th2 = (2 * Math.PI * (ith + 1)) / numTh;
            const thMid = (th1 + th2) / 2;

            const uVal = Jval * Math.cos(modeM * thMid) * timeFactor;
            // Map displacement to color: Blue negative, Red positive
            const hue = uVal > 0 ? 10 : 210;
            const sat = Math.min(100, Math.abs(uVal) * 180);
            const light = 20 + Math.min(60, Math.abs(uVal) * 90);

            ctx.fillStyle = `hsl(${hue}, ${sat}%, ${light}%)`;

            ctx.beginPath();
            ctx.arc(cx, cy, r2, th1, th2);
            ctx.arc(cx, cy, r1, th2, th1, true);
            ctx.closePath();
            ctx.fill();
          }
        }

        // Rim border
        ctx.strokeStyle = "#94a3b8";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(cx, cy, R, 0, Math.PI * 2);
        ctx.stroke();

        // Draw Nodal Diameters (where cos(m θ) = 0 => θ = (k + 1/2) π / m)
        if (modeM > 0) {
          ctx.strokeStyle = "#ffffff";
          ctx.lineWidth = 1.8;
          ctx.setLineDash([4, 4]);
          for (let k = 0; k < modeM; k++) {
            const angle = (Math.PI * (k + 0.5)) / modeM;
            ctx.beginPath();
            ctx.moveTo(cx - R * Math.cos(angle), cy - R * Math.sin(angle));
            ctx.lineTo(cx + R * Math.cos(angle), cy + R * Math.sin(angle));
            ctx.stroke();
          }
          ctx.setLineDash([]);
        }

        // Draw Internal Nodal Circles (where J_m(alpha * r / R) = 0)
        for (let k = 0; k < modeN - 1; k++) {
          const rootK = besselZeros[modeM][k];
          const nodalR = (rootK / alphaRoot) * R;
          ctx.strokeStyle = "#ffffff";
          ctx.lineWidth = 1.8;
          ctx.setLineDash([4, 4]);
          ctx.beginPath();
          ctx.arc(cx, cy, nodalR, 0, Math.PI * 2);
          ctx.stroke();
          ctx.setLineDash([]);
        }

      } else {
        // 3D Isometric Mesh View
        const nRings = 24;
        const nRays = 36;
        const tilt = 0.5;

        ctx.strokeStyle = "rgba(56, 189, 248, 0.6)";
        ctx.lineWidth = 1.2;

        for (let ir = 0; ir <= nRings; ir++) {
          const normR = ir / nRings;
          const rPhys = normR * R;
          const Jval = besselJ(modeM, normR * alphaRoot);

          ctx.beginPath();
          for (let ith = 0; ith <= nRays; ith++) {
            const th = (2 * Math.PI * ith) / nRays;
            const uVal = Jval * Math.cos(modeM * th) * timeFactor;
            const zDisp = uVal * 55;

            const px = cx + rPhys * Math.cos(th);
            const py = cy + (rPhys * Math.sin(th)) * tilt - zDisp;

            if (ith === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
          }
          ctx.stroke();
        }
      }

      // Mode Badge & Information
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(20, 20, 260, 65);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(20, 20, 260, 65);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Mode (${modeM}, ${modeN}): J_${modeM}(α_{${modeM},${modeN}} r / R) cos(${modeM}θ)`, 30, 38);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Zero α_{${modeM},${modeN}} = ${alphaRoot.toFixed(4)} | Nodal Circles: ${modeN - 1}`, 30, 56);
      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`Nodal Diameters: ${modeM} (White Dashed Lines)`, 30, 72);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 8. Unit 8: Green's Function & Method of Images Field Visualizer
// ============================================================================
window.SIMULATIONS["sim_pde_greens_function_images"] = {
  title: "Green's Functions & Method of Images Field Visualizer",
  description: "Explore Green's function G(x, y) = G_0(x, y) + Φ^x(y) for Poisson's equation ∇²u = -δ(x - x_0) with homogeneous Dirichlet boundary conditions. Drag the point charge and see the mirror image charge cancel the potential on the boundary in real-time.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let geomType = "halfplane"; // "halfplane", "corner", "sphere"
    let srcX = 140, srcY = 160;
    let isDragging = false;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Conducting Geometry:</label>
        <select id="pde-green-geom" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="halfplane" selected>Upper Half-Space y ≥ 0 (Single Image)</option>
          <option value="corner">Conducting 90° Corner (3 Orthogonal Images)</option>
          <option value="sphere">Grounded Conducting Sphere (Kelvin Inversion)</option>
        </select>
        <button id="btn-reset-charge" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Center Source</button>
      `;

      const sel = document.getElementById("pde-green-geom");
      const btnReset = document.getElementById("btn-reset-charge");

      sel.onchange = (e) => {
        geomType = e.target.value;
        if (geomType === "sphere") {
          srcX = canvas.width / 2 + 100;
          srcY = canvas.height / 2;
        } else {
          srcX = canvas.width / 2;
          srcY = canvas.height / 2 - 60;
        }
      };

      btnReset.onclick = () => {
        srcX = canvas.width / 2;
        srcY = canvas.height / 2 - 60;
      };
    }

    canvas.onmousedown = (e) => {
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;
      const dist = Math.hypot(mx - srcX, my - srcY);
      if (dist < 25) isDragging = true;
    };
    window.addEventListener("mouseup", () => { isDragging = false; });
    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      const rect = canvas.getBoundingClientRect();
      srcX = Math.max(30, Math.min(canvas.width - 30, e.clientX - rect.left));
      srcY = Math.max(30, Math.min(canvas.height - 30, e.clientY - rect.top));
    });

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const midX = W / 2;
      const midY = H / 2;

      let charges = []; // { x, y, q, isImage: bool }

      if (geomType === "halfplane") {
        // Ground plane at y = midY
        // Constrain source to y < midY
        if (srcY > midY - 10) srcY = midY - 10;
        charges.push({ x: srcX, y: srcY, q: +1.0, isImage: false });
        // Image charge reflected across y = midY
        const imgY = midY + (midY - srcY);
        charges.push({ x: srcX, y: imgY, q: -1.0, isImage: true });

        // Draw Grounded Boundary
        ctx.fillStyle = "#1e293b";
        ctx.fillRect(0, midY, W, H - midY);

        ctx.strokeStyle = "#10b981";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(0, midY); ctx.lineTo(W, midY);
        ctx.stroke();

        ctx.fillStyle = "#10b981";
        ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText("Grounded Boundary: G(x, y; x₀, y₀) ≡ 0 on y = 0", 25, midY + 20);

      } else if (geomType === "corner") {
        // Ground corner at x >= midX and y <= midY
        if (srcX < midX + 10) srcX = midX + 10;
        if (srcY > midY - 10) srcY = midY - 10;

        charges.push({ x: srcX, y: srcY, q: +1.0, isImage: false });
        // Image 1: reflected across x = midX
        charges.push({ x: midX - (srcX - midX), y: srcY, q: -1.0, isImage: true });
        // Image 2: reflected across y = midY
        charges.push({ x: srcX, y: midY + (midY - srcY), q: -1.0, isImage: true });
        // Image 3: reflected across origin
        charges.push({ x: midX - (srcX - midX), y: midY + (midY - srcY), q: +1.0, isImage: true });

        // Draw Grounded Corner
        ctx.fillStyle = "#1e293b";
        ctx.fillRect(0, 0, midX, H);
        ctx.fillRect(midX, midY, W - midX, H - midY);

        ctx.strokeStyle = "#10b981";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(midX, 0); ctx.lineTo(midX, midY); ctx.lineTo(W, midY);
        ctx.stroke();

        ctx.fillStyle = "#10b981";
        ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText("90° Grounded Conducting Corner (3 Image Charges)", midX + 20, midY + 25);

      } else {
        // Grounded Sphere of radius R0 at (midX, midY)
        const R0 = 90;
        const dx = srcX - midX;
        const dy = srcY - midY;
        const d = Math.hypot(dx, dy);

        // Keep source outside sphere
        if (d < R0 + 15) {
          srcX = midX + (dx / d) * (R0 + 15);
          srcY = midY + (dy / d) * (R0 + 15);
        }

        const dNow = Math.hypot(srcX - midX, srcY - midY);
        charges.push({ x: srcX, y: srcY, q: +1.0, isImage: false });

        // Kelvin inversion: image position d' = R0^2 / d, image charge q' = -q (R0 / d)
        const dImg = (R0 * R0) / dNow;
        const qImg = - (R0 / dNow);
        const imgX = midX + (dx / dNow) * dImg;
        const imgY = midY + (dy / dNow) * dImg;
        charges.push({ x: imgX, y: imgY, q: qImg, isImage: true });

        // Draw Grounded Sphere
        ctx.fillStyle = "#1e293b";
        ctx.beginPath();
        ctx.arc(midX, midY, R0, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = "#10b981";
        ctx.lineWidth = 3;
        ctx.stroke();

        ctx.fillStyle = "#10b981";
        ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText("Grounded Sphere (Kelvin Inversion r' = R²/d)", midX - 95, midY + R0 + 22);
      }

      // Draw Equipotential Field Contours via fast sampling
      const step = 14;
      for (let px = 20; px < W - 20; px += step) {
        for (let py = 20; py < H - 20; py += step) {
          // Calculate potential G = sum q_i ln(r_i) or 1/r_i in 2D: G = - 1/(2pi) sum q_i ln(r_i)
          let pot = 0;
          for (let ch of charges) {
            const r = Math.hypot(px - ch.x, py - ch.y) + 4.0;
            pot += - 15.0 * ch.q * Math.log(r);
          }

          if (Math.abs(pot % 20) < 3.5) {
            ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
            ctx.fillRect(px, py, 2.5, 2.5);
          }
        }
      }

      // Draw Charges
      for (let ch of charges) {
        ctx.fillStyle = ch.q > 0 ? "#ef4444" : "#3b82f6";
        ctx.beginPath();
        ctx.arc(ch.x, ch.y, ch.isImage ? 7 : 10, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = ch.isImage ? "#ffffff" : "#fef08a";
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 10px Inter, sans-serif";
        const label = ch.isImage ? `-${Math.abs(ch.q).toFixed(2)}` : "+1.0";
        ctx.fillText(label, ch.x - 12, ch.y - 12);
      }

      // Drag instruction
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Drag Source Charge (+1.0) with mouse", 25, 30);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// Simulation Engine Mount Utility
window.SimulationEngine = window.SimulationEngine || {
  initSimulation: function(containerId, simType) {
    const container = document.getElementById(containerId);
    if (!container) return;
    const simDef = window.SIMULATIONS[simType];
    if (!simDef) {
      console.warn("Simulation type not found:", simType);
      return;
    }

    const canvasId = `${containerId}-canvas`;
    const controlsId = `${containerId}-controls`;

    container.innerHTML = `
      <div class="simulation-card" style="margin: 1.5rem 0;">
        <div class="sim-header">
          <div class="sim-title">${simDef.title}</div>
          <div class="sim-badge">60 FPS Real-Time Canvas Engine</div>
        </div>
        <div class="canvas-wrapper" style="position: relative; width: 100%; height: 380px; background: #0f172a; border-radius: 8px; overflow: hidden;">
          <canvas id="${canvasId}" width="800" height="380" class="sim-canvas" style="width: 100%; height: 100%; display: block;"></canvas>
        </div>
        <div class="sim-controls" id="${controlsId}" style="padding: 1rem; background: #1e293b; border-radius: 0 0 8px 8px; display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center;"></div>
      </div>
    `;

    setTimeout(() => {
      simDef.init(canvasId, controlsId);
    }, 50);
  }
};
'''
    with open("partial-differential-equations-sims.js", "w", encoding="utf-8") as f:
        f.write(js_code)
    print("partial-differential-equations-sims.js written successfully.")

if __name__ == "__main__":
    generate_sims_js()
