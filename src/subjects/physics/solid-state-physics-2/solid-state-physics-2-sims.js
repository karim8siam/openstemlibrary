
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
  },

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
  },

// =========================================================================
  // UNIT 5: PHENOMENOLOGICAL SUPERCONDUCTIVITY & VORTEX PHYSICS
  // =========================================================================

  // 9. Meissner Effect, London Penetration Depth & Screening Currents
  "ssp2-meissner-london-sim": {
    title: "Meissner Effect, London Screening & Penetration Depth λ_L(T)",
    desc: "Rigorous phenomenological electrodynamics solver for ∇²B = B/λ_L². Demonstrates exponential magnetic expulsion B(x) = B₀ exp(-x/λ_L), surface supercurrent J_s(x), and critical temperature divergence.",
    isAnimated: true,
    controls: [
      { id: "tempRatio", label: "Temperature T / T_c", min: 0.0, max: 1.15, step: 0.05, value: 0.4 },
      { id: "appliedB", label: "Applied Field B₀ (mT)", min: 10, max: 150, step: 10, value: 60 },
      { id: "lambdaZero", label: "London Depth λ₀ (nm)", min: 30, max: 120, step: 10, value: 50 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const tRatio = vals.tempRatio !== undefined ? vals.tempRatio : 0.4;
      const B0 = vals.appliedB !== undefined ? vals.appliedB : 60;
      const lambda0 = vals.lambdaZero !== undefined ? vals.lambdaZero : 50;

      // Two-fluid Gorter-Casimir temperature dependence:
      // lambda_L(T) = lambda_0 / sqrt(1 - (T/Tc)^4)
      const isSuper = tRatio < 1.0;
      let lambdaT = Infinity;
      if (isSuper) {
        const denom = Math.sqrt(Math.max(1e-4, 1 - Math.pow(tRatio, 4)));
        lambdaT = lambda0 / denom; // in nm
      }

      // Split canvas: Left is spatial slab profile B(x) & J_s(x); Right is λ_L(T) curve & B_c(T)
      const splitX = Math.floor(w * 0.52);

      // --- LEFT: SPATIAL EXPONENTIAL DECAY ---
      const plotL = { x: 45, y: 35, w: splitX - 65, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Magnetic Field Penetration B(x) = B₀ e^{-x/λ_L} & Supercurrent", plotL.x, plotL.y - 12);

      const slabStartX = plotL.x + Math.floor(plotL.w * 0.28);

      // Vacuum region (left of slab)
      ctx.fillStyle = "rgba(30, 41, 59, 0.3)";
      ctx.fillRect(plotL.x, plotL.y, slabStartX - plotL.x, plotL.h);
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("VACUUM", plotL.x + 10, plotL.y + 20);

      // Superconductor slab (right of slabStartX)
      ctx.fillStyle = isSuper ? "rgba(16, 185, 129, 0.08)" : "rgba(239, 68, 68, 0.08)";
      ctx.fillRect(slabStartX, plotL.y, plotL.x + plotL.w - slabStartX, plotL.h);
      ctx.fillStyle = isSuper ? "#10b981" : "#ef4444"; ctx.font = "bold 10px Inter";
      ctx.fillText(isSuper ? "SUPERCONDUCTING SLAB" : "NORMAL STATE (T ≥ T_c)", slabStartX + 12, plotL.y + 20);

      // Slab interface line x = 0
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(slabStartX, plotL.y); ctx.lineTo(slabStartX, plotL.y + plotL.h); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "10px Inter"; ctx.fillText("x = 0", slabStartX - 14, plotL.y + plotL.h - 10);

      const midY = plotL.y + plotL.h * 0.55;
      const maxDist_nm = 300; // max depth on graph
      const slabW = plotL.x + plotL.w - slabStartX;

      // Plot B(x) profile
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      // In vacuum: B(x) = B0
      ctx.moveTo(plotL.x, midY - (B0 / 160) * (plotL.h * 0.4));
      ctx.lineTo(slabStartX, midY - (B0 / 160) * (plotL.h * 0.4));

      // Inside slab
      const xSteps = 60;
      for (let i = 0; i <= xSteps; i++) {
        const x_nm = (i / xSteps) * maxDist_nm;
        const bVal = isSuper ? B0 * Math.exp(-x_nm / lambdaT) : B0;
        const px = slabStartX + (x_nm / maxDist_nm) * slabW;
        const py = midY - (bVal / 160) * (plotL.h * 0.4);
        ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot London Penetration Depth λ_L marker line inside slab
      if (isSuper && lambdaT < maxDist_nm) {
        const lamPx = slabStartX + (lambdaT / maxDist_nm) * slabW;
        ctx.strokeStyle = "#f59e0b"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(lamPx, plotL.y + 35); ctx.lineTo(lamPx, plotL.y + plotL.h); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#f59e0b"; ctx.font = "10px Inter";
        ctx.fillText(`λ_L = ${lambdaT.toFixed(0)} nm (1/e point)`, lamPx + 4, plotL.y + 50);
      }

      // Draw surface screening current density J_s(x)
      if (isSuper) {
        ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.setLineDash([2, 2]); ctx.lineWidth = 1.8;
        for (let i = 0; i <= xSteps; i++) {
          const x_nm = (i / xSteps) * maxDist_nm;
          const jsVal = (B0 / Math.max(30, lambdaT)) * Math.exp(-x_nm / lambdaT); // arb units
          const px = slabStartX + (x_nm / maxDist_nm) * slabW;
          const py = midY + (jsVal * 60) * (plotL.h * 0.35);
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = "#a855f7"; ctx.font = "10px Inter";
        ctx.fillText("Screening Current J_s(x)", slabStartX + 15, midY + 35);
      }

      // --- RIGHT: λ_L(T) TEMPERATURE DIVERGENCE & PHASE DIAGRAM ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
      ctx.fillText("London Penetration Depth Divergence λ_L(T) → ∞ at T_c", plotR.x, plotR.y - 12);

      // Tc vertical asymptote
      const tcX = plotR.x + (1.0 / 1.15) * plotR.w;
      ctx.strokeStyle = "#ef4444"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(tcX, plotR.y); ctx.lineTo(tcX, plotR.y + plotR.h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter"; ctx.fillText("T = T_c", tcX - 16, plotR.y + 16);

      // Plot λ(T) curve
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.4;
      const tPts = 60;
      for (let i = 0; i <= tPts; i++) {
        const tr = (i / tPts) * 0.985;
        const lam = lambda0 / Math.sqrt(1 - Math.pow(tr, 4));
        const px = plotR.x + (tr / 1.15) * plotR.w;
        const py = plotR.y + plotR.h - (lam / 280) * (plotR.h * 0.8) - 15;
        const clampedPy = Math.max(plotR.y + 10, py);
        if (i === 0) ctx.moveTo(px, clampedPy); else ctx.lineTo(px, clampedPy);
      }
      ctx.stroke();

      // Current operational dot
      if (isSuper && lambdaT < 300) {
        const curPx = plotR.x + (tRatio / 1.15) * plotR.w;
        const curPy = plotR.y + plotR.h - (lambdaT / 280) * (plotR.h * 0.8) - 15;
        ctx.beginPath(); ctx.arc(curPx, Math.max(plotR.y + 10, curPy), 6, 0, 2 * Math.PI);
        ctx.fillStyle = "#38bdf8"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();
      }

      // Telemetry Box
      const tBoxY = plotR.y + plotR.h - 60;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, tBoxY, plotR.w - 20, 52);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, tBoxY, plotR.w - 20, 52);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Applied B₀ = ${B0} mT  |  λ₀ = ${lambda0} nm`, plotR.x + 18, tBoxY + 18);
      ctx.fillStyle = isSuper ? "#10b981" : "#ef4444"; ctx.font = "bold 11px Inter";
      ctx.fillText(isSuper ? `MEISSNER STATE: λ_L(T) = ${lambdaT.toFixed(1)} nm` : "NORMAL STATE: Perfect Flux Penetration (B = B₀)", plotR.x + 18, tBoxY + 36);
    }
  },

  // 10. Abrikosov Vortex Lattice & Type-II Mixed State
  "ssp2-abrikosov-vortex-sim": {
    title: "Abrikosov Flux Lattice, Vortex Cores & Type-II Phase Diagram",
    desc: "Simulates triangular Abrikosov vortex lattice in Type-II superconductors. Renders 2D circulating supercurrent streamlines, normal cores of radius ξ, magnetic flux quanta Φ₀ = h/2e, and H_c1–H_c2 phase bounds.",
    isAnimated: true,
    controls: [
      { id: "glKappa", label: "GL Parameter κ = λ/ξ", min: 1.0, max: 15.0, step: 0.5, value: 5.0 },
      { id: "fieldH", label: "Applied Field H / H_c2", min: 0.05, max: 0.95, step: 0.05, value: 0.35 },
      { id: "coherenceXi", label: "Coherence Length ξ (nm)", min: 2.0, max: 12.0, step: 1.0, value: 5.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const kappa = vals.glKappa !== undefined ? vals.glKappa : 5.0;
      const hRatio = vals.fieldH !== undefined ? vals.fieldH : 0.35;
      const xi = vals.coherenceXi !== undefined ? vals.coherenceXi : 5.0;
      const lambda = kappa * xi;

      // Critical fields in normalized units:
      // Hc1 / Hc = ln(kappa) / (sqrt(2) * kappa)
      // Hc2 / Hc = sqrt(2) * kappa
      // Hence Hc1 / Hc2 = ln(kappa) / (2 * kappa^2)
      const Hc1_Hc2 = Math.log(kappa) / (2 * kappa * kappa);
      const isMeissner = hRatio < Hc1_Hc2;

      // Triangular lattice constant a_tri = 1.075 * sqrt(Phi0 / B)
      // Number of vortices scales with field
      const vortexDensity = Math.max(1, Math.round(4 + hRatio * 18));

      // Split canvas: Left is 2D Abrikosov Lattice; Right is Phase Diagram & Vortex Profile
      const splitX = Math.floor(w * 0.52);

      // --- LEFT: 2D ABRIKOSOV LATTICE CANVAS ---
      const plotL = { x: 35, y: 35, w: splitX - 55, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText(`Abrikosov Vortex Lattice (Φ₀ = 2.07 × 10⁻¹⁵ Wb each)`, plotL.x, plotL.y - 12);

      if (isMeissner) {
        // Pure Meissner state (H < Hc1)
        ctx.fillStyle = "rgba(16, 185, 129, 0.1)";
        ctx.fillRect(plotL.x + 10, plotL.y + 10, plotL.w - 20, plotL.h - 20);
        ctx.fillStyle = "#10b981"; ctx.font = "bold 14px Inter";
        ctx.fillText("MEISSNER STATE (H < H_c1)", plotL.x + plotL.w * 0.25, plotL.y + plotL.h * 0.45);
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText("All magnetic flux completely expelled from the bulk.", plotL.x + plotL.w * 0.2, plotL.y + plotL.h * 0.52);
      } else {
        // Mixed Shubnikov State: Render triangular lattice
        const spacing = Math.max(35, 110 / Math.sqrt(vortexDensity));
        const rowH = spacing * Math.sqrt(3) / 2;
        const coreRad = Math.max(3, Math.min(12, (xi / 5.0) * 5));
        const penRad = Math.max(12, Math.min(35, (lambda / 25.0) * 18));

        // Clip to plotL
        ctx.save();
        ctx.beginPath(); ctx.rect(plotL.x, plotL.y, plotL.w, plotL.h); ctx.clip();

        // Loop over hexagonal grid
        let rowIdx = 0;
        for (let gy = plotL.y + 20; gy < plotL.y + plotL.h + spacing; gy += rowH) {
          const offsetX = (rowIdx % 2 === 0) ? 0 : spacing * 0.5;
          for (let gx = plotL.x + 20 + offsetX; gx < plotL.x + plotL.w + spacing; gx += spacing) {
            // Superconducting screening current loops
            ctx.strokeStyle = "rgba(56, 189, 248, 0.35)"; ctx.lineWidth = 1.0;
            ctx.beginPath(); ctx.arc(gx, gy, penRad, 0, 2 * Math.PI); ctx.stroke();

            // Magnetic field halo (Gaussian gradient)
            const radGrad = ctx.createRadialGradient(gx, gy, 0, gx, gy, penRad);
            radGrad.addColorStop(0, "rgba(245, 158, 11, 0.8)");
            radGrad.addColorStop(0.3, "rgba(245, 158, 11, 0.3)");
            radGrad.addColorStop(1, "rgba(245, 158, 11, 0.0)");
            ctx.fillStyle = radGrad;
            ctx.beginPath(); ctx.arc(gx, gy, penRad, 0, 2 * Math.PI); ctx.fill();

            // Normal Core (order parameter |ψ| → 0)
            ctx.fillStyle = "#ef4444";
            ctx.beginPath(); ctx.arc(gx, gy, coreRad, 0, 2 * Math.PI); ctx.fill();

            // Animated circulating current arrows
            const phaseAng = time * 2.5 + (gx + gy) * 0.05;
            const ax = gx + penRad * Math.cos(phaseAng);
            const ay = gy + penRad * Math.sin(phaseAng);
            ctx.fillStyle = "#38bdf8";
            ctx.beginPath(); ctx.arc(ax, ay, 2, 0, 2 * Math.PI); ctx.fill();
          }
          rowIdx++;
        }
        ctx.restore();
      }

      // --- RIGHT: PHASE DIAGRAM & VORTEX FIELD PROFILE ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText("Type-II H-T Phase Diagram & Core Profile", plotR.x, plotR.y - 12);

      // Phase diagram sub-plot (top half of plotR)
      const pdH = Math.floor(plotR.h * 0.48);
      ctx.fillStyle = "rgba(15, 23, 42, 0.6)"; ctx.fillRect(plotR.x + 15, plotR.y + 15, plotR.w - 30, pdH);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 15, plotR.y + 15, plotR.w - 30, pdH);

      // Boundaries Hc1 and Hc2
      const pdW = plotR.w - 30;
      // Hc2 curve: parabolic drop to 0 at Tc
      ctx.beginPath(); ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2;
      for (let i = 0; i <= 40; i++) {
        const tr = i / 40;
        const hc2 = 1.0 * (1 - tr * tr);
        const px = plotR.x + 15 + tr * pdW;
        const py = plotR.y + 15 + pdH * (1 - hc2);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Hc1 curve
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      for (let i = 0; i <= 40; i++) {
        const tr = i / 40;
        const hc1 = Hc1_Hc2 * (1 - tr * tr);
        const px = plotR.x + 15 + tr * pdW;
        const py = plotR.y + 15 + pdH * (1 - hc1);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current operational operating dot on phase diagram
      const curTr = 0.4;
      const opPx = plotR.x + 15 + curTr * pdW;
      const opPy = plotR.y + 15 + pdH * (1 - hRatio);
      ctx.beginPath(); ctx.arc(opPx, opPy, 5, 0, 2 * Math.PI);
      ctx.fillStyle = isMeissner ? "#10b981" : "#f59e0b"; ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      ctx.fillStyle = "#10b981"; ctx.font = "9px Inter"; ctx.fillText("Meissner (H < H_c1)", plotR.x + 25, plotR.y + 15 + pdH - 8);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("Mixed / Vortex State", plotR.x + 25, plotR.y + 15 + pdH * 0.45);
      ctx.fillStyle = "#ef4444"; ctx.fillText("Normal State (H > H_c2)", plotR.x + pdW * 0.4, plotR.y + 30);

      // Telemetry Box at bottom of plotR
      const tBoxY = plotR.y + pdH + 25;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 15, tBoxY, plotR.w - 30, plotR.h - pdH - 35);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 15, tBoxY, plotR.w - 30, plotR.h - pdH - 35);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`κ = λ/ξ = ${kappa.toFixed(1)}  (Type-II: κ > 1/√2 ≈ 0.707)`, plotR.x + 25, tBoxY + 20);
      ctx.fillText(`Coherence ξ = ${xi} nm  |  Penetration λ = ${lambda.toFixed(0)} nm`, plotR.x + 25, tBoxY + 38);
      ctx.fillStyle = isMeissner ? "#10b981" : "#f59e0b"; ctx.font = "bold 11px Inter";
      ctx.fillText(isMeissner ? "STATE: Pure Diamagnetic Meissner Expulsion" : `STATE: Abrikosov Triangular Flux Lattice (H/H_c2 = ${hRatio.toFixed(2)})`, plotR.x + 25, tBoxY + 56);
    }
  },

  // =========================================================================
  // UNIT 6: MICROSCOPIC BCS THEORY & JOSEPHSON PHENOMENA
  // =========================================================================

  // 11. BCS Energy Gap Δ(T), Quasiparticle DOS & Giaever Tunneling
  "ssp2-bcs-gap-sim": {
    title: "BCS Energy Gap Δ(T), Quasiparticle DOS & Giaever Tunneling",
    desc: "Solves BCS gap equation Δ(T)/Δ(0) ≈ 1.74√(1 - T/T_c). Displays quasiparticle density of states N_s(E) = N(0)|E|/√(E² - Δ²) and differential conductance dI/dV in Giaever S-I-N junctions.",
    isAnimated: true,
    controls: [
      { id: "tempRatio", label: "Reduced Temp T / T_c", min: 0.05, max: 0.98, step: 0.05, value: 0.35 },
      { id: "gapZero", label: "Zero-Temp Gap Δ(0) (meV)", min: 1.0, max: 4.5, step: 0.5, value: 2.5 },
      { id: "broadening", label: "Dynorphin Damping Γ (meV)", min: 0.02, max: 0.25, step: 0.02, value: 0.06 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const tRatio = vals.tempRatio !== undefined ? vals.tempRatio : 0.35;
      const delta0 = vals.gapZero !== undefined ? vals.gapZero : 2.5;
      const gamma = vals.broadening !== undefined ? vals.broadening : 0.06;

      // BCS temperature dependence approximation:
      // Delta(T) / Delta(0) ≈ tanh( 1.74 * sqrt(Tc/T - 1) )
      const deltaT = delta0 * Math.tanh(1.74 * Math.sqrt(Math.max(0, 1.0 / tRatio - 1.0)));

      // Split canvas: Left is BCS Gap Δ(T); Middle is Quasiparticle DOS N_s(E); Right is dI/dV Tunneling
      const subW = Math.floor((w - 80) / 3);

      // --- SUBPLOT 1: Δ(T) vs T/Tc ---
      const p1 = { x: 35, y: 35, w: subW, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(p1.x, p1.y, p1.w, p1.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText("BCS Gap Δ(T)/Δ(0) vs T/T_c", p1.x, p1.y - 12);

      // Trace BCS curve
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.2;
      for (let i = 0; i <= 50; i++) {
        const tr = i / 50;
        const gVal = tr < 1.0 ? Math.tanh(1.74 * Math.sqrt(1.0 / Math.max(0.01, tr) - 1.0)) : 0;
        const px = p1.x + tr * p1.w;
        const py = p1.y + p1.h - (gVal / 1.1) * (p1.h * 0.8) - 15;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current gap point
      const curP1x = p1.x + tRatio * p1.w;
      const curP1y = p1.y + p1.h - ((deltaT / delta0) / 1.1) * (p1.h * 0.8) - 15;
      ctx.beginPath(); ctx.arc(curP1x, curP1y, 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#10b981"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      // --- SUBPLOT 2: QUASIPARTICLE DENSITY OF STATES N_s(E) ---
      const p2 = { x: 35 + subW + 20, y: 35, w: subW, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(p2.x, p2.y, p2.w, p2.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 11px Inter";
      ctx.fillText("Quasiparticle DOS N_s(E) / N(0)", p2.x, p2.y - 12);

      const midE2 = p2.x + p2.w * 0.5;
      // Energy range from -2*delta0 to +2*delta0
      const maxE = 2.2 * delta0;

      ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.2;
      for (let i = 0; i <= 80; i++) {
        const E = -maxE + (2 * maxE * i) / 80;
        // Dynes formula for broadened BCS DOS: Re[ (E - iΓ) / sqrt((E - iΓ)² - Δ²) ]
        const absE = Math.abs(E);
        let dosVal = 0;
        if (absE > deltaT) {
          dosVal = absE / Math.sqrt(absE * absE - deltaT * deltaT + gamma * gamma);
        } else {
          dosVal = gamma / Math.sqrt(deltaT * deltaT - absE * absE + gamma * gamma);
        }
        const px = midE2 + (E / maxE) * (p2.w * 0.45);
        const py = p2.y + p2.h - Math.min(3.5, dosVal) / 3.8 * (p2.h * 0.85) - 10;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Shaded gap region
      const gapPxL = midE2 - (deltaT / maxE) * (p2.w * 0.45);
      const gapPxR = midE2 + (deltaT / maxE) * (p2.w * 0.45);
      ctx.fillStyle = "rgba(168, 85, 247, 0.12)";
      ctx.fillRect(gapPxL, p2.y + 20, gapPxR - gapPxL, p2.h - 35);
      ctx.fillStyle = "#c084fc"; ctx.font = "10px Inter";
      ctx.fillText("2Δ Gap", midE2 - 16, p2.y + p2.h * 0.45);

      // --- SUBPLOT 3: GIAEVER TUNNELING CONDUCTANCE dI/dV ---
      const p3 = { x: 35 + (subW + 20) * 2, y: 35, w: subW, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(p3.x, p3.y, p3.w, p3.h);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText("Giaever Tunneling Conductance dI/dV", p3.x, p3.y - 12);

      const midV3 = p3.x + p3.w * 0.5;
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.2;
      for (let i = 0; i <= 80; i++) {
        const eV_val = -maxE + (2 * maxE * i) / 80;
        const absV = Math.abs(eV_val);
        const cond = absV > deltaT ? absV / Math.sqrt(absV * absV - deltaT * deltaT + gamma * gamma) : 0.05;
        const px = midV3 + (eV_val / maxE) * (p3.w * 0.45);
        const py = p3.y + p3.h - Math.min(3.5, cond) / 3.8 * (p3.h * 0.85) - 10;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Readout Dashboard
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(p1.x, p1.y + p1.h - 50, w - 70, 45);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(p1.x, p1.y + p1.h - 50, w - 70, 45);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`T/T_c = ${tRatio.toFixed(2)}  |  Δ(0) = ${delta0.toFixed(2)} meV  |  2Δ(0)/k_B T_c = 3.53 (BCS Universal)`, p1.x + 15, p1.y + p1.h - 30);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Superconducting Gap Δ(T) = ${deltaT.toFixed(3)} meV  (Tunneling Threshold eV = ±Δ)`, p1.x + 15, p1.y + p1.h - 12);
    }
  },

  // 12. Josephson Effects, Shapiro Steps & DC SQUID Quantum Interference
  "ssp2-josephson-squid-sim": {
    title: "Josephson Junctions, Shapiro Voltage Steps & DC SQUID Interference",
    desc: "Rigorous RCSJ model and macroscopic phase difference dynamics. Visualizes DC Josephson supercurrent I = I_c sin(ϕ), microwave-induced Shapiro steps V_n = n ħω/2e, and DC SQUID flux modulation.",
    isAnimated: true,
    controls: [
      { id: "opMode", label: "Operation Mode", min: 0, max: 2, step: 1, value: 2 }, // 0: DC Josephson, 1: AC Shapiro Steps, 2: DC SQUID
      { id: "fluxPhi", label: "Magnetic Flux Φ / Φ₀", min: 0.0, max: 4.0, step: 0.1, value: 1.2 },
      { id: "biasCurrent", label: "Bias Current I / I_c", min: 0.0, max: 3.0, step: 0.1, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const mode = vals.opMode !== undefined ? Math.round(vals.opMode) : 2;
      const fluxRatio = vals.fluxPhi !== undefined ? vals.fluxPhi : 1.2;
      const biasI = vals.biasCurrent !== undefined ? vals.biasCurrent : 1.5;

      const Ic = 1.0; // mA
      const Phi0 = 2.0678e-15; // Wb

      // Split canvas: Left is Physical Device / Loop; Right is Characteristic Curve
      const splitX = Math.floor(w * 0.48);

      // --- LEFT PLOT: DEVICE SCHEMATIC ---
      const devBox = { x: 35, y: 35, w: splitX - 55, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(devBox.x, devBox.y, devBox.w, devBox.h);

      if (mode === 2) {
        // DC SQUID: Superconducting ring with 2 Josephson junctions
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
        ctx.fillText("DC SQUID: Two Junctions Interrupted Loop", devBox.x, devBox.y - 12);

        const ringCx = devBox.x + devBox.w * 0.5;
        const ringCy = devBox.y + devBox.h * 0.45;
        const ringRad = 65;

        // Superconducting ring
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 14;
        ctx.beginPath(); ctx.arc(ringCx, ringCy, ringRad, 0, 2 * Math.PI); ctx.stroke();

        // Junction gaps (top and bottom)
        ctx.fillStyle = "#050811";
        ctx.fillRect(ringCx - 14, ringCy - ringRad - 10, 28, 20); // Top junction J1
        ctx.fillRect(ringCx - 14, ringCy + ringRad - 10, 28, 20); // Bottom junction J2

        // Barrier insulators (orange)
        ctx.fillStyle = "#f59e0b";
        ctx.fillRect(ringCx - 4, ringCy - ringRad - 8, 8, 16);
        ctx.fillRect(ringCx - 4, ringCy + ringRad - 8, 8, 16);

        ctx.fillStyle = "#f59e0b"; ctx.font = "10px Inter";
        ctx.fillText("J₁ (Barrier)", ringCx - 26, ringCy - ringRad - 14);
        ctx.fillText("J₂ (Barrier)", ringCx - 26, ringCy + ringRad + 24);

        // Magnetic Flux thread in center
        ctx.fillStyle = "rgba(168, 85, 247, 0.2)";
        ctx.beginPath(); ctx.arc(ringCx, ringCy, ringRad * 0.65, 0, 2 * Math.PI); ctx.fill();
        ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2; ctx.stroke();

        ctx.fillStyle = "#c084fc"; ctx.font = "bold 11px Inter";
        ctx.fillText(`Threaded Flux Φ = ${fluxRatio.toFixed(2)} Φ₀`, ringCx - 60, ringCy + 4);

        // Animated current loops
        const circulatingI = Math.sin(Math.PI * fluxRatio);
        const flowT = time * 3.0;
        ctx.fillStyle = "#10b981";
        for (let a = 0; a < 6; a++) {
          const ang = a * (Math.PI / 3) + flowT;
          const ax = ringCx + ringRad * Math.cos(ang);
          const ay = ringCy + ringRad * Math.sin(ang);
          ctx.beginPath(); ctx.arc(ax, ay, 3, 0, 2 * Math.PI); ctx.fill();
        }
      } else {
        // Single Josephson Junction
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
        ctx.fillText(mode === 0 ? "DC Josephson Effect: Supercurrent I = I_c sin(ϕ)" : "AC Shapiro Effect: Microwave Quantized Voltage Steps", devBox.x, devBox.y - 12);

        const jx = devBox.x + devBox.w * 0.5 - 60;
        const jy = devBox.y + devBox.h * 0.35;
        // Electrode 1
        ctx.fillStyle = "rgba(56, 189, 248, 0.3)"; ctx.fillRect(jx - 40, jy, 40, 50);
        ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(jx - 40, jy, 40, 50);
        // Insulator
        ctx.fillStyle = "#f59e0b"; ctx.fillRect(jx, jy, 16, 50);
        // Electrode 2
        ctx.fillStyle = "rgba(56, 189, 248, 0.3)"; ctx.fillRect(jx + 16, jy, 40, 50);
        ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(jx + 16, jy, 40, 50);

        ctx.fillStyle = "#f1f5f9"; ctx.font = "11px Inter";
        ctx.fillText("Superconductor", jx - 45, jy - 10);
        ctx.fillText("Insulator ~1nm", jx - 12, jy + 70);
      }

      // --- RIGHT PLOT: QUANTUM INTERFERENCE / CHARACTERISTIC CURVE ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      if (mode === 2) {
        // SQUID Interference Pattern: I_max(Phi) = 2 * Ic * |cos(pi * Phi / Phi0)|
        ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
        ctx.fillText("SQUID Critical Current Modulation: I_c(Φ) = 2I_c |cos(πΦ/Φ₀)|", plotR.x, plotR.y - 12);

        const maxPhi = 4.0;
        ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.4;
        for (let i = 0; i <= 80; i++) {
          const phiVal = (i / 80) * maxPhi;
          const iMaxVal = 2 * Ic * Math.abs(Math.cos(Math.PI * phiVal));
          const px = plotR.x + (phiVal / maxPhi) * plotR.w;
          const py = plotR.y + plotR.h - (iMaxVal / (2.2 * Ic)) * (plotR.h * 0.8) - 15;
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Operating dot
        const currImax = 2 * Ic * Math.abs(Math.cos(Math.PI * fluxRatio));
        const curPx = plotR.x + (fluxRatio / maxPhi) * plotR.w;
        const curPy = plotR.y + plotR.h - (currImax / (2.2 * Ic)) * (plotR.h * 0.8) - 15;
        ctx.beginPath(); ctx.arc(curPx, curPy, 6, 0, 2 * Math.PI);
        ctx.fillStyle = "#10b981"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

        // Flux ticks
        for (let n = 0; n <= 4; n++) {
          const tx = plotR.x + (n / maxPhi) * plotR.w;
          ctx.strokeStyle = "#334155"; ctx.beginPath(); ctx.moveTo(tx, plotR.y + plotR.h - 5); ctx.lineTo(tx, plotR.y + plotR.h); ctx.stroke();
          ctx.fillStyle = "#64748b"; ctx.font = "9px Inter"; ctx.fillText(`${n}Φ₀`, tx - 8, plotR.y + plotR.h + 12);
        }
      } else if (mode === 1) {
        // Shapiro Voltage Steps: I-V curve with steps at V_n = n * hf / 2e
        ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
        ctx.fillText("Shapiro Steps I-V Curve: Quantized V_n = n ħω / 2e", plotR.x, plotR.y - 12);

        // Step staircase
        ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.2;
        const vStepW = plotR.w / 5;
        ctx.moveTo(plotR.x + 10, plotR.y + plotR.h - 15);
        for (let n = 0; n <= 4; n++) {
          const vx = plotR.x + (n + 0.5) * vStepW;
          const vy = plotR.y + plotR.h - (n + 1) * (plotR.h * 0.18) - 10;
          ctx.lineTo(vx, vy);
          ctx.lineTo(vx + vStepW * 0.8, vy);
        }
        ctx.stroke();

        ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
        ctx.fillText("Voltage Standards (Metrology)", plotR.x + 20, plotR.y + 30);
      } else {
        // DC Josephson I = Ic sin(phi)
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
        ctx.fillText("Current-Phase Relation: I(ϕ) = I_c sin(ϕ)", plotR.x, plotR.y - 12);

        ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.2;
        for (let i = 0; i <= 60; i++) {
          const phiVal = -Math.PI + (2 * Math.PI * i) / 60;
          const ival = Ic * Math.sin(phiVal);
          const px = plotR.x + (i / 60) * plotR.w;
          const py = plotR.y + plotR.h * 0.5 - (ival / 1.2) * (plotR.h * 0.4);
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Telemetry info panel
      const bY = plotR.y + plotR.h - 55;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, bY, plotR.w - 20, 48);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, bY, plotR.w - 20, 48);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Flux Φ = ${fluxRatio.toFixed(2)} Φ₀  |  I_c0 = ${Ic.toFixed(1)} mA`, plotR.x + 20, bY + 18);
      const curMaxI = 2 * Ic * Math.abs(Math.cos(Math.PI * fluxRatio));
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Maximum Interference Supercurrent: ${curMaxI.toFixed(3)} mA`, plotR.x + 20, bY + 36);
    }
  },

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

// Simulation Engine Adapter for Open STEM Library App Controller
window.SimulationEngine = window.SimulationEngine || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = "";

  const simConfig = (window.SSP2_SIMS && window.SSP2_SIMS[simType]) ||
                    (window.PLASMA_SIMS && window.PLASMA_SIMS[simType]) ||
                    (window.ASTRO_SIMS && window.ASTRO_SIMS[simType]) ||
                    (window.QM2_SIMS && window.QM2_SIMS[simType]) ||
                    (window.SSP_SIMS && window.SSP_SIMS[simType]) ||
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
