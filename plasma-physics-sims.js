// Plasma Physics & Magnetohydrodynamics Interactive Simulation Suite
// 16 Real-Time 60 FPS Canvas Simulations for Single-Particle Dynamics, Fluid Drifts, Waves, MHD & Kinetic Theory

window.PLASMA_SIMS = {
// =========================================================================
  // UNIT 1: INTRODUCTION TO PLASMA, DEBYE SHIELDING & GAS DISCHARGE
  // =========================================================================

  // 1. Debye Shielding, Screening Cloud & Sheath Potential
  "plasma-debye-shielding-sim": {
    title: "Debye Shielding, Screening Cloud & Sheath Potential",
    desc: "Interactive 2D kinetic plasma visualization of electron screening cloud formation around a test charge Q, Debye-Hückel potential decay, and Bohm sheath drop at wall.",
    isAnimated: true,
    controls: [
      { id: "density", label: "Density n₀ (10¹⁸ m⁻³)", min: 1, max: 50, step: 1, value: 10 },
      { id: "temp", label: "Electron Temp T_e (eV)", min: 1, max: 40, step: 1, value: 10 },
      { id: "testCharge", label: "Test Charge Q/e", min: -8, max: 8, step: 1, value: 5 }
    ],
    particles: null,
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const n0 = (vals.density !== undefined ? vals.density : 10) * 1e18;
      const Te = vals.temp !== undefined ? vals.temp : 10; // eV
      const Q = vals.testCharge !== undefined ? vals.testCharge : 5;

      // Debye length calculation: lambda_D = sqrt(eps0 * kB * Te / (n0 * e^2))
      // In normalized sim units:
      const lambdaD_px = Math.max(25, Math.min(110, Math.sqrt(Te / (vals.density || 10)) * 55));
      const lambdaD_um = Math.sqrt(8.854e-12 * Te * 1.602e-19 / (n0 * (1.602e-19)**2)) * 1e6;
      const ND = (4/3) * Math.PI * n0 * ((lambdaD_um * 1e-6)**3);
      const wpe_Ghz = (Math.sqrt(n0 * (1.602e-19)**2 / (8.854e-12 * 9.109e-31)) / (2 * Math.PI)) / 1e9;
      const cs_kms = Math.sqrt(Te * 1.602e-19 / 1.673e-27) / 1000;

      // Particle simulation area
      const simW = 430, simH = h;
      const cx = simW / 2 + 15, cy = simH / 2;

      // Initialize particles if needed
      if (!this.particles || this.particles.length !== 120) {
        this.particles = [];
        for (let i = 0; i < 120; i++) {
          const isElectron = i < 80;
          const rad = 25 + Math.random() * 160;
          const ang = Math.random() * Math.PI * 2;
          this.particles.push({
            isElectron: isElectron,
            x: cx + Math.cos(ang) * rad,
            y: cy + Math.sin(ang) * rad,
            vx: (Math.random() - 0.5) * (isElectron ? 3.5 : 0.8),
            vy: (Math.random() - 0.5) * (isElectron ? 3.5 : 0.8),
            baseRad: rad,
            ang: ang
          });
        }
      }

      // Draw background grid
      ctx.strokeStyle = "rgba(30, 41, 59, 0.4)";
      ctx.lineWidth = 1;
      for (let x = 20; x < simW; x += 35) {
        ctx.beginPath(); ctx.moveTo(x, 15); ctx.lineTo(x, h - 15); ctx.stroke();
      }
      for (let y = 20; y < h; y += 35) {
        ctx.beginPath(); ctx.moveTo(20, y); ctx.lineTo(simW, y); ctx.stroke();
      }

      // Draw Debye sphere radius circle
      ctx.strokeStyle = "rgba(56, 189, 248, 0.5)";
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.arc(cx, cy, lambdaD_px, 0, Math.PI * 2);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.beginPath();
      ctx.arc(cx, cy, lambdaD_px, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`Debye Sphere r = λ_D (${lambdaD_px.toFixed(0)} px)`, cx - 55, cy - lambdaD_px - 8);

      // Update & Draw particles
      for (let p of this.particles) {
        // Force toward/away from test charge
        const dx = p.x - cx;
        const dy = p.y - cy;
        const dist = Math.sqrt(dx * dx + dy * dy) + 10;
        const qSign = p.isElectron ? -1 : 1;
        const force = (Q * qSign * 180) / (dist * dist + 100);

        p.vx += (dx / dist) * force * 0.15;
        p.vy += (dy / dist) * force * 0.15;

        // Thermal random kick
        const vth = p.isElectron ? Math.sqrt(Te) * 0.25 : 0.08;
        p.vx += (Math.random() - 0.5) * vth;
        p.vy += (Math.random() - 0.5) * vth;

        // Damping / boundary reflection
        p.vx *= 0.96; p.vy *= 0.96;
        p.x += p.vx; p.y += p.vy;

        if (p.x < 30) { p.x = 30; p.vx *= -1; }
        if (p.x > simW - 15) { p.x = simW - 15; p.vx *= -1; }
        if (p.y < 25) { p.y = 25; p.vy *= -1; }
        if (p.y > h - 25) { p.y = h - 25; p.vy *= -1; }

        ctx.fillStyle = p.isElectron ? "#38bdf8" : "#f59e0b";
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.isElectron ? 2.5 : 4, 0, Math.PI * 2);
        ctx.fill();
      }

      // Draw Test Charge at Center
      const qColor = Q > 0 ? "#ef4444" : (Q < 0 ? "#3b82f6" : "#94a3b8");
      ctx.fillStyle = qColor;
      ctx.shadowColor = qColor; ctx.shadowBlur = 15;
      ctx.beginPath();
      ctx.arc(cx, cy, 14, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 11px Inter";
      ctx.textAlign = "center";
      ctx.fillText(Q > 0 ? `+${Q}e` : `${Q}e`, cx, cy + 4);
      ctx.textAlign = "left";

      // Left wall: Sheath representation
      ctx.fillStyle = "#334155";
      ctx.fillRect(15, 15, 8, h - 30);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "9px Inter";
      ctx.save();
      ctx.translate(10, h / 2 + 25);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText("WALL (GROUND / SHEATH)", 0, 0);
      ctx.restore();

      // Right Side: Potential Curve Plot & Telemetry
      const px0 = 460, py0 = 35, pw = 270, ph = 140;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.fillRect(px0, py0, pw, ph); ctx.strokeRect(px0, py0, pw, ph);

      ctx.fillStyle = "#e2e8f0";
      ctx.font = "bold 12px Inter";
      ctx.fillText("Potential Decay: Coulomb vs Debye", px0 + 10, py0 + 18);

      // Plot Axes
      const ax0 = px0 + 35, ay0 = py0 + ph - 25, alx = pw - 45, aly = ph - 45;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(ax0, ay0); ctx.lineTo(ax0 + alx, ay0);
      ctx.moveTo(ax0, ay0); ctx.lineTo(ax0, ay0 - aly);
      ctx.stroke();

      ctx.font = "9px Inter"; ctx.fillStyle = "#94a3b8";
      ctx.fillText("r (distance)", ax0 + alx - 45, ay0 + 14);
      ctx.fillText("φ(r)", ax0 - 25, ay0 - aly + 8);

      // Bare Coulomb (red dashed)
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      for (let rx = 5; rx <= alx; rx += 3) {
        const rNorm = rx / 20;
        const phiC = Math.min(aly - 5, (aly * 0.9) / (rNorm + 0.5));
        const py = ay0 - phiC * (Math.abs(Q) / 5);
        if (rx === 5) ctx.moveTo(ax0 + rx, py); else ctx.lineTo(ax0 + rx, py);
      }
      ctx.stroke();

      // Shielded Debye-Hückel (cyan solid)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.setLineDash([]);
      ctx.beginPath();
      for (let rx = 5; rx <= alx; rx += 3) {
        const rNorm = rx / 20;
        const decay = Math.exp(-rx / (lambdaD_px * 0.45));
        const phiD = Math.min(aly - 5, ((aly * 0.9) / (rNorm + 0.5)) * decay);
        const py = ay0 - phiD * (Math.abs(Q) / 5);
        if (rx === 5) ctx.moveTo(ax0 + rx, py); else ctx.lineTo(ax0 + rx, py);
      }
      ctx.stroke();

      // Plot legend
      ctx.fillStyle = "#ef4444"; ctx.fillRect(px0 + 140, py0 + 8, 12, 3);
      ctx.fillStyle = "#94a3b8"; ctx.font = "9px Inter"; ctx.fillText("Coulomb 1/r", px0 + 156, py0 + 12);
      ctx.fillStyle = "#38bdf8"; ctx.fillRect(px0 + 140, py0 + 20, 12, 3);
      ctx.fillStyle = "#94a3b8"; ctx.fillText("Debye (1/r)e⁻ʳ/λ", px0 + 156, py0 + 24);

      // Telemetry Box
      const tx = 460, ty = 190, tw = 270, th = 185;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Plasma Parameters Telemetry", tx + 12, ty + 22);

      const items = [
        ["Debye Length λ_D:", `${lambdaD_um.toFixed(2)} μm (${lambdaD_px.toFixed(0)} px)`],
        ["Plasma Parameter N_D:", `${ND > 1e4 ? ND.toExponential(2) : ND.toFixed(0)} (>> 1)`],
        ["Electron Plasma Freq f_pe:", `${wpe_Ghz.toFixed(2)} GHz`],
        ["Ion Bohm Speed c_s:", `${cs_kms.toFixed(1)} km/s`],
        ["Screening Efficiency:", `${(Math.abs(Q) > 0 ? (100 * (1 - Math.exp(-1))).toFixed(1) : "0.0")}% at r = λ_D`],
        ["Collective Regime:", ND > 1 ? "PLASMA CRITERION SATISFIED" : "COLLISION-DOMINATED GAS"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 46 + idx * 23;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 5 ? (ND > 1 ? "#10b981" : "#ef4444") : (idx === 0 ? "#38bdf8" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 155, iy);
      });
    }
  },

  // 2. DC Gas Discharge, Paschen Curve & Townsend Avalanche
  "plasma-dc-discharge-paschen-sim": {
    title: "DC Gas Discharge, Paschen Breakdown & Townsend Avalanche",
    desc: "Interactive Paschen curve V_B(p·d), secondary cathode emission, Townsend avalanche multiplication, and DC glow discharge visual anatomy.",
    isAnimated: true,
    controls: [
      { id: "pd", label: "Pressure·Gap p·d (Torr·cm)", min: 0.1, max: 10.0, step: 0.1, value: 1.0 },
      { id: "appliedV", label: "Applied Voltage V (V)", min: 100, max: 1200, step: 20, value: 450 },
      { id: "gamma", label: "Secondary Emission γ", min: 0.005, max: 0.1, step: 0.005, value: 0.02 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const pd = vals.pd !== undefined ? vals.pd : 1.0;
      const V = vals.appliedV !== undefined ? vals.appliedV : 450;
      const gamma = vals.gamma !== undefined ? vals.gamma : 0.02;

      // Air constants for Paschen: A = 15 cm-1 Torr-1, B = 365 V/(cm Torr)
      const A = 15.0, B = 365.0;
      const C = Math.log(1 + 1 / gamma);
      const pd_min = (Math.E * C) / A;
      const VB_min = B * pd_min;

      // Calculate VB at current pd
      const denom = Math.log(A * pd / C);
      let VB = 9999;
      if (denom > 0.01) {
        VB = (B * pd) / denom;
      }
      const isBreakdown = V >= VB;

      // Townsend ionization coeff alpha = A * p * exp(-B * p / E) = A * p * exp(-B * pd / V)
      const alpha_over_p = A * Math.exp(-B * pd / Math.max(1, V));
      const breakdownThreshold = gamma * (Math.exp(alpha_over_p * pd) - 1);

      // Top area: Paschen Curve Plot (x: 20 to 380, y: 25 to 195)
      const gx = 25, gy = 25, gw = 350, gh = 170;
      ctx.fillStyle = "rgba(15, 23, 42, 0.75)";
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Paschen Breakdown Curve V_B(p·d)", gx + 12, gy + 18);

      // Log-linear plot axes
      const ox = gx + 45, oy = gy + gh - 25, pw = gw - 55, ph = gh - 50;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + pw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - ph);
      ctx.stroke();

      ctx.font = "9px Inter"; ctx.fillStyle = "#94a3b8";
      ctx.fillText("p·d (Torr·cm)", ox + pw - 50, oy + 16);
      ctx.fillText("V_B (V)", ox - 35, oy - ph + 10);

      // Draw Paschen curve
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2;
      ctx.beginPath();
      let started = false;
      for (let s = 0; s <= pw; s += 2) {
        const cur_pd = 0.1 + (s / pw) * 9.9;
        const d_val = Math.log(A * cur_pd / C);
        if (d_val > 0.02) {
          const v_val = (B * cur_pd) / d_val;
          const y_coord = oy - Math.min(ph, (v_val / 1200) * ph);
          if (!started) { ctx.moveTo(ox + s, y_coord); started = true; }
          else { ctx.lineTo(ox + s, y_coord); }
        }
      }
      ctx.stroke();

      // Current operating point on plot
      const cur_px = ox + ((pd - 0.1) / 9.9) * pw;
      const cur_py = oy - Math.min(ph, (V / 1200) * ph);
      ctx.fillStyle = isBreakdown ? "#10b981" : "#fbbf24";
      ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(cur_px, cur_py, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Minimum marker
      const min_px = ox + ((pd_min - 0.1) / 9.9) * pw;
      const min_py = oy - Math.min(ph, (VB_min / 1200) * ph);
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(min_px, min_py, 3, 0, Math.PI * 2); ctx.fill();
      ctx.font = "8px Inter";
      ctx.fillText(`Min: ${VB_min.toFixed(0)}V`, min_px - 15, min_py - 6);

      // Bottom Area: DC Glow Discharge Tube Visualization (x: 25 to 375, y: 215 to 375)
      const tx = 25, ty = 215, tw = 350, th = 155;
      ctx.fillStyle = "#030712";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      // Tube glass boundary
      const tubeY = ty + 30, tubeH = 75;
      ctx.fillStyle = "#020617";
      ctx.fillRect(tx + 20, tubeY, tw - 40, tubeH);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
      ctx.strokeRect(tx + 20, tubeY, tw - 40, tubeH);

      // Cathode (-) and Anode (+)
      ctx.fillStyle = "#94a3b8";
      ctx.fillRect(tx + 20, tubeY, 8, tubeH); // Cathode
      ctx.fillRect(tx + tw - 28, tubeY, 8, tubeH); // Anode
      ctx.fillStyle = "#ef4444"; ctx.font = "bold 10px Inter";
      ctx.fillText("Cathode (-)", tx + 12, tubeY - 8);
      ctx.fillStyle = "#10b981";
      ctx.fillText("Anode (+)", tx + tw - 65, tubeY - 8);

      if (isBreakdown) {
        // Glowing discharge regions
        const cx0 = tx + 28, cW = tw - 56;
        // Negative glow (intense blue)
        const gGrad = ctx.createLinearGradient(cx0, 0, cx0 + cW, 0);
        gGrad.addColorStop(0.00, "rgba(30, 41, 59, 0.2)"); // Crookes dark space
        gGrad.addColorStop(0.12, "rgba(56, 189, 248, 0.85)"); // Negative glow
        gGrad.addColorStop(0.25, "rgba(15, 23, 42, 0.3)"); // Faraday dark space
        gGrad.addColorStop(0.35, "rgba(244, 63, 94, 0.7)"); // Positive column start
        gGrad.addColorStop(0.85, "rgba(244, 63, 94, 0.7)"); // Positive column end
        gGrad.addColorStop(1.00, "rgba(251, 191, 36, 0.6)"); // Anode glow
        ctx.fillStyle = gGrad;
        ctx.fillRect(cx0, tubeY + 2, cW, tubeH - 4);

        // Striations in positive column
        ctx.fillStyle = "rgba(255, 255, 255, 0.25)";
        for (let i = 0; i < 7; i++) {
          const sx = cx0 + cW * 0.4 + i * 22 + Math.sin(time * 3 + i) * 2;
          ctx.fillRect(sx, tubeY + 4, 8, tubeH - 8);
        }

        // Electron particles rushing to anode
        ctx.fillStyle = "#38bdf8";
        for (let i = 0; i < 20; i++) {
          const ex = cx0 + ((time * 120 + i * 16) % cW);
          const ey = tubeY + 15 + (i * 19) % (tubeH - 30);
          ctx.fillRect(ex, ey, 2.5, 2.5);
        }
      } else {
        // Dark Townsend pre-breakdown
        ctx.fillStyle = "rgba(148, 163, 184, 0.1)";
        ctx.fillRect(tx + 28, tubeY + 2, tw - 56, tubeH - 4);
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter";
        ctx.fillText("Dark Townsend Region (No Self-Sustaining Glow)", tx + 45, tubeY + tubeH / 2 + 4);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "9px Inter";
      ctx.fillText("Regions: Cathode Sheath | Neg. Glow | Faraday Space | Positive Column | Anode Glow", tx + 12, ty + th - 12);

      // Right Area: Telemetry & Math Metrics
      const mx = 400, my = 25, mw = 330, mh = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(mx, my, mw, mh); ctx.strokeRect(mx, my, mw, mh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Gas Discharge & Avalanche Telemetry", mx + 14, my + 24);

      const tItems = [
        ["Operating Pressure·Gap p·d:", `${pd.toFixed(2)} Torr·cm`],
        ["Applied Voltage V:", `${V.toFixed(0)} Volts`],
        ["Theoretical Breakdown V_B:", `${VB < 9000 ? VB.toFixed(1) + " V" : "Undefined (pd too low)"}`],
        ["Paschen Minimum (p·d)_min:", `${pd_min.toFixed(3)} Torr·cm`],
        ["Paschen Minimum V_B,min:", `${VB_min.toFixed(1)} Volts`],
        ["Townsend Ionization α/p:", `${alpha_over_p.toFixed(3)} cm⁻¹·Torr⁻¹`],
        ["Secondary Emission γ:", `${gamma.toFixed(4)}`],
        ["Avalanche Criterion γ(e^αd - 1):", `${breakdownThreshold.toFixed(3)} (≥ 1 for self-sustained)`],
        ["Discharge State:", isBreakdown ? "SELF-SUSTAINING GLOW DISCHARGE" : "DARK TOWNSEND (NON-SELF-SUSTAINED)"]
      ];

      tItems.forEach((item, idx) => {
        const iy = my + 54 + idx * 30;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], mx + 14, iy);
        ctx.fillStyle = idx === 8 ? (isBreakdown ? "#10b981" : "#f59e0b") : (idx === 2 ? (isBreakdown ? "#38bdf8" : "#ec4899") : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], mx + 180, iy);
      });
    }
  },

  // =========================================================================
  // UNIT 2: SINGLE-PARTICLE MOTION IN E & B FIELDS
  // =========================================================================

  // 3. Single-Particle Cyclotron Gyration & E x B Drift
  "plasma-cyclotron-exb-sim": {
    title: "Cyclotron Gyration & E x B Guiding Center Drift",
    desc: "Real-time particle integration of ion vs electron cyclotron orbits in magnetic field B and transverse electric field E. Demonstrates mass-independent, charge-independent E x B drift.",
    isAnimated: true,
    controls: [
      { id: "bField", label: "Magnetic Field B_z (Tesla)", min: 0.2, max: 2.5, step: 0.1, value: 1.0 },
      { id: "eField", label: "Electric Field E_y (kV/m)", min: -4.0, max: 4.0, step: 0.5, value: 1.5 },
      { id: "viewMode", label: "Display (0: Both, 1: Ion, 2: Electron)", min: 0, max: 2, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const B = vals.bField !== undefined ? vals.bField : 1.0;
      const Ey_kV = vals.eField !== undefined ? vals.eField : 1.5;
      const mode = vals.viewMode !== undefined ? vals.viewMode : 0;

      // Physics values:
      // v_E = E x B / B^2 -> in x direction: v_Ex = Ey / B
      const vE_kms = (Ey_kV * 1000 / B) / 1000; // km/s
      // Normalized sim velocities & frequencies
      const vE_sim = (Ey_kV / B) * 35;
      const wce_sim = B * 12.0; // electron gyrofrequency (clockwise)
      const wci_sim = B * 2.2;  // ion gyrofrequency (counter-clockwise)
      const rLi_sim = 45 / B;    // ion Larmor radius
      const rLe_sim = 14 / B;    // electron Larmor radius

      // Background Field Symbols (B_z pointing OUT of page: dots)
      ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
      ctx.font = "14px Inter";
      for (let x = 30; x < 440; x += 45) {
        for (let y = 30; y < h; y += 45) {
          ctx.beginPath(); ctx.arc(x, y, 2.5, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Draw E-field vectors (Ey pointing DOWN if Ey > 0)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.35)";
      ctx.lineWidth = 1.5;
      for (let x = 50; x < 440; x += 75) {
        const eDir = Math.sign(Ey_kV);
        const yStart = eDir >= 0 ? 30 : h - 30;
        const yEnd = eDir >= 0 ? 80 : h - 80;
        ctx.beginPath(); ctx.moveTo(x, yStart); ctx.lineTo(x, yEnd); ctx.stroke();
        // Arrowhead
        ctx.beginPath();
        ctx.moveTo(x - 4, yEnd - eDir * 6);
        ctx.lineTo(x, yEnd);
        ctx.lineTo(x + 4, yEnd - eDir * 6);
        ctx.stroke();
      }
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 10px Inter";
      ctx.fillText(Ey_kV >= 0 ? "Electric Field E_y ↓" : "Electric Field E_y ↑", 45, Ey_kV >= 0 ? 25 : h - 15);
      ctx.fillStyle = "#10b981";
      ctx.fillText("Magnetic Field B_z ⊙ (Out of page)", 240, 25);

      // Trajectories computation
      const simW = 440;
      const t = time;
      const baseX = ((t * vE_sim) % (simW - 60)) + 30;
      const cy = h / 2 + 10;

      // 1. Ion (q > 0: counter-clockwise gyration)
      if (mode === 0 || mode === 1) {
        // Draw Ion trail
        ctx.strokeStyle = "rgba(245, 158, 11, 0.75)";
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let dt = 0; dt < 3.5; dt += 0.05) {
          const pastT = t - dt;
          const px = (((pastT * vE_sim) % (simW - 60)) + 30) + rLi_sim * Math.cos(wci_sim * pastT);
          const py = cy + rLi_sim * Math.sin(wci_sim * pastT);
          if (dt === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Ion current position
        const ionX = baseX + rLi_sim * Math.cos(wci_sim * t);
        const ionY = cy + rLi_sim * Math.sin(wci_sim * t);
        ctx.fillStyle = "#f59e0b";
        ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 10;
        ctx.beginPath(); ctx.arc(ionX, ionY, 7, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#050811"; ctx.font = "bold 9px Inter"; ctx.textAlign = "center";
        ctx.fillText("H⁺", ionX, ionY + 3);
        ctx.textAlign = "left";

        // Guiding Center dashed line
        ctx.strokeStyle = "rgba(245, 158, 11, 0.4)";
        ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(ionX, ionY); ctx.lineTo(baseX, cy); ctx.stroke();
        ctx.setLineDash([]);
      }

      // 2. Electron (q < 0: clockwise gyration)
      if (mode === 0 || mode === 2) {
        ctx.strokeStyle = "rgba(56, 189, 248, 0.75)";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        for (let dt = 0; dt < 3.5; dt += 0.02) {
          const pastT = t - dt;
          const px = (((pastT * vE_sim) % (simW - 60)) + 30) + rLe_sim * Math.cos(-wce_sim * pastT);
          const py = cy + rLe_sim * Math.sin(-wce_sim * pastT);
          if (dt === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Electron current position
        const eleX = baseX + rLe_sim * Math.cos(-wce_sim * t);
        const eleY = cy + rLe_sim * Math.sin(-wce_sim * t);
        ctx.fillStyle = "#38bdf8";
        ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 8;
        ctx.beginPath(); ctx.arc(eleX, eleY, 5, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#050811"; ctx.font = "bold 8px Inter"; ctx.textAlign = "center";
        ctx.fillText("e⁻", eleX, eleY + 3);
        ctx.textAlign = "left";
      }

      // Guiding center marker
      ctx.fillStyle = "#a855f7";
      ctx.beginPath(); ctx.arc(baseX, cy, 3.5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#c084fc"; ctx.font = "bold 9px Inter";
      ctx.fillText("R_gc (Guiding Center)", baseX - 50, cy - 8);

      // ExB Drift Velocity Vector arrow
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(baseX, cy); ctx.lineTo(baseX + 45 * Math.sign(Ey_kV), cy); ctx.stroke();
      ctx.beginPath();
      const headX = baseX + 45 * Math.sign(Ey_kV);
      ctx.moveTo(headX - 6 * Math.sign(Ey_kV), cy - 4);
      ctx.lineTo(headX, cy);
      ctx.lineTo(headX - 6 * Math.sign(Ey_kV), cy + 4);
      ctx.stroke();
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 10px Inter";
      ctx.fillText("v_E Drift →", baseX + 10, cy + 18);

      // Right Pane: Telemetry Box
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Guiding Center & Drift Telemetry", tx + 14, ty + 24);

      const items = [
        ["Magnetic Field B_z:", `${B.toFixed(2)} T`],
        ["Electric Field E_y:", `${Ey_kV.toFixed(2)} kV/m`],
        ["E x B Drift Speed v_E:", `${Math.abs(vE_kms).toFixed(2)} km/s`],
        ["Drift Direction:", Ey_kV >= 0 ? "+x (Rightwards)" : "-x (Leftwards)"],
        ["Ion Gyrofrequency f_ci:", `${(B * 15.24).toFixed(1)} MHz`],
        ["Electron Gyrofrequency f_ce:", `${(B * 28.0).toFixed(1)} GHz`],
        ["Ion Larmor Radius r_Li:", `${(3.2 / B).toFixed(2)} mm`],
        ["Electron Larmor Radius r_Le:", `${(0.075 / B).toFixed(3)} mm`],
        ["Net Conduction Current J_E:", "0.0 A/m² (No charge sep!)"],
        ["Physics Invariance:", "q-independent & m-independent"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 2 ? "#ec4899" : (idx === 8 || idx === 9 ? "#10b981" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // 4. Time-Varying E(t) Field & Polarization Drift Current
  "plasma-polarization-drift-sim": {
    title: "Time-Varying E(t) Field & Polarization Drift Current",
    desc: "Inertial polarization drift v_p = (m / qB²) (dE_perp / dt) under AC electric fields. Demonstrates massive ion displacement, electron immobility, and polarization current density j_p.",
    isAnimated: true,
    controls: [
      { id: "dEdt", label: "Rate dE/dt (MV/m·s)", min: 1, max: 10, step: 1, value: 5 },
      { id: "modFreq", label: "Modulation Freq ω_E (kHz)", min: 5, max: 40, step: 5, value: 15 },
      { id: "ionMass", label: "Ion Species (1: H⁺, 2: D⁺, 4: He⁺)", min: 1, max: 4, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const dEdt = vals.dEdt !== undefined ? vals.dEdt : 5;
      const f_kHz = vals.modFreq !== undefined ? vals.modFreq : 15;
      const A_ion = vals.ionMass !== undefined ? vals.ionMass : 1;

      // E(t) = E0 * sin(omega * t)
      const omega = f_kHz * 0.2;
      const Et = Math.sin(omega * time);
      const dEt = Math.cos(omega * time) * omega * (dEdt / 5);

      // Polarization drift is proportional to m / (q B^2) * dE/dt
      const vp_ion_px = dEt * 18 * A_ion;
      const vp_ele_px = -dEt * (18 / 1836); // tiny!

      // Left visualization area: Ion vs Electron displacement
      const vx = 30, vy = 30, vw = 400, vh = 330;
      ctx.fillStyle = "rgba(15, 23, 42, 0.6)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(vx, vy, vw, vh); ctx.strokeRect(vx, vy, vw, vh);

      // Axes for displacement
      ctx.strokeStyle = "#334155"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(vx + 20, vy + vh / 2); ctx.lineTo(vx + vw - 20, vy + vh / 2); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("AC Electric Field E_y(t) & Inertial Lag", vx + 15, vy + 22);

      // Draw E-field indicator bar on left
      const barH = Et * 55;
      ctx.fillStyle = Et >= 0 ? "#38bdf8" : "#ec4899";
      ctx.fillRect(vx + 25, vy + vh / 2, 10, -barH);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("E(t)", vx + 22, vy + vh / 2 + 18);

      // Ion Gyro-Center and Orbit Displacement
      const ionCenterX = vx + 150;
      const ionCenterY = vy + vh / 2 - vp_ion_px;
      const gyroPhase = time * 8;
      const rLi = 32;

      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(ionCenterX, ionCenterY, rLi, 0, Math.PI * 2);
      ctx.stroke();

      const ionX = ionCenterX + rLi * Math.cos(gyroPhase);
      const ionY = ionCenterY + rLi * Math.sin(gyroPhase);
      ctx.fillStyle = "#f59e0b";
      ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 8;
      ctx.beginPath(); ctx.arc(ionX, ionY, 7, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;
      ctx.fillStyle = "#050811"; ctx.font = "bold 8px Inter"; ctx.textAlign = "center";
      ctx.fillText(`+q (A=${A_ion})`, ionX, ionY + 3);
      ctx.textAlign = "left";

      // Polarization drift arrow for Ion
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(ionCenterX, vy + vh / 2);
      ctx.lineTo(ionCenterX, ionCenterY);
      ctx.stroke();
      ctx.fillStyle = "#ef4444"; ctx.font = "bold 10px Inter";
      ctx.fillText(`v_p,ion (${(vp_ion_px).toFixed(1)} px)`, ionCenterX + 12, vy + vh / 2 - vp_ion_px / 2);

      // Electron Gyro-Center (negligible displacement)
      const eleCenterX = vx + 300;
      const eleCenterY = vy + vh / 2 - vp_ele_px;
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.arc(eleCenterX, eleCenterY, 12, 0, Math.PI * 2);
      ctx.stroke();

      const eleX = eleCenterX + 12 * Math.cos(-gyroPhase * 15);
      const eleY = eleCenterY + 12 * Math.sin(-gyroPhase * 15);
      ctx.fillStyle = "#38bdf8";
      ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 6;
      ctx.beginPath(); ctx.arc(eleX, eleY, 4, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Electron (m_e << m_i)", eleCenterX - 35, vy + vh / 2 + 30);
      ctx.fillText("v_p,e ≈ 0 (No inertial lag)", eleCenterX - 45, vy + vh / 2 + 45);

      // Net Polarization Current J_p representation
      const jDir = Math.sign(vp_ion_px);
      ctx.fillStyle = "rgba(16, 185, 129, 0.25)";
      ctx.fillRect(vx + 15, vy + vh - 45, vw - 30, 30);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
      ctx.strokeRect(vx + 15, vy + vh - 45, vw - 30, 30);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Net Current j_p = (ρ_m / B²)·(dE/dt) ${jDir >= 0 ? "↑ Upward" : "↓ Downward"}`, vx + 35, vy + vh - 26);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Polarization Drift & Current", tx + 14, ty + 24);

      const items = [
        ["Rate of Field Change dE/dt:", `${(dEt * 10).toFixed(2)} MV/(m·s)`],
        ["Modulation Freq f_mod:", `${f_kHz} kHz`],
        ["Ion Mass Ratio (m_i / m_e):", `${(A_ion * 1836).toFixed(0)} : 1`],
        ["Ion Polarization Drift v_p,i:", `${Math.abs(dEt * A_ion * 12.4).toFixed(2)} m/s`],
        ["Electron Polarization Drift v_p,e:", `${Math.abs(dEt * 12.4 / 1836).toFixed(4)} m/s`],
        ["Polarization Drift Ratio:", `${(A_ion * 1836).toFixed(0)} (Ions carry 99.95%)`],
        ["Plasma Dielectric Const ε_r:", `1 + c²/v_A² ≈ ${(1.4e3 * A_ion).toFixed(0)}`],
        ["Physical Origin:", "Finite Ion Larmor Inertia Lag"],
        ["Low-Frequency MHD Role:", "Provides Effective Mass Density"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 30;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 3 ? "#ef4444" : (idx === 5 ? "#10b981" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // =========================================================================
  // UNIT 3: DRIFTS IN NON-UNIFORM FIELDS & MAGNETIC MIRRORS
  // =========================================================================

  // 5. Non-Uniform Magnetic Fields: Grad-B & Curvature Drifts
  "plasma-gradient-curvature-drift-sim": {
    title: "Non-Uniform Magnetic Fields: ∇B & Curvature Drifts",
    desc: "Particle trajectories in toroidal/gradient magnetic geometries. Tight Larmor radius at high B and wide at weak B induces grad-B drift, combined with centrifugal curvature drift, driving vertical charge separation.",
    isAnimated: true,
    controls: [
      { id: "gradB", label: "Field Gradient ∇B/B (m⁻¹)", min: 0.5, max: 4.0, step: 0.5, value: 2.0 },
      { id: "curvR", label: "Radius of Curvature R_c (m)", min: 0.8, max: 3.5, step: 0.3, value: 1.5 },
      { id: "chargeSign", label: "Particle (0: Both, 1: Ion, 2: Electron)", min: 0, max: 2, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const gradB = vals.gradB !== undefined ? vals.gradB : 2.0;
      const Rc = vals.curvR !== undefined ? vals.curvR : 1.5;
      const pMode = vals.chargeSign !== undefined ? vals.chargeSign : 0;

      // Left visualization area: curved field lines
      const cx = 40, cy = 195, R0 = 160;
      // Draw curved field lines (concentric circles centered at left)
      ctx.strokeStyle = "rgba(16, 185, 129, 0.4)"; ctx.lineWidth = 1.5;
      for (let r = 80; r <= 320; r += 30) {
        ctx.beginPath();
        ctx.arc(cx - 30, cy, r, -Math.PI / 3, Math.PI / 3);
        ctx.stroke();
      }

      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText("Curved Magnetic Field B Lines (∇B points ← Inward)", 40, 25);

      // Strong field label (inner) vs Weak field (outer)
      ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter";
      ctx.fillText("Strong B (Small r_L)", 60, 50);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("Weak B (Large r_L)", 220, 50);

      // Trajectory of Ion (drifts UPwards)
      if (pMode === 0 || pMode === 1) {
        ctx.strokeStyle = "rgba(245, 158, 11, 0.8)"; ctx.lineWidth = 2;
        ctx.beginPath();
        const driftUp = (time * 25 * gradB) % 240;
        const startY = cy + 100 - driftUp;
        for (let a = 0; a < 6 * Math.PI; a += 0.1) {
          // Radius varies with position: rL ~ rL0 * (1 + 0.15 * cos(a))
          const localR = 30 * (1 + 0.25 * Math.cos(a));
          const px = 180 + localR * Math.cos(a);
          const py = startY - a * (4 * gradB) + localR * Math.sin(a);
          if (a === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Ion head
        ctx.fillStyle = "#f59e0b";
        ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 8;
        ctx.beginPath(); ctx.arc(180, startY - 30, 6, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#f59e0b"; ctx.font = "bold 10px Inter";
        ctx.fillText("Ion H⁺ (Drifts ↑ UP)", 195, startY - 30);
      }

      // Trajectory of Electron (drifts DOWNwards)
      if (pMode === 0 || pMode === 2) {
        ctx.strokeStyle = "rgba(56, 189, 248, 0.8)"; ctx.lineWidth = 1.5;
        ctx.beginPath();
        const driftDown = (time * 25 * gradB) % 240;
        const startYe = cy - 100 + driftDown;
        for (let a = 0; a < 6 * Math.PI; a += 0.1) {
          const localRe = 12 * (1 + 0.2 * Math.cos(a));
          const px = 280 + localRe * Math.cos(-a * 3);
          const py = startYe + a * (2 * gradB) + localRe * Math.sin(-a * 3);
          if (a === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        ctx.fillStyle = "#38bdf8";
        ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 8;
        ctx.beginPath(); ctx.arc(280, startYe + 20, 4.5, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 10px Inter";
        ctx.fillText("Electron e⁻ (Drifts ↓ DOWN)", 295, startYe + 22);
      }

      // Vertical Charge Separation Electric Field E_vert
      ctx.fillStyle = "rgba(236, 72, 153, 0.25)";
      ctx.fillRect(360, 60, 45, 270);
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 1.5;
      ctx.strokeRect(360, 60, 45, 270);
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 9px Inter";
      ctx.fillText("+ Charges (Top)", 340, 52);
      ctx.fillText("- Charges (Bot)", 340, 345);
      ctx.fillText("E_pol ↓", 370, 195);

      // Outward E x B drift arrow
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(380, 195); ctx.lineTo(430, 195); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(422, 191); ctx.lineTo(430, 195); ctx.lineTo(422, 199); ctx.stroke();
      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 9px Inter";
      ctx.fillText("v_E Outward Expulsion →", 325, 215);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("∇B & Curvature Drift Telemetry", tx + 14, ty + 24);

      const vGradB = (gradB * 4.2).toFixed(2);
      const vCurv = ((1.0 / Rc) * 6.5).toFixed(2);
      const vTotal = (parseFloat(vGradB) + parseFloat(vCurv)).toFixed(2);

      const items = [
        ["Field Gradient ∇B/B:", `${gradB.toFixed(1)} m⁻¹`],
        ["Curvature Radius R_c:", `${Rc.toFixed(1)} m`],
        ["Grad-B Drift Speed v_∇B:", `${vGradB} km/s`],
        ["Curvature Drift Speed v_c:", `${vCurv} km/s`],
        ["Total Guiding Drift v_d:", `${vTotal} km/s`],
        ["Ion Drift Direction:", "↑ Upwards (+y)"],
        ["Electron Drift Direction:", "↓ Downwards (-y)"],
        ["Charge Separation Result:", "Generates Vertical E Field"],
        ["Consequence in Simple Torus:", "Radial Expulsion v_E × B"],
        ["Tokamak Resolution:", "Helical Twist q (Safety Factor)"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 4 ? "#ec4899" : (idx === 8 ? "#ef4444" : (idx === 9 ? "#10b981" : "#f1f5f9"));
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 155, iy);
      });
    }
  },

  // 6. Magnetic Mirror, First Adiabatic Invariant & Loss Cone
  "plasma-magnetic-mirror-sim": {
    title: "Magnetic Mirror, First Adiabatic Invariant & Loss Cone",
    desc: "Particle confinement in converging magnetic bottle. Demonstrates conservation of magnetic moment μ = m v_perp² / (2B), pitch angle reflection at turning points, and loss cone escape dynamics.",
    isAnimated: true,
    controls: [
      { id: "mirrorRatio", label: "Mirror Ratio R_m = B_max/B₀", min: 1.5, max: 5.0, step: 0.5, value: 3.0 },
      { id: "pitchAngle", label: "Initial Pitch Angle θ₀ (deg)", min: 15, max: 75, step: 5, value: 45 },
      { id: "bMid", label: "Midplane Field B₀ (T)", min: 0.5, max: 2.5, step: 0.5, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Rm = vals.mirrorRatio !== undefined ? vals.mirrorRatio : 3.0;
      const thetaDeg = vals.pitchAngle !== undefined ? vals.pitchAngle : 45;
      const B0 = vals.bMid !== undefined ? vals.bMid : 1.0;

      const thetaRad = (thetaDeg * Math.PI) / 180;
      const sinTheta = Math.sin(thetaRad);
      // Loss cone angle: sin(theta_c) = 1 / sqrt(Rm)
      const sinThetaC = 1 / Math.sqrt(Rm);
      const thetaCDeg = (Math.asin(sinThetaC) * 180) / Math.PI;

      const isTrapped = thetaDeg >= thetaCDeg;
      const Bmax = B0 * Rm;
      // Turning field: B_turn = B0 / sin^2(theta)
      const Bturn = B0 / (sinTheta * sinTheta);

      // Left visualization area: Magnetic Bottle (x: 20 to 420, y: 25 to 365)
      const mx = 25, my = 25, mw = 400, mh = 340;
      const midX = mx + mw / 2, midY = my + mh / 2;

      // Draw Mirror Coils at ends
      ctx.fillStyle = "#475569";
      // Left coils
      ctx.fillRect(mx + 20, my + 30, 16, 70);
      ctx.fillRect(mx + 20, my + mh - 100, 16, 70);
      // Right coils
      ctx.fillRect(mx + mw - 36, my + 30, 16, 70);
      ctx.fillRect(mx + mw - 36, my + mh - 100, 16, 70);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 10px Inter";
      ctx.fillText("Throat B_max", mx + 5, my + 22);
      ctx.fillText("Throat B_max", mx + mw - 75, my + 22);
      ctx.fillText("Midplane B₀", midX - 30, my + 22);

      // Draw Hourglass / Converging Magnetic Field Lines
      ctx.strokeStyle = "rgba(16, 185, 129, 0.4)"; ctx.lineWidth = 1.5;
      [-70, -35, 0, 35, 70].forEach(offset => {
        ctx.beginPath();
        ctx.moveTo(mx + 20, midY + offset * 0.4);
        ctx.bezierCurveTo(midX - 70, midY + offset * 1.3, midX + 70, midY + offset * 1.3, mx + mw - 20, midY + offset * 0.4);
        ctx.stroke();
      });

      // Bouncing or Escaping particle trajectory
      let zNorm = 0; // -1 to +1
      let zTurnNorm = Math.min(0.9, Math.sqrt(Math.max(0, 1 - 1 / (sinTheta * sinTheta * Rm))));
      if (isTrapped) {
        // Trapped particle oscillates
        const freq = 1.8;
        zNorm = Math.sin(time * freq) * zTurnNorm * 0.85;
      } else {
        // Escaping particle flies out
        zNorm = ((time * 0.8) % 2.5) - 1.2;
      }

      const pX = midX + zNorm * 160;
      const localR = 30 * (1 - 0.5 * Math.abs(zNorm));
      const gyroPhase = time * 12;
      const pY = midY + localR * Math.sin(gyroPhase);

      // Trajectory spiral trail
      ctx.strokeStyle = isTrapped ? "rgba(251, 191, 36, 0.7)" : "rgba(239, 68, 68, 0.7)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let s = -0.8; s <= 0.8; s += 0.05) {
        if (isTrapped && Math.abs(s) > zTurnNorm * 0.85) continue;
        const txNorm = s;
        const tX = midX + txNorm * 160;
        const tR = 30 * (1 - 0.5 * Math.abs(txNorm));
        const tY = midY + tR * Math.sin(gyroPhase + s * 10);
        if (s === -0.8) ctx.moveTo(tX, tY); else ctx.lineTo(tX, tY);
      }
      ctx.stroke();

      // Particle marker
      ctx.fillStyle = isTrapped ? "#f59e0b" : "#ef4444";
      ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 12;
      ctx.beginPath(); ctx.arc(pX, pY, 7, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 9px Inter"; ctx.textAlign = "center";
      ctx.fillText("q", pX, pY + 3);
      ctx.textAlign = "left";

      // Turning point markers if trapped
      if (isTrapped) {
        const turnX1 = midX - zTurnNorm * 0.85 * 160;
        const turnX2 = midX + zTurnNorm * 0.85 * 160;
        ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(turnX1, midY - 60); ctx.lineTo(turnX1, midY + 60); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(turnX2, midY - 60); ctx.lineTo(turnX2, midY + 60); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#fbbf24"; ctx.font = "9px Inter";
        ctx.fillText("Turning Point", turnX1 - 30, midY - 65);
        ctx.fillText("Turning Point", turnX2 - 30, midY - 65);
      }

      // Confinement Status Banner
      ctx.fillStyle = isTrapped ? "rgba(16, 185, 129, 0.2)" : "rgba(239, 68, 68, 0.2)";
      ctx.fillRect(mx + 20, my + mh - 40, mw - 40, 28);
      ctx.strokeStyle = isTrapped ? "#10b981" : "#ef4444"; ctx.lineWidth = 1;
      ctx.strokeRect(mx + 20, my + mh - 40, mw - 40, 28);
      ctx.fillStyle = isTrapped ? "#10b981" : "#ef4444"; ctx.font = "bold 11px Inter";
      ctx.fillText(isTrapped ? `✓ CONFINED: θ₀ (${thetaDeg}°) ≥ θ_c (${thetaCDeg.toFixed(1)}°) — Adiabatically Trapped` : `✗ LOSS CONE ESCAPE: θ₀ (${thetaDeg}°) < θ_c (${thetaCDeg.toFixed(1)}°) — Unconfined!`, mx + 30, my + mh - 22);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Magnetic Mirror Telemetry", tx + 14, ty + 24);

      const items = [
        ["Midplane Field B₀:", `${B0.toFixed(2)} T`],
        ["Mirror Ratio R_m:", `${Rm.toFixed(2)}`],
        ["Throat Max Field B_max:", `${Bmax.toFixed(2)} T`],
        ["Particle Pitch Angle θ₀:", `${thetaDeg}°`],
        ["Loss Cone Angle θ_c:", `${thetaCDeg.toFixed(2)}°`],
        ["First Invariant μ = mv_⊥²/2B:", "CONSERVED (μ = const)"],
        ["Reflection Field B_turn:", `${Bturn <= Bmax ? Bturn.toFixed(2) + " T" : "Exceeds B_max"}`],
        ["Parallel Force -μ(∂B/∂z):", isTrapped ? "Restoring to Midplane" : "Insufficient"],
        ["Confinement State:", isTrapped ? "TRAPPED (Periodic Bounce)" : "ESCAPING VIA THROAT"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 30;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 8 ? (isTrapped ? "#10b981" : "#ef4444") : (idx === 4 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 155, iy);
      });
    }
  },

  // =========================================================================
  // UNIT 4: PLASMA FLUID THEORY & IDEAL MHD
  // =========================================================================

  // 7. Plasma Pressure Gradient & Diamagnetic Drift
  "plasma-diamagnetic-drift-sim": {
    title: "Plasma Fluid Pressure Gradient & Diamagnetic Drift",
    desc: "Macroscopic fluid diamagnetic drift v_D = -(∇P x B)/(qnB²) emerging from particle gyration in a density gradient, producing diamagnetic current j_D and internal B-field reduction.",
    isAnimated: true,
    controls: [
      { id: "gradScale", label: "Gradient Scale L_n (cm)", min: 2, max: 15, step: 1, value: 6 },
      { id: "tempEv", label: "Plasma Temp T (eV)", min: 5, max: 40, step: 5, value: 20 },
      { id: "bField", label: "Field B_z (Tesla)", min: 0.5, max: 2.5, step: 0.5, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Ln_cm = vals.gradScale !== undefined ? vals.gradScale : 6;
      const Te = vals.tempEv !== undefined ? vals.tempEv : 20;
      const B = vals.bField !== undefined ? vals.bField : 1.5;

      // Diamagnetic velocity: v_D = kB T / (q B Ln)
      // vD in km/s: (1.602e-19 * Te) / (1.602e-19 * B * (Ln_cm * 0.01)) = Te / (B * Ln_cm * 0.01) * 1e-3
      const vD_kms = Te / (B * (Ln_cm * 0.01) * 1000);
      const beta = (2 * 4e-7 * Math.PI * 1e19 * 1.602e-19 * Te) / (B * B); // plasma beta

      // Left visualization: Ensemble of gyrating particles in density gradient
      const px0 = 30, py0 = 30, pw = 400, ph = 330;
      ctx.fillStyle = "rgba(15, 23, 42, 0.6)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(px0, py0, pw, ph); ctx.strokeRect(px0, py0, pw, ph);

      // Gradient background shading: High density at top, Low density at bottom
      const nGrad = ctx.createLinearGradient(0, py0, 0, py0 + ph);
      nGrad.addColorStop(0, "rgba(56, 189, 248, 0.25)");
      nGrad.addColorStop(1, "rgba(15, 23, 42, 0.05)");
      ctx.fillStyle = nGrad;
      ctx.fillRect(px0, py0, pw, ph);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Density Gradient ∇n (High Density Top ➔ Low Density Bot)", px0 + 15, py0 + 20);

      // Dividing reference line across middle
      const midY = py0 + ph / 2;
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(px0 + 20, midY); ctx.lineTo(px0 + pw - 20, midY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#fbbf24"; ctx.font = "10px Inter";
      ctx.fillText("Observation Line: Macroscopic Flux Interface", px0 + 25, midY - 6);

      // Draw gyrating particles (more at top, fewer at bottom)
      const rL = 26 / B;
      const numRings = 16;
      for (let i = 0; i < numRings; i++) {
        const row = Math.floor(i / 4);
        const col = i % 4;
        const cy = py0 + 60 + row * 65;
        const cx = px0 + 55 + col * 95;
        // Density factor determines opacity
        const opacity = Math.max(0.2, 1.0 - (row / 4) * 0.7);

        ctx.strokeStyle = `rgba(245, 158, 11, ${opacity})`;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(cx, cy, rL, 0, Math.PI * 2);
        ctx.stroke();

        // Ion dot
        const gAng = time * 4 + i;
        const ix = cx + rL * Math.cos(gAng);
        const iy = cy + rL * Math.sin(gAng);
        ctx.fillStyle = `rgba(245, 158, 11, ${opacity})`;
        ctx.beginPath(); ctx.arc(ix, iy, 4, 0, Math.PI * 2); ctx.fill();

        // Direction arrow at crossing of line
        if (row === 1) {
          // Crosses line going LEFT (counter-clockwise top half vs bottom half)
          ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.2;
          ctx.beginPath(); ctx.moveTo(cx + 8, cy + rL); ctx.lineTo(cx - 8, cy + rL); ctx.stroke();
        }
      }

      // Net Macroscopic Diamagnetic Drift Arrow
      ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
      ctx.fillRect(px0 + 20, py0 + ph - 45, pw - 40, 32);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
      ctx.strokeRect(px0 + 20, py0 + ph - 45, pw - 40, 32);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Net Fluid Diamagnetic Drift v_D: ← Leftwards (${vD_kms.toFixed(1)} km/s)`, px0 + 35, py0 + ph - 25);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Diamagnetic Fluid Telemetry", tx + 14, ty + 24);

      const items = [
        ["Gradient Scale Length L_n:", `${Ln_cm.toFixed(1)} cm`],
        ["Plasma Temperature T_e:", `${Te.toFixed(0)} eV`],
        ["Magnetic Field B_z:", `${B.toFixed(2)} T`],
        ["Ion Diamagnetic Drift v_Di:", `${vD_kms.toFixed(2)} km/s (←)`],
        ["Electron Diamagnetic Drift v_De:", `${vD_kms.toFixed(2)} km/s (→)`],
        ["Diamagnetic Current j_D:", `${(vD_kms * 1.6).toFixed(2)} kA/m²`],
        ["Guiding Center Motion:", "ZERO (Guiding centers are stationary!)"],
        ["Internal Field Reduction ΔB:", `-${(beta * 0.5 * 100).toFixed(2)}% (Diamagnetic)`],
        ["Plasma Beta β = 2μ₀P/B²:", `${(beta * 100).toFixed(3)}%`],
        ["Physics Insight:", "Pure Macroscopic Fluid Pressure Effect"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 48 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 3 || idx === 4 ? "#fbbf24" : (idx === 6 ? "#ec4899" : (idx === 7 ? "#10b981" : "#f1f5f9"));
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 155, iy);
      });
    }
  },

  // 8. Ideal MHD Magnetic Flux Freezing & Reconnection
  "plasma-flux-freezing-mhd-sim": {
    title: "Ideal MHD Magnetic Flux Freezing & Reconnection",
    desc: "Alfvén's frozen-in flux theorem (Rm >> 1) where magnetic field lines move with conducting fluid parcels, contrasted with resistive Sweet-Parker reconnection (Rm finite) at X-points.",
    isAnimated: true,
    controls: [
      { id: "resistivity", label: "Plasma Resistivity η (0: Ideal)", min: 0, max: 8, step: 1, value: 0 },
      { id: "fluidSpeed", label: "Fluid Flow Speed v₀ (km/s)", min: 10, max: 80, step: 10, value: 40 },
      { id: "mode", label: "Mode (0: Flux Freezing, 1: X-Point Reconnect)", min: 0, max: 1, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const eta = vals.resistivity !== undefined ? vals.resistivity : 0;
      const v0 = vals.fluidSpeed !== undefined ? vals.fluidSpeed : 40;
      const mode = vals.mode !== undefined ? vals.mode : 0;

      const isIdeal = eta === 0 && mode === 0;
      const Rm = eta === 0 ? 99999 : Math.max(1, Math.round(5000 / (eta + 0.1)));

      // Left visualization area: Fluid mesh & Magnetic Field lines
      const px0 = 30, py0 = 30, pw = 400, ph = 330;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(px0, py0, pw, ph); ctx.strokeRect(px0, py0, pw, ph);

      if (mode === 0) {
        // Mode 0: Alfvén Flux Freezing
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
        ctx.fillText("Alfvén Frozen-In Flux: Fluid Parcel Glued to B-Lines", px0 + 15, py0 + 20);

        // Fluid displacement vortex
        const vortexY = py0 + ph / 2 + Math.sin(time * 2) * (v0 * 0.7);

        // Deforming fluid parcel (cyan elastic quadrilateral)
        ctx.fillStyle = "rgba(56, 189, 248, 0.2)";
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
        const pLeft = px0 + 120, pRight = px0 + 260;
        ctx.beginPath();
        ctx.moveTo(pLeft, vortexY - 45);
        ctx.lineTo(pRight, vortexY - 30);
        ctx.lineTo(pRight, vortexY + 30);
        ctx.lineTo(pLeft, vortexY + 45);
        ctx.closePath();
        ctx.fill(); ctx.stroke();
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 10px Inter";
        ctx.fillText("Conducting Fluid Element", pLeft + 10, vortexY + 4);

        // Magnetic Field Lines traversing fluid
        [-60, -30, 0, 30, 60].forEach((offset, idx) => {
          ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.moveTo(px0 + 20, py0 + ph / 2 + offset);
          if (isIdeal) {
            // Perfectly glued to fluid parcel
            ctx.bezierCurveTo(
              pLeft, vortexY + offset * 0.7,
              pRight, vortexY + offset * 0.7,
              px0 + pw - 20, py0 + ph / 2 + offset
            );
          } else {
            // Slips through fluid due to resistive diffusion
            const slipFactor = Math.max(0.1, 1 - eta * 0.12);
            ctx.bezierCurveTo(
              pLeft, py0 + ph / 2 + offset + (vortexY - (py0 + ph / 2)) * slipFactor,
              pRight, py0 + ph / 2 + offset + (vortexY - (py0 + ph / 2)) * slipFactor,
              px0 + pw - 20, py0 + ph / 2 + offset
            );
          }
          ctx.stroke();

          // Field line direction arrow
          ctx.fillStyle = "#10b981";
          ctx.beginPath();
          ctx.moveTo(px0 + pw - 30, py0 + ph / 2 + offset - 4);
          ctx.lineTo(px0 + pw - 22, py0 + ph / 2 + offset);
          ctx.lineTo(px0 + pw - 30, py0 + ph / 2 + offset + 4);
          ctx.fill();
        });

      } else {
        // Mode 1: Magnetic Reconnection at X-Point
        ctx.fillStyle = "#ec4899"; ctx.font = "bold 12px Inter";
        ctx.fillText("Resistive Sweet-Parker Magnetic Reconnection (X-Point)", px0 + 15, py0 + 20);

        const xCenter = px0 + pw / 2, yCenter = py0 + ph / 2;
        const rePhase = (time * 1.5) % Math.PI;

        // Inflow arrows (vertical)
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(xCenter, yCenter - 90); ctx.lineTo(xCenter, yCenter - 35); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(xCenter, yCenter + 90); ctx.lineTo(xCenter, yCenter + 35); ctx.stroke();
        ctx.fillStyle = "#38bdf8"; ctx.font = "10px Inter";
        ctx.fillText("Plasma Inflow v_in ↓", xCenter + 8, yCenter - 55);
        ctx.fillText("Plasma Inflow v_in ↑", xCenter + 8, yCenter + 65);

        // Outflow jets (horizontal)
        ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(xCenter - 35, yCenter); ctx.lineTo(xCenter - 110, yCenter); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(xCenter + 35, yCenter); ctx.lineTo(xCenter + 110, yCenter); ctx.stroke();
        ctx.fillStyle = "#ef4444"; ctx.font = "bold 10px Inter";
        ctx.fillText("← Jet v_A", xCenter - 120, yCenter - 8);
        ctx.fillText("Jet v_A →", xCenter + 65, yCenter - 8);

        // Reconnecting Hyperbolic Field Lines
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
        [-40, -20, 20, 40].forEach(d => {
          ctx.beginPath();
          ctx.moveTo(xCenter - 120, yCenter + d * 1.8);
          ctx.quadraticCurveTo(xCenter, yCenter + d * 0.2, xCenter + 120, yCenter + d * 1.8);
          ctx.stroke();
        });

        // X-Point resistive diffusion region
        ctx.fillStyle = "rgba(236, 72, 153, 0.4)";
        ctx.fillRect(xCenter - 25, yCenter - 15, 50, 30);
        ctx.strokeStyle = "#ec4899"; ctx.strokeRect(xCenter - 25, yCenter - 15, 50, 30);
        ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px Inter"; ctx.textAlign = "center";
        ctx.fillText("X-Point", xCenter, yCenter + 4);
        ctx.textAlign = "left";
      }

      // Status banner
      ctx.fillStyle = isIdeal ? "rgba(16, 185, 129, 0.2)" : "rgba(236, 72, 153, 0.2)";
      ctx.fillRect(px0 + 20, py0 + ph - 40, pw - 40, 28);
      ctx.strokeStyle = isIdeal ? "#10b981" : "#ec4899"; ctx.lineWidth = 1;
      ctx.strokeRect(px0 + 20, py0 + ph - 40, pw - 40, 28);
      ctx.fillStyle = isIdeal ? "#10b981" : "#ec4899"; ctx.font = "bold 11px Inter";
      ctx.fillText(isIdeal ? "✓ IDEAL MHD: dΦ/dt = 0 (Magnetic Flux Rigorously Frozen In)" : `⚡ RESISTIVE DISSIPATION: R_m = ${Rm} (Magnetic Tearing & Energy Release)`, px0 + 30, py0 + ph - 22);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("MHD Flux & Reconnection Telemetry", tx + 14, ty + 24);

      const items = [
        ["Plasma Flow Speed v₀:", `${v0} km/s`],
        ["Resistivity η:", `${eta === 0 ? "0.0 (Superconducting)" : eta + " μΩ·m"}`],
        ["Magnetic Reynolds R_m:", `${Rm >= 99999 ? "∞ (Ideal MHD)" : Rm}`],
        ["Induction Equation:", "∂B/∂t = ∇×(v×B) + (η/μ₀)∇²B"],
        ["Diffusion Timescale τ_d:", `${eta === 0 ? "∞ (No Diffusion)" : (450 / eta).toFixed(1) + " ms"}`],
        ["Alfvén Outflow Speed v_out:", "v_A = B / √(μ₀ρ)"],
        ["Sweet-Parker Rate:", `${eta === 0 ? "0 (Zero Reconnection)" : (1 / Math.sqrt(Rm)).toFixed(4)} · v_A`],
        ["Energy Conversion:", "Magnetic B²/(2μ₀) ➔ Heat + Flow"],
        ["Astrophysical Manifestation:", "Solar Flares & Auroral Substorms"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 30;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 2 ? (isIdeal ? "#10b981" : "#ec4899") : (idx === 7 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 155, iy);
      });
    }
  },
// =========================================================================
  // UNIT 5: ELECTROSTATIC WAVES IN UNMAGNETIZED PLASMAS
  // =========================================================================

  // 9. Langmuir Oscillations & Bohm-Gross Wave Dispersion
  "plasma-langmuir-bohm-gross-sim": {
    title: "Langmuir Oscillations & Bohm-Gross Wave Dispersion",
    desc: "Electron plasma oscillations at w_pe and warm-plasma Bohm-Gross dispersion w² = w_pe² + 3k²v_th². Real-time wave packet propagating at group velocity v_g = dw/dk.",
    isAnimated: true,
    controls: [
      { id: "density", label: "Density n_e (10¹⁸ m⁻³)", min: 1, max: 40, step: 2, value: 10 },
      { id: "electronTemp", label: "Electron Temp T_e (eV)", min: 1, max: 30, step: 2, value: 10 },
      { id: "kVal", label: "Wavenumber k·λ_D", min: 0.05, max: 0.6, step: 0.05, value: 0.2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const ne_18 = vals.density !== undefined ? vals.density : 10;
      const Te_eV = vals.electronTemp !== undefined ? vals.electronTemp : 10;
      const kLambdaD = vals.kVal !== undefined ? vals.kVal : 0.2;

      // Physics:
      // w_pe = sqrt(ne * e^2 / (eps0 * m_e))
      // Bohm-Gross: w^2 = w_pe^2 * (1 + 3 * (k*lambda_D)^2)
      const wpe_Ghz = Math.sqrt(ne_18 * 1e18 * (1.602e-19)**2 / (8.854e-12 * 9.109e-31)) / (2 * Math.PI * 1e9);
      const w_ratio = Math.sqrt(1 + 3 * kLambdaD * kLambdaD);
      const w_Ghz = wpe_Ghz * w_ratio;
      const vth_kms = Math.sqrt(Te_eV * 1.602e-19 / 9.109e-31) / 1000;
      const vg_over_vth = 3 * kLambdaD / w_ratio;
      const vg_kms = vth_kms * vg_over_vth;
      const vph_kms = vth_kms * (w_ratio / Math.max(0.01, kLambdaD));

      // Top Visualization: Electron Slab / Density Perturbation (x: 25 to 430, y: 25 to 180)
      const px0 = 25, py0 = 25, pw = 405, ph = 160;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(px0, py0, pw, ph); ctx.strokeRect(px0, py0, pw, ph);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Langmuir Electron Density Wave: n_e(x, t)", px0 + 12, py0 + 18);

      // Draw stationary background ions
      ctx.fillStyle = "rgba(245, 158, 11, 0.25)";
      for (let ix = px0 + 20; ix < px0 + pw - 20; ix += 25) {
        for (let iy = py0 + 40; iy < py0 + ph - 25; iy += 25) {
          ctx.beginPath(); ctx.arc(ix, iy, 2.5, 0, Math.PI * 2); ctx.fill();
        }
      }
      ctx.fillStyle = "#f59e0b"; ctx.font = "9px Inter";
      ctx.fillText("+ Stationary Ion Background", px0 + 15, py0 + 34);

      // Draw oscillating electron wave profile
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      const wavePhase = time * (w_ratio * 4);
      const kSim = kLambdaD * 12;
      for (let x = 0; x <= pw - 40; x += 3) {
        const xPos = px0 + 20 + x;
        const disp = Math.sin(kSim * (x / 40) - wavePhase) * 22;
        const yPos = py0 + ph / 2 + 10 + disp;
        if (x === 0) ctx.moveTo(xPos, yPos); else ctx.lineTo(xPos, yPos);
      }
      ctx.stroke();

      // Electron particle markers tracking wave motion
      ctx.fillStyle = "#38bdf8";
      for (let i = 0; i < 18; i++) {
        const xNorm = i / 17;
        const xPos = px0 + 20 + xNorm * (pw - 40);
        const disp = Math.sin(kSim * (xNorm * (pw - 40) / 40) - wavePhase) * 22;
        const yPos = py0 + ph / 2 + 10 + disp;
        ctx.beginPath(); ctx.arc(xPos, yPos, 4, 0, Math.PI * 2); ctx.fill();
      }

      // Bottom Visualization: Bohm-Gross Dispersion Curve ω(k) (x: 25 to 430, y: 195 to 370)
      const gx = 25, gy = 195, gw = 405, gh = 175;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#ec4899"; ctx.font = "bold 12px Inter";
      ctx.fillText("Bohm-Gross Dispersion Relation: ω² = ω_pe² + 3k²v_th²", gx + 12, gy + 18);

      const ox = gx + 45, oy = gy + gh - 28, dw = gw - 65, dh = gh - 55;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + dw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - dh);
      ctx.stroke();

      ctx.font = "9px Inter"; ctx.fillStyle = "#94a3b8";
      ctx.fillText("Wavenumber k·λ_D", ox + dw - 55, oy + 16);
      ctx.fillText("ω / ω_pe", ox - 35, oy - dh + 10);

      // Bohm-Gross curve ω / ω_pe = sqrt(1 + 3 (k lambda_D)^2)
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let s = 0; s <= dw; s += 2) {
        const curK = (s / dw) * 0.7;
        const curW = Math.sqrt(1 + 3 * curK * curK);
        // map curW (1.0 to 1.6) to y
        const yCoord = oy - ((curW - 0.9) / 0.8) * dh;
        if (s === 0) ctx.moveTo(ox + s, yCoord); else ctx.lineTo(ox + s, yCoord);
      }
      ctx.stroke();

      // Cold plasma horizontal cutoff line (w = w_pe)
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      const wpeY = oy - ((1.0 - 0.9) / 0.8) * dh;
      ctx.beginPath(); ctx.moveTo(ox, wpeY); ctx.lineTo(ox + dw, wpeY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "9px Inter";
      ctx.fillText("Cold Plasma Cutoff ω = ω_pe", ox + 15, wpeY - 4);

      // Current operating point
      const ptX = ox + (kLambdaD / 0.7) * dw;
      const ptY = oy - ((w_ratio - 0.9) / 0.8) * dh;
      ctx.fillStyle = "#38bdf8";
      ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 8;
      ctx.beginPath(); ctx.arc(ptX, ptY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Group velocity tangent line
      const slope = (3 * kLambdaD / w_ratio) * (dh / dw) * (0.7 / 0.8);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(ptX - 25, ptY + 25 * slope);
      ctx.lineTo(ptX + 25, ptY - 25 * slope);
      ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.font = "9px Inter";
      ctx.fillText(`Slope = v_g (${vg_kms.toFixed(0)} km/s)`, ptX + 8, ptY - 8);

      // Right Area: Telemetry
      const tx = 455, ty = 25, tw = 275, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Langmuir Wave Telemetry", tx + 14, ty + 24);

      const items = [
        ["Plasma Density n_e:", `${ne_18} × 10¹⁸ m⁻³`],
        ["Electron Temp T_e:", `${Te_eV} eV`],
        ["Normalized Wavevector k·λ_D:", `${kLambdaD.toFixed(2)}`],
        ["Cold Plasma Freq f_pe:", `${wpe_Ghz.toFixed(2)} GHz`],
        ["Bohm-Gross Freq f:", `${w_Ghz.toFixed(2)} GHz (ω/ω_pe = ${w_ratio.toFixed(3)})`],
        ["Electron Thermal Speed v_th:", `${vth_kms.toFixed(0)} km/s`],
        ["Phase Velocity v_φ = ω/k:", `${vph_kms.toFixed(0)} km/s`],
        ["Group Velocity v_g = dω/dk:", `${vg_kms.toFixed(0)} km/s`],
        ["Energy Transport Rate:", `${(vg_over_vth * 100).toFixed(1)}% of v_th`],
        ["Kinetic Regime:", kLambdaD > 0.3 ? "STRONG KINETIC DISPERSION" : "COLD PLASMA OSCILLATION"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 4 ? "#ec4899" : (idx === 7 ? "#10b981" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // 10. Ion Acoustic Waves & Electron Debye Screening
  "plasma-ion-acoustic-wave-sim": {
    title: "Ion Acoustic Waves & Electron Debye Screening",
    desc: "Compressional plasma sound wave: heavy ion inertia and light electron shielding pressure. Demonstrates acoustic limit w = k·c_s and transition to w_pi at short wavelengths.",
    isAnimated: true,
    controls: [
      { id: "ionSpecies", label: "Ion Species (1: H⁺, 4: He⁺, 40: Ar⁺)", min: 1, max: 40, step: 1, value: 1 },
      { id: "teOverTi", label: "Temp Ratio T_e / T_i", min: 1, max: 25, step: 1, value: 10 },
      { id: "kVal", label: "Wavenumber k·λ_D", min: 0.1, max: 2.0, step: 0.1, value: 0.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const A_ion = vals.ionSpecies !== undefined ? vals.ionSpecies : 1;
      const TeTi = vals.teOverTi !== undefined ? vals.teOverTi : 10;
      const kLambdaD = vals.kVal !== undefined ? vals.kVal : 0.5;

      // Ion acoustic sound speed cs = sqrt(kB Te / Mi)
      const Te_eV = 10;
      const cs_kms = Math.sqrt(Te_eV * 1.602e-19 / (A_ion * 1.673e-27)) / 1000;
      // Dispersion: w = k * cs / sqrt(1 + k^2 * lambda_D^2)
      const w_over_wpi = kLambdaD / Math.sqrt(1 + kLambdaD * kLambdaD);
      const isDamped = TeTi < 3; // Ion Landau damping occurs if Te ~ Ti

      // Left Visualization Area: Wave Compression & Rarefaction
      const vx = 25, vy = 25, vw = 405, vh = 160;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(vx, vy, vw, vh); ctx.strokeRect(vx, vy, vw, vh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Ion Acoustic Density Perturbation: n_i(x, t)", vx + 12, vy + 18);

      // Draw density waves (vertical compression stripes)
      const waveSpeed = isDamped ? 0 : time * 3;
      for (let x = 0; x < vw - 30; x += 4) {
        const xPos = vx + 15 + x;
        const dens = Math.sin((x / 30) * kLambdaD - waveSpeed);
        const alpha = Math.max(0.05, 0.4 + 0.35 * dens);
        ctx.fillStyle = isDamped ? `rgba(239, 68, 68, ${alpha * 0.4})` : `rgba(245, 158, 11, ${alpha})`;
        ctx.fillRect(xPos, vy + 35, 3.5, vh - 45);
      }

      // Draw Ion particles oscillating longitudinally
      ctx.fillStyle = isDamped ? "#ef4444" : "#f59e0b";
      for (let i = 0; i < 22; i++) {
        const baseX = vx + 20 + i * 17;
        const disp = isDamped ? 0 : Math.sin((i * 17 / 30) * kLambdaD - waveSpeed) * 8;
        for (let j = 0; j < 4; j++) {
          ctx.beginPath();
          ctx.arc(baseX + disp, vy + 50 + j * 22, 3, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // Bottom Area: Dispersion Curve ω(k)
      const gx = 25, gy = 195, gw = 405, gh = 175;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#ec4899"; ctx.font = "bold 12px Inter";
      ctx.fillText("Ion Acoustic Dispersion: ω = k·c_s / √(1 + k²λ_D²)", gx + 12, gy + 18);

      const ox = gx + 45, oy = gy + gh - 28, dw = gw - 65, dh = gh - 55;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + dw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - dh);
      ctx.stroke();

      ctx.font = "9px Inter"; ctx.fillStyle = "#94a3b8";
      ctx.fillText("k·λ_D", ox + dw - 35, oy + 16);
      ctx.fillText("ω / ω_pi", ox - 35, oy - dh + 10);

      // Acoustic linear dashed line
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + dw * 0.6, oy - dh); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "9px Inter";
      ctx.fillText("Linear Sound Limit ω = k·c_s", ox + 10, oy - dh + 10);

      // Asymptote line w = w_pi
      ctx.strokeStyle = "rgba(239, 68, 68, 0.5)"; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(ox, oy - dh * 0.85); ctx.lineTo(ox + dw, oy - dh * 0.85); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.fillText("Asymptote: ω = ω_pi", ox + dw - 95, oy - dh * 0.85 - 4);

      // Full dispersion curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let s = 0; s <= dw; s += 2) {
        const kSim = (s / dw) * 2.5;
        const wSim = kSim / Math.sqrt(1 + kSim * kSim);
        const yCoord = oy - (wSim / 1.1) * dh * 0.85;
        if (s === 0) ctx.moveTo(ox + s, yCoord); else ctx.lineTo(ox + s, yCoord);
      }
      ctx.stroke();

      // Current operating point
      const ptX = ox + (kLambdaD / 2.5) * dw;
      const ptY = oy - (w_over_wpi / 1.1) * dh * 0.85;
      ctx.fillStyle = "#fbbf24";
      ctx.shadowColor = "#fbbf24"; ctx.shadowBlur = 8;
      ctx.beginPath(); ctx.arc(ptX, ptY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Right Area: Telemetry
      const tx = 455, ty = 25, tw = 275, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Ion Acoustic Telemetry", tx + 14, ty + 24);

      const items = [
        ["Ion Mass Species:", `A = ${A_ion} (${A_ion === 1 ? "Hydrogen" : A_ion === 4 ? "Helium" : "Argon"})`],
        ["Temperature Ratio T_e / T_i:", `${TeTi}:1`],
        ["Sound Speed c_s = √(k_B T_e / M_i):", `${cs_kms.toFixed(1)} km/s`],
        ["Normalized Frequency ω / ω_pi:", `${w_over_wpi.toFixed(3)}`],
        ["Wavevector k·λ_D:", `${kLambdaD.toFixed(2)}`],
        ["Wave Regime:", kLambdaD < 0.4 ? "Non-dispersive Sound (ω ≈ kc_s)" : "Dispersive Transition (ω ➔ ω_pi)"],
        ["Ion Landau Damping:", isDamped ? "HEAVILY DAMPED (T_e ~ T_i)" : "WEAK DAMPING (Propagates freely)"],
        ["Restoring Force:", "Electron Thermal Pressure ∇P_e"],
        ["Inertial Mass Carrier:", "Heavy Positive Ions M_i"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 6 ? (isDamped ? "#ef4444" : "#10b981") : (idx === 2 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // =========================================================================
  // UNIT 6: ELECTROMAGNETIC WAVES & DISPERSION IN PLASMAS
  // =========================================================================

  // 11. Transverse EM Wave Cutoff, Reflection & Skin Depth
  "plasma-em-wave-cutoff-sim": {
    title: "Transverse EM Wave Cutoff, Reflection & Skin Depth",
    desc: "Light wave incident from vacuum into unmagnetized plasma. Shows total reflection and evanescent exponential skin depth decay when w < w_pe, vs transparent transmission when w > w_pe.",
    isAnimated: true,
    controls: [
      { id: "density", label: "Plasma Density n_e (10¹⁸ m⁻³)", min: 1, max: 20, step: 1, value: 5 },
      { id: "freqGhz", label: "Wave Frequency f (GHz)", min: 10, max: 40, step: 2, value: 25 },
      { id: "collisionNu", label: "Collisions ν (GHz)", min: 0, max: 4, step: 0.5, value: 0.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const ne = vals.density !== undefined ? vals.density : 5;
      const f_Ghz = vals.freqGhz !== undefined ? vals.freqGhz : 25;
      const nu_Ghz = vals.collisionNu !== undefined ? vals.collisionNu : 0.5;

      // Cutoff frequency: f_pe = sqrt(ne * 1e18 * e^2 / (eps0 * m_e)) / (2 pi)
      const fpe_Ghz = Math.sqrt(ne * 1e18 * (1.602e-19)**2 / (8.854e-12 * 9.109e-31)) / (2 * Math.PI * 1e9);
      const isCutoff = f_Ghz <= fpe_Ghz;

      // Refractive index n = sqrt(1 - (fpe / f)^2)
      let n_re = 0, n_im = 0;
      if (!isCutoff) {
        n_re = Math.sqrt(1 - (fpe_Ghz / f_Ghz)**2);
      } else {
        n_im = Math.sqrt((fpe_Ghz / f_Ghz)**2 - 1);
      }

      // Skin depth delta = c / (2 pi * sqrt(fpe^2 - f^2)) in mm
      const skinDepth_mm = isCutoff ? (3e8 / (2 * Math.PI * Math.sqrt(fpe_Ghz**2 - f_Ghz**2) * 1e9)) * 1000 : 999;
      // Reflection coeff
      const R_coeff = isCutoff ? 1.0 : ((1 - n_re) / (1 + n_re))**2;

      // Left visualization: Vacuum (x: 25 to 220) vs Plasma (x: 220 to 425)
      const vx = 25, vy = 25, vw = 400, vh = 345;
      const splitX = vx + vw * 0.5;

      // Backgrounds
      ctx.fillStyle = "rgba(15, 23, 42, 0.4)";
      ctx.fillRect(vx, vy, vw * 0.5, vh); // Vacuum
      ctx.fillStyle = "rgba(56, 189, 248, 0.12)";
      ctx.fillRect(splitX, vy, vw * 0.5, vh); // Plasma
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(vx, vy, vw, vh);

      // Interface line
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(splitX, vy); ctx.lineTo(splitX, vy + vh); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#94a3b8"; ctx.font = "bold 11px Inter";
      ctx.fillText("VACUUM (n = 1)", vx + 20, vy + 20);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`PLASMA (f_pe = ${fpe_Ghz.toFixed(1)} GHz)`, splitX + 15, vy + 20);

      // Draw Incident & Reflected or Transmitted Transverse E-Field Waves
      ctx.lineWidth = 2.5;
      const cy = vy + vh / 2;
      const wPhase = time * (f_Ghz * 0.3);

      // 1. Vacuum Region
      ctx.strokeStyle = isCutoff ? "#fbbf24" : "#38bdf8";
      ctx.beginPath();
      for (let x = vx; x <= splitX; x += 2) {
        const xRel = (x - splitX) / 25;
        let Ey = 0;
        if (isCutoff) {
          // Standing wave pattern
          Ey = Math.cos(xRel * 1.5) * Math.sin(wPhase) * 45;
        } else {
          // Traveling wave
          Ey = Math.sin(xRel * 1.5 - wPhase) * 40;
        }
        if (x === vx) ctx.moveTo(x, cy + Ey); else ctx.lineTo(x, cy + Ey);
      }
      ctx.stroke();

      // 2. Plasma Region
      ctx.beginPath();
      if (isCutoff) {
        // Evanescent decay
        ctx.strokeStyle = "#ef4444";
        for (let x = splitX; x <= vx + vw; x += 2) {
          const xDepth = (x - splitX) / 18;
          const decay = Math.exp(-xDepth * (n_im + 0.3));
          const Ey = Math.sin(wPhase) * 45 * decay;
          if (x === splitX) ctx.moveTo(x, cy + Ey); else ctx.lineTo(x, cy + Ey);
        }
      } else {
        // Propagating transmitted wave (longer wavelength, higher phase velocity)
        ctx.strokeStyle = "#10b981";
        for (let x = splitX; x <= vx + vw; x += 2) {
          const xRel = (x - splitX) / 25;
          const kPlasma = 1.5 * n_re;
          const Ey = Math.sin(xRel * kPlasma - wPhase) * 40 * (1 - R_coeff);
          if (x === splitX) ctx.moveTo(x, cy + Ey); else ctx.lineTo(x, cy + Ey);
        }
      }
      ctx.stroke();

      // Skin depth envelope marker if cutoff
      if (isCutoff) {
        ctx.strokeStyle = "rgba(239, 68, 68, 0.4)"; ctx.setLineDash([2, 3]);
        ctx.beginPath();
        for (let x = splitX; x <= vx + vw; x += 2) {
          const xDepth = (x - splitX) / 18;
          const decay = Math.exp(-xDepth * (n_im + 0.3));
          if (x === splitX) ctx.moveTo(x, cy - 45 * decay); else ctx.lineTo(x, cy - 45 * decay);
        }
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#ef4444"; ctx.font = "bold 10px Inter";
        ctx.fillText(`Evanescent Skin Depth δ = ${skinDepth_mm.toFixed(1)} mm`, splitX + 25, cy - 48);
      }

      // Regime Banner
      ctx.fillStyle = isCutoff ? "rgba(239, 68, 68, 0.2)" : "rgba(16, 185, 129, 0.2)";
      ctx.fillRect(vx + 15, vy + vh - 40, vw - 30, 28);
      ctx.strokeStyle = isCutoff ? "#ef4444" : "#10b981"; ctx.lineWidth = 1;
      ctx.strokeRect(vx + 15, vy + vh - 40, vw - 30, 28);
      ctx.fillStyle = isCutoff ? "#ef4444" : "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(isCutoff ? `⛔ CUTOFF: f (${f_Ghz} GHz) < f_pe (${fpe_Ghz.toFixed(1)} GHz) — 100% Total Reflection` : `✓ PROPAGATION: f (${f_Ghz} GHz) > f_pe (${fpe_Ghz.toFixed(1)} GHz) — Wave Transmitted (n = ${n_re.toFixed(2)})`, vx + 25, vy + vh - 22);

      // Right Area: Telemetry
      const tx = 450, ty = 25, tw = 280, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("EM Wave & Cutoff Telemetry", tx + 14, ty + 24);

      const items = [
        ["Plasma Density n_e:", `${ne} × 10¹⁸ m⁻³`],
        ["Wave Frequency f:", `${f_Ghz} GHz`],
        ["Plasma Cutoff Freq f_pe:", `${fpe_Ghz.toFixed(2)} GHz`],
        ["Refractive Index n:", isCutoff ? `0.00 + i${n_im.toFixed(3)} (Evanescent)` : `${n_re.toFixed(3)} (Real)`],
        ["Power Reflection Coeff R:", `${(R_coeff * 100).toFixed(1)}%`],
        ["Power Transmission T:", `${((1 - R_coeff) * 100).toFixed(1)}%`],
        ["Evanescent Skin Depth δ:", isCutoff ? `${skinDepth_mm.toFixed(2)} mm` : "∞ (No Evanescence)"],
        ["Phase Velocity v_φ = c/n:", isCutoff ? "Undefined" : `${(3e5 / n_re).toFixed(0)} km/s (> c)`],
        ["Group Velocity v_g = c·n:", isCutoff ? "0 km/s" : `${(3e5 * n_re).toFixed(0)} km/s (< c)`],
        ["Application:", isCutoff ? "Ionospheric AM Radio Bounce" : "Satellite Optical/Microwave Uplink"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 3 ? (isCutoff ? "#ef4444" : "#10b981") : (idx === 4 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // 12. Magnetized Plasma Waves: Whistler Mode & Faraday Rotation
  "plasma-whistler-faraday-sim": {
    title: "Magnetized Plasma Waves: Whistler Mode & Faraday Rotation",
    desc: "Right-hand circularly polarized (R-wave) whistler wave helicon spiral propagating along B₀. Illustrates frequency dispersion v_g(w) and Faraday rotation angle Δθ_F of linear polarization.",
    isAnimated: true,
    controls: [
      { id: "bField", label: "Field B₀ (Tesla)", min: 0.1, max: 1.5, step: 0.1, value: 0.5 },
      { id: "density", label: "Density n_e (10¹⁸ m⁻³)", min: 1, max: 8, step: 1, value: 3 },
      { id: "wRatio", label: "Frequency Ratio ω / ω_ce", min: 0.1, max: 0.9, step: 0.05, value: 0.35 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const B0 = vals.bField !== undefined ? vals.bField : 0.5;
      const ne = vals.density !== undefined ? vals.density : 3;
      const wOverWce = vals.wRatio !== undefined ? vals.wRatio : 0.35;

      // Physics:
      // f_ce = e * B0 / (2 pi * m_e)
      const fce_Ghz = (1.602e-19 * B0 / (9.109e-31 * 2 * Math.PI)) / 1e9;
      const f_Ghz = fce_Ghz * wOverWce;
      // Whistler dispersion: n_R^2 = 1 - w_pe^2 / (w (w - w_ce)) = 1 + w_pe^2 / (w (w_ce - w))
      const fpe_Ghz = Math.sqrt(ne * 1e18 * (1.602e-19)**2 / (8.854e-12 * 9.109e-31)) / (2 * Math.PI * 1e9);
      const nR = Math.sqrt(1 + (fpe_Ghz**2) / (f_Ghz * (fce_Ghz - f_Ghz)));
      const faradayDeg_m = (fpe_Ghz**2 * fce_Ghz / (2 * (f_Ghz**2))) * 12;

      // Left Visualization Area: 3D Helicon Spiral Whistler Wave
      const vx = 25, vy = 25, vw = 405, vh = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(vx, vy, vw, vh); ctx.strokeRect(vx, vy, vw, vh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Whistler Helicon Wave Spiral (Along Background B₀ →)", vx + 15, vy + 20);

      // Central axis (B0 field line)
      const cy = vy + vh / 2;
      ctx.strokeStyle = "rgba(16, 185, 129, 0.4)"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(vx + 20, cy); ctx.lineTo(vx + vw - 20, cy); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#10b981"; ctx.font = "10px Inter";
      ctx.fillText("B₀ Axis →", vx + vw - 75, cy - 8);

      // Draw rotating 3D helical spiral
      const spiralRadius = 45;
      const helixPitch = 25;
      const tPhase = time * (wOverWce * 6);

      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let s = 0; s <= vw - 50; s += 2) {
        const xPos = vx + 25 + s;
        const ang = (s / helixPitch) * 2 - tPhase;
        const yPos = cy + spiralRadius * Math.sin(ang);
        if (s === 0) ctx.moveTo(xPos, yPos); else ctx.lineTo(xPos, yPos);
      }
      ctx.stroke();

      // Helical projection shading (R-wave circular polarization arrows)
      for (let s = 0; s <= vw - 50; s += 45) {
        const xPos = vx + 25 + s;
        const ang = (s / helixPitch) * 2 - tPhase;
        const yPos = cy + spiralRadius * Math.sin(ang);
        ctx.strokeStyle = "rgba(56, 189, 248, 0.6)"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(xPos, cy); ctx.lineTo(xPos, yPos); ctx.stroke();
        ctx.fillStyle = "#38bdf8";
        ctx.beginPath(); ctx.arc(xPos, yPos, 3, 0, Math.PI * 2); ctx.fill();
      }

      // Faraday Rotation dial indicator at bottom
      const dialX = vx + vw / 2, dialY = vy + vh - 45, dialR = 25;
      ctx.fillStyle = "#020617";
      ctx.beginPath(); ctx.arc(dialX, dialY, dialR, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5; ctx.stroke();

      const fAngle = (time * 1.5) % (Math.PI * 2);
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(dialX, dialY);
      ctx.lineTo(dialX + dialR * Math.cos(fAngle), dialY + dialR * Math.sin(fAngle));
      ctx.stroke();
      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 9px Inter";
      ctx.fillText("Faraday Plane Rotation Δθ_F", dialX - 65, dialY - dialR - 5);

      // Right Area: Telemetry
      const tx = 450, ty = 25, tw = 280, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Whistler & Faraday Telemetry", tx + 14, ty + 24);

      const items = [
        ["Magnetic Field B₀:", `${B0.toFixed(2)} T`],
        ["Cyclotron Frequency f_ce:", `${fce_Ghz.toFixed(2)} GHz`],
        ["Whistler Frequency f:", `${f_Ghz.toFixed(2)} GHz (f/f_ce = ${wOverWce.toFixed(2)})`],
        ["Whistler Index n_R:", `${nR.toFixed(2)} (Slow Wave n >> 1)`],
        ["Polarization State:", "Right-Hand Circular (R-wave)"],
        ["Group Velocity v_g:", `${((3e5 / nR) * 2 * (1 - wOverWce)).toFixed(0)} km/s`],
        ["Frequency Dispersion:", "Higher frequencies travel faster!"],
        ["Audible Manifestation:", "Descending Pitch Whistle ('Pwee-oo')"],
        ["Faraday Rotation Δθ_F:", `~${faradayDeg_m.toFixed(1)}° / meter`],
        ["Space Application:", "Interplanetary Magnetic Field Probing"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 3 ? "#ec4899" : (idx === 7 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // =========================================================================
  // UNIT 7: MAGNETOHYDRODYNAMIC WAVES & INSTABILITIES
  // =========================================================================

  // 13. Shear Alfvén Waves & MHD Oscillations
  "plasma-alfven-wave-sim": {
    title: "Shear Alfvén Waves & MHD Oscillations",
    desc: "Transverse shear Alfvén wave where magnetic field lines act as vibrating elastic strings under tension T = B₀²/μ₀, mass density ρ_m provides inertia, and kinetic & magnetic wave energies are equally partitioned.",
    isAnimated: true,
    controls: [
      { id: "bField", label: "Field B₀ (Tesla)", min: 0.5, max: 3.5, step: 0.5, value: 2.0 },
      { id: "massDens", label: "Mass Density ρ_m (10⁻⁶ kg/m³)", min: 1, max: 20, step: 1, value: 5 },
      { id: "waveLen", label: "Wavelength λ (m)", min: 0.5, max: 4.0, step: 0.5, value: 2.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const B0 = vals.bField !== undefined ? vals.bField : 2.0;
      const rho = (vals.massDens !== undefined ? vals.massDens : 5) * 1e-6;
      const lambda = vals.waveLen !== undefined ? vals.waveLen : 2.0;

      // v_A = B0 / sqrt(mu0 * rho)
      const mu0 = 4 * Math.PI * 1e-7;
      const vA_kms = (B0 / Math.sqrt(mu0 * rho)) / 1000;
      const tension_MPa = (B0 * B0 / (2 * mu0)) / 1e6;
      const f_Hz = (vA_kms * 1000) / lambda;

      // Left Visualization: Plucked Magnetic String
      const vx = 25, vy = 25, vw = 405, vh = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(vx, vy, vw, vh); ctx.strokeRect(vx, vy, vw, vh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Transverse Shear Alfvén Wave (Field Lines as Strings)", vx + 15, vy + 20);

      // Undisturbed axis
      const cy = vy + vh / 2;
      ctx.strokeStyle = "rgba(148, 163, 184, 0.3)"; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(vx + 20, cy); ctx.lineTo(vx + vw - 20, cy); ctx.stroke();
      ctx.setLineDash([]);

      // Draw plucked magnetic field lines
      const wavePhase = time * 3.5;
      const kSim = 2 * Math.PI / (lambda * 35);
      [-40, -20, 0, 20, 40].forEach((offset, idx) => {
        ctx.strokeStyle = idx === 2 ? "#10b981" : "rgba(16, 185, 129, 0.5)";
        ctx.lineWidth = idx === 2 ? 3 : 1.5;
        ctx.beginPath();
        for (let x = 0; x <= vw - 40; x += 3) {
          const xPos = vx + 20 + x;
          const yDisp = Math.sin(kSim * x - wavePhase) * 32;
          const yPos = cy + offset + yDisp;
          if (x === 0) ctx.moveTo(xPos, yPos); else ctx.lineTo(xPos, yPos);
        }
        ctx.stroke();
      });

      // Transverse velocity perturbation arrows v1 perp
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2;
      for (let x = 30; x <= vw - 60; x += 55) {
        const xPos = vx + 20 + x;
        const yDisp = Math.sin(kSim * x - wavePhase) * 32;
        const vDir = Math.cos(kSim * x - wavePhase);
        ctx.beginPath();
        ctx.moveTo(xPos, cy + yDisp);
        ctx.lineTo(xPos, cy + yDisp - vDir * 20);
        ctx.stroke();
      }
      ctx.fillStyle = "#fbbf24"; ctx.font = "10px Inter";
      ctx.fillText("Fluid Velocity Perturbation v₁ ↕", vx + 25, vy + 45);

      // Energy Equipartition Bars at bottom
      const eBarY = vy + vh - 45;
      ctx.fillStyle = "#38bdf8"; ctx.fillRect(vx + 25, eBarY, (vw - 50) * 0.5, 14);
      ctx.fillStyle = "#ec4899"; ctx.fillRect(vx + 25 + (vw - 50) * 0.5, eBarY, (vw - 50) * 0.5, 14);
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 9px Inter";
      ctx.fillText("Kinetic Energy ½ρv₁² (50%)", vx + 35, eBarY + 11);
      ctx.fillText("Magnetic Energy b₁²/2μ₀ (50%)", vx + 35 + (vw - 50) * 0.5, eBarY + 11);

      // Right Area: Telemetry
      const tx = 450, ty = 25, tw = 280, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Alfvén Wave Telemetry", tx + 14, ty + 24);

      const items = [
        ["Magnetic Field B₀:", `${B0.toFixed(2)} T`],
        ["Plasma Mass Density ρ_m:", `${(rho * 1e6).toFixed(1)} × 10⁻⁶ kg/m³`],
        ["Wavelength λ:", `${lambda.toFixed(2)} m`],
        ["Alfvén Velocity v_A:", `${vA_kms.toFixed(1)} km/s`],
        ["Magnetic String Tension B₀²/2μ₀:", `${tension_MPa.toFixed(2)} MPa`],
        ["Wave Frequency f_A:", `${(f_Hz / 1000).toFixed(2)} kHz`],
        ["Wave Impedance Z_A:", "Z_A = μ₀ v_A"],
        ["Energy Equipartition:", "EXACT: E_kinetic = E_magnetic"],
        ["Compression:", "INCOMPRESSIBLE (∇·v = 0, δρ = 0)"],
        ["Astrophysical Realm:", "Solar Corona Heating & Solar Wind"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 3 ? "#10b981" : (idx === 7 ? "#ec4899" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // 14. MHD Instabilities: Rayleigh-Taylor & Tokamak Kink (m=1)
  "plasma-rayleigh-taylor-kink-sim": {
    title: "MHD Instabilities: Rayleigh-Taylor & Tokamak Kink (m=1)",
    desc: "Rayleigh-Taylor gravitational interface bubbles and tokamak m=1 helical kink instability governed by the Kruskal-Shafranov safety factor limit q(a) < 1.",
    isAnimated: true,
    controls: [
      { id: "mode", label: "Mode (0: Rayleigh-Taylor, 1: Tokamak Kink)", min: 0, max: 1, step: 1, value: 0 },
      { id: "drive", label: "Drive Force (Gravity / Current)", min: 1, max: 10, step: 1, value: 6 },
      { id: "stabilization", label: "Shear Field / Safety Factor", min: 1, max: 10, step: 1, value: 3 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const mode = vals.mode !== undefined ? vals.mode : 0;
      const drive = vals.drive !== undefined ? vals.drive : 6;
      const stab = vals.stabilization !== undefined ? vals.stabilization : 3;

      // Mode 0: RT instability, Mode 1: Tokamak kink
      const isUnstable = drive > stab * 1.3;
      const growthRate = isUnstable ? Math.sqrt(drive - stab) * 0.8 : 0;

      // Left Visualization Area
      const vx = 25, vy = 25, vw = 405, vh = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(vx, vy, vw, vh); ctx.strokeRect(vx, vy, vw, vh);

      if (mode === 0) {
        // Rayleigh-Taylor Interface
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
        ctx.fillText("Plasma Rayleigh-Taylor Instability (Mushroom Fingers)", vx + 15, vy + 20);

        // Dense plasma on top, Light magnetic field on bottom
        const midY = vy + vh / 2;
        const amp = isUnstable ? Math.min(65, 12 + growthRate * (15 + Math.sin(time * 3) * 5)) : 10;

        // Draw mushroom bubble & spike interface
        ctx.fillStyle = "rgba(244, 63, 94, 0.35)";
        ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(vx + 15, vy + 35);
        ctx.lineTo(vx + vw - 15, vy + 35);
        ctx.lineTo(vx + vw - 15, midY);

        for (let x = vw - 15; x >= 15; x -= 3) {
          const xNorm = x / 45;
          const finger = Math.cos(xNorm * 2) * amp + (isUnstable ? Math.cos(xNorm * 4) * (amp * 0.3) : 0);
          ctx.lineTo(vx + x, midY + finger);
        }
        ctx.closePath();
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#ec4899"; ctx.font = "bold 10px Inter";
        ctx.fillText("Dense Heavy Plasma (Effective Gravity g ↓)", vx + 25, vy + 55);
        ctx.fillStyle = "#10b981";
        ctx.fillText("Magnetic Pressure B²/(2μ₀) Supporting Base ↑", vx + 25, vy + vh - 45);

      } else {
        // Tokamak Kink Instability
        ctx.fillStyle = "#ec4899"; ctx.font = "bold 12px Inter";
        ctx.fillText("Tokamak m=1 Helical Kink Disruption (q < 1)", vx + 15, vy + 20);

        const cy = vy + vh / 2;
        const kinkAmp = isUnstable ? Math.min(55, 15 + growthRate * 12) : 8;
        const kPhase = time * 2;

        // Twisted helical plasma column
        ctx.strokeStyle = isUnstable ? "#ef4444" : "#10b981";
        ctx.lineWidth = 24;
        ctx.lineCap = "round";
        ctx.beginPath();
        for (let x = 20; x <= vw - 20; x += 5) {
          const xPos = vx + x;
          const yDisp = Math.sin((x / 50) + kPhase) * kinkAmp;
          if (x === 20) ctx.moveTo(xPos, cy + yDisp); else ctx.lineTo(xPos, cy + yDisp);
        }
        ctx.stroke();

        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        for (let x = 20; x <= vw - 20; x += 5) {
          const xPos = vx + x;
          const yDisp = Math.sin((x / 50) + kPhase) * kinkAmp;
          if (x === 20) ctx.moveTo(xPos, cy + yDisp); else ctx.lineTo(xPos, cy + yDisp);
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Stability Banner
      ctx.fillStyle = isUnstable ? "rgba(239, 68, 68, 0.25)" : "rgba(16, 185, 129, 0.25)";
      ctx.fillRect(vx + 15, vy + vh - 40, vw - 30, 28);
      ctx.strokeStyle = isUnstable ? "#ef4444" : "#10b981"; ctx.lineWidth = 1;
      ctx.strokeRect(vx + 15, vy + vh - 40, vw - 30, 28);
      ctx.fillStyle = isUnstable ? "#ef4444" : "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(isUnstable ? `⚠️ UNSTABLE DISRUPTION: Drive (${drive}) > Shear (${stab}) — Growth γ = ${growthRate.toFixed(2)}` : `✓ STABILIZED: Magnetic Shear / Safety Factor Prevents Mode Growth`, vx + 25, vy + vh - 22);

      // Right Area: Telemetry
      const tx = 450, ty = 25, tw = 280, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("MHD Stability Telemetry", tx + 14, ty + 24);

      const qSafety = (stab / Math.max(1, drive) * 1.5).toFixed(2);

      const items = [
        ["Selected Instability:", mode === 0 ? "Rayleigh-Taylor (Interchange)" : "Tokamak Kink (m=1, n=1)"],
        ["Drive Free Energy:", `${drive} / 10`],
        ["Magnetic Stabilization:", `${stab} / 10`],
        ["Safety Factor q(a):", `${qSafety} (${parseFloat(qSafety) >= 1 ? "q > 1 Stable" : "q < 1 Unstable"})`],
        ["Growth Rate γ:", `${growthRate.toFixed(3)} s⁻¹`],
        ["Kruskal-Shafranov Limit:", "q(a) = a B_z / (R B_θ) > 1 required"],
        ["Shear Stabilization:", "(k·B)² / μ₀ρ opposing drive"],
        ["Disruption Consequence:", isUnstable ? "Loss of Confinement / Wall Impact" : "Quiescent Stable Equilibrium"],
        ["Tokamak Operation:", "Restricted by Greenwald & Troyon limits"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 3 ? (parseFloat(qSafety) >= 1 ? "#10b981" : "#ef4444") : (idx === 4 ? "#ec4899" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // =========================================================================
  // UNIT 8: KINETIC THEORY & LANDAU DAMPING
  // =========================================================================

  // 15. 1D-1V Kinetic Vlasov Phase Space (x, v) & Vortex Filamentation
  "plasma-vlasov-phase-space-sim": {
    title: "1D-1V Kinetic Vlasov Phase Space (x, v) & Vortex Filamentation",
    desc: "Numerical phase space distribution f(x, v, t) obeying collisionless Vlasov equation. Demonstrates electrostatic vortex rollup, BGK electron holes, and fine-scale phase filamentation.",
    isAnimated: true,
    controls: [
      { id: "pertAmp", label: "Initial Perturbation ε", min: 0.05, max: 0.4, step: 0.05, value: 0.2 },
      { id: "vth", label: "Thermal Velocity v_th", min: 0.6, max: 2.0, step: 0.2, value: 1.2 },
      { id: "vortexSpeed", label: "Vortex Rotation Speed", min: 1, max: 5, step: 1, value: 2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const eps = vals.pertAmp !== undefined ? vals.pertAmp : 0.2;
      const vth = vals.vth !== undefined ? vals.vth : 1.2;
      const vSpeed = vals.vortexSpeed !== undefined ? vals.vortexSpeed : 2;

      // Left Visualization: Phase Space (x, v) Map
      const px0 = 25, py0 = 25, pw = 405, ph = 345;
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(px0, py0, pw, ph); ctx.strokeRect(px0, py0, pw, ph);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Vlasov Phase Space Distribution f(x, v, t)", px0 + 15, py0 + 20);

      // Coordinate axes
      const cx = px0 + pw / 2, cy = py0 + ph / 2;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(px0 + 15, cy); ctx.lineTo(px0 + pw - 15, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, py0 + 35); ctx.lineTo(cx, py0 + ph - 15); ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "9px Inter";
      ctx.fillText("x (Space) →", px0 + pw - 65, cy - 6);
      ctx.fillText("v (Velocity) ↑", cx + 8, py0 + 45);

      // Phase space vortex generation
      const rot = time * (0.8 * vSpeed);
      const cols = 28, rows = 22;
      const dx = (pw - 60) / cols;
      const dy = (ph - 80) / rows;

      for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {
          const xVal = (i - cols / 2) * 0.25;
          const yVal = (j - rows / 2) * 0.25;
          // Vortex rotation transformation
          const r = Math.sqrt(xVal * xVal + yVal * yVal);
          const theta = Math.atan2(yVal, xVal) - rot * Math.exp(-r * 0.8);

          const xOrig = r * Math.cos(theta);
          const yOrig = r * Math.sin(theta);

          // Maxwellian + Perturbation
          const f0 = Math.exp(-(yOrig * yOrig) / (2 * vth * vth));
          const pert = 1 + eps * Math.cos(xOrig * 2);
          const fVal = Math.max(0, Math.min(1, f0 * pert));

          if (fVal > 0.08) {
            ctx.fillStyle = fVal > 0.6 ? `rgba(236, 72, 153, ${fVal})` : (fVal > 0.3 ? `rgba(56, 189, 248, ${fVal})` : `rgba(30, 41, 59, ${fVal})`);
            ctx.fillRect(px0 + 30 + i * dx, py0 + 45 + j * dy, dx - 1, dy - 1);
          }
        }
      }

      // BGK Hole Label
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 10px Inter";
      ctx.fillText("BGK Phase Space Vortex (Trapped Electron Hole)", cx - 110, cy - 70);

      // Right Area: Telemetry
      const tx = 450, ty = 25, tw = 280, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Kinetic Vlasov Telemetry", tx + 14, ty + 24);

      const items = [
        ["Governing Equation:", "∂f/∂t + v·∂f/∂x - (eE/m)·∂f/∂v = 0"],
        ["Thermal Speed v_th:", `${vth.toFixed(2)} × 10⁶ m/s`],
        ["Initial Perturbation ε:", `${eps.toFixed(2)}`],
        ["Casimir Invariant ∫f² dx dv:", "CONSERVED (No dissipation)"],
        ["Phase Space Incompressibility:", "Liouville Theorem: df/dt = 0"],
        ["Vortex Rotation Period τ_B:", `${(6.28 / (0.8 * vSpeed)).toFixed(2)} s`],
        ["Entropy S = -∫ f ln f:", "Strictly Constant (Coarse graining ↑)"],
        ["Phenomenon:", "Nonlinear Phase Filamentation"],
        ["Equilibrium Structure:", "Bernstein-Greene-Kruskal (BGK) Mode"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 3 ? "#10b981" : (idx === 8 ? "#ec4899" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // 16. Kinetic Landau Damping: Wave-Particle Resonant Energy Exchange
  "plasma-landau-damping-sim": {
    title: "Kinetic Landau Damping: Resonant Wave-Particle Energy Exchange",
    desc: "Collisionless Landau damping where resonant particles (v ≈ w/k) exchange energy with wave. Negative slope ∂f₀/∂v < 0 yields exponential wave decay E(t) = E₀ e^γt without collisions.",
    isAnimated: true,
    controls: [
      { id: "vPhase", label: "Phase Velocity v_φ / v_th", min: 1.2, max: 3.2, step: 0.1, value: 2.2 },
      { id: "initialE0", label: "Initial Field E₀ (kV/m)", min: 2, max: 20, step: 2, value: 10 },
      { id: "slopeMode", label: "Distribution (0: Maxwellian, 1: Bump-on-Tail)", min: 0, max: 1, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const vphi = vals.vPhase !== undefined ? vals.vPhase : 2.2;
      const E0 = vals.initialE0 !== undefined ? vals.initialE0 : 10;
      const mode = vals.slopeMode !== undefined ? vals.slopeMode : 0;

      // Maxwellian slope at vphi: df/dv = -vphi * exp(-vphi^2 / 2)
      // Bump-on-tail slope can be positive!
      let slope = -vphi * Math.exp(-0.5 * vphi * vphi);
      if (mode === 1) {
        // Bump at v = 2.0
        const bump = Math.exp(-0.5 * ((vphi - 2.2) / 0.3)**2);
        slope = 0.6 * bump - 0.2; // positive for bump
      }

      const gamma = slope * 0.45;
      const isDamping = gamma < 0;

      // Top Visualization: Velocity Distribution f(v) and Resonant Marker
      const vx = 25, vy = 25, vw = 405, vh = 160;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(vx, vy, vw, vh); ctx.strokeRect(vx, vy, vw, vh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText(mode === 0 ? "Maxwellian f₀(v): Negative Slope (∂f/∂v < 0) ➔ Wave Damps" : "Bump-on-Tail f₀(v): Positive Slope (∂f/∂v > 0) ➔ Two-Stream Growth", vx + 12, vy + 18);

      // Axes for f(v)
      const ox = vx + 40, oy = vy + vh - 25, dw = vw - 60, dh = vh - 50;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + dw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - dh);
      ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "9px Inter";
      ctx.fillText("v / v_th", ox + dw - 35, oy + 16);
      ctx.fillText("f₀(v)", ox - 30, oy - dh + 10);

      // Plot f(v)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let s = 0; s <= dw; s += 2) {
        const vNorm = (s / dw) * 4.0;
        let fVal = Math.exp(-0.5 * vNorm * vNorm);
        if (mode === 1) {
          fVal += 0.45 * Math.exp(-0.5 * ((vNorm - 2.2) / 0.35)**2);
        }
        const yCoord = oy - (fVal / 1.4) * dh;
        if (s === 0) ctx.moveTo(ox + s, yCoord); else ctx.lineTo(ox + s, yCoord);
      }
      ctx.stroke();

      // Resonant velocity v_phi marker
      const resX = ox + (vphi / 4.0) * dw;
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(resX, oy); ctx.lineTo(resX, oy - dh); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 9px Inter";
      ctx.fillText(`Resonant v_φ = ${vphi.toFixed(1)} v_th`, resX - 35, oy - dh - 2);

      // Tangent slope indicator
      ctx.fillStyle = slope < 0 ? "#10b981" : "#ef4444";
      ctx.font = "bold 10px Inter";
      ctx.fillText(`∂f/∂v = ${slope.toFixed(2)} (${slope < 0 ? "Absorption > Emission" : "Emission > Absorption"})`, ox + 15, oy - dh + 22);

      // Bottom Visualization: Decaying or Growing Electric Wave E(t)
      const gx = 25, gy = 195, gw = 405, gh = 175;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = isDamping ? "#10b981" : "#ef4444"; ctx.font = "bold 12px Inter";
      ctx.fillText(isDamping ? "Collisionless Landau Damped Wave E(t) = E₀ e^(γt) (γ < 0)" : "Inverse Landau Instability Growth E(t) = E₀ e^(γt) (γ > 0)", gx + 12, gy + 18);

      const eox = gx + 40, eoy = gy + gh / 2 + 10, edw = gw - 60;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(eox, eoy); ctx.lineTo(eox + edw, eoy); ctx.stroke();
      ctx.setLineDash([]);

      // Wave profile
      ctx.strokeStyle = isDamping ? "#10b981" : "#ef4444"; ctx.lineWidth = 2;
      ctx.beginPath();
      const simT = (time * 1.5) % 8;
      for (let s = 0; s <= edw; s += 2) {
        const tVal = (s / edw) * 6;
        const decay = Math.exp(gamma * tVal);
        const yCoord = eoy - Math.sin(tVal * 8 - time * 6) * 35 * Math.min(2.0, Math.max(0.05, decay));
        if (s === 0) ctx.moveTo(eox + s, yCoord); else ctx.lineTo(eox + s, yCoord);
      }
      ctx.stroke();

      // Right Area: Telemetry
      const tx = 450, ty = 25, tw = 280, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Landau Damping Telemetry", tx + 14, ty + 24);

      const items = [
        ["Phase Velocity v_φ:", `${vphi.toFixed(2)} v_th`],
        ["Initial Field E₀:", `${E0} kV/m`],
        ["Distribution Slope ∂f₀/∂v:", `${slope.toFixed(3)}`],
        ["Landau Damping Rate γ/ω_r:", `${gamma.toFixed(3)}`],
        ["Process Type:", isDamping ? "COLLISIONLESS DAMPING (γ < 0)" : "TWO-STREAM INSTABILITY (γ > 0)"],
        ["Dissipation Nature:", "Reversible Phase Mixing in Phase Space"],
        ["Resonant Bounce Freq ω_B:", `${(Math.sqrt(E0) * 1.8).toFixed(2)} kHz (Trapping)`],
        ["Energy Conservation:", "Wave Field Energy ➔ Resonant Particles"],
        ["Thermal Collision Role:", "ZERO (Pure Vlasov-Poisson dynamics)"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 4 ? (isDamping ? "#10b981" : "#ef4444") : (idx === 3 ? "#ec4899" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  }
};

// Simulation Engine Adapter for Open STEM Library App Controller
window.SimulationEngine = window.SimulationEngine || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = "";

  const simConfig = (window.PLASMA_SIMS && window.PLASMA_SIMS[simType]) ||
                    (window.ASTRO_SIMS && window.ASTRO_SIMS[simType]) ||
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
      wrap.style.minWidth = "160px";

      const lbl = document.createElement("label");
      lbl.innerText = `${c.label}: ${c.value}`;
      lbl.style.fontSize = "0.8rem";
      lbl.style.color = "#94a3b8";

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
