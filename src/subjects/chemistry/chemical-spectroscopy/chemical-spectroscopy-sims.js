/**
 * chemical-spectroscopy-sims.js
 * 10 High-Performance 60 FPS Interactive HTML5 Canvas Simulation Engines
 * for Chemical Spectroscopy (OpenSTEM Milestone Textbook #51)
 */

window.SpectroscopySimulations = (function() {
  'use strict';

  // Helper for crisp high-DPI canvas rendering
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
     SIMULATION 1: sim_spec_electromagnetic_wave_fourier (Unit 1)
     EM Wave Superposition, Dipole Interaction & Live Michelson Interferogram FFT
     ========================================================================= */
  function sim_spec_electromagnetic_wave_fourier(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">EM Wave Superposition & Michelson Interferogram FFT</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 1: Transition Moments & FT Spectrometry</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="spec1_btn_fft" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Toggle FFT Spectrum</button>
            <button id="spec1_btn_reset" style="background:#1e293b; color:#94a3b8; border:1px solid #475569; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Reset</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec1_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Wave 1 Frequency $\\tilde{\\nu}_1$: <span id="spec1_nu1_val" style="color:#38bdf8; font-weight:600;">1200 cm⁻¹</span></label>
            <input type="range" id="spec1_nu1" min="600" max="2400" value="1200" step="50" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Wave 2 Frequency $\\tilde{\\nu}_2$: <span id="spec1_nu2_val" style="color:#f472b6; font-weight:600;">1600 cm⁻¹</span></label>
            <input type="range" id="spec1_nu2" min="600" max="2400" value="1600" step="50" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Interferometer Retardation Velocity: <span id="spec1_v_val" style="color:#34d399; font-weight:600;">1.0 mm/s</span></label>
            <input type="range" id="spec1_v" min="0.2" max="3.0" value="1.0" step="0.2" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec1_canvas");
    let state = { nu1: 1200, nu2: 1600, v: 1.0, showFFT: true, t: 0 };
    let animId = null;

    document.getElementById("spec1_nu1").oninput = (e) => {
      state.nu1 = parseFloat(e.target.value);
      document.getElementById("spec1_nu1_val").innerText = `${state.nu1} cm⁻¹`;
    };
    document.getElementById("spec1_nu2").oninput = (e) => {
      state.nu2 = parseFloat(e.target.value);
      document.getElementById("spec1_nu2_val").innerText = `${state.nu2} cm⁻¹`;
    };
    document.getElementById("spec1_v").oninput = (e) => {
      state.v = parseFloat(e.target.value);
      document.getElementById("spec1_v_val").innerText = `${state.v.toFixed(1)} mm/s`;
    };
    document.getElementById("spec1_btn_fft").onclick = () => {
      state.showFFT = !state.showFFT;
    };
    document.getElementById("spec1_btn_reset").onclick = () => {
      state.nu1 = 1200; state.nu2 = 1600; state.v = 1.0; state.t = 0; state.showFFT = true;
      document.getElementById("spec1_nu1").value = 1200;
      document.getElementById("spec1_nu2").value = 1600;
      document.getElementById("spec1_v").value = 1.0;
      document.getElementById("spec1_nu1_val").innerText = "1200 cm⁻¹";
      document.getElementById("spec1_nu2_val").innerText = "1600 cm⁻¹";
      document.getElementById("spec1_v_val").innerText = "1.0 mm/s";
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

      state.t += 0.02 * state.v;

      // Draw Grid
      ctx.strokeStyle = "rgba(255,255,255,0.06)";
      ctx.lineWidth = 1;
      for (let x = 0; x < W; x += 40) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
      for (let y = 0; y < H; y += 40) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      const splitH = state.showFFT ? H * 0.52 : H;

      // Top Panel: Michelson Interferometer Wave & Interferogram I(delta)
      ctx.fillStyle = "rgba(56, 189, 248, 0.9)";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Interferogram: I(δ) = I₁ cos(2π ν̃₁ δ) + I₂ cos(2π ν̃₂ δ)", 14, 20);

      const midY = splitH * 0.5;
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.beginPath();
      ctx.moveTo(40, midY);
      ctx.lineTo(W - 20, midY);
      ctx.stroke();

      // Waveform trace
      ctx.lineWidth = 2;
      ctx.beginPath();
      const k1 = state.nu1 * 0.005;
      const k2 = state.nu2 * 0.005;
      for (let x = 40; x < W - 20; x++) {
        const delta = (x - 40) * 0.04 - state.t;
        const amp = 0.5 * Math.cos(k1 * delta) + 0.5 * Math.cos(k2 * delta);
        const y = midY - amp * (splitH * 0.38);
        if (x === 40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.strokeStyle = "#38bdf8";
      ctx.stroke();

      // Oscillating molecular dipole at the right
      const probeX = W - 50;
      const probeDelta = (probeX - 40) * 0.04 - state.t;
      const probeAmp = 0.5 * Math.cos(k1 * probeDelta) + 0.5 * Math.cos(k2 * probeDelta);
      ctx.fillStyle = "#ec4899";
      ctx.beginPath();
      ctx.arc(probeX, midY - probeAmp * (splitH * 0.38), 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#94a3b8";
      ctx.fillText("Dipole μ(t)", probeX - 25, midY - probeAmp * (splitH * 0.38) - 10);

      // Bottom Panel: Fast Fourier Transform Power Spectrum S(nu)
      if (state.showFFT) {
        ctx.strokeStyle = "rgba(255,255,255,0.15)";
        ctx.beginPath();
        ctx.moveTo(10, splitH);
        ctx.lineTo(W - 10, splitH);
        ctx.stroke();

        ctx.fillStyle = "#34d399";
        ctx.fillText("FFT Recovered Spectrum: S(ν̃) = ℱ{I(δ)}", 14, splitH + 18);

        const specBaseY = H - 24;
        ctx.strokeStyle = "rgba(255,255,255,0.2)";
        ctx.beginPath();
        ctx.moveTo(40, specBaseY);
        ctx.lineTo(W - 20, specBaseY);
        ctx.stroke();

        // Frequency axis (600 to 2400 cm-1)
        const minNu = 600, maxNu = 2400;
        const nuToX = (nu) => 40 + ((nu - minNu) / (maxNu - minNu)) * (W - 80);

        // Peak 1 (Lorentzian line shape)
        ctx.fillStyle = "rgba(56, 189, 248, 0.3)";
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(40, specBaseY);
        for (let x = 40; x < W - 20; x++) {
          const nu = minNu + ((x - 40) / (W - 80)) * (maxNu - minNu);
          const l1 = 1 / (1 + Math.pow((nu - state.nu1) / 30, 2));
          const l2 = 1 / (1 + Math.pow((nu - state.nu2) / 30, 2));
          const height = (l1 + l2) * 0.85 * (H - splitH - 45);
          ctx.lineTo(x, specBaseY - height);
        }
        ctx.lineTo(W - 20, specBaseY);
        ctx.fill();
        ctx.stroke();

        // Peak labels
        ctx.fillStyle = "#38bdf8";
        ctx.fillText(`${state.nu1} cm⁻¹`, nuToX(state.nu1) - 20, specBaseY - (H - splitH - 40));
        ctx.fillStyle = "#f472b6";
        ctx.fillText(`${state.nu2} cm⁻¹`, nuToX(state.nu2) - 20, specBaseY - (H - splitH - 40));
      }

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 2: sim_spec_rotational_microwave_rotor (Unit 2)
     3D Rotating Dumbbell Rotor, Centrifugal Distortion & Stark Effect
     ========================================================================= */
  function sim_spec_rotational_microwave_rotor(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Rigid/Non-Rigid Rotor & Stark Splitting</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 2: Microwave Rotational Spectroscopy</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="spec2_btn_iso" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Isotope: ¹²C¹⁶O</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec2_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Rotational Constant $B$: <span id="spec2_b_val" style="color:#38bdf8; font-weight:600;">1.921 cm⁻¹</span></label>
            <input type="range" id="spec2_b" min="0.5" max="4.0" value="1.921" step="0.05" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Temperature $T$: <span id="spec2_t_val" style="color:#fbbf24; font-weight:600;">300 K</span></label>
            <input type="range" id="spec2_t" min="50" max="800" value="300" step="10" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Stark Electric Field $\\mathcal{E}$: <span id="spec2_e_val" style="color:#f472b6; font-weight:600;">0 kV/cm</span></label>
            <input type="range" id="spec2_e" min="0" max="15" value="0" step="1" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec2_canvas");
    let state = { B: 1.921, T: 300, E_field: 0, isotope: "12C16O", angle: 0 };
    let animId = null;

    document.getElementById("spec2_b").oninput = (e) => {
      state.B = parseFloat(e.target.value);
      document.getElementById("spec2_b_val").innerText = `${state.B.toFixed(3)} cm⁻¹`;
    };
    document.getElementById("spec2_t").oninput = (e) => {
      state.T = parseFloat(e.target.value);
      document.getElementById("spec2_t_val").innerText = `${state.T} K`;
    };
    document.getElementById("spec2_e").oninput = (e) => {
      state.E_field = parseFloat(e.target.value);
      document.getElementById("spec2_e_val").innerText = `${state.E_field} kV/cm`;
    };
    document.getElementById("spec2_btn_iso").onclick = (e) => {
      if (state.isotope === "12C16O") {
        state.isotope = "13C16O";
        state.B = 1.838;
        e.target.innerText = "Isotope: ¹³C¹⁶O";
      } else {
        state.isotope = "12C16O";
        state.B = 1.921;
        e.target.innerText = "Isotope: ¹²C¹⁶O";
      }
      document.getElementById("spec2_b").value = state.B;
      document.getElementById("spec2_b_val").innerText = `${state.B.toFixed(3)} cm⁻¹`;
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

      state.angle += 0.03 * Math.sqrt(state.B * (state.T / 300));

      // Left Panel: 3D Rotating Diatomic Molecule
      const molCenterX = W * 0.22;
      const molCenterY = H * 0.45;
      const bondLen = 65 + (state.T / 500) * 4; // slight centrifugal stretch

      const dx = Math.cos(state.angle) * (bondLen * 0.5);
      const dy = Math.sin(state.angle) * (bondLen * 0.5);

      // Bond cylinder
      ctx.strokeStyle = "#64748b";
      ctx.lineWidth = 6;
      ctx.beginPath();
      ctx.moveTo(molCenterX - dx, molCenterY - dy);
      ctx.lineTo(molCenterX + dx, molCenterY + dy);
      ctx.stroke();

      // Atom 1 (Carbon)
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(molCenterX - dx, molCenterY - dy, 16, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#0f172a";
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(state.isotope.startsWith("13") ? "¹³C" : "¹²C", molCenterX - dx - 9, molCenterY - dy + 4);

      // Atom 2 (Oxygen)
      ctx.fillStyle = "#ef4444";
      ctx.beginPath();
      ctx.arc(molCenterX + dx, molCenterY + dy, 18, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.fillText("¹⁶O", molCenterX + dx - 9, molCenterY + dy + 4);

      // Dipole vector arrow
      ctx.strokeStyle = "#fbbf24";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(molCenterX - dx * 0.6, molCenterY - dy * 0.6 - 22);
      ctx.lineTo(molCenterX + dx * 0.6, molCenterY + dy * 0.6 - 22);
      ctx.stroke();
      ctx.fillStyle = "#fbbf24";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText("μ₀ = 0.11 D", molCenterX - 25, molCenterY - 35);

      // Right Panel: Rotational Energy Ladder & Microwave Stick Spectrum
      const specLeft = W * 0.44;
      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Rotational Stick Spectrum & Stark Shifts (${state.isotope})`, specLeft, 22);

      const baselineY = H * 0.85;
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(specLeft, baselineY);
      ctx.lineTo(W - 20, baselineY);
      ctx.stroke();

      // Draw transition lines J -> J+1 (frequency nu = 2B(J+1))
      const maxJ = 12;
      const kB_T_hc = 0.695 * state.T; // cm-1
      const J_max = Math.sqrt(kB_T_hc / (2 * state.B)) - 0.5;

      for (let J = 0; J <= maxJ; J++) {
        const nu = 2 * state.B * (J + 1);
        const x = specLeft + ((nu) / (2 * state.B * (maxJ + 2))) * (W - specLeft - 30);
        // Intensity via Boltzmann factor: (2J+1) * exp(-B J(J+1) / kT)
        const EJ = state.B * J * (J + 1);
        const pop = (2 * J + 1) * Math.exp(-EJ / kB_T_hc);
        const intensity = (pop / ((2 * Math.floor(J_max) + 1) * Math.exp(-state.B * J_max * (J_max + 1) / kB_T_hc))) * (H * 0.55);

        // Stark splitting: if E_field > 0, split into components
        if (state.E_field > 0) {
          const splitCount = J + 1;
          for (let m = -J; m <= J; m++) {
            const shift = (state.E_field * 0.4) * (m / (J === 0 ? 1 : J));
            ctx.strokeStyle = "#f472b6";
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(x + shift, baselineY);
            ctx.lineTo(x + shift, baselineY - intensity / (2 * J + 1));
            ctx.stroke();
          }
        } else {
          ctx.strokeStyle = J === Math.round(J_max) ? "#fbbf24" : "#38bdf8";
          ctx.lineWidth = 2.5;
          ctx.beginPath();
          ctx.moveTo(x, baselineY);
          ctx.lineTo(x, baselineY - intensity);
          ctx.stroke();
        }

        // Labels for selected J
        if (J % 2 === 0) {
          ctx.fillStyle = "#94a3b8";
          ctx.font = "9px Inter, sans-serif";
          ctx.fillText(`J=${J}`, x - 8, baselineY + 14);
        }
      }

      ctx.fillStyle = "#fbbf24";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText(`Peak J_max ≈ ${Math.round(J_max)} | 2B spacing = ${(2 * state.B).toFixed(2)} cm⁻¹`, specLeft, H * 0.95);

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 3: sim_spec_rovibrational_co_spectrum (Unit 3)
     CO Rovibrational P & R Branches with Vibration-Rotation Interaction α_e
     ========================================================================= */
  function sim_spec_rovibrational_co_spectrum(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">CO Rovibrational Spectrum (P & R Branches)</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 3: Vibrational-Rotational Coupling</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="spec3_btn_alpha" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Toggle αₑ Coupling</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec3_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Temperature $T$: <span id="spec3_t_val" style="color:#fbbf24; font-weight:600;">300 K</span></label>
            <input type="range" id="spec3_t" min="100" max="1000" value="300" step="25" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Coupling $\\alpha_e$: <span id="spec3_a_val" style="color:#38bdf8; font-weight:600;">0.0175 cm⁻¹</span></label>
            <input type="range" id="spec3_a" min="0" max="0.05" value="0.0175" step="0.0025" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Band Origin $\\tilde{\\nu}_0$: <span id="spec3_nu0_val" style="color:#34d399; font-weight:600;">2143.2 cm⁻¹</span></label>
            <input type="range" id="spec3_nu0" min="2000" max="2300" value="2143.2" step="5" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec3_canvas");
    let state = { T: 300, alpha_e: 0.0175, nu0: 2143.2, Be: 1.931, withAlpha: true };
    let animId = null;

    document.getElementById("spec3_t").oninput = (e) => {
      state.T = parseFloat(e.target.value);
      document.getElementById("spec3_t_val").innerText = `${state.T} K`;
    };
    document.getElementById("spec3_a").oninput = (e) => {
      state.alpha_e = parseFloat(e.target.value);
      document.getElementById("spec3_a_val").innerText = `${state.alpha_e.toFixed(4)} cm⁻¹`;
    };
    document.getElementById("spec3_nu0").oninput = (e) => {
      state.nu0 = parseFloat(e.target.value);
      document.getElementById("spec3_nu0_val").innerText = `${state.nu0.toFixed(1)} cm⁻¹`;
    };
    document.getElementById("spec3_btn_alpha").onclick = () => {
      state.withAlpha = !state.withAlpha;
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

      const B0 = state.Be - 0.5 * (state.withAlpha ? state.alpha_e : 0);
      const B1 = state.Be - 1.5 * (state.withAlpha ? state.alpha_e : 0);

      // Top info
      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Carbon Monoxide ¹²C¹⁶O Fundamental Band (v=0 → 1) | Band Origin ν̃₀ = ${state.nu0.toFixed(1)} cm⁻¹`, 14, 20);

      const baselineY = H * 0.8;
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.beginPath();
      ctx.moveTo(30, baselineY);
      ctx.lineTo(W - 30, baselineY);
      ctx.stroke();

      const span = 160; // wavenumbers around nu0
      const nuToX = (nu) => 30 + ((nu - (state.nu0 - span)) / (2 * span)) * (W - 60);

      // Missing Q-branch indicator (Delta J = 0 forbidden for 1Sigma+ -> 1Sigma+)
      const qX = nuToX(state.nu0);
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = "rgba(239, 68, 68, 0.6)";
      ctx.beginPath();
      ctx.moveTo(qX, baselineY);
      ctx.lineTo(qX, baselineY - H * 0.5);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Q-branch (Forbidden ΔJ=0)", qX - 55, baselineY - H * 0.53);

      const kB_T_hc = 0.695 * state.T;

      // P-branch: Delta J = -1 (J'' -> J''-1, nu = nu0 - (B1+B0)J'' + (B1-B0)J''^2)
      // R-branch: Delta J = +1 (J'' -> J''+1, nu = nu0 + 2B1 + (3B1-B0)J'' + (B1-B0)J''^2)
      for (let J = 1; J <= 22; J++) {
        const pop = (2 * J + 1) * Math.exp(-B0 * J * (J + 1) / kB_T_hc);
        const height = (pop / 8) * (H * 0.48);

        // P-branch line
        const nuP = state.nu0 - (B1 + B0) * J + (B1 - B0) * J * J;
        const xP = nuToX(nuP);
        if (xP >= 30 && xP <= W - 30) {
          ctx.strokeStyle = "#38bdf8";
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.moveTo(xP, baselineY);
          ctx.lineTo(xP, baselineY - height);
          ctx.stroke();
          if (J % 3 === 0) {
            ctx.fillStyle = "#94a3b8";
            ctx.font = "9px Inter, sans-serif";
            ctx.fillText(`P(${J})`, xP - 10, baselineY + 14);
          }
        }

        // R-branch line (from J'' = J-1)
        const J_init = J - 1;
        const popR = (2 * J_init + 1) * Math.exp(-B0 * J_init * (J_init + 1) / kB_T_hc);
        const heightR = (popR / 8) * (H * 0.48);
        const nuR = state.nu0 + 2 * B1 + (3 * B1 - B0) * J_init + (B1 - B0) * J_init * J_init;
        const xR = nuToX(nuR);
        if (xR >= 30 && xR <= W - 30) {
          ctx.strokeStyle = "#34d399";
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.moveTo(xR, baselineY);
          ctx.lineTo(xR, baselineY - heightR);
          ctx.stroke();
          if (J_init % 3 === 0) {
            ctx.fillStyle = "#94a3b8";
            ctx.font = "9px Inter, sans-serif";
            ctx.fillText(`R(${J_init})`, xR - 10, baselineY + 14);
          }
        }
      }

      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("← P-Branch (ΔJ = -1)", 40, baselineY - H * 0.55);
      ctx.fillStyle = "#34d399";
      ctx.fillText("R-Branch (ΔJ = +1) →", W - 160, baselineY - H * 0.55);

      if (state.withAlpha) {
        ctx.fillStyle = "#fbbf24";
        ctx.font = "10px Inter, sans-serif";
        ctx.fillText(`αₑ = ${state.alpha_e.toFixed(4)} cm⁻¹ causes R-branch lines to converge and P-branch to diverge!`, W * 0.25, H * 0.95);
      }

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 4: sim_spec_raman_polarizability_ellipsoid (Unit 4)
     Polarizability Ellipsoid Vibration, Stokes & Anti-Stokes Raman Scattering
     ========================================================================= */
  function sim_spec_raman_polarizability_ellipsoid(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Raman Scattering & Polarizability Ellipsoid</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 4: Stokes, Anti-Stokes & Selection Rules</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="spec4_btn_laser" style="background:#1e293b; color:#34d399; border:1px solid #34d399; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Laser: 532 nm (Green)</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec4_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Temperature $T$: <span id="spec4_t_val" style="color:#fbbf24; font-weight:600;">300 K</span></label>
            <input type="range" id="spec4_t" min="100" max="800" value="300" step="10" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Vibrational Mode $\\tilde{\\nu}_v$: <span id="spec4_nu_val" style="color:#38bdf8; font-weight:600;">992 cm⁻¹ (Benzene ring)</span></label>
            <input type="range" id="spec4_nu" min="300" max="1800" value="992" step="20" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Laser Intensity: <span id="spec4_p_val" style="color:#ec4899; font-weight:600;">100 mW</span></label>
            <input type="range" id="spec4_p" min="10" max="250" value="100" step="10" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec4_canvas");
    let state = { T: 300, nu_v: 992, laserNm: 532, power: 100, t: 0 };
    let animId = null;

    document.getElementById("spec4_t").oninput = (e) => {
      state.T = parseFloat(e.target.value);
      document.getElementById("spec4_t_val").innerText = `${state.T} K`;
    };
    document.getElementById("spec4_nu").oninput = (e) => {
      state.nu_v = parseFloat(e.target.value);
      document.getElementById("spec4_nu_val").innerText = `${state.nu_v} cm⁻¹`;
    };
    document.getElementById("spec4_p").oninput = (e) => {
      state.power = parseFloat(e.target.value);
      document.getElementById("spec4_p_val").innerText = `${state.power} mW`;
    };
    document.getElementById("spec4_btn_laser").onclick = (e) => {
      if (state.laserNm === 532) {
        state.laserNm = 785;
        e.target.innerText = "Laser: 785 nm (NIR)";
        e.target.style.color = "#f43f5e";
        e.target.style.borderColor = "#f43f5e";
      } else {
        state.laserNm = 532;
        e.target.innerText = "Laser: 532 nm (Green)";
        e.target.style.color = "#34d399";
        e.target.style.borderColor = "#34d399";
      }
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

      // Left Panel: Dynamic Polarizability Ellipsoid
      const ellX = W * 0.22;
      const ellY = H * 0.45;
      const vibMod = Math.sin(state.t * 2);
      const radX = 55 + vibMod * 16;
      const radY = 32 - vibMod * 10;

      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Dynamic Polarizability Ellipsoid α(q)", 16, 20);

      // Draw Ellipsoid
      ctx.save();
      ctx.translate(ellX, ellY);
      ctx.beginPath();
      ctx.ellipse(0, 0, radX, radY, 0, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = "#38bdf8";
      ctx.stroke();

      // Induced dipole arrow
      const laserColor = state.laserNm === 532 ? "#34d399" : "#f43f5e";
      const fieldMod = Math.sin(state.t * 8);
      ctx.strokeStyle = laserColor;
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.lineTo(0, -fieldMod * 45);
      ctx.stroke();

      ctx.restore();

      ctx.fillStyle = laserColor;
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText(`Incident Field E₀ (${state.laserNm} nm)`, ellX - 45, ellY + 55);

      // Right Panel: Raman Spectrum (Rayleigh, Stokes, Anti-Stokes)
      const specLeft = W * 0.46;
      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Raman Spectrum: Rayleigh, Stokes (ν₀ - νᵥ), Anti-Stokes (ν₀ + νᵥ)", specLeft, 20);

      const baselineY = H * 0.8;
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.beginPath();
      ctx.moveTo(specLeft, baselineY);
      ctx.lineTo(W - 20, baselineY);
      ctx.stroke();

      const centerX = specLeft + (W - specLeft - 20) * 0.5;

      // Rayleigh Peak (Center)
      ctx.strokeStyle = laserColor;
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(centerX, baselineY);
      ctx.lineTo(centerX, baselineY - H * 0.68);
      ctx.stroke();
      ctx.fillStyle = laserColor;
      ctx.fillText("Rayleigh (ν₀)", centerX - 25, baselineY - H * 0.7);

      // Boltzmann Factor for Anti-Stokes / Stokes ratio: exp(-h nu_v / kT)
      const h_c_k = 1.4388; // cm K
      const boltzmannFactor = Math.exp(-(h_c_k * state.nu_v) / state.T);
      const stokesIntensity = (state.power / 100) * (H * 0.45);
      const antiStokesIntensity = stokesIntensity * boltzmannFactor;

      const deltaX = (state.nu_v / 2000) * (W - specLeft - 60) * 0.42;

      // Stokes Peak (Red-shifted / Wavenumber shift positive)
      const stokesX = centerX + deltaX;
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(stokesX, baselineY);
      ctx.lineTo(stokesX, baselineY - stokesIntensity);
      ctx.stroke();
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("Stokes", stokesX - 15, baselineY - stokesIntensity - 6);
      ctx.fillText(`+${state.nu_v.toFixed(0)} cm⁻¹`, stokesX - 22, baselineY + 16);

      // Anti-Stokes Peak (Blue-shifted)
      const antiStokesX = centerX - deltaX;
      ctx.strokeStyle = "#f472b6";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(antiStokesX, baselineY);
      ctx.lineTo(antiStokesX, baselineY - antiStokesIntensity);
      ctx.stroke();
      ctx.fillStyle = "#f472b6";
      ctx.fillText("Anti-Stokes", antiStokesX - 25, baselineY - Math.max(antiStokesIntensity, 15) - 6);
      ctx.fillText(`-${state.nu_v.toFixed(0)} cm⁻¹`, antiStokesX - 25, baselineY + 16);

      // Ratio formula readout
      ctx.fillStyle = "#fbbf24";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText(`I(Anti-Stokes) / I(Stokes) = exp(-hcν̃ᵥ/k_BT) = ${boltzmannFactor.toFixed(4)}`, specLeft, H * 0.94);

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 5: sim_spec_atomic_term_symbols_zeeman (Unit 5)
     Russell-Saunders Term Symbols, Spin-Orbit Doublet & Zeeman Splitting
     ========================================================================= */
  function sim_spec_atomic_term_symbols_zeeman(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Atomic Term Symbols & Anomalous Zeeman Effect</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 5: Spin-Orbit Coupling & Landé g-Factor</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="spec5_btn_atom" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">System: Sodium (Na D-Lines)</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec5_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Magnetic Field $B_0$: <span id="spec5_b_val" style="color:#fbbf24; font-weight:600;">1.5 Tesla</span></label>
            <input type="range" id="spec5_b" min="0" max="5.0" value="1.5" step="0.2" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Spin-Orbit Constant $\\zeta$: <span id="spec5_z_val" style="color:#38bdf8; font-weight:600;">17.2 cm⁻¹</span></label>
            <input type="range" id="spec5_z" min="5" max="50" value="17.2" step="1" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec5_canvas");
    let state = { B: 1.5, zeta: 17.2, system: "Na" };
    let animId = null;

    document.getElementById("spec5_b").oninput = (e) => {
      state.B = parseFloat(e.target.value);
      document.getElementById("spec5_b_val").innerText = `${state.B.toFixed(1)} Tesla`;
    };
    document.getElementById("spec5_z").oninput = (e) => {
      state.zeta = parseFloat(e.target.value);
      document.getElementById("spec5_z_val").innerText = `${state.zeta} cm⁻¹`;
    };
    document.getElementById("spec5_btn_atom").onclick = (e) => {
      if (state.system === "Na") {
        state.system = "C";
        e.target.innerText = "System: Carbon (2p² ³P)";
      } else {
        state.system = "Na";
        e.target.innerText = "System: Sodium (Na D-Lines)";
      }
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

      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(state.system === "Na" ? "Sodium 3p ²P State Fine Structure & Zeeman Splitting (²P₃/₂, ²P₁/₂ → ²S₁/₂)" : "Carbon 2p² Ground Configuration Term Splitting (³P₀, ³P₁, ³P₂)", 14, 20);

      const leftX = 60;
      const midX = W * 0.42;
      const rightX = W * 0.82;

      // Ground State (2S1/2 for Na)
      const gY = H * 0.85;
      ctx.strokeStyle = "#94a3b8";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(leftX, gY); ctx.lineTo(leftX + 80, gY); ctx.stroke();
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("²S₁/₂ (g=2)", leftX - 50, gY + 4);

      // Ground Zeeman splitting
      const gSplitting = state.B * 14;
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(rightX - 30, gY - gSplitting); ctx.lineTo(rightX + 50, gY - gSplitting); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(rightX - 30, gY + gSplitting); ctx.lineTo(rightX + 50, gY + gSplitting); ctx.stroke();
      ctx.fillStyle = "#38bdf8";
      ctx.font = "9px Inter, sans-serif";
      ctx.fillText("M_J = +1/2", rightX + 55, gY - gSplitting + 3);
      ctx.fillText("M_J = -1/2", rightX + 55, gY + gSplitting + 3);

      // Excited Unperturbed 2P State
      const pY = H * 0.28;
      ctx.strokeStyle = "rgba(255,255,255,0.4)";
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(leftX, pY); ctx.lineTo(leftX + 80, pY); ctx.stroke();
      ctx.fillStyle = "#ffffff";
      ctx.fillText("3p ²P (No SO)", leftX - 45, pY - 8);

      // Spin-Orbit Splitting into 2P3/2 and 2P1/2
      const soSplit = state.zeta * 1.5;
      const p32Y = pY - soSplit * 0.6;
      const p12Y = pY + soSplit * 1.2;

      ctx.strokeStyle = "#fbbf24";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(midX - 30, p32Y); ctx.lineTo(midX + 50, p32Y); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(midX - 30, p12Y); ctx.lineTo(midX + 50, p12Y); ctx.stroke();
      ctx.fillStyle = "#fbbf24";
      ctx.fillText("²P₃/₂ (g=4/3)", midX + 55, p32Y + 4);
      ctx.fillText("²P₁/₂ (g=2/3)", midX + 55, p12Y + 4);

      // Zeeman splitting of 2P3/2 (MJ = +3/2, +1/2, -1/2, -3/2)
      const g32 = 4 / 3;
      for (let m = 0; m < 4; m++) {
        const mj = 1.5 - m;
        const shift = mj * g32 * state.B * 12;
        ctx.strokeStyle = "#f472b6";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(rightX - 30, p32Y - shift);
        ctx.lineTo(rightX + 50, p32Y - shift);
        ctx.stroke();
        ctx.fillStyle = "#f472b6";
        ctx.fillText(`M_J = ${mj > 0 ? "+" : ""}${mj}`, rightX + 55, p32Y - shift + 3);
      }

      // Zeeman splitting of 2P1/2 (MJ = +1/2, -1/2)
      const g12 = 2 / 3;
      for (let m = 0; m < 2; m++) {
        const mj = 0.5 - m;
        const shift = mj * g12 * state.B * 12;
        ctx.strokeStyle = "#34d399";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(rightX - 30, p12Y - shift);
        ctx.lineTo(rightX + 50, p12Y - shift);
        ctx.stroke();
        ctx.fillStyle = "#34d399";
        ctx.fillText(`M_J = ${mj > 0 ? "+" : ""}${mj}`, rightX + 55, p12Y - shift + 3);
      }

      // Column labels
      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Config (n, l)", leftX + 15, H * 0.95);
      ctx.fillText("Spin-Orbit (L-S)", midX - 5, H * 0.95);
      ctx.fillText("Zeeman (B₀ Field)", rightX - 10, H * 0.95);

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 6: sim_spec_franck_condon_vibronic (Unit 6)
     Vibronic Potential Energy Curves & Franck-Condon Overlap Integrals
     ========================================================================= */
  function sim_spec_franck_condon_vibronic(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Franck-Condon Principle & Vibronic Envelope</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 6: Molecular Electronic Spectroscopy</span>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec6_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Equilibrium Displacement $\\Delta R_e$: <span id="spec6_r_val" style="color:#38bdf8; font-weight:600;">0.15 Å</span></label>
            <input type="range" id="spec6_r" min="0" max="0.4" value="0.15" step="0.02" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Excited State Force Constant $k'/k''$: <span id="spec6_k_val" style="color:#fbbf24; font-weight:600;">0.85</span></label>
            <input type="range" id="spec6_k" min="0.5" max="1.3" value="0.85" step="0.05" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec6_canvas");
    let state = { dRe: 0.15, kRatio: 0.85 };
    let animId = null;

    document.getElementById("spec6_r").oninput = (e) => {
      state.dRe = parseFloat(e.target.value);
      document.getElementById("spec6_r_val").innerText = `${state.dRe.toFixed(2)} Å`;
    };
    document.getElementById("spec6_k").oninput = (e) => {
      state.kRatio = parseFloat(e.target.value);
      document.getElementById("spec6_k_val").innerText = `${state.kRatio.toFixed(2)}`;
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

      // Left Panel: Potential Wells (Ground & Excited Electronic States)
      const potW = W * 0.58;
      const Re_g = potW * 0.38;
      const Re_e = Re_g + (state.dRe / 0.4) * (potW * 0.28);

      const gBaseY = H * 0.88;
      const eBaseY = H * 0.45;

      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Electronic Potential Wells & Vertical Transitions (R_e'' vs R_e')", 14, 20);

      // Ground Well (Harmonic / Morse approx)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 30; x < potW - 20; x++) {
        const dx = x - Re_g;
        const y = gBaseY - 0.007 * dx * dx;
        if (x === 30) ctx.moveTo(x, Math.max(y, 10)); else ctx.lineTo(x, Math.max(y, 10));
      }
      ctx.stroke();

      // Ground vibrational wavefunctions (v=0)
      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      ctx.beginPath();
      const v0Y = gBaseY - 14;
      ctx.moveTo(Re_g - 40, v0Y);
      for (let x = Re_g - 40; x <= Re_g + 40; x++) {
        const psi = Math.exp(-Math.pow((x - Re_g) / 16, 2)) * 16;
        ctx.lineTo(x, v0Y - psi);
      }
      ctx.lineTo(Re_g + 40, v0Y);
      ctx.fill();
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("v'' = 0", Re_g + 48, v0Y + 3);

      // Excited State Well
      ctx.strokeStyle = "#f472b6";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 30; x < potW - 20; x++) {
        const dx = x - Re_e;
        const y = eBaseY - 0.007 * state.kRatio * dx * dx;
        if (x === 30) ctx.moveTo(x, Math.max(y, 10)); else ctx.lineTo(x, Math.max(y, 10));
      }
      ctx.stroke();

      // Excited vibrational levels (v' = 0, 1, 2, 3, 4)
      for (let vp = 0; vp <= 4; vp++) {
        const vY = eBaseY - (vp + 0.5) * 18;
        ctx.strokeStyle = "rgba(244, 114, 182, 0.4)";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(Re_e - 35, vY);
        ctx.lineTo(Re_e + 35, vY);
        ctx.stroke();
        ctx.fillStyle = "#f472b6";
        ctx.font = "9px Inter, sans-serif";
        ctx.fillText(`v'=${vp}`, Re_e + 40, vY + 3);
      }

      // Vertical Franck-Condon Transition Arrow (R does not change during transition)
      ctx.strokeStyle = "#fbbf24";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(Re_g, v0Y);
      ctx.lineTo(Re_g, eBaseY - 55);
      ctx.stroke();
      ctx.fillStyle = "#fbbf24";
      ctx.beginPath();
      ctx.moveTo(Re_g, eBaseY - 60);
      ctx.lineTo(Re_g - 4, eBaseY - 50);
      ctx.lineTo(Re_g + 4, eBaseY - 50);
      ctx.fill();

      // Right Panel: Vibronic Absorption Progression Envelope
      const specLeft = potW + 20;
      ctx.fillStyle = "#34d399";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Vibronic Absorption Spectrum |⟨v'|0⟩|²", specLeft, 20);

      const baselineY = H * 0.85;
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.beginPath();
      ctx.moveTo(specLeft, baselineY);
      ctx.lineTo(W - 20, baselineY);
      ctx.stroke();

      // Poisson distribution for Franck-Condon factors: S^vp * exp(-S) / vp!
      const S = Math.pow(state.dRe * 8, 2); // Huang-Rhys factor
      function fact(n) { return n <= 1 ? 1 : n * fact(n - 1); }

      for (let vp = 0; vp <= 5; vp++) {
        const fcf = (Math.pow(S, vp) * Math.exp(-S)) / fact(vp);
        const x = specLeft + 25 + vp * 38;
        const height = fcf * (H * 0.65);

        ctx.strokeStyle = "#34d399";
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(x, baselineY);
        ctx.lineTo(x, baselineY - height);
        ctx.stroke();

        ctx.fillStyle = "#94a3b8";
        ctx.font = "10px Inter, sans-serif";
        ctx.fillText(`(${vp},0)`, x - 12, baselineY + 16);
      }

      ctx.fillStyle = "#fbbf24";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText(`Huang-Rhys Factor S = ${S.toFixed(2)}`, specLeft + 20, H * 0.95);

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 7: sim_spec_jablonski_photophysics (Unit 7)
     Jablonski Diagram, Fluorescence, Intersystem Crossing & Quenching
     ========================================================================= */
  function sim_spec_jablonski_photophysics(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Jablonski Diagram & Photophysical Dynamics</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 7: Fluorescence, ISC & Phosphorescence</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="spec7_btn_pulse" style="background:#38bdf8; color:#0f172a; font-weight:600; border:none; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Pulse Light</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec7_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Quencher Concentration $[Q]$: <span id="spec7_q_val" style="color:#ef4444; font-weight:600;">0.00 mM</span></label>
            <input type="range" id="spec7_q" min="0" max="0.05" value="0.0" step="0.005" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Heavy Atom Effect ($k_{\\text{ISC}}$): <span id="spec7_isc_val" style="color:#a855f7; font-weight:600;">1.0×</span></label>
            <input type="range" id="spec7_isc" min="0.2" max="5.0" value="1.0" step="0.2" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec7_canvas");
    let state = { Q: 0.0, k_isc_mult: 1.0, particles: [] };
    let animId = null;

    document.getElementById("spec7_q").oninput = (e) => {
      state.Q = parseFloat(e.target.value);
      document.getElementById("spec7_q_val").innerText = `${(state.Q * 1000).toFixed(1)} mM`;
    };
    document.getElementById("spec7_isc").oninput = (e) => {
      state.k_isc_mult = parseFloat(e.target.value);
      document.getElementById("spec7_isc_val").innerText = `${state.k_isc_mult.toFixed(1)}×`;
    };

    function addPulse() {
      for (let i = 0; i < 40; i++) {
        state.particles.push({
          x: 70 + Math.random() * 60,
          y: 280,
          state: 'absorb',
          targetY: 80,
          color: '#38bdf8'
        });
      }
    }
    document.getElementById("spec7_btn_pulse").onclick = addPulse;

    function render() {
      if (!canvas || !canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const setup = initCanvas(canvas);
      if (!setup) return;
      const { ctx, width: W, height: H } = setup;
      ctx.clearRect(0, 0, W, H);

      // Jablonski Diagram Energy Levels
      const s0Y = H * 0.85;
      const s1Y = H * 0.35;
      const s2Y = H * 0.15;
      const t1Y = H * 0.45;

      const sX = 60;
      const sW = W * 0.35;
      const tX = W * 0.52;
      const tW = W * 0.28;

      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Singlet States (S₀, S₁, S₂)", sX, 22);
      ctx.fillStyle = "#a855f7";
      ctx.fillText("Triplet State (T₁)", tX, 22);

      // S0 Level
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(sX, s0Y); ctx.lineTo(sX + sW, s0Y); ctx.stroke();
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("S₀ (Ground)", sX - 45, s0Y + 4);

      // S1 Level & Vibrational rungs
      ctx.strokeStyle = "#38bdf8";
      ctx.beginPath(); ctx.moveTo(sX, s1Y); ctx.lineTo(sX + sW, s1Y); ctx.stroke();
      ctx.fillText("S₁", sX - 25, s1Y + 4);

      // S2 Level
      ctx.strokeStyle = "rgba(56, 189, 248, 0.5)";
      ctx.beginPath(); ctx.moveTo(sX, s2Y); ctx.lineTo(sX + sW, s2Y); ctx.stroke();
      ctx.fillText("S₂", sX - 25, s2Y + 4);

      // T1 Level
      ctx.strokeStyle = "#a855f7";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(tX, t1Y); ctx.lineTo(tX + tW, t1Y); ctx.stroke();
      ctx.fillStyle = "#a855f7";
      ctx.fillText("T₁", tX + tW + 10, t1Y + 4);

      // Transition paths arrows
      // 1. Absorption S0 -> S1/S2 (Blue up)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(sX + 35, s0Y); ctx.lineTo(sX + 35, s1Y); ctx.stroke();

      // 2. Fluorescence S1 -> S0 (Green down)
      ctx.strokeStyle = "#34d399";
      ctx.beginPath(); ctx.moveTo(sX + 75, s1Y); ctx.lineTo(sX + 75, s0Y); ctx.stroke();

      // 3. Intersystem Crossing S1 -> T1 (Purple horizontal wavy)
      ctx.strokeStyle = "#a855f7";
      ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(sX + sW - 10, s1Y); ctx.lineTo(tX + 10, t1Y); ctx.stroke();
      ctx.setLineDash([]);

      // 4. Phosphorescence T1 -> S0 (Red down)
      ctx.strokeStyle = "#f43f5e";
      ctx.beginPath(); ctx.moveTo(tX + 45, t1Y); ctx.lineTo(tX + 45, s0Y); ctx.stroke();

      // Labels for pathways
      ctx.font = "10px Inter, sans-serif";
      ctx.fillStyle = "#38bdf8"; ctx.fillText("Abs (hν)", sX + 18, (s0Y + s1Y) * 0.5);
      ctx.fillStyle = "#34d399"; ctx.fillText("Fluor (k_r)", sX + 80, (s0Y + s1Y) * 0.5);
      ctx.fillStyle = "#a855f7"; ctx.fillText("ISC", (sX + sW + tX) * 0.5 - 10, s1Y + 12);
      ctx.fillStyle = "#f43f5e"; ctx.fillText("Phos (k_p)", tX + 50, (s0Y + t1Y) * 0.5);

      // Particle update & rendering
      for (let i = state.particles.length - 1; i >= 0; i--) {
        const p = state.particles[i];
        if (p.state === 'absorb') {
          p.y -= 4;
          if (p.y <= s1Y) {
            p.y = s1Y;
            // Decision: Fluor vs ISC vs Quench
            const rand = Math.random();
            const p_isc = 0.25 * state.k_isc_mult;
            const p_quench = state.Q * 12;
            if (rand < p_quench) {
              p.state = 'quenched';
              p.color = '#ef4444';
            } else if (rand < p_quench + p_isc) {
              p.state = 'isc';
              p.color = '#a855f7';
            } else {
              p.state = 'fluor';
              p.color = '#34d399';
            }
          }
        } else if (p.state === 'fluor') {
          p.y += 3;
          if (p.y >= s0Y) state.particles.splice(i, 1);
        } else if (p.state === 'isc') {
          p.x += 2;
          p.y += 0.5;
          if (p.x >= tX + 45) {
            p.state = 'phos';
            p.color = '#f43f5e';
          }
        } else if (p.state === 'phos') {
          p.y += 0.8; // slower
          if (p.y >= s0Y) state.particles.splice(i, 1);
        } else if (p.state === 'quenched') {
          p.y += 2;
          p.x += (Math.random() - 0.5) * 4;
          if (p.y >= s0Y) state.particles.splice(i, 1);
        }

        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, 3.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // Stern-Volmer Equation Live Readout
      const K_SV = 150; // M-1
      const F0_F = 1 + K_SV * state.Q;
      ctx.fillStyle = "#fbbf24";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText(`Stern-Volmer: F₀/F = 1 + K_SV[Q] = ${F0_F.toFixed(2)} | Quantum Yield Φ_f = ${(1 / F0_F * (1 / (1 + 0.3 * state.k_isc_mult))).toFixed(2)}`, sX, H * 0.95);

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 8: sim_spec_nmr_larmor_bloch_precession (Unit 8)
     3D Larmor Precession, RF Pulse Excitation & Bloch T1/T2 Relaxation
     ========================================================================= */
  function sim_spec_nmr_larmor_bloch_precession(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Nuclear Larmor Precession & Bloch Relaxation (FID)</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 8: Pulse NMR & Spin Dynamics</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="spec8_btn_90" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Apply 90° Pulse</button>
            <button id="spec8_btn_180" style="background:#1e293b; color:#fbbf24; border:1px solid #fbbf24; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Apply 180° Pulse</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec8_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Magnetic Field $B_0$: <span id="spec8_b_val" style="color:#38bdf8; font-weight:600;">7.05 T (300 MHz)</span></label>
            <input type="range" id="spec8_b" min="1.41" min="14.1" value="7.05" step="0.5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Longitudinal $T_1$ Relaxation: <span id="spec8_t1_val" style="color:#34d399; font-weight:600;">2.0 s</span></label>
            <input type="range" id="spec8_t1" min="0.5" max="5.0" value="2.0" step="0.5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Transverse $T_2$ Relaxation: <span id="spec8_t2_val" style="color:#f472b6; font-weight:600;">0.8 s</span></label>
            <input type="range" id="spec8_t2" min="0.2" max="2.0" value="0.8" step="0.1" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec8_canvas");
    let state = { B: 7.05, T1: 2.0, T2: 0.8, Mx: 0, My: 0, Mz: 1, angle: 0, fidHistory: [] };
    let animId = null;

    document.getElementById("spec8_btn_90").onclick = () => {
      // 90 degree pulse rotates Mz to My
      state.My = state.Mz;
      state.Mz = 0;
    };
    document.getElementById("spec8_btn_180").onclick = () => {
      // 180 degree pulse inverts Mz
      state.Mz = -state.Mz;
      state.My = -state.My;
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

      // Precession & Bloch relaxation equations
      const dt = 0.03;
      const omega = 3.5; // visual precession rate
      state.angle += omega * dt;

      // Bloch Relaxation: dMz/dt = (M0 - Mz)/T1, dMxy/dt = -Mxy/T2
      state.Mz += ((1.0 - state.Mz) / state.T1) * (dt * 0.5);
      state.Mx *= Math.exp(-(dt * 0.5) / state.T2);
      state.My *= Math.exp(-(dt * 0.5) / state.T2);

      const Mxy = Math.sqrt(state.Mx * state.Mx + state.My * state.My);
      const curMx = Mxy * Math.cos(state.angle);
      const curMy = Mxy * Math.sin(state.angle);

      state.fidHistory.push(curMy);
      if (state.fidHistory.length > 220) state.fidHistory.shift();

      // Left Panel: Bloch Sphere & Magnetization Vector
      const sphereX = W * 0.25;
      const sphereY = H * 0.5;
      const R = 75;

      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Bloch Sphere: M⃗(t) in Rotating Frame", 16, 20);

      // Sphere wireframe
      ctx.strokeStyle = "rgba(255,255,255,0.15)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.arc(sphereX, sphereY, R, 0, Math.PI * 2);
      ctx.stroke();

      // Equator ellipse
      ctx.beginPath();
      ctx.ellipse(sphereX, sphereY, R, R * 0.35, 0, 0, Math.PI * 2);
      ctx.stroke();

      // Z-axis (B0)
      ctx.strokeStyle = "#fbbf24";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(sphereX, sphereY + R + 15);
      ctx.lineTo(sphereX, sphereY - R - 20);
      ctx.stroke();
      ctx.fillStyle = "#fbbf24";
      ctx.fillText("B₀ (z)", sphereX + 8, sphereY - R - 15);

      // Magnetization Vector M
      const tipX = sphereX + curMx * (R * 0.85);
      const tipY = sphereY - state.Mz * (R * 0.85) + curMy * (R * 0.3);

      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(sphereX, sphereY);
      ctx.lineTo(tipX, tipY);
      ctx.stroke();

      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(tipX, tipY, 5, 0, Math.PI * 2);
      ctx.fill();

      // Right Panel: Free Induction Decay (FID) Signal Oscilloscope
      const fidLeft = W * 0.48;
      ctx.fillStyle = "#34d399";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Transverse Signal: FID S(t) = M_y(0) e^(-t/T₂) cos(ω₀t)", fidLeft, 20);

      const fidMidY = H * 0.5;
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(fidLeft, fidMidY);
      ctx.lineTo(W - 20, fidMidY);
      ctx.stroke();

      // Draw FID Waveform
      ctx.strokeStyle = "#34d399";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i < state.fidHistory.length; i++) {
        const x = fidLeft + (i / 220) * (W - fidLeft - 25);
        const y = fidMidY - state.fidHistory[i] * (H * 0.35);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Readouts
      ctx.fillStyle = "#fbbf24";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText(`M_z = ${state.Mz.toFixed(3)} | M_xy = ${Mxy.toFixed(3)} | ν₀ = 300 MHz`, fidLeft, H * 0.92);

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 9: sim_spec_nmr_spin_spin_splitting_2d (Unit 9)
     Scalar Coupling J Multiplet Tree & 2D COSY Cross-Peak Contour
     ========================================================================= */
  function sim_spec_nmr_spin_spin_splitting_2d(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Scalar J-Coupling & 2D COSY Cross-Peaks</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 9: Multiplet Trees & Correlation Spectroscopy</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="spec9_btn_sys" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">System: AX₃ (Triplet/Quartet)</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec9_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Coupling Constant $J$: <span id="spec9_j_val" style="color:#38bdf8; font-weight:600;">7.2 Hz</span></label>
            <input type="range" id="spec9_j" min="2.0" max="18.0" value="7.2" step="0.2" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Dihedral Angle $\\phi$ (Karplus): <span id="spec9_phi_val" style="color:#fbbf24; font-weight:600;">60°</span></label>
            <input type="range" id="spec9_phi" min="0" max="180" value="60" step="5" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec9_canvas");
    let state = { J: 7.2, phi: 60, system: "AX3" };
    let animId = null;

    document.getElementById("spec9_j").oninput = (e) => {
      state.J = parseFloat(e.target.value);
      document.getElementById("spec9_j_val").innerText = `${state.J.toFixed(1)} Hz`;
    };
    document.getElementById("spec9_phi").oninput = (e) => {
      state.phi = parseFloat(e.target.value);
      // Karplus relation: 7 - cos(phi) + 5 cos(2 phi)
      const rad = state.phi * Math.PI / 180;
      state.J = Math.max(1.5, 7.0 - 1.0 * Math.cos(rad) + 5.0 * Math.cos(2 * rad));
      document.getElementById("spec9_j").value = state.J;
      document.getElementById("spec9_j_val").innerText = `${state.J.toFixed(1)} Hz`;
      document.getElementById("spec9_phi_val").innerText = `${state.phi}°`;
    };
    document.getElementById("spec9_btn_sys").onclick = (e) => {
      if (state.system === "AX3") {
        state.system = "AX";
        e.target.innerText = "System: AX (Doublet/Doublet)";
      } else {
        state.system = "AX3";
        e.target.innerText = "System: AX₃ (Triplet/Quartet)";
      }
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

      // Left Panel: 1D Multiplet Tree & 1H Spectrum
      const specW = W * 0.52;
      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`1D ¹H Spectrum & Splitting Tree (${state.system}) | J = ${state.J.toFixed(1)} Hz`, 14, 20);

      const base1DY = H * 0.85;
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.beginPath();
      ctx.moveTo(30, base1DY);
      ctx.lineTo(specW - 20, base1DY);
      ctx.stroke();

      // Peak A (e.g. at 4.0 ppm) and Peak X (e.g. at 1.2 ppm)
      const xA = 80;
      const xX = specW - 80;

      if (state.system === "AX3") {
        // Peak A is a Quartet (1:3:3:1)
        const dX = state.J * 2.2;
        const qLines = [-1.5, -0.5, 0.5, 1.5];
        const qInts = [1, 3, 3, 1];
        for (let i = 0; i < 4; i++) {
          const px = xA + qLines[i] * dX;
          const h = (qInts[i] / 3) * (H * 0.45);
          ctx.strokeStyle = "#38bdf8";
          ctx.lineWidth = 2.5;
          ctx.beginPath(); ctx.moveTo(px, base1DY); ctx.lineTo(px, base1DY - h); ctx.stroke();
        }
        ctx.fillStyle = "#38bdf8";
        ctx.fillText("Quartet (1:3:3:1) -CH₂-", xA - 40, base1DY - H * 0.5);

        // Peak X is a Triplet (1:2:1)
        const tLines = [-1, 0, 1];
        const tInts = [1, 2, 1];
        for (let i = 0; i < 3; i++) {
          const px = xX + tLines[i] * dX;
          const h = (tInts[i] / 2) * (H * 0.5);
          ctx.strokeStyle = "#34d399";
          ctx.lineWidth = 2.5;
          ctx.beginPath(); ctx.moveTo(px, base1DY); ctx.lineTo(px, base1DY - h); ctx.stroke();
        }
        ctx.fillStyle = "#34d399";
        ctx.fillText("Triplet (1:2:1) -CH₃", xX - 35, base1DY - H * 0.55);
      } else {
        // Peak A is a Doublet (1:1), Peak X is a Doublet (1:1)
        const dX = state.J * 2.2;
        [-0.5, 0.5].forEach(m => {
          const pxA = xA + m * dX;
          ctx.strokeStyle = "#38bdf8";
          ctx.lineWidth = 2.5;
          ctx.beginPath(); ctx.moveTo(pxA, base1DY); ctx.lineTo(pxA, base1DY - H * 0.45); ctx.stroke();

          const pxX = xX + m * dX;
          ctx.strokeStyle = "#34d399";
          ctx.lineWidth = 2.5;
          ctx.beginPath(); ctx.moveTo(pxX, base1DY); ctx.lineTo(pxX, base1DY - H * 0.45); ctx.stroke();
        });
        ctx.fillStyle = "#38bdf8"; ctx.fillText("Doublet (1:1)", xA - 25, base1DY - H * 0.5);
        ctx.fillStyle = "#34d399"; ctx.fillText("Doublet (1:1)", xX - 25, base1DY - H * 0.5);
      }

      // Right Panel: 2D COSY Contour Map
      const cosyLeft = specW + 15;
      const cosySize = Math.min(W - cosyLeft - 30, H - 70);
      const cosyTop = 45;

      ctx.fillStyle = "#fbbf24";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("2D COSY Correlation Map", cosyLeft, 20);

      // COSY bounding box
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.lineWidth = 1;
      ctx.strokeRect(cosyLeft, cosyTop, cosySize, cosySize);

      // Diagonal line
      ctx.strokeStyle = "rgba(255,255,255,0.25)";
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(cosyLeft, cosyTop + cosySize);
      ctx.lineTo(cosyLeft + cosySize, cosyTop);
      ctx.stroke();
      ctx.setLineDash([]);

      // Diagonal peaks (A,A) and (X,X)
      const p1 = cosySize * 0.25;
      const p2 = cosySize * 0.75;

      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(cosyLeft + p1, cosyTop + cosySize - p1, 7, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#34d399";
      ctx.beginPath(); ctx.arc(cosyLeft + p2, cosyTop + cosySize - p2, 7, 0, Math.PI * 2); ctx.fill();

      // Cross peaks (A,X) and (X,A) showing scalar coupling!
      ctx.fillStyle = "#ec4899";
      ctx.beginPath(); ctx.arc(cosyLeft + p1, cosyTop + cosySize - p2, 6, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(cosyLeft + p2, cosyTop + cosySize - p1, 6, 0, Math.PI * 2); ctx.fill();

      ctx.font = "10px Inter, sans-serif";
      ctx.fillStyle = "#ec4899";
      ctx.fillText("Cross-Peak (A-X)", cosyLeft + p1 + 10, cosyTop + cosySize - p2 - 6);

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* =========================================================================
     SIMULATION 10: sim_spec_esr_mossbauer_hyperfine (Unit 10)
     Dual Mode: ESR Electron Hyperfine Multiplets & Mössbauer 57Fe Sextet
     ========================================================================= */
  function sim_spec_esr_mossbauer_hyperfine(container) {
    container = getContainerEl(container);
    if (!container) return;
    container.innerHTML = `
      <div style="background:#080d1a; border-radius:8px; padding:12px; color:#e2e8f0; font-family:Inter,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">ESR/EPR Hyperfine & Mössbauer Spectroscopy</span>
            <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 10: Unpaired Spins & Nuclear Transitions</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="spec10_btn_mode" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Mode: ESR Radical (·CH₃)</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
          <canvas id="spec10_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Hyperfine Coupling $a$ / Quadrupole $\\Delta E_Q$: <span id="spec10_a_val" style="color:#38bdf8; font-weight:600;">23.0 G</span></label>
            <input type="range" id="spec10_a" min="5" max="45" value="23" step="1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block;">Linewidth $\\Gamma$: <span id="spec10_w_val" style="color:#fbbf24; font-weight:600;">2.5 G</span></label>
            <input type="range" id="spec10_w" min="1.0" max="6.0" value="2.5" step="0.5" style="width:100%;">
          </div>
        </div>
      </div>
    `;

    const canvas = document.getElementById("spec10_canvas");
    let state = { mode: "ESR", a: 23, gamma: 2.5 };
    let animId = null;

    document.getElementById("spec10_a").oninput = (e) => {
      state.a = parseFloat(e.target.value);
      document.getElementById("spec10_a_val").innerText = state.mode === "ESR" ? `${state.a.toFixed(1)} G` : `${(state.a * 0.1).toFixed(2)} mm/s`;
    };
    document.getElementById("spec10_w").oninput = (e) => {
      state.gamma = parseFloat(e.target.value);
      document.getElementById("spec10_w_val").innerText = `${state.gamma.toFixed(1)} ${state.mode === "ESR" ? "G" : "mm/s"}`;
    };
    document.getElementById("spec10_btn_mode").onclick = (e) => {
      if (state.mode === "ESR") {
        state.mode = "Mossbauer";
        e.target.innerText = "Mode: Mössbauer ⁵⁷Fe Sextet";
        document.getElementById("spec10_a_val").innerText = `${(state.a * 0.1).toFixed(2)} mm/s`;
      } else {
        state.mode === "ESR";
        state.mode = "ESR";
        e.target.innerText = "Mode: ESR Radical (·CH₃)";
        document.getElementById("spec10_a_val").innerText = `${state.a.toFixed(1)} G`;
      }
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

      const midY = H * 0.52;
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.beginPath();
      ctx.moveTo(30, midY);
      ctx.lineTo(W - 30, midY);
      ctx.stroke();

      if (state.mode === "ESR") {
        // 1st Derivative ESR Line shape for Methyl Radical ·CH3 (1:3:3:1 Quartet from 3 equivalent protons)
        ctx.fillStyle = "#38bdf8";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText("ESR 1st-Derivative Spectrum: Methyl Radical ·CH₃ (Quartet 1:3:3:1) | a_H = " + state.a.toFixed(1) + " G", 14, 20);

        const centerX = W * 0.5;
        const spacing = state.a * 2.8;
        const shifts = [-1.5, -0.5, 0.5, 1.5];
        const amps = [1, 3, 3, 1];

        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        for (let x = 30; x < W - 30; x++) {
          let signal = 0;
          for (let i = 0; i < 4; i++) {
            const x0 = centerX + shifts[i] * spacing;
            const dx = (x - x0) / (state.gamma * 2.5);
            // 1st derivative of Lorentzian: -2 dx / (1 + dx^2)^2
            const deriv = (-2 * dx) / Math.pow(1 + dx * dx, 2);
            signal += amps[i] * deriv;
          }
          const y = midY - signal * 28;
          if (x === 30) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        ctx.fillStyle = "#fbbf24";
        ctx.font = "10px Inter, sans-serif";
        ctx.fillText("McConnell Relation: a_H = Q · ρ_π (Q ≈ -22.5 G) | Phase-sensitive 1st derivative", 30, H * 0.94);

      } else {
        // Mössbauer 57Fe Magnetic Sextet (3:2:1:1:2:3 absorption dips)
        ctx.fillStyle = "#f472b6";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText("⁵⁷Fe Mössbauer Transmission Spectrum: Magnetic Hyperfine Sextet (3:2:1:1:2:3)", 14, 20);

        const centerX = W * 0.5;
        const sextetLines = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5];
        const sextetInts = [3, 2, 1, 1, 2, 3];
        const spacing = state.a * 2.2;

        ctx.strokeStyle = "#f472b6";
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        for (let x = 30; x < W - 30; x++) {
          let trans = 1.0;
          for (let i = 0; i < 6; i++) {
            const x0 = centerX + sextetLines[i] * spacing;
            const dx = (x - x0) / (state.gamma * 3.0);
            const lorentz = 1 / (1 + dx * dx);
            trans -= (sextetInts[i] / 3) * 0.28 * lorentz;
          }
          const y = midY - (trans - 0.7) * (H * 0.7);
          if (x === 30) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        ctx.fillStyle = "#fbbf24";
        ctx.font = "10px Inter, sans-serif";
        ctx.fillText("Doppler Velocity v (mm/s) | Isomer shift δ & Internal field B_int = 33 Tesla (α-Fe)", 30, H * 0.94);
      }

      animId = requestAnimationFrame(render);
    }
    render();

    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  return {
    sim_spec_electromagnetic_wave_fourier,
    sim_spec_rotational_microwave_rotor,
    sim_spec_rovibrational_co_spectrum,
    sim_spec_raman_polarizability_ellipsoid,
    sim_spec_atomic_term_symbols_zeeman,
    sim_spec_franck_condon_vibronic,
    sim_spec_jablonski_photophysics,
    sim_spec_nmr_larmor_bloch_precession,
    sim_spec_nmr_spin_spin_splitting_2d,
    sim_spec_esr_mossbauer_hyperfine
  };
})();

/* ==========================================================================
   Global Simulation Engine Registry Adapter
   ========================================================================== */
if (typeof window !== 'undefined') {
  window.SimulationEngine = window.SimulationEngine || {};
  Object.keys(window.SpectroscopySimulations).forEach(function(key) {
    window[key] = window.SpectroscopySimulations[key];
  });
  const originalInit = window.SimulationEngine.initSimulation;
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    const el = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    if (!el) return;
    if (window.SpectroscopySimulations && typeof window.SpectroscopySimulations[simType] === 'function') {
      return window.SpectroscopySimulations[simType](el);
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

