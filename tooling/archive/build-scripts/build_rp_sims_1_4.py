# -*- coding: utf-8 -*-
"""
Builder for Reactor Physics Simulations 1 to 4
1. reactor-atom-density-breeder-sim
2. reactor-neutron-attenuation-flux-sim
3. reactor-fission-yield-spectrum-sim
4. reactor-fuel-burnup-energy-sim
"""
import json

sims = {}

# -----------------------------------------------------------------------------
# Sim 1: Atom Density and Fuel Breeding Simulator
# -----------------------------------------------------------------------------
sims["reactor-atom-density-breeder-sim"] = {
    "title": "Atom Density, Breeding Ratio & Doubling Time Simulator",
    "desc": "Calculates atomic number densities for actinide fuels and solves the breeding gain differential equation, computing fissile inventory accumulation and doubling time in fast breeder reactors.",
    "isAnimated": True,
    "controls": [
        {"id": "convRatio", "label": "Conversion Ratio CR", "min": 0.6, "max": 1.5, "step": 0.05, "value": 1.25},
        {"id": "thermalPower", "label": "Core Power (MWth)", "min": 500, "max": 3500, "step": 100, "value": 2000},
        {"id": "fissileMass", "label": "Initial Fissile Mass (kg)", "min": 1000, "max": 4000, "step": 100, "value": 2500}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 2: Neutron Attenuation and Flux Simulator
# -----------------------------------------------------------------------------
sims["reactor-neutron-attenuation-flux-sim"] = {
    "title": "Neutron Beam Attenuation & Reaction Rate Simulator",
    "desc": "Simulates exponential attenuation I(x) = I0 * exp(-Σt * x) of a monoenergetic neutron beam propagating through shielding materials, displaying macroscopic cross section, mean free path, and HVL.",
    "isAnimated": True,
    "controls": [
        {"id": "incidentIntensity", "label": "Incident Intensity I0 (n/cm²·s)", "min": 1000, "max": 10000, "step": 500, "value": 5000},
        {"id": "macroSigma", "label": "Macroscopic Cross Section Σt (cm⁻¹)", "min": 0.2, "max": 4.0, "step": 0.1, "value": 1.8},
        {"id": "shieldThick", "label": "Shield Thickness x (cm)", "min": 1.0, "max": 10.0, "step": 0.5, "value": 5.0}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 3: Fission Yield and Watt Spectrum Simulator
# -----------------------------------------------------------------------------
sims["reactor-fission-yield-spectrum-sim"] = {
    "title": "Fission Mass Yield & Prompt Neutron Watt Spectrum",
    "desc": "Displays the empirical asymmetric double-hump fission product mass yield curve Y(A) for U-235 and Pu-239 alongside the Cranberg/Watt prompt fission neutron energy distribution χ(E).",
    "isAnimated": True,
    "controls": [
        {"id": "fuelType", "label": "Fissile Isotope (1=U235, 2=Pu239)", "min": 1, "max": 2, "step": 1, "value": 1},
        {"id": "displayMode", "label": "Display (1=Mass Yield, 2=Watt Spectrum)", "min": 1, "max": 2, "step": 1, "value": 1},
        {"id": "incidentEnergy", "label": "Neutron Energy (1=Thermal, 2=Fast)", "min": 1, "max": 2, "step": 1, "value": 1}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 4: Fuel Burnup and Energy Release Simulator
# -----------------------------------------------------------------------------
sims["reactor-fuel-burnup-energy-sim"] = {
    "title": "Reactor Thermal Power & Fuel Burnup Dynamics",
    "desc": "Simulates fuel consumption, fission rate, daily U-235 burnup, and core burnup accumulation (MWd/MTU) over multi-month reactor operating campaigns.",
    "isAnimated": True,
    "controls": [
        {"id": "corePower", "label": "Thermal Power (MWth)", "min": 1000, "max": 4500, "step": 100, "value": 3000},
        {"id": "initialFuel", "label": "Core Heavy Metal (MTU)", "min": 60, "max": 120, "step": 5, "value": 90},
        {"id": "operatingDays", "label": "Operating Days", "min": 100, "max": 730, "step": 15, "value": 500}
    ],
    "code": r"""
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
"""
}

with open("rp_sims_1_4.json", "w", encoding="utf-8") as f:
    json.dump(sims, f, indent=2, ensure_ascii=False)

print("rp_sims_1_4.json successfully written!")
