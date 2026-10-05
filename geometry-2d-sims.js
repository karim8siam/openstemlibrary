// Two-Dimensional Coordinate Geometry & Conic Sections Simulation Suite
// 8 Real-Time 60 FPS Canvas Simulations for Analytic Geometry & Conics

window.GEOM2D_SIMS = {
  // 1. Dynamic Coordinate Translation & Rotation Explorer
  "geom2d-coord-transform-sim": {
    title: "Dynamic Coordinate Translation & Rotation Explorer",
    desc: "Visualizes rigid Euclidean transformations: translate origin to (h, k) and rotate axes by angle θ, demonstrating invariance of Euclidean distance and coordinate mappings.",
    isAnimated: false,
    controls: [
      { id: "shiftH", label: "Origin Shift h", min: -3.0, max: 3.0, step: 0.1, value: 1.5 },
      { id: "shiftK", label: "Origin Shift k", min: -3.0, max: 3.0, step: 0.1, value: 1.0 },
      { id: "angleDeg", label: "Rotation Angle θ (°)", min: 0, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const shH = vals.shiftH !== undefined ? vals.shiftH : 1.5;
      const shK = vals.shiftK !== undefined ? vals.shiftK : 1.0;
      const thetaDeg = vals.angleDeg !== undefined ? vals.angleDeg : 35;
      const theta = (thetaDeg * Math.PI) / 180;

      const minX = -5, maxX = 6, minY = -5, maxY = 6;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Base Grid
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let g = -4; g <= 5; g++) {
        ctx.beginPath(); ctx.moveTo(toScreenX(g), toScreenY(minY)); ctx.lineTo(toScreenX(g), toScreenY(maxY)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(g)); ctx.lineTo(toScreenX(maxX), toScreenY(g)); ctx.stroke();
      }

      // Base Axes Ox, Oy
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();
      ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("x", toScreenX(maxX) - 15, toScreenY(0) + 16);
      ctx.fillText("y", toScreenX(0) + 8, toScreenY(maxY) + 15);

      // Transformed Origin O'(h, k)
      const sox = toScreenX(shH), soy = toScreenY(shK);
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(sox, soy, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`O'(${shH.toFixed(1)}, ${shK.toFixed(1)})`, sox + 8, soy - 8);

      // Transformed Axes O'X, O'Y
      const axisLen = 4.5;
      const cosT = Math.cos(theta), sinT = Math.sin(theta);

      // New X-axis (direction (cosT, sinT))
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(toScreenX(shH - axisLen * cosT), toScreenY(shK - axisLen * sinT));
      ctx.lineTo(toScreenX(shH + axisLen * cosT), toScreenY(shK + axisLen * sinT));
      ctx.stroke();

      // New Y-axis (direction (-sinT, cosT))
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(toScreenX(shH + axisLen * sinT), toScreenY(shK - axisLen * cosT));
      ctx.lineTo(toScreenX(shH - axisLen * sinT), toScreenY(shK + axisLen * cosT));
      ctx.stroke();

      ctx.fillStyle = "#38bdf8"; ctx.fillText("X'", toScreenX(shH + axisLen * cosT) + 6, toScreenY(shK + axisLen * sinT));
      ctx.fillStyle = "#10b981"; ctx.fillText("Y'", toScreenX(shH - axisLen * sinT) - 15, toScreenY(shK + axisLen * cosT));

      // Test Point P in base coordinates
      const px = 3.5, py = 4.0;
      const spx = toScreenX(px), spy = toScreenY(py);

      // Compute coordinates in (X', Y') system:
      // X' = (x - h) cos θ + (y - k) sin θ
      // Y' = -(x - h) sin θ + (y - k) cos θ
      const dx = px - shH, dy = py - shK;
      const pXprime = dx * cosT + dy * sinT;
      const pYprime = -dx * sinT + dy * cosT;

      // Projections to old axes
      ctx.setLineDash([3, 3]); ctx.strokeStyle = "rgba(148, 163, 184, 0.4)"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(spx, spy); ctx.lineTo(spx, toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(spx, spy); ctx.lineTo(toScreenX(0), spy); ctx.stroke();

      // Projections to new axes
      const projX_x = shH + pXprime * cosT, projX_y = shK + pXprime * sinT;
      const projY_x = shH - pYprime * sinT, projY_y = shK + pYprime * cosT;
      ctx.strokeStyle = "rgba(56, 189, 248, 0.6)";
      ctx.beginPath(); ctx.moveTo(spx, spy); ctx.lineTo(toScreenX(projX_x), toScreenY(projX_y)); ctx.stroke();
      ctx.strokeStyle = "rgba(16, 185, 129, 0.6)";
      ctx.beginPath(); ctx.moveTo(spx, spy); ctx.lineTo(toScreenX(projY_x), toScreenY(projY_y)); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(spx, spy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`P: (x, y) = (${px.toFixed(1)}, ${py.toFixed(1)})`, spx + 8, spy - 8);

      // Info Header
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Rigid Transformation: Origin Translation O'(${shH.toFixed(2)}, ${shK.toFixed(2)}) & Rotation θ = ${thetaDeg}°`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Transformed Coordinates: (X', Y') = (${pXprime.toFixed(3)}, ${pYprime.toFixed(3)})`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      const distOld = Math.sqrt(dx * dx + dy * dy);
      const distNew = Math.sqrt(pXprime * pXprime + pYprime * pYprime);
      ctx.fillText(`Distance Invariance Verification: d(O', P) = √[(x-h)² + (y-k)²] = ${distOld.toFixed(4)} ≡ √(X'² + Y'²) = ${distNew.toFixed(4)}`, 65, 63);
    }
  },

  // 2. Pair of Straight Lines & Angle Bisectors Visualizer
  "geom2d-line-pair-sim": {
    title: "Pair of Straight Lines & Angle Bisectors Visualizer",
    desc: "Examines homogeneous quadratic equations ax² + 2hxy + by² = 0, computes individual lines, angle θ, and plots the perpendicular angle bisector pair.",
    isAnimated: false,
    controls: [
      { id: "paramA", label: "Coefficient a", min: -3.0, max: 3.0, step: 0.2, value: 2.0 },
      { id: "paramH", label: "Coefficient h", min: -3.0, max: 3.0, step: 0.2, value: 2.5 },
      { id: "paramB", label: "Coefficient b", min: -3.0, max: 3.0, step: 0.2, value: -2.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a = vals.paramA !== undefined ? vals.paramA : 2.0;
      const hVal = vals.paramH !== undefined ? vals.paramH : 2.5;
      let b = vals.paramB !== undefined ? vals.paramB : -2.0;
      if (Math.abs(b) < 0.01) b = 0.01;

      const D = hVal * hVal - a * b;

      const minX = -4, maxX = 4, minY = -4, maxY = 4;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      if (D >= 0) {
        const sqrtD = Math.sqrt(D);
        const m1 = (-hVal + sqrtD) / b;
        const m2 = (-hVal - sqrtD) / b;

        // Line 1 in cyan
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(toScreenX(minX), toScreenY(m1 * minX));
        ctx.lineTo(toScreenX(maxX), toScreenY(m1 * maxX));
        ctx.stroke();

        // Line 2 in amber
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(toScreenX(minX), toScreenY(m2 * minX));
        ctx.lineTo(toScreenX(maxX), toScreenY(m2 * maxX));
        ctx.stroke();

        // Angle Bisectors: (x^2 - y^2)/(a - b) = xy/h
        // h(x^2 - y^2) - (a - b)xy = 0 => h y^2 + (a - b)xy - h x^2 = 0
        // m_B = [-(a-b) +/- sqrt((a-b)^2 + 4h^2)] / (2h)
        if (Math.abs(hVal) > 0.01) {
          const bisectDisc = Math.sqrt((a - b) * (a - b) + 4 * hVal * hVal);
          const mb1 = (-(a - b) + bisectDisc) / (2 * hVal);
          const mb2 = (-(a - b) - bisectDisc) / (2 * hVal);

          ctx.setLineDash([4, 4]); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
          ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(mb1 * minX)); ctx.lineTo(toScreenX(maxX), toScreenY(mb1 * maxX)); ctx.stroke();
          ctx.strokeStyle = "#ec4899";
          ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(mb2 * minX)); ctx.lineTo(toScreenX(maxX), toScreenY(mb2 * maxX)); ctx.stroke();
          ctx.setLineDash([]);
        }

        // Angle between lines
        const acuteAngleRad = Math.atan(Math.abs(m1 - m2) / (1 + m1 * m2 >= 0 ? 1 + m1 * m2 : -(1 + m1 * m2)));
        const angleDeg = ((acuteAngleRad * 180) / Math.PI).toFixed(1);

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText(`Pair of Lines: ${a.toFixed(1)}x² + ${(2*hVal).toFixed(1)}xy + ${b.toFixed(1)}y² = 0 (h² - ab = ${D.toFixed(2)} ≥ 0)`, 65, 25);

        ctx.fillStyle = "#f59e0b"; ctx.font = "12px Inter, sans-serif";
        const perpNote = Math.abs(a + b) < 0.05 ? " (MUTUALLY PERPENDICULAR! a + b = 0)" : "";
        ctx.fillText(`Slopes: m₁ = ${m1.toFixed(3)}, m₂ = ${m2.toFixed(3)}  |  Included Angle θ = ${angleDeg}°${perpNote}`, 65, 45);

        ctx.fillStyle = "#10b981";
        ctx.fillText(`Angle Bisectors (Dashed Emerald/Pink): (x² - y²)/(${(a - b).toFixed(1)}) = xy/${hVal.toFixed(1)} (Always Orthogonal)`, 65, 63);
      } else {
        ctx.fillStyle = "#ef4444"; ctx.font = "bold 14px Inter, sans-serif";
        ctx.fillText(`Discriminant h² - ab = ${D.toFixed(3)} < 0: Imaginary lines with isolated real intersection (0, 0)`, 65, 45);
      }
    }
  },

  // 3. Radical Axis, Radical Center & Coaxial Circle System
  "geom2d-circle-radical-sim": {
    title: "Radical Axis, Radical Center & Coaxial Circle System",
    desc: "Visualizes the radical axis of two circles S₁ - S₂ = 0, verifies perpendicularity to the line of centers, and renders the coaxial system with limiting points.",
    isAnimated: false,
    controls: [
      { id: "r1", label: "Circle 1 Radius R₁", min: 1.0, max: 3.5, step: 0.1, value: 2.2 },
      { id: "r2", label: "Circle 2 Radius R₂", min: 1.0, max: 3.5, step: 0.1, value: 1.8 },
      { id: "dist", label: "Distance Between Centers", min: 2.5, max: 6.0, step: 0.1, value: 4.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const R1 = vals.r1 !== undefined ? vals.r1 : 2.2;
      const R2 = vals.r2 !== undefined ? vals.r2 : 1.8;
      const d = vals.dist !== undefined ? vals.dist : 4.0;

      // Center 1 at (-d/2, 0), Center 2 at (d/2, 0)
      const c1x = -d / 2, c2x = d / 2;

      // Circle 1: (x - c1x)^2 + y^2 = R1^2 => x^2 + y^2 - 2c1x*x + c1x^2 - R1^2 = 0
      // Circle 2: (x - c2x)^2 + y^2 = R2^2 => x^2 + y^2 - 2c2x*x + c2x^2 - R2^2 = 0
      // Radical axis S1 - S2 = 0:
      // 2(c2x - c1x)x + (c1x^2 - c2x^2) - (R1^2 - R2^2) = 0
      // 2(d)x + 0 - (R1^2 - R2^2) = 0 => x_rad = (R1^2 - R2^2) / (2d)
      const xRad = (R1 * R1 - R2 * R2) / (2 * d);

      const minX = -5, maxX = 5, minY = -4, maxY = 4;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Line of centers (y = 0)
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();

      // Circle 1 in cyan
      const sc1x = toScreenX(c1x), sc1y = toScreenY(0);
      const sR1 = (R1 / (maxX - minX)) * (w - 120);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.arc(sc1x, sc1y, sR1, 0, Math.PI * 2); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(sc1x, sc1y, 4, 0, Math.PI * 2); ctx.fill();

      // Circle 2 in amber
      const sc2x = toScreenX(c2x), sc2y = toScreenY(0);
      const sR2 = (R2 / (maxX - minX)) * (w - 120);
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.arc(sc2x, sc2y, sR2, 0, Math.PI * 2); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(sc2x, sc2y, 4, 0, Math.PI * 2); ctx.fill();

      // Radical Axis in glowing emerald
      const sRadX = toScreenX(xRad);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(sRadX, toScreenY(minY)); ctx.lineTo(sRadX, toScreenY(maxY)); ctx.stroke();

      // Test point P on radical axis at y = 2.5
      const py = 2.2;
      const spx = sRadX, spy = toScreenY(py);
      ctx.fillStyle = "#ec4899"; ctx.beginPath(); ctx.arc(spx, spy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`P(x_rad, ${py.toFixed(1)})`, spx + 8, spy - 6);

      // Tangents from P to C1 and C2
      const d1 = Math.sqrt((xRad - c1x) * (xRad - c1x) + py * py);
      const d2 = Math.sqrt((xRad - c2x) * (xRad - c2x) + py * py);
      const L1 = d1 > R1 ? Math.sqrt(d1 * d1 - R1 * R1) : 0;
      const L2 = d2 > R2 ? Math.sqrt(d2 * d2 - R2 * R2) : 0;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Radical Axis S₁ - S₂ = 0: Vertical Line x = ${xRad.toFixed(3)}`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Perpendicularity: Radical axis is strictly perpendicular to line of centers (y = 0)`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`Tangent Equality Verification from P: L₁ = √(d₁² - R₁²) = ${L1.toFixed(3)} ≡ L₂ = √(d₂² - R₂²) = ${L2.toFixed(3)}`, 65, 63);
    }
  },

  // 4. General Conic Discriminant & Canonical Morpher
  "geom2d-conic-discriminant-sim": {
    title: "General Conic Discriminant & Canonical Morpher",
    desc: "Visualizes the general second-degree conic ax² + 2hxy + by² + c = 0, calculating invariants Δ and D = ab - h² to morph from Ellipse (D > 0) to Parabola (D = 0) to Hyperbola (D < 0).",
    isAnimated: false,
    controls: [
      { id: "paramH", label: "Cross-term h", min: -2.0, max: 2.0, step: 0.1, value: 0.0 },
      { id: "paramB", label: "Coefficient b", min: -2.0, max: 2.0, step: 0.2, value: 1.0 },
      { id: "paramC", label: "Constant c", min: -8.0, max: -1.0, step: 0.5, value: -4.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a = 1.0;
      const hVal = vals.paramH !== undefined ? vals.paramH : 0.0;
      let b = vals.paramB !== undefined ? vals.paramB : 1.0;
      if (Math.abs(b) < 0.05) b = 0.05;
      const c = vals.paramC !== undefined ? vals.paramC : -4.0;

      const D = a * b - hVal * hVal;
      const I1 = a + b;

      const minX = -5, maxX = 5, minY = -5, maxY = 5;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Characteristic eigenvalues
      const trace = a + b;
      const disc = Math.sqrt(Math.max(0, (a - b) * (a - b) + 4 * hVal * hVal));
      const lam1 = (trace + disc) / 2;
      const lam2 = (trace - disc) / 2;

      let conicName = "General Conic";
      let conicColor = "#38bdf8";

      if (D > 0.05) {
        conicName = "Ellipse (D = ab - h² > 0)";
        conicColor = "#38bdf8";
      } else if (Math.abs(D) <= 0.05) {
        conicName = "Parabola (D = ab - h² ≈ 0)";
        conicColor = "#f59e0b";
      } else {
        conicName = "Hyperbola (D = ab - h² < 0)";
        conicColor = "#ec4899";
      }

      // Plot curve: solve quadratic in y for each x:
      // b y^2 + (2hx) y + (a x^2 + c) = 0
      ctx.strokeStyle = conicColor; ctx.lineWidth = 2.5;
      const steps = 300;
      for (let branch = 0; branch < 2; branch++) {
        ctx.beginPath();
        let started = false;
        for (let i = 0; i <= steps; i++) {
          const x = minX + (i / steps) * (maxX - minX);
          const quadA = b;
          const quadB = 2 * hVal * x;
          const quadC = a * x * x + c;
          const rad = quadB * quadB - 4 * quadA * quadC;
          if (rad >= 0) {
            const y = branch === 0 ? (-quadB + Math.sqrt(rad)) / (2 * quadA) : (-quadB - Math.sqrt(rad)) / (2 * quadA);
            if (y >= minY - 2 && y <= maxY + 2) {
              const sx = toScreenX(x), sy = toScreenY(y);
              if (!started) { ctx.moveTo(sx, sy); started = true; } else { ctx.lineTo(sx, sy); }
            } else { started = false; }
          } else { started = false; }
        }
        ctx.stroke();
      }

      // Header Readout
      ctx.fillStyle = conicColor; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`${conicName}: ${a.toFixed(1)}x² + ${(2*hVal).toFixed(1)}xy + ${b.toFixed(1)}y² + (${c.toFixed(1)}) = 0`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Discriminant Invariant: D = ab - h² = ${D.toFixed(3)}  |  Trace: a + b = ${I1.toFixed(2)}`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`Principal Eigenvalues: λ₁ = ${lam1.toFixed(3)}, λ₂ = ${lam2.toFixed(3)}  ⇒  Canonical Form: ${lam1.toFixed(2)}X'² + ${lam2.toFixed(2)}Y'² = ${(-c).toFixed(1)}`, 65, 63);
    }
  },

  // 5. Parabola Focus-Directrix & Optical Ray Tracing Engine
  "geom2d-parabola-optics-sim": {
    title: "Parabola Focus-Directrix & Optical Ray Tracing Engine",
    desc: "Demonstrates focus-directrix definition SP = PM, constant subnormal SN = 2a, and specular ray reflection toward the focus.",
    isAnimated: false,
    controls: [
      { id: "focalA", label: "Focal Parameter a", min: 0.5, max: 2.5, step: 0.1, value: 1.2 },
      { id: "paramT", label: "Point Parameter t", min: -2.0, max: 2.0, step: 0.1, value: 1.2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a = vals.focalA !== undefined ? vals.focalA : 1.2;
      const t = vals.paramT !== undefined ? vals.paramT : 1.2;

      const px = a * t * t, py = 2 * a * t;

      const minX = -3, maxX = 7, minY = -6, maxY = 6;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Directrix x = -a (dashed red)
      ctx.setLineDash([4, 4]); ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(-a), toScreenY(minY)); ctx.lineTo(toScreenX(-a), toScreenY(maxY)); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Directrix x = -${a.toFixed(1)}`, toScreenX(-a) + 8, toScreenY(minY) - 15);

      // Focus S(a, 0)
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(toScreenX(a), toScreenY(0), 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`Focus S(${a.toFixed(1)}, 0)`, toScreenX(a) + 8, toScreenY(0) + 16);

      // Parabola y^2 = 4ax
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let p = -2.8; p <= 2.8; p += 0.05) {
        const x = a * p * p, y = 2 * a * p;
        const sx = toScreenX(x), sy = toScreenY(y);
        if (p === -2.8) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Point P on curve
      const spx = toScreenX(px), spy = toScreenY(py);
      ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(spx, spy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`P(${px.toFixed(2)}, ${py.toFixed(2)})`, spx + 8, spy - 8);

      // Segments SP and PM
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(a), toScreenY(0)); ctx.lineTo(spx, spy); ctx.stroke();
      ctx.strokeStyle = "#ef4444";
      ctx.beginPath(); ctx.moveTo(spx, spy); ctx.lineTo(toScreenX(-a), spy); ctx.stroke();

      // Incoming parallel ray and reflected ray to focus
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(maxX), spy); ctx.lineTo(spx, spy); ctx.stroke();

      // Tangent line ty = x + at^2
      const mTan = 1 / (t !== 0 ? t : 0.01);
      ctx.setLineDash([3, 3]); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(toScreenX(px - 3), toScreenY(py - 3 * mTan));
      ctx.lineTo(toScreenX(px + 3), toScreenY(py + 3 * mTan));
      ctx.stroke();
      ctx.setLineDash([]);

      const SP_dist = Math.sqrt((px - a) * (px - a) + py * py);
      const PM_dist = px + a;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Parabola y² = 4ax (a = ${a.toFixed(1)}): Focus-Directrix & Optical Reflection Engine`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Locus Equality: SP = √[(x-a)²+y²] = ${SP_dist.toFixed(3)} ≡ PM = x + a = ${PM_dist.toFixed(3)}`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`Subnormal Invariant: MN = 2a = ${(2 * a).toFixed(2)} (Constant everywhere) | Ray reflects strictly through S(${a.toFixed(1)}, 0)`, 65, 63);
    }
  },

  // 6. Ellipse Auxiliary Circle, Conjugate Diameters & Foci Explorer
  "geom2d-ellipse-conjugate-sim": {
    title: "Ellipse Auxiliary Circle, Conjugate Diameters & Foci Explorer",
    desc: "Simulates the ellipse x²/a² + y²/b² = 1, auxiliary circle, eccentric angle φ, conjugate semi-diameters CP and CD, and verifies Apollonius' theorem CP² + CD² = a² + b².",
    isAnimated: false,
    controls: [
      { id: "semiA", label: "Major Semi-Axis a", min: 2.5, max: 4.5, step: 0.1, value: 3.5 },
      { id: "semiB", label: "Minor Semi-Axis b", min: 1.2, max: 3.0, step: 0.1, value: 2.0 },
      { id: "anglePhi", label: "Eccentric Angle φ (°)", min: 0, max: 360, step: 5, value: 45 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a = vals.semiA !== undefined ? vals.semiA : 3.5;
      const b = vals.semiB !== undefined ? vals.semiB : 2.0;
      const phiDeg = vals.anglePhi !== undefined ? vals.anglePhi : 45;
      const phi = (phiDeg * Math.PI) / 180;

      const minX = -5, maxX = 5, minY = -4, maxY = 4;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Auxiliary Circle x^2 + y^2 = a^2 (dashed grey)
      ctx.setLineDash([3, 3]); ctx.strokeStyle = "rgba(148, 163, 184, 0.4)"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let th = 0; th <= Math.PI * 2; th += 0.05) {
        const x = a * Math.cos(th), y = a * Math.sin(th);
        const sx = toScreenX(x), sy = toScreenY(y);
        if (th === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Ellipse x^2/a^2 + y^2/b^2 = 1 (cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let th = 0; th <= Math.PI * 2; th += 0.05) {
        const x = a * Math.cos(th), y = b * Math.sin(th);
        const sx = toScreenX(x), sy = toScreenY(y);
        if (th === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Point P(a cos φ, b sin φ) and Point D(-a sin φ, b cos φ)
      const px = a * Math.cos(phi), py = b * Math.sin(phi);
      const dx = -a * Math.sin(phi), dy = b * Math.cos(phi);

      const spx = toScreenX(px), spy = toScreenY(py);
      const sdx = toScreenX(dx), sdy = toScreenY(dy);
      const scx = toScreenX(0), scy = toScreenY(0);

      // Conjugate semi-diameters CP and CD
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(scx, scy); ctx.lineTo(spx, spy); ctx.stroke();
      ctx.strokeStyle = "#ec4899";
      ctx.beginPath(); ctx.moveTo(scx, scy); ctx.lineTo(sdx, sdy); ctx.stroke();

      ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(spx, spy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#ec4899"; ctx.beginPath(); ctx.arc(sdx, sdy, 6, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`P(${px.toFixed(2)}, ${py.toFixed(2)})`, spx + 8, spy - 8);
      ctx.fillStyle = "#ec4899";
      ctx.fillText(`D(${dx.toFixed(2)}, ${dy.toFixed(2)})`, sdx + 8, sdy - 8);

      // Foci S(ae, 0) and S'(-ae, 0)
      const e = Math.sqrt(Math.max(0, 1 - (b * b) / (a * a)));
      const ae = a * e;
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(toScreenX(ae), toScreenY(0), 4, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(toScreenX(-ae), toScreenY(0), 4, 0, Math.PI * 2); ctx.fill();

      const CP2 = px * px + py * py;
      const CD2 = dx * dx + dy * dy;
      const sumCP2_CD2 = CP2 + CD2;
      const exactA2_B2 = a * a + b * b;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Ellipse x²/${(a*a).toFixed(1)} + y²/${(b*b).toFixed(1)} = 1 (e = ${e.toFixed(3)}): Conjugate Diameters`, 65, 25);

      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Apollonius' 1st Theorem: CP² + CD² = ${sumCP2_CD2.toFixed(3)} ≡ a² + b² = ${exactA2_B2.toFixed(3)} (Invariant!)`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`Eccentric Angle φ = ${phiDeg}°  |  Area(Ellipse) = πab = ${(Math.PI * a * b).toFixed(2)}  |  Parallelogram Area = 4ab = ${(4 * a * b).toFixed(2)}`, 65, 63);
    }
  },

  // 7. Hyperbola Asymptotes & Equilateral xy = c^2 Visualizer
  "geom2d-hyperbola-asymptotes-sim": {
    title: "Hyperbola Asymptotes & Equilateral xy = c² Visualizer",
    desc: "Examines the hyperbola x²/a² - y²/b² = 1, its asymptotes y = ±(b/a)x, and the rectangular hyperbola xy = c² with constant tangent triangle area 2c².",
    isAnimated: false,
    controls: [
      { id: "semiA", label: "Semi-Axis a", min: 1.5, max: 3.5, step: 0.1, value: 2.5 },
      { id: "semiB", label: "Semi-Axis b", min: 1.2, max: 3.0, step: 0.1, value: 1.8 },
      { id: "viewMode", label: "Mode (0: Standard & Asymptotes, 1: xy = c²)", min: 0, max: 1, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a = vals.semiA !== undefined ? vals.semiA : 2.5;
      const b = vals.semiB !== undefined ? vals.semiB : 1.8;
      const mode = Math.round(vals.viewMode !== undefined ? vals.viewMode : 0);

      const minX = -6, maxX = 6, minY = -5, maxY = 5;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      if (mode === 0) {
        // Standard Hyperbola x^2/a^2 - y^2/b^2 = 1
        const slopeAsymp = b / a;

        // Asymptotes (dashed amber)
        ctx.setLineDash([4, 4]); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(-slopeAsymp * minX)); ctx.lineTo(toScreenX(maxX), toScreenY(slopeAsymp * maxX)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(slopeAsymp * minX)); ctx.lineTo(toScreenX(maxX), toScreenY(-slopeAsymp * maxX)); ctx.stroke();
        ctx.setLineDash([]);

        // Right & Left Branches
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        [-1, 1].forEach(sign => {
          ctx.beginPath();
          for (let p = -2.2; p <= 2.2; p += 0.05) {
            const x = sign * a * Math.cosh(p), y = b * Math.sinh(p);
            const sx = toScreenX(x), sy = toScreenY(y);
            if (p === -2.2) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
          }
          ctx.stroke();
        });

        const e = Math.sqrt(1 + (b * b) / (a * a));
        const asympAngle = (2 * Math.atan(b / a) * 180 / Math.PI).toFixed(1);

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText(`Hyperbola: x²/${(a*a).toFixed(1)} - y²/${(b*b).toFixed(1)} = 1 (Eccentricity e = ${e.toFixed(3)})`, 65, 25);

        ctx.fillStyle = "#f59e0b"; ctx.font = "12px Inter, sans-serif";
        ctx.fillText(`Asymptotes (Dashed Amber): y = ±${slopeAsymp.toFixed(2)}x  |  Angle Between Asymptotes: 2θ = ${asympAngle}°`, 65, 45);

        ctx.fillStyle = "#e2e8f0";
        ctx.fillText(`Foci at (±${(a*e).toFixed(2)}, 0)  |  Directrices at x = ±${(a/e).toFixed(2)}`, 65, 63);
      } else {
        // Mode 1: Rectangular Hyperbola xy = c^2
        const cVal = 2.0;
        const c2 = cVal * cVal;

        // Plot xy = c^2
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        [1, -1].forEach(branch => {
          ctx.beginPath();
          for (let i = 1; i <= 100; i++) {
            const x = branch * (0.3 + (i / 100) * 5.0);
            const y = c2 / x;
            const sx = toScreenX(x), sy = toScreenY(y);
            if (i === 1) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
          }
          ctx.stroke();
        });

        // Test Tangent at t = 1.3: P(ct, c/t)
        const tVal = 1.3;
        const px = cVal * tVal, py = cVal / tVal;
        const spx = toScreenX(px), spy = toScreenY(py);

        // Tangent intercepts: A(2ct, 0), B(0, 2c/t)
        const ax = 2 * cVal * tVal, by = 2 * cVal / tVal;
        const sax = toScreenX(ax), say = toScreenY(0);
        const sbx = toScreenX(0), sby = toScreenY(by);

        // Tangent Line in glowing emerald
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(sax, say); ctx.lineTo(sbx, sby); ctx.stroke();

        // Shaded Triangle OAB
        ctx.fillStyle = "rgba(16, 185, 129, 0.15)";
        ctx.beginPath();
        ctx.moveTo(toScreenX(0), toScreenY(0));
        ctx.lineTo(sax, say);
        ctx.lineTo(sbx, sby);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(spx, spy, 6, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText(`Rectangular Hyperbola: xy = c² (c = ${cVal.toFixed(1)}, e = √2 ≈ 1.414)`, 65, 25);

        ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
        ctx.fillText(`Constant Triangle Area Theorem: Area(ΔOAB) = ½(2ct)(2c/t) = 2c² = ${(2 * c2).toFixed(2)} (Invariant!)`, 65, 45);

        ctx.fillStyle = "#e2e8f0";
        ctx.fillText(`Midpoint Bisection: Point of Contact P(${px.toFixed(2)}, ${py.toFixed(2)}) exactly bisects tangent segment AB`, 65, 63);
      }
    }
  },

  // 8. Universal Polar Conic & Keplerian Orbit Simulator
  "geom2d-polar-conic-kepler-sim": {
    title: "Universal Polar Conic & Keplerian Orbit Simulator",
    desc: "Interactive focal conic l/r = 1 + e cos θ morphing smoothly from Circle (e = 0) to Ellipse (e < 1) to Parabola (e = 1) to Hyperbola (e > 1), illustrating celestial Keplerian orbits.",
    isAnimated: false,
    controls: [
      { id: "ecc", label: "Eccentricity e", min: 0.0, max: 2.0, step: 0.05, value: 0.6 },
      { id: "latus", label: "Semi-Latus Rectum l", min: 1.5, max: 4.5, step: 0.1, value: 2.8 },
      { id: "trueAnom", label: "True Anomaly θ (°)", min: -150, max: 150, step: 5, value: 45 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const e = vals.ecc !== undefined ? vals.ecc : 0.6;
      const l = vals.latus !== undefined ? vals.latus : 2.8;
      const thetaDeg = vals.trueAnom !== undefined ? vals.trueAnom : 45;
      const thetaRad = (thetaDeg * Math.PI) / 180;

      const minX = -6, maxX = 6, minY = -5, maxY = 5;
      const toScreenX = (x) => 60 + ((x - minX) / (maxX - minX)) * (w - 120);
      const toScreenY = (y) => (h - 50) - ((y - minY) / (maxY - minY)) * (h - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(minX), toScreenY(0)); ctx.lineTo(toScreenX(maxX), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(minY)); ctx.lineTo(toScreenX(0), toScreenY(maxY)); ctx.stroke();

      // Pole O (Central Gravitational Body in Gold)
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(toScreenX(0), toScreenY(0), 7, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Pole / Focus S(0, 0)", toScreenX(0) + 10, toScreenY(0) + 16);

      // Plot Conic Curve: r = l / (1 + e cos θ)
      let conicType = "Ellipse (Bound Closed Orbit)";
      let strokeColor = "#38bdf8";

      if (e === 0) {
        conicType = "Circle (e = 0, Perfectly Symmetric Orbit)";
      } else if (e < 1.0) {
        conicType = "Ellipse (0 < e < 1, Bound Periodic Orbit)";
      } else if (Math.abs(e - 1.0) < 0.02) {
        conicType = "Parabola (e = 1, Critical Escape Trajectory)";
        strokeColor = "#f59e0b";
      } else {
        conicType = "Hyperbola (e > 1, Unbound Interstellar Flyby)";
        strokeColor = "#ec4899";
      }

      ctx.strokeStyle = strokeColor; ctx.lineWidth = 2.5;
      ctx.beginPath();
      let started = false;
      const maxTh = e >= 1.0 ? Math.acos(-1 / e) - 0.08 : Math.PI;

      for (let th = -maxTh; th <= maxTh; th += 0.02) {
        const denom = 1 + e * Math.cos(th);
        if (denom > 0.02) {
          const r = l / denom;
          const x = r * Math.cos(th), y = r * Math.sin(th);
          if (x >= minX - 2 && x <= maxX + 2 && y >= minY - 2 && y <= maxY + 2) {
            const sx = toScreenX(x), sy = toScreenY(y);
            if (!started) { ctx.moveTo(sx, sy); started = true; } else { ctx.lineTo(sx, sy); }
          } else { started = false; }
        } else { started = false; }
      }
      ctx.stroke();

      // Current evaluation point P(r, θ)
      const curDenom = 1 + e * Math.cos(thetaRad);
      if (curDenom > 0.01) {
        const curR = l / curDenom;
        const curX = curR * Math.cos(thetaRad), curY = curR * Math.sin(thetaRad);
        const spx = toScreenX(curX), spy = toScreenY(curY);

        // Focal radius vector
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(0)); ctx.lineTo(spx, spy); ctx.stroke();

        ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(spx, spy, 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(`P: r = ${curR.toFixed(2)}, θ = ${thetaDeg}°`, spx + 8, spy - 8);
      }

      // Readouts
      ctx.fillStyle = strokeColor; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Universal Conic: l/r = 1 + e cos θ (l = ${l.toFixed(1)}, e = ${e.toFixed(2)}) — ${conicType}`, 65, 25);

      const rPeri = (l / (1 + e)).toFixed(2);
      const rApo = e < 1.0 ? (l / (1 - e)).toFixed(2) : "∞ (Unbound)";
      ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Periapsis r_min = l/(1+e) = ${rPeri}  |  Apoapsis r_max = l/(1-e) = ${rApo}`, 65, 45);

      ctx.fillStyle = "#e2e8f0";
      const energySign = e < 1 ? "E < 0 (Bound)" : (e === 1 ? "E = 0 (Parabolic Escape)" : "E > 0 (Hyperbolic Flyby)");
      ctx.fillText(`Orbital Energy: ${energySign} | Semi-latus rectum is harmonic mean of focal segments`, 65, 63);
    }
  }
};

// Simulation Engine Integration for 2D Geometry
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

const origGeom2dInit = window.SimulationEngine.initSimulation;
window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const simConfig = (window.GEOM2D_SIMS && window.GEOM2D_SIMS[simType]) ||
                    (window.CALC1_SIMS && window.CALC1_SIMS[simType]) ||
                    (window.RP_SIMS && window.RP_SIMS[simType]);

  if (!simConfig) {
    if (origGeom2dInit) {
      origGeom2dInit(containerId, simType);
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
