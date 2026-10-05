import json

part4_js = r'''
  // =========================================================================
  // UNIT 7: OPTICAL PROPERTIES, EXCITONS & CRYSTAL DEFECTS
  // =========================================================================

  // 13. Exciton States & Optical Absorption Spectrum
  "ssp2-exciton-optical-sim": {
    title: "Wannier-Mott vs Frenkel Excitons & Optical Absorption α(ħω)",
    desc: "Rigorous excitonic bound state solver. Calculates effective Rydberg energy R_y*, Bohr orbit radius a_exc = a₀ ε_r / (μ/m₀), and sub-bandgap hydrogenic absorption peaks below the fundamental bandgap E_g.",
    isAnimated: true,
    controls: [
      { id: "excType", label: "Exciton Regime", min: 0, max: 1, step: 1, value: 0 }, // 0: Wannier-Mott (semiconductor), 1: Frenkel (molecular/insulator)
      { id: "dielEps", label: "Dielectric Constant ε_r", min: 2.5, max: 16.0, step: 0.5, value: 11.9 },
      { id: "massMu", label: "Reduced Mass μ / m₀", min: 0.05, max: 0.40, step: 0.02, value: 0.12 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const isWannier = (vals.excType === undefined || Math.round(vals.excType) === 0);
      const epsR = vals.dielEps !== undefined ? vals.dielEps : 11.9;
      const mu = vals.massMu !== undefined ? vals.massMu : 0.12;

      const a0_A = 0.529; // Bohr radius in Angstroms
      const Ry_eV = 13.606; // Rydberg in eV
      const Eg = 1.50; // Fundamental gap in eV (e.g. GaAs-like)

      // Exciton parameters
      const a_exc = isWannier ? a0_A * epsR / mu : 1.2; // in Angstroms
      const Ry_star = isWannier ? (Ry_eV * mu / (epsR * epsR)) : 0.85; // in eV
      const E_b1 = Eg - Ry_star; // n=1 ground state

      // Split canvas: Left is Exciton Orbit vs Lattice; Right is Optical Absorption α(ħω)
      const splitX = Math.floor(w * 0.48);

      // --- LEFT PLOT: BOHR ORBIT & LATTICE COMPARISON ---
      const plotL = { x: 35, y: 35, w: splitX - 55, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText(isWannier ? `Wannier-Mott Exciton: Delocalized Orbit (a_exc ≫ a)` : `Frenkel Exciton: Tightly Bound on Single Cell`, plotL.x, plotL.y - 12);

      const latA_px = 30; // Lattice spacing in px
      const cx = plotL.x + plotL.w * 0.5;
      const cy = plotL.y + plotL.h * 0.48;

      // Draw crystal lattice ions
      for (let lx = plotL.x + 20; lx < plotL.x + plotL.w - 10; lx += latA_px) {
        for (let ly = plotL.y + 25; ly < plotL.y + plotL.h - 15; ly += latA_px) {
          ctx.beginPath(); ctx.arc(lx, ly, 2, 0, 2 * Math.PI);
          ctx.fillStyle = "#334155"; ctx.fill();
        }
      }

      // Draw Exciton Orbit
      const orbitRadPx = isWannier ? Math.min(105, (a_exc / 5.6) * latA_px * 0.7) : 18;

      // Orbit cloud
      const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, orbitRadPx);
      grad.addColorStop(0, "rgba(56, 189, 248, 0.4)");
      grad.addColorStop(0.7, "rgba(56, 189, 248, 0.15)");
      grad.addColorStop(1, "rgba(56, 189, 248, 0.0)");
      ctx.fillStyle = grad;
      ctx.beginPath(); ctx.arc(cx, cy, orbitRadPx, 0, 2 * Math.PI); ctx.fill();

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, orbitRadPx, 0, 2 * Math.PI); ctx.stroke();
      ctx.setLineDash([]);

      // Central Hole (h+) and Orbiting Electron (e-)
      ctx.beginPath(); ctx.arc(cx, cy, 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#f43f5e"; ctx.fill();
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 9px Inter"; ctx.fillText("h⁺", cx - 4, cy + 3);

      const eAng = time * 2.5;
      const ex = cx + orbitRadPx * Math.cos(eAng);
      const ey = cy + orbitRadPx * Math.sin(eAng);
      ctx.beginPath(); ctx.arc(ex, ey, 5, 0, 2 * Math.PI);
      ctx.fillStyle = "#38bdf8"; ctx.fill();
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 9px Inter"; ctx.fillText("e⁻", ex - 4, ey + 3);

      // --- RIGHT PLOT: ABSORPTION COEFFICIENT α(ħω) ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText("Optical Absorption α(ħω) with Hydrogenic Bound States", plotR.x, plotR.y - 12);

      const eMin = 1.35, eMax = 1.70;
      const gapPx = plotR.x + ((Eg - eMin) / (eMax - eMin)) * plotR.w;

      // Bandgap vertical line
      ctx.strokeStyle = "#475569"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(gapPx, plotR.y); ctx.lineTo(gapPx, plotR.y + plotR.h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter"; ctx.fillText("E_g Continuum", gapPx + 4, plotR.y + 18);

      // Trace Absorption spectrum: sharp Lorentzian exciton peaks for n=1,2,3 then sqrt(E - Eg) continuum
      ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.4;
      const gammaL = 0.008; // broadening in eV
      const specPts = 100;
      for (let i = 0; i <= specPts; i++) {
        const hOmega = eMin + (i / specPts) * (eMax - eMin);
        let alpha = 0;
        // Exciton peaks n=1, 2, 3
        for (let n = 1; n <= 3; n++) {
          const En = Eg - Ry_star / (n * n);
          const oscStrength = 1.0 / (n * n * n);
          const lorentz = (gammaL / (Math.PI * (Math.pow(hOmega - En, 2) + gammaL * gammaL))) * oscStrength * 0.05;
          alpha += lorentz;
        }
        // Interband continuum above Eg (Sommerfeld factor enhancement)
        if (hOmega >= Eg) {
          alpha += 0.8 * Math.sqrt((hOmega - Eg) / 0.1) + 0.35;
        }
        const px = plotR.x + (i / specPts) * plotR.w;
        const py = plotR.y + plotR.h - (alpha / 2.5) * (plotR.h * 0.8) - 15;
        const clampedPy = Math.max(plotR.y + 10, py);
        if (i === 0) ctx.moveTo(px, clampedPy); else ctx.lineTo(px, clampedPy);
      }
      ctx.stroke();

      // Peak label for n=1
      const n1Px = plotR.x + ((E_b1 - eMin) / (eMax - eMin)) * plotR.w;
      ctx.fillStyle = "#10b981"; ctx.font = "bold 10px Inter";
      ctx.fillText("n=1 Exciton Peak", n1Px - 30, plotR.y + plotR.h * 0.35);

      // Telemetry info panel
      const bY = plotR.y + plotR.h - 55;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, bY, plotR.w - 20, 48);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, bY, plotR.w - 20, 48);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Rydberg R_y* = ${(Ry_star * 1000).toFixed(1)} meV  |  Radius a_exc = ${a_exc.toFixed(1)} Å`, plotR.x + 20, bY + 18);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Binding Energy E_b = ${(Ry_star * 1000).toFixed(1)} meV  (E_exc = ${(Eg - Ry_star).toFixed(3)} eV)`, plotR.x + 20, bY + 36);
    }
  },

  // 14. Crystal Defects & Ionic Vacancy Diffusion Thermodynamics
  "ssp2-defects-diffusion-sim": {
    title: "Thermodynamics of Schottky/Frenkel Defects & Vacancy Diffusion",
    desc: "Rigorous statistical mechanics of equilibrium point defects: n_S = N exp(-E_f/2k_B T) and atomic vacancy diffusion D(T) = D₀ exp(-E_a/k_B T). Features real-time lattice hopping animation and Arrhenius plots.",
    isAnimated: true,
    controls: [
      { id: "defectType", label: "Defect Mechanism", min: 0, max: 1, step: 1, value: 0 }, // 0: Schottky, 1: Frenkel
      { id: "tempT", label: "Temperature T (Kelvin)", min: 400, max: 1400, step: 25, value: 900 },
      { id: "formEf", label: "Formation Energy E_f (eV)", min: 1.0, max: 3.0, step: 0.2, value: 1.8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const isSchottky = (vals.defectType === undefined || Math.round(vals.defectType) === 0);
      const T = vals.tempT !== undefined ? vals.tempT : 900;
      const Ef = vals.formEf !== undefined ? vals.formEf : 1.8;
      const Em = 0.8; // migration barrier eV
      const kB = 8.617e-5; // eV/K

      // Equilibrium defect fraction: n/N = exp(-Ef / 2kB T) for Schottky/Frenkel
      const defectFraction = Math.exp(-Ef / (2 * kB * T));
      const Ea = Ef / 2 + Em; // Total activation energy for self-diffusion
      const diffCoeff = Math.exp(-Ea / (kB * T)); // normalized D / D0

      // Split canvas: Left is Animated 2D Crystal Lattice; Right is Arrhenius Plot
      const splitX = Math.floor(w * 0.50);

      // --- LEFT PLOT: ANIMATED DEFECT LATTICE ---
      const latBox = { x: 35, y: 35, w: splitX - 55, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(latBox.x, latBox.y, latBox.w, latBox.h);

      ctx.fillStyle = isSchottky ? "#38bdf8" : "#f59e0b"; ctx.font = "bold 12px Inter";
      ctx.fillText(isSchottky ? "Schottky Defect Pair: Cation + Anion Vacancies" : "Frenkel Defect: Interstitial Ion + Vacancy", latBox.x, latBox.y - 12);

      const cols = 9, rows = 7;
      const dx = (latBox.w - 40) / (cols - 1);
      const dy = (latBox.h - 50) / (rows - 1);

      // Lattice nodes
      const jumpPhase = Math.floor(time * (T / 300) * 2.0) % 2;

      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const px = latBox.x + 20 + c * dx;
          const py = latBox.y + 25 + r * dy;
          const isCation = (r + c) % 2 === 0;

          // Introduce deliberate defect vacancies
          const isVac1 = (r === 3 && c === 4); // Cation vacancy
          const isVac2 = (r === 4 && c === 6 && isSchottky); // Anion vacancy

          if (isVac1 || isVac2) {
            // Vacancy square site marker
            ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.5; ctx.setLineDash([2, 2]);
            ctx.strokeRect(px - 7, py - 7, 14, 14);
            ctx.setLineDash([]);
            ctx.fillStyle = "#ef4444"; ctx.font = "8px Inter"; ctx.fillText("V", px - 3, py + 3);
          } else {
            // Normal ion
            ctx.beginPath(); ctx.arc(px, py, isCation ? 7 : 9, 0, 2 * Math.PI);
            ctx.fillStyle = isCation ? "#38bdf8" : "#10b981"; ctx.fill();
            ctx.strokeStyle = "#050811"; ctx.lineWidth = 1; ctx.stroke();
          }
        }
      }

      // If Frenkel, show interstitial squeezed between lattice sites
      if (!isSchottky) {
        const intX = latBox.x + 20 + 3.5 * dx;
        const intY = latBox.y + 25 + 2.5 * dy;
        ctx.beginPath(); ctx.arc(intX, intY, 5, 0, 2 * Math.PI);
        ctx.fillStyle = "#f59e0b"; ctx.fill();
        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1.2; ctx.stroke();
        ctx.fillStyle = "#f59e0b"; ctx.font = "9px Inter"; ctx.fillText("Interstitial", intX - 18, intY - 8);
      }

      // Legend
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(latBox.x + 20, latBox.y + latBox.h - 15, 5, 0, 2*Math.PI); ctx.fill();
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter"; ctx.fillText("Cation (+)", latBox.x + 30, latBox.y + latBox.h - 12);
      ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(latBox.x + 100, latBox.y + latBox.h - 15, 6, 0, 2*Math.PI); ctx.fill();
      ctx.fillText("Anion (-)", latBox.x + 112, latBox.y + latBox.h - 12);

      // --- RIGHT PLOT: ARRHENIUS PLOT ln(n/N) vs 1000/T ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText("Arrhenius Activation: ln(n/N) = -E_f / (2k_B T)", plotR.x, plotR.y - 12);

      const invTMin = 1000 / 1400; // ~0.71 K^-1
      const invTMax = 1000 / 400;  // 2.50 K^-1

      // Arrhenius Line
      ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.4;
      for (let i = 0; i <= 60; i++) {
        const invT = invTMin + (i / 60) * (invTMax - invTMin);
        const curTemp = 1000 / invT;
        const curFrac = Math.exp(-Ef / (2 * kB * curTemp));
        const lnVal = Math.log(Math.max(1e-25, curFrac)); // from 0 down to -30
        const px = plotR.x + (i / 60) * plotR.w;
        const py = plotR.y + plotR.h * (1 - (lnVal - (-25)) / 25);
        const clampedPy = Math.max(plotR.y + 5, Math.min(plotR.y + plotR.h - 5, py));
        if (i === 0) ctx.moveTo(px, clampedPy); else ctx.lineTo(px, clampedPy);
      }
      ctx.stroke();

      // Current operational dot
      const curInvT = 1000 / T;
      const curLn = Math.log(Math.max(1e-25, defectFraction));
      const curPx = plotR.x + ((curInvT - invTMin) / (invTMax - invTMin)) * plotR.w;
      const curPy = plotR.y + plotR.h * (1 - (curLn - (-25)) / 25);
      ctx.beginPath(); ctx.arc(curPx, Math.max(plotR.y + 5, Math.min(plotR.y + plotR.h - 5, curPy)), 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#10b981"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      // Telemetry Box
      const bY = plotR.y + plotR.h - 55;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, bY, plotR.w - 20, 48);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, bY, plotR.w - 20, 48);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`T = ${T} K  |  E_f = ${Ef.toFixed(2)} eV  |  E_m = ${Em.toFixed(2)} eV`, plotR.x + 20, bY + 18);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Defect Fraction n/N = ${defectFraction.toExponential(2)}  |  Total E_a = ${Ea.toFixed(2)} eV`, plotR.x + 20, bY + 36);
    }
  },

  // =========================================================================
  // UNIT 8: ADVANCED ELECTRON CORRELATIONS & BAND STRUCTURE
  // =========================================================================

  // 15. Lindhard Dielectric Function & Friedel Oscillations
  "ssp2-lindhard-screening-sim": {
    title: "Lindhard Dielectric Screening & Real-Space Friedel Oscillations",
    desc: "Rigorous quantum linear response of Fermi electron gas. Computes Lindhard static susceptibility χ(q)/χ₀, Kohn anomaly slope logarithmic singularity at q = 2k_F, and real-space Friedel oscillations δρ(r) ∝ cos(2k_F r)/r³.",
    isAnimated: true,
    controls: [
      { id: "fermiKf", label: "Fermi Wavenumber k_F (Å⁻¹)", min: 0.6, max: 2.0, step: 0.1, value: 1.2 },
      { id: "chargeZ", label: "Impurity Valence Z", min: -2, max: 3, step: 1, value: 1 },
      { id: "tfLambda", label: "Thomas-Fermi k_TF / k_F", min: 0.4, max: 1.8, step: 0.1, value: 0.8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const kF = vals.fermiKf !== undefined ? vals.fermiKf : 1.2;
      const Z = vals.chargeZ !== undefined ? vals.chargeZ : 1;
      const tfRatio = vals.tfLambda !== undefined ? vals.tfLambda : 0.8;
      const kTF = tfRatio * kF;

      // Lindhard function F(x) where x = q / (2kF):
      // F(x) = 1/2 + ((1 - x^2)/(4x)) * ln| (1 + x)/(1 - x) |
      function lindhardF(x) {
        if (Math.abs(x) < 1e-4) return 1.0;
        if (Math.abs(x - 1.0) < 1e-4) return 0.5;
        const arg = Math.abs((1 + x) / (1 - x));
        return 0.5 + ((1 - x * x) / (4 * x)) * Math.log(arg);
      }

      // Split canvas: Left is Real-Space Friedel Oscillations; Right is q-space Susceptibility χ(q)/χ0
      const splitX = Math.floor(w * 0.52);

      // --- LEFT PLOT: REAL-SPACE INDUCED CHARGE DENSITY δρ(r) ---
      const plotL = { x: 45, y: 35, w: splitX - 65, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Real-Space Charge Perturbation δρ(r) & Friedel Oscillations", plotL.x, plotL.y - 12);

      const midY = plotL.y + plotL.h * 0.5;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(plotL.x, midY); ctx.lineTo(plotL.x + plotL.w, midY); ctx.stroke();

      const rMax = 12.0; // r in Angstroms

      // Plot Thomas-Fermi monotonic exponential decay (green dashed)
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.6;
      for (let i = 1; i <= 80; i++) {
        const r = (i / 80) * rMax;
        const tfVal = Z * Math.exp(-kTF * r) / (r * 1.5);
        const px = plotL.x + (i / 80) * plotL.w;
        const py = midY - (tfVal / 1.5) * (plotL.h * 0.4);
        const clampedPy = Math.max(plotL.y + 5, Math.min(plotL.y + plotL.h - 5, py));
        if (i === 1) ctx.moveTo(px, clampedPy); else ctx.lineTo(px, clampedPy);
      }
      ctx.stroke(); ctx.setLineDash([]);

      // Plot Lindhard Quantum Response with Friedel Oscillations (blue solid)
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.2;
      for (let i = 1; i <= 100; i++) {
        const r = (i / 100) * rMax;
        // Asymptotic Friedel form: delta_rho(r) ~ cos(2 kF r) / r^3 for large r, screened Coulomb for small r
        const coreScreen = Z * Math.exp(-kTF * r) / (r * 1.5);
        const friedelOsc = 0.4 * Z * Math.cos(2 * kF * r) / (Math.pow(r, 2.5) + 0.5);
        const totalVal = coreScreen + friedelOsc;
        const px = plotL.x + (i / 100) * plotL.w;
        const py = midY - (totalVal / 1.5) * (plotL.h * 0.4);
        const clampedPy = Math.max(plotL.y + 5, Math.min(plotL.y + plotL.h - 5, py));
        if (i === 1) ctx.moveTo(px, clampedPy); else ctx.lineTo(px, clampedPy);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = "#38bdf8"; ctx.fillRect(plotL.x + plotL.w - 180, plotL.y + 15, 12, 3);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter"; ctx.fillText("Lindhard (Friedel cos 2k_F r / r³)", plotL.x + plotL.w - 162, plotL.y + 18);
      ctx.fillStyle = "#10b981"; ctx.fillRect(plotL.x + plotL.w - 180, plotL.y + 32, 12, 3);
      ctx.fillText("Thomas-Fermi (Monotonic exp)", plotL.x + plotL.w - 162, plotL.y + 35);

      // --- RIGHT PLOT: STATIC SUSCEPTIBILITY χ(q)/χ₀ & KOHN ANOMALY ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText("Static Susceptibility χ(q)/χ₀ & Kohn Singularity at q = 2k_F", plotR.x, plotR.y - 12);

      const maxQ_2kF = 2.5; // q / 2kF from 0 to 2.5
      const kohnX = plotR.x + (1.0 / maxQ_2kF) * plotR.w;

      // Vertical line at q = 2 kF
      ctx.strokeStyle = "#ef4444"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(kohnX, plotR.y); ctx.lineTo(kohnX, plotR.y + plotR.h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter"; ctx.fillText("q = 2k_F (Kohn Anomaly)", kohnX - 25, plotR.y + 16);

      // Plot Lindhard function F(q/2kF)
      ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.4;
      for (let i = 0; i <= 80; i++) {
        const xVal = (i / 80) * maxQ_2kF;
        const fVal = lindhardF(xVal);
        const px = plotR.x + (i / 80) * plotR.w;
        const py = plotR.y + plotR.h - (fVal / 1.1) * (plotR.h * 0.8) - 15;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Telemetry Panel
      const bY = plotR.y + plotR.h - 55;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, bY, plotR.w - 20, 48);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, bY, plotR.w - 20, 48);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`k_F = ${kF.toFixed(2)} Å⁻¹  |  2k_F = ${(2*kF).toFixed(2)} Å⁻¹  |  λ_Friedel = π/k_F = ${(Math.PI/kF).toFixed(2)} Å`, plotR.x + 20, bY + 18);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Derivative dχ/dq → -∞ at q = 2k_F (Drives Giant Kohn Phonon Softening)`, plotR.x + 20, bY + 36);
    }
  },

  // 16. Hubbard Model, Mott Transition & 2D Tight-Binding Band Structure
  "ssp2-tightbinding-hubbard-sim": {
    title: "Hubbard Model, Mott Insulating Transition & Nested Fermi Surface",
    desc: "Rigorous 2D Hubbard model H = -t ∑(c†c + h.c.) + U ∑ n_↑ n_↓ on square lattice. Computes half-filled nested diamond Fermi surface and Mott metal-insulator gap opening with split Lower/Upper Hubbard bands.",
    isAnimated: true,
    controls: [
      { id: "hubbardU", label: "Coulomb Repulsion U / t", min: 0.0, max: 10.0, step: 0.5, value: 4.5 },
      { id: "electronFill", label: "Filling Factor n (Half=1.0)", min: 0.6, max: 1.4, step: 0.05, value: 1.0 },
      { id: "hoppingT", label: "Hopping Energy t (eV)", min: 0.5, max: 2.5, step: 0.25, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const U_t = vals.hubbardU !== undefined ? vals.hubbardU : 4.5;
      const filling = vals.electronFill !== undefined ? vals.electronFill : 1.0;
      const t = vals.hoppingT !== undefined ? vals.hoppingT : 1.0;

      // Bandwidth W = 8t for 2D square lattice: E(kx, ky) = -2t (cos kx a + cos ky a)
      const W = 8 * t;
      const isMottInsulator = (Math.abs(filling - 1.0) < 0.08) && (U_t > 3.0);
      const mottGap = isMottInsulator ? Math.max(0, (U_t - 2.5) * t * 0.7) : 0.0;

      // Split canvas: Left is 2D Brillouin Zone & Fermi Surface; Right is Hubbard Density of States D(E)
      const splitX = Math.floor(w * 0.48);

      // --- LEFT PLOT: 2D BRILLOUIN ZONE & FERMI SURFACE ---
      const bzBox = { x: 35, y: 35, w: splitX - 55, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(bzBox.x, bzBox.y, bzBox.w, bzBox.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText(Math.abs(filling - 1.0) < 0.02 ? "Nested Diamond Fermi Surface at Half-Filling (n=1.0)" : `2D Fermi Surface Contours (n = ${filling.toFixed(2)})`, bzBox.x, bzBox.y - 12);

      const bzSize = Math.min(bzBox.w, bzBox.h) - 50;
      const bzCx = bzBox.x + bzBox.w * 0.5;
      const bzCy = bzBox.y + bzBox.h * 0.5;

      // Square Brillouin Zone Boundary [-pi, pi] x [-pi, pi]
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.strokeRect(bzCx - bzSize * 0.5, bzCy - bzSize * 0.5, bzSize, bzSize);

      // kx and ky axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(bzCx - bzSize * 0.5, bzCy); ctx.lineTo(bzCx + bzSize * 0.5, bzCy);
      ctx.moveTo(bzCx, bzCy - bzSize * 0.5); ctx.lineTo(bzCx, bzCy + bzSize * 0.5);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "9px Inter";
      ctx.fillText("k_x (π/a)", bzCx + bzSize * 0.5 - 35, bzCy - 5);
      ctx.fillText("k_y (π/a)", bzCx + 6, bzCy - bzSize * 0.5 + 14);

      // Calculate Fermi energy EF for given filling
      // n=1.0 corresponds exactly to EF = 0 (diamond nesting)
      const EF = (filling - 1.0) * 3.2 * t;

      // Draw Fermi surface contours by solving cos(kx) + cos(ky) = -EF / (2t)
      const targetVal = -EF / (2 * t);
      ctx.beginPath();
      ctx.strokeStyle = isMottInsulator ? "#ef4444" : "#10b981";
      ctx.lineWidth = 2.4;

      const fsPts = 70;
      // 4 Quadrants of the contour
      for (let quad = 0; quad < 4; quad++) {
        for (let i = 0; i <= fsPts; i++) {
          const kx = (i / fsPts) * Math.PI;
          const cosKy = targetVal - Math.cos(kx);
          if (cosKy >= -1.0 && cosKy <= 1.0) {
            const ky = Math.acos(cosKy);
            let signX = (quad === 0 || quad === 3) ? 1 : -1;
            let signY = (quad === 0 || quad === 1) ? 1 : -1;
            const px = bzCx + (signX * kx / Math.PI) * (bzSize * 0.5);
            const py = bzCy - (signY * ky / Math.PI) * (bzSize * 0.5);
            if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
          }
        }
      }
      ctx.stroke();

      // --- RIGHT PLOT: HUBBARD DENSITY OF STATES D(E) & MOTT GAP ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText("Hubbard DOS D(E): Lower & Upper Hubbard Bands", plotR.x, plotR.y - 12);

      const dosMidY = plotR.y + plotR.h * 0.5;
      const dosMaxE = 8.0 * t; // range from -8t to +8t

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(plotR.x, dosMidY); ctx.lineTo(plotR.x + plotR.w, dosMidY);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("E = 0 (Fermi Level)", plotR.x + 8, dosMidY - 5);

      // Plot DOS curve: Non-interacting single 2D tight-binding band vs Split Hubbard bands
      ctx.beginPath(); ctx.strokeStyle = isMottInsulator ? "#ef4444" : "#10b981"; ctx.lineWidth = 2.2;
      const dSteps = 100;
      for (let i = 0; i <= dSteps; i++) {
        const E = -dosMaxE + (i / dSteps) * (2 * dosMaxE);
        let dos = 0;
        if (U_t < 1.0) {
          // Free tight-binding van Hove log singularity
          const absE = Math.abs(E);
          if (absE < 4 * t) {
            dos = 1.2 * Math.log(Math.max(1.05, (4 * t) / Math.max(0.01, absE)));
          }
        } else {
          // Hubbard split bands centered at -U/2 and +U/2
          const peakL = -0.5 * U_t * t;
          const peakU = 0.5 * U_t * t;
          const width = 2.5 * t;
          const dL = Math.exp(-Math.pow((E - peakL) / width, 2));
          const dU = Math.exp(-Math.pow((E - peakU) / width, 2));
          // Central quasiparticle peak suppressed when U large
          const centralQP = Math.max(0, 1 - U_t / 5.0) * Math.exp(-Math.pow(E / (1.5 * t), 2));
          dos = (dL + dU) * 1.4 + centralQP * 1.5;
        }
        const px = plotR.x + (i / dSteps) * plotR.w;
        const py = plotR.y + plotR.h - (dos / 3.2) * (plotR.h * 0.8) - 15;
        const clampedPy = Math.max(plotR.y + 5, Math.min(plotR.y + plotR.h - 5, py));
        if (i === 0) ctx.moveTo(px, clampedPy); else ctx.lineTo(px, clampedPy);
      }
      ctx.stroke();

      // Band labels
      if (U_t >= 2.0) {
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 10px Inter";
        ctx.fillText("Lower Hubbard Band (LHB)", plotR.x + plotR.w * 0.15, plotR.y + 35);
        ctx.fillStyle = "#f43f5e";
        ctx.fillText("Upper Hubbard Band (UHB)", plotR.x + plotR.w * 0.65, plotR.y + 35);
      }

      // Telemetry Box
      const bY = plotR.y + plotR.h - 55;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, bY, plotR.w - 20, 48);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, bY, plotR.w - 20, 48);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`U / t = ${U_t.toFixed(1)}  |  Bandwidth W = 8t = ${(8*t).toFixed(1)} eV  |  Filling n = ${filling.toFixed(2)}`, plotR.x + 20, bY + 18);
      ctx.fillStyle = isMottInsulator ? "#ef4444" : "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(isMottInsulator ? `MOTT INSULATOR: Gap Opened Δ_Mott ≈ ${mottGap.toFixed(2)} eV (Correlation Driven)` : "CORRELATED METALLIC PHASE (Fermi Liquid)", plotR.x + 20, bY + 36);
    }
  }
};
''';

with open("ssp2_sims_p4.js", "w", encoding="utf-8") as f:
    f.write(part4_js)

print("ssp2_sims_p4.js generated! Size:", len(part4_js))
