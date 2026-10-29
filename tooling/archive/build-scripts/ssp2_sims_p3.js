
  // =========================================================================
  // UNIT 5: PHENOMENOLOGICAL SUPERCONDUCTIVITY & VORTEX PHYSICS
  // =========================================================================

  // 9. Meissner Effect, London Penetration Depth & Screening Currents
  "ssp2-meissner-london-sim": {
    title: "Meissner Effect, London Screening & Penetration Depth λ_L(T)",
    desc: "Rigorous phenomenological electrodynamics solver for ∇²B = B/λ_L². Demonstrates exponential magnetic expulsion B(x) = B₀ exp(-x/λ_L), surface supercurrent J_s(x), and critical temperature divergence.",
    isAnimated: true,
    controls: [
      { id: "tempRatio", label: "Temperature T / T_c", min: 0.0, max: 1.15, step: 0.05, value: 0.4 },
      { id: "appliedB", label: "Applied Field B₀ (mT)", min: 10, max: 150, step: 10, value: 60 },
      { id: "lambdaZero", label: "London Depth λ₀ (nm)", min: 30, max: 120, step: 10, value: 50 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const tRatio = vals.tempRatio !== undefined ? vals.tempRatio : 0.4;
      const B0 = vals.appliedB !== undefined ? vals.appliedB : 60;
      const lambda0 = vals.lambdaZero !== undefined ? vals.lambdaZero : 50;

      // Two-fluid Gorter-Casimir temperature dependence:
      // lambda_L(T) = lambda_0 / sqrt(1 - (T/Tc)^4)
      const isSuper = tRatio < 1.0;
      let lambdaT = Infinity;
      if (isSuper) {
        const denom = Math.sqrt(Math.max(1e-4, 1 - Math.pow(tRatio, 4)));
        lambdaT = lambda0 / denom; // in nm
      }

      // Split canvas: Left is spatial slab profile B(x) & J_s(x); Right is λ_L(T) curve & B_c(T)
      const splitX = Math.floor(w * 0.52);

      // --- LEFT: SPATIAL EXPONENTIAL DECAY ---
      const plotL = { x: 45, y: 35, w: splitX - 65, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText("Magnetic Field Penetration B(x) = B₀ e^{-x/λ_L} & Supercurrent", plotL.x, plotL.y - 12);

      const slabStartX = plotL.x + Math.floor(plotL.w * 0.28);

      // Vacuum region (left of slab)
      ctx.fillStyle = "rgba(30, 41, 59, 0.3)";
      ctx.fillRect(plotL.x, plotL.y, slabStartX - plotL.x, plotL.h);
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter";
      ctx.fillText("VACUUM", plotL.x + 10, plotL.y + 20);

      // Superconductor slab (right of slabStartX)
      ctx.fillStyle = isSuper ? "rgba(16, 185, 129, 0.08)" : "rgba(239, 68, 68, 0.08)";
      ctx.fillRect(slabStartX, plotL.y, plotL.x + plotL.w - slabStartX, plotL.h);
      ctx.fillStyle = isSuper ? "#10b981" : "#ef4444"; ctx.font = "bold 10px Inter";
      ctx.fillText(isSuper ? "SUPERCONDUCTING SLAB" : "NORMAL STATE (T ≥ T_c)", slabStartX + 12, plotL.y + 20);

      // Slab interface line x = 0
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(slabStartX, plotL.y); ctx.lineTo(slabStartX, plotL.y + plotL.h); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "10px Inter"; ctx.fillText("x = 0", slabStartX - 14, plotL.y + plotL.h - 10);

      const midY = plotL.y + plotL.h * 0.55;
      const maxDist_nm = 300; // max depth on graph
      const slabW = plotL.x + plotL.w - slabStartX;

      // Plot B(x) profile
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      // In vacuum: B(x) = B0
      ctx.moveTo(plotL.x, midY - (B0 / 160) * (plotL.h * 0.4));
      ctx.lineTo(slabStartX, midY - (B0 / 160) * (plotL.h * 0.4));

      // Inside slab
      const xSteps = 60;
      for (let i = 0; i <= xSteps; i++) {
        const x_nm = (i / xSteps) * maxDist_nm;
        const bVal = isSuper ? B0 * Math.exp(-x_nm / lambdaT) : B0;
        const px = slabStartX + (x_nm / maxDist_nm) * slabW;
        const py = midY - (bVal / 160) * (plotL.h * 0.4);
        ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot London Penetration Depth λ_L marker line inside slab
      if (isSuper && lambdaT < maxDist_nm) {
        const lamPx = slabStartX + (lambdaT / maxDist_nm) * slabW;
        ctx.strokeStyle = "#f59e0b"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(lamPx, plotL.y + 35); ctx.lineTo(lamPx, plotL.y + plotL.h); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#f59e0b"; ctx.font = "10px Inter";
        ctx.fillText(`λ_L = ${lambdaT.toFixed(0)} nm (1/e point)`, lamPx + 4, plotL.y + 50);
      }

      // Draw surface screening current density J_s(x)
      if (isSuper) {
        ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.setLineDash([2, 2]); ctx.lineWidth = 1.8;
        for (let i = 0; i <= xSteps; i++) {
          const x_nm = (i / xSteps) * maxDist_nm;
          const jsVal = (B0 / Math.max(30, lambdaT)) * Math.exp(-x_nm / lambdaT); // arb units
          const px = slabStartX + (x_nm / maxDist_nm) * slabW;
          const py = midY + (jsVal * 60) * (plotL.h * 0.35);
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = "#a855f7"; ctx.font = "10px Inter";
        ctx.fillText("Screening Current J_s(x)", slabStartX + 15, midY + 35);
      }

      // --- RIGHT: λ_L(T) TEMPERATURE DIVERGENCE & PHASE DIAGRAM ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
      ctx.fillText("London Penetration Depth Divergence λ_L(T) → ∞ at T_c", plotR.x, plotR.y - 12);

      // Tc vertical asymptote
      const tcX = plotR.x + (1.0 / 1.15) * plotR.w;
      ctx.strokeStyle = "#ef4444"; ctx.setLineDash([3, 3]); ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(tcX, plotR.y); ctx.lineTo(tcX, plotR.y + plotR.h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.font = "10px Inter"; ctx.fillText("T = T_c", tcX - 16, plotR.y + 16);

      // Plot λ(T) curve
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.4;
      const tPts = 60;
      for (let i = 0; i <= tPts; i++) {
        const tr = (i / tPts) * 0.985;
        const lam = lambda0 / Math.sqrt(1 - Math.pow(tr, 4));
        const px = plotR.x + (tr / 1.15) * plotR.w;
        const py = plotR.y + plotR.h - (lam / 280) * (plotR.h * 0.8) - 15;
        const clampedPy = Math.max(plotR.y + 10, py);
        if (i === 0) ctx.moveTo(px, clampedPy); else ctx.lineTo(px, clampedPy);
      }
      ctx.stroke();

      // Current operational dot
      if (isSuper && lambdaT < 300) {
        const curPx = plotR.x + (tRatio / 1.15) * plotR.w;
        const curPy = plotR.y + plotR.h - (lambdaT / 280) * (plotR.h * 0.8) - 15;
        ctx.beginPath(); ctx.arc(curPx, Math.max(plotR.y + 10, curPy), 6, 0, 2 * Math.PI);
        ctx.fillStyle = "#38bdf8"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();
      }

      // Telemetry Box
      const tBoxY = plotR.y + plotR.h - 60;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, tBoxY, plotR.w - 20, 52);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, tBoxY, plotR.w - 20, 52);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Applied B₀ = ${B0} mT  |  λ₀ = ${lambda0} nm`, plotR.x + 18, tBoxY + 18);
      ctx.fillStyle = isSuper ? "#10b981" : "#ef4444"; ctx.font = "bold 11px Inter";
      ctx.fillText(isSuper ? `MEISSNER STATE: λ_L(T) = ${lambdaT.toFixed(1)} nm` : "NORMAL STATE: Perfect Flux Penetration (B = B₀)", plotR.x + 18, tBoxY + 36);
    }
  },

  // 10. Abrikosov Vortex Lattice & Type-II Mixed State
  "ssp2-abrikosov-vortex-sim": {
    title: "Abrikosov Flux Lattice, Vortex Cores & Type-II Phase Diagram",
    desc: "Simulates triangular Abrikosov vortex lattice in Type-II superconductors. Renders 2D circulating supercurrent streamlines, normal cores of radius ξ, magnetic flux quanta Φ₀ = h/2e, and H_c1–H_c2 phase bounds.",
    isAnimated: true,
    controls: [
      { id: "glKappa", label: "GL Parameter κ = λ/ξ", min: 1.0, max: 15.0, step: 0.5, value: 5.0 },
      { id: "fieldH", label: "Applied Field H / H_c2", min: 0.05, max: 0.95, step: 0.05, value: 0.35 },
      { id: "coherenceXi", label: "Coherence Length ξ (nm)", min: 2.0, max: 12.0, step: 1.0, value: 5.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const kappa = vals.glKappa !== undefined ? vals.glKappa : 5.0;
      const hRatio = vals.fieldH !== undefined ? vals.fieldH : 0.35;
      const xi = vals.coherenceXi !== undefined ? vals.coherenceXi : 5.0;
      const lambda = kappa * xi;

      // Critical fields in normalized units:
      // Hc1 / Hc = ln(kappa) / (sqrt(2) * kappa)
      // Hc2 / Hc = sqrt(2) * kappa
      // Hence Hc1 / Hc2 = ln(kappa) / (2 * kappa^2)
      const Hc1_Hc2 = Math.log(kappa) / (2 * kappa * kappa);
      const isMeissner = hRatio < Hc1_Hc2;

      // Triangular lattice constant a_tri = 1.075 * sqrt(Phi0 / B)
      // Number of vortices scales with field
      const vortexDensity = Math.max(1, Math.round(4 + hRatio * 18));

      // Split canvas: Left is 2D Abrikosov Lattice; Right is Phase Diagram & Vortex Profile
      const splitX = Math.floor(w * 0.52);

      // --- LEFT: 2D ABRIKOSOV LATTICE CANVAS ---
      const plotL = { x: 35, y: 35, w: splitX - 55, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotL.x, plotL.y, plotL.w, plotL.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
      ctx.fillText(`Abrikosov Vortex Lattice (Φ₀ = 2.07 × 10⁻¹⁵ Wb each)`, plotL.x, plotL.y - 12);

      if (isMeissner) {
        // Pure Meissner state (H < Hc1)
        ctx.fillStyle = "rgba(16, 185, 129, 0.1)";
        ctx.fillRect(plotL.x + 10, plotL.y + 10, plotL.w - 20, plotL.h - 20);
        ctx.fillStyle = "#10b981"; ctx.font = "bold 14px Inter";
        ctx.fillText("MEISSNER STATE (H < H_c1)", plotL.x + plotL.w * 0.25, plotL.y + plotL.h * 0.45);
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
        ctx.fillText("All magnetic flux completely expelled from the bulk.", plotL.x + plotL.w * 0.2, plotL.y + plotL.h * 0.52);
      } else {
        // Mixed Shubnikov State: Render triangular lattice
        const spacing = Math.max(35, 110 / Math.sqrt(vortexDensity));
        const rowH = spacing * Math.sqrt(3) / 2;
        const coreRad = Math.max(3, Math.min(12, (xi / 5.0) * 5));
        const penRad = Math.max(12, Math.min(35, (lambda / 25.0) * 18));

        // Clip to plotL
        ctx.save();
        ctx.beginPath(); ctx.rect(plotL.x, plotL.y, plotL.w, plotL.h); ctx.clip();

        // Loop over hexagonal grid
        let rowIdx = 0;
        for (let gy = plotL.y + 20; gy < plotL.y + plotL.h + spacing; gy += rowH) {
          const offsetX = (rowIdx % 2 === 0) ? 0 : spacing * 0.5;
          for (let gx = plotL.x + 20 + offsetX; gx < plotL.x + plotL.w + spacing; gx += spacing) {
            // Superconducting screening current loops
            ctx.strokeStyle = "rgba(56, 189, 248, 0.35)"; ctx.lineWidth = 1.0;
            ctx.beginPath(); ctx.arc(gx, gy, penRad, 0, 2 * Math.PI); ctx.stroke();

            // Magnetic field halo (Gaussian gradient)
            const radGrad = ctx.createRadialGradient(gx, gy, 0, gx, gy, penRad);
            radGrad.addColorStop(0, "rgba(245, 158, 11, 0.8)");
            radGrad.addColorStop(0.3, "rgba(245, 158, 11, 0.3)");
            radGrad.addColorStop(1, "rgba(245, 158, 11, 0.0)");
            ctx.fillStyle = radGrad;
            ctx.beginPath(); ctx.arc(gx, gy, penRad, 0, 2 * Math.PI); ctx.fill();

            // Normal Core (order parameter |ψ| → 0)
            ctx.fillStyle = "#ef4444";
            ctx.beginPath(); ctx.arc(gx, gy, coreRad, 0, 2 * Math.PI); ctx.fill();

            // Animated circulating current arrows
            const phaseAng = time * 2.5 + (gx + gy) * 0.05;
            const ax = gx + penRad * Math.cos(phaseAng);
            const ay = gy + penRad * Math.sin(phaseAng);
            ctx.fillStyle = "#38bdf8";
            ctx.beginPath(); ctx.arc(ax, ay, 2, 0, 2 * Math.PI); ctx.fill();
          }
          rowIdx++;
        }
        ctx.restore();
      }

      // --- RIGHT: PHASE DIAGRAM & VORTEX FIELD PROFILE ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
      ctx.fillText("Type-II H-T Phase Diagram & Core Profile", plotR.x, plotR.y - 12);

      // Phase diagram sub-plot (top half of plotR)
      const pdH = Math.floor(plotR.h * 0.48);
      ctx.fillStyle = "rgba(15, 23, 42, 0.6)"; ctx.fillRect(plotR.x + 15, plotR.y + 15, plotR.w - 30, pdH);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 15, plotR.y + 15, plotR.w - 30, pdH);

      // Boundaries Hc1 and Hc2
      const pdW = plotR.w - 30;
      // Hc2 curve: parabolic drop to 0 at Tc
      ctx.beginPath(); ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2;
      for (let i = 0; i <= 40; i++) {
        const tr = i / 40;
        const hc2 = 1.0 * (1 - tr * tr);
        const px = plotR.x + 15 + tr * pdW;
        const py = plotR.y + 15 + pdH * (1 - hc2);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Hc1 curve
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      for (let i = 0; i <= 40; i++) {
        const tr = i / 40;
        const hc1 = Hc1_Hc2 * (1 - tr * tr);
        const px = plotR.x + 15 + tr * pdW;
        const py = plotR.y + 15 + pdH * (1 - hc1);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current operational operating dot on phase diagram
      const curTr = 0.4;
      const opPx = plotR.x + 15 + curTr * pdW;
      const opPy = plotR.y + 15 + pdH * (1 - hRatio);
      ctx.beginPath(); ctx.arc(opPx, opPy, 5, 0, 2 * Math.PI);
      ctx.fillStyle = isMeissner ? "#10b981" : "#f59e0b"; ctx.fill();
      ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      ctx.fillStyle = "#10b981"; ctx.font = "9px Inter"; ctx.fillText("Meissner (H < H_c1)", plotR.x + 25, plotR.y + 15 + pdH - 8);
      ctx.fillStyle = "#f59e0b"; ctx.fillText("Mixed / Vortex State", plotR.x + 25, plotR.y + 15 + pdH * 0.45);
      ctx.fillStyle = "#ef4444"; ctx.fillText("Normal State (H > H_c2)", plotR.x + pdW * 0.4, plotR.y + 30);

      // Telemetry Box at bottom of plotR
      const tBoxY = plotR.y + pdH + 25;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 15, tBoxY, plotR.w - 30, plotR.h - pdH - 35);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 15, tBoxY, plotR.w - 30, plotR.h - pdH - 35);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`κ = λ/ξ = ${kappa.toFixed(1)}  (Type-II: κ > 1/√2 ≈ 0.707)`, plotR.x + 25, tBoxY + 20);
      ctx.fillText(`Coherence ξ = ${xi} nm  |  Penetration λ = ${lambda.toFixed(0)} nm`, plotR.x + 25, tBoxY + 38);
      ctx.fillStyle = isMeissner ? "#10b981" : "#f59e0b"; ctx.font = "bold 11px Inter";
      ctx.fillText(isMeissner ? "STATE: Pure Diamagnetic Meissner Expulsion" : `STATE: Abrikosov Triangular Flux Lattice (H/H_c2 = ${hRatio.toFixed(2)})`, plotR.x + 25, tBoxY + 56);
    }
  },

  // =========================================================================
  // UNIT 6: MICROSCOPIC BCS THEORY & JOSEPHSON PHENOMENA
  // =========================================================================

  // 11. BCS Energy Gap Δ(T), Quasiparticle DOS & Giaever Tunneling
  "ssp2-bcs-gap-sim": {
    title: "BCS Energy Gap Δ(T), Quasiparticle DOS & Giaever Tunneling",
    desc: "Solves BCS gap equation Δ(T)/Δ(0) ≈ 1.74√(1 - T/T_c). Displays quasiparticle density of states N_s(E) = N(0)|E|/√(E² - Δ²) and differential conductance dI/dV in Giaever S-I-N junctions.",
    isAnimated: true,
    controls: [
      { id: "tempRatio", label: "Reduced Temp T / T_c", min: 0.05, max: 0.98, step: 0.05, value: 0.35 },
      { id: "gapZero", label: "Zero-Temp Gap Δ(0) (meV)", min: 1.0, max: 4.5, step: 0.5, value: 2.5 },
      { id: "broadening", label: "Dynorphin Damping Γ (meV)", min: 0.02, max: 0.25, step: 0.02, value: 0.06 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const tRatio = vals.tempRatio !== undefined ? vals.tempRatio : 0.35;
      const delta0 = vals.gapZero !== undefined ? vals.gapZero : 2.5;
      const gamma = vals.broadening !== undefined ? vals.broadening : 0.06;

      // BCS temperature dependence approximation:
      // Delta(T) / Delta(0) ≈ tanh( 1.74 * sqrt(Tc/T - 1) )
      const deltaT = delta0 * Math.tanh(1.74 * Math.sqrt(Math.max(0, 1.0 / tRatio - 1.0)));

      // Split canvas: Left is BCS Gap Δ(T); Middle is Quasiparticle DOS N_s(E); Right is dI/dV Tunneling
      const subW = Math.floor((w - 80) / 3);

      // --- SUBPLOT 1: Δ(T) vs T/Tc ---
      const p1 = { x: 35, y: 35, w: subW, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(p1.x, p1.y, p1.w, p1.h);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText("BCS Gap Δ(T)/Δ(0) vs T/T_c", p1.x, p1.y - 12);

      // Trace BCS curve
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.2;
      for (let i = 0; i <= 50; i++) {
        const tr = i / 50;
        const gVal = tr < 1.0 ? Math.tanh(1.74 * Math.sqrt(1.0 / Math.max(0.01, tr) - 1.0)) : 0;
        const px = p1.x + tr * p1.w;
        const py = p1.y + p1.h - (gVal / 1.1) * (p1.h * 0.8) - 15;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current gap point
      const curP1x = p1.x + tRatio * p1.w;
      const curP1y = p1.y + p1.h - ((deltaT / delta0) / 1.1) * (p1.h * 0.8) - 15;
      ctx.beginPath(); ctx.arc(curP1x, curP1y, 6, 0, 2 * Math.PI);
      ctx.fillStyle = "#10b981"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

      // --- SUBPLOT 2: QUASIPARTICLE DENSITY OF STATES N_s(E) ---
      const p2 = { x: 35 + subW + 20, y: 35, w: subW, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(p2.x, p2.y, p2.w, p2.h);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 11px Inter";
      ctx.fillText("Quasiparticle DOS N_s(E) / N(0)", p2.x, p2.y - 12);

      const midE2 = p2.x + p2.w * 0.5;
      // Energy range from -2*delta0 to +2*delta0
      const maxE = 2.2 * delta0;

      ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.2;
      for (let i = 0; i <= 80; i++) {
        const E = -maxE + (2 * maxE * i) / 80;
        // Dynes formula for broadened BCS DOS: Re[ (E - iΓ) / sqrt((E - iΓ)² - Δ²) ]
        const absE = Math.abs(E);
        let dosVal = 0;
        if (absE > deltaT) {
          dosVal = absE / Math.sqrt(absE * absE - deltaT * deltaT + gamma * gamma);
        } else {
          dosVal = gamma / Math.sqrt(deltaT * deltaT - absE * absE + gamma * gamma);
        }
        const px = midE2 + (E / maxE) * (p2.w * 0.45);
        const py = p2.y + p2.h - Math.min(3.5, dosVal) / 3.8 * (p2.h * 0.85) - 10;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Shaded gap region
      const gapPxL = midE2 - (deltaT / maxE) * (p2.w * 0.45);
      const gapPxR = midE2 + (deltaT / maxE) * (p2.w * 0.45);
      ctx.fillStyle = "rgba(168, 85, 247, 0.12)";
      ctx.fillRect(gapPxL, p2.y + 20, gapPxR - gapPxL, p2.h - 35);
      ctx.fillStyle = "#c084fc"; ctx.font = "10px Inter";
      ctx.fillText("2Δ Gap", midE2 - 16, p2.y + p2.h * 0.45);

      // --- SUBPLOT 3: GIAEVER TUNNELING CONDUCTANCE dI/dV ---
      const p3 = { x: 35 + (subW + 20) * 2, y: 35, w: subW, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(p3.x, p3.y, p3.w, p3.h);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText("Giaever Tunneling Conductance dI/dV", p3.x, p3.y - 12);

      const midV3 = p3.x + p3.w * 0.5;
      ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.2;
      for (let i = 0; i <= 80; i++) {
        const eV_val = -maxE + (2 * maxE * i) / 80;
        const absV = Math.abs(eV_val);
        const cond = absV > deltaT ? absV / Math.sqrt(absV * absV - deltaT * deltaT + gamma * gamma) : 0.05;
        const px = midV3 + (eV_val / maxE) * (p3.w * 0.45);
        const py = p3.y + p3.h - Math.min(3.5, cond) / 3.8 * (p3.h * 0.85) - 10;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Readout Dashboard
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(p1.x, p1.y + p1.h - 50, w - 70, 45);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(p1.x, p1.y + p1.h - 50, w - 70, 45);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`T/T_c = ${tRatio.toFixed(2)}  |  Δ(0) = ${delta0.toFixed(2)} meV  |  2Δ(0)/k_B T_c = 3.53 (BCS Universal)`, p1.x + 15, p1.y + p1.h - 30);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Superconducting Gap Δ(T) = ${deltaT.toFixed(3)} meV  (Tunneling Threshold eV = ±Δ)`, p1.x + 15, p1.y + p1.h - 12);
    }
  },

  // 12. Josephson Effects, Shapiro Steps & DC SQUID Quantum Interference
  "ssp2-josephson-squid-sim": {
    title: "Josephson Junctions, Shapiro Voltage Steps & DC SQUID Interference",
    desc: "Rigorous RCSJ model and macroscopic phase difference dynamics. Visualizes DC Josephson supercurrent I = I_c sin(ϕ), microwave-induced Shapiro steps V_n = n ħω/2e, and DC SQUID flux modulation.",
    isAnimated: true,
    controls: [
      { id: "opMode", label: "Operation Mode", min: 0, max: 2, step: 1, value: 2 }, // 0: DC Josephson, 1: AC Shapiro Steps, 2: DC SQUID
      { id: "fluxPhi", label: "Magnetic Flux Φ / Φ₀", min: 0.0, max: 4.0, step: 0.1, value: 1.2 },
      { id: "biasCurrent", label: "Bias Current I / I_c", min: 0.0, max: 3.0, step: 0.1, value: 1.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const mode = vals.opMode !== undefined ? Math.round(vals.opMode) : 2;
      const fluxRatio = vals.fluxPhi !== undefined ? vals.fluxPhi : 1.2;
      const biasI = vals.biasCurrent !== undefined ? vals.biasCurrent : 1.5;

      const Ic = 1.0; // mA
      const Phi0 = 2.0678e-15; // Wb

      // Split canvas: Left is Physical Device / Loop; Right is Characteristic Curve
      const splitX = Math.floor(w * 0.48);

      // --- LEFT PLOT: DEVICE SCHEMATIC ---
      const devBox = { x: 35, y: 35, w: splitX - 55, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(devBox.x, devBox.y, devBox.w, devBox.h);

      if (mode === 2) {
        // DC SQUID: Superconducting ring with 2 Josephson junctions
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
        ctx.fillText("DC SQUID: Two Junctions Interrupted Loop", devBox.x, devBox.y - 12);

        const ringCx = devBox.x + devBox.w * 0.5;
        const ringCy = devBox.y + devBox.h * 0.45;
        const ringRad = 65;

        // Superconducting ring
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 14;
        ctx.beginPath(); ctx.arc(ringCx, ringCy, ringRad, 0, 2 * Math.PI); ctx.stroke();

        // Junction gaps (top and bottom)
        ctx.fillStyle = "#050811";
        ctx.fillRect(ringCx - 14, ringCy - ringRad - 10, 28, 20); // Top junction J1
        ctx.fillRect(ringCx - 14, ringCy + ringRad - 10, 28, 20); // Bottom junction J2

        // Barrier insulators (orange)
        ctx.fillStyle = "#f59e0b";
        ctx.fillRect(ringCx - 4, ringCy - ringRad - 8, 8, 16);
        ctx.fillRect(ringCx - 4, ringCy + ringRad - 8, 8, 16);

        ctx.fillStyle = "#f59e0b"; ctx.font = "10px Inter";
        ctx.fillText("J₁ (Barrier)", ringCx - 26, ringCy - ringRad - 14);
        ctx.fillText("J₂ (Barrier)", ringCx - 26, ringCy + ringRad + 24);

        // Magnetic Flux thread in center
        ctx.fillStyle = "rgba(168, 85, 247, 0.2)";
        ctx.beginPath(); ctx.arc(ringCx, ringCy, ringRad * 0.65, 0, 2 * Math.PI); ctx.fill();
        ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2; ctx.stroke();

        ctx.fillStyle = "#c084fc"; ctx.font = "bold 11px Inter";
        ctx.fillText(`Threaded Flux Φ = ${fluxRatio.toFixed(2)} Φ₀`, ringCx - 60, ringCy + 4);

        // Animated current loops
        const circulatingI = Math.sin(Math.PI * fluxRatio);
        const flowT = time * 3.0;
        ctx.fillStyle = "#10b981";
        for (let a = 0; a < 6; a++) {
          const ang = a * (Math.PI / 3) + flowT;
          const ax = ringCx + ringRad * Math.cos(ang);
          const ay = ringCy + ringRad * Math.sin(ang);
          ctx.beginPath(); ctx.arc(ax, ay, 3, 0, 2 * Math.PI); ctx.fill();
        }
      } else {
        // Single Josephson Junction
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
        ctx.fillText(mode === 0 ? "DC Josephson Effect: Supercurrent I = I_c sin(ϕ)" : "AC Shapiro Effect: Microwave Quantized Voltage Steps", devBox.x, devBox.y - 12);

        const jx = devBox.x + devBox.w * 0.5 - 60;
        const jy = devBox.y + devBox.h * 0.35;
        // Electrode 1
        ctx.fillStyle = "rgba(56, 189, 248, 0.3)"; ctx.fillRect(jx - 40, jy, 40, 50);
        ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(jx - 40, jy, 40, 50);
        // Insulator
        ctx.fillStyle = "#f59e0b"; ctx.fillRect(jx, jy, 16, 50);
        // Electrode 2
        ctx.fillStyle = "rgba(56, 189, 248, 0.3)"; ctx.fillRect(jx + 16, jy, 40, 50);
        ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(jx + 16, jy, 40, 50);

        ctx.fillStyle = "#f1f5f9"; ctx.font = "11px Inter";
        ctx.fillText("Superconductor", jx - 45, jy - 10);
        ctx.fillText("Insulator ~1nm", jx - 12, jy + 70);
      }

      // --- RIGHT PLOT: QUANTUM INTERFERENCE / CHARACTERISTIC CURVE ---
      const plotR = { x: splitX + 25, y: 35, w: w - splitX - 45, h: h - 70 };
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1; ctx.strokeRect(plotR.x, plotR.y, plotR.w, plotR.h);

      if (mode === 2) {
        // SQUID Interference Pattern: I_max(Phi) = 2 * Ic * |cos(pi * Phi / Phi0)|
        ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter";
        ctx.fillText("SQUID Critical Current Modulation: I_c(Φ) = 2I_c |cos(πΦ/Φ₀)|", plotR.x, plotR.y - 12);

        const maxPhi = 4.0;
        ctx.beginPath(); ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.4;
        for (let i = 0; i <= 80; i++) {
          const phiVal = (i / 80) * maxPhi;
          const iMaxVal = 2 * Ic * Math.abs(Math.cos(Math.PI * phiVal));
          const px = plotR.x + (phiVal / maxPhi) * plotR.w;
          const py = plotR.y + plotR.h - (iMaxVal / (2.2 * Ic)) * (plotR.h * 0.8) - 15;
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Operating dot
        const currImax = 2 * Ic * Math.abs(Math.cos(Math.PI * fluxRatio));
        const curPx = plotR.x + (fluxRatio / maxPhi) * plotR.w;
        const curPy = plotR.y + plotR.h - (currImax / (2.2 * Ic)) * (plotR.h * 0.8) - 15;
        ctx.beginPath(); ctx.arc(curPx, curPy, 6, 0, 2 * Math.PI);
        ctx.fillStyle = "#10b981"; ctx.fill(); ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();

        // Flux ticks
        for (let n = 0; n <= 4; n++) {
          const tx = plotR.x + (n / maxPhi) * plotR.w;
          ctx.strokeStyle = "#334155"; ctx.beginPath(); ctx.moveTo(tx, plotR.y + plotR.h - 5); ctx.lineTo(tx, plotR.y + plotR.h); ctx.stroke();
          ctx.fillStyle = "#64748b"; ctx.font = "9px Inter"; ctx.fillText(`${n}Φ₀`, tx - 8, plotR.y + plotR.h + 12);
        }
      } else if (mode === 1) {
        // Shapiro Voltage Steps: I-V curve with steps at V_n = n * hf / 2e
        ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter";
        ctx.fillText("Shapiro Steps I-V Curve: Quantized V_n = n ħω / 2e", plotR.x, plotR.y - 12);

        // Step staircase
        ctx.beginPath(); ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.2;
        const vStepW = plotR.w / 5;
        ctx.moveTo(plotR.x + 10, plotR.y + plotR.h - 15);
        for (let n = 0; n <= 4; n++) {
          const vx = plotR.x + (n + 0.5) * vStepW;
          const vy = plotR.y + plotR.h - (n + 1) * (plotR.h * 0.18) - 10;
          ctx.lineTo(vx, vy);
          ctx.lineTo(vx + vStepW * 0.8, vy);
        }
        ctx.stroke();

        ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter";
        ctx.fillText("Voltage Standards (Metrology)", plotR.x + 20, plotR.y + 30);
      } else {
        // DC Josephson I = Ic sin(phi)
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter";
        ctx.fillText("Current-Phase Relation: I(ϕ) = I_c sin(ϕ)", plotR.x, plotR.y - 12);

        ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.2;
        for (let i = 0; i <= 60; i++) {
          const phiVal = -Math.PI + (2 * Math.PI * i) / 60;
          const ival = Ic * Math.sin(phiVal);
          const px = plotR.x + (i / 60) * plotR.w;
          const py = plotR.y + plotR.h * 0.5 - (ival / 1.2) * (plotR.h * 0.4);
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      // Telemetry info panel
      const bY = plotR.y + plotR.h - 55;
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(plotR.x + 10, bY, plotR.w - 20, 48);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(plotR.x + 10, bY, plotR.w - 20, 48);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter";
      ctx.fillText(`Flux Φ = ${fluxRatio.toFixed(2)} Φ₀  |  I_c0 = ${Ic.toFixed(1)} mA`, plotR.x + 20, bY + 18);
      const curMaxI = 2 * Ic * Math.abs(Math.cos(Math.PI * fluxRatio));
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter";
      ctx.fillText(`Maximum Interference Supercurrent: ${curMaxI.toFixed(3)} mA`, plotR.x + 20, bY + 36);
    }
  }
