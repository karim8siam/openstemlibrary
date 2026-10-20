// Astrophysics & Cosmology Interactive Simulation Suite
// 16 Real-Time 60 FPS Canvas Simulations for Celestial Mechanics, Stellar Evolution, Relativistic Objects & Cosmology

window.ASTRO_SIMS = {
  // =========================================================================
  // CHAPTER 1: CELESTIAL MECHANICS & DISTANCE LADDER
  // =========================================================================

  // 1. Celestial Sphere & Coordinate Transformations
  "astro-celestial-sphere-sim": {
    title: "Interactive Celestial Sphere & Coordinate Converter",
    desc: "3D-projected celestial sphere with equator, ecliptic (ε = 23.44°), observer horizon, zenith, meridian, and real-time equatorial (α, δ) to horizontal (Alt, Az) transformation.",
    isAnimated: true,
    controls: [
      { id: "obsLat", label: "Observer Latitude φ (deg)", min: -90, max: 90, step: 1, value: 38 },
      { id: "raStar", label: "Right Ascension α (hr)", min: 0, max: 24, step: 0.1, value: 5.5 },
      { id: "decStar", label: "Declination δ (deg)", min: -80, max: 80, step: 1, value: 20 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const phiDeg = vals.obsLat !== undefined ? vals.obsLat : 38;
      const raHr = vals.raStar !== undefined ? vals.raStar : 5.5;
      const decDeg = vals.decStar !== undefined ? vals.decStar : 20;

      const phi = (phiDeg * Math.PI) / 180;
      const dec = (decDeg * Math.PI) / 180;
      const lstHr = (time * 0.5) % 24; // Local Sidereal Time advances with time
      const lstDeg = (lstHr / 24) * 360;
      const raDeg = (raHr / 24) * 360;
      const hourAngleDeg = ((lstDeg - raDeg + 360) % 360);
      const H = (hourAngleDeg * Math.PI) / 180;

      // Spherical trig: Alt, Az
      const sinAlt = Math.sin(phi) * Math.sin(dec) + Math.cos(phi) * Math.cos(dec) * Math.cos(H);
      const alt = Math.asin(Math.max(-1, Math.min(1, sinAlt)));
      const altDeg = (alt * 180) / Math.PI;

      const cosAz = (Math.sin(dec) - Math.sin(phi) * sinAlt) / (Math.cos(phi) * Math.cos(alt) + 1e-7);
      let az = Math.acos(Math.max(-1, Math.min(1, cosAz)));
      if (Math.sin(H) > 0) az = 2 * Math.PI - az;
      const azDeg = (az * 180) / Math.PI;

      // 3D Sphere projection
      const cx = 220, cy = 200, R = 140;
      const rotY = time * 0.1;

      // Background starfield dots
      ctx.fillStyle = "rgba(255,255,255,0.4)";
      for (let i = 0; i < 40; i++) {
        const sx = (Math.sin(i * 99.3) * 0.5 + 0.5) * w;
        const sy = (Math.cos(i * 33.7) * 0.5 + 0.5) * h;
        ctx.fillRect(sx, sy, 1.2, 1.2);
      }

      // Celestial Sphere outer boundary
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.stroke();

      // Horizon Plane (ellipse based on tilt)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.ellipse(cx, cy, R, R * 0.35, 0, 0, Math.PI * 2);
      ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Observer Horizon", cx - R + 10, cy + 18);

      // Celestial Equator (tilted by 90 - phi)
      const eqTilt = (90 - phiDeg) * (Math.PI / 180);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 3]);
      ctx.beginPath();
      ctx.ellipse(cx, cy, R, R * Math.abs(Math.sin(eqTilt)), eqTilt, 0, Math.PI * 2);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("Celestial Equator", cx + 25, cy - R * 0.5);

      // Zenith & Nadir
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(cx, cy - R - 15); ctx.lineTo(cx, cy + R + 15); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.fillText("Zenith (Z)", cx + 6, cy - R - 5);
      ctx.fillText("Nadir", cx + 6, cy + R + 12);

      // North Celestial Pole
      const ncpX = cx + R * Math.cos(phi);
      const ncpY = cy - R * Math.sin(phi);
      ctx.fillStyle = "#a855f7";
      ctx.beginPath(); ctx.arc(ncpX, ncpY, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("NCP (δ=+90°)", ncpX + 8, ncpY + 3);

      // Target Star position on sphere
      const starRad = R * Math.cos(dec);
      const sAng = H + rotY;
      const px = cx + starRad * Math.sin(sAng);
      const py = cy - R * Math.sin(dec) * Math.cos(phi) + starRad * Math.cos(sAng) * Math.sin(phi) * 0.3;

      // Glow & star marker
      const isAbove = altDeg >= 0;
      ctx.fillStyle = isAbove ? "#fbbf24" : "#64748b";
      ctx.shadowColor = isAbove ? "#fbbf24" : "transparent"; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = isAbove ? "#fef08a" : "#94a3b8"; ctx.font = "bold 12px Inter";
      ctx.fillText(`Target Star (α=${raHr.toFixed(1)}h, δ=${decDeg}°)`, px + 10, py - 6);

      // Diurnal Path circle
      ctx.strokeStyle = "rgba(251, 191, 36, 0.3)"; ctx.lineWidth = 1; ctx.setLineDash([2, 4]);
      ctx.beginPath(); ctx.arc(cx, cy - R * Math.sin(dec) * 0.7, starRad * 0.8, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      // Telemetry Box
      const bx = 420, by = 40, bw = 310, bh = 320;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.fillRect(bx, by, bw, bh); ctx.strokeRect(bx, by, bw, bh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter";
      ctx.fillText("Equatorial ➔ Horizontal Converter", bx + 16, by + 28);

      const items = [
        ["Observer Latitude φ:", `${phiDeg >= 0 ? "+" : ""}${phiDeg.toFixed(1)}° (${phiDeg >= 0 ? "North" : "South"})`],
        ["Local Sidereal Time (LST):", `${lstHr.toFixed(2)} h (${lstDeg.toFixed(1)}°)`],
        ["Hour Angle H = LST - α:", `${(hourAngleDeg / 15).toFixed(2)} h (${hourAngleDeg.toFixed(1)}°)`],
        ["Calculated Altitude a:", `${altDeg.toFixed(2)}°`],
        ["Calculated Azimuth A:", `${azDeg.toFixed(2)}°`],
        ["Visibility Status:", isAbove ? "ABOVE HORIZON (Visible)" : "BELOW HORIZON (Blocked)"],
        ["Circumpolar Limit:", `δ ≥ ${(90 - Math.abs(phiDeg)).toFixed(1)}°`]
      ];

      ctx.font = "12px Inter";
      items.forEach((item, idx) => {
        const iy = by + 65 + idx * 32;
        ctx.fillStyle = "#94a3b8";
        ctx.fillText(item[0], bx + 16, iy);
        ctx.fillStyle = idx === 5 ? (isAbove ? "#10b981" : "#ef4444") : (idx === 3 || idx === 4 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 12px Inter";
        ctx.fillText(item[1], bx + 185, iy);
        ctx.font = "12px Inter";
      });

      // Spherical trig formula display
      ctx.fillStyle = "#64748b"; ctx.font = "11px Inter";
      ctx.fillText("sin(a) = sin φ sin δ + cos φ cos δ cos H", bx + 16, by + 295);
    }
  },
  // 2. Cosmic Distance Ladder & Cepheid Leavitt Law
  "astro-distance-ladder-sim": {
    title: "Cosmic Distance Ladder: Parallax & Cepheid Leavitt Law",
    desc: "Interactive trigonometric parallax geometry coupled to the classical Cepheid Period-Luminosity relation (Leavitt Law: MV = -2.81 log P - 1.43) and distance modulus.",
    isAnimated: true,
    controls: [
      { id: "parallaxArcsec", label: "Parallax Angle p (arcsec)", min: 0.02, max: 0.77, step: 0.01, value: 0.25 },
      { id: "cepheidPeriod", label: "Cepheid Period P (days)", min: 1.5, max: 50, step: 0.5, value: 10 },
      { id: "extinctionAv", label: "Interstellar Extinction Av (mag)", min: 0.0, max: 2.0, step: 0.1, value: 0.3 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const pArcsec = vals.parallaxArcsec !== undefined ? vals.parallaxArcsec : 0.25;
      const Pdays = vals.cepheidPeriod !== undefined ? vals.cepheidPeriod : 10;
      const Av = vals.extinctionAv !== undefined ? vals.extinctionAv : 0.3;

      const dPc = 1.0 / pArcsec;
      const dLy = dPc * 3.26156;

      // Leavitt Law
      const Mv = -2.81 * Math.log10(Pdays) - 1.43;
      const distMod = 5 * Math.log10(dPc) - 5;
      const appMag = Mv + distMod + Av;

      // Left Panel: Parallax Geometry
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("1. Trigonometric Parallax Baseline", 25, 28);

      const sunX = 140, sunY = 280;
      // Sun
      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(sunX, sunY, 12, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fef08a"; ctx.font = "10px Inter"; ctx.fillText("Sun", sunX - 10, sunY + 22);

      // Earth Orbit
      const orbR = 75;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.ellipse(sunX, sunY, orbR, orbR * 0.35, 0, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      // Earth Positions (January / July)
      const eAng = time * 0.8;
      const e1X = sunX - orbR * Math.cos(eAng);
      const e1Y = sunY - orbR * 0.35 * Math.sin(eAng);
      const e2X = sunX + orbR * Math.cos(eAng);
      const e2Y = sunY + orbR * 0.35 * Math.sin(eAng);

      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(e1X, e1Y, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#60a5fa"; ctx.beginPath(); ctx.arc(e2X, e2Y, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Earth (t=0)", e1X - 25, e1Y - 8);
      ctx.fillText("Earth (t+6mo)", e2X - 25, e2Y + 16);

      // Target Nearby Star
      const starX = sunX;
      const starDistPx = Math.max(70, Math.min(200, 240 - pArcsec * 200));
      const starY = sunY - starDistPx;

      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(starX, starY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fda4af"; ctx.font = "11px Inter"; ctx.fillText(`Target Star (p = ${pArcsec.toFixed(2)}")`, starX + 12, starY + 4);

      // Parallax sight lines
      ctx.strokeStyle = "rgba(244, 63, 94, 0.4)"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(e1X, e1Y); ctx.lineTo(starX, starY); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(e2X, e2Y); ctx.lineTo(starX, starY); ctx.stroke();
      ctx.strokeStyle = "rgba(255,255,255,0.2)"; ctx.beginPath(); ctx.moveTo(sunX, sunY); ctx.lineTo(starX, starY); ctx.stroke();

      // Right Panel: Cepheid Leavitt Law Period-Luminosity
      const gx = 380, gy = 40, gw = 350, gh = 180;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("2. Cepheid Period-Luminosity (Leavitt Law)", gx + 15, gy + 22);

      // Graph axes
      const ox = gx + 50, oy = gy + 150, plotW = 270, plotH = 110;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - plotH); ctx.lineTo(ox, oy); ctx.lineTo(ox + plotW, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("log₁₀(P / days)", ox + plotW - 60, oy + 16);
      ctx.save(); ctx.translate(ox - 25, oy - 40); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Abs Mag M_V", 0, 0); ctx.restore();

      // P-L Curve line: logP from 0.2 to 1.8 -> MV from -2.0 to -6.5
      ctx.strokeStyle = "#34d399"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let lp = 0.2; lp <= 1.8; lp += 0.05) {
        const curM = -2.81 * lp - 1.43;
        const cxp = ox + ((lp - 0.2) / 1.6) * plotW;
        const cyp = oy - ((-curM - 2.0) / 4.8) * plotH;
        if (lp === 0.2) ctx.moveTo(cxp, cyp); else ctx.lineTo(cxp, cyp);
      }
      ctx.stroke();

      // Current Cepheid point
      const curLp = Math.log10(Pdays);
      const curPx = ox + ((curLp - 0.2) / 1.6) * plotW;
      const curPy = oy - ((-Mv - 2.0) / 4.8) * plotH;

      // Pulsating Star Marker
      const pulsate = 1 + 0.3 * Math.sin(time * (10 / Pdays) * Math.PI * 2);
      ctx.fillStyle = "#f59e0b"; ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 12;
      ctx.beginPath(); ctx.arc(curPx, curPy, 5 * pulsate, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Bottom Telemetry Summary
      const by = 240, bh = 140;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, by, gw, bh); ctx.strokeRect(gx, by, gw, bh);

      ctx.fillStyle = "#f1f5f9"; ctx.font = "bold 13px Inter";
      ctx.fillText("Cosmic Distance Ladder Computations", gx + 15, by + 22);

      const metrics = [
        ["Parallax Distance d = 1/p:", `${dPc.toFixed(2)} pc (${dLy.toFixed(1)} ly)`],
        ["Cepheid Absolute Mag M_V:", `${Mv.toFixed(2)} mag (P = ${Pdays.toFixed(1)} d)`],
        ["Distance Modulus μ = m - M:", `${distMod.toFixed(2)} mag`],
        ["Apparent Magnitude m_V:", `${appMag.toFixed(2)} mag (with A_V = ${Av.toFixed(1)})`]
      ];

      ctx.font = "12px Inter";
      metrics.forEach((m, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(m[0], gx + 15, by + 48 + idx * 22);
        ctx.fillStyle = idx === 0 ? "#38bdf8" : (idx === 1 ? "#34d399" : "#fbbf24");
        ctx.font = "bold 12px Inter";
        ctx.fillText(m[1], gx + 200, by + 48 + idx * 22);
        ctx.font = "12px Inter";
      });
    }
  },
  // =========================================================================
  // CHAPTER 2: SOLAR PHYSICS & EXOPLANETS
  // =========================================================================

  // 3. Solar Interior & Thermonuclear Fusion Engine
  "astro-solar-interior-sim": {
    title: "Standard Solar Model Interior & p-p vs CNO Energy Generation",
    desc: "Radial profiles of temperature T(r), density ρ(r), enclosed mass M(r), and luminosity L(r), with temperature-dependent p-p chain (ε ∝ T⁴) vs CNO cycle (ε ∝ T¹⁷) cross-sections.",
    isAnimated: true,
    controls: [
      { id: "coreTemp", label: "Core Temp Tc (x10⁶ K)", min: 10, max: 35, step: 0.5, value: 15.7 },
      { id: "stellarMass", label: "Stellar Mass M/M⊙", min: 0.6, max: 2.2, step: 0.1, value: 1.0 },
      { id: "metallicityZ", label: "Metallicity Z", min: 0.005, max: 0.04, step: 0.005, value: 0.02 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Tc = vals.coreTemp !== undefined ? vals.coreTemp : 15.7; // in 10^6 K
      const M = vals.stellarMass !== undefined ? vals.stellarMass : 1.0;
      const Z = vals.metallicityZ !== undefined ? vals.metallicityZ : 0.02;

      // Energy generation rate calculations
      // pp: eps_pp ~ rho * X^2 * (T6)^4
      // cno: eps_cno ~ rho * X * Z * (T6)^17
      const T6 = Tc;
      const eps_pp = Math.pow(T6 / 15.7, 4.0);
      const eps_cno = (Z / 0.02) * Math.pow(T6 / 15.7, 17.0);
      const total_eps = eps_pp + eps_cno;
      const ppFraction = (eps_pp / total_eps) * 100;
      const cnoFraction = (eps_cno / total_eps) * 100;

      // Left Panel: Radial Cross Section of Sun
      const cx = 175, cy = 200, R = 130;
      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 13px Inter";
      ctx.fillText("Radial Zones & Convection Cells", 35, 28);

      // Convective Outer Envelope (r: 0.7 - 1.0 R)
      ctx.fillStyle = "rgba(245, 158, 11, 0.25)";
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.fill();

      // Animated Convection Cells
      ctx.strokeStyle = "rgba(245, 158, 11, 0.6)"; ctx.lineWidth = 1.2;
      for (let a = 0; a < Math.PI * 2; a += Math.PI / 6) {
        const r1 = R * 0.72, r2 = R * 0.95;
        const ca = a + time * 0.3;
        ctx.beginPath();
        ctx.arc(cx + Math.cos(ca) * (r1 + r2) * 0.5, cy + Math.sin(ca) * (r1 + r2) * 0.5, 12, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Radiative Intermediate Zone (r: 0.25 - 0.7 R)
      ctx.fillStyle = "rgba(234, 88, 12, 0.4)";
      ctx.beginPath(); ctx.arc(cx, cy, R * 0.7, 0, Math.PI * 2); ctx.fill();

      // Thermonuclear Core (r: 0.0 - 0.25 R)
      ctx.fillStyle = "#ef4444"; ctx.shadowColor = "#f97316"; ctx.shadowBlur = 18;
      ctx.beginPath(); ctx.arc(cx, cy, R * 0.25, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Zone labels
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px Inter";
      ctx.fillText("Core", cx - 12, cy + 3);
      ctx.fillStyle = "#fed7aa"; ctx.font = "10px Inter";
      ctx.fillText("Radiative Zone", cx + R * 0.32, cy - 10);
      ctx.fillStyle = "#fef08a";
      ctx.fillText("Convective Zone", cx + R * 0.65, cy + 25);

      // Right Panel: Standard Solar Model Radial Profiles
      const gx = 370, gy = 35, gw = 365, gh = 200;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("SSM Radial Profiles [T(r), ρ(r), M(r), L(r)]", gx + 15, gy + 22);

      const ox = gx + 45, oy = gy + 165, pw = 295, ph = 125;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("r / R⊙", ox + pw - 30, oy + 16);
      ctx.fillText("1.0", ox + pw - 8, oy + 14);
      ctx.fillText("0.0", ox - 5, oy + 14);

      // 4 Normalized Radial Curves
      // 1. Temperature: T ~ Tc * (1 - r^0.8)
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2; ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const r_norm = i / 100;
        const T_val = Math.max(0, 1 - Math.pow(r_norm, 0.75));
        const px = ox + r_norm * pw;
        const py = oy - T_val * ph;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // 2. Density: rho ~ rho_c * exp(-r / 0.15)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const r_norm = i / 100;
        const rho_val = Math.exp(-r_norm / 0.18);
        const px = ox + r_norm * pw;
        const py = oy - rho_val * ph;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // 3. Luminosity: L(r) climbs from 0 to 1 inside core (r < 0.25)
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2; ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const r_norm = i / 100;
        const L_val = 1 - Math.exp(-Math.pow(r_norm / 0.18, 2.5));
        const px = ox + r_norm * pw;
        const py = oy - L_val * ph;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Profile legend
      ctx.font = "10px Inter";
      ctx.fillStyle = "#ef4444"; ctx.fillText("— T(r)", ox + 15, oy - ph + 15);
      ctx.fillStyle = "#38bdf8"; ctx.fillText("— ρ(r)", ox + 70, oy - ph + 15);
      ctx.fillStyle = "#fbbf24"; ctx.fillText("— L(r)", ox + 125, oy - ph + 15);

      // Bottom Telemetry: p-p vs CNO Dominance
      const by = 250, bh = 135;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, by, gw, bh); ctx.strokeRect(gx, by, gw, bh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Thermonuclear Regime Breakdown", gx + 15, by + 22);

      // Horizontal Bar for Fusion Split
      const bx_bar = gx + 20, by_bar = by + 40, barW = gw - 40, barH = 18;
      ctx.fillStyle = "#f59e0b";
      ctx.fillRect(bx_bar, by_bar, barW * (ppFraction / 100), barH);
      ctx.fillStyle = "#3b82f6";
      ctx.fillRect(bx_bar + barW * (ppFraction / 100), by_bar, barW * (cnoFraction / 100), barH);

      ctx.fillStyle = "#000000"; ctx.font = "bold 10px Inter";
      if (ppFraction > 15) ctx.fillText(`p-p: ${ppFraction.toFixed(1)}%`, bx_bar + 8, by_bar + 13);
      if (cnoFraction > 15) ctx.fillText(`CNO: ${cnoFraction.toFixed(1)}%`, bx_bar + barW - 65, by_bar + 13);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Core Temp Tc: ${Tc.toFixed(1)} × 10⁶ K  |  Crossover Temp: 15.7 × 10⁶ K`, gx + 20, by + 80);
      ctx.fillStyle = Tc > 16.5 ? "#60a5fa" : "#fbbf24"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Current Fusion Mode: ${Tc > 16.5 ? "CNO CYCLE DOMINANT (Steep T¹⁷)" : "PROTON-PROTON CHAIN DOMINANT (T⁴)"}`, gx + 20, by + 102);
    }
  },
  // 4. Exoplanet Transit Photometry & Doppler Radial Velocity
  "astro-exoplanet-transit-sim": {
    title: "Exoplanet Transit Photometry & Doppler Radial Velocity",
    desc: "Simultaneous photometric light curve transit depth ΔF/F = (Rp/R*)² with limb darkening, and Doppler spectroscopic stellar radial velocity wobble K.",
    isAnimated: true,
    controls: [
      { id: "radiusRatio", label: "Radius Ratio Rp / R*", min: 0.05, max: 0.22, step: 0.01, value: 0.12 },
      { id: "orbitalInc", label: "Inclination i (deg)", min: 82, max: 90, step: 0.5, value: 88.5 },
      { id: "semiMajorAxis", label: "Semi-major Axis a (AU)", min: 0.03, max: 0.3, step: 0.01, value: 0.08 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const k = vals.radiusRatio !== undefined ? vals.radiusRatio : 0.12;
      const incDeg = vals.orbitalInc !== undefined ? vals.orbitalInc : 88.5;
      const aAu = vals.semiMajorAxis !== undefined ? vals.semiMajorAxis : 0.08;

      const inc = (incDeg * Math.PI) / 180;
      const transitDepthPct = (k * k) * 100;
      const periodSec = 6.0; // simulation cycle period
      const phase = ((time / periodSec) % 1.0); // 0 to 1
      const trueAnomaly = phase * Math.PI * 2;

      // Doppler wobble semi-amplitude K
      const K_kms = 120 * (k / 0.1) * Math.sin(inc) / Math.sqrt(aAu / 0.08);
      const vr = K_kms * Math.sin(trueAnomaly);

      // Star & Planet coordinates
      const cx = 175, cy = 110, Rstar = 55;
      const xOrbit = Math.cos(trueAnomaly);
      const yOrbit = Math.sin(trueAnomaly) * Math.cos(inc);
      const zOrbit = Math.sin(trueAnomaly) * Math.sin(inc); // positive = in front of star

      const px = cx + xOrbit * 120;
      const py = cy + yOrbit * 120;
      const Rplanet = Rstar * k;

      // Title
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Transit Telescope View & Doppler Shift", 25, 25);

      // If planet is behind star, draw planet first
      if (zOrbit < 0) {
        ctx.fillStyle = "#475569"; ctx.beginPath(); ctx.arc(px, py, Rplanet, 0, Math.PI * 2); ctx.fill();
      }

      // Host Star with limb darkening gradient
      const grad = ctx.createRadialGradient(cx, cy, 5, cx, cy, Rstar);
      grad.addColorStop(0, "#fffbeb");
      grad.addColorStop(0.7, "#fbbf24");
      grad.addColorStop(1.0, "#d97706");
      ctx.fillStyle = grad; ctx.beginPath(); ctx.arc(cx, cy, Rstar, 0, Math.PI * 2); ctx.fill();

      // If planet is in front of star, draw silhouette
      const isTransiting = (zOrbit >= 0 && Math.hypot(px - cx, py - cy) < (Rstar + Rplanet));
      if (zOrbit >= 0) {
        ctx.fillStyle = isTransiting ? "#020617" : "#334155";
        ctx.strokeStyle = isTransiting ? "#f43f5e" : "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.arc(px, py, Rplanet, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
      }

      // Doppler indicator on Star
      ctx.fillStyle = vr < 0 ? "#38bdf8" : "#f43f5e";
      ctx.font = "bold 11px Inter";
      ctx.fillText(vr < 0 ? `← BLUESHIFT (${vr.toFixed(1)} km/s)` : `REDSHIFT (${vr.toFixed(1)} km/s) →`, cx - 60, cy + Rstar + 22);

      // Bottom-Left: Doppler Radial Velocity Curve
      const dvx = 35, dvy = 240, dvw = 300, dvh = 140;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(dvx, dvy, dvw, dvh); ctx.strokeRect(dvx, dvy, dvw, dvh);

      ctx.fillStyle = "#60a5fa"; ctx.font = "bold 12px Inter";
      ctx.fillText("Spectroscopic Radial Velocity Curve v_r(t)", dvx + 12, dvy + 20);

      const doy = dvy + 75;
      ctx.strokeStyle = "#475569"; ctx.beginPath(); ctx.moveTo(dvx + 35, doy); ctx.lineTo(dvx + dvw - 15, doy); ctx.stroke();

      // Sine curve
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.beginPath();
      for (let s = 0; s < dvw - 50; s++) {
        const ph = s / (dvw - 50);
        const vy = doy - Math.sin(ph * Math.PI * 2) * 45;
        if (s === 0) ctx.moveTo(dvx + 35 + s, vy); else ctx.lineTo(dvx + 35 + s, vy);
      }
      ctx.stroke();

      // Current RV point
      const curRvx = dvx + 35 + phase * (dvw - 50);
      const curRvy = doy - Math.sin(phase * Math.PI * 2) * 45;
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(curRvx, curRvy, 5, 0, Math.PI * 2); ctx.fill();

      // Right Panel: Photometric Light Curve Dip
      const lcx = 360, lcy = 35, lcw = 375, lch = 345;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(lcx, lcy, lcw, lch); ctx.strokeRect(lcx, lcy, lcw, lch);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Kepler Photometric Transit Light Curve F(t) / F₀", lcx + 15, lcy + 25);

      const lox = lcx + 50, loy = lcy + 190, lpw = 300, lph = 140;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(lox, loy - lph); ctx.lineTo(lox, loy); ctx.lineTo(lox + lpw, loy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Orbital Phase φ", lox + lpw - 70, loy + 16);
      ctx.fillText("1.00", lox - 30, loy - lph + 15);
      ctx.fillText(`${(1.0 - transitDepthPct/100).toFixed(3)}`, lox - 40, loy - 15);

      // Draw light curve with ingress, bottom, egress
      ctx.strokeStyle = "#34d399"; ctx.lineWidth = 2.5; ctx.beginPath();
      const dipDepthPx = (transitDepthPct / 5.0) * lph; // scaled
      for (let s = 0; s < lpw; s++) {
        const ph = s / lpw;
        let flux = 1.0;
        // Transit centered at phase 0.25 (when z > 0 and crossing center)
        const dPhase = Math.abs(ph - 0.25);
        if (dPhase < 0.08) {
          if (dPhase < 0.04) {
            flux = 1.0 - (transitDepthPct / 100);
          } else {
            const slope = (0.08 - dPhase) / 0.04;
            flux = 1.0 - (transitDepthPct / 100) * slope;
          }
        }
        const py = (loy - lph + 15) + (1.0 - flux) * 2000;
        if (s === 0) ctx.moveTo(lox + s, py); else ctx.lineTo(lox + s, py);
      }
      ctx.stroke();

      // Current light curve position
      const curLcx = lox + phase * lpw;
      let curFlux = 1.0;
      const dPh = Math.abs(phase - 0.25);
      if (dPh < 0.08) {
        curFlux = dPh < 0.04 ? 1.0 - (transitDepthPct / 100) : 1.0 - (transitDepthPct / 100) * ((0.08 - dPh) / 0.04);
      }
      const curLcy = (loy - lph + 15) + (1.0 - curFlux) * 2000;
      ctx.fillStyle = "#f43f5e"; ctx.shadowColor = "#f43f5e"; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(curLcx, curLcy, 5, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Stats Box inside Right Panel
      const sby = lcy + 225;
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#1e293b";
      ctx.fillRect(lcx + 15, sby, lcw - 30, 100); ctx.strokeRect(lcx + 15, sby, lcw - 30, 100);

      const items = [
        ["Transit Depth ΔF/F = (Rp/R*)²:", `${transitDepthPct.toFixed(2)} %`],
        ["Planet Radius Rp:", `${(k * 109.2).toFixed(1)} R⊕ (${k.toFixed(3)} R⊙)`],
        ["Doppler RV Semi-Amplitude K:", `${K_kms.toFixed(2)} km/s`],
        ["Orbital Semi-Major Axis a:", `${aAu.toFixed(3)} AU`]
      ];
      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], lcx + 25, sby + 22 + idx * 22);
        ctx.fillStyle = idx === 0 ? "#34d399" : (idx === 2 ? "#60a5fa" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], lcx + 245, sby + 22 + idx * 22);
        ctx.font = "11px Inter";
      });
    }
  },
  // =========================================================================
  // CHAPTER 3: STELLAR STRUCTURE & EVOLUTION
  // =========================================================================

  // 5. Hertzsprung-Russell Diagram & Evolutionary Tracks
  "astro-hr-diagram-sim": {
    title: "Interactive Hertzsprung-Russell Diagram & Evolutionary Tracks",
    desc: "Complete empirical log(T_eff) vs log(L/L⊙) HR diagram with spectral classes (O, B, A, F, G, K, M), Main Sequence, Subgiant, RGB, AGB, and White Dwarf branches for stars from 0.8 to 25 M⊙.",
    isAnimated: true,
    controls: [
      { id: "starMass", label: "Initial Mass M (M⊙)", min: 0.8, max: 20, step: 0.2, value: 1.0 },
      { id: "evoPhase", label: "Evolutionary Phase", min: 0, max: 100, step: 1, value: 20 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const M = vals.starMass !== undefined ? vals.starMass : 1.0;
      const phase = vals.evoPhase !== undefined ? vals.evoPhase : 20;

      // HR Diagram Coordinates
      const gx = 50, gy = 30, gw = 420, gh = 340;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      // Title & Spectral axis
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Hertzsprung-Russell Diagram [log Teff vs log L/L⊙]", gx + 15, gy + 22);

      // Temperature reversed: 40,000 K (left) to 2,500 K (right)
      // log Teff from 4.6 (left) to 3.4 (right)
      // log L/L⊙ from -4 (bottom) to +6 (top)
      const ox = gx + 45, oy = gy + gh - 45, pw = gw - 65, ph = gh - 75;

      // Spectral Classes header at top
      const spec = ["O", "B", "A", "F", "G", "K", "M"];
      const specColors = ["#93c5fd", "#bfdbfe", "#ffffff", "#fef08a", "#fde047", "#f97316", "#ef4444"];
      ctx.font = "bold 11px Inter";
      spec.forEach((s, i) => {
        const sx = ox + (i / 6) * pw;
        ctx.fillStyle = specColors[i];
        ctx.fillText(s, sx - 4, gy + 42);
      });

      // Main Sequence Band
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 14; ctx.beginPath();
      ctx.moveTo(ox + 10, oy - ph + 25);
      ctx.bezierCurveTo(ox + pw * 0.35, oy - ph * 0.7, ox + pw * 0.6, oy - ph * 0.35, ox + pw - 20, oy - 20);
      ctx.stroke();

      // Giant & Supergiant regions
      ctx.fillStyle = "rgba(239, 68, 68, 0.15)";
      ctx.fillRect(ox + pw * 0.6, oy - ph + 30, pw * 0.38, ph * 0.45);
      ctx.fillStyle = "#fca5a5"; ctx.font = "10px Inter";
      ctx.fillText("Red Giants & AGB", ox + pw * 0.65, oy - ph * 0.7);

      // White Dwarf Region
      ctx.fillStyle = "rgba(147, 197, 253, 0.15)";
      ctx.fillRect(ox + 20, oy - ph * 0.25, pw * 0.3, ph * 0.22);
      ctx.fillStyle = "#93c5fd"; ctx.fillText("White Dwarfs", ox + 35, oy - 25);

      // Calculate track for star mass M
      // ZAMS position:
      const zams_logL = 3.8 * Math.log10(M); // L ~ M^3.8
      const zams_logT = 3.76 + 0.12 * Math.log10(M);
      const zamsX = ox + pw * (1 - (zams_logT - 3.4) / 1.2);
      const zamsY = oy - ((zams_logL + 4) / 10) * ph;

      // Track trajectory based on evolutionary phase (0: ZAMS -> 100: End state)
      let curX = zamsX, curY = zamsY;
      let stageName = "Zero-Age Main Sequence (ZAMS)";

      if (phase < 35) {
        // Main sequence burning
        stageName = "Main Sequence Core Hydrogen Burning";
        curX = zamsX + (phase / 35) * 20;
        curY = zamsY - (phase / 35) * 15;
      } else if (phase < 60) {
        // Subgiant & Red Giant Branch
        stageName = M < 8 ? "Red Giant Branch (Shell H-burning)" : "Red Supergiant (Advanced burning)";
        const p2 = (phase - 35) / 25;
        curX = zamsX + 20 + p2 * 110;
        curY = zamsY - 15 - p2 * 90;
      } else if (phase < 80) {
        // Horizontal Branch / Helium Flash
        stageName = "Helium Core Burning (Horizontal Branch)";
        const p3 = (phase - 60) / 20;
        curX = (zamsX + 130) - p3 * 60;
        curY = (zamsY - 105) + p3 * 15;
      } else {
        // End State
        if (M < 8) {
          stageName = "Planetary Nebula ➔ White Dwarf Cooling Track";
          const p4 = (phase - 80) / 20;
          curX = (zamsX + 70) - p4 * 120;
          curY = (zamsY - 90) + p4 * 180;
        } else {
          stageName = "Iron Core Collapse ➔ Supernova Type II";
          curX = zamsX + 130;
          curY = zamsY - 110;
        }
      }

      // Draw Evolutionary Track line
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([3, 2]);
      ctx.beginPath(); ctx.moveTo(zamsX, zamsY);
      ctx.lineTo(zamsX + 20, zamsY - 15);
      ctx.lineTo(zamsX + 130, zamsY - 105);
      ctx.lineTo(zamsX + 70, zamsY - 90);
      if (M < 8) ctx.lineTo(zamsX - 50, zamsY + 90);
      ctx.stroke(); ctx.setLineDash([]);

      // Current Star Marker on HR Diagram
      ctx.fillStyle = "#ffffff"; ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 12;
      ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Right Panel: Real-Time Physical Parameters
      const rx = 490, ry = 30, rw = 245, rh = 340;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Stellar State Parameters", rx + 15, ry + 25);

      const logL_cur = -4 + ((oy - curY) / ph) * 10;
      const logT_cur = 3.4 + (1 - (curX - ox) / pw) * 1.2;
      const L_solar = Math.pow(10, logL_cur);
      const Teff_val = Math.pow(10, logT_cur);
      // R / R_sun = sqrt(L / L_sun) / (T / T_sun)^2
      const R_solar = Math.sqrt(L_solar) / Math.pow(Teff_val / 5778, 2);

      const params = [
        ["Initial Mass M:", `${M.toFixed(1)} M⊙`],
        ["Effective Temp Teff:", `${Math.round(Teff_val)} K`],
        ["Luminosity L:", `${L_solar < 100 ? L_solar.toFixed(2) : Math.round(L_solar)} L⊙`],
        ["Stellar Radius R:", `${R_solar.toFixed(2)} R⊙`],
        ["Spectral Type:", Teff_val > 30000 ? "O" : (Teff_val > 10000 ? "B" : (Teff_val > 7500 ? "A" : (Teff_val > 6000 ? "F" : (Teff_val > 5200 ? "G" : (Teff_val > 3700 ? "K" : "M")))))],
        ["Main Sequence Lifetime:", `${(10 * Math.pow(M, -2.5)).toFixed(2)} Gyr`],
        ["Remnant Destiny:", M < 8 ? "C-O White Dwarf" : (M < 20 ? "Neutron Star" : "Black Hole")]
      ];

      ctx.font = "11px Inter";
      params.forEach((p, i) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(p[0], rx + 15, ry + 58 + i * 28);
        ctx.fillStyle = i === 4 ? "#fbbf24" : (i === 6 ? "#f43f5e" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(p[1], rx + 130, ry + 58 + i * 28);
        ctx.font = "11px Inter";
      });

      // Stage banner
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText("Current Evolutionary Stage:", rx + 15, ry + 275);
      ctx.fillStyle = "#fed7aa"; ctx.font = "10px Inter";
      ctx.fillText(stageName, rx + 15, ry + 295);
    }
  },
  // 6. Chandrasekhar Mass Limit & White Dwarf Degeneracy
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
  // =========================================================================
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
  // 8. General Relativistic Black Hole Geodesics & Ray Tracing
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
  // =========================================================================
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
  // 10. Lin-Shu Spiral Density Waves & Resonances
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
  // =========================================================================
  // CHAPTER 6: EXTRAGALACTIC ASTRONOMY & GRAVITATIONAL LENSING
  // =========================================================================

  // 11. AGN Accretion Disk & Superluminal Jet Kinematics
  "astro-agn-jet-sim": {
    title: "AGN Unified Model & Superluminal Jet Kinematics",
    desc: "Active Galactic Nucleus (AGN) supermassive black hole accretion disk with relativistic Doppler beaming and apparent superluminal jet kinematics β_app = β sinθ / (1 - β cosθ).",
    isAnimated: true,
    controls: [
      { id: "jetBeta", label: "Jet Relativistic Speed β = v/c", min: 0.8, max: 0.995, step: 0.005, value: 0.98 },
      { id: "viewAngle", label: "Viewing Angle θ (deg)", min: 2, max: 60, step: 1, value: 14 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const beta = vals.jetBeta !== undefined ? vals.jetBeta : 0.98;
      const thetaDeg = vals.viewAngle !== undefined ? vals.viewAngle : 14;

      const theta = (thetaDeg * Math.PI) / 180;
      const gamma = 1 / Math.sqrt(Math.max(1e-5, 1 - beta * beta));

      // Apparent speed beta_app = beta sin(theta) / (1 - beta cos(theta))
      const denom = 1 - beta * Math.cos(theta);
      const beta_app = (beta * Math.sin(theta)) / Math.max(1e-4, denom);
      const isSuperluminal = beta_app > 1.0;

      // Doppler beaming factor delta = 1 / [gamma * (1 - beta cos theta)]
      const delta = 1 / (gamma * Math.max(1e-4, denom));
      const fluxBoost = Math.pow(delta, 3.5);

      // Left Panel: AGN Central Engine Schematic
      const cx = 175, cy = 200;
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("AGN Accretion Disk & Relativistic Jet", 25, 25);

      // Dusty Torus
      ctx.fillStyle = "#334155";
      ctx.beginPath(); ctx.ellipse(cx, cy, 110, 35, 0, 0, Math.PI * 2); ctx.fill();

      // Accretion Disk
      const diskGrad = ctx.createRadialGradient(cx, cy, 5, cx, cy, 65);
      diskGrad.addColorStop(0, "#fde047");
      diskGrad.addColorStop(0.4, "#f97316");
      diskGrad.addColorStop(1, "rgba(220, 38, 38, 0.0)");
      ctx.fillStyle = diskGrad;
      ctx.beginPath(); ctx.ellipse(cx, cy, 65, 18, 0, 0, Math.PI * 2); ctx.fill();

      // Supermassive Black Hole
      ctx.fillStyle = "#000000"; ctx.beginPath(); ctx.arc(cx, cy, 10, 0, Math.PI * 2); ctx.fill();

      // Relativistic Plasma Jet (knots moving along jet)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.8)"; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + Math.cos(-Math.PI / 2 + theta * 0.5) * 150, cy - 150); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx - Math.cos(-Math.PI / 2 + theta * 0.5) * 150, cy + 150); ctx.stroke();

      // Moving synchrotron plasma knots
      for (let k = 1; k <= 3; k++) {
        const knotProgress = ((time * 0.4 + k * 0.33) % 1.0);
        const kx = cx + knotProgress * Math.cos(-Math.PI / 2 + theta * 0.5) * 150;
        const ky = cy - knotProgress * 150;
        ctx.fillStyle = "#67e8f9"; ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 10;
        ctx.beginPath(); ctx.arc(kx, ky, 5, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Approaching Jet Knot", cx + 25, cy - 110);
      ctx.fillText("Obscuring Dusty Torus", cx - 95, cy + 30);

      // Right Panel: Apparent Speed Curve & Superluminal Telemetry
      const gx = 360, gy = 35, gw = 375, gh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Superluminal Motion: β_app(θ) vs c", gx + 15, gy + 22);

      const ox = gx + 50, oy = gy + 175, pw = gw - 70, ph = 120;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Viewing Angle θ (deg)", ox + pw - 120, oy + 18);
      ctx.save(); ctx.translate(ox - 30, oy - 35); ctx.rotate(-Math.PI / 2);
      ctx.fillText("β_app = v_app / c", 0, 0); ctx.restore();

      // Horizontal dashed line at beta_app = 1 (c)
      const cLineY = oy - (1.0 / 6.0) * ph;
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(ox, cLineY); ctx.lineTo(ox + pw, cLineY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.fillText("c (Speed of Light)", ox + pw - 95, cLineY - 4);

      // Plot beta_app curve for chosen beta
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let th = 1; th <= 60; th += 1) {
        const rad = (th * Math.PI) / 180;
        const b_app = (beta * Math.sin(rad)) / Math.max(1e-4, 1 - beta * Math.cos(rad));
        const px = ox + (th / 60) * pw;
        const py = oy - (Math.min(6.0, b_app) / 6.0) * ph;
        if (th === 1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current point on curve
      const curX = ox + (thetaDeg / 60) * pw;
      const curY = oy - (Math.min(6.0, beta_app) / 6.0) * ph;
      ctx.fillStyle = isSuperluminal ? "#f43f5e" : "#10b981";
      ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Telemetry Box
      const by = gy + 195;
      const metrics = [
        ["Lorentz Factor γ:", `${gamma.toFixed(2)}`],
        ["Apparent Transverse Speed β_app:", `${beta_app.toFixed(2)} c`],
        ["Doppler Beaming Factor δ:", `${delta.toFixed(2)}`],
        ["Flux Boost Factor δ^(3+α):", `${fluxBoost.toExponential(2)} ×`],
        ["Superluminal Status:", isSuperluminal ? `SUPERLUMINAL (v_app = ${beta_app.toFixed(1)} c > c)` : "SUBLUMINAL (v_app < c)"]
      ];

      ctx.font = "11px Inter";
      metrics.forEach((m, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(m[0], gx + 15, by + 18 + idx * 24);
        ctx.fillStyle = idx === 4 ? (isSuperluminal ? "#f43f5e" : "#10b981") : (idx === 1 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(m[1], gx + 195, by + 18 + idx * 24);
        ctx.font = "11px Inter";
      });
    }
  },
  // 12. Gravitational Lensing & Einstein Rings
  "astro-gravitational-lensing-sim": {
    title: "Gravitational Lensing: Einstein Rings & Caustic Arcs",
    desc: "Interactive thin-screen gravitational lens simulator: solves the lens equation β = θ - θ_E² / θ, rendering Einstein rings, giant distorted arcs, and flux amplification.",
    isAnimated: true,
    controls: [
      { id: "einsteinRadius", label: "Einstein Radius θ_E (arcsec)", min: 10, max: 80, step: 1, value: 45 },
      { id: "sourceOffsetX", label: "Source Offset X (arcsec)", min: -60, max: 60, step: 1, value: 12 },
      { id: "sourceOffsetY", label: "Source Offset Y (arcsec)", min: -60, max: 60, step: 1, value: 8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const thetaE = vals.einsteinRadius !== undefined ? vals.einsteinRadius : 45;
      const betaX = vals.sourceOffsetX !== undefined ? vals.sourceOffsetX : 12;
      const betaY = vals.sourceOffsetY !== undefined ? vals.sourceOffsetY : 8;

      const beta = Math.hypot(betaX, betaY);
      const phiSource = Math.atan2(betaY, betaX);

      // Two image solutions: theta_pm = [beta +/- sqrt(beta^2 + 4 thetaE^2)] / 2
      const discr = Math.sqrt(beta * beta + 4 * thetaE * thetaE);
      const theta1 = (beta + discr) / 2;
      const theta2 = (beta - discr) / 2; // negative (opposite side)

      // Magnifications: mu = [1 - (thetaE / theta)^4]^(-1)
      const mu1 = Math.abs(1 / (1 - Math.pow(thetaE / Math.max(1e-3, theta1), 4)));
      const mu2 = Math.abs(1 / (1 - Math.pow(thetaE / Math.max(1e-3, Math.abs(theta2)), 4)));
      const totalMu = mu1 + mu2;

      // Left Panel: Sky View Observer Plane
      const cx = 200, cy = 200;
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Observer Plane: Lensed Images & Arcs", 25, 25);

      // Einstein Ring boundary (dashed yellow)
      ctx.strokeStyle = "rgba(250, 204, 21, 0.4)"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, thetaE * 1.5, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#facc15"; ctx.font = "10px Inter";
      ctx.fillText(`Einstein Ring θ_E = ${thetaE}"`, cx + thetaE * 1.5 + 8, cy);

      // Lens Galaxy (Elliptical / Cluster center)
      const lensGrad = ctx.createRadialGradient(cx, cy, 2, cx, cy, 30);
      lensGrad.addColorStop(0, "#ffffff");
      lensGrad.addColorStop(0.5, "#fbbf24");
      lensGrad.addColorStop(1, "rgba(245, 158, 11, 0.0)");
      ctx.fillStyle = lensGrad;
      ctx.beginPath(); ctx.arc(cx, cy, 30, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fed7aa"; ctx.font = "10px Inter"; ctx.fillText("Lens Galaxy", cx - 28, cy + 40);

      // True Source position (unlensed position, dashed marker)
      const unlensX = cx + betaX * 1.5;
      const unlensY = cy + betaY * 1.5;
      ctx.strokeStyle = "rgba(255, 255, 255, 0.4)"; ctx.lineWidth = 1; ctx.setLineDash([2, 2]);
      ctx.beginPath(); ctx.arc(unlensX, unlensY, 8, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.fillText("True Source (Unlensed)", unlensX + 12, unlensY + 3);

      // If beta is very close to 0: complete Einstein Ring!
      if (beta < 3) {
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 5; ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 15;
        ctx.beginPath(); ctx.arc(cx, cy, thetaE * 1.5, 0, Math.PI * 2); ctx.stroke();
        ctx.shadowBlur = 0;
      } else {
        // Image 1: Major Arc on source side
        const im1R = theta1 * 1.5;
        const im1X = cx + im1R * Math.cos(phiSource);
        const im1Y = cy + im1R * Math.sin(phiSource);
        const arcSpan1 = Math.min(Math.PI * 0.8, (thetaE / (beta + 1e-3)) * 0.4);

        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = Math.min(8, 2 + Math.log10(mu1) * 2);
        ctx.shadowColor = "#38bdf8"; ctx.shadowBlur = 12;
        ctx.beginPath();
        ctx.arc(cx, cy, im1R, phiSource - arcSpan1, phiSource + arcSpan1);
        ctx.stroke();

        // Image 2: Counter-image on opposite side
        const im2R = Math.abs(theta2) * 1.5;
        const oppPhi = phiSource + Math.PI;
        const arcSpan2 = Math.min(Math.PI * 0.5, (thetaE / (beta + 1e-3)) * 0.2);

        ctx.strokeStyle = "#60a5fa"; ctx.lineWidth = Math.min(6, 1.5 + Math.log10(mu2) * 2);
        ctx.shadowColor = "#60a5fa"; ctx.shadowBlur = 8;
        ctx.beginPath();
        ctx.arc(cx, cy, im2R, oppPhi - arcSpan2, oppPhi + arcSpan2);
        ctx.stroke();
        ctx.shadowBlur = 0;
      }

      // Right Panel: Lensing Optics Telemetry
      const rx = 430, ry = 35, rw = 305, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Gravitational Lens Equation Solver", rx + 15, ry + 22);

      const items = [
        ["Einstein Radius θ_E:", `${thetaE}"`],
        ["Source Offset β = √(βx²+βy²):", `${beta.toFixed(1)}"`],
        ["Primary Image θ₊:", `+${theta1.toFixed(1)}"`],
        ["Secondary Image θ₋:", `${theta2.toFixed(1)}"`],
        ["Primary Magnification μ₊:", `${mu1.toFixed(2)} ×`],
        ["Secondary Magnification μ₋:", `${mu2.toFixed(2)} ×`],
        ["Total Flux Amplification μ_tot:", `${totalMu.toFixed(2)} × (${(2.5 * Math.log10(totalMu)).toFixed(2)} mag)`]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx + 12, ry + 55 + idx * 28);
        ctx.fillStyle = idx === 6 ? "#fbbf24" : (idx === 0 ? "#facc15" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx + 12, ry + 70 + idx * 28);
        ctx.font = "11px Inter";
      });

      // Equation
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Lens Equation: β = θ - θ_E² / θ", rx + 12, ry + 275);
      ctx.fillText("As β ➔ 0: Images merge into perfect Einstein ring.", rx + 12, ry + 295);
    }
  },
  // =========================================================================
  // CHAPTER 7: COSMIC EXPANSION & RELATIVISTIC COSMOLOGY
  // =========================================================================

  // 13. Expanding Metric Cosmological Grid & Hubble Redshift Flow
  "astro-hubble-expansion-sim": {
    title: "Metric Space Expansion & Hubble Redshift Flow",
    desc: "2D uniform cosmological metric expansion demonstrating Hubble-Lemaître law v = H₀ d, cosmological redshift 1 + z = a₀ / a(t), and observer frame invariance across cosmic grid.",
    isAnimated: true,
    controls: [
      { id: "hubbleH0", label: "Hubble Constant H₀ (km/s/Mpc)", min: 50, max: 90, step: 1, value: 70 },
      { id: "scaleFactor", label: "Scale Factor a(t)", min: 0.5, max: 1.8, step: 0.05, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const H0 = vals.hubbleH0 !== undefined ? vals.hubbleH0 : 70;
      const baseScale = vals.scaleFactor !== undefined ? vals.scaleFactor : 1.0;
      // dynamic expansion with breathing
      const a_t = baseScale * (1 + 0.15 * Math.sin(time * 0.4));

      // Left Panel: Expanding Grid of Galaxies
      const cx = 200, cy = 200;
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("2D Expanding Robertson-Walker Metric Grid", 25, 25);

      // Metric grid lines
      ctx.strokeStyle = "rgba(51, 65, 85, 0.4)"; ctx.lineWidth = 1;
      const gridSize = 32 * a_t;
      for (let x = cx % gridSize; x < 400; x += gridSize) {
        ctx.beginPath(); ctx.moveTo(x, 40); ctx.lineTo(x, 360); ctx.stroke();
      }
      for (let y = cy % gridSize; y < 360; y += gridSize) {
        ctx.beginPath(); ctx.moveTo(20, y); ctx.lineTo(380, y); ctx.stroke();
      }

      // Central Observer Galaxy
      ctx.fillStyle = "#10b981"; ctx.shadowColor = "#10b981"; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(cx, cy, 7, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;
      ctx.fillStyle = "#a7f3d0"; ctx.font = "bold 10px Inter";
      ctx.fillText("Observer (v=0)", cx - 35, cy + 18);

      // Surrounding galaxies receding
      for (let gx = -3; gx <= 3; gx++) {
        for (let gy = -3; gy <= 3; gy++) {
          if (gx === 0 && gy === 0) continue;
          const px = cx + gx * gridSize;
          const py = cy + gy * gridSize;
          if (px < 30 || px > 370 || py < 45 || py > 355) continue;

          const comovDist = Math.hypot(gx, gy);
          const physDistMpc = comovDist * 15 * a_t;
          const recVel = H0 * physDistMpc;
          const z_redshift = recVel / 3e5; // v / c

          // Velocity vector
          const vLen = Math.min(22, recVel * 0.015);
          const ang = Math.atan2(py - cy, px - cx);
          ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.moveTo(px, py);
          ctx.lineTo(px + Math.cos(ang) * vLen, py + Math.sin(ang) * vLen);
          ctx.stroke();

          // Galaxy dot
          ctx.fillStyle = "#fbbf24";
          ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Right Panel: Hubble Diagram v vs d
      const hx = 420, hy = 35, hw = 315, hh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(hx, hy, hw, hh); ctx.strokeRect(hx, hy, hw, hh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Hubble-Lemaître Law v = H₀ d", hx + 15, hy + 22);

      const ox = hx + 50, oy = hy + 175, pw = hw - 70, ph = 120;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Proper Distance d (Mpc)", ox + pw - 120, oy + 18);
      ctx.save(); ctx.translate(ox - 30, oy - 30); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Recession v (km/s)", 0, 0); ctx.restore();

      // Hubble slope line
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.beginPath();
      ctx.moveTo(ox, oy);
      ctx.lineTo(ox + pw, oy - ph);
      ctx.stroke();

      // Plotted galaxy points
      for (let i = 1; i <= 8; i++) {
        const d_mpc = i * 10;
        const v_k = H0 * d_mpc;
        const px = ox + (d_mpc / 80) * pw;
        const py = oy - (v_k / (H0 * 80)) * ph;
        ctx.fillStyle = "#fbbf24";
        ctx.beginPath(); ctx.arc(px, py, 3.5, 0, Math.PI * 2); ctx.fill();
      }

      // Telemetry Box
      const by = hy + 200;
      const redshift = (1 / a_t) - 1;

      const items = [
        ["Hubble Constant H₀:", `${H0} km/s/Mpc`],
        ["Scale Factor a(t):", `${a_t.toFixed(3)} (Current epoch = 1.0)`],
        ["Cosmological Redshift z = 1/a - 1:", `${redshift > 0 ? "+" : ""}${redshift.toFixed(3)}`],
        ["Wavelength Stretching:", `λ_obs = (1 + z) λ_emit = ${(1 + redshift).toFixed(2)} λ₀`],
        ["Hubble Time t_H = 1/H₀:", `${(977.8 / H0).toFixed(1)} Gyr`]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], hx + 12, by + 18 + idx * 24);
        ctx.fillStyle = idx === 2 ? (redshift > 0 ? "#f43f5e" : "#38bdf8") : "#f1f5f9";
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], hx + 185, by + 18 + idx * 24);
        ctx.font = "11px Inter";
      });
    }
  },
  // 14. Friedmann Universe Scale Factor Integrator a(t)
  "astro-friedmann-universe-sim": {
    title: "Multi-Component Friedmann Equation Integrator a(t)",
    desc: "Numerical integration of (ȧ/a)² = H₀² [Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_k a⁻² + Ω_Λ] comparing Big Bang, deceleration-to-acceleration transition, and cosmological fates.",
    isAnimated: true,
    controls: [
      { id: "omegaM", label: "Matter Density Ω_m,0", min: 0.0, max: 1.0, step: 0.05, value: 0.31 },
      { id: "omegaLambda", label: "Dark Energy Ω_Λ,0", min: 0.0, max: 1.4, step: 0.05, value: 0.69 },
      { id: "hubbleParam", label: "Hubble Constant H₀", min: 60, max: 80, step: 1, value: 70 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const Om = vals.omegaM !== undefined ? vals.omegaM : 0.31;
      const OL = vals.omegaLambda !== undefined ? vals.omegaLambda : 0.69;
      const H0 = vals.hubbleParam !== undefined ? vals.hubbleParam : 70;

      const Ok = 1.0 - Om - OL;
      // Deceleration parameter q0 = 0.5 * Om - OL
      const q0 = 0.5 * Om - OL;
      const isAccelerating = q0 < 0;

      // Transition redshift where acceleration begins: z_trans = (2 OL / Om)^(1/3) - 1
      const z_trans = Om > 0.01 && OL > 0 ? Math.pow((2 * OL) / Om, 1/3) - 1 : null;

      // Left Panel: Scale Factor Trajectory a(t)
      const gx = 45, gy = 35, gw = 430, gh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Cosmic Scale Factor Evolution a(t) vs Cosmic Time", gx + 15, gy + 22);

      const ox = gx + 50, oy = gy + gh - 45, pw = gw - 70, ph = gh - 75;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Cosmic Time t (Gyr)", ox + pw - 110, oy + 18);
      ctx.save(); ctx.translate(ox - 30, oy - 45); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Scale Factor a(t)", 0, 0); ctx.restore();

      // Current epoch marker (t_0 ~ 13.8 Gyr, a = 1.0)
      const t0_x = ox + (13.8 / 30.0) * pw;
      const a1_y = oy - (1.0 / 2.2) * ph;
      ctx.strokeStyle = "#64748b"; ctx.lineWidth = 1; ctx.setLineDash([2, 2]);
      ctx.beginPath(); ctx.moveTo(t0_x, oy); ctx.lineTo(t0_x, oy - ph); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ox, a1_y); ctx.lineTo(ox + pw, a1_y); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#94a3b8"; ctx.fillText("t₀ (13.8 Gyr)", t0_x - 30, oy + 14);
      ctx.fillText("a = 1.0", ox - 35, a1_y + 4);

      // Integrate a(t) using Euler/RK approximation
      // dt / da = 1 / [ a * H0 * sqrt(Om/a^3 + Ok/a^2 + OL) ]
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let t = 0; t <= 30; t += 0.2) {
        // Approximate LCDM scale factor: a(t) ~ (Om / OL)^(1/3) * sinh^(2/3)(1.5 * sqrt(OL) * H0 * t)
        let a_calc = 0;
        if (OL > 0.05 && Om > 0.05) {
          const arg = 1.5 * Math.sqrt(OL) * (H0 / 977.8) * t;
          a_calc = Math.pow(Om / OL, 1/3) * Math.pow(Math.sinh(arg), 2/3);
        } else {
          // Einstein-de Sitter (Om=1, OL=0)
          a_calc = Math.pow((1.5 * (H0 / 977.8) * t), 2/3);
        }
        const px = ox + (t / 30.0) * pw;
        const py = oy - (Math.min(2.2, a_calc) / 2.2) * ph;
        if (t === 0) ctx.moveTo(px, oy); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current point (t0, 1.0)
      ctx.fillStyle = "#f59e0b"; ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(t0_x, a1_y, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Right Panel: Cosmological Fate & Parameters
      const rx = 490, ry = 35, rw = 245, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Cosmological Parameters", rx + 15, ry + 22);

      const items = [
        ["Matter Density Ω_m:", `${Om.toFixed(2)}`],
        ["Dark Energy Ω_Λ:", `${OL.toFixed(2)}`],
        ["Curvature Density Ω_k:", `${Ok.toFixed(2)} (${Math.abs(Ok) < 0.02 ? "Spatially Flat" : (Ok < 0 ? "Closed (k=+1)" : "Open (k=-1)")})`],
        ["Deceleration Param q₀:", `${q0.toFixed(2)} (${isAccelerating ? "ACCELERATING" : "DECELERATING"})`],
        ["Transition Redshift z_t:", z_trans && z_trans > 0 ? `${z_trans.toFixed(2)}` : "None"],
        ["Ultimate Cosmic Fate:", OL > 0 ? "EXPONENTIAL EXPANSION (Big Freeze)" : (Om > 1 ? "RECOLLAPSE (Big Crunch)" : "ETERNAL EXPANSION")]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx + 12, ry + 55 + idx * 28);
        ctx.fillStyle = idx === 3 ? (isAccelerating ? "#10b981" : "#ef4444") : (idx === 5 ? "#38bdf8" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx + 12, ry + 70 + idx * 28);
        ctx.font = "11px Inter";
      });

      // Friedmann formula
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("H²(a) = H₀² [Ω_m a⁻³ + Ω_k a⁻² + Ω_Λ]", rx + 12, ry + 275);
    }
  },
  // =========================================================================
  // CHAPTER 8: THE EARLY UNIVERSE & ASTROBIOLOGY
  // =========================================================================

  // 15. Primordial Big Bang Nucleosynthesis (BBN) Freeze-Out
  "astro-bbn-nucleosynthesis-sim": {
    title: "Big Bang Nucleosynthesis (BBN) Abundance Engine",
    desc: "Weak interaction freeze-out (n/p ~ e^(-Δm/kT) ~ 1/6) followed by neutron decay through the deuterium bottleneck, yielding primordial ⁴He (Y_p ~ 0.245), D/H, ³He, and ⁷Li vs baryon density η.",
    isAnimated: true,
    controls: [
      { id: "baryonDensity", label: "Baryon-to-Photon η₁₀ = 10¹⁰ η", min: 2.0, max: 9.0, step: 0.2, value: 6.1 },
      { id: "neutrinoFlavors", label: "Neutrino Species N_ν", min: 2.0, max: 4.0, step: 0.2, value: 3.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const eta10 = vals.baryonDensity !== undefined ? vals.baryonDensity : 6.1;
      const Nnu = vals.neutrinoFlavors !== undefined ? vals.neutrinoFlavors : 3.0;

      // Primordial 4He mass fraction Y_p:
      // Y_p ~ 0.247 + 0.013 * (Nnu - 3) + 0.010 * ln(eta10 / 6)
      const Yp = 0.247 + 0.013 * (Nnu - 3.0) + 0.010 * Math.log(eta10 / 6.0);

      // Deuterium abundance (D/H):
      // (D/H) ~ 2.5e-5 * (eta10 / 6)^(-1.6)
      const d_over_h = 2.5e-5 * Math.pow(eta10 / 6.0, -1.6);

      // Helium-3:
      const he3_over_h = 1.0e-5 * Math.pow(eta10 / 6.0, -0.6);

      // Lithium-7 (the cosmological lithium problem valley):
      const li7_over_h = 4.8e-10 * Math.pow(eta10 / 6.0, 2.0);

      // Left Panel: Schramm BBN Plot log(Abundance) vs eta
      const gx = 45, gy = 35, gw = 430, gh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Primordial Light Element Abundances vs Baryon Density η", gx + 15, gy + 22);

      const ox = gx + 55, oy = gy + gh - 45, pw = gw - 75, ph = gh - 75;
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(ox, oy - ph); ctx.lineTo(ox, oy); ctx.lineTo(ox + pw, oy); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
      ctx.fillText("Baryon Density η₁₀ = 10¹⁰ (n_b / n_γ)", ox + pw - 180, oy + 20);
      ctx.save(); ctx.translate(ox - 35, oy - 45); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Primordial Mass Fraction / Ratio", 0, 0); ctx.restore();

      // CMB concordance vertical band at eta10 = 6.1 +/- 0.2
      const cmbX = ox + ((6.1 - 2.0) / 7.0) * pw;
      ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
      ctx.fillRect(cmbX - 8, oy - ph, 16, ph);
      ctx.fillStyle = "#10b981"; ctx.font = "9px Inter";
      ctx.fillText("Planck CMB", cmbX - 25, oy - ph + 12);

      // Plot 1: 4He mass fraction Yp (~ 0.24 - 0.26)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let e = 2.0; e <= 9.0; e += 0.2) {
        const curYp = 0.247 + 0.013 * (Nnu - 3.0) + 0.010 * Math.log(e / 6.0);
        const px = ox + ((e - 2.0) / 7.0) * pw;
        const py = oy - (0.6 + (curYp - 0.2) * 2.0) * ph;
        if (e === 2.0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot 2: D/H (steep falloff)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.beginPath();
      for (let e = 2.0; e <= 9.0; e += 0.2) {
        const curDh = 2.5e-5 * Math.pow(e / 6.0, -1.6);
        const px = ox + ((e - 2.0) / 7.0) * pw;
        const logVal = Math.log10(curDh); // -4 to -5.5
        const py = oy - ((logVal + 6) / 4) * ph * 0.7;
        if (e === 2.0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot 3: 7Li/H (trough then rise)
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 1.8; ctx.beginPath();
      for (let e = 2.0; e <= 9.0; e += 0.2) {
        const curLi = 4.8e-10 * Math.pow(e / 6.0, 2.0);
        const px = ox + ((e - 2.0) / 7.0) * pw;
        const logVal = Math.log10(curLi);
        const py = oy - ((logVal + 11) / 5) * ph * 0.45;
        if (e === 2.0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Legend
      ctx.font = "10px Inter";
      ctx.fillStyle = "#38bdf8"; ctx.fillText("— ⁴He (Y_p)", ox + 15, gy + 45);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("— D / H", ox + 95, gy + 45);
      ctx.fillStyle = "#f43f5e"; ctx.fillText("— ⁷Li / H", ox + 165, gy + 45);

      // Current η point marker
      const curX = ox + ((eta10 - 2.0) / 7.0) * pw;
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1; ctx.setLineDash([3, 2]);
      ctx.beginPath(); ctx.moveTo(curX, oy); ctx.lineTo(curX, oy - ph); ctx.stroke();
      ctx.setLineDash([]);

      // Right Panel: Nuclear Yield Telemetry
      const rx = 490, ry = 35, rw = 245, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Primordial Nucleosynthesis Yields", rx + 15, ry + 22);

      const items = [
        ["Selected η₁₀:", `${eta10.toFixed(2)}`],
        ["Neutrino Species N_ν:", `${Nnu.toFixed(1)}`],
        ["⁴He Mass Fraction Y_p:", `${Yp.toFixed(4)} (24.7%)`],
        ["Deuterium D/H:", `${d_over_h.toExponential(2)}`],
        ["Helium-3 ³He/H:", `${he3_over_h.toExponential(2)}`],
        ["Lithium-7 ⁷Li/H:", `${li7_over_h.toExponential(2)}`],
        ["Baryon Density Ω_b h²:", `${(eta10 * 0.00365).toFixed(4)}`]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx + 12, ry + 55 + idx * 28);
        ctx.fillStyle = idx === 2 ? "#38bdf8" : (idx === 3 ? "#f59e0b" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx + 12, ry + 70 + idx * 28);
        ctx.font = "11px Inter";
      });

      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Deuterium is pristine cosmological baryometer", rx + 12, ry + 280);
      ctx.fillText("because all stars exclusively destroy it.", rx + 12, ry + 295);
    }
  },
  // 16. Circumstellar Habitable Zone & Drake Equation
  "astro-drake-habitable-sim": {
    title: "Circumstellar Habitable Zone & Drake Equation Calculator",
    desc: "Interactive planetary system habitable zone calculator (r_in = 0.95 √(L/L⊙) AU, r_out = 1.67 √(L/L⊙) AU) coupled to the Drake equation for communicating galactic civilizations N.",
    isAnimated: true,
    controls: [
      { id: "starLum", label: "Stellar Luminosity L (L⊙)", min: 0.1, max: 5.0, step: 0.1, value: 1.0 },
      { id: "planetDist", label: "Planet Orbit d (AU)", min: 0.2, max: 3.5, step: 0.05, value: 1.0 },
      { id: "civLifetime", label: "Civilization Lifetime L (years)", min: 100, max: 100000, step: 500, value: 10000 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const L = vals.starLum !== undefined ? vals.starLum : 1.0;
      const d = vals.planetDist !== undefined ? vals.planetDist : 1.0;
      const L_civ = vals.civLifetime !== undefined ? vals.civLifetime : 10000;

      // Habitable zone boundaries: r ~ sqrt(L)
      const r_in = 0.95 * Math.sqrt(L);  // Runaway greenhouse
      const r_out = 1.67 * Math.sqrt(L); // Maximum greenhouse

      // Planet equilibrium temperature: Teq = 278 * (L)^(1/4) / sqrt(d) (assuming albedo 0.3)
      const Teq = 278 * Math.pow(L, 0.25) / Math.sqrt(d);
      const isHabitable = d >= r_in && d <= r_out;

      // Drake Equation: N = R* * fp * ne * fl * fi * fc * L
      // Standard fiducial values: R*=2, fp=0.8, ne=0.5, fl=0.3, fi=0.1, fc=0.1
      const N_civ = Math.round(2.0 * 0.8 * 0.5 * 0.3 * 0.1 * 0.1 * L_civ);

      // Left Panel: Planetary System Habitable Zone
      const cx = 175, cy = 200;
      const scaleAU = 55; // pixels per AU

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 13px Inter";
      ctx.fillText("Planetary System & Circumstellar Habitable Zone", 25, 25);

      // Scorched Zone (too hot)
      ctx.fillStyle = "rgba(239, 68, 68, 0.15)";
      ctx.beginPath(); ctx.arc(cx, cy, r_in * scaleAU, 0, Math.PI * 2); ctx.fill();

      // Habitable Zone (Green Ring)
      ctx.strokeStyle = "rgba(16, 185, 129, 0.5)"; ctx.lineWidth = (r_out - r_in) * scaleAU;
      ctx.beginPath();
      ctx.arc(cx, cy, (r_in + r_out) * 0.5 * scaleAU, 0, Math.PI * 2);
      ctx.stroke();

      // Outer Frozen Zone (blue dash)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.3)"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, r_out * scaleAU + 35, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      // Central Host Star
      const starGrad = ctx.createRadialGradient(cx, cy, 2, cx, cy, 18);
      starGrad.addColorStop(0, "#ffffff");
      starGrad.addColorStop(0.5, "#fbbf24");
      starGrad.addColorStop(1, "#f97316");
      ctx.fillStyle = starGrad; ctx.shadowColor = "#f59e0b"; ctx.shadowBlur = 12;
      ctx.beginPath(); ctx.arc(cx, cy, 12 * Math.pow(L, 0.3), 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      // Orbiting Planet
      const orbPeriod = Math.pow(d, 1.5) * 3; // Keplers 3rd law
      const pAng = (time / orbPeriod) * Math.PI * 2;
      const px = cx + d * scaleAU * Math.cos(pAng);
      const py = cy + d * scaleAU * Math.sin(pAng);

      // Orbit circle
      ctx.strokeStyle = isHabitable ? "#10b981" : "#64748b"; ctx.lineWidth = 1; ctx.setLineDash([2, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, d * scaleAU, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      // Planet body
      ctx.fillStyle = isHabitable ? "#38bdf8" : (d < r_in ? "#ef4444" : "#93c5fd");
      ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 8;
      ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px Inter";
      ctx.fillText(`Planet (${d.toFixed(2)} AU)`, px + 9, py - 4);

      // Right Panel: Astrobiology & Drake Engine Telemetry
      const rx = 390, ry = 35, rw = 345, rh = 335;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(rx, ry, rw, rh); ctx.strokeRect(rx, ry, rw, rh);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter";
      ctx.fillText("Habitability & Drake Equation Calculation", rx + 15, ry + 22);

      const items = [
        ["Host Star Luminosity L:", `${L.toFixed(2)} L⊙`],
        ["Habitable Zone Inner Edge r_in:", `${r_in.toFixed(2)} AU (Runaway Greenhouse)`],
        ["Habitable Zone Outer Edge r_out:", `${r_out.toFixed(2)} AU (Maximum Greenhouse)`],
        ["Planet Equilibrium Temp Teq:", `${Math.round(Teq)} K (${Math.round(Teq - 273.15)} °C)`],
        ["Habitability Status:", isHabitable ? "POTENTIALLY HABITABLE (Liquid H₂O Stable)" : (d < r_in ? "TOO HOT (Runaway Greenhouse)" : "TOO COLD (Global Glaciation)")],
        ["Civilization Lifetime L:", `${L_civ.toLocaleString()} years`],
        ["Drake Communicating Civilizations N:", `${N_civ.toLocaleString()} civilizations in Milky Way`]
      ];

      ctx.font = "11px Inter";
      items.forEach((it, idx) => {
        ctx.fillStyle = "#94a3b8"; ctx.fillText(it[0], rx + 12, ry + 52 + idx * 28);
        ctx.fillStyle = idx === 4 ? (isHabitable ? "#10b981" : "#ef4444") : (idx === 6 ? "#fbbf24" : "#f1f5f9");
        ctx.font = "bold 11px Inter"; ctx.fillText(it[1], rx + 12, ry + 66 + idx * 28);
        ctx.font = "11px Inter";
      });

      // Drake equation summary
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("Drake Equation: N = R* × fp × ne × fl × fi × fc × L", rx + 12, ry + 275);
      ctx.fillText("If L ~ 10,000 yr, hundreds of communicating civilizations coexist.", rx + 12, ry + 295);
    }
  }
};

// Simulation Engine Adapter for Open STEM Library App Controller
window.SimulationEngine = window.SimulationEngine || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = "";

  const simConfig = (window.ASTRO_SIMS && window.ASTRO_SIMS[simType]) ||
                    (window.QM2_SIMS && window.QM2_SIMS[simType]) ||
                    (window.DIG_SIMS && window.DIG_SIMS[simType]) ||
                    (window.NUC_SIMS && window.NUC_SIMS[simType]);

  if (!simConfig) {
    container.innerHTML = `<div style="padding: 1rem; color: #ef4444; background: #1e1b4b; border-radius: 8px;">Simulation type '${simType}' not found in registry.</div>`;
    return;
  }

  if (window.SimulationEngine.activeAnimations && window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }
  window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

  const box = document.createElement("div");
  box.className = "simulation-box";
  box.style.background = "#0b1120";
  box.style.border = "1px solid #1e293b";
  box.style.borderRadius = "12px";
  box.style.padding = "1.25rem";
  box.style.marginTop = "1rem";
  box.style.marginBottom = "1.5rem";

  const header = document.createElement("div");
  header.style.marginBottom = "1rem";
  header.innerHTML = `
    <div style="display: flex; align-items: center; justify-content: space-between;">
      <h4 style="margin: 0; color: #38bdf8; font-size: 1.15rem; font-family: 'Space Grotesk', sans-serif;">${simConfig.title}</h4>
      <span style="font-size: 0.75rem; background: #1e293b; color: #94a3b8; padding: 0.2rem 0.5rem; border-radius: 4px; border: 1px solid #334155;">60 FPS Interactive</span>
    </div>
    <p style="margin: 0.4rem 0 0 0; color: #94a3b8; font-size: 0.85rem; line-height: 1.4;">${simConfig.desc}</p>
  `;
  box.appendChild(header);

  const canvas = document.createElement("canvas");
  canvas.width = 750;
  canvas.height = 390;
  canvas.style.width = "100%";
  canvas.style.maxWidth = "750px";
  canvas.style.height = "auto";
  canvas.style.aspectRatio = "750 / 390";
  canvas.style.background = "#050811";
  canvas.style.borderRadius = "8px";
  canvas.style.border = "1px solid #1e293b";
  canvas.style.display = "block";
  box.appendChild(canvas);

  const ctrlBar = document.createElement("div");
  ctrlBar.style.display = "flex";
  ctrlBar.style.flexWrap = "wrap";
  ctrlBar.style.gap = "1rem";
  ctrlBar.style.marginTop = "1rem";
  ctrlBar.style.alignItems = "center";

  const currentVals = {};

  if (simConfig.controls) {
    simConfig.controls.forEach(c => {
      currentVals[c.id] = c.value;
      const wrap = document.createElement("div");
      wrap.style.display = "flex";
      wrap.style.flexDirection = "column";
      wrap.style.gap = "0.25rem";

      const lbl = document.createElement("label");
      lbl.style.fontSize = "0.8rem";
      lbl.style.color = "#94a3b8";
      lbl.innerText = `${c.label}: ${c.value}`;

      const input = document.createElement("input");
      input.type = "range";
      input.min = c.min;
      input.max = c.max;
      input.step = c.step;
      input.value = c.value;
      input.style.accentColor = "#38bdf8";

      input.addEventListener("input", (e) => {
        const val = parseFloat(e.target.value);
        currentVals[c.id] = val;
        lbl.innerText = `${c.label}: ${val}`;
        if (!simConfig.isAnimated) {
          simConfig.render(canvas, currentVals, 0);
        }
      });

      wrap.appendChild(lbl);
      wrap.appendChild(input);
      ctrlBar.appendChild(wrap);
    });
  }

  if (simConfig.isAnimated) {
    const animCtrlWrap = document.createElement("div");
    animCtrlWrap.style.display = "flex";
    animCtrlWrap.style.alignItems = "flex-end";
    const pauseBtn = document.createElement("button");
    pauseBtn.innerText = "⏸️ Pause";
    pauseBtn.style.padding = "0.4rem 0.8rem";
    pauseBtn.style.background = "#1e293b";
    pauseBtn.style.color = "#38bdf8";
    pauseBtn.style.border = "1px solid #334155";
    pauseBtn.style.borderRadius = "6px";
    pauseBtn.style.cursor = "pointer";
    pauseBtn.style.fontSize = "0.85rem";

    let isPaused = false;
    pauseBtn.addEventListener("click", () => {
      isPaused = !isPaused;
      pauseBtn.innerText = isPaused ? "▶️ Play" : "⏸️ Pause";
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
