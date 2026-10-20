// Calculus I Interactive Geometric Simulation Suite
// 8 Real-Time 60 FPS Canvas Simulations for Single-Variable Differential Calculus & Real Analysis

window.CALC1_SIMS = {
  // 1. Dynamic Function Transformation & Inverse Reflection Explorer
  "calc1-trans-inverse-sim": {
    title: "Dynamic Function Transformation & Inverse Reflection Explorer",
    desc: "Visualizes horizontal and vertical transformations g(x) = a f(x - c), and tests invertibility via reflection across the identity line y = x.",
    isAnimated: false,
    controls: [
      { id: "funcSelect", label: "Function (0: x³, 1: eˣ, 2: 2x-1, 3: √x)", min: 0, max: 3, step: 1, value: 0 },
      { id: "paramA", label: "Vertical Scale a", min: -2.5, max: 2.5, step: 0.1, value: 1.0 },
      { id: "paramC", label: "Horizontal Shift c", min: -3.0, max: 3.0, step: 0.1, value: 0.0 },
      { id: "showInverse", label: "Show Inverse f⁻¹(x) (0: No, 1: Yes)", min: 0, max: 1, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const fType = Math.round(vals.funcSelect !== undefined ? vals.funcSelect : 0);
      const a = vals.paramA !== undefined ? vals.paramA : 1.0;
      const c = vals.paramC !== undefined ? vals.paramC : 0.0;
      const showInv = Math.round(vals.showInverse !== undefined ? vals.showInverse : 1) === 1;

      // Coordinate mapping: range [-5, 5] x [-5, 5]
      const minX = -5, maxX = 5, minY = -5, maxY = 5;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Grid & Axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let gx = -4; gx <= 4; gx += 2) {
        ctx.beginPath(); ctx.moveTo(toScreenX(gx), toScreenY(minY)); ctx.lineTo(toScreenX(gx), toScreenY(maxY)); ctx.stroke();
      }
      for (let gy = -4; gy <= 4; gy += 2) {
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(gy)); ctx.lineTo(toScreenX(maxX), toScreenY(gy)); ctx.stroke();
      }

      // Main Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Axis labels
      ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("x", toScreenX(maxX) - 15, toScreenY(0) + 16);
      ctx.fillText("y", toScreenX(0) + 8, toScreenY(maxY) + 15);

      // Identity line y = x (dashed)
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(toScreenX(minX), toScreenY(minX));
      ctx.lineTo(toScreenX(maxX), toScreenY(maxX));
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "rgba(148, 163, 184, 0.7)";
      ctx.fillText("y = x (Identity Line)", toScreenX(3), toScreenY(3) - 8);

      // Function definitions
      function baseF(x) {
        if (fType === 0) return Math.pow(x, 3);
        if (fType === 1) return Math.exp(x);
        if (fType === 2) return 2 * x - 1;
        if (fType === 3) return x >= 0 ? Math.sqrt(x) : NaN;
        return x;
      }
      function f(x) {
        return a * baseF(x - c);
      }

      // Plot f(x)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      let started = false;
      const numPts = 300;
      for (let i = 0; i <= numPts; i++) {
        const x = minX + (i / numPts) * (maxX - minX);
        const y = f(x);
        if (isNaN(y) || y < minY - 5 || y > maxY + 5) {
          started = false;
          continue;
        }
        const sx = toScreenX(x), sy = toScreenY(y);
        if (!started) { ctx.moveTo(sx, sy); started = true; } else { ctx.lineTo(sx, sy); }
      }
      ctx.stroke();

      // Plot f^-1(x) if requested
      if (showInv) {
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        started = false;
        // The graph of f^-1 is simply (f(t), t)
        for (let i = 0; i <= numPts; i++) {
          const t = minX + (i / numPts) * (maxX - minX);
          const y = f(t);
          if (isNaN(y) || y < minX || y > maxX) continue;
          const invX = y;
          const invY = t;
          if (invY < minY || invY > maxY) continue;
          const sx = toScreenX(invX), sy = toScreenY(invY);
          if (!started) { ctx.moveTo(sx, sy); started = true; } else { ctx.lineTo(sx, sy); }
        }
        ctx.stroke();

        // Sample reflection point
        const t0 = 1.0;
        const y0 = f(t0);
        if (!isNaN(y0) && y0 >= minY && y0 <= maxY) {
          const p1x = toScreenX(t0), p1y = toScreenY(y0);
          const p2x = toScreenX(y0), p2y = toScreenY(t0);

          ctx.setLineDash([3, 3]);
          ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
          ctx.beginPath(); ctx.moveTo(p1x, p1y); ctx.lineTo(p2x, p2y); ctx.stroke();
          ctx.setLineDash([]);

          ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(p1x, p1y, 5, 0, Math.PI * 2); ctx.fill();
          ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(p2x, p2y, 5, 0, Math.PI * 2); ctx.fill();

          ctx.fillStyle = "#e2e8f0"; ctx.font = "10px Inter, sans-serif";
          ctx.fillText(`P(${t0.toFixed(1)}, ${y0.toFixed(1)})`, p1x + 8, p1y - 6);
          ctx.fillText(`P'(${y0.toFixed(1)}, ${t0.toFixed(1)})`, p2x + 8, p2y + 14);
        }
      }

      // Legend & Info Panel
      const names = ["Cubic: f(x) = (x-c)³", "Exponential: f(x) = e^(x-c)", "Linear: f(x) = 2(x-c) - 1", "Root: f(x) = √(x-c)"];
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`f(x) = ${a.toFixed(1)} · ${names[fType]}`, 65, 30);

      if (showInv) {
        ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(`f⁻¹(x) [Reflection across y = x]`, 65, 48);
      }
    }
  },

  // 2. Transcendental & Hyperbolic Function Explorer
  "calc1-exp-log-hyperbolic-sim": {
    title: "Transcendental & Hyperbolic Function Explorer",
    desc: "Examines hyperbolic definitions sinh(x) = (eˣ - e⁻ˣ)/2 and cosh(x) = (eˣ + e⁻ˣ)/2, the unit hyperbola u² - v² = 1, and catenary geometry.",
    isAnimated: false,
    controls: [
      { id: "evalX", label: "Coordinate x / Parameter t", min: -2.5, max: 2.5, step: 0.1, value: 1.2 },
      { id: "viewMode", label: "Mode (0: Hyperbolic Curves, 1: Unit Hyperbola Geometry, 2: Exponential vs Log)", min: 0, max: 2, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const xVal = vals.evalX !== undefined ? vals.evalX : 1.2;
      const mode = Math.round(vals.viewMode !== undefined ? vals.viewMode : 0);

      const minX = -4, maxX = 4, minY = -4, maxY = 4;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let g = -3; g <= 3; g++) {
        if (g === 0) continue;
        ctx.beginPath(); ctx.moveTo(toScreenX(g), toScreenY(minY)); ctx.lineTo(toScreenX(g), toScreenY(maxY)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(g)); ctx.lineTo(toScreenX(maxX), toScreenY(g)); ctx.stroke();
      }
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      if (mode === 0) {
        // Mode 0: Hyperbolic functions
        // Plot cosh(x)
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let i = 0; i <= 200; i++) {
          const x = minX + (i / 200) * (maxX - minX);
          const y = Math.cosh(x);
          const sx = toScreenX(x), sy = toScreenY(y);
          if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Plot sinh(x)
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let i = 0; i <= 200; i++) {
          const x = minX + (i / 200) * (maxX - minX);
          const y = Math.sinh(x);
          const sx = toScreenX(x), sy = toScreenY(y);
          if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Plot tanh(x)
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
        ctx.beginPath();
        for (let i = 0; i <= 200; i++) {
          const x = minX + (i / 200) * (maxX - minX);
          const y = Math.tanh(x);
          const sx = toScreenX(x), sy = toScreenY(y);
          if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Marker at xVal
        const cVal = Math.cosh(xVal), sVal = Math.sinh(xVal), tVal = Math.tanh(xVal);
        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(toScreenX(xVal), toScreenY(cVal), 5, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(toScreenX(xVal), toScreenY(sVal), 5, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(toScreenX(xVal), toScreenY(tVal), 4, 0, Math.PI * 2); ctx.fill();

        // Header info
        ctx.fillStyle = "#f59e0b"; ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(`cosh(x) = ${(cVal).toFixed(4)}`, 65, 25);
        ctx.fillStyle = "#38bdf8";
        ctx.fillText(`sinh(x) = ${(sVal).toFixed(4)}`, 220, 25);
        ctx.fillStyle = "#10b981";
        ctx.fillText(`tanh(x) = ${(tVal).toFixed(4)}`, 380, 25);
        ctx.fillStyle = "#e2e8f0"; ctx.font = "12px Inter, sans-serif";
        ctx.fillText(`Fundamental Identity: cosh²(x) - sinh²(x) = ${(cVal*cVal - sVal*sVal).toFixed(4)} ≡ 1`, 65, 45);

      } else if (mode === 1) {
        // Mode 1: Unit Hyperbola u^2 - v^2 = 1
        // Asymptotes u = +/- v
        ctx.setLineDash([3, 3]);
        ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
        ctx.beginPath(); ctx.moveTo(toScreenX(-3.5), toScreenY(-3.5)); ctx.lineTo(toScreenX(3.5), toScreenY(3.5)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(toScreenX(-3.5), toScreenY(3.5)); ctx.lineTo(toScreenX(3.5), toScreenY(-3.5)); ctx.stroke();
        ctx.setLineDash([]);

        // Right branch of hyperbola
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let i = 0; i <= 200; i++) {
          const t = -2.5 + (i / 200) * 5.0;
          const u = Math.cosh(t), v = Math.sinh(t);
          const sx = toScreenX(u), sy = toScreenY(v);
          if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Evaluation point P(cosh t, sinh t)
        const u0 = Math.cosh(xVal), v0 = Math.sinh(xVal);
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(0)); ctx.lineTo(toScreenX(u0), toScreenY(v0)); ctx.stroke();

        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(toScreenX(u0), toScreenY(v0), 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(`P(cosh t, sinh t) = (${u0.toFixed(2)}, ${v0.toFixed(2)})`, toScreenX(u0) + 8, toScreenY(v0) - 8);

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText("Unit Hyperbola: u² - v² = 1 (Parametrized by Hyperbolic Angle t)", 65, 30);
      } else {
        // Mode 2: Exponential vs Logarithm
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let i = 0; i <= 200; i++) {
          const x = -3 + (i / 200) * 4.5;
          const y = Math.exp(x);
          const sx = toScreenX(x), sy = toScreenY(y);
          if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let i = 1; i <= 200; i++) {
          const x = 0.05 + (i / 200) * 3.9;
          const y = Math.log(x);
          const sx = toScreenX(x), sy = toScreenY(y);
          if (i === 1) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Identity line
        ctx.setLineDash([4, 4]); ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
        ctx.beginPath(); ctx.moveTo(toScreenX(-3), toScreenY(-3)); ctx.lineTo(toScreenX(3.5), toScreenY(3.5)); ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText("y = eˣ", 70, 30);
        ctx.fillStyle = "#10b981";
        ctx.fillText("y = ln(x)", 160, 30);
        ctx.fillStyle = "#94a3b8";
        ctx.fillText("Natural Inverse Logarithmic Reflection", 260, 30);
      }
    }
  },

  // 3. Cauchy-Weierstrass Epsilon-Delta Target Tube Explorer
  "calc1-epsilon-delta-sim": {
    title: "Cauchy-Weierstrass ε-δ Target Tube Explorer",
    desc: "Rigorous verification of limits: for any error tolerance ε > 0, find a neighborhood radius δ > 0 ensuring |f(x) - L| < ε whenever 0 < |x - x₀| < δ.",
    isAnimated: false,
    controls: [
      { id: "epsilon", label: "Error Tolerance ε", min: 0.1, max: 1.2, step: 0.05, value: 0.5 },
      { id: "targetX0", label: "Limit Point x₀", min: 1.0, max: 2.5, step: 0.1, value: 1.5 },
      { id: "funcType", label: "Function (0: x², 1: 2x+1, 2: √x)", min: 0, max: 2, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const eps = vals.epsilon !== undefined ? vals.epsilon : 0.5;
      const x0 = vals.targetX0 !== undefined ? vals.targetX0 : 1.5;
      const fType = Math.round(vals.funcType !== undefined ? vals.funcType : 0);

      function f(x) {
        if (fType === 0) return x * x;
        if (fType === 1) return 2 * x + 1;
        if (fType === 2) return Math.sqrt(Math.max(0, x));
        return x;
      }
      function fInv(y) {
        if (fType === 0) return Math.sqrt(Math.max(0, y));
        if (fType === 1) return (y - 1) / 2;
        if (fType === 2) return y * y;
        return y;
      }

      const L = f(x0);
      const yMinTgt = L - eps, yMaxTgt = L + eps;
      // Exact delta calculation
      const xLeft = fInv(yMinTgt), xRight = fInv(yMaxTgt);
      const delta = Math.min(Math.abs(x0 - xLeft), Math.abs(xRight - x0));

      const minX = 0, maxX = 3.5, minY = 0, maxY = 6.0;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let gx = 0.5; gx <= 3.0; gx += 0.5) {
        ctx.beginPath(); ctx.moveTo(toScreenX(gx), toScreenY(minY)); ctx.lineTo(toScreenX(gx), toScreenY(maxY)); ctx.stroke();
      }
      for (let gy = 1.0; gy <= 5.0; gy += 1.0) {
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(gy)); ctx.lineTo(toScreenX(maxX), toScreenY(gy)); ctx.stroke();
      }
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Shaded Epsilon Target Band on Y-axis
      const syMax = toScreenY(yMaxTgt), syMin = toScreenY(yMinTgt);
      ctx.fillStyle = "rgba(16, 185, 129, 0.12)";
      ctx.fillRect(toScreenX(minX), syMax, toScreenX(maxX) - toScreenX(minX), syMin - syMax);

      // Horizontal Epsilon Boundary lines
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), syMax); ctx.lineTo(toScreenX(maxX), syMax); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), syMin); ctx.lineTo(toScreenX(maxX), syMin); ctx.stroke();

      // Shaded Delta Control Band on X-axis
      const sxMin = toScreenX(x0 - delta), sxMax = toScreenX(x0 + delta);
      ctx.fillStyle = "rgba(56, 189, 248, 0.12)";
      ctx.fillRect(sxMin, toScreenY(maxY), sxMax - sxMin, toScreenY(minY) - toScreenY(maxY));

      // Vertical Delta Boundary lines
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(sxMin, toScreenY(minY)); ctx.lineTo(sxMin, toScreenY(maxY)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(sxMax, toScreenY(minY)); ctx.lineTo(sxMax, toScreenY(maxY)); ctx.stroke();
      ctx.setLineDash([]);

      // Function curve
      ctx.strokeStyle = "#e2e8f0"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= 200; i++) {
        const x = minX + (i / 200) * (maxX - minX);
        const y = f(x);
        const sx = toScreenX(x), sy = toScreenY(y);
        if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Target point (x0, L)
      const sx0 = toScreenX(x0), sL = toScreenY(L);
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(sx0, sL, 6, 0, Math.PI * 2); ctx.fill();

      // Readout
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      const fNames = ["f(x) = x²", "f(x) = 2x + 1", "f(x) = √x"];
      ctx.fillText(`Target Limit: lim_{x → ${x0.toFixed(2)}} ${fNames[fType]} = L = ${L.toFixed(3)}`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Given Tolerance: ε = ${eps.toFixed(2)}  ⇒  Target Window: [${yMinTgt.toFixed(2)}, ${yMaxTgt.toFixed(2)}]`, 65, 43);

      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Guaranteed Neighborhood: δ = ${delta.toFixed(4)}  ⇒  Domain Window: [${(x0 - delta).toFixed(4)}, ${(x0 + delta).toFixed(4)}]`, 65, 60);
    }
  },

  // 4. Intermediate Value Theorem (IVT) & Root Bisection Solver
  "calc1-ivt-bisection-sim": {
    title: "Intermediate Value Theorem (IVT) & Root Bisection Solver",
    desc: "Visualizes Bolzano's Intermediate Value Theorem: continuity on [a, b] with f(a)f(b) < 0 guarantees a root c. Steps through binary bisection interval halving [aₙ, bₙ].",
    isAnimated: false,
    controls: [
      { id: "steps", label: "Bisection Iterations n", min: 1, max: 8, step: 1, value: 3 },
      { id: "func", label: "Function (0: x³-2x-5, 1: cos(x)-x, 2: x³-x-2)", min: 0, max: 2, step: 1, value: 0 },
      { id: "bracketA", label: "Initial Left Endpoint a", min: 0.0, max: 2.0, step: 0.1, value: 1.0 },
      { id: "bracketB", label: "Initial Right Endpoint b", min: 2.2, max: 4.0, step: 0.1, value: 3.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const nSteps = Math.round(vals.steps !== undefined ? vals.steps : 3);
      const fType = Math.round(vals.func !== undefined ? vals.func : 0);
      let initA = vals.bracketA !== undefined ? vals.bracketA : 1.0;
      let initB = vals.bracketB !== undefined ? vals.bracketB : 3.0;

      function f(x) {
        if (fType === 0) return x * x * x - 2 * x - 5;
        if (fType === 1) return Math.cos(x) - x;
        if (fType === 2) return x * x * x - x - 2;
        return x;
      }

      // Perform bisection
      let a = initA, b = initB;
      const history = [];
      for (let s = 1; s <= nSteps; s++) {
        const m = (a + b) / 2;
        const fm = f(m);
        history.push({ step: s, a, b, m, fm });
        if (f(a) * fm <= 0) {
          b = m;
        } else {
          a = m;
        }
      }
      const curM = (a + b) / 2;

      // Coordinate mapping
      const minX = Math.min(initA - 0.5, 0), maxX = Math.max(initB + 0.5, 3.5);
      const minY = -10, maxY = 15;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Shaded active interval [a, b]
      const sa = toScreenX(a), sb = toScreenX(b);
      ctx.fillStyle = "rgba(16, 185, 129, 0.15)";
      ctx.fillRect(sa, toScreenY(maxY), sb - sa, toScreenY(minY) - toScreenY(maxY));

      // Plot curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= 250; i++) {
        const x = minX + (i / 250) * (maxX - minX);
        const y = f(x);
        const sx = toScreenX(x), sy = toScreenY(y);
        if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Interval boundary markers
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(sa, toScreenY(0) - 10); ctx.lineTo(sa, toScreenY(0) + 10); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(sb, toScreenY(0) - 10); ctx.lineTo(sb, toScreenY(0) + 10); ctx.stroke();

      // Current Midpoint marker
      const sm = toScreenX(curM);
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(sm, toScreenY(0), 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(sm, toScreenY(f(curM)), 6, 0, Math.PI * 2); ctx.fill();

      // Dashed vertical dropped to midpoint
      ctx.setLineDash([3, 3]); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(sm, toScreenY(0)); ctx.lineTo(sm, toScreenY(f(curM))); ctx.stroke();
      ctx.setLineDash([]);

      // Readouts
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`IVT Root Bisection: Step ${nSteps} | Active Bracket [${a.toFixed(4)}, ${b.toFixed(4)}]`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Current Approximation: c ≈ ${curM.toFixed(5)}  |  f(c) = ${f(curM).toFixed(5)}`, 65, 45);

      ctx.fillStyle = "#94a3b8";
      ctx.fillText(`Theoretical Error Bound: (b - a)/2ⁿ = ${((initB - initA) / Math.pow(2, nSteps)).toFixed(5)}`, 65, 63);
    }
  },

  // 5. Secant-to-Tangent Dynamic Limiter (h -> 0)
  "calc1-secant-tangent-sim": {
    title: "Secant-to-Tangent Dynamic Limiter (h → 0)",
    desc: "Calculates the difference quotient slope m_sec = [f(x₀+h) - f(x₀)]/h and demonstrates how the secant line smoothly collapses into the tangent line m_tan = f'(x₀) as h → 0.",
    isAnimated: false,
    controls: [
      { id: "x0", label: "Base Point x₀", min: -1.5, max: 2.0, step: 0.1, value: 1.0 },
      { id: "stepH", label: "Increment h", min: -2.0, max: 2.0, step: 0.05, value: 1.0 },
      { id: "func", label: "Function (0: x²-2, 1: sin(x), 2: x³-3x)", min: 0, max: 2, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const x0 = vals.x0 !== undefined ? vals.x0 : 1.0;
      let hVal = vals.stepH !== undefined ? vals.stepH : 1.0;
      if (Math.abs(hVal) < 0.01) hVal = 0.01; // Avoid divide by zero
      const fType = Math.round(vals.func !== undefined ? vals.func : 0);

      function f(x) {
        if (fType === 0) return x * x - 2;
        if (fType === 1) return 2 * Math.sin(x);
        if (fType === 2) return (x * x * x - 3 * x) / 2;
        return x;
      }
      function fPrime(x) {
        if (fType === 0) return 2 * x;
        if (fType === 1) return 2 * Math.cos(x);
        if (fType === 2) return (3 * x * x - 3) / 2;
        return 1;
      }

      const y0 = f(x0);
      const x1 = x0 + hVal;
      const y1 = f(x1);
      const mSec = (y1 - y0) / hVal;
      const mTan = fPrime(x0);

      const minX = -3.0, maxX = 3.5, minY = -4.0, maxY = 5.0;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Plot function curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= 250; i++) {
        const x = minX + (i / 250) * (maxX - minX);
        const y = f(x);
        const sx = toScreenX(x), sy = toScreenY(y);
        if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Tangent line at x0 (dashed emerald)
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath();
      const tanX_L = minX, tanY_L = y0 + mTan * (tanX_L - x0);
      const tanX_R = maxX, tanY_R = y0 + mTan * (tanX_R - x0);
      ctx.moveTo(toScreenX(tanX_L), toScreenY(tanY_L));
      ctx.lineTo(toScreenX(tanX_R), toScreenY(tanY_R));
      ctx.stroke();
      ctx.setLineDash([]);

      // Secant line through (x0, y0) and (x1, y1) in bright amber
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.beginPath();
      const secX_L = minX, secY_L = y0 + mSec * (secX_L - x0);
      const secX_R = maxX, secY_R = y0 + mSec * (secX_R - x0);
      ctx.moveTo(toScreenX(secX_L), toScreenY(secY_L));
      ctx.lineTo(toScreenX(secX_R), toScreenY(secY_R));
      ctx.stroke();

      // Points P and Q
      const sPx = toScreenX(x0), sPy = toScreenY(y0);
      const sQx = toScreenX(x1), sQy = toScreenY(y1);

      // Delta triangle
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(sPx, sPy);
      ctx.lineTo(sQx, sPy);
      ctx.lineTo(sQx, sQy);
      ctx.stroke();

      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(sPx, sPy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(sQx, sQy, 6, 0, Math.PI * 2); ctx.fill();

      // Readout
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Instantaneous Tangent Slope: f'(x₀) = ${mTan.toFixed(4)}`, 65, 25);

      ctx.fillStyle = "#f59e0b"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Secant Slope: m_sec = Δy/Δx = [f(x₀+h) - f(x₀)] / h = ${mSec.toFixed(4)} (h = ${hVal.toFixed(2)})`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`Difference Error: |m_sec - f'(x₀)| = ${Math.abs(mSec - mTan).toFixed(4)}`, 65, 63);
    }
  },

  // 6. Implicit Differentiation & Orthogonal Trajectories
  "calc1-implicit-slope-sim": {
    title: "Implicit Differentiation & Orthogonal Trajectories",
    desc: "Computes implicit slopes dy/dx = -F_x / F_y along algebraic plane curves (Folium of Descartes, Ellipse, Lemniscate) and renders tangent and normal lines.",
    isAnimated: false,
    controls: [
      { id: "curveType", label: "Algebraic Curve (0: Folium of Descartes, 1: Ellipse, 2: Lemniscate)", min: 0, max: 2, step: 1, value: 0 },
      { id: "paramT", label: "Parameter t (Angle/Position)", min: 0.2, max: 6.0, step: 0.1, value: 0.8 },
      { id: "showNormal", label: "Show Normal Line (0: No, 1: Yes)", min: 0, max: 1, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const cType = Math.round(vals.curveType !== undefined ? vals.curveType : 0);
      const t = vals.paramT !== undefined ? vals.paramT : 0.8;
      const showNorm = Math.round(vals.showNormal !== undefined ? vals.showNormal : 1) === 1;

      const minX = -3.5, maxX = 3.5, minY = -3.5, maxY = 3.5;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      let x0 = 0, y0 = 0, slope = 0, curveName = "";

      if (cType === 0) {
        // Folium of Descartes: x^3 + y^3 - 3axy = 0 (a = 2)
        // Parametric: x(p) = 3*a*p/(1+p^3), y(p) = 3*a*p^2/(1+p^3)
        const aParam = 1.5;
        curveName = "Folium of Descartes: x³ + y³ - 4.5xy = 0";
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        let started = false;
        for (let p = -4.0; p <= 4.0; p += 0.02) {
          if (Math.abs(p + 1.0) < 0.1) continue;
          const denom = 1 + p * p * p;
          const x = (3 * aParam * p) / denom;
          const y = (3 * aParam * p * p) / denom;
          if (x < minX || x > maxX || y < minY || y > maxY) { started = false; continue; }
          const sx = toScreenX(x), sy = toScreenY(y);
          if (!started) { ctx.moveTo(sx, sy); started = true; } else { ctx.lineTo(sx, sy); }
        }
        ctx.stroke();

        const p0 = t - 3.0;
        const denom0 = 1 + p0 * p0 * p0;
        x0 = (3 * aParam * p0) / (Math.abs(denom0) < 0.01 ? 0.01 : denom0);
        y0 = (3 * aParam * p0 * p0) / (Math.abs(denom0) < 0.01 ? 0.01 : denom0);
        // dy/dx via implicit diff: F(x, y) = x^3 + y^3 - 3axy = 0
        // F_x = 3x^2 - 3ay, F_y = 3y^2 - 3ax
        const Fx = 3 * x0 * x0 - 3 * aParam * y0;
        const Fy = 3 * y0 * y0 - 3 * aParam * x0;
        slope = Math.abs(Fy) > 0.001 ? -Fx / Fy : 999;

      } else if (cType === 1) {
        // Ellipse: x^2/4 + y^2/2 = 1 (a = 2, b = 1.414)
        curveName = "Ellipse: x²/4 + y²/2 = 1";
        const aParam = 2.0, bParam = 1.414;
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let a = 0; a <= 200; a++) {
          const ang = (a / 200) * Math.PI * 2;
          const x = aParam * Math.cos(ang), y = bParam * Math.sin(ang);
          const sx = toScreenX(x), sy = toScreenY(y);
          if (a === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        x0 = aParam * Math.cos(t);
        y0 = bParam * Math.sin(t);
        // dy/dx = - (b^2 x) / (a^2 y)
        slope = Math.abs(y0) > 0.001 ? -(bParam * bParam * x0) / (aParam * aParam * y0) : 999;

      } else {
        // Lemniscate: (x^2+y^2)^2 = 2 a^2 (x^2-y^2), a = 2
        curveName = "Lemniscate of Bernoulli: (x²+y²)² = 8(x²-y²)";
        const aParam = 2.0;
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        let started = false;
        for (let th = 0; th <= Math.PI * 2; th += 0.02) {
          const cos2 = Math.cos(2 * th);
          if (cos2 >= 0) {
            const r = Math.sqrt(2 * aParam * aParam * cos2);
            const x = r * Math.cos(th), y = r * Math.sin(th);
            const sx = toScreenX(x), sy = toScreenY(y);
            if (!started) { ctx.moveTo(sx, sy); started = true; } else { ctx.lineTo(sx, sy); }
          } else {
            started = false;
          }
        }
        ctx.stroke();

        const cos2t = Math.cos(2 * t);
        const r0 = cos2t >= 0 ? Math.sqrt(2 * aParam * aParam * cos2t) : 0;
        x0 = r0 * Math.cos(t);
        y0 = r0 * Math.sin(t);
        // Tangent slope from polar derivative
        const dr_dth = cos2t > 0.001 ? -(2 * aParam * aParam * Math.sin(2 * t)) / (2 * r0) : 0;
        const dx_dt = dr_dth * Math.cos(t) - r0 * Math.sin(t);
        const dy_dt = dr_dth * Math.sin(t) + r0 * Math.cos(t);
        slope = Math.abs(dx_dt) > 0.001 ? dy_dt / dx_dt : 999;
      }

      // Clamp point for drawing
      if (x0 >= minX && x0 <= maxX && y0 >= minY && y0 <= maxY) {
        const sx0 = toScreenX(x0), sy0 = toScreenY(y0);

        // Tangent Line
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
        ctx.beginPath();
        const tanX_L = minX, tanY_L = y0 + slope * (tanX_L - x0);
        const tanX_R = maxX, tanY_R = y0 + slope * (tanX_R - x0);
        ctx.moveTo(toScreenX(tanX_L), toScreenY(tanY_L));
        ctx.lineTo(toScreenX(tanX_R), toScreenY(tanY_R));
        ctx.stroke();

        // Normal Line
        if (showNorm && Math.abs(slope) > 0.001) {
          const normSlope = -1 / slope;
          ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2;
          ctx.beginPath();
          const normX_L = minX, normY_L = y0 + normSlope * (normX_L - x0);
          const normX_R = maxX, normY_R = y0 + normSlope * (normX_R - x0);
          ctx.moveTo(toScreenX(normX_L), toScreenY(normY_L));
          ctx.lineTo(toScreenX(normX_R), toScreenY(normY_R));
          ctx.stroke();
        }

        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(sx0, sy0, 6, 0, Math.PI * 2); ctx.fill();
      }

      // Readouts
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(curveName, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Point P(${x0.toFixed(3)}, ${y0.toFixed(3)})  |  Implicit Tangent dy/dx = ${slope.toFixed(4)}`, 65, 45);

      if (showNorm) {
        ctx.fillStyle = "#ec4899";
        const normVal = Math.abs(slope) > 0.001 ? (-1 / slope).toFixed(4) : "Undefined";
        ctx.fillText(`Orthogonal Normal Slope m_⊥ = -dx/dy = ${normVal}`, 65, 63);
      }
    }
  },

  // 7. Rolle's & Lagrange Mean Value Theorem Scanner
  "calc1-mvt-rolle-sim": {
    title: "Rolle's & Lagrange Mean Value Theorem Scanner",
    desc: "Scans the interior interval (a, b) to find points c guaranteed by the Mean Value Theorem where f'(c) = [f(b) - f(a)] / (b - a).",
    isAnimated: false,
    controls: [
      { id: "bracketA", label: "Left Endpoint a", min: -3.0, max: -0.5, step: 0.1, value: -2.0 },
      { id: "bracketB", label: "Right Endpoint b", min: 0.5, max: 3.0, step: 0.1, value: 2.0 },
      { id: "func", label: "Function (0: x³-3x, 1: -x²+4, 2: sin(x)+x/2)", min: 0, max: 2, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a = vals.bracketA !== undefined ? vals.bracketA : -2.0;
      const b = vals.bracketB !== undefined ? vals.bracketB : 2.0;
      const fType = Math.round(vals.func !== undefined ? vals.func : 0);

      function f(x) {
        if (fType === 0) return x * x * x - 3 * x;
        if (fType === 1) return -x * x + 4;
        if (fType === 2) return Math.sin(x) + x / 2;
        return x;
      }
      function fPrime(x) {
        if (fType === 0) return 3 * x * x - 3;
        if (fType === 1) return -2 * x;
        if (fType === 2) return Math.cos(x) + 0.5;
        return 1;
      }

      const fa = f(a), fb = f(b);
      const mAvg = (fb - fa) / (b - a);

      // Numerical search for roots c in (a, b) of f'(c) - mAvg = 0
      const cRoots = [];
      const steps = 300;
      let prevVal = fPrime(a + 0.001) - mAvg;
      for (let i = 1; i < steps; i++) {
        const x = a + (i / steps) * (b - a);
        const curVal = fPrime(x) - mAvg;
        if (prevVal * curVal <= 0) {
          // Bisection root refine
          let xL = x - (b - a) / steps, xR = x;
          for (let it = 0; it < 10; it++) {
            const xM = (xL + xR) / 2;
            if ((fPrime(xL) - mAvg) * (fPrime(xM) - mAvg) <= 0) xR = xM; else xL = xM;
          }
          cRoots.push((xL + xR) / 2);
        }
        prevVal = curVal;
      }

      const minX = -4.0, maxX = 4.0, minY = -5.0, maxY = 6.0;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Plot function curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= 250; i++) {
        const x = minX + (i / 250) * (maxX - minX);
        const y = f(x);
        const sx = toScreenX(x), sy = toScreenY(y);
        if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Secant chord from (a, fa) to (b, fb) in dashed amber
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(toScreenX(a), toScreenY(fa));
      ctx.lineTo(toScreenX(b), toScreenY(fb));
      ctx.stroke();
      ctx.setLineDash([]);

      // Endpoints A and B
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(toScreenX(a), toScreenY(fa), 6, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(toScreenX(b), toScreenY(fb), 6, 0, Math.PI * 2); ctx.fill();

      // Render parallel tangent lines at each found c
      cRoots.forEach(c => {
        const fc = f(c);
        const scx = toScreenX(c), scy = toScreenY(fc);

        // Vertical drop line
        ctx.setLineDash([3, 3]); ctx.strokeStyle = "rgba(16, 185, 129, 0.5)"; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.moveTo(scx, toScreenY(0)); ctx.lineTo(scx, scy); ctx.stroke();
        ctx.setLineDash([]);

        // Parallel tangent line
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
        ctx.beginPath();
        const tLen = 1.2;
        const xL = c - tLen, yL = fc + mAvg * (xL - c);
        const xR = c + tLen, yR = fc + mAvg * (xR - c);
        ctx.moveTo(toScreenX(xL), toScreenY(yL));
        ctx.lineTo(toScreenX(xR), toScreenY(yR));
        ctx.stroke();

        ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(scx, scy, 6, 0, Math.PI * 2); ctx.fill();
      });

      // Readouts
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Lagrange Mean Value Theorem on [${a.toFixed(2)}, ${b.toFixed(2)}]`, 65, 25);

      ctx.fillStyle = "#f59e0b"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Average Secant Slope: m_avg = [f(b) - f(a)] / (b - a) = ${mAvg.toFixed(4)}`, 65, 45);

      ctx.fillStyle = "#10b981";
      const cStr = cRoots.map(c => `c = ${c.toFixed(3)}`).join(", ");
      ctx.fillText(`Guaranteed Parallel Tangents: ${cRoots.length} points found: ${cStr || "None in interval"}`, 65, 63);
    }
  },

  // 8. Analytical Curve Sketcher & Applied Optimization Solver
  "calc1-curve-optimization-sim": {
    title: "Analytical Curve Sketcher & Applied Optimization Solver",
    desc: "Combines 7-step differential curve analysis (critical numbers, concavity, inflection points) with applied geometric optimization (box folding volume V = x(W-2x)(L-2x)).",
    isAnimated: false,
    controls: [
      { id: "mode", label: "Mode (0: Polynomial 7-Step, 1: Box Optimization, 2: Rational Asymptotes)", min: 0, max: 2, step: 1, value: 1 },
      { id: "cutX", label: "Box Corner Cutout x (Mode 1)", min: 0.5, max: 4.5, step: 0.1, value: 2.2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const mode = Math.round(vals.mode !== undefined ? vals.mode : 1);
      const cutX = vals.cutX !== undefined ? vals.cutX : 2.2;

      if (mode === 1) {
        // Mode 1: Box Optimization
        // Sheet dimensions W = 10, L = 16
        const W_sheet = 10.0, L_sheet = 16.0;
        // V(x) = x * (W - 2x) * (L - 2x)
        // dV/dx = (W - 2x)(L - 2x) - 2x(L - 2x) - 2x(W - 2x) = 12x^2 - 4(W+L)x + WL = 0
        // x* = [4(W+L) - sqrt(16(W+L)^2 - 48 WL)] / 24 = [(W+L) - sqrt(W^2 - WL + L^2)] / 6
        const xOpt = ((W_sheet + L_sheet) - Math.sqrt(W_sheet * W_sheet - W_sheet * L_sheet + L_sheet * L_sheet)) / 6;
        const curV = Math.max(0, cutX * (W_sheet - 2 * cutX) * (L_sheet - 2 * cutX));
        const maxV = xOpt * (W_sheet - 2 * xOpt) * (L_sheet - 2 * xOpt);

        // Left Panel: 2D Cardboard Layout
        const p2d = { x: 50, y: 80, w: 280, h: 220 };
        ctx.fillStyle = "rgba(30, 41, 59, 0.7)";
        ctx.fillRect(p2d.x, p2d.y, p2d.w, p2d.h);
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
        ctx.strokeRect(p2d.x, p2d.y, p2d.w, p2d.h);

        // Cutout corners of size cutX (scaled)
        const scale2D = p2d.h / W_sheet;
        const cutPx = cutX * scale2D;

        ctx.fillStyle = "rgba(239, 68, 68, 0.4)";
        ctx.fillRect(p2d.x, p2d.y, cutPx, cutPx); // Top-left
        ctx.fillRect(p2d.x + p2d.w - cutPx, p2d.y, cutPx, cutPx); // Top-right
        ctx.fillRect(p2d.x, p2d.y + p2d.h - cutPx, cutPx, cutPx); // Bottom-left
        ctx.fillRect(p2d.x + p2d.w - cutPx, p2d.y + p2d.h - cutPx, cutPx, cutPx); // Bottom-right

        // Dashed fold lines
        ctx.setLineDash([4, 4]); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
        ctx.strokeRect(p2d.x + cutPx, p2d.y + cutPx, p2d.w - 2 * cutPx, p2d.h - 2 * cutPx);
        ctx.setLineDash([]);

        ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Sheet Width: W = ${W_sheet}`, p2d.x + 10, p2d.y - 10);
        ctx.fillText(`Sheet Length: L = ${L_sheet}`, p2d.x + 150, p2d.y - 10);
        ctx.fillStyle = "#ef4444";
        ctx.fillText(`Corner Cutouts: x = ${cutX.toFixed(1)}`, p2d.x + 10, p2d.y + p2d.h + 20);

        // Right Panel: Volume Curve V(x) vs x
        const plot = { x: 380, y: 70, w: w - 420, h: 230 };
        ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
        ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

        const toGraphX = (x) => plot.x + (x / 5.0) * plot.w;
        const toGraphY = (v) => (plot.y + plot.h) - (v / (maxV * 1.25)) * plot.h;

        // Curve V(x)
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let i = 0; i <= 200; i++) {
          const gx = (i / 200) * (W_sheet / 2);
          const gv = gx * (W_sheet - 2 * gx) * (L_sheet - 2 * gx);
          const sx = toGraphX(gx), sy = toGraphY(gv);
          if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Optimum Peak marker
        const sOptX = toGraphX(xOpt), sOptY = toGraphY(maxV);
        ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(sOptX, sOptY, 6, 0, Math.PI * 2); ctx.fill();

        // Current cut marker
        const sCurX = toGraphX(cutX), sCurY = toGraphY(curV);
        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(sCurX, sCurY, 6, 0, Math.PI * 2); ctx.fill();

        // Readout Header
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText(`Applied Optimization: Box of Maximum Volume V(x) = x(W - 2x)(L - 2x)`, 50, 25);

        ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
        ctx.fillText(`Optimal Cutout: x* = ${xOpt.toFixed(3)}  |  Maximum Volume: V_max = ${maxV.toFixed(2)}`, 50, 45);

        ctx.fillStyle = "#f59e0b";
        ctx.fillText(`Current Cutout: x = ${cutX.toFixed(2)}  |  Current Volume: V(x) = ${curV.toFixed(2)}`, 420, 45);

      } else if (mode === 0) {
        // Mode 0: Polynomial 7-Step f(x) = x^4 - 4x^3 + 10
        function fPoly(x) { return Math.pow(x, 4) - 4 * Math.pow(x, 3) + 10; }
        const minX = -1.5, maxX = 4.5, minY = -25, maxY = 35;
        const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
        const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let i = 0; i <= 250; i++) {
          const x = minX + (i / 250) * (maxX - minX);
          const y = fPoly(x);
          const sx = toScreenX(x), sy = toScreenY(y);
          if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Critical Point & Local Min at (3, -17)
        ctx.fillStyle = "#10b981";
        ctx.beginPath(); ctx.arc(toScreenX(3), toScreenY(-17), 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Global Min (3, -17)", toScreenX(3) + 8, toScreenY(-17));

        // Inflection points at (0, 10) and (2, -6)
        ctx.fillStyle = "#ec4899";
        ctx.beginPath(); ctx.arc(toScreenX(0), toScreenY(10), 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillText("Inflection (0, 10)", toScreenX(0) + 8, toScreenY(10) - 8);

        ctx.beginPath(); ctx.arc(toScreenX(2), toScreenY(-6), 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillText("Inflection (2, -6)", toScreenX(2) + 8, toScreenY(-6) - 8);

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText("7-Step Polynomial Analysis: f(x) = x⁴ - 4x³ + 10", 65, 25);
        ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
        ctx.fillText("Critical numbers: x = 0, 3  |  f''(x) = 12x(x - 2) ⇒ Concave Up on (-∞,0) ∪ (2,∞)", 65, 45);

      } else {
        // Mode 2: Rational Function f(x) = x^2 / (x^2 - 4)
        function fRat(x) { return (x * x) / (x * x - 4); }
        const minX = -5, maxX = 5, minY = -5, maxY = 5;
        const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
        const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

        // Vertical asymptotes x = +/- 2
        ctx.setLineDash([4, 4]); ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(toScreenX(-2), toScreenY(minY)); ctx.lineTo(toScreenX(-2), toScreenY(maxY)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(toScreenX(2), toScreenY(minY)); ctx.lineTo(toScreenX(2), toScreenY(maxY)); ctx.stroke();

        // Horizontal asymptote y = 1
        ctx.strokeStyle = "#10b981";
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(1)); ctx.lineTo(toScreenX(maxX), toScreenY(1)); ctx.stroke();
        ctx.setLineDash([]);

        // Plot curve branches
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        [-4.9, -1.9, 2.1].forEach((startSeg, idx) => {
          const endSeg = idx === 0 ? -2.1 : (idx === 1 ? 1.9 : 4.9);
          ctx.beginPath();
          for (let i = 0; i <= 100; i++) {
            const x = startSeg + (i / 100) * (endSeg - startSeg);
            const y = fRat(x);
            const sx = toScreenX(x), sy = toScreenY(y);
            if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
          }
          ctx.stroke();
        });

        // Local max at (0, 0)
        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(toScreenX(0), toScreenY(0), 6, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText("Rational Asymptote Analysis: f(x) = x² / (x² - 4)", 65, 25);
        ctx.fillStyle = "#ef4444"; ctx.font = "12px Inter, sans-serif";
        ctx.fillText("Vertical Asymptotes: x = -2, x = +2  |  Horizontal Asymptote: y = 1", 65, 45);
      }
    }
  }
};

// Simulation Engine Integration for Calculus I
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

const origCalc1Init = window.SimulationEngine.initSimulation;
window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const simConfig = (window.CALC1_SIMS && window.CALC1_SIMS[simType]) ||
                    (window.RP_SIMS && window.RP_SIMS[simType]);

  if (!simConfig) {
    if (origCalc1Init) {
      origCalc1Init(containerId, simType);
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
    <p style="margin: 0.4rem 0 0 0; color: #94a3b8; font-size: 0.85rem; line-height: 1.4;">${simConfig.desc}</p>
  `;
  box.appendChild(header);

  const canvas = document.createElement("canvas");
  canvas.width = 750;
  canvas.height = 380;
  canvas.style.width = "100%";
  canvas.style.maxWidth = "750px";
  canvas.style.height = "auto";
  canvas.style.aspectRatio = "750 / 380";
  canvas.style.background = "#050811";
  canvas.style.borderRadius = "8px";
  canvas.style.border = "1px solid #1e293b";
  canvas.style.display = "block";
  box.appendChild(canvas);

  const ctrlBar = document.createElement("div");
  ctrlBar.style.display = "flex";
  ctrlBar.style.flexWrap = "wrap";
  ctrlBar.style.gap = "1rem";
  ctrlBar.style.marginTop = "1rem";
  ctrlBar.style.alignItems = "center";

  const currentVals = {};

  if (simConfig.controls) {
    simConfig.controls.forEach(c => {
      currentVals[c.id] = c.value;
      const wrap = document.createElement("div");
      wrap.style.display = "flex";
      wrap.style.flexDirection = "column";
      wrap.style.gap = "0.25rem";
      wrap.style.minWidth = "160px";

      const lbl = document.createElement("label");
      lbl.innerText = `${c.label}: ${c.value}`;
      lbl.style.fontSize = "0.8rem";
      lbl.style.color = "#94a3b8";

      const input = document.createElement("input");
      input.type = "range";
      input.min = c.min;
      input.max = c.max;
      input.step = c.step;
      input.value = c.value;
      input.style.accentColor = "#38bdf8";

      input.addEventListener("input", (e) => {
        const val = parseFloat(e.target.value);
        currentVals[c.id] = val;
        lbl.innerText = `${c.label}: ${val}`;
        if (!simConfig.isAnimated) {
          simConfig.render(canvas, currentVals, 0);
        }
      });

      wrap.appendChild(lbl);
      wrap.appendChild(input);
      ctrlBar.appendChild(wrap);
    });
  }

  box.appendChild(ctrlBar);
  container.appendChild(box);
  simConfig.render(canvas, currentVals, 0);
};
