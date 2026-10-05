# Update statmech-sims.js with dedicated simulations and aliases

with open('statmech-sims.js') as f:
    content = f.read()

new_sims = r'''
  // 23. Stirling's Approximation Convergence Sandbox
  "entropy-stirling-sim": {
    title: "📐 Stirling's Approximation & Factorial Asymptotics",
    desc: "Compare exact combinatorial factorials ln(N!) against Stirling leading and second-order asymptotic formulas as N scales.",
    isAnimated: false,
    controls: [
      { id: "stirling-n", label: "Number N", min: 2, max: 80, step: 1, value: 20 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const N = vals["stirling-n"];
      
      let exactLnFact = 0;
      for (let i = 1; i <= N; i++) exactLnFact += Math.log(i);
      const leadingStirling = N * Math.log(N) - N;
      const secondStirling = N * Math.log(N) - N + 0.5 * Math.log(2 * Math.PI * N);
      const errLeading = Math.abs((leadingStirling - exactLnFact) / exactLnFact) * 100;
      const errSecond = Math.abs((secondStirling - exactLnFact) / exactLnFact) * 100;

      // Draw Comparison Cards
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(40, 50, 310, 120);
      ctx.fillRect(370, 50, 310, 120);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px monospace";
      ctx.fillText("Exact ln(N!) vs Leading Stirling:", 55, 75);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Exact ln(${N}!):   ` + exactLnFact.toFixed(4), 55, 105);
      ctx.fillText(`N ln N - N:      ` + leadingStirling.toFixed(4), 55, 130);
      ctx.fillStyle = "#ec4899";
      ctx.fillText(`Relative Error:  ` + errLeading.toFixed(3) + " %", 55, 155);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 14px monospace";
      ctx.fillText("Second-Order Stirling Correction:", 385, 75);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Formula: N ln N - N + 0.5 ln(2πN)`, 385, 105);
      ctx.fillText(`Corrected Value: ` + secondStirling.toFixed(4), 385, 130);
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Relative Error:  ` + errSecond.toFixed(4) + " %", 385, 155);

      // Plot error curves across N = 2 to 60
      const originX = 60, originY = h - 40, plotW = w - 100, plotH = 90;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(originX, originY); ctx.lineTo(originX + plotW, originY);
      ctx.moveTo(originX, originY); ctx.lineTo(originX, originY - plotH);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Relative Error (%) vs N", originX + 10, originY - plotH + 12);
      ctx.fillText("N = 2", originX, originY + 18);
      ctx.fillText("N = 60", originX + plotW - 35, originY + 18);

      // Plot leading error curve (pink)
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2; ctx.beginPath();
      for (let n = 2; n <= 60; n++) {
        let exact = 0; for (let i = 1; i <= n; i++) exact += Math.log(i);
        let approx = n * Math.log(n) - n;
        let err = Math.abs((approx - exact) / exact) * 100;
        let x = originX + ((n - 2) / 58) * plotW;
        let y = originY - Math.min(plotH - 5, (err / 30) * (plotH - 10));
        if (n === 2) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Plot second order error curve (green)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.beginPath();
      for (let n = 2; n <= 60; n++) {
        let exact = 0; for (let i = 1; i <= n; i++) exact += Math.log(i);
        let approx = n * Math.log(n) - n + 0.5 * Math.log(2 * Math.PI * n);
        let err = Math.abs((approx - exact) / exact) * 100;
        let x = originX + ((n - 2) / 58) * plotW;
        let y = originY - Math.min(plotH - 5, (err / 30) * (plotH - 10));
        if (n === 2) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = "#ec4899"; ctx.fillText("■ Leading Term N ln N - N", originX + 220, originY - plotH + 12);
      ctx.fillStyle = "#10b981"; ctx.fillText("■ + 0.5 ln(2πN)", originX + 440, originY - plotH + 12);
    }
  },

  // 24. Liquid Helium Lambda Transition Specific Heat
  "liquid-helium-lambda-sim": {
    title: "🌡️ Liquid Helium-4 Lambda Point Specific Heat Logarithmic Cusp",
    desc: "Inspect the famous heat capacity lambda-peak of Liquid Helium-4 transitioning from normal He-I to frictionless superfluid He-II at T_lambda = 2.17 K.",
    isAnimated: false,
    controls: [
      { id: "lambda-t", label: "Temperature T (Kelvin)", min: 1.0, max: 3.5, step: 0.05, value: 2.17 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const T = vals["lambda-t"];
      const ox = 70, oy = h - 50, pw = w - 120, ph = h - 100;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + pw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - ph);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Temperature T (K)", ox + pw / 2 - 40, oy + 35);
      ctx.fillText("Specific Heat C_p / R", 10, oy - ph - 10);

      const tLam = 2.17;
      const xLam = ox + ((tLam - 1.0) / 2.5) * pw;
      ctx.strokeStyle = "#e11d48"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(xLam, oy); ctx.lineTo(xLam, oy - ph); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e";
      ctx.fillText("T_λ = 2.17 K", xLam - 28, oy - ph + 20);

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let temp = 1.0; temp <= 3.5; temp += 0.01) {
        const diff = Math.max(0.005, Math.abs(temp - tLam));
        let cp = 1.2 - 0.75 * Math.log(diff);
        if (temp > tLam) cp *= 0.65;
        const x = ox + ((temp - 1.0) / 2.5) * pw;
        const y = oy - Math.min(ph - 5, (cp / 5.5) * ph);
        if (temp === 1.0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      const curDiff = Math.max(0.005, Math.abs(T - tLam));
      let curCp = 1.2 - 0.75 * Math.log(curDiff);
      if (T > tLam) curCp *= 0.65;
      const curX = ox + ((T - 1.0) / 2.5) * pw;
      const curY = oy - Math.min(ph - 5, (curCp / 5.5) * ph);

      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#1e293b"; ctx.fillRect(w - 280, 40, 240, 80);
      ctx.fillStyle = T < tLam ? "#10b981" : "#38bdf8";
      ctx.font = "bold 14px monospace";
      ctx.fillText(T < tLam ? "Phase: Liquid He-II (Superfluid)" : "Phase: Liquid He-I (Normal Liquid)", w - 265, 68);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "12px monospace";
      ctx.fillText(`T = ${T.toFixed(2)} K | C_p/R ≈ ${curCp.toFixed(2)}`, w - 265, 95);
    }
  },

  // 25. Superfluid Two-Fluid Hydrodynamics & Fountain Effect (ANIMATED)
  "superfluid-two-fluid-sim": {
    title: "🌊 Superfluid Two-Fluid Flow & Thermal Fountain Effect",
    desc: "Watch the frictionless superfluid component flow through a fine porous plug when heated, building macroscopic fountain pressure.",
    isAnimated: true,
    controls: [
      { id: "sf-power", label: "Heater Power (mW)", min: 10, max: 100, step: 5, value: 40 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const power = vals["sf-power"];
      const fHeight = (power / 100) * 120;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.strokeRect(180, 160, 360, 140);
      ctx.strokeRect(340, 100, 40, 150);

      ctx.fillStyle = "#475569";
      ctx.fillRect(342, 230, 36, 30);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("Porous Plug", 328, 275);

      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      ctx.fillRect(182, 190, 356, 108);

      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(350, 215); ctx.lineTo(370, 215);
      ctx.lineTo(350, 220); ctx.lineTo(370, 220);
      ctx.stroke();
      ctx.fillStyle = "#ef4444"; ctx.font = "10px sans-serif"; ctx.fillText("Heater", 385, 220);

      const jetBaseX = 360, jetBaseY = 100;
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(jetBaseX, jetBaseY);
      ctx.lineTo(jetBaseX, jetBaseY - fHeight);
      ctx.stroke();

      ctx.fillStyle = "#38bdf8";
      for (let i = 0; i < 16; i++) {
        const phase = (animTime * 3 + i * 0.4) % 1;
        const dx = (Math.sin(i * 1.5) * 25) * phase;
        const dy = -fHeight * (1 - phase) + phase * phase * 20;
        ctx.beginPath();
        ctx.arc(jetBaseX + dx, jetBaseY + dy, 2.5, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.fillStyle = "#10b981";
      for (let i = 0; i < 20; i++) {
        const py = 290 - ((animTime * 60 + i * 18) % 60);
        const px = 345 + (i % 4) * 8;
        ctx.beginPath(); ctx.arc(px, py, 2, 0, Math.PI * 2); ctx.fill();
      }

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px monospace";
      ctx.fillText(`Allen & Jones Thermomechanical Fountain Effect (T < 2.17 K)`, 40, 40);
      ctx.fillStyle = "#10b981"; ctx.font = "12px monospace";
      ctx.fillText("↑ Frictionless Superfluid Component (ρ_s) rushes in", 40, 70);
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`Fountain Height: ${(fHeight * 0.25).toFixed(1)} cm | Thermo-osmotic Pressure ΔP = ρ S ΔT`, 40, 95);
    }
  },

  // 26. Bose Gas Momentum Distribution Sharpening (ANIMATED)
  "bose-gas-momentum-distribution-sim": {
    title: "📉 Bose-Einstein Condensate Momentum Distribution Collapse",
    desc: "Witness the real-time sharpening of momentum distribution as T drops across T_c into an ultra-narrow macroscopic zero-momentum spike.",
    isAnimated: true,
    controls: [
      { id: "bec-t-ratio", label: "Reduced Temperature T / T_c", min: 0.1, max: 2.0, step: 0.05, value: 0.8 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const tratio = vals["bec-t-ratio"];
      const ox = w / 2, base = h - 60;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(ox - 260, base); ctx.lineTo(ox + 260, base);
      ctx.moveTo(ox, base); ctx.lineTo(ox, 40);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("-p_max", ox - 260, base + 20);
      ctx.fillText("+p_max", ox + 220, base + 20);
      ctx.fillText("Momentum Distribution n(p)", ox + 15, 55);

      const thermSigma = 70 * Math.sqrt(tratio);
      const thermAmp = Math.min(90, 80 / tratio);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = -250; px <= 250; px += 2) {
        const val = thermAmp * Math.exp(-(px * px) / (2 * thermSigma * thermSigma));
        const x = ox + px, y = base - val;
        if (px === -250) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      if (tratio < 1.0) {
        const condFrac = 1.0 - Math.pow(tratio, 1.5);
        const peakHeight = condFrac * 180 + Math.sin(animTime * 3) * 5;
        const peakSigma = 8;

        ctx.fillStyle = "rgba(236, 72, 153, 0.35)";
        ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 3;
        ctx.beginPath();
        for (let px = -40; px <= 40; px += 1) {
          const val = peakHeight * Math.exp(-(px * px) / (2 * peakSigma * peakSigma));
          const x = ox + px, y = base - val;
          if (px === -40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.lineTo(ox + 40, base); ctx.lineTo(ox - 40, base);
        ctx.closePath();
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#ec4899"; ctx.font = "bold 13px monospace";
        ctx.fillText(`BEC Condensate Ground-State Spike (N_0/N = ${(condFrac * 100).toFixed(1)}%)`, ox - 180, base - peakHeight - 15);
      }

      ctx.fillStyle = "#f8fafc"; ctx.font = "12px monospace";
      ctx.fillText(`T/T_c = ${tratio.toFixed(2)} | ` + (tratio < 1 ? "Condensed Regime (Quantum Matter Wave)" : "Normal Thermal Gas (Broad Gaussian Distribution)"), 40, 35);
    }
  },

  // 27. Clausius-Clapeyron Phase Coexistence Diagram
  "phase-diagram-clapeyron-sim": {
    title: "⚗️ Clausius-Clapeyron Coexistence Boundaries & Phase Diagram",
    desc: "Interactive P-T phase boundaries (Solid, Liquid, Gas) demonstrating Clausius-Clapeyron slope dP/dT = L / (T ΔV), the triple point, and critical point.",
    isAnimated: false,
    controls: [
      { id: "cc-latent", label: "Latent Heat Scaling", min: 0.5, max: 2.0, step: 0.1, value: 1.0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const lat = vals["cc-latent"];
      const ox = 70, oy = h - 60, pw = w - 120, ph = h - 110;

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(ox, oy); ctx.lineTo(ox + pw, oy);
      ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - ph);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
      ctx.fillText("Temperature T →", ox + pw - 90, oy + 35);
      ctx.fillText("Pressure P →", ox - 50, oy - ph + 10);

      const tpx = ox + 0.32 * pw, tpy = oy - 0.38 * ph;

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(ox, oy);
      ctx.quadraticCurveTo(ox + 0.18 * pw, oy - 0.15 * ph, tpx, tpy);
      ctx.stroke();

      const cpx = ox + 0.85 * pw, cpy = oy - 0.88 * ph;
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(tpx, tpy);
      ctx.quadraticCurveTo(ox + 0.55 * pw, oy - 0.55 * ph * lat, cpx, cpy);
      ctx.stroke();

      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(tpx, tpy);
      ctx.lineTo(tpx - 15, oy - ph);
      ctx.stroke();

      ctx.font = "bold 15px monospace";
      ctx.fillStyle = "#93c5fd"; ctx.fillText("SOLID (Ice)", ox + 0.08 * pw, oy - 0.65 * ph);
      ctx.fillStyle = "#6ee7b7"; ctx.fillText("LIQUID (Water)", ox + 0.42 * pw, oy - 0.70 * ph);
      ctx.fillStyle = "#fde047"; ctx.fillText("GAS (Vapor)", ox + 0.55 * pw, oy - 0.22 * ph);

      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(tpx, tpy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f59e0b"; ctx.font = "12px monospace"; ctx.fillText("Triple Point (0.01°C, 611 Pa)", tpx + 10, tpy + 5);

      ctx.fillStyle = "#ef4444"; ctx.beginPath(); ctx.arc(cpx, cpy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#ef4444"; ctx.font = "12px monospace"; ctx.fillText("Critical Point (374°C, 22.1 MPa)", cpx - 120, cpy - 12);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "13px monospace";
      ctx.fillText("Clausius-Clapeyron: dP/dT = L / [T(V_2 - V_1)] | Negative melting slope for H_2O (V_ice > V_liq)", ox, h - 15);
    }
  },

  // 28. Transport Coefficients Sandbox
  "transport-coefficients-sim": {
    title: "🚚 Kinetic Transport: Viscosity, Thermal Conductivity & Diffusion",
    desc: "Inspect how gas viscosity η, thermal conductivity κ, and diffusion coefficient D respond to changes in temperature and pressure.",
    isAnimated: false,
    controls: [
      { id: "tc-temp", label: "Temperature (K)", min: 100, max: 800, step: 25, value: 300 },
      { id: "tc-press", label: "Pressure (atm)", min: 0.2, max: 5.0, step: 0.2, value: 1.0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18"; ctx.fillRect(0, 0, w, h);

      const T = vals["tc-temp"];
      const P = vals["tc-press"];

      const eta = 1.78e-5 * Math.sqrt(T / 300);
      const kappa = 0.026 * Math.sqrt(T / 300);
      const diff = 2.05e-5 * Math.pow(T / 300, 1.5) / P;
      const mfp = 68 * (T / 300) / P;

      const cardW = 190, cardH = 180, cardY = 60;
      
      ctx.fillStyle = "#1e293b"; ctx.fillRect(30, cardY, cardW, cardH);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px monospace";
      ctx.fillText("Viscosity (η)", 45, cardY + 30);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Value: ${(eta * 1e5).toFixed(2)} μPa·s`, 45, cardY + 65);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Scaling: η ∝ √T", 45, cardY + 95);
      ctx.fillText("Pressure: INDEPENDENT", 45, cardY + 120);
      ctx.fillStyle = "#10b981"; ctx.fillText("✓ Maxwell's Law verified", 45, cardY + 150);

      ctx.fillStyle = "#1e293b"; ctx.fillRect(250, cardY, cardW, cardH);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 14px monospace";
      ctx.fillText("Thermal Cond (κ)", 265, cardY + 30);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Value: ${(kappa * 1e3).toFixed(1)} mW/(m·K)`, 265, cardY + 65);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Scaling: κ ∝ √T", 265, cardY + 95);
      ctx.fillText("Pressure: INDEPENDENT", 265, cardY + 120);
      ctx.fillStyle = "#10b981"; ctx.fillText("✓ Kinetic transport", 265, cardY + 150);

      ctx.fillStyle = "#1e293b"; ctx.fillRect(470, cardY, cardW, cardH);
      ctx.fillStyle = "#ec4899"; ctx.font = "bold 14px monospace";
      ctx.fillText("Self-Diffusion (D)", 485, cardY + 30);
      ctx.fillStyle = "#f8fafc"; ctx.font = "13px monospace";
      ctx.fillText(`Value: ${(diff * 1e5).toFixed(2)} × 10⁻⁵ m²/s`, 485, cardY + 65);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("Scaling: D ∝ T^1.5 / P", 485, cardY + 95);
      ctx.fillText(`Mean Free Path: ${mfp.toFixed(1)} nm`, 485, cardY + 120);
      ctx.fillStyle = "#ec4899"; ctx.fillText("Inversely prop to pressure", 485, cardY + 150);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "13px monospace";
      ctx.fillText(`T = ${T} K | P = ${P.toFixed(1)} atm | Hard-sphere diameter d = 3.7 Å (Diatomic Nitrogen)`, 40, h - 35);
    }
  }
'''

idx = content.find('// Universal Engine Integration Adapter')
if idx == -1:
    idx = content.find('window.SimulationEngine =')

before = content[:idx].rstrip()
if before.endswith('};'):
    before = before[:-2] + ','

aliases = '''
// Aliases for seamless universal integration
window.STATMECH_SIMS["liouville-phase-space-sim"] = window.STATMECH_SIMS["phase-space-trajectory-sim"];
window.STATMECH_SIMS["canonical-boltzmann-sim"] = window.STATMECH_SIMS["canonical-ensemble-partition-sim"];
window.STATMECH_SIMS["equipartition-dof-sim"] = window.STATMECH_SIMS["diatomic-molecule-degrees-sim"];
window.STATMECH_SIMS["quantum-wavefunction-symmetry-sim"] = window.STATMECH_SIMS["identical-particles-exchange-sim"];
window.STATMECH_SIMS["three-statistics-comparison-sim"] = window.STATMECH_SIMS["quantum-distributions-compare-sim"];
window.STATMECH_SIMS["fermi-dirac-step-sim"] = window.STATMECH_SIMS["fermi-dirac-distribution-sim"];
window.STATMECH_SIMS["fermi-surface-sphere-sim"] = window.STATMECH_SIMS["fermi-sphere-3d-sim"];
window.STATMECH_SIMS["white-dwarf-chandrasekhar-sim"] = window.STATMECH_SIMS["white-dwarf-degeneracy-sim"];
window.STATMECH_SIMS["planck-blackbody-spectrum-sim"] = window.STATMECH_SIMS["planck-blackbody-radiation-sim"];
window.STATMECH_SIMS["debye-vs-einstein-cv-sim"] = window.STATMECH_SIMS["debye-einstein-heat-capacity-sim"];
window.STATMECH_SIMS["mean-free-path-transport-sim"] = window.STATMECH_SIMS["mean-free-path-viscosity-sim"];
window.STATMECH_SIMS["ising-model-monte-carlo-sim"] = window.STATMECH_SIMS["ising-model-phase-transition-sim"];
'''

after = content[idx:]

updated_content = before + new_sims + '\n};\n' + aliases + '\n' + after

with open('statmech-sims.js', 'w') as f:
    f.write(updated_content)

print('statmech-sims.js updated successfully with all 28 simulations and universal aliases!')
