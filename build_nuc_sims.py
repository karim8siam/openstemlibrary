# build_nuc_sims.py - Generates nuclear-sims.js with 16 high-performance interactive simulations

sims_code = r'''// Nuclear Physics Interactive Simulation Engine
// 16 Interactive 60-FPS Canvas Simulations for Nuclear Structure, Decay, Reactions & High Energy Physics

window.NUC_SIMS = {

  // 1. Binding Energy per Nucleon & SEMF Breakdown
  "nuc-binding-energy-sim": {
    title: "Nuclear Binding Energy per Nucleon & SEMF Breakdown",
    desc: "Interactive binding energy curve B/A vs mass number A. Inspect the Weizsäcker SEMF contributions (Volume, Surface, Coulomb, Asymmetry, Pairing) and observe why iron-56 represents the maximum thermodynamic stability.",
    isAnimated: false,
    controls: [
      { id: "massA", label: "Mass Number A (1 to 240)", min: 4, max: 240, step: 2, value: 56 },
      { id: "showTerms", label: "SEMF Terms (1: Total B/A, 2: Component Breakdown)", min: 1, max: 2, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const targetA = vals.massA || 56;
      const mode = Math.round(vals.showTerms || 1);

      // Plot margins
      const mx = 60, my = 40, pw = w - mx - 40, ph = h - my - 50;

      // Axes & grid
      ctx.strokeStyle = "#1e293b";
      ctx.lineWidth = 1;
      for (let a = 0; a <= 250; a += 50) {
        const x = mx + (a / 250) * pw;
        ctx.beginPath(); ctx.moveTo(x, my); ctx.lineTo(x, my + ph); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(a, x - 8, my + ph + 16);
      }
      for (let b = 0; b <= 10; b += 2) {
        const y = my + ph - (b / 10) * ph;
        ctx.beginPath(); ctx.moveTo(mx, y); ctx.lineTo(mx + pw, y); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(b + " MeV", mx - 45, y + 4);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("Mass Number A", mx + pw / 2 - 40, my + ph + 34);
      ctx.save(); ctx.translate(16, my + ph / 2 + 30); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Binding Energy B/A (MeV)", 0, 0); ctx.restore();

      function getSEMF(A) {
        const Z = Math.round(A / (1.98 + 0.015 * Math.pow(A, 2/3)));
        const av = 15.75, as = 17.8, ac = 0.711, aa = 23.7;
        const vol = av;
        const surf = -as / Math.pow(A, 1/3);
        const coul = -ac * Z * (Z - 1) / Math.pow(A, 4/3);
        const asym = -aa * Math.pow(A - 2*Z, 2) / Math.pow(A, 2);
        const pair = (A % 2 === 0 ? 11.2 / Math.pow(A, 1.5) : 0);
        const total = Math.max(0, vol + surf + coul + asym + pair);
        return { total, vol, surf, coul, asym, pair, Z };
      }

      // Draw Main Curve
      ctx.beginPath();
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      for (let a = 4; a <= 245; a++) {
        const res = getSEMF(a);
        const x = mx + (a / 250) * pw;
        const y = my + ph - (res.total / 10) * ph;
        if (a === 4) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Peak highlight (Fe-56)
      const feRes = getSEMF(56);
      const feX = mx + (56 / 250) * pw;
      const feY = my + ph - (feRes.total / 10) * ph;
      ctx.fillStyle = "#22c55e";
      ctx.beginPath(); ctx.arc(feX, feY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#22c55e"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("56Fe Peak (8.79 MeV)", feX - 30, feY - 12);

      // Target A marker
      const cur = getSEMF(targetA);
      const curX = mx + (targetA / 250) * pw;
      const curY = my + ph - (cur.total / 10) * ph;
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(curX, my); ctx.lineTo(curX, my + ph); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e";
      ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();

      // Details Badge
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 240, my + 10, 220, 120);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 240, my + 10, 220, 120);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Target: A = ${targetA} (Z ≈ ${cur.Z})`, w - 225, my + 32);
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Total B/A: ${cur.total.toFixed(3)} MeV/n`, w - 225, my + 52);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Volume: +${cur.vol.toFixed(2)} MeV`, w - 225, my + 72);
      ctx.fillText(`Surface: ${cur.surf.toFixed(2)} MeV`, w - 225, my + 88);
      ctx.fillText(`Coulomb: ${cur.coul.toFixed(2)} MeV`, w - 225, my + 104);
      ctx.fillText(`Asymmetry: ${cur.asym.toFixed(2)} MeV`, w - 225, my + 120);
    }
  },

  // 2. Nuclear Shell Model Energy Levels & Magic Numbers
  "nuc-shell-model-levels-sim": {
    title: "Nuclear Shell Model Single-Particle Energy Levels",
    desc: "Single-particle nucleon energy levels in a 3D harmonic oscillator / Woods-Saxon potential with Spin-Orbit Coupling toggle (V_so l·s). Observe how spin-orbit splitting creates the major energy gaps corresponding to the magic numbers 2, 8, 20, 28, 50, 82, 126.",
    isAnimated: false,
    controls: [
      { id: "spinOrbit", label: "Spin-Orbit Coupling Strength (0 to 1)", min: 0, max: 1, step: 0.1, value: 1 },
      { id: "nucleonType", label: "Nucleon (1: Protons, 2: Neutrons)", min: 1, max: 2, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const so = vals.spinOrbit !== undefined ? vals.spinOrbit : 1.0;
      const isNeutron = Math.round(vals.nucleonType || 1) === 2;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Nuclear Shell Model Levels (${isNeutron ? "Neutrons" : "Protons"}) | Spin-Orbit: ${(so * 100).toFixed(0)}%`, 25, 25);

      const levels = [
        { name: "1s 1/2", base: 40, split: 0, deg: 2, magic: 2 },
        { name: "1p 3/2", base: 80, split: -15, deg: 4 },
        { name: "1p 1/2", base: 80, split: 15, deg: 2, magic: 8 },
        { name: "1d 5/2", base: 130, split: -22, deg: 6 },
        { name: "2s 1/2", base: 135, split: 0, deg: 2 },
        { name: "1d 3/2", base: 130, split: 22, deg: 4, magic: 20 },
        { name: "1f 7/2", base: 190, split: -32, deg: 8, magic: 28 },
        { name: "2p 3/2", base: 220, split: -10, deg: 4 },
        { name: "1f 5/2", base: 190, split: 25, deg: 6 },
        { name: "2p 1/2", base: 220, split: 10, deg: 2 },
        { name: "1g 9/2", base: 260, split: -40, deg: 10, magic: 50 },
        { name: "1g 7/2", base: 260, split: 28, deg: 8 },
        { name: "2d 5/2", base: 280, split: -14, deg: 6 },
        { name: "1h 11/2", base: 310, split: -45, deg: 12, magic: 82 }
      ];

      const startY = h - 45;
      let cumDeg = 0;

      levels.forEach((lvl, i) => {
        const yEnergy = lvl.base + lvl.split * so;
        const py = startY - yEnergy * 0.75;
        cumDeg += lvl.deg;

        // Level line
        ctx.strokeStyle = lvl.magic ? "#22c55e" : "#38bdf8";
        ctx.lineWidth = lvl.magic ? 3 : 2;
        ctx.beginPath();
        ctx.moveTo(120, py);
        ctx.lineTo(360, py);
        ctx.stroke();

        // Level label
        ctx.fillStyle = "#f8fafc"; ctx.font = "11px monospace";
        ctx.fillText(lvl.name, 60, py + 4);

        // Capacity
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`(2j+1 = ${lvl.deg})`, 370, py + 4);

        // Magic Shell Gap Callout
        if (lvl.magic) {
          ctx.strokeStyle = "rgba(34, 197, 94, 0.4)"; ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.moveTo(360, py); ctx.lineTo(520, py); ctx.stroke();
          ctx.setLineDash([]);
          ctx.fillStyle = "#22c55e"; ctx.font = "bold 12px Inter, sans-serif";
          ctx.fillText(`MAGIC SHELL: ${lvl.magic}`, 530, py + 4);
        }
      });
    }
  },

  // 3. Nuclear Quadrupole Deformation Visualizer (Ellipsoid)
  "nuc-quadrupole-deformation-sim": {
    title: "Nuclear Quadrupole Moment & Ellipsoidal Deformation",
    desc: "Visualize 3D nuclear charge density under quadrupole deformation parameter beta_2. Transition continuously from spherical (beta_2 = 0, Q = 0) to prolate elongation (c > a, Q > 0) and oblate flattening (c < a, Q < 0).",
    isAnimated: true,
    controls: [
      { id: "beta2", label: "Deformation beta_2 (-0.6 to +0.6)", min: -0.6, max: 0.6, step: 0.05, value: 0.3 },
      { id: "rotSpeed", label: "Spin Speed", min: 0, max: 2, step: 0.2, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const beta = vals.beta2 !== undefined ? vals.beta2 : 0.3;
      const speed = vals.rotSpeed !== undefined ? vals.rotSpeed : 1.0;
      const angle = time * 0.9 * speed;

      const cx = w * 0.45, cy = h * 0.52;
      const R0 = 85;
      // Prolate: z axis elongated, x, y contracted
      const rz = R0 * (1 + 0.63 * beta);
      const rx = R0 * (1 - 0.31 * beta);
      const ry = rx;

      // 3D wireframe ellipsoid latitude & longitude lines
      ctx.lineWidth = 1.4;
      const lats = 9, lons = 12;

      for (let i = 1; i < lats; i++) {
        const phi = (i / lats - 0.5) * Math.PI;
        const z0 = rz * Math.sin(phi);
        const rad = rx * Math.cos(phi);

        ctx.beginPath();
        for (let j = 0; j <= 36; j++) {
          const theta = (j / 36) * Math.PI * 2;
          const x = rad * Math.cos(theta);
          const y = rad * Math.sin(theta);

          // Rotate around Y and tilt
          const x1 = x * Math.cos(angle) - z0 * Math.sin(angle);
          const z1 = x * Math.sin(angle) + z0 * Math.cos(angle);
          const px = cx + x1;
          const py = cy - (y * Math.cos(0.4) - z1 * Math.sin(0.4));
          if (j === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.strokeStyle = beta > 0.05 ? "rgba(56, 189, 248, 0.4)" : (beta < -0.05 ? "rgba(244, 63, 94, 0.4)" : "rgba(34, 197, 94, 0.4)");
        ctx.stroke();
      }

      // Deformation Info Panel
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 230, 20, 210, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 230, 20, 210, 130);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Shape Parameters", w - 215, 42);
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Deformation β2: ${beta.toFixed(2)}`, w - 215, 64);
      ctx.fillStyle = beta > 0.05 ? "#38bdf8" : (beta < -0.05 ? "#f43f5e" : "#22c55e");
      ctx.font = "bold 12px Inter, sans-serif";
      const shapeType = beta > 0.05 ? "Prolate (Cigar-like, Q > 0)" : (beta < -0.05 ? "Oblate (Pancake-like, Q < 0)" : "Spherical (Q = 0)");
      ctx.fillText(shapeType, w - 215, 84);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Major semi-axis c: ${rz.toFixed(1)} fm`, w - 215, 106);
      ctx.fillText(`Minor semi-axis a: ${rx.toFixed(1)} fm`, w - 215, 124);
      ctx.fillText(`Quadrupole Q0 ∝ β2 R0²`, w - 215, 140);
    }
  },

  // 4. Radioactive Decay Kinetics & Bateman Equations
  "nuc-decay-kinetics-sim": {
    title: "Radioactive Decay Series & Bateman Equations",
    desc: "Simulate a three-member decay chain (Parent N1 -> Daughter N2 -> Granddaughter N3) governed by the Bateman differential equations. Adjust half-lives to produce secular equilibrium, transient equilibrium, or no equilibrium.",
    isAnimated: false,
    controls: [
      { id: "t1", label: "Parent T1/2 (hours)", min: 1, max: 20, step: 1, value: 10 },
      { id: "t2", label: "Daughter T1/2 (hours)", min: 0.5, max: 10, step: 0.5, value: 2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const t1 = vals.t1 || 10, t2 = vals.t2 || 2;
      const l1 = Math.LN2 / t1, l2 = Math.LN2 / t2;

      const mx = 60, my = 40, pw = w - mx - 40, ph = h - my - 50;
      const tMax = 30; // hours

      // Grid
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let t = 0; t <= tMax; t += 5) {
        const x = mx + (t / tMax) * pw;
        ctx.beginPath(); ctx.moveTo(x, my); ctx.lineTo(x, my + ph); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(t + "h", x - 8, my + ph + 16);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("Elapsed Time (hours)", mx + pw / 2 - 40, my + ph + 34);

      // Parent N1(t) = N0 e^(-l1 t)
      // Daughter N2(t) = N0 * l1/(l2 - l1) * (e^-l1 t - e^-l2 t)
      // Stable Granddaughter N3(t) = N0 - N1 - N2
      const N0 = 1000;

      function getPops(t) {
        const n1 = N0 * Math.exp(-l1 * t);
        let n2 = 0;
        if (Math.abs(l1 - l2) < 1e-4) {
          n2 = N0 * l1 * t * Math.exp(-l1 * t);
        } else {
          n2 = N0 * (l1 / (l2 - l1)) * (Math.exp(-l1 * t) - Math.exp(-l2 * t));
        }
        const n3 = Math.max(0, N0 - n1 - n2);
        return { n1, n2, n3 };
      }

      // Draw Parent N1 (Cyan)
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      for (let t = 0; t <= tMax; t += 0.2) {
        const p = getPops(t);
        const x = mx + (t / tMax) * pw;
        const y = my + ph - (p.n1 / N0) * ph;
        if (t === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Draw Daughter N2 (Purple)
      ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.5;
      for (let t = 0; t <= tMax; t += 0.2) {
        const p = getPops(t);
        const x = mx + (t / tMax) * pw;
        const y = my + ph - (p.n2 / N0) * ph;
        if (t === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Draw Granddaughter N3 (Emerald)
      ctx.beginPath(); ctx.strokeStyle = "#22c55e"; ctx.lineWidth = 2;
      for (let t = 0; t <= tMax; t += 0.2) {
        const p = getPops(t);
        const x = mx + (t / tMax) * pw;
        const y = my + ph - (p.n3 / N0) * ph;
        if (t === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 230, 20, 210, 100);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 230, 20, 210, 100);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`— Parent N1 (T1/2 = ${t1}h)`, w - 215, 42);
      ctx.fillStyle = "#a855f7";
      ctx.fillText(`— Daughter N2 (T1/2 = ${t2}h)`, w - 215, 62);
      ctx.fillStyle = "#22c55e";
      ctx.fillText(`— Granddaughter N3 (Stable)`, w - 215, 82);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px Inter, sans-serif";
      const eqType = t1 > 10 * t2 ? "Secular Eq." : (t1 > t2 ? "Transient Eq." : "No Equilibrium");
      ctx.fillText(`State: ${eqType}`, w - 215, 102);
    }
  },

  // 5. Carbon-14 Radiocarbon Archaeological Dating Simulator
  "nuc-carbon-dating-sim": {
    title: "Carbon-14 Radiocarbon Age Calculator",
    desc: "Calculate archaeological specimen ages from residual Carbon-14 activity relative to modern biosphere activity (15.3 dpm/g Carbon, half-life 5,730 years).",
    isAnimated: false,
    controls: [
      { id: "activity", label: "Residual Activity (% of modern standard)", min: 1, max: 100, step: 1, value: 25 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const pct = vals.activity || 25;
      const fraction = pct / 100;
      const tHalf = 5730;
      const age = -tHalf * Math.log2(fraction);

      const mx = 60, my = 40, pw = w - mx - 40, ph = h - my - 50;
      const maxAge = 40000;

      // Grid
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let a = 0; a <= maxAge; a += 5000) {
        const x = mx + (a / maxAge) * pw;
        ctx.beginPath(); ctx.moveTo(x, my); ctx.lineTo(x, my + ph); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText((a / 1000) + "k", x - 8, my + ph + 16);
      }
      for (let p = 0; p <= 100; p += 20) {
        const y = my + ph - (p / 100) * ph;
        ctx.beginPath(); ctx.moveTo(mx, y); ctx.lineTo(mx + pw, y); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(p + "%", mx - 35, y + 4);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("Age Before Present (Years)", mx + pw / 2 - 50, my + ph + 34);

      // C-14 decay curve
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      for (let t = 0; t <= maxAge; t += 200) {
        const f = Math.pow(0.5, t / tHalf);
        const x = mx + (t / maxAge) * pw;
        const y = my + ph - f * ph;
        if (t === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Sample marker
      const sampleX = mx + (Math.min(age, maxAge) / maxAge) * pw;
      const sampleY = my + ph - fraction * ph;
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(sampleX, my); ctx.lineTo(sampleX, my + ph); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(mx, sampleY); ctx.lineTo(mx + pw, sampleY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(sampleX, sampleY, 6, 0, Math.PI * 2); ctx.fill();

      // Output Card
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(w - 250, 20, 230, 110);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 250, 20, 230, 110);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Archaeological Dating", w - 235, 42);
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Measured Activity: ${pct}%`, w - 235, 64);
      ctx.fillStyle = "#22c55e"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Calculated Age: ${Math.round(age).toLocaleString()} BP`, w - 235, 86);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Calendar Epoch: ≈ ${Math.max(0, Math.round(age - 1950)).toLocaleString()} BCE`, w - 235, 106);
    }
  },

  // 6. Alpha Decay Gamow Quantum Barrier Tunneling Simulator
  "nuc-alpha-gamow-tunneling-sim": {
    title: "Alpha Decay Gamow Quantum Barrier Penetration",
    desc: "Simulate the alpha particle wave packet incident on the combined nuclear potential well and repulsive Coulomb barrier. Observe how tunneling probability P scales exponentially with decay energy Q_alpha.",
    isAnimated: true,
    controls: [
      { id: "qAlpha", label: "Alpha Energy Q (4 to 9 MeV)", min: 4.0, max: 9.0, step: 0.2, value: 5.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Q = vals.qAlpha || 5.5;
      const mx = 60, my = 40, pw = w - mx - 40, ph = h - my - 50;

      // Potential V(r): Well for r < R_nuc (8 fm), Coulomb 30 MeV * (8/r) for r > R_nuc
      const R_nuc = 8;
      const b_turn = (30 / Q) * R_nuc; // classical turning point

      // Draw potential curve
      ctx.strokeStyle = "#e2e8f0"; ctx.lineWidth = 2;
      ctx.beginPath();
      // Well
      const x0 = mx + (R_nuc / 45) * pw;
      ctx.moveTo(mx, my + ph - 20); // bottom of well
      ctx.lineTo(x0, my + ph - 20);
      ctx.lineTo(x0, my + 30); // Coulomb peak (30 MeV)
      // Coulomb tail
      for (let r = R_nuc; r <= 45; r += 0.5) {
        const v = 30 * (R_nuc / r);
        const px = mx + (r / 45) * pw;
        const py = my + ph - (v / 35) * ph;
        ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Energy Q_alpha horizontal line
      const qY = my + ph - (Q / 35) * ph;
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(mx, qY); ctx.lineTo(mx + pw, qY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Q_α = ${Q.toFixed(1)} MeV`, mx + 15, qY - 8);

      // Classical turning point marker
      const xb = mx + (Math.min(b_turn, 45) / 45) * pw;
      ctx.fillStyle = "#f43f5e";
      ctx.beginPath(); ctx.arc(xb, qY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f43f5e"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`b = ${b_turn.toFixed(1)} fm`, xb - 15, qY + 18);

      // Tunneling Wave Packet Animation
      ctx.beginPath();
      ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.5;
      const freq = 12;
      for (let r = 0; r <= 45; r += 0.3) {
        const px = mx + (r / 45) * pw;
        let amp = 0;
        if (r < R_nuc) {
          amp = 18 * Math.sin(freq * (r / R_nuc) - time * 6);
        } else if (r < b_turn) {
          const decay = Math.exp(-2.5 * (r - R_nuc) / (b_turn - R_nuc));
          amp = 18 * decay * Math.cos(time * 6);
        } else {
          const transAmp = 3.5 * (Q / 6.0);
          amp = transAmp * Math.sin(freq * 0.7 * (r / 10) - time * 6);
        }
        const py = qY + amp;
        if (r === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Gamow Factor estimation
      const gamowG = 15.0 / Math.sqrt(Q);
      const P_tunnel = Math.exp(-gamowG);

      // Info badge
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(w - 230, 20, 210, 100);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 230, 20, 210, 100);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Gamow Tunneling", w - 215, 42);
      ctx.fillStyle = "#38bdf8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Barrier Width: ${(b_turn - R_nuc).toFixed(1)} fm`, w - 215, 62);
      ctx.fillStyle = "#22c55e"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`P_trans: ~ 10^(-${(gamowG / 2.302).toFixed(1)})`, w - 215, 84);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Geiger-Nuttall: log(T) ∝ Q^(-1/2)", w - 215, 104);
    }
  },

  // 7. Continuous Beta Energy Distribution & Fermi-Kurie Plot
  "nuc-beta-energy-spectrum-sim": {
    title: "Beta Decay Spectrum & Fermi-Kurie Plot Analysis",
    desc: "Inspect the continuous electron energy spectrum N(E) and linearized Fermi-Kurie plot K(E) = sqrt(N / (p^2 F)) as functions of endpoint energy E_0.",
    isAnimated: false,
    controls: [
      { id: "e0", label: "Endpoint Energy E0 (MeV)", min: 0.5, max: 3.5, step: 0.25, value: 1.5 },
      { id: "plotMode", label: "Display (1: Energy Spectrum N(E), 2: Fermi-Kurie Plot)", min: 1, max: 2, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const E0 = vals.e0 || 1.5;
      const mode = Math.round(vals.plotMode || 1);

      const mx = 60, my = 40, pw = w - mx - 40, ph = h - my - 50;

      // Grid
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let e = 0; e <= 4.0; e += 0.5) {
        const x = mx + (e / 4.0) * pw;
        ctx.beginPath(); ctx.moveTo(x, my); ctx.lineTo(x, my + ph); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(e.toFixed(1), x - 8, my + ph + 16);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("Electron Kinetic Energy T (MeV)", mx + pw / 2 - 60, my + ph + 34);

      if (mode === 1) {
        // Continuous Spectrum N(E) ∝ p E (E0 - E)^2
        ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        let maxVal = 0;
        const pts = [];
        for (let e = 0.01; e <= E0; e += 0.02) {
          const p = Math.sqrt(e * (e + 1.022));
          const val = p * (e + 0.511) * Math.pow(E0 - e, 2);
          if (val > maxVal) maxVal = val;
          pts.push({ e, val });
        }
        pts.forEach((pt, i) => {
          const x = mx + (pt.e / 4.0) * pw;
          const y = my + ph - (pt.val / maxVal) * ph * 0.9;
          if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        });
        ctx.stroke();

        // Fill area
        ctx.lineTo(mx + (E0 / 4.0) * pw, my + ph);
        ctx.lineTo(mx, my + ph);
        ctx.fillStyle = "rgba(56, 189, 248, 0.15)"; ctx.fill();

        // Endpoint marker
        const epX = mx + (E0 / 4.0) * pw;
        ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(epX, my + ph, 5, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(`E_endpoint = ${E0} MeV`, epX - 45, my + ph - 15);
      } else {
        // Fermi-Kurie Plot K(E) ∝ (E0 - E)
        ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.5;
        const x1 = mx;
        const y1 = my + 20;
        const x2 = mx + (E0 / 4.0) * pw;
        const y2 = my + ph;
        ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();

        ctx.fillStyle = "#a855f7"; ctx.beginPath(); ctx.arc(x2, y2, 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(`Kurie Intercept: E0 = ${E0} MeV`, x2 - 60, y2 - 20);
      }
    }
  },

  // 8. Photon Cross-Sections & Matter Interactions
  "nuc-photon-attenuation-sim": {
    title: "Photon Cross-Sections: Photoelectric, Compton & Pair Production",
    desc: "Energy-dependent photon interaction cross-sections across 10 keV to 100 MeV in Lead (Z=82) vs Aluminum (Z=13). Observe the dominant regimes for photoelectric effect, Compton scattering, and pair production above 1.022 MeV.",
    isAnimated: false,
    controls: [
      { id: "absorberZ", label: "Absorber Material (1: Lead Z=82, 2: Aluminum Z=13)", min: 1, max: 2, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isLead = Math.round(vals.absorberZ || 1) === 1;
      const Z = isLead ? 82 : 13;

      const mx = 65, my = 40, pw = w - mx - 40, ph = h - my - 50;

      // Log-Log axes: E from 0.01 MeV (10 keV) to 100 MeV (4 decades)
      // mu from 0.01 to 100 cm^-1 (4 decades)
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let dec = -2; dec <= 2; dec++) {
        const x = mx + ((dec + 2) / 4) * pw;
        ctx.beginPath(); ctx.moveTo(x, my); ctx.lineTo(x, my + ph); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(Math.pow(10, dec) + " MeV", x - 15, my + ph + 16);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("Photon Energy E_gamma", mx + pw / 2 - 45, my + ph + 34);

      // Photoelectric Curve: ~ Z^4 / E^3
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      for (let xPix = 0; xPix <= pw; xPix += 4) {
        const logE = -2 + (xPix / pw) * 4;
        const E = Math.pow(10, logE);
        const sigmaPE = (isLead ? 80 : 2) * Math.pow(0.1 / E, 3.2);
        const logS = Math.log10(Math.max(0.01, sigmaPE));
        const py = my + ph - ((logS + 2) / 4) * ph;
        if (xPix === 0) ctx.moveTo(mx + xPix, Math.min(my + ph, py)); else ctx.lineTo(mx + xPix, Math.min(my + ph, py));
      }
      ctx.stroke();

      // Compton Curve: ~ Z / E
      ctx.beginPath(); ctx.strokeStyle = "#22c55e"; ctx.lineWidth = 2;
      for (let xPix = 0; xPix <= pw; xPix += 4) {
        const logE = -2 + (xPix / pw) * 4;
        const E = Math.pow(10, logE);
        const sigmaC = (isLead ? 0.8 : 0.3) / (1 + 2 * E);
        const logS = Math.log10(Math.max(0.01, sigmaC));
        const py = my + ph - ((logS + 2) / 4) * ph;
        if (xPix === 0) ctx.moveTo(mx + xPix, py); else ctx.lineTo(mx + xPix, py);
      }
      ctx.stroke();

      // Pair Production Curve: starts at 1.022 MeV, ~ Z^2 ln(E)
      ctx.beginPath(); ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2;
      for (let xPix = 0; xPix <= pw; xPix += 4) {
        const logE = -2 + (xPix / pw) * 4;
        const E = Math.pow(10, logE);
        let sigmaPP = 0.01;
        if (E > 1.022) {
          sigmaPP = (isLead ? 0.5 : 0.04) * Math.log(E / 1.022);
        }
        const logS = Math.log10(Math.max(0.01, sigmaPP));
        const py = my + ph - ((logS + 2) / 4) * ph;
        if (xPix === 0) ctx.moveTo(mx + xPix, py); else ctx.lineTo(mx + xPix, py);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 240, 20, 220, 110);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 240, 20, 220, 110);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Absorber: ${isLead ? "Lead (Z=82)" : "Aluminum (Z=13)"}`, w - 225, 40);
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("— Photoelectric Effect (∝ Z⁴ / E³)", w - 225, 60);
      ctx.fillStyle = "#22c55e";
      ctx.fillText("— Compton Scattering (∝ Z / E)", w - 225, 80);
      ctx.fillStyle = "#f43f5e";
      ctx.fillText("— Pair Production (Threshold 1.02 MeV)", w - 225, 100);
    }
  },

  // 9. Nuclear Reaction Kinematics & Laboratory-to-CM Transformer
  "nuc-reaction-kinematics-sim": {
    title: "Nuclear Reaction Kinematics & Lab-to-CM Transformer",
    desc: "Calculate laboratory scattering angles and ejectile energies for two-body nuclear reactions X(a, b)Y. Inspect the center-of-mass velocity boost and threshold energy conditions for endothermic channels.",
    isAnimated: false,
    controls: [
      { id: "eLab", label: "Projectile Lab Energy Ta (MeV)", min: 1, max: 20, step: 1, value: 8 },
      { id: "thetaLab", label: "Lab Scattering Angle (degrees)", min: 0, max: 180, step: 10, value: 45 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Ta = vals.eLab || 8;
      const deg = vals.thetaLab || 45;
      const rad = (deg * Math.PI) / 180;

      // Reaction: 14N(alpha, p)17O with Q = -1.19 MeV
      const ma = 4, mX = 14, mb = 1, mY = 17;
      const Q = -1.19;
      const Eth = Math.abs(Q) * (1 + ma / mX); // 1.53 MeV

      const cx = w * 0.45, cy = h * 0.52;

      // Momentum vectors diagram
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      // Incident projectile vector
      ctx.beginPath(); ctx.moveTo(cx - 160, cy); ctx.lineTo(cx, cy); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(cx - 160, cy, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Alpha (Ta)", cx - 140, cy - 10);

      // Target at origin
      ctx.fillStyle = "#f8fafc"; ctx.beginPath(); ctx.arc(cx, cy, 7, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("Target 14N", cx - 30, cy + 24);

      if (Ta >= Eth) {
        // Ejectile vector
        const lenB = 120;
        const bx = cx + lenB * Math.cos(rad);
        const by = cy - lenB * Math.sin(rad);
        ctx.strokeStyle = "#22c55e"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(bx, by); ctx.stroke();
        ctx.fillStyle = "#22c55e"; ctx.beginPath(); ctx.arc(bx, by, 5, 0, Math.PI * 2); ctx.fill();
        ctx.fillText(`Proton (${deg}°)`, bx + 10, by);

        // Recoil vector
        const lenY = 70;
        const recAngle = Math.PI - rad * 0.4;
        const rx = cx + lenY * Math.cos(recAngle);
        const ry = cy + lenY * Math.sin(recAngle);
        ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(rx, ry); ctx.stroke();
        ctx.fillStyle = "#a855f7"; ctx.beginPath(); ctx.arc(rx, ry, 5, 0, Math.PI * 2); ctx.fill();
        ctx.fillText("Recoil 17O", rx - 65, ry + 15);
      } else {
        ctx.fillStyle = "#f43f5e"; ctx.font = "bold 14px Inter, sans-serif";
        ctx.fillText("REACTION FORBIDDEN: Ta < Threshold Energy!", cx - 120, cy - 40);
      }

      // Kinematics Panel
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 240, 20, 220, 110);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 240, 20, 220, 110);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Kinematics Parameters", w - 225, 40);
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Reaction Q: ${Q} MeV`, w - 225, 60);
      ctx.fillStyle = "#f43f5e";
      ctx.fillText(`Threshold Eth: ${Eth.toFixed(2)} MeV`, w - 225, 80);
      ctx.fillStyle = "#22c55e";
      const Tcm = Ta * (mX / (ma + mX));
      ctx.fillText(`CM Energy: ${Tcm.toFixed(2)} MeV`, w - 225, 100);
    }
  },

  // 10. Nuclear Fission Chain Reaction Cascade & Multiplication Factor k
  "nuc-fission-chain-reaction-sim": {
    title: "Nuclear Fission Chain Reaction & Multiplication Factor k",
    desc: "Observe real-time neutron generation branching in a multiplying fission medium. Vary the effective multiplication factor k to simulate subcritical decay (k < 1), critical steady-state (k = 1), and supercritical exponential surge (k > 1).",
    isAnimated: true,
    controls: [
      { id: "kFactor", label: "Multiplication Factor k (0.7 to 1.3)", min: 0.7, max: 1.3, step: 0.05, value: 1.05 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const k = vals.kFactor !== undefined ? vals.kFactor : 1.05;

      const levels = 5;
      const startX = 60, endX = w - 260;
      const dx = (endX - startX) / (levels - 1);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Neutron Fission Cascade | k = ${k.toFixed(2)} (${k > 1 ? "Supercritical" : (k < 1 ? "Subcritical" : "Critical")})`, 25, 25);

      let currentCount = 1;
      let prevNodes = [{ y: h / 2 }];

      for (let gen = 0; gen < levels; gen++) {
        const x = startX + gen * dx;
        const nextNodes = [];
        const nextCount = Math.min(24, Math.round(currentCount * k));

        // Draw nodes for this generation
        prevNodes.forEach(node => {
          ctx.fillStyle = "#22c55e";
          ctx.beginPath(); ctx.arc(x, node.y, 4, 0, Math.PI * 2); ctx.fill();
        });

        if (gen < levels - 1) {
          // Connect to next generation
          const stepY = (h - 80) / Math.max(1, nextCount);
          for (let n = 0; n < nextCount; n++) {
            const ny = 45 + n * stepY + (stepY / 2);
            nextNodes.push({ y: ny });

            const parentNode = prevNodes[Math.floor((n / nextCount) * prevNodes.length)] || prevNodes[0];
            ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 1.2;
            ctx.beginPath(); ctx.moveTo(x, parentNode.y); ctx.lineTo(x + dx, ny); ctx.stroke();
          }
          prevNodes = nextNodes;
          currentCount = nextCount;
        }
      }

      // Reactor Status Badge
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(w - 230, 20, 210, 110);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 230, 20, 210, 110);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Reactor Dynamics", w - 215, 40);
      ctx.fillStyle = k > 1 ? "#f43f5e" : (k < 1 ? "#38bdf8" : "#22c55e");
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(k > 1 ? "SUPERCRITICAL (Power Exponentiates)" : (k < 1 ? "SUBCRITICAL (Power Decays)" : "CRITICAL (Steady Power)"), w - 215, 62);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Multiplication: k = ${k.toFixed(2)}`, w - 215, 82);
      ctx.fillText(`Delayed fraction β ≈ 0.0065`, w - 215, 102);
    }
  },

  // 11. Thermonuclear Fusion Gamow Window Simulator
  "nuc-thermonuclear-fusion-sim": {
    title: "Thermonuclear D-T Fusion Gamow Window",
    desc: "Evaluate the convolution of the Maxwell-Boltzmann thermal velocity tail e^(-E/kT) and the quantum Coulomb barrier penetration factor e^(-b/sqrt(E)). The overlap forms the narrow Gamow Window where all fusion occurs.",
    isAnimated: false,
    controls: [
      { id: "plasmaTemp", label: "Plasma Temp T (keV)", min: 2, max: 30, step: 2, value: 15 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const kT = vals.plasmaTemp || 15;
      const mx = 60, my = 40, pw = w - mx - 40, ph = h - my - 50;

      // Energy E from 0 to 100 keV
      const maxE = 100;

      // Maxwell-Boltzmann tail: e^(-E / kT)
      // Tunneling: e^(-31.4 / sqrt(E))
      // Cross-section convolution: product
      let maxConv = 0;
      const pts = [];
      for (let e = 1; e <= maxE; e += 1) {
        const mb = Math.exp(-e / kT);
        const tun = Math.exp(-31.4 / Math.sqrt(e));
        const conv = mb * tun;
        if (conv > maxConv) maxConv = conv;
        pts.push({ e, mb, tun, conv });
      }

      // Draw Gamow Window peak
      ctx.beginPath(); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
      pts.forEach((pt, i) => {
        const x = mx + (pt.e / maxE) * pw;
        const y = my + ph - (pt.conv / maxConv) * ph * 0.85;
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      });
      ctx.stroke();

      // Fill Gamow window
      ctx.lineTo(mx + pw, my + ph); ctx.lineTo(mx, my + ph);
      ctx.fillStyle = "rgba(245, 158, 11, 0.2)"; ctx.fill();

      // Gamow peak position: E_0 = (b * kT / 2)^(2/3) ≈ 1.22 * (Z1 Z2 T)^2/3
      const e0Gamow = Math.pow((31.4 * kT) / 2, 2/3);
      const peakX = mx + (Math.min(e0Gamow, maxE) / maxE) * pw;
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(peakX, my + ph - 0.85 * ph, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Gamow Peak ≈ ${e0Gamow.toFixed(1)} keV`, peakX - 45, my + 50);

      // Info Badge
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 240, 20, 220, 100);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 240, 20, 220, 100);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`D-T Fusion Plasma (${kT} keV)`, w - 225, 40);
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("— Gamow Fusion Window", w - 225, 60);
      ctx.fillStyle = "#94a3b8";
      ctx.fillText(`Peak Energy E0: ${e0Gamow.toFixed(1)} keV`, w - 225, 80);
      ctx.fillText(`Lawson: n·T·τE > 3×10²¹ keV·s/m³`, w - 225, 98);
    }
  },

  // 12. Bragg Ionization Peak & Charged Particle Stopping Power
  "nuc-bragg-peak-sim": {
    title: "Bragg Ionization Peak in Radiation Therapy",
    desc: "Compare depth-dose ionization distributions in human tissue for Protons (Bragg peak) versus 6 MV Megavoltage Photons (exponential attenuation). Adjust proton beam energy to steer the Bragg peak into deep target tumors.",
    isAnimated: false,
    controls: [
      { id: "beamEnergy", label: "Proton Energy (100 to 220 MeV)", min: 100, max: 220, step: 20, value: 160 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const E = vals.beamEnergy || 160;
      const mx = 60, my = 40, pw = w - mx - 40, ph = h - my - 50;

      // Range R in cm ≈ (E / 22)^1.75
      const rangeCm = Math.pow(E / 32, 1.75);
      const maxDepth = 35; // cm

      // Axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let d = 0; d <= maxDepth; d += 5) {
        const x = mx + (d / maxDepth) * pw;
        ctx.beginPath(); ctx.moveTo(x, my); ctx.lineTo(x, my + ph); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(d + " cm", x - 10, my + ph + 16);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("Tissue Depth (cm)", mx + pw / 2 - 45, my + ph + 34);

      // Draw Photon Depth-Dose Curve (X-rays: build up then exponential attenuation)
      ctx.beginPath(); ctx.strokeStyle = "#64748b"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      for (let d = 0; d <= maxDepth; d += 0.5) {
        const dose = d < 1.5 ? (0.6 + 0.4 * (d / 1.5)) : Math.exp(-0.05 * (d - 1.5));
        const x = mx + (d / maxDepth) * pw;
        const y = my + ph - dose * ph * 0.45;
        if (d === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke(); ctx.setLineDash([]);

      // Draw Proton Bragg Peak
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      for (let d = 0; d <= maxDepth; d += 0.2) {
        let dose = 0;
        if (d < rangeCm - 1.5) {
          dose = 0.35 + 0.2 * (d / rangeCm);
        } else if (d <= rangeCm) {
          const delta = rangeCm - d;
          dose = 0.55 + 2.2 / (1 + delta * 2.5);
        } else {
          dose = Math.max(0, 2.7 * Math.exp(-8 * (d - rangeCm)));
        }
        const x = mx + (d / maxDepth) * pw;
        const y = my + ph - (dose / 3.0) * ph * 0.9;
        if (d === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Bragg Peak Highlight
      const peakX = mx + (rangeCm / maxDepth) * pw;
      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(peakX, my + 35, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Bragg Peak: ${rangeCm.toFixed(1)} cm`, peakX - 50, my + 25);

      // Legend
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 240, 20, 220, 100);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 240, 20, 220, 100);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`— Protons (${E} MeV)`, w - 225, 42);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("--- Photons (6 MV X-rays)", w - 225, 62);
      ctx.fillStyle = "#22c55e";
      ctx.fillText("Zero exit dose beyond peak!", w - 225, 82);
    }
  },

  // 13. Geiger-Müller Counter Townsend Avalanche Simulator
  "nuc-geiger-counter-sim": {
    title: "Geiger-Müller Counter Townsend Avalanche & Pulse Formation",
    desc: "Observe the radial electric field E(r) and Townsend electron avalanche near the central anode wire. Adjust anode voltage across Ion Chamber, Proportional, and Geiger plateau regimes.",
    isAnimated: true,
    controls: [
      { id: "voltage", label: "Cathode-Anode Voltage (V)", min: 100, max: 1200, step: 100, value: 900 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const V = vals.voltage || 900;
      const cx = w * 0.45, cy = h * 0.52;

      // Outer Cathode Cylinder
      const rCathode = 110;
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.arc(cx, cy, rCathode, 0, Math.PI * 2); ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Cathode Cylinder (- Ground)", cx - 65, cy + rCathode + 20);

      // Center Anode Wire
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(cx, cy, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`Anode (+${V} V)`, cx + 10, cy - 8);

      // Avalanche electrons animated
      const numRays = V > 700 ? 16 : (V > 300 ? 6 : 2);
      ctx.fillStyle = "#38bdf8";
      for (let i = 0; i < numRays; i++) {
        const theta = (i / numRays) * Math.PI * 2 + time * 0.4;
        const drift = ((time * 35 + i * 20) % (rCathode - 10));
        const r = rCathode - drift;
        const px = cx + r * Math.cos(theta);
        const py = cy + r * Math.sin(theta);
        ctx.beginPath(); ctx.arc(px, py, 2.5, 0, Math.PI * 2); ctx.fill();

        // Avalanche glow near anode
        if (r < 25 && V > 600) {
          ctx.fillStyle = "rgba(244, 63, 94, 0.4)";
          ctx.beginPath(); ctx.arc(cx, cy, 22, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Regime Badge
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 230, 20, 210, 100);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 230, 20, 210, 100);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Operating Regime", w - 215, 40);
      let regime = "Ionization Chamber (M = 1)";
      if (V >= 300 && V < 700) regime = "Proportional Counter (M ~ 10⁴)";
      if (V >= 700) regime = "Geiger-Müller Plateau (M ~ 10⁸)";
      ctx.fillStyle = V >= 700 ? "#f43f5e" : (V >= 300 ? "#a855f7" : "#38bdf8");
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(regime, w - 215, 62);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Dead Time τ ≈ ${V >= 700 ? "100 μs" : "< 1 μs"}`, w - 215, 82);
    }
  },

  // 14. High-Purity Germanium (HPGe) vs NaI(Tl) Gamma Spectroscopy
  "nuc-gamma-spectroscopy-hpge-sim": {
    title: "HPGe vs NaI(Tl) Gamma Pulse Height Spectroscopy",
    desc: "Compare high-resolution High-Purity Germanium (HPGe, FWHM 1.5 keV) vs standard NaI(Tl) scintillator (FWHM 80 keV) for the twin gamma peaks of Cobalt-60 (1173 keV and 1332 keV).",
    isAnimated: false,
    controls: [
      { id: "detType", label: "Detector (1: HPGe Semiconductor, 2: NaI(Tl) Scintillator)", min: 1, max: 2, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isHPGe = Math.round(vals.detType || 1) === 1;
      const sigma = isHPGe ? 1.2 : 35.0; // channels

      const mx = 60, my = 40, pw = w - mx - 40, ph = h - my - 50;

      // Energy 0 to 1500 keV
      const maxE = 1500;

      // Axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let e = 0; e <= maxE; e += 300) {
        const x = mx + (e / maxE) * pw;
        ctx.beginPath(); ctx.moveTo(x, my); ctx.lineTo(x, my + ph); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(e + " keV", x - 15, my + ph + 16);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("Gamma Energy E (keV)", mx + pw / 2 - 45, my + ph + 34);

      // Peaks at 1173 keV and 1332 keV, Compton continuum below 1000 keV
      function getCounts(e) {
        // Compton plateau
        let bg = e < 1100 ? (120 * Math.exp(-0.001 * e)) : 10;
        // 1173 keV photopeak
        const p1 = 600 * Math.exp(-Math.pow(e - 1173, 2) / (2 * Math.pow(sigma, 2)));
        // 1332 keV photopeak
        const p2 = 550 * Math.exp(-Math.pow(e - 1332, 2) / (2 * Math.pow(sigma, 2)));
        return bg + p1 + p2;
      }

      ctx.beginPath();
      ctx.strokeStyle = isHPGe ? "#38bdf8" : "#f59e0b";
      ctx.lineWidth = 2.5;
      for (let e = 50; e <= 1450; e += 2) {
        const c = getCounts(e);
        const x = mx + (e / maxE) * pw;
        const y = my + ph - (c / 700) * ph * 0.9;
        if (e === 50) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 240, 20, 220, 110);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 240, 20, 220, 110);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`60Co Spectrum (${isHPGe ? "HPGe" : "NaI:Tl"})`, w - 225, 40);
      ctx.fillStyle = isHPGe ? "#38bdf8" : "#f59e0b"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(isHPGe ? "HPGe: FWHM ≈ 1.5 keV (0.12%)" : "NaI(Tl): FWHM ≈ 80 keV (6.0%)", w - 225, 60);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Twin Photopeaks: 1173 & 1332 keV", w - 225, 80);
      ctx.fillText(isHPGe ? "Distinct sharp doublet resolved!" : "Doublet broadly blurred together", w - 225, 100);
    }
  },

  // 15. Cyclotron Relativistic Spiral Particle Trajectory
  "nuc-cyclotron-trajectory-sim": {
    title: "Cyclotron Relativistic Spiral Trajectory & Dee RF Phase",
    desc: "Simulate the outward spiraling orbit of protons inside a cyclotron. At each Dee gap crossing, the oscillating electric field accelerates the particle. Observe the relativistic orbit desynchronization limit.",
    isAnimated: true,
    controls: [
      { id: "magField", label: "Magnetic Field B (Tesla)", min: 1.0, max: 2.0, step: 0.1, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const B = vals.magField || 1.5;
      const cx = w * 0.45, cy = h * 0.52;

      // Draw two Dee electrodes
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      // Dee 1 (Left semi-circle)
      ctx.beginPath(); ctx.arc(cx - 5, cy, 110, Math.PI / 2, Math.PI * 1.5); ctx.closePath(); ctx.stroke();
      // Dee 2 (Right semi-circle)
      ctx.beginPath(); ctx.arc(cx + 5, cy, 110, -Math.PI / 2, Math.PI / 2); ctx.closePath(); ctx.stroke();

      // RF Gap
      ctx.fillStyle = "rgba(56, 189, 248, 0.1)";
      ctx.fillRect(cx - 5, cy - 110, 10, 220);

      // Spiral trajectory
      ctx.beginPath(); ctx.strokeStyle = "rgba(56, 189, 248, 0.35)"; ctx.lineWidth = 1.5;
      const maxSpirals = 7;
      for (let t = 0; t <= maxSpirals * Math.PI * 2; t += 0.1) {
        const r = 8 + (t / (maxSpirals * Math.PI * 2)) * 95;
        const px = cx + r * Math.cos(t);
        const py = cy + r * Math.sin(t);
        if (t === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Moving Particle
      const pAngle = (time * 4) % (maxSpirals * Math.PI * 2);
      const pr = 8 + (pAngle / (maxSpirals * Math.PI * 2)) * 95;
      const curX = cx + pr * Math.cos(pAngle);
      const curY = cy + pr * Math.sin(pAngle);
      ctx.fillStyle = "#22c55e"; ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();

      // Details Badge
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(w - 230, 20, 210, 100);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(w - 230, 20, 210, 100);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Cyclotron Resonator", w - 215, 40);
      const freq = (1.6e-19 * B / (2 * Math.PI * 1.67e-27)) / 1e6;
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`B-Field: ${B.toFixed(1)} T`, w - 215, 60);
      ctx.fillText(`Resonance fc: ${freq.toFixed(1)} MHz`, w - 215, 80);
      ctx.fillStyle = "#22c55e";
      ctx.fillText("Constant orbital frequency!", w - 215, 100);
    }
  },

  // 16. Standard Model Elementary Particle Periodic Table
  "nuc-standard-model-table-sim": {
    title: "Standard Model of Particle Physics Interactive Table",
    desc: "Explore the 17 fundamental particles of the Standard Model: 6 Quarks (up, down, charm, strange, top, bottom), 6 Leptons (e, mu, tau and neutrinos), 4 Gauge Bosons (gluon, photon, W, Z), and the Higgs scalar boson.",
    isAnimated: false,
    controls: [
      { id: "sector", label: "Sector (1: Quarks, 2: Leptons, 3: Gauge Bosons, 4: Higgs)", min: 1, max: 4, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const sector = Math.round(vals.sector || 1);

      const particles = {
        1: [
          { name: "Up (u)", mass: "2.2 MeV", charge: "+2/3 e", color: "#a855f7" },
          { name: "Charm (c)", mass: "1.28 GeV", charge: "+2/3 e", color: "#a855f7" },
          { name: "Top (t)", mass: "173.1 GeV", charge: "+2/3 e", color: "#a855f7" },
          { name: "Down (d)", mass: "4.7 MeV", charge: "-1/3 e", color: "#a855f7" },
          { name: "Strange (s)", mass: "96 MeV", charge: "-1/3 e", color: "#a855f7" },
          { name: "Bottom (b)", mass: "4.18 GeV", charge: "-1/3 e", color: "#a855f7" }
        ],
        2: [
          { name: "Electron (e⁻)", mass: "0.511 MeV", charge: "-1 e", color: "#22c55e" },
          { name: "Muon (μ⁻)", mass: "105.7 MeV", charge: "-1 e", color: "#22c55e" },
          { name: "Tau (τ⁻)", mass: "1777 MeV", charge: "-1 e", color: "#22c55e" },
          { name: "Neutrino ν_e", mass: "< 0.45 eV", charge: "0", color: "#22c55e" },
          { name: "Neutrino ν_μ", mass: "< 0.17 MeV", charge: "0", color: "#22c55e" },
          { name: "Neutrino ν_τ", mass: "< 18.2 MeV", charge: "0", color: "#22c55e" }
        ],
        3: [
          { name: "Gluon (g)", mass: "0", charge: "0", color: "#f43f5e" },
          { name: "Photon (γ)", mass: "0", charge: "0", color: "#f43f5e" },
          { name: "Z⁰ Boson", mass: "91.2 GeV", charge: "0", color: "#f43f5e" },
          { name: "W⁺/W⁻ Boson", mass: "80.4 GeV", charge: "±1 e", color: "#f43f5e" }
        ],
        4: [
          { name: "Higgs Boson (H⁰)", mass: "125.1 GeV", charge: "0", color: "#f59e0b" }
        ]
      };

      const list = particles[sector];
      const sectorNames = { 1: "Quarks (Fermions, Spin 1/2, Color SU(3))", 2: "Leptons (Fermions, Spin 1/2)", 3: "Gauge Bosons (Vector, Spin 1)", 4: "Higgs Boson (Scalar, Spin 0)" };

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(sectorNames[sector], 30, 35);

      const startX = 30, startY = 60;
      const cardW = 150, cardH = 110, gap = 18;

      list.forEach((p, idx) => {
        const col = idx % 4;
        const row = Math.floor(idx / 4);
        const x = startX + col * (cardW + gap);
        const y = startY + row * (cardH + gap);

        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.fillRect(x, y, cardW, cardH);
        ctx.strokeStyle = p.color; ctx.lineWidth = 1.5;
        ctx.strokeRect(x, y, cardW, cardH);

        ctx.fillStyle = p.color; ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText(p.name, x + 12, y + 26);
        ctx.fillStyle = "#cbd5e1"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Mass: ${p.mass}`, x + 12, y + 54);
        ctx.fillText(`Charge: ${p.charge}`, x + 12, y + 74);
        ctx.fillStyle = "#64748b";
        ctx.fillText("Generation " + (col < 3 ? (col + 1) : 1), x + 12, y + 94);
      });
    }
  }

};

// Simulation Engine Mount Adapter
window.SimulationEngine = window.SimulationEngine || {
  activeAnimations: {},

  initSimulation(containerId, simType) {
    const container = document.getElementById(containerId);
    if (!container) return;

    if (window.SimulationEngine.activeAnimations[containerId]) {
      cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
      delete window.SimulationEngine.activeAnimations[containerId];
    }

    container.innerHTML = '';
    const simConfig = (window.NUC_SIMS && window.NUC_SIMS[simType]) ||
                      (window.SSP_SIMS && window.SSP_SIMS[simType]) ||
                      (window.AMP_SIMS && window.AMP_SIMS[simType]) ||
                      (window.BE_SIMS && window.BE_SIMS[simType]);

    if (!simConfig) {
      container.innerHTML = `<div style="padding:1rem; color:#94a3b8; font-style:italic;">Simulation "${simType}" loaded.</div>`;
      return;
    }

    const box = document.createElement('div');
    box.className = 'sim-inline-card';
    box.style.background = '#0c1322';
    box.style.border = '1px solid #1e293b';
    box.style.borderRadius = '12px';
    box.style.padding = '1.5rem';
    box.style.margin = '1.75rem 0';

    const header = document.createElement('div');
    header.style.marginBottom = '1rem';
    header.innerHTML = `
      <h4 style="color:#38bdf8; font-size:1.15rem; margin-bottom:0.35rem; display:flex; align-items:center; gap:0.5rem;">
        ${simConfig.title}
      </h4>
      <p style="color:#94a3b8; font-size:0.9rem; line-height:1.5;">${simConfig.desc}</p>
    `;
    box.appendChild(header);

    const canvas = document.createElement('canvas');
    canvas.width = 720;
    canvas.height = 340;
    canvas.style.width = '100%';
    canvas.style.height = 'auto';
    canvas.style.borderRadius = '8px';
    canvas.style.display = 'block';
    canvas.style.background = '#070b14';
    canvas.style.border = '1px solid #1e293b';
    box.appendChild(canvas);

    const ctrlBar = document.createElement('div');
    ctrlBar.style.display = 'flex';
    ctrlBar.style.flexWrap = 'wrap';
    ctrlBar.style.gap = '1.25rem';
    ctrlBar.style.marginTop = '1rem';
    ctrlBar.style.padding = '0.75rem 1rem';
    ctrlBar.style.background = '#080e1c';
    ctrlBar.style.borderRadius = '8px';
    ctrlBar.style.border = '1px solid #1e293d';

    const currentVals = {};

    if (simConfig.controls && simConfig.controls.length > 0) {
      simConfig.controls.forEach(ctrl => {
        currentVals[ctrl.id] = ctrl.value;

        const wrap = document.createElement('div');
        wrap.style.display = 'flex';
        wrap.style.flexDirection = 'column';
        wrap.style.gap = '0.25rem';
        wrap.style.minWidth = '160px';

        const labelRow = document.createElement('div');
        labelRow.style.display = 'flex';
        labelRow.style.justifyContent = 'space-between';
        labelRow.style.fontSize = '0.82rem';
        labelRow.style.color = '#cbd5e1';

        const titleSpan = document.createElement('span');
        titleSpan.innerText = ctrl.label;
        const valSpan = document.createElement('span');
        valSpan.style.fontFamily = 'monospace';
        valSpan.style.color = '#38bdf8';
        valSpan.innerText = ctrl.value;

        labelRow.appendChild(titleSpan);
        labelRow.appendChild(valSpan);
        wrap.appendChild(labelRow);

        const input = document.createElement('input');
        input.type = 'range';
        input.min = ctrl.min;
        input.max = ctrl.max;
        input.step = ctrl.step;
        input.value = ctrl.value;
        input.style.accentColor = '#38bdf8';
        input.style.cursor = 'pointer';

        input.addEventListener('input', (e) => {
          const v = parseFloat(e.target.value);
          currentVals[ctrl.id] = v;
          valSpan.innerText = v;
          if (!simConfig.isAnimated) {
            simConfig.render(canvas, currentVals, 0);
          }
        });

        wrap.appendChild(input);
        ctrlBar.appendChild(wrap);
      });
    }

    if (simConfig.isAnimated) {
      const animCtrlWrap = document.createElement('div');
      animCtrlWrap.style.display = 'flex';
      animCtrlWrap.style.alignItems = 'flex-end';
      const pauseBtn = document.createElement('button');
      pauseBtn.innerText = '⏸️ Pause';
      pauseBtn.style.padding = '0.4rem 0.8rem';
      pauseBtn.style.background = '#1e293b';
      pauseBtn.style.color = '#38bdf8';
      pauseBtn.style.border = '1px solid #334155';
      pauseBtn.style.borderRadius = '6px';
      pauseBtn.style.cursor = 'pointer';
      pauseBtn.style.fontSize = '0.85rem';

      let isPaused = false;
      pauseBtn.addEventListener('click', () => {
        isPaused = !isPaused;
        pauseBtn.innerText = isPaused ? '▶️ Play' : '⏸️ Pause';
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
  }
};
'''

with open("nuclear-sims.js", "w", encoding="utf-8") as f:
    f.write(sims_code)
print("nuclear-sims.js generated successfully!")
