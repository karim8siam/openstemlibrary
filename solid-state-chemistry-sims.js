/**
 * solid-state-chemistry-sims.js
 * 10 High-Performance 60 FPS Interactive HTML5 Canvas Simulation Engines
 * for Solid State Chemistry (OpenSTEM Milestone Textbook #53)
 * Equipped with Dimension-Caching, DPR Scaling, and isConnected Cleanup Guards.
 */

window.SolidStateChemistrySimulations = (function() {
  'use strict';

  // High-DPI canvas initialization with dimensions caching to prevent per-frame GPU allocations
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
     SIMULATION 1: Born-Haber Cycle & Madelung Summation Engine
     ========================================================================== */
  function sim_ssc_born_haber_lattice_energy(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Born-Haber Cycle & Madelung Summation Engine</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 1: Cohesive Energetics, Analytical Potentials & Enthalpy Ladders</span>
          </div>
          <div style="display:flex; gap:8px; align-items:center;">
            <label style="font-size:0.85rem; color:#8b949e;">Salt Preset:</label>
            <select id="bh-salt-select" style="background:#161b22; color:#58a6ff; border:1px solid #30363d; border-radius:4px; padding:4px 8px; font-size:0.85rem;">
              <option value="NaCl">NaCl (Rock Salt, M = 1.748)</option>
              <option value="KCl">KCl (Rock Salt, M = 1.748)</option>
              <option value="CsCl">CsCl (Cesium Chloride, M = 1.763)</option>
              <option value="LiF">LiF (Rock Salt, M = 1.748)</option>
              <option value="MgO">MgO (Divalent Oxide, M = 1.748)</option>
            </select>
          </div>
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:12px; border-radius:6px; border:1px solid #30363d;">
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Interionic Distance r₀: <span id="bh-r0-val" style="color:#58a6ff; font-weight:bold;">2.82 Å</span></label>
            <input type="range" id="bh-r0-slider" min="1.8" max="4.0" step="0.05" value="2.82" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Born Exponent n: <span id="bh-n-val" style="color:#3fb950; font-weight:bold;">8.0</span></label>
            <input type="range" id="bh-n-slider" min="5.0" max="12.0" step="0.5" value="8.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Display Mode:</label>
            <div style="display:flex; gap:6px; margin-top:4px;">
              <button id="bh-btn-ladder" style="flex:1; background:#1f6feb; color:#fff; border:none; padding:4px 8px; border-radius:4px; font-size:0.8rem; cursor:pointer;">Enthalpy Ladder</button>
              <button id="bh-btn-madelung" style="flex:1; background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:4px 8px; border-radius:4px; font-size:0.8rem; cursor:pointer;">Madelung Series</button>
            </div>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div id="bh-stats" style="margin-top:10px; font-size:0.85rem; color:#8b949e; display:flex; justify-content:space-around; flex-wrap:wrap; gap:8px;">
          <span>Lattice Energy U_L: <strong id="bh-ul-val" style="color:#f85149;">-787.2 kJ/mol</strong></span>
          <span>Formation ΔH_f°: <strong id="bh-dhf-val" style="color:#3fb950;">-411.2 kJ/mol</strong></span>
          <span>Kapustinskii Estimate: <strong id="bh-kap-val" style="color:#d29922;">-755.4 kJ/mol</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const saltSelect = el.querySelector('#bh-salt-select');
    const r0Slider = el.querySelector('#bh-r0-slider');
    const nSlider = el.querySelector('#bh-n-slider');
    const r0Val = el.querySelector('#bh-r0-val');
    const nVal = el.querySelector('#bh-n-val');
    const btnLadder = el.querySelector('#bh-btn-ladder');
    const btnMadelung = el.querySelector('#bh-btn-madelung');
    const ulVal = el.querySelector('#bh-ul-val');
    const dhfVal = el.querySelector('#bh-dhf-val');
    const kapVal = el.querySelector('#bh-kap-val');

    let mode = 'ladder'; // 'ladder' or 'madelung'
    let animId = null;

    const saltData = {
      NaCl: { M: 1.74756, z1: 1, z2: 1, r0: 2.82, n: 8.0, sub: 107.3, ie: 495.8, diss: 121.7, ea: -349.0, dhf: -411.2 },
      KCl: { M: 1.74756, z1: 1, z2: 1, r0: 3.15, n: 9.0, sub: 89.2, ie: 418.8, diss: 121.7, ea: -349.0, dhf: -436.7 },
      CsCl: { M: 1.76267, z1: 1, z2: 1, r0: 3.57, n: 10.5, sub: 76.5, ie: 375.7, diss: 121.7, ea: -349.0, dhf: -443.0 },
      LiF: { M: 1.74756, z1: 1, z2: 1, r0: 2.01, n: 6.0, sub: 159.3, ie: 520.2, diss: 79.5, ea: -328.0, dhf: -616.0 },
      MgO: { M: 1.74756, z1: 2, z2: 2, r0: 2.10, n: 7.0, sub: 147.1, ie: 2188.4, diss: 249.2, ea: 657.0, dhf: -601.7 }
    };

    function updateSalt() {
      const s = saltData[saltSelect.value];
      r0Slider.value = s.r0;
      nSlider.value = s.n;
      r0Val.textContent = s.r0.toFixed(2) + ' Å';
      nVal.textContent = s.n.toFixed(1);
    }

    saltSelect.addEventListener('change', updateSalt);
    r0Slider.addEventListener('input', () => { r0Val.textContent = parseFloat(r0Slider.value).toFixed(2) + ' Å'; });
    nSlider.addEventListener('input', () => { nVal.textContent = parseFloat(nSlider.value).toFixed(1); });

    btnLadder.addEventListener('click', () => {
      mode = 'ladder';
      btnLadder.style.background = '#1f6feb'; btnLadder.style.color = '#fff';
      btnMadelung.style.background = '#21262d'; btnMadelung.style.color = '#c9d1d9';
    });
    btnMadelung.addEventListener('click', () => {
      mode = 'madelung';
      btnMadelung.style.background = '#1f6feb'; btnMadelung.style.color = '#fff';
      btnLadder.style.background = '#21262d'; btnLadder.style.color = '#c9d1d9';
    });

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      const s = saltData[saltSelect.value];
      const r0 = parseFloat(r0Slider.value);
      const n = parseFloat(nSlider.value);

      // Born-Lande: U_L = -1389.35 * (M * z1 * z2 / r0) * (1 - 1/n) in kJ/mol
      const uLande = -1389.35 * (s.M * s.z1 * s.z2 / r0) * (1 - 1/n);
      // Born-Haber cycle derived formation enthalpy
      const dhfCalc = s.sub + s.ie + s.diss + s.ea + uLande;
      // Kapustinskii equation: U_K = -1202 * (nu * z1 * z2 / (r_c + r_a)) * (1 - 0.345/r0)
      const uKap = -1202.0 * (2.0 * s.z1 * s.z2 / r0) * (1.0 - 0.345 / r0);

      ulVal.textContent = uLande.toFixed(1) + ' kJ/mol';
      dhfVal.textContent = dhfCalc.toFixed(1) + ' kJ/mol';
      kapVal.textContent = uKap.toFixed(1) + ' kJ/mol';

      if (mode === 'ladder') {
        // Render Born-Haber Enthalpy Ladder
        const marginX = 60, marginY = 40;
        const plotW = W - marginX * 2, plotH = H - marginY * 2;

        ctx.strokeStyle = '#21262d';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(marginX, marginY);
        ctx.lineTo(marginX, H - marginY);
        ctx.stroke();

        // Energy levels:
        // 0: Elements in standard states (M(s) + 1/2 X2(g)) = 0
        // 1: Sublimation -> M(g) + 1/2 X2(g)
        // 2: Dissociation -> M(g) + X(g)
        // 3: Ionization -> M+(g) + e- + X(g)
        // 4: Electron Affinity -> M+(g) + X-(g) [Top level before lattice collapse]
        // 5: Crystal Solid M(s) + X(s) -> Delta H_f
        const levels = [
          { name: 'M(s) + 1/2 X₂(g)', val: 0, col: '#8b949e' },
          { name: 'M(g) + 1/2 X₂(g) (+ΔH_sub)', val: s.sub, col: '#58a6ff' },
          { name: 'M(g) + X(g) (+1/2 D)', val: s.sub + s.diss, col: '#388bfd' },
          { name: 'M⁺(g) + e⁻ + X(g) (+IE)', val: s.sub + s.diss + s.ie, col: '#d29922' },
          { name: 'M⁺(g) + X⁻(g) (+EA)', val: s.sub + s.diss + s.ie + s.ea, col: '#f0883e' },
          { name: 'Solid MX(s) (ΔH_f°)', val: dhfCalc, col: '#3fb950' }
        ];

        const minE = Math.min(dhfCalc, 0) - 100;
        const maxE = (s.sub + s.diss + s.ie) + 150;
        const scaleY = (val) => H - marginY - ((val - minE) / (maxE - minE)) * plotH;

        // Draw zero baseline
        const y0 = scaleY(0);
        ctx.strokeStyle = '#30363d';
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(marginX, y0);
        ctx.lineTo(W - marginX, y0);
        ctx.stroke();
        ctx.setLineDash([]);

        // Draw levels
        const stepW = plotW / (levels.length - 1);
        levels.forEach((lev, idx) => {
          const x = marginX + idx * stepW;
          const y = scaleY(lev.val);
          ctx.strokeStyle = lev.col;
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.moveTo(x - 30, y);
          ctx.lineTo(x + 30, y);
          ctx.stroke();

          // Connect with arrow
          if (idx > 0 && idx < 5) {
            const prevY = scaleY(levels[idx - 1].val);
            const prevX = marginX + (idx - 1) * stepW + 30;
            ctx.strokeStyle = 'rgba(88, 166, 255, 0.4)';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(prevX, prevY);
            ctx.lineTo(x - 30, y);
            ctx.stroke();
          }

          // Label
          ctx.fillStyle = lev.col;
          ctx.font = '11px system-ui, sans-serif';
          ctx.textAlign = 'center';
          ctx.fillText(lev.val.toFixed(0) + ' kJ', x, y - 8);
          ctx.fillStyle = '#c9d1d9';
          ctx.font = '10px system-ui, sans-serif';
          ctx.fillText(lev.name.split(' ')[0], x, y + 18);
        });

        // Giant lattice energy arrow connecting ions (idx 4) to solid (idx 5)
        const xIons = marginX + 4 * stepW;
        const yIons = scaleY(levels[4].val);
        const xSolid = marginX + 5 * stepW;
        const ySolid = scaleY(levels[5].val);

        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(xIons + 30, yIons);
        ctx.lineTo(xSolid - 30, ySolid);
        ctx.stroke();

        ctx.fillStyle = '#f85149';
        ctx.font = 'bold 12px system-ui, sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText('Lattice Energy U_L = ' + uLande.toFixed(0) + ' kJ/mol', W - marginX - 10, (yIons + ySolid) / 2);

      } else {
        // Render 1D & 2D Madelung Series Convergence Plot
        const padX = 70, padY = 40;
        const pw = W - padX * 2, ph = H - padY * 2;

        ctx.strokeStyle = '#30363d';
        ctx.lineWidth = 1;
        ctx.strokeRect(padX, padY, pw, ph);

        // Compute 1D alternating line sum: M_1D = 2 * sum_{j=1}^N (-1)^(j+1) / j -> 2 ln 2 = 1.38629
        const exact1D = 2.0 * Math.log(2.0);
        const maxN = 50;
        const pts1D = [];
        let curSum = 0;
        for (let j = 1; j <= maxN; j++) {
          curSum += (j % 2 === 1 ? 1.0 : -1.0) / j;
          pts1D.push(2.0 * curSum);
        }

        const yMin = 0.5, yMax = 2.5;
        const getX = (n) => padX + (n / maxN) * pw;
        const getY = (val) => padY + ph - ((val - yMin) / (yMax - yMin)) * ph;

        // Exact line
        const yExact = getY(exact1D);
        ctx.strokeStyle = '#3fb950';
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(padX, yExact);
        ctx.lineTo(padX + pw, yExact);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#3fb950';
        ctx.font = '11px system-ui, sans-serif';
        ctx.fillText('1D Exact: 2 ln(2) = 1.3863', padX + pw - 140, yExact - 6);

        // 3D Rock salt Madelung line
        const yNaCl = getY(1.74756);
        ctx.strokeStyle = '#58a6ff';
        ctx.setLineDash([2, 2]);
        ctx.beginPath();
        ctx.moveTo(padX, yNaCl);
        ctx.lineTo(padX + pw, yNaCl);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#58a6ff';
        ctx.fillText('NaCl (3D Evjen/Ewald) M = 1.7476', padX + pw - 190, yNaCl - 6);

        // Plot 1D Convergence oscillations
        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 2;
        ctx.beginPath();
        pts1D.forEach((val, idx) => {
          const px = getX(idx + 1);
          const py = getY(val);
          if (idx === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        });
        ctx.stroke();

        pts1D.forEach((val, idx) => {
          if (idx % 2 === 0 || idx < 10) {
            const px = getX(idx + 1);
            const py = getY(val);
            ctx.fillStyle = '#f85149';
            ctx.beginPath();
            ctx.arc(px, py, 3, 0, Math.PI * 2);
            ctx.fill();
          }
        });

        // Axes labels
        ctx.fillStyle = '#8b949e';
        ctx.font = '12px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Coordination Shell Index / Lattice Spheres (N)', padX + pw / 2, H - 10);
        ctx.save();
        ctx.translate(20, padY + ph / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('Madelung Constant M_N', 0, 0);
        ctx.restore();
      }

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* ==========================================================================
     SIMULATION 2: Close-Packed Topologies & Voids Explorer (hcp/ccp, Td/Oh)
     ========================================================================== */
  function sim_ssc_close_packing_voids(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Close-Packed Topologies & Voids Explorer</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 2: Hexagonal (hcp) vs Cubic (ccp), Tetrahedral (Td) & Octahedral (Oh) Interstitials</span>
          </div>
          <div style="display:flex; gap:8px;">
            <button id="cp-btn-ccp" style="background:#1f6feb; color:#fff; border:none; padding:4px 10px; border-radius:4px; font-size:0.85rem; cursor:pointer;">CCP (ABCABC)</button>
            <button id="cp-btn-hcp" style="background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:4px 10px; border-radius:4px; font-size:0.85rem; cursor:pointer;">HCP (ABAB)</button>
          </div>
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:12px; border-radius:6px; border:1px solid #30363d;">
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Layer Explode Separation: <span id="cp-sep-val" style="color:#58a6ff;">1.00x</span></label>
            <input type="range" id="cp-sep-slider" min="1.0" max="2.2" step="0.05" value="1.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Atom Sphere Opacity: <span id="cp-alpha-val" style="color:#3fb950;">0.75</span></label>
            <input type="range" id="cp-alpha-slider" min="0.2" max="1.0" step="0.05" value="0.75" style="width:100%;">
          </div>
          <div style="display:flex; flex-direction:column; justify-content:center; gap:6px;">
            <label style="font-size:0.8rem; color:#8b949e; display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input type="checkbox" id="cp-chk-td" checked> Highlight T_d Voids (r/R = 0.225)
            </label>
            <label style="font-size:0.8rem; color:#8b949e; display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input type="checkbox" id="cp-chk-oh" checked> Highlight O_h Voids (r/R = 0.414)
            </label>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d; cursor:grab;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
          <div style="position:absolute; bottom:8px; left:8px; background:rgba(22,27,34,0.85); padding:4px 8px; border-radius:4px; font-size:0.75rem; color:#8b949e;">
            Drag to Rotate 3D View | APF = 74.05%
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const btnCcp = el.querySelector('#cp-btn-ccp');
    const btnHcp = el.querySelector('#cp-btn-hcp');
    const sepSlider = el.querySelector('#cp-sep-slider');
    const sepVal = el.querySelector('#cp-sep-val');
    const alphaSlider = el.querySelector('#cp-alpha-slider');
    const alphaVal = el.querySelector('#cp-alpha-val');
    const chkTd = el.querySelector('#cp-chk-td');
    const chkOh = el.querySelector('#cp-chk-oh');

    let packing = 'ccp'; // 'ccp' or 'hcp'
    let rotX = 0.5, rotY = 0.6;
    let isDragging = false, lastMouseX = 0, lastMouseY = 0;
    let animId = null;

    btnCcp.addEventListener('click', () => {
      packing = 'ccp';
      btnCcp.style.background = '#1f6feb'; btnCcp.style.color = '#fff';
      btnHcp.style.background = '#21262d'; btnHcp.style.color = '#c9d1d9';
    });
    btnHcp.addEventListener('click', () => {
      packing = 'hcp';
      btnHcp.style.background = '#1f6feb'; btnHcp.style.color = '#fff';
      btnCcp.style.background = '#21262d'; btnCcp.style.color = '#c9d1d9';
    });
    sepSlider.addEventListener('input', () => { sepVal.textContent = parseFloat(sepSlider.value).toFixed(2) + 'x'; });
    alphaSlider.addEventListener('input', () => { alphaVal.textContent = parseFloat(alphaSlider.value).toFixed(2); });

    canvas.addEventListener('mousedown', (e) => {
      isDragging = true;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
      canvas.style.cursor = 'grabbing';
    });
    window.addEventListener('mouseup', () => { isDragging = false; if (canvas) canvas.style.cursor = 'grab'; });
    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      const dx = e.clientX - lastMouseX;
      const dy = e.clientY - lastMouseY;
      rotY += dx * 0.01;
      rotX += dy * 0.01;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
    });

    // Generate sphere positions
    function getSpheres(pack, sep) {
      const spheres = [];
      const R = 30;
      const dZ = R * Math.sqrt(8.0 / 3.0) * sep; // Vertical layer distance

      // Layer A (Z = -dZ)
      const layerA_offsets = [
        [-1, -1], [0, -1], [1, -1],
        [-1, 0], [0, 0], [1, 0],
        [-1, 1], [0, 1], [1, 1]
      ];
      layerA_offsets.forEach(([i, j]) => {
        const x = (i + 0.5 * (j % 2)) * 2 * R;
        const y = j * Math.sqrt(3) * R;
        spheres.push({ x, y, z: -dZ, r: R, layer: 'A', col: '#58a6ff' });
      });

      // Layer B (Z = 0) (Shifted to triangular interstitial hollow)
      const shiftBX = R;
      const shiftBY = R / Math.sqrt(3);
      layerA_offsets.slice(0, 6).forEach(([i, j]) => {
        const x = (i + 0.5 * (j % 2)) * 2 * R + shiftBX;
        const y = j * Math.sqrt(3) * R + shiftBY;
        spheres.push({ x, y, z: 0, r: R, layer: 'B', col: '#3fb950' });
      });

      // Layer C or second A (Z = +dZ)
      if (pack === 'ccp') {
        const shiftCX = -R;
        const shiftCY = R / Math.sqrt(3);
        layerA_offsets.slice(0, 6).forEach(([i, j]) => {
          const x = (i + 0.5 * (j % 2)) * 2 * R + shiftCX;
          const y = j * Math.sqrt(3) * R + shiftCY;
          spheres.push({ x, y, z: dZ, r: R, layer: 'C', col: '#d29922' });
        });
      } else {
        // HCP: Layer A repeats directly above Layer A
        layerA_offsets.slice(0, 6).forEach(([i, j]) => {
          const x = (i + 0.5 * (j % 2)) * 2 * R;
          const y = j * Math.sqrt(3) * R;
          spheres.push({ x, y, z: dZ, r: R, layer: 'A', col: '#58a6ff' });
        });
      }

      // Add Voids
      const voids = [];
      if (chkTd.checked) {
        // Tetrahedral void (radius = 0.225 R)
        voids.push({ x: shiftBX / 2, y: shiftBY / 2, z: -dZ / 2, r: R * 0.225, type: 'Td', col: '#a371f7' });
        voids.push({ x: -shiftBX / 2, y: shiftBY / 2, z: dZ / 2, r: R * 0.225, type: 'Td', col: '#a371f7' });
      }
      if (chkOh.checked) {
        // Octahedral void (radius = 0.414 R)
        voids.push({ x: 0, y: shiftBY, z: -dZ / 2, r: R * 0.414, type: 'Oh', col: '#f85149' });
        voids.push({ x: shiftBX, y: 0, z: dZ / 2, r: R * 0.414, type: 'Oh', col: '#f85149' });
      }

      return { spheres, voids };
    }

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      const sep = parseFloat(sepSlider.value);
      const alpha = parseFloat(alphaSlider.value);
      const { spheres, voids } = getSpheres(packing, sep);

      // Rotate and project 3D points
      const allObjects = [...spheres, ...voids];
      const cosX = Math.cos(rotX), sinX = Math.sin(rotX);
      const cosY = Math.cos(rotY), sinY = Math.sin(rotY);

      allObjects.forEach(obj => {
        // Rotate Y
        const x1 = obj.x * cosY + obj.z * sinY;
        const z1 = -obj.x * sinY + obj.z * cosY;
        // Rotate X
        const y2 = obj.y * cosX - z1 * sinX;
        const z2 = obj.y * sinX + z1 * cosX;

        obj.projX = W / 2 + x1;
        obj.projY = H / 2 + y2;
        obj.projZ = z2;
      });

      // Painter's algorithm: sort back-to-front
      allObjects.sort((a, b) => a.projZ - b.projZ);

      allObjects.forEach(obj => {
        ctx.save();
        ctx.beginPath();
        ctx.arc(obj.projX, obj.projY, Math.max(2, obj.r), 0, Math.PI * 2);
        if (obj.type) {
          // Void sphere
          ctx.fillStyle = obj.col;
          ctx.shadowColor = obj.col;
          ctx.shadowBlur = 8;
          ctx.fill();
        } else {
          // Host close-packed atom
          ctx.fillStyle = obj.col;
          ctx.globalAlpha = alpha;
          ctx.fill();
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1;
          ctx.globalAlpha = Math.min(1.0, alpha + 0.2);
          ctx.stroke();
        }
        ctx.restore();
      });

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* ==========================================================================
     SIMULATION 3: Crystallographic Symmetry & 2D Space Group Generator
     ========================================================================== */
  function sim_ssc_space_group_symmetry(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Crystallographic Symmetry & 2D Space Group Generator</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 3: Plane Groups, Rotation Axes, Mirrors & Glide Transformations</span>
          </div>
          <div>
            <select id="sg-plane-select" style="background:#161b22; color:#58a6ff; border:1px solid #30363d; border-radius:4px; padding:4px 8px; font-size:0.85rem;">
              <option value="p1">p1 (Identity only)</option>
              <option value="p2">p2 (2-fold Rotations)</option>
              <option value="pm">pm (Mirror Reflection)</option>
              <option value="pg">pg (Glide Reflection)</option>
              <option value="p4" selected>p4 (4-fold Rotations)</option>
              <option value="p4mm">p4mm (4-fold + Mirrors + Glides)</option>
              <option value="p6">p6 (6-fold Rotations)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d; cursor:crosshair;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
          <div style="position:absolute; bottom:8px; left:8px; background:rgba(22,27,34,0.85); padding:4px 8px; border-radius:4px; font-size:0.75rem; color:#8b949e;">
            Click / Drag within Unit Cell to position Asymmetric Motif (Orange Dot)
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const sgSelect = el.querySelector('#sg-plane-select');

    let motifX = 0.35, motifY = 0.25; // Fractional coordinates in [0, 1]
    let animId = null;

    canvas.addEventListener('mousedown', setMotif);
    canvas.addEventListener('mousemove', (e) => { if (e.buttons === 1) setMotif(e); });

    function setMotif(e) {
      const rect = canvas.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const clickY = e.clientY - rect.top;
      const W = canvas._cssWidth || rect.width;
      const H = canvas._cssHeight || rect.height;
      const cellSize = Math.min(W, H) * 0.4;
      const startX = W / 2 - cellSize / 2;
      const startY = H / 2 - cellSize / 2;

      motifX = Math.max(0.05, Math.min(0.95, (clickX - startX) / cellSize));
      motifY = Math.max(0.05, Math.min(0.95, (clickY - startY) / cellSize));
    }

    // Apply plane symmetry operators to (x, y)
    function generatePoints(group, x, y) {
      const pts = [];
      const add = (px, py, desc) => {
        pts.push({ x: ((px % 1) + 1) % 1, y: ((py % 1) + 1) % 1, desc });
      };

      add(x, y, 'Identity');

      if (group === 'p2') {
        add(1 - x, 1 - y, '2-fold (180°)');
      } else if (group === 'pm') {
        add(1 - x, y, 'Mirror m_x');
      } else if (group === 'pg') {
        add(1 - x, y + 0.5, 'Glide g');
      } else if (group === 'p4') {
        add(1 - y, x, '4-fold (90°)');
        add(1 - x, 1 - y, '2-fold (180°)');
        add(y, 1 - x, '4-fold (270°)');
      } else if (group === 'p4mm') {
        // p4 plus mirrors
        add(1 - y, x, '4-fold (90°)');
        add(1 - x, 1 - y, '2-fold (180°)');
        add(y, 1 - x, '4-fold (270°)');
        add(1 - x, y, 'Mirror');
        add(x, 1 - y, 'Mirror');
        add(y, x, 'Diagonal Mirror');
        add(1 - y, 1 - x, 'Diagonal Mirror');
      } else if (group === 'p6') {
        for (let k = 1; k < 6; k++) {
          const angle = (k * Math.PI) / 3;
          const rx = (x - 0.5) * Math.cos(angle) - (y - 0.5) * Math.sin(angle) + 0.5;
          const ry = (x - 0.5) * Math.sin(angle) + (y - 0.5) * Math.cos(angle) + 0.5;
          add(rx, ry, `${k * 60}° Rotation`);
        }
      }

      return pts;
    }

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      const group = sgSelect.value;
      const cellSize = Math.min(W, H) * 0.45;
      const centerX = W / 2;
      const centerY = H / 2;

      // Draw 3x3 tiled unit cells to illustrate infinite lattice translations
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let tx = -1; tx <= 1; tx++) {
        for (let ty = -1; ty <= 1; ty++) {
          const x0 = centerX - cellSize / 2 + tx * cellSize;
          const y0 = centerY - cellSize / 2 + ty * cellSize;
          ctx.strokeRect(x0, y0, cellSize, cellSize);
        }
      }

      // Highlight central unit cell
      const startX = centerX - cellSize / 2;
      const startY = centerY - cellSize / 2;
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2;
      ctx.strokeRect(startX, startY, cellSize, cellSize);

      // Symmetry lines for group
      if (group === 'pm' || group === 'p4mm') {
        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(centerX, startY - cellSize);
        ctx.lineTo(centerX, startY + 2 * cellSize);
        ctx.stroke();
        ctx.setLineDash([]);
      }
      if (group === 'pg') {
        ctx.strokeStyle = '#bc8cff';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([6, 3, 2, 3]);
        ctx.beginPath();
        ctx.moveTo(centerX, startY - cellSize);
        ctx.lineTo(centerX, startY + 2 * cellSize);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      const symPoints = generatePoints(group, motifX, motifY);

      // Plot motifs across 3x3 tiles
      for (let tx = -1; tx <= 1; tx++) {
        for (let ty = -1; ty <= 1; ty++) {
          const isCenter = tx === 0 && ty === 0;
          symPoints.forEach((p, idx) => {
            const px = startX + tx * cellSize + p.x * cellSize;
            const py = startY + ty * cellSize + p.y * cellSize;

            ctx.save();
            ctx.beginPath();
            ctx.arc(px, py, isCenter ? 6 : 4, 0, Math.PI * 2);
            if (idx === 0) {
              // Master Asymmetric Motif
              ctx.fillStyle = '#ff7b72';
              ctx.shadowColor = '#ff7b72';
              ctx.shadowBlur = isCenter ? 10 : 0;
            } else {
              // Symmetry-generated copies
              ctx.fillStyle = isCenter ? '#79c0ff' : '#30363d';
            }
            ctx.fill();

            // Draw comma to indicate chirality / reflection inversion
            ctx.strokeStyle = '#0d1117';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.arc(px, py + 3, 2, 0, Math.PI);
            ctx.stroke();
            ctx.restore();
          });
        }
      }

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* ==========================================================================
     SIMULATION 4: Powder XRD & Ewald Sphere Simulator
     ========================================================================== */
  function sim_ssc_xrd_powder_diffraction(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Interactive Powder XRD & Ewald Sphere Simulator</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 4: Bragg Diffraction, Structure Factors, Systematic Absences & Scherrer Broadening</span>
          </div>
          <div>
            <select id="xrd-lattice-select" style="background:#161b22; color:#58a6ff; border:1px solid #30363d; border-radius:4px; padding:4px 8px; font-size:0.85rem;">
              <option value="SC">Simple Cubic (SC)</option>
              <option value="BCC">Body-Centered Cubic (BCC: h+k+l=even)</option>
              <option value="FCC" selected>Face-Centered Cubic (FCC: unmixed parity)</option>
              <option value="Diamond">Diamond Cubic (Si/Ge: Fd-3m extinctions)</option>
            </select>
          </div>
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:12px; border-radius:6px; border:1px solid #30363d;">
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">X-ray Wavelength λ: <span id="xrd-lambda-val" style="color:#58a6ff;">1.5406 Å (Cu Kα)</span></label>
            <input type="range" id="xrd-lambda-slider" min="0.7107" max="2.2897" step="0.05" value="1.5406" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Lattice Constant a: <span id="xrd-a-val" style="color:#3fb950;">4.08 Å</span></label>
            <input type="range" id="xrd-a-slider" min="2.8" max="6.5" step="0.05" value="4.08" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Crystallite Size L (Scherrer): <span id="xrd-size-val" style="color:#d29922;">25 nm</span></label>
            <input type="range" id="xrd-size-slider" min="5" max="80" step="5" value="25" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const latticeSelect = el.querySelector('#xrd-lattice-select');
    const lambdaSlider = el.querySelector('#xrd-lambda-slider');
    const aSlider = el.querySelector('#xrd-a-slider');
    const sizeSlider = el.querySelector('#xrd-size-slider');
    const lambdaVal = el.querySelector('#xrd-lambda-val');
    const aVal = el.querySelector('#xrd-a-val');
    const sizeVal = el.querySelector('#xrd-size-val');

    let animId = null;

    lambdaSlider.addEventListener('input', () => { lambdaVal.textContent = parseFloat(lambdaSlider.value).toFixed(4) + ' Å'; });
    aSlider.addEventListener('input', () => { aVal.textContent = parseFloat(aSlider.value).toFixed(2) + ' Å'; });
    sizeSlider.addEventListener('input', () => { sizeVal.textContent = parseInt(sizeSlider.value) + ' nm'; });

    // Compute Bragg diffraction peaks
    function getPeaks(lattice, a, lambda, L) {
      const peaks = [];
      const maxH = 4;
      for (let h = 0; h <= maxH; h++) {
        for (let k = 0; k <= h; k++) {
          for (let l = 0; l <= k; l++) {
            if (h === 0 && k === 0 && l === 0) continue;
            const s = h * h + k * k + l * l;
            const d = a / Math.sqrt(s);
            const sinTheta = lambda / (2.0 * d);
            if (sinTheta > 0.98) continue; // Bragg cutoff

            const theta = Math.asin(sinTheta);
            const twoThetaDeg = (2.0 * theta * 180.0) / Math.PI;

            // Selection rules
            let allowed = false;
            let mult = 0;
            // Approximate multiplicity
            if (h === k && k === l) mult = 8;
            else if (h === k || k === l || h === l) mult = 24;
            else mult = 48;
            if (l === 0) mult /= 2;

            const sum = h + k + l;
            const allOdd = (h % 2 === 1) && (k % 2 === 1) && (l % 2 === 1);
            const allEven = (h % 2 === 0) && (k % 2 === 0) && (l % 2 === 0);

            if (lattice === 'SC') {
              allowed = true;
            } else if (lattice === 'BCC') {
              allowed = (sum % 2 === 0);
            } else if (lattice === 'FCC') {
              allowed = (allOdd || allEven);
            } else if (lattice === 'Diamond') {
              if (allOdd) allowed = true;
              else if (allEven && sum % 4 === 0) allowed = true;
            }

            if (allowed) {
              // Scherrer broadening FWHM in 2theta radians: beta = 0.9 * lambda / (L * cos(theta))
              const betaRad = (0.9 * lambda) / (L * 10.0 * Math.cos(theta)); // L in Angstroms
              const betaDeg = (betaRad * 180.0) / Math.PI;
              peaks.push({ h, k, l, twoTheta: twoThetaDeg, intensity: mult / Math.pow(Math.sin(theta), 1.5), fwhm: Math.max(0.2, betaDeg) });
            }
          }
        }
      }
      return peaks;
    }

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      const lattice = latticeSelect.value;
      const lambda = parseFloat(lambdaSlider.value);
      const a = parseFloat(aSlider.value);
      const L = parseFloat(sizeSlider.value);

      const peaks = getPeaks(lattice, a, lambda, L);

      const padX = 60, padY = 40;
      const pw = W - padX * 2, ph = H - padY * 2;

      // Draw Axes
      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(padX, padY);
      ctx.lineTo(padX, padY + ph);
      ctx.lineTo(padX + pw, padY + ph);
      ctx.stroke();

      const min2Th = 10.0, max2Th = 90.0;
      const getX = (twoTh) => padX + ((twoTh - min2Th) / (max2Th - min2Th)) * pw;

      // Draw Grid
      ctx.fillStyle = '#8b949e';
      ctx.font = '10px system-ui, sans-serif';
      ctx.textAlign = 'center';
      for (let deg = 20; deg <= 80; deg += 10) {
        const gx = getX(deg);
        ctx.strokeStyle = '#161b22';
        ctx.beginPath();
        ctx.moveTo(gx, padY);
        ctx.lineTo(gx, padY + ph);
        ctx.stroke();
        ctx.fillText(deg + '°', gx, padY + ph + 16);
      }

      ctx.fillText('Diffraction Angle 2θ (degrees)', padX + pw / 2, H - 8);

      // Continuous diffractogram curve
      const maxInt = Math.max(...peaks.map(p => p.intensity), 1);
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2;
      ctx.beginPath();

      const numSamples = 300;
      for (let i = 0; i < numSamples; i++) {
        const cur2Th = min2Th + (i / numSamples) * (max2Th - min2Th);
        let totI = 0;
        peaks.forEach(p => {
          const delta = (cur2Th - p.twoTheta) / (p.fwhm / 2.355);
          totI += (p.intensity / maxInt) * Math.exp(-0.5 * delta * delta);
        });
        const px = getX(cur2Th);
        const py = padY + ph - totI * (ph * 0.85);
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Peak Labels (hkl)
      peaks.forEach(p => {
        if (p.twoTheta >= min2Th && p.twoTheta <= max2Th) {
          const px = getX(p.twoTheta);
          const py = padY + ph - (p.intensity / maxInt) * (ph * 0.85);
          ctx.fillStyle = '#3fb950';
          ctx.font = 'bold 10px system-ui, sans-serif';
          ctx.textAlign = 'center';
          ctx.fillText(`(${p.h}${p.k}${p.l})`, px, Math.max(padY + 15, py - 6));
        }
      });

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* ==========================================================================
     SIMULATION 5: Archetypal Binary Crystal 3D Visualizer (NaCl, CsCl, ZnS, CaF2)
     ========================================================================== */
  function sim_ssc_binary_crystal_viewer(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Archetypal Binary Crystal Structures 3D Visualizer</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 5: Unit Cells, Polyhedra & Limiting Radius Ratios</span>
          </div>
          <div>
            <select id="bc-struct-select" style="background:#161b22; color:#58a6ff; border:1px solid #30363d; border-radius:4px; padding:4px 8px; font-size:0.85rem;">
              <option value="NaCl" selected>NaCl (Rock Salt: 6:6 Octahedra)</option>
              <option value="CsCl">CsCl (Cesium Chloride: 8:8 Cubes)</option>
              <option value="ZnS">ZnS (Zinc Blende: 4:4 Tetrahedra)</option>
              <option value="CaF2">CaF2 (Fluorite: 8:4 Cubic/Tetrahedral)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d; cursor:grab;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
          <div style="position:absolute; bottom:8px; left:8px; background:rgba(22,27,34,0.85); padding:4px 8px; border-radius:4px; font-size:0.75rem; color:#8b949e;">
            Drag to Rotate | Blue = Cation | Green/Red = Anion
          </div>
          <div id="bc-info-badge" style="position:absolute; top:8px; right:8px; background:rgba(22,27,34,0.85); padding:6px 10px; border-radius:4px; font-size:0.8rem; border:1px solid #30363d;">
            CN = 6:6 | r+/r- = 0.563
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const structSelect = el.querySelector('#bc-struct-select');
    const infoBadge = el.querySelector('#bc-info-badge');

    let rotX = 0.4, rotY = 0.5;
    let isDragging = false, lastX = 0, lastY = 0;
    let animId = null;

    canvas.addEventListener('mousedown', (e) => {
      isDragging = true;
      lastX = e.clientX; lastY = e.clientY;
      canvas.style.cursor = 'grabbing';
    });
    window.addEventListener('mouseup', () => { isDragging = false; if (canvas) canvas.style.cursor = 'grab'; });
    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      rotY += (e.clientX - lastX) * 0.01;
      rotX += (e.clientY - lastY) * 0.01;
      lastX = e.clientX; lastY = e.clientY;
    });

    function getCrystalAtoms(type) {
      const atoms = [];
      const S = 90; // Half unit cell dimension

      if (type === 'NaCl') {
        infoBadge.textContent = 'Rock Salt (NaCl) | CN = 6:6 | Space Group Fm-3m';
        // Na+ at (0,0,0) and edge centers; Cl- at face centers and corners
        for (let x = -1; x <= 1; x++) {
          for (let y = -1; y <= 1; y++) {
            for (let z = -1; z <= 1; z++) {
              const isNa = (Math.abs(x) + Math.abs(y) + Math.abs(z)) % 2 === 1;
              atoms.push({
                x: x * S, y: y * S, z: z * S,
                r: isNa ? 14 : 20,
                col: isNa ? '#58a6ff' : '#3fb950',
                name: isNa ? 'Na⁺' : 'Cl⁻'
              });
            }
          }
        }
      } else if (type === 'CsCl') {
        infoBadge.textContent = 'Cesium Chloride (CsCl) | CN = 8:8 | Space Group Pm-3m';
        // Cl- at 8 cube corners, Cs+ at center
        const corners = [
          [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
          [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
        ];
        corners.forEach(([x, y, z]) => {
          atoms.push({ x: x * S, y: y * S, z: z * S, r: 22, col: '#3fb950', name: 'Cl⁻' });
        });
        atoms.push({ x: 0, y: 0, z: 0, r: 20, col: '#58a6ff', name: 'Cs⁺' });
      } else if (type === 'ZnS') {
        infoBadge.textContent = 'Zinc Blende (ZnS) | CN = 4:4 | Space Group F-43m';
        // S2- on FCC, Zn2+ in 4 tetrahedral sites
        const fcc = [
          [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
          [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],
          [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1]
        ];
        fcc.forEach(([x, y, z]) => {
          atoms.push({ x: x * S, y: y * S, z: z * S, r: 20, col: '#d29922', name: 'S²⁻' });
        });
        const tet = [
          [-0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [0.5, -0.5, 0.5], [-0.5, 0.5, 0.5]
        ];
        tet.forEach(([x, y, z]) => {
          atoms.push({ x: x * S, y: y * S, z: z * S, r: 12, col: '#58a6ff', name: 'Zn²⁺' });
        });
      } else if (type === 'CaF2') {
        infoBadge.textContent = 'Fluorite (CaF2) | CN = 8:4 | Space Group Fm-3m';
        // Ca2+ on FCC, F- in all 8 tetrahedral sites
        const fcc = [
          [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
          [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],
          [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1]
        ];
        fcc.forEach(([x, y, z]) => {
          atoms.push({ x: x * S, y: y * S, z: z * S, r: 20, col: '#58a6ff', name: 'Ca²⁺' });
        });
        for (let sx of [-0.5, 0.5]) {
          for (let sy of [-0.5, 0.5]) {
            for (let sz of [-0.5, 0.5]) {
              atoms.push({ x: sx * S, y: sy * S, z: sz * S, r: 11, col: '#f85149', name: 'F⁻' });
            }
          }
        }
      }

      return atoms;
    }

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      const atoms = getCrystalAtoms(structSelect.value);

      const cosX = Math.cos(rotX), sinX = Math.sin(rotX);
      const cosY = Math.cos(rotY), sinY = Math.sin(rotY);

      atoms.forEach(a => {
        const x1 = a.x * cosY + a.z * sinY;
        const z1 = -a.x * sinY + a.z * cosY;
        const y2 = a.y * cosX - z1 * sinX;
        const z2 = a.y * sinX + z1 * cosX;
        a.projX = W / 2 + x1;
        a.projY = H / 2 + y2;
        a.projZ = z2;
      });

      // Draw bounding box edges
      const S = 90;
      const boxCorners = [
        [-S,-S,-S], [S,-S,-S], [S,S,-S], [-S,S,-S],
        [-S,-S,S], [S,-S,S], [S,S,S], [-S,S,S]
      ].map(([x,y,z]) => {
        const x1 = x * cosY + z * sinY;
        const z1 = -x * sinY + z * cosY;
        const y2 = y * cosX - z1 * sinX;
        return { x: W / 2 + x1, y: H / 2 + y2 };
      });

      const edges = [
        [0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],
        [0,4],[1,5],[2,6],[3,7]
      ];
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      edges.forEach(([i, j]) => {
        ctx.beginPath();
        ctx.moveTo(boxCorners[i].x, boxCorners[i].y);
        ctx.lineTo(boxCorners[j].x, boxCorners[j].y);
        ctx.stroke();
      });

      // Sort atoms back to front
      atoms.sort((a, b) => a.projZ - b.projZ);

      atoms.forEach(a => {
        ctx.save();
        ctx.beginPath();
        ctx.arc(a.projX, a.projY, a.r, 0, Math.PI * 2);
        ctx.fillStyle = a.col;
        ctx.fill();
        ctx.strokeStyle = 'rgba(255,255,255,0.4)';
        ctx.lineWidth = 1.5;
        ctx.stroke();
        ctx.restore();
      });

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* ==========================================================================
     SIMULATION 6: Perovskite & Spinel Distortion Workbench
     ========================================================================== */
  function sim_ssc_perovskite_spinel_architectures(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Perovskite & Spinel Distortion Workbench</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 6: Goldschmidt Tolerance Factor, Octahedral Tilting & Normal vs Inverse Spinels</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="pv-btn-perov" style="background:#1f6feb; color:#fff; border:none; padding:4px 8px; border-radius:4px; font-size:0.85rem; cursor:pointer;">Perovskite (ABO₃)</button>
            <button id="pv-btn-spinel" style="background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:4px 8px; border-radius:4px; font-size:0.85rem; cursor:pointer;">Spinel (AB₂O₄)</button>
          </div>
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:12px; border-radius:6px; border:1px solid #30363d;">
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Goldschmidt Tolerance t: <span id="pv-t-val" style="color:#58a6ff; font-weight:bold;">1.00</span></label>
            <input type="range" id="pv-t-slider" min="0.75" max="1.10" step="0.01" value="1.00" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Octahedral Tilt Angle: <span id="pv-tilt-val" style="color:#3fb950; font-weight:bold;">0.0°</span></label>
            <input type="range" id="pv-tilt-slider" min="0" max="25" step="1" value="0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.8rem; color:#8b949e; display:block;">Predicted Distortion:</label>
            <span id="pv-dist-label" style="font-size:0.85rem; color:#d29922; font-weight:bold; display:block; margin-top:4px;">Ideal Cubic (Pm-3m)</span>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d; cursor:grab;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
          <div style="position:absolute; bottom:8px; left:8px; background:rgba(22,27,34,0.85); padding:4px 8px; border-radius:4px; font-size:0.75rem; color:#8b949e;">
            Drag to Rotate | Green = A-cation | Blue = B-cation | Red = Oxygen
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const tSlider = el.querySelector('#pv-t-slider');
    const tiltSlider = el.querySelector('#pv-tilt-slider');
    const tVal = el.querySelector('#pv-t-val');
    const tiltVal = el.querySelector('#pv-tilt-val');
    const distLabel = el.querySelector('#pv-dist-label');
    const btnPerov = el.querySelector('#pv-btn-perov');
    const btnSpinel = el.querySelector('#pv-btn-spinel');

    let mode = 'perov';
    let rotX = 0.4, rotY = 0.5;
    let isDragging = false, lastX = 0, lastY = 0;
    let animId = null;

    btnPerov.addEventListener('click', () => {
      mode = 'perov';
      btnPerov.style.background = '#1f6feb'; btnPerov.style.color = '#fff';
      btnSpinel.style.background = '#21262d'; btnSpinel.style.color = '#c9d1d9';
    });
    btnSpinel.addEventListener('click', () => {
      mode = 'spinel';
      btnSpinel.style.background = '#1f6feb'; btnSpinel.style.color = '#fff';
      btnPerov.style.background = '#21262d'; btnPerov.style.color = '#c9d1d9';
    });

    tSlider.addEventListener('input', () => {
      const t = parseFloat(tSlider.value);
      tVal.textContent = t.toFixed(2);
      if (t > 1.02) {
        distLabel.textContent = 'Ferroelectric Tetragonal / Hexagonal';
        distLabel.style.color = '#f85149';
        tiltSlider.value = 0;
      } else if (t >= 0.90) {
        distLabel.textContent = 'Ideal Cubic Perovskite (Pm-3m)';
        distLabel.style.color = '#3fb950';
        tiltSlider.value = 0;
      } else if (t >= 0.71) {
        distLabel.textContent = 'Orthorhombic Glazer Tilted (Pbnm)';
        distLabel.style.color = '#d29922';
        tiltSlider.value = Math.round((0.90 - t) * 100);
      } else {
        distLabel.textContent = 'Ilmenite (FeTiO₃) Framework';
        distLabel.style.color = '#bc8cff';
      }
      tiltVal.textContent = tiltSlider.value + '°';
    });

    tiltSlider.addEventListener('input', () => { tiltVal.textContent = tiltSlider.value + '°'; });

    canvas.addEventListener('mousedown', (e) => {
      isDragging = true;
      lastX = e.clientX; lastY = e.clientY;
      canvas.style.cursor = 'grabbing';
    });
    window.addEventListener('mouseup', () => { isDragging = false; if (canvas) canvas.style.cursor = 'grab'; });
    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      rotY += (e.clientX - lastX) * 0.01;
      rotX += (e.clientY - lastY) * 0.01;
      lastX = e.clientX; lastY = e.clientY;
    });

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      const tilt = (parseFloat(tiltSlider.value) * Math.PI) / 180.0;
      const t = parseFloat(tSlider.value);
      const S = 90;

      const cosX = Math.cos(rotX), sinX = Math.sin(rotX);
      const cosY = Math.cos(rotY), sinY = Math.sin(rotY);

      if (mode === 'perov') {
        // Draw Perovskite ABO3:
        // A at corners (8), B at center (1), O at face centers (6)
        const atoms = [];
        // A cations
        for (let x of [-S, S]) {
          for (let y of [-S, S]) {
            for (let z of [-S, S]) {
              atoms.push({ x, y, z, r: 16, col: '#3fb950', name: 'A (Ba²⁺/Sr²⁺)' });
            }
          }
        }
        // B cation (with off-center shift if t > 1.02)
        const shiftZ = t > 1.02 ? 15 : 0;
        atoms.push({ x: 0, y: 0, z: shiftZ, r: 14, col: '#58a6ff', name: 'B (Ti⁴⁺)' });

        // Oxygens at 6 face centers, rotated by tilt angle around z-axis
        const oxygens = [
          { x: S, y: 0, z: 0 }, { x: -S, y: 0, z: 0 },
          { x: 0, y: S, z: 0 }, { x: 0, y: -S, z: 0 },
          { x: 0, y: 0, z: S }, { x: 0, y: 0, z: -S }
        ];

        oxygens.forEach(o => {
          const rx = o.x * Math.cos(tilt) - o.y * Math.sin(tilt);
          const ry = o.x * Math.sin(tilt) + o.y * Math.cos(tilt);
          atoms.push({ x: rx, y: ry, z: o.z, r: 12, col: '#f85149', name: 'O²⁻' });
        });

        atoms.forEach(a => {
          const x1 = a.x * cosY + a.z * sinY;
          const z1 = -a.x * sinY + a.z * cosY;
          const y2 = a.y * cosX - z1 * sinX;
          const z2 = a.y * sinX + z1 * cosX;
          a.projX = W / 2 + x1;
          a.projY = H / 2 + y2;
          a.projZ = z2;
        });

        // Draw BO6 octahedron edges
        const oPts = atoms.slice(9, 15);
        ctx.strokeStyle = 'rgba(248, 81, 73, 0.4)';
        ctx.lineWidth = 1.5;
        // Connect equatorial to apical
        [oPts[4], oPts[5]].forEach(apical => {
          for (let eq = 0; eq < 4; eq++) {
            ctx.beginPath();
            ctx.moveTo(apical.projX, apical.projY);
            ctx.lineTo(oPts[eq].projX, oPts[eq].projY);
            ctx.stroke();
          }
        });

        atoms.sort((a, b) => a.projZ - b.projZ);
        atoms.forEach(a => {
          ctx.beginPath();
          ctx.arc(a.projX, a.projY, a.r, 0, Math.PI * 2);
          ctx.fillStyle = a.col;
          ctx.fill();
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1;
          ctx.stroke();
        });

      } else {
        // Spinel mode: normal vs inverse distribution
        ctx.fillStyle = '#c9d1d9';
        ctx.font = '14px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Spinel Unit Cell (AB₂O₄): 32 O²⁻ FCC Sublattice', W / 2, 40);
        ctx.font = '12px system-ui, sans-serif';
        ctx.fillStyle = '#8b949e';
        ctx.fillText('Normal Spinel: [A]tet [B₂]oct O₄ (e.g., MgAl₂O₄, FeCr₂O₄)', W / 2, 80);
        ctx.fillText('Inverse Spinel: [B]tet [A,B]oct O₄ (e.g., Fe₃O₄, NiFe₂O₄)', W / 2, 110);
        ctx.fillText('Governed by Octahedral Site Stabilization Energy: OSSE = CFSE(oct) - CFSE(tet)', W / 2, 150);

        // Visual OSSE bar chart
        const barY = 200;
        ctx.fillStyle = '#1f6feb';
        ctx.fillRect(W / 2 - 140, barY, 120, 40);
        ctx.fillStyle = '#3fb950';
        ctx.fillRect(W / 2 + 20, barY, 120, 40);
        ctx.fillStyle = '#ffffff';
        ctx.fillText('Fe²⁺ (d⁶): +0.13 Δ₀', W / 2 - 80, barY + 24);
        ctx.fillText('Ni²⁺ (d⁸): +0.84 Δ₀', W / 2 + 80, barY + 24);
      }

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* ==========================================================================
     SIMULATION 7: Kronig-Penney Band Structure & DOS Engine
     ========================================================================== */
  function sim_ssc_band_structure_kronig_penney(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Kronig-Penney Band Structure & Density of States Engine</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 7: Dispersion E(k), Forbidden Band Gaps & DOS g(E)</span>
          </div>
          <div style="display:flex; align-items:center; gap:8px;">
            <label style="font-size:0.85rem; color:#8b949e;">Barrier Strength P: <span id="kp-p-val" style="color:#58a6ff; font-weight:bold;">3.00</span></label>
            <input type="range" id="kp-p-slider" min="0" max="12" step="0.5" value="3.0" style="width:140px;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="margin-top:8px; font-size:0.8rem; color:#8b949e; display:flex; justify-content:space-between;">
          <span>P = 0: Free Electron Parabola</span>
          <span>P = 3-5: Nearly Free Electron Bandgaps</span>
          <span>P → ∞: Discrete Atomic Levels</span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const pSlider = el.querySelector('#kp-p-slider');
    const pVal = el.querySelector('#kp-p-val');

    let animId = null;

    pSlider.addEventListener('input', () => { pVal.textContent = parseFloat(pSlider.value).toFixed(2); });

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      const P = parseFloat(pSlider.value);

      // Left panel: E(k) band dispersion (2/3 width)
      // Right panel: DOS g(E) (1/3 width)
      const splitX = W * 0.70;
      const padY = 30;
      const plotH = H - padY * 2;

      // Draw E(k) axes
      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1;
      ctx.strokeRect(40, padY, splitX - 50, plotH);
      ctx.strokeRect(splitX + 10, padY, W - splitX - 30, plotH);

      const midK = 40 + (splitX - 50) / 2;
      ctx.setLineDash([2, 2]);
      ctx.beginPath();
      ctx.moveTo(midK, padY);
      ctx.lineTo(midK, padY + plotH);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#8b949e';
      ctx.font = '10px system-ui, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('-π/a', 40, padY + plotH + 15);
      ctx.fillText('0 (Γ)', midK, padY + plotH + 15);
      ctx.fillText('+π/a', splitX - 10, padY + plotH + 15);
      ctx.fillText('Wavevector k', midK, H - 4);
      ctx.fillText('DOS g(E)', splitX + (W - splitX - 20) / 2, H - 4);

      // Solve Kronig-Penney: f(alpha a) = P * sin(alpha a) / (alpha a) + cos(alpha a) = cos(k a)
      const maxAlpha = 4.5 * Math.PI;
      const numSteps = 500;
      const allowedBands = []; // Array of { alphaMin, alphaMax }
      let inBand = false, startAlpha = 0;

      for (let i = 1; i <= numSteps; i++) {
        const alpha = (i / numSteps) * maxAlpha;
        const fVal = P * (Math.sin(alpha) / alpha) + Math.cos(alpha);
        const isAllowed = Math.abs(fVal) <= 1.0;

        if (isAllowed && !inBand) {
          inBand = true;
          startAlpha = alpha;
        } else if (!isAllowed && inBand) {
          inBand = false;
          allowedBands.push({ a1: startAlpha, a2: alpha });
        }
      }
      if (inBand) allowedBands.push({ a1: startAlpha, a2: maxAlpha });

      const scaleE = (eVal) => padY + plotH - (eVal / (maxAlpha * maxAlpha)) * plotH;

      // Draw forbidden band gaps as shaded grey bars
      ctx.fillStyle = 'rgba(248, 81, 73, 0.12)';
      let lastEnd = 0;
      allowedBands.forEach((band, idx) => {
        if (idx > 0) {
          const yTop = scaleE(band.a1 * band.a1);
          const yBot = scaleE(lastEnd * lastEnd);
          ctx.fillRect(40, yTop, splitX - 50, yBot - yTop);
          ctx.fillStyle = '#f85149';
          ctx.font = '10px system-ui, sans-serif';
          ctx.textAlign = 'left';
          ctx.fillText(`Bandgap E_g`, 45, (yTop + yBot) / 2 + 3);
          ctx.fillStyle = 'rgba(248, 81, 73, 0.12)';
        }
        lastEnd = band.a2;
      });

      // Plot dispersion curves E(k) inside allowed bands
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2.5;

      allowedBands.forEach(band => {
        ctx.beginPath();
        const steps = 100;
        for (let j = 0; j <= steps; j++) {
          const alpha = band.a1 + (j / steps) * (band.a2 - band.a1);
          const fVal = P * (Math.sin(alpha) / alpha) + Math.cos(alpha);
          const clampedF = Math.max(-1.0, Math.min(1.0, fVal));
          const ka = Math.acos(clampedF); // [0, pi]
          const eVal = alpha * alpha;
          const py = scaleE(eVal);

          // Plot right side (+k)
          const pxRight = midK + (ka / Math.PI) * ((splitX - 50) / 2);
          if (j === 0) ctx.moveTo(pxRight, py);
          else ctx.lineTo(pxRight, py);
        }
        ctx.stroke();

        ctx.beginPath();
        for (let j = 0; j <= steps; j++) {
          const alpha = band.a1 + (j / steps) * (band.a2 - band.a1);
          const fVal = P * (Math.sin(alpha) / alpha) + Math.cos(alpha);
          const clampedF = Math.max(-1.0, Math.min(1.0, fVal));
          const ka = Math.acos(clampedF);
          const eVal = alpha * alpha;
          const py = scaleE(eVal);

          // Plot left side (-k)
          const pxLeft = midK - (ka / Math.PI) * ((splitX - 50) / 2);
          if (j === 0) ctx.moveTo(pxLeft, py);
          else ctx.lineTo(pxLeft, py);
        }
        ctx.stroke();
      });

      // Right panel: DOS g(E)
      ctx.strokeStyle = '#3fb950';
      ctx.lineWidth = 2;
      ctx.beginPath();
      const dosSteps = 200;
      for (let s = 1; s <= dosSteps; s++) {
        const eVal = (s / dosSteps) * (maxAlpha * maxAlpha);
        const alpha = Math.sqrt(eVal);
        const fVal = P * (Math.sin(alpha) / alpha) + Math.cos(alpha);
        const isAllowed = Math.abs(fVal) <= 1.0;
        const py = scaleE(eVal);
        let dos = 0;
        if (isAllowed) {
          // 1D Van Hove singularity g(E) ~ 1 / |dE/dk|
          const df = Math.abs(-P * Math.cos(alpha) / alpha + P * Math.sin(alpha) / (alpha * alpha) - Math.sin(alpha));
          dos = Math.min(60, 15.0 / (Math.sqrt(Math.max(0.01, 1.0 - fVal * fVal)) * df));
        }
        const px = splitX + 10 + dos;
        if (s === 1) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* ==========================================================================
     SIMULATION 8: Point Defect Thermodynamics & Brouwer Diagram Engine
     ========================================================================== */
  function sim_ssc_point_defect_thermodynamics(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Defect Thermodynamics & Brouwer Equilibrium Diagram</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 8: Kröger-Vink Equilibria, Non-Stoichiometry & PO₂ Regimes</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="df-btn-brouwer" style="background:#1f6feb; color:#fff; border:none; padding:4px 8px; border-radius:4px; font-size:0.85rem; cursor:pointer;">Brouwer Diagram (log PO₂)</button>
            <button id="df-btn-arrhenius" style="background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:4px 8px; border-radius:4px; font-size:0.85rem; cursor:pointer;">Arrhenius Plot (1/T)</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const btnBrouwer = el.querySelector('#df-btn-brouwer');
    const btnArrhenius = el.querySelector('#df-btn-arrhenius');

    let mode = 'brouwer';
    let animId = null;

    btnBrouwer.addEventListener('click', () => {
      mode = 'brouwer';
      btnBrouwer.style.background = '#1f6feb'; btnBrouwer.style.color = '#fff';
      btnArrhenius.style.background = '#21262d'; btnArrhenius.style.color = '#c9d1d9';
    });
    btnArrhenius.addEventListener('click', () => {
      mode = 'arrhenius';
      btnArrhenius.style.background = '#1f6feb'; btnArrhenius.style.color = '#fff';
      btnBrouwer.style.background = '#21262d'; btnBrouwer.style.color = '#c9d1d9';
    });

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      const padX = 70, padY = 40;
      const pw = W - padX * 2, ph = H - padY * 2;

      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1;
      ctx.strokeRect(padX, padY, pw, ph);

      if (mode === 'brouwer') {
        // Draw 3 Brouwer Regimes:
        // Regime I: Reducing (low PO2): n = 2 [V_O••]
        // Regime II: Stoichiometric: [V_M''] = [V_O••] (Schottky plateau)
        // Regime III: Oxidizing (high PO2): p = 2 [V_M'']
        const x1 = padX + pw * 0.35;
        const x2 = padX + pw * 0.65;

        ctx.strokeStyle = '#21262d';
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(x1, padY); ctx.lineTo(x1, padY + ph);
        ctx.moveTo(x2, padY); ctx.lineTo(x2, padY + ph);
        ctx.stroke();
        ctx.setLineDash([]);

        // Regime Labels
        ctx.fillStyle = '#8b949e';
        ctx.font = '11px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Regime I: n ≈ 2[V_O••]', padX + (x1 - padX) / 2, padY + 20);
        ctx.fillText("Regime II: [V_M''] ≈ [V_O••]", (x1 + x2) / 2, padY + 20);
        ctx.fillText("Regime III: p ≈ 2[V_M'']", x2 + (padX + pw - x2) / 2, padY + 20);

        // Lines for defects:
        // 1. [V_O••]: Slope -1/6 in I, -1/4 in II, -1/6 in III
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(padX, padY + ph * 0.25);
        ctx.lineTo(x1, padY + ph * 0.50);
        ctx.lineTo(x2, padY + ph * 0.50);
        ctx.lineTo(padX + pw, padY + ph * 0.85);
        ctx.stroke();

        // 2. [V_M'']: Slope +1/6 in I, 0 in II, +1/6 in III
        ctx.strokeStyle = '#3fb950';
        ctx.beginPath();
        ctx.moveTo(padX, padY + ph * 0.85);
        ctx.lineTo(x1, padY + ph * 0.50);
        ctx.lineTo(x2, padY + ph * 0.50);
        ctx.lineTo(padX + pw, padY + ph * 0.25);
        ctx.stroke();

        // 3. n (electrons): Slope -1/6 in I, -1/4 in II, -1/6 in III
        ctx.strokeStyle = '#d29922';
        ctx.beginPath();
        ctx.moveTo(padX, padY + ph * 0.20);
        ctx.lineTo(x1, padY + ph * 0.45);
        ctx.lineTo(x2, padY + ph * 0.70);
        ctx.lineTo(padX + pw, padY + ph * 0.95);
        ctx.stroke();

        // 4. p (holes): Slope +1/6 in I, +1/4 in II, +1/6 in III
        ctx.strokeStyle = '#f85149';
        ctx.beginPath();
        ctx.moveTo(padX, padY + ph * 0.95);
        ctx.lineTo(x1, padY + ph * 0.70);
        ctx.lineTo(x2, padY + ph * 0.45);
        ctx.lineTo(padX + pw, padY + ph * 0.20);
        ctx.stroke();

        // Legend
        ctx.font = '11px system-ui, sans-serif';
        ctx.fillStyle = '#58a6ff'; ctx.fillText('[V_O••] (slope -1/6)', padX + 60, padY + ph - 40);
        ctx.fillStyle = '#3fb950'; ctx.fillText("[V_M''] (slope +1/6)", padX + pw - 70, padY + ph - 40);
        ctx.fillStyle = '#d29922'; ctx.fillText('n (electrons)', padX + 50, padY + ph - 20);
        ctx.fillStyle = '#f85149'; ctx.fillText('p (holes)', padX + pw - 60, padY + ph - 20);

        ctx.fillStyle = '#8b949e';
        ctx.fillText('log P_O₂ (Reducing → Oxidizing)', padX + pw / 2, H - 8);

      } else {
        // Arrhenius Plot of Schottky defect fraction: ln x_S vs 1000/T
        ctx.fillStyle = '#c9d1d9';
        ctx.font = '13px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Arrhenius Plot: ln[Defects] vs 1000/T (K⁻¹)', padX + pw / 2, padY + 25);

        // Intrinsic regime (slope -ΔH_S / 2kB) vs Extrinsic regime (slope -ΔH_mig / kB)
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(padX + 20, padY + 60);
        ctx.lineTo(padX + pw * 0.5, padY + ph * 0.5);
        ctx.lineTo(padX + pw - 20, padY + ph * 0.65);
        ctx.stroke();

        ctx.fillStyle = '#58a6ff';
        ctx.font = '11px system-ui, sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText('Intrinsic Regime (Slope = -ΔH_S / 2k_B)', padX + 30, padY + 90);
        ctx.fillText('Extrinsic / Doped Regime (Slope = -ΔH_m / k_B)', padX + pw * 0.55, padY + ph * 0.60);
      }

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* ==========================================================================
     SIMULATION 9: Dislocation Slip, Peach-Koehler Force & Hall Effect Sensor
     ========================================================================== */
  function sim_ssc_dislocation_mechanics(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Dislocation Slip Mechanics & Hall Effect Sensor</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 9: Edge Dislocation Glide, Peach-Koehler Force & Lorentz Hall Deflection</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="dm-btn-slip" style="background:#1f6feb; color:#fff; border:none; padding:4px 8px; border-radius:4px; font-size:0.85rem; cursor:pointer;">Dislocation Slip</button>
            <button id="dm-btn-hall" style="background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:4px 8px; border-radius:4px; font-size:0.85rem; cursor:pointer;">Hall Effect</button>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const btnSlip = el.querySelector('#dm-btn-slip');
    const btnHall = el.querySelector('#dm-btn-hall');

    let mode = 'slip';
    let slipProgress = 0;
    let animId = null;

    btnSlip.addEventListener('click', () => {
      mode = 'slip';
      btnSlip.style.background = '#1f6feb'; btnSlip.style.color = '#fff';
      btnHall.style.background = '#21262d'; btnHall.style.color = '#c9d1d9';
    });
    btnHall.addEventListener('click', () => {
      mode = 'hall';
      btnHall.style.background = '#1f6feb'; btnHall.style.color = '#fff';
      btnSlip.style.background = '#21262d'; btnSlip.style.color = '#c9d1d9';
    });

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      if (mode === 'slip') {
        slipProgress = (slipProgress + 0.01) % 1.0;
        const dX = slipProgress * 30; // animated dislocation glide

        // Draw periodic lattice grid with extra half plane
        const rows = 9, cols = 15;
        const spacingX = W / (cols + 2);
        const spacingY = (H - 60) / (rows + 1);

        ctx.strokeStyle = '#30363d';
        ctx.lineWidth = 1;

        // Draw atoms
        for (let r = 0; r < rows; r++) {
          const isTopHalf = r < 4;
          const numColsThisRow = isTopHalf ? cols + 1 : cols;
          const y = 40 + r * spacingY;

          for (let c = 0; c < numColsThisRow; c++) {
            let x = (c + 1) * spacingX;
            if (isTopHalf) {
              // Compress towards dislocation core
              const coreX = (cols / 2) * spacingX + dX;
              const dist = x - coreX;
              x -= Math.sin(dist * 0.02) * 8;
            }
            ctx.fillStyle = r === 3 ? '#ff7b72' : '#58a6ff';
            ctx.beginPath();
            ctx.arc(x, y, 5, 0, Math.PI * 2);
            ctx.fill();
          }
        }

        // Draw Dislocation Symbol ⊥
        const corePosX = (cols / 2) * spacingX + dX;
        const corePosY = 40 + 3.5 * spacingY;
        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(corePosX, corePosY - 12);
        ctx.lineTo(corePosX, corePosY + 12);
        ctx.moveTo(corePosX - 12, corePosY + 12);
        ctx.lineTo(corePosX + 12, corePosY + 12);
        ctx.stroke();

        ctx.fillStyle = '#f85149';
        ctx.font = 'bold 12px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Peach-Koehler Force f = τ·b →', corePosX, corePosY - 20);

      } else {
        // Hall Effect visualizer
        const barW = W * 0.6;
        const barH = 120;
        const startX = W / 2 - barW / 2;
        const startY = H / 2 - barH / 2;

        ctx.fillStyle = '#161b22';
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 2;
        ctx.fillRect(startX, startY, barW, barH);
        ctx.strokeRect(startX, startY, barW, barH);

        // Magnetic Field B (arrows pointing out of page / dots)
        ctx.fillStyle = '#8b949e';
        ctx.font = '12px system-ui, sans-serif';
        ctx.fillText('Magnetic Field B_z ⊙ (Out of Screen)', W / 2, startY - 15);

        // Electric current I_x
        ctx.fillStyle = '#3fb950';
        ctx.fillText('Current I_x →', startX + 50, startY + barH / 2 + 5);

        // Electrons deflecting downwards due to Lorentz force: F = -e (v x B)
        for (let i = 0; i < 8; i++) {
          const ex = startX + 80 + i * (barW - 160) / 7;
          const ey = startY + barH - 20;
          ctx.fillStyle = '#f85149';
          ctx.beginPath();
          ctx.arc(ex, ey, 6, 0, Math.PI * 2);
          ctx.fill();
        }

        // Positive charge build up on top edge
        for (let i = 0; i < 8; i++) {
          const hx = startX + 80 + i * (barW - 160) / 7;
          const hy = startY + 20;
          ctx.fillStyle = '#58a6ff';
          ctx.beginPath();
          ctx.arc(hx, hy, 6, 0, Math.PI * 2);
          ctx.fill();
        }

        // Transverse Hall Voltage V_H
        ctx.strokeStyle = '#d29922';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(W / 2 + barW / 2 + 20, startY + 20);
        ctx.lineTo(W / 2 + barW / 2 + 40, startY + 20);
        ctx.lineTo(W / 2 + barW / 2 + 40, startY + barH - 20);
        ctx.lineTo(W / 2 + barW / 2 + 20, startY + barH - 20);
        ctx.stroke();

        ctx.fillStyle = '#d29922';
        ctx.font = 'bold 12px system-ui, sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText('Hall Voltage V_H = R_H · (I·B / t)', W / 2 + barW / 2 + 50, startY + barH / 2);
      }

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  /* ==========================================================================
     SIMULATION 10: Meissner Effect, London Penetration & Superionic Conduction
     ========================================================================== */
  function sim_ssc_superconductor_meissner_transport(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div class="sim-header" style="margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:1.1rem;">Meissner Effect, London Penetration & Superionic Transport</h4>
            <span style="font-size:0.8rem; color:#8b949e;">Unit 10: Magnetic Flux Expulsion, London Depth & Fast-Ion Conduction</span>
          </div>
          <div style="display:flex; align-items:center; gap:8px;">
            <label style="font-size:0.85rem; color:#8b949e;">Temperature T/T_c: <span id="sc-t-val" style="color:#58a6ff; font-weight:bold;">0.30</span></label>
            <input type="range" id="sc-t-slider" min="0.1" max="1.5" step="0.05" value="0.30" style="width:130px;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#040d21; border-radius:6px; overflow:hidden; border:1px solid #30363d;">
          <canvas class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
          <div id="sc-state-badge" style="position:absolute; top:8px; right:8px; background:rgba(22,27,34,0.85); padding:6px 10px; border-radius:4px; font-size:0.8rem; border:1px solid #30363d; color:#3fb950;">
            Superconducting State (B = 0)
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const tSlider = el.querySelector('#sc-t-slider');
    const tVal = el.querySelector('#sc-t-val');
    const stateBadge = el.querySelector('#sc-state-badge');

    let animId = null;

    tSlider.addEventListener('input', () => {
      const t = parseFloat(tSlider.value);
      tVal.textContent = t.toFixed(2);
      if (t < 1.0) {
        stateBadge.textContent = 'Meissner State (B = 0, Perfect Diamagnet χ = -1)';
        stateBadge.style.color = '#3fb950';
      } else {
        stateBadge.textContent = 'Normal Metallic State (B Penetrates Fully)';
        stateBadge.style.color = '#f85149';
      }
    });

    function render() {
      if (!canvas.isConnected) {
        if (animId) cancelAnimationFrame(animId);
        return;
      }
      const c = initCanvas(canvas);
      if (!c) { animId = requestAnimationFrame(render); return; }
      const { ctx, width: W, height: H } = c;

      ctx.clearRect(0, 0, W, H);

      const tRatio = parseFloat(tSlider.value);
      const isSuper = tRatio < 1.0;

      const scCenterX = W / 2;
      const scCenterY = H / 2;
      const scRadius = 60;

      // Draw Magnetic Field Lines (vertical lines from top to bottom)
      const numLines = 17;
      ctx.strokeStyle = isSuper ? '#58a6ff' : '#8b949e';
      ctx.lineWidth = 1.5;

      for (let i = 0; i < numLines; i++) {
        const origX = W * 0.15 + (i / (numLines - 1)) * (W * 0.70);
        ctx.beginPath();

        for (let y = 20; y <= H - 20; y += 4) {
          const dy = y - scCenterY;
          const dx = origX - scCenterX;
          const dist = Math.sqrt(dx * dx + dy * dy);

          let curX = origX;
          if (isSuper) {
            // Expel field lines around the sphere
            if (dist < scRadius * 1.8) {
              const repel = (scRadius * scRadius) / (dist * dist + 1);
              curX += (dx / dist) * repel * (scRadius * 0.9);
            }
          }

          if (y === 20) ctx.moveTo(curX, y);
          else ctx.lineTo(curX, y);
        }
        ctx.stroke();
      }

      // Draw Superconducting / Normal Sphere
      ctx.beginPath();
      ctx.arc(scCenterX, scCenterY, scRadius, 0, Math.PI * 2);
      ctx.fillStyle = isSuper ? '#1f6feb' : '#30363d';
      ctx.fill();
      ctx.strokeStyle = isSuper ? '#79c0ff' : '#8b949e';
      ctx.lineWidth = 3;
      ctx.stroke();

      // Label inside sphere
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px system-ui, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(isSuper ? 'B = 0' : 'B ≠ 0', scCenterX, scCenterY - 4);
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillText(isSuper ? 'Cooper Pairs' : 'Normal e⁻', scCenterX, scCenterY + 14);

      animId = requestAnimationFrame(render);
    }

    render();
    return () => { if (animId) cancelAnimationFrame(animId); };
  }

  return {
    sim_ssc_born_haber_lattice_energy,
    sim_ssc_close_packing_voids,
    sim_ssc_space_group_symmetry,
    sim_ssc_xrd_powder_diffraction,
    sim_ssc_binary_crystal_viewer,
    sim_ssc_perovskite_spinel_architectures,
    sim_ssc_band_structure_kronig_penney,
    sim_ssc_point_defect_thermodynamics,
    sim_ssc_dislocation_mechanics,
    sim_ssc_superconductor_meissner_transport
  };
})();

/* ==========================================================================
   Global Simulation Engine Registry Adapter
   ========================================================================== */
if (typeof window !== 'undefined') {
  window.SimulationEngine = window.SimulationEngine || {};
  Object.keys(window.SolidStateChemistrySimulations).forEach(function(key) {
    window[key] = window.SolidStateChemistrySimulations[key];
  });
  const originalInit = window.SimulationEngine.initSimulation;
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    const el = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    if (!el) return;
    if (window.SolidStateChemistrySimulations && typeof window.SolidStateChemistrySimulations[simType] === 'function') {
      return window.SolidStateChemistrySimulations[simType](el);
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
