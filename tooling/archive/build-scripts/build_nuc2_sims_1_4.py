# -*- coding: utf-8 -*-
"""
Builder for Nuclear Physics II Simulations 1 through 4
1. nuc2-deuteron-wavefunction-sim
2. nuc2-photodisintegration-sim
3. nuc2-np-scattering-phaseshift-sim
4. nuc2-ortho-para-hydrogen-sim
"""

sims_1_4 = r'''
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
'''
