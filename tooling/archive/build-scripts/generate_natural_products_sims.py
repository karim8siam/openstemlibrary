# -*- coding: utf-8 -*-
"""
generate_natural_products_sims.py
Generates natural-products-chemistry-sims.js containing all 10 interactive 60 FPS Canvas simulations
for Chemistry of Natural Products.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

import os
import re

sims_code = r"""/**
 * natural-products-chemistry-sims.js
 * 10 Interactive 60 FPS Canvas Simulation Engines for Chemistry of Natural Products
 * OpenSTEM Master Digital Textbook
 * Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
 */

window.SimulationEngine = window.SimulationEngine || {};

// Helper: Setup Canvas with Device Pixel Ratio
function setupCanvas(canvas) {
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  const width = rect.width || canvas.width || 800;
  const height = rect.height || canvas.height || 420;
  canvas.width = width * dpr;
  canvas.height = height * dpr;
  const ctx = canvas.getContext('2d');
  ctx.scale(dpr, dpr);
  return { ctx, width, height };
}

/* ==========================================================================
   SIMULATION 1: Biosynthetic Pathway Tracer (Unit 1)
   sim_nat_biosynthetic_pathway_tracer
   ========================================================================== */
window.sim_nat_biosynthetic_pathway_tracer = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">🌿 Biosynthetic Route & Secondary Metabolite Metabolic Tracer</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Pathway:
            <select id="sim1_path" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:3px 8px; font-size:0.85rem;">
              <option value="mva">Mevalonate (MVA) -> Terpenoids/Steroids</option>
              <option value="mep">Non-Mevalonate (MEP/DOXP) -> Monoterpenes</option>
              <option value="shikimate">Shikimic Acid -> Phenylpropanoids/Alkaloids</option>
              <option value="polyketide">Polyketide (PKS) -> Macrolides/Aromatics</option>
            </select>
          </label>
          <label style="font-size:0.85rem; color:#94a3b8;">Flux Speed:
            <input type="range" id="sim1_speed" min="1" max="5" value="2" style="width:70px;">
          </label>
          <button id="sim1_pulse" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:4px 10px; font-size:0.85rem; cursor:pointer;">Inject 14C Tracer</button>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim1_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div id="sim1_info" style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span>Active Flux: Acetyl-CoA -> HMG-CoA -> Mevalonate -> IPP/DMAPP</span>
        <span id="sim1_tracer_count" style="color:#a855f7;">Radioactive Tracers: 0</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim1_canvas");
  let ctx, width, height;
  const pathSelect = document.getElementById("sim1_path");
  const speedSlider = document.getElementById("sim1_speed");
  const pulseBtn = document.getElementById("sim1_pulse");
  const infoSpan = container.querySelector("#sim1_info span:first-child");
  const tracerSpan = document.getElementById("sim1_tracer_count");

  let tracers = [];
  let animId;

  const pathways = {
    mva: {
      title: "Active Pathway: Mevalonate (MVA) -> HMG-CoA Reductase -> IPP/DMAPP -> Steroids",
      nodes: [
        { name: "Acetyl-CoA", x: 0.12, y: 0.5, color: "#38bdf8" },
        { name: "Acetoacetyl-CoA", x: 0.30, y: 0.5, color: "#38bdf8" },
        { name: "HMG-CoA", x: 0.48, y: 0.5, color: "#f59e0b" },
        { name: "Mevalonate", x: 0.66, y: 0.5, color: "#10b981" },
        { name: "IPP / DMAPP", x: 0.88, y: 0.5, color: "#ec4899" }
      ]
    },
    mep: {
      title: "Active Pathway: 1-Deoxy-D-xylulose 5-phosphate (MEP/DOXP) -> Monoterpenes",
      nodes: [
        { name: "Pyruvate + GAP", x: 0.12, y: 0.5, color: "#38bdf8" },
        { name: "DOXP Synthase", x: 0.32, y: 0.5, color: "#f59e0b" },
        { name: "MEP Reductoisomerase", x: 0.52, y: 0.5, color: "#10b981" },
        { name: "HMBPP Intermediate", x: 0.72, y: 0.5, color: "#a855f7" },
        { name: "IPP + DMAPP", x: 0.90, y: 0.5, color: "#ec4899" }
      ]
    },
    shikimate: {
      title: "Active Pathway: Shikimic Acid -> Chorismate -> Phenylalanine/Tyrosine -> Alkaloids",
      nodes: [
        { name: "PEP + Erythrose-4P", x: 0.12, y: 0.5, color: "#38bdf8" },
        { name: "3-Dehydroquinate", x: 0.32, y: 0.5, color: "#38bdf8" },
        { name: "Shikimic Acid", x: 0.52, y: 0.5, color: "#10b981" },
        { name: "Chorismic Acid", x: 0.72, y: 0.5, color: "#f59e0b" },
        { name: "Aromatic Alkaloids", x: 0.90, y: 0.5, color: "#ec4899" }
      ]
    },
    polyketide: {
      title: "Active Pathway: Acetyl-CoA Starter + Malonyl-CoA Extenders -> Poly-beta-keto -> Macrolides",
      nodes: [
        { name: "Acetyl-CoA Starter", x: 0.12, y: 0.5, color: "#38bdf8" },
        { name: "Malonyl-CoA (xN)", x: 0.32, y: 0.5, color: "#f59e0b" },
        { name: "PKS Claisen Modules", x: 0.52, y: 0.5, color: "#a855f7" },
        { name: "Polyketide Chain", x: 0.72, y: 0.5, color: "#10b981" },
        { name: "Cyclized Macrolide", x: 0.90, y: 0.5, color: "#ec4899" }
      ]
    }
  };

  function spawnTracers() {
    for (let i = 0; i < 8; i++) {
      tracers.push({
        progress: Math.random() * 0.1,
        speed: 0.003 * (0.8 + Math.random() * 0.4),
        yOffset: (Math.random() - 0.5) * 20,
        color: "#f43f5e"
      });
    }
  }

  pulseBtn.onclick = () => {
    for (let i = 0; i < 15; i++) {
      tracers.push({
        progress: 0,
        speed: 0.004 * (0.9 + Math.random() * 0.3),
        yOffset: (Math.random() - 0.5) * 25,
        color: "#a855f7"
      });
    }
  };

  pathSelect.onchange = () => {
    infoSpan.textContent = pathways[pathSelect.value].title;
    tracers = [];
    spawnTracers();
  };

  function render() {
    const res = setupCanvas(canvas);
    ctx = res.ctx;
    width = res.width;
    height = res.height;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    // Draw background grid
    ctx.strokeStyle = "rgba(255,255,255,0.03)";
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 40) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
    }
    for (let y = 0; y < height; y += 40) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
    }

    const currPath = pathways[pathSelect.value];
    const nodes = currPath.nodes;
    const speedMult = parseFloat(speedSlider.value);

    // Draw Pathway Flow Conduit
    ctx.lineWidth = 8;
    ctx.strokeStyle = "rgba(56, 189, 248, 0.2)";
    ctx.beginPath();
    nodes.forEach((n, idx) => {
      const nx = n.x * width;
      const ny = n.y * height;
      if (idx === 0) ctx.moveTo(nx, ny);
      else ctx.lineTo(nx, ny);
    });
    ctx.stroke();

    ctx.lineWidth = 2;
    ctx.strokeStyle = "#38bdf8";
    ctx.beginPath();
    nodes.forEach((n, idx) => {
      const nx = n.x * width;
      const ny = n.y * height;
      if (idx === 0) ctx.moveTo(nx, ny);
      else ctx.lineTo(nx, ny);
    });
    ctx.stroke();

    // Update and draw Tracers
    if (Math.random() < 0.08) spawnTracers();

    for (let i = tracers.length - 1; i >= 0; i--) {
      const t = tracers[i];
      t.progress += t.speed * speedMult;
      if (t.progress >= 1.0) {
        tracers.splice(i, 1);
        continue;
      }

      // Compute position along polyline
      const totalSegs = nodes.length - 1;
      const segIndex = Math.min(Math.floor(t.progress * totalSegs), totalSegs - 1);
      const segFrac = (t.progress * totalSegs) - segIndex;

      const p1 = nodes[segIndex];
      const p2 = nodes[segIndex + 1];
      const px = (p1.x + (p2.x - p1.x) * segFrac) * width;
      const py = (p1.y + (p2.y - p1.y) * segFrac) * height + t.yOffset;

      ctx.fillStyle = t.color;
      ctx.shadowColor = t.color;
      ctx.shadowBlur = 10;
      ctx.beginPath();
      ctx.arc(px, py, 4.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    tracerSpan.textContent = `Radioactive Tracers: ${tracers.length}`;

    // Draw Reaction Nodes (Enzymes & Intermediates)
    nodes.forEach((n, idx) => {
      const nx = n.x * width;
      const ny = n.y * height;

      // Outer Glow
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.strokeStyle = n.color;
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.roundRect(nx - 55, ny - 28, 110, 56, 8);
      ctx.fill();
      ctx.stroke();

      // Node text
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 11px 'Inter', sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(n.name, nx, ny);

      // Node step badge
      ctx.fillStyle = n.color;
      ctx.font = "9px 'Inter', sans-serif";
      ctx.fillText(`Step ${idx + 1}`, nx, ny + 18);
    });

    animId = requestAnimationFrame(render);
  }

  spawnTracers();
  render();

  window.addEventListener('resize', () => setupCanvas(canvas));
};

/* ==========================================================================
   SIMULATION 2: Isoprene Rule Builder & Terpenoid Assembler (Unit 2)
   sim_nat_isoprene_rule_builder
   ========================================================================== */
window.sim_nat_isoprene_rule_builder = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">🧱 Wallach Isoprene Rule (C5H8)n Assembler</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Class:
            <select id="sim2_class" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:3px 8px; font-size:0.85rem;">
              <option value="monoterpene">Monoterpene (C10 - Myrcene / Citral)</option>
              <option value="sesquiterpene">Sesquiterpene (C15 - Farnesol)</option>
              <option value="diterpene">Diterpene (C20 - Phytol)</option>
              <option value="triterpene">Triterpene (C30 - Squalene tail-tail)</option>
            </select>
          </label>
          <label style="font-size:0.85rem; color:#94a3b8;">Linkage Mode:
            <select id="sim2_mode" style="background:#1e293b; color:#10b981; border:1px solid #334155; border-radius:4px; padding:3px 8px; font-size:0.85rem;">
              <option value="regular">Regular Head-to-Tail (1->4)</option>
              <option value="irregular">Irregular Tail-to-Tail (4->4)</option>
            </select>
          </label>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim2_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div id="sim2_footer" style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span id="sim2_desc">Formula: C10H16 • Units: 2 Isoprene (Head-to-Tail 1->4) • Natural Essential Oil Terpene</span>
        <span id="sim2_rule_status" style="color:#10b981; font-weight:600;">✓ O. Wallach Special Isoprene Rule Compliant</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim2_canvas");
  const classSelect = document.getElementById("sim2_class");
  const modeSelect = document.getElementById("sim2_mode");
  const descSpan = document.getElementById("sim2_desc");
  const statusSpan = document.getElementById("sim2_rule_status");

  let tOffset = 0;

  function updateDesc() {
    const cls = classSelect.value;
    const mode = modeSelect.value;
    if (cls === "monoterpene") {
      descSpan.textContent = "Formula: C10H16 • 2 Units (C5) • Myrcene / Citral / Geraniol Acyclic Monoterpenes";
    } else if (cls === "sesquiterpene") {
      descSpan.textContent = "Formula: C15H24 • 3 Units (C5) • Farnesol / Bisabolene Essential Oil Sesquiterpenes";
    } else if (cls === "diterpene") {
      descSpan.textContent = "Formula: C20H32 • 4 Units (C5) • Phytol Chlorophyll Side-Chain Diterpenes";
    } else {
      descSpan.textContent = "Formula: C30H48 • 6 Units (C5) • Squalene Biological Steroid Precursor (Central 4-4 Coupling)";
    }

    if (mode === "regular") {
      statusSpan.textContent = "✓ Regular Head-to-Tail (1->4) Isoprene Linkage";
      statusSpan.style.color = "#10b981";
    } else {
      statusSpan.textContent = "⚠️ Irregular Tail-to-Tail (4->4) Symmetrical Dimerization";
      statusSpan.style.color = "#f59e0b";
    }
  }

  classSelect.onchange = updateDesc;
  modeSelect.onchange = updateDesc;

  function render() {
    const res = setupCanvas(canvas);
    const ctx = res.ctx;
    const width = res.width;
    const height = res.height;

    tOffset += 0.02;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    const cls = classSelect.value;
    const mode = modeSelect.value;
    const unitCount = cls === "monoterpene" ? 2 : (cls === "sesquiterpene" ? 3 : (cls === "diterpene" ? 4 : 6));

    const cy = height * 0.5;
    const totalSpan = width * 0.8;
    const stepX = totalSpan / (unitCount + 0.5);
    const startX = (width - totalSpan) * 0.5 + 40;

    // Draw individual isoprene units
    for (let i = 0; i < unitCount; i++) {
      const ux = startX + i * stepX;
      const uy = cy + Math.sin(tOffset + i * 0.8) * 12;

      // Draw Isoprene Skeleton: C1-C2(=C)-C3=C4 with methyl at C2
      ctx.strokeStyle = i % 2 === 0 ? "#38bdf8" : "#a855f7";
      ctx.lineWidth = 3;

      // C1
      const c1x = ux - 35, c1y = uy + 20;
      // C2 (branched)
      const c2x = ux - 15, c2y = uy - 15;
      // C2-methyl (C5)
      const c5x = ux - 15, c5y = uy - 45;
      // C3
      const c3x = ux + 15, c3y = uy - 15;
      // C4
      const c4x = ux + 35, c4y = uy + 20;

      ctx.beginPath();
      ctx.moveTo(c1x, c1y);
      ctx.lineTo(c2x, c2y);
      ctx.lineTo(c3x, c3y);
      ctx.lineTo(c4x, c4y);
      ctx.stroke();

      // Methyl branch
      ctx.beginPath();
      ctx.moveTo(c2x, c2y);
      ctx.lineTo(c5x, c5y);
      ctx.stroke();

      // Double bond accent
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(c1x + 4, c1y - 3);
      ctx.lineTo(c2x + 4, c2y - 3);
      ctx.stroke();

      // Atoms circles
      const atoms = [
        { x: c1x, y: c1y, label: "H (1)", col: "#38bdf8" },
        { x: c2x, y: c2y, label: "2", col: "#94a3b8" },
        { x: c5x, y: c5y, label: "Me", col: "#f59e0b" },
        { x: c3x, y: c3y, label: "3", col: "#94a3b8" },
        { x: c4x, y: c4y, label: "T (4)", col: "#ec4899" }
      ];

      atoms.forEach(a => {
        ctx.fillStyle = "#0f172a";
        ctx.strokeStyle = a.col;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(a.x, a.y, 11, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#f8fafc";
        ctx.font = "bold 9px 'Inter', sans-serif";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(a.label, a.x, a.y);
      });

      // Unit bounding box
      ctx.strokeStyle = "rgba(255,255,255,0.1)";
      ctx.lineWidth = 1;
      ctx.setLineDash([4, 4]);
      ctx.strokeRect(ux - 45, uy - 55, 90, 85);
      ctx.setLineDash([]);

      ctx.fillStyle = "#64748b";
      ctx.font = "10px 'Inter', sans-serif";
      ctx.fillText(`Unit ${i+1} (C5)`, ux, uy + 42);

      // Connective Bond to Next Unit
      if (i < unitCount - 1) {
        const nextX = startX + (i + 1) * stepX - 35;
        const nextY = cy + Math.sin(tOffset + (i + 1) * 0.8) * 12 + 20;

        const isTailTail = (mode === "irregular" && i === Math.floor(unitCount / 2) - 1);
        ctx.strokeStyle = isTailTail ? "#eab308" : "#10b981";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(c4x, c4y);
        ctx.lineTo(nextX, nextY);
        ctx.stroke();

        // Label Linkage
        ctx.fillStyle = isTailTail ? "#eab308" : "#10b981";
        ctx.font = "bold 10px 'Inter', sans-serif";
        ctx.fillText(isTailTail ? "4-4 Tail-Tail" : "1-4 Head-Tail", (c4x + nextX) * 0.5, (c4y + nextY) * 0.5 - 12);
      }
    }

    requestAnimationFrame(render);
  }

  render();
};

/* ==========================================================================
   SIMULATION 3: Monoterpene Carbocation Cyclization Cascade (Unit 3)
   sim_nat_terpene_cyclization_cascade
   ========================================================================== */
window.sim_nat_terpene_cyclization_cascade = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">🔄 GPP Enzymatic Carbocation Folding & Cyclization Cascade</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Target Terpene:
            <select id="sim3_target" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:3px 8px; font-size:0.85rem;">
              <option value="limonene">Limonene (Monocyclic Monoterpene)</option>
              <option value="pinene">alpha-Pinene (Bicyclic 6-4 Ring)</option>
              <option value="borneol">Borneol / Camphor (Bicyclic 6-5 Ring)</option>
            </select>
          </label>
          <button id="sim3_step_btn" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:4px 12px; font-size:0.85rem; cursor:pointer;">Advance Reaction Step</button>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim3_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span id="sim3_step_info">Step 1: Geranyl Pyrophosphate (GPP) ionization with release of PPi -> Geranyl carbocation</span>
        <span id="sim3_carbocation_state" style="color:#f59e0b; font-weight:600;">[Intermediate: Allylic Carbocation]</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim3_canvas");
  const targetSelect = document.getElementById("sim3_target");
  const stepBtn = document.getElementById("sim3_step_btn");
  const infoSpan = document.getElementById("sim3_step_info");
  const stateSpan = document.getElementById("sim3_carbocation_state");

  let step = 0;
  const steps = [
    { text: "Step 1: Geranyl Pyrophosphate (GPP) ionization -> PPi loss generates allylic geranyl carbocation", state: "[Allylic C+]" },
    { text: "Step 2: Linalyl pyrophosphate isomerization allows C2-C3 rotation into cisoid conformer", state: "[Linalyl C+]" },
    { text: "Step 3: Intramolecular electrophilic attack on C6=C7 double bond yields alpha-terpinyl carbocation", state: "[alpha-Terpinyl C+ (Cyclized 6-Membered)]" },
    { text: "Step 4: Enzymatic deprotonation / Wagner-Meerwein shift quenches carbocation to yield target terpene", state: "[Neutral Terpenoid Product Formed]" }
  ];

  stepBtn.onclick = () => {
    step = (step + 1) % steps.length;
    infoSpan.textContent = steps[step].text;
    stateSpan.textContent = steps[step].state;
  };

  targetSelect.onchange = () => {
    step = 0;
    infoSpan.textContent = steps[0].text;
    stateSpan.textContent = steps[0].state;
  };

  function render() {
    const res = setupCanvas(canvas);
    const ctx = res.ctx;
    const width = res.width;
    const height = res.height;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    const cx = width * 0.5;
    const cy = height * 0.5;

    // Draw Enzyme Pocket Boundary
    ctx.strokeStyle = "rgba(56, 189, 248, 0.15)";
    ctx.lineWidth = 14;
    ctx.beginPath();
    ctx.arc(cx, cy, 140, 0.2 * Math.PI, 1.8 * Math.PI);
    ctx.stroke();

    ctx.fillStyle = "#64748b";
    ctx.font = "12px 'Inter', sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("Terpene Cyclase Hydrophobic Active Site Pocket", cx, cy - 155);

    // Draw Molecular Scaffold based on step
    if (step === 0) {
      // Linear GPP
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(cx - 120, cy);
      ctx.lineTo(cx - 60, cy - 30);
      ctx.lineTo(cx, cy);
      ctx.lineTo(cx + 60, cy - 30);
      ctx.lineTo(cx + 120, cy);
      ctx.stroke();

      // OPP Group
      ctx.fillStyle = "#ef4444";
      ctx.beginPath(); ctx.arc(cx + 120, cy, 12, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 9px sans-serif"; ctx.fillText("OPP", cx + 120, cy + 3);
    } else if (step === 1) {
      // Bent linalyl
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.arc(cx, cy, 50, Math.PI, 0);
      ctx.lineTo(cx + 60, cy + 40);
      ctx.stroke();

      // Positive charge
      ctx.fillStyle = "#eab308";
      ctx.beginPath(); ctx.arc(cx - 50, cy, 10, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#000"; ctx.font = "bold 12px sans-serif"; ctx.fillText("+", cx - 50, cy + 4);
    } else if (step === 2) {
      // 6-membered terpinyl cation ring
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 4;
      ctx.beginPath();
      for (let a = 0; a < 6; a++) {
        const ang = (a * Math.PI) / 3;
        const px = cx + Math.cos(ang) * 55;
        const py = cy + Math.sin(ang) * 55;
        if (a === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.stroke();

      // Exocyclic isopropyl cation
      ctx.beginPath();
      ctx.moveTo(cx + 55, cy);
      ctx.lineTo(cx + 100, cy);
      ctx.lineTo(cx + 125, cy - 25);
      ctx.moveTo(cx + 100, cy);
      ctx.lineTo(cx + 125, cy + 25);
      ctx.stroke();

      ctx.fillStyle = "#eab308";
      ctx.beginPath(); ctx.arc(cx + 100, cy, 10, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#000"; ctx.font = "bold 12px sans-serif"; ctx.fillText("+", cx + 100, cy + 4);
    } else {
      // Product Terpene (Limonene)
      ctx.strokeStyle = "#ec4899";
      ctx.lineWidth = 4;
      ctx.beginPath();
      for (let a = 0; a < 6; a++) {
        const ang = (a * Math.PI) / 3;
        const px = cx + Math.cos(ang) * 55;
        const py = cy + Math.sin(ang) * 55;
        if (a === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.stroke();

      // Isopropenyl group
      ctx.beginPath();
      ctx.moveTo(cx + 55, cy);
      ctx.lineTo(cx + 95, cy);
      ctx.lineTo(cx + 120, cy - 25);
      ctx.moveTo(cx + 95, cy);
      ctx.lineTo(cx + 120, cy + 25);
      ctx.stroke();

      ctx.fillStyle = "#10b981";
      ctx.font = "bold 14px 'Inter', sans-serif";
      ctx.fillText("Neutral Product: Limonene (C10H16)", cx, cy + 95);
    }

    requestAnimationFrame(render);
  }

  render();
};

/* ==========================================================================
   SIMULATION 4: Glucose Mutarotation & Chair Conformation (Unit 4)
   sim_nat_glucose_mutarotation_chair
   ========================================================================== */
window.sim_nat_glucose_mutarotation_chair = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">🌀 D-Glucose Mutarotation Kinetics & 4C1 Chair Equilibria</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Initial Species:
            <select id="sim4_init" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:3px 8px; font-size:0.85rem;">
              <option value="alpha">Pure alpha-D-Glucopyranose (+112.0°)</option>
              <option value="beta">Pure beta-D-Glucopyranose (+18.7°)</option>
            </select>
          </label>
          <button id="sim4_reset" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:4px 10px; font-size:0.85rem; cursor:pointer;">Reset Reaction</button>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim4_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span id="sim4_comp">Composition: 36.4% alpha-anomer | <0.02% open-chain | 63.6% beta-anomer</span>
        <span id="sim4_rot" style="color:#38bdf8; font-weight:600;">Observed [alpha]D: +52.7° (Equilibrium)</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim4_canvas");
  const initSelect = document.getElementById("sim4_init");
  const resetBtn = document.getElementById("sim4_reset");
  const compSpan = document.getElementById("sim4_comp");
  const rotSpan = document.getElementById("sim4_rot");

  let simTime = 0;
  let alphaFrac = 1.0;
  let betaFrac = 0.0;

  function resetSim() {
    simTime = 0;
    if (initSelect.value === "alpha") {
      alphaFrac = 1.0;
      betaFrac = 0.0;
    } else {
      alphaFrac = 0.0;
      betaFrac = 1.0;
    }
  }

  initSelect.onchange = resetSim;
  resetBtn.onclick = resetSim;
  resetSim();

  function render() {
    const res = setupCanvas(canvas);
    const ctx = res.ctx;
    const width = res.width;
    const height = res.height;

    simTime += 0.01;

    // Mutarotation kinetic approach to equilibrium: 36.4% alpha, 63.6% beta
    const targetAlpha = 0.364;
    const k = 0.015;
    if (initSelect.value === "alpha") {
      alphaFrac = targetAlpha + (1.0 - targetAlpha) * Math.exp(-k * simTime * 10);
    } else {
      alphaFrac = targetAlpha * (1.0 - Math.exp(-k * simTime * 10));
    }
    betaFrac = 1.0 - alphaFrac;

    const optRot = alphaFrac * 112.0 + betaFrac * 18.7;
    compSpan.textContent = `Composition: ${(alphaFrac * 100).toFixed(1)}% alpha-anomer | ${(betaFrac * 100).toFixed(1)}% beta-anomer`;
    rotSpan.textContent = `Observed [alpha]D: +${optRot.toFixed(1)}°`;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    // Left Panel: Polarimeter Dial
    const dialX = width * 0.25;
    const dialY = height * 0.5;
    const dialR = 85;

    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.arc(dialX, dialY, dialR, 0, Math.PI * 2);
    ctx.stroke();

    // Polarimeter needle
    const needleAng = ((optRot - 65) * Math.PI) / 180;
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(dialX, dialY);
    ctx.lineTo(dialX + Math.cos(needleAng) * (dialR - 10), dialY + Math.sin(needleAng) * (dialR - 10));
    ctx.stroke();

    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px 'Inter', sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(`[alpha]D = +${optRot.toFixed(1)}°`, dialX, dialY + dialR + 25);
    ctx.font = "11px 'Inter', sans-serif";
    ctx.fillStyle = "#64748b";
    ctx.fillText("Biot Optical Rotation Polarimeter", dialX, dialY - dialR - 15);

    // Right Panel: Dynamic Equilibrium Bar & Chair structures
    const barX = width * 0.55;
    const barY = height * 0.35;
    const barW = width * 0.38;
    const barH = 28;

    // Alpha bar
    ctx.fillStyle = "#f59e0b";
    ctx.fillRect(barX, barY, barW * alphaFrac, barH);
    // Beta bar
    ctx.fillStyle = "#10b981";
    ctx.fillRect(barX + barW * alphaFrac, barY, barW * betaFrac, barH);

    ctx.strokeStyle = "#475569";
    ctx.lineWidth = 1.5;
    ctx.strokeRect(barX, barY, barW, barH);

    ctx.fillStyle = "#f8fafc";
    ctx.font = "bold 11px sans-serif";
    ctx.textAlign = "left";
    ctx.fillText(`alpha-D: ${(alphaFrac * 100).toFixed(1)}% (axial C1-OH)`, barX, barY - 10);
    ctx.textAlign = "right";
    ctx.fillText(`beta-D: ${(betaFrac * 100).toFixed(1)}% (equatorial C1-OH)`, barX + barW, barY - 10);

    // Chair conformation representations
    ctx.fillStyle = "#e2e8f0";
    ctx.font = "11px sans-serif";
    ctx.textAlign = "left";
    ctx.fillText("beta-D-Glucopyranose (All 5 Substituents Equatorial in 4C1 Chair)", barX, barY + 70);
    ctx.fillStyle = "#94a3b8";
    ctx.font = "10px sans-serif";
    ctx.fillText("• Minimum 1,3-diaxial steric strain (Delta G° = -1.4 kJ/mol relative to alpha)", barX, barY + 90);
    ctx.fillText("• Anomeric effect stabilizes alpha-anomer partially in non-polar solvents", barX, barY + 110);
    ctx.fillText("• Water stabilizes beta-anomer via equatorial hydration shell", barX, barY + 130);

    requestAnimationFrame(render);
  }

  render();
};

/* ==========================================================================
   SIMULATION 5: Sucrose Inversion Polarimetry Kinetics (Unit 5)
   sim_nat_sucrose_inversion_polarimetry
   ========================================================================== */
window.sim_nat_sucrose_inversion_polarimetry = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">🧪 Inversion of Cane Sugar Polarimetric Kinetic Reactor</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Temp (T):
            <input type="range" id="sim5_temp" min="20" max="60" value="35" style="width:65px;">
            <span id="sim5_tval" style="color:#38bdf8; font-size:0.85rem;">35°C</span>
          </label>
          <label style="font-size:0.85rem; color:#94a3b8;">[HCl] (M):
            <input type="range" id="sim5_acid" min="0.5" max="2.0" step="0.5" value="1.0" style="width:60px;">
            <span id="sim5_aval" style="color:#10b981; font-size:0.85rem;">1.0 M</span>
          </label>
          <button id="sim5_start" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:4px 10px; font-size:0.85rem; cursor:pointer;">Restart Run</button>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim5_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span id="sim5_state">Reaction: Sucrose (+66.5°) + H2O -> D-Glucose (+52.7°) + D-Fructose (-92.4°)</span>
        <span id="sim5_angle" style="color:#f43f5e; font-weight:600;">Net Angle: +66.5° -> Inverts to -19.9°</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim5_canvas");
  const tempSlider = document.getElementById("sim5_temp");
  const acidSlider = document.getElementById("sim5_acid");
  const tVal = document.getElementById("sim5_tval");
  const aVal = document.getElementById("sim5_aval");
  const startBtn = document.getElementById("sim5_start");
  const angleSpan = document.getElementById("sim5_angle");

  let t = 0;
  let history = [];

  tempSlider.oninput = () => { tVal.textContent = `${tempSlider.value}°C`; };
  acidSlider.oninput = () => { aVal.textContent = `${parseFloat(acidSlider.value).toFixed(1)} M`; };
  startBtn.onclick = () => { t = 0; history = []; };

  function render() {
    const res = setupCanvas(canvas);
    const ctx = res.ctx;
    const width = res.width;
    const height = res.height;

    const temp = parseFloat(tempSlider.value);
    const acid = parseFloat(acidSlider.value);

    // Pseudo-first-order rate constant k_obs
    const k_obs = 0.005 * acid * Math.exp((temp - 25) / 10);
    t += 0.2;

    const fractionRemaining = Math.exp(-k_obs * t);
    // alpha(0) = +66.5, alpha(infinity) = -19.85
    const alpha_t = -19.85 + (66.5 - (-19.85)) * fractionRemaining;

    history.push({ t, alpha: alpha_t });
    if (history.length > 300) history.shift();

    angleSpan.textContent = `Elapsed: ${t.toFixed(0)} s | [alpha] = ${alpha_t.toFixed(1)}° (Inverted: ${alpha_t < 0 ? 'YES' : 'NO'})`;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    // Plot Optical Rotation vs Time
    const ox = 70;
    const oy = height - 50;
    const pw = width - 120;
    const ph = height - 100;

    // Zero-angle line
    const zeroY = oy - ((0 - (-25)) / (75 - (-25))) * ph;
    ctx.strokeStyle = "rgba(239, 68, 68, 0.4)";
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(ox, zeroY);
    ctx.lineTo(ox + pw, zeroY);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "#ef4444";
    ctx.font = "10px sans-serif";
    ctx.fillText("0° (Inversion Threshold)", ox + pw - 130, zeroY - 6);

    // Draw Axes
    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(ox, oy - ph);
    ctx.lineTo(ox, oy);
    ctx.lineTo(ox + pw, oy);
    ctx.stroke();

    // Plot line
    if (history.length > 1) {
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      history.forEach((pt, idx) => {
        const px = ox + (idx / 300) * pw;
        const py = oy - ((pt.alpha - (-25)) / (75 - (-25))) * ph;
        if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();
    }

    ctx.fillStyle = "#94a3b8";
    ctx.font = "11px 'Inter', sans-serif";
    ctx.fillText("+66.5° (Initial Sucrose)", ox + 10, oy - ph + 20);
    ctx.fillText("-19.9° (Invert Sugar)", ox + 10, oy - 15);

    requestAnimationFrame(render);
  }

  render();
};

/* ==========================================================================
   SIMULATION 6: Amino Acid Zwitterion Titration & pI Electrophoresis (Unit 6)
   sim_nat_amino_acid_titration_pi
   ========================================================================== */
window.sim_nat_amino_acid_titration_pi = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">⚡ Amino Acid Zwitterion Speciation & Isoelectric Point (pI)</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Amino Acid:
            <select id="sim6_aa" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:3px 8px; font-size:0.85rem;">
              <option value="glycine">Glycine (Neutral - pI = 5.97)</option>
              <option value="glutamic">Glutamic Acid (Acidic - pI = 3.22)</option>
              <option value="lysine">Lysine (Basic - pI = 9.74)</option>
            </select>
          </label>
          <label style="font-size:0.85rem; color:#94a3b8;">pH:
            <input type="range" id="sim6_ph" min="1.0" max="13.0" step="0.1" value="6.0" style="width:80px;">
            <span id="sim6_ph_val" style="color:#f59e0b; font-size:0.85rem;">6.0</span>
          </label>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim6_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span id="sim6_charge">Net Electric Charge: 0.00 • Electrophoretic Velocity: Stationary</span>
        <span id="sim6_pi_badge" style="color:#10b981; font-weight:600;">pI = (pK1 + pK2) / 2</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim6_canvas");
  const aaSelect = document.getElementById("sim6_aa");
  const phSlider = document.getElementById("sim6_ph");
  const phVal = document.getElementById("sim6_ph_val");
  const chargeSpan = document.getElementById("sim6_charge");
  const piBadge = document.getElementById("sim6_pi_badge");

  const aaData = {
    glycine: { pK1: 2.34, pK2: 9.60, pI: 5.97, name: "Glycine" },
    glutamic: { pK1: 2.19, pK2: 4.25, pK3: 9.67, pI: 3.22, name: "Glutamic Acid" },
    lysine: { pK1: 2.18, pK2: 8.95, pK3: 10.53, pI: 9.74, name: "Lysine" }
  };

  phSlider.oninput = () => { phVal.textContent = parseFloat(phSlider.value).toFixed(1); };

  function render() {
    const res = setupCanvas(canvas);
    const ctx = res.ctx;
    const width = res.width;
    const height = res.height;

    const cur = aaData[aaSelect.value];
    const pH = parseFloat(phSlider.value);

    // Calculate net charge
    let netCharge = 0;
    if (aaSelect.value === "glycine") {
      const fracPos = 1.0 / (1.0 + Math.pow(10, pH - cur.pK1));
      const fracNeg = 1.0 / (1.0 + Math.pow(10, cur.pK2 - pH));
      netCharge = fracPos - fracNeg;
      piBadge.textContent = `pI = (2.34 + 9.60) / 2 = 5.97`;
    } else if (aaSelect.value === "glutamic") {
      netCharge = (1 / (1 + Math.pow(10, pH - 2.19))) - (1 / (1 + Math.pow(10, 4.25 - pH))) - (1 / (1 + Math.pow(10, 9.67 - pH)));
      piBadge.textContent = `pI = (2.19 + 4.25) / 2 = 3.22`;
    } else {
      netCharge = (1 / (1 + Math.pow(10, pH - 2.18))) + (1 / (1 + Math.pow(10, pH - 8.95))) + (1 / (1 + Math.pow(10, pH - 10.53))) - 1;
      piBadge.textContent = `pI = (8.95 + 10.53) / 2 = 9.74`;
    }

    const direction = netCharge > 0.05 ? "Migrates toward Cathode (-)" : (netCharge < -0.05 ? "Migrates toward Anode (+)" : "Isoelectric Focus (Zero Migration)");
    chargeSpan.textContent = `Net Charge: ${netCharge.toFixed(2)} e • ${direction}`;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    // Draw Capillary Electrophoresis Tube
    const tubeX = 60;
    const tubeY = 50;
    const tubeW = width - 120;
    const tubeH = 70;

    ctx.fillStyle = "#0f172a";
    ctx.fillRect(tubeX, tubeY, tubeW, tubeH);
    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 2;
    ctx.strokeRect(tubeX, tubeY, tubeW, tubeH);

    // Anode (+) and Cathode (-)
    ctx.fillStyle = "#ef4444";
    ctx.fillRect(tubeX - 25, tubeY, 20, tubeH);
    ctx.fillStyle = "#3b82f6";
    ctx.fillRect(tubeX + tubeW + 5, tubeY, 20, tubeH);

    ctx.fillStyle = "#fff";
    ctx.font = "bold 11px sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("Anode (+)", tubeX - 15, tubeY + 40);
    ctx.fillText("Cathode (-)", tubeX + tubeW + 15, tubeY + 40);

    // Amino acid band position in tube
    // If netCharge < 0, shifts left; if netCharge > 0, shifts right
    const bandX = tubeX + (tubeW * 0.5) + netCharge * (tubeW * 0.4);
    ctx.fillStyle = "#a855f7";
    ctx.shadowColor = "#a855f7";
    ctx.shadowBlur = 12;
    ctx.fillRect(bandX - 8, tubeY + 4, 16, tubeH - 8);
    ctx.shadowBlur = 0;

    // Molecular State Diagram
    const molY = height * 0.65;
    ctx.fillStyle = "#f8fafc";
    ctx.font = "bold 13px 'Inter', sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(`Predominant Ionic Form at pH ${pH.toFixed(1)}:`, width * 0.5, molY - 30);

    if (netCharge > 0.4) {
      ctx.fillStyle = "#38bdf8";
      ctx.font = "14px 'Fira Code', monospace";
      ctx.fillText("H3N(+)-CH(R)-COOH  (Cationic Form)", width * 0.5, molY);
    } else if (netCharge < -0.4) {
      ctx.fillStyle = "#ef4444";
      ctx.font = "14px 'Fira Code', monospace";
      ctx.fillText("H2N-CH(R)-COO(-)  (Anionic Form)", width * 0.5, molY);
    } else {
      ctx.fillStyle = "#10b981";
      ctx.font = "14px 'Fira Code', monospace";
      ctx.fillText("H3N(+)-CH(R)-COO(-)  (Dipolar Zwitterion)", width * 0.5, molY);
    }

    requestAnimationFrame(render);
  }

  render();
};

/* ==========================================================================
   SIMULATION 7: DNA Double Helix Thermal Denaturation & Tm (Unit 7)
   sim_nat_dna_double_helix_melting
   ========================================================================== */
window.sim_nat_dna_double_helix_melting = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">🧬 DNA Double Helix Thermal Denaturation & Hyperchromicity</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Temperature:
            <input type="range" id="sim7_temp" min="40" max="100" value="70" style="width:75px;">
            <span id="sim7_tval" style="color:#ef4444; font-size:0.85rem;">70°C</span>
          </label>
          <label style="font-size:0.85rem; color:#94a3b8;">%GC Content:
            <input type="range" id="sim7_gc" min="20" max="80" value="50" style="width:65px;">
            <span id="sim7_gcval" style="color:#10b981; font-size:0.85rem;">50%</span>
          </label>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim7_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span id="sim7_melt_state">Fraction Denatured: 0.0% • B-DNA Duplex Intact</span>
        <span id="sim7_tm_badge" style="color:#38bdf8; font-weight:600;">Tm = 69.3 + 0.41(%GC) = 89.8°C</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim7_canvas");
  const tempSlider = document.getElementById("sim7_temp");
  const gcSlider = document.getElementById("sim7_gc");
  const tVal = document.getElementById("sim7_tval");
  const gcVal = document.getElementById("sim7_gcval");
  const stateSpan = document.getElementById("sim7_melt_state");
  const tmBadge = document.getElementById("sim7_tm_badge");

  tempSlider.oninput = () => { tVal.textContent = `${tempSlider.value}°C`; };
  gcSlider.oninput = () => { gcVal.textContent = `${gcSlider.value}%`; };

  function render() {
    const res = setupCanvas(canvas);
    const ctx = res.ctx;
    const width = res.width;
    const height = res.height;

    const T = parseFloat(tempSlider.value);
    const GC = parseFloat(gcSlider.value);

    // Marmur-Doty formula for Tm
    const Tm = 69.3 + 0.41 * GC;
    tmBadge.textContent = `Melting Point Tm = ${Tm.toFixed(1)}°C`;

    // Denaturation sigmoidal fraction theta
    const theta = 1.0 / (1.0 + Math.exp(-(T - Tm) / 2.5));
    stateSpan.textContent = `Fraction Denatured: ${(theta * 100).toFixed(1)}% • ${theta > 0.5 ? 'Single-Strand Random Coils' : 'B-DNA Double Helix'}`;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    // Left Panel: Hyperchromic UV Absorbance Curve (A260 vs T)
    const ox = 60;
    const oy = height - 40;
    const pw = width * 0.42;
    const ph = height - 80;

    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(ox, oy - ph);
    ctx.lineTo(ox, oy);
    ctx.lineTo(ox + pw, oy);
    ctx.stroke();

    // Plot Sigmoid
    ctx.strokeStyle = "#10b981";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let tempStep = 40; tempStep <= 100; tempStep += 1) {
      const frac = 1.0 / (1.0 + Math.exp(-(tempStep - Tm) / 2.5));
      const px = ox + ((tempStep - 40) / 60) * pw;
      const py = oy - frac * ph * 0.8 - ph * 0.1;
      if (tempStep === 40) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Current temperature marker
    const curPx = ox + ((T - 40) / 60) * pw;
    const curPy = oy - theta * ph * 0.8 - ph * 0.1;
    ctx.fillStyle = "#ef4444";
    ctx.beginPath();
    ctx.arc(curPx, curPy, 6, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "#94a3b8";
    ctx.font = "10px sans-serif";
    ctx.fillText("A260 Hyperchromicity (+40% Absorbance)", ox + 10, oy - ph + 15);
    ctx.fillText("40°C", ox, oy + 15);
    ctx.fillText("100°C", ox + pw - 25, oy + 15);

    // Right Panel: Double Helix Strand Unzipping Animation
    const hx = width * 0.72;
    const hy = height * 0.5;

    for (let b = -7; b <= 7; b++) {
      const by = hy + b * 18;
      const unzipped = Math.random() < theta;
      const separation = unzipped ? 65 : 18;

      // Base Pair
      ctx.strokeStyle = unzipped ? "#ef4444" : "#38bdf8";
      ctx.lineWidth = unzipped ? 1 : 2.5;
      ctx.beginPath();
      ctx.moveTo(hx - separation, by);
      ctx.lineTo(hx + separation, by);
      ctx.stroke();

      // Strand backbones
      ctx.fillStyle = "#ec4899";
      ctx.beginPath(); ctx.arc(hx - separation, by, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#3b82f6";
      ctx.beginPath(); ctx.arc(hx + separation, by, 4, 0, Math.PI * 2); ctx.fill();
    }

    requestAnimationFrame(render);
  }

  render();
};

/* ==========================================================================
   SIMULATION 8: Hofmann Exhaustive Methylation (Unit 8)
   sim_nat_hofmann_exhaustive_methylation
   ========================================================================== */
window.sim_nat_hofmann_exhaustive_methylation = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">🔬 Hofmann Exhaustive Methylation Alkaloid Nitrogen Ring Degradation</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Alkaloid Heterocycle:
            <select id="sim8_sub" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:3px 8px; font-size:0.85rem;">
              <option value="piperidine">Piperidine (6-Membered Monocyclic)</option>
              <option value="pyrrolidine">Pyrrolidine (5-Membered Monocyclic)</option>
              <option value="tropane">Tropane Core (Bicyclic Atropine/Cocaine)</option>
            </select>
          </label>
          <button id="sim8_next_step" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:4px 12px; font-size:0.85rem; cursor:pointer;">Trigger Next Reaction</button>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim8_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span id="sim8_step_text">Step 1: Piperidine + CH3I (excess) -> Quaternary Dimethylpiperidinium Iodide</span>
        <span id="sim8_elim_badge" style="color:#10b981; font-weight:600;">E2 Anti-Periplanar Elimination</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim8_canvas");
  const subSelect = document.getElementById("sim8_sub");
  const nextBtn = document.getElementById("sim8_next_step");
  const stepText = document.getElementById("sim8_step_text");

  let step = 0;
  const steps = [
    "Step 1: Nitrogen quaternization via excess CH3I -> Quaternary ammonium iodide salt formed",
    "Step 2: Moist silver oxide (Ag2O/H2O) treatment -> Precipitation of AgI; formation of Quaternary ammonium hydroxide",
    "Step 3: Thermal pyrolysis (heat) -> E2 anti-periplanar beta-elimination cleaves C-N bond; ring opens to dimethylamino alkene",
    "Step 4: Second exhaustive methylation & pyrolysis -> Nitrogen eliminated as N(CH3)3 gas; conjugated diene product isolated"
  ];

  nextBtn.onclick = () => {
    step = (step + 1) % steps.length;
    stepText.textContent = steps[step];
  };

  subSelect.onchange = () => {
    step = 0;
    stepText.textContent = steps[0];
  };

  function render() {
    const res = setupCanvas(canvas);
    const ctx = res.ctx;
    const width = res.width;
    const height = res.height;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    const cx = width * 0.5;
    const cy = height * 0.5;

    // Draw Reaction Mechanism Graphic
    if (step === 0) {
      // Intact Ring
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 4;
      ctx.beginPath();
      for (let a = 0; a < 6; a++) {
        const ang = (a * Math.PI) / 3;
        const px = cx + Math.cos(ang) * 60;
        const py = cy + Math.sin(ang) * 60;
        if (a === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.stroke();

      ctx.fillStyle = "#ef4444";
      ctx.beginPath(); ctx.arc(cx, cy + 60, 14, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fff"; ctx.font = "bold 11px sans-serif"; ctx.textAlign = "center";
      ctx.fillText("N+Me2", cx, cy + 64);

      ctx.fillStyle = "#f59e0b";
      ctx.fillText("I(-) Counter-ion", cx + 70, cy + 70);
    } else if (step === 1) {
      // Hydroxide Salt
      ctx.strokeStyle = "#a855f7";
      ctx.lineWidth = 4;
      ctx.beginPath();
      for (let a = 0; a < 6; a++) {
        const ang = (a * Math.PI) / 3;
        const px = cx + Math.cos(ang) * 60;
        const py = cy + Math.sin(ang) * 60;
        if (a === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.stroke();

      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(cx, cy + 60, 14, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fff"; ctx.font = "bold 11px sans-serif"; ctx.textAlign = "center";
      ctx.fillText("N+Me2", cx, cy + 64);

      ctx.fillStyle = "#10b981";
      ctx.fillText("OH(-) Hydroxide Base (AgI precipitated)", cx + 110, cy + 64);
    } else if (step === 2) {
      // Ring Opened
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(cx - 100, cy);
      ctx.lineTo(cx - 50, cy - 30);
      ctx.lineTo(cx, cy);
      ctx.lineTo(cx + 50, cy - 30);
      ctx.lineTo(cx + 100, cy);
      ctx.stroke();

      // Double bond formed
      ctx.strokeStyle = "#ef4444";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(cx - 98, cy - 4);
      ctx.lineTo(cx - 48, cy - 34);
      ctx.stroke();

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("Open-Chain Dimethylamino-pentene", cx, cy + 45);
    } else {
      // Symmetrical Diene + Trimethylamine
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(cx - 80, cy);
      ctx.lineTo(cx - 30, cy - 25);
      ctx.lineTo(cx + 20, cy);
      ctx.lineTo(cx + 70, cy - 25);
      ctx.stroke();

      // Conjugated diene bonds
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(cx - 78, cy - 5); ctx.lineTo(cx - 28, cy - 30);
      ctx.moveTo(cx + 22, cy - 5); ctx.lineTo(cx + 72, cy - 30);
      ctx.stroke();

      ctx.fillStyle = "#ec4899";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("Product: 1,4-Pentadiene (Confirms 5-Carbon Chain)", cx, cy + 45);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("+ N(CH3)3 (Trimethylamine gas evolved)", cx, cy + 70);
    }

    requestAnimationFrame(render);
  }

  render();
};

/* ==========================================================================
   SIMULATION 9: Steroid Conformation & Barbier-Wieland Degradation (Unit 9)
   sim_nat_steroid_ring_conformation_diels
   ========================================================================== */
window.sim_nat_steroid_ring_conformation_diels = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">🔬 Steroid Cyclopentanoperhydrophenanthrene (CPP) & Diels' Hydrocarbon</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Fusion:
            <select id="sim9_fusion" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:3px 8px; font-size:0.85rem;">
              <option value="trans">5alpha-Cholestane (A/B trans - Rigid Flat)</option>
              <option value="cis">5beta-Coprostane (A/B cis - Bent 90°)</option>
            </select>
          </label>
          <button id="sim9_dehydrogenate" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:4px 10px; font-size:0.85rem; cursor:pointer;">Selenium Dehydrogenation (Diels)</button>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim9_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span id="sim9_desc">Steroid Skeleton: Rings A, B, C (Phenanthrene) + Ring D (Cyclopentane)</span>
        <span id="sim9_status" style="color:#10b981; font-weight:600;">Standard trans-anti-trans-anti-trans Topology</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim9_canvas");
  const fusionSelect = document.getElementById("sim9_fusion");
  const dehydroBtn = document.getElementById("sim9_dehydrogenate");
  const descSpan = document.getElementById("sim9_desc");
  const statusSpan = document.getElementById("sim9_status");

  let isDiels = false;

  dehydroBtn.onclick = () => {
    isDiels = !isDiels;
    if (isDiels) {
      descSpan.textContent = "Product: Diels' Hydrocarbon (3'-methyl-1,2-cyclopentenophenanthrene, C18H16)";
      statusSpan.textContent = "Se, 360°C -> Aromatized CPP Skeleton";
      statusSpan.style.color = "#f59e0b";
      dehydroBtn.textContent = "Restore Cholesterol Intact";
    } else {
      descSpan.textContent = "Steroid Skeleton: Rings A, B, C (Phenanthrene) + Ring D (Cyclopentane)";
      statusSpan.textContent = "Standard trans-anti-trans-anti-trans Topology";
      statusSpan.style.color = "#10b981";
      dehydroBtn.textContent = "Selenium Dehydrogenation (Diels)";
    }
  };

  fusionSelect.onchange = () => { isDiels = false; };

  function render() {
    const res = setupCanvas(canvas);
    const ctx = res.ctx;
    const width = res.width;
    const height = res.height;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    const cx = width * 0.45;
    const cy = height * 0.55;

    ctx.lineWidth = 3;
    ctx.strokeStyle = isDiels ? "#f59e0b" : "#38bdf8";

    // Draw Steroid ABCD Rings
    // Ring A
    ctx.strokeRect(cx - 150, cy - 25, 60, 50);
    // Ring B
    ctx.strokeRect(cx - 90, cy - 50, 60, 50);
    // Ring C
    ctx.strokeRect(cx - 30, cy - 75, 60, 50);
    // Ring D (Cyclopentane pentagon)
    ctx.beginPath();
    ctx.moveTo(cx + 30, cy - 75);
    ctx.lineTo(cx + 70, cy - 90);
    ctx.lineTo(cx + 90, cy - 55);
    ctx.lineTo(cx + 60, cy - 35);
    ctx.lineTo(cx + 30, cy - 50);
    ctx.closePath();
    ctx.stroke();

    // Ring Labels
    ctx.fillStyle = "#94a3b8";
    ctx.font = "bold 13px 'Inter', sans-serif";
    ctx.fillText("A", cx - 120, cy);
    ctx.fillText("B", cx - 60, cy - 25);
    ctx.fillText("C", cx, cy - 50);
    ctx.fillText("D", cx + 55, cy - 60);

    // Angular Methyl Groups (C10, C13)
    if (!isDiels) {
      ctx.strokeStyle = "#10b981";
      ctx.beginPath();
      // C10 methyl
      ctx.moveTo(cx - 90, cy - 25); ctx.lineTo(cx - 90, cy - 50);
      // C13 methyl
      ctx.moveTo(cx - 30, cy - 50); ctx.lineTo(cx - 30, cy - 75);
      ctx.stroke();

      ctx.fillStyle = "#10b981";
      ctx.font = "10px sans-serif";
      ctx.fillText("C19 Me", cx - 90, cy - 55);
      ctx.fillText("C18 Me", cx - 30, cy - 80);
    } else {
      // Diels' hydrocarbon has methyl at 3' on cyclopentene
      ctx.fillStyle = "#f59e0b";
      ctx.font = "11px sans-serif";
      ctx.fillText("3'-Me", cx + 85, cy - 100);
      // Aromatic rings circles
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)";
      ctx.beginPath(); ctx.arc(cx - 120, cy, 18, 0, Math.PI * 2); ctx.stroke();
      ctx.beginPath(); ctx.arc(cx - 60, cy - 25, 18, 0, Math.PI * 2); ctx.stroke();
      ctx.beginPath(); ctx.arc(cx, cy - 50, 18, 0, Math.PI * 2); ctx.stroke();
    }

    requestAnimationFrame(render);
  }

  render();
};

/* ==========================================================================
   SIMULATION 10: Penicillin Beta-Lactam Transpeptidase Inhibition (Unit 10)
   sim_nat_penicillin_beta_lactam_inhibition
   ========================================================================== */
window.sim_nat_penicillin_beta_lactam_inhibition = function(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = `
    <div style="display:flex; flex-direction:column; width:100%; height:100%; background:#080d19; color:#e2e8f0; font-family:'Inter',sans-serif;">
      <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; padding:10px 16px; background:#0b1329; border-bottom:1px solid #1e293b;">
        <div style="font-weight:700; color:#38bdf8; font-size:0.95rem;">🛡️ Penicillin Strained Beta-Lactam Transpeptidase Suicide Inactivation</div>
        <div style="display:flex; gap:10px; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Enzyme Target:
            <select id="sim10_target" style="background:#1e293b; color:#38bdf8; border:1px solid #334155; border-radius:4px; padding:3px 8px; font-size:0.85rem;">
              <option value="pbp">Bacterial Transpeptidase (PBP - Inhibited)</option>
              <option value="betalactamase">beta-Lactamase Resistance (Hydrolyzed)</option>
              <option value="clavulanate">PBP + Clavulanic Acid (Inhibitor Protected)</option>
            </select>
          </label>
          <button id="sim10_attack" style="background:#0284c7; color:#fff; border:none; border-radius:4px; padding:4px 10px; font-size:0.85rem; cursor:pointer;">Initiate Nucleophilic Attack</button>
        </div>
      </div>
      <div style="flex:1; position:relative; min-height:360px;">
        <canvas id="sim10_canvas" class=\"sim-canvas\" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div style="padding:8px 16px; background:#090e1e; border-top:1px solid #1e293b; font-size:0.82rem; color:#94a3b8; display:flex; justify-content:space-between;">
        <span id="sim10_state">Mechanism: Serine-403 attack on strained 4-membered beta-lactam carbonyl</span>
        <span id="sim10_covalent_status" style="color:#10b981; font-weight:600;">Irreversible Covalent Inactivation</span>
      </div>
    </div>
  `;

  const canvas = document.getElementById("sim10_canvas");
  const targetSelect = document.getElementById("sim10_target");
  const attackBtn = document.getElementById("sim10_attack");
  const stateSpan = document.getElementById("sim10_state");
  const statusSpan = document.getElementById("sim10_covalent_status");

  let isAttacked = false;

  attackBtn.onclick = () => {
    isAttacked = true;
    const tgt = targetSelect.value;
    if (tgt === "pbp") {
      stateSpan.textContent = "Covalent Acyl-Enzyme complex formed! Transpeptidase cross-linking permanently arrested.";
      statusSpan.textContent = "Bactericidal Lysis";
      statusSpan.style.color = "#ef4444";
    } else if (tgt === "betalactamase") {
      stateSpan.textContent = "Beta-lactamase hydrolyzes beta-lactam ring to inactive penicilloic acid. Bacteria survives!";
      statusSpan.textContent = "Resistance Active";
      statusSpan.style.color = "#f59e0b";
    } else {
      stateSpan.textContent = "Clavulanate suicide-inhibits beta-lactamase! Penicillin freely acylates transpeptidase.";
      statusSpan.textContent = "Combination Synergism (Augmentin)";
      statusSpan.style.color = "#10b981";
    }
  };

  targetSelect.onchange = () => {
    isAttacked = false;
    stateSpan.textContent = "Mechanism: Serine-403 attack on strained 4-membered beta-lactam carbonyl";
    statusSpan.textContent = "Awaiting Nucleophile Attack";
    statusSpan.style.color = "#38bdf8";
  };

  function render() {
    const res = setupCanvas(canvas);
    const ctx = res.ctx;
    const width = res.width;
    const height = res.height;

    ctx.fillStyle = "#080d19";
    ctx.fillRect(0, 0, width, height);

    const cx = width * 0.5;
    const cy = height * 0.5;

    // Draw 4-membered Beta-Lactam Ring
    ctx.strokeStyle = isAttacked ? "#ef4444" : "#38bdf8";
    ctx.lineWidth = 4;
    ctx.strokeRect(cx - 80, cy - 40, 60, 60);

    // Fused 5-membered Thiazolidine Ring
    ctx.strokeStyle = "#10b981";
    ctx.beginPath();
    ctx.moveTo(cx - 20, cy - 40);
    ctx.lineTo(cx + 40, cy - 20);
    ctx.lineTo(cx + 40, cy + 20);
    ctx.lineTo(cx - 20, cy + 20);
    ctx.stroke();

    // Carbonyl Oxygen on Beta-Lactam
    ctx.strokeStyle = "#ef4444";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(cx - 50, cy - 40);
    ctx.lineTo(cx - 50, cy - 70);
    ctx.stroke();
    ctx.fillStyle = "#ef4444";
    ctx.beginPath(); ctx.arc(cx - 50, cy - 70, 7, 0, Math.PI * 2); ctx.fill();

    // Labels
    ctx.fillStyle = "#f8fafc";
    ctx.font = "bold 11px sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("Beta-Lactam Ring", cx - 50, cy - 10);
    ctx.fillText("Thiazolidine", cx + 15, cy - 5);

    // Active Site Nucleophile Ser-403
    const serX = isAttacked ? cx - 50 : cx - 140;
    const serY = cy - 40;

    ctx.fillStyle = "#f59e0b";
    ctx.beginPath(); ctx.arc(serX, serY, 12, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "#000"; ctx.font = "bold 9px sans-serif"; ctx.fillText("Ser-OH", serX, serY + 3);

    if (isAttacked) {
      ctx.fillStyle = "#ef4444";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.fillText("Covalent Ester Bond Formed (Permanent Acylation)", cx, cy + 65);
    }

    requestAnimationFrame(render);
  }

  render();
};

/* ==========================================================================
   Global Simulation Engine Registry Adapter
   ========================================================================== */
window.SimulationEngine.initSimulation = function(containerId, simType) {
  if (typeof window[simType] === 'function') {
    window[simType](containerId);
  } else {
    console.warn("Simulation function not found:", simType);
  }
};
"""

with open("natural-products-chemistry-sims.js", "w", encoding="utf-8") as f:
    f.write(sims_code)

print("Generated natural-products-chemistry-sims.js successfully!")
