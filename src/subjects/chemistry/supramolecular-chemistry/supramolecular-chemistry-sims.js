/**
 * supramolecular-chemistry-sims.js
 * 10 High-Performance 60 FPS Interactive HTML5 Canvas Simulation Engines
 * for Supramolecular Chemistry (OpenSTEM Milestone Textbook #55)
 * Equipped with Dimension-Caching, DPR Scaling, and isConnected Cleanup Guards.
 */

window.SupramolecularChemistrySimulations = (function() {
  'use strict';

  function initCanvas(canvas) {
    if (!canvas) return null;
    const dpr = window.devicePixelRatio || 1;
    let w = canvas._cssWidth;
    let h = canvas._cssHeight;

    if (!w || !h) {
      const rect = canvas.getBoundingClientRect();
      w = Math.floor(rect.width > 0 ? rect.width : (canvas.parentElement ? canvas.parentElement.clientWidth : 800)) || 800;
      h = Math.floor(rect.height > 0 ? rect.height : (canvas.parentElement ? canvas.parentElement.clientHeight : 380)) || 380;
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

  /* ==========================================================================
     SIMULATION 1: Non-Covalent Binding Titration & Job Plot Simulator
     ========================================================================== */
  function sim_supra_binding_titration_job(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 1: Non-Covalent Binding Titration & Job Plot Engine</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Equilibrium Isotherm</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Analysis Mode:</label>
            <select id="u1-mode" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="titration">1:1 Binding Titration ([G]t/[H]t)</option>
              <option value="job11">Job Plot: 1:1 Stoichiometry</option>
              <option value="job12">Job Plot: 1:2 Stoichiometry (HG2)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Affinity log Ka: <span id="u1-ka-val" style="color:#58a6ff; font-weight:bold;">4.50</span> (Ka = <span id="u1-ka-num">3.16e4</span> M⁻¹)</label>
            <input type="range" id="u1-ka" min="2.0" max="6.5" step="0.1" value="4.50" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Host Conc [H]₀ (mM): <span id="u1-h0-val" style="color:#58a6ff; font-weight:bold;">1.00</span></label>
            <input type="range" id="u1-h0" min="0.1" max="5.0" step="0.1" value="1.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Experimental Noise: <span id="u1-noise-val" style="color:#58a6ff; font-weight:bold;">Low (1.5%)</span></label>
            <input type="range" id="u1-noise" min="0" max="5" step="0.5" value="1.5" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u1-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>ΔG° = <strong id="u1-dg" style="color:#7ee787;">-25.68 kJ/mol</strong></span>
          <span>Max Saturation: <strong id="u1-sat" style="color:#7ee787;">96.8%</strong></span>
          <span>Job Peak Mole Fraction: <strong id="u1-xpeak" style="color:#7ee787;">x = 0.500</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u1-canvas');
    const modeSel = el.querySelector('#u1-mode');
    const kaSlider = el.querySelector('#u1-ka');
    const h0Slider = el.querySelector('#u1-h0');
    const noiseSlider = el.querySelector('#u1-noise');

    const kaVal = el.querySelector('#u1-ka-val');
    const kaNum = el.querySelector('#u1-ka-num');
    const h0Val = el.querySelector('#u1-h0-val');
    const noiseVal = el.querySelector('#u1-noise-val');
    const dgVal = el.querySelector('#u1-dg');
    const satVal = el.querySelector('#u1-sat');
    const xpeakVal = el.querySelector('#u1-xpeak');

    // Pseudo-random noise seed array
    const noiseOffsets = [];
    for (let i = 0; i < 50; i++) {
      noiseOffsets.push((Math.sin(i * 12.9898) * 43758.5453) % 1);
    }

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const mode = modeSel.value;
      const logKa = parseFloat(kaSlider.value);
      const Ka = Math.pow(10, logKa);
      const H0 = parseFloat(h0Slider.value) * 1e-3; // M
      const noiseAmp = parseFloat(noiseSlider.value) * 0.01;

      kaVal.textContent = logKa.toFixed(2);
      kaNum.textContent = Ka.toExponential(2);
      h0Val.textContent = (H0 * 1e3).toFixed(2);
      noiseVal.textContent = (noiseAmp * 100).toFixed(1) + '%';

      const dG = -8.31446 * 298.15 * Math.log(Ka) * 1e-3;
      dgVal.textContent = dG.toFixed(2) + ' kJ/mol';

      ctx.clearRect(0, 0, W, H);

      // Plot margins
      const pad = { left: 65, right: 30, top: 30, bottom: 50 };
      const pW = W - pad.left - pad.right;
      const pH = H - pad.top - pad.bottom;

      // Draw grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let i = 0; i <= 5; i++) {
        const y = pad.top + (pH * i) / 5;
        ctx.beginPath();
        ctx.moveTo(pad.left, y);
        ctx.lineTo(pad.left + pW, y);
        ctx.stroke();

        const x = pad.left + (pW * i) / 5;
        ctx.beginPath();
        ctx.moveTo(x, pad.top);
        ctx.lineTo(x, pad.top + pH);
        ctx.stroke();
      }

      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1.5;
      ctx.strokeRect(pad.left, pad.top, pW, pH);

      if (mode === 'titration') {
        xpeakVal.textContent = 'N/A (Job mode)';
        // 1:1 Titration: ratio r = [G]t / [H]t from 0 to 4.0
        const maxR = 4.0;
        ctx.fillStyle = '#8b949e';
        ctx.font = '11px sans-serif';
        ctx.textAlign = 'center';
        for (let i = 0; i <= 4; i++) {
          const x = pad.left + (pW * i) / 4;
          ctx.fillText((i).toString(), x, pad.top + pH + 18);
        }
        ctx.fillText('Equivalents of Guest added ([G]t / [H]t)', pad.left + pW / 2, pad.top + pH + 36);

        ctx.textAlign = 'right';
        for (let i = 0; i <= 5; i++) {
          const y = pad.top + pH - (pH * i) / 5;
          ctx.fillText((i * 0.2).toFixed(1), pad.left - 8, y + 4);
        }
        ctx.save();
        ctx.translate(18, pad.top + pH / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.textAlign = 'center';
        ctx.fillText('Fraction of Host Bound (fb = [HG] / [H]t)', 0, 0);
        ctx.restore();

        // Theoretical curve
        ctx.beginPath();
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 2.5;

        let maxFb = 0;
        for (let px = 0; px <= pW; px++) {
          const r = (px / pW) * maxR;
          const Gt = r * H0;
          // [HG] from quadratic: Ka [HG]^2 - (1 + Ka H0 + Ka Gt)[HG] + Ka H0 Gt = 0
          const b = 1.0 + Ka * (H0 + Gt);
          const disc = Math.max(0, b * b - 4.0 * Ka * Ka * H0 * Gt);
          const HG = (b - Math.sqrt(disc)) / (2.0 * Ka);
          const fb = Math.min(1.0, HG / H0);
          if (px === pW) maxFb = fb;

          const cx = pad.left + px;
          const cy = pad.top + pH - fb * pH;
          if (px === 0) ctx.moveTo(cx, cy);
          else ctx.lineTo(cx, cy);
        }
        ctx.stroke();

        satVal.textContent = (maxFb * 100).toFixed(1) + '%';

        // Experimental noisy data points
        const numPoints = 16;
        ctx.fillStyle = '#f0883e';
        for (let i = 0; i <= numPoints; i++) {
          const r = (i / numPoints) * maxR;
          const Gt = r * H0;
          const b = 1.0 + Ka * (H0 + Gt);
          const disc = Math.max(0, b * b - 4.0 * Ka * Ka * H0 * Gt);
          const HG = (b - Math.sqrt(disc)) / (2.0 * Ka);
          const baseFb = Math.min(1.0, HG / H0);
          const noise = (noiseOffsets[i % noiseOffsets.length] - 0.5) * 2 * noiseAmp;
          const expFb = Math.max(0, Math.min(1.0, baseFb + noise));

          const cx = pad.left + (r / maxR) * pW;
          const cy = pad.top + pH - expFb * pH;

          ctx.beginPath();
          ctx.arc(cx, cy, 4, 0, Math.PI * 2);
          ctx.fill();
          ctx.strokeStyle = '#0d1117';
          ctx.lineWidth = 1;
          ctx.stroke();
        }

        // Legend
        ctx.fillStyle = '#58a6ff';
        ctx.fillRect(pad.left + 20, pad.top + 15, 18, 3);
        ctx.fillStyle = '#c9d1d9';
        ctx.font = '11px sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText('Non-linear 1:1 Fit (Ka = ' + Ka.toExponential(1) + ' M⁻¹)', pad.left + 45, pad.top + 19);

        ctx.fillStyle = '#f0883e';
        ctx.beginPath();
        ctx.arc(pad.left + 29, pad.top + 33, 4, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#c9d1d9';
        ctx.fillText('Simulated NMR / UV Titration Data', pad.left + 45, pad.top + 36);

      } else {
        // Job Plot mode (Continuous variation)
        const is12 = mode === 'job12';
        xpeakVal.textContent = is12 ? 'x = 0.667 (1:2 complex HG₂)' : 'x = 0.500 (1:1 complex HG)';
        satVal.textContent = 'Job Peak Max';

        ctx.fillStyle = '#8b949e';
        ctx.font = '11px sans-serif';
        ctx.textAlign = 'center';
        for (let i = 0; i <= 5; i++) {
          const x = pad.left + (pW * i) / 5;
          ctx.fillText((i * 0.2).toFixed(1), x, pad.top + pH + 18);
        }
        ctx.fillText('Mole Fraction of Guest, x_guest = [G]t / ([H]t + [G]t)', pad.left + pW / 2, pad.top + pH + 36);

        ctx.textAlign = 'right';
        for (let i = 0; i <= 5; i++) {
          const y = pad.top + pH - (pH * i) / 5;
          ctx.fillText((i * 0.2).toFixed(1), pad.left - 8, y + 4);
        }
        ctx.save();
        ctx.translate(18, pad.top + pH / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.textAlign = 'center';
        ctx.fillText('Normalized Complex Signal (ΔA / ΔA_max)', 0, 0);
        ctx.restore();

        // Calculate peak location
        const peakX = is12 ? 2.0 / 3.0 : 0.5;

        // Draw Job Curve
        ctx.beginPath();
        ctx.strokeStyle = is12 ? '#d2a8ff' : '#7ee787';
        ctx.lineWidth = 2.5;

        const Ctotal = 2.0 * H0; // constant total concentration
        let maxVal = 0;
        // First pass for normalization
        for (let px = 0; px <= pW; px++) {
          const xg = px / pW;
          const xh = 1.0 - xg;
          let val = 0;
          if (!is12) {
            val = xh * xg; // proportional to [HG]
          } else {
            val = xh * xg * xg; // proportional to [HG2]
          }
          if (val > maxVal) maxVal = val;
        }

        for (let px = 0; px <= pW; px++) {
          const xg = px / pW;
          const xh = 1.0 - xg;
          const val = (!is12 ? (xh * xg) : (xh * xg * xg)) / (maxVal || 1.0);
          const cx = pad.left + px;
          const cy = pad.top + pH - val * pH;
          if (px === 0) ctx.moveTo(cx, cy);
          else ctx.lineTo(cx, cy);
        }
        ctx.stroke();

        // Draw vertical apex dashed line
        const apexPx = pad.left + peakX * pW;
        ctx.setLineDash([4, 4]);
        ctx.strokeStyle = '#f0883e';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(apexPx, pad.top);
        ctx.lineTo(apexPx, pad.top + pH);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#f0883e';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Apex: x = ' + peakX.toFixed(3), apexPx, pad.top - 8);

        // Experimental points
        const numPoints = 11;
        ctx.fillStyle = '#58a6ff';
        for (let i = 0; i <= numPoints; i++) {
          const xg = i / numPoints;
          const xh = 1.0 - xg;
          const baseVal = (!is12 ? (xh * xg) : (xh * xg * xg)) / (maxVal || 1.0);
          const noise = (noiseOffsets[i % noiseOffsets.length] - 0.5) * 2 * noiseAmp;
          const expVal = Math.max(0, Math.min(1.0, baseVal + noise));

          const cx = pad.left + xg * pW;
          const cy = pad.top + pH - expVal * pH;

          ctx.beginPath();
          ctx.arc(cx, cy, 4, 0, Math.PI * 2);
          ctx.fill();
        }

        // Legend
        ctx.fillStyle = is12 ? '#d2a8ff' : '#7ee787';
        ctx.fillRect(pad.left + 20, pad.top + 15, 18, 3);
        ctx.fillStyle = '#c9d1d9';
        ctx.font = '11px sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText(is12 ? 'Theoretical 1:2 Complex Job Profile' : 'Theoretical 1:1 Complex Job Profile', pad.left + 45, pad.top + 19);
      }
    }

    [modeSel, kaSlider, h0Slider, noiseSlider].forEach(s => s.addEventListener('input', render));
    render();
  }

  /* ==========================================================================
     SIMULATION 2: Crown Ether / Cryptand Cation Size-Cavity Selectivity
     ========================================================================== */
  function sim_supra_crown_ether_selectivity(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 2: Crown Ether & Cryptand Cavity-Size Selectivity</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Pedersen / Lehn Model</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Macrocyclic Host:</label>
            <select id="u2-host" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="12c4">12-Crown-4 (r = 0.65 Å)</option>
              <option value="15c5">15-Crown-5 (r = 0.89 Å)</option>
              <option value="18c6" selected>18-Crown-6 (r = 1.38 Å)</option>
              <option value="21c7">21-Crown-7 (r = 1.80 Å)</option>
              <option value="c222">Cryptand [2.2.2] (r = 1.40 Å)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Alkali Metal Cation:</label>
            <select id="u2-cation" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="Li">Li⁺ (r = 0.76 Å)</option>
              <option value="Na">Na⁺ (r = 1.02 Å)</option>
              <option value="K" selected>K⁺ (r = 1.38 Å)</option>
              <option value="Rb">Rb⁺ (r = 1.52 Å)</option>
              <option value="Cs">Cs⁺ (r = 1.67 Å)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Solvent System:</label>
            <select id="u2-solv" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="MeOH" selected>Methanol (MeOH)</option>
              <option value="H2O">Water (H₂O, high desolvation)</option>
              <option value="MeCN">Acetonitrile (MeCN)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Thermal Vibration: <span id="u2-temp-val" style="color:#58a6ff; font-weight:bold;">298 K</span></label>
            <input type="range" id="u2-temp" min="260" max="360" step="5" value="298" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u2-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Binding Constant: <strong id="u2-logk" style="color:#7ee787;">log Ka = 6.10</strong> (Ka = <strong id="u2-ka" style="color:#7ee787;">1.26e6 M⁻¹</strong>)</span>
          <span>Size Fit Mismatch: <strong id="u2-mismatch" style="color:#7ee787;">Δr = 0.00 Å (Optimal)</strong></span>
          <span>Macrocyclic Effect: <strong id="u2-effect" style="color:#7ee787;">High Enthalpic Gain</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u2-canvas');
    const hostSel = el.querySelector('#u2-host');
    const catSel = el.querySelector('#u2-cation');
    const solvSel = el.querySelector('#u2-solv');
    const tempSlider = el.querySelector('#u2-temp');

    const tempVal = el.querySelector('#u2-temp-val');
    const logkVal = el.querySelector('#u2-logk');
    const kaVal = el.querySelector('#u2-ka');
    const mismatchVal = el.querySelector('#u2-mismatch');
    const effectVal = el.querySelector('#u2-effect');

    // Radii in Angstroms
    const hostData = {
      '12c4': { r: 0.65, nO: 4, name: '12-Crown-4', kMap: { Li: 3.3, Na: 1.7, K: 1.3, Rb: 0.9, Cs: 0.5 } },
      '15c5': { r: 0.89, nO: 5, name: '15-Crown-5', kMap: { Li: 2.1, Na: 3.7, K: 2.4, Rb: 1.9, Cs: 1.4 } },
      '18c6': { r: 1.38, nO: 6, name: '18-Crown-6', kMap: { Li: 1.6, Na: 4.3, K: 6.1, Rb: 5.3, Cs: 4.6 } },
      '21c7': { r: 1.80, nO: 7, name: '21-Crown-7', kMap: { Li: 1.0, Na: 2.4, K: 4.2, Rb: 4.9, Cs: 5.4 } },
      'c222': { r: 1.40, nO: 6, isCrypt: true, name: 'Cryptand [2.2.2]', kMap: { Li: 2.5, Na: 7.2, K: 9.8, Rb: 8.5, Cs: 5.8 } }
    };

    const cationData = {
      Li: { r: 0.76, color: '#ff7b72', name: 'Lithium' },
      Na: { r: 1.02, color: '#f0883e', name: 'Sodium' },
      K:  { r: 1.38, color: '#7ee787', name: 'Potassium' },
      Rb: { r: 1.52, color: '#a5d6ff', name: 'Rubidium' },
      Cs: { r: 1.67, color: '#d2a8ff', name: 'Cesium' }
    };

    let animAngle = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const hostKey = hostSel.value;
      const catKey = catSel.value;
      const solvent = solvSel.value;
      const temp = parseFloat(tempSlider.value);
      tempVal.textContent = temp + ' K';

      const host = hostData[hostKey];
      const cation = cationData[catKey];

      // Base logKa in MeOH
      let logK = host.kMap[catKey] || 1.0;
      if (solvent === 'H2O') logK = Math.max(0.5, logK - 3.8); // heavy water hydration penalty
      else if (solvent === 'MeCN') logK = logK + 0.8; // aprotic boost

      const Ka = Math.pow(10, logK);
      logkVal.textContent = 'log Ka = ' + logK.toFixed(2);
      kaVal.textContent = Ka.toExponential(2) + ' M⁻¹';

      const deltaR = cation.r - host.r;
      let fitText = 'Δr = ' + Math.abs(deltaR).toFixed(2) + ' Å ';
      if (Math.abs(deltaR) < 0.08) fitText += '(Optimal Fit)';
      else if (deltaR < 0) fitText += '(Too Small - Rattles)';
      else fitText += '(Too Large - Perched)';
      mismatchVal.textContent = fitText;

      effectVal.textContent = host.isCrypt ? 'Cryptate Effect: 3D Macrobicyclic Wrap' : 'Macrocyclic Effect: Preorganized Ring';

      ctx.clearRect(0, 0, W, H);

      // Left half: Molecular visualization
      // Right half: Selectivity bar graph
      const leftW = W * 0.52;
      const rightW = W - leftW;

      // Draw dividing line
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(leftW, 20);
      ctx.lineTo(leftW, H - 20);
      ctx.stroke();

      // Center of left visualization
      const cx = leftW / 2;
      const cy = H / 2;
      const scale = 55; // pixels per Angstrom

      const hostRadiusPx = host.r * scale;
      const cationRadiusPx = cation.r * scale;

      // Draw Crown Ether backbone
      ctx.save();
      ctx.translate(cx, cy);

      // Gentle thermal jitter
      const jitterAmp = ((temp - 260) / 100) * 1.5;
      const jx = (Math.sin(animAngle * 3) + Math.cos(animAngle * 5)) * jitterAmp;
      const jy = (Math.cos(animAngle * 4) + Math.sin(animAngle * 2)) * jitterAmp;

      // Draw Cavity boundary dashed circle
      ctx.beginPath();
      ctx.arc(0, 0, hostRadiusPx, 0, Math.PI * 2);
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1.5;
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Oxygen donors around the ring
      const nO = host.nO;
      const oCoords = [];
      for (let i = 0; i < nO; i++) {
        const theta = (i * 2 * Math.PI) / nO + (animAngle * 0.1);
        const ox = Math.cos(theta) * (hostRadiusPx + 14);
        const oy = Math.sin(theta) * (hostRadiusPx + 14);
        oCoords.push({ x: ox, y: oy });
      }

      // Draw connecting polyether links
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let i = 0; i < nO; i++) {
        const p1 = oCoords[i];
        const p2 = oCoords[(i + 1) % nO];
        // Curved strand
        const midTheta = ((i + 0.5) * 2 * Math.PI) / nO + (animAngle * 0.1);
        const mx = Math.cos(midTheta) * (hostRadiusPx + 24);
        const my = Math.sin(midTheta) * (hostRadiusPx + 24);
        if (i === 0) ctx.moveTo(p1.x, p1.y);
        ctx.quadraticCurveTo(mx, my, p2.x, p2.y);
      }
      ctx.closePath();
      ctx.stroke();

      // If cryptand, draw a 3rd bridging strap
      if (host.isCrypt) {
        ctx.strokeStyle = '#d2a8ff';
        ctx.lineWidth = 2.5;
        ctx.setLineDash([6, 3]);
        ctx.beginPath();
        ctx.ellipse(0, 0, hostRadiusPx + 28, hostRadiusPx * 0.5, 0, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Draw oxygen atoms (red balls with lone pair chevrons)
      for (let i = 0; i < nO; i++) {
        const p = oCoords[i];
        ctx.fillStyle = '#f85149';
        ctx.beginPath();
        ctx.arc(p.x, p.y, 7, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Oxygen lone pair interaction lines to cation
        if (Math.abs(deltaR) < 0.25) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(jx, jy);
          ctx.strokeStyle = 'rgba(126, 231, 135, 0.45)';
          ctx.lineWidth = 1.5;
          ctx.stroke();
        }
      }

      // Draw central Cation
      ctx.fillStyle = cation.color;
      ctx.beginPath();
      // If cation too large, draw offset perched out of plane
      const perchY = deltaR > 0.15 ? -18 : 0;
      ctx.arc(jx, jy + perchY, cationRadiusPx, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Cation label
      ctx.fillStyle = '#010409';
      ctx.font = 'bold 12px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(catKey + '⁺', jx, jy + perchY);

      ctx.restore();

      // Sub-label for Host
      ctx.fillStyle = '#c9d1d9';
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(host.name + ' (Cavity r = ' + host.r.toFixed(2) + ' Å)', leftW / 2, 28);
      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.fillText('Encapsulating ' + cation.name + ' (r = ' + cation.r.toFixed(2) + ' Å)', leftW / 2, H - 18);

      // Right half: Selectivity Bar Chart
      const bPad = { left: leftW + 45, right: 25, top: 40, bottom: 45 };
      const bW = W - bPad.left - bPad.right;
      const bH = H - bPad.top - bPad.bottom;

      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 12px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Alkali Cation Selectivity Profile (log Ka in ' + solvent + ')', bPad.left, 24);

      // Y-axis grid
      const maxLogK = 10.0;
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let i = 0; i <= 5; i++) {
        const y = bPad.top + bH - (bH * i) / 5;
        ctx.beginPath();
        ctx.moveTo(bPad.left, y);
        ctx.lineTo(bPad.left + bW, y);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText((i * 2).toString(), bPad.left - 6, y + 3);
      }

      // X-axis baseline
      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(bPad.left, bPad.top + bH);
      ctx.lineTo(bPad.left + bW, bPad.top + bH);
      ctx.stroke();

      const cationsList = ['Li', 'Na', 'K', 'Rb', 'Cs'];
      const barSlot = bW / cationsList.length;
      const barWidth = barSlot * 0.58;

      cationsList.forEach((k, idx) => {
        let lk = host.kMap[k] || 0.5;
        if (solvent === 'H2O') lk = Math.max(0.2, lk - 3.8);
        else if (solvent === 'MeCN') lk = lk + 0.8;

        const bx = bPad.left + idx * barSlot + (barSlot - barWidth) / 2;
        const bHeight = (lk / maxLogK) * bH;
        const by = bPad.top + bH - bHeight;

        const isCurrent = k === catKey;
        ctx.fillStyle = isCurrent ? '#7ee787' : '#388bfd';
        ctx.fillRect(bx, by, barWidth, bHeight);

        if (isCurrent) {
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 2;
          ctx.strokeRect(bx, by, barWidth, bHeight);
        }

        ctx.fillStyle = '#c9d1d9';
        ctx.font = isCurrent ? 'bold 11px sans-serif' : '11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(k + '⁺', bx + barWidth / 2, bPad.top + bH + 16);

        // Value on bar top
        ctx.fillStyle = isCurrent ? '#7ee787' : '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.fillText(lk.toFixed(1), bx + barWidth / 2, by - 5);
      });

      animAngle += 0.03;
      animId = requestAnimationFrame(render);
    }

    [hostSel, catSel, solvSel, tempSlider].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));
    render();
  }

  /* ==========================================================================
     SIMULATION 3: pH-Switchable Anion vs Cation Dual Receptor
     ========================================================================== */
  function sim_supra_anion_recognition_ph_switch(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 3: pH-Switchable Dual Anion / Cation Recognition</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Bis-Urea / Ammonium Switch</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Solution pH: <span id="u3-ph-val" style="color:#58a6ff; font-weight:bold;">3.50</span></label>
            <input type="range" id="u3-ph" min="1.0" max="13.0" step="0.25" value="3.5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Target Anion Substrate:</label>
            <select id="u3-anion" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="Cl" selected>Chloride (Cl⁻, r = 1.81 Å)</option>
              <option value="SO4">Sulfate (SO₄²⁻, r = 2.30 Å)</option>
              <option value="H2PO4">Phosphate (H₂PO₄⁻, tetrahedral)</option>
              <option value="F">Fluoride (F⁻, r = 1.33 Å)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Cation Co-Substrate:</label>
            <select id="u3-cation" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="K" selected>Potassium (K⁺)</option>
              <option value="Na">Sodium (Na⁺)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u3-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Receptor State: <strong id="u3-state" style="color:#7ee787;">Cationic Diprotonated [H₂R²⁺]</strong></span>
          <span>Anion Affinity: <strong id="u3-anion-k" style="color:#7ee787;">log Ka = 5.40 M⁻¹</strong></span>
          <span>Cation Affinity: <strong id="u3-cat-k" style="color:#8b949e;">Repelled (log Ka < 1)</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u3-canvas');
    const phSlider = el.querySelector('#u3-ph');
    const anionSel = el.querySelector('#u3-anion');
    const catSel = el.querySelector('#u3-cation');

    const phVal = el.querySelector('#u3-ph-val');
    const stateVal = el.querySelector('#u3-state');
    const anionKVal = el.querySelector('#u3-anion-k');
    const catKVal = el.querySelector('#u3-cat-k');

    let t = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const ph = parseFloat(phSlider.value);
      phVal.textContent = ph.toFixed(2);

      const pKa1 = 4.5;
      const pKa2 = 8.5;

      // Speciation fractions:
      // Acid: [H2R]2+ (pH < 4.5)
      // Neutral: [HR]+ / R (4.5 < pH < 8.5)
      // Base: [R-2H]2- (pH > 8.5)
      const hPlus = Math.pow(10, -ph);
      const K1 = Math.pow(10, -pKa1);
      const K2 = Math.pow(10, -pKa2);
      const denom = hPlus * hPlus + hPlus * K1 + K1 * K2;

      const fH2R = (hPlus * hPlus) / denom;
      const fHR = (hPlus * K1) / denom;
      const fR = (K1 * K2) / denom;

      let stateDesc = '';
      let logKAnion = 1.0;
      let logKCat = 1.0;

      if (fH2R > 0.6) {
        stateDesc = 'Cationic Diprotonated [H₂R]²⁺ (High Anion Binding)';
        logKAnion = 5.4;
        logKCat = 0.5;
      } else if (fR > 0.6) {
        stateDesc = 'Anionic Deprotonated [R]²⁻ (High Cation Binding)';
        logKAnion = 0.5;
        logKCat = 4.8;
      } else {
        stateDesc = 'Neutral Zwitterionic / Mono-protonated [HR] (Intermediate)';
        logKAnion = 3.2;
        logKCat = 2.1;
      }

      stateVal.textContent = stateDesc;
      anionKVal.textContent = 'log Ka = ' + logKAnion.toFixed(2);
      catKVal.textContent = logKCat > 1.5 ? ('log Ka = ' + logKCat.toFixed(2)) : 'Repelled (log Ka < 1)';

      ctx.clearRect(0, 0, W, H);

      // Split canvas: Left is molecular receptor diagram, Right is speciation vs pH curve
      const leftW = W * 0.55;
      const rightW = W - leftW;

      ctx.strokeStyle = '#21262d';
      ctx.beginPath();
      ctx.moveTo(leftW, 20);
      ctx.lineTo(leftW, H - 20);
      ctx.stroke();

      // Left visualization: Receptor with two arms
      const cx = leftW / 2;
      const cy = H / 2;

      // Electrostatic glow
      const glowGrad = ctx.createRadialGradient(cx, cy, 10, cx, cy, 90);
      if (fH2R > 0.5) {
        glowGrad.addColorStop(0, 'rgba(88, 166, 255, 0.35)'); // positive blue
        glowGrad.addColorStop(1, 'rgba(88, 166, 255, 0.0)');
      } else if (fR > 0.5) {
        glowGrad.addColorStop(0, 'rgba(248, 81, 73, 0.35)'); // negative red
        glowGrad.addColorStop(1, 'rgba(248, 81, 73, 0.0)');
      } else {
        glowGrad.addColorStop(0, 'rgba(126, 231, 135, 0.25)'); // neutral green
        glowGrad.addColorStop(1, 'rgba(126, 231, 135, 0.0)');
      }
      ctx.fillStyle = glowGrad;
      ctx.beginPath();
      ctx.arc(cx, cy, 90, 0, Math.PI * 2);
      ctx.fill();

      // Draw Receptor Body (anthracene or spacer core)
      ctx.fillStyle = '#30363d';
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.roundRect(cx - 35, cy - 20, 70, 40, 8);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#c9d1d9';
      ctx.font = 'bold 11px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('Receptor Core', cx, cy);

      // Left arm (Ammonium / Amine portal)
      const arm1X = cx - 75;
      const arm1Y = cy - 35;
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(cx - 35, cy - 10);
      ctx.lineTo(arm1X, arm1Y);
      ctx.stroke();

      ctx.fillStyle = fH2R > 0.5 ? '#58a6ff' : (fR > 0.5 ? '#f85149' : '#e3b341');
      ctx.beginPath();
      ctx.arc(arm1X, arm1Y, 14, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 10px sans-serif';
      ctx.fillText(fH2R > 0.5 ? 'NH₃⁺' : (fR > 0.5 ? 'COO⁻' : 'NH₂'), arm1X, arm1Y);

      // Right arm (Bis-urea H-bond donors)
      const arm2X = cx + 75;
      const arm2Y = cy - 35;
      ctx.beginPath();
      ctx.moveTo(cx + 35, cy - 10);
      ctx.lineTo(arm2X, arm2Y);
      ctx.stroke();

      ctx.fillStyle = fH2R > 0.5 ? '#58a6ff' : (fR > 0.5 ? '#f85149' : '#e3b341');
      ctx.beginPath();
      ctx.arc(arm2X, arm2Y, 14, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 10px sans-serif';
      ctx.fillText(fH2R > 0.5 ? 'NH₃⁺' : (fR > 0.5 ? 'COO⁻' : 'Urea'), arm2X, arm2Y);

      // Bound / Approaching Ion
      const isAnionBound = fH2R > 0.4;
      const isCatBound = fR > 0.6;

      if (isAnionBound) {
        // Draw bound Cl- or SO4(2-) in cavity center
        const ionY = cy - 45 + Math.sin(t * 3) * 3;
        ctx.fillStyle = '#7ee787';
        ctx.beginPath();
        ctx.arc(cx, ionY, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#010409';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText(anionSel.value === 'SO4' ? 'SO₄²⁻' : 'Cl⁻', cx, ionY);

        // Coordination H-bonds (dashed green)
        ctx.setLineDash([3, 3]);
        ctx.strokeStyle = '#7ee787';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(arm1X + 10, arm1Y);
        ctx.lineTo(cx - 12, ionY);
        ctx.moveTo(arm2X - 10, arm2Y);
        ctx.lineTo(cx + 12, ionY);
        ctx.stroke();
        ctx.setLineDash([]);
      } else if (isCatBound) {
        // Draw bound K+ in cavity center
        const ionY = cy - 45 + Math.sin(t * 3) * 3;
        ctx.fillStyle = '#f0883e';
        ctx.beginPath();
        ctx.arc(cx, ionY, 14, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#010409';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText(catSel.value + '⁺', cx, ionY);

        // Electrostatic cation chelate
        ctx.setLineDash([3, 3]);
        ctx.strokeStyle = '#f0883e';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(arm1X + 10, arm1Y);
        ctx.lineTo(cx - 10, ionY);
        ctx.moveTo(arm2X - 10, arm2Y);
        ctx.lineTo(cx + 10, ionY);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Electrostatic & H-Bonding Cavity', cx, H - 24);

      // Right: Speciation Diagram vs pH
      const sPad = { left: leftW + 45, right: 25, top: 40, bottom: 45 };
      const sW = W - sPad.left - sPad.right;
      const sH = H - sPad.top - sPad.bottom;

      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 12px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Receptor Speciation vs Solution pH', sPad.left, 24);

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let i = 0; i <= 4; i++) {
        const y = sPad.top + (sH * i) / 4;
        ctx.beginPath();
        ctx.moveTo(sPad.left, y);
        ctx.lineTo(sPad.left + sW, y);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText((100 - i * 25) + '%', sPad.left - 6, y + 3);
      }

      // X-axis (pH 1 to 13)
      for (let p = 2; p <= 12; p += 2) {
        const x = sPad.left + ((p - 1) / 12) * sW;
        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(p.toString(), x, sPad.top + sH + 15);
      }
      ctx.fillText('pH', sPad.left + sW / 2, sPad.top + sH + 32);

      // Draw H2R2+ curve (Blue)
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = 0; px <= sW; px++) {
        const curPh = 1 + (px / sW) * 12;
        const curH = Math.pow(10, -curPh);
        const curD = curH * curH + curH * K1 + K1 * K2;
        const f = (curH * curH) / curD;
        const cy = sPad.top + sH - f * sH;
        if (px === 0) ctx.moveTo(sPad.left + px, cy);
        else ctx.lineTo(sPad.left + px, cy);
      }
      ctx.stroke();

      // Draw R2- curve (Red)
      ctx.strokeStyle = '#f85149';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = 0; px <= sW; px++) {
        const curPh = 1 + (px / sW) * 12;
        const curH = Math.pow(10, -curPh);
        const curD = curH * curH + curH * K1 + K1 * K2;
        const f = (K1 * K2) / curD;
        const cy = sPad.top + sH - f * sH;
        if (px === 0) ctx.moveTo(sPad.left + px, cy);
        else ctx.lineTo(sPad.left + px, cy);
      }
      ctx.stroke();

      // Draw Current pH vertical indicator line
      const curLineX = sPad.left + ((ph - 1) / 12) * sW;
      ctx.strokeStyle = '#e3b341';
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(curLineX, sPad.top);
      ctx.lineTo(curLineX, sPad.top + sH);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#e3b341';
      ctx.font = 'bold 11px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('pH ' + ph.toFixed(1), curLineX, sPad.top - 6);

      // Legend
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('[H₂R]²⁺ (Anion host)', sPad.left + 50, sPad.top + 20);
      ctx.fillStyle = '#f85149';
      ctx.fillText('[R]²⁻ (Cation host)', sPad.left + sW - 55, sPad.top + 20);

      t += 0.04;
      animId = requestAnimationFrame(render);
    }

    [phSlider, anionSel, catSel].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));
    render();
  }

  /* ==========================================================================
     SIMULATION 4: Bistable [2]Rotaxane Molecular Shuttle & Brownian Machine
     ========================================================================== */
  function sim_supra_rotaxane_molecular_shuttle(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 4: Bistable [2]Rotaxane Molecular Shuttle & Energy Ratchet</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Stoddart 2016 Nobel Model</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">TTF Station Redox State:</label>
            <select id="u4-redox" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="neutral" selected>Neutral: TTF⁰ (Strong π-donor)</option>
              <option value="ox1">Oxidized: TTF⁺• (+1 Monocation)</option>
              <option value="ox2">Fully Oxidized: TTF²⁺ (+2 Dication)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Thermal Energy (kBT): <span id="u4-temp-val" style="color:#58a6ff; font-weight:bold;">298 K</span></label>
            <input type="range" id="u4-temp" min="200" max="400" step="10" value="298" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Polyether Spacer Length: <span id="u4-len-val" style="color:#58a6ff; font-weight:bold;">Normal (3.2 nm)</span></label>
            <input type="range" id="u4-len" min="1" max="3" step="1" value="2" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u4-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Preferred Station: <strong id="u4-station" style="color:#7ee787;">Station 1: TTF⁰ (99.7% Occupancy)</strong></span>
          <span>Shuttling Frequency: <strong id="u4-freq" style="color:#7ee787;">ν ≈ 140 Hz</strong></span>
          <span>Switching Barrier: <strong id="u4-barrier" style="color:#7ee787;">ΔG‡ = 62.5 kJ/mol</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u4-canvas');
    const redoxSel = el.querySelector('#u4-redox');
    const tempSlider = el.querySelector('#u4-temp');
    const lenSlider = el.querySelector('#u4-len');

    const tempVal = el.querySelector('#u4-temp-val');
    const stationVal = el.querySelector('#u4-station');
    const freqVal = el.querySelector('#u4-freq');
    const barrierVal = el.querySelector('#u4-barrier');

    // Ring position along coordinate x in [-1, 1] (-1: TTF, +1: DNP)
    let ringX = -1.0;
    let ringVx = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const redox = redoxSel.value;
      const temp = parseFloat(tempSlider.value);
      tempVal.textContent = temp + ' K';

      // Free energy minimum coordinates:
      // When neutral: TTF is deep minimum (-15 kJ/mol), DNP is higher (-4 kJ/mol). Target = -1
      // When ox1: TTF has positive repulsion (+8 kJ/mol), DNP is deep minimum. Target = +1
      // When ox2: TTF has severe repulsion (+25 kJ/mol). Target = +1
      let targetX = -1.0;
      let dG0 = -14.0; // kJ/mol (favoring TTF)
      let barrier = 62.0;

      if (redox === 'ox1') {
        targetX = 1.0;
        dG0 = +16.0; // favoring DNP
        barrier = 54.0;
        stationVal.textContent = 'Station 2: DNP (99.2% Occupancy, Electrostatic Repulsion)';
      } else if (redox === 'ox2') {
        targetX = 1.0;
        dG0 = +32.0;
        barrier = 48.0;
        stationVal.textContent = 'Station 2: DNP (>99.9% Occupancy, Coulombic Ejection)';
      } else {
        stationVal.textContent = 'Station 1: TTF⁰ (99.7% Occupancy, Strong π-Donation)';
      }

      barrierVal.textContent = 'ΔG‡ = ' + barrier.toFixed(1) + ' kJ/mol';

      // Shuttling frequency estimation: nu = (kBT/h) exp(-barrier/RT)
      const freq = (1.38e-23 * temp / 6.63e-34) * Math.exp(-barrier * 1e3 / (8.314 * temp));
      freqVal.textContent = 'ν ≈ ' + (freq > 1e4 ? freq.toExponential(1) : freq.toFixed(0)) + ' Hz';

      // Brownian dynamic update of ringX
      const dt = 0.02;
      const kBT = (temp / 298.0) * 0.45;
      const force = -2.5 * (ringX - targetX); // restoring force to target well
      const randomKick = (Math.random() - 0.5) * Math.sqrt(kBT) * 2.8;

      ringVx = (ringVx + force * dt + randomKick) * 0.88; // friction damping
      ringX += ringVx * dt;
      // Clamp between stoppers
      ringX = Math.max(-1.15, Math.min(1.15, ringX));

      ctx.clearRect(0, 0, W, H);

      // Top half (H * 0.55): Molecular rotaxane dumbbell
      // Bottom half: Free energy potential well diagram G(x)
      const shaftY = H * 0.28;
      const shaftStartX = W * 0.15;
      const shaftEndX = W * 0.85;
      const shaftLength = shaftEndX - shaftStartX;

      const ttfX = shaftStartX + shaftLength * 0.22;
      const dnpX = shaftStartX + shaftLength * 0.78;

      // Draw Dumbbell Shaft
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 6;
      ctx.beginPath();
      ctx.moveTo(shaftStartX, shaftY);
      ctx.lineTo(shaftEndX, shaftY);
      ctx.stroke();

      // Bulky Terminal Stoppers (Triisopropylsilyl / tetraarylmethane)
      ctx.fillStyle = '#f0883e';
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      // Left stopper
      ctx.beginPath();
      ctx.arc(shaftStartX, shaftY, 22, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = '#010409';
      ctx.font = 'bold 10px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('STOP', shaftStartX, shaftY);

      // Right stopper
      ctx.fillStyle = '#f0883e';
      ctx.beginPath();
      ctx.arc(shaftEndX, shaftY, 22, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = '#010409';
      ctx.fillText('STOP', shaftEndX, shaftY);

      // Station 1: TTF (green if neutral, yellow/red if oxidized)
      let ttfColor = '#7ee787';
      if (redox === 'ox1') ttfColor = '#e3b341';
      else if (redox === 'ox2') ttfColor = '#f85149';

      ctx.fillStyle = ttfColor;
      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(ttfX - 28, shaftY - 14, 56, 28, 6);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = '#010409';
      ctx.font = 'bold 11px sans-serif';
      ctx.fillText(redox === 'neutral' ? 'TTF⁰' : (redox === 'ox1' ? 'TTF⁺•' : 'TTF²⁺'), ttfX, shaftY);

      // Station 2: DNP (Blue dioxynaphthalene)
      ctx.fillStyle = '#388bfd';
      ctx.beginPath();
      ctx.roundRect(dnpX - 28, shaftY - 14, 56, 28, 6);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = '#ffffff';
      ctx.fillText('DNP', dnpX, shaftY);

      // Calculate current ring position on screen
      // ringX = -1 maps to ttfX, ringX = +1 maps to dnpX
      const ringScreenX = ((ringX + 1.0) / 2.0) * (dnpX - ttfX) + ttfX;

      // Draw CBPQT(4+) "Blue Box" Macrocycle
      ctx.strokeStyle = '#58a6ff';
      ctx.fillStyle = 'rgba(88, 166, 255, 0.40)';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.roundRect(ringScreenX - 22, shaftY - 38, 44, 76, 10);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 10px sans-serif';
      ctx.fillText('CBPQT⁴⁺', ringScreenX, shaftY - 44);

      // Bottom Half: Potential Energy Well Landscape G(x)
      const pTop = H * 0.60;
      const pBottom = H * 0.90;
      const pH = pBottom - pTop;

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Free Energy Potential Landscape G(x)', shaftStartX, pTop - 8);

      ctx.beginPath();
      ctx.strokeStyle = '#7ee787';
      ctx.lineWidth = 2.5;

      for (let px = 0; px <= shaftLength; px++) {
        const xCoord = ((px / shaftLength) - 0.5) * 3.0; // [-1.5, 1.5]
        // Double well potential with bias
        // V(x) = (x^2 - 1)^2 + bias * x
        const bias = (targetX > 0) ? -0.8 : 0.8;
        const pot = Math.pow(xCoord * xCoord - 1.0, 2) + bias * xCoord;
        // Scale pot to screen
        const sy = pBottom - ((pot + 1.2) / 4.5) * pH;

        const sx = shaftStartX + px;
        if (px === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Draw red dot representing the macrocycle on the energy curve
      const potCurrent = Math.pow(ringX * ringX - 1.0, 2) + ((targetX > 0) ? -0.8 : 0.8) * ringX;
      const dotSy = pBottom - ((potCurrent + 1.2) / 4.5) * pH;
      ctx.fillStyle = '#f85149';
      ctx.beginPath();
      ctx.arc(ringScreenX, dotSy, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      animId = requestAnimationFrame(render);
    }

    [redoxSel, tempSlider, lenSlider].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));
    render();
  }

  /* ==========================================================================
     SIMULATION 5: Cyclodextrin Cavity Inclusion & Hydrophobic Expulsion
     ========================================================================== */
  function sim_supra_cyclodextrin_inclusion(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 5: Cyclodextrin Cavity Inclusion & High-Energy Water Expulsion</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Hydrophobic Torus</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Host Cyclodextrin:</label>
            <select id="u5-cd" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="alpha">α-Cyclodextrin (6 Glucose, d = 5.0 Å)</option>
              <option value="beta" selected>β-Cyclodextrin (7 Glucose, d = 6.2 Å)</option>
              <option value="gamma">γ-Cyclodextrin (8 Glucose, d = 7.9 Å)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Organic Guest Molecule:</label>
            <select id="u5-guest" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="toluene">Toluene (d = 4.8 Å, linear fit)</option>
              <option value="adamantane" selected>Adamantane-1-carboxylate (d = 6.4 Å)</option>
              <option value="cholesterol">Cholesterol (d = 7.5 Å, bulky)</option>
              <option value="c60">[60]Fullerene (d = 10.1 Å, large)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Inclusion Progress: <span id="u5-prog-val" style="color:#58a6ff; font-weight:bold;">Docked (100%)</span></label>
            <input type="range" id="u5-prog" min="0" max="100" step="1" value="100" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u5-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Binding Affinity: <strong id="u5-ka" style="color:#7ee787;">Ka = 3.20 × 10⁵ M⁻¹</strong></span>
          <span>Enthalpy Release: <strong id="u5-dh" style="color:#7ee787;">ΔH° = -22.4 kJ/mol</strong></span>
          <span>Entropy Gain: <strong id="u5-ds" style="color:#7ee787;">TΔS° = +9.0 kJ/mol</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u5-canvas');
    const cdSel = el.querySelector('#u5-cd');
    const guestSel = el.querySelector('#u5-guest');
    const progSlider = el.querySelector('#u5-prog');

    const progVal = el.querySelector('#u5-prog-val');
    const kaVal = el.querySelector('#u5-ka');
    const dhVal = el.querySelector('#u5-dh');
    const dsVal = el.querySelector('#u5-ds');

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const cdType = cdSel.value;
      const guestType = guestSel.value;
      const prog = parseFloat(progSlider.value) * 0.01; // 0 (separated) to 1 (docked)

      progVal.textContent = (prog * 100).toFixed(0) + '%';

      // CD Cavity dimension parameters
      let dCavity = 6.2; // Angstrom
      let glucoseUnits = 7;
      if (cdType === 'alpha') { dCavity = 5.0; glucoseUnits = 6; }
      else if (cdType === 'gamma') { dCavity = 7.9; glucoseUnits = 8; }

      // Guest parameters
      let dGuest = 6.4;
      let gName = 'Adamantane';
      let gColor = '#7ee787';
      if (guestType === 'toluene') { dGuest = 4.8; gName = 'Toluene'; gColor = '#58a6ff'; }
      else if (guestType === 'cholesterol') { dGuest = 7.5; gName = 'Cholesterol'; gColor = '#f0883e'; }
      else if (guestType === 'c60') { dGuest = 10.1; gName = '[60]Fullerene'; gColor = '#d2a8ff'; }

      // Fit calculation
      const mismatch = Math.abs(dGuest - dCavity);
      let Ka = 100;
      let dH = -10.0;
      let TdS = +4.0;

      if (mismatch < 0.6) {
        Ka = 3.2e5; dH = -22.4; TdS = +9.0;
      } else if (dGuest < dCavity) {
        Ka = 4.5e2; dH = -8.5; TdS = -2.0;
      } else {
        Ka = 15.0; dH = +5.0; TdS = -12.0; // severe steric clash
      }

      kaVal.textContent = 'Ka = ' + Ka.toExponential(2) + ' M⁻¹';
      dhVal.textContent = 'ΔH° = ' + dH.toFixed(1) + ' kJ/mol';
      dsVal.textContent = 'TΔS° = ' + (TdS > 0 ? '+' : '') + TdS.toFixed(1) + ' kJ/mol';

      ctx.clearRect(0, 0, W, H);

      const cx = W * 0.38;
      const cy = H * 0.60;

      // Draw Truncated Cone Torus (Side projection of Cyclodextrin)
      const topWidth = dCavity * 24 + 50; // Secondary rim (wider)
      const bottomWidth = dCavity * 20 + 35; // Primary rim (narrower)
      const torusH = 90;

      // Outer Torus Wall
      ctx.fillStyle = '#161b22';
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 3;

      ctx.beginPath();
      ctx.moveTo(cx - topWidth / 2, cy - torusH / 2);
      ctx.lineTo(cx + topWidth / 2, cy - torusH / 2);
      ctx.lineTo(cx + bottomWidth / 2, cy + torusH / 2);
      ctx.lineTo(cx - bottomWidth / 2, cy + torusH / 2);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Secondary Rim Hydroxyls (Top rim)
      ctx.fillStyle = '#f85149';
      for (let i = 0; i <= glucoseUnits; i++) {
        const x = cx - topWidth / 2 + (topWidth / glucoseUnits) * i;
        ctx.beginPath();
        ctx.arc(x, cy - torusH / 2, 5, 0, Math.PI * 2);
        ctx.fill();
      }

      // Primary Rim Hydroxyls (Bottom rim)
      for (let i = 0; i <= glucoseUnits; i++) {
        const x = cx - bottomWidth / 2 + (bottomWidth / glucoseUnits) * i;
        ctx.beginPath();
        ctx.arc(x, cy + torusH / 2, 4, 0, Math.PI * 2);
        ctx.fill();
      }

      // Cavity Hydrophobic Interior
      ctx.fillStyle = 'rgba(88, 166, 255, 0.12)';
      ctx.beginPath();
      ctx.moveTo(cx - (dCavity * 12), cy - torusH / 2);
      ctx.lineTo(cx + (dCavity * 12), cy - torusH / 2);
      ctx.lineTo(cx + (dCavity * 10), cy + torusH / 2);
      ctx.lineTo(cx - (dCavity * 10), cy + torusH / 2);
      ctx.closePath();
      ctx.fill();

      // Guest Position: Interpolate from above (cy - 140) to inside cavity (cy)
      const guestStartY = cy - 140;
      const guestFinalY = cy;
      const curGuestY = guestStartY + (guestFinalY - guestStartY) * prog;
      const guestRadiusPx = dGuest * 6.5;

      // Draw High-Energy Cavity Water molecules (expelled as prog increases)
      const numWaters = 5;
      for (let i = 0; i < numWaters; i++) {
        const ang = (i / numWaters) * Math.PI * 2;
        // If docked (prog high), waters fly out away into bulk
        const flyDist = prog * 85;
        const wx = cx + Math.cos(ang) * (18 + flyDist);
        const wy = (cy - 10) + Math.sin(ang) * (14 + flyDist * 0.7);

        ctx.fillStyle = '#388bfd';
        ctx.beginPath();
        ctx.arc(wx, wy, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = '8px sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('H₂O', wx, wy);
      }

      // Draw Guest Molecule
      ctx.fillStyle = gColor;
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(cx, curGuestY, guestRadiusPx, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#010409';
      ctx.font = 'bold 11px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(gName, cx, curGuestY);

      // Labels on left
      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Secondary Rim (C₂-OH, C₃-OH)', cx, cy - torusH / 2 - 12);
      ctx.fillText('Primary Rim (C₆-OH)', cx, cy + torusH / 2 + 18);

      // Right half: Thermodynamic Driving Force Breakdown
      const rLeft = W * 0.68;
      const rTop = 50;

      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 13px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Thermodynamic Driving Forces', rLeft, rTop);

      ctx.font = '11px sans-serif';
      ctx.fillStyle = '#c9d1d9';
      ctx.fillText('1. Expulsion of High-Energy Cavity Water', rLeft, rTop + 30);
      ctx.fillStyle = '#7ee787';
      ctx.fillText('   -> ΔH_water < 0 (Enthalpically favored)', rLeft, rTop + 46);

      ctx.fillStyle = '#c9d1d9';
      ctx.fillText('2. Hydrophobic Solvation Release', rLeft, rTop + 75);
      ctx.fillStyle = '#7ee787';
      ctx.fillText('   -> TΔS_desolv > 0 (Entropy gain)', rLeft, rTop + 91);

      ctx.fillStyle = '#c9d1d9';
      ctx.fillText('3. van der Waals / Dispersion Matching', rLeft, rTop + 120);
      ctx.fillStyle = mismatch < 0.6 ? '#7ee787' : '#f85149';
      ctx.fillText('   -> ' + (mismatch < 0.6 ? 'Optimal Contact (+)' : 'Steric Clash / Loose fit (-)'), rLeft, rTop + 136);

      // Total binding free energy bar
      const dG = dH - TdS;
      ctx.fillStyle = '#30363d';
      ctx.fillRect(rLeft, rTop + 175, 180, 24);
      const barW = Math.min(180, Math.max(0, -dG * 5.0));
      ctx.fillStyle = dG < 0 ? '#7ee787' : '#f85149';
      ctx.fillRect(rLeft, rTop + 175, barW, 24);

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 11px sans-serif';
      ctx.fillText('ΔG° = ' + dG.toFixed(1) + ' kJ/mol', rLeft + 10, rTop + 191);
    }

    [cdSel, guestSel, progSlider].forEach(s => s.addEventListener('input', render));
    render();
  }

  /* ==========================================================================
     SIMULATION 6: Collman's Picket-Fence Porphyrin Reversible O2 Binding
     ========================================================================== */
  function sim_supra_picket_fence_porphyrin(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 6: Collman Picket-Fence Porphyrin vs μ-Oxo Dimerization</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Biomimetic Model</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Porphyrin Architecture:</label>
            <select id="u6-arch" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="picket" selected>Collman Picket-Fence (Protected)</option>
              <option value="flat">Unhindered Flat Fe(TPP) (Prone to Dimerization)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Oxygen Pressure P_O₂ (torr): <span id="u6-po2-val" style="color:#58a6ff; font-weight:bold;">38 torr</span></label>
            <input type="range" id="u6-po2" min="0" max="250" step="2" value="38" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Trace CO Pressure (torr): <span id="u6-pco-val" style="color:#58a6ff; font-weight:bold;">0.00 torr</span></label>
            <input type="range" id="u6-pco" min="0" max="2.0" step="0.05" value="0.0" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u6-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Fraction Oxygenated (Y_O₂): <strong id="u6-yo2" style="color:#7ee787;">50.0% (P₁/₂ = 38 torr)</strong></span>
          <span>Dimerization Status: <strong id="u6-dimer" style="color:#7ee787;">Zero Dimerization (Protected)</strong></span>
          <span>Binding Mode: <strong id="u6-mode" style="color:#7ee787;">End-on Bent Fe-O-O (∠115°)</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u6-canvas');
    const archSel = el.querySelector('#u6-arch');
    const po2Slider = el.querySelector('#u6-po2');
    const pcoSlider = el.querySelector('#u6-pco');

    const po2Val = el.querySelector('#u6-po2-val');
    const pcoVal = el.querySelector('#u6-pco-val');
    const yo2Val = el.querySelector('#u6-yo2');
    const dimerVal = el.querySelector('#u6-dimer');
    const modeVal = el.querySelector('#u6-mode');

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const arch = archSel.value;
      const po2 = parseFloat(po2Slider.value);
      const pco = parseFloat(pcoSlider.value);

      po2Val.textContent = po2 + ' torr';
      pcoVal.textContent = pco.toFixed(2) + ' torr';

      // P1/2 for O2 in Picket-fence is ~38 torr
      // In flat porphyrin, irreversible dimerization occurs rapidly!
      let yo2 = 0;
      let yco = 0;

      if (arch === 'picket') {
        const kO2 = 1.0 / 38.0; // torr^-1
        const kCO = 20.0 * kO2; // partition M ~ 20 in pocket
        const denom = 1.0 + kO2 * po2 + kCO * pco;
        yo2 = (kO2 * po2) / denom;
        yco = (kCO * pco) / denom;

        yo2Val.textContent = (yo2 * 100).toFixed(1) + '% (Active reversible carrier)';
        dimerVal.textContent = 'Zero Dimerization (Picket Barrier Active)';
        dimerVal.style.color = '#7ee787';
        modeVal.textContent = 'End-on Bent Fe-O-O (∠115° Reversible)';
      } else {
        // Flat porphyrin destroys itself into mu-oxo dimer
        yo2Val.textContent = '0.0% (Inactivated)';
        dimerVal.textContent = 'CRITICAL: Rapid μ-Oxo Dimer (Fe-O-Fe) Degradation!';
        dimerVal.style.color = '#f85149';
        modeVal.textContent = 'Antiferromagnetic Inactive Fe-O-Fe Linear Bridge';
      }

      ctx.clearRect(0, 0, W, H);

      // Left: Molecular structural cross-section
      // Right: Saturation binding isotherm Y_O2 vs P_O2
      const leftW = W * 0.52;

      ctx.strokeStyle = '#21262d';
      ctx.beginPath();
      ctx.moveTo(leftW, 20);
      ctx.lineTo(leftW, H - 20);
      ctx.stroke();

      const cx = leftW / 2;
      const cy = H * 0.58;

      if (arch === 'picket') {
        // Flat porphyrin plane
        ctx.fillStyle = '#30363d';
        ctx.strokeStyle = '#8b949e';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.roundRect(cx - 90, cy, 180, 16, 4);
        ctx.fill();
        ctx.stroke();

        // Central Iron Atom
        ctx.fillStyle = '#f0883e';
        ctx.beginPath();
        ctx.arc(cx, cy + 8, 12, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#010409';
        ctx.font = 'bold 10px sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('Feᴵᴵ', cx, cy + 8);

        // Proximal 1,2-dimethylimidazole below
        ctx.fillStyle = '#58a6ff';
        ctx.beginPath();
        ctx.roundRect(cx - 16, cy + 24, 32, 28, 4);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = '9px sans-serif';
        ctx.fillText('Base', cx, cy + 38);

        // Four Pivalamide Pickets protruding upward
        const pickets = [cx - 75, cx - 35, cx + 35, cx + 75];
        pickets.forEach((px) => {
          ctx.fillStyle = '#7ee787';
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.roundRect(px - 14, cy - 70, 28, 70, 6);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = '#010409';
          ctx.font = 'bold 9px sans-serif';
          ctx.fillText('t-Bu', px, cy - 35);
        });

        // Coordinated O2 inside pocket (if po2 > 5)
        if (po2 > 5) {
          // Fe-O-O bent geometry
          ctx.strokeStyle = '#f85149';
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.moveTo(cx, cy);
          ctx.lineTo(cx + 8, cy - 25);
          ctx.lineTo(cx + 26, cy - 38);
          ctx.stroke();

          // Two oxygen spheres
          ctx.fillStyle = '#f85149';
          ctx.beginPath();
          ctx.arc(cx + 8, cy - 25, 8, 0, Math.PI * 2);
          ctx.arc(cx + 26, cy - 38, 8, 0, Math.PI * 2);
          ctx.fill();
        }

        ctx.fillStyle = '#7ee787';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Protected Hydrophobic Binding Cleft (5.0 Å)', cx, 30);

      } else {
        // Flat porphyrin showing bimolecular mu-oxo dimer
        // Two horizontal porphyrin planes bridged by oxygen
        ctx.fillStyle = '#30363d';
        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 4;

        // Top porphyrin
        ctx.beginPath();
        ctx.roundRect(cx - 85, cy - 45, 170, 14, 4);
        ctx.fill();
        ctx.stroke();

        // Bottom porphyrin
        ctx.beginPath();
        ctx.roundRect(cx - 85, cy + 35, 170, 14, 4);
        ctx.fill();
        ctx.stroke();

        // Fe-O-Fe linear bridge
        ctx.fillStyle = '#f0883e';
        ctx.beginPath();
        ctx.arc(cx, cy - 38, 10, 0, Math.PI * 2); // Top Fe
        ctx.arc(cx, cy + 42, 10, 0, Math.PI * 2); // Bottom Fe
        ctx.fill();

        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(cx, cy - 38);
        ctx.lineTo(cx, cy + 42);
        ctx.stroke();

        // Central bridging oxygen
        ctx.fillStyle = '#f85149';
        ctx.beginPath();
        ctx.arc(cx, cy + 2, 9, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 9px sans-serif';
        ctx.fillText('O', cx, cy + 2);

        ctx.fillStyle = '#f85149';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Irreversible μ-Oxo Dimer: Feᴵᴵᴵ-O-Feᴵᴵᴵ (Dead)', cx, 30);
      }

      // Right half: Oxygen binding isotherm curve
      const rPad = { left: leftW + 45, right: 25, top: 40, bottom: 45 };
      const rW = W - rPad.left - rPad.right;
      const rH = H - rPad.top - rPad.bottom;

      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 12px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('O₂ Saturation Isotherm Y_O₂ vs P_O₂', rPad.left, 24);

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let i = 0; i <= 4; i++) {
        const y = rPad.top + (rH * i) / 4;
        ctx.beginPath();
        ctx.moveTo(rPad.left, y);
        ctx.lineTo(rPad.left + rW, y);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText((100 - i * 25) + '%', rPad.left - 6, y + 3);
      }

      for (let p = 50; p <= 250; p += 50) {
        const x = rPad.left + (p / 250) * rW;
        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(p.toString(), x, rPad.top + rH + 15);
      }
      ctx.fillText('Oxygen Partial Pressure P_O₂ (torr)', rPad.left + rW / 2, rPad.top + rH + 32);

      if (arch === 'picket') {
        // Draw hyperbolic Langmuir saturation curve
        ctx.strokeStyle = '#7ee787';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let px = 0; px <= rW; px++) {
          const curP = (px / rW) * 250.0;
          const kO2 = 1.0 / 38.0;
          const curY = (kO2 * curP) / (1.0 + kO2 * curP);
          const cy = rPad.top + rH - curY * rH;
          if (px === 0) ctx.moveTo(rPad.left + px, cy);
          else ctx.lineTo(rPad.left + px, cy);
        }
        ctx.stroke();

        // Operating point dot
        const dotX = rPad.left + (po2 / 250) * rW;
        const dotY = rPad.top + rH - yo2 * rH;
        ctx.fillStyle = '#f0883e';
        ctx.beginPath();
        ctx.arc(dotX, dotY, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      } else {
        // Flat line at 0%
        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(rPad.left, rPad.top + rH);
        ctx.lineTo(rPad.left + rW, rPad.top + rH);
        ctx.stroke();
      }
    }

    [archSel, po2Slider, pcoSlider].forEach(s => s.addEventListener('input', render));
    render();
  }

  /* ==========================================================================
     SIMULATION 7: Self-Assembly of Helicates & Fujita Molecular Squares
     ========================================================================== */
  function sim_supra_helicate_cage_assembly(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 7: Directional Bonding Self-Assembly: Fujita Squares & Cages</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Enthalpic Ring Closure</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Assembly Architecture:</label>
            <select id="u7-arch" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="square" selected>Fujita Molecular Square [M₄L₄]⁸⁺</option>
              <option value="helicate">Lehn Double Helicate [Cu₂L₂]²⁺</option>
              <option value="octahedron">Fujita Octahedral Cage [M₆L₄]¹²⁺</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Dynamic Reversibility (Error Correction): <span id="u7-rev-val" style="color:#58a6ff; font-weight:bold;">High (95%)</span></label>
            <input type="range" id="u7-rev" min="10" max="100" step="5" value="95" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Simulation Control:</label>
            <button id="u7-reset" style="width:100%; background:#238636; color:#ffffff; border:none; border-radius:4px; padding:6px; font-weight:bold; cursor:pointer;">Thermal Anneal (Reset)</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u7-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Thermodynamic Yield: <strong id="u7-yield" style="color:#7ee787;">99.4% Discrete Monodisperse Assembly</strong></span>
          <span>Angle Matching: <strong id="u7-angle" style="color:#7ee787;">90° cis-Pd(II) + 180° 4,4'-bpy</strong></span>
          <span>Proofreading: <strong id="u7-proof" style="color:#7ee787;">Active Dynamic Error-Checking</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u7-canvas');
    const archSel = el.querySelector('#u7-arch');
    const revSlider = el.querySelector('#u7-rev');
    const resetBtn = el.querySelector('#u7-reset');

    const revVal = el.querySelector('#u7-rev-val');
    const yieldVal = el.querySelector('#u7-yield');
    const angleVal = el.querySelector('#u7-angle');

    let animAngle = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const arch = archSel.value;
      const reversibility = parseFloat(revSlider.value);
      revVal.textContent = reversibility + '%';

      yieldVal.textContent = (reversibility > 80 ? '99.4%' : (reversibility > 40 ? '78.2%' : '35.0%')) + ' Closed Product';

      if (arch === 'square') {
        angleVal.textContent = '90° cis-Pd(II) + 180° 4,4\'-bpy';
      } else if (arch === 'helicate') {
        angleVal.textContent = 'Tetrahedral Cu(I) (90° twist per step)';
      } else {
        angleVal.textContent = '90° cis-capped vertices + 120° tritopic triazine';
      }

      ctx.clearRect(0, 0, W, H);

      const cx = W / 2;
      const cy = H / 2;

      ctx.save();
      ctx.translate(cx, cy);

      if (arch === 'square') {
        // Draw 4 corners (90 deg Pd(en) vertices) and 4 linear edges (4,4'-bpy)
        const sqSize = 85;
        const corners = [
          { x: -sqSize, y: -sqSize },
          { x:  sqSize, y: -sqSize },
          { x:  sqSize, y:  sqSize },
          { x: -sqSize, y:  sqSize }
        ];

        // Rotation
        ctx.rotate(animAngle * 0.15);

        // Draw 4 bridging rods (bpy)
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 6;
        for (let i = 0; i < 4; i++) {
          const c1 = corners[i];
          const c2 = corners[(i + 1) % 4];
          ctx.beginPath();
          ctx.moveTo(c1.x, c1.y);
          ctx.lineTo(c2.x, c2.y);
          ctx.stroke();

          // Pyridyl rings on rod
          const midX = (c1.x + c2.x) / 2;
          const midY = (c1.y + c2.y) / 2;
          ctx.fillStyle = '#388bfd';
          ctx.beginPath();
          ctx.arc(midX, midY, 8, 0, Math.PI * 2);
          ctx.fill();
        }

        // Draw 4 cis-Pd(II) corner vertices (yellow squares with 90 degree coordinate arcs)
        corners.forEach((c) => {
          ctx.fillStyle = '#f0883e';
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.arc(c.x, c.y, 14, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = '#010409';
          ctx.font = 'bold 9px sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText('Pdᴵᴵ', c.x, c.y);
        });

        // Enclosed Cavity Guest (e.g. aromatic guest)
        ctx.fillStyle = 'rgba(126, 231, 135, 0.25)';
        ctx.beginPath();
        ctx.roundRect(-45, -45, 90, 90, 8);
        ctx.fill();

        ctx.fillStyle = '#7ee787';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Cavity 8 × 8 Å', 0, 0);

      } else if (arch === 'helicate') {
        // Draw Lehn Double Helicate: Two helical strands wrapping 2 or 3 Cu(I) centers
        ctx.rotate(animAngle * 0.1);
        const numCu = 3;
        const spacing = 80;

        // Draw Cu(I) centers along central axis
        for (let i = -1; i <= 1; i++) {
          const y = i * spacing;
          ctx.fillStyle = '#f85149';
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.arc(0, y, 12, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = '#ffffff';
          ctx.font = 'bold 9px sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText('Cuᴵ', 0, y);
        }

        // Draw Two intertwining sinusoidal strands
        for (let strand = 0; strand < 2; strand++) {
          const phase = strand * Math.PI;
          ctx.strokeStyle = strand === 0 ? '#58a6ff' : '#7ee787';
          ctx.lineWidth = 4;
          ctx.beginPath();
          for (let y = -120; y <= 120; y += 4) {
            const x = Math.sin((y / 45) + phase) * 48;
            if (y === -120) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
          }
          ctx.stroke();
        }

      } else {
        // Fujita Octahedral Cage [M6L4]
        ctx.rotate(animAngle * 0.2);
        // Draw 3D projection of octahedron with 6 vertices
        const rOct = 90;
        const v = [
          { x: 0, y: -rOct },
          { x: 0, y: rOct },
          { x: -rOct * 0.85, y: -rOct * 0.25 },
          { x: rOct * 0.85, y: -rOct * 0.25 },
          { x: -rOct * 0.55, y: rOct * 0.45 },
          { x: rOct * 0.55, y: rOct * 0.45 }
        ];

        // Draw triangular faces (triazine ligands)
        ctx.fillStyle = 'rgba(88, 166, 255, 0.25)';
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 2;

        const faces = [
          [0, 2, 3], [0, 4, 5], [1, 2, 4], [1, 3, 5]
        ];

        faces.forEach(f => {
          ctx.beginPath();
          ctx.moveTo(v[f[0]].x, v[f[0]].y);
          ctx.lineTo(v[f[1]].x, v[f[1]].y);
          ctx.lineTo(v[f[2]].x, v[f[2]].y);
          ctx.closePath();
          ctx.fill();
          ctx.stroke();
        });

        // Vertices
        v.forEach(pt => {
          ctx.fillStyle = '#f0883e';
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, 8, 0, Math.PI * 2);
          ctx.fill();
        });

        ctx.fillStyle = '#7ee787';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('[Pd₆(TPT)₄]¹²⁺ Octahedron', 0, 0);
      }

      ctx.restore();

      animAngle += 0.04;
      animId = requestAnimationFrame(render);
    }

    [archSel, revSlider].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));
    resetBtn.addEventListener('click', () => {
      animAngle = 0;
      cancelAnimationFrame(animId);
      render();
    });
    render();
  }

  /* ==========================================================================
     SIMULATION 8: Surfactant Critical Micelle Concentration & Packing Parameter
     ========================================================================== */
  function sim_supra_micelle_packing_cmc(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 8: Surfactant CMC & Critical Packing Parameter (P)</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Israelachvili / Tanford Model</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Surfactant Conc: <span id="u8-conc-val" style="color:#58a6ff; font-weight:bold;">12.0 mM</span> (CMC = 8.2 mM)</label>
            <input type="range" id="u8-conc" min="0.5" max="30.0" step="0.5" value="12.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Hydrocarbon Tail Length (n_c): <span id="u8-nc-val" style="color:#58a6ff; font-weight:bold;">12 (Dodecyl)</span></label>
            <input type="range" id="u8-nc" min="8" max="18" step="2" value="12" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Added Salt [NaCl] (mM): <span id="u8-salt-val" style="color:#58a6ff; font-weight:bold;">50 mM</span></label>
            <input type="range" id="u8-salt" min="0" max="300" step="10" value="50" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Chains per Monomer:</label>
            <select id="u8-chains" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="1" selected>Single-Chain Surfactant (SDS-like)</option>
              <option value="2">Double-Chain Lipid (Phospholipid / Vesicle)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u8-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Packing Parameter: <strong id="u8-p" style="color:#7ee787;">P = 0.35 (Spherical Micelle)</strong></span>
          <span>Surface Tension: <strong id="u8-gamma" style="color:#7ee787;">γ = 36.5 mN/m (Plateau)</strong></span>
          <span>Micelle Aggregation Number: <strong id="u8-nagg" style="color:#7ee787;">N_agg ≈ 62</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u8-canvas');
    const concSlider = el.querySelector('#u8-conc');
    const ncSlider = el.querySelector('#u8-nc');
    const saltSlider = el.querySelector('#u8-salt');
    const chainsSel = el.querySelector('#u8-chains');

    const concVal = el.querySelector('#u8-conc-val');
    const ncVal = el.querySelector('#u8-nc-val');
    const saltVal = el.querySelector('#u8-salt-val');
    const pVal = el.querySelector('#u8-p');
    const gammaVal = el.querySelector('#u8-gamma');
    const naggVal = el.querySelector('#u8-nagg');

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const conc = parseFloat(concSlider.value); // mM
      const nc = parseInt(ncSlider.value, 10);
      const salt = parseFloat(saltSlider.value); // mM
      const numChains = parseInt(chainsSel.value, 10);

      concVal.textContent = conc.toFixed(1) + ' mM';
      ncVal.textContent = nc + ' carbons';
      saltVal.textContent = salt + ' mM';

      // Empirical CMC formula: log10(CMC) = A - B * nc - K_g * log10(c_salt)
      const baseCMC = Math.pow(10, 1.5 - 0.28 * (nc - 8) - 0.15 * Math.log10(1 + salt * 0.05));
      const CMC = numChains === 2 ? baseCMC * 0.01 : baseCMC; // lipid CMC is orders of magnitude lower

      // Tanford chain parameters
      const v1 = 27.4 + 26.9 * nc; // A^3
      const v = v1 * numChains;
      const lc = 1.5 + 1.265 * nc; // A

      // Headgroup area a0 screened by salt
      const a0_base = numChains === 2 ? 65.0 : 62.0;
      const a0 = Math.max(32.0, a0_base - 0.06 * salt);

      // Packing Parameter P = v / (a0 * lc)
      const P = v / (a0 * lc);

      let morph = 'Spherical Micelle';
      if (P > 1.0) morph = 'Inverted Hexagonal / Inverted Micelles';
      else if (P > 0.8) morph = 'Planar Lamellar Bilayer';
      else if (P > 0.5) morph = 'Vesicle / Liposome';
      else if (P > 0.33) morph = 'Wormlike / Cylindrical Micelle';
      pVal.textContent = 'P = ' + P.toFixed(2) + ' (' + morph + ')';

      // Surface tension calculation
      let gamma = 72.0;
      if (conc < CMC) {
        gamma = Math.max(34.0, 72.0 - 16.0 * Math.log(1 + (conc / CMC) * 8));
      } else {
        gamma = 34.0; // saturation plateau
      }
      gammaVal.textContent = 'γ = ' + gamma.toFixed(1) + ' mN/m';

      const Nagg = Math.round((4 * Math.PI * Math.pow(lc, 3)) / (3 * v1));
      naggVal.textContent = 'N_agg ≈ ' + Math.min(180, Math.max(30, Nagg));

      ctx.clearRect(0, 0, W, H);

      // Left half: Molecular aggregate self-assembly rendering
      // Right half: Surface tension gamma vs ln(C) plot
      const leftW = W * 0.52;
      ctx.strokeStyle = '#21262d';
      ctx.beginPath();
      ctx.moveTo(leftW, 20);
      ctx.lineTo(leftW, H - 20);
      ctx.stroke();

      // Top air-water interface
      const airY = 40;
      ctx.fillStyle = '#090d13';
      ctx.fillRect(10, 10, leftW - 20, airY - 10);
      ctx.fillStyle = '#0d1d30';
      ctx.fillRect(10, airY, leftW - 20, H - airY - 15);

      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(10, airY);
      ctx.lineTo(leftW - 10, airY);
      ctx.stroke();

      ctx.fillStyle = '#8b949e';
      ctx.font = '10px sans-serif';
      ctx.fillText('AIR', 20, 25);
      ctx.fillText('AQUEOUS BULK', 20, airY + 20);

      // Draw surfactant monolayer at interface
      const numSurf = Math.min(24, Math.round((conc / CMC) * 16) + 4);
      for (let i = 0; i < numSurf; i++) {
        const sx = 25 + (i / numSurf) * (leftW - 50);
        // Head in water (airY + 5), tail pointing up into air
        ctx.fillStyle = '#f85149';
        ctx.beginPath();
        ctx.arc(sx, airY + 6, 5, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#e3b341';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(sx, airY + 2);
        ctx.lineTo(sx + (Math.sin(i) * 3), airY - 16);
        ctx.stroke();
      }

      // If conc > CMC, draw micellar aggregates in bulk
      const cx = leftW / 2;
      const cy = (airY + H) / 2 + 10;

      if (conc >= CMC) {
        if (P <= 0.38) {
          // Spherical micelle
          const micR = 48;
          ctx.fillStyle = 'rgba(227, 179, 65, 0.25)'; // hydrocarbon core
          ctx.beginPath();
          ctx.arc(cx, cy, micR - 10, 0, Math.PI * 2);
          ctx.fill();

          // Heads around circle
          const numHeads = 24;
          for (let i = 0; i < numHeads; i++) {
            const ang = (i / numHeads) * Math.PI * 2;
            const hx = cx + Math.cos(ang) * micR;
            const hy = cy + Math.sin(ang) * micR;
            ctx.fillStyle = '#58a6ff';
            ctx.beginPath();
            ctx.arc(hx, hy, 5, 0, Math.PI * 2);
            ctx.fill();

            // Tail pointing in
            ctx.strokeStyle = '#e3b341';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(hx, hy);
            ctx.lineTo(cx + Math.cos(ang) * (micR - 22), cy + Math.sin(ang) * (micR - 22));
            ctx.stroke();
          }
          ctx.fillStyle = '#7ee787';
          ctx.font = 'bold 11px sans-serif';
          ctx.textAlign = 'center';
          ctx.fillText('Spherical Micelle', cx, cy);

        } else if (P <= 0.52) {
          // Cylindrical / wormlike micelle
          ctx.fillStyle = 'rgba(227, 179, 65, 0.25)';
          ctx.beginPath();
          ctx.roundRect(cx - 70, cy - 25, 140, 50, 20);
          ctx.fill();

          ctx.fillStyle = '#58a6ff';
          for (let i = -6; i <= 6; i++) {
            ctx.beginPath();
            ctx.arc(cx + i * 11, cy - 25, 5, 0, Math.PI * 2);
            ctx.arc(cx + i * 11, cy + 25, 5, 0, Math.PI * 2);
            ctx.fill();
          }
          ctx.fillStyle = '#7ee787';
          ctx.font = 'bold 11px sans-serif';
          ctx.textAlign = 'center';
          ctx.fillText('Wormlike Cylindrical Micelle', cx, cy);

        } else {
          // Bilayer vesicle
          ctx.strokeStyle = '#58a6ff';
          ctx.lineWidth = 4;
          ctx.beginPath();
          ctx.arc(cx, cy, 65, 0, Math.PI * 2);
          ctx.stroke();

          ctx.strokeStyle = '#e3b341';
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.arc(cx, cy, 55, 0, Math.PI * 2);
          ctx.stroke();

          ctx.fillStyle = 'rgba(88, 166, 255, 0.15)';
          ctx.beginPath();
          ctx.arc(cx, cy, 45, 0, Math.PI * 2);
          ctx.fill();

          ctx.fillStyle = '#7ee787';
          ctx.font = 'bold 11px sans-serif';
          ctx.textAlign = 'center';
          ctx.fillText('Unilamellar Liposome Vesicle', cx, cy);
        }
      } else {
        ctx.fillStyle = '#8b949e';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Below CMC: Free Monomers Only', cx, cy);
      }

      // Right half: Surface Tension plot (gamma vs ln C)
      const rPad = { left: leftW + 45, right: 25, top: 40, bottom: 45 };
      const rW = W - rPad.left - rPad.right;
      const rH = H - rPad.top - rPad.bottom;

      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 12px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Surface Tension γ vs log₁₀(C)', rPad.left, 24);

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let i = 0; i <= 4; i++) {
        const y = rPad.top + (rH * i) / 4;
        ctx.beginPath();
        ctx.moveTo(rPad.left, y);
        ctx.lineTo(rPad.left + rW, y);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText((80 - i * 15) + ' mN/m', rPad.left - 6, y + 3);
      }

      ctx.fillText('Concentration C (mM)', rPad.left + rW / 2, rPad.top + rH + 32);

      // Draw Tensiometric Curve
      ctx.strokeStyle = '#7ee787';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = 0; px <= rW; px++) {
        const cVal = 0.5 + (px / rW) * 30.0;
        let gVal = 72.0;
        if (cVal < CMC) {
          gVal = Math.max(34.0, 72.0 - 16.0 * Math.log(1 + (cVal / CMC) * 8));
        } else {
          gVal = 34.0;
        }
        // y map: 80 mN/m -> rPad.top, 20 mN/m -> rPad.top + rH
        const cyPlot = rPad.top + ((80 - gVal) / 60) * rH;
        if (px === 0) ctx.moveTo(rPad.left + px, cyPlot);
        else ctx.lineTo(rPad.left + px, cyPlot);
      }
      ctx.stroke();

      // CMC vertical mark
      const cmcPx = rPad.left + ((CMC - 0.5) / 30.0) * rW;
      ctx.strokeStyle = '#f0883e';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(cmcPx, rPad.top);
      ctx.lineTo(cmcPx, rPad.top + rH);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#f0883e';
      ctx.font = 'bold 10px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('CMC = ' + CMC.toFixed(1) + ' mM', cmcPx, rPad.top - 6);

      // Current operating point
      const curPx = rPad.left + ((conc - 0.5) / 30.0) * rW;
      const curPy = rPad.top + ((80 - gamma) / 60) * rH;
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.arc(curPx, curPy, 5, 0, Math.PI * 2);
      ctx.fill();
    }

    [concSlider, ncSlider, saltSlider, chainsSel].forEach(s => s.addEventListener('input', render));
    render();
  }

  /* ==========================================================================
     SIMULATION 9: Nematic Director & Freedericksz Transition in LCDs
     ========================================================================== */
  function sim_supra_liquid_crystal_director(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 9: Nematic Director & Freedericksz Electro-Optic Transition</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Liquid Crystal Display (LCD)</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Applied Voltage V: <span id="u9-volt-val" style="color:#58a6ff; font-weight:bold;">0.00 V</span> (V_th = 0.78 V)</label>
            <input type="range" id="u9-volt" min="0.0" max="4.0" step="0.05" value="0.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Cell Alignment Geometry:</label>
            <select id="u9-align" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="planar" selected>Planar Homogeneous (Splay Mode)</option>
              <option value="twisted">Twisted Nematic (90° TN Cell)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Order Parameter S: <span id="u9-s-val" style="color:#58a6ff; font-weight:bold;">0.65</span></label>
            <input type="range" id="u9-s" min="0.3" max="0.85" step="0.05" value="0.65" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u9-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Electro-Optic State: <strong id="u9-state" style="color:#7ee787;">Bright OFF State (Planar Birefringent)</strong></span>
          <span>Optical Transmission: <strong id="u9-trans" style="color:#7ee787;">T = 98.4%</strong></span>
          <span>Director Tilt Angle: <strong id="u9-tilt" style="color:#7ee787;">θ_max = 0.0°</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u9-canvas');
    const voltSlider = el.querySelector('#u9-volt');
    const alignSel = el.querySelector('#u9-align');
    const sSlider = el.querySelector('#u9-s');

    const voltVal = el.querySelector('#u9-volt-val');
    const sVal = el.querySelector('#u9-s-val');
    const stateVal = el.querySelector('#u9-state');
    const transVal = el.querySelector('#u9-trans');
    const tiltVal = el.querySelector('#u9-tilt');

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const V = parseFloat(voltSlider.value);
      const align = alignSel.value;
      const S = parseFloat(sSlider.value);

      voltVal.textContent = V.toFixed(2) + ' V';
      sVal.textContent = S.toFixed(2);

      const Vth = 0.78; // Freedericksz threshold
      let thetaMax = 0.0;
      let trans = 1.0;

      if (V > Vth) {
        // Freedericksz tilt: theta_max = 2 * arctan(sqrt(V/Vth - 1))
        const ratio = V / Vth;
        thetaMax = Math.min(Math.PI / 2, 2.0 * Math.atan(Math.sqrt(ratio - 1)));
        // Optical transmission drops as molecules stand homeotropically
        trans = Math.max(0.01, Math.cos(thetaMax));
        stateVal.textContent = 'Freedericksz Reorientation Active (Homeotropic Tilt)';
        stateVal.style.color = '#e3b341';
      } else {
        thetaMax = 0.0;
        trans = 0.984;
        stateVal.textContent = 'Sub-Threshold OFF State (Bright Waveguiding)';
        stateVal.style.color = '#7ee787';
      }

      if (trans < 0.08) {
        stateVal.textContent = 'Dark ON State (Homeotropic Extinction)';
        stateVal.style.color = '#58a6ff';
      }

      tiltVal.textContent = 'θ_max = ' + (thetaMax * 180 / Math.PI).toFixed(1) + '°';
      transVal.textContent = 'T = ' + (trans * 100).toFixed(1) + '%';

      ctx.clearRect(0, 0, W, H);

      // Left: Cell cross-section with calamitic rod directors between electrodes
      // Right: Optical transmission curve T(V)
      const leftW = W * 0.52;
      ctx.strokeStyle = '#21262d';
      ctx.beginPath();
      ctx.moveTo(leftW, 20);
      ctx.lineTo(leftW, H - 20);
      ctx.stroke();

      // Draw Top & Bottom Electrodes (ITO glass plates)
      const padY = 45;
      const cellH = H - padY * 2;
      const cellTop = padY;
      const cellBottom = H - padY;

      ctx.fillStyle = '#30363d';
      ctx.fillRect(20, cellTop - 12, leftW - 40, 12);
      ctx.fillRect(20, cellBottom, leftW - 40, 12);

      ctx.fillStyle = '#8b949e';
      ctx.font = '10px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Top ITO Electrode (+)', 25, cellTop - 2);
      ctx.fillText('Bottom ITO Electrode (GND)', 25, cellBottom + 10);

      // Draw 5 rows x 11 cols of calamitic mesogen rods
      const rows = 7;
      const cols = 11;
      const cellW = leftW - 60;

      for (let r = 0; r < rows; r++) {
        const yNorm = r / (rows - 1); // 0 (top) to 1 (bottom)
        const py = cellTop + yNorm * cellH;

        // Middle tilts most; boundaries (r=0, r=rows-1) anchored at 0 tilt
        const zWeight = Math.sin(yNorm * Math.PI);
        const localTilt = thetaMax * zWeight;

        for (let cIdx = 0; cIdx < cols; cIdx++) {
          const px = 30 + (cIdx / (cols - 1)) * cellW;

          // Rod length 22px
          const rodL = 22;
          ctx.save();
          ctx.translate(px, py);
          ctx.rotate(localTilt);

          ctx.fillStyle = '#58a6ff';
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1;

          // Elliptical rod
          ctx.beginPath();
          ctx.ellipse(0, 0, rodL / 2, 4, 0, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();

          ctx.restore();
        }
      }

      // Polarization indicator arrows
      ctx.fillStyle = '#7ee787';
      ctx.font = 'bold 11px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Rubbed Anchoring: n = (1, 0, 0)', leftW / 2, H - 12);

      // Right half: Transmission curve T vs Voltage
      const rPad = { left: leftW + 45, right: 25, top: 40, bottom: 45 };
      const rW = W - rPad.left - rPad.right;
      const rH = H - rPad.top - rPad.bottom;

      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 12px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Electro-Optic Transmittance T(V)', rPad.left, 24);

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let i = 0; i <= 4; i++) {
        const y = rPad.top + (rH * i) / 4;
        ctx.beginPath();
        ctx.moveTo(rPad.left, y);
        ctx.lineTo(rPad.left + rW, y);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText((100 - i * 25) + '%', rPad.left - 6, y + 3);
      }

      for (let vStep = 0; vStep <= 4; vStep++) {
        const x = rPad.left + (vStep / 4.0) * rW;
        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(vStep + ' V', x, rPad.top + rH + 15);
      }
      ctx.fillText('Applied Voltage V (Volts)', rPad.left + rW / 2, rPad.top + rH + 32);

      // T(V) curve
      ctx.strokeStyle = '#7ee787';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = 0; px <= rW; px++) {
        const curV = (px / rW) * 4.0;
        let curT = 1.0;
        if (curV > Vth) {
          const ratio = curV / Vth;
          const th = Math.min(Math.PI / 2, 2.0 * Math.atan(Math.sqrt(ratio - 1)));
          curT = Math.max(0.01, Math.cos(th));
        } else {
          curT = 0.984;
        }
        const cyPlot = rPad.top + (1.0 - curT) * rH;
        if (px === 0) ctx.moveTo(rPad.left + px, cyPlot);
        else ctx.lineTo(rPad.left + px, cyPlot);
      }
      ctx.stroke();

      // Vth vertical marker
      const vthPx = rPad.left + (Vth / 4.0) * rW;
      ctx.strokeStyle = '#f0883e';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(vthPx, rPad.top);
      ctx.lineTo(vthPx, rPad.top + rH);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#f0883e';
      ctx.font = 'bold 10px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('V_th = 0.78 V', vthPx, rPad.top - 6);

      // Current operating point
      const curPx = rPad.left + (V / 4.0) * rW;
      const curPy = rPad.top + (1.0 - trans) * rH;
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.arc(curPx, curPy, 5, 0, Math.PI * 2);
      ctx.fill();
    }

    [voltSlider, alignSel, sSlider].forEach(s => s.addEventListener('input', render));
    render();
  }

  /* ==========================================================================
     SIMULATION 10: Discotic Metallomesogen Columnar Wires & 1D Conduction
     ========================================================================== */
  function sim_supra_metallomesogen_columnar(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 10: Discotic Metallomesogen Columnar Wires & 1D Charge Transport</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Hexagonal Col_h Lattice</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Central Metal Center:</label>
            <select id="u10-metal" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="Cu" selected>Copper(II) - CuPc(OR)₈ (d⁹, S = 1/2)</option>
              <option value="Pt">Platinum(II) - PtPc(OR)₈ (d⁸, strong dz² overlap)</option>
              <option value="Zn">Zinc(II) - ZnPc(OR)₈ (d¹⁰, high photo-carrier)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Iodine Doping Level: <span id="u10-doping-val" style="color:#58a6ff; font-weight:bold;">5.0 mol%</span></label>
            <input type="range" id="u10-doping" min="0" max="20" step="1" value="5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Electric Field E_z (kV/cm): <span id="u10-ez-val" style="color:#58a6ff; font-weight:bold;">10.0</span></label>
            <input type="range" id="u10-ez" min="1" max="50" step="1" value="10" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u10-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>1D Conductivity: <strong id="u10-cond" style="color:#7ee787;">σ_parallel = 0.68 S/cm</strong></span>
          <span>Conductivity Anisotropy: <strong id="u10-aniso" style="color:#7ee787;">σ_parallel / σ_perp ≈ 2.5 × 10⁵</strong></span>
          <span>Hole Hopping Mobility: <strong id="u10-mob" style="color:#7ee787;">μ = 0.45 cm²/(V·s)</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u10-canvas');
    const metalSel = el.querySelector('#u10-metal');
    const dopingSlider = el.querySelector('#u10-doping');
    const ezSlider = el.querySelector('#u10-ez');

    const dopingVal = el.querySelector('#u10-doping-val');
    const ezVal = el.querySelector('#u10-ez-val');
    const condVal = el.querySelector('#u10-cond');
    const anisoVal = el.querySelector('#u10-aniso');
    const mobVal = el.querySelector('#u10-mob');

    let polaronT = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const metal = metalSel.value;
      const doping = parseFloat(dopingSlider.value);
      const Ez = parseFloat(ezSlider.value);

      dopingVal.textContent = doping + ' mol%';
      ezVal.textContent = Ez.toFixed(1) + ' kV/cm';

      let baseCond = 0.05;
      let mobility = 0.25;
      if (metal === 'Pt') { baseCond = 0.40; mobility = 0.85; }
      else if (metal === 'Cu') { baseCond = 0.15; mobility = 0.45; }
      else { baseCond = 0.08; mobility = 0.32; }

      const sigma = (baseCond + doping * 0.12) * (1 + Ez * 0.02);
      condVal.textContent = 'σ_parallel = ' + sigma.toFixed(2) + ' S/cm';
      mobVal.textContent = 'μ = ' + mobility.toFixed(2) + ' cm²/(V·s)';
      anisoVal.textContent = 'σ_parallel / σ_perp ≈ 2.5 × 10⁵';

      ctx.clearRect(0, 0, W, H);

      // Left: 3D Perspective columnar stack of discotic metallophthalocyanines
      // Right: I-V Ohm / hopping conductivity plot
      const leftW = W * 0.52;
      ctx.strokeStyle = '#21262d';
      ctx.beginPath();
      ctx.moveTo(leftW, 20);
      ctx.lineTo(leftW, H - 20);
      ctx.stroke();

      const cx = leftW / 2;
      const numDiscs = 8;
      const discSpacing = 32;
      const stackStartY = 60;

      // Draw Columnar stack
      for (let i = 0; i < numDiscs; i++) {
        const dy = stackStartY + i * discSpacing;
        const discRx = 75;
        const discRy = 14;

        // Peripheral insulating alkyl mantle (yellowish halo)
        ctx.strokeStyle = 'rgba(227, 179, 65, 0.40)';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.ellipse(cx, dy, discRx + 18, discRy + 6, 0, 0, Math.PI * 2);
        ctx.stroke();

        // Rigid aromatic Phthalocyanine disc core
        ctx.fillStyle = '#161b22';
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.ellipse(cx, dy, discRx, discRy, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Central Metal Ion (Cu, Pt, Zn)
        ctx.fillStyle = metal === 'Pt' ? '#a5d6ff' : (metal === 'Cu' ? '#f0883e' : '#7ee787');
        ctx.beginPath();
        ctx.arc(cx, dy, 7, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1;
        ctx.stroke();
      }

      // Animated 1D polaron hole hopping along the central wire
      const hopPhase = (polaronT * (Ez * 0.1 + 1)) % numDiscs;
      const hopY = stackStartY + hopPhase * discSpacing;

      ctx.fillStyle = '#f85149';
      ctx.shadowColor = '#f85149';
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(cx, hopY, 9, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 10px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('h⁺', cx, hopY);

      // Label on column
      ctx.fillStyle = '#7ee787';
      ctx.font = 'bold 11px sans-serif';
      ctx.fillText('1D Co-axial π-dz² Electronic Channel (d = 3.4 Å)', cx, H - 24);

      // Right: Voltage vs Current (I-V curve)
      const rPad = { left: leftW + 45, right: 25, top: 40, bottom: 45 };
      const rW = W - rPad.left - rPad.right;
      const rH = H - rPad.top - rPad.bottom;

      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 12px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('1D Intracolumnar Current-Voltage (I-V)', rPad.left, 24);

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let i = 0; i <= 4; i++) {
        const y = rPad.top + (rH * i) / 4;
        ctx.beginPath();
        ctx.moveTo(rPad.left, y);
        ctx.lineTo(rPad.left + rW, y);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText((20 - i * 5) + ' mA', rPad.left - 6, y + 3);
      }

      for (let vStep = 0; vStep <= 50; vStep += 10) {
        const x = rPad.left + (vStep / 50.0) * rW;
        ctx.fillStyle = '#8b949e';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(vStep.toString(), x, rPad.top + rH + 15);
      }
      ctx.fillText('Electric Field Ez (kV/cm)', rPad.left + rW / 2, rPad.top + rH + 32);

      // Draw I-V curve: I = sigma * Ez * Area
      ctx.strokeStyle = '#7ee787';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = 0; px <= rW; px++) {
        const curE = (px / rW) * 50.0;
        const curI = (sigma * curE * 0.35); // in mA
        const cyPlot = rPad.top + rH - (curI / 20.0) * rH;
        if (px === 0) ctx.moveTo(rPad.left + px, cyPlot);
        else ctx.lineTo(rPad.left + px, cyPlot);
      }
      ctx.stroke();

      // Current operating dot
      const curPx = rPad.left + (Ez / 50.0) * rW;
      const curI = (sigma * Ez * 0.35);
      const curPy = rPad.top + rH - (curI / 20.0) * rH;
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.arc(curPx, curPy, 5, 0, Math.PI * 2);
      ctx.fill();

      polaronT += 0.05;
      animId = requestAnimationFrame(render);
    }

    [metalSel, dopingSlider, ezSlider].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));
    render();
  }

  return {
    sim_supra_binding_titration_job,
    sim_supra_crown_ether_selectivity,
    sim_supra_anion_recognition_ph_switch,
    sim_supra_rotaxane_molecular_shuttle,
    sim_supra_cyclodextrin_inclusion,
    sim_supra_picket_fence_porphyrin,
    sim_supra_helicate_cage_assembly,
    sim_supra_micelle_packing_cmc,
    sim_supra_liquid_crystal_director,
    sim_supra_metallomesogen_columnar
  };
})();

/* ==========================================================================
   Global Simulation Engine Registry Adapter
   ========================================================================== */
if (typeof window !== 'undefined') {
  window.SimulationEngine = window.SimulationEngine || {};
  Object.keys(window.SupramolecularChemistrySimulations).forEach(function(key) {
    window[key] = window.SupramolecularChemistrySimulations[key];
  });
  const originalInit = window.SimulationEngine.initSimulation;
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    const el = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    if (!el) return;
    if (window.SupramolecularChemistrySimulations && typeof window.SupramolecularChemistrySimulations[simType] === 'function') {
      return window.SupramolecularChemistrySimulations[simType](el);
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
