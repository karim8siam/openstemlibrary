# -*- coding: utf-8 -*-
"""
generate_nuclear_sims.py
Generates nuclear-radiochemistry-sims.js containing 10 real-time 60 FPS Canvas simulations
for Nuclear and Radiochemistry (#47) mounted via window.SimulationEngine.
"""

def generate_sims_js():
    js_code = r'''// Nuclear and Radiochemistry Interactive Simulation Suite
// 10 Real-Time 60 FPS Canvas Engines for Nuclear and Radiochemistry (#47)
// Mounted via window.SimulationEngine.initSimulation(containerId, simType)

(function() {
  'use strict';

  window.NuclearSims = window.NuclearSims || {};

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
  // 1. Bateman Multi-Nuclide Decay Chain Simulator
  // =========================================================================
  window.NuclearSims.sim_nuc_decay_series_bateman = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var mode = 'transient'; // secular, transient, no_eq
    var tHalfA = 60; // hours
    var tHalfB = 6.0; // hours
    var tHalfC = 1e8; // stable or long
    var maxT = 150; // hours displayed
    var animT = 0;
    var isPlaying = true;
    var animId = null;

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:12px;">Equilibrium Regime:
          <select id="${controlsId}-mode" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:4px;">
            <option value="transient" selected>Transient Equilibrium (Mo-99 -> Tc-99m)</option>
            <option value="secular">Secular Equilibrium (Ra-226 -> Rn-222)</option>
            <option value="no_eq">No Equilibrium (Parent T1/2 < Daughter T1/2)</option>
          </select>
        </label>
        <button id="${controlsId}-play" style="background:#0284c7; color:#fff; border:none; padding:4px 12px; border-radius:4px; cursor:pointer; font-size:12px;">Pause</button>
        <button id="${controlsId}-reset" style="background:#334155; color:#fff; border:none; padding:4px 12px; border-radius:4px; cursor:pointer; font-size:12px;">Reset</button>
      `;

      var modeSelect = document.getElementById(controlsId + '-mode');
      var playBtn = document.getElementById(controlsId + '-play');
      var resetBtn = document.getElementById(controlsId + '-reset');

      modeSelect.addEventListener('change', function(e) {
        mode = e.target.value;
        if (mode === 'transient') {
          tHalfA = 66.0;
          tHalfB = 6.0;
          maxT = 180;
        } else if (mode === 'secular') {
          tHalfA = 1600.0;
          tHalfB = 3.82;
          maxT = 30; // days
        } else {
          tHalfA = 4.0;
          tHalfB = 18.0;
          maxT = 50;
        }
        animT = 0;
      });

      playBtn.addEventListener('click', function() {
        isPlaying = !isPlaying;
        playBtn.textContent = isPlaying ? 'Pause' : 'Play';
      });

      resetBtn.addEventListener('click', function() {
        animT = 0;
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      var padL = 60, padR = 30, padT = 40, padB = 50;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      var lamA = Math.LN2 / tHalfA;
      var lamB = Math.LN2 / tHalfB;
      var N0 = 1000;

      // Draw Axes
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padL, padT);
      ctx.lineTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      // Axis labels
      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText('Activity A(t) [Bq / Relative]', padL - 10, padT + 10);
      ctx.textAlign = 'center';
      var timeUnit = (mode === 'secular') ? 'Days' : 'Hours';
      ctx.fillText(`Time Elapsed (${timeUnit})`, padL + plotW / 2, padT + plotH + 35);

      // Max Activity for scale
      var maxAct = lamA * N0;
      if (mode === 'transient') maxAct = lamA * N0 * 1.3;
      if (mode === 'secular') maxAct = lamA * N0 * 1.2;
      if (mode === 'no_eq') maxAct = lamA * N0;

      // Draw Curves
      function getActivities(t) {
        var NA = N0 * Math.exp(-lamA * t);
        var NB = 0;
        if (Math.abs(lamB - lamA) > 1e-9) {
          NB = N0 * (lamA / (lamB - lamA)) * (Math.exp(-lamA * t) - Math.exp(-lamB * t));
        } else {
          NB = N0 * lamA * t * Math.exp(-lamA * t);
        }
        var actA = lamA * NA;
        var actB = lamB * NB;
        var actTotal = actA + actB;
        return { actA: actA, actB: actB, actTotal: actTotal };
      }

      // Plot Curves
      ctx.lineWidth = 2.5;

      // Parent Activity (Blue)
      ctx.strokeStyle = '#38bdf8';
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var t = (px / plotW) * maxT;
        var act = getActivities(t).actA;
        var py = padT + plotH - (act / maxAct) * plotH;
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // Daughter Activity (Emerald)
      ctx.strokeStyle = '#10b981';
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var t = (px / plotW) * maxT;
        var act = getActivities(t).actB;
        var py = padT + plotH - (act / maxAct) * plotH;
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // Total Activity (Amber dashed)
      ctx.strokeStyle = '#f59e0b';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var t = (px / plotW) * maxT;
        var act = getActivities(t).actTotal;
        var py = padT + plotH - (act / maxAct) * plotH;
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Time cursor
      var curX = padL + (animT / maxT) * plotW;
      ctx.strokeStyle = '#e2e8f0';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(curX, padT);
      ctx.lineTo(curX, padT + plotH);
      ctx.stroke();

      var currentActs = getActivities(animT);

      // Legend & HUD
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(padL + 15, padT + 15, 290, 115);
      ctx.strokeRect(padL + 15, padT + 15, 290, 115);

      ctx.font = 'bold 12px monospace';
      ctx.textAlign = 'left';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`Parent A_1(t): ${(currentActs.actA).toFixed(3)} Bq (T1/2 = ${tHalfA})`, padL + 25, padT + 35);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Daughter A_2(t): ${(currentActs.actB).toFixed(3)} Bq (T1/2 = ${tHalfB})`, padL + 25, padT + 55);
      ctx.fillStyle = '#f59e0b';
      ctx.fillText(`Total A_tot(t): ${(currentActs.actTotal).toFixed(3)} Bq`, padL + 25, padT + 75);
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px sans-serif';
      var ratio = (currentActs.actB / (currentActs.actA || 1e-9)).toFixed(3);
      ctx.fillText(`Activity Ratio A_2 / A_1 = ${ratio}`, padL + 25, padT + 95);
      ctx.fillText(`Time t = ${animT.toFixed(1)} ${timeUnit}`, padL + 25, padT + 115);

      if (isPlaying) {
        animT += (maxT / 600);
        if (animT > maxT) animT = 0;
      }
      animId = requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 2. Semi-Empirical Mass Formula (SEMF) Binding Energy Curve
  // =========================================================================
  window.NuclearSims.sim_nuc_binding_energy_curve = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    // SEMF coefficients in MeV
    var av = 15.75;
    var as = 17.8;
    var ac = 0.711;
    var aa = 23.7;
    var ap = 11.18;

    var selectedA = 56; // Default Fe-56

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:12px;">Mass Number (A):
          <input type="range" id="${controlsId}-slider" min="1" max="250" value="56" style="margin-left:4px; vertical-align:middle; width:140px;">
          <span id="${controlsId}-val" style="color:#38bdf8; font-family:monospace; margin-left:4px;">A = 56</span>
        </label>
        <button id="${controlsId}-he4" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:3px 8px; border-radius:4px; cursor:pointer; font-size:11px;">He-4</button>
        <button id="${controlsId}-fe56" style="background:#0284c7; color:#fff; border:none; padding:3px 8px; border-radius:4px; cursor:pointer; font-size:11px;">Fe-56</button>
        <button id="${controlsId}-u238" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:3px 8px; border-radius:4px; cursor:pointer; font-size:11px;">U-238</button>
      `;

      var slider = document.getElementById(controlsId + '-slider');
      var valSpan = document.getElementById(controlsId + '-val');
      var btnHe = document.getElementById(controlsId + '-he4');
      var btnFe = document.getElementById(controlsId + '-fe56');
      var btnU = document.getElementById(controlsId + '-u238');

      function update(val) {
        selectedA = parseInt(val, 10);
        slider.value = selectedA;
        valSpan.textContent = `A = ${selectedA}`;
      }

      slider.addEventListener('input', function(e) { update(e.target.value); });
      btnHe.addEventListener('click', function() { update(4); });
      btnFe.addEventListener('click', function() { update(56); });
      btnU.addEventListener('click', function() { update(238); });
    }

    function calcSEMF(A) {
      if (A <= 1) return { B_per_A: 0, B: 0, vol: 0, surf: 0, coul: 0, asym: 0, pair: 0 };
      // Green's formula approximation for stable valley Z
      var Z = Math.round(A / (2 + 0.015 * Math.pow(A, 2/3)));
      if (Z < 1) Z = 1;
      var N = A - Z;

      var vol = av * A;
      var surf = -as * Math.pow(A, 2/3);
      var coul = -ac * (Z * (Z - 1)) / Math.pow(A, 1/3);
      var asym = -aa * Math.pow(A - 2 * Z, 2) / A;
      var delta = 0;
      if (Z % 2 === 0 && N % 2 === 0) delta = ap / Math.pow(A, 0.5);
      else if (Z % 2 !== 0 && N % 2 !== 0) delta = -ap / Math.pow(A, 0.5);

      var B = vol + surf + coul + asym + delta;
      if (B < 0) B = 0;
      return {
        Z: Z,
        N: N,
        B: B,
        B_per_A: B / A,
        vol_A: vol / A,
        surf_A: surf / A,
        coul_A: coul / A,
        asym_A: asym / A,
        pair_A: delta / A
      };
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      var padL = 60, padR = 40, padT = 30, padB = 50;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padL, padT);
      ctx.lineTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText('Binding Energy / Nucleon (B/A) [MeV]', padL - 10, padT + 10);
      ctx.textAlign = 'center';
      ctx.fillText('Mass Number A (Nucleons)', padL + plotW / 2, padT + plotH + 35);

      // Y-axis ticks (0 to 10 MeV)
      for (var meV = 0; meV <= 10; meV += 2) {
        var py = padT + plotH - (meV / 10) * plotH;
        ctx.strokeStyle = '#334155';
        ctx.beginPath();
        ctx.moveTo(padL - 4, py);
        ctx.lineTo(padL, py);
        ctx.stroke();
        ctx.fillText(meV.toString(), padL - 12, py + 4);
      }

      // Curve of B/A
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (var a = 2; a <= 250; a++) {
        var res = calcSEMF(a);
        var px = padL + (a / 250) * plotW;
        var py = padT + plotH - (res.B_per_A / 10) * plotH;
        if (a === 2) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Shaded Fission and Fusion regimes
      ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
      ctx.fillRect(padL, padT, (56 / 250) * plotW, plotH);
      ctx.fillStyle = 'rgba(239, 68, 68, 0.08)';
      ctx.fillRect(padL + (56 / 250) * plotW, padT, ((250 - 56) / 250) * plotW, plotH);

      ctx.font = '11px sans-serif';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('← Nuclear Fusion Regime (Exothermic)', padL + 80, padT + plotH - 20);
      ctx.fillStyle = '#ef4444';
      ctx.fillText('Nuclear Fission Regime (Exothermic) →', padL + plotW - 130, padT + plotH - 20);

      // Selected point
      var selRes = calcSEMF(selectedA);
      var selPx = padL + (selectedA / 250) * plotW;
      var selPy = padT + plotH - (selRes.B_per_A / 10) * plotH;

      ctx.strokeStyle = '#f59e0b';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(selPx, padT);
      ctx.lineTo(selPx, padT + plotH);
      ctx.moveTo(padL, selPy);
      ctx.lineTo(selPx, selPy);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(selPx, selPy, 6, 0, Math.PI * 2);
      ctx.fill();

      // Info HUD
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(padL + plotW - 280, padT + 15, 270, 150);
      ctx.strokeRect(padL + plotW - 280, padT + 15, 270, 150);

      ctx.textAlign = 'left';
      ctx.font = 'bold 12px monospace';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText(`Nuclide A = ${selectedA} (Z = ${selRes.Z}, N = ${selRes.N})`, padL + plotW - 270, padT + 35);
      ctx.fillStyle = '#f59e0b';
      ctx.fillText(`B/A = ${selRes.B_per_A.toFixed(3)} MeV/nucleon`, padL + plotW - 270, padT + 55);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Total B = ${selRes.B.toFixed(1)} MeV`, padL + plotW - 270, padT + 75);
      ctx.fillText(`Volume Term:    +${(selRes.vol_A).toFixed(2)} MeV`, padL + plotW - 270, padT + 93);
      ctx.fillText(`Surface Term:   ${(selRes.surf_A).toFixed(2)} MeV`, padL + plotW - 270, padT + 109);
      ctx.fillText(`Coulomb Term:   ${(selRes.coul_A).toFixed(2)} MeV`, padL + plotW - 270, padT + 125);
      ctx.fillText(`Asymmetry Term: ${(selRes.asym_A).toFixed(2)} MeV`, padL + plotW - 270, padT + 141);
      ctx.fillText(`Pairing Term:   ${(selRes.pair_A >= 0 ? '+' : '') + (selRes.pair_A).toFixed(2)} MeV`, padL + plotW - 270, padT + 157);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 3. Nuclear Reaction Kinematics & Breit-Wigner Cross Section Simulator
  // =========================================================================
  window.NuclearSims.sim_nuc_reaction_cross_section_q = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var reactionType = 'exo'; // 'exo' or 'endo'
    var resE = 4.2; // resonance energy in MeV
    var gamma = 0.6; // resonance width MeV
    var sigma0 = 120; // peak barns

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:12px;">Kinematic Channel:
          <select id="${controlsId}-type" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:4px;">
            <option value="exo" selected>Exothermic: Li-7(p, alpha)He-4 (Q = +17.35 MeV)</option>
            <option value="endo">Endothermic: C-12(alpha, n)O-15 (Q = -8.51 MeV, Eth = 11.35 MeV)</option>
            <option value="neutron">Resonance Capture: In-115(n, gamma)In-116 (E_res = 1.46 eV)</option>
          </select>
        </label>
      `;

      var select = document.getElementById(controlsId + '-type');
      select.addEventListener('change', function(e) {
        reactionType = e.target.value;
        if (reactionType === 'exo') {
          resE = 3.5;
          gamma = 0.8;
          sigma0 = 150;
        } else if (reactionType === 'endo') {
          resE = 12.0;
          gamma = 1.2;
          sigma0 = 80;
        } else {
          resE = 1.46;
          gamma = 0.15;
          sigma0 = 26000;
        }
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      var padL = 70, padR = 40, padT = 30, padB = 50;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      var maxE = (reactionType === 'endo') ? 20.0 : (reactionType === 'neutron' ? 4.0 : 8.0);
      var maxSigma = (reactionType === 'neutron') ? 30000 : 200;

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padL, padT);
      ctx.lineTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText('Cross Section sigma(E) [barns]', padL - 10, padT + 10);
      ctx.textAlign = 'center';
      var eUnit = (reactionType === 'neutron') ? 'eV' : 'MeV';
      ctx.fillText(`Incident Projectile Laboratory Kinetic Energy (${eUnit})`, padL + plotW / 2, padT + plotH + 35);

      // Threshold line for endothermic
      if (reactionType === 'endo') {
        var ethX = padL + (11.35 / maxE) * plotW;
        ctx.fillStyle = 'rgba(239, 68, 68, 0.15)';
        ctx.fillRect(padL, padT, ethX - padL, plotH);
        ctx.strokeStyle = '#ef4444';
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(ethX, padT);
        ctx.lineTo(ethX, padT + plotH);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#ef4444';
        ctx.font = '11px sans-serif';
        ctx.fillText('Kinematic Threshold E_th = 11.35 MeV (sigma = 0)', ethX + 100, padT + 30);
      }

      // Draw Breit-Wigner Curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      for (var px = 0; px <= plotW; px += 2) {
        var E = (px / plotW) * maxE;
        var sig = 0;
        if (reactionType === 'endo' && E < 11.35) {
          sig = 0;
        } else {
          // Breit-Wigner formula
          var num = (gamma * gamma) / 4;
          var denom = Math.pow(E - resE, 2) + (gamma * gamma) / 4;
          sig = sigma0 * (num / denom);
          // 1/v thermal background if neutron
          if (reactionType === 'neutron' && E > 0.05) {
            sig += 200 / Math.sqrt(E);
          }
        }
        var py = padT + plotH - (sig / maxSigma) * plotH;
        if (py < padT) py = padT;
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // Info HUD
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(padL + plotW - 320, padT + 20, 310, 120);
      ctx.strokeRect(padL + plotW - 320, padT + 20, 310, 120);

      ctx.textAlign = 'left';
      ctx.font = 'bold 12px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('Breit-Wigner Single-Level Resonance:', padL + plotW - 310, padT + 40);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText(`sigma(E) = sigma_0 * [Gamma^2/4] / [(E - E_0)^2 + Gamma^2/4]`, padL + plotW - 310, padT + 58);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Resonance Peak E_0 = ${resE} ${eUnit}`, padL + plotW - 310, padT + 76);
      ctx.fillText(`Total Level Width Gamma = ${gamma} ${eUnit}`, padL + plotW - 310, padT + 94);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Peak Cross-Section sigma_0 = ${sigma0} b`, padL + plotW - 310, padT + 112);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 4. Nuclear Fission Chain Reaction & Reactor Criticality Simulator
  // =========================================================================
  window.NuclearSims.sim_nuc_fission_chain_reactor = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var kEff = 1.000; // Criticality factor
    var controlRodPos = 50; // percentage inserted (0% to 100%)
    var neutrons = [];
    var maxNeutrons = 350;
    var nuclei = [];
    var fissionEvents = [];

    // Initialize fuel lattice nuclei
    var gridCols = 10, gridRows = 6;
    for (var r = 0; r < gridRows; r++) {
      for (var c = 0; c < gridCols; c++) {
        nuclei.push({
          x: 80 + c * ((W - 160) / (gridCols - 1)),
          y: 70 + r * ((H - 140) / (gridRows - 1)),
          r: 12,
          isU235: Math.random() > 0.3
        });
      }
    }

    // Spawn initial seed neutrons
    function spawnNeutron(x, y, speed, angle) {
      if (neutrons.length >= maxNeutrons) return;
      var a = angle !== undefined ? angle : Math.random() * Math.PI * 2;
      var s = speed !== undefined ? speed : 2.5 + Math.random() * 2;
      neutrons.push({
        x: x,
        y: y,
        vx: Math.cos(a) * s,
        vy: Math.sin(a) * s,
        life: 0,
        maxLife: 200 + Math.random() * 100,
        thermal: Math.random() > 0.5
      });
    }

    for (var i = 0; i < 20; i++) {
      spawnNeutron(W / 2 + (Math.random() - 0.5) * 100, H / 2 + (Math.random() - 0.5) * 100);
    }

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:12px;">Control Rod Insertion:
          <input type="range" id="${controlsId}-rod" min="0" max="100" value="50" style="margin-left:4px; vertical-align:middle; width:130px;">
          <span id="${controlsId}-rod-val" style="color:#f59e0b; font-family:monospace; margin-left:4px;">50%</span>
        </label>
        <button id="${controlsId}-scram" style="background:#ef4444; color:#fff; border:none; padding:3px 10px; border-radius:4px; cursor:pointer; font-size:11px; font-weight:bold;">SCRAM</button>
        <button id="${controlsId}-pulse" style="background:#0284c7; color:#fff; border:none; padding:3px 10px; border-radius:4px; cursor:pointer; font-size:11px;">Inject Neutrons</button>
      `;

      var rodSlider = document.getElementById(controlsId + '-rod');
      var rodSpan = document.getElementById(controlsId + '-rod-val');
      var scramBtn = document.getElementById(controlsId + '-scram');
      var pulseBtn = document.getElementById(controlsId + '-pulse');

      function updateRod(val) {
        controlRodPos = parseInt(val, 10);
        rodSpan.textContent = `${controlRodPos}%`;
        // k_eff varies with control rod insertion (50% = 1.000, 0% = 1.05 super, 100% = 0.85 sub)
        kEff = 1.05 - (controlRodPos / 100) * 0.20;
      }

      rodSlider.addEventListener('input', function(e) { updateRod(e.target.value); });
      scramBtn.addEventListener('click', function() {
        rodSlider.value = 100;
        updateRod(100);
      });
      pulseBtn.addEventListener('click', function() {
        for (var n = 0; n < 25; n++) {
          spawnNeutron(W / 2 + (Math.random() - 0.5) * 60, H / 2 + (Math.random() - 0.5) * 60);
        }
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      // Draw Control Rods hanging from top
      var rodHeight = (controlRodPos / 100) * (H - 80);
      var rodCols = [180, 360, 540];
      ctx.fillStyle = 'rgba(71, 85, 105, 0.8)';
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 1.5;
      for (var rc = 0; rc < rodCols.length; rc++) {
        var rx = rodCols[rc];
        ctx.fillRect(rx - 8, 20, 16, rodHeight);
        ctx.strokeRect(rx - 8, 20, 16, rodHeight);
      }

      // Draw Fuel Lattice Nuclei
      for (var k = 0; k < nuclei.length; k++) {
        var nuc = nuclei[k];
        ctx.beginPath();
        ctx.arc(nuc.x, nuc.y, nuc.r, 0, Math.PI * 2);
        if (nuc.isU235) {
          ctx.fillStyle = '#0284c7'; // U-235
          ctx.strokeStyle = '#38bdf8';
        } else {
          ctx.fillStyle = '#334155'; // U-238
          ctx.strokeStyle = '#475569';
        }
        ctx.fill();
        ctx.stroke();
      }

      // Draw Fission Flash Explosions
      for (var f = fissionEvents.length - 1; f >= 0; f--) {
        var fe = fissionEvents[f];
        fe.life++;
        ctx.beginPath();
        ctx.arc(fe.x, fe.y, fe.life * 3, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(245, 158, 11, ${1 - fe.life / 20})`;
        ctx.lineWidth = 2;
        ctx.stroke();
        if (fe.life > 20) fissionEvents.splice(f, 1);
      }

      // Update & Draw Neutrons
      for (var i = neutrons.length - 1; i >= 0; i--) {
        var p = neutrons[i];
        p.x += p.vx;
        p.y += p.vy;
        p.life++;

        // Bounce at boundaries
        if (p.x < 10 || p.x > W - 10) p.vx *= -1;
        if (p.y < 10 || p.y > H - 10) p.vy *= -1;

        // Check absorption by control rods
        var absorbed = false;
        for (var rc = 0; rc < rodCols.length; rc++) {
          var rx = rodCols[rc];
          if (p.x >= rx - 8 && p.x <= rx + 8 && p.y >= 20 && p.y <= 20 + rodHeight) {
            absorbed = true;
            break;
          }
        }
        if (absorbed) {
          neutrons.splice(i, 1);
          continue;
        }

        // Check collision with nuclei
        for (var k = 0; k < nuclei.length; k++) {
          var target = nuclei[k];
          var distSq = (p.x - target.x) * (p.x - target.x) + (p.y - target.y) * (p.y - target.y);
          if (distSq < target.r * target.r) {
            if (target.isU235) {
              // Fission event!
              fissionEvents.push({ x: target.x, y: target.y, life: 0 });
              neutrons.splice(i, 1);
              // Spawn 2 to 3 prompt neutrons depending on k_eff
              var yieldCount = (kEff >= 1.0) ? (Math.random() > 0.4 ? 3 : 2) : (Math.random() > 0.6 ? 2 : 1);
              for (var n = 0; n < yieldCount; n++) {
                spawnNeutron(target.x, target.y);
              }
              absorbed = true;
              break;
            } else {
              // U-238 radiative capture or scatter
              if (Math.random() > 0.7) {
                neutrons.splice(i, 1);
                absorbed = true;
                break;
              } else {
                p.vx *= -1;
                p.vy *= -1;
              }
            }
          }
        }
        if (absorbed) continue;

        if (p.life > p.maxLife) {
          neutrons.splice(i, 1);
          continue;
        }

        // Draw neutron
        ctx.beginPath();
        ctx.arc(p.x, p.y, 2.5, 0, Math.PI * 2);
        ctx.fillStyle = p.thermal ? '#fbbf24' : '#38bdf8';
        ctx.fill();
      }

      // HUD Status Bar
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(20, 20, 240, 100);
      ctx.strokeRect(20, 20, 240, 100);

      ctx.textAlign = 'left';
      ctx.font = 'bold 12px monospace';
      var stateColor = Math.abs(kEff - 1.0) < 0.01 ? '#10b981' : (kEff > 1.01 ? '#ef4444' : '#0284c7');
      var stateName = Math.abs(kEff - 1.0) < 0.01 ? 'CRITICAL (k = 1.000)' : (kEff > 1.01 ? 'SUPERCRITICAL (Power Rising)' : 'SUBCRITICAL (Power Falling)');
      ctx.fillStyle = stateColor;
      ctx.fillText(stateName, 30, 40);

      ctx.font = '11px monospace';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText(`k_eff = ${kEff.toFixed(4)}`, 30, 60);
      ctx.fillText(`Active Neutrons: ${neutrons.length} / ${maxNeutrons}`, 30, 78);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Control Rods: ${controlRodPos}% Depth`, 30, 96);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 5. Heavy Charged Particle Bethe-Bloch & Bragg Peak Simulator
  // =========================================================================
  window.NuclearSims.sim_nuc_bragg_peak_stopping_power = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var ionType = 'alpha'; // 'alpha' or 'proton' or 'electron'
    var medium = 'tissue'; // 'tissue' or 'air' or 'aluminum'

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:12px;">Radiation Particle:
          <select id="${controlsId}-ion" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:4px;">
            <option value="alpha" selected>Alpha Particle (5.49 MeV from Am-241)</option>
            <option value="proton">Proton (60 MeV Hadrontherapy Beam)</option>
            <option value="electron">Beta Electron (1.5 MeV Continuous Loss)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:12px; margin-left:10px;">Absorber Medium:
          <select id="${controlsId}-med" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:4px;">
            <option value="tissue" selected>Biological Soft Tissue</option>
            <option value="air">Atmospheric Air</option>
            <option value="aluminum">Solid Aluminum</option>
          </select>
        </label>
      `;

      var ionSel = document.getElementById(controlsId + '-ion');
      var medSel = document.getElementById(controlsId + '-med');

      ionSel.addEventListener('change', function(e) { ionType = e.target.value; });
      medSel.addEventListener('change', function(e) { medium = e.target.value; });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      var padL = 70, padR = 40, padT = 30, padB = 50;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padL, padT);
      ctx.lineTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText('Stopping Power -dE/dx [MeV / cm]', padL - 10, padT + 10);
      ctx.textAlign = 'center';
      var depthUnit = (medium === 'air') ? 'cm' : 'mm';
      ctx.fillText(`Penetration Depth in ${medium.toUpperCase()} (${depthUnit})`, padL + plotW / 2, padT + plotH + 35);

      // Bragg Peak Curve Calculation
      var peakDepthNorm = (ionType === 'alpha') ? 0.82 : (ionType === 'proton' ? 0.75 : 0.0);
      var maxPeak = 100;

      ctx.lineWidth = 3;
      ctx.strokeStyle = (ionType === 'alpha') ? '#38bdf8' : (ionType === 'proton' ? '#10b981' : '#f59e0b');
      ctx.beginPath();

      for (var px = 0; px <= plotW; px += 2) {
        var normX = px / plotW;
        var yVal = 0;
        if (ionType === 'electron') {
          // Exponential decay / broad plateau
          yVal = 30 * Math.exp(-normX * 3.5) + 10;
        } else {
          // Sharp Bragg Peak
          if (normX < peakDepthNorm) {
            yVal = 20 + 75 * Math.pow(normX / peakDepthNorm, 4);
          } else if (normX <= peakDepthNorm + 0.05) {
            var drop = (normX - peakDepthNorm) / 0.05;
            yVal = 95 * (1 - drop);
          } else {
            yVal = 0;
          }
        }

        var py = padT + plotH - (yVal / maxPeak) * plotH;
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // Peak Highlight
      if (ionType !== 'electron') {
        var braggPx = padL + peakDepthNorm * plotW;
        var braggPy = padT + plotH - (95 / maxPeak) * plotH;

        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(braggPx, braggPy, 5, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('BRAGG PEAK (Maximum Dose Deposition)', braggPx, braggPy - 12);
      }

      // HUD Panel
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(padL + 20, padT + 15, 300, 105);
      ctx.strokeRect(padL + 20, padT + 15, 300, 105);

      ctx.textAlign = 'left';
      ctx.font = 'bold 12px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('Bethe-Bloch Equation Formalism:', padL + 30, padT + 35);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText('-dE/dx = 4*pi*r_e^2 * m_e*c^2 * z^2 * n / beta^2', padL + 30, padT + 53);
      ctx.fillText('       * [ln(2*m_e*c^2*beta^2*gamma^2 / I) - beta^2]', padL + 30, padT + 69);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('As particle slows (beta -> 0), stopping power climbs', padL + 30, padT + 87);
      ctx.fillText('drastically until final rest (Bragg ionization peak).', padL + 30, padT + 103);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 6. Gamma-Ray Interaction Cross-Section Engine
  // =========================================================================
  window.NuclearSims.sim_nuc_gamma_interaction_modes = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var targetZ = 82; // Lead (Pb)

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:12px;">Absorber Material (Z):
          <select id="${controlsId}-mat" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:4px;">
            <option value="82" selected>Lead (Pb, Z = 82)</option>
            <option value="26">Iron (Fe, Z = 26)</option>
            <option value="13">Aluminum (Al, Z = 13)</option>
          </select>
        </label>
      `;

      var matSel = document.getElementById(controlsId + '-mat');
      matSel.addEventListener('change', function(e) {
        targetZ = parseInt(e.target.value, 10);
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      var padL = 70, padR = 40, padT = 30, padB = 50;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      // Log-log plot: E from 0.01 MeV to 100 MeV
      // mu/rho from 0.01 to 100 cm2/g
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padL, padT);
      ctx.lineTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText('Mass Attenuation mu/rho [cm^2/g]', padL - 10, padT + 10);
      ctx.textAlign = 'center';
      ctx.fillText('Photon Energy h*nu [MeV] (Log Scale: 0.01 to 100 MeV)', padL + plotW / 2, padT + plotH + 35);

      function logEToPx(E) {
        var logE = Math.log10(E);
        var norm = (logE - (-2)) / 4; // -2 to 2 (0.01 to 100)
        return padL + norm * plotW;
      }

      function logMuToPy(mu) {
        var logMu = Math.log10(Math.max(1e-3, mu));
        var norm = (logMu - (-2)) / 4; // -2 to 2 (0.01 to 100)
        return padT + plotH - norm * plotH;
      }

      // Calculate 3 modes for energy E
      function getMu(E) {
        // Photoelectric: ~ Z^4 to Z^5 / E^3
        var tau = 0.02 * Math.pow(targetZ / 82, 4.5) / Math.pow(E, 3.2);
        if (tau > 500) tau = 500;

        // Compton: ~ Z / E
        var sigmaC = (0.2 * (targetZ / 82)) / (1 + 2 * E);

        // Pair Production: 0 if E < 1.022 MeV, then ln(E)
        var kappa = 0;
        if (E > 1.022) {
          kappa = 0.04 * Math.pow(targetZ / 82, 2) * Math.log(E / 1.022);
        }

        var total = tau + sigmaC + kappa;
        return { tau: tau, compton: sigmaC, pair: kappa, total: total };
      }

      // Draw Curves
      // 1. Photoelectric (Violet)
      ctx.strokeStyle = '#a855f7';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var norm = px / plotW;
        var E = Math.pow(10, -2 + norm * 4);
        var py = logMuToPy(getMu(E).tau);
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // 2. Compton Scattering (Emerald)
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var norm = px / plotW;
        var E = Math.pow(10, -2 + norm * 4);
        var py = logMuToPy(getMu(E).compton);
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // 3. Pair Production (Amber)
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 2;
      ctx.beginPath();
      var started = false;
      for (var px = 0; px <= plotW; px += 2) {
        var norm = px / plotW;
        var E = Math.pow(10, -2 + norm * 4);
        if (E >= 1.022) {
          var py = logMuToPy(getMu(E).pair);
          if (!started) { ctx.moveTo(padL + px, py); started = true; }
          else ctx.lineTo(padL + px, py);
        }
      }
      ctx.stroke();

      // 4. Total Attenuation (Cyan Bold)
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var norm = px / plotW;
        var E = Math.pow(10, -2 + norm * 4);
        var py = logMuToPy(getMu(E).total);
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // 1.022 MeV Threshold line
      var pPairTh = logEToPx(1.022);
      ctx.strokeStyle = '#f59e0b';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(pPairTh, padT);
      ctx.lineTo(pPairTh, padT + plotH);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#f59e0b';
      ctx.font = '10px sans-serif';
      ctx.fillText('2 m_e c^2 = 1.022 MeV', pPairTh + 60, padT + plotH - 20);

      // Legend
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(padL + plotW - 270, padT + 15, 260, 110);
      ctx.strokeRect(padL + plotW - 270, padT + 15, 260, 110);

      ctx.textAlign = 'left';
      ctx.font = 'bold 11px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('— Total Mass Attenuation mu/rho', padL + plotW - 260, padT + 33);
      ctx.fillStyle = '#a855f7';
      ctx.fillText('— Photoelectric Effect (Low E, ~Z^5)', padL + plotW - 260, padT + 53);
      ctx.fillStyle = '#10b981';
      ctx.fillText('— Compton Scattering (Mid E, ~Z)', padL + plotW - 260, padT + 73);
      ctx.fillStyle = '#f59e0b';
      ctx.fillText('— Pair Production (High E > 1.022 MeV)', padL + plotW - 260, padT + 93);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Target: Z = ${targetZ}`, padL + plotW - 260, padT + 113);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 7. Geiger-Müller Townsend Avalanche & Dead Time Simulator
  // =========================================================================
  window.NuclearSims.sim_nuc_geiger_muller_avalanche = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var highVoltage = 900; // Volts
    var deadTimeUs = 150; // microseconds
    var particles = [];
    var ionizations = [];
    var isDischarge = false;
    var dischargeTimer = 0;

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:12px;">Operating High Voltage:
          <input type="range" id="${controlsId}-volt" min="400" max="1400" step="50" value="900" style="margin-left:4px; vertical-align:middle; width:120px;">
          <span id="${controlsId}-volt-val" style="color:#38bdf8; font-family:monospace; margin-left:4px;">900 V</span>
        </label>
        <button id="${controlsId}-ion" style="background:#0284c7; color:#fff; border:none; padding:3px 10px; border-radius:4px; cursor:pointer; font-size:11px;">Trigger Primary Ionization</button>
      `;

      var voltSlider = document.getElementById(controlsId + '-volt');
      var voltSpan = document.getElementById(controlsId + '-volt-val');
      var ionBtn = document.getElementById(controlsId + '-ion');

      voltSlider.addEventListener('input', function(e) {
        highVoltage = parseInt(e.target.value, 10);
        voltSpan.textContent = `${highVoltage} V`;
      });

      ionBtn.addEventListener('click', function() {
        triggerEvent();
      });
    }

    function triggerEvent() {
      if (isDischarge) return; // In dead time!
      isDischarge = true;
      dischargeTimer = 60; // frames
      // Create electron cascade towards central anode
      for (var i = 0; i < 40; i++) {
        var angle = Math.random() * Math.PI * 2;
        var r = 120 + (Math.random() - 0.5) * 30;
        particles.push({
          x: W / 2 + Math.cos(angle) * r,
          y: H / 2 + Math.sin(angle) * r,
          angle: angle,
          r: r,
          type: 'electron',
          life: 0
        });
      }
    }

    function render() {
      clearCanvas(ctx, W, H);

      // Tube Cross-section (Cylindrical Cathode & Central Anode Wire)
      var cx = W / 2, cy = H / 2;
      var cathodeRadius = 150;
      var anodeRadius = 4;

      // Cathode cylinder wall
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.arc(cx, cy, cathodeRadius, 0, Math.PI * 2);
      ctx.stroke();

      // Gas region fill
      ctx.fillStyle = isDischarge ? 'rgba(56, 189, 248, 0.12)' : 'rgba(15, 23, 42, 0.4)';
      ctx.beginPath();
      ctx.arc(cx, cy, cathodeRadius, 0, Math.PI * 2);
      ctx.fill();

      // Central Anode Wire (+HV)
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(cx, cy, anodeRadius, 0, Math.PI * 2);
      ctx.fill();

      // Radial E-field lines
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
      ctx.lineWidth = 1;
      for (var a = 0; a < Math.PI * 2; a += Math.PI / 8) {
        ctx.beginPath();
        ctx.moveTo(cx + Math.cos(a) * anodeRadius, cy + Math.sin(a) * anodeRadius);
        ctx.lineTo(cx + Math.cos(a) * cathodeRadius, cy + Math.sin(a) * cathodeRadius);
        ctx.stroke();
      }

      // Update particles
      for (var i = particles.length - 1; i >= 0; i--) {
        var p = particles[i];
        p.r -= 4.5 * (highVoltage / 800); // Accelerate inward to anode wire
        p.x = cx + Math.cos(p.angle) * p.r;
        p.y = cy + Math.sin(p.angle) * p.r;
        p.life++;

        ctx.beginPath();
        ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
        ctx.fillStyle = '#38bdf8';
        ctx.fill();

        if (p.r <= anodeRadius + 2) {
          particles.splice(i, 1);
        }
      }

      if (isDischarge) {
        dischargeTimer--;
        if (dischargeTimer <= 0) isDischarge = false;
      }

      // HUD
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(20, 20, 280, 115);
      ctx.strokeRect(20, 20, 280, 115);

      ctx.textAlign = 'left';
      ctx.font = 'bold 12px monospace';
      ctx.fillStyle = highVoltage >= 800 && highVoltage <= 1200 ? '#10b981' : (highVoltage < 800 ? '#f59e0b' : '#ef4444');
      var regime = highVoltage < 600 ? 'Proportional Region' : (highVoltage < 800 ? 'Limited Proportionality' : (highVoltage <= 1200 ? 'Geiger-Müller Plateau' : 'Continuous Glow Discharge'));
      ctx.fillText(regime, 30, 40);

      ctx.font = '11px monospace';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText(`Cathode Radius: 15.0 mm | Anode: 0.05 mm`, 30, 60);
      ctx.fillText(`Electric Field E(r) = V / [r * ln(b/a)]`, 30, 78);
      ctx.fillStyle = isDischarge ? '#ef4444' : '#94a3b8';
      ctx.fillText(`Detector Status: ${isDischarge ? 'DEAD TIME (Insensitive)' : 'READY FOR COUNTING'}`, 30, 96);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Resolving Time tau: ~${deadTimeUs} microseconds`, 30, 114);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 8. HPGe vs NaI(Tl) Multichannel Analyzer Gamma Spectroscopy Simulator
  // =========================================================================
  window.NuclearSims.sim_nuc_hpge_gamma_spectroscopy = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var detector = 'hpge'; // 'hpge' or 'nai'
    var source = 'cs137'; // 'cs137' or 'co60'

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:12px;">Detector Type:
          <select id="${controlsId}-det" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:4px;">
            <option value="hpge" selected>HPGe Semiconductor (FWHM = 0.2% / Ultra-High Res)</option>
            <option value="nai">NaI(Tl) Scintillation (FWHM = 7.0% / Broad Peaks)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:12px; margin-left:10px;">Calibration Source:
          <select id="${controlsId}-src" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:4px;">
            <option value="cs137" selected>Cs-137 (E_gamma = 661.7 keV)</option>
            <option value="co60">Co-60 (E_gamma1 = 1173.2 keV, E_gamma2 = 1332.5 keV)</option>
          </select>
        </label>
      `;

      var detSel = document.getElementById(controlsId + '-det');
      var srcSel = document.getElementById(controlsId + '-src');

      detSel.addEventListener('change', function(e) { detector = e.target.value; });
      srcSel.addEventListener('change', function(e) { source = e.target.value; });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      var padL = 70, padR = 40, padT = 30, padB = 50;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      var maxEnergy = 1600; // keV
      var fwhmFrac = (detector === 'hpge') ? 0.005 : 0.07; // peak width

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padL, padT);
      ctx.lineTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText('Counts per Channel [MCA]', padL - 10, padT + 10);
      ctx.textAlign = 'center';
      ctx.fillText('Gamma-Ray Energy [keV]', padL + plotW / 2, padT + plotH + 35);

      // Energy ticks
      for (var eVal = 0; eVal <= 1600; eVal += 400) {
        var px = padL + (eVal / maxEnergy) * plotW;
        ctx.fillText(eVal.toString(), px, padT + plotH + 18);
      }

      function calcSpectrum(E) {
        var counts = 15; // baseline noise
        if (source === 'cs137') {
          var ePhoto = 661.7;
          var eComptonEdge = ePhoto * (1 - 1 / (1 + (2 * ePhoto / 511.0))); // ~477 keV
          // Compton continuum
          if (E < eComptonEdge) {
            counts += 120 / (1 + Math.exp((E - eComptonEdge) / 20));
          }
          // Backscatter peak at ~184 keV
          var sigmaBs = 184 * fwhmFrac;
          counts += 40 * Math.exp(-Math.pow(E - 184, 2) / (2 * sigmaBs * sigmaBs));
          // Photopeak
          var sigma = ePhoto * fwhmFrac;
          var peakAmp = (detector === 'hpge') ? 450 : 220;
          counts += peakAmp * Math.exp(-Math.pow(E - ePhoto, 2) / (2 * sigma * sigma));
        } else {
          // Co-60
          var ePhoto1 = 1173.2, ePhoto2 = 1332.5;
          var eEdge1 = 963, eEdge2 = 1118;
          if (E < eEdge2) counts += 100 / (1 + Math.exp((E - eEdge2) / 30));
          var sig1 = ePhoto1 * fwhmFrac;
          var sig2 = ePhoto2 * fwhmFrac;
          var peakAmp = (detector === 'hpge') ? 350 : 160;
          counts += peakAmp * Math.exp(-Math.pow(E - ePhoto1, 2) / (2 * sig1 * sig1));
          counts += peakAmp * Math.exp(-Math.pow(E - ePhoto2, 2) / (2 * sig2 * sig2));
        }
        return counts;
      }

      // Draw Spectrum Line
      ctx.strokeStyle = (detector === 'hpge') ? '#10b981' : '#38bdf8';
      ctx.lineWidth = 2;
      ctx.beginPath();
      var maxCounts = 500;
      for (var px = 0; px <= plotW; px += 2) {
        var E = (px / plotW) * maxEnergy;
        var c = calcSpectrum(E);
        var py = padT + plotH - (c / maxCounts) * plotH;
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // HUD Info
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(padL + 20, padT + 15, 290, 105);
      ctx.strokeRect(padL + 20, padT + 15, 290, 105);

      ctx.textAlign = 'left';
      ctx.font = 'bold 12px monospace';
      ctx.fillStyle = (detector === 'hpge') ? '#10b981' : '#38bdf8';
      ctx.fillText(`Detector: ${detector === 'hpge' ? 'HPGe Semiconductor' : 'NaI(Tl) Scintillator'}`, padL + 30, padT + 35);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText(`FWHM Resolution: ${detector === 'hpge' ? '1.8 keV (0.27%) @ 662 keV' : '46 keV (7.0%) @ 662 keV'}`, padL + 30, padT + 53);
      ctx.fillText(`Source: ${source === 'cs137' ? 'Cs-137 (Single 662 keV Line)' : 'Co-60 (Doublet 1173 & 1332 keV)'}`, padL + 30, padT + 71);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Fano Factor F = ${detector === 'hpge' ? '0.08 (Germanium)' : 'N/A (Scintillation Process)'}`, padL + 30, padT + 89);
      ctx.fillText(`Photopeak vs Compton Edge clearly delineated.`, padL + 30, padT + 107);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 9. Neutron Activation Analysis (NAA) Irradiation & Decay Kinetics Engine
  // =========================================================================
  window.NuclearSims.sim_nuc_neutron_activation_analysis = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var fluxExp = 12; // 10^12 n / cm2 s
    var target = 'al27'; // Al-27 -> Al-28 (T1/2 = 2.24 min) or Au-197 -> Au-198 (T1/2 = 2.7 days)
    var tirr = 10; // min
    var tcool = 5; // min

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:12px;">Thermal Neutron Flux:
          <select id="${controlsId}-flux" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:4px;">
            <option value="12" selected>Medium Flux: 10^12 n/(cm^2*s)</option>
            <option value="14">High Flux (Research Reactor): 10^14 n/(cm^2*s)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:12px; margin-left:10px;">Target Nucleus:
          <select id="${controlsId}-nuclide" style="background:#1e293b; color:#f8fafc; border:1px solid #334155; padding:4px 8px; border-radius:4px; margin-left:4px;">
            <option value="al27" selected>Al-27(n,gamma)Al-28 (T1/2 = 2.24 min)</option>
            <option value="au197">Au-197(n,gamma)Au-198 (T1/2 = 2.70 days)</option>
          </select>
        </label>
      `;

      var fluxSel = document.getElementById(controlsId + '-flux');
      var nucSel = document.getElementById(controlsId + '-nuclide');

      fluxSel.addEventListener('change', function(e) { fluxExp = parseInt(e.target.value, 10); });
      nucSel.addEventListener('change', function(e) { target = e.target.value; });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      var padL = 70, padR = 40, padT = 30, padB = 50;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padL, padT);
      ctx.lineTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText('Induced Activity A(t) [kBq]', padL - 10, padT + 10);
      ctx.textAlign = 'center';
      var tUnit = (target === 'al27') ? 'Minutes' : 'Days';
      ctx.fillText(`Process Time Elapsed (${tUnit})`, padL + plotW / 2, padT + plotH + 35);

      var tHalf = (target === 'al27') ? 2.24 : 2.70;
      var lambda = Math.LN2 / tHalf;
      var maxTotalT = tHalf * 6;
      var tirrEnd = maxTotalT * 0.45;

      var asat = (fluxExp === 12) ? 100 : 350;

      // Plot Activation (Irradiation) + Cooling decay
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.beginPath();

      var tirrPx = padL + (tirrEnd / maxTotalT) * plotW;

      for (var px = 0; px <= plotW; px += 2) {
        var t = (px / plotW) * maxTotalT;
        var act = 0;
        if (t <= tirrEnd) {
          // Saturation curve: A(t) = A_sat * (1 - e^(-lambda * t))
          act = asat * (1 - Math.exp(-lambda * t));
        } else {
          // Cooling decay: A(t) = A(tirrEnd) * e^(-lambda * (t - tirrEnd))
          var aEnd = asat * (1 - Math.exp(-lambda * tirrEnd));
          act = aEnd * Math.exp(-lambda * (t - tirrEnd));
        }
        var py = padT + plotH - (act / (asat * 1.1)) * plotH;
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // Delineate Irradiation vs Cooling
      ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
      ctx.fillRect(padL, padT, tirrPx - padL, plotH);
      ctx.fillStyle = 'rgba(16, 185, 129, 0.08)';
      ctx.fillRect(tirrPx, padT, padL + plotW - tirrPx, plotH);

      ctx.strokeStyle = '#94a3b8';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(tirrPx, padT);
      ctx.lineTo(tirrPx, padT + plotH);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '11px sans-serif';
      ctx.fillText('← Reactor Irradiation Phase', padL + (tirrPx - padL) / 2, padT + 25);
      ctx.fillStyle = '#10b981';
      ctx.fillText('Cooling & Counting Phase →', tirrPx + (padL + plotW - tirrPx) / 2, padT + 25);

      // HUD Panel
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(padL + plotW - 320, padT + 45, 310, 105);
      ctx.strokeRect(padL + plotW - 320, padT + 45, 310, 105);

      ctx.textAlign = 'left';
      ctx.font = 'bold 12px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('NAA Master Activation Equation:', padL + plotW - 310, padT + 65);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText('A(t_irr) = N * sigma * Phi * [1 - exp(-lambda*t_irr)]', padL + plotW - 310, padT + 83);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Target: ${target.toUpperCase()} | Half-life T1/2 = ${tHalf} ${tUnit}`, padL + plotW - 310, padT + 101);
      ctx.fillText(`Saturation Activity A_sat = ${asat.toFixed(0)} kBq`, padL + plotW - 310, padT + 119);
      ctx.fillText(`Cooling Factor = exp(-lambda * t_cool)`, padL + plotW - 310, padT + 137);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 10. Mo-99 / Tc-99m Radioisotope Generator Elution Engine
  // =========================================================================
  window.NuclearSims.sim_nuc_generator_99mo_99mtc = function(canvasId, controlsId) {
    var obj = getCanvasAndCtx(canvasId);
    if (!obj) return;
    var canvas = obj.canvas;
    var ctx = obj.ctx;
    var W = canvas.width, H = canvas.height;

    var daysPassed = 0;
    var elutions = [24, 48, 72]; // hours at which eluted
    var currentT = 0;
    var isMilking = false;

    var controls = document.getElementById(controlsId);
    if (controls) {
      controls.innerHTML = `
        <button id="${controlsId}-milk" style="background:#0284c7; color:#fff; border:none; padding:4px 14px; border-radius:4px; cursor:pointer; font-size:12px; font-weight:bold;">Elute Tc-99m Column ("Milk Cow")</button>
        <button id="${controlsId}-reset" style="background:#334155; color:#fff; border:none; padding:4px 12px; border-radius:4px; cursor:pointer; font-size:12px; margin-left:8px;">Reset Generator</button>
      `;

      var milkBtn = document.getElementById(controlsId + '-milk');
      var resetBtn = document.getElementById(controlsId + '-reset');

      milkBtn.addEventListener('click', function() {
        if (!elutions.includes(Math.round(currentT))) {
          elutions.push(Math.round(currentT));
          elutions.sort(function(a, b) { return a - b; });
        }
      });

      resetBtn.addEventListener('click', function() {
        currentT = 0;
        elutions = [24, 48, 72];
      });
    }

    function render() {
      clearCanvas(ctx, W, H);
      drawGrid(ctx, W, H, 40);

      var padL = 70, padR = 40, padT = 30, padB = 50;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      var totalHours = 120; // 5 days
      var lamMo = Math.LN2 / 66.0; // Mo-99 half-life 66 h
      var lamTc = Math.LN2 / 6.0;  // Tc-99m half-life 6.0 h
      var branching = 0.875;       // 87.5% decays to Tc-99m
      var A0_Mo = 1000;            // initial GBq

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padL, padT);
      ctx.lineTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText('Activity on Column [GBq]', padL - 10, padT + 10);
      ctx.textAlign = 'center';
      ctx.fillText('Time Since Generator Production [Hours] (5 Days Total)', padL + plotW / 2, padT + plotH + 35);

      // Parent Mo-99 Activity Curve (Blue)
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var t = (px / plotW) * totalHours;
        var actMo = A0_Mo * Math.exp(-lamMo * t);
        var py = padT + plotH - (actMo / (A0_Mo * 1.1)) * plotH;
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // Daughter Tc-99m Activity Curve with Elutions (Emerald)
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      var lastElute = 0;
      for (var px = 0; px <= plotW; px += 2) {
        var t = (px / plotW) * totalHours;
        // find most recent elution prior to t
        var prevElute = 0;
        for (var e = 0; e < elutions.length; e++) {
          if (elutions[e] <= t) prevElute = elutions[e];
          else break;
        }

        var deltaT = t - prevElute;
        var actMoAtElute = A0_Mo * Math.exp(-lamMo * prevElute);
        // Growth formula from zero at prevElute
        var factor = branching * (lamTc / (lamTc - lamMo));
        var actTc = actMoAtElute * factor * (Math.exp(-lamMo * deltaT) - Math.exp(-lamTc * deltaT));

        var py = padT + plotH - (actTc / (A0_Mo * 1.1)) * plotH;
        if (px === 0) ctx.moveTo(padL + px, py);
        else ctx.lineTo(padL + px, py);
      }
      ctx.stroke();

      // Draw Elution Vertical Lines
      for (var e = 0; e < elutions.length; e++) {
        var et = elutions[e];
        if (et <= totalHours) {
          var epx = padL + (et / totalHours) * plotW;
          ctx.strokeStyle = '#f59e0b';
          ctx.setLineDash([3, 3]);
          ctx.beginPath();
          ctx.moveTo(epx, padT);
          ctx.lineTo(epx, padT + plotH);
          ctx.stroke();
          ctx.setLineDash([]);

          ctx.fillStyle = '#f59e0b';
          ctx.font = '10px monospace';
          ctx.textAlign = 'center';
          ctx.fillText(`Milked ${et}h`, epx, padT + 20);
        }
      }

      // HUD Info
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(padL + plotW - 320, padT + 35, 310, 115);
      ctx.strokeRect(padL + plotW - 320, padT + 35, 310, 115);

      ctx.textAlign = 'left';
      ctx.font = 'bold 12px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('Mo-99 / Tc-99m Generator Physics:', padL + plotW - 310, padT + 55);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText('Parent Mo-99 T1/2 = 66.0 h (Fission Mo-99 on Al2O3)', padL + plotW - 310, padT + 73);
      ctx.fillStyle = '#10b981';
      ctx.fillText('Daughter Tc-99m T1/2 = 6.0 h (Eluted as 99mTcO4-)', padL + plotW - 310, padT + 91);
      ctx.fillStyle = '#f59e0b';
      ctx.fillText('Transient Eq Peak: t_max ~ 22.9 hours post-elute', padL + plotW - 310, padT + 109);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Milking washes column with 0.9% sterile saline.', padL + plotW - 310, padT + 127);

      currentT = (currentT + 0.1) % totalHours;
      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // window.SimulationEngine Mount Adapter
  // =========================================================================
  var SIM_TITLES = {
    sim_nuc_decay_series_bateman: "Bateman Multi-Nuclide Decay Chain & Radioactive Equilibria Engine",
    sim_nuc_binding_energy_curve: "Semi-Empirical Mass Formula (SEMF) Binding Energy & Stability Curve",
    sim_nuc_reaction_cross_section_q: "Nuclear Reaction Kinematics & Breit-Wigner Resonance Simulator",
    sim_nuc_fission_chain_reactor: "2D Nuclear Fission Chain Reaction & Criticality Simulator",
    sim_nuc_bragg_peak_stopping_power: "Bethe-Bloch Heavy Charged Particle Stopping Power & Bragg Peak Engine",
    sim_nuc_gamma_interaction_modes: "Gamma-Ray Interaction Mechanisms (Photoelectric, Compton, Pair Production)",
    sim_nuc_geiger_muller_avalanche: "Geiger-Müller Townsend Avalanche, Voltage Plateau & Dead Time Visualizer",
    sim_nuc_hpge_gamma_spectroscopy: "HPGe Semiconductor vs NaI(Tl) MCA Gamma Spectroscopy Simulator",
    sim_nuc_neutron_activation_analysis: "Neutron Activation Analysis (NAA) Irradiation & Decay Kinetics Engine",
    sim_nuc_generator_99mo_99mtc: "Mo-99 / Tc-99m Radioisotope Generator Elution & Milk Scheduling Simulator"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.NuclearSims || typeof window.NuclearSims[simType] !== 'function') {
      console.warn('Simulation type not found in NuclearSims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Nuclear and Radiochemistry Interactive Simulation";
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
      window.NuclearSims[simType](canvasId, controlsId);
    }, 50);
  };

})();
'''

    with open('nuclear-radiochemistry-sims.js', 'w', encoding='utf-8') as f:
        f.write(js_code)

    print("Successfully generated nuclear-radiochemistry-sims.js")
    lines = len(js_code.splitlines())
    words = len(js_code.split())
    print(f"Stats: {lines} lines, {words} words, {len(js_code)} bytes")

if __name__ == '__main__':
    generate_sims_js()
