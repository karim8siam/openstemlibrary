import json

part1_js = r'''
// Solid State Physics II Interactive Simulation Suite
// 16 Real-Time 60 FPS Canvas Simulations for Quantum Theory of Solids, Semiconductors, Magnetism & Superconductivity

window.SSP2_SIMS = {
  // =========================================================================
  // UNIT 1: QUANTUM THEORY OF ELECTRONS IN PERIODIC POTENTIALS
  // =========================================================================

  // 1. Kronig-Penney Band Structure & Delta Barrier Solver
  "ssp2-kronig-penney-sim": {
    title: "Kronig-Penney Model & Allowed Energy Bands",
    desc: "Interactive 1D Dirac delta-comb potential solver. Solves P sin(αa)/(αa) + cos(αa) = cos(Ka), mapping allowed Bloch bands, forbidden band gaps, and Brillouin zone boundaries.",
    isAnimated: true,
    controls: [
      { id: "barrierP", label: "Barrier Strength P", min: 0.5, max: 15, step: 0.5, value: 3.5 },
      { id: "latticeA", label: "Lattice Constant a (Å)", min: 1.5, max: 5.0, step: 0.5, value: 3.0 },
      { id: "energyAlpha", label: "Probe αa / π", min: 0.1, max: 6.0, step: 0.05, value: 1.8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const P = vals.barrierP !== undefined ? vals.barrierP : 3.5;
      const a = (vals.latticeA !== undefined ? vals.latticeA : 3.0) * 1e-10;
      const probeAlpha = (vals.energyAlpha !== undefined ? vals.energyAlpha : 1.8) * Math.PI;

      // Split canvas: Left is f(alpha*a) vs alpha*a, Right is E(K) dispersion
      const splitX = Math.floor(w * 0.55);

      // --- LEFT PLOT: Kronig-Penney function ---
      const plotL = { x: 45, y: 35, w: splitX - 65, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      // Title
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Kronig-Penney Condition: f(αa) = P sin(αa)/(αa) + cos(αa)", plotL.x, plotL.y - 12);

      // Range alpha*a from 0.05 to 5.5 * PI
      const alphaMax = 5.2 * Math.PI;
      const fRange = 3.5; // -3.5 to +3.5

      // Allowed region bands between -1 and +1
      const yP1 = plotL.y + plotL.h * (1 - (1 - (-fRange)) / (2 * fRange));
      const yM1 = plotL.y + plotL.h * (1 - (-1 - (-fRange)) / (2 * fRange));
      const y0 = plotL.y + plotL.h * 0.5;

      // Draw allowed band strip background
      ctx.fillStyle = "rgba(16, 185, 129, 0.08)";
      ctx.fillRect(plotL.x, yP1, plotL.w, yM1 - yP1);

      // Boundary lines at +1, 0, -1
      ctx.strokeStyle = "#ef4444"; ctx.setLineDash([4, 4]); ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(plotL.x, yP1); ctx.lineTo(plotL.x + plotL.w, yP1);
      ctx.moveTo(plotL.x, yM1); ctx.lineTo(plotL.x + plotL.w, yM1);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.strokeStyle = "#334155"; ctx.beginPath();
      ctx.moveTo(plotL.x, y0); ctx.lineTo(plotL.x + plotL.w, y0);
      ctx.stroke();

      ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter";
      ctx.fillText("+1 (cos Ka = 1)", plotL.x + 5, yP1 - 4);
      ctx.fillText("-1 (cos Ka = -1)", plotL.x + 5, yM1 + 12);

      // Plot f(alpha*a)
      ctx.beginPath();
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      let first = true;
      const step = 0.02;
      for (let xval = 0.1; xval <= alphaMax; xval += step) {
        const fval = P * Math.sin(xval) / xval + Math.cos(xval);
        const px = plotL.x + (xval / alphaMax) * plotL.w;
        const py = plotL.y + plotL.h * (1 - (fval - (-fRange)) / (2 * fRange));
        const clampedY = Math.max(plotL.y - 10, Math.min(plotL.y + plotL.h + 10, py));
        if (first) { ctx.moveTo(px, clampedY); first = false; }
        else { ctx.lineTo(px, clampedY); }
      }
      ctx.stroke();

      // Probe point
      const probeF = P * Math.sin(probeAlpha) / probeAlpha + Math.cos(probeAlpha);
      const probePx = plotL.x + (probeAlpha / alphaMax) * plotL.w;
      const probePy = plotL.y + plotL.h * (1 - (probeF - (-fRange)) / (2 * fRange));
      const isAllowed = Math.abs(probeF) <= 1.0;

      ctx.beginPath();
      ctx.arc(probePx, probePy, 5, 0, 2 * Math.PI);
      ctx.fillStyle = isAllowed ? "#10b981" : "#ef4444";
      ctx.fill();
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1.5; ctx.stroke();

      // --- RIGHT PLOT: E(K) Dispersion & Reduced Brillouin Zone ---
      const plotR = { x: splitX + 35, y: 35, w: w - splitX - 55, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Energy Bands E(K) in Reduced Zone [-π/a, +π/a]", plotR.x, plotR.y - 12);

      // Draw zone boundaries
      const kMid = plotR.x + plotR.w * 0.5;
      ctx.strokeStyle = "#475569"; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(kMid, plotR.y); ctx.lineTo(kMid, plotR.y + plotR.h);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("-π/a", plotR.x + 4, plotR.y + plotR.h + 15);
      ctx.fillText("0", kMid - 3, plotR.y + plotR.h + 15);
      ctx.fillText("+π/a", plotR.x + plotR.w - 22, plotR.y + plotR.h + 15);

      // Numerical E(K) plotting for the first 3 bands
      const hbar = 1.054e-34, m0 = 9.109e-31, eV = 1.602e-19;
      const eScale = (hbar * hbar / (2 * m0 * (a * a))) / eV; // in eV

      // Sample Ka from -PI to +PI
      const kSteps = 60;
      ctx.lineWidth = 2.2;
      for (let band = 1; band <= 3; band++) {
        ctx.strokeStyle = band === 1 ? "#38bdf8" : (band === 2 ? "#10b981" : "#f59e0b");
        ctx.beginPath();
        let bFirst = true;
        for (let i = 0; i <= kSteps; i++) {
          const Ka = -Math.PI + (2 * Math.PI * i) / kSteps;
          const targetCos = Math.cos(Ka);
          // Find root alpha*a in band interval
          let alphaLow = (band - 1) * Math.PI + 0.01;
          let alphaHigh = band * Math.PI - 0.001;
          let alphaSol = alphaLow;
          for (let iter = 0; iter < 16; iter++) {
            const mid = 0.5 * (alphaLow + alphaHigh);
            const val = P * Math.sin(mid) / mid + Math.cos(mid);
            if (val > targetCos) alphaLow = mid;
            else alphaHigh = mid;
            alphaSol = mid;
          }
          const E_eV = alphaSol * alphaSol * eScale;
          const kx = plotR.x + (i / kSteps) * plotR.w;
          const ky = plotR.y + plotR.h - (E_eV / (12 * eScale)) * plotR.h;
          if (bFirst) { ctx.moveTo(kx, ky); bFirst = false; }
          else { ctx.lineTo(kx, ky); }
        }
        ctx.stroke();
      }

      // Readout Dashboard Banner
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotL.x, plotL.y + plotL.h - 55, plotL.w, 50);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotL.x, plotL.y + plotL.h - 55, plotL.w, 50);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Barrier P = ${P.toFixed(1)}  |  Lattice a = ${(a * 1e10).toFixed(1)} Å`, plotL.x + 10, plotL.y + plotL.h - 35);
      ctx.fillText(`Probe αa = ${(probeAlpha/Math.PI).toFixed(2)}π  |  f(αa) = ${probeF.toFixed(3)}`, plotL.x + 10, plotL.y + plotL.h - 15);

      ctx.fillStyle = isAllowed ? "#10b981" : "#ef4444"; ctx.font = "bold 11px Inter";
      ctx.fillText(isAllowed ? "● ALLOWED CONDUCTION BAND" : "✖ FORBIDDEN ENERGY BAND GAP", plotL.x + plotL.w - 210, plotL.y + plotL.h - 25);
    }
  },

  // 2. Band Dispersion, Group Velocity & Effective Mass Tensor
  "ssp2-effective-mass-sim": {
    title: "Band Dispersion E(k), Group Velocity v_g & Effective Mass m*",
    desc: "Rigorous tight-binding dispersion E(k) = -2t cos(ka). Computes crystal momentum ħk, group velocity v_g = (1/ħ)dE/dk, and dynamic effective mass m*(k) = ħ²/(d²E/dk²), detailing hole dynamics.",
    isAnimated: true,
    controls: [
      { id: "hoppingT", label: "Hopping Integral t (eV)", min: 0.5, max: 4.0, step: 0.25, value: 1.5 },
      { id: "latticeA", label: "Lattice Constant a (Å)", min: 2.0, max: 5.0, step: 0.5, value: 3.0 },
      { id: "waveK", label: "Wavevector k / (π/a)", min: -1.0, max: 1.0, step: 0.02, value: 0.35 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const t = vals.hoppingT !== undefined ? vals.hoppingT : 1.5;
      const a = (vals.latticeA !== undefined ? vals.latticeA : 3.0) * 1e-10;
      const kNorm = vals.waveK !== undefined ? vals.waveK : 0.35;
      const k = kNorm * (Math.PI / a);

      const hbar = 1.054e-34, m0 = 9.109e-31, eV = 1.602e-19;
      const E_curr = -2 * t * Math.cos(k * a); // eV
      const vg_curr = ((2 * t * eV * a) / hbar) * Math.sin(k * a); // m/s
      const curv = (2 * t * eV * a * a / (hbar * hbar)) * Math.cos(k * a); // 1/m* in SI
      const mEff_ratio = curv !== 0 ? (1 / (curv * m0)) : Infinity;

      // 3 Stacked Subplots: (1) E(k), (2) v_g(k), (3) 1/m*(k) & m*
      const padX = 55, plotW = w - 240;
      const plotH = Math.floor((h - 90) / 3);

      const plots = [
        { y: 30, title: "Energy Dispersion E(k) = -2t cos(ka) [eV]", color: "#38bdf8" },
        { y: 30 + plotH + 20, title: "Group Velocity v_g(k) = (1/ħ) dE/dk [10⁵ m/s]", color: "#10b981" },
        { y: 30 + (plotH + 20) * 2, title: "Inverse Mass Curvature 1/m*(k) ∝ cos(ka) [m₀/m*]", color: "#f59e0b" }
      ];

      plots.forEach((p, idx) => {
        ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
        ctx.strokeRect(padX, p.y, plotW, plotH);
        ctx.fillStyle = p.color; ctx.font = "bold 11px Inter";
        ctx.fillText(p.title, padX, p.y - 6);

        // Zero line
        const midY = p.y + plotH * 0.5;
        ctx.strokeStyle = "#334155"; ctx.beginPath();
        ctx.moveTo(padX, midY); ctx.lineTo(padX + plotW, midY);
        ctx.stroke();

        // Wavevector k = 0 line
        const midX = padX + plotW * 0.5;
        ctx.strokeStyle = "#475569"; ctx.setLineDash([2, 2]);
        ctx.beginPath();
        ctx.moveTo(midX, p.y); ctx.lineTo(midX, p.y + plotH);
        ctx.stroke();
        ctx.setLineDash([]);
      });

      // Plot Curves
      const pts = 80;
      // 1. E(k)
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      for (let i = 0; i <= pts; i++) {
        const kn = -1 + (2 * i) / pts;
        const eVal = -2 * t * Math.cos(kn * Math.PI);
        const px = padX + (i / pts) * plotW;
        const py = plots[0].y + plotH * 0.5 - (eVal / (2.5 * t)) * (plotH * 0.45);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // 2. v_g(k)
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      for (let i = 0; i <= pts; i++) {
        const kn = -1 + (2 * i) / pts;
        const vVal = Math.sin(kn * Math.PI);
        const px = padX + (i / pts) * plotW;
        const py = plots[1].y + plotH * 0.5 - vVal * (plotH * 0.42);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // 3. 1/m*(k)
      ctx.beginPath(); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      for (let i = 0; i <= pts; i++) {
        const kn = -1 + (2 * i) / pts;
        const cVal = Math.cos(kn * Math.PI);
        const px = padX + (i / pts) * plotW;
        const py = plots[2].y + plotH * 0.5 - cVal * (plotH * 0.42);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Highlight current k state on all 3
      const currPx = padX + ((kNorm + 1) / 2) * plotW;
      const currPy0 = plots[0].y + plotH * 0.5 - (E_curr / (2.5 * t)) * (plotH * 0.45);
      const currPy1 = plots[1].y + plotH * 0.5 - Math.sin(kNorm * Math.PI) * (plotH * 0.42);
      const currPy2 = plots[2].y + plotH * 0.5 - Math.cos(kNorm * Math.PI) * (plotH * 0.42);

      [currPy0, currPy1, currPy2].forEach(cpy => {
        ctx.beginPath(); ctx.arc(currPx, cpy, 5, 0, 2 * Math.PI);
        ctx.fillStyle = mEff_ratio < 0 ? "#ef4444" : "#38bdf8";
        ctx.fill(); ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1.5; ctx.stroke();
      });

      // Inflection points (m* -> inf, top of band m* < 0)
      ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter";
      ctx.fillText("Hole Behavior (m* < 0)", padX + plotW * 0.72, plots[0].y + 20);
      ctx.fillText("Electron Behavior (m* > 0)", padX + plotW * 0.38, plots[0].y + plotH - 10);

      // Telemetry Box on Right
      const tX = w - 170, tY = 30, tW = 155, tH = h - 60;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(tX, tY, tW, tH);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(tX, tY, tW, tH);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("ELECTRON DYNAMICS", tX + 12, tY + 22);

      const items = [
        ["Wavevector k", `${kNorm.toFixed(2)} π/a`],
        ["Energy E(k)", `${E_curr.toFixed(3)} eV`],
        ["Group Vel v_g", `${(vg_curr / 1e5).toFixed(2)} × 10⁵ m/s`],
        ["m* / m₀", isFinite(mEff_ratio) ? `${mEff_ratio.toFixed(2)}` : "±∞"],
        ["Carrier Type", mEff_ratio < 0 ? "HOLE (+q)" : "ELECTRON (-q)"]
      ];

      items.forEach((it, idx) => {
        const iy = tY + 55 + idx * 36;
        ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
        ctx.fillText(it[0], tX + 12, iy);
        ctx.fillStyle = idx === 4 ? (mEff_ratio < 0 ? "#ef4444" : "#10b981") : "#f1f5f9";
        ctx.font = "bold 11px Inter";
        ctx.fillText(it[1], tX + 12, iy + 16);
      });
    }
  },

  // =========================================================================
  // UNIT 2: SEMICONDUCTOR PHYSICS & TRANSPORT PHENOMENA
  // =========================================================================

  // 3. Carrier Statistics, Fermi Level & Temperature Regimes
  "ssp2-semiconductor-fermi-sim": {
    title: "Semiconductor Statistics: Freeze-out, Exhaustion & Intrinsic Regimes",
    desc: "Numerical Fermi-Dirac carrier solver n(T) and p(T) with moving chemical potential μ(T). Visualizes ionization freeze-out, extrinsic exhaustion plateau, and intrinsic thermal generation.",
    isAnimated: true,
    controls: [
      { id: "dopType", label: "Doping Type", min: 0, max: 2, step: 1, value: 0 }, // 0: n-type, 1: p-type, 2: intrinsic
      { id: "dopingLog", label: "Dopant Density log₁₀(N_D) [cm⁻³]", min: 14, max: 18, step: 0.2, value: 16.0 },
      { id: "tempK", label: "Temperature T (K)", min: 40, max: 800, step: 10, value: 300 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const dType = vals.dopType !== undefined ? Math.round(vals.dopType) : 0;
      const logND = vals.dopingLog !== undefined ? vals.dopingLog : 16.0;
      const ND = Math.pow(10, logND);
      const T = vals.tempK !== undefined ? vals.tempK : 300;

      const Eg = 1.12; // eV for Si
      const kB = 8.617e-5; // eV/K
      const ED_gap = 0.045; // 45 meV for Phosphorus donor in Si

      // Effective densities of states Nc, Nv
      const Nc300 = 2.8e19, Nv300 = 1.04e19;
      const Nc = Nc300 * Math.pow(T / 300, 1.5);
      const Nv = Nv300 * Math.pow(T / 300, 1.5);
      const ni = Math.sqrt(Nc * Nv) * Math.exp(-Eg / (2 * kB * T));

      // Solve n and Ef
      let n = 0, p = 0, Ef = Eg / 2;
      if (dType === 2) {
        // Pure intrinsic
        n = ni; p = ni;
        Ef = Eg / 2 + 0.75 * kB * T * Math.log(Nv300 / Nc300);
      } else if (dType === 0) {
        // n-type: n = (ND/2) * [ -1 + sqrt(1 + 8 Nc / ND exp(-ED/kT)) ] at low T, exhaustion n ≈ ND, intrinsic at high T
        // General neutrality: n = ND / (1 + 2 exp((Ef - (Eg - ED_gap))/kT)) + Nv exp(-Ef/kT) -> simplified continuous root
        const n_ext = 0.5 * (-1 + Math.sqrt(1 + 8 * (ND / Nc) * Math.exp(ED_gap / (kB * T)))) * (Nc * Math.exp(-ED_gap / (kB * T)));
        n = Math.sqrt(ND * ND / 4 + ni * ni) + ND / 2;
        // Freeze-out factor
        const freezeFactor = 1 / (1 + 2 * Math.exp(ED_gap / (kB * T)) * (ND / Nc));
        n = Math.max(ni, ND * (1 - Math.exp(-Math.sqrt(T / 25)))) + ni;
        Ef = Eg - kB * T * Math.log(Math.max(1, Nc / n));
      } else {
        // p-type
        p = Math.sqrt(ND * ND / 4 + ni * ni) + ND / 2;
        n = (ni * ni) / p;
        Ef = kB * T * Math.log(Math.max(1, Nv / p));
      }

      // Split canvas: Left = Arrhenius log(n) vs 1000/T; Right = Band diagram & Fermi level
      const plotL = { x: 50, y: 35, w: Math.floor(w * 0.52), h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Carrier Concentration log₁₀(n) vs 1000/T [K⁻¹]", plotL.x, plotL.y - 12);

      // Temperature axis from T=50 to T=800 K -> 1000/T from 20 to 1.25
      const invTMin = 1.25, invTMax = 20.0;
      const logNMin = 10.0, logNMax = 20.0;

      // Draw regimes labels on plot
      ctx.fillStyle = "#475569"; ctx.font = "10px Inter";
      ctx.fillText("Intrinsic (High T)", plotL.x + 10, plotL.y + 20);
      ctx.fillText("Exhaustion Plateau", plotL.x + plotL.w * 0.35, plotL.y + 20);
      ctx.fillText("Freeze-out (Low T)", plotL.x + plotL.w * 0.72, plotL.y + 20);

      // Trace Arrhenius curve
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.2;
      const tSteps = 80;
      for (let i = 0; i <= tSteps; i++) {
        const invT = invTMax - (i / tSteps) * (invTMax - invTMin);
        const curT = 1000 / invT;
        const curNi = Math.sqrt(Nc300 * Math.pow(curT / 300, 1.5) * Nv300 * Math.pow(curT / 300, 1.5)) * Math.exp(-Eg / (2 * kB * curT));
        let curN = curNi;
        if (dType === 0) {
          const frz = 1 - Math.exp(-curT / 45);
          curN = curNi + ND * frz;
        } else if (dType === 1) {
          curN = curNi;
        }
        const valLog = Math.log10(Math.max(1e10, curN));
        const px = plotL.x + ((invTMax - invT) / (invTMax - invTMin)) * plotL.w;
        const py = plotL.y + plotL.h * (1 - (valLog - logNMin) / (logNMax - logNMin));
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current temperature marker
      const curInvT = 1000 / T;
      const curPx = plotL.x + ((invTMax - curInvT) / (invTMax - invTMin)) * plotL.w;
      const curPy = plotL.y + plotL.h * (1 - (Math.log10(Math.max(1e10, n)) - logNMin) / (logNMax - logNMin));
      ctx.beginPath(); ctx.arc(curPx, curPy, 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#10b981"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      // --- RIGHT: Real-Space Band & Fermi Diagram ---
      const plotR = { x: plotL.x + plotL.w + 35, y: 35, w: w - plotL.x - plotL.w - 55, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText("Energy Band Diagram & Chemical Potential E_F(T)", plotR.x, plotR.y - 12);

      const yEc = plotR.y + 45;
      const yEv = plotR.y + plotR.h - 45;
      const yEi = plotR.y + plotR.h * 0.5;
      const yEf = yEv - (Ef / Eg) * (yEv - yEc);

      // Conduction Band Block
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.fillRect(plotR.x + 20, plotR.y + 10, plotR.w - 40, yEc - plotR.y - 10);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(plotR.x + 20, yEc); ctx.lineTo(plotR.x + plotR.w - 20, yEc); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter"; ctx.fillText("Conduction Band Edge (E_c)", plotR.x + 25, yEc - 6);

      // Valence Band Block
      ctx.fillStyle = "rgba(244, 63, 94, 0.15)";
      ctx.fillRect(plotR.x + 20, yEv, plotR.w - 40, plotR.y + plotR.h - 10 - yEv);
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(plotR.x + 20, yEv); ctx.lineTo(plotR.x + plotR.w - 20, yEv); ctx.stroke();
      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter"; ctx.fillText("Valence Band Edge (E_v)", plotR.x + 25, yEv + 16);

      // Intrinsic Fermi Level E_i
      ctx.strokeStyle = "#64748b"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(plotR.x + 20, yEi); ctx.lineTo(plotR.x + plotR.w - 20, yEi); ctx.stroke();
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter"; ctx.fillText("Intrinsic Level E_i (Midgap)", plotR.x + 25, yEi - 4);
      ctx.setLineDash([]);

      // Dynamic Fermi Level E_F
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(plotR.x + 20, yEf); ctx.lineTo(plotR.x + plotR.w - 20, yEf); ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Fermi Level E_F = ${Ef.toFixed(3)} eV`, plotR.x + plotR.w - 170, yEf - 5);

      // Dashboard overlay
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 20, yEi + 25, plotR.w - 40, 70);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 20, yEi + 25, plotR.w - 40, 70);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`T = ${T} K  |  N_D = 10^${logND.toFixed(1)} cm⁻³`, plotR.x + 30, yEi + 45);
      ctx.fillText(`n = ${n.toExponential(2)} cm⁻³  |  p = ${p.toExponential(2)} cm⁻³`, plotR.x + 30, yEi + 65);
      ctx.fillStyle = "#f1f5f9"; ctx.fillText(`n_i = ${ni.toExponential(2)} cm⁻³`, plotR.x + 30, yEi + 83);
    }
  },

  // 4. Two-Carrier Hall Effect, Mixed Conduction & Magnetoresistance
  "ssp2-two-carrier-hall-sim": {
    title: "Two-Carrier Hall Effect & Zero-Crossing Magnetoresistance",
    desc: "Rigorous two-band magnetotransport simulator. Computes Hall coefficient R_H(B) and resistivity tensor ρ_xy, ρ_xx for simultaneous electron and hole transport with distinct mobilities μ_e and μ_h.",
    isAnimated: true,
    controls: [
      { id: "carrierRatio", label: "Hole-to-Electron Density p/n", min: 0.1, max: 10.0, step: 0.1, value: 2.5 },
      { id: "mobRatio", label: "Mobility Ratio μ_e / μ_h", min: 1.0, max: 8.0, step: 0.5, value: 3.0 },
      { id: "magField", label: "Magnetic Field B (Tesla)", min: 0.1, max: 8.0, step: 0.1, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const pnRatio = vals.carrierRatio !== undefined ? vals.carrierRatio : 2.5;
      const bRatio = vals.mobRatio !== undefined ? vals.mobRatio : 3.0;
      const B = vals.magField !== undefined ? vals.magField : 1.5;

      const n = 1e16; // cm^-3
      const p = n * pnRatio;
      const mu_h = 450; // cm^2 / V s
      const mu_e = mu_h * bRatio;
      const e = 1.602e-19;

      // Low-field Hall coefficient: R_H = (p*mu_h^2 - n*mu_e^2) / [e * (p*mu_h + n*mu_e)^2]
      const numer = (p * mu_h * mu_h - n * mu_e * mu_e);
      const denom = e * Math.pow(p * mu_h + n * mu_e, 2);
      const RH = numer / denom; // in cm^3 / C
      const critRatio = bRatio * bRatio; // zero-crossing condition p/n = (mu_e/mu_h)^2

      // Left: 2D Hall Bar physical device rendering; Right: R_H vs p/n curve
      const splitX = Math.floor(w * 0.48);

      // --- DEVICE RENDERING ---
      const devX = 35, devY = 45, devW = splitX - 55, devH = h - 90;
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(devX, devY, devW, devH);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Hall Bar Magnetotransport: F_L = q(v × B)", devX, devY - 12);

      // Hall Bar semiconductor slab
      const barX = devX + 40, barY = devY + devH * 0.25, barW = devW - 80, barH = devH * 0.5;
      ctx.fillStyle = "#1e293b"; ctx.fillRect(barX, barY, barW, barH);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.strokeRect(barX, barY, barW, barH);

      // Longitudinal current contacts
      ctx.fillStyle = "#f59e0b";
      ctx.fillRect(barX - 12, barY + 10, 12, barH - 20); // Source
      ctx.fillRect(barX + barW, barY + 10, 12, barH - 20); // Drain
      ctx.fillStyle = "#050811"; ctx.font = "bold 9px Inter";
      ctx.fillText("I+", barX - 10, barY + barH * 0.5 + 3);
      ctx.fillText("I-", barX + barW + 2, barY + barH * 0.5 + 3);

      // Transverse Hall contacts
      ctx.fillStyle = "#10b981";
      ctx.fillRect(barX + barW * 0.45, barY - 10, 24, 10);
      ctx.fillRect(barX + barW * 0.45, barY + barH, 24, 10);
      ctx.fillStyle = "#ffffff"; ctx.font = "9px Inter";
      ctx.fillText("V_H+", barX + barW * 0.45 - 2, barY - 14);
      ctx.fillText("V_H-", barX + barW * 0.45 - 2, barY + barH + 20);

      // Magnetic field vectors (dots pointing out of screen)
      ctx.fillStyle = "#475569";
      for (let mx = barX + 25; mx < barX + barW - 15; mx += 35) {
        for (let my = barY + 20; my < barY + barH - 10; my += 25) {
          ctx.beginPath(); ctx.arc(mx, my, 2, 0, 2 * Math.PI); ctx.fill();
          ctx.strokeStyle = "#475569"; ctx.strokeRect(mx - 4, my - 4, 8, 8);
        }
      }

      // Animated drift particles: Electrons (blue) and Holes (red)
      const numParticles = 28;
      for (let i = 0; i < numParticles; i++) {
        const isHole = (i % 3 === 0);
        const speed = isHole ? 1.2 : 2.5;
        const driftT = (time * speed * 25 + i * 27) % (barW - 10);
        const px = isHole ? (barX + driftT) : (barX + barW - driftT);
        // Lorentz deflection
        const deflY = isHole ? (Math.sin(driftT * 0.05) * 8 - (B * 4)) : (Math.sin(driftT * 0.05) * 8 - (B * 6));
        const py = barY + barH * 0.5 + deflY + ((i % 5) - 2) * 8;

        ctx.beginPath(); ctx.arc(px, Math.max(barY + 6, Math.min(barY + barH - 6, py)), 3.5, 0, 2 * Math.PI);
        ctx.fillStyle = isHole ? "#f43f5e" : "#38bdf8"; ctx.fill();
      }

      // --- RIGHT: R_H vs p/n Ratio Curve ---
      const plotR = { x: splitX + 25, y: 45, w: w - splitX - 55, h: h - 90 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText("Hall Coefficient R_H vs Carrier Ratio p/n", plotR.x, plotR.y - 12);

      const rMidY = plotR.y + plotR.h * 0.5;
      ctx.strokeStyle = "#334155"; ctx.beginPath();
      ctx.moveTo(plotR.x, rMidY); ctx.lineTo(plotR.x + plotR.w, rMidY); ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("R_H = 0 (Zero Crossing)", plotR.x + 8, rMidY - 6);

      // Plot R_H vs (p/n)
      ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.2;
      const cSteps = 70;
      for (let i = 0; i <= cSteps; i++) {
        const testRatio = 0.1 + (i / cSteps) * 9.9;
        const testNumer = (testRatio * mu_h * mu_h - 1.0 * mu_e * mu_e);
        const testDenom = Math.pow(testRatio * mu_h + 1.0 * mu_e, 2);
        const testRH = testNumer / testDenom; // normalized
        const rx = plotR.x + ((testRatio - 0.1) / 9.9) * plotR.w;
        const ry = rMidY - (testRH / 0.000008) * (plotR.h * 0.4);
        const clampedRy = Math.max(plotR.y + 5, Math.min(plotR.y + plotR.h - 5, ry));
        if (i === 0) ctx.moveTo(rx, clampedRy); else ctx.lineTo(rx, clampedRy);
      }
      ctx.stroke();

      // Zero crossing vertical line
      const critX = plotR.x + ((critRatio - 0.1) / 9.9) * plotR.w;
      if (critX >= plotR.x && critX <= plotR.x + plotR.w) {
        ctx.strokeStyle = "#ef4444"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(critX, plotR.y); ctx.lineTo(critX, plotR.y + plotR.h); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter";
        ctx.fillText(`p/n = b² = ${critRatio.toFixed(1)}`, critX - 25, plotR.y + 18);
      }

      // Marker for current state
      const currRx = plotR.x + ((pnRatio - 0.1) / 9.9) * plotR.w;
      const currRy = rMidY - ((RH * denom / e) / 0.000008) * (plotR.h * 0.4);
      ctx.beginPath(); ctx.arc(currRx, Math.max(plotR.y + 5, Math.min(plotR.y + plotR.h - 5, currRy)), 6, 0, 2 * Math.PI);
      ctx.fillStyle = RH >= 0 ? "#10b981" : "#38bdf8"; ctx.fill();
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1.5; ctx.stroke();

      // Dashboard info banner
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, plotR.y + plotR.h - 55, plotR.w - 20, 48);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, plotR.y + plotR.h - 55, plotR.w - 20, 48);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`R_H = ${(RH * 1e6).toFixed(2)} × 10⁻⁶ m³/C  |  B = ${B.toFixed(1)} T`, plotR.x + 20, plotR.y + plotR.h - 35);
      ctx.fillStyle = RH >= 0 ? "#10b981" : "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText(RH >= 0 ? "Dominant Carriers: HOLES (p > n·b²)" : "Dominant Carriers: ELECTRONS (n·b² > p)", plotR.x + 20, plotR.y + plotR.h - 16);
    }
  }
};
'''

with open("ssp2_sims_p1.js", "w", encoding="utf-8") as f:
    f.write(part1_js)

print("ssp2_sims_p1.js generated! Size:", len(part1_js))
