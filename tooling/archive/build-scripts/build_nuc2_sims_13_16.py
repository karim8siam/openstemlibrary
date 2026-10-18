# -*- coding: utf-8 -*-
"""
Builder for Nuclear Physics II Simulations 13 through 16
13. nuc2-quark-confinement-potential-sim
14. nuc2-cp-violation-kaon-sim
15. nuc2-su3-flavor-multiplet-sim
16. nuc2-neutrino-oscillation-sim
"""

sims_13_16 = r'''
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
'''
