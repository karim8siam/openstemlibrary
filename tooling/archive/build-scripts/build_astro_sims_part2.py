# build_astro_sims_part2.py

sim6 = """  // 6. Chandrasekhar Mass Limit & White Dwarf Degeneracy
  "astro-chandrasekhar-limit-sim": {
    title: "Chandrasekhar Mass Limit & Relativistic Electron Degeneracy",
    desc: "Polytropic equation of state transition from non-relativistic (P ∝ ρ^(5/3), R ∝ M^(-1/3)) to ultra-relativistic degeneracy (P ∝ ρ^(4/3)), revealing the asymptotic collapse limit at M_Ch = 1.44 M⊙.",
    isAnimated: true,
    controls: [
      { id: "electronFraction", label: "Electron Fraction μe", min: 1.8, max: 2.2, step: 0.05, value: 2.0 },
      { id: "wdMass", label: "White Dwarf Mass M/M⊙", min: 0.2, max: 1.43, step: 0.02, value: 0.8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const mue = vals.electronFraction !== undefined ? vals.electronFraction : 2.0;
      const M = vals.wdMass !== undefined ? vals.wdMass : 0.8;

      // Chandrasekhar limit: M_ch ~ 5.83 / mue^2
      const Mch = 5.83 / (mue * mue);

      // Mass-radius relation: R/R_earth ~ 1.0 * (M/Mch)^(-1/3) * (1 - (M/Mch)^(4/3))^(1/2)
      const massRatio = Math.min(0.999, M / Mch);
      const radFactor = Math.pow(massRatio, -1/3) * Math.sqrt(Math.max(0.001, 1 - Math.pow(massRatio, 4/3)));
      const R_earth = 1.2 * radFactor; // Earth radii
      const R_km = R_earth * 6371;
      const rho_c = 2e6 * Math.pow(M / (R_earth * R_earth * R_earth), 1.0); // g/cm^3

      // Relativistic parameter x = p_F / (m_e c) ~ (rho / 10^6)^(1/3)
      const x_rel = Math.pow(rho_c / 1e6, 1/3);

      // Left Panel: Mass-Radius Curve Graph
      const gx = 40, gy = 35, gw = 420, gh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("White Dwarf Mass-Radius Relation M(R)", gx + 15, gy + 22);

      const ox = gx + 50, oy = gy + gh - 45, pw = gw - 70, ph = gh - 75;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("White Dwarf Mass M / M⊙", ox + pw - 120, oy + 20);
      ctx.save(); ctx.translate(ox - 30, oy - 40); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Radius R / R⊕", 0, 0); ctx.restore();

      // Axis ticks
      ctx.fillText("0.0", ox - 5, oy + 14);
      ctx.fillText("0.5", ox + (0.5 / 1.6) * pw, oy + 14);
      ctx.fillText("1.0", ox + (1.0 / 1.6) * pw, oy + 14);
      ctx.fillText("1.44", ox + (1.44 / 1.6) * pw - 10, oy + 14);

      // Chandrasekhar vertical asymptote line
      const chX = ox + (Mch / 1.6) * pw;
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 3]);
      ctx.beginPath(); ctx.moveTo(chX, oy); ctx.lineTo(chX, oy - ph); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.font = "bold 10px Inter";
      ctx.fillText(`M_Ch = ${Mch.toFixed(2)} M⊙`, chX - 75, oy - ph + 15);

      // Non-relativistic curve: R ~ M^(-1/3) (grey dash)
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 1; ctx.setLineDash([2, 3]);
      ctx.beginPath();
      for (let m = 0.1; m <= 1.5; m += 0.05) {
        const r_nonrel = 1.1 * Math.pow(m, -1/3);
        const px = ox + (m / 1.6) * pw;
        const py = oy - (r_nonrel / 2.5) * ph;
        if (m === 0.1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke(); ctx.setLineDash([]);

      // Full relativistic curve plunging to zero at Mch
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let m = 0.05; m < Mch; m += 0.02) {
        const mr = m / Mch;
        const rf = Math.pow(mr, -1/3) * Math.sqrt(Math.max(0, 1 - Math.pow(mr, 4/3)));
        const r_val = 1.2 * rf;
        const px = ox + (m / 1.6) * pw;
        const py = oy - (Math.min(2.5, r_val) / 2.5) * ph;
        if (m === 0.05) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.lineTo(chX, oy);
      ctx.stroke();

      // Current Mass Point
      const curPx = ox + (M / 1.6) * pw;
      const curPy = oy - (Math.min(2.5, R_earth) / 2.5) * ph;
      ctx.fillStyle = "#f59e0b"; ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(curPx, curPy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Right Panel: Degenerate Dwarf Visualization
      const rx = 480, ry = 35, rw = 255, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Degenerate Core Physical State", rx + 15, ry + 22);

      // White dwarf sphere graphic
      const dwX = rx + rw / 2, dwY = ry + 85;
      const dwR = Math.max(12, Math.min(50, R_earth * 25));
      const grad = ctx.createRadialGradient(dwX, dwY, 2, dwX, dwY, dwR);
      grad.addColorStop(0, "#ffffff");
      grad.addColorStop(0.5, "#93c5fd");
      grad.addColorStop(1, "#3b82f6");
      ctx.fillStyle = grad; ctx.shadowColor = "#60a5fa"; ctx.shadowBlur = 15;
      ctx.beginPath(); ctx.arc(dwX, dwY, dwR, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px Inter";
      ctx.fillText(`R = ${R_km.toFixed(0)} km`, dwX - 35, dwY + dwR + 18);

      // Stats
      const stats = [
        ["Selected Mass M:", `${M.toFixed(2)} M⊙`],
        ["Radius R:", `${R_earth.toFixed(3)} R⊕`],
        ["Central Density ρc:", `${rho_c.toExponential(2)} g/cm³`],
        ["Relativistic Param x:", `${x_rel.toFixed(2)} (${x_rel > 1 ? "Relativistic" : "Non-rel"})`],
        ["Equation of State:", x_rel > 1.2 ? "P ∝ ρ^(4/3) (Gamma = 4/3)" : "P ∝ ρ^(5/3) (Gamma = 5/3)"],
        ["Chandrasekhar Mass:", `${Mch.toFixed(2)} M⊙ (for μe = ${mue})`],
        ["Stability Status:", M >= Mch ? "UNSTABLE CORE COLLAPSE" : "STABLE ELECTRON DEGENERACY"]
      ];

      ctx.font = "11px Inter";
      stats.forEach((st, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(st[0], rx + 12, ry + 165 + idx * 23);
        ctx.fillStyle = idx === 6 ? (M >= Mch ? "#ef4444" : "#10b981") : "#f1f5f9";
        ctx.font = "bold 11px Inter"; ctx.fillText(st[1], rx + 12, ry + 178 + idx * 23);
        ctx.font = "11px Inter";
      });
    }
  },
"""

sim7 = """  // =========================================================================
  // CHAPTER 4: STELLAR REMNANTS & COMPACT OBJECTS
  // =========================================================================

  // 7. Rotating Magnetized Neutron Star & Pulsar Lighthouse
  "astro-pulsar-lighthouse-sim": {
    title: "3D Pulsar Lighthouse Beam & Synchrotron Pulse Profile",
    desc: "Rapidly rotating magnetized neutron star with dipole magnetic field lines, relativistic open-field particle acceleration beam sweeping observer line of sight, and real-time pulse oscilloscope.",
    isAnimated: true,
    controls: [
      { id: "spinPeriod", label: "Rotation Period P (ms)", min: 1.5, max: 200, step: 1, value: 33 },
      { id: "magTilt", label: "Magnetic Inclination α (deg)", min: 10, max: 80, step: 2, value: 45 },
      { id: "observerTilt", label: "Observer Angle ζ (deg)", min: 10, max: 80, step: 2, value: 50 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Pms = vals.spinPeriod !== undefined ? vals.spinPeriod : 33;
      const alphaDeg = vals.magTilt !== undefined ? vals.magTilt : 45;
      const zetaDeg = vals.observerTilt !== undefined ? vals.observerTilt : 50;

      const alpha = (alphaDeg * Math.PI) / 180;
      const zeta = (zetaDeg * Math.PI) / 180;
      const omega = (2 * Math.PI * 1000) / Pms; // rad/s
      const rotAngle = time * (1000 / Pms) * 0.15; // scaled rotation for smooth viewing

      // Geometry: angle between magnetic axis and observer
      // cos(theta_obs) = cos(zeta)cos(alpha) + sin(zeta)sin(alpha)cos(phi(t))
      const cosThetaObs = Math.cos(zeta) * Math.cos(alpha) + Math.sin(zeta) * Math.sin(alpha) * Math.cos(rotAngle);
      const thetaObs = Math.acos(Math.max(-1, Math.min(1, cosThetaObs)));
      const beamHalfWidth = (15 * Math.PI) / 180;
      const inBeam = thetaObs < beamHalfWidth;
      const pulseIntensity = Math.exp(-Math.pow(thetaObs / beamHalfWidth, 2) * 3);

      // Left Panel: 3D Projected Pulsar & Magnetic Cones
      const cx = 190, cy = 190, Rns = 35;

      // Title
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Rotating Neutron Star & Lighthouse Cones", 25, 25);

      // Magnetic field lines (dipole loops)
      ctx.save();
      ctx.translate(cx, cy);
      const tiltX = Math.sin(alpha) * Math.cos(rotAngle);
      const tiltY = -Math.cos(alpha);
      const magAngle = Math.atan2(tiltX, -tiltY);

      ctx.rotate(magAngle);
      ctx.strokeStyle = "rgba(56, 189, 248, 0.25)"; ctx.lineWidth = 1;
      for (let r = 50; r <= 130; r += 25) {
        ctx.beginPath();
        ctx.ellipse(0, 0, r, r * 0.45, 0, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Emission Cones (Upper & Lower Magnetic Poles)
      const beamLen = 145;
      const coneGrad1 = ctx.createRadialGradient(0, -Rns, 2, 0, -beamLen, 45);
      coneGrad1.addColorStop(0, "rgba(244, 63, 94, 0.9)");
      coneGrad1.addColorStop(1, "rgba(244, 63, 94, 0.0)");
      ctx.fillStyle = coneGrad1;
      ctx.beginPath();
      ctx.moveTo(0, -Rns);
      ctx.lineTo(-30, -beamLen);
      ctx.lineTo(30, -beamLen);
      ctx.closePath();
      ctx.fill();

      const coneGrad2 = ctx.createRadialGradient(0, Rns, 2, 0, beamLen, 45);
      coneGrad2.addColorStop(0, "rgba(244, 63, 94, 0.9)");
      coneGrad2.addColorStop(1, "rgba(244, 63, 94, 0.0)");
      ctx.fillStyle = coneGrad2;
      ctx.beginPath();
      ctx.moveTo(0, Rns);
      ctx.lineTo(-30, beamLen);
      ctx.lineTo(30, beamLen);
      ctx.closePath();
      ctx.fill();

      // Neutron star body
      const starGrad = ctx.createRadialGradient(0, 0, 2, 0, 0, Rns);
      starGrad.addColorStop(0, "#ffffff");
      starGrad.addColorStop(0.6, "#38bdf8");
      starGrad.addColorStop(1, "#0284c7");
      ctx.fillStyle = starGrad; ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 18;
      ctx.beginPath(); ctx.arc(0, 0, Rns, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Magnetic axis line
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(0, -beamLen - 10); ctx.lineTo(0, beamLen + 10); ctx.stroke();

      ctx.restore();

      // Rotation Axis (vertical)
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 2]);
      ctx.beginPath(); ctx.moveTo(cx, cy - 160); ctx.lineTo(cx, cy + 160); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ffffff"; ctx.font = "10px Inter";
      ctx.fillText("Rotation Axis Ω", cx + 8, cy - 145);

      // Right Panel: Real-Time Pulsed Radio Oscilloscope
      const ox = 390, oy = 35, ow = 345, oh = 180;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(ox, oy, ow, oh); ctx.strokeRect(ox, oy, ow, oh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Radio Telescope Oscilloscope Trace I(t)", ox + 15, oy + 22);

      const px0 = ox + 45, py0 = oy + 145, plotW = 275, plotH = 105;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(px0, py0 - plotH); ctx.lineTo(px0, py0); ctx.lineTo(px0 + plotW, py0); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Pulse Phase (0 to 1)", px0 + plotW - 90, py0 + 16);
      ctx.fillText("Peak Intensity", px0 - 40, py0 - plotH + 12);

      // Simulated oscilloscope trace with gaussian pulse
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.beginPath();
      for (let s = 0; s < plotW; s++) {
        const ph = s / plotW; // 0 to 1
        const ang = ph * Math.PI * 2;
        const curCos = Math.cos(zeta) * Math.cos(alpha) + Math.sin(zeta) * Math.sin(alpha) * Math.cos(ang);
        const curTh = Math.acos(Math.max(-1, Math.min(1, curCos)));
        const curI = Math.exp(-Math.pow(curTh / beamHalfWidth, 2) * 3);
        const iy = py0 - curI * (plotH * 0.85);
        if (s === 0) ctx.moveTo(px0 + s, iy); else ctx.lineTo(px0 + s, iy);
      }
      ctx.stroke();

      // Current pulse indicator dot
      const curPh = (rotAngle % (Math.PI * 2)) / (Math.PI * 2);
      const dotX = px0 + curPh * plotW;
      const dotY = py0 - pulseIntensity * (plotH * 0.85);
      ctx.fillStyle = inBeam ? "#f43f5e" : "#10b981";
      ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 12;
      ctx.beginPath(); ctx.arc(dotX, dotY, inBeam ? 6 : 4, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Telescope Signal Status
      if (inBeam) {
        ctx.fillStyle = "#f43f5e"; ctx.font = "bold 12px Inter";
        ctx.fillText("⚡ FLASH DETECTED! BEAM SWEEPS OBSERVER", ox + 15, oy + 45);
      }

      // Bottom Telemetry
      const by = 230, bh = 140;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(ox, by, ow, bh); ctx.strokeRect(ox, by, ow, bh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Pulsar Electrodynamic Parameters", ox + 15, by + 22);

      // Spin-down luminosity Edot = 4 pi^2 I Pdot / P^3
      const R_light_cyl = (3e5 / (2 * Math.PI * (1000 / Pms))).toFixed(0);
      const params = [
        ["Spin Period P:", `${Pms.toFixed(1)} ms (${(1000 / Pms).toFixed(1)} rev/s)`],
        ["Light Cylinder Radius R_L = c/Ω:", `${R_light_cyl} km`],
        ["Magnetic Field B₀:", `1.2 × 10¹² Gauss`],
        ["Pulse Detection Status:", inBeam ? "IN MAIN PULSE LOBE" : "OFF-PULSE INTER-PERIOD"]
      ];

      ctx.font = "11px Inter";
      params.forEach((p, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(p[0], ox + 15, by + 48 + idx * 22);
        ctx.fillStyle = idx === 3 ? (inBeam ? "#f43f5e" : "#64748b") : "#f1f5f9";
        ctx.font = "bold 11px Inter"; ctx.fillText(p[1], ox + 195, by + 48 + idx * 22);
        ctx.font = "11px Inter";
      });
    }
  },
"""

sim8 = """  // 8. General Relativistic Black Hole Geodesics & Ray Tracing
  "astro-black-hole-geodesic-sim": {
    title: "General Relativistic Schwarzschild Geodesic Ray-Tracer",
    desc: "Numerical integration of null and timelike geodesics around a Schwarzschild black hole: Event horizon (r = 2GM/c²), Photon sphere (r = 3GM/c²), ISCO (r = 6GM/c²), and relativistic gravitational light deflection.",
    isAnimated: true,
    controls: [
      { id: "impactParam", label: "Impact Parameter b (r_g)", min: 2.0, max: 10.0, step: 0.1, value: 5.4 },
      { id: "bhMass", label: "Black Hole Mass M (M⊙)", min: 3, max: 50, step: 1, value: 10 },
      { id: "isPhoton", label: "Particle Type (1=Photon, 0=Massive)", min: 0, max: 1, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#030712"; ctx.fillRect(0, 0, w, h);

      const b = vals.impactParam !== undefined ? vals.impactParam : 5.4;
      const M = vals.bhMass !== undefined ? vals.bhMass : 10;
      const isPhoton = vals.isPhoton !== undefined ? vals.isPhoton > 0.5 : true;

      // Critical impact parameter for photon capture: b_c = 3 sqrt(3) r_g ~ 5.196 r_g
      const b_crit = 5.196;
      const isCaptured = b < b_crit;

      // Black hole center
      const cx = 220, cy = 200;
      const scale = 22; // pixels per r_g (where r_g = GM/c^2)
      const r_s = 2.0 * scale;   // Event horizon: 2 r_g
      const r_ph = 3.0 * scale;  // Photon sphere: 3 r_g
      const r_isco = 6.0 * scale;// ISCO: 6 r_g

      // Accretion disk with relativistic Doppler beaming
      ctx.save();
      const diskGrad = ctx.createRadialGradient(cx, cy, r_isco, cx, cy, r_isco * 1.8);
      diskGrad.addColorStop(0, "rgba(245, 158, 11, 0.4)");
      diskGrad.addColorStop(0.5, "rgba(234, 88, 12, 0.2)");
      diskGrad.addColorStop(1, "rgba(234, 88, 12, 0.0)");
      ctx.fillStyle = diskGrad;
      ctx.beginPath(); ctx.arc(cx, cy, r_isco * 1.8, 0, Math.PI * 2); ctx.fill();
      ctx.restore();

      // ISCO Circle
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.arc(cx, cy, r_isco, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("ISCO (6 r_g)", cx + r_isco + 5, cy);

      // Photon Sphere Circle
      ctx.strokeStyle = "#eab308"; ctx.lineWidth = 1.2; ctx.setLineDash([2, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, r_ph, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#fde047";
      ctx.fillText("Photon Sphere (3 r_g)", cx + r_ph + 5, cy - 14);

      // Event Horizon (Shadow)
      ctx.fillStyle = "#000000"; ctx.strokeStyle = "#dc2626"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(cx, cy, r_s, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
      ctx.fillStyle = "#f87171"; ctx.font = "bold 11px Inter";
      ctx.fillText("Event Horizon (2 r_g)", cx - 45, cy + 4);

      // Title
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Schwarzschild Spacetime Ray-Tracer", 25, 25);

      // Integrate null geodesic (relativistic ray tracing)
      // d^2 u / d phi^2 + u = 3/2 r_s u^2 where u = 1/r
      const startX = -180;
      const startY = -b * scale;

      ctx.strokeStyle = isCaptured ? "#ef4444" : "#38bdf8";
      ctx.lineWidth = 2.5; ctx.beginPath();

      // Numerical ray path
      let rx = -200, ry = -b * scale;
      let vx = 3.0, vy = 0.0;
      ctx.moveTo(cx + rx, cy + ry);

      let stepCount = 0;
      let terminated = false;
      while (stepCount < 300 && !terminated) {
        stepCount++;
        const r_dist = Math.hypot(rx, ry);
        const r_rg = r_dist / scale;

        if (r_rg <= 2.05) {
          // Plunged into event horizon
          terminated = true;
          break;
        }

        // Relativistic acceleration: -grad(Phi_eff)
        // a = -GM/r^2 - 3GM L^2 / (c^2 r^4)
        const a_mag = (scale * scale * 25) / (r_dist * r_dist) * (1 + (3 * b * b * scale * scale) / (r_dist * r_dist));
        const ax = -a_mag * (rx / r_dist);
        const ay = -a_mag * (ry / r_dist);

        vx += ax * 0.08;
        vy += ay * 0.08;

        // Normalize photon speed to constant c
        if (isPhoton) {
          const spd = Math.hypot(vx, vy);
          vx = (vx / spd) * 3.2;
          vy = (vy / spd) * 3.2;
        }

        rx += vx;
        ry += vy;
        ctx.lineTo(cx + rx, cy + ry);

        if (rx > 220 || Math.abs(ry) > 220) {
          terminated = true;
        }
      }
      ctx.stroke();

      // Right Panel: Telemetry & Relativistic Optics
      const rx_p = 460, ry_p = 35, rw_p = 275, rh_p = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx_p, ry_p, rw_p, rh_p); ctx.strokeRect(rx_p, ry_p, rw_p, rh_p);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Relativistic Geodesic Telemetry", rx_p + 15, ry_p + 22);

      const r_g_km = (1.477 * M).toFixed(1);
      const r_s_km = (2.954 * M).toFixed(1);

      const items = [
        ["Black Hole Mass M:", `${M} M⊙`],
        ["Gravitational Radius r_g:", `${r_g_km} km`],
        ["Schwarzschild Radius r_s:", `${r_s_km} km`],
        ["Photon Sphere Radius r_ph:", `${(3 * 1.477 * M).toFixed(1)} km`],
        ["Selected Impact Param b:", `${b.toFixed(2)} r_g`],
        ["Critical Capture Param b_c:", `5.20 r_g (3√3 r_g)`],
        ["Geodesic Trajectory:", isCaptured ? "CAPTURED INTO HORIZON" : "DEFLECTED TO INFINITY"]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx_p + 12, ry_p + 55 + idx * 28);
        ctx.fillStyle = idx === 6 ? (isCaptured ? "#ef4444" : "#38bdf8") : (idx === 4 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx_p + 12, ry_p + 70 + idx * 28);
        ctx.font = "11px Inter";
      });

      // Deflection formula
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Weak Deflection: Δφ ≈ 4GM / (c² b)", rx_p + 12, ry_p + 285);
      ctx.fillText("Strong Deflection: Diverges as b ➔ b_c", rx_p + 12, ry_p + 305);
    }
  },
"""

sim9 = """  // =========================================================================
  // CHAPTER 5: GALACTIC DYNAMICS & DARK MATTER
  // =========================================================================

  // 9. Galactic Rotation Curve & Dark Matter Halo Decomposer
  "astro-galaxy-rotation-sim": {
    title: "Galactic Rotation Curve & Dark Matter Halo Decomposer",
    desc: "Deconstructs the Milky Way rotation curve v(r) into Keplerian central bulge, Freeman exponential disk, and Navarro-Frenk-White (NFW) dark matter halo components, resolving the dark matter problem.",
    isAnimated: true,
    controls: [
      { id: "darkMatterFraction", label: "Dark Matter Halo Density", min: 0.0, max: 2.0, step: 0.1, value: 1.0 },
      { id: "diskMass", label: "Disk Mass (x10¹⁰ M⊙)", min: 2.0, max: 8.0, step: 0.5, value: 5.0 },
      { id: "bulgeMass", label: "Bulge Mass (x10¹⁰ M⊙)", min: 0.5, max: 3.0, step: 0.2, value: 1.2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const dmScale = vals.darkMatterFraction !== undefined ? vals.darkMatterFraction : 1.0;
      const Md = vals.diskMass !== undefined ? vals.diskMass : 5.0;
      const Mb = vals.bulgeMass !== undefined ? vals.bulgeMass : 1.2;

      // Left Panel: Rotating Spiral Galaxy with Stars
      const cx = 175, cy = 195;
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Differential Galactic Rotation & Stars", 25, 25);

      // Dark Matter Halo (faint purple glow)
      if (dmScale > 0.1) {
        const haloGrad = ctx.createRadialGradient(cx, cy, 20, cx, cy, 145);
        haloGrad.addColorStop(0, `rgba(168, 85, 247, ${0.15 * dmScale})`);
        haloGrad.addColorStop(1, "rgba(168, 85, 247, 0.0)");
        ctx.fillStyle = haloGrad;
        ctx.beginPath(); ctx.arc(cx, cy, 145, 0, Math.PI * 2); ctx.fill();
      }

      // Spiral arms
      ctx.strokeStyle = "rgba(56, 189, 248, 0.35)"; ctx.lineWidth = 2.5;
      for (let arm = 0; arm < 2; arm++) {
        ctx.beginPath();
        for (let th = 0.5; th < 4.5; th += 0.1) {
          const r = 22 * Math.exp(0.25 * th);
          const ang = th + arm * Math.PI + time * 0.2;
          const px = cx + r * Math.cos(ang);
          const py = cy + r * Math.sin(ang) * 0.5; // inclined view
          if (th === 0.5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Bulge core
      const bulgeGrad = ctx.createRadialGradient(cx, cy, 2, cx, cy, 25);
      bulgeGrad.addColorStop(0, "#ffffff");
      bulgeGrad.addColorStop(0.5, "#fde047");
      bulgeGrad.addColorStop(1, "rgba(245, 158, 11, 0.0)");
      ctx.fillStyle = bulgeGrad;
      ctx.beginPath(); ctx.arc(cx, cy, 25, 0, Math.PI * 2); ctx.fill();

      // Tracer stars orbiting at v(r)
      ctx.fillStyle = "#ffffff";
      for (let i = 1; i <= 35; i++) {
        const r_kpc = (i / 35) * 20; // 0 to 20 kpc
        // Total velocity v
        const v_b = Math.sqrt((Mb * 1e10 * 4.3e-6) / Math.max(0.8, r_kpc));
        const v_d = Math.sqrt((Md * 1e10 * 4.3e-6 * r_kpc * r_kpc) / Math.pow(r_kpc * r_kpc + 16, 1.5));
        const v_h = Math.sqrt(dmScale * 220 * 220 * (r_kpc * r_kpc) / (r_kpc * r_kpc + 25));
        const v_tot = Math.sqrt(v_b * v_b + v_d * v_d + v_h * v_h);

        const omega = v_tot / (r_kpc + 0.1);
        const curAng = i * 1.6 + time * omega * 0.05;
        const r_px = (r_kpc / 20) * 125;
        const sx = cx + r_px * Math.cos(curAng);
        const sy = cy + r_px * Math.sin(curAng) * 0.5;

        ctx.fillRect(sx, sy, 2, 2);
      }

      // Right Panel: Rotation Curve Decomposition Graph
      const gx = 360, gy = 35, gw = 375, gh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Rotation Curve v(r) Component Decomposition", gx + 15, gy + 22);

      const ox = gx + 50, oy = gy + gh - 45, pw = gw - 70, ph = gh - 75;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Galactocentric Radius r (kpc)", ox + pw - 140, oy + 20);
      ctx.save(); ctx.translate(ox - 30, oy - 40); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Circular Velocity v (km/s)", 0, 0); ctx.restore();

      // Axis labels
      ctx.fillText("0", ox - 5, oy + 14);
      ctx.fillText("10", ox + (10 / 25) * pw, oy + 14);
      ctx.fillText("20", ox + (20 / 25) * pw, oy + 14);
      ctx.fillText("25", ox + pw - 5, oy + 14);

      ctx.fillText("300", ox - 25, oy - ph + 10);
      ctx.fillText("150", ox - 25, oy - ph * 0.5);

      // Plot Bulge (orange dashed)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 2]); ctx.beginPath();
      for (let r = 0.5; r <= 25; r += 0.5) {
        const vb = Math.sqrt((Mb * 1e10 * 4.3e-6) / Math.max(0.8, r)) * 22;
        const px = ox + (r / 25) * pw;
        const py = oy - (Math.min(300, vb) / 300) * ph;
        if (r === 0.5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot Disk (sky blue dashed)
      ctx.strokeStyle = "#38bdf8"; ctx.setLineDash([3, 2]); ctx.beginPath();
      for (let r = 0.5; r <= 25; r += 0.5) {
        const vd = Math.sqrt((Md * 1e10 * 4.3e-6 * r * r) / Math.pow(r * r + 16, 1.5)) * 25;
        const px = ox + (r / 25) * pw;
        const py = oy - (Math.min(300, vd) / 300) * ph;
        if (r === 0.5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot Dark Matter Halo (purple dashed)
      if (dmScale > 0) {
        ctx.strokeStyle = "#a855f7"; ctx.setLineDash([4, 2]); ctx.beginPath();
        for (let r = 0.5; r <= 25; r += 0.5) {
          const vh = Math.sqrt(dmScale * 210 * 210 * (r * r) / (r * r + 25));
          const px = ox + (r / 25) * pw;
          const py = oy - (Math.min(300, vh) / 300) * ph;
          if (r === 0.5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Plot Total Observed Velocity v_tot (solid green)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.setLineDash([]); ctx.beginPath();
      for (let r = 0.5; r <= 25; r += 0.5) {
        const vb = Math.sqrt((Mb * 1e10 * 4.3e-6) / Math.max(0.8, r)) * 22;
        const vd = Math.sqrt((Md * 1e10 * 4.3e-6 * r * r) / Math.pow(r * r + 16, 1.5)) * 25;
        const vh = Math.sqrt(dmScale * 210 * 210 * (r * r) / (r * r + 25));
        const vtot = Math.sqrt(vb * vb + vd * vd + vh * vh);
        const px = ox + (r / 25) * pw;
        const py = oy - (Math.min(300, vtot) / 300) * ph;
        if (r === 0.5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Legend
      ctx.font = "10px Inter";
      ctx.fillStyle = "#10b981"; ctx.fillText("— Total Observed v_tot", ox + 15, gy + 45);
      ctx.fillStyle = "#a855f7"; ctx.fillText("-- Dark Matter Halo", ox + 155, gy + 45);
      ctx.fillStyle = "#38bdf8"; ctx.fillText("-- Stellar Disk", ox + 15, gy + 60);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("-- Central Bulge", ox + 155, gy + 60);

      // Diagnostic message
      ctx.fillStyle = dmScale < 0.2 ? "#ef4444" : "#f1f5f9"; ctx.font = "bold 11px Inter";
      ctx.fillText(dmScale < 0.2 ? "⚠️ Without Dark Matter: Keplerian falloff v ∝ r^(-1/2) contradicts data!" : "✓ Flat Rotation Curve preserved by Extended Dark Matter Halo", ox + 15, oy - 20);
    }
  },
"""

sim10 = """  // 10. Lin-Shu Spiral Density Waves & Resonances
  "astro-density-wave-sim": {
    title: "Lin-Shu Spiral Density Waves & Galactic Resonances",
    desc: "Rigorous simulation of the Lin-Shu density wave hypothesis: stars on quasi-elliptic epicyclic orbits pass through rotating potential troughs, maintaining grand-design spiral arms without winding catastrophe.",
    isAnimated: true,
    controls: [
      { id: "armCount", label: "Spiral Arms m", min: 2, max: 4, step: 1, value: 2 },
      { id: "patternSpeed", label: "Pattern Speed Ωp (km/s/kpc)", min: 15, max: 35, step: 1, value: 22 },
      { id: "waveAmplitude", label: "Wave Amplitude", min: 0.1, max: 0.5, step: 0.05, value: 0.25 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const m = vals.armCount !== undefined ? Math.round(vals.armCount) : 2;
      const OmegaP = vals.patternSpeed !== undefined ? vals.patternSpeed : 22;
      const amp = vals.waveAmplitude !== undefined ? vals.waveAmplitude : 0.25;

      const cx = 220, cy = 200;
      const patAngle = time * (OmegaP * 0.015);

      // Title
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Lin-Shu Spiral Density Wave Pattern", 25, 25);

      // Galactic Disc Rings & Resonances
      const R_cr = 100; // Corotation where Omega(R) = OmegaP
      const R_ilr = 55; // Inner Lindblad Resonance
      const R_olr = 145; // Outer Lindblad Resonance

      // Draw resonance circles
      ctx.strokeStyle = "rgba(244, 63, 94, 0.4)"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, R_ilr, 0, Math.PI * 2); ctx.stroke();
      ctx.strokeStyle = "rgba(16, 185, 129, 0.5)";
      ctx.beginPath(); ctx.arc(cx, cy, R_cr, 0, Math.PI * 2); ctx.stroke();
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.beginPath(); ctx.arc(cx, cy, R_olr, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#f43f5e"; ctx.font = "9px Inter"; ctx.fillText("ILR", cx + R_ilr + 3, cy);
      ctx.fillStyle = "#10b981"; ctx.fillText("CR (Corotation)", cx + R_cr + 3, cy);
      ctx.fillStyle = "#38bdf8"; ctx.fillText("OLR", cx + R_olr + 3, cy);

      // Density wave arms (potential minimum troughs)
      ctx.strokeStyle = "rgba(96, 165, 250, 0.6)"; ctx.lineWidth = 4;
      for (let a = 0; a < m; a++) {
        const armOffset = (a * 2 * Math.PI) / m;
        ctx.beginPath();
        for (let r = 25; r < 165; r += 2) {
          const theta = patAngle + armOffset + 0.04 * r;
          const px = cx + r * Math.cos(theta);
          const py = cy + r * Math.sin(theta);
          if (r === 25) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Draw star particles executing epicyclic motion
      ctx.fillStyle = "#ffffff";
      for (let i = 0; i < 90; i++) {
        const meanR = 35 + (i / 90) * 125;
        // Material angular velocity Omega(r) falls with radius:
        const matOmega = 45 / Math.sqrt(meanR / 30);
        const meanTheta = (i * 1.7) + time * matOmega * 0.02;

        // Perturbation from wave: delta r
        const wavePhase = m * (meanTheta - patAngle) - 0.04 * meanR;
        const dr = -amp * 18 * Math.cos(wavePhase);

        const r_actual = meanR + dr;
        const sx = cx + r_actual * Math.cos(meanTheta);
        const sy = cy + r_actual * Math.sin(meanTheta);

        // Color stars blue if inside compression wave (triggering star formation)
        const inCompression = Math.cos(wavePhase) > 0.6;
        ctx.fillStyle = inCompression ? "#38bdf8" : "rgba(255,255,255,0.7)";
        ctx.fillRect(sx, sy, inCompression ? 2.5 : 1.5, inCompression ? 2.5 : 1.5);
      }

      // Right Panel: Theory & Resonance Telemetry
      const rx = 450, ry = 35, rw = 285, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Lin-Shu Resonance Analysis", rx + 15, ry + 22);

      const items = [
        ["Pattern Speed Ω_p:", `${OmegaP} km/s/kpc`],
        ["Arm Mode m:", `${m}-Armed Spiral Pattern`],
        ["Inner Lindblad Resonance (ILR):", `Ω_p = Ω(r) - κ(r)/${m}`],
        ["Corotation Resonance (CR):", `Ω_p = Ω(r) (Radius ~ 8.0 kpc)`],
        ["Outer Lindblad Resonance (OLR):", `Ω_p = Ω(r) + κ(r)/${m}`],
        ["Wave Compression Status:", "ACTIVE SHOCK FRONT (OB Stars)"],
        ["Winding Paradox Solution:", "Pattern Speed ≠ Material Speed"]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx + 12, ry + 55 + idx * 28);
        ctx.fillStyle = idx === 5 ? "#38bdf8" : (idx === 6 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx + 12, ry + 70 + idx * 28);
        ctx.font = "11px Inter";
      });

      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Compression at wave crests compresses giant", rx + 12, ry + 280);
      ctx.fillText("molecular clouds, triggering bright blue OB star bursts.", rx + 12, ry + 295);
    }
  },
"""

with open("build_astro_sims.py", "a", encoding="utf-8") as f:
    f.write(sim6)
    f.write(sim7)
    f.write(sim8)
    f.write(sim9)
    f.write(sim10)

print("Sims 6-10 appended to build_astro_sims.py")
