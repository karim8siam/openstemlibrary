# -*- coding: utf-8 -*-
"""
Builder for Reactor Physics Simulations 5 to 8
5. reactor-elastic-moderation-kinematics-sim
6. reactor-slowing-down-density-resonance-sim
7. reactor-fick-diffusion-flux-sim
8. reactor-fermi-age-slowing-sim
"""
import json

sims = {}

# -----------------------------------------------------------------------------
# Sim 5: Elastic Moderation Kinematics
# -----------------------------------------------------------------------------
sims["reactor-elastic-moderation-kinematics-sim"] = {
    "title": "Neutron Elastic Moderation Kinematics in CM & LAB Frames",
    "desc": "Simulates 2D elastic collision kinematics between a neutron and moderator nucleus (H, D, Be, C, U), calculating collision parameter α, average cosine μ0 = 2/(3A), logarithmic decrement ξ, and collision count.",
    "isAnimated": True,
    "controls": [
        {"id": "targetNuclide", "label": "Target (1=H, 2=D, 3=Be, 4=C, 5=U)", "min": 1, "max": 5, "step": 1, "value": 1},
        {"id": "cmAngle", "label": "CM Scattering Angle θ_CM (deg)", "min": 0, "max": 180, "step": 5, "value": 90},
        {"id": "incidentEnergy", "label": "Incident Energy E1 (MeV)", "min": 0.5, "max": 5.0, "step": 0.5, "value": 2.0}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 6: Slowing Down Density and Resonance Escape
# -----------------------------------------------------------------------------
sims["reactor-slowing-down-density-resonance-sim"] = {
    "title": "Slowing-Down Density q(E) & Resonance Escape Probability",
    "desc": "Simulates continuous slowing-down epithermal flux ϕ(E) ~ 1/E, displaying sharp U-238 radiative capture resonances (6.67 eV, 20.9 eV, 36.7 eV) and Doppler broadening temperature effects on resonance escape p.",
    "isAnimated": True,
    "controls": [
        {"id": "modType", "label": "Moderator (1=H2O, 2=D2O, 3=Graphite)", "min": 1, "max": 3, "step": 1, "value": 1},
        {"id": "modFuelRatio", "label": "Moderator/Fuel Ratio NM/NF", "min": 100, "max": 600, "step": 50, "value": 300},
        {"id": "fuelTemp", "label": "Fuel Temperature (K)", "min": 300, "max": 1200, "step": 100, "value": 600}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 7: Fick's Law and 1D Diffusion Solver
# -----------------------------------------------------------------------------
sims["reactor-fick-diffusion-flux-sim"] = {
    "title": "Neutron Diffusion Theory & Fick's Law Flux Profiles",
    "desc": "Solves steady-state 1D/radial neutron diffusion equation -D∇²ϕ + Σa ϕ = S(r), demonstrating Fick's Law J = -D∇ϕ, thermal diffusion length L = √(D/Σa), and extrapolated boundary d = 0.71 λtr.",
    "isAnimated": True,
    "controls": [
        {"id": "mediumType", "label": "Medium (1=H2O, 2=D2O, 3=Be, 4=Graphite)", "min": 1, "max": 4, "step": 1, "value": 1},
        {"id": "sourceGeom", "label": "Geometry (1=Point Source, 2=Planar Sheet)", "min": 1, "max": 2, "step": 1, "value": 1},
        {"id": "coreRadius", "label": "Boundary Radius R (cm)", "min": 10, "max": 60, "step": 5, "value": 30}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 8: Fermi Age Equation Slowing Down
# -----------------------------------------------------------------------------
sims["reactor-fermi-age-slowing-sim"] = {
    "title": "Fermi Age Theory & Fast Neutron Slowing-Down Density",
    "desc": "Solves the Fermi Age diffusion equation ∇²q = ∂q/∂τ, showing the Gaussian spatial spreading of fast neutrons q(r, τ) as age τ increases from fission birth to thermal energy.",
    "isAnimated": True,
    "controls": [
        {"id": "fermiAge", "label": "Fermi Age τ (cm²)", "min": 10, "max": 350, "step": 10, "value": 100},
        {"id": "sourcePower", "label": "Source Strength S (×10⁶ n/s)", "min": 1, "max": 10, "step": 1, "value": 5},
        {"id": "plotRange", "label": "Radial Plot Range (cm)", "min": 20, "max": 80, "step": 10, "value": 50}
    ],
    "code": r"""
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
"""
}

with open("rp_sims_5_8.json", "w", encoding="utf-8") as f:
    json.dump(sims, f, indent=2, ensure_ascii=False)

print("rp_sims_5_8.json successfully written!")
