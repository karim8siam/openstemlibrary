// Interactive Physics Simulation Suite for Properties of Matter and Waves
// 12 comprehensive topic-level simulations covering gravitation, elasticity, hydrostatics,
// hydrodynamics, oscillations, traveling waves, stationary normal modes, and acoustic Doppler phenomena.
// Equipped with 60 FPS animation loops, pause/play toggles, and interactive parameter sandboxes.

window.MATTER_SIMS = {
  // ==========================================
  // 1. Keplerian Orbits & Areal Velocity
  // ==========================================
  "kepler-orbit-sim": {
    title: "🪐 Keplerian Planetary Orbits & Sweeping Areal Velocity",
    desc: "Simulate an orbiting celestial body under Newtonian central gravity. Verify Kepler's Second Law (constant areal velocity dA/dt) and speed variation from perihelion to aphelion.",
    isAnimated: true,
    controls: [
      { id: "kop-e", label: "Eccentricity e", min: 0.0, max: 0.85, step: 0.05, value: 0.50 },
      { id: "kop-spd", label: "Orbit Speed Multiplier", min: 0.5, max: 2.5, step: 0.1, value: 1.0 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const e = parseFloat(vals["kop-e"] || 0.5);
      const spd = parseFloat(vals["kop-spd"] || 1.0);

      const cx = w * 0.48, cy = h * 0.50;
      const a = Math.min(w * 0.36, 210);
      const b = a * Math.sqrt(Math.max(0.01, 1 - e * e));
      const c = a * e; // distance from center to focus

      // Draw coordinate grid / stars
      ctx.fillStyle = "rgba(255,255,255,0.15)";
      for (let i = 0; i < 25; i++) {
        const sx = (i * 127) % w, sy = (i * 283) % h;
        ctx.fillRect(sx, sy, 1.5, 1.5);
      }

      // Draw Orbit Ellipse
      ctx.save();
      ctx.translate(cx, cy);
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.ellipse(0, 0, a, b, 0, 0, Math.PI * 2);
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Sun at Focus F1 (-c, 0)
      const sunX = -c, sunY = 0;
      const sunGrad = ctx.createRadialGradient(sunX, sunY, 2, sunX, sunY, 22);
      sunGrad.addColorStop(0, "#fbbf24");
      sunGrad.addColorStop(0.5, "#f59e0b");
      sunGrad.addColorStop(1, "rgba(245, 158, 11, 0)");
      ctx.fillStyle = sunGrad;
      ctx.beginPath();
      ctx.arc(sunX, sunY, 22, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = "#fff";
      ctx.beginPath();
      ctx.arc(sunX, sunY, 6, 0, Math.PI * 2);
      ctx.fill();

      // Planet Motion via Kepler's equation approximation
      // Mean anomaly M = omega * t
      const M = (animTime * 0.8 * spd) % (Math.PI * 2);
      // Solve Kepler's equation M = E - e*sin(E) by iteration
      let E = M;
      for (let iter = 0; iter < 5; iter++) {
        E = E - (E - e * Math.sin(E) - M) / (1 - e * Math.cos(E));
      }
      // Cartesian coordinates on ellipse
      const px = a * Math.cos(E);
      const py = b * Math.sin(E);

      // Sweeping areal triangle sector
      const E_prev = E - 0.25;
      const px_prev = a * Math.cos(E_prev);
      const py_prev = b * Math.sin(E_prev);

      ctx.fillStyle = "rgba(245, 158, 11, 0.25)";
      ctx.beginPath();
      ctx.moveTo(sunX, sunY);
      ctx.lineTo(px_prev, py_prev);
      ctx.lineTo(px, py);
      ctx.closePath();
      ctx.fill();

      // Radius vector r(t)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(sunX, sunY);
      ctx.lineTo(px, py);
      ctx.stroke();

      // Planet body
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(px, py, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#fff";
      ctx.beginPath();
      ctx.arc(px, py, 2.5, 0, Math.PI * 2);
      ctx.fill();

      // Velocity Vector (tangent to ellipse)
      const vx = -a * Math.sin(E);
      const vy = b * Math.cos(E);
      const vMag = Math.sqrt(vx * vx + vy * vy);
      const rDist = Math.sqrt((px - sunX) * (px - sunX) + py * py);
      const scaleV = 35 / (vMag || 1);
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(px, py);
      ctx.lineTo(px + vx * scaleV, py + vy * scaleV);
      ctx.stroke();

      ctx.restore();

      // Telemetry Box
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.strokeStyle = "#1e293b";
      ctx.lineWidth = 1;
      ctx.fillRect(16, 16, 250, 105);
      ctx.strokeRect(16, 16, 250, 105);

      const rReal = (rDist / a).toFixed(2);
      const vNorm = (Math.sqrt(2 / rReal - 1)).toFixed(2);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px monospace";
      ctx.fillText(`Kepler Orbit Parameters (e = ${e.toFixed(2)}):`, 26, 34);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Radius r / a:      ${rReal} AU`, 26, 52);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Orbital Speed v:   ${vNorm} v₀`, 26, 70);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Areal Velocity:    dA/dt = Const`, 26, 88);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`Perihelion: ${(1 - e).toFixed(2)} a | Aphelion: ${(1 + e).toFixed(2)} a`, 26, 106);
    }
  },

  // ==========================================
  // 2. Cavendish Torsion Balance
  // ==========================================
  "cavendish-gravitation-sim": {
    title: "⚖️ Cavendish Torsion Balance: Measuring Big G",
    desc: "Observe the damped torsional balance oscillation under gravitational attraction between small masses m and heavy spheres M, with laser mirror reflection.",
    isAnimated: true,
    controls: [
      { id: "cav-m", label: "Large Sphere Mass M (kg)", min: 50, max: 250, step: 25, value: 150 },
      { id: "cav-damp", label: "Damping Constant γ", min: 0.02, max: 0.20, step: 0.02, value: 0.06 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const M = parseFloat(vals["cav-m"] || 150);
      const gamma = parseFloat(vals["cav-damp"] || 0.06);

      const cx = w * 0.45, cy = h * 0.48;
      const rodLen = 120; // half length

      // Equilibrium angle theta_eq proportional to M
      const theta_eq = 0.18 * (M / 150);
      // Damped harmonic oscillation toward theta_eq
      const omega0 = 1.4;
      const theta = theta_eq * (1 - Math.exp(-gamma * animTime * 3) * Math.cos(omega0 * animTime * 3));

      // Draw Glass Enclosure Box
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.strokeRect(cx - 160, cy - 110, 320, 220);
      ctx.fillStyle = "rgba(148, 163, 184, 0.03)";
      ctx.fillRect(cx - 160, cy - 110, 320, 220);

      // Draw Fixed Large Spheres M (in Lead grey)
      const bigR = 26;
      const offsetD = 135;
      const perpOffset = 42;

      // Sphere M1 (top-right)
      ctx.fillStyle = "#64748b";
      ctx.beginPath();
      ctx.arc(cx + offsetD * Math.cos(theta_eq) - perpOffset * Math.sin(theta_eq), 
              cy + offsetD * Math.sin(theta_eq) + perpOffset * Math.cos(theta_eq), bigR, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#94a3b8"; ctx.stroke();

      // Sphere M2 (bottom-left)
      ctx.beginPath();
      ctx.arc(cx - offsetD * Math.cos(theta_eq) + perpOffset * Math.sin(theta_eq), 
              cy - offsetD * Math.sin(theta_eq) - perpOffset * Math.cos(theta_eq), bigR, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // Draw Torsion Beam rotated by theta
      const mX1 = cx + rodLen * Math.cos(theta);
      const mY1 = cy + rodLen * Math.sin(theta);
      const mX2 = cx - rodLen * Math.cos(theta);
      const mY2 = cy - rodLen * Math.sin(theta);

      ctx.strokeStyle = "#cbd5e1"; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(mX1, mY1); ctx.lineTo(mX2, mY2);
      ctx.stroke();

      // Small Spheres m
      const smallR = 9;
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(mX1, mY1, smallR, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(mX2, mY2, smallR, 0, Math.PI * 2); ctx.fill();

      // Central Quartz Fiber & Mirror
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(cx, cy, 6, 0, Math.PI * 2); ctx.fill();

      // Laser Beam reflection
      const laserSourceX = cx - 140, laserSourceY = cy - 80;
      ctx.strokeStyle = "rgba(239, 68, 68, 0.4)"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(laserSourceX, laserSourceY); ctx.lineTo(cx, cy); ctx.stroke();

      // Reflected beam rotated by 2*theta
      const reflAngle = -0.6 + 2 * theta;
      const scaleWallX = cx + 155;
      const scaleWallY = cy + Math.tan(reflAngle) * 155;
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(scaleWallX, scaleWallY); ctx.stroke();

      // Scale marker on wall
      ctx.fillStyle = "#ef4444";
      ctx.fillRect(scaleWallX - 4, scaleWallY - 4, 8, 8);

      // Readout
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(16, h - 85, 280, 70);
      ctx.strokeRect(16, h - 85, 280, 70);
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px monospace";
      ctx.fillText(`Cavendish Torsion Dynamics:`, 26, h - 65);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`Fiber Angle θ: ${(theta * (180 / Math.PI)).toFixed(3)}° (Eq: ${(theta_eq * 180 / Math.PI).toFixed(2)}°)`, 26, h - 45);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`G = 6.674 × 10⁻¹¹ N·m²/kg²`, 26, h - 25);
    }
  },

  // ==========================================
  // 3. Hooke's Law & Stress-Strain Curve
  // ==========================================
  "hooke-stress-strain-sim": {
    title: "📈 Engineering Stress-Strain Curve & Hooke's Elastic Limit",
    desc: "Interactive tensile test curve showing Hooke's proportional regime, yield stress, strain hardening, ultimate tensile strength, and necking fracture.",
    isAnimated: false,
    controls: [
      { id: "hss-strain", label: "Applied Strain ε (%)", min: 0.0, max: 20.0, step: 0.2, value: 2.0 },
      { id: "hss-ymod", label: "Young's Modulus Y (GPa)", min: 100, max: 250, step: 10, value: 200 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const strainPct = parseFloat(vals["hss-strain"] || 2.0);
      const eps = strainPct / 100;
      const Y = parseFloat(vals["hss-ymod"] || 200);

      const ox = 70, oy = h - 60;
      const pw = w - 120, ph = h - 110;

      // Draw Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + pw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - ph);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Strain ε (%) →", ox + pw - 60, oy + 25);
      ctx.fillText("Stress σ (MPa) ↑", ox - 60, oy - ph - 10);

      // Model stress-strain curve
      function getStress(e) {
        if (e <= 0.002) return e * Y * 1000; // Linear elastic
        if (e <= 0.015) return 0.002 * Y * 1000 + (e - 0.002) * 5000; // Yield plateau
        if (e <= 0.12) return 0.002 * Y * 1000 + 0.013 * 5000 + 400 * Math.pow((e - 0.015) / 0.105, 0.45); // Strain hardening
        if (e <= 0.20) {
          const peak = 0.002 * Y * 1000 + 0.013 * 5000 + 400;
          return peak - 280 * Math.pow((e - 0.12) / 0.08, 1.4); // Necking
        }
        return 0;
      }

      // Draw Curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      const maxPlotEps = 0.20;
      const maxPlotStress = 650;

      for (let i = 0; i <= 200; i++) {
        const curE = (i / 200) * maxPlotEps;
        const curS = getStress(curE);
        const px = ox + (curE / maxPlotEps) * pw;
        const py = oy - (curS / maxPlotStress) * ph;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Draw Highlighted Zones
      ctx.fillStyle = "rgba(16, 185, 129, 0.15)"; // Elastic
      const elX = ox + (0.002 / maxPlotEps) * pw;
      ctx.fillRect(ox, oy - ph, elX - ox, ph);
      ctx.fillStyle = "#10b981"; ctx.font = "10px sans-serif";
      ctx.fillText("Elastic Hookean Zone", ox + 5, oy - ph + 15);

      // Current Point
      const curStress = getStress(eps);
      const ptX = ox + (eps / maxPlotEps) * pw;
      const ptY = oy - (curStress / maxPlotStress) * ph;

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(ptX, ptY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      // Readout
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(w - 260, 20, 240, 85);
      ctx.strokeRect(w - 260, 20, 240, 85);
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px monospace";
      ctx.fillText(`State at ε = ${strainPct.toFixed(1)}%:`, w - 245, 40);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Tensile Stress: ${curStress.toFixed(1)} MPa`, w - 245, 60);
      ctx.fillStyle = eps <= 0.002 ? "#10b981" : eps <= 0.12 ? "#f59e0b" : "#ef4444";
      ctx.fillText(`Regime: ${eps <= 0.002 ? "Linear Hooke (Elastic)" : eps <= 0.015 ? "Yield Plateau" : eps <= 0.12 ? "Strain Hardening" : "Necking Fracture"}`, w - 245, 80);
    }
  },

  // ==========================================
  // 4. Cantilever Beam Deflection
  // ==========================================
  "cantilever-bending-sim": {
    title: "🏗️ Elastic Cantilever Beam Deflection & Stress Gradient",
    desc: "Deflection of a horizontal cantilever beam clamped at one end under concentrated end load W: y(x) = [W x² / (6 Y I)] (3L - x).",
    isAnimated: false,
    controls: [
      { id: "cb-load", label: "Tip Load W (N)", min: 100, max: 1000, step: 50, value: 450 },
      { id: "cb-len", label: "Beam Length L (m)", min: 1.0, max: 3.5, step: 0.25, value: 2.5 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const W = parseFloat(vals["cb-load"] || 450);
      const L = parseFloat(vals["cb-len"] || 2.5);

      const wallX = 80, wallY = 120;
      const beamDrawLen = w - 160;

      // Draw Rigid Fixed Support
      ctx.fillStyle = "#334155";
      ctx.fillRect(wallX - 30, wallY - 60, 30, 150);
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 2;
      for (let y = wallY - 50; y < wallY + 80; y += 12) {
        ctx.beginPath(); ctx.moveTo(wallX - 30, y); ctx.lineTo(wallX, y + 10); ctx.stroke();
      }

      // Max deflection scale
      const deltaMax = (W * Math.pow(L, 3)) / (3 * 200 * 0.15) * 0.08;

      // Draw Deflected Beam Top and Bottom Fibers
      const beamThick = 24;
      ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const s = i / 100;
        const x = wallX + s * beamDrawLen;
        // Cubic deflection shape
        const dy = deltaMax * (s * s * (3 - s) / 2);
        if (i === 0) ctx.moveTo(x, wallY + dy - beamThick / 2);
        else ctx.lineTo(x, wallY + dy - beamThick / 2);
      }
      for (let i = 100; i >= 0; i--) {
        const s = i / 100;
        const x = wallX + s * beamDrawLen;
        const dy = deltaMax * (s * s * (3 - s) / 2);
        ctx.lineTo(x, wallY + dy + beamThick / 2);
      }
      ctx.closePath();

      // Stress Gradient fill (Upper tension red, lower compression blue)
      const grad = ctx.createLinearGradient(0, wallY - 12, 0, wallY + 12);
      grad.addColorStop(0, "rgba(239, 68, 68, 0.7)");
      grad.addColorStop(0.5, "#10b981");
      grad.addColorStop(1, "rgba(56, 189, 248, 0.7)");
      ctx.fillStyle = grad;
      ctx.fill();
      ctx.strokeStyle = "#cbd5e1"; ctx.lineWidth = 1.5; ctx.stroke();

      // Tip Load Arrow
      const tipX = wallX + beamDrawLen;
      const tipY = wallY + deltaMax + beamThick / 2;
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(tipX, tipY + 10); ctx.lineTo(tipX, tipY + 50); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(tipX - 6, tipY + 40); ctx.lineTo(tipX, tipY + 50); ctx.lineTo(tipX + 6, tipY + 40); ctx.fill();

      ctx.fillStyle = "#ef4444"; ctx.font = "12px sans-serif";
      ctx.fillText(`Load W = ${W} N`, tipX - 35, tipY + 68);

      // Bending Moment Diagram below
      const bmdY = h - 50;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(wallX, bmdY); ctx.lineTo(tipX, bmdY); ctx.stroke();

      ctx.fillStyle = "rgba(245, 158, 11, 0.2)";
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(wallX, bmdY);
      ctx.lineTo(wallX, bmdY - 45 * (W / 600));
      ctx.lineTo(tipX, bmdY);
      ctx.closePath();
      ctx.fill(); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.font = "10px sans-serif";
      ctx.fillText("Bending Moment M(x) = -W(L - x)", wallX + 20, bmdY - 30);
    }
  },

  // ==========================================
  // 5. Capillary Rise & Soap Bubble
  // ==========================================
  "capillary-bubble-sim": {
    title: "🫧 Jurin's Law Capillarity & Soap Bubble Laplace Pressure",
    desc: "Observe capillary rise h = (2γ cosθ)/(ρ g r) and concave/convex menisci in a bore tube, plus Laplace excess pressure ΔP = 4γ/R in a spherical bubble.",
    isAnimated: true,
    controls: [
      { id: "cap-r", label: "Tube Radius r (mm)", min: 0.3, max: 2.0, step: 0.1, value: 0.8 },
      { id: "cap-ang", label: "Contact Angle θ (°)", min: 0, max: 140, step: 10, value: 20 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const r = parseFloat(vals["cap-r"] || 0.8);
      const thetaDeg = parseFloat(vals["cap-ang"] || 20);
      const thetaRad = thetaDeg * (Math.PI / 180);

      const leftMidX = w * 0.30;
      const rightMidX = w * 0.72;
      const baseLevel = h - 80;

      // 1. Capillary Tube Setup (Left)
      // Height by Jurin's law
      const gamma = 0.073, rho = 1000, g = 9.8;
      const h_jurin_mm = (2 * gamma * Math.cos(thetaRad)) / (rho * g * (r * 1e-3)) * 1000;
      const h_draw = h_jurin_mm * 2.8;

      // Draw Trough Water
      ctx.fillStyle = "rgba(56, 189, 248, 0.35)";
      ctx.fillRect(leftMidX - 90, baseLevel, 180, 50);

      // Capillary Tube Walls
      const tubeW = Math.max(12, r * 22);
      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(leftMidX - tubeW / 2, baseLevel - 150);
      ctx.lineTo(leftMidX - tubeW / 2, baseLevel + 25);
      ctx.moveTo(leftMidX + tubeW / 2, baseLevel - 150);
      ctx.lineTo(leftMidX + tubeW / 2, baseLevel + 25);
      ctx.stroke();

      // Liquid inside tube
      const colTop = baseLevel - h_draw;
      ctx.fillStyle = "rgba(56, 189, 248, 0.65)";
      ctx.fillRect(leftMidX - tubeW / 2 + 1, colTop, tubeW - 2, baseLevel - colTop + 25);

      // Meniscus Curvature
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      const curvOffset = Math.sin(thetaRad) * 6;
      ctx.moveTo(leftMidX - tubeW / 2, colTop);
      ctx.quadraticCurveTo(leftMidX, colTop + (thetaDeg < 90 ? 8 : -8), leftMidX + tubeW / 2, colTop);
      ctx.stroke();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px sans-serif";
      ctx.fillText(`Jurin Rise h = ${h_jurin_mm.toFixed(1)} mm`, leftMidX - 60, baseLevel + 40);

      // 2. Soap Bubble (Right)
      const bRad = 55 + 5 * Math.sin(animTime * 2);
      const bX = rightMidX, bY = h * 0.45;

      const bubGrad = ctx.createRadialGradient(bX - 15, bY - 15, 5, bX, bY, bRad);
      bubGrad.addColorStop(0, "rgba(236, 72, 153, 0.1)");
      bubGrad.addColorStop(0.8, "rgba(56, 189, 248, 0.3)");
      bubGrad.addColorStop(1, "rgba(245, 158, 11, 0.8)");

      ctx.fillStyle = bubGrad;
      ctx.beginPath(); ctx.arc(bX, bY, bRad, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "rgba(255, 255, 255, 0.8)"; ctx.lineWidth = 2; ctx.stroke();

      // Bubble highlight reflection
      ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
      ctx.beginPath(); ctx.ellipse(bX - bRad * 0.45, bY - bRad * 0.45, 12, 5, -0.6, 0, Math.PI * 2); ctx.fill();

      const deltaP = (4 * 0.025 / (bRad * 1e-3)).toFixed(1);
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px monospace";
      ctx.fillText(`Soap Bubble Laplace Law:`, rightMidX - 80, bY + bRad + 25);
      ctx.fillText(`ΔP = 4γ/R = ${deltaP} Pa`, rightMidX - 80, bY + bRad + 42);
    }
  },

  // ==========================================
  // 6. Laminar vs Turbulent Pipe Flow
  // ==========================================
  "hydro-pipe-flow-sim": {
    title: "🌊 Laminar Streamlines vs Turbulent Pipe Flow & Reynolds Number",
    desc: "Observe fluid laminae slide past one another at low Reynolds numbers, transitioning to chaotic tumbling vortex eddies as velocity increases.",
    isAnimated: true,
    controls: [
      { id: "hpf-v", label: "Flow Velocity v (m/s)", min: 0.2, max: 2.8, step: 0.2, value: 0.8 },
      { id: "hpf-eta", label: "Viscosity η (mPa·s)", min: 0.8, max: 4.0, step: 0.4, value: 1.6 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const v = parseFloat(vals["hpf-v"] || 0.8);
      const eta = parseFloat(vals["hpf-eta"] || 1.6);
      const D = 0.05, rho = 1000;
      const Re = Math.round((rho * v * D) / (eta * 1e-3));

      const py1 = 70, py2 = h - 90;
      const pipeH = py2 - py1;
      const pipeMidY = (py1 + py2) / 2;

      // Draw Pipe Solid Walls
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(0, py1 - 15, w, 15);
      ctx.fillRect(0, py2, w, 15);
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(0, py1); ctx.lineTo(w, py1);
      ctx.moveTo(0, py2); ctx.lineTo(w, py2);
      ctx.stroke();

      // Fluid particles stream
      const isTurbulent = Re > 2800;
      const isTransition = Re >= 2000 && Re <= 2800;

      const numStreamlines = 9;
      for (let s = 1; s < numStreamlines; s++) {
        const yRel = s / numStreamlines;
        const yBase = py1 + yRel * pipeH;
        // Parabolic profile: v(r) = vmax * (1 - (r/R)^2)
        const rNorm = 2 * (yRel - 0.5);
        const vLayer = v * (1 - rNorm * rNorm) * 120;

        ctx.strokeStyle = isTurbulent ? "rgba(239, 68, 68, 0.45)" : "rgba(56, 189, 248, 0.45)";
        ctx.lineWidth = 1.5;
        ctx.beginPath();

        for (let x = 0; x <= w; x += 15) {
          let dy = 0;
          if (isTurbulent) {
            dy = Math.sin(x * 0.05 + animTime * 6 + s) * 14 * Math.sin(animTime * 3 + x * 0.02);
          } else if (isTransition) {
            dy = Math.sin(x * 0.03 + animTime * 3) * 4;
          }
          if (x === 0) ctx.moveTo(x, yBase + dy);
          else ctx.lineTo(x, yBase + dy);
        }
        ctx.stroke();

        // Moving tracer bubbles along streamline
        for (let p = 0; p < 3; p++) {
          const px = ((animTime * vLayer * 0.8 + p * 180 + s * 45) % (w + 40)) - 20;
          let pdy = 0;
          if (isTurbulent) pdy = Math.sin(px * 0.05 + animTime * 6 + s) * 14;
          ctx.fillStyle = isTurbulent ? "#ec4899" : "#38bdf8";
          ctx.beginPath();
          ctx.arc(px, yBase + pdy, 3, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // Parabolic velocity profile on left
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let y = py1; y <= py2; y += 4) {
        const rNorm = (y - pipeMidY) / (pipeH / 2);
        const vx = 30 + (1 - rNorm * rNorm) * 70 * (v / 1.5);
        if (y === py1) ctx.moveTo(vx, y); else ctx.lineTo(vx, y);
      }
      ctx.stroke();

      // Readout
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(w - 280, h - 75, 260, 60);
      ctx.strokeRect(w - 280, h - 75, 260, 60);
      ctx.fillStyle = isTurbulent ? "#ef4444" : isTransition ? "#f59e0b" : "#10b981";
      ctx.font = "12px monospace";
      ctx.fillText(`Reynolds Number Re = ${Re}`, w - 265, h - 55);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`Flow Regime: ${isTurbulent ? "TURBULENT (Eddies)" : isTransition ? "TRANSITIONAL" : "LAMINAR (Streamline)"}`, w - 265, h - 35);
    }
  },

  // ==========================================
  // 7. Venturi Meter & Torricelli Efflux
  // ==========================================
  "venturi-bernoulli-sim": {
    title: "🚀 Venturi Constriction Effect & Torricelli Efflux Tank",
    desc: "Demonstrate Bernoulli pressure drop across a throat constriction A1 > A2 and gravity efflux velocity v = √(2gh) from a liquid tank orifice.",
    isAnimated: true,
    controls: [
      { id: "vb-ratio", label: "Area Ratio A1/A2", min: 1.5, max: 4.5, step: 0.5, value: 3.0 },
      { id: "vb-v1", label: "Inlet Speed v1 (m/s)", min: 0.5, max: 2.2, step: 0.1, value: 1.2 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const ratio = parseFloat(vals["vb-ratio"] || 3.0);
      const v1 = parseFloat(vals["vb-v1"] || 1.2);
      const v2 = v1 * ratio;

      const midY = h * 0.55;
      const pipeH1 = 80;
      const pipeH2 = pipeH1 / Math.sqrt(ratio);

      // Venturi Profile Contours
      ctx.fillStyle = "rgba(56, 189, 248, 0.12)";
      ctx.beginPath();
      ctx.moveTo(40, midY - pipeH1 / 2);
      ctx.lineTo(w * 0.35, midY - pipeH1 / 2);
      ctx.lineTo(w * 0.45, midY - pipeH2 / 2);
      ctx.lineTo(w * 0.55, midY - pipeH2 / 2);
      ctx.lineTo(w * 0.65, midY - pipeH1 / 2);
      ctx.lineTo(w - 40, midY - pipeH1 / 2);
      ctx.lineTo(w - 40, midY + pipeH1 / 2);
      ctx.lineTo(w * 0.65, midY + pipeH1 / 2);
      ctx.lineTo(w * 0.55, midY + pipeH2 / 2);
      ctx.lineTo(w * 0.45, midY + pipeH2 / 2);
      ctx.lineTo(w * 0.35, midY + pipeH1 / 2);
      ctx.lineTo(40, midY + pipeH1 / 2);
      ctx.closePath();
      ctx.fill();
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 2.5; ctx.stroke();

      // Piezometer vertical columns
      // P1 vs P2
      const hCol1 = 90;
      const deltaP_h = (v2 * v2 - v1 * v1) / (2 * 9.8) * 45;
      const hCol2 = Math.max(15, hCol1 - deltaP_h);

      // Manometer 1 (Inlet)
      const m1X = w * 0.25;
      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 2;
      ctx.strokeRect(m1X - 7, midY - pipeH1 / 2 - 110, 14, 110);
      ctx.fillStyle = "rgba(56, 189, 248, 0.7)";
      ctx.fillRect(m1X - 6, midY - pipeH1 / 2 - hCol1, 12, hCol1);

      // Manometer 2 (Throat)
      const m2X = w * 0.50;
      ctx.strokeRect(m2X - 7, midY - pipeH2 / 2 - 110, 14, 110);
      ctx.fillStyle = "rgba(56, 189, 248, 0.7)";
      ctx.fillRect(m2X - 6, midY - pipeH2 / 2 - hCol2, 12, hCol2);

      // Flowing streamline tracer particles
      for (let i = 0; i < 20; i++) {
        const frac = ((animTime * 0.4 + i * 0.05) % 1.0);
        const px = 40 + frac * (w - 80);
        let curH = pipeH1;
        let curV = v1;
        if (px >= w * 0.35 && px <= w * 0.45) {
          const t = (px - w * 0.35) / (w * 0.10);
          curH = pipeH1 + t * (pipeH2 - pipeH1);
          curV = v1 + t * (v2 - v1);
        } else if (px > w * 0.45 && px <= w * 0.55) {
          curH = pipeH2; curV = v2;
        } else if (px > w * 0.55 && px <= w * 0.65) {
          const t = (px - w * 0.55) / (w * 0.10);
          curH = pipeH2 + t * (pipeH1 - pipeH2);
          curV = v2 + t * (v1 - v2);
        }
        const py = midY + ((i % 5) - 2) * (curH / 6);
        ctx.fillStyle = "#38bdf8";
        ctx.beginPath(); ctx.arc(px, py, 2.5, 0, Math.PI * 2); ctx.fill();
      }

      // Readouts
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(20, h - 80, 320, 65);
      ctx.strokeRect(20, h - 80, 320, 65);
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px monospace";
      ctx.fillText(`Bernoulli Continuity & Pressure:`, 30, h - 60);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Inlet Speed v1:  ${v1.toFixed(2)} m/s (High Pressure)`, 30, h - 42);
      ctx.fillStyle = "#ef4444";
      ctx.fillText(`Throat Speed v2: ${v2.toFixed(2)} m/s (Low Pressure)`, 30, h - 24);
    }
  },

  // ==========================================
  // 8. Stokes Viscous Terminal Velocity
  // ==========================================
  "viscosity-stokes-sim": {
    title: "💧 Stokes' Law Viscous Falling Sphere & Terminal Velocity",
    desc: "Observe a spherical body achieve terminal velocity vt = [2 r² (ρ - σ) g] / (9 η) under gravity, Archimedes buoyancy, and Stokes drag.",
    isAnimated: true,
    controls: [
      { id: "stk-r", label: "Sphere Radius r (mm)", min: 0.8, max: 3.0, step: 0.2, value: 1.5 },
      { id: "stk-eta", label: "Liquid Viscosity η (Pa·s)", min: 0.2, max: 2.0, step: 0.2, value: 0.8 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const r_mm = parseFloat(vals["stk-r"] || 1.5);
      const eta = parseFloat(vals["stk-eta"] || 0.8);
      const r_m = r_mm * 1e-3;
      const rho = 7800, sigma = 950, g = 9.8;
      const vt = (2 * r_m * r_m * (rho - sigma) * g) / (9 * eta);

      const colX = w * 0.32, colW = 100;
      const topY = 40, botY = h - 50;

      // Draw Glass Cylinder filled with viscous fluid
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 2.5;
      ctx.strokeRect(colX - colW / 2, topY, colW, botY - topY);
      ctx.fillStyle = "rgba(245, 158, 11, 0.15)";
      ctx.fillRect(colX - colW / 2, topY, colW, botY - topY);

      // Sphere animation loop
      const loopTime = (animTime * 1.5) % 4.0;
      // v(t) = vt * (1 - exp(-t / tau))
      const tau = (2 * r_m * r_m * rho) / (9 * eta);
      const yNorm = Math.min(1.0, loopTime / 3.0);
      const sphereY = topY + 20 + yNorm * (botY - topY - 40);

      const sphereDrawR = Math.max(6, r_mm * 5);
      ctx.fillStyle = "#94a3b8";
      ctx.beginPath(); ctx.arc(colX, sphereY, sphereDrawR, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#f8fafc"; ctx.lineWidth = 1.5; ctx.stroke();

      // Force Vectors on Sphere
      // 1. Gravity (Down)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(colX, sphereY); ctx.lineTo(colX, sphereY + 45); ctx.stroke();
      ctx.fillStyle = "#10b981";
      ctx.fillText("W (mg)", colX + 8, sphereY + 40);

      // 2. Buoyancy (Up)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(colX - 8, sphereY); ctx.lineTo(colX - 8, sphereY - 18); ctx.stroke();

      // 3. Stokes Drag (Up)
      const dragLen = 27 * Math.min(1.0, loopTime / 1.5);
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(colX + 8, sphereY); ctx.lineTo(colX + 8, sphereY - dragLen); ctx.stroke();
      ctx.fillStyle = "#ef4444";
      ctx.fillText("Fd (6πηrv)", colX + 15, sphereY - 15);

      // Graph on the right: Velocity vs Time
      const gx = w * 0.58, gy = h - 60, gw = w * 0.36, gh = 130;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(gx, gy); ctx.lineTo(gx + gw, gy);
      ctx.moveTo(gx, gy); ctx.lineTo(gx, gy - gh);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("Time t →", gx + gw - 40, gy + 18);
      ctx.fillText("Speed v(t) ↑", gx - 20, gy - gh - 8);

      // Asymptotic Curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let t = 0; t <= 100; t++) {
        const px = gx + (t / 100) * gw;
        const speedFrac = 1 - Math.exp(-t / 18);
        const py = gy - speedFrac * (gh * 0.75);
        if (t === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Asymptote dashed line
      ctx.strokeStyle = "#ef4444"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(gx, gy - gh * 0.75); ctx.lineTo(gx + gw, gy - gh * 0.75); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444";
      ctx.fillText(`Terminal vt = ${(vt * 100).toFixed(2)} cm/s`, gx + 30, gy - gh * 0.75 - 5);
    }
  },

  // ==========================================
  // 9. SHM Reference Circle & Resonance
  // ==========================================
  "shm-resonance-sim": {
    title: "🔄 SHM Reference Circle & Forced Mechanical Resonance",
    desc: "Visualize SHM as the 1D projection of uniform circular motion, damped decay regimes, and resonance magnification Q as driving frequency sweeps across ω₀.",
    isAnimated: true,
    controls: [
      { id: "shm-w", label: "Driving Frequency ω / ω₀", min: 0.4, max: 1.6, step: 0.05, value: 1.0 },
      { id: "shm-damp", label: "Damping γ / ω₀", min: 0.02, max: 0.25, step: 0.02, value: 0.08 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const wRatio = parseFloat(vals["shm-w"] || 1.0);
      const gamma = parseFloat(vals["shm-damp"] || 0.08);

      const cx = w * 0.25, cy = h * 0.48;
      const refR = 55;

      // 1. Reference Circle
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.arc(cx, cy, refR, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      const phi = animTime * 3 * wRatio;
      const px = cx + refR * Math.cos(phi);
      const py = cy - refR * Math.sin(phi);

      // Rotating phasor
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(px, py); ctx.stroke();
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(px, py, 5, 0, Math.PI * 2); ctx.fill();

      // Vertical projection line
      const projY = py;
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.setLineDash([2, 2]);
      ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(cx + 85, projY); ctx.stroke();
      ctx.setLineDash([]);

      // Oscillating Mass on Spring
      const springX = cx + 85;
      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(springX, projY, 8, 0, Math.PI * 2); ctx.fill();

      // 2. Resonance Curve on the right
      const rx = w * 0.52, ry = h - 60, rw = w * 0.42, rh = 135;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(rx, ry); ctx.lineTo(rx + rw, ry);
      ctx.moveTo(rx, ry); ctx.lineTo(rx, ry - rh);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("Driving Frequency ω/ω₀ →", rx + rw - 110, ry + 18);
      ctx.fillText("Amplitude A(ω) ↑", rx - 20, ry - rh - 8);

      // Lorentzian response curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const u = 0.3 + (i / 100) * 1.4;
        const denom = Math.sqrt(Math.pow(1 - u * u, 2) + 4 * gamma * gamma * u * u);
        const amp = 1.0 / denom;
        const gx = rx + ((u - 0.3) / 1.4) * rw;
        const gy = ry - Math.min(rh - 10, amp * 12);
        if (i === 0) ctx.moveTo(gx, gy); else ctx.lineTo(gx, gy);
      }
      ctx.stroke();

      // Current operating point on resonance curve
      const curDenom = Math.sqrt(Math.pow(1 - wRatio * wRatio, 2) + 4 * gamma * gamma * wRatio * wRatio);
      const curAmp = 1.0 / curDenom;
      const opX = rx + ((wRatio - 0.3) / 1.4) * rw;
      const opY = ry - Math.min(rh - 10, curAmp * 12);

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(opX, opY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.stroke();

      const Q = (1 / (2 * gamma)).toFixed(1);
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px monospace";
      ctx.fillText(`Quality Factor Q = ${Q}`, rx + 15, ry - rh + 15);
      ctx.fillText(`Amp Magnification: ${curAmp.toFixed(1)}x`, rx + 15, ry - rh + 32);
    }
  },

  // ==========================================
  // 10. Continuous Traveling Waves
  // ==========================================
  "traveling-wave-sim": {
    title: "〰️ 1D Continuous Traveling Wave & Harmonic Dispersion",
    desc: "Observe continuous harmonic wave propagation ψ(x,t) = A cos(kx - ωt) with dynamic phase velocity and transverse particle motion.",
    isAnimated: true,
    controls: [
      { id: "tw-freq", label: "Wave Frequency f (Hz)", min: 0.5, max: 2.5, step: 0.1, value: 1.2 },
      { id: "tw-lambda", label: "Wavelength λ (m)", min: 1.0, max: 4.5, step: 0.25, value: 2.5 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const f = parseFloat(vals["tw-freq"] || 1.2);
      const lambda = parseFloat(vals["tw-lambda"] || 2.5);
      const v = f * lambda;
      const omega = 2 * Math.PI * f;
      const k = (2 * Math.PI) / (lambda * 80); // scale for pixels

      const midY = h * 0.48;
      const amp = 42;

      // Draw Center Baseline
      ctx.strokeStyle = "rgba(148, 163, 184, 0.2)"; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(30, midY); ctx.lineTo(w - 30, midY); ctx.stroke();
      ctx.setLineDash([]);

      // Traveling Wave Curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let x = 30; x <= w - 30; x += 3) {
        const y = midY + amp * Math.cos(k * x - omega * animTime);
        if (x === 30) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Transverse Oscillating Particles on String
      for (let i = 0; i < 7; i++) {
        const px = 60 + i * ((w - 120) / 6);
        const py = midY + amp * Math.cos(k * px - omega * animTime);
        ctx.fillStyle = "#10b981";
        ctx.beginPath(); ctx.arc(px, py, 5, 0, Math.PI * 2); ctx.fill();

        // Transverse vertical displacement line
        ctx.strokeStyle = "rgba(16, 185, 129, 0.35)"; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.moveTo(px, midY); ctx.lineTo(px, py); ctx.stroke();
      }

      // Readout
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(30, h - 75, 280, 60);
      ctx.strokeRect(30, h - 75, 280, 60);
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px monospace";
      ctx.fillText(`Traveling Wave Parameters:`, 42, h - 55);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Phase Speed v = f·λ = ${v.toFixed(2)} m/s`, 42, h - 35);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Wavenumber k = ${(2 * Math.PI / lambda).toFixed(2)} rad/m`, 42, h - 20);
    }
  },

  // ==========================================
  // 11. Stretched String Standing Waves
  // ==========================================
  "standing-wave-sim": {
    title: "🎸 Stretched String Normal Modes & Nodes / Antinodes",
    desc: "Observe stationary normal modes fn = (n/2L)√(T/μ) on a clamped string. Identify stationary nodes of permanent zero displacement and resonant antinodes.",
    isAnimated: true,
    controls: [
      { id: "sw-mode", label: "Mode Harmonic Number n", min: 1, max: 5, step: 1, value: 3 },
      { id: "sw-t", label: "String Tension T (N)", min: 100, max: 400, step: 50, value: 250 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const n = parseInt(vals["sw-mode"] || 3);
      const T = parseFloat(vals["sw-t"] || 250);
      const mu = 0.004;
      const v = Math.sqrt(T / mu);
      const L_px = w - 120;
      const leftX = 60, rightX = leftX + L_px;
      const midY = h * 0.48;

      const f1 = v / (2 * 1.0); // 1m virtual length
      const fn = n * f1;
      const omega = 4.0; // visual speed

      const maxAmp = 46;
      const tOsc = Math.cos(omega * animTime);

      // Clamped Wall Supports
      ctx.fillStyle = "#334155";
      ctx.fillRect(leftX - 16, midY - 60, 16, 120);
      ctx.fillRect(rightX, midY - 60, 16, 120);

      // Envelope Outline (translucent)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.25)"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      for (let x = 0; x <= L_px; x += 3) {
        const yTop = midY + maxAmp * Math.sin((n * Math.PI * x) / L_px);
        if (x === 0) ctx.moveTo(leftX + x, yTop); else ctx.lineTo(leftX + x, yTop);
      }
      ctx.stroke();
      ctx.beginPath();
      for (let x = 0; x <= L_px; x += 3) {
        const yBot = midY - maxAmp * Math.sin((n * Math.PI * x) / L_px);
        if (x === 0) ctx.moveTo(leftX + x, yBot); else ctx.lineTo(leftX + x, yBot);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Dynamic Vibrating String
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let x = 0; x <= L_px; x += 3) {
        const y = midY + maxAmp * Math.sin((n * Math.PI * x) / L_px) * tOsc;
        if (x === 0) ctx.moveTo(leftX + x, y); else ctx.lineTo(leftX + x, y);
      }
      ctx.stroke();

      // Nodes (Red stationary markers)
      for (let i = 0; i <= n; i++) {
        const nx = leftX + (i / n) * L_px;
        ctx.fillStyle = "#ef4444";
        ctx.beginPath(); ctx.arc(nx, midY, 5, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#fca5a5"; ctx.font = "10px sans-serif";
        ctx.fillText("N", nx - 3, midY - 12);
      }

      // Antinodes (Cyan markers)
      for (let i = 0; i < n; i++) {
        const ax = leftX + ((i + 0.5) / n) * L_px;
        const ay = midY + maxAmp * Math.sin((n * Math.PI * (ax - leftX)) / L_px) * tOsc;
        ctx.fillStyle = "#38bdf8";
        ctx.beginPath(); ctx.arc(ax, ay, 4, 0, Math.PI * 2); ctx.fill();
      }

      // Readout
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(leftX, h - 75, 320, 60);
      ctx.strokeRect(leftX, h - 75, 320, 60);
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px monospace";
      ctx.fillText(`Normal Mode n = ${n} (${n === 1 ? "Fundamental" : n - 1 + "th Overtone"}):`, leftX + 12, h - 55);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Nodes: ${n + 1} | Antinodes: ${n}`, leftX + 12, h - 35);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Frequency: fn = ${fn.toFixed(1)} Hz (v = ${v.toFixed(0)} m/s)`, leftX + 12, h - 20);
    }
  },

  // ==========================================
  // 12. Acoustic Beats & Doppler Mach Cone
  // ==========================================
  "sound-beats-doppler-sim": {
    title: "🔊 Acoustic Beats, Doppler Wavefront Compression & Mach Cone",
    desc: "Observe envelope beats between neighboring audio frequencies and Doppler compression of spherical wavefronts from subsonic speeds to supersonic Mach 1.4 shock cones.",
    isAnimated: true,
    controls: [
      { id: "sbd-mach", label: "Source Mach Number M", min: 0.0, max: 1.4, step: 0.1, value: 0.6 },
      { id: "sbd-beat", label: "Beat Frequency Δf (Hz)", min: 1.0, max: 8.0, step: 0.5, value: 3.5 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const M = parseFloat(vals["sbd-mach"] || 0.6);
      const beatFreq = parseFloat(vals["sbd-beat"] || 3.5);

      // Top Half: Acoustic Beats Waveform
      const bH = h * 0.35, bMidY = bH * 0.55;
      ctx.strokeStyle = "rgba(148, 163, 184, 0.15)"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(30, bMidY); ctx.lineTo(w - 30, bMidY); ctx.stroke();

      // Envelope
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.setLineDash([2, 2]);
      ctx.beginPath();
      for (let x = 30; x <= w - 30; x += 3) {
        const env = 30 * Math.abs(Math.cos(beatFreq * 0.015 * x - animTime * 3));
        if (x === 30) ctx.moveTo(x, bMidY - env); else ctx.lineTo(x, bMidY - env);
      }
      ctx.stroke();
      ctx.beginPath();
      for (let x = 30; x <= w - 30; x += 3) {
        const env = 30 * Math.abs(Math.cos(beatFreq * 0.015 * x - animTime * 3));
        if (x === 30) ctx.moveTo(x, bMidY + env); else ctx.lineTo(x, bMidY + env);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Rapid Carrier Oscillation inside Envelope
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let x = 30; x <= w - 30; x += 2) {
        const env = 30 * Math.cos(beatFreq * 0.015 * x - animTime * 3);
        const y = bMidY + env * Math.cos(x * 0.25);
        if (x === 30) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      ctx.fillStyle = "#f59e0b"; ctx.font = "10px monospace";
      ctx.fillText(`Beats Envelope: f_beat = |f1 - f2| = ${beatFreq.toFixed(1)} Hz`, 40, 20);

      // Bottom Half: Doppler Wavefronts & Mach Cone
      const dY = h * 0.70;
      const c = 70; // speed of sound in pixels/sec
      const vs = M * c;
      const srcPeriod = 0.4;
      const numWaves = 10;

      // Source current position
      const cycleT = (animTime * 1.2) % 4.0;
      const srcX = 60 + cycleT * vs;

      // Draw wavefront circles emitted in the past
      for (let i = 1; i <= numWaves; i++) {
        const tAge = (animTime * 1.2 - i * srcPeriod) % 4.0;
        if (tAge > 0) {
          const emitX = 60 + (cycleT - tAge) * vs;
          const radius = tAge * c;
          if (radius > 0 && radius < w) {
            ctx.strokeStyle = M >= 1.0 ? "rgba(239, 68, 68, 0.4)" : "rgba(56, 189, 248, 0.4)";
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.arc(emitX, dY, radius, 0, Math.PI * 2);
            ctx.stroke();
          }
        }
      }

      // Supersonic Mach Cone Envelope
      if (M > 1.0) {
        const sinTheta = 1.0 / M;
        const theta = Math.asin(sinTheta);
        ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
        // Upper shock line
        ctx.beginPath();
        ctx.moveTo(srcX, dY);
        ctx.lineTo(srcX - 180, dY - 180 * Math.tan(theta));
        ctx.stroke();
        // Lower shock line
        ctx.beginPath();
        ctx.moveTo(srcX, dY);
        ctx.lineTo(srcX - 180, dY + 180 * Math.tan(theta));
        ctx.stroke();

        ctx.fillStyle = "#ef4444"; ctx.font = "11px monospace";
        ctx.fillText(`Mach Cone Shock Front (θ = ${(theta * 180 / Math.PI).toFixed(1)}°)`, srcX - 160, dY - 80);
      }

      // Moving Source
      ctx.fillStyle = "#fbbf24";
      ctx.beginPath(); ctx.arc(srcX, dY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();
    }
  }
};


// Universal Engine Integration Adapter for Properties of Matter and Waves
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  if (window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }

  const simConfig = (window.MATTER_SIMS && window.MATTER_SIMS[simType]) || (window.STATMECH_SIMS && window.STATMECH_SIMS[simType]);
  if (!simConfig) {
    console.warn('Properties of Matter simulation not found:', simType);
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
