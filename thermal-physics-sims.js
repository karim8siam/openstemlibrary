// Thermal Physics Interactive Simulations Engine
// 14 60-FPS Canvas Simulations for Classical Thermodynamics, Radiation & Kinetic Theory

window.TP_SIMS = {

  // 1. Ideal Gas Processes (Isothermal, Adiabatic, Isobaric, Isochoric)
  "ideal-gas-processes-sim": {
    title: "Thermodynamic State Processes: P-V Indicator & Microscopic Piston",
    desc: "Observe real-time molecular kinetic energy and piston work across Isothermal (T=const), Adiabatic (Q=0), Isobaric (P=const), and Isochoric (V=const) transformations.",
    isAnimated: true,
    controls: [
      { id: "process", label: "Process (0:IsoT, 1:Adia, 2:IsoP, 3:IsoV)", min: 0, max: 3, step: 1, value: 0 },
      { id: "volume", label: "Volume (V/V0)", min: 0.6, max: 2.0, step: 0.05, value: 1.0 }
    ],
    particles: null,
    initParticles() {
      this.particles = [];
      for (let i = 0; i < 45; i++) {
        this.particles.push({
          x: 40 + Math.random() * 120,
          y: 60 + Math.random() * 180,
          vx: (Math.random() - 0.5) * 4,
          vy: (Math.random() - 0.5) * 4
        });
      }
    },
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      if (!this.particles) this.initParticles();

      const proc = Math.round(vals.process || 0);
      const V_rel = vals.volume || 1.0;
      const gamma = 1.40;

      // Calculate state (P, V, T) based on process
      let P_rel = 1.0, T_rel = 1.0;
      let procName = "Isothermal (T = const)";
      let procColor = "#38bdf8";

      if (proc === 0) { // Isothermal: P * V = const
        procName = "Isothermal (T = const, Q = W)";
        procColor = "#38bdf8";
        P_rel = 1.0 / V_rel;
        T_rel = 1.0;
      } else if (proc === 1) { // Adiabatic: P * V^gamma = const
        procName = "Adiabatic (Q = 0, PV^γ = const)";
        procColor = "#f59e0b";
        P_rel = 1.0 / Math.pow(V_rel, gamma);
        T_rel = P_rel * V_rel;
      } else if (proc === 2) { // Isobaric: P = const
        procName = "Isobaric (P = const, V/T = const)";
        procColor = "#10b981";
        P_rel = 1.0;
        T_rel = V_rel;
      } else { // Isochoric: V = const (override V_rel visually to 1.0)
        procName = "Isochoric (V = const, W = 0)";
        procColor = "#ec4899";
        const effV = 1.0;
        T_rel = V_rel; // use slider as temperature controller
        P_rel = T_rel;
      }

      // --- Left: Piston-Cylinder Chamber ---
      const cylX = 35, cylY = 50, cylW = 200, cylH = 220;
      const pistonPos = proc === 3 ? 150 : (cylW * 0.35 + (V_rel - 0.6) / 1.4 * (cylW * 0.55));

      // Cylinder Walls
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 4;
      ctx.strokeRect(cylX, cylY, cylW, cylH);

      // Piston Face
      ctx.fillStyle = "#94a3b8";
      ctx.fillRect(cylX + pistonPos, cylY + 2, 16, cylH - 4);
      // Piston Shaft
      ctx.fillStyle = "#64748b";
      ctx.fillRect(cylX + pistonPos + 16, cylY + cylH / 2 - 8, cylW - pistonPos + 40, 16);

      // Gas chamber background glow based on Temperature
      const tempHue = Math.max(180, Math.min(360, 220 - (T_rel - 1.0) * 80));
      ctx.fillStyle = `hsla(${tempHue}, 80%, 45%, 0.15)`;
      ctx.fillRect(cylX + 2, cylY + 2, pistonPos - 2, cylH - 4);

      // Particles Motion
      const speedScale = Math.sqrt(Math.max(0.2, T_rel));
      ctx.fillStyle = T_rel > 1.1 ? "#f87171" : (T_rel < 0.9 ? "#60a5fa" : "#38bdf8");

      this.particles.forEach(p => {
        p.x += p.vx * speedScale;
        p.y += p.vy * speedScale;

        // Boundaries
        if (p.x < cylX + 6) { p.x = cylX + 6; p.vx *= -1; }
        if (p.x > cylX + pistonPos - 6) { p.x = cylX + pistonPos - 6; p.vx *= -1; }
        if (p.y < cylY + 6) { p.y = cylY + 6; p.vy *= -1; }
        if (p.y > cylY + cylH - 6) { p.y = cylY + cylH - 6; p.vy *= -1; }

        ctx.beginPath();
        ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
        ctx.fill();
      });

      // Chamber Info
      ctx.fillStyle = "#f1f5f9";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText(`Gas Chamber: T = ${(T_rel * 300).toFixed(0)} K`, cylX, cylY + cylH + 25);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px sans-serif";
      ctx.fillText(`P = ${(P_rel * 101.3).toFixed(1)} kPa | V = ${(V_rel * 0.025).toFixed(3)} m³`, cylX, cylY + cylH + 42);

      // --- Right: Live P-V Indicator Diagram ---
      const pvX = 330, pvY = 50, pvW = 340, pvH = 220;

      // Axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(pvX, pvY);
      ctx.lineTo(pvX, pvY + pvH);
      ctx.lineTo(pvX + pvW, pvY + pvH);
      ctx.stroke();

      ctx.fillStyle = "#64748b";
      ctx.font = "11px monospace";
      ctx.fillText("Pressure P →", pvX + 10, pvY - 10);
      ctx.fillText("Volume V →", pvX + pvW - 60, pvY + pvH + 20);

      // Draw process reference curves
      const drawCurve = (color, fn, label) => {
        ctx.strokeStyle = color;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        for (let vx = 0.6; vx <= 2.0; vx += 0.05) {
          const px = pvX + ((vx - 0.6) / 1.4) * pvW;
          const py = pvY + pvH - (fn(vx) / 2.0) * (pvH - 30);
          if (vx === 0.6) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();
      };

      // Reference lines
      drawCurve("rgba(56, 189, 248, 0.4)", v => 1.0 / v, "IsoT");
      drawCurve("rgba(245, 158, 11, 0.4)", v => 1.0 / Math.pow(v, gamma), "Adia");
      drawCurve("rgba(16, 185, 129, 0.4)", v => 1.0, "IsoP");

      // Active process path
      ctx.strokeStyle = procColor;
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      for (let vx = 0.6; vx <= Math.min(2.0, V_rel); vx += 0.04) {
        let pVal = 1.0;
        if (proc === 0) pVal = 1.0 / vx;
        else if (proc === 1) pVal = 1.0 / Math.pow(vx, gamma);
        else if (proc === 2) pVal = 1.0;
        else pVal = (vx - 0.6) / 1.4 * 1.5 + 0.4;

        const px = pvX + ((vx - 0.6) / 1.4) * pvW;
        const py = pvY + pvH - (pVal / 2.0) * (pvH - 30);
        if (vx === 0.6) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current State Point
      const curX = pvX + ((V_rel - 0.6) / 1.4) * pvW;
      const curY = pvY + pvH - (P_rel / 2.0) * (pvH - 30);

      ctx.fillStyle = procColor;
      ctx.beginPath();
      ctx.arc(curX, curY, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
      ctx.stroke();

      // Work Done Shadow Area (Integral P dV)
      ctx.fillStyle = `${procColor}22`;
      ctx.beginPath();
      ctx.moveTo(pvX, pvY + pvH);
      for (let vx = 0.6; vx <= V_rel; vx += 0.05) {
        let pVal = proc === 0 ? 1.0 / vx : (proc === 1 ? 1.0 / Math.pow(vx, gamma) : (proc === 2 ? 1.0 : P_rel));
        const px = pvX + ((vx - 0.6) / 1.4) * pvW;
        const py = pvY + pvH - (pVal / 2.0) * (pvH - 30);
        ctx.lineTo(px, py);
      }
      ctx.lineTo(curX, pvY + pvH);
      ctx.closePath();
      ctx.fill();

      // Banner Header
      ctx.fillStyle = procColor;
      ctx.font = "bold 13px sans-serif";
      ctx.fillText(procName, pvX, pvY + pvH + 42);
    }
  },

  // 2. Carnot Engine Cycle (Synchronized P-V & T-S Diagrams)
  "carnot-engine-sim": {
    title: "The 4-Stroke Carnot Engine: Synchronized P-V and T-S Cycle",
    desc: "Follow the reversible 4-stage cycle (Isothermal Exp, Adiabatic Exp, Isothermal Comp, Adiabatic Comp) with synchronized work extraction and theoretical Carnot efficiency.",
    isAnimated: true,
    controls: [
      { id: "th", label: "Hot Reservoir TH (K)", min: 600, max: 1200, step: 25, value: 900 },
      { id: "tc", label: "Cold Reservoir TC (K)", min: 250, max: 450, step: 25, value: 300 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const TH = vals.th || 900;
      const TC = vals.tc || 300;
      const eta = 1.0 - (TC / TH);

      // Cycle phase (0 to 4 across 8-second loop)
      const cyclePhase = ((time * 0.5) % 4);
      const stageIdx = Math.floor(cyclePhase);
      const stageFrac = cyclePhase - stageIdx;

      const stages = [
        { name: "1. Isothermal Expansion (TH)", color: "#ef4444", res: "Hot Res (TH)", heat: "Q_H absorbed" },
        { name: "2. Adiabatic Expansion (TH → TC)", color: "#f59e0b", res: "Insulated Stand", heat: "Q = 0 (Gas cools)" },
        { name: "3. Isothermal Compression (TC)", color: "#38bdf8", res: "Cold Res (TC)", heat: "Q_C rejected" },
        { name: "4. Adiabatic Compression (TC → TH)", color: "#10b981", res: "Insulated Stand", heat: "Q = 0 (Gas warms)" }
      ];

      const curStage = stages[stageIdx];

      // --- Left: Mechanical Engine Visualization ---
      const engX = 30, engY = 50, engW = 180, engH = 200;

      // Thermal Reservoir Base
      ctx.fillStyle = stageIdx === 0 ? "#ef4444" : (stageIdx === 2 ? "#38bdf8" : "#334155");
      ctx.fillRect(engX + 20, engY + engH - 30, engW - 40, 25);
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 11px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(curStage.res, engX + engW / 2, engY + engH - 14);
      ctx.textAlign = "left";

      // Cylinder
      ctx.strokeStyle = "#64748b";
      ctx.lineWidth = 3;
      ctx.strokeRect(engX + 30, engY + 20, engW - 60, engH - 55);

      // Piston height in cylinder
      let pistonY = engY + 60;
      if (stageIdx === 0) pistonY = engY + 60 + stageFrac * 35;
      else if (stageIdx === 1) pistonY = engY + 95 + stageFrac * 40;
      else if (stageIdx === 2) pistonY = engY + 135 - stageFrac * 35;
      else pistonY = engY + 100 - stageFrac * 40;

      // Gas region
      ctx.fillStyle = curStage.color + "33";
      ctx.fillRect(engX + 32, pistonY + 14, engW - 64, (engY + engH - 35) - (pistonY + 14));

      // Piston block & connecting rod
      ctx.fillStyle = "#94a3b8";
      ctx.fillRect(engX + 32, pistonY, engW - 64, 14);

      // Crankshaft wheel
      const crankAngle = cyclePhase * Math.PI / 2;
      const crankCx = engX + engW / 2, crankCy = engY - 10;
      ctx.strokeStyle = "#475569";
      ctx.beginPath();
      ctx.arc(crankCx, crankCy, 16, 0, Math.PI * 2);
      ctx.stroke();

      // Connecting Rod
      ctx.strokeStyle = "#cbd5e1";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(crankCx + Math.cos(crankAngle) * 14, crankCy + Math.sin(crankAngle) * 14);
      ctx.lineTo(engX + engW / 2, pistonY);
      ctx.stroke();

      // Engine Status Box
      ctx.fillStyle = curStage.color;
      ctx.font = "bold 12px sans-serif";
      ctx.fillText(curStage.name, engX, engY + engH + 20);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px sans-serif";
      ctx.fillText(curStage.heat, engX, engY + engH + 36);

      // --- Middle: P-V Indicator Loop ---
      const pvX = 240, pvY = 60, pvW = 210, pvH = 170;
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.strokeRect(pvX, pvY, pvW, pvH);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px monospace";
      ctx.fillText("P-V Diagram (Area = W)", pvX + 10, pvY - 10);

      // Carnot 4 Corner points in PV space
      const pA = { x: pvX + 35, y: pvY + 30 };
      const pB = { x: pvX + 115, y: pvY + 60 };
      const pC = { x: pvX + 185, y: pvY + 140 };
      const pD = { x: pvX + 85, y: pvY + 115 };

      // Draw PV loop
      ctx.lineWidth = 2;
      ctx.strokeStyle = "#ef4444";
      ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pB.x, pB.y); ctx.stroke(); // A->B
      ctx.strokeStyle = "#f59e0b";
      ctx.beginPath(); ctx.moveTo(pB.x, pB.y); ctx.lineTo(pC.x, pC.y); ctx.stroke(); // B->C
      ctx.strokeStyle = "#38bdf8";
      ctx.beginPath(); ctx.moveTo(pC.x, pC.y); ctx.lineTo(pD.x, pD.y); ctx.stroke(); // C->D
      ctx.strokeStyle = "#10b981";
      ctx.beginPath(); ctx.moveTo(pD.x, pD.y); ctx.lineTo(pA.x, pA.y); ctx.stroke(); // D->A

      // Enclosed work fill
      ctx.fillStyle = "rgba(56, 189, 248, 0.12)";
      ctx.beginPath();
      ctx.moveTo(pA.x, pA.y); ctx.lineTo(pB.x, pB.y); ctx.lineTo(pC.x, pC.y); ctx.lineTo(pD.x, pD.y);
      ctx.closePath();
      ctx.fill();

      // Current PV point
      let curPV = { x: pA.x, y: pA.y };
      if (stageIdx === 0) curPV = { x: pA.x + (pB.x - pA.x) * stageFrac, y: pA.y + (pB.y - pA.y) * stageFrac };
      else if (stageIdx === 1) curPV = { x: pB.x + (pC.x - pB.x) * stageFrac, y: pB.y + (pC.y - pB.y) * stageFrac };
      else if (stageIdx === 2) curPV = { x: pC.x + (pD.x - pC.x) * stageFrac, y: pC.y + (pD.y - pC.y) * stageFrac };
      else curPV = { x: pD.x + (pA.x - pD.x) * stageFrac, y: pD.y + (pA.y - pD.y) * stageFrac };

      ctx.fillStyle = "#ffffff";
      ctx.beginPath(); ctx.arc(curPV.x, curPV.y, 5, 0, Math.PI * 2); ctx.fill();

      // --- Right: T-S Rectangular Diagram ---
      const tsX = 485, tsY = 60, tsW = 205, tsH = 170;
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.strokeRect(tsX, tsY, tsW, tsH);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px monospace";
      ctx.fillText("T-S Diagram (Exact Rectangle)", tsX + 10, tsY - 10);

      const tsRect = {
        x1: tsX + 40,
        x2: tsX + tsW - 40,
        yTop: tsY + 35,
        yBot: tsY + tsH - 35
      };

      // Fill work area = (TH - TC) * DeltaS
      ctx.fillStyle = "rgba(16, 185, 129, 0.15)";
      ctx.fillRect(tsRect.x1, tsRect.yTop, tsRect.x2 - tsRect.x1, tsRect.yBot - tsRect.yTop);

      // Draw T-S Rectangle
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = "#ef4444"; // Isothermal TH
      ctx.beginPath(); ctx.moveTo(tsRect.x1, tsRect.yTop); ctx.lineTo(tsRect.x2, tsRect.yTop); ctx.stroke();
      ctx.strokeStyle = "#f59e0b"; // Adiabatic cooling
      ctx.beginPath(); ctx.moveTo(tsRect.x2, tsRect.yTop); ctx.lineTo(tsRect.x2, tsRect.yBot); ctx.stroke();
      ctx.strokeStyle = "#38bdf8"; // Isothermal TC
      ctx.beginPath(); ctx.moveTo(tsRect.x2, tsRect.yBot); ctx.lineTo(tsRect.x1, tsRect.yBot); ctx.stroke();
      ctx.strokeStyle = "#10b981"; // Adiabatic heating
      ctx.beginPath(); ctx.moveTo(tsRect.x1, tsRect.yBot); ctx.lineTo(tsRect.x1, tsRect.yTop); ctx.stroke();

      // Current TS point
      let curTS = { x: tsRect.x1, y: tsRect.yTop };
      if (stageIdx === 0) curTS = { x: tsRect.x1 + (tsRect.x2 - tsRect.x1) * stageFrac, y: tsRect.yTop };
      else if (stageIdx === 1) curTS = { x: tsRect.x2, y: tsRect.yTop + (tsRect.yBot - tsRect.yTop) * stageFrac };
      else if (stageIdx === 2) curTS = { x: tsRect.x2 - (tsRect.x2 - tsRect.x1) * stageFrac, y: tsRect.yBot };
      else curTS = { x: tsRect.x1, y: tsRect.yBot - (tsRect.yBot - tsRect.yTop) * stageFrac };

      ctx.fillStyle = "#ffffff";
      ctx.beginPath(); ctx.arc(curTS.x, curTS.y, 5, 0, Math.PI * 2); ctx.fill();

      // Efficiency Metrics Box
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(tsX, tsY + tsH + 10, tsW, 45);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(tsX, tsY + tsH + 10, tsW, 45);
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px monospace";
      ctx.fillText(`η = 1 - TC/TH = ${(eta * 100).toFixed(1)}%`, tsX + 12, tsY + tsH + 28);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "10px sans-serif";
      ctx.fillText(`TH = ${TH} K | TC = ${TC} K`, tsX + 12, tsY + tsH + 44);
    }
  },

  // 3. Refrigerator and Heat Pump (COP Analysis)
  "refrigerator-heat-pump-sim": {
    title: "Reversed Carnot Cycle: Refrigerator & Heat Pump Performance",
    desc: "Examine mechanical work consumption, heat extraction QC from cold spaces, and rejection QH to warm ambient air with live COP comparisons.",
    isAnimated: true,
    controls: [
      { id: "tc", label: "Cold Space TC (K)", min: 250, max: 285, step: 1, value: 268 },
      { id: "th", label: "Ambient Space TH (K)", min: 290, max: 330, step: 1, value: 300 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const TC = vals.tc || 268;
      const TH = vals.th || 300;
      const deltaT = TH - TC;
      const copRef = TC / deltaT;
      const copHp = TH / deltaT;

      // Diagram Layout
      const midX = w / 2, midY = h / 2 - 20;

      // Cold Space (Left)
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.fillRect(50, 60, 160, 160);
      ctx.strokeRect(50, 60, 160, 160);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 14px sans-serif";
      ctx.fillText("Cold Compartment", 65, 90);
      ctx.fillStyle = "#e0f2fe";
      ctx.font = "12px monospace";
      ctx.fillText(`TC = ${TC} K (${(TC - 273.15).toFixed(1)}°C)`, 65, 115);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px sans-serif";
      ctx.fillText("Food Storage / Evaporator", 65, 140);

      // Hot Space (Right)
      ctx.fillStyle = "rgba(239, 68, 68, 0.15)";
      ctx.strokeStyle = "#ef4444";
      ctx.fillRect(510, 60, 160, 160);
      ctx.strokeRect(510, 60, 160, 160);

      ctx.fillStyle = "#ef4444";
      ctx.font = "bold 14px sans-serif";
      ctx.fillText("Warm Ambient Room", 525, 90);
      ctx.fillStyle = "#fee2e2";
      ctx.font = "12px monospace";
      ctx.fillText(`TH = ${TH} K (${(TH - 273.15).toFixed(1)}°C)`, 525, 115);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px sans-serif";
      ctx.fillText("Condenser Coils / Living Space", 525, 140);

      // Center Compressor Cycle
      ctx.fillStyle = "#1e293b";
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.arc(midX, midY, 55, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#f59e0b";
      ctx.font = "bold 13px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("Refrigerant", midX, midY - 10);
      ctx.fillText("Compressor", midX, midY + 8);
      ctx.font = "11px monospace";
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText("W_in", midX, midY + 28);
      ctx.textAlign = "left";

      // Animated Energy Flow Arrows
      const flowOffset = (time * 60) % 20;

      // 1. Heat extraction QC (Left to Center)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(210, midY); ctx.lineTo(midX - 55, midY);
      ctx.stroke();

      // Moving tracer dots
      ctx.fillStyle = "#38bdf8";
      for (let x = 220 + flowOffset; x < midX - 55; x += 30) {
        ctx.beginPath(); ctx.arc(x, midY, 4, 0, Math.PI * 2); ctx.fill();
      }
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText("Q_C (Heat Extracted)", 230, midY - 12);

      // 2. Work Input W_in (Top to Center)
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(midX, 20); ctx.lineTo(midX, midY - 55);
      ctx.stroke();
      ctx.fillStyle = "#f59e0b";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText("Electrical Work W_in", midX + 10, 35);

      // 3. Heat Rejection QH (Center to Right)
      ctx.strokeStyle = "#ef4444";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(midX + 55, midY); ctx.lineTo(510, midY);
      ctx.stroke();

      ctx.fillStyle = "#ef4444";
      for (let x = midX + 65 + flowOffset; x < 500; x += 30) {
        ctx.beginPath(); ctx.arc(x, midY, 4, 0, Math.PI * 2); ctx.fill();
      }
      ctx.font = "bold 12px sans-serif";
      ctx.fillText("Q_H = Q_C + W", midX + 65, midY - 12);

      // Bottom Metrics Cards
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(80, h - 75, 260, 60);
      ctx.strokeRect(80, h - 75, 260, 60);
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("Refrigerator COP (β):", 95, h - 52);
      ctx.font = "13px monospace";
      ctx.fillText(`β = TC / (TH - TC) = ${copRef.toFixed(2)}`, 95, h - 30);

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(380, h - 75, 260, 60);
      ctx.strokeRect(380, h - 75, 260, 60);
      ctx.fillStyle = "#10b981";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("Heat Pump COP:", 395, h - 52);
      ctx.font = "13px monospace";
      ctx.fillText(`COP_hp = β + 1 = ${copHp.toFixed(2)}`, 395, h - 30);
    }
  },

  // 4. Entropy of Mixing & Particle Diffusion
  "entropy-mixing-sim": {
    title: "Irreversible Entropy Growth: Inter-Diffusion of Distinct Gases",
    desc: "Observe spontaneous irreversible mixing of two gas species upon partition removal, verifying universal entropy production ΔS_univ > 0.",
    isAnimated: true,
    controls: [
      { id: "state", label: "Partition (0: Open/Mixing, 1: Closed)", min: 0, max: 1, step: 1, value: 0 },
      { id: "speed", label: "Thermal Velocity (T)", min: 1, max: 5, step: 0.5, value: 2.5 }
    ],
    particles: null,
    initParticles() {
      this.particles = [];
      // 40 Red particles on left
      for (let i = 0; i < 45; i++) {
        this.particles.push({
          x: 40 + Math.random() * 260,
          y: 40 + Math.random() * 220,
          vx: (Math.random() - 0.5) * 3,
          vy: (Math.random() - 0.5) * 3,
          color: "#f87171",
          type: "A"
        });
      }
      // 40 Blue particles on right
      for (let i = 0; i < 45; i++) {
        this.particles.push({
          x: 360 + Math.random() * 260,
          y: 40 + Math.random() * 220,
          vx: (Math.random() - 0.5) * 3,
          vy: (Math.random() - 0.5) * 3,
          color: "#38bdf8",
          type: "B"
        });
      }
    },
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      if (!this.particles) this.initParticles();

      const isClosed = Math.round(vals.state || 0) === 1;
      const spd = vals.speed || 2.5;

      const boxX = 35, boxY = 40, boxW = 650, boxH = 220;
      const midX = boxX + boxW / 2;

      // Outer chamber
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 3;
      ctx.strokeRect(boxX, boxY, boxW, boxH);

      // Partition
      if (isClosed) {
        ctx.fillStyle = "#94a3b8";
        ctx.fillRect(midX - 4, boxY + 2, 8, boxH - 4);
      } else {
        ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(midX, boxY); ctx.lineTo(midX, boxY + boxH);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Update & Render Particles
      let leftCountA = 0, rightCountA = 0;
      let leftCountB = 0, rightCountB = 0;

      this.particles.forEach(p => {
        p.x += p.vx * (spd / 2.0);
        p.y += p.vy * (spd / 2.0);

        // Wall collisions
        if (p.x < boxX + 5) { p.x = boxX + 5; p.vx *= -1; }
        if (p.x > boxX + boxW - 5) { p.x = boxX + boxW - 5; p.vx *= -1; }
        if (p.y < boxY + 5) { p.y = boxY + 5; p.vy *= -1; }
        if (p.y > boxY + boxH - 5) { p.y = boxY + boxH - 5; p.vy *= -1; }

        // Partition collisions if closed
        if (isClosed) {
          if (p.type === "A" && p.x > midX - 7) { p.x = midX - 7; p.vx *= -1; }
          if (p.type === "B" && p.x < midX + 7) { p.x = midX + 7; p.vx *= -1; }
        }

        // Tally distribution
        if (p.x < midX) {
          if (p.type === "A") leftCountA++; else leftCountB++;
        } else {
          if (p.type === "A") rightCountA++; else rightCountB++;
        }

        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, 4, 0, Math.PI * 2);
        ctx.fill();
      });

      // Calculate instantaneous mixing entropy fraction
      const totalA = leftCountA + rightCountA;
      const totalB = leftCountB + rightCountB;
      const fracA_left = leftCountA / totalA;
      const fracB_right = rightCountB / totalB;
      const mixDegree = 1.0 - (Math.abs(fracA_left - 0.5) + Math.abs(fracB_right - 0.5));

      // Info Footer
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(boxX, h - 65, boxW, 50);
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(boxX, h - 65, boxW, 50);

      ctx.fillStyle = "#f59e0b";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText(`Entropy of Mixing: ΔS = 2 n R ln(2) · ${(mixDegree).toFixed(2)}`, boxX + 15, h - 42);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px sans-serif";
      ctx.fillText(isClosed ? "Status: Separated by Adiabatic Partition (Zero Mixing)" : "Status: Free Inter-Diffusion In Progress (Spontaneous Irreversible Process)", boxX + 15, h - 24);
    }
  },

  // 5. Adiabatic Demagnetization Cryogenic Cooling
  "adiabatic-demag-sim": {
    title: "Adiabatic Demagnetization: Sub-Millikelvin Cooling of Paramagnetic Spins",
    desc: "Simulate spin entropy reduction during isothermal magnetization (H ↑) and subsequent drastic lattice temperature drop upon adiabatic demagnetization (H → 0).",
    isAnimated: true,
    controls: [
      { id: "field", label: "Magnetic Field H (Tesla)", min: 0, max: 4.0, step: 0.1, value: 0 },
      { id: "stage", label: "Mode (0: Adiabatic H→0, 1: Isothermal H↑)", min: 0, max: 1, step: 1, value: 0 }
    ],
    spins: null,
    initSpins() {
      this.spins = [];
      for (let i = 0; i < 70; i++) {
        this.spins.push({
          x: 40 + (i % 10) * 28,
          y: 65 + Math.floor(i / 10) * 26,
          angle: Math.random() * Math.PI * 2
        });
      }
    },
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      if (!this.spins) this.initSpins();

      const H = vals.field || 0;
      const isIso = Math.round(vals.stage || 0) === 1;

      // Internal local field
      const h_int = 0.05;
      const Ti = 1.2; // starting liquid He bath temperature

      // Temperature based on thermodynamic demagnetization formula
      let T_cur = Ti;
      if (!isIso) {
        // Adiabatic: T = Ti * sqrt(H^2 + h_int^2) / sqrt(H_max^2 + h_int^2)
        T_cur = Ti * Math.sqrt(H * H + h_int * h_int) / Math.sqrt(4.0 * 4.0 + h_int * h_int);
      }

      // --- Left: Magnetic Spin Lattice ---
      const latX = 35, latY = 45, latW = 310, latH = 220;
      ctx.fillStyle = "#0f172a";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(latX, latY, latW, latH);
      ctx.strokeRect(latX, latY, latW, latH);

      // Magnetic field coil indicators
      if (H > 0.2) {
        ctx.fillStyle = "rgba(56, 189, 248, 0.1)";
        ctx.fillRect(latX, latY, latW, latH);
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 1;
        for (let y = latY + 20; y < latY + latH; y += 35) {
          ctx.beginPath();
          ctx.moveTo(latX + 10, y); ctx.lineTo(latX + latW - 10, y);
          ctx.stroke();
        }
      }

      // Draw atomic magnetic dipole vectors
      this.spins.forEach(s => {
        // Alignment probability driven by H / T
        const targetAngle = 0; // pointing right (along field)
        const disorder = Math.min(Math.PI, 1.2 / (1.0 + H * 4.0));
        const noise = (Math.sin(time * 5 + s.x) * disorder);
        const finalAngle = targetAngle + noise;

        const len = 9;
        const x2 = s.x + Math.cos(finalAngle) * len;
        const y2 = s.y + Math.sin(finalAngle) * len;

        ctx.strokeStyle = H > 1.5 ? "#38bdf8" : "#f59e0b";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(s.x, s.y); ctx.lineTo(x2, y2);
        ctx.stroke();

        ctx.fillStyle = ctx.strokeStyle;
        ctx.beginPath(); ctx.arc(x2, y2, 2.5, 0, Math.PI * 2); ctx.fill();
      });

      // --- Right: Thermodynamic State Readouts ---
      const infoX = 375, infoY = 45, infoW = 310, infoH = 220;
      ctx.fillStyle = "#0c1322";
      ctx.strokeStyle = "#1e293b";
      ctx.fillRect(infoX, infoY, infoW, infoH);
      ctx.strokeRect(infoX, infoY, infoW, infoH);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 15px sans-serif";
      ctx.fillText("Paramagnetic Salt Crystal", infoX + 15, infoY + 28);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px sans-serif";
      ctx.fillText(`Applied Field: H = ${H.toFixed(2)} Tesla`, infoX + 15, infoY + 60);
      ctx.fillText(`Internal Local Field: h_int = 0.05 Tesla`, infoX + 15, infoY + 82);

      // Temperature display with cryogenic color coding
      const isUltraCold = T_cur < 0.1;
      ctx.fillStyle = isUltraCold ? "#7dd3fc" : (T_cur < 0.8 ? "#38bdf8" : "#f59e0b");
      ctx.font = "bold 18px monospace";
      ctx.fillText(`Temperature: ${(T_cur * 1000).toFixed(1)} mK`, infoX + 15, infoY + 125);

      ctx.font = "11px sans-serif";
      ctx.fillStyle = "#94a3b8";
      if (isIso) {
        ctx.fillText("Mode: Isothermal Magnetization (Spins Align)", infoX + 15, infoY + 160);
        ctx.fillText("Heat of alignment dumped into He-4 bath", infoX + 15, infoY + 178);
      } else {
        ctx.fillText("Mode: Adiabatic Demagnetization (H → 0)", infoX + 15, infoY + 160);
        ctx.fillText("Spins absorb lattice phonon energy → Deep cooling", infoX + 15, infoY + 178);
      }

      ctx.fillStyle = "#10b981";
      ctx.font = "11px monospace";
      ctx.fillText(`T_final = T_initial · (h_int / H_max)`, infoX + 15, infoY + 205);
    }
  },

  // 6. Clausius-Clapeyron P-T Phase Diagram
  "clapeyron-phase-diagram-sim": {
    title: "Clausius-Clapeyron Phase Boundaries: Water vs Carbon Dioxide",
    desc: "Compare dynamic P-T equilibrium lines. Observe anomalous negative fusion slope for water (ice regelation) vs positive slope for CO2.",
    isAnimated: false,
    controls: [
      { id: "substance", label: "Substance (0: H2O, 1: CO2)", min: 0, max: 1, step: 1, value: 0 },
      { id: "temp", label: "Temperature (K)", min: 200, max: 450, step: 5, value: 273 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isCO2 = Math.round(vals.substance || 0) === 1;
      const T_sel = vals.temp || 273;

      const subName = isCO2 ? "Carbon Dioxide (CO₂)" : "Water (H₂O - Anomalous Fusion Slope)";
      const diagX = 60, diagY = 50, diagW = 400, diagH = 220;

      // Axes
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(diagX, diagY); ctx.lineTo(diagX, diagY + diagH); ctx.lineTo(diagX + diagW, diagY + diagH);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px monospace";
      ctx.fillText("Pressure P (atm) →", diagX + 10, diagY - 10);
      ctx.fillText("Temperature T (K) →", diagX + diagW - 90, diagY + diagH + 20);

      // Triple Point Coordinates in Diagram
      const tpX = diagX + 140, tpY = diagY + 130;
      const critX = diagX + 340, critY = diagY + 30;

      // 1. Sublimation Curve (Solid - Vapor)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(diagX + 20, diagY + diagH - 10);
      ctx.quadraticCurveTo(diagX + 80, diagY + diagH - 20, tpX, tpY);
      ctx.stroke();

      // 2. Vaporization Curve (Liquid - Vapor) terminates at Critical Point
      ctx.strokeStyle = "#f59e0b";
      ctx.beginPath();
      ctx.moveTo(tpX, tpY);
      ctx.quadraticCurveTo(diagX + 240, diagY + 80, critX, critY);
      ctx.stroke();

      // 3. Fusion Curve (Solid - Liquid)
      ctx.strokeStyle = "#10b981";
      ctx.beginPath();
      ctx.moveTo(tpX, tpY);
      if (!isCO2) {
        // Water: Negative slope (tilts backward to the left!)
        ctx.lineTo(tpX - 35, diagY + 10);
      } else {
        // CO2: Positive slope (tilts forward to the right)
        ctx.lineTo(tpX + 50, diagY + 10);
      }
      ctx.stroke();

      // Critical Point & Triple Point Dots
      ctx.fillStyle = "#ec4899";
      ctx.beginPath(); ctx.arc(critX, critY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.beginPath(); ctx.arc(tpX, tpY, 5, 0, Math.PI * 2); ctx.fill();

      // Region Labels
      ctx.font = "bold 13px sans-serif";
      ctx.fillStyle = "#60a5fa"; ctx.fillText("SOLID", diagX + 45, diagY + 70);
      ctx.fillStyle = "#34d399"; ctx.fillText("LIQUID", tpX + (isCO2 ? 5 : 20), diagY + 60);
      ctx.fillStyle = "#fbbf24"; ctx.fillText("VAPOR", diagX + 230, diagY + 170);

      // --- Right: Mathematical Slope Analysis ---
      const rx = 490, ry = 50, rw = 200;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(rx, ry, rw, diagH);
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(rx, ry, rw, diagH);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText(subName, rx + 12, ry + 25);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px monospace";
      ctx.fillText("dP/dT = L / (T·Δv)", rx + 12, ry + 60);

      if (!isCO2) {
        ctx.fillStyle = "#10b981";
        ctx.fillText("Ice Fusion: v_liq < v_ice", rx + 12, ry + 95);
        ctx.fillText("Δv < 0  ⟹  dP/dT < 0", rx + 12, ry + 115);
        ctx.fillStyle = "#94a3b8";
        ctx.font = "10px sans-serif";
        ctx.fillText("Pressure lowers melting point", rx + 12, ry + 145);
        ctx.fillText("(Glacier flow & Ice skating)", rx + 12, ry + 162);
      } else {
        ctx.fillStyle = "#f59e0b";
        ctx.fillText("CO₂ Fusion: v_liq > v_sol", rx + 12, ry + 95);
        ctx.fillText("Δv > 0  ⟹  dP/dT > 0", rx + 12, ry + 115);
        ctx.fillStyle = "#94a3b8";
        ctx.font = "10px sans-serif";
        ctx.fillText("Normal substance behavior", rx + 12, ry + 145);
        ctx.fillText("Triple point at 5.11 atm", rx + 12, ry + 162);
      }
    }
  },

  // 7. Fourier 1D Heat Conduction & Compound Walls
  "fourier-conduction-sim": {
    title: "Fourier Conduction & Compound Wall Thermal Resistances",
    desc: "Calculate steady-state temperature gradients T(x) and interface junction temperatures across series material slabs.",
    isAnimated: true,
    controls: [
      { id: "k1", label: "Conductivity Layer 1 (k1)", min: 10, max: 100, step: 5, value: 60 },
      { id: "k2", label: "Conductivity Layer 2 (k2)", min: 1, max: 20, step: 1, value: 5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const k1 = vals.k1 || 60;
      const k2 = vals.k2 || 5;
      const T1 = 380, T2 = 290; // boundary temperatures

      // Two layers of equal thickness L1 = L2 = 1.0 m
      const L1 = 1.0, L2 = 1.0;
      // Interface temperature: Tj = (k1*T1 + k2*T2) / (k1 + k2)
      const Tj = (k1 * T1 + k2 * T2) / (k1 + k2);
      const H_flux = (T1 - T2) / ((L1 / k1) + (L2 / k2));

      // Wall Rendering
      const wallX = 60, wallY = 60, wallW = 380, wallH = 170;
      const midWall = wallX + wallW / 2;

      // Layer 1 (Good conductor)
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(wallX, wallY, wallW / 2, wallH);
      // Layer 2 (Insulator)
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(midWall, wallY, wallW / 2, wallH);

      // Border and Interface Line
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 2;
      ctx.strokeRect(wallX, wallY, wallW, wallH);
      ctx.strokeStyle = "#f59e0b";
      ctx.strokeRect(midWall, wallY, 1, wallH);

      // Temperature Graph Line across wall
      ctx.lineWidth = 3;
      // Section 1
      ctx.strokeStyle = "#ef4444";
      ctx.beginPath();
      ctx.moveTo(wallX, wallY + wallH - ((T1 - 280) / 110) * wallH);
      ctx.lineTo(midWall, wallY + wallH - ((Tj - 280) / 110) * wallH);
      ctx.stroke();

      // Section 2
      ctx.strokeStyle = "#38bdf8";
      ctx.beginPath();
      ctx.moveTo(midWall, wallY + wallH - ((Tj - 280) / 110) * wallH);
      ctx.lineTo(wallX + wallW, wallY + wallH - ((T2 - 280) / 110) * wallH);
      ctx.stroke();

      // Interface Node
      ctx.fillStyle = "#ffffff";
      ctx.beginPath();
      ctx.arc(midWall, wallY + wallH - ((Tj - 280) / 110) * wallH, 5, 0, Math.PI * 2);
      ctx.fill();

      // Animated Heat Flux Arrows
      const arrowPhase = (time * 50) % 40;
      ctx.fillStyle = "#f59e0b";
      for (let x = wallX + 25 + arrowPhase; x < wallX + wallW - 20; x += 40) {
        ctx.beginPath();
        ctx.arc(x, wallY + wallH / 2, 3, 0, Math.PI * 2);
        ctx.fill();
      }

      // Labels on Wall
      ctx.font = "bold 12px sans-serif";
      ctx.fillStyle = "#ef4444"; ctx.fillText(`Hot Side T1 = ${T1} K`, wallX + 10, wallY - 15);
      ctx.fillStyle = "#38bdf8"; ctx.fillText(`Cold Side T2 = ${T2} K`, wallX + wallW - 130, wallY - 15);
      ctx.fillStyle = "#f59e0b"; ctx.fillText(`Junction Tj = ${Tj.toFixed(1)} K`, midWall - 50, wallY + wallH + 25);

      // Right: Calculation Metrics
      const mx = 480, my = 60, mw = 210;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(mx, my, mw, wallH);
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(mx, my, mw, wallH);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("Thermal Resistances:", mx + 15, my + 25);

      ctx.font = "11px monospace";
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`R1 = L1/k1 = ${(L1/k1).toFixed(4)}`, mx + 15, my + 55);
      ctx.fillText(`R2 = L2/k2 = ${(L2/k2).toFixed(4)}`, mx + 15, my + 78);
      ctx.fillText(`R_tot = ${(L1/k1 + L2/k2).toFixed(4)} K/W`, mx + 15, my + 102);

      ctx.fillStyle = "#10b981";
      ctx.fillText(`Heat Flux H = ${H_flux.toFixed(1)} W/m²`, mx + 15, my + 135);
    }
  },

  // 8. Radial Coaxial Steam Pipe Conduction
  "radial-heat-pipe-sim": {
    title: "Radial Heat Conduction: Coaxial Steam Pipe Logarithmic Profile",
    desc: "Examine heat flux through cylindrical insulation pipe walls where area expands with radius, yielding logarithmic temperature gradient T(r) ∝ ln(r2/r1).",
    isAnimated: false,
    controls: [
      { id: "r1", label: "Inner Pipe Radius r1 (cm)", min: 4, max: 10, step: 1, value: 5 },
      { id: "r2", label: "Outer Insulation r2 (cm)", min: 12, max: 25, step: 1, value: 16 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const r1 = (vals.r1 || 5) * 4;
      const r2 = (vals.r2 || 16) * 4;

      const cx = 180, cy = 140;

      // Outer insulation boundary
      ctx.fillStyle = "#1e293b";
      ctx.beginPath(); ctx.arc(cx, cy, r2, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 2;
      ctx.stroke();

      // Inner steam pipe
      ctx.fillStyle = "#ef4444";
      ctx.beginPath(); ctx.arc(cx, cy, r1, 0, Math.PI * 2); ctx.fill();

      // Radial heat flow arrows
      ctx.strokeStyle = "rgba(245, 158, 11, 0.7)";
      ctx.lineWidth = 1.5;
      for (let angle = 0; angle < Math.PI * 2; angle += Math.PI / 4) {
        ctx.beginPath();
        ctx.moveTo(cx + Math.cos(angle) * (r1 + 5), cy + Math.sin(angle) * (r1 + 5));
        ctx.lineTo(cx + Math.cos(angle) * (r2 - 5), cy + Math.sin(angle) * (r2 - 5));
        ctx.stroke();
      }

      // Graph on Right: T(r) Profile
      const gx = 380, gy = 50, gw = 290, gh = 180;
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px monospace";
      ctx.fillText("Temperature T(r) vs Radius r", gx + 10, gy - 10);

      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let r = r1; r <= r2; r += 2) {
        const frac = Math.log(r / r1) / Math.log(r2 / r1);
        const px = gx + ((r - r1) / (r2 - r1)) * gw;
        const py = gy + 20 + frac * (gh - 40);
        if (r === r1) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Equation box
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(gx, gy + gh + 15, gw, 55);
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(gx, gy + gh + 15, gw, 55);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px monospace";
      ctx.fillText("H = 2π k L (T1 - T2) / ln(r2/r1)", gx + 12, gy + gh + 35);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px sans-serif";
      ctx.fillText(`Logarithmic radial gradient confirmed`, gx + 12, gy + gh + 53);
    }
  },

  // 9. Blackbody Spectrum & Wien Peak
  "blackbody-spectrum-sim": {
    title: "Planck Blackbody Radiation Spectrum & Wien's Displacement Law",
    desc: "Sweep temperatures from 1500 K to 9000 K to trace the Planck spectral distribution, visible light rainbow window, and peak wavelength shift.",
    isAnimated: false,
    controls: [
      { id: "temp", label: "Blackbody Temperature (K)", min: 2000, max: 8000, step: 200, value: 5800 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const T = vals.temp || 5800;
      const b_wien = 2.898e-3;
      const lambda_max_nm = (b_wien / T) * 1e9;

      const gx = 60, gy = 50, gw = 600, gh = 210;

      // Axes
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1.5;
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px monospace";
      ctx.fillText("Spectral Exitance u_λ →", gx + 10, gy - 10);
      ctx.fillText("Wavelength λ (nm) →", gx + gw - 130, gy + gh + 22);

      // Visible Spectrum Band (380 to 750 nm)
      const visX1 = gx + (380 / 2000) * gw;
      const visX2 = gx + (750 / 2000) * gw;
      const grad = ctx.createLinearGradient(visX1, 0, visX2, 0);
      grad.addColorStop(0.0, "rgba(147, 51, 234, 0.2)");
      grad.addColorStop(0.2, "rgba(59, 130, 246, 0.2)");
      grad.addColorStop(0.5, "rgba(34, 197, 94, 0.2)");
      grad.addColorStop(0.7, "rgba(234, 179, 8, 0.2)");
      grad.addColorStop(1.0, "rgba(239, 68, 68, 0.2)");
      ctx.fillStyle = grad;
      ctx.fillRect(visX1, gy, visX2 - visX1, gh);

      // Draw Planck Curve
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();

      let maxU = 0;
      const pts = [];
      for (let lam = 50; lam <= 2000; lam += 10) {
        const x = lam * 1e-9;
        // Planck formula proportional factor
        const u = (1 / Math.pow(x, 5)) / (Math.exp(1.4388e-2 / (x * T)) - 1);
        if (u > maxU) maxU = u;
        pts.push({ lam, u });
      }

      pts.forEach((p, idx) => {
        const px = gx + (p.lam / 2000) * gw;
        const py = gy + gh - (p.u / maxU) * (gh - 30);
        if (idx === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      });
      ctx.stroke();

      // Wien Peak Indicator
      const peakX = gx + (lambda_max_nm / 2000) * gw;
      const peakY = gy + 30;
      ctx.fillStyle = "#ec4899";
      ctx.beginPath(); ctx.arc(peakX, peakY, 6, 0, Math.PI * 2); ctx.fill();

      ctx.strokeStyle = "#ec4899";
      ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(peakX, peakY); ctx.lineTo(peakX, gy + gh); ctx.stroke();
      ctx.setLineDash([]);

      // Status Bar
      ctx.fillStyle = "#f1f5f9";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText(`T = ${T} K (Solar Photosphere ~5778 K)`, gx, gy + gh + 42);
      ctx.fillStyle = "#ec4899";
      ctx.font = "12px monospace";
      ctx.fillText(`Wien Peak: λ_max = ${lambda_max_nm.toFixed(1)} nm`, gx + 300, gy + gh + 42);
    }
  },

  // 10. Solar Radiation Balance & Planetary Temperature
  "solar-radiation-balance-sim": {
    title: "Planetary Radiation Budget & Greenhouse Equilibrium",
    desc: "Calculate planetary equilibrium temperature from Solar flux, Bond albedo reflection, and greenhouse gas infrared atmospheric absorption.",
    isAnimated: false,
    controls: [
      { id: "albedo", label: "Planetary Albedo A", min: 0.1, max: 0.7, step: 0.05, value: 0.3 },
      { id: "greenhouse", label: "Greenhouse Gas Opacity", min: 0.0, max: 0.9, step: 0.05, value: 0.77 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const S = 1361; // Solar constant W/m2
      const A = vals.albedo || 0.3;
      const eps = vals.greenhouse || 0.77;
      const sigma = 5.67e-8;

      // Bare rock equilibrium temp: T_bare = [S(1-A)/(4*sigma)]^0.25
      const T_bare = Math.pow((S * (1 - A)) / (4 * sigma), 0.25);
      // Greenhouse surface temp: T_surf = T_bare / (1 - eps/2)^0.25
      const T_surf = T_bare / Math.pow(1 - eps / 2, 0.25);

      const earthX = 220, earthY = 150, earthR = 65;

      // Space Background & Sun Beam
      ctx.fillStyle = "#fbbf24";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("Incoming Solar Flux S = 1361 W/m² ➔", 40, 45);

      ctx.strokeStyle = "#fbbf24";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(30, 80); ctx.lineTo(earthX - earthR - 10, 80);
      ctx.stroke();

      // Earth Globe
      ctx.fillStyle = "#1e3a8a";
      ctx.beginPath(); ctx.arc(earthX, earthY, earthR, 0, Math.PI * 2); ctx.fill();

      // Atmosphere Shell (Greenhouse Layer)
      ctx.strokeStyle = `rgba(56, 189, 248, ${0.3 + eps * 0.5})`;
      ctx.lineWidth = 12;
      ctx.beginPath(); ctx.arc(earthX, earthY, earthR + 10, 0, Math.PI * 2); ctx.stroke();

      // Reflected Solar Beam (Albedo)
      ctx.strokeStyle = "#94a3b8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(earthX - earthR, earthY - 30);
      ctx.lineTo(earthX - earthR - 60, earthY - 80);
      ctx.stroke();
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px sans-serif";
      ctx.fillText(`Reflected: ${(A * 100).toFixed(0)}%`, earthX - earthR - 100, earthY - 85);

      // Outgoing Thermal IR
      ctx.strokeStyle = "#ef4444";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(earthX + earthR, earthY);
      ctx.lineTo(earthX + earthR + 50, earthY);
      ctx.stroke();
      ctx.fillStyle = "#ef4444";
      ctx.fillText("Outgoing Infrared", earthX + earthR + 55, earthY + 4);

      // Right: Calculation Summary Card
      const rx = 440, ry = 50, rw = 250;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(rx, ry, rw, 210);
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(rx, ry, rw, 210);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 14px sans-serif";
      ctx.fillText("Planetary Temperature:", rx + 15, ry + 28);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px sans-serif";
      ctx.fillText(`Without Atmosphere:`, rx + 15, ry + 65);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "13px monospace";
      ctx.fillText(`${T_bare.toFixed(1)} K (${(T_bare - 273.15).toFixed(1)}°C)`, rx + 15, ry + 88);

      ctx.fillStyle = "#10b981";
      ctx.font = "12px sans-serif";
      ctx.fillText(`With Greenhouse Gases:`, rx + 15, ry + 125);
      ctx.font = "bold 15px monospace";
      ctx.fillText(`${T_surf.toFixed(1)} K (${(T_surf - 273.15).toFixed(1)}°C)`, rx + 15, ry + 150);

      ctx.fillStyle = "#f59e0b";
      ctx.font = "11px monospace";
      ctx.fillText(`Greenhouse Warming: +${(T_surf - T_bare).toFixed(1)}°C`, rx + 15, ry + 185);
    }
  },

  // 11. Mean Free Path & Kinetic Collisions
  "mean-free-path-sim": {
    title: "Kinetic Theory Chamber: Mean Free Path & Collision Tracking",
    desc: "Track the zigzag trajectory of a single test molecule colliding in a 2D gas to verify λ = 1 / (√2 n π d²).",
    isAnimated: true,
    controls: [
      { id: "density", label: "Gas Density N", min: 25, max: 80, step: 5, value: 45 },
      { id: "diameter", label: "Collision Diameter d", min: 3, max: 9, step: 1, value: 5 }
    ],
    particles: null,
    testTrail: [],
    colCount: 0,
    initSim(density, d) {
      this.particles = [];
      this.testTrail = [];
      this.colCount = 0;
      for (let i = 0; i < density; i++) {
        this.particles.push({
          x: 40 + Math.random() * 320,
          y: 40 + Math.random() * 220,
          vx: (Math.random() - 0.5) * 3,
          vy: (Math.random() - 0.5) * 3,
          isTest: i === 0
        });
      }
    },
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const N = vals.density || 45;
      const d = vals.diameter || 5;

      if (!this.particles || this.particles.length !== N) {
        this.initSim(N, d);
      }

      const boxX = 35, boxY = 40, boxW = 380, boxH = 220;

      // Chamber boundary
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 2;
      ctx.strokeRect(boxX, boxY, boxW, boxH);

      // Move particles
      const testP = this.particles[0];

      this.particles.forEach((p, idx) => {
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < boxX + d) { p.x = boxX + d; p.vx *= -1; }
        if (p.x > boxX + boxW - d) { p.x = boxX + boxW - d; p.vx *= -1; }
        if (p.y < boxY + d) { p.y = boxY + d; p.vy *= -1; }
        if (p.y > boxY + boxH - d) { p.y = boxY + boxH - d; p.vy *= -1; }

        // Test collision with others
        if (p.isTest) {
          for (let j = 1; j < this.particles.length; j++) {
            const o = this.particles[j];
            const dist = Math.hypot(p.x - o.x, p.y - o.y);
            if (dist < d * 2) {
              p.vx *= -1; p.vy *= -1;
              o.vx *= -1; o.vy *= -1;
              this.colCount++;
              this.testTrail.push({ x: p.x, y: p.y });
              if (this.testTrail.length > 25) this.testTrail.shift();
            }
          }
        }

        ctx.fillStyle = p.isTest ? "#ec4899" : "#38bdf8";
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.isTest ? d + 1 : d, 0, Math.PI * 2);
        ctx.fill();
      });

      // Draw Test Molecule Trail
      ctx.strokeStyle = "#ec4899";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      this.testTrail.forEach((pt, i) => {
        if (i === 0) ctx.moveTo(pt.x, pt.y);
        else ctx.lineTo(pt.x, pt.y);
      });
      ctx.stroke();

      // Right: Mathematical Stats
      const sx = 440, sy = 40, sw = 250;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(sx, sy, sw, boxH);
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(sx, sy, sw, boxH);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("Maxwell Mean Free Path:", sx + 15, sy + 25);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px monospace";
      ctx.fillText("λ = 1 / (√2 · n · π · d²)", sx + 15, sy + 55);

      const lambdaEst = 1200 / (N * (d / 5));
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Est. Mean Free Path: ${lambdaEst.toFixed(1)} px`, sx + 15, sy + 85);
      ctx.fillText(`Collision Events: ${this.colCount}`, sx + 15, sy + 110);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px sans-serif";
      ctx.fillText("• λ is inversely proportional to pressure P", sx + 15, sy + 145);
      ctx.fillText("• Gaseous viscosity η is independent of P", sx + 15, sy + 165);
    }
  },

  // 12. Brownian Motion & Einstein Diffusion
  "brownian-motion-sim": {
    title: "Brownian Motion: Fluctuation-Dissipation & Einstein Diffusion",
    desc: "Colloidal pollen particle subjected to thermal solvent collisions, showing linear mean-square displacement growth ⟨r²(t)⟩ = 2Dt.",
    isAnimated: true,
    controls: [
      { id: "temp", label: "Temperature (T)", min: 100, max: 400, step: 25, value: 300 },
      { id: "visc", label: "Viscosity (η)", min: 0.5, max: 2.0, step: 0.1, value: 1.0 }
    ],
    pollen: { x: 200, y: 150, vx: 0, vy: 0 },
    pollenTrail: [],
    msdHistory: [],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const T = vals.temp || 300;
      const eta = vals.visc || 1.0;
      const D = (T / (300 * eta)) * 1.5;

      const boxX = 35, boxY = 40, boxW = 340, boxH = 220;

      // Update Pollen position with Langevin thermal noise + Stokes drag
      this.pollen.vx += (Math.random() - 0.5) * Math.sqrt(D) * 1.2 - this.pollen.vx * 0.1 * eta;
      this.pollen.vy += (Math.random() - 0.5) * Math.sqrt(D) * 1.2 - this.pollen.vy * 0.1 * eta;

      this.pollen.x += this.pollen.vx;
      this.pollen.y += this.pollen.vy;

      // Chamber wall bounce
      if (this.pollen.x < boxX + 15) { this.pollen.x = boxX + 15; this.pollen.vx *= -1; }
      if (this.pollen.x > boxX + boxW - 15) { this.pollen.x = boxX + boxW - 15; this.pollen.vx *= -1; }
      if (this.pollen.y < boxY + 15) { this.pollen.y = boxY + 15; this.pollen.vy *= -1; }
      if (this.pollen.y > boxY + boxH - 15) { this.pollen.y = boxY + boxH - 15; this.pollen.vy *= -1; }

      this.pollenTrail.push({ x: this.pollen.x, y: this.pollen.y });
      if (this.pollenTrail.length > 120) this.pollenTrail.shift();

      // Chamber
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 2;
      ctx.strokeRect(boxX, boxY, boxW, boxH);

      // Pollen Trail
      ctx.strokeStyle = "rgba(245, 158, 11, 0.7)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      this.pollenTrail.forEach((pt, i) => {
        if (i === 0) ctx.moveTo(pt.x, pt.y);
        else ctx.lineTo(pt.x, pt.y);
      });
      ctx.stroke();

      // Pollen Particle
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(this.pollen.x, this.pollen.y, 8, 0, Math.PI * 2);
      ctx.fill();

      // Right: ⟨r²⟩ vs Time Graph
      const gx = 405, gy = 40, gw = 280, gh = 220;
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText("Einstein Diffusion: ⟨x²⟩ = 2 D t", gx + 15, gy + 22);

      // Theoretical slope line
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(gx + 20, gy + gh - 20);
      ctx.lineTo(gx + gw - 20, gy + gh - 20 - (D * 35));
      ctx.stroke();

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px monospace";
      ctx.fillText(`Diffusion D = ${D.toFixed(2)} · 10⁻¹³ m²/s`, gx + 15, gy + 65);
      ctx.fillText(`Stokes Friction: γ = 6πηr`, gx + 15, gy + 88);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px sans-serif";
      ctx.fillText("Perrin verified atoms by measuring", gx + 15, gy + 130);
      ctx.fillText("Avogadro's number N_A from this slope.", gx + 15, gy + 148);
    }
  },

  // 13. Van der Waals Real Gas Isotherms
  "vanderwaals-pv-sim": {
    title: "Van der Waals Real Gas Isotherms & Critical Point",
    desc: "Inspect cubic isotherms across supercritical (T > Tc), critical (T = Tc), and subcritical (T < Tc) regimes with Maxwell equal-area construction.",
    isAnimated: false,
    controls: [
      { id: "tr", label: "Reduced Temperature Tr (T/Tc)", min: 0.8, max: 1.25, step: 0.05, value: 0.95 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Tr = vals.tr || 0.95;

      const gx = 60, gy = 50, gw = 410, gh = 210;

      // Axes
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1.5;
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px monospace";
      ctx.fillText("Reduced Pressure Pr →", gx + 10, gy - 10);
      ctx.fillText("Reduced Volume Vr →", gx + gw - 130, gy + gh + 22);

      // Draw Isotherms using reduced Van der Waals eq: Pr = (8*Tr)/(3*Vr - 1) - 3/Vr^2
      const drawVDW = (tempRatio, color, isBold) => {
        ctx.strokeStyle = color;
        ctx.lineWidth = isBold ? 3.5 : 1.5;
        ctx.beginPath();
        for (let vr = 0.45; vr <= 3.5; vr += 0.04) {
          const pr = (8 * tempRatio) / (3 * vr - 1) - 3 / (vr * vr);
          if (pr < 0 || pr > 3.0) continue;
          const px = gx + ((vr - 0.45) / 3.05) * gw;
          const py = gy + gh - (pr / 2.2) * gh;
          ctx.lineTo(px, py);
        }
        ctx.stroke();
      };

      // Reference Isotherms
      drawVDW(1.20, "rgba(56, 189, 248, 0.35)", false); // T > Tc
      drawVDW(1.00, "#f59e0b", false); // T = Tc (Critical)
      drawVDW(0.85, "rgba(239, 68, 68, 0.35)", false); // T < Tc

      // Active user selected isotherm
      drawVDW(Tr, Tr >= 1.0 ? "#38bdf8" : "#ec4899", true);

      // Critical Point Mark (Pr = 1, Vr = 1)
      const cpx = gx + ((1.0 - 0.45) / 3.05) * gw;
      const cpy = gy + gh - (1.0 / 2.2) * gh;
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(cpx, cpy, 6, 0, Math.PI * 2); ctx.fill();

      // Right: State Details
      const rx = 490, ry = 50, rw = 200;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(rx, ry, rw, gh);
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(rx, ry, rw, gh);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("Reduced Coordinates:", rx + 12, ry + 25);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px monospace";
      ctx.fillText(`Tr = T/Tc = ${Tr.toFixed(2)}`, rx + 12, ry + 55);
      ctx.fillText(`Vc = 3b`, rx + 12, ry + 78);
      ctx.fillText(`Pc = a / 27b²`, rx + 12, ry + 100);
      ctx.fillText(`Zc = 3/8 = 0.375`, rx + 12, ry + 122);

      ctx.fillStyle = Tr < 1.0 ? "#ec4899" : "#38bdf8";
      ctx.font = "11px sans-serif";
      if (Tr < 1.0) {
        ctx.fillText("Regime: Liquid-Vapor", rx + 12, ry + 160);
        ctx.fillText("Coexistence (Tie Line)", rx + 12, ry + 178);
      } else {
        ctx.fillText("Regime: Supercritical Fluid", rx + 12, ry + 160);
        ctx.fillText("(No Phase Boundary)", rx + 12, ry + 178);
      }
    }
  },

  // 14. Joule-Thomson Throttling & Inversion Curve
  "joule-thomson-throttling-sim": {
    title: "Joule-Thomson Throttling Chamber & Inversion Temperature",
    desc: "Observe isenthalpic porous plug throttling expansion (ΔH = 0) with temperature inversion boundary separating cooling (μJT > 0) from heating.",
    isAnimated: true,
    controls: [
      { id: "tin", label: "Inlet Temperature Tin (K)", min: 150, max: 800, step: 25, value: 300 },
      { id: "pin", label: "Inlet Pressure P1 (bar)", min: 20, max: 180, step: 10, value: 120 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Tin = vals.tin || 300;
      const Pin = vals.pin || 120;
      const Ti_max = 600; // Inversion temperature for air / nitrogen

      // Does it cool or heat?
      const willCool = Tin < Ti_max;
      const muJT = (2.0 * 0.137 / (8.314 * Tin) - 3.87e-5) * 1e5; // approximate K/bar
      const Tout = Tin - (willCool ? (Pin * 0.22) : (-Pin * 0.10));

      const chamX = 60, chamY = 60, chamW = 360, chamH = 160;
      const plugX = chamX + chamW / 2;

      // Upstream pipe
      ctx.fillStyle = willCool ? "rgba(56, 189, 248, 0.15)" : "rgba(239, 68, 68, 0.15)";
      ctx.fillRect(chamX, chamY, chamW / 2, chamH);

      // Downstream pipe
      ctx.fillStyle = willCool ? "rgba(56, 189, 248, 0.35)" : "rgba(239, 68, 68, 0.35)";
      ctx.fillRect(plugX, chamY, chamW / 2, chamH);

      // Pipe borders
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 3;
      ctx.strokeRect(chamX, chamY, chamW, chamH);

      // Porous Plug
      ctx.fillStyle = "#94a3b8";
      ctx.fillRect(plugX - 8, chamY + 2, 16, chamH - 4);
      ctx.fillStyle = "#070b14";
      // Porous holes
      for (let y = chamY + 15; y < chamY + chamH; y += 20) {
        ctx.fillRect(plugX - 6, y, 12, 4);
      }

      // Animated Gas Stream Flow
      const flowOffset = (time * 60) % 30;
      ctx.fillStyle = willCool ? "#60a5fa" : "#f87171";
      for (let x = chamX + 20 + flowOffset; x < chamX + chamW - 20; x += 30) {
        ctx.beginPath();
        ctx.arc(x, chamY + chamH / 2, 3.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // Upstream / Downstream Labels
      ctx.font = "bold 12px sans-serif";
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`Inlet: P1 = ${Pin} bar`, chamX + 15, chamY + 30);
      ctx.fillText(`T1 = ${Tin} K`, chamX + 15, chamY + 50);

      ctx.fillStyle = willCool ? "#38bdf8" : "#ef4444";
      ctx.fillText(`Outlet: P2 = 1 bar`, plugX + 15, chamY + 30);
      ctx.fillText(`T2 = ${Tout.toFixed(1)} K (${willCool ? 'Cooling' : 'Heating'})`, plugX + 15, chamY + 50);

      // Right: Inversion Curve Summary
      const rx = 445, ry = 60, rw = 245;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(rx, ry, rw, chamH);
      ctx.strokeStyle = "#1e293b";
      ctx.strokeRect(rx, ry, rw, chamH);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("Joule-Thomson Throttling:", rx + 15, ry + 25);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px monospace";
      ctx.fillText("Process is isenthalpic: ΔH = 0", rx + 15, ry + 50);
      ctx.fillText(`Inversion Temp Ti = 2a/Rb ≈ 600 K`, rx + 15, ry + 75);

      ctx.fillStyle = willCool ? "#10b981" : "#ef4444";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText(willCool ? "Status: Cooling (Tin < Ti)" : "Status: Heating (Tin > Ti)", rx + 15, ry + 110);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px sans-serif";
      ctx.fillText("Basis for industrial air liquefaction", rx + 15, ry + 135);
      ctx.fillText("(Linde-Hampson regenerative cycle).", rx + 15, ry + 148);
    }
  }

};

// Universal Engine Integration Adapter for Thermal Physics
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  if (window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }

  const simConfig = (window.TP_SIMS && window.TP_SIMS[simType]) ||
                    (window.EM_SIMS && window.EM_SIMS[simType]) ||
                    (window.MATTER_SIMS && window.MATTER_SIMS[simType]) ||
                    (window.STATMECH_SIMS && window.STATMECH_SIMS[simType]);
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
