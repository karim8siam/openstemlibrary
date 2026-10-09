// Organic Chemistry I Interactive Simulation Engines (60 FPS Canvas)
// Strictly ZERO course numbers or marks.
(function() {
  'use strict';

  // Setup Canvas with dimension caching to prevent per-frame GPU reallocations
  function setupCanvas(canvas) {
    if (!canvas) return { ctx: null, width: 800, height: 420 };
    var dpr = window.devicePixelRatio || 1;
    var width = canvas._cssWidth;
    var height = canvas._cssHeight;

    if (!width || !height) {
      var rect = canvas.getBoundingClientRect();
      width = Math.floor(rect.width > 0 ? rect.width : (canvas.parentElement ? canvas.parentElement.clientWidth : 800)) || 800;
      height = Math.floor(rect.height > 0 ? rect.height : 420) || 420;
      canvas._cssWidth = width;
      canvas._cssHeight = height;
    }

    var targetW = Math.round(width * dpr);
    var targetH = Math.round(height * dpr);

    if (canvas.width !== targetW || canvas.height !== targetH) {
      canvas.width = targetW;
      canvas.height = targetH;
      var ctx = canvas.getContext('2d');
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    var ctx = canvas.getContext('2d');
    return { ctx: ctx, width: width, height: height };
  }

  if (typeof window !== 'undefined') {
    window.addEventListener('resize', function() {
      document.querySelectorAll('.sim-canvas').forEach(function(c) {
        c._cssWidth = null;
        c._cssHeight = null;
      });
    });
  }

  window.Org1Sims = {};

  // =========================================================================
  // 1. sim_chem_organic_hybridization_resonance (Unit 1)
  // 3D Hybrid Orbitals, Sigma/Pi Overlap & Resonance Hybrid Mixer
  // =========================================================================
  window.Org1Sims.sim_chem_organic_hybridization_resonance = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      mode: 'sp3', // sp3, sp2, sp, resonance
      rotX: 0.35,
      rotY: 0.55,
      isDragging: false,
      lastMouseX: 0,
      lastMouseY: 0,
      resonanceWeight: 0.5, // 0 = form A, 1 = form B
      phase: 0
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Hybridization & Mode:</label>
        <select id="${controlsId}-mode" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="sp3">sp³ Hybridization (Tetrahedral 109.5°)</option>
          <option value="sp2">sp² Hybridization (Trigonal Planar 120° + pz)</option>
          <option value="sp">sp Hybridization (Linear 180° + py, pz)</option>
          <option value="resonance">Resonance Hybrid Mixer (Acetate / Allyl)</option>
        </select>
        <div id="${controlsId}-res-container" style="display:none; align-items:center; gap:8px;">
          <span style="color:#94a3b8; font-size:0.85rem;">Form 1</span>
          <input type="range" id="${controlsId}-res-weight" min="0" max="1" step="0.01" value="0.5" style="width:110px;">
          <span style="color:#94a3b8; font-size:0.85rem;">Form 2</span>
        </div>
        <button id="${controlsId}-reset" style="background:#3b82f6; color:#fff; border:none; padding:4px 12px; border-radius:4px; font-size:0.85rem; cursor:pointer;">Reset View</button>
      `;

      var modeSelect = document.getElementById(controlsId + '-mode');
      var resContainer = document.getElementById(controlsId + '-res-container');
      var resSlider = document.getElementById(controlsId + '-res-weight');
      var resetBtn = document.getElementById(controlsId + '-reset');

      modeSelect.addEventListener('change', function(e) {
        state.mode = e.target.value;
        resContainer.style.display = (state.mode === 'resonance') ? 'flex' : 'none';
      });

      if (resSlider) {
        resSlider.addEventListener('input', function(e) {
          state.resonanceWeight = parseFloat(e.target.value);
        });
      }

      resetBtn.addEventListener('click', function() {
        state.rotX = 0.35;
        state.rotY = 0.55;
      });
    }

    function onMouseDown(e) {
      state.isDragging = true;
      state.lastMouseX = e.clientX || (e.touches && e.touches[0].clientX);
      state.lastMouseY = e.clientY || (e.touches && e.touches[0].clientY);
    }
    function onMouseMove(e) {
      if (!state.isDragging) return;
      var clientX = e.clientX || (e.touches && e.touches[0].clientX);
      var clientY = e.clientY || (e.touches && e.touches[0].clientY);
      var dx = clientX - state.lastMouseX;
      var dy = clientY - state.lastMouseY;
      state.rotY += dx * 0.01;
      state.rotX += dy * 0.01;
      state.lastMouseX = clientX;
      state.lastMouseY = clientY;
    }
    function onMouseUp() { state.isDragging = false; }

    canvas.addEventListener('mousedown', onMouseDown);
    window.addEventListener('mousemove', onMouseMove);
    window.addEventListener('mouseup', onMouseUp);
    canvas.addEventListener('touchstart', onMouseDown, { passive: true });
    window.addEventListener('touchmove', onMouseMove, { passive: true });
    window.addEventListener('touchend', onMouseUp);

    function project(x, y, z, cx, cy, scale) {
      var cosY = Math.cos(state.rotY), sinY = Math.sin(state.rotY);
      var x1 = x * cosY - z * sinY;
      var z1 = x * sinY + z * cosY;
      var cosX = Math.cos(state.rotX), sinX = Math.sin(state.rotX);
      var y2 = y * cosX - z1 * sinX;
      var z2 = y * sinX + z1 * cosX;
      var fov = 450 / (450 + z2);
      return { x: cx + x1 * scale * fov, y: cy + y2 * scale * fov, z: z2 };
    }

    function drawLobe(cx, cy, dirX, dirY, dirZ, length, width, color1, color2) {
      var steps = 18;
      for (var i = 0; i <= steps; i++) {
        var t = i / steps;
        var r = Math.sin(t * Math.PI) * width;
        var dist = t * length;
        var px = dirX * dist;
        var py = dirY * dist;
        var pz = dirZ * dist;
        var p = project(px, py, pz, cx, cy, 1);
        ctx.beginPath();
        ctx.arc(p.x, p.y, Math.max(2, r), 0, Math.PI * 2);
        var grad = ctx.createRadialGradient(p.x - r*0.3, p.y - r*0.3, 1, p.x, p.y, r);
        grad.addColorStop(0, color1);
        grad.addColorStop(1, color2);
        ctx.fillStyle = grad;
        ctx.fill();
      }
    }

    function render() {
      setup = setupCanvas(canvas);
      ctx = setup.ctx;
      var w = setup.width;
      var h = setup.height;
      state.phase += 0.02;

      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      // Grid background
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      for (var gx = 20; gx < w; gx += 40) {
        ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, h); ctx.stroke();
      }
      for (var gy = 20; gy < h; gy += 40) {
        ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(w, gy); ctx.stroke();
      }

      var cx = w * 0.42;
      var cy = h * 0.52;

      // Draw Orbitals based on mode
      if (state.mode === 'sp3') {
        // 4 tetrahedral lobes pointing to vertices of cube
        var tetDirs = [
          [ 1,  1,  1],
          [-1, -1,  1],
          [-1,  1, -1],
          [ 1, -1, -1]
        ];
        tetDirs.forEach(function(d, idx) {
          var mag = Math.sqrt(d[0]*d[0] + d[1]*d[1] + d[2]*d[2]);
          var dx = d[0]/mag, dy = d[1]/mag, dz = d[2]/mag;
          drawLobe(cx, cy, dx, dy, dz, 130, 24, '#60a5fa', 'rgba(37, 99, 235, 0.25)');
          // Small back lobe
          drawLobe(cx, cy, -dx, -dy, -dz, 35, 10, '#f87171', 'rgba(239, 68, 68, 0.2)');
        });
        // Central carbon atom
        var cp = project(0, 0, 0, cx, cy, 1);
        ctx.beginPath();
        ctx.arc(cp.x, cp.y, 16, 0, Math.PI * 2);
        ctx.fillStyle = '#334155'; ctx.fill();
        ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 2; ctx.stroke();
        ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('C', cp.x, cp.y);

      } else if (state.mode === 'sp2') {
        // 3 trigonal planar lobes at 120 deg in xy plane
        for (var a = 0; a < 3; a++) {
          var angle = a * (Math.PI * 2 / 3);
          var dx = Math.cos(angle), dy = Math.sin(angle), dz = 0;
          drawLobe(cx, cy, dx, dy, dz, 125, 22, '#34d399', 'rgba(16, 185, 129, 0.25)');
          drawLobe(cx, cy, -dx, -dy, 0, 32, 9, '#fbbf24', 'rgba(245, 158, 11, 0.2)');
        }
        // Unhybridized pz orbital perpendicular (z-axis)
        drawLobe(cx, cy, 0, 0, 1, 110, 20, '#f472b6', 'rgba(236, 72, 153, 0.25)');
        drawLobe(cx, cy, 0, 0, -1, 110, 20, '#818cf8', 'rgba(99, 102, 241, 0.25)');
        var cp = project(0, 0, 0, cx, cy, 1);
        ctx.beginPath();
        ctx.arc(cp.x, cp.y, 15, 0, Math.PI * 2);
        ctx.fillStyle = '#334155'; ctx.fill();
        ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('C', cp.x, cp.y);

      } else if (state.mode === 'sp') {
        // 2 collinear sp lobes along x-axis
        drawLobe(cx, cy, 1, 0, 0, 130, 24, '#38bdf8', 'rgba(14, 165, 233, 0.25)');
        drawLobe(cx, cy, -1, 0, 0, 130, 24, '#38bdf8', 'rgba(14, 165, 233, 0.25)');
        // 2 perpendicular p-orbitals: py and pz
        drawLobe(cx, cy, 0, 1, 0, 100, 18, '#fb923c', 'rgba(249, 115, 22, 0.25)');
        drawLobe(cx, cy, 0, -1, 0, 100, 18, '#fb923c', 'rgba(249, 115, 22, 0.25)');
        drawLobe(cx, cy, 0, 0, 1, 100, 18, '#a78bfa', 'rgba(139, 92, 246, 0.25)');
        drawLobe(cx, cy, 0, 0, -1, 100, 18, '#a78bfa', 'rgba(139, 92, 246, 0.25)');
        var cp = project(0, 0, 0, cx, cy, 1);
        ctx.beginPath();
        ctx.arc(cp.x, cp.y, 14, 0, Math.PI * 2);
        ctx.fillStyle = '#334155'; ctx.fill();
        ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('C', cp.x, cp.y);

      } else if (state.mode === 'resonance') {
        // Resonance hybrid visualization (Allyl / Carboxylate system)
        var wA = 1 - state.resonanceWeight;
        var wB = state.resonanceWeight;
        var bond1Order = 1.0 + wA * 1.0;
        var bond2Order = 1.0 + wB * 1.0;
        var qLeft = -wA;
        var qRight = -wB;

        // Draw 3-atom conjugated backbone: O1 - C - O2 or C1 - C2 - C3
        var xC = cx, yC = cy - 20;
        var xL = cx - 120, yL = cy + 70;
        var xR = cx + 120, yR = cy + 70;

        // Bonds
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 4;
        ctx.beginPath(); ctx.moveTo(xC, yC); ctx.lineTo(xL, yL); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(xC, yC); ctx.lineTo(xR, yR); ctx.stroke();

        // Delocalized pi bond dashed line
        ctx.save();
        ctx.setLineDash([6, 4]);
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(xL + 10, yL - 10); ctx.quadraticCurveTo(xC, yC - 35, xR - 10, yR - 10); ctx.stroke();
        ctx.restore();

        // Atom nodes
        function drawAtom(x, y, sym, col, charge) {
          ctx.beginPath(); ctx.arc(x, y, 22, 0, Math.PI * 2);
          ctx.fillStyle = col; ctx.fill();
          ctx.strokeStyle = '#f8fafc'; ctx.lineWidth = 2; ctx.stroke();
          ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 15px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
          ctx.fillText(sym, x, y);
          // Charge label
          ctx.fillStyle = '#f43f5e'; ctx.font = 'bold 12px monospace';
          var chgText = (charge < -0.05) ? (charge.toFixed(2) + ' δ⁻') : (charge > 0.05 ? ('+' + charge.toFixed(2)) : '0');
          ctx.fillText(chgText, x, y - 32);
        }

        drawAtom(xC, yC, 'C', '#334155', +0.2);
        drawAtom(xL, yL, 'O₁', '#dc2626', qLeft);
        drawAtom(xR, yR, 'O₂', '#dc2626', qRight);

        // Resonance telemetry box
        ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 1;
        ctx.fillRect(w - 260, 20, 240, 160);
        ctx.strokeRect(w - 260, 20, 240, 160);

        ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 13px sans-serif'; ctx.textAlign = 'left';
        ctx.fillText('Resonance Hybrid Telemetry', w - 245, 45);
        ctx.fillStyle = '#cbd5e1'; ctx.font = '12px monospace';
        ctx.fillText('Canonical Form A: ' + (wA * 100).toFixed(0) + '%', w - 245, 72);
        ctx.fillText('Canonical Form B: ' + (wB * 100).toFixed(0) + '%', w - 245, 95);
        ctx.fillText('C–O₁ Bond Order:  ' + bond1Order.toFixed(2), w - 245, 118);
        ctx.fillText('C–O₂ Bond Order:  ' + bond2Order.toFixed(2), w - 245, 141);
        ctx.fillText('Deloc. Energy:   -128.5 kJ/mol', w - 245, 164);
      }

      // HUD overlay
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.fillRect(15, 15, 260, 100);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(15, 15, 260, 100);

      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 13px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Hybridization & Geometry Engine', 25, 38);
      ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
      var geomText = {
        sp3: 'Tetrahedral (109.47°), 4 σ bonds, 25% s / 75% p',
        sp2: 'Trigonal Planar (120°), 3 σ + 1 π, 33% s / 67% p',
        sp: 'Linear (180°), 2 σ + 2 π, 50% s / 50% p',
        resonance: 'Conjugated π System, Partial Double Bond Order'
      }[state.mode];
      ctx.fillText(geomText, 25, 58);
      ctx.fillStyle = '#64748b'; ctx.font = '10px monospace';
      ctx.fillText('• Drag mouse/touch to rotate 3D view', 25, 78);
      ctx.fillText('• Coulson: 1 + λ₁λ₂cos θ = 0', 25, 95);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 2. sim_chem_cycloalkane_conformational_strain (Unit 2)
  // Cyclohexane Chair-Flip, Newman Projection & A-Value Strain Engine
  // =========================================================================
  window.Org1Sims.sim_chem_cycloalkane_conformational_strain = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      substituent: 'tBu', // H, Me, tBu, OH, Br
      isFlipped: false,
      animProgress: 0, // 0 = chair 1, 1 = chair 2
      tempK: 298.15
    };

    var aValues = {
      H: { name: 'Hydrogen (-H)', aVal: 0.0, clash: 'Negligible' },
      Me: { name: 'Methyl (-CH₃)', aVal: 7.3, clash: 'Moderate 1,3-Diaxial' },
      tBu: { name: 'tert-Butyl (-C(CH₃)₃)', aVal: 20.5, clash: 'Severe Conformational Lock' },
      OH: { name: 'Hydroxyl (-OH)', aVal: 3.9, clash: 'Mild 1,3-Diaxial' },
      Br: { name: 'Bromo (-Br)', aVal: 1.6, clash: 'Small 1,3-Diaxial' }
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">C1 Substituent:</label>
        <select id="${controlsId}-sub" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="tBu">tert-Butyl (-C(CH₃)₃) [A = 20.5 kJ/mol]</option>
          <option value="Me">Methyl (-CH₃) [A = 7.3 kJ/mol]</option>
          <option value="OH">Hydroxyl (-OH) [A = 3.9 kJ/mol]</option>
          <option value="Br">Bromo (-Br) [A = 1.6 kJ/mol]</option>
          <option value="H">Hydrogen (-H) [A = 0.0 kJ/mol]</option>
        </select>
        <button id="${controlsId}-flip" style="background:#10b981; color:#fff; border:none; padding:4px 12px; border-radius:4px; font-size:0.85rem; cursor:pointer; font-weight:600;">Chair Flip Interconversion</button>
      `;

      var subSelect = document.getElementById(controlsId + '-sub');
      var flipBtn = document.getElementById(controlsId + '-flip');

      subSelect.addEventListener('change', function(e) {
        state.substituent = e.target.value;
      });

      flipBtn.addEventListener('click', function() {
        state.isFlipped = !state.isFlipped;
      });
    }

    function render() {
      setup = setupCanvas(canvas);
      ctx = setup.ctx;
      var w = setup.width;
      var h = setup.height;

      // Smooth animation progress
      var targetProg = state.isFlipped ? 1.0 : 0.0;
      state.animProgress += (targetProg - state.animProgress) * 0.08;

      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      // Section Dividers
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(w * 0.58, 0); ctx.lineTo(w * 0.58, h); ctx.stroke();

      // LEFT: 3D Chair Visualization
      var cx = w * 0.28;
      var cy = h * 0.52;
      var s = 70; // scale
      var t = state.animProgress; // 0 to 1

      // Interpolate 6 vertices between Chair A and Chair B (through Twist-Boat)
      // Chair A vertices
      var vA = [
        { x: -s*1.2, y:  s*0.2 }, // C1 (bottom left)
        { x: -s*0.5, y: -s*0.6 }, // C2 (top left)
        { x:  s*0.6, y: -s*0.6 }, // C3 (top right)
        { x:  s*1.2, y: -s*0.2 }, // C4 (top far right)
        { x:  s*0.5, y:  s*0.6 }, // C5 (bottom right)
        { x: -s*0.6, y:  s*0.6 }  // C6 (bottom mid)
      ];

      // Chair B vertices (inverted tilt)
      var vB = [
        { x: -s*1.2, y: -s*0.2 }, // C1 (up)
        { x: -s*0.5, y:  s*0.6 }, // C2 (down)
        { x:  s*0.6, y:  s*0.6 }, // C3 (down)
        { x:  s*1.2, y:  s*0.2 }, // C4 (down)
        { x:  s*0.5, y: -s*0.6 }, // C5 (up)
        { x: -s*0.6, y: -s*0.6 }  // C6 (up)
      ];

      var verts = [];
      for (var i = 0; i < 6; i++) {
        var vx = cx + vA[i].x * (1 - t) + vB[i].x * t;
        var vy = cy + vA[i].y * (1 - t) + vB[i].y * t;
        verts.push({ x: vx, y: vy });
      }

      // Draw Carbon-Carbon ring bonds
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 5;
      ctx.lineJoin = 'round';
      ctx.beginPath();
      ctx.moveTo(verts[0].x, verts[0].y);
      for (var j = 1; j < 6; j++) {
        ctx.lineTo(verts[j].x, verts[j].y);
      }
      ctx.closePath();
      ctx.stroke();

      // Carbon nodes
      verts.forEach(function(v, idx) {
        ctx.beginPath(); ctx.arc(v.x, v.y, 9, 0, Math.PI * 2);
        ctx.fillStyle = '#0f172a'; ctx.fill();
        ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5; ctx.stroke();
        ctx.fillStyle = '#94a3b8'; ctx.font = '10px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('C' + (idx + 1), v.x, v.y);
      });

      // Substituent at C1:
      // In Chair A: Equatorial (slanted down-left)
      // In Chair B: Axial (pointing straight up)
      var subA_eq = { x: verts[0].x - 45, y: verts[0].y + 25 };
      var subB_ax = { x: verts[0].x, y: verts[0].y - 55 };
      var subPos = {
        x: subA_eq.x * (1 - t) + subB_ax.x * t,
        y: subA_eq.y * (1 - t) + subB_ax.y * t
      };

      // Bond to substituent
      ctx.strokeStyle = (t > 0.5) ? '#f43f5e' : '#10b981';
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(verts[0].x, verts[0].y); ctx.lineTo(subPos.x, subPos.y); ctx.stroke();

      // Substituent node
      var info = aValues[state.substituent];
      ctx.beginPath(); ctx.arc(subPos.x, subPos.y, 16, 0, Math.PI * 2);
      ctx.fillStyle = (t > 0.5) ? '#e11d48' : '#059669'; ctx.fill();
      ctx.strokeStyle = '#f8fafc'; ctx.lineWidth = 2; ctx.stroke();
      ctx.fillStyle = '#fff'; ctx.font = 'bold 11px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(state.substituent, subPos.x, subPos.y);

      // Highlight 1,3-diaxial clashes when in axial conformation (t > 0.5)
      if (t > 0.4 && state.substituent !== 'H') {
        var c3 = verts[2], c5 = verts[4];
        var ax3 = { x: c3.x, y: c3.y - 45 };
        var ax5 = { x: c5.x, y: c5.y - 45 };

        ctx.save();
        ctx.setLineDash([4, 4]);
        ctx.strokeStyle = '#f43f5e';
        ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(subPos.x, subPos.y); ctx.lineTo(ax3.x, ax3.y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(subPos.x, subPos.y); ctx.lineTo(ax5.x, ax5.y); ctx.stroke();
        ctx.restore();

        // 1,3-diaxial clash label
        ctx.fillStyle = '#f43f5e'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'center';
        ctx.fillText('⚠️ 1,3-Diaxial Steric Clash', cx, cy - 100);
      }

      // Title & Conf state
      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Cyclohexane Chair Conformation', 25, 35);
      ctx.fillStyle = (t > 0.5) ? '#f43f5e' : '#10b981'; ctx.font = 'bold 12px monospace';
      ctx.fillText(t > 0.5 ? 'AXIAL CONFORMATION (Higher Energy)' : 'EQUATORIAL CONFORMATION (Global Minimum)', 25, 55);

      // RIGHT: Thermodynamics & Energy Profile
      var rx = w * 0.62;
      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Thermodynamic & Conformational Equilibrium', rx, 35);

      var deltaG = info.aVal; // kJ/mol
      var R = 8.314e-3; // kJ/(mol K)
      var K_eq = Math.exp(deltaG / (R * state.tempK)); // [Eq] / [Ax]
      var pctEq = (K_eq / (1 + K_eq)) * 100;
      var pctAx = 100 - pctEq;

      ctx.fillStyle = '#cbd5e1'; ctx.font = '12px monospace';
      ctx.fillText('Substituent:         ' + info.name, rx, 70);
      ctx.fillText('A-Value (-ΔG°):      ' + deltaG.toFixed(1) + ' kJ/mol', rx, 95);
      ctx.fillText('Equilibrium Const K: ' + (deltaG === 0 ? '1.0' : K_eq.toFixed(1)), rx, 120);
      ctx.fillText('Steric Severity:     ' + info.clash, rx, 145);

      // Population Bar Chart
      var barY = 180;
      ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
      ctx.fillText('Conformational Population at 298 K:', rx, barY);

      var barW = w * 0.32;
      var barH = 24;
      var eqW = (pctEq / 100) * barW;
      var axW = barW - eqW;

      ctx.fillStyle = '#10b981'; ctx.fillRect(rx, barY + 10, eqW, barH);
      ctx.fillStyle = '#e11d48'; ctx.fillRect(rx + eqW, barY + 10, axW, barH);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(rx, barY + 10, barW, barH);

      ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 11px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Equatorial: ' + pctEq.toFixed(1) + '%', rx + 6, barY + 26);
      if (pctAx > 4) {
        ctx.textAlign = 'right';
        ctx.fillText('Axial: ' + pctAx.toFixed(1) + '%', rx + barW - 6, barY + 26);
      }

      // Energy Coordinate Diagram
      var graphY = 240;
      var graphH = 120;
      ctx.fillStyle = 'rgba(15, 23, 42, 0.7)';
      ctx.fillRect(rx, graphY, barW, graphH);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(rx, graphY, barW, graphH);

      // Draw double-well curve with chair-flip barrier (~45 kJ/mol)
      ctx.beginPath();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      for (var px = 0; px <= barW; px++) {
        var normX = px / barW; // 0 to 1
        // double well with hump in middle (half-chair TS)
        var pot = Math.sin(normX * Math.PI) * 75 + normX * (deltaG * 1.5);
        var py = graphY + graphH - 25 - pot;
        if (px === 0) ctx.moveTo(rx + px, py);
        else ctx.lineTo(rx + px, py);
      }
      ctx.stroke();

      // Marker for current progress
      var curX = rx + t * barW;
      var curPot = Math.sin(t * Math.PI) * 75 + t * (deltaG * 1.5);
      var curY = graphY + graphH - 25 - curPot;
      ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2);
      ctx.fillStyle = '#fbbf24'; ctx.fill(); ctx.stroke();

      ctx.fillStyle = '#64748b'; ctx.font = '10px sans-serif'; ctx.textAlign = 'center';
      ctx.fillText('Equatorial Chair', rx + 40, graphY + graphH - 8);
      ctx.fillText('Half-Chair TS', rx + barW * 0.5, graphY + 15);
      ctx.fillText('Axial Chair', rx + barW - 40, graphY + graphH - 8);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 3. sim_chem_alkene_addition_stereochemistry (Unit 3)
  // Stereospecific Anti vs Syn Additions & Regiochemistry Engine
  // =========================================================================
  window.Org1Sims.sim_chem_alkene_addition_stereochemistry = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      reaction: 'halogenation', // halogenation, hydroboration, oxymercuration, hbr_shift
      step: 0, // 0 = reactants, 1 = intermediate, 2 = products
      animT: 0
    };

    var rxnData = {
      halogenation: {
        title: "Electrophilic Halogenation (Anti-Addition via Cyclic Halonium)",
        reagent: "Br₂ in CH₂Cl₂",
        interName: "Cyclic Bromonium Ion (Bromiranium)",
        prodName: "Vicinal Dibromide (Stereospecific Anti Enantiomeric Pair)",
        regio: "N/A (Symmetric Attack)",
        stereo: "Strict Anti-Addition (Walden Inversion at C2)",
        ea: "62 kJ/mol"
      },
      hydroboration: {
        title: "Hydroboration-Oxidation (Concerted Syn & Anti-Markovnikov)",
        reagent: "1. BH₃·THF  2. H₂O₂, NaOH",
        interName: "4-Membered Cyclic Square Transition State",
        prodName: "Primary Alcohol (Anti-Markovnikov, Syn-Hydration)",
        regio: "Anti-Markovnikov (Boron to Less-Substituted C)",
        stereo: "Strict Syn-Addition (Retention during Oxidation)",
        ea: "48 kJ/mol"
      },
      oxymercuration: {
        title: "Oxymercuration-Demercuration (Markovnikov without Rearrangement)",
        reagent: "1. Hg(OAc)₂, H₂O  2. NaBH₄",
        interName: "Mercurinium Ion (Bridge avoids Carbocation Rearrangement)",
        prodName: "Secondary Alcohol (Markovnikov Regioselectivity)",
        regio: "Markovnikov (OH to More-Substituted C)",
        stereo: "Anti-Addition followed by Stereorandom Reduction",
        ea: "55 kJ/mol"
      },
      hbr_shift: {
        title: "Electrophilic Addition of HBr with 1,2-Hydride/Alkyl Shift",
        reagent: "HBr (Cold, Dark, No Peroxides)",
        interName: "2° Carbocation → 1,2-Hydride Shift to 3° Carbocation",
        prodName: "Tertiary Bromoalkane (Major Rearranged Product)",
        regio: "Markovnikov via Thermodynamic 3° C⁺ Intermediate",
        stereo: "Racemic Mixture (Planar Carbocation)",
        ea: "74 kJ/mol"
      }
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Alkene Addition Pathway:</label>
        <select id="${controlsId}-rxn" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="halogenation">Halogenation: Anti Br₂ Addition (Bromonium Ion)</option>
          <option value="hydroboration">Hydroboration-Oxidation: Concerted Syn Addition</option>
          <option value="oxymercuration">Oxymercuration-Demercuration: Markovnikov (No Shift)</option>
          <option value="hbr_shift">Hydrobromination: Markovnikov with 1,2-Shift</option>
        </select>
        <button id="${controlsId}-next" style="background:#3b82f6; color:#fff; border:none; padding:4px 12px; border-radius:4px; font-size:0.85rem; cursor:pointer; font-weight:600;">Advance Mechanism Step</button>
      `;

      var rxnSelect = document.getElementById(controlsId + '-rxn');
      var nextBtn = document.getElementById(controlsId + '-next');

      rxnSelect.addEventListener('change', function(e) {
        state.reaction = e.target.value;
        state.step = 0;
        state.animT = 0;
      });

      nextBtn.addEventListener('click', function() {
        state.step = (state.step + 1) % 3;
        state.animT = 0;
      });
    }

    function render() {
      setup = setupCanvas(canvas);
      ctx = setup.ctx;
      var w = setup.width;
      var h = setup.height;
      state.animT += 0.05;

      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var curRxn = rxnData[state.reaction];

      // Reaction Title & Steps
      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText(curRxn.title, 25, 30);
      ctx.fillStyle = '#94a3b8'; ctx.font = '12px sans-serif';
      ctx.fillText('Reagent: ' + curRxn.reagent, 25, 50);

      // Stepper Bar
      var stepNames = ['1. Reactant Alkene & Electrophile', '2. Reactive Intermediate / Transition State', '3. Regio- & Stereospecific Product'];
      var stepW = (w - 50) / 3;
      for (var s = 0; s < 3; s++) {
        var sx = 25 + s * stepW;
        var isCur = (state.step === s);
        ctx.fillStyle = isCur ? '#3b82f6' : '#1e293b';
        ctx.fillRect(sx, 65, stepW - 10, 26);
        ctx.fillStyle = isCur ? '#fff' : '#64748b';
        ctx.font = isCur ? 'bold 11px sans-serif' : '11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(stepNames[s], sx + (stepW - 10) / 2, 82);
      }

      // Main Mechanism Canvas Area
      var mainY = 110;
      var mainH = h - 210;
      ctx.fillStyle = 'rgba(15, 23, 42, 0.6)';
      ctx.fillRect(25, mainY, w - 50, mainH);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(25, mainY, w - 50, mainH);

      var cx = w * 0.5;
      var cy = mainY + mainH * 0.5;

      // Draw Mechanism graphics depending on step
      if (state.step === 0) {
        // Step 0: C=C Alkene + Reagent approaching
        ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 6;
        ctx.beginPath(); ctx.moveTo(cx - 70, cy - 6); ctx.lineTo(cx + 70, cy - 6); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx - 70, cy + 6); ctx.lineTo(cx + 70, cy + 6); ctx.stroke();

        // Carbon atoms
        ctx.beginPath(); ctx.arc(cx - 70, cy, 18, 0, Math.PI * 2); ctx.fillStyle = '#334155'; ctx.fill(); ctx.stroke();
        ctx.beginPath(); ctx.arc(cx + 70, cy, 18, 0, Math.PI * 2); ctx.fillStyle = '#334155'; ctx.fill(); ctx.stroke();
        ctx.fillStyle = '#fff'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('CH₂', cx - 70, cy); ctx.fillText('CH–R', cx + 70, cy);

        // Approaching Electrophile with pulsating arrow
        var bob = Math.sin(state.animT) * 6;
        ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(cx, cy - 80 + bob); ctx.lineTo(cx, cy - 25 + bob); ctx.stroke();
        // Arrowhead
        ctx.beginPath(); ctx.moveTo(cx - 6, cy - 35 + bob); ctx.lineTo(cx, cy - 25 + bob); ctx.lineTo(cx + 6, cy - 35 + bob); ctx.stroke();

        ctx.fillStyle = '#f43f5e'; ctx.font = 'bold 13px monospace';
        ctx.fillText(curRxn.reagent.split(' ')[0], cx, cy - 95 + bob);

      } else if (state.step === 1) {
        // Step 1: Intermediate
        ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'center';
        ctx.fillText(curRxn.interName, cx, mainY + 25);

        if (state.reaction === 'halogenation') {
          // Cyclic Bromonium 3-membered ring
          ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 4;
          ctx.beginPath(); ctx.moveTo(cx - 50, cy + 20); ctx.lineTo(cx + 50, cy + 20); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(cx - 50, cy + 20); ctx.lineTo(cx, cy - 40); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(cx + 50, cy + 20); ctx.lineTo(cx, cy - 40); ctx.stroke();

          ctx.beginPath(); ctx.arc(cx, cy - 40, 20, 0, Math.PI * 2); ctx.fillStyle = '#b45309'; ctx.fill();
          ctx.fillStyle = '#fff'; ctx.font = 'bold 13px sans-serif'; ctx.fillText('Br⁺', cx, cy - 40);

          // Approaching Br- from opposite face (anti-attack)
          var brX = cx + 80, brY = cy + 60 - Math.sin(state.animT)*4;
          ctx.beginPath(); ctx.arc(brX, brY, 16, 0, Math.PI * 2); ctx.fillStyle = '#e11d48'; ctx.fill();
          ctx.fillStyle = '#fff'; ctx.fillText('Br⁻', brX, brY);

          // Curved arrow from Br- to back face
          ctx.strokeStyle = '#f43f5e'; ctx.setLineDash([3, 3]); ctx.lineWidth = 2;
          ctx.beginPath(); ctx.moveTo(brX - 10, brY); ctx.quadraticCurveTo(cx + 30, cy + 50, cx + 15, cy + 25); ctx.stroke();
          ctx.setLineDash([]);

        } else if (state.reaction === 'hydroboration') {
          // 4-membered cyclic transition state
          ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 3; ctx.setLineDash([5, 4]);
          ctx.strokeRect(cx - 50, cy - 35, 100, 70);
          ctx.setLineDash([]);

          ctx.fillStyle = '#38bdf8'; ctx.fillText('C=C', cx - 50, cy + 25);
          ctx.fillStyle = '#ec4899'; ctx.fillText('H—BH₂', cx + 50, cy - 25);
          ctx.fillStyle = '#a78bfa'; ctx.font = '11px monospace';
          ctx.fillText('Concerted 4-Center Syn-Addition Transition State', cx, cy + 55);

        } else {
          // Carbocation / Mercurinium
          ctx.beginPath(); ctx.arc(cx, cy, 28, 0, Math.PI * 2);
          ctx.fillStyle = '#334155'; ctx.fill(); ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 3; ctx.stroke();
          ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 14px monospace'; ctx.fillText('C⁺ Intermediate', cx, cy);
        }

      } else {
        // Step 2: Final Product
        ctx.fillStyle = '#10b981'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'center';
        ctx.fillText(curRxn.prodName, cx, mainY + 25);

        // Product structure
        ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 4;
        ctx.beginPath(); ctx.moveTo(cx - 80, cy); ctx.lineTo(cx + 80, cy); ctx.stroke();

        // Stereospecific substituents
        ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(cx - 50, cy); ctx.lineTo(cx - 50, cy - 50); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx + 50, cy); ctx.lineTo(cx + 50, cy + 50); ctx.stroke();

        ctx.fillStyle = '#10b981'; ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Group A (Anti)', cx - 50, cy - 65);
        ctx.fillText('Group B (Anti)', cx + 50, cy + 65);
      }

      // Bottom Diagnostic Footer
      var botY = h - 90;
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(25, botY, w - 50, 75);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(25, botY, w - 50, 75);

      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Mechanistic & Stereochemical Diagnostics', 35, botY + 20);
      ctx.fillStyle = '#cbd5e1'; ctx.font = '11px monospace';
      ctx.fillText('Regiochemical Outcome: ' + curRxn.regio, 35, botY + 40);
      ctx.fillText('Stereochemical Course: ' + curRxn.stereo, 35, botY + 58);
      ctx.fillStyle = '#fbbf24';
      ctx.fillText('Activation Barrier Ea: ' + curRxn.ea, w * 0.65, botY + 40);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 4. sim_chem_diels_alder_fmo_cycloaddition (Unit 4)
  // Diels-Alder [4+2] FMO Symmetry, Endo-Rule & Activation Barrier
  // =========================================================================
  window.Org1Sims.sim_chem_diels_alder_fmo_cycloaddition = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      approach: 'endo', // endo, exo
      dienophile: 'maleic', // ethylene, maleic, acrolein
      tempK: 300,
      phase: 0
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Stereochemical Approach:</label>
        <select id="${controlsId}-app" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="endo">Endo Approach (Secondary Orbital Overlap Favored)</option>
          <option value="exo">Exo Approach (Thermodynamic Steric Favored)</option>
        </select>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:10px;">Dienophile:</label>
        <select id="${controlsId}-dien" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="maleic">Maleic Anhydride (EWG = Anhydride)</option>
          <option value="acrolein">Acrolein (EWG = -CHO)</option>
          <option value="ethylene">Ethylene (Unactivated, High Ea)</option>
        </select>
      `;

      var appSelect = document.getElementById(controlsId + '-app');
      var dienSelect = document.getElementById(controlsId + '-dien');

      appSelect.addEventListener('change', function(e) { state.approach = e.target.value; });
      dienSelect.addEventListener('change', function(e) { state.dienophile = e.target.value; });
    }

    function render() {
      setup = setupCanvas(canvas);
      ctx = setup.ctx;
      var w = setup.width;
      var h = setup.height;
      state.phase += 0.03;

      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      // LEFT: Frontier Molecular Orbital (FMO) Interaction
      var cx = w * 0.32;
      var cy = h * 0.52;

      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Frontier Molecular Orbital (FMO) Symmetry', 25, 30);
      ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
      ctx.fillText('Diene HOMO (Ψ₂) ↔ Dienophile LUMO (π*) [Suprafacial-Suprafacial]', 25, 50);

      // Draw 1,3-Butadiene in s-cis conformation (top)
      var dY = cy - 70;
      var dieneNodes = [
        { x: cx - 90, y: dY + 30, phase: +1 }, // C1
        { x: cx - 45, y: dY - 20, phase: -1 }, // C2
        { x: cx + 45, y: dY - 20, phase: -1 }, // C3
        { x: cx + 90, y: dY + 30, phase: +1 }  // C4
      ];

      // Draw Diene sigma framework
      ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(dieneNodes[0].x, dieneNodes[0].y);
      for (var k = 1; k < 4; k++) ctx.lineTo(dieneNodes[k].x, dieneNodes[k].y);
      ctx.stroke();

      // Draw Diene HOMO p-orbital lobes
      dieneNodes.forEach(function(n) {
        var topColor = (n.phase > 0) ? '#38bdf8' : '#f43f5e';
        var botColor = (n.phase > 0) ? '#f43f5e' : '#38bdf8';
        // top lobe
        ctx.beginPath(); ctx.ellipse(n.x, n.y - 18, 12, 18, 0, 0, Math.PI * 2);
        ctx.fillStyle = topColor; ctx.fill(); ctx.stroke();
        // bottom lobe
        ctx.beginPath(); ctx.ellipse(n.x, n.y + 18, 12, 18, 0, 0, Math.PI * 2);
        ctx.fillStyle = botColor; ctx.fill(); ctx.stroke();
      });

      // Draw Dienophile (bottom)
      var pY = cy + 70;
      var philNodes = [
        { x: cx - 90, y: pY, phase: +1 }, // C5
        { x: cx + 90, y: pY, phase: -1 }  // C6
      ];

      // Dienophile sigma bond
      ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(philNodes[0].x, philNodes[0].y); ctx.lineTo(philNodes[1].x, philNodes[1].y); ctx.stroke();

      // Dienophile LUMO p-orbital lobes
      philNodes.forEach(function(n) {
        var topColor = (n.phase > 0) ? '#38bdf8' : '#f43f5e';
        var botColor = (n.phase > 0) ? '#f43f5e' : '#38bdf8';
        ctx.beginPath(); ctx.ellipse(n.x, n.y - 18, 12, 18, 0, 0, Math.PI * 2);
        ctx.fillStyle = topColor; ctx.fill(); ctx.stroke();
        ctx.beginPath(); ctx.ellipse(n.x, n.y + 18, 12, 18, 0, 0, Math.PI * 2);
        ctx.fillStyle = botColor; ctx.fill(); ctx.stroke();
      });

      // Primary Orbital Overlaps (C1-C5 and C4-C6)
      ctx.save();
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(dieneNodes[0].x, dieneNodes[0].y + 18); ctx.lineTo(philNodes[0].x, philNodes[0].y - 18); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(dieneNodes[3].x, dieneNodes[3].y + 18); ctx.lineTo(philNodes[1].x, philNodes[1].y - 18); ctx.stroke();
      ctx.restore();

      ctx.fillStyle = '#10b981'; ctx.font = 'bold 11px sans-serif'; ctx.textAlign = 'center';
      ctx.fillText('Primary Bonding Overlap', dieneNodes[0].x - 10, cy);
      ctx.fillText('Primary Bonding Overlap', dieneNodes[3].x + 10, cy);

      // Secondary Orbital Interaction (Alder Endo Rule)
      if (state.approach === 'endo' && state.dienophile !== 'ethylene') {
        ctx.save();
        ctx.setLineDash([3, 3]);
        ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(dieneNodes[1].x, dieneNodes[1].y + 18); ctx.lineTo(cx, cy + 30); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(dieneNodes[2].x, dieneNodes[2].y + 18); ctx.lineTo(cx, cy + 30); ctx.stroke();
        ctx.restore();

        ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 11px sans-serif';
        ctx.fillText('★ Secondary Orbital Interaction (EWG)', cx, cy + 20);
      }

      // RIGHT: Energy Profile & Stereochemical Outcomes
      var rx = w * 0.62;
      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Thermodynamic & Kinetic Energy Profiles', rx, 30);

      var eaEndo = (state.dienophile === 'maleic' ? 45 : (state.dienophile === 'acrolein' ? 58 : 115));
      var eaExo = eaEndo + 14; // Endo has lower barrier due to secondary overlap

      ctx.fillStyle = '#cbd5e1'; ctx.font = '12px monospace';
      ctx.fillText('Dienophile:          ' + state.dienophile.toUpperCase(), rx, 65);
      ctx.fillText('Conformation:        s-cis diene mandatory', rx, 85);
      ctx.fillText('Woodward-Hoffmann:   [π4s + π2s] thermally allowed', rx, 105);
      ctx.fillText('Endo Barrier Ea:     ' + eaEndo + ' kJ/mol (Kinetic Favored)', rx, 125);
      ctx.fillText('Exo Barrier Ea:      ' + eaExo + ' kJ/mol (Thermodynamic)', rx, 145);

      // Energy Diagram
      var graphY = 175;
      var graphW = w * 0.33;
      var graphH = 150;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.7)';
      ctx.fillRect(rx, graphY, graphW, graphH);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(rx, graphY, graphW, graphH);

      // Endo Curve (Blue)
      ctx.beginPath(); ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;
      for (var px = 0; px <= graphW; px++) {
        var nx = px / graphW;
        var yCurve = graphY + graphH - 30 - Math.sin(nx * Math.PI) * (graphH * 0.7 * (eaEndo / 115)) - nx * 40;
        if (px === 0) ctx.moveTo(rx + px, yCurve); else ctx.lineTo(rx + px, yCurve);
      }
      ctx.stroke();

      // Exo Curve (Red dashed)
      ctx.save(); ctx.setLineDash([5, 4]); ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var px = 0; px <= graphW; px++) {
        var nx = px / graphW;
        var yCurve = graphY + graphH - 30 - Math.sin(nx * Math.PI) * (graphH * 0.7 * (eaExo / 115)) - nx * 50;
        if (px === 0) ctx.moveTo(rx + px, yCurve); else ctx.lineTo(rx + px, yCurve);
      }
      ctx.stroke();
      ctx.restore();

      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 11px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('— Endo Pathway (Lower TS)', rx + 10, graphY + 25);
      ctx.fillStyle = '#f43f5e';
      ctx.fillText('--- Exo Pathway (More Stable Product)', rx + 10, graphY + 45);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 5. sim_chem_aromatic_eas_director_simulator (Unit 5)
  // Wheland Intermediate Resonance Structures & Hammett Regiochemistry
  // =========================================================================
  window.Org1Sims.sim_chem_aromatic_eas_director_simulator = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      substituent: 'OH', // OH, CH3, Cl, NO2, COCH3
      attackPosition: 'ortho' // ortho, meta, para
    };

    var subInfo = {
      OH: { name: 'Hydroxyl (-OH)', type: 'Strong Activating (+M > -I)', dir: 'Ortho / Para', sigmaP: -0.37, relRate: '1,000× faster' },
      CH3: { name: 'Methyl (-CH₃)', type: 'Weak Activating (Hyperconjugation)', dir: 'Ortho / Para', sigmaP: -0.17, relRate: '25× faster' },
      Cl: { name: 'Chloro (-Cl)', type: 'Weak Deactivating (-I > +M)', dir: 'Ortho / Para (Halogen Anomaly)', sigmaP: +0.23, relRate: '0.03× slower' },
      NO2: { name: 'Nitro (-NO₂)', type: 'Strong Deactivating (-M, -I)', dir: 'Meta Directing', sigmaP: +0.78, relRate: '10⁻⁶× slower' },
      COCH3: { name: 'Acetyl (-COCH₃)', type: 'Moderate Deactivating (-M)', dir: 'Meta Directing', sigmaP: +0.50, relRate: '10⁻³× slower' }
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Ring Substituent:</label>
        <select id="${controlsId}-sub" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="OH">-OH (Strong Activating, o/p)</option>
          <option value="CH3">-CH₃ (Weak Activating, o/p)</option>
          <option value="Cl">-Cl (Halogen Anomaly: Deactivating, o/p)</option>
          <option value="NO2">-NO₂ (Strong Deactivating, meta)</option>
          <option value="COCH3">-COCH₃ (Moderate Deactivating, meta)</option>
        </select>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:10px;">Attack Position:</label>
        <select id="${controlsId}-pos" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="ortho">Ortho Attack (Adjacent to Substituent)</option>
          <option value="para">Para Attack (Opposite to Substituent)</option>
          <option value="meta">Meta Attack (1,3-Relationship)</option>
        </select>
      `;

      var subSelect = document.getElementById(controlsId + '-sub');
      var posSelect = document.getElementById(controlsId + '-pos');

      subSelect.addEventListener('change', function(e) { state.substituent = e.target.value; });
      posSelect.addEventListener('change', function(e) { state.attackPosition = e.target.value; });
    }

    function render() {
      setup = setupCanvas(canvas);
      ctx = setup.ctx;
      var w = setup.width;
      var h = setup.height;

      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var curSub = subInfo[state.substituent];

      // Header
      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Electrophilic Aromatic Substitution (EAS) Wheland Intermediate', 25, 30);
      ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
      ctx.fillText('Substituent: ' + curSub.name + ' | ' + curSub.type + ' | Hammett σ_p = ' + curSub.sigmaP, 25, 50);

      // Draw 3 Canonical Wheland Resonance Contributors
      var cy = h * 0.45;
      var ringSpacing = w * 0.28;
      var startX = w * 0.18;

      var numContrib = (state.substituent === 'OH' && state.attackPosition !== 'meta') ? 4 : 3;

      for (var c = 0; c < numContrib; c++) {
        var rx = startX + c * (ringSpacing * 0.85);

        // Hexagon ring
        ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3.5;
        ctx.beginPath();
        for (var a = 0; a < 6; a++) {
          var ang = a * (Math.PI / 3) - Math.PI / 2;
          var hx = rx + Math.cos(ang) * 42;
          var hy = cy + Math.sin(ang) * 42;
          if (a === 0) ctx.moveTo(hx, hy); else ctx.lineTo(hx, hy);
        }
        ctx.closePath();
        ctx.stroke();

        // Substituent at top (C1)
        ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(rx, cy - 42); ctx.lineTo(rx, cy - 65); ctx.stroke();
        ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 11px sans-serif'; ctx.textAlign = 'center';
        ctx.fillText(state.substituent, rx, cy - 72);

        // Incoming electrophile E+ and H at attack position
        var attAngle = (state.attackPosition === 'ortho') ? (-Math.PI/6) : ((state.attackPosition === 'para') ? (Math.PI/2) : (Math.PI/6));
        var attX = rx + Math.cos(attAngle) * 42;
        var attY = cy + Math.sin(attAngle) * 42;

        ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(attX, attY); ctx.lineTo(attX + 18, attY + 12); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(attX, attY); ctx.lineTo(attX + 18, attY - 12); ctx.stroke();

        ctx.fillStyle = '#10b981'; ctx.font = 'bold 10px monospace';
        ctx.fillText('E', attX + 24, attY - 10);
        ctx.fillText('H', attX + 24, attY + 14);

        // Positive charge localization in Wheland intermediate
        var chgAngles = [Math.PI/6, 5*Math.PI/6, -5*Math.PI/6];
        var chgPos = chgAngles[c % 3];
        var cxP = rx + Math.cos(chgPos) * 26;
        var cyP = cy + Math.sin(chgPos) * 26;

        ctx.beginPath(); ctx.arc(cxP, cyP, 12, 0, Math.PI * 2);
        ctx.fillStyle = '#f43f5e'; ctx.fill();
        ctx.fillStyle = '#fff'; ctx.font = 'bold 12px monospace';
        ctx.fillText('+', cxP, cyP);

        // Label contributor
        ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
        var formLabel = 'Resonance Form ' + (c + 1);
        if (c === 3) formLabel = '★ Extra Stable Octet Form';
        ctx.fillText(formLabel, rx, cy + 62);
      }

      // Bottom Analysis Panel
      var botY = h - 90;
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(20, botY, w - 40, 75);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(20, botY, w - 40, 75);

      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Regiochemical & Energetic Outcome', 30, botY + 20);

      var isFavored = false;
      if (curSub.dir.indexOf('Ortho') !== -1 && (state.attackPosition === 'ortho' || state.attackPosition === 'para')) isFavored = true;
      if (curSub.dir.indexOf('Meta') !== -1 && state.attackPosition === 'meta') isFavored = true;

      ctx.fillStyle = isFavored ? '#10b981' : '#f43f5e'; ctx.font = 'bold 12px monospace';
      ctx.fillText(isFavored ? 'FAVORED ATTACK PATHWAY (Lowest Activation Barrier)' : 'DISFAVORED ATTACK PATHWAY (High Activation Barrier)', 30, botY + 42);

      ctx.fillStyle = '#cbd5e1'; ctx.font = '11px sans-serif';
      ctx.fillText('Relative EAS Rate: ' + curSub.relRate + ' | Natural Regioselectivity: ' + curSub.dir, 30, botY + 62);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 6. sim_chem_sn1_sn2_e1_e2_mechanism_matrix (Unit 6)
  // Nucleophilic Substitution & Elimination Decision Engine & Kinetics
  // =========================================================================
  window.Org1Sims.sim_chem_sn1_sn2_e1_e2_mechanism_matrix = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      substrate: '2deg', // 1deg, 2deg, 3deg, methyl
      nuBase: 'strong_unhindered', // strong_unhindered, strong_bulky, weak_good_nu, weak_poor
      solvent: 'polar_aprotic', // polar_aprotic, polar_protic
      temp: 'warm' // cold, warm
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Substrate:</label>
        <select id="${controlsId}-sub" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="2deg">Secondary (2°) Alkyl Halide</option>
          <option value="1deg">Primary (1°) Alkyl Halide</option>
          <option value="3deg">Tertiary (3°) Alkyl Halide</option>
          <option value="methyl">Methyl Halide (CH₃-X)</option>
        </select>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:8px;">Nucleophile/Base:</label>
        <select id="${controlsId}-nu" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="strong_unhindered">Strong / Non-bulky (OH⁻, OMe⁻)</option>
          <option value="strong_bulky">Strong / Bulky (t-BuO⁻)</option>
          <option value="weak_good_nu">Weak Base / Good Nu (I⁻, N₃⁻, SH⁻)</option>
          <option value="weak_poor">Weak Base / Poor Nu (H₂O, EtOH)</option>
        </select>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:8px;">Solvent:</label>
        <select id="${controlsId}-solv" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="polar_aprotic">Polar Aprotic (Acetone, DMSO, DMF)</option>
          <option value="polar_protic">Polar Protic (H₂O, MeOH, EtOH)</option>
        </select>
      `;

      var subSelect = document.getElementById(controlsId + '-sub');
      var nuSelect = document.getElementById(controlsId + '-nu');
      var solvSelect = document.getElementById(controlsId + '-solv');

      subSelect.addEventListener('change', function(e) { state.substrate = e.target.value; });
      nuSelect.addEventListener('change', function(e) { state.nuBase = e.target.value; });
      solvSelect.addEventListener('change', function(e) { state.solvent = e.target.value; });
    }

    function calculateOutcomes() {
      // Return percentage distribution [% SN2, % SN1, % E2, % E1]
      var sub = state.substrate;
      var nu = state.nuBase;
      var solv = state.solvent;

      if (sub === 'methyl') {
        if (nu === 'weak_poor') return [10, 0, 0, 0];
        return [100, 0, 0, 0];
      }
      if (sub === '1deg') {
        if (nu === 'strong_bulky') return [15, 0, 85, 0];
        if (nu === 'strong_unhindered') return [85, 0, 15, 0];
        if (nu === 'weak_good_nu') return [100, 0, 0, 0];
        return [20, 0, 0, 0]; // very slow
      }
      if (sub === '2deg') {
        if (nu === 'strong_bulky') return [5, 0, 95, 0];
        if (nu === 'strong_unhindered') return [25, 0, 75, 0];
        if (nu === 'weak_good_nu') return solv === 'polar_aprotic' ? [90, 10, 0, 0] : [60, 40, 0, 0];
        // weak_poor:
        return solv === 'polar_protic' ? [0, 80, 0, 20] : [10, 70, 0, 20];
      }
      if (sub === '3deg') {
        if (nu === 'strong_bulky' || nu === 'strong_unhindered') return [0, 0, 100, 0];
        // weak nucleophile / base
        return solv === 'polar_protic' ? [0, 75, 0, 25] : [0, 70, 0, 30];
      }
      return [50, 0, 50, 0];
    }

    function render() {
      setup = setupCanvas(canvas);
      ctx = setup.ctx;
      var w = setup.width;
      var h = setup.height;

      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var dist = calculateOutcomes(); // [SN2, SN1, E2, E1]

      // Header
      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('SN1 / SN2 / E1 / E2 Mechanistic Decision Matrix & Competition', 25, 30);
      ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
      ctx.fillText('Dynamic Kinetic & Thermodynamic Branching Calculator', 25, 50);

      // LEFT: Pathway Distribution Bar Chart
      var chartX = 35;
      var chartY = 80;
      var chartW = w * 0.45;
      var chartH = 220;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.7)';
      ctx.fillRect(chartX, chartY, chartW, chartH);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(chartX, chartY, chartW, chartH);

      var pathways = [
        { name: 'SN2 (Substitution Bimolecular)', pct: dist[0], col: '#3b82f6', note: 'Walden Inversion, Bimolecular Rate = k[R-X][Nu]' },
        { name: 'SN1 (Substitution Unimolecular)', pct: dist[1], col: '#10b981', note: 'Carbocation, Racemization, Rate = k[R-X]' },
        { name: 'E2 (Elimination Bimolecular)', pct: dist[2], col: '#f59e0b', note: 'Anti-periplanar, Zaitsev/Hofmann Alkene' },
        { name: 'E1 (Elimination Unimolecular)', pct: dist[3], col: '#f43f5e', note: 'Carbocation De-protonation, Most Stable Alkene' }
      ];

      pathways.forEach(function(p, idx) {
        var py = chartY + 25 + idx * 48;
        ctx.fillStyle = '#cbd5e1'; ctx.font = 'bold 11px sans-serif'; ctx.textAlign = 'left';
        ctx.fillText(p.name, chartX + 15, py);

        // Progress bar
        var barMaxW = chartW - 140;
        var barW = (p.pct / 100) * barMaxW;
        ctx.fillStyle = '#1e293b'; ctx.fillRect(chartX + 15, py + 8, barMaxW, 16);
        ctx.fillStyle = p.col; ctx.fillRect(chartX + 15, py + 8, barW, 16);

        ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 11px monospace'; ctx.textAlign = 'right';
        ctx.fillText(p.pct + '%', chartX + chartW - 20, py + 21);
      });

      // RIGHT: Mechanistic Diagnostics & Rate Law
      var rx = w * 0.54;
      var ry = 80;
      var rw = w * 0.42;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.7)';
      ctx.fillRect(rx, ry, rw, chartH);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(rx, ry, rw, chartH);

      // Dominant pathway
      var maxPct = -1, dominant = pathways[0];
      pathways.forEach(function(p) {
        if (p.pct > maxPct) { maxPct = p.pct; dominant = p; }
      });

      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 13px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Dominant Mechanistic Outcome:', rx + 15, ry + 30);
      ctx.fillStyle = dominant.col; ctx.font = 'bold 15px monospace';
      ctx.fillText(dominant.name.split(' ')[0] + ' (' + dominant.pct + '%)', rx + 15, ry + 60);

      ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
      ctx.fillText('Stereochemistry:', rx + 15, ry + 90);
      ctx.fillStyle = '#f8fafc'; ctx.font = '11px monospace';
      var stereoNote = (dominant.name.indexOf('SN2') !== -1) ? '100% Inversion (Walden Backside Attack)' : ((dominant.name.indexOf('SN1') !== -1) ? 'Racemization with Partial Inversion' : 'Anti-Coplanar Elimination (Stereospecific E/Z)');
      ctx.fillText(stereoNote, rx + 15, ry + 108);

      ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
      ctx.fillText('Rate Law Kinetic Formalism:', rx + 15, ry + 135);
      ctx.fillStyle = '#fbbf24'; ctx.font = '12px monospace';
      var rateLaw = (dominant.name.indexOf('2') !== -1) ? 'Rate = k [R–X] [Nu/Base]' : 'Rate = k [R–X]';
      ctx.fillText(rateLaw, rx + 15, ry + 155);

      ctx.fillStyle = '#64748b'; ctx.font = '10px monospace';
      ctx.fillText('Solvent Influence: ' + (state.solvent === 'polar_aprotic' ? 'Favors SN2 (Unsolvated naked Nu⁻)' : 'Favors SN1/E1 (Ionizes leaving group)'), rx + 15, ry + 185);

      // Bottom footer banner
      var botY = h - 85;
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(20, botY, w - 40, 70);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(20, botY, w - 40, 70);

      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Grignard Organometallic Synthesis Note', 30, botY + 22);
      ctx.fillStyle = '#cbd5e1'; ctx.font = '11px sans-serif';
      ctx.fillText('Primary, secondary, and aryl halides react with Mg⁰ in dry Et₂O to generate Grignard RMgX (Schlenk equilibrium).', 30, botY + 42);
      ctx.fillText('Acts as powerful carbanion nucleophile (pKa of alkane conjugate base ~50), reacting with aldehydes to yield 2° alcohols and ketones to 3° alcohols.', 30, botY + 58);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 7. sim_chem_epoxide_ring_opening_pinacol (Unit 7)
  // Epoxide Regiochemistry & Pinacol-Pinacolone Rearrangement Coordinate
  // =========================================================================
  window.Org1Sims.sim_chem_epoxide_ring_opening_pinacol = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      mode: 'epoxide_basic', // epoxide_basic, epoxide_acidic, pinacol
      migratoryGroup: 'anisyl' // anisyl, tolyl, phenyl, methyl, H
    };

    var migratoryApt = {
      anisyl: { name: 'p-Anisyl (p-MeO-C₆H₄-)', relRate: '500×', reason: 'Strong +M resonance stabilizes carbocation' },
      tolyl: { name: 'p-Tolyl (p-Me-C₆H₄-)', relRate: '15×', reason: 'Inductive / hyperconjugative donor' },
      phenyl: { name: 'Phenyl (C₆H₅-)', relRate: '1.0× (Standard)', reason: 'Aryl standard baseline' },
      methyl: { name: 'Methyl (-CH₃)', relRate: '0.002×', reason: 'Alkyl group lacks resonance assistance' },
      H: { name: 'Hydride (-H)', relRate: '0.1×', reason: 'Fast migration when sterically non-hindered' }
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">System Mode:</label>
        <select id="${controlsId}-mode" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="epoxide_basic">Epoxide Ring-Opening (Basic: SN2 at Less Hindered C)</option>
          <option value="epoxide_acidic">Epoxide Ring-Opening (Acidic: Attack at More Substituted C)</option>
          <option value="pinacol">Pinacol-Pinacolone Rearrangement (Migratory Aptitudes)</option>
        </select>
        <div id="${controlsId}-mig-wrap" style="display:none; align-items:center; gap:8px;">
          <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Migrating Group:</label>
          <select id="${controlsId}-mig" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
            <option value="anisyl">p-Anisyl (Highest Aptitude)</option>
            <option value="tolyl">p-Tolyl</option>
            <option value="phenyl">Phenyl</option>
            <option value="methyl">Methyl</option>
            <option value="H">Hydride</option>
          </select>
        </div>
      `;

      var modeSelect = document.getElementById(controlsId + '-mode');
      var migWrap = document.getElementById(controlsId + '-mig-wrap');
      var migSelect = document.getElementById(controlsId + '-mig');

      modeSelect.addEventListener('change', function(e) {
        state.mode = e.target.value;
        migWrap.style.display = (state.mode === 'pinacol') ? 'flex' : 'none';
      });

      migSelect.addEventListener('change', function(e) {
        state.migratoryGroup = e.target.value;
      });
    }

    function render() {
      setup = setupCanvas(canvas);
      ctx = setup.ctx;
      var w = setup.width;
      var h = setup.height;

      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      if (state.mode.indexOf('epoxide') !== -1) {
        // Epoxide Ring Opening Visualizer
        var isAcid = (state.mode === 'epoxide_acidic');
        ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
        ctx.fillText(isAcid ? 'Acid-Catalyzed Epoxide Ring-Opening (Electronic Control)' : 'Base-Catalyzed Epoxide Ring-Opening (Steric SN2 Control)', 25, 30);
        ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
        ctx.fillText(isAcid ? 'Protonation creates partial carbocation on more-substituted carbon; attack with inversion' : 'Strong nucleophile attacks less-hindered carbon via backside SN2 displacement', 25, 50);

        var cx = w * 0.45;
        var cy = h * 0.48;

        // Draw unsymmetrical epoxide: C1(Me,Me) - O - C2(H,H)
        var c1 = { x: cx - 60, y: cy + 30 }; // 3° carbon
        var c2 = { x: cx + 60, y: cy + 30 }; // 1° carbon
        var ox = { x: cx, y: cy - 40 };      // Oxygen

        // Ring bonds
        ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 4;
        ctx.beginPath(); ctx.moveTo(c1.x, c1.y); ctx.lineTo(c2.x, c2.y); ctx.lineTo(ox.x, ox.y); ctx.closePath(); ctx.stroke();

        // Oxygen atom
        ctx.beginPath(); ctx.arc(ox.x, ox.y, 18, 0, Math.PI * 2); ctx.fillStyle = '#dc2626'; ctx.fill();
        ctx.fillStyle = '#fff'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(isAcid ? 'OH⁺' : 'O', ox.x, ox.y);

        // Carbon 1 (more substituted)
        ctx.beginPath(); ctx.arc(c1.x, c1.y, 16, 0, Math.PI * 2); ctx.fillStyle = '#334155'; ctx.fill();
        ctx.fillStyle = '#fff'; ctx.fillText('C₁', c1.x, c1.y);
        ctx.fillStyle = '#f59e0b'; ctx.font = '10px sans-serif'; ctx.fillText('3° (Me₂)', c1.x, c1.y + 26);

        // Carbon 2 (less substituted)
        ctx.beginPath(); ctx.arc(c2.x, c2.y, 16, 0, Math.PI * 2); ctx.fillStyle = '#334155'; ctx.fill();
        ctx.fillStyle = '#fff'; ctx.fillText('C₂', c2.x, c2.y);
        ctx.fillStyle = '#10b981'; ctx.font = '10px sans-serif'; ctx.fillText('1° (H₂)', c2.x, c2.y + 26);

        // Nucleophilic attack arrow
        var targetC = isAcid ? c1 : c2;
        var arrowColor = isAcid ? '#f59e0b' : '#10b981';
        ctx.strokeStyle = arrowColor; ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(targetC.x + (isAcid ? -70 : 70), targetC.y + 60);
        ctx.quadraticCurveTo(targetC.x + (isAcid ? -30 : 30), targetC.y + 40, targetC.x, targetC.y + 16);
        ctx.stroke();

        ctx.fillStyle = arrowColor; ctx.font = 'bold 12px monospace';
        ctx.fillText('Nu⁻ Attack', targetC.x + (isAcid ? -60 : 60), targetC.y + 80);

        // Telemetry Box
        ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
        ctx.fillRect(w - 260, 80, 240, 160);
        ctx.strokeStyle = '#334155'; ctx.strokeRect(w - 260, 80, 240, 160);

        ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 13px sans-serif'; ctx.textAlign = 'left';
        ctx.fillText('Regiochemical Summary', w - 245, 105);
        ctx.fillStyle = '#cbd5e1'; ctx.font = '11px sans-serif';
        ctx.fillText('Regiochemical Target: ' + (isAcid ? 'C1 (3° Carbon)' : 'C2 (1° Carbon)'), w - 245, 130);
        ctx.fillText('Controlling Factor:   ' + (isAcid ? 'Electronic (C⁺ character)' : 'Steric Accessibility'), w - 245, 150);
        ctx.fillText('Stereochemistry:      Inversion at attacked C', w - 245, 170);
        ctx.fillText('Crown Ether Utility:  Phase-Transfer Catalyst', w - 245, 195);
        ctx.fillText('18-Crown-6 binds K⁺, leaves Nu⁻ bare', w - 245, 215);

      } else {
        // Pinacol-Pinacolone Rearrangement Visualizer
        var mig = migratoryApt[state.migratoryGroup];
        ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
        ctx.fillText('Pinacol-Pinacolone Rearrangement (Vicinal Diol → Ketone)', 25, 30);
        ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
        ctx.fillText('Acid-catalyzed loss of H₂O followed by 1,2-migration to oxocarbenium ion', 25, 50);

        var rx = w * 0.42;
        var ry = h * 0.48;

        // Draw Pinacol core: C1(OH, R) - C2(OH, Me)
        ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 4;
        ctx.beginPath(); ctx.moveTo(rx - 70, ry); ctx.lineTo(rx + 70, ry); ctx.stroke();

        // Carbon nodes
        ctx.beginPath(); ctx.arc(rx - 70, ry, 18, 0, Math.PI * 2); ctx.fillStyle = '#334155'; ctx.fill();
        ctx.beginPath(); ctx.arc(rx + 70, ry, 18, 0, Math.PI * 2); ctx.fillStyle = '#334155'; ctx.fill();
        ctx.fillStyle = '#fff'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('C₁', rx - 70, ry); ctx.fillText('C₂⁺', rx + 70, ry);

        // Migrating group on C1 curving over to C2+
        ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 3; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(rx - 70, ry - 18); ctx.quadraticCurveTo(rx, ry - 60, rx + 70, ry - 18); ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 12px monospace';
        ctx.fillText('1,2-Migration: ' + mig.name.split(' ')[0], rx, ry - 75);

        // Driving force: Oxygen lone pair donation
        ctx.fillStyle = '#10b981'; ctx.fillText('O=C (Resonance Driven Oxocarbenium Ion)', rx - 70, ry + 40);

        // Telemetry Box
        ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
        ctx.fillRect(w - 280, 80, 260, 160);
        ctx.strokeStyle = '#334155'; ctx.strokeRect(w - 280, 80, 260, 160);

        ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 13px sans-serif'; ctx.textAlign = 'left';
        ctx.fillText('Migratory Aptitude Metrics', w - 265, 105);
        ctx.fillStyle = '#cbd5e1'; ctx.font = '11px sans-serif';
        ctx.fillText('Group:         ' + mig.name, w - 265, 130);
        ctx.fillText('Relative Rate: ' + mig.relRate, w - 265, 150);
        ctx.fillText('Rationale:     ' + mig.reason, w - 265, 175);
        ctx.fillText('Aptitude Hierarchy:', w - 265, 205);
        ctx.fillText('p-Anisyl > p-Tolyl > Ph > H > Alkyl', w - 265, 225);
      }

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // 8. sim_chem_heterocycle_aromaticity_eas (Unit 8)
  // Heteroaromatic Ring Electron Density & EAS Regioselectivity Analyzer
  // =========================================================================
  window.Org1Sims.sim_chem_heterocycle_aromaticity_eas = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      ring: 'pyrrole', // pyrrole, furan, thiophene, pyridine
      attackPos: 'C2' // C2, C3, C4
    };

    var ringData = {
      pyrrole: {
        name: 'Pyrrole (5-Membered, π-Excessive)',
        hetero: 'N–H',
        aromIndex: 0.78,
        pKaConj: -3.8, // extremely weak base!
        easFavored: 'C2 Position (3 Wheland resonance forms vs 2 for C3)',
        resEnerg: '88 kJ/mol'
      },
      furan: {
        name: 'Furan (5-Membered, π-Excessive, Low Aromaticity)',
        hetero: 'O',
        aromIndex: 0.43,
        pKaConj: -10.0,
        easFavored: 'C2 Position (High diene character, susceptible to addition)',
        resEnerg: '67 kJ/mol'
      },
      thiophene: {
        name: 'Thiophene (5-Membered, Most Aromatic)',
        hetero: 'S',
        aromIndex: 0.86,
        pKaConj: -13.0,
        easFavored: 'C2 Position (Sulfur 3p-2p d-orbital contribution)',
        resEnerg: '121 kJ/mol'
      },
      pyridine: {
        name: 'Pyridine (6-Membered, π-Deficient)',
        hetero: 'N (sp² lone pair)',
        aromIndex: 0.98,
        pKaConj: +5.25, // moderately basic!
        easFavored: 'C3 Position (Avoids unstable positive sextet on electronegative N)',
        resEnerg: '134 kJ/mol'
      }
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Heterocycle:</label>
        <select id="${controlsId}-ring" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="pyrrole">Pyrrole (π-Excessive, C2 attack)</option>
          <option value="furan">Furan (π-Excessive, Diene character)</option>
          <option value="thiophene">Thiophene (Highest Aromaticity in 5-rings)</option>
          <option value="pyridine">Pyridine (π-Deficient, C3 EAS / C2 Chichibabin)</option>
        </select>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:8px;">Attack Site:</label>
        <select id="${controlsId}-pos" style="background:#1e293b; color:#e2e8f0; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="C2">C2 Position (Adjacent to Heteroatom)</option>
          <option value="C3">C3 Position (β-Position)</option>
          <option value="C4">C4 Position (Pyridine γ-Position)</option>
        </select>
      `;

      var ringSelect = document.getElementById(controlsId + '-ring');
      var posSelect = document.getElementById(controlsId + '-pos');

      ringSelect.addEventListener('change', function(e) { state.ring = e.target.value; });
      posSelect.addEventListener('change', function(e) { state.attackPos = e.target.value; });
    }

    function render() {
      setup = setupCanvas(canvas);
      ctx = setup.ctx;
      var w = setup.width;
      var h = setup.height;

      ctx.fillStyle = '#080d19';
      ctx.fillRect(0, 0, w, h);

      var curRing = ringData[state.ring];
      var isSix = (state.ring === 'pyridine');

      // Title
      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText(curRing.name, 25, 30);
      ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
      ctx.fillText('Aromatic Stabilization & EAS Regiochemical Stability Profile', 25, 50);

      // LEFT: Ring Structure & Electrostatic Potential Map
      var cx = w * 0.32;
      var cy = h * 0.52;
      var r = 60;

      var numVerts = isSix ? 6 : 5;
      var verts = [];

      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 4;
      ctx.beginPath();
      for (var i = 0; i < numVerts; i++) {
        var ang = i * (Math.PI * 2 / numVerts) - Math.PI / 2;
        var vx = cx + Math.cos(ang) * r;
        var vy = cy + Math.sin(ang) * r;
        verts.push({ x: vx, y: vy });
        if (i === 0) ctx.moveTo(vx, vy); else ctx.lineTo(vx, vy);
      }
      ctx.closePath();
      ctx.stroke();

      // Electron Cloud Overlay (glow)
      var cloudGrad = ctx.createRadialGradient(cx, cy, 10, cx, cy, r + 15);
      cloudGrad.addColorStop(0, isSix ? 'rgba(59, 130, 246, 0.25)' : 'rgba(236, 72, 153, 0.25)');
      cloudGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = cloudGrad;
      ctx.beginPath(); ctx.arc(cx, cy, r + 20, 0, Math.PI * 2); ctx.fill();

      // Draw Heteroatom at Top (C1 or N1)
      ctx.beginPath(); ctx.arc(verts[0].x, verts[0].y, 20, 0, Math.PI * 2);
      ctx.fillStyle = (state.ring === 'pyridine' || state.ring === 'pyrrole') ? '#2563eb' : (state.ring === 'furan' ? '#dc2626' : '#d97706');
      ctx.fill(); ctx.strokeStyle = '#f8fafc'; ctx.lineWidth = 2; ctx.stroke();
      ctx.fillStyle = '#fff'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(curRing.hetero.split(' ')[0], verts[0].x, verts[0].y);

      // Other Carbons
      for (var v = 1; v < numVerts; v++) {
        ctx.beginPath(); ctx.arc(verts[v].x, verts[v].y, 14, 0, Math.PI * 2);
        ctx.fillStyle = '#334155'; ctx.fill(); ctx.strokeStyle = '#64748b'; ctx.lineWidth = 1.5; ctx.stroke();
        ctx.fillStyle = '#cbd5e1'; ctx.font = '10px monospace';
        ctx.fillText('C' + (v + 1), verts[v].x, verts[v].y);
      }

      // Attack Target Highlight
      var targetIdx = (state.attackPos === 'C2') ? 1 : ((state.attackPos === 'C3') ? 2 : (numVerts > 5 ? 3 : 2));
      var tNode = verts[targetIdx];
      ctx.beginPath(); ctx.arc(tNode.x, tNode.y, 18, 0, Math.PI * 2);
      ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3; ctx.stroke();
      ctx.fillStyle = '#10b981'; ctx.font = 'bold 11px sans-serif';
      ctx.fillText('🎯 Attack', tNode.x + 35, tNode.y);

      // RIGHT: Heterocycle Diagnostics & Wheland Stability
      var rx = w * 0.58;
      var ry = 70;
      var rw = w * 0.38;
      var rh = 250;

      ctx.fillStyle = 'rgba(15, 23, 42, 0.8)';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 13px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Electronic & Regiochemical Diagnostics', rx + 15, ry + 25);

      ctx.fillStyle = '#cbd5e1'; ctx.font = '11px monospace';
      ctx.fillText('Aromaticity Index: ' + curRing.aromIndex + ' (Benzene = 1.0)', rx + 15, ry + 55);
      ctx.fillText('Resonance Energy:  ' + curRing.resEnerg, rx + 15, ry + 78);
      ctx.fillText('Basicity pKa:      ' + curRing.pKaConj, rx + 15, ry + 101);

      // Resonance forms comparison
      var formsC2 = isSix ? 2 : 3;
      var formsC3 = isSix ? 3 : 2;
      ctx.fillStyle = '#fbbf24';
      ctx.fillText('C2 Wheland Cation: ' + formsC2 + ' Canonical Forms' + (isSix ? ' (Unfavorable sextet on N⁺)' : ' (Favored)'), rx + 15, ry + 135);
      ctx.fillText('C3 Wheland Cation: ' + formsC3 + ' Canonical Forms' + (isSix ? ' (Favored EAS position)' : ' (Less stable)'), rx + 15, ry + 158);

      ctx.fillStyle = '#94a3b8'; ctx.font = '11px sans-serif';
      ctx.fillText('EAS Regioselectivity:', rx + 15, ry + 190);
      ctx.fillStyle = '#10b981'; ctx.font = 'bold 12px sans-serif';
      ctx.fillText(curRing.easFavored, rx + 15, ry + 212);

      if (isSix) {
        ctx.fillStyle = '#f43f5e'; ctx.font = '10px monospace';
        ctx.fillText('★ Chichibabin Nucleophilic Amination occurs at C2/C4!', rx + 15, ry + 235);
      }

      // Bottom Banner
      var botY = h - 75;
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(20, botY, w - 40, 60);
      ctx.strokeStyle = '#334155'; ctx.strokeRect(20, botY, w - 40, 60);

      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = 'left';
      ctx.fillText('Heterocyclic Electron Density Classification', 30, botY + 20);
      ctx.fillStyle = '#cbd5e1'; ctx.font = '11px sans-serif';
      ctx.fillText(isSix ? 'π-Deficient: Ring nitrogen withdraws electron density inductively and by resonance; undergoes EAS only under forcing conditions (300°C).' : 'π-Excessive: 6 π electrons distributed over 5 atoms (1.2 e⁻/atom); far more reactive than benzene toward electrophiles.', 30, botY + 42);

      requestAnimationFrame(render);
    }

    render();
  };

  // =========================================================================
  // window.SimulationEngine Mount Adapter
  // =========================================================================
  var SIM_TITLES = {
    sim_chem_organic_hybridization_resonance: "3D Hybrid Orbitals, Sigma/Pi Overlap & Resonance Hybrid Mixer",
    sim_chem_cycloalkane_conformational_strain: "Cyclohexane Chair-Flip & A-Value Conformational Strain Engine",
    sim_chem_alkene_addition_stereochemistry: "Alkene Addition Stereospecificity & Reaction Coordinate Simulator",
    sim_chem_diels_alder_fmo_cycloaddition: "Diels-Alder [4+2] FMO Symmetry & Endo-Rule Simulator",
    sim_chem_aromatic_eas_director_simulator: "EAS Wheland Intermediate Resonance & Regiochemistry Engine",
    sim_chem_sn1_sn2_e1_e2_mechanism_matrix: "SN1 / SN2 / E1 / E2 Dynamic Mechanistic Decision Matrix",
    sim_chem_epoxide_ring_opening_pinacol: "Epoxide Ring-Opening Regiochemistry & Pinacol Rearrangement Coordinate",
    sim_chem_heterocycle_aromaticity_eas: "Heteroaromatic Electron Density & EAS Regioselectivity Analyzer"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.Org1Sims || typeof window.Org1Sims[simType] !== 'function') {
      console.warn('Simulation type not found in Org1Sims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Organic Chemistry Interactive Simulation";
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
      window.Org1Sims[simType](canvasId, controlsId);
    }, 50);
  };

})();
