import json

part2_js = r'''
  // =========================================================================
  // UNIT 3: MAGNETIC PROPERTIES OF MATERIALS (DIAMAGNETISM & PARAMAGNETISM)
  // =========================================================================

  // 5. Quantum Brillouin Paramagnetism & Langevin Theory
  "ssp2-brillouin-paramagnetism-sim": {
    title: "Quantum Brillouin Paramagnetism vs Classical Langevin Theory",
    desc: "Rigorous quantum statistical mechanics of magnetic moments in applied field B. Computes Brillouin function B_J(η) for arbitrary angular momentum J, Zeeman level occupancies, and Curie-law limits.",
    isAnimated: true,
    controls: [
      { id: "spinJ", label: "Angular Momentum J", min: 0.5, max: 2.5, step: 0.5, value: 0.5 },
      { id: "magB", label: "Magnetic Field B (Tesla)", min: 0.1, max: 10.0, step: 0.2, value: 2.0 },
      { id: "tempT", label: "Temperature T (Kelvin)", min: 2.0, max: 100.0, step: 2.0, value: 15.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const J = vals.spinJ !== undefined ? vals.spinJ : 0.5;
      const B = vals.magB !== undefined ? vals.magB : 2.0;
      const T = vals.tempT !== undefined ? vals.tempT : 15.0;

      const g = 2.0;
      const muB = 9.274e-24; // J/T
      const kB = 1.381e-23; // J/K
      const x = (g * muB * B) / (kB * T);
      const eta = J * x;

      // Brillouin function: B_J(eta) = (2J+1)/(2J) coth((2J+1)eta/(2J)) - 1/(2J) coth(eta/(2J))
      function coth(val) {
        if (Math.abs(val) < 1e-6) return 1 / val;
        return (Math.exp(val) + Math.exp(-val)) / (Math.exp(val) - Math.exp(-val));
      }
      function brillouin(jVal, etaVal) {
        if (etaVal < 1e-4) return (jVal + 1) / (3 * jVal) * etaVal;
        const c1 = (2 * jVal + 1) / (2 * jVal);
        const c2 = 1 / (2 * jVal);
        return c1 * coth(c1 * etaVal) - c2 * coth(c2 * etaVal);
      }
      function langevin(xVal) {
        if (xVal < 1e-4) return xVal / 3;
        return coth(xVal) - 1 / xVal;
      }

      const BJ_curr = Math.min(1.0, Math.max(0.0, brillouin(J, eta)));
      const L_curr = Math.min(1.0, Math.max(0.0, langevin(eta)));

      // Split canvas: Left is M/Ms vs eta curves; Right is Zeeman energy levels & Boltzmann population
      const splitX = Math.floor(w * 0.55);

      // --- LEFT: Brillouin Function Plots ---
      const plotL = { x: 45, y: 35, w: splitX - 65, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Magnetization M/M_s vs Scaling Parameter η = gμ_B JB / k_B T", plotL.x, plotL.y - 12);

      // Grid lines
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 0.8;
      for (let gy = 0.25; gy <= 1.0; gy += 0.25) {
        const ypos = plotL.y + plotL.h * (1 - gy);
        ctx.beginPath(); ctx.moveTo(plotL.x, ypos); ctx.lineTo(plotL.x + plotL.w, ypos); ctx.stroke();
        ctx.fillStyle = "#475569"; ctx.font = "9px Inter"; ctx.fillText(gy.toFixed(2), plotL.x + 5, ypos - 3);
      }

      const maxEta = 4.0;
      // Plot classical Langevin (J -> inf)
      ctx.beginPath(); ctx.strokeStyle = "#64748b"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.5;
      for (let i = 0; i <= 60; i++) {
        const evalEta = (i / 60) * maxEta;
        const valL = langevin(evalEta);
        const px = plotL.x + (evalEta / maxEta) * plotL.w;
        const py = plotL.y + plotL.h * (1 - valL);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke(); ctx.setLineDash([]);

      // Plot Brillouin curve for current J
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.4;
      for (let i = 0; i <= 60; i++) {
        const evalEta = (i / 60) * maxEta;
        const valB = brillouin(J, evalEta);
        const px = plotL.x + (evalEta / maxEta) * plotL.w;
        const py = plotL.y + plotL.h * (1 - valB);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current operational dot
      const opEta = Math.min(maxEta, eta);
      const opPx = plotL.x + (opEta / maxEta) * plotL.w;
      const opPy = plotL.y + plotL.h * (1 - BJ_curr);
      ctx.beginPath(); ctx.arc(opPx, opPy, 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#10b981"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      // Legend
      ctx.fillStyle = "#38bdf8"; ctx.fillRect(plotL.x + plotL.w - 140, plotL.y + plotL.h - 45, 12, 3);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter"; ctx.fillText(`Brillouin B_J (J = ${J})`, plotL.x + plotL.w - 122, plotL.y + plotL.h - 42);
      ctx.fillStyle = "#64748b"; ctx.fillRect(plotL.x + plotL.w - 140, plotL.y + plotL.h - 25, 12, 3);
      ctx.fillText("Classical Langevin L(x)", plotL.x + plotL.w - 122, plotL.y + plotL.h - 22);

      // --- RIGHT: Zeeman Splittings & Population ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText(`Zeeman Energy Levels: m_J ∈ [-${J}, +${J}]`, plotR.x, plotR.y - 12);

      const numLevels = Math.round(2 * J + 1);
      const levelH = plotR.h / (numLevels + 1);
      let sumExp = 0;
      const mValues = [];
      for (let m = -J; m <= J + 1e-4; m += 1.0) {
        const energy = -g * muB * m * B; // Joules
        const expFactor = Math.exp(-energy / (kB * T));
        sumExp += expFactor;
        mValues.push({ m: m, energy: energy, expFactor: expFactor });
      }

      mValues.forEach((item, idx) => {
        const prob = item.expFactor / sumExp;
        const ly = plotR.y + plotR.h - (idx + 1) * levelH;

        // Energy line
        ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(plotR.x + 25, ly); ctx.lineTo(plotR.x + 130, ly); ctx.stroke();

        ctx.fillStyle = "#c084fc"; ctx.font = "10px Inter";
        ctx.fillText(`m = ${item.m > 0 ? "+" : ""}${item.m}`, plotR.x + 30, ly - 5);

        // Population bar
        const barMaxW = plotR.w - 200;
        const barW = prob * barMaxW;
        ctx.fillStyle = "rgba(16, 185, 129, 0.75)";
        ctx.fillRect(plotR.x + 145, ly - 8, barW, 16);
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x + 145, ly - 8, barW, 16);

        ctx.fillStyle = "#f1f5f9"; ctx.font = "bold 10px Inter";
        ctx.fillText(`${(prob * 100).toFixed(1)}%`, plotR.x + 155 + barW, ly + 4);
      });

      // Bottom Telemetry
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, plotR.y + plotR.h - 55, plotR.w - 20, 48);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, plotR.y + plotR.h - 55, plotR.w - 20, 48);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`M / M_s = ${BJ_curr.toFixed(3)}  |  Langevin = ${L_curr.toFixed(3)}`, plotR.x + 20, plotR.y + plotR.h - 35);
      const isCurie = eta < 0.3;
      ctx.fillStyle = isCurie ? "#10b981" : "#f59e0b"; ctx.font = "bold 11px Inter";
      ctx.fillText(isCurie ? "Curie Law Linear Regime (M ∝ B/T)" : "High-Field Saturation Regime (M → M_s)", plotR.x + 20, plotR.y + plotR.h - 16);
    }
  },

  // 6. Heisenberg Exchange, Ferromagnetism vs Antiferromagnetism & Spin Waves
  "ssp2-exchange-interaction-sim": {
    title: "Heisenberg Exchange Interaction & Spin-Wave Magnon Dispersion",
    desc: "Simulates quantum exchange H = -2J_ex ∑ S_i · S_j. Real-time dynamic lattice rendering of precessing spin vectors for ferromagnetic (J > 0) and antiferromagnetic (J < 0) orders and magnon dispersion ħω(k).",
    isAnimated: true,
    controls: [
      { id: "exchangeJ", label: "Exchange Coupling J_ex (meV)", min: -8.0, max: 8.0, step: 0.5, value: 4.0 },
      { id: "spinWaveK", label: "Magnon Wavenumber ka / π", min: 0.05, max: 1.0, step: 0.05, value: 0.3 },
      { id: "animSpeed", label: "Precession Frequency", min: 0.5, max: 3.0, step: 0.5, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Jex = vals.exchangeJ !== undefined ? vals.exchangeJ : 4.0;
      const ka = (vals.spinWaveK !== undefined ? vals.spinWaveK : 0.3) * Math.PI;
      const speed = vals.animSpeed !== undefined ? vals.animSpeed : 1.5;

      const isFerro = Jex >= 0;
      const S = 1.0;
      // Magnon energy: Ferromagnet ħω = 4J S (1 - cos ka); Antiferromagnet ħω = 4|J| S |sin ka|
      const omega_FM = 4 * Math.abs(Jex) * S * (1 - Math.cos(ka));
      const omega_AFM = 4 * Math.abs(Jex) * S * Math.abs(Math.sin(ka));
      const omega = isFerro ? omega_FM : omega_AFM;

      // Split canvas: Top = Animated 1D Spin Lattice; Bottom = Magnon Dispersion ħω(k)
      const topH = Math.floor(h * 0.52);
      const botH = h - topH - 45;

      // --- TOP: DYNAMIC SPIN VECTOR LATTICE ---
      const topBox = { x: 35, y: 30, w: w - 70, h: topH - 40 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(topBox.x, topBox.y, topBox.w, topBox.h);

      ctx.fillStyle = isFerro ? "#38bdf8" : "#f43f5e"; ctx.font = "bold 12px Inter";
      ctx.fillText(isFerro ? `Ferromagnetic Spin Chain (J_ex = +${Jex.toFixed(1)} meV) - Transverse Spin Wave` : `Antiferromagnetic Néel Chain (J_ex = ${Jex.toFixed(1)} meV) - Alternating Precession`, topBox.x, topBox.y - 10);

      const numSpins = 18;
      const spinSpacing = topBox.w / (numSpins + 1);
      const spinBaseY = topBox.y + topBox.h * 0.55;

      // Draw crystal substrate line
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(topBox.x + 15, spinBaseY); ctx.lineTo(topBox.x + topBox.w - 15, spinBaseY); ctx.stroke();

      const spinLen = 38;
      const tPhase = time * speed * 3.0;

      for (let i = 0; i < numSpins; i++) {
        const sx = topBox.x + (i + 1) * spinSpacing;
        // Spin angle for FM vs AFM
        let baseAngle = isFerro ? -Math.PI / 2 : (i % 2 === 0 ? -Math.PI / 2 : Math.PI / 2);
        // Transverse spin wave perturbation
        const wavePhase = i * ka - tPhase;
        const pertTheta = 0.35 * Math.sin(wavePhase);
        const pertPhi = 0.35 * Math.cos(wavePhase);

        const tipX = sx + spinLen * Math.sin(pertTheta);
        const tipY = spinBaseY + (isFerro ? -spinLen * Math.cos(pertTheta) : (i % 2 === 0 ? -spinLen * Math.cos(pertTheta) : spinLen * Math.cos(pertTheta)));

        // Precession cone ellipse
        ctx.strokeStyle = "rgba(100, 116, 139, 0.4)"; ctx.lineWidth = 0.8;
        ctx.beginPath();
        const coneCenterY = isFerro ? spinBaseY - spinLen * 0.95 : (i % 2 === 0 ? spinBaseY - spinLen * 0.95 : spinBaseY + spinLen * 0.95);
        ctx.ellipse(sx, coneCenterY, spinLen * 0.35, spinLen * 0.12, 0, 0, 2 * Math.PI);
        ctx.stroke();

        // Spin Arrow
        ctx.beginPath(); ctx.moveTo(sx, spinBaseY); ctx.lineTo(tipX, tipY);
        ctx.strokeStyle = isFerro ? "#38bdf8" : (i % 2 === 0 ? "#10b981" : "#f43f5e");
        ctx.lineWidth = 3.0; ctx.stroke();

        // Arrow head
        ctx.beginPath(); ctx.arc(tipX, tipY, 4, 0, 2 * Math.PI);
        ctx.fillStyle = "#ffffff"; ctx.fill();

        // Lattice site atom
        ctx.beginPath(); ctx.arc(sx, spinBaseY, 3, 0, 2 * Math.PI);
        ctx.fillStyle = "#94a3b8"; ctx.fill();
      }

      // --- BOTTOM: MAGNON DISPERSION ħω(k) ---
      const botBox = { x: 35, y: topH + 15, w: w - 70, h: botH };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(botBox.x, botBox.y, botBox.w, botBox.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText(isFerro ? "Ferromagnetic Magnon Dispersion: ħω(k) = 4JS(1 - cos ka) ∝ k² (Near k=0)" : "Antiferromagnetic Magnon Dispersion: ħω(k) = 4|J|S |sin ka| ∝ k (Acoustic-like)", botBox.x, botBox.y - 8);

      const maxDispE = 8 * Math.abs(Jex) * S + 1.0;

      // Plot curve
      ctx.beginPath(); ctx.strokeStyle = isFerro ? "#38bdf8" : "#f43f5e"; ctx.lineWidth = 2.4;
      const dSteps = 60;
      for (let i = 0; i <= dSteps; i++) {
        const curK = (i / dSteps) * Math.PI;
        const eVal = isFerro ? 4 * Math.abs(Jex) * S * (1 - Math.cos(curK)) : 4 * Math.abs(Jex) * S * Math.abs(Math.sin(curK));
        const px = botBox.x + (curK / Math.PI) * botBox.w;
        const py = botBox.y + botBox.h - (eVal / maxDispE) * (botBox.h * 0.85) - 10;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current wavenumber marker
      const curPx = botBox.x + (ka / Math.PI) * botBox.w;
      const curPy = botBox.y + botBox.h - (omega / maxDispE) * (botBox.h * 0.85) - 10;
      ctx.beginPath(); ctx.arc(curPx, curPy, 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#10b981"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      // Labels
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("k = 0", botBox.x + 5, botBox.y + botBox.h - 5);
      ctx.fillText("k = π/a (Zone Boundary)", botBox.x + botBox.w - 130, botBox.y + botBox.h - 5);

      // Readout
      ctx.fillStyle = "#f1f5f9"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Mode: ${isFerro ? "FERROMAGNET" : "ANTIFERROMAGNET"} | ħω(k) = ${omega.toFixed(2)} meV | ka = ${(ka/Math.PI).toFixed(2)}π`, botBox.x + 15, botBox.y + 22);
    }
  },

  // =========================================================================
  // UNIT 4: MAGNETIC ORDERING, DOMAINS & RESONANCE
  // =========================================================================

  // 7. Weiss Mean-Field Theory & Ferromagnetic Hysteresis M(H) Loop
  "ssp2-weiss-hysteresis-sim": {
    title: "Weiss Mean Field, Domain Wall Dynamics & Hysteresis M(H) Loop",
    desc: "Simulates ferromagnetic hysteresis M(H) and spontaneous magnetization M_s(T). Displays remanence M_r, coercive field H_c, domain wall pinning centers, and Barkhausen jumps.",
    isAnimated: true,
    controls: [
      { id: "appliedH", label: "Applied Field H (Oe)", min: -250, max: 250, step: 5, value: 50 },
      { id: "coercivity", label: "Coercivity H_c (Oe)", min: 20, max: 120, step: 5, value: 60 },
      { id: "tempRatio", label: "Temperature T / T_c", min: 0.1, max: 1.2, step: 0.05, value: 0.4 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const H = vals.appliedH !== undefined ? vals.appliedH : 50;
      const Hc = vals.coercivity !== undefined ? vals.coercivity : 60;
      const T_Tc = vals.tempRatio !== undefined ? vals.tempRatio : 0.4;

      // Spontaneous magnetization Ms(T) via Weiss mean-field: Ms(T) / Ms(0) ≈ sqrt(3 * (1 - T/Tc)) for T < Tc, 0 for T >= Tc
      const Ms0 = 1.0;
      const Ms = T_Tc < 1.0 ? Ms0 * Math.min(1.0, Math.sqrt(Math.max(0, 3 * (1 - T_Tc)))) : 0.0;

      // Remanence Mr
      const Mr = Ms * 0.75;

      // Compute current M(H) along hysteresis branch
      // Model classic Jiles-Atherton / tanh hysteresis loop:
      const H_norm = H / Hc;
      let M_curr = 0;
      if (Ms > 0) {
        // Upper or lower branch depending on sign of H with coercive offset
        const effH = H - Math.sign(H) * (Hc * 0.5);
        M_curr = Ms * Math.tanh((H + (H >= 0 ? -Hc * 0.6 : Hc * 0.6)) / (Hc * 0.8));
      }

      // Split canvas: Left = M(H) Loop; Right = Microscopic Magnetic Domains
      const splitX = Math.floor(w * 0.52);

      // --- LEFT: HYSTERESIS LOOP ---
      const plotL = { x: 45, y: 35, w: splitX - 65, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Ferromagnetic Hysteresis Loop M(H) & Weiss Field", plotL.x, plotL.y - 12);

      // Coordinate axes
      const midX = plotL.x + plotL.w * 0.5;
      const midY = plotL.y + plotL.h * 0.5;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(plotL.x, midY); ctx.lineTo(plotL.x + plotL.w, midY); // H axis
      ctx.moveTo(midX, plotL.y); ctx.lineTo(midX, plotL.y + plotL.h); // M axis
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("+H", plotL.x + plotL.w - 18, midY - 6);
      ctx.fillText("-H", plotL.x + 6, midY - 6);
      ctx.fillText("+M_s", midX + 6, plotL.y + 14);
      ctx.fillText("-M_s", midX + 6, plotL.y + plotL.h - 8);

      const maxH = 260;

      // Draw Hysteresis Loop Curves if below Tc
      if (Ms > 0) {
        // Ascending branch (lower)
        ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.0;
        for (let hval = -maxH; hval <= maxH; hval += 5) {
          const mval = Ms * Math.tanh((hval - Hc * 0.65) / (Hc * 0.75));
          const px = midX + (hval / maxH) * (plotL.w * 0.48);
          const py = midY - (mval / 1.1) * (plotL.h * 0.45);
          if (hval === -maxH) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Descending branch (upper)
        ctx.beginPath();
        for (let hval = maxH; hval >= -maxH; hval -= 5) {
          const mval = Ms * Math.tanh((hval + Hc * 0.65) / (Hc * 0.75));
          const px = midX + (hval / maxH) * (plotL.w * 0.48);
          const py = midY - (mval / 1.1) * (plotL.h * 0.45);
          if (hval === maxH) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Current state marker
        const curPx = midX + (H / maxH) * (plotL.w * 0.48);
        const curPy = midY - (M_curr / 1.1) * (plotL.h * 0.45);
        ctx.beginPath(); ctx.arc(curPx, curPy, 6, 0, 2 * Math.PI);
        ctx.fillStyle = "#10b981"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();
      } else {
        // Paramagnetic linear response M = chi * H
        ctx.beginPath(); ctx.strokeStyle = "#64748b"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.8;
        ctx.moveTo(midX - plotL.w * 0.45, midY + plotL.h * 0.2);
        ctx.lineTo(midX + plotL.w * 0.45, midY - plotL.h * 0.2);
        ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = "#ef4444"; ctx.font = "bold 11px Inter";
        ctx.fillText("PARAMAGNETIC PHASE (T ≥ T_c): Zero Hysteresis", plotL.x + 30, midY - 30);
      }

      // --- RIGHT: 2D MAGNETIC DOMAINS & WALL DISPLACEMENT ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
      ctx.fillText("Magnetic Domains & 180° Bloch Wall Motion", plotR.x, plotR.y - 12);

      // Domain window inside plotR
      const domX = plotR.x + 20, domY = plotR.y + 25, domW = plotR.w - 40, domH = plotR.h * 0.55;
      ctx.fillStyle = "#090d16"; ctx.fillRect(domX, domY, domW, domH);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(domX, domY, domW, domH);

      // Domain wall position shifts with H
      const wallShift = Ms > 0 ? (M_curr / Ms) * (domW * 0.35) : 0;
      const wall1X = domX + domW * 0.33 + wallShift;
      const wall2X = domX + domW * 0.66 + wallShift * 0.8;

      // Fill Domains with opposite spin orientations
      // Domain 1: UP (blue)
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.fillRect(domX, domY, Math.max(0, wall1X - domX), domH);
      // Domain 2: DOWN (red)
      ctx.fillStyle = "rgba(244, 63, 94, 0.15)";
      ctx.fillRect(wall1X, domY, Math.max(0, wall2X - wall1X), domH);
      // Domain 3: UP (blue)
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.fillRect(wall2X, domY, Math.max(0, domX + domW - wall2X), domH);

      // Domain wall lines
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      [wall1X, wall2X].forEach(wx => {
        if (wx >= domX && wx <= domX + domW) {
          ctx.beginPath(); ctx.moveTo(wx, domY); ctx.lineTo(wx, domY + domH); ctx.stroke();
        }
      });

      // Domain arrows
      function drawArrow(ax, ay, isUp) {
        ctx.strokeStyle = isUp ? "#38bdf8" : "#f43f5e"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(ax, isUp ? ay + 14 : ay - 14);
        ctx.lineTo(ax, isUp ? ay - 14 : ay + 14);
        ctx.stroke();
        // Head
        ctx.beginPath();
        if (isUp) {
          ctx.moveTo(ax - 5, ay - 6); ctx.lineTo(ax, ay - 14); ctx.lineTo(ax + 5, ay - 6);
        } else {
          ctx.moveTo(ax - 5, ay + 6); ctx.lineTo(ax, ay + 14); ctx.lineTo(ax + 5, ay + 6);
        }
        ctx.stroke();
      }

      const d1Mid = domX + (wall1X - domX) * 0.5;
      const d2Mid = wall1X + (wall2X - wall1X) * 0.5;
      const d3Mid = wall2X + (domX + domW - wall2X) * 0.5;
      if (d1Mid > domX && d1Mid < domX + domW) drawArrow(d1Mid, domY + domH * 0.5, true);
      if (d2Mid > domX && d2Mid < domX + domW) drawArrow(d2Mid, domY + domH * 0.5, false);
      if (d3Mid > domX && d3Mid < domX + domW) drawArrow(d3Mid, domY + domH * 0.5, true);

      // Telemetry Panel
      const teleY = domY + domH + 15;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(domX, teleY, domW, plotR.h - domH - 30);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(domX, teleY, domW, plotR.h - domH - 30);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Applied Field H = ${H} Oe  |  Coercivity H_c = ${Hc} Oe`, domX + 15, teleY + 20);
      ctx.fillText(`Saturation M_s = ${Ms.toFixed(2)} M_0  |  Remanence M_r = ${Mr.toFixed(2)} M_0`, domX + 15, teleY + 38);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Net Magnetization M = ${M_curr.toFixed(3)} M_0`, domX + 15, teleY + 56);
    }
  },

  // 8. Antiferromagnetic Susceptibility & Spin-Flop Resonance (AFMR)
  "ssp2-antiferro-resonance-sim": {
    title: "Antiferromagnetic Susceptibility χ(T), Spin-Flop & AFMR Modes",
    desc: "Two-sublattice Néel model. Computes parallel χ_||(T) and perpendicular χ_⊥(T) magnetic susceptibilities, spin-flop phase transition field H_sf = √(2 H_E H_A), and Kittel AFMR modes.",
    isAnimated: true,
    controls: [
      { id: "neelTemp", label: "Reduced Temp T / T_N", min: 0.05, max: 2.0, step: 0.05, value: 0.5 },
      { id: "appliedField", label: "Applied Field H₀ (Tesla)", min: 0.0, max: 12.0, step: 0.5, value: 3.0 },
      { id: "anisotropyField", label: "Anisotropy Field H_A (T)", min: 0.5, max: 4.0, step: 0.25, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const tRatio = vals.neelTemp !== undefined ? vals.neelTemp : 0.5;
      const H0 = vals.appliedField !== undefined ? vals.appliedField : 3.0;
      const HA = vals.anisotropyField !== undefined ? vals.anisotropyField : 1.5;
      const HE = 30.0; // Exchange field HE = 30 T

      // Spin flop critical field: H_sf = sqrt(2 * HE * HA - HA^2) ≈ sqrt(2 * HE * HA)
      const Hsf = Math.sqrt(2 * HE * HA - HA * HA);
      const isSpinFlop = H0 >= Hsf;

      // Antiferromagnetic Resonance Frequency modes (Kittel):
      // omega_pm / gamma = sqrt(2 * HE * HA + HA^2) ± H0
      const gamma_GHz = 28.0; // GHz/T
      const wZero = Math.sqrt(2 * HE * HA + HA * HA);
      const wModePlus = (wZero + H0) * gamma_GHz;
      const wModeMinus = Math.max(0, (wZero - H0) * gamma_GHz);

      // Susceptibility curves:
      // T < TN: chi_perp is constant = C / (2*TN); chi_parallel drops from chi_perp down to 0 at T=0
      // T >= TN: Curie-Weiss law chi = C / (T + theta_p)
      const chiPerp = 1.0;
      const chiPara = tRatio < 1.0 ? Math.pow(tRatio, 1.6) * chiPerp : chiPerp / (0.5 + 0.5 * tRatio);

      // Split canvas: Left = Chi(T) plot; Right = Sublattice Precession & Spin-Flop
      const splitX = Math.floor(w * 0.52);

      // --- LEFT: SUSCEPTIBILITY PLOT ---
      const plotL = { x: 45, y: 35, w: splitX - 65, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Magnetic Susceptibility: χ_⊥(T) vs χ_∥(T)", plotL.x, plotL.y - 12);

      // Néel Temp line
      const tnX = plotL.x + (1.0 / 2.0) * plotL.w;
      ctx.strokeStyle = "#475569"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(tnX, plotL.y); ctx.lineTo(tnX, plotL.y + plotL.h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter"; ctx.fillText("T = T_N", tnX - 16, plotL.y + 16);

      // Plot chi_perp (horizontal below TN, drops above)
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.2;
      for (let i = 0; i <= 60; i++) {
        const tr = (i / 60) * 2.0;
        const cVal = tr <= 1.0 ? chiPerp : chiPerp / (0.5 + 0.5 * tr);
        const px = plotL.x + (tr / 2.0) * plotL.w;
        const py = plotL.y + plotL.h - (cVal / 1.3) * (plotL.h * 0.8) - 15;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot chi_parallel (freezes to 0 below TN)
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.2;
      for (let i = 0; i <= 60; i++) {
        const tr = (i / 60) * 2.0;
        const cVal = tr <= 1.0 ? Math.pow(tr, 1.6) * chiPerp : chiPerp / (0.5 + 0.5 * tr);
        const px = plotL.x + (tr / 2.0) * plotL.w;
        const py = plotL.y + plotL.h - (cVal / 1.3) * (plotL.h * 0.8) - 15;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current operational marker
      const curPx = plotL.x + (tRatio / 2.0) * plotL.w;
      const curPy = plotL.y + plotL.h - (chiPara / 1.3) * (plotL.h * 0.8) - 15;
      ctx.beginPath(); ctx.arc(curPx, curPy, 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#ef4444"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      // Legend
      ctx.fillStyle = "#10b981"; ctx.fillRect(plotL.x + 15, plotL.y + plotL.h - 45, 12, 3);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter"; ctx.fillText("Perpendicular χ_⊥(T)", plotL.x + 32, plotL.y + plotL.h - 42);
      ctx.fillStyle = "#38bdf8"; ctx.fillRect(plotL.x + 15, plotL.y + plotL.h - 25, 12, 3);
      ctx.fillText("Parallel χ_∥(T) (drops to 0)", plotL.x + 32, plotL.y + plotL.h - 22);

      // --- RIGHT: SUBLATTICE MAGNETIZATION & SPIN-FLOP ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = isSpinFlop ? "#f59e0b" : "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText(isSpinFlop ? "SPIN-FLOP STATE (H₀ > H_sf): Spins Perpendicular" : "COLINEAR NÉEL STATE: Sublattices M_A & M_B Anti-Parallel", plotR.x, plotR.y - 12);

      // Render 2 Sublattice Vectors M_A and M_B
      const centerVx = plotR.x + plotR.w * 0.5;
      const centerVy = plotR.y + plotR.h * 0.42;

      // Draw H0 applied field arrow vertically
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.setLineDash([2, 2]);
      ctx.beginPath(); ctx.moveTo(centerVx, centerVy + 70); ctx.lineTo(centerVx, centerVy - 70); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter"; ctx.fillText(`Applied H₀ = ${H0} T`, centerVx + 8, centerVy - 65);

      const vLen = 65;
      let angleA, angleB;
      if (!isSpinFlop) {
        // Colinear precessing under AFMR
        const precPhase = time * 3.0;
        angleA = -Math.PI / 2 + 0.25 * Math.sin(precPhase);
        angleB = Math.PI / 2 + 0.25 * Math.sin(precPhase + Math.PI);
      } else {
        // Spin-flop canted state perpendicular to easy axis
        const cantAngle = Math.asin(Math.min(0.9, H0 / (2 * HE)));
        angleA = -Math.PI + cantAngle;
        angleB = -cantAngle;
      }

      // Vector M_A (blue)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3.5;
      ctx.beginPath(); ctx.moveTo(centerVx, centerVy);
      ctx.lineTo(centerVx + vLen * Math.cos(angleA), centerVy + vLen * Math.sin(angleA));
      ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText("M_A", centerVx + (vLen + 12) * Math.cos(angleA) - 8, centerVy + (vLen + 12) * Math.sin(angleA));

      // Vector M_B (red)
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 3.5;
      ctx.beginPath(); ctx.moveTo(centerVx, centerVy);
      ctx.lineTo(centerVx + vLen * Math.cos(angleB), centerVy + vLen * Math.sin(angleB));
      ctx.stroke();
      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter";
      ctx.fillText("M_B", centerVx + (vLen + 12) * Math.cos(angleB) - 8, centerVy + (vLen + 12) * Math.sin(angleB));

      // Telemetry info panel
      const boxY = plotR.y + plotR.h - 60;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, boxY, plotR.w - 20, 52);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, boxY, plotR.w - 20, 52);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Spin-Flop Field H_sf = ${Hsf.toFixed(2)} T  |  H_E = ${HE} T, H_A = ${HA} T`, plotR.x + 18, boxY + 18);
      ctx.fillText(`AFMR Mode ω⁺ = ${wModePlus.toFixed(1)} GHz  |  ω⁻ = ${wModeMinus.toFixed(1)} GHz`, plotR.x + 18, boxY + 36);
    }
  }
''';

with open("ssp2_sims_p2.js", "w", encoding="utf-8") as f:
    f.write(part2_js)

print("ssp2_sims_p2.js generated! Size:", len(part2_js))
