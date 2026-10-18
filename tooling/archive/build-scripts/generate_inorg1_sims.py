# -*- coding: utf-8 -*-
"""
generate_inorg1_sims.py
Generates inorganic-chemistry-1-sims.js containing 8 real-time 60 FPS interactive Canvas
simulations for Inorganic Chemistry I with window.SimulationEngine mount adapter.
Strictly ZERO course numbers or codes.
"""

sims_code = r'''// Inorganic Chemistry I Interactive Simulation Engines (60 FPS Canvas)
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

  window.Inorg1Sims = {};

  // =========================================================================
  // 1. sim_chem_bohr_schrodinger_orbitals (Unit 1)
  // 3D Atomic Orbital Visualizer & Radial Distribution Functions
  // =========================================================================
  window.Inorg1Sims.sim_chem_bohr_schrodinger_orbitals = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      n: 2,
      l: 1, // 0: s, 1: p, 2: d
      m: 0,
      rotX: 0.3,
      rotY: 0.4,
      isDragging: false,
      lastMouseX: 0,
      lastMouseY: 0,
      phase: 0
    };

    var orbitalNames = {
      '1,0,0': '1s Orbital',
      '2,0,0': '2s Orbital',
      '2,1,0': '2pz Orbital',
      '2,1,1': '2px Orbital',
      '2,1,-1': '2py Orbital',
      '3,0,0': '3s Orbital',
      '3,1,0': '3pz Orbital',
      '3,2,0': '3dz² Orbital',
      '3,2,1': '3dxz Orbital',
      '3,2,-1': '3dyz Orbital',
      '3,2,2': '3dx²-y² Orbital',
      '3,2,-2': '3dxy Orbital'
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Orbital Preset:</label>
        <select id="${controlsId}-preset" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="1,0,0">1s (n=1, l=0, m=0)</option>
          <option value="2,0,0">2s (n=2, l=0, m=0)</option>
          <option value="2,1,0" selected>2pz (n=2, l=1, m=0)</option>
          <option value="2,1,1">2px (n=2, l=1, m=1)</option>
          <option value="3,0,0">3s (n=3, l=0, m=0)</option>
          <option value="3,1,0">3pz (n=3, l=1, m=0)</option>
          <option value="3,2,0">3dz² (n=3, l=2, m=0)</option>
          <option value="3,2,2">3dx²-y² (n=3, l=2, m=2)</option>
          <option value="3,2,-2">3dxy (n=3, l=2, m=-2)</option>
        </select>
        <span style="color:#64748b; font-size:0.75rem; margin-left:8px;">(Click & drag to rotate 3D view)</span>
      `;

      var presetSelect = document.getElementById(controlsId + '-preset');
      if (presetSelect) {
        presetSelect.addEventListener('change', function(e) {
          var parts = e.target.value.split(',').map(Number);
          state.n = parts[0];
          state.l = parts[1];
          state.m = parts[2];
        });
      }
    }

    // Mouse drag interaction
    canvas.addEventListener('mousedown', function(e) {
      state.isDragging = true;
      state.lastMouseX = e.clientX;
      state.lastMouseY = e.clientY;
    });
    window.addEventListener('mouseup', function() { state.isDragging = false; });
    canvas.addEventListener('mousemove', function(e) {
      if (!state.isDragging) return;
      var dx = e.clientX - state.lastMouseX;
      var dy = e.clientY - state.lastMouseY;
      state.rotY += dx * 0.01;
      state.rotX += dy * 0.01;
      state.lastMouseX = e.clientX;
      state.lastMouseY = e.clientY;
    });

    function draw() {
      var w = setup.width;
      var h = setup.height;
      ctx.clearRect(0, 0, w, h);

      state.phase += 0.02;

      // 3D Orbital Visualizer Box (Left)
      var cx = w * 0.35;
      var cy = h * 0.52;
      var rBox = Math.min(w * 0.32, h * 0.44);

      ctx.fillStyle = '#050811';
      ctx.fillRect(15, 15, w * 0.65, h - 30);
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      ctx.strokeRect(15, 15, w * 0.65, h - 30);

      // Coordinate axes
      ctx.save();
      ctx.translate(cx, cy);

      function project(x, y, z) {
        // Simple 3D rotation
        var cosY = Math.cos(state.rotY), sinY = Math.sin(state.rotY);
        var cosX = Math.cos(state.rotX), sinX = Math.sin(state.rotX);
        var x1 = x * cosY + z * sinY;
        var z1 = -x * sinY + z * cosY;
        var y1 = y * cosX - z1 * sinX;
        var z2 = y * sinX + z1 * cosX;
        var scale = 180 / (180 + z2 * 0.3);
        return { x: x1 * scale, y: y1 * scale, z: z2 };
      }

      // Draw Axes
      var axes = [
        { x: 120, y: 0, z: 0, label: 'x', color: '#ef4444' },
        { x: 0, y: -120, z: 0, label: 'z', color: '#38bdf8' },
        { x: 0, y: 0, z: 120, label: 'y', color: '#10b981' }
      ];
      axes.forEach(function(axis) {
        var p0 = project(0, 0, 0);
        var p1 = project(axis.x, axis.y, axis.z);
        ctx.strokeStyle = axis.color;
        ctx.setLineDash([2, 4]);
        ctx.beginPath();
        ctx.moveTo(p0.x, p0.y);
        ctx.lineTo(p1.x, p1.y);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = axis.color;
        ctx.font = '10px monospace';
        ctx.fillText(axis.label, p1.x + 4, p1.y + 4);
      });

      // Render Orbital Cloud / Boundary Surfaces
      var key = state.n + ',' + state.l + ',' + state.m;
      var orbName = orbitalNames[key] || 'Orbital';

      var numPts = 320;
      var points = [];
      for (var i = 0; i < numPts; i++) {
        var theta = (i / numPts) * Math.PI;
        for (var j = 0; j < 12; j++) {
          var phi = (j / 12) * 2 * Math.PI + (i % 2) * 0.2;
          var R = 0;
          var sign = 1;

          if (state.l === 0) { // s orbital
            R = (state.n === 1) ? 55 : 80;
            sign = 1;
          } else if (state.l === 1) { // p orbital
            if (state.m === 0) { // pz
              R = 90 * Math.abs(Math.cos(theta));
              sign = Math.cos(theta) >= 0 ? 1 : -1;
            } else { // px
              R = 90 * Math.abs(Math.sin(theta) * Math.cos(phi));
              sign = (Math.sin(theta) * Math.cos(phi)) >= 0 ? 1 : -1;
            }
          } else if (state.l === 2) { // d orbital
            if (state.m === 0) { // dz²
              R = 85 * Math.abs(3 * Math.cos(theta) * Math.cos(theta) - 1) / 2;
              sign = (3 * Math.cos(theta) * Math.cos(theta) - 1) >= 0 ? 1 : -1;
            } else { // dx²-y²
              R = 85 * Math.abs(Math.sin(theta) * Math.sin(theta) * Math.cos(2 * phi));
              sign = Math.cos(2 * phi) >= 0 ? 1 : -1;
            }
          }

          var px = R * Math.sin(theta) * Math.cos(phi);
          var py = -R * Math.cos(theta); // z axis up
          var pz = R * Math.sin(theta) * Math.sin(phi);

          var pr = project(px, py, pz);
          points.push({ x: pr.x, y: pr.y, z: pr.z, sign: sign });
        }
      }

      // Sort points by depth
      points.sort(function(a, b) { return a.z - b.z; });

      // Draw points
      points.forEach(function(pt) {
        var alpha = Math.max(0.2, Math.min(0.9, (pt.z + 100) / 200));
        ctx.fillStyle = pt.sign > 0 ? `rgba(56, 189, 248, ${alpha})` : `rgba(244, 63, 94, ${alpha})`;
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, 2, 0, 2 * Math.PI);
        ctx.fill();
      });

      // Nucleus
      var pNuc = project(0, 0, 0);
      ctx.fillStyle = '#fbbf24';
      ctx.beginPath();
      ctx.arc(pNuc.x, pNuc.y, 4, 0, 2 * Math.PI);
      ctx.fill();

      ctx.restore();

      // Orbital Title & Legend
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 14px system-ui, sans-serif';
      ctx.fillText(orbName, 30, 42);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(`Quantum Numbers: n=${state.n}, l=${state.l}, ml=${state.m}`, 30, 60);

      // Node Count HUD
      var radialNodes = state.n - state.l - 1;
      var angularNodes = state.l;
      var totalNodes = state.n - 1;
      ctx.fillText(`Radial Nodes: ${radialNodes} | Angular Nodes: ${angularNodes} | Total: ${totalNodes}`, 30, 76);

      // Phase legend
      ctx.fillStyle = '#38bdf8';
      ctx.fillRect(30, h - 38, 10, 10);
      ctx.fillStyle = '#cbd5e1';
      ctx.fillText('Positive Phase (+ψ)', 46, h - 29);

      ctx.fillStyle = '#f43f5e';
      ctx.fillRect(170, h - 38, 10, 10);
      ctx.fillStyle = '#cbd5e1';
      ctx.fillText('Negative Phase (-ψ)', 186, h - 29);

      // Right Panel: Radial Distribution Function 4πr²R²(r)
      var rx = w * 0.70;
      var ry = 15;
      var rw = w * 0.28;
      var rh = h - 30;

      ctx.fillStyle = '#080d1a';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px system-ui, sans-serif';
      ctx.fillText('Radial Distribution: 4πr²R²(r)', rx + 14, ry + 25);

      // Draw plot axes
      var plotX = rx + 25;
      var plotY = ry + rh - 40;
      var plotW = rw - 40;
      var plotH = rh - 85;

      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(plotX, plotY - plotH);
      ctx.lineTo(plotX, plotY);
      ctx.lineTo(plotX + plotW, plotY);
      ctx.stroke();

      ctx.fillStyle = '#64748b';
      ctx.font = '10px monospace';
      ctx.fillText('0', plotX - 8, plotY + 12);
      ctx.fillText('r / a₀ →', plotX + plotW - 40, plotY + 14);
      ctx.fillText('P(r) ↑', plotX - 15, plotY - plotH + 10);

      // Plot curve
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2;
      ctx.beginPath();

      var rMax = 18;
      for (var k = 0; k <= plotW; k++) {
        var r = (k / plotW) * rMax;
        var val = 0;

        if (state.n === 1 && state.l === 0) { // 1s
          val = 4 * r * r * Math.exp(-2 * r);
        } else if (state.n === 2 && state.l === 0) { // 2s
          var term2s = (2 - r);
          val = 0.5 * r * r * term2s * term2s * Math.exp(-r);
        } else if (state.n === 2 && state.l === 1) { // 2p
          val = (1 / 24) * r * r * (r * r) * Math.exp(-r);
        } else if (state.n === 3 && state.l === 0) { // 3s
          var term3s = (27 - 18 * (2 * r / 3) + 2 * (4 * r * r / 9));
          val = 0.04 * r * r * term3s * term3s * Math.exp(-2 * r / 3);
        } else if (state.n === 3 && state.l === 1) { // 3p
          var term3p = (6 - 2 * r / 3) * (2 * r / 3);
          val = 0.05 * r * r * term3p * term3p * Math.exp(-2 * r / 3);
        } else { // 3d
          val = 0.0008 * Math.pow(r, 6) * Math.exp(-2 * r / 3);
        }

        var yPlot = plotY - Math.min(plotH, val * plotH * 1.8);
        if (k === 0) ctx.moveTo(plotX + k, yPlot);
        else ctx.lineTo(plotX + k, yPlot);
      }
      ctx.stroke();

      // Peak r_mp indicator
      var rPeak = (state.n === 1 && state.l === 0) ? 1.0 : (state.n === 2 && state.l === 1 ? 4.0 : (state.n === 2 && state.l === 0 ? 5.2 : 9.0));
      var peakX = plotX + (rPeak / rMax) * plotW;
      ctx.strokeStyle = '#fbbf24';
      ctx.setLineDash([2, 3]);
      ctx.beginPath();
      ctx.moveTo(peakX, plotY);
      ctx.lineTo(peakX, plotY - plotH * 0.7);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#fbbf24';
      ctx.font = '10px monospace';
      ctx.fillText(`r_mp = ${rPeak} a₀`, peakX - 20, plotY - plotH * 0.75);

      requestAnimationFrame(draw);
    }

    draw();
  };

  // =========================================================================
  // 2. sim_chem_periodic_trends_explorer (Unit 2)
  // Interactive Periodic Matrix & Slater Z_eff Calculator
  // =========================================================================
  window.Inorg1Sims.sim_chem_periodic_trends_explorer = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var elements = [
      { sym: 'H', z: 1, p: 1, g: 1, r: 37, ie: 13.6, ea: 0.75, en: 2.20 },
      { sym: 'He', z: 2, p: 1, g: 18, r: 31, ie: 24.59, ea: 0.0, en: 0.0 },
      { sym: 'Li', z: 3, p: 2, g: 1, r: 152, ie: 5.39, ea: 0.62, en: 0.98 },
      { sym: 'Be', z: 4, p: 2, g: 2, r: 112, ie: 9.32, ea: 0.0, en: 1.57 },
      { sym: 'B', z: 5, p: 2, g: 13, r: 85, ie: 8.30, ea: 0.28, en: 2.04 },
      { sym: 'C', z: 6, p: 2, g: 14, r: 77, ie: 11.26, ea: 1.26, en: 2.55 },
      { sym: 'N', z: 7, p: 2, g: 15, r: 75, ie: 14.53, ea: 0.0, en: 3.04 },
      { sym: 'O', z: 8, p: 2, g: 16, r: 73, ie: 13.62, ea: 1.46, en: 3.44 },
      { sym: 'F', z: 9, p: 2, g: 17, r: 71, ie: 17.42, ea: 3.40, en: 3.98 },
      { sym: 'Ne', z: 10, p: 2, g: 18, r: 69, ie: 21.56, ea: 0.0, en: 0.0 },
      { sym: 'Na', z: 11, p: 3, g: 1, r: 186, ie: 5.14, ea: 0.55, en: 0.93 },
      { sym: 'Mg', z: 12, p: 3, g: 2, r: 160, ie: 7.65, ea: 0.0, en: 1.31 },
      { sym: 'Al', z: 13, p: 3, g: 13, r: 143, ie: 5.99, ea: 0.43, en: 1.61 },
      { sym: 'Si', z: 14, p: 3, g: 14, r: 118, ie: 8.15, ea: 1.39, en: 1.90 },
      { sym: 'P', z: 15, p: 3, g: 15, r: 110, ie: 10.49, ea: 0.75, en: 2.19 },
      { sym: 'S', z: 16, p: 3, g: 16, r: 103, ie: 10.36, ea: 2.08, en: 2.58 },
      { sym: 'Cl', z: 17, p: 3, g: 17, r: 99, ie: 12.97, ea: 3.61, en: 3.16 },
      { sym: 'Ar', z: 18, p: 3, g: 18, r: 97, ie: 15.76, ea: 0.0, en: 0.0 }
    ];

    var state = {
      property: 'r', // 'r', 'ie', 'ea', 'en'
      selectedEl: elements[7] // Oxygen
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Periodic Property:</label>
        <button id="${controlsId}-btn-r" class="pchem-btn" style="background:#0284c7; color:#fff; border:none; padding:4px 10px; border-radius:4px; font-size:0.8rem; cursor:pointer;">Atomic Radius (pm)</button>
        <button id="${controlsId}-btn-ie" class="pchem-btn" style="background:#1e293b; color:#cbd5e1; border:1px solid #334155; padding:4px 10px; border-radius:4px; font-size:0.8rem; cursor:pointer;">Ionization Energy (eV)</button>
        <button id="${controlsId}-btn-en" class="pchem-btn" style="background:#1e293b; color:#cbd5e1; border:1px solid #334155; padding:4px 10px; border-radius:4px; font-size:0.8rem; cursor:pointer;">Electronegativity (Pauling)</button>
        <button id="${controlsId}-btn-ea" class="pchem-btn" style="background:#1e293b; color:#cbd5e1; border:1px solid #334155; padding:4px 10px; border-radius:4px; font-size:0.8rem; cursor:pointer;">Electron Affinity (eV)</button>
      `;

      function setActiveBtn(btnId) {
        ['r', 'ie', 'en', 'ea'].forEach(function(k) {
          var b = document.getElementById(`${controlsId}-btn-${k}`);
          if (b) {
            b.style.background = (btnId === k) ? '#0284c7' : '#1e293b';
            b.style.color = (btnId === k) ? '#fff' : '#cbd5e1';
          }
        });
      }

      ['r', 'ie', 'en', 'ea'].forEach(function(k) {
        var b = document.getElementById(`${controlsId}-btn-${k}`);
        if (b) {
          b.addEventListener('click', function() {
            state.property = k;
            setActiveBtn(k);
          });
        }
      });
    }

    // Canvas click to select element
    canvas.addEventListener('click', function(e) {
      var rect = canvas.getBoundingClientRect();
      var mx = e.clientX - rect.left;
      var my = e.clientY - rect.top;

      elements.forEach(function(el) {
        var col = (el.g === 1 ? 0 : (el.g === 2 ? 1 : (el.g >= 13 ? el.g - 11 : 0)));
        var x = 30 + col * 46;
        var y = 60 + (el.p - 1) * 62;
        if (mx >= x && mx <= x + 40 && my >= y && my <= y + 54) {
          state.selectedEl = el;
        }
      });
    });

    function draw() {
      var w = setup.width;
      var h = setup.height;
      ctx.clearRect(0, 0, w, h);

      // Left Panel: Interactive Periodic Grid (Periods 1-3)
      ctx.fillStyle = '#050811';
      ctx.fillRect(15, 15, w * 0.58, h - 30);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(15, 15, w * 0.58, h - 30);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px system-ui, sans-serif';
      var propTitles = { r: 'Atomic Radius (pm)', ie: 'First Ionization Energy (eV)', en: 'Pauling Electronegativity', ea: 'Electron Affinity (eV)' };
      ctx.fillText(`Periodic Table Map (Periods 1-3) • ${propTitles[state.property]}`, 28, 40);

      // Draw Element Tiles
      elements.forEach(function(el) {
        var col = (el.g === 1 ? 0 : (el.g === 2 ? 1 : (el.g >= 13 ? el.g - 11 : 0)));
        var x = 30 + col * 46;
        var y = 60 + (el.p - 1) * 62;
        var isSel = (el.sym === state.selectedEl.sym);

        // Color intensity based on selected property
        var val = el[state.property];
        var norm = (state.property === 'r') ? (val - 30) / 160 : ((state.property === 'ie') ? val / 25 : ((state.property === 'en') ? val / 4 : val / 3.8));
        norm = Math.max(0, Math.min(1, norm));

        var bg = isSel ? '#0284c7' : (state.property === 'r' ? `rgba(16, 185, 129, ${0.15 + norm * 0.7})` : `rgba(56, 189, 248, ${0.15 + norm * 0.7})`);
        ctx.fillStyle = bg;
        ctx.fillRect(x, y, 40, 54);
        ctx.strokeStyle = isSel ? '#38bdf8' : '#334155';
        ctx.lineWidth = isSel ? 2 : 1;
        ctx.strokeRect(x, y, 40, 54);

        ctx.fillStyle = isSel ? '#ffffff' : '#f8fafc';
        ctx.font = 'bold 13px system-ui, sans-serif';
        ctx.fillText(el.sym, x + 6, y + 22);

        ctx.fillStyle = '#94a3b8';
        ctx.font = '9px monospace';
        ctx.fillText(el.z, x + 24, y + 14);

        ctx.fillStyle = isSel ? '#e0f2fe' : '#38bdf8';
        ctx.font = '10px monospace';
        ctx.fillText(val.toFixed(1), x + 5, y + 42);
      });

      // Periodicity Graph (Below Grid in Left Box)
      var pGphX = 30;
      var pGphY = 320;
      var pGphW = w * 0.52;
      var pGphH = 65;

      ctx.fillStyle = '#64748b';
      ctx.font = '10px system-ui, sans-serif';
      ctx.fillText(`Period 2 Trend (Li → Ne)`, pGphX, pGphY - 10);

      var p2 = elements.filter(function(e) { return e.p === 2; });
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.beginPath();
      p2.forEach(function(el, idx) {
        var gx = pGphX + (idx / (p2.length - 1)) * pGphW;
        var val = el[state.property];
        var norm = (state.property === 'r') ? (val - 60) / 100 : (val / 22);
        var gy = pGphY + pGphH - norm * pGphH;
        if (idx === 0) ctx.moveTo(gx, gy);
        else ctx.lineTo(gx, gy);

        ctx.fillStyle = (el.sym === state.selectedEl.sym) ? '#fbbf24' : '#38bdf8';
        ctx.beginPath();
        ctx.arc(gx, gy, (el.sym === state.selectedEl.sym) ? 5 : 3, 0, 2 * Math.PI);
        ctx.fill();
      });
      ctx.stroke();

      // Right Panel: Slater's Rule Effective Nuclear Charge Z_eff Engine
      var rx = w * 0.63;
      var ry = 15;
      var rw = w * 0.35;
      var rh = h - 30;

      ctx.fillStyle = '#080d1a';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(rx, ry, rw, rh);

      var sel = state.selectedEl;
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 15px system-ui, sans-serif';
      ctx.fillText(`${sel.sym} (Z = ${sel.z}) Detail Analysis`, rx + 16, ry + 30);

      // Compute Slater Rules for Z_eff
      var sigma = 0;
      if (sel.z === 1) sigma = 0;
      else if (sel.z === 2) sigma = 0.30;
      else if (sel.p === 2) {
        var valenceElectrons = sel.z - 2;
        sigma = (valenceElectrons - 1) * 0.35 + 2 * 0.85;
      } else if (sel.p === 3) {
        var valenceElectrons = sel.z - 10;
        sigma = (valenceElectrons - 1) * 0.35 + 8 * 0.85 + 2 * 1.00;
      }
      var zeff = Math.max(1, sel.z - sigma);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '12px system-ui, sans-serif';
      ctx.fillText(`Atomic Number (Z): ${sel.z}`, rx + 16, ry + 65);
      ctx.fillText(`Slater Screening (σ): ${sigma.toFixed(2)}`, rx + 16, ry + 90);

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillText(`Effective Charge (Z_eff): ${zeff.toFixed(2)}`, rx + 16, ry + 118);

      // Property Metrics HUD
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`• Atomic Radius:     ${sel.r} pm`, rx + 16, ry + 155);
      ctx.fillText(`• Ionization Energy: ${sel.ie.toFixed(2)} eV`, rx + 16, ry + 175);
      ctx.fillText(`• Electronegativity: ${sel.en.toFixed(2)}`, rx + 16, ry + 195);
      ctx.fillText(`• Electron Affinity: ${sel.ea.toFixed(2)} eV`, rx + 16, ry + 215);

      // Physical Insight Text
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px system-ui, sans-serif';
      var insight = '';
      if (sel.sym === 'N') insight = 'N has half-filled 2p³ stability → IE is higher than Oxygen (14.5 eV vs 13.6 eV)!';
      else if (sel.sym === 'O') insight = 'Paired 2p⁴ electron experiences inter-electron repulsion → Lower IE than Nitrogen.';
      else if (sel.sym === 'F') insight = 'Highest electronegativity (3.98) due to large Z_eff (5.20) and tiny covalent radius.';
      else if (sel.sym === 'Li') insight = 'Large radius (152 pm) and weak Z_eff (1.30) yield low ionization threshold (5.39 eV).';
      else insight = 'Z_eff increases left-to-right, drawing valence clouds closer and elevating electronegativity.';

      var words = insight.split(' ');
      var line = '';
      var yTxt = ry + 260;
      words.forEach(function(word) {
        var testLine = line + word + ' ';
        if (ctx.measureText(testLine).width > rw - 35) {
          ctx.fillText(line, rx + 16, yTxt);
          line = word + ' ';
          yTxt += 16;
        } else {
          line = testLine;
        }
      });
      ctx.fillText(line, rx + 16, yTxt);

      requestAnimationFrame(draw);
    }

    draw();
  };

  // =========================================================================
  // 3. sim_chem_born_haber_lattice_cycle (Unit 3)
  // Interactive Born-Haber Cycle & Born-Landé Lattice Energy Engine
  // =========================================================================
  window.Inorg1Sims.sim_chem_born_haber_lattice_cycle = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var salts = {
      'NaCl': { name: 'Sodium Chloride (NaCl)', dHsub: 107.3, ie: 495.8, dHdiss: 121.7, ea: -348.6, dHf: -411.2, r0: 282, M: 1.7476, n: 8 },
      'KCl':  { name: 'Potassium Chloride (KCl)', dHsub: 89.2, ie: 418.8, dHdiss: 121.7, ea: -348.6, dHf: -436.7, r0: 315, M: 1.7476, n: 9 },
      'LiF':  { name: 'Lithium Fluoride (LiF)', dHsub: 159.4, ie: 520.2, dHdiss: 79.4, ea: -328.2, dHf: -616.0, r0: 201, M: 1.7476, n: 6 },
      'MgO':  { name: 'Magnesium Oxide (MgO)', dHsub: 147.7, ie: 2188.4, dHdiss: 249.2, ea: 657.0, dHf: -601.7, r0: 210, M: 1.7476, n: 7, z: 2 }
    };

    var state = {
      currentSalt: 'NaCl'
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Crystal Salt:</label>
        <select id="${controlsId}-salt" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="NaCl" selected>Sodium Chloride (NaCl)</option>
          <option value="KCl">Potassium Chloride (KCl)</option>
          <option value="LiF">Lithium Fluoride (LiF)</option>
          <option value="MgO">Magnesium Oxide (MgO - High Charge z=2)</option>
        </select>
      `;

      var saltSelect = document.getElementById(controlsId + '-salt');
      if (saltSelect) {
        saltSelect.addEventListener('change', function(e) {
          state.currentSalt = e.target.value;
        });
      }
    }

    function draw() {
      var w = setup.width;
      var h = setup.height;
      ctx.clearRect(0, 0, w, h);

      var salt = salts[state.currentSalt];
      // Calculate Lattice Energy U_latt via Hess's Law:
      // ΔH_f = ΔH_sub + IE + 1/2 ΔH_diss + EA - U_latt
      // => U_latt = ΔH_sub + IE + 1/2 ΔH_diss + EA - ΔH_f
      var uLattExp = salt.dHsub + salt.ie + salt.dHdiss + salt.ea - salt.dHf;

      // Theoretical Born-Lande: U_calc ~ (1389 * M * z+ * z- / r0) * (1 - 1/n)
      var z = salt.z || 1;
      var uLande = (1389.35 * salt.M * z * z / (salt.r0 * 0.1)) * (1 - 1 / salt.n);

      // Energy Level Diagram (Left 65%)
      ctx.fillStyle = '#050811';
      ctx.fillRect(15, 15, w * 0.62, h - 30);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(15, 15, w * 0.62, h - 30);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillText(`Thermochemical Born-Haber Cycle: ${salt.name}`, 30, 40);

      // Draw Energy Ladder
      var baseY = h - 65;
      var scale = 0.12;
      if (state.currentSalt === 'MgO') scale = 0.045;

      var levels = [
        { name: 'Crystal: MX(s)', e: salt.dHf, color: '#38bdf8' },
        { name: 'Elements: M(s) + ½X₂(g)', e: 0, color: '#94a3b8' },
        { name: 'M(g) + ½X₂(g) [ΔH_sub]', e: salt.dHsub, color: '#fbbf24' },
        { name: 'M⁺(g) + ½X₂(g) [IE]', e: salt.dHsub + salt.ie, color: '#f59e0b' },
        { name: 'M⁺(g) + X(g) [½D]', e: salt.dHsub + salt.ie + salt.dHdiss, color: '#ec4899' },
        { name: 'M⁺(g) + X⁻(g) [EA]', e: salt.dHsub + salt.ie + salt.dHdiss + salt.ea, color: '#10b981' }
      ];

      // Zero line
      var yZero = baseY - (0 - salt.dHf) * scale;
      ctx.strokeStyle = '#334155';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(30, yZero);
      ctx.lineTo(w * 0.60, yZero);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#64748b';
      ctx.font = '10px monospace';
      ctx.fillText('Reference Enthalpy Zero (0 kJ/mol)', w * 0.40, yZero - 4);

      // Draw Energy Steps
      levels.forEach(function(lvl, i) {
        var yLvl = baseY - (lvl.e - salt.dHf) * scale;
        var xLvl = 40 + i * 50;

        ctx.strokeStyle = lvl.color;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(xLvl, yLvl);
        ctx.lineTo(xLvl + 65, yLvl);
        ctx.stroke();

        ctx.fillStyle = lvl.color;
        ctx.font = 'bold 10px monospace';
        ctx.fillText(lvl.e.toFixed(0), xLvl + 70, yLvl + 3);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '9px system-ui, sans-serif';
        ctx.fillText(lvl.name, xLvl, yLvl - 6);
      });

      // Big downward arrow: Lattice Energy U_latt
      var yTop = baseY - (levels[5].e - salt.dHf) * scale;
      var yBottom = baseY;
      var xArrow = w * 0.54;

      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(xArrow, yTop);
      ctx.lineTo(xArrow, yBottom);
      ctx.stroke();

      // Arrowhead
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.moveTo(xArrow, yBottom);
      ctx.lineTo(xArrow - 5, yBottom - 10);
      ctx.lineTo(xArrow + 5, yBottom - 10);
      ctx.fill();

      ctx.font = 'bold 12px monospace';
      ctx.fillText(`-U_latt = -${uLattExp.toFixed(1)} kJ/mol`, xArrow - 140, (yTop + yBottom) / 2);

      // Right Panel: Thermodynamic Data & Born-Lande Verification
      var rx = w * 0.67;
      var ry = 15;
      var rw = w * 0.31;
      var rh = h - 30;

      ctx.fillStyle = '#080d1a';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 14px system-ui, sans-serif';
      ctx.fillText('Thermochemical Accounting', rx + 14, ry + 28);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`• ΔH_sub(M):    +${salt.dHsub.toFixed(1)} kJ`, rx + 14, ry + 60);
      ctx.fillText(`• IE(M):         +${salt.ie.toFixed(1)} kJ`, rx + 14, ry + 80);
      ctx.fillText(`• ½D(X₂):        +${salt.dHdiss.toFixed(1)} kJ`, rx + 14, ry + 100);
      ctx.fillText(`• EA(X):         ${salt.ea.toFixed(1)} kJ`, rx + 14, ry + 120);
      ctx.fillText(`• ΔH°f(MX):      ${salt.dHf.toFixed(1)} kJ`, rx + 14, ry + 140);

      ctx.strokeStyle = '#334155';
      ctx.beginPath();
      ctx.moveTo(rx + 14, ry + 155);
      ctx.lineTo(rx + rw - 14, ry + 155);
      ctx.stroke();

      ctx.fillStyle = '#ef4444';
      ctx.font = 'bold 12px monospace';
      ctx.fillText(`Lattice Energy (Hess):`, rx + 14, ry + 175);
      ctx.fillText(`U_latt = +${uLattExp.toFixed(1)} kJ/mol`, rx + 14, ry + 195);

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 12px monospace';
      ctx.fillText(`Born-Landé Theoretical:`, rx + 14, ry + 230);
      ctx.fillText(`U_calc = +${uLande.toFixed(1)} kJ/mol`, rx + 14, ry + 250);

      var diff = Math.abs(uLattExp - uLande);
      var pct = (diff / uLattExp) * 100;
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px system-ui, sans-serif';
      ctx.fillText(`Madelung M = ${salt.M.toFixed(4)}`, rx + 14, ry + 280);
      ctx.fillText(`Interionic r₀ = ${salt.r0} pm`, rx + 14, ry + 300);
      ctx.fillText(`Born Exponent n = ${salt.n}`, rx + 14, ry + 320);
      ctx.fillText(`Model Concordance: ${(100 - pct).toFixed(1)}% match!`, rx + 14, ry + 345);

      requestAnimationFrame(draw);
    }

    draw();
  };

  // =========================================================================
  // 4. sim_chem_vsepr_molecular_geometry (Unit 4)
  // 3D VSEPR Molecular Geometry Engine & Lone-Pair Bending
  // =========================================================================
  window.Inorg1Sims.sim_chem_vsepr_molecular_geometry = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var molecules = {
      'CO2':   { formula: 'CO₂', sn: 2, bp: 2, lp: 0, geom: 'Linear', angle: 180.0, mu: '0.00 D (Non-polar)', atoms: [{ x: 0, y: 0, z: 0, el: 'C', r: 16, c: '#475569' }, { x: -80, y: 0, z: 0, el: 'O', r: 14, c: '#ef4444' }, { x: 80, y: 0, z: 0, el: 'O', r: 14, c: '#ef4444' }] },
      'BF3':   { formula: 'BF₃', sn: 3, bp: 3, lp: 0, geom: 'Trigonal Planar', angle: 120.0, mu: '0.00 D (Non-polar)', atoms: [{ x: 0, y: 0, z: 0, el: 'B', r: 15, c: '#ec4899' }, { x: 0, y: -75, z: 0, el: 'F', r: 13, c: '#10b981' }, { x: 65, y: 38, z: 0, el: 'F', r: 13, c: '#10b981' }, { x: -65, y: 38, z: 0, el: 'F', r: 13, c: '#10b981' }] },
      'CH4':   { formula: 'CH₄', sn: 4, bp: 4, lp: 0, geom: 'Tetrahedral', angle: 109.5, mu: '0.00 D (Non-polar)', atoms: [{ x: 0, y: 0, z: 0, el: 'C', r: 16, c: '#475569' }, { x: 0, y: -75, z: 0, el: 'H', r: 10, c: '#f8fafc' }, { x: 71, y: 25, z: 0, el: 'H', r: 10, c: '#f8fafc' }, { x: -35, y: 25, z: 61, el: 'H', r: 10, c: '#f8fafc' }, { x: -35, y: 25, z: -61, el: 'H', r: 10, c: '#f8fafc' }] },
      'NH3':   { formula: 'NH₃', sn: 4, bp: 3, lp: 1, geom: 'Trigonal Pyramidal', angle: 107.3, mu: '1.47 D (Polar)', atoms: [{ x: 0, y: -15, z: 0, el: 'N', r: 15, c: '#38bdf8' }, { x: 65, y: 25, z: 0, el: 'H', r: 10, c: '#f8fafc' }, { x: -32, y: 25, z: 56, el: 'H', r: 10, c: '#f8fafc' }, { x: -32, y: 25, z: -56, el: 'H', r: 10, c: '#f8fafc' }], lpCoords: [{ x: 0, y: -60, z: 0 }] },
      'H2O':   { formula: 'H₂O', sn: 4, bp: 2, lp: 2, geom: 'Bent (Angular)', angle: 104.5, mu: '1.85 D (Polar)', atoms: [{ x: 0, y: -10, z: 0, el: 'O', r: 15, c: '#ef4444' }, { x: -55, y: 35, z: 0, el: 'H', r: 10, c: '#f8fafc' }, { x: 55, y: 35, z: 0, el: 'H', r: 10, c: '#f8fafc' }], lpCoords: [{ x: -35, y: -50, z: 30 }, { x: 35, y: -50, z: -30 }] },
      'PCl5':  { formula: 'PCl₅', sn: 5, bp: 5, lp: 0, geom: 'Trigonal Bipyramidal', angle: 120.0, mu: '0.00 D (Non-polar)', atoms: [{ x: 0, y: 0, z: 0, el: 'P', r: 16, c: '#f59e0b' }, { x: 0, y: -80, z: 0, el: 'Cl', r: 14, c: '#10b981' }, { x: 0, y: 80, z: 0, el: 'Cl', r: 14, c: '#10b981' }, { x: 70, y: 0, z: 0, el: 'Cl', r: 14, c: '#10b981' }, { x: -35, y: 0, z: 61, el: 'Cl', r: 14, c: '#10b981' }, { x: -35, y: 0, z: -61, el: 'Cl', r: 14, c: '#10b981' }] },
      'SF6':   { formula: 'SF₆', sn: 6, bp: 6, lp: 0, geom: 'Octahedral', angle: 90.0, mu: '0.00 D (Non-polar)', atoms: [{ x: 0, y: 0, z: 0, el: 'S', r: 16, c: '#eab308' }, { x: 0, y: -75, z: 0, el: 'F', r: 13, c: '#10b981' }, { x: 0, y: 75, z: 0, el: 'F', r: 13, c: '#10b981' }, { x: 75, y: 0, z: 0, el: 'F', r: 13, c: '#10b981' }, { x: -75, y: 0, z: 0, el: 'F', r: 13, c: '#10b981' }, { x: 0, y: 0, z: 75, el: 'F', r: 13, c: '#10b981' }, { x: 0, y: 0, z: -75, el: 'F', r: 13, c: '#10b981' }] }
    };

    var state = {
      molKey: 'H2O',
      rotX: 0.2,
      rotY: 0.3,
      isDragging: false,
      lastX: 0,
      lastY: 0
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Molecule Archetype:</label>
        <select id="${controlsId}-mol" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="H2O" selected>Water (H₂O) - SN=4 (2 BP, 2 LP) Bent</option>
          <option value="NH3">Ammonia (NH₃) - SN=4 (3 BP, 1 LP) Pyramidal</option>
          <option value="CH4">Methane (CH₄) - SN=4 (4 BP, 0 LP) Tetrahedral</option>
          <option value="BF3">Boron Trifluoride (BF₃) - SN=3 Trigonal Planar</option>
          <option value="CO2">Carbon Dioxide (CO₂) - SN=2 Linear</option>
          <option value="PCl5">Phosphorus Pentachloride (PCl₅) - SN=5 TBP</option>
          <option value="SF6">Sulfur Hexafluoride (SF₆) - SN=6 Octahedral</option>
        </select>
        <span style="color:#64748b; font-size:0.75rem; margin-left:8px;">(Drag to rotate 3D geometry)</span>
      `;

      var molSelect = document.getElementById(controlsId + '-mol');
      if (molSelect) {
        molSelect.addEventListener('change', function(e) {
          state.molKey = e.target.value;
        });
      }
    }

    canvas.addEventListener('mousedown', function(e) {
      state.isDragging = true;
      state.lastX = e.clientX;
      state.lastY = e.clientY;
    });
    window.addEventListener('mouseup', function() { state.isDragging = false; });
    canvas.addEventListener('mousemove', function(e) {
      if (!state.isDragging) return;
      var dx = e.clientX - state.lastX;
      var dy = e.clientY - state.lastY;
      state.rotY += dx * 0.01;
      state.rotX += dy * 0.01;
      state.lastX = e.clientX;
      state.lastY = e.clientY;
    });

    function draw() {
      var w = setup.width;
      var h = setup.height;
      ctx.clearRect(0, 0, w, h);

      var mol = molecules[state.molKey];

      // 3D Visualizer Canvas (Left 65%)
      ctx.fillStyle = '#050811';
      ctx.fillRect(15, 15, w * 0.62, h - 30);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(15, 15, w * 0.62, h - 30);

      var cx = w * 0.32;
      var cy = h * 0.52;

      function project(x, y, z) {
        var cosY = Math.cos(state.rotY), sinY = Math.sin(state.rotY);
        var cosX = Math.cos(state.rotX), sinX = Math.sin(state.rotX);
        var x1 = x * cosY + z * sinY;
        var z1 = -x * sinY + z * cosY;
        var y1 = y * cosX - z1 * sinX;
        var z2 = y * sinX + z1 * cosX;
        var scale = 220 / (220 + z2 * 0.35);
        return { x: cx + x1 * scale, y: cy + y1 * scale, z: z2 };
      }

      // Draw Bonds from center atom (atoms[0]) to ligands
      var centerProj = project(mol.atoms[0].x, mol.atoms[0].y, mol.atoms[0].z);
      for (var i = 1; i < mol.atoms.length; i++) {
        var aProj = project(mol.atoms[i].x, mol.atoms[i].y, mol.atoms[i].z);
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(centerProj.x, centerProj.y);
        ctx.lineTo(aProj.x, aProj.y);
        ctx.stroke();
      }

      // Draw Lone Pair Lobes
      if (mol.lpCoords) {
        mol.lpCoords.forEach(function(lp) {
          var lpProj = project(lp.x, lp.y, lp.z);
          ctx.strokeStyle = '#fbbf24';
          ctx.fillStyle = 'rgba(251, 191, 36, 0.25)';
          ctx.lineWidth = 2;
          ctx.setLineDash([2, 3]);
          ctx.beginPath();
          ctx.ellipse((centerProj.x + lpProj.x) / 2, (centerProj.y + lpProj.y) / 2, 22, 12, Math.atan2(lpProj.y - centerProj.y, lpProj.x - centerProj.x), 0, 2 * Math.PI);
          ctx.fill();
          ctx.stroke();
          ctx.setLineDash([]);

          ctx.fillStyle = '#fbbf24';
          ctx.font = '10px monospace';
          ctx.fillText('•• LP', lpProj.x - 10, lpProj.y);
        });
      }

      // Sort atoms by Z for proper rendering
      var renderAtoms = mol.atoms.map(function(a) {
        var p = project(a.x, a.y, a.z);
        return { proj: p, el: a.el, r: a.r, c: a.c, z: p.z };
      });
      renderAtoms.sort(function(a, b) { return a.z - b.z; });

      renderAtoms.forEach(function(atom) {
        ctx.fillStyle = atom.c;
        ctx.beginPath();
        ctx.arc(atom.proj.x, atom.proj.y, atom.r, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#f8fafc';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 11px system-ui, sans-serif';
        ctx.fillText(atom.el, atom.proj.x - 4, atom.proj.y + 4);
      });

      // Title & Molecule Info
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 15px system-ui, sans-serif';
      ctx.fillText(`${mol.formula} Geometry (${mol.geom})`, 30, 42);

      // Right Panel: VSEPR Metrics & Bent's Rule
      var rx = w * 0.67;
      var ry = 15;
      var rw = w * 0.31;
      var rh = h - 30;

      ctx.fillStyle = '#080d1a';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillText('VSEPR Electronic Metrics', rx + 14, ry + 28);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`• Steric Number (SN):  ${mol.sn}`, rx + 14, ry + 60);
      ctx.fillText(`• Bonding Pairs (BP):  ${mol.bp}`, rx + 14, ry + 80);
      ctx.fillText(`• Lone Pairs (LP):     ${mol.lp}`, rx + 14, ry + 100);
      ctx.fillText(`• Observed Angle:      ${mol.angle}°`, rx + 14, ry + 120);

      ctx.strokeStyle = '#334155';
      ctx.beginPath();
      ctx.moveTo(rx + 14, ry + 140);
      ctx.lineTo(rx + rw - 14, ry + 140);
      ctx.stroke();

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 12px monospace';
      ctx.fillText(`Dipole Moment:`, rx + 14, ry + 165);
      ctx.fillText(`${mol.mu}`, rx + 14, ry + 185);

      // Repulsion Hierarchy Note
      ctx.fillStyle = '#fbbf24';
      ctx.font = '11px system-ui, sans-serif';
      ctx.fillText('Repulsion Hierarchy:', rx + 14, ry + 225);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '10px monospace';
      ctx.fillText('LP-LP > LP-BP > BP-BP', rx + 14, ry + 242);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px system-ui, sans-serif';
      var note = '';
      if (mol.lp === 2) note = 'Two bulky lone pairs push bonding pairs together: angle compresses from ideal tetrahedral 109.5° down to 104.5°.';
      else if (mol.lp === 1) note = 'One lone pair repels N-H bonds: angle compresses to 107.3°.';
      else if (mol.sn === 5) note = 'Bent\'s Rule: Electronegative Cl atoms occupy axial positions with higher p-character (longer bonds).';
      else note = 'Highly symmetric distribution: individual bond dipoles cancel out completely (zero net dipole moment).';

      var words = note.split(' ');
      var line = '';
      var yTxt = ry + 275;
      words.forEach(function(word) {
        var testLine = line + word + ' ';
        if (ctx.measureText(testLine).width > rw - 35) {
          ctx.fillText(line, rx + 14, yTxt);
          line = word + ' ';
          yTxt += 16;
        } else {
          line = testLine;
        }
      });
      ctx.fillText(line, rx + 14, yTxt);

      requestAnimationFrame(draw);
    }

    draw();
  };

  // =========================================================================
  // 5. sim_chem_molecular_orbital_lcao (Unit 5)
  // LCAO-MO Diatomic Energy Level Generator & Magnetic Analyzer
  // =========================================================================
  window.Inorg1Sims.sim_chem_molecular_orbital_lcao = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var diatomics = {
      'O2':  { formula: 'O₂ (Diatomic Oxygen)', valenceE: 12, mixing: false, bo: 2.0, mag: 'Paramagnetic (2 unpaired e⁻ in π*2p)', homonuclear: true },
      'N2':  { formula: 'N₂ (Diatomic Nitrogen)', valenceE: 10, mixing: true,  bo: 3.0, mag: 'Diamagnetic (All electrons paired)', homonuclear: true },
      'C2':  { formula: 'C₂ (Dicarbon)', valenceE: 8, mixing: true, bo: 2.0, mag: 'Diamagnetic (π2p fully filled, double bond)', homonuclear: true },
      'B2':  { formula: 'B₂ (Diboron)', valenceE: 6, mixing: true, bo: 1.0, mag: 'Paramagnetic (2 unpaired e⁻ in π2p)', homonuclear: true },
      'NO':  { formula: 'NO (Nitric Oxide)', valenceE: 11, mixing: true, bo: 2.5, mag: 'Paramagnetic (1 unpaired e⁻ in π*2p FMO)', homonuclear: false },
      'CO':  { formula: 'CO (Carbon Monoxide)', valenceE: 10, mixing: true, bo: 3.0, mag: 'Diamagnetic (HOMO is non-bonding σ carbon lone pair)', homonuclear: false }
    };

    var state = {
      molKey: 'O2'
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Diatomic Molecule:</label>
        <select id="${controlsId}-diatomic" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="O2" selected>O₂ (Oxygen) - Classic Paramagnetism</option>
          <option value="N2">N₂ (Nitrogen) - Strong Triple Bond (s-p mixing)</option>
          <option value="C2">C₂ (Dicarbon) - Pure π Double Bond</option>
          <option value="B2">B₂ (Diboron) - Paramagnetic Single Bond</option>
          <option value="NO">NO (Nitric Oxide) - Radical Free Electron</option>
          <option value="CO">CO (Carbon Monoxide) - Triple Bond & C-lone pair</option>
        </select>
      `;

      var diaSelect = document.getElementById(controlsId + '-diatomic');
      if (diaSelect) {
        diaSelect.addEventListener('change', function(e) {
          state.molKey = e.target.value;
        });
      }
    }

    function draw() {
      var w = setup.width;
      var h = setup.height;
      ctx.clearRect(0, 0, w, h);

      var dia = diatomics[state.molKey];

      // Left Panel: MO Energy Level Diagram
      ctx.fillStyle = '#050811';
      ctx.fillRect(15, 15, w * 0.65, h - 30);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(15, 15, w * 0.65, h - 30);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillText(`Molecular Orbital Diagram: ${dia.formula}`, 30, 40);

      var xAO1 = 50;
      var xMO  = w * 0.33;
      var xAO2 = w * 0.53;

      // Labels for AO Columns
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(dia.homonuclear ? 'Atom A (2s, 2p)' : 'Atom A (Less EN)', xAO1 - 10, h - 30);
      ctx.fillText('Molecular Orbitals', xMO - 25, h - 30);
      ctx.fillText(dia.homonuclear ? 'Atom B (2s, 2p)' : 'Atom B (More EN)', xAO2 - 10, h - 30);

      // Define MO levels based on s-p mixing
      // In O2, F2: no mixing -> σ2p lower than π2p
      // In B2, C2, N2: s-p mixing -> π2p lower than σ2p
      var levels = [];
      levels.push({ name: 'σ2s', y: h - 90, cap: 2, type: 'bond' });
      levels.push({ name: 'σ*2s', y: h - 140, cap: 2, type: 'anti' });

      if (dia.mixing) {
        levels.push({ name: 'π2px, π2py', y: h - 210, cap: 4, type: 'bond', degenerate: true });
        levels.push({ name: 'σ2pz', y: h - 255, cap: 2, type: 'bond' });
      } else {
        levels.push({ name: 'σ2pz', y: h - 210, cap: 2, type: 'bond' });
        levels.push({ name: 'π2px, π2py', y: h - 255, cap: 4, type: 'bond', degenerate: true });
      }

      levels.push({ name: 'π*2px, π*2py', y: h - 315, cap: 4, type: 'anti', degenerate: true });
      levels.push({ name: 'σ*2pz', y: h - 365, cap: 2, type: 'anti' });

      // Fill electrons into MOs
      var remE = dia.valenceE;
      levels.forEach(function(lvl) {
        lvl.electrons = Math.min(remE, lvl.cap);
        remE -= lvl.electrons;
      });

      // Draw Atomic Orbitals on sides
      // 2s AOs
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(xAO1, h - 115); ctx.lineTo(xAO1 + 40, h - 115);
      ctx.moveTo(xAO2, h - 115); ctx.lineTo(xAO2 + 40, h - 115);
      // 2p AOs
      ctx.moveTo(xAO1 - 10, h - 235); ctx.lineTo(xAO1 + 50, h - 235);
      ctx.moveTo(xAO2 - 10, h - 235); ctx.lineTo(xAO2 + 50, h - 235);
      ctx.stroke();

      ctx.fillStyle = '#64748b';
      ctx.font = '10px monospace';
      ctx.fillText('2s', xAO1 + 12, h - 120);
      ctx.fillText('2s', xAO2 + 12, h - 120);
      ctx.fillText('2p', xAO1 + 12, h - 240);
      ctx.fillText('2p', xAO2 + 12, h - 240);

      // Draw Molecular Orbitals (Center)
      levels.forEach(function(lvl) {
        var isAnti = lvl.type === 'anti';
        ctx.strokeStyle = isAnti ? '#ef4444' : '#38bdf8';
        ctx.lineWidth = 2.5;

        if (lvl.degenerate) {
          // Double bar for degenerates
          ctx.beginPath();
          ctx.moveTo(xMO - 35, lvl.y); ctx.lineTo(xMO - 5, lvl.y);
          ctx.moveTo(xMO + 5, lvl.y);  ctx.lineTo(xMO + 35, lvl.y);
          ctx.stroke();

          // Connect dash lines to AOs
          ctx.strokeStyle = '#334155';
          ctx.setLineDash([2, 4]);
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(xAO1 + 40, h - 235); ctx.lineTo(xMO - 35, lvl.y);
          ctx.moveTo(xAO2, h - 235);      ctx.lineTo(xMO + 35, lvl.y);
          ctx.stroke();
          ctx.setLineDash([]);
        } else {
          ctx.beginPath();
          ctx.moveTo(xMO - 25, lvl.y); ctx.lineTo(xMO + 25, lvl.y);
          ctx.stroke();

          ctx.strokeStyle = '#334155';
          ctx.setLineDash([2, 4]);
          ctx.lineWidth = 1;
          ctx.beginPath();
          var srcY = (lvl.y > h - 160) ? h - 115 : h - 235;
          ctx.moveTo(xAO1 + 40, srcY); ctx.lineTo(xMO - 25, lvl.y);
          ctx.moveTo(xAO2, srcY);      ctx.lineTo(xMO + 25, lvl.y);
          ctx.stroke();
          ctx.setLineDash([]);
        }

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '10px monospace';
        ctx.fillText(lvl.name, xMO + 42, lvl.y + 4);

        // Draw Electron Spin Arrows
        if (lvl.electrons > 0) {
          ctx.fillStyle = '#fbbf24';
          ctx.font = 'bold 12px monospace';
          if (lvl.degenerate) {
            // Hund's rule filling
            if (lvl.electrons === 1) ctx.fillText('↑', xMO - 22, lvl.y - 4);
            else if (lvl.electrons === 2) { ctx.fillText('↑', xMO - 22, lvl.y - 4); ctx.fillText('↑', xMO + 16, lvl.y - 4); }
            else if (lvl.electrons === 3) { ctx.fillText('↑↓', xMO - 25, lvl.y - 4); ctx.fillText('↑', xMO + 16, lvl.y - 4); }
            else if (lvl.electrons === 4) { ctx.fillText('↑↓', xMO - 25, lvl.y - 4); ctx.fillText('↑↓', xMO + 14, lvl.y - 4); }
          } else {
            if (lvl.electrons === 1) ctx.fillText('↑', xMO - 4, lvl.y - 4);
            else if (lvl.electrons === 2) ctx.fillText('↑↓', xMO - 8, lvl.y - 4);
          }
        }
      });

      // Right Panel: Bond Order & Magnetism Analytics
      var rx = w * 0.70;
      var ry = 15;
      var rw = w * 0.28;
      var rh = h - 30;

      ctx.fillStyle = '#080d1a';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 14px system-ui, sans-serif';
      ctx.fillText('MO Theory Properties', rx + 14, ry + 28);

      var nBond = levels.filter(function(l) { return l.type === 'bond'; }).reduce(function(acc, l) { return acc + l.electrons; }, 0);
      var nAnti = levels.filter(function(l) { return l.type === 'anti'; }).reduce(function(acc, l) { return acc + l.electrons; }, 0);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`• Valence Electrons: ${dia.valenceE}`, rx + 14, ry + 65);
      ctx.fillText(`• Bonding e⁻ (Nb):   ${nBond}`, rx + 14, ry + 85);
      ctx.fillText(`• Antibonding e⁻ (Na):${nAnti}`, rx + 14, ry + 105);

      ctx.strokeStyle = '#334155';
      ctx.beginPath();
      ctx.moveTo(rx + 14, ry + 120);
      ctx.lineTo(rx + rw - 14, ry + 120);
      ctx.stroke();

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 13px monospace';
      ctx.fillText(`Bond Order = ½(Nb - Na)`, rx + 14, ry + 145);
      ctx.fillText(`BO = ${dia.bo.toFixed(1)}`, rx + 14, ry + 168);

      ctx.fillStyle = dia.mag.includes('Paramagnetic') ? '#f43f5e' : '#38bdf8';
      ctx.font = 'bold 12px system-ui, sans-serif';
      ctx.fillText('Magnetic Character:', rx + 14, ry + 205);
      ctx.font = '11px monospace';
      ctx.fillText(dia.mag.split('(')[0], rx + 14, ry + 225);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px system-ui, sans-serif';
      var expl = dia.mag.includes('(') ? '(' + dia.mag.split('(')[1] : '';
      ctx.fillText(expl, rx + 14, ry + 245);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px system-ui, sans-serif';
      ctx.fillText(dia.mixing ? '★ s-p mixing observed' : '★ Normal ordering (no s-p mixing)', rx + 14, ry + 285);

      requestAnimationFrame(draw);
    }

    draw();
  };

  // =========================================================================
  // 6. sim_chem_bent_rule_hybridization (Unit 6)
  // Orbital Hybridization & Bent's Rule s/p Character Engine
  // =========================================================================
  window.Inorg1Sims.sim_chem_bent_rule_hybridization = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var state = {
      substituentEN: 4.0, // 2.0 (H) to 4.0 (F)
      angle: 104.5
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Substituent Electronegativity (X):</label>
        <input type="range" id="${controlsId}-en" min="2.0" max="4.0" step="0.1" value="4.0" style="width:140px; accent-color:#0284c7;">
        <span id="${controlsId}-en-val" style="color:#38bdf8; font-family:monospace; font-size:0.85rem;">4.0 (Fluorine)</span>
      `;

      var enSlider = document.getElementById(controlsId + '-en');
      var enVal = document.getElementById(controlsId + '-en-val');
      if (enSlider) {
        enSlider.addEventListener('input', function(e) {
          state.substituentEN = parseFloat(e.target.value);
          if (enVal) {
            var label = state.substituentEN >= 3.8 ? 'Fluorine (F)' : (state.substituentEN >= 3.0 ? 'Chlorine (Cl)' : (state.substituentEN >= 2.5 ? 'Carbon (C)' : 'Hydrogen (H)'));
            enVal.innerText = `${state.substituentEN.toFixed(1)} (${label})`;
          }
        });
      }
    }

    function draw() {
      var w = setup.width;
      var h = setup.height;
      ctx.clearRect(0, 0, w, h);

      // Calculations via Bent's Rule:
      // Higher electronegativity of substituent -> demands more p-character in central atom hybrid pointing to it
      // %p = 75 + (substituentEN - 2.5) * 6
      var pctP = Math.min(88, Math.max(65, 75 + (state.substituentEN - 2.5) * 6.5));
      var pctS = 100 - pctP;

      // Resulting inter-bond angle via cos θ = -s / (1 - s) = -s / p
      var sFrac = pctS / 100;
      var pFrac = pctP / 100;
      var cosTheta = -sFrac / pFrac;
      var thetaRad = Math.acos(Math.max(-1, Math.min(1, cosTheta)));
      var thetaDeg = (thetaRad * 180 / Math.PI);

      // Left Panel: Dynamic Hybrid Lobe Contour
      ctx.fillStyle = '#050811';
      ctx.fillRect(15, 15, w * 0.62, h - 30);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(15, 15, w * 0.62, h - 30);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillText(`Bent's Rule Hybridization Geometry: Central Atom Lobe Distortion`, 28, 40);

      var cx = w * 0.31;
      var cy = h * 0.52;

      // Draw two hybrid bond lobes with angle thetaDeg
      var halfAngle = (thetaDeg * Math.PI / 180) / 2;

      [-halfAngle, halfAngle].forEach(function(ang) {
        ctx.save();
        ctx.translate(cx, cy);
        ctx.rotate(ang - Math.PI / 2);

        // Major hybrid lobe
        ctx.fillStyle = 'rgba(56, 189, 248, 0.45)';
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.ellipse(0, 55, 30 * (pctP / 75), 55, 0, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        // Minor back lobe (s-character dependent)
        ctx.fillStyle = 'rgba(244, 63, 94, 0.35)';
        ctx.strokeStyle = '#f43f5e';
        ctx.beginPath();
        ctx.ellipse(0, -18, 14 * (pctS / 25), 18, 0, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        // Ligand atom at tip
        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.arc(0, 115, 14, 0, 2 * Math.PI);
        ctx.fill();
        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 10px monospace';
        ctx.fillText('X', -3, 118);

        ctx.restore();
      });

      // Central atom nucleus
      ctx.fillStyle = '#fbbf24';
      ctx.beginPath();
      ctx.arc(cx, cy, 12, 0, 2 * Math.PI);
      ctx.fill();
      ctx.fillStyle = '#0f172a';
      ctx.font = 'bold 10px monospace';
      ctx.fillText('A', cx - 4, cy + 4);

      // Arc for bond angle
      ctx.strokeStyle = '#fbbf24';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(cx, cy, 45, -Math.PI / 2 - halfAngle, -Math.PI / 2 + halfAngle);
      ctx.stroke();

      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 12px monospace';
      ctx.fillText(`θ = ${thetaDeg.toFixed(1)}°`, cx - 25, cy - 55);

      // Right Panel: Bent's Rule Theorem HUD
      var rx = w * 0.67;
      var ry = 15;
      var rw = w * 0.31;
      var rh = h - 30;

      ctx.fillStyle = '#080d1a';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 14px system-ui, sans-serif';
      ctx.fillText("Bent's Rule Theorem", rx + 14, ry + 28);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`• Ligand EN (χ):      ${state.substituentEN.toFixed(1)}`, rx + 14, ry + 65);
      ctx.fillText(`• Directed % p-char:  ${pctP.toFixed(1)}%`, rx + 14, ry + 85);
      ctx.fillText(`• Directed % s-char:  ${pctS.toFixed(1)}%`, rx + 14, ry + 105);

      ctx.strokeStyle = '#334155';
      ctx.beginPath();
      ctx.moveTo(rx + 14, ry + 125);
      ctx.lineTo(rx + rw - 14, ry + 125);
      ctx.stroke();

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 12px monospace';
      ctx.fillText('Coulson Hybridization Eq:', rx + 14, ry + 150);
      ctx.fillText('cos θ = -s / (1 - s) = -s / p', rx + 14, ry + 170);

      ctx.fillStyle = '#ef4444';
      ctx.font = 'bold 12px monospace';
      ctx.fillText(`Calculated θ = ${thetaDeg.toFixed(1)}°`, rx + 14, ry + 205);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px system-ui, sans-serif';
      var textBent = "Bent's Formal Law: More electronegative substituents direct themselves into hybrid orbitals having greater p-character, thereby preserving stabilizing s-character in bonds directed to electropositive groups or non-bonding lone pairs.";
      var words = textBent.split(' ');
      var line = '';
      var yTxt = ry + 245;
      words.forEach(function(word) {
        var testLine = line + word + ' ';
        if (ctx.measureText(testLine).width > rw - 35) {
          ctx.fillText(line, rx + 14, yTxt);
          line = word + ' ';
          yTxt += 16;
        } else {
          line = testLine;
        }
      });
      ctx.fillText(line, rx + 14, yTxt);

      requestAnimationFrame(draw);
    }

    draw();
  };

  // =========================================================================
  // 7. sim_chem_acid_base_titration_speciation (Unit 7)
  // Exact Polyprotic Acid-Base Titration & Speciation Curves
  // =========================================================================
  window.Inorg1Sims.sim_chem_acid_base_titration_speciation = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var systems = {
      'H3PO4': { name: 'Phosphoric Acid (H₃PO₄) - Triprotic', pKa1: 2.15, pKa2: 7.20, pKa3: 12.35, poly: 3 },
      'H2CO3': { name: 'Carbonic Acid (H₂CO₃) - Diprotic', pKa1: 6.35, pKa2: 10.33, pKa3: 14.0, poly: 2 },
      'CH3COOH': { name: 'Acetic Acid (CH₃COOH) - Monoprotic', pKa1: 4.76, pKa2: 14.0, pKa3: 14.0, poly: 1 }
    };

    var state = {
      sysKey: 'H3PO4',
      vAdded: 25.0 // mL NaOH added
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Acid System:</label>
        <select id="${controlsId}-sys" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; padding:4px 8px; border-radius:4px; font-size:0.85rem;">
          <option value="H3PO4" selected>Phosphoric Acid (H₃PO₄) - Triprotic</option>
          <option value="H2CO3">Carbonic Acid (H₂CO₃) - Diprotic Buffer</option>
          <option value="CH3COOH">Acetic Acid (CH₃COOH) - Monoprotic Buffer</option>
        </select>
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600; margin-left:12px;">NaOH Added (mL):</label>
        <input type="range" id="${controlsId}-v" min="0" max="60" step="0.5" value="25.0" style="width:120px; accent-color:#0284c7;">
        <span id="${controlsId}-v-val" style="color:#38bdf8; font-family:monospace; font-size:0.85rem;">25.0 mL</span>
      `;

      var sSelect = document.getElementById(controlsId + '-sys');
      if (sSelect) {
        sSelect.addEventListener('change', function(e) {
          state.sysKey = e.target.value;
        });
      }
      var vSlider = document.getElementById(controlsId + '-v');
      var vVal = document.getElementById(controlsId + '-v-val');
      if (vSlider) {
        vSlider.addEventListener('input', function(e) {
          state.vAdded = parseFloat(e.target.value);
          if (vVal) vVal.innerText = `${state.vAdded.toFixed(1)} mL`;
        });
      }
    }

    function computePH(v, sys) {
      // Analytical titration curve approximation
      // 20 mL is eq 1, 40 mL is eq 2, 60 mL is eq 3
      if (v <= 0) return sys.pKa1 * 0.6;
      if (v < 20) {
        var ratio = Math.max(0.01, Math.min(99, v / (20 - v)));
        return sys.pKa1 + Math.log10(ratio);
      } else if (v === 20) {
        return (sys.pKa1 + sys.pKa2) / 2;
      } else if (v < 40 && sys.poly >= 2) {
        var vSub = v - 20;
        var ratio = Math.max(0.01, Math.min(99, vSub / (20 - vSub)));
        return sys.pKa2 + Math.log10(ratio);
      } else if (v === 40 && sys.poly >= 2) {
        return (sys.pKa2 + sys.pKa3) / 2;
      } else if (v < 60 && sys.poly >= 3) {
        var vSub = v - 40;
        var ratio = Math.max(0.01, Math.min(99, vSub / (20 - vSub)));
        return sys.pKa3 + Math.log10(ratio);
      } else {
        return 12.8 + Math.log10(Math.max(0.01, (v - 60) * 0.1 + 1));
      }
    }

    function draw() {
      var w = setup.width;
      var h = setup.height;
      ctx.clearRect(0, 0, w, h);

      var sys = systems[state.sysKey];

      // Left Panel: Titration Curve pH vs V_NaOH
      ctx.fillStyle = '#050811';
      ctx.fillRect(15, 15, w * 0.65, h - 30);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(15, 15, w * 0.65, h - 30);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillText(`Titration Curve: ${sys.name}`, 30, 40);

      var pX = 55;
      var pY = h - 55;
      var pW = w * 0.55;
      var pH = h - 110;

      // Axes
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(pX, pY - pH);
      ctx.lineTo(pX, pY);
      ctx.lineTo(pX + pW, pY);
      ctx.stroke();

      // Axis labels
      ctx.fillStyle = '#64748b';
      ctx.font = '10px monospace';
      for (var phIdx = 0; phIdx <= 14; phIdx += 2) {
        var yVal = pY - (phIdx / 14) * pH;
        ctx.fillText(phIdx, pX - 22, yVal + 4);
        ctx.strokeStyle = '#1e293b';
        ctx.beginPath();
        ctx.moveTo(pX, yVal);
        ctx.lineTo(pX + pW, yVal);
        ctx.stroke();
      }
      ctx.fillText('0 mL', pX, pY + 16);
      ctx.fillText('20 mL (Eq 1)', pX + pW * (20 / 60) - 25, pY + 16);
      ctx.fillText('40 mL (Eq 2)', pX + pW * (40 / 60) - 25, pY + 16);
      ctx.fillText('60 mL (Eq 3)', pX + pW - 35, pY + 16);

      // Plot curve
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var vStep = 0; vStep <= 60; vStep += 0.5) {
        var curPH = computePH(vStep, sys);
        var xPlot = pX + (vStep / 60) * pW;
        var yPlot = pY - (Math.min(14, curPH) / 14) * pH;
        if (vStep === 0) ctx.moveTo(xPlot, yPlot);
        else ctx.lineTo(xPlot, yPlot);
      }
      ctx.stroke();

      // Current Volume Marker
      var activePH = computePH(state.vAdded, sys);
      var curX = pX + (state.vAdded / 60) * pW;
      var curY = pY - (Math.min(14, activePH) / 14) * pH;

      ctx.strokeStyle = '#fbbf24';
      ctx.setLineDash([2, 4]);
      ctx.beginPath();
      ctx.moveTo(curX, pY);
      ctx.lineTo(curX, curY);
      ctx.lineTo(pX, curY);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#fbbf24';
      ctx.beginPath();
      ctx.arc(curX, curY, 6, 0, 2 * Math.PI);
      ctx.fill();

      // Right Panel: Speciation & Henderson-Hasselbalch Diagnostics
      var rx = w * 0.70;
      var ry = 15;
      var rw = w * 0.28;
      var rh = h - 30;

      ctx.fillStyle = '#080d1a';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 14px system-ui, sans-serif';
      ctx.fillText('Speciation Diagnostics', rx + 14, ry + 28);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`• NaOH Added:    ${state.vAdded.toFixed(1)} mL`, rx + 14, ry + 60);

      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 13px monospace';
      ctx.fillText(`• Solution pH:   ${activePH.toFixed(2)}`, rx + 14, ry + 85);

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`• pKa₁:          ${sys.pKa1.toFixed(2)}`, rx + 14, ry + 115);
      if (sys.poly >= 2) ctx.fillText(`• pKa₂:          ${sys.pKa2.toFixed(2)}`, rx + 14, ry + 135);
      if (sys.poly >= 3) ctx.fillText(`• pKa₃:          ${sys.pKa3.toFixed(2)}`, rx + 14, ry + 155);

      ctx.strokeStyle = '#334155';
      ctx.beginPath();
      ctx.moveTo(rx + 14, ry + 175);
      ctx.lineTo(rx + rw - 14, ry + 175);
      ctx.stroke();

      // Dominant Species Identification
      var dom = '';
      if (activePH < sys.pKa1) dom = (sys.poly === 3 ? 'H₃PO₄' : 'H₂CO₃');
      else if (activePH < sys.pKa2) dom = (sys.poly === 3 ? 'H₂PO₄⁻' : 'HCO₃⁻');
      else if (activePH < sys.pKa3) dom = (sys.poly === 3 ? 'HPO₄²⁻' : 'CO₃²⁻');
      else dom = (sys.poly === 3 ? 'PO₄³⁻' : 'CO₃²⁻');

      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 12px system-ui, sans-serif';
      ctx.fillText('Dominant Buffer Species:', rx + 14, ry + 200);
      ctx.font = 'bold 14px monospace';
      ctx.fillText(dom, rx + 14, ry + 225);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px system-ui, sans-serif';
      var buffNote = '';
      if (Math.abs(activePH - sys.pKa1) < 0.5) buffNote = 'Operating inside Maximum Buffer Capacity Zone (pH ≈ pKa₁)!';
      else if (Math.abs(activePH - sys.pKa2) < 0.5) buffNote = 'Operating inside Maximum Buffer Capacity Zone (pH ≈ pKa₂)!';
      else if (Math.abs(state.vAdded - 20) < 1) buffNote = 'First Equivalence Point: Sharp pH inflection leap!';
      else if (Math.abs(state.vAdded - 40) < 1) buffNote = 'Second Equivalence Point reached!';
      else buffNote = 'Henderson-Hasselbalch buffer equilibrium: pH = pKa + log([A⁻]/[HA]).';

      var words = buffNote.split(' ');
      var line = '';
      var yTxt = ry + 265;
      words.forEach(function(word) {
        var testLine = line + word + ' ';
        if (ctx.measureText(testLine).width > rw - 35) {
          ctx.fillText(line, rx + 14, yTxt);
          line = word + ' ';
          yTxt += 16;
        } else {
          line = testLine;
        }
      });
      ctx.fillText(line, rx + 14, yTxt);

      requestAnimationFrame(draw);
    }

    draw();
  };

  // =========================================================================
  // 8. sim_chem_redox_latimer_frost_diagram (Unit 8)
  // Dynamic Latimer & Frost Oxidation State Diagram Analyzer
  // =========================================================================
  window.Inorg1Sims.sim_chem_redox_latimer_frost_diagram = function(canvasId, controlsId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var controls = document.getElementById(controlsId);
    var setup = setupCanvas(canvas);
    var ctx = setup.ctx;

    var elements = {
      'Mn': {
        name: 'Manganese Species (Acid pH 0)',
        // Oxidation states: 0 to +7
        // deltaG/F = -nE°
        points: [
          { ox: 0, species: 'Mn', nE: 0.0 },
          { ox: 2, species: 'Mn²⁺', nE: -2.36 },
          { ox: 3, species: 'Mn³⁺', nE: -0.85 },
          { ox: 4, species: 'MnO₂', nE: +0.10 },
          { ox: 6, species: 'MnO₄²⁻', nE: +4.64 },
          { ox: 7, species: 'MnO₄⁻', nE: +5.20 }
        ],
        latimer: 'MnO₄⁻ --(+0.56V)--> MnO₄²⁻ --(+2.27V)--> MnO₂ --(+0.95V)--> Mn³⁺ --(+1.51V)--> Mn²⁺ --(-1.18V)--> Mn'
      },
      'N': {
        name: 'Nitrogen Species (Acid pH 0)',
        points: [
          { ox: -3, species: 'NH₄⁺', nE: -0.81 },
          { ox: 0, species: 'N₂', nE: 0.0 },
          { ox: 1, species: 'N₂O', nE: +1.77 },
          { ox: 2, species: 'NO', nE: +3.36 },
          { ox: 3, species: 'HNO₂', nE: +4.35 },
          { ox: 4, species: 'NO₂', nE: +5.42 },
          { ox: 5, species: 'NO₃⁻', nE: +4.75 }
        ],
        latimer: 'NO₃⁻ --(+0.80V)--> NO₂ --(+1.07V)--> HNO₂ --(+1.00V)--> NO --(+1.59V)--> N₂O --(+1.77V)--> N₂'
      }
    };

    var state = {
      elKey: 'Mn',
      selPoint: elements['Mn'].points[4] // MnO4^2- (classic disproportionation convex peak)
    };

    if (controls) {
      controls.innerHTML = `
        <label style="color:#94a3b8; font-size:0.85rem; font-weight:600;">Redox System:</label>
        <button id="${controlsId}-btn-mn" class="pchem-btn" style="background:#0284c7; color:#fff; border:none; padding:4px 10px; border-radius:4px; font-size:0.8rem; cursor:pointer;">Manganese (Frost Disproportionation)</button>
        <button id="${controlsId}-btn-n" class="pchem-btn" style="background:#1e293b; color:#cbd5e1; border:1px solid #334155; padding:4px 10px; border-radius:4px; font-size:0.8rem; cursor:pointer;">Nitrogen (Multiple Oxidation States)</button>
      `;

      var btnMn = document.getElementById(controlsId + '-btn-mn');
      var btnN  = document.getElementById(controlsId + '-btn-n');
      if (btnMn && btnN) {
        btnMn.addEventListener('click', function() {
          state.elKey = 'Mn';
          state.selPoint = elements['Mn'].points[4];
          btnMn.style.background = '#0284c7'; btnMn.style.color = '#fff';
          btnN.style.background = '#1e293b'; btnN.style.color = '#cbd5e1';
        });
        btnN.addEventListener('click', function() {
          state.elKey = 'N';
          state.selPoint = elements['N'].points[4];
          btnN.style.background = '#0284c7'; btnN.style.color = '#fff';
          btnMn.style.background = '#1e293b'; btnMn.style.color = '#cbd5e1';
        });
      }
    }

    function draw() {
      var w = setup.width;
      var h = setup.height;
      ctx.clearRect(0, 0, w, h);

      var sys = elements[state.elKey];

      // Left Panel: Frost Diagram Plot (nE° vs Oxidation Number N)
      ctx.fillStyle = '#050811';
      ctx.fillRect(15, 15, w * 0.65, h - 30);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(15, 15, w * 0.65, h - 30);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px system-ui, sans-serif';
      ctx.fillText(`Frost Oxidation State Diagram: ${sys.name}`, 30, 40);

      var pX = 65;
      var pY = h * 0.65;
      var pW = w * 0.53;
      var pH = h * 0.60;

      // Draw zero axis
      ctx.strokeStyle = '#334155';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(pX, pY);
      ctx.lineTo(pX + pW, pY);
      ctx.stroke();
      ctx.setLineDash([]);

      // Vertical zero axis (Ox = 0)
      var minOx = (state.elKey === 'N') ? -3 : 0;
      var maxOx = (state.elKey === 'N') ? 5 : 7;
      var xZeroOx = pX + ((0 - minOx) / (maxOx - minOx)) * pW;
      ctx.strokeStyle = '#334155';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(xZeroOx, 45);
      ctx.lineTo(xZeroOx, h - 30);
      ctx.stroke();
      ctx.setLineDash([]);

      // Plot Frost Points
      var minNE = -3.0;
      var maxNE = 6.0;

      function toPlot(ox, nE) {
        var px = pX + ((ox - minOx) / (maxOx - minOx)) * pW;
        var py = pY - (nE / (maxNE - minNE)) * pH;
        return { x: px, y: py };
      }

      // Draw connecting lines
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      sys.points.forEach(function(pt, idx) {
        var pr = toPlot(pt.ox, pt.nE);
        if (idx === 0) ctx.moveTo(pr.x, pr.y);
        else ctx.lineTo(pr.x, pr.y);
      });
      ctx.stroke();

      // Disproportionation convex tie-line for Mn(VI)
      if (state.elKey === 'Mn') {
        var pMnO2 = toPlot(4, 0.10);
        var pMnO4 = toPlot(7, 5.20);
        ctx.strokeStyle = '#f43f5e';
        ctx.setLineDash([4, 4]);
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(pMnO2.x, pMnO2.y);
        ctx.lineTo(pMnO4.x, pMnO4.y);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Draw Point Nodes
      sys.points.forEach(function(pt) {
        var pr = toPlot(pt.ox, pt.nE);
        var isSel = (pt.species === state.selPoint.species);

        ctx.fillStyle = isSel ? '#fbbf24' : '#38bdf8';
        ctx.beginPath();
        ctx.arc(pr.x, pr.y, isSel ? 7 : 4.5, 0, 2 * Math.PI);
        ctx.fill();

        ctx.fillStyle = isSel ? '#fbbf24' : '#cbd5e1';
        ctx.font = 'bold 11px system-ui, sans-serif';
        ctx.fillText(pt.species, pr.x - 12, pr.y - 10);
      });

      // Axis labels
      ctx.fillStyle = '#64748b';
      ctx.font = '10px monospace';
      ctx.fillText('Oxidation Number (N) →', pX + pW - 120, pY + 16);
      ctx.fillText('ΔG°/F = -nE° (V) ↑', pX - 45, 60);

      // Latimer Chain Below Plot
      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px monospace';
      ctx.fillText('Latimer Chain:', 30, h - 35);
      ctx.fillStyle = '#cbd5e1';
      ctx.fillText(sys.latimer, 30, h - 22);

      // Right Panel: Thermodynamic Disproportionation Analysis
      var rx = w * 0.70;
      var ry = 15;
      var rw = w * 0.28;
      var rh = h - 30;

      ctx.fillStyle = '#080d1a';
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 14px system-ui, sans-serif';
      ctx.fillText('Frost Curve Diagnostics', rx + 14, ry + 28);

      var sel = state.selPoint;
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px monospace';
      ctx.fillText(`• Species:       ${sel.species}`, rx + 14, ry + 60);
      ctx.fillText(`• Oxidation No:  +${sel.ox}`, rx + 14, ry + 80);
      ctx.fillText(`• Voltage nE°:   ${sel.nE.toFixed(2)} V`, rx + 14, ry + 100);

      ctx.strokeStyle = '#334155';
      ctx.beginPath();
      ctx.moveTo(rx + 14, ry + 120);
      ctx.lineTo(rx + rw - 14, ry + 120);
      ctx.stroke();

      // Frost Thermodynamic Stability Rule
      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 12px system-ui, sans-serif';
      ctx.fillText('Convexity Criterion:', rx + 14, ry + 145);

      var ruleText = '';
      if (sel.species === 'MnO₄²⁻') {
        ruleText = 'Convex Peak (Above tie-line): Thermodynamically UNSTABLE toward spontaneous disproportionation into MnO₂ + MnO₄⁻!';
      } else if (sel.species === 'Mn²⁺') {
        ruleText = 'Deepest Thermodynamic Concavity: Most stable species in acidic solution. High resistance to reduction or oxidation.';
      } else if (sel.species === 'N₂') {
        ruleText = 'Absolute Thermodynamic Minimum (nE° = 0): Colossally stable triple bond N≡N sink.';
      } else if (sel.species === 'HNO₂') {
        ruleText = 'Convex intermediate: Readily disproportionates into NO and NO₃⁻ in acidic media.';
      } else {
        ruleText = 'Slope of line connecting any two species gives the standard reduction potential E° of that redox couple!';
      }

      ctx.fillStyle = (sel.species === 'MnO₄²⁻' || sel.species === 'HNO₂') ? '#f43f5e' : '#10b981';
      var words = ruleText.split(' ');
      var line = '';
      var yTxt = ry + 175;
      words.forEach(function(word) {
        var testLine = line + word + ' ';
        if (ctx.measureText(testLine).width > rw - 35) {
          ctx.fillText(line, rx + 14, yTxt);
          line = word + ' ';
          yTxt += 16;
        } else {
          line = testLine;
        }
      });
      ctx.fillText(line, rx + 14, yTxt);

      requestAnimationFrame(draw);
    }

    draw();
  };

  // =========================================================================
  // window.SimulationEngine Mount Adapter
  // =========================================================================
  var SIM_TITLES = {
    sim_chem_bohr_schrodinger_orbitals: "3D Hydrogenic Atomic Orbitals & Radial Distribution Function Visualizer",
    sim_chem_periodic_trends_explorer: "Interactive Periodic Trends Matrix & Slater Z_eff Calculator",
    sim_chem_born_haber_lattice_cycle: "Thermochemical Born-Haber Cycle & Born-Landé Lattice Energy Engine",
    sim_chem_vsepr_molecular_geometry: "3D VSEPR Molecular Geometry Engine & Lone-Pair Dipole Analyzer",
    sim_chem_molecular_orbital_lcao: "LCAO-MO Diatomic Energy Level Generator & Magnetic Analyzer",
    sim_chem_bent_rule_hybridization: "Orbital Hybridization & Bent's Rule s/p Character Engine",
    sim_chem_acid_base_titration_speciation: "Exact Polyprotic Acid-Base Titration & Speciation Curves",
    sim_chem_redox_latimer_frost_diagram: "Dynamic Latimer & Frost Oxidation State Diagram Analyzer"
  };

  window.SimulationEngine = window.SimulationEngine || {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!window.Inorg1Sims || typeof window.Inorg1Sims[simType] !== 'function') {
      console.warn('Simulation type not found in Inorg1Sims:', simType);
      return;
    }

    var title = SIM_TITLES[simType] || "Inorganic Chemistry Interactive Simulation";
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
      window.Inorg1Sims[simType](canvasId, controlsId);
    }, 50);
  };

})();
'''

with open("inorganic-chemistry-1-sims.js", "w", encoding="utf-8") as f:
    f.write(sims_code)

print("SUCCESS: inorganic-chemistry-1-sims.js created with 8 interactive 60 FPS simulations.")
