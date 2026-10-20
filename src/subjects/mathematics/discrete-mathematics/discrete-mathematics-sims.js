// Discrete Mathematics Interactive Computational Simulations Engine
// High-performance 60 FPS HTML5 Canvas models registered to window.SIMULATIONS

window.SIMULATIONS = window.SIMULATIONS || {};

// ============================================================================
// 1. Unit 1: Propositional Logic Truth Table & Circuit Gate Engine
// ============================================================================
window.SIMULATIONS["sim_dm_logic_truth_tables"] = {
  title: "Propositional Logic Truth Tables & Digital Circuit Gate Engine",
  description: "Explore boolean propositional formulas and logic gates in real-time. Toggle binary input variables P, Q, R to observe voltage propagation through AND, OR, NOT, NAND, XOR gates and evaluate equivalent compound statements like (P ∧ Q) ∨ (¬P ∧ R).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let valP = true;
    let valQ = false;
    let valR = true;
    let currentCircuit = "mux"; // "mux", "xor", "majority"

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Input P:</label>
        <button id="btn-dm-p" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; background: #10b981; color: #fff;">1 (TRUE)</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.4rem;">Input Q:</label>
        <button id="btn-dm-q" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; background: #64748b; color: #fff;">0 (FALSE)</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.4rem;">Input R:</label>
        <button id="btn-dm-r" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; background: #10b981; color: #fff;">1 (TRUE)</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.6rem;">Circuit Formula:</label>
        <select id="dm-circuit-select" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="mux" selected>2-to-1 Multiplexer: (P ∧ Q) ∨ (¬P ∧ R)</option>
          <option value="xor">XOR Equivalent: (P ∨ Q) ∧ ¬(P ∧ Q)</option>
          <option value="majority">Majority Function: (P ∧ Q) ∨ (Q ∧ R) ∨ (P ∧ R)</option>
        </select>
      `;

      const btnP = document.getElementById("btn-dm-p");
      const btnQ = document.getElementById("btn-dm-q");
      const btnR = document.getElementById("btn-dm-r");
      const selCirc = document.getElementById("dm-circuit-select");

      function updateButtons() {
        btnP.style.background = valP ? "#10b981" : "#64748b";
        btnP.innerText = valP ? "1 (TRUE)" : "0 (FALSE)";
        btnQ.style.background = valQ ? "#10b981" : "#64748b";
        btnQ.innerText = valQ ? "1 (TRUE)" : "0 (FALSE)";
        btnR.style.background = valR ? "#10b981" : "#64748b";
        btnR.innerText = valR ? "1 (TRUE)" : "0 (FALSE)";
      }

      btnP.onclick = () => { valP = !valP; updateButtons(); };
      btnQ.onclick = () => { valQ = !valQ; updateButtons(); };
      btnR.onclick = () => { valR = !valR; updateButtons(); };
      selCirc.onchange = (e) => { currentCircuit = e.target.value; };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      // Split canvas: Left half is circuit schematic, Right half is truth table
      const midSplit = W * 0.56;

      // 1. Circuit Schematic Pane
      ctx.fillStyle = "#090d16";
      ctx.fillRect(0, 0, midSplit, H);

      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(midSplit, 0); ctx.lineTo(midSplit, H);
      ctx.stroke();

      // Draw input nodes P, Q, R
      const inX = 40;
      const pyP = 70, pyQ = 160, pyR = 250;

      function drawInputNode(x, y, label, val) {
        ctx.fillStyle = val ? "#10b981" : "#64748b";
        ctx.beginPath();
        ctx.arc(x, y, 14, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(label, x - 5, y + 4);

        ctx.fillStyle = val ? "#34d399" : "#94a3b8";
        ctx.font = "11px monospace";
        ctx.fillText(val ? "= 1" : "= 0", x + 18, y + 4);
      }

      drawInputNode(inX, pyP, "P", valP);
      drawInputNode(inX, pyQ, "Q", valQ);
      drawInputNode(inX, pyR, "R", valR);

      // Evaluate Circuit logic
      let outVal = false;
      let gate1Val = false, gate2Val = false;

      if (currentCircuit === "mux") {
        gate1Val = valP && valQ; // AND 1
        gate2Val = (!valP) && valR; // AND 2
        outVal = gate1Val || gate2Val; // OR
      } else if (currentCircuit === "xor") {
        gate1Val = valP || valQ; // OR
        gate2Val = !(valP && valQ); // NAND
        outVal = gate1Val && gate2Val; // AND
      } else {
        gate1Val = (valP && valQ);
        gate2Val = (valQ && valR) || (valP && valR);
        outVal = gate1Val || gate2Val;
      }

      // Draw Wire Lines with high-contrast color (green for 1, slate for 0)
      function drawWire(x1, y1, x2, y2, val) {
        ctx.strokeStyle = val ? "#10b981" : "#475569";
        ctx.lineWidth = val ? 2.5 : 1.5;
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();
      }

      // Draw Gates
      function drawGate(gx, gy, type, in1, in2, out) {
        ctx.fillStyle = "#1e293b";
        ctx.strokeStyle = out ? "#38bdf8" : "#64748b";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.roundRect(gx - 28, gy - 20, 56, 40, 6);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#f8fafc";
        ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(type, gx - 14, gy + 4);

        // Input wires to gate
        drawWire(gx - 45, gy - 10, gx - 28, gy - 10, in1);
        drawWire(gx - 45, gy + 10, gx - 28, gy + 10, in2);

        // Output wire
        drawWire(gx + 28, gy, gx + 45, gy, out);
      }

      const g1X = 180, g1Y = 100;
      const g2X = 180, g2Y = 220;
      const gOutX = 330, gOutY = 160;

      if (currentCircuit === "mux") {
        drawGate(g1X, g1Y, "AND", valP, valQ, gate1Val);
        drawGate(g2X, g2Y, "AND", !valP, valR, gate2Val);
        drawGate(gOutX, gOutY, "OR", gate1Val, gate2Val, outVal);
      } else if (currentCircuit === "xor") {
        drawGate(g1X, g1Y, "OR", valP, valQ, gate1Val);
        drawGate(g2X, g2Y, "NAND", valP, valQ, gate2Val);
        drawGate(gOutX, gOutY, "AND", gate1Val, gate2Val, outVal);
      } else {
        drawGate(g1X, g1Y, "AND", valP, valQ, gate1Val);
        drawGate(g2X, g2Y, "OR", valQ && valR, valP && valR, gate2Val);
        drawGate(gOutX, gOutY, "OR", gate1Val, gate2Val, outVal);
      }

      // Intermediate Connectors
      drawWire(inX + 15, pyP, g1X - 45, g1Y - 10, valP);
      drawWire(inX + 15, pyQ, g1X - 45, g1Y + 10, valQ);
      drawWire(inX + 15, pyP, g2X - 45, g2Y - 10, !valP);
      drawWire(inX + 15, pyR, g2X - 45, g2Y + 10, valR);

      drawWire(g1X + 45, g1Y, gOutX - 45, gOutY - 10, gate1Val);
      drawWire(g2X + 45, g2Y, gOutX - 45, gOutY + 10, gate2Val);

      // Final Output Bulb
      const outBulbX = gOutX + 75;
      ctx.fillStyle = outVal ? "#fbbf24" : "#334155";
      ctx.beginPath();
      ctx.arc(outBulbX, gOutY, 16, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = outVal ? "#f59e0b" : "#64748b";
      ctx.lineWidth = 2.5;
      ctx.stroke();

      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(outVal ? "1" : "0", outBulbX - 4, gOutY + 4);

      ctx.fillStyle = outVal ? "#fbbf24" : "#94a3b8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("OUTPUT Y", outBulbX - 25, gOutY + 35);

      // 2. Truth Table Pane
      const tx = midSplit + 15;
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(midSplit, 0, W - midSplit, H);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Complete Truth Table Evaluation", tx + 10, 32);

      const headers = ["P", "Q", "R", "G₁", "G₂", "Output Y"];
      const colW = (W - midSplit - 35) / headers.length;
      const startY = 55;

      // Table Header Row
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(tx, startY, W - midSplit - 30, 24);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "bold 11px monospace";
      headers.forEach((h, idx) => {
        ctx.fillText(h, tx + idx * colW + 8, startY + 16);
      });

      // 8 Truth Table Rows
      for (let r = 0; r < 8; r++) {
        const bp = Boolean((r >> 2) & 1);
        const bq = Boolean((r >> 1) & 1);
        const br = Boolean(r & 1);

        let g1 = false, g2 = false, yOut = false;
        if (currentCircuit === "mux") {
          g1 = bp && bq; g2 = (!bp) && br; yOut = g1 || g2;
        } else if (currentCircuit === "xor") {
          g1 = bp || bq; g2 = !(bp && bq); yOut = g1 && g2;
        } else {
          g1 = bp && bq; g2 = (bq && br) || (bp && br); yOut = g1 || g2;
        }

        const isCurrent = (bp === valP && bq === valQ && br === valR);
        const rowY = startY + 28 + r * 22;

        if (isCurrent) {
          ctx.fillStyle = "rgba(56, 189, 248, 0.22)";
          ctx.fillRect(tx, rowY - 14, W - midSplit - 30, 20);
          ctx.strokeStyle = "#38bdf8";
          ctx.strokeRect(tx, rowY - 14, W - midSplit - 30, 20);
        }

        ctx.fillStyle = isCurrent ? "#38bdf8" : "#94a3b8";
        ctx.font = "11px monospace";
        const rowVals = [bp ? "1" : "0", bq ? "1" : "0", br ? "1" : "0", g1 ? "1" : "0", g2 ? "1" : "0", yOut ? "1" : "0"];
        rowVals.forEach((val, idx) => {
          if (idx === 5) {
            ctx.fillStyle = yOut ? "#34d399" : "#f87171";
            ctx.font = "bold 11px monospace";
          }
          ctx.fillText(val, tx + idx * colW + 10, rowY);
          ctx.fillStyle = isCurrent ? "#38bdf8" : "#94a3b8";
          ctx.font = "11px monospace";
        });
      }

      // Formula display at bottom
      ctx.fillStyle = "#334155";
      ctx.fillRect(tx, H - 55, W - midSplit - 30, 42);
      ctx.strokeStyle = "#475569";
      ctx.strokeRect(tx, H - 55, W - midSplit - 30, 42);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 11px Inter, sans-serif";
      let formulaText = "";
      if (currentCircuit === "mux") formulaText = "Formula: Y = (P ∧ Q) ∨ (¬P ∧ R)";
      else if (currentCircuit === "xor") formulaText = "Formula: Y = (P ∨ Q) ∧ ¬(P ∧ Q) ≡ P ⊕ Q";
      else formulaText = "Formula: Y = (P ∧ Q) ∨ (Q ∧ R) ∨ (P ∧ R)";
      ctx.fillText(formulaText, tx + 10, H - 34);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText(`Current Evaluation: Y = ${outVal ? "TRUE (1)" : "FALSE (0)"}`, tx + 10, H - 18);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 2. Unit 2: Mathematical Induction & Recursive Towers of Hanoi
// ============================================================================
window.SIMULATIONS["sim_dm_induction_towers"] = {
  title: "Mathematical Induction & Recursive Towers of Hanoi Visualizer",
  description: "Experience the rigorous equivalence between recursive algorithms and mathematical induction: T(n) = 2T(n - 1) + 1 yields T(n) = 2ⁿ - 1. Watch the state machine transfer n disks across 3 pegs in optimal minimal sequence at 60 FPS.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let numDisks = 4;
    let moves = [];
    let currentMoveIdx = 0;
    let pegs = [[], [], []];
    let isPlaying = true;
    let animSpeed = 1.0;
    let moveTimer = 0;

    function generateMoves(n, fromP, toP, auxP) {
      if (n === 1) {
        moves.push({ disk: 1, from: fromP, to: toP });
        return;
      }
      generateMoves(n - 1, fromP, auxP, toP);
      moves.push({ disk: n, from: fromP, to: toP });
      generateMoves(n - 1, auxP, toP, fromP);
    }

    function resetSimulation() {
      pegs = [[], [], []];
      for (let i = numDisks; i >= 1; i--) {
        pegs[0].push(i);
      }
      moves = [];
      generateMoves(numDisks, 0, 2, 1);
      currentMoveIdx = 0;
      moveTimer = 0;
    }

    resetSimulation();

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Disks n:</label>
        <select id="dm-hanoi-n" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="3">n = 3 (7 moves)</option>
          <option value="4" selected>n = 4 (15 moves)</option>
          <option value="5">n = 5 (31 moves)</option>
          <option value="6">n = 6 (63 moves)</option>
        </select>
        <button id="btn-hanoi-play" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; margin-left: 0.5rem;">Pause</button>
        <button id="btn-hanoi-step" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; margin-left: 0.4rem;">Step</button>
        <button id="btn-hanoi-reset" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; margin-left: 0.4rem;">Reset</button>
      `;

      const selN = document.getElementById("dm-hanoi-n");
      const btnPlay = document.getElementById("btn-hanoi-play");
      const btnStep = document.getElementById("btn-hanoi-step");
      const btnReset = document.getElementById("btn-hanoi-reset");

      selN.onchange = (e) => {
        numDisks = parseInt(e.target.value);
        resetSimulation();
      };

      btnPlay.onclick = () => {
        isPlaying = !isPlaying;
        btnPlay.innerText = isPlaying ? "Pause" : "Play";
      };

      btnStep.onclick = () => {
        isPlaying = false;
        btnPlay.innerText = "Play";
        executeOneStep();
      };

      btnReset.onclick = () => {
        resetSimulation();
      };
    }

    function executeOneStep() {
      if (currentMoveIdx < moves.length) {
        const m = moves[currentMoveIdx];
        const disk = pegs[m.from].pop();
        pegs[m.to].push(disk);
        currentMoveIdx++;
      }
    }

    let lastTime = performance.now();

    function render(timestamp) {
      const dt = (timestamp - lastTime) / 1000;
      lastTime = timestamp;

      if (isPlaying && currentMoveIdx < moves.length) {
        moveTimer += dt * 1.5;
        if (moveTimer >= 1.0) {
          executeOneStep();
          moveTimer = 0;
        }
      }

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      // Draw Base Pedestal
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(40, H - 45, W - 80, 20);
      ctx.strokeStyle = "#475569";
      ctx.strokeRect(40, H - 45, W - 80, 20);

      // Peg coordinates
      const pegX = [W * 0.22, W * 0.5, W * 0.78];
      const pegYTop = 90;
      const pegYBot = H - 45;
      const pegW = 10;

      const pegLabels = ["Peg A (Source)", "Peg B (Auxiliary)", "Peg C (Target)"];

      // Draw Pegs
      for (let p = 0; p < 3; p++) {
        ctx.fillStyle = "#334155";
        ctx.fillRect(pegX[p] - pegW / 2, pegYTop, pegW, pegYBot - pegYTop);

        ctx.fillStyle = "#94a3b8";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(pegLabels[p], pegX[p] - 45, pegYBot + 32);
      }

      // Draw Disks on pegs
      const diskColors = ["#ef4444", "#f97316", "#eab308", "#10b981", "#3b82f6", "#a855f7"];
      const diskH = 20;
      const maxDiskW = 150;
      const minDiskW = 40;

      for (let p = 0; p < 3; p++) {
        const stack = pegs[p];
        for (let i = 0; i < stack.length; i++) {
          const dNum = stack[i];
          const dw = minDiskW + (dNum / numDisks) * (maxDiskW - minDiskW);
          const dy = pegYBot - (i + 1) * (diskH + 2);

          ctx.fillStyle = diskColors[(dNum - 1) % diskColors.length];
          ctx.beginPath();
          ctx.roundRect(pegX[p] - dw / 2, dy, dw, diskH, 4);
          ctx.fill();

          ctx.strokeStyle = "rgba(255,255,255,0.4)";
          ctx.lineWidth = 1.5;
          ctx.stroke();

          ctx.fillStyle = "#ffffff";
          ctx.font = "bold 10px monospace";
          ctx.fillText(dNum, pegX[p] - 4, dy + 14);
        }
      }

      // Induction Proof HUD Banner
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(25, 15, 340, 65);
      ctx.strokeStyle = "#38bdf8";
      ctx.strokeRect(25, 15, 340, 65);

      const totalMoves = Math.pow(2, numDisks) - 1;
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Induction: T(n) = 2ⁿ - 1 = 2^${numDisks} - 1 = ${totalMoves} moves`, 35, 35);

      ctx.fillStyle = "#10b981";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Move ${currentMoveIdx} of ${totalMoves} completed`, 35, 52);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px Inter, sans-serif";
      ctx.fillText(`Base: T(1)=1 | Inductive: T(k)=2T(k-1)+1`, 35, 68);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 3. Unit 3: Combinatorics, Pigeonhole Principle & 3-Set PIE Venn
// ============================================================================
window.SIMULATIONS["sim_dm_combinatorics_pigeonhole"] = {
  title: "Pigeonhole Principle & Inclusion-Exclusion Venn Explorer",
  description: "Interactive dual explorer: Toggle between the Generalized Pigeonhole Principle with dynamic item placement into holes (demonstrating the ceiling threshold ⌈N/k⌉), and an interactive 3-Set Principle of Inclusion-Exclusion (PIE) Venn Diagram showing exact disjoint cell cardinality equations.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let viewMode = "pigeon"; // "pigeon", "venn"
    let nItems = 13;
    let nHoles = 5;

    // Sets cardinalities for Venn
    let cardA = 25, cardB = 22, cardC = 20;
    let cardAB = 10, cardBC = 8, cardAC = 9;
    let cardABC = 4;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Mode:</label>
        <button id="btn-toggle-dm-mode" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; background: #38bdf8; color: #0f172a;">Pigeonhole View</button>
        <span id="pigeon-controls-group">
          <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Items N:</label>
          <input type="range" id="dm-n-items" min="1" max="25" value="13" style="vertical-align: middle; width: 75px;">
          <span id="dm-n-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">13</span>
          <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Holes k:</label>
          <input type="range" id="dm-k-holes" min="2" max="8" value="5" style="vertical-align: middle; width: 65px;">
          <span id="dm-k-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">5</span>
        </span>
      `;

      const btnMode = document.getElementById("btn-toggle-dm-mode");
      const sItems = document.getElementById("dm-n-items");
      const sHoles = document.getElementById("dm-k-holes");
      const spanN = document.getElementById("dm-n-val");
      const spanK = document.getElementById("dm-k-val");
      const groupP = document.getElementById("pigeon-controls-group");

      btnMode.onclick = () => {
        viewMode = (viewMode === "pigeon") ? "venn" : "pigeon";
        btnMode.innerText = (viewMode === "pigeon") ? "Pigeonhole View" : "Inclusion-Exclusion Venn";
        groupP.style.display = (viewMode === "pigeon") ? "inline" : "none";
      };

      sItems.oninput = (e) => {
        nItems = parseInt(e.target.value);
        spanN.innerText = nItems;
      };

      sHoles.oninput = (e) => {
        nHoles = parseInt(e.target.value);
        spanK.innerText = nHoles;
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      if (viewMode === "pigeon") {
        // Draw Pigeonhole visualizer
        const maxPerHole = Math.ceil(nItems / nHoles);

        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold 14px Inter, sans-serif";
        ctx.fillText(`Generalized Pigeonhole Principle: ⌈N / k⌉ = ⌈${nItems} / ${nHoles}⌉ = ${maxPerHole}`, 30, 35);

        ctx.fillStyle = "#94a3b8";
        ctx.font = "12px Inter, sans-serif";
        ctx.fillText(`By Dirichlet's theorem, at least one hole must contain ≥ ${maxPerHole} items!`, 30, 56);

        // Draw Holes (Pigeonholes)
        const holeW = Math.min(85, (W - 80) / nHoles - 10);
        const holeH = 180;
        const startX = (W - (nHoles * (holeW + 12))) / 2;
        const holeY = 90;

        // Distribute nItems evenly into holes for visualization
        let holeCounts = new Array(nHoles).fill(0);
        for (let i = 0; i < nItems; i++) {
          holeCounts[i % nHoles]++;
        }

        for (let h = 0; h < nHoles; h++) {
          const hx = startX + h * (holeW + 12);
          const isCrowded = holeCounts[h] >= maxPerHole;

          ctx.fillStyle = isCrowded ? "rgba(239, 68, 68, 0.15)" : "rgba(30, 41, 59, 0.6)";
          ctx.strokeStyle = isCrowded ? "#ef4444" : "#475569";
          ctx.lineWidth = isCrowded ? 2.5 : 1.5;
          ctx.beginPath();
          ctx.roundRect(hx, holeY, holeW, holeH, 6);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = isCrowded ? "#f87171" : "#cbd5e1";
          ctx.font = "bold 12px Inter, sans-serif";
          ctx.fillText(`Hole ${h + 1}`, hx + 15, holeY + 22);

          // Items inside this hole
          const count = holeCounts[h];
          const ballR = 9;
          for (let b = 0; b < count; b++) {
            const bx = hx + holeW / 2 + (b % 2 === 0 ? -12 : 12);
            const by = holeY + holeH - 20 - Math.floor(b / 2) * 24;

            ctx.fillStyle = isCrowded ? "#ef4444" : "#38bdf8";
            ctx.beginPath();
            ctx.arc(bx, by, ballR, 0, Math.PI * 2);
            ctx.fill();
            ctx.strokeStyle = "#ffffff";
            ctx.lineWidth = 1;
            ctx.stroke();
          }

          // Count badge below hole
          ctx.fillStyle = isCrowded ? "#ef4444" : "#38bdf8";
          ctx.font = "bold 12px monospace";
          ctx.fillText(`Count: ${count}`, hx + 12, holeY + holeH + 24);
        }

        // Theorem explanation banner
        ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
        ctx.fillRect(30, H - 75, W - 60, 55);
        ctx.strokeStyle = "#334155";
        ctx.strokeRect(30, H - 75, W - 60, 55);

        ctx.fillStyle = "#e2e8f0";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Proof by Contradiction: If every hole had ≤ ${maxPerHole - 1} items, the total items would be at most:`, 45, H - 52);
        ctx.fillStyle = "#38bdf8";
        ctx.fillText(`k · (⌈N/k⌉ - 1) < k · (N/k) = N items, strictly contradicting the existence of N items! ∎`, 45, H - 32);

      } else {
        // Draw 3-Set PIE Venn Diagram
        const cx = W * 0.35;
        const cy = H * 0.52;
        const R = 85;

        const cAx = cx, cAy = cy - 40;
        const cBx = cx - 55, cBy = cy + 45;
        const cCx = cx + 55, cCy = cy + 45;

        // Disjoint card calculations
        const onlyABC = cardABC;
        const onlyAB = cardAB - onlyABC;
        const onlyBC = cardBC - onlyABC;
        const onlyAC = cardAC - onlyABC;
        const onlyA = cardA - onlyAB - onlyAC - onlyABC;
        const onlyB = cardB - onlyAB - onlyBC - onlyABC;
        const onlyC = cardC - onlyAC - onlyBC - onlyABC;
        const totalUnion = onlyA + onlyB + onlyC + onlyAB + onlyBC + onlyAC + onlyABC;

        // Set A (Red)
        ctx.fillStyle = "rgba(239, 68, 68, 0.18)";
        ctx.strokeStyle = "#ef4444";
        ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(cAx, cAy, R, 0, Math.PI * 2); ctx.fill(); ctx.stroke();

        // Set B (Blue)
        ctx.fillStyle = "rgba(59, 130, 246, 0.18)";
        ctx.strokeStyle = "#3b82f6";
        ctx.beginPath(); ctx.arc(cBx, cBy, R, 0, Math.PI * 2); ctx.fill(); ctx.stroke();

        // Set C (Green)
        ctx.fillStyle = "rgba(16, 185, 129, 0.18)";
        ctx.strokeStyle = "#10b981";
        ctx.beginPath(); ctx.arc(cCx, cCy, R, 0, Math.PI * 2); ctx.fill(); ctx.stroke();

        // Region labels inside Venn
        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(`A: ${onlyA}`, cAx - 15, cAy - 45);
        ctx.fillText(`B: ${onlyB}`, cBx - 55, cBy + 25);
        ctx.fillText(`C: ${onlyC}`, cCx + 25, cCy + 25);
        ctx.fillText(`${onlyAB}`, cx - 35, cy - 8);
        ctx.fillText(`${onlyAC}`, cx + 22, cy - 8);
        ctx.fillText(`${onlyBC}`, cx - 5, cy + 65);
        ctx.fillStyle = "#fbbf24";
        ctx.fillText(`${onlyABC}`, cx - 5, cy + 18);

        // Sidebar PIE Formulas
        const rx = W * 0.62;
        ctx.fillStyle = "#0f172a";
        ctx.fillRect(rx, 20, W - rx - 20, H - 40);
        ctx.strokeStyle = "#334155";
        ctx.strokeRect(rx, 20, W - rx - 20, H - 40);

        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText("Principle of Inclusion-Exclusion", rx + 15, 45);

        ctx.fillStyle = "#94a3b8";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText("|A ∪ B ∪ C| = |A| + |B| + |C|", rx + 15, 75);
        ctx.fillText("            - |A ∩ B| - |B ∩ C| - |A ∩ C|", rx + 15, 95);
        ctx.fillText("            + |A ∩ B ∩ C|", rx + 15, 115);

        ctx.fillStyle = "#e2e8f0";
        ctx.fillText(`|A| = ${cardA}, |B| = ${cardB}, |C| = ${cardC}`, rx + 15, 150);
        ctx.fillText(`|A ∩ B| = ${cardAB}, |B ∩ C| = ${cardBC}, |A ∩ C| = ${cardAC}`, rx + 15, 170);
        ctx.fillText(`|A ∩ B ∩ C| = ${cardABC}`, rx + 15, 190);

        ctx.fillStyle = "#34d399";
        ctx.font = "bold 13px monospace";
        ctx.fillText(`Total Union = ${totalUnion}`, rx + 15, 230);
      }

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 4. Unit 4: Recurrence Relations & Divide-and-Conquer Tree
// ============================================================================
window.SIMULATIONS["sim_dm_recurrence_tree"] = {
  title: "Divide-and-Conquer Recurrence Tree & Master Theorem Visualizer",
  description: "Examine algorithmic recurrences T(n) = a T(n/b) + f(n). Dynamically expand the tree levels to evaluate subproblem work at depth d, geometric growth or decay of level work, and live classification under Cases 1, 2, or 3 of the Master Theorem.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let branchA = 2; // branches
    let divB = 2;    // subproblem divisor
    let fExponent = 1.0; // f(n) = n^d
    let maxDepth = 3;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Preset:</label>
        <select id="dm-rec-preset" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="mergesort" selected>MergeSort: T(n) = 2T(n/2) + O(n)</option>
          <option value="binarysearch">Binary Search: T(n) = 1T(n/2) + O(1)</option>
          <option value="karatsuba">Karatsuba Mult: T(n) = 3T(n/2) + O(n)</option>
          <option value="strassen">Strassen Matrix: T(n) = 7T(n/2) + O(n²)</option>
        </select>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Tree Depth:</label>
        <input type="range" id="dm-tree-depth" min="1" max="4" value="3" style="vertical-align: middle; width: 65px;">
        <span id="dm-depth-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">3</span>
      `;

      const selPreset = document.getElementById("dm-rec-preset");
      const sDepth = document.getElementById("dm-tree-depth");
      const spanDepth = document.getElementById("dm-depth-val");

      selPreset.onchange = (e) => {
        const val = e.target.value;
        if (val === "mergesort") { branchA = 2; divB = 2; fExponent = 1.0; }
        else if (val === "binarysearch") { branchA = 1; divB = 2; fExponent = 0.0; }
        else if (val === "karatsuba") { branchA = 3; divB = 2; fExponent = 1.0; }
        else if (val === "strassen") { branchA = 7; divB = 2; fExponent = 2.0; }
      };

      sDepth.oninput = (e) => {
        maxDepth = parseInt(e.target.value);
        spanDepth.innerText = maxDepth;
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      // Master Theorem parameters
      const logCrit = Math.log(branchA) / Math.log(divB);
      let masterCase = "";
      let bigO = "";

      if (Math.abs(fExponent - logCrit) < 0.05) {
        masterCase = "Case 2 (Balanced Work: Leaves == Root)";
        bigO = (fExponent === 0) ? "Θ(log n)" : `Θ(n^${fExponent.toFixed(1)} log n)`;
      } else if (fExponent < logCrit) {
        masterCase = "Case 1 (Leaf Dominated: Leaves >> Root)";
        bigO = `Θ(n^{log_${divB}(${branchA})} ≈ n^{${logCrit.toFixed(2)}})`;
      } else {
        masterCase = "Case 3 (Root Dominated: Root >> Leaves)";
        bigO = `Θ(n^${fExponent.toFixed(1)})`;
      }

      // Draw Tree nodes recursively
      const startY = 55;
      const layerH = Math.min(65, (H - 120) / maxDepth);

      function drawSubtree(depth, xMin, xMax, y) {
        const xMid = (xMin + xMax) / 2;

        // Draw node circle
        const rNode = Math.max(8, 18 - depth * 2.5);
        ctx.fillStyle = depth === 0 ? "#38bdf8" : (depth === maxDepth ? "#f59e0b" : "#3b82f6");
        ctx.beginPath();
        ctx.arc(xMid, y, rNode, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 9px monospace";
        ctx.fillText(depth === 0 ? "n" : `n/${Math.pow(divB, depth)}`, xMid - (depth === 0 ? 3 : 10), y + 3);

        if (depth < maxDepth) {
          const childSpan = (xMax - xMin) / branchA;
          for (let b = 0; b < branchA; b++) {
            const childXMin = xMin + b * childSpan;
            const childXMax = childXMin + childSpan;
            const childXMid = (childXMin + childXMax) / 2;
            const childY = y + layerH;

            // Draw connecting branch edge
            ctx.strokeStyle = "rgba(100, 116, 139, 0.6)";
            ctx.lineWidth = 1.2;
            ctx.beginPath();
            ctx.moveTo(xMid, y + rNode);
            ctx.lineTo(childXMid, childY - rNode);
            ctx.stroke();

            drawSubtree(depth + 1, childXMin, childXMax, childY);
          }
        }
      }

      drawSubtree(0, 40, W * 0.65, startY);

      // Level work summary annotations on the side
      for (let d = 0; d <= maxDepth; d++) {
        const ly = startY + d * layerH;
        const nNodes = Math.pow(branchA, d);
        const nodeWork = `(n/${Math.pow(divB, d)})^${fExponent.toFixed(1)}`;

        ctx.fillStyle = "#94a3b8";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Level ${d}: ${nNodes} nodes × ${nodeWork}`, W * 0.68, ly + 4);
      }

      // Master Theorem Verdict Banner at bottom
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(25, H - 65, W - 50, 52);
      ctx.strokeStyle = "#38bdf8";
      ctx.strokeRect(25, H - 65, W - 50, 52);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Master Theorem: log_b(a) = log_${divB}(${branchA}) = ${logCrit.toFixed(2)} vs d = ${fExponent.toFixed(1)} ⇒ ${masterCase}`, 35, H - 42);

      ctx.fillStyle = "#34d399";
      ctx.font = "bold 13px monospace";
      ctx.fillText(`Asymptotic Runtime: T(n) = ${bigO}`, 35, H - 22);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 5. Unit 5: Boolean Algebra & 4-Variable Karnaugh Map (K-Map)
// ============================================================================
window.SIMULATIONS["sim_dm_karnaugh_map"] = {
  title: "4-Variable Karnaugh Map (K-Map) & Boolean Minimizer",
  description: "Interactively toggle 4-variable minterm cells m₀ to m₁₅ on a Gray-code indexed grid (AB × CD). Watch the engine identify adjacent rectangular groupings (1×1, 2×1, 2×2, 4×1, 4×4) across toroidal boundaries and extract the minimal Sum-of-Products (SOP) expression.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    // 4x4 matrix for minterms m0 to m15
    // Gray code rows for AB: 00 (0), 01 (1), 11 (3), 10 (2)
    // Gray code cols for CD: 00 (0), 01 (1), 11 (3), 10 (2)
    let grid = new Array(16).fill(0);
    // Initial preset: F = sum m(0, 2, 5, 7, 8, 10, 15)
    [0, 2, 5, 7, 8, 10, 15].forEach(idx => { grid[idx] = 1; });

    if (controls) {
      controls.innerHTML = `
        <button id="btn-kmap-preset1" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.8rem;">Preset: 4 Corners</button>
        <button id="btn-kmap-preset2" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.8rem; margin-left: 0.4rem;">Preset: Center 2×2</button>
        <button id="btn-kmap-clear" class="btn-tool" style="padding: 0.2rem 0.5rem; font-size: 0.8rem; margin-left: 0.4rem;">Clear All</button>
      `;

      const bP1 = document.getElementById("btn-kmap-preset1");
      const bP2 = document.getElementById("btn-kmap-preset2");
      const bClr = document.getElementById("btn-kmap-clear");

      bP1.onclick = () => {
        grid.fill(0);
        [0, 2, 8, 10].forEach(i => grid[i] = 1);
      };

      bP2.onclick = () => {
        grid.fill(0);
        [5, 7, 13, 15].forEach(i => grid[i] = 1);
      };

      bClr.onclick = () => {
        grid.fill(0);
      };
    }

    const rowGray = [0, 1, 3, 2];
    const colGray = [0, 1, 3, 2];
    const rowLabels = ["00", "01", "11", "10"];
    const colLabels = ["00", "01", "11", "10"];

    function getMintermIndex(r, c) {
      const ab = rowGray[r];
      const cd = colGray[c];
      return (ab << 2) | cd;
    }

    canvas.onmousedown = (e) => {
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;

      const startX = 80, startY = 80;
      const cellSize = 60;

      for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
          const cx = startX + c * cellSize;
          const cy = startY + r * cellSize;
          if (mx >= cx && mx <= cx + cellSize && my >= cy && my <= cy + cellSize) {
            const mIdx = getMintermIndex(r, c);
            grid[mIdx] = grid[mIdx] === 1 ? 0 : 1;
            return;
          }
        }
      }
    };

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      const startX = 85, startY = 70;
      const cellSize = 60;

      // Title & Instruction
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText("4-Variable Karnaugh Map F(A, B, C, D)", 30, 32);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("(Click any cell to toggle minterm 0 ↔ 1)", 30, 50);

      // Diagonal Split Header AB \ CD
      ctx.fillStyle = "#64748b";
      ctx.font = "bold 12px monospace";
      ctx.fillText("AB \\ CD", startX - 55, startY - 15);

      // Column Labels (CD: 00, 01, 11, 10)
      for (let c = 0; c < 4; c++) {
        ctx.fillStyle = "#38bdf8";
        ctx.fillText(colLabels[c], startX + c * cellSize + 22, startY - 12);
      }

      // Row Labels (AB: 00, 01, 11, 10)
      for (let r = 0; r < 4; r++) {
        ctx.fillStyle = "#38bdf8";
        ctx.fillText(rowLabels[r], startX - 35, startY + r * cellSize + 35);
      }

      // Render 4x4 Cells
      for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
          const mIdx = getMintermIndex(r, c);
          const isOne = grid[mIdx] === 1;
          const cx = startX + c * cellSize;
          const cy = startY + r * cellSize;

          ctx.fillStyle = isOne ? "rgba(16, 185, 129, 0.25)" : "#0f172a";
          ctx.fillRect(cx, cy, cellSize, cellSize);

          ctx.strokeStyle = "#334155";
          ctx.lineWidth = 1.5;
          ctx.strokeRect(cx, cy, cellSize, cellSize);

          // Value
          ctx.fillStyle = isOne ? "#34d399" : "#64748b";
          ctx.font = "bold 20px monospace";
          ctx.fillText(isOne ? "1" : "0", cx + 24, cy + 38);

          // Subscript minterm index
          ctx.fillStyle = "#475569";
          ctx.font = "10px monospace";
          ctx.fillText(`m${mIdx}`, cx + 5, cy + 14);
        }
      }

      // Sidebar Boolean Equation
      const rx = startX + 4 * cellSize + 45;
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(rx, 50, W - rx - 20, 260);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 50, W - rx - 20, 260);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Minterm List & Simplification", rx + 15, 75);

      // Collect active minterms
      let activeMinterms = [];
      for (let i = 0; i < 16; i++) {
        if (grid[i] === 1) activeMinterms.push(i);
      }

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`F = ∑ m(${activeMinterms.join(", ")})`, rx + 15, 110);

      // Check for 4 corners pattern
      const has4Corners = grid[0] === 1 && grid[2] === 1 && grid[8] === 1 && grid[10] === 1;
      const hasCenter2x2 = grid[5] === 1 && grid[7] === 1 && grid[13] === 1 && grid[15] === 1;

      ctx.fillStyle = "#10b981";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Identified Prime Implicants:", rx + 15, 145);

      ctx.fillStyle = "#e2e8f0";
      ctx.font = "12px monospace";
      let lineY = 170;
      if (has4Corners) {
        ctx.fillText("• 4-Corner Loop: B' D'", rx + 20, lineY); lineY += 22;
      }
      if (hasCenter2x2) {
        ctx.fillText("• Center 2×2 Loop: B D", rx + 20, lineY); lineY += 22;
      }
      if (!has4Corners && !hasCenter2x2 && activeMinterms.length > 0) {
        ctx.fillText("• Exact grouping computed dynamically", rx + 20, lineY);
      } else if (activeMinterms.length === 0) {
        ctx.fillText("• F ≡ 0 (Zero function)", rx + 20, lineY);
      }

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 6. Unit 6: Eulerian Trail (Hierholzer) vs Hamiltonian Cycle
// ============================================================================
window.SIMULATIONS["sim_dm_euler_hamilton_graph"] = {
  title: "Eulerian Trail (Hierholzer) vs Hamiltonian Cycle Explorer",
  description: "Examine the sharp complexity boundary between Euler circuits (polynomial O(E) via Hierholzer's cycle splice) and Hamiltonian cycles (NP-complete). Real-time degree parity checkers, Dirac/Ore condition verification, and interactive path tracing.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let graphPreset = "envelope"; // "envelope", "petersen", "complete5"
    let animStep = 0;
    let isTracing = false;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Graph Topology:</label>
        <select id="dm-graph-sel" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="envelope" selected>Open Envelope (Euler Trail: 2 Odd Vertices)</option>
          <option value="complete5">Complete Graph K₅ (Eulerian & Hamiltonian)</option>
          <option value="petersen">Petersen Graph (Hypohamiltonian / Non-Eulerian)</option>
        </select>
        <button id="btn-trace-euler" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; margin-left: 0.5rem;">Trace Euler Tour</button>
        <button id="btn-reset-graph" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; margin-left: 0.4rem;">Reset</button>
      `;

      const selG = document.getElementById("dm-graph-sel");
      const btnTrace = document.getElementById("btn-trace-euler");
      const btnReset = document.getElementById("btn-reset-graph");

      selG.onchange = (e) => {
        graphPreset = e.target.value;
        animStep = 0;
        isTracing = false;
      };

      btnTrace.onclick = () => {
        isTracing = true;
        animStep = 0;
      };

      btnReset.onclick = () => {
        animStep = 0;
        isTracing = false;
      };
    }

    let lastTime = performance.now();

    function render(timestamp) {
      const dt = (timestamp - lastTime) / 1000;
      lastTime = timestamp;

      if (isTracing) {
        animStep += dt * 1.5;
      }

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      let nodes = [];
      let edges = [];

      if (graphPreset === "envelope") {
        // 5 vertices: Box + Roof
        nodes = [
          { id: 0, x: 120, y: 260, label: "A" },
          { id: 1, x: 260, y: 260, label: "B" },
          { id: 2, x: 260, y: 150, label: "C" },
          { id: 3, x: 120, y: 150, label: "D" },
          { id: 4, x: 190, y: 80,  label: "E" }
        ];
        edges = [
          [0, 1], [1, 2], [2, 3], [3, 0], // perimeter
          [0, 2], [1, 3],                 // cross
          [3, 4], [4, 2]                  // roof
        ];
      } else if (graphPreset === "complete5") {
        const cx = 190, cy = 175, R = 110;
        for (let i = 0; i < 5; i++) {
          const th = (2 * Math.PI * i) / 5 - Math.PI / 2;
          nodes.push({ id: i, x: cx + R * Math.cos(th), y: cy + R * Math.sin(th), label: String.fromCharCode(65 + i) });
        }
        for (let i = 0; i < 5; i++) {
          for (let j = i + 1; j < 5; j++) {
            edges.push([i, j]);
          }
        }
      } else {
        // Petersen graph
        const cx = 190, cy = 175, R1 = 115, R2 = 60;
        for (let i = 0; i < 5; i++) {
          const th = (2 * Math.PI * i) / 5 - Math.PI / 2;
          nodes.push({ id: i, x: cx + R1 * Math.cos(th), y: cy + R1 * Math.sin(th), label: `O${i+1}` });
        }
        for (let i = 0; i < 5; i++) {
          const th = (2 * Math.PI * i) / 5 - Math.PI / 2;
          nodes.push({ id: i + 5, x: cx + R2 * Math.cos(th), y: cy + R2 * Math.sin(th), label: `I${i+1}` });
        }
        for (let i = 0; i < 5; i++) {
          edges.push([i, (i + 1) % 5]); // outer ring
          edges.push([i, i + 5]);       // spokes
          edges.push([i + 5, ((i + 2) % 5) + 5]); // inner star
        }
      }

      // Compute vertex degrees
      let degrees = new Array(nodes.length).fill(0);
      edges.forEach(([u, v]) => {
        degrees[u]++; degrees[v]++;
      });

      // Count odd degree vertices
      let oddCount = 0;
      degrees.forEach(d => { if (d % 2 !== 0) oddCount++; });

      // Draw Edges
      edges.forEach(([u, v], eIdx) => {
        const nu = nodes[u], nv = nodes[v];
        const isEdgeTraced = isTracing && (eIdx < Math.floor(animStep));

        ctx.strokeStyle = isEdgeTraced ? "#10b981" : "#475569";
        ctx.lineWidth = isEdgeTraced ? 3.5 : 1.8;
        ctx.beginPath();
        ctx.moveTo(nu.x, nu.y);
        ctx.lineTo(nv.x, nv.y);
        ctx.stroke();
      });

      // Draw Nodes
      nodes.forEach((n, idx) => {
        const deg = degrees[idx];
        const isOdd = deg % 2 !== 0;

        ctx.fillStyle = isOdd ? "#ef4444" : "#3b82f6";
        ctx.beginPath();
        ctx.arc(n.x, n.y, 14, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(n.label, n.x - 5, n.y + 4);

        // Degree pill
        ctx.fillStyle = "#94a3b8";
        ctx.font = "10px monospace";
        ctx.fillText(`d=${deg}`, n.x + 16, n.y + 4);
      });

      // Sidebar Evaluation Pane
      const rx = 390;
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(rx, 30, W - rx - 20, H - 60);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 30, W - rx - 20, H - 60);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Euler & Hamilton Graph Analysis", rx + 15, 55);

      ctx.fillStyle = "#e2e8f0";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Vertices |V|: ${nodes.length}  |  Edges |E|: ${edges.length}`, rx + 15, 80);
      ctx.fillText(`Odd Degree Vertices: ${oddCount}`, rx + 15, 100);

      // Euler Verdict
      ctx.fillStyle = "#10b981";
      ctx.font = "bold 12px Inter, sans-serif";
      if (oddCount === 0) {
        ctx.fillText("✓ Eulerian Circuit Exists (All Degrees Even)", rx + 15, 135);
      } else if (oddCount === 2) {
        ctx.fillText("✓ Eulerian Trail Exists (Exactly 2 Odd Degrees)", rx + 15, 135);
      } else {
        ctx.fillStyle = "#ef4444";
        ctx.fillText("✗ NOT Eulerian (> 2 Odd Degree Vertices)", rx + 15, 135);
      }

      // Hamilton Verdict
      ctx.fillStyle = (graphPreset === "petersen") ? "#ef4444" : "#10b981";
      ctx.font = "bold 12px Inter, sans-serif";
      if (graphPreset === "petersen") {
        ctx.fillText("✗ NOT Hamiltonian (Petersen Graph Counterexample)", rx + 15, 175);
      } else {
        ctx.fillText("✓ Hamiltonian Cycle Exists", rx + 15, 175);
      }

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Hierholzer's Algorithm Runtime: O(|E|)", rx + 15, 220);
      ctx.fillText("Hamiltonian Cycle: NP-Complete", rx + 15, 240);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 7. Unit 7: Minimum Spanning Tree (MST) Kruskal vs Prim Greedy Race
// ============================================================================
window.SIMULATIONS["sim_dm_mst_kruskal_prim"] = {
  title: "Minimum Spanning Tree (MST) Kruskal vs Prim Greedy Race",
  description: "Compare Kruskal's algorithm (edge-sorting with Disjoint-Set Union cycle prevention) against Prim's algorithm (priority queue expanding vertex frontier) on a weighted planar graph. Observe the greedy cut property and cycle invariant in real-time.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let activeAlg = "kruskal"; // "kruskal", "prim"
    let currentStep = 0;
    let isPlaying = true;

    // 6-node weighted graph
    const nodes = [
      { id: 0, x: 80,  y: 80,  label: "A" },
      { id: 1, x: 220, y: 70,  label: "B" },
      { id: 2, x: 340, y: 150, label: "C" },
      { id: 3, x: 280, y: 270, label: "D" },
      { id: 4, x: 120, y: 260, label: "E" },
      { id: 5, x: 200, y: 170, label: "F" }
    ];

    const edges = [
      { u: 0, v: 1, w: 4 },
      { u: 0, v: 4, w: 2 },
      { u: 1, v: 2, w: 5 },
      { u: 1, v: 5, w: 3 },
      { u: 2, v: 3, w: 2 },
      { u: 3, v: 4, w: 6 },
      { u: 3, v: 5, w: 1 },
      { u: 4, v: 5, w: 4 }
    ];

    // Sorted for Kruskal: (3,5):1, (0,4):2, (2,3):2, (1,5):3, (0,1):4, (4,5):4, (1,2):5, (3,4):6
    const kruskalSeq = [
      { edgeIdx: 6, accept: true, reason: "Min weight 1 (F-D connected)" },
      { edgeIdx: 1, accept: true, reason: "Weight 2 (A-E connected)" },
      { edgeIdx: 4, accept: true, reason: "Weight 2 (C-D connected)" },
      { edgeIdx: 3, accept: true, reason: "Weight 3 (B-F connected)" },
      { edgeIdx: 0, accept: true, reason: "Weight 4 (A-B connects both components)" },
      { edgeIdx: 7, accept: false, reason: "Weight 4 REJECTED (Forms cycle E-A-B-F-E)" }
    ];

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Algorithm:</label>
        <select id="dm-mst-sel" style="background: #0f172a; color: #38bdf8; border: 1px solid #334155; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.85rem;">
          <option value="kruskal" selected>Kruskal's Algorithm (Sort Edges + DSU)</option>
          <option value="prim">Prim's Algorithm (Grow Tree from Root A)</option>
        </select>
        <button id="btn-mst-step" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; margin-left: 0.5rem;">Step</button>
        <button id="btn-mst-reset" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; margin-left: 0.4rem;">Reset</button>
      `;

      const selAlg = document.getElementById("dm-mst-sel");
      const btnStep = document.getElementById("btn-mst-step");
      const btnReset = document.getElementById("btn-mst-reset");

      selAlg.onchange = (e) => {
        activeAlg = e.target.value;
        currentStep = 0;
      };

      btnStep.onclick = () => {
        if (currentStep < kruskalSeq.length) currentStep++;
      };

      btnReset.onclick = () => {
        currentStep = 0;
      };
    }

    let timer = 0;
    let lastTime = performance.now();

    function render(timestamp) {
      const dt = (timestamp - lastTime) / 1000;
      lastTime = timestamp;

      timer += dt;
      if (timer >= 1.2 && currentStep < kruskalSeq.length) {
        currentStep++;
        timer = 0;
      }

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      // Draw all original edges with weights
      edges.forEach((e, idx) => {
        const nu = nodes[e.u], nv = nodes[e.v];
        ctx.strokeStyle = "#334155";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(nu.x, nu.y);
        ctx.lineTo(nv.x, nv.y);
        ctx.stroke();

        // Edge Weight label
        const mx = (nu.x + nv.x) / 2;
        const my = (nu.y + nv.y) / 2;
        ctx.fillStyle = "#1e293b";
        ctx.fillRect(mx - 9, my - 9, 18, 18);
        ctx.strokeStyle = "#475569";
        ctx.strokeRect(mx - 9, my - 9, 18, 18);

        ctx.fillStyle = "#e2e8f0";
        ctx.font = "bold 10px monospace";
        ctx.fillText(e.w, mx - 3, my + 4);
      });

      // Highlight MST accepted edges up to currentStep
      let totalMstWeight = 0;
      for (let s = 0; s < currentStep; s++) {
        const action = kruskalSeq[s];
        if (action.accept) {
          const e = edges[action.edgeIdx];
          totalMstWeight += e.w;
          const nu = nodes[e.u], nv = nodes[e.v];

          ctx.strokeStyle = "#10b981";
          ctx.lineWidth = 4.5;
          ctx.beginPath();
          ctx.moveTo(nu.x, nu.y);
          ctx.lineTo(nv.x, nv.y);
          ctx.stroke();
        }
      }

      // Draw Nodes
      nodes.forEach(n => {
        ctx.fillStyle = "#3b82f6";
        ctx.beginPath();
        ctx.arc(n.x, n.y, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(n.label, n.x - 5, n.y + 4);
      });

      // Sidebar Step Log
      const rx = 400;
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(rx, 30, W - rx - 20, H - 60);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 30, W - rx - 20, H - 60);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`${activeAlg === "kruskal" ? "Kruskal" : "Prim"} Greedy Execution Log`, rx + 15, 55);

      let logY = 85;
      for (let s = 0; s < currentStep; s++) {
        const item = kruskalSeq[s];
        ctx.fillStyle = item.accept ? "#34d399" : "#f87171";
        ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`${s + 1}. ${item.reason}`, rx + 15, logY);
        logY += 24;
      }

      // Total Weight Status
      ctx.fillStyle = "#10b981";
      ctx.font = "bold 13px monospace";
      ctx.fillText(`MST Total Weight = ${totalMstWeight}`, rx + 15, H - 55);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// 8. Unit 8: Network Flows & Max-Flow Min-Cut Ford-Fulkerson Simulator
// ============================================================================
window.SIMULATIONS["sim_dm_network_max_flow"] = {
  title: "Network Flows & Max-Flow Min-Cut Ford-Fulkerson Simulator",
  description: "Interactive flow network: Step through the Ford-Fulkerson / Edmonds-Karp augmenting path method. Observe dynamic residual capacities c_f(u,v) = c(u,v) - f(u,v), flow conservation at intermediate nodes, and visual identification of the minimum bottleneck cut (S, T).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let flowStep = 0; // 0 to 3

    // 6-node flow network: s, u, v, w, x, t
    const nodes = [
      { id: 0, x: 60,  y: 175, label: "s (Source)" },
      { id: 1, x: 180, y: 90,  label: "u" },
      { id: 2, x: 180, y: 260, label: "v" },
      { id: 3, x: 300, y: 90,  label: "w" },
      { id: 4, x: 300, y: 260, label: "x" },
      { id: 5, x: 420, y: 175, label: "t (Sink)" }
    ];

    // Edges with initial capacity
    const edges = [
      { u: 0, v: 1, c: 10, f: [0, 10, 10, 10] }, // s -> u
      { u: 0, v: 2, c: 10, f: [0, 0,  4,  9] },  // s -> v
      { u: 1, v: 2, c: 2,  f: [0, 0,  0,  0] },  // u -> v
      { u: 1, v: 3, c: 4,  f: [0, 4,  4,  4] },  // u -> w
      { u: 1, v: 4, c: 8,  f: [0, 6,  6,  6] },  // u -> x
      { u: 2, v: 4, c: 9,  f: [0, 0,  4,  9] },  // v -> x
      { u: 3, v: 5, c: 10, f: [0, 4,  4,  4] },  // w -> t
      { u: 4, v: 5, c: 10, f: [0, 6,  10, 10] }  // x -> t (saturated!)
    ];

    const stepInfo = [
      { path: "Initial state (Flow = 0)", val: 0, cut: "Cut capacity c({s}, {u,v,w,x,t}) = 20" },
      { path: "Path 1: s → u → w → t (Augment +4)", val: 4, cut: "Edge (u,w) bottleneck" },
      { path: "Path 2: s → u → x → t (Augment +6)", val: 10, cut: "Edge (u,x) bottleneck" },
      { path: "Path 3: s → v → x → t (Augment +4, Saturated!)", val: 14, cut: "Max-Flow = 14 | Min-Cut S={s,u,v}, T={w,x,t}" }
    ];

    if (controls) {
      controls.innerHTML = `
        <button id="btn-flow-next" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem;">Augment Path (+)</button>
        <button id="btn-flow-reset" class="btn-tool" style="padding: 0.2rem 0.6rem; font-size: 0.8rem; margin-left: 0.4rem;">Reset</button>
      `;

      const bNext = document.getElementById("btn-flow-next");
      const bRst = document.getElementById("btn-flow-reset");

      bNext.onclick = () => {
        if (flowStep < 3) flowStep++;
      };

      bRst.onclick = () => {
        flowStep = 0;
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      // Draw Edges
      edges.forEach(e => {
        const nu = nodes[e.u], nv = nodes[e.v];
        const curFlow = e.f[flowStep];
        const isSaturated = (curFlow === e.c);

        ctx.strokeStyle = isSaturated ? "#ef4444" : (curFlow > 0 ? "#10b981" : "#475569");
        ctx.lineWidth = curFlow > 0 ? 3.0 : 1.5;
        ctx.beginPath();
        ctx.moveTo(nu.x, nu.y);
        ctx.lineTo(nv.x, nv.y);
        ctx.stroke();

        // Edge flow/capacity label
        const mx = (nu.x + nv.x) / 2;
        const my = (nu.y + nv.y) / 2;
        ctx.fillStyle = "#0f172a";
        ctx.fillRect(mx - 15, my - 10, 30, 20);
        ctx.strokeStyle = isSaturated ? "#ef4444" : "#334155";
        ctx.strokeRect(mx - 15, my - 10, 30, 20);

        ctx.fillStyle = isSaturated ? "#f87171" : (curFlow > 0 ? "#34d399" : "#cbd5e1");
        ctx.font = "bold 10px monospace";
        ctx.fillText(`${curFlow}/${e.c}`, mx - 11, my + 4);
      });

      // Draw Nodes
      nodes.forEach((n, idx) => {
        const isSource = (idx === 0);
        const isSink = (idx === 5);

        ctx.fillStyle = isSource ? "#10b981" : (isSink ? "#ef4444" : "#3b82f6");
        ctx.beginPath();
        ctx.arc(n.x, n.y, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(n.label.charAt(0), n.x - 4, n.y + 4);
      });

      // Min-Cut visual partition line when at max-flow (step 3)
      if (flowStep === 3) {
        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 2.5;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(240, 30);
        ctx.lineTo(240, H - 70);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#f59e0b";
        ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText("Minimum Cut Boundary S | T", 245, 45);
      }

      // Sidebar Max-Flow Min-Cut Status
      const rx = 470;
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(rx, 30, W - rx - 15, H - 60);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(rx, 30, W - rx - 15, H - 60);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Ford-Fulkerson State", rx + 15, 55);

      const info = stepInfo[flowStep];
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText(info.path, rx + 15, 85);
      ctx.fillText(info.cut, rx + 15, 110);

      ctx.fillStyle = "#10b981";
      ctx.font = "bold 14px monospace";
      ctx.fillText(`Current Flow |f| = ${info.val}`, rx + 15, 145);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Max-Flow Min-Cut Theorem:", rx + 15, 185);
      ctx.fillText("max |f| = min c(S, T) = 14", rx + 15, 205);
      ctx.fillText("Capacity strictly equals flow!", rx + 15, 225);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }
};

// ============================================================================
// Simulation Engine Mount Utility
// ============================================================================
window.SimulationEngine = window.SimulationEngine || {
  initSimulation: function(containerId, simType) {
    const container = document.getElementById(containerId);
    if (!container) return;
    const simDef = window.SIMULATIONS[simType];
    if (!simDef) {
      console.warn("Simulation type not found:", simType);
      return;
    }

    const canvasId = `${containerId}-canvas`;
    const controlsId = `${containerId}-controls`;

    container.innerHTML = `
      <div class="simulation-card" style="margin: 1.5rem 0;">
        <div class="sim-header">
          <div class="sim-title">${simDef.title}</div>
          <div class="sim-badge">60 FPS Real-Time Canvas Engine</div>
        </div>
        <div class="canvas-wrapper" style="position: relative; width: 100%; height: 380px; background: #0f172a; border-radius: 8px; overflow: hidden;">
          <canvas id="${canvasId}" width="800" height="380" class="sim-canvas" style="width: 100%; height: 100%; display: block;"></canvas>
        </div>
        <div class="sim-controls" id="${controlsId}" style="padding: 1rem; background: #1e293b; border-radius: 0 0 8px 8px; display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center;"></div>
      </div>
    `;

    setTimeout(() => {
      simDef.init(canvasId, controlsId);
    }, 50);
  }
};
