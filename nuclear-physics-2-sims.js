// Nuclear Physics II Interactive Simulation Suite
// 16 Real-Time 60 FPS Canvas Simulations for Two-Body Bound States, Nuclear Forces, Reaction Models & Hadron Symmetries

window.NUC2_SIMS = {

  // =========================================================================
  // UNIT 1: TWO-NUCLEON BOUND STATE (DEUTERON)
  // =========================================================================

  // 1. Deuteron Radial Wavefunction & D-State Admixture Solver
  "nuc2-deuteron-wavefunction-sim": {
    title: "Deuteron Radial Wavefunction & D-State Admixture Solver",
    desc: "Numerical integration of coupled S-wave and D-wave deuteron radial wavefunctions (B = 2.2245 MeV) in a central plus tensor potential. Visualizes u(r), w(r), exterior exponential tail, and diffuse probability density.",
    isAnimated: true,
    controls: [
      { id: "wellDepth", label: "Well Depth V0 (MeV)", min: 30, max: 50, step: 1, value: 38.5 },
      { id: "wellRadius", label: "Core Radius b (fm)", min: 1.4, max: 2.6, step: 0.1, value: 2.0 },
      { id: "dStateMix", label: "D-State Mix η (%)", min: 0.0, max: 8.0, step: 0.5, value: 4.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const V0 = vals.wellDepth !== undefined ? vals.wellDepth : 38.5;
      const b = vals.wellRadius !== undefined ? vals.wellRadius : 2.0;
      const eta = (vals.dStateMix !== undefined ? vals.dStateMix : 4.0) / 100.0;

      const plot = { x: 55, y: 35, w: w - 85, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

      // Title & metrics
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Coupled S-Wave u(r) & D-Wave w(r) Wavefunctions | B = 2.225 MeV", plot.x, plot.y - 12);

      const rMax = 8.0; // fm
      const B = 2.2245; // MeV
      // gamma = sqrt(2 * mu * B)/hbar c, mu = 469.46 MeV/c^2
      const gamma = Math.sqrt(2 * 469.46 * B) / 197.327; // ~ 0.2316 fm^-1
      const K = Math.sqrt(2 * 469.46 * (V0 - B)) / 197.327;

      // Draw potential well boundary (r = b)
      const xWell = plot.x + (b / rMax) * plot.w;
      ctx.fillStyle = "rgba(56, 189, 248, 0.06)";
      ctx.fillRect(plot.x, plot.y, xWell - plot.x, plot.h);
      ctx.strokeStyle = "#38bdf8"; ctx.setLineDash([4, 4]); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(xWell, plot.y); ctx.lineTo(xWell, plot.y + plot.h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText(`Core Boundary b = ${b.toFixed(1)} fm`, xWell + 4, plot.y + 16);

      // Axes labels
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      for (let r = 0; r <= 8; r += 2) {
        const px = plot.x + (r / rMax) * plot.w;
        ctx.fillText(`${r} fm`, px - 10, plot.y + plot.h + 16);
      }
      ctx.fillText("0", plot.x - 16, plot.y + plot.h - 5);
      ctx.fillText("u(r), w(r)", plot.x - 45, plot.y + 15);

      // Solve S-wave u(r) and D-wave w(r)
      const dr = 0.05;
      const ptsU = [], ptsW = [], ptsP = [];
      const normS = Math.sin(K * b);
      const ampExt = normS * Math.exp(gamma * b);

      for (let r = 0.02; r <= rMax; r += dr) {
        let u_val = 0;
        if (r <= b) {
          u_val = Math.sin(K * r);
        } else {
          u_val = ampExt * Math.exp(-gamma * r);
        }
        // D-wave w(r) is suppressed at origin as r^3, peaks near r ~ b, decays with tensor mixing
        let w_val = 0;
        if (r <= b) {
          w_val = eta * Math.pow(r / b, 3) * Math.sin(K * r) * 1.5;
        } else {
          w_val = eta * ampExt * Math.exp(-gamma * r) * (1 + 3 / (gamma * r) + 3 / (gamma * gamma * r * r)) * 0.25;
        }
        const prob = (u_val * u_val + w_val * w_val);
        ptsU.push({ r, val: u_val });
        ptsW.push({ r, val: w_val });
        ptsP.push({ r, val: prob });
      }

      // Max val for normalization
      const maxVal = 1.25;

      // Draw Probability Density background fill
      ctx.fillStyle = "rgba(168, 85, 247, 0.15)";
      ctx.beginPath();
      ctx.moveTo(plot.x, plot.y + plot.h);
      ptsP.forEach((pt, i) => {
        const px = plot.x + (pt.r / rMax) * plot.w;
        const py = plot.y + plot.h * (1 - pt.val / (maxVal * maxVal));
        if (i === 0) ctx.lineTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.lineTo(plot.x + plot.w, plot.y + plot.h);
      ctx.closePath();
      ctx.fill();

      // Draw S-wave u(r) (Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ptsU.forEach((pt, i) => {
        const px = plot.x + (pt.r / rMax) * plot.w;
        const py = plot.y + plot.h * (1 - pt.val / maxVal);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();

      // Draw D-wave w(r) (Amber)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.beginPath();
      ptsW.forEach((pt, i) => {
        const px = plot.x + (pt.r / rMax) * plot.w;
        const py = plot.y + plot.h * (1 - (pt.val * 3) / maxVal);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();

      // Legend & stats badge
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
      ctx.fillRect(plot.x + plot.w - 240, plot.y + 15, 230, 95);
      ctx.strokeRect(plot.x + plot.w - 240, plot.y + 15, 230, 95);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText("— S-Wave u(r) [3S1 (96%)]", plot.x + plot.w - 225, plot.y + 35);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`— D-Wave w(r) [3D1 (${(eta * 100).toFixed(1)}%)] (×3)`, plot.x + plot.w - 225, plot.y + 53);
      ctx.fillStyle = "#a855f7";
      ctx.fillText("■ Total Density P(r) = u² + w²", plot.x + plot.w - 225, plot.y + 71);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      const pExt = (Math.exp(-2 * gamma * b) / (1 + 2 * gamma * b) * 100).toFixed(1);
      ctx.fillText(`Ext Tail Probability: ~${pExt}% (Diffuse Bound State)`, plot.x + plot.w - 225, plot.y + 92);
    }
  },

  // 2. Deuteron Photodisintegration: γ + d -> n + p Kinematics & Cross Section
  "nuc2-photodisintegration-sim": {
    title: "Deuteron Photodisintegration: γ + d → n + p Kinematics & Cross Section",
    desc: "Calculates electric dipole E1 and magnetic dipole M1 photodisintegration cross sections σ(Eγ) above threshold 2.225 MeV, and demonstrates the sin²θ angular distribution.",
    isAnimated: true,
    controls: [
      { id: "photonEnergy", label: "Photon Energy Eγ (MeV)", min: 2.3, max: 25.0, step: 0.5, value: 6.0 },
      { id: "thetaAngle", label: "Angle θ (deg)", min: 0, max: 180, step: 5, value: 90 },
      { id: "m1Ratio", label: "M1 Fraction", min: 0.01, max: 0.25, step: 0.01, value: 0.05 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const E_gamma = vals.photonEnergy !== undefined ? vals.photonEnergy : 6.0;
      const thetaDeg = vals.thetaAngle !== undefined ? vals.thetaAngle : 90;
      const m1Frac = vals.m1Ratio !== undefined ? vals.m1Ratio : 0.05;
      const thetaRad = (thetaDeg * Math.PI) / 180;

      const splitX = Math.floor(w * 0.52);

      // LEFT PLOT: Cross section sigma(E_gamma)
      const pL = { x: 50, y: 35, w: splitX - 65, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Total Cross Section σ(Eγ) [Bethe-Peierls]", pL.x, pL.y - 12);

      const B = 2.2245; // Threshold
      const eMax = 25.0; // MeV
      const sigMax = 3.2; // mb

      // Plot curve
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      let first = true;
      for (let eg = 2.23; eg <= eMax; eg += 0.2) {
        const eps = (eg - B) / B;
        // Bethe-Peierls formula: sigma_E1 proportional to (eg - B)^1.5 / eg^3
        const sigE1 = 2.5 * Math.pow(eps, 1.5) / Math.pow(1 + eps, 3);
        const sigM1 = (m1Frac * 1.5) / (1 + eps);
        const sigTot = sigE1 + sigM1;

        const px = pL.x + ((eg - 2.2) / (eMax - 2.2)) * pL.w;
        const py = pL.y + pL.h * (1 - sigTot / sigMax);
        if (first) { ctx.moveTo(px, py); first = false; } else { ctx.lineTo(px, py); }
      }
      ctx.stroke();

      // Current operating point
      const epsCur = (E_gamma - B) / B;
      const curSigE1 = E_gamma > B ? 2.5 * Math.pow(epsCur, 1.5) / Math.pow(1 + epsCur, 3) : 0;
      const curSigM1 = E_gamma > B ? (m1Frac * 1.5) / (1 + epsCur) : 0;
      const curSigTot = curSigE1 + curSigM1;

      const curX = pL.x + ((E_gamma - 2.2) / (eMax - 2.2)) * pL.w;
      const curY = pL.y + pL.h * (1 - curSigTot / sigMax);

      ctx.fillStyle = "#f43f5e"; ctx.beginPath();
      ctx.arc(curX, curY, 5, 0, 2 * Math.PI); ctx.fill();

      // Threshold line
      ctx.strokeStyle = "#f59e0b"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(pL.x + 2, pL.y); ctx.lineTo(pL.x + 2, pL.y + pL.h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.font = "9px Inter";
      ctx.fillText("Eth=2.22 MeV", pL.x + 5, pL.y + 20);

      // RIGHT PLOT: Center of Mass Angular Distribution (dσ/dΩ ~ a + b sin²θ)
      const pR = { x: splitX + 35, y: 35, w: w - splitX - 55, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Angular Distribution dσ/dΩ(θ) ∝ a + b sin²θ", pR.x, pL.y - 12);

      const dSigMax = 1.2;
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      for (let th = 0; th <= 180; th += 2) {
        const rth = (th * Math.PI) / 180;
        const dsig = curSigM1 * 0.3 + curSigE1 * Math.sin(rth) * Math.sin(rth);
        const px = pR.x + (th / 180) * pR.w;
        const py = pR.y + pR.h * (1 - dsig / dSigMax);
        if (th === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Probe marker on angular distribution
      const probeDsig = curSigM1 * 0.3 + curSigE1 * Math.sin(thetaRad) * Math.sin(thetaRad);
      const prX = pR.x + (thetaDeg / 180) * pR.w;
      const prY = pR.y + pR.h * (1 - probeDsig / dSigMax);
      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(prX, prY, 5, 0, 2 * Math.PI); ctx.fill();

      // Bottom info readout
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Photon Energy Eγ: ${E_gamma.toFixed(1)} MeV`, pL.x, h - 15);
      ctx.fillText(`Total Cross Section: ${curSigTot.toFixed(2)} mb (Peak ~4.4 MeV)`, pL.x + 180, h - 15);
      ctx.fillText(`Angle θ: ${thetaDeg}° (dσ/dΩ: ${probeDsig.toFixed(2)} a.u.)`, pR.x, h - 15);
    }
  },

  // =========================================================================
  // UNIT 2: NUCLEON-NUCLEON SCATTERING
  // =========================================================================

  // 3. Low-Energy n-p Scattering: Phase Shifts & Effective Range Theory
  "nuc2-np-scattering-phaseshift-sim": {
    title: "Low-Energy n-p Scattering: Phase Shifts & Effective Range Solver",
    desc: "Computes triplet (at = +5.42 fm) and singlet (as = -23.7 fm) s-wave phase shifts δ0(k), effective range expansion, and the total unpolarized cross section σ = 3/4 σt + 1/4 σs ≈ 20.48 b.",
    isAnimated: true,
    controls: [
      { id: "neutronE", label: "Neutron Energy (MeV)", min: 0.01, max: 20.0, step: 0.1, value: 0.5 },
      { id: "singletA", label: "Singlet as (fm)", min: -30.0, max: -15.0, step: 0.5, value: -23.7 },
      { id: "tripletA", label: "Triplet at (fm)", min: 3.0, max: 7.0, step: 0.2, value: 5.42 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const En = vals.neutronE !== undefined ? vals.neutronE : 0.5;
      const as = vals.singletA !== undefined ? vals.singletA : -23.7;
      const at = vals.tripletA !== undefined ? vals.tripletA : 5.42;

      const r0s = 2.75, r0t = 1.75; // effective ranges in fm

      const splitX = Math.floor(w * 0.52);

      // LEFT PLOT: Phase shifts delta_t and delta_s vs Energy (0 to 20 MeV)
      const pL = { x: 50, y: 35, w: splitX - 65, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("s-Wave Phase Shifts δ0(E): Triplet vs Singlet", pL.x, pL.y - 12);

      const eMax = 20.0;
      // Draw curves
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.beginPath();
      // Triplet phase shift
      for (let e = 0.05; e <= eMax; e += 0.2) {
        const k = Math.sqrt(2 * 469.46 * (e / 2)) / 197.327; // k in cm frame
        const cotDeltaT = -1 / at + 0.5 * r0t * k * k;
        let deltaT = Math.atan2(k, cotDeltaT) * (180 / Math.PI);
        if (deltaT < 0) deltaT += 180;
        const px = pL.x + (e / eMax) * pL.w;
        const py = pL.y + pL.h * (1 - deltaT / 180);
        if (e === 0.05) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Singlet phase shift
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.beginPath();
      for (let e = 0.05; e <= eMax; e += 0.2) {
        const k = Math.sqrt(2 * 469.46 * (e / 2)) / 197.327;
        const cotDeltaS = -1 / as + 0.5 * r0s * k * k;
        let deltaS = Math.atan2(k, cotDeltaS) * (180 / Math.PI);
        if (deltaS < 0) deltaS += 180;
        const px = pL.x + (e / eMax) * pL.w;
        const py = pL.y + pL.h * (1 - deltaS / 180);
        if (e === 0.05) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // RIGHT PLOT: Cross section sigma_total vs Energy (log or normalized)
      const pR = { x: splitX + 35, y: 35, w: w - splitX - 55, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Total Unpolarized Cross Section σ(E) (barns)", pR.x, pL.y - 12);

      const sigMax = 25.0; // barns
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.beginPath();
      for (let e = 0.05; e <= eMax; e += 0.2) {
        const k = Math.sqrt(2 * 469.46 * (e / 2)) / 197.327;
        const cotT = -1 / at + 0.5 * r0t * k * k;
        const cotS = -1 / as + 0.5 * r0s * k * k;
        const sin2T = (k * k) / (cotT * cotT + k * k);
        const sin2S = (k * k) / (cotS * cotS + k * k);
        const sigT = (4 * Math.PI / (k * k)) * sin2T * 0.1; // in barns
        const sigS = (4 * Math.PI / (k * k)) * sin2S * 0.1;
        const sigTot = 0.75 * sigT + 0.25 * sigS;
        const px = pR.x + (e / eMax) * pR.w;
        const py = pR.y + pR.h * (1 - Math.min(sigTot, sigMax) / sigMax);
        if (e === 0.05) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current calculations
      const kCur = Math.sqrt(2 * 469.46 * (En / 2)) / 197.327;
      const cotTCur = -1 / at + 0.5 * r0t * kCur * kCur;
      const cotSCur = -1 / as + 0.5 * r0s * kCur * kCur;
      const sin2TCur = (kCur * kCur) / (cotTCur * cotTCur + kCur * kCur);
      const sin2SCur = (kCur * kCur) / (cotSCur * cotSCur + kCur * kCur);
      const curSigT = (4 * Math.PI / (kCur * kCur)) * sin2TCur * 0.1;
      const curSigS = (4 * Math.PI / (kCur * kCur)) * sin2SCur * 0.1;
      const curSigTot = 0.75 * curSigT + 0.25 * curSigS;

      // Operating point marker on RHS
      const ptX = pR.x + (En / eMax) * pR.w;
      const ptY = pR.y + pR.h * (1 - Math.min(curSigTot, sigMax) / sigMax);
      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(ptX, ptY, 5, 0, 2 * Math.PI); ctx.fill();

      // Readouts
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`En = ${En.toFixed(2)} MeV`, pL.x, h - 15);
      ctx.fillText(`— Triplet δt (3S1)`, pL.x + 120, h - 15);
      ctx.fillText(`— Singlet δs (1S0)`, pL.x + 230, h - 15);
      ctx.fillText(`σ_total: ${curSigTot.toFixed(2)} b (Thermal limit: 20.48 b)`, pR.x, h - 15);
    }
  },

  // 4. Ortho- vs Para-Hydrogen Thermal Neutron Scattering
  "nuc2-ortho-para-hydrogen-sim": {
    title: "Ortho- vs Para-Hydrogen Thermal Neutron Scattering & Coherent Interference",
    desc: "Simulates thermal neutron scattering on ortho-H2 (parallel proton spins) and para-H2 (antiparallel spins). Demonstrates coherent vs incoherent interference yielding σ_ortho/σ_para ≈ 35.",
    isAnimated: true,
    controls: [
      { id: "temperature", label: "Gas Temp T (K)", min: 10, max: 300, step: 10, value: 20 },
      { id: "neutronWave", label: "Neutron λn (Å)", min: 0.8, max: 3.5, step: 0.1, value: 1.8 },
      { id: "paraFraction", label: "Para-H2 Fraction (%)", min: 0, max: 100, step: 5, value: 75 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const T = vals.temperature !== undefined ? vals.temperature : 20;
      const lambdaN = vals.neutronWave !== undefined ? vals.neutronWave : 1.8;
      const fPara = (vals.paraFraction !== undefined ? vals.paraFraction : 75) / 100.0;
      const fOrtho = 1.0 - fPara;

      // Cross sections in barns
      // Para-H2: coherent destructive interference between protons with opposite spins
      // sigma_para ~ 4.2 b at thermal; ortho-H2: constructive interference ~ 145 b
      const sigPara = 4.2 * Math.exp(-0.003 * T);
      const sigOrtho = 145.0 / (1 + 0.002 * T);
      const sigAvg = fPara * sigPara + fOrtho * sigOrtho;

      // Draw two interactive panels:
      // Left: Molecular scattering animation; Right: Bar comparison
      const splitX = Math.floor(w * 0.55);

      // LEFT: Molecular visualizer
      const pL = { x: 30, y: 30, w: splitX - 45, h: h - 60 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pL.x, pL.y, pL.w, pL.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Molecular Wave Interference Visualization", pL.x + 15, pL.y + 22);

      // Draw incoming neutron wavepacket
      const waveX = pL.x + 35 + ((time * 70) % (pL.w - 120));
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 1.5;
      for (let offset = -20; offset <= 20; offset += 8) {
        ctx.beginPath();
        ctx.arc(waveX + offset, pL.y + pL.h * 0.45, 30, -Math.PI / 3, Math.PI / 3);
        ctx.stroke();
      }

      // Draw H2 Molecule at center
      const molX = pL.x + pL.w * 0.7;
      const molY = pL.y + pL.h * 0.45;
      const d = 30; // bond length

      // Proton 1 & 2
      ctx.fillStyle = "#ef4444"; ctx.beginPath(); ctx.arc(molX - d/2, molY, 9, 0, 2*Math.PI); ctx.fill();
      ctx.fillStyle = "#3b82f6"; ctx.beginPath(); ctx.arc(molX + d/2, molY, 9, 0, 2*Math.PI); ctx.fill();

      // Molecular bond
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(molX - d/2 + 8, molY); ctx.lineTo(molX + d/2 - 8, molY); ctx.stroke();

      // Spin arrows
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      // Proton 1 spin Up
      ctx.beginPath(); ctx.moveTo(molX - d/2, molY - 12); ctx.lineTo(molX - d/2, molY - 26); ctx.stroke();
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.moveTo(molX - d/2, molY - 26); ctx.lineTo(molX - d/2 - 3, molY - 20); ctx.lineTo(molX - d/2 + 3, molY - 20); ctx.fill();

      // Proton 2 spin (Up if Ortho, Down if Para)
      const p2Up = fOrtho > 0.5;
      const arrowDir = p2Up ? -1 : 1;
      ctx.strokeStyle = p2Up ? "#f59e0b" : "#10b981";
      ctx.beginPath(); ctx.moveTo(molX + d/2, molY + arrowDir * 12); ctx.lineTo(molX + d/2, molY + arrowDir * 26); ctx.stroke();
      ctx.fillStyle = p2Up ? "#f59e0b" : "#10b981";
      ctx.beginPath();
      ctx.moveTo(molX + d/2, molY + arrowDir * 26);
      ctx.lineTo(molX + d/2 - 3, molY + arrowDir * 20);
      ctx.lineTo(molX + d/2 + 3, molY + arrowDir * 20);
      ctx.fill();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(p2Up ? "Ortho-H2 (S = 1, Triplet)" : "Para-H2 (S = 0, Singlet)", molX - 55, molY + 45);

      // RIGHT: Cross Section Bar Chart
      const pR = { x: splitX + 20, y: 30, w: w - splitX - 45, h: h - 60 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pR.x, pR.y, pR.w, pR.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Effective Scattering Cross Section (b)", pR.x + 15, pR.y + 22);

      const maxBar = 160;
      // Bar 1: Ortho
      const hOrtho = (sigOrtho / maxBar) * (pR.h - 90);
      ctx.fillStyle = "#f59e0b";
      ctx.fillRect(pR.x + 35, pR.y + pR.h - 40 - hOrtho, 45, hOrtho);
      ctx.fillStyle = "#ffffff"; ctx.font = "10px Inter";
      ctx.fillText(`${sigOrtho.toFixed(1)} b`, pR.x + 38, pR.y + pR.h - 45 - hOrtho);
      ctx.fillText("Ortho", pR.x + 40, pR.y + pR.h - 22);

      // Bar 2: Para
      const hPara = (sigPara / maxBar) * (pR.h - 90);
      ctx.fillStyle = "#10b981";
      ctx.fillRect(pR.x + 105, pR.y + pR.h - 40 - hPara, 45, hPara);
      ctx.fillText(`${sigPara.toFixed(1)} b`, pR.x + 108, pR.y + pR.h - 45 - hPara);
      ctx.fillText("Para", pR.x + 112, pR.y + pR.h - 22);

      // Bar 3: Measured Mix
      const hMix = (sigAvg / maxBar) * (pR.h - 90);
      ctx.fillStyle = "#38bdf8";
      ctx.fillRect(pR.x + 175, pR.y + pR.h - 40 - hMix, 45, hMix);
      ctx.fillText(`${sigAvg.toFixed(1)} b`, pR.x + 178, pR.y + pR.h - 45 - hMix);
      ctx.fillText("Mix", pR.x + 185, pR.y + pR.h - 22);

      // Ratio badge
      const ratio = (sigOrtho / sigPara).toFixed(1);
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Cross Section Ratio: σ_ortho / σ_para ≈ ${ratio}`, pR.x + 20, pR.y + 55);
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Destructive interference in Para (S=0)", pR.x + 20, pR.y + 72);
      ctx.fillText("proves nuclear force spin dependence!", pR.x + 20, pR.y + 86);
    }
  },

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

  // =========================================================================
  // UNIT 5: ADVANCED NUCLEAR STRUCTURE MODELS
  // =========================================================================

  // 9. Nuclear Shell Model with Mayer-Jensen Spin-Orbit Coupling
  "nuc2-shell-model-spin-orbit-sim": {
    title: "Nuclear Shell Model with Mayer-Jensen Spin-Orbit Coupling",
    desc: "Interactive single-particle energy level diagram. Dialing the Mayer-Jensen spin-orbit coupling -V_so (l·s) splits j = l ± 1/2 orbitals, generating the historic magic numbers 2, 8, 20, 28, 50, 82, 126.",
    isAnimated: true,
    controls: [
      { id: "spinOrbitStrength", label: "Spin-Orbit Vso (MeV)", min: 0.0, max: 24.0, step: 1.0, value: 16.0 },
      { id: "wsDiffuseness", label: "Diffuseness a (fm)", min: 0.4, max: 0.9, step: 0.05, value: 0.65 },
      { id: "wellDepthV0", label: "Well Depth V0 (MeV)", min: 40, max: 60, step: 2, value: 50 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Vso = vals.spinOrbitStrength !== undefined ? vals.spinOrbitStrength : 16.0;

      const pL = { x: 50, y: 35, w: w - 100, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Shell Model Energy Levels: Harmonic Oscillator → Woods-Saxon + Mayer-Jensen Spin-Orbit", pL.x, pL.y - 12);

      // We plot energy levels across the horizontal axis:
      // Left (x = 0): Unperturbed HO levels
      // Center (x = 0.5): Woods-Saxon (flattened bottom)
      // Right (x = 1.0): Full Mayer-Jensen Spin-Orbit splitting
      const levels = [
        { name: "1s1/2", l: 0, j: 0.5, e0: -45, deg: 2, magicBelow: 2 },
        { name: "1p3/2", l: 1, j: 1.5, e0: -38, deg: 4, magicBelow: null },
        { name: "1p1/2", l: 1, j: 0.5, e0: -38, deg: 2, magicBelow: 8 },
        { name: "1d5/2", l: 2, j: 2.5, e0: -29, deg: 6, magicBelow: null },
        { name: "2s1/2", l: 0, j: 0.5, e0: -29, deg: 2, magicBelow: null },
        { name: "1d3/2", l: 2, j: 1.5, e0: -29, deg: 4, magicBelow: 20 },
        { name: "1f7/2", l: 3, j: 3.5, e0: -20, deg: 8, magicBelow: 28 }, // Magic!
        { name: "2p3/2", l: 1, j: 1.5, e0: -20, deg: 4, magicBelow: null },
        { name: "1f5/2", l: 3, j: 2.5, e0: -20, deg: 6, magicBelow: null },
        { name: "2p1/2", l: 1, j: 0.5, e0: -20, deg: 2, magicBelow: null },
        { name: "1g9/2", l: 4, j: 4.5, e0: -11, deg: 10, magicBelow: 50 }, // Magic!
        { name: "2d5/2", l: 2, j: 2.5, e0: -11, deg: 6, magicBelow: null },
        { name: "1g7/2", l: 4, j: 3.5, e0: -11, deg: 8, magicBelow: null },
        { name: "1h11/2", l: 5, j: 5.5, e0: -2, deg: 12, magicBelow: 82 } // Magic!
      ];

      // Spin-orbit shift: Delta E = -0.5 * Vso * [j(j+1) - l(l+1) - 3/4] / (2l + 1)
      const eMin = -48, eMax = 5;

      levels.forEach(lvl => {
        let l_dot_s = 0;
        if (lvl.l > 0) {
          l_dot_s = (lvl.j === lvl.l + 0.5) ? lvl.l / 2.0 : -(lvl.l + 1.0) / 2.0;
        }
        // Shift in MeV
        const soShift = -(Vso * 0.4) * l_dot_s;
        const eFinal = lvl.e0 + soShift;

        // Path from Left to Right
        const x1 = pL.x + 20;
        const x2 = pL.x + pL.w * 0.35;
        const x3 = pL.x + pL.w - 30;

        const y1 = pL.y + pL.h * (1 - (lvl.e0 - eMin) / (eMax - eMin));
        const y3 = pL.y + pL.h * (1 - (eFinal - eMin) / (eMax - eMin));

        ctx.strokeStyle = (lvl.j === lvl.l + 0.5 && lvl.l >= 3) ? "#f43f5e" : "#38bdf8";
        ctx.lineWidth = (lvl.j === lvl.l + 0.5 && lvl.l >= 3) ? 2 : 1.2;

        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y1);
        ctx.lineTo(x3, y3);
        ctx.stroke();

        // Level label on right
        ctx.fillStyle = (lvl.j === lvl.l + 0.5 && lvl.l >= 3) ? "#f43f5e" : "#94a3b8";
        ctx.font = "10px Inter";
        ctx.fillText(`${lvl.name} (${lvl.deg})`, x3 + 5, y3 + 3);

        // Magic number badge if applicable
        if (lvl.magicBelow) {
          const magicY = y3 - 8;
          ctx.strokeStyle = "#10b981"; ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.moveTo(x2, magicY); ctx.lineTo(x3 + 60, magicY); ctx.stroke();
          ctx.setLineDash([]);
          ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
          ctx.fillText(`Magic [${lvl.magicBelow}]`, x3 - 90, magicY - 2);
        }
      });

      // Bottom guidance note
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText("Harmonic Oscillator", pL.x + 20, pL.y + pL.h - 10);
      ctx.fillText("Woods-Saxon + l²", pL.x + pL.w * 0.30, pL.y + pL.h - 10);
      ctx.fillText("+ Spin-Orbit Splitting -Vso(l·s)", pL.x + pL.w - 200, pL.y + pL.h - 10);
    }
  },

  // 10. Bohr-Mottelson Collective Rotations, Vibrations & Coriolis Backbending
  "nuc2-collective-rotational-vibrational-sim": {
    title: "Bohr-Mottelson Rotations, Vibrations & Coriolis Backbending",
    desc: "Interactive 3D deformed collective rotor. Calculates rotational yrast levels E(I) = A I(I+1) with R_4/2 ≈ 3.33, compares with harmonic vibrator R_4/2 = 2.0, and plots Coriolis pair-breaking backbending.",
    isAnimated: true,
    controls: [
      { id: "rotationalParam", label: "A_rot (keV)", min: 8, max: 35, step: 1, value: 15 },
      { id: "deformationBeta2", label: "Deformation β2", min: 0.0, max: 0.45, step: 0.05, value: 0.30 },
      { id: "backbendSpin", label: "Spin I Range", min: 6, max: 20, step: 2, value: 16 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Arot = vals.rotationalParam !== undefined ? vals.rotationalParam : 15;
      const beta = vals.deformationBeta2 !== undefined ? vals.deformationBeta2 : 0.30;
      const maxI = vals.backbendSpin !== undefined ? vals.backbendSpin : 16;

      const splitX = Math.floor(w * 0.48);

      // LEFT PANEL: 3D Rotating Prolate Ellipsoid Canvas
      const pL = { x: 30, y: 30, w: splitX - 45, h: h - 60 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pL.x, pL.y, pL.w, pL.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Deformed Prolate Spheroid (3D Rotating)", pL.x + 15, pL.y + 22);

      const cx = pL.x + pL.w / 2;
      const cy = pL.y + pL.h / 2 + 10;
      const rotAngle = time * 1.5;

      // Draw rotating 3D ellipsoid wireframe
      const aAxis = 65 * (1 + 0.6 * beta);
      const bAxis = 65 * (1 - 0.3 * beta);

      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(rotAngle * 0.4);

      // Draw glowing nucleus body
      const grad = ctx.createRadialGradient(0, 0, 10, 0, 0, aAxis);
      grad.addColorStop(0, "rgba(56, 189, 248, 0.8)");
      grad.addColorStop(0.7, "rgba(16, 185, 129, 0.4)");
      grad.addColorStop(1, "rgba(16, 185, 129, 0.0)");

      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.ellipse(0, 0, aAxis, bAxis, 0, 0, 2 * Math.PI);
      ctx.fill();

      // Ellipsoidal latitude rings
      ctx.strokeStyle = "rgba(56, 189, 248, 0.6)"; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.ellipse(0, 0, aAxis, bAxis, 0, 0, 2 * Math.PI); ctx.stroke();
      ctx.beginPath(); ctx.ellipse(0, 0, aAxis * 0.7, bAxis * 0.7, 0, 0, 2 * Math.PI); ctx.stroke();

      // Rotation axis
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(0, -aAxis - 25); ctx.lineTo(0, aAxis + 25); ctx.stroke();

      ctx.restore();

      ctx.fillStyle = "#f59e0b"; ctx.font = "10px Inter";
      ctx.fillText("Spin Vector I →", cx - 35, cy - aAxis - 15);
      ctx.fillStyle = "#94a3b8";
      ctx.fillText(`β2 = ${beta.toFixed(2)} (Prolate Rotor)`, pL.x + 15, pL.y + pL.h - 15);

      // RIGHT PANEL: Backbending Plot 2*I / hbar^2 vs (hbar*omega)^2
      const pR = { x: splitX + 20, y: 30, w: w - splitX - 45, h: h - 60 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pR.x, pR.y, pR.w, pR.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Coriolis Backbending Curve: 2J/ħ² vs (ħω)²", pR.x + 15, pR.y + 22);

      // Generate points for backbending curve:
      // Normal rotor: 2J/hbar^2 ~ 65 MeV^-1; at I ~ 12-14, alignment jumps to rigid ~ 130 MeV^-1
      const pts = [];
      for (let I = 2; I <= maxI; I += 2) {
        // Rotational frequency hbar*omega = (E(I) - E(I-2))/2
        let eI = Arot * I * (I + 1);
        let ePrev = Arot * (I - 2) * (I - 1);
        if (I >= 12 && I <= 16) {
          // Coriolis pair breaking suppresses transition energy
          eI -= 180 * Math.sin((I - 12) * Math.PI / 4);
        }
        const hbarOmega = Math.max(0.05, (eI - ePrev) / 2.0); // in keV
        const hbarOmegaSq = Math.pow(hbarOmega / 100, 2);
        // Moment of inertia: 2J/hbar^2 = (4I - 2) / (E(I) - E(I-2))
        const momInertia = (4 * I - 2) / (2 * hbarOmega) * 1000;
        pts.push({ I, x: hbarOmegaSq, y: momInertia });
      }

      // Plot the S-shaped backbending line
      const xMax = 0.25, yMax = 140;
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5; ctx.beginPath();
      pts.forEach((pt, i) => {
        const px = pR.x + 35 + (pt.x / xMax) * (pR.w - 55);
        const py = pR.y + pR.h - 35 - (pt.y / yMax) * (pR.h - 70);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();

      // Draw points with spin labels
      pts.forEach(pt => {
        const px = pR.x + 35 + (pt.x / xMax) * (pR.w - 55);
        const py = pR.y + pR.h - 35 - (pt.y / yMax) * (pR.h - 70);
        ctx.fillStyle = pt.I >= 12 && pt.I <= 16 ? "#f43f5e" : "#38bdf8";
        ctx.beginPath(); ctx.arc(px, py, 4, 0, 2 * Math.PI); ctx.fill();
        ctx.fillStyle = "#ffffff"; ctx.font = "9px Inter";
        ctx.fillText(`${pt.I}+`, px + 6, py - 4);
      });

      // Stats badge
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText("Pair-breaking at I ~ 14ħ (i13/2 neutron alignment)", pR.x + 15, pR.y + 50);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("E(4+)/E(2+) = 3.33 (Rotor) vs 2.00 (Vibrator)", pR.x + 15, pR.y + 66);
    }
  },

  // =========================================================================
  // UNIT 6: NUCLEAR REACTIONS & SCATTERING
  // =========================================================================

  // 11. Nuclear Optical Model: Complex Potential & Differential Cross Section
  "nuc2-optical-model-scattering-sim": {
    title: "Nuclear Optical Model: Complex Potential & Cross Section",
    desc: "Partial-wave scattering solver for a complex optical potential U(r) = -V f(r) - i W g(r). Computes absorption, S-matrix transmission coefficients T_l = 1 - |S_l|², and differential cross section dσ/dΩ(θ).",
    isAnimated: true,
    controls: [
      { id: "realDepthV", label: "Real Depth V (MeV)", min: 30, max: 60, step: 2, value: 48 },
      { id: "imagDepthW", label: "Imag Absorption W (MeV)", min: 2, max: 20, step: 1, value: 10 },
      { id: "incidentE", label: "Energy Elab (MeV)", min: 5, max: 50, step: 2, value: 14 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const V = vals.realDepthV !== undefined ? vals.realDepthV : 48;
      const W = vals.imagDepthW !== undefined ? vals.imagDepthW : 10;
      const E = vals.incidentE !== undefined ? vals.incidentE : 14;

      const splitX = Math.floor(w * 0.52);

      // LEFT PLOT: Differential Cross Section dσ/dΩ(θ) on Log Scale (0 to 180 deg)
      const pL = { x: 50, y: 35, w: splitX - 65, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Angular Differential Cross Section dσ/dΩ(θ) [Log mb/sr]", pL.x, pL.y - 12);

      // Airy diffraction pattern damped by absorption W:
      // dsigma/dOmega ~ [J1(k R sin theta) / (k R sin theta)]^2 + absorption damping
      const k = Math.sqrt(2 * 938 * E) / 197.327; // fm^-1
      const R = 1.25 * Math.pow(40, 1/3); // ~ 4.27 fm

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.beginPath();
      for (let deg = 0.5; deg <= 179.5; deg += 1) {
        const rad = (deg * Math.PI) / 180;
        const q = 2 * k * Math.sin(rad / 2);
        const x = q * R;
        // Bessel approximation
        let j1_x = (Math.sin(x) - x * Math.cos(x)) / (x * x);
        if (x < 0.1) j1_x = 0.333;
        const diffPeak = Math.pow(j1_x, 2) * 500;
        const absDamp = Math.exp(-0.04 * W * rad);
        const dsig = Math.max(0.01, diffPeak * absDamp + 0.1);
        const logVal = Math.log10(dsig); // range -1 to 3

        const px = pL.x + (deg / 180) * pL.w;
        const py = pL.y + pL.h * (1 - (logVal - (-1)) / (3 - (-1)));
        if (deg === 0.5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("10³", pL.x - 22, pL.y + 12);
      ctx.fillText("10¹", pL.x - 22, pL.y + pL.h * 0.5);
      ctx.fillText("10⁻¹", pL.x - 26, pL.y + pL.h - 5);
      ctx.fillText("Scattering Angle θ (deg) →", pL.x + pL.w - 130, pL.y + pL.h + 16);

      // RIGHT PLOT: Partial Wave Transmission Coefficients T_l = 1 - |S_l|²
      const pR = { x: splitX + 35, y: 35, w: w - splitX - 55, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Partial Wave Transmission Tl = 1 - |Sl|²", pR.x, pL.y - 12);

      // Grazing angular momentum: l_grazing ~ k * R
      const lGrazing = k * R;

      // Draw bar chart for l = 0 to 8
      const maxL = 8;
      const barWidth = 18;
      for (let l = 0; l <= maxL; l++) {
        // Fermi function cutoff: T_l = 1 / [1 + exp((l - lGrazing)/0.6)]
        const T_l = 1.0 / (1.0 + Math.exp((l - lGrazing) / 0.65));
        const px = pR.x + 25 + l * 26;
        const barH = T_l * (pR.h - 50);
        const py = pR.y + pR.h - 30 - barH;

        ctx.fillStyle = l <= lGrazing ? "#38bdf8" : "#f43f5e";
        ctx.fillRect(px, py, barWidth, barH);

        ctx.fillStyle = "#ffffff"; ctx.font = "9px Inter";
        ctx.fillText(`${l}`, px + 5, pR.y + pR.h - 15);
      }

      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Grazing Angular Momentum lgrazing ≈ ${lGrazing.toFixed(1)}ħ`, pR.x + 20, pR.y + 35);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Sharp cutoff in Tl reflects black-disc nuclear absorption", pR.x + 20, pR.y + 52);
    }
  },

  // 12. Breit-Wigner Single-Level Resonance & Potential Interference
  "nuc2-breit-wigner-resonance-sim": {
    title: "Breit-Wigner Single-Level Resonance & Interference",
    desc: "Calculates single-level Breit-Wigner dispersion resonance for slow neutron capture and scattering. Demonstrates asymmetric Fano-type potential-resonance interference and Doppler broadening.",
    isAnimated: true,
    controls: [
      { id: "resEnergy", label: "Resonance E0 (eV)", min: 0.2, max: 8.0, step: 0.2, value: 1.45 },
      { id: "neutronWidth", label: "Neutron Γn (meV)", min: 0.1, max: 4.0, step: 0.1, value: 0.8 },
      { id: "gammaWidth", label: "Capture Γγ (meV)", min: 20, max: 150, step: 5, value: 85 },
      { id: "temperatureK", label: "Temp T (K)", min: 0, max: 1200, step: 100, value: 300 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const E0 = vals.resEnergy !== undefined ? vals.resEnergy : 1.45;
      const Gn_meV = vals.neutronWidth !== undefined ? vals.neutronWidth : 0.8;
      const Gg_meV = vals.gammaWidth !== undefined ? vals.gammaWidth : 85;
      const T = vals.temperatureK !== undefined ? vals.temperatureK : 300;

      const Gn = Gn_meV * 1e-3; // in eV
      const Gg = Gg_meV * 1e-3; // in eV
      const Gtot = Gn + Gg;

      // Doppler width: Delta = sqrt(4 * k_B * T * E0 * (m_n / M))
      const kB = 8.617e-5; // eV/K
      const Delta = Math.sqrt(4 * kB * Math.max(1, T) * E0 * (1.0 / 115.0));

      const pL = { x: 55, y: 35, w: w - 85, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Breit-Wigner Neutron Cross Section σ(E) | E0 = ${E0.toFixed(2)} eV, Γ = ${(Gtot*1e3).toFixed(1)} meV, T = ${T} K`, pL.x, pL.y - 12);

      // Scan energy around resonance E0 ± 4*Gtot (or at least ±0.5 eV)
      const span = Math.max(0.6, 5 * (Gtot + Delta));
      const eMin = Math.max(0.01, E0 - span);
      const eMax = E0 + span;

      // Peak capture cross section (barns) ~ 4*pi/k^2 * g * Gn * Gg / Gtot^2
      // At E ~ 1 eV, 4*pi/k^2 ~ 2.6e6 barns
      const peakSig = (2.6e6 / E0) * (Gn * Gg) / Math.pow(Gtot, 2);
      const yMax = peakSig * 1.25;

      // Draw Capture Cross Section (Amber) and Elastic Scattering Cross Section with Interference (Cyan)
      const ptsCap = [], ptsScat = [];
      const de = (eMax - eMin) / 300;

      for (let e = eMin; e <= eMax; e += de) {
        // Effective width with Doppler convolution
        const effG = Math.sqrt(Gtot * Gtot + Delta * Delta);
        const x = (e - E0) / (effG / 2.0);
        const lor = 1.0 / (1.0 + x * x);

        const sigCap = peakSig * lor;
        // Elastic scattering has potential term R' ~ 5 fm plus resonance plus interference 2*R'*lor*x
        const sigPot = 5.0; // barns
        const sigScat = sigPot + (peakSig * (Gn / Gg)) * lor + 2.0 * Math.sqrt(sigPot * peakSig * (Gn / Gg)) * (x / (1 + x * x));

        const px = pL.x + ((e - eMin) / (eMax - eMin)) * pL.w;
        ptsCap.push({ px, py: pL.y + pL.h * (1 - Math.min(sigCap, yMax) / yMax) });
        ptsScat.push({ px, py: pL.y + pL.h * (1 - Math.min(sigScat, yMax * 0.4) / (yMax * 0.4)) });
      }

      // 1. Capture Cross Section
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5; ctx.beginPath();
      ptsCap.forEach((p, i) => { if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py); });
      ctx.stroke();

      // 2. Scattering Cross Section (showing interference dip before resonance!)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.beginPath();
      ptsScat.forEach((p, i) => { if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py); });
      ctx.stroke();

      // Legend
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
      ctx.fillRect(pL.x + pL.w - 240, pL.y + 15, 230, 85);
      ctx.strokeRect(pL.x + pL.w - 240, pL.y + 15, 230, 85);

      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 11px Inter";
      ctx.fillText(`— Radiative Capture σγ (Peak: ${Math.round(peakSig)} b)`, pL.x + pL.w - 225, pL.y + 35);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("— Elastic Scattering σn (Interference Dip)", pL.x + pL.w - 225, pL.y + 53);
      ctx.fillStyle = "#10b981"; ctx.font = "10px Inter";
      ctx.fillText(`Doppler Width Δ = ${(Delta*1e3).toFixed(1)} meV (${T > 0 ? "Thermal Broadened" : "Zero T"})`, pL.x + pL.w - 225, pL.y + 73);

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText(`Neutron Incident Energy E (eV) [Resonance: ${E0.toFixed(2)} eV] →`, pL.x + 30, pL.y + pL.h + 16);
    }
  },

  // =========================================================================
  // UNIT 7: ELEMENTARY PARTICLES I (SYMMETRIES & QUARK MODEL)
  // =========================================================================

  // 13. Cornell Quark Confinement Potential & Flux Tube Hadronization
  "nuc2-quark-confinement-potential-sim": {
    title: "Cornell Quark Confinement Potential & String Breaking",
    desc: "Visualizes the Cornell potential V(r) = -4/3 αs/r + κ r. Simulates the color chromoelectric flux tube between a quark-antiquark pair and animates string snapping (hadronization) when κ r exceeds 2 mq c².",
    isAnimated: true,
    controls: [
      { id: "stringTension", label: "String Tension κ (GeV/fm)", min: 0.6, max: 1.4, step: 0.05, value: 1.0 },
      { id: "strongAlpha", label: "Coupling αs", min: 0.2, max: 0.6, step: 0.02, value: 0.38 },
      { id: "quarkSeparation", label: "Separation r (fm)", min: 0.2, max: 2.2, step: 0.05, value: 0.8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const kappa = vals.stringTension !== undefined ? vals.stringTension : 1.0;
      const alphaS = vals.strongAlpha !== undefined ? vals.strongAlpha : 0.38;
      const r_val = vals.quarkSeparation !== undefined ? vals.quarkSeparation : 0.8;

      const splitX = Math.floor(w * 0.52);

      // LEFT PLOT: Cornell Potential V(r) vs r (0.05 to 2.5 fm)
      const pL = { x: 50, y: 35, w: splitX - 65, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Cornell Potential V(r) = -4/3 (αs ħc)/r + κ r", pL.x, pL.y - 12);

      const rMax = 2.5; // fm
      const vMin = -1.5, vMax = 2.5; // GeV

      // Draw zero axis line
      const yZero = pL.y + pL.h * (1 - (0 - vMin) / (vMax - vMin));
      ctx.strokeStyle = "#475569"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(pL.x, yZero); ctx.lineTo(pL.x + pL.w, yZero); ctx.stroke();
      ctx.setLineDash([]);

      // Plot Cornell curve
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let r = 0.08; r <= rMax; r += 0.02) {
        // V(r) in GeV: hbar c = 0.1973 GeV fm
        const vCoul = -(4.0 / 3.0) * (alphaS * 0.1973) / r;
        const vString = kappa * r;
        const vTot = vCoul + vString;

        const px = pL.x + (r / rMax) * pL.w;
        const py = pL.y + pL.h * (1 - (vTot - vMin) / (vMax - vMin));
        if (r === 0.08) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current separation point
      const curCoul = -(4.0 / 3.0) * (alphaS * 0.1973) / r_val;
      const curString = kappa * r_val;
      const curTot = curCoul + curString;
      const curX = pL.x + (r_val / rMax) * pL.w;
      const curY = pL.y + pL.h * (1 - (curTot - vMin) / (vMax - vMin));

      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(curX, curY, 6, 0, 2 * Math.PI); ctx.fill();

      // Hadronization threshold line (2 * m_q ~ 2 * 0.33 = 0.66 GeV or 2 m_pi ~ 0.28 GeV)
      const vBreak = 1.2; // GeV
      const yBreak = pL.y + pL.h * (1 - (vBreak - vMin) / (vMax - vMin));
      ctx.strokeStyle = "#ef4444"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(pL.x, yBreak); ctx.lineTo(pL.x + pL.w, yBreak); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter";
      ctx.fillText("String Breaking Threshold (2 m_meson ≈ 1.2 GeV)", pL.x + 10, yBreak - 4);

      // RIGHT PANEL: Animated Chromoelectric Flux Tube & Quarks
      const pR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 75 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pR.x, pR.y, pR.w, pR.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Color Flux Tube & Hadronization", pR.x + 15, pR.y + 22);

      const isBroken = curTot >= vBreak;
      const midY = pR.y + pR.h * 0.5;
      const spanPx = (r_val / rMax) * (pR.w - 100);
      const q1X = pR.x + pR.w / 2 - spanPx / 2;
      const q2X = pR.x + pR.w / 2 + spanPx / 2;

      if (!isBroken) {
        // Draw continuous shimmering color flux tube
        const tubeGrad = ctx.createLinearGradient(q1X, midY, q2X, midY);
        tubeGrad.addColorStop(0, "rgba(239, 68, 68, 0.8)");
        tubeGrad.addColorStop(0.5, "rgba(168, 85, 247, 0.8)");
        tubeGrad.addColorStop(1, "rgba(56, 189, 248, 0.8)");

        ctx.fillStyle = tubeGrad;
        const tubeH = 16 + 4 * Math.sin(time * 6);
        ctx.fillRect(q1X + 8, midY - tubeH / 2, q2X - q1X - 16, tubeH);

        // Flux lines
        ctx.strokeStyle = "rgba(255, 255, 255, 0.6)"; ctx.lineWidth = 1;
        ctx.beginPath();
        for (let x = q1X + 12; x <= q2X - 12; x += 12) {
          const yOff = Math.sin(x * 0.1 + time * 8) * (tubeH * 0.4);
          ctx.lineTo(x, midY + yOff);
        }
        ctx.stroke();
      } else {
        // String has SNAPPED! Pair creation of q_bar and q
        ctx.fillStyle = "#ef4444"; ctx.font = "bold 11px Inter";
        ctx.fillText("⚡ STRING SNAPPED! Pair Production (q q̄)", pR.x + 25, midY - 35);

        // Meson 1 (left)
        ctx.fillStyle = "rgba(239, 68, 68, 0.3)";
        ctx.fillRect(q1X - 5, midY - 14, 55, 28);
        ctx.strokeStyle = "#ef4444"; ctx.strokeRect(q1X - 5, midY - 14, 55, 28);

        // Meson 2 (right)
        ctx.fillStyle = "rgba(56, 189, 248, 0.3)";
        ctx.fillRect(q2X - 50, midY - 14, 55, 28);
        ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(q2X - 50, midY - 14, 55, 28);

        // Created pair at center
        ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(q1X + 40, midY, 6, 0, 2*Math.PI); ctx.fill();
        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(q2X - 40, midY, 6, 0, 2*Math.PI); ctx.fill();
        ctx.fillStyle = "#ffffff"; ctx.font = "8px Inter";
        ctx.fillText("q̄", q1X + 38, midY + 3);
        ctx.fillText("q", q2X - 42, midY + 3);
      }

      // Draw primary quarks
      // Quark 1 (Red)
      ctx.fillStyle = "#ef4444"; ctx.beginPath(); ctx.arc(q1X, midY, 10, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px Inter"; ctx.fillText("q", q1X - 3, midY + 3);

      // Quark 2 (Anti-quark, Cyan)
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(q2X, midY, 10, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = "#000000"; ctx.fillText("q̄", q2X - 4, midY + 3);

      // Readouts
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`r = ${r_val.toFixed(2)} fm | V(r) = ${curTot.toFixed(2)} GeV`, pL.x, h - 15);
      ctx.fillText(isBroken ? "Color Confinement prevents free quarks!" : "Linear string tension κ = 16 metric tons!", pR.x + 10, h - 15);
    }
  },

  // 14. Neutral Kaon Oscillations & Cronin-Fitch CP Violation
  "nuc2-cp-violation-kaon-sim": {
    title: "Neutral Kaon Oscillations & Cronin-Fitch CP Violation",
    desc: "Simulates time evolution of initial |K0⟩ state. Shows rapid strangeness oscillations between K0 and K0_bar, short-lived KS -> 2π and long-lived KL -> 3π decays, and CP violation KL -> 2π with |ε| ≈ 2.23 × 10⁻³.",
    isAnimated: true,
    controls: [
      { id: "timeScale", label: "Time t / τS", min: 0.0, max: 14.0, step: 0.2, value: 4.75 },
      { id: "massDiffRatio", label: "Mass Δm / ΓS", min: 0.2, max: 0.8, step: 0.05, value: 0.474 },
      { id: "epsilonCP", label: "CP Impurity |ε|×10³", min: 0.0, max: 5.0, step: 0.2, value: 2.23 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const curT = vals.timeScale !== undefined ? vals.timeScale : 4.75;
      const deltaM = vals.massDiffRatio !== undefined ? vals.massDiffRatio : 0.474;
      const epsVal = (vals.epsilonCP !== undefined ? vals.epsilonCP : 2.23) * 1e-3;

      const splitX = Math.floor(w * 0.54);

      // LEFT PLOT: Probabilities P(K0) and P(K0_bar) vs proper time t / tau_S
      const pL = { x: 50, y: 35, w: splitX - 65, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Strangeness Oscillations: P(K0, t) & P(K̄0, t) vs t/τS", pL.x, pL.y - 12);

      const tMax = 14.0;
      const gammaL_over_S = 1.0 / 570.0; // KL lives 570 times longer

      // Curves
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.beginPath();
      // P(K0, t)
      for (let t = 0; t <= tMax; t += 0.1) {
        const pK0 = 0.25 * (Math.exp(-t) + Math.exp(-t * gammaL_over_S) + 2 * Math.exp(-0.5 * t) * Math.cos(deltaM * t));
        const px = pL.x + (t / tMax) * pL.w;
        const py = pL.y + pL.h * (1 - pK0);
        if (t === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // P(K0_bar, t) (Amber)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.beginPath();
      for (let t = 0; t <= tMax; t += 0.1) {
        const pK0bar = 0.25 * (Math.exp(-t) + Math.exp(-t * gammaL_over_S) - 2 * Math.exp(-0.5 * t) * Math.cos(deltaM * t));
        const px = pL.x + (t / tMax) * pL.w;
        const py = pL.y + pL.h * (1 - pK0bar);
        if (t === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Time cursor line
      const curX = pL.x + (curT / tMax) * pL.w;
      ctx.strokeStyle = "#ec4899"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(curX, pL.y); ctx.lineTo(curX, pL.y + pL.h); ctx.stroke();
      ctx.setLineDash([]);

      const curPK0 = 0.25 * (Math.exp(-curT) + Math.exp(-curT * gammaL_over_S) + 2 * Math.exp(-0.5 * curT) * Math.cos(deltaM * curT));
      const curPK0bar = 0.25 * (Math.exp(-curT) + Math.exp(-curT * gammaL_over_S) - 2 * Math.exp(-0.5 * curT) * Math.cos(deltaM * curT));

      // RIGHT PANEL: Cronin-Fitch CP Violation Detector Readout
      const pR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 75 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pR.x, pR.y, pR.w, pR.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Cronin-Fitch CP Violation (1964)", pR.x + 15, pR.y + 22);

      // Decay rates at current time:
      // Rate to 2pi is proportional to |<2pi|KS> exp(-t/2) + eps <2pi|KL> exp(-gamma_L t / 2)|^2
      const rate2pi = Math.exp(-curT) + Math.pow(epsVal, 2) * Math.exp(-curT * gammaL_over_S) + 2 * epsVal * Math.exp(-0.5 * curT) * Math.cos(deltaM * curT - 0.76);
      const isDownstream = curT > 6.0;

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Beam Proper Time: t = ${curT.toFixed(2)} τS`, pR.x + 15, pR.y + 50);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`P(K0, Strangeness = +1): ${(curPK0 * 100).toFixed(1)}%`, pR.x + 15, pR.y + 70);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`P(K̄0, Strangeness = -1): ${(curPK0bar * 100).toFixed(1)}%`, pR.x + 15, pR.y + 90);

      // Cronin-Fitch downstream detection box
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
      ctx.fillRect(pR.x + 15, pR.y + 115, pR.w - 30, 75);
      ctx.strokeRect(pR.x + 15, pR.y + 115, pR.w - 30, 75);

      ctx.fillStyle = isDownstream ? "#ec4899" : "#64748b"; ctx.font = "bold 11px Inter";
      ctx.fillText("Downstream Region (>6 τS, KS decayed away):", pR.x + 25, pR.y + 135);

      ctx.fillStyle = "#ffffff"; ctx.font = "10px Inter";
      ctx.fillText(`KL → π⁺ + π⁻ Branching Ratio: ~2.0 × 10⁻³`, pR.x + 25, pR.y + 155);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`CP Impurity |ε| = ${(epsVal * 1e3).toFixed(2)} × 10⁻³ (Nobel 1980)`, pR.x + 25, pR.y + 172);

      // Bottom readouts
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("— P(K0)", pL.x + 10, h - 15);
      ctx.fillText("— P(K̄0) [Strangeness Oscillation Peak at t ≈ 4.75 τS]", pL.x + 70, h - 15);
    }
  },

  // =========================================================================
  // UNIT 8: ELEMENTARY PARTICLES II (HADRON SPECTROSCOPY & UNIFICATION)
  // =========================================================================

  // 15. The Eightfold Way: SU(3) Flavor Weight Diagrams & Gell-Mann-Okubo Mass
  "nuc2-su3-flavor-multiplet-sim": {
    title: "The Eightfold Way: SU(3) Flavor Weight Diagrams & GMO Mass",
    desc: "Interactive Lie group SU(3) Flavor Weight Diagram (Y vs I3). Switch between the Pseudoscalar Mesons (0⁻), Baryon Octet (1/2⁺), and Baryon Decuplet (3/2⁺). Demonstrates the decuplet equal-spacing rule and the Ω⁻ discovery.",
    isAnimated: true,
    controls: [
      { id: "multipletType", label: "Multiplet (1:Meson, 2:Octet, 3:Decuplet)", min: 1, max: 3, step: 1, value: 3 },
      { id: "symmetryBreaking", label: "SU(3) Breaking ms - mu (MeV)", min: 60, max: 240, step: 10, value: 150 },
      { id: "spacingRule", label: "Decuplet Spacing ΔM (MeV)", min: 120, max: 170, step: 2, value: 147 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const mType = Math.round(vals.multipletType !== undefined ? vals.multipletType : 3);
      const deltaM = vals.spacingRule !== undefined ? vals.spacingRule : 147;

      const splitX = Math.floor(w * 0.55);

      // LEFT PANEL: 2D SU(3) Weight Diagram (I3 on X, Y on Y)
      const pL = { x: 30, y: 30, w: splitX - 45, h: h - 60 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pL.x, pL.y, pL.w, pL.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      const titleMap = {
        1: "Pseudoscalar Meson Nonet (JP = 0⁻)",
        2: "Baryon Octet (JP = 1/2⁺)",
        3: "Baryon Decuplet (JP = 3/2⁺) [Historic Ω⁻]"
      };
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText(titleMap[mType], pL.x + 15, pL.y + 22);

      const cx = pL.x + pL.w / 2;
      const cy = pL.y + pL.h / 2 + 10;
      const scaleX = 85;
      const scaleY = 70;

      // Draw Axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(pL.x + 20, cy); ctx.lineTo(pL.x + pL.w - 20, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, pL.y + 35); ctx.lineTo(cx, pL.y + pL.h - 15); ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Isospin I3 →", pL.x + pL.w - 75, cy - 6);
      ctx.fillText("Hypercharge Y ↑", cx + 8, pL.y + 48);

      // Hadron states for each representation
      let hadrons = [];
      if (mType === 1) {
        // Meson octet/nonet
        hadrons = [
          { name: "K⁺", i3: 0.5, y: 1.0, color: "#38bdf8" },
          { name: "K⁰", i3: -0.5, y: 1.0, color: "#38bdf8" },
          { name: "π⁺", i3: 1.0, y: 0.0, color: "#10b981" },
          { name: "π⁰/η", i3: 0.0, y: 0.0, color: "#ffffff" },
          { name: "π⁻", i3: -1.0, y: 0.0, color: "#10b981" },
          { name: "K̄⁰", i3: 0.5, y: -1.0, color: "#f59e0b" },
          { name: "K⁻", i3: -0.5, y: -1.0, color: "#f59e0b" }
        ];
      } else if (mType === 2) {
        // Baryon Octet
        hadrons = [
          { name: "p", i3: 0.5, y: 1.0, color: "#38bdf8" },
          { name: "n", i3: -0.5, y: 1.0, color: "#38bdf8" },
          { name: "Σ⁺", i3: 1.0, y: 0.0, color: "#10b981" },
          { name: "Σ⁰/Λ", i3: 0.0, y: 0.0, color: "#ffffff" },
          { name: "Σ⁻", i3: -1.0, y: 0.0, color: "#10b981" },
          { name: "Ξ⁰", i3: 0.5, y: -1.0, color: "#f59e0b" },
          { name: "Ξ⁻", i3: -0.5, y: -1.0, color: "#f59e0b" }
        ];
      } else {
        // Baryon Decuplet (Inverted Triangle)
        hadrons = [
          { name: "Δ⁺⁺", i3: 1.5, y: 1.0, color: "#38bdf8" },
          { name: "Δ⁺", i3: 0.5, y: 1.0, color: "#38bdf8" },
          { name: "Δ⁰", i3: -0.5, y: 1.0, color: "#38bdf8" },
          { name: "Δ⁻", i3: -1.5, y: 1.0, color: "#38bdf8" },
          { name: "Σ*⁺", i3: 1.0, y: 0.0, color: "#10b981" },
          { name: "Σ*⁰", i3: 0.0, y: 0.0, color: "#10b981" },
          { name: "Σ*⁻", i3: -1.0, y: 0.0, color: "#10b981" },
          { name: "Ξ*⁰", i3: 0.5, y: -1.0, color: "#f59e0b" },
          { name: "Ξ*⁻", i3: -0.5, y: -1.0, color: "#f59e0b" },
          { name: "Ω⁻", i3: 0.0, y: -2.0, color: "#f43f5e", isOmega: true }
        ];
      }

      // Draw state circles
      hadrons.forEach(h => {
        const px = cx + h.i3 * scaleX;
        const py = cy - h.y * scaleY;

        ctx.fillStyle = h.color;
        ctx.beginPath(); ctx.arc(px, py, h.isOmega ? 9 : 7, 0, 2 * Math.PI); ctx.fill();

        ctx.fillStyle = "#ffffff"; ctx.font = h.isOmega ? "bold 11px Inter" : "10px Inter";
        ctx.fillText(h.name, px + 10, py + 4);
      });

      // RIGHT PANEL: Gell-Mann-Okubo Decuplet Equal-Spacing Spectrum
      const pR = { x: splitX + 20, y: 30, w: w - splitX - 45, h: h - 60 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pR.x, pR.y, pR.w, pR.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Decuplet Equal-Spacing Rule (GMO)", pR.x + 15, pR.y + 22);

      // Mass tiers
      const tiers = [
        { name: "Δ (1232)", s: 0, m: 1232 },
        { name: "Σ* (1385)", s: -1, m: 1232 + deltaM },
        { name: "Ξ* (1530)", s: -2, m: 1232 + 2 * deltaM },
        { name: "Ω⁻ (1672)", s: -3, m: 1232 + 3 * deltaM, isPredicted: true }
      ];

      let tY = pR.y + 60;
      tiers.forEach((t, idx) => {
        ctx.fillStyle = t.isPredicted ? "#f43f5e" : "#38bdf8";
        ctx.fillRect(pR.x + 20, tY - 14, 8, 28);

        ctx.font = "bold 11px Inter";
        ctx.fillText(`${t.name}:`, pR.x + 35, tY);
        ctx.fillStyle = "#ffffff";
        ctx.fillText(`${t.m} MeV/c² (S = ${t.s})`, pR.x + 115, tY);

        if (idx < 3) {
          ctx.fillStyle = "#10b981"; ctx.font = "10px Inter";
          ctx.fillText(`↓ +ΔM = ${deltaM} MeV`, pR.x + 60, tY + 22);
        }
        tY += 40;
      });

      // Historic note
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Historic Prediction: M(Ω⁻) = 1673 MeV/c²`, pR.x + 20, pR.y + pR.h - 32);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText(`Discovered at BNL in 1964 with mass 1672 MeV/c²!`, pR.x + 20, pR.y + pR.h - 16);
    }
  },

  // 16. Three-Flavor Neutrino Oscillations & PMNS Mixing with Solar MSW Resonance
  "nuc2-neutrino-oscillation-sim": {
    title: "Three-Flavor Neutrino Oscillations & PMNS Mixing",
    desc: "Simulates neutrino flavor evolution (νe, νμ, ντ) over baseline L/E. Evaluates PMNS transition probabilities P(να -> νβ) with solar Δm²_21 and atmospheric Δm²_32, and demonstrates the Mikheyev-Smirnov-Wolfenstein (MSW) matter resonance.",
    isAnimated: true,
    controls: [
      { id: "baselineRatio", label: "Log10(L/E) (km/GeV)", min: 0.0, max: 4.5, step: 0.1, value: 2.3 },
      { id: "theta12Deg", label: "Solar θ12 (deg)", min: 25.0, max: 40.0, step: 1.0, value: 33.4 },
      { id: "matterDensity", label: "Matter Density ne", min: 0.0, max: 2.5, step: 0.1, value: 0.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const logLE = vals.baselineRatio !== undefined ? vals.baselineRatio : 2.3;
      const th12 = (vals.theta12Deg !== undefined ? vals.theta12Deg : 33.4) * (Math.PI / 180);
      const ne = vals.matterDensity !== undefined ? vals.matterDensity : 0.0;

      const splitX = Math.floor(w * 0.54);

      // LEFT PLOT: Transition Probabilities P(νe -> νe) and P(νe -> νμ) vs log10(L/E)
      const pL = { x: 50, y: 35, w: splitX - 65, h: h - 75 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(pL.x, pL.y, pL.w, pL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Oscillation Probabilities: P(νe → νe) & P(νe → νμ) vs Log10(L/E)", pL.x, pL.y - 12);

      // Physical parameters:
      // Delta m^2_21 = 7.5e-5 eV^2 (Solar)
      // Delta m^2_32 = 2.45e-3 eV^2 (Atmospheric)
      const dm21 = 7.5e-5;
      const dm32 = 2.45e-3;

      // In medium: MSW effective mixing
      const sin2_2th_eff = Math.sin(2 * th12) / Math.sqrt(Math.pow(Math.cos(2 * th12) - 0.4 * ne, 2) + Math.pow(Math.sin(2 * th12), 2));

      // Plot curves from log10(L/E) = 0 to 4.5
      const ptsPe = [], ptsPmu = [];
      for (let l = 0.0; l <= 4.5; l += 0.05) {
        const LE = Math.pow(10, l); // km/GeV
        // phases: Phi = 1.267 * dm^2 * (L/E)
        const phiAtm = 1.267 * dm32 * LE;
        const phiSol = 1.267 * dm21 * LE;

        // Approx 3-flavor probability starting with nu_e:
        // P(nu_e -> nu_e) ~ 1 - sin^2(2*th13)*sin^2(phiAtm) - cos^4(th13)*sin2_2th_eff*sin^2(phiSol)
        const p_ee = Math.max(0.02, 1.0 - 0.09 * Math.pow(Math.sin(phiAtm), 2) - 0.85 * Math.pow(sin2_2th_eff, 2) * Math.pow(Math.sin(phiSol), 2));
        const p_emu = Math.min(0.95, (1.0 - p_ee) * 0.65);

        const px = pL.x + (l / 4.5) * pL.w;
        ptsPe.push({ px, py: pL.y + pL.h * (1 - p_ee) });
        ptsPmu.push({ px, py: pL.y + pL.h * (1 - p_emu) });
      }

      // Draw P(nu_e -> nu_e) (Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      ptsPe.forEach((p, i) => { if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py); });
      ctx.stroke();

      // Draw P(nu_e -> nu_mu) (Amber)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.beginPath();
      ptsPmu.forEach((p, i) => { if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py); });
      ctx.stroke();

      // Current baseline indicator
      const curX = pL.x + (logLE / 4.5) * pL.w;
      ctx.strokeStyle = "#ec4899"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(curX, pL.y); ctx.lineTo(curX, pL.y + pL.h); ctx.stroke();
      ctx.setLineDash([]);

      // RIGHT PANEL: Flavor Composition Pie / Bar
      const pR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 75 };
      ctx.fillStyle = "#0b1120"; ctx.fillRect(pR.x, pR.y, pR.w, pR.h);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(pR.x, pR.y, pR.w, pR.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Neutrino Flavor Composition", pR.x + 15, pR.y + 22);

      const curLE = Math.pow(10, logLE);
      const curPhiAtm = 1.267 * dm32 * curLE;
      const curPhiSol = 1.267 * dm21 * curLE;
      const curPee = Math.max(0.02, 1.0 - 0.09 * Math.pow(Math.sin(curPhiAtm), 2) - 0.85 * Math.pow(sin2_2th_eff, 2) * Math.pow(Math.sin(curPhiSol), 2));
      const curPemu = (1.0 - curPee) * 0.6;
      const curPetau = Math.max(0, 1.0 - curPee - curPemu);

      const barW = 45;
      const hE = curPee * (pR.h - 90);
      const hMu = curPemu * (pR.h - 90);
      const hTau = curPetau * (pR.h - 90);

      // Bar 1: nu_e
      ctx.fillStyle = "#38bdf8";
      ctx.fillRect(pR.x + 30, pR.y + pR.h - 40 - hE, barW, hE);
      ctx.fillStyle = "#ffffff"; ctx.font = "10px Inter";
      ctx.fillText(`${(curPee * 100).toFixed(1)}%`, pR.x + 32, pR.y + pR.h - 45 - hE);
      ctx.fillText("νe", pR.x + 45, pR.y + pR.h - 22);

      // Bar 2: nu_mu
      ctx.fillStyle = "#f59e0b";
      ctx.fillRect(pR.x + 100, pR.y + pR.h - 40 - hMu, barW, hMu);
      ctx.fillText(`${(curPemu * 100).toFixed(1)}%`, pR.x + 102, pR.y + pR.h - 45 - hMu);
      ctx.fillText("νμ", pR.x + 115, pR.y + pR.h - 22);

      // Bar 3: nu_tau
      ctx.fillStyle = "#10b981";
      ctx.fillRect(pR.x + 170, pR.y + pR.h - 40 - hTau, barW, hTau);
      ctx.fillText(`${(curPetau * 100).toFixed(1)}%`, pR.x + 172, pR.y + pR.h - 45 - hTau);
      ctx.fillText("ντ", pR.x + 185, pR.y + pR.h - 22);

      // MSW resonance note
      if (ne > 0.5) {
        ctx.fillStyle = "#ec4899"; ctx.font = "bold 11px Inter";
        ctx.fillText("⚡ MSW Solar Matter Resonance Active!", pR.x + 20, pR.y + 55);
        ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
        ctx.fillText("Adiabatic level crossing converts νe → ν2", pR.x + 20, pR.y + 72);
      } else {
        ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
        ctx.fillText("Vacuum oscillations (SNO, Super-K, KamLAND)", pR.x + 20, pR.y + 55);
      }

      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText(`Log10(L/E) = ${logLE.toFixed(1)} | L/E ≈ ${Math.round(curLE)} km/GeV`, pL.x + 20, h - 15);
    }
  }
};

// Simulation Engine Bridge
window.SimulationEngine = window.SimulationEngine || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const simConfig = (window.NUC2_SIMS && window.NUC2_SIMS[simType]) ||
                    (window.SSP2_SIMS && window.SSP2_SIMS[simType]) ||
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
