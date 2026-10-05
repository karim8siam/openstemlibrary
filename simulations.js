// Quantum Mechanics Simulations Engine
// High-performance Canvas renderers with requestAnimationFrame and interactive controls

window.SimulationEngine = {
  activeInstances: {},

  initSimulation: function(containerId, simType) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    // Clean up any existing instance
    if (this.activeInstances[containerId]) {
      this.activeInstances[containerId].destroy();
    }

    container.innerHTML = "";
    
    switch(simType) {
      case "double-slit":
        this.activeInstances[containerId] = new DoubleSlitSim(container);
        break;
      case "uncertainty-principle":
        this.activeInstances[containerId] = new UncertaintySim(container);
        break;
      case "quantum-measurement":
        this.activeInstances[containerId] = new MeasurementSim(container);
        break;
      case "wavepacket-dispersion":
        this.activeInstances[containerId] = new DispersionSim(container);
        break;
      case "quantum-tunneling":
        this.activeInstances[containerId] = new TunnelingSim(container);
        break;
      case "particle-in-a-box":
        this.activeInstances[containerId] = new BoxSim(container);
        break;
      case "harmonic-oscillator":
        this.activeInstances[containerId] = new HarmonicSim(container);
        break;
      case "hydrogen-orbitals":
        this.activeInstances[containerId] = new HydrogenSim(container);
        break;
      case "blackbody-spectrum-sim":
        this.activeInstances[containerId] = new BlackbodySim(container);
        break;
      case "photoelectric-effect-sim":
        this.activeInstances[containerId] = new PhotoelectricSim(container);
        break;
      case "bohr-orbit-sim":
        this.activeInstances[containerId] = new BohrOrbitSim(container);
        break;
      case "finite-square-well-sim":
        this.activeInstances[containerId] = new FiniteWellSim(container);
        break;
      case "angular-momentum-sim":
        this.activeInstances[containerId] = new AngularMomentumSim(container);
        break;
      case "zeeman-effect-sim":
        this.activeInstances[containerId] = new ZeemanSim(container);
        break;
      default:
        console.warn("Unknown simulation type:", simType);
    }
  }
};

// ==========================================
// 1. Double-Slit Wave-Particle Duality
// ==========================================
class DoubleSlitSim {
  constructor(container) {
    this.container = container;
    this.detectorOn = false;
    this.firingRate = "medium";
    this.particles = [];
    this.hits = [];
    this.hitCount = 0;
    this.maxHits = 1800;
    this.animId = null;

    this.renderDOM();
    this.initCanvas();
    this.startLoop();
  }

  renderDOM() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div class="sim-title">
            <span class="sim-badge">Simulation 1.1</span>
            <strong>Double-Slit Wave-Particle Duality & Detector Collapse</strong>
          </div>
          <div class="sim-controls">
            <button id="ds-toggle-det" class="btn-control ${this.detectorOn ? 'active' : ''}">
              🔬 Slit Detector: <span id="ds-det-status">OFF (Wave)</span>
            </button>
            <button id="ds-clear" class="btn-control secondary">Clear Screen</button>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="ds-canvas" width="760" height="340"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-footer">
          <div class="sim-stat">Hits Recorded: <span id="ds-count">0</span></div>
          <div class="sim-hint">
            💡 <em>Notice:</em> With Detector <strong>OFF</strong>, single dots gradually build up an interference pattern. Turn Detector <strong>ON</strong> to see the quantum measurement collapse the wave into two classical bands!
          </div>
        </div>
      </div>
    `;

    document.getElementById("ds-toggle-det").onclick = () => {
      this.detectorOn = !this.detectorOn;
      const statusSpan = document.getElementById("ds-det-status");
      const btn = document.getElementById("ds-toggle-det");
      if (this.detectorOn) {
        statusSpan.innerText = "ON (Which-Way Known)";
        btn.classList.add("active-danger");
      } else {
        statusSpan.innerText = "OFF (Wave)";
        btn.classList.remove("active-danger");
      }
      this.hits = [];
      this.hitCount = 0;
    };

    document.getElementById("ds-clear").onclick = () => {
      this.hits = [];
      this.hitCount = 0;
    };
  }

  initCanvas() {
    this.canvas = document.getElementById("ds-canvas");
    this.ctx = this.canvas.getContext("2d");
  }

  startLoop() {
    const loop = () => {
      this.update();
      this.draw();
      this.animId = requestAnimationFrame(loop);
    };
    this.animId = requestAnimationFrame(loop);
  }

  update() {
    // Generate new particle
    if (this.particles.length < 8 && this.hitCount < this.maxHits) {
      this.particles.push({
        x: 40,
        y: 170 + (Math.random() - 0.5) * 20,
        vx: 4.8 + Math.random() * 0.8,
        vy: (Math.random() - 0.5) * 0.8,
        state: 'pre-slit',
        slit: Math.random() < 0.5 ? 1 : 2
      });
    }

    // Move existing particles
    for (let i = this.particles.length - 1; i >= 0; i--) {
      const p = this.particles[i];
      p.x += p.vx;
      p.y += p.vy;

      // Passing slits at x = 280
      if (p.x >= 280 && p.state === 'pre-slit') {
        p.state = 'post-slit';
        const slitY = p.slit === 1 ? 130 : 210;
        p.y = slitY + (Math.random() - 0.5) * 6;

        if (this.detectorOn) {
          // Classical trajectory: spreading from specific slit
          const targetY = slitY + (Math.random() - 0.5) * 70;
          const dist = 700 - 280;
          p.vy = ((targetY - slitY) / dist) * p.vx;
        } else {
          // Quantum interference sampling
          const angle = this.sampleInterferenceAngle();
          p.vy = Math.tan(angle) * p.vx;
        }
      }

      // Reaching detector screen at x = 700
      if (p.x >= 700) {
        if (p.y >= 20 && p.y <= 320) {
          this.hits.push({ y: p.y, opacity: 0.95 });
          this.hitCount++;
          const countEl = document.getElementById("ds-count");
          if (countEl) countEl.innerText = this.hitCount;
        }
        this.particles.splice(i, 1);
      }
    }
  }

  sampleInterferenceAngle() {
    // Rejection sampling for I(theta) = cos^2(beta) * sinc^2(alpha)
    for (let attempt = 0; attempt < 50; attempt++) {
      const yNorm = (Math.random() - 0.5) * 280; // range [-140, 140]
      const lambda = 12;
      const d = 80; // slit separation
      const L = 420; // distance to screen
      const phase = (Math.PI * d * yNorm) / (lambda * L);
      const intensity = Math.pow(Math.cos(phase), 2) * Math.exp(-Math.pow(yNorm / 85, 2));
      if (Math.random() < intensity) {
        return Math.atan(yNorm / L);
      }
    }
    return (Math.random() - 0.5) * 0.4;
  }

  draw() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Background gradient
    const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
    grad.addColorStop(0, "#0b0f19");
    grad.addColorStop(1, "#111827");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw Source Gun
    ctx.fillStyle = "#38bdf8";
    ctx.fillRect(20, 155, 25, 30);
    ctx.fillStyle = "#94a3b8";
    ctx.font = "11px Inter, sans-serif";
    ctx.fillText("Electron Gun", 10, 145);

    // Draw Double-Slit Barrier at x = 280
    ctx.fillStyle = "#475569";
    ctx.fillRect(280, 0, 12, 120); // Top wall
    ctx.fillRect(280, 140, 12, 60); // Middle wall
    ctx.fillRect(280, 220, 12, 120); // Bottom wall

    // Slit labels
    ctx.fillStyle = "#38bdf8";
    ctx.fillText("Slit 1", 240, 134);
    ctx.fillText("Slit 2", 240, 214);

    // Detector indicator if ON
    if (this.detectorOn) {
      ctx.fillStyle = "#ef4444";
      ctx.beginPath();
      ctx.arc(286, 130, 8, 0, Math.PI * 2);
      ctx.arc(286, 210, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#fca5a5";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText("OBSERVING", 298, 134);
      ctx.fillText("OBSERVING", 298, 214);
    }

    // Draw Detection Screen at x = 700
    ctx.fillStyle = "#334155";
    ctx.fillRect(700, 20, 8, 300);
    ctx.fillStyle = "#94a3b8";
    ctx.fillText("Phosphor Screen", 660, 15);

    // Draw Hits on Screen
    ctx.fillStyle = this.detectorOn ? "#f87171" : "#34d399";
    for (let hit of this.hits) {
      ctx.beginPath();
      ctx.arc(704, hit.y, 2, 0, Math.PI * 2);
      ctx.fill();
    }

    // Draw moving particles
    for (let p of this.particles) {
      ctx.fillStyle = "#67e8f9";
      ctx.shadowColor = "#38bdf8";
      ctx.shadowBlur = 6;
      ctx.beginPath();
      ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    // Draw Theoretical Intensity Curve behind phosphor screen
    ctx.strokeStyle = this.detectorOn ? "rgba(239, 68, 68, 0.4)" : "rgba(52, 211, 153, 0.45)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let y = 30; y <= 310; y += 2) {
      const yNorm = y - 170;
      let curveX;
      if (this.detectorOn) {
        // Two independent gaussians
        const g1 = Math.exp(-Math.pow((y - 130) / 32, 2));
        const g2 = Math.exp(-Math.pow((y - 210) / 32, 2));
        curveX = 708 + (g1 + g2) * 28;
      } else {
        const phase = (Math.PI * 80 * yNorm) / (12 * 420);
        const intensity = Math.pow(Math.cos(phase), 2) * Math.exp(-Math.pow(yNorm / 80, 2));
        curveX = 708 + intensity * 40;
      }
      if (y === 30) ctx.moveTo(curveX, y);
      else ctx.lineTo(curveX, y);
    }
    ctx.stroke();
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}

// ==========================================
// 2. Heisenberg Uncertainty Principle
// ==========================================
class UncertaintySim {
  constructor(container) {
    this.container = container;
    this.deltaX = 28; // width in pixels
    this.animId = null;
    this.t = 0;

    this.renderDOM();
    this.initCanvas();
    this.startLoop();
  }

  renderDOM() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div class="sim-title">
            <span class="sim-badge">Simulation 1.2</span>
            <strong>Heisenberg Conjugate Distributions: $\\Delta x \\cdot \\Delta p \\ge \\frac{\\hbar}{2}$</strong>
          </div>
          <div class="slider-control-group">
            <label>Position Confinement $\\Delta x$: <strong id="unc-dx-val">28 nm</strong></label>
            <input type="range" id="unc-slider" min="10" max="90" value="28" class="range-slider">
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="unc-canvas" width="760" height="320"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-metrics-grid">
          <div class="metric-card">
            <div class="metric-label">Spatial Uncertainty $\\Delta x$</div>
            <div class="metric-value text-sky" id="metric-dx">0.28 Å</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Momentum Spread $\\Delta p$</div>
            <div class="metric-value text-amber" id="metric-dp">1.88 × 10⁻²⁴ kg·m/s</div>
          </div>
          <div class="metric-card highlight">
            <div class="metric-label">Uncertainty Product $\\Delta x \\cdot \\Delta p$</div>
            <div class="metric-value text-emerald" id="metric-prod">0.53 ℏ (≥ 0.50 ℏ)</div>
          </div>
        </div>
      </div>
    `;

    const slider = document.getElementById("unc-slider");
    slider.oninput = (e) => {
      this.deltaX = parseFloat(e.target.value);
      document.getElementById("unc-dx-val").innerText = this.deltaX + " nm";
      this.updateMetrics();
    };
    this.updateMetrics();
  }

  updateMetrics() {
    const dxRel = this.deltaX / 100;
    const dpRel = 1 / dxRel;
    const prod = dxRel * dpRel * 0.52; // slightly above minimum bound

    document.getElementById("metric-dx").innerText = (dxRel * 0.8).toFixed(2) + " Å";
    document.getElementById("metric-dp").innerText = (dpRel * 0.95).toFixed(2) + " × 10⁻²⁴ kg·m/s";
    document.getElementById("metric-prod").innerText = prod.toFixed(2) + " ℏ (≥ 0.50 ℏ)";
  }

  initCanvas() {
    this.canvas = document.getElementById("unc-canvas");
    this.ctx = this.canvas.getContext("2d");
  }

  startLoop() {
    const loop = () => {
      this.t += 0.05;
      this.draw();
      this.animId = requestAnimationFrame(loop);
    };
    this.animId = requestAnimationFrame(loop);
  }

  draw() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#090d16";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const halfW = canvas.width / 2;

    // Left Panel: Spatial Wavefunction |psi(x)|^2
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const xCenter = halfW / 2;
    const yBaseline = 210;

    // Draw baseline
    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(30, yBaseline);
    ctx.lineTo(halfW - 30, yBaseline);
    ctx.moveTo(halfW + 30, yBaseline);
    ctx.lineTo(canvas.width - 30, yBaseline);
    ctx.stroke();

    // Labels
    ctx.fillStyle = "#94a3b8";
    ctx.font = "13px Inter, sans-serif";
    ctx.fillText("Position Space: |ψ(x)|²", 40, 40);
    ctx.fillText("Momentum Space: |φ(p)|²", halfW + 40, 40);

    // Plot Left: Spatial Gaussian
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const sigmaX = this.deltaX * 1.5;
    for (let x = 30; x <= halfW - 30; x++) {
      const dist = x - xCenter;
      const val = Math.exp(-Math.pow(dist / sigmaX, 2));
      const y = yBaseline - val * 140;
      if (x === 30) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Wave oscillations Re(psi(x))
    ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    for (let x = 30; x <= halfW - 30; x++) {
      const dist = x - xCenter;
      const env = Math.exp(-Math.pow(dist / sigmaX, 2));
      const osc = Math.cos(0.2 * dist - this.t);
      const y = yBaseline - env * osc * 140;
      if (x === 30) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Plot Right: Momentum Distribution (Conjugate Fourier)
    // As sigmaX decreases, sigmaP increases inversely!
    const sigmaP = (2200 / sigmaX);
    const pCenter = halfW + halfW / 2;

    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let px = halfW + 30; px <= canvas.width - 30; px++) {
      const dist = px - pCenter;
      const val = Math.exp(-Math.pow(dist / sigmaP, 2));
      const y = yBaseline - val * 140;
      if (px === halfW + 30) ctx.moveTo(px, y);
      else ctx.lineTo(px, y);
    }
    ctx.stroke();

    // Draw Width Brackets (Delta x)
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(xCenter - sigmaX, yBaseline + 15);
    ctx.lineTo(xCenter + sigmaX, yBaseline + 15);
    ctx.stroke();
    ctx.fillStyle = "#38bdf8";
    ctx.font = "12px Inter, sans-serif";
    ctx.fillText("Δx", xCenter - 6, yBaseline + 32);

    // Draw Width Brackets (Delta p)
    ctx.strokeStyle = "#f59e0b";
    ctx.beginPath();
    ctx.moveTo(pCenter - sigmaP, yBaseline + 15);
    ctx.lineTo(pCenter + sigmaP, yBaseline + 15);
    ctx.stroke();
    ctx.fillStyle = "#f59e0b";
    ctx.fillText("Δp", pCenter - 6, yBaseline + 32);
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}

// ==========================================
// 3. Quantum Measurement & Collapse
// ==========================================
class MeasurementSim {
  constructor(container) {
    this.container = container;
    this.prob0 = 0.5;
    this.state = 'superposition'; // 'superposition', 'collapsed-0', 'collapsed-1'
    this.animId = null;
    this.pulse = 0;

    this.renderDOM();
    this.initCanvas();
    this.startLoop();
  }

  renderDOM() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div class="sim-title">
            <span class="sim-badge">Simulation 2.1</span>
            <strong>Superposition State & Quantum Measurement Collapse</strong>
          </div>
          <div class="sim-controls">
            <button id="qm-measure-btn" class="btn-control active">⚡ Measure System</button>
            <button id="qm-reset-btn" class="btn-control secondary">Reset to Superposition</button>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="qm-canvas" width="760" height="280"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="slider-control-group mt-3">
          <label>Superposition Amplitude $|c_0|^2$ (Probability of $|0\\rangle$): <strong id="qm-c0-val">50%</strong></label>
          <input type="range" id="qm-prob-slider" min="5" max="95" value="50" class="range-slider">
        </div>
      </div>
    `;

    const slider = document.getElementById("qm-prob-slider");
    slider.oninput = (e) => {
      this.prob0 = parseFloat(e.target.value) / 100;
      document.getElementById("qm-c0-val").innerText = Math.round(this.prob0 * 100) + "%";
      this.state = 'superposition';
    };

    document.getElementById("qm-measure-btn").onclick = () => {
      // Collapse state according to Born's Rule
      const rand = Math.random();
      this.state = rand < this.prob0 ? 'collapsed-0' : 'collapsed-1';
      this.pulse = 1.0;
    };

    document.getElementById("qm-reset-btn").onclick = () => {
      this.state = 'superposition';
    };
  }

  initCanvas() {
    this.canvas = document.getElementById("qm-canvas");
    this.ctx = this.canvas.getContext("2d");
  }

  startLoop() {
    const loop = () => {
      if (this.pulse > 0) this.pulse -= 0.03;
      this.draw();
      this.animId = requestAnimationFrame(loop);
    };
    this.animId = requestAnimationFrame(loop);
  }

  draw() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0a0e17";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const prob1 = 1 - this.prob0;
    const c0 = Math.sqrt(this.prob0).toFixed(2);
    const c1 = Math.sqrt(prob1).toFixed(2);

    // State Formula Header
    ctx.fillStyle = "#f8fafc";
    ctx.font = "16px 'Fira Code', monospace";
    let stateText = `|ψ⟩ = ${c0} |0⟩ + ${c1} |1⟩`;
    if (this.state === 'collapsed-0') stateText = `MEASURED: Eigenstate |0⟩ (Probability was ${(this.prob0*100).toFixed(0)}%)`;
    if (this.state === 'collapsed-1') stateText = `MEASURED: Eigenstate |1⟩ (Probability was ${(prob1*100).toFixed(0)}%)`;

    ctx.fillText(stateText, 40, 45);

    // Draw Eigenstate Probability Bars
    const barWidth = 140;
    const baseY = 210;

    // Bar 0
    const h0 = this.state === 'superposition' ? this.prob0 * 140 : (this.state === 'collapsed-0' ? 140 : 4);
    ctx.fillStyle = this.state === 'collapsed-0' ? "#10b981" : "#38bdf8";
    ctx.fillRect(180, baseY - h0, barWidth, h0);
    ctx.fillStyle = "#cbd5e1";
    ctx.font = "14px Inter, sans-serif";
    ctx.fillText("|0⟩ State", 220, baseY + 25);
    ctx.fillText(`${(this.prob0 * 100).toFixed(0)}%`, 230, baseY - h0 - 10);

    // Bar 1
    const h1 = this.state === 'superposition' ? prob1 * 140 : (this.state === 'collapsed-1' ? 140 : 4);
    ctx.fillStyle = this.state === 'collapsed-1' ? "#10b981" : "#818cf8";
    ctx.fillRect(440, baseY - h1, barWidth, h1);
    ctx.fillStyle = "#cbd5e1";
    ctx.fillText("|1⟩ State", 480, baseY + 25);
    ctx.fillText(`${(prob1 * 100).toFixed(0)}%`, 490, baseY - h1 - 10);

    // Flash border when measured
    if (this.pulse > 0) {
      ctx.strokeStyle = `rgba(16, 185, 129, ${this.pulse})`;
      ctx.lineWidth = 6;
      ctx.strokeRect(0, 0, canvas.width, canvas.height);
    }
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}

// ==========================================
// 4. Free Wavepacket Dispersion
// ==========================================
class DispersionSim {
  constructor(container) {
    this.container = container;
    this.t = 0;
    this.isPlaying = true;
    this.animId = null;

    this.renderDOM();
    this.initCanvas();
    this.startLoop();
  }

  renderDOM() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div class="sim-title">
            <span class="sim-badge">Simulation 3.1</span>
            <strong>Free Particle Wavepacket Dispersion (Spreading over Time)</strong>
          </div>
          <div class="sim-controls">
            <button id="disp-play" class="btn-control active">⏸ Pause / Play</button>
            <button id="disp-reset" class="btn-control secondary">Reset Time t = 0</button>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="disp-canvas" width="760" height="280"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-footer">
          <div class="sim-hint">
            💡 As time progresses ($t > 0$), a free wave packet naturally spreads: $\\sigma(t) = \\sigma_0\\sqrt{1 + (\\hbar t / 2m\\sigma_0^2)^2}$. Higher momentum components travel faster than lower ones!
          </div>
        </div>
      </div>
    `;

    document.getElementById("disp-play").onclick = () => {
      this.isPlaying = !this.isPlaying;
    };
    document.getElementById("disp-reset").onclick = () => {
      this.t = 0;
    };
  }

  initCanvas() {
    this.canvas = document.getElementById("disp-canvas");
    this.ctx = this.canvas.getContext("2d");
  }

  startLoop() {
    const loop = () => {
      if (this.isPlaying) this.t += 0.015;
      if (this.t > 8) this.t = 0;
      this.draw();
      this.animId = requestAnimationFrame(loop);
    };
    this.animId = requestAnimationFrame(loop);
  }

  draw() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0b0f19";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const baseY = 190;
    ctx.strokeStyle = "#334155";
    ctx.beginPath();
    ctx.moveTo(30, baseY);
    ctx.lineTo(canvas.width - 30, baseY);
    ctx.stroke();

    const sigma0 = 25;
    const spread = sigma0 * Math.sqrt(1 + Math.pow(this.t * 0.9, 2));
    const xCenter = 140 + this.t * 55; // group velocity drift

    // Draw Probability Density Envelope
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let x = 30; x <= canvas.width - 30; x++) {
      const dist = x - xCenter;
      const amp = (sigma0 / spread) * Math.exp(-Math.pow(dist / spread, 2));
      const y = baseY - amp * 120;
      if (x === 30) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Draw Real Part Oscillations
    ctx.strokeStyle = "rgba(147, 197, 253, 0.4)";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    for (let x = 30; x <= canvas.width - 30; x++) {
      const dist = x - xCenter;
      const amp = (sigma0 / spread) * Math.exp(-Math.pow(dist / spread, 2));
      const phase = 0.25 * dist - this.t * 8;
      const y = baseY - amp * Math.cos(phase) * 120;
      if (x === 30) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Time display
    ctx.fillStyle = "#94a3b8";
    ctx.font = "13px Inter, sans-serif";
    ctx.fillText(`Evolution Time: t = ${this.t.toFixed(2)} fs`, 40, 35);
    ctx.fillText(`Width σ(t) = ${(spread * 0.1).toFixed(2)} nm`, 40, 55);
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}

// ==========================================
// 5. Quantum Tunneling Through Barrier
// ==========================================
class TunnelingSim {
  constructor(container) {
    this.container = container;
    this.energy = 5.0; // eV
    this.v0 = 8.0; // barrier height eV
    this.barrierWidth = 60; // pixels
    this.animId = null;
    this.t = 0;

    this.renderDOM();
    this.initCanvas();
    this.startLoop();
  }

  renderDOM() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div class="sim-title">
            <span class="sim-badge">Simulation 4.1</span>
            <strong>Quantum Mechanical Tunneling ($E < V_0$)</strong>
          </div>
          <div class="slider-control-group">
            <label>Particle Energy $E$: <strong id="tun-e-val">5.0 eV</strong></label>
            <input type="range" id="tun-e-slider" min="10" max="95" value="50" class="range-slider">
            <label class="mt-2">Barrier Height $V_0$: <strong id="tun-v-val">8.0 eV</strong></label>
            <input type="range" id="tun-v-slider" min="40" max="120" value="80" class="range-slider">
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="tun-canvas" width="760" height="320"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-metrics-grid">
          <div class="metric-card">
            <div class="metric-label">Transmission Coeff. $T$</div>
            <div class="metric-value text-emerald" id="tun-t-val">8.4%</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Reflection Coeff. $R$</div>
            <div class="metric-value text-amber" id="tun-r-val">91.6%</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Attenuation $\\kappa$</div>
            <div class="metric-value text-sky" id="tun-k-val">1.25 nm⁻¹</div>
          </div>
        </div>
      </div>
    `;

    document.getElementById("tun-e-slider").oninput = (e) => {
      this.energy = (parseFloat(e.target.value) / 10).toFixed(1);
      document.getElementById("tun-e-val").innerText = this.energy + " eV";
      this.updateCoeffs();
    };

    document.getElementById("tun-v-slider").oninput = (e) => {
      this.v0 = (parseFloat(e.target.value) / 10).toFixed(1);
      document.getElementById("tun-v-val").innerText = this.v0 + " eV";
      this.updateCoeffs();
    };

    this.updateCoeffs();
  }

  updateCoeffs() {
    const E = parseFloat(this.energy);
    const V0 = parseFloat(this.v0);
    let T = 0;
    let kappa = 0;

    if (E < V0) {
      kappa = Math.sqrt(V0 - E) * 0.8;
      const decay = Math.exp(-2 * kappa * (this.barrierWidth / 25));
      T = Math.min(0.99, 16 * (E / V0) * (1 - E / V0) * decay);
    } else {
      T = 1.0 - Math.pow((V0 / (2 * E)), 2) * 0.15;
    }
    const R = Math.max(0, 1 - T);

    document.getElementById("tun-t-val").innerText = (T * 100).toFixed(1) + "%";
    document.getElementById("tun-r-val").innerText = (R * 100).toFixed(1) + "%";
    document.getElementById("tun-k-val").innerText = kappa.toFixed(2) + " nm⁻¹";
  }

  initCanvas() {
    this.canvas = document.getElementById("tun-canvas");
    this.ctx = this.canvas.getContext("2d");
  }

  startLoop() {
    const loop = () => {
      this.t += 0.08;
      this.draw();
      this.animId = requestAnimationFrame(loop);
    };
    this.animId = requestAnimationFrame(loop);
  }

  draw() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0a0f1d";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const bStart = 330;
    const bEnd = bStart + this.barrierWidth;
    const baseY = 240;

    // Draw Potential Barrier
    const bHeight = Math.min(180, parseFloat(this.v0) * 16);
    ctx.fillStyle = "rgba(239, 68, 68, 0.22)";
    ctx.fillRect(bStart, baseY - bHeight, this.barrierWidth, bHeight);
    ctx.strokeStyle = "#ef4444";
    ctx.lineWidth = 2;
    ctx.strokeRect(bStart, baseY - bHeight, this.barrierWidth, bHeight);

    // Energy line E
    const eHeight = Math.min(220, parseFloat(this.energy) * 16);
    ctx.strokeStyle = "#38bdf8";
    ctx.setLineDash([6, 4]);
    ctx.beginPath();
    ctx.moveTo(30, baseY - eHeight);
    ctx.lineTo(canvas.width - 30, baseY - eHeight);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "#38bdf8";
    ctx.font = "12px Inter, sans-serif";
    ctx.fillText(`Particle Energy E = ${this.energy} eV`, 40, baseY - eHeight - 8);

    // Baseline
    ctx.strokeStyle = "#475569";
    ctx.beginPath();
    ctx.moveTo(20, baseY);
    ctx.lineTo(canvas.width - 20, baseY);
    ctx.stroke();

    // Plot Wavefunction ψ(x)
    ctx.strokeStyle = "#10b981";
    ctx.lineWidth = 2.5;
    ctx.beginPath();

    const E = parseFloat(this.energy);
    const V0 = parseFloat(this.v0);
    const k1 = 0.12 * Math.sqrt(E);
    const ampInc = 35;

    // Region 1 (x < bStart): Incident + partial reflected
    for (let x = 30; x <= bStart; x++) {
      const inc = ampInc * Math.sin(k1 * x - this.t);
      const ref = ampInc * 0.7 * Math.sin(-k1 * x - this.t);
      const y = baseY - eHeight - (inc + ref);
      if (x === 30) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }

    // Region 2 (inside barrier): Exponential decay
    const valAtStart = baseY - eHeight - ampInc * 0.3 * Math.sin(k1 * bStart - this.t);
    const kappa = Math.max(0.02, 0.05 * Math.sqrt(Math.abs(V0 - E)));
    for (let x = bStart; x <= bEnd; x++) {
      const decay = Math.exp(-kappa * (x - bStart));
      const y = (baseY - eHeight) - (baseY - eHeight - valAtStart) * decay;
      ctx.lineTo(x, y);
    }

    // Region 3 (transmitted): Sinusoidal with reduced amplitude
    const transAmp = ampInc * Math.exp(-kappa * this.barrierWidth);
    for (let x = bEnd; x <= canvas.width - 30; x++) {
      const trans = transAmp * Math.sin(k1 * (x - bEnd) - this.t);
      const y = baseY - eHeight - trans;
      ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Labels
    ctx.fillStyle = "#ef4444";
    ctx.fillText(`V₀ = ${this.v0} eV`, bStart + 6, baseY - bHeight + 20);
    ctx.fillStyle = "#94a3b8";
    ctx.fillText("Region I: Incident + Reflected", 60, baseY + 30);
    ctx.fillText("Region II: Tunneling Decay", bStart - 20, baseY + 45);
    ctx.fillText("Region III: Transmitted Wave", bEnd + 20, baseY + 30);
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}

// ==========================================
// 6. Particle in a Box (Infinite Square Well)
// ==========================================
class BoxSim {
  constructor(container) {
    this.container = container;
    this.n = 1;
    this.viewMode = 'both'; // 'psi', 'prob', 'both'
    this.animId = null;
    this.t = 0;

    this.renderDOM();
    this.initCanvas();
    this.startLoop();
  }

  renderDOM() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div class="sim-title">
            <span class="sim-badge">Simulation 4.2</span>
            <strong>Particle in an Infinite Square Well: $E_n = \\frac{n^2 \\pi^2 \\hbar^2}{2mL^2}$</strong>
          </div>
          <div class="sim-controls">
            <button class="btn-n ${this.n===1?'active':''}" data-n="1">n = 1</button>
            <button class="btn-n ${this.n===2?'active':''}" data-n="2">n = 2</button>
            <button class="btn-n ${this.n===3?'active':''}" data-n="3">n = 3</button>
            <button class="btn-n ${this.n===4?'active':''}" data-n="4">n = 4</button>
            <button class="btn-n ${this.n===5?'active':''}" data-n="5">n = 5</button>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="box-canvas" width="760" height="320"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-footer">
          <div class="sim-hint">
            💡 Blue curve: Wavefunction $\\psi_n(x) = \\sqrt{2/L}\\sin(n\\pi x/L)$. Orange shaded: Probability Density $|\\psi_n(x)|^2$. Notice $n-1$ nodes where the particle has <strong>zero</strong> probability of being found!
          </div>
        </div>
      </div>
    `;

    this.container.querySelectorAll(".btn-n").forEach(btn => {
      btn.onclick = () => {
        this.container.querySelectorAll(".btn-n").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        this.n = parseInt(btn.getAttribute("data-n"));
      };
    });
  }

  initCanvas() {
    this.canvas = document.getElementById("box-canvas");
    this.ctx = this.canvas.getContext("2d");
  }

  startLoop() {
    const loop = () => {
      this.t += 0.04;
      this.draw();
      this.animId = requestAnimationFrame(loop);
    };
    this.animId = requestAnimationFrame(loop);
  }

  draw() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0a0e1a";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const leftWall = 80;
    const rightWall = 520;
    const L = rightWall - leftWall;
    const baseY = 240;

    // Draw Infinite Walls
    ctx.fillStyle = "#334155";
    ctx.fillRect(0, 20, leftWall, 250);
    ctx.fillRect(rightWall, 20, 30, 250);

    ctx.fillStyle = "#ef4444";
    ctx.font = "12px Inter, sans-serif";
    ctx.fillText("V = ∞", 25, 140);
    ctx.fillText("V = ∞", rightWall + 5, 140);

    // Box baseline
    ctx.strokeStyle = "#64748b";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(leftWall, baseY);
    ctx.lineTo(rightWall, baseY);
    ctx.stroke();

    // Draw Energy Level Ladder on the right
    const ladderX = 580;
    ctx.fillStyle = "#94a3b8";
    ctx.fillText("Energy Levels", ladderX, 40);
    for (let lev = 1; lev <= 5; lev++) {
      const levY = baseY - (lev * lev * 8);
      ctx.strokeStyle = (lev === this.n) ? "#38bdf8" : "#475569";
      ctx.lineWidth = (lev === this.n) ? 3 : 1.5;
      ctx.beginPath();
      ctx.moveTo(ladderX, levY);
      ctx.lineTo(ladderX + 130, levY);
      ctx.stroke();
      ctx.fillStyle = (lev === this.n) ? "#38bdf8" : "#64748b";
      ctx.fillText(`E${lev} = ${lev*lev} E₁`, ladderX + 140, levY + 4);
    }

    // Draw Shaded Probability Density |psi(x)|^2
    ctx.fillStyle = "rgba(245, 158, 11, 0.25)";
    ctx.beginPath();
    ctx.moveTo(leftWall, baseY);
    for (let x = leftWall; x <= rightWall; x++) {
      const xNorm = (x - leftWall) / L;
      const prob = Math.pow(Math.sin(this.n * Math.PI * xNorm), 2);
      const y = baseY - prob * 120;
      ctx.lineTo(x, y);
    }
    ctx.lineTo(rightWall, baseY);
    ctx.closePath();
    ctx.fill();

    // Draw Probability Density outline
    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let x = leftWall; x <= rightWall; x++) {
      const xNorm = (x - leftWall) / L;
      const prob = Math.pow(Math.sin(this.n * Math.PI * xNorm), 2);
      const y = baseY - prob * 120;
      if (x === leftWall) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Draw Wavefunction psi(x) with time phase factor cos(E*t)
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const phase = Math.cos(this.n * this.n * 0.3 * this.t);
    for (let x = leftWall; x <= rightWall; x++) {
      const xNorm = (x - leftWall) / L;
      const psi = Math.sin(this.n * Math.PI * xNorm) * phase;
      const y = baseY - psi * 60;
      if (x === leftWall) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Wall coordinate labels
    ctx.fillStyle = "#cbd5e1";
    ctx.fillText("x = 0", leftWall - 15, baseY + 20);
    ctx.fillText("x = L", rightWall - 10, baseY + 20);
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}

// ==========================================
// 7. Quantum Harmonic Oscillator
// ==========================================
class HarmonicSim {
  constructor(container) {
    this.container = container;
    this.n = 0;
    this.animId = null;
    this.t = 0;

    this.renderDOM();
    this.initCanvas();
    this.startLoop();
  }

  renderDOM() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div class="sim-title">
            <span class="sim-badge">Simulation 5.1</span>
            <strong>Quantum Harmonic Oscillator: $E_n = (n + \\frac{1}{2})\\hbar\\omega$</strong>
          </div>
          <div class="sim-controls">
            <button class="btn-sho ${this.n===0?'active':''}" data-n="0">n = 0 (Ground)</button>
            <button class="btn-sho ${this.n===1?'active':''}" data-n="1">n = 1</button>
            <button class="btn-sho ${this.n===2?'active':''}" data-n="2">n = 2</button>
            <button class="btn-sho ${this.n===3?'active':''}" data-n="3">n = 3</button>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="sho-canvas" width="760" height="330"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-footer">
          <div class="sim-hint">
            💡 Notice that even in the ground state ($n=0$), energy is <strong>$0.5\\hbar\\omega$</strong> (Zero-Point Energy). The wavefunction penetrates beyond the red vertical dashed lines (classical turning points) into the forbidden region!
          </div>
        </div>
      </div>
    `;

    this.container.querySelectorAll(".btn-sho").forEach(btn => {
      btn.onclick = () => {
        this.container.querySelectorAll(".btn-sho").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        this.n = parseInt(btn.getAttribute("data-n"));
      };
    });
  }

  initCanvas() {
    this.canvas = document.getElementById("sho-canvas");
    this.ctx = this.canvas.getContext("2d");
  }

  startLoop() {
    const loop = () => {
      this.t += 0.05;
      this.draw();
      this.animId = requestAnimationFrame(loop);
    };
    this.animId = requestAnimationFrame(loop);
  }

  // Hermite polynomials
  hermite(n, x) {
    if (n === 0) return 1;
    if (n === 1) return 2 * x;
    if (n === 2) return 4 * x * x - 2;
    if (n === 3) return 8 * x * x * x - 12 * x;
    return 1;
  }

  draw() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0b101e";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const centerX = canvas.width / 2;
    const baseY = 270;
    const kParabola = 0.0035;

    // Draw Parabolic Potential V(x) = 1/2 k x^2
    ctx.strokeStyle = "#94a3b8";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let x = 80; x <= canvas.width - 80; x++) {
      const dx = x - centerX;
      const V = kParabola * dx * dx;
      const y = baseY - V;
      if (x === 80) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Draw Energy Rungs E_n = (n + 1/2) hbar omega
    for (let i = 0; i <= 4; i++) {
      const energyY = baseY - (i + 0.5) * 44;
      const turningDist = Math.sqrt(((i + 0.5) * 44) / kParabola);

      ctx.strokeStyle = (i === this.n) ? "#38bdf8" : "#334155";
      ctx.lineWidth = (i === this.n) ? 2.5 : 1;
      ctx.beginPath();
      ctx.moveTo(centerX - turningDist, energyY);
      ctx.lineTo(centerX + turningDist, energyY);
      ctx.stroke();

      ctx.fillStyle = (i === this.n) ? "#38bdf8" : "#64748b";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`E${i} = ${(i + 0.5).toFixed(1)} ℏω`, centerX + turningDist + 15, energyY + 4);

      // Highlight classical turning points for active state
      if (i === this.n) {
        ctx.strokeStyle = "#ef4444";
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(centerX - turningDist, baseY);
        ctx.lineTo(centerX - turningDist, energyY - 20);
        ctx.moveTo(centerX + turningDist, baseY);
        ctx.lineTo(centerX + turningDist, energyY - 20);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#ef4444";
        ctx.fillText("Classical Turning Points", centerX - turningDist - 30, baseY + 18);
      }
    }

    // Draw Wavefunction psi_n(x) on top of the n-th energy level
    const currentEY = baseY - (this.n + 0.5) * 44;
    ctx.strokeStyle = "#34d399";
    ctx.lineWidth = 2.5;
    ctx.beginPath();

    const scaleX = 40;
    const norm = [1, 0.7, 0.45, 0.28][this.n];

    for (let x = 80; x <= canvas.width - 80; x++) {
      const xi = (x - centerX) / scaleX;
      const H = this.hermite(this.n, xi);
      const psi = norm * H * Math.exp(-0.5 * xi * xi) * 32;
      const y = currentEY - psi;
      if (x === 80) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    ctx.fillStyle = "#34d399";
    ctx.font = "13px Inter, sans-serif";
    ctx.fillText(`Active State: ψ${this.n}(x)`, 60, 45);
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}

// ==========================================
// 8. Hydrogen Atom Orbitals & Radial Distribution
// ==========================================
class HydrogenSim {
  constructor(container) {
    this.container = container;
    this.orbital = "1s"; // 1s, 2s, 2p, 3d
    this.animId = null;

    this.renderDOM();
    this.initCanvas();
    this.draw();
  }

  renderDOM() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div class="sim-title">
            <span class="sim-badge">Simulation 6.1</span>
            <strong>Hydrogen Atom Radial Probability Density: $P(r) = r^2 |R_{nl}(r)|^2$</strong>
          </div>
          <div class="sim-controls">
            <button class="btn-orb ${this.orbital==='1s'?'active':''}" data-orb="1s">1s (n=1, l=0)</button>
            <button class="btn-orb ${this.orbital==='2s'?'active':''}" data-orb="2s">2s (n=2, l=0)</button>
            <button class="btn-orb ${this.orbital==='2p'?'active':''}" data-orb="2p">2p (n=2, l=1)</button>
            <button class="btn-orb ${this.orbital==='3d'?'active':''}" data-orb="3d">3d (n=3, l=2)</button>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="hyd-canvas" width="760" height="320"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-footer">
          <div class="sim-hint">
            💡 Notice that for <strong>1s</strong>, the peak of $P(r)$ occurs precisely at $r = 1.0\\, a_0$ (the Bohr radius). For <strong>2s</strong>, there is a radial node at $r = 2a_0$ where the electron is never found!
          </div>
        </div>
      </div>
    `;

    this.container.querySelectorAll(".btn-orb").forEach(btn => {
      btn.onclick = () => {
        this.container.querySelectorAll(".btn-orb").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        this.orbital = btn.getAttribute("data-orb");
        this.draw();
      };
    });
  }

  initCanvas() {
    this.canvas = document.getElementById("hyd-canvas");
    this.ctx = this.canvas.getContext("2d");
  }

  // Radial probability densities P(r) = r^2 * |R_nl(r)|^2
  getP(r) {
    // r in units of a_0
    switch(this.orbital) {
      case "1s":
        // 4 * r^2 * exp(-2r)
        return 4 * r * r * Math.exp(-2 * r);
      case "2s":
        // 0.5 * r^2 * (1 - 0.5r)^2 * exp(-r)
        return 0.125 * r * r * Math.pow(2 - r, 2) * Math.exp(-r);
      case "2p":
        // 1/24 * r^4 * exp(-r)
        return (1 / 24) * Math.pow(r, 4) * Math.exp(-r);
      case "3d":
        // (4 / 81 * 30) * r^6 * exp(-2r/3)
        return 0.0003 * Math.pow(r, 6) * Math.exp(-2 * r / 3);
      default:
        return 4 * r * r * Math.exp(-2 * r);
    }
  }

  draw() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0b1020";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const halfW = 460;
    const baseY = 250;

    // Left Half: P(r) Graph
    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(50, baseY);
    ctx.lineTo(halfW - 20, baseY);
    ctx.moveTo(50, baseY);
    ctx.lineTo(50, 40);
    ctx.stroke();

    ctx.fillStyle = "#94a3b8";
    ctx.font = "12px Inter, sans-serif";
    ctx.fillText("Radial Density P(r)", 30, 30);
    ctx.fillText("Distance r (in units of a₀)", halfW - 160, baseY + 30);

    // Plot P(r)
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2.5;
    ctx.fillStyle = "rgba(56, 189, 248, 0.2)";
    ctx.beginPath();
    ctx.moveTo(50, baseY);

    const maxR = 12.0;
    for (let px = 50; px <= halfW - 20; px++) {
      const r = ((px - 50) / (halfW - 70)) * maxR;
      const p = this.getP(r);
      const y = baseY - p * 340;
      ctx.lineTo(px, y);
    }
    ctx.lineTo(halfW - 20, baseY);
    ctx.closePath();
    ctx.fill();

    // Re-stroke line
    ctx.beginPath();
    for (let px = 50; px <= halfW - 20; px++) {
      const r = ((px - 50) / (halfW - 70)) * maxR;
      const p = this.getP(r);
      const y = baseY - p * 340;
      if (px === 50) ctx.moveTo(px, y);
      else ctx.lineTo(px, y);
    }
    ctx.stroke();

    // Right Half: 2D Electron Cloud Slice Simulation
    const cloudCenterX = 610;
    const cloudCenterY = 160;

    ctx.fillStyle = "#94a3b8";
    ctx.fillText("2D Probability Cloud Slice", cloudCenterX - 75, 40);

    // Nucleus Dot
    ctx.fillStyle = "#ef4444";
    ctx.beginPath();
    ctx.arc(cloudCenterX, cloudCenterY, 3, 0, Math.PI * 2);
    ctx.fill();

    // Render Cloud Stippling Dots
    const numDots = 1200;
    for (let d = 0; d < numDots; d++) {
      const angle = Math.random() * Math.PI * 2;
      const rNorm = Math.random() * 8;
      const prob = this.getP(rNorm);

      if (Math.random() < prob * 1.5) {
        const distPx = rNorm * 14;
        const x = cloudCenterX + Math.cos(angle) * distPx;
        const y = cloudCenterY + Math.sin(angle) * distPx;

        ctx.fillStyle = "rgba(103, 232, 249, 0.6)";
        ctx.fillRect(x, y, 1.5, 1.5);
      }
    }
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}


// ==========================================
// 9. Blackbody Radiation vs UV Catastrophe Simulator
// ==========================================
class BlackbodySim {
  constructor(container) {
    this.container = container;
    this.tempK = 5800; // Sun surface temp
    this.showClassical = true;
    this.initUI();
    this.render();
  }

  initUI() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div>
            <span class="sim-badge">Topic §1.1 Experiment</span>
            <strong class="sim-title">Planck Blackbody Radiation Spectrum vs Ultraviolet Catastrophe</strong>
          </div>
          <button class="btn-control active" id="btn-toggle-classical">Classical (Rayleigh-Jeans): ON</button>
        </div>
        <div class="canvas-container">
          <canvas id="bb-canvas" width="760" height="280"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-metrics-grid">
          <div class="metric-card">
            <span class="metric-label">Peak Wavelength (Wien's Law)</span>
            <span class="metric-val" id="bb-lmax-val">500 nm (Green Visible)</span>
          </div>
          <div class="metric-card">
            <span class="metric-label">Total Radiated Flux (σT⁴)</span>
            <span class="metric-val" id="bb-flux-val">6.42 × 10⁷ W/m²</span>
          </div>
          <div class="metric-card">
            <span class="metric-label">Classical UV Catastrophe</span>
            <span class="metric-val" id="bb-uv-val" style="color:#f43f5e;">Diverges at λ → 0</span>
          </div>
        </div>
        <div class="slider-control-group mt-3">
          <label>Cavity Temperature (T): <strong id="bb-t-lbl" style="color:#38bdf8;">5800 K (Sun's Surface)</strong></label>
          <input type="range" class="range-slider" id="bb-t-slider" min="2000" max="8000" step="100" value="5800">
        </div>
      </div>
    `;

    this.canvas = this.container.querySelector("#bb-canvas");
    this.ctx = this.canvas.getContext("2d");

    this.container.querySelector("#bb-t-slider").addEventListener("input", (e) => {
      this.tempK = parseFloat(e.target.value);
      this.container.querySelector("#bb-t-lbl").innerText = `${this.tempK} K`;
      this.updateMetrics();
      this.render();
    });

    const btnClass = this.container.querySelector("#btn-toggle-classical");
    btnClass.addEventListener("click", () => {
      this.showClassical = !this.showClassical;
      btnClass.innerText = `Classical (Rayleigh-Jeans): ${this.showClassical ? 'ON' : 'OFF'}`;
      btnClass.classList.toggle("active", this.showClassical);
      this.render();
    });

    this.updateMetrics();
  }

  updateMetrics() {
    const lMaxNm = (2.89777e-3 / this.tempK * 1e9).toFixed(0);
    const sigma = 5.67037e-8;
    const flux = (sigma * Math.pow(this.tempK, 4)).toExponential(2);

    const lMaxEl = this.container.querySelector("#bb-lmax-val");
    const fluxEl = this.container.querySelector("#bb-flux-val");

    if (lMaxEl) lMaxEl.innerText = `${lMaxNm} nm`;
    if (fluxEl) fluxEl.innerText = `${flux} W/m²`;
  }

  render() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;

    ctx.fillStyle = "#080c14";
    ctx.fillRect(0, 0, w, h);

    const graphX = 80;
    const graphY = 30;
    const graphW = 630;
    const graphH = 200;

    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 1;
    ctx.strokeRect(graphX, graphY, graphW, graphH);

    // Visible light spectrum band (380 - 750 nm)
    const visX1 = graphX + (380 / 2000) * graphW;
    const visX2 = graphX + (750 / 2000) * graphW;
    const grad = ctx.createLinearGradient(visX1, 0, visX2, 0);
    grad.addColorStop(0, "rgba(168, 85, 247, 0.2)");
    grad.addColorStop(0.3, "rgba(59, 130, 246, 0.2)");
    grad.addColorStop(0.5, "rgba(34, 197, 94, 0.2)");
    grad.addColorStop(0.7, "rgba(234, 179, 8, 0.2)");
    grad.addColorStop(1, "rgba(239, 68, 68, 0.2)");

    ctx.fillStyle = grad;
    ctx.fillRect(visX1, graphY, visX2 - visX1, graphH);

    ctx.fillStyle = "#94a3b8";
    ctx.font = "10px Inter, sans-serif";
    ctx.fillText("Visible Band", visX1 + 10, graphY + 18);

    // Planck curve
    const hConst = 6.626e-34;
    const cConst = 3.00e8;
    const kB = 1.381e-23;
    const T = this.tempK;

    const norm = Math.pow(T / 5800, 5) * 1.0;

    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2.5;
    ctx.beginPath();

    for (let nm = 10; nm <= 2000; nm += 10) {
      const lam = nm * 1e-9;
      const xExp = (hConst * cConst) / (lam * kB * T);
      const planck = (xExp < 50) ? (8 * Math.PI * hConst * cConst) / (Math.pow(lam, 5) * (Math.exp(xExp) - 1)) : 0;

      const px = graphX + (nm / 2000) * graphW;
      const py = graphY + graphH - Math.min(graphH - 10, (planck / 1.8e5) * (graphH / norm));

      if (nm === 10) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Classical Rayleigh-Jeans curve
    if (this.showClassical) {
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 2;
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      for (let nm = 100; nm <= 2000; nm += 15) {
        const lam = nm * 1e-9;
        const rj = (8 * Math.PI * kB * T) / Math.pow(lam, 4);

        const px = graphX + (nm / 2000) * graphW;
        const py = graphY + graphH - Math.min(graphH, (rj / 1.8e5) * (graphH / norm));

        if (nm === 100) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#f43f5e";
      ctx.fillText("Classical Rayleigh-Jeans (UV Catastrophe Divergence → ∞)", graphX + 220, graphY + 45);
    }

    ctx.fillStyle = "#38bdf8";
    ctx.fillText("Planck Quantum Distribution (Finite Integral)", graphX + 220, graphY + 25);
  }

  destroy() {}
}

// ==========================================
// 10. Photoelectric Effect Simulator
// ==========================================
class PhotoelectricSim {
  constructor(container) {
    this.container = container;
    this.wavelengthNm = 280; // UV
    this.workFunctionEV = 2.28; // Sodium metal (2.28 eV)
    this.electrons = [];
    this.animId = null;
    this.initUI();
    this.animate();
  }

  initUI() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div>
            <span class="sim-badge">Topic §1.2 Experiment</span>
            <strong class="sim-title">Einstein Photoelectric Effect & Stopping Potential</strong>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="pe-canvas" width="760" height="280"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-metrics-grid">
          <div class="metric-card">
            <span class="metric-label">Photon Energy (hν)</span>
            <span class="metric-val" id="pe-e-val">4.43 eV</span>
          </div>
          <div class="metric-card">
            <span class="metric-label">Max Kinetic Energy (Kmax)</span>
            <span class="metric-val" id="pe-kmax-val">2.15 eV</span>
          </div>
          <div class="metric-card">
            <span class="metric-label">Stopping Potential (V0)</span>
            <span class="metric-val" id="pe-v0-val">2.15 V</span>
          </div>
        </div>
        <div class="sim-controls-grid" style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem; margin-top:1rem;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8;">Light Wavelength (λ): <strong id="pe-lam-lbl" style="color:#38bdf8;">280 nm (UV)</strong></label>
            <input type="range" class="range-slider" id="pe-lam-slider" min="180" max="700" step="10" value="280">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8;">Cathode Metal Work Function (Φ): <strong id="pe-phi-lbl" style="color:#38bdf8;">2.28 eV (Sodium)</strong></label>
            <input type="range" class="range-slider" id="pe-phi-slider" min="1.9" max="5.0" step="0.1" value="2.28">
          </div>
        </div>
      </div>
    `;

    this.canvas = this.container.querySelector("#pe-canvas");
    this.ctx = this.canvas.getContext("2d");

    this.container.querySelector("#pe-lam-slider").addEventListener("input", (e) => {
      this.wavelengthNm = parseFloat(e.target.value);
      this.container.querySelector("#pe-lam-lbl").innerText = `${this.wavelengthNm} nm`;
      this.updateMetrics();
    });

    this.container.querySelector("#pe-phi-slider").addEventListener("input", (e) => {
      this.workFunctionEV = parseFloat(e.target.value);
      this.container.querySelector("#pe-phi-lbl").innerText = `${this.workFunctionEV.toFixed(2)} eV`;
      this.updateMetrics();
    });

    this.updateMetrics();
  }

  updateMetrics() {
    const hNu = 1240 / this.wavelengthNm; // eV
    const kMax = Math.max(0, hNu - this.workFunctionEV);
    const v0 = kMax;

    const eEl = this.container.querySelector("#pe-e-val");
    const kEl = this.container.querySelector("#pe-kmax-val");
    const vEl = this.container.querySelector("#pe-v0-val");

    if (eEl) eEl.innerText = `${hNu.toFixed(2)} eV`;
    if (kEl) kEl.innerText = kMax > 0 ? `${kMax.toFixed(2)} eV` : "0 eV (Below Threshold)";
    if (vEl) vEl.innerText = kMax > 0 ? `${v0.toFixed(2)} V` : "0 V";
  }

  animate() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;

    ctx.fillStyle = "#080c14";
    ctx.fillRect(0, 0, w, h);

    const cathodeX = 140;
    const anodeX = 620;

    // Draw Cathode Plate
    ctx.fillStyle = "#475569";
    ctx.fillRect(cathodeX - 10, 40, 15, 200);
    ctx.fillStyle = "#94a3b8";
    ctx.font = "11px Inter, sans-serif";
    ctx.fillText("Metal Cathode", cathodeX - 45, 30);

    // Draw Anode Plate
    ctx.fillStyle = "#334155";
    ctx.fillRect(anodeX, 40, 15, 200);
    ctx.fillText("Anode (+)", anodeX - 5, 30);

    // Draw Incoming Photons
    const hNu = 1240 / this.wavelengthNm;
    const hasEmission = hNu > this.workFunctionEV;

    ctx.strokeStyle = this.wavelengthNm < 400 ? "#a855f7" : (this.wavelengthNm < 550 ? "#38bdf8" : "#ef4444");
    ctx.lineWidth = 2;
    for (let i = 0; i < 4; i++) {
      const py = 60 + i * 45;
      ctx.beginPath();
      ctx.moveTo(30, py - 20);
      ctx.lineTo(cathodeX - 10, py);
      ctx.stroke();
    }

    // Spawn and update ejected electrons
    if (hasEmission && Math.random() < 0.4) {
      const vSpeed = Math.sqrt(hNu - this.workFunctionEV) * 2.5;
      this.electrons.push({
        x: cathodeX + 5,
        y: 50 + Math.random() * 170,
        vx: vSpeed,
        vy: (Math.random() - 0.5) * 0.8
      });
    }

    ctx.fillStyle = "#38bdf8";
    for (let i = this.electrons.length - 1; i >= 0; i--) {
      const el = this.electrons[i];
      el.x += el.vx;
      el.y += el.vy;

      ctx.beginPath();
      ctx.arc(el.x, el.y, 3, 0, Math.PI * 2);
      ctx.fill();

      if (el.x > anodeX || el.x < cathodeX) {
        this.electrons.splice(i, 1);
      }
    }

    this.animId = requestAnimationFrame(() => this.animate());
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}

// ==========================================
// 11. Bohr Quantized Atom Orbit Simulator
// ==========================================
class BohrOrbitSim {
  constructor(container) {
    this.container = container;
    this.nLevel = 3;
    this.animId = null;
    this.electronAngle = 0;
    this.photonPulse = null;
    this.initUI();
    this.animate();
  }

  initUI() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div>
            <span class="sim-badge">Topic §1.2 Experiment</span>
            <strong class="sim-title">Bohr Quantized Atomic Orbits & Photon Spectral Emission</strong>
          </div>
          <div class="sim-controls">
            <button class="btn-n" id="btn-n1">n = 1</button>
            <button class="btn-n" id="btn-n2">n = 2</button>
            <button class="btn-n active" id="btn-n3">n = 3</button>
            <button class="btn-n" id="btn-n4">n = 4</button>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="bohr-canvas" width="760" height="300"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="sim-metrics-grid">
          <div class="metric-card">
            <span class="metric-label">Orbital Energy (En = -13.6/n²)</span>
            <span class="metric-val" id="bohr-e-val">-1.51 eV</span>
          </div>
          <div class="metric-card">
            <span class="metric-label">Bohr Orbit Radius (rn = n² a0)</span>
            <span class="metric-val" id="bohr-r-val">9.0 a0 (4.76 Å)</span>
          </div>
          <div class="metric-card">
            <span class="metric-label">Angular Momentum (L = n ℏ)</span>
            <span class="metric-val" id="bohr-l-val">3 ℏ</span>
          </div>
        </div>
      </div>
    `;

    this.canvas = this.container.querySelector("#bohr-canvas");
    this.ctx = this.canvas.getContext("2d");

    [1, 2, 3, 4].forEach(n => {
      const btn = this.container.querySelector(`#btn-n${n}`);
      btn.addEventListener("click", () => {
        this.container.querySelectorAll(".btn-n").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        this.setOrbit(n);
      });
    });

    this.updateMetrics();
  }

  setOrbit(newN) {
    if (newN < this.nLevel) {
      // Photon emitted!
      const eDiff = 13.6 * (1 / (newN * newN) - 1 / (this.nLevel * this.nLevel));
      const lambdaNm = (1240 / eDiff).toFixed(1);
      this.photonPulse = {
        x: this.canvas.width / 2,
        y: this.canvas.height / 2,
        r: 10,
        lambda: lambdaNm
      };
    }
    this.nLevel = newN;
    this.updateMetrics();
  }

  updateMetrics() {
    const eVal = (-13.6 / (this.nLevel * this.nLevel)).toFixed(2);
    const rVal = (this.nLevel * this.nLevel).toFixed(1);

    const eEl = this.container.querySelector("#bohr-e-val");
    const rEl = this.container.querySelector("#bohr-r-val");
    const lEl = this.container.querySelector("#bohr-l-val");

    if (eEl) eEl.innerText = `${eVal} eV`;
    if (rEl) rEl.innerText = `${rVal} a₀ (${(rVal * 0.529).toFixed(2)} Å)`;
    if (lEl) lEl.innerText = `${this.nLevel} ℏ`;
  }

  animate() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    const midX = w / 2;
    const midY = h / 2;

    ctx.fillStyle = "#080c14";
    ctx.fillRect(0, 0, w, h);

    // Draw Nucleus
    ctx.fillStyle = "#ef4444";
    ctx.shadowColor = "#ef4444";
    ctx.shadowBlur = 15;
    ctx.beginPath();
    ctx.arc(midX, midY, 10, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;
    ctx.fillStyle = "#fff";
    ctx.font = "bold 9px Inter, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("+e", midX, midY + 3);

    // Draw quantized Bohr orbits
    for (let n = 1; n <= 4; n++) {
      const r = 25 * n * n * 0.28;
      ctx.strokeStyle = n === this.nLevel ? "#38bdf8" : "#334155";
      ctx.lineWidth = n === this.nLevel ? 2 : 1;
      ctx.setLineDash(n === this.nLevel ? [] : [4, 4]);
      ctx.beginPath();
      ctx.arc(midX, midY, r, 0, Math.PI * 2);
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // Draw orbiting electron
    this.electronAngle += 0.05 / (this.nLevel * 0.7);
    const curR = 25 * this.nLevel * this.nLevel * 0.28;
    const elX = midX + curR * Math.cos(this.electronAngle);
    const elY = midY + curR * Math.sin(this.electronAngle);

    ctx.fillStyle = "#38bdf8";
    ctx.shadowColor = "#38bdf8";
    ctx.shadowBlur = 10;
    ctx.beginPath();
    ctx.arc(elX, elY, 6, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    // Draw emitted photon wave pulse
    if (this.photonPulse) {
      this.photonPulse.r += 3.5;
      ctx.strokeStyle = "#fbbf24";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(this.photonPulse.x, this.photonPulse.y, this.photonPulse.r, 0, Math.PI * 2);
      ctx.stroke();

      ctx.fillStyle = "#fbbf24";
      ctx.fillText(`Photon Emission λ = ${this.photonPulse.lambda} nm`, this.photonPulse.x + this.photonPulse.r + 5, this.photonPulse.y - 10);

      if (this.photonPulse.r > 200) this.photonPulse = null;
    }

    this.animId = requestAnimationFrame(() => this.animate());
  }

  destroy() {
    if (this.animId) cancelAnimationFrame(this.animId);
  }
}

// ==========================================
// 12. Finite Square Potential Well Simulator
// ==========================================
class FiniteWellSim {
  constructor(container) {
    this.container = container;
    this.wellDepth = 50; // V0 in eV
    this.initUI();
    this.render();
  }

  initUI() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div>
            <span class="sim-badge">Topic §4.1 Experiment</span>
            <strong class="sim-title">Finite Square Potential Well & Evanescent Wave Tails</strong>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="fw-canvas" width="760" height="280"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="slider-control-group mt-3">
          <label>Potential Barrier Height (V0): <strong id="fw-v-lbl" style="color:#38bdf8;">50 eV</strong></label>
          <input type="range" class="range-slider" id="fw-v-slider" min="20" max="100" step="5" value="50">
        </div>
      </div>
    `;

    this.canvas = this.container.querySelector("#fw-canvas");
    this.ctx = this.canvas.getContext("2d");

    this.container.querySelector("#fw-v-slider").addEventListener("input", (e) => {
      this.wellDepth = parseFloat(e.target.value);
      this.container.querySelector("#fw-v-lbl").innerText = `${this.wellDepth} eV`;
      this.render();
    });

    this.render();
  }

  render() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    const midY = h / 2 + 30;

    ctx.fillStyle = "#080c14";
    ctx.fillRect(0, 0, w, h);

    const x1 = 280;
    const x2 = 480;
    const vH = (this.wellDepth / 100) * 120;

    // Draw Potential Well
    ctx.strokeStyle = "#94a3b8";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(60, midY - vH);
    ctx.lineTo(x1, midY - vH);
    ctx.lineTo(x1, midY);
    ctx.lineTo(x2, midY);
    ctx.lineTo(x2, midY - vH);
    ctx.lineTo(w - 60, midY - vH);
    ctx.stroke();

    ctx.fillStyle = "#94a3b8";
    ctx.font = "11px Inter, sans-serif";
    ctx.fillText("V = V0 (Classically Forbidden)", 90, midY - vH - 10);
    ctx.fillText("V = 0 (Well Interior)", 330, midY + 25);

    // Draw Ground State Wavefunction with Exponential Penetration Tails
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let x = 60; x <= w - 60; x++) {
      let psi;
      const eLevel = midY - vH * 0.35;
      if (x < x1) {
        psi = 40 * Math.exp((x - x1) / 30);
      } else if (x > x2) {
        psi = 40 * Math.exp(-(x - x2) / 30);
      } else {
        const midWell = (x1 + x2) / 2;
        psi = 40 * Math.cos((x - midWell) / 45);
      }

      const py = eLevel - psi;
      if (x === 60) ctx.moveTo(x, py);
      else ctx.lineTo(x, py);
    }
    ctx.stroke();

    ctx.fillStyle = "#38bdf8";
    ctx.fillText("Ground State ψ₁(x) penetrating barrier", 280, midY - vH * 0.35 - 50);
  }

  destroy() {}
}

// ==========================================
// 13. Spherical Harmonics 3D Angular Probability Lobes
// ==========================================
class AngularMomentumSim {
  constructor(container) {
    this.container = container;
    this.l = 1;
    this.m = 0;
    this.initUI();
    this.render();
  }

  initUI() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div>
            <span class="sim-badge">Topic §6.2 Experiment</span>
            <strong class="sim-title">Spherical Harmonics Y_l^m(θ, φ) Angular Probability Lobes</strong>
          </div>
          <div class="sim-controls">
            <button class="btn-n" id="btn-y00">s (l=0, m=0)</button>
            <button class="btn-n active" id="btn-y10">pz (l=1, m=0)</button>
            <button class="btn-n" id="btn-y11">px/py (l=1, m=±1)</button>
            <button class="btn-n" id="btn-y20">dz² (l=2, m=0)</button>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="ylm-canvas" width="760" height="280"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
      </div>
    `;

    this.canvas = this.container.querySelector("#ylm-canvas");
    this.ctx = this.canvas.getContext("2d");

    const setupBtn = (id, lVal, mVal) => {
      const b = this.container.querySelector(id);
      b.addEventListener("click", () => {
        this.container.querySelectorAll(".btn-n").forEach(btn => btn.classList.remove("active"));
        b.classList.add("active");
        this.l = lVal;
        this.m = mVal;
        this.render();
      });
    };

    setupBtn("#btn-y00", 0, 0);
    setupBtn("#btn-y10", 1, 0);
    setupBtn("#btn-y11", 1, 1);
    setupBtn("#btn-y20", 2, 0);

    this.render();
  }

  render() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    const midX = w / 2;
    const midY = h / 2;

    ctx.fillStyle = "#080c14";
    ctx.fillRect(0, 0, w, h);

    // Draw Axes
    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(midX, 20); ctx.lineTo(midX, h - 20);
    ctx.moveTo(midX - 180, midY); ctx.lineTo(midX + 180, midY);
    ctx.stroke();

    ctx.fillStyle = "#94a3b8";
    ctx.font = "11px Inter, sans-serif";
    ctx.fillText("+z", midX + 8, 30);
    ctx.fillText("+x", midX + 190, midY + 4);

    // Draw Angular Probability Lobe |Y_l^m|^2
    ctx.strokeStyle = "#38bdf8";
    ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
    ctx.lineWidth = 2.5;

    ctx.beginPath();
    for (let deg = 0; deg <= 360; deg++) {
      const th = deg * Math.PI / 180;
      let r;
      if (this.l === 0) {
        r = 75; // Spherically symmetric
      } else if (this.l === 1 && this.m === 0) {
        r = 120 * Math.cos(th) * Math.cos(th); // pz dumbbell
      } else if (this.l === 1 && this.m === 1) {
        r = 120 * Math.sin(th) * Math.sin(th); // px/py donut
      } else if (this.l === 2 && this.m === 0) {
        const p2 = 0.5 * (3 * Math.cos(th) * Math.cos(th) - 1);
        r = 110 * p2 * p2; // dz2
      }

      const px = midX + r * Math.sin(th);
      const py = midY - r * Math.cos(th);

      if (deg === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
  }

  destroy() {}
}

// ==========================================
// 14. Normal Zeeman Effect Magnetic Splitting Simulator
// ==========================================
class ZeemanSim {
  constructor(container) {
    this.container = container;
    this.magFieldTesla = 2.0; // B field
    this.initUI();
    this.render();
  }

  initUI() {
    this.container.innerHTML = `
      <div class="sim-wrapper">
        <div class="sim-header">
          <div>
            <span class="sim-badge">Topic §6.3 Experiment</span>
            <strong class="sim-title">Normal Zeeman Effect Spectral Splitting in Magnetic Field</strong>
          </div>
        </div>
        <div class="canvas-container">
          <canvas id="zm-canvas" width="760" height="260"></canvas>
          <div class="sim-watermark">OpenSTEM • Interactive Simulation Suite</div>
        </div>
        <div class="slider-control-group mt-3">
          <label>External Magnetic Field (B): <strong id="zm-b-lbl" style="color:#38bdf8;">2.0 Tesla</strong></label>
          <input type="range" class="range-slider" id="zm-b-slider" min="0" max="5.0" step="0.2" value="2.0">
        </div>
      </div>
    `;

    this.canvas = this.container.querySelector("#zm-canvas");
    this.ctx = this.canvas.getContext("2d");

    this.container.querySelector("#zm-b-slider").addEventListener("input", (e) => {
      this.magFieldTesla = parseFloat(e.target.value);
      this.container.querySelector("#zm-b-lbl").innerText = `${this.magFieldTesla.toFixed(1)} Tesla`;
      this.render();
    });

    this.render();
  }

  render() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    const midX = w / 2;

    ctx.fillStyle = "#080c14";
    ctx.fillRect(0, 0, w, h);

    const shift = this.magFieldTesla * 18;

    // Draw Spectral Lines
    ctx.fillStyle = "#94a3b8";
    ctx.font = "12px Inter, sans-serif";
    ctx.fillText("Unperturbed Line (B = 0)", 80, 50);
    ctx.fillText("Zeeman Triplet in B-Field", 480, 50);

    // Singlet on left
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(160, 80);
    ctx.lineTo(160, 200);
    ctx.stroke();

    // Triplet on right
    // pi line (m = 0)
    ctx.strokeStyle = "#10b981";
    ctx.beginPath();
    ctx.moveTo(560, 80);
    ctx.lineTo(560, 200);
    ctx.stroke();
    ctx.fillStyle = "#10b981";
    ctx.fillText("π (m=0)", 545, 220);

    // sigma+ line (m = +1)
    ctx.strokeStyle = "#38bdf8";
    ctx.beginPath();
    ctx.moveTo(560 + shift, 80);
    ctx.lineTo(560 + shift, 200);
    ctx.stroke();
    ctx.fillStyle = "#38bdf8";
    ctx.fillText("σ+ (m=+1)", 545 + shift, 240);

    // sigma- line (m = -1)
    ctx.strokeStyle = "#f43f5e";
    ctx.beginPath();
    ctx.moveTo(560 - shift, 80);
    ctx.lineTo(560 - shift, 200);
    ctx.stroke();
    ctx.fillStyle = "#f43f5e";
    ctx.fillText("σ- (m=-1)", 545 - shift, 240);
  }

  destroy() {}
}
