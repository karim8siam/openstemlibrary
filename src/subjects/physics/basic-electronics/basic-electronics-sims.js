// Basic Electronics & Analog Circuits Interactive Simulation Engine
// 16 Interactive 60-FPS Canvas Simulations for Diodes, Transistors, Thyristors, Amplifiers, Oscillators & Op-Amps

window.BE_SIMS = {

  // 1. PN Junction Diode & Shockley I-V Curve
  "pn-junction-diode-sim": {
    title: "PN Junction Barrier & Shockley I-V Characteristic",
    desc: "Observe how forward bias narrows the depletion layer and causes exponential majority carrier injection, while reverse bias widens the barrier potential.",
    isAnimated: true,
    controls: [
      { id: "v", label: "Bias Voltage V (V)", min: -3.0, max: 0.8, step: 0.05, value: 0.65 },
      { id: "temp", label: "Temperature T (K)", min: 250, max: 400, step: 10, value: 300 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const V = vals.v !== undefined ? vals.v : 0.65;
      const T = vals.temp || 300;
      const Vt = (1.38e-23 * T) / 1.6e-19; // ~0.02586V at 300K
      const Is = 1e-12 * Math.pow(T / 300, 3); // saturation current
      const I = Is * (Math.exp(Math.min(V, 0.78) / (1.0 * Vt)) - 1); // Shockley current

      // Left panel: Physical PN Junction (x: 20 to 340)
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(30, 40, 300, 240);

      // Depletion width depends on bias
      const Vbi = 0.75;
      let depRatio = Math.max(0.08, Math.min(0.85, (V < 0 ? Math.sqrt(1 - V / Vbi) * 0.35 : Math.max(0.08, 0.35 * Math.sqrt(Math.max(0.01, 1 - V / Vbi))))));
      const midX = 180;
      const depHalf = 150 * depRatio;

      // P region
      ctx.fillStyle = "rgba(239, 68, 68, 0.15)";
      ctx.fillRect(30, 40, midX - depHalf - 30, 240);
      // N region
      ctx.fillStyle = "rgba(59, 130, 246, 0.15)";
      ctx.fillRect(midX + depHalf, 40, 330 - (midX + depHalf), 240);
      // Depletion region
      ctx.fillStyle = "rgba(148, 163, 184, 0.12)";
      ctx.fillRect(midX - depHalf, 40, 2 * depHalf, 240);

      // Labels
      ctx.font = "bold 14px sans-serif";
      ctx.fillStyle = "#f87171";
      ctx.fillText("P-Type (Holes +)", 50, 70);
      ctx.fillStyle = "#60a5fa";
      ctx.fillText("N-Type (Electrons -)", 200, 70);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px sans-serif";
      ctx.fillText("Depletion Zone", midX - 40, 260);

      // Moving carriers if forward biased
      if (V > 0.4) {
        ctx.fillStyle = "#f87171";
        for (let i = 0; i < 8; i++) {
          const cx = 50 + ((time * 40 + i * 35) % (midX + depHalf - 50));
          const cy = 100 + (i * 20) % 120;
          ctx.beginPath(); ctx.arc(cx, cy, 4, 0, Math.PI * 2); ctx.fill();
        }
        ctx.fillStyle = "#60a5fa";
        for (let i = 0; i < 8; i++) {
          const cx = 310 - ((time * 40 + i * 35) % (310 - (midX - depHalf)));
          const cy = 110 + (i * 20) % 120;
          ctx.beginPath(); ctx.arc(cx, cy, 4, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Barrier potential curve below junction
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(30, 220);
      ctx.lineTo(midX - depHalf, 220);
      ctx.bezierCurveTo(midX, 220, midX, 150 + V * 60, midX + depHalf, 150 + V * 60);
      ctx.lineTo(330, 150 + V * 60);
      ctx.stroke();

      // Right panel: Shockley I-V Curve (x: 380 to 680, y: 40 to 280)
      const gx = 400, gy = 240, gw = 280, gh = 200;
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1;
      // Axes
      ctx.beginPath();
      ctx.moveTo(gx + 60, gy - gh); ctx.lineTo(gx + 60, gy); ctx.lineTo(gx + gw, gy);
      ctx.stroke();
      ctx.fillStyle = "#94a3b8";
      ctx.fillText("V (Volts)", gx + gw - 40, gy + 20);
      ctx.fillText("I (mA)", gx + 15, gy - gh + 15);
      ctx.fillText("0", gx + 50, gy + 15);
      ctx.fillText("0.7V", gx + 180, gy + 15);

      // Draw I-V trace
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = -50; px <= 200; px += 2) {
        const vVal = px * 0.004; // -0.2 to 0.8V
        const iVal = Is * (Math.exp(Math.min(vVal, 0.78) / (1.0 * Vt)) - 1);
        const scrX = gx + 60 + px * 1.3;
        const scrY = gy - Math.min(gh - 10, iVal * 2500);
        if (px === -50) ctx.moveTo(scrX, scrY);
        else ctx.lineTo(scrX, scrY);
      }
      ctx.stroke();

      // Operating point marker
      const curX = gx + 60 + (V / 0.004) * 1.3;
      const curY = gy - Math.min(gh - 10, I * 2500);
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(curX, Math.max(gy - gh, curY), 6, 0, Math.PI * 2); ctx.fill();

      // Readout
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "13px monospace";
      ctx.fillText(`Bias Voltage V = ${V.toFixed(2)} V`, 400, 305);
      ctx.fillText(`Diode Current I = ${(I * 1000).toFixed(2)} mA`, 400, 325);
    }
  },

  // 2. Full-Wave Bridge Rectifier
  "full-wave-bridge-rectifier-sim": {
    title: "Full-Wave Bridge Rectifier AC-to-DC Waveforms",
    desc: "Observe how four bridge diodes alternate in conduction pairs (D1-D2 vs D3-D4) across the AC cycle, converting dual polarities into pulsating DC.",
    isAnimated: true,
    controls: [
      { id: "vm", label: "Peak AC Voltage Vm (V)", min: 5, max: 24, step: 1, value: 12 },
      { id: "freq", label: "AC Frequency (Hz)", min: 20, max: 80, step: 5, value: 50 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Vm = vals.vm || 12;
      const freq = vals.freq || 50;
      const omega = 2 * Math.PI * (freq / 10); // visual frequency
      const curAngle = (omega * time) % (2 * Math.PI);
      const isPositiveHalf = Math.sin(curAngle) >= 0;

      // Schematic on left: Bridge Rectifier (x: 40 to 280, y: 40 to 280)
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 2;
      const bx = 160, by = 160, bSize = 70;

      // Diamond diamond lines
      ctx.beginPath();
      ctx.moveTo(bx, by - bSize);
      ctx.lineTo(bx + bSize, by);
      ctx.lineTo(bx, by + bSize);
      ctx.lineTo(bx - bSize, by);
      ctx.closePath();
      ctx.stroke();

      // Diodes on edges
      const dActive12 = isPositiveHalf; // D1, D2 conducting
      const dActive34 = !isPositiveHalf; // D3, D4 conducting

      // Highlight active diode branches
      ctx.lineWidth = 4;
      // D1 (top-right) and D2 (bottom-left)
      ctx.strokeStyle = dActive12 ? "#10b981" : "#334155";
      ctx.beginPath(); ctx.moveTo(bx, by - bSize); ctx.lineTo(bx + bSize, by); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(bx - bSize, by); ctx.lineTo(bx, by + bSize); ctx.stroke();

      // D3 (top-left) and D4 (bottom-right)
      ctx.strokeStyle = dActive34 ? "#10b981" : "#334155";
      ctx.beginPath(); ctx.moveTo(bx - bSize, by); ctx.lineTo(bx, by - bSize); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(bx, by + bSize); ctx.lineTo(bx + bSize, by); ctx.stroke();

      ctx.fillStyle = dActive12 ? "#10b981" : "#64748b";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("D1, D2 ON", bx + bSize + 10, by - 20);
      ctx.fillStyle = dActive34 ? "#10b981" : "#64748b";
      ctx.fillText("D3, D4 ON", bx - bSize - 80, by + 30);

      // Right side: Scope traces (x: 320 to 690)
      // Trace 1: Input AC Waveform (top half)
      const sx = 320, sy1 = 100, sw = 360, sh = 60;
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(sx, 40, sw, 120);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px sans-serif";
      ctx.fillText("AC Input Waveform vs(t) [Sinusoidal]", sx + 10, 58);

      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const tVal = (x / sw) * 4 * Math.PI - curAngle;
        const yVal = sy1 - Math.sin(tVal) * (Vm * 2.8);
        if (x === 0) ctx.moveTo(sx + x, yVal);
        else ctx.lineTo(sx + x, yVal);
      }
      ctx.stroke();

      // Trace 2: Rectified DC Waveform (bottom half)
      const sy2 = 250;
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(sx, 180, sw, 120);
      ctx.fillStyle = "#10b981";
      ctx.fillText("Rectified Output vo(t) [Pulsating DC, Ripple = 2f]", sx + 10, 198);

      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const tVal = (x / sw) * 4 * Math.PI - curAngle;
        const yVal = sy2 - Math.abs(Math.sin(tVal)) * (Vm * 2.8);
        if (x === 0) ctx.moveTo(sx + x, yVal);
        else ctx.lineTo(sx + x, yVal);
      }
      ctx.stroke();

      // Performance stats
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "12px monospace";
      const Vdc = (2 * Vm) / Math.PI;
      ctx.fillText(`Peak Vm: ${Vm} V | Vdc: ${Vdc.toFixed(2)} V | Efficiency: 81.2% | Ripple: 0.482`, 40, 325);
    }
  },

  // 3. Shunt Capacitor Filter Ripple
  "capacitor-filter-ripple-sim": {
    title: "Capacitor Filter Smoothing & Ripple Factor Reduction",
    desc: "Observe how increasing filter capacitance C or load resistance RL extends the discharge time constant, drastically suppressing AC ripple voltage.",
    isAnimated: true,
    controls: [
      { id: "cap", label: "Capacitance C (uF)", min: 20, max: 500, step: 20, value: 120 },
      { id: "load", label: "Load Resistor RL (Ohm)", min: 50, max: 500, step: 25, value: 200 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const C = (vals.cap || 120) * 1e-6;
      const RL = vals.load || 200;
      const Vm = 15;
      const f = 50;
      const Vr_pp = Vm / (2 * f * C * RL); // approx ripple peak-to-peak
      const Vdc = Math.max(0, Vm - Vr_pp / 2);
      const rippleFactor = 1 / (4 * Math.sqrt(3) * f * C * RL);

      const sx = 50, sy = 220, sw = 620, sh = 160;
      // Grid
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(sx, 40, sw, 220);
      ctx.beginPath();
      ctx.moveTo(sx, sy); ctx.lineTo(sx + sw, sy);
      ctx.stroke();

      // Draw unfiltered rectified sine reference (dashed)
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
      ctx.setLineDash([3, 3]);
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      const periods = 4;
      for (let x = 0; x < sw; x++) {
        const phi = (x / sw) * periods * Math.PI;
        const y = sy - Math.abs(Math.sin(phi)) * 120;
        if (x === 0) ctx.moveTo(sx + x, y);
        else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw filtered capacitor voltage (charge up on peaks, exponential decay between)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();

      const tau = RL * C * 1000; // visual time constant
      let capV = Vm;
      for (let x = 0; x < sw; x++) {
        const phi = (x / sw) * periods * Math.PI;
        const rectified = Math.abs(Math.sin(phi)) * Vm;
        if (rectified >= capV) {
          capV = rectified; // charging pulse
        } else {
          capV -= (capV / (RL * C * 400)); // discharge
        }
        const y = sy - (capV / Vm) * 120;
        if (x === 0) ctx.moveTo(sx + x, y);
        else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      // Readout telemetry banner
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(sx, 275, sw, 50);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(sx, 275, sw, 50);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px monospace";
      ctx.fillText(`Ripple Vr(pp): ${Vr_pp.toFixed(2)} V`, sx + 20, 305);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`DC Output Vdc: ${Vdc.toFixed(2)} V`, sx + 220, 305);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Ripple Factor r: ${(rippleFactor * 100).toFixed(2)}%`, sx + 430, 305);
    }
  },

  // 4. Zener Diode Shunt Voltage Regulator
  "zener-diode-regulator-sim": {
    title: "Zener Diode Shunt Voltage Regulator & Load Regulation",
    desc: "Observe how the Zener diode absorbs input line fluctuations (Vin) and load current variations (RL) while clamping load voltage strictly at Vz.",
    isAnimated: true,
    controls: [
      { id: "vin", label: "Input Voltage Vin (V)", min: 10, max: 25, step: 0.5, value: 16 },
      { id: "vz", label: "Zener Breakdown Vz (V)", min: 5.1, max: 12.0, step: 0.1, value: 9.1 },
      { id: "rl", label: "Load Resistance RL (Ohm)", min: 100, max: 1000, step: 50, value: 470 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Vin = vals.vin || 16;
      const Vz = vals.vz || 9.1;
      const RL = vals.rl || 470;
      const Rs = 220; // 220 ohm series resistor

      // Calculate currents
      const IL = (Vz / RL) * 1000; // mA
      const Is = ((Vin - Vz) / Rs) * 1000; // mA
      const Iz = Math.max(0, Is - IL); // mA
      const isRegulating = Is > IL && Iz > 2.0;

      // Draw Schematic Diagram
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 2.5;

      // Wires
      ctx.beginPath();
      ctx.moveTo(60, 100); ctx.lineTo(180, 100); // to Rs
      ctx.moveTo(260, 100); ctx.lineTo(420, 100); // from Rs to Zener & Load
      ctx.moveTo(420, 100); ctx.lineTo(580, 100);
      ctx.moveTo(420, 100); ctx.lineTo(420, 150); // to Zener
      ctx.moveTo(420, 210); ctx.lineTo(420, 240); // from Zener to GND
      ctx.moveTo(580, 100); ctx.lineTo(580, 150); // to RL
      ctx.moveTo(580, 210); ctx.lineTo(580, 240); // from RL to GND
      ctx.moveTo(60, 240); ctx.lineTo(580, 240); // Ground rail
      ctx.stroke();

      // Series Resistor Rs box
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(180, 85, 80, 30);
      ctx.strokeRect(180, 85, 80, 30);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px sans-serif";
      ctx.fillText(`Rs = ${Rs}Ω`, 195, 105);

      // Zener Diode Symbol at (420, 180)
      ctx.fillStyle = isRegulating ? "#10b981" : "#ef4444";
      ctx.beginPath();
      ctx.moveTo(405, 185); ctx.lineTo(435, 185); ctx.lineTo(420, 160); ctx.closePath();
      ctx.fill();
      // Cathode bent bar
      ctx.strokeStyle = "#e2e8f0";
      ctx.beginPath();
      ctx.moveTo(400, 160); ctx.lineTo(405, 160); ctx.lineTo(435, 160); ctx.lineTo(440, 165);
      ctx.stroke();

      // Load Resistor RL box
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(555, 150, 50, 60);
      ctx.strokeRect(555, 150, 50, 60);
      ctx.fillStyle = "#e2e8f0";
      ctx.fillText(`RL`, 570, 185);

      // Status LED indicator
      ctx.fillStyle = isRegulating ? "#10b981" : "#ef4444";
      ctx.beginPath(); ctx.arc(420, 60, 8, 0, Math.PI * 2); ctx.fill();
      ctx.font = "bold 13px sans-serif";
      ctx.fillText(isRegulating ? "REGULATING (Active Breakdown)" : "DROPOUT (Unregulated)", 435, 65);

      // Bar gauges for Current Flow
      const drawGauge = (x, y, label, val, max, color) => {
        ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
        ctx.fillText(label, x, y);
        ctx.fillStyle = "#1e293b";
        ctx.fillRect(x, y + 8, 160, 14);
        ctx.fillStyle = color;
        const fillW = Math.min(160, (val / max) * 160);
        ctx.fillRect(x, y + 8, fillW, 14);
        ctx.fillStyle = "#e2e8f0"; ctx.font = "11px monospace";
        ctx.fillText(`${val.toFixed(1)} mA`, x + 165, y + 20);
      };

      drawGauge(60, 275, "Total Source Current Is", Is, 80, "#38bdf8");
      drawGauge(280, 275, "Zener Shunt Current Iz", Iz, 60, isRegulating ? "#10b981" : "#ef4444");
      drawGauge(500, 275, "Load Current IL", IL, 60, "#f59e0b");
    }
  },

  // 5. BJT Common Emitter Output Characteristics
  "bjt-ce-characteristics-sim": {
    title: "BJT Common Emitter Output Characteristics & Dynamic DC Load Line",
    desc: "Examine the collector characteristics family (IC vs VCE) across base current steps, illustrating active amplification, saturation knee, and Q-point stability.",
    isAnimated: true,
    controls: [
      { id: "ib", label: "Base Current Ib (uA)", min: 5, max: 60, step: 5, value: 30 },
      { id: "vcc", label: "Supply Voltage Vcc (V)", min: 8, max: 24, step: 1, value: 16 },
      { id: "rc", label: "Collector Resistor Rc (kOhm)", min: 0.5, max: 4.0, step: 0.5, value: 2.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Ib = vals.ib || 30; // uA
      const Vcc = vals.vcc || 16;
      const Rc = (vals.rc || 2.0) * 1000;
      const beta = 100;
      const Va = 100; // Early voltage (V)

      const gx = 60, gy = 260, gw = 600, gh = 210;

      // Axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(gx, gy - gh); ctx.lineTo(gx, gy); ctx.lineTo(gx + gw, gy);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Collector-Emitter Voltage VCE (V)", gx + gw - 190, gy + 25);
      ctx.fillText("Collector Current IC (mA)", gx - 45, gy - gh - 8);

      // Draw Family of Curves for Ib = 10, 20, 30, 40, 50, 60 uA
      const ibSteps = [10, 20, 30, 40, 50, 60];
      ibSteps.forEach(currIb => {
        const isSelected = Math.abs(currIb - Ib) < 3;
        ctx.strokeStyle = isSelected ? "#38bdf8" : "rgba(148, 163, 184, 0.35)";
        ctx.lineWidth = isSelected ? 3 : 1.5;
        ctx.beginPath();

        for (let vce = 0; vce <= 25; vce += 0.2) {
          // Saturation curve transition + active early effect
          const satFactor = 1 - Math.exp(-vce / 0.5);
          const ic = (beta * (currIb * 1e-6) * (1 + vce / Va) * satFactor) * 1000; // mA
          const px = gx + (vce / 25) * gw;
          const py = gy - (ic / 12) * gh;
          if (vce === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        ctx.fillStyle = isSelected ? "#38bdf8" : "#64748b";
        ctx.font = "11px monospace";
        ctx.fillText(`Ib=${currIb}uA`, gx + gw - 55, gy - ((beta * (currIb * 1e-6) * 1000) / 12) * gh - 5);
      });

      // Draw DC Load Line: from (0, Vcc/Rc) to (Vcc, 0)
      const icSat = (Vcc / Rc) * 1000; // mA
      const l1x = gx, l1y = gy - Math.min(gh, (icSat / 12) * gh);
      const l2x = gx + (Vcc / 25) * gw, l2y = gy;

      ctx.strokeStyle = "#ef4444";
      ctx.lineWidth = 2.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(l1x, l1y); ctx.lineTo(l2x, l2y); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444";
      ctx.fillText("DC Load Line", l2x - 80, l2y - 15);

      // Q-point calculation (intersection)
      const icQ = Math.min(icSat * 0.98, (beta * (Ib * 1e-6) * 1000));
      const vceQ = Math.max(0.2, Vcc - (icQ / 1000) * Rc);
      const qx = gx + (vceQ / 25) * gw;
      const qy = gy - (icQ / 12) * gh;

      // Q-point marker
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(qx, qy, 7, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText(`Q-Point (Vce=${vceQ.toFixed(1)}V, Ic=${icQ.toFixed(2)}mA)`, qx + 12, qy - 10);
    }
  },

  // 6. JFET Drain Characteristics
  "jfet-drain-characteristics-sim": {
    title: "N-Channel JFET Drain Characteristics & Pinch-Off Boundary",
    desc: "Observe the transition from Ohmic (voltage-controlled resistor) to Saturation (constant-current source) across gate-source voltages VGS.",
    isAnimated: true,
    controls: [
      { id: "vgs", label: "Gate-Source VGS (V)", min: -4.0, max: 0.0, step: 0.2, value: -1.6 },
      { id: "vp", label: "Pinch-off Vp (V)", min: -5.0, max: -2.0, step: 0.5, value: -4.0 },
      { id: "idss", label: "IDSS (mA)", min: 4, max: 16, step: 1, value: 10 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Vgs = vals.vgs !== undefined ? vals.vgs : -1.6;
      const Vp = vals.vp || -4.0;
      const IDSS = vals.idss || 10;

      const gx = 60, gy = 260, gw = 600, gh = 210;

      // Axes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(gx, gy - gh); ctx.lineTo(gx, gy); ctx.lineTo(gx + gw, gy); ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Drain-Source Voltage VDS (V)", gx + gw - 170, gy + 25);
      ctx.fillText("Drain Current ID (mA)", gx - 45, gy - gh - 8);

      // Pinch-off locus parabola
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)";
      ctx.lineWidth = 2; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      for (let vds = 0; vds <= -Vp; vds += 0.2) {
        const vgsEquiv = vds + Vp;
        const idParabola = IDSS * Math.pow(1 - vgsEquiv / Vp, 2);
        const px = gx + (vds / 15) * gw;
        const py = gy - (idParabola / (IDSS * 1.2)) * gh;
        if (vds === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("Pinch-off Locus VDS = VGS - Vp", gx + 150, gy - gh + 20);

      // Family of curves
      const vgsLevels = [0, -1, -2, -3, -4];
      vgsLevels.forEach(vg => {
        const isCurrent = Math.abs(vg - Math.round(Vgs)) < 0.5;
        ctx.strokeStyle = isCurrent ? "#38bdf8" : "rgba(148, 163, 184, 0.35)";
        ctx.lineWidth = isCurrent ? 3 : 1.5;
        ctx.beginPath();

        const vdsSat = vg - Vp;
        for (let vds = 0; vds <= 15; vds += 0.2) {
          let id = 0;
          if (vds < vdsSat) {
            id = (2 * IDSS / (-Vp)) * ((vg - Vp) * vds - (vds * vds) / 2);
          } else {
            id = IDSS * Math.pow(Math.max(0, 1 - vg / Vp), 2);
          }
          const px = gx + (vds / 15) * gw;
          const py = gy - (id / (IDSS * 1.2)) * gh;
          if (vds === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      });

      // Active state readout
      const vdsActive = 6.0;
      const idActive = IDSS * Math.pow(Math.max(0, 1 - Vgs / Vp), 2);
      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(gx + (vdsActive / 15) * gw, gy - (idActive / (IDSS * 1.2)) * gh, 6, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#e2e8f0"; ctx.font = "13px monospace";
      ctx.fillText(`VGS: ${Vgs.toFixed(1)} V | Vp: ${Vp.toFixed(1)} V | ID: ${idActive.toFixed(2)} mA (Saturation)`, 60, 315);
    }
  },

  // 7. SCR Phase Control
  "scr-phase-control-sim": {
    title: "SCR AC Phase Control & Delay Angle Firing Waveforms",
    desc: "Adjust the gate firing angle alpha to control the conduction angle gamma and smoothly regulate average DC power delivered to the resistive load.",
    isAnimated: true,
    controls: [
      { id: "alpha", label: "Firing Angle alpha (deg)", min: 10, max: 160, step: 5, value: 60 },
      { id: "vm", label: "Peak AC Voltage Vm (V)", min: 100, max: 325, step: 25, value: 230 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const alphaDeg = vals.alpha || 60;
      const alphaRad = (alphaDeg * Math.PI) / 180;
      const Vm = vals.vm || 230;
      const Vdc = (Vm / (2 * Math.PI)) * (1 + Math.cos(alphaRad));

      const sx = 50, sy = 160, sw = 620;

      // Axis
      ctx.strokeStyle = "#334155";
      ctx.beginPath(); ctx.moveTo(sx, sy); ctx.lineTo(sx + sw, sy); ctx.stroke();

      // Input Sine reference (dashed)
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const theta = (x / sw) * 4 * Math.PI;
        const y = sy - Math.sin(theta) * 100;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // SCR Output chopped wave
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const theta = (x / sw) * 4 * Math.PI;
        const modCycle = theta % (2 * Math.PI);
        let y = sy;
        if (modCycle >= alphaRad && modCycle <= Math.PI) {
          y = sy - Math.sin(modCycle) * 100;
        }
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      // Gate pulse markers
      for (let cycle = 0; cycle < 2; cycle++) {
        const trigX = sx + ((alphaRad + cycle * 2 * Math.PI) / (4 * Math.PI)) * sw;
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(trigX, sy + 30); ctx.lineTo(trigX, sy + 60); ctx.stroke();
        ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
        ctx.fillText("Gate Trigger Pulse", trigX - 45, sy + 75);
      }

      // Telemetry
      ctx.fillStyle = "#38bdf8"; ctx.font = "13px monospace";
      ctx.fillText(`Firing Angle: ${alphaDeg}° | Conduction Angle: ${180 - alphaDeg}° | Vdc: ${Vdc.toFixed(1)} V`, 50, 310);
    }
  },

  // 8. UJT Relaxation Oscillator
  "ujt-relaxation-oscillator-sim": {
    title: "UJT Relaxation Oscillator & Standoff Trigger Dynamics",
    desc: "Observe the exponential capacitor voltage charging toward VBB until triggering at peak point VP = eta*VBB + VD, firing repetitive pulses at Base-1.",
    isAnimated: true,
    controls: [
      { id: "eta", label: "Standoff Ratio eta", min: 0.51, max: 0.82, step: 0.02, value: 0.65 },
      { id: "r", label: "Timing Resistor R (kOhm)", min: 20, max: 100, step: 5, value: 47 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const eta = vals.eta || 0.65;
      const R = (vals.r || 47) * 1e3;
      const C = 0.1e-6;
      const Vbb = 15;
      const Vp = eta * Vbb + 0.7;
      const Vv = 1.5;
      const T = R * C * Math.log(1 / (1 - eta));
      const freq = 1 / T;

      const sx = 50, sy = 220, sw = 620;

      // Threshold lines
      const yVp = sy - (Vp / Vbb) * 150;
      const yVv = sy - (Vv / Vbb) * 150;
      ctx.strokeStyle = "rgba(239, 68, 68, 0.4)"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(sx, yVp); ctx.lineTo(sx + sw, yVp); ctx.stroke();
      ctx.strokeStyle = "rgba(16, 185, 129, 0.4)";
      ctx.beginPath(); ctx.moveTo(sx, yVv); ctx.lineTo(sx + sw, yVv); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#ef4444"; ctx.font = "11px sans-serif";
      ctx.fillText(`Peak Voltage Vp = ${Vp.toFixed(2)} V`, sx + 10, yVp - 6);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Valley Voltage Vv = ${Vv.toFixed(2)} V`, sx + 10, yVv + 15);

      // Sawtooth wave on capacitor
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      const periodPx = 140;
      for (let x = 0; x < sw; x++) {
        const phase = (x % periodPx) / periodPx;
        let vCap = 0;
        if (phase < 0.92) {
          vCap = Vv + (Vbb - Vv) * (1 - Math.exp(-phase * 3));
          if (vCap > Vp) vCap = Vp;
        } else {
          vCap = Vp - (Vp - Vv) * ((phase - 0.92) / 0.08); // rapid discharge
        }
        const y = sy - (vCap / Vbb) * 150;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      // Output pulses at B1
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      for (let x = periodPx * 0.92; x < sw; x += periodPx) {
        ctx.beginPath(); ctx.moveTo(sx + x, sy + 30); ctx.lineTo(sx + x, sy + 8); ctx.stroke();
      }

      ctx.fillStyle = "#e2e8f0"; ctx.font = "13px monospace";
      ctx.fillText(`Period T = ${(T * 1000).toFixed(2)} ms | Oscillation Freq f = ${freq.toFixed(1)} Hz`, 50, 310);
    }
  },

  // 9. BJT CE Small-Signal Amplifier Waveforms
  "bjt-ce-amplifier-waveform-sim": {
    title: "Common Emitter Amplifier 180-Degree Phase Inversion",
    desc: "Examine the linear voltage amplification and intrinsic 180-degree phase shift between base input and collector output, noting headroom clipping limits.",
    isAnimated: true,
    controls: [
      { id: "vin", label: "Input Amplitude (mV)", min: 5, max: 50, step: 5, value: 20 },
      { id: "gain", label: "Voltage Gain |Av|", min: 50, max: 250, step: 25, value: 120 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Vin_mV = vals.vin || 20;
      const Av = vals.gain || 120;
      const Vout_V = (Vin_mV * 1e-3) * Av;

      const sx = 60, sy1 = 100, sy2 = 220, sw = 600;

      // Input trace (Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const t = (x / sw) * 4 * Math.PI - time * 6;
        const y = sy1 - Math.sin(t) * (Vin_mV * 1.5);
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px sans-serif";
      ctx.fillText(`Input Signal vin(t) = ${Vin_mV} mV peak`, sx + 10, sy1 - 40);

      // Inverted output trace (Amber)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      const maxClip = 75; // clipping threshold
      for (let x = 0; x < sw; x++) {
        const t = (x / sw) * 4 * Math.PI - time * 6;
        // Inverted: -sin(t)
        let unclipped = -Math.sin(t) * (Vout_V * 25);
        let y = sy2 + Math.max(-maxClip, Math.min(maxClip, unclipped));
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Inverted Output vout(t) = ${Vout_V.toFixed(2)} V peak (180° Out of Phase)`, sx + 10, sy2 - 50);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Voltage Gain Av = -${Av} | Headroom Status: ${Vout_V > 2.8 ? 'CLIPPING DISTORTION' : 'Clean Linear Swing'}`, 60, 315);
    }
  },

  // 10. Class B Push-Pull & Crossover Distortion
  "class-b-push-pull-sim": {
    title: "Push-Pull Amplifier: Class B Crossover vs Class AB Linearization",
    desc: "Observe how the 0.7V VBE barrier causes deadband crossover distortion in pure Class B, and how Class AB diode biasing restores high-fidelity linearity.",
    isAnimated: true,
    controls: [
      { id: "bias", label: "Mode (0: Class B, 1: Class AB)", min: 0, max: 1, step: 1, value: 0 },
      { id: "vin", label: "Input Signal Peak (V)", min: 1.5, max: 8.0, step: 0.5, value: 4.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isClassAB = (vals.bias || 0) === 1;
      const Vin = vals.vin || 4.0;
      const vDead = 0.7;

      const sx = 60, sy = 160, sw = 600;

      // Axis
      ctx.strokeStyle = "#334155";
      ctx.beginPath(); ctx.moveTo(sx, sy); ctx.lineTo(sx + sw, sy); ctx.stroke();

      // Deadband markers if Class B
      if (!isClassAB) {
        ctx.fillStyle = "rgba(239, 68, 68, 0.1)";
        ctx.fillRect(sx, sy - 15, sw, 30);
        ctx.fillStyle = "#ef4444"; ctx.font = "11px sans-serif";
        ctx.fillText("Deadband Zone: -0.7V < Vin < +0.7V (Both Q1 & Q2 OFF)", sx + 130, sy - 22);
      }

      // Output Waveform
      ctx.strokeStyle = isClassAB ? "#10b981" : "#ef4444";
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const t = (x / sw) * 4 * Math.PI - time * 5;
        const vInput = Math.sin(t) * Vin;
        let vOut = 0;
        if (isClassAB) {
          vOut = vInput; // smooth conduction
        } else {
          if (vInput > vDead) vOut = vInput - vDead;
          else if (vInput < -vDead) vOut = vInput + vDead;
          else vOut = 0;
        }
        const y = sy - vOut * 25;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      // Status Banner
      ctx.fillStyle = isClassAB ? "#10b981" : "#ef4444";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText(isClassAB ? "Class AB: Diode Biased (Zero Crossover Distortion)" : "Pure Class B: Unbiased (Severe Crossover Distortion Flaws)", 60, 275);
    }
  },

  // 11. Colpitts LC Resonant Oscillator
  "colpitts-hartley-oscillator-sim": {
    title: "Colpitts LC Oscillator Resonant Tank Energy Exchange",
    desc: "Observe the circulating sinusoidal energy exchange between capacitor electrostatic charge and inductor magnetic flux at resonance frequency f0.",
    isAnimated: true,
    controls: [
      { id: "ind", label: "Inductance L (uH)", min: 5, max: 40, step: 5, value: 15 },
      { id: "c1", label: "Tank Cap C1 (nF)", min: 0.5, max: 5.0, step: 0.5, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const L = (vals.ind || 15) * 1e-6;
      const C1 = (vals.c1 || 1.0) * 1e-9;
      const C2 = 10e-9;
      const Ceq = (C1 * C2) / (C1 + C2);
      const f0 = 1 / (2 * Math.PI * Math.sqrt(L * Ceq));

      const sx = 60, sy = 160, sw = 600;

      // Tank Voltage Oscillation trace
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const t = (x / sw) * 6 * Math.PI - time * 12;
        const y = sy - Math.sin(t) * 70;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      // Energy Bar Graphs (Electric vs Magnetic)
      const phase = (time * 12) % (Math.PI * 2);
      const eElec = Math.pow(Math.cos(phase), 2);
      const eMag = Math.pow(Math.sin(phase), 2);

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Capacitor Electric Field (0.5 C v^2)", 80, 245);
      ctx.fillStyle = "#38bdf8"; ctx.fillRect(80, 255, eElec * 180, 14);

      ctx.fillStyle = "#94a3b8";
      ctx.fillText("Inductor Magnetic Field (0.5 L i^2)", 380, 245);
      ctx.fillStyle = "#f59e0b"; ctx.fillRect(380, 255, eMag * 180, 14);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "13px monospace";
      ctx.fillText(`Equivalent Ceq: ${(Ceq * 1e9).toFixed(3)} nF | Resonant Freq f0: ${(f0 / 1e6).toFixed(3)} MHz`, 60, 315);
    }
  },

  // 12. Wien Bridge Audio Oscillator
  "wien-bridge-oscillator-sim": {
    title: "Wien Bridge Lead-Lag Network Phase & Magnitude Resonance",
    desc: "Examine how the Wien bridge transfer function peaks at exactly beta = 1/3 with zero net phase shift (phi = 0) at resonance frequency f0 = 1/(2*pi*R*C).",
    isAnimated: true,
    controls: [
      { id: "r", label: "Resistor R (kOhm)", min: 5, max: 50, step: 5, value: 16 },
      { id: "c", label: "Capacitor C (nF)", min: 2, max: 20, step: 2, value: 10 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const R = (vals.r || 16) * 1e3;
      const C = (vals.c || 10) * 1e-9;
      const f0 = 1 / (2 * Math.PI * R * C);

      // Left panel: Frequency response curve (x: 50 to 350)
      const gx = 60, gy = 230, gw = 280, gh = 170;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx, 50, gw, gh);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Frequency (Log Scale)", gx + 80, gy + 20);
      ctx.fillText("Beta Peak = 1/3", gx + 10, 68);

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = 0; px < gw; px++) {
        const normW = Math.pow(10, (px / gw - 0.5) * 2); // 0.1 to 10
        const mag = normW / Math.sqrt(Math.pow(1 - normW * normW, 2) + Math.pow(3 * normW, 2));
        const py = gy - mag * 3 * (gh - 30);
        if (px === 0) ctx.moveTo(gx + px, py); else ctx.lineTo(gx + px, py);
      }
      ctx.stroke();

      // Right panel: Generated Sine Wave (x: 380 to 680)
      const sx = 380, sy = 140, sw = 300;
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const t = (x / sw) * 4 * Math.PI - time * 8;
        const y = sy - Math.sin(t) * 60;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();
      ctx.fillStyle = "#10b981";
      ctx.fillText("Output Sine Wave (Zero Phase Shift at f0)", sx + 10, 50);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "13px monospace";
      ctx.fillText(`Resonant Freq f0 = ${f0.toFixed(1)} Hz | Required Non-inverting Gain Av >= 3`, 60, 310);
    }
  },

  // 13. Amplitude Modulation Envelope
  "am-modulation-envelope-sim": {
    title: "Amplitude Modulation (AM) Time-Domain Envelope & Sidebands",
    desc: "Vary the modulation index ma to observe under-modulation, critical 100% modulation, and envelope phase inversion during over-modulation.",
    isAnimated: true,
    controls: [
      { id: "ma", label: "Modulation Index ma", min: 0.2, max: 1.4, step: 0.1, value: 0.6 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const ma = vals.ma !== undefined ? vals.ma : 0.6;
      const Vc = 50;

      const sx = 60, sy = 160, sw = 600;

      // Draw upper and lower dashed envelope curves
      ctx.strokeStyle = "rgba(245, 158, 11, 0.5)"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const tm = (x / sw) * 4 * Math.PI - time * 3;
        const env = Vc * (1 + ma * Math.cos(tm));
        const y = sy - env;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const tm = (x / sw) * 4 * Math.PI - time * 3;
        const env = Vc * (1 + ma * Math.cos(tm));
        const y = sy + env;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // AM Modulated Waveform
      ctx.strokeStyle = ma > 1.0 ? "#ef4444" : "#38bdf8"; ctx.lineWidth = 1.8;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const tm = (x / sw) * 4 * Math.PI - time * 3;
        const tc = (x / sw) * 48 * Math.PI - time * 36;
        const s = Vc * (1 + ma * Math.cos(tm)) * Math.cos(tc);
        const y = sy - s;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      const eta = (ma * ma) / (2 + ma * ma);
      ctx.fillStyle = ma > 1.0 ? "#ef4444" : "#10b981";
      ctx.font = "bold 13px sans-serif";
      const statusText = ma > 1.0 ? "OVER-MODULATION (Severe Envelope Distortion & Clipping)" : (ma === 1.0 ? "CRITICAL MODULATION (100% Depth)" : "UNDER-MODULATION (Linear Diode Envelope Recovery)");
      ctx.fillText(statusText, 60, 275);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`ma: ${ma.toFixed(2)} | Transmission Efficiency eta: ${(eta * 100).toFixed(1)}% | Sideband Power: ${((ma*ma/2)/(1+ma*ma/2)*100).toFixed(1)}%`, 60, 305);
    }
  },

  // 14. Superheterodyne Receiver Mixer & Image Frequency
  "superheterodyne-mixer-sim": {
    title: "Superheterodyne Receiver: Local Oscillator & Image Rejection",
    desc: "Observe how high-side mixing downconverts incoming RF stations to a fixed 455 kHz IF, and how the RF preselector suppresses image frequencies.",
    isAnimated: true,
    controls: [
      { id: "fs", label: "Tuned Station fs (kHz)", min: 600, max: 1500, step: 50, value: 1000 },
      { id: "q", label: "RF Stage Q-Factor", min: 30, max: 120, step: 10, value: 80 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const fs = vals.fs || 1000;
      const Q = vals.q || 80;
      const fIF = 455;
      const fLO = fs + fIF;
      const fImg = fs + 2 * fIF;
      const rho = (fImg / fs) - (fs / fImg);
      const IRR = Math.sqrt(1 + Math.pow(Q * rho, 2));
      const IRR_dB = 20 * Math.log10(IRR);

      // Spectrum Display
      const sx = 60, sy = 240, sw = 600, sh = 170;
      ctx.strokeStyle = "#334155";
      ctx.beginPath(); ctx.moveTo(sx, sy); ctx.lineTo(sx + sw, sy); ctx.stroke();

      // Station Signal fs (Green)
      const px_fs = sx + ((fs - 500) / 2000) * sw;
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(px_fs, sy); ctx.lineTo(px_fs, sy - 130); ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px sans-serif";
      ctx.fillText(`fs (${fs} kHz)`, px_fs - 30, sy - 140);

      // Local Oscillator fLO (Amber)
      const px_flo = sx + ((fLO - 500) / 2000) * sw;
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(px_flo, sy); ctx.lineTo(px_flo, sy - 160); ctx.stroke();
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`fLO (${fLO} kHz)`, px_flo - 35, sy - 170);

      // Image Frequency fImg (Red)
      const px_fimg = sx + ((fImg - 500) / 2000) * sw;
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 3; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(px_fimg, sy); ctx.lineTo(px_fimg, sy - 90); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444";
      ctx.fillText(`Image fimg (${fImg} kHz)`, px_fimg - 45, sy - 100);

      // RF Filter Response Skirt (Cyan Curve centered on fs)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.6)"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const curFreq = 500 + (x / sw) * 2000;
        const delta = Math.abs(curFreq - fs) / (fs / Q);
        const resp = 1 / Math.sqrt(1 + delta * delta);
        const y = sy - resp * 135;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`IF: ${fIF} kHz | Image Rejection Ratio: ${IRR.toFixed(1)}x (${IRR_dB.toFixed(1)} dB)`, 60, 310);
    }
  },

  // 15. Operational Amplifier Inverting / Non-Inverting
  "opamp-inverting-noninverting-sim": {
    title: "Operational Amplifier Closed-Loop Gain & Rail Saturation",
    desc: "Demonstrate the Virtual Short theorem and compare closed-loop inverting gain (-Rf/R1) with non-inverting gain (1 + Rf/R1) with power supply clipping.",
    isAnimated: true,
    controls: [
      { id: "rf", label: "Feedback Rf (kOhm)", min: 10, max: 100, step: 10, value: 50 },
      { id: "r1", label: "Input R1 (kOhm)", min: 5, max: 25, step: 5, value: 10 },
      { id: "vin", label: "Input Peak Vin (V)", min: 0.5, max: 4.0, step: 0.5, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Rf = vals.rf || 50;
      const R1 = vals.r1 || 10;
      const Vin = vals.vin || 1.5;
      const gainInv = -(Rf / R1);
      const gainNonInv = 1 + (Rf / R1);
      const Vsat = 13.5;

      const sx = 60, sy = 160, sw = 600;

      // Supply rails
      ctx.strokeStyle = "rgba(239, 68, 68, 0.3)"; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(sx, sy - 90); ctx.lineTo(sx + sw, sy - 90);
      ctx.moveTo(sx, sy + 90); ctx.lineTo(sx + sw, sy + 90);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.font = "11px sans-serif";
      ctx.fillText("+Vsat (+13.5V)", sx + 10, sy - 96);
      ctx.fillText("-Vsat (-13.5V)", sx + 10, sy + 104);

      // Input wave (Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const t = (x / sw) * 4 * Math.PI - time * 5;
        const y = sy - Math.sin(t) * (Vin * 12);
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      // Inverting Output wave (Amber)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const t = (x / sw) * 4 * Math.PI - time * 5;
        let vOut = Math.sin(t) * Vin * gainInv;
        vOut = Math.max(-Vsat, Math.min(Vsat, vOut));
        const y = sy - (vOut / Vsat) * 90;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      ctx.fillStyle = "#38bdf8"; ctx.font = "12px sans-serif";
      ctx.fillText(`Input Vin: ${Vin.toFixed(1)} V peak`, sx + 120, sy - 70);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Inverting Vout: Gain = -${(Rf/R1).toFixed(1)}`, sx + 340, sy - 70);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Inverting Gain Av: -${(Rf/R1).toFixed(1)} | Non-inverting Gain Av: +${gainNonInv.toFixed(1)} | Virtual Ground: V- = 0.000 V`, 60, 315);
    }
  },

  // 16. Schmitt Trigger Hysteresis Loop
  "schmitt-trigger-hysteresis-sim": {
    title: "Schmitt Trigger Positive Feedback & Symmetrical Hysteresis",
    desc: "Observe how upper and lower trip points (VUTP and VLTP) prevent false comparator chatter when processing noisy real-world analog inputs.",
    isAnimated: true,
    controls: [
      { id: "r1", label: "R1 (kOhm)", min: 5, max: 40, step: 5, value: 10 },
      { id: "r2", label: "R2 (kOhm)", min: 10, max: 80, step: 10, value: 40 },
      { id: "noise", label: "Noise Amplitude (V)", min: 0.0, max: 1.5, step: 0.1, value: 0.6 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const R1 = vals.r1 || 10;
      const R2 = vals.r2 || 40;
      const noise = vals.noise !== undefined ? vals.noise : 0.6;
      const Vsat = 12.0;
      const beta = R1 / (R1 + R2);
      const Vutp = beta * Vsat;
      const Vltp = -beta * Vsat;
      const Vh = Vutp - Vltp;

      // Left panel: Time Waveforms (x: 50 to 390)
      const sx = 50, sy = 160, sw = 340;
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(sx, 40, sw, 230);

      // Trip levels
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(sx, sy - (Vutp / Vsat) * 80); ctx.lineTo(sx + sw, sy - (Vutp / Vsat) * 80);
      ctx.moveTo(sx, sy - (Vltp / Vsat) * 80); ctx.lineTo(sx + sw, sy - (Vltp / Vsat) * 80);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
      ctx.fillText(`VUTP (+${Vutp.toFixed(2)}V)`, sx + 10, sy - (Vutp / Vsat) * 80 - 4);
      ctx.fillText(`VLTP (${Vltp.toFixed(2)}V)`, sx + 10, sy - (Vltp / Vsat) * 80 + 12);

      // Noisy Sine Input
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      let state = 1;
      for (let x = 0; x < sw; x++) {
        const t = (x / sw) * 4 * Math.PI - time * 4;
        const noisy = Math.sin(t) * 6.0 + (Math.sin(t * 15) * noise);
        const y = sy - (noisy / Vsat) * 80;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      // Clean Square Wave Output
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      let outState = 1;
      for (let x = 0; x < sw; x++) {
        const t = (x / sw) * 4 * Math.PI - time * 4;
        const noisy = Math.sin(t) * 6.0 + (Math.sin(t * 15) * noise);
        if (noisy > Vutp) outState = -1;
        else if (noisy < Vltp) outState = 1;
        const y = sy - outState * 65;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      // Right panel: Hysteresis Loop (x: 430 to 670, y: 40 to 270)
      const hx = 430, hy = 160, hw = 240;
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(hx, 40, hw, 230);
      ctx.beginPath();
      ctx.moveTo(hx, hy); ctx.lineTo(hx + hw, hy);
      ctx.moveTo(hx + hw / 2, 40); ctx.lineTo(hx + hw / 2, 270);
      ctx.stroke();
      ctx.fillStyle = "#94a3b8";
      ctx.fillText("Vin", hx + hw - 25, hy + 18);
      ctx.fillText("Vout", hx + hw / 2 + 8, 55);

      // Rectangular Loop
      const px_utp = hx + hw / 2 + (Vutp / Vsat) * 80;
      const px_ltp = hx + hw / 2 + (Vltp / Vsat) * 80;
      const py_hi = hy - 65;
      const py_lo = hy + 65;

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(px_ltp, py_hi); ctx.lineTo(px_utp, py_hi);
      ctx.lineTo(px_utp, py_lo); ctx.lineTo(px_ltp, py_lo);
      ctx.closePath();
      ctx.stroke();

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Hysteresis Width delta-VH = ${Vh.toFixed(2)} V | Noise Immunity Margin: 100% Chatter Free`, 50, 315);
    }
  }
};

// Simulation Engine Mount Adapter
if (!window.SimulationEngine) {
  window.SimulationEngine = {
    activeAnimations: {}
  };
}

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  if (window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }

  const simConfig = (window.BE_SIMS && window.BE_SIMS[simType]) ||
                    (window.CM_SIMS && window.CM_SIMS[simType]) ||
                    (window.TP_SIMS && window.TP_SIMS[simType]) ||
                    (window.EM_SIMS && window.EM_SIMS[simType]);

  if (!simConfig) {
    console.warn('Simulation not found:', simType);
    return;
  }

  container.innerHTML = '';

  const box = document.createElement('div');
  box.className = 'sim-inline-card';
  box.style.background = '#0c1322';
  box.style.border = '1px solid #1e293b';
  box.style.borderRadius = '12px';
  box.style.padding = '1.5rem';
  box.style.margin = '1.75rem 0';

  const header = document.createElement('div');
  header.style.marginBottom = '1rem';
  header.innerHTML = `
    <h4 style="color:#38bdf8; font-size:1.15rem; margin-bottom:0.35rem; display:flex; align-items:center; gap:0.5rem;">
      ${simConfig.title}
    </h4>
    <p style="color:#94a3b8; font-size:0.9rem; line-height:1.5;">${simConfig.desc}</p>
  `;
  box.appendChild(header);

  const canvas = document.createElement('canvas');
  canvas.width = 720;
  canvas.height = 340;
  canvas.style.width = '100%';
  canvas.style.height = 'auto';
  canvas.style.borderRadius = '8px';
  canvas.style.display = 'block';
  canvas.style.background = '#070b14';
  canvas.style.border = '1px solid #1e293b';
  box.appendChild(canvas);

  const ctrlBar = document.createElement('div');
  ctrlBar.style.display = 'flex';
  ctrlBar.style.flexWrap = 'wrap';
  ctrlBar.style.gap = '1.25rem';
  ctrlBar.style.marginTop = '1rem';
  ctrlBar.style.padding = '0.75rem 1rem';
  ctrlBar.style.background = '#080e1c';
  ctrlBar.style.borderRadius = '8px';
  ctrlBar.style.border = '1px solid #1e293d';

  const currentVals = {};

  if (simConfig.controls && simConfig.controls.length > 0) {
    simConfig.controls.forEach(ctrl => {
      currentVals[ctrl.id] = ctrl.value;

      const wrap = document.createElement('div');
      wrap.style.display = 'flex';
      wrap.style.flexDirection = 'column';
      wrap.style.gap = '0.25rem';
      wrap.style.minWidth = '160px';

      const labelRow = document.createElement('div');
      labelRow.style.display = 'flex';
      labelRow.style.justifyContent = 'space-between';
      labelRow.style.fontSize = '0.82rem';
      labelRow.style.color = '#cbd5e1';

      const titleSpan = document.createElement('span');
      titleSpan.innerText = ctrl.label;
      const valSpan = document.createElement('span');
      valSpan.style.fontFamily = 'monospace';
      valSpan.style.color = '#38bdf8';
      valSpan.innerText = ctrl.value;

      labelRow.appendChild(titleSpan);
      labelRow.appendChild(valSpan);
      wrap.appendChild(labelRow);

      const input = document.createElement('input');
      input.type = 'range';
      input.min = ctrl.min;
      input.max = ctrl.max;
      input.step = ctrl.step;
      input.value = ctrl.value;
      input.style.accentColor = '#38bdf8';
      input.style.cursor = 'pointer';

      input.addEventListener('input', (e) => {
        const v = parseFloat(e.target.value);
        currentVals[ctrl.id] = v;
        valSpan.innerText = v;
        if (!simConfig.isAnimated) {
          simConfig.render(canvas, currentVals, 0);
        }
      });

      wrap.appendChild(input);
      ctrlBar.appendChild(wrap);
    });
  }

  if (simConfig.isAnimated) {
    const animCtrlWrap = document.createElement('div');
    animCtrlWrap.style.display = 'flex';
    animCtrlWrap.style.alignItems = 'flex-end';
    const pauseBtn = document.createElement('button');
    pauseBtn.innerText = '⏸️ Pause';
    pauseBtn.style.padding = '0.4rem 0.8rem';
    pauseBtn.style.background = '#1e293b';
    pauseBtn.style.color = '#38bdf8';
    pauseBtn.style.border = '1px solid #334155';
    pauseBtn.style.borderRadius = '6px';
    pauseBtn.style.cursor = 'pointer';
    pauseBtn.style.fontSize = '0.85rem';

    let isPaused = false;
    pauseBtn.addEventListener('click', () => {
      isPaused = !isPaused;
      pauseBtn.innerText = isPaused ? '▶️ Play' : '⏸️ Pause';
    });
    animCtrlWrap.appendChild(pauseBtn);
    ctrlBar.appendChild(animCtrlWrap);

    box.appendChild(ctrlBar);
    container.appendChild(box);

    let startTime = performance.now();
    let elapsedBeforePause = 0;

    function animLoop(now) {
      if (!document.getElementById(containerId)) return;
      if (!isPaused) {
        const t = (now - startTime) / 1000 + elapsedBeforePause;
        simConfig.render(canvas, currentVals, t);
      }
      window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(animLoop);
    }
    window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(animLoop);
  } else {
    box.appendChild(ctrlBar);
    container.appendChild(box);
    simConfig.render(canvas, currentVals, 0);
  }
};
