# -*- coding: utf-8 -*-
"""
generate_analytical_sims.py
Generates analytical-chemistry-sims.js containing 10 real-time 60 FPS Canvas simulations
for Analytical Chemistry (#46) mounted via window.SimulationEngine.
"""

def generate_sims_js():
    js_code = r'''// Analytical Chemistry Interactive Simulation Suite
// 10 Real-Time 60 FPS Canvas Engines for Analytical Chemistry (#46)
// Mounted via window.SimulationEngine.initSimulation(containerId, simType)

(function() {
  'use strict';

  window.AnalyticalSims = window.AnalyticalSims || {};

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
  // SIMULATION 1: Gaussian Error Distribution & Statistical Outliers (Unit 1)
  // sim_chem_error_gaussian_statistics
  // =========================================================================
  window.AnalyticalSims.sim_chem_error_gaussian_statistics = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var mu = 10.0;
    var sigma = 0.5;
    var confLevel = 95; // 90, 95, 99
    var showTDist = false;
    var sampleN = 5;

    // Controls
    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Mean (μ): <strong id="lbl-mu" style="color:#38bdf8;">10.0</strong>
          <input type="range" id="rng-mu" min="8.0" max="12.0" step="0.1" value="10.0" style="accent-color:#38bdf8;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Std Dev (σ): <strong id="lbl-sigma" style="color:#f59e0b;">0.50</strong>
          <input type="range" id="rng-sigma" min="0.2" max="1.5" step="0.05" value="0.5" style="accent-color:#f59e0b;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Conf:
          <select id="sel-conf" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; border-radius:4px; padding:2px 4px;">
            <option value="90">90% (z=1.645)</option>
            <option value="95" selected>95% (z=1.960)</option>
            <option value="99">99% (z=2.576)</option>
          </select>
        </label>
        <button id="btn-toggle-t" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:3px 8px; font-size:0.8rem; cursor:pointer; margin-left:0.5rem;">Toggle Student's t</button>
      `;

      document.getElementById('rng-mu').addEventListener('input', function(e) {
        mu = parseFloat(e.target.value);
        document.getElementById('lbl-mu').innerText = mu.toFixed(1);
      });
      document.getElementById('rng-sigma').addEventListener('input', function(e) {
        sigma = parseFloat(e.target.value);
        document.getElementById('lbl-sigma').innerText = sigma.toFixed(2);
      });
      document.getElementById('sel-conf').addEventListener('change', function(e) {
        confLevel = parseInt(e.target.value, 10);
      });
      document.getElementById('btn-toggle-t').addEventListener('click', function() {
        showTDist = !showTDist;
        this.style.background = showTDist ? '#10b981' : '#0284c7';
      });
    }

    var zMap = { 90: 1.645, 95: 1.960, 99: 2.576 };

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;
      var z = zMap[confLevel] || 1.96;

      // Coordinate scaling
      var xMin = mu - 4.5 * sigma;
      var xMax = mu + 4.5 * sigma;
      var yMax = 1.0 / (sigma * Math.sqrt(2 * Math.PI));

      function toScreenX(xVal) {
        return 70 + ((xVal - xMin) / (xMax - xMin)) * (w - 140);
      }
      function toScreenY(yVal) {
        return (h - 70) - (yVal / (yMax * 1.15)) * (h - 130);
      }

      // Draw Shaded Confidence Interval
      var xLow = mu - z * sigma;
      var xHigh = mu + z * sigma;
      ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
      ctx.beginPath();
      ctx.moveTo(toScreenX(xLow), toScreenY(0));
      for (var x = xLow; x <= xHigh; x += (xHigh - xLow) / 60) {
        var yNorm = (1.0 / (sigma * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * Math.pow((x - mu) / sigma, 2));
        ctx.lineTo(toScreenX(x), toScreenY(yNorm));
      }
      ctx.lineTo(toScreenX(xHigh), toScreenY(0));
      ctx.closePath();
      ctx.fill();

      // Draw Gaussian Curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var px = 0; px <= 150; px++) {
        var curX = xMin + (px / 150) * (xMax - xMin);
        var curY = (1.0 / (sigma * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * Math.pow((curX - mu) / sigma, 2));
        var sx = toScreenX(curX);
        var sy = toScreenY(curY);
        if (px === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Optional Student's t curve (dof = 4)
      if (showTDist) {
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        for (var px2 = 0; px2 <= 150; px2++) {
          var txVal = xMin + (px2 / 150) * (xMax - xMin);
          var tDiff = (txVal - mu) / sigma;
          var tPdf = (1.0 / (sigma * Math.sqrt(Math.PI * 4))) * (3.0 / 8.0) * Math.pow(1 + (tDiff * tDiff) / 4, -2.5);
          var tsx = toScreenX(txVal);
          var tsy = toScreenY(tPdf);
          if (px2 === 0) ctx.moveTo(tsx, tsy);
          else ctx.lineTo(tsx, tsy);
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Draw Mean Line
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(toScreenX(mu), toScreenY(0));
      ctx.lineTo(toScreenX(mu), toScreenY(yMax));
      ctx.stroke();
      ctx.setLineDash([]);

      // Baseline and Axes
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(50, toScreenY(0));
      ctx.lineTo(w - 50, toScreenY(0));
      ctx.stroke();

      // Metric Overlay Box
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(w - 280, 20, 260, 130);
      ctx.strokeRect(w - 280, 20, 260, 130);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('Normal Distribution Statistics', w - 265, 40);

      ctx.font = '11px monospace';
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Mean (μ): ' + mu.toFixed(2), w - 265, 60);
      ctx.fillText('Std Dev (σ): ' + sigma.toFixed(2), w - 265, 78);
      ctx.fillText('Confidence Interval: ' + confLevel + '%', w - 265, 96);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('[' + (mu - z * sigma).toFixed(2) + ' , ' + (mu + z * sigma).toFixed(2) + ']', w - 265, 114);
      ctx.fillStyle = '#10b981';
      ctx.fillText('Margin: ±' + (z * sigma).toFixed(2) + ' (z=' + z.toFixed(3) + ')', w - 265, 132);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // SIMULATION 2: von Weimarn Supersaturation & Precipitation (Unit 3)
  // sim_chem_precipitation_titration_solubility
  // =========================================================================
  window.AnalyticalSims.sim_chem_precipitation_titration_solubility = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var concQ = 0.05; // M
    var solS = 0.001; // M
    var tempC = 25; // C
    var particles = [];

    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Initial Conc Q (M): <strong id="lbl-q" style="color:#38bdf8;">0.050</strong>
          <input type="range" id="rng-q" min="0.002" max="0.2" step="0.002" value="0.05" style="accent-color:#38bdf8;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Solubility S (M): <strong id="lbl-s" style="color:#f59e0b;">0.0010</strong>
          <input type="range" id="rng-s" min="0.0002" max="0.01" step="0.0002" value="0.001" style="accent-color:#f59e0b;">
        </label>
        <button id="btn-add-reagent" style="background:#10b981; color:#fff; border:none; border-radius:4px; padding:3px 8px; font-size:0.8rem; cursor:pointer; margin-left:0.5rem;">Add Reagent Drop</button>
      `;

      document.getElementById('rng-q').addEventListener('input', function(e) {
        concQ = parseFloat(e.target.value);
        document.getElementById('lbl-q').innerText = concQ.toFixed(3);
      });
      document.getElementById('rng-s').addEventListener('input', function(e) {
        solS = parseFloat(e.target.value);
        document.getElementById('lbl-s').innerText = solS.toFixed(4);
      });
      document.getElementById('btn-add-reagent').addEventListener('click', function() {
        spawnPrecipitate();
      });
    }

    function spawnPrecipitate() {
      var rss = (concQ - solS) / solS;
      var numP = Math.min(180, Math.max(10, Math.floor(rss * 1.5)));
      particles = [];
      for (var i = 0; i < numP; i++) {
        particles.push({
          x: 80 + Math.random() * 260,
          y: 70 + Math.random() * 260,
          vx: (Math.random() - 0.5) * 0.8,
          vy: Math.random() * 0.5 + 0.2,
          radius: rss > 50 ? (1.5 + Math.random() * 1.5) : (4.0 + Math.random() * 3.5), // high RSS = tiny colloidal particles, low RSS = coarse crystals
          color: rss > 50 ? '#f43f5e' : '#38bdf8'
        });
      }
    }
    spawnPrecipitate();

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;
      var rss = Math.max(0, (concQ - solS) / solS);

      // Left: Reaction Beaker Vessel
      ctx.fillStyle = 'rgba(30, 41, 59, 0.5)';
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 2;
      ctx.fillRect(60, 60, 300, 280);
      ctx.strokeRect(60, 60, 300, 280);

      // Solution liquid fill
      ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
      ctx.fillRect(62, 90, 296, 248);

      // Draw precipitate particles
      for (var i = 0; i < particles.length; i++) {
        var p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 70 || p.x > 350) p.vx *= -1;
        if (p.y > 330) {
          p.y = 330;
          p.vy = 0;
        }

        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();
      }

      // Beaker Label
      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Reaction Beaker (Precipitation Chamber)', 80, 45);

      // Right: Relative Supersaturation Graph (RSS vs Particle Size)
      var gx = 420;
      var gy = 60;
      var gw = 340;
      var gh = 280;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.7)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('von Weimarn Ratio of Relative Supersaturation', gx + 15, gy + 25);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText('RSS = (Q - S) / S', gx + 15, gy + 50);
      ctx.fillStyle = '#f59e0b';
      ctx.fillText('Current RSS: ' + rss.toFixed(1), gx + 15, gy + 70);

      // Regime classification
      var regime = rss > 50 ? 'Colloidal Dispersion (Nucleation >> Growth)' : (rss > 10 ? 'Intermediate Mixed Regime' : 'Coarse Crystalline (Growth >> Nucleation)');
      var regColor = rss > 50 ? '#f43f5e' : (rss > 10 ? '#f59e0b' : '#10b981');
      ctx.fillStyle = regColor;
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('Regime: ' + regime, gx + 15, gy + 95);

      // Graphical curve of Nucleation Rate vs Crystal Growth Rate
      ctx.strokeStyle = '#475569';
      ctx.beginPath();
      ctx.moveTo(gx + 30, gy + gh - 40);
      ctx.lineTo(gx + gw - 30, gy + gh - 40);
      ctx.stroke();

      // Nucleation Rate Curve (Exponential)
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (var rx = 0; rx <= 100; rx++) {
        var nx = (gx + 30) + (rx / 100) * (gw - 60);
        var ny = (gy + gh - 42) - Math.pow(rx / 100, 3) * 110;
        if (rx === 0) ctx.moveTo(nx, ny);
        else ctx.lineTo(nx, ny);
      }
      ctx.stroke();

      // Crystal Growth Rate Curve (Linear)
      ctx.strokeStyle = '#10b981';
      ctx.beginPath();
      for (var gx2 = 0; gx2 <= 100; gx2++) {
        var gnx = (gx + 30) + (gx2 / 100) * (gw - 60);
        var gny = (gy + gh - 42) - (gx2 / 100) * 85;
        if (gx2 === 0) ctx.moveTo(gnx, gny);
        else ctx.lineTo(gnx, gny);
      }
      ctx.stroke();

      // Legends
      ctx.fillStyle = '#f43f5e';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('● Nucleation Rate', gx + 30, gy + 125);
      ctx.fillStyle = '#10b981';
      ctx.fillText('● Crystal Growth Rate', gx + 160, gy + 125);

      // Operating point marker on curve
      var normRss = Math.min(1.0, rss / 100);
      var ptX = (gx + 30) + normRss * (gw - 60);
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.arc(ptX, gy + gh - 40, 5, 0, Math.PI * 2);
      ctx.fill();

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // SIMULATION 3: EDTA Complexometric Titration & Conditional Constants (Unit 4)
  // sim_chem_edta_complexometric_titration
  // =========================================================================
  window.AnalyticalSims.sim_chem_edta_complexometric_titration = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var metal = 'Ca'; // Ca, Mg, Zn, Fe
    var pH = 10.0;
    var titrantVol = 25.0; // mL
    var animVol = 0;

    var logKfMap = { Ca: 10.65, Mg: 8.79, Zn: 16.50, Fe: 25.1 };
    var metalName = { Ca: 'Calcium (Ca²⁺)', Mg: 'Magnesium (Mg²⁺)', Zn: 'Zinc (Zn²⁺)', Fe: 'Iron (Fe³⁺)' };

    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Metal Ion:
          <select id="sel-metal" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; border-radius:4px; padding:2px 4px;">
            <option value="Ca" selected>Ca²⁺ (log Kf = 10.65)</option>
            <option value="Mg">Mg²⁺ (log Kf = 8.79)</option>
            <option value="Zn">Zn²⁺ (log Kf = 16.50)</option>
            <option value="Fe">Fe³⁺ (log Kf = 25.1)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Buffer pH: <strong id="lbl-ph" style="color:#f59e0b;">10.0</strong>
          <input type="range" id="rng-ph" min="2.0" max="13.0" step="0.5" value="10.0" style="accent-color:#f59e0b;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">EDTA Added (mL): <strong id="lbl-vol" style="color:#38bdf8;">25.0</strong>
          <input type="range" id="rng-vol" min="0.0" max="50.0" step="0.5" value="25.0" style="accent-color:#38bdf8;">
        </label>
      `;

      document.getElementById('sel-metal').addEventListener('change', function(e) {
        metal = e.target.value;
      });
      document.getElementById('rng-ph').addEventListener('input', function(e) {
        pH = parseFloat(e.target.value);
        document.getElementById('lbl-ph').innerText = pH.toFixed(1);
      });
      document.getElementById('rng-vol').addEventListener('input', function(e) {
        titrantVol = parseFloat(e.target.value);
        document.getElementById('lbl-vol').innerText = titrantVol.toFixed(1);
      });
    }

    // Alpha_Y4- calculation based on pH
    function getAlphaY4(curPh) {
      if (curPh <= 2) return 3.7e-14;
      if (curPh <= 4) return 3.6e-9;
      if (curPh <= 6) return 2.2e-5;
      if (curPh <= 8) return 5.4e-3;
      if (curPh <= 10) return 0.35;
      if (curPh <= 12) return 0.98;
      return 1.0;
    }

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;
      var logKf = logKfMap[metal] || 10.65;
      var alphaY = getAlphaY4(pH);
      var logAlphaY = Math.log10(alphaY);
      var logKfPrime = logKf + logAlphaY; // conditional formation constant

      // Titration Curve Plot (Left to Mid)
      var px = 60;
      var py = 40;
      var pw = 420;
      var phVal = 300;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.7)';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.fillRect(px, py, pw, phVal);
      ctx.strokeRect(px, py, pw, phVal);

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.beginPath();
      ctx.moveTo(px + 40, py + phVal - 30);
      ctx.lineTo(px + pw - 20, py + phVal - 30); // x-axis
      ctx.moveTo(px + 40, py + 20);
      ctx.lineTo(px + 40, py + phVal - 30); // y-axis
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('0', px + 35, py + phVal - 15);
      ctx.fillText('25 mL (Eq Pt)', px + 210, py + phVal - 15);
      ctx.fillText('50 mL', px + pw - 40, py + phVal - 15);
      ctx.fillText('pM', px + 15, py + 30);

      // Calculate titration curve: 25.0 mL of 0.01 M M^n+ titrated with 0.01 M EDTA
      // Equivalence point is at 25.0 mL
      var Veq = 25.0;
      var cM0 = 0.01;
      var V0 = 25.0;

      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      for (var vStep = 0; vStep <= 50; vStep += 0.5) {
        var pMVal = 0;
        if (vStep < Veq - 0.1) {
          // Pre-equivalence: excess free metal
          var cM = (cM0 * V0 - cM0 * vStep) / (V0 + vStep);
          pMVal = -Math.log10(Math.max(1e-12, cM));
        } else if (Math.abs(vStep - Veq) <= 0.1) {
          // At equivalence: [M] = sqrt(cMY / K'_f)
          var cMY = (cM0 * V0) / (V0 + Veq);
          var KfPrime = Math.pow(10, logKfPrime);
          var cMeq = Math.sqrt(cMY / KfPrime);
          pMVal = -Math.log10(Math.max(1e-16, cMeq));
        } else {
          // Post-equivalence: excess EDTA
          var cMYpost = (cM0 * V0) / (V0 + vStep);
          var cYexcess = (cM0 * (vStep - Veq)) / (V0 + vStep);
          var KfPrimePost = Math.pow(10, logKfPrime);
          var cMpost = cMYpost / (KfPrimePost * cYexcess * alphaY);
          pMVal = -Math.log10(Math.max(1e-22, cMpost));
        }

        // Map pMVal (range 2 to 14) to screen coordinates
        var sx = (px + 40) + (vStep / 50.0) * (pw - 60);
        var sy = (py + phVal - 30) - ((pMVal - 2.0) / 12.0) * (phVal - 50);
        sy = Math.max(py + 20, Math.min(py + phVal - 30, sy));

        if (vStep === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Current titrant cursor
      var curX = (px + 40) + (titrantVol / 50.0) * (pw - 60);
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(curX, py + 20);
      ctx.lineTo(curX, py + phVal - 30);
      ctx.stroke();
      ctx.setLineDash([]);

      // Right: Indicator Color & Physical Metrics Box
      var rx = 510;
      var ry = 40;
      var rw = 250;
      var rh = 300;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = '#334155';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(metalName[metal], rx + 15, ry + 25);

      ctx.font = '11px monospace';
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Absolute log Kf: ' + logKf.toFixed(2), rx + 15, ry + 50);
      ctx.fillText('α_Y4- at pH ' + pH.toFixed(1) + ': ' + alphaY.toExponential(2), rx + 15, ry + 70);
      ctx.fillStyle = '#f59e0b';
      ctx.fillText('log K\'f (Conditional): ' + logKfPrime.toFixed(2), rx + 15, ry + 90);

      // Indicator Flask Visualization
      var indColor = titrantVol < 24.5 ? '#e11d48' : (titrantVol > 25.5 ? '#0284c7' : '#8b5cf6');
      var indText = titrantVol < 24.5 ? 'Wine Red [M-In⁻]' : (titrantVol > 25.5 ? 'Sky Blue [Free HIn²⁻]' : 'Transition Endpoint');

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('Eriochrome Black T Indicator:', rx + 15, ry + 125);

      // Flask Graphic
      ctx.fillStyle = indColor;
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(rx + 125, ry + 185, 45, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(indText, rx + 125, ry + 255);
      ctx.textAlign = 'left';

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // SIMULATION 4: Atomic Absorption & Flameless Zeeman Correction (Unit 5)
  // sim_chem_atomic_absorption_flameless_zeeman
  // =========================================================================
  window.AnalyticalSims.sim_chem_atomic_absorption_flameless_zeeman = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var mode = 'GFAAS'; // Flame or GFAAS
    var zeemanOn = false;
    var stage = 'Atomize'; // Dry, Ash, Atomize, Clean
    var stageProgress = 0;

    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Atomizer:
          <select id="sel-aas-mode" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; border-radius:4px; padding:2px 4px;">
            <option value="Flame">Flame Burner (Premix)</option>
            <option value="GFAAS" selected>Graphite Furnace (ETA)</option>
          </select>
        </label>
        <button id="btn-toggle-zeeman" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:3px 8px; font-size:0.8rem; cursor:pointer; margin-left:0.5rem;">Zeeman Magnet: OFF</button>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Furnace Cycle:
          <select id="sel-furnace-stage" style="background:#1e293b; color:#f59e0b; border:1px solid #475569; border-radius:4px; padding:2px 4px;">
            <option value="Dry">1. Dry (110°C)</option>
            <option value="Ash">2. Pyrolysis/Ash (800°C)</option>
            <option value="Atomize" selected>3. Atomize (2400°C)</option>
            <option value="Clean">4. Tube Clean (2600°C)</option>
          </select>
        </label>
      `;

      document.getElementById('sel-aas-mode').addEventListener('change', function(e) {
        mode = e.target.value;
      });
      document.getElementById('btn-toggle-zeeman').addEventListener('click', function() {
        zeemanOn = !zeemanOn;
        this.style.background = zeemanOn ? '#10b981' : '#0284c7';
        this.innerText = 'Zeeman Magnet: ' + (zeemanOn ? 'ON (Transverse)' : 'OFF');
      });
      document.getElementById('sel-furnace-stage').addEventListener('change', function(e) {
        stage = e.target.value;
      });
    }

    var photonOffset = 0;

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;
      photonOffset = (photonOffset + 3) % 40;

      // Layout:
      // Left: Hollow Cathode Lamp (HCL)
      // Center: Atom Cell (Flame or Graphite Tube with Electromagnet)
      // Right: Monochromator Grating & PMT Detector

      // 1. Hollow Cathode Lamp
      ctx.fillStyle = '#1e293b';
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.fillRect(40, 110, 110, 100);
      ctx.strokeRect(40, 110, 110, 100);

      // Cathode Cup inside HCL
      ctx.fillStyle = '#f59e0b';
      ctx.fillRect(80, 140, 30, 40);
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('HCL Source', 55, 130);
      ctx.fillStyle = '#94a3b8';
      ctx.font = '9px monospace';
      ctx.fillText('λ = 285.2 nm', 55, 195);

      // 2. Optical Light Beam
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(150, 160);
      ctx.lineTo(590, 160);
      ctx.stroke();

      // Photons traversing beam
      ctx.fillStyle = '#ffffff';
      for (var bx = 160 + photonOffset; bx < 580; bx += 40) {
        ctx.beginPath();
        ctx.arc(bx, 160, 2.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // 3. Atom Cell (Center)
      if (mode === 'GFAAS') {
        // Graphite Tube
        var tubeTemp = stage === 'Dry' ? 110 : (stage === 'Ash' ? 800 : (stage === 'Atomize' ? 2400 : 2600));
        var glowColor = stage === 'Dry' ? '#334155' : (stage === 'Ash' ? '#b45309' : '#f97316');

        ctx.fillStyle = glowColor;
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 2;
        ctx.fillRect(260, 130, 180, 60);
        ctx.strokeRect(260, 130, 180, 60);

        // L'vov Platform inside
        ctx.fillStyle = '#475569';
        ctx.fillRect(320, 165, 60, 8);

        // Zeeman Electromagnet Poles (if active)
        if (zeemanOn) {
          ctx.fillStyle = '#dc2626'; // North
          ctx.fillRect(280, 80, 140, 35);
          ctx.fillStyle = '#2563eb'; // South
          ctx.fillRect(280, 205, 140, 35);

          ctx.fillStyle = '#ffffff';
          ctx.font = 'bold 11px Inter, sans-serif';
          ctx.fillText('Magnetic Field B (Zeeman σ/π)', 285, 102);
        }

        ctx.fillStyle = '#f59e0b';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillText('Graphite Furnace: ' + tubeTemp + '°C', 280, 260);
        ctx.fillStyle = '#94a3b8';
        ctx.font = '10px Inter, sans-serif';
        ctx.fillText('Stage: ' + stage, 280, 275);
      } else {
        // Flame Premix Burner
        ctx.fillStyle = '#0ea5e9';
        ctx.beginPath();
        ctx.moveTo(270, 190);
        ctx.lineTo(350, 110);
        ctx.lineTo(430, 190);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle = '#1e293b';
        ctx.fillRect(320, 190, 60, 60);
        ctx.fillStyle = '#f59e0b';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillText('Air-C₂H₂ Flame (2300°C)', 280, 270);
      }

      // 4. Monochromator & Detector (Right)
      ctx.fillStyle = '#1e293b';
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2;
      ctx.fillRect(590, 110, 160, 110);
      ctx.strokeRect(590, 110, 160, 110);

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('Czerny-Turner PMT', 605, 135);

      // Diffraction Grating icon
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 1.5;
      for (var gi = 0; gi < 8; gi++) {
        ctx.beginPath();
        ctx.moveTo(630 + gi * 6, 155);
        ctx.lineTo(625 + gi * 6, 185);
        ctx.stroke();
      }

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px monospace';
      ctx.fillText('Detector Signal: OK', 605, 205);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // SIMULATION 5: Ion-Exchange Resin & Breakthrough Curves (Unit 6)
  // sim_chem_ion_exchange_breakthrough_curve
  // =========================================================================
  window.AnalyticalSims.sim_chem_ion_exchange_breakthrough_curve = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var flowRate = 2.0; // mL/min
    var capacity = 5.0; // meq/mL
    var bedVolumes = 15;
    var ionPair = 'ZnMg'; // Zn/Mg or Cl/Br

    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Separation:
          <select id="sel-ion-pair" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; border-radius:4px; padding:2px 4px;">
            <option value="ZnMg" selected>Zn²⁺ vs Mg²⁺ (Anion Chloro-Complex)</option>
            <option value="ClBr">Cl⁻ vs Br⁻ (Anion Exchange)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Flow (mL/min): <strong id="lbl-flow" style="color:#f59e0b;">2.0</strong>
          <input type="range" id="rng-flow" min="0.5" max="5.0" step="0.5" value="2.0" style="accent-color:#f59e0b;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Bed Volumes (BV): <strong id="lbl-bv" style="color:#38bdf8;">15</strong>
          <input type="range" id="rng-bv" min="2" max="30" step="1" value="15" style="accent-color:#38bdf8;">
        </label>
      `;

      document.getElementById('sel-ion-pair').addEventListener('change', function(e) {
        ionPair = e.target.value;
      });
      document.getElementById('rng-flow').addEventListener('input', function(e) {
        flowRate = parseFloat(e.target.value);
        document.getElementById('lbl-flow').innerText = flowRate.toFixed(1);
      });
      document.getElementById('rng-bv').addEventListener('input', function(e) {
        bedVolumes = parseInt(e.target.value, 10);
        document.getElementById('lbl-bv').innerText = bedVolumes;
      });
    }

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;

      // Left: Ion Exchange Chromatography Column
      var cx = 80;
      var cy = 40;
      var cw = 110;
      var ch = 310;

      ctx.fillStyle = 'rgba(30, 41, 59, 0.6)';
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 2;
      ctx.fillRect(cx, cy, cw, ch);
      ctx.strokeRect(cx, cy, cw, ch);

      // Resin Beads Packing
      for (var bx = cx + 12; bx < cx + cw - 12; bx += 16) {
        for (var by = cy + 20; by < cy + ch - 25; by += 16) {
          ctx.fillStyle = '#f59e0b';
          ctx.beginPath();
          ctx.arc(bx + (by % 8), by, 5, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('PS-DVB Resin', cx + 15, cy + ch + 20);

      // Right: Breakthrough Curve Plot (C/C0 vs Bed Volumes)
      var px = 240;
      var py = 40;
      var pw = 500;
      var pht = 300;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = '#334155';
      ctx.fillRect(px, py, pw, pht);
      ctx.strokeRect(px, py, pw, pht);

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.beginPath();
      ctx.moveTo(px + 40, py + pht - 30);
      ctx.lineTo(px + pw - 20, py + pht - 30);
      ctx.moveTo(px + 40, py + 20);
      ctx.lineTo(px + 40, py + pht - 30);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('0', px + 35, py + pht - 15);
      ctx.fillText('10 BV', px + 180, py + pht - 15);
      ctx.fillText('20 BV', px + 330, py + pht - 15);
      ctx.fillText('30 BV', px + pw - 35, py + pht - 15);
      ctx.fillText('C / C₀', px + 10, py + 30);

      // Plot Component A Breakthrough (e.g. Mg²⁺ uncomplexed - immediate breakthrough at BV ~ 2)
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var bv = 0; bv <= 30; bv += 0.5) {
        var cRatioA = 1.0 / (1.0 + Math.exp(-(bv - 3.0) / (0.6 * flowRate)));
        var sxA = (px + 40) + (bv / 30.0) * (pw - 60);
        var syA = (py + pht - 30) - cRatioA * (pht - 50);
        if (bv === 0) ctx.moveTo(sxA, syA);
        else ctx.lineTo(sxA, syA);
      }
      ctx.stroke();

      // Plot Component B Breakthrough (e.g. Zn²⁺ chloro-complex [ZnCl4]²⁻ strongly retained until BV ~ 18)
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var bv2 = 0; bv2 <= 30; bv2 += 0.5) {
        var cRatioB = 1.0 / (1.0 + Math.exp(-(bv2 - 18.0) / (0.8 * flowRate)));
        var sxB = (px + 40) + (bv2 / 30.0) * (pw - 60);
        var syB = (py + pht - 30) - cRatioB * (pht - 50);
        if (bv2 === 0) ctx.moveTo(sxB, syB);
        else ctx.lineTo(sxB, syB);
      }
      ctx.stroke();

      // Current operating BV marker line
      var curX = (px + 40) + (bedVolumes / 30.0) * (pw - 60);
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(curX, py + 20);
      ctx.lineTo(curX, py + pht - 30);
      ctx.stroke();
      ctx.setLineDash([]);

      // Legend
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('● Fast Eluting (Mg²⁺ uncomplexed)', px + 50, py + 35);
      ctx.fillStyle = '#f43f5e';
      ctx.fillText('● Retained (ZnCl₄²⁻ chloro-anion)', px + 260, py + 35);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // SIMULATION 6: Beer-Lambert Law & Stray Light Deviations (Unit 7)
  // sim_chem_beer_lambert_spectrophotometer
  // =========================================================================
  window.AnalyticalSims.sim_chem_beer_lambert_spectrophotometer = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var eps = 5000; // L/(mol*cm)
    var pathlength = 1.0; // cm
    var conc = 0.0002; // M
    var strayLight = 1.0; // % stray light

    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Molar Absorptivity (ε): <strong id="lbl-eps" style="color:#38bdf8;">5000</strong>
          <input type="range" id="rng-eps" min="1000" max="15000" step="500" value="5000" style="accent-color:#38bdf8;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Pathlength b (cm): <strong id="lbl-b" style="color:#f59e0b;">1.0</strong>
          <input type="range" id="rng-b" min="0.1" max="2.0" step="0.1" value="1.0" style="accent-color:#f59e0b;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Stray Light (%): <strong id="lbl-stray" style="color:#f43f5e;">1.0%</strong>
          <input type="range" id="rng-stray" min="0.0" max="5.0" step="0.2" value="1.0" style="accent-color:#f43f5e;">
        </label>
      `;

      document.getElementById('rng-eps').addEventListener('input', function(e) {
        eps = parseFloat(e.target.value);
        document.getElementById('lbl-eps').innerText = eps.toFixed(0);
      });
      document.getElementById('rng-b').addEventListener('input', function(e) {
        pathlength = parseFloat(e.target.value);
        document.getElementById('lbl-b').innerText = pathlength.toFixed(1);
      });
      document.getElementById('rng-stray').addEventListener('input', function(e) {
        strayLight = parseFloat(e.target.value);
        document.getElementById('lbl-stray').innerText = strayLight.toFixed(1) + '%';
      });
    }

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;

      // Plot: Absorbance vs Concentration (0 to 0.0006 M)
      var px = 80;
      var py = 40;
      var pw = 620;
      var pht = 290;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = '#334155';
      ctx.fillRect(px, py, pw, pht);
      ctx.strokeRect(px, py, pw, pht);

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.beginPath();
      ctx.moveTo(px + 40, py + pht - 30);
      ctx.lineTo(px + pw - 20, py + pht - 30);
      ctx.moveTo(px + 40, py + 20);
      ctx.lineTo(px + 40, py + pht - 30);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('0', px + 35, py + pht - 15);
      ctx.fillText('0.0002 M', px + 220, py + pht - 15);
      ctx.fillText('0.0004 M', px + 410, py + pht - 15);
      ctx.fillText('0.0006 M', px + pw - 45, py + pht - 15);
      ctx.fillText('Absorbance A', px + 5, py + 25);

      // Maximum ideal absorbance at 0.0006 M
      var maxConc = 0.0006;
      var maxIdealA = eps * pathlength * maxConc;
      var scaleY = Math.max(3.0, maxIdealA);

      // 1. Ideal Beer's Law Line (Straight line)
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (var cStep = 0; cStep <= 60; cStep++) {
        var cVal = (cStep / 60.0) * maxConc;
        var aIdeal = eps * pathlength * cVal;
        var sx = (px + 40) + (cStep / 60.0) * (pw - 60);
        var sy = (py + pht - 30) - (aIdeal / scaleY) * (pht - 50);
        if (cStep === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // 2. Real Apparent Absorbance with Stray Light:
      // A_app = -log10((10^(-A_true) + s) / (1 + s))
      var sFrac = strayLight / 100.0;
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var cStep2 = 0; cStep2 <= 60; cStep2++) {
        var cVal2 = (cStep2 / 60.0) * maxConc;
        var aTrue = eps * pathlength * cVal2;
        var transTrue = Math.pow(10, -aTrue);
        var transApp = (transTrue + sFrac) / (1.0 + sFrac);
        var aApp = -Math.log10(transApp);

        var sx2 = (px + 40) + (cStep2 / 60.0) * (pw - 60);
        var sy2 = (py + pht - 30) - (aApp / scaleY) * (pht - 50);
        if (cStep2 === 0) ctx.moveTo(sx2, sy2);
        else ctx.lineTo(sx2, sy2);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('● Ideal Linear Beer-Lambert (A = ε b c)', px + 50, py + 35);
      ctx.fillStyle = '#f43f5e';
      ctx.fillText('● Apparent Absorbance with Stray Light (' + strayLight.toFixed(1) + '%)', px + 330, py + 35);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // SIMULATION 7: Spectrophotometric Titration Curve Engine (Unit 7)
  // sim_chem_spectrophotometric_titration_curves
  // =========================================================================
  window.AnalyticalSims.sim_chem_spectrophotometric_titration_curves = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var epsA = 1000;
    var epsT = 0;
    var epsP = 5000;
    var corrVol = true;

    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Profile:
          <select id="sel-spec-type" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; border-radius:4px; padding:2px 4px;">
            <option value="ProductOnly" selected>Product Absorbs Only (Inverted V)</option>
            <option value="AnalyteOnly">Analyte Absorbs Only (L-Shape)</option>
            <option value="TitrantOnly">Titrant Absorbs Only (Rising Line)</option>
            <option value="AnalyteTitrant">Analyte + Titrant Absorb (V-Shape)</option>
          </select>
        </label>
        <button id="btn-toggle-volcorr" style="background:#10b981; color:#fff; border:none; border-radius:4px; padding:3px 8px; font-size:0.8rem; cursor:pointer; margin-left:0.5rem;">Dilution Correction: ON</button>
      `;

      document.getElementById('sel-spec-type').addEventListener('change', function(e) {
        var v = e.target.value;
        if (v === 'ProductOnly') { epsA = 0; epsT = 0; epsP = 4000; }
        else if (v === 'AnalyteOnly') { epsA = 4000; epsT = 0; epsP = 0; }
        else if (v === 'TitrantOnly') { epsA = 0; epsT = 4000; epsP = 0; }
        else if (v === 'AnalyteTitrant') { epsA = 3500; epsT = 3500; epsP = 0; }
      });

      document.getElementById('btn-toggle-volcorr').addEventListener('click', function() {
        corrVol = !corrVol;
        this.style.background = corrVol ? '#10b981' : '#64748b';
        this.innerText = 'Dilution Correction: ' + (corrVol ? 'ON' : 'OFF');
      });
    }

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;

      var px = 80;
      var py = 40;
      var pw = 640;
      var pht = 290;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = '#334155';
      ctx.fillRect(px, py, pw, pht);
      ctx.strokeRect(px, py, pw, pht);

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.beginPath();
      ctx.moveTo(px + 40, py + pht - 30);
      ctx.lineTo(px + pw - 20, py + pht - 30);
      ctx.moveTo(px + 40, py + 20);
      ctx.lineTo(px + 40, py + pht - 30);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('0', px + 35, py + pht - 15);
      ctx.fillText('V_eq (25 mL)', px + 300, py + pht - 15);
      ctx.fillText('50 mL', px + pw - 45, py + pht - 15);
      ctx.fillText('Absorbance A', px + 5, py + 25);

      // Titration titration mechanics: V0 = 25 mL, cA0 = 0.001 M, cT = 0.001 M, Veq = 25 mL
      var V0 = 25.0;
      var Veq = 25.0;
      var cA0 = 0.001;

      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      for (var vt = 0; vt <= 50; vt += 0.5) {
        var cA = 0;
        var cT = 0;
        var cP = 0;

        if (vt <= Veq) {
          cA = (cA0 * (Veq - vt)) / (V0 + vt);
          cP = (cA0 * vt) / (V0 + vt);
          cT = 0;
        } else {
          cA = 0;
          cP = (cA0 * Veq) / (V0 + vt);
          cT = (cA0 * (vt - Veq)) / (V0 + vt);
        }

        var Aobs = epsA * cA + epsT * cT + epsP * cP;
        var Aplot = corrVol ? Aobs * ((V0 + vt) / V0) : Aobs;

        var sx = (px + 40) + (vt / 50.0) * (pw - 60);
        var sy = (py + pht - 30) - (Aplot / 4.5) * (pht - 50);
        sy = Math.max(py + 20, Math.min(py + pht - 30, sy));

        if (vt === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Equivalence point marker
      var eqX = (px + 40) + (Veq / 50.0) * (pw - 60);
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(eqX, py + 20);
      ctx.lineTo(eqX, py + pht - 30);
      ctx.stroke();
      ctx.setLineDash([]);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // SIMULATION 8: Liquid-Liquid Extraction Partition Thermodynamics (Unit 8)
  // sim_chem_solvent_extraction_partition
  // =========================================================================
  window.AnalyticalSims.sim_chem_solvent_extraction_partition = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var distD = 8.0;
    var V_aq = 50.0;
    var V_org_tot = 50.0;
    var numExt = 3;

    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Distribution Ratio (D): <strong id="lbl-dist-d" style="color:#38bdf8;">8.0</strong>
          <input type="range" id="rng-dist-d" min="0.5" max="25.0" step="0.5" value="8.0" style="accent-color:#38bdf8;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Extractions (n): <strong id="lbl-next" style="color:#f59e0b;">3</strong>
          <input type="range" id="rng-next" min="1" max="5" step="1" value="3" style="accent-color:#f59e0b;">
        </label>
      `;

      document.getElementById('rng-dist-d').addEventListener('input', function(e) {
        distD = parseFloat(e.target.value);
        document.getElementById('lbl-dist-d').innerText = distD.toFixed(1);
      });
      document.getElementById('rng-next').addEventListener('input', function(e) {
        numExt = parseInt(e.target.value, 10);
        document.getElementById('lbl-next').innerText = numExt;
      });
    }

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;

      // Fraction remaining in aqueous phase:
      // q_n = (V_aq / (V_aq + D * (V_org / n)))^n
      var vPortion = V_org_tot / numExt;
      var q_n = Math.pow(V_aq / (V_aq + distD * vPortion), numExt);
      var percentExtracted = (1.0 - q_n) * 100.0;

      // Single extraction equivalent (n = 1 using entire 50 mL)
      var q_1 = V_aq / (V_aq + distD * V_org_tot);
      var percentExtractedSingle = (1.0 - q_1) * 100.0;

      // Left: Separatory Funnel Graphic
      var fx = 120;
      var fy = 60;

      // Funnel Glass Outline
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(fx - 40, fy);
      ctx.lineTo(fx + 40, fy);
      ctx.lineTo(fx + 35, fy + 70);
      ctx.lineTo(fx + 5, fy + 160);
      ctx.lineTo(fx + 5, fy + 210);
      ctx.lineTo(fx - 5, fy + 210);
      ctx.lineTo(fx - 5, fy + 160);
      ctx.lineTo(fx - 35, fy + 70);
      ctx.closePath();
      ctx.stroke();

      // Organic Layer (Top: Ether / MIBK)
      ctx.fillStyle = 'rgba(245, 158, 11, 0.4)';
      ctx.fillRect(fx - 32, fy + 20, 64, 45);

      // Aqueous Layer (Bottom)
      ctx.fillStyle = 'rgba(56, 189, 248, 0.4)';
      ctx.fillRect(fx - 28, fy + 65, 56, 70);

      ctx.fillStyle = '#f59e0b';
      ctx.font = 'bold 10px Inter, sans-serif';
      ctx.fillText('Organic Phase', fx + 50, fy + 45);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('Aqueous Phase', fx + 50, fy + 95);

      // Right: Extraction Comparison Chart
      var cx = 320;
      var cy = 50;
      var cw = 420;
      var ch = 280;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = '#334155';
      ctx.fillRect(cx, cy, cw, ch);
      ctx.strokeRect(cx, cy, cw, ch);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('Multiple Batch Extraction Efficiency Proof', cx + 20, cy + 30);

      // Bar Chart: 1 extraction vs n extractions
      var bar1H = (percentExtractedSingle / 100.0) * 160;
      var barNH = (percentExtracted / 100.0) * 160;

      // Bar 1 (Single)
      ctx.fillStyle = '#64748b';
      ctx.fillRect(cx + 60, cy + 220 - bar1H, 80, bar1H);
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 11px monospace';
      ctx.fillText(percentExtractedSingle.toFixed(1) + '%', cx + 75, cy + 210 - bar1H);

      // Bar 2 (Multiple)
      ctx.fillStyle = '#10b981';
      ctx.fillRect(cx + 220, cy + 220 - barNH, 80, barNH);
      ctx.fillStyle = '#ffffff';
      ctx.fillText(percentExtracted.toFixed(2) + '%', cx + 230, cy + 210 - barNH);

      // Labels below bars
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('Single 50 mL (n=1)', cx + 55, cy + 245);
      ctx.fillText(numExt + ' × ' + vPortion.toFixed(1) + ' mL (n=' + numExt + ')', cx + 215, cy + 245);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // SIMULATION 9: van Deemter Column Efficiency & Flow Rate (Unit 9)
  // sim_chem_chromatography_van_deemter_efficiency
  // =========================================================================
  window.AnalyticalSims.sim_chem_chromatography_van_deemter_efficiency = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var termA = 0.5; // mm (Eddy diffusion)
    var termB = 1.2; // mm*cm/s (Longitudinal diffusion)
    var termC = 0.08; // mm*s/cm (Mass transfer resistance)
    var curFlow = 3.5; // cm/s

    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Eddy Diff A (mm): <strong id="lbl-term-a" style="color:#38bdf8;">0.50</strong>
          <input type="range" id="rng-term-a" min="0.1" max="1.5" step="0.05" value="0.5" style="accent-color:#38bdf8;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Longitud B: <strong id="lbl-term-b" style="color:#f59e0b;">1.20</strong>
          <input type="range" id="rng-term-b" min="0.2" max="3.0" step="0.1" value="1.2" style="accent-color:#f59e0b;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Mass Trans C: <strong id="lbl-term-c" style="color:#f43f5e;">0.08</strong>
          <input type="range" id="rng-term-c" min="0.01" max="0.3" step="0.01" value="0.08" style="accent-color:#f43f5e;">
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Flow u: <strong id="lbl-cur-flow" style="color:#10b981;">3.5</strong>
          <input type="range" id="rng-cur-flow" min="0.5" max="10.0" step="0.2" value="3.5" style="accent-color:#10b981;">
        </label>
      `;

      document.getElementById('rng-term-a').addEventListener('input', function(e) {
        termA = parseFloat(e.target.value);
        document.getElementById('lbl-term-a').innerText = termA.toFixed(2);
      });
      document.getElementById('rng-term-b').addEventListener('input', function(e) {
        termB = parseFloat(e.target.value);
        document.getElementById('lbl-term-b').innerText = termB.toFixed(2);
      });
      document.getElementById('rng-term-c').addEventListener('input', function(e) {
        termC = parseFloat(e.target.value);
        document.getElementById('lbl-term-c').innerText = termC.toFixed(2);
      });
      document.getElementById('rng-cur-flow').addEventListener('input', function(e) {
        curFlow = parseFloat(e.target.value);
        document.getElementById('lbl-cur-flow').innerText = curFlow.toFixed(1);
      });
    }

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;

      // Plot: van Deemter Equation H = A + B/u + C*u
      var px = 80;
      var py = 40;
      var pw = 640;
      var pht = 290;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = '#334155';
      ctx.fillRect(px, py, pw, pht);
      ctx.strokeRect(px, py, pw, pht);

      // Axes
      ctx.strokeStyle = '#475569';
      ctx.beginPath();
      ctx.moveTo(px + 40, py + pht - 30);
      ctx.lineTo(px + pw - 20, py + pht - 30);
      ctx.moveTo(px + 40, py + 20);
      ctx.lineTo(px + 40, py + pht - 30);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('0', px + 35, py + pht - 15);
      ctx.fillText('5 cm/s', px + 320, py + pht - 15);
      ctx.fillText('10 cm/s', px + pw - 45, py + pht - 15);
      ctx.fillText('Plate Height H (mm)', px + 5, py + 25);

      // Calculate u_opt = sqrt(B / C) and H_min = A + 2*sqrt(B*C)
      var uOpt = Math.sqrt(termB / termC);
      var hMin = termA + 2.0 * Math.sqrt(termB * termC);

      // Draw Individual Contributions
      // 1. Term A (Constant)
      ctx.strokeStyle = '#64748b';
      ctx.setLineDash([2, 2]);
      ctx.beginPath();
      ctx.moveTo(px + 40, (py + pht - 30) - (termA / 3.0) * (pht - 50));
      ctx.lineTo(px + pw - 20, (py + pht - 30) - (termA / 3.0) * (pht - 50));
      ctx.stroke();

      // 2. Composite van Deemter Curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.setLineDash([]);
      ctx.beginPath();

      for (var u = 0.4; u <= 10.0; u += 0.1) {
        var Hval = termA + (termB / u) + (termC * u);
        var sx = (px + 40) + (u / 10.0) * (pw - 60);
        var sy = (py + pht - 30) - (Hval / 3.0) * (pht - 50);
        sy = Math.max(py + 20, Math.min(py + pht - 30, sy));

        if (u === 0.4) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Highlight Optimal Flow velocity
      var optX = (px + 40) + (Math.min(10.0, uOpt) / 10.0) * (pw - 60);
      var optY = (py + pht - 30) - (hMin / 3.0) * (pht - 50);
      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.arc(optX, optY, 6, 0, Math.PI * 2);
      ctx.fill();

      // Current Flow Marker
      var curX = (px + 40) + (curFlow / 10.0) * (pw - 60);
      var curH = termA + (termB / curFlow) + (termC * curFlow);
      var curY = (py + pht - 30) - (curH / 3.0) * (pht - 50);
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(curX, curY, 5, 0, Math.PI * 2);
      ctx.fill();

      // Metric Annotation Box
      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('Optimal Velocity u_opt: ' + uOpt.toFixed(2) + ' cm/s (H_min = ' + hMin.toFixed(2) + ' mm)', px + 50, py + 35);
      ctx.fillStyle = '#f59e0b';
      ctx.fillText('Current u: ' + curFlow.toFixed(2) + ' cm/s → H = ' + curH.toFixed(2) + ' mm', px + 50, py + 52);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // SIMULATION 10: HPLC & TLC Multi-Mode Separation Engine (Unit 9)
  // sim_chem_hplc_tlc_separation_engine
  // =========================================================================
  window.AnalyticalSims.sim_chem_hplc_tlc_separation_engine = function(canvasId, controlsId) {
    var cInfo = getCanvasAndCtx(canvasId);
    if (!cInfo) return;
    var canvas = cInfo.canvas;
    var ctx = cInfo.ctx;

    var mode = 'HPLC'; // HPLC or TLC
    var polarity = 50; // % organic modifier (e.g. % Acetonitrile in RP-HPLC)

    var cPanel = document.getElementById(controlsId);
    if (cPanel) {
      cPanel.innerHTML = `
        <label style="color:#94a3b8; font-size:0.8rem;">Chromatography Mode:
          <select id="sel-chrom-mode" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; border-radius:4px; padding:2px 4px;">
            <option value="HPLC" selected>Reversed-Phase HPLC (C18 Column)</option>
            <option value="TLC">Thin Layer Chromatography (Silica Plate)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.8rem; margin-left:0.5rem;">Organic Modifier (%): <strong id="lbl-pol" style="color:#f59e0b;">50%</strong>
          <input type="range" id="rng-pol" min="20" max="80" step="5" value="50" style="accent-color:#f59e0b;">
        </label>
      `;

      document.getElementById('sel-chrom-mode').addEventListener('change', function(e) {
        mode = e.target.value;
      });
      document.getElementById('rng-pol').addEventListener('input', function(e) {
        polarity = parseInt(e.target.value, 10);
        document.getElementById('lbl-pol').innerText = polarity + '%';
      });
    }

    function render() {
      clearCanvas(ctx, canvas.width, canvas.height, '#080d19');
      drawGrid(ctx, canvas.width, canvas.height, 40);

      var w = canvas.width;
      var h = canvas.height;

      if (mode === 'HPLC') {
        // RP-HPLC Chromatogram View
        var px = 80;
        var py = 40;
        var pw = 640;
        var pht = 290;

        ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
        ctx.strokeStyle = '#334155';
        ctx.fillRect(px, py, pw, pht);
        ctx.strokeRect(px, py, pw, pht);

        // Axes
        ctx.strokeStyle = '#475569';
        ctx.beginPath();
        ctx.moveTo(px + 40, py + pht - 30);
        ctx.lineTo(px + pw - 20, py + pht - 30);
        ctx.moveTo(px + 40, py + 20);
        ctx.lineTo(px + 40, py + pht - 30);
        ctx.stroke();

        ctx.fillStyle = '#94a3b8';
        ctx.font = '10px Inter, sans-serif';
        ctx.fillText('0 min', px + 35, py + pht - 15);
        ctx.fillText('5 min', px + 240, py + pht - 15);
        ctx.fillText('10 min', px + 440, py + pht - 15);
        ctx.fillText('15 min', px + pw - 45, py + pht - 15);
        ctx.fillText('Absorbance (mAU)', px + 5, py + 25);

        // Retention shifts with % organic modifier
        // High % acetonitrile = faster elution (lower t_R)
        var tR1 = 2.0 + (100 - polarity) * 0.05;
        var tR2 = 4.0 + (100 - polarity) * 0.12;

        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        for (var t = 0; t <= 15; t += 0.05) {
          var sig1 = 150 * Math.exp(-0.5 * Math.pow((t - tR1) / 0.18, 2));
          var sig2 = 180 * Math.exp(-0.5 * Math.pow((t - tR2) / 0.28, 2));
          var totalSig = sig1 + sig2;

          var sx = (px + 40) + (t / 15.0) * (pw - 60);
          var sy = (py + pht - 30) - (totalSig / 220.0) * (pht - 50);

          if (t === 0) ctx.moveTo(sx, sy);
          else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Peak Labels
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillText('Peak 1 (Polar Solute)', (px + 40) + (tR1 / 15.0) * (pw - 60) - 20, py + 50);
        ctx.fillText('Peak 2 (Non-Polar Solute)', (px + 40) + (tR2 / 15.0) * (pw - 60) - 20, py + 50);
      } else {
        // TLC Plate Visualization
        var tx = 280;
        var ty = 40;
        var tw = 240;
        var th = 300;

        ctx.fillStyle = '#f8fafc'; // White silica gel
        ctx.strokeStyle = '#475569';
        ctx.lineWidth = 2;
        ctx.fillRect(tx, ty, tw, th);
        ctx.strokeRect(tx, ty, tw, th);

        // Origin Baseline
        ctx.strokeStyle = '#94a3b8';
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(tx + 20, ty + th - 40);
        ctx.lineTo(tx + tw - 20, ty + th - 40);
        ctx.stroke();

        // Solvent Front
        ctx.beginPath();
        ctx.moveTo(tx + 20, ty + 30);
        ctx.lineTo(tx + tw - 20, ty + 30);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#64748b';
        ctx.font = '10px Inter, sans-serif';
        ctx.fillText('Solvent Front', tx + tw - 80, ty + 25);
        ctx.fillText('Origin Line', tx + tw - 70, ty + th - 45);

        // Solute Migration Spots (e.g. Ni²⁺ and Cu²⁺ with DMG/rubeanic acid)
        var rf1 = 0.25 + (polarity / 100.0) * 0.3;
        var rf2 = 0.55 + (polarity / 100.0) * 0.35;
        rf2 = Math.min(0.92, rf2);

        var spot1Y = (ty + th - 40) - rf1 * (th - 70);
        var spot2Y = (ty + th - 40) - rf2 * (th - 70);

        // Spot 1 (Ni²⁺ - Pink/Red DMG complex)
        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.ellipse(tx + 80, spot1Y, 12, 16, 0, 0, Math.PI * 2);
        ctx.fill();

        // Spot 2 (Cu²⁺ - Olive Green/Brown rubeanic acid complex)
        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.ellipse(tx + 160, spot2Y, 14, 20, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#0f172a';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillText('Ni²⁺ (Rf=' + rf1.toFixed(2) + ')', tx + 55, spot1Y - 20);
        ctx.fillText('Cu²⁺ (Rf=' + rf2.toFixed(2) + ')', tx + 135, spot2Y - 24);
      }

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // window.SimulationEngine Mount Adapter
  // =========================================================================
  var SIM_TITLES = {
    sim_chem_error_gaussian_statistics: "Gaussian Error Statistics & Confidence Boundary Simulator",
    sim_chem_precipitation_titration_solubility: "von Weimarn Relative Supersaturation & Precipitation Engine",
    sim_chem_edta_complexometric_titration: "EDTA Complexometric Titration & Conditional Constant Simulator",
    sim_chem_atomic_absorption_flameless_zeeman: "Atomic Absorption & Flameless Zeeman Background Correction",
    sim_chem_ion_exchange_breakthrough_curve: "Ion-Exchange Resin Breakthrough & Chloro-Anion Separation Engine",
    sim_chem_beer_lambert_spectrophotometer: "Beer-Lambert Law & Photometric Stray Light Analyzer",
    sim_chem_spectrophotometric_titration_curves: "Spectrophotometric Titration Curve & Molar Absorptivity Engine",
    sim_chem_solvent_extraction_partition: "Liquid-Liquid Extraction Partition Thermodynamics Simulator",
    sim_chem_chromatography_van_deemter_efficiency: "Chromatographic van Deemter Efficiency & Flow Rate Visualizer",
    sim_chem_hplc_tlc_separation_engine: "HPLC & Thin Layer Chromatography Multi-Mode Separation Engine"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.AnalyticalSims || typeof window.AnalyticalSims[simType] !== 'function') {
      console.warn('Simulation type not found in AnalyticalSims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Analytical Chemistry Interactive Simulation";
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
      window.AnalyticalSims[simType](canvasId, controlsId);
    }, 50);
  };

})();
'''

    with open('analytical-chemistry-sims.js', 'w', encoding='utf-8') as f:
        f.write(js_code)

    print("Successfully generated analytical-chemistry-sims.js")
    lines = len(js_code.splitlines())
    words = len(js_code.split())
    print(f"Stats: {lines} lines, {words} words, {len(js_code)} bytes")

if __name__ == '__main__':
    generate_sims_js()
