#!/usr/bin/env python3
"""
generate_kinetics_sims.py
Generates molecular-motion-kinetics-sims.js containing 10 interactive 60 FPS Canvas simulation engines.
"""

def generate_sims_js():
    code = """// Molecular Motion & Reaction Kinetics Interactive Simulation Suite
// 10 Real-Time 60 FPS Canvas Simulation Engines for OpenSTEM Master Digital Textbook #49
// Mounted via window.SimulationEngine.initSimulation(containerId, simType)

(function() {
  'use strict';

  window.KineticsSims = window.KineticsSims || {};

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
  // 1. Maxwell-Boltzmann Speed Distribution & Knudsen Effusion Simulator
  // =========================================================================
  window.KineticsSims.sim_kin_maxwell_boltzmann_effusion = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var tempK = 300;     // Temperature (K)
    var molarMass = 28;  // g/mol (N2 = 28, He = 4, Ar = 40, Xe = 131)
    var R = 8.314;       // J/(mol K)
    var animOffset = 0;

    // Effusion particle pool
    var particles = [];
    var chamberW = 320;
    var chamberH = H - 80;
    var pinholeY = 160;
    var pinholeSize = 28;

    for (var i = 0; i < 45; i++) {
      particles.push({
        x: 30 + Math.random() * (chamberW - 50),
        y: 40 + Math.random() * (chamberH - 20),
        vx: (Math.random() - 0.5) * 4,
        vy: (Math.random() - 0.5) * 4,
        effused: false
      });
    }

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Temperature (K):</strong>
            <input type="range" id="${canvasId}-temp" min="100" max="1200" step="25" value="${tempK}" style="vertical-align:middle;">
            <span id="${canvasId}-temp-val">${tempK} K</span>
          </label>
          <label><strong>Molar Mass (g/mol):</strong>
            <select id="${canvasId}-gas" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; padding:2px 6px; border-radius:4px;">
              <option value="4">Helium (He, 4.0 g/mol)</option>
              <option value="28" selected>Nitrogen (N₂, 28.0 g/mol)</option>
              <option value="40">Argon (Ar, 40.0 g/mol)</option>
              <option value="131">Xenon (Xe, 131.3 g/mol)</option>
            </select>
          </label>
          <button id="${canvasId}-reset" style="background:#0284c7; color:#fff; border:none; padding:3px 10px; border-radius:4px; cursor:pointer;">Reset Chamber</button>
        </div>
      `;

      var tSlider = document.getElementById(`${canvasId}-temp`);
      var tVal = document.getElementById(`${canvasId}-temp-val`);
      var gSelect = document.getElementById(`${canvasId}-gas`);
      var rBtn = document.getElementById(`${canvasId}-reset`);

      if (tSlider && tVal) {
        tSlider.addEventListener('input', function(e) {
          tempK = parseFloat(e.target.value);
          tVal.textContent = tempK + ' K';
        });
      }
      if (gSelect) {
        gSelect.addEventListener('change', function(e) {
          molarMass = parseFloat(e.target.value);
        });
      }
      if (rBtn) {
        rBtn.addEventListener('click', function() {
          particles.forEach(function(p) {
            p.x = 30 + Math.random() * (chamberW - 50);
            p.y = 40 + Math.random() * (chamberH - 20);
            p.effused = false;
          });
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      // Speeds calculation
      var M_kg = molarMass / 1000.0;
      var v_mp = Math.sqrt((2 * R * tempK) / M_kg);
      var v_bar = Math.sqrt((8 * R * tempK) / (Math.PI * M_kg));
      var v_rms = Math.sqrt((3 * R * tempK) / M_kg);

      // Left: 2D Effusion Chamber
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(20, 30, chamberW, chamberH);
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      // Walls with pinhole orifice
      ctx.beginPath();
      ctx.moveTo(20, 30);
      ctx.lineTo(20, 30 + chamberH);
      ctx.lineTo(20 + chamberW, 30 + chamberH);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(20, 30);
      ctx.lineTo(20 + chamberW, 30);
      ctx.lineTo(20 + chamberW, pinholeY);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(20 + chamberW, pinholeY + pinholeSize);
      ctx.lineTo(20 + chamberW, 30 + chamberH);
      ctx.stroke();

      // Orifice glow
      ctx.fillStyle = '#fbbf24';
      ctx.fillRect(20 + chamberW - 2, pinholeY, 4, pinholeSize);

      // Right: High vacuum chamber
      ctx.fillStyle = 'rgba(2, 6, 23, 0.7)';
      ctx.fillRect(20 + chamberW, 30, 80, chamberH);

      // Particle simulation
      var speedScale = (v_bar / 500) * 1.5;
      particles.forEach(function(p) {
        p.x += p.vx * speedScale;
        p.y += p.vy * speedScale;

        if (!p.effused) {
          // Bounce inside chamber
          if (p.x < 25) { p.x = 25; p.vx = Math.abs(p.vx); }
          if (p.y < 35) { p.y = 35; p.vy = Math.abs(p.vy); }
          if (p.y > 25 + chamberH) { p.y = 25 + chamberH; p.vy = -Math.abs(p.vy); }

          if (p.x > 15 + chamberW) {
            if (p.y >= pinholeY && p.y <= pinholeY + pinholeSize) {
              p.effused = true; // Escaped through pinhole!
            } else {
              p.x = 15 + chamberW;
              p.vx = -Math.abs(p.vx);
            }
          }
          ctx.fillStyle = '#60a5fa';
        } else {
          // Escaping through pinhole into vacuum
          if (p.x > 20 + chamberW + 75) {
            p.x = 30 + Math.random() * (chamberW - 50);
            p.y = 40 + Math.random() * (chamberH - 20);
            p.effused = false;
          }
          ctx.fillStyle = '#f43f5e';
        }

        ctx.beginPath();
        ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
        ctx.fill();
      });

      // Right half: Maxwell-Boltzmann speed distribution curve
      var graphX = 450, graphY = 40, graphW = W - graphX - 40, graphH = H - 90;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graphX, graphY, graphW, graphH);
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1;
      ctx.strokeRect(graphX, graphY, graphW, graphH);

      // Plot f(v) = 4*pi*(M/(2*pi*R*T))^(3/2) * v^2 * exp(-M*v^2 / (2*R*T))
      ctx.beginPath();
      var maxV = 2500; // m/s
      var factor1 = 4 * Math.PI * Math.pow(M_kg / (2 * Math.PI * R * tempK), 1.5);
      var maxF = 0;

      for (var v = 0; v < maxV; v += 10) {
        var fv = factor1 * v * v * Math.exp(-(M_kg * v * v) / (2 * R * tempK));
        if (fv > maxF) maxF = fv;
      }

      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      for (var v = 0; v < maxV; v += 10) {
        var fv = factor1 * v * v * Math.exp(-(M_kg * v * v) / (2 * R * tempK));
        var px = graphX + (v / maxV) * graphW;
        var py = graphY + graphH - (fv / (maxF * 1.15)) * graphH;
        if (v === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Mark Characteristic Speeds
      function drawSpeedMarker(spd, color, label) {
        if (spd > maxV) return;
        var sx = graphX + (spd / maxV) * graphW;
        ctx.strokeStyle = color;
        ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.moveTo(sx, graphY);
        ctx.lineTo(sx, graphY + graphH);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = color;
        ctx.font = '10px monospace';
        ctx.fillText(label + ` (${Math.round(spd)} m/s)`, sx + 4, graphY + 18 + (label === 'v_rms' ? 24 : (label === 'v̄' ? 12 : 0)));
      }

      drawSpeedMarker(v_mp, '#22c55e', 'v_mp');
      drawSpeedMarker(v_bar, '#fbbf24', 'v̄');
      drawSpeedMarker(v_rms, '#f43f5e', 'v_rms');

      // Title & Labels
      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Maxwell-Boltzmann Speed Distribution f(v)', graphX + 12, graphY - 12);
      ctx.fillText('Knudsen Effusion Chamber (Gas Leakage)', 20, 22);

      // Metrics Bar
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(`M = ${molarMass} g/mol | T = ${tempK} K | v_mp = ${Math.round(v_mp)} m/s | v̄ = ${Math.round(v_bar)} m/s | v_rms = ${Math.round(v_rms)} m/s`, graphX + 8, graphY + graphH - 12);
      ctx.fillText(`Relative Effusion Rate ∝ √(T/M) = ${(Math.sqrt(tempK / molarMass)).toFixed(2)} a.u.`, 25, H - 20);

      animOffset += 1;
      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 2. Electrolyte Ionic Mobility & Stokes Drift Simulator
  // =========================================================================
  window.KineticsSims.sim_kin_electrolyte_ionic_mobility = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var eField = 100;    // V/m
    var viscosity = 1.0; // cP (mPa*s)
    var electrolyte = 'NaCl'; // 'HCl', 'NaCl', 'CuSO4'

    // Ions
    var cations = [];
    var anions = [];
    for (var i = 0; i < 28; i++) {
      cations.push({ x: 60 + Math.random() * (W - 120), y: 70 + Math.random() * (H - 140) });
      anions.push({ x: 60 + Math.random() * (W - 120), y: 70 + Math.random() * (H - 140) });
    }

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Electric Field (V/m):</strong>
            <input type="range" id="${canvasId}-efield" min="10" max="300" step="10" value="${eField}" style="vertical-align:middle;">
            <span id="${canvasId}-efield-val">${eField} V/m</span>
          </label>
          <label><strong>Solvent Viscosity η (cP):</strong>
            <input type="range" id="${canvasId}-visc" min="0.5" max="3.0" step="0.1" value="${viscosity}" style="vertical-align:middle;">
            <span id="${canvasId}-visc-val">${viscosity.toFixed(1)} cP</span>
          </label>
          <label><strong>Electrolyte System:</strong>
            <select id="${canvasId}-elect" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; padding:2px 6px; border-radius:4px;">
              <option value="HCl">Hydrochloric Acid (H⁺ / Cl⁻)</option>
              <option value="NaCl" selected>Sodium Chloride (Na⁺ / Cl⁻)</option>
              <option value="CuSO4">Copper Sulfate (Cu²⁺ / SO₄²⁻)</option>
            </select>
          </label>
        </div>
      `;

      var efSlider = document.getElementById(`${canvasId}-efield`);
      var efVal = document.getElementById(`${canvasId}-efield-val`);
      var vSlider = document.getElementById(`${canvasId}-visc`);
      var vVal = document.getElementById(`${canvasId}-visc-val`);
      var elSelect = document.getElementById(`${canvasId}-elect`);

      if (efSlider && efVal) {
        efSlider.addEventListener('input', function(e) {
          eField = parseFloat(e.target.value);
          efVal.textContent = eField + ' V/m';
        });
      }
      if (vSlider && vVal) {
        vSlider.addEventListener('input', function(e) {
          viscosity = parseFloat(e.target.value);
          vVal.textContent = viscosity.toFixed(1) + ' cP';
        });
      }
      if (elSelect) {
        elSelect.addEventListener('change', function(e) {
          electrolyte = e.target.value;
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 35);

      // Ionic mobilities u = z*e / (6*pi*eta*r) in 10^-8 m^2/(V*s)
      var u_cat = 5.19, u_an = 7.91; // Default NaCl (Na+=5.19, Cl-=7.91)
      var catName = 'Na⁺', anName = 'Cl⁻';
      var z_c = 1, z_a = 1;

      if (electrolyte === 'HCl') {
        u_cat = 36.23; // Grotthuss proton hopping!
        u_an = 7.91;
        catName = 'H⁺ (hydronium)';
        anName = 'Cl⁻';
      } else if (electrolyte === 'CuSO4') {
        u_cat = 5.56;
        u_an = 8.29;
        z_c = 2; z_a = 2;
        catName = 'Cu²⁺';
        anName = 'SO₄²⁻';
      }

      // Viscosity scaling (Walden's rule: u * eta = const)
      var eff_u_cat = (u_cat / viscosity) * (eField / 100);
      var eff_u_an = (u_an / viscosity) * (eField / 100);

      // Transport numbers
      var t_plus = eff_u_cat / (eff_u_cat + eff_u_an);
      var t_minus = eff_u_an / (eff_u_cat + eff_u_an);

      // Draw Electrodes
      // Anode (+) on Left
      ctx.fillStyle = '#ef4444';
      ctx.fillRect(30, 50, 16, H - 100);
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('ANODE (+)', 15, 40);

      // Cathode (-) on Right
      ctx.fillStyle = '#3b82f6';
      ctx.fillRect(W - 46, 50, 16, H - 100);
      ctx.fillStyle = '#ffffff';
      ctx.fillText('CATHODE (-)', W - 90, 40);

      // Electric field arrows E ->
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
      ctx.lineWidth = 1;
      for (var y = 70; y < H - 50; y += 45) {
        ctx.beginPath();
        ctx.moveTo(60, y);
        ctx.lineTo(W - 60, y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(W - 68, y - 4);
        ctx.lineTo(W - 60, y);
        ctx.lineTo(W - 68, y + 4);
        ctx.stroke();
      }

      // Update Cations (drift to Cathode right)
      cations.forEach(function(c) {
        var drift = (eff_u_cat * 0.12);
        var thermal = (Math.random() - 0.5) * 1.5;
        c.x += drift + thermal;
        c.y += (Math.random() - 0.5) * 1.2;

        if (c.x > W - 55) c.x = 55 + Math.random() * 20;
        if (c.y < 60) c.y = 60;
        if (c.y > H - 60) c.y = H - 60;

        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(c.x, c.y, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#0f172a';
        ctx.font = 'bold 8px monospace';
        ctx.fillText('+', c.x - 3, c.y + 3);
      });

      // Update Anions (drift to Anode left)
      anions.forEach(function(a) {
        var drift = (eff_u_an * 0.12);
        var thermal = (Math.random() - 0.5) * 1.5;
        a.x -= (drift - thermal);
        a.y += (Math.random() - 0.5) * 1.2;

        if (a.x < 55) a.x = W - 55 - Math.random() * 20;
        if (a.y < 60) a.y = 60;
        if (a.y > H - 60) a.y = H - 60;

        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.arc(a.x, a.y, 7, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 8px monospace';
        ctx.fillText('-', a.x - 2, a.y + 3);
      });

      // Dashboard
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(W / 2 - 220, H - 60, 440, 48);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(W / 2 - 220, H - 60, 440, 48);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '11px monospace';
      ctx.fillText(`Cation: ${catName} | Drift Mobility u₊: ${(eff_u_cat).toFixed(2)} ×10⁻⁸ m²/(V·s) | Transport t₊: ${(t_plus).toFixed(3)}`, W / 2 - 210, H - 42);
      ctx.fillStyle = '#f43f5e';
      ctx.fillText(`Anion: ${anName} | Drift Mobility u₋: ${(eff_u_an).toFixed(2)} ×10⁻⁸ m²/(V·s) | Transport t₋: ${(t_minus).toFixed(3)}`, W / 2 - 210, H - 24);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 3. Fickian Diffusion Gradient & Brownian Random Walk Simulator
  // =========================================================================
  window.KineticsSims.sim_kin_fick_diffusion_brownian_walk = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var diffCoeff = 2.0; // Diffusion coefficient D (x10^-9 m^2/s)
    var simTime = 0;
    var paused = false;

    // Ensemble of random walkers
    var walkers = [];
    for (var i = 0; i < 90; i++) {
      walkers.push({ x: W / 4, y: H / 2 });
    }

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Diffusion Coeff D:</strong>
            <input type="range" id="${canvasId}-dcoeff" min="0.5" max="5.0" step="0.25" value="${diffCoeff}" style="vertical-align:middle;">
            <span id="${canvasId}-dcoeff-val">${diffCoeff.toFixed(2)} ×10⁻⁹ m²/s</span>
          </label>
          <button id="${canvasId}-pulse" style="background:#0284c7; color:#fff; border:none; padding:3px 10px; border-radius:4px; cursor:pointer;">Inject Delta Pulse (t=0)</button>
        </div>
      `;

      var dSlider = document.getElementById(`${canvasId}-dcoeff`);
      var dVal = document.getElementById(`${canvasId}-dcoeff-val`);
      var pBtn = document.getElementById(`${canvasId}-pulse`);

      if (dSlider && dVal) {
        dSlider.addEventListener('input', function(e) {
          diffCoeff = parseFloat(e.target.value);
          dVal.textContent = diffCoeff.toFixed(2) + ' ×10⁻⁹ m²/s';
        });
      }
      if (pBtn) {
        pBtn.addEventListener('click', function() {
          simTime = 0.1;
          walkers.forEach(function(w) {
            w.x = W / 4;
            w.y = H / 2;
          });
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 35);

      simTime += 0.03 * (diffCoeff / 2.0);

      // Left Half: 2D Brownian Particle Ensemble
      var boxW = W / 2 - 30;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(20, 30, boxW, H - 70);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(20, 30, boxW, H - 70);

      ctx.fillStyle = '#e2e8f0';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Brownian Random Walk Ensemble (⟨r²⟩ = 4Dt)', 30, 22);

      // Walkers update
      var stepSize = Math.sqrt(2 * diffCoeff * 0.4);
      walkers.forEach(function(w) {
        w.x += (Math.random() - 0.5) * stepSize * 3;
        w.y += (Math.random() - 0.5) * stepSize * 3;

        // Boundaries
        if (w.x < 25) w.x = 25;
        if (w.x > 20 + boxW - 5) w.x = 20 + boxW - 5;
        if (w.y < 35) w.y = 35;
        if (w.y > H - 45) w.y = H - 45;

        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(w.x, w.y, 2.5, 0, Math.PI * 2);
        ctx.fill();
      });

      // Mean displacement circle
      var rmsR = Math.min(boxW / 2 - 10, Math.sqrt(4 * diffCoeff * simTime * 120));
      ctx.strokeStyle = 'rgba(239, 68, 68, 0.7)';
      ctx.setLineDash([4, 4]);
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(W / 4, H / 2, rmsR, 0, Math.PI * 2);
      ctx.stroke();
      ctx.setLineDash([]);

      // Right Half: Fick's Second Law Gaussian Concentration Profile c(x, t)
      var graphX = W / 2 + 15, graphY = 30, graphW = W / 2 - 35, graphH = H - 70;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graphX, graphY, graphW, graphH);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(graphX, graphY, graphW, graphH);

      ctx.fillStyle = '#e2e8f0';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText("Fick's 2nd Law: ∂c/∂t = D (∂²c/∂x²)", graphX + 10, 22);

      // Gaussian curve: c(x,t) = (N / sqrt(4*pi*D*t)) * exp(-x^2 / (4*D*t))
      var sigma = Math.max(8, Math.sqrt(2 * diffCoeff * (simTime + 0.1) * 35));
      ctx.strokeStyle = '#22c55e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      var midX = graphX + graphW / 2;
      for (var px = graphX; px <= graphX + graphW; px += 2) {
        var dx = px - midX;
        var cy = (graphY + graphH - 20) - (240 / (sigma / 8)) * Math.exp(-(dx * dx) / (2 * sigma * sigma));
        if (px === graphX) ctx.moveTo(px, cy);
        else ctx.lineTo(px, cy);
      }
      ctx.stroke();

      // Axis lines
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(graphX, graphY + graphH - 20);
      ctx.lineTo(graphX + graphW, graphY + graphH - 20);
      ctx.stroke();

      // Metrics footer
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(`Diffusion Time: ${(simTime).toFixed(2)} s | RMS Displacement: ${(Math.sqrt(2 * diffCoeff * simTime * 1e-9) * 1e6).toFixed(2)} µm`, 30, H - 15);
      ctx.fillText(`FWHM Gaussian Width: ${(2.355 * sigma).toFixed(1)} px`, graphX + 10, H - 15);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 4. Integrated Rate Laws & Reaction Order Transformation
  // =========================================================================
  window.KineticsSims.sim_kin_integrated_rate_laws = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var order = 1;      // 0, 1, 2, 3
    var kRate = 0.05;   // Rate constant k
    var a0 = 1.0;       // Initial conc [A]0 (M)
    var simT = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Reaction Order (n):</strong>
            <select id="${canvasId}-order" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; padding:2px 6px; border-radius:4px;">
              <option value="0">Zero Order (n = 0)</option>
              <option value="1" selected>First Order (n = 1)</option>
              <option value="2">Second Order (n = 2)</option>
              <option value="3">Third Order (n = 3)</option>
            </select>
          </label>
          <label><strong>Rate Constant (k):</strong>
            <input type="range" id="${canvasId}-krate" min="0.01" max="0.15" step="0.01" value="${kRate}" style="vertical-align:middle;">
            <span id="${canvasId}-krate-val">${kRate.toFixed(2)}</span>
          </label>
          <button id="${canvasId}-replay" style="background:#0284c7; color:#fff; border:none; padding:3px 10px; border-radius:4px; cursor:pointer;">Restart Kinetics</button>
        </div>
      `;

      var oSelect = document.getElementById(`${canvasId}-order`);
      var kSlider = document.getElementById(`${canvasId}-krate`);
      var kVal = document.getElementById(`${canvasId}-krate-val`);
      var rBtn = document.getElementById(`${canvasId}-replay`);

      if (oSelect) {
        oSelect.addEventListener('change', function(e) {
          order = parseInt(e.target.value);
          simT = 0;
        });
      }
      if (kSlider && kVal) {
        kSlider.addEventListener('input', function(e) {
          kRate = parseFloat(e.target.value);
          kVal.textContent = kRate.toFixed(2);
        });
      }
      if (rBtn) {
        rBtn.addEventListener('click', function() { simT = 0; });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      simT += 0.2;
      if (simT > 60) simT = 60;

      var graph1X = 50, graphY = 40, graphW = W / 2 - 70, graphH = H - 90;
      var graph2X = W / 2 + 30, graph2W = W / 2 - 60;

      // Concentration [A] vs time t
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graph1X, graphY, graphW, graphH);
      ctx.strokeRect(graph1X, graphY, graphW, graphH);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('[A] vs Time (Decay Curve)', graph1X + 10, graphY - 10);

      function calcConc(t) {
        if (order === 0) return Math.max(0, a0 - kRate * t);
        if (order === 1) return a0 * Math.exp(-kRate * t);
        if (order === 2) return a0 / (1 + kRate * a0 * t);
        if (order === 3) return a0 / Math.sqrt(1 + 2 * kRate * a0 * a0 * t);
      }

      // Plot [A] curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var t = 0; t <= 60; t += 0.5) {
        var c = calcConc(t);
        var px = graph1X + (t / 60) * graphW;
        var py = graphY + graphH - (c / a0) * graphH;
        if (t === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current live point
      var currentC = calcConc(simT);
      var curX = graph1X + (simT / 60) * graphW;
      var curY = graphY + graphH - (currentC / a0) * graphH;
      ctx.fillStyle = '#f43f5e';
      ctx.beginPath();
      ctx.arc(curX, curY, 5, 0, Math.PI * 2);
      ctx.fill();

      // Linearized plot on the right
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graph2X, graphY, graph2W, graphH);
      ctx.strokeRect(graph2X, graphY, graph2W, graphH);

      var linearTitle = '[A] vs t (Zero Order)';
      if (order === 1) linearTitle = 'ln[A] vs t (First Order)';
      else if (order === 2) linearTitle = '1/[A] vs t (Second Order)';
      else if (order === 3) linearTitle = '1/[A]² vs t (Third Order)';

      ctx.fillStyle = '#f8fafc';
      ctx.fillText('Linear Transform: ' + linearTitle, graph2X + 10, graphY - 10);

      ctx.strokeStyle = '#22c55e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var t = 0; t <= 60; t += 0.5) {
        var c = calcConc(t);
        var linY = 0;
        if (order === 0) linY = c / a0;
        else if (order === 1) linY = (Math.log(c) + 4) / 4; // Normalized ln[A]
        else if (order === 2) linY = ((1 / c) - 1) / (1 / calcConc(60) - 1);
        else if (order === 3) linY = ((1 / (c * c)) - 1) / (1 / (calcConc(60) * calcConc(60)) - 1);

        var px = graph2X + (t / 60) * graph2W;
        var py = graphY + graphH - Math.max(0, Math.min(1, linY)) * graphH;
        if (t === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Half-life metric
      var t_half = 0;
      if (order === 0) t_half = a0 / (2 * kRate);
      else if (order === 1) t_half = Math.log(2) / kRate;
      else if (order === 2) t_half = 1 / (kRate * a0);
      else if (order === 3) t_half = 1.5 / (kRate * a0 * a0);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(`Current [A]: ${currentC.toFixed(4)} M | t = ${simT.toFixed(1)} s | t₁/₂ = ${t_half.toFixed(2)} s`, 50, H - 15);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 5. Arrhenius Activation Energy & Maxwellian Barrier Crossing
  // =========================================================================
  window.KineticsSims.sim_kin_arrhenius_activation_energy = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var tempK = 320;   // K
    var Ea_kJ = 50;    // kJ/mol
    var A_factor = 1e11;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Temperature T (K):</strong>
            <input type="range" id="${canvasId}-temp" min="250" max="800" step="10" value="${tempK}" style="vertical-align:middle;">
            <span id="${canvasId}-temp-val">${tempK} K</span>
          </label>
          <label><strong>Activation Barrier Eₐ (kJ/mol):</strong>
            <input type="range" id="${canvasId}-ea" min="20" max="100" step="5" value="${Ea_kJ}" style="vertical-align:middle;">
            <span id="${canvasId}-ea-val">${Ea_kJ} kJ/mol</span>
          </label>
        </div>
      `;

      var tSlider = document.getElementById(`${canvasId}-temp`);
      var tVal = document.getElementById(`${canvasId}-temp-val`);
      var eSlider = document.getElementById(`${canvasId}-ea`);
      var eVal = document.getElementById(`${canvasId}-ea-val`);

      if (tSlider && tVal) {
        tSlider.addEventListener('input', function(e) {
          tempK = parseFloat(e.target.value);
          tVal.textContent = tempK + ' K';
        });
      }
      if (eSlider && eVal) {
        eSlider.addEventListener('input', function(e) {
          Ea_kJ = parseFloat(e.target.value);
          eVal.textContent = Ea_kJ + ' kJ/mol';
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 35);

      var R = 8.314;
      var Ea_J = Ea_kJ * 1000;
      var boltzmannFraction = Math.exp(-Ea_J / (R * tempK));
      var rateConstK = A_factor * boltzmannFraction;

      var graph1X = 40, graphY = 40, graphW = W / 2 - 60, graphH = H - 90;
      var graph2X = W / 2 + 30, graph2W = W / 2 - 60;

      // Left: Boltzmann Energy Distribution f(E) vs E
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graph1X, graphY, graphW, graphH);
      ctx.strokeRect(graph1X, graphY, graphW, graphH);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Kinetic Energy Distribution & Reactive Fraction (E ≥ Eₐ)', graph1X + 10, graphY - 10);

      var maxE = 120; // kJ/mol
      var maxFE = 0;
      // Pre-calculate max
      for (var e = 0; e < maxE; e += 1) {
        var prob = (1 / (R * tempK / 1000)) * Math.exp(-(e) / (R * tempK / 1000));
        if (prob > maxFE) maxFE = prob;
      }

      // Fill area under E >= Ea (reactive molecules)
      ctx.fillStyle = 'rgba(239, 68, 68, 0.4)';
      ctx.beginPath();
      var eaX = graph1X + (Ea_kJ / maxE) * graphW;
      ctx.moveTo(eaX, graphY + graphH);
      for (var e = Ea_kJ; e <= maxE; e += 1) {
        var prob = (1 / (R * tempK / 1000)) * Math.exp(-(e) / (R * tempK / 1000));
        var px = graph1X + (e / maxE) * graphW;
        var py = graphY + graphH - (prob / (maxFE * 1.1)) * graphH;
        ctx.lineTo(px, py);
      }
      ctx.lineTo(graph1X + graphW, graphY + graphH);
      ctx.closePath();
      ctx.fill();

      // Draw distribution curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var e = 0; e <= maxE; e += 1) {
        var prob = (1 / (R * tempK / 1000)) * Math.exp(-(e) / (R * tempK / 1000));
        var px = graph1X + (e / maxE) * graphW;
        var py = graphY + graphH - (prob / (maxFE * 1.1)) * graphH;
        if (e === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Activation Barrier Line
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 3]);
      ctx.beginPath();
      ctx.moveTo(eaX, graphY);
      ctx.lineTo(eaX, graphY + graphH);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#ef4444';
      ctx.font = '11px monospace';
      ctx.fillText(`Eₐ = ${Ea_kJ} kJ`, eaX + 4, graphY + 25);

      // Right: Arrhenius Plot ln(k) vs 1/T
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graph2X, graphY, graph2W, graphH);
      ctx.strokeRect(graph2X, graphY, graph2W, graphH);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Arrhenius Linearization: ln(k) = ln(A) - Eₐ/(RT)', graph2X + 10, graphY - 10);

      // Plot line over 1/T range 0.001 to 0.004 K^-1
      ctx.strokeStyle = '#22c55e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      var invT_min = 0.001, invT_max = 0.004;
      var lnK_max = Math.log(A_factor) - (Ea_J / (R * 1000));
      var lnK_min = Math.log(A_factor) - (Ea_J / (R * 250));

      for (var invT = invT_min; invT <= invT_max; invT += 0.0001) {
        var lnK = Math.log(A_factor) - (Ea_J / R) * invT;
        var px = graph2X + ((invT - invT_min) / (invT_max - invT_min)) * graph2W;
        var py = graphY + graphH - ((lnK - lnK_min) / (lnK_max - lnK_min)) * graphH;
        if (invT === invT_min) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current operational dot
      var curInvT = 1.0 / tempK;
      var curLnK = Math.log(rateConstK);
      var curDotX = graph2X + ((curInvT - invT_min) / (invT_max - invT_min)) * graph2W;
      var curDotY = graphY + graphH - ((curLnK - lnK_min) / (lnK_max - lnK_min)) * graphH;
      ctx.fillStyle = '#fbbf24';
      ctx.beginPath();
      ctx.arc(curDotX, curDotY, 6, 0, Math.PI * 2);
      ctx.fill();

      // Dashboard
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(`Fraction with E ≥ Eₐ: exp(-Eₐ/RT) = ${boltzmannFraction.toExponential(3)} | k = ${rateConstK.toExponential(3)} s⁻¹`, 40, H - 15);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 6. Consecutive Reactions & Steady-State Approximation (SSA) Engine
  // =========================================================================
  window.KineticsSims.sim_kin_consecutive_reactions_ssa = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var k1 = 0.8;   // A -> B rate constant
    var k2 = 0.2;   // B -> C rate constant
    var showSSA = true;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Rate Constant k₁ (s⁻¹):</strong>
            <input type="range" id="${canvasId}-k1" min="0.1" max="2.0" step="0.1" value="${k1}" style="vertical-align:middle;">
            <span id="${canvasId}-k1-val">${k1.toFixed(1)}</span>
          </label>
          <label><strong>Rate Constant k₂ (s⁻¹):</strong>
            <input type="range" id="${canvasId}-k2" min="0.05" max="3.0" step="0.05" value="${k2}" style="vertical-align:middle;">
            <span id="${canvasId}-k2-val">${k2.toFixed(2)}</span>
          </label>
          <label><input type="checkbox" id="${canvasId}-ssa" ${showSSA ? 'checked' : ''}> Show Bodenstein SSA Curve [B]_SSA</label>
        </div>
      `;

      var k1Slider = document.getElementById(`${canvasId}-k1`);
      var k1Val = document.getElementById(`${canvasId}-k1-val`);
      var k2Slider = document.getElementById(`${canvasId}-k2`);
      var k2Val = document.getElementById(`${canvasId}-k2-val`);
      var ssaCheck = document.getElementById(`${canvasId}-ssa`);

      if (k1Slider && k1Val) {
        k1Slider.addEventListener('input', function(e) {
          k1 = parseFloat(e.target.value);
          k1Val.textContent = k1.toFixed(1);
        });
      }
      if (k2Slider && k2Val) {
        k2Slider.addEventListener('input', function(e) {
          k2 = parseFloat(e.target.value);
          k2Val.textContent = k2.toFixed(2);
        });
      }
      if (ssaCheck) {
        ssaCheck.addEventListener('change', function(e) {
          showSSA = e.target.checked;
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 35);

      var graphX = 60, graphY = 40, graphW = W - 120, graphH = H - 90;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graphX, graphY, graphW, graphH);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(graphX, graphY, graphW, graphH);

      var a0 = 1.0;
      var maxT = 15.0; // seconds

      // t_max = ln(k2/k1) / (k2 - k1)
      var t_max = (k1 !== k2) ? Math.log(k2 / k1) / (k2 - k1) : 1 / k1;
      var b_max = (k1 !== k2) ? a0 * Math.pow(k2 / k1, k2 / (k1 - k2)) : a0 / Math.E;

      // Plot [A](t) = [A]0 * exp(-k1*t)
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var t = 0; t <= maxT; t += 0.1) {
        var a = a0 * Math.exp(-k1 * t);
        var px = graphX + (t / maxT) * graphW;
        var py = graphY + graphH - (a / a0) * graphH;
        if (t === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot [B](t) = [A]0 * (k1/(k2 - k1)) * (exp(-k1*t) - exp(-k2*t))
      ctx.strokeStyle = '#fbbf24';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var t = 0; t <= maxT; t += 0.1) {
        var b = (k1 !== k2)
          ? a0 * (k1 / (k2 - k1)) * (Math.exp(-k1 * t) - Math.exp(-k2 * t))
          : a0 * k1 * t * Math.exp(-k1 * t);
        var px = graphX + (t / maxT) * graphW;
        var py = graphY + graphH - (b / a0) * graphH;
        if (t === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot [C](t) = [A]0 * [1 - (k2*exp(-k1*t) - k1*exp(-k2*t))/(k2 - k1)]
      ctx.strokeStyle = '#22c55e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var t = 0; t <= maxT; t += 0.1) {
        var c = (k1 !== k2)
          ? a0 * (1 - (k2 * Math.exp(-k1 * t) - k1 * Math.exp(-k2 * t)) / (k2 - k1))
          : a0 * (1 - Math.exp(-k1 * t) * (1 + k1 * t));
        var px = graphX + (t / maxT) * graphW;
        var py = graphY + graphH - (c / a0) * graphH;
        if (t === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot [B]_SSA = (k1 / k2) * [A](t) if enabled
      if (showSSA) {
        ctx.strokeStyle = '#f43f5e';
        ctx.setLineDash([5, 4]);
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (var t = 0; t <= maxT; t += 0.1) {
          var b_ssa = (k1 / k2) * a0 * Math.exp(-k1 * t);
          var px = graphX + (t / maxT) * graphW;
          var py = graphY + graphH - Math.min(1.2, b_ssa / a0) * graphH;
          if (t === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Intermediate Peak Marker
      if (t_max >= 0 && t_max <= maxT) {
        var peakX = graphX + (t_max / maxT) * graphW;
        var peakY = graphY + graphH - (b_max / a0) * graphH;
        ctx.fillStyle = '#fbbf24';
        ctx.beginPath();
        ctx.arc(peakX, peakY, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.font = '10px monospace';
        ctx.fillText(`Peak [B] = ${b_max.toFixed(3)} at t = ${t_max.toFixed(2)} s`, peakX + 8, peakY - 8);
      }

      // Legend
      ctx.font = 'bold 12px sans-serif';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('— [A](t) Reactant', graphX + 15, graphY + 25);
      ctx.fillStyle = '#fbbf24';
      ctx.fillText('— [B](t) Exact Intermediate', graphX + 150, graphY + 25);
      ctx.fillStyle = '#22c55e';
      ctx.fillText('— [C](t) Product', graphX + 340, graphY + 25);
      if (showSSA) {
        ctx.fillStyle = '#f43f5e';
        ctx.fillText('--- [B] SSA (k₁/k₂)[A]', graphX + 460, graphY + 25);
      }

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(`k₁ = ${k1} s⁻¹ | k₂ = ${k2} s⁻¹ | Ratio k₂/k₁ = ${(k2/k1).toFixed(2)} (${k2 > 5*k1 ? 'SSA Valid: k₂ ≫ k₁' : 'SSA Invalid: k₂ ~ k₁'})`, graphX, H - 15);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 7. Lindemann-Hinshelwood Unimolecular Pressure Fall-off Engine
  // =========================================================================
  window.KineticsSims.sim_kin_lindemann_pressure_falloff = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var k1 = 1.0e-3;   // Collisional activation rate constant
    var k_minus1 = 1.0; // Deactivation rate constant
    var k2 = 0.5;      // Product decomposition rate constant
    var gasM = 1.0;    // Gas concentration / pressure proxy

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Decomposition Barrier k₂ (s⁻¹):</strong>
            <input type="range" id="${canvasId}-k2" min="0.1" max="2.0" step="0.1" value="${k2}" style="vertical-align:middle;">
            <span id="${canvasId}-k2-val">${k2.toFixed(1)}</span>
          </label>
          <label><strong>Deactivation k₋₁:</strong>
            <input type="range" id="${canvasId}-km1" min="0.2" max="3.0" step="0.2" value="${k_minus1}" style="vertical-align:middle;">
            <span id="${canvasId}-km1-val">${k_minus1.toFixed(1)}</span>
          </label>
        </div>
      `;

      var k2Slider = document.getElementById(`${canvasId}-k2`);
      var k2Val = document.getElementById(`${canvasId}-k2-val`);
      var km1Slider = document.getElementById(`${canvasId}-km1`);
      var km1Val = document.getElementById(`${canvasId}-km1-val`);

      if (k2Slider && k2Val) {
        k2Slider.addEventListener('input', function(e) {
          k2 = parseFloat(e.target.value);
          k2Val.textContent = k2.toFixed(1);
        });
      }
      if (km1Slider && km1Val) {
        km1Slider.addEventListener('input', function(e) {
          k_minus1 = parseFloat(e.target.value);
          km1Val.textContent = k_minus1.toFixed(1);
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 35);

      var graph1X = 50, graphY = 40, graphW = W / 2 - 70, graphH = H - 90;
      var graph2X = W / 2 + 30, graph2W = W / 2 - 60;

      // k_uni = (k1 * k2 * [M]) / (k_minus1 * [M] + k2)
      // High pressure limit: k_inf = (k1 * k2) / k_minus1
      var k_inf = (k1 * k2) / k_minus1;

      // Left: k_uni vs Pressure [M] (Fall-off curve)
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graph1X, graphY, graphW, graphH);
      ctx.strokeRect(graph1X, graphY, graphW, graphH);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Lindemann Fall-off Curve: k_uni vs Pressure [M]', graph1X + 10, graphY - 10);

      var maxM = 5.0; // pressure range
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var m = 0; m <= maxM; m += 0.05) {
        var kuni = (k1 * k2 * m) / (k_minus1 * m + k2);
        var px = graph1X + (m / maxM) * graphW;
        var py = graphY + graphH - (kuni / (k_inf * 1.15)) * graphH;
        if (m === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // High pressure asymptote k_inf line
      var infY = graphY + graphH - (k_inf / (k_inf * 1.15)) * graphH;
      ctx.strokeStyle = '#ef4444';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(graph1X, infY);
      ctx.lineTo(graph1X + graphW, infY);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#ef4444';
      ctx.font = '10px monospace';
      ctx.fillText(`k_∞ = ${(k_inf).toExponential(2)} (High P: 1st Order)`, graph1X + 10, infY - 6);

      // Low pressure tangent
      ctx.strokeStyle = '#fbbf24';
      ctx.setLineDash([2, 3]);
      ctx.beginPath();
      ctx.moveTo(graph1X, graphY + graphH);
      ctx.lineTo(graph1X + graphW * 0.4, graphY + graphH - (k1 * (maxM * 0.4) / (k_inf * 1.15)) * graphH);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#fbbf24';
      ctx.fillText('Low P: 2nd Order k_uni ∝ [M]', graph1X + graphW * 0.25, graphY + graphH - 25);

      // Right: Double reciprocal plot 1/k_uni vs 1/[M]
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graph2X, graphY, graph2W, graphH);
      ctx.strokeRect(graph2X, graphY, graph2W, graphH);

      ctx.fillStyle = '#f8fafc';
      ctx.fillText('Lineweaver-style: 1/k_uni = (1/k_∞) + (k₋₁/k₁k₂)(1/[M])', graph2X + 10, graphY - 10);

      // 1/k_uni = 1/k_inf + (k_minus1/(k1*k2))*(1/[M])
      ctx.strokeStyle = '#22c55e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      var maxInvM = 4.0;
      for (var invM = 0; invM <= maxInvM; invM += 0.1) {
        var invK = (1 / k_inf) + (k_minus1 / (k1 * k2)) * invM;
        var px = graph2X + (invM / maxInvM) * graph2W;
        var py = graphY + graphH - (invK / ((1 / k_inf) + (k_minus1 / (k1 * k2)) * maxInvM * 1.1)) * graphH;
        if (invM === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(`k₁ = ${k1.toExponential(1)} | k₋₁ = ${k_minus1} | k₂ = ${k2} s⁻¹ | k_∞ = ${k_inf.toExponential(2)} s⁻¹`, graph1X, H - 15);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 8. Branched Chain Explosion Peninsula (H₂ + O₂) Simulator
  // =========================================================================
  window.KineticsSims.sim_kin_branched_chain_explosion_peninsula = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var tempC = 520;  // Operating Temperature (°C)
    var pressTorr = 40; // Operating Pressure (Torr)

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Temperature (°C):</strong>
            <input type="range" id="${canvasId}-temp" min="400" max="650" step="5" value="${tempC}" style="vertical-align:middle;">
            <span id="${canvasId}-temp-val">${tempC} °C</span>
          </label>
          <label><strong>Pressure (Torr):</strong>
            <input type="range" id="${canvasId}-press" min="1" max="250" step="1" value="${pressTorr}" style="vertical-align:middle;">
            <span id="${canvasId}-press-val">${pressTorr} Torr</span>
          </label>
        </div>
      `;

      var tSlider = document.getElementById(`${canvasId}-temp`);
      var tVal = document.getElementById(`${canvasId}-temp-val`);
      var pSlider = document.getElementById(`${canvasId}-press`);
      var pVal = document.getElementById(`${canvasId}-press-val`);

      if (tSlider && tVal) {
        tSlider.addEventListener('input', function(e) {
          tempC = parseFloat(e.target.value);
          tVal.textContent = tempC + ' °C';
        });
      }
      if (pSlider && pVal) {
        pSlider.addEventListener('input', function(e) {
          pressTorr = parseFloat(e.target.value);
          pVal.textContent = pressTorr + ' Torr';
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 35);

      var graphX = 60, graphY = 40, graphW = W - 120, graphH = H - 90;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graphX, graphY, graphW, graphH);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(graphX, graphY, graphW, graphH);

      // Temperature bounds: 400 to 650 C
      // Pressure bounds: 0 to 250 Torr (log/linear mapped)
      var tMin = 400, tMax = 650;
      var pMax = 250;

      // Draw explosion peninsula boundaries
      // First limit: wall deactivation (p1 decreases with T)
      // Second limit: three-body gas deactivation H + O2 + M -> HO2 + M (p2 increases with T)
      // Third limit: thermal runaway (p3 decreases with T)
      ctx.fillStyle = 'rgba(239, 68, 68, 0.25)';
      ctx.beginPath();

      // Lower curve (1st limit)
      for (var t = 440; t <= 620; t += 5) {
        var p1 = 15 * Math.exp(-(t - 450) / 60);
        var px = graphX + ((t - tMin) / (tMax - tMin)) * graphW;
        var py = graphY + graphH - (p1 / pMax) * graphH;
        if (t === 440) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      // Upper curve (2nd limit)
      for (var t = 620; t >= 440; t -= 5) {
        var p2 = 8 + 140 * Math.pow((t - 430) / 190, 1.8);
        var px = graphX + ((t - tMin) / (tMax - tMin)) * graphW;
        var py = graphY + graphH - (p2 / pMax) * graphH;
        ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.fill();

      // Draw boundary lines
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2.5;
      // 1st limit
      ctx.beginPath();
      for (var t = 440; t <= 650; t += 5) {
        var p1 = 15 * Math.exp(-(t - 450) / 60);
        var px = graphX + ((t - tMin) / (tMax - tMin)) * graphW;
        var py = graphY + graphH - (p1 / pMax) * graphH;
        if (t === 440) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // 2nd limit
      ctx.beginPath();
      for (var t = 440; t <= 620; t += 5) {
        var p2 = 8 + 140 * Math.pow((t - 430) / 190, 1.8);
        var px = graphX + ((t - tMin) / (tMax - tMin)) * graphW;
        var py = graphY + graphH - (p2 / pMax) * graphH;
        if (t === 440) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // 3rd limit (Thermal explosion)
      ctx.strokeStyle = '#fbbf24';
      ctx.beginPath();
      for (var t = 520; t <= 650; t += 5) {
        var p3 = 240 - 120 * Math.pow((t - 520) / 130, 0.8);
        var px = graphX + ((t - tMin) / (tMax - tMin)) * graphW;
        var py = graphY + graphH - (p3 / pMax) * graphH;
        if (t === 520) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // State determination
      var p1_cur = 15 * Math.exp(-(tempC - 450) / 60);
      var p2_cur = (tempC >= 430) ? 8 + 140 * Math.pow((tempC - 430) / 190, 1.8) : 0;
      var p3_cur = (tempC >= 520) ? 240 - 120 * Math.pow((tempC - 520) / 130, 0.8) : 999;

      var isExplosion = false;
      var regime = 'Slow Steady Reaction (Wall Termination)';

      if (tempC > 440 && pressTorr >= p1_cur && pressTorr <= p2_cur) {
        isExplosion = true;
        regime = 'EXPLOSIVE BRANCHED CHAIN (Peninsula: 2k₂ > k_wall)';
      } else if (tempC > 520 && pressTorr >= p3_cur) {
        isExplosion = true;
        regime = 'THERMAL RUNAWAY EXPLOSION (3rd Limit)';
      } else if (pressTorr > p2_cur) {
        regime = 'Slow Reaction (Three-Body Termination: H + O₂ + M → HO₂ + M)';
      }

      // Plot Operating Point
      var curX = graphX + ((tempC - tMin) / (tMax - tMin)) * graphW;
      var curY = graphY + graphH - (pressTorr / pMax) * graphH;

      ctx.fillStyle = isExplosion ? '#ef4444' : '#22c55e';
      ctx.beginPath();
      ctx.arc(curX, curY, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Label Peninsula
      ctx.fillStyle = '#ef4444';
      ctx.font = 'bold 13px sans-serif';
      ctx.fillText('BRANCHED CHAIN EXPLOSION PENINSULA', graphX + graphW * 0.45, graphY + graphH * 0.65);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px monospace';
      ctx.fillText('1st Limit: Wall Destruction of Radicals', graphX + 15, graphY + graphH - 12);
      ctx.fillText('2nd Limit: Gas Three-Body Termination', graphX + 15, graphY + graphH * 0.45);
      ctx.fillText('3rd Limit: Thermal Runaway', graphX + graphW * 0.65, graphY + 30);

      // Title & Status
      ctx.fillStyle = isExplosion ? '#f87171' : '#4ade80';
      ctx.font = 'bold 12px monospace';
      ctx.fillText(`State: ${regime} [T = ${tempC}°C, P = ${pressTorr} Torr]`, graphX, graphY - 10);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 9. Michaelis-Menten Enzyme Kinetics & Inhibition Modes
  // =========================================================================
  window.KineticsSims.sim_kin_michaelis_menten_inhibition = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var Vmax = 100;     // µmol/(L*min)
    var Km = 20;        // µM
    var inhType = 'none'; // 'none', 'comp', 'uncomp', 'noncomp'
    var inhConc = 15;   // µM
    var Ki = 10;        // µM

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Inhibition Mode:</strong>
            <select id="${canvasId}-inhtype" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; padding:2px 6px; border-radius:4px;">
              <option value="none" selected>No Inhibitor (Baseline)</option>
              <option value="comp">Competitive Inhibition</option>
              <option value="uncomp">Uncompetitive Inhibition</option>
              <option value="noncomp">Non-Competitive Inhibition</option>
            </select>
          </label>
          <label><strong>Inhibitor [I] (µM):</strong>
            <input type="range" id="${canvasId}-inhi" min="0" max="50" step="5" value="${inhConc}" style="vertical-align:middle;">
            <span id="${canvasId}-inhi-val">${inhConc} µM</span>
          </label>
        </div>
      `;

      var iSelect = document.getElementById(`${canvasId}-inhtype`);
      var iSlider = document.getElementById(`${canvasId}-inhi`);
      var iVal = document.getElementById(`${canvasId}-inhi-val`);

      if (iSelect) {
        iSelect.addEventListener('change', function(e) {
          inhType = e.target.value;
        });
      }
      if (iSlider && iVal) {
        iSlider.addEventListener('input', function(e) {
          inhConc = parseFloat(e.target.value);
          iVal.textContent = inhConc + ' µM';
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 35);

      var graph1X = 50, graphY = 40, graphW = W / 2 - 70, graphH = H - 90;
      var graph2X = W / 2 + 30, graph2W = W / 2 - 60;

      // Calculate Apparent Parameters
      var alpha = 1 + (inhType !== 'none' ? inhConc / Ki : 0);
      var alpha_prime = 1;
      if (inhType === 'uncomp') { alpha_prime = alpha; alpha = 1; }
      else if (inhType === 'noncomp') { alpha_prime = alpha; }

      var Vmax_app = Vmax / alpha_prime;
      var Km_app = (Km * alpha) / alpha_prime;

      // Left: Michaelis-Menten Hyperbola v vs [S]
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graph1X, graphY, graphW, graphH);
      ctx.strokeRect(graph1X, graphY, graphW, graphH);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Michaelis-Menten Velocity: v = V_max[S] / (K_m + [S])', graph1X + 10, graphY - 10);

      var maxS = 120; // µM
      // Baseline curve (Uninhibited)
      ctx.strokeStyle = '#64748b';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      for (var s = 0; s <= maxS; s += 2) {
        var v = (Vmax * s) / (Km + s);
        var px = graph1X + (s / maxS) * graphW;
        var py = graphY + graphH - (v / (Vmax * 1.15)) * graphH;
        if (s === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Active / Inhibited curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var s = 0; s <= maxS; s += 2) {
        var v = (Vmax_app * s) / (Km_app + s);
        var px = graph1X + (s / maxS) * graphW;
        var py = graphY + graphH - (v / (Vmax * 1.15)) * graphH;
        if (s === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Right: Lineweaver-Burk Double-Reciprocal Plot (1/v vs 1/[S])
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graph2X, graphY, graph2W, graphH);
      ctx.strokeRect(graph2X, graphY, graph2W, graphH);

      ctx.fillStyle = '#f8fafc';
      ctx.fillText('Lineweaver-Burk: 1/v = (K_m/V_max)(1/[S]) + 1/V_max', graph2X + 10, graphY - 10);

      // Plot line
      ctx.strokeStyle = '#22c55e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      var maxInvS = 0.15;
      var maxInvV = 0.08;

      for (var invS = 0; invS <= maxInvS; invS += 0.005) {
        var invV = (Km_app / Vmax_app) * invS + (1 / Vmax_app);
        var px = graph2X + (invS / maxInvS) * graph2W;
        var py = graphY + graphH - (invV / maxInvV) * graphH;
        if (invS === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Metrics Dashboard
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(`Baseline: V_max = ${Vmax} µM/min, K_m = ${Km} µM | Inhibited Apparent: V_max(app) = ${Vmax_app.toFixed(1)}, K_m(app) = ${Km_app.toFixed(1)} µM`, graph1X, H - 15);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 10. London-Eyring-Polanyi-Sato (LEPS) Potential Energy Surface Trajectory
  // =========================================================================
  window.KineticsSims.sim_kin_potential_energy_surface_trajectory = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var trajEnergy = 35; // kJ/mol (relative to reactant valley)
    var animT = 0;

    var ctrls = document.getElementById(controlsId);
    if (ctrls) {
      ctrls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:12px; align-items:center; color:#cbd5e1; font-size:12px;">
          <label><strong>Collision Energy E_coll (kJ/mol):</strong>
            <input type="range" id="${canvasId}-energy" min="15" max="65" step="2" value="${trajEnergy}" style="vertical-align:middle;">
            <span id="${canvasId}-energy-val">${trajEnergy} kJ/mol</span>
          </label>
        </div>
      `;

      var eSlider = document.getElementById(`${canvasId}-energy`);
      var eVal = document.getElementById(`${canvasId}-energy-val`);

      if (eSlider && eVal) {
        eSlider.addEventListener('input', function(e) {
          trajEnergy = parseFloat(e.target.value);
          eVal.textContent = trajEnergy + ' kJ/mol';
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 35);

      var graphX = 60, graphY = 35, graphSize = H - 75;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(graphX, graphY, graphSize, graphSize);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(graphX, graphY, graphSize, graphSize);

      // LEPS 2D contour simulation (R_AB vs R_BC)
      // Saddle point at R_AB = 1.4 A, R_BC = 1.4 A, barrier = 32 kJ/mol
      var saddleX = graphX + graphSize * 0.45;
      var saddleY = graphY + graphSize * 0.55;

      // Draw Contours
      for (var lvl = 10; lvl <= 100; lvl += 15) {
        ctx.strokeStyle = (lvl <= 35) ? 'rgba(56, 189, 248, 0.4)' : 'rgba(239, 68, 68, 0.3)';
        ctx.lineWidth = 1.5;

        // Reactant valley (high R_AB, low R_BC)
        ctx.beginPath();
        var rx = graphX + graphSize * (0.15 + lvl * 0.003);
        ctx.arc(graphX + graphSize, graphY + graphSize * 0.15, graphSize * (0.8 - lvl * 0.006), Math.PI * 0.6, Math.PI);
        ctx.stroke();

        // Product valley (low R_AB, high R_BC)
        ctx.beginPath();
        ctx.arc(graphX + graphSize * 0.15, graphY + graphSize, graphSize * (0.8 - lvl * 0.006), 0, Math.PI * 0.4);
        ctx.stroke();
      }

      // Mark Transition State Saddle Point ‡
      ctx.fillStyle = '#fbbf24';
      ctx.beginPath();
      ctx.arc(saddleX, saddleY, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('[A···B···C]‡ (Transition State Saddle)', saddleX + 10, saddleY + 4);

      // Trajectory Dynamics
      animT += 0.025;
      var cycleT = animT % 6.0;

      var barrierThreshold = 32; // kJ/mol
      var willReact = (trajEnergy >= barrierThreshold);

      var trajX, trajY;
      if (cycleT < 3.0) {
        // Approaching transition state
        var p = cycleT / 3.0;
        trajX = (graphX + graphSize * 0.85) * (1 - p) + saddleX * p;
        trajY = (graphY + graphSize * 0.15) * (1 - p) + saddleY * p + Math.sin(cycleT * 12) * 8; // bond vibration
      } else {
        var p = (cycleT - 3.0) / 3.0;
        if (willReact) {
          // Reactive: crosses saddle into product valley
          trajX = saddleX * (1 - p) + (graphX + graphSize * 0.15) * p;
          trajY = saddleY * (1 - p) + (graphY + graphSize * 0.85) * p + Math.sin(cycleT * 12) * 8;
        } else {
          // Non-reactive: rebounds off repulsion wall
          trajX = saddleX * (1 - p) + (graphX + graphSize * 0.85) * p;
          trajY = saddleY * (1 - p) + (graphY + graphSize * 0.25) * p + Math.sin(cycleT * 12) * 8;
        }
      }

      // Draw Trajectory Path
      ctx.fillStyle = willReact ? '#22c55e' : '#f43f5e';
      ctx.beginPath();
      ctx.arc(trajX, trajY, 6, 0, Math.PI * 2);
      ctx.fill();

      // Right: Coordinate Energy Profile
      var profX = graphX + graphSize + 30, profW = W - profX - 40;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(profX, graphY, profW, graphSize);
      ctx.strokeRect(profX, graphY, profW, graphSize);

      ctx.fillStyle = '#f8fafc';
      ctx.fillText('1D Energy Profile along Reaction Coordinate', profX + 10, graphY + 20);

      // Potential energy barrier curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var s = 0; s <= profW - 40; s += 2) {
        var q = (s / (profW - 40)) * 2 - 1; // -1 to +1
        var v_pot = 32 * Math.exp(-q * q * 4); // Gaussian barrier
        var py = (graphY + graphSize - 40) - (v_pot / 60) * (graphSize - 80);
        if (s === 0) ctx.moveTo(profX + 20 + s, py);
        else ctx.lineTo(profX + 20 + s, py);
      }
      ctx.stroke();

      // Collision Energy Level Line
      var eY = (graphY + graphSize - 40) - (trajEnergy / 60) * (graphSize - 80);
      ctx.strokeStyle = willReact ? '#22c55e' : '#f43f5e';
      ctx.setLineDash([4, 3]);
      ctx.beginPath();
      ctx.moveTo(profX + 20, eY);
      ctx.lineTo(profX + profW - 20, eY);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = willReact ? '#22c55e' : '#f43f5e';
      ctx.fillText(`E_coll = ${trajEnergy} kJ/mol (${willReact ? 'REACTIVE: Over Barrier' : 'INELASTIC: Rebound'})`, profX + 25, eY - 8);

      // Dashboard
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText('Reactants: A + BC (Valley: R_AB large, R_BC eq) → Products: AB + C (Valley: R_AB eq, R_BC large)', graphX, H - 15);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // window.SimulationEngine Mount Adapter
  // =========================================================================
  var SIM_TITLES = {
    sim_kin_maxwell_boltzmann_effusion: "Maxwell-Boltzmann Speed Distribution & Knudsen Effusion Simulator",
    sim_kin_electrolyte_ionic_mobility: "Electrolyte Ionic Mobility & Stokes Drift Simulator",
    sim_kin_fick_diffusion_brownian_walk: "Fickian Diffusion Gradient & Brownian Random Walk Simulator",
    sim_kin_integrated_rate_laws: "Integrated Rate Laws & Reaction Order Transformation Engine",
    sim_kin_arrhenius_activation_energy: "Arrhenius Activation Energy & Maxwellian Barrier Crossing",
    sim_kin_consecutive_reactions_ssa: "Consecutive Reactions & Steady-State Approximation (SSA) Engine",
    sim_kin_lindemann_pressure_falloff: "Lindemann-Hinshelwood Unimolecular Pressure Fall-off Simulator",
    sim_kin_branched_chain_explosion_peninsula: "Branched Chain Explosion Peninsula (H₂ + O₂) Simulator",
    sim_kin_michaelis_menten_inhibition: "Michaelis-Menten Enzyme Kinetics & Inhibition Modes Visualizer",
    sim_kin_potential_energy_surface_trajectory: "LEPS Potential Energy Surface Trajectory & Reaction Dynamics"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.KineticsSims || typeof window.KineticsSims[simType] !== 'function') {
      console.warn('Simulation type not found in KineticsSims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Reaction Kinetics Interactive Simulation";
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
      window.KineticsSims[simType](canvasId, controlsId);
    }, 50);
  };

})();
"""
    with open("molecular-motion-kinetics-sims.js", "w", encoding="utf-8") as f:
        f.write(code)
    print("Generated molecular-motion-kinetics-sims.js successfully!")

if __name__ == "__main__":
    generate_sims_js()
