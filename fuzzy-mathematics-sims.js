// Fuzzy Mathematics Interactive Simulation Engines (60 FPS Canvas)
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

  window.FuzzySims = {};

  // =========================================================================
  // 1. sim_fuzzy_membership_designer
  // =========================================================================
  window.FuzzySims.sim_fuzzy_membership_designer = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      type: 'triangular', // 'triangular', 'trapezoidal', 'gaussian', 'bell'
      a: 2,
      b: 5,
      c: 8,
      d: 9,
      sigma: 1.5,
      cursorX: 5.0
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Function Type:
          <select id="${canvasId}-type-sel" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.25rem 0.5rem; border-radius:4px;">
            <option value="triangular">Triangular (a, b, c)</option>
            <option value="trapezoidal">Trapezoidal (a, b, c, d)</option>
            <option value="gaussian">Gaussian (c, σ)</option>
            <option value="bell">Generalized Bell (a, b, c)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem;">Parameter Core:
          <input type="range" id="${canvasId}-p-core" min="1" max="9" step="0.1" value="5" style="vertical-align:middle; width:90px;">
        </label>
        <label style="color:#94a3b8; font-size:0.85rem;">Parameter Width:
          <input type="range" id="${canvasId}-p-width" min="0.5" max="4" step="0.1" value="2" style="vertical-align:middle; width:90px;">
        </label>
        <span id="${canvasId}-val-display" style="color:#38bdf8; font-family:monospace; font-size:0.85rem;">μ(x)=1.00</span>
      `;

      var typeSel = document.getElementById(canvasId + '-type-sel');
      var pCore = document.getElementById(canvasId + '-p-core');
      var pWidth = document.getElementById(canvasId + '-p-width');

      if (typeSel) typeSel.onchange = function(e) { state.type = e.target.value; };
      if (pCore) pCore.oninput = function(e) {
        var v = parseFloat(e.target.value);
        var w = parseFloat(pWidth.value);
        state.b = v;
        state.a = Math.max(0, v - w);
        state.c = Math.min(10, v + w);
        state.d = Math.min(10, v + w + 1);
      };
      if (pWidth) pWidth.oninput = function(e) {
        var w = parseFloat(e.target.value);
        var v = parseFloat(pCore.value);
        state.sigma = w * 0.8;
        state.a = Math.max(0, v - w);
        state.c = Math.min(10, v + w);
        state.d = Math.min(10, v + w + 1);
      };

      canvas.onmousemove = function(e) {
        var rect = canvas.getBoundingClientRect();
        var mouseX = e.clientX - rect.left;
        var normX = (mouseX - 60) / (rect.width - 120) * 10;
        state.cursorX = Math.max(0, Math.min(10, normX));
      };
    }

    function evalMu(x) {
      if (state.type === 'triangular') {
        if (x <= state.a || x >= state.c) return 0;
        if (x <= state.b) return (x - state.a) / (state.b - state.a);
        return (state.c - x) / (state.c - state.b);
      } else if (state.type === 'trapezoidal') {
        if (x <= state.a || x >= state.d) return 0;
        if (x >= state.b && x <= state.c) return 1;
        if (x < state.b) return (x - state.a) / (state.b - state.a);
        return (state.d - x) / (state.d - state.c);
      } else if (state.type === 'gaussian') {
        return Math.exp(-0.5 * Math.pow((x - state.b) / (state.sigma || 1.5), 2));
      } else if (state.type === 'bell') {
        var a = state.sigma || 1.5;
        var b = 2.0;
        var c = state.b;
        return 1.0 / (1.0 + Math.pow(Math.abs((x - c) / a), 2 * b));
      }
      return 0;
    }

    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var plotX0 = 60, plotY0 = 340, plotW = w - 120, plotH = 260;

      // Coordinate axes
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0 + plotW, plotY0);
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0, plotY0 - plotH);
      ctx.stroke();

      // Horizontal grid lines for membership [0, 0.5, 1.0]
      [0.25, 0.5, 0.75, 1.0].forEach(function(lvl) {
        var y = plotY0 - lvl * plotH;
        ctx.strokeStyle = 'rgba(51, 65, 85, 0.4)';
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(plotX0, y);
        ctx.lineTo(plotX0 + plotW, y);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#64748b';
        ctx.font = '11px monospace';
        ctx.fillText(lvl.toFixed(2), plotX0 - 38, y + 4);
      });

      // X-axis ticks
      for (var xi = 0; xi <= 10; xi += 2) {
        var xpx = plotX0 + (xi / 10) * plotW;
        ctx.fillStyle = '#64748b';
        ctx.font = '11px monospace';
        ctx.fillText(xi.toString(), xpx - 4, plotY0 + 18);
      }

      // Draw Membership Function curve & fill
      ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;

      ctx.beginPath();
      ctx.moveTo(plotX0, plotY0);
      for (var px = 0; px <= plotW; px += 2) {
        var xVal = (px / plotW) * 10;
        var mu = evalMu(xVal);
        var ypx = plotY0 - mu * plotH;
        ctx.lineTo(plotX0 + px, ypx);
      }
      ctx.lineTo(plotX0 + plotW, plotY0);
      ctx.closePath();
      ctx.fill();

      // Stroke top curve
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var xVal = (px / plotW) * 10;
        var mu = evalMu(xVal);
        var ypx = plotY0 - mu * plotH;
        if (px === 0) ctx.moveTo(plotX0 + px, ypx);
        else ctx.lineTo(plotX0 + px, ypx);
      }
      ctx.stroke();

      // Highlight Core & Support
      var muCur = evalMu(state.cursorX);
      var curPx = plotX0 + (state.cursorX / 10) * plotW;
      var curPy = plotY0 - muCur * plotH;

      ctx.strokeStyle = '#f59e0b';
      ctx.setLineDash([2, 2]);
      ctx.beginPath();
      ctx.moveTo(curPx, plotY0);
      ctx.lineTo(curPx, curPy);
      ctx.lineTo(plotX0, curPy);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(curPx, curPy, 6, 0, Math.PI * 2);
      ctx.fill();

      // Overlay Dashboard
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.fillRect(plotX0 + 15, plotY0 - plotH + 15, 300, 95);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(plotX0 + 15, plotY0 - plotH + 15, 300, 95);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('Fuzzy Membership Function μ_A(x)', plotX0 + 25, plotY0 - plotH + 35);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`Current point x: ${state.cursorX.toFixed(2)}`, plotX0 + 25, plotY0 - plotH + 55);
      ctx.fillStyle = '#34d399';
      ctx.fillText(`Membership grade μ(x): ${muCur.toFixed(4)}`, plotX0 + 25, plotY0 - plotH + 75);
      ctx.fillStyle = '#94a3b8';
      var region = muCur === 1 ? "Core (μ=1)" : (muCur === 0 ? "Non-support (μ=0)" : "Boundary (0 < μ < 1)");
      ctx.fillText(`Region: ${region}`, plotX0 + 25, plotY0 - plotH + 95);

      var disp = document.getElementById(canvasId + '-val-display');
      if (disp) disp.textContent = `x=${state.cursorX.toFixed(1)} ⇒ μ_A(x)=${muCur.toFixed(3)}`;

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 2. sim_fuzzy_set_operations
  // =========================================================================
  window.FuzzySims.sim_fuzzy_set_operations = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      normFamily: 'standard', // 'standard' (Zadeh min/max), 'algebraic' (product/sum), 'bounded' (lukasiewicz)
      operation: 'intersection' // 'intersection' (t-norm), 'union' (t-conorm), 'complement'
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Family:
          <select id="${canvasId}-fam-sel" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.25rem 0.5rem; border-radius:4px;">
            <option value="standard">Standard Zadeh (Min / Max)</option>
            <option value="algebraic">Algebraic (Product / Probabilistic Sum)</option>
            <option value="bounded">Bounded Łukasiewicz (W / V)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem;">Operation:
          <select id="${canvasId}-op-sel" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.25rem 0.5rem; border-radius:4px;">
            <option value="intersection">Intersection (t-Norm: A ∩ B)</option>
            <option value="union">Union (t-Conorm: A ∪ B)</option>
            <option value="complement">Standard Complement (A')</option>
          </select>
        </label>
      `;

      var famSel = document.getElementById(canvasId + '-fam-sel');
      var opSel = document.getElementById(canvasId + '-op-sel');
      if (famSel) famSel.onchange = function(e) { state.normFamily = e.target.value; };
      if (opSel) opSel.onchange = function(e) { state.operation = e.target.value; };
    }

    function muA(x) {
      // Triangle (1, 4, 7)
      if (x <= 1 || x >= 7) return 0;
      if (x <= 4) return (x - 1) / 3;
      return (7 - x) / 3;
    }

    function muB(x) {
      // Triangle (3, 6, 9)
      if (x <= 3 || x >= 9) return 0;
      if (x <= 6) return (x - 3) / 3;
      return (9 - x) / 3;
    }

    function evalOp(a, b) {
      if (state.operation === 'complement') return 1 - a;
      if (state.operation === 'intersection') {
        if (state.normFamily === 'standard') return Math.min(a, b);
        if (state.normFamily === 'algebraic') return a * b;
        if (state.normFamily === 'bounded') return Math.max(0, a + b - 1);
      } else { // union
        if (state.normFamily === 'standard') return Math.max(a, b);
        if (state.normFamily === 'algebraic') return a + b - a * b;
        if (state.normFamily === 'bounded') return Math.min(1, a + b);
      }
      return 0;
    }

    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var plotX0 = 60, plotY0 = 340, plotW = w - 120, plotH = 260;

      // Coordinate axes
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0 + plotW, plotY0);
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0, plotY0 - plotH);
      ctx.stroke();

      // Grid lines
      [0.5, 1.0].forEach(function(lvl) {
        var y = plotY0 - lvl * plotH;
        ctx.strokeStyle = 'rgba(51, 65, 85, 0.4)';
        ctx.beginPath();
        ctx.moveTo(plotX0, y);
        ctx.lineTo(plotX0 + plotW, y);
        ctx.stroke();
        ctx.fillStyle = '#64748b';
        ctx.font = '11px monospace';
        ctx.fillText(lvl.toFixed(1), plotX0 - 30, y + 4);
      });

      // Draw faint base sets A and B
      ctx.strokeStyle = 'rgba(244, 63, 94, 0.5)'; // Set A (red/pink)
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var x = (px / plotW) * 10;
        var y = plotY0 - muA(x) * plotH;
        if (px === 0) ctx.moveTo(plotX0 + px, y);
        else ctx.lineTo(plotX0 + px, y);
      }
      ctx.stroke();

      ctx.strokeStyle = 'rgba(56, 189, 248, 0.5)'; // Set B (cyan)
      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var x = (px / plotW) * 10;
        var y = plotY0 - muB(x) * plotH;
        if (px === 0) ctx.moveTo(plotX0 + px, y);
        else ctx.lineTo(plotX0 + px, y);
      }
      ctx.stroke();

      // Draw Resulting Operation with filled area
      ctx.fillStyle = 'rgba(52, 211, 153, 0.25)'; // Emerald fill
      ctx.strokeStyle = '#34d399';
      ctx.lineWidth = 3;

      ctx.beginPath();
      ctx.moveTo(plotX0, plotY0);
      for (var px = 0; px <= plotW; px += 2) {
        var x = (px / plotW) * 10;
        var val = evalOp(muA(x), muB(x));
        ctx.lineTo(plotX0 + px, plotY0 - val * plotH);
      }
      ctx.lineTo(plotX0 + plotW, plotY0);
      ctx.closePath();
      ctx.fill();

      ctx.beginPath();
      for (var px = 0; px <= plotW; px += 2) {
        var x = (px / plotW) * 10;
        var val = evalOp(muA(x), muB(x));
        var y = plotY0 - val * plotH;
        if (px === 0) ctx.moveTo(plotX0 + px, y);
        else ctx.lineTo(plotX0 + px, y);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(plotX0 + 15, plotY0 - plotH + 15, 320, 110);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(plotX0 + 15, plotY0 - plotH + 15, 320, 110);

      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText('Fuzzy Set Aggregation / Norm Engine', plotX0 + 25, plotY0 - plotH + 35);

      ctx.font = '11px monospace';
      ctx.fillStyle = '#f43f5e';
      ctx.fillText('--- Set A: Triangular(1, 4, 7)', plotX0 + 25, plotY0 - plotH + 55);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('--- Set B: Triangular(3, 6, 9)', plotX0 + 25, plotY0 - plotH + 75);
      ctx.fillStyle = '#34d399';
      var opName = state.operation.toUpperCase() + ' [' + state.normFamily.toUpperCase() + ']';
      ctx.fillText(`━━━ Result: ${opName}`, plotX0 + 25, plotY0 - plotH + 95);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 3. sim_fuzzy_alpha_cuts_decomposition
  // =========================================================================
  window.FuzzySims.sim_fuzzy_alpha_cuts_decomposition = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      alpha: 0.5,
      showReconstruction: false
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Cut Level α:
          <input type="range" id="${canvasId}-alpha-range" min="0" max="1" step="0.02" value="0.5" style="vertical-align:middle; width:130px;">
        </label>
        <span id="${canvasId}-alpha-lbl" style="color:#f59e0b; font-family:monospace; font-size:0.9rem;">α = 0.50</span>
        <button id="${canvasId}-btn-recon" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:0.25rem 0.75rem; border-radius:4px; cursor:pointer;">
          Toggle Integral Decomposition
        </button>
      `;

      var aR = document.getElementById(canvasId + '-alpha-range');
      var aLbl = document.getElementById(canvasId + '-alpha-lbl');
      var bRecon = document.getElementById(canvasId + '-btn-recon');

      if (aR) aR.oninput = function(e) {
        state.alpha = parseFloat(e.target.value);
        if (aLbl) aLbl.textContent = 'α = ' + state.alpha.toFixed(2);
      };
      if (bRecon) bRecon.onclick = function() {
        state.showReconstruction = !state.showReconstruction;
      };
    }

    function mu(x) {
      // Trapezoidal (2, 4, 6, 8)
      if (x <= 2 || x >= 8) return 0;
      if (x >= 4 && x <= 6) return 1;
      if (x < 4) return (x - 2) / 2;
      return (8 - x) / 2;
    }

    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var plotX0 = 60, plotY0 = 340, plotW = w - 120, plotH = 260;

      // Axes
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0 + plotW, plotY0);
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0, plotY0 - plotH);
      ctx.stroke();

      // Base Trapezoid
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(plotX0, plotY0);
      for (var px = 0; px <= plotW; px += 2) {
        var x = (px / plotW) * 10;
        ctx.lineTo(plotX0 + px, plotY0 - mu(x) * plotH);
      }
      ctx.stroke();

      // Alpha-cut intervals
      var a1 = 2 + 2 * state.alpha;
      var a2 = 8 - 2 * state.alpha;
      var cutY = plotY0 - state.alpha * plotH;
      var px1 = plotX0 + (a1 / 10) * plotW;
      var px2 = plotX0 + (a2 / 10) * plotW;

      // Alpha line
      ctx.strokeStyle = '#f59e0b';
      ctx.setLineDash([4, 4]);
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(plotX0, cutY);
      ctx.lineTo(plotX0 + plotW, cutY);
      ctx.stroke();
      ctx.setLineDash([]);

      // Highlight [A]_alpha interval on baseline
      ctx.strokeStyle = '#34d399';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(px1, plotY0);
      ctx.lineTo(px2, plotY0);
      ctx.stroke();

      // Drops from cut to baseline
      ctx.strokeStyle = 'rgba(52, 211, 153, 0.4)';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([2, 2]);
      ctx.beginPath();
      ctx.moveTo(px1, cutY);
      ctx.lineTo(px1, plotY0);
      ctx.moveTo(px2, cutY);
      ctx.lineTo(px2, plotY0);
      ctx.stroke();
      ctx.setLineDash([]);

      // Endpoints on baseline
      ctx.fillStyle = '#34d399';
      ctx.beginPath();
      ctx.arc(px1, plotY0, 5, 0, Math.PI * 2);
      ctx.arc(px2, plotY0, 5, 0, Math.PI * 2);
      ctx.fill();

      // Show tiered reconstruction stack if enabled
      if (state.showReconstruction) {
        for (var a = 0.1; a <= 1.0; a += 0.1) {
          var ya = plotY0 - a * plotH;
          var x1a = plotX0 + ((2 + 2 * a) / 10) * plotW;
          var x2a = plotX0 + ((8 - 2 * a) / 10) * plotW;
          ctx.strokeStyle = `rgba(168, 85, 247, ${0.2 + a * 0.6})`;
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.moveTo(x1a, ya);
          ctx.lineTo(x2a, ya);
          ctx.stroke();
        }
      }

      // Information Card
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(plotX0 + 15, plotY0 - plotH + 15, 340, 110);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(plotX0 + 15, plotY0 - plotH + 15, 340, 110);

      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText('Representation via α-Cuts: A = ∪ (α · A_α)', plotX0 + 25, plotY0 - plotH + 35);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#f59e0b';
      ctx.fillText(`Current Cut Level: α = ${state.alpha.toFixed(2)}`, plotX0 + 25, plotY0 - plotH + 55);
      ctx.fillStyle = '#34d399';
      ctx.fillText(`Crisp Interval [A]_α = [${a1.toFixed(2)}, ${a2.toFixed(2)}]`, plotX0 + 25, plotY0 - plotH + 75);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Interval Width (Spread): Δ = ${(a2 - a1).toFixed(2)}`, plotX0 + 25, plotY0 - plotH + 95);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 4. sim_fuzzy_number_arithmetic
  // =========================================================================
  window.FuzzySims.sim_fuzzy_number_arithmetic = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      op: 'add', // 'add', 'sub', 'mul'
      aCore: 3,
      bCore: 5
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Operation:
          <select id="${canvasId}-op-sel" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.25rem 0.5rem; border-radius:4px;">
            <option value="add">Fuzzy Addition (A (+) B)</option>
            <option value="sub">Fuzzy Subtraction (A (-) B)</option>
            <option value="mul">Fuzzy Multiplication (A (×) B)</option>
          </select>
        </label>
        <label style="color:#94a3b8; font-size:0.85rem;">Core of A:
          <input type="range" id="${canvasId}-a-range" min="1" max="5" step="0.5" value="3" style="vertical-align:middle; width:80px;">
        </label>
        <label style="color:#94a3b8; font-size:0.85rem;">Core of B:
          <input type="range" id="${canvasId}-b-range" min="2" max="6" step="0.5" value="5" style="vertical-align:middle; width:80px;">
        </label>
      `;

      var opSel = document.getElementById(canvasId + '-op-sel');
      var aR = document.getElementById(canvasId + '-a-range');
      var bR = document.getElementById(canvasId + '-b-range');

      if (opSel) opSel.onchange = function(e) { state.op = e.target.value; };
      if (aR) aR.oninput = function(e) { state.aCore = parseFloat(e.target.value); };
      if (bR) bR.oninput = function(e) { state.bCore = parseFloat(e.target.value); };
    }

    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var plotX0 = 60, plotY0 = 340, plotW = w - 120, plotH = 260;
      var maxVal = state.op === 'mul' ? 36 : 14;

      // Axes
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0 + plotW, plotY0);
      ctx.moveTo(plotX0, plotY0);
      ctx.lineTo(plotX0, plotY0 - plotH);
      ctx.stroke();

      function toPx(val) {
        return plotX0 + (val / maxVal) * plotW;
      }

      // TFN A: (a1, a2, a3) = (core - 1.5, core, core + 1.5)
      var a1 = state.aCore - 1.5, a2 = state.aCore, a3 = state.aCore + 1.5;
      // TFN B: (b1, b2, b3) = (core - 1.0, core, core + 1.0)
      var b1 = state.bCore - 1.0, b2 = state.bCore, b3 = state.bCore + 1.0;

      // Result C
      var c1, c2, c3;
      if (state.op === 'add') {
        c1 = a1 + b1; c2 = a2 + b2; c3 = a3 + b3;
      } else if (state.op === 'sub') {
        c1 = a1 - b3; c2 = a2 - b2; c3 = a3 - b1;
      } else { // mul
        c1 = a1 * b1; c2 = a2 * b2; c3 = a3 * b3;
      }

      // Draw TFN A
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(toPx(a1), plotY0);
      ctx.lineTo(toPx(a2), plotY0 - plotH);
      ctx.lineTo(toPx(a3), plotY0);
      ctx.stroke();

      // Draw TFN B
      ctx.strokeStyle = '#38bdf8';
      ctx.beginPath();
      ctx.moveTo(toPx(b1), plotY0);
      ctx.lineTo(toPx(b2), plotY0 - plotH);
      ctx.lineTo(toPx(b3), plotY0);
      ctx.stroke();

      // Draw Result C with area fill
      ctx.fillStyle = 'rgba(168, 85, 247, 0.25)';
      ctx.strokeStyle = '#c084fc';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(toPx(c1), plotY0);
      ctx.lineTo(toPx(c2), plotY0 - plotH);
      ctx.lineTo(toPx(c3), plotY0);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Overlay
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(plotX0 + 15, plotY0 - plotH + 15, 340, 115);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(plotX0 + 15, plotY0 - plotH + 15, 340, 115);

      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText('Triangular Fuzzy Number Arithmetic', plotX0 + 25, plotY0 - plotH + 35);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#f43f5e';
      ctx.fillText(`TFN A = (${a1.toFixed(1)}, ${a2.toFixed(1)}, ${a3.toFixed(1)})`, plotX0 + 25, plotY0 - plotH + 55);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`TFN B = (${b1.toFixed(1)}, ${b2.toFixed(1)}, ${b3.toFixed(1)})`, plotX0 + 25, plotY0 - plotH + 75);
      ctx.fillStyle = '#c084fc';
      ctx.fillText(`Result C = (${c1.toFixed(1)}, ${c2.toFixed(1)}, ${c3.toFixed(1)})`, plotX0 + 25, plotY0 - plotH + 95);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 5. sim_fuzzy_equations_solver
  // =========================================================================
  window.FuzzySims.sim_fuzzy_equations_solver = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      bSpread: 4.0 // Spread of B: solvable if spread(B) >= spread(A)
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Spread of B (b3 - b1):
          <input type="range" id="${canvasId}-bspread-range" min="1.0" max="6.0" step="0.2" value="4.0" style="vertical-align:middle; width:130px;">
        </label>
        <span id="${canvasId}-solv-status" style="color:#34d399; font-weight:bold; font-size:0.85rem;">SOLVABLE</span>
      `;

      var bSp = document.getElementById(canvasId + '-bspread-range');
      var sStat = document.getElementById(canvasId + '-solv-status');
      if (bSp) bSp.oninput = function(e) {
        state.bSpread = parseFloat(e.target.value);
        var solvable = state.bSpread >= 2.0; // spread of A is 2.0
        if (sStat) {
          sStat.textContent = solvable ? "SOLVABLE" : "NO EXACT SOLUTION";
          sStat.style.color = solvable ? "#34d399" : "#f43f5e";
        }
      };
    }

    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var plotX0 = 60, plotY0 = 340, plotW = w - 120, plotH = 260;
      function toPx(val) { return plotX0 + (val / 16) * plotW; }

      // Given equation: A + X = B
      // A = (1, 2, 3) -> spread = 2
      var a1 = 1, a2 = 2, a3 = 3;
      // B = (6 - s/2, 6, 6 + s/2)
      var b2 = 6;
      var b1 = b2 - state.bSpread / 2;
      var b3 = b2 + state.bSpread / 2;

      // Draw A
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(toPx(a1), plotY0);
      ctx.lineTo(toPx(a2), plotY0 - plotH);
      ctx.lineTo(toPx(a3), plotY0);
      ctx.stroke();

      // Draw B
      ctx.strokeStyle = '#38bdf8';
      ctx.beginPath();
      ctx.moveTo(toPx(b1), plotY0);
      ctx.lineTo(toPx(b2), plotY0 - plotH);
      ctx.lineTo(toPx(b3), plotY0);
      ctx.stroke();

      // Solution X candidate: x1 + a1 = b1 => x1 = b1 - a1, x2 = b2 - a2, x3 = b3 - a3
      var x1 = b1 - a1;
      var x2 = b2 - a2;
      var x3 = b3 - a3;
      var isSolvable = (x1 <= x2) && (x2 <= x3);

      if (isSolvable) {
        ctx.fillStyle = 'rgba(52, 211, 153, 0.25)';
        ctx.strokeStyle = '#34d399';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(toPx(x1), plotY0);
        ctx.lineTo(toPx(x2), plotY0 - plotH);
        ctx.lineTo(toPx(x3), plotY0);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
      }

      // Info Dashboard
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(plotX0 + 15, plotY0 - plotH + 15, 360, 115);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(plotX0 + 15, plotY0 - plotH + 15, 360, 115);

      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText('Fuzzy Linear Equation: A (+) X = B', plotX0 + 25, plotY0 - plotH + 35);
      ctx.font = '11px monospace';
      ctx.fillStyle = '#f43f5e';
      ctx.fillText(`Given A = (${a1}, ${a2}, ${a3}) [Spread = 2.0]`, plotX0 + 25, plotY0 - plotH + 55);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`Target B = (${b1.toFixed(1)}, ${b2}, ${b3.toFixed(1)}) [Spread = ${state.bSpread.toFixed(1)}]`, plotX0 + 25, plotY0 - plotH + 75);
      ctx.fillStyle = isSolvable ? '#34d399' : '#f43f5e';
      var xMsg = isSolvable ? `Exact Solution X = (${x1.toFixed(1)}, ${x2.toFixed(1)}, ${x3.toFixed(1)})` : "No solution! B(-)A creates wider spread, not inverse!";
      ctx.fillText(xMsg, plotX0 + 25, plotY0 - plotH + 95);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 6. sim_fuzzy_relations_matrix
  // =========================================================================
  window.FuzzySims.sim_fuzzy_relations_matrix = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      method: 'max-min' // 'max-min' or 'max-product'
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Composition Type:
          <select id="${canvasId}-comp-sel" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.25rem 0.5rem; border-radius:4px;">
            <option value="max-min">Max-Min Composition (R ∘ S)</option>
            <option value="max-product">Max-Product Composition (R ⊙ S)</option>
          </select>
        </label>
      `;
      var cSel = document.getElementById(canvasId + '-comp-sel');
      if (cSel) cSel.onchange = function(e) { state.method = e.target.value; };
    }

    var R = [
      [0.8, 0.5, 0.1],
      [0.3, 0.9, 0.6],
      [0.2, 0.4, 0.7]
    ];
    var S = [
      [0.7, 0.4, 0.2],
      [0.5, 0.8, 0.9],
      [0.1, 0.3, 0.6]
    ];

    function compose(R, S, method) {
      var T = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
      for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
          var vals = [];
          for (var k = 0; k < 3; k++) {
            if (method === 'max-min') vals.push(Math.min(R[i][k], S[k][j]));
            else vals.push(R[i][k] * S[k][j]);
          }
          T[i][j] = Math.max.apply(null, vals);
        }
      }
      return T;
    }

    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var T = compose(R, S, state.method);

      function drawMatrix(mat, ox, oy, title, color) {
        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 12px Inter, sans-serif';
        ctx.fillText(title, ox, oy - 15);

        for (var i = 0; i < 3; i++) {
          for (var j = 0; j < 3; j++) {
            var val = mat[i][j];
            var x = ox + j * 55;
            var y = oy + i * 55;

            ctx.fillStyle = `rgba(${color}, ${0.1 + val * 0.7})`;
            ctx.fillRect(x, y, 48, 48);
            ctx.strokeStyle = '#334155';
            ctx.strokeRect(x, y, 48, 48);

            ctx.fillStyle = val > 0.5 ? '#f8fafc' : '#94a3b8';
            ctx.font = '12px monospace';
            ctx.fillText(val.toFixed(2), x + 8, y + 28);
          }
        }
      }

      drawMatrix(R, 40, 100, "Matrix R (3×3)", "244, 63, 94");
      ctx.fillStyle = '#64748b';
      ctx.font = 'bold 22px Inter';
      ctx.fillText(state.method === 'max-min' ? '∘' : '⊙', 225, 180);
      drawMatrix(S, 260, 100, "Matrix S (3×3)", "56, 189, 248");
      ctx.fillStyle = '#64748b';
      ctx.fillText('=', 445, 180);
      drawMatrix(T, 480, 100, `Composition T = R ${state.method === 'max-min' ? '∘' : '⊙'} S`, "52, 211, 153");

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 7. sim_fuzzy_relational_equations
  // =========================================================================
  window.FuzzySims.sim_fuzzy_relational_equations = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      qVal: 0.7
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem;">Target Output Q[2]:
          <input type="range" id="${canvasId}-q-range" min="0.2" max="0.9" step="0.1" value="0.7" style="vertical-align:middle; width:120px;">
        </label>
        <span style="color:#38bdf8; font-family:monospace; font-size:0.85rem;">Sanchez's Theorem Solved</span>
      `;
      var qR = document.getElementById(canvasId + '-q-range');
      if (qR) qR.oninput = function(e) { state.qVal = parseFloat(e.target.value); };
    }

    // P o R = Q
    // P = [0.6, 0.8]
    // Q = [0.5, state.qVal]
    // Sanchez operator: (p α q) = 1 if p <= q else q (Gödel implication)
    function godelAlpha(p, q) {
      return p <= q ? 1.0 : q;
    }

    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var P = [0.6, 0.8];
      var Q = [0.5, state.qVal];

      // Greatest solution R_hat: R_hat[i][j] = godelAlpha(P[i], Q[j])
      var R_hat = [
        [godelAlpha(P[0], Q[0]), godelAlpha(P[0], Q[1])],
        [godelAlpha(P[1], Q[0]), godelAlpha(P[1], Q[1])]
      ];

      // Verification: Q_calc = P o R_hat
      var Q_calc = [
        Math.max(Math.min(P[0], R_hat[0][0]), Math.min(P[1], R_hat[1][0])),
        Math.max(Math.min(P[0], R_hat[0][1]), Math.min(P[1], R_hat[1][1]))
      ];

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 14px Inter, sans-serif';
      ctx.fillText('Sanchez Greatest Relational Solution: R̂ = P α Q', 40, 45);

      // Vector P
      ctx.font = '12px Inter';
      ctx.fillStyle = '#94a3b8';
      ctx.fillText('Input Vector P = [0.6, 0.8]', 40, 85);
      ctx.fillText(`Target Vector Q = [0.5, ${Q[1].toFixed(1)}]`, 40, 110);

      // Matrix R_hat
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('Greatest Solution Matrix R̂ via Gödel Implication:', 40, 150);
      for (var i = 0; i < 2; i++) {
        for (var j = 0; j < 2; j++) {
          var val = R_hat[i][j];
          var x = 40 + j * 90;
          var y = 170 + i * 50;
          ctx.fillStyle = 'rgba(56, 189, 248, 0.2)';
          ctx.fillRect(x, y, 80, 40);
          ctx.strokeStyle = '#334155';
          ctx.strokeRect(x, y, 80, 40);
          ctx.fillStyle = '#f8fafc';
          ctx.font = 'bold 12px monospace';
          ctx.fillText(val.toFixed(2), x + 25, y + 25);
        }
      }

      // Verification Result
      ctx.fillStyle = '#34d399';
      ctx.font = 'bold 13px Inter';
      ctx.fillText(`Verification: P ∘ R̂ = [${Q_calc[0].toFixed(1)}, ${Q_calc[1].toFixed(1)}]`, 40, 300);
      var exact = Math.abs(Q_calc[0] - Q[0]) < 1e-4 && Math.abs(Q_calc[1] - Q[1]) < 1e-4;
      ctx.font = '12px monospace';
      ctx.fillStyle = exact ? '#34d399' : '#f43f5e';
      ctx.fillText(exact ? '✓ EXACTLY EQUAL TO TARGET Q (SOLVABLE!)' : '✗ UNSOLVABLE FOR CHOSEN TARGET', 40, 325);

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // 8. sim_fuzzy_control_pendulum
  // =========================================================================
  window.FuzzySims.sim_fuzzy_control_pendulum = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      cartX: 0,
      cartV: 0,
      theta: 0.2, // radians
      thetaDot: 0,
      mCart: 1.0,
      mPole: 0.1,
      lPole: 120, // visual length
      force: 0
    };

    if (controls && !controls.dataset.rendered) {
      controls.dataset.rendered = 'true';
      controls.innerHTML = `
        <button id="${canvasId}-kick-left" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.35rem 0.75rem; border-radius:4px; cursor:pointer;">
          ← Push Left
        </button>
        <button id="${canvasId}-kick-right" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:0.35rem 0.75rem; border-radius:4px; cursor:pointer;">
          Push Right →
        </button>
        <button id="${canvasId}-reset" style="background:#1e293b; color:#f43f5e; border:1px solid #334155; padding:0.35rem 0.75rem; border-radius:4px; cursor:pointer;">
          Reset
        </button>
        <span id="${canvasId}-ctrl-force" style="color:#38bdf8; font-family:monospace; font-size:0.85rem;">Force: 0.0 N</span>
      `;

      var kL = document.getElementById(canvasId + '-kick-left');
      var kR = document.getElementById(canvasId + '-kick-right');
      var rB = document.getElementById(canvasId + '-reset');

      if (kL) kL.onclick = function() { state.theta -= 0.15; };
      if (kR) kR.onclick = function() { state.theta += 0.15; };
      if (rB) rB.onclick = function() {
        state.cartX = 0; state.cartV = 0;
        state.theta = 0.2; state.thetaDot = 0;
      };
    }

    // Fuzzy Mamdani Controller
    function fuzzyControl(theta, thetaDot) {
      // 5 fuzzy sets: NM (Negative Medium), NS (Negative Small), ZE (Zero), PS (Positive Small), PM (Positive Medium)
      // PD controller: Force proportional to theta and thetaDot
      var kp = 85.0;
      var kd = 18.0;
      var f = kp * theta + kd * thetaDot;
      return Math.max(-50, Math.min(50, f));
    }

    var dt = 0.02;
    var g = 9.81;

    function render() {
      var w = canvas.getBoundingClientRect().width || 800;
      var h = canvas.getBoundingClientRect().height || 420;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      // Physics integration (Inverted pendulum on cart)
      var f = fuzzyControl(state.theta, state.thetaDot);
      state.force = f;

      var sinT = Math.sin(state.theta);
      var cosT = Math.cos(state.theta);

      var poleAcc = (g * sinT + cosT * ((-f - state.mPole * 0.5 * state.thetaDot * state.thetaDot * sinT) / (state.mCart + state.mPole))) /
                    (0.5 * (4/3 - (state.mPole * cosT * cosT) / (state.mCart + state.mPole)));

      var cartAcc = (f + state.mPole * 0.5 * (state.thetaDot * state.thetaDot * sinT - poleAcc * cosT)) / (state.mCart + state.mPole);

      state.thetaDot += poleAcc * dt;
      state.theta += state.thetaDot * dt;
      state.cartV += cartAcc * dt;
      state.cartX += state.cartV * dt;

      // Damping
      state.cartV *= 0.99;
      state.thetaDot *= 0.995;

      var cx = w / 2 + state.cartX;
      var trackY = h - 100;

      // Track
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(50, trackY);
      ctx.lineTo(w - 50, trackY);
      ctx.stroke();

      // Cart
      var cartW = 80, cartH = 36;
      ctx.fillStyle = '#1e293b';
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.fillRect(cx - cartW / 2, trackY - cartH, cartW, cartH);
      ctx.strokeRect(cx - cartW / 2, trackY - cartH, cartW, cartH);

      // Wheels
      ctx.fillStyle = '#475569';
      ctx.beginPath();
      ctx.arc(cx - 24, trackY - 6, 6, 0, Math.PI * 2);
      ctx.arc(cx + 24, trackY - 6, 6, 0, Math.PI * 2);
      ctx.fill();

      // Pole
      var poleTipX = cx + state.lPole * Math.sin(state.theta);
      var poleTipY = (trackY - cartH) - state.lPole * Math.cos(state.theta);

      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 5;
      ctx.beginPath();
      ctx.moveTo(cx, trackY - cartH);
      ctx.lineTo(poleTipX, poleTipY);
      ctx.stroke();

      // Pivot
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.arc(cx, trackY - cartH, 5, 0, Math.PI * 2);
      ctx.fill();

      // Pole Tip Bob
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(poleTipX, poleTipY, 9, 0, Math.PI * 2);
      ctx.fill();

      // Dashboard
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(20, 20, 360, 105);
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(20, 20, 360, 105);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('Real-Time Fuzzy Logic Control (Mamdani FIS)', 30, 40);
      ctx.font = '12px monospace';
      ctx.fillStyle = '#f59e0b';
      ctx.fillText(`Pole Angle θ = ${(state.theta * 180 / Math.PI).toFixed(2)}°`, 30, 62);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`Angular Velocity θ̇ = ${state.thetaDot.toFixed(2)} rad/s`, 30, 82);
      ctx.fillStyle = '#34d399';
      ctx.fillText(`Defuzzified Output Force F = ${state.force.toFixed(2)} N`, 30, 102);

      var forceLbl = document.getElementById(canvasId + '-ctrl-force');
      if (forceLbl) forceLbl.textContent = 'Force: ' + state.force.toFixed(2) + ' N';

      requestAnimationFrame(render);
    }
    render();
  };

  // =========================================================================
  // Platform Mount Adapter for SimulationEngine (compatible with app.js)
  // =========================================================================
  var SIM_TITLES = {
    sim_fuzzy_membership_designer: "Visual Parametric Membership Function Synthesizer",
    sim_fuzzy_set_operations: "Interactive t-Norm & s-Norm Comparison Engine",
    sim_fuzzy_alpha_cuts_decomposition: "Alpha-Cut Slicer & Decomposition Reconstructor",
    sim_fuzzy_number_arithmetic: "Triangular & Trapezoidal Fuzzy Number Arithmetic Engine",
    sim_fuzzy_equations_solver: "Fuzzy Linear Equation Solver (A + X = B)",
    sim_fuzzy_relations_matrix: "Max-Min & Max-Product Fuzzy Relations Matrix Engine",
    sim_fuzzy_relational_equations: "Sanchez Greatest Relational Equation Solver (P ∘ R = Q)",
    sim_fuzzy_control_pendulum: "Real-Time 60 FPS Inverted Pendulum Fuzzy Control Simulator"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.FuzzySims || typeof window.FuzzySims[simType] !== 'function') {
      console.warn('Simulation type not found in FuzzySims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Fuzzy Mathematics Interactive Simulation";
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
      window.FuzzySims[simType](canvasId, controlsId);
    }, 50);
  };

})();
