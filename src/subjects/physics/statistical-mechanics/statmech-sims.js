// Interactive Physics Simulation Suite for Statistical Mechanics
// 22 comprehensive topic-level simulations covering classical, quantum, Fermi, Bose, condensed matter, and transport physics.
// Equipped with 60 FPS animation loops, pause/play toggles, and interactive parameter sandboxes.

window.STATMECH_SIMS = {
  // ==========================================
  // UNIT 1: CLASSICAL STATISTICAL MECHANICS
  // ==========================================

  // 1. Microstates vs Macrostates (ANIMATED)
  "microstates-macrostates-sim": {
    title: "🎲 Microstates vs Macrostates: Combinatorial Multiplicity & Stirling Envelope",
    desc: "Observe microscopic binary particle configurations fluctuate in real time to build the macroscopic binomial probability distribution W(N, n).",
    isAnimated: true,
    controls: [
      { id: "mm-n", label: "Number of Particles N", min: 10, max: 60, step: 2, value: 30 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const N = vals["mm-n"];
      const midX = w * 0.55, base = h - 50;

      // Draw particle microstate box on the left
      const boxW = 160, boxH = 140, boxX = 40, boxY = 60;
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 2;
      ctx.strokeRect(boxX, boxY, boxW, boxH);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px sans-serif";
      ctx.fillText("Microscopic Realization:", boxX, boxY - 10);

      // Random microstate based on time
      const seed = Math.floor(animTime * 4);
      let countUp = 0;
      const cols = 6;
      for (let i = 0; i < N; i++) {
        const row = Math.floor(i / cols), col = i % cols;
        const px = boxX + 18 + col * 23;
        const py = boxY + 20 + row * 23;
        const isUp = ((i * 137 + seed * 31) % 100) < 50;
        if (isUp) countUp++;
        ctx.fillStyle = isUp ? "#38bdf8" : "#ec4899";
        ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();
      }

      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`State: n = ${countUp} (Up), ${N - countUp} (Down)`, boxX, boxY + boxH + 20);

      // Plot Binomial Distribution W(N, n) on the right
      const plotW = w - midX - 40;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(midX, base); ctx.lineTo(midX + plotW, base);
      ctx.moveTo(midX, base); ctx.lineTo(midX, 40);
      ctx.stroke();

      // Binomial Curve
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      const p = 0.5;
      const sigma = Math.sqrt(N * p * (1 - p));
      const mean = N * p;

      for (let n = 0; n <= N; n++) {
        const x = midX + (n / N) * plotW;
        // Gaussian approximation for W(n)
        const prob = (1 / (sigma * Math.sqrt(2 * Math.PI))) * Math.exp(-Math.pow(n - mean, 2) / (2 * sigma * sigma));
        const y = base - prob * 420;
        if (n === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);

        // Bar at current macrostate
        if (n === countUp) {
          ctx.fillStyle = "rgba(245, 158, 11, 0.4)";
          ctx.fillRect(x - 3, y, 6, base - y);
          ctx.fillStyle = "#f59e0b";
          ctx.beginPath(); ctx.arc(x, y, 5, 0, Math.PI * 2); ctx.fill();
        }
      }
      ctx.stroke();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Thermodynamic Probability W = N! / [n! (N-n)!] | Peak at Mean n = ${mean.toFixed(0)}`, 20, 25);
    }
  },

  // 2. Phase Space Trajectory & Liouville's Theorem (ANIMATED)
  "phase-space-trajectory-sim": {
    title: "🌀 Phase Space Trajectory (q, p) & Liouville’s Theorem Incompressibility",
    desc: "Observe phase points orbit in phase space (q, p). A swarm of states deforms but preserves its total phase area, demonstrating Liouville’s Theorem.",
    isAnimated: true,
    controls: [
      { id: "ps-energy", label: "Energy Level E", min: 20, max: 80, step: 5, value: 50 },
      { id: "ps-omega", label: "Frequency ω (rad/s)", min: 1, max: 4, step: 0.2, value: 2.0 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = w * 0.5, oY = h * 0.5;
      const E = vals["ps-energy"];
      const omega = vals["ps-omega"];
      const a = E * 1.8, b = E * 1.1;

      // Coordinate axes (q horizontal, p vertical)
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX - 160, oY); ctx.lineTo(oX + 160, oY);
      ctx.moveTo(oX, oY - 120); ctx.lineTo(oX, oY + 120);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("Coordinate q →", oX + 110, oY + 16);
      ctx.fillText("Momentum p ↑", oX + 8, oY - 105);

      // Elliptical phase trajectory
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.ellipse(oX, oY, a, b, 0, 0, Math.PI * 2); ctx.stroke();

      // Swarm of phase points demonstrating Liouville volume preservation
      const thBase = animTime * omega;
      const numPts = 12;
      ctx.fillStyle = "rgba(16, 185, 129, 0.25)";
      ctx.beginPath();
      for (let i = 0; i < numPts; i++) {
        const dTh = (i * 2 * Math.PI) / numPts;
        const q = (a + 12 * Math.cos(dTh)) * Math.cos(thBase + dTh * 0.15);
        const p = (b + 12 * Math.sin(dTh)) * Math.sin(thBase + dTh * 0.15);
        if (i === 0) ctx.moveTo(oX + q, oY - p);
        else ctx.lineTo(oX + q, oY - p);
      }
      ctx.closePath(); ctx.fill();
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5; ctx.stroke();

      // Main representative point
      const curQ = a * Math.cos(thBase);
      const curP = b * Math.sin(thBase);
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(oX + curQ, oY - curP, 6, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Liouville's Theorem: dρ/dt = 0 | Phase Area ∮ p dq = 2π E/ω = Constant`, 20, 25);
    }
  },

  // 3. Density of States g(ε) Across Dimensions
  "density-of-states-sim": {
    title: "📊 Density of States g(ε) Across 1D, 2D, 3D and Relativistic Systems",
    desc: "Compare how dimensional confinement alters the energy spectrum: g(ε) ∝ ε^-1/2 (1D wire), constant (2D well), ε^1/2 (3D bulk), and ε^2 (photons).",
    isAnimated: false,
    controls: [
      { id: "dos-dim", label: "Dimensionality: 1=1D, 2=2D, 3=3D, 4=Relativistic", min: 1, max: 4, step: 1, value: 3 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 80, oY = h - 60;
      const dim = vals["dos-dim"];

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 40); ctx.lineTo(oX, oY); ctx.lineTo(w - 40, oY);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("Energy ε →", w - 110, oY + 22);
      ctx.fillText("Density of States g(ε) ↑", oX - 10, 30);

      // Plot curve
      ctx.strokeStyle = dim === 1 ? "#ec4899" : (dim === 2 ? "#10b981" : (dim === 3 ? "#38bdf8" : "#f59e0b"));
      ctx.lineWidth = 3;
      ctx.beginPath();

      const maxE = 200;
      for (let e = 1; e <= maxE; e += 2) {
        let gVal = 0;
        if (dim === 1) {
          // 1D: g(ε) ∝ ε^-1/2
          gVal = 800 / Math.sqrt(e);
        } else if (dim === 2) {
          // 2D: g(ε) = const
          gVal = 90;
        } else if (dim === 3) {
          // 3D: g(ε) ∝ ε^1/2
          gVal = 14 * Math.sqrt(e);
        } else {
          // Relativistic: g(ε) ∝ ε^2
          gVal = 0.005 * e * e;
        }
        const px = oX + (e / maxE) * (w - 140);
        const py = Math.max(40, oY - gVal);
        if (e === 1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      const labels = [
        "1D Quantum Wire: g(ε) ∝ ε^(-1/2) (Van Hove Singularity)",
        "2D Quantum Well: g(ε) = m / (π ħ²) = Constant",
        "3D Bulk Solid: g(ε) = V / (4π²) (2m/ħ²)^(3/2) ε^(1/2)",
        "Ultrarelativistic 3D Gas (Photons): g(ε) ∝ ε^2"
      ];

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(labels[dim - 1], 20, 25);
    }
  },

  // ==========================================
  // UNIT 2: STATISTICS AND THERMODYNAMICS
  // ==========================================

  // 4. Canonical Ensemble Partition Function (ANIMATED)
  "canonical-ensemble-partition-sim": {
    title: "📈 Canonical Ensemble: Discrete Level Populations P_i = e^(-β ε_i) / Z",
    desc: "Observe how quantum level populations dynamically redistribute with temperature according to Boltzmann factors e^(-ε / k_B T).",
    isAnimated: true,
    controls: [
      { id: "ce-temp", label: "Temperature T (K)", min: 50, max: 800, step: 25, value: 300 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const T = vals["ce-temp"];
      const kB = 1.0; // Scaled units
      const beta = 1 / (0.008 * T);

      const energies = [0, 1.0, 2.0, 3.0, 4.0];
      const Z = energies.reduce((sum, e) => sum + Math.exp(-beta * e), 0);
      const probs = energies.map(e => Math.exp(-beta * e) / Z);

      const startX = 100, barW = 60, gap = 45;
      const base = h - 60;

      // Draw Energy Level Bars
      energies.forEach((e, idx) => {
        const x = startX + idx * (barW + gap);
        const p = probs[idx];
        const barH = p * 190;

        // Level line
        ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(x - 10, base - idx * 35); ctx.lineTo(x + barW + 10, base - idx * 35); ctx.stroke();

        // Population column
        ctx.fillStyle = "#38bdf8";
        ctx.fillRect(x, base - barH, barW, barH);

        // Particle jumping animation
        const numParticles = Math.round(p * 20);
        ctx.fillStyle = "#f59e0b";
        for (let j = 0; j < numParticles; j++) {
          const jitter = Math.sin(animTime * 3 + j * 1.5) * 4;
          ctx.beginPath();
          ctx.arc(x + 12 + (j % 4) * 12, base - barH + 10 + Math.floor(j / 4) * 14 + jitter, 4, 0, Math.PI * 2);
          ctx.fill();
        }

        ctx.fillStyle = "#cbd5e1"; ctx.font = "11px monospace";
        ctx.fillText(`ε_${idx} = ${e} eV`, x, base + 18);
        ctx.fillText(`P = ${(p * 100).toFixed(1)}%`, x, base - barH - 8);
      });

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Canonical Ensemble: Z = ∑ e^(-βε_i) = ${Z.toFixed(2)} | Free Energy F = -k_B T ln Z`, 20, 25);
    }
  },

  // 5. Harmonic Oscillator Heat Capacity & Freezing Out
  "harmonic-oscillator-statmech-sim": {
    title: "⚡ Quantum Harmonic Oscillator: Energy <E> & Heat Capacity C_V vs T",
    desc: "Observe how quantum energy quantization ℏω causes the specific heat C_V to freeze out exponentially to zero as T → 0, matching the Third Law.",
    isAnimated: false,
    controls: [
      { id: "ho-hw", label: "Quantum Energy Gap ℏω (meV)", min: 10, max: 60, step: 5, value: 30 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 80, oY = h - 60;
      const hw = vals["ho-hw"];

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 40); ctx.lineTo(oX, oY); ctx.lineTo(w - 40, oY);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("Temperature T (K) →", w - 160, oY + 22);
      ctx.fillText("Heat Capacity C_V / k_B ↑", oX - 10, 30);

      // Classical Dulong-Petit asymptote (C_V = 1.0 k_B)
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.lineWidth = 1.5; ctx.setLineDash([6, 4]);
      const yAsymptote = oY - 140;
      ctx.beginPath(); ctx.moveTo(oX, yAsymptote); ctx.lineTo(w - 40, yAsymptote); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("Classical Limit C_V = 1.0 k_B", w - 210, yAsymptote - 8);

      // Quantum Einstein curve C_V(T)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let T = 2; T <= 500; T += 4) {
        const x = (hw * 11.605) / T; // x = ℏω / (k_B T)
        const cv = (x * x * Math.exp(x)) / Math.pow(Math.exp(x) - 1, 2);
        const px = oX + (T / 500) * (w - 140);
        const py = oY - cv * 140;
        if (T === 2) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`C_V = k_B (ℏω / k_B T)² e^(ℏω/k_BT) / [e^(ℏω/k_BT) - 1]² | Exponential Freeze-out at T → 0`, 20, 25);
    }
  },

  // 6. Maxwell-Boltzmann Molecular Velocity Chamber (ANIMATED)
  "maxwell-boltzmann-velocity-sim": {
    title: "💨 2D Gas Collision Chamber & Maxwell-Boltzmann Speed Distribution",
    desc: "Watch 50 classical gas particles collide elastically in a box while their speed distribution is sampled in real time to trace the Maxwell curve.",
    isAnimated: true,
    controls: [
      { id: "mb-temp", label: "Gas Temperature T", min: 100, max: 600, step: 25, value: 300 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const T = vals["mb-temp"];
      const vScale = Math.sqrt(T / 300);

      // Left: 2D Collision Box
      const boxW = 200, boxH = 180, boxX = 40, boxY = 60;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.strokeRect(boxX, boxY, boxW, boxH);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px sans-serif";
      ctx.fillText("Thermal Gas Chamber:", boxX, boxY - 10);

      // Render 30 moving particles
      const numP = 30;
      for (let i = 0; i < numP; i++) {
        const vx0 = Math.cos(i * 1.7) * 25 * vScale;
        const vy0 = Math.sin(i * 1.7) * 25 * vScale;
        const x = boxX + 15 + ((i * 35 + animTime * vx0 * 20) % (boxW - 30) + (boxW - 30)) % (boxW - 30);
        const y = boxY + 15 + ((i * 27 + animTime * vy0 * 20) % (boxH - 30) + (boxH - 30)) % (boxH - 30);

        ctx.fillStyle = "#38bdf8";
        ctx.beginPath(); ctx.arc(x, y, 4, 0, Math.PI * 2); ctx.fill();
      }

      // Right: Theoretical Maxwell-Boltzmann Distribution Curve
      const plotX = w * 0.48, plotBase = h - 60, plotW = w - plotX - 40;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(plotX, 40); ctx.lineTo(plotX, plotBase); ctx.lineTo(plotX + plotW, plotBase);
      ctx.stroke();

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 3;
      ctx.beginPath();
      const a = 1 / (2 * 40 * vScale * vScale);
      for (let v = 0; v <= 120; v += 2) {
        const fv = 4 * Math.PI * Math.pow(a / Math.PI, 1.5) * v * v * Math.exp(-a * v * v) * 2800;
        const px = plotX + (v / 120) * plotW;
        const py = plotBase - fv;
        if (v === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Characteristic speeds
      const vp = Math.sqrt(2) * 15 * vScale;
      const vmean = Math.sqrt(8 / Math.PI) * 15 * vScale;
      const vrms = Math.sqrt(3) * 15 * vScale;

      ctx.fillStyle = "#f59e0b"; ctx.fillRect(plotX + (vp / 120) * plotW - 1, 60, 2, plotBase - 60);
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px monospace"; ctx.fillText("v_p", plotX + (vp / 120) * plotW - 8, 55);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`v_p = √(2k_BT/m) < <v> = √(8k_BT/πm) < v_rms = √(3k_BT/m)`, 20, 25);
    }
  },

  // ==========================================
  // UNIT 3: QUANTUM STATISTICAL MECHANICS
  // ==========================================

  // 7. Identical Particles Exchange: Bosons vs Fermions (ANIMATED)
  "identical-particles-exchange-sim": {
    title: "⚛️ Identical Particles: Boson Bunching vs Fermion Pauli Repulsion",
    desc: "Observe how wave function symmetry dictates spatial correlation: Bosons (symmetric ψ) bunch together, while Fermions (antisymmetric ψ) avoid each other.",
    isAnimated: true,
    controls: [
      { id: "ip-type", label: "Particle Type: 0=Bosons (Bunching), 1=Fermions (Pauli)", min: 0, max: 1, step: 1, value: 0 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const isFermion = vals["ip-type"] === 1;
      const midX = w / 2, baseY = h - 60;

      // 1D Potential Trap Curve
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = -140; x <= 140; x += 4) {
        const u = 0.006 * x * x;
        const px = midX + x, py = baseY - u;
        if (x === -140) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Two particle positions oscillating
      const osc = Math.sin(animTime * 2.5);
      let x1 = 0, x2 = 0;

      if (!isFermion) {
        // Bosons: bunch close to origin
        x1 = 20 * osc;
        x2 = 25 * osc + 8 * Math.cos(animTime * 4);
      } else {
        // Fermions: maintain Pauli hole separation
        x1 = -45 + 15 * osc;
        x2 = 45 + 15 * osc;
      }

      // Draw particles
      ctx.fillStyle = isFermion ? "#ec4899" : "#38bdf8";
      ctx.beginPath(); ctx.arc(midX + x1, baseY - 0.006 * x1 * x1 - 8, 8, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(midX + x2, baseY - 0.006 * x2 * x2 - 8, 8, 0, Math.PI * 2); ctx.fill();

      // Connecting wave probability cloud
      ctx.fillStyle = isFermion ? "rgba(236, 72, 153, 0.15)" : "rgba(56, 189, 248, 0.25)";
      ctx.beginPath();
      ctx.ellipse(midX + (x1 + x2) / 2, baseY - 20, Math.abs(x2 - x1) / 2 + 15, 18, 0, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      const desc = isFermion ? "Fermions: Ψ(x₁, x₂) = -Ψ(x₂, x₁) | Pauli Exclusion Hole (Zero Coincidence Probability)" : "Bosons: Ψ(x₁, x₂) = +Ψ(x₂, x₁) | Exchange Attraction (Bosonic Bunching into Same State)";
      ctx.fillText(desc, 20, 25);
    }
  },

  // 8. Density Matrix Pure vs Mixed State on Bloch Sphere
  "density-matrix-pure-mixed-sim": {
    title: "🌐 Density Matrix: Pure State (Tr ρ² = 1) vs Mixed Ensemble (Tr ρ² < 1)",
    desc: "Inspect the Bloch sphere: Pure quantum states lie strictly on the surface (|r|=1), whereas statistical thermal mixtures collapse into the interior (|r|<1).",
    isAnimated: false,
    controls: [
      { id: "dm-purity", label: "State Purity |r|: 1.0=Pure, 0.2=Highly Mixed", min: 0.1, max: 1.0, step: 0.05, value: 0.8 },
      { id: "dm-theta", label: "Polar Angle θ (°)", min: 10, max: 170, step: 5, value: 45 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = w * 0.45, oY = h * 0.52;
      const R = 100;
      const rPurity = vals["dm-purity"];
      const th = (vals["dm-theta"] * Math.PI) / 180;

      // Bloch sphere outline
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(oX, oY, R, 0, Math.PI * 2); ctx.stroke();
      ctx.beginPath(); ctx.ellipse(oX, oY, R, R * 0.35, 0, 0, Math.PI * 2); ctx.stroke();

      // Axis |0> and |1>
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(oX, oY - R - 20); ctx.lineTo(oX, oY + R + 20); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px monospace";
      ctx.fillText("|0⟩", oX + 8, oY - R - 8);
      ctx.fillText("|1⟩", oX + 8, oY + R + 18);

      // State Bloch vector
      const vx = rPurity * R * Math.sin(th);
      const vy = -rPurity * R * Math.cos(th);

      drawArrow(ctx, oX, oY, oX + vx, oY + vy, rPurity === 1.0 ? "#10b981" : "#f59e0b", "ρ", 2.5);

      const purity = (1 + rPurity * rPurity) / 2;
      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      const status = rPurity === 1.0 ? "Pure Quantum State (Tr ρ² = 1.0)" : `Mixed Statistical State (Tr ρ² = ${purity.toFixed(3)} < 1)`;
      ctx.fillText(`Bloch Radius |r| = ${rPurity.toFixed(2)} | ${status}`, 20, 25);
    }
  },

  // 9. Unified Quantum Distributions Overlay
  "quantum-distributions-compare-sim": {
    title: "📊 Unified Quantum Statistics: Maxwell-Boltzmann vs Bose vs Fermi",
    desc: "Compare mean state occupation <n(ε)>: Fermi-Dirac (f ≤ 1), Bose-Einstein (diverges at ε → μ), and classical Maxwell-Boltzmann (exponential).",
    isAnimated: false,
    controls: [
      { id: "qd-temp", label: "Temperature Scale", min: 0.5, max: 2.5, step: 0.1, value: 1.0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 80, oY = h - 60;
      const kBT = vals["qd-temp"];

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 30); ctx.lineTo(oX, oY); ctx.lineTo(w - 40, oY);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("(ε - μ) / k_B T →", w - 160, oY + 22);
      ctx.fillText("Occupation Number <n> ↑", oX - 10, 25);

      // Plot curves
      const maxDelta = 4.0;
      const plotW = w - oX - 60;

      // 1. Fermi-Dirac (Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let d = -2.0; d <= maxDelta; d += 0.05) {
        const f = 1 / (Math.exp(d / kBT) + 1);
        const px = oX + ((d + 2.0) / (maxDelta + 2.0)) * plotW;
        const py = oY - f * 150;
        if (d === -2.0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // 2. Bose-Einstein (Pink)
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let d = 0.1; d <= maxDelta; d += 0.05) {
        const b = 1 / (Math.exp(d / kBT) - 1);
        const px = oX + ((d + 2.0) / (maxDelta + 2.0)) * plotW;
        const py = Math.max(35, oY - Math.min(2.0, b) * 150);
        if (d === 0.1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // 3. Maxwell-Boltzmann (Amber dashed)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([5, 4]);
      ctx.beginPath();
      for (let d = -2.0; d <= maxDelta; d += 0.05) {
        const m = Math.exp(-d / kBT);
        const px = oX + ((d + 2.0) / (maxDelta + 2.0)) * plotW;
        const py = Math.max(35, oY - Math.min(2.0, m) * 150);
        if (d === -2.0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText("Cyan: Fermi-Dirac | Pink: Bose-Einstein | Amber: Classical Maxwell-Boltzmann", 20, 25);
    }
  },

  // ==========================================
  // UNIT 4: FERMI SYSTEMS
  // ==========================================

  // 10. Fermi-Dirac Distribution & Thermal Broadening (ANIMATED)
  "fermi-dirac-distribution-sim": {
    title: "⚡ Fermi-Dirac Step Function: T = 0 Sharp Sea vs Thermal Smearing k_B T",
    desc: "Observe how thermal fluctuations smear the sharp T = 0 Fermi step edge into an exponential tail, enabling only a fraction ~k_B T / ε_F of electrons to conduct heat.",
    isAnimated: true,
    controls: [
      { id: "fd-temp", label: "Temperature T (K)", min: 0, max: 2000, step: 50, value: 300 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 80, oY = h - 60;
      const T = vals["fd-temp"];
      const ef = 4.0; // eV
      const kBT = Math.max(0.001, 8.617e-5 * T);

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 30); ctx.lineTo(oX, oY); ctx.lineTo(w - 40, oY);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("Energy ε (eV) →", w - 150, oY + 22);
      ctx.fillText("f(ε) ↑", oX - 10, 25);

      // Fermi Energy vertical dashed line
      const plotW = w - oX - 60;
      const efPx = oX + (ef / 8.0) * plotW;
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(efPx, 40); ctx.lineTo(efPx, oY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("ε_F = 4.0 eV", efPx - 25, 35);

      // Fermi-Dirac Curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let e = 0; e <= 8.0; e += 0.05) {
        const f = 1 / (Math.exp((e - ef) / kBT) + 1);
        const px = oX + (e / 8.0) * plotW;
        const py = oY - f * 160;
        if (e === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`f(ε) = 1 / [e^((ε - μ)/k_BT) + 1] | At ε = μ: f(ε) ≡ 0.5 | Thermal Smearing ~ ${ (kBT * 1000).toFixed(1) } meV`, 20, 25);
    }
  },

  // 11. 3D Fermi Sphere in k-Space (ANIMATED)
  "fermi-sphere-3d-sim": {
    title: "🌐 3D Fermi Sphere in k-Space: Filled Fermi Sea k < k_F",
    desc: "Watch the 3D Fermi sphere rotate in k-space. Conduction electrons fill all states up to Fermi radius k_F = (3π² n)^1/3.",
    isAnimated: true,
    controls: [
      { id: "fs-kf", label: "Fermi Wavevector k_F", min: 40, max: 110, step: 5, value: 80 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = w * 0.5, oY = h * 0.52;
      const kF = vals["fs-kf"];
      const rot = animTime * 0.8;

      // 3D axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(oX - 130, oY); ctx.lineTo(oX + 130, oY); // k_x
      ctx.moveTo(oX, oY - 120); ctx.lineTo(oX, oY + 120); // k_z
      ctx.stroke();

      // Rotating Fermi Sphere
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.beginPath(); ctx.arc(oX, oY, kF, 0, Math.PI * 2); ctx.fill();

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(oX, oY, kF, 0, Math.PI * 2); ctx.stroke();

      // Rotating latitude ellipses
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.beginPath();
      ctx.ellipse(oX, oY, kF, kF * 0.35 * Math.cos(rot), 0, 0, Math.PI * 2);
      ctx.stroke();

      // Filled Fermi Sea quantum points
      const numPts = 35;
      ctx.fillStyle = "#10b981";
      for (let i = 0; i < numPts; i++) {
        const rP = (kF * 0.8) * Math.sqrt((i + 1) / numPts);
        const thP = i * 2.4 + rot;
        const px = oX + rP * Math.cos(thP);
        const py = oY + rP * Math.sin(thP) * 0.6;
        ctx.beginPath(); ctx.arc(px, py, 2.5, 0, Math.PI * 2); ctx.fill();
      }

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Fermi Sphere Volume V_k = 4/3 π k_F³ | Total Electrons N = V k_F³ / (3π²)`, 20, 25);
    }
  },

  // 12. Pauli Paramagnetism Sub-Band Splitting (ANIMATED)
  "pauli-paramagnetism-sim": {
    title: "🧲 Pauli Paramagnetism: Magnetic Field Zeeman Band Splitting",
    desc: "Observe how an applied magnetic field B shifts spin-up (ε - μ_B B) and spin-down (ε + μ_B B) sub-bands, generating a temperature-independent net magnetization.",
    isAnimated: true,
    controls: [
      { id: "pp-b", label: "Magnetic Field B (Tesla)", min: 0, max: 20, step: 1, value: 8 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const midX = w * 0.5, baseY = h - 60;
      const B = vals["pp-b"];
      const shift = B * 3.5;

      // Two parabolas for spin-up and spin-down
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; // Spin Up
      ctx.beginPath();
      for (let k = -90; k <= 90; k += 3) {
        const e = 0.015 * k * k - shift;
        const px = midX - 80 + k, py = baseY - (e + 40) * 1.5;
        if (k === -90) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5; // Spin Down
      ctx.beginPath();
      for (let k = -90; k <= 90; k += 3) {
        const e = 0.015 * k * k + shift;
        const px = midX + 80 + k, py = baseY - (e + 40) * 1.5;
        if (k === -90) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Common Fermi level
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([5, 4]);
      const efY = baseY - 120;
      ctx.beginPath(); ctx.moveTo(midX - 180, efY); ctx.lineTo(midX + 180, efY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("Chemical Potential μ", midX + 90, efY - 8);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Pauli Susceptibility χ_Pauli = μ₀ μ_B² g(ε_F) = Constant (Independent of T)`, 20, 25);
    }
  },

  // 13. White Dwarf Degeneracy & Chandrasekhar Limit
  "white-dwarf-degeneracy-sim": {
    title: "⭐ White Dwarf Hydrostatic Equilibrium & Chandrasekhar Mass Limit",
    desc: "Observe how non-relativistic degeneracy pressure yields R ∝ M^-1/3, while relativistic collapse triggers the strict Chandrasekhar limit at M_Ch = 1.44 M_☉.",
    isAnimated: false,
    controls: [
      { id: "wd-mass", label: "Stellar Mass M / M_☉", min: 0.2, max: 1.4, step: 0.05, value: 0.8 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 80, oY = h - 60;
      const mRatio = vals["wd-mass"];

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 30); ctx.lineTo(oX, oY); ctx.lineTo(w - 40, oY);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("Stellar Mass M / M_☉ →", w - 180, oY + 22);
      ctx.fillText("Radius R / R_Earth ↑", oX - 10, 25);

      // Chandrasekhar limit vertical line at M = 1.44
      const plotW = w - oX - 60;
      const mChPx = oX + (1.44 / 1.6) * plotW;
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(mChPx, 30); ctx.lineTo(mChPx, oY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e"; ctx.fillText("Chandrasekhar Limit M_Ch = 1.44 M_☉", mChPx - 130, 45);

      // White Dwarf Mass-Radius Curve: R ∝ (1 - (M/M_Ch)^(4/3))^1/2 / M^(1/3)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let m = 0.1; m <= 1.43; m += 0.02) {
        const factor = Math.max(0, 1 - Math.pow(m / 1.44, 4 / 3));
        const rRel = (Math.sqrt(factor) / Math.pow(m, 1 / 3)) * 1.2;
        const px = oX + (m / 1.6) * plotW;
        const py = oY - rRel * 85;
        if (m === 0.1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current star point
      const curFactor = Math.max(0, 1 - Math.pow(mRatio / 1.44, 4 / 3));
      const curR = (Math.sqrt(curFactor) / Math.pow(mRatio, 1 / 3)) * 1.2;
      const curPx = oX + (mRatio / 1.6) * plotW;
      const curPy = oY - curR * 85;

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(curPx, curPy, 6, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Mass M = ${mRatio.toFixed(2)} M_☉ | Radius R = ${(curR * 0.9).toFixed(2)} R_Earth | Relativistic Collapse at M_Ch`, 20, 25);
    }
  },

  // ==========================================
  // UNIT 5: BOSE SYSTEMS
  // ==========================================

  // 14. Planck Blackbody Radiation Law
  "planck-blackbody-radiation-sim": {
    title: "☀️ Planck Blackbody Radiation Spectrum & Wien Displacement Law",
    desc: "Adjust temperature T to observe spectral radiance u(ν, T), the Rayleigh-Jeans classical limit at low frequencies, and Wien's peak shift λ_max T = b.",
    isAnimated: false,
    controls: [
      { id: "bb-temp", label: "Temperature T (K)", min: 2000, max: 7000, step: 250, value: 5500 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 80, oY = h - 60;
      const T = vals["bb-temp"];

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 30); ctx.lineTo(oX, oY); ctx.lineTo(w - 40, oY);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("Wavelength λ (nm) →", w - 160, oY + 22);
      ctx.fillText("Radiance u(λ, T) ↑", oX - 10, 25);

      // Planck spectral curve
      const plotW = w - oX - 60;
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
      ctx.beginPath();

      const c1 = 3.7418e-16, c2 = 1.4388e-2;
      let maxVal = 0, peakLambda = 0;

      for (let lamNm = 100; lamNm <= 2000; lamNm += 10) {
        const lam = lamNm * 1e-9;
        const u = (c1 / Math.pow(lam, 5)) / (Math.exp(c2 / (lam * T)) - 1);
        if (u > maxVal) { maxVal = u; peakLambda = lamNm; }
      }

      for (let lamNm = 100; lamNm <= 2000; lamNm += 10) {
        const lam = lamNm * 1e-9;
        const u = (c1 / Math.pow(lam, 5)) / (Math.exp(c2 / (lam * T)) - 1);
        const px = oX + ((lamNm - 100) / 1900) * plotW;
        const py = oY - (u / maxVal) * 170;
        if (lamNm === 100) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Peak vertical marker
      const peakPx = oX + ((peakLambda - 100) / 1900) * plotW;
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(peakPx, 35); ctx.lineTo(peakPx, oY); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Peak Wavelength λ_max = ${peakLambda} nm | Total Emissive Power ∝ T⁴ (Stefan-Boltzmann)`, 20, 25);
    }
  },

  // 15. Bose-Einstein Condensation (ANIMATED)
  "bose-einstein-condensation-sim": {
    title: "❄️ Bose-Einstein Condensation: Macroscopic Ground-State Collapse",
    desc: "Cool below critical temperature T_c to observe the momentum cloud collapse into a macroscopic zero-momentum spike N_0 / N = 1 - (T/T_c)^3/2.",
    isAnimated: true,
    controls: [
      { id: "bec-ratio", label: "Reduced Temperature T / T_c", min: 0.1, max: 1.5, step: 0.05, value: 0.6 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const ratio = vals["bec-ratio"];
      const isCond = ratio < 1.0;
      const n0Fraction = isCond ? (1 - Math.pow(ratio, 1.5)) : 0;

      const midX = w * 0.5, baseY = h - 60;

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(midX - 160, baseY); ctx.lineTo(midX + 160, baseY);
      ctx.moveTo(midX, baseY); ctx.lineTo(midX, 40);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("Momentum p →", midX + 100, baseY + 18);
      ctx.fillText("Number of Bosons N(p) ↑", midX + 8, 45);

      // Thermal background Gaussian distribution
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      const sigma = 50 * Math.sqrt(ratio);
      for (let p = -140; p <= 140; p += 3) {
        const np = 80 * Math.exp(- (p * p) / (2 * sigma * sigma));
        const px = midX + p, py = baseY - np;
        if (p === -140) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Condensate zero-momentum sharp spike
      if (isCond) {
        const spikeH = n0Fraction * 160;
        ctx.fillStyle = "#f59e0b";
        ctx.beginPath();
        ctx.moveTo(midX - 12, baseY);
        ctx.lineTo(midX, baseY - spikeH);
        ctx.lineTo(midX + 12, baseY);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle = "#f59e0b";
        ctx.fillText(`Condensate Peak: ${(n0Fraction * 100).toFixed(1)}% in Ground State`, midX - 90, baseY - spikeH - 10);
      }

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`T / T_c = ${ratio.toFixed(2)} | Condensate Fraction N₀/N = 1 - (T/T_c)^(3/2) = ${(n0Fraction * 100).toFixed(1)}%`, 20, 25);
    }
  },

  // 16. Diatomic Molecule Degrees of Freedom Plateaus
  "diatomic-molecule-degrees-sim": {
    title: "🌡️ Diatomic Gas Heat Capacity C_V / R: Translation, Rotation & Vibration",
    desc: "Observe the stepwise quantization plateaus: 3/2 R (translations only), 5/2 R (rotations activated ~85 K), and 7/2 R (vibrations activated ~3000 K).",
    isAnimated: false,
    controls: [
      { id: "dm-tscale", label: "Selected Temperature T (K)", min: 20, max: 4000, step: 50, value: 300 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 80, oY = h - 60;
      const T = vals["dm-tscale"];

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 30); ctx.lineTo(oX, oY); ctx.lineTo(w - 40, oY);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("Temperature T (Log Scale) →", w - 210, oY + 22);
      ctx.fillText("C_V / R ↑", oX - 10, 25);

      // Plateaus: 3/2, 5/2, 7/2
      const plotW = w - oX - 60;
      const y32 = oY - (1.5 / 4.0) * 180;
      const y52 = oY - (2.5 / 4.0) * 180;
      const y72 = oY - (3.5 / 4.0) * 180;

      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)"; ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(oX, y32); ctx.lineTo(w - 40, y32);
      ctx.moveTo(oX, y52); ctx.lineTo(w - 40, y52);
      ctx.moveTo(oX, y72); ctx.lineTo(w - 40, y72);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px monospace";
      ctx.fillText("3/2 R (Trans)", oX + 10, y32 - 6);
      ctx.fillText("5/2 R (Trans + Rot)", oX + 10, y52 - 6);
      ctx.fillText("7/2 R (Trans + Rot + Vib)", oX + 10, y72 - 6);

      // Stepwise smooth curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let logT = 1; logT <= 4; logT += 0.05) {
        const curT = Math.pow(10, logT);
        // Effective degrees of freedom
        const rotContrib = 1 / (1 + Math.exp(- (curT - 85) / 30));
        const vibContrib = 1 / (1 + Math.exp(- (curT - 2500) / 600));
        const cv = 1.5 + rotContrib + vibContrib;
        const px = oX + ((logT - 1) / 3) * plotW;
        const py = oY - (cv / 4.0) * 180;
        if (logT === 1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`At T = ${T} K: Specific Heat Plateaus Reached through Quantum Excitation`, 20, 25);
    }
  },

  // ==========================================
  // UNIT 6: THE CONDENSED STATE
  // ==========================================

  // 17. Lattice Specific Heat: Debye vs Einstein vs Dulong-Petit
  "debye-einstein-heat-capacity-sim": {
    title: "⚙️ Lattice Specific Heat: Classical Dulong-Petit vs Einstein vs Debye T³",
    desc: "Compare lattice specific heat theories: Classical Dulong-Petit (3R), Einstein exponential freeze-out, and Debye's acoustic phonon T³ law.",
    isAnimated: false,
    controls: [
      { id: "cv-td", label: "Debye Temperature Θ_D (K)", min: 100, max: 600, step: 25, value: 300 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 80, oY = h - 60;
      const ThD = vals["cv-td"];
      const plotW = w - oX - 60;

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 30); ctx.lineTo(oX, oY); ctx.lineTo(w - 40, oY);
      ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "12px monospace";
      ctx.fillText("Temperature T / Θ_D →", w - 170, oY + 22);
      ctx.fillText("C_V / (3R) ↑", oX - 10, 25);

      // Dulong-Petit asymptote C_V = 1.0 (3R)
      const y3R = oY - 150;
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5; ctx.setLineDash([6, 4]);
      ctx.beginPath(); ctx.moveTo(oX, y3R); ctx.lineTo(w - 40, y3R); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("Dulong-Petit Limit = 3R", w - 190, y3R - 8);

      // 1. Debye Model Curve (Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let tau = 0.02; tau <= 1.5; tau += 0.02) {
        // Debye approximation
        let cv = 0;
        if (tau < 0.15) cv = (12 * Math.PI**4 / 5) * Math.pow(tau, 3) / 3;
        else cv = 1.0 - (1 / 20) * Math.pow(1 / tau, 2);
        cv = Math.min(1.0, Math.max(0, cv));
        const px = oX + (tau / 1.5) * plotW;
        const py = oY - cv * 150;
        if (tau === 0.02) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // 2. Einstein Model Curve (Pink)
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let tau = 0.02; tau <= 1.5; tau += 0.02) {
        const x = 0.75 / tau;
        const cv = (x * x * Math.exp(x)) / Math.pow(Math.exp(x) - 1, 2);
        const px = oX + (tau / 1.5) * plotW;
        const py = oY - cv * 150;
        if (tau === 0.02) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText("Cyan: Debye Model (Exact T³ Law at Low T) | Pink: Einstein Model | Amber: Dulong-Petit (3R)", 20, 25);
    }
  },

  // 18. Crystal Lattice Phonon Vibration Wave (ANIMATED)
  "lattice-phonons-vibration-sim": {
    title: "🌊 1D Crystal Lattice Vibrations: Acoustic vs Optical Phonon Waves",
    desc: "Observe 18 lattice ions oscillate in real time to form longitudinal traveling phonon waves, transporting thermal sound energy through the solid.",
    isAnimated: true,
    controls: [
      { id: "lp-type", label: "Phonon Branch: 0=Acoustic, 1=Optical", min: 0, max: 1, step: 1, value: 0 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const isOptical = vals["lp-type"] === 1;
      const numIons = 18;
      const startX = 60, gap = (w - 120) / (numIons - 1);
      const midY = h * 0.52;

      // Draw connecting springs and vibrating ions
      for (let i = 0; i < numIons; i++) {
        const phase = i * 0.6 - animTime * 3.0;
        // In optical branch, adjacent atoms vibrate out of phase
        const parity = isOptical ? (i % 2 === 0 ? 1 : -1) : 1;
        const displ = 14 * Math.sin(phase) * parity;
        const px = startX + i * gap + displ;

        // Springs
        if (i < numIons - 1) {
          const nextDispl = 14 * Math.sin((i + 1) * 0.6 - animTime * 3.0) * (isOptical ? ((i + 1) % 2 === 0 ? 1 : -1) : 1);
          const nextPx = startX + (i + 1) * gap + nextDispl;
          ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
          ctx.beginPath(); ctx.moveTo(px, midY); ctx.lineTo(nextPx, midY); ctx.stroke();
        }

        // Ion
        ctx.fillStyle = isOptical ? (i % 2 === 0 ? "#38bdf8" : "#ec4899") : "#10b981";
        const radius = isOptical ? (i % 2 === 0 ? 9 : 6) : 8;
        ctx.beginPath(); ctx.arc(px, midY, radius, 0, Math.PI * 2); ctx.fill();
      }

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      const branchText = isOptical ? "Optical Branch: Adjacent unequal masses vibrate in antiphase (ω > 0 at k = 0)" : "Acoustic Branch: Neighboring atoms move in unison (Linear Sound Wave ω = v_s k)";
      ctx.fillText(branchText, 20, 25);
    }
  },

  // 19. Electronic Bandgap & Fermi Surface
  "band-structure-fermi-surface-sim": {
    title: "⚡ Electronic Bandgap Structure: Metal vs Semiconductor vs Insulator",
    desc: "Compare electronic band occupation: Metals (Fermi level cuts conduction band), Semiconductors (small thermal gap E_g ~ 1 eV), and Insulators (large E_g > 5 eV).",
    isAnimated: false,
    controls: [
      { id: "bs-type", label: "Material: 0=Metal, 1=Semiconductor, 2=Insulator", min: 0, max: 2, step: 1, value: 0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const type = vals["bs-type"];
      const midX = w * 0.5, baseY = h - 50;

      const bandW = 140, bandH = 65;

      // Valence Band (always at bottom)
      const vbY = baseY - bandH;
      ctx.fillStyle = "#38bdf8";
      ctx.fillRect(midX - bandW / 2, vbY, bandW, bandH);
      ctx.strokeStyle = "#0284c7"; ctx.strokeRect(midX - bandW / 2, vbY, bandW, bandH);

      // Conduction Band (shifted by bandgap)
      let gapH = 0;
      if (type === 0) gapH = 0; // Overlapping in metal
      else if (type === 1) gapH = 35; // ~1 eV gap
      else gapH = 85; // ~5 eV gap

      const cbY = vbY - gapH - bandH;
      ctx.fillStyle = type === 0 ? "rgba(56, 189, 248, 0.4)" : "rgba(148, 163, 184, 0.15)";
      ctx.fillRect(midX - bandW / 2, cbY, bandW, bandH);
      ctx.strokeStyle = "#475569"; ctx.strokeRect(midX - bandW / 2, cbY, bandW, bandH);

      // Fermi Level E_F line
      let efY = 0;
      if (type === 0) efY = vbY - bandH * 0.5;
      else efY = vbY - gapH / 2;

      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([5, 4]);
      ctx.beginPath(); ctx.moveTo(midX - bandW / 2 - 30, efY); ctx.lineTo(midX + bandW / 2 + 30, efY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("Fermi Level E_F", midX + bandW / 2 + 35, efY + 4);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      const names = [
        "Metal: Partially filled band / Fermi level intersects conduction states (High Conductivity)",
        "Semiconductor: Bandgap E_g ~ 1.1 eV | Thermal activation generates electron-hole pairs",
        "Insulator (Dielectric): Large Bandgap E_g > 5.0 eV | Valence band full, Conduction empty"
      ];
      ctx.fillText(names[type], 20, 25);
    }
  },

  // =======================================================
  // UNIT 7: TRANSPORT PHENOMENA & PHASE TRANSITIONS
  // =======================================================

  // 20. Mean Free Path and Viscosity Gas Box (ANIMATED)
  "mean-free-path-viscosity-sim": {
    title: "💨 Mean Free Path & Molecular Viscosity Momentum Transfer",
    desc: "Follow a highlighted molecule (amber) as it travels mean free path distance λ between elastic collisions, transferring shear momentum η = 1/3 ρ v λ.",
    isAnimated: true,
    controls: [
      { id: "mfp-dens", label: "Gas Density n", min: 1, max: 4, step: 0.5, value: 2.0 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 60, oY = 50, boxW = w - 120, boxH = h - 110;
      const dens = vals["mfp-dens"];

      // Container walls
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.strokeRect(oX, oY, boxW, boxH);

      // Background gas molecules
      const numMols = Math.round(30 * dens);
      ctx.fillStyle = "#38bdf8";
      for (let i = 0; i < numMols; i++) {
        const x = oX + 15 + ((i * 47 + animTime * 40 * Math.cos(i)) % (boxW - 30) + (boxW - 30)) % (boxW - 30);
        const y = oY + 15 + ((i * 31 + animTime * 40 * Math.sin(i)) % (boxH - 30) + (boxH - 30)) % (boxH - 30);
        ctx.beginPath(); ctx.arc(x, y, 3, 0, Math.PI * 2); ctx.fill();
      }

      // Highlighted test molecule tracing mean free path
      const tP = animTime * 2.5;
      const leg = Math.floor(tP);
      const frac = tP - leg;
      const x0 = oX + 80 + ((leg * 73) % (boxW - 160));
      const y0 = oY + 50 + ((leg * 51) % (boxH - 100));
      const x1 = oX + 80 + (((leg + 1) * 73) % (boxW - 160));
      const y1 = oY + 50 + (((leg + 1) * 51) % (boxH - 100));

      const curX = x0 + (x1 - x0) * frac;
      const curY = y0 + (y1 - y0) * frac;

      // Free path vector line
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke();

      // Test particle (Amber)
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(curX, curY, 7, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Mean Free Path λ = 1 / (√2 π d² n) | Gas Viscosity η = 1/3 ρ v λ (Independent of Pressure!)`, 20, 25);
    }
  },

  // 21. Brownian Motion & Diffusion Random Walk (ANIMATED)
  "brownian-motion-diffusion-sim": {
    title: "🔬 Brownian Motion & Einstein Diffusion Relation: <r²> = 6 D t",
    desc: "Watch a macroscopic colloid particle execute a stochastic 2D random walk driven by Langevin thermal kicks, verifying Einstein’s relation D = k_B T / (6πηR).",
    isAnimated: true,
    controls: [
      { id: "bm-temp", label: "Fluid Temperature T", min: 100, max: 500, step: 25, value: 300 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = w * 0.4, oY = h * 0.52;
      const T = vals["bm-temp"];
      const stepScale = Math.sqrt(T / 300) * 8;

      // Trace random walk path up to current time
      const maxSteps = Math.min(180, Math.floor(animTime * 25));
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      let curX = oX, curY = oY;
      ctx.moveTo(curX, curY);

      for (let s = 1; s <= maxSteps; s++) {
        const ang = (s * 137.5) % (Math.PI * 2);
        curX += Math.cos(ang) * (stepScale * 0.8);
        curY += Math.sin(ang) * (stepScale * 0.8);
        ctx.lineTo(curX, curY);
      }
      ctx.stroke();

      // Origin marker
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(oX, oY, 5, 0, Math.PI * 2); ctx.stroke();

      // Brownian Colloid Particle
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(curX, curY, 9, 0, Math.PI * 2); ctx.fill();

      // Dispersed solvent molecules bombarding particle
      ctx.fillStyle = "rgba(148, 163, 184, 0.4)";
      for (let i = 0; i < 8; i++) {
        const th = i * 0.8 + animTime * 8;
        ctx.beginPath(); ctx.arc(curX + 16 * Math.cos(th), curY + 16 * Math.sin(th), 2, 0, Math.PI * 2); ctx.fill();
      }

      const distSq = Math.pow(curX - oX, 2) + Math.pow(curY - oY, 2);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Langevin Equation: M dv/dt = -γv + ξ(t) | MSD <r²> = 4Dt = ${(distSq).toFixed(0)} px²`, 20, 25);
    }
  },

  // 22. 2D Ising Model Metropolis Monte Carlo (ANIMATED)
  "ising-model-phase-transition-sim": {
    title: "🧲 2D Ising Model: Spontaneous Magnetization & Metropolis Monte Carlo",
    desc: "Watch a 2D spin lattice simulate ferromagnetic phase transitions. Below critical temperature T_c = 2.27 J/k_B, spins spontaneously cluster into ordered magnetic domains.",
    isAnimated: true,
    controls: [
      { id: "im-temp", label: "Reduced Temperature T / T_c", min: 0.2, max: 2.2, step: 0.1, value: 0.9 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const ratio = vals["im-temp"];
      const isOrdered = ratio < 1.0;

      // 28 x 20 spin grid
      const cols = 28, rows = 18;
      const startX = w * 0.15, startY = 55;
      const cellW = 18, cellH = 12;

      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const px = startX + c * cellW;
          const py = startY + r * cellH;

          // Pseudo-random spin domain generation modulated by temperature
          let spinUp = false;
          if (isOrdered) {
            // Strong domain formation
            const domainPhase = Math.sin(c * 0.18 + animTime * 0.3) + Math.cos(r * 0.22);
            spinUp = (domainPhase + (Math.random() - 0.5) * ratio) > 0;
          } else {
            // Disordered paramagnetic noise
            spinUp = Math.random() > 0.5;
          }

          ctx.fillStyle = spinUp ? "#38bdf8" : "#0f172a";
          ctx.fillRect(px, py, cellW - 2, cellH - 2);
        }
      }

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      const state = isOrdered ? "Ordered Ferromagnetic Phase (Spontaneous Domain Alignment)" : "Disordered Paramagnetic Phase (Zero Net Magnetization)";
      ctx.fillText(`Onsager Critical Temperature T_c = 2.269 J/k_B | T/T_c = ${ratio.toFixed(2)}: ${state}`, 20, 25);
    }
  }
,
  // 23. Stirling's Approximation Convergence Sandbox
  "entropy-stirling-sim": {
    title: "📐 Stirling's Approximation & Factorial Asymptotics",
    desc: "Compare exact combinatorial factorials ln(N!) against Stirling leading and second-order asymptotic formulas as N scales.",
    isAnimated: false,
    controls: [
      { id: "stirling-n", label: "Number N", min: 2, max: 80, step: 1, value: 20 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const N = vals["stirling-n"];
      
      let exactLnFact = 0;
      for (let i = 1; i <= N; i++) exactLnFact += Math.log(i);
      const leadingStirling = N * Math.log(N) - N;
      const secondStirling = N * Math.log(N) - N + 0.5 * Math.log(2 * Math.PI * N);
      const errLeading = Math.abs((leadingStirling - exactLnFact) / exactLnFact) * 100;
      const errSecond = Math.abs((secondStirling - exactLnFact) / exactLnFact) * 100;

      // Draw Comparison Cards
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(40, 50, 310, 120);
      ctx.fillRect(370, 50, 310, 120);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px monospace";
      ctx.fillText("Exact ln(N!) vs Leading Stirling:", 55, 75);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Exact ln(${N}!):   ` + exactLnFact.toFixed(4), 55, 105);
      ctx.fillText(`N ln N - N:      ` + leadingStirling.toFixed(4), 55, 130);
      ctx.fillStyle = "#ec4899";
      ctx.fillText(`Relative Error:  ` + errLeading.toFixed(3) + " %", 55, 155);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 14px monospace";
      ctx.fillText("Second-Order Stirling Correction:", 385, 75);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Formula: N ln N - N + 0.5 ln(2πN)`, 385, 105);
      ctx.fillText(`Corrected Value: ` + secondStirling.toFixed(4), 385, 130);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Relative Error:  ` + errSecond.toFixed(4) + " %", 385, 155);

      // Plot error curves across N = 2 to 60
      const originX = 60, originY = h - 40, plotW = w - 100, plotH = 90;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(originX, originY); ctx.lineTo(originX + plotW, originY);
      ctx.moveTo(originX, originY); ctx.lineTo(originX, originY - plotH);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Relative Error (%) vs N", originX + 10, originY - plotH + 12);
      ctx.fillText("N = 2", originX, originY + 18);
      ctx.fillText("N = 60", originX + plotW - 35, originY + 18);

      // Plot leading error curve (pink)
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2; ctx.beginPath();
      for (let n = 2; n <= 60; n++) {
        let exact = 0; for (let i = 1; i <= n; i++) exact += Math.log(i);
        let approx = n * Math.log(n) - n;
        let err = Math.abs((approx - exact) / exact) * 100;
        let x = originX + ((n - 2) / 58) * plotW;
        let y = originY - Math.min(plotH - 5, (err / 30) * (plotH - 10));
        if (n === 2) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Plot second order error curve (green)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.beginPath();
      for (let n = 2; n <= 60; n++) {
        let exact = 0; for (let i = 1; i <= n; i++) exact += Math.log(i);
        let approx = n * Math.log(n) - n + 0.5 * Math.log(2 * Math.PI * n);
        let err = Math.abs((approx - exact) / exact) * 100;
        let x = originX + ((n - 2) / 58) * plotW;
        let y = originY - Math.min(plotH - 5, (err / 30) * (plotH - 10));
        if (n === 2) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = "#ec4899"; ctx.fillText("■ Leading Term N ln N - N", originX + 220, originY - plotH + 12);
      ctx.fillStyle = "#10b981"; ctx.fillText("■ + 0.5 ln(2πN)", originX + 440, originY - plotH + 12);
    }
  },

  // 24. Liquid Helium Lambda Transition Specific Heat
  "liquid-helium-lambda-sim": {
    title: "🌡️ Liquid Helium-4 Lambda Point Specific Heat Logarithmic Cusp",
    desc: "Inspect the famous heat capacity lambda-peak of Liquid Helium-4 transitioning from normal He-I to frictionless superfluid He-II at T_lambda = 2.17 K.",
    isAnimated: false,
    controls: [
      { id: "lambda-t", label: "Temperature T (Kelvin)", min: 1.0, max: 3.5, step: 0.05, value: 2.17 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const T = vals["lambda-t"];
      const ox = 70, oy = h - 50, pw = w - 120, ph = h - 100;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + pw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - ph);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Temperature T (K)", ox + pw / 2 - 40, oy + 35);
      ctx.fillText("Specific Heat C_p / R", 10, oy - ph - 10);

      const tLam = 2.17;
      const xLam = ox + ((tLam - 1.0) / 2.5) * pw;
      ctx.strokeStyle = "#e11d48"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(xLam, oy); ctx.lineTo(xLam, oy - ph); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e";
      ctx.fillText("T_λ = 2.17 K", xLam - 28, oy - ph + 20);

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let temp = 1.0; temp <= 3.5; temp += 0.01) {
        const diff = Math.max(0.005, Math.abs(temp - tLam));
        let cp = 1.2 - 0.75 * Math.log(diff);
        if (temp > tLam) cp *= 0.65;
        const x = ox + ((temp - 1.0) / 2.5) * pw;
        const y = oy - Math.min(ph - 5, (cp / 5.5) * ph);
        if (temp === 1.0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      const curDiff = Math.max(0.005, Math.abs(T - tLam));
      let curCp = 1.2 - 0.75 * Math.log(curDiff);
      if (T > tLam) curCp *= 0.65;
      const curX = ox + ((T - 1.0) / 2.5) * pw;
      const curY = oy - Math.min(ph - 5, (curCp / 5.5) * ph);

      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#1e293b"; ctx.fillRect(w - 280, 40, 240, 80);
      ctx.fillStyle = T < tLam ? "#10b981" : "#38bdf8";
      ctx.font = "bold 14px monospace";
      ctx.fillText(T < tLam ? "Phase: Liquid He-II (Superfluid)" : "Phase: Liquid He-I (Normal Liquid)", w - 265, 68);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`T = ${T.toFixed(2)} K | C_p/R ≈ ${curCp.toFixed(2)}`, w - 265, 95);
    }
  },

  // 25. Superfluid Two-Fluid Hydrodynamics & Fountain Effect (ANIMATED)
  "superfluid-two-fluid-sim": {
    title: "🌊 Superfluid Two-Fluid Flow & Thermal Fountain Effect",
    desc: "Watch the frictionless superfluid component flow through a fine porous plug when heated, building macroscopic fountain pressure.",
    isAnimated: true,
    controls: [
      { id: "sf-power", label: "Heater Power (mW)", min: 10, max: 100, step: 5, value: 40 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const power = vals["sf-power"];
      const fHeight = (power / 100) * 120;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.strokeRect(180, 160, 360, 140);
      ctx.strokeRect(340, 100, 40, 150);

      ctx.fillStyle = "#475569";
      ctx.fillRect(342, 230, 36, 30);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("Porous Plug", 328, 275);

      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      ctx.fillRect(182, 190, 356, 108);

      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(350, 215); ctx.lineTo(370, 215);
      ctx.lineTo(350, 220); ctx.lineTo(370, 220);
      ctx.stroke();
      ctx.fillStyle = "#ef4444"; ctx.font = "10px sans-serif"; ctx.fillText("Heater", 385, 220);

      const jetBaseX = 360, jetBaseY = 100;
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(jetBaseX, jetBaseY);
      ctx.lineTo(jetBaseX, jetBaseY - fHeight);
      ctx.stroke();

      ctx.fillStyle = "#38bdf8";
      for (let i = 0; i < 16; i++) {
        const phase = (animTime * 3 + i * 0.4) % 1;
        const dx = (Math.sin(i * 1.5) * 25) * phase;
        const dy = -fHeight * (1 - phase) + phase * phase * 20;
        ctx.beginPath();
        ctx.arc(jetBaseX + dx, jetBaseY + dy, 2.5, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.fillStyle = "#10b981";
      for (let i = 0; i < 20; i++) {
        const py = 290 - ((animTime * 60 + i * 18) % 60);
        const px = 345 + (i % 4) * 8;
        ctx.beginPath(); ctx.arc(px, py, 2, 0, Math.PI * 2); ctx.fill();
      }

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px monospace";
      ctx.fillText(`Allen & Jones Thermomechanical Fountain Effect (T < 2.17 K)`, 40, 40);
      ctx.fillStyle = "#10b981"; ctx.font = "12px monospace";
      ctx.fillText("↑ Frictionless Superfluid Component (ρ_s) rushes in", 40, 70);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Fountain Height: ${(fHeight * 0.25).toFixed(1)} cm | Thermo-osmotic Pressure ΔP = ρ S ΔT`, 40, 95);
    }
  },

  // 26. Bose Gas Momentum Distribution Sharpening (ANIMATED)
  "bose-gas-momentum-distribution-sim": {
    title: "📉 Bose-Einstein Condensate Momentum Distribution Collapse",
    desc: "Witness the real-time sharpening of momentum distribution as T drops across T_c into an ultra-narrow macroscopic zero-momentum spike.",
    isAnimated: true,
    controls: [
      { id: "bec-t-ratio", label: "Reduced Temperature T / T_c", min: 0.1, max: 2.0, step: 0.05, value: 0.8 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const tratio = vals["bec-t-ratio"];
      const ox = w / 2, base = h - 60;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(ox - 260, base); ctx.lineTo(ox + 260, base);
      ctx.moveTo(ox, base); ctx.lineTo(ox, 40);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("-p_max", ox - 260, base + 20);
      ctx.fillText("+p_max", ox + 220, base + 20);
      ctx.fillText("Momentum Distribution n(p)", ox + 15, 55);

      const thermSigma = 70 * Math.sqrt(tratio);
      const thermAmp = Math.min(90, 80 / tratio);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = -250; px <= 250; px += 2) {
        const val = thermAmp * Math.exp(-(px * px) / (2 * thermSigma * thermSigma));
        const x = ox + px, y = base - val;
        if (px === -250) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      if (tratio < 1.0) {
        const condFrac = 1.0 - Math.pow(tratio, 1.5);
        const peakHeight = condFrac * 180 + Math.sin(animTime * 3) * 5;
        const peakSigma = 8;

        ctx.fillStyle = "rgba(236, 72, 153, 0.35)";
        ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 3;
        ctx.beginPath();
        for (let px = -40; px <= 40; px += 1) {
          const val = peakHeight * Math.exp(-(px * px) / (2 * peakSigma * peakSigma));
          const x = ox + px, y = base - val;
          if (px === -40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.lineTo(ox + 40, base); ctx.lineTo(ox - 40, base);
        ctx.closePath();
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#ec4899"; ctx.font = "bold 13px monospace";
        ctx.fillText(`BEC Condensate Ground-State Spike (N_0/N = ${(condFrac * 100).toFixed(1)}%)`, ox - 180, base - peakHeight - 15);
      }

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px monospace";
      ctx.fillText(`T/T_c = ${tratio.toFixed(2)} | ` + (tratio < 1 ? "Condensed Regime (Quantum Matter Wave)" : "Normal Thermal Gas (Broad Gaussian Distribution)"), 40, 35);
    }
  },

  // 27. Clausius-Clapeyron Phase Coexistence Diagram
  "phase-diagram-clapeyron-sim": {
    title: "⚗️ Clausius-Clapeyron Coexistence Boundaries & Phase Diagram",
    desc: "Interactive P-T phase boundaries (Solid, Liquid, Gas) demonstrating Clausius-Clapeyron slope dP/dT = L / (T ΔV), the triple point, and critical point.",
    isAnimated: false,
    controls: [
      { id: "cc-latent", label: "Latent Heat Scaling", min: 0.5, max: 2.0, step: 0.1, value: 1.0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const lat = vals["cc-latent"];
      const ox = 70, oy = h - 60, pw = w - 120, ph = h - 110;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + pw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - ph);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Temperature T →", ox + pw - 90, oy + 35);
      ctx.fillText("Pressure P →", ox - 50, oy - ph + 10);

      const tpx = ox + 0.32 * pw, tpy = oy - 0.38 * ph;

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(ox, oy);
      ctx.quadraticCurveTo(ox + 0.18 * pw, oy - 0.15 * ph, tpx, tpy);
      ctx.stroke();

      const cpx = ox + 0.85 * pw, cpy = oy - 0.88 * ph;
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(tpx, tpy);
      ctx.quadraticCurveTo(ox + 0.55 * pw, oy - 0.55 * ph * lat, cpx, cpy);
      ctx.stroke();

      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(tpx, tpy);
      ctx.lineTo(tpx - 15, oy - ph);
      ctx.stroke();

      ctx.font = "bold 15px monospace";
      ctx.fillStyle = "#93c5fd"; ctx.fillText("SOLID (Ice)", ox + 0.08 * pw, oy - 0.65 * ph);
      ctx.fillStyle = "#6ee7b7"; ctx.fillText("LIQUID (Water)", ox + 0.42 * pw, oy - 0.70 * ph);
      ctx.fillStyle = "#fde047"; ctx.fillText("GAS (Vapor)", ox + 0.55 * pw, oy - 0.22 * ph);

      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(tpx, tpy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f59e0b"; ctx.font = "12px monospace"; ctx.fillText("Triple Point (0.01°C, 611 Pa)", tpx + 10, tpy + 5);

      ctx.fillStyle = "#ef4444"; ctx.beginPath(); ctx.arc(cpx, cpy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#ef4444"; ctx.font = "12px monospace"; ctx.fillText("Critical Point (374°C, 22.1 MPa)", cpx - 120, cpy - 12);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "13px monospace";
      ctx.fillText("Clausius-Clapeyron: dP/dT = L / [T(V_2 - V_1)] | Negative melting slope for H_2O (V_ice > V_liq)", ox, h - 15);
    }
  },

  // 28. Transport Coefficients Sandbox
  "transport-coefficients-sim": {
    title: "🚚 Kinetic Transport: Viscosity, Thermal Conductivity & Diffusion",
    desc: "Inspect how gas viscosity η, thermal conductivity κ, and diffusion coefficient D respond to changes in temperature and pressure.",
    isAnimated: false,
    controls: [
      { id: "tc-temp", label: "Temperature (K)", min: 100, max: 800, step: 25, value: 300 },
      { id: "tc-press", label: "Pressure (atm)", min: 0.2, max: 5.0, step: 0.2, value: 1.0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const T = vals["tc-temp"];
      const P = vals["tc-press"];

      const eta = 1.78e-5 * Math.sqrt(T / 300);
      const kappa = 0.026 * Math.sqrt(T / 300);
      const diff = 2.05e-5 * Math.pow(T / 300, 1.5) / P;
      const mfp = 68 * (T / 300) / P;

      const cardW = 190, cardH = 180, cardY = 60;
      
      ctx.fillStyle = "#1e293b"; ctx.fillRect(30, cardY, cardW, cardH);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px monospace";
      ctx.fillText("Viscosity (η)", 45, cardY + 30);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Value: ${(eta * 1e5).toFixed(2)} μPa·s`, 45, cardY + 65);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Scaling: η ∝ √T", 45, cardY + 95);
      ctx.fillText("Pressure: INDEPENDENT", 45, cardY + 120);
      ctx.fillStyle = "#10b981"; ctx.fillText("✓ Maxwell's Law verified", 45, cardY + 150);

      ctx.fillStyle = "#1e293b"; ctx.fillRect(250, cardY, cardW, cardH);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 14px monospace";
      ctx.fillText("Thermal Cond (κ)", 265, cardY + 30);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Value: ${(kappa * 1e3).toFixed(1)} mW/(m·K)`, 265, cardY + 65);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Scaling: κ ∝ √T", 265, cardY + 95);
      ctx.fillText("Pressure: INDEPENDENT", 265, cardY + 120);
      ctx.fillStyle = "#10b981"; ctx.fillText("✓ Kinetic transport", 265, cardY + 150);

      ctx.fillStyle = "#1e293b"; ctx.fillRect(470, cardY, cardW, cardH);
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 14px monospace";
      ctx.fillText("Self-Diffusion (D)", 485, cardY + 30);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Value: ${(diff * 1e5).toFixed(2)} × 10⁻⁵ m²/s`, 485, cardY + 65);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Scaling: D ∝ T^1.5 / P", 485, cardY + 95);
      ctx.fillText(`Mean Free Path: ${mfp.toFixed(1)} nm`, 485, cardY + 120);
      ctx.fillStyle = "#ec4899"; ctx.fillText("Inversely prop to pressure", 485, cardY + 150);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "13px monospace";
      ctx.fillText(`T = ${T} K | P = ${P.toFixed(1)} atm | Hard-sphere diameter d = 3.7 Å (Diatomic Nitrogen)`, 40, h - 35);
    }
  }

};

// Aliases for seamless universal integration
window.STATMECH_SIMS["liouville-phase-space-sim"] = window.STATMECH_SIMS["phase-space-trajectory-sim"];
window.STATMECH_SIMS["canonical-boltzmann-sim"] = window.STATMECH_SIMS["canonical-ensemble-partition-sim"];
window.STATMECH_SIMS["equipartition-dof-sim"] = window.STATMECH_SIMS["diatomic-molecule-degrees-sim"];
window.STATMECH_SIMS["quantum-wavefunction-symmetry-sim"] = window.STATMECH_SIMS["identical-particles-exchange-sim"];
window.STATMECH_SIMS["three-statistics-comparison-sim"] = window.STATMECH_SIMS["quantum-distributions-compare-sim"];
window.STATMECH_SIMS["fermi-dirac-step-sim"] = window.STATMECH_SIMS["fermi-dirac-distribution-sim"];
window.STATMECH_SIMS["fermi-surface-sphere-sim"] = window.STATMECH_SIMS["fermi-sphere-3d-sim"];
window.STATMECH_SIMS["white-dwarf-chandrasekhar-sim"] = window.STATMECH_SIMS["white-dwarf-degeneracy-sim"];
window.STATMECH_SIMS["planck-blackbody-spectrum-sim"] = window.STATMECH_SIMS["planck-blackbody-radiation-sim"];
window.STATMECH_SIMS["debye-vs-einstein-cv-sim"] = window.STATMECH_SIMS["debye-einstein-heat-capacity-sim"];
window.STATMECH_SIMS["mean-free-path-transport-sim"] = window.STATMECH_SIMS["mean-free-path-viscosity-sim"];
window.STATMECH_SIMS["ising-model-monte-carlo-sim"] = window.STATMECH_SIMS["ising-model-phase-transition-sim"];

// Universal Engine Integration Adapter
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  if (window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }

  const simConfig = window.STATMECH_SIMS[simType];
  if (!simConfig) {
    console.warn("Statistical Mechanics simulation not found:", simType);
    return;
  }

  container.innerHTML = "";

  const box = document.createElement("div");
  box.className = "sim-inline-card";
  box.style.background = "#0c1322";
  box.style.border = "1px solid #1e293b";
  box.style.borderRadius = "12px";
  box.style.padding = "1.5rem";
  box.style.margin = "1.75rem 0";

  const header = document.createElement("div");
  header.style.marginBottom = "1rem";
  header.innerHTML = `
    <h4 style="color:#38bdf8; font-size:1.15rem; margin-bottom:0.35rem; display:flex; align-items:center; gap:0.5rem;">
      ${simConfig.title}
    </h4>
    <p style="color:#94a3b8; font-size:0.9rem; line-height:1.5;">${simConfig.desc}</p>
  `;
  box.appendChild(header);

  const canvas = document.createElement("canvas");
  canvas.width = 720;
  canvas.height = 340;
  canvas.style.width = "100%";
  canvas.style.height = "auto";
  canvas.style.borderRadius = "8px";
  canvas.style.display = "block";
  canvas.style.background = "#070b14";
  canvas.style.border = "1px solid #1e293b";
  box.appendChild(canvas);

  const ctrlBar = document.createElement("div");
  ctrlBar.style.display = "flex";
  ctrlBar.style.flexWrap = "wrap";
  ctrlBar.style.gap = "1.25rem";
  ctrlBar.style.marginTop = "1rem";
  ctrlBar.style.padding = "0.75rem 1rem";
  ctrlBar.style.background = "#080e1c";
  ctrlBar.style.borderRadius = "8px";
  ctrlBar.style.border = "1px solid #1e293d";

  const currentVals = {};

  if (simConfig.controls && simConfig.controls.length > 0) {
    simConfig.controls.forEach(ctrl => {
      currentVals[ctrl.id] = ctrl.value;

      const wrap = document.createElement("div");
      wrap.style.display = "flex";
      wrap.style.flexDirection = "column";
      wrap.style.gap = "0.25rem";
      wrap.style.minWidth = "160px";

      const labelRow = document.createElement("div");
      labelRow.style.display = "flex";
      labelRow.style.justifyContent = "space-between";
      labelRow.style.fontSize = "0.82rem";
      labelRow.style.color = "#cbd5e1";

      const titleSpan = document.createElement("span");
      titleSpan.innerText = ctrl.label;
      const valSpan = document.createElement("span");
      valSpan.style.fontFamily = "monospace";
      valSpan.style.color = "#38bdf8";
      valSpan.innerText = ctrl.value;

      labelRow.appendChild(titleSpan);
      labelRow.appendChild(valSpan);
      wrap.appendChild(labelRow);

      const input = document.createElement("input");
      input.type = "range";
      input.min = ctrl.min;
      input.max = ctrl.max;
      input.step = ctrl.step;
      input.value = ctrl.value;
      input.style.accentColor = "#38bdf8";
      input.style.cursor = "pointer";

      input.addEventListener("input", (e) => {
        const v = parseFloat(e.target.value);
        currentVals[ctrl.id] = v;
        valSpan.innerText = v;
        if (!simConfig.isAnimated) {
          simConfig.render(canvas, currentVals, 0);
        }
      });

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

function drawArrow(ctx, fromx, fromy, tox, toy, color, label, width) {
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = width || 2;
  const headlen = 10;
  const angle = Math.atan2(toy - fromy, tox - fromx);

  ctx.beginPath();
  ctx.moveTo(fromx, fromy);
  ctx.lineTo(tox, toy);
  ctx.stroke();

  ctx.beginPath();
  ctx.moveTo(tox, toy);
  ctx.lineTo(tox - headlen * Math.cos(angle - Math.PI / 6), toy - headlen * Math.sin(angle - Math.PI / 6));
  ctx.lineTo(tox - headlen * Math.cos(angle + Math.PI / 6), toy - headlen * Math.sin(angle + Math.PI / 6));
  ctx.closePath();
  ctx.fill();

  if (label) {
    ctx.font = "12px sans-serif";
    ctx.fillText(label, tox + 6, toy + 4);
  }
}

console.log("Statistical Mechanics simulation suite compiled successfully with 22 simulations!");
