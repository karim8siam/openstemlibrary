// Industrial Chemistry Interactive Simulation Suite
// 10 Real-Time 60 FPS Canvas Engines for Industrial Chemistry (#48)
// Mounted via window.SimulationEngine.initSimulation(containerId, simType)

(function() {
  'use strict';

  window.IndustrialSims = window.IndustrialSims || {};

  // =========================================================================
  // Helper Utilities
  // =========================================================================
  function getCanvasAndCtx(canvasId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return null;
    var ctx = canvas.getContext('2d');
    return { canvas: canvas, ctx: ctx };
  }

  function clearCanvas(ctx, width, height, bgColor) {
    ctx.fillStyle = bgColor || '#080d19';
    ctx.fillRect(0, 0, width, height);
  }

  function drawGrid(ctx, width, height, step, strokeStyle) {
    ctx.save();
    ctx.strokeStyle = strokeStyle || 'rgba(255, 255, 255, 0.04)';
    ctx.lineWidth = 1;
    for (var x = 0; x < width; x += step) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    for (var y = 0; y < height; y += step) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }
    ctx.restore();
  }

  // =========================================================================
  // 1. Viscose Rayon Acid Coagulation & Filament Draw Simulator
  // =========================================================================
  window.IndustrialSims.sim_ind_textile_viscose_spinning = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var h2so4Conc = 10.0; // wt% H2SO4
    var znso4Conc = 1.2;  // wt% ZnSO4
    var drawRatio = 1.6;  // stretching draw ratio
    var spinSpeed = 80;   // m/min
    var animOffset = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Bath H₂SO₄ (%):</strong>
            <input type="range" id="${canvasId}-h2so4" min="7" max="14" step="0.5" value="${h2so4Conc}" style="vertical-align:middle;">
            <span id="${canvasId}-h2so4-val">${h2so4Conc}%</span>
          </label>
          <label><strong>ZnSO₄ Modifier (%):</strong>
            <input type="range" id="${canvasId}-znso4" min="0.5" max="3.0" step="0.1" value="${znso4Conc}" style="vertical-align:middle;">
            <span id="${canvasId}-znso4-val">${znso4Conc}%</span>
          </label>
          <label><strong>Draw Ratio:</strong>
            <input type="range" id="${canvasId}-draw" min="1.0" max="2.5" step="0.1" value="${drawRatio}" style="vertical-align:middle;">
            <span id="${canvasId}-draw-val">${drawRatio}×</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-h2so4`).addEventListener('input', function(e) {
        h2so4Conc = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-h2so4-val`).textContent = h2so4Conc.toFixed(1) + '%';
      });
      document.getElementById(`${canvasId}-znso4`).addEventListener('input', function(e) {
        znso4Conc = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-znso4-val`).textContent = znso4Conc.toFixed(1) + '%';
      });
      document.getElementById(`${canvasId}-draw`).addEventListener('input', function(e) {
        drawRatio = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-draw-val`).textContent = drawRatio.toFixed(1) + '×';
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // Spinneret extrusion and acid regeneration bath
      var bathX = 140, bathY = 80, bathW = 420, bathH = 220;
      ctx.fillStyle = 'rgba(14, 116, 144, 0.15)';
      ctx.fillRect(bathX, bathY, bathW, bathH);
      ctx.strokeStyle = '#06b6d4';
      ctx.lineWidth = 2;
      ctx.strokeRect(bathX, bathY, bathW, bathH);

      // Spinneret Head
      ctx.fillStyle = '#64748b';
      ctx.beginPath();
      ctx.roundRect(60, 140, 70, 100, [6, 0, 0, 6]);
      ctx.fill();
      ctx.strokeStyle = '#94a3b8';
      ctx.stroke();

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 11px sans-serif';
      ctx.fillText('Viscose Dope', 66, 185);
      ctx.font = '9px monospace';
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Na-Cell-Xanthate', 66, 200);

      // Filaments extruded through acid bath
      var numFilaments = 12;
      var tenPerSec = (drawRatio * 2.2 + znso4Conc * 0.8); // Tenacity in cN/dtex
      var skinCoreRatio = Math.min(0.95, 0.35 + znso4Conc * 0.18);

      for (var i = 0; i < numFilaments; i++) {
        var startY = 150 + i * 7;
        var endY = 160 + i * 5;
        var midX = bathX + bathW * 0.6;

        ctx.beginPath();
        ctx.moveTo(130, startY);
        // Bezier trajectory toward godet roll
        ctx.bezierCurveTo(midX, startY, bathX + bathW, endY, 600, 150 + i * 3);

        // Color transition: yellow-orange (xanthate dope) to pure white (regenerated cellulose)
        var grad = ctx.createLinearGradient(130, startY, 600, 150);
        grad.addColorStop(0, '#f59e0b');
        grad.addColorStop(0.35, '#38bdf8');
        grad.addColorStop(1, '#ffffff');

        ctx.strokeStyle = grad;
        ctx.lineWidth = Math.max(1, 3.5 / drawRatio);
        ctx.stroke();
      }

      // Godet Wheels (Stretching and Take-up)
      var g1x = 620, g1y = 150, g1r = 30;
      var g2x = 710, g2y = 130, g2r = 45;

      ctx.save();
      ctx.translate(g1x, g1y);
      ctx.rotate(animOffset * 0.05);
      ctx.beginPath();
      ctx.arc(0, 0, g1r, 0, Math.PI * 2);
      ctx.fillStyle = '#1e293b';
      ctx.fill();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.restore();

      ctx.save();
      ctx.translate(g2x, g2y);
      ctx.rotate(animOffset * 0.05 * drawRatio);
      ctx.beginPath();
      ctx.arc(0, 0, g2r, 0, Math.PI * 2);
      ctx.fillStyle = '#1e293b';
      ctx.fill();
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.restore();

      // Metrics Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Müller Coagulation & Regeneration Kinetics: [Cell-O-CSS⁻Na⁺ + H⁺ → Cell-OH + CS₂↑ + Na⁺]', 65, 342);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Acid Decomposition Rate: ${(h2so4Conc * 1.45).toFixed(1)} mol/m³·s | Zn-Cell-Xanthate Retardation: ${(znso4Conc * 3.2).toFixed(1)} s`, 65, 362);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Filament Tenacity: ${tenPerSec.toFixed(2)} cN/dtex | Elongation at Break: ${(28.0 / drawRatio).toFixed(1)}% | Skin-Core Ratio: ${(skinCoreRatio * 100).toFixed(0)}%`, 65, 382);

      animOffset += 1;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 2. Stamicarbon Urea Synthesis & Stripping Reactor
  // =========================================================================
  window.IndustrialSims.sim_ind_urea_synthesis_autoclave = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var temp = 185; // °C (175 - 200)
    var press = 140; // bar (130 - 160)
    var nh3Ratio = 2.95; // NH3/CO2 molar ratio (2.5 - 3.5)
    var simTime = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Reactor Temp (°C):</strong>
            <input type="range" id="${canvasId}-temp" min="175" max="200" step="1" value="${temp}" style="vertical-align:middle;">
            <span id="${canvasId}-temp-val">${temp} °C</span>
          </label>
          <label><strong>Pressure (bar):</strong>
            <input type="range" id="${canvasId}-press" min="130" max="160" step="1" value="${press}" style="vertical-align:middle;">
            <span id="${canvasId}-press-val">${press} bar</span>
          </label>
          <label><strong>NH₃:CO₂ Ratio:</strong>
            <input type="range" id="${canvasId}-ratio" min="2.5" max="3.5" step="0.05" value="${nh3Ratio}" style="vertical-align:middle;">
            <span id="${canvasId}-ratio-val">${nh3Ratio.toFixed(2)}</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-temp`).addEventListener('input', function(e) {
        temp = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-temp-val`).textContent = temp + ' °C';
      });
      document.getElementById(`${canvasId}-press`).addEventListener('input', function(e) {
        press = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-press-val`).textContent = press + ' bar';
      });
      document.getElementById(`${canvasId}-ratio`).addEventListener('input', function(e) {
        nh3Ratio = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-ratio-val`).textContent = nh3Ratio.toFixed(2);
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // Equilibrium Brunner thermodynamics
      // Reaction 1: 2NH3 + CO2 <=> NH2COONH4 (fast, exothermic, ΔH = -117 kJ/mol)
      // Reaction 2: NH2COONH4 <=> NH2CONH2 + H2O (slow endothermic, ΔH = +15.5 kJ/mol)
      var kEq = Math.exp((temp - 170) * 0.04) * (press / 140) * (nh3Ratio / 3.0);
      var conversionPct = Math.min(78, Math.max(48, 56.0 + (temp - 180) * 0.65 + (nh3Ratio - 2.8) * 14.0 + (press - 140) * 0.25));

      // Draw Autoclave Vessel
      var vx = 80, vy = 60, vw = 160, vh = 240;
      ctx.fillStyle = '#1e293b';
      ctx.beginPath();
      ctx.roundRect(vx, vy, vw, vh, [80, 80, 20, 20]);
      ctx.fill();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.stroke();

      // Liquid Phase Level inside Autoclave
      var liqH = vh * 0.72;
      ctx.fillStyle = 'rgba(56, 189, 248, 0.25)';
      ctx.beginPath();
      ctx.roundRect(vx + 6, vy + vh - liqH, vw - 12, liqH - 6, [0, 0, 16, 16]);
      ctx.fill();

      // Bubbles representing gas dissolution
      for (var b = 0; b < 12; b++) {
        var bx = vx + 25 + (b * 27 + simTime * 2) % (vw - 50);
        var by = vy + vh - 20 - ((b * 35 + simTime * 3) % (liqH - 40));
        ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
        ctx.beginPath();
        ctx.arc(bx, by, 3, 0, Math.PI * 2);
        ctx.fill();
      }

      // Stripper Column
      var sx = 300, sy = 70, sw = 110, sh = 230;
      ctx.fillStyle = '#1e293b';
      ctx.fillRect(sx, sy, sw, sh);
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 2;
      ctx.strokeRect(sx, sy, sw, sh);

      // Packing trays inside stripper
      ctx.strokeStyle = 'rgba(245, 158, 11, 0.4)';
      for (var t = 0; t < 8; t++) {
        ctx.beginPath();
        ctx.moveTo(sx + 10, sy + 30 + t * 24);
        ctx.lineTo(sx + sw - 10, sy + 30 + t * 24);
        ctx.stroke();
      }

      // Connecting pipes
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(vx + vw, vy + vh - 30);
      ctx.lineTo(sx, vy + vh - 30);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(sx + sw / 2, sy);
      ctx.lineTo(sx + sw / 2, vy + 20);
      ctx.lineTo(vx + vw / 2, vy + 20);
      ctx.stroke();

      // Flow labels
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 10px sans-serif';
      ctx.fillText('Autoclave (140 bar)', vx + 22, vy + 45);
      ctx.fillStyle = '#f59e0b';
      ctx.fillText('CO₂ High-P Stripper', sx + 6, sy + 20);

      // Right Chart: Conversion vs Temperature Curve
      var cx = 460, cy = 60, cw = 280, ch = 230;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(cx, cy, cw, ch);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(cx, cy, cw, ch);

      ctx.fillStyle = '#e2e8f0';
      ctx.font = 'bold 11px sans-serif';
      ctx.fillText('CO₂-to-Urea Conversion Equilibrium (%)', cx + 18, cy + 22);

      // Draw T-X curve
      ctx.beginPath();
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.5;
      for (var tPlot = 170; tPlot <= 205; tPlot += 2) {
        var xPlot = 50.0 + (tPlot - 170) * 0.9 - Math.pow(tPlot - 192, 2) * 0.04;
        var px = cx + 30 + ((tPlot - 170) / 35.0) * (cw - 60);
        var py = cy + ch - 30 - ((xPlot - 40) / 45.0) * (ch - 60);
        if (tPlot === 170) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current operating point marker
      var curPx = cx + 30 + ((temp - 170) / 35.0) * (cw - 60);
      var curPy = cy + ch - 30 - ((conversionPct - 40) / 45.0) * (ch - 60);
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(curPx, curPy, 6, 0, Math.PI * 2);
      ctx.fill();

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Stamicarbon CO₂ Stripping Synthesis Loop: 2NH₃ + CO₂ ⇌ NH₂COONH₄ ⇌ NH₂CONH₂ + H₂O', 65, 342);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Net Single-Pass CO₂ Conversion: ${conversionPct.toFixed(1)}% | Unreacted Carbamate Recycle: ${(100 - conversionPct).toFixed(1)}%`, 65, 362);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Biuret Formation Defect: ${(0.35 + (temp > 190 ? (temp - 190) * 0.08 : 0)).toFixed(2)} wt% (Specification < 1.00 wt%)`, 65, 382);

      simTime += 0.5;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 3. Quadruple-Effect Sugar Juice Evaporator Simulator
  // =========================================================================
  window.IndustrialSims.sim_ind_sugar_multiple_effect_evaporator = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var feedBrix = 15; // °Bx initial juice
    var steamPress = 2.4; // bar absolute
    var targetBrix = 65; // °Bx thick juice
    var animT = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Raw Juice Feed (°Bx):</strong>
            <input type="range" id="${canvasId}-feed" min="12" max="18" step="0.5" value="${feedBrix}" style="vertical-align:middle;">
            <span id="${canvasId}-feed-val">${feedBrix} °Bx</span>
          </label>
          <label><strong>Live Steam (bar):</strong>
            <input type="range" id="${canvasId}-steam" min="1.8" max="3.2" step="0.1" value="${steamPress}" style="vertical-align:middle;">
            <span id="${canvasId}-steam-val">${steamPress.toFixed(1)} bar</span>
          </label>
          <label><strong>Target Syup (°Bx):</strong>
            <input type="range" id="${canvasId}-target" min="60" max="70" step="1" value="${targetBrix}" style="vertical-align:middle;">
            <span id="${canvasId}-target-val">${targetBrix} °Bx</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-feed`).addEventListener('input', function(e) {
        feedBrix = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-feed-val`).textContent = feedBrix + ' °Bx';
      });
      document.getElementById(`${canvasId}-steam`).addEventListener('input', function(e) {
        steamPress = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-steam-val`).textContent = steamPress.toFixed(1) + ' bar';
      });
      document.getElementById(`${canvasId}-target`).addEventListener('input', function(e) {
        targetBrix = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-target-val`).textContent = targetBrix + ' °Bx';
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // 4 Evaporator Effects (Robert Calandria bodies)
      var effects = [
        { name: 'Effect I',  t: 124, p: 2.2, bx: feedBrix * 1.35 },
        { name: 'Effect II', t: 110, p: 1.4, bx: feedBrix * 1.85 },
        { name: 'Effect III',t: 94,  p: 0.8, bx: feedBrix * 2.70 },
        { name: 'Effect IV', t: 65,  p: 0.25, bx: targetBrix }
      ];

      var startX = 60, bodyW = 125, bodyH = 200;
      var gap = 45;

      for (var i = 0; i < 4; i++) {
        var ex = startX + i * (bodyW + gap);
        var ey = 80;

        // Calandria Shell
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(ex, ey, bodyW, bodyH, [12, 12, 20, 20]);
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Calandria Heating Basket (lower 40%)
        var basketH = bodyH * 0.42;
        ctx.fillStyle = 'rgba(239, 68, 68, 0.2)';
        ctx.fillRect(ex + 8, ey + bodyH - basketH - 10, bodyW - 16, basketH);
        ctx.strokeStyle = '#ef4444';
        ctx.strokeRect(ex + 8, ey + bodyH - basketH - 10, bodyW - 16, basketH);

        // Vertical Calandria tubes
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 1;
        for (var tube = 0; tube < 5; tube++) {
          var tx = ex + 20 + tube * 18;
          ctx.beginPath();
          ctx.moveTo(tx, ey + bodyH - basketH - 10);
          ctx.lineTo(tx, ey + bodyH - 10);
          ctx.stroke();
        }

        // Boiling Liquid inside
        var brixFraction = (effects[i].bx - 10) / 60.0;
        ctx.fillStyle = `rgba(${Math.floor(180 + brixFraction * 75)}, ${Math.floor(130 - brixFraction * 80)}, 30, 0.45)`;
        ctx.fillRect(ex + 6, ey + bodyH - basketH, bodyW - 12, basketH - 4);

        // Vapor bubbles
        for (var vb = 0; vb < 4; vb++) {
          var vbx = ex + 15 + (vb * 25 + animT) % (bodyW - 30);
          var vby = ey + bodyH - basketH + 10 - ((vb * 15 + animT * 1.5) % 40);
          ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
          ctx.beginPath();
          ctx.arc(vbx, vby, 2.5, 0, Math.PI * 2);
          ctx.fill();
        }

        // Header Text
        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText(effects[i].name, ex + 34, ey + 24);
        ctx.font = '10px monospace';
        ctx.fillStyle = '#38bdf8';
        ctx.fillText(`${effects[i].bx.toFixed(1)} °Bx`, ex + 38, ey + 42);
        ctx.fillStyle = '#f59e0b';
        ctx.fillText(`${effects[i].t}°C (${effects[i].p} bar)`, ex + 20, ey + 58);

        // Vapor duct to next calandria
        if (i < 3) {
          ctx.strokeStyle = '#64748b';
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.moveTo(ex + bodyW / 2, ey);
          ctx.lineTo(ex + bodyW / 2, ey - 20);
          ctx.lineTo(ex + bodyW + gap + 15, ey - 20);
          ctx.lineTo(ex + bodyW + gap + 15, ey + bodyH - basketH / 2);
          ctx.stroke();
        }
      }

      // Barometric Condenser on Effect 4
      ctx.strokeStyle = '#06b6d4';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(startX + 3 * (bodyW + gap) + bodyW / 2, 80);
      ctx.lineTo(startX + 3 * (bodyW + gap) + bodyW / 2, 45);
      ctx.lineTo(720, 45);
      ctx.stroke();

      ctx.fillStyle = '#0891b2';
      ctx.beginPath();
      ctx.arc(720, 45, 12, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = '9px sans-serif';
      ctx.fillText('Vac', 712, 48);

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      var waterEvapKg = (1000 * (1 - feedBrix / targetBrix)).toFixed(0);
      var steamEconomy = (3.45 + (steamPress - 2.0) * 0.2).toFixed(2);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Multiple-Effect Evaporator Material & Energy Balances (Rillieux Principles)', 65, 342);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Water Evaporated per 1000 kg Clarified Juice: ${waterEvapKg} kg | Global Steam Economy: ${steamEconomy} kg water / kg live steam`, 65, 362);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Thick Juice Outlet Brix: ${targetBrix.toFixed(1)} °Bx | Total Boiling Point Elevation (BPE): 5.8 °C across train`, 65, 382);

      animT = (animT + 1) % 100;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 4. Cement Rotary Kiln Thermochemical Reaction Profile
  // =========================================================================
  window.IndustrialSims.sim_ind_cement_rotary_kiln_profile = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var burningZoneTemp = 1450; // °C (1350 - 1550)
    var kilnTilt = 3.5; // percent slope
    var rawLsRatio = 0.96; // Lime Saturation Factor (LSF)
    var animPhase = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Burning Temp (°C):</strong>
            <input type="range" id="${canvasId}-temp" min="1350" max="1550" step="10" value="${burningZoneTemp}" style="vertical-align:middle;">
            <span id="${canvasId}-temp-val">${burningZoneTemp} °C</span>
          </label>
          <label><strong>Lime Saturation (LSF):</strong>
            <input type="range" id="${canvasId}-lsf" min="0.88" max="1.02" step="0.01" value="${rawLsRatio}" style="vertical-align:middle;">
            <span id="${canvasId}-lsf-val">${rawLsRatio.toFixed(2)}</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-temp`).addEventListener('input', function(e) {
        burningZoneTemp = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-temp-val`).textContent = burningZoneTemp + ' °C';
      });
      document.getElementById(`${canvasId}-lsf`).addEventListener('input', function(e) {
        rawLsRatio = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-lsf-val`).textContent = rawLsRatio.toFixed(2);
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // Rotary Kiln Geometry (Tilted Cylinder)
      var kx = 80, ky = 70, kw = 640, kh = 90;
      var tiltOffset = 20;

      // Kiln Body
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(kx, ky);
      ctx.lineTo(kx + kw, ky + tiltOffset);
      ctx.lineTo(kx + kw, ky + kh + tiltOffset);
      ctx.lineTo(kx, ky + kh);
      ctx.closePath();

      // Kiln Interior Heat Gradient
      var kGrad = ctx.createLinearGradient(kx, 0, kx + kw, 0);
      kGrad.addColorStop(0, '#334155');   // Preheating (200-800°C)
      kGrad.addColorStop(0.35, '#b45309'); // Calcination (900°C)
      kGrad.addColorStop(0.75, '#ea580c'); // Transition (1250°C)
      kGrad.addColorStop(1.0, '#f97316');  // Sintering/Clinkering (1450°C)

      ctx.fillStyle = kGrad;
      ctx.fill();
      ctx.strokeStyle = '#cbd5e1';
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.restore();

      // Burning Flame Lance from Right end
      ctx.fillStyle = '#fef08a';
      ctx.beginPath();
      ctx.moveTo(kx + kw + 10, ky + kh / 2 + tiltOffset);
      ctx.lineTo(kx + kw - 140, ky + kh / 2 + tiltOffset - 12);
      ctx.lineTo(kx + kw - 180 + Math.sin(animPhase) * 15, ky + kh / 2 + tiltOffset);
      ctx.lineTo(kx + kw - 140, ky + kh / 2 + tiltOffset + 12);
      ctx.closePath();
      ctx.fill();

      // Rolling Clinker Nodules
      for (var n = 0; n < 18; n++) {
        var nx = kx + 40 + (n * 35 + animPhase * 2) % (kw - 60);
        var ny = ky + kh - 15 + (nx - kx) * (tiltOffset / kw);
        ctx.fillStyle = nx > (kx + kw * 0.7) ? '#475569' : '#e2e8f0';
        ctx.beginPath();
        ctx.arc(nx, ny, 4.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // Zone Labels
      ctx.font = 'bold 10px sans-serif';
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('1. Dehydration (100-500°C)', kx + 10, ky - 10);
      ctx.fillText('2. Calcining (800-950°C)', kx + 180, ky - 10);
      ctx.fillText('3. Solid Belite (1200°C)', kx + 360, ky - 10);
      ctx.fillText('4. Sintering Alite (1450°C)', kx + 510, ky - 10);

      // Temperature Profile Curve Plot
      var py0 = 200, pw = kw, ph = 100;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(kx, py0, pw, ph);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(kx, py0, pw, ph);

      ctx.beginPath();
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 2.5;
      for (var step = 0; step <= 50; step++) {
        var frac = step / 50.0;
        var tempAtFrac = 250 + Math.pow(frac, 1.8) * (burningZoneTemp - 250);
        var ptX = kx + frac * pw;
        var ptY = py0 + ph - ((tempAtFrac - 200) / 1400.0) * (ph - 15);
        if (step === 0) ctx.moveTo(ptX, ptY);
        else ctx.lineTo(ptX, ptY);
      }
      ctx.stroke();

      ctx.fillStyle = '#ef4444';
      ctx.font = '10px monospace';
      ctx.fillText(`Flame Peak: ${burningZoneTemp}°C`, kx + pw - 130, py0 + 20);

      // Bogue Calculations
      var c3s = Math.max(35, Math.min(68, 55 + (rawLsRatio - 0.95) * 110 + (burningZoneTemp - 1450) * 0.05));
      var c2s = Math.max(10, Math.min(38, 20 - (rawLsRatio - 0.95) * 90));
      var c3a = 9.2;
      var c4af = 8.5;

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Portland Cement Clinker Phase Systematics (Bogue Formulations):', 65, 342);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Alite (C₃S, 3CaO·SiO₂): ${c3s.toFixed(1)}% | Belite (C₂S, 2CaO·SiO₂): ${c2s.toFixed(1)}% | Celite (C₃A): ${c3a}% | Ferrite (C₄AF): ${c4af}%`, 65, 362);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Free Lime (CaO uncombined): ${(rawLsRatio > 0.98 ? 1.8 : 0.7).toFixed(1)}% | ASTM C150 Type I Early Strength Potential: ${(c3s * 0.72).toFixed(1)} MPa at 28d`, 65, 382);

      animPhase += 0.08;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 5. Triglyceride Saponification & Phase Separation Engine
  // =========================================================================
  window.IndustrialSims.sim_ind_soap_saponification_reactor = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var saltPct = 8.0; // wt% NaCl brine for graining out
    var waterPct = 30.0; // wt% H2O
    var tempC = 95; // °C
    var animT = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Graining Salt (NaCl %):</strong>
            <input type="range" id="${canvasId}-salt" min="2" max="15" step="0.5" value="${saltPct}" style="vertical-align:middle;">
            <span id="${canvasId}-salt-val">${saltPct}%</span>
          </label>
          <label><strong>Water in Kettle (%):</strong>
            <input type="range" id="${canvasId}-water" min="20" max="45" step="1" value="${waterPct}" style="vertical-align:middle;">
            <span id="${canvasId}-water-val">${waterPct}%</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-salt`).addEventListener('input', function(e) {
        saltPct = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-salt-val`).textContent = saltPct.toFixed(1) + '%';
      });
      document.getElementById(`${canvasId}-water`).addEventListener('input', function(e) {
        waterPct = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-water-val`).textContent = waterPct + '%';
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // Saponification Kettle (Cross Section)
      var kx = 100, ky = 60, kw = 240, kh = 240;
      ctx.fillStyle = '#1e293b';
      ctx.beginPath();
      ctx.roundRect(kx, ky, kw, kh, [20, 20, 100, 100]);
      ctx.fill();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.stroke();

      // McBain Ternary Phase Equilibria
      // Neat Soap (Curd) separates on top if saltPct > 6.5%
      var isGrainedOut = saltPct >= 6.5;
      var neatH = isGrainedOut ? kh * 0.55 : kh * 0.85;

      // Top Layer: Neat Soap / Curd
      ctx.fillStyle = isGrainedOut ? '#fef08a' : '#f59e0b';
      ctx.beginPath();
      ctx.roundRect(kx + 8, ky + 10, kw - 16, neatH, [12, 12, 0, 0]);
      ctx.fill();

      // Bottom Layer: Spent Lye / Nigre (Glycerol + Salt + Impurities)
      if (isGrainedOut) {
        ctx.fillStyle = 'rgba(56, 189, 248, 0.45)';
        ctx.beginPath();
        ctx.roundRect(kx + 8, ky + neatH + 10, kw - 16, kh - neatH - 20, [0, 0, 90, 90]);
        ctx.fill();

        ctx.fillStyle = '#0284c7';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Spent Lye (Glycerol + NaCl)', kx + 35, ky + neatH + 45);
      }

      ctx.fillStyle = '#1e293b';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText(isGrainedOut ? 'Curd / Neat Soap (~66% TFM)' : 'Single Homogeneous Middle Soap', kx + 20, ky + neatH / 2);

      // Steam Sparger Coil at bottom
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.arc(kx + kw / 2, ky + kh - 35, 35, Math.PI * 0.2, Math.PI * 0.8);
      ctx.stroke();

      // Ternary Phase Triangle on the Right
      var tx = 430, ty = 60, tSize = 240;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(tx, ty, tSize + 60, tSize + 10);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(tx, ty, tSize + 60, tSize + 10);

      // Draw McBain Triangle (Soap - Water - Electrolyte)
      var pTop = { x: tx + tSize / 2 + 30, y: ty + 30 };
      var pLeft = { x: tx + 30, y: ty + tSize };
      var pRight = { x: tx + tSize + 30, y: ty + tSize };

      ctx.beginPath();
      ctx.moveTo(pTop.x, pTop.y);
      ctx.lineTo(pLeft.x, pLeft.y);
      ctx.lineTo(pRight.x, pRight.y);
      ctx.closePath();
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 10px sans-serif';
      ctx.fillText('Soap (Na-Carboxylate)', pTop.x - 55, pTop.y - 10);
      ctx.fillText('Water (H₂O)', pLeft.x - 20, pLeft.y + 16);
      ctx.fillText('NaCl Brine', pRight.x - 10, pRight.y + 16);

      // Operating composition point in triangle
      var compX = pLeft.x + (saltPct / 20.0) * (pRight.x - pLeft.x) + 40;
      var compY = pLeft.y - ((100 - waterPct - saltPct) / 100.0) * (pLeft.y - pTop.y);
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(compX, compY, 6, 0, Math.PI * 2);
      ctx.fill();

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Continuous Kettle Saponification: (RCOO)₃C₃H₅ + 3NaOH → 3RCOONa + C₃H₅(OH)₃', 65, 342);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Graining Phase State: ${isGrainedOut ? 'Two-Phase (Neat Soap + Spent Lye)' : 'Single Phase (Isotropic Solution)'} | Glycerol Recovery: ${(isGrainedOut ? 94.5 : 42.0).toFixed(1)}%`, 65, 362);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Total Fatty Matter (TFM): ${(isGrainedOut ? 68.2 : 45.0).toFixed(1)}% | Salt in Neat Soap: ${(saltPct * 0.08).toFixed(2)} wt% (Grade 1 Standard < 0.8%)`, 65, 382);

      animT += 1;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 6. Kraft Pulping & Tomlinson Recovery Boiler Cycle
  // =========================================================================
  window.IndustrialSims.sim_ind_kraft_recovery_boiler_cycle = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var sulfidity = 28; // % sulfidity (20 - 40)
    var activeAlkali = 16; // % AA on wood
    var kappaTarget = 24; // Bleachable grade
    var simT = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Sulfidity (% Na₂S):</strong>
            <input type="range" id="${canvasId}-sulf" min="20" max="40" step="1" value="${sulfidity}" style="vertical-align:middle;">
            <span id="${canvasId}-sulf-val">${sulfidity}%</span>
          </label>
          <label><strong>Active Alkali (% AA):</strong>
            <input type="range" id="${canvasId}-aa" min="13" max="22" step="0.5" value="${activeAlkali}" style="vertical-align:middle;">
            <span id="${canvasId}-aa-val">${activeAlkali}%</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-sulf`).addEventListener('input', function(e) {
        sulfidity = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-sulf-val`).textContent = sulfidity + '%';
      });
      document.getElementById(`${canvasId}-aa`).addEventListener('input', function(e) {
        activeAlkali = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-aa-val`).textContent = activeAlkali.toFixed(1) + '%';
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // Cycle Node Positions
      var nodes = [
        { name: 'Continuous Digester', x: 120, y: 110, col: '#38bdf8' },
        { name: 'Evaporators (Heavy BL)', x: 340, y: 80, col: '#f59e0b' },
        { name: 'Tomlinson Boiler', x: 580, y: 110, col: '#ef4444' },
        { name: 'Smelt Dissolver', x: 580, y: 240, col: '#10b981' },
        { name: 'Causticizing / Slaker', x: 340, y: 260, col: '#a855f7' },
        { name: 'White Liquor Storage', x: 120, y: 240, col: '#06b6d4' }
      ];

      // Connecting flow cycle loops
      ctx.lineWidth = 3;
      for (var i = 0; i < nodes.length; i++) {
        var n1 = nodes[i];
        var n2 = nodes[(i + 1) % nodes.length];

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        ctx.beginPath();
        ctx.moveTo(n1.x, n1.y);
        ctx.lineTo(n2.x, n2.y);
        ctx.stroke();

        // Pulsing flow particle
        var pFrac = (simT * 0.015 + i * 0.16) % 1.0;
        var px = n1.x + (n2.x - n1.x) * pFrac;
        var py = n1.y + (n2.y - n1.y) * pFrac;
        ctx.fillStyle = n1.col;
        ctx.beginPath();
        ctx.arc(px, py, 4, 0, Math.PI * 2);
        ctx.fill();
      }

      // Draw Node Cards
      nodes.forEach(function(node) {
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(node.x - 70, node.y - 25, 140, 50, 8);
        ctx.fill();
        ctx.strokeStyle = node.col;
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 10px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(node.name, node.x, node.y + 4);
      });
      ctx.textAlign = 'left';

      // Computed Chemistry Parameters
      var pulpYield = (52.0 - activeAlkali * 0.5 + sulfidity * 0.12).toFixed(1);
      var kappaNum = Math.max(16, (38.0 - activeAlkali * 0.95 - sulfidity * 0.2)).toFixed(1);
      var reductionEfficiency = (91.5 + sulfidity * 0.15).toFixed(1);

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Kraft Chemical Recovery Loop: Na₂SO₄ + 2C → Na₂S + 2CO₂ | Na₂CO₃ + Ca(OH)₂ → 2NaOH + CaCO₃', 65, 342);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Screened Pulp Yield: ${pulpYield}% | Brownstock Kappa Number: ${kappaNum} (Residual Lignin ~ ${(kappaNum * 0.15).toFixed(1)}%)`, 65, 362);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Recovery Boiler Smelt Reduction Efficiency: ${reductionEfficiency}% | White Liquor Causticizing Ratio: 82.5%`, 65, 382);

      simT += 1;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 7. Pilkington Float Glass Bath & Annealing Lehr Visualizer
  // =========================================================================
  window.IndustrialSims.sim_ind_glass_float_annealing_lehr = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var drawSpeed = 4.0; // m/min
    var lehrCoolRate = 12.0; // °C/min
    var animX = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Ribbon Speed (m/min):</strong>
            <input type="range" id="${canvasId}-speed" min="1" max="10" step="0.5" value="${drawSpeed}" style="vertical-align:middle;">
            <span id="${canvasId}-speed-val">${drawSpeed} m/min</span>
          </label>
          <label><strong>Lehr Cooling Rate (°C/min):</strong>
            <input type="range" id="${canvasId}-cool" min="5" max="25" step="1" value="${lehrCoolRate}" style="vertical-align:middle;">
            <span id="${canvasId}-cool-val">${lehrCoolRate} °C/min</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-speed`).addEventListener('input', function(e) {
        drawSpeed = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-speed-val`).textContent = drawSpeed.toFixed(1) + ' m/min';
      });
      document.getElementById(`${canvasId}-cool`).addEventListener('input', function(e) {
        lehrCoolRate = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-cool-val`).textContent = lehrCoolRate + ' °C/min';
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // Float Bath (Liquid Tin)
      var bx = 60, by = 90, bw = 320, bh = 140;
      ctx.fillStyle = '#334155';
      ctx.fillRect(bx, by, bw, bh);
      ctx.strokeStyle = '#06b6d4';
      ctx.lineWidth = 2;
      ctx.strokeRect(bx, by, bw, bh);

      // Liquid Tin Bath surface
      ctx.fillStyle = 'rgba(203, 213, 225, 0.35)';
      ctx.fillRect(bx + 5, by + bh - 50, bw - 10, 45);
      ctx.fillStyle = '#94a3b8';
      ctx.font = 'bold 10px sans-serif';
      ctx.fillText('Molten Tin Bath (1000°C → 600°C in N₂/H₂ Atm)', bx + 15, by + bh - 20);

      // Glass Ribbon spreading across tin
      var ribbonThickness = Math.max(1.8, Math.min(19.0, 6.8 / Math.sqrt(drawSpeed / 4.0)));
      var rx = bx + 10, ry = by + bh - 50 - ribbonThickness;
      var rw = bw - 15;

      var rGrad = ctx.createLinearGradient(rx, 0, rx + rw, 0);
      rGrad.addColorStop(0, '#f97316'); // 1050°C red glowing glass
      rGrad.addColorStop(0.6, '#fde047'); // 800°C
      rGrad.addColorStop(1, '#38bdf8');   // 600°C rigid ribbon

      ctx.fillStyle = rGrad;
      ctx.fillRect(rx, ry, rw, ribbonThickness);

      // Top knurled edge rolls
      for (var kr = 0; kr < 4; kr++) {
        var kx = bx + 40 + kr * 65;
        ctx.fillStyle = '#475569';
        ctx.beginPath();
        ctx.arc(kx, ry - 6, 8, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#94a3b8';
        ctx.stroke();
      }

      // Annealing Lehr (Cooling Tunnel)
      var lx = 410, ly = 90, lw = 310, lh = 140;
      ctx.fillStyle = '#1e293b';
      ctx.fillRect(lx, ly, lw, lh);
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2;
      ctx.strokeRect(lx, ly, lw, lh);

      // Roller Hearth
      for (var roll = 0; roll < 8; roll++) {
        var rlx = lx + 15 + roll * 38;
        ctx.fillStyle = '#64748b';
        ctx.beginPath();
        ctx.arc(rlx, ly + lh - 40, 7, 0, Math.PI * 2);
        ctx.fill();
      }

      // Cold Glass Sheet emerging
      ctx.fillStyle = 'rgba(56, 189, 248, 0.7)';
      ctx.fillRect(lx, ly + lh - 40 - ribbonThickness, lw, ribbonThickness);

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 10px sans-serif';
      ctx.fillText('Controlled Annealing Lehr (600°C → 50°C)', lx + 20, ly + 25);

      // Residual Stress calculation
      var stressMpa = (lehrCoolRate * 0.45 * (ribbonThickness / 6.0)).toFixed(1);

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Pilkington Float Equilibrium & Adams-Williamson Annealing Physics:', 65, 342);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Equilibrium Ribbon Thickness: ${ribbonThickness.toFixed(2)} mm (Natural Tin Surface Equilibrium = 6.8 mm)`, 65, 362);
      ctx.fillStyle = stressMpa < 5.0 ? '#10b981' : '#f59e0b';
      ctx.fillText(`Residual Permanent Birefringent Stress: ${stressMpa} MPa (Automotive/Architectural Standard < 5.0 MPa)`, 65, 382);

      animX += 1;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 8. Nafion Membrane Chlor-Alkali Cell Dynamics
  // =========================================================================
  window.IndustrialSims.sim_ind_chlor_alkali_membrane_cell = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var currentDensity = 4.0; // kA/m^2 (2.5 - 6.0)
    var brineTemp = 88; // °C
    var animT = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Current Density (kA/m²):</strong>
            <input type="range" id="${canvasId}-cd" min="2.5" max="6.0" step="0.2" value="${currentDensity}" style="vertical-align:middle;">
            <span id="${canvasId}-cd-val">${currentDensity.toFixed(1)} kA/m²</span>
          </label>
          <label><strong>Brine Temp (°C):</strong>
            <input type="range" id="${canvasId}-temp" min="75" max="95" step="1" value="${brineTemp}" style="vertical-align:middle;">
            <span id="${canvasId}-temp-val">${brineTemp} °C</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-cd`).addEventListener('input', function(e) {
        currentDensity = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-cd-val`).textContent = currentDensity.toFixed(1) + ' kA/m²';
      });
      document.getElementById(`${canvasId}-temp`).addEventListener('input', function(e) {
        brineTemp = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-temp-val`).textContent = brineTemp + ' °C';
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // Membrane Cell Compartments
      var cx = 160, cy = 60, cw = 480, ch = 240;
      var midX = cx + cw / 2;

      // Anode Chamber (Left, Anolyte: Purified Saturated NaCl Brine)
      ctx.fillStyle = 'rgba(234, 179, 8, 0.15)';
      ctx.fillRect(cx, cy, cw / 2, ch);

      // Cathode Chamber (Right, Catholyte: 32% NaOH solution)
      ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
      ctx.fillRect(midX, cy, cw / 2, ch);

      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 2;
      ctx.strokeRect(cx, cy, cw, ch);

      // Perfluorosulfonate Nafion Membrane Divider
      ctx.strokeStyle = '#a855f7';
      ctx.lineWidth = 6;
      ctx.beginPath();
      ctx.moveTo(midX, cy);
      ctx.lineTo(midX, cy + ch);
      ctx.stroke();

      // Anode Electrode (DSA RuO2/TiO2 coated titanium)
      ctx.fillStyle = '#ef4444';
      ctx.fillRect(cx + 20, cy + 20, 15, ch - 40);

      // Cathode Electrode (Nickel mesh / Ru-coated)
      ctx.fillStyle = '#10b981';
      ctx.fillRect(cx + cw - 35, cy + 20, 15, ch - 40);

      // Chlorine Gas Bubbles rising at Anode
      ctx.fillStyle = 'rgba(250, 204, 21, 0.8)';
      for (var cb = 0; cb < 10; cb++) {
        var cbx = cx + 45 + (cb * 12) % 60;
        var cby = cy + ch - 30 - ((cb * 22 + animT * 3) % (ch - 60));
        ctx.beginPath();
        ctx.arc(cbx, cby, 3.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // Hydrogen Gas Bubbles rising at Cathode
      ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
      for (var hb = 0; hb < 14; hb++) {
        var hbx = cx + cw - 55 - (hb * 10) % 60;
        var hby = cy + ch - 30 - ((hb * 20 + animT * 4) % (ch - 60));
        ctx.beginPath();
        ctx.arc(hbx, hby, 2.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // Sodium Ions (Na+) crossing the membrane
      ctx.fillStyle = '#a855f7';
      for (var na = 0; na < 6; na++) {
        var nax = midX - 40 + ((na * 35 + animT * 2) % 80);
        var nay = cy + 40 + na * 30;
        ctx.beginPath();
        ctx.arc(nax, nay, 4, 0, Math.PI * 2);
        ctx.fill();
      }

      // Labels
      ctx.fillStyle = '#ef4444';
      ctx.font = 'bold 11px sans-serif';
      ctx.fillText('DSA® Anode (+)', cx + 15, cy - 10);
      ctx.fillStyle = '#eab308';
      ctx.fillText('2Cl⁻ → Cl₂↑ + 2e⁻', cx + 15, cy + 15);

      ctx.fillStyle = '#10b981';
      ctx.fillText('Ni Cathode (-)', cx + cw - 85, cy - 10);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('2H₂O + 2e⁻ → H₂↑ + 2OH⁻', cx + cw - 145, cy + 15);

      ctx.fillStyle = '#a855f7';
      ctx.fillText('Cation-Permeable Membrane (Na⁺ Migration)', midX - 95, cy + ch + 18);

      // Calculations
      var cellVoltage = (2.20 + currentDensity * 0.21 - (brineTemp - 80) * 0.005).toFixed(2);
      var specEnergyKwh = (cellVoltage * 755.0 / 0.96).toFixed(0);

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Electrolytic Chlor-Alkali Stoichiometry: 2NaCl + 2H₂O → 2NaOH + Cl₂ + H₂', 65, 342);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Operating Terminal Cell Voltage: ${cellVoltage} V | Specific DC Energy Consumption: ${specEnergyKwh} kWh / ton NaOH`, 65, 362);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Faradaic Current Efficiency: 96.5% | Product Caustic Purity: 32.5 wt% NaOH with < 20 ppm NaCl`, 65, 382);

      animT += 1;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 9. Fluid Catalytic Cracking (FCC) Riser-Regenerator Engine
  // =========================================================================
  window.IndustrialSims.sim_ind_fcc_riser_regenerator = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var riserTemp = 530; // °C (500 - 560)
    var catToOil = 6.5; // C/O mass ratio (4.0 - 9.0)
    var animT = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Riser Temp (°C):</strong>
            <input type="range" id="${canvasId}-temp" min="500" max="560" step="2" value="${riserTemp}" style="vertical-align:middle;">
            <span id="${canvasId}-temp-val">${riserTemp} °C</span>
          </label>
          <label><strong>Cat/Oil Ratio:</strong>
            <input type="range" id="${canvasId}-co" min="4.0" max="9.0" step="0.2" value="${catToOil}" style="vertical-align:middle;">
            <span id="${canvasId}-co-val">${catToOil.toFixed(1)}</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-temp`).addEventListener('input', function(e) {
        riserTemp = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-temp-val`).textContent = riserTemp + ' °C';
      });
      document.getElementById(`${canvasId}-co`).addEventListener('input', function(e) {
        catToOil = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-co-val`).textContent = catToOil.toFixed(1);
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // Regenerator Vessel (Right, 700°C catalyst coke burnoff)
      var regX = 460, regY = 70, regW = 160, regH = 210;
      ctx.fillStyle = '#1e293b';
      ctx.beginPath();
      ctx.roundRect(regX, regY, regW, regH, [40, 40, 40, 40]);
      ctx.fill();
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 3;
      ctx.stroke();

      // Fluidized Catalyst Bed in Regenerator
      ctx.fillStyle = 'rgba(239, 68, 68, 0.35)';
      ctx.fillRect(regX + 8, regY + regH - 120, regW - 16, 110);
      ctx.fillStyle = '#f87171';
      ctx.font = 'bold 11px sans-serif';
      ctx.fillText('Regenerator (700°C)', regX + 22, regY + 30);
      ctx.font = '9px monospace';
      ctx.fillText('Coke Burn: C + O₂ → CO₂', regX + 16, regY + 48);

      // Reactor Disengager & Riser Tube (Left)
      var disX = 140, disY = 60, disW = 140, disH = 120;
      ctx.fillStyle = '#1e293b';
      ctx.beginPath();
      ctx.roundRect(disX, disY, disW, disH, [30, 30, 20, 20]);
      ctx.fill();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 11px sans-serif';
      ctx.fillText('Disengager / Cyclone', disX + 12, disY + 25);

      // Vertical Riser Tube
      var risX = disX + 45, risY = disY + disH, risW = 50, risH = 120;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(risX, risY, risW, risH);
      ctx.strokeStyle = '#38bdf8';
      ctx.strokeRect(risX, risY, risW, risH);

      // Moving Zeolite Catalyst Particles up the Riser
      for (var p = 0; p < 15; p++) {
        var px = risX + 8 + (p * 9) % 34;
        var py = risY + risH - ((p * 18 + animT * 4) % risH);
        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(px, py, 3, 0, Math.PI * 2);
        ctx.fill();
      }

      // Transfer lines between Riser and Regenerator
      // Spent cat line (Reactor -> Regen)
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(disX + disW - 20, disY + disH);
      ctx.lineTo(regX, regY + regH - 60);
      ctx.stroke();

      // Regenerated cat line (Regen -> Riser bottom)
      ctx.beginPath();
      ctx.moveTo(regX + 30, regY + regH);
      ctx.lineTo(risX + risW / 2, risY + risH);
      ctx.stroke();

      // Product Yield Calculations
      var conversion = Math.min(84, Math.max(62, 60.0 + (riserTemp - 510) * 0.25 + (catToOil - 5.0) * 2.8));
      var gasolineYield = (conversion * 0.62).toFixed(1);
      var lpgYield = (conversion * 0.26).toFixed(1);
      var cokeYield = (4.2 + (catToOil - 5.0) * 0.4).toFixed(1);

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Zeolite Y Catalytic Cracking Carbenium Ion Kinetics: VGO Gas Oil Feed', 65, 342);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Total Feed Conversion: ${conversion.toFixed(1)}% | Gasoline Fraction (C₅-C₁₂): ${gasolineYield} wt% (RON ~ 92.5)`, 65, 362);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`LPG Olefins (Propylene/Butylene): ${lpgYield} wt% | Coke on Spent Catalyst: ${cokeYield} wt% (Heat-balanced)`, 65, 382);

      animT += 1;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 10. Blast Furnace Ironmaking Countercurrent Reactor
  // =========================================================================
  window.IndustrialSims.sim_ind_blast_furnace_ironmaking = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var blastTemp = 1150; // °C (1000 - 1250)
    var pciRate = 160; // kg/ton hot metal
    var animT = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Hot Blast Temp (°C):</strong>
            <input type="range" id="${canvasId}-blast" min="1000" max="1250" step="10" value="${blastTemp}" style="vertical-align:middle;">
            <span id="${canvasId}-blast-val">${blastTemp} °C</span>
          </label>
          <label><strong>PCI Injection (kg/tHM):</strong>
            <input type="range" id="${canvasId}-pci" min="100" max="220" step="5" value="${pciRate}" style="vertical-align:middle;">
            <span id="${canvasId}-pci-val">${pciRate} kg/tHM</span>
          </label>
        </div>
      `;

      document.getElementById(`${canvasId}-blast`).addEventListener('input', function(e) {
        blastTemp = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-blast-val`).textContent = blastTemp + ' °C';
      });
      document.getElementById(`${canvasId}-pci`).addEventListener('input', function(e) {
        pciRate = parseFloat(e.target.value);
        document.getElementById(`${canvasId}-pci-val`).textContent = pciRate + ' kg/tHM';
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 25);

      // Blast Furnace Silhouette (Bosh, Belly, Stack, Throat)
      var cx = W / 2;
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(cx - 45, 60);  // Top throat
      ctx.lineTo(cx + 45, 60);
      ctx.lineTo(cx + 90, 160); // Belly
      ctx.lineTo(cx + 70, 240); // Bosh / Tuyeres
      ctx.lineTo(cx + 65, 290); // Hearth
      ctx.lineTo(cx - 65, 290);
      ctx.lineTo(cx - 70, 240);
      ctx.lineTo(cx - 90, 160);
      ctx.closePath();

      // Furnace Interior Heat Zones
      var fGrad = ctx.createLinearGradient(0, 60, 0, 290);
      fGrad.addColorStop(0, '#475569');   // 400°C Top gas / Indirect reduction (Fe2O3 -> Fe3O4)
      fGrad.addColorStop(0.4, '#ea580c'); // 900°C Wustite (FeO) reduction
      fGrad.addColorStop(0.75, '#f97316'); // 1400°C Cohesive zone
      fGrad.addColorStop(1.0, '#facc15');  // 2000°C Raceways & Tuyeres

      ctx.fillStyle = fGrad;
      ctx.fill();
      ctx.strokeStyle = '#cbd5e1';
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.restore();

      // Burden layers descending (Iron ore pellets & coke)
      for (var l = 0; l < 8; l++) {
        var ly = 80 + l * 25 + (animT * 0.4) % 25;
        if (ly < 260) {
          var halfW = 45 + (ly - 60) * 0.35;
          ctx.strokeStyle = (l % 2 === 0) ? '#94a3b8' : '#334155';
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.moveTo(cx - halfW + 10, ly);
          ctx.lineTo(cx + halfW - 10, ly);
          ctx.stroke();
        }
      }

      // Hot Blast Tuyeres (Air + PCI blowpipes)
      ctx.fillStyle = '#ef4444';
      ctx.fillRect(cx - 95, 240, 25, 12);
      ctx.fillRect(cx + 70, 240, 25, 12);

      // Liquid Pig Iron Taphole
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(cx - 65, 285, 6, 0, Math.PI * 2);
      ctx.fill();

      // Zone Descriptions (Left & Right callouts)
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '10px sans-serif';
      ctx.fillText('Stack: 3Fe₂O₃ + CO → 2Fe₃O₄ + CO₂ (400-700°C)', 45, 110);
      ctx.fillText('Belly: Fe₃O₄ + CO → 3FeO + CO₂ (700-900°C)', 45, 160);
      ctx.fillText('Bosh: FeO + CO → Fe + CO₂ & Boudouard (C + CO₂ → 2CO)', 45, 210);

      ctx.fillStyle = '#facc15';
      ctx.fillText(`Tuyere Flame: ${(1950 + (blastTemp - 1100) * 1.2).toFixed(0)}°C`, cx + 85, 248);

      // Calculations
      var cokeRate = (480 - pciRate * 0.85 - (blastTemp - 1100) * 0.15).toFixed(0);
      var coRatio = (1.35 + pciRate * 0.002).toFixed(2);

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(50, 320, 700, 85);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(50, 320, 700, 85);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Blast Furnace Thermochemistry & Countercurrent Burden Reduction:', 65, 342);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`Metallurgical Coke Rate: ${cokeRate} kg/tHM | Coal Replacement Ratio: 0.85 kg coke / kg PCI`, 65, 362);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Hot Metal Composition: 94.2% Fe, 4.3% C, 0.6% Si, 0.4% Mn, 0.04% S | Basicity (CaO/SiO₂): 1.18`, 65, 382);

      animT += 1;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // window.SimulationEngine Mount Adapter
  // =========================================================================
  var SIM_TITLES = {
    sim_ind_textile_viscose_spinning: "Viscose Rayon Acid Coagulation & Filament Draw Simulator",
    sim_ind_urea_synthesis_autoclave: "Stamicarbon Urea Synthesis & Stripping Reactor",
    sim_ind_sugar_multiple_effect_evaporator: "Quadruple-Effect Sugar Juice Evaporator Simulator",
    sim_ind_cement_rotary_kiln_profile: "Cement Rotary Kiln Thermochemical Reaction Profile",
    sim_ind_soap_saponification_reactor: "Triglyceride Saponification & Phase Separation Engine",
    sim_ind_kraft_recovery_boiler_cycle: "Kraft Pulping & Tomlinson Recovery Boiler Cycle",
    sim_ind_glass_float_annealing_lehr: "Pilkington Float Glass Bath & Annealing Lehr Visualizer",
    sim_ind_chlor_alkali_membrane_cell: "Nafion Membrane Chlor-Alkali Cell Dynamics",
    sim_ind_fcc_riser_regenerator: "Fluid Catalytic Cracking (FCC) Riser-Regenerator Engine",
    sim_ind_blast_furnace_ironmaking: "Blast Furnace Ironmaking Countercurrent Reactor"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.IndustrialSims || typeof window.IndustrialSims[simType] !== 'function') {
      console.warn('Simulation type not found in IndustrialSims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Industrial Chemistry Interactive Simulation";
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
      window.IndustrialSims[simType](canvasId, controlsId);
    }, 50);
  };

})();
