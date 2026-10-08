# generate_org2_sims.py
# Generates organic-chemistry-2-sims.js with 10 interactive 60 FPS Canvas simulations
# for Organic Chemistry II (Textbook #45)

def get_sims_code():
    return r"""// Organic Chemistry II Interactive Simulation Suite
// 60 FPS Real-time HTML5 Canvas Simulations for Master Textbook #45
// STRICT CONSTRAINT: ZERO PROHIBITED CODES PERMITTED

(function() {
  'use strict';

  window.Org2Sims = window.Org2Sims || {};

  // Utility helpers
  function setupCanvas(canvasId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return null;
    var ctx = canvas.getContext('2d');
    var dpr = window.devicePixelRatio || 1;
    var rect = canvas.getBoundingClientRect();
    var width = rect.width || 800;
    var height = rect.height || 420;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    ctx.scale(dpr, dpr);
    return { canvas: canvas, ctx: ctx, width: width, height: height };
  }

  function clearCanvas(ctx, width, height) {
    ctx.fillStyle = '#080d19';
    ctx.fillRect(0, 0, width, height);

    // Subtle technical grid
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.05)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (var x = 0; x < width; x += 40) {
      ctx.moveTo(x, 0); ctx.lineTo(x, height);
    }
    for (var y = 0; y < height; y += 40) {
      ctx.moveTo(0, y); ctx.lineTo(width, y);
    }
    ctx.stroke();
  }

  // =========================================================================
  // SIMULATION 1: Polyaromatic Clar Sextet & EAS Regiochemistry (Unit 1)
  // =========================================================================
  window.Org2Sims.sim_chem_polyaromatic_clar_sextet = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      molecule: 'phenanthrene', // 'naphthalene', 'anthracene', 'phenanthrene'
      electrophileSite: 'C9',   // active attack site
      time: 0,
      animating: true
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">PAH Framework:
          <select id="${controlsId}-mol" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="phenanthrene" selected>Phenanthrene (Clar 2 Sextets)</option>
            <option value="anthracene">Anthracene (Clar 1 Sextet)</option>
            <option value="naphthalene">Naphthalene (Clar 1 Sextet)</option>
          </select>
        </label>
        <button id="${controlsId}-attack" style="background:#0284c7; color:#fff; border:none; padding:5px 12px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:600;">Simulate E+ Attack</button>
      `;
      var sel = document.getElementById(`${controlsId}-mol`);
      if (sel) sel.onchange = function() { state.molecule = sel.value; };
      var btn = document.getElementById(`${controlsId}-attack`);
      if (btn) btn.onclick = function() { state.time = 0; };
    }

    function render() {
      state.time += 0.03;
      clearCanvas(ctx, width, height);

      ctx.save();
      ctx.translate(width * 0.45, height * 0.5);

      // Title HUD
      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 14px "Inter", sans-serif';
      ctx.textAlign = 'left';
      var molNames = {
        naphthalene: 'Naphthalene (2 Rings, RE = 252 kJ/mol)',
        anthracene: 'Anthracene (3 Linear Rings, RE = 350 kJ/mol)',
        phenanthrene: 'Phenanthrene (3 Angular Rings, RE = 380 kJ/mol)'
      };
      ctx.fillText(molNames[state.molecule], -width * 0.4, -height * 0.4);

      // Draw Rings
      var R = 50;
      if (state.molecule === 'naphthalene') {
        drawBenzeneRing(ctx, -R * 0.866, 0, R, true, 'Clar Sextet');
        drawBenzeneRing(ctx, R * 0.866, 0, R, false, 'Migrating');
      } else if (state.molecule === 'anthracene') {
        drawBenzeneRing(ctx, -R * 1.732, 0, R, true, 'Clar Sextet');
        drawBenzeneRing(ctx, 0, 0, R, false, 'Reactive C9/C10');
        drawBenzeneRing(ctx, R * 1.732, 0, R, false, 'Migrating');
      } else {
        // Phenanthrene (angular)
        drawBenzeneRing(ctx, -R * 1.3, R * 0.7, R, true, 'Clar Sextet A');
        drawBenzeneRing(ctx, 0, 0, R, false, 'Localized C9=C10');
        drawBenzeneRing(ctx, R * 1.3, R * 0.7, R, true, 'Clar Sextet B');
      }

      // Draw electrophilic attack particle
      var tMod = (Math.sin(state.time * 2) + 1) * 0.5;
      var pulse = 4 + Math.sin(state.time * 4) * 2;
      ctx.fillStyle = '#f43f5e';
      ctx.beginPath();
      ctx.arc(0, -R * 1.2 * (1 - tMod * 0.3), pulse, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#fda4af';
      ctx.font = '600 12px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('NO2+ (Electrophile)', 0, -R * 1.5);

      ctx.restore();

      // Right Info Panel
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(width - 240, 20, 220, 180);
      ctx.strokeRect(width - 240, 20, 220, 180);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 12px "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Clar Sextet Rule Metrics', width - 225, 45);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px "Inter", sans-serif';
      if (state.molecule === 'phenanthrene') {
        ctx.fillText('• Disjoint Sextets: 2 (High Stability)', width - 225, 70);
        ctx.fillText('• C9-C10 Bond Order: 0.775', width - 225, 90);
        ctx.fillText('• Reacts like localized alkene', width - 225, 110);
        ctx.fillText('• Preserves 2 intact sextets!', width - 225, 130);
        ctx.fillText('• Delta H(addition) favored', width - 225, 150);
      } else if (state.molecule === 'anthracene') {
        ctx.fillText('• Disjoint Sextets: 1', width - 225, 70);
        ctx.fillText('• Central C9/C10 Localization: High', width - 225, 90);
        ctx.fillText('• Facile Diels-Alder [4+2]', width - 225, 110);
        ctx.fillText('• Loss of aromaticity = only 30 kJ', width - 225, 130);
        ctx.fillText('• RE = 350 kJ/mol (Less stable)', width - 225, 150);
      } else {
        ctx.fillText('• Alpha-position attack preferred', width - 225, 70);
        ctx.fillText('• 4 Wheland benzenoid forms', width - 225, 90);
        ctx.fillText('• Beta-attack gives only 2 forms', width - 225, 110);
        ctx.fillText('• 80°C: 96% alpha (kinetic)', width - 225, 130);
        ctx.fillText('• 160°C: 85% beta (thermodynamic)', width - 225, 150);
      }

      requestAnimationFrame(render);
    }

    function drawBenzeneRing(ctx, cx, cy, r, hasClarCircle, label) {
      ctx.save();
      ctx.translate(cx, cy);

      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var i = 0; i < 6; i++) {
        var angle = (i * Math.PI) / 3;
        var x = r * Math.cos(angle);
        var y = r * Math.sin(angle);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.closePath();
      ctx.stroke();

      if (hasClarCircle) {
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.arc(0, 0, r * 0.55, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#fbbf24';
        ctx.font = '500 10px "Inter", sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('6π Sextet', 0, 3);
      }

      if (label) {
        ctx.fillStyle = '#94a3b8';
        ctx.font = '10px "Inter", sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(label, 0, r * 1.35);
      }

      ctx.restore();
    }

    render();
  };

  // =========================================================================
  // SIMULATION 2: Carbonyl Addition Bürgi-Dunitz 107° Trajectory (Unit 2)
  // =========================================================================
  window.Org2Sims.sim_chem_carbonyl_addition_burgi_dunitz = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      substrate: 'aldehyde', // 'aldehyde', 'ketone', 'ester'
      angle: 107,
      distance: 2.2, // Angstroms
      time: 0
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Carbonyl Substrate:
          <select id="${controlsId}-sub" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="aldehyde" selected>Acetaldehyde (Fast, Less Hindered)</option>
            <option value="ketone">Acetone (Moderate, Steric Crowding)</option>
            <option value="ester">Methyl Acetate (Resonance Deactivated)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:12px;">Attack Distance:
          <input type="range" id="${controlsId}-dist" min="1.4" max="3.5" step="0.1" value="2.2" style="margin-left:6px; vertical-align:middle;">
          <span id="${controlsId}-dist-val" style="color:#38bdf8; font-family:'Fira Code',monospace;">2.2 Å</span>
        </label>
      `;
      var sel = document.getElementById(`${controlsId}-sub`);
      if (sel) sel.onchange = function() { state.substrate = sel.value; };
      var slider = document.getElementById(`${controlsId}-dist`);
      var distVal = document.getElementById(`${controlsId}-dist-val`);
      if (slider && distVal) {
        slider.oninput = function() {
          state.distance = parseFloat(slider.value);
          distVal.innerText = state.distance.toFixed(1) + ' Å';
        };
      }
    }

    function render() {
      state.time += 0.02;
      clearCanvas(ctx, width, height);

      var cx = width * 0.42, cy = height * 0.55;

      ctx.save();
      ctx.translate(cx, cy);

      // Carbonyl Group C=O
      var C_pos = { x: 0, y: 0 };
      var O_pos = { x: 0, y: -110 };

      // Double bond C=O
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(-6, 0); ctx.lineTo(-6, -110);
      ctx.moveTo(6, 0); ctx.lineTo(6, -110);
      ctx.stroke();

      // Substituent 1 (left)
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(0, 0); ctx.lineTo(-90, 40);
      ctx.stroke();

      // Substituent 2 (right)
      ctx.beginPath();
      ctx.moveTo(0, 0); ctx.lineTo(90, 40);
      ctx.stroke();

      // Pi* Antibonding Orbital lobes on Carbon (transparent blue/red)
      var scaleD = Math.max(0.6, 2.5 - state.distance * 0.4);
      ctx.fillStyle = 'rgba(56, 189, 248, 0.25)';
      ctx.beginPath();
      ctx.ellipse(-35, -20, 40 * scaleD, 22 * scaleD, -Math.PI / 6, 0, Math.PI * 2);
      ctx.fill();

      // Oxygen atom
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(O_pos.x, O_pos.y, 22, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 15px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('O', O_pos.x, O_pos.y + 5);

      // Delta minus on Oxygen
      ctx.fillStyle = '#fca5a5';
      ctx.font = '12px "Inter", sans-serif';
      ctx.fillText('δ⁻', O_pos.x + 28, O_pos.y - 5);

      // Carbon atom
      ctx.fillStyle = '#334155';
      ctx.beginPath();
      ctx.arc(C_pos.x, C_pos.y, 24, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('C', C_pos.x, C_pos.y + 5);

      // Delta plus on Carbon
      ctx.fillStyle = '#7dd3fc';
      ctx.font = '12px "Inter", sans-serif';
      ctx.fillText('δ⁺', C_pos.x + 28, C_pos.y + 5);

      // Nucleophile approach trajectory along Bürgi-Dunitz Angle (107°)
      var rad = (state.angle * Math.PI) / 180;
      var distPx = state.distance * 65;
      var Nu_x = -distPx * Math.sin(rad - Math.PI / 2);
      var Nu_y = -distPx * Math.cos(rad - Math.PI / 2);

      // Trajectory dashed line
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2;
      ctx.setLineDash([5, 4]);
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.lineTo(Nu_x * 1.3, Nu_y * 1.3);
      ctx.stroke();
      ctx.setLineDash([]);

      // Bürgi-Dunitz Angle Arc
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(0, 0, 45, -Math.PI / 2, -(Math.PI / 2 + (Math.PI - rad)), true);
      ctx.stroke();

      ctx.fillStyle = '#f59e0b';
      ctx.font = '600 12px "Fira Code", monospace';
      ctx.fillText('107°', -42, -50);

      // Nucleophile sphere (Nu⁻)
      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.arc(Nu_x, Nu_y, 20, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 13px "Inter", sans-serif';
      ctx.fillText('Nu⁻', Nu_x, Nu_y + 4);

      ctx.restore();

      // Right Stats & Orbital Theory Panel
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.strokeStyle = '#334155';
      ctx.fillRect(width - 250, 20, 230, 210);
      ctx.strokeRect(width - 250, 20, 230, 210);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.fillText('Bürgi-Dunitz Stereoelectronics', width - 235, 45);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px "Inter", sans-serif';
      ctx.fillText('• Trajectory Angle: 107° ± 2°', width - 235, 70);
      ctx.fillText('• Maximizes Nu(HOMO) to π*(LUMO) overlap', width - 235, 90);
      ctx.fillText('• Minimizes Pauli clash with O lone pairs', width - 235, 110);
      var relRates = {
        aldehyde: 'Rate: 1.0 (Fastest, High Delta+)',
        ketone: 'Rate: 0.04 (Steric Hindrance)',
        ester: 'Rate: 0.0002 (Resonance Donor)'
      };
      ctx.fillText('• Substrate: ' + state.substrate.toUpperCase(), width - 235, 135);
      ctx.fillStyle = '#10b981';
      ctx.fillText(relRates[state.substrate], width - 235, 155);
      ctx.fillStyle = '#cbd5e1';
      ctx.fillText('• Distance: ' + state.distance.toFixed(1) + ' Å', width - 235, 180);
      var rehybrid = Math.max(0, (3.0 - state.distance) / 1.6 * 100);
      ctx.fillText('• Rehybridization to sp³: ' + rehybrid.toFixed(0) + '%', width - 235, 200);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // SIMULATION 3: Aldol Condensation Reaction Coordinate & Dehydration (Unit 2)
  // =========================================================================
  window.Org2Sims.sim_chem_aldol_condensation_equilibria = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      step: 0, // 0: Enolate generation, 1: Nucleophilic addition, 2: Protonation, 3: E1cB dehydration
      temp: 25 // Celsius
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Aldol Cascade Step:
          <select id="${controlsId}-step" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="0">Step 1: Enolate Formation (pKa ~ 20)</option>
            <option value="1">Step 2: C-C Bond Addition (Reversible)</option>
            <option value="2">Step 3: Beta-Hydroxy Carbonyl (Aldol)</option>
            <option value="3">Step 4: E1cB Dehydration (Irreversible)</option>
          </select>
        </label>
        <button id="${controlsId}-auto" style="background:#0284c7; color:#fff; border:none; padding:5px 12px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:600; margin-left:12px;">Auto Play</button>
      `;
      var sel = document.getElementById(`${controlsId}-step`);
      if (sel) sel.onchange = function() { state.step = parseInt(sel.value); };
      var autoBtn = document.getElementById(`${controlsId}-auto`);
      if (autoBtn) {
        autoBtn.onclick = function() {
          state.step = (state.step + 1) % 4;
          if (sel) sel.value = state.step;
        };
      }
    }

    function render() {
      clearCanvas(ctx, width, height);

      // Draw Energy Coordinate Curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.beginPath();
      var curvePoints = [
        { x: 60, y: 300 }, // Reactant
        { x: 140, y: 160 }, // TS1 (deprotonation)
        { x: 220, y: 240 }, // Enolate intermediate
        { x: 320, y: 120 }, // TS2 (addition)
        { x: 420, y: 220 }, // Alkoxide intermediate
        { x: 500, y: 210 }, // Beta-hydroxy aldehyde (Aldol)
        { x: 600, y: 140 }, // TS3 (E1cB dehydration)
        { x: 720, y: 340 }  // Alpha,beta-unsaturated enone (Thermodynamic Sink)
      ];

      ctx.moveTo(curvePoints[0].x, curvePoints[0].y);
      for (var i = 1; i < curvePoints.length; i++) {
        var xc = (curvePoints[i].x + curvePoints[i - 1].x) / 2;
        var yc = (curvePoints[i].y + curvePoints[i - 1].y) / 2;
        ctx.quadraticCurveTo(curvePoints[i - 1].x, curvePoints[i - 1].y, xc, yc);
      }
      ctx.lineTo(curvePoints[curvePoints.length - 1].x, curvePoints[curvePoints.length - 1].y);
      ctx.stroke();

      // Highlight current step point
      var stepIndices = [2, 4, 5, 7];
      var curPt = curvePoints[stepIndices[state.step]];
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(curPt.x, curPt.y, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Step Explanation HUD
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(50, 30, width - 100, 75);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 30, width - 100, 75);

      var explanations = [
        "Step 1: Hydroxide deprotonates alpha-carbon (pKa ~ 20). Enolate stabilized by C=C-O⁻ resonance.",
        "Step 2: Nucleophilic enolate carbon attacks neutral carbonyl via 107° Bürgi-Dunitz angle. Reversible equilibrium.",
        "Step 3: Alkoxide abstracts proton from water, forming neutral beta-hydroxy aldehyde (Aldol). Reversible at low T.",
        "Step 4: Conjugate base enolate eliminates OH⁻ via E1cB. Irreversible thermodynamic driving force: conjugated enone!"
      ];
      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(`Aldol Reaction Profile: Step ${state.step + 1} / 4`, 65, 52);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '12px "Inter", sans-serif';
      ctx.fillText(explanations[state.step], 65, 75);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // SIMULATION 4: Carboxylic Derivative Tetrahedral Matrix (Unit 4)
  // =========================================================================
  window.Org2Sims.sim_chem_carboxylic_derivative_tetrahedral_matrix = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      derivative: 'chloride', // 'chloride', 'anhydride', 'ester', 'amide'
      nucleophile: 'amine',   // 'water', 'alcohol', 'amine'
      time: 0
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Acyl Derivative:
          <select id="${controlsId}-deriv" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="chloride" selected>Acyl Chloride (Leaving Group: Cl⁻, pKa -7)</option>
            <option value="anhydride">Acid Anhydride (Leaving Group: RCOO⁻, pKa 4.8)</option>
            <option value="ester">Ester (Leaving Group: RO⁻, pKa 16)</option>
            <option value="amide">Amide (Leaving Group: NH2⁻, pKa 38)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:12px;">Nucleophile:
          <select id="${controlsId}-nu" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="amine" selected>Amine (RNH2, Strong Nucleophile)</option>
            <option value="alcohol">Alcohol (ROH, Moderate Nucleophile)</option>
            <option value="water">Water (H2O, Weak Nucleophile)</option>
          </select>
        </label>
      `;
      var selD = document.getElementById(`${controlsId}-deriv`);
      if (selD) selD.onchange = function() { state.derivative = selD.value; };
      var selN = document.getElementById(`${controlsId}-nu`);
      if (selN) selN.onchange = function() { state.nucleophile = selN.value; };
    }

    function render() {
      state.time += 0.025;
      clearCanvas(ctx, width, height);

      // Reactivity ladder bars
      var derivatives = [
        { name: 'Acyl Chloride', rate: 100000, pKa: -7, col: '#ef4444' },
        { name: 'Anhydride', rate: 1000, pKa: 4.8, col: '#f59e0b' },
        { name: 'Ester', rate: 1, pKa: 16, col: '#10b981' },
        { name: 'Amide', rate: 0.0001, pKa: 38, col: '#3b82f6' }
      ];

      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 14px "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Nucleophilic Acyl Substitution (B_AC2) Relative Rates', 40, 40);

      var startY = 80;
      for (var i = 0; i < derivatives.length; i++) {
        var d = derivatives[i];
        var isCurrent = d.name.toLowerCase().includes(state.derivative.substring(0, 4));
        var barW = Math.max(25, (Math.log10(d.rate) + 5) * 45);

        ctx.fillStyle = isCurrent ? '#f8fafc' : '#94a3b8';
        ctx.font = (isCurrent ? 'bold ' : '') + '12px "Inter", sans-serif';
        ctx.fillText(d.name, 40, startY + i * 45 + 16);

        ctx.fillStyle = isCurrent ? d.col : 'rgba(51, 65, 85, 0.7)';
        ctx.fillRect(160, startY + i * 45, barW, 24);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '11px "Fira Code", monospace';
        ctx.fillText(`pKa(LG) = ${d.pKa} | k_rel ~ 10^${Math.round(Math.log10(d.rate))}`, 170 + barW + 10, startY + i * 45 + 16);
      }

      // Tetrahedral Intermediate Graphic
      var tX = width * 0.72, tY = height * 0.65;
      ctx.save();
      ctx.translate(tX, tY);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Tetrahedral Intermediate (sp³)', 0, -85);

      // Central Carbon
      ctx.fillStyle = '#1e293b';
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(0, 0, 22, 0, Math.PI * 2);
      ctx.fill(); ctx.stroke();
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 14px "Inter", sans-serif';
      ctx.fillText('C', 0, 5);

      // Bonds to 4 groups
      drawBond(ctx, 0, 0, 0, -55, 'O⁻', '#ef4444');
      drawBond(ctx, 0, 0, -55, 30, 'R', '#94a3b8');
      drawBond(ctx, 0, 0, 55, 30, 'LG (Leaving Group)', '#f59e0b');
      drawBond(ctx, 0, 0, 0, 60, `Nu (${state.nucleophile})`, '#10b981');

      ctx.restore();

      requestAnimationFrame(render);
    }

    function drawBond(ctx, x1, y1, x2, y2, label, col) {
      ctx.strokeStyle = col;
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(x1, y1); ctx.lineTo(x2, y2);
      ctx.stroke();

      ctx.fillStyle = col;
      ctx.beginPath();
      ctx.arc(x2, y2, 14, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 10px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(label.split(' ')[0], x2, y2 + 3);
    }

    render();
  };

  // =========================================================================
  // SIMULATION 5: Amine Pyramidal Inversion & Hofmann Elimination (Unit 5)
  // =========================================================================
  window.Org2Sims.sim_chem_amine_inversion_hofmann_elimination = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      mode: 'inversion', // 'inversion', 'hofmann'
      angle: 0,
      time: 0
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <button id="${controlsId}-m1" style="background:#0284c7; color:#fff; border:none; padding:5px 12px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:600;">Pyramidal Inversion (Umbrella Flip)</button>
        <button id="${controlsId}-m2" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:5px 12px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:600; margin-left:8px;">Hofmann Anti-Coplanar Elimination</button>
      `;
      var b1 = document.getElementById(`${controlsId}-m1`);
      var b2 = document.getElementById(`${controlsId}-m2`);
      if (b1 && b2) {
        b1.onclick = function() {
          state.mode = 'inversion';
          b1.style.background = '#0284c7'; b1.style.color = '#fff';
          b2.style.background = '#1e293b'; b2.style.color = '#38bdf8';
        };
        b2.onclick = function() {
          state.mode = 'hofmann';
          b2.style.background = '#0284c7'; b2.style.color = '#fff';
          b1.style.background = '#1e293b'; b1.style.color = '#38bdf8';
        };
      }
    }

    function render() {
      state.time += 0.03;
      clearCanvas(ctx, width, height);

      if (state.mode === 'inversion') {
        // Umbrella inversion animation
        var invFlip = Math.sin(state.time * 2.5); // oscillates -1 to +1
        var cx = width * 0.45, cy = height * 0.5;

        ctx.save();
        ctx.translate(cx, cy);

        // Nitrogen atom
        ctx.fillStyle = '#3b82f6';
        ctx.beginPath();
        ctx.arc(0, 0, 26, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 16px "Inter", sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('N', 0, 5);

        // Lone pair lobe
        var lpY = -55 * invFlip;
        ctx.fillStyle = 'rgba(56, 189, 248, 0.4)';
        ctx.beginPath();
        ctx.ellipse(0, lpY, 20, 35, 0, 0, Math.PI * 2);
        ctx.fill();

        // Three substituent bonds
        var R_y = 55 * invFlip;
        drawSubstituent(ctx, -60, R_y, 'R1');
        drawSubstituent(ctx, 0, R_y * 1.2, 'R2');
        drawSubstituent(ctx, 60, R_y, 'R3');

        ctx.restore();

        // Right Energy Double-Well HUD
        ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
        ctx.fillRect(width - 250, 20, 230, 190);
        ctx.strokeStyle = '#334155';
        ctx.strokeRect(width - 250, 20, 230, 190);

        ctx.fillStyle = '#38bdf8';
        ctx.font = '600 13px "Inter", sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText('Nitrogen Inversion Dynamics', width - 235, 45);
        ctx.fillStyle = '#cbd5e1';
        ctx.font = '11px "Inter", sans-serif';
        ctx.fillText('• Barrier: Delta G‡ ~ 25 kJ/mol', width - 235, 70);
        ctx.fillText('• Frequency: k ~ 2 x 10^10 s⁻¹', width - 235, 90);
        ctx.fillText('• Cannot resolve chiral amine', width - 235, 110);
        ctx.fillText('  enantiomers at 25°C!', width - 235, 130);
        ctx.fillText('• Planar sp² transition state', width - 235, 155);
        ctx.fillText('• Quaternary ammonium: LOCKED', width - 235, 175);
      } else {
        // Hofmann Elimination Demonstration
        ctx.fillStyle = '#38bdf8';
        ctx.font = '600 14px "Inter", sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText('Hofmann Elimination: Steric Bulk Forces Least-Substituted Alkene', 40, 40);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '12px "Inter", sans-serif';
        ctx.fillText('Bulky Leaving Group -N⁺Me3 enforces anti-coplanar attack at less hindered primary beta-hydrogen:', 40, 65);

        // Draw Substrate Newman/Anti Projection
        var hX = width * 0.45, hY = height * 0.55;
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(hX - 90, hY); ctx.lineTo(hX + 90, hY);
        ctx.stroke();

        ctx.fillStyle = '#10b981';
        ctx.fillText('H (Least Hindered)', hX - 90, hY - 60);
        ctx.strokeStyle = '#10b981';
        ctx.beginPath();
        ctx.moveTo(hX - 90, hY); ctx.lineTo(hX - 90, hY - 45);
        ctx.stroke();

        ctx.fillStyle = '#ef4444';
        ctx.fillText('-N⁺Me3 (Bulky Leaving Group)', hX + 90, hY + 60);
        ctx.strokeStyle = '#ef4444';
        ctx.beginPath();
        ctx.moveTo(hX + 90, hY); ctx.lineTo(hX + 90, hY + 45);
        ctx.stroke();

        ctx.fillStyle = '#f59e0b';
        ctx.font = 'bold 14px "Inter", sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Hofmann Alkene Product: 1-Butene (95%) vs 2-Butene (5%)', width * 0.5, height - 40);
      }

      requestAnimationFrame(render);
    }

    function drawSubstituent(ctx, x, y, name) {
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(0, 0); ctx.lineTo(x, y);
      ctx.stroke();

      ctx.fillStyle = '#1e293b';
      ctx.beginPath();
      ctx.arc(x, y, 14, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#38bdf8';
      ctx.font = '11px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(name, x, y + 4);
    }

    render();
  };

  // =========================================================================
  // SIMULATION 6: Diazonium Coupling & Azo Dye Color Engine (Unit 5)
  // =========================================================================
  window.Org2Sims.sim_chem_diazonium_coupling_color_engine = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      couplingPartner: 'beta_naphthol', // 'beta_naphthol', 'aniline', 'phenol'
      pH: 9.5
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Coupling Partner:
          <select id="${controlsId}-partner" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="beta_naphthol" selected>2-Naphthol (Sudan I Red Dye)</option>
            <option value="aniline">N,N-Dimethylaniline (Methyl Orange)</option>
            <option value="phenol">Phenol (p-Hydroxyazobenzene Yellow)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:12px;">Medium pH:
          <input type="range" id="${controlsId}-ph" min="3" max="12" step="0.5" value="9.5" style="margin-left:6px; vertical-align:middle;">
          <span id="${controlsId}-ph-val" style="color:#38bdf8; font-family:'Fira Code',monospace;">pH 9.5</span>
        </label>
      `;
      var selP = document.getElementById(`${controlsId}-partner`);
      if (selP) selP.onchange = function() { state.couplingPartner = selP.value; };
      var slider = document.getElementById(`${controlsId}-ph`);
      var phVal = document.getElementById(`${controlsId}-ph-val`);
      if (slider && phVal) {
        slider.oninput = function() {
          state.pH = parseFloat(slider.value);
          phVal.innerText = 'pH ' + state.pH.toFixed(1);
        };
      }
    }

    function render() {
      clearCanvas(ctx, width, height);

      var dyes = {
        beta_naphthol: { name: 'Sudan I (1-Phenylazo-2-naphthol)', color: '#dc2626', lambda: 485, rgb: 'rgb(220, 38, 38)' },
        aniline: { name: 'Methyl Orange (4-Dimethylaminoazobenzene)', color: '#ea580c', lambda: 508, rgb: 'rgb(234, 88, 12)' },
        phenol: { name: 'p-Hydroxyazobenzene', color: '#eab308', lambda: 430, rgb: 'rgb(234, 179, 8)' }
      };

      var curDye = dyes[state.couplingPartner];

      // Draw Color Cuvette / Flask
      var cX = 140, cY = height * 0.55;
      ctx.fillStyle = curDye.color;
      ctx.fillRect(cX - 50, cY - 80, 100, 150);

      // Glass highlight
      ctx.fillStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.fillRect(cX - 45, cY - 75, 15, 140);

      ctx.strokeStyle = '#cbd5e1';
      ctx.lineWidth = 3;
      ctx.strokeRect(cX - 50, cY - 80, 100, 150);

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 13px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Azo Dye Solution', cX, cY + 90);

      // Structure Formula Display
      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 15px "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(curDye.name, 240, 50);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '12px "Inter", sans-serif';
      ctx.fillText('Mechanism: Electrophilic Aromatic Attack of Arenediazonium Cation (Ar-N≡N⁺)', 240, 75);

      // Spectral UV-Vis Graph
      var gX = 260, gY = 120, gW = width - 300, gH = 180;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(gX, gY, gW, gH);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(gX, gY, gW, gH);

      // Axis labels
      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px "Inter", sans-serif';
      ctx.fillText('350 nm (UV)', gX + 10, gY + gH - 8);
      ctx.fillText('700 nm (Near IR)', gX + gW - 80, gY + gH - 8);
      ctx.fillText('Absorption Abs', gX + 10, gY + 18);

      // Draw Gaussian UV-Vis Absorption Peak
      ctx.strokeStyle = curDye.color;
      ctx.lineWidth = 3;
      ctx.beginPath();
      var peakNorm = (curDye.lambda - 350) / 350;
      var peakX = gX + peakNorm * gW;
      for (var px = gX + 5; px < gX + gW - 5; px += 2) {
        var dx = px - peakX;
        var absY = Math.exp(-(dx * dx) / 1200);
        var py = gY + gH - 25 - absY * (gH - 50);
        if (px === gX + 5) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Peak label
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px "Fira Code", monospace';
      ctx.textAlign = 'center';
      ctx.fillText(`λ_max = ${curDye.lambda} nm`, peakX, gY + 35);

      // pH coupling kinetics notice
      ctx.fillStyle = '#fbbf24';
      ctx.font = '11px "Inter", sans-serif';
      ctx.textAlign = 'left';
      if (state.pH < 5) {
        ctx.fillText('⚠️ Low pH: Phenoxide/amine un-ionized or protonated. Coupling is sluggish.', 260, height - 30);
      } else if (state.pH > 10.5) {
        ctx.fillText('⚠️ High pH: Diazonium converted to unreactive diazotate [Ar-N=N-O]⁻. Coupling halted!', 260, height - 30);
      } else {
        ctx.fillStyle = '#10b981';
        ctx.fillText('✓ Optimal pH Window (8-10): Fast electrophilic coupling to vibrant azo dye!', 260, height - 30);
      }

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // SIMULATION 7: 3D Polarimeter & Optical Activity (Unit 6)
  // =========================================================================
  window.Org2Sims.sim_chem_optical_activity_polarimeter_3d = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      enantiomer: 'dex', // 'dex' (+), 'laevo' (-), 'racemic' (0)
      conc: 1.0,         // g/mL
      pathLength: 1.0,   // dm
      specificRot: 52.7  // D-glucose degrees
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Sample Type:
          <select id="${controlsId}-enant" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="dex" selected>D-Glucose (+52.7° Dextrorotatory)</option>
            <option value="laevo">L-Glucose (-52.7° Laevorotatory)</option>
            <option value="racemic">Racemic Mixture (0.0° Optically Inactive)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:12px;">Concentration:
          <input type="range" id="${controlsId}-c" min="0.2" max="2.0" step="0.1" value="1.0" style="margin-left:6px; vertical-align:middle;">
          <span id="${controlsId}-c-val" style="color:#38bdf8; font-family:'Fira Code',monospace;">1.0 g/mL</span>
        </label>
      `;
      var selE = document.getElementById(`${controlsId}-enant`);
      if (selE) selE.onchange = function() { state.enantiomer = selE.value; };
      var slider = document.getElementById(`${controlsId}-c`);
      var cVal = document.getElementById(`${controlsId}-c-val`);
      if (slider && cVal) {
        slider.oninput = function() {
          state.conc = parseFloat(slider.value);
          cVal.innerText = state.conc.toFixed(1) + ' g/mL';
        };
      }
    }

    function render() {
      clearCanvas(ctx, width, height);

      // Calculate Biot's Law Observed Rotation: alpha = [alpha] * c * l
      var sign = state.enantiomer === 'dex' ? 1 : (state.enantiomer === 'laevo' ? -1 : 0);
      var obsRot = sign * state.specificRot * state.conc * state.pathLength;

      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 14px "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText("Biot's Polarimetric Optical Rotation Engine", 40, 35);

      // Polarimeter Optical Bench Diagram
      var bY = height * 0.45;
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(50, bY); ctx.lineTo(width - 50, bY);
      ctx.stroke();

      // 1. Monochromatic Light Source (Sodium D-line 589.3 nm)
      ctx.fillStyle = '#facc15';
      ctx.beginPath();
      ctx.arc(80, bY, 18, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = '10px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Na-D', 80, bY + 32);

      // 2. Polarizer (Nicol Prism)
      ctx.fillStyle = '#3b82f6';
      ctx.fillRect(170, bY - 45, 16, 90);
      ctx.fillText('Polarizer', 178, bY + 62);

      // 3. Sample Tube
      ctx.fillStyle = 'rgba(56, 189, 248, 0.2)';
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.fillRect(250, bY - 35, 180, 70);
      ctx.strokeRect(250, bY - 35, 180, 70);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('Sample Cell (l = 1.0 dm)', 340, bY + 52);

      // 4. Analyzer Disc
      var aX = 520;
      ctx.fillStyle = '#8b5cf6';
      ctx.fillRect(aX - 8, bY - 45, 16, 90);
      ctx.fillText('Analyzer', aX, bY + 62);

      // 5. Eyepiece / Detector
      var eX = 640;
      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.arc(eX, bY, 40, 0, Math.PI * 2);
      ctx.fill();

      // Draw Laurent Half-Shade Eyepiece View
      ctx.save();
      ctx.translate(eX, bY);
      ctx.rotate((obsRot * Math.PI) / 180);
      ctx.strokeStyle = '#080d19';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(0, -38); ctx.lineTo(0, 38);
      ctx.stroke();
      ctx.restore();

      ctx.fillStyle = '#ffffff';
      ctx.font = '10px "Inter", sans-serif';
      ctx.fillText('Half-Shade Field', eX, bY + 55);

      // Bottom Formulas HUD
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(50, height - 100, width - 100, 75);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, height - 100, width - 100, 75);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 13px "Fira Code", monospace';
      ctx.textAlign = 'left';
      ctx.fillText(`α_obs = [α]_D^T × c × l = ${obsRot >= 0 ? '+' : ''}${obsRot.toFixed(2)}°`, 70, height - 75);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '12px "Inter", sans-serif';
      var modeText = state.enantiomer === 'dex' ? 'Dextrorotatory (+): Rotates plane of polarization clockwise.' : (state.enantiomer === 'laevo' ? 'Laevorotatory (-): Rotates plane of polarization counter-clockwise.' : 'Racemic Mixture: External compensation between enantiomers yields exactly 0.00° net rotation.');
      ctx.fillText(modeText, 70, height - 48);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // SIMULATION 8: Michael Addition & Robinson Annulation Cascade (Unit 7)
  // =========================================================================
  window.Org2Sims.sim_chem_michael_robinson_annulation_cascade = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      step: 0 // 0: Michael Enolate 1,4-addition, 1: Intramolecular aldol condensation, 2: Final bicyclic enone
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Cascade Stage:
          <select id="${controlsId}-stage" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="0" selected>Stage 1: Michael 1,4-Conjugate Addition</option>
            <option value="1">Stage 2: Intramolecular Aldol Cyclization</option>
            <option value="2">Stage 3: Dehydration to Fused Bicyclic Enone</option>
          </select>
        </label>
        <button id="${controlsId}-next" style="background:#0284c7; color:#fff; border:none; padding:5px 12px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:600; margin-left:12px;">Next Step →</button>
      `;
      var selS = document.getElementById(`${controlsId}-stage`);
      if (selS) selS.onchange = function() { state.step = parseInt(selS.value); };
      var nextB = document.getElementById(`${controlsId}-next`);
      if (nextB) {
        nextB.onclick = function() {
          state.step = (state.step + 1) % 3;
          if (selS) selS.value = state.step;
        };
      }
    }

    function render() {
      clearCanvas(ctx, width, height);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 14px "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Robinson Annulation: Michael Addition + Intramolecular Aldol', 40, 35);

      var steps = [
        {
          title: "Stage 1: Michael Conjugate 1,4-Addition",
          desc: "Cyclohexanone enolate (donor) attacks methyl vinyl ketone beta-carbon (acceptor) via soft-soft interaction.",
          leftMol: "Cyclohexanone Enolate",
          rightMol: "Methyl Vinyl Ketone",
          result: "1,5-Dicarbonyl Intermediate"
        },
        {
          title: "Stage 2: Intramolecular Aldol Cyclization",
          desc: "Deprotonation of terminal methyl forms internal enolate, which attacks ring carbonyl via favorable 6-enolexo-trig.",
          leftMol: "1,5-Dicarbonyl Adduct",
          rightMol: "Intramolecular Enolate",
          result: "Bicyclic Beta-Hydroxy Ketone"
        },
        {
          title: "Stage 3: E1cB Dehydration to Fused Bicyclic Enone",
          desc: "Irreversible base-catalyzed loss of water delivers the stable conjugated Wieland-Miescher ketone core!",
          leftMol: "Bicyclic Beta-Hydroxy Ketone",
          rightMol: "Base (KOH / MeOH)",
          result: "Delta-4-Octalone / Steroid Precursor"
        }
      ];

      var cur = steps[state.step];

      // Draw Cascade Flowchart Blocks
      var bY = height * 0.42;
      drawFlowBlock(ctx, 80, bY, 180, 70, cur.leftMol, '#3b82f6');
      drawFlowBlock(ctx, 310, bY, 180, 70, cur.rightMol, '#10b981');
      drawFlowBlock(ctx, 550, bY, 200, 70, cur.result, '#f59e0b');

      // Connecting Arrows
      drawArrow(ctx, 265, bY + 35, 305, bY + 35);
      drawArrow(ctx, 495, bY + 35, 545, bY + 35);

      // Bottom Explanation Box
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(40, height - 110, width - 80, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(40, height - 110, width - 80, 85);

      ctx.fillStyle = '#f59e0b';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.fillText(cur.title, 60, height - 85);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '12px "Inter", sans-serif';
      ctx.fillText(cur.desc, 60, height - 60);

      requestAnimationFrame(render);
    }

    function drawFlowBlock(ctx, x, y, w, h, text, col) {
      ctx.fillStyle = 'rgba(30, 41, 59, 0.8)';
      ctx.strokeStyle = col;
      ctx.lineWidth = 2;
      ctx.fillRect(x, y, w, h);
      ctx.strokeRect(x, y, w, h);

      ctx.fillStyle = col;
      ctx.font = '600 12px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(text, x + w / 2, y + h / 2 + 4);
    }

    function drawArrow(ctx, x1, y1, x2, y2) {
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(x1, y1); ctx.lineTo(x2, y2);
      ctx.stroke();
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.moveTo(x2, y2);
      ctx.lineTo(x2 - 8, y2 - 5);
      ctx.lineTo(x2 - 8, y2 + 5);
      ctx.closePath();
      ctx.fill();
    }

    render();
  };

  // =========================================================================
  // SIMULATION 9: Medicinal Target Binding & Aspirin/Sulfa Docking (Unit 8)
  // =========================================================================
  window.Org2Sims.sim_chem_drug_docking_target_binding = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      drug: 'aspirin', // 'aspirin', 'sulfanilamide'
      bound: false,
      time: 0
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Pharmaceutical Target:
          <select id="${controlsId}-drug" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="aspirin" selected>Aspirin (COX-1/2 Active Site Ser-530)</option>
            <option value="sulfanilamide">Sulfanilamide (DHPS PABA Competitor)</option>
          </select>
        </label>
        <button id="${controlsId}-dock" style="background:#0284c7; color:#fff; border:none; padding:5px 12px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:600; margin-left:12px;">Toggle Docking</button>
      `;
      var selD = document.getElementById(`${controlsId}-drug`);
      if (selD) selD.onchange = function() { state.drug = selD.value; state.bound = false; };
      var btnD = document.getElementById(`${controlsId}-dock`);
      if (btnD) btnD.onclick = function() { state.bound = !state.bound; };
    }

    function render() {
      state.time += 0.025;
      clearCanvas(ctx, width, height);

      var pX = width * 0.45, pY = height * 0.55;

      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 14px "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(state.drug === 'aspirin' ? 'Aspirin: Irreversible Acetylation of Cyclooxygenase (Ser-530)' : 'Sulfanilamide: Antimetabolite Competitive Inhibition of DHPS', 40, 35);

      // Draw Enzyme Pocket (Channel)
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(pX - 180, pY - 100);
      ctx.lineTo(pX - 60, pY - 30);
      ctx.lineTo(pX - 60, pY + 70);
      ctx.lineTo(pX + 60, pY + 70);
      ctx.lineTo(pX + 60, pY - 30);
      ctx.lineTo(pX + 180, pY - 100);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(state.drug === 'aspirin' ? 'COX Hydrophobic Channel' : 'DHPS Catalytic Pocket', pX, pY + 95);

      // Key Catalytic Residue
      var resY = pY + 45;
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(pX - 45, resY, 10, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#fca5a5';
      ctx.font = '10px "Inter", sans-serif';
      ctx.fillText(state.drug === 'aspirin' ? 'Ser-530 -OH' : 'Arg-255 Guanidinium', pX - 45, resY - 15);

      // Drug molecule position
      var drugY = state.bound ? pY + 20 : pY - 90 + Math.sin(state.time * 2) * 8;

      ctx.save();
      ctx.translate(pX, drugY);

      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.arc(0, 0, 24, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px "Inter", sans-serif';
      ctx.fillText(state.drug === 'aspirin' ? 'Aspirin' : 'Sulfa', 0, 4);

      if (state.bound) {
        // Covalent bond / H-bond dashes
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.moveTo(0, 0); ctx.lineTo(-45, 25);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#f59e0b';
        ctx.font = '600 11px "Inter", sans-serif';
        ctx.fillText(state.drug === 'aspirin' ? 'Covalent Acetyl Transfer!' : 'PABA Competitive H-Bond', 0, -35);
      }

      ctx.restore();

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // SIMULATION 10: Fused Heterocycles: Fischer Indole & Skraup (Unit 9)
  // =========================================================================
  window.Org2Sims.sim_chem_fused_heterocycle_fischer_skraup = function(canvasId, controlsId) {
    var target = setupCanvas(canvasId);
    if (!target) return;
    var ctx = target.ctx, width = target.width, height = target.height;

    var state = {
      reaction: 'fischer', // 'fischer', 'skraup'
      step: 0
    };

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Fused Ring Cascade:
          <select id="${controlsId}-rxn" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:6px;">
            <option value="fischer" selected>Fischer Indole ([3,3]-Sigmatropic Cascade)</option>
            <option value="skraup">Skraup Quinoline Synthesis (Glycerol + Aniline)</option>
          </select>
        </label>
      `;
      var selR = document.getElementById(`${controlsId}-rxn`);
      if (selR) selR.onchange = function() { state.reaction = selR.value; };
    }

    function render() {
      clearCanvas(ctx, width, height);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '600 14px "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(state.reaction === 'fischer' ? 'Fischer Indole Synthesis: [3,3]-Sigmatropic Driving Force' : 'Skraup Quinoline Synthesis: Dehydration, Michael, EAS & Oxidation', 40, 35);

      var steps = state.reaction === 'fischer' ? [
        "1. Hydrazone Ene-hydrazine tautomerism under acid catalysis.",
        "2. Rate-determining [3,3]-sigmatropic shift: cleaves weak N-N (160 kJ/mol) to form strong C-C bond (350 kJ/mol)!",
        "3. Rearomatization, intramolecular nucleophilic cyclization to indoline.",
        "4. Acid-catalyzed expulsion of NH3 gas yields aromatic Indole core!"
      ] : [
        "1. Dehydration of glycerol by concentrated H2SO4 generates acrolein (CH2=CH-CHO).",
        "2. Michael addition of aniline amino group to acrolein conjugate double bond.",
        "3. Acid-catalyzed intramolecular EAS cyclization onto benzene ring ortho position.",
        "4. Oxidation (nitrobenzene / FeSO4) aromatizes dihydroxyquinoline to fully aromatic Quinoline!"
      ];

      var startY = 80;
      for (var i = 0; i < steps.length; i++) {
        ctx.fillStyle = 'rgba(30, 41, 59, 0.7)';
        ctx.fillRect(40, startY + i * 55, width - 80, 42);
        ctx.strokeStyle = '#334155';
        ctx.strokeRect(40, startY + i * 55, width - 80, 42);

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 12px "Fira Code", monospace';
        ctx.fillText(`Step ${i + 1}`, 55, startY + i * 55 + 26);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '12px "Inter", sans-serif';
        ctx.fillText(steps[i], 120, startY + i * 55 + 26);
      }

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // window.SimulationEngine Mount Adapter
  // =========================================================================
  var SIM_TITLES = {
    sim_chem_polyaromatic_clar_sextet: "Polyaromatic Clar Sextets & Regiochemistry Engine",
    sim_chem_carbonyl_addition_burgi_dunitz: "Carbonyl Bürgi-Dunitz 107° Trajectory Simulator",
    sim_chem_aldol_condensation_equilibria: "Aldol Condensation & Dehydration Coordinate",
    sim_chem_carboxylic_derivative_tetrahedral_matrix: "Nucleophilic Acyl Substitution Tetrahedral Matrix",
    sim_chem_amine_inversion_hofmann_elimination: "Amine Pyramidal Inversion & Hofmann Elimination",
    sim_chem_diazonium_coupling_color_engine: "Diazonium Azo Coupling & UV-Vis Color Synthesizer",
    sim_chem_optical_activity_polarimeter_3d: "3D Laurent Polarimeter & Biot's Law Engine",
    sim_chem_michael_robinson_annulation_cascade: "Michael Addition & Robinson Annulation Simulator",
    sim_chem_drug_docking_target_binding: "Pharmaceutical Target Docking & Inhibition Engine",
    sim_chem_fused_heterocycle_fischer_skraup: "Fused Heterocycle Fischer & Skraup Cascade Simulator"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.Org2Sims || typeof window.Org2Sims[simType] !== 'function') {
      console.warn('Simulation type not found in Org2Sims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Organic Chemistry II Interactive Simulation";
    var canvasId = containerId + '-canvas';
    var controlsId = containerId + '-controls';

    container.innerHTML = `
      <div class="simulation-card" style="margin: 1.5rem 0;">
        <div class="sim-header">
          <div class="sim-title">${title}</div>
          <div class="sim-badge">60 FPS Real-Time Canvas Engine</div>
        </div>
        <div class="canvas-wrapper" style="position: relative; width: 100%; height: 420px; background: #080d19; border-radius: 8px; overflow: hidden;">
          <canvas id="${canvasId}" width="800" height="420" class="sim-canvas" style="width: 100%; height: 100%; display: block;"></canvas>
        </div>
        <div class="sim-controls" id="${controlsId}" style="padding: 0.75rem 1rem; background: #0b1120; border-top: 1px solid #1e293b; display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center;"></div>
      </div>
    `;

    setTimeout(function() {
      window.Org2Sims[simType](canvasId, controlsId);
    }, 50);
  };

})();
"""

if __name__ == "__main__":
    code = get_sims_code()
    with open("organic-chemistry-2-sims.js", "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Generated organic-chemistry-2-sims.js ({len(code)} characters)")
