// Interactive Physics Simulation Suite for Electricity and Magnetism
// 11 comprehensive topic-level simulations covering Coulomb fields, Gauss flux, potential gradients,
// capacitor dielectrics, Drude electron drift, RC transients, Lorentz/Hall effect, Biot-Savart loops,
// Faraday induction & Lenz law, AC RLC resonance, and Thevenin/Norton network theorems.
// Equipped with 60 FPS animation loops, pause/play toggles, and interactive parameter sandboxes.

window.EM_SIMS = {
  // ==========================================
  // 1. Coulomb Field & Vector Superposition
  // ==========================================
  "coulomb-field-sim": {
    title: "⚡ Coulomb Electrostatic Field & Superposition Vectors",
    desc: "Visualize electric field lines, equipotential contours, and resultant vector forces between interactive positive and negative point charges.",
    isAnimated: true,
    controls: [
      { id: "cf-q2", label: "Charge q2 Polarity", min: -2, max: 2, step: 1, value: -1 },
      { id: "cf-dist", label: "Separation Distance d (cm)", min: 8, max: 24, step: 2, value: 16 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const q2Val = parseInt(vals["cf-q2"] !== undefined ? vals["cf-q2"] : -1);
      const dist = parseFloat(vals["cf-dist"] || 16) * 10; // scale to px

      const cx = w * 0.50, cy = h * 0.48;
      const x1 = cx - dist / 2, y1 = cy;
      const x2 = cx + dist / 2, y2 = cy;
      const q1 = +1;
      const q2 = q2Val;

      // Draw Grid / Equipotential Rings
      ctx.strokeStyle = "rgba(56, 189, 248, 0.12)";
      ctx.lineWidth = 1;
      for (let r = 25; r <= 180; r += 30) {
        ctx.beginPath(); ctx.arc(x1, y1, r, 0, Math.PI * 2); ctx.stroke();
        if (q2 !== 0) {
          ctx.beginPath(); ctx.arc(x2, y2, r, 0, Math.PI * 2); ctx.stroke();
        }
      }

      // Draw Field Vectors Mesh
      const step = 38;
      for (let x = 30; x < w - 30; x += step) {
        for (let y = 30; y < h - 50; y += step) {
          const dx1 = x - x1, dy1 = y - y1;
          const r1sq = dx1 * dx1 + dy1 * dy1 + 400;
          const r1 = Math.sqrt(r1sq);
          const e1x = (q1 * dx1) / (r1sq * r1);
          const e1y = (q1 * dy1) / (r1sq * r1);

          let e2x = 0, e2y = 0;
          if (q2 !== 0) {
            const dx2 = x - x2, dy2 = y - y2;
            const r2sq = dx2 * dx2 + dy2 * dy2 + 400;
            const r2 = Math.sqrt(r2sq);
            e2x = (q2 * dx2) / (r2sq * r2);
            e2y = (q2 * dy2) / (r2sq * r2);
          }

          const ex = e1x + e2x;
          const ey = e1y + e2y;
          const emag = Math.sqrt(ex * ex + ey * ey);

          if (emag > 0.00001) {
            const arrowLen = Math.min(18, emag * 12000);
            const ux = (ex / emag) * arrowLen;
            const uy = (ey / emag) * arrowLen;

            ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
            ctx.lineWidth = 1.2;
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(x + ux, y + uy);
            ctx.stroke();
          }
        }
      }

      // Moving Test Charge Orbit / Wander
      const wanderT = animTime * 1.5;
      const tx = cx + Math.cos(wanderT) * (dist * 0.45);
      const ty = cy + Math.sin(wanderT * 1.3) * 45;

      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(tx, ty, 5, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.font = "10px sans-serif";
      ctx.fillText("+q₀", tx + 7, ty - 5);

      // Charge 1 (+q)
      ctx.fillStyle = "#ef4444";
      ctx.beginPath(); ctx.arc(x1, y1, 14, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fff"; ctx.font = "bold 13px sans-serif";
      ctx.fillText("+q", x1 - 8, y1 + 5);

      // Charge 2 (q2)
      if (q2 !== 0) {
        ctx.fillStyle = q2 > 0 ? "#ef4444" : "#3b82f6";
        ctx.beginPath(); ctx.arc(x2, y2, 14, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#fff"; ctx.font = "bold 13px sans-serif";
        ctx.fillText(q2 > 0 ? `+${q2}q` : `${q2}q`, x2 - 9, y2 + 5);
      }

      // Telemetry Box
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(20, h - 70, 320, 55);
      ctx.strokeRect(20, h - 70, 320, 55);
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px monospace";
      ctx.fillText(`Coulomb Vector Field State:`, 32, h - 50);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`q1 = +1.0 μC  |  q2 = ${q2 > 0 ? "+" + q2 : q2}.0 μC  |  d = ${(dist / 10).toFixed(1)} cm`, 32, h - 30);
    }
  },

  // ==========================================
  // 2. Gauss's Law & Flux Enclosure
  // ==========================================
  "gauss-flux-sim": {
    title: "🌐 Gauss's Law: Closed Surface Flux & Enclosed Charge",
    desc: "Calculate electric flux ΦE = ∮ E·dA across spherical and cylindrical Gaussian surfaces as enclosed charge Qencl varies.",
    isAnimated: true,
    controls: [
      { id: "gf-q", label: "Enclosed Charge Q (nC)", min: 1, max: 10, step: 1, value: 5 },
      { id: "gf-rad", label: "Gaussian Radius r (cm)", min: 4, max: 12, step: 1, value: 7 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const Q = parseFloat(vals["gf-q"] || 5);
      const r_cm = parseFloat(vals["gf-rad"] || 7);
      const r_px = r_cm * 12;

      const cx = w * 0.38, cy = h * 0.50;

      // Draw Radial E-Field Vectors Piercing the Surface
      const numRays = 16;
      for (let i = 0; i < numRays; i++) {
        const theta = (i / numRays) * Math.PI * 2 + animTime * 0.2;
        const xStart = cx + 18 * Math.cos(theta);
        const yStart = cy + 18 * Math.sin(theta);
        const xEnd = cx + (r_px + 45) * Math.cos(theta);
        const yEnd = cy + (r_px + 45) * Math.sin(theta);

        ctx.strokeStyle = "rgba(56, 189, 248, 0.45)";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(xStart, yStart);
        ctx.lineTo(xEnd, yEnd);
        ctx.stroke();

        // Arrow head on ray
        const ahX = cx + (r_px + 20) * Math.cos(theta);
        const ahY = cy + (r_px + 20) * Math.sin(theta);
        ctx.fillStyle = "#38bdf8";
        ctx.beginPath(); ctx.arc(ahX, ahY, 3, 0, Math.PI * 2); ctx.fill();
      }

      // Draw Closed Spherical Gaussian Surface
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5; ctx.setLineDash([5, 5]);
      ctx.beginPath(); ctx.arc(cx, cy, r_px, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "rgba(245, 158, 11, 0.08)";
      ctx.beginPath(); ctx.arc(cx, cy, r_px, 0, Math.PI * 2); ctx.fill();

      // Central Enclosed Charge
      ctx.fillStyle = "#ef4444";
      ctx.beginPath(); ctx.arc(cx, cy, 14, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fff"; ctx.font = "bold 11px sans-serif";
      ctx.fillText(`+${Q}nC`, cx - 14, cy + 4);

      // Flux Calculation Gauges on the right
      const eps0 = 8.854e-12;
      const flux = (Q * 1e-9) / eps0; // in V·m
      const E_field = (8.988e9 * (Q * 1e-9)) / Math.pow(r_cm * 1e-2, 2);

      const rx = w * 0.68, ry = 50, rw = w * 0.28;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(rx, ry, rw, 180);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(rx, ry, rw, 180);

      ctx.fillStyle = "#f59e0b"; ctx.font = "12px monospace";
      ctx.fillText("Gauss Flux Audit:", rx + 12, ry + 25);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px monospace";
      ctx.fillText(`Radius r = ${r_cm.toFixed(1)} cm`, rx + 12, ry + 55);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`E(r) = ${(E_field / 1000).toFixed(1)} kV/m`, rx + 12, ry + 85);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`ΦE = Q_encl / ε₀`, rx + 12, ry + 115);
      ctx.fillText(`   = ${(flux).toFixed(0)} V·m`, rx + 12, ry + 135);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("Independent of shape!", rx + 12, ry + 165);
    }
  },

  // ==========================================
  // 3. Electric Potential Gradient E = -grad V
  // ==========================================
  "potential-gradient-sim": {
    title: "🏔️ Potential Landscape & Gradient Vector E = -∇V",
    desc: "Observe how the electric field vector E always points in the direction of steepest potential descent perpendicular to equipotential lines.",
    isAnimated: false,
    controls: [
      { id: "pg-v0", label: "Center Potential V0 (V)", min: 50, max: 250, step: 25, value: 150 },
      { id: "pg-pos", label: "Test Charge Radius r (cm)", min: 3, max: 14, step: 1, value: 8 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const V0 = parseFloat(vals["pg-v0"] || 150);
      const r_cm = parseFloat(vals["pg-pos"] || 8);
      const r_px = r_cm * 14;

      const cx = w * 0.40, cy = h * 0.50;

      // Draw Equipotential Contour Rings
      for (let r = 25; r <= 190; r += 28) {
        const vVal = (V0 * 25 / r).toFixed(0);
        ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
        ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.stroke();
        ctx.fillStyle = "#94a3b8"; ctx.font = "10px monospace";
        ctx.fillText(`${vVal} V`, cx + r - 12, cy - 6);
      }

      // Central Source Peak
      const peakGrad = ctx.createRadialGradient(cx, cy, 2, cx, cy, 24);
      peakGrad.addColorStop(0, "#fbbf24");
      peakGrad.addColorStop(1, "rgba(245, 158, 11, 0)");
      ctx.fillStyle = peakGrad;
      ctx.beginPath(); ctx.arc(cx, cy, 24, 0, Math.PI * 2); ctx.fill();

      // Test Point at (r_px, 0)
      const px = cx + r_px * 0.707, py = cy - r_px * 0.707;
      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      // Electric field vector pointing radially OUTWARD (downhill potential)
      const eLen = Math.max(20, 60 * (60 / r_px));
      const ux = (px - cx) / r_px;
      const uy = (py - cy) / r_px;

      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(px, py);
      ctx.lineTo(px + ux * eLen, py + uy * eLen);
      ctx.stroke();

      // Arrow head
      ctx.fillStyle = "#ef4444";
      ctx.beginPath();
      ctx.arc(px + ux * eLen, py + uy * eLen, 4, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = "#ef4444"; ctx.font = "bold 11px sans-serif";
      ctx.fillText("E = -∇V", px + ux * eLen + 8, py + uy * eLen);

      // Readout
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(w - 280, 40, 260, 95);
      ctx.strokeRect(w - 280, 40, 260, 95);
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px monospace";
      ctx.fillText("Potential Gradient:", w - 265, 65);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`Potential V: ${(V0 * 25 / r_px).toFixed(1)} V`, w - 265, 88);
      ctx.fillStyle = "#ef4444";
      ctx.fillText(`Field E = -dV/dr (Radial)`, w - 265, 110);
    }
  },

  // ==========================================
  // 4. Capacitor & Dielectric Polarization
  // ==========================================
  "dielectric-capacitor-sim": {
    title: "🔋 Parallel Plate Capacitor & Dielectric Polarization",
    desc: "Observe microscopic atomic dipole orientation inside a dielectric slab, surface bound charge density σb, and capacitance increase C = κ C0.",
    isAnimated: true,
    controls: [
      { id: "dc-kappa", label: "Dielectric Constant κ", min: 1.0, max: 6.0, step: 0.5, value: 3.5 },
      { id: "dc-volt", label: "Plate Voltage V (V)", min: 50, max: 300, step: 25, value: 150 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const kappa = parseFloat(vals["dc-kappa"] || 3.5);
      const volt = parseFloat(vals["dc-volt"] || 150);

      const capX1 = w * 0.22, capX2 = w * 0.68;
      const topY = 60, botY = h - 80;
      const capH = botY - topY;

      // Draw Metal Plates
      // Left Plate (+Q)
      ctx.fillStyle = "#ef4444";
      ctx.fillRect(capX1 - 14, topY, 14, capH);
      // Right Plate (-Q)
      ctx.fillStyle = "#3b82f6";
      ctx.fillRect(capX2, topY, 14, capH);

      // Plate charge labels
      ctx.fillStyle = "#fff"; ctx.font = "bold 12px sans-serif";
      for (let y = topY + 20; y < botY; y += 32) {
        ctx.fillText("+", capX1 - 10, y);
        ctx.fillText("-", capX2 + 3, y);
      }

      // Dielectric Slab in between
      const hasDiel = kappa > 1.0;
      if (hasDiel) {
        ctx.fillStyle = "rgba(16, 185, 129, 0.18)";
        ctx.fillRect(capX1, topY, capX2 - capX1, capH);
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
        ctx.strokeRect(capX1, topY, capX2 - capX1, capH);

        // Aligned Molecular Dipoles
        const rows = 6, cols = 8;
        const dx = (capX2 - capX1) / (cols + 1);
        const dy = capH / (rows + 1);
        for (let r = 1; r <= rows; r++) {
          for (let c = 1; c <= cols; c++) {
            const px = capX1 + c * dx;
            const py = topY + r * dy;
            const dipAngle = (Math.sin(animTime * 2 + r + c) * 0.08) * (1 / kappa);

            ctx.save();
            ctx.translate(px, py);
            ctx.rotate(dipAngle);
            // Dipole negative left, positive right (opposing plate field)
            ctx.fillStyle = "#3b82f6";
            ctx.beginPath(); ctx.arc(-6, 0, 3, 0, Math.PI * 2); ctx.fill();
            ctx.fillStyle = "#ef4444";
            ctx.beginPath(); ctx.arc(6, 0, 3, 0, Math.PI * 2); ctx.fill();
            ctx.restore();
          }
        }
      }

      // Electric field lines (left to right)
      ctx.strokeStyle = hasDiel ? "rgba(56, 189, 248, 0.35)" : "rgba(56, 189, 248, 0.7)";
      ctx.lineWidth = 2;
      for (let y = topY + 25; y < botY; y += 35) {
        ctx.beginPath();
        ctx.moveTo(capX1, y);
        ctx.lineTo(capX2, y);
        ctx.stroke();
      }

      // Capacitance & Energy Readout
      const C0 = 50; // pF
      const C = (C0 * kappa).toFixed(1);
      const U = (0.5 * (C0 * kappa * 1e-12) * Math.pow(volt, 2) * 1e6).toFixed(2); // in microJoules

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(w - 240, h - 90, 220, 75);
      ctx.strokeRect(w - 240, h - 90, 220, 75);
      ctx.fillStyle = "#10b981"; ctx.font = "11px monospace";
      ctx.fillText(`Dielectric Constant κ = ${kappa.toFixed(1)}`, w - 225, h - 70);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Capacitance C = ${C} pF`, w - 225, h - 50);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Stored Energy U = ${U} μJ`, w - 225, h - 30);
    }
  },

  // ==========================================
  // 5. Drude Model & Electron Drift Velocity
  // ==========================================
  "drude-current-sim": {
    title: "🔬 Drude Model: Conduction Electron Drift & Lattice Scattering",
    desc: "Observe random thermal collisions between conduction electrons and lattice ions producing net microscopic drift velocity vd = -(eτ/m) E.",
    isAnimated: true,
    controls: [
      { id: "dr-efield", label: "Applied Electric Field E (V/m)", min: 0.2, max: 2.0, step: 0.2, value: 1.0 },
      { id: "dr-temp", label: "Lattice Temperature T (K)", min: 100, max: 500, step: 50, value: 300 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const E = parseFloat(vals["dr-efield"] || 1.0);
      const T = parseFloat(vals["dr-temp"] || 300);

      const boxX = 40, boxY = 50, boxW = w - 80, boxH = h - 110;

      // Wire boundary
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 2;
      ctx.strokeRect(boxX, boxY, boxW, boxH);
      ctx.fillStyle = "rgba(30, 41, 59, 0.25)";
      ctx.fillRect(boxX, boxY, boxW, boxH);

      // Copper Lattice Ions (vibrating with T)
      const cols = 12, rows = 5;
      const dx = boxW / cols, dy = boxH / rows;
      for (let c = 0; c < cols; c++) {
        for (let r = 0; r < rows; r++) {
          const vibX = Math.sin(animTime * 15 + c * 3 + r) * (T / 250);
          const vibY = Math.cos(animTime * 15 + r * 3 + c) * (T / 250);
          const ix = boxX + (c + 0.5) * dx + vibX;
          const iy = boxY + (r + 0.5) * dy + vibY;

          ctx.fillStyle = "#64748b";
          ctx.beginPath(); ctx.arc(ix, iy, 7, 0, Math.PI * 2); ctx.fill();
          ctx.fillStyle = "#94a3b8"; ctx.font = "8px sans-serif";
          ctx.fillText("+", ix - 3, iy + 3);
        }
      }

      // Conduction Electrons drifting from right to left (opposite E-field)
      const numElectrons = 30;
      for (let i = 0; i < numElectrons; i++) {
        // Net drift along -x direction
        const driftSpeed = E * 60;
        const seed = i * 137;
        const thermalVx = Math.cos(seed + animTime * 4) * 25;
        const thermalVy = Math.sin(seed + animTime * 4) * 25;
        const posX = ((seed * 31 - animTime * driftSpeed + thermalVx) % boxW + boxW) % boxW;
        const posY = (seed * 19 + thermalVy) % (boxH - 20) + 10;

        ctx.fillStyle = "#38bdf8";
        ctx.beginPath();
        ctx.arc(boxX + posX, boxY + posY, 3.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // E-field Arrow (pointing right)
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(w / 2 - 50, 25); ctx.lineTo(w / 2 + 50, 25); ctx.stroke();
      ctx.fillStyle = "#ef4444"; ctx.font = "11px sans-serif";
      ctx.fillText("Electric Field E →", w / 2 - 45, 20);

      // Readout
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(40, h - 50, w - 80, 40);
      ctx.strokeRect(40, h - 50, w - 80, 40);
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px monospace";
      ctx.fillText(`Drude Drift Velocity: vd = -0.${(E * 3.3).toFixed(1)} mm/s  |  Relaxation Time τ ≈ 2.5 × 10⁻¹⁴ s  |  Ohmic Regime J = σE`, 55, h - 26);
    }
  },

  // ==========================================
  // 6. RC Circuit Transient Charging/Discharging
  // ==========================================
  "rc-transient-sim": {
    title: "⏱️ RC Circuit Transient: Exponential Charging & 50% Energy Paradox",
    desc: "Interactive RC charging and discharging curve q(t) = Q0(1 - e^-t/RC) confirming that exactly 50% of the battery energy is stored while 50% is lost as heat.",
    isAnimated: true,
    controls: [
      { id: "rc-r", label: "Resistance R (kΩ)", min: 10, max: 100, step: 10, value: 40 },
      { id: "rc-c", label: "Capacitance C (μF)", min: 5, max: 50, step: 5, value: 25 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const R_k = parseFloat(vals["rc-r"] || 40);
      const C_u = parseFloat(vals["rc-c"] || 25);
      const tau = (R_k * 1e3 * C_u * 1e-6); // in seconds

      const ox = 70, oy = h - 60;
      const pw = w - 120, ph = h - 110;

      // Draw Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + pw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - ph);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("Time t (seconds) →", ox + pw - 90, oy + 20);
      ctx.fillText("Voltage VC(t) (Volts) ↑", ox - 60, oy - ph - 8);

      // Charging Exponential Curve
      const maxT = tau * 5;
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const t = (i / 100) * maxT;
        const vFrac = 1 - Math.exp(-t / tau);
        const gx = ox + (i / 100) * pw;
        const gy = oy - vFrac * ph;
        if (i === 0) ctx.moveTo(gx, gy); else ctx.lineTo(gx, gy);
      }
      ctx.stroke();

      // Tau marker (63.2%)
      const tauX = ox + (tau / maxT) * pw;
      const tauY = oy - 0.632 * ph;
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(tauX, oy); ctx.lineTo(tauX, tauY);
      ctx.moveTo(ox, tauY); ctx.lineTo(tauX, tauY);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.font = "10px monospace";
      ctx.fillText(`τ = ${tau.toFixed(2)}s (63.2%)`, tauX + 5, tauY - 5);

      // Animated tracer dot
      const simT = (animTime * 1.5) % maxT;
      const curFrac = 1 - Math.exp(-simT / tau);
      const dotX = ox + (simT / maxT) * pw;
      const dotY = oy - curFrac * ph;

      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(dotX, dotY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.stroke();

      // Readout
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(w - 260, 30, 240, 75);
      ctx.strokeRect(w - 260, 30, 240, 75);
      ctx.fillStyle = "#10b981"; ctx.font = "11px monospace";
      ctx.fillText(`Time Constant τ = RC = ${tau.toFixed(2)} s`, w - 245, 52);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Current Charge: ${(curFrac * 100).toFixed(1)}%`, w - 245, 72);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Energy Partition: 50% C / 50% Heat`, w - 245, 92);
    }
  },

  // ==========================================
  // 7. Lorentz Force & Hall Effect
  // ==========================================
  "lorentz-hall-sim": {
    title: "🧲 Lorentz Magnetic Force & The Hall Effect",
    desc: "Observe cyclotron circular deflection of charges in magnetic fields and transverse charge accumulation establishing Hall voltage VH = (IB)/(nqt).",
    isAnimated: true,
    controls: [
      { id: "lh-b", label: "Magnetic Field B (Tesla)", min: 0.2, max: 2.0, step: 0.2, value: 1.0 },
      { id: "lh-sign", label: "Carrier Sign (+hole / -electron)", min: -1, max: 1, step: 2, value: -1 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const B = parseFloat(vals["lh-b"] || 1.0);
      const sign = parseInt(vals["lh-sign"] || -1);

      // Left Half: Cyclotron Orbit in B-field
      const cycx = w * 0.25, cycy = h * 0.50;
      const cycR = Math.max(25, 70 / B);

      // B-field grid dots (pointing out of screen ⊙)
      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      for (let x = 30; x < w * 0.45; x += 35) {
        for (let y = 40; y < h - 40; y += 35) {
          ctx.beginPath(); ctx.arc(x, y, 2, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Cyclotron circular trajectory
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.arc(cycx, cycy, cycR, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      const orbitTheta = animTime * 3 * B * (sign < 0 ? 1 : -1);
      const px = cycx + cycR * Math.cos(orbitTheta);
      const py = cycy + cycR * Math.sin(orbitTheta);

      ctx.fillStyle = sign < 0 ? "#3b82f6" : "#ef4444";
      ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.stroke();

      // Right Half: Semiconductor Hall Strip
      const hx = w * 0.55, hy = 80, hw = w * 0.38, hh = 120;
      ctx.fillStyle = "rgba(30, 41, 59, 0.5)";
      ctx.fillRect(hx, hy, hw, hh);
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 2;
      ctx.strokeRect(hx, hy, hw, hh);

      // Accumulated transverse charges
      ctx.fillStyle = sign < 0 ? "#3b82f6" : "#ef4444";
      for (let x = hx + 15; x < hx + hw - 10; x += 22) {
        ctx.beginPath(); ctx.arc(x, hy + hh - 8, 4, 0, Math.PI * 2); ctx.fill();
      }
      ctx.fillStyle = sign < 0 ? "#ef4444" : "#3b82f6";
      for (let x = hx + 15; x < hx + hw - 10; x += 22) {
        ctx.beginPath(); ctx.arc(x, hy + 8, 4, 0, Math.PI * 2); ctx.fill();
      }

      // Voltmeter reading Hall Voltage
      const vh_val = (B * (sign < 0 ? -12.5 : 12.5)).toFixed(1);
      ctx.fillStyle = "#f59e0b"; ctx.font = "12px monospace";
      ctx.fillText(`Hall Voltage: VH = ${vh_val} mV`, hx + 20, hy + hh + 30);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "10px sans-serif";
      ctx.fillText(`Majority Carrier: ${sign < 0 ? "Electrons (n-type)" : "Holes (p-type)"}`, hx + 20, hy + hh + 48);
    }
  },

  // ==========================================
  // 8. Biot-Savart Law & Circular Loop Axis
  // ==========================================
  "biot-savart-sim": {
    title: "🔄 Biot-Savart Law: Circular Current Loop Magnetic Field",
    desc: "Calculate magnetic field B(x) = [μ0 I R²] / [2(R² + x²)^(3/2)] along the central symmetry axis of a current-carrying loop.",
    isAnimated: true,
    controls: [
      { id: "bs-i", label: "Loop Current I (A)", min: 1, max: 8, step: 1, value: 4 },
      { id: "bs-r", label: "Loop Radius R (cm)", min: 5, max: 15, step: 1, value: 10 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const I = parseFloat(vals["bs-i"] || 4);
      const R_cm = parseFloat(vals["bs-r"] || 10);
      const R_px = R_cm * 6;

      const cx = w * 0.32, cy = h * 0.50;

      // Draw Elliptical Projected Current Loop
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.ellipse(cx, cy, 14, R_px, 0, 0, Math.PI * 2);
      ctx.stroke();

      // Current direction arrows
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`I = ${I} A`, cx - 20, cy - R_px - 8);

      // Central Axis line
      ctx.strokeStyle = "rgba(148, 163, 184, 0.3)"; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(cx - 60, cy); ctx.lineTo(w - 30, cy); ctx.stroke();
      ctx.setLineDash([]);

      // Magnetic field profile curve plotted below
      const gx = w * 0.52, gy = h - 60, gw = w * 0.42, gh = 120;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(gx, gy); ctx.lineTo(gx + gw, gy);
      ctx.moveTo(gx, gy); ctx.lineTo(gx, gy - gh);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("Axial Distance x →", gx + gw - 90, gy + 18);
      ctx.fillText("Field B(x) (mT) ↑", gx - 20, gy - gh - 8);

      // Biot-Savart bell curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      const B0 = (I * 2.5); // normalized
      for (let i = 0; i <= 100; i++) {
        const xRel = (i / 100) * 2.5; // in units of R
        const bVal = B0 / Math.pow(1 + xRel * xRel, 1.5);
        const px = gx + (i / 100) * gw;
        const py = gy - (bVal / B0) * (gh * 0.85);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Central field value
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px monospace";
      ctx.fillText(`Center B(0) = μ0 I / 2R = ${(4 * Math.PI * 1e-7 * I / (2 * R_cm * 1e-2) * 1e3).toFixed(2)} mT`, gx + 15, gy - gh + 15);
    }
  },

  // ==========================================
  // 9. Faraday Induction & Lenz's Law
  // ==========================================
  "faraday-induction-sim": {
    title: "🧲 Faraday's Induction & Lenz's Opposing EMF",
    desc: "Drop a magnetic dipole through a conductive coil. Observe changing magnetic flux dΦ/dt, induced back EMF polarity, and magnetic drag.",
    isAnimated: true,
    controls: [
      { id: "fi-speed", label: "Magnet Speed v", min: 0.5, max: 2.5, step: 0.2, value: 1.2 },
      { id: "fi-turns", label: "Coil Turns N", min: 50, max: 250, step: 25, value: 100 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const spd = parseFloat(vals["fi-speed"] || 1.2);
      const N = parseInt(vals["fi-turns"] || 100);

      const midX = w * 0.35;
      const coilY = h * 0.50;

      // Draw Wire Coil Solenoid in cross-section
      ctx.fillStyle = "#f59e0b";
      for (let y = coilY - 40; y <= coilY + 40; y += 14) {
        ctx.beginPath(); ctx.arc(midX - 35, y, 5, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.arc(midX + 35, y, 5, 0, Math.PI * 2); ctx.fill();
      }

      // Falling Bar Magnet
      const loopH = h - 60;
      const magY = 30 + ((animTime * spd * 90) % loopH);
      const magW = 28, magH = 50;

      // North Pole (Red)
      ctx.fillStyle = "#ef4444";
      ctx.fillRect(midX - magW / 2, magY - magH / 2, magW, magH / 2);
      ctx.fillStyle = "#fff"; ctx.font = "bold 11px sans-serif";
      ctx.fillText("N", midX - 4, magY - magH / 4 + 4);

      // South Pole (Blue)
      ctx.fillStyle = "#3b82f6";
      ctx.fillRect(midX - magW / 2, magY, magW, magH / 2);
      ctx.fillStyle = "#fff";
      ctx.fillText("S", midX - 4, magY + magH / 4 + 4);

      // Oscilloscope Screen on the right (EMF trace)
      const ox = w * 0.58, oy = 50, ow = w * 0.38, oh = 160;
      ctx.fillStyle = "#022c22"; ctx.fillRect(ox, oy, ow, oh);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5; ctx.strokeRect(ox, oy, ow, oh);

      // Center baseline
      ctx.strokeStyle = "rgba(16, 185, 129, 0.25)";
      ctx.beginPath(); ctx.moveTo(ox, oy + oh / 2); ctx.lineTo(ox + ow, oy + oh / 2); ctx.stroke();

      // Theoretical double-pulse EMF curve: dPhi/dt peaks positive entering, negative exiting
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const u = (i - 50) / 15;
        // Derivative of Gaussian: -u * exp(-u^2/2)
        const emfVal = -u * Math.exp(-u * u / 2) * (oh * 0.4) * (N / 100);
        const gx = ox + (i / 100) * ow;
        const gy = oy + oh / 2 + emfVal;
        if (i === 0) ctx.moveTo(gx, gy); else ctx.lineTo(gx, gy);
      }
      ctx.stroke();

      ctx.fillStyle = "#10b981"; ctx.font = "11px monospace";
      ctx.fillText("Induced EMF Oscilloscope:", ox + 10, oy + 20);
      ctx.fillText("E = -N (dΦB/dt)", ox + 10, oy + 38);
    }
  },

  // ==========================================
  // 10. AC Series LCR Resonance & Phasors
  // ==========================================
  "ac-rlc-resonance-sim": {
    title: "⚡ AC Series LCR Resonance & Rotating Phasor Vectors",
    desc: "Sweep driving frequency ω across electrical resonance ω0 = 1/√(LC). Observe VR, VL, and VC phasor cancellation and Quality factor Q.",
    isAnimated: true,
    controls: [
      { id: "rlc-w", label: "Frequency Ratio ω / ω0", min: 0.4, max: 1.6, step: 0.05, value: 1.0 },
      { id: "rlc-r", label: "Resistance R (Ω)", min: 5, max: 40, step: 5, value: 15 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const wRatio = parseFloat(vals["rlc-w"] || 1.0);
      const R = parseFloat(vals["rlc-r"] || 15);

      const px = w * 0.28, py = h * 0.50;

      // Rotating reference angle
      const omegaT = animTime * 3;

      // Reactances
      const XL = 50 * wRatio;
      const XC = 50 / wRatio;
      const Z = Math.sqrt(R * R + Math.pow(XL - XC, 2));
      const I0 = 100 / Z;

      // Phasor components
      const VR = I0 * R * 0.7;
      const VL = I0 * XL * 0.7;
      const VC = I0 * XC * 0.7;

      // Draw Rotating Phasors
      // 1. VR (in phase with current)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(px, py);
      ctx.lineTo(px + VR * Math.cos(omegaT), py - VR * Math.sin(omegaT));
      ctx.stroke();

      // 2. VL (+90 deg lead)
      ctx.strokeStyle = "#38bdf8";
      ctx.beginPath();
      ctx.moveTo(px, py);
      ctx.lineTo(px + VL * Math.cos(omegaT + Math.PI / 2), py - VL * Math.sin(omegaT + Math.PI / 2));
      ctx.stroke();

      // 3. VC (-90 deg lag)
      ctx.strokeStyle = "#ef4444";
      ctx.beginPath();
      ctx.moveTo(px, py);
      ctx.lineTo(px + VC * Math.cos(omegaT - Math.PI / 2), py - VC * Math.sin(omegaT - Math.PI / 2));
      ctx.stroke();

      // Resonance Curve on the right
      const rx = w * 0.55, ry = h - 60, rw = w * 0.38, rh = 120;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(rx, ry); ctx.lineTo(rx + rw, ry);
      ctx.moveTo(rx, ry); ctx.lineTo(rx, ry - rh);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("Frequency ω/ω0 →", rx + rw - 90, ry + 18);
      ctx.fillText("RMS Current I (A) ↑", rx - 20, ry - rh - 8);

      // Current curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const u = 0.3 + (i / 100) * 1.4;
        const curZ = Math.sqrt(R * R + Math.pow(50 * u - 50 / u, 2));
        const curI = (100 / curZ) * 8;
        const gx = rx + ((u - 0.3) / 1.4) * rw;
        const gy = ry - Math.min(rh - 10, curI);
        if (i === 0) ctx.moveTo(gx, gy); else ctx.lineTo(gx, gy);
      }
      ctx.stroke();

      // Operating marker on resonance curve
      const opX = rx + ((wRatio - 0.3) / 1.4) * rw;
      const opY = ry - Math.min(rh - 10, (100 / Z) * 8);
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(opX, opY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.stroke();

      const Q = (50 / R).toFixed(1);
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px monospace";
      ctx.fillText(`Quality Factor Q = ${Q}`, rx + 15, ry - rh + 15);
      ctx.fillText(`Impedance Z = ${Z.toFixed(1)} Ω`, rx + 15, ry - rh + 32);
    }
  },

  // ==========================================
  // 11. Thevenin & Norton Network Theorems
  // ==========================================
  "thevenin-norton-sim": {
    title: "🧮 Thevenin & Norton Theorems & Maximum Power Transfer",
    desc: "Solve equivalent source parameters Vth and Rth across variable load resistor RL, confirming maximum power absorption at matching impedance RL = Rth.",
    isAnimated: false,
    controls: [
      { id: "tn-rl", label: "Load Resistance RL (Ω)", min: 4, max: 40, step: 2, value: 16 },
      { id: "tn-vth", label: "Thevenin Voltage Vth (V)", min: 10, max: 50, step: 5, value: 24 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const RL = parseFloat(vals["tn-rl"] || 16);
      const Vth = parseFloat(vals["tn-vth"] || 24);
      const Rth = 16.0; // fixed internal Thevenin resistance

      const IL = Vth / (Rth + RL);
      const PL = Math.pow(IL, 2) * RL;
      const eff = (RL / (Rth + RL)) * 100;

      // Left: Schematic Diagram of Thevenin Equivalent
      const sx = 60, sy = 60, sw = w * 0.42, sh = 130;
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 2;
      ctx.strokeRect(sx, sy, sw, sh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px monospace";
      ctx.fillText(`Vth = ${Vth.toFixed(1)} V`, sx + 20, sy + 70);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Rth = ${Rth.toFixed(1)} Ω`, sx + sw / 2 - 25, sy + 30);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Load RL = ${RL.toFixed(1)} Ω`, sx + sw - 80, sy + 70);

      // Right: Power Curve PL(RL)
      const gx = w * 0.55, gy = h - 50, gw = w * 0.38, gh = 125;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(gx, gy); ctx.lineTo(gx + gw, gy);
      ctx.moveTo(gx, gy); ctx.lineTo(gx, gy - gh);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("Load Resistance RL (Ω) →", gx + gw - 110, gy + 18);
      ctx.fillText("Power PL (Watts) ↑", gx - 20, gy - gh - 8);

      // Plot Power curve
      const Pmax = Math.pow(Vth, 2) / (4 * Rth);
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let r = 2; r <= 50; r += 1) {
        const pVal = Math.pow(Vth / (Rth + r), 2) * r;
        const px = gx + (r / 50) * gw;
        const py = gy - (pVal / Pmax) * (gh * 0.85);
        if (r === 2) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current RL point on power curve
      const ptX = gx + (RL / 50) * gw;
      const ptY = gy - (PL / Pmax) * (gh * 0.85);
      ctx.fillStyle = "#ef4444";
      ctx.beginPath(); ctx.arc(ptX, ptY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.stroke();

      // Readouts
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(sx, h - 80, sw, 60);
      ctx.strokeRect(sx, h - 80, sw, 60);
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px monospace";
      ctx.fillText(`Power Delivered: PL = ${PL.toFixed(2)} W (Max: ${Pmax.toFixed(2)} W)`, sx + 12, h - 60);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`Load Current: IL = ${IL.toFixed(2)} A | Efficiency: ${eff.toFixed(1)}%`, sx + 12, h - 40);
    }
  }
};


// Universal Engine Integration Adapter for Electricity and Magnetism
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  if (window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }

  const simConfig = (window.EM_SIMS && window.EM_SIMS[simType]) ||
                    (window.MATTER_SIMS && window.MATTER_SIMS[simType]) ||
                    (window.STATMECH_SIMS && window.STATMECH_SIMS[simType]);
  if (!simConfig) {
    console.warn('Simulation not found:', simType);
    return;
  }

  container.innerHTML = '';

  const box = document.createElement('div');
  box.className = 'sim-inline-card';
  box.style.background = '#0c1322';
  box.style.border = '1px solid #1e293b';
  box.style.borderRadius = '12px';
  box.style.padding = '1.5rem';
  box.style.margin = '1.75rem 0';

  const header = document.createElement('div');
  header.style.marginBottom = '1rem';
  header.innerHTML = `
    <h4 style="color:#38bdf8; font-size:1.15rem; margin-bottom:0.35rem; display:flex; align-items:center; gap:0.5rem;">
      ${simConfig.title}
    </h4>
    <p style="color:#94a3b8; font-size:0.9rem; line-height:1.5;">${simConfig.desc}</p>
  `;
  box.appendChild(header);

  const canvas = document.createElement('canvas');
  canvas.width = 720;
  canvas.height = 340;
  canvas.style.width = '100%';
  canvas.style.height = 'auto';
  canvas.style.borderRadius = '8px';
  canvas.style.display = 'block';
  canvas.style.background = '#070b14';
  canvas.style.border = '1px solid #1e293b';
  box.appendChild(canvas);

  const ctrlBar = document.createElement('div');
  ctrlBar.style.display = 'flex';
  ctrlBar.style.flexWrap = 'wrap';
  ctrlBar.style.gap = '1.25rem';
  ctrlBar.style.marginTop = '1rem';
  ctrlBar.style.padding = '0.75rem 1rem';
  ctrlBar.style.background = '#080e1c';
  ctrlBar.style.borderRadius = '8px';
  ctrlBar.style.border = '1px solid #1e293d';

  const currentVals = {};

  if (simConfig.controls && simConfig.controls.length > 0) {
    simConfig.controls.forEach(ctrl => {
      currentVals[ctrl.id] = ctrl.value;

      const wrap = document.createElement('div');
      wrap.style.display = 'flex';
      wrap.style.flexDirection = 'column';
      wrap.style.gap = '0.25rem';
      wrap.style.minWidth = '160px';

      const labelRow = document.createElement('div');
      labelRow.style.display = 'flex';
      labelRow.style.justifyContent = 'space-between';
      labelRow.style.fontSize = '0.82rem';
      labelRow.style.color = '#cbd5e1';

      const titleSpan = document.createElement('span');
      titleSpan.innerText = ctrl.label;
      const valSpan = document.createElement('span');
      valSpan.style.fontFamily = 'monospace';
      valSpan.style.color = '#38bdf8';
      valSpan.innerText = ctrl.value;

      labelRow.appendChild(titleSpan);
      labelRow.appendChild(valSpan);
      wrap.appendChild(labelRow);

      const input = document.createElement('input');
      input.type = 'range';
      input.min = ctrl.min;
      input.max = ctrl.max;
      input.step = ctrl.step;
      input.value = ctrl.value;
      input.style.accentColor = '#38bdf8';
      input.style.cursor = 'pointer';

      input.addEventListener('input', (e) => {
        const v = parseFloat(e.target.value);
        currentVals[ctrl.id] = v;
        valSpan.innerText = v;
        if (!simConfig.isAnimated) {
          simConfig.render(canvas, currentVals, 0);
        }
      });

      wrap.appendChild(input);
      ctrlBar.appendChild(wrap);
    });
  }

  if (simConfig.isAnimated) {
    const animCtrlWrap = document.createElement('div');
    animCtrlWrap.style.display = 'flex';
    animCtrlWrap.style.alignItems = 'flex-end';
    const pauseBtn = document.createElement('button');
    pauseBtn.innerText = '⏸️ Pause';
    pauseBtn.style.padding = '0.4rem 0.8rem';
    pauseBtn.style.background = '#1e293b';
    pauseBtn.style.color = '#38bdf8';
    pauseBtn.style.border = '1px solid #334155';
    pauseBtn.style.borderRadius = '6px';
    pauseBtn.style.cursor = 'pointer';
    pauseBtn.style.fontSize = '0.85rem';

    let isPaused = false;
    pauseBtn.addEventListener('click', () => {
      isPaused = !isPaused;
      pauseBtn.innerText = isPaused ? '▶️ Play' : '⏸️ Pause';
    });
    animCtrlWrap.appendChild(pauseBtn);
    ctrlBar.appendChild(animCtrlWrap);

    box.appendChild(ctrlBar);
    container.appendChild(box);

    let startTime = performance.now();
    let elapsedBeforePause = 0;

    function animLoop(now) {
      if (!document.getElementById(containerId)) return;
      if (!isPaused) {
        const t = (now - startTime) / 1000 + elapsedBeforePause;
        simConfig.render(canvas, currentVals, t);
      }
      window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(animLoop);
    }
    window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(animLoop);
  } else {
    box.appendChild(ctrlBar);
    container.appendChild(box);
    simConfig.render(canvas, currentVals, 0);
  }
};
