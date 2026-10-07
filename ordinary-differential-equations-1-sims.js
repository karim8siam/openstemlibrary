// MTH 2103: Ordinary Differential Equations I — Interactive Simulation Suite
// 8 Real-Time 60 FPS HTML5 Canvas Mathematical & Physical Simulations

window.ODE1_SIMS = {
  // 1. Direction Fields, Streamlines & Phase Line Stability Analyzer
  "ode1-dirfield-sim": {
    title: "Direction Fields, Streamlines & Phase Line Stability Analyzer",
    desc: "Interactive slope field generator for first-order ODEs y' = f(x, y). Explore vector slopes, isoclines, and numerical integral curves using Runge-Kutta 4th Order (RK4).",
    isAnimated: true,
    controls: [
      { id: "eqType", label: "System (0: y(1-y), 1: x-y, 2: y²-x, 3: sin(x)-y)", min: 0, max: 3, step: 1, value: 0 },
      { id: "gridDensity", label: "Grid Density", min: 10, max: 26, step: 2, value: 18 },
      { id: "initY0", label: "Initial Condition y(0)", min: -1.5, max: 2.5, step: 0.1, value: 0.2 },
      { id: "stepSize", label: "RK4 Step dt", min: 0.02, max: 0.1, step: 0.01, value: 0.05 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const eq = Math.round(vals.eqType !== undefined ? vals.eqType : 0);
      const density = vals.gridDensity || 18;
      const y0 = vals.initY0 !== undefined ? vals.initY0 : 0.2;
      const dt = vals.stepSize || 0.05;

      // Coordinate mapping [-4, 4] x [-3, 3]
      const minX = -4, maxX = 4, minY = -3, maxY = 3;
      const toScreenX = (x) => 55 + ((x - minX) / (maxX - minX)) * (w - 110);
      const toScreenY = (y) => (h - 45) - ((y - minY) / (maxY - minY)) * (h - 90);
      const toMathX = (sx) => minX + ((sx - 55) / (w - 110)) * (maxX - minX);
      const toMathY = (sy) => minY + (((h - 45) - sy) / (h - 90)) * (maxY - minY);

      // ODE Slope Function f(x, y)
      const f = (x, y) => {
        if (eq === 0) return y * (1 - y); // Logistic autonomous
        if (eq === 1) return x - y;      // Linear non-autonomous
        if (eq === 2) return y * y - x;  // Non-linear Riccati-type
        return Math.sin(x) - y;          // Oscillatory
      };

      // Background grid
      ctx.strokeStyle = "#131f38";
      ctx.lineWidth = 1;
      for (let x = -3; x <= 3; x++) {
        ctx.beginPath(); ctx.moveTo(toScreenX(x), toScreenY(minY)); ctx.lineTo(toScreenX(x), toScreenY(maxY)); ctx.stroke();
      }
      for (let y = -2; y <= 2; y++) {
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(y)); ctx.lineTo(toScreenX(maxX), toScreenY(y)); ctx.stroke();
      }

      // Coordinate axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Axis labels
      ctx.fillStyle = "#64748b";
      ctx.font = "11px Fira Code, monospace";
      ctx.fillText("x", toScreenX(maxX) - 12, toScreenY(0) + 15);
      ctx.fillText("y", toScreenX(0) + 8, toScreenY(maxY) + 15);

      // Draw Direction Field Slopes
      const xStep = (maxX - minX) / density;
      const yStep = (maxY - minY) / density;
      const segLen = 9;

      for (let x = minX; x <= maxX; x += xStep) {
        for (let y = minY; y <= maxY; y += yStep) {
          const slope = f(x, y);
          const angle = Math.atan(slope);
          const sx = toScreenX(x), sy = toScreenY(y);
          const dx = Math.cos(angle) * segLen;
          const dy = Math.sin(angle) * segLen;

          // Color based on slope magnitude
          const hue = 195 + Math.tanh(slope) * 45;
          ctx.strokeStyle = `hsla(${hue}, 85%, 60%, 0.45)`;
          ctx.lineWidth = 1.2;
          ctx.beginPath();
          ctx.moveTo(sx - dx, sy + dy);
          ctx.lineTo(sx + dx, sy - dy);
          ctx.stroke();

          // Small directional arrow head
          ctx.fillStyle = `hsla(${hue}, 85%, 70%, 0.6)`;
          ctx.beginPath();
          ctx.arc(sx + dx, sy - dy, 1.2, 0, 2 * Math.PI);
          ctx.fill();
        }
      }

      // Numerical RK4 Streamline Integration from Initial Conditions
      const drawStreamline = (startX, startY, strokeStyle, width) => {
        ctx.strokeStyle = strokeStyle;
        ctx.lineWidth = width;
        ctx.beginPath();

        // Forward integration
        let curX = startX, curY = startY;
        ctx.moveTo(toScreenX(curX), toScreenY(curY));
        for (let step = 0; step < 240; step++) {
          if (curX > maxX || curY < minY || curY > maxY) break;
          const k1 = f(curX, curY);
          const k2 = f(curX + 0.5 * dt, curY + 0.5 * dt * k1);
          const k3 = f(curX + 0.5 * dt, curY + 0.5 * dt * k2);
          const k4 = f(curX + dt, curY + dt * k3);
          curY += (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
          curX += dt;
          ctx.lineTo(toScreenX(curX), toScreenY(curY));
        }
        ctx.stroke();

        // Backward integration
        curX = startX; curY = startY;
        ctx.beginPath();
        ctx.moveTo(toScreenX(curX), toScreenY(curY));
        for (let step = 0; step < 240; step++) {
          if (curX < minX || curY < minY || curY > maxY) break;
          const k1 = f(curX, curY);
          const k2 = f(curX - 0.5 * dt, curY - 0.5 * dt * k1);
          const k3 = f(curX - 0.5 * dt, curY - 0.5 * dt * k2);
          const k4 = f(curX - dt, curY - dt * k3);
          curY -= (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
          curX -= dt;
          ctx.lineTo(toScreenX(curX), toScreenY(curY));
        }
        ctx.stroke();
      };

      // Draw secondary streamlines for context
      [-1.5, -0.5, 0.5, 1.2, 1.8].forEach(ic => {
        drawStreamline(0, ic, "rgba(56, 189, 248, 0.25)", 1.2);
      });

      // Primary selected user trajectory
      drawStreamline(0, y0, "#38bdf8", 2.6);

      // Pulse circle on initial condition point (0, y0)
      const pulse = 4 + 2 * Math.sin(time * 0.005);
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(toScreenX(0), toScreenY(y0), pulse, 0, 2 * Math.PI);
      ctx.fill();

      // Info badge
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.strokeStyle = "#1e293b";
      ctx.lineWidth = 1;
      ctx.fillRect(65, 15, 340, 48);
      ctx.strokeRect(65, 15, 340, 48);

      const eqNames = ["Logistic: y' = y(1 - y)", "Linear: y' = x - y", "Riccati: y' = y² - x", "Non-Auto: y' = sin(x) - y"];
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(eqNames[eq], 75, 33);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Fira Code, monospace";
      ctx.fillText(`Initial Condition: (0, ${y0.toFixed(2)}) • RK4 dt=${dt}`, 75, 51);
    }
  },

  // 2. Exact Differential Equations & Potential Function Contour Plotter
  "ode1-exact-contour-sim": {
    title: "Exact Equations & Potential Function Level Curves Φ(x, y) = C",
    desc: "Visualizes the scalar potential field Φ(x, y) whose gradient yields the exact differential form M(x, y)dx + N(x, y)dy = 0, verifying ∂M/∂y = ∂N/∂x.",
    isAnimated: false,
    controls: [
      { id: "systemSel", label: "Potential Form (0: x²+y², 1: x³-3xy², 2: eˣsin(y), 3: x²y-y³)", min: 0, max: 3, step: 1, value: 0 },
      { id: "levelConst", label: "Target Contour Constant C", min: -8, max: 12, step: 0.5, value: 4 },
      { id: "numContours", label: "Contour Count", min: 6, max: 20, step: 2, value: 12 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const sys = Math.round(vals.systemSel || 0);
      const targetC = vals.levelConst !== undefined ? vals.levelConst : 4;
      const nContours = vals.numContours || 12;

      // Coordinate mapping [-3.5, 3.5] x [-3.5, 3.5]
      const minX = -3.5, maxX = 3.5, minY = -3.5, maxY = 3.5;
      const toScreenX = (x) => 55 + ((x - minX) / (maxX - minX)) * (w - 110);
      const toScreenY = (y) => (h - 45) - ((y - minY) / (maxY - minY)) * (h - 90);

      const phi = (x, y) => {
        if (sys === 0) return x * x + y * y; // Circles: 2x dx + 2y dy = 0
        if (sys === 1) return x * x * x - 3 * x * y * y; // Harmonic: (3x²-3y²)dx - 6xy dy = 0
        if (sys === 2) return Math.exp(x) * Math.sin(y); // Exponential: eˣsin y dx + eˣcos y dy = 0
        return x * x * y - (y * y * y) / 3; // Cubic: 2xy dx + (x²-y²) dy = 0
      };

      // Axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Marching squares / Grid contour approximation
      const res = 70;
      const dx = (maxX - minX) / res;
      const dy = (maxY - minY) / res;

      // Sample grid
      const grid = [];
      for (let i = 0; i <= res; i++) {
        grid[i] = [];
        const x = minX + i * dx;
        for (let j = 0; j <= res; j++) {
          const y = minY + j * dy;
          grid[i][j] = phi(x, y);
        }
      }

      // Generate a set of contour levels
      const levels = [];
      for (let k = 0; k < nContours; k++) {
        levels.push(-6 + (k / (nContours - 1)) * 18);
      }
      levels.push(targetC);

      // Draw Contours
      levels.forEach(lvl => {
        const isTarget = Math.abs(lvl - targetC) < 0.01;
        ctx.strokeStyle = isTarget ? "#10b981" : "rgba(56, 189, 248, 0.28)";
        ctx.lineWidth = isTarget ? 2.8 : 1.2;

        for (let i = 0; i < res; i++) {
          for (let j = 0; j < res; j++) {
            const v00 = grid[i][j] - lvl;
            const v10 = grid[i + 1][j] - lvl;
            const v01 = grid[i][j + 1] - lvl;
            const v11 = grid[i + 1][j + 1] - lvl;

            const x1 = minX + i * dx, x2 = x1 + dx;
            const y1 = minY + j * dy, y2 = y1 + dy;

            // Simplified linear interpolation segment
            const pts = [];
            if ((v00 > 0) !== (v10 > 0)) {
              const t = -v00 / (v10 - v00);
              pts.push({ x: x1 + t * dx, y: y1 });
            }
            if ((v10 > 0) !== (v11 > 0)) {
              const t = -v10 / (v11 - v10);
              pts.push({ x: x2, y: y1 + t * dy });
            }
            if ((v01 > 0) !== (v11 > 0)) {
              const t = -v01 / (v11 - v01);
              pts.push({ x: x1 + t * dx, y: y2 });
            }
            if ((v00 > 0) !== (v01 > 0)) {
              const t = -v00 / (v01 - v00);
              pts.push({ x: x1, y: y1 + t * dy });
            }

            if (pts.length >= 2) {
              ctx.beginPath();
              ctx.moveTo(toScreenX(pts[0].x), toScreenY(pts[0].y));
              ctx.lineTo(toScreenX(pts[1].x), toScreenY(pts[1].y));
              ctx.stroke();
            }
          }
        }
      });

      // Legend & Math details
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b";
      ctx.fillRect(65, 15, 380, 52);
      ctx.strokeRect(65, 15, 380, 52);

      const sysNames = [
        "Φ(x, y) = x² + y² = C  [M = 2x, N = 2y]",
        "Φ(x, y) = x³ - 3xy² = C  [Harmonic Potential]",
        "Φ(x, y) = eˣ sin(y) = C  [Exact Cauchy-Riemann]",
        "Φ(x, y) = x²y - y³/3 = C  [Cubic Exact Form]"
      ];
      ctx.fillStyle = "#10b981";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(sysNames[sys], 75, 33);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Fira Code, monospace";
      ctx.fillText(`Target Level Curve Φ = ${targetC.toFixed(1)} (Green) • ∂M/∂y ≡ ∂N/∂x`, 75, 52);
    }
  },

  // 3. Clairaut's Envelope & Singular Solution Generator
  "ode1-clairaut-envelope-sim": {
    title: "Clairaut's Family of Tangent Lines & The Singular Envelope Curve",
    desc: "Illustrates Clairaut's equation y = x p + f(p). The general solution family of straight lines y = c x + f(c) envelopes the non-linear singular solution curve.",
    isAnimated: false,
    controls: [
      { id: "clairautType", label: "Form f(p) (0: -p²/4 parabola, 1: 1/p hyperbola, 2: p³ cubic)", min: 0, max: 2, step: 1, value: 0 },
      { id: "lineCount", label: "Number of Tangent Lines", min: 10, max: 40, step: 2, value: 24 },
      { id: "cMax", label: "Parameter Span [-c, +c]", min: 2, max: 6, step: 0.5, value: 4 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const fType = Math.round(vals.clairautType || 0);
      const count = vals.lineCount || 24;
      const cRange = vals.cMax || 4;

      // Coordinate mapping [-5, 5] x [-5, 5]
      const minX = -5, maxX = 5, minY = -5, maxY = 5;
      const toScreenX = (x) => 55 + ((x - minX) / (maxX - minX)) * (w - 110);
      const toScreenY = (y) => (h - 45) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // f(p) and Envelope parametric equations:
      // x = -f'(p), y = f(p) - p f'(p)
      const f_p = (p) => {
        if (fType === 0) return -0.25 * p * p;   // y = x p - p²/4 -> envelope y = x²
        if (fType === 1) return 2 / (p || 0.001); // y = x p + 2/p -> envelope y² = 8x
        return 0.1 * p * p * p;                  // y = x p + 0.1 p³
      };

      // Draw General Solution Straight Lines: y = c x + f(c)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.28)";
      ctx.lineWidth = 1.2;

      for (let i = 0; i < count; i++) {
        const c = -cRange + (i / (count - 1)) * (2 * cRange);
        if (fType === 1 && Math.abs(c) < 0.2) continue; // avoid singularity

        const yLeft = c * minX + f_p(c);
        const yRight = c * maxX + f_p(c);

        ctx.beginPath();
        ctx.moveTo(toScreenX(minX), toScreenY(yLeft));
        ctx.lineTo(toScreenX(maxX), toScreenY(yRight));
        ctx.stroke();
      }

      // Draw Envelope (Singular Solution)
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 3.2;
      ctx.beginPath();

      const pSteps = 120;
      let first = true;
      for (let i = 0; i <= pSteps; i++) {
        const p = -cRange + (i / pSteps) * (2 * cRange);
        if (fType === 1 && Math.abs(p) < 0.15) continue;

        let envX, envY;
        if (fType === 0) {
          // f(p) = -p²/4 -> f'(p) = -p/2 -> x = p/2 => p = 2x, y = 2x² - x² = x²
          envX = 0.5 * p;
          envY = envX * envX;
        } else if (fType === 1) {
          // f(p) = 2/p -> f'(p) = -2/p² -> x = 2/p² -> y = 4/p
          envX = 2 / (p * p);
          envY = 4 / p;
        } else {
          // f(p) = 0.1 p³ -> f'(p) = 0.3 p² -> x = -0.3 p² -> y = -0.2 p³
          envX = -0.3 * p * p;
          envY = -0.2 * p * p * p;
        }

        const sx = toScreenX(envX), sy = toScreenY(envY);
        if (sx >= 55 && sx <= w - 55 && sy >= 45 && sy <= h - 45) {
          if (first) { ctx.moveTo(sx, sy); first = false; }
          else { ctx.lineTo(sx, sy); }
        } else {
          first = true;
        }
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b";
      ctx.fillRect(65, 15, 410, 52);
      ctx.strokeRect(65, 15, 410, 52);

      ctx.fillStyle = "#f59e0b";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Amber Curve: Singular Solution Envelope (dF/dp = 0)", 75, 33);
      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px Fira Code, monospace";
      ctx.fillText(`Cyan Lines: General Solution Family y = cx + f(c) [N=${count}]`, 75, 52);
    }
  },

  // 4. Mixing Tanks & Logistic Population Harvesting Simulator
  "ode1-firstorder-models-sim": {
    title: "Dynamic First-Order Modeling: Mixing Tanks & Logistic Harvesting",
    desc: "Simulates continuous mixture concentration dynamics dQ/dt = R_in - R_out and logistic population growth under harvesting dP/dt = rP(1 - P/K) - H.",
    isAnimated: true,
    controls: [
      { id: "modelMode", label: "Model Mode (0: Mixing Tank, 1: Logistic Harvesting)", min: 0, max: 1, step: 1, value: 0 },
      { id: "paramRate", label: "Flow Rate r / Growth Rate r", min: 1, max: 8, step: 0.5, value: 4 },
      { id: "paramConst", label: "Inflow Conc. Cin / Harvesting H", min: 0, max: 5, step: 0.25, value: 2 },
      { id: "initVal", label: "Initial State Q(0) or P(0)", min: 0, max: 100, step: 5, value: 10 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const mode = Math.round(vals.modelMode || 0);
      const r = vals.paramRate !== undefined ? vals.paramRate : 4;
      const c_in = vals.paramConst !== undefined ? vals.paramConst : 2;
      const y0 = vals.initVal !== undefined ? vals.initVal : 10;

      // Coordinate mapping: Time t in [0, 20]
      const minT = 0, maxT = 20;
      const maxY = mode === 0 ? 120 : 120;
      const toScreenX = (t) => 65 + (t / maxT) * (w - 130);
      const toScreenY = (y) => (h - 50) - (y / maxY) * (h - 100);

      // Grid
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let t = 0; t <= 20; t += 4) {
        ctx.beginPath(); ctx.moveTo(toScreenX(t), toScreenY(0)); ctx.lineTo(toScreenX(t), toScreenY(maxY)); ctx.stroke();
      }
      for (let y = 0; y <= maxY; y += 20) {
        ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(y)); ctx.lineTo(toScreenX(maxT), toScreenY(y)); ctx.stroke();
      }

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(0)); ctx.lineTo(toScreenX(maxT), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(0)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "11px Fira Code, monospace";
      ctx.fillText("Time t", toScreenX(maxT) - 20, toScreenY(0) + 18);
      ctx.fillText(mode === 0 ? "Salt Q(t) [kg]" : "Population P(t)", toScreenX(0) + 10, toScreenY(maxY) + 15);

      // Analytical Solutions:
      // Mode 0: Mixing Tank: V = 50 L, Inflow = Outflow = r L/min
      // dQ/dt = r * c_in - (r / 50) * Q -> Q(t) = 50*c_in + (Q0 - 50*c_in) * e^(-(r/50)*t)
      // Mode 1: Logistic: K = 100. dP/dt = (r/10) * P * (1 - P/100) - H
      ctx.lineWidth = 3;
      ctx.strokeStyle = mode === 0 ? "#38bdf8" : "#10b981";
      ctx.beginPath();

      const V = 50;
      const steadyQ = V * c_in;

      if (mode === 0) {
        for (let t = 0; t <= maxT; t += 0.1) {
          const Qt = steadyQ + (y0 - steadyQ) * Math.exp(-(r / V) * t);
          const sx = toScreenX(t), sy = toScreenY(Qt);
          if (t === 0) ctx.moveTo(sx, sy);
          else ctx.lineTo(sx, sy);
        }
      } else {
        // RK4 numerical simulation for logistic with harvesting
        let curP = y0;
        const dt = 0.05;
        const K = 100;
        const growthR = r / 10;
        const H = c_in * 3; // Harvesting magnitude
        ctx.moveTo(toScreenX(0), toScreenY(curP));

        for (let t = 0; t <= maxT; t += dt) {
          const dP = (p) => growthR * p * (1 - p / K) - H;
          const k1 = dP(curP);
          const k2 = dP(curP + 0.5 * dt * k1);
          const k3 = dP(curP + 0.5 * dt * k2);
          const k4 = dP(curP + dt * k3);
          curP += (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
          if (curP < 0) curP = 0;
          ctx.lineTo(toScreenX(t + dt), toScreenY(curP));
        }
      }
      ctx.stroke();

      // Steady state / Carrying capacity horizontal line
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 1.5;
      const asymptoteY = mode === 0 ? steadyQ : 100;
      ctx.beginPath();
      ctx.moveTo(toScreenX(0), toScreenY(asymptoteY));
      ctx.lineTo(toScreenX(maxT), toScreenY(asymptoteY));
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#f59e0b";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(mode === 0 ? `Equilibrium Q_inf = ${steadyQ.toFixed(1)} kg` : `Carrying Capacity K = 100`, toScreenX(8), toScreenY(asymptoteY) - 8);

      // Info box
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b";
      ctx.fillRect(70, 15, 380, 50);
      ctx.strokeRect(70, 15, 380, 50);

      ctx.fillStyle = mode === 0 ? "#38bdf8" : "#10b981";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(mode === 0 ? "Well-Stirred Mixture: dQ/dt = r·c_in - (r/V)·Q" : "Logistic Growth with Harvesting: dP/dt = rP(1-P/K) - H", 80, 32);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Fira Code, monospace";
      ctx.fillText(`State(0) = ${y0} • Rate r = ${r} • Input/Harvest = ${c_in}`, 80, 50);
    }
  },

  // 5. The Wronskian Determinant & Phase Space Independence Explorer
  "ode1-wronskian-sim": {
    title: "The Wronskian Determinant & Abel's Identity Explorer",
    desc: "Evaluates W(y1, y2)(x) = y1 y2' - y1' y2 and demonstrates Abel's formula W(x) = W(x0) exp(-∫ P(t) dt) for second-order linear differential equations.",
    isAnimated: true,
    controls: [
      { id: "dampingCoeff", label: "Damping Coefficient P", min: -1.0, max: 2.0, step: 0.1, value: 0.4 },
      { id: "freqOmega", label: "Frequency ω", min: 1.0, max: 4.0, step: 0.2, value: 2.0 },
      { id: "timeSpan", label: "Time Range t_max", min: 5, max: 15, step: 1, value: 10 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const P = vals.dampingCoeff !== undefined ? vals.dampingCoeff : 0.4;
      const omega = vals.freqOmega || 2.0;
      const tMax = vals.timeSpan || 10;

      // Coordinate mapping [0, tMax]
      const toScreenX = (t) => 65 + (t / tMax) * (w - 130);
      const toScreenY_y = (val) => 130 - (val / 3) * 80;
      const toScreenY_w = (wVal) => (h - 60) - (wVal / 4) * 80;

      // Divider between solutions and Wronskian
      ctx.strokeStyle = "#1e293b";
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(50, 180); ctx.lineTo(w - 50, 180); ctx.stroke();

      // Draw Sub-axis 1: Solutions y1, y2
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY_y(0)); ctx.lineTo(toScreenX(tMax), toScreenY_y(0)); ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Solutions y₁(t) [Cyan] & y₂(t) [Indigo]", toScreenX(0), 40);

      // Two fundamental solutions:
      // y'' + P y' + (ω² + P²/4) y = 0
      // y1(t) = e^(-Pt/2) cos(ωt), y2(t) = e^(-Pt/2) sin(ωt)
      // W(y1, y2)(t) = ω e^(-Pt)
      ctx.lineWidth = 2.2;

      // y1(t)
      ctx.strokeStyle = "#38bdf8";
      ctx.beginPath();
      for (let t = 0; t <= tMax; t += 0.05) {
        const y1 = Math.exp(-0.5 * P * t) * Math.cos(omega * t);
        const sx = toScreenX(t), sy = toScreenY_y(y1);
        if (t === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // y2(t)
      ctx.strokeStyle = "#818cf8";
      ctx.beginPath();
      for (let t = 0; t <= tMax; t += 0.05) {
        const y2 = Math.exp(-0.5 * P * t) * Math.sin(omega * t);
        const sx = toScreenX(t), sy = toScreenY_y(y2);
        if (t === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Draw Sub-axis 2: Wronskian W(t)
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY_w(0)); ctx.lineTo(toScreenX(tMax), toScreenY_w(0)); ctx.stroke();
      ctx.fillStyle = "#10b981";
      ctx.fillText("Wronskian W(y₁, y₂)(t) = ω · e^(-Pt)  [Abel's Identity]", toScreenX(0), 205);

      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 2.6;
      ctx.beginPath();
      for (let t = 0; t <= tMax; t += 0.05) {
        const W_t = omega * Math.exp(-P * t);
        const sx = toScreenX(t), sy = toScreenY_w(W_t);
        if (t === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Animate current inspection cursor
      const tNow = ((time * 0.001) % tMax);
      const curW = omega * Math.exp(-P * tNow);
      ctx.fillStyle = "#10b981";
      ctx.beginPath();
      ctx.arc(toScreenX(tNow), toScreenY_w(curW), 5, 0, 2 * Math.PI);
      ctx.fill();

      // Vertical marker
      ctx.setLineDash([3, 3]);
      ctx.strokeStyle = "rgba(16, 185, 129, 0.4)";
      ctx.beginPath();
      ctx.moveTo(toScreenX(tNow), 30);
      ctx.lineTo(toScreenX(tNow), h - 35);
      ctx.stroke();
      ctx.setLineDash([]);

      // Legend box
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b";
      ctx.fillRect(w - 280, 15, 240, 48);
      ctx.strokeRect(w - 280, 15, 240, 48);
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 11px Fira Code, monospace";
      ctx.fillText(`W(0) = ${omega.toFixed(2)}  (Non-zero => Indep.)`, w - 270, 32);
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`W(${tNow.toFixed(1)}) = ${curW.toFixed(3)} [Abel Exp.]`, w - 270, 49);
    }
  },

  // 6. Characteristic Roots Morphing & Phase State Trajectory
  "ode1-aux-roots-sim": {
    title: "Characteristic Roots Morphing & Second-Order Solution Regimes",
    desc: "Visualizes the roots of the auxiliary polynomial a r² + b r + c = 0 on the Complex Argand Plane and the resulting time-domain response y(t).",
    isAnimated: false,
    controls: [
      { id: "coeffA", label: "Inertia Coeff a", min: 1, max: 4, step: 0.5, value: 1 },
      { id: "coeffB", label: "Damping Coeff b", min: 0, max: 6, step: 0.2, value: 2 },
      { id: "coeffC", label: "Stiffness Coeff c", min: 1, max: 9, step: 0.5, value: 5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const a = vals.coeffA || 1;
      const b = vals.coeffB !== undefined ? vals.coeffB : 2;
      const c = vals.coeffC || 5;

      // Discriminant Δ = b² - 4ac
      const disc = b * b - 4 * a * c;

      // Left column: Complex plane [-4, 2] x [-4, 4]
      const planeW = w * 0.45;
      const cMinX = -4, cMaxX = 2, cMinY = -3.5, cMaxY = 3.5;
      const toPlaneX = (re) => 45 + ((re - cMinX) / (cMaxX - cMinX)) * (planeW - 70);
      const toPlaneY = (im) => (h - 45) - ((im - cMinY) / (cMaxY - cMinY)) * (h - 90);

      // Axes for Complex Plane
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(toPlaneX(cMinX), toPlaneY(0)); ctx.lineTo(toPlaneX(cMaxX), toPlaneY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toPlaneX(0), toPlaneY(cMinY)); ctx.lineTo(toPlaneX(0), toPlaneY(cMaxY)); ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Re(r)", toPlaneX(cMaxX) - 25, toPlaneY(0) + 15);
      ctx.fillText("Im(r)", toPlaneX(0) + 8, toPlaneY(cMaxY) + 15);
      ctx.fillText("Argand Complex Plane", 45, 30);

      // Compute Roots
      let r1_re, r1_im, r2_re, r2_im;
      if (disc >= 0) {
        r1_re = (-b + Math.sqrt(disc)) / (2 * a); r1_im = 0;
        r2_re = (-b - Math.sqrt(disc)) / (2 * a); r2_im = 0;
      } else {
        r1_re = -b / (2 * a); r1_im = Math.sqrt(-disc) / (2 * a);
        r2_re = -b / (2 * a); r2_im = -Math.sqrt(-disc) / (2 * a);
      }

      // Plot Roots
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(toPlaneX(r1_re), toPlaneY(r1_im), 6, 0, 2 * Math.PI); ctx.fill();
      ctx.beginPath(); ctx.arc(toPlaneX(r2_re), toPlaneY(r2_im), 6, 0, 2 * Math.PI); ctx.fill();

      // Right column: Time domain y(t)
      const graphX0 = planeW + 25;
      const graphW = w - graphX0 - 45;
      const tMax = 8;
      const toGraphX = (t) => graphX0 + (t / tMax) * graphW;
      const toGraphY = (y) => (h * 0.55) - (y / 2) * 80;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(toGraphX(0), toGraphY(0)); ctx.lineTo(toGraphX(tMax), toGraphY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toGraphX(0), 45); ctx.lineTo(toGraphX(0), h - 45); ctx.stroke();

      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Time Response y(t) with y(0)=1, y'(0)=0", graphX0, 30);

      // Plot y(t)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      for (let t = 0; t <= tMax; t += 0.05) {
        let yt;
        if (disc > 0.01) {
          // Overdamped
          const c1 = r2_re / (r2_re - r1_re);
          const c2 = -r1_re / (r2_re - r1_re);
          yt = c1 * Math.exp(r1_re * t) + c2 * Math.exp(r2_re * t);
        } else if (Math.abs(disc) <= 0.01) {
          // Critically damped
          const alpha = -b / (2 * a);
          yt = (1 - alpha * t) * Math.exp(alpha * t);
        } else {
          // Underdamped
          const alpha = r1_re, beta = r1_im;
          yt = Math.exp(alpha * t) * (Math.cos(beta * t) - (alpha / beta) * Math.sin(beta * t));
        }

        const sx = toGraphX(t), sy = toGraphY(yt);
        if (t === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Classification Badge
      let regimeName = "Underdamped (Complex Conjugate Roots)";
      let regimeColor = "#38bdf8";
      if (disc > 0.01) { regimeName = "Overdamped (Distinct Real Roots)"; regimeColor = "#f59e0b"; }
      else if (Math.abs(disc) <= 0.01) { regimeName = "Critically Damped (Repeated Real Root)"; regimeColor = "#10b981"; }

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b";
      ctx.fillRect(45, h - 38, w - 90, 30);
      ctx.strokeRect(45, h - 38, w - 90, 30);

      ctx.fillStyle = regimeColor;
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`Δ = b² - 4ac = ${disc.toFixed(2)} • ${regimeName}`, 55, h - 18);
    }
  },

  // 7. Method of Undetermined Coefficients & Resonance Beats
  "ode1-resonance-beats-sim": {
    title: "Forced Harmonic Oscillations: Beating & Secular Resonance",
    desc: "Simulates y'' + ω₀² y = F₀ cos(ω t). When driving frequency ω approaches natural frequency ω₀, beating occurs. At exact equality ω = ω₀, pure secular resonance builds without bound.",
    isAnimated: true,
    controls: [
      { id: "omega0", label: "Natural Freq ω₀", min: 1.0, max: 4.0, step: 0.2, value: 2.0 },
      { id: "omegaDriver", label: "Driving Freq ω", min: 1.0, max: 4.0, step: 0.1, value: 1.8 },
      { id: "forceAmp", label: "Force Amplitude F₀", min: 0.5, max: 3.0, step: 0.25, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const w0 = vals.omega0 || 2.0;
      const wD = vals.omegaDriver || 1.8;
      const F0 = vals.forceAmp || 1.5;

      const tMax = 35;
      const toScreenX = (t) => 55 + (t / tMax) * (w - 110);
      const toScreenY = (y) => (h * 0.52) - (y / 5) * 110;

      // Coordinate axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(0)); ctx.lineTo(toScreenX(tMax), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), 30); ctx.lineTo(toScreenX(0), h - 30); ctx.stroke();

      const isResonance = Math.abs(w0 - wD) < 0.05;

      // If not exact resonance:
      // y(t) = F0 / (w0² - wD²) * (cos(wD t) - cos(w0 t))
      //      = 2 F0 / (w0² - wD²) * sin((w0 - wD)t / 2) * sin((w0 + wD)t / 2)
      // If exact resonance:
      // y(t) = (F0 / (2 w0)) * t * sin(w0 t)

      // Envelope curves (dashed amber)
      if (!isResonance) {
        ctx.setLineDash([4, 4]);
        ctx.strokeStyle = "rgba(245, 158, 11, 0.4)";
        ctx.lineWidth = 1.5;

        const beatAmp = Math.abs((2 * F0) / (w0 * w0 - wD * wD));
        ctx.beginPath();
        for (let t = 0; t <= tMax; t += 0.1) {
          const env = beatAmp * Math.abs(Math.sin(0.5 * (w0 - wD) * t));
          const sx = toScreenX(t), sy = toScreenY(env);
          if (t === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        ctx.beginPath();
        for (let t = 0; t <= tMax; t += 0.1) {
          const env = -beatAmp * Math.abs(Math.sin(0.5 * (w0 - wD) * t));
          const sx = toScreenX(t), sy = toScreenY(env);
          if (t === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Main waveform y(t)
      ctx.strokeStyle = isResonance ? "#ef4444" : "#38bdf8";
      ctx.lineWidth = 2.2;
      ctx.beginPath();

      for (let t = 0; t <= tMax; t += 0.05) {
        let yt;
        if (isResonance) {
          yt = (F0 / (2 * w0)) * t * Math.sin(w0 * t);
        } else {
          yt = (F0 / (w0 * w0 - wD * wD)) * (Math.cos(wD * t) - Math.cos(w0 * t));
        }

        const sx = toScreenX(t), sy = toScreenY(yt);
        if (t === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Header Banner
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b";
      ctx.fillRect(60, 10, 420, 48);
      ctx.strokeRect(60, 10, 420, 48);

      ctx.fillStyle = isResonance ? "#ef4444" : "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(isResonance ? "⚠️ EXACT SECULAR RESONANCE (ω = ω₀): Linear Growth" : "BEATING PHENOMENON (ω ≈ ω₀): Modulated Envelope", 70, 28);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px Fira Code, monospace";
      const beatFreq = Math.abs(w0 - wD) / (2 * Math.PI);
      ctx.fillText(`ω₀ = ${w0.toFixed(2)} rad/s • ω = ${wD.toFixed(2)} rad/s • Beat Freq = ${beatFreq.toFixed(3)} Hz`, 70, 46);
    }
  },

  // 8. Damped Mechanical Oscillator, Phase Plane & Resonance Amplification Curve
  "ode1-damped-resonance-sim": {
    title: "Damped Driven Oscillator: Real-Time Phase Portrait & Frequency Response",
    desc: "Simulates m x'' + c x' + k x = F₀ cos(ω t). Demonstrates transient decay, steady-state response, phase plane orbits, and the resonance amplification curve M(ω).",
    isAnimated: true,
    controls: [
      { id: "mass", label: "Mass m (kg)", min: 0.5, max: 3.0, step: 0.25, value: 1.0 },
      { id: "damping", label: "Damping c (N·s/m)", min: 0.1, max: 2.0, step: 0.1, value: 0.3 },
      { id: "stiffness", label: "Spring k (N/m)", min: 2.0, max: 12.0, step: 0.5, value: 6.0 },
      { id: "driverOmega", label: "Driver Freq ω (rad/s)", min: 0.5, max: 5.0, step: 0.1, value: 2.4 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const m = vals.mass || 1.0;
      const c = vals.damping !== undefined ? vals.damping : 0.3;
      const k = vals.stiffness || 6.0;
      const wD = vals.driverOmega || 2.4;
      const F0 = 4.0;

      const w0 = Math.sqrt(k / m);
      const zeta = c / (2 * Math.sqrt(m * k));
      const resOmega = w0 * Math.sqrt(Math.max(0, 1 - 2 * zeta * zeta));

      // Left panel: Physical mass-spring & Phase plane (x vs v)
      const pW = w * 0.48;
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(40, 40, pW - 20, h - 80);

      // Phase Portrait in Left Box
      const cx = 40 + (pW - 20) / 2;
      const cy = 40 + (h - 80) / 2;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(50, cy); ctx.lineTo(40 + pW - 30, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, 50); ctx.lineTo(cx, h - 50); ctx.stroke();

      ctx.fillStyle = "#64748b"; ctx.font = "10px Fira Code, monospace";
      ctx.fillText("Position x", 40 + pW - 65, cy + 14);
      ctx.fillText("Velocity v", cx + 6, 60);

      // Right panel: Resonance Amplitude Curve M(ω) vs ω
      const rX = pW + 35;
      const rW = w - rX - 45;
      const rH = h - 100;
      const rY0 = h - 50;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(rX, rY0); ctx.lineTo(rX + rW, rY0); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(rX, rY0); ctx.lineTo(rX, 50); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Frequency Response Curve M(ω)", rX, 35);
      ctx.fillStyle = "#64748b"; ctx.font = "10px Fira Code, monospace";
      ctx.fillText("ω [rad/s]", rX + rW - 30, rY0 + 16);
      ctx.fillText("Amp A(ω)", rX + 6, 60);

      // Plot M(ω) = (F0 / m) / sqrt((w0² - w²)² + (c·w/m)²)
      const maxPlotW = 5.5;
      const ampAt = (omega) => (F0 / m) / Math.sqrt(Math.pow(w0 * w0 - omega * omega, 2) + Math.pow((c * omega) / m, 2));

      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 2.4;
      ctx.beginPath();
      const maxDisplayAmp = 8;

      for (let freq = 0.2; freq <= maxPlotW; freq += 0.05) {
        const A = ampAt(freq);
        const sx = rX + (freq / maxPlotW) * rW;
        const sy = rY0 - (Math.min(A, maxDisplayAmp) / maxDisplayAmp) * rH;
        if (freq === 0.2) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Current operational operating frequency marker
      const curAmp = ampAt(wD);
      const markX = rX + (wD / maxPlotW) * rW;
      const markY = rY0 - (Math.min(curAmp, maxDisplayAmp) / maxDisplayAmp) * rH;

      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(markX, markY, 6, 0, 2 * Math.PI); ctx.fill();

      ctx.setLineDash([3, 3]);
      ctx.strokeStyle = "rgba(56, 189, 248, 0.5)";
      ctx.beginPath(); ctx.moveTo(markX, rY0); ctx.lineTo(markX, markY); ctx.stroke();
      ctx.setLineDash([]);

      // Draw Phase Plane Orbit in Left Box
      const phi = Math.atan2((c * wD) / m, w0 * w0 - wD * wD);
      const orbitScale = 25;

      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath();

      for (let a = 0; a <= 2 * Math.PI; a += 0.05) {
        const xVal = curAmp * Math.cos(a - phi);
        const vVal = -curAmp * wD * Math.sin(a - phi);
        const px = cx + xVal * orbitScale;
        const py = cy - vVal * (orbitScale / (w0 || 1));
        if (a === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current moving state on orbit
      const curTimeSec = time * 0.003;
      const curX = curAmp * Math.cos(wD * curTimeSec - phi);
      const curV = -curAmp * wD * Math.sin(wD * curTimeSec - phi);
      const statePx = cx + curX * orbitScale;
      const statePy = cy - curV * (orbitScale / (w0 || 1));

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(statePx, statePy, 5, 0, 2 * Math.PI); ctx.fill();

      // Status text
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b";
      ctx.fillRect(45, h - 35, w - 90, 26);
      ctx.strokeRect(45, h - 35, w - 90, 26);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Fira Code, monospace";
      ctx.fillText(`ω₀ = ${w0.toFixed(2)} rad/s • Res. Peak ω_r = ${resOmega.toFixed(2)} rad/s • Current Amp A = ${curAmp.toFixed(2)} • ζ = ${zeta.toFixed(3)}`, 55, h - 18);
    }
  }
};

// Mount simulation function
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const simConfig = window.ODE1_SIMS[simType];
  if (!simConfig) {
    console.warn(`ODE1 Simulation '${simType}' not found.`);
    return;
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
  canvas.style.background = "#070c18";
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

  if (simConfig.isAnimated) {
    let animId;
    const animLoop = (ts) => {
      simConfig.render(canvas, currentVals, ts);
      animId = requestAnimationFrame(animLoop);
    };
    animId = requestAnimationFrame(animLoop);
  } else {
    simConfig.render(canvas, currentVals, 0);
  }
};
