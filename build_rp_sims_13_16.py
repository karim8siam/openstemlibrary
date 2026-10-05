# -*- coding: utf-8 -*-
"""
Builder for Reactor Physics Simulations 13 to 16
13. reactor-point-kinetics-delayed-neutrons-sim
14. reactor-inhour-reactivity-period-sim
15. reactor-temperature-feedback-control-sim
16. reactor-xenon-samarium-poisoning-sim
"""
import json

sims = {}

# -----------------------------------------------------------------------------
# Sim 13: Point Reactor Kinetics with Delayed Neutrons
# -----------------------------------------------------------------------------
sims["reactor-point-kinetics-delayed-neutrons-sim"] = {
    "title": "Point Reactor Kinetics & Delayed Precursor Dynamics (PRKE)",
    "desc": "Solves point reactor kinetics equations with delayed neutron precursors, illustrating the instantaneous prompt jump P(0+) = P0 / (1 - ρ/β) followed by stable exponential growth or decay.",
    "isAnimated": True,
    "controls": [
        {"id": "reactivityRho", "label": "Reactivity ρ ($)", "min": -1.5, "max": 0.8, "step": 0.1, "value": 0.3},
        {"id": "genTimeLambda", "label": "Generation Time Λ (×10⁻⁴ s)", "min": 0.2, "max": 5.0, "step": 0.2, "value": 1.0},
        {"id": "simTimeSpan", "label": "Simulation Time Window (s)", "min": 5, "max": 40, "step": 5, "value": 20}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 14: Inhour Equation Reactivity-Period Solver
# -----------------------------------------------------------------------------
sims["reactor-inhour-reactivity-period-sim"] = {
    "title": "Inhour Equation Solver: Reactivity vs Stable Period",
    "desc": "Solves the exact 6-group Inhour equation ρ = Λ/T + ∑ βi/(1 + λi·T), displaying the characteristic curve, vertical asymptote poles at -1/λi, and the prompt critical boundary ρ = 1$.",
    "isAnimated": True,
    "controls": [
        {"id": "rhoInputDollars", "label": "Reactivity ($)", "min": -1.5, "max": 0.95, "step": 0.05, "value": 0.4},
        {"id": "precursorNuclide", "label": "Fissile Fuel (1=U235, 2=Pu239)", "min": 1, "max": 2, "step": 1, "value": 1},
        {"id": "plotRangeT", "label": "Period Range (s)", "min": 20, "max": 120, "step": 20, "value": 60}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 15: Temperature Feedback & Control Rod Dynamics
# -----------------------------------------------------------------------------
sims["reactor-temperature-feedback-control-sim"] = {
    "title": "Reactivity Feedback & Control Rod Self-Regulation",
    "desc": "Simulates inherent negative reactivity feedback (Doppler coefficient αD and moderator coefficient αM) counteracting positive reactivity step insertions and stabilizing reactor power.",
    "isAnimated": True,
    "controls": [
        {"id": "stepDisturb", "label": "Step Disturbance (pcm)", "min": -300, "max": 400, "step": 50, "value": 200},
        {"id": "dopplerCoeff", "label": "Doppler Coeff αD (pcm/°C)", "min": -5.0, "max": -1.0, "step": 0.5, "value": -2.5},
        {"id": "rodInsertion", "label": "Control Rod Depth z/H (%)", "min": 0, "max": 100, "step": 5, "value": 30}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 16: Xenon-135 and Iodine-135 Dynamics ("The Iodine Pit")
# -----------------------------------------------------------------------------
sims["reactor-xenon-samarium-poisoning-sim"] = {
    "title": "Fission Product Poisoning Dynamics & Post-Shutdown Iodine Pit",
    "desc": "Solves coupled differential equations for Iodine-135 and Xenon-135 (σa = 2.65×10⁶ b), displaying steady-state equilibrium poisoning and the dangerous post-shutdown xenon peak 10 hours later.",
    "isAnimated": True,
    "controls": [
        {"id": "fluxLevel", "label": "Thermal Flux ϕ0 (×10¹⁴ n/cm²·s)", "min": 0.5, "max": 3.0, "step": 0.5, "value": 1.5},
        {"id": "reactorStatus", "label": "Core State (1=Shutdown Trip, 2=Steady State)", "min": 1, "max": 2, "step": 1, "value": 1},
        {"id": "historyHours", "label": "Time Window (hours)", "min": 24, "max": 72, "step": 12, "value": 48}
    ],
    "code": r"""
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
"""
}

with open("rp_sims_13_16.json", "w", encoding="utf-8") as f:
    json.dump(sims, f, indent=2, ensure_ascii=False)

print("rp_sims_13_16.json successfully written!")
