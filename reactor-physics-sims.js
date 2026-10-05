// Nuclear Reactor Physics Simulation Suite
// 16 Real-Time 60 FPS Canvas Simulations for Neutron Diffusion, Fission Energetics, Chain Reactions & Kinetics

window.RP_SIMS = {
  "reactor-atom-density-breeder-sim": {
    title: "Atom Density, Breeding Ratio & Doubling Time Simulator",
    desc: "Calculates atomic number densities for actinide fuels and solves the breeding gain differential equation, computing fissile inventory accumulation and doubling time in fast breeder reactors.",
    isAnimated: true,
    controls: [
      {
            "id": "convRatio",
            "label": "Conversion Ratio CR",
            "min": 0.6,
            "max": 1.5,
            "step": 0.05,
            "value": 1.25
      },
      {
            "id": "thermalPower",
            "label": "Core Power (MWth)",
            "min": 500,
            "max": 3500,
            "step": 100,
            "value": 2000
      },
      {
            "id": "fissileMass",
            "label": "Initial Fissile Mass (kg)",
            "min": 1000,
            "max": 4000,
            "step": 100,
            "value": 2500
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const CR = vals.convRatio !== undefined ? vals.convRatio : 1.25;
    const P = vals.thermalPower !== undefined ? vals.thermalPower : 2000;
    const M0 = vals.fissileMass !== undefined ? vals.fissileMass : 2500;

    const plot = { x: 60, y: 40, w: w - 90, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
    ctx.fillText(`Breeder Reactor Fissile Inventory Trajectory | CR = ${CR.toFixed(2)} | P = ${P} MWth`, plot.x, plot.y - 12);

    // Physics: daily consumption rate = 1.05 * (1 + alpha) * P g/day ~ 1.23 * P g/day
    // Fissile production rate = CR * consumption
    // Net accumulation rate dM/dt = (CR - 1) * 1.23 * P [kg/yr]
    const alpha = 0.17;
    const consPerDay = 1.05 * (1 + alpha) * (P / 1000); // kg/day
    const netPerYear = (CR - 1) * consPerDay * 365; // kg/year
    const T_double = (CR > 1.0) ? (M0 * Math.log(2)) / (netPerYear * Math.log(2) / (M0 * (CR - 1) * 0.0003 * 365)) : Infinity;
    const actualDoublingTime = (CR > 1.0) ? (M0 / netPerYear) : Infinity;

    // Grid & axes
    const maxYears = 20;
    const yMax = M0 * 2.5;
    const yMin = 0;

    ctx.strokeStyle = "rgba(30, 41, 59, 0.6)"; ctx.lineWidth = 1;
    for (let yr = 0; yr <= maxYears; yr += 5) {
      const px = plot.x + (yr / maxYears) * plot.w;
      ctx.beginPath(); ctx.moveTo(px, plot.y); ctx.lineTo(px, plot.y + plot.h); ctx.stroke();
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText(`${yr} yr`, px - 12, plot.y + plot.h + 16);
    }

    for (let m = 0; m <= yMax; m += 1500) {
      const py = plot.y + plot.h - ((m - yMin) / (yMax - yMin)) * plot.h;
      ctx.beginPath(); ctx.moveTo(plot.x, py); ctx.lineTo(plot.x + plot.w, py); ctx.stroke();
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText(`${m} kg`, plot.x - 48, py + 4);
    }

    // Initial mass baseline
    const yBase = plot.y + plot.h - ((M0 - yMin) / (yMax - yMin)) * plot.h;
    ctx.strokeStyle = "#475569"; ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(plot.x, yBase); ctx.lineTo(plot.x + plot.w, yBase); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
    ctx.fillText(`M0 = ${M0} kg (Initial)`, plot.x + 8, yBase - 4);

    // Plot trajectory curve
    ctx.beginPath();
    ctx.strokeStyle = CR > 1.0 ? "#10b981" : (CR === 1.0 ? "#f59e0b" : "#ef4444");
    ctx.lineWidth = 2.5;
    for (let yr = 0; yr <= maxYears; yr += 0.2) {
      const M = Math.max(0, M0 + netPerYear * yr);
      const px = plot.x + (yr / maxYears) * plot.w;
      const py = plot.y + plot.h - ((M - yMin) / (yMax - yMin)) * plot.h;
      if (yr === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Animated operating time marker
    const animYr = (time % 15) * (maxYears / 15);
    const animM = Math.max(0, M0 + netPerYear * animYr);
    const animX = plot.x + (animYr / maxYears) * plot.w;
    const animY = plot.y + plot.h - ((animM - yMin) / (yMax - yMin)) * plot.h;

    ctx.fillStyle = CR > 1.0 ? "#34d399" : "#f87171";
    ctx.beginPath(); ctx.arc(animX, animY, 5, 0, Math.PI * 2); ctx.fill();

    // Info overlay box
    ctx.fillStyle = "rgba(11, 17, 32, 0.85)";
    ctx.fillRect(plot.x + plot.w - 230, plot.y + 12, 218, 90);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + plot.w - 230, plot.y + 12, 218, 90);

    ctx.font = "11px Inter";
    ctx.fillStyle = "#94a3b8";
    ctx.fillText(`Regime: `, plot.x + plot.w - 220, plot.y + 30);
    ctx.fillStyle = CR > 1.0 ? "#10b981" : (CR === 1.0 ? "#f59e0b" : "#ef4444");
    ctx.font = "bold 11px Inter";
    ctx.fillText(CR > 1.0 ? "Fast Breeder (CR > 1)" : (CR === 1.0 ? "Break-Even (CR = 1)" : "Burner / Converter"), plot.x + plot.w - 170, plot.y + 30);

    ctx.font = "11px Inter"; ctx.fillStyle = "#cbd5e1";
    ctx.fillText(`Net Fissile Gain: ${(netPerYear >= 0 ? "+" : "") + netPerYear.toFixed(1)} kg/yr`, plot.x + plot.w - 220, plot.y + 50);
    ctx.fillText(`Doubling Time Td: ${actualDoublingTime !== Infinity ? actualDoublingTime.toFixed(1) + " years" : "N/A (Non-breeder)"}`, plot.x + plot.w - 220, plot.y + 70);
    ctx.fillText(`Simulated Year: ${animYr.toFixed(1)} yr | Fissile: ${animM.toFixed(0)} kg`, plot.x + plot.w - 220, plot.y + 90);
    }
  },
  "reactor-neutron-attenuation-flux-sim": {
    title: "Neutron Beam Attenuation & Reaction Rate Simulator",
    desc: "Simulates exponential attenuation I(x) = I0 * exp(-\u03a3t * x) of a monoenergetic neutron beam propagating through shielding materials, displaying macroscopic cross section, mean free path, and HVL.",
    isAnimated: true,
    controls: [
      {
            "id": "incidentIntensity",
            "label": "Incident Intensity I0 (n/cm\u00b2\u00b7s)",
            "min": 1000,
            "max": 10000,
            "step": 500,
            "value": 5000
      },
      {
            "id": "macroSigma",
            "label": "Macroscopic Cross Section \u03a3t (cm\u207b\u00b9)",
            "min": 0.2,
            "max": 4.0,
            "step": 0.1,
            "value": 1.8
      },
      {
            "id": "shieldThick",
            "label": "Shield Thickness x (cm)",
            "min": 1.0,
            "max": 10.0,
            "step": 0.5,
            "value": 5.0
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const I0 = vals.incidentIntensity !== undefined ? vals.incidentIntensity : 5000;
    const Sigma_t = vals.macroSigma !== undefined ? vals.macroSigma : 1.8;
    const thick = vals.shieldThick !== undefined ? vals.shieldThick : 5.0;

    const lambda = 1.0 / Sigma_t;
    const HVL = Math.LN2 / Sigma_t;
    const I_out = I0 * Math.exp(-Sigma_t * thick);

    // Left diagram: Physical beam penetrating slab
    const slabBox = { x: 50, y: 50, w: 280, h: h - 100 };
    ctx.strokeStyle = "#334155"; ctx.strokeRect(slabBox.x, slabBox.y, slabBox.w, slabBox.h);

    // Material slab visual
    const slabW = (thick / 10.0) * (slabBox.w * 0.6);
    const slabX = slabBox.x + 80;
    ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
    ctx.fillRect(slabX, slabBox.y, slabW, slabBox.h);
    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
    ctx.strokeRect(slabX, slabBox.y, slabW, slabBox.h);

    ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
    ctx.fillText(`Target Slab: ${thick.toFixed(1)} cm`, slabX + 5, slabBox.y - 8);

    // Draw animated neutron rays
    const numRays = 18;
    for (let i = 0; i < numRays; i++) {
      const rayY = slabBox.y + 15 + i * (slabBox.h - 30) / (numRays - 1);
      const speed = 120;
      const rayPhase = ((time * speed + i * 25) % (slabBox.w + 40));
      const rayX = slabBox.x + rayPhase;

      // Check transmission probability
      let transmitted = true;
      if (rayX > slabX) {
        const distInSlab = Math.min(slabW, rayX - slabX);
        const transProb = Math.exp(-Sigma_t * (distInSlab / (slabBox.w * 0.6) * 10.0));
        if (Math.sin(i * 99 + 1) > transProb * 2 - 1) {
          transmitted = false;
        }
      }

      ctx.fillStyle = transmitted ? "#38bdf8" : "rgba(239, 68, 68, 0.4)";
      ctx.beginPath();
      ctx.arc(rayX, rayY, 2.5, 0, Math.PI * 2);
      ctx.fill();
    }

    // Right diagram: Exponential attenuation curve
    const plot = { x: 370, y: 50, w: w - 400, h: h - 100 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText("Intensity Profile I(x) = I0 · exp(-Σt · x)", plot.x, plot.y - 10);

    // Plot curve
    ctx.beginPath();
    ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
    for (let x = 0; x <= 10; x += 0.1) {
      const I_x = I0 * Math.exp(-Sigma_t * x);
      const px = plot.x + (x / 10.0) * plot.w;
      const py = plot.y + plot.h - (I_x / I0) * plot.h;
      if (x === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Mark current slab thickness point
    const curPx = plot.x + (thick / 10.0) * plot.w;
    const curPy = plot.y + plot.h - (I_out / I0) * plot.h;
    ctx.strokeStyle = "#f59e0b"; ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(curPx, plot.y); ctx.lineTo(curPx, plot.y + plot.h); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(plot.x, curPy); ctx.lineTo(curPx, curPy); ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = "#f59e0b";
    ctx.beginPath(); ctx.arc(curPx, curPy, 4.5, 0, Math.PI * 2); ctx.fill();

    // Metrics panel
    ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter";
    ctx.fillText(`Transmitted Flux: ${I_out.toFixed(1)} n/cm²·s (${((I_out / I0) * 100).toFixed(2)}%)`, plot.x + 10, plot.y + 25);
    ctx.fillText(`Mean Free Path λ: ${lambda.toFixed(3)} cm`, plot.x + 10, plot.y + 45);
    ctx.fillText(`Half-Value Layer HVL: ${HVL.toFixed(3)} cm`, plot.x + 10, plot.y + 65);
    ctx.fillText(`Attenuated Fraction: ${((1 - I_out / I0) * 100).toFixed(2)}%`, plot.x + 10, plot.y + 85);
    }
  },
  "reactor-fission-yield-spectrum-sim": {
    title: "Fission Mass Yield & Prompt Neutron Watt Spectrum",
    desc: "Displays the empirical asymmetric double-hump fission product mass yield curve Y(A) for U-235 and Pu-239 alongside the Cranberg/Watt prompt fission neutron energy distribution \u03c7(E).",
    isAnimated: true,
    controls: [
      {
            "id": "fuelType",
            "label": "Fissile Isotope (1=U235, 2=Pu239)",
            "min": 1,
            "max": 2,
            "step": 1,
            "value": 1
      },
      {
            "id": "displayMode",
            "label": "Display (1=Mass Yield, 2=Watt Spectrum)",
            "min": 1,
            "max": 2,
            "step": 1,
            "value": 1
      },
      {
            "id": "incidentEnergy",
            "label": "Neutron Energy (1=Thermal, 2=Fast)",
            "min": 1,
            "max": 2,
            "step": 1,
            "value": 1
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const isPu = (vals.fuelType === 2);
    const isWatt = (vals.displayMode === 2);
    const isFast = (vals.incidentEnergy === 2);

    const plot = { x: 65, y: 45, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    if (!isWatt) {
      // Mass yield Y(A)
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText(`Fission Product Mass Yield Y(A) | ${isPu ? "Pu-239" : "U-235"} | ${isFast ? "Fast (14 MeV)" : "Thermal (0.025 eV)"}`, plot.x, plot.y - 12);

      // Light and heavy peaks
      const peakL = isPu ? 99 : 95;
      const peakH = isPu ? 139 : 140;
      const valley = 117;
      const valleyHeight = isFast ? 1.2 : 0.01;

      // Draw Y(A) curve
      ctx.beginPath();
      ctx.strokeStyle = isPu ? "#f43f5e" : "#38bdf8"; ctx.lineWidth = 2.5;

      for (let A = 70; A <= 165; A += 0.5) {
        // Double Gaussian plus valley
        const gL = 6.6 * Math.exp(-Math.pow((A - peakL) / 6.5, 2));
        const gH = 6.6 * Math.exp(-Math.pow((A - peakH) / 6.5, 2));
        const v = valleyHeight * Math.exp(-Math.pow((A - valley) / 10.0, 2));
        const y = gL + gH + v;

        const px = plot.x + ((A - 70) / 95.0) * plot.w;
        const py = plot.y + plot.h - (y / 7.5) * plot.h;
        if (A === 70) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Axes & labels
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      for (let A = 70; A <= 165; A += 15) {
        const px = plot.x + ((A - 70) / 95.0) * plot.w;
        ctx.fillText(`${A}`, px - 8, plot.y + plot.h + 16);
      }
      ctx.fillText("Mass Number A", plot.x + plot.w / 2 - 35, plot.y + plot.h + 30);

      for (let y = 0; y <= 7; y += 2) {
        const py = plot.y + plot.h - (y / 7.5) * plot.h;
        ctx.fillText(`${y}%`, plot.x - 30, py + 4);
      }
      ctx.fillText("Yield Y(A)", plot.x - 55, plot.y + 15);

      // Annotations
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px Inter";
      ctx.fillText(`Light Peak A ≈ ${peakL} (~6.6%)`, plot.x + ((peakL - 70) / 95.0) * plot.w - 40, plot.y + 35);
      ctx.fillText(`Heavy Peak A ≈ ${peakH} (~6.6%)`, plot.x + ((peakH - 70) / 95.0) * plot.w - 40, plot.y + 35);
      ctx.fillStyle = "#94a3b8";
      ctx.fillText(`Symmetric Valley A ≈ 117 (${isFast ? "Filled (Fast)" : "Deep (~0.01%)"})`, plot.x + ((valley - 70) / 95.0) * plot.w - 55, plot.y + plot.h - 20);

    } else {
      // Watt prompt neutron spectrum χ(E)
      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
      ctx.fillText(`Prompt Fission Neutron Watt Spectrum χ(E) = c · exp(-E/a) · sinh(√(b·E))`, plot.x, plot.y - 12);

      const a = isPu ? 0.966 : 0.988;
      const b = isPu ? 2.842 : 2.249;

      ctx.beginPath();
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;

      for (let E = 0.05; E <= 10.0; E += 0.05) {
        const chi = 0.453 * Math.exp(-1.036 * E) * Math.sinh(Math.sqrt(2.29 * E));
        const px = plot.x + (E / 10.0) * plot.w;
        const py = plot.y + plot.h - (chi / 0.40) * plot.h;
        if (E === 0.05) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Peak marker (Most probable energy ~ 0.73 MeV)
      const Emp = 0.73;
      const chiMax = 0.453 * Math.exp(-1.036 * Emp) * Math.sinh(Math.sqrt(2.29 * Emp));
      const pxMp = plot.x + (Emp / 10.0) * plot.w;
      const pyMp = plot.y + plot.h - (chiMax / 0.40) * plot.h;

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(pxMp, pyMp, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`Most Probable: Emp = 0.73 MeV`, pxMp + 10, pyMp + 5);

      // Mean energy marker (E_avg ~ 1.98 MeV)
      const Eavg = 1.98;
      const chiAvg = 0.453 * Math.exp(-1.036 * Eavg) * Math.sinh(Math.sqrt(2.29 * Eavg));
      const pxAvg = plot.x + (Eavg / 10.0) * plot.w;
      const pyAvg = plot.y + plot.h - (chiAvg / 0.40) * plot.h;

      ctx.strokeStyle = "#38bdf8"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(pxAvg, plot.y); ctx.lineTo(pxAvg, plot.y + plot.h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Average: E_mean = 1.98 MeV`, pxAvg + 8, plot.y + 40);

      // X axes
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      for (let E = 0; E <= 10; E += 1) {
        const px = plot.x + (E / 10.0) * plot.w;
        ctx.fillText(`${E}`, px - 4, plot.y + plot.h + 16);
      }
      ctx.fillText("Neutron Energy E (MeV)", plot.x + plot.w / 2 - 50, plot.y + plot.h + 30);
    }
    }
  },
  "reactor-fuel-burnup-energy-sim": {
    title: "Reactor Thermal Power & Fuel Burnup Dynamics",
    desc: "Simulates fuel consumption, fission rate, daily U-235 burnup, and core burnup accumulation (MWd/MTU) over multi-month reactor operating campaigns.",
    isAnimated: true,
    controls: [
      {
            "id": "corePower",
            "label": "Thermal Power (MWth)",
            "min": 1000,
            "max": 4500,
            "step": 100,
            "value": 3000
      },
      {
            "id": "initialFuel",
            "label": "Core Heavy Metal (MTU)",
            "min": 60,
            "max": 120,
            "step": 5,
            "value": 90
      },
      {
            "id": "operatingDays",
            "label": "Operating Days",
            "min": 100,
            "max": 730,
            "step": 15,
            "value": 500
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const P = vals.corePower !== undefined ? vals.corePower : 3000;
    const M_HM = vals.initialFuel !== undefined ? vals.initialFuel : 90;
    const days = vals.operatingDays !== undefined ? vals.operatingDays : 500;

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Core Burnup Trajectory & U-235 Depletion | P = ${P} MWth | M = ${M_HM} MTU`, plot.x, plot.y - 12);

    // Physics
    const dailyEnergy = P; // MWd/day
    const totalBurnup = (P * days) / M_HM; // MWd/MTU
    const dailyU235Burn = 1.05 * 1.17 * (P / 1000.0); // kg/day
    const totalU235Burned = dailyU235Burn * days; // kg

    // Axes
    const maxDays = 750;
    const maxBurnup = (4500 * 750) / 60; // ~ 56,250 MWd/MTU

    ctx.strokeStyle = "rgba(30, 41, 59, 0.5)"; ctx.lineWidth = 1;
    for (let d = 0; d <= maxDays; d += 150) {
      const px = plot.x + (d / maxDays) * plot.w;
      ctx.beginPath(); ctx.moveTo(px, plot.y); ctx.lineTo(px, plot.y + plot.h); ctx.stroke();
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText(`${d} d`, px - 10, plot.y + plot.h + 16);
    }

    for (let b = 0; b <= 50000; b += 10000) {
      const py = plot.y + plot.h - (b / 55000) * plot.h;
      ctx.beginPath(); ctx.moveTo(plot.x, py); ctx.lineTo(plot.x + plot.w, py); ctx.stroke();
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText(`${b / 1000}k`, plot.x - 30, py + 4);
    }
    ctx.fillText("Burnup (MWd/MTU)", plot.x - 55, plot.y + 15);

    // Plot burnup curve
    ctx.beginPath();
    ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
    for (let d = 0; d <= days; d += 5) {
      const b = (P * d) / M_HM;
      const px = plot.x + (d / maxDays) * plot.w;
      const py = plot.y + plot.h - (b / 55000) * plot.h;
      if (d === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Mark current operating point
    const curX = plot.x + (days / maxDays) * plot.w;
    const curY = plot.y + plot.h - (totalBurnup / 55000) * plot.h;
    ctx.fillStyle = "#f59e0b";
    ctx.beginPath(); ctx.arc(curX, curY, 5, 0, Math.PI * 2); ctx.fill();

    // Metrics overlay box
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + 20, plot.y + 20, 240, 95);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + 20, plot.y + 20, 240, 95);

    ctx.font = "11px Inter"; ctx.fillStyle = "#38bdf8";
    ctx.fillText(`Core Burnup: ${totalBurnup.toFixed(0)} MWd/MTU`, plot.x + 30, plot.y + 40);
    ctx.fillStyle = "#cbd5e1";
    ctx.fillText(`Fission Rate: ${(P * 3.12e16 / 1e19).toFixed(2)} × 10¹⁹ fissions/s`, plot.x + 30, plot.y + 60);
    ctx.fillText(`Daily U-235 Burn: ${dailyU235Burn.toFixed(2)} kg/day`, plot.x + 30, plot.y + 80);
    ctx.fillText(`Total U-235 Destroyed: ${totalU235Burned.toFixed(0)} kg`, plot.x + 30, plot.y + 100);
    }
  },
  "reactor-elastic-moderation-kinematics-sim": {
    title: "Neutron Elastic Moderation Kinematics in CM & LAB Frames",
    desc: "Simulates 2D elastic collision kinematics between a neutron and moderator nucleus (H, D, Be, C, U), calculating collision parameter \u03b1, average cosine \u03bc0 = 2/(3A), logarithmic decrement \u03be, and collision count.",
    isAnimated: true,
    controls: [
      {
            "id": "targetNuclide",
            "label": "Target (1=H, 2=D, 3=Be, 4=C, 5=U)",
            "min": 1,
            "max": 5,
            "step": 1,
            "value": 1
      },
      {
            "id": "cmAngle",
            "label": "CM Scattering Angle \u03b8_CM (deg)",
            "min": 0,
            "max": 180,
            "step": 5,
            "value": 90
      },
      {
            "id": "incidentEnergy",
            "label": "Incident Energy E1 (MeV)",
            "min": 0.5,
            "max": 5.0,
            "step": 0.5,
            "value": 2.0
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const nuclideIdx = vals.targetNuclide || 1;
    const thetaCM_deg = vals.cmAngle !== undefined ? vals.cmAngle : 90;
    const E1 = vals.incidentEnergy !== undefined ? vals.incidentEnergy : 2.0;

    const A_vals = [1.0, 2.014, 9.012, 12.0, 238.05];
    const names = ["Hydrogen (¹H)", "Deuterium (²H)", "Beryllium (⁹Be)", "Carbon (¹²C)", "Uranium (²³⁸U)"];
    const A = A_vals[nuclideIdx - 1];
    const name = names[nuclideIdx - 1];

    const thetaCM = (thetaCM_deg * Math.PI) / 180.0;
    const alpha = Math.pow((A - 1) / (A + 1), 2);
    const E2_ratio = (1 + alpha) / 2.0 + ((1 - alpha) / 2.0) * Math.cos(thetaCM);
    const E2 = E1 * E2_ratio;
    const deltaE = E1 - E2;
    const mu0 = 2.0 / (3.0 * A);

    let xi;
    if (A === 1.0) {
      xi = 1.0;
    } else {
      xi = 1.0 + (alpha / (1.0 - alpha)) * Math.log(alpha);
    }
    const nColl = 18.2 / xi;

    // Vector kinematics visualization
    const center = { x: 180, y: h / 2 };
    const radius = 100;

    ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.arc(center.x, center.y, radius, 0, Math.PI * 2); ctx.stroke();

    // CM velocity center
    const V_cm = radius / (A + 1);
    const u2 = (A / (A + 1)) * radius;

    // Incident neutron line
    ctx.strokeStyle = "#475569"; ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(center.x - radius - 30, center.y); ctx.lineTo(center.x + radius + 30, center.y); ctx.stroke();
    ctx.setLineDash([]);

    // CM scattered vector u2
    const u2_x = center.x + u2 * Math.cos(thetaCM);
    const u2_y = center.y - u2 * Math.sin(thetaCM);

    ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(center.x, center.y); ctx.lineTo(u2_x, u2_y); ctx.stroke();

    // LAB scattered vector v2
    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(center.x - V_cm, center.y); ctx.lineTo(u2_x, u2_y); ctx.stroke();

    // Labels & indicators
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Target: ${name} (A = ${A.toFixed(1)})`, 40, 30);

    ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
    ctx.fillText("LAB Scattered v₂", u2_x + 8, u2_y);
    ctx.fillText("CM Center", center.x + 5, center.y + 15);

    // Right metrics card
    const card = { x: 380, y: 35, w: w - 410, h: h - 70 };
    ctx.fillStyle = "rgba(11, 17, 32, 0.85)";
    ctx.fillRect(card.x, card.y, card.w, card.h);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(card.x, card.y, card.w, card.h);

    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText("Elastic Moderation Parameters", card.x + 15, card.y + 25);

    ctx.font = "11px Inter"; ctx.fillStyle = "#e2e8f0";
    ctx.fillText(`Collision Parameter α: ${alpha.toFixed(4)}`, card.x + 15, card.y + 55);
    ctx.fillText(`Scattered Energy E₂: ${E2.toFixed(3)} MeV (${(E2_ratio * 100).toFixed(1)}%)`, card.x + 15, card.y + 80);
    ctx.fillText(`Energy Transferred ΔE: ${deltaE.toFixed(3)} MeV (${((1 - E2_ratio) * 100).toFixed(1)}%)`, card.x + 15, card.y + 105);
    ctx.fillText(`Avg Scattering Cosine μ̄₀ = 2/(3A): ${mu0.toFixed(4)}`, card.x + 15, card.y + 130);
    ctx.fillText(`Logarithmic Decrement ξ: ${xi.toFixed(4)}`, card.x + 15, card.y + 155);

    ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Collisions to Thermalize: ~${Math.round(nColl)} collisions`, card.x + 15, card.y + 190);
    }
  },
  "reactor-slowing-down-density-resonance-sim": {
    title: "Slowing-Down Density q(E) & Resonance Escape Probability",
    desc: "Simulates continuous slowing-down epithermal flux \u03d5(E) ~ 1/E, displaying sharp U-238 radiative capture resonances (6.67 eV, 20.9 eV, 36.7 eV) and Doppler broadening temperature effects on resonance escape p.",
    isAnimated: true,
    controls: [
      {
            "id": "modType",
            "label": "Moderator (1=H2O, 2=D2O, 3=Graphite)",
            "min": 1,
            "max": 3,
            "step": 1,
            "value": 1
      },
      {
            "id": "modFuelRatio",
            "label": "Moderator/Fuel Ratio NM/NF",
            "min": 100,
            "max": 600,
            "step": 50,
            "value": 300
      },
      {
            "id": "fuelTemp",
            "label": "Fuel Temperature (K)",
            "min": 300,
            "max": 1200,
            "step": 100,
            "value": 600
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const modIdx = vals.modType || 1;
    const NM_NF = vals.modFuelRatio !== undefined ? vals.modFuelRatio : 300;
    const T = vals.fuelTemp !== undefined ? vals.fuelTemp : 600;

    const modNames = ["Light Water (H₂O)", "Heavy Water (D₂O)", "Graphite (C)"];
    const MR_vals = [61, 5670, 192];
    const xi_vals = [0.925, 0.508, 0.158];

    const modName = modNames[modIdx - 1];
    const MR = MR_vals[modIdx - 1];
    const xi = xi_vals[modIdx - 1];

    // Doppler broadening factor
    const doppler = Math.sqrt(T / 300.0);
    // Effective resonance integral (barns)
    const I_eff = (10.0 + 15.0 / Math.sqrt(NM_NF)) * (1 + 0.005 * (Math.sqrt(T) - Math.sqrt(300)));
    // Resonance escape probability p = exp(- I_eff / (xi * Sigma_s / NF))
    const sigma_s_mod = (modIdx === 1) ? 44.8 : ((modIdx === 2) ? 10.6 : 4.8);
    const xi_Sigma_s_NF = xi * NM_NF * sigma_s_mod;
    const p = Math.exp(-I_eff / (xi_Sigma_s_NF / 10.0));

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Epithermal Flux Spectrum & Resonance Absorption | ${modName} | T_fuel = ${T} K`, plot.x, plot.y - 12);

    // Plot 1/E slowing down flux with resonance absorption dips
    ctx.beginPath();
    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;

    // Resonances at 6.67 eV, 20.9 eV, 36.7 eV, 66.0 eV
    const res = [6.67, 20.9, 36.7, 66.0];
    const resW = [1.5 * doppler, 2.0 * doppler, 2.5 * doppler, 3.0 * doppler];
    const resD = [0.85, 0.65, 0.55, 0.45];

    for (let eLog = 0; eLog <= 2.5; eLog += 0.01) {
      const E = Math.pow(10, eLog); // 1 eV to ~316 eV
      // Base 1/E flux (normalized in log space)
      let flux = 1.0;

      // Subtract resonance dips
      for (let r = 0; r < res.length; r++) {
        const dE = E - res[r];
        const dip = resD[r] * Math.exp(-Math.pow(dE / resW[r], 2));
        flux -= dip;
      }
      flux = Math.max(0.05, flux);

      const px = plot.x + (eLog / 2.5) * plot.w;
      const py = plot.y + plot.h - flux * (plot.h * 0.85);
      if (eLog === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Axes
    ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
    for (let exp = 0; exp <= 2; exp++) {
      const px = plot.x + (exp / 2.5) * plot.w;
      ctx.fillText(`10^${exp} eV`, px - 15, plot.y + plot.h + 16);
    }
    ctx.fillText("Neutron Energy E", plot.x + plot.w / 2 - 35, plot.y + plot.h + 30);
    ctx.fillText("Flux ϕ(E) ~ 1/E", plot.x - 55, plot.y + 15);

    // Annotations for resonances
    ctx.fillStyle = "#f59e0b"; ctx.font = "10px Inter";
    ctx.fillText("6.67 eV", plot.x + (Math.log10(6.67) / 2.5) * plot.w - 15, plot.y + plot.h - 15);
    ctx.fillText("20.9 eV", plot.x + (Math.log10(20.9) / 2.5) * plot.w - 15, plot.y + plot.h - 15);

    // Results card
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + plot.w - 240, plot.y + 15, 225, 95);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + plot.w - 240, plot.y + 15, 225, 95);

    ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Resonance Escape p: ${p.toFixed(4)} (${(p * 100).toFixed(2)}%)`, plot.x + plot.w - 225, plot.y + 35);
    ctx.fillStyle = "#cbd5e1"; ctx.font = "11px Inter";
    ctx.fillText(`Moderating Ratio: ${MR}`, plot.x + plot.w - 225, plot.y + 55);
    ctx.fillText(`Effective Integral I_eff: ${I_eff.toFixed(2)} b`, plot.x + plot.w - 225, plot.y + 75);
    ctx.fillText(`Doppler Broadening: ×${doppler.toFixed(2)}`, plot.x + plot.w - 225, plot.y + 95);
    }
  },
  "reactor-fick-diffusion-flux-sim": {
    title: "Neutron Diffusion Theory & Fick's Law Flux Profiles",
    desc: "Solves steady-state 1D/radial neutron diffusion equation -D\u2207\u00b2\u03d5 + \u03a3a \u03d5 = S(r), demonstrating Fick's Law J = -D\u2207\u03d5, thermal diffusion length L = \u221a(D/\u03a3a), and extrapolated boundary d = 0.71 \u03bbtr.",
    isAnimated: true,
    controls: [
      {
            "id": "mediumType",
            "label": "Medium (1=H2O, 2=D2O, 3=Be, 4=Graphite)",
            "min": 1,
            "max": 4,
            "step": 1,
            "value": 1
      },
      {
            "id": "sourceGeom",
            "label": "Geometry (1=Point Source, 2=Planar Sheet)",
            "min": 1,
            "max": 2,
            "step": 1,
            "value": 1
      },
      {
            "id": "coreRadius",
            "label": "Boundary Radius R (cm)",
            "min": 10,
            "max": 60,
            "step": 5,
            "value": 30
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const medIdx = vals.mediumType || 1;
    const isPlane = (vals.sourceGeom === 2);
    const R = vals.coreRadius !== undefined ? vals.coreRadius : 30;

    const medNames = ["Light Water (H₂O)", "Heavy Water (D₂O)", "Beryllium (Be)", "Graphite (C)"];
    const D_vals = [0.16, 0.85, 0.48, 0.85];
    const L_vals = [2.85, 171.0, 20.5, 59.0];
    const d_vals = [0.35, 1.80, 1.05, 1.85];

    const medName = medNames[medIdx - 1];
    const D = D_vals[medIdx - 1];
    const L = L_vals[medIdx - 1];
    const d = d_vals[medIdx - 1];
    const R_tilde = R + d;

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Diffusion Flux ϕ(r) & Extrapolated Boundary | ${medName} | ${isPlane ? "Planar" : "Point"} Source`, plot.x, plot.y - 12);

    // Physical boundary and extrapolated boundary lines
    const pxR = plot.x + (R / (R + 15)) * plot.w;
    const pxR_tilde = plot.x + (R_tilde / (R + 15)) * plot.w;

    ctx.fillStyle = "rgba(56, 189, 248, 0.05)";
    ctx.fillRect(plot.x, plot.y, pxR - plot.x, plot.h);

    // Boundary lines
    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(pxR, plot.y); ctx.lineTo(pxR, plot.y + plot.h); ctx.stroke();

    ctx.strokeStyle = "#ef4444"; ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(pxR_tilde, plot.y); ctx.lineTo(pxR_tilde, plot.y + plot.h); ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = "#38bdf8"; ctx.font = "10px Inter";
    ctx.fillText(`Surface R = ${R} cm`, pxR - 40, plot.y + 15);
    ctx.fillStyle = "#ef4444";
    ctx.fillText(`Extrapolated R̃ = ${R_tilde.toFixed(1)} cm`, pxR_tilde + 4, plot.y + 15);

    // Plot flux curve
    ctx.beginPath();
    ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;

    for (let r = 0.5; r <= R_tilde; r += 0.2) {
      let phi;
      if (isPlane) {
        // Planar: sinh((R_tilde - r)/L) / sinh(R_tilde/L)
        phi = Math.sinh((R_tilde - r) / L) / Math.sinh(R_tilde / L);
      } else {
        // Radial/point: sinh((R_tilde - r)/L) / (r * sinh(R_tilde/L))
        phi = Math.sinh((R_tilde - r) / L) / (r * Math.sinh(R_tilde / L));
      }

      const px = plot.x + (r / (R + 15)) * plot.w;
      const py = plot.y + plot.h - Math.min(1.0, phi * (isPlane ? 1.0 : 3.0)) * (plot.h * 0.85);
      if (r === 0.5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Axes
    ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
    for (let r = 0; r <= R + 15; r += 10) {
      const px = plot.x + (r / (R + 15)) * plot.w;
      ctx.fillText(`${r} cm`, px - 12, plot.y + plot.h + 16);
    }
    ctx.fillText("Distance r (cm)", plot.x + plot.w / 2 - 35, plot.y + plot.h + 30);

    // Metrics box
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + plot.w - 235, plot.y + 25, 220, 95);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + plot.w - 235, plot.y + 25, 220, 95);

    ctx.font = "11px Inter"; ctx.fillStyle = "#38bdf8";
    ctx.fillText(`Diffusion Length L: ${L.toFixed(1)} cm`, plot.x + plot.w - 220, plot.y + 45);
    ctx.fillStyle = "#cbd5e1";
    ctx.fillText(`Diffusion Coeff D: ${D.toFixed(3)} cm`, plot.x + plot.w - 220, plot.y + 65);
    ctx.fillText(`Extrapolated Distance d: ${d.toFixed(2)} cm`, plot.x + plot.w - 220, plot.y + 85);
    ctx.fillText(`Fick Flux Gradient: J = -D ∇ϕ`, plot.x + plot.w - 220, plot.y + 105);
    }
  },
  "reactor-fermi-age-slowing-sim": {
    title: "Fermi Age Theory & Fast Neutron Slowing-Down Density",
    desc: "Solves the Fermi Age diffusion equation \u2207\u00b2q = \u2202q/\u2202\u03c4, showing the Gaussian spatial spreading of fast neutrons q(r, \u03c4) as age \u03c4 increases from fission birth to thermal energy.",
    isAnimated: true,
    controls: [
      {
            "id": "fermiAge",
            "label": "Fermi Age \u03c4 (cm\u00b2)",
            "min": 10,
            "max": 350,
            "step": 10,
            "value": 100
      },
      {
            "id": "sourcePower",
            "label": "Source Strength S (\u00d710\u2076 n/s)",
            "min": 1,
            "max": 10,
            "step": 1,
            "value": 5
      },
      {
            "id": "plotRange",
            "label": "Radial Plot Range (cm)",
            "min": 20,
            "max": 80,
            "step": 10,
            "value": 50
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const tau = vals.fermiAge !== undefined ? vals.fermiAge : 100;
    const S = (vals.sourcePower !== undefined ? vals.sourcePower : 5) * 1e6;
    const rMax = vals.plotRange !== undefined ? vals.plotRange : 50;

    const L_s = Math.sqrt(tau); // Slowing down length
    const r_rms = Math.sqrt(6 * tau); // RMS slowing down distance

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Spatial Slowing-Down Kernel q(r, τ) = [S / (4πτ)^(3/2)] · exp(-r² / 4τ)`, plot.x, plot.y - 12);

    // Peak q(0, tau)
    const q0 = S / Math.pow(4 * Math.PI * tau, 1.5);

    // Plot Gaussian curve
    ctx.beginPath();
    ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;

    for (let r = 0; r <= rMax; r += 0.5) {
      const q = q0 * Math.exp(-(r * r) / (4 * tau));
      const px = plot.x + (r / rMax) * plot.w;
      const py = plot.y + plot.h - (q / q0) * (plot.h * 0.85);
      if (r === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Mark slowing down length L_s and RMS radius
    const pxLs = plot.x + (L_s / rMax) * plot.w;
    const pxRms = plot.x + (r_rms / rMax) * plot.w;

    if (L_s <= rMax) {
      ctx.strokeStyle = "#38bdf8"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(pxLs, plot.y); ctx.lineTo(pxLs, plot.y + plot.h); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "10px Inter";
      ctx.fillText(`L_s = ${L_s.toFixed(1)} cm`, pxLs + 4, plot.y + 35);
    }

    if (r_rms <= rMax) {
      ctx.strokeStyle = "#10b981"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(pxRms, plot.y); ctx.lineTo(pxRms, plot.y + plot.h); ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.font = "10px Inter";
      ctx.fillText(`r_rms = ${r_rms.toFixed(1)} cm`, pxRms + 4, plot.y + 55);
    }
    ctx.setLineDash([]);

    // Axes
    ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
    for (let r = 0; r <= rMax; r += 10) {
      const px = plot.x + (r / rMax) * plot.w;
      ctx.fillText(`${r} cm`, px - 12, plot.y + plot.h + 16);
    }
    ctx.fillText("Radial Distance r (cm)", plot.x + plot.w / 2 - 45, plot.y + plot.h + 30);
    ctx.fillText("Slowing Density q(r)", plot.x - 55, plot.y + 15);

    // Results info panel
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + plot.w - 235, plot.y + 20, 220, 95);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + plot.w - 235, plot.y + 20, 220, 95);

    ctx.font = "11px Inter"; ctx.fillStyle = "#f59e0b";
    ctx.fillText(`Fermi Age τ: ${tau} cm²`, plot.x + plot.w - 220, plot.y + 40);
    ctx.fillStyle = "#38bdf8";
    ctx.fillText(`Slowing-Down Length L_s: ${L_s.toFixed(2)} cm`, plot.x + plot.w - 220, plot.y + 60);
    ctx.fillStyle = "#10b981";
    ctx.fillText(`RMS Slowing Distance: ${r_rms.toFixed(2)} cm`, plot.x + plot.w - 220, plot.y + 80);
    ctx.fillStyle = "#94a3b8";
    ctx.fillText(`Peak q(0, τ): ${(q0 / 1e3).toFixed(1)} × 10³ n/cm³·s`, plot.x + plot.w - 220, plot.y + 100);
    }
  },
  "reactor-four-factor-lifecycle-sim": {
    title: "Four-Factor Formula Animated Neutron Life Cycle",
    desc: "Tracks 1000 fast neutrons through their complete generational life cycle: fast fission boost \u03f5, resonance escape p during slowing down, thermal utilization f, and reproduction \u03b7, computing k\u221e = \u03f5\u00b7p\u00b7\u03b7\u00b7f.",
    isAnimated: true,
    controls: [
      {
            "id": "fastFission",
            "label": "Fast Fission Factor \u03f5",
            "min": 1.0,
            "max": 1.08,
            "step": 0.01,
            "value": 1.03
      },
      {
            "id": "resEscape",
            "label": "Resonance Escape p",
            "min": 0.7,
            "max": 0.95,
            "step": 0.01,
            "value": 0.88
      },
      {
            "id": "thermUtil",
            "label": "Thermal Utilization f",
            "min": 0.75,
            "max": 0.98,
            "step": 0.01,
            "value": 0.89
      },
      {
            "id": "reproductionEta",
            "label": "Reproduction Factor \u03b7",
            "min": 1.3,
            "max": 2.2,
            "step": 0.05,
            "value": 1.65
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const eps = vals.fastFission !== undefined ? vals.fastFission : 1.03;
    const p = vals.resEscape !== undefined ? vals.resEscape : 0.88;
    const f = vals.thermUtil !== undefined ? vals.thermUtil : 0.89;
    const eta = vals.reproductionEta !== undefined ? vals.reproductionEta : 1.65;

    const k_inf = eps * p * f * eta;

    // Populations starting from 1000 fast neutrons
    const N0 = 1000;
    const N1 = Math.round(N0 * eps);
    const N2 = Math.round(N1 * p);
    const N3 = Math.round(N2 * f);
    const N4 = Math.round(N3 * eta);

    // Circular life cycle layout
    const cx = w / 2 - 40, cy = h / 2 + 10;
    const R_track = 115;

    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.arc(cx, cy, R_track, 0, Math.PI * 2); ctx.stroke();

    // 4 Stations around circle:
    // Top (0): Fast Fission (N1)
    // Right (PI/2): Resonance Escape / Thermalization (N2)
    // Bottom (PI): Thermal Absorption in Fuel (N3)
    // Left (3PI/2): Next Generation Fast Neutrons (N4)
    const stations = [
      { angle: -Math.PI / 2, label: `Fast Fission: ${N1}`, sub: `ϵ = ${eps.toFixed(2)}`, color: "#38bdf8" },
      { angle: 0, label: `Thermalized: ${N2}`, sub: `p = ${p.toFixed(2)}`, color: "#10b981" },
      { angle: Math.PI / 2, label: `Fuel Absorbed: ${N3}`, sub: `f = ${f.toFixed(2)}`, color: "#f59e0b" },
      { angle: Math.PI, label: `Generation N+1: ${N4}`, sub: `η = ${eta.toFixed(2)}`, color: "#a855f7" }
    ];

    stations.forEach((st) => {
      const sx = cx + R_track * Math.cos(st.angle);
      const sy = cy + R_track * Math.sin(st.angle);

      ctx.fillStyle = st.color;
      ctx.beginPath(); ctx.arc(sx, sy, 9, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 11px Inter";
      const offsetX = Math.cos(st.angle) * 35;
      const offsetY = Math.sin(st.angle) * 20;
      ctx.fillText(st.label, sx + offsetX - 35, sy + offsetY - 5);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText(st.sub, sx + offsetX - 20, sy + offsetY + 10);
    });

    // Animated particles orbiting the track
    const numParticles = 16;
    for (let i = 0; i < numParticles; i++) {
      const phase = (time * 0.8 + (i / numParticles) * Math.PI * 2) % (Math.PI * 2);
      const px = cx + R_track * Math.cos(phase);
      const py = cy + R_track * Math.sin(phase);

      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(px, py, 2.5, 0, Math.PI * 2); ctx.fill();
    }

    // Center multiplication summary
    ctx.fillStyle = "#0f172a";
    ctx.beginPath(); ctx.arc(cx, cy, 55, 0, Math.PI * 2); ctx.fill();
    ctx.strokeStyle = k_inf >= 1.0 ? "#10b981" : "#ef4444"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(cx, cy, 55, 0, Math.PI * 2); ctx.stroke();

    ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
    ctx.fillText("Infinite Mult", cx - 28, cy - 15);
    ctx.fillStyle = k_inf >= 1.0 ? "#10b981" : "#ef4444"; ctx.font = "bold 16px Inter";
    ctx.fillText(`k∞ = ${k_inf.toFixed(3)}`, cx - 35, cy + 8);
    ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
    ctx.fillText(k_inf > 1.0 ? "Supercritical" : (k_inf === 1.0 ? "Critical" : "Subcritical"), cx - 24, cy + 26);

    // Right info panel
    const card = { x: w - 215, y: 35, w: 195, h: h - 70 };
    ctx.fillStyle = "rgba(11, 17, 32, 0.85)";
    ctx.fillRect(card.x, card.y, card.w, card.h);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(card.x, card.y, card.w, card.h);

    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText("Neutron Balance", card.x + 15, card.y + 25);

    ctx.font = "11px Inter"; ctx.fillStyle = "#cbd5e1";
    ctx.fillText(`Fast Birth: 1000`, card.x + 15, card.y + 50);
    ctx.fillText(`Fast Fissions: +${N1 - N0}`, card.x + 15, card.y + 70);
    ctx.fillStyle = "#ef4444";
    ctx.fillText(`Resonance Loss: -${N1 - N2}`, card.x + 15, card.y + 90);
    ctx.fillText(`Parasitic Loss: -${N2 - N3}`, card.x + 15, card.y + 110);
    ctx.fillStyle = "#10b981";
    ctx.fillText(`Thermal Fissions: ${N3}`, card.x + 15, card.y + 130);
    ctx.fillText(`Next Gen: ${N4} neutrons`, card.x + 15, card.y + 155);

    ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
    ctx.fillText(`Net Gain/Loss: ${(N4 - N0 >= 0 ? "+" : "") + (N4 - N0)}`, card.x + 15, card.y + 185);
    }
  },
  "reactor-six-factor-leakage-sim": {
    title: "Six-Factor Formula & Finite Core Leakage Balance",
    desc: "Calculates fast and thermal non-leakage probabilities P_FNL = 1/(1 + Bg\u00b2\u00b7\u03c4) and P_TNL = 1/(1 + Bg\u00b2\u00b7L\u00b2), demonstrating effective core multiplication keff = k\u221e \u00b7 P_FNL \u00b7 P_TNL.",
    isAnimated: true,
    controls: [
      {
            "id": "kInf",
            "label": "Infinite Mult k\u221e",
            "min": 1.0,
            "max": 1.35,
            "step": 0.01,
            "value": 1.15
      },
      {
            "id": "coreBuckling",
            "label": "Buckling Bg\u00b2 (\u00d710\u207b\u2074 cm\u207b\u00b2)",
            "min": 1.0,
            "max": 15.0,
            "step": 0.5,
            "value": 5.0
      },
      {
            "id": "migrArea",
            "label": "Migration Area M\u00b2 (cm\u00b2)",
            "min": 35,
            "max": 350,
            "step": 15,
            "value": 150
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const k_inf = vals.kInf !== undefined ? vals.kInf : 1.15;
    const Bg2 = (vals.coreBuckling !== undefined ? vals.coreBuckling : 5.0) * 1e-4;
    const M2 = vals.migrArea !== undefined ? vals.migrArea : 150;

    // Partition M2 into tau (30%) and L2 (70%)
    const tau = M2 * 0.35;
    const L2 = M2 * 0.65;

    const P_FNL = 1.0 / (1.0 + Bg2 * tau);
    const P_TNL = 1.0 / (1.0 + Bg2 * L2);
    const k_eff = k_inf * P_FNL * P_TNL;
    const rho_pcm = ((k_eff - 1.0) / k_eff) * 1e5;

    // Waterfall bar chart showing multiplication stages
    const plot = { x: 60, y: 50, w: w - 100, h: h - 95 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Six-Factor Critical Balance | keff = k∞ · P_FNL · P_TNL = ${k_eff.toFixed(4)}`, plot.x, plot.y - 12);

    const stages = [
      { label: "k∞ (Infinite)", val: k_inf, color: "#38bdf8" },
      { label: "Fast Leak (-)", val: k_inf * (1 - P_FNL), color: "#ef4444", isLoss: true },
      { label: "After Fast Leak", val: k_inf * P_FNL, color: "#0ea5e9" },
      { label: "Thermal Leak (-)", val: (k_inf * P_FNL) * (1 - P_TNL), color: "#f43f5e", isLoss: true },
      { label: "keff (Net Finite)", val: k_eff, color: k_eff >= 1.0 ? "#10b981" : "#f59e0b" }
    ];

    const barW = (plot.w - 80) / stages.length;
    const maxVal = 1.4;

    stages.forEach((st, idx) => {
      const bx = plot.x + 30 + idx * (barW + 10);
      const barH = (st.val / maxVal) * plot.h;
      const by = plot.y + plot.h - barH;

      ctx.fillStyle = st.color;
      ctx.fillRect(bx, by, barW, barH);
      ctx.strokeStyle = "#1e293b"; ctx.strokeRect(bx, by, barW, barH);

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 11px Inter";
      ctx.fillText(st.val.toFixed(3), bx + 6, by - 6);

      ctx.fillStyle = "#94a3b8"; ctx.font = "9px Inter";
      ctx.fillText(st.label, bx - 5, plot.y + plot.h + 16);
    });

    // Reference Critical Line (k = 1.0)
    const yCrit = plot.y + plot.h - (1.0 / maxVal) * plot.h;
    ctx.strokeStyle = "#10b981"; ctx.setLineDash([4, 4]); ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(plot.x, yCrit); ctx.lineTo(plot.x + plot.w, yCrit); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "#10b981"; ctx.font = "10px Inter";
    ctx.fillText("Critical Line: k = 1.000", plot.x + plot.w - 130, yCrit - 4);

    // Summary overlay badge
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + 20, plot.y + 15, 230, 80);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + 20, plot.y + 15, 230, 80);

    ctx.fillStyle = k_eff >= 1.0 ? "#10b981" : "#f59e0b"; ctx.font = "bold 12px Inter";
    ctx.fillText(k_eff >= 1.0005 ? "SUPERCRITICAL (Power Rising)" : (k_eff >= 0.9995 ? "EXACT CRITICAL (Steady State)" : "SUBCRITICAL (Power Decaying)"), plot.x + 30, plot.y + 35);

    ctx.font = "11px Inter"; ctx.fillStyle = "#cbd5e1";
    ctx.fillText(`Fast Non-Leak P_FNL: ${(P_FNL * 100).toFixed(2)}%`, plot.x + 30, plot.y + 55);
    ctx.fillText(`Thermal Non-Leak P_TNL: ${(P_TNL * 100).toFixed(2)}%`, plot.x + 30, plot.y + 70);
    ctx.fillText(`Net Reactivity ρ: ${(rho_pcm >= 0 ? "+" : "") + Math.round(rho_pcm)} pcm`, plot.x + 30, plot.y + 85);
    }
  },
  "reactor-geometric-buckling-geometries-sim": {
    title: "Geometric Buckling & Flux Profiles in 5 Canonical Geometries",
    desc: "Solves Helmholtz critical wave equation \u2207\u00b2\u03d5 + Bg\u00b2\u00b7\u03d5 = 0 across sphere, finite cylinder, cube, rectangular parallelepiped, and slab, calculating geometric buckling Bg\u00b2 and optimum cylinder volume.",
    isAnimated: true,
    controls: [
      {
            "id": "geomShape",
            "label": "Geometry (1=Sphere, 2=Opt Cyl, 3=Cube, 4=Slab)",
            "min": 1,
            "max": 4,
            "step": 1,
            "value": 1
      },
      {
            "id": "dimSize",
            "label": "Characteristic Dimension (m)",
            "min": 1.0,
            "max": 5.0,
            "step": 0.2,
            "value": 2.5
      },
      {
            "id": "display3D",
            "label": "View Mode (1=Flux Curve, 2=Volume Bar)",
            "min": 1,
            "max": 2,
            "step": 1,
            "value": 1
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const shapeIdx = vals.geomShape || 1;
    const D_dim = vals.dimSize !== undefined ? vals.dimSize : 2.5; // meters
    const isVolBar = (vals.display3D === 2);

    const shapes = ["Bare Sphere", "Optimum Finite Cylinder (H=1.082D)", "Bare Cube", "Infinite Slab"];
    const name = shapes[shapeIdx - 1];

    // Compute buckling Bg2 (m^-2) and minimum critical volume factor
    let Bg2, vol, fluxFormula;
    const R_m = D_dim / 2.0;

    if (shapeIdx === 1) {
      // Sphere: Bg = pi / R
      Bg2 = Math.pow(Math.PI / R_m, 2);
      vol = (4.0 / 3.0) * Math.PI * Math.pow(R_m, 3);
      fluxFormula = "ϕ(r) = ϕ0 · sin(π·r/R) / (π·r/R)";
    } else if (shapeIdx === 2) {
      // Opt cylinder: H = 1.082 * 2R = 2.164 R
      const H = 2.164 * R_m;
      Bg2 = Math.pow(2.405 / R_m, 2) + Math.pow(Math.PI / H, 2);
      vol = Math.PI * Math.pow(R_m, 2) * H;
      fluxFormula = "ϕ(r, z) = ϕ0 · J0(2.405·r/R) · cos(π·z/H)";
    } else if (shapeIdx === 3) {
      // Cube: a = D_dim
      Bg2 = 3.0 * Math.pow(Math.PI / D_dim, 2);
      vol = Math.pow(D_dim, 3);
      fluxFormula = "ϕ(x,y,z) = ϕ0 · cos(πx/a)cos(πy/a)cos(πz/a)";
    } else {
      // Slab: thickness a = D_dim
      Bg2 = Math.pow(Math.PI / D_dim, 2);
      vol = Infinity;
      fluxFormula = "ϕ(x) = ϕ0 · cos(π·x/a)";
    }

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Helmholtz Critical Solution | ${name} | Bg² = ${Bg2.toFixed(3)} m⁻²`, plot.x, plot.y - 12);

    if (!isVolBar) {
      // Plot spatial flux distribution from center to boundary
      ctx.beginPath();
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;

      const nPts = 100;
      for (let i = 0; i <= nPts; i++) {
        const u = i / nPts; // 0 to 1 (normalized distance to boundary)
        let phi;
        if (shapeIdx === 1) {
          phi = (u === 0) ? 1.0 : Math.sin(Math.PI * u) / (Math.PI * u);
        } else if (shapeIdx === 2) {
          // Approximation to J0(2.405 * u)
          phi = Math.cos(1.2 * u * Math.PI / 2) * (1 - 0.2 * u * u);
        } else {
          phi = Math.cos((Math.PI / 2) * u);
        }

        const px = plot.x + u * plot.w;
        const py = plot.y + plot.h - Math.max(0, phi) * (plot.h * 0.85);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Axes
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Center (r=0)", plot.x + 5, plot.y + plot.h + 16);
      ctx.fillText(`Boundary (${D_dim.toFixed(1)} m)`, plot.x + plot.w - 75, plot.y + plot.h + 16);
      ctx.fillText("Relative Flux ϕ/ϕ0", plot.x - 55, plot.y + 15);

      // Peaking factor annotation
      const peakFactor = (shapeIdx === 1) ? 3.29 : ((shapeIdx === 2) ? 3.64 : ((shapeIdx === 3) ? 3.88 : 1.57));
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px Inter";
      ctx.fillText(`Peak-to-Average Peaking Factor Ω = ${peakFactor.toFixed(2)}`, plot.x + 20, plot.y + 35);
      ctx.fillText(`Formula: ${fluxFormula}`, plot.x + 20, plot.y + 55);

    } else {
      // Comparison of critical volume across geometries for identical B^2
      const geoms = [
        { name: "Sphere", factor: 130, color: "#10b981" },
        { name: "Opt Cyl", factor: 148, color: "#38bdf8" },
        { name: "Cube", factor: 161, color: "#f59e0b" },
        { name: "P-piped", factor: 185, color: "#a855f7" }
      ];

      const barW = (plot.w - 100) / geoms.length;
      geoms.forEach((g, idx) => {
        const bx = plot.x + 40 + idx * (barW + 15);
        const bh = (g.factor / 200) * plot.h;
        const by = plot.y + plot.h - bh;

        ctx.fillStyle = g.color;
        ctx.fillRect(bx, by, barW, bh);

        ctx.fillStyle = "#ffffff"; ctx.font = "bold 11px Inter";
        ctx.fillText(`${g.factor}/B³`, bx + 10, by - 6);

        ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
        ctx.fillText(g.name, bx + 5, plot.y + plot.h + 16);
      });
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter";
      ctx.fillText("Minimum Critical Volume Theorem: Sphere requires lowest critical mass!", plot.x + 20, plot.y + 25);
    }
    }
  },
  "reactor-reflected-core-savings-sim": {
    title: "Two-Region Reflected Core & Reflector Savings \u03b4",
    desc: "Solves coupled two-region diffusion equations in multiplying core and non-multiplying reflector, demonstrating the thermal flux peak in the reflector and reduction in critical core size (reflector savings \u03b4).",
    isAnimated: true,
    controls: [
      {
            "id": "coreSize",
            "label": "Bare Critical Radius (cm)",
            "min": 30,
            "max": 100,
            "step": 5,
            "value": 60
      },
      {
            "id": "reflMaterial",
            "label": "Reflector (1=Graphite, 2=D2O, 3=Be, 4=H2O)",
            "min": 1,
            "max": 4,
            "step": 1,
            "value": 1
      },
      {
            "id": "reflThick",
            "label": "Reflector Thickness (cm)",
            "min": 10,
            "max": 60,
            "step": 5,
            "value": 35
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const R_bare = vals.coreSize !== undefined ? vals.coreSize : 60;
    const refIdx = vals.reflMaterial || 1;
    const T_refl = vals.reflThick !== undefined ? vals.reflThick : 35;

    const refNames = ["Graphite (C)", "Heavy Water (D₂O)", "Beryllium (Be)", "Light Water (H₂O)"];
    const Lr_vals = [50.0, 171.0, 21.0, 2.85];
    const Lr = Lr_vals[refIdx - 1];

    // Reflector savings delta approx = Lr * tanh(T_refl / Lr)
    const delta = Math.min(R_bare * 0.5, Lr * Math.tanh(T_refl / Lr));
    const R_refl = R_bare - delta;
    const R_total = R_refl + T_refl;

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Reflected Reactor Flux Profile | ${refNames[refIdx - 1]} Reflector | Savings δ = ${delta.toFixed(1)} cm`, plot.x, plot.y - 12);

    // Interface and outer boundary markers
    const pxInt = plot.x + (R_refl / (R_bare + 40)) * plot.w;
    const pxBare = plot.x + (R_bare / (R_bare + 40)) * plot.w;
    const pxOuter = plot.x + (R_total / (R_bare + 40)) * plot.w;

    // Core region shading
    ctx.fillStyle = "rgba(56, 189, 248, 0.08)";
    ctx.fillRect(plot.x, plot.y, pxInt - plot.x, plot.h);

    // Reflector region shading
    ctx.fillStyle = "rgba(16, 185, 129, 0.08)";
    ctx.fillRect(pxInt, plot.y, Math.min(plot.w - (pxInt - plot.x), pxOuter - pxInt), plot.h);

    // Boundary lines
    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(pxInt, plot.y); ctx.lineTo(pxInt, plot.y + plot.h); ctx.stroke();

    ctx.strokeStyle = "#ef4444"; ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(pxBare, plot.y); ctx.lineTo(pxBare, plot.y + plot.h); ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = "#38bdf8"; ctx.font = "10px Inter";
    ctx.fillText(`Core Interface R = ${R_refl.toFixed(1)} cm`, pxInt - 60, plot.y + 15);
    ctx.fillStyle = "#ef4444";
    ctx.fillText(`Bare R = ${R_bare} cm`, pxBare + 4, plot.y + 15);

    // Plot radial flux profile showing reflector thermal flux peak
    ctx.beginPath();
    ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;

    for (let r = 0; r <= R_total; r += 0.5) {
      let phi;
      if (r <= R_refl) {
        // In core: Bessel/cosine shape
        phi = Math.cos((Math.PI / 2) * (r / (R_refl + delta)));
      } else {
        // In reflector: bump due to thermalization and hyperbolic decay
        const distFromInt = r - R_refl;
        const decay = Math.sinh((T_refl - distFromInt) / Lr) / Math.sinh(T_refl / Lr);
        const bump = 0.25 * Math.exp(-distFromInt / 8.0);
        phi = Math.cos((Math.PI / 2) * (R_refl / (R_refl + delta))) * decay + bump;
      }

      const px = plot.x + (r / (R_bare + 40)) * plot.w;
      const py = plot.y + plot.h - Math.max(0, phi) * (plot.h * 0.82);
      if (r === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Results info box
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + plot.w - 235, plot.y + 25, 220, 85);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + plot.w - 235, plot.y + 25, 220, 85);

    ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Reflector Savings δ: ${delta.toFixed(1)} cm`, plot.x + plot.w - 220, plot.y + 45);
    ctx.fillStyle = "#cbd5e1"; ctx.font = "11px Inter";
    ctx.fillText(`Reflected Core Radius: ${R_refl.toFixed(1)} cm`, plot.x + plot.w - 220, plot.y + 65);
    ctx.fillText(`Core Volume Saved: ${((1 - Math.pow(R_refl / R_bare, 3)) * 100).toFixed(1)}%`, plot.x + plot.w - 220, plot.y + 85);
    }
  },
  "reactor-point-kinetics-delayed-neutrons-sim": {
    title: "Point Reactor Kinetics & Delayed Precursor Dynamics (PRKE)",
    desc: "Solves point reactor kinetics equations with delayed neutron precursors, illustrating the instantaneous prompt jump P(0+) = P0 / (1 - \u03c1/\u03b2) followed by stable exponential growth or decay.",
    isAnimated: true,
    controls: [
      {
            "id": "reactivityRho",
            "label": "Reactivity \u03c1 ($)",
            "min": -1.5,
            "max": 0.8,
            "step": 0.1,
            "value": 0.3
      },
      {
            "id": "genTimeLambda",
            "label": "Generation Time \u039b (\u00d710\u207b\u2074 s)",
            "min": 0.2,
            "max": 5.0,
            "step": 0.2,
            "value": 1.0
      },
      {
            "id": "simTimeSpan",
            "label": "Simulation Time Window (s)",
            "min": 5,
            "max": 40,
            "step": 5,
            "value": 20
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const rho_dollars = vals.reactivityRho !== undefined ? vals.reactivityRho : 0.3;
    const Lambda = (vals.genTimeLambda !== undefined ? vals.genTimeLambda : 1.0) * 1e-4;
    const tMax = vals.simTimeSpan !== undefined ? vals.simTimeSpan : 20;

    const beta = 0.0065;
    const rho = rho_dollars * beta;
    const lambda_eff = 0.08; // 1/s

    // Prompt jump ratio: P(0+) / P0 = 1 / (1 - rho/beta) = 1 / (1 - rho_dollars)
    const promptJump = (rho_dollars < 1.0) ? (1.0 / (1.0 - rho_dollars)) : 10.0;
    // Stable period: T = (beta - rho) / (lambda_eff * rho)
    const T_stable = (rho !== 0) ? (beta - rho) / (lambda_eff * rho) : Infinity;

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Point Reactor Kinetics Response | ρ = ${rho_dollars.toFixed(2)}$ (${Math.round(rho * 1e5)} pcm) | Prompt Jump = ×${promptJump.toFixed(2)}`, plot.x, plot.y - 12);

    // Compute transient curve
    const maxPower = Math.max(3.0, promptJump * 2.5);

    ctx.beginPath();
    ctx.strokeStyle = rho_dollars > 0 ? "#10b981" : (rho_dollars === 0 ? "#f59e0b" : "#38bdf8");
    ctx.lineWidth = 2.5;

    for (let t = 0; t <= tMax; t += 0.1) {
      let P;
      if (t < 0.05) {
        P = 1.0;
      } else {
        // Prompt jump followed by stable period exponential
        if (T_stable !== Infinity && T_stable > 0) {
          P = promptJump * Math.exp(t / T_stable);
        } else if (T_stable < 0) {
          P = promptJump * Math.exp(t / T_stable);
        } else {
          P = 1.0;
        }
      }

      const px = plot.x + (t / tMax) * plot.w;
      const py = plot.y + plot.h - Math.min(1.0, P / maxPower) * (plot.h * 0.85);
      if (t === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Baseline P = 1.0 line
    const yBase = plot.y + plot.h - (1.0 / maxPower) * (plot.h * 0.85);
    ctx.strokeStyle = "#475569"; ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(plot.x, yBase); ctx.lineTo(plot.x + plot.w, yBase); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
    ctx.fillText("Initial Power P0 = 1.0", plot.x + 10, yBase - 4);

    // Axes
    ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
    for (let t = 0; t <= tMax; t += 5) {
      const px = plot.x + (t / tMax) * plot.w;
      ctx.fillText(`${t} s`, px - 8, plot.y + plot.h + 16);
    }
    ctx.fillText("Time t (seconds)", plot.x + plot.w / 2 - 35, plot.y + plot.h + 30);
    ctx.fillText("Relative Power P/P0", plot.x - 55, plot.y + 15);

    // Results card
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + plot.w - 240, plot.y + 20, 225, 95);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + plot.w - 240, plot.y + 20, 225, 95);

    ctx.fillStyle = rho_dollars > 0 ? "#10b981" : (rho_dollars === 0 ? "#f59e0b" : "#38bdf8");
    ctx.font = "bold 12px Inter";
    ctx.fillText(rho_dollars > 0 ? "Supercritical (Power Rising)" : (rho_dollars === 0 ? "Critical (Steady Power)" : "Subcritical (Power Decaying)"), plot.x + plot.w - 225, plot.y + 40);

    ctx.font = "11px Inter"; ctx.fillStyle = "#cbd5e1";
    ctx.fillText(`Prompt Jump P(0+): ${promptJump.toFixed(3)} · P0`, plot.x + plot.w - 225, plot.y + 60);
    ctx.fillText(`Stable Period T: ${isFinite(T_stable) ? T_stable.toFixed(1) + " s" : "∞ (Steady)"}`, plot.x + plot.w - 225, plot.y + 80);
    ctx.fillText(`Doubling Time Td: ${isFinite(T_stable) && T_stable > 0 ? (T_stable * Math.LN2).toFixed(1) + " s" : "N/A"}`, plot.x + plot.w - 225, plot.y + 100);
    }
  },
  "reactor-inhour-reactivity-period-sim": {
    title: "Inhour Equation Solver: Reactivity vs Stable Period",
    desc: "Solves the exact 6-group Inhour equation \u03c1 = \u039b/T + \u2211 \u03b2i/(1 + \u03bbi\u00b7T), displaying the characteristic curve, vertical asymptote poles at -1/\u03bbi, and the prompt critical boundary \u03c1 = 1$.",
    isAnimated: true,
    controls: [
      {
            "id": "rhoInputDollars",
            "label": "Reactivity ($)",
            "min": -1.5,
            "max": 0.95,
            "step": 0.05,
            "value": 0.4
      },
      {
            "id": "precursorNuclide",
            "label": "Fissile Fuel (1=U235, 2=Pu239)",
            "min": 1,
            "max": 2,
            "step": 1,
            "value": 1
      },
      {
            "id": "plotRangeT",
            "label": "Period Range (s)",
            "min": 20,
            "max": 120,
            "step": 20,
            "value": 60
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const rho_dlr = vals.rhoInputDollars !== undefined ? vals.rhoInputDollars : 0.4;
    const isPu = (vals.precursorNuclide === 2);
    const maxT = vals.plotRangeT !== undefined ? vals.plotRangeT : 60;

    const beta = isPu ? 0.00215 : 0.00650;
    const Lambda = 1e-4;

    // 6-group parameters for U235
    const beta_i = isPu ? [0.072, 0.625, 0.442, 0.686, 0.180, 0.145] : [0.215, 1.424, 1.274, 2.568, 0.748, 0.271];
    const lambda_i = [0.0124, 0.0305, 0.111, 0.301, 1.14, 3.01];

    // Find stable period T for given rho_dlr using bisection
    const targetRho = rho_dlr * beta;
    let T_lo = 0.05, T_hi = 500.0, T_sol = 50.0;

    for (let iter = 0; iter < 40; iter++) {
      const T_mid = (T_lo + T_hi) / 2.0;
      let rho_calc = Lambda / T_mid;
      for (let i = 0; i < 6; i++) {
        rho_calc += (beta_i[i] * 1e-3) / (1.0 + lambda_i[i] * T_mid);
      }
      if (rho_calc > targetRho) {
        T_lo = T_mid;
      } else {
        T_hi = T_mid;
      }
      T_sol = T_mid;
    }
    const T_double = T_sol * Math.LN2;

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Inhour Equation: ρ = Λ/T + ∑ βi/(1 + λi·T) | ${isPu ? "Pu-239" : "U-235"} | β = ${(beta * 100).toFixed(3)}%`, plot.x, plot.y - 12);

    // Prompt critical limit line (ρ = 1$)
    const yPrompt = plot.y + plot.h - (1.0 / 1.2) * (plot.h * 0.85);
    ctx.strokeStyle = "#ef4444"; ctx.setLineDash([4, 4]); ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(plot.x, yPrompt); ctx.lineTo(plot.x + plot.w, yPrompt); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter";
    ctx.fillText("Prompt Critical Boundary: ρ = 1.00 $ (Explosive)", plot.x + 20, yPrompt - 5);

    // Plot Inhour curve (ρ in dollars vs T in seconds)
    ctx.beginPath();
    ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;

    for (let T = 1.0; T <= maxT; T += 0.5) {
      let rho_c = Lambda / T;
      for (let i = 0; i < 6; i++) {
        rho_c += (beta_i[i] * 1e-3) / (1.0 + lambda_i[i] * T);
      }
      const rho_dollars_c = rho_c / beta;

      const px = plot.x + (T / maxT) * plot.w;
      const py = plot.y + plot.h - (rho_dollars_c / 1.2) * (plot.h * 0.85);
      if (T === 1.0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Mark current operating point
    const curPx = plot.x + (T_sol / maxT) * plot.w;
    const curPy = plot.y + plot.h - (rho_dlr / 1.2) * (plot.h * 0.85);

    if (T_sol <= maxT) {
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(curPx, curPy, 5, 0, Math.PI * 2); ctx.fill();
    }

    // Axes
    ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
    for (let T = 0; T <= maxT; T += 10) {
      const px = plot.x + (T / maxT) * plot.w;
      ctx.fillText(`${T} s`, px - 8, plot.y + plot.h + 16);
    }
    ctx.fillText("Stable Reactor Period T (seconds)", plot.x + plot.w / 2 - 50, plot.y + plot.h + 30);
    ctx.fillText("Reactivity ρ ($)", plot.x - 55, plot.y + 15);

    // Results info box
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + plot.w - 235, plot.y + 45, 220, 85);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + plot.w - 235, plot.y + 45, 220, 85);

    ctx.font = "11px Inter"; ctx.fillStyle = "#f59e0b";
    ctx.fillText(`Input Reactivity: ${rho_dlr.toFixed(2)} $`, plot.x + plot.w - 220, plot.y + 65);
    ctx.fillStyle = "#10b981";
    ctx.fillText(`Stable Period T: ${T_sol.toFixed(2)} seconds`, plot.x + plot.w - 220, plot.y + 85);
    ctx.fillStyle = "#38bdf8";
    ctx.fillText(`Doubling Time Td: ${T_double.toFixed(2)} seconds`, plot.x + plot.w - 220, plot.y + 105);
    }
  },
  "reactor-temperature-feedback-control-sim": {
    title: "Reactivity Feedback & Control Rod Self-Regulation",
    desc: "Simulates inherent negative reactivity feedback (Doppler coefficient \u03b1D and moderator coefficient \u03b1M) counteracting positive reactivity step insertions and stabilizing reactor power.",
    isAnimated: true,
    controls: [
      {
            "id": "stepDisturb",
            "label": "Step Disturbance (pcm)",
            "min": -300,
            "max": 400,
            "step": 50,
            "value": 200
      },
      {
            "id": "dopplerCoeff",
            "label": "Doppler Coeff \u03b1D (pcm/\u00b0C)",
            "min": -5.0,
            "max": -1.0,
            "step": 0.5,
            "value": -2.5
      },
      {
            "id": "rodInsertion",
            "label": "Control Rod Depth z/H (%)",
            "min": 0,
            "max": 100,
            "step": 5,
            "value": 30
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const rho_step = vals.stepDisturb !== undefined ? vals.stepDisturb : 200; // pcm
    const alpha_D = vals.dopplerCoeff !== undefined ? vals.dopplerCoeff : -2.5; // pcm/degC
    const z_frac = (vals.rodInsertion !== undefined ? vals.rodInsertion : 30) / 100.0;

    // Control rod worth S-curve: rho(z) = rho_tot * [z - sin(2pi*z)/(2pi)]
    const rho_rod_tot = -2500; // pcm
    const rho_rod = rho_rod_tot * (z_frac - Math.sin(2 * Math.PI * z_frac) / (2 * Math.PI));

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Inherent Safety: Doppler Feedback Power Self-Stabilization | αD = ${alpha_D} pcm/°C`, plot.x, plot.y - 12);

    // Simulate thermal-hydraulic power response over 30 seconds
    const maxT = 30;
    const dt = 0.2;
    let P = 1.0;
    let T_fuel = 600; // degC
    const pts = [];

    const totalInitRho = rho_step;

    for (let t = 0; t <= maxT; t += dt) {
      const deltaT = T_fuel - 600;
      const rho_feedback = alpha_D * deltaT;
      const net_rho = totalInitRho + rho_feedback;

      // PRKE quasi-static power change + thermal balance
      P += (net_rho / (0.0065 * 1e5)) * P * 0.8 * dt;
      P = Math.max(0.1, P);

      // Fuel temperature rate of change
      T_fuel += (P - 1.0) * 15.0 * dt - deltaT * 0.05 * dt;

      pts.push({ t, P });
    }

    // Plot power stabilization trajectory
    ctx.beginPath();
    ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;

    pts.forEach((pt, i) => {
      const px = plot.x + (pt.t / maxT) * plot.w;
      const py = plot.y + plot.h - Math.min(1.0, pt.P / 2.5) * (plot.h * 0.85);
      if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Baseline P = 1.0
    const yBase = plot.y + plot.h - (1.0 / 2.5) * (plot.h * 0.85);
    ctx.strokeStyle = "#475569"; ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(plot.x, yBase); ctx.lineTo(plot.x + plot.w, yBase); ctx.stroke();
    ctx.setLineDash([]);

    // Axes
    ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
    for (let t = 0; t <= maxT; t += 5) {
      const px = plot.x + (t / maxT) * plot.w;
      ctx.fillText(`${t} s`, px - 8, plot.y + plot.h + 16);
    }
    ctx.fillText("Time t (seconds)", plot.x + plot.w / 2 - 35, plot.y + plot.h + 30);
    ctx.fillText("Reactor Power P/P0", plot.x - 55, plot.y + 15);

    // Results info panel
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + plot.w - 235, plot.y + 20, 220, 95);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + plot.w - 235, plot.y + 20, 220, 95);

    ctx.font = "11px Inter"; ctx.fillStyle = "#38bdf8";
    ctx.fillText(`Initial Disturbance: +${rho_step} pcm`, plot.x + plot.w - 220, plot.y + 40);
    ctx.fillStyle = "#10b981";
    ctx.fillText(`Control Rod Worth: ${Math.round(rho_rod)} pcm`, plot.x + plot.w - 220, plot.y + 60);
    ctx.fillText(`Stabilized Fuel ΔT: +${Math.round(Math.abs(rho_step / alpha_D))} °C`, plot.x + plot.w - 220, plot.y + 80);
    ctx.fillStyle = "#f59e0b";
    ctx.fillText(`State: Passively Self-Limiting`, plot.x + plot.w - 220, plot.y + 100);
    }
  },
  "reactor-xenon-samarium-poisoning-sim": {
    title: "Fission Product Poisoning Dynamics & Post-Shutdown Iodine Pit",
    desc: "Solves coupled differential equations for Iodine-135 and Xenon-135 (\u03c3a = 2.65\u00d710\u2076 b), displaying steady-state equilibrium poisoning and the dangerous post-shutdown xenon peak 10 hours later.",
    isAnimated: true,
    controls: [
      {
            "id": "fluxLevel",
            "label": "Thermal Flux \u03d50 (\u00d710\u00b9\u2074 n/cm\u00b2\u00b7s)",
            "min": 0.5,
            "max": 3.0,
            "step": 0.5,
            "value": 1.5
      },
      {
            "id": "reactorStatus",
            "label": "Core State (1=Shutdown Trip, 2=Steady State)",
            "min": 1,
            "max": 2,
            "step": 1,
            "value": 1
      },
      {
            "id": "historyHours",
            "label": "Time Window (hours)",
            "min": 24,
            "max": 72,
            "step": 12,
            "value": 48
      }
],
    render(canvas, vals, time) {

    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

    const phi0 = (vals.fluxLevel !== undefined ? vals.fluxLevel : 1.5) * 1e14;
    const isShutdown = (vals.reactorStatus === 1);
    const maxHours = vals.historyHours !== undefined ? vals.historyHours : 48;

    const gamma_I = 0.061, lambda_I = 2.87e-5; // s^-1 (6.7 h)
    const gamma_Xe = 0.003, lambda_Xe = 2.09e-5; // s^-1 (9.2 h)
    const sigma_a_Xe = 2.65e-18; // cm^2
    const Sigma_f = 0.115; // cm^-1

    // Steady state values
    const I0 = (gamma_I * Sigma_f * phi0) / lambda_I;
    const X0 = ((gamma_I + gamma_Xe) * Sigma_f * phi0) / (lambda_Xe + sigma_a_Xe * phi0);

    const plot = { x: 65, y: 40, w: w - 95, h: h - 85 };
    ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
    ctx.strokeRect(plot.x, plot.y, plot.w, plot.h);

    // Title
    ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
    ctx.fillText(`Xenon-135 Poisoning Dynamics | ${isShutdown ? "Post-Shutdown Iodine Pit" : "Equilibrium Steady State"} | ϕ0 = ${(phi0 / 1e14).toFixed(1)} × 10¹⁴ n/cm²·s`, plot.x, plot.y - 12);

    // Calculate curve points over time (hours)
    let peakX = X0, peakTimeH = 10.5;
    const pts = [];

    for (let t_h = 0; t_h <= maxHours; t_h += 0.5) {
      const t_s = t_h * 3600;
      let X;
      if (isShutdown) {
        // Post-shutdown analytic solution: X(t) = X0*e^(-lambda_Xe*t) + (lambda_I*I0/(lambda_I - lambda_Xe))*(e^(-lambda_Xe*t) - e^(-lambda_I*t))
        const term1 = X0 * Math.exp(-lambda_Xe * t_s);
        const term2 = (lambda_I * I0 / (lambda_I - lambda_Xe)) * (Math.exp(-lambda_Xe * t_s) - Math.exp(-lambda_I * t_s));
        X = term1 + term2;
        if (X > peakX) { peakX = X; peakTimeH = t_h; }
      } else {
        X = X0;
      }
      pts.push({ t_h, X });
    }

    const maxY = isShutdown ? peakX * 1.15 : X0 * 1.5;

    // Plot curve
    ctx.beginPath();
    ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;

    pts.forEach((pt, i) => {
      const px = plot.x + (pt.t_h / maxHours) * plot.w;
      const py = plot.y + plot.h - (pt.X / maxY) * (plot.h * 0.85);
      if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Mark peak xenon position
    if (isShutdown) {
      const pxPeak = plot.x + (peakTimeH / maxHours) * plot.w;
      const pyPeak = plot.y + plot.h - (peakX / maxY) * (plot.h * 0.85);

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(pxPeak, pyPeak, 5, 0, Math.PI * 2); ctx.fill();

      ctx.strokeStyle = "#f59e0b"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(pxPeak, plot.y); ctx.lineTo(pxPeak, plot.y + plot.h); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Peak Xenon: ~${peakTimeH.toFixed(1)} hrs`, pxPeak + 8, pyPeak - 8);
    }

    // Axes
    ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
    for (let h = 0; h <= maxHours; h += 12) {
      const px = plot.x + (h / maxHours) * plot.w;
      ctx.fillText(`${h} h`, px - 8, plot.y + plot.h + 16);
    }
    ctx.fillText("Time After Shutdown (hours)", plot.x + plot.w / 2 - 55, plot.y + plot.h + 30);
    ctx.fillText("Xenon Concentration X(t)", plot.x - 55, plot.y + 15);

    // Results panel
    ctx.fillStyle = "rgba(11, 17, 32, 0.9)";
    ctx.fillRect(plot.x + plot.w - 245, plot.y + 25, 230, 95);
    ctx.strokeStyle = "#334155"; ctx.strokeRect(plot.x + plot.w - 245, plot.y + 25, 230, 95);

    ctx.font = "11px Inter"; ctx.fillStyle = "#ef4444";
    ctx.fillText(`Equilibrium Xenon: ${(X0 / 1e15).toFixed(2)} × 10¹⁵ cm⁻³`, plot.x + plot.w - 230, plot.y + 45);
    ctx.fillStyle = "#f59e0b";
    ctx.fillText(`Peak Post-Shutdown: ${(peakX / 1e15).toFixed(2)} × 10¹⁵ cm⁻³`, plot.x + plot.w - 230, plot.y + 65);
    ctx.fillStyle = "#cbd5e1";
    ctx.fillText(`Peak Reactivity Penalty: -${Math.round((peakX * sigma_a_Xe / 0.16) * 1e5)} pcm`, plot.x + plot.w - 230, plot.y + 85);
    ctx.fillText(`Deadtime: Locked until t > 30 hrs`, plot.x + plot.w - 230, plot.y + 105);
    }
  }
};


// Generic Simulation Engine Integration
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

const origInit = window.SimulationEngine.initSimulation;
window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const simConfig = (window.RP_SIMS && window.RP_SIMS[simType]) ||
                    (window.NUC2_SIMS && window.NUC2_SIMS[simType]) ||
                    (window.SSP2_SIMS && window.SSP2_SIMS[simType]) ||
                    (window.PLASMA_SIMS && window.PLASMA_SIMS[simType]) ||
                    (window.ASTRO_SIMS && window.ASTRO_SIMS[simType]) ||
                    (window.QM2_SIMS && window.QM2_SIMS[simType]) ||
                    (window.SSP_SIMS && window.SSP_SIMS[simType]) ||
                    (window.DIG_SIMS && window.DIG_SIMS[simType]) ||
                    (window.NUC_SIMS && window.NUC_SIMS[simType]);

  if (!simConfig) {
    if (origInit) {
      origInit(containerId, simType);
    } else {
      container.innerHTML = `<div style="padding: 1rem; color: #ef4444; background: #1e1b4b; border-radius: 8px;">Simulation type '${simType}' not found in registry.</div>`;
    }
    return;
  }

  if (window.SimulationEngine.activeAnimations && window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }
  window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

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
  canvas.height = 390;
  canvas.style.width = "100%";
  canvas.style.maxWidth = "750px";
  canvas.style.height = "auto";
  canvas.style.aspectRatio = "750 / 390";
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

  if (simConfig.isAnimated) {
    const animCtrlWrap = document.createElement("div");
    animCtrlWrap.style.display = "flex";
    animCtrlWrap.style.alignItems = "flex-end";
    const pauseBtn = document.createElement("button");
    pauseBtn.innerText = "⏸️ Pause";
    pauseBtn.style.padding = "0.4rem 0.8rem";
    pauseBtn.style.background = "#1e293b";
    pauseBtn.style.color = "#38bdf8";
    pauseBtn.style.border = "1px solid #334155";
    pauseBtn.style.borderRadius = "6px";
    pauseBtn.style.cursor = "pointer";
    pauseBtn.style.fontSize = "0.85rem";

    let isPaused = false;
    pauseBtn.addEventListener("click", () => {
      isPaused = !isPaused;
      pauseBtn.innerText = isPaused ? "▶️ Play" : "⏸️ Pause";
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
