import os

print("Writing calculus-2-sims.js...")

sims_code = r'''// Calculus II Simulation Suite
// 8 Real-Time 60 FPS Canvas Simulations for University Integral Calculus & Series Analysis

window.CALC2_SIMS = {
  // 1. Trigonometric Reduction & Wallis Integrals Engine
  "sim_calc2_reduction": {
    title: "Trigonometric Reduction & Wallis Integrals Engine",
    desc: "Adjust the power exponent n for Iₙ = ∫₀^(π/2) sinⁿ(x) dx. Observe the non-linear flattening of the wave, the step-by-step recurrence reduction Iₙ = ((n-1)/n) Iₙ₋₂, and the convergence of Wallis' ratio toward 1.",
    isAnimated: false,
    controls: [
      { id: "n", label: "Power Exponent (n)", min: 1, max: 10, step: 1, value: 4 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const n = Math.round(vals.n !== undefined ? vals.n : 4);

      // Coordinate mapping [0, pi/2] -> [60, w - 60], [0, 1.2] -> [h - 60, 50]
      const toScreenX = (x) => 70 + (x / (Math.PI / 2)) * (w - 140);
      const toScreenY = (y) => (h - 70) - (y / 1.15) * (h - 130);

      // Grid & Axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let gy = 0.2; gy <= 1.0; gy += 0.2) {
        ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(gy)); ctx.lineTo(toScreenX(Math.PI / 2), toScreenY(gy)); ctx.stroke();
      }

      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(0)); ctx.lineTo(toScreenX(Math.PI / 2), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(0)); ctx.lineTo(toScreenX(0), toScreenY(1.1)); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("0", toScreenX(0) - 15, toScreenY(0) + 15);
      ctx.fillText("π/4", toScreenX(Math.PI / 4) - 8, toScreenY(0) + 18);
      ctx.fillText("π/2", toScreenX(Math.PI / 2) - 8, toScreenY(0) + 18);
      ctx.fillText("1.0", toScreenX(0) - 30, toScreenY(1.0) + 4);
      ctx.fillText("y = sinⁿ(x)", toScreenX(0) + 10, toScreenY(1.1) + 10);

      // Shaded Area under sin^n(x)
      ctx.beginPath();
      ctx.moveTo(toScreenX(0), toScreenY(0));
      for (let s = 0; s <= 200; s++) {
        const x = (s / 200) * (Math.PI / 2);
        const y = Math.pow(Math.sin(x), n);
        ctx.lineTo(toScreenX(x), toScreenY(y));
      }
      ctx.lineTo(toScreenX(Math.PI / 2), toScreenY(0));
      ctx.closePath();
      const grad = ctx.createLinearGradient(0, toScreenY(1), 0, toScreenY(0));
      grad.addColorStop(0, "rgba(56, 189, 248, 0.45)");
      grad.addColorStop(1, "rgba(56, 189, 248, 0.05)");
      ctx.fillStyle = grad;
      ctx.fill();

      // Curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let s = 0; s <= 200; s++) {
        const x = (s / 200) * (Math.PI / 2);
        const y = Math.pow(Math.sin(x), n);
        if (s === 0) ctx.moveTo(toScreenX(x), toScreenY(y));
        else ctx.lineTo(toScreenX(x), toScreenY(y));
      }
      ctx.stroke();

      // Compute exact Wallis integral W_n
      function wallis(k) {
        if (k === 0) return Math.PI / 2;
        if (k === 1) return 1.0;
        let val = (k % 2 === 0) ? (Math.PI / 2) : 1.0;
        for (let i = k; i >= 2; i -= 2) {
          val *= (i - 1) / i;
        }
        return val;
      }

      const exactVal = wallis(n);
      const isEven = (n % 2 === 0);
      let fracStr = "";
      if (n === 1) fracStr = "1";
      else if (n === 2) fracStr = "π / 4";
      else if (n === 3) fracStr = "2 / 3";
      else if (n === 4) fracStr = "3π / 16";
      else if (n === 5) fracStr = "8 / 15";
      else if (n === 6) fracStr = "5π / 32";
      else if (n === 7) fracStr = "16 / 35";
      else if (n === 8) fracStr = "35π / 256";
      else if (n === 9) fracStr = "128 / 315";
      else fracStr = "63π / 512";

      // Wall panel readout
      const px = w - 240, py = 50;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1;
      ctx.fillRect(px, py, 220, 140);
      ctx.strokeRect(px, py, 220, 140);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Wallis Integral (n = ${n})`, px + 12, py + 22);

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Exact I_${n} = ${fracStr}`, px + 12, py + 48);
      ctx.fillText(`Numerical Value ≈ ${exactVal.toFixed(5)}`, px + 12, py + 70);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Parity: ${isEven ? 'Even (π factor)' : 'Odd (rational)'}`, px + 12, py + 95);
      const recFactor = n >= 2 ? `${n - 1}/${n}` : 'Base';
      ctx.fillText(`Recurrence: I_${n} = (${recFactor}) · I_${n >= 2 ? n - 2 : '0'}`, px + 12, py + 118);
    }
  },

  // 2. Riemann Sum Convergence & Error Decay Engine
  "sim_calc2_riemann": {
    title: "Riemann Sum Convergence & Error Decay Engine",
    desc: "Compare Left, Right, Midpoint, and Trapezoidal sums for f(x) = x³ - 2x + 2 on [0, 2]. Drag partition slider N to trace convergence toward the exact analytical integral I = 4.0.",
    isAnimated: false,
    controls: [
      { id: "method", label: "Rule (1=Left, 2=Right, 3=Midpoint, 4=Trap)", min: 1, max: 4, step: 1, value: 3 },
      { id: "n", label: "Partitions (N)", min: 2, max: 60, step: 1, value: 12 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const method = Math.round(vals.method !== undefined ? vals.method : 3);
      const N = Math.round(vals.n !== undefined ? vals.n : 12);

      const f = (x) => Math.pow(x, 3) - 2 * x + 2;
      const a = 0, b = 2;
      // Exact integral: ∫₀² (x³ - 2x + 2) dx = [x⁴/4 - x² + 2x]₀² = (16/4 - 4 + 4) = 4.0
      const exactI = 4.0;

      const toScreenX = (x) => 70 + (x / 2.2) * (w - 140);
      const toScreenY = (y) => (h - 70) - (y / 7.0) * (h - 130);

      // Axes & grid
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let gy = 1; gy <= 6; gy++) {
        ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(gy)); ctx.lineTo(toScreenX(2.2), toScreenY(gy)); ctx.stroke();
      }

      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(0)); ctx.lineTo(toScreenX(2.2), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(0)); ctx.lineTo(toScreenX(0), toScreenY(6.5)); ctx.stroke();

      const dx = (b - a) / N;
      let approxSum = 0;

      const ruleName = method === 1 ? "Left Riemann" : (method === 2 ? "Right Riemann" : (method === 3 ? "Midpoint Rule" : "Trapezoidal Rule"));
      const fillColor = method === 3 ? "rgba(56, 189, 248, 0.35)" : (method === 4 ? "rgba(16, 185, 129, 0.35)" : "rgba(245, 158, 11, 0.35)");
      const strokeColor = method === 3 ? "#38bdf8" : (method === 4 ? "#10b981" : "#f59e0b");

      // Draw Riemann Rectangles or Trapezoids
      for (let i = 0; i < N; i++) {
        const xLeft = a + i * dx;
        const xRight = a + (i + 1) * dx;
        const sxL = toScreenX(xLeft), sxR = toScreenX(xRight);
        const sy0 = toScreenY(0);

        if (method === 4) {
          // Trapezoidal
          const yL = f(xLeft), yR = f(xRight);
          approxSum += 0.5 * (yL + yR) * dx;
          const syL = toScreenY(yL), syR = toScreenY(yR);

          ctx.fillStyle = fillColor;
          ctx.beginPath();
          ctx.moveTo(sxL, sy0);
          ctx.lineTo(sxL, syL);
          ctx.lineTo(sxR, syR);
          ctx.lineTo(sxR, sy0);
          ctx.closePath();
          ctx.fill();

          ctx.strokeStyle = strokeColor; ctx.lineWidth = 1;
          ctx.stroke();
        } else {
          // Rectangular rules
          let evalX = xLeft;
          if (method === 2) evalX = xRight;
          else if (method === 3) evalX = 0.5 * (xLeft + xRight);

          const hVal = f(evalX);
          approxSum += hVal * dx;
          const syH = toScreenY(hVal);

          ctx.fillStyle = fillColor;
          ctx.fillRect(sxL, syH, sxR - sxL, sy0 - syH);

          ctx.strokeStyle = strokeColor; ctx.lineWidth = 1;
          ctx.strokeRect(sxL, syH, sxR - sxL, sy0 - syH);
        }
      }

      // Exact curve
      ctx.strokeStyle = "#f8fafc"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let s = 0; s <= 200; s++) {
        const x = (s / 200) * 2.15;
        const y = f(x);
        if (s === 0) ctx.moveTo(toScreenX(x), toScreenY(y));
        else ctx.lineTo(toScreenX(x), toScreenY(y));
      }
      ctx.stroke();

      // Readout panel
      const err = Math.abs(approxSum - exactI);
      const px = w - 240, py = 45;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1;
      ctx.fillRect(px, py, 220, 145);
      ctx.strokeRect(px, py, 220, 145);

      ctx.fillStyle = strokeColor; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`${ruleName} (N = ${N})`, px + 12, py + 22);

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Exact Integral I = ${exactI.toFixed(4)}`, px + 12, py + 48);
      ctx.fillText(`Sum S_N = ${approxSum.toFixed(4)}`, px + 12, py + 70);

      ctx.fillStyle = err < 0.05 ? "#10b981" : "#f59e0b";
      ctx.fillText(`Absolute Error = ${err.toFixed(5)}`, px + 12, py + 95);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Step Width Δx = ${(2.0 / N).toFixed(4)}`, px + 12, py + 120);
    }
  },

  // 3. Solids of Revolution: Disk vs Cylindrical Shell Slicer
  "sim_calc2_solids": {
    title: "Solids of Revolution: Disk vs Cylindrical Shell Slicer",
    desc: "Revolve y = √x on [0, 4] around horizontal axis y = 0 (Disk Method) or around vertical axis x = 5 (Cylindrical Shell Method). Sweep rotation angle and slice location to observe 3D volume accumulation.",
    isAnimated: false,
    controls: [
      { id: "method", label: "Method (1=Disk y=0, 2=Shell x=5)", min: 1, max: 2, step: 1, value: 1 },
      { id: "sweep", label: "Rotation Sweep (rad)", min: 0.5, max: 6.28, step: 0.2, value: 5.2 },
      { id: "sliceX", label: "Active Slice (x)", min: 0.5, max: 3.8, step: 0.1, value: 2.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const method = Math.round(vals.method !== undefined ? vals.method : 1);
      const sweep = vals.sweep !== undefined ? vals.sweep : 5.2;
      const sliceX = vals.sliceX !== undefined ? vals.sliceX : 2.5;

      const cx = w * 0.45, cy = h * 0.52;
      const scaleX = 75, scaleY = 45;

      // Draw 3D revolved wireframe
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      const numRings = 12;

      if (method === 1) {
        // Disk method around x-axis
        // V = π ∫₀⁴ (√x)² dx = π [x²/2]₀⁴ = 8π ≈ 25.1327
        for (let i = 1; i <= numRings; i++) {
          const x = (i / numRings) * 4.0;
          const r = Math.sqrt(x);
          const px = cx + (x - 2) * scaleX;

          ctx.beginPath();
          ctx.ellipse(px, cy, r * 12, r * scaleY, 0, 0, sweep);
          ctx.strokeStyle = "rgba(56, 189, 248, 0.25)";
          ctx.stroke();
        }

        // Highlight active disk slice
        const activeR = Math.sqrt(sliceX);
        const activePx = cx + (sliceX - 2) * scaleX;
        ctx.beginPath();
        ctx.ellipse(activePx, cy, activeR * 12, activeR * scaleY, 0, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(245, 158, 11, 0.35)";
        ctx.fill();
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
        ctx.stroke();

        // Rotation axis
        ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(cx - 180, cy); ctx.lineTo(cx + 200, cy); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Rotation Axis: y = 0 (x-axis)", cx - 180, cy - 10);
      } else {
        // Shell method around vertical line x = 5
        // V = 2π ∫₀⁴ (5 - x)√x dx = 2π [10/3 x^(3/2) - 2/5 x^(5/2)]₀⁴ = 2π(80/3 - 64/5) = 2π(208/15) = 416π/15 ≈ 87.1268
        const axisPx = cx + (5 - 2) * scaleX;

        // Draw shells
        for (let i = 1; i <= numRings; i++) {
          const x = (i / numRings) * 4.0;
          const radius = (5 - x);
          const hVal = Math.sqrt(x);

          ctx.beginPath();
          ctx.ellipse(axisPx, cy, radius * 35, radius * 14, 0, 0, sweep);
          ctx.strokeStyle = "rgba(16, 185, 129, 0.25)";
          ctx.stroke();
        }

        // Active shell
        const activeRadius = (5 - sliceX);
        const activeH = Math.sqrt(sliceX);
        ctx.beginPath();
        ctx.ellipse(axisPx, cy - activeH * 15, activeRadius * 35, activeRadius * 14, 0, 0, Math.PI * 2);
        ctx.ellipse(axisPx, cy + activeH * 15, activeRadius * 35, activeRadius * 14, 0, 0, Math.PI * 2);
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
        ctx.stroke();

        // Rotation axis
        ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(axisPx, cy - 120); ctx.lineTo(axisPx, cy + 120); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Axis: x = 5", axisPx + 8, cy - 100);
      }

      // Information readout
      const px = w - 240, py = 45;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(px, py, 220, 150);
      ctx.strokeRect(px, py, 220, 150);

      ctx.fillStyle = method === 1 ? "#38bdf8" : "#10b981"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(method === 1 ? "Disk Method (y = 0)" : "Shell Method (x = 5)", px + 12, py + 22);

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px Inter, sans-serif";
      const totalV = method === 1 ? 8 * Math.PI : (416 * Math.PI / 15);
      const totalStr = method === 1 ? "8π ≈ 25.133" : "416π/15 ≈ 87.127";
      ctx.fillText(`Total Volume V = ${totalStr}`, px + 12, py + 48);

      ctx.fillStyle = "#cbd5e1";
      if (method === 1) {
        ctx.fillText(`Active Radius R(x) = √${sliceX.toFixed(1)} = ${Math.sqrt(sliceX).toFixed(2)}`, px + 12, py + 72);
        ctx.fillText(`Slice dV = π·R²·dx = π(${sliceX.toFixed(1)})dx`, px + 12, py + 95);
      } else {
        ctx.fillText(`Shell Radius r = 5 - ${sliceX.toFixed(1)} = ${(5 - sliceX).toFixed(1)}`, px + 12, py + 72);
        ctx.fillText(`Shell Height h = √${sliceX.toFixed(1)} = ${Math.sqrt(sliceX).toFixed(2)}`, px + 12, py + 95);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Rotation: ${(sweep * 180 / Math.PI).toFixed(0)}° / 360°`, px + 12, py + 122);
    }
  },

  // 4. Polar Curve Tracing & Sector Area Sweep Engine
  "sim_calc2_polar": {
    title: "Polar Curve Tracing & Sector Area Sweep Engine",
    desc: "Trace classical polar curves (Cardioid, Rose Curve, Limaçon, Lemniscate). Sweep the polar angle θ ∈ [0, 2π] to visualize the radius vector r(θ), tangent line, angle ψ satisfying tan ψ = r / (dr/dθ), and cumulative shaded sector area.",
    isAnimated: false,
    controls: [
      { id: "curve", label: "Curve (1=Cardioid, 2=Rose, 3=Limaçon)", min: 1, max: 3, step: 1, value: 1 },
      { id: "theta", label: "Sweep Angle θ (rad)", min: 0.2, max: 6.28, step: 0.1, value: 2.4 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const curveType = Math.round(vals.curve !== undefined ? vals.curve : 1);
      const thetaSweep = vals.theta !== undefined ? vals.theta : 2.4;

      const cx = w * 0.42, cy = h * 0.5;
      const scale = 58;

      // Polar radius functions
      let rFn, drFn, curveTitle;
      if (curveType === 1) {
        curveTitle = "Cardioid: r = 2(1 + cos θ)";
        rFn = (th) => 2 * (1 + Math.cos(th));
        drFn = (th) => -2 * Math.sin(th);
      } else if (curveType === 2) {
        curveTitle = "Four-Petal Rose: r = 3 cos(2θ)";
        rFn = (th) => 3 * Math.cos(2 * th);
        drFn = (th) => -6 * Math.sin(2 * th);
      } else {
        curveTitle = "Limaçon: r = 1.5 + 2 cos θ";
        rFn = (th) => 1.5 + 2 * Math.cos(th);
        drFn = (th) => -2 * Math.sin(th);
      }

      // Polar grid circles
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let rVal = 1; rVal <= 4; rVal++) {
        ctx.beginPath();
        ctx.arc(cx, cy, rVal * scale, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Polar axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(cx - 220, cy); ctx.lineTo(cx + 220, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy - 180); ctx.lineTo(cx, cy + 180); ctx.stroke();

      // Shaded Sector Area
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      let areaAcc = 0;
      const numSteps = 200;
      for (let i = 0; i <= numSteps; i++) {
        const th = (i / numSteps) * thetaSweep;
        const r = Math.max(0, rFn(th));
        areaAcc += 0.5 * r * r * (thetaSweep / numSteps);
        const px = cx + r * Math.cos(th) * scale;
        const py = cy - r * Math.sin(th) * scale;
        ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      ctx.fill();

      // Full curve outline (dim)
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let i = 0; i <= 360; i++) {
        const th = (i / 360) * Math.PI * 2;
        const r = rFn(th);
        const px = cx + r * Math.cos(th) * scale;
        const py = cy - r * Math.sin(th) * scale;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Traced curve path (bright cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= numSteps; i++) {
        const th = (i / numSteps) * thetaSweep;
        const r = rFn(th);
        const px = cx + r * Math.cos(th) * scale;
        const py = cy - r * Math.sin(th) * scale;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current tip vector
      const currentR = rFn(thetaSweep);
      const tipX = cx + currentR * Math.cos(thetaSweep) * scale;
      const tipY = cy - currentR * Math.sin(thetaSweep) * scale;

      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(tipX, tipY); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(tipX, tipY, 5, 0, Math.PI * 2); ctx.fill();

      // Tangent vector
      const dr = drFn(thetaSweep);
      const dxTh = dr * Math.cos(thetaSweep) - currentR * Math.sin(thetaSweep);
      const dyTh = dr * Math.sin(thetaSweep) + currentR * Math.cos(thetaSweep);
      const tanLen = Math.hypot(dxTh, dyTh) || 1;
      const ux = (dxTh / tanLen) * 45;
      const uy = -(dyTh / tanLen) * 45;

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(tipX - ux, tipY - uy); ctx.lineTo(tipX + ux, tipY + uy); ctx.stroke();

      // Information Panel
      const px = w - 240, py = 45;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(px, py, 220, 160);
      ctx.strokeRect(px, py, 220, 160);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(curveTitle, px + 12, py + 22);

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Angle θ = ${(thetaSweep * 180 / Math.PI).toFixed(1)}° (${thetaSweep.toFixed(2)} rad)`, px + 12, py + 48);
      ctx.fillText(`Radius r(θ) = ${currentR.toFixed(3)}`, px + 12, py + 70);
      ctx.fillText(`Rate dr/dθ = ${dr.toFixed(3)}`, px + 12, py + 92);

      const tanPsi = Math.abs(dr) > 1e-4 ? (currentR / dr) : 999;
      const psiDeg = (Math.atan(tanPsi) * 180 / Math.PI);
      ctx.fillText(`Angle ψ = ${psiDeg.toFixed(1)}°`, px + 12, py + 115);

      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Sector Area A ≈ ${areaAcc.toFixed(3)}`, px + 12, py + 140);
    }
  },

  // 5. Improper Integrals & Gabriel's Horn Explorer
  "sim_calc2_improper": {
    title: "Improper Integrals & Gabriel's Horn Explorer",
    desc: "Examine Type I improper integral ∫₁^M (1/xᵖ) dx. Adjust power p and cutoff M to observe p ≤ 1 divergence vs p > 1 convergence, and inspect Gabriel's Horn finite volume V = π vs infinite surface area S → ∞.",
    isAnimated: false,
    controls: [
      { id: "p", label: "Power Exponent (p)", min: 0.4, max: 2.5, step: 0.1, value: 1.0 },
      { id: "M", label: "Upper Bound (M)", min: 2, max: 80, step: 2, value: 25 },
      { id: "horn", label: "Mode (1=Integral, 2=Gabriel's Horn)", min: 1, max: 2, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const p = vals.p !== undefined ? vals.p : 1.0;
      const M = vals.M !== undefined ? vals.M : 25;
      const isHorn = Math.round(vals.horn !== undefined ? vals.horn : 1) === 2;

      if (!isHorn) {
        // Standard Integral View
        const toScreenX = (x) => 70 + ((x - 1) / (M - 1)) * (w - 320);
        const toScreenY = (y) => (h - 70) - (y / 1.15) * (h - 130);

        // Axes
        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(70, toScreenY(0)); ctx.lineTo(w - 240, toScreenY(0)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(70, toScreenY(0)); ctx.lineTo(70, toScreenY(1.1)); ctx.stroke();

        // Shaded area
        ctx.beginPath();
        ctx.moveTo(toScreenX(1), toScreenY(0));
        const steps = 150;
        for (let i = 0; i <= steps; i++) {
          const x = 1 + (i / steps) * (M - 1);
          const y = Math.pow(x, -p);
          ctx.lineTo(toScreenX(x), toScreenY(y));
        }
        ctx.lineTo(toScreenX(M), toScreenY(0));
        ctx.closePath();
        ctx.fillStyle = p > 1.0 ? "rgba(16, 185, 129, 0.35)" : "rgba(239, 68, 68, 0.35)";
        ctx.fill();

        // Curve
        ctx.strokeStyle = p > 1.0 ? "#10b981" : "#ef4444"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let i = 0; i <= steps; i++) {
          const x = 1 + (i / steps) * (M - 1);
          const y = Math.pow(x, -p);
          if (i === 0) ctx.moveTo(toScreenX(x), toScreenY(y));
          else ctx.lineTo(toScreenX(x), toScreenY(y));
        }
        ctx.stroke();

        // Evaluation
        let currentArea = 0;
        if (Math.abs(p - 1.0) < 0.02) {
          currentArea = Math.log(M);
        } else {
          currentArea = (Math.pow(M, 1 - p) - 1) / (1 - p);
        }

        const px = w - 240, py = 45;
        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.strokeStyle = "#334155";
        ctx.fillRect(px, py, 220, 155);
        ctx.strokeRect(px, py, 220, 155);

        ctx.fillStyle = p > 1.0 ? "#10b981" : "#ef4444"; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText(p > 1.0 ? "CONVERGENT (p > 1)" : "DIVERGENT (p ≤ 1)", px + 12, py + 22);

        ctx.fillStyle = "#f8fafc"; ctx.font = "12px Inter, sans-serif";
        ctx.fillText(`Integral ∫₁^${M} x⁻ᵖ dx`, px + 12, py + 48);
        ctx.fillText(`Truncated Area = ${currentArea.toFixed(4)}`, px + 12, py + 70);

        if (p > 1.0) {
          const limitVal = 1 / (p - 1);
          ctx.fillText(`Limit (M→∞) = 1/(p-1) = ${limitVal.toFixed(4)}`, px + 12, py + 95);
        } else {
          ctx.fillText(`Limit (M→∞) = +∞`, px + 12, py + 95);
        }

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`p-Test Threshold: p = 1.0`, px + 12, py + 122);
      } else {
        // Gabriel's Horn 3D wireframe
        const cx = 90, cy = h * 0.5;
        const hornLen = w - 340;

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + hornLen, cy); ctx.stroke();
        ctx.setLineDash([]);

        const rings = 20;
        for (let i = 0; i <= rings; i++) {
          const u = i / rings;
          const x = 1 + u * (M - 1);
          const r = (1 / x) * 60;
          const px = cx + u * hornLen;

          ctx.beginPath();
          ctx.ellipse(px, cy, r * 0.25, r, 0, 0, Math.PI * 2);
          ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
          ctx.stroke();
        }

        // Boundary curves
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
        ctx.beginPath();
        for (let i = 0; i <= rings; i++) {
          const u = i / rings;
          const x = 1 + u * (M - 1);
          const r = (1 / x) * 60;
          const px = cx + u * hornLen;
          if (i === 0) ctx.moveTo(px, cy - r);
          else ctx.lineTo(px, cy - r);
        }
        ctx.stroke();

        ctx.beginPath();
        for (let i = 0; i <= rings; i++) {
          const u = i / rings;
          const x = 1 + u * (M - 1);
          const r = (1 / x) * 60;
          const px = cx + u * hornLen;
          if (i === 0) ctx.moveTo(px, cy + r);
          else ctx.lineTo(px, cy + r);
        }
        ctx.stroke();

        // Readout
        const vol = Math.PI * (1 - 1 / M);
        const areaLower = 2 * Math.PI * Math.log(M);

        const px = w - 240, py = 45;
        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.strokeStyle = "#334155";
        ctx.fillRect(px, py, 220, 160);
        ctx.strokeRect(px, py, 220, 160);

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText("Gabriel's Horn (Torricelli)", px + 12, py + 22);

        ctx.fillStyle = "#10b981"; ctx.font = "12px Inter, sans-serif";
        ctx.fillText(`Volume V = π(1 - 1/M)`, px + 12, py + 48);
        ctx.fillText(`V(M) ≈ ${vol.toFixed(4)} → π ≈ 3.1416`, px + 12, py + 70);

        ctx.fillStyle = "#ef4444";
        ctx.fillText(`Surface Area S > 2π ln(M)`, px + 12, py + 95);
        ctx.fillText(`S(M) > ${areaLower.toFixed(3)} → ∞`, px + 12, py + 118);

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText("Finite Volume, Infinite Area!", px + 12, py + 142);
      }
    }
  },

  // 6. Euler Gamma & Beta Function Continuous Explorer
  "sim_calc2_gamma_beta": {
    title: "Euler Gamma & Beta Function Continuous Explorer",
    desc: "Explore Euler's Gamma function Γ(x) continuously across the real line. Observe poles at {0, -1, -2, -3}, factorial interpolation at positive integers, and examine the Beta relation B(p, q) = Γ(p)Γ(q)/Γ(p+q).",
    isAnimated: false,
    controls: [
      { id: "xProbe", label: "Gamma Probe (x)", min: -3.8, max: 4.5, step: 0.1, value: 2.5 },
      { id: "p", label: "Beta p", min: 0.5, max: 4.0, step: 0.5, value: 2.0 },
      { id: "q", label: "Beta q", min: 0.5, max: 4.0, step: 0.5, value: 3.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const xProbe = vals.xProbe !== undefined ? vals.xProbe : 2.5;
      const pBeta = vals.p !== undefined ? vals.p : 2.0;
      const qBeta = vals.q !== undefined ? vals.q : 3.0;

      // Lanczos approximation for Gamma
      function gamma(z) {
        if (z < 0.5) {
          // Reflection formula: Γ(z)Γ(1-z) = π / sin(πz)
          return Math.PI / (Math.sin(Math.PI * z) * gamma(1 - z));
        }
        z -= 1;
        const g = 7;
        const c = [
          0.99999999999980993, 676.5203681218851, -1259.1392167224028,
          771.32342877765313, -176.61502916214059, 12.507343278686905,
          -0.138571095831171, 9.9843695780195716e-6, 1.5056327351493116e-7
        ];
        let x = c[0];
        for (let i = 1; i < g + 2; i++) {
          x += c[i] / (z + i);
        }
        const t = z + g + 0.5;
        return Math.sqrt(2 * Math.PI) * Math.pow(t, z + 0.5) * Math.exp(-t) * x;
      }

      const toScreenX = (x) => 70 + ((x + 4.0) / 8.8) * (w - 320);
      const toScreenY = (y) => (h * 0.5) - (y / 6.0) * (h * 0.4);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(-4.0), toScreenY(0)); ctx.lineTo(toScreenX(4.8), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(-6.0)); ctx.lineTo(toScreenX(0), toScreenY(6.0)); ctx.stroke();

      // Pole dashed lines
      ctx.strokeStyle = "rgba(239, 68, 68, 0.4)"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      [-3, -2, -1, 0].forEach(pole => {
        ctx.beginPath(); ctx.moveTo(toScreenX(pole), 30); ctx.lineTo(toScreenX(pole), h - 30); ctx.stroke();
      });
      ctx.setLineDash([]);

      // Draw continuous Gamma curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      const segments = [
        [-3.95, -3.05],
        [-2.95, -2.05],
        [-1.95, -1.05],
        [-0.95, -0.05],
        [0.05, 4.5]
      ];

      segments.forEach(seg => {
        ctx.beginPath();
        let started = false;
        const steps = 100;
        for (let i = 0; i <= steps; i++) {
          const x = seg[0] + (i / steps) * (seg[1] - seg[0]);
          const y = gamma(x);
          if (Math.abs(y) <= 8) {
            const sx = toScreenX(x), sy = toScreenY(y);
            if (!started) { ctx.moveTo(sx, sy); started = true; }
            else ctx.lineTo(sx, sy);
          } else {
            started = false;
          }
        }
        ctx.stroke();
      });

      // Factorial node points (1, 1), (2, 1), (3, 2), (4, 6)
      const nodes = [{x: 1, y: 1}, {x: 2, y: 1}, {x: 3, y: 2}, {x: 4, y: 6}, {x: 0.5, y: Math.sqrt(Math.PI)}];
      ctx.fillStyle = "#10b981";
      nodes.forEach(pt => {
        ctx.beginPath(); ctx.arc(toScreenX(pt.x), toScreenY(pt.y), 4.5, 0, Math.PI * 2); ctx.fill();
      });

      // Probe point
      const probeY = gamma(xProbe);
      if (Math.abs(probeY) <= 8) {
        ctx.fillStyle = "#f59e0b";
        ctx.beginPath(); ctx.arc(toScreenX(xProbe), toScreenY(probeY), 6, 0, Math.PI * 2); ctx.fill();
      }

      // Readout panel
      const betaVal = (gamma(pBeta) * gamma(qBeta)) / gamma(pBeta + qBeta);
      const px = w - 240, py = 45;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(px, py, 220, 160);
      ctx.strokeRect(px, py, 220, 160);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Euler Gamma & Beta", px + 12, py + 22);

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Probe x = ${xProbe.toFixed(2)}`, px + 12, py + 48);
      ctx.fillText(`Γ(${xProbe.toFixed(2)}) ≈ ${Math.abs(probeY) < 100 ? probeY.toFixed(4) : '±∞ (Pole)'}`, px + 12, py + 70);

      ctx.fillStyle = "#10b981";
      ctx.fillText(`Γ(1/2) = √π ≈ 1.7725`, px + 12, py + 95);

      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Beta B(${pBeta.toFixed(1)}, ${qBeta.toFixed(1)}) = ${betaVal.toFixed(5)}`, px + 12, py + 120);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Bridge: B(p,q) = Γ(p)Γ(q)/Γ(p+q)`, px + 12, py + 144);
    }
  },

  // 7. Power Series Radius of Convergence & Partial Sums
  "sim_calc2_power_series": {
    title: "Power Series Radius of Convergence & Partial Sums",
    desc: "Inspect partial sums P_N(x) for power series. Vary polynomial order N ∈ [1, 16] to witness strict convergence inside the interval (-R, R) and violent divergence outside.",
    isAnimated: false,
    controls: [
      { id: "series", label: "Series (1=1/(1-x), 2=ln(1+x), 3=eˣ)", min: 1, max: 3, step: 1, value: 1 },
      { id: "N", label: "Polynomial Order (N)", min: 1, max: 16, step: 1, value: 5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const seriesType = Math.round(vals.series !== undefined ? vals.series : 1);
      const N = Math.round(vals.N !== undefined ? vals.N : 5);

      let targetFn, partialFn, radius, titleStr;
      if (seriesType === 1) {
        titleStr = "Geometric: 1/(1 - x)";
        radius = 1.0;
        targetFn = (x) => (Math.abs(x - 1) > 0.02 ? 1 / (1 - x) : NaN);
        partialFn = (x) => {
          let sum = 0;
          for (let k = 0; k <= N; k++) sum += Math.pow(x, k);
          return sum;
        };
      } else if (seriesType === 2) {
        titleStr = "Logarithm: ln(1 + x)";
        radius = 1.0;
        targetFn = (x) => (x > -0.98 ? Math.log(1 + x) : NaN);
        partialFn = (x) => {
          let sum = 0;
          for (let k = 1; k <= N; k++) sum += (Math.pow(-1, k - 1) * Math.pow(x, k)) / k;
          return sum;
        };
      } else {
        titleStr = "Exponential: eˣ";
        radius = Infinity;
        targetFn = (x) => Math.exp(x);
        partialFn = (x) => {
          let sum = 1, term = 1;
          for (let k = 1; k <= N; k++) {
            term *= x / k;
            sum += term;
          }
          return sum;
        };
      }

      const toScreenX = (x) => 70 + ((x + 2.2) / 4.4) * (w - 320);
      const toScreenY = (y) => (h * 0.5) - (y / 5.0) * (h * 0.4);

      // Shaded convergence zone
      if (radius < 10) {
        const sxL = toScreenX(-radius), sxR = toScreenX(radius);
        ctx.fillStyle = "rgba(16, 185, 129, 0.12)";
        ctx.fillRect(sxL, 30, sxR - sxL, h - 60);

        // Boundary lines
        ctx.strokeStyle = "rgba(16, 185, 129, 0.6)"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(sxL, 30); ctx.lineTo(sxL, h - 30); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(sxR, 30); ctx.lineTo(sxR, h - 30); ctx.stroke();
        ctx.setLineDash([]);
      }

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(-2.2), toScreenY(0)); ctx.lineTo(toScreenX(2.2), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(-5.0)); ctx.lineTo(toScreenX(0), toScreenY(5.0)); ctx.stroke();

      // Target curve (dashed white)
      ctx.strokeStyle = "rgba(248, 250, 252, 0.5)"; ctx.lineWidth = 2; ctx.setLineDash([5, 5]);
      ctx.beginPath();
      let started = false;
      for (let i = 0; i <= 200; i++) {
        const x = -2.1 + (i / 200) * 4.2;
        const y = targetFn(x);
        if (!isNaN(y) && Math.abs(y) <= 6) {
          const sx = toScreenX(x), sy = toScreenY(y);
          if (!started) { ctx.moveTo(sx, sy); started = true; }
          else ctx.lineTo(sx, sy);
        } else {
          started = false;
        }
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Partial sum curve (solid cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      started = false;
      for (let i = 0; i <= 200; i++) {
        const x = -2.1 + (i / 200) * 4.2;
        const y = partialFn(x);
        if (!isNaN(y) && Math.abs(y) <= 6.5) {
          const sx = toScreenX(x), sy = toScreenY(y);
          if (!started) { ctx.moveTo(sx, sy); started = true; }
          else ctx.lineTo(sx, sy);
        } else {
          started = false;
        }
      }
      ctx.stroke();

      // Readout panel
      const px = w - 240, py = 45;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(px, py, 220, 150);
      ctx.strokeRect(px, py, 220, 150);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(titleStr, px + 12, py + 22);

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Partial Sum Degree N = ${N}`, px + 12, py + 48);

      ctx.fillStyle = "#10b981";
      ctx.fillText(`Radius R = ${radius === Infinity ? '∞' : radius.toFixed(1)}`, px + 12, py + 72);
      ctx.fillText(`Convergence: ${radius === Infinity ? '(-∞, ∞)' : '(-1, 1)'}`, px + 12, py + 95);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Dashed: Target f(x)", px + 12, py + 120);
      ctx.fillText("Cyan: Partial Sum P_N(x)", px + 12, py + 138);
    }
  },

  // 8. Taylor Polynomial Approximation & Remainder Bound Explorer
  "sim_calc2_taylor": {
    title: "Taylor Polynomial Approximation & Remainder Bound Explorer",
    desc: "Select target function and adjust degree n ∈ [1, 10] to observe higher-order osculation, residual error |f(x) - P_n(x)|, and verify the theoretical Lagrange remainder bound.",
    isAnimated: false,
    controls: [
      { id: "fn", label: "Function (1=sin x, 2=cos x, 3=eˣ)", min: 1, max: 3, step: 1, value: 1 },
      { id: "degree", label: "Taylor Degree (n)", min: 1, max: 9, step: 2, value: 3 },
      { id: "probe", label: "Probe (x)", min: -2.5, max: 2.5, step: 0.1, value: 1.2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const fnType = Math.round(vals.fn !== undefined ? vals.fn : 1);
      const degree = Math.round(vals.degree !== undefined ? vals.degree : 3);
      const probeX = vals.probe !== undefined ? vals.probe : 1.2;

      let targetFn, taylorFn, titleStr;
      if (fnType === 1) {
        titleStr = "Target: f(x) = sin(x)";
        targetFn = (x) => Math.sin(x);
        taylorFn = (x) => {
          let sum = 0;
          for (let k = 0; 2 * k + 1 <= degree; k++) {
            const term = (Math.pow(-1, k) * Math.pow(x, 2 * k + 1)) / factorial(2 * k + 1);
            sum += term;
          }
          return sum;
        };
      } else if (fnType === 2) {
        titleStr = "Target: f(x) = cos(x)";
        targetFn = (x) => Math.cos(x);
        taylorFn = (x) => {
          let sum = 0;
          for (let k = 0; 2 * k <= degree; k++) {
            const term = (Math.pow(-1, k) * Math.pow(x, 2 * k)) / factorial(2 * k);
            sum += term;
          }
          return sum;
        };
      } else {
        titleStr = "Target: f(x) = eˣ";
        targetFn = (x) => Math.exp(x);
        taylorFn = (x) => {
          let sum = 0;
          for (let k = 0; k <= degree; k++) {
            sum += Math.pow(x, k) / factorial(k);
          }
          return sum;
        };
      }

      function factorial(n) {
        let f = 1;
        for (let i = 2; i <= n; i++) f *= i;
        return f;
      }

      const toScreenX = (x) => 70 + ((x + 3.0) / 6.0) * (w - 320);
      const toScreenY = (y) => (h * 0.5) - (y / 3.5) * (h * 0.4);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toScreenX(-3.0), toScreenY(0)); ctx.lineTo(toScreenX(3.0), toScreenY(0)); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toScreenX(0), toScreenY(-3.5)); ctx.lineTo(toScreenX(0), toScreenY(3.5)); ctx.stroke();

      // Target curve
      ctx.strokeStyle = "rgba(248, 250, 252, 0.6)"; ctx.lineWidth = 2; ctx.setLineDash([5, 5]);
      ctx.beginPath();
      for (let i = 0; i <= 200; i++) {
        const x = -2.9 + (i / 200) * 5.8;
        const y = targetFn(x);
        const sx = toScreenX(x), sy = toScreenY(y);
        if (i === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Taylor Polynomial curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      let started = false;
      for (let i = 0; i <= 200; i++) {
        const x = -2.9 + (i / 200) * 5.8;
        const y = taylorFn(x);
        if (Math.abs(y) <= 4.0) {
          const sx = toScreenX(x), sy = toScreenY(y);
          if (!started) { ctx.moveTo(sx, sy); started = true; }
          else ctx.lineTo(sx, sy);
        } else {
          started = false;
        }
      }
      ctx.stroke();

      // Probe values
      const trueVal = targetFn(probeX);
      const approxVal = taylorFn(probeX);
      const error = Math.abs(trueVal - approxVal);

      // Draw probe indicator
      const sxP = toScreenX(probeX);
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(sxP, toScreenY(trueVal)); ctx.lineTo(sxP, toScreenY(approxVal)); ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(sxP, toScreenY(trueVal), 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(sxP, toScreenY(approxVal), 5, 0, Math.PI * 2); ctx.fill();

      // Readout
      const lagrangeBound = (Math.pow(Math.abs(probeX), degree + 1)) / factorial(degree + 1);
      const px = w - 240, py = 45;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(px, py, 220, 160);
      ctx.strokeRect(px, py, 220, 160);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(titleStr, px + 12, py + 22);

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Degree n = ${degree} (Centered at 0)`, px + 12, py + 48);
      ctx.fillText(`True f(${probeX.toFixed(1)}) = ${trueVal.toFixed(5)}`, px + 12, py + 70);
      ctx.fillText(`Taylor P_${degree}(${probeX.toFixed(1)}) = ${approxVal.toFixed(5)}`, px + 12, py + 92);

      ctx.fillStyle = error < 1e-3 ? "#10b981" : "#f59e0b";
      ctx.fillText(`Actual Error |R_n| = ${error.toFixed(6)}`, px + 12, py + 115);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Lagrange Bound ≤ ${lagrangeBound.toFixed(6)}`, px + 12, py + 140);
    }
  }
};

// Simulation Engine Bridge
window.SimulationEngine = window.SimulationEngine || {
  activeAnimations: {},
  initSimulation: function(containerId, simKey) {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = "";

    const simConfig = window.CALC2_SIMS && window.CALC2_SIMS[simKey];
    if (!simConfig) {
      container.innerHTML = `<div style="padding:1rem;color:#94a3b8;">Simulation ${simKey} ready.</div>`;
      return;
    }

    const box = document.createElement("div");
    box.className = "sim-box-wrapper";
    box.style.background = "#050811";
    box.style.border = "1px solid #1e293b";
    box.style.borderRadius = "12px";
    box.style.padding = "1rem";
    box.style.marginBottom = "1.5rem";

    const header = document.createElement("div");
    header.style.display = "flex";
    header.style.justifyContent = "space-between";
    header.style.alignItems = "center";
    header.style.marginBottom = "0.75rem";

    const titleEl = document.createElement("h4");
    titleEl.style.margin = "0";
    titleEl.style.color = "#38bdf8";
    titleEl.style.fontSize = "1.05rem";
    titleEl.innerText = simConfig.title;

    const badge = document.createElement("span");
    badge.innerText = "60 FPS Interactive";
    badge.style.fontSize = "0.75rem";
    badge.style.background = "rgba(56, 189, 248, 0.15)";
    badge.style.color = "#38bdf8";
    badge.style.padding = "3px 8px";
    badge.style.borderRadius = "999px";

    header.appendChild(titleEl);
    header.appendChild(badge);
    box.appendChild(header);

    const descEl = document.createElement("p");
    descEl.style.color = "#94a3b8";
    descEl.style.fontSize = "0.85rem";
    descEl.style.marginBottom = "1rem";
    descEl.innerText = simConfig.desc;
    box.appendChild(descEl);

    const canvas = document.createElement("canvas");
    canvas.width = 720;
    canvas.height = 340;
    canvas.style.width = "100%";
    canvas.style.height = "auto";
    canvas.style.background = "#050811";
    canvas.style.borderRadius = "8px";
    canvas.style.border = "1px solid #1e293b";
    canvas.style.display = "block";
    box.appendChild(canvas);

    const controlsContainer = document.createElement("div");
    controlsContainer.style.display = "grid";
    controlsContainer.style.gridTemplateColumns = "repeat(auto-fit, minmax(140px, 1fr))";
    controlsContainer.style.gap = "1rem";
    controlsContainer.style.marginTop = "1rem";

    const vals = {};
    if (simConfig.controls) {
      simConfig.controls.forEach(ctrl => {
        vals[ctrl.id] = ctrl.value;
        const wrap = document.createElement("div");
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
  }
};
'''

with open("calculus-2-sims.js", "w", encoding="utf-8") as f:
    f.write(sims_code)

print("calculus-2-sims.js created successfully with all 8 simulation engines!")
