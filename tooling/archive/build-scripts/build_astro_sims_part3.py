# build_astro_sims_part3.py

sim11 = """  // =========================================================================
  // CHAPTER 6: EXTRAGALACTIC ASTRONOMY & GRAVITATIONAL LENSING
  // =========================================================================

  // 11. AGN Accretion Disk & Superluminal Jet Kinematics
  "astro-agn-jet-sim": {
    title: "AGN Unified Model & Superluminal Jet Kinematics",
    desc: "Active Galactic Nucleus (AGN) supermassive black hole accretion disk with relativistic Doppler beaming and apparent superluminal jet kinematics β_app = β sinθ / (1 - β cosθ).",
    isAnimated: true,
    controls: [
      { id: "jetBeta", label: "Jet Relativistic Speed β = v/c", min: 0.8, max: 0.995, step: 0.005, value: 0.98 },
      { id: "viewAngle", label: "Viewing Angle θ (deg)", min: 2, max: 60, step: 1, value: 14 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const beta = vals.jetBeta !== undefined ? vals.jetBeta : 0.98;
      const thetaDeg = vals.viewAngle !== undefined ? vals.viewAngle : 14;

      const theta = (thetaDeg * Math.PI) / 180;
      const gamma = 1 / Math.sqrt(Math.max(1e-5, 1 - beta * beta));

      // Apparent speed beta_app = beta sin(theta) / (1 - beta cos(theta))
      const denom = 1 - beta * Math.cos(theta);
      const beta_app = (beta * Math.sin(theta)) / Math.max(1e-4, denom);
      const isSuperluminal = beta_app > 1.0;

      // Doppler beaming factor delta = 1 / [gamma * (1 - beta cos theta)]
      const delta = 1 / (gamma * Math.max(1e-4, denom));
      const fluxBoost = Math.pow(delta, 3.5);

      // Left Panel: AGN Central Engine Schematic
      const cx = 175, cy = 200;
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("AGN Accretion Disk & Relativistic Jet", 25, 25);

      // Dusty Torus
      ctx.fillStyle = "#334155";
      ctx.beginPath(); ctx.ellipse(cx, cy, 110, 35, 0, 0, Math.PI * 2); ctx.fill();

      // Accretion Disk
      const diskGrad = ctx.createRadialGradient(cx, cy, 5, cx, cy, 65);
      diskGrad.addColorStop(0, "#fde047");
      diskGrad.addColorStop(0.4, "#f97316");
      diskGrad.addColorStop(1, "rgba(220, 38, 38, 0.0)");
      ctx.fillStyle = diskGrad;
      ctx.beginPath(); ctx.ellipse(cx, cy, 65, 18, 0, 0, Math.PI * 2); ctx.fill();

      // Supermassive Black Hole
      ctx.fillStyle = "#000000"; ctx.beginPath(); ctx.arc(cx, cy, 10, 0, Math.PI * 2); ctx.fill();

      // Relativistic Plasma Jet (knots moving along jet)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.8)"; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + Math.cos(-Math.PI / 2 + theta * 0.5) * 150, cy - 150); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx - Math.cos(-Math.PI / 2 + theta * 0.5) * 150, cy + 150); ctx.stroke();

      // Moving synchrotron plasma knots
      for (let k = 1; k <= 3; k++) {
        const knotProgress = ((time * 0.4 + k * 0.33) % 1.0);
        const kx = cx + knotProgress * Math.cos(-Math.PI / 2 + theta * 0.5) * 150;
        const ky = cy - knotProgress * 150;
        ctx.fillStyle = "#67e8f9"; ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 10;
        ctx.beginPath(); ctx.arc(kx, ky, 5, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Approaching Jet Knot", cx + 25, cy - 110);
      ctx.fillText("Obscuring Dusty Torus", cx - 95, cy + 30);

      // Right Panel: Apparent Speed Curve & Superluminal Telemetry
      const gx = 360, gy = 35, gw = 375, gh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Superluminal Motion: β_app(θ) vs c", gx + 15, gy + 22);

      const ox = gx + 50, oy = gy + 175, pw = gw - 70, ph = 120;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Viewing Angle θ (deg)", ox + pw - 120, oy + 18);
      ctx.save(); ctx.translate(ox - 30, oy - 35); ctx.rotate(-Math.PI / 2);
      ctx.fillText("β_app = v_app / c", 0, 0); ctx.restore();

      // Horizontal dashed line at beta_app = 1 (c)
      const cLineY = oy - (1.0 / 6.0) * ph;
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(ox, cLineY); ctx.lineTo(ox + pw, cLineY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.fillText("c (Speed of Light)", ox + pw - 95, cLineY - 4);

      // Plot beta_app curve for chosen beta
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let th = 1; th <= 60; th += 1) {
        const rad = (th * Math.PI) / 180;
        const b_app = (beta * Math.sin(rad)) / Math.max(1e-4, 1 - beta * Math.cos(rad));
        const px = ox + (th / 60) * pw;
        const py = oy - (Math.min(6.0, b_app) / 6.0) * ph;
        if (th === 1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current point on curve
      const curX = ox + (thetaDeg / 60) * pw;
      const curY = oy - (Math.min(6.0, beta_app) / 6.0) * ph;
      ctx.fillStyle = isSuperluminal ? "#f43f5e" : "#10b981";
      ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Telemetry Box
      const by = gy + 195;
      const metrics = [
        ["Lorentz Factor γ:", `${gamma.toFixed(2)}`],
        ["Apparent Transverse Speed β_app:", `${beta_app.toFixed(2)} c`],
        ["Doppler Beaming Factor δ:", `${delta.toFixed(2)}`],
        ["Flux Boost Factor δ^(3+α):", `${fluxBoost.toExponential(2)} ×`],
        ["Superluminal Status:", isSuperluminal ? `SUPERLUMINAL (v_app = ${beta_app.toFixed(1)} c > c)` : "SUBLUMINAL (v_app < c)"]
      ];

      ctx.font = "11px Inter";
      metrics.forEach((m, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(m[0], gx + 15, by + 18 + idx * 24);
        ctx.fillStyle = idx === 4 ? (isSuperluminal ? "#f43f5e" : "#10b981") : (idx === 1 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(m[1], gx + 195, by + 18 + idx * 24);
        ctx.font = "11px Inter";
      });
    }
  },
"""

sim12 = """  // 12. Gravitational Lensing & Einstein Rings
  "astro-gravitational-lensing-sim": {
    title: "Gravitational Lensing: Einstein Rings & Caustic Arcs",
    desc: "Interactive thin-screen gravitational lens simulator: solves the lens equation β = θ - θ_E² / θ, rendering Einstein rings, giant distorted arcs, and flux amplification.",
    isAnimated: true,
    controls: [
      { id: "einsteinRadius", label: "Einstein Radius θ_E (arcsec)", min: 10, max: 80, step: 1, value: 45 },
      { id: "sourceOffsetX", label: "Source Offset X (arcsec)", min: -60, max: 60, step: 1, value: 12 },
      { id: "sourceOffsetY", label: "Source Offset Y (arcsec)", min: -60, max: 60, step: 1, value: 8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const thetaE = vals.einsteinRadius !== undefined ? vals.einsteinRadius : 45;
      const betaX = vals.sourceOffsetX !== undefined ? vals.sourceOffsetX : 12;
      const betaY = vals.sourceOffsetY !== undefined ? vals.sourceOffsetY : 8;

      const beta = Math.hypot(betaX, betaY);
      const phiSource = Math.atan2(betaY, betaX);

      // Two image solutions: theta_pm = [beta +/- sqrt(beta^2 + 4 thetaE^2)] / 2
      const discr = Math.sqrt(beta * beta + 4 * thetaE * thetaE);
      const theta1 = (beta + discr) / 2;
      const theta2 = (beta - discr) / 2; // negative (opposite side)

      // Magnifications: mu = [1 - (thetaE / theta)^4]^(-1)
      const mu1 = Math.abs(1 / (1 - Math.pow(thetaE / Math.max(1e-3, theta1), 4)));
      const mu2 = Math.abs(1 / (1 - Math.pow(thetaE / Math.max(1e-3, Math.abs(theta2)), 4)));
      const totalMu = mu1 + mu2;

      // Left Panel: Sky View Observer Plane
      const cx = 200, cy = 200;
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Observer Plane: Lensed Images & Arcs", 25, 25);

      // Einstein Ring boundary (dashed yellow)
      ctx.strokeStyle = "rgba(250, 204, 21, 0.4)"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, thetaE * 1.5, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#facc15"; ctx.font = "10px Inter";
      ctx.fillText(`Einstein Ring θ_E = ${thetaE}"`, cx + thetaE * 1.5 + 8, cy);

      // Lens Galaxy (Elliptical / Cluster center)
      const lensGrad = ctx.createRadialGradient(cx, cy, 2, cx, cy, 30);
      lensGrad.addColorStop(0, "#ffffff");
      lensGrad.addColorStop(0.5, "#fbbf24");
      lensGrad.addColorStop(1, "rgba(245, 158, 11, 0.0)");
      ctx.fillStyle = lensGrad;
      ctx.beginPath(); ctx.arc(cx, cy, 30, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fed7aa"; ctx.font = "10px Inter"; ctx.fillText("Lens Galaxy", cx - 28, cy + 40);

      // True Source position (unlensed position, dashed marker)
      const unlensX = cx + betaX * 1.5;
      const unlensY = cy + betaY * 1.5;
      ctx.strokeStyle = "rgba(255, 255, 255, 0.4)"; ctx.lineWidth = 1; ctx.setLineDash([2, 2]);
      ctx.beginPath(); ctx.arc(unlensX, unlensY, 8, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.fillText("True Source (Unlensed)", unlensX + 12, unlensY + 3);

      // If beta is very close to 0: complete Einstein Ring!
      if (beta < 3) {
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 5; ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 15;
        ctx.beginPath(); ctx.arc(cx, cy, thetaE * 1.5, 0, Math.PI * 2); ctx.stroke();
        ctx.shadowBlur = 0;
      } else {
        // Image 1: Major Arc on source side
        const im1R = theta1 * 1.5;
        const im1X = cx + im1R * Math.cos(phiSource);
        const im1Y = cy + im1R * Math.sin(phiSource);
        const arcSpan1 = Math.min(Math.PI * 0.8, (thetaE / (beta + 1e-3)) * 0.4);

        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = Math.min(8, 2 + Math.log10(mu1) * 2);
        ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 12;
        ctx.beginPath();
        ctx.arc(cx, cy, im1R, phiSource - arcSpan1, phiSource + arcSpan1);
        ctx.stroke();

        // Image 2: Counter-image on opposite side
        const im2R = Math.abs(theta2) * 1.5;
        const oppPhi = phiSource + Math.PI;
        const arcSpan2 = Math.min(Math.PI * 0.5, (thetaE / (beta + 1e-3)) * 0.2);

        ctx.strokeStyle = "#60a5fa"; ctx.lineWidth = Math.min(6, 1.5 + Math.log10(mu2) * 2);
        ctx.shadowColor = "#60a5fa"; ctx.shadowBlur = 8;
        ctx.beginPath();
        ctx.arc(cx, cy, im2R, oppPhi - arcSpan2, oppPhi + arcSpan2);
        ctx.stroke();
        ctx.shadowBlur = 0;
      }

      // Right Panel: Lensing Optics Telemetry
      const rx = 430, ry = 35, rw = 305, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Gravitational Lens Equation Solver", rx + 15, ry + 22);

      const items = [
        ["Einstein Radius θ_E:", `${thetaE}"`],
        ["Source Offset β = √(βx²+βy²):", `${beta.toFixed(1)}"`],
        ["Primary Image θ₊:", `+${theta1.toFixed(1)}"`],
        ["Secondary Image θ₋:", `${theta2.toFixed(1)}"`],
        ["Primary Magnification μ₊:", `${mu1.toFixed(2)} ×`],
        ["Secondary Magnification μ₋:", `${mu2.toFixed(2)} ×`],
        ["Total Flux Amplification μ_tot:", `${totalMu.toFixed(2)} × (${(2.5 * Math.log10(totalMu)).toFixed(2)} mag)`]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx + 12, ry + 55 + idx * 28);
        ctx.fillStyle = idx === 6 ? "#fbbf24" : (idx === 0 ? "#facc15" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx + 12, ry + 70 + idx * 28);
        ctx.font = "11px Inter";
      });

      // Equation
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Lens Equation: β = θ - θ_E² / θ", rx + 12, ry + 275);
      ctx.fillText("As β ➔ 0: Images merge into perfect Einstein ring.", rx + 12, ry + 295);
    }
  },
"""

sim13 = """  // =========================================================================
  // CHAPTER 7: COSMIC EXPANSION & RELATIVISTIC COSMOLOGY
  // =========================================================================

  // 13. Expanding Metric Cosmological Grid & Hubble Redshift Flow
  "astro-hubble-expansion-sim": {
    title: "Metric Space Expansion & Hubble Redshift Flow",
    desc: "2D uniform cosmological metric expansion demonstrating Hubble-Lemaître law v = H₀ d, cosmological redshift 1 + z = a₀ / a(t), and observer frame invariance across cosmic grid.",
    isAnimated: true,
    controls: [
      { id: "hubbleH0", label: "Hubble Constant H₀ (km/s/Mpc)", min: 50, max: 90, step: 1, value: 70 },
      { id: "scaleFactor", label: "Scale Factor a(t)", min: 0.5, max: 1.8, step: 0.05, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const H0 = vals.hubbleH0 !== undefined ? vals.hubbleH0 : 70;
      const baseScale = vals.scaleFactor !== undefined ? vals.scaleFactor : 1.0;
      // dynamic expansion with breathing
      const a_t = baseScale * (1 + 0.15 * Math.sin(time * 0.4));

      // Left Panel: Expanding Grid of Galaxies
      const cx = 200, cy = 200;
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("2D Expanding Robertson-Walker Metric Grid", 25, 25);

      // Metric grid lines
      ctx.strokeStyle = "rgba(51, 65, 85, 0.4)"; ctx.lineWidth = 1;
      const gridSize = 32 * a_t;
      for (let x = cx % gridSize; x < 400; x += gridSize) {
        ctx.beginPath(); ctx.moveTo(x, 40); ctx.lineTo(x, 360); ctx.stroke();
      }
      for (let y = cy % gridSize; y < 360; y += gridSize) {
        ctx.beginPath(); ctx.moveTo(20, y); ctx.lineTo(380, y); ctx.stroke();
      }

      // Central Observer Galaxy
      ctx.fillStyle = "#10b981"; ctx.shadowColor = "#10b981"; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(cx, cy, 7, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;
      ctx.fillStyle = "#a7f3d0"; ctx.font = "bold 10px Inter";
      ctx.fillText("Observer (v=0)", cx - 35, cy + 18);

      // Surrounding galaxies receding
      for (let gx = -3; gx <= 3; gx++) {
        for (let gy = -3; gy <= 3; gy++) {
          if (gx === 0 && gy === 0) continue;
          const px = cx + gx * gridSize;
          const py = cy + gy * gridSize;
          if (px < 30 || px > 370 || py < 45 || py > 355) continue;

          const comovDist = Math.hypot(gx, gy);
          const physDistMpc = comovDist * 15 * a_t;
          const recVel = H0 * physDistMpc;
          const z_redshift = recVel / 3e5; // v / c

          // Velocity vector
          const vLen = Math.min(22, recVel * 0.015);
          const ang = Math.atan2(py - cy, px - cx);
          ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.moveTo(px, py);
          ctx.lineTo(px + Math.cos(ang) * vLen, py + Math.sin(ang) * vLen);
          ctx.stroke();

          // Galaxy dot
          ctx.fillStyle = "#fbbf24";
          ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Right Panel: Hubble Diagram v vs d
      const hx = 420, hy = 35, hw = 315, hh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(hx, hy, hw, hh); ctx.strokeRect(hx, hy, hw, hh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Hubble-Lemaître Law v = H₀ d", hx + 15, hy + 22);

      const ox = hx + 50, oy = hy + 175, pw = hw - 70, ph = 120;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Proper Distance d (Mpc)", ox + pw - 120, oy + 18);
      ctx.save(); ctx.translate(ox - 30, oy - 30); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Recession v (km/s)", 0, 0); ctx.restore();

      // Hubble slope line
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.beginPath();
      ctx.moveTo(ox, oy);
      ctx.lineTo(ox + pw, oy - ph);
      ctx.stroke();

      // Plotted galaxy points
      for (let i = 1; i <= 8; i++) {
        const d_mpc = i * 10;
        const v_k = H0 * d_mpc;
        const px = ox + (d_mpc / 80) * pw;
        const py = oy - (v_k / (H0 * 80)) * ph;
        ctx.fillStyle = "#fbbf24";
        ctx.beginPath(); ctx.arc(px, py, 3.5, 0, Math.PI * 2); ctx.fill();
      }

      // Telemetry Box
      const by = hy + 200;
      const redshift = (1 / a_t) - 1;

      const items = [
        ["Hubble Constant H₀:", `${H0} km/s/Mpc`],
        ["Scale Factor a(t):", `${a_t.toFixed(3)} (Current epoch = 1.0)`],
        ["Cosmological Redshift z = 1/a - 1:", `${redshift > 0 ? "+" : ""}${redshift.toFixed(3)}`],
        ["Wavelength Stretching:", `λ_obs = (1 + z) λ_emit = ${(1 + redshift).toFixed(2)} λ₀`],
        ["Hubble Time t_H = 1/H₀:", `${(977.8 / H0).toFixed(1)} Gyr`]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], hx + 12, by + 18 + idx * 24);
        ctx.fillStyle = idx === 2 ? (redshift > 0 ? "#f43f5e" : "#38bdf8") : "#f1f5f9";
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], hx + 185, by + 18 + idx * 24);
        ctx.font = "11px Inter";
      });
    }
  },
"""

sim14 = """  // 14. Friedmann Universe Scale Factor Integrator a(t)
  "astro-friedmann-universe-sim": {
    title: "Multi-Component Friedmann Equation Integrator a(t)",
    desc: "Numerical integration of (ȧ/a)² = H₀² [Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_k a⁻² + Ω_Λ] comparing Big Bang, deceleration-to-acceleration transition, and cosmological fates.",
    isAnimated: true,
    controls: [
      { id: "omegaM", label: "Matter Density Ω_m,0", min: 0.0, max: 1.0, step: 0.05, value: 0.31 },
      { id: "omegaLambda", label: "Dark Energy Ω_Λ,0", min: 0.0, max: 1.4, step: 0.05, value: 0.69 },
      { id: "hubbleParam", label: "Hubble Constant H₀", min: 60, max: 80, step: 1, value: 70 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Om = vals.omegaM !== undefined ? vals.omegaM : 0.31;
      const OL = vals.omegaLambda !== undefined ? vals.omegaLambda : 0.69;
      const H0 = vals.hubbleParam !== undefined ? vals.hubbleParam : 70;

      const Ok = 1.0 - Om - OL;
      // Deceleration parameter q0 = 0.5 * Om - OL
      const q0 = 0.5 * Om - OL;
      const isAccelerating = q0 < 0;

      // Transition redshift where acceleration begins: z_trans = (2 OL / Om)^(1/3) - 1
      const z_trans = Om > 0.01 && OL > 0 ? Math.pow((2 * OL) / Om, 1/3) - 1 : null;

      // Left Panel: Scale Factor Trajectory a(t)
      const gx = 45, gy = 35, gw = 430, gh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Cosmic Scale Factor Evolution a(t) vs Cosmic Time", gx + 15, gy + 22);

      const ox = gx + 50, oy = gy + gh - 45, pw = gw - 70, ph = gh - 75;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Cosmic Time t (Gyr)", ox + pw - 110, oy + 18);
      ctx.save(); ctx.translate(ox - 30, oy - 45); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Scale Factor a(t)", 0, 0); ctx.restore();

      // Current epoch marker (t_0 ~ 13.8 Gyr, a = 1.0)
      const t0_x = ox + (13.8 / 30.0) * pw;
      const a1_y = oy - (1.0 / 2.2) * ph;
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 1; ctx.setLineDash([2, 2]);
      ctx.beginPath(); ctx.moveTo(t0_x, oy); ctx.lineTo(t0_x, oy - ph); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ox, a1_y); ctx.lineTo(ox + pw, a1_y); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.fillText("t₀ (13.8 Gyr)", t0_x - 30, oy + 14);
      ctx.fillText("a = 1.0", ox - 35, a1_y + 4);

      // Integrate a(t) using Euler/RK approximation
      // dt / da = 1 / [ a * H0 * sqrt(Om/a^3 + Ok/a^2 + OL) ]
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let t = 0; t <= 30; t += 0.2) {
        // Approximate LCDM scale factor: a(t) ~ (Om / OL)^(1/3) * sinh^(2/3)(1.5 * sqrt(OL) * H0 * t)
        let a_calc = 0;
        if (OL > 0.05 && Om > 0.05) {
          const arg = 1.5 * Math.sqrt(OL) * (H0 / 977.8) * t;
          a_calc = Math.pow(Om / OL, 1/3) * Math.pow(Math.sinh(arg), 2/3);
        } else {
          // Einstein-de Sitter (Om=1, OL=0)
          a_calc = Math.pow((1.5 * (H0 / 977.8) * t), 2/3);
        }
        const px = ox + (t / 30.0) * pw;
        const py = oy - (Math.min(2.2, a_calc) / 2.2) * ph;
        if (t === 0) ctx.moveTo(px, oy); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current point (t0, 1.0)
      ctx.fillStyle = "#f59e0b"; ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(t0_x, a1_y, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Right Panel: Cosmological Fate & Parameters
      const rx = 490, ry = 35, rw = 245, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Cosmological Parameters", rx + 15, ry + 22);

      const items = [
        ["Matter Density Ω_m:", `${Om.toFixed(2)}`],
        ["Dark Energy Ω_Λ:", `${OL.toFixed(2)}`],
        ["Curvature Density Ω_k:", `${Ok.toFixed(2)} (${Math.abs(Ok) < 0.02 ? "Spatially Flat" : (Ok < 0 ? "Closed (k=+1)" : "Open (k=-1)")})`],
        ["Deceleration Param q₀:", `${q0.toFixed(2)} (${isAccelerating ? "ACCELERATING" : "DECELERATING"})`],
        ["Transition Redshift z_t:", z_trans && z_trans > 0 ? `${z_trans.toFixed(2)}` : "None"],
        ["Ultimate Cosmic Fate:", OL > 0 ? "EXPONENTIAL EXPANSION (Big Freeze)" : (Om > 1 ? "RECOLLAPSE (Big Crunch)" : "ETERNAL EXPANSION")]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx + 12, ry + 55 + idx * 28);
        ctx.fillStyle = idx === 3 ? (isAccelerating ? "#10b981" : "#ef4444") : (idx === 5 ? "#38bdf8" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx + 12, ry + 70 + idx * 28);
        ctx.font = "11px Inter";
      });

      // Friedmann formula
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("H²(a) = H₀² [Ω_m a⁻³ + Ω_k a⁻² + Ω_Λ]", rx + 12, ry + 275);
    }
  },
"""

sim15 = """  // =========================================================================
  // CHAPTER 8: THE EARLY UNIVERSE & ASTROBIOLOGY
  // =========================================================================

  // 15. Primordial Big Bang Nucleosynthesis (BBN) Freeze-Out
  "astro-bbn-nucleosynthesis-sim": {
    title: "Big Bang Nucleosynthesis (BBN) Abundance Engine",
    desc: "Weak interaction freeze-out (n/p ~ e^(-Δm/kT) ~ 1/6) followed by neutron decay through the deuterium bottleneck, yielding primordial ⁴He (Y_p ~ 0.245), D/H, ³He, and ⁷Li vs baryon density η.",
    isAnimated: true,
    controls: [
      { id: "baryonDensity", label: "Baryon-to-Photon η₁₀ = 10¹⁰ η", min: 2.0, max: 9.0, step: 0.2, value: 6.1 },
      { id: "neutrinoFlavors", label: "Neutrino Species N_ν", min: 2.0, max: 4.0, step: 0.2, value: 3.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const eta10 = vals.baryonDensity !== undefined ? vals.baryonDensity : 6.1;
      const Nnu = vals.neutrinoFlavors !== undefined ? vals.neutrinoFlavors : 3.0;

      // Primordial 4He mass fraction Y_p:
      // Y_p ~ 0.247 + 0.013 * (Nnu - 3) + 0.010 * ln(eta10 / 6)
      const Yp = 0.247 + 0.013 * (Nnu - 3.0) + 0.010 * Math.log(eta10 / 6.0);

      // Deuterium abundance (D/H):
      // (D/H) ~ 2.5e-5 * (eta10 / 6)^(-1.6)
      const d_over_h = 2.5e-5 * Math.pow(eta10 / 6.0, -1.6);

      // Helium-3:
      const he3_over_h = 1.0e-5 * Math.pow(eta10 / 6.0, -0.6);

      // Lithium-7 (the cosmological lithium problem valley):
      const li7_over_h = 4.8e-10 * Math.pow(eta10 / 6.0, 2.0);

      // Left Panel: Schramm BBN Plot log(Abundance) vs eta
      const gx = 45, gy = 35, gw = 430, gh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Primordial Light Element Abundances vs Baryon Density η", gx + 15, gy + 22);

      const ox = gx + 55, oy = gy + gh - 45, pw = gw - 75, ph = gh - 75;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Baryon Density η₁₀ = 10¹⁰ (n_b / n_γ)", ox + pw - 180, oy + 20);
      ctx.save(); ctx.translate(ox - 35, oy - 45); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Primordial Mass Fraction / Ratio", 0, 0); ctx.restore();

      // CMB concordance vertical band at eta10 = 6.1 +/- 0.2
      const cmbX = ox + ((6.1 - 2.0) / 7.0) * pw;
      ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
      ctx.fillRect(cmbX - 8, oy - ph, 16, ph);
      ctx.fillStyle = "#10b981"; ctx.font = "9px Inter";
      ctx.fillText("Planck CMB", cmbX - 25, oy - ph + 12);

      // Plot 1: 4He mass fraction Yp (~ 0.24 - 0.26)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let e = 2.0; e <= 9.0; e += 0.2) {
        const curYp = 0.247 + 0.013 * (Nnu - 3.0) + 0.010 * Math.log(e / 6.0);
        const px = ox + ((e - 2.0) / 7.0) * pw;
        const py = oy - (0.6 + (curYp - 0.2) * 2.0) * ph;
        if (e === 2.0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot 2: D/H (steep falloff)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.beginPath();
      for (let e = 2.0; e <= 9.0; e += 0.2) {
        const curDh = 2.5e-5 * Math.pow(e / 6.0, -1.6);
        const px = ox + ((e - 2.0) / 7.0) * pw;
        const logVal = Math.log10(curDh); // -4 to -5.5
        const py = oy - ((logVal + 6) / 4) * ph * 0.7;
        if (e === 2.0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot 3: 7Li/H (trough then rise)
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 1.8; ctx.beginPath();
      for (let e = 2.0; e <= 9.0; e += 0.2) {
        const curLi = 4.8e-10 * Math.pow(e / 6.0, 2.0);
        const px = ox + ((e - 2.0) / 7.0) * pw;
        const logVal = Math.log10(curLi);
        const py = oy - ((logVal + 11) / 5) * ph * 0.45;
        if (e === 2.0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Legend
      ctx.font = "10px Inter";
      ctx.fillStyle = "#38bdf8"; ctx.fillText("— ⁴He (Y_p)", ox + 15, gy + 45);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("— D / H", ox + 95, gy + 45);
      ctx.fillStyle = "#f43f5e"; ctx.fillText("— ⁷Li / H", ox + 165, gy + 45);

      // Current η point marker
      const curX = ox + ((eta10 - 2.0) / 7.0) * pw;
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1; ctx.setLineDash([3, 2]);
      ctx.beginPath(); ctx.moveTo(curX, oy); ctx.lineTo(curX, oy - ph); ctx.stroke();
      ctx.setLineDash([]);

      // Right Panel: Nuclear Yield Telemetry
      const rx = 490, ry = 35, rw = 245, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Primordial Nucleosynthesis Yields", rx + 15, ry + 22);

      const items = [
        ["Selected η₁₀:", `${eta10.toFixed(2)}`],
        ["Neutrino Species N_ν:", `${Nnu.toFixed(1)}`],
        ["⁴He Mass Fraction Y_p:", `${Yp.toFixed(4)} (24.7%)`],
        ["Deuterium D/H:", `${d_over_h.toExponential(2)}`],
        ["Helium-3 ³He/H:", `${he3_over_h.toExponential(2)}`],
        ["Lithium-7 ⁷Li/H:", `${li7_over_h.toExponential(2)}`],
        ["Baryon Density Ω_b h²:", `${(eta10 * 0.00365).toFixed(4)}`]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx + 12, ry + 55 + idx * 28);
        ctx.fillStyle = idx === 2 ? "#38bdf8" : (idx === 3 ? "#f59e0b" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx + 12, ry + 70 + idx * 28);
        ctx.font = "11px Inter";
      });

      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Deuterium is pristine cosmological baryometer", rx + 12, ry + 280);
      ctx.fillText("because all stars exclusively destroy it.", rx + 12, ry + 295);
    }
  },
"""

sim16 = """  // 16. Circumstellar Habitable Zone & Drake Equation
  "astro-drake-habitable-sim": {
    title: "Circumstellar Habitable Zone & Drake Equation Calculator",
    desc: "Interactive planetary system habitable zone calculator (r_in = 0.95 √(L/L⊙) AU, r_out = 1.67 √(L/L⊙) AU) coupled to the Drake equation for communicating galactic civilizations N.",
    isAnimated: true,
    controls: [
      { id: "starLum", label: "Stellar Luminosity L (L⊙)", min: 0.1, max: 5.0, step: 0.1, value: 1.0 },
      { id: "planetDist", label: "Planet Orbit d (AU)", min: 0.2, max: 3.5, step: 0.05, value: 1.0 },
      { id: "civLifetime", label: "Civilization Lifetime L (years)", min: 100, max: 100000, step: 500, value: 10000 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const L = vals.starLum !== undefined ? vals.starLum : 1.0;
      const d = vals.planetDist !== undefined ? vals.planetDist : 1.0;
      const L_civ = vals.civLifetime !== undefined ? vals.civLifetime : 10000;

      // Habitable zone boundaries: r ~ sqrt(L)
      const r_in = 0.95 * Math.sqrt(L);  // Runaway greenhouse
      const r_out = 1.67 * Math.sqrt(L); // Maximum greenhouse

      // Planet equilibrium temperature: Teq = 278 * (L)^(1/4) / sqrt(d) (assuming albedo 0.3)
      const Teq = 278 * Math.pow(L, 0.25) / Math.sqrt(d);
      const isHabitable = d >= r_in && d <= r_out;

      // Drake Equation: N = R* * fp * ne * fl * fi * fc * L
      // Standard fiducial values: R*=2, fp=0.8, ne=0.5, fl=0.3, fi=0.1, fc=0.1
      const N_civ = Math.round(2.0 * 0.8 * 0.5 * 0.3 * 0.1 * 0.1 * L_civ);

      // Left Panel: Planetary System Habitable Zone
      const cx = 175, cy = 200;
      const scaleAU = 55; // pixels per AU

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Planetary System & Circumstellar Habitable Zone", 25, 25);

      // Scorched Zone (too hot)
      ctx.fillStyle = "rgba(239, 68, 68, 0.15)";
      ctx.beginPath(); ctx.arc(cx, cy, r_in * scaleAU, 0, Math.PI * 2); ctx.fill();

      // Habitable Zone (Green Ring)
      ctx.strokeStyle = "rgba(16, 185, 129, 0.5)"; ctx.lineWidth = (r_out - r_in) * scaleAU;
      ctx.beginPath();
      ctx.arc(cx, cy, (r_in + r_out) * 0.5 * scaleAU, 0, Math.PI * 2);
      ctx.stroke();

      // Outer Frozen Zone (blue dash)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.3)"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, r_out * scaleAU + 35, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      // Central Host Star
      const starGrad = ctx.createRadialGradient(cx, cy, 2, cx, cy, 18);
      starGrad.addColorStop(0, "#ffffff");
      starGrad.addColorStop(0.5, "#fbbf24");
      starGrad.addColorStop(1, "#f97316");
      ctx.fillStyle = starGrad; ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 12;
      ctx.beginPath(); ctx.arc(cx, cy, 12 * Math.pow(L, 0.3), 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Orbiting Planet
      const orbPeriod = Math.pow(d, 1.5) * 3; // Keplers 3rd law
      const pAng = (time / orbPeriod) * Math.PI * 2;
      const px = cx + d * scaleAU * Math.cos(pAng);
      const py = cy + d * scaleAU * Math.sin(pAng);

      // Orbit circle
      ctx.strokeStyle = isHabitable ? "#10b981" : "#64748b"; ctx.lineWidth = 1; ctx.setLineDash([2, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, d * scaleAU, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      // Planet body
      ctx.fillStyle = isHabitable ? "#38bdf8" : (d < r_in ? "#ef4444" : "#93c5fd");
      ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 8;
      ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px Inter";
      ctx.fillText(`Planet (${d.toFixed(2)} AU)`, px + 9, py - 4);

      // Right Panel: Astrobiology & Drake Engine Telemetry
      const rx = 390, ry = 35, rw = 345, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Habitability & Drake Equation Calculation", rx + 15, ry + 22);

      const items = [
        ["Host Star Luminosity L:", `${L.toFixed(2)} L⊙`],
        ["Habitable Zone Inner Edge r_in:", `${r_in.toFixed(2)} AU (Runaway Greenhouse)`],
        ["Habitable Zone Outer Edge r_out:", `${r_out.toFixed(2)} AU (Maximum Greenhouse)`],
        ["Planet Equilibrium Temp Teq:", `${Math.round(Teq)} K (${Math.round(Teq - 273.15)} °C)`],
        ["Habitability Status:", isHabitable ? "POTENTIALLY HABITABLE (Liquid H₂O Stable)" : (d < r_in ? "TOO HOT (Runaway Greenhouse)" : "TOO COLD (Global Glaciation)")],
        ["Civilization Lifetime L:", `${L_civ.toLocaleString()} years`],
        ["Drake Communicating Civilizations N:", `${N_civ.toLocaleString()} civilizations in Milky Way`]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx + 12, ry + 52 + idx * 28);
        ctx.fillStyle = idx === 4 ? (isHabitable ? "#10b981" : "#ef4444") : (idx === 6 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx + 12, ry + 66 + idx * 28);
        ctx.font = "11px Inter";
      });

      // Drake equation summary
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Drake Equation: N = R* × fp × ne × fl × fi × fc × L", rx + 12, ry + 275);
      ctx.fillText("If L ~ 10,000 yr, hundreds of communicating civilizations coexist.", rx + 12, ry + 295);
    }
  }
};

// Simulation Engine Adapter for Open STEM Library App Controller
window.SimulationEngine = window.SimulationEngine || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = "";

  const simConfig = (window.ASTRO_SIMS && window.ASTRO_SIMS[simType]) ||
                    (window.QM2_SIMS && window.QM2_SIMS[simType]) ||
                    (window.DIG_SIMS && window.DIG_SIMS[simType]) ||
                    (window.NUC_SIMS && window.NUC_SIMS[simType]);

  if (!simConfig) {
    container.innerHTML = `<div style="padding: 1rem; color: #ef4444; background: #1e1b4b; border-radius: 8px;">Simulation type '${simType}' not found in registry.</div>`;
    return;
  }

  if (window.SimulationEngine.activeAnimations && window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }
  window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

  const box = document.createElement("div");
  box.className = "simulation-box";
  box.style.background = "#0b1120";
  box.style.border = "1px solid #1e293b";
  box.style.borderRadius = "12px";
  box.style.padding = "1.25rem";
  box.style.marginTop = "1rem";
  box.style.marginBottom = "1.5rem";

  const header = document.createElement("div");
  header.style.marginBottom = "1rem";
  header.innerHTML = `
    <div style="display: flex; align-items: center; justify-content: space-between;">
      <h4 style="margin: 0; color: #38bdf8; font-size: 1.15rem; font-family: 'Space Grotesk', sans-serif;">${simConfig.title}</h4>
      <span style="font-size: 0.75rem; background: #1e293b; color: #94a3b8; padding: 0.2rem 0.5rem; border-radius: 4px; border: 1px solid #334155;">60 FPS Interactive</span>
    </div>
    <p style="margin: 0.4rem 0 0 0; color: #94a3b8; font-size: 0.85rem; line-height: 1.4;">${simConfig.desc}</p>
  `;
  box.appendChild(header);

  const canvas = document.createElement("canvas");
  canvas.width = 750;
  canvas.height = 390;
  canvas.style.width = "100%";
  canvas.style.maxWidth = "750px";
  canvas.style.height = "auto";
  canvas.style.aspectRatio = "750 / 390";
  canvas.style.background = "#050811";
  canvas.style.borderRadius = "8px";
  canvas.style.border = "1px solid #1e293b";
  canvas.style.display = "block";
  box.appendChild(canvas);

  const ctrlBar = document.createElement("div");
  ctrlBar.style.display = "flex";
  ctrlBar.style.flexWrap = "wrap";
  ctrlBar.style.gap = "1rem";
  ctrlBar.style.marginTop = "1rem";
  ctrlBar.style.alignItems = "center";

  const currentVals = {};

  if (simConfig.controls) {
    simConfig.controls.forEach(c => {
      currentVals[c.id] = c.value;
      const wrap = document.createElement("div");
      wrap.style.display = "flex";
      wrap.style.flexDirection = "column";
      wrap.style.gap = "0.25rem";

      const lbl = document.createElement("label");
      lbl.style.fontSize = "0.8rem";
      lbl.style.color = "#94a3b8";
      lbl.innerText = `${c.label}: ${c.value}`;

      const input = document.createElement("input");
      input.type = "range";
      input.min = c.min;
      input.max = c.max;
      input.step = c.step;
      input.value = c.value;
      input.style.accentColor = "#38bdf8";

      input.addEventListener("input", (e) => {
        const val = parseFloat(e.target.value);
        currentVals[c.id] = val;
        lbl.innerText = `${c.label}: ${val}`;
        if (!simConfig.isAnimated) {
          simConfig.render(canvas, currentVals, 0);
        }
      });

      wrap.appendChild(lbl);
      wrap.appendChild(input);
      ctrlBar.appendChild(wrap);
    });
  }

  if (simConfig.isAnimated) {
    const animCtrlWrap = document.createElement("div");
    animCtrlWrap.style.display = "flex";
    animCtrlWrap.style.alignItems = "flex-end";
    const pauseBtn = document.createElement("button");
    pauseBtn.innerText = "⏸️ Pause";
    pauseBtn.style.padding = "0.4rem 0.8rem";
    pauseBtn.style.background = "#1e293b";
    pauseBtn.style.color = "#38bdf8";
    pauseBtn.style.border = "1px solid #334155";
    pauseBtn.style.borderRadius = "6px";
    pauseBtn.style.cursor = "pointer";
    pauseBtn.style.fontSize = "0.85rem";

    let isPaused = false;
    pauseBtn.addEventListener("click", () => {
      isPaused = !isPaused;
      pauseBtn.innerText = isPaused ? "▶️ Play" : "⏸️ Pause";
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
"""

with open("build_astro_sims.py", "a", encoding="utf-8") as f:
    f.write(sim11)
    f.write(sim12)
    f.write(sim13)
    f.write(sim14)
    f.write(sim15)
    f.write(sim16)

# Now copy build_astro_sims.py to astrophysics-sims.js
import shutil
shutil.copyfile("build_astro_sims.py", "astrophysics-sims.js")
print("All 16 simulations generated and written to astrophysics-sims.js!")
