// Real Analysis Interactive Simulation Suite (60 FPS Canvas)
// Integrated with OpenSTEM Simulation Engine & Textbook Controllers

window.SIMULATIONS = window.SIMULATIONS || {};
window.SimulationEngine = window.SimulationEngine || {};

// 1. Unit 1: Dedekind Cuts, Infimum & Supremum Completeness Explorer
window.SIMULATIONS["sim_ra_dedekind_completeness"] = {
  title: "Dedekind Cuts, Supremum Principle & Completeness of Real Numbers",
  description: "Examine how Dedekind cuts partition the rational line Q, demonstrating the gap at irrational numbers like sqrt(2) and how the Supremum Axiom establishes the complete continuum R.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let cutValue = Math.SQRT2;
    let epsilon = 0.25;
    let isIrrational = true;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Cut Point c:</label>
        <button id="ra-btn-sqrt2" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">c = √2 (Irrational)</button>
        <button id="ra-btn-half" style="padding: 0.35rem 0.75rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer;">c = 1.5 (Rational)</button>
        <button id="ra-btn-pi" style="padding: 0.35rem 0.75rem; background: #8b5cf6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">c = e ≈ 2.718</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">ε-Window:</label>
        <input type="range" id="ra-slider-eps" min="0.05" max="0.6" step="0.05" value="0.25" style="vertical-align: middle; width: 100px;">
        <span id="ra-eps-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">ε = 0.25</span>
      `;

      document.getElementById("ra-btn-sqrt2").onclick = () => { cutValue = Math.SQRT2; isIrrational = true; render(); };
      document.getElementById("ra-btn-half").onclick = () => { cutValue = 1.5; isIrrational = false; render(); };
      document.getElementById("ra-btn-pi").onclick = () => { cutValue = Math.E; isIrrational = true; render(); };
      const epsSlider = document.getElementById("ra-slider-eps");
      epsSlider.oninput = (e) => {
        epsilon = parseFloat(e.target.value);
        document.getElementById("ra-eps-val").innerText = `ε = ${epsilon.toFixed(2)}`;
        render();
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      // Coordinate mapping for real line x in [-0.5, 4.0]
      const xMin = -0.5, xMax = 4.0;
      const toPx = (x) => 60 + ((x - xMin) / (xMax - xMin)) * (W - 120);
      const axisY = H / 2 + 10;

      // Background grid
      ctx.strokeStyle = "rgba(255,255,255,0.06)";
      ctx.lineWidth = 1;
      for (let x = 0; x <= 4; x += 0.5) {
        let px = toPx(x);
        ctx.beginPath(); ctx.moveTo(px, 40); ctx.lineTo(px, H - 40); ctx.stroke();
      }

      // Cut lower class A: {x in Q : x < c}
      let cutPx = toPx(cutValue);
      ctx.fillStyle = "rgba(56, 189, 248, 0.18)";
      ctx.fillRect(toPx(xMin), axisY - 45, cutPx - toPx(xMin), 90);

      // Cut upper class B: {x in Q : x > c}
      ctx.fillStyle = "rgba(236, 72, 153, 0.15)";
      ctx.fillRect(cutPx, axisY - 45, toPx(xMax) - cutPx, 90);

      // Epsilon neighborhood (c - eps, c]
      let epsLeftPx = toPx(cutValue - epsilon);
      ctx.fillStyle = "rgba(234, 179, 8, 0.25)";
      ctx.fillRect(epsLeftPx, axisY - 35, cutPx - epsLeftPx, 70);
      ctx.strokeStyle = "#eab308";
      ctx.setLineDash([4, 4]);
      ctx.strokeRect(epsLeftPx, axisY - 35, cutPx - epsLeftPx, 70);
      ctx.setLineDash([]);

      // Draw Main Number Line
      ctx.strokeStyle = "#cbd5e1";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(toPx(xMin), axisY);
      ctx.lineTo(toPx(xMax), axisY);
      ctx.stroke();

      // Axis Ticks
      for (let x = 0; x <= 4; x += 1) {
        let px = toPx(x);
        ctx.beginPath(); ctx.moveTo(px, axisY - 8); ctx.lineTo(px, axisY + 8); ctx.stroke();
        ctx.fillStyle = "#94a3b8";
        ctx.font = "12px 'Inter', sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(x.toString(), px, axisY + 24);
      }

      // Scatter sample rational points in A and B
      const sampleQ = [-0.2, 0.1, 0.33, 0.5, 0.75, 1.0, 1.25, 1.33, 1.4, 1.41, 1.414, 1.5, 1.75, 2.0, 2.25, 2.5, 2.71, 3.0, 3.25, 3.5, 3.8];
      sampleQ.forEach(q => {
        if (q < cutValue) {
          ctx.fillStyle = "#38bdf8";
        } else {
          ctx.fillStyle = "#f43f5e";
        }
        ctx.beginPath();
        ctx.arc(toPx(q), axisY, 3, 0, Math.PI * 2);
        ctx.fill();
      });

      // Draw Cut Boundary Marker
      ctx.strokeStyle = isIrrational ? "#f59e0b" : "#10b981";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(cutPx, axisY - 55);
      ctx.lineTo(cutPx, axisY + 55);
      ctx.stroke();

      ctx.fillStyle = isIrrational ? "#f59e0b" : "#10b981";
      ctx.beginPath();
      ctx.arc(cutPx, axisY, 6, 0, Math.PI * 2);
      ctx.fill();

      // Labels and Math Annotations
      ctx.textAlign = "left";
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.fillText("Lower Cut Set A = {q ∈ ℚ : q < c}", 70, axisY - 60);

      ctx.fillStyle = "#f43f5e";
      ctx.textAlign = "right";
      ctx.fillText("Upper Cut Set B = {q ∈ ℚ : q > c}", W - 70, axisY - 60);

      // Cut Value Badge
      ctx.fillStyle = "#f8fafc";
      ctx.font = "bold 14px 'Fira Code', monospace";
      ctx.textAlign = "center";
      ctx.fillText(`c = sup(A) = ${cutValue.toFixed(4)}`, cutPx, axisY - 68);

      ctx.fillStyle = isIrrational ? "#fbbf24" : "#34d399";
      ctx.font = "12px 'Inter', sans-serif";
      ctx.fillText(isIrrational ? "Dedekind Gap in ℚ! Closed by ℝ Completeness Axiom." : "Rational Cut: c ∈ ℚ (No gap)", cutPx, axisY + 50);

      // Epsilon supremum condition note
      ctx.fillStyle = "#eab308";
      ctx.font = "11px 'Fira Code', monospace";
      ctx.fillText(`Supremum Principle: ∃ a ∈ A such that a > sup(A) - ε`, W / 2, H - 20);
    }

    render();
  }
};

// 2. Unit 2: Heine-Borel Theorem & Open Cover Reduction Simulator
window.SIMULATIONS["sim_ra_topology_heine_borel"] = {
  title: "Heine-Borel Compactness & Finite Subcover Extractor",
  description: "Explore the topological compactness of [a, b]: every open cover of a closed bounded interval admits a finite subcover, while non-compact sets like (0, 1) or [0, infinity) fail.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let setType = "compact"; // compact [0, 1], open (0, 1), unbounded [0, inf)
    let extracted = false;
    let coverCount = 18;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Set Topology:</label>
        <button id="ra-btn-comp" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">[0, 1] Compact (Closed & Bounded)</button>
        <button id="ra-btn-open" style="padding: 0.35rem 0.75rem; background: #64748b; color: #fff; border: none; border-radius: 4px; cursor: pointer;">(0, 1) Open (Not Compact)</button>
        <button id="ra-btn-unb" style="padding: 0.35rem 0.75rem; background: #64748b; color: #fff; border: none; border-radius: 4px; cursor: pointer;">[0, ∞) Unbounded (Not Compact)</button>
        <button id="ra-btn-subcover" style="padding: 0.35rem 0.75rem; background: #10b981; color: #fff; border: none; border-radius: 4px; cursor: pointer; margin-left: 0.5rem;">⚡ Extract Finite Subcover</button>
      `;

      document.getElementById("ra-btn-comp").onclick = () => {
        setType = "compact"; extracted = false;
        highlightBtn("ra-btn-comp"); render();
      };
      document.getElementById("ra-btn-open").onclick = () => {
        setType = "open"; extracted = false;
        highlightBtn("ra-btn-open"); render();
      };
      document.getElementById("ra-btn-unb").onclick = () => {
        setType = "unbounded"; extracted = false;
        highlightBtn("ra-btn-unb"); render();
      };
      document.getElementById("ra-btn-subcover").onclick = () => {
        extracted = true; render();
      };

      function highlightBtn(id) {
        ["ra-btn-comp", "ra-btn-open", "ra-btn-unb"].forEach(b => {
          document.getElementById(b).style.background = (b === id) ? "#3b82f6" : "#64748b";
        });
      }
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const axisY = H - 70;

      // Coordinate system x in [-0.2, 1.4]
      const toPx = (x) => 80 + (x / 1.3) * (W - 160);

      // Draw Main Real Axis
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(40, axisY);
      ctx.lineTo(W - 40, axisY);
      ctx.stroke();

      // Draw Set S
      let sStart = 0, sEnd = 1.0;
      let px0 = toPx(sStart), px1 = toPx(sEnd);

      if (setType === "compact") {
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 6;
        ctx.beginPath(); ctx.moveTo(px0, axisY); ctx.lineTo(px1, axisY); ctx.stroke();
        // Solid endpoints
        ctx.fillStyle = "#38bdf8";
        ctx.beginPath(); ctx.arc(px0, axisY, 7, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.arc(px1, axisY, 7, 0, Math.PI * 2); ctx.fill();
      } else if (setType === "open") {
        ctx.strokeStyle = "#f43f5e";
        ctx.lineWidth = 6;
        ctx.beginPath(); ctx.moveTo(px0, axisY); ctx.lineTo(px1, axisY); ctx.stroke();
        // Hollow endpoints
        ctx.strokeStyle = "#f43f5e"; ctx.fillStyle = "#0f172a"; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.arc(px0, axisY, 6, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
        ctx.beginPath(); ctx.arc(px1, axisY, 6, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
      } else {
        // Unbounded [0, inf)
        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 6;
        ctx.beginPath(); ctx.moveTo(px0, axisY); ctx.lineTo(W - 50, axisY); ctx.stroke();
        ctx.fillStyle = "#f59e0b";
        ctx.beginPath(); ctx.arc(px0, axisY, 7, 0, Math.PI * 2); ctx.fill();
      }

      // Draw Numbers
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px 'Inter', sans-serif"; ctx.textAlign = "center";
      ctx.fillText("0", px0, axisY + 22);
      ctx.fillText("1", px1, axisY + 22);

      // Generate Open Cover Intervals
      let intervals = [];
      if (setType === "compact") {
        for (let i = 0; i < coverCount; i++) {
          let center = -0.05 + (i / (coverCount - 1)) * 1.1;
          let rad = 0.12 + ((i * 7) % 5) * 0.02;
          intervals.push({ a: center - rad, b: center + rad, kept: (i % 3 === 0 || i === coverCount - 1) });
        }
      } else if (setType === "open") {
        // Cover for (0, 1): I_n = (1/n, 1) as n -> infty
        for (let n = 2; n <= 18; n++) {
          intervals.push({ a: 1.0 / n, b: 1.0, kept: true });
        }
      } else {
        // Cover for [0, inf): I_n = (-1, n)
        for (let n = 1; n <= 12; n++) {
          intervals.push({ a: -0.1, b: n * 0.15, kept: true });
        }
      }

      // Render Intervals in Stacked Rows
      intervals.forEach((iv, idx) => {
        let isKept = !extracted || (setType === "compact" && iv.kept);
        if (extracted && setType !== "compact") isKept = true; // cannot reduce!

        let rowY = 50 + (idx % 6) * 35;
        let leftPx = toPx(Math.max(-0.2, iv.a));
        let rightPx = toPx(Math.min(1.3, iv.b));

        ctx.strokeStyle = isKept ? (setType === "compact" ? "#34d399" : "#fb7185") : "rgba(148, 163, 184, 0.2)";
        ctx.lineWidth = isKept ? 2.5 : 1;
        ctx.fillStyle = isKept ? (setType === "compact" ? "rgba(52, 211, 153, 0.15)" : "rgba(251, 113, 133, 0.15)") : "rgba(255, 255, 255, 0.02)";

        ctx.beginPath();
        ctx.roundRect ? ctx.roundRect(leftPx, rowY - 10, rightPx - leftPx, 20, 4) : ctx.rect(leftPx, rowY - 10, rightPx - leftPx, 20);
        ctx.fill();
        ctx.stroke();

        if (isKept) {
          ctx.fillStyle = setType === "compact" ? "#34d399" : "#fb7185";
          ctx.font = "10px 'Fira Code', monospace";
          ctx.textAlign = "center";
          ctx.fillText(`U_${idx+1}`, (leftPx + rightPx) / 2, rowY + 4);
        }
      });

      // Status info text
      ctx.textAlign = "left";
      ctx.font = "bold 13px 'Inter', sans-serif";
      if (setType === "compact") {
        ctx.fillStyle = "#38bdf8";
        ctx.fillText("Heine-Borel Theorem Holds: K = [0, 1] is Closed & Bounded.", 40, 30);
        ctx.fillStyle = extracted ? "#34d399" : "#94a3b8";
        ctx.fillText(extracted ? `✓ Success: Reduced from ${coverCount} open sets to a Finite Subcover of 6 sets!` : `Infinite/Dense Open Cover active (${coverCount} sets). Click 'Extract Finite Subcover'.`, 40, 260);
      } else if (setType === "open") {
        ctx.fillStyle = "#f43f5e";
        ctx.fillText("Non-Compact: S = (0, 1) is not closed (missing endpoints 0 and 1).", 40, 30);
        ctx.fillStyle = "#fb7185";
        ctx.fillText(extracted ? "❌ Violation: Open cover {(1/n, 1) : n >= 2} has NO finite subcover! (1/N -> 0 as N -> ∞)" : "Cover: {(1/n, 1) : n >= 2}. As x -> 0, infinitely many sets required.", 40, 260);
      } else {
        ctx.fillStyle = "#f59e0b";
        ctx.fillText("Non-Compact: S = [0, ∞) is not bounded.", 40, 30);
        ctx.fillStyle = "#fbbf24";
        ctx.fillText(extracted ? "❌ Violation: Cover {(-1, n) : n in N} has NO finite subcover! (Max finite set n_k < ∞)." : "Cover: {(-1, n) : n in N}. Unbounded growth requires infinitely many sets.", 40, 260);
      }
    }

    render();
  }
};

// 3. Unit 3: Sequence Convergence, Limsup/Liminf & Cauchy Criterion
window.SIMULATIONS["sim_ra_sequence_cauchy"] = {
  title: "Sequence Orbit, Limsup / Liminf Envelopes & Cauchy Criterion",
  description: "Visualize the trajectory of real sequences x_n, monitor running suprema and infima to compute limsup and liminf, and test the Cauchy criterion |x_n - x_m| < eps.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let seqChoice = "osc"; // osc, harmonic, alternating
    let epsilon = 0.25;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Sequence x_n:</label>
        <button id="ra-seq-osc" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">x_n = (-1)^n(1 + 2/n)</button>
        <button id="ra-seq-harm" style="padding: 0.35rem 0.75rem; background: #64748b; color: #fff; border: none; border-radius: 4px; cursor: pointer;">x_n = 1 + 1/n (Convergent)</button>
        <button id="ra-seq-sin" style="padding: 0.35rem 0.75rem; background: #64748b; color: #fff; border: none; border-radius: 4px; cursor: pointer;">x_n = sin(n)</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Cauchy ε:</label>
        <input type="range" id="ra-slider-seq-eps" min="0.1" max="0.8" step="0.05" value="0.25" style="vertical-align: middle; width: 100px;">
        <span id="ra-seq-eps-text" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">ε = 0.25</span>
      `;

      document.getElementById("ra-seq-osc").onclick = () => { seqChoice = "osc"; highlight("ra-seq-osc"); render(); };
      document.getElementById("ra-seq-harm").onclick = () => { seqChoice = "harmonic"; highlight("ra-seq-harm"); render(); };
      document.getElementById("ra-seq-sin").onclick = () => { seqChoice = "sin"; highlight("ra-seq-sin"); render(); };
      document.getElementById("ra-slider-seq-eps").oninput = (e) => {
        epsilon = parseFloat(e.target.value);
        document.getElementById("ra-seq-eps-text").innerText = `ε = ${epsilon.toFixed(2)}`;
        render();
      };

      function highlight(id) {
        ["ra-seq-osc", "ra-seq-harm", "ra-seq-sin"].forEach(b => {
          document.getElementById(b).style.background = (b === id) ? "#3b82f6" : "#64748b";
        });
      }
    }

    function getTerm(n) {
      if (seqChoice === "osc") return Math.pow(-1, n) * (1.0 + 2.0 / n);
      if (seqChoice === "harmonic") return 1.0 + 1.0 / n;
      return Math.sin(n);
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const maxN = 32;

      // Coordinate mapping: n in [1, maxN], y in [-3, 3]
      const toPxX = (n) => 70 + ((n - 1) / (maxN - 1)) * (W - 140);
      const toPxY = (y) => (H / 2) - (y / 3.0) * (H / 2 - 40);

      // Grid Lines
      ctx.strokeStyle = "rgba(255,255,255,0.06)";
      ctx.lineWidth = 1;
      for (let y = -2; y <= 2; y += 1) {
        let py = toPxY(y);
        ctx.beginPath(); ctx.moveTo(60, py); ctx.lineTo(W - 60, py); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px 'Fira Code', monospace"; ctx.textAlign = "right";
        ctx.fillText(y.toFixed(1), 52, py + 4);
      }

      // X-Axis
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(60, toPxY(0)); ctx.lineTo(W - 60, toPxY(0)); ctx.stroke();

      // Compute Terms and Running Envelopes
      let terms = [];
      for (let n = 1; n <= maxN; n++) {
        terms.push({ n: n, val: getTerm(n) });
      }

      let runningSup = [], runningInf = [];
      for (let n = 0; n < maxN; n++) {
        let slice = terms.slice(n).map(t => t.val);
        runningSup.push(Math.max(...slice));
        runningInf.push(Math.min(...slice));
      }

      // Draw Limsup & Liminf Envelopes
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.setLineDash([5, 5]);
      ctx.beginPath();
      runningSup.forEach((v, idx) => {
        let px = toPxX(idx + 1), py = toPxY(v);
        if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();

      ctx.strokeStyle = "#f43f5e";
      ctx.beginPath();
      runningInf.forEach((v, idx) => {
        let px = toPxX(idx + 1), py = toPxY(v);
        if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Sequence Points
      terms.forEach(t => {
        let px = toPxX(t.n), py = toPxY(t.val);
        ctx.strokeStyle = "rgba(255, 255, 255, 0.2)";
        ctx.beginPath(); ctx.moveTo(px, toPxY(0)); ctx.lineTo(px, py); ctx.stroke();

        ctx.fillStyle = "#facc15";
        ctx.beginPath(); ctx.arc(px, py, 4.5, 0, Math.PI * 2); ctx.fill();
      });

      // Annotations for Limsup / Liminf / Cauchy
      let limsup = runningSup[runningSup.length - 1];
      let liminf = runningInf[runningInf.length - 1];
      let isCauchy = Math.abs(limsup - liminf) < 0.05;

      ctx.textAlign = "left"; ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`lim sup(x_n) = ${limsup.toFixed(3)} (Upper Subsequential Limit)`, 70, 30);
      ctx.fillStyle = "#f43f5e";
      ctx.fillText(`lim inf(x_n) = ${liminf.toFixed(3)} (Lower Subsequential Limit)`, 70, 50);

      ctx.fillStyle = isCauchy ? "#34d399" : "#fbbf24";
      ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(isCauchy ? `✓ lim sup = lim inf = ${limsup.toFixed(2)}: Sequence is Convergent & Cauchy!` : `Oscillating: lim sup ≠ lim inf. Sequence Diverges (Non-Cauchy).`, 70, H - 15);
    }

    render();
  }
};

// 4. Unit 4: Infinite Series Convergence Laboratory & Integral Bounds
window.SIMULATIONS["sim_ra_series_convergence"] = {
  title: "Series Convergence Laboratory & Maclaurin-Cauchy Integral Test",
  description: "Analyze the behavior of partial sums S_N, compare terms with the bounding integral f(x)dx, and test the Ratio, Root, and Raabe's criteria.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let seriesType = "p2"; // p2 (p=2), p1 (harmonic), p05 (p=0.5), geom (r=0.5)

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Series ∑ a_n:</label>
        <button id="ra-s-p2" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">∑ 1/n² (p = 2, Converges to π²/6)</button>
        <button id="ra-s-p1" style="padding: 0.35rem 0.75rem; background: #64748b; color: #fff; border: none; border-radius: 4px; cursor: pointer;">∑ 1/n (Harmonic, Diverges)</button>
        <button id="ra-s-geom" style="padding: 0.35rem 0.75rem; background: #64748b; color: #fff; border: none; border-radius: 4px; cursor: pointer;">∑ (0.5)ⁿ (Geometric, r = 0.5)</button>
        <button id="ra-s-alt" style="padding: 0.35rem 0.75rem; background: #64748b; color: #fff; border: none; border-radius: 4px; cursor: pointer;">∑ (-1)ⁿ⁺¹/n (Conditionally Conv)</button>
      `;

      document.getElementById("ra-s-p2").onclick = () => { seriesType = "p2"; highlight("ra-s-p2"); render(); };
      document.getElementById("ra-s-p1").onclick = () => { seriesType = "p1"; highlight("ra-s-p1"); render(); };
      document.getElementById("ra-s-geom").onclick = () => { seriesType = "geom"; highlight("ra-s-geom"); render(); };
      document.getElementById("ra-s-alt").onclick = () => { seriesType = "alt"; highlight("ra-s-alt"); render(); };

      function highlight(id) {
        ["ra-s-p2", "ra-s-p1", "ra-s-geom", "ra-s-alt"].forEach(b => {
          document.getElementById(b).style.background = (b === id) ? "#3b82f6" : "#64748b";
        });
      }
    }

    function getTerm(n) {
      if (seriesType === "p2") return 1.0 / (n * n);
      if (seriesType === "p1") return 1.0 / n;
      if (seriesType === "geom") return Math.pow(0.5, n);
      return Math.pow(-1, n + 1) / n;
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;
      const maxN = 20;

      const toPxX = (n) => 70 + ((n - 1) / (maxN - 1)) * (W - 140);
      const toPxY = (s) => (H - 50) - (s / 4.0) * (H - 100);

      // Compute partial sums
      let partialSums = [];
      let currentS = 0;
      for (let n = 1; n <= maxN; n++) {
        let an = getTerm(n);
        currentS += an;
        partialSums.push({ n: n, an: an, s: currentS });
      }

      // Draw Axis
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(60, H - 50); ctx.lineTo(W - 60, H - 50); ctx.stroke();

      // Draw Term Rectangles (Integral Test visualization)
      partialSums.forEach(p => {
        let px = toPxX(p.n);
        let barW = (W - 140) / maxN * 0.75;
        let barH = (p.an / 4.0) * (H - 100);
        ctx.fillStyle = p.an >= 0 ? "rgba(56, 189, 248, 0.25)" : "rgba(244, 63, 94, 0.25)";
        ctx.strokeStyle = p.an >= 0 ? "#38bdf8" : "#f43f5e";
        ctx.lineWidth = 1.5;
        ctx.fillRect(px - barW / 2, H - 50 - barH, barW, barH);
        ctx.strokeRect(px - barW / 2, H - 50 - barH, barW, barH);
      });

      // Draw Partial Sums Curve
      ctx.strokeStyle = "#34d399"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      partialSums.forEach((p, idx) => {
        let px = toPxX(p.n), py = toPxY(p.s);
        if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();

      partialSums.forEach(p => {
        let px = toPxX(p.n), py = toPxY(p.s);
        ctx.fillStyle = "#34d399";
        ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2); ctx.fill();
      });

      // Summation & Limit line
      if (seriesType === "p2") {
        let sumInf = Math.PI * Math.PI / 6.0;
        let py = toPxY(sumInf);
        ctx.strokeStyle = "#f59e0b"; ctx.setLineDash([6, 6]);
        ctx.beginPath(); ctx.moveTo(60, py); ctx.lineTo(W - 60, py); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#f59e0b"; ctx.font = "12px 'Fira Code', monospace"; ctx.textAlign = "left";
        ctx.fillText(`Limit S = π²/6 ≈ 1.6449`, 70, py - 8);
      } else if (seriesType === "geom") {
        let sumInf = 1.0;
        let py = toPxY(sumInf);
        ctx.strokeStyle = "#f59e0b"; ctx.setLineDash([6, 6]);
        ctx.beginPath(); ctx.moveTo(60, py); ctx.lineTo(W - 60, py); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#f59e0b"; ctx.font = "12px 'Fira Code', monospace"; ctx.textAlign = "left";
        ctx.fillText(`Limit S = a/(1-r) = 1.000`, 70, py - 8);
      }

      // Title & Status
      ctx.textAlign = "left"; ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.fillStyle = "#f8fafc";
      ctx.fillText(`Partial Sums S_N up to N = ${maxN}: Current S_${maxN} = ${currentS.toFixed(4)}`, 70, 30);

      ctx.fillStyle = "#38bdf8"; ctx.font = "12px 'Fira Code', monospace";
      if (seriesType === "p2") ctx.fillText("Integral Test: ∫ 1/x² dx < ∞. Convergent via p-series (p = 2 > 1).", 70, 52);
      else if (seriesType === "p1") ctx.fillText("Integral Test: ∫ 1/x dx = ln(x) -> ∞. Harmonic series Diverges!", 70, 52);
      else if (seriesType === "geom") ctx.fillText("Ratio Test: |a_{n+1}/a_n| = 0.5 < 1. Absolutely Convergent.", 70, 52);
      else ctx.fillText("Leibniz Test: a_n decreases monotonically to 0. Conditionally Convergent.", 70, 52);
    }

    render();
  }
};

// 5. Unit 5: Epsilon-Delta Continuity & Uniform Continuity Explorer
window.SIMULATIONS["sim_ra_continuity_epsilon_delta"] = {
  title: "Epsilon-Delta Continuity & Uniform Continuity Explorer",
  description: "Control target point x0 and tolerance epsilon to dynamically determine the delta window ensuring f((x0-delta, x0+delta)) subset (f(x0)-eps, f(x0)+eps).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let funcType = "sq"; // sq (x^2), inv (1/x)
    let x0 = 1.2;
    let eps = 0.5;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Function f(x):</label>
        <button id="ra-fn-sq" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">f(x) = x²</button>
        <button id="ra-fn-inv" style="padding: 0.35rem 0.75rem; background: #64748b; color: #fff; border: none; border-radius: 4px; cursor: pointer;">f(x) = 1/x (Non-Uniform on (0, 1))</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Target x0:</label>
        <input type="range" id="ra-slider-x0" min="0.3" max="2.0" step="0.1" value="1.2" style="vertical-align: middle; width: 90px;">
        <span id="ra-x0-text" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">x0 = 1.20</span>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">ε-Tolerance:</label>
        <input type="range" id="ra-slider-f-eps" min="0.2" max="1.0" step="0.1" value="0.5" style="vertical-align: middle; width: 90px;">
        <span id="ra-f-eps-text" style="color: #f43f5e; font-family: monospace; font-size: 0.85rem;">ε = 0.50</span>
      `;

      document.getElementById("ra-fn-sq").onclick = () => { funcType = "sq"; highlight("ra-fn-sq"); render(); };
      document.getElementById("ra-fn-inv").onclick = () => { funcType = "inv"; highlight("ra-fn-inv"); render(); };
      document.getElementById("ra-slider-x0").oninput = (e) => {
        x0 = parseFloat(e.target.value);
        document.getElementById("ra-x0-text").innerText = `x0 = ${x0.toFixed(2)}`;
        render();
      };
      document.getElementById("ra-slider-f-eps").oninput = (e) => {
        eps = parseFloat(e.target.value);
        document.getElementById("ra-f-eps-text").innerText = `ε = ${eps.toFixed(2)}`;
        render();
      };

      function highlight(id) {
        ["ra-fn-sq", "ra-fn-inv"].forEach(b => {
          document.getElementById(b).style.background = (b === id) ? "#3b82f6" : "#64748b";
        });
      }
    }

    function f(x) {
      if (funcType === "sq") return x * x;
      return 1.0 / Math.max(0.05, x);
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      // Coordinate mapping: x in [0, 2.5], y in [0, 4.0]
      const toPxX = (x) => 80 + (x / 2.5) * (W - 160);
      const toPxY = (y) => (H - 50) - (y / 4.0) * (H - 90);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(80, H - 50); ctx.lineTo(W - 60, H - 50); // x-axis
      ctx.moveTo(80, H - 50); ctx.lineTo(80, 40); // y-axis
      ctx.stroke();

      // Compute y0 = f(x0)
      let y0 = f(x0);
      let yMin = Math.max(0, y0 - eps);
      let yMax = y0 + eps;

      // Find maximal delta: solve f(x0 + delta) = yMax or f(x0 - delta) = yMin
      let delta = 0.2;
      if (funcType === "sq") {
        let d1 = Math.sqrt(yMax) - x0;
        let d2 = x0 - Math.sqrt(Math.max(0, yMin));
        delta = Math.min(d1, d2);
      } else {
        let d1 = 1.0 / yMin - x0;
        let d2 = x0 - 1.0 / yMax;
        delta = Math.min(d1, d2);
      }
      delta = Math.max(0.02, Math.min(0.6, delta));

      // Draw Epsilon Horizontal Band [y0 - eps, y0 + eps]
      let pyTop = toPxY(yMax);
      let pyBottom = toPxY(yMin);
      ctx.fillStyle = "rgba(244, 63, 94, 0.12)";
      ctx.fillRect(80, pyTop, W - 140, pyBottom - pyTop);
      ctx.strokeStyle = "rgba(244, 63, 94, 0.4)"; ctx.setLineDash([4, 4]);
      ctx.strokeRect(80, pyTop, W - 140, pyBottom - pyTop);
      ctx.setLineDash([]);

      // Draw Delta Vertical Band [x0 - delta, x0 + delta]
      let pxLeft = toPxX(x0 - delta);
      let pxRight = toPxX(x0 + delta);
      ctx.fillStyle = "rgba(56, 189, 248, 0.12)";
      ctx.fillRect(pxLeft, 40, pxRight - pxLeft, H - 90);
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.setLineDash([4, 4]);
      ctx.strokeRect(pxLeft, 40, pxRight - pxLeft, H - 90);
      ctx.setLineDash([]);

      // Draw Function Curve
      ctx.strokeStyle = "#facc15"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let x = 0.1; x <= 2.4; x += 0.02) {
        let px = toPxX(x), py = toPxY(f(x));
        if (py < 40 || py > H - 50) continue;
        if (x === 0.1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Draw Point (x0, y0)
      let p0x = toPxX(x0), p0y = toPxY(y0);
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(p0x, p0y, 6, 0, Math.PI * 2); ctx.fill();

      // Math Labels
      ctx.textAlign = "left"; ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.fillStyle = "#f8fafc";
      ctx.fillText(`Target: x0 = ${x0.toFixed(2)}, f(x0) = ${y0.toFixed(2)}`, 90, 30);

      ctx.fillStyle = "#f43f5e"; ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Epsilon Band: |f(x) - f(x0)| < ${eps.toFixed(2)}`, 90, 50);

      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Maximal Admissible Delta: δ = ${delta.toFixed(3)}`, 90, 70);

      if (funcType === "inv" && x0 < 0.6) {
        ctx.fillStyle = "#f59e0b";
        ctx.fillText("Notice: As x0 -> 0+, δ -> 0! Fails Uniform Continuity on (0, 1).", 90, H - 20);
      } else {
        ctx.fillStyle = "#34d399";
        ctx.fillText("Continuity Verified: |x - x0| < δ ⟹ |f(x) - f(x0)| < ε.", 90, H - 20);
      }
    }

    render();
  }
};

// 6. Unit 6: Mean Value Theorem & Taylor Polynomial Remainder Analyzer
window.SIMULATIONS["sim_ra_mvt_taylor"] = {
  title: "Lagrange Mean Value Theorem & Taylor Remainder Analyzer",
  description: "Interactively explore Rolle's and Lagrange's Mean Value Theorems: find the intermediate point c in (a, b) where f'(c) equals the secant slope (f(b)-f(a))/(b-a).",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let a = -1.2, b = 1.4;

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Left Endpoint a:</label>
        <input type="range" id="ra-slider-a" min="-2.0" max="-0.2" step="0.1" value="-1.2" style="vertical-align: middle; width: 100px;">
        <span id="ra-a-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">a = -1.2</span>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Right Endpoint b:</label>
        <input type="range" id="ra-slider-b" min="0.2" max="2.0" step="0.1" value="1.4" style="vertical-align: middle; width: 100px;">
        <span id="ra-b-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">b = 1.4</span>
      `;

      document.getElementById("ra-slider-a").oninput = (e) => {
        a = parseFloat(e.target.value);
        document.getElementById("ra-a-val").innerText = `a = ${a.toFixed(1)}`;
        render();
      };
      document.getElementById("ra-slider-b").oninput = (e) => {
        b = parseFloat(e.target.value);
        document.getElementById("ra-b-val").innerText = `b = ${b.toFixed(1)}`;
        render();
      };
    }

    // Function: f(x) = x^3 - 2x
    function f(x) { return x * x * x - 2 * x; }
    function df(x) { return 3 * x * x - 2; }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      // Coordinate mapping: x in [-2.5, 2.5], y in [-4, 4]
      const toPxX = (x) => (W / 2) + (x / 2.5) * (W / 2 - 50);
      const toPxY = (y) => (H / 2) - (y / 4.0) * (H / 2 - 40);

      // Axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(40, toPxY(0)); ctx.lineTo(W - 40, toPxY(0)); // x-axis
      ctx.moveTo(toPxX(0), 30); ctx.lineTo(toPxX(0), H - 30); // y-axis
      ctx.stroke();

      // Plot f(x) = x³ - 2x
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let x = -2.2; x <= 2.2; x += 0.05) {
        let px = toPxX(x), py = toPxY(f(x));
        if (x === -2.2) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Secant Line between (a, f(a)) and (b, f(b))
      let fa = f(a), fb = f(b);
      let secantSlope = (fb - fa) / (b - a);
      let pax = toPxX(a), pay = toPxY(fa);
      let pbx = toPxX(b), pby = toPxY(fb);

      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(pax, pay); ctx.lineTo(pbx, pby); ctx.stroke();
      ctx.setLineDash([]);

      // Find c in (a, b) where f'(c) = secantSlope: 3 c^2 - 2 = secantSlope
      let cCand = Math.sqrt(Math.max(0, (secantSlope + 2) / 3));
      let validC = [];
      [-cCand, cCand].forEach(c => {
        if (c > a && c < b) validC.push(c);
      });

      // Draw Tangent line(s) at c
      validC.forEach(c => {
        let pcx = toPxX(c), pcy = toPxY(f(c));

        // Tangent segment
        let tLen = 0.6;
        let tLeftX = c - tLen, tLeftY = f(c) - secantSlope * tLen;
        let tRightX = c + tLen, tRightY = f(c) + secantSlope * tLen;

        ctx.strokeStyle = "#34d399"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(toPxX(tLeftX), toPxY(tLeftY));
        ctx.lineTo(toPxX(tRightX), toPxY(tRightY));
        ctx.stroke();

        ctx.fillStyle = "#34d399";
        ctx.beginPath(); ctx.arc(pcx, pcy, 5.5, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = "#f8fafc"; ctx.font = "12px 'Fira Code', monospace"; ctx.textAlign = "center";
        ctx.fillText(`c = ${c.toFixed(2)}`, pcx, pcy - 12);
      });

      // Endpoints Markers
      ctx.fillStyle = "#f43f5e";
      ctx.beginPath(); ctx.arc(pax, pay, 6, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(pbx, pby, 6, 0, Math.PI * 2); ctx.fill();

      // Info text
      ctx.textAlign = "left"; ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.fillStyle = "#f8fafc";
      ctx.fillText(`Lagrange MVT: f'(c) = (f(b) - f(a)) / (b - a)`, 50, 25);

      ctx.fillStyle = "#f43f5e"; ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Secant Slope m_sec = ${secantSlope.toFixed(3)}`, 50, 45);

      ctx.fillStyle = "#34d399";
      ctx.fillText(`Tangents with f'(c) = m_sec found at: ${validC.map(c => `c = ${c.toFixed(2)}`).join(", ")}`, 50, 65);
    }

    render();
  }
};

// 7. Unit 7: Darboux Mesh Refinement & Pointwise vs Uniform Convergence
window.SIMULATIONS["sim_ra_riemann_uniform_conv"] = {
  title: "Riemann-Darboux Integrability & Uniform vs Pointwise Limits",
  description: "Refine partition mesh ||P|| to watch upper Darboux sums U(P) and lower Darboux sums L(P) squeeze towards the exact integral, and toggle to examine uniform convergence tubes.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let numPartitions = 8;
    let mode = "darboux"; // darboux, uniform

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Mode:</label>
        <button id="ra-m-darb" style="padding: 0.35rem 0.75rem; background: #3b82f6; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Riemann-Darboux Sums</button>
        <button id="ra-m-uni" style="padding: 0.35rem 0.75rem; background: #64748b; color: #fff; border: none; border-radius: 4px; cursor: pointer;">Uniform Convergence Tube (fn -> f)</button>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Mesh N:</label>
        <input type="range" id="ra-slider-n" min="2" max="32" step="2" value="8" style="vertical-align: middle; width: 100px;">
        <span id="ra-n-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">N = 8</span>
      `;

      document.getElementById("ra-m-darb").onclick = () => { mode = "darboux"; highlight("ra-m-darb"); render(); };
      document.getElementById("ra-m-uni").onclick = () => { mode = "uniform"; highlight("ra-m-uni"); render(); };
      document.getElementById("ra-slider-n").oninput = (e) => {
        numPartitions = parseInt(e.target.value);
        document.getElementById("ra-n-val").innerText = `N = ${numPartitions}`;
        render();
      };

      function highlight(id) {
        ["ra-m-darb", "ra-m-uni"].forEach(b => {
          document.getElementById(b).style.background = (b === id) ? "#3b82f6" : "#64748b";
        });
      }
    }

    function f(x) { return Math.sin(x) + 0.5 * x + 0.5; }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      if (mode === "darboux") {
        const a = 0, b = 3.0;
        const toPxX = (x) => 80 + (x / 3.2) * (W - 160);
        const toPxY = (y) => (H - 50) - (y / 3.0) * (H - 90);

        // Axes
        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(70, H - 50); ctx.lineTo(W - 60, H - 50); ctx.stroke();

        let dx = (b - a) / numPartitions;
        let upperSum = 0, lowerSum = 0;

        for (let i = 0; i < numPartitions; i++) {
          let xi = a + i * dx;
          let xnext = xi + dx;

          // Sample subinterval to find Mi and mi
          let samples = [];
          for (let s = 0; s <= 10; s++) samples.push(f(xi + s * (dx / 10)));
          let Mi = Math.max(...samples);
          let mi = Math.min(...samples);

          upperSum += Mi * dx;
          lowerSum += mi * dx;

          let px1 = toPxX(xi), px2 = toPxX(xnext);

          // Upper Darboux Rectangle (Cyan transparent)
          ctx.fillStyle = "rgba(56, 189, 248, 0.18)";
          ctx.strokeStyle = "#38bdf8";
          ctx.lineWidth = 1;
          ctx.fillRect(px1, toPxY(Mi), px2 - px1, toPxY(0) - toPxY(Mi));
          ctx.strokeRect(px1, toPxY(Mi), px2 - px1, toPxY(0) - toPxY(Mi));

          // Lower Darboux Rectangle (Dark Blue)
          ctx.fillStyle = "rgba(30, 58, 138, 0.4)";
          ctx.strokeStyle = "#60a5fa";
          ctx.fillRect(px1, toPxY(mi), px2 - px1, toPxY(0) - toPxY(mi));
          ctx.strokeRect(px1, toPxY(mi), px2 - px1, toPxY(0) - toPxY(mi));
        }

        // Draw Function Curve
        ctx.strokeStyle = "#facc15"; ctx.lineWidth = 3;
        ctx.beginPath();
        for (let x = 0; x <= 3.1; x += 0.05) {
          let px = toPxX(x), py = toPxY(f(x));
          if (x === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Stats
        ctx.textAlign = "left"; ctx.font = "bold 13px 'Inter', sans-serif";
        ctx.fillStyle = "#38bdf8";
        ctx.fillText(`Upper Darboux Sum U(P, f) = ${upperSum.toFixed(4)}`, 80, 25);
        ctx.fillStyle = "#60a5fa";
        ctx.fillText(`Lower Darboux Sum L(P, f) = ${lowerSum.toFixed(4)}`, 80, 45);

        let diff = upperSum - lowerSum;
        ctx.fillStyle = diff < 0.2 ? "#34d399" : "#f59e0b";
        ctx.font = "12px 'Fira Code', monospace";
        ctx.fillText(`Riemann Criterion: U(P, f) - L(P, f) = ${diff.toFixed(4)}  (-> 0 as N -> ∞)`, 80, 65);
      } else {
        // Mode Uniform Convergence: fn(x) = x^n on [0, 1]
        const toPxX = (x) => 100 + x * (W - 200);
        const toPxY = (y) => (H - 60) - y * (H - 120);

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(90, H - 60); ctx.lineTo(W - 80, H - 60); ctx.stroke();

        // Draw family of curves fn(x) = x^n
        for (let n = 1; n <= numPartitions; n++) {
          ctx.strokeStyle = `hsla(${(n * 25) % 360}, 80%, 65%, 0.7)`;
          ctx.lineWidth = 2;
          ctx.beginPath();
          for (let x = 0; x <= 1.0; x += 0.02) {
            let px = toPxX(x), py = toPxY(Math.pow(x, n));
            if (x === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
          }
          ctx.stroke();
        }

        // Limit function f(x): 0 on [0, 1) and 1 at x=1
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 3.5;
        ctx.beginPath(); ctx.moveTo(toPxX(0), toPxY(0)); ctx.lineTo(toPxX(0.99), toPxY(0)); ctx.stroke();
        ctx.fillStyle = "#f43f5e";
        ctx.beginPath(); ctx.arc(toPxX(1.0), toPxY(1.0), 5, 0, Math.PI * 2); ctx.fill();

        ctx.textAlign = "left"; ctx.font = "bold 13px 'Inter', sans-serif";
        ctx.fillStyle = "#f8fafc";
        ctx.fillText("Pointwise vs Uniform Convergence: fn(x) = xⁿ on [0, 1]", 90, 25);
        ctx.fillStyle = "#f43f5e"; ctx.font = "12px 'Fira Code', monospace";
        ctx.fillText("Limit function f(x) is Discontinuous at x=1! Therefore convergence CANNOT be uniform.", 90, 48);
        ctx.fillStyle = "#38bdf8";
        ctx.fillText("Preservation Theorem: Uniform limit of continuous functions must be continuous.", 90, 68);
      }
    }

    render();
  }
};

// 8. Unit 8: Multivariable Jacobian Deformation & Coordinate Transformations
window.SIMULATIONS["sim_ra_multivariable_jacobian"] = {
  title: "Multivariable Jacobian Deformation & Area Scaling in R²",
  description: "Examine total Fréchet derivatives and the Jacobian matrix J: observe how infinitesimal squares in the uv-domain deform into parallelograms in the xy-domain with area scaled by |det(J)|.",
  init: function(canvasId, controlsId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const controls = document.getElementById(controlsId);

    let rVal = 1.4;
    let thetaVal = 0.785; // 45 deg

    if (controls) {
      controls.innerHTML = `
        <label style="color: #94a3b8; font-size: 0.85rem;">Radius r:</label>
        <input type="range" id="ra-slider-r" min="0.5" max="2.2" step="0.1" value="1.4" style="vertical-align: middle; width: 90px;">
        <span id="ra-r-val" style="color: #38bdf8; font-family: monospace; font-size: 0.85rem;">r = 1.40</span>
        <label style="color: #94a3b8; font-size: 0.85rem; margin-left: 0.5rem;">Angle θ:</label>
        <input type="range" id="ra-slider-theta" min="0.1" max="1.57" step="0.05" value="0.785" style="vertical-align: middle; width: 90px;">
        <span id="ra-theta-val" style="color: #f43f5e; font-family: monospace; font-size: 0.85rem;">θ = 45°</span>
      `;

      document.getElementById("ra-slider-r").oninput = (e) => {
        rVal = parseFloat(e.target.value);
        document.getElementById("ra-r-val").innerText = `r = ${rVal.toFixed(2)}`;
        render();
      };
      document.getElementById("ra-slider-theta").oninput = (e) => {
        thetaVal = parseFloat(e.target.value);
        document.getElementById("ra-theta-val").innerText = `θ = ${(thetaVal * 180 / Math.PI).toFixed(0)}°`;
        render();
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const W = canvas.width;
      const H = canvas.height;

      const midX = W / 2;

      // Left Panel: Polar Domain (r, θ)
      ctx.fillStyle = "rgba(255,255,255,0.03)";
      ctx.fillRect(20, 40, midX - 35, H - 60);
      ctx.strokeStyle = "rgba(255,255,255,0.1)"; ctx.strokeRect(20, 40, midX - 35, H - 60);

      // Right Panel: Cartesian Domain (x, y)
      ctx.fillStyle = "rgba(255,255,255,0.03)";
      ctx.fillRect(midX + 15, 40, midX - 35, H - 60);
      ctx.strokeStyle = "rgba(255,255,255,0.1)"; ctx.strokeRect(midX + 15, 40, midX - 35, H - 60);

      // Left: dr x dtheta rectangle
      const dr = 0.35, dtheta = 0.3;
      let leftOriginX = 70, leftOriginY = H - 80;
      let lpx = leftOriginX + (rVal / 2.5) * (midX - 140);
      let lpy = leftOriginY - (thetaVal / 1.6) * (H - 140);

      ctx.fillStyle = "rgba(56, 189, 248, 0.3)";
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      let wPx = (dr / 2.5) * (midX - 140);
      let hPx = (dtheta / 1.6) * (H - 140);
      ctx.fillRect(lpx, lpy - hPx, wPx, hPx);
      ctx.strokeRect(lpx, lpy - hPx, wPx, hPx);

      // Right: Transformed Wedge (dx dy)
      let rightCenterX = midX + 15 + (midX - 35) / 2;
      let rightCenterY = H / 2 + 30;
      let scale = 75;

      let p1 = { x: rightCenterX + rVal * Math.cos(thetaVal) * scale, y: rightCenterY - rVal * Math.sin(thetaVal) * scale };
      let p2 = { x: rightCenterX + (rVal + dr) * Math.cos(thetaVal) * scale, y: rightCenterY - (rVal + dr) * Math.sin(thetaVal) * scale };
      let p3 = { x: rightCenterX + (rVal + dr) * Math.cos(thetaVal + dtheta) * scale, y: rightCenterY - (rVal + dr) * Math.sin(thetaVal + dtheta) * scale };
      let p4 = { x: rightCenterX + rVal * Math.cos(thetaVal + dtheta) * scale, y: rightCenterY - rVal * Math.sin(thetaVal + dtheta) * scale };

      ctx.fillStyle = "rgba(52, 211, 153, 0.35)";
      ctx.strokeStyle = "#34d399"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.lineTo(p3.x, p3.y);
      ctx.lineTo(p4.x, p4.y);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Jacobian calculation
      let detJ = rVal; // Jacobian for polar is r
      let areaUV = dr * dtheta;
      let areaXY = detJ * areaUV;

      // Text Labels
      ctx.textAlign = "left"; ctx.font = "bold 13px 'Inter', sans-serif";
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("Domain (r, θ) Element dr·dθ", 35, 25);

      ctx.fillStyle = "#34d399";
      ctx.fillText("Codomain (x, y) Wedge dx·dy = r·dr·dθ", midX + 30, 25);

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px 'Fira Code', monospace";
      ctx.fillText(`Jacobian Matrix J = [cos θ, -r sin θ; sin θ, r cos θ]`, 35, H - 15);
      ctx.fillText(`|det(J)| = r = ${rVal.toFixed(2)}  (Area Scale Factor)`, midX + 30, H - 15);
    }

    render();
  }
};

// Simulation engine adapter for app.js
window.SimulationEngine.initSimulation = function(containerId, simType) {
  const sim = window.SIMULATIONS[simType];
  if (!sim) {
    console.warn("Real Analysis Simulation not found:", simType);
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
