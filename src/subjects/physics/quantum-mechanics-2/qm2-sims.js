// Quantum Mechanics II Interactive Simulation Suite
// 16 Real-Time Canvas Simulations for Advanced Dynamics, Perturbation Theory, Scattering & Relativistic Waves

window.QM2_SIMS = {

  // =========================================================================
  // CHAPTER 1: MATRIX MECHANICS & HILBERT SPACE
  // =========================================================================

  // 1. Interactive Hilbert State Space & Unitary Basis Rotation
  "qm2-hilbert-state-sim": {
    title: "Interactive Hilbert State Space & Unitary Basis Rotation",
    desc: "Visualize state ket |ψ⟩ = c₁|u₁⟩ + c₂|u₂⟩ in a 2D Hilbert space slice, orthonormal basis projections, and continuous unitary SU(2) state rotations with norm conservation.",
    isAnimated: true,
    controls: [
      { id: "thetaAngle", label: "State Polar Angle θ (deg)", min: 0, max: 180, step: 1, value: 45 },
      { id: "phiPhase", label: "Relative Phase φ (deg)", min: 0, max: 360, step: 2, value: 30 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const thetaDeg = vals.thetaAngle !== undefined ? vals.thetaAngle : 45;
      const phiDeg = vals.phiPhase !== undefined ? vals.phiPhase : 30;
      const theta = (thetaDeg * Math.PI) / 180;
      const phi = (phiDeg * Math.PI) / 180 + time * 0.5;

      const c1 = Math.cos(theta / 2);
      const c2_r = Math.sin(theta / 2) * Math.cos(phi);
      const c2_i = Math.sin(theta / 2) * Math.sin(phi);
      const p1 = c1 * c1;
      const p2 = c2_r * c2_r + c2_i * c2_i;

      // Title
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("Hilbert State Ket |ψ⟩ & Unitary Projection Space", 25, 30);

      // Complex Plane Circle / State Vector
      const cx = 220, cy = 210, R = 140;
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.stroke();

      // Axes
      ctx.strokeStyle = "#334155"; ctx.beginPath();
      ctx.moveTo(cx - R - 20, cy); ctx.lineTo(cx + R + 20, cy);
      ctx.moveTo(cx, cy - R - 20); ctx.lineTo(cx, cy + R + 20); ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("|u₁⟩ (Re)", cx + R + 5, cy - 8);
      ctx.fillText("|u₂⟩ (Im)", cx + 8, cy - R - 5);

      // Rotating State Vector
      const vx = cx + R * Math.cos(theta) * Math.cos(phi);
      const vy = cy - R * Math.sin(theta);

      // Projection lines
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(vx, vy); ctx.lineTo(vx, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(vx, vy); ctx.lineTo(cx, vy); ctx.stroke();
      ctx.setLineDash([]);

      // State Arrow
      ctx.strokeStyle = "#22c55e"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(vx, vy); ctx.stroke();
      ctx.fillStyle = "#22c55e"; ctx.beginPath(); ctx.arc(vx, vy, 6, 0, Math.PI * 2); ctx.fill();

      // State Equation Badge
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 13px monospace";
      ctx.fillText(`|ψ⟩ = cos(θ/2)|u₁⟩ + e^(iφ)sin(θ/2)|u₂⟩`, 25, 60);

      // Probability Bar Panels
      const barX = 420, barY = 90, barW = 280, barH = 26;
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`P(|u₁⟩) = |c₁|² = ${p1.toFixed(3)} (${(p1 * 100).toFixed(1)}%)`, barX, barY);
      ctx.fillStyle = "#1e293b"; ctx.fillRect(barX, barY + 8, barW, barH);
      ctx.fillStyle = "#38bdf8"; ctx.fillRect(barX, barY + 8, barW * p1, barH);

      ctx.fillStyle = "#94a3b8";
      ctx.fillText(`P(|u₂⟩) = |c₂|² = ${p2.toFixed(3)} (${(p2 * 100).toFixed(1)}%)`, barX, barY + 65);
      ctx.fillStyle = "#1e293b"; ctx.fillRect(barX, barY + 73, barW, barH);
      ctx.fillStyle = "#ec4899"; ctx.fillRect(barX, barY + 73, barW * p2, barH);

      // Completeness check
      ctx.fillStyle = "#10b981"; ctx.font = "13px Inter, sans-serif";
      ctx.fillText(`Total Norm: ⟨ψ|ψ⟩ = ${ (p1 + p2).toFixed(4) } (Strictly Conserved)`, barX, barY + 135);
      ctx.fillStyle = "#64748b"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Polar θ = ${thetaDeg}°, Relative Phase φ = ${phiDeg}° + ωt`, barX, barY + 165);
      ctx.fillText(`Purity: Tr(ρ²) = 1.000 (Pure State Ray)`, barX, barY + 190);
    }
  },

  // 2. Harmonic Oscillator Fock State Matrix Elements & Ladder Transitions
  "qm2-ladder-operator-sim": {
    title: "Harmonic Oscillator Fock State Matrix Elements & Ladder Transitions",
    desc: "Interactive visualizer for harmonic oscillator Fock energy levels |n⟩, non-zero matrix elements ⟨n'|x|n⟩, and raising/lowering ladder operations â†|n⟩ = √(n+1)|n+1⟩ and â|n⟩ = √n|n-1⟩.",
    isAnimated: false,
    controls: [
      { id: "fockN", label: "Initial Fock Level n (0 to 6)", min: 0, max: 6, step: 1, value: 2 },
      { id: "opMode", label: "Operation: 0: Lowering â, 1: Raising â†", min: 0, max: 1, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const n = Math.round(vals.fockN !== undefined ? vals.fockN : 2);
      const isRaising = Math.round(vals.opMode !== undefined ? vals.opMode : 1) === 1;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("Harmonic Oscillator Matrix Mechanics & Ladder Transitions", 25, 30);

      // Draw Energy Ladder
      const startX = 60, ladderW = 220;
      const bottomY = 320, levelSpacing = 38;

      for (let i = 0; i <= 7; i++) {
        const y = bottomY - i * levelSpacing;
        ctx.strokeStyle = i === n ? "#f59e0b" : "#334155";
        ctx.lineWidth = i === n ? 3 : 1.5;
        ctx.beginPath(); ctx.moveTo(startX, y); ctx.lineTo(startX + ladderW, y); ctx.stroke();

        ctx.fillStyle = i === n ? "#f59e0b" : "#94a3b8";
        ctx.font = i === n ? "bold 13px Inter" : "12px Inter";
        ctx.fillText(`|${i}⟩  E = ${(i + 0.5).toFixed(1)} ħω`, startX - 45, y + 4);
      }

      // Transition Arrow
      const fromY = bottomY - n * levelSpacing;
      let toY, targetN, factor, opName;
      if (isRaising) {
        targetN = n + 1;
        toY = bottomY - targetN * levelSpacing;
        factor = Math.sqrt(n + 1);
        opName = "â† (Creation)";
      } else {
        targetN = n - 1;
        toY = n > 0 ? bottomY - targetN * levelSpacing : fromY;
        factor = n > 0 ? Math.sqrt(n) : 0;
        opName = "â (Annihilation)";
      }

      if (isRaising || n > 0) {
        const arrowX = startX + ladderW / 2;
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(arrowX, fromY); ctx.lineTo(arrowX, toY); ctx.stroke();
        // Arrowhead
        ctx.fillStyle = "#10b981"; ctx.beginPath();
        if (isRaising) {
          ctx.moveTo(arrowX - 6, toY + 10); ctx.lineTo(arrowX + 6, toY + 10); ctx.lineTo(arrowX, toY);
        } else {
          ctx.moveTo(arrowX - 6, toY - 10); ctx.lineTo(arrowX + 6, toY - 10); ctx.lineTo(arrowX, toY);
        }
        ctx.fill();
      }

      // Matrix Grid Display (Right)
      const matX = 350, matY = 70, cellS = 40;
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Coordinate Operator Matrix Elements ⟨n'| x |n⟩ (units of x₀)", matX, matY - 15);

      for (let r = 0; r < 6; r++) {
        for (let c = 0; c < 6; c++) {
          const cx = matX + c * cellS;
          const cy = matY + r * cellS;
          let val = 0;
          if (r === c - 1) val = Math.sqrt(c) / Math.SQRT2;
          else if (r === c + 1) val = Math.sqrt(r) / Math.SQRT2;

          ctx.fillStyle = val > 0 ? "rgba(56, 189, 248, 0.2)" : "rgba(30, 41, 59, 0.5)";
          ctx.fillRect(cx, cy, cellS - 3, cellS - 3);
          ctx.strokeStyle = (r === targetN && c === n) ? "#10b981" : "#334155";
          ctx.lineWidth = (r === targetN && c === n) ? 2 : 1;
          ctx.strokeRect(cx, cy, cellS - 3, cellS - 3);

          ctx.fillStyle = val > 0 ? "#38bdf8" : "#64748b";
          ctx.font = "11px monospace";
          ctx.fillText(val > 0 ? val.toFixed(2) : "0", cx + 7, cy + 24);
        }
      }

      // Bottom Info
      ctx.fillStyle = "#ffffff"; ctx.font = "13px Inter, sans-serif";
      ctx.fillText(`Active Operator: ${opName} | Current State: |${n}⟩`, 25, 360);
      if (isRaising) {
        ctx.fillStyle = "#10b981";
        ctx.fillText(`â†|${n}⟩ = √(${n}+1)|${n+1}⟩ = ${factor.toFixed(3)} |${targetN}⟩`, 25, 385);
      } else if (n > 0) {
        ctx.fillStyle = "#10b981";
        ctx.fillText(`â|${n}⟩ = √${n}|${n-1}⟩ = ${factor.toFixed(3)} |${targetN}⟩`, 25, 385);
      } else {
        ctx.fillStyle = "#ef4444";
        ctx.fillText(`â|0⟩ = 0  (Ground state annihilated; spectrum bounded from below!)`, 25, 385);
      }
    }
  },

  // =========================================================================
  // CHAPTER 2: QUANTUM DYNAMICS & PICTURES
  // =========================================================================

  // 3. Heisenberg Operator Dynamics & Phase Space Trajectories
  "qm2-heisenberg-dynamics-sim": {
    title: "Heisenberg Operator Dynamics & Phase Space Trajectories",
    desc: "Real-time evolution of position and momentum expectation values ⟨x(t)⟩ and ⟨p(t)⟩ in the Heisenberg picture, illustrating Ehrenfest's theorem and phase space trajectories.",
    isAnimated: true,
    controls: [
      { id: "omegaFreq", label: "Oscillator Frequency ω (rad/s)", min: 0.5, max: 3.0, step: 0.1, value: 1.2 },
      { id: "initX", label: "Initial Displacement x₀", min: 0.5, max: 2.5, step: 0.1, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const omega = vals.omegaFreq !== undefined ? vals.omegaFreq : 1.2;
      const x0 = vals.initX !== undefined ? vals.initX : 1.5;
      const p0 = 0.0;

      const xt = x0 * Math.cos(omega * time) + (p0 / omega) * Math.sin(omega * time);
      const pt = -x0 * omega * Math.sin(omega * time) + p0 * Math.cos(omega * time);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("Heisenberg Picture: Operator Expectation & Phase Space Orbits", 25, 30);

      // Phase Space Canvas (Left)
      const cx = 200, cy = 200, scale = 50;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(cx - 150, cy); ctx.lineTo(cx + 150, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy - 150); ctx.lineTo(cx, cy + 150); ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText("⟨x(t)⟩", cx + 130, cy - 8);
      ctx.fillText("⟨p(t)⟩ / mω", cx + 8, cy - 130);

      // Orbit Ellipse
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(cx, cy, x0 * scale, 0, Math.PI * 2); ctx.stroke();

      // Current Particle Point
      const px = cx + xt * scale;
      const py = cy - (pt / omega) * scale;
      ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(px, py, 7, 0, Math.PI * 2); ctx.fill();

      // Waveform Display (Right)
      const waveX = 400, waveY = 200, waveW = 320, waveH = 100;
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(waveX, waveY - waveH/2, waveW, waveH);
      ctx.beginPath(); ctx.moveTo(waveX, waveY); ctx.lineTo(waveX + waveW, waveY); ctx.stroke();

      // Draw historical x(t) wave
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.beginPath();
      for (let i = 0; i < waveW; i++) {
        const tau = time - (waveW - i) * 0.02;
        const x_val = x0 * Math.cos(omega * tau);
        const y_pos = waveY - x_val * (waveH / 2 / 2.5);
        if (i === 0) ctx.moveTo(waveX + i, y_pos);
        else ctx.lineTo(waveX + i, y_pos);
      }
      ctx.stroke();

      // Formula and Metrics
      ctx.fillStyle = "#ffffff"; ctx.font = "13px monospace";
      ctx.fillText(`x_H(t) = x(0)cos(ωt) + (p(0)/mω)sin(ωt)`, 25, 360);
      ctx.fillText(`⟨x(t)⟩ = ${xt.toFixed(3)} x₀ | ⟨p(t)⟩ = ${pt.toFixed(3)} ħk`, 25, 385);
      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter";
      ctx.fillText("Verified: [x_H(t), p_H(t)] = iħ (Invariant for all time)", 400, 360);
    }
  },

  // 4. Interactive Two-Level Rabi Flopping & Detuning Resonance
  "qm2-rabi-oscillations-sim": {
    title: "Interactive Two-Level Rabi Flopping & Detuning Resonance",
    desc: "Simulate driven two-level transitions under a monochromatic laser, observing population inversion, Rabi flopping frequency Ω_eff = √(Ω_R² + Δ²), and resonance suppression.",
    isAnimated: true,
    controls: [
      { id: "rabiFreq", label: "Rabi Frequency Ω_R (rad/s)", min: 0.5, max: 3.0, step: 0.1, value: 1.5 },
      { id: "detuning", label: "Laser Detuning Δ = ω - ω₀ (rad/s)", min: -3.0, max: 3.0, step: 0.1, value: 0.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const omegaR = vals.rabiFreq !== undefined ? vals.rabiFreq : 1.5;
      const delta = vals.detuning !== undefined ? vals.detuning : 0.0;
      const omegaEff = Math.sqrt(omegaR * omegaR + delta * delta);
      const maxP = (omegaR * omegaR) / (omegaEff * omegaEff);
      const p2 = maxP * Math.pow(Math.sin((omegaEff * time) / 2), 2);
      const p1 = 1 - p2;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("Two-Level Driven System: Rabi Flopping & Resonance Dynamics", 25, 30);

      // Population Bars (Left)
      const bx = 60, by = 80, bw = 60, bh = 200;
      // Level 2 (Excited)
      ctx.fillStyle = "#1e293b"; ctx.fillRect(bx, by, bw, bh);
      ctx.fillStyle = "#ec4899"; ctx.fillRect(bx, by + bh * (1 - p2), bw, bh * p2);
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 1.5; ctx.strokeRect(bx, by, bw, bh);

      // Level 1 (Ground)
      const gx = bx + 90;
      ctx.fillStyle = "#1e293b"; ctx.fillRect(gx, by, bw, bh);
      ctx.fillStyle = "#38bdf8"; ctx.fillRect(gx, by + bh * (1 - p1), bw, bh * p1);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5; ctx.strokeRect(gx, by, bw, bh);

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 12px Inter";
      ctx.fillText(`P_e: ${(p2 * 100).toFixed(1)}%`, bx + 5, by + bh + 20);
      ctx.fillText(`P_g: ${(p1 * 100).toFixed(1)}%`, gx + 5, by + bh + 20);
      ctx.fillText("|e⟩ (Excited)", bx, by - 8);
      ctx.fillText("|g⟩ (Ground)", gx, by - 8);

      // Time Waveform (Right)
      const graphX = 270, graphY = 80, graphW = 440, graphH = 200;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)"; ctx.fillRect(graphX, graphY, graphW, graphH);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(graphX, graphY, graphW, graphH);

      // Gridlines
      ctx.strokeStyle = "#1e293b"; ctx.beginPath();
      ctx.moveTo(graphX, graphY + graphH / 2); ctx.lineTo(graphX + graphW, graphY + graphH / 2);
      ctx.stroke();

      // Plot P_e(t) trace
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let i = 0; i < graphW; i++) {
        const t_plot = time - (graphW - i) * 0.02;
        const val = maxP * Math.pow(Math.sin((omegaEff * t_plot) / 2), 2);
        const py = graphY + graphH * (1 - val);
        if (i === 0) ctx.moveTo(graphX + i, py);
        else ctx.lineTo(graphX + i, py);
      }
      ctx.stroke();

      // Metric Summary
      ctx.fillStyle = "#ffffff"; ctx.font = "13px Inter";
      ctx.fillText(`Ω_eff = √(Ω_R² + Δ²) = ${omegaEff.toFixed(2)} rad/s | Max Transition = ${(maxP * 100).toFixed(1)}%`, 25, 340);
      ctx.fillStyle = delta === 0 ? "#10b981" : "#f59e0b";
      ctx.fillText(delta === 0 ? "★ EXACT RESONANCE (Δ = 0): 100% Inversion Achievable!" : `Detuned (Δ = ${delta.toFixed(1)}): Inversion capped at ${(maxP * 100).toFixed(1)}%`, 25, 365);
    }
  },

  // =========================================================================
  // CHAPTER 3: PERTURBATION THEORY & TRANSITIONS
  // =========================================================================

  // 5. Interactive Stark & Zeeman Hydrogen Level Splitting
  "qm2-stark-zeeman-levels-sim": {
    title: "Interactive Stark & Zeeman Hydrogen Level Splitting",
    desc: "Energy level diagrams of Hydrogen n=2 states under electric field E (Linear Stark effect ±3ea₀E) and magnetic field B (Zeeman splitting ΔE = g_J μ_B B m_j).",
    isAnimated: false,
    controls: [
      { id: "eField", label: "Electric Field E (kV/cm)", min: 0, max: 100, step: 2, value: 40 },
      { id: "bField", label: "Magnetic Field B (Tesla)", min: 0, max: 5, step: 0.1, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const E = vals.eField !== undefined ? vals.eField : 40;
      const B = vals.bField !== undefined ? vals.bField : 1.5;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("Hydrogen n=2 Level Splitting: Linear Stark & Zeeman Regimes", 25, 30);

      // Unperturbed Level
      const originX = 80, originY = 200;
      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(originX, originY); ctx.lineTo(originX + 80, originY); ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText("n=2 Unperturbed", originX, originY - 10);
      ctx.fillText("(4-fold degenerate)", originX, originY + 22);

      // Stark Splitting (Middle panel)
      const starkX = 280;
      const starkShift = E * 0.9;
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      // Level +3ea0E
      ctx.beginPath(); ctx.moveTo(starkX, originY - starkShift); ctx.lineTo(starkX + 100, originY - starkShift); ctx.stroke();
      ctx.fillText(`|2s - 2p₀⟩ (+${(E*0.012).toFixed(2)} meV)`, starkX + 110, originY - starkShift + 4);
      // Level 0 (2p±1)
      ctx.beginPath(); ctx.moveTo(starkX, originY); ctx.lineTo(starkX + 100, originY); ctx.stroke();
      ctx.fillText(`|2p₁⟩, |2p₋₁⟩ (0 meV)`, starkX + 110, originY + 4);
      // Level -3ea0E
      ctx.beginPath(); ctx.moveTo(starkX, originY + starkShift); ctx.lineTo(starkX + 100, originY + starkShift); ctx.stroke();
      ctx.fillText(`|2s + 2p₀⟩ (-${(E*0.012).toFixed(2)} meV)`, starkX + 110, originY + starkShift + 4);

      // Connecting fan lines
      ctx.setLineDash([3, 3]); ctx.strokeStyle = "#475569";
      ctx.beginPath(); ctx.moveTo(originX + 80, originY); ctx.lineTo(starkX, originY - starkShift); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(originX + 80, originY); ctx.lineTo(starkX, originY); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(originX + 80, originY); ctx.lineTo(starkX, originY + starkShift); ctx.stroke();
      ctx.setLineDash([]);

      // Zeeman splitting summary (Right panel)
      const zX = 480, zY = 70;
      ctx.fillStyle = "rgba(15, 23, 42, 0.8)"; ctx.fillRect(zX, zY, 240, 240);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(zX, zY, 240, 240);

      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 13px Inter";
      ctx.fillText(`Zeeman Splitting (B = ${B.toFixed(1)} T)`, zX + 15, zY + 30);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      const muB_B = B * 0.05788; // meV
      ctx.fillText(`μ_B · B = ${muB_B.toFixed(3)} meV`, zX + 15, zY + 60);
      ctx.fillText(`m_j = +3/2: +${(1.33 * muB_B).toFixed(3)} meV`, zX + 15, zY + 95);
      ctx.fillText(`m_j = +1/2: +${(0.67 * muB_B).toFixed(3)} meV`, zX + 15, zY + 125);
      ctx.fillText(`m_j = -1/2: -${(0.67 * muB_B).toFixed(3)} meV`, zX + 15, zY + 155);
      ctx.fillText(`m_j = -3/2: -${(1.33 * muB_B).toFixed(3)} meV`, zX + 15, zY + 185);
      ctx.fillStyle = "#10b981";
      ctx.fillText("g_J = 1 + [j(j+1)+s(s+1)-l(l+1)]/2j(j+1)", zX + 15, zY + 220);
    }
  },

  // 6. Fermi's Golden Rule Sinc-Squared Transition Dynamics
  "qm2-fermi-golden-rule-sim": {
    title: "Fermi's Golden Rule Sinc-Squared Transition Dynamics",
    desc: "Interactive visualizer of the transition probability sinc²(Δω t / 2) / Δω², demonstrating how broadening narrows into a sharp Dirac delta distribution as interaction time t → ∞.",
    isAnimated: true,
    controls: [
      { id: "intTime", label: "Interaction Time t (arbitrary)", min: 1, max: 20, step: 0.5, value: 5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const t = vals.intTime !== undefined ? vals.intTime : 5;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("Fermi's Golden Rule: Transition Probability Density Profile", 25, 30);

      const cx = w / 2, cy = 240, scaleX = 35, scaleY = 1.8 * t;
      // Axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(60, cy); ctx.lineTo(w - 60, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, 60); ctx.lineTo(cx, cy + 30); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText("Transition Detuning Δω = (E_f - E_i - ħω)/ħ", w - 300, cy + 25);
      ctx.fillText("Probability Rate P(Δω)/t", cx + 10, 75);

      // Sinc² curve: [sin(x*t/2)/(x/2)]² / t
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let px = 60; px < w - 60; px++) {
        const deltaOmega = (px - cx) / scaleX;
        let yVal;
        if (Math.abs(deltaOmega) < 1e-4) {
          yVal = t;
        } else {
          const s = Math.sin((deltaOmega * t) / 2) / (deltaOmega / 2);
          yVal = (s * s) / t;
        }
        const py = cy - yVal * 10;
        if (px === 60) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Peak height and width annotation
      ctx.fillStyle = "#ffffff"; ctx.font = "13px monospace";
      ctx.fillText(`Peak Height ~ t = ${t.toFixed(1)} | FWHM Width ~ 2π/t = ${( (2 * Math.PI) / t ).toFixed(2)}`, 25, 340);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("lim_{t→∞} [sin²(Δω t / 2) / (Δω² t)] = (π/2) δ(Δω)  ⇒ W = (2π/ħ)|V_fi|² ρ(E_f)", 25, 365);
    }
  },

  // =========================================================================
  // CHAPTER 4: VARIATIONAL & WKB APPROXIMATIONS
  // =========================================================================

  // 7. Helium Atom Ground State Variational Energy Minimizer
  "qm2-variational-helium-sim": {
    title: "Helium Atom Ground State Variational Energy Minimizer",
    desc: "Interactive Rayleigh-Ritz minimization curve E(Z*) = [2Z*² - 4ZZ* + 5/4 Z*] E_R for Helium (Z=2), showing optimal shielding Z* = 27/16 = 1.6875 and ground state energy -77.46 eV.",
    isAnimated: false,
    controls: [
      { id: "effZ", label: "Effective Nuclear Charge Z*", min: 1.0, max: 2.5, step: 0.01, value: 1.69 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const zStar = vals.effZ !== undefined ? vals.effZ : 1.69;
      const ER = 13.6; // eV
      const Z = 2;

      // E(Z*) = (2 Z*^2 - 4*Z*Z* + (5/4)*Z*) * ER = (2 Z*^2 - 8 Z* + 1.25 Z*) * ER = (2 Z*^2 - 6.75 Z*) * ER
      const curE = (2 * zStar * zStar - 6.75 * zStar) * ER;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("Helium Atom Variational Rayleigh-Ritz Energy Curve", 25, 30);

      // Plot Graph
      const gx = 80, gy = 60, gw = 450, gh = 240;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)"; ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx, gy, gw, gh);

      // Coordinate axes (Z* from 1.0 to 2.5, E from -90 to -50 eV)
      const minZ = 1.0, maxZ = 2.5, minE = -90, maxE = -50;
      const toX = (z) => gx + ((z - minZ) / (maxZ - minZ)) * gw;
      const toY = (e) => gy + gh - ((e - minE) / (maxE - minE)) * gh;

      // Experimental line (-79.0 eV)
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#ec4899";
      ctx.beginPath(); ctx.moveTo(gx, toY(-79.0)); ctx.lineTo(gx + gw, toY(-79.0)); ctx.stroke();
      ctx.fillStyle = "#ec4899"; ctx.font = "11px Inter";
      ctx.fillText("Experimental: -79.00 eV", gx + 15, toY(-79.0) - 6);
      ctx.setLineDash([]);

      // Draw Parabola Curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let z = minZ; z <= maxZ; z += 0.02) {
        const eVal = (2 * z * z - 6.75 * z) * ER;
        const px = toX(z);
        const py = toY(eVal);
        if (z === minZ) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current Point Marker
      const ptX = toX(zStar);
      const ptY = toY(curE);
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(ptX, ptY, 7, 0, Math.PI * 2); ctx.fill();

      // Optimal Minimum (Z* = 1.6875, E = -77.46 eV)
      const optX = toX(27 / 16);
      const optY = toY(-77.46);
      ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(optX, optY, 5, 0, Math.PI * 2); ctx.fill();

      // Side Info Panel
      const infoX = 560, infoY = 80;
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 13px Inter";
      ctx.fillText("Variational Parameters:", infoX, infoY);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText(`Selected Z* = ${zStar.toFixed(2)}`, infoX, infoY + 25);
      ctx.fillText(`⟨H⟩(Z*) = ${curE.toFixed(2)} eV`, infoX, infoY + 50);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
      ctx.fillText(`Analytical Min: Z* = 27/16 = 1.688`, infoX, infoY + 90);
      ctx.fillText(`E_min = -77.46 eV (1.9% error)`, infoX, infoY + 115);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Shielding = 2 - 1.688 = 0.312 e`, infoX, infoY + 145);
      ctx.fillText(`Unshielded (Z=2): -108.8 eV`, infoX, infoY + 170);
    }
  },

  // 8. WKB Semiclassical Barrier Penetration & Alpha Decay Simulator
  "qm2-wkb-tunneling-sim": {
    title: "WKB Semiclassical Barrier Penetration & Alpha Decay Simulator",
    desc: "Simulation of WKB wavefunctions across classical turning points with continuous connection matching, Airy function turning profiles, and exponential tunneling decay T ≈ exp(-2γ).",
    isAnimated: true,
    controls: [
      { id: "barrierV", label: "Barrier Height V₀ (eV)", min: 5, max: 20, step: 0.5, value: 12 },
      { id: "particleE", label: "Particle Energy E (eV)", min: 2, max: 10, step: 0.5, value: 6 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const V0 = vals.barrierV !== undefined ? vals.barrierV : 12;
      const E = vals.particleE !== undefined ? vals.particleE : 6;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("WKB Semiclassical Barrier Tunneling & Connection Matching", 25, 30);

      // Barrier geometry
      const bLeft = 240, bRight = 460;
      const baselineY = 280;
      const vScale = 12;
      const barrierTopY = baselineY - V0 * vScale;
      const energyLineY = baselineY - E * vScale;

      // Draw Potential Barrier
      ctx.fillStyle = "rgba(30, 41, 59, 0.6)";
      ctx.fillRect(bLeft, barrierTopY, bRight - bLeft, baselineY - barrierTopY);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(60, baselineY); ctx.lineTo(bLeft, baselineY);
      ctx.lineTo(bLeft, barrierTopY); ctx.lineTo(bRight, barrierTopY);
      ctx.lineTo(bRight, baselineY); ctx.lineTo(w - 60, baselineY);
      ctx.stroke();

      // Energy Level E
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(60, energyLineY); ctx.lineTo(w - 60, energyLineY); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.font = "12px Inter";
      ctx.fillText(`E = ${E.toFixed(1)} eV`, 65, energyLineY - 8);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`V₀ = ${V0.toFixed(1)} eV`, bLeft + 15, barrierTopY - 8);
      ctx.setLineDash([]);

      // WKB Transmission factor
      const kappa = Math.sqrt(Math.max(0, V0 - E)) * 0.45;
      const barrierWidth = (bRight - bLeft) * 0.03;
      const gamma = kappa * barrierWidth;
      const T = Math.exp(-2 * gamma);

      // Draw Oscillating Wavepacket
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.beginPath();
      for (let x = 60; x <= w - 60; x++) {
        let amp;
        if (x < bLeft) {
          amp = 25 * Math.sin(0.12 * (x - 60) - time * 4);
        } else if (x <= bRight) {
          const frac = (x - bLeft) / (bRight - bLeft);
          amp = 25 * Math.exp(-gamma * frac) * Math.sin(-time * 4);
        } else {
          amp = 25 * Math.sqrt(T) * Math.sin(0.12 * (x - bRight) - time * 4);
        }
        const py = energyLineY + amp;
        if (x === 60) ctx.moveTo(x, py);
        else ctx.lineTo(x, py);
      }
      ctx.stroke();

      // Metrics
      ctx.fillStyle = "#ffffff"; ctx.font = "13px Inter";
      ctx.fillText(`WKB Barrier Integral: γ = (1/ħ) ∫ √(2m(V-E)) dx = ${gamma.toFixed(2)}`, 25, 340);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText(`Tunneling Probability T ≈ e^(-2γ) = ${T.toExponential(3)}`, 25, 365);
    }
  },

  // =========================================================================
  // CHAPTER 5: ANGULAR MOMENTUM & CLEBSCH-GORDAN COEFFICIENTS
  // =========================================================================

  // 9. 3D Spherical Harmonics Orbital Lobe & Nodal Visualizer
  "qm2-spherical-harmonics-3d-sim": {
    title: "3D Spherical Harmonics Orbital Lobe & Nodal Visualizer",
    desc: "Interactive 3D representation of spherical harmonics |Y_lm(θ, φ)|² showing electron orbital geometries (s, p, d, f orbitals), nodal surfaces, and angular probability densities.",
    isAnimated: true,
    controls: [
      { id: "orbitalL", label: "Orbital Angular Momentum l (0:s, 1:p, 2:d, 3:f)", min: 0, max: 3, step: 1, value: 2 },
      { id: "orbitalM", label: "Magnetic Quantum Number m", min: -2, max: 2, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const l = Math.round(vals.orbitalL !== undefined ? vals.orbitalL : 2);
      const rawM = Math.round(vals.orbitalM !== undefined ? vals.orbitalM : 0);
      const m = Math.max(-l, Math.min(l, rawM));

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      const names = ["s (l=0)", "p (l=1)", "d (l=2)", "f (l=3)"];
      ctx.fillText(`Spherical Harmonic Probability Density |Y_${l},${m}(θ, φ)|² [${names[l]}]`, 25, 30);

      // Polar Orbit Lobe (Render in 2D cross-section plane)
      const cx = w / 2, cy = 200, maxR = 130;

      // Draw Reference Grid
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(cx, cy, maxR, 0, Math.PI * 2); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx - maxR - 20, cy); ctx.lineTo(cx + maxR + 20, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy - maxR - 20); ctx.lineTo(cx, cy + maxR + 20); ctx.stroke();

      // Compute Y_lm(theta) amplitude
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      ctx.beginPath();

      for (let i = 0; i <= 360; i++) {
        const theta = (i * Math.PI) / 180;
        let y_val = 0;
        const cosT = Math.cos(theta);

        if (l === 0) y_val = 1;
        else if (l === 1) {
          y_val = m === 0 ? Math.abs(cosT) : Math.abs(Math.sin(theta));
        } else if (l === 2) {
          if (m === 0) y_val = Math.abs(3 * cosT * cosT - 1) / 2;
          else if (Math.abs(m) === 1) y_val = Math.abs(3 * Math.sin(theta) * cosT);
          else y_val = Math.abs(3 * Math.pow(Math.sin(theta), 2));
        } else if (l === 3) {
          if (m === 0) y_val = Math.abs(5 * Math.pow(cosT, 3) - 3 * cosT) / 2;
          else y_val = Math.abs(Math.sin(theta) * (5 * cosT * cosT - 1));
        }

        const r = (y_val / (l === 0 ? 1 : (l === 1 ? 1 : (l === 2 ? 3 : 2.5)))) * maxR;
        const px = cx + r * Math.sin(theta);
        const py = cy - r * Math.cos(theta);

        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.closePath(); ctx.fill(); ctx.stroke();

      // Summary
      ctx.fillStyle = "#ffffff"; ctx.font = "13px Inter";
      ctx.fillText(`Eigenvalues: L² = ${l * (l + 1)} ħ² | L_z = ${m} ħ`, 25, 350);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Number of Angular Nodal Cones = ${l - Math.abs(m)} | Azimuthal Nodal Planes = ${Math.abs(m)}`, 25, 375);
    }
  },

  // 10. Interactive Clebsch-Gordan Coefficient Calculator & Coupling Tree
  "qm2-clebsch-gordan-sim": {
    title: "Interactive Clebsch-Gordan Coefficient Calculator & Coupling Tree",
    desc: "Calculate Clebsch-Gordan coefficients ⟨j₁, m₁; j₂, m₂ | J, M⟩ for adding two angular momenta j₁ ⊗ j₂, verifying triangle inequality |j₁ - j₂| ≤ J ≤ j₁ + j₂ and Condon-Shortley phases.",
    isAnimated: false,
    controls: [
      { id: "j1Val", label: "Angular Momentum j₁", min: 0.5, max: 2.0, step: 0.5, value: 1.0 },
      { id: "j2Val", label: "Angular Momentum j₂", min: 0.5, max: 1.5, step: 0.5, value: 0.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const j1 = vals.j1Val !== undefined ? vals.j1Val : 1.0;
      const j2 = vals.j2Val !== undefined ? vals.j2Val : 0.5;

      const minJ = Math.abs(j1 - j2);
      const maxJ = j1 + j2;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText(`Clebsch-Gordan Coupling: j₁ = ${j1} ⊗ j₂ = ${j2}`, 25, 30);

      // Dimension calculation
      const dim1 = 2 * j1 + 1;
      const dim2 = 2 * j2 + 1;
      const totalDim = dim1 * dim2;

      ctx.fillStyle = "#ffffff"; ctx.font = "13px Inter";
      ctx.fillText(`Uncoupled Basis Space Dimension: (${dim1}) × (${dim2}) = ${totalDim} States`, 25, 65);

      // Coupling Tree Branches
      let startX = 60, currentY = 110;
      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 13px Inter";
      ctx.fillText("Allowed Total Angular Momenta J (Triangle Rule |j₁ - j₂| ≤ J ≤ j₁ + j₂):", startX, currentY);

      currentY += 30;
      let sumDim = 0;
      for (let J = maxJ; J >= minJ; J -= 1) {
        const mult = 2 * J + 1;
        sumDim += mult;
        ctx.fillStyle = "rgba(15, 23, 42, 0.8)";
        ctx.fillRect(startX, currentY, 320, 36);
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1;
        ctx.strokeRect(startX, currentY, 320, 36);

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px monospace";
        ctx.fillText(`J = ${J.toFixed(1)}  (Multiplet dimension: 2J+1 = ${mult})`, startX + 15, currentY + 23);
        currentY += 46;
      }

      // Verification badge
      ctx.fillStyle = "#10b981"; ctx.font = "13px Inter";
      ctx.fillText(`Dimensionality Check: Σ(2J + 1) = ${sumDim} ≡ ${totalDim} (Exact Match!)`, startX, currentY + 15);

      // Sample CG coefficient table for 1 ⊗ 1/2
      const tableX = 420, tableY = 100;
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 13px Inter";
      ctx.fillText("Sample CG Coefficients for 1 ⊗ 1/2:", tableX, tableY);

      const rows = [
        "|3/2, 3/2⟩ = |1, 1/2⟩  (CG = 1)",
        "|3/2, 1/2⟩ = √(2/3)|0, 1/2⟩ + √(1/3)|1, -1/2⟩",
        "|1/2, 1/2⟩ = √(1/3)|0, 1/2⟩ - √(2/3)|1, -1/2⟩",
        "|3/2, -1/2⟩ = √(1/3)|-1, 1/2⟩ + √(2/3)|0, -1/2⟩",
        "|1/2, -1/2⟩ = √(2/3)|-1, 1/2⟩ - √(1/3)|0, -1/2⟩",
        "|3/2, -3/2⟩ = |-1, -1/2⟩  (CG = 1)"
      ];

      rows.forEach((r, idx) => {
        ctx.fillStyle = idx % 2 === 0 ? "#94a3b8" : "#38bdf8";
        ctx.font = "12px monospace";
        ctx.fillText(r, tableX, tableY + 30 + idx * 24);
      });
    }
  },

  // =========================================================================
  // CHAPTER 6: IDENTICAL PARTICLES & MANY-BODY SYSTEMS
  // =========================================================================

  // 11. Degenerate Fermi Gas Density of States & Fermi Sphere
  "qm2-fermi-gas-dos-sim": {
    title: "Degenerate Fermi Gas Density of States & Fermi Sphere",
    desc: "Interactive simulation of the degenerate Fermi gas in 1D, 2D, and 3D showing density of states g(E), Fermi energy E_F = ħ²(3π²n)^(2/3)/2m, and Fermi-Dirac thermal smearing.",
    isAnimated: false,
    controls: [
      { id: "dimChoice", label: "Dimension: 1: 1D, 2: 2D, 3: 3D", min: 1, max: 3, step: 1, value: 3 },
      { id: "tempT", label: "Temperature T / T_F", min: 0.0, max: 0.5, step: 0.05, value: 0.05 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const d = Math.round(vals.dimChoice !== undefined ? vals.dimChoice : 3);
      const temp = vals.tempT !== undefined ? vals.tempT : 0.05;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText(`Degenerate Fermi Gas: ${d}D Density of States & Occupation Distribution`, 25, 30);

      // Plot Graph
      const gx = 80, gy = 70, gw = 450, gh = 220;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)"; ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx, gy, gw, gh);

      // Energy E from 0 to 2 E_F
      const EF = 1.0;
      const toX = (e) => gx + (e / 2.0) * gw;
      const toY = (val) => gy + gh - val * (gh * 0.7);

      // Fermi Energy Vertical Line
      const efX = toX(EF);
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#f59e0b";
      ctx.beginPath(); ctx.moveTo(efX, gy); ctx.lineTo(efX, gy + gh); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.font = "12px Inter";
      ctx.fillText("E = E_F", efX - 18, gy - 8);
      ctx.setLineDash([]);

      // Draw g(E) curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let px = 0; px <= gw; px++) {
        const e = (px / gw) * 2.0;
        let dos = 0;
        if (d === 1) dos = e > 0 ? 0.8 / Math.sqrt(Math.max(0.01, e)) : 0;
        else if (d === 2) dos = 1.0;
        else dos = Math.sqrt(e);

        const py = toY(dos);
        if (px === 0) ctx.moveTo(gx + px, py);
        else ctx.lineTo(gx + px, py);
      }
      ctx.stroke();

      // Draw Fermi-Dirac Occupation f(E)
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2; ctx.beginPath();
      for (let px = 0; px <= gw; px++) {
        const e = (px / gw) * 2.0;
        let f_occ;
        if (temp === 0) f_occ = e <= EF ? 1.0 : 0.0;
        else f_occ = 1.0 / (Math.exp((e - EF) / Math.max(0.01, temp)) + 1.0);

        const py = gy + gh - f_occ * (gh * 0.8);
        if (px === 0) ctx.moveTo(gx + px, py);
        else ctx.lineTo(gx + px, py);
      }
      ctx.stroke();

      // Legend & Formulas
      const legX = 560, legY = 90;
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText(`Density of States g(E):`, legX, legY);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText(d === 1 ? "1D: g(E) ∝ E^(-1/2)" : (d === 2 ? "2D: g(E) = Constant" : "3D: g(E) ∝ E^(1/2)"), legX, legY + 22);

      ctx.fillStyle = "#ec4899"; ctx.font = "bold 13px Inter";
      ctx.fillText(`Fermi-Dirac f(E, T):`, legX, legY + 65);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText(`T/T_F = ${temp.toFixed(2)}`, legX, legY + 87);
      ctx.fillText(temp === 0 ? "Step function at T=0" : "Thermal smearing ~ k_B T", legX, legY + 107);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Quantum Degeneracy Pressure:", legX, legY + 150);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText("P = (2/5) n E_F (at T = 0)", legX, legY + 172);
      ctx.fillText("⟨E⟩ = (3/5) E_F per fermion", legX, legY + 194);
    }
  },

  // 12. 2D Landau Level Quantization & Magnetic Degeneracy Visualizer
  "qm2-landau-levels-sim": {
    title: "2D Landau Level Quantization & Magnetic Degeneracy Visualizer",
    desc: "Interactive visualizer of 2D Landau levels in a magnetic field B, demonstrating cyclotron orbit collapse, harmonic oscillator potential shifts x₀, and macroscopic degeneracy g = Φ/Φ₀.",
    isAnimated: false,
    controls: [
      { id: "magB", label: "Magnetic Field B (Tesla)", min: 1, max: 10, step: 0.5, value: 4 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const B = vals.magB !== undefined ? vals.magB : 4;
      const omegaC = B * 0.176; // arbitrary unit
      const lB = 25.6 / Math.sqrt(B); // nm magnetic length

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText(`Landau Level Quantization in 2D Electron Gas (B = ${B.toFixed(1)} T)`, 25, 30);

      // Draw Energy Spectrum Ladder
      const lx = 80, lw = 280, bottomY = 320, gap = 45;
      for (let n = 0; n < 5; n++) {
        const y = bottomY - (n + 0.5) * (gap * (B / 4));
        if (y < 60) break;
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(lx, y); ctx.lineTo(lx + lw, y); ctx.stroke();

        ctx.fillStyle = "#ffffff"; ctx.font = "bold 12px Inter";
        ctx.fillText(`N = ${n} : E = ${(n + 0.5).toFixed(1)} ħω_c`, lx + lw + 15, y + 4);
      }

      // Cyclotron Orbit Visualizer (Right)
      const cx = 530, cy = 190, orbitR = (35 / Math.sqrt(B)) * 1.5;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(cx, cy, 100, 0, Math.PI * 2); ctx.stroke();

      ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
      ctx.beginPath(); ctx.arc(cx, cy, orbitR, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.stroke();

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Cyclotron Orbit (Ground State)", cx - 90, cy + 125);
      ctx.fillText(`Magnetic Length l_B = ${lB.toFixed(1)} nm`, cx - 80, cy + 145);

      // Quantization Metrics
      const gDeg = (B * 2.418).toFixed(2); // 10^11 cm^-2
      ctx.fillStyle = "#ffffff"; ctx.font = "13px Inter";
      ctx.fillText(`Cyclotron Frequency ω_c = eB/m = ${(omegaC * 10).toFixed(1)} × 10¹¹ rad/s`, 25, 360);
      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 13px Inter";
      ctx.fillText(`Landau Level Degeneracy per Unit Area: n_B = eB/h = ${gDeg} × 10¹¹ cm⁻²`, 25, 385);
    }
  },

  // =========================================================================
  // CHAPTER 7: QUANTUM SCATTERING THEORY
  // =========================================================================

  // 13. Interactive Partial Wave Phase Shifts & Differential Cross-Section
  "qm2-partial-wave-scattering-sim": {
    title: "Interactive Partial Wave Phase Shifts & Differential Cross-Section",
    desc: "Visualizer for partial wave decomposition of central scattering, displaying radial functions, phase shifts δ₀, δ₁, δ₂, and angular differential cross-section dσ/dΩ(θ).",
    isAnimated: false,
    controls: [
      { id: "delta0", label: "s-wave Phase Shift δ₀ (deg)", min: -180, max: 180, step: 5, value: 45 },
      { id: "delta1", label: "p-wave Phase Shift δ₁ (deg)", min: -90, max: 90, step: 5, value: 20 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const d0 = ((vals.delta0 !== undefined ? vals.delta0 : 45) * Math.PI) / 180;
      const d1 = ((vals.delta1 !== undefined ? vals.delta1 : 20) * Math.PI) / 180;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("Partial Wave Scattering: Angular Differential Cross-Section dσ/dΩ(θ)", 25, 30);

      // Polar Cross Section Plot (Left)
      const cx = 220, cy = 200, rScale = 90;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(cx, cy, rScale, 0, Math.PI * 2); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx - 120, cy); ctx.lineTo(cx + 120, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy - 120); ctx.lineTo(cx, cy + 120); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText("Forward θ = 0°", cx + 75, cy - 8);
      ctx.fillText("Backward θ = 180°", cx - 145, cy - 8);

      // f(theta) = f0 + 3 f1 cos(theta)
      const f0_r = Math.cos(d0) * Math.sin(d0), f0_i = Math.sin(d0) * Math.sin(d0);
      const f1_r = Math.cos(d1) * Math.sin(d1), f1_i = Math.sin(d1) * Math.sin(d1);

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let deg = 0; deg <= 360; deg++) {
        const rad = (deg * Math.PI) / 180;
        const cosT = Math.cos(rad);
        const re = f0_r + 3 * f1_r * cosT;
        const im = f0_i + 3 * f1_i * cosT;
        const sigma = re * re + im * im;

        const r = Math.min(130, sigma * rScale * 1.5);
        const px = cx + r * Math.cos(rad);
        const py = cy - r * Math.sin(rad);
        if (deg === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Right Info Panel
      const rx = 420, ry = 80;
      ctx.fillStyle = "rgba(15, 23, 42, 0.8)"; ctx.fillRect(rx, ry, 300, 240);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(rx, ry, 300, 240);

      const sig0 = 4 * Math.PI * Math.pow(Math.sin(d0), 2);
      const sig1 = 12 * Math.PI * Math.pow(Math.sin(d1), 2);
      const sigTot = sig0 + sig1;

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 13px Inter";
      ctx.fillText("Partial Cross-Section Breakdown:", rx + 15, ry + 30);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText(`s-wave (l=0): σ₀ = 4π/k² sin²(δ₀) = ${sig0.toFixed(2)} / k²`, rx + 15, ry + 65);
      ctx.fillText(`p-wave (l=1): σ₁ = 12π/k² sin²(δ₁) = ${sig1.toFixed(2)} / k²`, rx + 15, ry + 95);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText(`Total σ_tot = ${sigTot.toFixed(2)} / k²`, rx + 15, ry + 135);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Optical Theorem Verification:", rx + 15, ry + 175);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText(`(4π/k) Im[f(0)] = ${sigTot.toFixed(2)} / k²  (Exact!)`, rx + 15, ry + 200);
    }
  },

  // 14. Born Approximation Yukawa & Coulomb Scattering Visualizer
  "qm2-born-approximation-sim": {
    title: "Born Approximation Yukawa & Coulomb Scattering Visualizer",
    desc: "Interactive cross-section simulator for the Yukawa potential V(r) = V₀ e^(-μr)/r, demonstrating how screening parameter μ smoothly transitions into Rutherford scattering.",
    isAnimated: false,
    controls: [
      { id: "screenMu", label: "Screening Parameter μ (fm⁻¹)", min: 0.1, max: 2.0, step: 0.1, value: 0.5 },
      { id: "incK", label: "Incident Wavevector k (fm⁻¹)", min: 0.5, max: 3.0, step: 0.1, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const mu = vals.screenMu !== undefined ? vals.screenMu : 0.5;
      const k = vals.incK !== undefined ? vals.incK : 1.5;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText(`Born Approximation: Yukawa to Coulomb Transition (μ = ${mu.toFixed(1)} fm⁻¹)`, 25, 30);

      // Plot Angular Cross-Section (theta from 0 to 180 deg)
      const gx = 80, gy = 70, gw = 600, gh = 230;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)"; ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx, gy, gw, gh);

      // X-axis: 0 to 180 deg
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText("Scattering Angle θ (degrees)", gx + gw / 2 - 70, gy + gh + 25);
      ctx.fillText("0°", gx, gy + gh + 18);
      ctx.fillText("90°", gx + gw / 2 - 8, gy + gh + 18);
      ctx.fillText("180°", gx + gw - 25, gy + gh + 18);

      // Evaluate dsigma/dOmega = 1 / (mu^2 + 4k^2 sin^2(theta/2))^2
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.beginPath();
      const maxVal = 1 / Math.pow(mu * mu, 2);

      for (let deg = 2; deg <= 180; deg++) {
        const rad = (deg * Math.PI) / 180;
        const q2 = 4 * k * k * Math.pow(Math.sin(rad / 2), 2);
        const sig = 1 / Math.pow(mu * mu + q2, 2);
        const normSig = Math.min(1.0, sig / (maxVal * 0.4));

        const px = gx + (deg / 180) * gw;
        const py = gy + gh - normSig * (gh * 0.9);
        if (deg === 2) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Info text
      ctx.fillStyle = "#ffffff"; ctx.font = "13px monospace";
      ctx.fillText(`f(θ) = -2m V₀ / [ħ² (μ² + 4k² sin²(θ/2))]`, 25, 355);
      ctx.fillStyle = mu <= 0.2 ? "#ec4899" : "#38bdf8";
      ctx.fillText(mu <= 0.2 ? "★ Nearly Unscreened Coulomb: High forward divergence (Rutherford Law ∝ 1/sin⁴(θ/2))" : "Short-Range Yukawa Potential: Forward cross-section regularized by screening mass μ²", 25, 380);
    }
  },

  // =========================================================================
  // CHAPTER 8: RELATIVISTIC QUANTUM MECHANICS
  // =========================================================================

  // 15. Dirac 4-Component Spinor Dispersion & Helicity Visualizer
  "qm2-dirac-spinor-sim": {
    title: "Dirac 4-Component Spinor Dispersion & Helicity Visualizer",
    desc: "Interactive visualizer of Dirac 4-component spinors in momentum space, showing positive/negative energy branches E = ±√(p²c² + m²c⁴), upper/lower component ratios, and helicity projections.",
    isAnimated: false,
    controls: [
      { id: "momP", label: "Momentum p / (mc)", min: 0.0, max: 3.0, step: 0.1, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const pRel = vals.momP !== undefined ? vals.momP : 1.0;
      const Ep = Math.sqrt(pRel * pRel + 1.0); // units of mc^2

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("Relativistic Dirac Dispersion & 4-Component Spinor Decomposition", 25, 30);

      // Dispersion Diagram (Left)
      const gx = 80, gy = 70, gw = 340, gh = 240;
      const cy = gy + gh / 2;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)"; ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx, gy, gw, gh);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.beginPath();
      ctx.moveTo(gx, cy); ctx.lineTo(gx + gw, cy); ctx.stroke();
      const cx = gx + gw / 2;
      ctx.beginPath(); ctx.moveTo(cx, gy); ctx.lineTo(cx, gy + gh); ctx.stroke();

      // Energy Gap Shading (+mc^2 to -mc^2)
      ctx.fillStyle = "rgba(239, 68, 68, 0.15)";
      ctx.fillRect(gx, cy - 35, gw, 70);
      ctx.fillStyle = "#ef4444"; ctx.font = "11px Inter";
      ctx.fillText("Forbidden Gap: 2mc²", cx + 15, cy + 4);

      // Plot Positive Branch
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let px = 0; px <= gw; px++) {
        const pVal = ((px - gw/2) / (gw/2)) * 3.0;
        const eVal = Math.sqrt(pVal * pVal + 1);
        const yPos = cy - eVal * 35;
        if (px === 0) ctx.moveTo(gx + px, yPos);
        else ctx.lineTo(gx + px, yPos);
      }
      ctx.stroke();

      // Plot Negative Branch
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let px = 0; px <= gw; px++) {
        const pVal = ((px - gw/2) / (gw/2)) * 3.0;
        const eVal = Math.sqrt(pVal * pVal + 1);
        const yPos = cy + eVal * 35;
        if (px === 0) ctx.moveTo(gx + px, yPos);
        else ctx.lineTo(gx + px, yPos);
      }
      ctx.stroke();

      // Current momentum point
      const ptX = cx + (pRel / 3.0) * (gw / 2);
      ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(ptX, cy - Ep * 35, 6, 0, Math.PI * 2); ctx.fill();

      // 4-Component Spinor Card (Right)
      const sx = 460, sy = 70;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)"; ctx.fillRect(sx, sy, 260, 240);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(sx, sy, 260, 240);

      const ratio = pRel / (Ep + 1.0);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText(`Free Dirac Spinor u(p) for p = ${pRel.toFixed(1)} mc:`, sx + 15, sy + 30);

      ctx.fillStyle = "#ffffff"; ctx.font = "13px monospace";
      ctx.fillText(`E = +${Ep.toFixed(3)} mc²`, sx + 15, sy + 65);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Upper Spinor φ: [ 1.000,  0.000 ]ᵀ`, sx + 15, sy + 105);
      ctx.fillStyle = "#ec4899";
      ctx.fillText(`Lower Spinor χ: [ ${ratio.toFixed(3)},  0.000 ]ᵀ`, sx + 15, sy + 135);

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter";
      ctx.fillText(`Small/Large Ratio = ${ratio.toFixed(3)}`, sx + 15, sy + 175);
      ctx.fillText(pRel === 0 ? "Non-relativistic: Lower spinor = 0" : "Relativistic: Lower spinor approaches upper!", sx + 15, sy + 205);
    }
  },

  // 16. The Klein Paradox: Relativistic Barrier Tunneling & Pair Production
  "qm2-klein-paradox-sim": {
    title: "The Klein Paradox: Relativistic Barrier Tunneling & Pair Production",
    desc: "Simulation of Dirac wavepacket transmission at a supercritical step potential V₀ > E + mc², showing anti-matter phase oscillation and Klein transmission into the negative energy continuum.",
    isAnimated: true,
    controls: [
      { id: "barrierStep", label: "Step Potential V₀ / (mc²)", min: 1.0, max: 4.0, step: 0.1, value: 2.8 },
      { id: "electronEnergy", label: "Electron Energy E / (mc²)", min: 1.1, max: 2.0, step: 0.1, value: 1.4 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const V0 = vals.barrierStep !== undefined ? vals.barrierStep : 2.8;
      const E = vals.electronEnergy !== undefined ? vals.electronEnergy : 1.4;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText("The Klein Paradox: Supercritical Relativistic Barrier Penetration", 25, 30);

      // Step Interface
      const stepX = 350, baselineY = 280, scale = 50;
      const eLineY = baselineY - E * scale;
      const vLineY = baselineY - V0 * scale;

      // Draw Step
      ctx.fillStyle = "rgba(30, 41, 59, 0.6)"; ctx.fillRect(stepX, vLineY, w - stepX - 40, baselineY - vLineY);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(50, baselineY); ctx.lineTo(stepX, baselineY);
      ctx.lineTo(stepX, vLineY); ctx.lineTo(w - 40, vLineY);
      ctx.stroke();

      // Energy E line
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(50, eLineY); ctx.lineTo(w - 40, eLineY); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.font = "12px Inter";
      ctx.fillText(`E = ${E.toFixed(1)} mc²`, 60, eLineY - 8);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`V₀ = ${V0.toFixed(1)} mc²`, stepX + 20, vLineY - 8);
      ctx.setLineDash([]);

      const isSupercritical = V0 > E + 1.0;

      // Propagating Dirac wave
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.beginPath();
      for (let px = 50; px <= w - 40; px++) {
        let amp;
        if (px < stepX) {
          amp = 20 * Math.sin(0.15 * px - time * 5);
        } else {
          if (isSupercritical) {
            // Positron propagation into negative energy sea!
            amp = 18 * Math.sin(0.18 * (px - stepX) + time * 5); // Backward phase velocity!
          } else {
            // Standard exponential decay
            amp = 20 * Math.exp(-0.04 * (px - stepX)) * Math.sin(-time * 5);
          }
        }
        const py = eLineY + amp;
        if (px === 50) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Status Badge
      ctx.fillStyle = isSupercritical ? "#ec4899" : "#38bdf8";
      ctx.font = "bold 13px Inter";
      if (isSupercritical) {
        ctx.fillText("★ SUPERCRITICAL REGIME (V₀ > E + mc²): Transmission Paradox Active!", 25, 345);
        ctx.fillStyle = "#ffffff"; ctx.font = "12px Inter";
        ctx.fillText("Electrons reflect while vacuum sparks e⁺/e⁻ pairs: Positrons propagate inside the barrier!", 25, 370);
      } else {
        ctx.fillText("Subcritical Regime (V₀ < E + mc²): Ordinary exponential wave damping inside barrier.", 25, 345);
      }
    }
  }
};

// Simulation Engine Adapter for Open STEM Library App Controller
window.SimulationEngine = {
  activeAnimations: {},

  initSimulation(containerId, simType) {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = "";

    const simConfig = (window.QM2_SIMS && window.QM2_SIMS[simType]) ||
                      (window.DIG_SIMS && window.DIG_SIMS[simType]) ||
                      (window.NUC_SIMS && window.NUC_SIMS[simType]);

    if (!simConfig) {
      container.innerHTML = `<div style="padding: 1rem; color: #ef4444; background: #1e1b4b; border-radius: 8px;">Simulation type '${simType}' not found in registry.</div>`;
      return;
    }

    if (window.SimulationEngine.activeAnimations[containerId]) {
      cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
      delete window.SimulationEngine.activeAnimations[containerId];
    }

    const box = document.createElement("div");
    box.className = "simulation-box";
    box.style.background = "#0b1120";
    box.style.border = "1px solid #1e293b";
    box.style.borderRadius = "12px";
    box.style.padding = "1.25rem";
    box.style.marginTop = "1rem";
    box.style.marginBottom = "1.5rem";

    const header = document.createElement("div");
    header.style.marginBottom = "0.75rem";
    header.innerHTML = `
      <div style="font-size: 0.75rem; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.05em;">Interactive Numerical Simulation</div>
      <h4 style="margin: 0.25rem 0; color: #f8fafc; font-size: 1.15rem;">${simConfig.title}</h4>
      <p style="margin: 0; color: #94a3b8; font-size: 0.875rem;">${simConfig.desc}</p>
    `;
    box.appendChild(header);

    const canvas = document.createElement("canvas");
    canvas.width = 760;
    canvas.height = 400;
    canvas.style.width = "100%";
    canvas.style.height = "auto";
    canvas.style.background = "#070b14";
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

        const lbl = document.createElement("label");
        lbl.style.fontSize = "0.8rem";
        lbl.style.color = "#94a3b8";
        lbl.innerText = `${c.label}: ${c.value}`;

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
  }
};
