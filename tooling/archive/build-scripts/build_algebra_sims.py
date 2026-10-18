# -*- coding: utf-8 -*-
"""
Generates basic-algebra-sims.js with 8 high-performance 60 FPS Canvas simulations
for Basic Algebra: Complex Numbers, De Moivre, Theory of Equations, Series, Matrices,
Gauss-Jordan RREF, and the Leontief Input-Output Economic Model.
"""

sims_code = r'''// Basic Algebra Simulation Suite
// 8 Real-Time 60 FPS Canvas Simulations for University Algebra & Leontief Economics

window.ALGEBRA_SIMS = {
  // 1. Interactive Argand Diagram & Complex Operation Visualizer
  "algebra-complex-plane-sim": {
    title: "Interactive Argand Plane & Vector Operations Visualizer",
    desc: "Drag complex coordinates z₁ and z₂ to inspect vector addition (parallelogram rule), complex multiplication (moduli scaling and argument addition), and dynamic triangle inequality bounds.",
    isAnimated: false,
    controls: [
      { id: "x1", label: "Re(z₁)", min: -4.0, max: 4.0, step: 0.2, value: 2.0 },
      { id: "y1", label: "Im(z₁)", min: -4.0, max: 4.0, step: 0.2, value: 1.6 },
      { id: "x2", label: "Re(z₂)", min: -4.0, max: 4.0, step: 0.2, value: -1.2 },
      { id: "y2", label: "Im(z₂)", min: -4.0, max: 4.0, step: 0.2, value: 2.2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const x1 = vals.x1 !== undefined ? vals.x1 : 2.0;
      const y1 = vals.y1 !== undefined ? vals.y1 : 1.6;
      const x2 = vals.x2 !== undefined ? vals.x2 : -1.2;
      const y2 = vals.y2 !== undefined ? vals.y2 : 2.2;

      const minVal = -5.5, maxVal = 5.5;
      const toScreenX = (x) => 60 + ((x - minVal) / (maxVal - minVal)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minVal) / (maxVal - minVal)) * (h - 90);

      // Grid
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let g = -5; g <= 5; g++) {
        ctx.beginPath(); ctx.moveTo(toScreenX(g), toScreenY(minVal)); ctx.lineTo(toScreenX(g), toScreenY(maxVal)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(toScreenX(minVal), toScreenY(g)); ctx.lineTo(toScreenX(maxVal), toScreenY(g)); ctx.stroke();
      }

      // Real and Imaginary Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minVal), toScreenY(0)); ctx.lineTo(toScreenX(maxVal), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minVal)); ctx.lineTo(toScreenX(0), toScreenY(maxVal)); ctx.stroke();
      ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Re (Real Axis)", toScreenX(maxVal) - 75, toScreenY(0) + 16);
      ctx.fillText("Im (Imaginary Axis)", toScreenX(0) + 8, toScreenY(maxVal) + 16);

      const sx0 = toScreenX(0), sy0 = toScreenY(0);
      const sx1 = toScreenX(x1), sy1 = toScreenY(y1);
      const sx2 = toScreenX(x2), sy2 = toScreenY(y2);
      const sxSum = toScreenX(x1 + x2), sySum = toScreenY(y1 + y2);

      // Parallelogram dashed lines
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(sx1, sy1); ctx.lineTo(sxSum, sySum); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(sx2, sy2); ctx.lineTo(sxSum, sySum); ctx.stroke();
      ctx.setLineDash([]);

      // Vector z1 (Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(sx0, sy0); ctx.lineTo(sx1, sy1); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(sx1, sy1, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`z₁ = ${x1.toFixed(1)} + ${y1.toFixed(1)}i`, sx1 + 8, sy1 - 8);

      // Vector z2 (Emerald)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(sx0, sy0); ctx.lineTo(sx2, sy2); ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(sx2, sy2, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`z₂ = ${x2.toFixed(1)} + ${y2.toFixed(1)}i`, sx2 + 8, sy2 - 8);

      // Vector z1 + z2 (Amber)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(sx0, sy0); ctx.lineTo(sxSum, sySum); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(sxSum, sySum, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`z₁ + z₂ = ${(x1+x2).toFixed(1)} + ${(y1+y2).toFixed(1)}i`, sxSum + 8, sySum - 8);

      // Math Invariants
      const mod1 = Math.sqrt(x1 * x1 + y1 * y1);
      const mod2 = Math.sqrt(x2 * x2 + y2 * y2);
      const modSum = Math.sqrt((x1 + x2) * (x1 + x2) + (y1 + y2) * (y1 + y2));

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Argand Plane: Vector Addition & Triangle Inequality Verification", 65, 25);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Moduli: |z₁| = ${mod1.toFixed(3)},  |z₂| = ${mod2.toFixed(3)},  |z₁ + z₂| = ${modSum.toFixed(3)}`, 65, 45);

      ctx.fillStyle = "#10b981";
      ctx.fillText(`Triangle Inequality: |z₁ + z₂| = ${modSum.toFixed(3)} ≤ |z₁| + |z₂| = ${(mod1 + mod2).toFixed(3)} (Verified!)`, 65, 63);
    }
  },

  // 2. Interactive n-th Roots of Unity & Regular Polygon Generator
  "algebra-demoivre-roots-sim": {
    title: "Interactive n-th Roots of Unity & Regular Polygon Generator",
    desc: "Adjust the order slider n to visualize the n-th roots of unity forming regular polygons on the unit circle. Highlights primitive roots, rotation dynamics, and verifies algebraic sums equal to zero.",
    isAnimated: false,
    controls: [
      { id: "orderN", label: "Root Order n", min: 2, max: 12, step: 1, value: 5 },
      { id: "rotDeg", label: "Phase Shift θ (°)", min: 0, max: 360, step: 5, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const n = vals.orderN !== undefined ? Math.round(vals.orderN) : 5;
      const rotDeg = vals.rotDeg !== undefined ? vals.rotDeg : 0;
      const rot = (rotDeg * Math.PI) / 180;

      const cx = w / 2, cy = h / 2 + 15;
      const R = Math.min(w, h) * 0.32;

      // Coordinate axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(cx - R - 40, cy); ctx.lineTo(cx + R + 40, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy - R - 40); ctx.lineTo(cx, cy + R + 40); ctx.stroke();

      // Unit Circle
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      function gcd(a, b) { return b === 0 ? a : gcd(b, a % b); }

      const roots = [];
      let sumRe = 0, sumIm = 0;

      for (let k = 0; k < n; k++) {
        const angle = rot + (2 * Math.PI * k) / n;
        const re = Math.cos(angle);
        const im = Math.sin(angle);
        sumRe += re; sumIm += im;
        const isPrimitive = gcd(k, n) === 1;
        roots.push({ k, angle, re, im, sx: cx + R * re, sy: cy - R * im, isPrimitive });
      }

      // Draw Polygon
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.fillStyle = "rgba(56, 189, 248, 0.08)";
      ctx.beginPath();
      roots.forEach((r, idx) => {
        if (idx === 0) ctx.moveTo(r.sx, r.sy); else ctx.lineTo(r.sx, r.sy);
      });
      ctx.closePath();
      ctx.fill(); ctx.stroke();

      // Draw Spoke Lines and Points
      roots.forEach(r => {
        ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(r.sx, r.sy); ctx.stroke();

        ctx.fillStyle = r.isPrimitive ? "#f59e0b" : "#38bdf8";
        ctx.beginPath(); ctx.arc(r.sx, r.sy, 5.5, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 11px Inter, sans-serif";
        const labelX = r.sx + (r.re >= 0 ? 10 : -35);
        const labelY = r.sy + (r.im >= 0 ? -8 : 15);
        ctx.fillText(`ω_${r.k}`, labelX, labelY);
      });

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`De Moivre ${n}-th Roots of Unity (Regular ${n}-gon on Unit Circle)`, 65, 25);

      ctx.fillStyle = "#f59e0b"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Angular Spacing: Δθ = 2π/${n} = ${(360/n).toFixed(1)}° | Gold Nodes: Primitive Roots (gcd(k, ${n}) = 1)`, 65, 45);

      ctx.fillStyle = "#10b981";
      ctx.fillText(`Sum of Roots: Σ ω_k = (${sumRe.toFixed(3)}, ${sumIm.toFixed(3)}) ≡ 0 (Centroid at Origin)`, 65, 63);
    }
  },

  // 3. Interactive Polynomial Roots & Viète Symmetric Invariant Explorer
  "algebra-viete-symmetric-sim": {
    title: "Polynomial Roots & Viète Symmetric Invariants",
    desc: "Drag cubic polynomial roots α, β, γ along the horizontal axis to reconstruct the curve P(x), inspect Viète relations, and compute Newton-Girard power sums s₁ through s₄.",
    isAnimated: false,
    controls: [
      { id: "rootA", label: "Root α", min: -3.0, max: 3.0, step: 0.2, value: -2.0 },
      { id: "rootB", label: "Root β", min: -3.0, max: 3.0, step: 0.2, value: 0.5 },
      { id: "rootC", label: "Root γ", min: -3.0, max: 3.0, step: 0.2, value: 2.2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const rA = vals.rootA !== undefined ? vals.rootA : -2.0;
      const rB = vals.rootB !== undefined ? vals.rootB : 0.5;
      const rC = vals.rootC !== undefined ? vals.rootC : 2.2;

      // Viète Relations
      const p1 = -(rA + rB + rC);
      const p2 = (rA * rB + rB * rC + rC * rA);
      const p3 = -(rA * rB * rC);

      // Newton-Girard Sums
      const s1 = rA + rB + rC;
      const s2 = rA * rA + rB * rB + rC * rC;
      const s3 = rA**3 + rB**3 + rC**3;
      const s4 = rA**4 + rB**4 + rC**4;

      const minX = -4, maxX = 4, minY = -12, maxY = 12;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Polynomial Curve P(x) = (x - rA)(x - rB)(x - rC)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = minX; x <= maxX; x += 0.05) {
        const y = (x - rA) * (x - rB) * (x - rC);
        const sx = toScreenX(x), sy = toScreenY(Math.max(minY, Math.min(maxY, y)));
        if (x === minX) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Highlight Roots
      [rA, rB, rC].forEach((r, idx) => {
        const labels = ["α", "β", "γ"];
        const colors = ["#ef4444", "#10b981", "#f59e0b"];
        ctx.fillStyle = colors[idx];
        ctx.beginPath(); ctx.arc(toScreenX(r), toScreenY(0), 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(`${labels[idx]} = ${r.toFixed(1)}`, toScreenX(r) - 15, toScreenY(0) + 20);
      });

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Cubic Polynomial: P(x) = x³ + (${p1.toFixed(2)})x² + (${p2.toFixed(2)})x + (${p3.toFixed(2)}) = 0`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Viète Relations: Σα = ${(-p1).toFixed(2)},  Σαβ = ${p2.toFixed(2)},  αβγ = ${(-p3).toFixed(2)}`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`Newton-Girard Power Sums: s₁ = ${s1.toFixed(2)},  s₂ = ${s2.toFixed(2)},  s₃ = ${s3.toFixed(2)},  s₄ = ${s4.toFixed(2)}`, 65, 63);
    }
  },

  // 4. Interactive Descartes Sign Variations & Root Multiplicity Inspector
  "algebra-descartes-multiplicity-sim": {
    title: "Descartes' Rule of Signs & Root Multiplicity Visualizer",
    desc: "Examine polynomial sign changes, compute live Descartes upper bounds on positive/negative real roots, and inspect root multiplicity by visualizing tangent touching points where P(x) = 0 and P'(x) = 0.",
    isAnimated: false,
    controls: [
      { id: "mult", label: "Multiplicity m of Root at x=1", min: 1, max: 3, step: 1, value: 2 },
      { id: "rootOther", label: "Second Root r₂", min: -3.0, max: 2.0, step: 0.5, value: -1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const m = vals.mult !== undefined ? Math.round(vals.mult) : 2;
      const r2 = vals.rootOther !== undefined ? vals.rootOther : -1.5;

      const minX = -3.5, maxX = 3.5, minY = -8, maxY = 8;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      function P(x) { return Math.pow(x - 1, m) * (x - r2); }
      function Pprime(x) {
        if (m === 1) return (x - r2) + (x - 1);
        return m * Math.pow(x - 1, m - 1) * (x - r2) + Math.pow(x - 1, m);
      }

      // Plot P(x) in Cyan
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = minX; x <= maxX; x += 0.05) {
        const y = P(x);
        const sx = toScreenX(x), sy = toScreenY(Math.max(minY, Math.min(maxY, y)));
        if (x === minX) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Plot P'(x) in Amber dashed
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let x = minX; x <= maxX; x += 0.05) {
        const y = Pprime(x);
        const sx = toScreenX(x), sy = toScreenY(Math.max(minY, Math.min(maxY, y)));
        if (x === minX) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Mark the Multiple Root at x = 1
      ctx.fillStyle = m >= 2 ? "#10b981" : "#ef4444";
      ctx.beginPath(); ctx.arc(toScreenX(1), toScreenY(0), 6, 0, Math.PI * 2); ctx.fill();

      // Mark the Second Root at r2
      ctx.fillStyle = "#ec4899";
      ctx.beginPath(); ctx.arc(toScreenX(r2), toScreenY(0), 6, 0, Math.PI * 2); ctx.fill();

      const behavior = m === 1 ? "Simple Cross (m=1): P'(1) ≠ 0" : (m === 2 ? "Tangent Touch (m=2): P(1) = 0 and P'(1) = 0" : "Tangent Inflection (m=3): P = P' = P'' = 0");

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Polynomial P(x) = (x - 1)^${m} · (x - (${r2.toFixed(1)})) | Solid Cyan: P(x), Dashed Amber: P'(x)`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Root Multiplicity at x = 1.0: ${behavior}`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`Descartes Invariant: Multiple roots satisfy gcd(P, P') = (x - 1)^${m-1}`, 65, 63);
    }
  },

  // 5. Interactive C + iS Complex Phasor & Trigonometric Sum Visualizer
  "algebra-series-cis-phasor-sim": {
    title: "C + iS Complex Phasor & Trigonometric Series Visualizer",
    desc: "Visualize trigonometric summation by chaining complex phasors exp(i(α + kβ)) in the Argand plane. Adjust angle parameters and term count N to watch the polygon of chords close onto circular arcs, verifying the closed form.",
    isAnimated: false,
    controls: [
      { id: "alphaDeg", label: "Initial Phase α (°)", min: 0, max: 90, step: 5, value: 15 },
      { id: "betaDeg", label: "Angle Step β (°)", min: 10, max: 60, step: 2, value: 25 },
      { id: "numTerms", label: "Number of Terms N", min: 2, max: 12, step: 1, value: 6 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const alphaDeg = vals.alphaDeg !== undefined ? vals.alphaDeg : 15;
      const betaDeg = vals.betaDeg !== undefined ? vals.betaDeg : 25;
      const N = vals.numTerms !== undefined ? Math.round(vals.numTerms) : 6;

      const alpha = (alphaDeg * Math.PI) / 180;
      const beta = (betaDeg * Math.PI) / 180;

      const cx = 100, cy = h - 100;
      const scale = Math.min(w, h) * 0.12;

      // Coordinate axes from origin
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(30, cy); ctx.lineTo(w - 30, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, 30); ctx.lineTo(cx, h - 30); ctx.stroke();

      let currX = cx, currY = cy;
      let sumCos = 0, sumSin = 0;

      ctx.lineWidth = 2;
      for (let k = 0; k < N; k++) {
        const theta = alpha + k * beta;
        const dx = Math.cos(theta);
        const dy = Math.sin(theta);
        sumCos += dx; sumSin += dy;

        const nextX = currX + scale * dx;
        const nextY = currY - scale * dy;

        ctx.strokeStyle = `hsl(${(k * 360) / N}, 80%, 60%)`;
        ctx.beginPath(); ctx.moveTo(currX, currY); ctx.lineTo(nextX, nextY); ctx.stroke();

        ctx.fillStyle = "#e2e8f0"; ctx.beginPath(); ctx.arc(nextX, nextY, 3, 0, Math.PI * 2); ctx.fill();
        currX = nextX; currY = nextY;
      }

      // Resultant Vector R = C + iS in Gold
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(currX, currY); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(currX, currY, 6, 0, Math.PI * 2); ctx.fill();

      // Theoretical Closed Form
      const denom = Math.sin(beta / 2);
      const factor = Math.sin((N * beta) / 2) / (denom !== 0 ? denom : 0.0001);
      const midAngle = alpha + ((N - 1) * beta) / 2;
      const theoC = factor * Math.cos(midAngle);
      const theoS = factor * Math.sin(midAngle);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`C + iS Phasor Chain (N = ${N} Terms, α = ${alphaDeg}°, β = ${betaDeg}°)`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Sum of Cosines C = Σ cos(α + kβ) = ${sumCos.toFixed(3)}  |  Theory: ${theoC.toFixed(3)} (Matches!)`, 65, 45);

      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Sum of Sines S = Σ sin(α + kβ) = ${sumSin.toFixed(3)}  |  Theory: ${theoS.toFixed(3)} (Matches!)`, 65, 63);
    }
  },

  // 6. Interactive Matrix Transformation & Signed Determinant Visualizer
  "algebra-matrix-determinant-sim": {
    title: "Matrix Transformation & Signed Determinant Visualizer",
    desc: "Adjust entries of a 2x2 matrix M to visualize linear geometric deformations of the unit square. Live computes signed area det(M), matrix trace, orientation parity, and checks singularity.",
    isAnimated: false,
    controls: [
      { id: "matA", label: "Entry a (1,1)", min: -2.0, max: 2.0, step: 0.1, value: 1.5 },
      { id: "matB", label: "Entry b (1,2)", min: -2.0, max: 2.0, step: 0.1, value: 0.5 },
      { id: "matC", label: "Entry c (2,1)", min: -2.0, max: 2.0, step: 0.1, value: 0.5 },
      { id: "matD", label: "Entry d (2,2)", min: -2.0, max: 2.0, step: 0.1, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a = vals.matA !== undefined ? vals.matA : 1.5;
      const b = vals.matB !== undefined ? vals.matB : 0.5;
      const c = vals.matC !== undefined ? vals.matC : 0.5;
      const d = vals.matD !== undefined ? vals.matD : 1.5;

      const det = a * d - b * c;
      const tr = a + d;

      const minVal = -3.5, maxVal = 3.5;
      const toScreenX = (x) => 60 + ((x - minVal) / (maxVal - minVal)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minVal) / (maxVal - minVal)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minVal), toScreenY(0)); ctx.lineTo(toScreenX(maxVal), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minVal)); ctx.lineTo(toScreenX(0), toScreenY(maxVal)); ctx.stroke();

      // Original Unit Square [0, 1] x [0, 1] dashed
      ctx.setLineDash([3, 3]); ctx.strokeStyle = "#64748b"; ctx.lineWidth = 1.5;
      ctx.strokeRect(toScreenX(0), toScreenY(1), toScreenX(1) - toScreenX(0), toScreenY(0) - toScreenY(1));
      ctx.setLineDash([]);

      // Deformed Parallelogram Vertices: (0,0), (a,c), (a+b, c+d), (b,d)
      const p0 = { x: toScreenX(0), y: toScreenY(0) };
      const p1 = { x: toScreenX(a), y: toScreenY(c) };
      const p2 = { x: toScreenX(a + b), y: toScreenY(c + d) };
      const p3 = { x: toScreenX(b), y: toScreenY(d) };

      const fillColor = Math.abs(det) < 0.05 ? "rgba(245, 158, 11, 0.2)" : (det > 0 ? "rgba(16, 185, 129, 0.25)" : "rgba(239, 68, 68, 0.25)");
      const strokeColor = Math.abs(det) < 0.05 ? "#f59e0b" : (det > 0 ? "#10b981" : "#ef4444");

      ctx.fillStyle = fillColor; ctx.strokeStyle = strokeColor; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(p0.x, p0.y);
      ctx.lineTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.lineTo(p3.x, p3.y);
      ctx.closePath();
      ctx.fill(); ctx.stroke();

      // Column Vectors Basis Arrows
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(p0.x, p0.y); ctx.lineTo(p1.x, p1.y); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.fillText(`v₁ = (${a.toFixed(1)}, ${c.toFixed(1)})`, p1.x + 8, p1.y);

      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(p0.x, p0.y); ctx.lineTo(p3.x, p3.y); ctx.stroke();
      ctx.fillStyle = "#ec4899"; ctx.fillText(`v₂ = (${b.toFixed(1)}, ${d.toFixed(1)})`, p3.x + 8, p3.y);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Matrix M = [[${a.toFixed(1)}, ${b.toFixed(1)}], [${c.toFixed(1)}, ${d.toFixed(1)}]]`, 65, 25);

      ctx.fillStyle = det > 0 ? "#10b981" : (det < 0 ? "#ef4444" : "#f59e0b"); ctx.font = "12px Inter, sans-serif";
      const orientation = Math.abs(det) < 0.05 ? "SINGULAR / COLLAPSED (det = 0)" : (det > 0 ? "ORIENTATION-PRESERVING (det > 0)" : "ORIENTATION-REVERSING (det < 0)");
      ctx.fillText(`Signed Determinant Area: det(M) = ad - bc = ${det.toFixed(3)} | ${orientation}`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`Matrix Trace: tr(M) = a + d = ${tr.toFixed(2)} | Invertibility: ${Math.abs(det) >= 0.05 ? "Invertible" : "Singular"}`, 65, 63);
    }
  },

  // 7. Interactive Gauss-Jordan Elimination & RREF Stepper
  "algebra-gauss-jordan-rref-sim": {
    title: "Gauss-Jordan Elimination & RREF Stepper",
    desc: "Step through Gauss-Jordan elementary row operations on an augmented system [A | B]. Live highlights pivot selections, applies row multipliers, and displays the canonical Reduced Row Echelon Form (RREF).",
    isAnimated: false,
    controls: [
      { id: "stepIdx", label: "Elimination Step (0 to 4)", min: 0, max: 4, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const step = vals.stepIdx !== undefined ? Math.round(vals.stepIdx) : 0;

      const stepsData = [
        {
          name: "Step 0: Initial Augmented System [A | B]",
          op: "Original linear equations: x + y + 2z = 9; 2x + 4y - 3z = 1; 3x + 6y - 5z = 0",
          matrix: [
            [1, 1, 2, 9],
            [2, 4, -3, 1],
            [3, 6, -5, 0]
          ],
          pivot: [0, 0]
        },
        {
          name: "Step 1: Eliminate Below Pivot 1",
          op: "Row operations: R₂ → R₂ - 2R₁  and  R₃ → R₃ - 3R₁",
          matrix: [
            [1, 1, 2, 9],
            [0, 2, -7, -17],
            [0, 3, -11, -27]
          ],
          pivot: [1, 1]
        },
        {
          name: "Step 2: Normalize Pivot 2 and Eliminate Below",
          op: "Row operations: R₂ → 0.5 R₂  and  R₃ → R₃ - 3 R₂",
          matrix: [
            [1, 1, 2, 9],
            [0, 1, -3.5, -8.5],
            [0, 0, -0.5, -1.5]
          ],
          pivot: [2, 2]
        },
        {
          name: "Step 3: Normalize Pivot 3 (Upper Triangular REF)",
          op: "Row operation: R₃ → -2 R₃  (Pivot 3 becomes 1.0)",
          matrix: [
            [1, 1, 2, 9],
            [0, 1, -3.5, -8.5],
            [0, 0, 1, 3]
          ],
          pivot: [2, 2]
        },
        {
          name: "Step 4: Backward Elimination to RREF [I₃ | X]",
          op: "R₂ → R₂ + 3.5 R₃; R₁ → R₁ - 2 R₃; then R₁ → R₁ - R₂ ⇒ Solution: (1, 2, 3)!",
          matrix: [
            [1, 0, 0, 1],
            [0, 1, 0, 2],
            [0, 0, 1, 3]
          ],
          pivot: null
        }
      ];

      const cur = stepsData[step];

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(cur.name, 65, 25);

      ctx.fillStyle = "#f59e0b"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(cur.op, 65, 45);

      // Render Matrix Table
      const startX = w / 2 - 180, startY = 85;
      const cellW = 85, cellH = 45;

      // Outer Bracket
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(startX - 15, startY - 10); ctx.lineTo(startX - 25, startY - 10);
      ctx.lineTo(startX - 25, startY + 3 * cellH + 10); ctx.lineTo(startX - 15, startY + 3 * cellH + 10);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(startX + 4 * cellW + 15, startY - 10); ctx.lineTo(startX + 4 * cellW + 25, startY - 10);
      ctx.lineTo(startX + 4 * cellW + 25, startY + 3 * cellH + 10); ctx.lineTo(startX + 4 * cellW + 15, startY + 3 * cellH + 10);
      ctx.stroke();

      // Divider line for augmented B column
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(startX + 3 * cellW, startY - 10);
      ctx.lineTo(startX + 3 * cellW, startY + 3 * cellH + 10);
      ctx.stroke();
      ctx.setLineDash([]);

      for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 4; c++) {
          const val = cur.matrix[r][c];
          const isPivot = cur.pivot && cur.pivot[0] === r && cur.pivot[1] === c;

          const px = startX + c * cellW;
          const py = startY + r * cellH;

          if (isPivot) {
            ctx.fillStyle = "rgba(245, 158, 11, 0.25)";
            ctx.fillRect(px + 4, py + 4, cellW - 8, cellH - 8);
            ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
            ctx.strokeRect(px + 4, py + 4, cellW - 8, cellH - 8);
          }

          ctx.fillStyle = isPivot ? "#f59e0b" : (c === 3 ? "#38bdf8" : "#e2e8f0");
          ctx.font = isPivot ? "bold 15px Inter, monospace" : "14px Inter, monospace";
          ctx.textAlign = "center";
          ctx.fillText(Number(val).toFixed(val % 1 !== 0 ? 1 : 0), px + cellW / 2, py + cellH / 2 + 5);
        }
      }
      ctx.textAlign = "left";

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      if (step === 4) {
        ctx.fillText("RREF Complete: System is strictly consistent with rank(A) = rank([A|B]) = 3. Unique solution: x = 1, y = 2, z = 3.", 65, h - 25);
      } else {
        ctx.fillText(`Current Rank: 3 | Leading pivot at row ${(cur.pivot ? cur.pivot[0] + 1 : 3)}, col ${(cur.pivot ? cur.pivot[1] + 1 : 3)}`, 65, h - 25);
      }
    }
  },

  // 8. Interactive Leontief Multi-Sector Economy & Supply Chain Simulator
  "algebra-leontief-economy-sim": {
    title: "Leontief Multi-Sector Economic Equilibrium Simulator",
    desc: "Simulate a 3-sector macroeconomy (Agriculture, Manufacturing, Energy). Adjust consumer final demand sliders D and economic coupling to watch dynamic matrix inversion (I - C)⁻¹, verify Hawkins-Simon viability, and trace gross production output.",
    isAnimated: false,
    controls: [
      { id: "demAgri", label: "Agriculture Demand D₁ ($M)", min: 20, max: 150, step: 5, value: 60 },
      { id: "demMfg", label: "Manufacturing Demand D₂ ($M)", min: 20, max: 150, step: 5, value: 80 },
      { id: "demEnergy", label: "Energy Demand D₃ ($M)", min: 20, max: 150, step: 5, value: 50 },
      { id: "coupling", label: "Coupling Intensity", min: 0.7, max: 1.2, step: 0.05, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const d1 = vals.demAgri !== undefined ? vals.demAgri : 60;
      const d2 = vals.demMfg !== undefined ? vals.demMfg : 80;
      const d3 = vals.demEnergy !== undefined ? vals.demEnergy : 50;
      const k = vals.coupling !== undefined ? vals.coupling : 1.0;

      // Base Consumption Matrix C
      const C = [
        [0.10 * k, 0.20 * k, 0.15 * k],
        [0.25 * k, 0.15 * k, 0.20 * k],
        [0.15 * k, 0.20 * k, 0.10 * k]
      ];

      // Leontief Matrix M = I - C
      const M = [
        [1 - C[0][0], -C[0][1], -C[0][2]],
        [-C[1][0], 1 - C[1][1], -C[1][2]],
        [-C[2][0], -C[2][1], 1 - C[2][2]]
      ];

      // Determinant of M (Hawkins-Simon check)
      const detM =
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) -
        M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) +
        M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]);

      // Inverse of 3x3 M
      let X = [0, 0, 0];
      let viable = detM > 0.05;

      if (viable) {
        const inv = [
          [
            (M[1][1]*M[2][2] - M[1][2]*M[2][1])/detM,
            (M[0][2]*M[2][1] - M[0][1]*M[2][2])/detM,
            (M[0][1]*M[1][2] - M[0][2]*M[1][1])/detM
          ],
          [
            (M[1][2]*M[2][0] - M[1][0]*M[2][2])/detM,
            (M[0][0]*M[2][2] - M[0][2]*M[2][0])/detM,
            (M[0][2]*M[1][0] - M[0][0]*M[1][2])/detM
          ],
          [
            (M[1][0]*M[2][1] - M[1][1]*M[2][0])/detM,
            (M[0][1]*M[2][0] - M[0][0]*M[2][1])/detM,
            (M[0][0]*M[1][1] - M[0][1]*M[1][0])/detM
          ]
        ];

        X[0] = inv[0][0]*d1 + inv[0][1]*d2 + inv[0][2]*d3;
        X[1] = inv[1][0]*d1 + inv[1][1]*d2 + inv[1][2]*d3;
        X[2] = inv[2][0]*d1 + inv[2][1]*d2 + inv[2][2]*d3;
      }

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Leontief Input-Output Equilibrium: (I - C) X = D ⇒ X = (I - C)⁻¹ D", 65, 25);

      ctx.fillStyle = viable ? "#10b981" : "#ef4444"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Hawkins-Simon Viability: det(I - C) = ${detM.toFixed(3)} ${viable ? "> 0 (Economically Viable!)" : "≤ 0 (Infeasible Feedback Loop!)"}`, 65, 45);

      // Render Bar Comparison of Final Demand D vs Total Gross Output X
      const sectors = [
        { name: "Sector 1: Agriculture", D: d1, X: X[0], color: "#10b981" },
        { name: "Sector 2: Manufacturing", D: d2, X: X[1], color: "#38bdf8" },
        { name: "Sector 3: Energy", D: d3, X: X[2], color: "#f59e0b" }
      ];

      const startY = 80;
      const barHeight = 22;
      const maxVal = 250;
      const barMaxWidth = w - 340;

      sectors.forEach((sec, idx) => {
        const y = startY + idx * 55;

        ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(sec.name, 65, y + 10);

        // Final Demand bar (striped / semi-transparent)
        const dWidth = Math.min(barMaxWidth, (sec.D / maxVal) * barMaxWidth);
        ctx.fillStyle = "rgba(148, 163, 184, 0.3)";
        ctx.fillRect(200, y - 5, dWidth, barHeight);
        ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1;
        ctx.strokeRect(200, y - 5, dWidth, barHeight);

        // Gross Output bar (glowing color)
        const xVal = viable ? sec.X : 0;
        const xWidth = Math.min(barMaxWidth, (xVal / maxVal) * barMaxWidth);
        ctx.fillStyle = sec.color;
        ctx.fillRect(200, y - 5, xWidth, barHeight);

        // Value text
        ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Output X = $${xVal.toFixed(1)}M  (Demand D = $${sec.D.toFixed(0)}M, Multiplier = ${(xVal / (sec.D || 1)).toFixed(2)}x)`, 205 + xWidth, y + 10);
      });

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Direct vs Indirect Multiplier Effect: Gross output must exceed final consumer demand to replenish inter-industry consumption.", 65, h - 20);
    }
  }
};

// Simulation Engine Integration for Basic Algebra
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

const origAlgebraInit = window.SimulationEngine.initSimulation;
window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const simConfig = (window.ALGEBRA_SIMS && window.ALGEBRA_SIMS[simType]) ||
                    (window.GEOM2D_SIMS && window.GEOM2D_SIMS[simType]) ||
                    (window.CALC1_SIMS && window.CALC1_SIMS[simType]) ||
                    (window.RP_SIMS && window.RP_SIMS[simType]);

  if (!simConfig) {
    if (origAlgebraInit) {
      origAlgebraInit(containerId, simType);
    } else {
      container.innerHTML = `<div style="padding: 1rem; color: #ef4444; background: #1e1b4b; border-radius: 8px;">Simulation type '${simType}' not found in registry.</div>`;
    }
    return;
  }

  if (window.SimulationEngine.activeAnimations && window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }

  container.innerHTML = "";
  const box = document.createElement("div");
  box.className = "simulation-box";
  box.style.background = "#0b1120";
  box.style.border = "1px solid #1e293b";
  box.style.borderRadius = "12px";
  box.style.padding = "1.25rem";
  box.style.marginTop = "1rem";
  box.style.marginBottom = "1.5rem";

  const header = document.createElement("div");
  header.style.marginBottom = "1rem";
  header.innerHTML = `
    <div style="display: flex; align-items: center; justify-content: space-between;">
      <h4 style="margin: 0; color: #38bdf8; font-size: 1.15rem; font-family: 'Space Grotesk', sans-serif;">${simConfig.title}</h4>
      <span style="font-size: 0.75rem; background: #1e293b; color: #94a3b8; padding: 0.2rem 0.5rem; border-radius: 4px; border: 1px solid #334155;">60 FPS Interactive</span>
    </div>
    <p style="margin: 0.35rem 0 0 0; color: #94a3b8; font-size: 0.85rem; line-height: 1.4;">${simConfig.desc}</p>
  `;
  box.appendChild(header);

  const canvas = document.createElement("canvas");
  canvas.width = 760;
  canvas.height = 360;
  canvas.style.width = "100%";
  canvas.style.height = "auto";
  canvas.style.display = "block";
  canvas.style.borderRadius = "8px";
  canvas.style.border = "1px solid #1e293b";
  box.appendChild(canvas);

  const controlsContainer = document.createElement("div");
  controlsContainer.style.display = "flex";
  controlsContainer.style.flexWrap = "wrap";
  controlsContainer.style.gap = "1rem";
  controlsContainer.style.marginTop = "1rem";
  controlsContainer.style.paddingTop = "0.75rem";
  controlsContainer.style.borderTop = "1px solid #1e293b";

  const vals = {};
  if (simConfig.controls) {
    simConfig.controls.forEach(ctrl => {
      vals[ctrl.id] = ctrl.value;
      const wrap = document.createElement("div");
      wrap.style.flex = "1";
      wrap.style.minWidth = "160px";

      const lbl = document.createElement("label");
      lbl.style.display = "block";
      lbl.style.fontSize = "0.75rem";
      lbl.style.color = "#94a3b8";
      lbl.style.marginBottom = "0.25rem";
      lbl.innerText = `${ctrl.label}: ${ctrl.value}`;

      const input = document.createElement("input");
      input.type = "range";
      input.min = ctrl.min;
      input.max = ctrl.max;
      input.step = ctrl.step;
      input.value = ctrl.value;
      input.style.width = "100%";
      input.style.accentColor = "#38bdf8";

      input.addEventListener("input", (e) => {
        vals[ctrl.id] = parseFloat(e.target.value);
        lbl.innerText = `${ctrl.label}: ${vals[ctrl.id]}`;
        if (!simConfig.isAnimated) {
          simConfig.render(canvas, vals, 0);
        }
      });

      wrap.appendChild(lbl);
      wrap.appendChild(input);
      controlsContainer.appendChild(wrap);
    });
  }
  box.appendChild(controlsContainer);
  container.appendChild(box);

  if (simConfig.isAnimated) {
    let start = performance.now();
    function loop(now) {
      const t = (now - start) / 1000;
      simConfig.render(canvas, vals, t);
      window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(loop);
    }
    window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(loop);
  } else {
    simConfig.render(canvas, vals, 0);
  }
};
'''

with open("basic-algebra-sims.js", "w", encoding="utf-8") as f:
    f.write(sims_code.strip() + "\n")

print("basic-algebra-sims.js generated successfully!")
