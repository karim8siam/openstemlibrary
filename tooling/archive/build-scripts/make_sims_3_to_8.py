sims_code = """
  // =========================================================================
  // UNIT 2: SINGLE-PARTICLE MOTION IN E & B FIELDS
  // =========================================================================

  // 3. Single-Particle Cyclotron Gyration & E x B Drift
  "plasma-cyclotron-exb-sim": {
    title: "Cyclotron Gyration & E x B Guiding Center Drift",
    desc: "Real-time particle integration of ion vs electron cyclotron orbits in magnetic field B and transverse electric field E. Demonstrates mass-independent, charge-independent E x B drift.",
    isAnimated: true,
    controls: [
      { id: "bField", label: "Magnetic Field B_z (Tesla)", min: 0.2, max: 2.5, step: 0.1, value: 1.0 },
      { id: "eField", label: "Electric Field E_y (kV/m)", min: -4.0, max: 4.0, step: 0.5, value: 1.5 },
      { id: "viewMode", label: "Display (0: Both, 1: Ion, 2: Electron)", min: 0, max: 2, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const B = vals.bField !== undefined ? vals.bField : 1.0;
      const Ey_kV = vals.eField !== undefined ? vals.eField : 1.5;
      const mode = vals.viewMode !== undefined ? vals.viewMode : 0;

      // Physics values:
      // v_E = E x B / B^2 -> in x direction: v_Ex = Ey / B
      const vE_kms = (Ey_kV * 1000 / B) / 1000; // km/s
      // Normalized sim velocities & frequencies
      const vE_sim = (Ey_kV / B) * 35;
      const wce_sim = B * 12.0; // electron gyrofrequency (clockwise)
      const wci_sim = B * 2.2;  // ion gyrofrequency (counter-clockwise)
      const rLi_sim = 45 / B;    // ion Larmor radius
      const rLe_sim = 14 / B;    // electron Larmor radius

      // Background Field Symbols (B_z pointing OUT of page: dots)
      ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
      ctx.font = "14px Inter";
      for (let x = 30; x < 440; x += 45) {
        for (let y = 30; y < h; y += 45) {
          ctx.beginPath(); ctx.arc(x, y, 2.5, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Draw E-field vectors (Ey pointing DOWN if Ey > 0)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.35)";
      ctx.lineWidth = 1.5;
      for (let x = 50; x < 440; x += 75) {
        const eDir = Math.sign(Ey_kV);
        const yStart = eDir >= 0 ? 30 : h - 30;
        const yEnd = eDir >= 0 ? 80 : h - 80;
        ctx.beginPath(); ctx.moveTo(x, yStart); ctx.lineTo(x, yEnd); ctx.stroke();
        // Arrowhead
        ctx.beginPath();
        ctx.moveTo(x - 4, yEnd - eDir * 6);
        ctx.lineTo(x, yEnd);
        ctx.lineTo(x + 4, yEnd - eDir * 6);
        ctx.stroke();
      }
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 10px Inter";
      ctx.fillText(Ey_kV >= 0 ? "Electric Field E_y ↓" : "Electric Field E_y ↑", 45, Ey_kV >= 0 ? 25 : h - 15);
      ctx.fillStyle = "#10b981";
      ctx.fillText("Magnetic Field B_z ⊙ (Out of page)", 240, 25);

      // Trajectories computation
      const simW = 440;
      const t = time;
      const baseX = ((t * vE_sim) % (simW - 60)) + 30;
      const cy = h / 2 + 10;

      // 1. Ion (q > 0: counter-clockwise gyration)
      if (mode === 0 || mode === 1) {
        // Draw Ion trail
        ctx.strokeStyle = "rgba(245, 158, 11, 0.75)";
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let dt = 0; dt < 3.5; dt += 0.05) {
          const pastT = t - dt;
          const px = (((pastT * vE_sim) % (simW - 60)) + 30) + rLi_sim * Math.cos(wci_sim * pastT);
          const py = cy + rLi_sim * Math.sin(wci_sim * pastT);
          if (dt === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Ion current position
        const ionX = baseX + rLi_sim * Math.cos(wci_sim * t);
        const ionY = cy + rLi_sim * Math.sin(wci_sim * t);
        ctx.fillStyle = "#f59e0b";
        ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 10;
        ctx.beginPath(); ctx.arc(ionX, ionY, 7, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#050811"; ctx.font = "bold 9px Inter"; ctx.textAlign = "center";
        ctx.fillText("H⁺", ionX, ionY + 3);
        ctx.textAlign = "left";

        // Guiding Center dashed line
        ctx.strokeStyle = "rgba(245, 158, 11, 0.4)";
        ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(ionX, ionY); ctx.lineTo(baseX, cy); ctx.stroke();
        ctx.setLineDash([]);
      }

      // 2. Electron (q < 0: clockwise gyration)
      if (mode === 0 || mode === 2) {
        ctx.strokeStyle = "rgba(56, 189, 248, 0.75)";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        for (let dt = 0; dt < 3.5; dt += 0.02) {
          const pastT = t - dt;
          const px = (((pastT * vE_sim) % (simW - 60)) + 30) + rLe_sim * Math.cos(-wce_sim * pastT);
          const py = cy + rLe_sim * Math.sin(-wce_sim * pastT);
          if (dt === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Electron current position
        const eleX = baseX + rLe_sim * Math.cos(-wce_sim * t);
        const eleY = cy + rLe_sim * Math.sin(-wce_sim * t);
        ctx.fillStyle = "#38bdf8";
        ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 8;
        ctx.beginPath(); ctx.arc(eleX, eleY, 5, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#050811"; ctx.font = "bold 8px Inter"; ctx.textAlign = "center";
        ctx.fillText("e⁻", eleX, eleY + 3);
        ctx.textAlign = "left";
      }

      // Guiding center marker
      ctx.fillStyle = "#a855f7";
      ctx.beginPath(); ctx.arc(baseX, cy, 3.5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#c084fc"; ctx.font = "bold 9px Inter";
      ctx.fillText("R_gc (Guiding Center)", baseX - 50, cy - 8);

      // ExB Drift Velocity Vector arrow
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(baseX, cy); ctx.lineTo(baseX + 45 * Math.sign(Ey_kV), cy); ctx.stroke();
      ctx.beginPath();
      const headX = baseX + 45 * Math.sign(Ey_kV);
      ctx.moveTo(headX - 6 * Math.sign(Ey_kV), cy - 4);
      ctx.lineTo(headX, cy);
      ctx.lineTo(headX - 6 * Math.sign(Ey_kV), cy + 4);
      ctx.stroke();
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 10px Inter";
      ctx.fillText("v_E Drift →", baseX + 10, cy + 18);

      // Right Pane: Telemetry Box
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Guiding Center & Drift Telemetry", tx + 14, ty + 24);

      const items = [
        ["Magnetic Field B_z:", `${B.toFixed(2)} T`],
        ["Electric Field E_y:", `${Ey_kV.toFixed(2)} kV/m`],
        ["E x B Drift Speed v_E:", `${Math.abs(vE_kms).toFixed(2)} km/s`],
        ["Drift Direction:", Ey_kV >= 0 ? "+x (Rightwards)" : "-x (Leftwards)"],
        ["Ion Gyrofrequency f_ci:", `${(B * 15.24).toFixed(1)} MHz`],
        ["Electron Gyrofrequency f_ce:", `${(B * 28.0).toFixed(1)} GHz`],
        ["Ion Larmor Radius r_Li:", `${(3.2 / B).toFixed(2)} mm`],
        ["Electron Larmor Radius r_Le:", `${(0.075 / B).toFixed(3)} mm`],
        ["Net Conduction Current J_E:", "0.0 A/m² (No charge sep!)"],
        ["Physics Invariance:", "q-independent & m-independent"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 2 ? "#ec4899" : (idx === 8 || idx === 9 ? "#10b981" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // 4. Time-Varying E(t) Field & Polarization Drift Current
  "plasma-polarization-drift-sim": {
    title: "Time-Varying E(t) Field & Polarization Drift Current",
    desc: "Inertial polarization drift v_p = (m / qB²) (dE_perp / dt) under AC electric fields. Demonstrates massive ion displacement, electron immobility, and polarization current density j_p.",
    isAnimated: true,
    controls: [
      { id: "dEdt", label: "Rate dE/dt (MV/m·s)", min: 1, max: 10, step: 1, value: 5 },
      { id: "modFreq", label: "Modulation Freq ω_E (kHz)", min: 5, max: 40, step: 5, value: 15 },
      { id: "ionMass", label: "Ion Species (1: H⁺, 2: D⁺, 4: He⁺)", min: 1, max: 4, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const dEdt = vals.dEdt !== undefined ? vals.dEdt : 5;
      const f_kHz = vals.modFreq !== undefined ? vals.modFreq : 15;
      const A_ion = vals.ionMass !== undefined ? vals.ionMass : 1;

      // E(t) = E0 * sin(omega * t)
      const omega = f_kHz * 0.2;
      const Et = Math.sin(omega * time);
      const dEt = Math.cos(omega * time) * omega * (dEdt / 5);

      // Polarization drift is proportional to m / (q B^2) * dE/dt
      const vp_ion_px = dEt * 18 * A_ion;
      const vp_ele_px = -dEt * (18 / 1836); // tiny!

      // Left visualization area: Ion vs Electron displacement
      const vx = 30, vy = 30, vw = 400, vh = 330;
      ctx.fillStyle = "rgba(15, 23, 42, 0.6)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(vx, vy, vw, vh); ctx.strokeRect(vx, vy, vw, vh);

      // Axes for displacement
      ctx.strokeStyle = "#334155"; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(vx + 20, vy + vh / 2); ctx.lineTo(vx + vw - 20, vy + vh / 2); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("AC Electric Field E_y(t) & Inertial Lag", vx + 15, vy + 22);

      // Draw E-field indicator bar on left
      const barH = Et * 55;
      ctx.fillStyle = Et >= 0 ? "#38bdf8" : "#ec4899";
      ctx.fillRect(vx + 25, vy + vh / 2, 10, -barH);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("E(t)", vx + 22, vy + vh / 2 + 18);

      // Ion Gyro-Center and Orbit Displacement
      const ionCenterX = vx + 150;
      const ionCenterY = vy + vh / 2 - vp_ion_px;
      const gyroPhase = time * 8;
      const rLi = 32;

      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(ionCenterX, ionCenterY, rLi, 0, Math.PI * 2);
      ctx.stroke();

      const ionX = ionCenterX + rLi * Math.cos(gyroPhase);
      const ionY = ionCenterY + rLi * Math.sin(gyroPhase);
      ctx.fillStyle = "#f59e0b";
      ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 8;
      ctx.beginPath(); ctx.arc(ionX, ionY, 7, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;
      ctx.fillStyle = "#050811"; ctx.font = "bold 8px Inter"; ctx.textAlign = "center";
      ctx.fillText(`+q (A=${A_ion})`, ionX, ionY + 3);
      ctx.textAlign = "left";

      // Polarization drift arrow for Ion
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(ionCenterX, vy + vh / 2);
      ctx.lineTo(ionCenterX, ionCenterY);
      ctx.stroke();
      ctx.fillStyle = "#ef4444"; ctx.font = "bold 10px Inter";
      ctx.fillText(`v_p,ion (${(vp_ion_px).toFixed(1)} px)`, ionCenterX + 12, vy + vh / 2 - vp_ion_px / 2);

      // Electron Gyro-Center (negligible displacement)
      const eleCenterX = vx + 300;
      const eleCenterY = vy + vh / 2 - vp_ele_px;
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.arc(eleCenterX, eleCenterY, 12, 0, Math.PI * 2);
      ctx.stroke();

      const eleX = eleCenterX + 12 * Math.cos(-gyroPhase * 15);
      const eleY = eleCenterY + 12 * Math.sin(-gyroPhase * 15);
      ctx.fillStyle = "#38bdf8";
      ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 6;
      ctx.beginPath(); ctx.arc(eleX, eleY, 4, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Electron (m_e << m_i)", eleCenterX - 35, vy + vh / 2 + 30);
      ctx.fillText("v_p,e ≈ 0 (No inertial lag)", eleCenterX - 45, vy + vh / 2 + 45);

      // Net Polarization Current J_p representation
      const jDir = Math.sign(vp_ion_px);
      ctx.fillStyle = "rgba(16, 185, 129, 0.25)";
      ctx.fillRect(vx + 15, vy + vh - 45, vw - 30, 30);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
      ctx.strokeRect(vx + 15, vy + vh - 45, vw - 30, 30);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Net Current j_p = (ρ_m / B²)·(dE/dt) ${jDir >= 0 ? "↑ Upward" : "↓ Downward"}`, vx + 35, vy + vh - 26);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Polarization Drift & Current", tx + 14, ty + 24);

      const items = [
        ["Rate of Field Change dE/dt:", `${(dEt * 10).toFixed(2)} MV/(m·s)`],
        ["Modulation Freq f_mod:", `${f_kHz} kHz`],
        ["Ion Mass Ratio (m_i / m_e):", `${(A_ion * 1836).toFixed(0)} : 1`],
        ["Ion Polarization Drift v_p,i:", `${Math.abs(dEt * A_ion * 12.4).toFixed(2)} m/s`],
        ["Electron Polarization Drift v_p,e:", `${Math.abs(dEt * 12.4 / 1836).toFixed(4)} m/s`],
        ["Polarization Drift Ratio:", `${(A_ion * 1836).toFixed(0)} (Ions carry 99.95%)`],
        ["Plasma Dielectric Const ε_r:", `1 + c²/v_A² ≈ ${(1.4e3 * A_ion).toFixed(0)}`],
        ["Physical Origin:", "Finite Ion Larmor Inertia Lag"],
        ["Low-Frequency MHD Role:", "Provides Effective Mass Density"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 30;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 3 ? "#ef4444" : (idx === 5 ? "#10b981" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 160, iy);
      });
    }
  },

  // =========================================================================
  // UNIT 3: DRIFTS IN NON-UNIFORM FIELDS & MAGNETIC MIRRORS
  // =========================================================================

  // 5. Non-Uniform Magnetic Fields: Grad-B & Curvature Drifts
  "plasma-gradient-curvature-drift-sim": {
    title: "Non-Uniform Magnetic Fields: ∇B & Curvature Drifts",
    desc: "Particle trajectories in toroidal/gradient magnetic geometries. Tight Larmor radius at high B and wide at weak B induces grad-B drift, combined with centrifugal curvature drift, driving vertical charge separation.",
    isAnimated: true,
    controls: [
      { id: "gradB", label: "Field Gradient ∇B/B (m⁻¹)", min: 0.5, max: 4.0, step: 0.5, value: 2.0 },
      { id: "curvR", label: "Radius of Curvature R_c (m)", min: 0.8, max: 3.5, step: 0.3, value: 1.5 },
      { id: "chargeSign", label: "Particle (0: Both, 1: Ion, 2: Electron)", min: 0, max: 2, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const gradB = vals.gradB !== undefined ? vals.gradB : 2.0;
      const Rc = vals.curvR !== undefined ? vals.curvR : 1.5;
      const pMode = vals.chargeSign !== undefined ? vals.chargeSign : 0;

      // Left visualization area: curved field lines
      const cx = 40, cy = 195, R0 = 160;
      // Draw curved field lines (concentric circles centered at left)
      ctx.strokeStyle = "rgba(16, 185, 129, 0.4)"; ctx.lineWidth = 1.5;
      for (let r = 80; r <= 320; r += 30) {
        ctx.beginPath();
        ctx.arc(cx - 30, cy, r, -Math.PI / 3, Math.PI / 3);
        ctx.stroke();
      }

      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText("Curved Magnetic Field B Lines (∇B points ← Inward)", 40, 25);

      // Strong field label (inner) vs Weak field (outer)
      ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter";
      ctx.fillText("Strong B (Small r_L)", 60, 50);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("Weak B (Large r_L)", 220, 50);

      // Trajectory of Ion (drifts UPwards)
      if (pMode === 0 || pMode === 1) {
        ctx.strokeStyle = "rgba(245, 158, 11, 0.8)"; ctx.lineWidth = 2;
        ctx.beginPath();
        const driftUp = (time * 25 * gradB) % 240;
        const startY = cy + 100 - driftUp;
        for (let a = 0; a < 6 * Math.PI; a += 0.1) {
          // Radius varies with position: rL ~ rL0 * (1 + 0.15 * cos(a))
          const localR = 30 * (1 + 0.25 * Math.cos(a));
          const px = 180 + localR * Math.cos(a);
          const py = startY - a * (4 * gradB) + localR * Math.sin(a);
          if (a === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Ion head
        ctx.fillStyle = "#f59e0b";
        ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 8;
        ctx.beginPath(); ctx.arc(180, startY - 30, 6, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#f59e0b"; ctx.font = "bold 10px Inter";
        ctx.fillText("Ion H⁺ (Drifts ↑ UP)", 195, startY - 30);
      }

      // Trajectory of Electron (drifts DOWNwards)
      if (pMode === 0 || pMode === 2) {
        ctx.strokeStyle = "rgba(56, 189, 248, 0.8)"; ctx.lineWidth = 1.5;
        ctx.beginPath();
        const driftDown = (time * 25 * gradB) % 240;
        const startYe = cy - 100 + driftDown;
        for (let a = 0; a < 6 * Math.PI; a += 0.1) {
          const localRe = 12 * (1 + 0.2 * Math.cos(a));
          const px = 280 + localRe * Math.cos(-a * 3);
          const py = startYe + a * (2 * gradB) + localRe * Math.sin(-a * 3);
          if (a === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        ctx.fillStyle = "#38bdf8";
        ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 8;
        ctx.beginPath(); ctx.arc(280, startYe + 20, 4.5, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 10px Inter";
        ctx.fillText("Electron e⁻ (Drifts ↓ DOWN)", 295, startYe + 22);
      }

      // Vertical Charge Separation Electric Field E_vert
      ctx.fillStyle = "rgba(236, 72, 153, 0.25)";
      ctx.fillRect(360, 60, 45, 270);
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 1.5;
      ctx.strokeRect(360, 60, 45, 270);
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 9px Inter";
      ctx.fillText("+ Charges (Top)", 340, 52);
      ctx.fillText("- Charges (Bot)", 340, 345);
      ctx.fillText("E_pol ↓", 370, 195);

      // Outward E x B drift arrow
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(380, 195); ctx.lineTo(430, 195); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(422, 191); ctx.lineTo(430, 195); ctx.lineTo(422, 199); ctx.stroke();
      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 9px Inter";
      ctx.fillText("v_E Outward Expulsion →", 325, 215);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("∇B & Curvature Drift Telemetry", tx + 14, ty + 24);

      const vGradB = (gradB * 4.2).toFixed(2);
      const vCurv = ((1.0 / Rc) * 6.5).toFixed(2);
      const vTotal = (parseFloat(vGradB) + parseFloat(vCurv)).toFixed(2);

      const items = [
        ["Field Gradient ∇B/B:", `${gradB.toFixed(1)} m⁻¹`],
        ["Curvature Radius R_c:", `${Rc.toFixed(1)} m`],
        ["Grad-B Drift Speed v_∇B:", `${vGradB} km/s`],
        ["Curvature Drift Speed v_c:", `${vCurv} km/s`],
        ["Total Guiding Drift v_d:", `${vTotal} km/s`],
        ["Ion Drift Direction:", "↑ Upwards (+y)"],
        ["Electron Drift Direction:", "↓ Downwards (-y)"],
        ["Charge Separation Result:", "Generates Vertical E Field"],
        ["Consequence in Simple Torus:", "Radial Expulsion v_E × B"],
        ["Tokamak Resolution:", "Helical Twist q (Safety Factor)"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 4 ? "#ec4899" : (idx === 8 ? "#ef4444" : (idx === 9 ? "#10b981" : "#f1f5f9"));
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 155, iy);
      });
    }
  },

  // 6. Magnetic Mirror, First Adiabatic Invariant & Loss Cone
  "plasma-magnetic-mirror-sim": {
    title: "Magnetic Mirror, First Adiabatic Invariant & Loss Cone",
    desc: "Particle confinement in converging magnetic bottle. Demonstrates conservation of magnetic moment μ = m v_perp² / (2B), pitch angle reflection at turning points, and loss cone escape dynamics.",
    isAnimated: true,
    controls: [
      { id: "mirrorRatio", label: "Mirror Ratio R_m = B_max/B₀", min: 1.5, max: 5.0, step: 0.5, value: 3.0 },
      { id: "pitchAngle", label: "Initial Pitch Angle θ₀ (deg)", min: 15, max: 75, step: 5, value: 45 },
      { id: "bMid", label: "Midplane Field B₀ (T)", min: 0.5, max: 2.5, step: 0.5, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Rm = vals.mirrorRatio !== undefined ? vals.mirrorRatio : 3.0;
      const thetaDeg = vals.pitchAngle !== undefined ? vals.pitchAngle : 45;
      const B0 = vals.bMid !== undefined ? vals.bMid : 1.0;

      const thetaRad = (thetaDeg * Math.PI) / 180;
      const sinTheta = Math.sin(thetaRad);
      // Loss cone angle: sin(theta_c) = 1 / sqrt(Rm)
      const sinThetaC = 1 / Math.sqrt(Rm);
      const thetaCDeg = (Math.asin(sinThetaC) * 180) / Math.PI;

      const isTrapped = thetaDeg >= thetaCDeg;
      const Bmax = B0 * Rm;
      // Turning field: B_turn = B0 / sin^2(theta)
      const Bturn = B0 / (sinTheta * sinTheta);

      // Left visualization area: Magnetic Bottle (x: 20 to 420, y: 25 to 365)
      const mx = 25, my = 25, mw = 400, mh = 340;
      const midX = mx + mw / 2, midY = my + mh / 2;

      // Draw Mirror Coils at ends
      ctx.fillStyle = "#475569";
      // Left coils
      ctx.fillRect(mx + 20, my + 30, 16, 70);
      ctx.fillRect(mx + 20, my + mh - 100, 16, 70);
      // Right coils
      ctx.fillRect(mx + mw - 36, my + 30, 16, 70);
      ctx.fillRect(mx + mw - 36, my + mh - 100, 16, 70);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 10px Inter";
      ctx.fillText("Throat B_max", mx + 5, my + 22);
      ctx.fillText("Throat B_max", mx + mw - 75, my + 22);
      ctx.fillText("Midplane B₀", midX - 30, my + 22);

      // Draw Hourglass / Converging Magnetic Field Lines
      ctx.strokeStyle = "rgba(16, 185, 129, 0.4)"; ctx.lineWidth = 1.5;
      [-70, -35, 0, 35, 70].forEach(offset => {
        ctx.beginPath();
        ctx.moveTo(mx + 20, midY + offset * 0.4);
        ctx.bezierCurveTo(midX - 70, midY + offset * 1.3, midX + 70, midY + offset * 1.3, mx + mw - 20, midY + offset * 0.4);
        ctx.stroke();
      });

      // Bouncing or Escaping particle trajectory
      let zNorm = 0; // -1 to +1
      let zTurnNorm = Math.min(0.9, Math.sqrt(Math.max(0, 1 - 1 / (sinTheta * sinTheta * Rm))));
      if (isTrapped) {
        // Trapped particle oscillates
        const freq = 1.8;
        zNorm = Math.sin(time * freq) * zTurnNorm * 0.85;
      } else {
        // Escaping particle flies out
        zNorm = ((time * 0.8) % 2.5) - 1.2;
      }

      const pX = midX + zNorm * 160;
      const localR = 30 * (1 - 0.5 * Math.abs(zNorm));
      const gyroPhase = time * 12;
      const pY = midY + localR * Math.sin(gyroPhase);

      // Trajectory spiral trail
      ctx.strokeStyle = isTrapped ? "rgba(251, 191, 36, 0.7)" : "rgba(239, 68, 68, 0.7)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let s = -0.8; s <= 0.8; s += 0.05) {
        if (isTrapped && Math.abs(s) > zTurnNorm * 0.85) continue;
        const txNorm = s;
        const tX = midX + txNorm * 160;
        const tR = 30 * (1 - 0.5 * Math.abs(txNorm));
        const tY = midY + tR * Math.sin(gyroPhase + s * 10);
        if (s === -0.8) ctx.moveTo(tX, tY); else ctx.lineTo(tX, tY);
      }
      ctx.stroke();

      // Particle marker
      ctx.fillStyle = isTrapped ? "#f59e0b" : "#ef4444";
      ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 12;
      ctx.beginPath(); ctx.arc(pX, pY, 7, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 9px Inter"; ctx.textAlign = "center";
      ctx.fillText("q", pX, pY + 3);
      ctx.textAlign = "left";

      // Turning point markers if trapped
      if (isTrapped) {
        const turnX1 = midX - zTurnNorm * 0.85 * 160;
        const turnX2 = midX + zTurnNorm * 0.85 * 160;
        ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(turnX1, midY - 60); ctx.lineTo(turnX1, midY + 60); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(turnX2, midY - 60); ctx.lineTo(turnX2, midY + 60); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#fbbf24"; ctx.font = "9px Inter";
        ctx.fillText("Turning Point", turnX1 - 30, midY - 65);
        ctx.fillText("Turning Point", turnX2 - 30, midY - 65);
      }

      // Confinement Status Banner
      ctx.fillStyle = isTrapped ? "rgba(16, 185, 129, 0.2)" : "rgba(239, 68, 68, 0.2)";
      ctx.fillRect(mx + 20, my + mh - 40, mw - 40, 28);
      ctx.strokeStyle = isTrapped ? "#10b981" : "#ef4444"; ctx.lineWidth = 1;
      ctx.strokeRect(mx + 20, my + mh - 40, mw - 40, 28);
      ctx.fillStyle = isTrapped ? "#10b981" : "#ef4444"; ctx.font = "bold 11px Inter";
      ctx.fillText(isTrapped ? `✓ CONFINED: θ₀ (${thetaDeg}°) ≥ θ_c (${thetaCDeg.toFixed(1)}°) — Adiabatically Trapped` : `✗ LOSS CONE ESCAPE: θ₀ (${thetaDeg}°) < θ_c (${thetaCDeg.toFixed(1)}°) — Unconfined!`, mx + 30, my + mh - 22);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Magnetic Mirror Telemetry", tx + 14, ty + 24);

      const items = [
        ["Midplane Field B₀:", `${B0.toFixed(2)} T`],
        ["Mirror Ratio R_m:", `${Rm.toFixed(2)}`],
        ["Throat Max Field B_max:", `${Bmax.toFixed(2)} T`],
        ["Particle Pitch Angle θ₀:", `${thetaDeg}°`],
        ["Loss Cone Angle θ_c:", `${thetaCDeg.toFixed(2)}°`],
        ["First Invariant μ = mv_⊥²/2B:", "CONSERVED (μ = const)"],
        ["Reflection Field B_turn:", `${Bturn <= Bmax ? Bturn.toFixed(2) + " T" : "Exceeds B_max"}`],
        ["Parallel Force -μ(∂B/∂z):", isTrapped ? "Restoring to Midplane" : "Insufficient"],
        ["Confinement State:", isTrapped ? "TRAPPED (Periodic Bounce)" : "ESCAPING VIA THROAT"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 30;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 8 ? (isTrapped ? "#10b981" : "#ef4444") : (idx === 4 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 155, iy);
      });
    }
  },

  // =========================================================================
  // UNIT 4: PLASMA FLUID THEORY & IDEAL MHD
  // =========================================================================

  // 7. Plasma Pressure Gradient & Diamagnetic Drift
  "plasma-diamagnetic-drift-sim": {
    title: "Plasma Fluid Pressure Gradient & Diamagnetic Drift",
    desc: "Macroscopic fluid diamagnetic drift v_D = -(∇P x B)/(qnB²) emerging from particle gyration in a density gradient, producing diamagnetic current j_D and internal B-field reduction.",
    isAnimated: true,
    controls: [
      { id: "gradScale", label: "Gradient Scale L_n (cm)", min: 2, max: 15, step: 1, value: 6 },
      { id: "tempEv", label: "Plasma Temp T (eV)", min: 5, max: 40, step: 5, value: 20 },
      { id: "bField", label: "Field B_z (Tesla)", min: 0.5, max: 2.5, step: 0.5, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Ln_cm = vals.gradScale !== undefined ? vals.gradScale : 6;
      const Te = vals.tempEv !== undefined ? vals.tempEv : 20;
      const B = vals.bField !== undefined ? vals.bField : 1.5;

      // Diamagnetic velocity: v_D = kB T / (q B Ln)
      // vD in km/s: (1.602e-19 * Te) / (1.602e-19 * B * (Ln_cm * 0.01)) = Te / (B * Ln_cm * 0.01) * 1e-3
      const vD_kms = Te / (B * (Ln_cm * 0.01) * 1000);
      const beta = (2 * 4e-7 * Math.PI * 1e19 * 1.602e-19 * Te) / (B * B); // plasma beta

      // Left visualization: Ensemble of gyrating particles in density gradient
      const px0 = 30, py0 = 30, pw = 400, ph = 330;
      ctx.fillStyle = "rgba(15, 23, 42, 0.6)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(px0, py0, pw, ph); ctx.strokeRect(px0, py0, pw, ph);

      // Gradient background shading: High density at top, Low density at bottom
      const nGrad = ctx.createLinearGradient(0, py0, 0, py0 + ph);
      nGrad.addColorStop(0, "rgba(56, 189, 248, 0.25)");
      nGrad.addColorStop(1, "rgba(15, 23, 42, 0.05)");
      ctx.fillStyle = nGrad;
      ctx.fillRect(px0, py0, pw, ph);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Density Gradient ∇n (High Density Top ➔ Low Density Bot)", px0 + 15, py0 + 20);

      // Dividing reference line across middle
      const midY = py0 + ph / 2;
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(px0 + 20, midY); ctx.lineTo(px0 + pw - 20, midY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#fbbf24"; ctx.font = "10px Inter";
      ctx.fillText("Observation Line: Macroscopic Flux Interface", px0 + 25, midY - 6);

      // Draw gyrating particles (more at top, fewer at bottom)
      const rL = 26 / B;
      const numRings = 16;
      for (let i = 0; i < numRings; i++) {
        const row = Math.floor(i / 4);
        const col = i % 4;
        const cy = py0 + 60 + row * 65;
        const cx = px0 + 55 + col * 95;
        // Density factor determines opacity
        const opacity = Math.max(0.2, 1.0 - (row / 4) * 0.7);

        ctx.strokeStyle = `rgba(245, 158, 11, ${opacity})`;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(cx, cy, rL, 0, Math.PI * 2);
        ctx.stroke();

        // Ion dot
        const gAng = time * 4 + i;
        const ix = cx + rL * Math.cos(gAng);
        const iy = cy + rL * Math.sin(gAng);
        ctx.fillStyle = `rgba(245, 158, 11, ${opacity})`;
        ctx.beginPath(); ctx.arc(ix, iy, 4, 0, Math.PI * 2); ctx.fill();

        // Direction arrow at crossing of line
        if (row === 1) {
          // Crosses line going LEFT (counter-clockwise top half vs bottom half)
          ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.2;
          ctx.beginPath(); ctx.moveTo(cx + 8, cy + rL); ctx.lineTo(cx - 8, cy + rL); ctx.stroke();
        }
      }

      // Net Macroscopic Diamagnetic Drift Arrow
      ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
      ctx.fillRect(px0 + 20, py0 + ph - 45, pw - 40, 32);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
      ctx.strokeRect(px0 + 20, py0 + ph - 45, pw - 40, 32);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Net Fluid Diamagnetic Drift v_D: ← Leftwards (${vD_kms.toFixed(1)} km/s)`, px0 + 35, py0 + ph - 25);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Diamagnetic Fluid Telemetry", tx + 14, ty + 24);

      const items = [
        ["Gradient Scale Length L_n:", `${Ln_cm.toFixed(1)} cm`],
        ["Plasma Temperature T_e:", `${Te.toFixed(0)} eV`],
        ["Magnetic Field B_z:", `${B.toFixed(2)} T`],
        ["Ion Diamagnetic Drift v_Di:", `${vD_kms.toFixed(2)} km/s (←)`],
        ["Electron Diamagnetic Drift v_De:", `${vD_kms.toFixed(2)} km/s (→)`],
        ["Diamagnetic Current j_D:", `${(vD_kms * 1.6).toFixed(2)} kA/m²`],
        ["Guiding Center Motion:", "ZERO (Guiding centers are stationary!)"],
        ["Internal Field Reduction ΔB:", `-${(beta * 0.5 * 100).toFixed(2)}% (Diamagnetic)`],
        ["Plasma Beta β = 2μ₀P/B²:", `${(beta * 100).toFixed(3)}%`],
        ["Physics Insight:", "Pure Macroscopic Fluid Pressure Effect"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 48 + idx * 28;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 3 || idx === 4 ? "#fbbf24" : (idx === 6 ? "#ec4899" : (idx === 7 ? "#10b981" : "#f1f5f9"));
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 155, iy);
      });
    }
  },

  // 8. Ideal MHD Magnetic Flux Freezing & Reconnection
  "plasma-flux-freezing-mhd-sim": {
    title: "Ideal MHD Magnetic Flux Freezing & Reconnection",
    desc: "Alfvén's frozen-in flux theorem (Rm >> 1) where magnetic field lines move with conducting fluid parcels, contrasted with resistive Sweet-Parker reconnection (Rm finite) at X-points.",
    isAnimated: true,
    controls: [
      { id: "resistivity", label: "Plasma Resistivity η (0: Ideal)", min: 0, max: 8, step: 1, value: 0 },
      { id: "fluidSpeed", label: "Fluid Flow Speed v₀ (km/s)", min: 10, max: 80, step: 10, value: 40 },
      { id: "mode", label: "Mode (0: Flux Freezing, 1: X-Point Reconnect)", min: 0, max: 1, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const eta = vals.resistivity !== undefined ? vals.resistivity : 0;
      const v0 = vals.fluidSpeed !== undefined ? vals.fluidSpeed : 40;
      const mode = vals.mode !== undefined ? vals.mode : 0;

      const isIdeal = eta === 0 && mode === 0;
      const Rm = eta === 0 ? 99999 : Math.max(1, Math.round(5000 / (eta + 0.1)));

      // Left visualization area: Fluid mesh & Magnetic Field lines
      const px0 = 30, py0 = 30, pw = 400, ph = 330;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(px0, py0, pw, ph); ctx.strokeRect(px0, py0, pw, ph);

      if (mode === 0) {
        // Mode 0: Alfvén Flux Freezing
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
        ctx.fillText("Alfvén Frozen-In Flux: Fluid Parcel Glued to B-Lines", px0 + 15, py0 + 20);

        // Fluid displacement vortex
        const vortexY = py0 + ph / 2 + Math.sin(time * 2) * (v0 * 0.7);

        // Deforming fluid parcel (cyan elastic quadrilateral)
        ctx.fillStyle = "rgba(56, 189, 248, 0.2)";
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
        const pLeft = px0 + 120, pRight = px0 + 260;
        ctx.beginPath();
        ctx.moveTo(pLeft, vortexY - 45);
        ctx.lineTo(pRight, vortexY - 30);
        ctx.lineTo(pRight, vortexY + 30);
        ctx.lineTo(pLeft, vortexY + 45);
        ctx.closePath();
        ctx.fill(); ctx.stroke();
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 10px Inter";
        ctx.fillText("Conducting Fluid Element", pLeft + 10, vortexY + 4);

        // Magnetic Field Lines traversing fluid
        [-60, -30, 0, 30, 60].forEach((offset, idx) => {
          ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.moveTo(px0 + 20, py0 + ph / 2 + offset);
          if (isIdeal) {
            // Perfectly glued to fluid parcel
            ctx.bezierCurveTo(
              pLeft, vortexY + offset * 0.7,
              pRight, vortexY + offset * 0.7,
              px0 + pw - 20, py0 + ph / 2 + offset
            );
          } else {
            // Slips through fluid due to resistive diffusion
            const slipFactor = Math.max(0.1, 1 - eta * 0.12);
            ctx.bezierCurveTo(
              pLeft, py0 + ph / 2 + offset + (vortexY - (py0 + ph / 2)) * slipFactor,
              pRight, py0 + ph / 2 + offset + (vortexY - (py0 + ph / 2)) * slipFactor,
              px0 + pw - 20, py0 + ph / 2 + offset
            );
          }
          ctx.stroke();

          // Field line direction arrow
          ctx.fillStyle = "#10b981";
          ctx.beginPath();
          ctx.moveTo(px0 + pw - 30, py0 + ph / 2 + offset - 4);
          ctx.lineTo(px0 + pw - 22, py0 + ph / 2 + offset);
          ctx.lineTo(px0 + pw - 30, py0 + ph / 2 + offset + 4);
          ctx.fill();
        });

      } else {
        // Mode 1: Magnetic Reconnection at X-Point
        ctx.fillStyle = "#ec4899"; ctx.font = "bold 12px Inter";
        ctx.fillText("Resistive Sweet-Parker Magnetic Reconnection (X-Point)", px0 + 15, py0 + 20);

        const xCenter = px0 + pw / 2, yCenter = py0 + ph / 2;
        const rePhase = (time * 1.5) % Math.PI;

        // Inflow arrows (vertical)
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(xCenter, yCenter - 90); ctx.lineTo(xCenter, yCenter - 35); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(xCenter, yCenter + 90); ctx.lineTo(xCenter, yCenter + 35); ctx.stroke();
        ctx.fillStyle = "#38bdf8"; ctx.font = "10px Inter";
        ctx.fillText("Plasma Inflow v_in ↓", xCenter + 8, yCenter - 55);
        ctx.fillText("Plasma Inflow v_in ↑", xCenter + 8, yCenter + 65);

        // Outflow jets (horizontal)
        ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(xCenter - 35, yCenter); ctx.lineTo(xCenter - 110, yCenter); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(xCenter + 35, yCenter); ctx.lineTo(xCenter + 110, yCenter); ctx.stroke();
        ctx.fillStyle = "#ef4444"; ctx.font = "bold 10px Inter";
        ctx.fillText("← Jet v_A", xCenter - 120, yCenter - 8);
        ctx.fillText("Jet v_A →", xCenter + 65, yCenter - 8);

        // Reconnecting Hyperbolic Field Lines
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
        [-40, -20, 20, 40].forEach(d => {
          ctx.beginPath();
          ctx.moveTo(xCenter - 120, yCenter + d * 1.8);
          ctx.quadraticCurveTo(xCenter, yCenter + d * 0.2, xCenter + 120, yCenter + d * 1.8);
          ctx.stroke();
        });

        // X-Point resistive diffusion region
        ctx.fillStyle = "rgba(236, 72, 153, 0.4)";
        ctx.fillRect(xCenter - 25, yCenter - 15, 50, 30);
        ctx.strokeStyle = "#ec4899"; ctx.strokeRect(xCenter - 25, yCenter - 15, 50, 30);
        ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px Inter"; ctx.textAlign = "center";
        ctx.fillText("X-Point", xCenter, yCenter + 4);
        ctx.textAlign = "left";
      }

      // Status banner
      ctx.fillStyle = isIdeal ? "rgba(16, 185, 129, 0.2)" : "rgba(236, 72, 153, 0.2)";
      ctx.fillRect(px0 + 20, py0 + ph - 40, pw - 40, 28);
      ctx.strokeStyle = isIdeal ? "#10b981" : "#ec4899"; ctx.lineWidth = 1;
      ctx.strokeRect(px0 + 20, py0 + ph - 40, pw - 40, 28);
      ctx.fillStyle = isIdeal ? "#10b981" : "#ec4899"; ctx.font = "bold 11px Inter";
      ctx.fillText(isIdeal ? "✓ IDEAL MHD: dΦ/dt = 0 (Magnetic Flux Rigorously Frozen In)" : `⚡ RESISTIVE DISSIPATION: R_m = ${Rm} (Magnetic Tearing & Energy Release)`, px0 + 30, py0 + ph - 22);

      // Right Area: Telemetry
      const tx = 460, ty = 25, tw = 270, th = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("MHD Flux & Reconnection Telemetry", tx + 14, ty + 24);

      const items = [
        ["Plasma Flow Speed v₀:", `${v0} km/s`],
        ["Resistivity η:", `${eta === 0 ? "0.0 (Superconducting)" : eta + " μΩ·m"}`],
        ["Magnetic Reynolds R_m:", `${Rm >= 99999 ? "∞ (Ideal MHD)" : Rm}`],
        ["Induction Equation:", "∂B/∂t = ∇×(v×B) + (η/μ₀)∇²B"],
        ["Diffusion Timescale τ_d:", `${eta === 0 ? "∞ (No Diffusion)" : (450 / eta).toFixed(1) + " ms"}`],
        ["Alfvén Outflow Speed v_out:", "v_A = B / √(μ₀ρ)"],
        ["Sweet-Parker Rate:", `${eta === 0 ? "0 (Zero Reconnection)" : (1 / Math.sqrt(Rm)).toFixed(4)} · v_A`],
        ["Energy Conversion:", "Magnetic B²/(2μ₀) ➔ Heat + Flow"],
        ["Astrophysical Manifestation:", "Solar Flares & Auroral Substorms"]
      ];

      items.forEach((item, idx) => {
        const iy = ty + 50 + idx * 30;
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText(item[0], tx + 12, iy);
        ctx.fillStyle = idx === 2 ? (isIdeal ? "#10b981" : "#ec4899") : (idx === 7 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter";
        ctx.fillText(item[1], tx + 155, iy);
      });
    }
  },
"""

with open("sims_part1.py", "a") as f:
    f.write(sims_code)

print("Simulations 3 to 8 appended to sims_part1.py successfully.")
