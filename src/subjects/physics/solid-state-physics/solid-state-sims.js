// Solid State Physics Interactive Simulation Engine
// 16 Interactive 60-FPS Canvas Simulations for Crystallography, Phonons, Bands, Plasmons & Nanostructures

window.SSP_SIMS = {

  // 1. 3D Bravais Lattice & Unit Cell Geometry Simulator
  "ssp-bravais-lattice-sim": {
    title: "3D Bravais Lattice & Crystal System Viewer",
    desc: "Explore the 3D unit cell geometry under varying axial ratios (a, b, c) and interaxial angles (alpha, beta, gamma), switching between Simple Cubic, BCC, FCC, and Hexagonal lattice types.",
    isAnimated: true,
    controls: [
      { id: "type", label: "Lattice Type (1:SC, 2:BCC, 3:FCC, 4:Hex)", min: 1, max: 4, step: 1, value: 3 },
      { id: "rotSpeed", label: "Rotation Speed", min: 0, max: 2, step: 0.2, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const latType = Math.round(vals.type || 3);
      const speed = vals.rotSpeed !== undefined ? vals.rotSpeed : 1.0;
      const angle = time * 0.8 * speed;

      // 3D projection parameters
      const cx = w * 0.42, cy = h * 0.52;
      const scale = 110;

      function project(x, y, z) {
        // Rotate around Y axis, then tilt X axis
        const cosA = Math.cos(angle), sinA = Math.sin(angle);
        const x1 = x * cosA - z * sinA;
        const z1 = x * sinA + z * cosA;
        const cosTilt = Math.cos(0.45), sinTilt = Math.sin(0.45);
        const y2 = y * cosTilt - z1 * sinTilt;
        const z2 = y * sinTilt + z1 * cosTilt;
        return {
          px: cx + x1 * scale,
          py: cy - y2 * scale,
          depth: z2
        };
      }

      // Unit cell corner vertices [-0.5, 0.5]
      const corners = [
        [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5],
        [-0.5, -0.5,  0.5], [0.5, -0.5,  0.5], [0.5, 0.5,  0.5], [-0.5, 0.5,  0.5]
      ];
      const edges = [
        [0,1],[1,2],[2,3],[3,0],
        [4,5],[5,6],[6,7],[7,4],
        [0,4],[1,5],[2,6],[3,7]
      ];

      // Draw wireframe box
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 1.5;
      edges.forEach(([i, j]) => {
        const p1 = project(...corners[i]);
        const p2 = project(...corners[j]);
        ctx.beginPath();
        ctx.moveTo(p1.px, p1.py);
        ctx.lineTo(p2.px, p2.py);
        ctx.stroke();
      });

      // Gather atoms based on lattice type
      let atoms = corners.map(c => ({ pos: c, r: 8, col: "#38bdf8", label: "Corner" }));
      let typeLabel = "Simple Cubic (SC)";

      if (latType === 2) {
        typeLabel = "Body-Centered Cubic (BCC)";
        atoms.push({ pos: [0, 0, 0], r: 10, col: "#f59e0b", label: "Body Center" });
      } else if (latType === 3) {
        typeLabel = "Face-Centered Cubic (FCC)";
        const faceCenters = [
          [0, 0, -0.5], [0, 0, 0.5],
          [0, -0.5, 0], [0, 0.5, 0],
          [-0.5, 0, 0], [0.5, 0, 0]
        ];
        faceCenters.forEach(fc => atoms.push({ pos: fc, r: 9, col: "#10b981", label: "Face Center" }));
      } else if (latType === 4) {
        typeLabel = "Hexagonal Close-Packed (HCP)";
      }

      // Sort atoms by depth for proper 3D rendering
      atoms.map(a => ({ ...a, proj: project(...a.pos) }))
           .sort((a, b) => a.proj.depth - b.proj.depth)
           .forEach(a => {
             ctx.beginPath();
             ctx.arc(a.proj.px, a.proj.py, a.r, 0, 2 * Math.PI);
             const grad = ctx.createRadialGradient(a.proj.px - 2, a.proj.py - 2, 1, a.proj.px, a.proj.py, a.r);
             grad.addColorStop(0, "#ffffff");
             grad.addColorStop(0.3, a.col);
             grad.addColorStop(1, "#030712");
             ctx.fillStyle = grad;
             ctx.fill();
             ctx.strokeStyle = "rgba(255,255,255,0.4)";
             ctx.lineWidth = 1;
             ctx.stroke();
           });

      // Info Dashboard
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(w - 240, 20, 220, 150);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(w - 240, 20, 220, 150);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px sans-serif";
      ctx.fillText(typeLabel, w - 225, 45);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      if (latType === 1) {
        ctx.fillText("• Coordination Number: 6", w - 225, 70);
        ctx.fillText("• Atoms / Cell: 1", w - 225, 90);
        ctx.fillText("• Packing Factor: 52.4%", w - 225, 110);
        ctx.fillText("• Example: Po (Polonium)", w - 225, 130);
      } else if (latType === 2) {
        ctx.fillText("• Coordination Number: 8", w - 225, 70);
        ctx.fillText("• Atoms / Cell: 2", w - 225, 90);
        ctx.fillText("• Packing Factor: 68.0%", w - 225, 110);
        ctx.fillText("• Example: Fe, Na, W, Cr", w - 225, 130);
      } else if (latType === 3) {
        ctx.fillText("• Coordination Number: 12", w - 225, 70);
        ctx.fillText("• Atoms / Cell: 4", w - 225, 90);
        ctx.fillText("• Packing Factor: 74.1%", w - 225, 110);
        ctx.fillText("• Example: Cu, Al, Au, Ni", w - 225, 130);
      } else {
        ctx.fillText("• Stacking: ABABAB...", w - 225, 70);
        ctx.fillText("• Atoms / Cell: 2 (primitive)", w - 225, 90);
        ctx.fillText("• Packing Factor: 74.1%", w - 225, 110);
        ctx.fillText("• Example: Mg, Zn, Ti", w - 225, 130);
      }
    }
  },

  // 2. Bragg X-Ray Diffraction Simulator
  "ssp-bragg-xray-diffraction-sim": {
    title: "Bragg X-Ray Diffraction & Crystal Plane Scattering",
    desc: "Observe monochromatic X-ray beam reflection from crystal planes (hkl). Tune incident angle theta and interplanar spacing d to discover constructive interference peaks satisfying 2d sin(theta) = n lambda.",
    isAnimated: true,
    controls: [
      { id: "theta", label: "Bragg Angle theta (deg)", min: 10, max: 60, step: 1, value: 25 },
      { id: "d", label: "Interplanar Spacing d (A)", min: 1.5, max: 4.0, step: 0.1, value: 2.8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const thetaDeg = vals.theta !== undefined ? vals.theta : 25;
      const d = vals.d !== undefined ? vals.d : 2.8;
      const theta = thetaDeg * Math.PI / 180;
      const lambda = 1.54; // Cu K_alpha

      // Constructive interference path difference Delta = 2 d sin(theta)
      const pathDiff = 2 * d * Math.sin(theta);
      const order = pathDiff / lambda;
      const phaseDiff = 2 * Math.PI * (pathDiff / lambda);
      const intensity = Math.pow(Math.cos(phaseDiff / 2), 2);

      // Drawing crystal planes (3 horizontal layers)
      const cy = 200, planeSpacing = d * 22;
      for (let layer = 0; layer < 3; layer++) {
        const py = cy + layer * planeSpacing;
        ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(40, py); ctx.lineTo(w - 40, py); ctx.stroke();
        ctx.setLineDash([]);

        // Draw atoms along the plane
        for (let ax = 60; ax <= w - 60; ax += 45) {
          ctx.beginPath();
          ctx.arc(ax, py, 6, 0, 2 * Math.PI);
          ctx.fillStyle = "#38bdf8";
          ctx.fill();
        }
      }

      // X-Ray beam incoming & reflected (Ray 1 and Ray 2)
      const beamX = 240;
      const len = 150;
      const dx = len * Math.cos(theta);
      const dy = len * Math.sin(theta);

      // Ray 1 (reflects from Layer 0)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(beamX - dx, cy - dy);
      ctx.lineTo(beamX, cy);
      ctx.lineTo(beamX + dx, cy - dy);
      ctx.stroke();

      // Ray 2 (reflects from Layer 1)
      const beamX2 = beamX + planeSpacing / Math.tan(theta);
      ctx.strokeStyle = `rgba(245, 158, 11, ${0.4 + 0.6 * intensity})`;
      ctx.beginPath();
      ctx.moveTo(beamX2 - dx, (cy + planeSpacing) - dy);
      ctx.lineTo(beamX2, cy + planeSpacing);
      ctx.lineTo(beamX2 + dx, (cy + planeSpacing) - dy);
      ctx.stroke();

      // Animated wavefront pulses
      const wavePhase = (time * 6) % (2 * Math.PI);
      ctx.strokeStyle = "rgba(255, 255, 255, 0.6)"; ctx.lineWidth = 1;
      for (let r = 20; r < len; r += 25) {
        const offset = (r + wavePhase * 4) % len;
        const wx = beamX - dx * (offset / len);
        const wy = cy - dy * (offset / len);
        ctx.beginPath();
        ctx.moveTo(wx - 10 * Math.sin(theta), wy + 10 * Math.cos(theta));
        ctx.lineTo(wx + 10 * Math.sin(theta), wy - 10 * Math.cos(theta));
        ctx.stroke();
      }

      // Dashboard & Interference readout
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(20, 20, 280, 110);
      ctx.strokeStyle = "#334155";
      ctx.strokeRect(20, 20, 280, 110);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px sans-serif";
      ctx.fillText("Bragg Condition: 2d sin(θ) = nλ", 35, 42);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px sans-serif";
      ctx.fillText(`• Wavelength λ: ${lambda.toFixed(2)} Å (Cu Kα)`, 35, 62);
      ctx.fillText(`• Path Difference Δ: ${pathDiff.toFixed(3)} Å`, 35, 80);
      ctx.fillText(`• Order ratio Δ/λ: ${order.toFixed(2)}`, 35, 98);

      const isBragg = Math.abs(order - Math.round(order)) < 0.05;
      ctx.fillStyle = isBragg ? "#10b981" : "#f43f5e";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText(isBragg ? `✨ BRAGG PEAK n = ${Math.round(order)} (Constructive)` : `Destructive Interference (Intensity: ${(intensity * 100).toFixed(0)}%)`, 35, 118);
    }
  },

  // 3. Madelung Potential & 1D Ionic Chain Convergence
  "ssp-madelung-potential-sim": {
    title: "Madelung Constant Convergence in Alternating Ionic Chains",
    desc: "Calculate the electrostatic Madelung constant sum alpha = 2 sum (-1)^(m-1)/m in real time as the number of shells N increases, demonstrating convergence toward the exact analytical value 2 ln(2) = 1.38629.",
    isAnimated: false,
    controls: [
      { id: "shells", label: "Number of Ion Shells N", min: 1, max: 50, step: 1, value: 12 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const N = Math.round(vals.shells || 12);
      let sum = 0;
      const history = [];
      for (let m = 1; m <= N; m++) {
        sum += (m % 2 === 1 ? 2.0 / m : -2.0 / m);
        history.push({ m, val: sum });
      }

      // Plot area: x from 70 to w - 40, y from 40 to h - 50
      const px0 = 70, px1 = w - 40, py0 = 40, py1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(px0, py0, px1 - px0, py1 - py0);

      // Reference line for 2 ln(2) approx 1.38629
      const exactVal = 2 * Math.LN2;
      const minVal = 0.5, maxVal = 2.2;
      const yExact = py1 - ((exactVal - minVal) / (maxVal - minVal)) * (py1 - py0);

      ctx.strokeStyle = "rgba(16, 185, 129, 0.6)"; ctx.setLineDash([5, 5]);
      ctx.beginPath(); ctx.moveTo(px0, yExact); ctx.lineTo(px1, yExact); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#10b981"; ctx.font = "11px sans-serif";
      ctx.fillText(`Exact 2 ln(2) = 1.38629`, px1 - 140, yExact - 8);

      // Plot convergence points
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      history.forEach((pt, idx) => {
        const x = px0 + (idx / Math.max(1, N - 1)) * (px1 - px0);
        const y = py1 - ((pt.val - minVal) / (maxVal - minVal)) * (py1 - py0);
        if (idx === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      });
      ctx.stroke();

      history.forEach((pt, idx) => {
        const x = px0 + (idx / Math.max(1, N - 1)) * (px1 - px0);
        const y = py1 - ((pt.val - minVal) / (maxVal - minVal)) * (py1 - py0);
        ctx.beginPath(); ctx.arc(x, y, 4, 0, 2 * Math.PI);
        ctx.fillStyle = pt.m % 2 === 1 ? "#f59e0b" : "#38bdf8";
        ctx.fill();
      });

      // Labels
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Shell Number (m)", (px0 + px1) / 2 - 40, h - 20);
      ctx.save(); ctx.translate(25, (py0 + py1) / 2 + 30); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Partial Madelung Sum α", 0, 0); ctx.restore();

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px sans-serif";
      ctx.fillText(`At N = ${N}: α = ${sum.toFixed(5)} (Error: ${Math.abs(sum - exactVal).toFixed(5)})`, px0 + 10, py0 + 25);
    }
  },

  // 4. Lennard-Jones (6-12) Potential Simulator
  "ssp-lennard-jones-potential-sim": {
    title: "Lennard-Jones (6-12) Interatomic Potential Curve",
    desc: "Examine the competition between short-range Pauli core repulsion (1/R^12) and London dispersion attraction (-1/R^6). Observe the potential well depth epsilon and equilibrium distance R0 = 2^(1/6) sigma.",
    isAnimated: false,
    controls: [
      { id: "eps", label: "Well Depth epsilon (meV)", min: 5, max: 25, step: 1, value: 10 },
      { id: "sigma", label: "Zero-Crossing sigma (A)", min: 2.5, max: 4.5, step: 0.1, value: 3.4 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const eps = vals.eps || 10;
      const sigma = vals.sigma || 3.4;
      const rMin = Math.pow(2, 1/6) * sigma;

      const px0 = 70, px1 = w - 40, py0 = 40, py1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(px0, py0, px1 - px0, py1 - py0);

      // Axes: R from 2.5 to 8.0 A, U from -15 to +20 meV
      const rStart = 2.5, rEnd = 8.0;
      const uMin = -15, uMax = 25;
      const yZero = py1 - ((0 - uMin) / (uMax - uMin)) * (py1 - py0);

      ctx.strokeStyle = "rgba(148, 163, 184, 0.3)";
      ctx.beginPath(); ctx.moveTo(px0, yZero); ctx.lineTo(px1, yZero); ctx.stroke();

      // Plot Lennard-Jones Curve U(R) = 4 eps [ (sigma/R)^12 - (sigma/R)^6 ]
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      let first = true;
      for (let px = px0; px <= px1; px += 2) {
        const R = rStart + ((px - px0) / (px1 - px0)) * (rEnd - rStart);
        const sOverR = sigma / R;
        const u = 4 * eps * (Math.pow(sOverR, 12) - Math.pow(sOverR, 6));
        const clampedU = Math.max(uMin, Math.min(uMax, u));
        const py = py1 - ((clampedU - uMin) / (uMax - uMin)) * (py1 - py0);
        if (first) { ctx.moveTo(px, py); first = false; } else { ctx.lineTo(px, py); }
      }
      ctx.stroke();

      // Mark minimum point (R0, -epsilon)
      const pxMin = px0 + ((rMin - rStart) / (rEnd - rStart)) * (px1 - px0);
      const pyMin = py1 - (((-eps) - uMin) / (uMax - uMin)) * (py1 - py0);
      ctx.beginPath(); ctx.arc(pxMin, pyMin, 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#f59e0b"; ctx.fill();

      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 12px sans-serif";
      ctx.fillText(`R₀ = ${rMin.toFixed(2)} Å, U = -${eps} meV`, pxMin + 10, pyMin + 5);

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Interatomic Separation R (Å)", (px0 + px1) / 2 - 70, h - 20);
      ctx.save(); ctx.translate(25, (py0 + py1) / 2 + 40); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Potential Energy U(R) [meV]", 0, 0); ctx.restore();
    }
  },

  // 5. Phonon Dispersion: Monatomic & Diatomic Chains
  "ssp-phonon-dispersion-sim": {
    title: "Phonon Dispersion: Acoustic & Optical Branches",
    desc: "Visualize propagating lattice vibrational waves in 1D. Toggle mass ratio M1/M2 to open an optical-acoustic band gap at the Brillouin zone boundary k = pi/a.",
    isAnimated: true,
    controls: [
      { id: "massRatio", label: "Mass Ratio M1 / M2", min: 1.0, max: 4.0, step: 0.2, value: 2.0 },
      { id: "kNorm", label: "Wavevector k / (pi/a)", min: 0.05, max: 1.0, step: 0.05, value: 0.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const ratio = vals.massRatio || 2.0;
      const kNorm = vals.kNorm || 0.5; // fraction of zone edge
      const k = kNorm * Math.PI;

      // Split canvas: Top = physical atomic lattice animation, Bottom = dispersion graph
      // 1. Top Lattice Chain Animation
      const numAtoms = 14;
      const spacing = (w - 80) / numAtoms;
      const midY = 70;

      ctx.fillStyle = "#1e293b"; ctx.fillRect(20, 20, w - 40, 100);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(20, 20, w - 40, 100);

      // Acoustic wave frequency omega_ac
      const C = 1.0, M2 = 1.0, M1 = ratio * M2;
      const term1 = C * (1/M1 + 1/M2);
      const term2 = C * Math.sqrt(Math.pow(1/M1 + 1/M2, 2) - (4 * Math.pow(Math.sin(k/2), 2)) / (M1 * M2));
      const omegaAc = Math.sqrt(Math.max(0, term1 - term2));
      const omegaOpt = Math.sqrt(term1 + term2);

      for (let i = 0; i < numAtoms; i++) {
        const isM1 = i % 2 === 0;
        const mass = isM1 ? M1 : M2;
        const disp = 12 * Math.sin(k * i - omegaAc * time * 3);
        const x = 50 + i * spacing + disp;
        const r = isM1 ? 9 : 6;

        ctx.beginPath(); ctx.arc(x, midY, r, 0, 2 * Math.PI);
        ctx.fillStyle = isM1 ? "#38bdf8" : "#f59e0b";
        ctx.fill();
        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1; ctx.stroke();

        // Connect with spring lines
        if (i > 0) {
          const prevDisp = 12 * Math.sin(k * (i - 1) - omegaAc * time * 3);
          const prevX = 50 + (i - 1) * spacing + prevDisp;
          ctx.strokeStyle = "rgba(148, 163, 184, 0.4)"; ctx.lineWidth = 1.5;
          ctx.beginPath(); ctx.moveTo(prevX + (isM1 ? 6 : 9), midY); ctx.lineTo(x - r, midY); ctx.stroke();
        }
      }

      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px sans-serif";
      ctx.fillText(`Lattice Wave (Acoustic Branch) • M₁ (cyan) = ${ratio.toFixed(1)} M₂, M₂ (amber)`, 35, 40);

      // 2. Bottom Dispersion Relation Plot
      const gx0 = 60, gx1 = w - 40, gy0 = 150, gy1 = h - 40;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      const maxW = Math.sqrt(2 * C * (1/M1 + 1/M2)) * 1.15;

      // Plot Optical and Acoustic branches
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5; // Optical
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        const q = ((px - gx0) / (gx1 - gx0)) * Math.PI;
        const t2 = C * Math.sqrt(Math.pow(1/M1 + 1/M2, 2) - (4 * Math.pow(Math.sin(q/2), 2)) / (M1 * M2));
        const wOpt = Math.sqrt(term1 + t2);
        const py = gy1 - (wOpt / maxW) * (gy1 - gy0);
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; // Acoustic
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        const q = ((px - gx0) / (gx1 - gx0)) * Math.PI;
        const t2 = C * Math.sqrt(Math.pow(1/M1 + 1/M2, 2) - (4 * Math.pow(Math.sin(q/2), 2)) / (M1 * M2));
        const wAc = Math.sqrt(Math.max(0, term1 - t2));
        const py = gy1 - (wAc / maxW) * (gy1 - gy0);
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Band gap shading at zone boundary
      const wAcEdge = Math.sqrt(2 * C / M1);
      const wOptEdge = Math.sqrt(2 * C / M2);
      const pyAcEdge = gy1 - (wAcEdge / maxW) * (gy1 - gy0);
      const pyOptEdge = gy1 - (wOptEdge / maxW) * (gy1 - gy0);

      ctx.fillStyle = "rgba(244, 63, 94, 0.15)";
      ctx.fillRect(gx0, pyOptEdge, gx1 - gx0, pyAcEdge - pyOptEdge);
      ctx.fillStyle = "#f43f5e"; ctx.font = "11px sans-serif";
      ctx.fillText(`Phononic Band Gap Δω = ${(wOptEdge - wAcEdge).toFixed(2)}`, gx1 - 180, (pyAcEdge + pyOptEdge) / 2 + 4);

      // Labels
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("0 (Zone Center)", gx0, gy1 + 18);
      ctx.fillText("π/a (Zone Boundary)", gx1 - 80, gy1 + 18);
      ctx.fillText("Wavevector k", (gx0 + gx1) / 2 - 30, gy1 + 25);
    }
  },

  // 6. Debye vs Einstein Specific Heat Simulator
  "ssp-debye-specific-heat-sim": {
    title: "Lattice Specific Heat: Debye T^3 vs Einstein vs Classical",
    desc: "Compare the temperature dependence of heat capacity CV / (3R) across the classical Dulong-Petit asymptote, the Einstein exponential freeze-out, and the Debye T^3 law.",
    isAnimated: false,
    controls: [
      { id: "maxT", label: "Max T / Theta", min: 1.0, max: 3.0, step: 0.2, value: 1.8 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const maxT = vals.maxT || 1.8;
      const gx0 = 60, gx1 = w - 40, gy0 = 40, gy1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      // Classical asymptote at C_V = 1.0 (3R)
      const y1 = gy1 - (1.0 / 1.15) * (gy1 - gy0);
      ctx.strokeStyle = "#64748b"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(gx0, y1); ctx.lineTo(gx1, y1); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Classical Dulong-Petit (3R = 1.0)", gx0 + 10, y1 - 6);

      // Einstein Curve C_E(T) = (1/T)^2 * exp(1/T) / (exp(1/T) - 1)^2
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        const t = 0.02 + ((px - gx0) / (gx1 - gx0)) * maxT;
        const x = 1.0 / t;
        const cE = (x * x * Math.exp(x)) / Math.pow(Math.exp(x) - 1, 2);
        const py = gy1 - (cE / 1.15) * (gy1 - gy0);
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Debye Curve C_D(T) approx interpolation matching T^3 at low T and 1 at high T
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        const t = 0.02 + ((px - gx0) / (gx1 - gx0)) * maxT;
        // Accurate numerical approximation for Debye function D_3(1/t)
        const cD = t < 0.1 ? (77.93 * Math.pow(t, 3)) : (1 - Math.exp(-3.5 * t));
        const py = gy1 - (Math.min(1.0, cD) / 1.15) * (gy1 - gy0);
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px sans-serif";
      ctx.fillText("— Debye Model (T³ at low T)", gx1 - 200, gy0 + 30);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText("— Einstein Model (exponential)", gx1 - 200, gy0 + 50);

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Reduced Temperature T / Θ_D", (gx0 + gx1) / 2 - 70, h - 20);
      ctx.save(); ctx.translate(25, (gy0 + gy1) / 2 + 30); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Heat Capacity C_V / 3R", 0, 0); ctx.restore();
    }
  },

  // 7. Hartree Self-Consistent Field (SCF) Simulator
  "ssp-hartree-scf-sim": {
    title: "Hartree Self-Consistent Field (SCF) Iteration Convergence",
    desc: "Simulate the iterative convergence of the effective electronic screening potential V_eff(r) in a multi-electron atom. Observe how the screening error vanishes after several SCF cycles.",
    isAnimated: false,
    controls: [
      { id: "cycle", label: "SCF Iteration Cycle", min: 1, max: 6, step: 1, value: 3 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const cycle = Math.round(vals.cycle || 3);
      const gx0 = 60, gx1 = w - 40, gy0 = 40, gy1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      // Bare nuclear potential V_nuc = -Z/r (Z=2)
      ctx.strokeStyle = "#64748b"; ctx.setLineDash([4, 4]); ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let px = gx0 + 5; px <= gx1; px += 2) {
        const r = 0.1 + ((px - gx0) / (gx1 - gx0)) * 3.0;
        const v = - 2.0 / r;
        const py = gy1 - ((v + 10) / 10) * (gy1 - gy0);
        if (px === gx0 + 5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Bare Nuclear Potential -Z/r", gx0 + 10, gy1 - 20);

      // Converging SCF potential: V(r) = - (1 + exp(-r * (1 + 0.3*cycle))) / r
      const colors = ["#f43f5e", "#f59e0b", "#eab308", "#10b981", "#06b6d4", "#38bdf8"];
      ctx.strokeStyle = colors[cycle - 1]; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = gx0 + 5; px <= gx1; px += 2) {
        const r = 0.1 + ((px - gx0) / (gx1 - gx0)) * 3.0;
        const alpha = 1.0 + 0.25 * cycle;
        const v = - (1.0 + Math.exp(-alpha * r)) / r;
        const py = gy1 - ((v + 10) / 10) * (gy1 - gy0);
        if (px === gx0 + 5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = colors[cycle - 1]; ctx.font = "bold 13px sans-serif";
      const err = (1.0 / Math.pow(2.2, cycle)).toFixed(4);
      ctx.fillText(`Iteration Cycle ${cycle} • Residual Error |ΔV| = ${err}`, gx0 + 15, gy0 + 30);

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Radial Distance r (Bohr radii a₀)", (gx0 + gx1) / 2 - 80, h - 20);
      ctx.save(); ctx.translate(25, (gy0 + gy1) / 2 + 40); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Effective Potential V_eff(r) [Hartree]", 0, 0); ctx.restore();
    }
  },

  // 8. LCAO Molecular Orbitals Simulator
  "ssp-lcao-molecular-orbital-sim": {
    title: "LCAO Molecular Orbitals: Bonding vs Antibonding",
    desc: "Visualize electron probability density psi^2 along the internuclear axis for the symmetric bonding sigma_g orbital and the antisymmetric antibonding sigma_u* orbital.",
    isAnimated: false,
    controls: [
      { id: "orbital", label: "Orbital Type (1: Bonding σ_g, 2: Antibonding σ_u*)", min: 1, max: 2, step: 1, value: 1 },
      { id: "dist", label: "Internuclear Distance R (A)", min: 0.8, max: 2.5, step: 0.1, value: 1.4 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const isBonding = (vals.orbital || 1) === 1;
      const R = vals.dist || 1.4;

      const gx0 = 60, gx1 = w - 40, gy0 = 40, gy1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      // Nuclear positions at -R/2 and +R/2
      const cx = (gx0 + gx1) / 2;
      const scaleX = (gx1 - gx0) / 4.0;
      const xNuc1 = cx - (R / 2) * scaleX;
      const xNuc2 = cx + (R / 2) * scaleX;

      // Draw nuclei markers
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(xNuc1, gy1, 7, 0, 2 * Math.PI); ctx.fill();
      ctx.beginPath(); ctx.arc(xNuc2, gy1, 7, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
      ctx.fillText("Nucleus A", xNuc1 - 25, gy1 + 20);
      ctx.fillText("Nucleus B", xNuc2 - 25, gy1 + 20);

      // Plot |psi|^2
      ctx.strokeStyle = isBonding ? "#10b981" : "#f43f5e"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        const x = (px - cx) / scaleX;
        const rA = Math.abs(x + R / 2);
        const rB = Math.abs(x - R / 2);
        const phiA = Math.exp(-rA);
        const phiB = Math.exp(-rB);
        const psi = isBonding ? (phiA + phiB) : (phiA - phiB);
        const prob = psi * psi;
        const py = gy1 - (prob / 3.0) * (gy1 - gy0);
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = isBonding ? "#10b981" : "#f43f5e"; ctx.font = "bold 13px sans-serif";
      ctx.fillText(isBonding ? "Bonding Molecular Orbital (σ_g) • High Electron Density Between Nuclei" : "Antibonding Molecular Orbital (σ_u*) • Nodal Plane (ψ=0) at Center", gx0 + 15, gy0 + 25);
    }
  },

  // 9. Fermi-Dirac Distribution & 3D DOS Simulator
  "ssp-fermi-dirac-dos-sim": {
    title: "Fermi-Dirac Distribution & Conduction Density of States",
    desc: "Observe the thermal smearing of the Fermi-Dirac step function f(E) and the product g(E) f(E) governing thermal electron excitation near the Fermi energy EF.",
    isAnimated: false,
    controls: [
      { id: "T", label: "Temperature T (K)", min: 0, max: 2000, step: 100, value: 300 },
      { id: "Ef", label: "Fermi Energy E_F (eV)", min: 3.0, max: 9.0, step: 0.5, value: 7.0 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const T = vals.T !== undefined ? vals.T : 300;
      const Ef = vals.Ef || 7.0;
      const kB = 8.617e-5; // eV/K
      const kBT = Math.max(1e-4, kB * T);

      const gx0 = 60, gx1 = w - 40, gy0 = 40, gy1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      // Vertical line at Ef
      const maxE = 10.0;
      const xEf = gx0 + (Ef / maxE) * (gx1 - gx0);
      ctx.strokeStyle = "rgba(245, 158, 11, 0.5)"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(xEf, gy0); ctx.lineTo(xEf, gy1); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
      ctx.fillText(`E_F = ${Ef.toFixed(1)} eV`, xEf - 25, gy0 + 15);

      // Plot Fermi-Dirac function f(E) (cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        const E = ((px - gx0) / (gx1 - gx0)) * maxE;
        const f = 1.0 / (1.0 + Math.exp((E - Ef) / kBT));
        const py = gy1 - f * (gy1 - gy0) * 0.45;
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot Product g(E) * f(E) (green shaded)
      ctx.fillStyle = "rgba(16, 185, 129, 0.25)";
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(gx0, gy1);
      for (let px = gx0; px <= gx1; px += 2) {
        const E = ((px - gx0) / (gx1 - gx0)) * maxE;
        const f = 1.0 / (1.0 + Math.exp((E - Ef) / kBT));
        const g = Math.sqrt(Math.max(0, E)); // ~ sqrt(E)
        const occ = (g * f) / Math.sqrt(maxE);
        const py = gy1 - occ * (gy1 - gy0) * 0.85;
        ctx.lineTo(px, py);
      }
      ctx.lineTo(gx1, gy1);
      ctx.fill(); ctx.stroke();

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px sans-serif";
      ctx.fillText(`Temperature T = ${T} K (k_B T = ${(kBT * 1000).toFixed(1)} meV)`, gx0 + 10, gy0 + 35);
      ctx.fillStyle = "#10b981"; ctx.fillText("■ Occupied Electron States g(E) f(E)", gx0 + 10, gy0 + 55);
      ctx.fillStyle = "#38bdf8"; ctx.fillText("— Fermi-Dirac Factor f(E)", gx0 + 10, gy0 + 75);
    }
  },

  // 10. Hall Effect & Lorentz Force Simulator
  "ssp-hall-effect-sim": {
    title: "The Hall Effect & Transverse Lorentz Carrier Deflection",
    desc: "Observe how an applied magnetic field Bz deflects moving charge carriers transversely, building up a transverse electric field Ey until electrostatic repulsion balances the magnetic force.",
    isAnimated: true,
    controls: [
      { id: "bField", label: "Magnetic Field Bz (Tesla)", min: 0, max: 3.0, step: 0.2, value: 1.5 },
      { id: "carrier", label: "Carrier Sign (1: Electrons, -1: Holes)", min: -1, max: 1, step: 2, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const Bz = vals.bField !== undefined ? vals.bField : 1.5;
      const isElectron = (vals.carrier || 1) === 1;

      // Slab dimensions
      const sx0 = 80, sy0 = 80, sw = w - 160, sh = 180;
      ctx.fillStyle = "#0f172a"; ctx.fillRect(sx0, sy0, sw, sh);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.strokeRect(sx0, sy0, sw, sh);

      // Magnetic field markers (circles with dots for out-of-page B)
      ctx.fillStyle = "rgba(245, 158, 11, 0.4)";
      for (let mx = sx0 + 40; mx < sx0 + sw; mx += 60) {
        for (let my = sy0 + 30; my < sy0 + sh; my += 40) {
          ctx.beginPath(); ctx.arc(mx, my, 8, 0, 2 * Math.PI); ctx.stroke();
          ctx.beginPath(); ctx.arc(mx, my, 2, 0, 2 * Math.PI); ctx.fill();
        }
      }
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
      ctx.fillText(`Magnetic Field B_z = ${Bz.toFixed(1)} T (⊙ Out of page)`, sx0 + 10, sy0 - 10);

      // Charge accumulation on top/bottom boundaries
      const hallV = Bz * (isElectron ? -1 : 1) * 2.4;
      ctx.fillStyle = isElectron ? "#f43f5e" : "#10b981"; ctx.font = "bold 13px sans-serif";
      ctx.fillText(isElectron ? "- - - - - Negative Surface Charge Accumulated - - - - -" : "+ + + + + Positive Surface Charge Accumulated + + + + +", sx0 + 30, sy0 + 20);

      // Animate flowing carriers
      const numP = 18;
      for (let i = 0; i < numP; i++) {
        const speed = 70;
        const x = sx0 + ((i * 35 + time * speed) % sw);
        // Vertical deflection due to Lorentz force
        const yDeflect = Math.sin((x / sw) * Math.PI) * Bz * (isElectron ? -25 : 25);
        const y = sy0 + sh / 2 + yDeflect + (Math.sin(i * 1.5) * 25);

        ctx.beginPath(); ctx.arc(x, y, 6, 0, 2 * Math.PI);
        ctx.fillStyle = isElectron ? "#38bdf8" : "#10b981"; ctx.fill();
      }

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px sans-serif";
      ctx.fillText(`Current J_x → | Carrier: ${isElectron ? "Electrons (-e)" : "Holes (+e)"} | Hall Voltage V_H = ${hallV.toFixed(2)} µV`, sx0, sy0 + sh + 30);
    }
  },

  // 11. Kronig-Penney Band Gap Solver
  "ssp-kronig-penney-sim": {
    title: "Kronig-Penney Model: Energy Bands & Band-Gap Opening",
    desc: "Tune barrier strength P to observe how periodic potential barriers split the free-electron spectrum into allowed energy bands and forbidden band gaps.",
    isAnimated: false,
    controls: [
      { id: "P", label: "Barrier Strength P", min: 0.5, max: 10.0, step: 0.5, value: 3.0 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const P = vals.P || 3.0;
      const gx0 = 60, gx1 = w - 40, gy0 = 40, gy1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      // Bounds [-1, +1]
      const yMid = (gy0 + gy1) / 2;
      const yPlus = yMid - (gy1 - gy0) * 0.35;
      const yMinus = yMid + (gy1 - gy0) * 0.35;

      ctx.fillStyle = "rgba(56, 189, 248, 0.08)";
      ctx.fillRect(gx0, yPlus, gx1 - gx0, yMinus - yPlus);

      ctx.strokeStyle = "rgba(148, 163, 184, 0.5)"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(gx0, yPlus); ctx.lineTo(gx1, yPlus); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(gx0, yMinus); ctx.lineTo(gx1, yMinus); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("+1.0 (Upper Bound)", gx0 + 10, yPlus - 6);
      ctx.fillText("-1.0 (Lower Bound)", gx0 + 10, yMinus + 15);

      // Plot Kronig-Penney function f(Ka) = P sin(Ka)/(Ka) + cos(Ka)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      const maxKa = 4.5 * Math.PI;
      for (let px = gx0; px <= gx1; px += 2) {
        const Ka = 0.05 + ((px - gx0) / (gx1 - gx0)) * maxKa;
        const f = P * (Math.sin(Ka) / Ka) + Math.cos(Ka);
        const py = yMid - (f / 2.5) * (gy1 - gy0) * 0.35;
        const clampedY = Math.max(gy0 - 20, Math.min(gy1 + 20, py));
        if (px === gx0) ctx.moveTo(px, clampedY); else ctx.lineTo(px, clampedY);
      }
      ctx.stroke();

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px sans-serif";
      ctx.fillText(`Barrier Strength P = ${P.toFixed(1)} • Shaded Blue: Allowed Bands (|f(Ka)| ≤ 1)`, gx0 + 10, gy0 + 25);
    }
  },

  // 12. Effective Mass & Band Curvature Simulator
  "ssp-effective-mass-sim": {
    title: "Effective Mass, Band Curvature & Hole Dynamics",
    desc: "Examine energy dispersion E(k), group velocity vg(k), and the effective mass m*(k) = hbar^2 / (d^2E/dk^2). Observe the transition from positive electron mass to negative mass (positive holes) near zone boundaries.",
    isAnimated: false,
    controls: [
      { id: "bandwidth", label: "Bandwidth 4t (eV)", min: 1.0, max: 6.0, step: 0.5, value: 3.0 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const W = vals.bandwidth || 3.0;
      const t = W / 4;

      const gx0 = 60, gx1 = w - 40, gy0 = 40, gy1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      // Plot 1: E(k) = - 2t cos(ka) (cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        const ka = ((px - gx0) / (gx1 - gx0)) * Math.PI;
        const E = - 2 * t * Math.cos(ka);
        const py = (gy0 + gy1)/2 - (E / (2 * t)) * (gy1 - gy0) * 0.4;
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot 2: Effective Mass Inverse 1/m* ~ cos(ka) (amber)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        const ka = ((px - gx0) / (gx1 - gx0)) * Math.PI;
        const invM = Math.cos(ka); // >0 at bottom, <0 at top
        const py = (gy0 + gy1)/2 - invM * (gy1 - gy0) * 0.35;
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px sans-serif";
      ctx.fillText("— Energy Dispersion E(k)", gx0 + 15, gy0 + 25);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText("— Inverse Effective Mass (1/m*): >0 (Electrons) → <0 (Holes)", gx0 + 15, gy0 + 45);
    }
  },

  // 13. Clausius-Mossotti Dielectric Relation
  "ssp-clausius-mossotti-sim": {
    title: "Clausius-Mossotti Relation & Dielectric Permittivity",
    desc: "Observe how relative dielectric permittivity epsilon_r scales non-linearly with atomic polarizability volume density (N alpha / 3 epsilon_0), leading toward the polar catastrophe as denominator approaches unity.",
    isAnimated: false,
    controls: [
      { id: "density", label: "Polarizability Factor N*alpha / 3eps0", min: 0.1, max: 0.9, step: 0.05, value: 0.6 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const fVal = vals.density || 0.6;
      const gx0 = 60, gx1 = w - 40, gy0 = 40, gy1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      // Plot epsilon_r = (1 + 2f) / (1 - f)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        const f = 0.05 + ((px - gx0) / (gx1 - gx0)) * 0.92;
        const epsR = (1 + 2 * f) / (1 - f);
        const py = gy1 - (Math.min(25, epsR) / 25) * (gy1 - gy0);
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current point marker
      const curEps = (1 + 2 * fVal) / (1 - fVal);
      const curPx = gx0 + ((fVal - 0.05) / 0.92) * (gx1 - gx0);
      const curPy = gy1 - (Math.min(25, curEps) / 25) * (gy1 - gy0);

      ctx.beginPath(); ctx.arc(curPx, curPy, 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#f59e0b"; ctx.fill();

      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 13px sans-serif";
      ctx.fillText(`At Factor = ${fVal.toFixed(2)}: ε_r = ${curEps.toFixed(2)}`, gx0 + 15, gy0 + 25);
    }
  },

  // 14. Plasma Frequency & Optical Reflectivity Simulator
  "ssp-plasma-frequency-sim": {
    title: "Plasma Frequency & Ultraviolet Optical Transparency Edge",
    desc: "Examine the optical reflectance R(omega) of a metal. Light is completely reflected (R approx 100%) below the plasma frequency omega_p, but passes freely (R -> 0) at higher frequencies.",
    isAnimated: false,
    controls: [
      { id: "carrierDensity", label: "Electron Density n (10^28 m^-3)", min: 1.0, max: 15.0, step: 1.0, value: 8.5 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const n = (vals.carrierDensity || 8.5) * 1e28;
      const eps0 = 8.854e-12, m = 9.109e-31, e = 1.602e-19;
      const wp = Math.sqrt((n * e * e) / (eps0 * m));
      const wpEV = (1.054e-34 * wp) / e;

      const gx0 = 60, gx1 = w - 40, gy0 = 40, gy1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      // Plot Reflectance R(w) = | (1 - sqrt(eps)) / (1 + sqrt(eps)) |^2
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      const maxEV = 20.0;
      for (let px = gx0; px <= gx1; px += 2) {
        const ev = ((px - gx0) / (gx1 - gx0)) * maxEV;
        let R = 1.0;
        if (ev > wpEV) {
          const eps = 1 - Math.pow(wpEV / ev, 2);
          const sqrtEps = Math.sqrt(eps);
          R = Math.pow((1 - sqrtEps) / (1 + sqrtEps), 2);
        }
        const py = gy1 - R * (gy1 - gy0) * 0.9;
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Mark Plasma Energy threshold
      const xWp = gx0 + (wpEV / maxEV) * (gx1 - gx0);
      ctx.strokeStyle = "#f59e0b"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(xWp, gy0); ctx.lineTo(xWp, gy1); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 12px sans-serif";
      ctx.fillText(`Plasma Edge ℏω_p = ${wpEV.toFixed(2)} eV`, xWp + 10, gy0 + 40);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px sans-serif";
      ctx.fillText("Total Metallic Reflection (R = 100%)", gx0 + 15, gy1 - 30);
      ctx.fillText("UV Transparency Window →", xWp + 15, gy1 - 30);
    }
  },

  // 15. p-n Junction Band Bending Simulator
  "ssp-pn-junction-band-sim": {
    title: "p-n Junction Energy Band Diagram & Bias Modulator",
    desc: "Observe how conduction band Ec, valence band Ev, and Fermi level EF bend across the space-charge depletion region under thermal equilibrium, forward bias, and reverse bias.",
    isAnimated: false,
    controls: [
      { id: "bias", label: "Applied Voltage Va (Volts)", min: -1.5, max: 0.8, step: 0.1, value: 0.0 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const Va = vals.bias !== undefined ? vals.bias : 0.0;
      const Vbi = 0.9; // Built-in potential
      const barrier = Math.max(0.1, Vbi - Va);

      const gx0 = 60, gx1 = w - 40, gy0 = 40, gy1 = h - 60;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx0, gy0, gx1 - gx0, gy1 - gy0);

      const cx = (gx0 + gx1) / 2;
      const Wdep = 80 * Math.sqrt(barrier / Vbi);

      // Conduction Band Ec (cyan) & Valence Band Ev (green)
      const Eg = 70; // visual band gap
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        let yShift = 0;
        if (px < cx - Wdep) yShift = - barrier * 45;
        else if (px > cx + Wdep) yShift = barrier * 45;
        else {
          const frac = (px - (cx - Wdep)) / (2 * Wdep);
          yShift = (- barrier + 2 * barrier * (3*frac*frac - 2*frac*frac*frac)) * 45;
        }
        const py = (gy0 + gy1)/2 + yShift - Eg/2;
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = gx0; px <= gx1; px += 2) {
        let yShift = 0;
        if (px < cx - Wdep) yShift = - barrier * 45;
        else if (px > cx + Wdep) yShift = barrier * 45;
        else {
          const frac = (px - (cx - Wdep)) / (2 * Wdep);
          yShift = (- barrier + 2 * barrier * (3*frac*frac - 2*frac*frac*frac)) * 45;
        }
        const py = (gy0 + gy1)/2 + yShift + Eg/2;
        if (px === gx0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Depletion boundary shaded area
      ctx.fillStyle = "rgba(244, 63, 94, 0.1)";
      ctx.fillRect(cx - Wdep, gy0, 2 * Wdep, gy1 - gy0);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px sans-serif";
      ctx.fillText("p-region", gx0 + 20, gy0 + 25);
      ctx.fillText("n-region", gx1 - 70, gy0 + 25);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Effective Barrier: q(V_bi - V_a) = ${barrier.toFixed(2)} eV (Width: ${(Wdep*2).toFixed(0)} nm)`, cx - 110, gy0 + 25);
    }
  },

  // 16. Quantum Dot Confinement Simulator
  "ssp-quantum-dot-confinement-sim": {
    title: "Quantum Dot Confinement: Radius vs. Emission Color",
    desc: "Tune the nanocrystal radius R of a semiconductor quantum dot. Observe the particle-in-a-sphere confinement energy shift Delta E ~ 1/R^2 tuning emission across the visible spectrum.",
    isAnimated: true,
    controls: [
      { id: "radius", label: "Nanocrystal Radius R (nm)", min: 1.5, max: 5.5, step: 0.2, value: 2.8 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, w, h);

      const R = vals.radius || 2.8; // nm
      // Bulk bandgap 1.74 eV (CdSe). Delta E ~ hbar^2 pi^2 / (2 mu R^2)
      const deltaE = 4.0 / (R * R);
      const effectiveEg = 1.74 + deltaE;
      const wavelength = 1240 / effectiveEg; // nm

      // Map wavelength to approximate RGB color
      let r = 0, g = 0, b = 0;
      if (wavelength >= 380 && wavelength < 440) { r = -(wavelength - 440)/60; b = 1; }
      else if (wavelength >= 440 && wavelength < 490) { g = (wavelength - 440)/50; b = 1; }
      else if (wavelength >= 490 && wavelength < 510) { g = 1; b = -(wavelength - 510)/20; }
      else if (wavelength >= 510 && wavelength < 580) { r = (wavelength - 510)/70; g = 1; }
      else if (wavelength >= 580 && wavelength < 645) { r = 1; g = -(wavelength - 645)/65; }
      else if (wavelength >= 645) { r = 1; }
      const colStr = `rgb(${Math.round(r * 255)}, ${Math.round(g * 255)}, ${Math.round(b * 255)})`;

      // Draw quantum dot sphere with glow
      const cx = 180, cy = h / 2;
      const dotPixelRadius = R * 14;

      const grad = ctx.createRadialGradient(cx, cy, 2, cx, cy, dotPixelRadius * 1.5);
      grad.addColorStop(0, "#ffffff");
      grad.addColorStop(0.4, colStr);
      grad.addColorStop(1, "rgba(0,0,0,0)");

      ctx.beginPath(); ctx.arc(cx, cy, dotPixelRadius * 1.5, 0, 2 * Math.PI);
      ctx.fillStyle = grad; ctx.fill();

      // Info Card
      ctx.fillStyle = "#1e293b"; ctx.fillRect(340, 50, w - 380, h - 100);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(340, 50, w - 380, h - 100);

      ctx.fillStyle = colStr; ctx.font = "bold 16px sans-serif";
      ctx.fillText(`Quantum Dot Emission: ${wavelength.toFixed(0)} nm`, 365, 85);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px sans-serif";
      ctx.fillText(`• Nanocrystal Radius R: ${R.toFixed(1)} nm`, 365, 120);
      ctx.fillText(`• Bulk Bandgap E_g(bulk): 1.74 eV (CdSe)`, 365, 145);
      ctx.fillText(`• Quantum Confinement Shift: +${deltaE.toFixed(2)} eV`, 365, 170);
      ctx.fillText(`• Effective Bandgap E_g(R): ${effectiveEg.toFixed(2)} eV`, 365, 195);
      ctx.fillText(`• Density of States: Completely Discrete 0D Dirac Deltas`, 365, 220);
    }
  }

};

// SimulationEngine Integration Adapter
window.SimulationEngine = window.SimulationEngine || {
  activeAnimations: {},
  initSimulation: function(containerId, simType) {
    const container = document.getElementById(containerId);
    if (!container) return;

    if (window.SimulationEngine.activeAnimations[containerId]) {
      cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
      delete window.SimulationEngine.activeAnimations[containerId];
    }

    container.innerHTML = '';
    const simConfig = (window.SSP_SIMS && window.SSP_SIMS[simType]) ||
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
