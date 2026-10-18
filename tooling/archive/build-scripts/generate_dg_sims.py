# -*- coding: utf-8 -*-
"""
generate_dg_sims.py
Generates differential-geometry-sims.js containing 8 real-time 60 FPS Canvas simulations
for all 8 units of the Differential Geometry master textbook.
Registered cleanly with window.SIMULATIONS and window.SimulationEngine.
"""

def generate_sims():
    js_code = r'''// Differential Geometry Interactive Simulation Suite (60 FPS Canvas)
// Integrated with OpenSTEM Simulation Engine & Textbook Controllers

window.SIMULATIONS = window.SIMULATIONS || {};
window.SimulationEngine = window.SimulationEngine || {};

// 1. Unit 1: Space Curve Parametrization, Tangent Vector & Osculating Plane Explorer
window.SIMULATIONS["sim_dg_space_curve_tangent"] = {
  title: "Space Curve Parametrization, Tangent Vector & Osculating Plane",
  description: "Examine smooth space curves in 3D Euclidean space: interactively adjust curve parameters, move along the curve to trace the velocity vector r'(t), normalized unit tangent T(t), and the osculating plane.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let tVal = 0.5;
    let curveType = "twisted_cubic"; // "twisted_cubic", "circular_helix", "trefoil"
    let rotX = 0.45;
    let rotY = 0.65;
    let isDragging = false;
    let lastMouseX = 0;
    let lastMouseY = 0;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Curve:</label>
        <button id="dg-btn-cubic" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Twisted Cubic</button>
        <button id="dg-btn-helix" style="padding: 0.35rem 0.75rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Circular Helix</button>
        <button id="dg-btn-trefoil" style="padding: 0.35rem 0.75rem; background: #8b5cf6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Trefoil Knot</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Parameter t:</label>
        <input type="range" id="dg-slider-t" min="0" max="1" step="0.01" value="0.5" style="vertical-align: middle; width: 110px;">
        <span id="dg-t-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">t = 0.50</span>
      `;

      document.getElementById("dg-btn-cubic").onclick = () => { curveType = "twisted_cubic"; render(); };
      document.getElementById("dg-btn-helix").onclick = () => { curveType = "circular_helix"; render(); };
      document.getElementById("dg-btn-trefoil").onclick = () => { curveType = "trefoil"; render(); };

      const tSlider = document.getElementById("dg-slider-t");
      tSlider.oninput = (e) => {
        tVal = parseFloat(e.target.value);
        document.getElementById("dg-t-val").innerText = `t = ${tVal.toFixed(2)}`;
        render();
      };
    }

    // Mouse drag for 3D rotation
    canvas.onmousedown = (e) => {
      isDragging = true;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
    };
    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      let dx = e.clientX - lastMouseX;
      let dy = e.clientY - lastMouseY;
      rotY += dx * 0.008;
      rotX += dy * 0.008;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
      render();
    });
    window.addEventListener("mouseup", () => { isDragging = false; });

    function getCurvePoint(t) {
      if (curveType === "twisted_cubic") {
        // t mapped from [-1.2, 1.2]
        let p = (t - 0.5) * 2.4;
        return {
          pos: [p * 0.9, (p * p - 0.8) * 0.7, (p * p * p) * 0.4],
          vel: [0.9, 1.4 * p, 1.2 * p * p],
          acc: [0, 1.4, 2.4 * p]
        };
      } else if (curveType === "circular_helix") {
        let p = t * Math.PI * 4;
        return {
          pos: [Math.cos(p) * 1.0, (t - 0.5) * 2.0, Math.sin(p) * 1.0],
          vel: [-Math.sin(p) * 4 * Math.PI, 2.0, Math.cos(p) * 4 * Math.PI],
          acc: [-Math.cos(p) * 16 * Math.PI * Math.PI, 0, -Math.sin(p) * 16 * Math.PI * Math.PI]
        };
      } else {
        // Trefoil knot
        let p = t * Math.PI * 2;
        let r = Math.sin(p) + 2 * Math.sin(2 * p);
        let z = Math.cos(p) - 2 * Math.cos(2 * p);
        let y = -Math.sin(3 * p);
        let dr = Math.cos(p) + 4 * Math.cos(2 * p);
        let dz = -Math.sin(p) + 4 * Math.sin(2 * p);
        let dy = -3 * Math.cos(3 * p);
        return {
          pos: [r * 0.45, y * 0.45, z * 0.45],
          vel: [dr * 0.45, dy * 0.45, dz * 0.45],
          acc: [(-Math.sin(p) - 8 * Math.sin(2 * p)) * 0.45, (9 * Math.sin(3 * p)) * 0.45, (-Math.cos(p) + 8 * Math.cos(2 * p)) * 0.45]
        };
      }
    }

    function project3D(v, cx, cy, scale) {
      // Rotate Y then X
      let x1 = v[0] * Math.cos(rotY) + v[2] * Math.sin(rotY);
      let z1 = -v[0] * Math.sin(rotY) + v[2] * Math.cos(rotY);
      let y1 = v[1] * Math.cos(rotX) - z1 * Math.sin(rotX);
      let z2 = v[1] * Math.sin(rotX) + z1 * Math.cos(rotX);
      let fov = 3.5 / (3.5 + z2);
      return [cx + x1 * scale * fov, cy - y1 * scale * fov];
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;
      const cx = W / 2, cy = H / 2;
      const scale = 130;

      // Coordinate axes
      const origin2D = project3D([0, 0, 0], cx, cy, scale);
      const axes = [
        { v: [1.3, 0, 0], col: "#ef4444", label: "X" },
        { v: [0, 1.3, 0], col: "#10b981", label: "Y" },
        { v: [0, 0, 1.3], col: "#3b82f6", label: "Z" }
      ];
      axes.forEach(ax => {
        let p2 = project3D(ax.v, cx, cy, scale);
        ctx.strokeStyle = ax.col;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(origin2D[0], origin2D[1]);
        ctx.lineTo(p2[0], p2[1]);
        ctx.stroke();
        ctx.fillStyle = ax.col;
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText(ax.label, p2[0] + 4, p2[1] - 4);
      });

      // Draw the Space Curve
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const numSteps = 140;
      for (let i = 0; i <= numSteps; i++) {
        let s = i / numSteps;
        let pt = getCurvePoint(s);
        let p2 = project3D(pt.pos, cx, cy, scale);
        if (i === 0) ctx.moveTo(p2[0], p2[1]);
        else ctx.lineTo(p2[0], p2[1]);
      }
      ctx.stroke();

      // Current point
      let current = getCurvePoint(tVal);
      let cur2D = project3D(current.pos, cx, cy, scale);

      // Tangent vector T = r' / ||r'||
      let vx = current.vel[0], vy = current.vel[1], vz = current.vel[2];
      let vNorm = Math.sqrt(vx * vx + vy * vy + vz * vz) || 1e-6;
      let tx = vx / vNorm, ty = vy / vNorm, tz = vz / vNorm;

      // Binormal vector direction r' x r''
      let ax = current.acc[0], ay = current.acc[1], az = current.acc[2];
      let bx = vy * az - vz * ay;
      let by = vz * ax - vx * az;
      let bz = vx * ay - vy * ax;
      let bNorm = Math.sqrt(bx * bx + by * by + bz * bz) || 1e-6;
      bx /= bNorm; by /= bNorm; bz /= bNorm;

      // Principal normal N = B x T
      let nx = by * tz - bz * ty;
      let ny = bz * tx - bx * tz;
      let nz = bx * ty - by * tx;

      // Draw Osculating Plane polygon (span of T and N at r(t))
      let planeSize = 0.55;
      let pA = [current.pos[0] - tx * planeSize - nx * planeSize, current.pos[1] - ty * planeSize - ny * planeSize, current.pos[2] - tz * planeSize - nz * planeSize];
      let pB = [current.pos[0] + tx * planeSize - nx * planeSize, current.pos[1] + ty * planeSize - ny * planeSize, current.pos[2] + tz * planeSize - nz * planeSize];
      let pC = [current.pos[0] + tx * planeSize + nx * planeSize, current.pos[1] + ty * planeSize + ny * planeSize, current.pos[2] + tz * planeSize + nz * planeSize];
      let pD = [current.pos[0] - tx * planeSize + nx * planeSize, current.pos[1] - ty * planeSize + ny * planeSize, current.pos[2] - tz * planeSize + nz * planeSize];

      let pA2 = project3D(pA, cx, cy, scale);
      let pB2 = project3D(pB, cx, cy, scale);
      let pC2 = project3D(pC, cx, cy, scale);
      let pD2 = project3D(pD, cx, cy, scale);

      ctx.fillStyle = "rgba(234, 179, 8, 0.22)";
      ctx.beginPath();
      ctx.moveTo(pA2[0], pA2[1]);
      ctx.lineTo(pB2[0], pB2[1]);
      ctx.lineTo(pC2[0], pC2[1]);
      ctx.lineTo(pD2[0], pD2[1]);
      ctx.closePath();
      ctx.fill();
      ctx.strokeStyle = "#eab308";
      ctx.lineWidth = 1;
      ctx.stroke();

      // Tangent vector arrow
      let tTip = [current.pos[0] + tx * 0.7, current.pos[1] + ty * 0.7, current.pos[2] + tz * 0.7];
      let tTip2D = project3D(tTip, cx, cy, scale);
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(cur2D[0], cur2D[1]);
      ctx.lineTo(tTip2D[0], tTip2D[1]);
      ctx.stroke();

      // Point marker
      ctx.fillStyle = "#fff";
      ctx.beginPath();
      ctx.arc(cur2D[0], cur2D[1], 5, 0, Math.PI * 2);
      ctx.fill();

      // Labels & HUD
      ctx.fillStyle = "#f43f5e";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Unit Tangent T(t)", tTip2D[0] + 6, tTip2D[1]);

      ctx.fillStyle = "#eab308";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Osculating Plane (Span{T, N})", pC2[0] + 5, pC2[1] - 5);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, monospace";
      ctx.fillText(`r(t) = (${current.pos[0].toFixed(2)}, ${current.pos[1].toFixed(2)}, ${current.pos[2].toFixed(2)})`, 15, 25);
      ctx.fillText(`||r'(t)|| = ${vNorm.toFixed(3)} (Speed)`, 15, 42);
      ctx.fillText("Drag mouse to rotate 3D view", W - 190, H - 15);
    }

    render();
  }
};

// 2. Unit 2: The Frenet-Serret Moving Trihedron & Curvature-Torsion Inspector
window.SIMULATIONS["sim_dg_frenet_frame"] = {
  title: "The Frenet-Serret Moving Trihedron: {T, N, B} Frame & Darboux Vector",
  description: "Experience the Frenet-Serret moving trihedron {T, N, B} propagating along a 3D curve with dynamic curvature kappa and torsion tau computation, illustrating the fundamental planes and Darboux rotation vector.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let progress = 0.35;
    let animSpeed = 0.003;
    let isPlaying = true;
    let rotX = 0.5, rotY = 0.7;
    let isDragging = false, lastX = 0, lastY = 0;

    if (controls) {
      controls.innerHTML = `
        <button id="dg-frenet-play" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Pause</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Frame Position s:</label>
        <input type="range" id="dg-frenet-slider" min="0" max="1" step="0.005" value="0.35" style="vertical-align: middle; width: 120px;">
        <span id="dg-frenet-vals" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">s = 0.35</span>
      `;

      const playBtn = document.getElementById("dg-frenet-play");
      playBtn.onclick = () => {
        isPlaying = !isPlaying;
        playBtn.innerText = isPlaying ? "Pause" : "Play";
      };

      const sSlider = document.getElementById("dg-frenet-slider");
      sSlider.oninput = (e) => {
        progress = parseFloat(e.target.value);
        document.getElementById("dg-frenet-vals").innerText = `s = ${progress.toFixed(2)}`;
      };
    }

    canvas.onmousedown = (e) => { isDragging = true; lastX = e.clientX; lastY = e.clientY; };
    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      rotY += (e.clientX - lastX) * 0.008;
      rotX += (e.clientY - lastY) * 0.008;
      lastX = e.clientX; lastY = e.clientY;
    });
    window.addEventListener("mouseup", () => { isDragging = false; });

    function getHelixData(s) {
      let a = 1.1, b = 0.28;
      let theta = s * Math.PI * 4;
      let pos = [a * Math.cos(theta), b * theta - 1.7, a * Math.sin(theta)];
      let c = Math.sqrt(a * a + b * b);
      let T = [(-a * Math.sin(theta)) / c, b / c, (a * Math.cos(theta)) / c];
      let N = [-Math.cos(theta), 0, -Math.sin(theta)];
      let B = [(b * Math.sin(theta)) / c, a / c, (-b * Math.cos(theta)) / c];
      let kappa = a / (c * c);
      let tau = b / (c * c);
      return { pos, T, N, B, kappa, tau };
    }

    function project3D(v, cx, cy, scale) {
      let x1 = v[0] * Math.cos(rotY) + v[2] * Math.sin(rotY);
      let z1 = -v[0] * Math.sin(rotY) + v[2] * Math.cos(rotY);
      let y1 = v[1] * Math.cos(rotX) - z1 * Math.sin(rotX);
      let z2 = v[1] * Math.sin(rotX) + z1 * Math.cos(rotX);
      let fov = 3.5 / (3.5 + z2);
      return [cx + x1 * scale * fov, cy - y1 * scale * fov];
    }

    function animate() {
      if (isPlaying) {
        progress = (progress + animSpeed) % 1.0;
        const sSlider = document.getElementById("dg-frenet-slider");
        if (sSlider) {
          sSlider.value = progress;
          document.getElementById("dg-frenet-vals").innerText = `s = ${progress.toFixed(2)}`;
        }
      }

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;
      const cx = W / 2, cy = H / 2;
      const scale = 115;

      // Draw helix path
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i <= 150; i++) {
        let p = getHelixData(i / 150).pos;
        let p2 = project3D(p, cx, cy, scale);
        if (i === 0) ctx.moveTo(p2[0], p2[1]);
        else ctx.lineTo(p2[0], p2[1]);
      }
      ctx.stroke();

      // Current Frenet frame
      let frame = getHelixData(progress);
      let p0 = project3D(frame.pos, cx, cy, scale);

      // Draw T (Red)
      let pT = project3D([frame.pos[0] + frame.T[0] * 0.75, frame.pos[1] + frame.T[1] * 0.75, frame.pos[2] + frame.T[2] * 0.75], cx, cy, scale);
      ctx.strokeStyle = "#ef4444";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(p0[0], p0[1]); ctx.lineTo(pT[0], pT[1]); ctx.stroke();

      // Draw N (Green)
      let pN = project3D([frame.pos[0] + frame.N[0] * 0.75, frame.pos[1] + frame.N[1] * 0.75, frame.pos[2] + frame.N[2] * 0.75], cx, cy, scale);
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(p0[0], p0[1]); ctx.lineTo(pN[0], pN[1]); ctx.stroke();

      // Draw B (Blue)
      let pB = project3D([frame.pos[0] + frame.B[0] * 0.75, frame.pos[1] + frame.B[1] * 0.75, frame.pos[2] + frame.B[2] * 0.75], cx, cy, scale);
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(p0[0], p0[1]); ctx.lineTo(pB[0], pB[1]); ctx.stroke();

      // Darboux Vector omega = tau*T + kappa*B (Purple)
      let dwx = frame.tau * frame.T[0] + frame.kappa * frame.B[0];
      let dwy = frame.tau * frame.T[1] + frame.kappa * frame.B[1];
      let dwz = frame.tau * frame.T[2] + frame.kappa * frame.B[2];
      let pDarboux = project3D([frame.pos[0] + dwx * 0.8, frame.pos[1] + dwy * 0.8, frame.pos[2] + dwz * 0.8], cx, cy, scale);
      ctx.strokeStyle = "#c084fc";
      ctx.setLineDash([4, 4]);
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(p0[0], p0[1]); ctx.lineTo(pDarboux[0], pDarboux[1]); ctx.stroke();
      ctx.setLineDash([]);

      // Point node
      ctx.fillStyle = "#ffffff";
      ctx.beginPath(); ctx.arc(p0[0], p0[1], 5, 0, Math.PI * 2); ctx.fill();

      // HUD Legend
      ctx.fillStyle = "#ef4444"; ctx.font = "bold 11px Inter"; ctx.fillText("T (Tangent)", pT[0] + 5, pT[1]);
      ctx.fillStyle = "#10b981"; ctx.fillText("N (Principal Normal)", pN[0] + 5, pN[1]);
      ctx.fillStyle = "#38bdf8"; ctx.fillText("B (Binormal)", pB[0] + 5, pB[1]);
      ctx.fillStyle = "#c084fc"; ctx.fillText("ω (Darboux Vector)", pDarboux[0] + 5, pDarboux[1]);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, monospace";
      ctx.fillText(`Curvature κ = ${frame.kappa.toFixed(3)}`, 15, 25);
      ctx.fillText(`Torsion   τ = ${frame.tau.toFixed(3)}`, 15, 42);
      ctx.fillText(`Ratio τ/κ = ${(frame.tau / frame.kappa).toFixed(3)} (Const → Helix)`, 15, 59);

      requestAnimationFrame(animate);
    }

    animate();
  }
};

// 3. Unit 3: Helices, Involutes, Evolutes & Bertrand Curves Explorer
window.SIMULATIONS["sim_dg_helix_bertrand"] = {
  title: "General Helices, Bertrand Mates & Evolute String Unwinding",
  description: "Inspect the geometric duality of general helices with constant Lancret pitch ratio, generate Bertrand curve pairs with shared principal normals, and visualize the involute string construction.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let viewMode = "bertrand"; // "bertrand", "involute"
    let helixPitch = 0.45;
    let mateDistance = 0.4;
    let rotX = 0.4, rotY = 0.6;
    let isDragging = false, lastX = 0, lastY = 0;

    if (controls) {
      controls.innerHTML = `
        <button id="dg-btn-bertrand" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Bertrand Pair</button>
        <button id="dg-btn-involute" style="padding: 0.35rem 0.75rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Evolute & Involute</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Pitch:</label>
        <input type="range" id="dg-pitch-slider" min="0.1" max="1.0" step="0.05" value="0.45" style="vertical-align: middle; width: 90px;">
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Mate Offset a:</label>
        <input type="range" id="dg-offset-slider" min="0.1" max="0.8" step="0.05" value="0.4" style="vertical-align: middle; width: 90px;">
      `;

      document.getElementById("dg-btn-bertrand").onclick = () => { viewMode = "bertrand"; render(); };
      document.getElementById("dg-btn-involute").onclick = () => { viewMode = "involute"; render(); };
      document.getElementById("dg-pitch-slider").oninput = (e) => { helixPitch = parseFloat(e.target.value); render(); };
      document.getElementById("dg-offset-slider").oninput = (e) => { mateDistance = parseFloat(e.target.value); render(); };
    }

    canvas.onmousedown = (e) => { isDragging = true; lastX = e.clientX; lastY = e.clientY; };
    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      rotY += (e.clientX - lastX) * 0.008;
      rotX += (e.clientY - lastY) * 0.008;
      lastX = e.clientX; lastY = e.clientY;
      render();
    });
    window.addEventListener("mouseup", () => { isDragging = false; });

    function project3D(v, cx, cy, scale) {
      let x1 = v[0] * Math.cos(rotY) + v[2] * Math.sin(rotY);
      let z1 = -v[0] * Math.sin(rotY) + v[2] * Math.cos(rotY);
      let y1 = v[1] * Math.cos(rotX) - z1 * Math.sin(rotX);
      let z2 = v[1] * Math.sin(rotX) + z1 * Math.cos(rotX);
      let fov = 3.5 / (3.5 + z2);
      return [cx + x1 * scale * fov, cy - y1 * scale * fov];
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;
      const cx = W / 2, cy = H / 2;
      const scale = 110;

      const numSteps = 120;
      let primaryCurve = [];
      let secondaryCurve = [];
      let connectingNormals = [];

      for (let i = 0; i <= numSteps; i++) {
        let u = (i / numSteps) * Math.PI * 4;
        let R = 1.0;
        let x = R * Math.cos(u);
        let y = (u - Math.PI * 2) * helixPitch * 0.4;
        let z = R * Math.sin(u);

        // Principal normal points inward towards axis: (-cos u, 0, -sin u)
        let nx = -Math.cos(u);
        let ny = 0;
        let nz = -Math.sin(u);

        primaryCurve.push([x, y, z]);

        if (viewMode === "bertrand") {
          // Bertrand mate: r*(s) = r(s) + a * N(s)
          let xm = x + mateDistance * nx;
          let ym = y + mateDistance * ny;
          let zm = z + mateDistance * nz;
          secondaryCurve.push([xm, ym, zm]);
          if (i % 12 === 0) {
            connectingNormals.push({ p1: [x, y, z], p2: [xm, ym, zm] });
          }
        } else {
          // Involute: r_inv(s) = r(s) + (c - s) * T(s)
          let T_mag = Math.sqrt(R * R + (helixPitch * 0.4) * (helixPitch * 0.4));
          let tx = (-R * Math.sin(u)) / T_mag;
          let ty = (helixPitch * 0.4) / T_mag;
          let tz = (R * Math.cos(u)) / T_mag;
          let stringLen = (Math.PI * 4 - u) * 0.25;
          secondaryCurve.push([x + stringLen * tx, y + stringLen * ty, z + stringLen * tz]);
        }
      }

      // Draw Primary Curve (Blue)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i < primaryCurve.length; i++) {
        let p = project3D(primaryCurve[i], cx, cy, scale);
        if (i === 0) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]);
      }
      ctx.stroke();

      // Draw Secondary Curve (Pink / Green)
      ctx.strokeStyle = viewMode === "bertrand" ? "#f43f5e" : "#10b981";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i < secondaryCurve.length; i++) {
        let p = project3D(secondaryCurve[i], cx, cy, scale);
        if (i === 0) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]);
      }
      ctx.stroke();

      // Draw connecting common normals for Bertrand pairs
      if (viewMode === "bertrand") {
        ctx.strokeStyle = "rgba(234, 179, 8, 0.6)";
        ctx.lineWidth = 1.5;
        connectingNormals.forEach(cn => {
          let pt1 = project3D(cn.p1, cx, cy, scale);
          let pt2 = project3D(cn.p2, cx, cy, scale);
          ctx.beginPath(); ctx.moveTo(pt1[0], pt1[1]); ctx.lineTo(pt2[0], pt2[1]); ctx.stroke();
        });
      }

      // HUD
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Primary Curve r(s)", 15, 25);
      ctx.fillStyle = viewMode === "bertrand" ? "#f43f5e" : "#10b981";
      ctx.fillText(viewMode === "bertrand" ? "Bertrand Mate r*(s) = r(s) + a·N(s)" : "Involute Curve r_inv(s)", 15, 42);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, monospace";
      if (viewMode === "bertrand") {
        ctx.fillText("Linear relation: a·κ + b·τ = 1 (Shared Principal Normal N)", 15, 60);
      } else {
        ctx.fillText("Orthogonal string trajectory: Tangent of evolute is normal of involute", 15, 60);
      }
    }

    render();
  }
};

// 4. Unit 4: First Fundamental Form & Metric Tensor Explorer
window.SIMULATIONS["sim_dg_first_fundamental_form"] = {
  title: "The First Fundamental Form: Metric Tensor, Angles & Surface Area Element",
  description: "Examine parametric surfaces r(u, v): view coordinate curves, tangent vectors r_u and r_v, calculate metric coefficients E, F, G, and measure local Riemannian surface area elements dA = sqrt(EG - F^2) du dv.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let surfType = "torus"; // "torus", "saddle", "sphere"
    let uPoint = 0.5, vPoint = 0.5;
    let rotX = 0.5, rotY = 0.5;
    let isDragging = false, lastX = 0, lastY = 0;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Surface:</label>
        <button id="dg-surf-torus" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Torus</button>
        <button id="dg-surf-saddle" style="padding: 0.35rem 0.75rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Monkey Saddle</button>
        <button id="dg-surf-sphere" style="padding: 0.35rem 0.75rem; background: #8b5cf6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Sphere</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">u:</label>
        <input type="range" id="dg-u-slider" min="0" max="1" step="0.02" value="0.5" style="vertical-align: middle; width: 80px;">
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">v:</label>
        <input type="range" id="dg-v-slider" min="0" max="1" step="0.02" value="0.5" style="vertical-align: middle; width: 80px;">
      `;

      document.getElementById("dg-surf-torus").onclick = () => { surfType = "torus"; render(); };
      document.getElementById("dg-surf-saddle").onclick = () => { surfType = "saddle"; render(); };
      document.getElementById("dg-surf-sphere").onclick = () => { surfType = "sphere"; render(); };

      document.getElementById("dg-u-slider").oninput = (e) => { uPoint = parseFloat(e.target.value); render(); };
      document.getElementById("dg-v-slider").oninput = (e) => { vPoint = parseFloat(e.target.value); render(); };
    }

    canvas.onmousedown = (e) => { isDragging = true; lastX = e.clientX; lastY = e.clientY; };
    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      rotY += (e.clientX - lastX) * 0.008;
      rotX += (e.clientY - lastY) * 0.008;
      lastX = e.clientX; lastY = e.clientY;
      render();
    });
    window.addEventListener("mouseup", () => { isDragging = false; });

    function getSurfacePoint(u, v) {
      if (surfType === "torus") {
        let R = 1.1, r = 0.45;
        let phi = u * Math.PI * 2;
        let psi = v * Math.PI * 2;
        let x = (R + r * Math.cos(psi)) * Math.cos(phi);
        let y = (R + r * Math.cos(psi)) * Math.sin(phi);
        let z = r * Math.sin(psi);
        let ru = [-(R + r * Math.cos(psi)) * Math.sin(phi) * 2 * Math.PI, (R + r * Math.cos(psi)) * Math.cos(phi) * 2 * Math.PI, 0];
        let rv = [-r * Math.sin(psi) * Math.cos(phi) * 2 * Math.PI, -r * Math.sin(psi) * Math.sin(phi) * 2 * Math.PI, r * Math.cos(psi) * 2 * Math.PI];
        return { pos: [x, z, y], ru: [ru[0], ru[2], ru[1]], rv: [rv[0], rv[2], rv[1]] };
      } else if (surfType === "saddle") {
        let x = (u - 0.5) * 2.0;
        let y = (v - 0.5) * 2.0;
        let z = (x * x - y * y) * 0.5;
        return { pos: [x, z, y], ru: [2.0, x * 2.0, 0], rv: [0, -y * 2.0, 2.0] };
      } else {
        // Sphere
        let R = 1.1;
        let theta = u * Math.PI;
        let phi = v * Math.PI * 2;
        let x = R * Math.sin(theta) * Math.cos(phi);
        let y = R * Math.sin(theta) * Math.sin(phi);
        let z = R * Math.cos(theta);
        let ru = [R * Math.cos(theta) * Math.cos(phi) * Math.PI, R * Math.cos(theta) * Math.sin(phi) * Math.PI, -R * Math.sin(theta) * Math.PI];
        let rv = [-R * Math.sin(theta) * Math.sin(phi) * 2 * Math.PI, R * Math.sin(theta) * Math.cos(phi) * 2 * Math.PI, 0];
        return { pos: [x, z, y], ru: [ru[0], ru[2], ru[1]], rv: [rv[0], rv[2], rv[1]] };
      }
    }

    function project3D(v, cx, cy, scale) {
      let x1 = v[0] * Math.cos(rotY) + v[2] * Math.sin(rotY);
      let z1 = -v[0] * Math.sin(rotY) + v[2] * Math.cos(rotY);
      let y1 = v[1] * Math.cos(rotX) - z1 * Math.sin(rotX);
      let z2 = v[1] * Math.sin(rotX) + z1 * Math.cos(rotX);
      let fov = 3.5 / (3.5 + z2);
      return [cx + x1 * scale * fov, cy - y1 * scale * fov];
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;
      const cx = W / 2, cy = H / 2;
      const scale = 110;

      // Draw wireframe grid
      const gridN = 20;
      ctx.strokeStyle = "rgba(148, 163, 184, 0.22)";
      ctx.lineWidth = 1;

      // u-lines
      for (let i = 0; i <= gridN; i++) {
        let u = i / gridN;
        ctx.beginPath();
        for (let j = 0; j <= gridN; j++) {
          let v = j / gridN;
          let p2 = project3D(getSurfacePoint(u, v).pos, cx, cy, scale);
          if (j === 0) ctx.moveTo(p2[0], p2[1]); else ctx.lineTo(p2[0], p2[1]);
        }
        ctx.stroke();
      }

      // v-lines
      for (let j = 0; j <= gridN; j++) {
        let v = j / gridN;
        ctx.beginPath();
        for (let i = 0; i <= gridN; i++) {
          let u = i / gridN;
          let p2 = project3D(getSurfacePoint(u, v).pos, cx, cy, scale);
          if (i === 0) ctx.moveTo(p2[0], p2[1]); else ctx.lineTo(p2[0], p2[1]);
        }
        ctx.stroke();
      }

      // Current evaluation point
      let cur = getSurfacePoint(uPoint, vPoint);
      let p0 = project3D(cur.pos, cx, cy, scale);

      // Compute metric coefficients E, F, G
      let ru = cur.ru, rv = cur.rv;
      let E = ru[0] * ru[0] + ru[1] * ru[1] + ru[2] * ru[2];
      let F = ru[0] * rv[0] + ru[1] * rv[1] + ru[2] * rv[2];
      let G = rv[0] * rv[0] + rv[1] * rv[1] + rv[2] * rv[2];
      let detI = E * G - F * F;
      let dA = Math.sqrt(Math.max(0, detI));

      // Draw tangent vectors r_u (Red) and r_v (Green)
      let vecScale = 0.08;
      let pRu = project3D([cur.pos[0] + ru[0] * vecScale, cur.pos[1] + ru[1] * vecScale, cur.pos[2] + ru[2] * vecScale], cx, cy, scale);
      let pRv = project3D([cur.pos[0] + rv[0] * vecScale, cur.pos[1] + rv[1] * vecScale, cur.pos[2] + rv[2] * vecScale], cx, cy, scale);

      // Draw tangent parallelogram (dA element)
      let pCorner = project3D([cur.pos[0] + (ru[0] + rv[0]) * vecScale, cur.pos[1] + (ru[1] + rv[1]) * vecScale, cur.pos[2] + (ru[2] + rv[2]) * vecScale], cx, cy, scale);
      ctx.fillStyle = "rgba(234, 179, 8, 0.28)";
      ctx.beginPath();
      ctx.moveTo(p0[0], p0[1]); ctx.lineTo(pRu[0], pRu[1]); ctx.lineTo(pCorner[0], pCorner[1]); ctx.lineTo(pRv[0], pRv[1]);
      ctx.closePath();
      ctx.fill();

      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(p0[0], p0[1]); ctx.lineTo(pRu[0], pRu[1]); ctx.stroke();
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(p0[0], p0[1]); ctx.lineTo(pRv[0], pRv[1]); ctx.stroke();

      ctx.fillStyle = "#ffffff";
      ctx.beginPath(); ctx.arc(p0[0], p0[1], 4.5, 0, Math.PI * 2); ctx.fill();

      // HUD
      ctx.fillStyle = "#ef4444"; ctx.font = "bold 11px Inter"; ctx.fillText("r_u", pRu[0] + 5, pRu[1]);
      ctx.fillStyle = "#10b981"; ctx.fillText("r_v", pRv[0] + 5, pRv[1]);
      ctx.fillStyle = "#eab308"; ctx.fillText("dA = √g du dv", pCorner[0] + 5, pCorner[1]);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, monospace";
      ctx.fillText(`First Fundamental Form: I = E du² + 2F du dv + G dv²`, 15, 25);
      ctx.fillText(`E = <r_u, r_u> = ${E.toFixed(2)}`, 15, 42);
      ctx.fillText(`F = <r_u, r_v> = ${F.toFixed(2)}`, 15, 59);
      ctx.fillText(`G = <r_v, r_v> = ${G.toFixed(2)}`, 15, 76);
      ctx.fillText(`det(g_ij) = EG - F² = ${detI.toFixed(2)}`, 15, 93);
    }

    render();
  }
};

// 5. Unit 5: Second Fundamental Form & Gauss Map Sphere Visualizer
window.SIMULATIONS["sim_dg_gauss_map_weingarten"] = {
  title: "The Gauss Map & The Second Fundamental Form",
  description: "Visualize how surface points map to the unit sphere S^2 under the Gauss normal map n: S -> S^2, and how the Shape Operator (Weingarten map) differentiates normal directions.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let curvatureMode = "elliptic"; // "elliptic", "hyperbolic", "parabolic"
    let probeX = 0.0, probeY = 0.0;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Local Point Geometry:</label>
        <button id="dg-btn-ellip" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Elliptic (K > 0)</button>
        <button id="dg-btn-hyper" style="padding: 0.35rem 0.75rem; background: #f43f5e; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Hyperbolic (K < 0)</button>
        <button id="dg-btn-para" style="padding: 0.35rem 0.75rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Parabolic (K = 0)</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Probe Offset X:</label>
        <input type="range" id="dg-probe-x" min="-0.8" max="0.8" step="0.05" value="0.0" style="vertical-align: middle; width: 80px;">
      `;

      document.getElementById("dg-btn-ellip").onclick = () => { curvatureMode = "elliptic"; render(); };
      document.getElementById("dg-btn-hyper").onclick = () => { curvatureMode = "hyperbolic"; render(); };
      document.getElementById("dg-btn-para").onclick = () => { curvatureMode = "parabolic"; render(); };

      document.getElementById("dg-probe-x").oninput = (e) => {
        probeX = parseFloat(e.target.value);
        render();
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;

      // Two viewport split: Left = Surface Patch, Right = Gauss Sphere S^2
      const leftCx = W * 0.28, rightCx = W * 0.74, cy = H / 2;
      const patchR = 85, sphereR = 75;

      // Draw Left: Surface patch height map z = 1/2(k1 x^2 + k2 y^2)
      let k1 = 1.0, k2 = 1.0;
      if (curvatureMode === "hyperbolic") { k1 = 1.0; k2 = -1.0; }
      else if (curvatureMode === "parabolic") { k1 = 1.0; k2 = 0.0; }

      // Surface patch representation
      ctx.strokeStyle = "rgba(148, 163, 184, 0.3)";
      ctx.lineWidth = 1;
      for (let y = -0.8; y <= 0.8; y += 0.2) {
        ctx.beginPath();
        for (let x = -0.8; x <= 0.8; x += 0.05) {
          let px = leftCx + x * patchR;
          let z = 0.5 * (k1 * x * x + k2 * y * y);
          let py = cy + y * (patchR * 0.7) - z * 40;
          if (x === -0.8) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Left Normal vector at probe point
      let x0 = probeX, y0 = 0.2;
      let z0 = 0.5 * (k1 * x0 * x0 + k2 * y0 * y0);
      let pSurface = [leftCx + x0 * patchR, cy + y0 * (patchR * 0.7) - z0 * 40];

      // Normal is (-zx, -zy, 1) / sqrt(1 + zx^2 + zy^2)
      let zx = k1 * x0, zy = k2 * y0;
      let nNorm = Math.sqrt(zx * zx + zy * zy + 1);
      let nx = -zx / nNorm, ny = -zy / nNorm, nz = 1 / nNorm;

      // Draw normal arrow on left
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(pSurface[0], pSurface[1]);
      ctx.lineTo(pSurface[0] + nx * 50, pSurface[1] - nz * 50 + ny * 20);
      ctx.stroke();

      ctx.fillStyle = "#ffffff";
      ctx.beginPath(); ctx.arc(pSurface[0], pSurface[1], 4, 0, Math.PI * 2); ctx.fill();

      // Draw Right: Gauss Sphere S^2
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(rightCx, cy, sphereR, 0, Math.PI * 2); ctx.stroke();
      // Equator & meridian
      ctx.beginPath(); ctx.ellipse(rightCx, cy, sphereR, sphereR * 0.35, 0, 0, Math.PI * 2); ctx.stroke();
      ctx.beginPath(); ctx.ellipse(rightCx, cy, sphereR * 0.35, sphereR, 0, 0, Math.PI * 2); ctx.stroke();

      // Normal vector tip mapped onto S^2
      let pSphere = [rightCx + nx * sphereR, cy - nz * sphereR * 0.8 + ny * sphereR * 0.3];
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(rightCx, cy); ctx.lineTo(pSphere[0], pSphere[1]); ctx.stroke();

      ctx.fillStyle = "#f43f5e";
      ctx.beginPath(); ctx.arc(pSphere[0], pSphere[1], 5, 0, Math.PI * 2); ctx.fill();

      // Titles & Math
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Surface Patch M", leftCx - 50, cy - patchR - 15);
      ctx.fillText("Gauss Sphere S²", rightCx - 50, cy - sphereR - 15);

      let K = k1 * k2;
      let meanH = 0.5 * (k1 + k2);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, monospace";
      ctx.fillText(`Shape Operator S_p = -dn`, 15, 25);
      ctx.fillText(`Principal Curvatures: κ₁ = ${k1.toFixed(1)}, κ₂ = ${k2.toFixed(1)}`, 15, 42);
      ctx.fillText(`Gaussian Curvature   K = κ₁κ₂ = ${K.toFixed(2)} (${curvatureMode.toUpperCase()})`, 15, 59);
      ctx.fillText(`Mean Curvature       H = ½(κ₁+κ₂) = ${meanH.toFixed(2)}`, 15, 76);
      ctx.fillText(`Second Form: II = L du² + 2M du dv + N dv²`, 15, 93);
    }

    render();
  }
};

// 6. Unit 6: Principal Curvatures & Shape Classification Engine
window.SIMULATIONS["sim_dg_curvatures_principal"] = {
  title: "Principal Curvatures, Osculating Paraboloids & Curvature Heatmaps",
  description: "Inspect the orthogonal principal curvatures kappa_1 and kappa_2, observe osculating circular arcs along principal sections, and witness how the Gaussian curvature K dictates local surface topology.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let k1 = 1.2, k2 = -0.8;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">κ₁ (Principal 1):</label>
        <input type="range" id="dg-k1-slider" min="-2.0" max="2.0" step="0.1" value="1.2" style="vertical-align: middle; width: 90px;">
        <span id="dg-k1-val" style="color: #ef4444; font-family: monospace; font-size: 0.85rem;">κ₁ = 1.20</span>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">κ₂ (Principal 2):</label>
        <input type="range" id="dg-k2-slider" min="-2.0" max="2.0" step="0.1" value="-0.8" style="vertical-align: middle; width: 90px;">
        <span id="dg-k2-val" style="color: #10b981; font-family: monospace; font-size: 0.85rem;">κ₂ = -0.80</span>
      `;

      document.getElementById("dg-k1-slider").oninput = (e) => {
        k1 = parseFloat(e.target.value);
        document.getElementById("dg-k1-val").innerText = `κ₁ = ${k1.toFixed(2)}`;
        render();
      };
      document.getElementById("dg-k2-slider").oninput = (e) => {
        k2 = parseFloat(e.target.value);
        document.getElementById("dg-k2-val").innerText = `κ₂ = ${k2.toFixed(2)}`;
        render();
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;
      const cx = W / 2 + 30, cy = H / 2 + 15;

      let K = k1 * k2;
      let meanH = 0.5 * (k1 + k2);

      // 3D Oblique projection of the osculating quadric z = 1/2(k1 x^2 + k2 y^2)
      const uScale = 85, vScale = 50, zScale = 40;

      // Draw surface quadric mesh
      for (let v = -1.2; v <= 1.2; v += 0.15) {
        ctx.beginPath();
        ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
        for (let u = -1.2; u <= 1.2; u += 0.05) {
          let z = 0.5 * (k1 * u * u + k2 * v * v);
          let px = cx + u * uScale - v * (vScale * 0.7);
          let py = cy + v * vScale - z * zScale;
          if (u === -1.2) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Draw Principal Section 1 (v = 0, Red parabola)
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let u = -1.2; u <= 1.2; u += 0.04) {
        let z = 0.5 * k1 * u * u;
        let px = cx + u * uScale;
        let py = cy - z * zScale;
        if (u === -1.2) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Draw Principal Section 2 (u = 0, Green parabola)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let v = -1.2; v <= 1.2; v += 0.04) {
        let z = 0.5 * k2 * v * v;
        let px = cx - v * (vScale * 0.7);
        let py = cy + v * vScale - z * zScale;
        if (v === -1.2) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Normal vector at origin
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx, cy - 65); ctx.stroke();
      ctx.fillStyle = "#ffffff"; ctx.beginPath(); ctx.arc(cx, cy, 4.5, 0, Math.PI * 2); ctx.fill();

      // Classification Badge
      let classText = "ELLIPTIC POINT (K > 0)";
      let classColor = "#3b82f6";
      if (Math.abs(K) < 0.01) {
        classText = (Math.abs(k1) < 0.01 && Math.abs(k2) < 0.01) ? "PLANAR POINT (K = 0, H = 0)" : "PARABOLIC POINT (K = 0)";
        classColor = "#10b981";
      } else if (K < 0) {
        classText = "HYPERBOLIC POINT (K < 0)";
        classColor = "#f43f5e";
      }

      ctx.fillStyle = classColor; ctx.font = "bold 13px Inter";
      ctx.fillText(classText, 15, 25);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, monospace";
      ctx.fillText(`Gaussian Curvature K = κ₁ · κ₂ = ${K.toFixed(3)}`, 15, 45);
      ctx.fillText(`Mean Curvature     H = ½(κ₁ + κ₂) = ${meanH.toFixed(3)}`, 15, 62);
      ctx.fillStyle = "#ef4444"; ctx.fillText(`Principal Curvature 1 (Red): κ₁ = ${k1.toFixed(2)}`, 15, 80);
      ctx.fillStyle = "#10b981"; ctx.fillText(`Principal Curvature 2 (Green): κ₂ = ${k2.toFixed(2)}`, 15, 97);
    }

    render();
  }
};

// 7. Unit 7: The Dupin Indicatrix & Euler's Normal Curvature Wheel
window.SIMULATIONS["sim_dg_dupin_indicatrix"] = {
  title: "The Dupin Indicatrix & Euler's Normal Curvature Wheel",
  description: "Explore Euler's Theorem on normal curvature kappa_n(theta) = kappa_1 cos^2 theta + kappa_2 sin^2 theta, and examine the Dupin Indicatrix conics and asymptotic directions at elliptic and hyperbolic points.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let k1 = 1.0, k2 = -0.6;
    let angleTheta = 0.45;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Direction θ:</label>
        <input type="range" id="dg-theta-slider" min="0" max="3.1415" step="0.02" value="0.45" style="vertical-align: middle; width: 100px;">
        <span id="dg-theta-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">θ = 25.8°</span>
        <button id="dg-btn-dup-ell" style="padding: 0.35rem 0.65rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer; margin-left: 0.5rem;">Elliptic</button>
        <button id="dg-btn-dup-hyp" style="padding: 0.35rem 0.65rem; background: #f43f5e; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Hyperbolic</button>
      `;

      const tSlider = document.getElementById("dg-theta-slider");
      tSlider.oninput = (e) => {
        angleTheta = parseFloat(e.target.value);
        document.getElementById("dg-theta-val").innerText = `θ = ${(angleTheta * 180 / Math.PI).toFixed(1)}°`;
        render();
      };

      document.getElementById("dg-btn-dup-ell").onclick = () => { k1 = 1.0; k2 = 0.5; render(); };
      document.getElementById("dg-btn-dup-hyp").onclick = () => { k1 = 1.0; k2 = -0.6; render(); };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;
      const cx = W / 2 + 50, cy = H / 2;
      const R = 90;

      // Coordinate axes for Dupin Indicatrix: x / sqrt(|k1|), y / sqrt(|k2|)
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(cx - 140, cy); ctx.lineTo(cx + 140, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy - 120); ctx.lineTo(cx, cy + 120); ctx.stroke();

      // Normal Curvature via Euler's Theorem
      let cosT = Math.cos(angleTheta), sinT = Math.sin(angleTheta);
      let kn = k1 * cosT * cosT + k2 * sinT * sinT;

      // Draw Dupin Indicatrix: |k1| x^2 + |k2| y^2 = 1 (or hyperbolas if k2 < 0)
      if (k1 * k2 > 0) {
        // Ellipse
        let a = R / Math.sqrt(Math.abs(k1));
        let b = R / Math.sqrt(Math.abs(k2));
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.ellipse(cx, cy, a, b, 0, 0, Math.PI * 2); ctx.stroke();
      } else {
        // Hyperbola pair: k1 x^2 + k2 y^2 = ±1
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2;
        // Branch 1: k1 x^2 - |k2| y^2 = 1
        let a = R / Math.sqrt(Math.abs(k1));
        let b = R / Math.sqrt(Math.abs(k2));
        for (let sign of [-1, 1]) {
          ctx.beginPath();
          for (let y = -90; y <= 90; y += 3) {
            let val = 1 + (y * y) / (b * b);
            let x = sign * a * Math.sqrt(val);
            if (y === -90) ctx.moveTo(cx + x, cy + y); else ctx.lineTo(cx + x, cy + y);
          }
          ctx.stroke();
        }
        // Asymptotes: y = ± sqrt(k1 / |k2|) x
        let slope = Math.sqrt(Math.abs(k1) / Math.abs(k2));
        ctx.strokeStyle = "rgba(234, 179, 8, 0.4)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(cx - 100, cy - 100 * slope); ctx.lineTo(cx + 100, cy + 100 * slope); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx - 100, cy + 100 * slope); ctx.lineTo(cx + 100, cy - 100 * slope); ctx.stroke();
        ctx.setLineDash([]);
      }

      // Draw current direction line at angle theta
      let dirLen = 120;
      let dx = dirLen * cosT, dy = -dirLen * sinT;
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + dx, cy + dy); ctx.stroke();

      // Indicatrix radius r = 1 / sqrt(|kn|)
      if (Math.abs(kn) > 1e-4) {
        let rIndicatrix = R / Math.sqrt(Math.abs(kn));
        let pInd = [cx + rIndicatrix * cosT, cy - rIndicatrix * sinT];
        ctx.fillStyle = "#10b981";
        ctx.beginPath(); ctx.arc(pInd[0], pInd[1], 5, 0, Math.PI * 2); ctx.fill();
        ctx.fillText(`r = 1/√|κ_n|`, pInd[0] + 8, pInd[1]);
      }

      // HUD
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Euler's Theorem on Normal Curvature", 15, 25);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, monospace";
      ctx.fillText(`κ_n(θ) = κ₁ cos²θ + κ₂ sin²θ`, 15, 45);
      ctx.fillText(`κ₁ = ${k1.toFixed(2)},  κ₂ = ${k2.toFixed(2)}`, 15, 62);
      ctx.fillText(`Direction θ = ${(angleTheta * 180 / Math.PI).toFixed(1)}°`, 15, 79);
      ctx.fillStyle = kn >= 0 ? "#10b981" : "#f43f5e";
      ctx.fillText(`Normal Curvature κ_n = ${kn.toFixed(3)}`, 15, 96);
    }

    render();
  }
};

// 8. Unit 8: Geodesics, Christoffel Symbols & Theorema Egregium Inspector
window.SIMULATIONS["sim_dg_geodesic_egregium"] = {
  title: "Geodesics & Gauss's Theorema Egregium: Intrinsic Curvature Invariance",
  description: "Shoot geodesic trajectories on surfaces of different intrinsic curvatures: plane (K = 0), cylinder (K = 0, developable), and sphere (K > 0), demonstrating Gauss's Remarkable Theorem that K is preserved under bending without stretching.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let spaceGeo = "sphere"; // "sphere", "cylinder", "plane"
    let launchAngle = 0.6;
    let rotX = 0.4, rotY = 0.5;
    let isDragging = false, lastX = 0, lastY = 0;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Geometry:</label>
        <button id="dg-geo-sphere" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Sphere (K > 0)</button>
        <button id="dg-geo-cyl" style="padding: 0.35rem 0.75rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Cylinder (K = 0)</button>
        <button id="dg-geo-plane" style="padding: 0.35rem 0.75rem; background: #8b5cf6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Plane (K = 0)</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Launch Heading α:</label>
        <input type="range" id="dg-angle-slider" min="0" max="3.14" step="0.05" value="0.6" style="vertical-align: middle; width: 90px;">
      `;

      document.getElementById("dg-geo-sphere").onclick = () => { spaceGeo = "sphere"; render(); };
      document.getElementById("dg-geo-cyl").onclick = () => { spaceGeo = "cylinder"; render(); };
      document.getElementById("dg-geo-plane").onclick = () => { spaceGeo = "plane"; render(); };
      document.getElementById("dg-angle-slider").oninput = (e) => { launchAngle = parseFloat(e.target.value); render(); };
    }

    canvas.onmousedown = (e) => { isDragging = true; lastX = e.clientX; lastY = e.clientY; };
    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      rotY += (e.clientX - lastX) * 0.008;
      rotX += (e.clientY - lastY) * 0.008;
      lastX = e.clientX; lastY = e.clientY;
      render();
    });
    window.addEventListener("mouseup", () => { isDragging = false; });

    function project3D(v, cx, cy, scale) {
      let x1 = v[0] * Math.cos(rotY) + v[2] * Math.sin(rotY);
      let z1 = -v[0] * Math.sin(rotY) + v[2] * Math.cos(rotY);
      let y1 = v[1] * Math.cos(rotX) - z1 * Math.sin(rotX);
      let z2 = v[1] * Math.sin(rotX) + z1 * Math.cos(rotX);
      let fov = 3.5 / (3.5 + z2);
      return [cx + x1 * scale * fov, cy - y1 * scale * fov];
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;
      const cx = W / 2, cy = H / 2;
      const scale = 110;

      if (spaceGeo === "sphere") {
        // Draw sphere wireframe
        ctx.strokeStyle = "rgba(148, 163, 184, 0.2)";
        for (let t = 0.2; t < Math.PI; t += 0.3) {
          ctx.beginPath();
          for (let p = 0; p <= Math.PI * 2; p += 0.1) {
            let pt = [Math.sin(t) * Math.cos(p), Math.cos(t), Math.sin(t) * Math.sin(p)];
            let p2 = project3D(pt, cx, cy, scale);
            if (p === 0) ctx.moveTo(p2[0], p2[1]); else ctx.lineTo(p2[0], p2[1]);
          }
          ctx.stroke();
        }

        // Great circle geodesic
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 3;
        ctx.beginPath();
        for (let s = 0; s <= Math.PI * 2; s += 0.05) {
          // Great circle tilted by launchAngle
          let pt = [Math.cos(s), Math.sin(s) * Math.sin(launchAngle), Math.sin(s) * Math.cos(launchAngle)];
          let p2 = project3D(pt, cx, cy, scale);
          if (s === 0) ctx.moveTo(p2[0], p2[1]); else ctx.lineTo(p2[0], p2[1]);
        }
        ctx.stroke();
      } else if (spaceGeo === "cylinder") {
        // Cylinder
        ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
        for (let h = -1.2; h <= 1.2; h += 0.4) {
          ctx.beginPath();
          for (let t = 0; t <= Math.PI * 2; t += 0.1) {
            let pt = [Math.cos(t), h, Math.sin(t)];
            let p2 = project3D(pt, cx, cy, scale);
            if (t === 0) ctx.moveTo(p2[0], p2[1]); else ctx.lineTo(p2[0], p2[1]);
          }
          ctx.stroke();
        }

        // Helical geodesic on cylinder
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 3;
        ctx.beginPath();
        for (let s = -Math.PI * 2; s <= Math.PI * 2; s += 0.05) {
          let pt = [Math.cos(s), s * Math.tan(launchAngle * 0.4) * 0.3, Math.sin(s)];
          let p2 = project3D(pt, cx, cy, scale);
          if (s === -Math.PI * 2) ctx.moveTo(p2[0], p2[1]); else ctx.lineTo(p2[0], p2[1]);
        }
        ctx.stroke();
      } else {
        // Plane
        ctx.strokeStyle = "rgba(148, 163, 184, 0.3)";
        for (let y = -1.2; y <= 1.2; y += 0.3) {
          let p1 = project3D([-1.2, 0, y], cx, cy, scale);
          let p2 = project3D([1.2, 0, y], cx, cy, scale);
          ctx.beginPath(); ctx.moveTo(p1[0], p1[1]); ctx.lineTo(p2[0], p2[1]); ctx.stroke();
        }
        // Straight line geodesic on plane
        let pA = project3D([-1.2 * Math.cos(launchAngle), 0, -1.2 * Math.sin(launchAngle)], cx, cy, scale);
        let pB = project3D([1.2 * Math.cos(launchAngle), 0, 1.2 * Math.sin(launchAngle)], cx, cy, scale);
        ctx.strokeStyle = "#8b5cf6"; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(pA[0], pA[1]); ctx.lineTo(pB[0], pB[1]); ctx.stroke();
      }

      // HUD
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Gauss's Theorema Egregium", 15, 25);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, monospace";
      if (spaceGeo === "sphere") {
        ctx.fillText("Sphere: K = 1/R² > 0 (Strictly curved intrinsically)", 15, 45);
        ctx.fillText("Geodesics are Great Circles (Shortest paths on sphere)", 15, 62);
      } else if (spaceGeo === "cylinder") {
        ctx.fillText("Cylinder: K = 0 (Locally isometric to Euclidean plane!)", 15, 45);
        ctx.fillText("Geodesics are Helices (Unroll into straight lines on flat sheet)", 15, 62);
      } else {
        ctx.fillText("Plane: K = 0 (Flat Euclidean geometry)", 15, 45);
        ctx.fillText("Geodesics are Straight Lines", 15, 62);
      }
      ctx.fillText("Brioschi's Formula: K depends solely on E, F, G and their derivatives", 15, 82);
    }

    render();
  }
};
''';

    with open("differential-geometry-sims.js", "w", encoding="utf-8") as f:
        f.write(js_code)

    print("Successfully generated differential-geometry-sims.js with all 8 real-time simulations.")

if __name__ == "__main__":
    generate_sims()
