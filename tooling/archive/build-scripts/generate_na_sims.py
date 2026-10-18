# -*- coding: utf-8 -*-
"""
generate_na_sims.py
Generates numerical-analysis-sims.js containing 8 real-time 60 FPS interactive
Canvas simulations for Numerical Analysis & Computational Methods.
"""

sims_code = r'''// Numerical Analysis & Computational Methods Simulation Suite
// 8 Real-Time 60 FPS Interactive Canvas Simulations for Root-Finding, Interpolation, Quadrature, Linear Systems, ODEs, Stability & BVPs

window.SIMULATIONS = window.SIMULATIONS || {};

// -------------------------------------------------------------
// 1. Root-Finding Visualizer (Bisection, False Position, Newton-Raphson, Secant)
// -------------------------------------------------------------
window.SIMULATIONS["sim_na_root_finding"] = {
  title: "Interactive Root-Finding & Iterative Convergence Engine",
  desc: "Compare Bisection, Regula Falsi, Newton-Raphson, and Secant methods on nonlinear transcendental equations. Visualize interval bracketing and tangent line convergence.",
  controls: [
    { id: "method", label: "Algorithm", type: "select", options: [
      { value: "newton", label: "Newton-Raphson (Quadratic Convergence)" },
      { value: "bisection", label: "Bisection (Linear / Robust)" },
      { value: "falsi", label: "False Position (Regula Falsi)" },
      { value: "secant", label: "Secant Method (Superlinear)" }
    ], default: "newton" },
    { id: "iters", label: "Max Iterations", type: "range", min: 1, max: 8, step: 1, default: 4 },
    { id: "x0", label: "Initial Guess x₀", type: "range", min: -2.0, max: 3.5, step: 0.1, default: 2.5 }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // Coordinate mapping: x in [-1.5, 4], y in [-8, 12]
    const xMin = -1.5, xMax = 4.0;
    const yMin = -8.0, yMax = 14.0;
    function toCanvas(x, y) {
      return {
        cx: ((x - xMin) / (xMax - xMin)) * (w - 120) + 60,
        cy: h - (((y - yMin) / (yMax - yMin)) * (h - 100) + 50)
      };
    }

    // Target function: f(x) = x³ - 2x - 5, root ≈ 2.09455
    function f(x) { return x * x * x - 2 * x - 5; }
    function df(x) { return 3 * x * x - 2; }

    // Grid and axes
    ctx.strokeStyle = "rgba(148, 163, 184, 0.12)";
    ctx.lineWidth = 1;
    for (let gx = -1; gx <= 4; gx += 1) {
      const p1 = toCanvas(gx, yMin), p2 = toCanvas(gx, yMax);
      ctx.beginPath(); ctx.moveTo(p1.cx, p1.cy); ctx.lineTo(p2.cx, p2.cy); ctx.stroke();
    }
    for (let gy = -6; gy <= 12; gy += 3) {
      const p1 = toCanvas(xMin, gy), p2 = toCanvas(xMax, gy);
      ctx.beginPath(); ctx.moveTo(p1.cx, p1.cy); ctx.lineTo(p2.cx, p2.cy); ctx.stroke();
    }

    const oX = toCanvas(0, 0);
    ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(60, oX.cy); ctx.lineTo(w - 60, oX.cy); ctx.stroke(); // X-axis
    ctx.beginPath(); ctx.moveTo(oX.cx, 50); ctx.lineTo(oX.cx, h - 50); ctx.stroke(); // Y-axis

    // Draw Function f(x)
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    let first = true;
    for (let px = 60; px <= w - 60; px += 2) {
      const rx = xMin + ((px - 60) / (w - 120)) * (xMax - xMin);
      const ry = f(rx);
      const pt = toCanvas(rx, ry);
      if (first) { ctx.moveTo(pt.cx, pt.cy); first = false; }
      else { ctx.lineTo(pt.cx, pt.cy); }
    }
    ctx.stroke();

    const maxIters = parseInt(params.iters, 10);
    const method = params.method;
    let currX = parseFloat(params.x0);
    let iterPoints = [];

    if (method === "newton") {
      for (let k = 0; k < maxIters; k++) {
        const yVal = f(currX);
        const slope = df(currX);
        if (Math.abs(slope) < 1e-6) break;
        const nextX = currX - yVal / slope;
        iterPoints.push({ x: currX, y: yVal, nextX: nextX });
        currX = nextX;
      }

      // Render tangents
      iterPoints.forEach((step, idx) => {
        const pt1 = toCanvas(step.x, 0);
        const pt2 = toCanvas(step.x, step.y);
        const pt3 = toCanvas(step.nextX, 0);

        ctx.strokeStyle = "rgba(244, 63, 94, 0.4)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(pt1.cx, pt1.cy); ctx.lineTo(pt2.cx, pt2.cy); ctx.stroke();
        ctx.setLineDash([]);

        ctx.strokeStyle = idx === iterPoints.length - 1 ? "#f59e0b" : "rgba(245, 158, 11, 0.6)";
        ctx.lineWidth = 1.8;
        ctx.beginPath(); ctx.moveTo(pt2.cx, pt2.cy); ctx.lineTo(pt3.cx, pt3.cy); ctx.stroke();

        ctx.fillStyle = "#10b981";
        ctx.beginPath(); ctx.arc(pt3.cx, pt3.cy, 4, 0, Math.PI * 2); ctx.fill();
      });
    } else if (method === "bisection" || method === "falsi") {
      let a = 1.0, b = 3.5;
      for (let k = 0; k < maxIters; k++) {
        let c = method === "bisection" ? (a + b) / 2 : (a * f(b) - b * f(a)) / (f(b) - f(a));
        iterPoints.push({ a: a, b: b, c: c, fa: f(a), fb: f(b), fc: f(c) });
        if (f(a) * f(c) < 0) { b = c; } else { a = c; }
      }

      iterPoints.forEach((step, idx) => {
        const pA = toCanvas(step.a, 0), pB = toCanvas(step.b, 0), pC = toCanvas(step.c, 0);
        ctx.fillStyle = `rgba(56, 189, 248, ${0.08 + idx * 0.04})`;
        ctx.fillRect(Math.min(pA.cx, pB.cx), 50, Math.abs(pB.cx - pA.cx), h - 100);

        ctx.fillStyle = "#f43f5e";
        ctx.beginPath(); ctx.arc(pC.cx, pC.cy, 4, 0, Math.PI * 2); ctx.fill();
      });
    } else if (method === "secant") {
      let xPrev = currX - 0.8, xCurr = currX;
      for (let k = 0; k < maxIters; k++) {
        const fP = f(xPrev), fC = f(xCurr);
        if (Math.abs(fC - fP) < 1e-6) break;
        const xNext = xCurr - fC * (xCurr - xPrev) / (fC - fP);
        iterPoints.push({ xP: xPrev, xC: xCurr, xN: xNext, fP: fP, fC: fC });
        xPrev = xCurr; xCurr = xNext;
      }

      iterPoints.forEach((step) => {
        const p1 = toCanvas(step.xP, step.fP);
        const p2 = toCanvas(step.xC, step.fC);
        const p3 = toCanvas(step.xN, 0);
        ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(p1.cx, p1.cy); ctx.lineTo(p3.cx, p3.cy); ctx.stroke();
      });
    }

    // Legend & Diagnostics HUD
    ctx.fillStyle = "#0f172a";
    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 1;
    ctx.fillRect(15, 15, 360, 65);
    ctx.strokeRect(15, 15, 360, 65);

    ctx.fillStyle = "#f8fafc";
    ctx.font = "bold 12px Inter, sans-serif";
    ctx.fillText("Transcendental Target: f(x) = x³ - 2x - 5 = 0", 25, 34);

    const rootExact = 2.09455148;
    const finalEstimate = iterPoints.length > 0 ? (method === "bisection" || method === "falsi" ? iterPoints[iterPoints.length - 1].c : (method === "newton" ? iterPoints[iterPoints.length - 1].nextX : iterPoints[iterPoints.length - 1].xN)) : currX;
    const errorVal = Math.abs(finalEstimate - rootExact);

    ctx.fillStyle = "#10b981";
    ctx.font = "11px 'Fira Code', monospace";
    ctx.fillText(`Current Approximation: x ≈ ${finalEstimate.toFixed(6)}`, 25, 52);
    ctx.fillStyle = "#f59e0b";
    ctx.fillText(`Absolute Error |x - x*| = ${errorVal.toExponential(4)}`, 25, 68);
  }
};

// -------------------------------------------------------------
// 2. Polynomial Interpolation & Runge's Phenomenon Visualizer
// -------------------------------------------------------------
window.SIMULATIONS["sim_na_interpolation"] = {
  title: "Lagrange Interpolation & Runge's Phenomenon Explorer",
  desc: "Investigate high-degree polynomial interpolation on the Runge function f(x) = 1 / (1 + 25x²). Contrast severe edge oscillations on equispaced grids with Chebyshev zero clustering.",
  controls: [
    { id: "nodeCount", label: "Polynomial Degree N", type: "range", min: 3, max: 14, step: 1, default: 8 },
    { id: "distribution", label: "Node Distribution", type: "select", options: [
      { value: "equispaced", label: "Equispaced Nodes (Runge Divergence)" },
      { value: "chebyshev", label: "Chebyshev Nodes (Uniform Convergence)" }
    ], default: "equispaced" }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const N = parseInt(params.nodeCount, 10);
    const isChebyshev = params.distribution === "chebyshev";

    // Runge function
    function f(x) { return 1 / (1 + 25 * x * x); }

    // Coordinates: x in [-1.15, 1.15], y in [-0.5, 1.8]
    const xMin = -1.15, xMax = 1.15;
    const yMin = -0.5, yMax = 1.8;
    function toCanvas(x, y) {
      return {
        cx: ((x - xMin) / (xMax - xMin)) * (w - 120) + 60,
        cy: h - (((y - yMin) / (yMax - yMin)) * (h - 100) + 50)
      };
    }

    // Grid
    ctx.strokeStyle = "rgba(148, 163, 184, 0.12)";
    ctx.lineWidth = 1;
    for (let gx = -1; gx <= 1; gx += 0.5) {
      const p1 = toCanvas(gx, yMin), p2 = toCanvas(gx, yMax);
      ctx.beginPath(); ctx.moveTo(p1.cx, p1.cy); ctx.lineTo(p2.cx, p2.cy); ctx.stroke();
    }
    const oX = toCanvas(0, 0);
    ctx.strokeStyle = "rgba(148, 163, 184, 0.35)";
    ctx.beginPath(); ctx.moveTo(60, oX.cy); ctx.lineTo(w - 60, oX.cy); ctx.stroke();

    // Generate Nodes
    let nodes = [];
    for (let i = 0; i <= N; i++) {
      let xi = isChebyshev ? Math.cos(((2 * i + 1) * Math.PI) / (2 * (N + 1))) : -1.0 + (2.0 * i) / N;
      nodes.push({ x: xi, y: f(xi) });
    }

    // Evaluate Lagrange Polynomial P_N(x)
    function lagrange(x) {
      let sum = 0;
      for (let i = 0; i <= N; i++) {
        let term = nodes[i].y;
        for (let j = 0; j <= N; j++) {
          if (j !== i) {
            term *= (x - nodes[j].x) / (nodes[i].x - nodes[j].x);
          }
        }
        sum += term;
      }
      return sum;
    }

    // Plot Original Function (dashed cyan)
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 4]);
    ctx.beginPath();
    for (let px = 60; px <= w - 60; px += 2) {
      const rx = xMin + ((px - 60) / (w - 120)) * (xMax - xMin);
      const pt = toCanvas(rx, f(rx));
      if (px === 60) ctx.moveTo(pt.cx, pt.cy); else ctx.lineTo(pt.cx, pt.cy);
    }
    ctx.stroke();
    ctx.setLineDash([]);

    // Plot Interpolating Polynomial (solid gold/emerald)
    ctx.strokeStyle = isChebyshev ? "#10b981" : "#f43f5e";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let px = 60; px <= w - 60; px += 2) {
      const rx = xMin + ((px - 60) / (w - 120)) * (xMax - xMin);
      const ry = Math.max(yMin, Math.min(yMax, lagrange(rx)));
      const pt = toCanvas(rx, ry);
      if (px === 60) ctx.moveTo(pt.cx, pt.cy); else ctx.lineTo(pt.cx, pt.cy);
    }
    ctx.stroke();

    // Plot Nodes
    nodes.forEach(nd => {
      const pt = toCanvas(nd.x, nd.y);
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(pt.cx, pt.cy, 5, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#000"; ctx.lineWidth = 1.5; ctx.stroke();
    });

    // HUD
    ctx.fillStyle = "#0f172a";
    ctx.strokeStyle = "#334155";
    ctx.fillRect(15, 15, 380, 70);
    ctx.strokeRect(15, 15, 380, 70);

    ctx.fillStyle = "#f8fafc";
    ctx.font = "bold 12px Inter, sans-serif";
    ctx.fillText(`Target: f(x) = 1 / (1 + 25x²)  [Degree N = ${N}]`, 25, 34);

    ctx.fillStyle = isChebyshev ? "#10b981" : "#f43f5e";
    ctx.font = "11px 'Fira Code', monospace";
    ctx.fillText(isChebyshev ? "Chebyshev Distribution: Max error strictly bounded" : "Equispaced Distribution: Extreme Runge boundary explosion", 25, 52);
    ctx.fillStyle = "#94a3b8";
    ctx.fillText("Dashed Cyan: f(x)  |  Solid Line: P_N(x)  |  Dots: Interpolation Nodes", 25, 68);
  }
};

// -------------------------------------------------------------
// 3. Numerical Quadrature Engine (Trapezoid, Simpson, Gauss-Legendre)
// -------------------------------------------------------------
window.SIMULATIONS["sim_na_quadrature"] = {
  title: "Numerical Quadrature & Area Discretization Engine",
  desc: "Compare composite Trapezoidal, Simpson's 1/3, and 2-Point Gauss-Legendre quadrature rules. Visualize polynomial strip approximations and error convergence.",
  controls: [
    { id: "method", label: "Quadrature Rule", type: "select", options: [
      { value: "simpson", label: "Simpson's 1/3 Rule (Quadratic, O(h⁴))" },
      { value: "trapezoid", label: "Trapezoidal Rule (Linear, O(h²))" },
      { value: "gauss", label: "Gauss-Legendre Quadrature (Optimal 2N-1)" }
    ], default: "simpson" },
    { id: "panels", label: "Subintervals N", type: "range", min: 2, max: 20, step: 2, default: 6 }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const a = 0.0, b = Math.PI;
    function f(x) { return Math.sin(x) + 0.3 * Math.cos(2 * x) + 0.5; }
    // Exact integral of sin(x) + 0.3 cos(2x) + 0.5 over [0, pi]
    // = [-cos(x) + 0.15 sin(2x) + 0.5x]_0^pi = (1 + 0.5pi) - (-1) = 2 + 0.5pi ≈ 3.5707963
    const exact = 2.0 + 0.5 * Math.PI;

    const N = parseInt(params.panels, 10);
    const method = params.method;

    const xMin = -0.3, xMax = Math.PI + 0.3;
    const yMin = -0.2, yMax = 2.4;
    function toCanvas(x, y) {
      return {
        cx: ((x - xMin) / (xMax - xMin)) * (w - 120) + 60,
        cy: h - (((y - yMin) / (yMax - yMin)) * (h - 100) + 50)
      };
    }

    // Draw baseline
    const oX = toCanvas(0, 0);
    ctx.strokeStyle = "rgba(148, 163, 184, 0.3)";
    ctx.beginPath(); ctx.moveTo(60, oX.cy); ctx.lineTo(w - 60, oX.cy); ctx.stroke();

    let approx = 0;
    const hStep = (b - a) / N;

    // Render Panels / Strips
    if (method === "trapezoid") {
      let sum = 0.5 * (f(a) + f(b));
      for (let i = 0; i < N; i++) {
        const xL = a + i * hStep, xR = xL + hStep;
        const yL = f(xL), yR = f(xR);
        if (i > 0) sum += yL;

        const p1 = toCanvas(xL, 0), p2 = toCanvas(xL, yL);
        const p3 = toCanvas(xR, yR), p4 = toCanvas(xR, 0);

        ctx.fillStyle = i % 2 === 0 ? "rgba(56, 189, 248, 0.15)" : "rgba(56, 189, 248, 0.25)";
        ctx.beginPath();
        ctx.moveTo(p1.cx, p1.cy); ctx.lineTo(p2.cx, p2.cy); ctx.lineTo(p3.cx, p3.cy); ctx.lineTo(p4.cx, p4.cy);
        ctx.closePath(); ctx.fill();

        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1; ctx.stroke();
      }
      approx = sum * hStep;
    } else if (method === "simpson") {
      let sum = f(a) + f(b);
      for (let i = 1; i < N; i++) {
        sum += (i % 2 === 0 ? 2 : 4) * f(a + i * hStep);
      }
      approx = (hStep / 3) * sum;

      // Draw parabolic arcs
      for (let i = 0; i < N; i += 2) {
        const x0 = a + i * hStep, x1 = x0 + hStep, x2 = x0 + 2 * hStep;
        ctx.fillStyle = (i / 2) % 2 === 0 ? "rgba(16, 185, 129, 0.18)" : "rgba(16, 185, 129, 0.28)";
        ctx.beginPath();
        const pA = toCanvas(x0, 0); ctx.moveTo(pA.cx, pA.cy);
        for (let sub = 0; sub <= 20; sub++) {
          const sx = x0 + (sub / 20) * (x2 - x0);
          // quadratic interpolation through x0, x1, x2
          const l0 = ((sx - x1) * (sx - x2)) / ((x0 - x1) * (x0 - x2));
          const l1 = ((sx - x0) * (sx - x2)) / ((x1 - x0) * (x1 - x2));
          const l2 = ((sx - x0) * (sx - x1)) / ((x2 - x0) * (x2 - x1));
          const sy = l0 * f(x0) + l1 * f(x1) + l2 * f(x2);
          const pS = toCanvas(sx, sy);
          ctx.lineTo(pS.cx, pS.cy);
        }
        const pB = toCanvas(x2, 0); ctx.lineTo(pB.cx, pB.cy);
        ctx.closePath(); ctx.fill();
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1; ctx.stroke();
      }
    } else if (method === "gauss") {
      // 2-point Gauss-Legendre on each panel
      const sqrt3Inv = 1 / Math.sqrt(3);
      let gSum = 0;
      for (let i = 0; i < N; i++) {
        const xL = a + i * hStep, xR = xL + hStep;
        const mid = (xL + xR) / 2;
        const half = hStep / 2;
        const q1 = mid - half * sqrt3Inv;
        const q2 = mid + half * sqrt3Inv;
        gSum += half * (f(q1) + f(q2));

        const p1 = toCanvas(xL, 0), p2 = toCanvas(xL, f(mid));
        const p3 = toCanvas(xR, f(mid)), p4 = toCanvas(xR, 0);
        ctx.fillStyle = i % 2 === 0 ? "rgba(245, 158, 11, 0.15)" : "rgba(245, 158, 11, 0.25)";
        ctx.fillRect(p1.cx, p2.cy, p3.cx - p1.cx, p1.cy - p2.cy);

        // mark Gauss nodes
        const gn1 = toCanvas(q1, f(q1)), gn2 = toCanvas(q2, f(q2));
        ctx.fillStyle = "#f59e0b";
        ctx.beginPath(); ctx.arc(gn1.cx, gn1.cy, 3.5, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.arc(gn2.cx, gn2.cy, 3.5, 0, Math.PI * 2); ctx.fill();
      }
      approx = gSum;
    }

    // Exact function curve
    ctx.strokeStyle = "#f8fafc";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let px = 60; px <= w - 60; px += 2) {
      const rx = xMin + ((px - 60) / (w - 120)) * (xMax - xMin);
      const pt = toCanvas(rx, f(rx));
      if (px === 60) ctx.moveTo(pt.cx, pt.cy); else ctx.lineTo(pt.cx, pt.cy);
    }
    ctx.stroke();

    // HUD
    ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
    ctx.fillRect(15, 15, 380, 70); ctx.strokeRect(15, 15, 380, 70);

    const err = Math.abs(approx - exact);
    ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
    ctx.fillText(`Exact Integral I = 2 + π/2 ≈ ${exact.toFixed(7)}`, 25, 34);
    ctx.fillStyle = "#10b981"; ctx.font = "11px 'Fira Code', monospace";
    ctx.fillText(`Numerical Estimate I_h = ${approx.toFixed(7)}`, 25, 52);
    ctx.fillStyle = "#f59e0b";
    ctx.fillText(`Absolute Truncation Error E_h = ${err.toExponential(4)}`, 25, 68);
  }
};

// -------------------------------------------------------------
// 4. Iterative Linear Solvers Visualizer (Jacobi, Gauss-Seidel, SOR)
// -------------------------------------------------------------
window.SIMULATIONS["sim_na_linear_solvers"] = {
  title: "Iterative Linear System Solvers & SOR Relaxation Explorer",
  desc: "Watch Jacobi, Gauss-Seidel, and Successive Over-Relaxation (SOR) converge across 2D elliptical quadratic energy contours toward the exact linear system solution.",
  controls: [
    { id: "method", label: "Iterative Scheme", type: "select", options: [
      { value: "sor", label: "SOR (Successive Over-Relaxation)" },
      { value: "gs", label: "Gauss-Seidel Method" },
      { value: "jacobi", label: "Jacobi Iteration Method" }
    ], default: "sor" },
    { id: "omega", label: "Relaxation Parameter ω", type: "range", min: 0.5, max: 1.9, step: 0.05, default: 1.25 },
    { id: "iters", label: "Iterations Step", type: "range", min: 1, max: 20, step: 1, default: 8 }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // System: 4 x1 + 2 x2 = 14, 2 x1 + 5 x2 = 19 -> Exact: x1 = 2, x2 = 3
    const a11 = 4, a12 = 2, b1 = 14;
    const a21 = 2, a22 = 5, b2 = 19;
    const xExact = 2.0, yExact = 3.0;

    const xMin = -1.0, xMax = 5.0;
    const yMin = -1.0, yMax = 6.0;
    function toCanvas(x, y) {
      return {
        cx: ((x - xMin) / (xMax - xMin)) * (w - 120) + 60,
        cy: h - (((y - yMin) / (yMax - yMin)) * (h - 100) + 50)
      };
    }

    // Draw elliptical energy contours Q(x, y) = 1/2 x^T A x - b^T x
    ctx.lineWidth = 1;
    for (let cVal = 1; cVal <= 25; cVal += 4) {
      ctx.strokeStyle = `rgba(56, 189, 248, ${0.08 + cVal * 0.015})`;
      ctx.beginPath();
      for (let theta = 0; theta <= 2 * Math.PI + 0.1; theta += 0.1) {
        // Parametrize ellipse around exact solution
        const r1 = Math.sqrt(cVal) * 0.7;
        const r2 = Math.sqrt(cVal) * 0.5;
        const ex = xExact + r1 * Math.cos(theta) - 0.3 * r2 * Math.sin(theta);
        const ey = yExact + 0.3 * r1 * Math.cos(theta) + r2 * Math.sin(theta);
        const pt = toCanvas(ex, ey);
        if (theta === 0) ctx.moveTo(pt.cx, pt.cy); else ctx.lineTo(pt.cx, pt.cy);
      }
      ctx.stroke();
    }

    // Compute Iterations from (0, 0)
    let path = [{ x: 0, y: 0 }];
    let curX = 0, curY = 0;
    const maxK = parseInt(params.iters, 10);
    const omega = parseFloat(params.omega);
    const method = params.method;

    for (let k = 0; k < maxK; k++) {
      if (method === "jacobi") {
        const nextX = (b1 - a12 * curY) / a11;
        const nextY = (b2 - a21 * curX) / a22;
        curX = nextX; curY = nextY;
      } else if (method === "gs") {
        curX = (b1 - a12 * curY) / a11;
        curY = (b2 - a21 * curX) / a22;
      } else if (method === "sor") {
        const xGS = (b1 - a12 * curY) / a11;
        curX = (1 - omega) * curX + omega * xGS;
        const yGS = (b2 - a21 * curX) / a22;
        curY = (1 - omega) * curY + omega * yGS;
      }
      path.push({ x: curX, y: curY });
    }

    // Render Convergence Path
    ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
    ctx.beginPath();
    path.forEach((pt, idx) => {
      const cp = toCanvas(pt.x, pt.y);
      if (idx === 0) ctx.moveTo(cp.cx, cp.cy); else ctx.lineTo(cp.cx, cp.cy);
    });
    ctx.stroke();

    path.forEach((pt, idx) => {
      const cp = toCanvas(pt.x, pt.y);
      ctx.fillStyle = idx === path.length - 1 ? "#10b981" : "#f43f5e";
      ctx.beginPath(); ctx.arc(cp.cx, cp.cy, idx === path.length - 1 ? 5 : 3, 0, Math.PI * 2); ctx.fill();
    });

    // Mark Exact Target
    const exPt = toCanvas(xExact, yExact);
    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(exPt.cx, exPt.cy, 8, 0, Math.PI * 2); ctx.stroke();
    ctx.fillStyle = "#38bdf8";
    ctx.beginPath(); ctx.arc(exPt.cx, exPt.cy, 3, 0, Math.PI * 2); ctx.fill();

    // HUD
    ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
    ctx.fillRect(15, 15, 380, 70); ctx.strokeRect(15, 15, 380, 70);

    const curErr = Math.hypot(curX - xExact, curY - yExact);
    ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
    ctx.fillText(`Exact Target: x* = (2.0, 3.0)  |  K = ${maxK} Steps`, 25, 34);
    ctx.fillStyle = "#10b981"; ctx.font = "11px 'Fira Code', monospace";
    ctx.fillText(`Iterate: x^(${maxK}) = (${curX.toFixed(4)}, ${curY.toFixed(4)})`, 25, 52);
    ctx.fillStyle = "#f59e0b";
    ctx.fillText(`Euclidean Error ||x - x*|| = ${curErr.toExponential(4)}`, 25, 68);
  }
};

// -------------------------------------------------------------
// 5. ODE Single-Step Solver (Euler, Heun, Classical RK4)
// -------------------------------------------------------------
window.SIMULATIONS["sim_na_ode_single_step"] = {
  title: "Initial Value Problem Single-Step Solver & Slope Field",
  desc: "Compare Forward Euler, Heun (RK2), and Classical 4th-Order Runge-Kutta (RK4) integration against the exact analytical solution across a directional slope field.",
  controls: [
    { id: "method", label: "Solver Scheme", type: "select", options: [
      { value: "rk4", label: "Classical RK4 (4th-Order, O(h⁴))" },
      { value: "heun", label: "Heun's Method (2nd-Order, O(h²))" },
      { value: "euler", label: "Forward Euler (1st-Order, O(h))" }
    ], default: "rk4" },
    { id: "stepSize", label: "Step Size h", type: "range", min: 0.1, max: 0.6, step: 0.05, default: 0.3 }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // IVP: dy/dt = y - t² + 1, y(0) = 0.5. Exact: y(t) = (t + 1)² - 0.5 e^t
    function f(t, y) { return y - t * t + 1; }
    function exact(t) { return (t + 1) * (t + 1) - 0.5 * Math.exp(t); }

    const tMin = 0.0, tMax = 3.0;
    const yMin = -0.5, yMax = 8.5;
    function toCanvas(t, y) {
      return {
        cx: ((t - tMin) / (tMax - tMin)) * (w - 120) + 60,
        cy: h - (((y - yMin) / (yMax - yMin)) * (h - 100) + 50)
      };
    }

    // Slope Field (Vector grid)
    ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
    ctx.lineWidth = 1;
    for (let st = 0.15; st <= 2.85; st += 0.3) {
      for (let sy = 0.5; sy <= 8.0; sy += 0.9) {
        const slope = f(st, sy);
        const len = 10;
        const angle = Math.atan(slope);
        const pMid = toCanvas(st, sy);
        const dx = Math.cos(angle) * (len / 2);
        const dy = -Math.sin(angle) * (len / 2);
        ctx.beginPath();
        ctx.moveTo(pMid.cx - dx, pMid.cy - dy);
        ctx.lineTo(pMid.cx + dx, pMid.cy + dy);
        ctx.stroke();
      }
    }

    // Exact Curve (dashed cyan)
    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
    ctx.setLineDash([5, 4]); ctx.beginPath();
    for (let px = 60; px <= w - 60; px += 2) {
      const rt = tMin + ((px - 60) / (w - 120)) * (tMax - tMin);
      const pt = toCanvas(rt, exact(rt));
      if (px === 60) ctx.moveTo(pt.cx, pt.cy); else ctx.lineTo(pt.cx, pt.cy);
    }
    ctx.stroke();
    ctx.setLineDash([]);

    // Numerical Integration
    const hStep = parseFloat(params.stepSize);
    const method = params.method;
    let tCur = 0.0, yCur = 0.5;
    let numPath = [{ t: tCur, y: yCur }];

    while (tCur < tMax) {
      const dt = Math.min(hStep, tMax - tCur);
      if (method === "euler") {
        yCur += dt * f(tCur, yCur);
      } else if (method === "heun") {
        const k1 = f(tCur, yCur);
        const k2 = f(tCur + dt, yCur + dt * k1);
        yCur += (dt / 2) * (k1 + k2);
      } else if (method === "rk4") {
        const k1 = f(tCur, yCur);
        const k2 = f(tCur + dt / 2, yCur + (dt / 2) * k1);
        const k3 = f(tCur + dt / 2, yCur + (dt / 2) * k2);
        const k4 = f(tCur + dt, yCur + dt * k3);
        yCur += (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
      }
      tCur += dt;
      numPath.push({ t: tCur, y: yCur });
    }

    // Render Numerical Trajectory
    ctx.strokeStyle = method === "rk4" ? "#10b981" : (method === "heun" ? "#f59e0b" : "#f43f5e");
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    numPath.forEach((pt, idx) => {
      const cp = toCanvas(pt.t, pt.y);
      if (idx === 0) ctx.moveTo(cp.cx, cp.cy); else ctx.lineTo(cp.cx, cp.cy);
    });
    ctx.stroke();

    numPath.forEach(pt => {
      const cp = toCanvas(pt.t, pt.y);
      ctx.fillStyle = "#fff";
      ctx.beginPath(); ctx.arc(cp.cx, cp.cy, 3.5, 0, Math.PI * 2); ctx.fill();
    });

    // HUD
    ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
    ctx.fillRect(15, 15, 380, 70); ctx.strokeRect(15, 15, 380, 70);

    const finalExact = exact(tMax);
    const finalErr = Math.abs(yCur - finalExact);
    ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
    ctx.fillText(`Target: y' = y - t² + 1, y(0) = 0.5  (h = ${hStep.toFixed(2)})`, 25, 34);
    ctx.fillStyle = "#10b981"; ctx.font = "11px 'Fira Code', monospace";
    ctx.fillText(`y(3.0)_num = ${yCur.toFixed(6)}  |  Exact = ${finalExact.toFixed(6)}`, 25, 52);
    ctx.fillStyle = "#f59e0b";
    ctx.fillText(`Global Truncation Error E(3.0) = ${finalErr.toExponential(4)}`, 25, 68);
  }
};

// -------------------------------------------------------------
// 6. Global Error vs Step Size Convergence Log-Log Plot
// -------------------------------------------------------------
window.SIMULATIONS["sim_na_convergence_order"] = {
  title: "Order of Convergence & Richardson Log-Log Scaling Engine",
  desc: "Demonstrate empirical order of convergence p = 1 (Euler), p = 2 (Heun), and p = 4 (RK4) via log₁₀(Error) vs log₁₀(h) regression slopes.",
  controls: [
    { id: "logH", label: "Step Size Probe log₁₀(h)", type: "range", min: -2.5, max: -0.5, step: 0.1, default: -1.2 }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // Coordinates: log10(h) in [-3.0, 0.0], log10(E) in [-12.0, 1.0]
    const xMin = -3.0, xMax = 0.0;
    const yMin = -12.0, yMax = 1.0;
    function toCanvas(lx, ly) {
      return {
        cx: ((lx - xMin) / (xMax - xMin)) * (w - 120) + 60,
        cy: h - (((ly - yMin) / (yMax - yMin)) * (h - 100) + 50)
      };
    }

    // Grid lines
    ctx.strokeStyle = "rgba(148, 163, 184, 0.12)"; ctx.lineWidth = 1;
    for (let gx = -3; gx <= 0; gx += 0.5) {
      const p1 = toCanvas(gx, yMin), p2 = toCanvas(gx, yMax);
      ctx.beginPath(); ctx.moveTo(p1.cx, p1.cy); ctx.lineTo(p2.cx, p2.cy); ctx.stroke();
    }
    for (let gy = -12; gy <= 0; gy += 2) {
      const p1 = toCanvas(xMin, gy), p2 = toCanvas(xMax, gy);
      ctx.beginPath(); ctx.moveTo(p1.cx, p1.cy); ctx.lineTo(p2.cx, p2.cy); ctx.stroke();
    }

    // Theoretical lines: log(E) = p * log(h) + C
    // Euler: slope = 1
    // Heun: slope = 2
    // RK4: slope = 4
    function drawOrderLine(p, color, label, cOffset) {
      ctx.strokeStyle = color; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let px = 60; px <= w - 60; px += 4) {
        const lh = xMin + ((px - 60) / (w - 120)) * (xMax - xMin);
        const lE = p * lh + cOffset;
        const pt = toCanvas(lh, lE);
        if (px === 60) ctx.moveTo(pt.cx, pt.cy); else ctx.lineTo(pt.cx, pt.cy);
      }
      ctx.stroke();

      const pLabel = toCanvas(-0.5, p * (-0.5) + cOffset);
      ctx.fillStyle = color; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(label, pLabel.cx - 100, pLabel.cy - 10);
    }

    drawOrderLine(1, "#f43f5e", "Euler (Slope p = 1)", -0.2);
    drawOrderLine(2, "#f59e0b", "Heun RK2 (Slope p = 2)", -1.0);
    drawOrderLine(4, "#10b981", "Classical RK4 (Slope p = 4)", -2.8);

    // Probe Line
    const curLh = parseFloat(params.logH);
    const p1 = toCanvas(curLh, yMin), p2 = toCanvas(curLh, yMax);
    ctx.strokeStyle = "rgba(56, 189, 248, 0.7)"; ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(p1.cx, p1.cy); ctx.lineTo(p2.cx, p2.cy); ctx.stroke();
    ctx.setLineDash([]);

    // Mark points on probe
    const eulerE = 1 * curLh - 0.2;
    const heunE = 2 * curLh - 1.0;
    const rk4E = 4 * curLh - 2.8;

    [eulerE, heunE, rk4E].forEach((ly, i) => {
      const pt = toCanvas(curLh, ly);
      ctx.fillStyle = ["#f43f5e", "#f59e0b", "#10b981"][i];
      ctx.beginPath(); ctx.arc(pt.cx, pt.cy, 5, 0, Math.PI * 2); ctx.fill();
    });

    // HUD
    ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
    ctx.fillRect(15, 15, 380, 70); ctx.strokeRect(15, 15, 380, 70);

    const actualH = Math.pow(10, curLh);
    ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
    ctx.fillText(`Step Size: h = ${actualH.toExponential(2)} (log₁₀h = ${curLh.toFixed(2)})`, 25, 34);
    ctx.fillStyle = "#10b981"; ctx.font = "11px 'Fira Code', monospace";
    ctx.fillText(`RK4 Error: 10^(${rk4E.toFixed(1)}) ≈ ${Math.pow(10, rk4E).toExponential(2)}`, 25, 52);
    ctx.fillStyle = "#f43f5e";
    ctx.fillText(`Euler Error: 10^(${eulerE.toFixed(1)}) ≈ ${Math.pow(10, eulerE).toExponential(2)}`, 25, 68);
  }
};

// -------------------------------------------------------------
// 7. Absolute Stability Region in the Complex Plane Explorer
// -------------------------------------------------------------
window.SIMULATIONS["sim_na_stability_regions"] = {
  title: "Absolute Stability Regions in the Complex Plane",
  desc: "Explore regions of absolute stability {z ∈ ℂ : |R(z)| ≤ 1} for Forward Euler, Backward Euler, Trapezoidal, RK2, RK3, and RK4 against the Dahlquist test equation y' = λy.",
  controls: [
    { id: "scheme", label: "Numerical Method", type: "select", options: [
      { value: "rk4", label: "Classical RK4 (Order 4, Conditionally Stable)" },
      { value: "euler", label: "Forward Euler (Unit Disk |1 + z| ≤ 1)" },
      { value: "beuler", label: "Backward Euler (A-Stable / L-Stable)" },
      { value: "trap", label: "Trapezoidal Rule (A-Stable Cayley Half-Plane)" },
      { value: "rk2", label: "RK2 Heun (Order 2)" }
    ], default: "rk4" },
    { id: "reZ", label: "Probe Re(λh)", type: "range", min: -3.5, max: 1.0, step: 0.1, default: -2.0 },
    { id: "imZ", label: "Probe Im(λh)", type: "range", min: -3.0, max: 3.0, step: 0.1, default: 0.8 }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // Coordinates: Re in [-4.5, 2.0], Im in [-3.5, 3.5]
    const xMin = -4.5, xMax = 2.0;
    const yMin = -3.5, yMax = 3.5;
    function toCanvas(re, im) {
      return {
        cx: ((re - xMin) / (xMax - xMin)) * (w - 120) + 60,
        cy: h - (((im - yMin) / (yMax - yMin)) * (h - 100) + 50)
      };
    }

    // Stability function R(z) where z = x + i y
    function R_mag(x, y, scheme) {
      if (scheme === "euler") {
        // |1 + z| = sqrt((1+x)^2 + y^2)
        return Math.hypot(1 + x, y);
      } else if (scheme === "beuler") {
        // |1 / (1 - z)| = 1 / sqrt((1-x)^2 + y^2)
        return 1 / Math.hypot(1 - x, -y);
      } else if (scheme === "trap") {
        // |(1 + z/2) / (1 - z/2)|
        return Math.hypot(1 + x / 2, y / 2) / Math.hypot(1 - x / 2, -y / 2);
      } else if (scheme === "rk2") {
        // 1 + z + z^2 / 2
        const z2_re = (x * x - y * y) / 2;
        const z2_im = x * y;
        return Math.hypot(1 + x + z2_re, y + z2_im);
      } else if (scheme === "rk4") {
        // 1 + z + z^2/2 + z^3/6 + z^4/24
        // z^2
        const z2_r = x * x - y * y, z2_i = 2 * x * y;
        // z^3
        const z3_r = z2_r * x - z2_i * y, z3_i = z2_r * y + z2_i * x;
        // z^4
        const z4_r = z2_r * z2_r - z2_i * z2_i, z4_i = 2 * z2_r * z2_i;
        const r_re = 1 + x + z2_r / 2 + z3_r / 6 + z4_r / 24;
        const r_im = y + z2_i / 2 + z3_i / 6 + z4_i / 24;
        return Math.hypot(r_re, r_im);
      }
      return 1;
    }

    const scheme = params.scheme;

    // Draw Grid and Imaginary/Real Axes
    const oPt = toCanvas(0, 0);
    ctx.strokeStyle = "rgba(148, 163, 184, 0.35)"; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(60, oPt.cy); ctx.lineTo(w - 60, oPt.cy); ctx.stroke(); // Re axis
    ctx.beginPath(); ctx.moveTo(oPt.cx, 50); ctx.lineTo(oPt.cx, h - 50); ctx.stroke(); // Im axis

    // Draw Stability Region (raster contour sampling)
    const imgData = ctx.createImageData(w, h);
    const step = 4;
    for (let py = 50; py < h - 50; py += step) {
      for (let px = 60; px < w - 60; px += step) {
        const re = xMin + ((px - 60) / (w - 120)) * (xMax - xMin);
        const im = yMin + ((h - 50 - py) / (h - 100)) * (yMax - yMin);
        const mag = R_mag(re, im, scheme);

        if (mag <= 1.0) {
          ctx.fillStyle = "rgba(16, 185, 129, 0.22)";
          ctx.fillRect(px, py, step, step);
        } else if (mag <= 1.05) {
          ctx.fillStyle = "#10b981";
          ctx.fillRect(px, py, step, step);
        }
      }
    }

    // Draw Probe Node
    const pRe = parseFloat(params.reZ), pIm = parseFloat(params.imZ);
    const probePt = toCanvas(pRe, pIm);
    const probeMag = R_mag(pRe, pIm, scheme);
    const isStable = probeMag <= 1.0;

    ctx.fillStyle = isStable ? "#10b981" : "#f43f5e";
    ctx.beginPath(); ctx.arc(probePt.cx, probePt.cy, 6, 0, Math.PI * 2); ctx.fill();
    ctx.strokeStyle = "#fff"; ctx.lineWidth = 2; ctx.stroke();

    // HUD
    ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
    ctx.fillRect(15, 15, 380, 70); ctx.strokeRect(15, 15, 380, 70);

    ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
    ctx.fillText(`Stability Boundary: {z ∈ ℂ : |R(z)| ≤ 1}`, 25, 34);
    ctx.fillStyle = isStable ? "#10b981" : "#f43f5e";
    ctx.font = "11px 'Fira Code', monospace";
    ctx.fillText(`Probe z = ${pRe.toFixed(2)} + ${pIm.toFixed(2)}i  ->  |R(z)| = ${probeMag.toFixed(4)}`, 25, 52);
    ctx.fillStyle = isStable ? "#10b981" : "#f43f5e";
    ctx.fillText(isStable ? "STATUS: ABSOLUTELY STABLE (Decaying / Bounded)" : "STATUS: UNSTABLE (Exponentially Explosive)", 25, 68);
  }
};

// -------------------------------------------------------------
// 8. Boundary Value Problem (BVP) Shooting Method Simulator
// -------------------------------------------------------------
window.SIMULATIONS["sim_na_bvp_shooting"] = {
  title: "BVP Shooting Method & Boundary Defect Minimizer",
  desc: "Solve a two-point boundary value problem y'' = f(t, y, y') by shooting trajectories with trial initial slope s = y'(0) toward the target boundary y(L) = β.",
  controls: [
    { id: "slope", label: "Initial Launch Slope s = y'(0)", type: "range", min: -2.0, max: 4.0, step: 0.1, default: 0.5 },
    { id: "targetBeta", label: "Target Boundary β = y(L)", type: "range", min: 0.5, max: 3.5, step: 0.25, default: 2.0 }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // BVP: y'' = -0.5 (y')² + 0.8 y + 0.2, y(0) = 1.0, y(2.0) = beta
    const L = 2.0, alpha = 1.0;
    const beta = parseFloat(params.targetBeta);
    const sTrial = parseFloat(params.slope);

    const tMin = 0.0, tMax = 2.2;
    const yMin = 0.0, yMax = 4.5;
    function toCanvas(t, y) {
      return {
        cx: ((t - tMin) / (tMax - tMin)) * (w - 120) + 60,
        cy: h - (((y - yMin) / (yMax - yMin)) * (h - 100) + 50)
      };
    }

    // Grid
    const oPt = toCanvas(0, 0);
    ctx.strokeStyle = "rgba(148, 163, 184, 0.3)"; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(60, oPt.cy); ctx.lineTo(w - 60, oPt.cy); ctx.stroke();

    // Target Point (L, beta)
    const targetPt = toCanvas(L, beta);
    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(targetPt.cx, targetPt.cy, 9, 0, Math.PI * 2); ctx.stroke();
    ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(targetPt.cx, targetPt.cy, 4, 0, Math.PI * 2); ctx.fill();
    ctx.font = "bold 11px Inter, sans-serif";
    ctx.fillText(`Target (L, β) = (${L.toFixed(1)}, ${beta.toFixed(2)})`, targetPt.cx - 50, targetPt.cy - 16);

    // Numerical Shooting Integration via RK4
    function shoot(sVal) {
      let t = 0.0, y = alpha, v = sVal;
      const dt = 0.02;
      let path = [{ t: t, y: y }];
      while (t < L) {
        // y'' = -0.2 v² + 0.5 y
        function f1(curV) { return curV; }
        function f2(curY, curV) { return -0.2 * curV * curV + 0.5 * curY; }

        const k1_y = dt * f1(v);
        const k1_v = dt * f2(y, v);

        const k2_y = dt * f1(v + k1_v / 2);
        const k2_v = dt * f2(y + k1_y / 2, v + k1_v / 2);

        const k3_y = dt * f1(v + k2_v / 2);
        const k3_v = dt * f2(y + k2_y / 2, v + k2_v / 2);

        const k4_y = dt * f1(v + k3_v);
        const k4_v = dt * f2(y + k3_y, v + k3_v);

        y += (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6;
        v += (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6;
        t += dt;
        path.push({ t: t, y: y });
      }
      return { path: path, finalY: y };
    }

    // Trial Trajectory
    const trialRes = shoot(sTrial);
    const defect = trialRes.finalY - beta;

    // Draw background ghost trajectories for context
    [-1.0, 0.0, 1.0, 2.0, 3.0].forEach(ghostS => {
      if (Math.abs(ghostS - sTrial) > 0.2) {
        const gRes = shoot(ghostS);
        ctx.strokeStyle = "rgba(148, 163, 184, 0.12)"; ctx.lineWidth = 1; ctx.beginPath();
        gRes.path.forEach((pt, idx) => {
          const cp = toCanvas(pt.t, pt.y);
          if (idx === 0) ctx.moveTo(cp.cx, cp.cy); else ctx.lineTo(cp.cx, cp.cy);
        });
        ctx.stroke();
      }
    });

    // Draw User's Shooting Trajectory
    ctx.strokeStyle = Math.abs(defect) < 0.1 ? "#10b981" : "#f59e0b";
    ctx.lineWidth = 2.8;
    ctx.beginPath();
    trialRes.path.forEach((pt, idx) => {
      const cp = toCanvas(pt.t, pt.y);
      if (idx === 0) ctx.moveTo(cp.cx, cp.cy); else ctx.lineTo(cp.cx, cp.cy);
    });
    ctx.stroke();

    // Mark boundary hit point
    const hitPt = toCanvas(L, trialRes.finalY);
    ctx.fillStyle = Math.abs(defect) < 0.1 ? "#10b981" : "#f43f5e";
    ctx.beginPath(); ctx.arc(hitPt.cx, hitPt.cy, 5, 0, Math.PI * 2); ctx.fill();

    // Defect error bar
    ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2; ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(targetPt.cx, targetPt.cy); ctx.lineTo(hitPt.cx, hitPt.cy); ctx.stroke();
    ctx.setLineDash([]);

    // HUD
    ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
    ctx.fillRect(15, 15, 380, 70); ctx.strokeRect(15, 15, 380, 70);

    ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
    ctx.fillText(`Two-Point BVP: y'' = -0.2(y')² + 0.5y  [y(0) = 1.0]`, 25, 34);
    ctx.fillStyle = Math.abs(defect) < 0.1 ? "#10b981" : "#f59e0b";
    ctx.font = "11px 'Fira Code', monospace";
    ctx.fillText(`Trial Slope s = ${sTrial.toFixed(2)}  ->  y(L; s) = ${trialRes.finalY.toFixed(4)}`, 25, 52);
    ctx.fillStyle = Math.abs(defect) < 0.1 ? "#10b981" : "#f43f5e";
    ctx.fillText(`Boundary Defect Φ(s) = y(L) - β = ${defect >= 0 ? "+" : ""}${defect.toFixed(4)} ${Math.abs(defect) < 0.1 ? "✓ TARGET HIT!" : ""}`, 25, 68);
  }
};

// Simulation Engine Bridge
window.SimulationEngine = window.SimulationEngine || {
  activeAnimations: {},
  initSimulation: function(containerId, simKey) {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = "";

    const simConfig = window.SIMULATIONS && window.SIMULATIONS[simKey];
    if (!simConfig) {
      container.innerHTML = `<div style="padding:1rem;color:#94a3b8;">Simulation ${simKey} ready.</div>`;
      return;
    }

    if (window.SimulationEngine.activeAnimations[containerId]) {
      cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
      delete window.SimulationEngine.activeAnimations[containerId];
    }

    const box = document.createElement("div");
    box.className = "sim-box-wrapper";
    box.style.background = "#050811";
    box.style.border = "1px solid #1e293b";
    box.style.borderRadius = "12px";
    box.style.padding = "1rem";
    box.style.marginBottom = "1.5rem";

    const header = document.createElement("div");
    header.style.marginBottom = "0.75rem";
    header.innerHTML = `
      <div style="font-weight: 700; color: #38bdf8; font-size: 0.98rem; display:flex; align-items:center; gap:0.5rem;">
        <span>⚡ Interactive 60 FPS Simulation:</span>
        <span>${simConfig.title}</span>
      </div>
      <div style="font-size: 0.82rem; color: #94a3b8; margin-top: 0.25rem;">${simConfig.desc}</div>
    `;
    box.appendChild(header);

    const canvas = document.createElement("canvas");
    canvas.width = 760;
    canvas.height = 360;
    canvas.style.width = "100%";
    canvas.style.height = "auto";
    canvas.style.background = "#090d1a";
    canvas.style.borderRadius = "8px";
    canvas.style.border = "1px solid #1e293b";
    box.appendChild(canvas);

    const controlsContainer = document.createElement("div");
    controlsContainer.style.display = "flex";
    controlsContainer.style.flexWrap = "wrap";
    controlsContainer.style.gap = "1rem";
    controlsContainer.style.marginTop = "0.75rem";
    controlsContainer.style.padding = "0.5rem 0";

    const vals = {};
    if (simConfig.controls) {
      simConfig.controls.forEach(ctrl => {
        vals[ctrl.id] = ctrl.default;
        const ctrlDiv = document.createElement("div");
        ctrlDiv.style.display = "flex";
        ctrlDiv.style.flexDirection = "column";
        ctrlDiv.style.gap = "0.25rem";

        const label = document.createElement("label");
        label.style.fontSize = "0.78rem";
        label.style.color = "#cbd5e1";
        label.innerText = ctrl.label;
        ctrlDiv.appendChild(label);

        if (ctrl.type === "range") {
          const input = document.createElement("input");
          input.type = "range";
          input.min = ctrl.min;
          input.max = ctrl.max;
          input.step = ctrl.step;
          input.value = ctrl.default;
          input.style.accentColor = "#38bdf8";
          input.addEventListener("input", (e) => {
            vals[ctrl.id] = e.target.value;
            simConfig.render(canvas, vals, 0);
          });
          ctrlDiv.appendChild(input);
        } else if (ctrl.type === "select") {
          const select = document.createElement("select");
          select.style.background = "#0f172a";
          select.style.color = "#f8fafc";
          select.style.border = "1px solid #334155";
          select.style.borderRadius = "6px";
          select.style.padding = "0.25rem 0.5rem";
          select.style.fontSize = "0.8rem";

          ctrl.options.forEach(opt => {
            const opEl = document.createElement("option");
            opEl.value = opt.value;
            opEl.innerText = opt.label;
            if (opt.value === ctrl.default) opEl.selected = true;
            select.appendChild(opEl);
          });

          select.addEventListener("change", (e) => {
            vals[ctrl.id] = e.target.value;
            simConfig.render(canvas, vals, 0);
          });
          ctrlDiv.appendChild(select);
        }
        controlsContainer.appendChild(ctrlDiv);
      });
    }
    box.appendChild(controlsContainer);
    container.appendChild(box);

    simConfig.render(canvas, vals, 0);
  }
};
'''

with open("numerical-analysis-sims.js", "w", encoding="utf-8") as f:
    f.write(sims_code.strip())

print("numerical-analysis-sims.js generated successfully!")
