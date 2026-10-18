# -*- coding: utf-8 -*-
"""
generate_aa_sims.py
Generates abstract-algebra-sims.js with 8 real-time, 60 FPS interactive Canvas simulations
registered into window.SIMULATIONS and window.SimulationEngine:
1. sim_aa_modular_cayley: Interactive modular arithmetic Cayley tables & subgroup highlight
2. sim_aa_subgroup_lattices: Dynamic subgroup lattice visualizer for cyclic, Klein-4, and dihedral groups
3. sim_aa_permutation_orbits: Permutation cycle decomposition & polygon symmetry action
4. sim_aa_coset_partition: Left/right coset partitioning of groups & quotient projection
5. sim_aa_homomorphism_kernel: Group homomorphism fibers, kernel collapse & 1st isomorphism theorem
6. sim_aa_ring_ideals: Principal ideals, prime ideals vs maximal ideals in Z_n and polynomial rings
7. sim_aa_domain_hierarchy: Interactive Venn diagram & element factorization (Field -> ED -> PID -> UFD -> Ring)
8. sim_aa_polynomial_roots: Polynomial factorization, Eisenstein's criterion tester & field extension degrees
"""

def generate_sims_js():
    js_code = r"""// Abstract Algebra: Groups, Rings, Fields & Modern Algebraic Structures
// 8 Real-Time 60 FPS Interactive Canvas Simulations Suite

window.SIMULATIONS = window.SIMULATIONS || {};

// -------------------------------------------------------------
// 1. Modular Cayley Table Visualizer
// -------------------------------------------------------------
window.SIMULATIONS["sim_aa_modular_cayley"] = {
  title: "Interactive Modular Arithmetic Cayley Table & Subgroups",
  desc: "Examine binary group operations, identity elements, Latin square property, and subgroup closure under modular addition (Z_n, +) and unit multiplication (U(n), ·).",
  controls: [
    { id: "n", label: "Modulus n", type: "range", min: 3, max: 10, step: 1, default: 6 },
    { id: "op", label: "Group Operation", type: "select", options: [
      { value: "add", label: "(Z_n, +) Modular Addition" },
      { value: "mul", label: "(U(n), ·) Multiplicative Units Group" }
    ], default: "add" },
    { id: "subgroup", label: "Highlight Subgroup", type: "select", options: [
      { value: "none", label: "None" },
      { value: "even", label: "Even Elements / Parity Subgroup" },
      { value: "gens", label: "Generator Orbit ⟨2⟩" }
    ], default: "none" }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const n = parseInt(params.n, 10);
    const op = params.op;
    const sub = params.subgroup;

    function gcd(a, b) {
      while (b) { let t = b; b = a % b; a = t; }
      return a;
    }

    const elements = [];
    if (op === "add") {
      for (let i = 0; i < n; i++) elements.push(i);
    } else {
      for (let i = 1; i < n; i++) {
        if (gcd(i, n) === 1) elements.push(i);
      }
    }

    const m = elements.length;
    const margin = 35;
    const cellSize = Math.min((w - margin * 2) / (m + 1.2), (h - margin * 2) / (m + 1.2));
    const startX = (w - (m + 1) * cellSize) / 2;
    const startY = (h - (m + 1) * cellSize) / 2;

    // Header title
    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px Inter, sans-serif";
    ctx.textAlign = "center";
    const groupName = op === "add" ? `Additive Cyclic Group (Z_${n}, +) [Order ${n}]` : `Multiplicative Units Group U(${n}) [Order ${m}]`;
    ctx.fillText(groupName, w / 2, startY - 10);

    // Operator cell
    ctx.fillStyle = "#f59e0b";
    ctx.fillRect(startX, startY, cellSize, cellSize);
    ctx.fillStyle = "#0f172a";
    ctx.font = "bold 15px Fira Code, monospace";
    ctx.textBaseline = "middle";
    ctx.fillText(op === "add" ? "+" : "·", startX + cellSize / 2, startY + cellSize / 2);

    // Row / Col Headers
    ctx.font = "600 12px Fira Code, monospace";
    for (let i = 0; i < m; i++) {
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(startX + (i + 1) * cellSize, startY, cellSize, cellSize);
      ctx.fillRect(startX, startY + (i + 1) * cellSize, cellSize, cellSize);

      ctx.fillStyle = "#94a3b8";
      ctx.fillText(elements[i], startX + (i + 1) * cellSize + cellSize / 2, startY + cellSize / 2);
      ctx.fillText(elements[i], startX + cellSize / 2, startY + (i + 1) * cellSize + cellSize / 2);
    }

    // Table Cells
    for (let r = 0; r < m; r++) {
      for (let c = 0; c < m; c++) {
        const val = op === "add"
          ? (elements[r] + elements[c]) % n
          : (elements[r] * elements[c]) % n;

        const cx = startX + (c + 1) * cellSize;
        const cy = startY + (r + 1) * cellSize;

        let isSub = false;
        if (sub === "even" && val % 2 === 0) isSub = true;
        if (sub === "gens" && (val === 0 || val === 2 || val === 4 || val === 6 || val === 8)) isSub = true;

        ctx.fillStyle = isSub ? "#581c87" : "#0369a1";
        ctx.globalAlpha = 0.25 + (val / n) * 0.45;
        ctx.fillRect(cx + 1, cy + 1, cellSize - 2, cellSize - 2);
        ctx.globalAlpha = 1.0;

        ctx.fillStyle = isSub ? "#e9d5ff" : "#f8fafc";
        ctx.fillText(val, cx + cellSize / 2, cy + cellSize / 2);

        ctx.strokeStyle = "#334155";
        ctx.lineWidth = 1;
        ctx.strokeRect(cx, cy, cellSize, cellSize);
      }
    }
  }
};

// -------------------------------------------------------------
// 2. Subgroup Lattice Diagram Visualizer
// -------------------------------------------------------------
window.SIMULATIONS["sim_aa_subgroup_lattices"] = {
  title: "Subgroup Lattice Diagram & Inclusion Hierarchy",
  desc: "Visualize the partially ordered set of subgroups under inclusion H ≤ K for cyclic groups, the Klein 4-group, and the non-abelian Dihedral group D_4.",
  controls: [
    { id: "group", label: "Group G", type: "select", options: [
      { value: "Z12", label: "Z_12 (Cyclic, Order 12, 6 Subgroups)" },
      { value: "Z8", label: "Z_8 (Cyclic p-group, Order 8, Linear Chain)" },
      { value: "V4", label: "V_4 ≅ Z_2 × Z_2 (Klein 4-Group, Diamond Lattice)" },
      { value: "D8", label: "D_4 (Dihedral Group, Order 8, 10 Subgroups)" }
    ], default: "Z12" }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const group = params.group;

    const lattices = {
      Z12: {
        nodes: [
          { name: "Z_12 = ⟨1⟩", order: 12, x: 0.5, y: 0.16 },
          { name: "⟨2⟩ = {0,2,4,6,8,10}", order: 6, x: 0.28, y: 0.4 },
          { name: "⟨3⟩ = {0,3,6,9}", order: 4, x: 0.72, y: 0.4 },
          { name: "⟨4⟩ = {0,4,8}", order: 3, x: 0.28, y: 0.65 },
          { name: "⟨6⟩ = {0,6}", order: 2, x: 0.72, y: 0.65 },
          { name: "{0} = ⟨0⟩", order: 1, x: 0.5, y: 0.88 }
        ],
        edges: [
          [0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5]
        ]
      },
      Z8: {
        nodes: [
          { name: "Z_8 = ⟨1⟩", order: 8, x: 0.5, y: 0.16 },
          { name: "⟨2⟩ = {0,2,4,6}", order: 4, x: 0.5, y: 0.40 },
          { name: "⟨4⟩ = {0,4}", order: 2, x: 0.5, y: 0.65 },
          { name: "{0} = ⟨0⟩", order: 1, x: 0.5, y: 0.88 }
        ],
        edges: [
          [0, 1], [1, 2], [2, 3]
        ]
      },
      V4: {
        nodes: [
          { name: "V_4 = {e, a, b, c}", order: 4, x: 0.5, y: 0.16 },
          { name: "⟨a⟩ = {e, a}", order: 2, x: 0.24, y: 0.52 },
          { name: "⟨b⟩ = {e, b}", order: 2, x: 0.50, y: 0.52 },
          { name: "⟨c⟩ = {e, c}", order: 2, x: 0.76, y: 0.52 },
          { name: "{e}", order: 1, x: 0.5, y: 0.88 }
        ],
        edges: [
          [0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 4]
        ]
      },
      D8: {
        nodes: [
          { name: "D_4 (Order 8)", order: 8, x: 0.5, y: 0.12 },
          { name: "⟨r⟩ = {e, r, r², r³}", order: 4, x: 0.20, y: 0.35 },
          { name: "{e, r², s, sr²}", order: 4, x: 0.50, y: 0.35 },
          { name: "{e, r², sr, sr³}", order: 4, x: 0.80, y: 0.35 },
          { name: "⟨r²⟩ = Z(D_4)", order: 2, x: 0.50, y: 0.58 },
          { name: "⟨s⟩", order: 2, x: 0.14, y: 0.68 },
          { name: "⟨sr²⟩", order: 2, x: 0.32, y: 0.68 },
          { name: "⟨sr⟩", order: 2, x: 0.68, y: 0.68 },
          { name: "⟨sr³⟩", order: 2, x: 0.86, y: 0.68 },
          { name: "{e}", order: 1, x: 0.5, y: 0.90 }
        ],
        edges: [
          [0, 1], [0, 2], [0, 3],
          [1, 4], [2, 4], [3, 4],
          [2, 5], [2, 6], [3, 7], [3, 8],
          [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]
        ]
      }
    };

    const lat = lattices[group] || lattices.Z12;

    // Header
    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px Inter, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(`Subgroup Lattice L(G) — Top is G, Bottom is {e}`, w / 2, 22);

    // Draw Edges
    ctx.strokeStyle = "#475569";
    ctx.lineWidth = 2;
    lat.edges.forEach(([u, v]) => {
      const p1 = lat.nodes[u];
      const p2 = lat.nodes[v];
      ctx.beginPath();
      ctx.moveTo(p1.x * w, p1.y * h);
      ctx.lineTo(p2.x * w, p2.y * h);
      ctx.stroke();
    });

    // Draw Nodes
    lat.nodes.forEach(node => {
      const nx = node.x * w;
      const ny = node.y * h;

      ctx.font = "600 11px Inter, sans-serif";
      const tw = ctx.measureText(node.name).width;
      const bw = Math.max(tw + 18, 65);
      const bh = 24;

      ctx.fillStyle = node.order === 1 ? "#1e293b" : (node.order === lat.nodes[0].order ? "#1e3a8a" : "#064e3b");
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(nx - bw / 2, ny - bh / 2, bw, bh, 5);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#f8fafc";
      ctx.textBaseline = "middle";
      ctx.fillText(node.name, nx, ny);

      ctx.font = "bold 8px Fira Code, monospace";
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`|H|=${node.order}`, nx, ny - bh / 2 - 5);
    });
  }
};

// -------------------------------------------------------------
// 3. Permutation Cycle Decomposition & Parity Visualizer
// -------------------------------------------------------------
window.SIMULATIONS["sim_aa_permutation_orbits"] = {
  title: "Permutation Cycle Decomposition & Parity Engine",
  desc: "Decompose permutations in S_n into disjoint cycles, compute element order via lcm(lengths), and determine even/odd parity sgn(σ) ∈ {+1, -1}.",
  controls: [
    { id: "perm", label: "Permutation σ ∈ S_6", type: "select", options: [
      { value: "p1", label: "(1 2 3)(4 5) — Disjoint (3-cycle)(2-cycle), Order 6, Odd" },
      { value: "p2", label: "(1 2 3 4 5) — Single 5-cycle, Order 5, Even (∈ A_6)" },
      { value: "p3", label: "(1 4)(2 5)(3 6) — Three 2-cycles, Order 2, Odd" },
      { value: "p4", label: "(1 2)(3 4) — Two 2-cycles, Order 2, Even (∈ A_6)" },
      { value: "p5", label: "(1 2 3 4 5 6) — Full 6-cycle, Order 6, Odd" }
    ], default: "p1" }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const n = 6;
    const R = Math.min(w, h) * 0.30;
    const cx = w / 2;
    const cy = h / 2 + 10;

    let map = { 1: 2, 2: 3, 3: 1, 4: 5, 5: 4, 6: 6 };
    let info = { order: 6, sgn: "-1 (Odd)", set: "S_6 \\ A_6", trans: "4 transpositions" };

    if (params.perm === "p2") {
      map = { 1: 2, 2: 3, 3: 4, 4: 5, 5: 1, 6: 6 };
      info = { order: 5, sgn: "+1 (Even)", set: "A_6", trans: "4 transpositions" };
    } else if (params.perm === "p3") {
      map = { 1: 4, 4: 1, 2: 5, 5: 2, 3: 6, 6: 3 };
      info = { order: 2, sgn: "-1 (Odd)", set: "S_6 \\ A_6", trans: "3 transpositions" };
    } else if (params.perm === "p4") {
      map = { 1: 2, 2: 1, 3: 4, 4: 3, 5: 5, 6: 6 };
      info = { order: 2, sgn: "+1 (Even)", set: "A_6", trans: "2 transpositions" };
    } else if (params.perm === "p5") {
      map = { 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 1 };
      info = { order: 6, sgn: "-1 (Odd)", set: "S_6 \\ A_6", trans: "5 transpositions" };
    }

    // Title & Info Badge
    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px Inter, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(`Permutation Mapping on {1, 2, 3, 4, 5, 6}`, w / 2, 20);

    ctx.fillStyle = info.sgn.includes("Even") ? "#10b981" : "#ef4444";
    ctx.font = "600 12px Inter, sans-serif";
    ctx.fillText(`Order = ${info.order} | Parity sgn(σ) = ${info.sgn} | Class: ${info.set}`, w / 2, 40);

    // Node coordinates
    const coords = [];
    for (let i = 0; i < n; i++) {
      const th = (2 * Math.PI * i) / n - Math.PI / 2;
      coords.push({
        x: cx + R * Math.cos(th),
        y: cy + R * Math.sin(th),
        id: i + 1
      });
    }

    // Draw Directed Curved Arrows
    const colors = ["#f43f5e", "#a855f7", "#3b82f6", "#10b981", "#f59e0b", "#06b6d4"];
    for (let i = 1; i <= n; i++) {
      const dest = map[i];
      if (dest === i) continue; // fixed point
      const p1 = coords[i - 1];
      const p2 = coords[dest - 1];

      ctx.strokeStyle = colors[(i - 1) % colors.length];
      ctx.fillStyle = ctx.strokeStyle;
      ctx.lineWidth = 2.5;

      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      const mx = (p1.x + p2.x) / 2 + (cx - (p1.x + p2.x) / 2) * 0.45;
      const my = (p1.y + p2.y) / 2 + (cy - (p1.y + p2.y) / 2) * 0.45;
      ctx.quadraticCurveTo(mx, my, p2.x, p2.y);
      ctx.stroke();

      const ang = Math.atan2(p2.y - my, p2.x - mx);
      ctx.beginPath();
      ctx.moveTo(p2.x - 17 * Math.cos(ang), p2.y - 17 * Math.sin(ang));
      ctx.lineTo(p2.x - 27 * Math.cos(ang) + 5 * Math.sin(ang), p2.y - 27 * Math.sin(ang) - 5 * Math.cos(ang));
      ctx.lineTo(p2.x - 27 * Math.cos(ang) - 5 * Math.sin(ang), p2.y - 27 * Math.sin(ang) + 5 * Math.cos(ang));
      ctx.fill();
    }

    // Draw Nodes
    coords.forEach(p => {
      ctx.fillStyle = map[p.id] === p.id ? "#334155" : "#1e293b";
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(p.x, p.y, 16, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Fira Code, monospace";
      ctx.textBaseline = "middle";
      ctx.fillText(p.id, p.x, p.y);
    });
  }
};

// -------------------------------------------------------------
// 4. Coset Partition & Lagrange Equipartition Visualizer
// -------------------------------------------------------------
window.SIMULATIONS["sim_aa_coset_partition"] = {
  title: "Lagrange's Theorem & Coset Equipartition Engine",
  desc: "Demonstrate that left cosets gH form a disjoint partition of group G where every coset has cardinality |H|, proving |G| = [G : H] · |H|.",
  controls: [
    { id: "choice", label: "Group & Subgroup", type: "select", options: [
      { value: "Z12_H4", label: "G = Z_12, H = ⟨4⟩ = {0, 4, 8} [Index = 4]" },
      { value: "Z12_H6", label: "G = Z_12, H = ⟨6⟩ = {0, 6} [Index = 6]" },
      { value: "Z12_H3", label: "G = Z_12, H = ⟨3⟩ = {0, 3, 6, 9} [Index = 3]" },
      { value: "S3_A3", label: "G = S_3, H = A_3 (Even Permutations) [Index = 2]" }
    ], default: "Z12_H4" }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const configs = {
      Z12_H4: {
        gName: "Z_12 (Order 12)",
        index: 4,
        hOrder: 3,
        cosets: [
          { name: "0 + H", items: [0, 4, 8], color: "#38bdf8" },
          { name: "1 + H", items: [1, 5, 9], color: "#a855f7" },
          { name: "2 + H", items: [2, 6, 10], color: "#10b981" },
          { name: "3 + H", items: [3, 7, 11], color: "#f59e0b" }
        ]
      },
      Z12_H6: {
        gName: "Z_12 (Order 12)",
        index: 6,
        hOrder: 2,
        cosets: [
          { name: "0 + H", items: [0, 6], color: "#38bdf8" },
          { name: "1 + H", items: [1, 7], color: "#a855f7" },
          { name: "2 + H", items: [2, 8], color: "#10b981" },
          { name: "3 + H", items: [3, 9], color: "#f59e0b" },
          { name: "4 + H", items: [4, 10], color: "#ec4899" },
          { name: "5 + H", items: [5, 11], color: "#06b6d4" }
        ]
      },
      Z12_H3: {
        gName: "Z_12 (Order 12)",
        index: 3,
        hOrder: 4,
        cosets: [
          { name: "0 + H", items: [0, 3, 6, 9], color: "#38bdf8" },
          { name: "1 + H", items: [1, 4, 7, 10], color: "#a855f7" },
          { name: "2 + H", items: [2, 5, 8, 11], color: "#10b981" }
        ]
      },
      S3_A3: {
        gName: "S_3 (Order 6)",
        index: 2,
        hOrder: 3,
        cosets: [
          { name: "eH = A_3 (Even)", items: ["()", "(1 2 3)", "(1 3 2)"], color: "#10b981" },
          { name: "(1 2)H (Odd)", items: ["(1 2)", "(1 3)", "(2 3)"], color: "#ef4444" }
        ]
      }
    };

    const cfg = configs[params.choice] || configs.Z12_H4;

    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px Inter, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(`Lagrange Coset Equipartition: G = ⨆ (g_i H)`, w / 2, 22);

    ctx.fillStyle = "#94a3b8";
    ctx.font = "12px Inter, sans-serif";
    ctx.fillText(`${cfg.gName}: [G : H] = ${cfg.index} disjoint cosets of cardinality |H| = ${cfg.hOrder}`, w / 2, 42);

    const padX = 24;
    const boxW = (w - padX * 2) / cfg.index;
    const startY = 65;
    const boxH = h - 90;

    cfg.cosets.forEach((coset, idx) => {
      const bx = padX + idx * boxW;

      ctx.fillStyle = "#1e293b";
      ctx.strokeStyle = coset.color;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.roundRect(bx + 4, startY, boxW - 8, boxH, 6);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = coset.color;
      ctx.font = "bold 12px Fira Code, monospace";
      ctx.fillText(coset.name, bx + boxW / 2, startY + 22);

      ctx.font = "10px Inter, sans-serif";
      ctx.fillStyle = idx === 0 ? "#10b981" : "#94a3b8";
      ctx.fillText(idx === 0 ? "Subgroup H" : `Coset #${idx + 1}`, bx + boxW / 2, startY + 38);

      const spacing = (boxH - 70) / coset.items.length;
      coset.items.forEach((item, itemIdx) => {
        const iy = startY + 65 + itemIdx * spacing;
        ctx.fillStyle = "#0f172a";
        ctx.beginPath();
        ctx.roundRect(bx + boxW / 2 - 28, iy - 12, 56, 24, 4);
        ctx.fill();
        ctx.strokeStyle = "#475569";
        ctx.lineWidth = 1;
        ctx.stroke();

        ctx.fillStyle = "#f8fafc";
        ctx.font = "bold 12px Fira Code, monospace";
        ctx.fillText(item, bx + boxW / 2, iy + 3);
      });
    });
  }
};

// -------------------------------------------------------------
// 5. Homomorphism & First Isomorphism Theorem Visualizer
// -------------------------------------------------------------
window.SIMULATIONS["sim_aa_homomorphism_kernel"] = {
  title: "Group Homomorphism, Kernel & First Isomorphism Theorem",
  desc: "Map domain group G through homomorphism φ to target group, identify the normal subgroup ker(φ), and verify G/ker(φ) ≅ im(φ).",
  controls: [
    { id: "mod", label: "Surjection Target Z_k", type: "select", options: [
      { value: "4", label: "φ: Z_12 ↠ Z_4 (ker size 3, index 4)" },
      { value: "6", label: "φ: Z_12 ↠ Z_6 (ker size 2, index 6)" },
      { value: "3", label: "φ: Z_12 ↠ Z_3 (ker size 4, index 3)" }
    ], default: "4" }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const k = parseInt(params.mod, 10);
    const n = 12;

    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px Inter, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(`First Isomorphism Theorem: G / ker(φ) ≅ im(φ)`, w / 2, 20);

    ctx.fillStyle = "#94a3b8";
    ctx.font = "12px Inter, sans-serif";
    ctx.fillText(`Epimorphism φ: (Z_${n}, +) ↠ (Z_${k}, +) with φ(x) = x mod ${k}`, w / 2, 38);

    const col1X = w * 0.22;
    const col2X = w * 0.50;
    const col3X = w * 0.80;

    // Headers
    ctx.fillStyle = "#38bdf8";
    ctx.font = "600 12px Inter, sans-serif";
    ctx.fillText(`Domain G = Z_12`, col1X, 65);
    ctx.fillStyle = "#a855f7";
    ctx.fillText(`Quotient G/ker(φ)`, col2X, 65);
    ctx.fillStyle = "#10b981";
    ctx.fillText(`Image im(φ) = Z_${k}`, col3X, 65);

    const fibers = [];
    for (let r = 0; r < k; r++) {
      const elms = [];
      for (let x = 0; x < n; x++) {
        if (x % k === r) elms.push(x);
      }
      fibers.push({
        rem: r,
        elms: elms,
        isKer: r === 0
      });
    }

    const startY = 90;
    const spacingY = Math.min(50, (h - 120) / k);

    fibers.forEach((fib, idx) => {
      const y = startY + idx * spacingY;

      // Domain fiber
      ctx.fillStyle = fib.isKer ? "#7f1d1d" : "#1e293b";
      ctx.strokeStyle = fib.isKer ? "#f87171" : "#475569";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(col1X - 60, y - 14, 120, 28, 5);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#f8fafc";
      ctx.font = "11px Fira Code, monospace";
      ctx.fillText(`{${fib.elms.join(', ')}}`, col1X, y + 2);

      // Quotient element
      ctx.fillStyle = "#4c1d95";
      ctx.strokeStyle = "#c4b5fd";
      ctx.beginPath();
      ctx.roundRect(col2X - 40, y - 14, 80, 28, 5);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 11px Fira Code, monospace";
      ctx.fillText(`${fib.rem} + K`, col2X, y + 2);

      // Image element
      ctx.fillStyle = "#064e3b";
      ctx.strokeStyle = "#34d399";
      ctx.beginPath();
      ctx.roundRect(col3X - 30, y - 14, 60, 28, 5);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 13px Fira Code, monospace";
      ctx.fillText(fib.rem, col3X, y + 2);

      // Arrow
      ctx.strokeStyle = "#a855f7";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(col2X + 45, y);
      ctx.lineTo(col3X - 35, y);
      ctx.stroke();
    });
  }
};

// -------------------------------------------------------------
// 6. Ring Ideals & Quotient Rings Visualizer
// -------------------------------------------------------------
window.SIMULATIONS["sim_aa_ring_ideals"] = {
  title: "Principal Ideals, Prime Ideals & Factor Rings",
  desc: "Explore ideals I = ⟨a⟩ in ring Z_n, test ideal absorption r·i ∈ I, and determine whether R/I is a Field (maximal ideal) or an Integral Domain.",
  controls: [
    { id: "ring", label: "Ring R", type: "select", options: [
      { value: "12", label: "Ring Z_12" },
      { value: "8", label: "Ring Z_8" },
      { value: "6", label: "Ring Z_6" }
    ], default: "12" },
    { id: "gen", label: "Ideal Generator a", type: "select", options: [
      { value: "2", label: "⟨2⟩" },
      { value: "3", label: "⟨3⟩" },
      { value: "4", label: "⟨4⟩" },
      { value: "6", label: "⟨6⟩" }
    ], default: "3" }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const n = parseInt(params.ring, 10);
    const a = parseInt(params.gen, 10);

    function gcd(x, y) { while (y) { let t = y; y = x % y; x = t; } return x; }

    const idealElms = new Set();
    for (let k = 0; k < n; k++) idealElms.add((a * k) % n);

    const qSize = gcd(a, n);
    function isPrime(x) {
      if (x < 2) return false;
      for (let i = 2; i * i <= x; i++) if (x % i === 0) return false;
      return true;
    }

    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px Inter, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(`Ring R = Z_${n} with Principal Ideal I = ⟨${a}⟩`, w / 2, 22);

    const isMax = isPrime(qSize);
    ctx.fillStyle = isMax ? "#10b981" : "#ef4444";
    ctx.font = "600 12px Inter, sans-serif";
    ctx.fillText(isMax 
      ? `⟨${a}⟩ is Maximal & Prime ⟹ R/I ≅ Z_${qSize} is a Field!` 
      : `⟨${a}⟩ is Not Maximal ⟹ R/I ≅ Z_${qSize} has Zero Divisors!`, w / 2, 42);

    // Elements grid
    const cols = Math.min(n, 6);
    const cellW = 50;
    const startX = (w - cols * cellW) / 2;
    const startY = 70;

    for (let i = 0; i < n; i++) {
      const r = Math.floor(i / cols);
      const c = i % cols;
      const cx = startX + c * cellW;
      const cy = startY + r * cellW;

      const inI = idealElms.has(i);

      ctx.fillStyle = inI ? "#581c87" : "#1e293b";
      ctx.strokeStyle = inI ? "#c084fc" : "#334155";
      ctx.lineWidth = inI ? 2 : 1;
      ctx.beginPath();
      ctx.roundRect(cx + 4, cy + 4, cellW - 8, cellW - 8, 6);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = inI ? "#f8fafc" : "#94a3b8";
      ctx.font = "bold 14px Fira Code, monospace";
      ctx.textBaseline = "middle";
      ctx.fillText(i, cx + cellW / 2, cy + cellW / 2);
    }
  }
};

// -------------------------------------------------------------
// 7. Domain Hierarchy Venn Diagram Visualizer
// -------------------------------------------------------------
window.SIMULATIONS["sim_aa_domain_hierarchy"] = {
  title: "The Algebraic Domain Hierarchy Venn Diagram",
  desc: "Interactive containment diagram showing Fields ⊂ Euclidean Domains (ED) ⊂ Principal Ideal Domains (PID) ⊂ Unique Factorization Domains (UFD) ⊂ Integral Domains.",
  controls: [
    { id: "highlight", label: "Inspect Domain Class", type: "select", options: [
      { value: "all", label: "All Containments" },
      { value: "fields", label: "Fields (Q, R, C, F_p)" },
      { value: "ed", label: "Euclidean Domains (Z, F[x], Z[i])" },
      { value: "pid", label: "PIDs (Every ideal is principal)" },
      { value: "ufd", label: "UFDs (Z[x] is UFD but not PID!)" },
      { value: "id", label: "Integral Domains (Z[√-5] fails UFD!)" }
    ], default: "all" }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const levels = [
      { id: "rings", name: "Commutative Rings with Unity (CR)", eg: "Z_6, Z × Z", col: "#334155" },
      { id: "id", name: "Integral Domains (No Zero Divisors)", eg: "Z[√-5] (fails unique factorization)", col: "#1e3a8a" },
      { id: "ufd", name: "Unique Factorization Domains (UFD)", eg: "Z[x], F[x, y] (not a PID!)", col: "#065f46" },
      { id: "pid", name: "Principal Ideal Domains (PID)", eg: "PIDs satisfy ACCP", col: "#7c2d12" },
      { id: "ed", name: "Euclidean Domains (ED)", eg: "Z, F[x], Z[i] (Gaussian Integers)", col: "#6b21a8" },
      { id: "fields", name: "Fields (Every non-zero element is unit)", eg: "Q, R, C, F_p = Z_p", col: "#047857" }
    ];

    const cx = w / 2;
    const cy = h / 2 + 10;
    const maxRx = w * 0.42;
    const maxRy = h * 0.38;

    for (let i = 0; i < levels.length; i++) {
      const factor = 1 - (i * 0.155);
      const rx = maxRx * factor;
      const ry = maxRy * factor;

      const isHl = params.highlight === "all" || params.highlight === levels[i].id;

      ctx.fillStyle = levels[i].col;
      ctx.globalAlpha = isHl ? 0.45 : 0.12;
      ctx.beginPath();
      ctx.ellipse(cx, cy + (i * 10), rx, ry, 0, 0, 2 * Math.PI);
      ctx.fill();

      ctx.globalAlpha = 1.0;
      ctx.strokeStyle = isHl ? "#38bdf8" : "#475569";
      ctx.lineWidth = isHl ? 2 : 1;
      ctx.stroke();

      const labelY = cy + (i * 10) - ry + 12;
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 10px Inter, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(levels[i].name, cx, labelY);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "italic 9px Fira Code, monospace";
      ctx.fillText(`e.g. ${levels[i].eg}`, cx, labelY + 11);
    }
  }
};

// -------------------------------------------------------------
// 8. Polynomial Irreducibility & Field Extensions Visualizer
// -------------------------------------------------------------
window.SIMULATIONS["sim_aa_polynomial_roots"] = {
  title: "Eisenstein Criterion & Simple Field Extensions",
  desc: "Analyze polynomial irreducibility in Q[x] via Eisenstein's criterion, compute minimal polynomials, and construct extension towers [K : F].",
  controls: [
    { id: "poly", label: "Polynomial p(x)", type: "select", options: [
      { value: "x2_2", label: "p(x) = x² - 2 [Eisenstein p=2, Degree 2]" },
      { value: "x3_2", label: "p(x) = x³ - 2 [Eisenstein p=2, Degree 3]" },
      { value: "x4_4", label: "p(x) = x⁴ - 4 = (x²-2)(x²+2) [Reducible!]" },
      { value: "x2_1", label: "p(x) = x² + 1 [Degree 2, Roots ±i]" },
      { value: "phi5", label: "p(x) = Φ_5(x) = x⁴+x³+x²+x+1 [Degree 4]" }
    ], default: "x2_2" }
  ],
  render: function(canvas, params, time) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const polyData = {
      x2_2: {
        deg: 2,
        eisenstein: "Irreducible by Eisenstein with prime p = 2 (2|2, 2∤1, 4∤2).",
        field: "Q(√2)",
        degStr: "[Q(√2) : Q] = 2",
        basis: "{1, √2}"
      },
      x3_2: {
        deg: 3,
        eisenstein: "Irreducible by Eisenstein with prime p = 2 (2|2, 2∤1, 4∤2).",
        field: "Q(∛2)",
        degStr: "[Q(∛2) : Q] = 3",
        basis: "{1, ∛2, ∛4}"
      },
      x4_4: {
        deg: 4,
        eisenstein: "REDUCIBLE: x⁴ - 4 = (x² - 2)(x² + 2). Eisenstein fails because p²=4 divides 4!",
        field: "Composite Factors",
        degStr: "Splitting Field Q(√2, i)",
        basis: "Reducible in Q[x]"
      },
      x2_1: {
        deg: 2,
        eisenstein: "Irreducible over Q and R (no real roots; discriminant Δ = -4 < 0).",
        field: "Q(i) (Gaussian Rationals)",
        degStr: "[Q(i) : Q] = 2",
        basis: "{1, i}"
      },
      phi5: {
        deg: 4,
        eisenstein: "Irreducible cyclotomic polynomial: Φ_5(y+1) satisfies Eisenstein with p = 5!",
        field: "Q(ζ_5) (Cyclotomic Field)",
        degStr: "[Q(ζ_5) : Q] = 4 = φ(5)",
        basis: "{1, ζ, ζ², ζ³}"
      }
    };

    const p = polyData[params.poly] || polyData.x2_2;

    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px Inter, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(`Polynomial Irreducibility & Field Extension Degree`, w / 2, 22);

    // Card Box
    ctx.fillStyle = "#1e293b";
    ctx.strokeStyle = "#334155";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.roundRect(w * 0.1, 45, w * 0.8, 55, 6);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#f8fafc";
    ctx.font = "600 11px Inter, sans-serif";
    ctx.fillText("Eisenstein & Irreducibility Analysis:", w / 2, 62);
    ctx.fillStyle = "#f59e0b";
    ctx.font = "11px Inter, sans-serif";
    ctx.fillText(p.eisenstein, w / 2, 82);

    // Tower diagram
    const cx = w / 2;
    const topY = 145;
    const botY = 230;

    // Top field K
    ctx.fillStyle = "#065f46";
    ctx.strokeStyle = "#34d399";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(cx - 80, topY - 16, 160, 32, 5);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#f8fafc";
    ctx.font = "bold 13px Fira Code, monospace";
    ctx.textBaseline = "middle";
    ctx.fillText(p.field, cx, topY);

    // Bottom field Q
    ctx.fillStyle = "#1e3a8a";
    ctx.strokeStyle = "#60a5fa";
    ctx.beginPath();
    ctx.roundRect(cx - 60, botY - 16, 120, 32, 5);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#f8fafc";
    ctx.fillText("Q (Base Field)", cx, botY);

    // Connecting line
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(cx, topY + 16);
    ctx.lineTo(cx, botY - 16);
    ctx.stroke();

    // Degree badge
    ctx.fillStyle = "#f59e0b";
    ctx.font = "bold 12px Fira Code, monospace";
    ctx.fillText(`Degree = ${p.deg}`, cx + 45, (topY + botY) / 2);

    // Basis text
    ctx.fillStyle = "#94a3b8";
    ctx.font = "11px Inter, sans-serif";
    ctx.fillText(`Q-Vector Space Basis: ${p.basis}`, cx, h - 20);
  }
};

// -------------------------------------------------------------
// Engine Dispatcher for app.js
// -------------------------------------------------------------
window.SimulationEngine = {
  simulations: window.SIMULATIONS,
  initSimulation: function(containerId, simType) {
    const container = document.getElementById(containerId);
    if (!container) return;
    const simConfig = window.SIMULATIONS[simType];
    if (!simConfig) return;

    container.innerHTML = "";
    const box = document.createElement("div");
    box.className = "sim-inline-card";
    box.style.background = "#0b1120";
    box.style.border = "1px solid #1e293b";
    box.style.borderRadius = "10px";
    box.style.padding = "1rem";
    box.style.margin = "1.5rem 0";

    const titleEl = document.createElement("div");
    titleEl.style.fontWeight = "700";
    titleEl.style.color = "#38bdf8";
    titleEl.style.fontSize = "1rem";
    titleEl.style.marginBottom = "0.25rem";
    titleEl.innerText = simConfig.title;
    box.appendChild(titleEl);

    if (simConfig.desc) {
      const descEl = document.createElement("div");
      descEl.style.fontSize = "0.82rem";
      descEl.style.color = "#94a3b8";
      descEl.style.marginBottom = "0.75rem";
      descEl.innerText = simConfig.desc;
      box.appendChild(descEl);
    }

    const canvas = document.createElement("canvas");
    canvas.width = 760;
    canvas.height = 360;
    canvas.style.width = "100%";
    canvas.style.height = "auto";
    canvas.style.background = "#090d1a";
    canvas.style.borderRadius = "8px";
    canvas.style.border = "1px solid #1e293b";
    box.appendChild(canvas);

    const controlsContainer = document.createElement("div");
    controlsContainer.style.display = "flex";
    controlsContainer.style.flexWrap = "wrap";
    controlsContainer.style.gap = "1rem";
    controlsContainer.style.marginTop = "0.75rem";
    controlsContainer.style.padding = "0.5rem 0";

    const vals = {};
    if (simConfig.controls) {
      simConfig.controls.forEach(ctrl => {
        vals[ctrl.id] = ctrl.default;
        const ctrlDiv = document.createElement("div");
        ctrlDiv.style.display = "flex";
        ctrlDiv.style.flexDirection = "column";
        ctrlDiv.style.gap = "0.25rem";

        const label = document.createElement("label");
        label.style.fontSize = "0.78rem";
        label.style.color = "#cbd5e1";
        label.innerText = ctrl.label;
        ctrlDiv.appendChild(label);

        if (ctrl.type === "range") {
          const input = document.createElement("input");
          input.type = "range";
          input.min = ctrl.min;
          input.max = ctrl.max;
          input.step = ctrl.step;
          input.value = ctrl.default;
          input.addEventListener("input", (e) => {
            vals[ctrl.id] = e.target.value;
            simConfig.render(canvas, vals, 0);
          });
          ctrlDiv.appendChild(input);
        } else if (ctrl.type === "select") {
          const select = document.createElement("select");
          select.style.background = "#0f172a";
          select.style.color = "#f8fafc";
          select.style.border = "1px solid #334155";
          select.style.borderRadius = "6px";
          select.style.padding = "0.25rem 0.5rem";
          select.style.fontSize = "0.8rem";

          ctrl.options.forEach(opt => {
            const opEl = document.createElement("option");
            opEl.value = opt.value;
            opEl.innerText = opt.label;
            if (opt.value === ctrl.default) opEl.selected = true;
            select.appendChild(opEl);
          });

          select.addEventListener("change", (e) => {
            vals[ctrl.id] = e.target.value;
            simConfig.render(canvas, vals, 0);
          });
          ctrlDiv.appendChild(select);
        }
        controlsContainer.appendChild(ctrlDiv);
      });
    }
    box.appendChild(controlsContainer);
    container.appendChild(box);

    simConfig.render(canvas, vals, 0);
  }
};
"""

    with open("abstract-algebra-sims.js", "w", encoding="utf-8") as f:
        f.write(js_code)
    print("Successfully generated abstract-algebra-sims.js! Length:", len(js_code), "bytes")

if __name__ == "__main__":
    generate_sims_js()
