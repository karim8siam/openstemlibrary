/**
 * quantum-chemistry-thermodynamics-sims.js
 * 10 High-Performance 60 FPS Interactive HTML5 Canvas Simulation Engines
 * for Quantum Chemistry & Statistical Thermodynamics (OpenSTEM Milestone Textbook #52)
 */

window.QuantumChemistrySimulations = (function() {
  'use strict';

  // Optimized high-DPI canvas initialization with dimensions caching (avoids per-frame GPU allocations)
  function initCanvas(canvas) {
    if (!canvas) return null;
    const dpr = window.devicePixelRatio || 1;
    let w = canvas._cssWidth;
    let h = canvas._cssHeight;

    if (!w || !h) {
      const rect = canvas.getBoundingClientRect();
      w = Math.floor(rect.width > 0 ? rect.width : (canvas.parentElement ? canvas.parentElement.clientWidth : 800)) || 800;
      h = Math.floor(rect.height > 0 ? rect.height : (canvas.parentElement ? canvas.parentElement.clientHeight : 340)) || 340;
      canvas._cssWidth = w;
      canvas._cssHeight = h;
    }

    const targetW = Math.round(w * dpr);
    const targetH = Math.round(h * dpr);

    if (canvas.width !== targetW || canvas.height !== targetH) {
      canvas.width = targetW;
      canvas.height = targetH;
      const ctx = canvas.getContext('2d');
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    const ctx = canvas.getContext('2d');
    return { ctx, width: w, height: h, dpr };
  }

  if (typeof window !== 'undefined') {
    window.addEventListener('resize', function() {
      document.querySelectorAll('.sim-canvas').forEach(function(c) {
        c._cssWidth = null;
        c._cssHeight = null;
      });
    });
  }

  function getContainerEl(c) {
    return typeof c === 'string' ? document.getElementById(c) : c;
  }

  /* =========================================================================
     SIMULATION 1: sim_qc_blackbody_compton_wavepacket (Unit 1)
     Planck Blackbody Radiance vs Classical Rayleigh-Jeans Catastrophe & Wavepacket
     ========================================================================= */
  function sim_qc_blackbody_compton_wavepacket(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Planck Blackbody Radiance & Quantum Wavepacket</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 1: Foundations & Classical Failures</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="qc1_btn_mode" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Mode: Planck Radiance</button>
            <button id="qc1_btn_reset" style="background:#1e293b; color:#94a3b8; border:1px solid #475569; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Reset</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc1_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Absolute Temperature T: <span id="qc1_T_val" style="color:#38bdf8; font-weight:600;">5500 K</span></label>
            <input type="range" id="qc1_T" min="2500" max="8000" value="5500" step="100" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Wavepacket Initial Width Δx₀: <span id="qc1_sig_val" style="color:#f472b6; font-weight:600;">1.20 a.u.</span></label>
            <input type="range" id="qc1_sig" min="0.5" max="3.0" value="1.2" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Wavepacket Velocity v₀: <span id="qc1_v_val" style="color:#34d399; font-weight:600;">2.0 a.u.</span></label>
            <input type="range" id="qc1_v" min="0.0" max="5.0" value="2.0" step="0.2" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc1_canvas");
    let state = { T: 5500, sig0: 1.2, v0: 2.0, mode: "planck", t: 0 };
    let animId = null;

    document.getElementById("qc1_T").oninput = (e) => {
      state.T = parseFloat(e.target.value);
      document.getElementById("qc1_T_val").innerText = `${state.T} K`;
    };
    document.getElementById("qc1_sig").oninput = (e) => {
      state.sig0 = parseFloat(e.target.value);
      document.getElementById("qc1_sig_val").innerText = `${state.sig0.toFixed(2)} a.u.`;
    };
    document.getElementById("qc1_v").oninput = (e) => {
      state.v0 = parseFloat(e.target.value);
      document.getElementById("qc1_v_val").innerText = `${state.v0.toFixed(1)} a.u.`;
    };

    const modeBtn = document.getElementById("qc1_btn_mode");
    modeBtn.onclick = () => {
      state.mode = state.mode === "planck" ? "wavepacket" : "planck";
      modeBtn.innerText = state.mode === "planck" ? "Mode: Planck Radiance" : "Mode: Wavepacket Dispersion";
      state.t = 0;
    };

    document.getElementById("qc1_btn_reset").onclick = () => {
      state.T = 5500; state.sig0 = 1.2; state.v0 = 2.0; state.t = 0;
      document.getElementById("qc1_T").value = 5500;
      document.getElementById("qc1_sig").value = 1.2;
      document.getElementById("qc1_v").value = 2.0;
      document.getElementById("qc1_T_val").innerText = "5500 K";
      document.getElementById("qc1_sig_val").innerText = "1.20 a.u.";
      document.getElementById("qc1_v_val").innerText = "2.0 a.u.";
    };

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.03;

      if (state.mode === "planck") {
        // Grid & Axes
        ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
        for (let x = 60; x < W; x += 60) { ctx.beginPath(); ctx.moveTo(x, 20); ctx.lineTo(x, H - 40); ctx.stroke(); }
        for (let y = 30; y < H - 40; y += 40) { ctx.beginPath(); ctx.moveTo(60, y); ctx.lineTo(W - 20, y); ctx.stroke(); }

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(60, 20); ctx.lineTo(60, H - 40); ctx.lineTo(W - 20, H - 40); ctx.stroke();

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Wavelength λ (nm)", W / 2 - 40, H - 15);
        ctx.save(); ctx.translate(20, H / 2 + 30); ctx.rotate(-Math.PI / 2);
        ctx.fillText("Spectral Radiance u(λ, T)", 0, 0); ctx.restore();

        // Visible spectrum rainbow background band (380 - 750 nm)
        const xVisStart = 60 + ((380) / 2000) * (W - 80);
        const xVisEnd = 60 + ((750) / 2000) * (W - 80);
        const gradVis = ctx.createLinearGradient(xVisStart, 0, xVisEnd, 0);
        gradVis.addColorStop(0, "rgba(147, 51, 234, 0.15)");
        gradVis.addColorStop(0.2, "rgba(59, 130, 246, 0.15)");
        gradVis.addColorStop(0.4, "rgba(16, 185, 129, 0.15)");
        gradVis.addColorStop(0.7, "rgba(234, 179, 8, 0.15)");
        gradVis.addColorStop(1, "rgba(239, 68, 68, 0.15)");
        ctx.fillStyle = gradVis;
        ctx.fillRect(xVisStart, 20, xVisEnd - xVisStart, H - 60);

        ctx.fillStyle = "#64748b"; ctx.font = "10px sans-serif";
        ctx.fillText("Visible", (xVisStart + xVisEnd) / 2 - 15, 35);

        // Constants for normalized Planck calculation
        const c1 = 1.191e8; // arb scaling
        const c2 = 1.439e7;
        const T = state.T;
        const maxScale = (T / 5500) ** 5 * 1.4;

        // Draw Classical Rayleigh-Jeans (UV Catastrophe)
        ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.8; ctx.setLineDash([4, 4]);
        ctx.beginPath();
        for (let x = 60; x < W - 20; x++) {
          const lam = 100 + ((x - 60) / (W - 80)) * 2000; // nm
          const rj = (T / 5500) * (1500 / lam) ** 4 * 0.12 * (H - 80);
          const y = (H - 40) - rj;
          if (x === 60) ctx.moveTo(x, Math.max(20, y));
          else ctx.lineTo(x, Math.max(20, y));
        }
        ctx.stroke();
        ctx.setLineDash([]);

        // Draw Quantum Planck Curve
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        let maxLam = 0, maxY = H - 40;
        for (let x = 60; x < W - 20; x++) {
          const lam = 100 + ((x - 60) / (W - 80)) * 2000; // nm
          const expTerm = Math.exp((c2 / (lam * T)) * 0.001);
          const u = (1e9 / (lam ** 5)) / (expTerm - 1);
          const normU = (u / maxScale) * (H - 80) * 0.85;
          const y = (H - 40) - normU;
          if (normU > (H - 40 - maxY)) { maxY = y; maxLam = lam; }
          if (x === 60) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Wien's Displacement Peak
        const xPeak = 60 + ((2.898e6 / T - 100) / 2000) * (W - 80);
        if (xPeak >= 60 && xPeak <= W - 20) {
          ctx.fillStyle = "#fbbf24";
          ctx.beginPath(); ctx.arc(xPeak, maxY, 4, 0, Math.PI * 2); ctx.fill();
          ctx.fillText(`λ_max = ${(2.898e6 / T).toFixed(0)} nm`, xPeak + 8, maxY - 8);
        }

        // Legend
        ctx.fillStyle = "#38bdf8"; ctx.fillText("— Planck Quantum Law (Experimental Match)", 80, 50);
        ctx.fillStyle = "#ef4444"; ctx.fillText("- - Classical Rayleigh-Jeans (Ultraviolet Catastrophe)", 80, 68);
        ctx.fillStyle = "#fbbf24"; ctx.fillText(`• Wien's Law: λ_max · T = 2.898 × 10⁶ nm·K`, 80, 86);

      } else {
        // Mode: Wavepacket Dispersion
        ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
        const cy = H / 2;
        ctx.beginPath(); ctx.moveTo(40, cy); ctx.lineTo(W - 40, cy); ctx.stroke();

        const x0 = 100 + (state.v0 * state.t * 15) % (W - 200);
        const hbar_m = 1.0;
        const st = state.sig0 * Math.sqrt(1 + (state.t * hbar_m / (state.sig0 ** 2)) ** 2);

        // Draw Probability Density |ψ(x, t)|²
        ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let x = 40; x < W - 40; x++) {
          const dx = (x - x0) / (st * 18);
          const prob = Math.exp(-dx * dx) * (state.sig0 / st) * 110;
          const y = cy - prob;
          if (x === 40) ctx.moveTo(x, cy); else ctx.lineTo(x, y);
        }
        ctx.lineTo(W - 40, cy); ctx.closePath();
        ctx.fill(); ctx.stroke();

        // Draw Phase oscillations Re[ψ]
        ctx.strokeStyle = "#f472b6"; ctx.lineWidth = 1.5;
        ctx.beginPath();
        for (let x = 40; x < W - 40; x++) {
          const dx = (x - x0) / (st * 18);
          const amp = Math.exp(-dx * dx * 0.5) * Math.sqrt(state.sig0 / st) * 60;
          const phase = state.v0 * (x - x0) * 0.2 - state.t * 3;
          const y = cy - amp * Math.cos(phase);
          if (x === 40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Probability Density |ψ(x, t)|² (Dispersion Δx(t) = ${st.toFixed(2)} a.u.)`, 60, 40);
        ctx.fillStyle = "#f472b6";
        ctx.fillText("Real Wavefunction Re[ψ(x, t)] (Phase Velocity vs Group Velocity)", 60, 58);
        ctx.fillStyle = "#fbbf24";
        ctx.fillText(`Heisenberg Uncertainty Principle: Δx · Δp ≥ ℏ / 2`, 60, 76);
      }

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 2: sim_qc_particle_box_ring_quantum (Unit 2)
     1D/2D Particle in a Box & Cyclic Ring Aromatic Quantization
     ========================================================================= */
  function sim_qc_particle_box_ring_quantum(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Particle in a Box & Electron in a Ring</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 2: Bound States & Periodic Boundaries</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="qc2_btn_geom" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Model: 1D Infinite Well</button>
            <button id="qc2_btn_prob" style="background:#1e293b; color:#34d399; border:1px solid #34d399; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Show: |ψ|² Density</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc2_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Quantum Number n (or m_l): <span id="qc2_n_val" style="color:#38bdf8; font-weight:600;">3</span></label>
            <input type="range" id="qc2_n" min="1" max="6" value="3" step="1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Box Length L: <span id="qc2_L_val" style="color:#f472b6; font-weight:600;">1.0 nm</span></label>
            <input type="range" id="qc2_L" min="0.5" max="2.0" value="1.0" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Potential Barrier V₀: <span id="qc2_V_val" style="color:#fbbf24; font-weight:600;">∞ (Infinite)</span></label>
            <input type="range" id="qc2_V" min="10" max="100" value="100" step="10" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc2_canvas");
    let state = { n: 3, L: 1.0, geom: "1d", showProb: true, t: 0 };
    let animId = null;

    document.getElementById("qc2_n").oninput = (e) => {
      state.n = parseInt(e.target.value);
      document.getElementById("qc2_n_val").innerText = state.n;
    };
    document.getElementById("qc2_L").oninput = (e) => {
      state.L = parseFloat(e.target.value);
      document.getElementById("qc2_L_val").innerText = `${state.L.toFixed(1)} nm`;
    };

    const geomBtn = document.getElementById("qc2_btn_geom");
    geomBtn.onclick = () => {
      state.geom = state.geom === "1d" ? "ring" : "1d";
      geomBtn.innerText = state.geom === "1d" ? "Model: 1D Infinite Well" : "Model: Electron in a Ring";
    };

    const probBtn = document.getElementById("qc2_btn_prob");
    probBtn.onclick = () => {
      state.showProb = !state.showProb;
      probBtn.innerText = state.showProb ? "Show: |ψ|² Density" : "Show: Wavefunction ψ";
    };

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.04;

      if (state.geom === "1d") {
        const left = W * 0.15, right = W * 0.85, base = H * 0.82;
        const boxW = right - left;

        // Infinite Potential Walls
        ctx.fillStyle = "rgba(239, 68, 68, 0.15)";
        ctx.fillRect(0, 30, left, base - 30);
        ctx.fillRect(right, 30, W - right, base - 30);

        ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, base); ctx.lineTo(right, base); ctx.lineTo(right, 30); ctx.stroke();

        ctx.fillStyle = "#ef4444"; ctx.font = "12px sans-serif";
        ctx.fillText("V = ∞", left - 45, 60); ctx.fillText("V = ∞", right + 10, 60);
        ctx.fillStyle = "#94a3b8"; ctx.fillText("V = 0", (left + right) / 2 - 15, base + 20);

        // Draw Energy levels E_k = k² E₁
        for (let k = 1; k <= 5; k++) {
          const eNorm = (k * k) / 25;
          const yLevel = base - eNorm * (base - 60);
          ctx.strokeStyle = k === state.n ? "#38bdf8" : "#334155";
          ctx.lineWidth = k === state.n ? 2 : 1;
          ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.moveTo(left, yLevel); ctx.lineTo(right, yLevel); ctx.stroke();
          ctx.setLineDash([]);
          ctx.fillStyle = k === state.n ? "#38bdf8" : "#64748b";
          ctx.fillText(`n=${k} (E_${k} = ${k*k}·E₁)`, right + 10, yLevel + 4);
        }

        // Draw current state ψ_n(x) or |ψ_n(x)|²
        const n = state.n;
        const eNorm = (n * n) / 25;
        const yRef = base - eNorm * (base - 60);

        ctx.strokeStyle = state.showProb ? "#34d399" : "#38bdf8";
        ctx.fillStyle = state.showProb ? "rgba(52, 211, 153, 0.2)" : "rgba(56, 189, 248, 0.2)";
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        const amp = 45;
        for (let x = left; x <= right; x++) {
          const frac = (x - left) / boxW;
          const psi = Math.sin(n * Math.PI * frac);
          const val = state.showProb ? (psi * psi) * amp : psi * amp * Math.cos(state.t);
          const y = yRef - val;
          if (x === left) ctx.moveTo(x, yRef); else ctx.lineTo(x, y);
        }
        if (state.showProb) { ctx.lineTo(right, yRef); ctx.closePath(); ctx.fill(); }
        ctx.stroke();

        ctx.fillStyle = "#fbbf24"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`E_${n} = n² h² / (8 m L²) = ${(n*n).toFixed(0)} E₁ | Nodes = ${n-1}`, left, 45);

      } else {
        // Model: Electron in a Ring (Aromatic Ring Quantization)
        const cx = W / 2, cy = H / 2, R = 90;
        ctx.strokeStyle = "#475569"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.stroke();

        const m = state.n;
        const pts = 200;
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
        ctx.beginPath();

        for (let i = 0; i <= pts; i++) {
          const phi = (i / pts) * Math.PI * 2;
          const psi = Math.cos(m * phi - state.t * 2);
          const rMod = R + (state.showProb ? (psi * psi * 35) : (psi * 30));
          const x = cx + rMod * Math.cos(phi);
          const y = cy + rMod * Math.sin(phi);
          if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.closePath(); ctx.stroke(); ctx.fill();

        // Node markers
        for (let k = 0; k < 2 * m; k++) {
          const angle = (k * Math.PI) / m + (state.t * 2) / m;
          const nx = cx + R * Math.cos(angle);
          const ny = cy + R * Math.sin(angle);
          ctx.fillStyle = "#f472b6";
          ctx.beginPath(); ctx.arc(nx, ny, 3.5, 0, Math.PI * 2); ctx.fill();
        }

        ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Electron on a Ring: ψ(ϕ) = (2π)^(-1/2) exp(i m_l ϕ) | Angular Momentum L_z = ${m} ℏ`, 40, 40);
        ctx.fillStyle = "#f472b6";
        ctx.fillText(`Degeneracy g = 2 (±m_l for m_l ≠ 0) | Nodal Points = ${2 * m} | Hückel (4n+2) Benzene π-ring`, 40, 58);
      }

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 3: sim_qc_harmonic_oscillator_ladder (Unit 3)
     Hermite Polynomials, Turning Points & Ladder Operator Transitions
     ========================================================================= */
  function sim_qc_harmonic_oscillator_ladder(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Harmonic Oscillator & Ladder Operators</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 3: Hermite Eigenfunctions & Zero-Point Energy</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="qc3_btn_raise" style="background:#1e293b; color:#34d399; border:1px solid #34d399; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">a† Raise Level</button>
            <button id="qc3_btn_lower" style="background:#1e293b; color:#f472b6; border:1px solid #f472b6; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">a Lower Level</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc3_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Vibrational Quantum Number v: <span id="qc3_v_val" style="color:#38bdf8; font-weight:600;">2</span></label>
            <input type="range" id="qc3_v" min="0" max="5" value="2" step="1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Force Constant k: <span id="qc3_k_val" style="color:#fbbf24; font-weight:600;">1.0 a.u.</span></label>
            <input type="range" id="qc3_k" min="0.5" max="2.0" value="1.0" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Reduced Mass μ: <span id="qc3_mu_val" style="color:#34d399; font-weight:600;">1.0 a.u.</span></label>
            <input type="range" id="qc3_mu" min="0.5" max="2.0" value="1.0" step="0.1" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc3_canvas");
    let state = { v: 2, k: 1.0, mu: 1.0, t: 0 };
    let animId = null;

    document.getElementById("qc3_v").oninput = (e) => {
      state.v = parseInt(e.target.value);
      document.getElementById("qc3_v_val").innerText = state.v;
    };
    document.getElementById("qc3_k").oninput = (e) => {
      state.k = parseFloat(e.target.value);
      document.getElementById("qc3_k_val").innerText = `${state.k.toFixed(1)} a.u.`;
    };
    document.getElementById("qc3_mu").oninput = (e) => {
      state.mu = parseFloat(e.target.value);
      document.getElementById("qc3_mu_val").innerText = `${state.mu.toFixed(1)} a.u.`;
    };

    document.getElementById("qc3_btn_raise").onclick = () => {
      if (state.v < 5) {
        state.v++;
        document.getElementById("qc3_v").value = state.v;
        document.getElementById("qc3_v_val").innerText = state.v;
      }
    };
    document.getElementById("qc3_btn_lower").onclick = () => {
      if (state.v > 0) {
        state.v--;
        document.getElementById("qc3_v").value = state.v;
        document.getElementById("qc3_v_val").innerText = state.v;
      }
    };

    // Hermite polynomials H_v(y)
    function hermite(v, y) {
      if (v === 0) return 1;
      if (v === 1) return 2 * y;
      if (v === 2) return 4 * y * y - 2;
      if (v === 3) return 8 * y * y * y - 12 * y;
      if (v === 4) return 16 * y ** 4 - 48 * y * y + 12;
      if (v === 5) return 32 * y ** 5 - 160 * y ** 3 + 120 * y;
      return 1;
    }

    const normFactors = [
      1 / Math.PI ** 0.25,
      1 / (Math.sqrt(2) * Math.PI ** 0.25),
      1 / (Math.sqrt(8) * Math.PI ** 0.25),
      1 / (Math.sqrt(48) * Math.PI ** 0.25),
      1 / (Math.sqrt(384) * Math.PI ** 0.25),
      1 / (Math.sqrt(3840) * Math.PI ** 0.25)
    ];

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.03;

      const cx = W / 2, base = H * 0.85;
      const omega = Math.sqrt(state.k / state.mu);

      // Draw Parabolic Potential V(x) = 1/2 k x²
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 40; x < W - 40; x++) {
        const dx = (x - cx) / 50;
        const v_pot = 0.5 * state.k * dx * dx * 28;
        const y = base - v_pot;
        if (x === 40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Draw energy level rungs E_v = (v + 1/2) ℏω
      const dE = 38 * omega;
      for (let v = 0; v <= 5; v++) {
        const yE = base - (v + 0.5) * dE;
        const xTurn = Math.sqrt((v + 0.5) * 2 / state.k) * 50;

        ctx.strokeStyle = v === state.v ? "#38bdf8" : "#334155";
        ctx.lineWidth = v === state.v ? 2 : 1;
        ctx.beginPath();
        ctx.moveTo(cx - xTurn, yE); ctx.lineTo(cx + xTurn, yE);
        ctx.stroke();

        ctx.fillStyle = v === state.v ? "#38bdf8" : "#64748b";
        ctx.font = "10px sans-serif";
        ctx.fillText(`v=${v} (E = ${(v + 0.5).toFixed(1)} ℏω)`, cx + xTurn + 8, yE + 3);
      }

      // Draw Wavefunction ψ_v(x) for selected state
      const v = state.v;
      const yE = base - (v + 0.5) * dE;
      const nf = normFactors[v] || 0.5;

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      ctx.beginPath();

      const alpha = Math.sqrt(state.k * state.mu);
      const scaleX = 45;
      for (let x = cx - 180; x <= cx + 180; x++) {
        const y_norm = ((x - cx) / scaleX) * Math.sqrt(alpha);
        const psi = nf * Math.exp(-0.5 * y_norm * y_norm) * hermite(v, y_norm);
        const prob = (psi * psi) * 45;
        const y = yE - prob;
        if (x === cx - 180) ctx.moveTo(x, yE); else ctx.lineTo(x, y);
      }
      ctx.lineTo(cx + 180, yE); ctx.closePath();
      ctx.fill(); ctx.stroke();

      // Turning point verticals
      const xTurn = Math.sqrt((v + 0.5) * 2 / state.k) * 50;
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(cx - xTurn, yE - 30); ctx.lineTo(cx - xTurn, yE + 20);
      ctx.moveTo(cx + xTurn, yE - 30); ctx.lineTo(cx + xTurn, yE + 20);
      ctx.stroke(); ctx.setLineDash([]);

      ctx.fillStyle = "#fbbf24"; ctx.font = "10px sans-serif";
      ctx.fillText("Classical Turning Point", cx + xTurn - 40, yE - 35);

      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Zero-Point Energy E₀ = 1/2 ℏω | Turning Points x_c = ±√(2(v+1/2)ℏ/k)`, 40, 40);
      ctx.fillStyle = "#34d399";
      ctx.fillText(`Ladder Operators: a†|v⟩ = √(v+1)|v+1⟩ ,  a|v⟩ = √v|v-1⟩`, 40, 58);

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 4: sim_qc_hydrogen_orbital_radial_prob (Unit 4)
     Hydrogen Atom Wavefunctions & Radial Distribution Probability P(r) = 4πr²R²
     ========================================================================= */
  function sim_qc_hydrogen_orbital_radial_prob(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Hydrogen Atom Radial Functions & 3D Orbitals</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 4: Central Field & Quantum Numbers (n, l)</span>
          </div>
          <div style="display:flex; gap:6px;">
            <select id="qc4_orbital_sel" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 8px; border-radius:4px; font-size:0.75rem; cursor:pointer;">
              <option value="1s">1s (n=1, l=0)</option>
              <option value="2s">2s (n=2, l=0)</option>
              <option value="2p">2p (n=2, l=1)</option>
              <option value="3s">3s (n=3, l=0)</option>
              <option value="3p">3p (n=3, l=1)</option>
              <option value="3d">3d (n=3, l=2)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc4_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Effective Nuclear Charge Z: <span id="qc4_Z_val" style="color:#38bdf8; font-weight:600;">1.0 (H)</span></label>
            <input type="range" id="qc4_Z" min="1.0" max="4.0" value="1.0" step="0.2" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Max Distance Range r_max: <span id="qc4_rmax_val" style="color:#f472b6; font-weight:600;">20 a₀</span></label>
            <input type="range" id="qc4_rmax" min="10" max="35" value="20" step="5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Display Mode: <span id="qc4_disp_val" style="color:#34d399; font-weight:600;">Both R(r) & P(r)</span></label>
            <input type="range" id="qc4_disp" min="1" max="3" value="1" step="1" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc4_canvas");
    let state = { orbital: "2s", Z: 1.0, rmax: 20, disp: 1, t: 0 };
    let animId = null;

    document.getElementById("qc4_orbital_sel").onchange = (e) => {
      state.orbital = e.target.value;
    };
    document.getElementById("qc4_Z").oninput = (e) => {
      state.Z = parseFloat(e.target.value);
      document.getElementById("qc4_Z_val").innerText = state.Z.toFixed(1);
    };
    document.getElementById("qc4_rmax").oninput = (e) => {
      state.rmax = parseInt(e.target.value);
      document.getElementById("qc4_rmax_val").innerText = `${state.rmax} a₀`;
    };
    document.getElementById("qc4_disp").oninput = (e) => {
      state.disp = parseInt(e.target.value);
      const labels = ["Both R(r) & P(r)", "R(r) Wavefunction Only", "P(r) = 4πr²R² Distribution"];
      document.getElementById("qc4_disp_val").innerText = labels[state.disp - 1];
    };

    // Radial wavefunctions R_nl(rho)
    function calcR(orb, r, Z) {
      const rho = Z * r; // in units of a_0
      if (orb === "1s") return 2 * (Z ** 1.5) * Math.exp(-rho);
      if (orb === "2s") return (1 / (2 * Math.sqrt(2))) * (Z ** 1.5) * (2 - rho) * Math.exp(-rho / 2);
      if (orb === "2p") return (1 / (2 * Math.sqrt(6))) * (Z ** 1.5) * rho * Math.exp(-rho / 2);
      if (orb === "3s") return (2 / (81 * Math.sqrt(3))) * (Z ** 1.5) * (27 - 18 * rho + 2 * rho * rho) * Math.exp(-rho / 3);
      if (orb === "3p") return (4 / (81 * Math.sqrt(6))) * (Z ** 1.5) * (6 * rho - rho * rho) * Math.exp(-rho / 3);
      if (orb === "3d") return (4 / (81 * Math.sqrt(30))) * (Z ** 1.5) * (rho * rho) * Math.exp(-rho / 3);
      return 0;
    }

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.02;

      const base = H * 0.8;
      const left = 60, right = W - 40;
      const plotW = right - left;

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, base); ctx.lineTo(right, base); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Radius r (in Bohr radii a₀)", W / 2 - 40, base + 25);

      // Grid
      for (let r = 5; r <= state.rmax; r += 5) {
        const x = left + (r / state.rmax) * plotW;
        ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.moveTo(x, 30); ctx.lineTo(x, base); ctx.stroke();
        ctx.fillText(`${r}`, x - 4, base + 15);
      }

      // Plot Radial Distribution Function P(r) = 4π r² R²
      if (state.disp === 1 || state.disp === 3) {
        ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();

        let maxP = 0, rPeak = 0;
        for (let x = left; x <= right; x++) {
          const r = ((x - left) / plotW) * state.rmax;
          const R = calcR(state.orbital, r, state.Z);
          const P = 4 * Math.PI * r * r * R * R;
          if (P > maxP) { maxP = P; rPeak = r; }
          const y = base - P * 150;
          if (x === left) ctx.moveTo(x, base); else ctx.lineTo(x, y);
        }
        ctx.lineTo(right, base); ctx.closePath();
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#38bdf8";
        ctx.fillText(`Peak Probability r_max = ${rPeak.toFixed(2)} a₀`, left + 20, 50);
      }

      // Plot Radial Wavefunction R(r)
      if (state.disp === 1 || state.disp === 2) {
        ctx.strokeStyle = "#f472b6"; ctx.lineWidth = 2;
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const r = ((x - left) / plotW) * state.rmax;
          const R = calcR(state.orbital, r, state.Z);
          const y = base - R * 90;
          if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.fillStyle = "#f472b6";
        ctx.fillText("— Radial Wavefunction R_nl(r)", left + 20, 70);
      }

      // Node count calculation
      const orb = state.orbital;
      const n = parseInt(orb[0]);
      const l = orb[1] === 's' ? 0 : (orb[1] === 'p' ? 1 : 2);
      const radNodes = n - l - 1;

      ctx.fillStyle = "#fbbf24"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Orbital ${orb}: Principal n = ${n}, Angular l = ${l} | Radial Nodes = ${radNodes} | Angular Nodes = ${l}`, left + 20, 90);

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 5: sim_qc_variational_perturbation_solver (Unit 5)
     Variational Energy Minimization & 2-State Perturbation Repulsion
     ========================================================================= */
  function sim_qc_variational_perturbation_solver(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Variational Principle & Perturbation Level Repulsion</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 5: Quantum Approximation Methods</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="qc5_btn_mode" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Model: Variational Principle</button>
            <button id="qc5_btn_opt" style="background:#1e293b; color:#34d399; border:1px solid #34d399; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Snap to Minimum</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc5_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Variational Parameter α: <span id="qc5_alpha_val" style="color:#38bdf8; font-weight:600;">1.40</span></label>
            <input type="range" id="qc5_alpha" min="0.3" max="3.0" value="1.4" step="0.05" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Perturbation Coupling V₁₂: <span id="qc5_V12_val" style="color:#f472b6; font-weight:600;">0.80 a.u.</span></label>
            <input type="range" id="qc5_V12" min="0.0" max="2.5" value="0.8" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Unperturbed Gap ΔE₀: <span id="qc5_gap_val" style="color:#fbbf24; font-weight:600;">1.50 a.u.</span></label>
            <input type="range" id="qc5_gap" min="0.2" max="3.0" value="1.5" step="0.1" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc5_canvas");
    let state = { alpha: 1.4, V12: 0.8, gap: 1.5, mode: "variational", t: 0 };
    let animId = null;

    document.getElementById("qc5_alpha").oninput = (e) => {
      state.alpha = parseFloat(e.target.value);
      document.getElementById("qc5_alpha_val").innerText = state.alpha.toFixed(2);
    };
    document.getElementById("qc5_V12").oninput = (e) => {
      state.V12 = parseFloat(e.target.value);
      document.getElementById("qc5_V12_val").innerText = `${state.V12.toFixed(2)} a.u.`;
    };
    document.getElementById("qc5_gap").oninput = (e) => {
      state.gap = parseFloat(e.target.value);
      document.getElementById("qc5_gap_val").innerText = `${state.gap.toFixed(2)} a.u.`;
    };

    const modeBtn = document.getElementById("qc5_btn_mode");
    modeBtn.onclick = () => {
      state.mode = state.mode === "variational" ? "perturbation" : "variational";
      modeBtn.innerText = state.mode === "variational" ? "Model: Variational Principle" : "Model: Avoided Crossing (Perturbation)";
    };

    document.getElementById("qc5_btn_opt").onclick = () => {
      state.alpha = 1.0;
      document.getElementById("qc5_alpha").value = 1.0;
      document.getElementById("qc5_alpha_val").innerText = "1.00";
    };

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.03;

      if (state.mode === "variational") {
        // Plot Variational E(alpha) curve vs exact ground state E_0
        const left = 60, right = W - 40, base = H * 0.85;
        const plotW = right - left;

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, base); ctx.lineTo(right, base); ctx.stroke();

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Variational Parameter α", W / 2 - 40, base + 25);
        ctx.fillText("Energy ⟨H⟩", 15, 40);

        // Exact ground state E_0 line (e.g. E_0 = 0.50)
        const yE0 = base - 0.5 * 140;
        ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(left, yE0); ctx.lineTo(right, yE0); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#ef4444"; ctx.fillText("Exact Ground State E₀ = 0.50 ℏω", right - 220, yE0 - 8);

        // Variational Curve E(alpha) = 1/4 (alpha + 1/alpha) -> min at alpha=1, E=0.5
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const a = 0.3 + ((x - left) / plotW) * 2.7;
          const E = 0.25 * (a + 1 / a);
          const y = base - E * 140;
          if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Current Alpha Marker
        const curX = left + ((state.alpha - 0.3) / 2.7) * plotW;
        const curE = 0.25 * (state.alpha + 1 / state.alpha);
        const curY = base - curE * 140;

        ctx.fillStyle = "#fbbf24";
        ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillText(`⟨E⟩(α) = ${curE.toFixed(3)} ℏω`, curX + 10, curY - 10);

        ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Variational Theorem: ⟨ψ_trial|H|ψ_trial⟩ ≥ E₀ (Upper Bound Property)", left + 20, 50);
        ctx.fillStyle = "#34d399";
        ctx.fillText("Minimum reached at d⟨E⟩/dα = 0 ⇒ Optimal Wavefunction Approximation", left + 20, 68);

      } else {
        // Mode: 2-State Avoided Crossing Level Repulsion
        const left = 60, right = W - 40, cy = H / 2;
        const plotW = right - left;

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, H - 30); ctx.lineTo(right, H - 30); ctx.stroke();

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Tuning Parameter λ", W / 2 - 40, H - 15);

        // Diabatic unperturbed crossing lines
        ctx.strokeStyle = "#64748b"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const lam = -2.0 + ((x - left) / plotW) * 4.0;
          const e1_0 = -lam * 20;
          const e2_0 = lam * 20;
          if (x === left) { ctx.moveTo(x, cy - e1_0); } else { ctx.lineTo(x, cy - e1_0); }
        }
        ctx.stroke();

        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const lam = -2.0 + ((x - left) / plotW) * 4.0;
          const e2_0 = lam * 20;
          if (x === left) { ctx.moveTo(x, cy - e2_0); } else { ctx.lineTo(x, cy - e2_0); }
        }
        ctx.stroke();
        ctx.setLineDash([]);

        // Adiabatic perturbed eigenvalues E_± = 1/2 (E1+E2) ± 1/2 √((E1-E2)² + 4 V12²)
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const lam = -2.0 + ((x - left) / plotW) * 4.0;
          const delta = lam * 40;
          const split = Math.sqrt(delta * delta + 4 * (state.V12 * 35) ** 2) * 0.5;
          const y = cy - split;
          if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        ctx.strokeStyle = "#f472b6"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const lam = -2.0 + ((x - left) / plotW) * 4.0;
          const delta = lam * 40;
          const split = Math.sqrt(delta * delta + 4 * (state.V12 * 35) ** 2) * 0.5;
          const y = cy + split;
          if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Upper Adiabatic State E₊ (Avoided Crossing Minimum Gap = 2V₁₂ = ${(2*state.V12).toFixed(2)} a.u.)`, left + 20, 50);
        ctx.fillStyle = "#f472b6";
        ctx.fillText("Lower Adiabatic State E₋ (Level Repulsion Prevents Crossing)", left + 20, 68);
      }

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 6: sim_qc_helium_h2_molecule_potential (Unit 6)
     Helium Atom Screening & H2+ / H2 Molecular Bonding Potential Curves
     ========================================================================= */
  function sim_qc_helium_h2_molecule_potential(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Helium Screening & H₂ / H₂⁺ Molecular Potential Curves</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 6: Many-Electron Atoms & Chemical Bonding</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="qc6_btn_model" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Model: H₂⁺ & H₂ Curves</button>
            <button id="qc6_btn_orb" style="background:#1e293b; color:#34d399; border:1px solid #34d399; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Show: σ_g vs σ_u*</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc6_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Internuclear Separation R: <span id="qc6_R_val" style="color:#38bdf8; font-weight:600;">1.40 a₀</span></label>
            <input type="range" id="qc6_R" min="0.6" max="5.0" value="1.4" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Helium Effective Charge Z_eff: <span id="qc6_Zeff_val" style="color:#f472b6; font-weight:600;">1.69</span></label>
            <input type="range" id="qc6_Zeff" min="1.0" max="2.0" value="1.69" step="0.02" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Overlap Integral S(R): <span id="qc6_S_val" style="color:#fbbf24; font-weight:600;">0.753</span></label>
            <input type="range" id="qc6_S" min="0.0" max="1.0" value="0.75" step="0.05" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc6_canvas");
    let state = { R: 1.4, Zeff: 1.69, mode: "curves", t: 0 };
    let animId = null;

    document.getElementById("qc6_R").oninput = (e) => {
      state.R = parseFloat(e.target.value);
      document.getElementById("qc6_R_val").innerText = `${state.R.toFixed(2)} a₀`;
    };
    document.getElementById("qc6_Zeff").oninput = (e) => {
      state.Zeff = parseFloat(e.target.value);
      document.getElementById("qc6_Zeff_val").innerText = state.Zeff.toFixed(2);
    };

    const modelBtn = document.getElementById("qc6_btn_model");
    modelBtn.onclick = () => {
      state.mode = state.mode === "curves" ? "orbitals" : "curves";
      modelBtn.innerText = state.mode === "curves" ? "Model: H₂⁺ & H₂ Curves" : "Model: Electron Density Cross-Section";
    };

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.03;

      if (state.mode === "curves") {
        const left = 60, right = W - 40, base = H * 0.65;
        const plotW = right - left;

        // Axes
        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, H - 30); ctx.lineTo(right, H - 30); ctx.stroke();

        // Zero energy dissociation line
        ctx.strokeStyle = "#334155"; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(left, base); ctx.lineTo(right, base); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#64748b"; ctx.font = "10px sans-serif";
        ctx.fillText("Dissociation Limit (H + H⁺)", right - 160, base - 6);

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Internuclear Distance R (Bohr radii a₀)", W / 2 - 60, H - 10);

        // Bonding Curve E_g (sigma_g)
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        let minEg = 999, rMin = 2.0;
        for (let x = left; x <= right; x++) {
          const r = 0.6 + ((x - left) / plotW) * 4.4;
          // Approximate H2+ bonding curve
          const D = 0.1026; // a.u.
          const a = 0.72;
          const re = 2.0;
          const morse = D * ((1 - Math.exp(-a * (r - re))) ** 2 - 1);
          const y = base + morse * 800;
          if (morse < minEg) { minEg = morse; rMin = r; }
          if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Antibonding Curve E_u (sigma_u*)
        ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const r = 0.6 + ((x - left) / plotW) * 4.4;
          const anti = 0.15 * Math.exp(-1.1 * (r - 0.6));
          const y = base - anti * 800;
          if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Marker for current R
        const curX = left + ((state.R - 0.6) / 4.4) * plotW;
        ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 1.5; ctx.setLineDash([2, 2]);
        ctx.beginPath(); ctx.moveTo(curX, 30); ctx.lineTo(curX, H - 30); ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("— Bonding Molecular Orbital σ_g (Potential Energy Well with Stable Minimum)", left + 20, 50);
        ctx.fillStyle = "#ef4444";
        ctx.fillText("— Antibonding Molecular Orbital σ_u* (Purely Repulsive, Nodal Plane Between Nuclei)", left + 20, 68);
        ctx.fillStyle = "#fbbf24";
        ctx.fillText(`H₂⁺ Equilibrium Distance R_e = 2.00 a₀ (1.06 Å) | Dissociation Energy D_e = 2.79 eV`, left + 20, 86);

      } else {
        // Mode: Molecular orbital contours
        const cx = W / 2, cy = H / 2;
        const dNuclei = state.R * 40;

        // Two Nuclei (protons)
        ctx.fillStyle = "#f472b6";
        ctx.beginPath(); ctx.arc(cx - dNuclei / 2, cy, 7, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.arc(cx + dNuclei / 2, cy, 7, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = "#fff"; ctx.font = "bold 9px sans-serif";
        ctx.fillText("H+", cx - dNuclei / 2 - 6, cy + 3);
        ctx.fillText("H+", cx + dNuclei / 2 - 6, cy + 3);

        // Electron density cloud in between (bonding)
        const grad = ctx.createRadialGradient(cx, cy, 5, cx, cy, dNuclei * 1.2);
        grad.addColorStop(0, "rgba(56, 189, 248, 0.6)");
        grad.addColorStop(0.5, "rgba(56, 189, 248, 0.2)");
        grad.addColorStop(1, "rgba(56, 189, 248, 0.0)");
        ctx.fillStyle = grad;
        ctx.beginPath(); ctx.ellipse(cx, cy, dNuclei * 1.3, 50, 0, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Bonding Charge Accumulation in Internuclear Region (Lowers Potential Energy)", 40, 40);
        ctx.fillStyle = "#fbbf24";
        ctx.fillText(`Helium Variational Ground State: Z_eff = 27/16 = 1.6875 ⇒ E = -77.5 eV (Exp: -79.0 eV)`, 40, 60);
      }

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 7: sim_qc_maxwell_boltzmann_microstates (Unit 7)
     Microstates Energy Level Population & Canonical Distribution
     ========================================================================= */
  function sim_qc_maxwell_boltzmann_microstates(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Microstates & Maxwell-Boltzmann Distribution</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 7: Statistical Ensembles & Lagrange Multipliers</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="qc7_btn_equil" style="background:#1e293b; color:#34d399; border:1px solid #34d399; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Equilibrate Ensembles</button>
            <button id="qc7_btn_reset" style="background:#1e293b; color:#94a3b8; border:1px solid #475569; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Reset</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc7_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Temperature T: <span id="qc7_T_val" style="color:#38bdf8; font-weight:600;">300 K</span></label>
            <input type="range" id="qc7_T" min="50" max="1000" value="300" step="25" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Energy Level Spacing Δε: <span id="qc7_eps_val" style="color:#f472b6; font-weight:600;">1.0 k_B·T₀</span></label>
            <input type="range" id="qc7_eps" min="0.5" max="3.0" value="1.0" step="0.2" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Total Particles N: <span id="qc7_N_val" style="color:#34d399; font-weight:600;">600</span></label>
            <input type="range" id="qc7_N" min="200" max="1000" value="600" step="50" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc7_canvas");
    let state = { T: 300, eps: 1.0, N: 600, t: 0 };
    let animId = null;

    document.getElementById("qc7_T").oninput = (e) => {
      state.T = parseInt(e.target.value);
      document.getElementById("qc7_T_val").innerText = `${state.T} K`;
    };
    document.getElementById("qc7_eps").oninput = (e) => {
      state.eps = parseFloat(e.target.value);
      document.getElementById("qc7_eps_val").innerText = `${state.eps.toFixed(1)} k_B·T₀`;
    };
    document.getElementById("qc7_N").oninput = (e) => {
      state.N = parseInt(e.target.value);
      document.getElementById("qc7_N_val").innerText = state.N;
    };

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.05;

      const levels = 8;
      const beta = state.eps / (state.T / 300);

      // Calculate partition function q = sum exp(-beta * i)
      let q = 0;
      for (let i = 0; i < levels; i++) q += Math.exp(-beta * i);

      const base = H * 0.85;
      const left = 60;
      const barW = (W - 120) / levels;

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, base); ctx.lineTo(W - 40, base); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Energy State ε_i (i · Δε)", W / 2 - 50, base + 25);
      ctx.fillText("Occupancy N_i", 15, 35);

      // Draw bars and Boltzmann exponential fit
      ctx.strokeStyle = "#f472b6"; ctx.lineWidth = 2.5;
      ctx.beginPath();

      for (let i = 0; i < levels; i++) {
        const prob = Math.exp(-beta * i) / q;
        const Ni = prob * state.N;
        const barH = (Ni / state.N) * 220;

        const bx = left + i * barW + 10;
        const bw = barW - 20;
        const by = base - barH;

        // Fluctuation effect
        const fluc = (Math.sin(state.t + i * 2) * 2);

        // Bar
        ctx.fillStyle = "rgba(56, 189, 248, 0.4)";
        ctx.fillRect(bx, by + fluc, bw, barH - fluc);
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
        ctx.strokeRect(bx, by + fluc, bw, barH - fluc);

        // Bar labels
        ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
        ctx.fillText(`ε_${i}`, bx + bw / 2 - 8, base + 14);
        ctx.fillStyle = "#38bdf8";
        ctx.fillText(`${Ni.toFixed(0)}`, bx + bw / 2 - 10, by - 5);

        // Fit curve line
        const cx = bx + bw / 2;
        if (i === 0) ctx.moveTo(cx, by); else ctx.lineTo(cx, by);
      }
      ctx.stroke();

      // Thermodynamic entropy S = k_B ln W calculation
      const S = (state.N * (1 / (state.T / 300) + Math.log(q))).toFixed(1);

      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Maxwell-Boltzmann Distribution: N_i = (N / q) exp(-β ε_i) | β = 1 / (k_B T)`, left + 10, 45);
      ctx.fillStyle = "#fbbf24";
      ctx.fillText(`Partition Function q = ${q.toFixed(2)} | Thermodynamic Entropy S / k_B = ${S}`, left + 10, 63);

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 8: sim_qc_molecular_partition_functions (Unit 8)
     Translational, Rotational, Vibrational Partition Functions & Bridge to U, S
     ========================================================================= */
  function sim_qc_molecular_partition_functions(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Molecular Partition Functions & Thermodynamic Bridge</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 8: q_trans, q_rot, q_vib & Properties (U, S, C_v)</span>
          </div>
          <div style="display:flex; gap:6px;">
            <select id="qc8_gas_sel" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 8px; border-radius:4px; font-size:0.75rem; cursor:pointer;">
              <option value="N2">Nitrogen N₂ (θ_rot=2.88 K, θ_vib=3374 K)</option>
              <option value="O2">Oxygen O₂ (θ_rot=2.07 K, θ_vib=2256 K)</option>
              <option value="HCl">Hydrogen Chloride HCl (θ_rot=15.0 K, θ_vib=4227 K)</option>
              <option value="I2">Iodine I₂ (θ_rot=0.05 K, θ_vib=308 K)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc8_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Temperature T: <span id="qc8_T_val" style="color:#38bdf8; font-weight:600;">500 K</span></label>
            <input type="range" id="qc8_T" min="20" max="2500" value="500" step="20" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Display Target: <span id="qc8_prop_val" style="color:#f472b6; font-weight:600;">Heat Capacity C_v(T)</span></label>
            <input type="range" id="qc8_prop" min="1" max="3" value="1" step="1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Pressure P: <span id="qc8_P_val" style="color:#34d399; font-weight:600;">1.0 bar</span></label>
            <input type="range" id="qc8_P" min="0.1" max="5.0" value="1.0" step="0.1" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc8_canvas");
    let state = { gas: "N2", T: 500, prop: 1, P: 1.0, t: 0 };
    let animId = null;

    const gasParams = {
      N2: { thetaRot: 2.88, thetaVib: 3374, sigma: 2 },
      O2: { thetaRot: 2.07, thetaVib: 2256, sigma: 2 },
      HCl: { thetaRot: 15.0, thetaVib: 4227, sigma: 1 },
      I2: { thetaRot: 0.05, thetaVib: 308, sigma: 2 }
    };

    document.getElementById("qc8_gas_sel").onchange = (e) => {
      state.gas = e.target.value;
    };
    document.getElementById("qc8_T").oninput = (e) => {
      state.T = parseInt(e.target.value);
      document.getElementById("qc8_T_val").innerText = `${state.T} K`;
    };
    document.getElementById("qc8_prop").oninput = (e) => {
      state.prop = parseInt(e.target.value);
      const labels = ["Heat Capacity C_v(T)", "Internal Energy U(T)", "Entropy S(T)"];
      document.getElementById("qc8_prop_val").innerText = labels[state.prop - 1];
    };

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.03;

      const p = gasParams[state.gas];
      const left = 60, right = W - 40, base = H * 0.8;
      const plotW = right - left;

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, base); ctx.lineTo(right, base); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Temperature T (K)", W / 2 - 40, base + 25);

      // Plot Heat Capacity C_v(T) curve from 0 to 2500 K
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();

      // Asymptotic limits: 3/2 R (trans) -> 5/2 R (trans + rot) -> 7/2 R (trans + rot + vib)
      const R = 8.314;
      for (let x = left; x <= right; x++) {
        const temp = 5 + ((x - left) / plotW) * 2500;
        const cTrans = 1.5 * R;
        const cRot = (temp < p.thetaRot * 0.5) ? 0 : 1.0 * R;
        const xVib = p.thetaVib / temp;
        const expV = Math.exp(xVib);
        const cVib = (expV > 1e4) ? 0 : R * (xVib * xVib * expV) / ((expV - 1) ** 2);
        const cTotal = (cTrans + cRot + cVib) / R; // in units of R

        const y = base - (cTotal / 4.0) * (base - 60);
        if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Equipartition Classical Limit Guide Lines
      const y32 = base - (1.5 / 4.0) * (base - 60);
      const y52 = base - (2.5 / 4.0) * (base - 60);
      const y72 = base - (3.5 / 4.0) * (base - 60);

      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(left, y32); ctx.lineTo(right, y32); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(left, y52); ctx.lineTo(right, y52); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(left, y72); ctx.lineTo(right, y72); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#64748b"; ctx.font = "10px sans-serif";
      ctx.fillText("3/2 R (Trans Only)", right - 95, y32 - 4);
      ctx.fillText("5/2 R (Trans + Rot)", right - 100, y52 - 4);
      ctx.fillText("7/2 R (Equipartition High-T)", right - 130, y72 - 4);

      // Marker for current T
      const curX = left + ((state.T - 5) / 2500) * plotW;
      const xVib = p.thetaVib / state.T;
      const expV = Math.exp(xVib);
      const cVibCur = (expV > 1e4) ? 0 : (xVib * xVib * expV) / ((expV - 1) ** 2);
      const curCv = 1.5 + (state.T < p.thetaRot ? 0 : 1.0) + cVibCur;
      const curY = base - (curCv / 4.0) * (base - 60);

      ctx.fillStyle = "#fbbf24";
      ctx.beginPath(); ctx.arc(curX, curY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`C_v = ${curCv.toFixed(2)} R`, curX + 8, curY - 6);

      // Info header
      const qRot = (state.T / (p.sigma * p.thetaRot)).toFixed(1);
      const qVib = (1 / (1 - Math.exp(-p.thetaVib / state.T))).toFixed(3);

      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Diatomic ${state.gas}: q_rot = T / (σ θ_rot) = ${qRot} | q_vib = (1 - e^(-θ_vib/T))⁻¹ = ${qVib}`, left + 10, 45);
      ctx.fillStyle = "#34d399";
      ctx.fillText(`Quantum Freezing: Rotations Freeze Out at T ≪ θ_rot | Vibrations Inactive Until T ~ θ_vib`, left + 10, 63);

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 9: sim_qc_chemical_equilibrium_stat_mech (Unit 9)
     Equilibrium Constant K_p(T) from Molecular Partition Functions
     ========================================================================= */
  function sim_qc_chemical_equilibrium_stat_mech(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Statistical Equilibrium Constant K_p(T)</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 9: Diatomic Dissociation & Gas Reactions</span>
          </div>
          <div style="display:flex; gap:6px;">
            <select id="qc9_rxn_sel" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 8px; border-radius:4px; font-size:0.75rem; cursor:pointer;">
              <option value="I2">I₂ (g) ⇌ 2 I (g) [D₀ = 149 kJ/mol]</option>
              <option value="H2_I2">H₂ + I₂ ⇌ 2 HI [ΔE₀ = -9.6 kJ/mol]</option>
              <option value="N2_3H2">N₂ + 3H₂ ⇌ 2 NH₃ [ΔE₀ = -92 kJ/mol]</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc9_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Reaction Temperature T: <span id="qc9_T_val" style="color:#38bdf8; font-weight:600;">800 K</span></label>
            <input type="range" id="qc9_T" min="300" max="1800" value="800" step="50" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Total Pressure P: <span id="qc9_P_val" style="color:#f472b6; font-weight:600;">1.0 atm</span></label>
            <input type="range" id="qc9_P" min="0.2" max="5.0" value="1.0" step="0.2" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Dissociation Energy ΔE₀: <span id="qc9_dE_val" style="color:#34d399; font-weight:600;">149 kJ/mol</span></label>
            <input type="range" id="qc9_dE" min="50" max="250" value="149" step="5" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc9_canvas");
    let state = { rxn: "I2", T: 800, P: 1.0, dE: 149, t: 0 };
    let animId = null;

    document.getElementById("qc9_rxn_sel").onchange = (e) => {
      state.rxn = e.target.value;
      if (state.rxn === "I2") state.dE = 149;
      if (state.rxn === "H2_I2") state.dE = -9.6;
      if (state.rxn === "N2_3H2") state.dE = -92;
      document.getElementById("qc9_dE_val").innerText = `${state.dE} kJ/mol`;
    };
    document.getElementById("qc9_T").oninput = (e) => {
      state.T = parseInt(e.target.value);
      document.getElementById("qc9_T_val").innerText = `${state.T} K`;
    };
    document.getElementById("qc9_P").oninput = (e) => {
      state.P = parseFloat(e.target.value);
      document.getElementById("qc9_P_val").innerText = `${state.P.toFixed(1)} atm`;
    };
    document.getElementById("qc9_dE").oninput = (e) => {
      state.dE = parseFloat(e.target.value);
      document.getElementById("qc9_dE_val").innerText = `${state.dE} kJ/mol`;
    };

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.03;

      const left = 60, right = W - 40, base = H * 0.8;
      const plotW = right - left;

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, base); ctx.lineTo(right, base); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Temperature T (K)", W / 2 - 40, base + 25);
      ctx.fillText("ln(K_p)", 20, 40);

      // Plot ln(K_p) vs T (van 't Hoff type curve)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();

      const R_kJ = 8.314e-3;
      let curLnKp = 0;

      for (let x = left; x <= right; x++) {
        const temp = 300 + ((x - left) / plotW) * 1500;
        // K_p = (q_prod/V) / (q_react/V) * exp(-dE / RT)
        const dS_est = 0.11; // kJ/mol K approx entropy
        const lnKp = (dS_est / R_kJ) - (state.dE / (R_kJ * temp));
        const yNorm = (lnKp + 20) / 40; // map ln Kp from -20 to +20
        const y = Math.max(30, Math.min(base, base - yNorm * (base - 60)));

        if (Math.abs(temp - state.T) < 10) curLnKp = lnKp;
        if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Current Marker
      const curX = left + ((state.T - 300) / 1500) * plotW;
      const curYNorm = (curLnKp + 20) / 40;
      const curY = Math.max(30, Math.min(base, base - curYNorm * (base - 60)));

      ctx.fillStyle = "#fbbf24";
      ctx.beginPath(); ctx.arc(curX, curY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`ln K_p = ${curLnKp.toFixed(2)} (K_p = ${Math.exp(Math.min(10, curLnKp)).toExponential(2)})`, curX + 10, curY - 8);

      // Gas reaction breakdown
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Statistical K_p(T) = ∏ (q_j / V)^ν_j · exp(-ΔE₀ / k_B T) · (k_B T)^(-Δν)`, left + 10, 45);
      ctx.fillStyle = "#34d399";
      ctx.fillText(`Translational, Rotational & Vibrational Degrees of Freedom Drive Thermodynamic Equilibrium`, left + 10, 63);

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 10: sim_qc_fermi_bose_debye_heat_capacity (Unit 10)
     Fermi-Dirac vs Bose-Einstein Statistics & Einstein/Debye Solid Heat Capacity
     ========================================================================= */
  function sim_qc_fermi_bose_debye_heat_capacity(container) {
    container = getContainerEl(container);
    if (!container) return;

    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Fermi-Dirac, Bose-Einstein & Debye Solid C_v(T)</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 10: Quantum Statistics & Solids</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="qc10_btn_mode" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Mode: Quantum Distributions</button>
            <select id="qc10_solid_sel" style="background:#1e293b; color:#34d399; border:1px solid #34d399; padding:4px 8px; border-radius:4px; font-size:0.75rem; cursor:pointer;">
              <option value="diamond">Diamond (θ_D = 2230 K)</option>
              <option value="copper">Copper (θ_D = 343 K)</option>
              <option value="lead">Lead (θ_D = 105 K)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="qc10_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Reduced Temperature T / T_F (or T / θ_D): <span id="qc10_T_val" style="color:#38bdf8; font-weight:600;">0.20</span></label>
            <input type="range" id="qc10_T" min="0.01" max="1.5" value="0.2" step="0.02" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Fermi Energy E_F: <span id="qc10_EF_val" style="color:#f472b6; font-weight:600;">5.0 eV</span></label>
            <input type="range" id="qc10_EF" min="2.0" max="10.0" value="5.0" step="0.5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Phonon Velocity Scaling: <span id="qc10_c_val" style="color:#34d399; font-weight:600;">1.0 a.u.</span></label>
            <input type="range" id="qc10_c" min="0.5" max="2.0" value="1.0" step="0.1" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("qc10_canvas");
    let state = { mode: "dist", tRed: 0.2, EF: 5.0, solid: "copper", t: 0 };
    let animId = null;

    document.getElementById("qc10_T").oninput = (e) => {
      state.tRed = parseFloat(e.target.value);
      document.getElementById("qc10_T_val").innerText = state.tRed.toFixed(2);
    };
    document.getElementById("qc10_EF").oninput = (e) => {
      state.EF = parseFloat(e.target.value);
      document.getElementById("qc10_EF_val").innerText = `${state.EF.toFixed(1)} eV`;
    };

    const modeBtn = document.getElementById("qc10_btn_mode");
    modeBtn.onclick = () => {
      state.mode = state.mode === "dist" ? "solid" : "dist";
      modeBtn.innerText = state.mode === "dist" ? "Mode: Quantum Distributions" : "Mode: Solid Heat Capacity (Debye vs Einstein)";
    };

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);
      state.t += 0.03;

      if (state.mode === "dist") {
        // Plot Fermi-Dirac vs Bose-Einstein vs Maxwell-Boltzmann
        const left = 60, right = W - 40, base = H * 0.8;
        const plotW = right - left;

        // Axes
        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, base); ctx.lineTo(right, base); ctx.stroke();

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Energy E / E_F", W / 2 - 30, base + 25);
        ctx.fillText("Occupancy f(E)", 15, 35);

        // Fermi level vertical guide
        const xEF = left + (1.0 / 2.5) * plotW;
        ctx.strokeStyle = "#64748b"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(xEF, 30); ctx.lineTo(xEF, base); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillText("Fermi Energy E_F", xEF - 35, base - 10);

        // 1. Fermi-Dirac: f_FD(E) = 1 / [exp((E - E_F) / kT) + 1]
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const eNorm = ((x - left) / plotW) * 2.5;
          const arg = (eNorm - 1.0) / state.tRed;
          const fFD = 1.0 / (Math.exp(Math.max(-50, Math.min(50, arg))) + 1.0);
          const y = base - fFD * 180;
          if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // 2. Bose-Einstein: f_BE(E) = 1 / [exp(E / kT) - 1] (with chem pot mu=0)
        ctx.strokeStyle = "#f472b6"; ctx.lineWidth = 2.0; ctx.setLineDash([4, 2]);
        ctx.beginPath();
        for (let x = left + 5; x <= right; x++) {
          const eNorm = ((x - left) / plotW) * 2.5;
          const arg = (eNorm - 0.05) / state.tRed;
          if (arg <= 0) continue;
          const fBE = Math.min(2.0, 1.0 / (Math.exp(arg) - 1.0));
          const y = base - Math.min(1.2, fBE) * 180;
          if (x === left + 5) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // 3. Maxwell-Boltzmann classical tail
        ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 1.5; ctx.setLineDash([2, 2]);
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const eNorm = ((x - left) / plotW) * 2.5;
          const fMB = Math.exp(-(eNorm - 1.0) / state.tRed);
          const y = base - Math.min(1.2, fMB) * 180;
          if (x === left) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("— Fermi-Dirac f_FD (Fermions, Half-Integer Spin, Pauli Exclusion)", left + 20, 50);
        ctx.fillStyle = "#f472b6";
        ctx.fillText("- - Bose-Einstein f_BE (Bosons, Integer Spin, BEC Condensation)", left + 20, 68);
        ctx.fillStyle = "#fbbf24";
        ctx.fillText("· · Maxwell-Boltzmann Limit (Classical High-T Tail)", left + 20, 86);

      } else {
        // Mode: Debye vs Einstein Heat Capacity of Solids
        const left = 60, right = W - 40, base = H * 0.8;
        const plotW = right - left;

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(left, 30); ctx.lineTo(left, base); ctx.lineTo(right, base); ctx.stroke();

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Reduced Temperature T / θ_D", W / 2 - 40, base + 25);
        ctx.fillText("Heat Capacity C_v / (3R)", 15, 35);

        // Dulong-Petit Classical Law 3R Line
        const y3R = base - 1.0 * 180;
        ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(left, y3R); ctx.lineTo(right, y3R); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#ef4444"; ctx.fillText("Dulong-Petit Classical Law (C_v = 3R)", right - 190, y3R - 6);

        // Debye Model Curve C_v(T) -> T^3 at low T, asymptotes to 3R
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const tRat = ((x - left) / plotW) * 1.5;
          // Approximate Debye function interpolation
          let cvD = 0;
          if (tRat < 0.1) {
            cvD = (12 * Math.PI ** 4 / 5) * (tRat ** 3);
          } else {
            cvD = 1.0 - (1.0 / (1 + 8 * (tRat ** 2.2)));
          }
          cvD = Math.min(1.0, cvD);
          const y = base - cvD * 180;
          if (x === left) ctx.moveTo(x, base); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Einstein Model Curve C_v(T) -> exp(-theta/T) exponential freeze
        ctx.strokeStyle = "#f472b6"; ctx.lineWidth = 2.0; ctx.setLineDash([3, 3]);
        ctx.beginPath();
        for (let x = left; x <= right; x++) {
          const tRat = ((x - left) / plotW) * 1.5;
          const xE = 0.75 / (tRat + 0.001);
          const expE = Math.exp(Math.min(30, xE));
          const cvE = (xE * xE * expE) / ((expE - 1) ** 2);
          const y = base - Math.min(1.0, cvE) * 180;
          if (x === left) ctx.moveTo(x, base); else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("— Debye Model: C_v ∝ T³ Law at Low Temperatures (Acoustic Phonon Modes)", left + 20, 50);
        ctx.fillStyle = "#f472b6";
        ctx.fillText("- - Einstein Model: Exponential Fall-Off (Single Optical Frequency)", left + 20, 68);
      }

      animId = requestAnimationFrame(render);
    }
    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  return {
    sim_qc_blackbody_compton_wavepacket,
    sim_qc_particle_box_ring_quantum,
    sim_qc_harmonic_oscillator_ladder,
    sim_qc_hydrogen_orbital_radial_prob,
    sim_qc_variational_perturbation_solver,
    sim_qc_helium_h2_molecule_potential,
    sim_qc_maxwell_boltzmann_microstates,
    sim_qc_molecular_partition_functions,
    sim_qc_chemical_equilibrium_stat_mech,
    sim_qc_fermi_bose_debye_heat_capacity
  };
})();

/* ==========================================================================
   Global Simulation Engine Registry Adapter
   ========================================================================== */
if (typeof window !== 'undefined') {
  window.SimulationEngine = window.SimulationEngine || {};
  Object.keys(window.QuantumChemistrySimulations).forEach(function(key) {
    window[key] = window.QuantumChemistrySimulations[key];
  });
  const originalInit = window.SimulationEngine.initSimulation;
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    const el = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    if (!el) return;
    if (window.QuantumChemistrySimulations && typeof window.QuantumChemistrySimulations[simType] === 'function') {
      return window.QuantumChemistrySimulations[simType](el);
    }
    if (typeof window[simType] === 'function') {
      return window[simType](el);
    }
    if (originalInit) {
      return originalInit(containerId, simType);
    }
    console.warn("Simulation not found:", simType);
  };
}
