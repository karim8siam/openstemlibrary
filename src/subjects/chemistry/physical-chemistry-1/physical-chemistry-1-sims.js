// Physical Chemistry I Interactive Simulation Engines (60 FPS Canvas)
// Strictly ZERO course numbers or codes.
(function() {
  'use strict';

  function setupCanvas(canvas) {
    var dpr = window.devicePixelRatio || 1;
    var rect = canvas.getBoundingClientRect();
    var width = rect.width || 800;
    var height = rect.height || 420;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    var ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);
    return { ctx: ctx, width: width, height: height };
  }

  window.PChem1Sims = {};

  // =========================================================================
  // 1. sim_chem_dimensional_matter_converter
  // =========================================================================
  window.PChem1Sims.sim_chem_dimensional_matter_converter = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      phase: 'gas', // 'solid', 'liquid', 'gas', 'supercritical'
      tempK: 300,
      pressBar: 1.0,
      particles: []
    };

    // Initialize particles
    var numP = 70;
    for (var i = 0; i < numP; i++) {
      state.particles.push({
        x: 50 + Math.random() * 320,
        y: 60 + Math.random() * 300,
        vx: (Math.random() - 0.5) * 2,
        vy: (Math.random() - 0.5) * 2,
        r: 5
      });
    }

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Phase State:
          <select id="${controlsId}-phase" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:0.25rem 0.5rem; margin-left:0.35rem;">
            <option value="solid">Solid (Lattice Order)</option>
            <option value="liquid">Liquid (Condensed Flow)</option>
            <option value="gas" selected>Gas (Kinetic Chaos)</option>
            <option value="supercritical">Supercritical Fluid</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.5rem;">Temperature (K):
          <input type="range" id="${controlsId}-temp" min="50" max="900" step="10" value="300" style="vertical-align:middle; width:100px;">
          <span id="${controlsId}-temp-val" style="color:#38bdf8; font-family:monospace;">300 K</span>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.5rem;">Pressure (bar):
          <input type="range" id="${controlsId}-press" min="0.1" max="150" step="0.5" value="1.0" style="vertical-align:middle; width:90px;">
          <span id="${controlsId}-press-val" style="color:#38bdf8; font-family:monospace;">1.0 bar</span>
        </label>
      `;

      var pSel = document.getElementById(`${controlsId}-phase`);
      var tSl = document.getElementById(`${controlsId}-temp`);
      var prSl = document.getElementById(`${controlsId}-press`);

      if (pSel) pSel.addEventListener('change', function(e) {
        state.phase = e.target.value;
        if (state.phase === 'solid') { state.tempK = 100; state.pressBar = 1.0; }
        else if (state.phase === 'liquid') { state.tempK = 295; state.pressBar = 1.0; }
        else if (state.phase === 'gas') { state.tempK = 450; state.pressBar = 1.0; }
        else if (state.phase === 'supercritical') { state.tempK = 750; state.pressBar = 110.0; }
        if (tSl) tSl.value = state.tempK;
        if (prSl) prSl.value = state.pressBar;
        document.getElementById(`${controlsId}-temp-val`).innerText = state.tempK + ' K';
        document.getElementById(`${controlsId}-press-val`).innerText = state.pressBar.toFixed(1) + ' bar';
      });

      if (tSl) tSl.addEventListener('input', function(e) {
        state.tempK = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-temp-val`).innerText = state.tempK + ' K';
      });

      if (prSl) prSl.addEventListener('input', function(e) {
        state.pressBar = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-press-val`).innerText = state.pressBar.toFixed(1) + ' bar';
      });
    }

    var animId;
    function render() {
      var w = setup.width;
      var h = setup.height;
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      // Simulation box (Left)
      var boxW = w * 0.52;
      var boxH = h - 50;
      var boxX = 20;
      var boxY = 25;

      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 2;
      ctx.strokeRect(boxX, boxY, boxW, boxH);

      // Label box
      ctx.fillStyle = '#64748b';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('MICROSCOPIC MOLECULAR CHAMBER (2D Enclosed Domain)', boxX + 10, boxY + 18);

      // Physics update based on phase & temp
      var speedScale = Math.sqrt(state.tempK / 300);
      var boxBottom = boxY + boxH;

      for (var i = 0; i < state.particles.length; i++) {
        var p = state.particles[i];

        if (state.phase === 'solid') {
          // Vibrating lattice
          var row = Math.floor(i / 10);
          var col = i % 10;
          var baseGridX = boxX + 50 + col * (boxW - 100) / 9;
          var baseGridY = boxBottom - 40 - row * 28;
          var vibAmp = 1.2 * (state.tempK / 300);
          p.x = baseGridX + (Math.sin(Date.now() * 0.02 + i) * vibAmp);
          p.y = baseGridY + (Math.cos(Date.now() * 0.02 + i * 2) * vibAmp);
        } else if (state.phase === 'liquid') {
          // Closely packed sliding particles confined to lower half
          var liquidTop = boxY + boxH * 0.45;
          p.x += p.vx * speedScale * 0.8;
          p.y += p.vy * speedScale * 0.8;
          if (p.x < boxX + p.r) { p.x = boxX + p.r; p.vx *= -1; }
          if (p.x > boxX + boxW - p.r) { p.x = boxX + boxW - p.r; p.vx *= -1; }
          if (p.y < liquidTop) { p.y = liquidTop; p.vy = Math.abs(p.vy); }
          if (p.y > boxBottom - p.r) { p.y = boxBottom - p.r; p.vy = -Math.abs(p.vy); }
        } else {
          // Gas or Supercritical
          p.x += p.vx * speedScale * (state.phase === 'supercritical' ? 2.2 : 1.6);
          p.y += p.vy * speedScale * (state.phase === 'supercritical' ? 2.2 : 1.6);
          if (p.x < boxX + p.r) { p.x = boxX + p.r; p.vx *= -1; }
          if (p.x > boxX + boxW - p.r) { p.x = boxX + boxW - p.r; p.vx *= -1; }
          if (p.y < boxY + 28) { p.y = boxY + 28; p.vy *= -1; }
          if (p.y > boxBottom - p.r) { p.y = boxBottom - p.r; p.vy *= -1; }
        }

        // Draw particle
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        if (state.phase === 'solid') {
          ctx.fillStyle = '#38bdf8';
          ctx.shadowColor = '#0284c7';
        } else if (state.phase === 'liquid') {
          ctx.fillStyle = '#06b6d4';
          ctx.shadowColor = '#0891b2';
        } else if (state.phase === 'gas') {
          ctx.fillStyle = '#f59e0b';
          ctx.shadowColor = '#d97706';
        } else {
          ctx.fillStyle = '#ec4899';
          ctx.shadowColor = '#db2777';
        }
        ctx.shadowBlur = 4;
        ctx.fill();
        ctx.shadowBlur = 0;
      }

      // Right Panel: Thermodynamic State & Dimensional Unit Converter
      var infoX = boxX + boxW + 20;
      var infoW = w - infoX - 20;

      // Card 1: State Description
      ctx.fillStyle = '#0f172a';
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      ctx.fillRect(infoX, boxY, infoW, 140);
      ctx.strokeRect(infoX, boxY, infoW, 140);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('PHYSICAL STATE PROPERTIES', infoX + 12, boxY + 24);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Current Phase: ' + state.phase.toUpperCase(), infoX + 12, boxY + 48);

      var orderText = state.phase === 'solid' ? 'Long-Range Crystalline Order' :
                      (state.phase === 'liquid' ? 'Short-Range Dynamic Order' : 'Zero Positional Order (Total Chaos)');
      ctx.fillText('Molecular Order: ' + orderText, infoX + 12, boxY + 70);

      var compText = state.phase === 'gas' ? 'Very High (Ideal/van der Waals)' :
                     (state.phase === 'supercritical' ? 'Moderate / Gas-like' : 'Near Zero (Incompressible)');
      ctx.fillText('Compressibility: ' + compText, infoX + 12, boxY + 92);

      var diffText = state.phase === 'gas' ? '~ 10⁻¹ cm²/s' :
                     (state.phase === 'liquid' ? '~ 10⁻⁵ cm²/s' : '< 10⁻¹² cm²/s');
      ctx.fillText('Self-Diffusion D: ' + diffText, infoX + 12, boxY + 114);

      // Card 2: Real-Time Dimensional Unit Converter
      var convY = boxY + 155;
      var convH = boxH - 155;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(infoX, convY, infoW, convH);
      ctx.strokeRect(infoX, convY, infoW, convH);

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('DIMENSIONAL CONVERSIONS (Live)', infoX + 12, convY + 24);

      // Pressure conversions
      var pBar = state.pressBar;
      var pPa = pBar * 1e5;
      var pAtm = pBar * 0.986923;
      var pTorr = pAtm * 760;

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px "Fira Code", monospace';
      ctx.fillText('PRESSURE CONVERSIONS:', infoX + 12, convY + 48);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('• Pascal (SI): ' + pPa.toExponential(4) + ' Pa', infoX + 18, convY + 68);
      ctx.fillText('• Standard atm: ' + pAtm.toFixed(4) + ' atm', infoX + 18, convY + 86);
      ctx.fillText('• Millimeters Hg: ' + pTorr.toFixed(2) + ' Torr', infoX + 18, convY + 104);

      // Temperature conversions
      var tK = state.tempK;
      var tC = tK - 273.15;
      var tF = tC * 9 / 5 + 32;

      ctx.fillStyle = '#cbd5e1';
      ctx.fillText('TEMPERATURE CONVERSIONS:', infoX + 12, convY + 130);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('• Kelvin (SI): ' + tK.toFixed(2) + ' K', infoX + 18, convY + 150);
      ctx.fillText('• Celsius: ' + tC.toFixed(2) + ' °C', infoX + 18, convY + 168);
      ctx.fillText('• Fahrenheit: ' + tF.toFixed(2) + ' °F', infoX + 18, convY + 186);

      animId = requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 2. sim_chem_gas_laws_maxwell_boltzmann
  // =========================================================================
  window.PChem1Sims.sim_chem_gas_laws_maxwell_boltzmann = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      gas: 'N2', // 'He' (4 g/mol), 'N2' (28 g/mol), 'Xe' (131 g/mol)
      molarMass: 0.028, // kg/mol
      tempK: 300,
      volL: 5.0,
      moles: 1.0,
      particles: []
    };

    var R = 8.314;
    var numP = 80;
    for (var i = 0; i < numP; i++) {
      state.particles.push({
        x: 40 + Math.random() * 260,
        y: 60 + Math.random() * 280,
        vx: (Math.random() - 0.5) * 4,
        vy: (Math.random() - 0.5) * 4,
        r: 3.5
      });
    }

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Gas Species:
          <select id="${controlsId}-species" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:0.25rem 0.5rem; margin-left:0.35rem;">
            <option value="He">Helium (He, M=4.00 g/mol)</option>
            <option value="N2" selected>Nitrogen (N₂, M=28.02 g/mol)</option>
            <option value="Xe">Xenon (Xe, M=131.29 g/mol)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.5rem;">Temperature:
          <input type="range" id="${controlsId}-temp" min="100" max="1000" step="10" value="300" style="vertical-align:middle; width:90px;">
          <span id="${controlsId}-temp-val" style="color:#38bdf8; font-family:monospace;">300 K</span>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.5rem;">Volume:
          <input type="range" id="${controlsId}-vol" min="2.0" max="10.0" step="0.2" value="5.0" style="vertical-align:middle; width:80px;">
          <span id="${controlsId}-vol-val" style="color:#38bdf8; font-family:monospace;">5.0 L</span>
        </label>
      `;

      var spSel = document.getElementById(`${controlsId}-species`);
      var tSl = document.getElementById(`${controlsId}-temp`);
      var vSl = document.getElementById(`${controlsId}-vol`);

      if (spSel) spSel.addEventListener('change', function(e) {
        state.gas = e.target.value;
        if (state.gas === 'He') state.molarMass = 0.004;
        else if (state.gas === 'N2') state.molarMass = 0.02802;
        else if (state.gas === 'Xe') state.molarMass = 0.13129;
      });

      if (tSl) tSl.addEventListener('input', function(e) {
        state.tempK = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-temp-val`).innerText = state.tempK + ' K';
      });

      if (vSl) vSl.addEventListener('input', function(e) {
        state.volL = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-vol-val`).innerText = state.volL.toFixed(1) + ' L';
      });
    }

    function render() {
      var w = setup.width;
      var h = setup.height;
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      // Gas chamber with movable piston (Left)
      var maxChamberW = w * 0.45;
      var chamberW = (state.volL / 10.0) * maxChamberW;
      var chamberH = h - 60;
      var cx = 20;
      var cy = 30;

      // Piston cylinder walls
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(cx + maxChamberW, cy);
      ctx.lineTo(cx, cy);
      ctx.lineTo(cx, cy + chamberH);
      ctx.lineTo(cx + maxChamberW, cy + chamberH);
      ctx.stroke();

      // Movable piston head
      ctx.fillStyle = '#334155';
      ctx.fillRect(cx + chamberW, cy, 14, chamberH);
      ctx.strokeStyle = '#0284c7';
      ctx.strokeRect(cx + chamberW, cy, 14, chamberH);

      // Label piston
      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText(`PISTON HEAD (V = ${state.volL.toFixed(1)} L)`, cx + chamberW - 110, cy + 18);

      // Thermal velocity scale v_scale ~ sqrt(T / M)
      var vScale = Math.sqrt((state.tempK / 300) / (state.molarMass / 0.02802));

      for (var i = 0; i < state.particles.length; i++) {
        var p = state.particles[i];
        p.x += p.vx * vScale * 0.7;
        p.y += p.vy * vScale * 0.7;

        if (p.x < cx + p.r) { p.x = cx + p.r; p.vx = Math.abs(p.vx); }
        if (p.x > cx + chamberW - p.r) { p.x = cx + chamberW - p.r; p.vx = -Math.abs(p.vx); }
        if (p.y < cy + p.r) { p.y = cy + p.r; p.vy = Math.abs(p.vy); }
        if (p.y > cy + chamberH - p.r) { p.y = cy + chamberH - p.r; p.vy = -Math.abs(p.vy); }

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = '#38bdf8';
        ctx.fill();
      }

      // Right Panel: Maxwell-Boltzmann Speed Distribution Curve
      var curveX = w * 0.52;
      var curveY = 30;
      var curveW = w - curveX - 25;
      var curveH = h - 60;

      ctx.fillStyle = '#0f172a';
      ctx.fillRect(curveX, curveY, curveW, curveH);
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      ctx.strokeRect(curveX, curveY, curveW, curveH);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('MAXWELL-BOLTZMANN SPEED DISTRIBUTION f(v)', curveX + 12, curveY + 22);

      // Calculate characteristic speeds
      var M = state.molarMass;
      var T = state.tempK;
      var v_mp = Math.sqrt((2 * R * T) / M);
      var v_avg = Math.sqrt((8 * R * T) / (Math.PI * M));
      var v_rms = Math.sqrt((3 * R * T) / M);

      // Max velocity on graph = 2.5 * v_rms
      var vMax = Math.max(1600, 2.5 * v_rms);

      // Plot f(v) curve
      var plotX0 = curveX + 45;
      var plotY0 = curveY + curveH - 45;
      var plotW = curveW - 60;
      var plotH = curveH - 80;

      // Axes
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0 + plotW, plotY0);
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0, plotY0 - plotH);
      ctx.stroke();

      ctx.fillStyle = '#64748b';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('Speed v (m/s)', plotX0 + plotW - 60, plotY0 + 20);
      ctx.fillText('f(v)', plotX0 - 30, plotY0 - plotH + 10);

      // Plot curve
      ctx.beginPath();
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.5;

      var peakF = (4 * Math.PI) * Math.pow(M / (2 * Math.PI * R * T), 1.5) * Math.pow(v_mp, 2) * Math.exp(-M * v_mp * v_mp / (2 * R * T));

      for (var px = 0; px <= plotW; px += 2) {
        var v = (px / plotW) * vMax;
        var f_v = (4 * Math.PI) * Math.pow(M / (2 * Math.PI * R * T), 1.5) * Math.pow(v, 2) * Math.exp(-M * v * v / (2 * R * T));
        var py = plotY0 - (f_v / peakF) * (plotH * 0.85);
        if (px === 0) ctx.moveTo(plotX0 + px, py);
        else ctx.lineTo(plotX0 + px, py);
      }
      ctx.stroke();

      // Vertical markers for v_mp, v_avg, v_rms
      function drawMarker(vVal, col, label) {
        var mx = plotX0 + (vVal / vMax) * plotW;
        if (mx <= plotX0 + plotW) {
          ctx.strokeStyle = col;
          ctx.setLineDash([3, 3]);
          ctx.beginPath();
          ctx.moveTo(mx, plotY0);
          ctx.lineTo(mx, plotY0 - plotH * 0.9);
          ctx.stroke();
          ctx.setLineDash([]);

          ctx.fillStyle = col;
          ctx.font = '10px "Fira Code", monospace';
          ctx.fillText(label, mx - 12, plotY0 - plotH * 0.92);
        }
      }

      drawMarker(v_mp, '#f59e0b', 'v_mp');
      drawMarker(v_avg, '#38bdf8', 'v̄');
      drawMarker(v_rms, '#ec4899', 'v_rms');

      // Numerical HUD readout
      var pIdealAtm = (state.moles * 0.08206 * state.tempK) / state.volL;
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px "Fira Code", monospace';
      ctx.fillText(`P_ideal: ${pIdealAtm.toFixed(2)} atm  |  T: ${T} K  |  M: ${(M*1000).toFixed(1)} g/mol`, curveX + 12, curveY + curveH - 12);
      ctx.fillText(`v_mp: ${Math.round(v_mp)} m/s | v̄: ${Math.round(v_avg)} m/s | v_rms: ${Math.round(v_rms)} m/s`, curveX + 12, curveY + curveH - 28);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 3. sim_chem_calorimetry_hess_cycle
  // =========================================================================
  window.PChem1Sims.sim_chem_calorimetry_hess_cycle = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      sample: 'benzoic', // 'benzoic', 'glucose', 'methane'
      massG: 1.22,
      cCal: 10.25, // kJ/K
      ignited: false,
      igniteTime: 0,
      tInitial: 298.15,
      deltaT: 0
    };

    var molarData = {
      benzoic: { name: 'Benzoic Acid (C₇H₆O₂)', M: 122.12, deltaHc: -3227 }, // kJ/mol
      glucose: { name: 'D-Glucose (C₆H₁₂O₆)', M: 180.16, deltaHc: -2808 },
      methane: { name: 'Methane (CH₄ gas)', M: 16.04, deltaHc: -890.3 }
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Combustion Fuel:
          <select id="${controlsId}-fuel" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:0.25rem 0.5rem; margin-left:0.35rem;">
            <option value="benzoic" selected>Benzoic Acid (C₇H₆O₂)</option>
            <option value="glucose">D-Glucose (C₆H₁₂O₆)</option>
            <option value="methane">Methane (CH₄)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.5rem;">Sample Mass:
          <input type="range" id="${controlsId}-mass" min="0.5" max="3.0" step="0.1" value="1.2" style="vertical-align:middle; width:80px;">
          <span id="${controlsId}-mass-val" style="color:#38bdf8; font-family:monospace;">1.2 g</span>
        </label>
        <button id="${controlsId}-ignite-btn" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:0.3rem 0.75rem; font-size:0.85rem; margin-left:0.75rem; cursor:pointer;">⚡ Trigger Ignition</button>
      `;

      var fSel = document.getElementById(`${controlsId}-fuel`);
      var mSl = document.getElementById(`${controlsId}-mass`);
      var btn = document.getElementById(`${controlsId}-ignite-btn`);

      if (fSel) fSel.addEventListener('change', function(e) {
        state.sample = e.target.value;
        state.ignited = false;
      });

      if (mSl) mSl.addEventListener('input', function(e) {
        state.massG = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-mass-val`).innerText = state.massG.toFixed(1) + ' g';
        state.ignited = false;
      });

      if (btn) btn.addEventListener('click', function() {
        state.ignited = true;
        state.igniteTime = Date.now();
      });
    }

    function render() {
      var w = setup.width;
      var h = setup.height;
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      var fuel = molarData[state.sample];
      var moles = state.massG / fuel.M;
      var qTotal = Math.abs(fuel.deltaHc) * moles; // kJ
      var expectedDeltaT = qTotal / state.cCal; // K

      // Left: Animated Bomb Calorimeter
      var calX = 30;
      var calY = 35;
      var calW = w * 0.42;
      var calH = h - 70;

      // Outer thermal adiabatic jacket
      ctx.fillStyle = '#1e293b';
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 3;
      ctx.fillRect(calX, calY, calW, calH);
      ctx.strokeRect(calX, calY, calW, calH);

      // Inner water bath
      var waterX = calX + 25;
      var waterY = calY + 25;
      var waterW = calW - 50;
      var waterH = calH - 45;
      ctx.fillStyle = '#0369a1';
      ctx.fillRect(waterX, waterY, waterW, waterH);

      // Steel bomb vessel
      var bombW = waterW * 0.48;
      var bombH = waterH * 0.65;
      var bombX = waterX + (waterW - bombW) / 2;
      var bombY = waterY + (waterH - bombH) / 2;
      ctx.fillStyle = '#0f172a';
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 2;
      ctx.fillRect(bombX, bombY, bombW, bombH);
      ctx.strokeRect(bombX, bombY, bombW, bombH);

      // Combustion crucible inside bomb
      var cruX = bombX + bombW * 0.3;
      var cruY = bombY + bombH * 0.6;
      var cruW = bombW * 0.4;
      var cruH = bombH * 0.25;
      ctx.fillStyle = '#64748b';
      ctx.fillRect(cruX, cruY, cruW, cruH);

      // Flame if ignited
      var elapsed = state.ignited ? (Date.now() - state.igniteTime) / 1000 : 0;
      var tempRise = 0;
      if (state.ignited) {
        tempRise = expectedDeltaT * (1 - Math.exp(-elapsed / 2.5));
        if (elapsed < 3.5) {
          // Flame animation
          ctx.fillStyle = '#f59e0b';
          ctx.beginPath();
          ctx.arc(cruX + cruW/2, cruY - 5, 8 + Math.random()*4, 0, Math.PI*2);
          ctx.fill();
        }
      }

      // Stirrer & Thermometer
      ctx.fillStyle = '#cbd5e1';
      ctx.fillRect(waterX + 15, calY - 10, 4, waterH + 20); // stirrer shaft
      ctx.fillRect(waterX + 10, waterY + waterH - 15, 20, 4); // stirrer blade

      ctx.fillStyle = '#ef4444';
      ctx.fillRect(waterX + waterW - 20, calY - 15, 6, waterH + 10); // thermometer
      ctx.beginPath();
      ctx.arc(waterX + waterW - 17, waterY + waterH - 10, 6, 0, Math.PI*2);
      ctx.fill();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('ADIABATIC BOMB CALORIMETER', calX + 10, calY + 18);

      // Right: Thermogram Heating Curve T vs time
      var graphX = calX + calW + 25;
      var graphY = 35;
      var graphW = w - graphX - 25;
      var graphH = h - 70;

      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graphX, graphY, graphW, graphH);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(graphX, graphY, graphW, graphH);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('EXPERIMENTAL THERMOGRAM (Temperature vs Time)', graphX + 12, graphY + 22);

      // Plot axes
      var pX0 = graphX + 50;
      var pY0 = graphY + graphH - 45;
      var pW = graphW - 70;
      var pH = graphH - 80;

      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(pX0, pY0);
      ctx.lineTo(pX0 + pW, pY0);
      ctx.moveTo(pX0, pY0);
      ctx.lineTo(pX0, pY0 - pH);
      ctx.stroke();

      ctx.fillStyle = '#64748b';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('Time t (s)', pX0 + pW - 45, pY0 + 20);
      ctx.fillText('T (K)', pX0 - 32, pY0 - pH + 10);

      // Draw baseline + rise curve
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      var tMaxRise = expectedDeltaT * 1.25;
      for (var px = 0; px <= pW; px += 3) {
        var tSec = (px / pW) * 15; // 0 to 15 seconds
        var tVal = 0;
        if (tSec > 3) {
          tVal = expectedDeltaT * (1 - Math.exp(-(tSec - 3) / 2.5));
        }
        var py = pY0 - (tVal / (tMaxRise || 1)) * (pH * 0.8);
        if (px === 0) ctx.moveTo(pX0 + px, py);
        else ctx.lineTo(pX0 + px, py);
      }
      ctx.stroke();

      // Readout
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px "Fira Code", monospace';
      var currentT = state.tInitial + tempRise;
      ctx.fillText(`T_obs: ${currentT.toFixed(3)} K | ΔT_max: ${expectedDeltaT.toFixed(3)} K`, graphX + 12, graphY + graphH - 12);
      ctx.fillText(`Heat Released q_v = C_cal·ΔT = ${qTotal.toFixed(2)} kJ  |  ΔH_c° = ${fuel.deltaHc} kJ/mol`, graphX + 12, graphY + graphH - 28);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 4. sim_chem_crystal_lattice_unit_cell
  // =========================================================================
  window.PChem1Sims.sim_chem_crystal_lattice_unit_cell = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      type: 'fcc', // 'sc', 'bcc', 'fcc'
      rotAngle: 0.35,
      sliceMode: false
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Cubic Lattice:
          <select id="${controlsId}-type" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:0.25rem 0.5rem; margin-left:0.35rem;">
            <option value="sc">Simple Cubic (SC)</option>
            <option value="bcc">Body-Centered Cubic (BCC)</option>
            <option value="fcc" selected>Face-Centered Cubic (FCC / CCP)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.75rem;">3D Rotation:
          <input type="range" id="${controlsId}-rot" min="0" max="6.28" step="0.05" value="0.35" style="vertical-align:middle; width:90px;">
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.75rem;">
          <input type="checkbox" id="${controlsId}-slice" style="vertical-align:middle;"> Unit Cell Slicing
        </label>
      `;

      var tSel = document.getElementById(`${controlsId}-type`);
      var rSl = document.getElementById(`${controlsId}-rot`);
      var chk = document.getElementById(`${controlsId}-slice`);

      if (tSel) tSel.addEventListener('change', function(e) { state.type = e.target.value; });
      if (rSl) rSl.addEventListener('input', function(e) { state.rotAngle = parseFloat(e.target.value); });
      if (chk) chk.addEventListener('change', function(e) { state.sliceMode = e.target.checked; });
    }

    function render() {
      var w = setup.width;
      var h = setup.height;
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      // Isometric 3D Projection
      var ox = w * 0.35;
      var oy = h * 0.52;
      var size = 130;
      var rot = state.rotAngle;

      function project3D(x, y, z) {
        // Rotate around Y axis
        var rx = x * Math.cos(rot) - z * Math.sin(rot);
        var rz = x * Math.sin(rot) + z * Math.cos(rot);
        // Isometric tilt
        var px = ox + (rx - rz * 0.35);
        var py = oy - y + (rx * 0.25 + rz * 0.45);
        return { x: px, y: py, depth: rz };
      }

      // Unit cell wireframe edges (8 corners: (±1, ±1, ±1))
      var corners = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1,  1], [1, -1,  1], [1, 1,  1], [-1, 1,  1]
      ];

      var edges = [
        [0,1],[1,2],[2,3],[3,0],
        [4,5],[5,6],[6,7],[7,4],
        [0,4],[1,5],[2,6],[3,7]
      ];

      // Draw wireframe
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 2;
      for (var e = 0; e < edges.length; e++) {
        var p1 = project3D(corners[edges[e][0]][0] * size/2, corners[edges[e][0]][1] * size/2, corners[edges[e][0]][2] * size/2);
        var p2 = project3D(corners[edges[e][1]][0] * size/2, corners[edges[e][1]][1] * size/2, corners[edges[e][1]][2] * size/2);
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();
      }

      // Collect atoms based on lattice
      var atoms = [];
      // 8 corner atoms
      for (var c = 0; c < 8; c++) {
        atoms.push({
          pos: [corners[c][0] * size/2, corners[c][1] * size/2, corners[c][2] * size/2],
          color: '#38bdf8',
          r: state.sliceMode ? 16 : 22,
          frac: '1/8'
        });
      }

      if (state.type === 'bcc') {
        // Body center atom
        atoms.push({
          pos: [0, 0, 0],
          color: '#f59e0b',
          r: state.sliceMode ? 26 : 26,
          frac: '1'
        });
      } else if (state.type === 'fcc') {
        // 6 face center atoms
        var faces = [
          [0, 0, size/2], [0, 0, -size/2],
          [size/2, 0, 0], [-size/2, 0, 0],
          [0, size/2, 0], [0, -size/2, 0]
        ];
        for (var f = 0; f < 6; f++) {
          atoms.push({
            pos: faces[f],
            color: '#10b981',
            r: state.sliceMode ? 18 : 22,
            frac: '1/2'
          });
        }
      }

      // Sort atoms by depth for proper painter's algorithm
      atoms.forEach(function(a) {
        a.proj = project3D(a.pos[0], a.pos[1], a.pos[2]);
      });
      atoms.sort(function(a, b) { return a.proj.depth - b.proj.depth; });

      // Draw atoms
      for (var i = 0; i < atoms.length; i++) {
        var a = atoms[i];
        ctx.beginPath();
        ctx.arc(a.proj.x, a.proj.y, a.r, 0, Math.PI * 2);
        ctx.fillStyle = a.color;
        ctx.shadowColor = '#000';
        ctx.shadowBlur = 6;
        ctx.fill();
        ctx.shadowBlur = 0;

        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1;
        ctx.stroke();
      }

      // Right Panel: Crystallographic Parameters & Packing Efficiency
      var panX = w * 0.62;
      var panY = 30;
      var panW = w - panX - 25;
      var panH = h - 60;

      ctx.fillStyle = '#0f172a';
      ctx.fillRect(panX, panY, panW, panH);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(panX, panY, panW, panH);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      var titleStr = state.type === 'sc' ? 'SIMPLE CUBIC (SC)' :
                     (state.type === 'bcc' ? 'BODY-CENTERED CUBIC (BCC)' : 'FACE-CENTERED CUBIC (FCC / CCP)');
      ctx.fillText(titleStr, panX + 12, panY + 24);

      var atomsPerCell = state.type === 'sc' ? '1 atom (8 × 1/8)' :
                         (state.type === 'bcc' ? '2 atoms (8 × 1/8 + 1 body)' : '4 atoms (8 × 1/8 + 6 × 1/2)');
      var coordNum = state.type === 'sc' ? '6' : (state.type === 'bcc' ? '8' : '12 (Closest Packing)');
      var geomRel = state.type === 'sc' ? 'a = 2r' : (state.type === 'bcc' ? '4r = a√3  →  r = a√3/4' : '4r = a√2  →  r = a√2/4');
      var apfVal = state.type === 'sc' ? '52.36% (π / 6)' : (state.type === 'bcc' ? '68.02% (π√3 / 8)' : '74.05% (π√2 / 6)');

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Atoms Per Unit Cell N: ', panX + 12, panY + 54);
      ctx.fillStyle = '#cbd5e1';
      ctx.fillText(atomsPerCell, panX + 12, panY + 72);

      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Coordination Number (CN): ', panX + 12, panY + 100);
      ctx.fillStyle = '#cbd5e1';
      ctx.fillText(coordNum, panX + 12, panY + 118);

      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Lattice Geometry Relation: ', panX + 12, panY + 146);
      ctx.fillStyle = '#f59e0b';
      ctx.font = '11px "Fira Code", monospace';
      ctx.fillText(geomRel, panX + 12, panY + 164);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Atomic Packing Factor (APF): ', panX + 12, panY + 192);
      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 15px "Fira Code", monospace';
      ctx.fillText(apfVal, panX + 12, panY + 214);

      // Packing bar visual
      var barW = panW - 24;
      var barH = 14;
      var barY = panY + 230;
      ctx.fillStyle = '#1e293b';
      ctx.fillRect(panX + 12, barY, barW, barH);
      var pct = state.type === 'sc' ? 0.5236 : (state.type === 'bcc' ? 0.6802 : 0.7405);
      ctx.fillStyle = '#10b981';
      ctx.fillRect(panX + 12, barY, barW * pct, barH);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 5. sim_chem_solution_colligative_properties
  // =========================================================================
  window.PChem1Sims.sim_chem_solution_colligative_properties = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      solute: 'nacl', // 'glucose' (i=1), 'nacl' (i=1.9), 'cacl2' (i=2.7)
      molality: 1.0,
      vanTHoff: 1.9,
      waterKf: 1.86, // K·kg/mol
      waterKb: 0.512 // K·kg/mol
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Solute Particle:
          <select id="${controlsId}-solute" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:0.25rem 0.5rem; margin-left:0.35rem;">
            <option value="glucose">Glucose (Nonelectrolyte, i = 1.0)</option>
            <option value="nacl" selected>Sodium Chloride (NaCl, i = 1.9)</option>
            <option value="cacl2">Calcium Chloride (CaCl₂, i = 2.7)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.75rem;">Molality m:
          <input type="range" id="${controlsId}-mol" min="0.1" max="3.0" step="0.1" value="1.0" style="vertical-align:middle; width:90px;">
          <span id="${controlsId}-mol-val" style="color:#38bdf8; font-family:monospace;">1.0 m</span>
        </label>
      `;

      var sSel = document.getElementById(`${controlsId}-solute`);
      var mSl = document.getElementById(`${controlsId}-mol`);

      if (sSel) sSel.addEventListener('change', function(e) {
        state.solute = e.target.value;
        if (state.solute === 'glucose') state.vanTHoff = 1.0;
        else if (state.solute === 'nacl') state.vanTHoff = 1.9;
        else if (state.solute === 'cacl2') state.vanTHoff = 2.7;
      });

      if (mSl) mSl.addEventListener('input', function(e) {
        state.molality = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-mol-val`).innerText = state.molality.toFixed(1) + ' m';
      });
    }

    function render() {
      var w = setup.width;
      var h = setup.height;
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      // Colligative shifts
      var deltaTf = state.vanTHoff * state.waterKf * state.molality;
      var deltaTb = state.vanTHoff * state.waterKb * state.molality;
      var osmoticPi = state.vanTHoff * state.molality * 0.08206 * 298.15; // atm approx

      // Left: Osmotic Pressure U-Tube Chamber
      var tubeX = 40;
      var tubeY = 40;
      var tubeW = w * 0.45;
      var tubeH = h - 80;

      // Draw U-tube
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(tubeX, tubeY, tubeW, tubeH);
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 3;

      var armW = 45;
      var bottomH = 40;
      var midX = tubeX + tubeW / 2;

      // Left arm (Pure Solvent)
      var leftH = tubeH - 70;
      ctx.fillStyle = '#0284c7';
      ctx.fillRect(tubeX + 25, tubeY + tubeH - bottomH - leftH, armW, leftH + bottomH);

      // Right arm (Solution with osmotic rise)
      var hRise = Math.min(tubeH - 60, 25 + osmoticPi * 1.5);
      ctx.fillStyle = '#06b6d4';
      ctx.fillRect(tubeX + tubeW - 25 - armW, tubeY + tubeH - bottomH - hRise, armW, hRise + bottomH);

      // Semi-permeable membrane at bottom
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(midX, tubeY + tubeH - bottomH);
      ctx.lineTo(midX, tubeY + tubeH);
      ctx.stroke();

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('Pure Water', tubeX + 22, tubeY + tubeH + 18);
      ctx.fillText('Solution', tubeX + tubeW - 65, tubeY + tubeH + 18);
      ctx.fillText('MEMBRANE', midX - 25, tubeY + tubeH - bottomH - 8);

      // Osmotic height difference indicator
      ctx.strokeStyle = '#ef4444';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(tubeX + 25 + armW, tubeY + tubeH - bottomH - leftH);
      ctx.lineTo(tubeX + tubeW - 25, tubeY + tubeH - bottomH - leftH);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#ef4444';
      ctx.font = 'bold 11px "Fira Code", monospace';
      ctx.fillText(`Δh → Π = ${osmoticPi.toFixed(1)} atm`, midX - 50, tubeY + tubeH - bottomH - hRise - 8);

      // Right: Phase Diagram Temperature Shifts & Colligative Summary
      var panX = tubeX + tubeW + 25;
      var panY = 40;
      var panW = w - panX - 25;
      var panH = h - 80;

      ctx.fillStyle = '#0f172a';
      ctx.fillRect(panX, panY, panW, panH);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(panX, panY, panW, panH);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('COLLIGATIVE PROPERTIES DASHBOARD', panX + 12, panY + 24);

      // 1. Freezing Point Depression
      ctx.fillStyle = '#38bdf8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('1. Freezing Point Depression (ΔT_f):', panX + 12, panY + 55);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px "Fira Code", monospace';
      ctx.fillText(`ΔT_f = i·K_f·m = ${state.vanTHoff} × 1.86 × ${state.molality.toFixed(1)} = ${deltaTf.toFixed(3)} °C`, panX + 18, panY + 75);
      ctx.fillText(`New Freezing Point: T_f = -${deltaTf.toFixed(3)} °C (273.15 K → ${(273.15 - deltaTf).toFixed(2)} K)`, panX + 18, panY + 93);

      // 2. Boiling Point Elevation
      ctx.fillStyle = '#f59e0b';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('2. Boiling Point Elevation (ΔT_b):', panX + 12, panY + 125);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px "Fira Code", monospace';
      ctx.fillText(`ΔT_b = i·K_b·m = ${state.vanTHoff} × 0.512 × ${state.molality.toFixed(1)} = ${deltaTb.toFixed(3)} °C`, panX + 18, panY + 145);
      ctx.fillText(`New Boiling Point: T_b = ${(100.0 + deltaTb).toFixed(3)} °C (373.15 K → ${(373.15 + deltaTb).toFixed(2)} K)`, panX + 18, panY + 163);

      // 3. Osmotic Pressure
      ctx.fillStyle = '#10b981';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('3. Osmotic Pressure (Π = i·M·R·T):', panX + 12, panY + 195);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px "Fira Code", monospace';
      ctx.fillText(`Π ≈ ${osmoticPi.toFixed(2)} atm (${(osmoticPi * 1.01325).toFixed(2)} bar)`, panX + 18, panY + 215);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 6. sim_chem_reaction_kinetics_arrhenius
  // =========================================================================
  window.PChem1Sims.sim_chem_reaction_kinetics_arrhenius = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      order: 1, // 0, 1, 2
      a0: 1.0, // mol/L
      tempK: 300,
      hasCatalyst: false
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Reaction Order:
          <select id="${controlsId}-order" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:0.25rem 0.5rem; margin-left:0.35rem;">
            <option value="0">Zero-Order (r = k)</option>
            <option value="1" selected>First-Order (r = k[A])</option>
            <option value="2">Second-Order (r = k[A]²)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.75rem;">Temperature:
          <input type="range" id="${controlsId}-temp" min="250" max="600" step="10" value="300" style="vertical-align:middle; width:85px;">
          <span id="${controlsId}-temp-val" style="color:#38bdf8; font-family:monospace;">300 K</span>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.75rem;">
          <input type="checkbox" id="${controlsId}-cat" style="vertical-align:middle;"> Catalyst (Lowers E_a)
        </label>
      `;

      var oSel = document.getElementById(`${controlsId}-order`);
      var tSl = document.getElementById(`${controlsId}-temp`);
      var cChk = document.getElementById(`${controlsId}-cat`);

      if (oSel) oSel.addEventListener('change', function(e) { state.order = parseInt(e.target.value, 10); });
      if (tSl) tSl.addEventListener('input', function(e) {
        state.tempK = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-temp-val`).innerText = state.tempK + ' K';
      });
      if (cChk) cChk.addEventListener('change', function(e) { state.hasCatalyst = e.target.checked; });
    }

    function render() {
      var w = setup.width;
      var h = setup.height;
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      // Arrhenius rate constant calculation: k = A * exp(-E_a / RT)
      var R = 8.314;
      var EaBase = 50000; // J/mol (50 kJ/mol)
      var Ea = state.hasCatalyst ? 30000 : EaBase; // Catalyst lowers Ea by 20 kJ/mol
      var A_factor = 1e7;
      var k = A_factor * Math.exp(-Ea / (R * state.tempK));

      // Left Panel: Concentration Decay Curve [A] vs t
      var g1X = 35;
      var g1Y = 35;
      var g1W = w * 0.44;
      var g1H = h - 70;

      ctx.fillStyle = '#0f172a';
      ctx.fillRect(g1X, g1Y, g1W, g1H);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(g1X, g1Y, g1W, g1H);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('CONCENTRATION PROFILE [A] vs TIME', g1X + 12, g1Y + 22);

      var p1X0 = g1X + 45;
      var p1Y0 = g1Y + g1H - 45;
      var p1W = g1W - 60;
      var p1H = g1H - 75;

      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(p1X0, p1Y0);
      ctx.lineTo(p1X0 + p1W, p1Y0);
      ctx.moveTo(p1X0, p1Y0);
      ctx.lineTo(p1X0, p1Y0 - p1H);
      ctx.stroke();

      ctx.fillStyle = '#64748b';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('Time t (s)', p1X0 + p1W - 40, p1Y0 + 20);
      ctx.fillText('[A] (M)', p1X0 - 32, p1Y0 - p1H + 10);

      // Draw [A](t) curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      var tMax = 60; // 60 seconds
      for (var px = 0; px <= p1W; px += 2) {
        var t = (px / p1W) * tMax;
        var conc = 0;
        if (state.order === 0) {
          conc = Math.max(0, state.a0 - k * 0.02 * t);
        } else if (state.order === 1) {
          conc = state.a0 * Math.exp(-k * 0.05 * t);
        } else {
          conc = state.a0 / (1 + k * 0.1 * state.a0 * t);
        }
        var py = p1Y0 - (conc / state.a0) * (p1H * 0.85);
        if (px === 0) ctx.moveTo(p1X0 + px, py);
        else ctx.lineTo(p1X0 + px, py);
      }
      ctx.stroke();

      // Right Panel: Reaction Energy Coordinate & Activation Energy Barrier E_a
      var g2X = g1X + g1W + 20;
      var g2Y = 35;
      var g2W = w - g2X - 25;
      var g2H = h - 70;

      ctx.fillStyle = '#0f172a';
      ctx.fillRect(g2X, g2Y, g2W, g2H);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(g2X, g2Y, g2W, g2H);

      ctx.fillStyle = '#f59e0b';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('REACTION ENERGY PROFILE (E_a Barrier)', g2X + 12, g2Y + 22);

      var p2X0 = g2X + 45;
      var p2Y0 = g2Y + g2H - 45;
      var p2W = g2W - 60;
      var p2H = g2H - 75;

      // Draw Energy Coordinate
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(p2X0, p2Y0);
      ctx.lineTo(p2X0 + p2W, p2Y0);
      ctx.moveTo(p2X0, p2Y0);
      ctx.lineTo(p2X0, p2Y0 - p2H);
      ctx.stroke();

      ctx.fillStyle = '#64748b';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('Reaction Coordinate', p2X0 + p2W - 85, p2Y0 + 20);
      ctx.fillText('Potential Energy', p2X0 - 40, p2Y0 - p2H + 10);

      // Uncatalyzed profile (Dotted if catalyzed)
      ctx.strokeStyle = state.hasCatalyst ? '#64748b' : '#ef4444';
      ctx.lineWidth = 2;
      ctx.beginPath();
      var rY = p2Y0 - p2H * 0.35; // Reactants
      var pY = p2Y0 - p2H * 0.15; // Products (Exothermic)
      var tsUncatY = p2Y0 - p2H * 0.85; // Uncatalyzed Transition State
      ctx.moveTo(p2X0 + 10, rY);
      ctx.bezierCurveTo(p2X0 + p2W * 0.3, rY, p2X0 + p2W * 0.45, tsUncatY, p2X0 + p2W * 0.5, tsUncatY);
      ctx.bezierCurveTo(p2X0 + p2W * 0.55, tsUncatY, p2X0 + p2W * 0.7, pY, p2X0 + p2W - 10, pY);
      ctx.stroke();

      if (state.hasCatalyst) {
        // Catalyzed curve (Green)
        var tsCatY = p2Y0 - p2H * 0.58;
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(p2X0 + 10, rY);
        ctx.bezierCurveTo(p2X0 + p2W * 0.3, rY, p2X0 + p2W * 0.45, tsCatY, p2X0 + p2W * 0.5, tsCatY);
        ctx.bezierCurveTo(p2X0 + p2W * 0.55, tsCatY, p2X0 + p2W * 0.7, pY, p2X0 + p2W - 10, pY);
        ctx.stroke();

        ctx.fillStyle = '#10b981';
        ctx.font = '10px "Fira Code", monospace';
        ctx.fillText('Catalyzed Path (E_a = 30 kJ/mol)', p2X0 + p2W * 0.35, tsCatY - 10);
      } else {
        ctx.fillStyle = '#ef4444';
        ctx.font = '10px "Fira Code", monospace';
        ctx.fillText('Uncatalyzed E_a = 50 kJ/mol', p2X0 + p2W * 0.35, tsUncatY - 10);
      }

      // Readout
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px "Fira Code", monospace';
      ctx.fillText(`k: ${k.toExponential(3)} s⁻¹  |  T: ${state.tempK} K  |  E_a: ${(Ea/1000).toFixed(0)} kJ/mol`, g2X + 12, g2Y + g2H - 12);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 7. sim_chem_equilibrium_le_chatelier
  // =========================================================================
  window.PChem1Sims.sim_chem_equilibrium_le_chatelier = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    // Haber Reaction: N2 + 3H2 <=> 2NH3  (Exothermic: deltaH = -92 kJ/mol)
    var state = {
      nN2: 1.0,
      nH2: 3.0,
      nNH3: 0.5,
      tempK: 500,
      volumeL: 5.0
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Temperature:
          <input type="range" id="${controlsId}-temp" min="300" max="800" step="10" value="500" style="vertical-align:middle; width:80px;">
          <span id="${controlsId}-temp-val" style="color:#38bdf8; font-family:monospace;">500 K</span>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.5rem;">Volume:
          <input type="range" id="${controlsId}-vol" min="2.0" max="10.0" step="0.5" value="5.0" style="vertical-align:middle; width:75px;">
          <span id="${controlsId}-vol-val" style="color:#38bdf8; font-family:monospace;">5.0 L</span>
        </label>
        <button id="${controlsId}-add-react" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:0.25rem 0.5rem; font-size:0.8rem; margin-left:0.5rem; cursor:pointer;">+ Add N₂/H₂</button>
        <button id="${controlsId}-rem-prod" style="background:#059669; color:#fff; border:none; border-radius:4px; padding:0.25rem 0.5rem; font-size:0.8rem; margin-left:0.35rem; cursor:pointer;">- Remove NH₃</button>
      `;

      var tSl = document.getElementById(`${controlsId}-temp`);
      var vSl = document.getElementById(`${controlsId}-vol`);
      var bReact = document.getElementById(`${controlsId}-add-react`);
      var bProd = document.getElementById(`${controlsId}-rem-prod`);

      if (tSl) tSl.addEventListener('input', function(e) {
        state.tempK = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-temp-val`).innerText = state.tempK + ' K';
      });

      if (vSl) vSl.addEventListener('input', function(e) {
        state.volumeL = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-vol-val`).innerText = state.volumeL.toFixed(1) + ' L';
      });

      if (bReact) bReact.addEventListener('click', function() {
        state.nN2 += 0.8;
        state.nH2 += 1.5;
      });

      if (bProd) bProd.addEventListener('click', function() {
        state.nNH3 = Math.max(0.1, state.nNH3 - 0.8);
      });
    }

    function render() {
      var w = setup.width;
      var h = setup.height;
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      // Equilibrium constant from van 't Hoff: ln(K2/K1) = -deltaH/R * (1/T2 - 1/T1)
      // Reference at 500 K: Kc ~ 0.05
      var R = 8.314;
      var deltaH = -92200; // J/mol
      var Kc_ref = 0.05;
      var T_ref = 500;
      var Kc = Kc_ref * Math.exp((-deltaH / R) * ((1 / state.tempK) - (1 / T_ref)));

      // Current concentrations: C = n / V
      var cN2 = state.nN2 / state.volumeL;
      var cH2 = state.nH2 / state.volumeL;
      var cNH3 = state.nNH3 / state.volumeL;

      // Reaction quotient: Qc = [NH3]^2 / ([N2] * [H2]^3)
      var denom = cN2 * Math.pow(cH2, 3);
      var Qc = denom > 1e-6 ? Math.pow(cNH3, 2) / denom : 999;

      // Dynamic approach to equilibrium: shift moles toward Qc == Kc
      var rate = 0.015;
      if (Qc < Kc * 0.95) {
        // Shift forward (consume N2, H2 -> form NH3)
        var step = Math.min(0.01, (state.nN2 * 0.02));
        state.nN2 -= step;
        state.nH2 -= 3 * step;
        state.nNH3 += 2 * step;
      } else if (Qc > Kc * 1.05) {
        // Shift reverse (decompose NH3 -> form N2, H2)
        var step = Math.min(0.01, (state.nNH3 * 0.02));
        state.nNH3 -= 2 * step;
        state.nN2 += step;
        state.nH2 += 3 * step;
      }

      // Left Panel: Dynamic Chemical Chamber & Bar Chart
      var cX = 35;
      var cY = 35;
      var cW = w * 0.44;
      var cH = h - 70;

      ctx.fillStyle = '#0f172a';
      ctx.fillRect(cX, cY, cW, cH);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(cX, cY, cW, cH);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('HABER EQUILIBRIUM: N₂(g) + 3H₂(g) ⇌ 2NH₃(g)', cX + 12, cY + 22);

      // Bar chart for concentrations
      var barW = 40;
      var maxC = 2.0;
      var chartY = cY + cH - 50;

      function drawBar(x, val, col, label) {
        var hBar = Math.min(cH - 90, (val / maxC) * (cH - 100));
        ctx.fillStyle = col;
        ctx.fillRect(x, chartY - hBar, barW, hBar);
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1;
        ctx.strokeRect(x, chartY - hBar, barW, hBar);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '10px "Fira Code", monospace';
        ctx.fillText(val.toFixed(2) + ' M', x - 2, chartY - hBar - 6);
        ctx.fillText(label, x + 8, chartY + 18);
      }

      drawBar(cX + 30, cN2, '#38bdf8', '[N₂]');
      drawBar(cX + 100, cH2, '#f59e0b', '[H₂]');
      drawBar(cX + 170, cNH3, '#10b981', '[NH₃]');

      // Right Panel: Le Chatelier Quotient Q vs K Gauge
      var gX = cX + cW + 20;
      var gY = 35;
      var gW = w - gX - 25;
      var gH = h - 70;

      ctx.fillStyle = '#0f172a';
      ctx.fillRect(gX, gY, gW, gH);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(gX, gY, gW, gH);

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('LE CHÂTELIER REACTION QUOTIENT (Q_c vs K_c)', gX + 12, gY + 22);

      // Equilibrium status gauge
      var gaugeY = gY + 70;
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Equilibrium Constant K_c(T): ' + Kc.toExponential(3), gX + 15, gaugeY);
      ctx.fillText('Current Reaction Quotient Q_c: ' + Qc.toExponential(3), gX + 15, gaugeY + 25);

      var statusText = Math.abs(Qc - Kc) / Kc < 0.1 ? 'Dynamic Equilibrium (Q ≈ K)' :
                       (Qc < Kc ? 'SHIFTS FORWARD → (Produces NH₃)' : '← SHIFTS REVERSE (Decomposes NH₃)');
      var statusCol = Math.abs(Qc - Kc) / Kc < 0.1 ? '#10b981' : (Qc < Kc ? '#38bdf8' : '#ef4444');

      ctx.fillStyle = statusCol;
      ctx.font = 'bold 14px Inter, sans-serif';
      ctx.fillText(statusText, gX + 15, gaugeY + 65);

      // Temperature effect explanation
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('• Exothermic reaction (ΔH° = -92.2 kJ/mol)', gX + 15, gaugeY + 105);
      ctx.fillText('• Increasing T decreases K_c (van \'t Hoff law)', gX + 15, gaugeY + 125);
      ctx.fillText('• Compressing chamber (↓V) shifts toward fewer moles (→)', gX + 15, gaugeY + 145);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 8. sim_chem_galvanic_cell_nernst
  // =========================================================================
  window.PChem1Sims.sim_chem_galvanic_cell_nernst = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    // Daniell Cell: Zn(s) | Zn2+(aq) || Cu2+(aq) | Cu(s)
    var state = {
      cZn: 1.0, // mol/L
      cCu: 1.0, // mol/L
      tempK: 298.15,
      isElectrolytic: false,
      electronOffset: 0
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">[Zn²⁺] Anode:
          <input type="range" id="${controlsId}-zn" min="0.001" max="2.0" step="0.05" value="1.0" style="vertical-align:middle; width:80px;">
          <span id="${controlsId}-zn-val" style="color:#38bdf8; font-family:monospace;">1.00 M</span>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.5rem;">[Cu²⁺] Cathode:
          <input type="range" id="${controlsId}-cu" min="0.001" max="2.0" step="0.05" value="1.0" style="vertical-align:middle; width:80px;">
          <span id="${controlsId}-cu-val" style="color:#38bdf8; font-family:monospace;">1.00 M</span>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem; margin-left:0.5rem;">
          <input type="checkbox" id="${controlsId}-mode" style="vertical-align:middle;"> Electrolytic Recharge Mode
        </label>
      `;

      var znSl = document.getElementById(`${controlsId}-zn`);
      var cuSl = document.getElementById(`${controlsId}-cu`);
      var mChk = document.getElementById(`${controlsId}-mode`);

      if (znSl) znSl.addEventListener('input', function(e) {
        state.cZn = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-zn-val`).innerText = state.cZn.toFixed(2) + ' M';
      });

      if (cuSl) cuSl.addEventListener('input', function(e) {
        state.cCu = parseFloat(e.target.value);
        document.getElementById(`${controlsId}-cu-val`).innerText = state.cCu.toFixed(2) + ' M';
      });

      if (mChk) mChk.addEventListener('change', function(e) {
        state.isElectrolytic = e.target.checked;
      });
    }

    function render() {
      var w = setup.width;
      var h = setup.height;
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      // Nernst Equation: E_cell = E0 - (RT / nF) * ln(Q)
      // E0 = E(Cu2+/Cu) - E(Zn2+/Zn) = 0.34 - (-0.76) = 1.100 V
      var E0 = 1.100;
      var n = 2;
      var R = 8.314;
      var F = 96485;
      var Q = state.cZn / state.cCu;
      var nernstFactor = (R * state.tempK) / (n * F);
      var E_cell = E0 - nernstFactor * Math.log(Q);
      var deltaG = -n * F * E_cell / 1000; // kJ/mol

      // Left: Animated Daniell Cell Apparatus
      var cellX = 35;
      var cellY = 35;
      var cellW = w * 0.52;
      var cellH = h - 70;

      // Two Beakers
      var bW = 100;
      var bH = 150;
      var bY = cellY + cellH - bH - 10;
      var b1X = cellX + 30; // Zn Beaker
      var b2X = cellX + cellW - bW - 30; // Cu Beaker

      // Zn Beaker & solution
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(b1X, bY, bW, bH);
      ctx.fillStyle = 'rgba(56, 189, 248, 0.25)'; // Zn2+ solution
      ctx.fillRect(b1X, bY + 30, bW, bH - 30);
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 2;
      ctx.strokeRect(b1X, bY, bW, bH);

      // Cu Beaker & solution
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(b2X, bY, bW, bH);
      ctx.fillStyle = 'rgba(16, 185, 129, 0.25)'; // Cu2+ solution
      ctx.fillRect(b2X, bY + 30, bW, bH - 30);
      ctx.strokeRect(b2X, bY, bW, bH);

      // Electrodes
      // Zn Anode (Grey)
      ctx.fillStyle = '#94a3b8';
      ctx.fillRect(b1X + 35, bY - 20, 25, bH);
      ctx.strokeStyle = '#cbd5e1';
      ctx.strokeRect(b1X + 35, bY - 20, 25, bH);

      // Cu Cathode (Copper-Orange)
      ctx.fillStyle = '#d97706';
      ctx.fillRect(b2X + 35, bY - 20, 25, bH);
      ctx.strokeStyle = '#f59e0b';
      ctx.strokeRect(b2X + 35, bY - 20, 25, bH);

      // Inverted U-tube Salt Bridge (KNO3)
      var sbX1 = b1X + 70;
      var sbX2 = b2X + 30;
      var sbTopY = bY + 15;
      ctx.strokeStyle = '#fbbf24';
      ctx.lineWidth = 14;
      ctx.lineCap = 'round';
      ctx.beginPath();
      ctx.moveTo(sbX1, bY + 80);
      ctx.lineTo(sbX1, sbTopY);
      ctx.lineTo(sbX2, sbTopY);
      ctx.lineTo(sbX2, bY + 80);
      ctx.stroke();

      ctx.fillStyle = '#0f172a';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('SALT BRIDGE (KNO₃)', (sbX1 + sbX2) / 2 - 45, sbTopY - 12);

      // External Circuit Wire & Voltmeter
      var wireY = cellY + 25;
      ctx.strokeStyle = '#cbd5e1';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(b1X + 47, bY - 20);
      ctx.lineTo(b1X + 47, wireY);
      ctx.lineTo(b2X + 47, wireY);
      ctx.lineTo(b2X + 47, bY - 20);
      ctx.stroke();

      // Voltmeter Circle at center
      var vmX = (b1X + b2X) / 2 + 47;
      ctx.fillStyle = '#0f172a';
      ctx.beginPath();
      ctx.arc(vmX, wireY, 20, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 11px "Fira Code", monospace';
      ctx.fillText(E_cell.toFixed(3) + 'V', vmX - 18, wireY + 4);

      // Animated Electron Flow on Wire
      state.electronOffset = (state.electronOffset + (state.isElectrolytic ? -1.5 : 1.5)) % 25;
      ctx.fillStyle = '#facc15';
      var wireLen = (b2X - b1X);
      for (var ex = 10; ex < wireLen - 10; ex += 25) {
        var dotX = b1X + 47 + ((ex + state.electronOffset) % wireLen);
        if (Math.abs(dotX - vmX) > 22) {
          ctx.beginPath();
          ctx.arc(dotX, wireY, 3, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // Labels on electrodes
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('Zn Anode (-)', b1X + 15, bY + bH + 20);
      ctx.fillText('Cu Cathode (+)', b2X + 15, bY + bH + 20);

      // Right Panel: Nernst Equation & Thermodynamics Dashboard
      var panX = cellX + cellW + 20;
      var panY = 35;
      var panW = w - panX - 25;
      var panH = h - 70;

      ctx.fillStyle = '#0f172a';
      ctx.fillRect(panX, panY, panW, panH);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(panX, panY, panW, panH);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('ELECTROCHEMISTRY & NERNST DASHBOARD', panX + 12, panY + 22);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('Standard Cell Potential E°:', panX + 12, panY + 50);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = 'bold 12px "Fira Code", monospace';
      ctx.fillText('E°_cell = +1.100 V (Spontaneous)', panX + 18, panY + 68);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('Reaction Quotient Q = [Zn²⁺]/[Cu²⁺]:', panX + 12, panY + 95);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '12px "Fira Code", monospace';
      ctx.fillText(`Q = ${state.cZn.toFixed(2)} / ${state.cCu.toFixed(2)} = ${Q.toFixed(3)}`, panX + 18, panY + 113);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('Nernst Potential E_cell at 298.15 K:', panX + 12, panY + 140);
      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 15px "Fira Code", monospace';
      ctx.fillText(`E_cell = ${E_cell.toFixed(4)} V`, panX + 18, panY + 162);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('Gibbs Free Energy Change ΔG:', panX + 12, panY + 190);
      ctx.fillStyle = deltaG < 0 ? '#10b981' : '#ef4444';
      ctx.font = 'bold 13px "Fira Code", monospace';
      ctx.fillText(`ΔG = -nFE = ${deltaG.toFixed(2)} kJ/mol`, panX + 18, panY + 210);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // Platform Mount Adapter for SimulationEngine (compatible with app.js)
  // =========================================================================
  var SIM_TITLES = {
    sim_chem_dimensional_matter_converter: "Interactive Dimensional Analysis & 3D Phase States Visualizer",
    sim_chem_gas_laws_maxwell_boltzmann: "Kinetic Molecular Gas Chamber & Maxwell-Boltzmann Speed Engine",
    sim_chem_calorimetry_hess_cycle: "Adiabatic Bomb Calorimeter & Dynamic Hess's Law Thermogram",
    sim_chem_crystal_lattice_unit_cell: "3D Crystal Unit Cell Slicer & Atomic Packing Factor Engine (SC/BCC/FCC)",
    sim_chem_solution_colligative_properties: "Osmotic Pressure U-Tube & Colligative Shifts Simulator (ΔTf, ΔTb, Π)",
    sim_chem_reaction_kinetics_arrhenius: "Multi-Order Integrated Rate Laws & Arrhenius Activation Barrier Engine",
    sim_chem_equilibrium_le_chatelier: "Haber Synthesis Dynamic Reactor & Le Châtelier Q vs K Gauge",
    sim_chem_galvanic_cell_nernst: "Animated Daniell Galvanic Cell & Real-Time Nernst Potential Simulator"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.PChem1Sims || typeof window.PChem1Sims[simType] !== 'function') {
      console.warn('Simulation type not found in PChem1Sims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Physical Chemistry Interactive Simulation";
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
      window.PChem1Sims[simType](canvasId, controlsId);
    }, 50);
  };

})();
