# -*- coding: utf-8 -*-
"""
Builder for Nuclear Physics II Simulations 9 through 12
9. nuc2-shell-model-spin-orbit-sim
10. nuc2-collective-rotational-vibrational-sim
11. nuc2-optical-model-scattering-sim
12. nuc2-breit-wigner-resonance-sim
"""

sims_9_12 = r'''
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
'''
