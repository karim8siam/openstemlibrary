// General Topology Interactive Computational Simulations Engine
// High-performance 60 FPS HTML5 Canvas models registered to window.SIMULATIONS

window.SIMULATIONS = window.SIMULATIONS || {};

// 1. Unit 1: Metric Balls in L^p Spaces & Cauchy Sequences
window.SIMULATIONS["sim_top_metric_balls_p"] = {
  title: "Metric Balls in L^p Spaces & Cauchy Sequences Visualizer",
  description: "Explore how the unit ball { (x,y) : (|x|^p + |y|^p)^(1/p) <= 1 } deforms across p in [0.5, inf], illustrating non-convexity for p < 1, the taxicab diamond (p=1), Euclidean disk (p=2), and supremum square (p=inf).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let pVal = 2.0;
    let isInf = false;
    let showSequence = true;
    let animT = 0;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Norm Parameter p:</label>
        <input type="range" id="top-p-slider" min="0.5" max="8.0" step="0.1" value="2.0" style="vertical-align: middle; width: 100px;">
        <span id="top-p-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">p = 2.0 (Euclidean)</span>
        <button id="btn-top-p-inf" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">p = ∞ (Max Norm)</button>
        <button id="btn-top-p-seq" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Toggle Cauchy Sequence</button>
      `;

      const pSlider = document.getElementById("top-p-slider");
      const pValSpan = document.getElementById("top-p-val");
      const btnInf = document.getElementById("btn-top-p-inf");
      const btnSeq = document.getElementById("btn-top-p-seq");

      pSlider.oninput = (e) => {
        isInf = false;
        pVal = parseFloat(e.target.value);
        let label = `p = ${pVal.toFixed(1)}`;
        if (Math.abs(pVal - 1.0) < 0.05) label += " (Taxicab / L1)";
        else if (Math.abs(pVal - 2.0) < 0.05) label += " (Euclidean / L2)";
        else if (pVal < 1.0) label += " (Non-convex quasi-norm)";
        pValSpan.innerText = label;
      };

      btnInf.onclick = () => {
        isInf = !isInf;
        btnInf.style.background = isInf ? "#38bdf8" : "";
        btnInf.style.color = isInf ? "#0f172a" : "";
        pValSpan.innerText = isInf ? "p = ∞ (Chebyshev / Supremum)" : `p = ${pVal.toFixed(1)}`;
      };

      btnSeq.onclick = () => {
        showSequence = !showSequence;
      };
    }

    let animId;
    function render() {
      animT += 0.02;
      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      // Background grid
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      const cx = w * 0.45;
      const cy = h * 0.5;
      const scale = Math.min(w, h) * 0.32;

      // Coordinate axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(cx - scale * 1.5, cy);
      ctx.lineTo(cx + scale * 1.5, cy);
      ctx.moveTo(cx, cy - scale * 1.4);
      ctx.lineTo(cx, cy + scale * 1.4);
      ctx.stroke();

      // Axis ticks (+1, -1)
      ctx.fillStyle = "#64748b";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("+1", cx + scale - 5, cy + 16);
      ctx.fillText("-1", cx - scale - 12, cy + 16);
      ctx.fillText("+1", cx + 8, cy - scale + 5);
      ctx.fillText("-1", cx + 8, cy + scale + 5);

      // Draw Unit Ball boundary
      ctx.beginPath();
      const numPts = 360;
      for (let i = 0; i <= numPts; i++) {
        const theta = (i / numPts) * 2 * Math.PI;
        const cosT = Math.cos(theta);
        const sinT = Math.sin(theta);

        let r;
        if (isInf) {
          r = 1.0 / Math.max(Math.abs(cosT), Math.abs(sinT));
        } else {
          const denom = Math.pow(Math.abs(cosT), pVal) + Math.pow(Math.abs(sinT), pVal);
          r = Math.pow(denom, -1.0 / pVal);
        }

        const px = cx + r * cosT * scale;
        const py = cy - r * sinT * scale;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.closePath();

      // Shaded ball interior
      ctx.fillStyle = pVal < 1.0 && !isInf ? "rgba(239, 68, 68, 0.15)" : "rgba(56, 189, 248, 0.18)";
      ctx.fill();

      // Perimeter stroke
      ctx.strokeStyle = pVal < 1.0 && !isInf ? "#ef4444" : "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // Draw Cauchy sequence spiraling to target (0.5, 0.5)
      if (showSequence) {
        const targetX = 0.45;
        const targetY = 0.45;
        ctx.strokeStyle = "rgba(245, 158, 11, 0.5)";
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let k = 1; k <= 25; k++) {
          const tOffset = animT + k * 0.4;
          const decay = Math.exp(-k * 0.15);
          const xk = targetX + decay * Math.cos(tOffset);
          const yk = targetY + decay * Math.sin(tOffset);
          const sx = cx + xk * scale;
          const sy = cy - yk * scale;

          if (k === 1) ctx.moveTo(sx, sy);
          else ctx.lineTo(sx, sy);

          // Draw sequence dot
          ctx.fillStyle = k > 18 ? "#10b981" : "#f59e0b";
          ctx.beginPath();
          ctx.arc(sx, sy, Math.max(2, 5 - k * 0.12), 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.stroke();

        // Limit point
        const limX = cx + targetX * scale;
        const limY = cy - targetY * scale;
        ctx.fillStyle = "#10b981";
        ctx.beginPath();
        ctx.arc(limX, limY, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#e2e8f0";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText("x* = lim x_k", limX + 8, limY - 4);
      }

      // Legend panel on right
      const rx = w * 0.72;
      ctx.fillStyle = "rgba(30, 41, 59, 0.85)";
      ctx.fillRect(rx, 20, w - rx - 15, h - 40);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 20, w - rx - 15, h - 40);

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("L^p Metric Ball Geometry", rx + 14, 45);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Ball: B(0, 1) = { x : ||x||_p ≤ 1 }", rx + 14, 70);

      ctx.fillStyle = "#38bdf8";
      if (isInf) {
        ctx.fillText("p = ∞: ||x||_∞ = max(|x|, |y|)", rx + 14, 95);
        ctx.fillText("Square boundary (Chebyshev)", rx + 14, 115);
      } else if (pVal < 1.0) {
        ctx.fillStyle = "#ef4444";
        ctx.fillText(`p = ${pVal.toFixed(1)} < 1: Non-convex!`, rx + 14, 95);
        ctx.fillText("Fails triangle inequality d(x,y)", rx + 14, 115);
      } else if (Math.abs(pVal - 1.0) < 0.05) {
        ctx.fillText("p = 1: ||x||_1 = |x| + |y|", rx + 14, 95);
        ctx.fillText("Rhombus / Taxicab Metric", rx + 14, 115);
      } else if (Math.abs(pVal - 2.0) < 0.05) {
        ctx.fillText("p = 2: Euclidean Disk √(x² + y²)", rx + 14, 95);
        ctx.fillText("Rotational invariance & Hilbert norm", rx + 14, 115);
      } else {
        ctx.fillText(`p = ${pVal.toFixed(1)}: Rounded super-ellipse`, rx + 14, 95);
        ctx.fillText("Convex unit ball (Minkowski)", rx + 14, 115);
      }

      ctx.fillStyle = "#f59e0b";
      ctx.fillText("Cauchy Sequence (Green limit):", rx + 14, 150);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText("d_p(x_m, x_n) → 0 as m, n → ∞", rx + 14, 170);
      ctx.fillText("Every Cauchy sequence converges", rx + 14, 190);
      ctx.fillText("⇒ (R², d_p) is COMPLETE.", rx + 14, 210);

      animId = requestAnimationFrame(render);
    }
    render();
  }
};

// 2. Unit 2: Closure, Interior, Boundary & Derived Set Visualizer
window.SIMULATIONS["sim_top_closure_interior_boundary"] = {
  title: "Set Topology: Interior, Closure & Boundary Explorer",
  description: "Examine subsets of R² and dynamically classify points into Interior (int A), Boundary (∂A), and Exterior (ext A), illustrating the Kuratowski topological closure axioms.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let activeSet = "annulus"; // 'disk', 'annulus', 'square_slit', 'cantor'
    let mouseX = -1, mouseY = -1;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Select Topological Set A:</label>
        <button id="btn-top-set-disk" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Half-Open Disk</button>
        <button id="btn-top-set-annulus" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Open Annulus</button>
        <button id="btn-top-set-slit" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Square with Slit</button>
      `;

      document.getElementById("btn-top-set-disk").onclick = () => { activeSet = "disk"; };
      document.getElementById("btn-top-set-annulus").onclick = () => { activeSet = "annulus"; };
      document.getElementById("btn-top-set-slit").onclick = () => { activeSet = "square_slit"; };
    }

    canvas.onmousemove = (e) => {
      const rect = canvas.getBoundingClientRect();
      mouseX = e.clientX - rect.left;
      mouseY = e.clientY - rect.top;
    };

    let animId;
    function render() {
      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      const cx = w * 0.42;
      const cy = h * 0.5;

      // Coordinate axes
      ctx.strokeStyle = "#1e293b";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(30, cy); ctx.lineTo(w * 0.75, cy);
      ctx.moveTo(cx, 30); ctx.lineTo(cx, h - 30);
      ctx.stroke();

      let inInterior = false, onBoundary = false;

      if (activeSet === "disk") {
        const R = 110;
        // Interior
        ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
        ctx.beginPath();
        ctx.arc(cx, cy, R, 0, Math.PI * 2);
        ctx.fill();

        // Boundary: top half solid (included in A), bottom half dashed (excluded)
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(cx, cy, R, Math.PI, 0); // top half included
        ctx.stroke();

        ctx.setLineDash([6, 6]);
        ctx.strokeStyle = "#f59e0b";
        ctx.beginPath();
        ctx.arc(cx, cy, R, 0, Math.PI); // bottom half excluded
        ctx.stroke();
        ctx.setLineDash([]);

        // Mouse hit test
        if (mouseX > 0) {
          const d = Math.hypot(mouseX - cx, mouseY - cy);
          if (d < R - 5) inInterior = true;
          else if (Math.abs(d - R) <= 7) onBoundary = true;
        }
      } else if (activeSet === "annulus") {
        const r1 = 55, r2 = 125;
        ctx.fillStyle = "rgba(56, 189, 248, 0.22)";
        ctx.beginPath();
        ctx.arc(cx, cy, r2, 0, Math.PI * 2);
        ctx.arc(cx, cy, r1, 0, Math.PI * 2, true);
        ctx.fill();

        // Dashed boundaries (open annulus has boundary disjoint from A)
        ctx.setLineDash([5, 5]);
        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(cx, cy, r1, 0, Math.PI * 2);
        ctx.arc(cx, cy, r2, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);

        if (mouseX > 0) {
          const d = Math.hypot(mouseX - cx, mouseY - cy);
          if (d > r1 + 5 && d < r2 - 5) inInterior = true;
          else if (Math.abs(d - r1) <= 7 || Math.abs(d - r2) <= 7) onBoundary = true;
        }
      } else if (activeSet === "square_slit") {
        const side = 180;
        const x0 = cx - side / 2, y0 = cy - side / 2;
        ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
        ctx.fillRect(x0, y0, side, side);

        // Slit cut out
        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(cx + side / 2, cy);
        ctx.stroke();

        ctx.strokeStyle = "#38bdf8";
        ctx.strokeRect(x0, y0, side, side);

        if (mouseX > 0) {
          if (mouseX > x0 + 5 && mouseX < x0 + side - 5 && mouseY > y0 + 5 && mouseY < y0 + side - 5) {
            if (Math.abs(mouseY - cy) <= 4 && mouseX >= cx && mouseX <= x0 + side) onBoundary = true;
            else inInterior = true;
          } else if (mouseX >= x0 - 5 && mouseX <= x0 + side + 5 && mouseY >= y0 - 5 && mouseY <= y0 + side + 5) {
            onBoundary = true;
          }
        }
      }

      // Cursor neighborhood circle
      if (mouseX > 0 && mouseX < w * 0.75) {
        ctx.strokeStyle = inInterior ? "#38bdf8" : (onBoundary ? "#f59e0b" : "#64748b");
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(mouseX, mouseY, 18, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = inInterior ? "#38bdf8" : (onBoundary ? "#f59e0b" : "#94a3b8");
        ctx.beginPath();
        ctx.arc(mouseX, mouseY, 3.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // Information & Legend Panel
      const rx = w * 0.74;
      ctx.fillStyle = "rgba(30, 41, 59, 0.9)";
      ctx.fillRect(rx, 20, w - rx - 15, h - 40);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 20, w - rx - 15, h - 40);

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Topological Set Decomposition", rx + 14, 45);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "12px Inter, sans-serif";
      ctx.fillText("■ Interior int(A):", rx + 14, 75);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Points with open ball B(x, ε) ⊆ A", rx + 14, 95);

      ctx.fillStyle = "#f59e0b";
      ctx.font = "12px Inter, sans-serif";
      ctx.fillText("■ Boundary ∂A:", rx + 14, 125);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Every ball intersects both A and Aᶜ", rx + 14, 145);
      ctx.fillText("∂A = cl(A) \\ int(A)", rx + 14, 165);

      ctx.fillStyle = "#10b981";
      ctx.font = "12px Inter, sans-serif";
      ctx.fillText("■ Closure cl(A):", rx + 14, 195);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("cl(A) = int(A) ∪ ∂A = A ∪ A'", rx + 14, 215);

      // Current Point Status
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Cursor Probe Status:", rx + 14, 255);

      let statusText = "Outside (Exterior ext A)";
      let statusColor = "#94a3b8";
      if (inInterior) { statusText = "Point x ∈ int(A)"; statusColor = "#38bdf8"; }
      else if (onBoundary) { statusText = "Point x ∈ ∂A (Boundary)"; statusColor = "#f59e0b"; }

      ctx.fillStyle = statusColor;
      ctx.font = "bold 13px monospace";
      ctx.fillText(statusText, rx + 14, 280);

      animId = requestAnimationFrame(render);
    }
    render();
  }
};

// 3. Unit 3: 3D Quotient Surfaces Visualizer (Cylinder, Möbius, Torus, Klein)
window.SIMULATIONS["sim_top_quotient_surfaces"] = {
  title: "Quotient Topology: 3D Identification Surfaces Visualizer",
  description: "Examine the quotient identification maps on the unit square I²: cylinder, non-orientable Möbius strip, torus T², and the 4D Klein bottle immersed in 3D.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let currentSurface = "mobius"; // 'cylinder', 'mobius', 'torus', 'klein'
    let rotX = 0.5, rotY = 0.6;
    let isDragging = false, lastMouseX = 0, lastMouseY = 0;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Quotient Space I² / ~ :</label>
        <button id="btn-top-surf-cyl" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Cylinder</button>
        <button id="btn-top-surf-mob" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Möbius Strip</button>
        <button id="btn-top-surf-tor" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Torus T²</button>
        <button id="btn-top-surf-klein" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Klein Bottle</button>
      `;

      document.getElementById("btn-top-surf-cyl").onclick = () => { currentSurface = "cylinder"; };
      document.getElementById("btn-top-surf-mob").onclick = () => { currentSurface = "mobius"; };
      document.getElementById("btn-top-surf-tor").onclick = () => { currentSurface = "torus"; };
      document.getElementById("btn-top-surf-klein").onclick = () => { currentSurface = "klein"; };
    }

    canvas.onmousedown = (e) => {
      isDragging = true;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
    };
    window.onmouseup = () => { isDragging = false; };
    canvas.onmousemove = (e) => {
      if (isDragging) {
        const dx = e.clientX - lastMouseX;
        const dy = e.clientY - lastMouseY;
        rotY += dx * 0.01;
        rotX += dy * 0.01;
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;
      }
    };

    function project(x, y, z, cx, cy, scale) {
      // 3D rotation
      const cosY = Math.cos(rotY), sinY = Math.sin(rotY);
      const x1 = x * cosY - z * sinY;
      const z1 = x * sinY + z * cosY;

      const cosX = Math.cos(rotX), sinX = Math.sin(rotX);
      const y2 = y * cosX - z1 * sinX;
      const z2 = y * sinX + z1 * cosX;

      const fov = 400;
      const dist = fov / (fov + z2 + 180);
      return {
        px: cx + x1 * scale * dist,
        py: cy - y2 * scale * dist,
        z: z2
      };
    }

    let animId;
    function render() {
      if (!isDragging) rotY += 0.006;
      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      const cx = w * 0.42;
      const cy = h * 0.5;

      const uSteps = 45, vSteps = 22;
      const grid = [];

      for (let i = 0; i <= uSteps; i++) {
        const u = (i / uSteps) * 2 * Math.PI; // [0, 2pi]
        const row = [];
        for (let j = 0; j <= vSteps; j++) {
          const v = (j / vSteps) - 0.5; // [-0.5, 0.5]

          let x, y, z;
          if (currentSurface === "cylinder") {
            const r = 85;
            x = r * Math.cos(u);
            z = r * Math.sin(u);
            y = v * 150;
          } else if (currentSurface === "mobius") {
            const R = 85, wWidth = 45;
            x = (R + v * wWidth * Math.cos(u / 2)) * Math.cos(u);
            y = (R + v * wWidth * Math.cos(u / 2)) * Math.sin(u);
            z = v * wWidth * Math.sin(u / 2);
          } else if (currentSurface === "torus") {
            const R = 90, r = 38;
            const phi = (j / vSteps) * 2 * Math.PI;
            x = (R + r * Math.cos(phi)) * Math.cos(u);
            z = (R + r * Math.cos(phi)) * Math.sin(u);
            y = r * Math.sin(phi);
          } else if (currentSurface === "klein") {
            const v2 = (j / vSteps) * 2 * Math.PI;
            const a = 55;
            if (u < Math.PI) {
              x = 3 * Math.cos(u) * (1 + Math.sin(u)) + (2 * (1 - Math.cos(u) / 2)) * Math.cos(u) * Math.cos(v2);
              z = -8 * Math.sin(u) - 2 * (1 - Math.cos(u) / 2) * Math.sin(u) * Math.cos(v2);
            } else {
              x = 3 * Math.cos(u) * (1 + Math.sin(u)) + (2 * (1 - Math.cos(u) / 2)) * Math.cos(v2 + Math.PI);
              z = -8 * Math.sin(u);
            }
            y = 2 * (1 - Math.cos(u) / 2) * Math.sin(v2);
            x *= 11; y *= 18; z *= 11;
          }
          row.push(project(x, y, z, cx, cy, 1.0));
        }
        grid.push(row);
      }

      // Draw wireframe patches
      ctx.lineWidth = 1.0;
      for (let i = 0; i < uSteps; i++) {
        for (let j = 0; j < vSteps; j++) {
          const p1 = grid[i][j];
          const p2 = grid[i + 1][j];
          const p3 = grid[i + 1][j + 1];
          const p4 = grid[i][j + 1];

          const avgZ = (p1.z + p2.z + p3.z + p4.z) / 4;
          const alpha = Math.max(0.12, Math.min(0.85, (avgZ + 120) / 240));

          ctx.fillStyle = currentSurface === "mobius" ? `rgba(245, 158, 11, ${alpha * 0.4})` :
                          (currentSurface === "klein" ? `rgba(239, 68, 68, ${alpha * 0.4})` : `rgba(56, 189, 248, ${alpha * 0.4})`);
          ctx.strokeStyle = currentSurface === "mobius" ? `rgba(245, 158, 11, ${alpha * 0.9})` :
                            (currentSurface === "klein" ? `rgba(239, 68, 68, ${alpha * 0.9})` : `rgba(56, 189, 248, ${alpha * 0.9})`);

          ctx.beginPath();
          ctx.moveTo(p1.px, p1.py);
          ctx.lineTo(p2.px, p2.py);
          ctx.lineTo(p3.px, p3.py);
          ctx.lineTo(p4.px, p4.py);
          ctx.closePath();
          ctx.fill();
          ctx.stroke();
        }
      }

      // Information Panel
      const rx = w * 0.74;
      ctx.fillStyle = "rgba(30, 41, 59, 0.9)";
      ctx.fillRect(rx, 20, w - rx - 15, h - 40);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 20, w - rx - 15, h - 40);

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Quotient Topology Model", rx + 14, 45);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Square I² = [0,1] × [0,1] / ~", rx + 14, 68);

      if (currentSurface === "cylinder") {
        ctx.fillStyle = "#38bdf8";
        ctx.fillText("Cylinder:", rx + 14, 98);
        ctx.fillStyle = "#cbd5e1";
        ctx.fillText("(0, y) ~ (1, y)", rx + 14, 118);
        ctx.fillText("Orientable 2-manifold with boundary.", rx + 14, 138);
      } else if (currentSurface === "mobius") {
        ctx.fillStyle = "#f59e0b";
        ctx.fillText("Möbius Strip:", rx + 14, 98);
        ctx.fillStyle = "#cbd5e1";
        ctx.fillText("(0, y) ~ (1, 1 - y)", rx + 14, 118);
        ctx.fillText("Non-orientable, 1-sided surface.", rx + 14, 138);
        ctx.fillText("Euler characteristic χ = 0.", rx + 14, 158);
      } else if (currentSurface === "torus") {
        ctx.fillStyle = "#38bdf8";
        ctx.fillText("Torus T² = S¹ × S¹:", rx + 14, 98);
        ctx.fillStyle = "#cbd5e1";
        ctx.fillText("(0, y) ~ (1, y) and (x, 0) ~ (x, 1)", rx + 14, 118);
        ctx.fillText("Compact orientable surface, χ = 0.", rx + 14, 138);
      } else if (currentSurface === "klein") {
        ctx.fillStyle = "#ef4444";
        ctx.fillText("Klein Bottle K²:", rx + 14, 98);
        ctx.fillStyle = "#cbd5e1";
        ctx.fillText("(0, y) ~ (1, 1 - y)", rx + 14, 118);
        ctx.fillText("and (x, 0) ~ (x, 1)", rx + 14, 138);
        ctx.fillText("Closed non-orientable surface.", rx + 14, 158);
        ctx.fillText("Self-intersecting immersion in R³.", rx + 14, 178);
      }

      ctx.fillStyle = "#64748b";
      ctx.fillText("Tip: Click & drag to rotate 3D view.", rx + 14, h - 35);

      animId = requestAnimationFrame(render);
    }
    render();
  }
};

// 4. Unit 4: Countability Hierarchy & Sorgenfrey Counterexamples
window.SIMULATIONS["sim_top_countability_hierarchy"] = {
  title: "Countability Hierarchy & Sorgenfrey Line Explorer",
  description: "Examine the implications between 1st-Countable, 2nd-Countable, Separable, and Lindelöf spaces, visualizing why the Sorgenfrey Line R_l and Sorgenfrey Plane fail product Lindelöf preservation.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let selectedSpace = "sorgenfrey"; // 'euclidean', 'sorgenfrey', 'sorgenfrey_plane', 'discrete_uncountable'

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Topological Space:</label>
        <button id="btn-top-sp-euc" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Euclidean R^n</button>
        <button id="btn-top-sp-sorg" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Sorgenfrey Line R_l</button>
        <button id="btn-top-sp-plane" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Sorgenfrey Plane R_l²</button>
        <button id="btn-top-sp-disc" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Uncountable Discrete</button>
      `;

      document.getElementById("btn-top-sp-euc").onclick = () => { selectedSpace = "euclidean"; render(); };
      document.getElementById("btn-top-sp-sorg").onclick = () => { selectedSpace = "sorgenfrey"; render(); };
      document.getElementById("btn-top-sp-plane").onclick = () => { selectedSpace = "sorgenfrey_plane"; render(); };
      document.getElementById("btn-top-sp-disc").onclick = () => { selectedSpace = "discrete_uncountable"; render(); };
    }

    function render() {
      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      // Draw Countability Implications Flowchart
      const cx = w * 0.38;
      const cy = h * 0.45;

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText("Topological Countability Axioms Hierarchy", 30, 35);

      // Node coordinates
      const nodes = {
        second: { x: cx - 110, y: cy - 90, label: "2nd-Countable (C2)", sub: "Countable Base B" },
        first: { x: cx - 210, y: cy + 40, label: "1st-Countable (C1)", sub: "Countable Local Base" },
        separable: { x: cx - 10, y: cy + 40, label: "Separable (S)", sub: "Countable Dense Set D" },
        lindelof: { x: cx + 110, y: cy - 90, label: "Lindelöf (L)", sub: "Countable Subcover" }
      };

      // Draw arrows C2 -> C1, C2 -> S, C2 -> L
      function drawArrow(x1, y1, x2, y2, color) {
        ctx.strokeStyle = color;
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();

        const angle = Math.atan2(y2 - y1, x2 - x1);
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.moveTo(x2, y2);
        ctx.lineTo(x2 - 10 * Math.cos(angle - 0.4), y2 - 10 * Math.sin(angle - 0.4));
        ctx.lineTo(x2 - 10 * Math.cos(angle + 0.4), y2 - 10 * Math.sin(angle + 0.4));
        ctx.closePath();
        ctx.fill();
      }

      drawArrow(nodes.second.x, nodes.second.y + 20, nodes.first.x + 30, nodes.first.y - 20, "#38bdf8");
      drawArrow(nodes.second.x + 20, nodes.second.y + 20, nodes.separable.x - 20, nodes.separable.y - 20, "#38bdf8");
      drawArrow(nodes.second.x + 70, nodes.second.y, nodes.lindelof.x - 70, nodes.lindelof.y, "#38bdf8");

      // Evaluation for selected space
      let status = { C1: false, C2: false, S: false, L: false };
      if (selectedSpace === "euclidean") { status = { C1: true, C2: true, S: true, L: true }; }
      else if (selectedSpace === "sorgenfrey") { status = { C1: true, C2: false, S: true, L: true }; }
      else if (selectedSpace === "sorgenfrey_plane") { status = { C1: true, C2: false, S: true, L: false }; }
      else if (selectedSpace === "discrete_uncountable") { status = { C1: true, C2: false, S: false, L: false }; }

      // Draw Nodes
      Object.keys(nodes).forEach(key => {
        const n = nodes[key];
        const isSatisfied = (key === "first" && status.C1) || (key === "second" && status.C2) ||
                            (key === "separable" && status.S) || (key === "lindelof" && status.L);

        const nw = 140, nh = 50;
        ctx.fillStyle = isSatisfied ? "rgba(16, 185, 129, 0.2)" : "rgba(239, 68, 68, 0.18)";
        ctx.strokeStyle = isSatisfied ? "#10b981" : "#ef4444";
        ctx.lineWidth = 2;
        ctx.fillRect(n.x - nw / 2, n.y - nh / 2, nw, nh);
        ctx.strokeRect(n.x - nw / 2, n.y - nh / 2, nw, nh);

        ctx.fillStyle = isSatisfied ? "#34d399" : "#f87171";
        ctx.font = "bold 11px Inter, sans-serif";
        ctx.textAlign = "center";
        ctx.fillText((isSatisfied ? "✓ " : "✗ ") + n.label, n.x, n.y - 4);
        ctx.fillStyle = "#94a3b8";
        ctx.font = "10px Inter, sans-serif";
        ctx.fillText(n.sub, n.x, n.y + 14);
        ctx.textAlign = "left";
      });

      // Geometric Demonstration: Sorgenfrey Half-Open Basis [x, x+ε)
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(30, h - 110, cx * 1.5, 95);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(30, h - 110, cx * 1.5, 95);

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Basis Elements: Standard Topology vs Lower Limit Topology (R_l)", 45, h - 85);

      const ax = 55, ay = h - 45;
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(ax, ay); ctx.lineTo(ax + 200, ay);
      ctx.moveTo(ax + 240, ay); ctx.lineTo(ax + 440, ay);
      ctx.stroke();

      // Standard (a, b)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.arc(ax + 50, ay, 4, 0, Math.PI * 2);
      ctx.arc(ax + 150, ay, 4, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ax + 54, ay); ctx.lineTo(ax + 146, ay); ctx.stroke();
      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px monospace";
      ctx.fillText("(a, b) Open Interval", ax + 55, ay - 12);

      // Sorgenfrey [x, x + ε)
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 3;
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(ax + 290, ay, 4, 0, Math.PI * 2);
      ctx.fill();
      ctx.beginPath();
      ctx.arc(ax + 390, ay, 4, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ax + 290, ay); ctx.lineTo(ax + 386, ay); ctx.stroke();
      ctx.fillText("[x, x + ε) Half-Open Clopen", ax + 285, ay - 12);

      // Sidebar Inspection
      const rx = w * 0.72;
      ctx.fillStyle = "rgba(30, 41, 59, 0.9)";
      ctx.fillRect(rx, 20, w - rx - 15, h - 40);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 20, w - rx - 15, h - 40);

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Selected Space Audit", rx + 14, 45);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      let nameStr = "Euclidean Space R^n";
      if (selectedSpace === "sorgenfrey") nameStr = "Sorgenfrey Line (R_l)";
      else if (selectedSpace === "sorgenfrey_plane") nameStr = "Sorgenfrey Plane (R_l × R_l)";
      else if (selectedSpace === "discrete_uncountable") nameStr = "Uncountable Discrete Space";
      ctx.fillText(nameStr, rx + 14, 72);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Inter, sans-serif";
      if (selectedSpace === "sorgenfrey") {
        ctx.fillText("• 1st-Countable: { [x, x + 1/n) } local base.", rx + 14, 98);
        ctx.fillText("• Separable: Q is dense in R_l.", rx + 14, 118);
        ctx.fillText("• Lindelöf: Every open cover has subcover.", rx + 14, 138);
        ctx.fillStyle = "#ef4444";
        ctx.fillText("• NOT 2nd-Countable: Any base must be", rx + 14, 162);
        ctx.fillText("  uncountable (distinct lower endpoints).", rx + 14, 180);
      } else if (selectedSpace === "sorgenfrey_plane") {
        ctx.fillText("• Product of two Lindelöf spaces R_l.", rx + 14, 98);
        ctx.fillStyle = "#ef4444";
        ctx.fillText("• NOT Lindelöf! The anti-diagonal", rx + 14, 125);
        ctx.fillText("  Δ = { (x, -x) : x ∈ R } is a discrete", rx + 14, 145);
        ctx.fillText("  uncountable closed subspace.", rx + 14, 165);
        ctx.fillText("  Fails Lindelöf product preservation!", rx + 14, 185);
      } else if (selectedSpace === "euclidean") {
        ctx.fillStyle = "#10b981";
        ctx.fillText("• Satisfies ALL 4 countability axioms.", rx + 14, 98);
        ctx.fillText("• Rational balls B(q, r) with q ∈ Q^n,", rx + 14, 118);
        ctx.fillText("  r ∈ Q form a countable base.", rx + 14, 138);
      } else {
        ctx.fillText("• Discrete topology on uncountable X.", rx + 14, 98);
        ctx.fillText("• 1st-Countable (local base {x}).", rx + 14, 118);
        ctx.fillStyle = "#ef4444";
        ctx.fillText("• Fails 2nd-Countable, Separable, and Lindelöf.", rx + 14, 142);
      }
    }
    render();
  }
};

// 5. Unit 5: Separation Axioms T0, T1, T2 (Hausdorff) & T3 (Regular)
window.SIMULATIONS["sim_top_separation_axioms"] = {
  title: "Separation Axioms: T0, T1, T2 (Hausdorff) & T3 Visualizer",
  description: "Examine how increasing separation axioms distinguish points and closed sets via open neighborhoods, preventing sequence limit bifurcation and ensuring Hausdorff diagonal closure.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let activeAxiom = "T2"; // 'T0', 'T1', 'T2', 'T3'
    let animPulse = 0;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Separation Axiom:</label>
        <button id="btn-top-t0" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">T0 (Kolmogorov)</button>
        <button id="btn-top-t1" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">T1 (Fréchet)</button>
        <button id="btn-top-t2" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; background: #38bdf8; color: #0f172a;">T2 (Hausdorff)</button>
        <button id="btn-top-t3" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">T3 (Regular)</button>
      `;

      const setBtn = (id, ax) => {
        ['btn-top-t0', 'btn-top-t1', 'btn-top-t2', 'btn-top-t3'].forEach(b => {
          document.getElementById(b).style.background = "";
          document.getElementById(b).style.color = "";
        });
        document.getElementById(id).style.background = "#38bdf8";
        document.getElementById(id).style.color = "#0f172a";
        activeAxiom = ax;
      };

      document.getElementById("btn-top-t0").onclick = () => setBtn("btn-top-t0", "T0");
      document.getElementById("btn-top-t1").onclick = () => setBtn("btn-top-t1", "T1");
      document.getElementById("btn-top-t2").onclick = () => setBtn("btn-top-t2", "T2");
      document.getElementById("btn-top-t3").onclick = () => setBtn("btn-top-t3", "T3");
    }

    let animId;
    function render() {
      animPulse += 0.03;
      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      const cx = w * 0.40;
      const cy = h * 0.5;

      const p1 = { x: cx - 110, y: cy };
      const p2 = { x: cx + 110, y: cy };
      const pulseR = Math.sin(animPulse) * 4;

      if (activeAxiom === "T0") {
        // T0: One open set U contains p1 but not p2
        ctx.fillStyle = "rgba(56, 189, 248, 0.2)";
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(p1.x, p1.y, 70 + pulseR, 0, Math.PI * 2);
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText("Open Set U (x ∈ U, y ∉ U)", p1.x - 70, p1.y - 80);
      } else if (activeAxiom === "T1") {
        // T1: U contains p1 without p2, V contains p2 without p1 (may overlap!)
        ctx.fillStyle = "rgba(56, 189, 248, 0.18)";
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(p1.x, p1.y, 140, 0, Math.PI * 2);
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "rgba(245, 158, 11, 0.18)";
        ctx.strokeStyle = "#f59e0b";
        ctx.beginPath();
        ctx.arc(p2.x, p2.y, 140, 0, Math.PI * 2);
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText("U (x ∈ U, y ∉ U)", p1.x - 110, p1.y - 145);
        ctx.fillStyle = "#f59e0b";
        ctx.fillText("V (y ∈ V, x ∉ V)", p2.x + 10, p2.y - 145);
        ctx.fillStyle = "#94a3b8";
        ctx.fillText("Note: U ∩ V ≠ ∅ is permitted in T1!", cx - 90, cy + 120);
      } else if (activeAxiom === "T2") {
        // T2: Disjoint open sets U and V (Hausdorff)
        const rad = 85 + pulseR;
        ctx.fillStyle = "rgba(56, 189, 248, 0.22)";
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(p1.x, p1.y, rad, 0, Math.PI * 2);
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "rgba(16, 185, 129, 0.22)";
        ctx.strokeStyle = "#10b981";
        ctx.beginPath();
        ctx.arc(p2.x, p2.y, rad, 0, Math.PI * 2);
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText("Neighborhood U(x)", p1.x - 55, p1.y - rad - 12);
        ctx.fillStyle = "#10b981";
        ctx.fillText("Neighborhood V(y)", p2.x - 55, p2.y - rad - 12);

        ctx.fillStyle = "#f8fafc";
        ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText("U ∩ V = ∅ (DISJOINT!)", cx - 75, cy + rad + 35);
      } else if (activeAxiom === "T3") {
        // T3: Point x and closed set F separated by disjoint open sets
        const rad1 = 65 + pulseR;
        ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(p1.x, p1.y, rad1, 0, Math.PI * 2);
        ctx.fill(); ctx.stroke();

        // Closed set F inside open V
        ctx.fillStyle = "rgba(168, 85, 247, 0.2)";
        ctx.strokeStyle = "#a855f7";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.roundRect(p2.x - 65, cy - 90, 130, 180, 20);
        ctx.fill(); ctx.stroke();

        // Solid Closed Set F inside
        ctx.fillStyle = "rgba(239, 68, 68, 0.4)";
        ctx.strokeStyle = "#ef4444";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.roundRect(p2.x - 40, cy - 60, 80, 120, 10);
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText("Open U ∋ x", p1.x - 35, p1.y - rad1 - 12);
        ctx.fillStyle = "#a855f7";
        ctx.fillText("Open V ⊇ F", p2.x - 30, cy - 100);
        ctx.fillStyle = "#ef4444";
        ctx.fillText("Closed Set F", p2.x - 35, cy);
      }

      // Draw Points
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(p1.x, p1.y, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("x", p1.x - 4, p1.y - 12);

      if (activeAxiom !== "T3") {
        ctx.fillStyle = activeAxiom === "T2" ? "#10b981" : "#f59e0b";
        ctx.beginPath(); ctx.arc(p2.x, p2.y, 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#f8fafc";
        ctx.fillText("y", p2.x - 4, p2.y - 12);
      }

      // Information Panel
      const rx = w * 0.72;
      ctx.fillStyle = "rgba(30, 41, 59, 0.9)";
      ctx.fillRect(rx, 20, w - rx - 15, h - 40);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 20, w - rx - 15, h - 40);

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Separation Properties", rx + 14, 45);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Current: ${activeAxiom} Space`, rx + 14, 72);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Inter, sans-serif";
      if (activeAxiom === "T0") {
        ctx.fillText("• Distinct points topologically distinguishable.", rx + 14, 98);
        ctx.fillText("• Example: Sierpiński space {0, 1}.", rx + 14, 118);
      } else if (activeAxiom === "T1") {
        ctx.fillText("• Each singleton {x} is CLOSED in X.", rx + 14, 98);
        ctx.fillText("• Points separated from each other.", rx + 14, 118);
        ctx.fillText("• Example: Co-finite topology on infinite X.", rx + 14, 138);
      } else if (activeAxiom === "T2") {
        ctx.fillStyle = "#10b981";
        ctx.fillText("• Hausdorff Property:", rx + 14, 98);
        ctx.fillStyle = "#cbd5e1";
        ctx.fillText("• Disjoint open neighborhoods U ∩ V = ∅.", rx + 14, 118);
        ctx.fillText("• Sequence limits are UNIQUE!", rx + 14, 138);
        ctx.fillText("• Diagonal Δ ⊆ X × X is CLOSED.", rx + 14, 158);
      } else if (activeAxiom === "T3") {
        ctx.fillText("• Regular + T1:", rx + 14, 98);
        ctx.fillText("• Points separated from closed sets.", rx + 14, 118);
        ctx.fillText("• Every point has a neighborhood base", rx + 14, 138);
        ctx.fillText("  of CLOSED sets.", rx + 14, 158);
      }

      animId = requestAnimationFrame(render);
    }
    render();
  }
};

// 6. Unit 6: Urysohn's Lemma Dyadic Step Potential
window.SIMULATIONS["sim_top_urysohn_dyadic_potential"] = {
  title: "Urysohn's Lemma: Dyadic Rational Potential Generator",
  description: "Visualize how Urysohn's Lemma constructs a continuous function f: X -> [0, 1] separating disjoint closed sets A and B via nested open sets indexed by dyadic rationals D_k = { m / 2^k }.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let dyadicK = 2; // k in 1..5, 2^k steps

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Dyadic Depth k (2^k steps):</label>
        <input type="range" id="top-dyadic-slider" min="1" max="5" step="1" value="2" style="vertical-align: middle; width: 100px;">
        <span id="top-dyadic-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">k = 2 (4 levels)</span>
      `;

      const slider = document.getElementById("top-dyadic-slider");
      const valSpan = document.getElementById("top-dyadic-val");
      slider.oninput = (e) => {
        dyadicK = parseInt(e.target.value);
        valSpan.innerText = `k = ${dyadicK} (${Math.pow(2, dyadicK)} levels)`;
        render();
      };
    }

    function render() {
      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      const plotX = 50;
      const plotY = 60;
      const plotW = w * 0.65;
      const plotH = h - 120;

      // Coordinate axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(plotX, plotY); ctx.lineTo(plotX, plotY + plotH);
      ctx.lineTo(plotX + plotW, plotY + plotH);
      ctx.stroke();

      // Labels
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Closed Set A (f = 0)", plotX + 15, plotY + plotH + 25);
      ctx.fillText("Closed Set B (f = 1)", plotX + plotW - 130, plotY + plotH + 25);
      ctx.fillText("f(x) = 1.0", plotX - 45, plotY + 10);
      ctx.fillText("f(x) = 0.0", plotX - 45, plotY + plotH);

      // Closed Sets A and B highlighted on domain
      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      ctx.fillRect(plotX, plotY, plotW * 0.2, plotH);
      ctx.fillStyle = "rgba(239, 68, 68, 0.25)";
      ctx.fillRect(plotX + plotW * 0.8, plotY, plotW * 0.2, plotH);

      // Draw Dyadic Staircase / Smooth Approximant
      const steps = Math.pow(2, dyadicK);
      const xStart = plotW * 0.2;
      const xEnd = plotW * 0.8;
      const stepWidth = (xEnd - xStart) / steps;

      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(plotX, plotY + plotH);
      ctx.lineTo(plotX + xStart, plotY + plotH);

      for (let s = 0; s < steps; s++) {
        const rVal = s / steps;
        const curX = plotX + xStart + s * stepWidth;
        const nextX = curX + stepWidth;
        const curY = plotY + plotH - rVal * plotH;

        ctx.lineTo(curX, curY);
        ctx.lineTo(nextX, curY);

        // Grid lines for dyadic values r
        ctx.setLineDash([3, 3]);
        ctx.strokeStyle = "rgba(148, 163, 184, 0.2)";
        ctx.beginPath();
        ctx.moveTo(plotX, curY); ctx.lineTo(plotX + plotW, curY);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.strokeStyle = "#f59e0b";
      }
      ctx.lineTo(plotX + plotW, plotY);
      ctx.stroke();

      // Smooth Limit Curve (k -> inf)
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let px = 0; px <= plotW; px++) {
        const xPos = plotX + px;
        let yVal;
        if (px < xStart) yVal = 0;
        else if (px > xEnd) yVal = 1;
        else {
          const t = (px - xStart) / (xEnd - xStart);
          // Smooth sigmoid curve
          yVal = (1 - Math.cos(t * Math.PI)) / 2;
        }
        const py = plotY + plotH - yVal * plotH;
        if (px === 0) ctx.moveTo(xPos, py);
        else ctx.lineTo(xPos, py);
      }
      ctx.stroke();

      // Info Panel
      const rx = w * 0.73;
      ctx.fillStyle = "rgba(30, 41, 59, 0.9)";
      ctx.fillRect(rx, 20, w - rx - 15, h - 40);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 20, w - rx - 15, h - 40);

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Urysohn's Lemma Derivation", rx + 14, 45);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("• In a normal (T4) space X:", rx + 14, 70);
      ctx.fillText("  Closed A, B disjoint.", rx + 14, 88);
      ctx.fillText("• Dyadic rationals D = { m/2^k }.", rx + 14, 110);
      ctx.fillText("• Construct open chain U_r:", rx + 14, 130);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText("  cl(U_r) ⊆ U_s  whenever r < s", rx + 14, 150);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText("• Define potential function:", rx + 14, 175);
      ctx.fillStyle = "#10b981";
      ctx.fillText("  f(x) = inf { r : x ∈ U_r }", rx + 14, 195);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText("• Continuous f: X → [0, 1] with", rx + 14, 220);
      ctx.fillText("  f(A) = 0 and f(B) = 1.", rx + 14, 240);
    }
    render();
  }
};

// 7. Unit 7: Compactness & Open Cover Extractor
window.SIMULATIONS["sim_top_compact_open_covers"] = {
  title: "Compactness: Finite Subcover & Lebesgue Number Visualizer",
  description: "Interactively explore Heine-Borel compactness on [0, 1] vs the non-compact open interval (0, 1), extracting finite subcovers and demonstrating the Lebesgue Covering Lemma.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let isCompact = true; // true = [0,1], false = (0,1) with (1/n, 1)
    let extracted = false;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Domain Set:</label>
        <button id="btn-top-comp-closed" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; background: #38bdf8; color: #0f172a;">Compact [0, 1]</button>
        <button id="btn-top-comp-open" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Non-Compact (0, 1)</button>
        <button id="btn-top-comp-subcover" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; margin-left: 0.5rem;">Extract Finite Subcover</button>
      `;

      document.getElementById("btn-top-comp-closed").onclick = () => {
        isCompact = true; extracted = false;
        document.getElementById("btn-top-comp-closed").style.background = "#38bdf8";
        document.getElementById("btn-top-comp-closed").style.color = "#0f172a";
        document.getElementById("btn-top-comp-open").style.background = "";
        document.getElementById("btn-top-comp-open").style.color = "";
        render();
      };

      document.getElementById("btn-top-comp-open").onclick = () => {
        isCompact = false; extracted = false;
        document.getElementById("btn-top-comp-open").style.background = "#ef4444";
        document.getElementById("btn-top-comp-open").style.color = "#fff";
        document.getElementById("btn-top-comp-closed").style.background = "";
        document.getElementById("btn-top-comp-closed").style.color = "";
        render();
      };

      document.getElementById("btn-top-comp-subcover").onclick = () => {
        extracted = !extracted;
        render();
      };
    }

    function render() {
      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      const x0 = 60, y0 = h * 0.45;
      const len = w * 0.62;

      // Base line for interval
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(x0, y0); ctx.lineTo(x0 + len, y0);
      ctx.stroke();

      // Endpoints
      ctx.fillStyle = isCompact ? "#38bdf8" : "#94a3b8";
      ctx.beginPath();
      ctx.arc(x0, y0, 6, 0, Math.PI * 2);
      ctx.arc(x0 + len, y0, 6, 0, Math.PI * 2);
      if (isCompact) ctx.fill(); else ctx.stroke();

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(isCompact ? "[ 0" : "( 0", x0 - 15, y0 + 26);
      ctx.fillText(isCompact ? "1 ]" : "1 )", x0 + len + 5, y0 + 26);

      // Open covers
      if (isCompact) {
        // Family of overlapping open intervals covering [0, 1]
        const intervals = [
          { a: -0.1, b: 0.35, color: "#38bdf8", sub: true },
          { a: 0.15, b: 0.45, color: "#a855f7", sub: false },
          { a: 0.28, b: 0.62, color: "#10b981", sub: true },
          { a: 0.48, b: 0.78, color: "#f59e0b", sub: false },
          { a: 0.58, b: 0.88, color: "#ec4899", sub: true },
          { a: 0.75, b: 1.10, color: "#06b6d4", sub: true }
        ];

        intervals.forEach((iv, idx) => {
          if (extracted && !iv.sub) return; // Hide non-subcover intervals

          const startX = x0 + Math.max(-0.05, iv.a) * len;
          const endX = x0 + Math.min(1.05, iv.b) * len;
          const yOff = y0 - 30 - (idx % 3) * 26;

          ctx.strokeStyle = iv.color;
          ctx.lineWidth = 2.5;
          ctx.beginPath();
          ctx.arc(startX, yOff, 4, 0, Math.PI * 2);
          ctx.arc(endX, yOff, 4, 0, Math.PI * 2);
          ctx.stroke();
          ctx.beginPath(); ctx.moveTo(startX, yOff); ctx.lineTo(endX, yOff); ctx.stroke();
        });
      } else {
        // Open interval (0, 1) with cover { (1/n, 1) : n >= 2 }
        for (let n = 2; n <= 12; n++) {
          if (extracted && n > 5) break; // Attempted finite subcover fails at 0!

          const startX = x0 + (1 / n) * len;
          const endX = x0 + len;
          const yOff = y0 - 25 - (n - 2) * 16;

          ctx.strokeStyle = n <= 5 ? "#ef4444" : "#64748b";
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.moveTo(startX, yOff); ctx.lineTo(endX, yOff);
          ctx.stroke();
        }

        // Highlight uncovered gap near 0 if extracted
        if (extracted) {
          const gapX = x0 + (1 / 5) * len;
          ctx.fillStyle = "rgba(239, 68, 68, 0.3)";
          ctx.fillRect(x0, y0 - 15, gapX - x0, 30);
          ctx.fillStyle = "#ef4444";
          ctx.font = "bold 12px Inter, sans-serif";
          ctx.fillText("Gap Uncovered! (0, 1/5] missing!", x0 + 10, y0 + 55);
        }
      }

      // Sidebar Panel
      const rx = w * 0.72;
      ctx.fillStyle = "rgba(30, 41, 59, 0.9)";
      ctx.fillRect(rx, 20, w - rx - 15, h - 40);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 20, w - rx - 15, h - 40);

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Compactness Analysis", rx + 14, 45);

      if (isCompact) {
        ctx.fillStyle = "#10b981";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText("✓ Compact Interval [0, 1]", rx + 14, 72);
        ctx.fillStyle = "#cbd5e1";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText("• Closed & Bounded in R (Heine-Borel).", rx + 14, 95);
        ctx.fillText("• Every open cover has a FINITE subcover.", rx + 14, 115);
        ctx.fillText("• Lebesgue Number δ > 0 exists:", rx + 14, 138);
        ctx.fillText("  Every ball B(x, δ) lies entirely", rx + 14, 156);
        ctx.fillText("  inside some member of the cover.", rx + 14, 174);
      } else {
        ctx.fillStyle = "#ef4444";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText("✗ Non-Compact (0, 1)", rx + 14, 72);
        ctx.fillStyle = "#cbd5e1";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText("• Open cover U_n = (1/n, 1) for n ≥ 2.", rx + 14, 95);
        ctx.fillText("• Any finite subcollection has a max N,", rx + 14, 118);
        ctx.fillText("  leaving (0, 1/N] UNCOVERED!", rx + 14, 138);
        ctx.fillText("• Fails compactness definition.", rx + 14, 160);
      }
    }
    render();
  }
};

// 8. Unit 8: Topologist's Sine Curve & Connectedness
window.SIMULATIONS["sim_top_connected_sine_curve"] = {
  title: "Topologist's Sine Curve: Connected vs Path-Connected Visualizer",
  description: "Examine the iconic Topologist's Sine Curve S = { (x, sin(1/x)) : x in (0, 1] } U ({0} x [-1, 1]), rigorously demonstrating why it is connected but fails path-connectedness.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let animX = 1.0;
    let traceActive = true;

    if (controls) {
      controls.innerHTML = `
        <button id="btn-top-sine-trace" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Animate Curve Tracer</button>
      `;

      document.getElementById("btn-top-sine-trace").onclick = () => {
        traceActive = !traceActive;
      };
    }

    let animId;
    function render() {
      if (traceActive) {
        animX -= 0.003;
        if (animX < 0.02) animX = 1.0;
      }

      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      const originX = 110;
      const originY = h * 0.5;
      const scaleX = w * 0.55;
      const scaleY = 110;

      // Coordinate axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(originX - 40, originY); ctx.lineTo(originX + scaleX + 20, originY);
      ctx.moveTo(originX, 30); ctx.lineTo(originX, h - 30);
      ctx.stroke();

      // Axis labels
      ctx.fillStyle = "#64748b";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("x = 0", originX - 35, originY + 16);
      ctx.fillText("x = 1", originX + scaleX - 10, originY + 16);
      ctx.fillText("+1", originX - 25, originY - scaleY + 4);
      ctx.fillText("-1", originX - 25, originY + scaleY + 4);

      // 1. The Limit Segment: {0} x [-1, 1] (Golden/Amber)
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(originX, originY - scaleY);
      ctx.lineTo(originX, originY + scaleY);
      ctx.stroke();

      // 2. The Oscillating Curve: y = sin(1/x)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.6;
      ctx.beginPath();

      const numPts = 1200;
      for (let i = 1; i <= numPts; i++) {
        const x = (i / numPts); // (0, 1]
        const y = Math.sin(1.0 / x);
        const px = originX + x * scaleX;
        const py = originY - y * scaleY;
        if (i === 1) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Tracer dot approaching x -> 0
      const traceY = Math.sin(1.0 / animX);
      const dotX = originX + animX * scaleX;
      const dotY = originY - traceY * scaleY;
      ctx.fillStyle = "#10b981";
      ctx.beginPath();
      ctx.arc(dotX, dotY, 5, 0, Math.PI * 2);
      ctx.fill();

      // Sidebar Panel
      const rx = w * 0.72;
      ctx.fillStyle = "rgba(30, 41, 59, 0.9)";
      ctx.fillRect(rx, 20, w - rx - 15, h - 40);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 20, w - rx - 15, h - 40);

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Topologist's Sine Curve S̄", rx + 14, 45);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("S̄ = S ∪ ({0} × [-1, 1])", rx + 14, 70);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("1. S̄ is CONNECTED:", rx + 14, 95);
      ctx.fillText("• S = { (x, sin(1/x)) } is connected", rx + 14, 115);
      ctx.fillText("  (continuous image of (0, 1]).", rx + 14, 133);
      ctx.fillText("• The closure of a connected set", rx + 14, 151);
      ctx.fillText("  is always connected ⇒ S̄ is connected!", rx + 14, 169);

      ctx.fillStyle = "#ef4444";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("2. S̄ is NOT Path-Connected:", rx + 14, 200);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("• No continuous path γ: [0, 1] → S̄", rx + 14, 222);
      ctx.fillText("  can connect (0, 0) to (1, sin 1).", rx + 14, 240);
      ctx.fillText("• Infinite oscillation near x = 0", rx + 14, 258);
      ctx.fillText("  violates the Intermediate Value", rx + 14, 276);
      ctx.fillText("  Theorem for continuous paths!", rx + 14, 294);

      animId = requestAnimationFrame(render);
    }
    render();
  }
};
