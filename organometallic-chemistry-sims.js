/**
 * organometallic-chemistry-sims.js
 * 10 High-Performance 60 FPS Interactive HTML5 Canvas Simulation Engines
 * for Organometallic Chemistry (OpenSTEM Milestone Textbook #56)
 * Equipped with Dimension-Caching, DPR Scaling, and isConnected Cleanup Guards.
 */

window.OrganometallicChemistrySimulations = (function() {
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
     SIMULATION 1: 18-Electron Rule & Frontier MO Workbench
     ========================================================================== */
  function sim_organo_electron_counting_18e(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 1: 18-Electron Rule & Frontier MO Electron Counting Workbench</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Valence Orbital Saturation</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Transition Metal Center:</label>
            <select id="u1-metal" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="Fe">Fe (Group 8, 8 val e⁻)</option>
              <option value="Ru">Ru (Group 8, 8 val e⁻)</option>
              <option value="Os">Os (Group 8, 8 val e⁻)</option>
              <option value="Co">Co (Group 9, 9 val e⁻)</option>
              <option value="Rh" selected>Rh (Group 9, 9 val e⁻)</option>
              <option value="Ir">Ir (Group 9, 9 val e⁻)</option>
              <option value="Ni">Ni (Group 10, 10 val e⁻)</option>
              <option value="Pd">Pd (Group 10, 10 val e⁻)</option>
              <option value="Pt">Pt (Group 10, 10 val e⁻)</option>
              <option value="Cr">Cr (Group 6, 6 val e⁻)</option>
              <option value="Mo">Mo (Group 6, 6 val e⁻)</option>
              <option value="W">W (Group 6, 6 val e⁻)</option>
              <option value="Mn">Mn (Group 7, 7 val e⁻)</option>
              <option value="Ti">Ti (Group 4, 4 val e⁻)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Formal Oxidation State:</label>
            <select id="u1-ox" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="-2">-2</option>
              <option value="-1">-1</option>
              <option value="0">0</option>
              <option value="1" selected>+1</option>
              <option value="2">+2</option>
              <option value="3">+3</option>
              <option value="4">+4</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Geometry Template:</label>
            <select id="u1-geom" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="oct">Octahedral (Oh, 18e favored)</option>
              <option value="sqpl" selected>Square Planar (D4h, 16e stable)</option>
              <option value="tet">Tetrahedral (Td)</option>
              <option value="tbp">Trigonal Bipyramidal (D3h)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Ligand Set Preset:</label>
            <select id="u1-preset" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="vaska">Vaska's: IrCl(CO)(PPh3)2</option>
              <option value="wilk" selected>Wilkinson's: RhCl(PPh3)3</option>
              <option value="ferro">Ferrocene: Fe(Cp)2</option>
              <option value="crco6">Chromium hexacarbonyl: Cr(CO)6</option>
              <option value="zeise">Zeise's salt anion: [PtCl3(C2H4)]⁻</option>
              <option value="fecon">Iron pentacarbonyl: Fe(CO)5</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u1-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Valence e⁻ Count: <strong id="u1-total" style="color:#7ee787;">16 e⁻</strong></span>
          <span>d-Electron Count: <strong id="u1-dn" style="color:#58a6ff;">d⁸</strong></span>
          <span>Classification: <strong id="u1-class" style="color:#e3b341;">Coordinatively Unsaturated (Square Planar)</strong></span>
          <span>Counting Mode: <strong id="u1-mode-lbl" style="color:#d2a8ff;">Neutral: 9 + 7 = 16e | Ionic: d⁸ + 8 = 16e</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u1-canvas');
    const metalSel = el.querySelector('#u1-metal');
    const oxSel = el.querySelector('#u1-ox');
    const geomSel = el.querySelector('#u1-geom');
    const presetSel = el.querySelector('#u1-preset');

    const totalEl = el.querySelector('#u1-total');
    const dnEl = el.querySelector('#u1-dn');
    const classEl = el.querySelector('#u1-class');
    const modeEl = el.querySelector('#u1-mode-lbl');

    const metalGroups = {
      Ti: 4, Cr: 6, Mo: 6, W: 6, Mn: 7, Fe: 8, Ru: 8, Os: 8,
      Co: 9, Rh: 9, Ir: 9, Ni: 10, Pd: 10, Pt: 10
    };

    const presets = {
      vaska: { metal: 'Ir', ox: 1, geom: 'sqpl', ligDesc: 'Cl⁻ (X, 1e neutral / 2e ionic) + CO (L, 2e) + 2 PPh3 (2L, 4e)', ligValNeutral: 7, ligValIonic: 8 },
      wilk: { metal: 'Rh', ox: 1, geom: 'sqpl', ligDesc: 'Cl⁻ (X, 1e neutral / 2e ionic) + 3 PPh3 (3L, 6e)', ligValNeutral: 7, ligValIonic: 8 },
      ferro: { metal: 'Fe', ox: 2, geom: 'oct', ligDesc: '2 η⁵-Cp⁻ (2 L2X, 2×5e neutral / 2×6e ionic)', ligValNeutral: 10, ligValIonic: 12 },
      crco6: { metal: 'Cr', ox: 0, geom: 'oct', ligDesc: '6 CO (6L, 12e)', ligValNeutral: 12, ligValIonic: 12 },
      zeise: { metal: 'Pt', ox: 2, geom: 'sqpl', ligDesc: '3 Cl⁻ (3X, 3e neutral / 6e ionic) + η²-C2H4 (L, 2e) - charge 1⁻', ligValNeutral: 6, ligValIonic: 8 },
      fecon: { metal: 'Fe', ox: 0, geom: 'tbp', ligDesc: '5 CO (5L, 10e)', ligValNeutral: 10, ligValIonic: 10 }
    };

    presetSel.addEventListener('change', function() {
      const p = presets[presetSel.value];
      if (p) {
        metalSel.value = p.metal;
        oxSel.value = String(p.ox);
        geomSel.value = p.geom;
        render();
      }
    });

    [metalSel, oxSel, geomSel].forEach(s => s.addEventListener('change', render));

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const m = metalSel.value;
      const ox = parseInt(oxSel.value, 10);
      const geom = geomSel.value;
      const grp = metalGroups[m] || 8;
      const dn = Math.max(0, grp - ox);

      let ligNeutral = 8;
      let ligIonic = 8;
      const pKey = presetSel.value;
      if (presets[pKey] && presets[pKey].metal === m && presets[pKey].ox === ox) {
        ligNeutral = presets[pKey].ligValNeutral;
        ligIonic = presets[pKey].ligValIonic;
      } else {
        // generic estimate based on geometry
        if (geom === 'oct') { ligNeutral = 12 - ox; ligIonic = 12; }
        else if (geom === 'sqpl') { ligNeutral = 8 - ox; ligIonic = 8; }
        else if (geom === 'tet') { ligNeutral = 8 - ox; ligIonic = 8; }
        else if (geom === 'tbp') { ligNeutral = 10 - ox; ligIonic = 10; }
      }

      const totalNeutral = grp + ligNeutral;
      const totalIonic = dn + ligIonic;
      const totalE = totalNeutral; // Both methods yield identical total

      totalEl.textContent = totalE + ' e⁻';
      dnEl.textContent = 'd' + dn;

      if (totalE === 18) {
        totalEl.style.color = '#7ee787';
        classEl.textContent = '18e Saturated (Thermodynamically Stable, Diamagnetic)';
        classEl.style.color = '#7ee787';
      } else if (totalE === 16 && (geom === 'sqpl' || dn === 8)) {
        totalEl.style.color = '#58a6ff';
        classEl.textContent = '16e Stable Square Planar (d⁸ Center, Associative/OA Active)';
        classEl.style.color = '#58a6ff';
      } else if (totalE < 18) {
        totalEl.style.color = '#e3b341';
        classEl.textContent = 'Coordinatively Unsaturated (' + (18 - totalE) + 'e Vacancy, Electrophilic)';
        classEl.style.color = '#e3b341';
      } else {
        totalEl.style.color = '#ff7b72';
        classEl.textContent = 'Super-18e Complex (' + (totalE - 18) + ' Antibonding Electrons, Highly Reactive)';
        classEl.style.color = '#ff7b72';
      }

      modeEl.textContent = `Neutral: ${grp} + ${ligNeutral} = ${totalE}e | Ionic: d${dn} + ${ligIonic} = ${totalE}e`;

      ctx.clearRect(0, 0, W, H);

      // Left Panel: Electron Breakdown Card
      const pW = W * 0.45;
      ctx.fillStyle = '#161b22';
      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.roundRect(20, 20, pW - 30, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 14px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Electron Counting Audit', 35, 48);

      ctx.font = '12px system-ui, sans-serif';
      ctx.fillStyle = '#8b949e';
      ctx.fillText('Metal: ' + m + ' (Group ' + grp + ') | Formal OS: +' + ox, 35, 75);
      ctx.fillText('Covalent Method (CBC / Neutral):', 35, 105);
      ctx.fillStyle = '#c9d1d9';
      ctx.fillText('• Metal Valence Electrons: ' + grp, 45, 125);
      ctx.fillText('• Ligand Contribution: ' + ligNeutral + ' e⁻', 45, 145);
      ctx.fillStyle = '#7ee787';
      ctx.fillText('  Total Covalent: ' + totalNeutral + ' e⁻', 45, 168);

      ctx.fillStyle = '#8b949e';
      ctx.fillText('Ionic Method (Formal):', 35, 200);
      ctx.fillStyle = '#c9d1d9';
      ctx.fillText('• Metal d-Electrons (dⁿ = ' + grp + ' - ' + ox + '): ' + dn, 45, 220);
      ctx.fillText('• Ligand Pairs (L-donor pairs): ' + ligIonic + ' e⁻', 45, 240);
      ctx.fillStyle = '#7ee787';
      ctx.fillText('  Total Ionic: ' + totalIonic + ' e⁻', 45, 263);

      // Valence Bar Indicator
      const barY = H - 55;
      ctx.fillStyle = '#21262d';
      ctx.fillRect(35, barY, pW - 60, 16);
      const frac = Math.min(1.0, totalE / 18.0);
      ctx.fillStyle = totalE === 18 ? '#238636' : (totalE === 16 ? '#1f6feb' : '#d29922');
      ctx.fillRect(35, barY, (pW - 60) * frac, 16);
      ctx.strokeStyle = '#30363d';
      ctx.strokeRect(35, barY, pW - 60, 16);
      ctx.fillStyle = '#ffffff';
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillText(`${totalE} / 18 e⁻ (${Math.round((totalE/18)*100)}% Saturation)`, 45, barY + 12);

      // Right Panel: Frontier MO Ladder
      const rX = pW + 10;
      const rW = W - rX - 20;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(rX, 20, rW, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 14px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Frontier Molecular Orbital Energy Diagram', rX + 15, 48);

      // MO levels based on geometry
      let levels = [];
      if (geom === 'oct') {
        levels = [
          { name: 'eg* (dx²-y², dz²)', y: 90, deg: 2, antibonding: true },
          { name: 't2g (dxy, dxz, dyz)', y: 190, deg: 3, antibonding: false }
        ];
      } else if (geom === 'sqpl') {
        levels = [
          { name: 'b1g* (dx²-y²)', y: 80, deg: 1, antibonding: true },
          { name: 'b2g (dxy)', y: 140, deg: 1, antibonding: false },
          { name: 'a1g (dz²)', y: 190, deg: 1, antibonding: false },
          { name: 'eg (dxz, dyz)', y: 240, deg: 2, antibonding: false }
        ];
      } else {
        levels = [
          { name: 't2* (dxy, dxz, dyz)', y: 100, deg: 3, antibonding: true },
          { name: 'e (dz², dx²-y²)', y: 200, deg: 2, antibonding: false }
        ];
      }

      // Draw Energy Axis
      ctx.strokeStyle = '#484f58';
      ctx.beginPath();
      ctx.moveTo(rX + 40, H - 60);
      ctx.lineTo(rX + 40, 70);
      ctx.stroke();
      // Arrowhead
      ctx.fillStyle = '#8b949e';
      ctx.beginPath();
      ctx.moveTo(rX + 40, 65);
      ctx.lineTo(rX + 36, 75);
      ctx.lineTo(rX + 44, 75);
      ctx.fill();
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillText('Energy (E)', rX + 15, 75);

      // Distribute d-electrons into levels (Hund's rule / low spin)
      let remE = dn;
      const sortedLevels = [...levels].sort((a,b) => b.y - a.y); // lowest energy has largest y
      const occMap = {};

      sortedLevels.forEach(lvl => {
        const capacity = lvl.deg * 2;
        const put = Math.min(remE, capacity);
        occMap[lvl.name] = put;
        remE -= put;
      });

      levels.forEach(lvl => {
        const occ = occMap[lvl.name] || 0;
        const orbW = 40;
        const gap = 15;
        const totalW = lvl.deg * orbW + (lvl.deg - 1) * gap;
        const startOrbX = rX + 70;

        ctx.font = '12px system-ui, sans-serif';
        ctx.fillStyle = lvl.antibonding ? '#ff7b72' : '#79c0ff';
        ctx.fillText(lvl.name, rX + 70 + totalW + 15, lvl.y + 4);

        for (let i = 0; i < lvl.deg; i++) {
          const ox = startOrbX + i * (orbW + gap);
          ctx.strokeStyle = lvl.antibonding ? '#f85149' : '#388bfd';
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.moveTo(ox, lvl.y);
          ctx.lineTo(ox + orbW, lvl.y);
          ctx.stroke();

          // Calculate electrons in this degenerate orbital
          let orbE = 0;
          if (occ > i * 2 + 1) orbE = 2;
          else if (occ > i * 2) orbE = 1;

          // Draw arrows
          if (orbE >= 1) {
            ctx.fillStyle = '#58a6ff';
            ctx.beginPath();
            ctx.moveTo(ox + orbW * 0.35, lvl.y + 12);
            ctx.lineTo(ox + orbW * 0.35, lvl.y - 12);
            ctx.lineTo(ox + orbW * 0.25, lvl.y - 6);
            ctx.stroke();
          }
          if (orbE === 2) {
            ctx.fillStyle = '#f0883e';
            ctx.beginPath();
            ctx.moveTo(ox + orbW * 0.65, lvl.y - 12);
            ctx.lineTo(ox + orbW * 0.65, lvl.y + 12);
            ctx.lineTo(ox + orbW * 0.75, lvl.y + 6);
            ctx.stroke();
          }
        }
      });
    }

    render();
  }

  /* ==========================================================================
     SIMULATION 2: Main Group Dimerization & 3c-2e Bridge Equilibria
     ========================================================================== */
  function sim_organo_main_group_dimer_equilibria(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 2: Main Group Alkyl Dimerization & 3c-2e Bridge Equilibria</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Van 't Hoff Thermodynamic Engine</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Compound System:</label>
            <select id="u2-system" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="alme" selected>Trimethylaluminum: Al₂Me₆ ⇌ 2 AlMe₃</option>
              <option value="game">Trimethylgallium: Ga₂Me₆ ⇌ 2 GaMe₃ (Weak dimer)</option>
              <option value="bme">Trimethylborane: BMe₃ (Steric monomer only)</option>
              <option value="et2mg">Schlenk: 2 EtMgBr ⇌ MgEt₂ + MgBr₂</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Temperature: <span id="u2-t-val" style="color:#58a6ff; font-weight:bold;">298 K</span></label>
            <input type="range" id="u2-t" min="200" max="450" step="5" value="298" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Total Concentration [M]₀: <span id="u2-c-val" style="color:#58a6ff; font-weight:bold;">0.50 M</span></label>
            <input type="range" id="u2-c" min="0.01" max="2.00" step="0.05" value="0.50" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Donor Solvent (Lewis Base):</label>
            <select id="u2-solv" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="none" selected>Non-coordinating (Hexane / Benzene)</option>
              <option value="et2o">Diethyl Ether (Et₂O adduct formed)</option>
              <option value="thf">Tetrahydrofuran (Strong Lewis base cleavage)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u2-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Dissociation Const Kdiss: <strong id="u2-kd" style="color:#7ee787;">1.52 × 10⁻³ M</strong></span>
          <span>Degree of Dissociation α: <strong id="u2-alpha" style="color:#58a6ff;">5.4%</strong></span>
          <span>ΔH°_diss: <strong id="u2-dh" style="color:#e3b341;">+84.0 kJ/mol</strong></span>
          <span>3c-2e Bond Character: <strong id="u2-bond" style="color:#d2a8ff;">Electron-Deficient Al-C-Al Bridge</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u2-canvas');
    const sysSel = el.querySelector('#u2-system');
    const tSlider = el.querySelector('#u2-t');
    const cSlider = el.querySelector('#u2-c');
    const solvSel = el.querySelector('#u2-solv');

    const tVal = el.querySelector('#u2-t-val');
    const cVal = el.querySelector('#u2-c-val');
    const kdEl = el.querySelector('#u2-kd');
    const alphaEl = el.querySelector('#u2-alpha');
    const dhEl = el.querySelector('#u2-dh');
    const bondEl = el.querySelector('#u2-bond');

    const thermoParams = {
      alme: { dH: 84.0, dS: 156.0, name: 'Al₂Me₆ ⇌ 2 AlMe₃', bond: '3c-2e Bridging Methyls' },
      game: { dH: 35.0, dS: 120.0, name: 'Ga₂Me₆ ⇌ 2 GaMe₃', bond: 'Weak Bridge (Steric Repulsion)' },
      bme: { dH: 0.0, dS: 0.0, name: 'BMe₃ (Sterically Inactive to Dimer)', bond: 'Planar Monomer (Empty p_z)' },
      et2mg: { dH: 22.0, dS: 45.0, name: '2 EtMgBr ⇌ MgEt₂ + MgBr₂', bond: 'Schlenk Halide/Alkyl Bridging' }
    };

    let time = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const sys = sysSel.value;
      const T = parseFloat(tSlider.value);
      const C0 = parseFloat(cSlider.value);
      const solv = solvSel.value;

      tVal.textContent = T.toFixed(0) + ' K';
      cVal.textContent = C0.toFixed(2) + ' M';

      const p = thermoParams[sys];
      dhEl.textContent = '+' + p.dH.toFixed(1) + ' kJ/mol';
      bondEl.textContent = p.bond;

      // Thermodynamics calculation
      let Kdiss = 0;
      let alpha = 0;
      if (sys === 'bme') {
        Kdiss = 1e6;
        alpha = 1.0;
      } else {
        let dH = p.dH * 1000;
        let dS = p.dS;
        if (solv === 'et2o') { dH -= 25000; dS -= 40; }
        if (solv === 'thf') { dH -= 45000; dS -= 60; }

        const dG = dH - T * dS;
        Kdiss = Math.exp(-dG / (8.314 * T));

        // For Dimer ⇌ 2 Monomer: Dimer = C0*(1-alpha)/2, Monomer = C0*alpha
        // Kdiss = (C0*alpha)^2 / [C0*(1-alpha)/2] = 2 * C0 * alpha^2 / (1-alpha)
        // 2 C0 alpha^2 + Kdiss * alpha - Kdiss = 0
        const A = 2 * C0;
        const B = Kdiss;
        const C = -Kdiss;
        const disc = Math.sqrt(B * B - 4 * A * C);
        alpha = (-B + disc) / (2 * A);
        alpha = Math.max(0, Math.min(1.0, alpha));
      }

      kdEl.textContent = Kdiss < 1e-4 ? Kdiss.toExponential(2) + ' M' : Kdiss.toFixed(4) + ' M';
      alphaEl.textContent = (alpha * 100).toFixed(1) + '%';

      ctx.clearRect(0, 0, W, H);

      // Left side: 3D-like Molecule Visualization of 3c-2e bridge
      const mW = W * 0.5;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(20, 20, mW - 30, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Structural Topology: 3-Center 2-Electron Bridge', 35, 45);

      const cx = mW / 2 + 5;
      const cy = H / 2 + 10;
      const osc = Math.sin(time * 2) * 5;

      if (sys === 'alme' || sys === 'game') {
        const atomM = sys === 'alme' ? 'Al' : 'Ga';
        // Two M centers
        const xM1 = cx - 70;
        const xM2 = cx + 70;
        const yM = cy;

        // Bridge Carbons (Top and Bottom)
        const xC_br1 = cx;
        const yC_br1 = cy - 65 + osc;
        const xC_br2 = cx;
        const yC_br2 = cy + 65 - osc;

        // Draw 3c-2e orbital cloud lobes (rhomboid bridge)
        ctx.fillStyle = 'rgba(88, 166, 255, 0.15)';
        ctx.beginPath();
        ctx.ellipse(cx, cy, 75, 45, 0, 0, Math.PI * 2);
        ctx.fill();

        // 3c-2e bridge bonds
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 3;
        ctx.setLineDash([4, 4]);
        [ [xM1, yM, xC_br1, yC_br1], [xM2, yM, xC_br1, yC_br1],
          [xM1, yM, xC_br2, yC_br2], [xM2, yM, xC_br2, yC_br2] ].forEach(([x1, y1, x2, y2]) => {
          ctx.beginPath();
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
          ctx.stroke();
        });
        ctx.setLineDash([]);

        // Terminal M-Me bonds
        ctx.strokeStyle = '#c9d1d9';
        ctx.lineWidth = 2.5;
        // Left terminals
        ctx.beginPath(); ctx.moveTo(xM1, yM); ctx.lineTo(xM1 - 45, yM - 40); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(xM1, yM); ctx.lineTo(xM1 - 45, yM + 40); ctx.stroke();
        // Right terminals
        ctx.beginPath(); ctx.moveTo(xM2, yM); ctx.lineTo(xM2 + 45, yM - 40); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(xM2, yM); ctx.lineTo(xM2 + 45, yM + 40); ctx.stroke();

        // Draw Atoms
        function drawAtom(x, y, r, color, label, fontColor='#ffffff') {
          ctx.fillStyle = color;
          ctx.beginPath();
          ctx.arc(x, y, r, 0, Math.PI * 2);
          ctx.fill();
          ctx.strokeStyle = '#30363d';
          ctx.lineWidth = 1;
          ctx.stroke();
          ctx.fillStyle = fontColor;
          ctx.font = 'bold 11px system-ui, sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(label, x, y);
          ctx.textAlign = 'start';
          ctx.textBaseline = 'alphabetic';
        }

        drawAtom(xM1, yM, 18, '#238636', atomM);
        drawAtom(xM2, yM, 18, '#238636', atomM);
        drawAtom(xC_br1, yC_br1, 14, '#1f6feb', 'μ-C');
        drawAtom(xC_br2, yC_br2, 14, '#1f6feb', 'μ-C');
        drawAtom(xM1 - 45, yM - 40, 11, '#6e7681', 'Me');
        drawAtom(xM1 - 45, yM + 40, 11, '#6e7681', 'Me');
        drawAtom(xM2 + 45, yM - 40, 11, '#6e7681', 'Me');
        drawAtom(xM2 + 45, yM + 40, 11, '#6e7681', 'Me');

        ctx.fillStyle = '#8b949e';
        ctx.font = '11px system-ui, sans-serif';
        ctx.fillText(`Bridge Al-C: 2.14 Å | Terminal Al-C: 1.97 Å | Al-C-Al: 75°`, 35, H - 35);
      } else {
        // Monomer planar geometry
        ctx.fillStyle = '#c9d1d9';
        ctx.font = '13px system-ui, sans-serif';
        ctx.fillText('Monomeric Trigonal Planar (D3h) species:', cx - 110, cy - 50);
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx, cy - 60); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + 52, cy + 30); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx - 52, cy + 30); ctx.stroke();
        ctx.fillStyle = '#da3633';
        ctx.beginPath(); ctx.arc(cx, cy, 18, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.fillText(sys === 'bme' ? 'B' : 'Mg', cx - 5, cy + 5);
      }

      // Right side: Equilibrium Concentration & Van 't Hoff Chart
      const rX = mW + 10;
      const rW = W - rX - 20;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(rX, 20, rW, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Dynamic Speciation & Monomer Fraction', rX + 15, 45);

      // Species Distribution Bars
      const bY = 75;
      const cDimer = C0 * (1 - alpha) / 2;
      const cMonomer = C0 * alpha;

      ctx.font = '12px system-ui, sans-serif';
      ctx.fillStyle = '#c9d1d9';
      ctx.fillText(`[Dimer]: ${cDimer.toFixed(3)} M (${((1-alpha)*100).toFixed(1)}% of metal)`, rX + 15, bY + 15);
      ctx.fillStyle = '#21262d';
      ctx.fillRect(rX + 15, bY + 22, rW - 30, 14);
      ctx.fillStyle = '#238636';
      ctx.fillRect(rX + 15, bY + 22, (rW - 30) * (1 - alpha), 14);

      ctx.fillStyle = '#c9d1d9';
      ctx.fillText(`[Monomer]: ${cMonomer.toFixed(3)} M (${(alpha*100).toFixed(1)}% of metal)`, rX + 15, bY + 55);
      ctx.fillStyle = '#21262d';
      ctx.fillRect(rX + 15, bY + 62, rW - 30, 14);
      ctx.fillStyle = '#1f6feb';
      ctx.fillRect(rX + 15, bY + 62, (rW - 30) * alpha, 14);

      // Van 't Hoff Plot Preview
      const gX = rX + 40;
      const gY = 175;
      const gW = rW - 60;
      const gH = 100;

      ctx.strokeStyle = '#30363d';
      ctx.strokeRect(gX, gY, gW, gH);

      ctx.font = '10px system-ui, sans-serif';
      ctx.fillStyle = '#8b949e';
      ctx.fillText('ln Kdiss vs 1/T (Van \'t Hoff)', gX + 5, gY - 6);

      // Plot theoretical line
      ctx.strokeStyle = '#d29922';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i <= gW; i++) {
        const invT = (1/450) + (i / gW) * ( (1/200) - (1/450) ); // from 450K to 200K
        const curT = 1 / invT;
        const curDG = (p.dH * 1000) - curT * p.dS;
        const curLnKd = -curDG / (8.314 * curT);
        // Map lnKd from -15 to +5
        const normY = (curLnKd - (-15)) / (5 - (-15));
        const py = gY + gH - normY * gH;
        if (i === 0) ctx.moveTo(gX + i, py);
        else ctx.lineTo(gX + i, py);
      }
      ctx.stroke();

      // Current operating point dot
      const curInvT = 1 / T;
      const curPtX = gX + ((curInvT - (1/450)) / ((1/200) - (1/450))) * gW;
      const curDG = (p.dH * 1000) - T * p.dS;
      const curLnKd = -curDG / (8.314 * T);
      const curPtY = gY + gH - ((curLnKd - (-15)) / (5 - (-15))) * gH;

      ctx.fillStyle = '#f85149';
      ctx.beginPath();
      ctx.arc(curPtX, Math.max(gY, Math.min(gY + gH, curPtY)), 5, 0, Math.PI * 2);
      ctx.fill();

      time += 0.03;
      animId = requestAnimationFrame(render);
    }

    [sysSel, tSlider, cSlider, solvSel].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 3: Dewar-Chatt-Duncanson Carbonyl Backbonding & IR Engine
     ========================================================================== */
  function sim_organo_carbonyl_backbonding_ir(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 3: Dewar-Chatt-Duncanson Carbonyl Backbonding & IR Spectrometer</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">FTIR Transmittance Simulator</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Isoelectronic Series / Complex:</label>
            <select id="u3-complex" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="vco6">[V(CO)₆]⁻ (1859 cm⁻¹, Strong π-backbonding)</option>
              <option value="crco6" selected>[Cr(CO)₆] (2000 cm⁻¹, Neutral benchmark)</option>
              <option value="mnco6">[Mn(CO)₆]⁺ (2090 cm⁻¹, Weak π-backbonding)</option>
              <option value="feco6">[Fe(CO)₆]²⁺ (2204 cm⁻¹, Electrostatic limit)</option>
              <option value="nico4">Ni(CO)₄ (2060 cm⁻¹, Tetrahedral d¹⁰)</option>
              <option value="mopme3">Mo(CO)₃(PMe₃)₃ (1934 cm⁻¹, Electron-rich)</option>
              <option value="mopf3">Mo(CO)₃(PF₃)₃ (2055 cm⁻¹, Strong π-acceptor coligands)</option>
              <option value="freeco">Free CO gas (2143 cm⁻¹ reference)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Metal Electron Density (d_π): <span id="u3-dpi-val" style="color:#58a6ff; font-weight:bold;">1.00</span></label>
            <input type="range" id="u3-dpi" min="0.2" max="2.0" step="0.05" value="1.00" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Tolman Electronic Parameter χ: <span id="u3-tol-val" style="color:#58a6ff; font-weight:bold;">0.0 cm⁻¹</span></label>
            <input type="range" id="u3-tol" min="-20" max="20" step="1" value="0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Trans-Ligand Competition:</label>
            <select id="u3-trans" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="none" selected>Trans to CO (Symmetric competition)</option>
              <option value="strong_pi">Trans to Strong π-Acceptor (e.g. NO⁺)</option>
              <option value="pure_sigma">Trans to Pure σ-Donor (e.g. Pyridine/NH₃)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u3-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Stretching Frequency ν_CO: <strong id="u3-nu" style="color:#7ee787;">2000 cm⁻¹</strong></span>
          <span>C-O Bond Order: <strong id="u3-boco" style="color:#58a6ff;">2.68</strong></span>
          <span>M-C Bond Order: <strong id="u3-bomc" style="color:#e3b341;">1.32</strong></span>
          <span>M-C-O Angle: <strong id="u3-angle" style="color:#d2a8ff;">179.8° (Linear Terminal)</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u3-canvas');
    const compSel = el.querySelector('#u3-complex');
    const dpiSlider = el.querySelector('#u3-dpi');
    const tolSlider = el.querySelector('#u3-tol');
    const transSel = el.querySelector('#u3-trans');

    const dpiVal = el.querySelector('#u3-dpi-val');
    const tolVal = el.querySelector('#u3-tol-val');
    const nuEl = el.querySelector('#u3-nu');
    const bocoEl = el.querySelector('#u3-boco');
    const bomcEl = el.querySelector('#u3-bomc');
    const angleEl = el.querySelector('#u3-angle');

    const baseFreqs = {
      vco6: 1859,
      crco6: 2000,
      mnco6: 2090,
      feco6: 2204,
      nico4: 2060,
      mopme3: 1934,
      mopf3: 2055,
      freeco: 2143
    };

    let phase = 0;
    let animId = null;

    compSel.addEventListener('change', () => {
      dpiSlider.value = compSel.value === 'vco6' ? '1.5' : (compSel.value === 'feco6' ? '0.4' : '1.0');
      tolSlider.value = '0';
      render();
    });

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const comp = compSel.value;
      const dpi = parseFloat(dpiSlider.value);
      const tol = parseFloat(tolSlider.value);
      const trans = transSel.value;

      dpiVal.textContent = dpi.toFixed(2);
      tolVal.textContent = (tol >= 0 ? '+' : '') + tol.toFixed(0) + ' cm⁻¹';

      let transShift = 0;
      if (trans === 'strong_pi') transShift = +35; // less backbonding to CO -> higher nu
      if (trans === 'pure_sigma') transShift = -45; // more backbonding to CO -> lower nu

      const baseNu = baseFreqs[comp] || 2000;
      // High dpi means more d_pi -> pi* backbonding -> weaker C-O -> lower frequency
      const nuShift = - (dpi - 1.0) * 120 + tol + transShift;
      const nuCO = comp === 'freeco' ? 2143 : Math.round(baseNu + nuShift);

      // Bond orders
      const boCO = comp === 'freeco' ? 3.0 : (3.0 - (2143 - nuCO) / 320).toFixed(2);
      const boMC = comp === 'freeco' ? 0.0 : (1.0 + (2143 - nuCO) / 300).toFixed(2);

      nuEl.textContent = nuCO + ' cm⁻¹';
      bocoEl.textContent = boCO;
      bomcEl.textContent = boMC;
      angleEl.textContent = '179.8° (Linear Terminal)';

      ctx.clearRect(0, 0, W, H);

      // Left: DCD Orbital Synergic Visualizer
      const leftW = W * 0.48;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(20, 20, leftW - 30, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Dewar-Chatt-Duncanson Orbital Model', 35, 45);

      const ox = leftW / 2 - 10;
      const oy = H / 2 + 10;

      // Draw Metal Center (d_xy / d_xz orbital lobes)
      const pulse = Math.sin(phase * 3) * 0.15 + 1.0;
      const mSize = 24;

      // Metal d-orbital lobes (4 lobes)
      const lobeLen = 42 * pulse;
      ctx.fillStyle = 'rgba(238, 99, 82, 0.4)';
      // Upper Right lobe
      ctx.beginPath(); ctx.ellipse(ox - 60 + lobeLen*0.7, oy - lobeLen*0.7, 18, 9, Math.PI/4, 0, Math.PI*2); ctx.fill();
      // Upper Left lobe
      ctx.beginPath(); ctx.ellipse(ox - 60 - lobeLen*0.7, oy - lobeLen*0.7, 18, 9, -Math.PI/4, 0, Math.PI*2); ctx.fill();
      // Lower Right lobe
      ctx.beginPath(); ctx.ellipse(ox - 60 + lobeLen*0.7, oy + lobeLen*0.7, 18, 9, -Math.PI/4, 0, Math.PI*2); ctx.fill();
      // Lower Left lobe
      ctx.beginPath(); ctx.ellipse(ox - 60 - lobeLen*0.7, oy + lobeLen*0.7, 18, 9, Math.PI/4, 0, Math.PI*2); ctx.fill();

      // Metal Atom Circle
      ctx.fillStyle = '#238636';
      ctx.beginPath(); ctx.arc(ox - 60, oy, mSize, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px system-ui, sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText('M (d_π)', ox - 60, oy);

      // Carbon Atom
      const cX = ox + 45;
      const cY = oy;
      ctx.fillStyle = '#1f6feb';
      ctx.beginPath(); ctx.arc(cX, cY, 16, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.fillText('C', cX, cY);

      // Oxygen Atom
      const oX = ox + 115;
      const oY = oy;
      ctx.fillStyle = '#da3633';
      ctx.beginPath(); ctx.arc(oX, oY, 15, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.fillText('O', oX, oY);

      ctx.textAlign = 'start'; ctx.textBaseline = 'alphabetic';

      // Sigma donation arrow: C 5σ -> M d_σ (Cyan arrow along axis)
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(cX - 18, oy); ctx.lineTo(ox - 30, oy); ctx.stroke();
      ctx.fillStyle = '#58a6ff';
      ctx.beginPath(); ctx.moveTo(ox - 30, oy); ctx.lineTo(ox - 24, oy - 4); ctx.lineTo(ox - 24, oy + 4); ctx.fill();

      // Pi backbonding arrows: M d_π -> CO π* (Magenta curved arrows)
      const alphaBack = Math.min(1.0, Math.max(0.2, (2143 - nuCO) / 300));
      ctx.strokeStyle = `rgba(210, 168, 255, ${alphaBack})`;
      ctx.lineWidth = 3.5;
      // Top curve
      ctx.beginPath(); ctx.arc(ox - 8, oy - 25, 30, Math.PI, 0); ctx.stroke();
      // Bottom curve
      ctx.beginPath(); ctx.arc(ox - 8, oy + 25, 30, 0, Math.PI); ctx.stroke();

      ctx.font = '11px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('σ-donation (C 5σ → M)', ox - 70, oy - 65);
      ctx.fillStyle = '#d2a8ff';
      ctx.fillText('π-backdonation (M d_π → CO π*)', ox - 50, oy + 75);

      // Right: Simulated FTIR Transmittance Spectrum
      const rX = leftW + 10;
      const rW = W - rX - 20;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(rX, 20, rW, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('FTIR Carbonyl Region (1700 - 2250 cm⁻¹)', rX + 15, 45);

      const sX = rX + 45;
      const sY = 65;
      const sW = rW - 65;
      const sH = H - 120;

      // Draw Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let f = 1750; f <= 2200; f += 100) {
        const px = sX + sW - ((f - 1700) / (2250 - 1700)) * sW; // IR plotted high to low cm-1
        ctx.beginPath(); ctx.moveTo(px, sY); ctx.lineTo(px, sY + sH); ctx.stroke();
        ctx.fillStyle = '#6e7681';
        ctx.font = '10px system-ui, sans-serif';
        ctx.fillText(f, px - 12, sY + sH + 15);
      }

      ctx.strokeStyle = '#30363d';
      ctx.strokeRect(sX, sY, sW, sH);

      // Transmittance curve (Lorentzian absorption dips)
      ctx.strokeStyle = '#3fb950';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      const fMin = 1700;
      const fMax = 2250;
      const peakW = 12; // peak width in cm-1

      for (let i = 0; i <= sW; i++) {
        // x=0 is fMax, x=sW is fMin
        const curFreq = fMax - (i / sW) * (fMax - fMin);
        // Lorentzian dip at nuCO
        const delta = curFreq - nuCO;
        const dip = 0.85 / (1.0 + (delta / peakW) * (delta / peakW));
        const Tval = 1.0 - dip; // Transmittance 0 to 1
        const py = sY + (1.0 - Tval) * sH * 0.9 + 5;

        if (i === 0) ctx.moveTo(sX + i, py);
        else ctx.lineTo(sX + i, py);
      }
      ctx.stroke();

      // Peak label
      const peakX = sX + ((fMax - nuCO) / (fMax - fMin)) * sW;
      ctx.fillStyle = '#ffffff';
      ctx.beginPath(); ctx.arc(peakX, sY + sH * 0.82, 4, 0, Math.PI * 2); ctx.fill();
      ctx.font = 'bold 11px system-ui, sans-serif';
      ctx.fillStyle = '#7ee787';
      ctx.fillText(`${nuCO} cm⁻¹`, peakX - 25, sY + sH * 0.82 - 8);

      phase += 0.04;
      animId = requestAnimationFrame(render);
    }

    [compSel, dpiSlider, tolSlider, transSel].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 4: β-Hydride Elimination & Agostic Interaction Engine
     ========================================================================== */
  function sim_organo_beta_hydride_elimination(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 4: β-Hydride Elimination & Agostic Transition State Dynamics</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Concerted 4-Membered Cyclic Pathway</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Alkyl Ligand Structure:</label>
            <select id="u4-alkyl" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="ethyl" selected>Ethyl (-CH₂CH₃, 3 β-H atoms)</option>
              <option value="propyl">n-Propyl (-CH₂CH₂CH₃, 2 β-H atoms)</option>
              <option value="isobutyl">Isobutyl (-CH₂CH(CH₃)₂, 1 β-H atom)</option>
              <option value="neopentyl">Neopentyl (-CH₂C(CH₃)₃, NO β-H atoms!)</option>
              <option value="methyl">Methyl (-CH₃, No β-C atom!)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Dihedral Angle θ(M-C_α-C_β-H): <span id="u4-dihedral-val" style="color:#58a6ff; font-weight:bold;">0° (Syn-Coplanar)</span></label>
            <input type="range" id="u4-dihedral" min="0" max="180" step="2" value="0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Coordination Site Status:</label>
            <select id="u4-site" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="vacant" selected>Vacant Cis Site Present (Facile Elimination)</option>
              <option value="blocked">Coordinatively Saturated (Blocked by PR₃)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Transition Metal Center:</label>
            <select id="u4-metal" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="pd" selected>Pd(II) / Pt(II) (d⁸ Square Planar)</option>
              <option value="ti">Ti(IV) / Zr(IV) (d⁰ Early Metal, Agostic prone)</option>
              <option value="rh">Rh(I) / Ir(I) (d⁸ Planar)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u4-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Elimination Barrier ΔG‡: <strong id="u4-barrier" style="color:#7ee787;">68.5 kJ/mol</strong></span>
          <span>Relative Rate k_rel: <strong id="u4-krel" style="color:#58a6ff;">1.0 × 10⁶ s⁻¹</strong></span>
          <span>Agostic Interaction: <strong id="u4-agostic" style="color:#e3b341;">Active 3c-2e (C_β-H···M)</strong></span>
          <span>Kinetic Status: <strong id="u4-status" style="color:#d2a8ff;">Allowed Syn-Coplanar Pathway</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u4-canvas');
    const alkylSel = el.querySelector('#u4-alkyl');
    const dihSlider = el.querySelector('#u4-dihedral');
    const siteSel = el.querySelector('#u4-site');
    const metalSel = el.querySelector('#u4-metal');

    const dihVal = el.querySelector('#u4-dihedral-val');
    const barEl = el.querySelector('#u4-barrier');
    const krelEl = el.querySelector('#u4-krel');
    const agostEl = el.querySelector('#u4-agostic');
    const statEl = el.querySelector('#u4-status');

    let animTime = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const alkyl = alkylSel.value;
      const theta = parseFloat(dihSlider.value);
      const site = siteSel.value;
      const metal = metalSel.value;

      dihVal.textContent = theta.toFixed(0) + '° (' + (theta < 20 ? 'Syn-Coplanar' : (theta > 160 ? 'Anti-Coplanar' : 'Skewed')) + ')';

      const hasBetaH = (alkyl !== 'neopentyl' && alkyl !== 'methyl');
      const isBlocked = (site === 'blocked');

      let dGact = 68.5; // base kJ/mol
      if (!hasBetaH) {
        dGact = 999.0;
      } else if (isBlocked) {
        dGact = 185.0; // Dissociation of ligand required first
      } else {
        // Torsional barrier contribution: minimum at 0 deg, maximum at 90-180 deg
        const thetaRad = (theta * Math.PI) / 180;
        dGact += 45.0 * (1 - Math.cos(thetaRad));
        if (alkyl === 'propyl') dGact += 5.0;
        if (alkyl === 'isobutyl') dGact += 12.0;
      }

      if (!hasBetaH) {
        barEl.textContent = '∞ (No β-H present)';
        krelEl.textContent = '0 (Kinetically Inert)';
        agostEl.textContent = 'Forbidden';
        statEl.textContent = 'Thermally Robust Alkyl (No β-H pathway)';
      } else if (isBlocked) {
        barEl.textContent = '> 180 kJ/mol';
        krelEl.textContent = '10⁻¹⁰ (Inhibited by PR₃)';
        agostEl.textContent = 'Sterically Blocked';
        statEl.textContent = 'Inhibited by Coordinative Saturation';
      } else {
        barEl.textContent = dGact.toFixed(1) + ' kJ/mol';
        const k = Math.exp(- (dGact - 68.5) * 1000 / (8.314 * 298.15));
        krelEl.textContent = k < 1e-3 ? k.toExponential(2) : (k * 1e6).toExponential(2) + ' s⁻¹';
        agostEl.textContent = theta < 30 ? 'Active 3c-2e (C_β-H···M)' : 'Weak / Broken';
        statEl.textContent = theta < 25 ? 'Allowed Syn-Coplanar 4-Center TS' : 'Rotational Mismatch (High Barrier)';
      }

      ctx.clearRect(0, 0, W, H);

      // Left Panel: 4-Membered Cyclic Transition State Simulation
      const leftW = W * 0.52;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(20, 20, leftW - 30, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('4-Membered Cyclic Transition State [M-C_α-C_β-H]‡', 35, 45);

      const cx = leftW / 2;
      const cy = H / 2 + 10;
      const osc = Math.sin(animTime * 3) * (hasBetaH && !isBlocked && theta < 35 ? 4 : 0);

      // Coordinates for 4-membered ring
      // Metal at (cx - 65, cy)
      const xM = cx - 65;
      const yM = cy;
      // C_alpha at (cx, cy + 45)
      const xCa = cx;
      const yCa = cy + 45;
      // C_beta at (cx + 55, cy - 10)
      const xCb = cx + 55;
      const yCb = cy - 10;
      // H_beta at (cx - 10, cy - 45)
      const xH = cx - 15 + osc;
      const yH = cy - 45 - osc;

      // Draw Bonds
      // M - C_alpha bond
      ctx.strokeStyle = '#c9d1d9';
      ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(xM, yM); ctx.lineTo(xCa, yCa); ctx.stroke();

      // C_alpha - C_beta bond
      ctx.beginPath(); ctx.moveTo(xCa, yCa); ctx.lineTo(xCb, yCb); ctx.stroke();

      if (hasBetaH) {
        // C_beta - H bond (elongated in TS)
        ctx.strokeStyle = theta < 30 ? '#d2a8ff' : '#6e7681';
        ctx.lineWidth = 2;
        ctx.setLineDash(theta < 30 ? [4, 4] : []);
        ctx.beginPath(); ctx.moveTo(xCb, yCb); ctx.lineTo(xH, yH); ctx.stroke();

        // M ··· H agostic / hydride bond
        if (!isBlocked) {
          ctx.strokeStyle = '#f85149';
          ctx.lineWidth = 2.5;
          ctx.beginPath(); ctx.moveTo(xM, yM); ctx.lineTo(xH, yH); ctx.stroke();
        }
        ctx.setLineDash([]);
      }

      // Draw cis vacant or blocked site
      const xVac = xM - 35;
      const yVac = yM - 45;
      if (isBlocked) {
        ctx.strokeStyle = '#6e7681';
        ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(xM, yM); ctx.lineTo(xVac, yVac); ctx.stroke();
        ctx.fillStyle = '#d29922';
        ctx.beginPath(); ctx.arc(xVac, yVac, 12, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 9px system-ui, sans-serif';
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('PR₃', xVac, yVac);
      } else {
        ctx.strokeStyle = '#388bfd';
        ctx.setLineDash([3, 3]);
        ctx.strokeRect(xVac - 8, yVac - 8, 16, 16);
        ctx.setLineDash([]);
        ctx.fillStyle = '#58a6ff';
        ctx.font = '9px system-ui, sans-serif';
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('Vacant', xVac, yVac - 14);
      }

      // Draw Atoms
      function drawAtom(x, y, r, fill, label) {
        ctx.fillStyle = fill;
        ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();
        ctx.strokeStyle = '#30363d'; ctx.lineWidth = 1; ctx.stroke();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px system-ui, sans-serif';
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(label, x, y);
      }

      drawAtom(xM, yM, 20, '#238636', metal.toUpperCase());
      drawAtom(xCa, yCa, 16, '#1f6feb', 'C_α');
      drawAtom(xCb, yCb, 16, '#1f6feb', 'C_β');
      if (hasBetaH) {
        drawAtom(xH, yH, 12, '#da3633', 'H_β');
      }

      ctx.textAlign = 'start'; ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = '#8b949e';
      ctx.font = '11px system-ui, sans-serif';
      ctx.fillText('Requires: Coplanar M-Cα-Cβ-H ring + empty cis coordination orbital', 35, H - 35);

      // Right Panel: Potential Energy Landscape
      const rX = leftW + 10;
      const rW = W - rX - 20;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(rX, 20, rW, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Potential Energy Barrier vs Dihedral θ', rX + 15, 45);

      const pX = rX + 40;
      const pY = 80;
      const pW = rW - 55;
      const pH = H - 140;

      ctx.strokeStyle = '#30363d';
      ctx.strokeRect(pX, pY, pW, pH);

      // Labels
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillStyle = '#8b949e';
      ctx.fillText('0° (Syn)', pX - 5, pY + pH + 15);
      ctx.fillText('90°', pX + pW*0.5 - 10, pY + pH + 15);
      ctx.fillText('180° (Anti)', pX + pW - 25, pY + pH + 15);

      // Energy curve
      ctx.strokeStyle = '#f0883e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= pW; i++) {
        const th = (i / pW) * Math.PI;
        // barrier rises with 1 - cos(th)
        const barrierNorm = (1 - Math.cos(th)) / 2.0;
        const curY = pY + pH - 15 - barrierNorm * (pH - 30);
        if (i === 0) ctx.moveTo(pX + i, curY);
        else ctx.lineTo(pX + i, curY);
      }
      ctx.stroke();

      // Current operating dot
      const curDotX = pX + (theta / 180.0) * pW;
      const curDotNorm = (1 - Math.cos((theta * Math.PI) / 180)) / 2.0;
      const curDotY = pY + pH - 15 - curDotNorm * (pH - 30);

      ctx.fillStyle = '#7ee787';
      ctx.beginPath(); ctx.arc(curDotX, curDotY, 6, 0, Math.PI * 2); ctx.fill();

      ctx.font = 'bold 11px system-ui, sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.fillText(`ΔG‡ = ${hasBetaH ? dGact.toFixed(1) + ' kJ/mol' : '∞'}`, pX + 10, pY + 25);

      animTime += 0.03;
      animId = requestAnimationFrame(render);
    }

    [alkylSel, dihSlider, siteSel, metalSel].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 5: Zeise's Salt Alkene Rotation & Dynamic NMR Coalescence
     ========================================================================== */
  function sim_organo_zeise_alkene_rotation(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 5: Zeise's Salt Alkene Rotation & Dynamic ¹H NMR Coalescence</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Dewar-Chatt-Duncanson π-Coordination</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Temperature: <span id="u5-t-val" style="color:#58a6ff; font-weight:bold;">298 K (25°C)</span></label>
            <input type="range" id="u5-t" min="190" max="380" step="2" value="298" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Trans-Ligand Influence:</label>
            <select id="u5-trans" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="cl" selected>Cl⁻ (Standard Zeise's Salt, ΔG‡ = 62 kJ/mol)</option>
              <option value="nh3">NH₃ (Weak trans-influence, ΔG‡ = 74 kJ/mol)</option>
              <option value="pe3">PEt₃ (Strong trans-influence, ΔG‡ = 48 kJ/mol)</option>
              <option value="sncl3">SnCl₃⁻ (Very strong π-acceptor, ΔG‡ = 38 kJ/mol)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Alkene Substrate:</label>
            <select id="u5-alkene" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="c2h4" selected>Ethylene (C₂H₄)</option>
              <option value="propene">Propene (MeCH=CH₂)</option>
              <option value="tcne">TCNE (Tetracyanoethylene - Rigid Metallacycle)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Spectrometer Frequency B₀:</label>
            <select id="u5-b0" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="300">300 MHz (Δν = 60 Hz)</option>
              <option value="500" selected>500 MHz (Δν = 100 Hz)</option>
              <option value="800">800 MHz (Δν = 160 Hz)</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u5-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Rotational Rate k_rot: <strong id="u5-krot" style="color:#7ee787;">8.4 × 10³ s⁻¹</strong></span>
          <span>Coalescence Temp T_c: <strong id="u5-tc" style="color:#58a6ff;">258 K (-15°C)</strong></span>
          <span>Exchange Regime: <strong id="u5-regime" style="color:#e3b341;">Fast Exchange (Singlet + Satellites)</strong></span>
          <span>¹⁹⁵Pt-Coupling ²J_Pt-H: <strong id="u5-jpt" style="color:#d2a8ff;">34 Hz (Confirmed Pt-Olefin Bond)</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u5-canvas');
    const tSlider = el.querySelector('#u5-t');
    const transSel = el.querySelector('#u5-trans');
    const alkSel = el.querySelector('#u5-alkene');
    const b0Sel = el.querySelector('#u5-b0');

    const tVal = el.querySelector('#u5-t-val');
    const krotEl = el.querySelector('#u5-krot');
    const tcEl = el.querySelector('#u5-tc');
    const regEl = el.querySelector('#u5-regime');
    const jptEl = el.querySelector('#u5-jpt');

    const barrierMap = {
      cl: 62.0, nh3: 74.0, pe3: 48.0, sncl3: 38.0
    };

    let rotAngle = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const T = parseFloat(tSlider.value);
      const trans = transSel.value;
      const alk = alkSel.value;
      const b0 = parseFloat(b0Sel.value);

      tVal.textContent = T.toFixed(0) + ' K (' + (T - 273.15).toFixed(0) + '°C)';

      let dGact = barrierMap[trans] || 62.0;
      if (alk === 'tcne') dGact = 135.0; // Rigid metallacyclopropane

      // Rotation rate via Eyring equation: k = (kB*T/h) * exp(-dG/RT)
      const kB = 1.380649e-23;
      const h = 6.62607e-34;
      const R = 8.31446;
      const krot = (kB * T / h) * Math.exp(- (dGact * 1000) / (R * T));

      // Peak separation at slow exchange (Hz)
      const deltaNu = (b0 / 500) * 100; // Hz between inner and outer protons
      // Coalescence condition: k_c = pi * deltaNu / sqrt(2) = 2.22 * deltaNu
      const k_c = (Math.PI * deltaNu) / Math.SQRT2;

      // Approximate T_c:
      const Tc = (dGact * 1000) / (R * Math.log( (kB * 260 / h) / k_c ));

      krotEl.textContent = krot < 1e-2 ? krot.toExponential(2) + ' s⁻¹' : (krot < 1e5 ? krot.toFixed(1) + ' s⁻¹' : krot.toExponential(2) + ' s⁻¹');
      tcEl.textContent = Tc.toFixed(0) + ' K (' + (Tc - 273.15).toFixed(0) + '°C)';

      if (krot < k_c * 0.2) {
        regEl.textContent = 'Slow Exchange (Two distinct proton environments)';
        regEl.style.color = '#58a6ff';
      } else if (krot > k_c * 5.0) {
        regEl.textContent = 'Fast Exchange (Time-averaged sharp singlet)';
        regEl.style.color = '#7ee787';
      } else {
        regEl.textContent = 'Coalescence Regime (Extreme line broadening)';
        regEl.style.color = '#e3b341';
      }

      jptEl.textContent = alk === 'tcne' ? '68 Hz (High sp³ metallacycle character)' : '34 Hz (Pt-195 satellite doublet)';

      ctx.clearRect(0, 0, W, H);

      // Left Panel: Rotating Alkene Complex Animation
      const leftW = W * 0.48;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(20, 20, leftW - 30, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Zeise\'s Salt Anion: [PtCl₃(η²-C₂H₄)]⁻', 35, 45);

      const cx = leftW / 2 - 15;
      const cy = H / 2 + 10;

      // Central Pt(II) atom
      ctx.fillStyle = '#238636';
      ctx.beginPath(); ctx.arc(cx, cy, 20, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = '#30363d'; ctx.stroke();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px system-ui, sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText('Pt(II)', cx, cy);

      // 3 Cl ligands (Square planar coordination)
      // Cl1: left (trans to alkene)
      const xCl_trans = cx - 75;
      const yCl_trans = cy;
      // Cl2: top cis
      const xCl_top = cx;
      const yCl_top = cy - 65;
      // Cl3: bottom cis
      const xCl_bot = cx;
      const yCl_bot = cy + 65;

      ctx.strokeStyle = '#c9d1d9';
      ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(xCl_trans, yCl_trans); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(xCl_top, yCl_top); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(xCl_bot, yCl_bot); ctx.stroke();

      function drawLig(x, y, label, col='#1f6feb') {
        ctx.fillStyle = col;
        ctx.beginPath(); ctx.arc(x, y, 14, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10px system-ui, sans-serif';
        ctx.fillText(label, x, y);
      }
      drawLig(xCl_trans, yCl_trans, trans.toUpperCase(), trans === 'cl' ? '#1f6feb' : '#d29922');
      drawLig(xCl_top, yCl_top, 'Cl');
      drawLig(xCl_bot, yCl_bot, 'Cl');

      // Alkene Centroid on right (at cx + 70)
      const xCent = cx + 70;
      const yCent = cy;

      // Pt - alkene coordination bond (dashed centroid line)
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2.5;
      ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(xCent, yCent); ctx.stroke();
      ctx.setLineDash([]);

      // Rotating C=C axis
      // The alkene rotates around the Pt-Centroid axis (in 3D). We project with rotAngle.
      const cDist = 28;
      const c1x = xCent;
      const c1y = yCent - Math.cos(rotAngle) * cDist;
      const c1z = Math.sin(rotAngle);

      const c2x = xCent;
      const c2y = yCent + Math.cos(rotAngle) * cDist;

      // C=C double bond
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(c1x, c1y); ctx.lineTo(c2x, c2y); ctx.stroke();

      // C atoms
      const r1 = 12 + c1z * 3;
      const r2 = 12 - c1z * 3;
      ctx.fillStyle = '#388bfd';
      ctx.beginPath(); ctx.arc(c1x, c1y, r1, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(c2x, c2y, r2, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 10px system-ui, sans-serif';
      ctx.fillText('C', c1x, c1y);
      ctx.fillText('C', c2x, c2y);

      ctx.textAlign = 'start'; ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = '#8b949e';
      ctx.font = '11px system-ui, sans-serif';
      ctx.fillText('Rotation axis: Pt-Centroid vector | Barrier = ' + dGact.toFixed(0) + ' kJ/mol', 35, H - 35);

      // Right Panel: Dynamic NMR Spectrum (Gutowsky-Holm Simulation)
      const rX = leftW + 10;
      const rW = W - rX - 20;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(rX, 20, rW, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Dynamic ¹H NMR Lineshape Simulation', rX + 15, 45);

      const nX = rX + 35;
      const nY = 70;
      const nW = rW - 50;
      const nH = H - 130;

      ctx.strokeStyle = '#30363d';
      ctx.strokeRect(nX, nY, nW, nH);

      // Two-site exchange lineshape equation (Gutowsky-Holm)
      // I(nu) = proportional to lineshape function
      const tau = 1.0 / (2 * Math.max(1, krot));
      const dW = deltaNu; // Hz between sites (-dW/2 and +dW/2)

      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      const spanHz = 240; // from -120 Hz to +120 Hz
      let maxInt = 0;
      const pts = [];

      for (let i = 0; i <= nW; i++) {
        const freq = - (spanHz / 2) + (i / nW) * spanHz; // relative frequency in Hz
        // Gutowsky-Holm intensity:
        // P = tau * (dW^2 / 4 - freq^2) ...
        const f2 = freq * freq;
        const dW2 = (dW / 2) * (dW / 2);
        const P = tau * (dW2 - f2);
        const Q = -freq * (1.0 + 2.0 * tau * 5.0); // 5Hz natural width
        const denom = (P + 5.0)^2 + (Q)^2 + 1e-4;
        // Simplified two-site exchange lineshape:
        const t2 = 0.05; // natural relaxation
        const k = krot;
        const num = k * (dW * dW);
        const den = Math.pow(dW2 - f2 + k/t2, 2) + 4 * f2 * Math.pow(1/t2 + k, 2) + 1e-6;
        const intensity = 1.0 / ( (Math.pow(dW2 - f2, 2) / (k + 1e-3)) + 4 * f2 * (k + 10) * 0.001 + 0.02 );
        pts.push(intensity);
        if (intensity > maxInt) maxInt = intensity;
      }

      for (let i = 0; i <= nW; i++) {
        const normY = pts[i] / (maxInt + 1e-6);
        const py = nY + nH - 5 - normY * (nH - 20);
        if (i === 0) ctx.moveTo(nX + i, py);
        else ctx.lineTo(nX + i, py);
      }
      ctx.stroke();

      // Axis label
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillStyle = '#8b949e';
      ctx.fillText('-100 Hz', nX + 5, nY + nH + 15);
      ctx.fillText('0 Hz (Avg)', nX + nW/2 - 15, nY + nH + 15);
      ctx.fillText('+100 Hz', nX + nW - 40, nY + nH + 15);

      // Advance rotation angle based on krot
      const speed = Math.min(0.25, Math.max(0.01, Math.log10(krot + 1) * 0.03));
      rotAngle += speed;
      animId = requestAnimationFrame(render);
    }

    [tSlider, transSel, alkSel, b0Sel].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 6: Metallocene Frontier MO Architecture & Ring Rotation
     ========================================================================== */
  function sim_organo_ferrocene_mo_dynamics(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 6: Metallocene Frontier MO Architecture & Ring Rotation</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Sandwich Coordination Chemistry</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Metallocene Complex M(Cp)₂:</label>
            <select id="u6-metal" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="fe" selected>Ferrocene: Fe(Cp)₂ (18e, Diamagnetic, Inactive to Air)</option>
              <option value="co">Cobaltocene: Co(Cp)₂ (19e, 1 unpaired e⁻, Reducing Agent)</option>
              <option value="ni">Nickelocene: Ni(Cp)₂ (20e, 2 unpaired e⁻, Reactive)</option>
              <option value="cr">Chromocene: Cr(Cp)₂ (16e, High Spin S=2)</option>
              <option value="v">Vanadocene: V(Cp)₂ (15e, S=3/2)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Cp Ring Dihedral Angle φ: <span id="u6-phi-val" style="color:#58a6ff; font-weight:bold;">0° (Eclipsed D₅h)</span></label>
            <input type="range" id="u6-phi" min="0" max="36" step="1" value="0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Redox State:</label>
            <select id="u6-redox" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="0" selected>Neutral [M(Cp)₂]⁰</option>
              <option value="1">Monocation [M(Cp)₂]⁺ (Ferrocenium / Cobaltocenium)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Temperature: <span id="u6-t-val" style="color:#58a6ff; font-weight:bold;">298 K</span></label>
            <input type="range" id="u6-t" min="100" max="500" step="10" value="298" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u6-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Valence e⁻: <strong id="u6-val" style="color:#7ee787;">18 e⁻</strong></span>
          <span>Magnetic Moment μ_eff: <strong id="u6-mu" style="color:#58a6ff;">0.00 μ_B (Diamagnetic)</strong></span>
          <span>Point Group Symmetry: <strong id="u6-symm" style="color:#e3b341;">D₅h (Eclipsed Ground State in Gas Phase)</strong></span>
          <span>Rotational Barrier V₀: <strong id="u6-v0" style="color:#d2a8ff;">3.8 kJ/mol (Ultra-Facile Fluxional Ring Rotation)</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u6-canvas');
    const metalSel = el.querySelector('#u6-metal');
    const phiSlider = el.querySelector('#u6-phi');
    const redoxSel = el.querySelector('#u6-redox');
    const tSlider = el.querySelector('#u6-t');

    const phiVal = el.querySelector('#u6-phi-val');
    const tVal = el.querySelector('#u6-t-val');
    const valEl = el.querySelector('#u6-val');
    const muEl = el.querySelector('#u6-mu');
    const symmEl = el.querySelector('#u6-symm');
    const v0El = el.querySelector('#u6-v0');

    const metalData = {
      fe: { baseE: 18, dE: 6, name: 'Fe', v0: 3.8 },
      co: { baseE: 19, dE: 7, name: 'Co', v0: 5.5 },
      ni: { baseE: 20, dE: 8, name: 'Ni', v0: 6.2 },
      cr: { baseE: 16, dE: 4, name: 'Cr', v0: 4.1 },
      v:  { baseE: 15, dE: 3, name: 'V',  v0: 4.8 }
    };

    let ringT = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const mKey = metalSel.value;
      const phi = parseFloat(phiSlider.value);
      const redox = parseInt(redoxSel.value, 10);
      const T = parseFloat(tSlider.value);

      const m = metalData[mKey];
      const totalE = m.baseE - redox;
      const dE = m.dE - redox;

      phiVal.textContent = phi.toFixed(0) + '° (' + (phi === 0 ? 'D₅h Eclipsed' : (phi === 36 ? 'D₅d Staggered' : 'Intermediate')) + ')';
      tVal.textContent = T.toFixed(0) + ' K';
      valEl.textContent = totalE + ' e⁻';
      v0El.textContent = m.v0.toFixed(1) + ' kJ/mol (Ultra-Facile Ring Rotation)';

      let nUnpaired = 0;
      if (totalE === 18) nUnpaired = 0;
      else if (totalE === 19) nUnpaired = 1;
      else if (totalE === 20) nUnpaired = 2;
      else if (totalE === 17) nUnpaired = 1; // Ferrocenium
      else if (totalE === 16) nUnpaired = 2; // Chromocene
      else if (totalE === 15) nUnpaired = 3; // Vanadocene

      const mu = Math.sqrt(nUnpaired * (nUnpaired + 2));
      muEl.textContent = mu.toFixed(2) + ' μ_B (' + (nUnpaired === 0 ? 'Diamagnetic' : nUnpaired + ' Unpaired e⁻') + ')';

      symmEl.textContent = (phi === 0 ? 'D₅h (Eclipsed)' : (phi === 36 ? 'D₅d (Staggered)' : 'C₅ (Chiral Conformer)'));

      ctx.clearRect(0, 0, W, H);

      // Left Panel: 3D-perspective Metallocene Sandwich
      const leftW = W * 0.48;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(20, 20, leftW - 30, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText(`Metallocene Sandwich: ${m.name}(η⁵-C₅H₅)₂`, 35, 45);

      const cx = leftW / 2 - 10;
      const cy = H / 2 + 10;

      // Draw Top Cp Ring (Offset y - 65)
      const topY = cy - 65;
      const botY = cy + 65;

      function drawCpRing(yCenter, rotDeg, fillCol, edgeCol) {
        const radX = 55;
        const radY = 22;
        const pts = [];
        for (let i = 0; i < 5; i++) {
          const ang = ((i * 72 + rotDeg) * Math.PI) / 180;
          pts.push({ x: cx + Math.cos(ang) * radX, y: yCenter + Math.sin(ang) * radY });
        }
        ctx.fillStyle = fillCol;
        ctx.strokeStyle = edgeCol;
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        pts.forEach((p, idx) => {
          if (idx === 0) ctx.moveTo(p.x, p.y);
          else ctx.lineTo(p.x, p.y);
        });
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Carbon vertices
        pts.forEach(p => {
          ctx.fillStyle = '#ffffff';
          ctx.beginPath(); ctx.arc(p.x, p.y, 4, 0, Math.PI * 2); ctx.fill();
        });
      }

      // Coordination centroid dashed bonds to metal
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2;
      ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(cx, topY); ctx.lineTo(cx, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, botY); ctx.lineTo(cx, cy); ctx.stroke();
      ctx.setLineDash([]);

      // Draw Rings
      // Top ring rotates with animation ringT
      drawCpRing(topY, ringT, 'rgba(88, 166, 255, 0.25)', '#58a6ff');
      // Bottom ring rotates with phi offset
      drawCpRing(botY, ringT + phi, 'rgba(88, 166, 255, 0.25)', '#388bfd');

      // Central Metal Sphere
      ctx.fillStyle = '#238636';
      ctx.beginPath(); ctx.arc(cx, cy, 22, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = '#30363d'; ctx.stroke();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px system-ui, sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(m.name, cx, cy);

      ctx.textAlign = 'start'; ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = '#8b949e';
      ctx.font = '11px system-ui, sans-serif';
      ctx.fillText('Centroid-Fe-Centroid = 180° | Fe-C dist = 2.06 Å', 35, H - 35);

      // Right Panel: Frontier MO Diagram (a1g', e2g, e1g*)
      const rX = leftW + 10;
      const rW = W - rX - 20;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(rX, 20, rW, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Frontier MO Splitting (D₅d / D₅h)', rX + 15, 45);

      // Frontier levels:
      // e1g* (LUMO in Ferrocene, antibonding dxz, dyz)
      // a1g' (HOMO in Ferrocene, non-bonding dz²)
      // e2g  (HOMO-1 in Ferrocene, bonding dxy, dx²-y²)
      const moLevels = [
        { name: 'e₁g* (dxz, dyz) - Antibonding', y: 85, deg: 2, col: '#ff7b72' },
        { name: 'a₁g\' (dz²) - Non-bonding', y: 155, deg: 1, col: '#7ee787' },
        { name: 'e₂g (dxy, dx²-y²) - Weakly Bonding', y: 225, deg: 2, col: '#58a6ff' }
      ];

      // Distribute d-electrons (Ferrocene has 6 d-electrons: e2g^4 a1g'^2)
      let rem = dE;
      const occMap = { 'e₂g': 0, 'a₁g\'': 0, 'e₁g*': 0 };

      // Fill e2g (up to 4)
      const putE2g = Math.min(4, rem);
      occMap['e₂g'] = putE2g;
      rem -= putE2g;

      // Fill a1g' (up to 2)
      const putA1g = Math.min(2, rem);
      occMap['a₁g\''] = putA1g;
      rem -= putA1g;

      // Remaining go to e1g* (Cobaltocene, Nickelocene)
      occMap['e₁g*'] = Math.min(4, rem);

      moLevels.forEach(lvl => {
        const shortKey = lvl.name.split(' ')[0];
        const occ = occMap[shortKey] || 0;
        const totalW = lvl.deg * 45 + (lvl.deg - 1) * 15;
        const startX = rX + 60;

        ctx.font = '11px system-ui, sans-serif';
        ctx.fillStyle = lvl.col;
        ctx.fillText(lvl.name, startX + totalW + 15, lvl.y + 4);

        for (let i = 0; i < lvl.deg; i++) {
          const ox = startX + i * 60;
          ctx.strokeStyle = lvl.col;
          ctx.lineWidth = 2.5;
          ctx.beginPath(); ctx.moveTo(ox, lvl.y); ctx.lineTo(ox + 45, lvl.y); ctx.stroke();

          let numArrow = 0;
          if (occ > i * 2 + 1) numArrow = 2;
          else if (occ > i * 2) numArrow = 1;

          if (numArrow >= 1) {
            ctx.fillStyle = '#58a6ff';
            ctx.beginPath();
            ctx.moveTo(ox + 15, lvl.y + 12); ctx.lineTo(ox + 15, lvl.y - 12); ctx.lineTo(ox + 9, lvl.y - 6);
            ctx.stroke();
          }
          if (numArrow === 2) {
            ctx.fillStyle = '#f0883e';
            ctx.beginPath();
            ctx.moveTo(ox + 30, lvl.y - 12); ctx.lineTo(ox + 30, lvl.y + 12); ctx.lineTo(ox + 36, lvl.y + 6);
            ctx.stroke();
          }
        }
      });

      ringT += 0.5;
      animId = requestAnimationFrame(render);
    }

    [metalSel, phiSlider, redoxSel, tSlider].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 7: Wade-Mingos Polyhedral Cluster (PSEPT) Engine
     ========================================================================== */
  function sim_organo_wade_mingos_cluster_psept(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 7: Wade-Mingos Polyhedral Cluster (PSEPT) Architecture</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Polyhedral Skeletal Electron Pair Theory</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">High-Nuclearity Carbonyl Cluster:</label>
            <select id="u7-cluster" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="rh6" selected>Rh₆(CO)₁₆ (Octahedron, Closo, 86 TVE)</option>
              <option value="fe5c">Fe₅C(CO)₁₅ (Square Pyramid, Nido, 74 TVE)</option>
              <option value="os6">Os₆(CO)₁₈ (Octahedron, Closo, 86 TVE)</option>
              <option value="fe4c">Fe₄(CO)₁₃²⁻ (Tetrahedron, Closo, 60 TVE)</option>
              <option value="os3">Os₃(CO)₁₂ (Trigonal Ring, 48 TVE)</option>
              <option value="b10h14">B₁₀H₁₄ (Nido-borane benchmark, 12 SEP)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Cluster Structural Class:</label>
            <select id="u7-type" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="closo" selected>Closo (Complete Polyhedron, n+1 SEP)</option>
              <option value="nido">Nido (1 Missing Vertex, n+2 SEP)</option>
              <option value="arachno">Arachno (2 Missing Vertices, n+3 SEP)</option>
              <option value="hypho">Hypho (3 Missing Vertices, n+4 SEP)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">3D Cage Rotation Speed: <span id="u7-rot-val" style="color:#58a6ff; font-weight:bold;">1.0×</span></label>
            <input type="range" id="u7-rot" min="0" max="3" step="0.2" value="1.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Display Mode:</label>
            <select id="u7-disp" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="poly" selected>Polyhedral Wireframe + Solid Facets</option>
              <option value="orbitals">Skeletal Core Bonding MO Centroid</option>
            </select>
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u7-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Total Valence Electrons: <strong id="u7-tve" style="color:#7ee787;">86 e⁻</strong></span>
          <span>Skeletal Electron Pairs (SEP): <strong id="u7-sep" style="color:#58a6ff;">7 Pairs (n + 1)</strong></span>
          <span>Parent Polyhedron: <strong id="u7-parent" style="color:#e3b341;">Octahedron (Oh)</strong></span>
          <span>Formula: <strong id="u7-formula" style="color:#d2a8ff;">SEP = [TVE - 12n] / 2 = [86 - 72] / 2 = 7</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u7-canvas');
    const clustSel = el.querySelector('#u7-cluster');
    const typeSel = el.querySelector('#u7-type');
    const rotSlider = el.querySelector('#u7-rot');
    const dispSel = el.querySelector('#u7-disp');

    const rotVal = el.querySelector('#u7-rot-val');
    const tveEl = el.querySelector('#u7-tve');
    const sepEl = el.querySelector('#u7-sep');
    const parentEl = el.querySelector('#u7-parent');
    const formEl = el.querySelector('#u7-formula');

    const clusterData = {
      rh6: { n: 6, tve: 86, sep: 7, name: 'Rh₆(CO)₁₆', parent: 'Octahedron', type: 'closo', verts: [
        [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]
      ]},
      fe5c: { n: 5, tve: 74, sep: 7, name: 'Fe₅C(CO)₁₅', parent: 'Octahedron (1 vertex removed)', type: 'nido', verts: [
        [0, 1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]
      ]},
      os6: { n: 6, tve: 86, sep: 7, name: 'Os₆(CO)₁₈', parent: 'Octahedron', type: 'closo', verts: [
        [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]
      ]},
      fe4c: { n: 4, tve: 60, sep: 6, name: 'Fe₄(CO)₁₃²⁻', parent: 'Tetrahedron / TBP parent', type: 'closo', verts: [
        [1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]
      ]},
      os3: { n: 3, tve: 48, sep: 6, name: 'Os₃(CO)₁₂', parent: 'Trigonal Triangle (Localized M-M)', type: 'closo', verts: [
        [0, 1, 0], [0.866, -0.5, 0], [-0.866, -0.5, 0]
      ]},
      b10h14: { n: 10, tve: 44, sep: 12, name: 'B₁₀H₁₄', parent: 'Icosahedron (2 vertices removed)', type: 'nido', verts: [
        [0, 1, 0.5], [0.8, 0.5, 0.3], [-0.8, 0.5, 0.3], [0.5, -0.5, 0.6], [-0.5, -0.5, 0.6],
        [0.8, -0.5, -0.3], [-0.8, -0.5, -0.3], [0, 0.5, -0.7], [0.4, 0, -0.8], [-0.4, 0, -0.8]
      ]}
    };

    let angX = 0.4;
    let angY = 0.6;
    let animId = null;

    clustSel.addEventListener('change', () => {
      const cd = clusterData[clustSel.value];
      if (cd) {
        typeSel.value = cd.type;
        render();
      }
    });

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const cKey = clustSel.value;
      const cd = clusterData[cKey];
      const rSpeed = parseFloat(rotSlider.value);
      const disp = dispSel.value;

      rotVal.textContent = rSpeed.toFixed(1) + '×';
      tveEl.textContent = cd.tve + ' e⁻';
      sepEl.textContent = `${cd.sep} Pairs (${cd.type === 'closo' ? 'n + 1' : 'n + 2'})`;
      parentEl.textContent = cd.parent;
      formEl.textContent = `SEP = [TVE - 12n]/2 = [${cd.tve} - ${12*cd.n}]/2 = ${cd.sep}`;

      ctx.clearRect(0, 0, W, H);

      // Left Panel: 3D Isometric Cluster Wireframe
      const leftW = W * 0.52;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(20, 20, leftW - 30, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText(`Polyhedral Cage: ${cd.name} [${cd.type.toUpperCase()}]`, 35, 45);

      const cx = leftW / 2 - 10;
      const cy = H / 2 + 10;
      const scale = 75;

      // Project 3D vertices with rotations angX and angY
      const projVerts = cd.verts.map(v => {
        let x = v[0], y = v[1], z = v[2];
        // Rotate Y
        let x1 = x * Math.cos(angY) + z * Math.sin(angY);
        let z1 = -x * Math.sin(angY) + z * Math.cos(angY);
        // Rotate X
        let y2 = y * Math.cos(angX) - z1 * Math.sin(angX);
        let z2 = y * Math.sin(angX) + z1 * Math.cos(angX);
        return { px: cx + x1 * scale, py: cy + y2 * scale, pz: z2 };
      });

      // Draw Edges (connect all close pairs)
      ctx.strokeStyle = '#388bfd';
      ctx.lineWidth = 2;
      for (let i = 0; i < projVerts.length; i++) {
        for (let j = i + 1; j < projVerts.length; j++) {
          const v1 = cd.verts[i];
          const v2 = cd.verts[j];
          const dist3d = Math.sqrt(Math.pow(v1[0]-v2[0], 2) + Math.pow(v1[1]-v2[1], 2) + Math.pow(v1[2]-v2[2], 2));
          // Connect if neighbor
          if (dist3d < 2.1) {
            ctx.beginPath();
            ctx.moveTo(projVerts[i].px, projVerts[i].py);
            ctx.lineTo(projVerts[j].px, projVerts[j].py);
            ctx.stroke();
          }
        }
      }

      // Draw Skeletal Core Centroid
      if (disp === 'orbitals') {
        ctx.fillStyle = 'rgba(210, 168, 255, 0.25)';
        ctx.beginPath();
        ctx.arc(cx, cy, 35, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#d2a8ff';
        ctx.setLineDash([3, 3]);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#d2a8ff';
        ctx.font = '10px system-ui, sans-serif';
        ctx.fillText('Delocalized a1g Cluster Core', cx - 55, cy - 40);
      }

      // Draw Vertices
      projVerts.forEach((pv, idx) => {
        ctx.fillStyle = '#238636';
        ctx.beginPath();
        ctx.arc(pv.px, pv.py, 10, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 9px system-ui, sans-serif';
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(idx + 1, pv.px, pv.py);
      });

      ctx.textAlign = 'start'; ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = '#8b949e';
      ctx.font = '11px system-ui, sans-serif';
      ctx.fillText(`${cd.n} Vertices | PSEPT Classification: ${cd.type.toUpperCase()}`, 35, H - 35);

      // Right Panel: Wade-Mingos Electron Accounting Card
      const rX = leftW + 10;
      const rW = W - rX - 20;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(rX, 20, rW, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Wade-Mingos (PSEPT) Rules Audit', rX + 15, 45);

      ctx.font = '12px system-ui, sans-serif';
      ctx.fillStyle = '#c9d1d9';
      ctx.fillText(`• Metal Vertices (n): ${cd.n}`, rX + 15, 75);
      ctx.fillText(`• Total Valence Electrons (TVE): ${cd.tve}`, rX + 15, 95);
      ctx.fillText(`• Core Cluster Orbitals: 12 × n = ${12 * cd.n} e⁻`, rX + 15, 115);
      ctx.fillStyle = '#7ee787';
      ctx.fillText(`• Skeletal Bonding Electrons: ${cd.tve - 12 * cd.n} e⁻`, rX + 15, 140);
      ctx.fillText(`• Skeletal Electron Pairs: ${cd.sep} pairs`, rX + 15, 160);

      // Classification table mini-view
      ctx.fillStyle = '#21262d';
      ctx.fillRect(rX + 15, 180, rW - 30, 85);
      ctx.strokeStyle = '#30363d';
      ctx.strokeRect(rX + 15, 180, rW - 30, 85);

      ctx.font = '11px system-ui, sans-serif';
      ctx.fillStyle = '#8b949e';
      ctx.fillText('Polyhedral Geometry Spectrum:', rX + 22, 198);
      ctx.fillStyle = cd.type === 'closo' ? '#7ee787' : '#c9d1d9';
      ctx.fillText('• Closo: [n + 1] SEP → Closed Polyhedron', rX + 22, 216);
      ctx.fillStyle = cd.type === 'nido' ? '#7ee787' : '#c9d1d9';
      ctx.fillText('• Nido: [n + 2] SEP → 1 Vertex Missing (Nest)', rX + 22, 234);
      ctx.fillStyle = cd.type === 'arachno' ? '#7ee787' : '#c9d1d9';
      ctx.fillText('• Arachno: [n + 3] SEP → 2 Vertices Missing (Web)', rX + 22, 252);

      angX += 0.008 * rSpeed;
      angY += 0.012 * rSpeed;
      animId = requestAnimationFrame(render);
    }

    [clustSel, typeSel, rotSlider, dispSel].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 8: Oxidative Addition & Reductive Elimination Energy Landscapes
     ========================================================================== */
  function sim_organo_oxidative_addition_reductive_elim(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 8: Oxidative Addition & Reductive Elimination Free Energy Landscapes</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Diphosphine Bite Angle & Electronics</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Substrate Bond X-Y:</label>
            <select id="u8-sub" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="h2" selected>H-H (Nonpolar Concerted 3-Centered TS)</option>
              <option value="mei">Me-I (Polar S_N2 Nucleophilic Attack)</option>
              <option value="phbr">Ph-Br (Aromatic Concerted Pathway)</option>
              <option value="sih">Et₃Si-H (Polarized σ-bond activation)</option>
              <option value="meme">Me-Me (High C-C barrier, ~140 kJ/mol)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Diphosphine Bite Angle β_n:</label>
            <select id="u8-bite" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="78">dppm: 78° (Favors small angle / Octahedral)</option>
              <option value="85" selected>dppe: 85° (Intermediate bite angle)</option>
              <option value="92">dppp: 92° (Balanced bite angle)</option>
              <option value="99">dppb: 99° (Wide bite angle)</option>
              <option value="111">Xantphos: 111° (Wide bite angle: Promotes Reductive Elim!)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Metal Electron Richness: <span id="u8-rich-val" style="color:#58a6ff; font-weight:bold;">High [Ir(I) / Pt(0)]</span></label>
            <input type="range" id="u8-rich" min="1" max="5" step="1" value="4" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Temperature: <span id="u8-t-val" style="color:#58a6ff; font-weight:bold;">298 K</span></label>
            <input type="range" id="u8-t" min="200" max="450" step="10" value="298" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u8-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>ΔG‡ (Oxidative Addition): <strong id="u8-dgoa" style="color:#7ee787;">52.4 kJ/mol</strong></span>
          <span>ΔG‡ (Reductive Elimination): <strong id="u8-dgre" style="color:#58a6ff;">84.2 kJ/mol</strong></span>
          <span>Net ΔG°_rxn: <strong id="u8-dgnet" style="color:#e3b341;">-31.8 kJ/mol (Exergonic OA)</strong></span>
          <span>Mechanism: <strong id="u8-mech" style="color:#d2a8ff;">Concerted 3-Centered Non-Polar TS</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u8-canvas');
    const subSel = el.querySelector('#u8-sub');
    const biteSel = el.querySelector('#u8-bite');
    const richSlider = el.querySelector('#u8-rich');
    const tSlider = el.querySelector('#u8-t');

    const richVal = el.querySelector('#u8-rich-val');
    const tVal = el.querySelector('#u8-t-val');
    const dgoaEl = el.querySelector('#u8-dgoa');
    const dgreEl = el.querySelector('#u8-dgre');
    const dgnetEl = el.querySelector('#u8-dgnet');
    const mechEl = el.querySelector('#u8-mech');

    const subParams = {
      h2: { baseOA: 55.0, dG0: -40.0, mech: 'Concerted 3-Centered TS (Retention)' },
      mei: { baseOA: 62.0, dG0: -75.0, mech: 'Polar SN2 Inversion TS (Linear M-C-I)' },
      phbr: { baseOA: 80.0, dG0: -50.0, mech: 'Concerted Aryl Coordination Pathway' },
      sih: { baseOA: 58.0, dG0: -35.0, mech: 'Polarized σ-Bond Activation' },
      meme: { baseOA: 140.0, dG0: +15.0, mech: 'Spatially Hindered High Barrier' }
    };

    let rxnCoord = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const sub = subSel.value;
      const bite = parseFloat(biteSel.value);
      const rich = parseInt(richSlider.value, 10);
      const T = parseFloat(tSlider.value);

      const richLabels = ['', 'Very Low [Pt(II)]', 'Low [Pd(II)]', 'Moderate [Rh(I)]', 'High [Ir(I)]', 'Extremely High [Pt(0)]'];
      richVal.textContent = richLabels[rich] || 'Moderate';
      tVal.textContent = T.toFixed(0) + ' K';

      const sp = subParams[sub];
      mechEl.textContent = sp.mech;

      // Influence of bite angle: wide bite angle destabilizes square planar (16e) or stabilizes linear (14e),
      // dramatically lowering Reductive Elimination barrier!
      // Wide bite angle (e.g. Xantphos 111°) increases OA barrier slightly and decreases RE barrier dramatically.
      const biteFactorOA = (bite - 85) * 0.25;
      const biteFactorRE = - (bite - 85) * 0.65; // Wide bite accelerates RE!

      // Influence of electron richness: rich metal center accelerates OA (lowers OA barrier)
      const richFactorOA = - (rich - 3) * 12.0;
      const richFactorRE = + (rich - 3) * 10.0;

      const dG_OA = Math.max(20.0, sp.baseOA + biteFactorOA + richFactorOA);
      const dG_net = sp.dG0 + (richFactorOA * 0.5) - (biteFactorRE * 0.3);
      const dG_RE = Math.max(25.0, dG_OA - dG_net + biteFactorRE);

      dgoaEl.textContent = dG_OA.toFixed(1) + ' kJ/mol';
      dgreEl.textContent = dG_RE.toFixed(1) + ' kJ/mol';
      dgnetEl.textContent = `${dG_net.toFixed(1)} kJ/mol (${dG_net < 0 ? 'Exergonic OA' : 'Endergonic OA'})`;

      ctx.clearRect(0, 0, W, H);

      // Left Panel: Free Energy Reaction Coordinate Diagram
      const leftW = W * 0.52;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(20, 20, leftW - 30, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Free Energy Profile: OA ⇌ [TS]‡ ⇌ RE', 35, 45);

      const pX = 55;
      const pY = 75;
      const pW = leftW - 100;
      const pH = H - 140;

      ctx.strokeStyle = '#30363d';
      ctx.strokeRect(pX, pY, pW, pH);

      // Reactant Level (L_n M + X-Y) at left
      const yReact = pY + pH * 0.6;
      // TS Level at center
      const yTS = yReact - (dG_OA / 160.0) * (pH * 0.65);
      // Product Level (L_n M(X)(Y)) at right
      const yProd = yReact + (dG_net / 160.0) * (pH * 0.65);

      // Draw Energy Curve (spline)
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(pX, yReact);
      ctx.bezierCurveTo(pX + pW * 0.25, yReact, pX + pW * 0.35, yTS, pX + pW * 0.5, yTS);
      ctx.bezierCurveTo(pX + pW * 0.65, yTS, pX + pW * 0.75, yProd, pX + pW, yProd);
      ctx.stroke();

      // State markers and labels
      ctx.fillStyle = '#7ee787';
      ctx.fillRect(pX - 10, yReact - 3, 20, 6);
      ctx.fillStyle = '#ff7b72';
      ctx.fillRect(pX + pW * 0.5 - 10, yTS - 3, 20, 6);
      ctx.fillStyle = '#d29922';
      ctx.fillRect(pX + pW - 10, yProd - 3, 20, 6);

      ctx.font = '11px system-ui, sans-serif';
      ctx.fillStyle = '#c9d1d9';
      ctx.fillText('LₙM + X-Y', pX + 5, yReact + 18);
      ctx.fillStyle = '#ff7b72';
      ctx.fillText(`[TS]‡ (ΔG‡_OA = ${dG_OA.toFixed(1)})`, pX + pW * 0.3, yTS - 10);
      ctx.fillStyle = '#c9d1d9';
      ctx.fillText('LₙM(X)(Y)', pX + pW - 55, yProd + 18);

      // Animated traveling reaction coordinate dot
      const rxnNorm = (Math.sin(rxnCoord) + 1) / 2; // 0 to 1
      const curX = pX + rxnNorm * pW;
      // Evaluate bezier Y at rxnNorm
      let curY = yReact;
      if (rxnNorm < 0.5) {
        const u = rxnNorm / 0.5;
        curY = (1-u)*(1-u)*yReact + 2*(1-u)*u*yTS + u*u*yTS;
      } else {
        const u = (rxnNorm - 0.5) / 0.5;
        curY = (1-u)*(1-u)*yTS + 2*(1-u)*u*yProd + u*u*yProd;
      }

      ctx.fillStyle = '#ffffff';
      ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();

      // Right Panel: Coordination Geometry & Bite Angle Visualizer
      const rX = leftW + 10;
      const rW = W - rX - 20;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(rX, 20, rW, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText(`Diphosphine Bite Angle: β = ${bite}°`, rX + 15, 45);

      const cx = rX + rW / 2;
      const cy = H / 2 + 10;

      // Central Metal
      ctx.fillStyle = '#238636';
      ctx.beginPath(); ctx.arc(cx, cy, 20, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 11px system-ui, sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText('M', cx, cy);

      // Two Phosphines at angle +/- bite/2 from the left
      const radBite = (bite * Math.PI) / 180;
      const rP = 70;
      const xP1 = cx - Math.cos(-radBite / 2) * rP;
      const yP1 = cy + Math.sin(-radBite / 2) * rP;
      const xP2 = cx - Math.cos(radBite / 2) * rP;
      const yP2 = cy + Math.sin(radBite / 2) * rP;

      ctx.strokeStyle = '#c9d1d9';
      ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(xP1, yP1); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(xP2, yP2); ctx.stroke();

      // Chelate backbone link
      ctx.strokeStyle = '#6e7681';
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(xP1, yP1); ctx.lineTo(cx - 95, cy); ctx.lineTo(xP2, yP2); ctx.stroke();

      function drawP(x, y) {
        ctx.fillStyle = '#d2a8ff';
        ctx.beginPath(); ctx.arc(x, y, 14, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10px system-ui, sans-serif';
        ctx.fillText('PR₂', x, y);
      }
      drawP(xP1, yP1);
      drawP(xP2, yP2);

      // Bite Angle Arc
      ctx.strokeStyle = '#e3b341';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(cx, cy, 35, Math.PI - radBite/2, Math.PI + radBite/2);
      ctx.stroke();
      ctx.fillStyle = '#e3b341';
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillText(`${bite}°`, cx - 50, cy);

      // Incoming / Cleaving X and Y on the right
      const xX = cx + 60;
      const yX = cy - 25 * (1 - rxnNorm);
      const xY = cx + 60;
      const yY = cy + 25 * (1 - rxnNorm);

      ctx.fillStyle = '#da3633';
      ctx.beginPath(); ctx.arc(xX, yX, 12, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(xY, yY, 12, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.fillText('X', xX, yX);
      ctx.fillText('Y', xY, yY);

      ctx.textAlign = 'start'; ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = '#8b949e';
      ctx.font = '11px system-ui, sans-serif';
      ctx.fillText('Wide bite angle sterically forces cis-ligands together → accelerates RE', rX + 15, H - 35);

      rxnCoord += 0.03;
      animId = requestAnimationFrame(render);
    }

    [subSel, biteSel, richSlider, tSlider].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 9: Wilkinson's Homogeneous Catalysis State Machine
     ========================================================================== */
  function sim_organo_wilkinson_hydrogenation_cycle(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 9: Wilkinson's Homogeneous Catalysis State Machine</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Catalytic Cycle Kinetic Flux Engine</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Olefin Substrate:</label>
            <select id="u9-sub" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="cyclohexene" selected>Cyclohexene (Standard substrate)</option>
              <option value="1hexene">1-Hexene (Fast terminal alkene, TOF 2×)</option>
              <option value="styrene">Styrene (Conjugated alkene)</option>
              <option value="stilbene">trans-Stilbene (Hindered disubstituted, TOF 0.05×)</option>
              <option value="tetrameth">Tetramethylethylene (Sterically blocked, NO reaction)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Hydrogen Pressure P_H₂: <span id="u9-ph2-val" style="color:#58a6ff; font-weight:bold;">1.0 atm</span></label>
            <input type="range" id="u9-ph2" min="0.1" max="5.0" step="0.1" value="1.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Added Free PPh₃ (Inhibitor):</label>
            <select id="u9-pph3" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="0" selected>None (Standard Dissociation Equilibrium)</option>
              <option value="1">Low (+1 equivalent PPh₃, 40% Inhibition)</option>
              <option value="5">Excess (+5 equivalents PPh₃, 85% Inhibition)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Catalyst Loading [Rh]₀: <span id="u9-cat-val" style="color:#58a6ff; font-weight:bold;">1.0 mM</span></label>
            <input type="range" id="u9-cat" min="0.1" max="5.0" step="0.1" value="1.0" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u9-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Turnover Frequency (TOF): <strong id="u9-tof" style="color:#7ee787;">650 h⁻¹</strong></span>
          <span>Turnover Number (TON): <strong id="u9-ton" style="color:#58a6ff;">1,300</strong></span>
          <span>Rate-Determining Step: <strong id="u9-rds" style="color:#e3b341;">Migratory Insertion (Alkyl Hydride Formation)</strong></span>
          <span>Active Catalyst: <strong id="u9-active" style="color:#d2a8ff;">14e RhCl(PPh₃)₂ (Phosphine Dissociated)</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u9-canvas');
    const subSel = el.querySelector('#u9-sub');
    const ph2Slider = el.querySelector('#u9-ph2');
    const pph3Sel = el.querySelector('#u9-pph3');
    const catSlider = el.querySelector('#u9-cat');

    const ph2Val = el.querySelector('#u9-ph2-val');
    const catVal = el.querySelector('#u9-cat-val');
    const tofEl = el.querySelector('#u9-tof');
    const tonEl = el.querySelector('#u9-ton');
    const rdsEl = el.querySelector('#u9-rds');
    const activeEl = el.querySelector('#u9-active');

    const subRates = {
      cyclohexene: 1.0,
      '1hexene': 2.2,
      styrene: 1.5,
      stilbene: 0.05,
      tetrameth: 0.00
    };

    let fluxPhase = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const sub = subSel.value;
      const pH2 = parseFloat(ph2Slider.value);
      const pph3 = parseInt(pph3Sel.value, 10);
      const cCat = parseFloat(catSlider.value);

      ph2Val.textContent = pH2.toFixed(1) + ' atm';
      catVal.textContent = cCat.toFixed(1) + ' mM';

      const baseRate = subRates[sub] || 1.0;
      let inhib = 1.0;
      if (pph3 === 1) inhib = 0.6;
      if (pph3 === 5) inhib = 0.15;

      const tof = baseRate * pH2 * inhib * 650.0;
      tofEl.textContent = tof > 0 ? tof.toFixed(0) + ' h⁻¹' : '0 h⁻¹ (Sterically Inaccessible)';
      tonEl.textContent = (tof * 2.0).toFixed(0);

      if (sub === 'tetrameth') {
        rdsEl.textContent = 'Steric Blocking: Alkene cannot coordinate to Rh';
        activeEl.textContent = 'Dihydride Dimer Resting State';
      } else {
        rdsEl.textContent = 'Migratory Insertion (Alkyl Hydride Formation)';
        activeEl.textContent = '14e RhCl(PPh₃)₂ (Phosphine Dissociated)';
      }

      ctx.clearRect(0, 0, W, H);

      // Catalytic Cycle Circular Layout
      const cx = W / 2;
      const cy = H / 2;
      const R_cycle = Math.min(W, H) * 0.35;

      // 5 Major Species around the circle:
      // 1. Top: RhCl(PPh3)3 (16e Pre-catalyst) -> [dissociation]
      // 2. Top-Right: RhCl(PPh3)2 (14e Active)
      // 3. Right: RhCl(H)2(PPh3)2 (16e Dihydride via OA of H2)
      // 4. Bottom: RhCl(H)2(alkene)(PPh3)2 (18e Alkene Adduct)
      // 5. Left: RhCl(H)(alkyl)(PPh3)2 (16e Alkyl Hydride via Insertion)
      const states = [
        { label: 'RhCl(PPh₃)₂', sub: '14e Active', ang: -Math.PI / 2, col: '#58a6ff' },
        { label: 'RhCl(H)₂(PPh₃)₂', sub: '16e Dihydride', ang: -Math.PI / 6, col: '#7ee787' },
        { label: 'RhCl(H)₂(alkene)(PPh₃)', sub: '18e Alkene Adduct', ang: Math.PI / 3, col: '#d2a8ff' },
        { label: 'RhCl(H)(alkyl)(PPh₃)', sub: '16e Alkyl Hydride', ang: Math.PI * 0.85, col: '#e3b341' },
        { label: 'Alkane Elimination', sub: 'Reductive Elim', ang: -Math.PI * 0.75, col: '#ff7b72' }
      ];

      // Draw Cycle Ring
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.arc(cx, cy, R_cycle, 0, Math.PI * 2);
      ctx.stroke();

      // Draw Animated Flux Pulses along cycle
      if (tof > 0) {
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 3;
        ctx.setLineDash([12, 18]);
        ctx.lineDashOffset = -fluxPhase * 25;
        ctx.beginPath();
        ctx.arc(cx, cy, R_cycle, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Draw State Nodes
      states.forEach((st, idx) => {
        const sx = cx + Math.cos(st.ang) * R_cycle;
        const sy = cy + Math.sin(st.ang) * R_cycle;

        ctx.fillStyle = '#161b22';
        ctx.strokeStyle = st.col;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(sx, sy, 26, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(idx + 1, sx, sy - 5);
        ctx.fillStyle = st.col;
        ctx.font = '9px system-ui, sans-serif';
        ctx.fillText(st.sub.split(' ')[0], sx, sy + 7);

        // Outside Label
        const lx = cx + Math.cos(st.ang) * (R_cycle + 48);
        const ly = cy + Math.sin(st.ang) * (R_cycle + 42);
        ctx.fillStyle = '#c9d1d9';
        ctx.font = '10px system-ui, sans-serif';
        ctx.fillText(st.label, lx, ly);
      });

      // Center Hub: Cycle Metadata & Chemical Input/Outputs
      ctx.fillStyle = '#161b22';
      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.arc(cx, cy, 42, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 11px system-ui, sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText('Wilkinson', cx, cy - 8);
      ctx.fillStyle = '#7ee787';
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillText(`${tof.toFixed(0)} h⁻¹`, cx, cy + 8);

      ctx.textAlign = 'start'; ctx.textBaseline = 'alphabetic';

      // Reagent Inputs & Outputs annotations
      ctx.fillStyle = '#7ee787';
      ctx.font = 'bold 10px system-ui, sans-serif';
      ctx.fillText('+ H₂ (Oxidative Addition)', cx + R_cycle * 0.65, cy - R_cycle * 0.7);

      ctx.fillStyle = '#d2a8ff';
      ctx.fillText('+ Alkene', cx + R_cycle * 0.75, cy + R_cycle * 0.55);

      ctx.fillStyle = '#ff7b72';
      ctx.fillText('– Alkane Product', cx - R_cycle - 20, cy - R_cycle * 0.65);

      fluxPhase += 0.05 * (tof / 650.0);
      animId = requestAnimationFrame(render);
    }

    [subSel, ph2Slider, pph3Sel, catSlider].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 10: Cossee-Arlman Olefin Polymerization & Chain Kinetics
     ========================================================================== */
  function sim_organo_olefin_polymerization_kinetics(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h4 style="margin:0; color:#58a6ff; font-size:16px;">Unit 10: Cossee-Arlman Olefin Polymerization & Chain Kinetics</h4>
          <span style="font-size:12px; background:#1f242c; padding:3px 8px; border-radius:4px; border:1px solid #30363d;">Ziegler-Natta & Metallocene Polymerization</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:14px; background:#161b22; padding:12px; border-radius:6px;">
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Catalyst Architecture:</label>
            <select id="u10-cat" style="width:100%; background:#0d1117; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
              <option value="meta" selected>Metallocene Cp₂ZrCl₂/MAO (Single-Site, PDI = 2.0)</option>
              <option value="zn">Heterogeneous TiCl₄/MgCl₂ (Multi-Site, Broad PDI = 5.5)</option>
              <option value="brook">Brookhart Ni(II) Diimine (Chain Walking Branching)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Ethylene Pressure P_monomer: <span id="u10-p-val" style="color:#58a6ff; font-weight:bold;">5.0 bar</span></label>
            <input type="range" id="u10-p" min="1.0" max="20.0" step="0.5" value="5.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Hydrogen Chain Transfer [H₂]: <span id="u10-h2-val" style="color:#58a6ff; font-weight:bold;">0.5 mol%</span></label>
            <input type="range" id="u10-h2" min="0.0" max="3.0" step="0.1" value="0.5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:12px; color:#8b949e; display:block; margin-bottom:4px;">Reaction Time t: <span id="u10-t-val" style="color:#58a6ff; font-weight:bold;">30 min</span></label>
            <input type="range" id="u10-t" min="5" max="120" step="5" value="30" style="width:100%;">
          </div>
        </div>
        <div style="position:relative; width:100%; height:340px; background:#010409; border-radius:6px; border:1px solid #30363d; overflow:hidden;">
          <canvas class="sim-canvas" id="u10-canvas" style="width:100%; height:100%; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:12px; color:#8b949e; flex-wrap:wrap; gap:8px;">
          <span>Number-Avg MW (M_n): <strong id="u10-mn" style="color:#7ee787;">142,000 g/mol</strong></span>
          <span>Weight-Avg MW (M_w): <strong id="u10-mw" style="color:#58a6ff;">284,000 g/mol</strong></span>
          <span>Polydispersity Index (PDI): <strong id="u10-pdi" style="color:#e3b341;">2.00 (Flory-Schulz Limit)</strong></span>
          <span>Polymer Yield: <strong id="u10-yield" style="color:#d2a8ff;">18.5 kg PE / (mol Zr · h · bar)</strong></span>
        </div>
      </div>
    `;

    const canvas = el.querySelector('#u10-canvas');
    const catSel = el.querySelector('#u10-cat');
    const pSlider = el.querySelector('#u10-p');
    const h2Slider = el.querySelector('#u10-h2');
    const tSlider = el.querySelector('#u10-t');

    const pVal = el.querySelector('#u10-p-val');
    const h2Val = el.querySelector('#u10-h2-val');
    const tVal = el.querySelector('#u10-t-val');
    const mnEl = el.querySelector('#u10-mn');
    const mwEl = el.querySelector('#u10-mw');
    const pdiEl = el.querySelector('#u10-pdi');
    const yieldEl = el.querySelector('#u10-yield');

    let phase = 0;
    let animId = null;

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width: W, height: H } = c;

      const cat = catSel.value;
      const P = parseFloat(pSlider.value);
      const H2 = parseFloat(h2Slider.value);
      const timeMin = parseFloat(tSlider.value);

      pVal.textContent = P.toFixed(1) + ' bar';
      h2Val.textContent = H2.toFixed(1) + ' mol%';
      tVal.textContent = timeMin.toFixed(0) + ' min';

      // Kinetics:
      // Rp = kp * [Zr*] * [M]
      // Transfer rate: R_tr = k_beta + k_H2 * [H2]
      // DP_n = Rp / R_tr
      const kp = cat === 'meta' ? 5000 : (cat === 'brook' ? 3200 : 2100);
      const kBeta = 0.05;
      const kH2 = 1.2;

      const rateTr = kBeta + kH2 * H2;
      const dpN = Math.round((P * 1500) / rateTr);
      const Mn = dpN * 28; // 28 g/mol for ethylene monomer

      let pdi = 2.0;
      if (cat === 'zn') pdi = 5.5;
      if (cat === 'brook') pdi = 2.4;

      const Mw = Math.round(Mn * pdi);
      const yieldKg = (P * (timeMin / 60) * (cat === 'meta' ? 3.7 : 1.8)).toFixed(1);

      mnEl.textContent = Mn.toLocaleString() + ' g/mol';
      mwEl.textContent = Mw.toLocaleString() + ' g/mol';
      pdiEl.textContent = pdi.toFixed(2) + (cat === 'meta' ? ' (Flory-Schulz Single-Site)' : ' (Multi-Site Heterogeneous)');
      yieldEl.textContent = yieldKg + ' kg PE / (mol Cat · h)';

      ctx.clearRect(0, 0, W, H);

      // Left Panel: Animated Cossee-Arlman Migratory Insertion
      const leftW = W * 0.48;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(20, 20, leftW - 30, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Cossee-Arlman Coordination & Insertion Mechanism', 35, 45);

      const cx = leftW / 2 - 10;
      const cy = H / 2 + 10;

      // Active Cationic Metal Center [Cp2Zr-R]+
      ctx.fillStyle = '#238636';
      ctx.beginPath(); ctx.arc(cx - 50, cy, 22, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = '#30363d'; ctx.stroke();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px system-ui, sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(cat === 'meta' ? 'Zr⁺' : (cat === 'brook' ? 'Ni⁺' : 'Ti⁺'), cx - 50, cy);

      // Incoming Ethylene coordination at cis-vacant site
      const osc = Math.sin(phase * 4);
      const xEth = cx + 25 - (osc > 0 ? osc * 20 : 0);
      const yEth = cy - 35 + (osc > 0 ? osc * 15 : 0);

      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(xEth, yEth - 10); ctx.lineTo(xEth, yEth + 10); ctx.stroke();

      ctx.fillStyle = '#1f6feb';
      ctx.beginPath(); ctx.arc(xEth, yEth - 10, 8, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(xEth, yEth + 10, 8, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = '8px system-ui, sans-serif';
      ctx.fillText('C', xEth, yEth - 10);
      ctx.fillText('C', xEth, yEth + 10);

      // Growing Polymer Chain (Wavy tail)
      ctx.strokeStyle = '#7ee787';
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      ctx.moveTo(cx - 30, cy + 15);
      const chainPts = 6;
      for (let i = 1; i <= chainPts; i++) {
        const px = cx - 30 + i * 18;
        const py = cy + 15 + Math.sin(phase + i * 0.8) * 12;
        ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = '#7ee787';
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillText('-(CH₂CH₂)ₙ- Polymer Chain', cx + 60, cy + 45);

      ctx.textAlign = 'start'; ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = '#8b949e';
      ctx.font = '11px system-ui, sans-serif';
      ctx.fillText('Migratory 4-center insertion generates new vacant site cis to chain', 35, H - 35);

      // Right Panel: Schulz-Flory Molecular Weight Distribution Curve
      const rX = leftW + 10;
      const rW = W - rX - 20;
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.roundRect(rX, 20, rW, H - 40, 6);
      ctx.fill();
      ctx.stroke();

      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('Schulz-Flory Molecular Weight Distribution W(M)', rX + 15, 45);

      const dX = rX + 35;
      const dY = 70;
      const dW = rW - 55;
      const dH = H - 130;

      ctx.strokeStyle = '#30363d';
      ctx.strokeRect(dX, dY, dW, dH);

      // Plot W(M) vs log(M)
      ctx.strokeStyle = cat === 'meta' ? '#7ee787' : '#e3b341';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      const logM_min = 3; // 1,000 g/mol
      const logM_max = 7; // 10,000,000 g/mol
      const logMn = Math.log10(Mn);

      for (let i = 0; i <= dW; i++) {
        const curLogM = logM_min + (i / dW) * (logM_max - logM_min);
        const curM = Math.pow(10, curLogM);
        // Schulz-Flory distribution: W(M) = (M / Mn^2) * exp(-M / Mn) * M * ln(10)
        const xVal = curM / Mn;
        const W_val = xVal * xVal * Math.exp(-xVal);
        const normH = Math.min(1.0, W_val / 0.54);
        const py = dY + dH - 5 - normH * (dH - 25);

        if (i === 0) ctx.moveTo(dX + i, py);
        else ctx.lineTo(dX + i, py);
      }
      ctx.stroke();

      // Mn mark
      const mnX = dX + ((logMn - logM_min) / (logM_max - logM_min)) * dW;
      ctx.strokeStyle = '#58a6ff';
      ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(mnX, dY); ctx.lineTo(mnX, dY + dH); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#58a6ff';
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillText(`M_n: ${Math.round(Mn/1000)}k`, mnX - 20, dY + 20);

      // Axes labels
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillStyle = '#8b949e';
      ctx.fillText('10³', dX + 5, dY + dH + 15);
      ctx.fillText('10⁵', dX + dW * 0.5 - 10, dY + dH + 15);
      ctx.fillText('10⁷ g/mol', dX + dW - 35, dY + dH + 15);

      phase += 0.03;
      animId = requestAnimationFrame(render);
    }

    [catSel, pSlider, h2Slider, tSlider].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  return {
    sim_organo_electron_counting_18e,
    sim_organo_main_group_dimer_equilibria,
    sim_organo_carbonyl_backbonding_ir,
    sim_organo_beta_hydride_elimination,
    sim_organo_zeise_alkene_rotation,
    sim_organo_ferrocene_mo_dynamics,
    sim_organo_wade_mingos_cluster_psept,
    sim_organo_oxidative_addition_reductive_elim,
    sim_organo_wilkinson_hydrogenation_cycle,
    sim_organo_olefin_polymerization_kinetics
  };
})();

/* ==========================================================================
   Global Simulation Engine Registry Adapter
   ========================================================================== */
if (typeof window !== 'undefined') {
  window.SimulationEngine = window.SimulationEngine || {};
  Object.keys(window.OrganometallicChemistrySimulations).forEach(function(key) {
    window[key] = window.OrganometallicChemistrySimulations[key];
  });
  const originalInit = window.SimulationEngine.initSimulation;
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    const el = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    if (!el) return;
    if (window.OrganometallicChemistrySimulations && typeof window.OrganometallicChemistrySimulations[simType] === 'function') {
      return window.OrganometallicChemistrySimulations[simType](el);
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
