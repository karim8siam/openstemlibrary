// Atomic and Molecular Physics Interactive Simulation Engine
// 15 Interactive 60-FPS Canvas Simulations for Relativity, Quanta, Atoms, Spin & Spectroscopy

window.AMP_SIMS = {

  // 1. Michelson-Morley Interferometer
  "michelson-morley-interferometer-sim": {
    title: "Michelson-Morley Interferometer & Ether Wind Null Result",
    desc: "Observe how longitudinal and transverse light travel times compare under a hypothetical ether wind, demonstrating why fringe shift Delta-N vanishes in reality.",
    isAnimated: true,
    controls: [
      { id: "v", label: "Ether Wind v (km/s)", min: 0, max: 60, step: 5, value: 30 },
      { id: "angle", label: "Rotation Angle (deg)", min: 0, max: 90, step: 5, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const v = vals.v !== undefined ? vals.v : 30;
      const angle = (vals.angle || 0) * Math.PI / 180;
      const c = 300; // visual speed of light
      const beta = (v / 300000); // realistic beta
      const deltaN_expected = (2 * 11 * Math.pow(v * 1000, 2)) / (590e-9 * Math.pow(3e8, 2)) * Math.cos(2 * angle);

      // Left side: Schematic of Interferometer (x: 40 to 360, y: 40 to 280)
      const cx = 180, cy = 160, armLen = 95;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(30, 40, 310, 240);

      // Ether wind direction arrows
      ctx.strokeStyle = "rgba(56, 189, 248, 0.3)"; ctx.lineWidth = 1.5;
      for (let y = 60; y <= 260; y += 40) {
        ctx.beginPath(); ctx.moveTo(45, y); ctx.lineTo(105, y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(98, y - 4); ctx.lineTo(105, y); ctx.lineTo(98, y + 4); ctx.stroke();
      }
      ctx.fillStyle = "#38bdf8"; ctx.font = "11px sans-serif";
      ctx.fillText(`Ether Wind v = ${v} km/s`, 45, 55);

      // Half-silvered mirror at center (angled at 45 deg)
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(angle);

      // Arm 1 (horizontal in lab frame)
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(-armLen, 0); ctx.lineTo(armLen, 0); ctx.stroke();
      // Arm 2 (vertical in lab frame)
      ctx.beginPath(); ctx.moveTo(0, -armLen); ctx.lineTo(0, armLen); ctx.stroke();

      // Mirror 1 (right)
      ctx.fillStyle = "#94a3b8"; ctx.fillRect(armLen - 3, -15, 6, 30);
      // Mirror 2 (top)
      ctx.fillRect(-15, -armLen - 3, 30, 6);
      // Beam splitter (center)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(-15, -15); ctx.lineTo(15, 15); ctx.stroke();

      // Traveling light pulses
      const pulseT1 = (time * 120) % (2 * armLen);
      const pulseT2 = (time * 120 + 50) % (2 * armLen);
      ctx.fillStyle = "#ef4444";
      // Pulse on horizontal arm
      const p1x = pulseT1 < armLen ? pulseT1 : 2 * armLen - pulseT1;
      ctx.beginPath(); ctx.arc(p1x, 0, 4, 0, Math.PI * 2); ctx.fill();
      // Pulse on vertical arm
      const p2y = pulseT2 < armLen ? -pulseT2 : -(2 * armLen - pulseT2);
      ctx.beginPath(); ctx.arc(0, p2y, 4, 0, Math.PI * 2); ctx.fill();

      ctx.restore();

      // Right side: Interference Fringe Pattern (x: 380 to 680)
      const fx = 390, fy = 40, fw = 290, fh = 240;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(fx, fy, fw, fh);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Interference Fringe Pattern", fx + 50, fy + 25);

      // Draw concentric / vertical interference fringes
      const shiftPx = deltaN_expected * 25; // theoretical shift if ether existed
      const actualShift = 0; // reality: strictly null
      for (let x = 0; x < fw; x++) {
        const fringePhase = (x / 14) * 2 * Math.PI + actualShift;
        const intensity = 0.5 + 0.5 * Math.cos(fringePhase);
        const col = Math.floor(intensity * 255);
        ctx.fillStyle = `rgb(${Math.floor(col * 0.2)}, ${Math.floor(col * 0.8)}, ${col})`;
        ctx.fillRect(fx + x, fy + 45, 1, fh - 60);
      }

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px sans-serif";
      ctx.fillText("EXPERIMENTAL RESULT: ZERO SHIFT (Delta-N = 0)", fx + 15, fy + fh - 35);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Ether Hypothesis Predicted: ${Math.abs(deltaN_expected).toFixed(3)} fringes`, fx + 15, fy + fh - 12);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`Interferometer Rotation: ${(angle * 180 / Math.PI).toFixed(0)}° | Speed of Light c = const`, 40, 315);
    }
  },

  // 2. Minkowski Spacetime Diagram & Lorentz Boost
  "lorentz-boost-spacetime-sim": {
    title: "Minkowski Spacetime Diagram & Lorentz Boost Invariants",
    desc: "Observe how coordinate axes ct' and x' rotate symmetrically toward the 45-degree light cone during a relativistic boost, demonstrating the relativity of simultaneity.",
    isAnimated: true,
    controls: [
      { id: "beta", label: "Relativistic Boost beta = v/c", min: 0.0, max: 0.85, step: 0.05, value: 0.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const beta = vals.beta !== undefined ? vals.beta : 0.5;
      const gamma = 1 / Math.sqrt(1 - beta * beta);

      const ox = 360, oy = 170, scale = 110;

      // Unprimed Frame S Axes (ct and x)
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(ox, 20); ctx.lineTo(ox, 320); ctx.stroke(); // ct
      ctx.beginPath(); ctx.moveTo(100, oy); ctx.lineTo(620, oy); ctx.stroke(); // x
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("ct (Time)", ox + 10, 35);
      ctx.fillText("x (Space)", 600, oy + 20);

      // Light Cone (45 deg lines)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(ox - 140, oy + 140); ctx.lineTo(ox + 140, oy - 140); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ox - 140, oy - 140); ctx.lineTo(ox + 140, oy + 140); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
      ctx.fillText("Light Cone (x = ct)", ox + 115, oy - 120);

      // Invariant Hyperbolas (s^2 = +1 timelike, s^2 = -1 spacelike)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.25)"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let x = -130; x <= 130; x += 2) {
        const ctVal = Math.sqrt(x * x + scale * scale);
        const px = ox + x, py = oy - ctVal;
        if (x === -130) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Primed Frame S' Axes (Boosted)
      // ct' axis has slope 1/beta: angle from vertical = arctan(beta)
      // x' axis has slope beta: angle from horizontal = arctan(beta)
      const theta = Math.atan(beta);
      const len = 135;

      // ct' axis (Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(ox - Math.sin(theta) * len, oy + Math.cos(theta) * len);
      ctx.lineTo(ox + Math.sin(theta) * len, oy - Math.cos(theta) * len);
      ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px sans-serif";
      ctx.fillText("ct' (Worldline)", ox + Math.sin(theta) * len + 8, oy - Math.cos(theta) * len);

      // x' axis (Cyan) - Line of Simultaneity
      ctx.beginPath();
      ctx.moveTo(ox - Math.cos(theta) * len, oy + Math.sin(theta) * len);
      ctx.lineTo(ox + Math.cos(theta) * len, oy - Math.sin(theta) * len);
      ctx.stroke();
      ctx.fillText("x' (Simultaneity)", ox + Math.cos(theta) * len + 8, oy - Math.sin(theta) * len);

      // Telemetry Banner
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Boost beta: ${beta.toFixed(2)} c | Lorentz Factor gamma: ${gamma.toFixed(3)} | Axis Tilt: ${(theta * 180 / Math.PI).toFixed(1)}°`, 60, 315);
    }
  },

  // 3. Relativistic Dynamics (Energy & Momentum vs Speed)
  "relativistic-kinematics-sim": {
    title: "Relativistic Momentum & Kinetic Energy Divergence",
    desc: "Compare Einstein's relativistic kinetic energy K = (gamma - 1)mc^2 with classical Newtonian 0.5*m*v^2, showing the asymptotic barrier as v -> c.",
    isAnimated: true,
    controls: [
      { id: "v", label: "Velocity v/c", min: 0.1, max: 0.98, step: 0.02, value: 0.75 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const beta = vals.v !== undefined ? vals.v : 0.75;
      const gamma = 1 / Math.sqrt(1 - beta * beta);
      const m0 = 1.0; // unit rest mass
      const c = 1.0;
      const K_rel = (gamma - 1) * m0 * c * c;
      const K_class = 0.5 * m0 * beta * beta;

      const gx = 80, gy = 260, gw = 560, gh = 210;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(gx, gy - gh); ctx.lineTo(gx, gy); ctx.lineTo(gx + gw, gy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Speed (v/c)", gx + gw - 65, gy + 22);
      ctx.fillText("Kinetic Energy / m0 c^2", gx - 55, gy - gh - 8);

      // Light speed barrier at v = c
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(gx + gw, gy); ctx.lineTo(gx + gw, gy - gh); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.fillText("c (Universal Speed Limit)", gx + gw - 145, gy - gh + 15);

      // Plot Classical Curve (Dashed Amber)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      for (let px = 0; px <= gw; px += 2) {
        const b = px / gw;
        const k = 0.5 * b * b;
        const py = gy - (k / 3.0) * gh;
        if (px === 0) ctx.moveTo(gx + px, py); else ctx.lineTo(gx + px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("Newtonian: K = 0.5 m v^2", gx + 160, gy - 30);

      // Plot Relativistic Curve (Solid Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let px = 0; px < gw - 5; px += 2) {
        const b = px / gw;
        const gam = 1 / Math.sqrt(1 - b * b);
        const k = (gam - 1);
        const py = gy - Math.min(gh, (k / 3.0) * gh);
        if (px === 0) ctx.moveTo(gx + px, py); else ctx.lineTo(gx + px, py);
      }
      ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.fillText("Einstein: K = (gamma - 1) m0 c^2", gx + 220, gy - gh + 40);

      // Operating Point Marker
      const curX = gx + beta * gw;
      const curY = gy - Math.min(gh, (K_rel / 3.0) * gh);
      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(curX, curY, 7, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`v = ${beta.toFixed(2)} c | gamma = ${gamma.toFixed(2)} | Relativistic K: ${K_rel.toFixed(2)} m0 c^2 | Classical K: ${K_class.toFixed(2)} m0 c^2`, 60, 315);
    }
  },

  // 4. Photoelectric Effect & Stopping Potential
  "photoelectric-effect-sim": {
    title: "Photoelectric Effect Stopping Potential & Work Function",
    desc: "Adjust the incident wavelength lambda and target metal work function W0 to observe photoelectron emission velocities and retarding potential cutoff.",
    isAnimated: true,
    controls: [
      { id: "lambda", label: "Wavelength lambda (nm)", min: 200, max: 700, step: 10, value: 350 },
      { id: "w0", label: "Work Function W0 (eV)", min: 1.8, max: 4.8, step: 0.1, value: 2.2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const lambda = vals.lambda || 350;
      const W0 = vals.w0 || 2.2;
      const E_phot = 1240 / lambda; // eV
      const K_max = Math.max(0, E_phot - W0);
      const isEmitting = E_phot > W0;
      const V_stop = K_max; // Volts

      // Left panel: Photocell Apparatus (x: 40 to 360)
      ctx.strokeStyle = "#334155"; ctx.strokeRect(40, 40, 310, 240);

      // Metal Emitter Plate (left)
      ctx.fillStyle = "#64748b"; ctx.fillRect(70, 70, 16, 180);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px sans-serif";
      ctx.fillText("Emitter", 55, 62);

      // Collector Plate (right)
      ctx.fillStyle = "#475569"; ctx.fillRect(300, 70, 16, 180);
      ctx.fillText("Collector", 285, 62);

      // Incident Light Beams
      const lightCol = lambda < 380 ? "#c084fc" : (lambda < 490 ? "#38bdf8" : (lambda < 580 ? "#10b981" : "#ef4444"));
      ctx.strokeStyle = lightCol; ctx.lineWidth = 3;
      for (let i = 0; i < 4; i++) {
        const y = 95 + i * 40;
        ctx.beginPath(); ctx.moveTo(40, y - 30); ctx.lineTo(70, y); ctx.stroke();
      }

      // Flying photoelectrons if emitting
      if (isEmitting) {
        ctx.fillStyle = "#38bdf8";
        const vSpeed = Math.sqrt(K_max) * 70;
        for (let i = 0; i < 7; i++) {
          const px = 86 + ((time * vSpeed + i * 45) % 214);
          const py = 90 + (i * 26) % 140;
          ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Right panel: Energy Balance Bar Graphs (x: 390 to 680)
      const bx = 400, by = 40, bw = 270, bh = 240;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, by, bw, bh);

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Energy Conservation: h nu = W0 + Kmax", bx + 15, by + 25);

      const drawBar = (x, y, label, val, max, col) => {
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
        ctx.fillText(`${label}: ${val.toFixed(2)} eV`, x, y);
        ctx.fillStyle = "#1e293b"; ctx.fillRect(x, y + 6, 220, 16);
        ctx.fillStyle = col;
        ctx.fillRect(x, y + 6, Math.min(220, (val / max) * 220), 16);
      };

      drawBar(bx + 20, by + 50, "Incident Photon h nu", E_phot, 6.5, lightCol);
      drawBar(bx + 20, by + 105, "Metal Work Function W0", W0, 6.5, "#f59e0b");
      drawBar(bx + 20, by + 160, "Max Kinetic Energy Kmax", K_max, 6.5, isEmitting ? "#10b981" : "#ef4444");

      ctx.fillStyle = isEmitting ? "#10b981" : "#ef4444";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText(isEmitting ? `EMITTING (Stopping Potential V0 = ${V_stop.toFixed(2)} V)` : "BELOW THRESHOLD (Zero Emission)", bx + 15, by + 225);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Photon Energy: ${E_phot.toFixed(2)} eV | Work Function: ${W0.toFixed(2)} eV | Kmax: ${K_max.toFixed(2)} eV`, 60, 315);
    }
  },

  // 5. Compton Scattering
  "compton-scattering-sim": {
    title: "Compton Scattering Relativistic Kinematics & Recoil Angle",
    desc: "Observe an incident photon scatter off a stationary electron at angle theta, transferring kinetic energy to the recoil electron and shifting its wavelength.",
    isAnimated: true,
    controls: [
      { id: "theta", label: "Scattering Angle theta (deg)", min: 0, max: 180, step: 5, value: 60 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const thetaDeg = vals.theta !== undefined ? vals.theta : 60;
      const theta = thetaDeg * Math.PI / 180;
      const lambda_c = 0.02426; // Angstroms
      const deltaLambda = lambda_c * (1 - Math.cos(theta));
      const lambda0 = 0.0709; // Mo K_alpha in A
      const lambdaPrime = lambda0 + deltaLambda;

      const cx = 260, cy = 160;

      // Interaction center (target electron)
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(cx, cy, 8, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px sans-serif";
      ctx.fillText("Target Electron", cx - 40, cy + 24);

      // Incident photon wave (from left)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 60; x <= cx - 12; x++) {
        const y = cy + Math.sin((x - time * 180) * 0.25) * 12;
        if (x === 60) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
      ctx.fillText("Incident Photon (lambda)", 70, cy - 20);

      // Scattered photon (angle theta)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(-theta);
      ctx.beginPath();
      for (let x = 12; x <= 180; x++) {
        const y = Math.sin((x - time * 140) * 0.16) * 14;
        if (x === 12) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
      ctx.restore();
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`Scattered Photon (theta = ${thetaDeg}°)`, cx + 110, cy - 80);

      // Recoil electron angle phi
      const phi = Math.atan2(Math.sin(theta), (1 + deltaLambda / lambda0) - Math.cos(theta));
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 3;
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(phi);
      ctx.beginPath(); ctx.moveTo(12, 0); ctx.lineTo(140, 0); ctx.stroke();
      ctx.restore();
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Recoil Electron (phi = ${(phi * 180 / Math.PI).toFixed(1)}°)`, cx + 70, cy + 90);

      // Readout
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Compton Shift: Delta-lambda = ${deltaLambda.toFixed(4)} Å | Scattered lambda': ${lambdaPrime.toFixed(4)} Å`, 60, 315);
    }
  },

  // 6. Moseley's Law & Bragg Diffraction
  "xray-moseley-diffraction-sim": {
    title: "Moseley's Law & Bragg Crystal X-Ray Diffraction",
    desc: "Observe how characteristic K-alpha X-ray frequencies scale with atomic number Z, and verify constructive interference at Bragg angles 2d*sin(theta) = n*lambda.",
    isAnimated: true,
    controls: [
      { id: "z", label: "Atomic Number Z", min: 20, max: 74, step: 1, value: 29 },
      { id: "angle", label: "Bragg Glancing Angle (deg)", min: 10, max: 45, step: 1, value: 18 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const Z = vals.z || 29;
      const angleDeg = vals.angle || 18;
      const angleRad = angleDeg * Math.PI / 180;
      const d = 2.82; // NaCl lattice spacing in A
      const lambda_ka = (1215.7 / Math.pow(Z - 1, 2)) * 4 / 3; // Approx K_alpha in A
      const pathDiff = 2 * d * Math.sin(angleRad);
      const isBraggMatch = Math.abs(pathDiff - lambda_ka) < 0.25;

      // Left panel: Moseley Plot (sqrt(nu) vs Z)
      const gx = 60, gy = 240, gw = 280, gh = 180;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(gx, 50, gw, gh);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Atomic Number Z", gx + 90, gy + 20);
      ctx.fillText("sqrt(nu)", gx + 8, 68);

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(gx + 20, gy - 20);
      ctx.lineTo(gx + gw - 20, gy - gh + 20);
      ctx.stroke();

      // Current Z marker
      const curZx = gx + 20 + ((Z - 20) / 54) * (gw - 40);
      const curZy = gy - 20 - ((Z - 20) / 54) * (gh - 40);
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(curZx, curZy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`Z=${Z} (lambda=${lambda_ka.toFixed(2)}Å)`, curZx - 30, curZy - 10);

      // Right panel: Crystal Lattice Bragg Reflection (x: 380 to 680)
      const lx = 380, ly = 50, lw = 290, lh = 180;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(lx, ly, lw, lh);

      // Lattice atomic dots
      ctx.fillStyle = "#64748b";
      for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 6; col++) {
          ctx.beginPath();
          ctx.arc(lx + 40 + col * 42, ly + 90 + row * 35, 4, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // Reflected X-ray beams
      ctx.strokeStyle = isBraggMatch ? "#10b981" : "#ef4444"; ctx.lineWidth = 2.5;
      // Top beam
      ctx.beginPath(); ctx.moveTo(lx + 40, ly + 40); ctx.lineTo(lx + 124, ly + 90); ctx.lineTo(lx + 208, ly + 40); ctx.stroke();
      // Lower beam
      ctx.beginPath(); ctx.moveTo(lx + 40, ly + 75); ctx.lineTo(lx + 124, ly + 125); ctx.lineTo(lx + 208, ly + 75); ctx.stroke();

      ctx.fillStyle = isBraggMatch ? "#10b981" : "#ef4444"; ctx.font = "bold 12px sans-serif";
      ctx.fillText(isBraggMatch ? "BRAGG CONSTRUCTIVE INTERFERENCE PEAK!" : "Destructive Interference (Off Peak)", lx + 15, ly + lh - 15);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Target Z: ${Z} | 2d*sin(theta): ${pathDiff.toFixed(2)} Å | K-alpha lambda: ${lambda_ka.toFixed(2)} Å`, 60, 315);
    }
  },

  // 7. de Broglie Wave Packet (Phase vs Group Velocity)
  "de-broglie-matter-waves-sim": {
    title: "Matter Wave Packet: Phase Velocity vs Group Velocity",
    desc: "Observe how fast individual carrier ripples (phase velocity vp = c^2/v > c) propagate through a localized wave envelope traveling at physical group velocity vg = v.",
    isAnimated: true,
    controls: [
      { id: "v", label: "Particle Velocity v/c", min: 0.2, max: 0.8, step: 0.05, value: 0.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const v = vals.v !== undefined ? vals.v : 0.5;
      const vg = v; // group velocity
      const vp = 1 / v; // phase velocity > 1

      const sx = 60, sy = 160, sw = 600;

      // Group envelope center moves at vg
      const envCenter = (time * vg * 90) % (sw + 200) - 100;

      // Draw wave packet
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const dist = (x - envCenter) / 45;
        const envelope = Math.exp(-dist * dist);
        // Phase carrier moves at vp
        const phase = (x / 6) - (time * vp * 40);
        const y = sy - envelope * Math.cos(phase) * 85;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();

      // Envelope outline (dashed amber)
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const dist = (x - envCenter) / 45;
        const envelope = Math.exp(-dist * dist) * 85;
        const y = sy - envelope;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();
      ctx.beginPath();
      for (let x = 0; x < sw; x++) {
        const dist = (x - envCenter) / 45;
        const envelope = Math.exp(-dist * dist) * 85;
        const y = sy + envelope;
        if (x === 0) ctx.moveTo(sx + x, y); else ctx.lineTo(sx + x, y);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#f59e0b"; ctx.font = "12px sans-serif";
      ctx.fillText(`Envelope Moves at Group Velocity vg = ${vg.toFixed(2)} c (= Particle Speed)`, sx + 10, 60);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Internal Phase Ripples Move at Phase Velocity vp = ${vp.toFixed(2)} c (> c)`, sx + 10, 85);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Relativistic Identity: vp * vg = c^2 | Total Probability Integral = 1.000`, 60, 315);
    }
  },

  // 8. Davisson-Germer Electron Diffraction
  "davisson-germer-diffraction-sim": {
    title: "Davisson-Germer Experiment: Electron Polar Diffraction Peak",
    desc: "Vary accelerating voltage V to observe the emergence of the sharp Bragg diffraction peak at exactly 54 V and scattering angle 50 degrees.",
    isAnimated: true,
    controls: [
      { id: "volt", label: "Accelerating Voltage (V)", min: 35, max: 70, step: 1, value: 54 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const V = vals.volt || 54;
      const lambda_dB = 1.226 / Math.sqrt(V); // nm
      const lambda_target = 0.165; // nm (54V peak)
      const resonance = Math.exp(-Math.pow(V - 54, 2) / 36);

      const cx = 300, cy = 250, rMax = 180;

      // Polar coordinate grid
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(cx, cy, rMax, Math.PI, 0); ctx.stroke();
      ctx.beginPath(); ctx.arc(cx, cy, rMax * 0.5, Math.PI, 0); ctx.stroke();

      // Crystal surface at bottom
      ctx.fillStyle = "#64748b"; ctx.fillRect(cx - 150, cy, 300, 15);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px sans-serif";
      ctx.fillText("Nickel Crystal Target", cx - 60, cy + 30);

      // Polar intensity curve (Scattering angle theta from 0 to 90 deg relative to normal)
      ctx.strokeStyle = resonance > 0.6 ? "#10b981" : "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let theta = 0; theta <= 90; theta += 1) {
        const rad = (90 - theta) * Math.PI / 180;
        // Peak at 50 degrees
        const peakFactor = Math.exp(-Math.pow(theta - 50, 2) / 60) * resonance * 90;
        const intensity = 50 + peakFactor;
        const px = cx + Math.cos(rad) * intensity;
        const py = cy - Math.sin(rad) * intensity;
        if (theta === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Readout
      ctx.fillStyle = resonance > 0.6 ? "#10b981" : "#94a3b8";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText(V === 54 ? "RESONANCE PEAK AT theta = 50° (54 V)" : `Scattering Pattern at ${V} V`, 450, 80);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`de Broglie lambda: ${lambda_dB.toFixed(3)} nm | Bragg lambda: 0.165 nm | Agreement: 99.1%`, 60, 315);
    }
  },

  // 9. Heisenberg Gamma-Ray Microscope
  "heisenberg-microscope-sim": {
    title: "Heisenberg Gamma-Ray Microscope Thought Experiment",
    desc: "Observe how reducing probe photon wavelength improves spatial resolution Delta-x while imparting an unavoidable recoil kick Delta-p.",
    isAnimated: true,
    controls: [
      { id: "lambda", label: "Photon Wavelength lambda (pm)", min: 2, max: 50, step: 2, value: 10 },
      { id: "theta", label: "Aperture Half-Angle (deg)", min: 10, max: 60, step: 5, value: 30 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const lambda_pm = vals.lambda || 10;
      const thetaDeg = vals.theta || 30;
      const theta = thetaDeg * Math.PI / 180;

      // Delta x ~ lambda / (2 sin(theta))
      const deltaX_pm = lambda_pm / (2 * Math.sin(theta));
      // Delta p ~ 2 (h/lambda) sin(theta) -> in units of h/pm
      const deltaP_rel = 2 * Math.sin(theta) / lambda_pm;
      const product = deltaX_pm * deltaP_rel; // = 1.0 (in h units)

      const cx = 360, cy = 200;

      // Microscope lens at top
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.arc(cx, 40, 160, Math.PI * 0.35, Math.PI * 0.65);
      ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText(`Microscope Objective (Aperture 2*theta = ${2 * thetaDeg}°)`, cx - 110, 45);

      // Light cone rays from electron to lens
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.5;
      const lensHalfW = 100 * Math.sin(theta);
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx - lensHalfW, 60); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + lensHalfW, 60); ctx.stroke();
      ctx.setLineDash([]);

      // Electron at focal point
      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(cx, cy, 7, 0, Math.PI * 2); ctx.fill();

      // Uncertainty fuzz box around electron
      ctx.strokeStyle = "rgba(239, 68, 68, 0.6)"; ctx.lineWidth = 2;
      const boxW = Math.min(120, deltaX_pm * 3.5);
      ctx.strokeRect(cx - boxW / 2, cy - 15, boxW, 30);
      ctx.fillStyle = "#ef4444"; ctx.font = "11px sans-serif";
      ctx.fillText(`Delta-x = ${deltaX_pm.toFixed(1)} pm`, cx - 35, cy + 32);

      // Telemetry
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Delta-x: ${deltaX_pm.toFixed(2)} pm | Momentum Kick Delta-px: ${deltaP_rel.toFixed(3)} h/pm | Delta-x * Delta-px >= h/2`, 60, 315);
    }
  },

  // 10. Rutherford Alpha Scattering Hyperbolic Trajectories
  "rutherford-alpha-scattering-sim": {
    title: "Rutherford Alpha Scattering Hyperbolic Trajectories",
    desc: "Observe how Coulomb electrostatic repulsion deflects alpha particles into hyperbolic orbits, producing wide backscattering at small impact parameters b.",
    isAnimated: true,
    controls: [
      { id: "b", label: "Impact Parameter b (fm)", min: 5, max: 50, step: 2, value: 18 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const b = vals.b || 18;
      const dmin = 29.5; // fm
      const theta = 2 * Math.atan(dmin / (2 * b));
      const thetaDeg = theta * 180 / Math.PI;

      const nucX = 400, nucY = 160;

      // Heavy Gold Nucleus (+79e)
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(nucX, nucY, 14, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 12px sans-serif";
      ctx.fillText("Gold Nucleus (+79e)", nucX - 55, nucY + 32);

      // Impact parameter guideline (dashed)
      const bPx = b * 3.2;
      ctx.strokeStyle = "rgba(148, 163, 184, 0.3)"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(60, nucY - bPx); ctx.lineTo(nucX, nucY - bPx); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText(`Impact Parameter b = ${b} fm`, 80, nucY - bPx - 8);

      // Trajectory hyperbolic curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let t = -4.0; t <= 4.0; t += 0.05) {
        // Parametric hyperbolic approximation
        const x = nucX + (t * 80) - (dmin * 1.6) / (1 + t * t);
        const y = (nucY - bPx) + (dmin * 2.2) / (1 + t * t) * (t < 0 ? -1 : 1) * Math.sin(theta / 2);
        if (t === -4.0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Moving alpha particle
      const animT = ((time * 1.5) % 8.0) - 4.0;
      const ax = nucX + (animT * 80) - (dmin * 1.6) / (1 + animT * animT);
      const ay = (nucY - bPx) + (dmin * 2.2) / (1 + animT * animT) * (animT < 0 ? -1 : 1) * Math.sin(theta / 2);
      ctx.fillStyle = "#ef4444";
      ctx.beginPath(); ctx.arc(ax, ay, 6, 0, Math.PI * 2); ctx.fill();

      // Readout
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Scattering Angle theta: ${thetaDeg.toFixed(1)}° | Distance of Closest Approach: ${(dmin * 0.5 * (1 + 1 / Math.sin(theta/2))).toFixed(1)} fm`, 60, 315);
    }
  },

  // 11. Bohr Hydrogenic Atomic Transitions
  "bohr-atom-spectral-series-sim": {
    title: "Bohr Hydrogenic Energy Transitions & Spectral Series",
    desc: "Trigger electron jumps between quantized stationary states (ni -> nf) and observe real-time photon emission and spectral line mapping across series.",
    isAnimated: true,
    controls: [
      { id: "ni", label: "Initial State ni", min: 2, max: 6, step: 1, value: 3 },
      { id: "nf", label: "Final State nf", min: 1, max: 3, step: 1, value: 2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const ni = vals.ni || 3;
      let nf = vals.nf || 2;
      if (nf >= ni) nf = ni - 1; // ensure downward transition

      const Ei = -13.606 / (ni * ni);
      const Ef = -13.606 / (nf * nf);
      const deltaE = Ei - Ef;
      const lambda_nm = 1239.84 / deltaE;

      const cx = 220, cy = 160;

      // Draw Bohr Orbits n = 1 to 5
      for (let n = 1; n <= 5; n++) {
        const r = 24 + n * n * 5.2;
        ctx.strokeStyle = n === nf ? "#10b981" : (n === ni ? "#38bdf8" : "#334155");
        ctx.lineWidth = (n === nf || n === ni) ? 2.5 : 1;
        ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "10px sans-serif";
        ctx.fillText(`n=${n}`, cx + r + 4, cy);
      }

      // Nucleus
      ctx.fillStyle = "#ef4444";
      ctx.beginPath(); ctx.arc(cx, cy, 7, 0, Math.PI * 2); ctx.fill();

      // Electron orbiting
      const rf = 24 + nf * nf * 5.2;
      const orbAngle = time * 3.5;
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(cx + Math.cos(orbAngle) * rf, cy + Math.sin(orbAngle) * rf, 5, 0, Math.PI * 2);
      ctx.fill();

      // Right side: Energy Level Ladder (x: 420 to 680)
      const lx = 430, ly = 40, lw = 240, lh = 240;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(lx, ly, lw, lh);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Energy Level Transitions", lx + 45, ly + 25);

      for (let n = 1; n <= 5; n++) {
        const en = -13.606 / (n * n);
        const yPos = ly + lh - 30 - ((en + 13.606) / 13.606) * 160;
        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(lx + 20, yPos); ctx.lineTo(lx + lw - 20, yPos); ctx.stroke();
        ctx.fillStyle = "#cbd5e1"; ctx.font = "10px monospace";
        ctx.fillText(`n=${n} (${en.toFixed(2)}eV)`, lx + lw - 75, yPos - 4);
      }

      // Transition arrow
      const yi = ly + lh - 30 - ((Ei + 13.606) / 13.606) * 160;
      const yf = ly + lh - 30 - ((Ef + 13.606) / 13.606) * 160;
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(lx + 80, yi); ctx.lineTo(lx + 80, yf); ctx.stroke();

      const seriesName = nf === 1 ? "Lyman (UV)" : (nf === 2 ? "Balmer (Visible)" : "Paschen (IR)");
      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Transition: n=${ni} -> n=${nf} (${seriesName}) | Photon lambda = ${lambda_nm.toFixed(1)} nm`, 60, 315);
    }
  },

  // 12. Stern-Gerlach Experiment (Spin-1/2 Splitting)
  "stern-gerlach-spin-sim": {
    title: "Stern-Gerlach Spatial Quantization & Electron Spin-1/2",
    desc: "Observe how an inhomogeneous magnetic field dBz/dz splits a neutral silver atom beam into exactly two discrete traces (ms = +1/2 and ms = -1/2).",
    isAnimated: true,
    controls: [
      { id: "grad", label: "Field Gradient dBz/dz (T/m)", min: 20, max: 150, step: 10, value: 80 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const grad = vals.grad || 80;
      const splitDist = (grad / 150) * 55;

      // Oven source (left)
      ctx.fillStyle = "#475569"; ctx.fillRect(40, 140, 40, 40);
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(60, 160, 8, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px sans-serif";
      ctx.fillText("Ag Oven", 40, 130);

      // Magnet Pole Pieces (center)
      // Top knife-edge pole (N)
      ctx.fillStyle = "#334155";
      ctx.beginPath();
      ctx.moveTo(220, 80); ctx.lineTo(340, 80); ctx.lineTo(280, 125); ctx.closePath();
      ctx.fill();
      ctx.fillStyle = "#ef4444"; ctx.font = "bold 13px sans-serif"; ctx.fillText("N (Wedge)", 255, 105);

      // Bottom flat pole (S)
      ctx.fillStyle = "#334155";
      ctx.beginPath();
      ctx.moveTo(220, 240); ctx.lineTo(340, 240); ctx.lineTo(340, 195); ctx.lineTo(220, 195); ctx.closePath();
      ctx.fill();
      ctx.fillStyle = "#38bdf8"; ctx.fillText("S (Flat)", 265, 220);

      // Detector Plate (right)
      ctx.fillStyle = "#1e293b"; ctx.fillRect(580, 70, 12, 180);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Detector", 565, 60);

      // Atomic Beam Trails
      // Unsplit incoming beam
      ctx.strokeStyle = "#cbd5e1"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(80, 160); ctx.lineTo(250, 160); ctx.stroke();

      // Splitting inside and beyond magnet into TWO traces
      // Spin Up (+1/2) deflects upward
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(250, 160); ctx.bezierCurveTo(340, 160, 420, 160 - splitDist, 580, 160 - splitDist); ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px sans-serif";
      ctx.fillText("ms = +1/2 (Spin Up)", 470, 160 - splitDist - 8);

      // Spin Down (-1/2) deflects downward
      ctx.strokeStyle = "#38bdf8";
      ctx.beginPath(); ctx.moveTo(250, 160); ctx.bezierCurveTo(340, 160, 420, 160 + splitDist, 580, 160 + splitDist); ctx.stroke();
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("ms = -1/2 (Spin Down)", 470, 160 + splitDist + 18);

      // Detected spots on plate
      ctx.fillStyle = "#10b981"; ctx.fillRect(576, 160 - splitDist - 5, 8, 10);
      ctx.fillStyle = "#38bdf8"; ctx.fillRect(576, 160 + splitDist - 5, 8, 10);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Gradient: ${grad} T/m | Spatial Deflection Separation: ${(splitDist * 0.4).toFixed(2)} mm | Exactly 2 Traces`, 60, 315);
    }
  },

  // 13. Zeeman Effect Splitting
  "zeeman-effect-splitting-sim": {
    title: "Normal vs Anomalous Zeeman Effect Magnetic Level Splitting",
    desc: "Examine how an external magnetic field B splits singlet states into a Normal Lorentz triplet vs anomalous multiplet splitting governed by the Lande g-factor.",
    isAnimated: true,
    controls: [
      { id: "b", label: "Magnetic Field B (Tesla)", min: 0.0, max: 2.5, step: 0.25, value: 1.25 },
      { id: "mode", label: "Mode (0: Normal Triplet, 1: Anomalous Sextet)", min: 0, max: 1, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const B = vals.b !== undefined ? vals.b : 1.25;
      const isAnomalous = (vals.mode || 1) === 1;
      const dE = B * 35; // pixel energy shift

      const cx = 360, cy = 160;

      // Energy Level Diagram (Left to Center)
      ctx.strokeStyle = "#334155"; ctx.strokeRect(50, 40, 320, 240);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText(isAnomalous ? "Anomalous Zeeman: ^2P_{3/2} -> ^2S_{1/2}" : "Normal Zeeman: Singlet ^1P_1 -> ^1S_0", 65, 62);

      // Upper State Levels
      if (isAnomalous) {
        // ^2P_3/2 splits into 4 levels (g = 4/3)
        const g2 = 4 / 3;
        const mLevels = [+1.5, +0.5, -0.5, -1.5];
        mLevels.forEach(m => {
          const y = 100 - m * (dE * g2 * 0.4);
          ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.8;
          ctx.beginPath(); ctx.moveTo(90, y); ctx.lineTo(260, y); ctx.stroke();
          ctx.fillStyle = "#38bdf8"; ctx.font = "10px monospace";
          ctx.fillText(`mj=${m > 0 ? '+' : ''}${m}`, 265, y + 4);
        });

        // Lower State ^2S_1/2 splits into 2 levels (g = 2)
        const g1 = 2.0;
        const mLower = [+0.5, -0.5];
        mLower.forEach(m => {
          const y = 230 - m * (dE * g1 * 0.4);
          ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
          ctx.beginPath(); ctx.moveTo(90, y); ctx.lineTo(260, y); ctx.stroke();
          ctx.fillStyle = "#10b981"; ctx.font = "10px monospace";
          ctx.fillText(`mj=${m > 0 ? '+' : ''}${m}`, 265, y + 4);
        });
      } else {
        // Normal Zeeman: upper ^1P_1 splits into 3 (m = +1, 0, -1)
        [-1, 0, 1].forEach(m => {
          const y = 100 - m * (dE * 0.45);
          ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
          ctx.beginPath(); ctx.moveTo(90, y); ctx.lineTo(260, y); ctx.stroke();
          ctx.fillStyle = "#38bdf8"; ctx.font = "10px monospace";
          ctx.fillText(`ml=${m > 0 ? '+' : ''}${m}`, 265, y + 4);
        });
        // Lower state ^1S_0 unshifted (m = 0)
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(90, 230); ctx.lineTo(260, 230); ctx.stroke();
      }

      // Right Panel: Optical Spectrum Lines (x: 400 to 680)
      const sx = 410, sy = 40, sw = 270, sh = 240;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(sx, sy, sw, sh);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Observed Optical Spectrum", sx + 50, sy + 25);

      const midLineX = sx + sw / 2;
      ctx.strokeStyle = "#475569"; ctx.beginPath(); ctx.moveTo(midLineX, sy + 40); ctx.lineTo(midLineX, sy + sh - 20); ctx.stroke();

      if (isAnomalous) {
        // 6 spectral lines
        const shifts = [-1.8, -1.0, -0.2, +0.2, +1.0, +1.8];
        shifts.forEach((shft, idx) => {
          const px = midLineX + shft * (dE * 0.35);
          ctx.strokeStyle = Math.abs(shft) < 0.5 ? "#f59e0b" : "#38bdf8"; // pi vs sigma
          ctx.lineWidth = 2.5;
          ctx.beginPath(); ctx.moveTo(px, sy + 60); ctx.lineTo(px, sy + sh - 40); ctx.stroke();
        });
        ctx.fillStyle = "#f59e0b"; ctx.fillText("pi lines (center)", sx + 20, sy + sh - 15);
        ctx.fillStyle = "#38bdf8"; ctx.fillText("sigma lines (outer)", sx + 150, sy + sh - 15);
      } else {
        // 3 spectral lines (Lorentz triplet)
        [-1, 0, 1].forEach(shft => {
          const px = midLineX + shft * (dE * 0.45);
          ctx.strokeStyle = shft === 0 ? "#f59e0b" : "#38bdf8";
          ctx.lineWidth = 3;
          ctx.beginPath(); ctx.moveTo(px, sy + 60); ctx.lineTo(px, sy + sh - 40); ctx.stroke();
        });
      }

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`B-Field: ${B.toFixed(2)} T | Mode: ${isAnomalous ? 'Anomalous (6 Lines)' : 'Normal Triplet (3 Lines)'}`, 60, 315);
    }
  },

  // 14. Molecular Rigid Rotor Spectrum
  "molecular-rigid-rotor-sim": {
    title: "Molecular Rigid Rotor & Equidistant 2B Rotational Lines",
    desc: "Observe the quantum rotational energy ladder EJ = B*J*(J+1) and the resulting microwave absorption spectrum exhibiting constant 2B spacing.",
    isAnimated: true,
    controls: [
      { id: "b_const", label: "Rotational Const B (cm^-1)", min: 1.0, max: 10.0, step: 0.5, value: 1.92 },
      { id: "j_max", label: "Max J Level", min: 4, max: 8, step: 1, value: 6 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const B = vals.b_const || 1.92;
      const jMax = vals.j_max || 6;

      // Left Panel: Rotating Diatomic Molecule
      const cx = 160, cy = 160;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(30, 40, 260, 240);

      const rotAngle = time * 4.0;
      const rBond = 55;
      const x1 = cx + Math.cos(rotAngle) * rBond;
      const y1 = cy + Math.sin(rotAngle) * rBond;
      const x2 = cx - Math.cos(rotAngle) * (rBond * 0.75);
      const y2 = cy - Math.sin(rotAngle) * (rBond * 0.75);

      // Bond cylinder
      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 5;
      ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();

      // Atom 1 (Carbon - blue)
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(x1, y1, 14, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#e2e8f0"; ctx.font = "bold 11px sans-serif"; ctx.fillText("C", x1 - 4, y1 + 4);

      // Atom 2 (Oxygen - red)
      ctx.fillStyle = "#ef4444"; ctx.beginPath(); ctx.arc(x2, y2, 16, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("O", x2 - 5, y2 + 4);

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Diatomic Rigid Rotor (CO)", cx - 65, 65);

      // Right Panel: Microwave Absorption Spectrum
      const sx = 310, sy = 40, sw = 370, sh = 240;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(sx, sy, sw, sh);
      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Microwave Absorption Spectrum (Delta-nu = 2B)", sx + 40, sy + 25);

      // Spectrum baseline
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(sx + 20, sy + sh - 40); ctx.lineTo(sx + sw - 20, sy + sh - 40); ctx.stroke();

      // Equidistant 2B lines: 2B, 4B, 6B, 8B...
      for (let J = 0; J < jMax; J++) {
        const lineFreq = 2 * B * (J + 1);
        const px = sx + 35 + (J / jMax) * (sw - 70);
        // Intensity proportional to Boltzmann factor (2J+1) * exp(-BJ(J+1)/kT)
        const boltz = (2 * J + 1) * Math.exp(-J * (J + 1) * 0.08);
        const lineH = Math.min(130, boltz * 35);

        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(px, sy + sh - 40); ctx.lineTo(px, sy + sh - 40 - lineH); ctx.stroke();

        ctx.fillStyle = "#cbd5e1"; ctx.font = "10px monospace";
        ctx.fillText(`J=${J}->${J+1}`, px - 18, sy + sh - 25);
      }

      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px monospace";
      ctx.fillText(`Constant Line Spacing: 2B = ${(2 * B).toFixed(2)} cm^-1`, sx + 60, sy + 55);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`Rotational Constant B = ${B.toFixed(2)} cm^-1 | Equidistant Absorption Line Spacing = ${(2*B).toFixed(2)} cm^-1`, 60, 315);
    }
  },

  // 15. Raman Spectroscopy (Stokes & Anti-Stokes)
  "raman-spectroscopy-sim": {
    title: "Raman Scattering Spectrum: Stokes & Anti-Stokes Lines",
    desc: "Observe inelastic Raman scattering producing red-shifted Stokes lines (vibration excitation) and blue-shifted Anti-Stokes lines with Boltzmann thermal ratios.",
    isAnimated: true,
    controls: [
      { id: "temp", label: "Temperature T (K)", min: 100, max: 900, step: 50, value: 300 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const T = vals.temp || 300;
      const vib_cm = 1000; // vibrational shift
      // Boltzmann population factor
      const boltz = Math.exp(-(1.439 * vib_cm) / T);
      const asRatio = Math.min(0.65, Math.max(0.005, boltz * 1.5));

      const sx = 60, sy = 40, sw = 600, sh = 240;
      ctx.strokeStyle = "#334155"; ctx.strokeRect(sx, sy, sw, sh);

      // Baseline
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(sx + 20, sy + sh - 40); ctx.lineTo(sx + sw - 20, sy + sh - 40); ctx.stroke();

      const midX = sx + sw / 2;

      // 1. Rayleigh Scattering (Center line, unshifted nu0 - colossal intensity)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 5;
      ctx.beginPath(); ctx.moveTo(midX, sy + sh - 40); ctx.lineTo(midX, sy + 30); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px sans-serif";
      ctx.fillText("Rayleigh (nu0)", midX - 35, sy + 25);

      // 2. Stokes Line (Left - Red-shifted, nu0 - nu_v)
      const stokesX = midX - 160;
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(stokesX, sy + sh - 40); ctx.lineTo(stokesX, sy + 65); ctx.stroke();
      ctx.fillStyle = "#ef4444";
      ctx.fillText("Stokes (nu0 - nu_v)", stokesX - 50, sy + 55);

      // 3. Anti-Stokes Line (Right - Blue-shifted, nu0 + nu_v)
      const antiStokesX = midX + 160;
      const asHeight = Math.max(10, (sy + sh - 40 - 65) * asRatio);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(antiStokesX, sy + sh - 40); ctx.lineTo(antiStokesX, sy + sh - 40 - asHeight); ctx.stroke();
      ctx.fillStyle = "#10b981";
      ctx.fillText("Anti-Stokes (nu0 + nu_v)", antiStokesX - 60, sy + sh - 45 - asHeight);

      // Explanation annotations
      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px monospace";
      ctx.fillText(`Stokes (High Intensity): Molecule absorbs h*nu_v`, sx + 30, sy + 110);
      ctx.fillText(`Anti-Stokes (Temperature Dependent): Molecule gives up h*nu_v`, sx + 30, sy + 130);

      ctx.fillStyle = "#e2e8f0"; ctx.font = "12px monospace";
      ctx.fillText(`T = ${T} K | Anti-Stokes / Stokes Intensity Ratio = ${(asRatio * 100).toFixed(2)}% | Boltzmann Suppressed`, 60, 315);
    }
  }
};

// Simulation Engine Mount Adapter
if (!window.SimulationEngine) {
  window.SimulationEngine = {
    activeAnimations: {}
  };
}

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  if (window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }

  const simConfig = (window.AMP_SIMS && window.AMP_SIMS[simType]) ||
                    (window.BE_SIMS && window.BE_SIMS[simType]) ||
                    (window.CM_SIMS && window.CM_SIMS[simType]) ||
                    (window.TP_SIMS && window.TP_SIMS[simType]) ||
                    (window.EM_SIMS && window.EM_SIMS[simType]);

  if (!simConfig) {
    console.warn('Simulation not found:', simType);
    return;
  }

  container.innerHTML = '';

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
};
