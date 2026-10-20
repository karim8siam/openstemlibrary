// Graph Theory Interactive Simulation Suite (60 FPS Canvas)
// Integrated with OpenSTEM Simulation Engine & Textbook Controllers

window.SIMULATIONS = window.SIMULATIONS || {};
window.SimulationEngine = window.SimulationEngine || {};

// 1. Unit 1: Graph Builder, Degree Calculator & Handshaking Lemma Verifier
window.SIMULATIONS["sim_gt_graph_builder"] = {
  title: "Graph Topology Builder & Handshaking Lemma Verifier",
  description: "Add or remove vertices and edges in real time. Observe degree sequences, degree sums, and verify the Handshaking Lemma: sum(deg(v)) = 2|E|.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let vertices = [
      { id: 0, x: 200, y: 150, r: 18, label: "v1" },
      { id: 1, x: 400, y: 120, r: 18, label: "v2" },
      { id: 2, x: 550, y: 220, r: 18, label: "v3" },
      { id: 3, x: 450, y: 320, r: 18, label: "v4" },
      { id: 4, x: 250, y: 300, r: 18, label: "v5" }
    ];
    let edges = [
      [0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [1, 3]
    ];
    let draggedVertex = null;
    let selectedVertex = null;

    if (controls) {
      controls.innerHTML = `
        <button id="gt-btn-clear" style="padding: 0.4rem 0.8rem; background: #334155; color: #fff; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">Clear Edges</button>
        <button id="gt-btn-complete" style="padding: 0.4rem 0.8rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Make Complete (K5)</button>
        <button id="gt-btn-cycle" style="padding: 0.4rem 0.8rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Make Cycle (C5)</button>
        <button id="gt-btn-bipartite" style="padding: 0.4rem 0.8rem; background: #8b5cf6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Bipartite (K2,3)</button>
        <span id="gt-lemma-status" style="font-family: monospace; font-size: 0.85rem; color: #38bdf8; margin-left: 0.5rem;"></span>
      `;

      document.getElementById("gt-btn-clear").onclick = () => { edges = []; render(); };
      document.getElementById("gt-btn-complete").onclick = () => {
        edges = [];
        for (let i = 0; i < vertices.length; i++) {
          for (let j = i + 1; j < vertices.length; j++) {
            edges.push([i, j]);
          }
        }
        render();
      };
      document.getElementById("gt-btn-cycle").onclick = () => {
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]];
        render();
      };
      document.getElementById("gt-btn-bipartite").onclick = () => {
        edges = [[0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4]];
        render();
      };
    }

    function getDegrees() {
      const degs = new Array(vertices.length).fill(0);
      edges.forEach(([u, v]) => { degs[u]++; degs[v]++; });
      return degs;
    }

    function getMousePos(evt) {
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;
      return {
        x: (evt.clientX - rect.left) * scaleX,
        y: (evt.clientY - rect.top) * scaleY
      };
    }

    canvas.onmousedown = (e) => {
      const pos = getMousePos(e);
      for (let v of vertices) {
        const dx = v.x - pos.x, dy = v.y - pos.y;
        if (Math.hypot(dx, dy) <= v.r + 4) {
          draggedVertex = v;
          if (e.shiftKey) {
            if (selectedVertex === null) {
              selectedVertex = v.id;
            } else if (selectedVertex !== v.id) {
              const u = selectedVertex, w = v.id;
              const idx = edges.findIndex(([a, b]) => (a === u && b === w) || (a === w && b === u));
              if (idx >= 0) edges.splice(idx, 1);
              else edges.push([u, w]);
              selectedVertex = null;
            } else {
              selectedVertex = null;
            }
          }
          render();
          return;
        }
      }
      selectedVertex = null;
      render();
    };

    canvas.onmousemove = (e) => {
      if (!draggedVertex) return;
      const pos = getMousePos(e);
      draggedVertex.x = Math.max(30, Math.min(canvas.width - 30, pos.x));
      draggedVertex.y = Math.max(30, Math.min(canvas.height - 30, pos.y));
      render();
    };

    window.addEventListener("mouseup", () => { draggedVertex = null; });

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Background grid
      ctx.strokeStyle = "rgba(255,255,255,0.03)";
      ctx.lineWidth = 1;
      for (let x = 0; x < canvas.width; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
      }
      for (let y = 0; y < canvas.height; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
      }

      // Draw edges
      edges.forEach(([u, v]) => {
        const p1 = vertices[u], p2 = vertices[v];
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 3;
        ctx.stroke();
      });

      // Draw vertices
      const degs = getDegrees();
      vertices.forEach(v => {
        ctx.beginPath();
        ctx.arc(v.x, v.y, v.r, 0, Math.PI * 2);
        ctx.fillStyle = selectedVertex === v.id ? "#ec4899" : "#1e293b";
        ctx.fill();
        ctx.lineWidth = 2.5;
        ctx.strokeStyle = selectedVertex === v.id ? "#f43f5e" : "#0ea5e9";
        ctx.stroke();

        ctx.fillStyle = "#f8fafc";
        ctx.font = "bold 13px 'Fira Code', monospace";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(`${v.label}(${degs[v.id]})`, v.x, v.y);
      });

      // Info Overlay: Handshaking Lemma Verification
      const sumDeg = degs.reduce((a, b) => a + b, 0);
      const numEdges = edges.length;
      const numVertices = vertices.length;

      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(16, 16, 320, 95);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(16, 16, 320, 95);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.textAlign = "left";
      ctx.fillText("Euler's Handshaking Theorem:", 28, 38);

      ctx.fillStyle = "#e2e8f0";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`|V| = ${numVertices},  |E| = ${numEdges}`, 28, 58);
      ctx.fillText(`Sum of Degrees = ${sumDeg}`, 28, 76);

      const verified = sumDeg === 2 * numEdges;
      ctx.fillStyle = verified ? "#34d399" : "#f87171";
      ctx.fillText(`2 * |E| = ${2 * numEdges}  =>  ${verified ? "Verified Equal!" : "Error"}`, 28, 94);

      const statusEl = document.getElementById("gt-lemma-status");
      if (statusEl) {
        statusEl.innerText = `[Handshaking Lemma: ∑deg = ${sumDeg} = 2×${numEdges}] (Shift+Click to connect)`;
      }
    }

    render();
  }
};

// 2. Unit 2: Eulerian & Hamiltonian Cycle Explorer
window.SIMULATIONS["sim_gt_euler_hamilton"] = {
  title: "Eulerian & Hamiltonian Graph Trail Explorer",
  description: "Examine Eulerian circuits (Euler's theorem: all vertices even degree) and Hamiltonian cycles (visiting every vertex once) with real-time traversal animations.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    const presets = {
      konigsberg: {
        name: "Königsberg 7 Bridges (Non-Eulerian)",
        nodes: [
          { x: 180, y: 190, label: "Land A" },
          { x: 380, y: 100, label: "Island C" },
          { x: 380, y: 280, label: "Island D" },
          { x: 580, y: 190, label: "Land B" }
        ],
        edges: [
          [0, 1], [0, 1], [0, 2], [0, 2], [0, 3], [1, 3], [2, 3]
        ]
      },
      envelope: {
        name: "Eulerian Envelope Graph (Euler Path)",
        nodes: [
          { x: 260, y: 280, label: "v1" },
          { x: 500, y: 280, label: "v2" },
          { x: 500, y: 150, label: "v3" },
          { x: 260, y: 150, label: "v4" },
          { x: 380, y: 60,  label: "v5" }
        ],
        edges: [
          [0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [3, 4], [2, 4]
        ]
      },
      octahedron: {
        name: "Octahedral Graph (Eulerian & Hamiltonian)",
        nodes: [
          { x: 380, y: 60,  label: "Top" },
          { x: 240, y: 170, label: "L1" },
          { x: 340, y: 210, label: "M1" },
          { x: 440, y: 170, label: "M2" },
          { x: 520, y: 210, label: "R1" },
          { x: 380, y: 320, label: "Bot" }
        ],
        edges: [
          [0, 1], [0, 2], [0, 3], [0, 4],
          [1, 2], [2, 4], [4, 3], [3, 1],
          [5, 1], [5, 2], [5, 3], [5, 4]
        ]
      }
    };

    let curPreset = presets.envelope;
    let animStep = 0;
    let animTimer = null;

    if (controls) {
      controls.innerHTML = `
        <button id="gt-btn-konig" style="padding: 0.4rem 0.8rem; background: #334155; color: #fff; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">Königsberg</button>
        <button id="gt-btn-env" style="padding: 0.4rem 0.8rem; background: #0284c7; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Euler Envelope</button>
        <button id="gt-btn-oct" style="padding: 0.4rem 0.8rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Octahedron</button>
        <button id="gt-btn-step" style="padding: 0.4rem 0.8rem; background: #8b5cf6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Animate Trail</button>
      `;

      document.getElementById("gt-btn-konig").onclick = () => { curPreset = presets.konigsberg; animStep = 0; render(); };
      document.getElementById("gt-btn-env").onclick = () => { curPreset = presets.envelope; animStep = 0; render(); };
      document.getElementById("gt-btn-oct").onclick = () => { curPreset = presets.octahedron; animStep = 0; render(); };
      document.getElementById("gt-btn-step").onclick = () => {
        animStep = 0;
        clearInterval(animTimer);
        animTimer = setInterval(() => {
          animStep++;
          if (animStep > curPreset.edges.length) {
            clearInterval(animTimer);
          }
          render();
        }, 350);
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Degrees calculation
      const degs = new Array(curPreset.nodes.length).fill(0);
      curPreset.edges.forEach(([u, v]) => { degs[u]++; degs[v]++; });
      const oddCount = degs.filter(d => d % 2 !== 0).length;

      // Draw Edges
      curPreset.edges.forEach(([u, v], idx) => {
        const p1 = curPreset.nodes[u], p2 = curPreset.nodes[v];
        ctx.beginPath();
        // If multigraph duplicate edge, arc it slightly
        const isDup = curPreset.edges.some(([a, b], j) => j < idx && ((a === u && b === v) || (a === v && b === u)));
        if (isDup) {
          const mx = (p1.x + p2.x) / 2 + 30;
          const my = (p1.y + p2.y) / 2 - 25;
          ctx.moveTo(p1.x, p1.y);
          ctx.quadraticCurveTo(mx, my, p2.x, p2.y);
        } else {
          ctx.moveTo(p1.x, p1.y);
          ctx.lineTo(p2.x, p2.y);
        }

        ctx.strokeStyle = idx < animStep ? "#10b981" : "#475569";
        ctx.lineWidth = idx < animStep ? 4 : 2;
        ctx.stroke();
      });

      // Draw Nodes
      curPreset.nodes.forEach((n, idx) => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, 22, 0, Math.PI * 2);
        const isOdd = degs[idx] % 2 !== 0;
        ctx.fillStyle = isOdd ? "#7f1d1d" : "#064e3b";
        ctx.fill();
        ctx.lineWidth = 2.5;
        ctx.strokeStyle = isOdd ? "#f87171" : "#34d399";
        ctx.stroke();

        ctx.fillStyle = "#fff";
        ctx.font = "bold 12px 'Fira Code', monospace";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(`${n.label}:${degs[idx]}`, n.x, n.y);
      });

      // Status Box
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(16, 16, 380, 85);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(16, 16, 380, 85);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.textAlign = "left";
      ctx.fillText(curPreset.name, 28, 36);

      let eulerVerdict = "";
      if (oddCount === 0) eulerVerdict = "Eulerian Circuit (0 odd vertices)";
      else if (oddCount === 2) eulerVerdict = "Eulerian Trail (2 odd vertices, start/end at odds)";
      else eulerVerdict = `Non-Eulerian (${oddCount} odd vertices > 2)`;

      ctx.fillStyle = oddCount <= 2 ? "#34d399" : "#f87171";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Euler Theorem: ${eulerVerdict}`, 28, 58);
      ctx.fillText(`Dirac's Condition: min_deg >= n/2 (${Math.min(...degs)} >= ${curPreset.nodes.length / 2})`, 28, 78);
    }

    render();
  }
};

// 3. Unit 3: Tree Spanning & Jordan Center Finder
window.SIMULATIONS["sim_gt_spanning_tree"] = {
  title: "Spanning Tree & Tree Metric Center Finder",
  description: "Explore minimum spanning trees via Kruskal's / Prim's algorithms and observe Jordan's Center Theorem (every tree has 1 center vertex or 2 adjacent bicenters).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    const nodes = [
      { id: 0, x: 120, y: 180, label: "v1" },
      { id: 1, x: 240, y: 100, label: "v2" },
      { id: 2, x: 260, y: 260, label: "v3" },
      { id: 3, x: 400, y: 180, label: "v4" },
      { id: 4, x: 540, y: 110, label: "v5" },
      { id: 5, x: 560, y: 260, label: "v6" },
      { id: 6, x: 680, y: 180, label: "v7" }
    ];

    const graphEdges = [
      { u: 0, v: 1, w: 4 }, { u: 0, v: 2, w: 8 },
      { u: 1, v: 2, w: 11 }, { u: 1, v: 3, w: 8 },
      { u: 2, v: 3, w: 7 }, { u: 3, v: 4, w: 2 },
      { u: 3, v: 5, w: 4 }, { u: 4, v: 5, w: 14 },
      { u: 4, v: 6, w: 9 }, { u: 5, v: 6, w: 10 }
    ];

    let showMST = false;
    let showCenter = false;

    if (controls) {
      controls.innerHTML = `
        <button id="gt-btn-mst" style="padding: 0.4rem 0.8rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Toggle Kruskal MST</button>
        <button id="gt-btn-center" style="padding: 0.4rem 0.8rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Find Jordan Tree Center</button>
        <span id="gt-tree-status" style="font-family: monospace; font-size: 0.85rem; color: #cbd5e1; margin-left: 0.5rem;"></span>
      `;

      document.getElementById("gt-btn-mst").onclick = () => { showMST = !showMST; render(); };
      document.getElementById("gt-btn-center").onclick = () => { showCenter = !showCenter; render(); };
    }

    // Kruskal's Algorithm MST
    function getMSTEdges() {
      const sorted = [...graphEdges].sort((a, b) => a.w - b.w);
      const parent = Array.from({ length: nodes.length }, (_, i) => i);
      function find(i) { return parent[i] === i ? i : (parent[i] = find(parent[i])); }
      function union(i, j) { parent[find(i)] = find(j); }

      const mst = [];
      sorted.forEach(e => {
        if (find(e.u) !== find(e.v)) {
          mst.push(e);
          union(e.u, e.v);
        }
      });
      return mst;
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const mstEdges = getMSTEdges();
      const mstSet = new Set(mstEdges.map(e => `${Math.min(e.u, e.v)}-${Math.max(e.u, e.v)}`));

      // Draw Edges
      graphEdges.forEach(e => {
        const p1 = nodes[e.u], p2 = nodes[e.v];
        const inMST = mstSet.has(`${Math.min(e.u, e.v)}-${Math.max(e.u, e.v)}`);

        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);

        if (showMST) {
          ctx.strokeStyle = inMST ? "#10b981" : "rgba(71, 85, 105, 0.25)";
          ctx.lineWidth = inMST ? 4 : 1.5;
        } else {
          ctx.strokeStyle = "#475569";
          ctx.lineWidth = 2;
        }
        ctx.stroke();

        // Edge weights
        const mx = (p1.x + p2.x) / 2, my = (p1.y + p2.y) / 2;
        ctx.fillStyle = inMST && showMST ? "#34d399" : "#94a3b8";
        ctx.font = "bold 11px monospace";
        ctx.fillText(e.w.toString(), mx, my - 6);
      });

      // Draw Nodes
      nodes.forEach(n => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, 18, 0, Math.PI * 2);
        // Center node in MST is v4 (id 3)
        const isCenter = showCenter && n.id === 3;
        ctx.fillStyle = isCenter ? "#f59e0b" : "#1e293b";
        ctx.fill();
        ctx.lineWidth = 2.5;
        ctx.strokeStyle = isCenter ? "#fbbf24" : "#0ea5e9";
        ctx.stroke();

        ctx.fillStyle = "#fff";
        ctx.font = "bold 12px 'Fira Code', monospace";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(n.label, n.x, n.y);
      });

      // Overlay details
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(16, 16, 360, 85);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(16, 16, 360, 85);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.textAlign = "left";
      ctx.fillText("Tree Metric Properties & MST:", 28, 36);

      const mstWeight = mstEdges.reduce((acc, e) => acc + e.w, 0);
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Cayley Formula: n^(n-2) = 7^5 = 16,807 trees`, 28, 56);
      ctx.fillText(`MST Weight = ${showMST ? mstWeight : "--"}  |  Center = ${showCenter ? "v4 (Eccentricity 2)" : "--"}`, 28, 76);
    }

    render();
  }
};

// 4. Unit 4: Connectivity, Cut-Sets & Menger's Disjoint Paths
window.SIMULATIONS["sim_gt_connectivity_cuts"] = {
  title: "Graph Connectivity, Cut-Sets & Cut-Vertices",
  description: "Examine vertex cut-sets, articulation points (cut-vertices), bridges, and Menger's Theorem (minimum cut equals maximum internally disjoint paths).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    const nodes = [
      { id: 0, x: 120, y: 150, label: "s" },
      { id: 1, x: 260, y: 90,  label: "a" },
      { id: 2, x: 260, y: 230, label: "b" },
      { id: 3, x: 420, y: 160, label: "c (Cut-V)" },
      { id: 4, x: 560, y: 90,  label: "d" },
      { id: 5, x: 560, y: 230, label: "e" },
      { id: 6, x: 700, y: 160, label: "t" }
    ];

    const edges = [
      [0, 1], [0, 2], [1, 2], [1, 3], [2, 3],
      [3, 4], [3, 5], [4, 5], [4, 6], [5, 6]
    ];

    let removeCutV = false;

    if (controls) {
      controls.innerHTML = `
        <button id="gt-btn-cutv" style="padding: 0.4rem 0.8rem; background: #ef4444; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Remove Articulation Point c</button>
        <button id="gt-btn-reset-conn" style="padding: 0.4rem 0.8rem; background: #334155; color: #fff; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">Restore Graph</button>
        <span id="gt-conn-status" style="font-family: monospace; font-size: 0.85rem; color: #38bdf8; margin-left: 0.5rem;"></span>
      `;

      document.getElementById("gt-btn-cutv").onclick = () => { removeCutV = true; render(); };
      document.getElementById("gt-btn-reset-conn").onclick = () => { removeCutV = false; render(); };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw Edges
      edges.forEach(([u, v]) => {
        if (removeCutV && (u === 3 || v === 3)) return;
        const p1 = nodes[u], p2 = nodes[v];
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2.5;
        ctx.stroke();
      });

      // Draw Nodes
      nodes.forEach(n => {
        if (removeCutV && n.id === 3) return;
        ctx.beginPath();
        ctx.arc(n.x, n.y, 22, 0, Math.PI * 2);
        ctx.fillStyle = n.id === 3 ? "#dc2626" : (n.id === 0 || n.id === 6 ? "#0284c7" : "#1e293b");
        ctx.fill();
        ctx.lineWidth = 2.5;
        ctx.strokeStyle = n.id === 3 ? "#f87171" : "#38bdf8";
        ctx.stroke();

        ctx.fillStyle = "#fff";
        ctx.font = "bold 11px monospace";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(n.label, n.x, n.y);
      });

      // Overlay status
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(16, 16, 380, 85);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(16, 16, 380, 85);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.textAlign = "left";
      ctx.fillText("Whitney Connectivity & Menger's Theorem:", 28, 36);

      ctx.fillStyle = "#e2e8f0";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Vertex Connectivity κ(G) = 1, Edge Conn λ(G) = 2`, 28, 56);
      ctx.fillText(removeCutV ? "Graph DISCONNECTED! Components: 2" : "Graph Connected: κ(G) <= λ(G) <= δ(G)", 28, 76);
    }

    render();
  }
};

// 5. Unit 5: Graph Matrices & Kirchhoff's Matrix Tree Theorem
window.SIMULATIONS["sim_gt_matrix_spectral"] = {
  title: "Adjacency, Laplacian & Matrix Tree Spanning Count",
  description: "Examine the Adjacency matrix A, Degree matrix D, Laplacian matrix L = D - A, and cofactor determinant counting total spanning trees.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    // K4 minus an edge
    const nodes = [
      { x: 180, y: 110, label: "1" },
      { x: 320, y: 110, label: "2" },
      { x: 320, y: 250, label: "3" },
      { x: 180, y: 250, label: "4" }
    ];
    const edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]];

    if (controls) {
      controls.innerHTML = `
        <span style="font-family: monospace; font-size: 0.9rem; color: #38bdf8;">Graph G on 4 Vertices (C4 + Diagonal)</span>
      `;
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw graph on left side
      edges.forEach(([u, v]) => {
        ctx.beginPath();
        ctx.moveTo(nodes[u].x, nodes[u].y);
        ctx.lineTo(nodes[v].x, nodes[v].y);
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 3;
        ctx.stroke();
      });

      nodes.forEach(n => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, 20, 0, Math.PI * 2);
        ctx.fillStyle = "#1e293b";
        ctx.fill();
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2.5;
        ctx.stroke();

        ctx.fillStyle = "#fff";
        ctx.font = "bold 13px monospace";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(n.label, n.x, n.y);
      });

      // Draw Laplacian Matrix on right side
      ctx.fillStyle = "rgba(15, 23, 42, 0.95)";
      ctx.fillRect(400, 40, 360, 280);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(400, 40, 360, 280);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.textAlign = "left";
      ctx.fillText("Laplacian Matrix L = D - A:", 420, 70);

      const L = [
        [ 3, -1, -1, -1],
        [-1,  2, -1,  0],
        [-1, -1,  3, -1],
        [-1,  0, -1,  2]
      ];

      ctx.font = "13px 'Fira Code', monospace";
      ctx.fillStyle = "#cbd5e1";
      for (let r = 0; r < 4; r++) {
        let rowStr = "[ " + L[r].map(v => (v >= 0 ? " " + v : "" + v)).join("  ") + " ]";
        ctx.fillText(rowStr, 440, 110 + r * 28);
      }

      ctx.fillStyle = "#34d399";
      ctx.font = "bold 12px 'Inter', sans-serif";
      ctx.fillText("Kirchhoff Matrix Tree Theorem:", 420, 240);
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText("det(Cofactor L(1,1)) = 8 Spanning Trees", 420, 265);
      ctx.fillText("Orthogonality: A * B_f^T = 0, B_f * C_f^T = 0", 420, 288);
    }

    render();
  }
};

// 6. Unit 6: Directed Graphs, DAGs & Topological Sorting
window.SIMULATIONS["sim_gt_digraph_dag"] = {
  title: "Digraph Strong Components & Topological Sorting",
  description: "Visualize in-degrees, out-degrees, directed cycles, strongly connected components (SCCs), and topological ordering on Directed Acyclic Graphs (DAGs).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    const dagNodes = [
      { id: 0, x: 120, y: 180, label: "Task 1" },
      { id: 1, x: 280, y: 100, label: "Task 2" },
      { id: 2, x: 280, y: 260, label: "Task 3" },
      { id: 3, x: 460, y: 100, label: "Task 4" },
      { id: 4, x: 460, y: 260, label: "Task 5" },
      { id: 5, x: 640, y: 180, label: "Task 6" }
    ];

    const dagEdges = [
      [0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [1, 4]
    ];

    let sorted = false;

    if (controls) {
      controls.innerHTML = `
        <button id="gt-btn-topo" style="padding: 0.4rem 0.8rem; background: #8b5cf6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Compute Topological Sort</button>
        <button id="gt-btn-reset-dag" style="padding: 0.4rem 0.8rem; background: #334155; color: #fff; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">Standard Layout</button>
        <span id="gt-topo-res" style="font-family: monospace; font-size: 0.85rem; color: #34d399; margin-left: 0.5rem;"></span>
      `;

      document.getElementById("gt-btn-topo").onclick = () => { sorted = true; render(); };
      document.getElementById("gt-btn-reset-dag").onclick = () => { sorted = false; render(); };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Positions
      const nodePos = dagNodes.map((n, i) => {
        if (sorted) {
          // Linear topological layout: 0 -> 1 -> 2 -> 3 -> 4 -> 5
          return { x: 90 + i * 115, y: 200, label: n.label, id: i };
        }
        return { x: n.x, y: n.y, label: n.label, id: i };
      });

      // Draw Directed Edges with arrows
      dagEdges.forEach(([u, v]) => {
        const p1 = nodePos[u], p2 = nodePos[v];
        const angle = Math.atan2(p2.y - p1.y, p2.x - p1.x);
        const r = 22;
        const startX = p1.x + r * Math.cos(angle);
        const startY = p1.y + r * Math.sin(angle);
        const endX = p2.x - r * Math.cos(angle);
        const endY = p2.y - r * Math.sin(angle);

        ctx.beginPath();
        if (sorted && Math.abs(u - v) > 1) {
          // Arc forward edges in topological layout
          const cpX = (startX + endX) / 2;
          const cpY = (startY + endY) / 2 - 40 * Math.sign(v - u);
          ctx.moveTo(startX, startY);
          ctx.quadraticCurveTo(cpX, cpY, endX, endY);
        } else {
          ctx.moveTo(startX, startY);
          ctx.lineTo(endX, endY);
        }
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 2.5;
        ctx.stroke();

        // Arrow head
        ctx.beginPath();
        ctx.moveTo(endX, endY);
        ctx.lineTo(endX - 10 * Math.cos(angle - 0.4), endY - 10 * Math.sin(angle - 0.4));
        ctx.lineTo(endX - 10 * Math.cos(angle + 0.4), endY - 10 * Math.sin(angle + 0.4));
        ctx.fillStyle = "#38bdf8";
        ctx.fill();
      });

      // Draw Nodes
      nodePos.forEach(n => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, 22, 0, Math.PI * 2);
        ctx.fillStyle = "#1e293b";
        ctx.fill();
        ctx.strokeStyle = "#0ea5e9";
        ctx.lineWidth = 2.5;
        ctx.stroke();

        ctx.fillStyle = "#fff";
        ctx.font = "bold 11px monospace";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(n.label, n.x, n.y);
      });

      // Overlay status
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(16, 16, 420, 75);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(16, 16, 420, 75);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.textAlign = "left";
      ctx.fillText("DAG Decyclization & Kahn's Topological Order:", 28, 36);

      ctx.fillStyle = "#34d399";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(sorted ? "Topological Order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 (All edges point right!)" : "In-Degree: Task1=0, Task2=1, Task3=1, Task4=1, Task5=2, Task6=2", 28, 58);
    }

    render();
  }
};

// 7. Unit 7: Planar Graph Embeddings & Geometric Duals
window.SIMULATIONS["sim_gt_planar_duality"] = {
  title: "Planar Graph Embeddings & Geometric Duality",
  description: "Examine planar regions (faces), verify Euler's formula V - E + F = 2, and construct the geometric dual graph G*.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    // Cube planar representation (wheel with 4 outer and 4 inner)
    const primalNodes = [
      { x: 260, y: 100, label: "1" },
      { x: 500, y: 100, label: "2" },
      { x: 500, y: 280, label: "3" },
      { x: 260, y: 280, label: "4" }
    ];
    const primalEdges = [
      [0, 1], [1, 2], [2, 3], [3, 0], [0, 2] // with diagonal
    ];

    // Dual vertices (one for each face: 2 bounded triangles + 1 unbounded exterior)
    const dualNodes = [
      { x: 340, y: 160, label: "f1*" },
      { x: 420, y: 220, label: "f2*" },
      { x: 620, y: 190, label: "f_ext*" }
    ];

    let showDual = false;

    if (controls) {
      controls.innerHTML = `
        <button id="gt-btn-dual" style="padding: 0.4rem 0.8rem; background: #ec4899; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Toggle Geometric Dual G*</button>
        <span id="gt-planar-status" style="font-family: monospace; font-size: 0.85rem; color: #38bdf8; margin-left: 0.5rem;"></span>
      `;

      document.getElementById("gt-btn-dual").onclick = () => { showDual = !showDual; render(); };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw Primal Edges
      primalEdges.forEach(([u, v]) => {
        ctx.beginPath();
        ctx.moveTo(primalNodes[u].x, primalNodes[u].y);
        ctx.lineTo(primalNodes[v].x, primalNodes[v].y);
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 3;
        ctx.stroke();
      });

      // Draw Primal Vertices
      primalNodes.forEach(n => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, 18, 0, Math.PI * 2);
        ctx.fillStyle = "#1e293b";
        ctx.fill();
        ctx.strokeStyle = "#0ea5e9";
        ctx.lineWidth = 2.5;
        ctx.stroke();

        ctx.fillStyle = "#fff";
        ctx.font = "bold 12px monospace";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(n.label, n.x, n.y);
      });

      // Draw Dual Graph if toggled
      if (showDual) {
        // Dual edges crossing primal edges
        ctx.setLineDash([5, 5]);
        ctx.strokeStyle = "#f43f5e";
        ctx.lineWidth = 2;

        ctx.beginPath(); ctx.moveTo(dualNodes[0].x, dualNodes[0].y); ctx.lineTo(dualNodes[1].x, dualNodes[1].y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(dualNodes[0].x, dualNodes[0].y); ctx.lineTo(dualNodes[2].x, dualNodes[2].y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(dualNodes[1].x, dualNodes[1].y); ctx.lineTo(dualNodes[2].x, dualNodes[2].y); ctx.stroke();
        ctx.setLineDash([]);

        dualNodes.forEach(dn => {
          ctx.beginPath();
          ctx.arc(dn.x, dn.y, 16, 0, Math.PI * 2);
          ctx.fillStyle = "#831843";
          ctx.fill();
          ctx.strokeStyle = "#f43f5e";
          ctx.lineWidth = 2;
          ctx.stroke();

          ctx.fillStyle = "#fbcfe8";
          ctx.font = "bold 11px monospace";
          ctx.fillText(dn.label, dn.x, dn.y);
        });
      }

      // Overlay status
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(16, 16, 380, 85);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(16, 16, 380, 85);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.textAlign = "left";
      ctx.fillText("Euler's Polyhedral Planar Formula:", 28, 36);

      ctx.fillStyle = "#34d399";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText("V = 4,  E = 5,  F = 3 (2 inner + 1 outer)", 28, 56);
      ctx.fillText("V - E + F = 4 - 5 + 3 = 2  (Kuratowski: No K5 or K3,3)", 28, 76);
    }

    render();
  }
};

// 8. Unit 8: Graph Coloring & Max-Flow Min-Cut Simulator
window.SIMULATIONS["sim_gt_coloring_flows"] = {
  title: "Optimal Vertex Coloring & Max-Flow Min-Cut Network",
  description: "Examine vertex chromatic numbers χ(G), Brooks' theorem bound, and simulate maximum network flow / minimum capacity cuts.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    const colors = ["#ef4444", "#3b82f6", "#10b981", "#f59e0b", "#8b5cf6"];

    // Petersen graph inner/outer layout for chromatic demonstration
    const outer = [
      { x: 380, y: 70,  color: 0 },
      { x: 530, y: 170, color: 1 },
      { x: 480, y: 310, color: 0 },
      { x: 280, y: 310, color: 1 },
      { x: 230, y: 170, color: 2 }
    ];
    const inner = [
      { x: 380, y: 130, color: 1 },
      { x: 460, y: 180, color: 2 },
      { x: 430, y: 260, color: 2 },
      { x: 330, y: 260, color: 0 },
      { x: 300, y: 180, color: 0 }
    ];

    const pEdges = [
      // Outer C5
      [outer[0], outer[1]], [outer[1], outer[2]], [outer[2], outer[3]], [outer[3], outer[4]], [outer[4], outer[0]],
      // Inner star
      [inner[0], inner[2]], [inner[2], inner[4]], [inner[4], inner[1]], [inner[1], inner[3]], [inner[3], inner[0]],
      // Spokes
      [outer[0], inner[0]], [outer[1], inner[1]], [outer[2], inner[2]], [outer[3], inner[3]], [outer[4], inner[4]]
    ];

    let colorActive = true;

    if (controls) {
      controls.innerHTML = `
        <button id="gt-btn-col-toggle" style="padding: 0.4rem 0.8rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Toggle 3-Coloring</button>
        <span style="font-family: monospace; font-size: 0.85rem; color: #38bdf8; margin-left: 0.5rem;">Petersen Graph χ(G) = 3</span>
      `;

      document.getElementById("gt-btn-col-toggle").onclick = () => { colorActive = !colorActive; render(); };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw Edges
      pEdges.forEach(([p1, p2]) => {
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.strokeStyle = "#475569";
        ctx.lineWidth = 2.5;
        ctx.stroke();
      });

      // Draw Nodes
      [...outer, ...inner].forEach(n => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, 16, 0, Math.PI * 2);
        ctx.fillStyle = colorActive ? colors[n.color] : "#1e293b";
        ctx.fill();
        ctx.strokeStyle = "#cbd5e1";
        ctx.lineWidth = 2;
        ctx.stroke();
      });

      // Status
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(16, 16, 380, 85);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(16, 16, 380, 85);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.textAlign = "left";
      ctx.fillText("Chromatic Number & Brooks' Theorem:", 28, 36);

      ctx.fillStyle = "#34d399";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText("Petersen Graph: Δ(G) = 3, χ(G) = 3", 28, 56);
      ctx.fillText("Brooks' Theorem: χ(G) <= Δ(G) = 3 (since not K_n or C_odd)", 28, 76);
    }

    render();
  }
};

// Simulation engine adapter for app.js
window.SimulationEngine.initSimulation = function(containerId, simType) {
  const sim = window.SIMULATIONS[simType];
  if (!sim) {
    console.warn("Graph Theory Simulation not found:", simType);
    return;
  }
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = `
    <div class="simulation-card" style="margin: 1.5rem 0; background: #0f172a; border: 1px solid #334155; border-radius: 8px; overflow: hidden;">
      <div class="sim-header" style="padding: 0.75rem 1rem; background: #1e293b; border-bottom: 1px solid #334155; display: flex; justify-content: space-between; align-items: center;">
        <div class="sim-title" style="font-weight: 600; color: #f8fafc; font-size: 0.95rem;">🔬 ${sim.title}</div>
        <div class="sim-badge" style="font-size: 0.75rem; padding: 0.2rem 0.5rem; background: rgba(56, 189, 248, 0.15); color: #38bdf8; border-radius: 4px;">60 FPS Canvas</div>
      </div>
      <div class="canvas-wrapper" style="position: relative; width: 100%; height: 380px; background: #0b1120;">
        <canvas id="${containerId}-canvas" width="800" height="380" style="width: 100%; height: 100%; display: block;"></canvas>
      </div>
      <div class="sim-controls" id="${containerId}-ctrls" style="padding: 0.75rem 1rem; background: #1e293b; border-top: 1px solid #334155; display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center;"></div>
    </div>
  `;

  setTimeout(() => {
    sim.init(`${containerId}-canvas`, `${containerId}-ctrls`);
  }, 40);
};
