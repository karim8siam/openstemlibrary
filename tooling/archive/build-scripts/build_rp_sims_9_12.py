# -*- coding: utf-8 -*-
"""
Builder for Reactor Physics Simulations 9 to 12
9. reactor-four-factor-lifecycle-sim
10. reactor-six-factor-leakage-sim
11. reactor-geometric-buckling-geometries-sim
12. reactor-reflected-core-savings-sim
"""
import json

sims = {}

# -----------------------------------------------------------------------------
# Sim 9: Four-Factor Formula Lifecycle Simulator
# -----------------------------------------------------------------------------
sims["reactor-four-factor-lifecycle-sim"] = {
    "title": "Four-Factor Formula Animated Neutron Life Cycle",
    "desc": "Tracks 1000 fast neutrons through their complete generational life cycle: fast fission boost ϵ, resonance escape p during slowing down, thermal utilization f, and reproduction η, computing k∞ = ϵ·p·η·f.",
    "isAnimated": True,
    "controls": [
        {"id": "fastFission", "label": "Fast Fission Factor ϵ", "min": 1.00, "max": 1.08, "step": 0.01, "value": 1.03},
        {"id": "resEscape", "label": "Resonance Escape p", "min": 0.70, "max": 0.95, "step": 0.01, "value": 0.88},
        {"id": "thermUtil", "label": "Thermal Utilization f", "min": 0.75, "max": 0.98, "step": 0.01, "value": 0.89},
        {"id": "reproductionEta", "label": "Reproduction Factor η", "min": 1.30, "max": 2.20, "step": 0.05, "value": 1.65}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 10: Six-Factor Leakage and Critical Balance
# -----------------------------------------------------------------------------
sims["reactor-six-factor-leakage-sim"] = {
    "title": "Six-Factor Formula & Finite Core Leakage Balance",
    "desc": "Calculates fast and thermal non-leakage probabilities P_FNL = 1/(1 + Bg²·τ) and P_TNL = 1/(1 + Bg²·L²), demonstrating effective core multiplication keff = k∞ · P_FNL · P_TNL.",
    "isAnimated": True,
    "controls": [
        {"id": "kInf", "label": "Infinite Mult k∞", "min": 1.00, "max": 1.35, "step": 0.01, "value": 1.15},
        {"id": "coreBuckling", "label": "Buckling Bg² (×10⁻⁴ cm⁻²)", "min": 1.0, "max": 15.0, "step": 0.5, "value": 5.0},
        {"id": "migrArea", "label": "Migration Area M² (cm²)", "min": 35, "max": 350, "step": 15, "value": 150}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 11: Geometric Buckling Across 5 Canonical Geometries
# -----------------------------------------------------------------------------
sims["reactor-geometric-buckling-geometries-sim"] = {
    "title": "Geometric Buckling & Flux Profiles in 5 Canonical Geometries",
    "desc": "Solves Helmholtz critical wave equation ∇²ϕ + Bg²·ϕ = 0 across sphere, finite cylinder, cube, rectangular parallelepiped, and slab, calculating geometric buckling Bg² and optimum cylinder volume.",
    "isAnimated": True,
    "controls": [
        {"id": "geomShape", "label": "Geometry (1=Sphere, 2=Opt Cyl, 3=Cube, 4=Slab)", "min": 1, "max": 4, "step": 1, "value": 1},
        {"id": "dimSize", "label": "Characteristic Dimension (m)", "min": 1.0, "max": 5.0, "step": 0.2, "value": 2.5},
        {"id": "display3D", "label": "View Mode (1=Flux Curve, 2=Volume Bar)", "min": 1, "max": 2, "step": 1, "value": 1}
    ],
    "code": r"""
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
"""
}

# -----------------------------------------------------------------------------
# Sim 12: Reflected Reactor Core and Reflector Savings
# -----------------------------------------------------------------------------
sims["reactor-reflected-core-savings-sim"] = {
    "title": "Two-Region Reflected Core & Reflector Savings δ",
    "desc": "Solves coupled two-region diffusion equations in multiplying core and non-multiplying reflector, demonstrating the thermal flux peak in the reflector and reduction in critical core size (reflector savings δ).",
    "isAnimated": True,
    "controls": [
        {"id": "coreSize", "label": "Bare Critical Radius (cm)", "min": 30, "max": 100, "step": 5, "value": 60},
        {"id": "reflMaterial", "label": "Reflector (1=Graphite, 2=D2O, 3=Be, 4=H2O)", "min": 1, "max": 4, "step": 1, "value": 1},
        {"id": "reflThick", "label": "Reflector Thickness (cm)", "min": 10, "max": 60, "step": 5, "value": 35}
    ],
    "code": r"""
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
"""
}

with open("rp_sims_9_12.json", "w", encoding="utf-8") as f:
    json.dump(sims, f, indent=2, ensure_ascii=False)

print("rp_sims_9_12.json successfully written!")
