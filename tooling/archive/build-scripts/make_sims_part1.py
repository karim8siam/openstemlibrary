# Generator for simulations 1 to 8 of Plasma Physics
import json

part1_code = """
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
"""

with open("sims_part1.py", "w") as f:
    f.write(part1_code)

print("Part 1 written successfully.")
