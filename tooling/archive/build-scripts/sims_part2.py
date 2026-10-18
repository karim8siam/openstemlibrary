
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
