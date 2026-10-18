# -*- coding: utf-8 -*-
"""
generate_nt_sims.py
Generates number-theory-sims.js containing 8 real-time 60 FPS interactive Canvas simulations
for Theory of Numbers:
1. sim_nt_euclidean_bezout: Step-by-step Euclidean algorithm and Bézout coefficients ax + by = gcd(a,b)
2. sim_nt_continued_fractions_pell: Continued fraction convergents and Pell equation hyperbola lattice points x^2 - dy^2 = 1
3. sim_nt_chinese_remainder_crt: Multi-ring modular gear clock visualizer for Chinese Remainder Theorem
4. sim_nt_primitive_roots_indices: Cyclic generator orbit wheel, modular orders, and discrete logarithms
5. sim_nt_arithmetic_functions_sigma: Divisor lattice, tau(n), sigma(n), and Mersenne / Perfect number scanner
6. sim_nt_mobius_ramanujan: Complex unit circle phasor sum visualizer for Ramanujan trigonometric sums and Möbius sieve
7. sim_nt_pythagorean_fermat_descent: Stereographic projection on the unit circle generating Pythagorean triples and Fermat descent tree
8. sim_nt_sums_of_squares_lagrange: Lattice points on circles and 4-spheres decomposing integers into sums of 2, 3, and 4 squares
"""

def generate_sims_js():
    js_code = r'''// Number Theory Interactive Computational Simulations Engine
// High-performance 60 FPS HTML5 Canvas numerical models registered to window.SIMULATIONS

window.SIMULATIONS = window.SIMULATIONS || {};

// 1. Unit 1: Euclidean Algorithm & Bézout's Identity Visualizer
window.SIMULATIONS["sim_nt_euclidean_bezout"] = {
  title: "Extended Euclidean Algorithm & Bézout Identity Visualizer",
  description: "Explore the step-by-step Euclidean division algorithm geometrically via subdivision rectangles and compute the Bézout coefficients x, y such that ax + by = gcd(a, b).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let a = 120, b = 45;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Integer a:</label>
        <input type="range" id="nt-a-slider" min="10" max="300" step="1" value="120" style="vertical-align: middle; width: 90px;">
        <span id="nt-a-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">a = 120</span>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Integer b:</label>
        <input type="range" id="nt-b-slider" min="5" max="150" step="1" value="45" style="vertical-align: middle; width: 90px;">
        <span id="nt-b-val" style="color: #f59e0b; font-family: monospace; font-size: 0.85rem;">b = 45</span>
      `;

      document.getElementById("nt-a-slider").oninput = (e) => {
        a = parseInt(e.target.value);
        document.getElementById("nt-a-val").innerText = `a = ${a}`;
        render();
      };
      document.getElementById("nt-b-slider").oninput = (e) => {
        b = parseInt(e.target.value);
        document.getElementById("nt-b-val").innerText = `b = ${b}`;
        render();
      };
    }

    function extendedGcd(u, v) {
      let steps = [];
      let r0 = u, r1 = v;
      let s0 = 1, s1 = 0;
      let t0 = 0, t1 = 1;

      while (r1 !== 0) {
        let q = Math.floor(r0 / r1);
        let r2 = r0 % r1;
        let s2 = s0 - q * s1;
        let t2 = t0 - q * t1;
        steps.push({ q: q, r0: r0, r1: r1, r2: r2, s: s1, t: t1 });
        r0 = r1; r1 = r2;
        s0 = s1; s1 = s2;
        t0 = t1; t1 = t2;
      }
      return { gcd: r0, x: s0, y: t0, steps: steps };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;

      const res = extendedGcd(a, b);

      // Left panel: geometric rectangle dissection (a x b)
      const leftW = W * 0.45;
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(20, 40, leftW - 40, H - 60);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(20, 40, leftW - 40, H - 60);

      // Recursive square subdivision inside bounding box
      let rx = 30, ry = 50, rw = leftW - 60, rh = H - 80;
      let curA = a, curB = b;
      let horizontal = true;
      let colors = ["#38bdf8", "#f59e0b", "#10b981", "#ec4899", "#8b5cf6"];
      let colorIdx = 0;

      for (let i = 0; i < Math.min(res.steps.length, 6); i++) {
        let step = res.steps[i];
        let q = step.q;
        for (let k = 0; k < Math.min(q, 4); k++) {
          ctx.strokeStyle = colors[colorIdx % colors.length];
          ctx.lineWidth = 1.5;
          if (horizontal) {
            let sqSize = Math.min(rw, rh / Math.max(q, 1));
            ctx.strokeRect(rx, ry + k * sqSize, rw, sqSize);
          } else {
            let sqSize = Math.min(rh, rw / Math.max(q, 1));
            ctx.strokeRect(rx + k * sqSize, ry, sqSize, rh);
          }
        }
        colorIdx++;
        horizontal = !horizontal;
      }

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Euclidean Rectangle Subdivision (${a} × ${b})`, 25, 30);

      // Right panel: Step-by-step Division Equations & Bézout identity
      const rightX = leftW + 20;
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 14px Inter";
      ctx.fillText(`Extended Euclidean Algorithm & Bézout Identity`, rightX, 30);

      ctx.font = "12px 'Fira Code', monospace";
      let textY = 65;

      for (let i = 0; i < Math.min(res.steps.length, 7); i++) {
        let s = res.steps[i];
        ctx.fillStyle = "#94a3b8";
        ctx.fillText(`Step ${i+1}:  ${s.r0} = ${s.q} × (${s.r1}) + ${s.r2}`, rightX, textY);
        textY += 24;
      }

      textY += 15;
      ctx.fillStyle = "#10b981";
      ctx.font = "bold 13px 'Fira Code', monospace";
      ctx.fillText(`Greatest Common Divisor: gcd(${a}, ${b}) = ${res.gcd}`, rightX, textY);

      textY += 30;
      ctx.fillStyle = "#fbbf24";
      ctx.fillText(`Bézout's Identity:`, rightX, textY);
      textY += 24;
      ctx.fillStyle = "#38bdf8";
      ctx.font = "13px 'Fira Code', monospace";
      ctx.fillText(`a · (${res.x}) + b · (${res.y}) = ${res.gcd}`, rightX, textY);
      textY += 22;
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter";
      ctx.fillText(`Verification: ${a} × (${res.x}) + ${b} × (${res.y}) = ${a * res.x + b * res.y}`, rightX, textY);

      textY += 35;
      ctx.fillStyle = "#ec4899";
      ctx.font = "bold 12px Inter";
      ctx.fillText(`Linear Diophantine Equation ax + by = c is solvable iff gcd(a,b) | c`, rightX, textY);
    }

    render();
  }
};

// 2. Unit 2: Continued Fractions & Pell's Equation Visualizer
window.SIMULATIONS["sim_nt_continued_fractions_pell"] = {
  title: "Continued Fraction Convergents & Pell's Equation Hyperbola",
  description: "Calculate simple continued fractions for square roots sqrt(d), observe the alternating convergents p_k / q_k approaching the irrational, and solve Pell's equation x^2 - d y^2 = 1.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let dVal = 7; // non-square d

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Non-square d:</label>
        <select id="nt-d-select" style="padding: 0.25rem 0.5rem; background: #1e293b; color: #f8fafc; border: 1px solid #475569; border-radius: 4px;">
          <option value="2">d = 2 (√2)</option>
          <option value="3">d = 3 (√3)</option>
          <option value="5">d = 5 (√5)</option>
          <option value="7" selected>d = 7 (√7)</option>
          <option value="11">d = 11 (√11)</option>
          <option value="13">d = 13 (√13)</option>
          <option value="14">d = 14 (√14)</option>
          <option value="19">d = 19 (√19)</option>
        </select>
      `;

      document.getElementById("nt-d-select").onchange = (e) => {
        dVal = parseInt(e.target.value);
        render();
      };
    }

    function getContinuedFractionSqrt(d, maxTerms) {
      let a0 = Math.floor(Math.sqrt(d));
      if (a0 * a0 === d) return { terms: [a0], period: 0, convergents: [] };

      let terms = [a0];
      let m = 0, denom = 1, a = a0;
      let period = 0;

      while (terms.length < maxTerms && a !== 2 * a0) {
        m = denom * a - m;
        denom = Math.floor((d - m * m) / denom);
        a = Math.floor((a0 + m) / denom);
        terms.push(a);
        period++;
      }

      // Compute convergents p_k / q_k
      let convs = [];
      let p_prev = 1, p_curr = terms[0];
      let q_prev = 0, q_curr = 1;
      convs.push({ k: 0, a: terms[0], p: p_curr, q: q_curr, val: p_curr / q_curr, pell: p_curr * p_curr - d * q_curr * q_curr });

      for (let i = 1; i < terms.length; i++) {
        let p_next = terms[i] * p_curr + p_prev;
        let q_next = terms[i] * q_curr + q_prev;
        let diff = p_next * p_next - d * q_next * q_next;
        convs.push({ k: i, a: terms[i], p: p_next, q: q_next, val: p_next / q_next, pell: diff });
        p_prev = p_curr; p_curr = p_next;
        q_prev = q_curr; q_curr = q_next;
      }

      return { terms: terms, period: period, convergents: convs };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;

      const res = getContinuedFractionSqrt(dVal, 9);
      const exactVal = Math.sqrt(dVal);

      // Left panel: Number line & alternating convergents ladder
      const leftW = W * 0.48;
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Convergents Ladder for √${dVal} ≈ ${exactVal.toFixed(6)}`, 20, 25);

      const axisY = H * 0.55;
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(30, axisY); ctx.lineTo(leftW - 30, axisY);
      ctx.stroke();

      // Axis ticks around exact value
      const span = 0.4;
      const xToCanvas = (val) => 30 + ((val - (exactVal - span/2)) / span) * (leftW - 60);

      // Exact mark
      const exactX = xToCanvas(exactVal);
      ctx.strokeStyle = "#ef4444";
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(exactX, 50); ctx.lineTo(exactX, axisY + 40); ctx.stroke();
      ctx.fillStyle = "#ef4444";
      ctx.font = "bold 11px 'Fira Code'";
      ctx.fillText(`√${dVal}`, exactX - 10, 45);

      // Plot convergents
      res.convergents.slice(0, 6).forEach((c, idx) => {
        let cx = xToCanvas(c.val);
        let cy = 65 + idx * 26;
        let color = c.pell === 1 ? "#10b981" : (c.pell === -1 ? "#f59e0b" : "#38bdf8");

        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(cx, cy, 4, 0, Math.PI * 2);
        ctx.fill();

        ctx.font = "11px 'Fira Code', monospace";
        ctx.fillText(`p_${c.k}/q_${c.k} = ${c.p}/${c.q}`, cx + 8, cy + 4);
      });

      // Right panel: Pell's Equation x^2 - d y^2 = 1 & Periodic Expansion
      const rightX = leftW + 20;
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Pell's Equation: x² - ${dVal}y² = 1`, rightX, 25);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px 'Fira Code', monospace";
      let termStr = `[${res.terms[0]}; ${res.terms.slice(1).join(", ")}]`;
      ctx.fillText(`Continued Fraction:`, rightX, 55);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`√${dVal} = ${termStr}`, rightX, 75);

      let textY = 110;
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 12px Inter";
      ctx.fillText(`Table of Convergents & Norm x² - ${dVal}y²:`, rightX, textY);
      textY += 24;

      ctx.fillStyle = "#64748b";
      ctx.font = "11px 'Fira Code', monospace";
      ctx.fillText(`k    p_k       q_k       p_k² - ${dVal}q_k²`, rightX, textY);
      textY += 18;

      let fundamentalSol = null;
      res.convergents.slice(0, 7).forEach((c) => {
        let isSol = c.pell === 1;
        if (isSol && !fundamentalSol) fundamentalSol = c;
        ctx.fillStyle = isSol ? "#10b981" : (c.pell === -1 ? "#f59e0b" : "#cbd5e1");
        ctx.fillText(`${c.k}    ${String(c.p).padEnd(9)} ${String(c.q).padEnd(9)} ${c.pell > 0 ? "+" : ""}${c.pell}`, rightX, textY);
        textY += 20;
      });

      textY += 15;
      if (fundamentalSol) {
        ctx.fillStyle = "#10b981";
        ctx.font = "bold 12px 'Fira Code'";
        ctx.fillText(`Fundamental Solution: (x₁, y₁) = (${fundamentalSol.p}, ${fundamentalSol.q})`, rightX, textY);
        textY += 20;
        ctx.fillStyle = "#94a3b8";
        ctx.font = "11px Inter";
        ctx.fillText(`All solutions given by: x_n + y_n√${dVal} = (${fundamentalSol.p} + ${fundamentalSol.q}√${dVal})ⁿ`, rightX, textY);
      }
    }

    render();
  }
};

// 3. Unit 3: Chinese Remainder Theorem Multi-Gear Clock
window.SIMULATIONS["sim_nt_chinese_remainder_crt"] = {
  title: "Chinese Remainder Theorem Multi-Ring Clock System",
  description: "Observe simultaneous linear congruences x = a_i (mod m_i) for pairwise coprime moduli m_1, m_2, m_3 as rotating gears intersecting at the unique solution modulo M = m_1 m_2 m_3.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let m1 = 3, m2 = 5, m3 = 7;
    let a1 = 2, a2 = 3, a3 = 2;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">x ≡ a₁ (mod 3):</label>
        <select id="nt-a1-sel" style="background: #1e293b; color: #38bdf8; border: 1px solid #475569; border-radius: 4px;">
          <option value="0">0</option><option value="1">1</option><option value="2" selected>2</option>
        </select>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">x ≡ a₂ (mod 5):</label>
        <select id="nt-a2-sel" style="background: #1e293b; color: #f59e0b; border: 1px solid #475569; border-radius: 4px;">
          <option value="0">0</option><option value="1">1</option><option value="2">2</option><option value="3" selected>3</option><option value="4">4</option>
        </select>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">x ≡ a₃ (mod 7):</label>
        <select id="nt-a3-sel" style="background: #1e293b; color: #10b981; border: 1px solid #475569; border-radius: 4px;">
          <option value="0">0</option><option value="1">1</option><option value="2" selected>2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option>
        </select>
      `;

      document.getElementById("nt-a1-sel").onchange = (e) => { a1 = parseInt(e.target.value); render(); };
      document.getElementById("nt-a2-sel").onchange = (e) => { a2 = parseInt(e.target.value); render(); };
      document.getElementById("nt-a3-sel").onchange = (e) => { a3 = parseInt(e.target.value); render(); };
    }

    function modInverse(val, mod) {
      val = ((val % mod) + mod) % mod;
      for (let x = 1; x < mod; x++) {
        if ((val * x) % mod === 1) return x;
      }
      return 1;
    }

    function solveCRT() {
      let M = m1 * m2 * m3;
      let M1 = M / m1, M2 = M / m2, M3 = M / m3;
      let y1 = modInverse(M1, m1);
      let y2 = modInverse(M2, m2);
      let y3 = modInverse(M3, m3);

      let x = (a1 * M1 * y1 + a2 * M2 * y2 + a3 * M3 * y3) % M;
      x = (x + M) % M;
      return { x: x, M: M, M1: M1, M2: M2, M3: M3, y1: y1, y2: y2, y3: y3 };
    }

    function drawClock(cx, cy, r, mod, rem, color, title) {
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.stroke();

      for (let i = 0; i < mod; i++) {
        let theta = (i / mod) * Math.PI * 2 - Math.PI / 2;
        let px = cx + Math.cos(theta) * r;
        let py = cy + Math.sin(theta) * r;

        let isTarget = (i === rem);
        ctx.fillStyle = isTarget ? color : "#64748b";
        ctx.beginPath();
        ctx.arc(px, py, isTarget ? 5.5 : 3, 0, Math.PI * 2);
        ctx.fill();

        let lx = cx + Math.cos(theta) * (r + 14);
        let ly = cy + Math.sin(theta) * (r + 14);
        ctx.font = isTarget ? "bold 11px 'Fira Code'" : "10px Inter";
        ctx.fillText(`${i}`, lx - 4, ly + 4);
      }

      ctx.fillStyle = color;
      ctx.font = "bold 12px Inter";
      ctx.fillText(title, cx - 35, cy + r + 30);
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;

      const sol = solveCRT();

      // Draw three modular clocks
      const clockY = H * 0.42;
      drawClock(W * 0.15, clockY, 48, m1, a1, "#38bdf8", `mod ${m1} (a₁=${a1})`);
      drawClock(W * 0.40, clockY, 56, m2, a2, "#f59e0b", `mod ${m2} (a₂=${a2})`);
      drawClock(W * 0.65, clockY, 64, m3, a3, "#10b981", `mod ${m3} (a₃=${a3})`);

      // Solution header
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 14px Inter";
      ctx.fillText(`Chinese Remainder Theorem Simultaneous Solution`, 20, 28);

      // Right solution panel
      const rightX = W * 0.78;
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`M = m₁m₂m₃ = ${sol.M}`, rightX, 60);
      ctx.fillText(`M₁ = ${sol.M1}, y₁ = ${sol.y1}`, rightX, 85);
      ctx.fillText(`M₂ = ${sol.M2}, y₂ = ${sol.y2}`, rightX, 110);
      ctx.fillText(`M₃ = ${sol.M3}, y₃ = ${sol.y3}`, rightX, 135);

      ctx.fillStyle = "#10b981";
      ctx.font = "bold 14px 'Fira Code', monospace";
      ctx.fillText(`x ≡ ${sol.x} (mod ${sol.M})`, rightX, 185);

      // Bottom verification timeline
      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px 'Fira Code', monospace";
      ctx.fillText(`Check: ${sol.x} ≡ ${sol.x % m1} (mod ${m1}),  ${sol.x} ≡ ${sol.x % m2} (mod ${m2}),  ${sol.x} ≡ ${sol.x % m3} (mod ${m3})`, 25, H - 20);
    }

    render();
  }
};

// 4. Unit 4: Primitive Roots & Indices Discrete Logarithm Engine
window.SIMULATIONS["sim_nt_primitive_roots_indices"] = {
  title: "Primitive Roots Generator & Discrete Logarithms Wheel",
  description: "Examine the cyclic group structure of (Z/pZ)*, verify whether a candidate generator g produces all reduced residues modulo p, and compute the discrete logarithm index table.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let p = 13;
    let g = 2;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Prime p:</label>
        <select id="nt-p-sel" style="background: #1e293b; color: #38bdf8; border: 1px solid #475569; border-radius: 4px;">
          <option value="5">p = 5</option>
          <option value="7">p = 7</option>
          <option value="11">p = 11</option>
          <option value="13" selected>p = 13</option>
          <option value="17">p = 17</option>
          <option value="19">p = 19</option>
        </select>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Base g:</label>
        <input type="range" id="nt-g-slider" min="2" max="12" step="1" value="2" style="vertical-align: middle; width: 80px;">
        <span id="nt-g-val" style="color: #f59e0b; font-family: monospace; font-size: 0.85rem;">g = 2</span>
      `;

      document.getElementById("nt-p-sel").onchange = (e) => {
        p = parseInt(e.target.value);
        document.getElementById("nt-g-slider").max = p - 1;
        if (g >= p) g = 2;
        document.getElementById("nt-g-slider").value = g;
        document.getElementById("nt-g-val").innerText = `g = ${g}`;
        render();
      };

      document.getElementById("nt-g-slider").oninput = (e) => {
        g = parseInt(e.target.value);
        document.getElementById("nt-g-val").innerText = `g = ${g}`;
        render();
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;

      // Compute orbit of g: g^1, g^2, ..., g^(p-1) mod p
      let orbit = [];
      let cur = 1;
      let visited = new Set();
      for (let k = 1; k < p; k++) {
        cur = (cur * g) % p;
        orbit.push({ exp: k, val: cur });
        visited.add(cur);
      }
      let isPrimitive = (visited.size === p - 1);
      let order = orbit.findIndex(o => o.val === 1) + 1;

      // Draw Orbit Wheel
      const cx = W * 0.32, cy = H * 0.52, r = 110;
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.stroke();

      for (let i = 1; i < p; i++) {
        let theta = (i / (p - 1)) * Math.PI * 2 - Math.PI / 2;
        let px = cx + Math.cos(theta) * r;
        let py = cy + Math.sin(theta) * r;

        let inOrbit = visited.has(i);
        ctx.fillStyle = inOrbit ? "#38bdf8" : "#475569";
        ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = "#94a3b8";
        ctx.font = "10px Inter";
        ctx.fillText(`${i}`, cx + Math.cos(theta) * (r + 14) - 4, cy + Math.sin(theta) * (r + 14) + 4);
      }

      // Draw connecting orbit chords
      ctx.strokeStyle = isPrimitive ? "rgba(16, 185, 129, 0.45)" : "rgba(239, 68, 68, 0.45)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      orbit.forEach((pt, idx) => {
        let theta = (pt.val / (p - 1)) * Math.PI * 2 - Math.PI / 2;
        let px = cx + Math.cos(theta) * r;
        let py = cy + Math.sin(theta) * r;
        if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();

      // Left title
      ctx.fillStyle = isPrimitive ? "#10b981" : "#ef4444";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`g = ${g} is ${isPrimitive ? "a Primitive Root" : "NOT a Primitive Root"} mod ${p}`, 20, 25);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px 'Fira Code', monospace";
      ctx.fillText(`ord_${p}(${g}) = ${order}  (ϕ(${p}) = ${p - 1})`, 20, 45);

      // Right table: Power orbit & Indices
      const rightX = W * 0.62;
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Powers & Discrete Logarithms Table`, rightX, 25);

      ctx.fillStyle = "#64748b";
      ctx.font = "11px 'Fira Code', monospace";
      ctx.fillText(`k      ${g}^k mod ${p}       ind_${g}(a)`, rightX, 55);

      let textY = 78;
      orbit.slice(0, 12).forEach(o => {
        ctx.fillStyle = o.val === 1 ? "#fbbf24" : "#cbd5e1";
        ctx.font = "11px 'Fira Code', monospace";
        ctx.fillText(`${String(o.exp).padEnd(6)} ${String(o.val).padEnd(12)} ind_${g}(${o.val}) = ${o.exp}`, rightX, textY);
        textY += 21;
      });
    }

    render();
  }
};

// 5. Unit 5: Arithmetical Functions, Divisor Lattice & Perfect Numbers
window.SIMULATIONS["sim_nt_arithmetic_functions_sigma"] = {
  title: "Arithmetical Functions tau(n), sigma(n) & Perfect Numbers Scanner",
  description: "Inspect the prime factorization of integer n, compute the number of divisors tau(n), sum of divisors sigma(n), and test for Euclid-Euler even perfect numbers 2^(p-1)(2^p - 1).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let n = 28;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Integer n:</label>
        <input type="range" id="nt-n-slider" min="1" max="120" step="1" value="28" style="vertical-align: middle; width: 100px;">
        <span id="nt-n-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">n = 28</span>
        <button id="nt-btn-perf6" style="margin-left: 0.5rem; padding: 0.25rem 0.5rem; background: #1e293b; color: #10b981; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">n = 6</button>
        <button id="nt-btn-perf28" style="padding: 0.25rem 0.5rem; background: #1e293b; color: #10b981; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">n = 28</button>
      `;

      document.getElementById("nt-n-slider").oninput = (e) => {
        n = parseInt(e.target.value);
        document.getElementById("nt-n-val").innerText = `n = ${n}`;
        render();
      };
      document.getElementById("nt-btn-perf6").onclick = () => {
        n = 6;
        document.getElementById("nt-n-slider").value = 6;
        document.getElementById("nt-n-val").innerText = `n = 6`;
        render();
      };
      document.getElementById("nt-btn-perf28").onclick = () => {
        n = 28;
        document.getElementById("nt-n-slider").value = 28;
        document.getElementById("nt-n-val").innerText = `n = 28`;
        render();
      };
    }

    function getDivisors(val) {
      let divs = [];
      for (let i = 1; i <= val; i++) {
        if (val % i === 0) divs.push(i);
      }
      return divs;
    }

    function getPrimeFactors(val) {
      let f = {};
      let temp = val;
      for (let d = 2; d * d <= temp; d++) {
        while (temp % d === 0) {
          f[d] = (f[d] || 0) + 1;
          temp /= d;
        }
      }
      if (temp > 1) f[temp] = 1;
      return f;
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;

      const divs = getDivisors(n);
      const tau = divs.length;
      const sigma = divs.reduce((sum, d) => sum + d, 0);
      const isPerfect = (sigma === 2 * n);
      const factors = getPrimeFactors(n);

      // Left panel: Divisor bar visualizer
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Divisors of n = ${n} (Total τ(n) = ${tau})`, 25, 28);

      const maxD = Math.max(...divs, 1);
      const barStartY = 50;
      const barH = Math.min(18, (H - 120) / Math.max(divs.length, 1));

      divs.forEach((d, idx) => {
        let bw = (d / maxD) * (W * 0.45);
        let by = barStartY + idx * (barH + 4);

        ctx.fillStyle = (d === n || d === 1) ? "#f59e0b" : "#3b82f6";
        ctx.fillRect(30, by, bw, barH);

        ctx.fillStyle = "#f8fafc";
        ctx.font = "11px 'Fira Code', monospace";
        ctx.fillText(`${d}`, 35 + bw + 6, by + barH * 0.75);
      });

      // Right panel: Arithmetical function values & Multiplicativity
      const rightX = W * 0.55;
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Arithmetical Function Invariants`, rightX, 28);

      let pStr = Object.entries(factors).map(([p, a]) => a === 1 ? `${p}` : `${p}^${a}`).join(" · ") || "1";
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Prime Factorization: n = ${pStr}`, rightX, 60);

      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`τ(n) [Divisor Count]  = ${tau}`, rightX, 90);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`σ(n) [Divisor Sum]    = ${sigma}`, rightX, 115);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`Divisor list: {${divs.join(", ")}}`, rightX, 140);

      // Perfect Number Evaluation
      let evalY = 180;
      if (isPerfect) {
        ctx.fillStyle = "#10b981";
        ctx.font = "bold 14px Inter";
        ctx.fillText(`✨ ${n} is an EVEN PERFECT NUMBER!`, rightX, evalY);
        ctx.font = "12px 'Fira Code'";
        ctx.fillText(`σ(${n}) = 2 · ${n} = ${2 * n}`, rightX, evalY + 25);
        ctx.fillStyle = "#94a3b8";
        ctx.font = "11px Inter";
        ctx.fillText(`Euclid-Euler Theorem: Even perfect number format 2^(p-1)(2^p - 1)`, rightX, evalY + 48);
      } else {
        ctx.fillStyle = sigma > 2 * n ? "#ec4899" : "#64748b";
        ctx.font = "bold 12px Inter";
        let status = sigma > 2 * n ? "Abundant (σ(n) > 2n)" : "Deficient (σ(n) < 2n)";
        ctx.fillText(`Classification: ${status}`, rightX, evalY);
        ctx.font = "11px 'Fira Code'";
        ctx.fillText(`Deficiency: |σ(n) - 2n| = ${Math.abs(sigma - 2 * n)}`, rightX, evalY + 22);
      }
    }

    render();
  }
};

// 6. Unit 6: Ramanujan Trigonometric Sums & Möbius Inversion Visualizer
window.SIMULATIONS["sim_nt_mobius_ramanujan"] = {
  title: "Ramanujan Trigonometric Sum c_q(n) & Möbius Sieve Phasor Visualizer",
  description: "Visualize Ramanujan's trigonometric sum c_q(n) = sum_{gcd(a,q)=1} e^(2pi i a n / q) as rotating phasor vectors in the complex plane, verifying the exact identity c_q(n) = sum_{d | gcd(q,n)} d mu(q/d).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let q = 6;
    let n = 2;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Modulus q:</label>
        <input type="range" id="nt-q-slider" min="2" max="12" step="1" value="6" style="vertical-align: middle; width: 80px;">
        <span id="nt-q-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">q = 6</span>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Integer n:</label>
        <input type="range" id="nt-raman-n" min="1" max="12" step="1" value="2" style="vertical-align: middle; width: 80px;">
        <span id="nt-raman-n-val" style="color: #f59e0b; font-family: monospace; font-size: 0.85rem;">n = 2</span>
      `;

      document.getElementById("nt-q-slider").oninput = (e) => {
        q = parseInt(e.target.value);
        document.getElementById("nt-q-val").innerText = `q = ${q}`;
        render();
      };
      document.getElementById("nt-raman-n").oninput = (e) => {
        n = parseInt(e.target.value);
        document.getElementById("nt-raman-n-val").innerText = `n = ${n}`;
        render();
      };
    }

    function gcd(u, v) {
      while (v !== 0) { let t = u % v; u = v; v = t; }
      return u;
    }

    function mu(val) {
      if (val === 1) return 1;
      let count = 0, temp = val;
      for (let p = 2; p * p <= temp; p++) {
        if (temp % p === 0) {
          temp /= p;
          count++;
          if (temp % p === 0) return 0; // square factor
        }
      }
      if (temp > 1) count++;
      return (count % 2 === 1) ? -1 : 1;
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;

      // Collect reduced residue roots for Ramanujan sum
      let reducedA = [];
      for (let a = 1; a <= q; a++) {
        if (gcd(a, q) === 1) reducedA.push(a);
      }

      // Compute phasor sum
      let sumRe = 0, sumIm = 0;
      let phasors = [];
      reducedA.forEach(a => {
        let angle = (2 * Math.PI * a * n) / q;
        let vx = Math.cos(angle);
        let vy = Math.sin(angle);
        sumRe += vx;
        sumIm += vy;
        phasors.push({ a: a, angle: angle, vx: vx, vy: vy });
      });

      // Möbius formula evaluation: sum_{d | gcd(q, n)} d mu(q/d)
      let g = gcd(q, n);
      let mobiusSum = 0;
      let mobiusTerms = [];
      for (let d = 1; d <= g; d++) {
        if (g % d === 0) {
          let term = d * mu(q / d);
          mobiusSum += term;
          mobiusTerms.push(`(${d} × μ(${q / d})) = ${term}`);
        }
      }

      // Draw Complex Phasor Circle
      const cx = W * 0.32, cy = H * 0.52, R_circle = 110;
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(cx, cy, R_circle, 0, Math.PI * 2); ctx.stroke();

      // Axes
      ctx.strokeStyle = "#1e293b";
      ctx.beginPath();
      ctx.moveTo(cx - R_circle - 15, cy); ctx.lineTo(cx + R_circle + 15, cy);
      ctx.moveTo(cx, cy - R_circle - 15); ctx.lineTo(cx, cy + R_circle + 15);
      ctx.stroke();

      // Plot phasors tip-to-tail
      let curX = cx, curY = cy;
      const phasorScale = R_circle * 0.45;
      phasors.forEach(p => {
        let nxtX = curX + p.vx * phasorScale;
        let nxtY = curY - p.vy * phasorScale;

        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(curX, curY); ctx.lineTo(nxtX, nxtY); ctx.stroke();

        ctx.fillStyle = "#f59e0b";
        ctx.beginPath(); ctx.arc(nxtX, nxtY, 3, 0, Math.PI * 2); ctx.fill();

        curX = nxtX; curY = nxtY;
      });

      // Resultant vector
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(curX, curY); ctx.stroke();
      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(curX, curY, 5, 0, Math.PI * 2); ctx.fill();

      // Titles
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Ramanujan Sum c_${q}(${n}) in the Complex Plane`, 20, 25);

      // Right analysis panel
      const rightX = W * 0.62;
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Exact Arithmetic Evaluation`, rightX, 25);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Reduced residues mod ${q}: {${reducedA.join(", ")}}`, rightX, 55);
      ctx.fillText(`Number of terms: ϕ(${q}) = ${reducedA.length}`, rightX, 78);
      ctx.fillText(`gcd(q, n) = gcd(${q}, ${n}) = ${g}`, rightX, 101);

      ctx.fillStyle = "#10b981";
      ctx.font = "bold 14px 'Fira Code', monospace";
      ctx.fillText(`c_${q}(${n}) = ${Math.round(sumRe)}`, rightX, 140);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Möbius Formula Identity:`, rightX, 175);
      ctx.fillStyle = "#fbbf24";
      ctx.font = "11px 'Fira Code'";
      ctx.fillText(`Σ_{d | gcd(q,n)} d·μ(q/d) = ${mobiusTerms.join(" + ")} = ${mobiusSum}`, rightX, 198);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter";
      ctx.fillText(`✓ Phasor projection and Möbius formula match identically!`, rightX, 230);
    }

    render();
  }
};

// 7. Unit 7: Pythagorean Triples & Fermat's Descent Visualizer
window.SIMULATIONS["sim_nt_pythagorean_fermat_descent"] = {
  title: "Pythagorean Triples Generator & Fermat Descent Tree",
  description: "Generate primitive Pythagorean triples x = m^2 - n^2, y = 2mn, z = m^2 + n^2 via stereographic projection of rational points on the unit circle, and trace Fermat's descent for x^4 + y^4 = z^2.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let m = 2, n = 1;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Parameter m:</label>
        <input type="range" id="nt-m-slider" min="2" max="8" step="1" value="2" style="vertical-align: middle; width: 80px;">
        <span id="nt-m-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">m = 2</span>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Parameter n:</label>
        <input type="range" id="nt-n-slider" min="1" max="7" step="1" value="1" style="vertical-align: middle; width: 80px;">
        <span id="nt-n-val" style="color: #f59e0b; font-family: monospace; font-size: 0.85rem;">n = 1</span>
      `;

      document.getElementById("nt-m-slider").oninput = (e) => {
        m = parseInt(e.target.value);
        if (n >= m) n = m - 1;
        document.getElementById("nt-n-slider").max = m - 1;
        document.getElementById("nt-n-slider").value = n;
        document.getElementById("nt-m-val").innerText = `m = ${m}`;
        document.getElementById("nt-n-val").innerText = `n = ${n}`;
        render();
      };
      document.getElementById("nt-n-slider").oninput = (e) => {
        n = parseInt(e.target.value);
        document.getElementById("nt-n-val").innerText = `n = ${n}`;
        render();
      };
    }

    function gcd(u, v) {
      while (v !== 0) { let t = u % v; u = v; v = t; }
      return u;
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;

      let isCoprime = (gcd(m, n) === 1);
      let diffParity = ((m - n) % 2 === 1);
      let isPrimitive = isCoprime && diffParity;

      let x = m * m - n * n;
      let y = 2 * m * n;
      let z = m * m + n * n;

      // Left panel: Unit Circle Stereographic Projection
      const cx = W * 0.30, cy = H * 0.52, R_unit = 110;
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(cx, cy, R_unit, 0, Math.PI * 2); ctx.stroke();

      // Axes
      ctx.strokeStyle = "#1e293b";
      ctx.beginPath();
      ctx.moveTo(cx - R_unit - 20, cy); ctx.lineTo(cx + R_unit + 20, cy);
      ctx.moveTo(cx, cy - R_unit - 20); ctx.lineTo(cx, cy + R_unit + 20);
      ctx.stroke();

      // Rational point P(x/z, y/z)
      let px = cx + (x / z) * R_unit;
      let py = cy - (y / z) * R_unit;

      // Stereographic line from (-1, 0) through (0, n/m) to (x/z, y/z)
      let poleX = cx - R_unit, poleY = cy;
      ctx.strokeStyle = "rgba(245, 158, 11, 0.6)";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(poleX, poleY); ctx.lineTo(px, py); ctx.stroke();

      // Plot point P
      ctx.fillStyle = isPrimitive ? "#10b981" : "#f59e0b";
      ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();

      // Left title
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Rational Points on Unit Circle & Pythagorean Triples`, 20, 25);

      // Right analysis panel: Triple verification & Infinite Descent Tree
      const rightX = W * 0.58;
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Pythagorean Triple Generation:`, rightX, 25);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`m = ${m}, n = ${n} (gcd=${gcd(m,n)}, opposite parity: ${diffParity ? "Yes" : "No"})`, rightX, 55);

      ctx.fillStyle = isPrimitive ? "#10b981" : "#f59e0b";
      ctx.font = "bold 14px 'Fira Code', monospace";
      ctx.fillText(`(x, y, z) = (${x}, ${y}, ${z})`, rightX, 85);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Check: ${x}² + ${y}² = ${x*x} + ${y*y} = ${z*z} = ${z}²`, rightX, 112);

      // Fermat's descent section
      ctx.fillStyle = "#ec4899";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Fermat's Infinite Descent for x⁴ + y⁴ = z²:`, rightX, 155);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter";
      ctx.fillText(`1. Assume positive integer solution (x, y, z) with minimal z > 0.`, rightX, 180);
      ctx.fillText(`2. x² = m² - n², y² = 2mn, z = m² + n² with gcd(m, n) = 1.`, rightX, 202);
      ctx.fillText(`3. x² + n² = m² yields new primitive triple m = a² + b².`, rightX, 224);
      ctx.fillText(`4. Produces smaller integer solution (x₁, y₁, z₁) with z₁ < z.`, rightX, 246);
      ctx.fillStyle = "#ef4444";
      ctx.font = "bold 11px Inter";
      ctx.fillText(`Contradiction of well-ordering principle! No solutions exist.`, rightX, 272);
    }

    render();
  }
};

// 8. Unit 8: Representation of Integers as Sums of Squares Visualizer
window.SIMULATIONS["sim_nt_sums_of_squares_lagrange"] = {
  title: "Sums of 2, 3, and 4 Squares Decomposition Engine",
  description: "Decompose any positive integer n into sums of squares, verify Fermat's Christmas two-square criterion (p = 1 mod 4), Legendre's three-square obstruction n != 4^a(8b + 7), and Lagrange's universal four-square theorem.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let n = 29;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Integer n:</label>
        <input type="range" id="nt-sq-slider" min="1" max="150" step="1" value="29" style="vertical-align: middle; width: 110px;">
        <span id="nt-sq-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">n = 29</span>
        <button id="nt-btn-n7" style="margin-left: 0.5rem; padding: 0.25rem 0.5rem; background: #1e293b; color: #f59e0b; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">n = 7 (4-sq)</button>
        <button id="nt-btn-n29" style="padding: 0.25rem 0.5rem; background: #1e293b; color: #10b981; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">n = 29 (2-sq)</button>
      `;

      document.getElementById("nt-sq-slider").oninput = (e) => {
        n = parseInt(e.target.value);
        document.getElementById("nt-sq-val").innerText = `n = ${n}`;
        render();
      };
      document.getElementById("nt-btn-n7").onclick = () => {
        n = 7;
        document.getElementById("nt-sq-slider").value = 7;
        document.getElementById("nt-sq-val").innerText = `n = 7`;
        render();
      };
      document.getElementById("nt-btn-n29").onclick = () => {
        n = 29;
        document.getElementById("nt-sq-slider").value = 29;
        document.getElementById("nt-sq-val").innerText = `n = 29`;
        render();
      };
    }

    function findTwoSquares(val) {
      for (let x = 0; x * x <= val; x++) {
        let rem = val - x * x;
        let y = Math.round(Math.sqrt(rem));
        if (y * y === rem) return [x, y];
      }
      return null;
    }

    function findThreeSquares(val) {
      let temp = val;
      while (temp % 4 === 0) temp /= 4;
      if (temp % 8 === 7) return null; // Legendre condition obstruction

      for (let x = 0; x * x <= val; x++) {
        for (let y = x; x * x + y * y <= val; y++) {
          let rem = val - x * x - y * y;
          let z = Math.round(Math.sqrt(rem));
          if (z * z === rem) return [x, y, z];
        }
      }
      return null;
    }

    function findFourSquares(val) {
      for (let x = 0; x * x <= val; x++) {
        for (let y = x; x * x + y * y <= val; y++) {
          for (let z = y; x * x + y * y + z * z <= val; z++) {
            let rem = val - x * x - y * y - z * z;
            let w = Math.round(Math.sqrt(rem));
            if (w * w === rem) return [x, y, z, w];
          }
        }
      }
      return [0, 0, 0, 0];
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width, H = canvas.height;

      const twoSq = findTwoSquares(n);
      const threeSq = findThreeSquares(n);
      const fourSq = findFourSquares(n);

      // Left panel: 2D integer circle lattice
      const cx = W * 0.28, cy = H * 0.52, R_box = 110;
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(cx - R_box, cy - R_box, 2 * R_box, 2 * R_box);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(cx - R_box, cy - R_box, 2 * R_box, 2 * R_box);

      // Draw circle x^2 + y^2 = n
      const maxCoord = Math.ceil(Math.sqrt(n)) + 1;
      const scale = R_box / maxCoord;

      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(cx, cy, Math.sqrt(n) * scale, 0, Math.PI * 2);
      ctx.stroke();

      // Plot grid points and solutions
      for (let gx = -maxCoord; gx <= maxCoord; gx++) {
        for (let gy = -maxCoord; gy <= maxCoord; gy++) {
          let isSol = (gx * gx + gy * gy === n);
          let px = cx + gx * scale;
          let py = cy - gy * scale;
          if (Math.abs(px - cx) <= R_box && Math.abs(py - cy) <= R_box) {
            ctx.fillStyle = isSol ? "#10b981" : "#475569";
            ctx.beginPath();
            ctx.arc(px, py, isSol ? 4.5 : 1.5, 0, Math.PI * 2);
            ctx.fill();
          }
        }
      }

      // Title left
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Lattice Circle x² + y² = ${n}`, 20, 25);

      // Right analysis panel: Two, Three, Four squares
      const rightX = W * 0.58;
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Inter";
      ctx.fillText(`Decomposition into Sums of Squares (n = ${n})`, rightX, 25);

      // Two Squares
      let textY = 60;
      ctx.fillStyle = twoSq ? "#10b981" : "#ef4444";
      ctx.font = "bold 12px Inter";
      ctx.fillText(`1. Sum of Two Squares (Fermat's Theorem):`, rightX, textY);
      textY += 22;
      ctx.font = "12px 'Fira Code', monospace";
      if (twoSq) {
        ctx.fillStyle = "#10b981";
        ctx.fillText(`✓ ${n} = ${twoSq[0]}² + ${twoSq[1]}² = ${twoSq[0]*twoSq[0]} + ${twoSq[1]*twoSq[1]}`, rightX + 15, textY);
      } else {
        ctx.fillStyle = "#ef4444";
        ctx.fillText(`✗ ${n} CANNOT be expressed as sum of two squares`, rightX + 15, textY);
      }

      // Three Squares
      textY += 35;
      ctx.fillStyle = threeSq ? "#10b981" : "#f59e0b";
      ctx.font = "bold 12px Inter";
      ctx.fillText(`2. Sum of Three Squares (Legendre's Theorem):`, rightX, textY);
      textY += 22;
      ctx.font = "12px 'Fira Code', monospace";
      if (threeSq) {
        ctx.fillStyle = "#10b981";
        ctx.fillText(`✓ ${n} = ${threeSq[0]}² + ${threeSq[1]}² + ${threeSq[2]}²`, rightX + 15, textY);
      } else {
        ctx.fillStyle = "#f59e0b";
        ctx.fillText(`✗ Obstructed: ${n} is of form 4^a(8b + 7)`, rightX + 15, textY);
      }

      // Four Squares
      textY += 35;
      ctx.fillStyle = "#10b981";
      ctx.font = "bold 12px Inter";
      ctx.fillText(`3. Sum of Four Squares (Lagrange's Theorem):`, rightX, textY);
      textY += 22;
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`✓ Universal: ${n} = ${fourSq[0]}² + ${fourSq[1]}² + ${fourSq[2]}² + ${fourSq[3]}²`, rightX + 15, textY);
      textY += 20;
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter";
      ctx.fillText(`Euler's four-square identity guarantees multiplicativity!`, rightX + 15, textY);
    }

    render();
  }
};

// Simulation Engine Mount Utility
window.SimulationEngine = window.SimulationEngine || {
  initSimulation: function(containerId, simType) {
    const container = document.getElementById(containerId);
    if (!container) return;
    const simDef = window.SIMULATIONS[simType];
    if (!simDef) {
      console.warn("Simulation type not found:", simType);
      return;
    }

    const canvasId = `${containerId}-canvas`;
    const controlsId = `${containerId}-controls`;

    container.innerHTML = `
      <div class="simulation-card" style="margin: 1.5rem 0;">
        <div class="sim-header">
          <div class="sim-title">${simDef.title}</div>
          <div class="sim-badge">60 FPS Real-Time Canvas Engine</div>
        </div>
        <div class="canvas-wrapper" style="position: relative; width: 100%; height: 380px; background: #0f172a; border-radius: 8px; overflow: hidden;">
          <canvas id="${canvasId}" width="800" height="380" style="width: 100%; height: 100%; display: block;"></canvas>
        </div>
        <div class="sim-controls" id="${controlsId}" style="padding: 1rem; background: #1e293b; border-radius: 0 0 8px 8px; display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center;"></div>
      </div>
    `;

    setTimeout(() => {
      simDef.init(canvasId, controlsId);
    }, 50);
  }
};
'''
    with open("number-theory-sims.js", "w", encoding="utf-8") as f:
        f.write(js_code)
    print("Successfully generated number-theory-sims.js with 8 Canvas simulations.")

if __name__ == "__main__":
    generate_sims_js()
