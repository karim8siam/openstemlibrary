# -*- coding: utf-8 -*-
"""
Builder for Nuclear Physics II Simulations 5 through 8
5. nuc2-yukawa-meson-exchange-sim
6. nuc2-isospin-multiplet-sim
7. nuc2-multipole-selection-sim
8. nuc2-internal-conversion-gdr-sim
"""

sims_5_8 = r'''
  // =========================================================================
  // UNIT 3: FUNDAMENTAL NUCLEAR FORCES & MESON THEORY
  // =========================================================================

  // 5. Yukawa Meson Exchange & One-Boson-Exchange (OBE) Potential
  "nuc2-yukawa-meson-exchange-sim": {
    title: "Yukawa Meson Exchange & One-Boson-Exchange (OBE) Potential",
    desc: "Simulates the NN potential V_NN(r) decomposed into pion exchange (OPEP, long-range tensor attraction), sigma exchange (intermediate scalar attraction), and omega exchange (short-range vector repulsive core).",
    isAnimated: true,
    controls: [
      { id: "pionCutoff", label: "Pion Coupling gπ²/4π", min: 10.0, max: 18.0, step: 0.5, value: 14.4 },
      { id: "sigmaMass", label: "Scalar σ Mass (MeV)", min: 450, max: 650, step: 25, value: 550 },
      { id: "omegaRepulsion", label: "Omega Coupling gω²/4π", min: 15.0, max: 30.0, step: 1.0, value: 20.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const gPi = vals.pionCutoff !== undefined ? vals.pionCutoff : 14.4;
      const mSigma = vals.sigmaMass !== undefined ? vals.sigmaMass : 550;
      const gOmega = vals.omegaRepulsion !== undefined ? vals.omegaRepulsion : 20.0;

      const mPi = 138.0; // MeV
      const mOmega = 782.0; // MeV

      // mu = m * c / hbar in fm^-1
      const muPi = mPi / 197.327; // ~ 0.70 fm^-1
      const muSigma = mSigma / 197.327; // ~ 2.78 fm^-1
      const muOmega = mOmega / 197.327; // ~ 3.96 fm^-1

      const plot = { x: 55, y: 35, w: w - 85, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("One-Boson-Exchange Potential Components: V(r) vs Nucleon Separation r (fm)", plot.x, plot.y - 12);

      // Y-axis spans -120 MeV to +250 MeV
      const yMin = -120, yMax = 250;
      const rMax = 3.0; // fm

      // Draw zero axis line
      const yZero = plot.y + plot.h * (1 - (0 - yMin) / (yMax - yMin));
      ctx.strokeStyle = "#475569"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(plot.x, yZero); ctx.lineTo(plot.x + plot.w, yZero); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("V = 0", plot.x + 5, yZero - 4);

      // Tick marks on r-axis
      for (let r = 0.5; r <= 3.0; r += 0.5) {
        const px = plot.x + (r / rMax) * plot.w;
        ctx.fillText(`${r.toFixed(1)} fm`, px - 12, plot.y + plot.h + 16);
      }

      // Arrays for potential curves
      const ptsPi = [], ptsSig = [], ptsOm = [], ptsTot = [];
      const dr = 0.02;

      for (let r = 0.15; r <= rMax; r += dr) {
        // Yukawa functions
        const vPi = -(gPi * 197.327 * 0.05 / r) * Math.exp(-muPi * r);
        const vSig = -(12.0 * 197.327 * 0.15 / r) * Math.exp(-muSigma * r);
        const vOm = (gOmega * 197.327 * 0.12 / r) * Math.exp(-muOmega * r);
        const vTot = vPi + vSig + vOm;

        const px = plot.x + (r / rMax) * plot.w;
        ptsPi.push({ px, py: plot.y + plot.h * (1 - (vPi - yMin) / (yMax - yMin)) });
        ptsSig.push({ px, py: plot.y + plot.h * (1 - (vSig - yMin) / (yMax - yMin)) });
        ptsOm.push({ px, py: plot.y + plot.h * (1 - (Math.min(vOm, yMax) - yMin) / (yMax - yMin)) });
        ptsTot.push({ px, py: plot.y + plot.h * (1 - (Math.min(vTot, yMax) - yMin) / (yMax - yMin)) });
      }

      // Draw components
      // 1. Pion (dashed green)
      ctx.strokeStyle = "#10b981"; ctx.setLineDash([4, 3]); ctx.lineWidth = 1.5;
      ctx.beginPath();
      ptsPi.forEach((p, i) => { if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py); });
      ctx.stroke();

      // 2. Sigma (dashed cyan)
      ctx.strokeStyle = "#06b6d4"; ctx.setLineDash([4, 3]);
      ctx.beginPath();
      ptsSig.forEach((p, i) => { if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py); });
      ctx.stroke();

      // 3. Omega (dashed red)
      ctx.strokeStyle = "#ef4444"; ctx.setLineDash([4, 3]);
      ctx.beginPath();
      ptsOm.forEach((p, i) => { if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py); });
      ctx.stroke();
      ctx.setLineDash([]);

      // 4. Total OBE Potential (solid amber/gold)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
      ctx.beginPath();
      ptsTot.forEach((p, i) => { if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py); });
      ctx.stroke();

      // Repulsive core highlight (rc ~ 0.45 fm)
      const rc = 0.45;
      const xCore = plot.x + (rc / rMax) * plot.w;
      ctx.fillStyle = "rgba(239, 68, 68, 0.1)";
      ctx.fillRect(plot.x, plot.y, xCore - plot.x, plot.h);
      ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter";
      ctx.fillText("Hard Core rc ≈ 0.4 fm", xCore - 65, plot.y + 40);

      // Legend panel
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
      ctx.fillRect(plot.x + plot.w - 245, plot.y + 15, 235, 105);
      ctx.strokeRect(plot.x + plot.w - 245, plot.y + 15, 235, 105);

      ctx.font = "bold 11px Inter";
      ctx.fillStyle = "#f59e0b"; ctx.fillText("— Total OBE Potential V(r)", plot.x + plot.w - 230, plot.y + 35);
      ctx.fillStyle = "#10b981"; ctx.fillText("--- Pion π Exchange (Long Range, 1-2 fm)", plot.x + plot.w - 230, plot.y + 53);
      ctx.fillStyle = "#06b6d4"; ctx.fillText("--- Sigma σ Exchange (Intermediate Attraction)", plot.x + plot.w - 230, plot.y + 71);
      ctx.fillStyle = "#ef4444"; ctx.fillText("--- Omega ω Exchange (Repulsive Core)", plot.x + plot.w - 230, plot.y + 89);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Well Depth ~ -50 to -70 MeV at r ≈ 0.8 fm", plot.x + plot.w - 230, plot.y + 107);
    }
  },

  // 6. Isospin Multiplets & Clebsch-Gordan Pion-Nucleon Resonances
  "nuc2-isospin-multiplet-sim": {
    title: "Isospin Multiplets & Clebsch-Gordan Pion-Nucleon Resonances",
    desc: "Calculates isospin amplitude decomposition for pion-nucleon scattering (I = 1/2 and I = 3/2). Demonstrates the Delta(1232) resonance cross section ratio 9 : 1 : 2 across the three fundamental charge channels.",
    isAnimated: true,
    controls: [
      { id: "energyDelta", label: "Pion Beam Tπ (MeV)", min: 50, max: 350, step: 10, value: 195 },
      { id: "resonanceWidth", label: "Delta Width Γ (MeV)", min: 80, max: 150, step: 5, value: 115 },
      { id: "deltaMass", label: "Delta Mass MΔ (MeV)", min: 1200, max: 1260, step: 5, value: 1232 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Tpi = vals.energyDelta !== undefined ? vals.energyDelta : 195;
      const Gamma = vals.resonanceWidth !== undefined ? vals.resonanceWidth : 115;
      const MDelta = vals.deltaMass !== undefined ? vals.deltaMass : 1232;

      const splitX = Math.floor(w * 0.54);

      // LEFT PLOT: Breit-Wigner Cross Section Curves vs Pion Kinetic Energy (50 to 350 MeV)
      const pL = { x: 50, y: 35, w: splitX - 65, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Δ(1232) Isospin Resonances: σ(Tπ) across 3 Channels", pL.x, pL.y - 12);

      const tMin = 50, tMax = 350;
      const sigMax = 220; // mb

      // Resonance peak occurs around Tpi ~ 195 MeV (sqrt(s) = 1232 MeV)
      const tRes = 195.0;

      function getSigma(t, factor) {
        const den = Math.pow(t - tRes, 2) + Math.pow(Gamma / 2, 2);
        return factor * 200.0 * Math.pow(Gamma / 2, 2) / den;
      }

      // Draw Channel 1: π+ + p -> π+ + p (I = 3/2 pure, factor 1.0)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let t = tMin; t <= tMax; t += 2) {
        const sig = getSigma(t, 1.0);
        const px = pL.x + ((t - tMin) / (tMax - tMin)) * pL.w;
        const py = pL.y + pL.h * (1 - sig / sigMax);
        if (t === tMin) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Draw Channel 2: π- + p -> π- + p (factor 1/9)
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2; ctx.beginPath();
      for (let t = tMin; t <= tMax; t += 2) {
        const sig = getSigma(t, 1.0 / 9.0);
        const px = pL.x + ((t - tMin) / (tMax - tMin)) * pL.w;
        const py = pL.y + pL.h * (1 - sig / sigMax);
        if (t === tMin) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Draw Channel 3: π- + p -> π0 + n (Charge Exchange, factor 2/9)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.beginPath();
      for (let t = tMin; t <= tMax; t += 2) {
        const sig = getSigma(t, 2.0 / 9.0);
        const px = pL.x + ((t - tMin) / (tMax - tMin)) * pL.w;
        const py = pL.y + pL.h * (1 - sig / sigMax);
        if (t === tMin) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Operating marker on Channel 1
      const curSig1 = getSigma(Tpi, 1.0);
      const curSig2 = getSigma(Tpi, 1.0 / 9.0);
      const curSig3 = getSigma(Tpi, 2.0 / 9.0);
      const curX = pL.x + ((Tpi - tMin) / (tMax - tMin)) * pL.w;
      const curY = pL.y + pL.h * (1 - curSig1 / sigMax);
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(curX, curY, 5, 0, 2*Math.PI); ctx.fill();

      // RIGHT PANEL: Clebsch-Gordan Weight Ratios (9 : 1 : 2)
      const pR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 75 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pR.x, pR.y, pR.w, pR.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Clebsch-Gordan Isospin Ratio", pR.x + 15, pR.y + 22);

      // Bar Chart for the three channels
      const barW = 45;
      const maxSig = 200;
      const h1 = (curSig1 / maxSig) * (pR.h - 90);
      const h2 = (curSig2 / maxSig) * (pR.h - 90);
      const h3 = (curSig3 / maxSig) * (pR.h - 90);

      // Bar 1: π+ p
      ctx.fillStyle = "#38bdf8";
      ctx.fillRect(pR.x + 30, pR.y + pR.h - 40 - h1, barW, h1);
      ctx.fillStyle = "#ffffff"; ctx.font = "10px Inter";
      ctx.fillText(`${curSig1.toFixed(1)} mb`, pR.x + 32, pR.y + pR.h - 45 - h1);
      ctx.fillText("π+ p (9)", pR.x + 32, pR.y + pR.h - 22);

      // Bar 2: π- p (Elastic)
      ctx.fillStyle = "#f43f5e";
      ctx.fillRect(pR.x + 100, pR.y + pR.h - 40 - h2, barW, h2);
      ctx.fillText(`${curSig2.toFixed(1)} mb`, pR.x + 102, pR.y + pR.h - 45 - h2);
      ctx.fillText("π- p (1)", pR.x + 102, pR.y + pR.h - 22);

      // Bar 3: π- p -> π0 n (CEX)
      ctx.fillStyle = "#f59e0b";
      ctx.fillRect(pR.x + 170, pR.y + pR.h - 40 - h3, barW, h3);
      ctx.fillText(`${curSig3.toFixed(1)} mb`, pR.x + 172, pR.y + pR.h - 45 - h3);
      ctx.fillText("CEX (2)", pR.x + 175, pR.y + pR.h - 22);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText("Exact CG Ratio at Peak = 9 : 1 : 2", pR.x + 35, pR.y + 55);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Since Δ(1232) is pure I = 3/2, the", pR.x + 35, pR.y + 72);
      ctx.fillText("isospin Clebsch-Gordan coefficients", pR.x + 35, pR.y + 86);
      ctx.fillText("dictate the relative branching matrix!", pR.x + 35, pR.y + 100);
    }
  },

  // =========================================================================
  // UNIT 4: ELECTROMAGNETIC TRANSITIONS & SELECTION RULES
  // =========================================================================

  // 7. Multipole Selection Rules & Weisskopf Single-Particle Decay Rates
  "nuc2-multipole-selection-sim": {
    title: "Multipole Selection Rules & Weisskopf Single-Particle Rates",
    desc: "Evaluates allowed electric Eλ and magnetic Mλ multipole transition modes between initial and final nuclear states (Ii^πi -> If^πf), calculating Weisskopf single-particle transition rates T_W and branching ratios.",
    isAnimated: true,
    controls: [
      { id: "massA", label: "Mass Number A", min: 12, max: 240, step: 4, value: 60 },
      { id: "gammaEnergy", label: "Gamma Energy (MeV)", min: 0.1, max: 4.0, step: 0.1, value: 1.33 },
      { id: "spinInitial", label: "Initial Spin Ii", min: 0, max: 6, step: 1, value: 2 },
      { id: "spinFinal", label: "Final Spin If", min: 0, max: 6, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const A = vals.massA !== undefined ? vals.massA : 60;
      const Eg = vals.gammaEnergy !== undefined ? vals.gammaEnergy : 1.33;
      const Ii = vals.spinInitial !== undefined ? vals.spinInitial : 2;
      const If = vals.spinFinal !== undefined ? vals.spinFinal : 0;

      // Triangle inequality: |Ii - If| <= lambda <= Ii + If (lambda >= 1 for photons)
      const lMin = Math.max(1, Math.abs(Ii - If));
      const lMax = Math.max(lMin, Ii + If);

      const pL = { x: 35, y: 35, w: w * 0.45, h: h - 70 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pL.x, pL.y, pL.w, pL.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText(`Selection Rules for ${Ii} → ${If} Transition`, pL.x + 15, pL.y + 24);

      // Assume parity change: pi_i = +1, pi_f = +1 (Delta pi = no)
      // Allowed modes
      const modes = [];
      for (let L = lMin; L <= Math.min(lMax, 5); L++) {
        // Parity rules: E_L has pi = (-1)^L; M_L has pi = (-1)^(L+1)
        // If parity does not change, E_even and M_odd are allowed
        if (L % 2 === 0) modes.push({ type: "E", L, parity: "yes" });
        if (L % 2 === 1) modes.push({ type: "M", L, parity: "yes" });
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Angular Momentum Range: ${lMin} ≤ λ ≤ ${lMax}`, pL.x + 15, pL.y + 50);
      ctx.fillText(`Photons have S=1, so λ=0 (E0) strictly cannot emit γ.`, pL.x + 15, pL.y + 70);

      // Display allowed multipole modes
      let curY = pL.y + 105;
      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
      ctx.fillText("Allowed Radiation Multipoles:", pL.x + 15, curY);
      curY += 22;

      modes.forEach((m, idx) => {
        const isLowest = idx === 0;
        ctx.fillStyle = isLowest ? "#38bdf8" : "#94a3b8";
        ctx.font = isLowest ? "bold 12px Inter" : "11px Inter";
        ctx.fillText(`• ${m.type}${m.L} (${m.type === "E" ? "Electric" : "Magnetic"} ${m.L === 1 ? "Dipole" : m.L === 2 ? "Quadrupole" : m.L === 3 ? "Octupole" : "Hexadecapole"}) ${isLowest ? "★ DOMINANT" : ""}`, pL.x + 20, curY);
        curY += 20;
      });

      // RIGHT PANEL: Weisskopf Single Particle Transition Rates
      const pR = { x: w * 0.52, y: 35, w: w * 0.44, h: h - 70 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pR.x, pR.y, pR.w, pR.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Weisskopf Single-Particle Rates Tw (s⁻¹)", pR.x + 15, pR.y + 24);

      // Formulas (in s^-1):
      // T_W(E1) = 1.0e14 * A^(2/3) * Eg^3
      // T_W(M1) = 3.1e13 * Eg^3
      // T_W(E2) = 7.3e7 * A^(4/3) * Eg^5
      // T_W(M2) = 2.2e7 * A^(2/3) * Eg^5
      const TwE1 = 1.0e14 * Math.pow(A, 2/3) * Math.pow(Eg, 3);
      const TwM1 = 3.1e13 * Math.pow(Eg, 3);
      const TwE2 = 7.3e7 * Math.pow(A, 4/3) * Math.pow(Eg, 5);
      const TwM2 = 2.2e7 * Math.pow(A, 2/3) * Math.pow(Eg, 5);

      const rates = [
        { name: "E1", val: TwE1 },
        { name: "M1", val: TwM1 },
        { name: "E2", val: TwE2 },
        { name: "M2", val: TwM2 }
      ];

      curY = pR.y + 60;
      rates.forEach(r => {
        ctx.fillStyle = "#f59e0b"; ctx.font = "bold 11px Inter";
        ctx.fillText(`${r.name}:`, pR.x + 15, curY);
        ctx.fillStyle = "#ffffff"; ctx.font = "11px Inter";
        ctx.fillText(`${r.val.toExponential(2)} s⁻¹`, pR.x + 50, curY);

        const halfLife = (0.693 / r.val);
        ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
        ctx.fillText(`(T½ ≈ ${halfLife < 1e-12 ? (halfLife*1e15).toFixed(1) + " fs" : halfLife < 1e-6 ? (halfLife*1e12).toFixed(1) + " ps" : (halfLife*1e9).toFixed(1) + " ns"})`, pR.x + 175, curY);
        curY += 32;
      });

      // Bottom highlight
      ctx.fillStyle = "#ec4899"; ctx.font = "11px Inter";
      ctx.fillText(`Notice: Each multipole order λ increase suppresses`, pR.x + 15, pR.y + pR.h - 35);
      ctx.fillText(`the rate by ~10⁵ to 10⁶!`, pR.x + 15, pR.y + pR.h - 18);
    }
  },

  // 8. Internal Conversion Coefficients & Giant Dipole Resonance (GDR)
  "nuc2-internal-conversion-gdr-sim": {
    title: "Internal Conversion Coefficients & Giant Dipole Resonance (GDR)",
    desc: "Dual-mode electromagnetic simulator: (1) Internal conversion coefficient α_K vs transition energy Eγ and Z; (2) Collective Giant Dipole Resonance (GDR) cross section with prolate deformation splitting.",
    isAnimated: true,
    controls: [
      { id: "atomicZ", label: "Atomic Number Z", min: 20, max: 92, step: 2, value: 74 },
      { id: "deformationBeta", label: "Deformation β2", min: 0.0, max: 0.40, step: 0.05, value: 0.28 },
      { id: "gdrDamping", label: "GDR Width Γ (MeV)", min: 3.0, max: 8.0, step: 0.5, value: 4.8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Z = vals.atomicZ !== undefined ? vals.atomicZ : 74;
      const beta = vals.deformationBeta !== undefined ? vals.deformationBeta : 0.28;
      const Gamma = vals.gdrDamping !== undefined ? vals.gdrDamping : 4.8;

      const splitX = Math.floor(w * 0.52);

      // LEFT PLOT: Internal Conversion Coefficient alpha_K vs E_gamma (0.05 to 1.5 MeV)
      const pL = { x: 50, y: 35, w: splitX - 65, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Internal Conversion Coefficient αK vs Eγ (MeV)", pL.x, pL.y - 12);

      // Plot alpha_K ~ Z^3 / E_gamma^(7/2)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.beginPath();
      const egMin = 0.08, egMax = 1.2;
      for (let eg = egMin; eg <= egMax; eg += 0.02) {
        // Log plot: log10(alpha_K) from -3 to +2
        const alphaK = 1.2e-4 * Math.pow(Z / 74, 3) / Math.pow(eg, 3.5);
        const logAlpha = Math.log10(Math.max(1e-4, Math.min(100, alphaK)));
        const px = pL.x + ((eg - egMin) / (egMax - egMin)) * pL.w;
        const py = pL.y + pL.h * (1 - (logAlpha - (-3)) / (2 - (-3)));
        if (eg === egMin) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("10²", pL.x - 22, pL.y + 12);
      ctx.fillText("10⁰", pL.x - 22, pL.y + pL.h * 0.4);
      ctx.fillText("10⁻²", pL.x - 26, pL.y + pL.h * 0.8);
      ctx.fillText("Eγ (MeV) →", pL.x + pL.w - 55, pL.y + pL.h + 16);

      // RIGHT PLOT: Giant Dipole Resonance (GDR) Lorentzian Cross Section with Deformation Splitting
      const pR = { x: splitX + 35, y: 35, w: w - splitX - 55, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("GDR Lorentzian Cross Section σ(Eγ) [Deformation Split]", pR.x, pL.y - 12);

      // Goldhaber-Teller / Steinwedel-Jensen GDR centroid energy: E0 ~ 79 * A^(-1/3) ~ 15 MeV
      const A = Math.round(Z * 2.5);
      const E0 = 79.0 * Math.pow(A, -1/3);
      // Splitting for prolate nucleus: E_a = E0(1 - 0.66 beta), E_b = E0(1 + 0.33 beta)
      const E_a = E0 * (1.0 - 0.66 * beta);
      const E_b = E0 * (1.0 + 0.33 * beta);

      const eGdrMin = 8.0, eGdrMax = 22.0;
      const sigGdrMax = 350; // mb

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let eg = eGdrMin; eg <= eGdrMax; eg += 0.2) {
        // Double Lorentzian
        const L_a = (1/3) * (250 * Math.pow(eg * Gamma, 2)) / (Math.pow(eg*eg - E_a*E_a, 2) + Math.pow(eg * Gamma, 2));
        const L_b = (2/3) * (250 * Math.pow(eg * Gamma, 2)) / (Math.pow(eg*eg - E_b*E_b, 2) + Math.pow(eg * Gamma, 2));
        const sigGDR = L_a + L_b;
        const px = pR.x + ((eg - eGdrMin) / (eGdrMax - eGdrMin)) * pR.w;
        const py = pR.y + pR.h * (1 - sigGDR / sigGdrMax);
        if (eg === eGdrMin) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Readouts
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Z = ${Z} (αK ∝ Z³)`, pL.x, h - 15);
      ctx.fillText(`E0 = ${E0.toFixed(1)} MeV | Peak Split: Ea = ${E_a.toFixed(1)}, Eb = ${E_b.toFixed(1)} MeV`, pR.x, h - 15);
    }
  },
'''
